"""Dữ liệu bài học SGK Toán Lớp 4 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 4 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 4

LESSONS = [{'topic': 'l4-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 4 · Chủ đề 1: Ôn tập các số đến 100 000; số chẵn, số lẻ; biểu thức chứa chữ; bài toán '
             '3 bước tính.',
  'title': 'Bài 1: Ôn tập các số đến 100 000',
  'icon': '🔢',
  'description': 'Củng cố đọc, viết, phân tích cấu tạo thập phân, so sánh và làm tròn các số trong phạm vi '
                 '100 000.',
  'requirements': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                   'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                   'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
  'definition': '- Số có năm chữ số gồm các hàng: **chục nghìn, nghìn, trăm, chục, đơn vị**: '
                '$\\overline{abcde} = a \\times 10\\,000 + b \\times 1\\,000 + c \\times 100 + d \\times 10 '
                '+ e$.\n'
                '- Khi so sánh hai số, số có nhiều chữ số hơn thì lớn hơn; nếu cùng số chữ số thì so sánh '
                'từng hàng từ trái sang phải.',
  'theory': '### 1. Đọc, viết và phân tích số\n'
            '- Ví dụ: $65\\,308 = 60\\,000 + 5\\,000 + 300 + 8$ đọc là "sáu mươi lăm nghìn ba trăm linh '
            'tám".\n'
            '### 2. So sánh và làm tròn số\n'
            '- Làm tròn đến hàng nghìn: xét chữ số hàng trăm ($< 5$ xuống, $\\ge 5$ lên).\n'
            '- Làm tròn đến hàng chục nghìn: xét chữ số hàng nghìn ($< 5$ xuống, $\\ge 5$ lên).',
  'formulas': [{'category': 'I. Cấu tạo thập phân',
                'items': [{'name': 'Phân tích số',
                           'formula': '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'}]},
               {'category': 'II. Làm tròn số',
                'items': [{'name': 'Quy tắc 5',
                           'formula': 'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge '
                                      '5 \\rightarrow$ lên'}]}],
  'example': 'Cho số $74\\,629$. Hãy nêu giá trị của chữ số $4$ và làm tròn số đó đến hàng nghìn.',
  'example_answer': 'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**.\n'
                    'Vì chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**.',
  'real_life': '- Đọc số tiền trên hóa đơn mua hàng, số dân của một phường/xã.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $83\\,542$, chữ số $3$ có giá trị là:',
            'options': ['$3\\,000$', '$300$', '$30\\,000$', '$3$'],
            'answer': 0,
            'solution': 'Chữ số $3$ đứng ở hàng nghìn nên có giá trị là **$3\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số gồm $5$ chục nghìn, $7$ trăm và $4$ đơn vị được viết là:',
            'options': ['$5\\,704$', '$50\\,704$', '$57\\,004$', '$50\\,740$'],
            'answer': 1,
            'solution': 'Ta có $50\\,000 + 700 + 4 = 50\\,704$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Ôn tập các số đến 100 000**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Phân tích số**?',
            'options': ['Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ ($0 < '
                        'r < b$)'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Ôn tập các số đến 100 000, **Phân tích '
                        'số** được xác định bởi: $\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Ôn tập các số đến 100 000**, nội dung/biểu thức Chữ số ngay bên phải hàng '
                 'làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Phân tích số', 'Quy tắc', 'Chia có dư', 'Quy tắc 5'],
            'answer': 3,
            'solution': 'Trong Bài 1: Ôn tập các số đến 100 000, biểu thức/quy tắc Chữ số ngay bên phải hàng '
                        'làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 \\rightarrow$ lên chính là nội dung '
                        'của **Quy tắc 5**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Làm tròn số $38\\,520$ đến hàng nghìn ta được:',
            'options': ['$39\\,000$', '$38\\,000$', '$40\\,000$', '$38\\,500$'],
            'answer': 0,
            'solution': 'Chữ số hàng trăm là $5 \\ge 5$ nên làm tròn lên đến hàng nghìn được **$39\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Ôn tập các số đến 100 000** (Chủ đề 1: Ôn tập và bổ sung), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đặt tính và tính đúng bốn phép tính cộng, trừ, nhân, chia trong phạm vi '
                        '$100\\,000$.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Tính đúng giá trị biểu thức số và tìm thành phần chưa biết.',
                        'Giải được bài toán thực tế có hai bước tính.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Ôn tập các số đến 100 000: Đọc, viết, nêu giá trị '
                        'các chữ số theo hàng của số trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số lớn nhất có năm chữ số khác nhau là $99\\,999$."',
            'answer': False,
            'solution': 'Số $99\\,999$ có các chữ số giống nhau; số lớn nhất có năm chữ số khác nhau phải là '
                        '$98\\,765$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 1: Ôn tập các số đến 100 000**, quy tắc **Phân tích số** được xác định bởi '
                 '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$ và áp dụng trực tiếp vào bài toán: '
                 '“Cho số $74\\,629$. Hãy nêu giá trị của chữ số $4$ và làm tròn số đó đến hàng nghìn.”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Phân tích số** ($\\overline{abcde} = a0\\,000 + '
                        'b\\,000 + c00 + d0 + e$) là kiến thức cốt lõi của Bài 1: Ôn tập các số đến 100 000. '
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn đượ...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Ôn tập các số đến 100 000** để giải quyết tình huống sau: Cho '
                 'số $74\\,629$. Hãy nêu giá trị của chữ số $4$ và làm tròn số đó đến hàng nghìn. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thay $a = 12, b = 5, c = 40$ vào biểu thức ta được: $12 \\times 5 + 40 = 60 + 40 = '
                        '100$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Ôn tập các số đến 100 000: Trong số $74\\,629$, chữ '
                        'số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**.\n'
                        'Vì chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tròn chục nghìn liền sau của số $62\\,450$ (viết số liền).',
            'answer': ['70000'],
            'unit': None,
            'solution': 'Số $62\\,450$ nằm giữa $60\\,000$ và $70\\,000$ nên số tròn chục nghìn liền sau là '
                        '**$70000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 4 · Chủ đề 1: Ôn tập các số đến 100 000; số chẵn, số lẻ; biểu thức chứa chữ; bài toán '
             '3 bước tính.',
  'title': 'Bài 2: Ôn tập các phép tính trong phạm vi 100 000',
  'icon': '🧮',
  'description': 'Ôn tập cộng, trừ, nhân, chia và tính giá trị biểu thức số trong phạm vi 100 000.',
  'requirements': ['Đặt tính và tính đúng bốn phép tính cộng, trừ, nhân, chia trong phạm vi $100\\,000$.',
                   'Tính đúng giá trị biểu thức số và tìm thành phần chưa biết.',
                   'Giải được bài toán thực tế có hai bước tính.'],
  'definition': '- **Cộng, trừ, nhân**: đặt tính thẳng cột, thực hiện từ phải sang trái.\n'
                '- **Chia**: thực hiện từ trái sang phải (từ hàng cao nhất), ở mỗi lượt: chia $\\rightarrow$ '
                'nhân $\\rightarrow$ trừ $\\rightarrow$ hạ.\n'
                '- **Biểu thức số**: trong ngoặc trước $\\rightarrow$ nhân, chia $\\rightarrow$ cộng, trừ.',
  'theory': '### 1. Ôn tập bốn phép tính\n'
            '- Phép cộng và trừ: chú ý các lượt nhớ.\n'
            '- Phép nhân và chia với số có một chữ số: chú ý viết chữ số $0$ ở thương khi lượt chia bé hơn '
            'số chia.\n'
            '### 2. Tìm thành phần chưa biết\n'
            '- Số hạng $= \\text{Tổng} - \\text{Số hạng kia}$; Số bị chia $= \\text{Thương} \\times '
            '\\text{Số chia}$.',
  'formulas': [{'category': 'I. Thứ tự thực hiện phép tính',
                'items': [{'name': 'Quy tắc', 'formula': '$() \\rightarrow \\times, : \\rightarrow +, -$'}]},
               {'category': 'II. Quan hệ phép tính',
                'items': [{'name': 'Chia có dư',
                           'formula': '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + '
                                      '\\text{Số dư}$ ($0 < r < b$)'}]}],
  'example': 'Tính giá trị của biểu thức: $65\\,000 - 12\\,000 \\times 4$.',
  'example_answer': 'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$.\n'
                    'Thực hiện phép trừ sau: $65\\,000 - 48\\,000 = 17\\,000$.',
  'real_life': '- Tính tiền mua nhiều món đồ dùng học tập và số tiền còn dư.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $15\\,000 \\times 4$ là:',
            'options': ['$45\\,000$', '$60\\,000$', '$50\\,000$', '$19\\,000$'],
            'answer': 1,
            'solution': 'Nhẩm: $15$ nghìn $\\times 4 = 60$ nghìn $= 60\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $48\\,024 : 6$ là:',
            'options': ['$804$', '$8\\,040$', '$8\\,004$', '$840$'],
            'answer': 2,
            'solution': 'Ta có $48 : 6 = 8$, hạ $0 \\rightarrow 0$, hạ $2 < 6 \\rightarrow 0$, hạ $4$ được '
                        '$24 : 6 = 4 \\rightarrow 8\\,004$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Ôn tập các phép tính trong phạm vi 100 000**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Quy tắc**?',
            'options': ['$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ ($0 < '
                        'r < b$)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Ôn tập các phép tính trong phạm vi 100 '
                        '000, **Quy tắc** được xác định bởi: $() \\rightarrow \\times, : \\rightarrow +, '
                        '-$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Ôn tập các phép tính trong phạm vi 100 000**, nội dung/biểu thức $\\text{Số '
                 'bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ ($0 < r < b$) là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Chia có dư', 'Quy tắc', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 2: Ôn tập các phép tính trong phạm vi 100 000, biểu thức/quy tắc '
                        '$\\text{Số bị chia} = \\text{Thương} \\times \\text{Số chia} + \\text{Số dư}$ ($0 < '
                        'r < b$) chính là nội dung của **Chia có dư**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $(24\\,000 + 16\\,000) : 8$ là:',
            'options': ['$26\\,000$', '$5\\,000$', '$4\\,000$', '$500$'],
            'answer': 1,
            'solution': 'Tính trong ngoặc trước: $40\\,000 : 8 = 5\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Ôn tập các phép tính trong phạm vi 100 000** (Chủ đề 1: Ôn tập và bổ '
                 'sung), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Đặt tính và tính đúng bốn phép tính cộng, trừ, nhân, chia trong phạm vi '
                        '$100\\,000$.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Ôn tập các phép tính trong phạm vi 100 000: Đặt '
                        'tính và tính đúng bốn phép tính cộng, trừ, nhân, chia trong phạm vi $100\\,000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $50\\,000 - 10\\,000 : 5$ là $8\\,000$."',
            'answer': False,
            'solution': 'Chia trước: $10\\,000 : 5 = 2\\,000$; sau đó $50\\,000 - 2\\,000 = 48\\,000$, không '
                        'phải $8\\,000$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 2: Ôn tập các phép tính trong phạm vi 100 000**, quy tắc **Quy tắc** được xác '
                 'định bởi $() \\rightarrow \\times, : \\rightarrow +, -$ và áp dụng trực tiếp vào bài toán: '
                 '“Tính giá trị của biểu thức: $65\\,000 - 12\\,000 \\times 4$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy tắc** ($() \\rightarrow \\times, : \\rightarrow '
                        '+, -$) là kiến thức cốt lõi của Bài 2: Ôn tập các phép tính trong phạm vi 100 000. '
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Ôn tập các phép tính trong phạm vi 100 000** để giải quyết '
                 'tình huống sau: Tính giá trị của biểu thức: $65\\,000 - 12\\,000 \\times 4$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Thay $a = 12, b = 5, c = 40$ vào biểu thức ta được: $12 \\times 5 + 40 = 60 + 40 = '
                        '100$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Ôn tập các phép tính trong phạm vi 100 000: Thực hiện '
                        'phép nhân trước: $12\\,000 \\times 4 = 48\\,000$.\n'
                        'Thực hiện phép trừ sau: $65\\,000 - 48\\,000 = 17\\,000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mua $5$ hộp bánh như nhau hết $95\\,000$ đồng. Hỏi mỗi hộp bánh giá bao nhiêu đồng (viết '
                 'số liền)?',
            'answer': ['19000'],
            'unit': 'đồng',
            'solution': 'Giá tiền mỗi hộp bánh là: $95\\,000 : 5 = 19\\,000\\text{ (đồng)}$.\n'
                        'Đáp số: **$19000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 4 · Chủ đề 1: Ôn tập các số đến 100 000; số chẵn, số lẻ; biểu thức chứa chữ; bài toán '
             '3 bước tính.',
  'title': 'Bài 3: Số chẵn, số lẻ',
  'icon': '⚖️',
  'description': 'Nhận biết dấu hiệu của số chẵn, số lẻ và quy luật hai số chẵn (hoặc hai số lẻ) liên tiếp.',
  'requirements': ['Nhận biết được số chẵn (tận cùng là $0, 2, 4, 6, 8$) và số lẻ (tận cùng là $1, 3, 5, 7, '
                   '9$).',
                   'Hiểu số chẵn là số chia hết cho $2$, số lẻ là số không chia hết cho $2$.',
                   'Biết hai số chẵn (hoặc hai số lẻ) liên tiếp hơn kém nhau $2$ đơn vị.'],
  'definition': '- **Số chẵn** là các số có chữ số tận cùng (hàng đơn vị) là **$0, 2, 4, 6, 8$** (chia hết '
                'cho $2$).\n'
                '- **Số lẻ** là các số có chữ số tận cùng (hàng đơn vị) là **$1, 3, 5, 7, 9$** (chia cho $2$ '
                'dư $1$).\n'
                '- Hai số chẵn liên tiếp (hoặc hai số lẻ liên tiếp) hơn kém nhau **$2$ đơn vị**.',
  'theory': '### 1. Cách nhận biết nhanh số chẵn, số lẻ\n'
            '- Chỉ cần nhìn vào **chữ số tận cùng** (hàng đơn vị), không phụ thuộc các chữ số đứng trước.\n'
            '- Ví dụ: $13\\,578$ có tận cùng là $8$ nên là **số chẵn**; $24\\,685$ có tận cùng là $5$ nên là '
            '**số lẻ**.\n'
            '### 2. Tính chất cộng, trừ chẵn – lẻ\n'
            '- $\\text{Chẵn} + \\text{Chẵn} = \\text{Chẵn}$; $\\text{Lẻ} + \\text{Lẻ} = \\text{Chẵn}$; '
            '$\\text{Chẵn} + \\text{Lẻ} = \\text{Lẻ}$.',
  'formulas': [{'category': 'I. Dấu hiệu nhận biết',
                'items': [{'name': 'Số chẵn', 'formula': 'Tận cùng là $0, 2, 4, 6, 8$ (chia hết cho $2$)'},
                          {'name': 'Số lẻ',
                           'formula': 'Tận cùng là $1, 3, 5, 7, 9$ (không chia hết cho $2$)'}]},
               {'category': 'II. Hai số liên tiếp',
                'items': [{'name': 'Hai số chẵn/lẻ liên tiếp',
                           'formula': 'Hơn kém nhau $2$ đơn vị: $n$ và $n + 2$'}]}],
  'example': 'Tìm số chẵn liền sau của số $1\\,998$ và số lẻ liền trước của số $2\\,025$.',
  'example_answer': '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$.\n'
                    '- Số lẻ liền trước của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
  'real_life': '- Đánh số nhà trên đường phố: một bên đường đánh toàn số chẵn ($2, 4, 6, \\dots$), bên đối '
               'diện đánh toàn số lẻ ($1, 3, 5, \\dots$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số sau, số nào là số chẵn?',
            'options': ['$357$', '$1\\,209$', '$4\\,618$', '$75\\,391$'],
            'answer': 2,
            'solution': 'Số **$4\\,618$** có chữ số tận cùng là $8$ nên là số chẵn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số sau, số nào là số lẻ?',
            'options': ['$2\\,470$', '$3\\,584$', '$1\\,006$', '$6\\,723$'],
            'answer': 3,
            'solution': 'Số **$6\\,723$** có chữ số tận cùng là $3$ nên là số lẻ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Số chẵn, số lẻ**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Số chẵn**?',
            'options': ['Tận cùng là $0, 2, 4, 6, 8$ (chia hết cho $2$)',
                        'Tận cùng là $1, 3, 5, 7, 9$ (không chia hết cho $2$)',
                        'Hơn kém nhau $2$ đơn vị: $n$ và $n + 2$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Số chẵn, số lẻ, **Số chẵn** được xác định '
                        'bởi: Tận cùng là $0, 2, 4, 6, 8$ (chia hết cho $2$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Số chẵn, số lẻ**, nội dung/biểu thức Tận cùng là $1, 3, 5, 7, 9$ (không '
                 'chia hết cho $2$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số chẵn', 'Số lẻ', 'Hai số chẵn/lẻ liên tiếp', 'Phân tích số'],
            'answer': 1,
            'solution': 'Trong Bài 3: Số chẵn, số lẻ, biểu thức/quy tắc Tận cùng là $1, 3, 5, 7, 9$ (không '
                        'chia hết cho $2$) chính là nội dung của **Số lẻ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số chẵn liền sau của số $1\\,998$ là:',
            'options': ['$1\\,999$', '$2\\,002$', '$2\\,000$', '$1\\,996$'],
            'answer': 2,
            'solution': 'Hai số chẵn liên tiếp hơn kém nhau $2$ đơn vị: $1\\,998 + 2 = 2\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Số chẵn, số lẻ** (Chủ đề 1: Ôn tập và bổ sung), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Nhận biết được số chẵn (tận cùng là $0, 2, 4, 6, 8$) và số lẻ (tận cùng là $1, 3, '
                        '5, 7, 9$).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Số chẵn, số lẻ: Nhận biết được số chẵn (tận cùng là '
                        '$0, 2, 4, 6, 8$) và số lẻ (tận cùng là $1, 3, 5, 7, 9$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tổng của hai số lẻ bất kỳ luôn là một số chẵn."',
            'answer': True,
            'solution': 'Ví dụ $3 + 5 = 8$, tổng hai số lẻ luôn chia hết cho $2$ nên là số chẵn '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 3: Số chẵn, số lẻ**, quy tắc **Số chẵn** được xác định bởi Tận cùng là $0, 2, '
                 '4, 6, 8$ (chia hết cho $2$) và áp dụng trực tiếp vào bài toán: “Tìm số chẵn liền sau của '
                 'số $1\\,998$ và số lẻ liền trước của số $2\\,025$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Số chẵn** (Tận cùng là $0, 2, 4, 6, 8$ (chia hết cho '
                        '$2$)) là kiến thức cốt lõi của Bài 3: Số chẵn, số lẻ. - Số chẵn liền sau của '
                        '$1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước của $2\\,025$ là: '
                        '$2\\,025 - 2 = 2\\,023$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Số chẵn, số lẻ** để giải quyết tình huống sau: Tìm số chẵn '
                 'liền sau của số $1\\,998$ và số lẻ liền trước của số $2\\,025$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Thay $a = 12, b = 5, c = 40$ vào biểu thức ta được: $12 \\times 5 + 40 = 60 + 40 = '
                        '100$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Số chẵn, số lẻ: - Số chẵn liền sau của $1\\,998$ là: '
                        '$1\\,998 + 2 = 2\\,000$.\n'
                        '- Số lẻ liền trước của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Từ số $10$ đến số $20$ (tính cả $10$ và $20$) có tất cả bao nhiêu số chẵn?',
            'answer': ['6'],
            'unit': 'số',
            'solution': 'Các số chẵn là $10, 12, 14, 16, 18, 20$, gồm tất cả **$6$** số chẵn.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 4 · Chủ đề 1: Ôn tập các số đến 100 000; số chẵn, số lẻ; biểu thức chứa chữ; bài toán '
             '3 bước tính.',
  'title': 'Bài 4: Biểu thức chứa chữ',
  'icon': '🔤',
  'description': 'Nhận biết biểu thức chứa một chữ, hai chữ, ba chữ và tính giá trị biểu thức khi biết giá '
                 'trị của chữ.',
  'requirements': ['Nhận biết được biểu thức chứa một chữ, hai chữ, ba chữ (ví dụ $a + 5$, $a \\times b$, $a '
                   '+ b + c$).',
                   'Tính đúng giá trị của biểu thức chứa chữ khi thay chữ bằng số cho trước.',
                   'Vận dụng biểu thức chứa chữ vào công thức tính chu vi, diện tích.'],
  'definition': '- **Biểu thức chứa chữ** là biểu thức có chứa các số, dấu phép tính và các chữ cái ($a, b, '
                'c, m, n, x, \\dots$).\n'
                '- Mỗi lần thay chữ bằng số, ta tính được **một giá trị** của biểu thức chứa chữ đó.',
  'theory': '### 1. Biểu thức chứa một chữ, hai chữ, ba chữ\n'
            '- Chứa một chữ: $35 + a \\times 3$. Với $a = 7$, giá trị biểu thức là $35 + 7 \\times 3 = 35 + '
            '21 = 56$.\n'
            '- Chứa hai chữ: $(m + n) \\times 2$. Với $m = 6, n = 4$, giá trị biểu thức là $(6 + 4) \\times '
            '2 = 20$.\n'
            '- Chứa ba chữ: $a \\times b + c$. Với $a = 12, b = 5, c = 40$, giá trị biểu thức là $12 \\times '
            '5 + 40 = 100$.\n'
            '### 2. Công thức toán học là biểu thức chứa chữ\n'
            '- Chu vi hình vuông cạnh $a$: $P = a \\times 4$; chu vi hình chữ nhật: $P = (a + b) \\times 2$; '
            'chu vi tam giác: $P = a + b + c$.',
  'formulas': [{'category': 'I. Phân loại biểu thức chứa chữ',
                'items': [{'name': 'Một chữ', 'formula': '$a + 15$ · $48 : a$ · $a \\times 4$'},
                          {'name': 'Hai chữ', 'formula': '$a + b$ · $(a + b) \\times 2$ · $a \\times b$'},
                          {'name': 'Ba chữ', 'formula': '$a + b + c$ · $a \\times b + c$'}]}],
  'example': 'Tính giá trị của biểu thức $a \\times b + c$ với $a = 12$, $b = 5$, $c = 40$.',
  'example_answer': 'Thay $a = 12, b = 5, c = 40$ vào biểu thức ta được:\n'
                    '$12 \\times 5 + 40 = 60 + 40 = 100$.',
  'real_life': '- Viết công thức tổng quát tính chu vi, diện tích hoặc công thức tính tiền mua hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a = 9$, giá trị của biểu thức $45 : a$ là:',
            'options': ['$36$', '$54$', '$405$', '$5$'],
            'answer': 3,
            'solution': 'Thay $a = 9$ vào biểu thức: $45 : 9 = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức nào dưới đây là biểu thức chứa hai chữ?',
            'options': ['$m \\times n$', '$a + 25$', '$35 \\times 2$', '$a + b + c$'],
            'answer': 0,
            'solution': 'Biểu thức **$m \\times n$** chứa hai chữ là $m$ và $n$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4: Biểu thức chứa chữ**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Một chữ**?',
            'options': ['$a + b$ · $(a + b) \\times 2$ · $a \\times b$',
                        '$a + 15$ · $48 : a$ · $a \\times 4$',
                        '$a + b + c$ · $a \\times b + c$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4: Biểu thức chứa chữ, **Một chữ** được xác '
                        'định bởi: $a + 15$ · $48 : a$ · $a \\times 4$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Biểu thức chứa chữ**, nội dung/biểu thức $a + b$ · $(a + b) \\times 2$ · $a '
                 '\\times b$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Một chữ', 'Ba chữ', 'Hai chữ', 'Phân tích số'],
            'answer': 2,
            'solution': 'Trong Bài 4: Biểu thức chứa chữ, biểu thức/quy tắc $a + b$ · $(a + b) \\times 2$ · '
                        '$a \\times b$ chính là nội dung của **Hai chữ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Với $m = 6$ và $n = 4$, giá trị của biểu thức $(m + n) \\times 2$ là:',
            'options': ['$14$', '$48$', '$12$', '$20$'],
            'answer': 3,
            'solution': 'Thay số: $(6 + 4) \\times 2 = 10 \\times 2 = 20$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Biểu thức chứa chữ** (Chủ đề 1: Ôn tập và bổ sung), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được biểu thức chứa một chữ, hai chữ, ba chữ (ví dụ $a + 5$, $a \\times '
                        'b$, $a + b + c$).',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4: Biểu thức chứa chữ: Nhận biết được biểu thức chứa '
                        'một chữ, hai chữ, ba chữ (ví dụ $a + 5$, $a \\times b$, $a + b + c$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Với $a = 3$, giá trị của biểu thức $20 - a \\times 4$ bằng $68$."',
            'answer': False,
            'solution': 'Thực hiện nhân trước: $20 - 3 \\times 4 = 20 - 12 = 8$, không phải $68$ '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 4: Biểu thức chứa chữ**, quy tắc **Một chữ** được xác định bởi $a + 15$ · $48 '
                 ': a$ · $a \\times 4$ và áp dụng trực tiếp vào bài toán: “Tính giá trị của biểu thức $a '
                 '\\times b + c$ với $a = 12$, $b = 5$, $c = 40$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Một chữ** ($a + 15$ · $48 : a$ · $a \\times 4$) là '
                        'kiến thức cốt lõi của Bài 4: Biểu thức chứa chữ. Thay $a = 12, b = 5, c = 40$ vào '
                        'biểu thức ta được: $12 \\times 5 + 40 = 60 + 40 = 100$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4: Biểu thức chứa chữ** để giải quyết tình huống sau: Tính giá '
                 'trị của biểu thức $a \\times b + c$ với $a = 12$, $b = 5$, $c = 40$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thay $a = 12, b = 5, c = 40$ vào biểu thức ta được: $12 \\times 5 + 40 = 60 + 40 = '
                        '100$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Biểu thức chứa chữ: Thay $a = 12, b = 5, c = 40$ vào '
                        'biểu thức ta được:\n'
                        '$12 \\times 5 + 40 = 60 + 40 = 100$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình tam giác có độ dài ba cạnh là $a, b, c$ (chu vi $P = a + b + c$). Tính chu vi '
                 'hình tam giác biết $a = 15\\text{ cm}, b = 20\\text{ cm}, c = 25\\text{ cm}$.',
            'answer': ['60'],
            'unit': 'cm',
            'solution': 'Chu vi hình tam giác là: $P = 15 + 20 + 25 = 60\\text{ (cm)}$.\n'
                        'Đáp số: **$60\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 4 · Chủ đề 1: Ôn tập các số đến 100 000; số chẵn, số lẻ; biểu thức chứa chữ; bài toán '
             '3 bước tính.',
  'title': 'Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung',
  'icon': '🧠',
  'description': 'Phương pháp phân tích và trình bày bài giải bài toán có lời văn bằng ba bước tính.',
  'requirements': ['Phân tích được đề bài để xác định trình tự $3$ bước tính hợp lý.',
                   'Trình bày rõ ràng $3$ lời giải, $3$ phép tính và đáp số.',
                   'Vận dụng giải các bài toán thực tế về mua bán, chia đều, tổng – hiệu ba đối tượng.'],
  'definition': '- **Bài toán có $3$ bước tính**: ta tìm lần lượt $2$ đại lượng trung gian ở bước $1$ và '
                'bước $2$, sau đó dùng chúng để tính kết quả ở bước $3$.',
  'theory': '### 1. Dạng 1: Tính hai thành phần rồi tính tổng/hiệu\n'
            '- Ví dụ: Mua $3\\text{ kg}$ táo (giá $45\\,000$ đồng/kg) và $2\\text{ kg}$ cam (giá $30\\,000$ '
            'đồng/kg).\n'
            '  - Bước 1: Tính tiền mua táo ($45\\,000 \\times 3 = 135\\,000$ đồng).\n'
            '  - Bước 2: Tính tiền mua cam ($30\\,000 \\times 2 = 60\\,000$ đồng).\n'
            '  - Bước 3: Tính tổng số tiền ($135\\,000 + 60\\,000 = 195\\,000$ đồng).\n'
            '### 2. Dạng 2: Chuỗi biến đổi liên tiếp\n'
            '- Tìm tổng ban đầu $\\rightarrow$ trừ đi phần đã dùng $\\rightarrow$ chia đều phần còn lại.',
  'formulas': [{'category': 'I. Quy trình giải bài toán 3 bước tính',
                'items': [{'name': 'Bước 1 & Bước 2', 'formula': 'Tìm hai đại lượng trung gian cần thiết'},
                          {'name': 'Bước 3',
                           'formula': 'Thực hiện phép tính cuối cùng để trả lời câu hỏi đề bài'}]}],
  'example': 'Một cửa hàng có $3$ thùng dầu, mỗi thùng chứa $125\\text{ l}$. Cửa hàng đã bán đi $160\\text{ '
             'l}$ dầu. Số dầu còn lại chia đều vào $5$ can. Hỏi mỗi can có bao nhiêu lít dầu?',
  'example_answer': '- Bước 1: Số lít dầu trong $3$ thùng là: $125 \\times 3 = 375\\text{ (l)}$.\n'
                    '- Bước 2: Số lít dầu còn lại sau khi bán là: $375 - 160 = 215\\text{ (l)}$.\n'
                    '- Bước 3: Mỗi can chứa số lít dầu là: $215 : 5 = 43\\text{ (l)}$.',
  'real_life': '- Tính tổng hóa đơn mua nhiều mặt hàng với số lượng khác nhau rồi tính tiền thừa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một bài toán giải bằng ba bước tính cần tối thiểu mấy lời giải và mấy phép tính?',
            'options': ['$3$ lời giải, $3$ phép tính',
                        '$2$ lời giải, $2$ phép tính',
                        '$1$ lời giải, $3$ phép tính',
                        '$4$ lời giải, $4$ phép tính'],
            'answer': 0,
            'solution': 'Bài toán ba bước tính chuẩn gồm **$3$ lời giải và $3$ phép tính**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mua $3$ quyển vở giá $8\\,000$ đồng/quyển và $2$ cái bút giá $5\\,000$ đồng/cái. Tổng số '
                 'tiền mua vở và bút là:',
            'options': ['$24\\,000$ đồng', '$34\\,000$ đồng', '$13\\,000$ đồng', '$39\\,000$ đồng'],
            'answer': 1,
            'solution': 'Tiền vở: $8\\,000 \\times 3 = 24\\,000$ đồng; tiền bút: $5\\,000 \\times 2 = '
                        '10\\,000$ đồng; tổng: $24\\,000 + 10\\,000 = 34\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 5, 6: Giải bài toán có ba bước tính và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Bước 1 & Bước 2**?',
            'options': ['Thực hiện phép tính cuối cùng để trả lời câu hỏi đề bài',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Tìm hai đại lượng trung gian cần thiết',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 5, 6: Giải bài toán có ba bước tính và luyện '
                        'tập chung, **Bước 1 & Bước 2** được xác định bởi: Tìm hai đại lượng trung gian cần '
                        'thiết.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung**, nội dung/biểu thức '
                 'Thực hiện phép tính cuối cùng để trả lời câu hỏi đề bài là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Bước 1 & Bước 2', 'Phân tích số', 'Quy tắc 5', 'Bước 3'],
            'answer': 3,
            'solution': 'Trong Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung, biểu thức/quy tắc '
                        'Thực hiện phép tính cuối cùng để trả lời câu hỏi đề bài chính là nội dung của '
                        '**Bước 3**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mua $3\\text{ kg}$ táo giá $45\\,000$ đồng/kg và $2\\text{ kg}$ cam giá $30\\,000$ '
                 'đồng/kg. Đưa tờ $200\\,000$ đồng thì được trả lại:',
            'options': ['$5\\,000$ đồng', '$25\\,000$ đồng', '$15\\,000$ đồng', '$65\\,000$ đồng'],
            'answer': 0,
            'solution': 'Tiền táo $135\\,000$ đồng, tiền cam $60\\,000$ đồng, tổng $195\\,000$ đồng. Tiền '
                        'trả lại: $200\\,000 - 195\\,000 = 5\\,000$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung** (Chủ đề 1: Ôn tập '
                 'và bổ sung), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Phân tích được đề bài để xác định trình tự $3$ bước tính hợp lý.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 5, 6: Giải bài toán có ba bước tính và luyện tập '
                        'chung: Phân tích được đề bài để xác định trình tự $3$ bước tính hợp lý.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tổ 1 trồng $12$ cây, tổ 2 trồng gấp đôi tổ 1, tổ 3 trồng ít hơn tổ 2 là $4$ '
                 'cây thì tổ 3 trồng được $20$ cây."',
            'answer': True,
            'solution': 'Tổ 2 trồng $12 \\times 2 = 24$ cây; tổ 3 trồng $24 - 4 = 20$ cây $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung**, quy tắc **Bước 1 & '
                 'Bước 2** được xác định bởi Tìm hai đại lượng trung gian cần thiết và áp dụng trực tiếp vào '
                 'bài toán: “Một cửa hàng có $3$ thùng dầu, mỗi thùng chứa $125\\text{ l}$. Cửa hàng đã bán '
                 'đi $160\\text{ l}$ dầu. Số dầu còn lại chia đều vào $5$ can. Hỏ...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bước 1 & Bước 2** (Tìm hai đại lượng trung gian cần '
                        'thiết) là kiến thức cốt lõi của Bài 5, 6: Giải bài toán có ba bước tính và luyện '
                        'tập chung. - Bước 1: Số lít dầu trong $3$ thùng là: $125 \\times 3 = 375\\text{ '
                        '(l)}$. - Bước 2: Số lít dầu còn lại sau khi bán là: $375 - 160 = 215\\text{ '
                        '(l)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung** để giải '
                 'quyết tình huống sau: Một cửa hàng có $3$ thùng dầu, mỗi thùng chứa $125\\text{ l}$. Cửa '
                 'hàng đã bán đi $160\\text{ l}$ dầu. Số dầu còn lại chia đều vào $5$ can. Hỏi mỗi can có '
                 'bao nhiêu lít dầu? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Bước 1: Số lít dầu trong $3$ thùng là: $125 \\times 3 = 375\\text{ (l)}$. - Bước '
                        '2: Số lít dầu còn lại sau khi bán là: $375 - 160 = 215\\text{ (l)}$. - Bước...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5, 6: Giải bài toán có ba bước tính và luyện tập chung: '
                        '- Bước 1: Số lít dầu trong $3$ thùng là: $125 \\times 3 = 375\\text{ (l)}$.\n'
                        '- Bước 2: Số lít dầu còn lại sau khi bán là: $375 - 160 = 215\\text{ (l)}$.\n'
                        '- Bước 3: Mỗi can chứa số lít dầu là: $215 : 5 = 43\\text{ (l)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng có $3$ thùng dầu, mỗi thùng $125\\text{ l}$. Đã bán $160\\text{ l}$, số dầu '
                 'còn lại chia đều vào $5$ can. Hỏi mỗi can có bao nhiêu lít dầu?',
            'answer': ['43'],
            'unit': 'l',
            'solution': 'Tổng số dầu: $125 \\times 3 = 375\\text{ (l)}$. Còn lại: $375 - 160 = 215\\text{ '
                        '(l)}$. Mỗi can có: $215 : 5 = 43\\text{ (l)}$.\n'
                        'Đáp số: **$43\\text{ l}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd02-goc-va-don-vi-do-goc',
  'context_title': 'Chủ đề 2: Góc và đơn vị đo góc',
  'context': 'SGK Toán 4 · Chủ đề 2: Góc và đơn vị đo góc (độ); góc nhọn, góc tù, góc bẹt.',
  'title': 'Bài 7: Đo góc, đơn vị đo góc',
  'icon': '📐',
  'description': 'Nhận biết đơn vị đo góc là độ (°) và cách sử dụng thước đo góc để đo số đo của một góc.',
  'requirements': ['Nhận biết được đơn vị đo góc là **độ** (ký hiệu $^\\circ$).',
                   'Biết cấu tạo của thước đo góc và quy tắc đặt thước đo góc đúng cách.',
                   'Đọc đúng số đo của các góc $60^\\circ, 90^\\circ, 120^\\circ, 180^\\circ$ trên thước đo '
                   'góc.'],
  'definition': '- **Độ** (ký hiệu $^\\circ$) là đơn vị đo góc. Ví dụ: một độ viết là $1^\\circ$, góc vuông '
                'có số đo bằng **$90^\\circ$**.\n'
                '- **Cách đo góc bằng thước đo góc**:\n'
                '  1. Đặt **tâm** của thước trùng với **đỉnh** của góc.\n'
                '  2. Xoay thước sao cho **một cạnh** của góc đi qua **vạch $0^\\circ$** của thước.\n'
                '  3. Cạnh còn lại của góc đi qua vạch số nào (trên cùng vòng cung với vạch $0^\\circ$ đã '
                'chọn) thì đó là **số đo của góc**.',
  'theory': '### 1. Lưu ý hai vòng chia độ trên thước đo góc\n'
            '- Trên thước đo góc có $2$ vòng số từ $0$ đến $180$ ngược chiều nhau.\n'
            '- Nếu cạnh thứ nhất đi qua vạch $0^\\circ$ ở vòng trong thì phải đọc số đo ở vòng trong; nếu đi '
            'qua vạch $0^\\circ$ ở vòng ngoài thì đọc ở vòng ngoài.',
  'formulas': [{'category': 'I. Đo góc',
                'items': [{'name': 'Đơn vị đo góc', 'formula': 'Độ ($^\\circ$) · Góc vuông $= 90^\\circ$'},
                          {'name': '3 bước đặt thước',
                           'formula': 'Tâm thước $\\equiv$ Đỉnh góc · Cạnh 1 đi qua vạch $0^\\circ$ · Đọc số '
                                      'ở cạnh 2'}]}],
  'example': 'Khi đo góc đỉnh $O$, cạnh $OA, OB$, bạn Lan đặt tâm thước trùng đỉnh $O$, tia $OA$ đi qua vạch '
             '$0^\\circ$ vòng trong và tia $OB$ đi qua vạch $60$ vòng trong. Số đo góc đó là bao nhiêu?',
  'example_answer': 'Góc đỉnh $O$, cạnh $OA, OB$ có số đo bằng **$60^\\circ$** (đọc là sáu mươi độ).',
  'real_life': '- Đo góc nghiêng của cầu trượt, góc mở của chiếc quạt giấy hoặc góc của mái nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị dùng để đo góc là:',
            'options': ['Mét ($\\text{m}$)',
                        'Độ ($^\\circ$)',
                        'Giây ($\\text{s}$)',
                        'Ki-lô-gam ($\\text{kg}$)'],
            'answer': 1,
            'solution': 'Đơn vị đo góc là **độ ($^\\circ$)**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc vuông có số đo bằng bao nhiêu độ?',
            'options': ['$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$180^\\circ$'],
            'answer': 2,
            'solution': 'Góc vuông có số đo bằng **$90^\\circ$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7: Đo góc, đơn vị đo góc**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Đơn vị đo góc**?',
            'options': ['Tâm thước $\\equiv$ Đỉnh góc · Cạnh 1 đi qua vạch $0^\\circ$ · Đọc số ở cạnh 2',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        'Độ ($^\\circ$) · Góc vuông $= 90^\\circ$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7: Đo góc, đơn vị đo góc, **Đơn vị đo góc** '
                        'được xác định bởi: Độ ($^\\circ$) · Góc vuông $= 90^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Đo góc, đơn vị đo góc**, nội dung/biểu thức Tâm thước $\\equiv$ Đỉnh góc · '
                 'Cạnh 1 đi qua vạch $0^\\circ$ · Đọc số ở cạnh 2 là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['3 bước đặt thước', 'Đơn vị đo góc', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 7: Đo góc, đơn vị đo góc, biểu thức/quy tắc Tâm thước $\\equiv$ Đỉnh góc '
                        '· Cạnh 1 đi qua vạch $0^\\circ$ · Đọc số ở cạnh 2 chính là nội dung của **3 bước '
                        'đặt thước**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi đặt thước đo góc, tâm của thước phải đặt trùng với yếu tố nào của góc?',
            'options': ['Cạnh thứ nhất của góc',
                        'Đỉnh của góc',
                        'Cạnh thứ hai của góc',
                        'Điểm bất kỳ trên cạnh'],
            'answer': 1,
            'solution': 'Tâm của thước đo góc phải trùng với **đỉnh của góc**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Đo góc, đơn vị đo góc** (Chủ đề 2: Góc và đơn vị đo góc), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Nhận biết được đơn vị đo góc là **độ** (ký hiệu $^\\circ$).',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 7: Đo góc, đơn vị đo góc: Nhận biết được đơn vị đo góc '
                        'là **độ** (ký hiệu $^\\circ$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số đo $120^\\circ$ được đọc là một trăm hai mươi độ."',
            'answer': True,
            'solution': 'Ký hiệu $^\\circ$ đọc là độ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 7: Đo góc, đơn vị đo góc**, quy tắc **Đơn vị đo góc** được xác định bởi Độ '
                 '($^\\circ$) · Góc vuông $= 90^\\circ$ và áp dụng trực tiếp vào bài toán: “Khi đo góc đỉnh '
                 '$O$, cạnh $OA, OB$, bạn Lan đặt tâm thước trùng đỉnh $O$, tia $OA$ đi qua vạch $0^\\circ$ '
                 'vòng trong và tia $OB$ đi qua vạch...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đơn vị đo góc** (Độ ($^\\circ$) · Góc vuông $= '
                        '90^\\circ$) là kiến thức cốt lõi của Bài 7: Đo góc, đơn vị đo góc. Góc đỉnh $O$, '
                        'cạnh $OA, OB$ có số đo bằng **$60^\\circ$** (đọc là sáu mươi độ).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7: Đo góc, đơn vị đo góc** để giải quyết tình huống sau: Khi đo '
                 'góc đỉnh $O$, cạnh $OA, OB$, bạn Lan đặt tâm thước trùng đỉnh $O$, tia $OA$ đi qua vạch '
                 '$0^\\circ$ vòng trong và tia $OB$ đi qua vạch $60$ vòng trong. Số đo góc đó là bao nhiêu? '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Góc đỉnh $O$, cạnh $OA, OB$ có số đo bằng **$60^\\circ$** (đọc là sáu mươi độ).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 7: Đo góc, đơn vị đo góc: Góc đỉnh $O$, cạnh $OA, OB$ có '
                        'số đo bằng **$60^\\circ$** (đọc là sáu mươi độ).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Góc đỉnh $A$, cạnh $AB, AC$ có số đo bằng nửa số đo của góc vuông. Hỏi góc đỉnh $A$ có số '
                 'đo bằng bao nhiêu độ?',
            'answer': ['45'],
            'unit': '°',
            'solution': 'Số đo góc vuông là $90^\\circ$, nửa góc vuông là: $90 : 2 = 45^\\circ$.\n'
                        'Đáp số: **$45^\\circ$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd02-goc-va-don-vi-do-goc',
  'context_title': 'Chủ đề 2: Góc và đơn vị đo góc',
  'context': 'SGK Toán 4 · Chủ đề 2: Góc và đơn vị đo góc (độ); góc nhọn, góc tù, góc bẹt.',
  'title': 'Bài 8: Góc nhọn, góc tù, góc bẹt',
  'icon': '📐',
  'description': 'Nhận biết và phân loại góc nhọn, góc vuông, góc tù, góc bẹt theo số đo góc.',
  'requirements': ['Nhận biết được góc nhọn (bé hơn góc vuông), góc tù (lớn hơn góc vuông và bé hơn góc '
                   'bẹt), góc bẹt (bằng hai góc vuông).',
                   'Phân loại được góc khi biết số đo của góc đó ($0^\\circ < \\text{nhọn} < 90^\\circ < '
                   '\\text{tù} < 180^\\circ$).',
                   'Nhận diện được các loại góc tạo bởi hai kim đồng hồ.'],
  'definition': '- **Góc nhọn**: có số đo **bé hơn $90^\\circ$** (bé hơn góc vuông).\n'
                '- **Góc vuông**: có số đo **bằng $90^\\circ$**.\n'
                '- **Góc tù**: có số đo **lớn hơn $90^\\circ$ và bé hơn $180^\\circ$** (lớn hơn góc vuông, '
                'bé hơn góc bẹt).\n'
                '- **Góc bẹt**: có số đo **bằng $180^\\circ$** (bằng $2$ góc vuông; hai cạnh là hai tia đối '
                'nhau tạo thành một đường thẳng).',
  'theory': '### 1. So sánh độ lớn các loại góc\n'
            '- Thứ tự tăng dần: $\\text{Góc nhọn} < \\text{Góc vuông } (90^\\circ) < \\text{Góc tù} < '
            '\\text{Góc bẹt } (180^\\circ)$.\n'
            '### 2. Góc giữa hai kim đồng hồ\n'
            '- Mỗi khoảng giữa hai số liên tiếp trên mặt đồng hồ ứng với $30^\\circ$.\n'
            '- Lúc $2$ giờ: $2 \\times 30^\\circ = 60^\\circ$ (góc nhọn); lúc $3$ giờ: $90^\\circ$ (góc '
            'vuông); lúc $4$ giờ: $120^\\circ$ (góc tù); lúc $6$ giờ: $180^\\circ$ (góc bẹt).',
  'formulas': [{'category': 'I. Phân loại góc theo số đo',
                'items': [{'name': 'Góc nhọn', 'formula': '$0^\\circ < \\alpha < 90^\\circ$'},
                          {'name': 'Góc vuông', 'formula': '$\\alpha = 90^\\circ$'},
                          {'name': 'Góc tù', 'formula': '$90^\\circ < \\alpha < 180^\\circ$'},
                          {'name': 'Góc bẹt', 'formula': '$\\alpha = 180^\\circ = 2 \\times 90^\\circ$'}]}],
  'example': 'Cho các góc có số đo: $35^\\circ, 90^\\circ, 135^\\circ, 180^\\circ$. Hãy cho biết mỗi góc '
             'thuộc loại góc gì?',
  'example_answer': '- Góc $35^\\circ < 90^\\circ$ là **góc nhọn**.\n'
                    '- Góc $90^\\circ$ là **góc vuông**.\n'
                    '- Góc $135^\\circ$ ($90^\\circ < 135^\\circ < 180^\\circ$) là **góc tù**.\n'
                    '- Góc $180^\\circ$ là **góc bẹt**.',
  'real_life': '- Cánh cửa mở hé tạo góc nhọn, mở rộng quá góc vuông tạo góc tù; chiếc quạt xếp mở hết cỡ '
               'tạo góc bẹt $180^\\circ$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc bẹt có số đo bằng bao nhiêu độ?',
            'options': ['$90^\\circ$', '$120^\\circ$', '$180^\\circ$', '$360^\\circ$'],
            'answer': 2,
            'solution': 'Góc bẹt có số đo bằng **$180^\\circ$** (bằng hai góc vuông).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc có số đo $45^\\circ$ là góc gì?',
            'options': ['Góc vuông', 'Góc tù', 'Góc bẹt', 'Góc nhọn'],
            'answer': 3,
            'solution': 'Vì $45^\\circ < 90^\\circ$ nên đó là **góc nhọn**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 8: Góc nhọn, góc tù, góc bẹt**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Góc nhọn**?',
            'options': ['$0^\\circ < \\alpha < 90^\\circ$',
                        '$\\alpha = 90^\\circ$',
                        '$90^\\circ < \\alpha < 180^\\circ$',
                        '$\\alpha = 180^\\circ = 2 \\times 90^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 8: Góc nhọn, góc tù, góc bẹt, **Góc nhọn** '
                        'được xác định bởi: $0^\\circ < \\alpha < 90^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Góc nhọn, góc tù, góc bẹt**, nội dung/biểu thức $\\alpha = 90^\\circ$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Góc nhọn', 'Góc vuông', 'Góc tù', 'Góc bẹt'],
            'answer': 1,
            'solution': 'Trong Bài 8: Góc nhọn, góc tù, góc bẹt, biểu thức/quy tắc $\\alpha = 90^\\circ$ '
                        'chính là nội dung của **Góc vuông**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Góc có số đo $135^\\circ$ là góc gì?',
            'options': ['Góc nhọn', 'Góc vuông', 'Góc tù', 'Góc bẹt'],
            'answer': 2,
            'solution': 'Vì $90^\\circ < 135^\\circ < 180^\\circ$ nên đó là **góc tù**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Góc nhọn, góc tù, góc bẹt** (Chủ đề 2: Góc và đơn vị đo góc), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Nhận biết được góc nhọn (bé hơn góc vuông), góc tù (lớn hơn góc vuông và bé hơn góc '
                        'bẹt), góc bẹt (bằng hai góc vuông).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 8: Góc nhọn, góc tù, góc bẹt: Nhận biết được góc nhọn '
                        '(bé hơn góc vuông), góc tù (lớn hơn góc vuông và bé hơn góc bẹt), góc bẹt (bằng hai '
                        'góc vuông).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Góc tù luôn có số đo lớn hơn $180^\\circ$."',
            'answer': False,
            'solution': 'Góc tù lớn hơn $90^\\circ$ nhưng luôn **bé hơn $180^\\circ$** $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 8: Góc nhọn, góc tù, góc bẹt**, quy tắc **Góc nhọn** được xác định bởi '
                 '$0^\\circ < \\alpha < 90^\\circ$ và áp dụng trực tiếp vào bài toán: “Cho các góc có số đo: '
                 '$35^\\circ, 90^\\circ, 135^\\circ, 180^\\circ$. Hãy cho biết mỗi góc thuộc loại góc gì?”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Góc nhọn** ($0^\\circ < \\alpha < 90^\\circ$) là '
                        'kiến thức cốt lõi của Bài 8: Góc nhọn, góc tù, góc bẹt. - Góc $35^\\circ < '
                        '90^\\circ$ là **góc nhọn**. - Góc $90^\\circ$ là **góc vuông**. - Góc $135^\\circ$ '
                        '($90^\\circ < 135^\\circ < 180^\\circ$) là **...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 8: Góc nhọn, góc tù, góc bẹt** để giải quyết tình huống sau: Cho '
                 'các góc có số đo: $35^\\circ, 90^\\circ, 135^\\circ, 180^\\circ$. Hãy cho biết mỗi góc '
                 'thuộc loại góc gì? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['- Góc $35^\\circ < 90^\\circ$ là **góc nhọn**. - Góc $90^\\circ$ là **góc vuông**. '
                        '- Góc $135^\\circ$ ($90^\\circ < 135^\\circ < 180^\\circ$) là **góc tù**. - Góc...',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 8: Góc nhọn, góc tù, góc bẹt: - Góc $35^\\circ < '
                        '90^\\circ$ là **góc nhọn**.\n'
                        '- Góc $90^\\circ$ là **góc vuông**.\n'
                        '- Góc $135^\\circ$ ($90^\\circ < 135^\\circ < 180^\\circ$) là **góc tù**.\n'
                        '- Góc $180^\\circ$ là **góc bẹt**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lúc $6$ giờ đúng, kim giờ và kim phút của đồng hồ tạo thành một góc bẹt. Hỏi góc đó có số '
                 'đo bằng bao nhiêu độ?',
            'answer': ['180'],
            'unit': '°',
            'solution': 'Góc bẹt có số đo bằng **$180^\\circ$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd02-goc-va-don-vi-do-goc',
  'context_title': 'Chủ đề 2: Góc và đơn vị đo góc',
  'context': 'SGK Toán 4 · Chủ đề 2: Góc và đơn vị đo góc (độ); góc nhọn, góc tù, góc bẹt.',
  'title': 'Bài 9: Luyện tập chung về góc và đo góc',
  'icon': '🧭',
  'description': 'Vận dụng đo góc, so sánh các góc và tính số đo góc trong các hình phẳng và mặt đồng hồ.',
  'requirements': ['Xác định đúng các góc nhọn, góc vuông, góc tù, góc bẹt trong các hình đa giác.',
                   'Tính được số đo góc tạo bởi hai kim đồng hồ tại các giờ đúng.',
                   'Giải được các bài toán ghép hai góc kề nhau.'],
  'definition': '- Trên mặt đồng hồ chia $12$ vạch số: góc bẹt ($6$ khoảng số) ứng với $180^\\circ$, nên mỗi '
                'khoảng giữa hai số liên tiếp ứng với $180^\\circ : 6 = 30^\\circ$.\n'
                '- Góc bẹt bằng $2$ lần góc vuông ($180^\\circ = 2 \\times 90^\\circ$).',
  'theory': '### 1. Tính góc kim đồng hồ lúc $n$ giờ đúng ($1 \\le n \\le 6$)\n'
            '- Số đo góc giữa kim giờ và kim phút lúc $n$ giờ đúng là: $n \\times 30^\\circ$.\n'
            '- Ví dụ: Lúc $1$ giờ là $30^\\circ$; lúc $2$ giờ là $60^\\circ$; lúc $3$ giờ là $90^\\circ$; '
            'lúc $4$ giờ là $120^\\circ$; lúc $5$ giờ là $150^\\circ$; lúc $6$ giờ là $180^\\circ$.\n'
            '### 2. Nhận biết góc trong tam giác, tứ giác\n'
            '- Một hình tam giác có thể có $3$ góc nhọn, hoặc $1$ góc vuông và $2$ góc nhọn, hoặc $1$ góc tù '
            'và $2$ góc nhọn.',
  'formulas': [{'category': 'I. Góc trên mặt đồng hồ',
                'items': [{'name': 'Một khoảng số', 'formula': '$180^\\circ : 6 = 30^\\circ$'},
                          {'name': 'Lúc n giờ đúng (1 đến 6 giờ)',
                           'formula': '$\\text{Số đo góc} = n \\times 30^\\circ$'}]}],
  'example': 'Lúc $4$ giờ đúng, kim giờ và kim phút tạo thành góc gì và có số đo bao nhiêu độ?',
  'example_answer': 'Lúc $4$ giờ đúng, hai kim cách nhau $4$ khoảng số: $4 \\times 30^\\circ = 120^\\circ$.\n'
                    'Vì $90^\\circ < 120^\\circ < 180^\\circ$ nên đó là **góc tù** có số đo '
                    '**$120^\\circ$**.',
  'real_life': '- Thiết kế độ nghiêng thang máy, cầu thang bộ (thường nghiêng góc nhọn khoảng $30^\\circ$ '
               'đến $35^\\circ$ so với mặt sàn).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Lúc $3$ giờ đúng, hai kim đồng hồ tạo thành góc gì?',
            'options': ['Góc nhọn', 'Góc tù', 'Góc bẹt', 'Góc vuông'],
            'answer': 3,
            'solution': 'Lúc $3$ giờ đúng, hai kim tạo thành **góc vuông** ($90^\\circ$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số đo góc $89^\\circ, 90^\\circ, 91^\\circ, 180^\\circ$, số đo nào là của góc '
                 'tù?',
            'options': ['$91^\\circ$', '$89^\\circ$', '$90^\\circ$', '$180^\\circ$'],
            'answer': 0,
            'solution': 'Vì $90^\\circ < 91^\\circ < 180^\\circ$ nên **$91^\\circ$** là số đo của góc tù.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9: Luyện tập chung về góc và đo góc**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Một khoảng số**?',
            'options': ['$\\text{Số đo góc} = n \\times 30^\\circ$',
                        '$180^\\circ : 6 = 30^\\circ$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9: Luyện tập chung về góc và đo góc, **Một '
                        'khoảng số** được xác định bởi: $180^\\circ : 6 = 30^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Luyện tập chung về góc và đo góc**, nội dung/biểu thức $\\text{Số đo góc} = '
                 'n \\times 30^\\circ$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Một khoảng số', 'Phân tích số', 'Lúc n giờ đúng (1 đến 6 giờ)', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 9: Luyện tập chung về góc và đo góc, biểu thức/quy tắc $\\text{Số đo góc} '
                        '= n \\times 30^\\circ$ chính là nội dung của **Lúc n giờ đúng (1 đến 6 giờ)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Ghép hai góc nhọn có số đo $40^\\circ$ và $65^\\circ$ chung cạnh sát nhau, ta được góc mới '
                 'là:',
            'options': ['Góc nhọn ($105^\\circ$)',
                        'Góc vuông ($90^\\circ$)',
                        'Góc bẹt ($180^\\circ$)',
                        'Góc tù ($105^\\circ$)'],
            'answer': 3,
            'solution': 'Tổng số đo là $40^\\circ + 65^\\circ = 105^\\circ > 90^\\circ$ nên là **góc tù '
                        '($105^\\circ$)**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Luyện tập chung về góc và đo góc** (Chủ đề 2: Góc và đơn vị đo góc), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Xác định đúng các góc nhọn, góc vuông, góc tù, góc bẹt trong các hình đa giác.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 9: Luyện tập chung về góc và đo góc: Xác định đúng các '
                        'góc nhọn, góc vuông, góc tù, góc bẹt trong các hình đa giác.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số đo của góc bẹt gấp hai lần số đo của góc vuông."',
            'answer': True,
            'solution': 'Vì $180^\\circ = 2 \\times 90^\\circ$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 9: Luyện tập chung về góc và đo góc**, quy tắc **Một khoảng số** được xác định '
                 'bởi $180^\\circ : 6 = 30^\\circ$ và áp dụng trực tiếp vào bài toán: “Lúc $4$ giờ đúng, kim '
                 'giờ và kim phút tạo thành góc gì và có số đo bao nhiêu độ?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Một khoảng số** ($180^\\circ : 6 = 30^\\circ$) là '
                        'kiến thức cốt lõi của Bài 9: Luyện tập chung về góc và đo góc. Lúc $4$ giờ đúng, '
                        'hai kim cách nhau $4$ khoảng số: $4 \\times 30^\\circ = 120^\\circ$. Vì $90^\\circ '
                        '< 120^\\circ < 180^\\circ$ nên đó là **góc tù...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9: Luyện tập chung về góc và đo góc** để giải quyết tình huống '
                 'sau: Lúc $4$ giờ đúng, kim giờ và kim phút tạo thành góc gì và có số đo bao nhiêu độ? Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Lúc $4$ giờ đúng, hai kim cách nhau $4$ khoảng số: $4 \\times 30^\\circ = '
                        '120^\\circ$. Vì $90^\\circ < 120^\\circ < 180^\\circ$ nên đó là **góc tù** có số đo '
                        '**$120^\\circ$...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 9: Luyện tập chung về góc và đo góc: Lúc $4$ giờ đúng, '
                        'hai kim cách nhau $4$ khoảng số: $4 \\times 30^\\circ = 120^\\circ$.\n'
                        'Vì $90^\\circ < 120^\\circ < 180^\\circ$ nên đó là **góc tù** có số đo '
                        '**$120^\\circ$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lúc $2$ giờ đúng, góc tạo bởi kim giờ và kim phút trên mặt đồng hồ bằng bao nhiêu độ?',
            'answer': ['60'],
            'unit': '°',
            'solution': 'Hai kim cách nhau $2$ khoảng số, mỗi khoảng $30^\\circ$: $2 \\times 30^\\circ = '
                        '60^\\circ$.\n'
                        'Đáp số: **$60^\\circ$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd03-so-co-nhieu-chu-so',
  'context_title': 'Chủ đề 3: Số có nhiều chữ số',
  'context': 'SGK Toán 4 · Chủ đề 3: Số có nhiều chữ số (đến lớp triệu); hàng và lớp; làm tròn; dãy số tự '
             'nhiên.',
  'title': 'Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp',
  'icon': '🔢',
  'description': 'Đọc, viết số có sáu chữ số, số 1 000 000; nhận biết lớp đơn vị, lớp nghìn và giá trị chữ '
                 'số theo vị trí.',
  'requirements': ['Đọc, viết được các số có sáu chữ số và số một triệu ($1\\,000\\,000$).',
                   'Phân biệt được **lớp đơn vị** (đơn vị, chục, trăm) và **lớp nghìn** (nghìn, chục nghìn, '
                   'trăm nghìn).',
                   'Xác định đúng hàng, lớp và giá trị theo vị trí của mỗi chữ số.'],
  'definition': '- $10$ trăm nghìn $= 1$ triệu, viết là **$1\\,000\\,000$** ($1$ chữ số $1$ và $6$ chữ số '
                '$0$).\n'
                '- **Lớp đơn vị** gồm $3$ hàng: hàng đơn vị, hàng chục, hàng trăm.\n'
                '- **Lớp nghìn** gồm $3$ hàng: hàng nghìn, hàng chục nghìn, hàng trăm nghìn.',
  'theory': '### 1. Số có sáu chữ số\n'
            '- Bao gồm hàng trăm nghìn, chục nghìn, nghìn, trăm, chục, đơn vị.\n'
            '- Khi viết số có nhiều chữ số, ta tách thành từng lớp (mỗi lớp $3$ chữ số từ phải sang trái) để '
            'dễ đọc: ví dụ $352\\,140$.\n'
            '### 2. Hàng và lớp\n'
            '- Trong số $352\\,140$: lớp nghìn gồm các chữ số $3, 5, 2$; lớp đơn vị gồm các chữ số $1, 4, '
            '0$. Chữ số $5$ ở hàng chục nghìn có giá trị là $50\\,000$.',
  'formulas': [{'category': 'I. Cấu trúc hàng và lớp',
                'items': [{'name': 'Lớp nghìn', 'formula': 'Hàng trăm nghìn · Hàng chục nghìn · Hàng nghìn'},
                          {'name': 'Lớp đơn vị', 'formula': 'Hàng trăm · Hàng chục · Hàng đơn vị'},
                          {'name': 'Một triệu', 'formula': '$10 \\text{ trăm nghìn} = 1\\,000\\,000$'}]}],
  'example': 'Trong số $648\\,205$, hãy nêu các chữ số thuộc lớp nghìn và giá trị của chữ số $6$.',
  'example_answer': 'Các chữ số thuộc lớp nghìn là **$6, 4, 8$**.\n'
                    'Chữ số $6$ đứng ở hàng trăm nghìn nên có giá trị là **$600\\,000$**.',
  'real_life': '- Đọc giá tiền các thiết bị điện gia dụng ($850\\,000$ đồng, $1\\,000\\,000$ đồng).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số "một triệu" được viết là:',
            'options': ['$1\\,000\\,000$', '$100\\,000$', '$10\\,000\\,000$', '$1\\,000$'],
            'answer': 0,
            'solution': 'Một triệu viết là **$1\\,000\\,000$** (gồm chữ số $1$ và $6$ chữ số $0$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Lớp nghìn gồm những hàng nào?',
            'options': ['Đơn vị, chục, trăm',
                        'Nghìn, chục nghìn, trăm nghìn',
                        'Triệu, chục triệu, trăm triệu',
                        'Trăm, nghìn, chục nghìn'],
            'answer': 1,
            'solution': 'Lớp nghìn gồm $3$ hàng: **nghìn, chục nghìn, trăm nghìn**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Lớp nghìn**?',
            'options': ['Hàng trăm · Hàng chục · Hàng đơn vị',
                        '$10 \\text{ trăm nghìn} = 1\\,000\\,000$',
                        'Hàng trăm nghìn · Hàng chục nghìn · Hàng nghìn',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng '
                        'và lớp, **Lớp nghìn** được xác định bởi: Hàng trăm nghìn · Hàng chục nghìn · Hàng '
                        'nghìn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp**, nội dung/biểu thức Hàng '
                 'trăm · Hàng chục · Hàng đơn vị là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Lớp nghìn', 'Một triệu', 'Phân tích số', 'Lớp đơn vị'],
            'answer': 3,
            'solution': 'Trong Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp, biểu thức/quy tắc '
                        'Hàng trăm · Hàng chục · Hàng đơn vị chính là nội dung của **Lớp đơn vị**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong số $548\\,302$, chữ số $5$ có giá trị là bao nhiêu?',
            'options': ['$500\\,000$', '$5\\,000$', '$50\\,000$', '$5$'],
            'answer': 0,
            'solution': 'Chữ số $5$ đứng ở hàng trăm nghìn nên có giá trị là **$500\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp** (Chủ đề 3: Số có nhiều '
                 'chữ số), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Đọc, viết được các số có sáu chữ số và số một triệu ($1\\,000\\,000$).',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp: '
                        'Đọc, viết được các số có sáu chữ số và số một triệu ($1\\,000\\,000$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số liền trước của số $1\\,000\\,000$ là số $999\\,999$."',
            'answer': True,
            'solution': 'Ta có $1\\,000\\,000 - 1 = 999\\,999$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp**, quy tắc **Lớp nghìn** '
                 'được xác định bởi Hàng trăm nghìn · Hàng chục nghìn · Hàng nghìn và áp dụng trực tiếp vào '
                 'bài toán: “Trong số $648\\,205$, hãy nêu các chữ số thuộc lớp nghìn và giá trị của chữ số '
                 '$6$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Lớp nghìn** (Hàng trăm nghìn · Hàng chục nghìn · '
                        'Hàng nghìn) là kiến thức cốt lõi của Bài 10, 11: Số có sáu chữ số. Số 1 000 000. '
                        'Hàng và lớp. Các chữ số thuộc lớp nghìn là **$6, 4, 8$**. Chữ số $6$ đứng ở hàng '
                        'trăm nghìn nên có giá trị là **$600\\,000$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp** để giải '
                 'quyết tình huống sau: Trong số $648\\,205$, hãy nêu các chữ số thuộc lớp nghìn và giá trị '
                 'của chữ số $6$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Các chữ số thuộc lớp nghìn là **$6, 4, 8$**. Chữ số $6$ đứng ở hàng trăm nghìn nên '
                        'có giá trị là **$600\\,000$**.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 10, 11: Số có sáu chữ số. Số 1 000 000. Hàng và lớp: Các '
                        'chữ số thuộc lớp nghìn là **$6, 4, 8$**.\n'
                        'Chữ số $6$ đứng ở hàng trăm nghìn nên có giá trị là **$600\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Viết số gồm $4$ trăm nghìn, $6$ chục nghìn, $2$ trăm và $5$ đơn vị (viết số liền).',
            'answer': ['460205'],
            'unit': None,
            'solution': 'Ta có $400\\,000 + 60\\,000 + 200 + 5 = 460\\,205$.\nĐáp số: **$460205$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd03-so-co-nhieu-chu-so',
  'context_title': 'Chủ đề 3: Số có nhiều chữ số',
  'context': 'SGK Toán 4 · Chủ đề 3: Số có nhiều chữ số (đến lớp triệu); hàng và lớp; làm tròn; dãy số tự '
             'nhiên.',
  'title': 'Bài 12: Các số trong phạm vi lớp triệu',
  'icon': '💯',
  'description': 'Đọc, viết các số đến lớp triệu (hàng triệu, hàng chục triệu, hàng trăm triệu) và xác định '
                 'giá trị từng hàng.',
  'requirements': ['Nhận biết **lớp triệu** gồm $3$ hàng: hàng triệu, hàng chục triệu, hàng trăm triệu.',
                   'Đọc và viết thành thạo các số có đến chín chữ số.',
                   'Viết được số có nhiều chữ số thành tổng theo các hàng.'],
  'definition': '- **Lớp triệu** gồm $3$ hàng: **hàng triệu, hàng chục triệu, hàng trăm triệu**.\n'
                '- Khi đọc số có nhiều chữ số, ta tách số thành từng lớp ($3$ chữ số một lớp từ phải sang '
                'trái: lớp đơn vị, lớp nghìn, lớp triệu) rồi đọc từ trái sang phải kèm tên lớp.',
  'theory': '### 1. Cách đọc số đến lớp triệu\n'
            '- Ví dụ: $345\\,207\\,816$ tách thành $345 \\mid 207 \\mid 816$, đọc là: "ba trăm bốn mươi lăm '
            'triệu hai trăm linh bảy nghìn tám trăm mười sáu".\n'
            '### 2. Cách viết số đến lớp triệu\n'
            '- Nếu ở lớp nghìn hoặc lớp đơn vị có hàng nào vắng mặt thì phải viết chữ số $0$ vào đúng vị trí '
            'hàng đó.',
  'formulas': [{'category': 'I. Ba lớp của số tự nhiên',
                'items': [{'name': 'Thứ tự 3 lớp (từ trái sang phải)',
                           'formula': 'Lớp triệu ($3$ hàng) $\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp đơn vị '
                                      '($3$ hàng)'}]}],
  'example': 'Đọc số $20\\,506\\,070$ và nêu giá trị của chữ số $5$ trong số đó.',
  'example_answer': 'Đọc là: **hai mươi triệu năm trăm linh sáu nghìn không trăm bảy mươi**.\n'
                    'Chữ số $5$ đứng ở hàng trăm nghìn (lớp nghìn) nên có giá trị là **$500\\,000$**.',
  'real_life': '- Đọc dân số Việt Nam (khoảng $100\\,000\\,000$ người), diện tích các đại dương hoặc khoảng '
               'cách từ Trái Đất đến Mặt Trời.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $4\\,382\\,615$, chữ số $3$ thuộc hàng nào?',
            'options': ['Hàng chục nghìn', 'Hàng trăm nghìn', 'Hàng triệu', 'Hàng nghìn'],
            'answer': 1,
            'solution': 'Tách lớp $4 \\mid 382 \\mid 615$: chữ số $3$ đứng đầu lớp nghìn nên thuộc **hàng '
                        'trăm nghìn**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số $7\\,030\\,405$ được đọc là:',
            'options': ['Bảy triệu ba trăm nghìn bốn trăm linh năm',
                        'Bảy mươi triệu ba nghìn bốn trăm linh năm',
                        'Bảy triệu ba mươi nghìn bốn trăm linh năm',
                        'Bảy triệu ba mươi nghìn bốn mươi lăm'],
            'answer': 2,
            'solution': 'Tách lớp $7 \\mid 030 \\mid 405 \\rightarrow$ **Bảy triệu ba mươi nghìn bốn trăm '
                        'linh năm**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Các số trong phạm vi lớp triệu**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Thứ tự 3 lớp (từ trái sang phải)**?',
            'options': ['$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$',
                        'Lớp triệu ($3$ hàng) $\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp đơn vị ($3$ hàng)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Các số trong phạm vi lớp triệu, **Thứ tự '
                        '3 lớp (từ trái sang phải)** được xác định bởi: Lớp triệu ($3$ hàng) $\\mid$ Lớp '
                        'nghìn ($3$ hàng) $\\mid$ Lớp đơn vị ($3$ hàng).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Các số trong phạm vi lớp triệu**, nội dung/biểu thức Lớp triệu ($3$ hàng) '
                 '$\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp đơn vị ($3$ hàng) là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Thứ tự 3 lớp (từ trái sang phải)', 'Phân tích số', 'Quy tắc 5', 'Quy tắc'],
            'answer': 0,
            'solution': 'Trong Bài 12: Các số trong phạm vi lớp triệu, biểu thức/quy tắc Lớp triệu ($3$ '
                        'hàng) $\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp đơn vị ($3$ hàng) chính là nội dung '
                        'của **Thứ tự 3 lớp (từ trái sang phải)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của chữ số $6$ trong số $2\\,760\\,345$ là:',
            'options': ['$6\\,000$', '$60\\,000$', '$600\\,000$', '$6\\,000\\,000$'],
            'answer': 1,
            'solution': 'Chữ số $6$ đứng ở hàng chục nghìn nên có giá trị là **$60\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Các số trong phạm vi lớp triệu** (Chủ đề 3: Số có nhiều chữ số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Nhận biết **lớp triệu** gồm $3$ hàng: hàng triệu, hàng chục triệu, hàng trăm triệu.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Các số trong phạm vi lớp triệu: Nhận biết **lớp '
                        'triệu** gồm $3$ hàng: hàng triệu, hàng chục triệu, hàng trăm triệu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Lớp triệu gồm ba hàng: hàng triệu, hàng chục triệu và hàng trăm triệu."',
            'answer': True,
            'solution': 'Đúng theo cấu tạo lớp triệu $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 12: Các số trong phạm vi lớp triệu**, quy tắc **Thứ tự 3 lớp (từ trái sang '
                 'phải)** được xác định bởi Lớp triệu ($3$ hàng) $\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp '
                 'đơn vị ($3$ hàng) và áp dụng trực tiếp vào bài toán: “Đọc số $20\\,506\\,070$ và nêu giá '
                 'trị của chữ số $5$ trong số đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thứ tự 3 lớp (từ trái sang phải)** (Lớp triệu ($3$ '
                        'hàng) $\\mid$ Lớp nghìn ($3$ hàng) $\\mid$ Lớp đơn vị ($3$ hàng)) là kiến thức cốt '
                        'lõi của Bài 12: Các số trong phạm vi lớp triệu. Đọc là: **hai mươi triệu năm trăm '
                        'linh sáu nghìn không trăm bảy mươi**. Chữ số $5$ đứng ở hàng trăm nghìn (lớp nghìn) '
                        'nên có giá trị là **$500\\,000$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Các số trong phạm vi lớp triệu** để giải quyết tình huống '
                 'sau: Đọc số $20\\,506\\,070$ và nêu giá trị của chữ số $5$ trong số đó. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Đọc là: **hai mươi triệu năm trăm linh sáu nghìn không trăm bảy mươi**. Chữ số $5$ '
                        'đứng ở hàng trăm nghìn (lớp nghìn) nên có giá trị là **$500\\,000$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 12: Các số trong phạm vi lớp triệu: Đọc là: **hai mươi '
                        'triệu năm trăm linh sáu nghìn không trăm bảy mươi**.\n'
                        'Chữ số $5$ đứng ở hàng trăm nghìn (lớp nghìn) nên có giá trị là **$500\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Viết số gồm $3$ chục triệu, $4$ triệu, $5$ chục nghìn và $2$ đơn vị (viết số liền không '
                 'dấu cách).',
            'answer': ['34050002'],
            'unit': None,
            'solution': 'Ta có $30\\,000\\,000 + 4\\,000\\,000 + 50\\,000 + 2 = 34\\,050\\,002$.\n'
                        'Đáp số: **$34050002$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd03-so-co-nhieu-chu-so',
  'context_title': 'Chủ đề 3: Số có nhiều chữ số',
  'context': 'SGK Toán 4 · Chủ đề 3: Số có nhiều chữ số (đến lớp triệu); hàng và lớp; làm tròn; dãy số tự '
             'nhiên.',
  'title': 'Bài 13: Làm tròn số đến hàng trăm nghìn',
  'icon': '🔄',
  'description': 'Quy tắc làm tròn các số có nhiều chữ số đến hàng trăm nghìn (và hàng triệu) dựa vào chữ số '
                 'hàng kế bên phải.',
  'requirements': ['Làm tròn được số đến hàng trăm nghìn bằng cách xét chữ số hàng chục nghìn.',
                   'Mở rộng làm tròn đến hàng triệu bằng cách xét chữ số hàng trăm nghìn.',
                   'Vận dụng làm tròn số để ước lượng số liệu thống kê trong thực tiễn.'],
  'definition': '- Khi **làm tròn số đến hàng trăm nghìn**, ta so sánh chữ số **hàng chục nghìn** với $5$:\n'
                '  - Nếu chữ số hàng chục nghìn **bé hơn $5$** ($0, 1, 2, 3, 4$) thì làm tròn xuống (giữ '
                'nguyên hàng trăm nghìn).\n'
                '  - Nếu chữ số hàng chục nghìn **lớn hơn hoặc bằng $5$** ($5, 6, 7, 8, 9$) thì làm tròn lên '
                '(tăng hàng trăm nghìn thêm $1$).\n'
                '  - Sau đó thay tất cả các chữ số từ hàng chục nghìn đến hàng đơn vị bằng chữ số $0$.',
  'theory': '### 1. Ví dụ làm tròn đến hàng trăm nghìn\n'
            '- Số $3\\,482\\,000$: chữ số hàng chục nghìn là $8 \\ge 5 \\rightarrow$ làm tròn lên thành '
            '$3\\,500\\,000$.\n'
            '- Số $5\\,649\\,000$: chữ số hàng chục nghìn là $4 < 5 \\rightarrow$ làm tròn xuống thành '
            '$5\\,600\\,000$.\n'
            '### 2. Mở rộng làm tròn đến hàng triệu\n'
            '- Xét chữ số hàng trăm nghìn: ví dụ $2\\,750\\,000$ có chữ số hàng trăm nghìn là $7 \\ge 5 '
            '\\rightarrow 3\\,000\\,000$.',
  'formulas': [{'category': 'I. Quy tắc làm tròn đến hàng trăm nghìn',
                'items': [{'name': 'Xét chữ số hàng chục nghìn',
                           'formula': '$< 5 \\rightarrow$ giữ nguyên trăm nghìn · $\\ge 5 \\rightarrow$ cộng '
                                      '$1$ vào trăm nghìn'},
                          {'name': 'Các hàng bên phải',
                           'formula': 'Thay tất cả $5$ chữ số bên phải bằng $00\\,000$'}]}],
  'example': 'Làm tròn số $1\\,864\\,250$ đến hàng trăm nghìn.',
  'example_answer': 'Chữ số hàng chục nghìn của số $1\\,864\\,250$ là $6 \\ge 5$ nên ta làm tròn lên đến '
                    'hàng trăm nghìn được **$1\\,900\\,000$**.',
  'real_life': '- Làm tròn số dân của một tỉnh hoặc doanh thu bán hàng trên báo cáo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi làm tròn một số đến hàng trăm nghìn, ta cần xét chữ số ở hàng nào?',
            'options': ['Hàng triệu', 'Hàng trăm nghìn', 'Hàng chục nghìn', 'Hàng nghìn'],
            'answer': 2,
            'solution': 'Ta xét chữ số ngay bên phải hàng trăm nghìn là **hàng chục nghìn**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $5\\,649\\,000$ đến hàng trăm nghìn ta được:',
            'options': ['$5\\,700\\,000$', '$6\\,000\\,000$', '$5\\,650\\,000$', '$5\\,600\\,000$'],
            'answer': 3,
            'solution': 'Chữ số hàng chục nghìn là $4 < 5$ nên làm tròn xuống được **$5\\,600\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Làm tròn số đến hàng trăm nghìn**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Xét chữ số hàng chục nghìn**?',
            'options': ['$< 5 \\rightarrow$ giữ nguyên trăm nghìn · $\\ge 5 \\rightarrow$ cộng $1$ vào trăm '
                        'nghìn',
                        'Thay tất cả $5$ chữ số bên phải bằng $00\\,000$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Làm tròn số đến hàng trăm nghìn, **Xét '
                        'chữ số hàng chục nghìn** được xác định bởi: $< 5 \\rightarrow$ giữ nguyên trăm '
                        'nghìn · $\\ge 5 \\rightarrow$ cộng $1$ vào trăm nghìn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Làm tròn số đến hàng trăm nghìn**, nội dung/biểu thức Thay tất cả $5$ chữ '
                 'số bên phải bằng $00\\,000$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Xét chữ số hàng chục nghìn', 'Các hàng bên phải', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 13: Làm tròn số đến hàng trăm nghìn, biểu thức/quy tắc Thay tất cả $5$ '
                        'chữ số bên phải bằng $00\\,000$ chính là nội dung của **Các hàng bên phải**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Làm tròn số $3\\,482\\,000$ đến hàng trăm nghìn ta được:',
            'options': ['$3\\,400\\,000$', '$3\\,000\\,000$', '$3\\,500\\,000$', '$4\\,000\\,000$'],
            'answer': 2,
            'solution': 'Chữ số hàng chục nghìn là $8 \\ge 5$ nên làm tròn lên được **$3\\,500\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Làm tròn số đến hàng trăm nghìn** (Chủ đề 3: Số có nhiều chữ số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Làm tròn được số đến hàng trăm nghìn bằng cách xét chữ số hàng chục nghìn.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Làm tròn số đến hàng trăm nghìn: Làm tròn được số '
                        'đến hàng trăm nghìn bằng cách xét chữ số hàng chục nghìn.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số $750\\,000$ khi làm tròn đến hàng trăm nghìn thì được $700\\,000$."',
            'answer': False,
            'solution': 'Chữ số hàng chục nghìn là $5 \\ge 5$ nên phải làm tròn lên thành $800\\,000$ '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 13: Làm tròn số đến hàng trăm nghìn**, quy tắc **Xét chữ số hàng chục nghìn** '
                 'được xác định bởi $< 5 \\rightarrow$ giữ nguyên trăm nghìn · $\\ge 5 \\rightarrow$ cộng '
                 '$1$ vào trăm nghìn và áp dụng trực tiếp vào bài toán: “Làm tròn số $1\\,864\\,250$ đến '
                 'hàng trăm nghìn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Xét chữ số hàng chục nghìn** ($< 5 \\rightarrow$ giữ '
                        'nguyên trăm nghìn · $\\ge 5 \\rightarrow$ cộng $1$ vào trăm nghìn) là kiến thức cốt '
                        'lõi của Bài 13: Làm tròn số đến hàng trăm nghìn. Chữ số hàng chục nghìn của số '
                        '$1\\,864\\,250$ là $6 \\ge 5$ nên ta làm tròn lên đến hàng trăm nghìn được '
                        '**$1\\,900\\,000$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Làm tròn số đến hàng trăm nghìn** để giải quyết tình huống '
                 'sau: Làm tròn số $1\\,864\\,250$ đến hàng trăm nghìn. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Chữ số hàng chục nghìn của số $1\\,864\\,250$ là $6 \\ge 5$ nên ta làm tròn lên đến '
                        'hàng trăm nghìn được **$1\\,900\\,000$**.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 13: Làm tròn số đến hàng trăm nghìn: Chữ số hàng chục '
                        'nghìn của số $1\\,864\\,250$ là $6 \\ge 5$ nên ta làm tròn lên đến hàng trăm nghìn '
                        'được **$1\\,900\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một huyện có $268\\,450$ người. Làm tròn số dân của huyện đó đến hàng trăm nghìn thì được '
                 'bao nhiêu người (viết số liền)?',
            'answer': ['300000'],
            'unit': 'người',
            'solution': 'Chữ số hàng chục nghìn là $6 \\ge 5$ nên làm tròn lên đến hàng trăm nghìn được '
                        '**$300000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd03-so-co-nhieu-chu-so',
  'context_title': 'Chủ đề 3: Số có nhiều chữ số',
  'context': 'SGK Toán 4 · Chủ đề 3: Số có nhiều chữ số (đến lớp triệu); hàng và lớp; làm tròn; dãy số tự '
             'nhiên.',
  'title': 'Bài 14: So sánh các số có nhiều chữ số',
  'icon': '⚖️',
  'description': 'Quy tắc so sánh hai số có nhiều chữ số và ứng dụng sắp xếp số liệu thực tế.',
  'requirements': ['So sánh được hai số có nhiều chữ số bằng cách đếm số chữ số hoặc so sánh từng hàng từ '
                   'trái sang phải.',
                   'Tìm được số lớn nhất, số bé nhất trong một nhóm số.',
                   'Sắp xếp các số có nhiều chữ số theo thứ tự tăng dần hoặc giảm dần.'],
  'definition': '- Trong hai số tự nhiên:\n'
                '  1. Số nào có **nhiều chữ số hơn** thì số đó **lớn hơn** (ví dụ $1\\,000\\,000 > '
                '999\\,999$).\n'
                '  2. Nếu hai số có **cùng số chữ số**, ta so sánh từng cặp chữ số ở cùng một hàng kể từ '
                '**trái sang phải**.',
  'theory': '### 1. So sánh hai số khác số chữ số\n'
            '- Số $999\\,999$ ($6$ chữ số) $< 1\\,000\\,000$ ($7$ chữ số).\n'
            '### 2. So sánh hai số cùng số chữ số\n'
            '- Ví dụ: So sánh $1\\,542\\,000$ và $1\\,524\\,300$. Cả hai đều có $7$ chữ số, cùng $1$ triệu, '
            'cùng $5$ trăm nghìn; ở hàng chục nghìn có $4 > 2$ nên $1\\,542\\,000 > 1\\,524\\,300$.',
  'formulas': [{'category': 'I. Quy tắc so sánh',
                'items': [{'name': 'Bước 1: Đếm chữ số',
                           'formula': 'Nhiều chữ số hơn $\\rightarrow$ Lớn hơn'},
                          {'name': 'Bước 2: Cùng số chữ số',
                           'formula': 'So sánh từng hàng từ trái sang phải đến cặp chữ số khác nhau đầu '
                                      'tiên'}]}],
  'example': 'Dân số tỉnh A là $1\\,452\\,800$ người, tỉnh B là $1\\,425\\,900$ người, tỉnh C là '
             '$1\\,542\\,000$ người, tỉnh D là $1\\,524\\,300$ người. Tỉnh nào đông dân nhất?',
  'example_answer': 'Cả bốn số đều có $7$ chữ số và chữ số hàng triệu là $1$.\n'
                    'Xét hàng trăm nghìn: tỉnh C và D có $5 > 4$.\n'
                    'Xét tiếp hàng chục nghìn giữa C và D: $4 > 2$ nên $1\\,542\\,000$ lớn nhất. Vậy **tỉnh '
                    'C** đông dân nhất.',
  'real_life': '- So sánh diện tích hoặc dân số giữa các tỉnh, thành phố; so sánh giá bán nhà đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $999\\,999 \\dots 1\\,000\\,000$ là:',
            'options': ['$>$', '$=$', 'Không so sánh được', '$<$'],
            'answer': 3,
            'solution': 'Số $999\\,999$ có $6$ chữ số, bé hơn $1\\,000\\,000$ có $7$ chữ số $\\rightarrow '
                        '<$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hai số $45\\,678\\,900$ và $45\\,687\\,900$, số nào lớn hơn?',
            'options': ['$45\\,687\\,900$', '$45\\,678\\,900$', 'Hai số bằng nhau', 'Không xác định'],
            'answer': 0,
            'solution': 'Cùng $8$ chữ số, so đến hàng chục nghìn: $8 > 7$ nên **$45\\,687\\,900$** lớn hơn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14: So sánh các số có nhiều chữ số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Bước 1: Đếm chữ số**?',
            'options': ['So sánh từng hàng từ trái sang phải đến cặp chữ số khác nhau đầu tiên',
                        'Nhiều chữ số hơn $\\rightarrow$ Lớn hơn',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14: So sánh các số có nhiều chữ số, **Bước 1: '
                        'Đếm chữ số** được xác định bởi: Nhiều chữ số hơn $\\rightarrow$ Lớn hơn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: So sánh các số có nhiều chữ số**, nội dung/biểu thức So sánh từng hàng từ '
                 'trái sang phải đến cặp chữ số khác nhau đầu tiên là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Bước 1: Đếm chữ số', 'Phân tích số', 'Bước 2: Cùng số chữ số', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 14: So sánh các số có nhiều chữ số, biểu thức/quy tắc So sánh từng hàng '
                        'từ trái sang phải đến cặp chữ số khác nhau đầu tiên chính là nội dung của **Bước 2: '
                        'Cùng số chữ số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho dân số 4 tỉnh: A ($1\\,452\\,800$), B ($1\\,425\\,900$), C ($1\\,542\\,000$), D '
                 '($1\\,524\\,300$). Tỉnh đông dân nhất là:',
            'options': ['Tỉnh A', 'Tỉnh B', 'Tỉnh D', 'Tỉnh C'],
            'answer': 3,
            'solution': 'Vì $1\\,542\\,000$ lớn nhất nên **tỉnh C** đông dân nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: So sánh các số có nhiều chữ số** (Chủ đề 3: Số có nhiều chữ số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['So sánh được hai số có nhiều chữ số bằng cách đếm số chữ số hoặc so sánh từng hàng '
                        'từ trái sang phải.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 14: So sánh các số có nhiều chữ số: So sánh được hai '
                        'số có nhiều chữ số bằng cách đếm số chữ số hoặc so sánh từng hàng từ trái sang '
                        'phải.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$8\\,050\\,400 > 8\\,500\\,400$."',
            'answer': False,
            'solution': 'Cùng $7$ chữ số và cùng $8$ triệu, nhưng chữ số hàng trăm nghìn $0 < 5$ nên '
                        '$8\\,050\\,400 < 8\\,500\\,400$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 14: So sánh các số có nhiều chữ số**, quy tắc **Bước 1: Đếm chữ số** được xác '
                 'định bởi Nhiều chữ số hơn $\\rightarrow$ Lớn hơn và áp dụng trực tiếp vào bài toán: “Dân '
                 'số tỉnh A là $1\\,452\\,800$ người, tỉnh B là $1\\,425\\,900$ người, tỉnh C là '
                 '$1\\,542\\,000$ người, tỉnh D là $1\\,524\\,300$ người. Tỉnh nào...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bước 1: Đếm chữ số** (Nhiều chữ số hơn '
                        '$\\rightarrow$ Lớn hơn) là kiến thức cốt lõi của Bài 14: So sánh các số có nhiều '
                        'chữ số. Cả bốn số đều có $7$ chữ số và chữ số hàng triệu là $1$. Xét hàng trăm '
                        'nghìn: tỉnh C và D có $5 > 4$. Xét tiếp hàng chục nghìn giữa C và D...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14: So sánh các số có nhiều chữ số** để giải quyết tình huống '
                 'sau: Dân số tỉnh A là $1\\,452\\,800$ người, tỉnh B là $1\\,425\\,900$ người, tỉnh C là '
                 '$1\\,542\\,000$ người, tỉnh D là $1\\,524\\,300$ người. Tỉnh nào đông dân nhất? Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Cả bốn số đều có $7$ chữ số và chữ số hàng triệu là $1$. Xét hàng trăm nghìn: tỉnh '
                        'C và D có $5 > 4$. Xét tiếp hàng chục nghìn giữa C và D: $4 > 2$ nên '
                        '$1\\,542\\,000$...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 14: So sánh các số có nhiều chữ số: Cả bốn số đều có $7$ '
                        'chữ số và chữ số hàng triệu là $1$.\n'
                        'Xét hàng trăm nghìn: tỉnh C và D có $5 > 4$.\n'
                        'Xét tiếp hàng chục nghìn giữa C và D: $4 > 2$ nên $1\\,542\\,000$ lớn nhất. Vậy '
                        '**tỉnh C** đông dân nhất.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong các số $650\\,000$; $605\\,000$; $655\\,000$; $565\\,000$, số lớn nhất là số nào '
                 '(viết số liền)?',
            'answer': ['655000'],
            'unit': None,
            'solution': 'So sánh hàng trăm nghìn và chục nghìn ta thấy số lớn nhất là **$655000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd03-so-co-nhieu-chu-so',
  'context_title': 'Chủ đề 3: Số có nhiều chữ số',
  'context': 'SGK Toán 4 · Chủ đề 3: Số có nhiều chữ số (đến lớp triệu); hàng và lớp; làm tròn; dãy số tự '
             'nhiên.',
  'title': 'Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung',
  'icon': '♾️',
  'description': 'Nhận biết dãy số tự nhiên 0, 1, 2, 3, ... và các đặc điểm cơ bản của dãy số tự nhiên.',
  'requirements': ['Nhận biết được số tự nhiên và dãy số tự nhiên $0, 1, 2, 3, 4, \\dots$',
                   'Nắm vững đặc điểm: $0$ là số tự nhiên bé nhất, không có số tự nhiên lớn nhất.',
                   'Tìm được số liền trước (trừ $1$) và số liền sau (cộng $1$) của một số tự nhiên.'],
  'definition': '- Các số $0, 1, 2, 3, 4, \\dots, 1\\,000, \\dots$ là các **số tự nhiên**. Viết theo thứ tự '
                'từ bé đến lớn ta được **dãy số tự nhiên**: $0, 1, 2, 3, 4, 5, \\dots$\n'
                '- **Đặc điểm**:\n'
                '  - Số **$0$** là số tự nhiên **bé nhất** (số $0$ không có số tự nhiên liền trước).\n'
                '  - **Không có** số tự nhiên **lớn nhất** (thêm $1$ vào bất kỳ số nào cũng được số tự nhiên '
                'liền sau).\n'
                '  - Hai số tự nhiên liên tiếp hơn kém nhau **$1$ đơn vị**.',
  'theory': '### 1. Số liền trước và số liền sau\n'
            '- Thêm $1$ vào một số tự nhiên ta được **số liền sau** của nó.\n'
            '- Bớt $1$ ở một số tự nhiên (khác $0$) ta được **số liền trước** của nó.\n'
            '### 2. Biểu diễn trên tia số\n'
            '- Điểm $0$ ở gốc tia số; số đứng bên trái bé hơn số đứng bên phải.',
  'formulas': [{'category': 'I. Dãy số tự nhiên',
                'items': [{'name': 'Tập hợp',
                           'formula': '$0, 1, 2, 3, 4, \\dots$ (bé nhất là $0$, không có lớn nhất)'},
                          {'name': 'Hai số liên tiếp',
                           'formula': '$\\text{Số liền trước} = n - 1$ ($n > 0$) · $\\text{Số liền sau} = n '
                                      '+ 1$'}]}],
  'example': 'Tìm ba số tự nhiên liên tiếp biết số ở giữa là $999\\,999$.',
  'example_answer': 'Số liền trước của $999\\,999$ là $999\\,998$; số liền sau của $999\\,999$ là '
                    '$1\\,000\\,000$.\n'
                    'Vậy ba số tự nhiên liên tiếp đó là: **$999\\,998$; $999\\,999$; $1\\,000\\,000$**.',
  'real_life': '- Đếm số thứ tự vé xếp hàng, số trang sách hoặc số bước chân trên đồng hồ đếm bước.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số tự nhiên bé nhất là số nào?',
            'options': ['$0$', '$1$', '$10$', 'Không có số bé nhất'],
            'answer': 0,
            'solution': 'Trong dãy số tự nhiên $0, 1, 2, 3, \\dots$, số bé nhất là **$0$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai số tự nhiên liên tiếp hơn kém nhau bao nhiêu đơn vị?',
            'options': ['$2$ đơn vị', '$1$ đơn vị', '$10$ đơn vị', '$0$ đơn vị'],
            'answer': 1,
            'solution': 'Hai số tự nhiên liên tiếp hơn kém nhau **$1$ đơn vị**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tập hợp**?',
            'options': ['$\\text{Số liền trước} = n - 1$ ($n > 0$) · $\\text{Số liền sau} = n + 1$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$0, 1, 2, 3, 4, \\dots$ (bé nhất là $0$, không có lớn nhất)',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 15, 16: Làm quen với dãy số tự nhiên và luyện '
                        'tập chung, **Tập hợp** được xác định bởi: $0, 1, 2, 3, 4, \\dots$ (bé nhất là $0$, '
                        'không có lớn nhất).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung**, nội dung/biểu thức '
                 '$\\text{Số liền trước} = n - 1$ ($n > 0$) · $\\text{Số liền sau} = n + 1$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Tập hợp', 'Phân tích số', 'Quy tắc 5', 'Hai số liên tiếp'],
            'answer': 3,
            'solution': 'Trong Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung, biểu thức/quy '
                        'tắc $\\text{Số liền trước} = n - 1$ ($n > 0$) · $\\text{Số liền sau} = n + 1$ chính '
                        'là nội dung của **Hai số liên tiếp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số tự nhiên nào dưới đây không có số tự nhiên liền trước?',
            'options': ['$0$', '$1$', '$100$', '$999\\,999$'],
            'answer': 0,
            'solution': 'Vì $0$ là số tự nhiên bé nhất nên số **$0$** không có số tự nhiên liền trước.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung** (Chủ đề 3: Số có '
                 'nhiều chữ số), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Nhận biết được số tự nhiên và dãy số tự nhiên $0, 1, 2, 3, 4, \\dots$',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập '
                        'chung: Nhận biết được số tự nhiên và dãy số tự nhiên $0, 1, 2, 3, 4, \\dots$'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số tự nhiên lớn nhất là $999\\,999\\,999$."',
            'answer': False,
            'solution': 'Thêm $1$ vào bất kỳ số tự nhiên nào cũng được số lớn hơn nên **không có** số tự '
                        'nhiên lớn nhất $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung**, quy tắc **Tập hợp** '
                 'được xác định bởi $0, 1, 2, 3, 4, \\dots$ (bé nhất là $0$, không có lớn nhất) và áp dụng '
                 'trực tiếp vào bài toán: “Tìm ba số tự nhiên liên tiếp biết số ở giữa là $999\\,999$.”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tập hợp** ($0, 1, 2, 3, 4, \\dots$ (bé nhất là $0$, '
                        'không có lớn nhất)) là kiến thức cốt lõi của Bài 15, 16: Làm quen với dãy số tự '
                        'nhiên và luyện tập chung. Số liền trước của $999\\,999$ là $999\\,998$; số liền sau '
                        'của $999\\,999$ là $1\\,000\\,000$. Vậy ba số tự nhiên liên tiếp đó là: '
                        '**$999\\,998$; $999\\,999$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung** để giải '
                 'quyết tình huống sau: Tìm ba số tự nhiên liên tiếp biết số ở giữa là $999\\,999$. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Số liền trước của $999\\,999$ là $999\\,998$; số liền sau của $999\\,999$ là '
                        '$1\\,000\\,000$. Vậy ba số tự nhiên liên tiếp đó là: **$999\\,998$; $999\\,999$; '
                        '$1\\,000\\,000$...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 15, 16: Làm quen với dãy số tự nhiên và luyện tập chung: '
                        'Số liền trước của $999\\,999$ là $999\\,998$; số liền sau của $999\\,999$ là '
                        '$1\\,000\\,000$.\n'
                        'Vậy ba số tự nhiên liên tiếp đó là: **$999\\,998$; $999\\,999$; $1\\,000\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tự nhiên liền sau của số $2\\,099\\,999$ (viết số liền).',
            'answer': ['2100000'],
            'unit': None,
            'solution': 'Ta có $2\\,099\\,999 + 1 = 2\\,100\\,000$.\nĐáp số: **$2100000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd04-don-vi-do-dai-luong',
  'context_title': 'Chủ đề 4: Một số đơn vị đo đại lượng',
  'context': 'SGK Toán 4 · Chủ đề 4: Các đơn vị đo khối lượng (yến, tạ, tấn), diện tích (dm², m², mm²) và '
             'thời gian (giây, thế kỉ).',
  'title': 'Bài 17: Yến, tạ, tấn',
  'icon': '⚖️',
  'description': 'Nhận biết các đơn vị đo khối lượng lớn hơn ki-lô-gam (yến, tạ, tấn) và mối quan hệ quy '
                 'đổi.',
  'requirements': ['Nhận biết các đơn vị đo khối lượng lớn hơn $\\text{kg}$ là **yến, tạ, tấn**.',
                   'Nắm vững mối quan hệ: $1\\text{ yến} = 10\\text{ kg}$, $1\\text{ tạ} = 10\\text{ yến} = '
                   '100\\text{ kg}$, $1\\text{ tấn} = 10\\text{ tạ} = 1\\,000\\text{ kg}$.',
                   'Thực hiện được chuyển đổi đơn vị và giải bài toán thực tế.'],
  'definition': '- Để đo khối lượng các vật nặng hàng chục, hàng trăm, hàng nghìn ki-lô-gam, người ta dùng '
                'các đơn vị **yến, tạ, tấn**.\n'
                '- **Quan hệ**:\n'
                '  - $1\\text{ yến} = 10\\text{ kg}$\n'
                '  - $1\\text{ tạ} = 10\\text{ yến} = 100\\text{ kg}$\n'
                '  - $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1\\,000\\text{ kg}$',
  'theory': '### 1. Quy luật đơn vị đo khối lượng liền kề\n'
            '- Theo thứ tự từ lớn đến bé: **tấn $\\rightarrow$ tạ $\\rightarrow$ yến $\\rightarrow$ '
            '$\\text{kg}$**.\n'
            '- Hai đơn vị đo khối lượng liền kề luôn gấp (hoặc kém) nhau **$10$ lần**.\n'
            '### 2. Đổi số đo có hai tên đơn vị\n'
            '- Ví dụ: $3\\text{ tấn } 5\\text{ tạ} = 3\\,000\\text{ kg} + 500\\text{ kg} = 3\\,500\\text{ '
            'kg}$.',
  'formulas': [{'category': 'I. Bảng quy đổi khối lượng',
                'items': [{'name': 'Đổi sang kg',
                           'formula': '$1\\text{ yến} = 10\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · '
                                      '$1\\text{ tấn} = 1\\,000\\text{ kg}$'},
                          {'name': 'Quan hệ liền kề',
                           'formula': '$1\\text{ tấn} = 10\\text{ tạ}$ · $1\\text{ tạ} = 10\\text{ yến}$'}]}],
  'example': 'Một xe tải chở được tối đa $4$ tấn hàng. Trên xe đã chất $25$ bao gạo, mỗi bao nặng $1$ tạ. '
             'Hỏi xe đó còn chở thêm được nhiều nhất bao nhiêu ki-lô-gam hàng nữa?',
  'example_answer': 'Đổi $4\\text{ tấn} = 4\\,000\\text{ kg}$; $1\\text{ tạ} = 100\\text{ kg}$.\n'
                    'Khối lượng $25$ bao gạo trên xe là: $100 \\times 25 = 2\\,500\\text{ (kg)}$.\n'
                    'Xe còn chở thêm được: $4\\,000 - 2\\,500 = 1\\,500\\text{ (kg)}$.',
  'real_life': '- Cân nông sản (lúa, ngô, khoai) theo yến, tạ; tính tải trọng cầu đường và xe tải theo tấn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ tấn} = \\dots\\text{ kg}$?',
            'options': ['$10\\text{ kg}$',
                        '$1\\,000\\text{ kg}$',
                        '$100\\text{ kg}$',
                        '$10\\,000\\text{ kg}$'],
            'answer': 1,
            'solution': 'Ta có $1\\text{ tấn} = 1\\,000\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $2\\text{ tạ} = \\dots\\text{ kg}$?',
            'options': ['$20\\text{ kg}$', '$2\\,000\\text{ kg}$', '$200\\text{ kg}$', '$2\\text{ kg}$'],
            'answer': 2,
            'solution': 'Vì $1\\text{ tạ} = 100\\text{ kg}$ nên $2\\text{ tạ} = 200\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Yến, tạ, tấn**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Đổi sang kg**?',
            'options': ['$1\\text{ tấn} = 10\\text{ tạ}$ · $1\\text{ tạ} = 10\\text{ yến}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$1\\text{ yến} = 10\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ tấn} '
                        '= 1\\,000\\text{ kg}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Yến, tạ, tấn, **Đổi sang kg** được xác '
                        'định bởi: $1\\text{ yến} = 10\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · '
                        '$1\\text{ tấn} = 1\\,000\\text{ kg}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Yến, tạ, tấn**, nội dung/biểu thức $1\\text{ tấn} = 10\\text{ tạ}$ · '
                 '$1\\text{ tạ} = 10\\text{ yến}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quan hệ liền kề', 'Đổi sang kg', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 17: Yến, tạ, tấn, biểu thức/quy tắc $1\\text{ tấn} = 10\\text{ tạ}$ · '
                        '$1\\text{ tạ} = 10\\text{ yến}$ chính là nội dung của **Quan hệ liền kề**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm $5\\text{ tạ } 7\\text{ yến} = \\dots\\text{ kg}$ là:',
            'options': ['$57$', '$570$', '$507$', '$5\\,070$'],
            'answer': 1,
            'solution': 'Ta có $5\\text{ tạ} = 500\\text{ kg}$, $7\\text{ yến} = 70\\text{ kg} \\Rightarrow '
                        '500 + 70 = 570\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Yến, tạ, tấn** (Chủ đề 4: Một số đơn vị đo đại lượng), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Nhận biết các đơn vị đo khối lượng lớn hơn $\\text{kg}$ là **yến, tạ, tấn**.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Yến, tạ, tấn: Nhận biết các đơn vị đo khối lượng '
                        'lớn hơn $\\text{kg}$ là **yến, tạ, tấn**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$2\\text{ tấn } 30\\text{ kg} = 230\\text{ kg}$."',
            'answer': False,
            'solution': 'Vì $2\\text{ tấn} = 2\\,000\\text{ kg}$ nên $2\\text{ tấn } 30\\text{ kg} = '
                        '2\\,030\\text{ kg}$, không phải $230\\text{ kg}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 17: Yến, tạ, tấn**, quy tắc **Đổi sang kg** được xác định bởi $1\\text{ yến} = '
                 '10\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ tấn} = 1\\,000\\text{ kg}$ và '
                 'áp dụng trực tiếp vào bài toán: “Một xe tải chở được tối đa $4$ tấn hàng. Trên xe đã chất '
                 '$25$ bao gạo, mỗi bao nặng $1$ tạ. Hỏi xe đó còn chở thêm được nhiều nhất bao nhiêu...”. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đổi sang kg** ($1\\text{ yến} = 10\\text{ kg}$ · '
                        '$1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ tấn} = 1\\,000\\text{ kg}$) là kiến '
                        'thức cốt lõi của Bài 17: Yến, tạ, tấn. Đổi $4\\text{ tấn} = 4\\,000\\text{ kg}$; '
                        '$1\\text{ tạ} = 100\\text{ kg}$. Khối lượng $25$ bao gạo trên xe là: $100 \\times '
                        '25 = 2\\,500\\text{ (kg)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Yến, tạ, tấn** để giải quyết tình huống sau: Một xe tải chở '
                 'được tối đa $4$ tấn hàng. Trên xe đã chất $25$ bao gạo, mỗi bao nặng $1$ tạ. Hỏi xe đó còn '
                 'chở thêm được nhiều nhất bao nhiêu ki-lô-gam hàng nữa? Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Đổi $4\\text{ tấn} = 4\\,000\\text{ kg}$; $1\\text{ tạ} = 100\\text{ kg}$. Khối '
                        'lượng $25$ bao gạo trên xe là: $100 \\times 25 = 2\\,500\\text{ (kg)}$. Xe còn '
                        'chở...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 17: Yến, tạ, tấn: Đổi $4\\text{ tấn} = 4\\,000\\text{ '
                        'kg}$; $1\\text{ tạ} = 100\\text{ kg}$.\n'
                        'Khối lượng $25$ bao gạo trên xe là: $100 \\times 25 = 2\\,500\\text{ (kg)}$.\n'
                        'Xe còn chở thêm được: $4\\,000 - 2\\,500 = 1\\,500\\text{ (kg)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một xe tải chở được tối đa $4$ tấn hàng. Đã chất lên xe $25$ bao gạo, mỗi bao nặng $1$ tạ. '
                 'Hỏi xe còn chở thêm được bao nhiêu ki-lô-gam hàng (viết số liền)?',
            'answer': ['1500'],
            'unit': 'kg',
            'solution': 'Đổi $4\\text{ tấn} = 4\\,000\\text{ kg}$; $25\\text{ tạ} = 2\\,500\\text{ kg}$. Còn '
                        'chở thêm được: $4\\,000 - 2\\,500 = 1\\,500\\text{ (kg)}$.\n'
                        'Đáp số: **$1500$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd04-don-vi-do-dai-luong',
  'context_title': 'Chủ đề 4: Một số đơn vị đo đại lượng',
  'context': 'SGK Toán 4 · Chủ đề 4: Các đơn vị đo khối lượng (yến, tạ, tấn), diện tích (dm², m², mm²) và '
             'thời gian (giây, thế kỉ).',
  'title': 'Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông',
  'icon': '🟩',
  'description': 'Nhận biết các đơn vị đo diện tích dm², m², mm² và quy luật hai đơn vị diện tích liền kề '
                 'gấp kém nhau 100 lần.',
  'requirements': ['Nhận biết được các đơn vị đo diện tích: đề-xi-mét vuông ($\\text{dm}^2$), mét vuông '
                   '($\\text{m}^2$), mi-li-mét vuông ($\\text{mm}^2$).',
                   'Nắm vững mối quan hệ giữa các đơn vị đo diện tích liền kề hơn kém nhau $100$ lần.',
                   'Chuyển đổi đơn vị diện tích và giải bài toán lát gạch nền nhà.'],
  'definition': '- **Đề-xi-mét vuông** ($\\text{dm}^2$), **mét vuông** ($\\text{m}^2$), **mi-li-mét vuông** '
                '($\\text{mm}^2$) lần lượt là diện tích của hình vuông có cạnh dài $1\\text{ dm}$, $1\\text{ '
                'm}$, $1\\text{ mm}$.\n'
                '- **Quy tắc vàng**: Hai đơn vị đo diện tích liền kề ($\\text{m}^2 - \\text{dm}^2 - '
                '\\text{cm}^2 - \\text{mm}^2$) luôn gấp hoặc kém nhau **$100$ lần**.',
  'theory': '### 1. Mối quan hệ giữa các đơn vị diện tích\n'
            '- $1\\text{ m}^2 = 100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$.\n'
            '- $1\\text{ dm}^2 = 100\\text{ cm}^2$.\n'
            '- $1\\text{ cm}^2 = 100\\text{ mm}^2$.\n'
            '### 2. Chuyển đổi số đo diện tích phức hợp\n'
            '- Ví dụ: $2\\text{ m}^2\\text{ } 8\\text{ dm}^2 = 200\\text{ dm}^2 + 8\\text{ dm}^2 = '
            '208\\text{ dm}^2$ (chú ý chữ số $0$ ở hàng chục).',
  'formulas': [{'category': 'I. Quan hệ đơn vị đo diện tích',
                'items': [{'name': 'Liền kề gấp 100 lần',
                           'formula': '$1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ '
                                      'cm}^2$ · $1\\text{ cm}^2 = 100\\text{ mm}^2$'},
                          {'name': 'Cách 1 đơn vị',
                           'formula': '$1\\text{ m}^2 = 10\\,000\\text{ cm}^2$ · $1\\text{ dm}^2 = '
                                      '10\\,000\\text{ mm}^2$'}]}],
  'example': 'Một căn phòng hình chữ nhật dài $6\\text{ m}$, rộng $4\\text{ m}$. Người ta lát nền căn phòng '
             'bằng các viên gạch hình vuông cạnh $4\\text{ dm}$. Hỏi cần bao nhiêu viên gạch?',
  'example_answer': 'Diện tích nền phòng là: $6 \\times 4 = 24\\text{ (m}^2\\text{)} = 2\\,400\\text{ '
                    '(dm}^2\\text{)}$.\n'
                    'Diện tích $1$ viên gạch là: $4 \\times 4 = 16\\text{ (dm}^2\\text{)}$.\n'
                    'Số viên gạch cần dùng là: $2\\,400 : 16 = 150\\text{ (viên)}$.',
  'real_life': '- Tính diện tích căn hộ chung cư ($\\text{m}^2$), diện tích viên gạch lát nền '
               '($\\text{dm}^2$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ m}^2 = \\dots\\text{ dm}^2$?',
            'options': ['$10$', '$1\\,000$', '$100$', '$10\\,000$'],
            'answer': 2,
            'solution': 'Hai đơn vị diện tích liền kề gấp nhau $100$ lần: $1\\text{ m}^2 = 100\\text{ '
                        'dm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $1\\text{ cm}^2 = \\dots\\text{ mm}^2$?',
            'options': ['$10$', '$1\\,000$', '$1$', '$100$'],
            'answer': 3,
            'solution': 'Ta có $1\\text{ cm}^2 = 100\\text{ mm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Liền kề gấp 100 lần**?',
            'options': ['$1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ cm}^2$ · '
                        '$1\\text{ cm}^2 = 100\\text{ mm}^2$',
                        '$1\\text{ m}^2 = 10\\,000\\text{ cm}^2$ · $1\\text{ dm}^2 = 10\\,000\\text{ mm}^2$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét '
                        'vuông, **Liền kề gấp 100 lần** được xác định bởi: $1\\text{ m}^2 = 100\\text{ '
                        'dm}^2$ · $1\\text{ dm}^2 = 100\\text{ cm}^2$ · $1\\text{ cm}^2 = 100\\text{ '
                        'mm}^2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông**, nội dung/biểu thức '
                 '$1\\text{ m}^2 = 10\\,000\\text{ cm}^2$ · $1\\text{ dm}^2 = 10\\,000\\text{ mm}^2$ là quy '
                 'tắc hoặc công thức của mục nào sau đây?',
            'options': ['Liền kề gấp 100 lần', 'Cách 1 đơn vị', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông, biểu thức/quy tắc '
                        '$1\\text{ m}^2 = 10\\,000\\text{ cm}^2$ · $1\\text{ dm}^2 = 10\\,000\\text{ mm}^2$ '
                        'chính là nội dung của **Cách 1 đơn vị**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm $2\\text{ m}^2\\text{ } 8\\text{ dm}^2 = \\dots\\text{ '
                 'dm}^2$ là:',
            'options': ['$28$', '$280$', '$208$', '$2\\,008$'],
            'answer': 2,
            'solution': 'Vì $2\\text{ m}^2 = 200\\text{ dm}^2$ nên $200 + 8 = 208\\text{ (dm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông** (Chủ đề 4: Một số đơn vị '
                 'đo đại lượng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Nhận biết được các đơn vị đo diện tích: đề-xi-mét vuông ($\\text{dm}^2$), mét vuông '
                        '($\\text{m}^2$), mi-li-mét vuông ($\\text{mm}^2$).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông: Nhận '
                        'biết được các đơn vị đo diện tích: đề-xi-mét vuông ($\\text{dm}^2$), mét vuông '
                        '($\\text{m}^2$), mi-li-mét vuông ($\\text{mm}^2$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$500\\text{ dm}^2 = 5\\text{ m}^2$."',
            'answer': True,
            'solution': 'Vì $100\\text{ dm}^2 = 1\\text{ m}^2$ nên $500\\text{ dm}^2 = 5\\text{ m}^2$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông**, quy tắc **Liền kề gấp 100 '
                 'lần** được xác định bởi $1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ '
                 'cm}^2$ · $1\\text{ cm}^2 = 100\\text{ mm}^2$ và áp dụng trực tiếp vào bài toán: “Một căn '
                 'phòng hình chữ nhật dài $6\\text{ m}$, rộng $4\\text{ m}$. Người ta lát nền căn phòng bằng '
                 'các viên gạch hình vuông cạnh $4\\text{ dm}$...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Liền kề gấp 100 lần** ($1\\text{ m}^2 = 100\\text{ '
                        'dm}^2$ · $1\\text{ dm}^2 = 100\\text{ cm}^2$ · $1\\text{ cm}^2 = 100\\text{ mm}^2$) '
                        'là kiến thức cốt lõi của Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông. Diện '
                        'tích nền phòng là: $6 \\times 4 = 24\\text{ (m}^2\\text{)} = 2\\,400\\text{ '
                        '(dm}^2\\text{)}$. Diện tích $1$ viên gạch là: $4 \\times 4 = 16\\text{ '
                        '(dm}^2\\text{)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông** để giải quyết '
                 'tình huống sau: Một căn phòng hình chữ nhật dài $6\\text{ m}$, rộng $4\\text{ m}$. Người '
                 'ta lát nền căn phòng bằng các viên gạch hình vuông cạnh $4\\text{ dm}$. Hỏi cần bao nhiêu '
                 'viên gạch? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Diện tích nền phòng là: $6 \\times 4 = 24\\text{ (m}^2\\text{)} = 2\\,400\\text{ '
                        '(dm}^2\\text{)}$. Diện tích $1$ viên gạch là: $4 \\times 4 = 16\\text{ '
                        '(dm}^2\\text{)}$...',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 18: Đề-xi-mét vuông, mét vuông, mi-li-mét vuông: Diện '
                        'tích nền phòng là: $6 \\times 4 = 24\\text{ (m}^2\\text{)} = 2\\,400\\text{ '
                        '(dm}^2\\text{)}$.\n'
                        'Diện tích $1$ viên gạch là: $4 \\times 4 = 16\\text{ (dm}^2\\text{)}$.\n'
                        'Số viên gạch cần dùng là: $2\\,400 : 16 = 150\\text{ (viên)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bức tường hình chữ nhật có chiều dài $5\\text{ m}$, chiều rộng $3\\text{ m}$. Diện '
                 'tích bức tường đó bằng bao nhiêu đề-xi-mét vuông (viết số liền)?',
            'answer': ['1500'],
            'unit': 'dm²',
            'solution': 'Diện tích bức tường là: $5 \\times 3 = 15\\text{ (m}^2\\text{)} = 1\\,500\\text{ '
                        '(dm}^2\\text{)}$.\n'
                        'Đáp số: **$1500$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd04-don-vi-do-dai-luong',
  'context_title': 'Chủ đề 4: Một số đơn vị đo đại lượng',
  'context': 'SGK Toán 4 · Chủ đề 4: Các đơn vị đo khối lượng (yến, tạ, tấn), diện tích (dm², m², mm²) và '
             'thời gian (giây, thế kỉ).',
  'title': 'Bài 19: Giây, thế kỉ',
  'icon': '⏳',
  'description': 'Nhận biết đơn vị đo thời gian giây, thế kỉ; mối quan hệ với phút, năm và cách xác định thế '
                 'kỉ của một năm.',
  'requirements': ['Nắm vững mối quan hệ: $1\\text{ phút} = 60\\text{ giây}$ và $1\\text{ thế kỉ} = '
                   '100\\text{ năm}$.',
                   'Xác định đúng một năm lịch sử thuộc thế kỉ thứ mấy (thường viết bằng chữ số La Mã).',
                   'Thực hiện được đổi đơn vị thời gian và giải toán thực tế.'],
  'definition': '- **Giây**: $1\\text{ phút} = 60\\text{ giây}$ (kim giây chạy $1$ vòng mặt đồng hồ là $60$ '
                'giây $= 1$ phút).\n'
                '- **Thế kỉ**: $1\\text{ thế kỉ} = 100\\text{ năm}$.\n'
                '  - Từ năm $1$ đến năm $100$ là **thế kỉ $\\text{I}$**.\n'
                '  - Từ năm $1901$ đến năm $2000$ là **thế kỉ $\\text{XX}$** ($20$).\n'
                '  - Từ năm $2001$ đến năm $2100$ là **thế kỉ $\\text{XXI}$** ($21$).',
  'theory': '### 1. Mẹo xác định nhanh thế kỉ của một năm\n'
            '- Nếu năm kết thúc bằng hai chữ số $00$ (năm tròn trăm): gạch bỏ hai chữ số $00$ cuối, phần còn '
            'lại chính là số thế kỉ (ví dụ năm $2000 \\rightarrow$ thế kỉ $20$ hay $\\text{XX}$).\n'
            '- Nếu năm **không** kết thúc bằng $00$: gạch bỏ hai chữ số cuối rồi **cộng thêm $1$** vào phần '
            'còn lại (ví dụ năm $1945 \\rightarrow 19 + 1 = 20 \\rightarrow$ thế kỉ $\\text{XX}$).',
  'formulas': [{'category': 'I. Thời gian',
                'items': [{'name': 'Giây và phút',
                           'formula': '$1\\text{ phút} = 60\\text{ giây}$ · $1\\text{ giờ} = 60\\text{ phút} '
                                      '= 3\\,600\\text{ giây}$'},
                          {'name': 'Thế kỉ và năm', 'formula': '$1\\text{ thế kỉ} = 100\\text{ năm}$'},
                          {'name': 'Tìm thế kỉ của năm abcd (cd ≠ 00)',
                           'formula': '$\\text{Thế kỉ} = \\overline{ab} + 1$',
                           'note': 'Ví dụ: năm $1010 \\rightarrow 10 + 1 = 11$ (thế kỉ $\\text{XI}$)'}]}],
  'example': 'Bác Hồ đọc Bản Tuyên ngôn Độc lập vào năm $1945$. Năm $1945$ thuộc thế kỉ nào?',
  'example_answer': 'Từ năm $1901$ đến năm $2000$ là thế kỉ $20$ ($19 + 1 = 20$).\n'
                    'Vậy năm $1945$ thuộc **thế kỉ $\\text{XX}$**.',
  'real_life': '- Bấm đồng hồ tính thành tích chạy $100\\text{ m}$ bằng giây; xác định niên đại các sự kiện '
               'lịch sử dân tộc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một thế kỉ có bao nhiêu năm và một phút có bao nhiêu giây?',
            'options': ['$10$ năm; $60$ giây',
                        '$100$ năm; $100$ giây',
                        '$1\\,000$ năm; $60$ giây',
                        '$100$ năm; $60$ giây'],
            'answer': 3,
            'solution': 'Ta có $1\\text{ thế kỉ} = 100\\text{ năm}$ và $1\\text{ phút} = 60\\text{ giây}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Năm $2026$ thuộc thế kỉ thứ mấy?',
            'options': ['Thế kỉ $\\text{XXI}$',
                        'Thế kỉ $\\text{XX}$',
                        'Thế kỉ $\\text{XIX}$',
                        'Thế kỉ $\\text{XXII}$'],
            'answer': 0,
            'solution': 'Từ năm $2001$ đến năm $2100$ thuộc **thế kỉ $\\text{XXI}$** ($20 + 1 = 21$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19: Giây, thế kỉ**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Giây và phút**?',
            'options': ['$1\\text{ thế kỉ} = 100\\text{ năm}$',
                        '$1\\text{ phút} = 60\\text{ giây}$ · $1\\text{ giờ} = 60\\text{ phút} = '
                        '3\\,600\\text{ giây}$',
                        '$\\text{Thế kỉ} = \\overline{ab} + 1$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19: Giây, thế kỉ, **Giây và phút** được xác '
                        'định bởi: $1\\text{ phút} = 60\\text{ giây}$ · $1\\text{ giờ} = 60\\text{ phút} = '
                        '3\\,600\\text{ giây}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Giây, thế kỉ**, nội dung/biểu thức $1\\text{ thế kỉ} = 100\\text{ năm}$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Giây và phút', 'Tìm thế kỉ của năm abcd (cd ≠ 00)', 'Thế kỉ và năm', 'Phân tích số'],
            'answer': 2,
            'solution': 'Trong Bài 19: Giây, thế kỉ, biểu thức/quy tắc $1\\text{ thế kỉ} = 100\\text{ năm}$ '
                        'chính là nội dung của **Thế kỉ và năm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Năm $1010$, Vua Lý Thái Tổ dời đô về Thăng Long. Năm đó thuộc thế kỉ nào?',
            'options': ['Thế kỉ $\\text{X}$',
                        'Thế kỉ $\\text{IX}$',
                        'Thế kỉ $\\text{XII}$',
                        'Thế kỉ $\\text{XI}$'],
            'answer': 3,
            'solution': 'Từ năm $1001$ đến năm $1100$ là **thế kỉ $\\text{XI}$** ($10 + 1 = 11$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Giây, thế kỉ** (Chủ đề 4: Một số đơn vị đo đại lượng), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nắm vững mối quan hệ: $1\\text{ phút} = 60\\text{ giây}$ và $1\\text{ thế kỉ} = '
                        '100\\text{ năm}$.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 19: Giây, thế kỉ: Nắm vững mối quan hệ: $1\\text{ '
                        'phút} = 60\\text{ giây}$ và $1\\text{ thế kỉ} = 100\\text{ năm}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$3\\text{ phút } 20\\text{ giây} = 320\\text{ giây}$."',
            'answer': False,
            'solution': 'Vì $3\\text{ phút} = 3 \\times 60 = 180\\text{ giây}$ nên $180 + 20 = 200\\text{ '
                        'giây}$, không phải $320\\text{ giây}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 19: Giây, thế kỉ**, quy tắc **Giây và phút** được xác định bởi $1\\text{ phút} '
                 '= 60\\text{ giây}$ · $1\\text{ giờ} = 60\\text{ phút} = 3\\,600\\text{ giây}$ và áp dụng '
                 'trực tiếp vào bài toán: “Bác Hồ đọc Bản Tuyên ngôn Độc lập vào năm $1945$. Năm $1945$ '
                 'thuộc thế kỉ nào?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giây và phút** ($1\\text{ phút} = 60\\text{ giây}$ · '
                        '$1\\text{ giờ} = 60\\text{ phút} = 3\\,600\\text{ giây}$) là kiến thức cốt lõi của '
                        'Bài 19: Giây, thế kỉ. Từ năm $1901$ đến năm $2000$ là thế kỉ $20$ ($19 + 1 = 20$). '
                        'Vậy năm $1945$ thuộc **thế kỉ $\\text{XX}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19: Giây, thế kỉ** để giải quyết tình huống sau: Bác Hồ đọc Bản '
                 'Tuyên ngôn Độc lập vào năm $1945$. Năm $1945$ thuộc thế kỉ nào? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Từ năm $1901$ đến năm $2000$ là thế kỉ $20$ ($19 + 1 = 20$). Vậy năm $1945$ thuộc '
                        '**thế kỉ $\\text{XX}$**.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 19: Giây, thế kỉ: Từ năm $1901$ đến năm $2000$ là thế kỉ '
                        '$20$ ($19 + 1 = 20$).\n'
                        'Vậy năm $1945$ thuộc **thế kỉ $\\text{XX}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Vận động viên chạy hết quãng đường trong $2\\text{ phút } 15\\text{ giây}$. Hỏi vận động '
                 'viên đó đã chạy trong bao nhiêu giây?',
            'answer': ['135'],
            'unit': 'giây',
            'solution': 'Đổi $2\\text{ phút} = 120\\text{ giây}$; $120 + 15 = 135\\text{ (giây)}$.\n'
                        'Đáp số: **$135\\text{ giây}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd04-don-vi-do-dai-luong',
  'context_title': 'Chủ đề 4: Một số đơn vị đo đại lượng',
  'context': 'SGK Toán 4 · Chủ đề 4: Các đơn vị đo khối lượng (yến, tạ, tấn), diện tích (dm², m², mm²) và '
             'thời gian (giây, thế kỉ).',
  'title': 'Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng',
  'icon': '🧭',
  'description': 'Tổng hợp chuyển đổi, ước lượng và giải toán thực tế với các đơn vị khối lượng, diện tích, '
                 'thời gian.',
  'requirements': ['Phân biệt rõ hệ số quy đổi giữa đơn vị khối lượng (liền kề gấp $10$), diện tích (liền kề '
                   'gấp $100$) và thời gian ($1\\text{ phút} = 60\\text{ giây}, 1\\text{ thế kỉ} = '
                   '100\\text{ năm}$).',
                   'Ước lượng hợp lý số đo khối lượng, diện tích, thời gian của các sự vật quen thuộc.',
                   'Giải được bài toán thực tế kết hợp diện tích và sản lượng thu hoạch.'],
  'definition': '- **Khối lượng**: $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1\\,000\\text{ kg}$.\n'
                '- **Diện tích**: $1\\text{ m}^2 = 100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$; $1\\text{ '
                'cm}^2 = 100\\text{ mm}^2$.\n'
                '- **Thời gian**: $1\\text{ phút} = 60\\text{ giây}$; $1\\text{ thế kỉ} = 100\\text{ năm}$.',
  'theory': '### 1. Tránh các lỗi nhầm lẫn thường gặp\n'
            '- Không nhầm $1\\text{ m}^2 = 10\\text{ dm}^2$ (đúng phải là $100\\text{ dm}^2$).\n'
            '- Không nhầm $1\\text{ phút} = 100\\text{ giây}$ (đúng phải là $60\\text{ giây}$).\n'
            '- Năm tròn trăm như năm $1900$ là năm cuối cùng của thế kỉ $\\text{XIX}$ ($19$), còn năm $1901$ '
            'mới bắt đầu thế kỉ $\\text{XX}$ ($20$).',
  'formulas': [{'category': 'I. Bảng tổng hợp quy đổi',
                'items': [{'name': 'Khối lượng',
                           'formula': '$1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ '
                                      'kg}$ · $1\\text{ yến} = 10\\text{ kg}$'},
                          {'name': 'Diện tích',
                           'formula': '$1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ '
                                      'cm}^2$ · $1\\text{ cm}^2 = 100\\text{ mm}^2$'},
                          {'name': 'Thời gian',
                           'formula': '$1\\text{ thế kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ '
                                      'giây}$'}]}],
  'example': 'Đổi các đơn vị sau: a) $4\\text{ tấn } 15\\text{ kg} = \\dots\\text{ kg}$; b) $5\\text{ '
             'dm}^2\\text{ } 6\\text{ cm}^2 = \\dots\\text{ cm}^2$.',
  'example_answer': 'a) $4\\text{ tấn } 15\\text{ kg} = 4\\,000\\text{ kg} + 15\\text{ kg} = 4\\,015\\text{ '
                    'kg}$.\n'
                    'b) $5\\text{ dm}^2\\text{ } 6\\text{ cm}^2 = 500\\text{ cm}^2 + 6\\text{ cm}^2 = '
                    '506\\text{ cm}^2$.',
  'real_life': '- Tính diện tích mặt sàn căn phòng và số viên gạch cần mua; quy đổi sản lượng nông sản từ '
               'ki-lô-gam sang tạ, tấn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $3\\text{ tấn } 5\\text{ tạ} = \\dots\\text{ kg}$?',
            'options': ['$3\\,500\\text{ kg}$',
                        '$350\\text{ kg}$',
                        '$3\\,050\\text{ kg}$',
                        '$35\\,000\\text{ kg}$'],
            'answer': 0,
            'solution': 'Ta có $3\\text{ tấn} = 3\\,000\\text{ kg}$ và $5\\text{ tạ} = 500\\text{ kg} '
                        '\\Rightarrow 3\\,500\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $\\dfrac{1}{4}$ thế kỉ bằng bao nhiêu năm?',
            'options': ['$20$ năm', '$25$ năm', '$40$ năm', '$50$ năm'],
            'answer': 1,
            'solution': 'Vì $1\\text{ thế kỉ} = 100\\text{ năm}$ nên $\\dfrac{1}{4}$ thế kỉ là $100 : 4 = '
                        '25\\text{ (năm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại '
                 'lượng**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Khối lượng**?',
            'options': ['$1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ cm}^2$ · '
                        '$1\\text{ cm}^2 = 100\\text{ mm}^2$',
                        '$1\\text{ thế kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ giây}$',
                        '$1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ '
                        'yến} = 10\\text{ kg}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 20, 21: Thực hành và luyện tập chung về đơn '
                        'vị đo đại lượng, **Khối lượng** được xác định bởi: $1\\text{ tấn} = 1\\,000\\text{ '
                        'kg}$ · $1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ yến} = 10\\text{ kg}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng**, nội dung/biểu '
                 'thức $1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ cm}^2$ · $1\\text{ '
                 'cm}^2 = 100\\text{ mm}^2$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khối lượng', 'Thời gian', 'Phân tích số', 'Diện tích'],
            'answer': 3,
            'solution': 'Trong Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng, biểu '
                        'thức/quy tắc $1\\text{ m}^2 = 100\\text{ dm}^2$ · $1\\text{ dm}^2 = 100\\text{ '
                        'cm}^2$ · $1\\text{ cm}^2 = 100\\text{ mm}^2$ chính là nội dung của **Diện tích**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các bạn chạy thi $100\\text{ m}$: Nam chạy hết $18$ giây, Minh chạy hết '
                 '$\\dfrac{1}{3}$ phút, Hải chạy hết $16$ giây. Ai chạy nhanh nhất?',
            'options': ['Hải', 'Nam', 'Minh', 'Nam và Minh bằng nhau'],
            'answer': 0,
            'solution': 'Đổi $\\dfrac{1}{3}\\text{ phút} = 60 : 3 = 20\\text{ giây}$. Thời gian ít nhất là '
                        '$16$ giây nên **Hải** chạy nhanh nhất.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng** (Chủ đề 4: Một '
                 'số đơn vị đo đại lượng), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Phân biệt rõ hệ số quy đổi giữa đơn vị khối lượng (liền kề gấp $10$), diện tích '
                        '(liền kề gấp $100$) và thời gian ($1\\text{ phút} = 60\\text{ giây}, 1\\text{ thế '
                        'kỉ} = 100\\text{ năm}$).',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại '
                        'lượng: Phân biệt rõ hệ số quy đổi giữa đơn vị khối lượng (liền kề gấp $10$), diện '
                        'tích (liền kề gấp $100$) và thời gian ($1\\text{ phút} = 60\\text{ giây}, 1\\text{ '
                        'thế kỉ} = 100\\text{ năm}$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$1\\text{ dm}^2 = 100\\text{ cm}^2$."',
            'answer': True,
            'solution': 'Hình vuông cạnh $1\\text{ dm} = 10\\text{ cm}$ có diện tích $10 \\times 10 = '
                        '100\\text{ cm}^2$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng**, quy tắc **Khối '
                 'lượng** được xác định bởi $1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ tạ} = '
                 '100\\text{ kg}$ · $1\\text{ yến} = 10\\text{ kg}$ và áp dụng trực tiếp vào bài toán: “Đổi '
                 'các đơn vị sau: a) $4\\text{ tấn } 15\\text{ kg} = \\dots\\text{ kg}$; b) $5\\text{ '
                 'dm}^2\\text{ } 6\\text{ cm}^2 = \\dots\\text{ cm}^2$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khối lượng** ($1\\text{ tấn} = 1\\,000\\text{ kg}$ · '
                        '$1\\text{ tạ} = 100\\text{ kg}$ · $1\\text{ yến} = 10\\text{ kg}$) là kiến thức cốt '
                        'lõi của Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng. a) '
                        '$4\\text{ tấn } 15\\text{ kg} = 4\\,000\\text{ kg} + 15\\text{ kg} = 4\\,015\\text{ '
                        'kg}$. b) $5\\text{ dm}^2\\text{ } 6\\text{ cm}^2 = 500\\text{ cm}^2 + 6\\text{ '
                        'cm}^2 = 506\\text{ cm}^2$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại lượng** để '
                 'giải quyết tình huống sau: Đổi các đơn vị sau: a) $4\\text{ tấn } 15\\text{ kg} = '
                 '\\dots\\text{ kg}$; b) $5\\text{ dm}^2\\text{ } 6\\text{ cm}^2 = \\dots\\text{ cm}^2$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'a) $4\\text{ tấn } 15\\text{ kg} = 4\\,000\\text{ kg} + 15\\text{ kg} = '
                        '4\\,015\\text{ kg}$. b) $5\\text{ dm}^2\\text{ } 6\\text{ cm}^2 = 500\\text{ cm}^2 '
                        '+ 6\\text{ cm}^2 = 506\\text{ cm}^2$...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 20, 21: Thực hành và luyện tập chung về đơn vị đo đại '
                        'lượng: a) $4\\text{ tấn } 15\\text{ kg} = 4\\,000\\text{ kg} + 15\\text{ kg} = '
                        '4\\,015\\text{ kg}$.\n'
                        'b) $5\\text{ dm}^2\\text{ } 6\\text{ cm}^2 = 500\\text{ cm}^2 + 6\\text{ cm}^2 = '
                        '506\\text{ cm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một căn phòng hình chữ nhật dài $6\\text{ m}$, rộng $4\\text{ m}$. Người ta lát nền bằng '
                 'các viên gạch hình vuông cạnh $4\\text{ dm}$. Hỏi cần bao nhiêu viên gạch để lát kín nền '
                 'phòng?',
            'answer': ['150'],
            'unit': 'viên',
            'solution': 'Diện tích phòng: $6 \\times 4 = 24\\text{ m}^2 = 2\\,400\\text{ dm}^2$. Diện tích '
                        '$1$ viên gạch: $4 \\times 4 = 16\\text{ dm}^2$. Số viên gạch: $2\\,400 : 16 = '
                        '150\\text{ (viên)}$.\n'
                        'Đáp số: **$150\\text{ viên}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd05-phep-cong-va-phep-tru',
  'context_title': 'Chủ đề 5: Phép cộng và phép trừ',
  'context': 'SGK Toán 4 · Chủ đề 5: Phép cộng, phép trừ các số có nhiều chữ số; bài toán tìm hai số khi '
             'biết tổng và hiệu.',
  'title': 'Bài 22: Phép cộng các số có nhiều chữ số',
  'icon': '➕',
  'description': 'Đặt tính và thực hiện phép cộng các số tự nhiên có nhiều chữ số (đến lớp triệu).',
  'requirements': ['Đặt tính thẳng cột và tính đúng phép cộng các số có nhiều chữ số (không nhớ và có nhớ).',
                   'Cộng nhẩm được các số tròn triệu, tròn trăm nghìn.',
                   'Giải được bài toán thực tế có phép cộng các số lớn.'],
  'definition': '- Khi đặt tính cộng các số có nhiều chữ số ($a + b$), ta viết các chữ số cùng một hàng '
                'thẳng cột với nhau.\n'
                '- Thực hiện cộng lần lượt từ phải sang trái, nếu tổng một hàng $\\ge 10$ thì nhớ sang hàng '
                'liền trước bên trái.',
  'theory': '### 1. Phép cộng không nhớ\n'
            '- Ví dụ: $425\\,316 + 172\\,483 = 597\\,799$.\n'
            '### 2. Phép cộng có nhớ\n'
            '- Ví dụ: $367\\,528 + 241\\,736 = 609\\,264$ (chú ý cộng thêm $1$ ở các hàng có nhớ từ hàng bên '
            'phải sang).',
  'formulas': [{'category': 'I. Quy tắc cộng viết',
                'items': [{'name': 'Đặt tính & Tính',
                           'formula': 'Thẳng cột theo hàng · Cộng từ phải sang trái · Nhớ sang hàng liền '
                                      'trước'}]}],
  'example': 'Đặt tính rồi tính: $367\\,528 + 241\\,736$.',
  'example_answer': 'Thực hiện cộng từ hàng đơn vị sang hàng trăm nghìn:\n'
                    '$367\\,528 + 241\\,736 = 609\\,264$.',
  'real_life': '- Tính tổng dân số của hai tỉnh hoặc tổng kinh phí xây dựng hai công trình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $425\\,316 + 172\\,483$ là:',
            'options': ['$597\\,899$', '$597\\,799$', '$587\\,799$', '$252\\,833$'],
            'answer': 1,
            'solution': 'Cộng từng hàng không nhớ ta được **$597\\,799$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $367\\,528 + 241\\,736$ là:',
            'options': ['$608\\,264$', '$509\\,264$', '$609\\,264$', '$609\\,164$'],
            'answer': 2,
            'solution': 'Cộng có nhớ ở hàng đơn vị, hàng trăm và hàng chục nghìn $\\rightarrow$ '
                        '**$609\\,264$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 22: Phép cộng các số có nhiều chữ số**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Đặt tính & Tính**?',
            'options': ['$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$',
                        'Thẳng cột theo hàng · Cộng từ phải sang trái · Nhớ sang hàng liền trước'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 22: Phép cộng các số có nhiều chữ số, **Đặt '
                        'tính & Tính** được xác định bởi: Thẳng cột theo hàng · Cộng từ phải sang trái · Nhớ '
                        'sang hàng liền trước.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Phép cộng các số có nhiều chữ số**, nội dung/biểu thức Thẳng cột theo hàng '
                 '· Cộng từ phải sang trái · Nhớ sang hàng liền trước là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Đặt tính & Tính', 'Phân tích số', 'Quy tắc 5', 'Quy tắc'],
            'answer': 0,
            'solution': 'Trong Bài 22: Phép cộng các số có nhiều chữ số, biểu thức/quy tắc Thẳng cột theo '
                        'hàng · Cộng từ phải sang trái · Nhớ sang hàng liền trước chính là nội dung của '
                        '**Đặt tính & Tính**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số bị trừ $x$ biết $x - 145\\,200 = 354\\,800$:',
            'options': ['$209\\,600$', '$500\\,000$', '$490\\,000$', '$499\\,000$'],
            'answer': 1,
            'solution': 'Số bị trừ $x = 354\\,800 + 145\\,200 = 500\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Phép cộng các số có nhiều chữ số** (Chủ đề 5: Phép cộng và phép trừ), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Đặt tính thẳng cột và tính đúng phép cộng các số có nhiều chữ số (không nhớ và có '
                        'nhớ).',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 22: Phép cộng các số có nhiều chữ số: Đặt tính thẳng '
                        'cột và tính đúng phép cộng các số có nhiều chữ số (không nhớ và có nhớ).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tổng của $650\\,000$ và $350\\,000$ bằng $1\\,000\\,000$."',
            'answer': True,
            'solution': 'Ta có $650\\,000 + 350\\,000 = 1\\,000\\,000$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 22: Phép cộng các số có nhiều chữ số**, quy tắc **Đặt tính & Tính** được xác '
                 'định bởi Thẳng cột theo hàng · Cộng từ phải sang trái · Nhớ sang hàng liền trước và áp '
                 'dụng trực tiếp vào bài toán: “Đặt tính rồi tính: $367\\,528 + 241\\,736$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đặt tính & Tính** (Thẳng cột theo hàng · Cộng từ '
                        'phải sang trái · Nhớ sang hàng liền trước) là kiến thức cốt lõi của Bài 22: Phép '
                        'cộng các số có nhiều chữ số. Thực hiện cộng từ hàng đơn vị sang hàng trăm nghìn: '
                        '$367\\,528 + 241\\,736 = 609\\,264$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 22: Phép cộng các số có nhiều chữ số** để giải quyết tình huống '
                 'sau: Đặt tính rồi tính: $367\\,528 + 241\\,736$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Thực hiện cộng từ hàng đơn vị sang hàng trăm nghìn: $367\\,528 + 241\\,736 = '
                        '609\\,264$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Phép cộng các số có nhiều chữ số: Thực hiện cộng từ '
                        'hàng đơn vị sang hàng trăm nghìn:\n'
                        '$367\\,528 + 241\\,736 = 609\\,264$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tháng thứ nhất nhà máy sản xuất được $245\\,000$ sản phẩm, tháng thứ hai sản xuất được '
                 'nhiều hơn tháng thứ nhất $35\\,000$ sản phẩm. Hỏi tháng thứ hai nhà máy sản xuất được bao '
                 'nhiêu sản phẩm (viết số liền)?',
            'answer': ['280000'],
            'unit': 'sản phẩm',
            'solution': 'Tháng thứ hai sản xuất được: $245\\,000 + 35\\,000 = 280\\,000\\text{ (sản '
                        'phẩm)}$.\n'
                        'Đáp số: **$280000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd05-phep-cong-va-phep-tru',
  'context_title': 'Chủ đề 5: Phép cộng và phép trừ',
  'context': 'SGK Toán 4 · Chủ đề 5: Phép cộng, phép trừ các số có nhiều chữ số; bài toán tìm hai số khi '
             'biết tổng và hiệu.',
  'title': 'Bài 23: Phép trừ các số có nhiều chữ số',
  'icon': '➖',
  'description': 'Đặt tính và thực hiện phép trừ các số tự nhiên có nhiều chữ số và thử lại bằng phép cộng.',
  'requirements': ['Đặt tính thẳng cột và tính đúng phép trừ các số có nhiều chữ số (không nhớ và có nhớ).',
                   'Biết thử lại phép trừ bằng phép cộng ($\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị '
                   'trừ}$).',
                   'Giải được bài toán thực tế có phép trừ các số có nhiều chữ số.'],
  'definition': '- Khi đặt tính trừ, ta viết số trừ dưới số bị trừ sao cho các chữ số ở cùng một hàng thẳng '
                'cột với nhau.\n'
                '- Trừ lần lượt từ phải sang trái; nếu chữ số ở số bị trừ bé hơn thì mượn $10$ ở hàng liền '
                'trước và nhớ $1$ vào số trừ ở hàng liền trước.',
  'theory': '### 1. Phép trừ không nhớ và có nhớ\n'
            '- Ví dụ: $865\\,279 - 450\\,237 = 415\\,042$.\n'
            '- Ví dụ có nhớ: $720\\,405 - 318\\,627 = 401\\,778$.\n'
            '### 2. Kiểm tra kết quả\n'
            '- Lấy hiệu vừa tìm được cộng với số trừ, nếu đúng bằng số bị trừ thì phép tính đúng.',
  'formulas': [{'category': 'I. Phép trừ',
                'items': [{'name': 'Thử lại',
                           'formula': '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$'},
                          {'name': 'Tìm thành phần',
                           'formula': '$\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu}$'}]}],
  'example': 'Đặt tính rồi tính và thử lại: $720\\,405 - 318\\,627$.',
  'example_answer': 'Ta có $720\\,405 - 318\\,627 = 401\\,778$.\n'
                    'Thử lại: $401\\,778 + 318\\,627 = 720\\,405$ (đúng).',
  'real_life': '- Tính chênh lệch diện tích hoặc dân số giữa hai địa phương; tính số tiền quỹ còn lại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $865\\,279 - 450\\,237$ là:',
            'options': ['$415\\,142$', '$405\\,042$', '$415\\,042$', '$315\\,042$'],
            'answer': 2,
            'solution': 'Trừ từng hàng từ phải sang trái ta được **$415\\,042$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $720\\,405 - 318\\,627$ là:',
            'options': ['$402\\,778$', '$401\\,878$', '$1\\,039\\,032$', '$401\\,778$'],
            'answer': 3,
            'solution': 'Ta có $720\\,405 - 318\\,627 = 401\\,778$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Phép trừ các số có nhiều chữ số**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Thử lại**?',
            'options': ['$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        '$\\text{Số trừ} = \\text{Số bị trừ} - \\text{Hiệu}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Phép trừ các số có nhiều chữ số, **Thử '
                        'lại** được xác định bởi: $\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Phép trừ các số có nhiều chữ số**, nội dung/biểu thức $\\text{Số trừ} = '
                 '\\text{Số bị trừ} - \\text{Hiệu}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thử lại', 'Tìm thành phần', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 23: Phép trừ các số có nhiều chữ số, biểu thức/quy tắc $\\text{Số trừ} = '
                        '\\text{Số bị trừ} - \\text{Hiệu}$ chính là nội dung của **Tìm thành phần**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x + 240\\,500 = 600\\,000$:',
            'options': ['$360\\,500$', '$459\\,500$', '$359\\,500$', '$840\\,500$'],
            'answer': 2,
            'solution': 'Ta có $x = 600\\,000 - 240\\,500 = 359\\,500$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Phép trừ các số có nhiều chữ số** (Chủ đề 5: Phép cộng và phép trừ), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Đặt tính thẳng cột và tính đúng phép trừ các số có nhiều chữ số (không nhớ và có '
                        'nhớ).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Phép trừ các số có nhiều chữ số: Đặt tính thẳng '
                        'cột và tính đúng phép trừ các số có nhiều chữ số (không nhớ và có nhớ).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$1\\,000\\,000 - 350\\,000 = 750\\,000$."',
            'answer': False,
            'solution': 'Ta có $1\\,000\\,000 - 350\\,000 = 650\\,000$, không phải $750\\,000$ '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 23: Phép trừ các số có nhiều chữ số**, quy tắc **Thử lại** được xác định bởi '
                 '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$ và áp dụng trực tiếp vào bài toán: '
                 '“Đặt tính rồi tính và thử lại: $720\\,405 - 318\\,627$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thử lại** ($\\text{Hiệu} + \\text{Số trừ} = '
                        '\\text{Số bị trừ}$) là kiến thức cốt lõi của Bài 23: Phép trừ các số có nhiều chữ '
                        'số. Ta có $720\\,405 - 318\\,627 = 401\\,778$. Thử lại: $401\\,778 + 318\\,627 = '
                        '720\\,405$ (đúng).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Phép trừ các số có nhiều chữ số** để giải quyết tình huống '
                 'sau: Đặt tính rồi tính và thử lại: $720\\,405 - 318\\,627$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $720\\,405 - 318\\,627 = 401\\,778$. Thử lại: $401\\,778 + 318\\,627 = '
                        '720\\,405$ (đúng).',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Phép trừ các số có nhiều chữ số: Ta có $720\\,405 - '
                        '318\\,627 = 401\\,778$.\n'
                        'Thử lại: $401\\,778 + 318\\,627 = 720\\,405$ (đúng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Quãng đường từ Hà Nội đến Thành phố Hồ Chí Minh dài khoảng $1\\,726\\text{ km}$, trong đó '
                 'quãng đường từ Hà Nội đến Đà Nẵng dài $766\\text{ km}$. Hỏi quãng đường từ Đà Nẵng đến '
                 'Thành phố Hồ Chí Minh dài bao nhiêu ki-lô-mét?',
            'answer': ['960'],
            'unit': 'km',
            'solution': 'Quãng đường từ Đà Nẵng đến TP. Hồ Chí Minh dài: $1\\,726 - 766 = 960\\text{ '
                        '(km)}$.\n'
                        'Đáp số: **$960\\text{ km}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd05-phep-cong-va-phep-tru',
  'context_title': 'Chủ đề 5: Phép cộng và phép trừ',
  'context': 'SGK Toán 4 · Chủ đề 5: Phép cộng, phép trừ các số có nhiều chữ số; bài toán tìm hai số khi '
             'biết tổng và hiệu.',
  'title': 'Bài 24: Tính chất giao hoán và kết hợp của phép cộng',
  'icon': '🔄',
  'description': 'Vận dụng tính chất giao hoán và tính chất kết hợp của phép cộng để tính nhẩm và tính bằng '
                 'cách thuận tiện.',
  'requirements': ['Phát biểu và viết được công thức chữ của tính chất giao hoán ($a + b = b + a$) và tính '
                   'chất kết hợp ($(a + b) + c = a + (b + c)$).',
                   'Biết tính chất cộng với số $0$: $a + 0 = 0 + a = a$.',
                   'Vận dụng nhóm các số hạng tạo thành số tròn chục, tròn trăm, tròn nghìn để tính nhanh.'],
  'definition': '- **Tính chất giao hoán**: Khi đổi chỗ các số hạng trong một tổng thì tổng không thay đổi: '
                '$a + b = b + a$.\n'
                '- **Tính chất kết hợp**: Khi cộng một tổng hai số với số thứ ba, ta có thể cộng số thứ nhất '
                'với tổng của số thứ hai và số thứ ba: $(a + b) + c = a + (b + c)$.\n'
                '- **Cộng với $0$**: Bất kỳ số nào cộng với $0$ cũng bằng chính số đó: $a + 0 = 0 + a = a$.',
  'theory': '### 1. Ứng dụng tính bằng cách thuận tiện nhất\n'
            '- Khi tính tổng của nhiều số, ta dùng tính chất giao hoán và kết hợp để ghép các cặp số có tận '
            'cùng cộng lại bằng $10, 100, 1\\,000, \\dots$\n'
            '- Ví dụ: $168 + 279 + 32 = (168 + 32) + 279 = 200 + 279 = 479$.\n'
            '- Ví dụ: $2\\,475 + 3\\,618 + 525 + 382 = (2\\,475 + 525) + (3\\,618 + 382) = 3\\,000 + 4\\,000 '
            '= 7\\,000$.',
  'formulas': [{'category': 'I. Các tính chất của phép cộng',
                'items': [{'name': 'Giao hoán', 'formula': '$a + b = b + a$'},
                          {'name': 'Kết hợp', 'formula': '$(a + b) + c = a + (b + c)$'},
                          {'name': 'Cộng với 0', 'formula': '$a + 0 = 0 + a = a$'}]}],
  'example': 'Tính bằng cách thuận tiện nhất: $2\\,475 + 3\\,618 + 525 + 382$.',
  'example_answer': 'Ta nhóm các số hạng tạo thành tổng tròn nghìn:\n'
                    '$(2\\,475 + 525) + (3\\,618 + 382) = 3\\,000 + 4\\,000 = 7\\,000$.',
  'real_life': '- Cộng nhẩm nhanh các khoản chi tiêu bằng cách ghép các khoản lẻ thành số tròn chục nghìn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức $(a + b) + c = a + (b + c)$ thể hiện tính chất gì của phép cộng?',
            'options': ['Tính chất giao hoán', 'Tính chất phân phối', 'Cộng với số $0$', 'Tính chất kết hợp'],
            'answer': 3,
            'solution': 'Đó là **tính chất kết hợp** của phép cộng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhanh: $168 + 279 + 32 = ?$',
            'options': ['$479$', '$469$', '$489$', '$579$'],
            'answer': 0,
            'solution': 'Ta nhóm $(168 + 32) + 279 = 200 + 279 = 479$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24: Tính chất giao hoán và kết hợp của phép cộng**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Giao hoán**?',
            'options': ['$(a + b) + c = a + (b + c)$',
                        '$a + b = b + a$',
                        '$a + 0 = 0 + a = a$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24: Tính chất giao hoán và kết hợp của phép '
                        'cộng, **Giao hoán** được xác định bởi: $a + b = b + a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Tính chất giao hoán và kết hợp của phép cộng**, nội dung/biểu thức $(a + '
                 'b) + c = a + (b + c)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Giao hoán', 'Cộng với 0', 'Kết hợp', 'Phân tích số'],
            'answer': 2,
            'solution': 'Trong Bài 24: Tính chất giao hoán và kết hợp của phép cộng, biểu thức/quy tắc $(a + '
                        'b) + c = a + (b + c)$ chính là nội dung của **Kết hợp**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm để $345 + 198 = 198 + \\dots$ là:',
            'options': ['$198$', '$543$', '$0$', '$345$'],
            'answer': 3,
            'solution': 'Theo tính chất giao hoán của phép cộng: $345 + 198 = 198 + 345$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Tính chất giao hoán và kết hợp của phép cộng** (Chủ đề 5: Phép cộng và '
                 'phép trừ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Phát biểu và viết được công thức chữ của tính chất giao hoán ($a + b = b + a$) và '
                        'tính chất kết hợp ($(a + b) + c = a + (b + c)$).',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 24: Tính chất giao hoán và kết hợp của phép cộng: Phát '
                        'biểu và viết được công thức chữ của tính chất giao hoán ($a + b = b + a$) và tính '
                        'chất kết hợp ($(a + b) + c = a + (b + c)$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $1\\,250 + 4\\,300 + 750 + 700$ bằng $7\\,000$."',
            'answer': True,
            'solution': 'Ta có $(1\\,250 + 750) + (4\\,300 + 700) = 2\\,000 + 5\\,000 = 7\\,000$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 24: Tính chất giao hoán và kết hợp của phép cộng**, quy tắc **Giao hoán** được '
                 'xác định bởi $a + b = b + a$ và áp dụng trực tiếp vào bài toán: “Tính bằng cách thuận tiện '
                 'nhất: $2\\,475 + 3\\,618 + 525 + 382$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giao hoán** ($a + b = b + a$) là kiến thức cốt lõi '
                        'của Bài 24: Tính chất giao hoán và kết hợp của phép cộng. Ta nhóm các số hạng tạo '
                        'thành tổng tròn nghìn: $(2\\,475 + 525) + (3\\,618 + 382) = 3\\,000 + 4\\,000 = '
                        '7\\,000$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24: Tính chất giao hoán và kết hợp của phép cộng** để giải quyết '
                 'tình huống sau: Tính bằng cách thuận tiện nhất: $2\\,475 + 3\\,618 + 525 + 382$. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Ta nhóm các số hạng tạo thành tổng tròn nghìn: $(2\\,475 + 525) + (3\\,618 + 382) = '
                        '3\\,000 + 4\\,000 = 7\\,000$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Tính chất giao hoán và kết hợp của phép cộng: Ta '
                        'nhóm các số hạng tạo thành tổng tròn nghìn:\n'
                        '$(2\\,475 + 525) + (3\\,618 + 382) = 3\\,000 + 4\\,000 = 7\\,000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức: $2\\,475 + 3\\,618 + 525 + 382$.',
            'answer': ['7000'],
            'unit': None,
            'solution': 'Nhóm $(2\\,475 + 525) + (3\\,618 + 382) = 3\\,000 + 4\\,000 = 7\\,000$.\n'
                        'Đáp số: **$7000$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd05-phep-cong-va-phep-tru',
  'context_title': 'Chủ đề 5: Phép cộng và phép trừ',
  'context': 'SGK Toán 4 · Chủ đề 5: Phép cộng, phép trừ các số có nhiều chữ số; bài toán tìm hai số khi '
             'biết tổng và hiệu.',
  'title': 'Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó',
  'icon': '🧩',
  'description': 'Công thức và phương pháp giải bài toán tìm hai số khi biết tổng và hiệu của hai số đó.',
  'requirements': ['Thuộc và áp dụng đúng hai cách tìm số lớn, số bé khi biết tổng và hiệu.',
                   'Biết vẽ sơ đồ đoạn thẳng biểu diễn tổng và hiệu của hai số.',
                   'Giải được các bài toán thực tế (tính tuổi, tính chiều dài/chiều rộng hình chữ nhật khi '
                   'biết chu vi và hiệu hai cạnh).'],
  'definition': '- Khi biết **Tổng** và **Hiệu** của hai số:\n'
                '  - **Cách 1 (Tìm số bé trước)**: $\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$; sau '
                'đó $\\text{Số lớn} = \\text{Số bé} + \\text{Hiệu}$ (hoặc $\\text{Tổng} - \\text{Số bé}$).\n'
                '  - **Cách 2 (Tìm số lớn trước)**: $\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$; '
                'sau đó $\\text{Số bé} = \\text{Số lớn} - \\text{Hiệu}$ (hoặc $\\text{Tổng} - \\text{Số '
                'lớn}$).',
  'theory': '### 1. Ý nghĩa trên sơ đồ đoạn thẳng\n'
            '- Nếu bớt ở số lớn đi phần Hiệu thì hai số bằng nhau và tổng mới bằng $2$ lần số bé: $2 \\times '
            '\\text{Số bé} = \\text{Tổng} - \\text{Hiệu}$.\n'
            '- Nếu thêm vào số bé phần Hiệu thì hai số bằng nhau và tổng mới bằng $2$ lần số lớn: $2 \\times '
            '\\text{Số lớn} = \\text{Tổng} + \\text{Hiệu}$.\n'
            '### 2. Lưu ý với bài toán hình chữ nhật\n'
            '- Tổng của chiều dài và chiều rộng chính là **nửa chu vi** ($P : 2$).',
  'formulas': [{'category': 'I. Công thức Tổng – Hiệu',
                'items': [{'name': 'Tìm số lớn',
                           'formula': '$\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$'},
                          {'name': 'Tìm số bé',
                           'formula': '$\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$'}]}],
  'example': 'Hai lớp 4A và 4B trồng được tất cả $150$ cây. Lớp 4A trồng được nhiều hơn lớp 4B là $12$ cây. '
             'Hỏi mỗi lớp trồng được bao nhiêu cây?',
  'example_answer': '- Số cây lớp 4A trồng (số lớn) là: $(150 + 12) : 2 = 81\\text{ (cây)}$.\n'
                    '- Số cây lớp 4B trồng (số bé) là: $150 - 81 = 69\\text{ (cây)}$.',
  'real_life': '- Tính tuổi của bố và con khi biết tổng số tuổi và số tuổi bố hơn con; tính số học sinh nam '
               'và nữ của lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm số lớn khi biết tổng và hiệu của hai số đó, ta tính:',
            'options': ['$(\\text{Tổng} + \\text{Hiệu}) : 2$',
                        '$(\\text{Tổng} - \\text{Hiệu}) : 2$',
                        '$\\text{Tổng} \\times \\text{Hiệu}$',
                        '$\\text{Tổng} : \\text{Hiệu}$'],
            'answer': 0,
            'solution': 'Theo công thức: $\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn tìm số bé khi biết tổng và hiệu của hai số đó, ta tính:',
            'options': ['$(\\text{Tổng} + \\text{Hiệu}) : 2$',
                        '$(\\text{Tổng} - \\text{Hiệu}) : 2$',
                        '$\\text{Tổng} - \\text{Hiệu}$',
                        '$\\text{Hiệu} : 2$'],
            'answer': 1,
            'solution': 'Theo công thức: $\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Tìm số lớn**?',
            'options': ['$\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25, 26: Tìm hai số biết tổng và hiệu của hai '
                        'số đó, **Tìm số lớn** được xác định bởi: $\\text{Số lớn} = (\\text{Tổng} + '
                        '\\text{Hiệu}) : 2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó**, nội dung/biểu thức '
                 '$\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Tìm số lớn', 'Phân tích số', 'Quy tắc 5', 'Tìm số bé'],
            'answer': 3,
            'solution': 'Trong Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó, biểu thức/quy tắc '
                        '$\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$ chính là nội dung của **Tìm số '
                        'bé**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai thùng có tất cả $250\\text{ l}$ dầu. Thùng thứ nhất có ít hơn thùng thứ hai $30\\text{ '
                 'l}$ dầu. Thùng thứ nhất có số lít dầu là:',
            'options': ['$110\\text{ l}$', '$140\\text{ l}$', '$220\\text{ l}$', '$125\\text{ l}$'],
            'answer': 0,
            'solution': 'Thùng thứ nhất là số bé: $(250 - 30) : 2 = 110\\text{ (l)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó** (Chủ đề 5: Phép cộng và '
                 'phép trừ), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Thuộc và áp dụng đúng hai cách tìm số lớn, số bé khi biết tổng và hiệu.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó: '
                        'Thuộc và áp dụng đúng hai cách tìm số lớn, số bé khi biết tổng và hiệu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Tổng của hai số là $100$, hiệu của hai số là $30$ thì số lớn là $70$."',
            'answer': False,
            'solution': 'Số lớn là $(100 + 30) : 2 = 65$, không phải $70$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó**, quy tắc **Tìm số lớn** '
                 'được xác định bởi $\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$ và áp dụng trực '
                 'tiếp vào bài toán: “Hai lớp 4A và 4B trồng được tất cả $150$ cây. Lớp 4A trồng được nhiều '
                 'hơn lớp 4B là $12$ cây. Hỏi mỗi lớp trồng được bao nhiêu cây?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tìm số lớn** ($\\text{Số lớn} = (\\text{Tổng} + '
                        '\\text{Hiệu}) : 2$) là kiến thức cốt lõi của Bài 25, 26: Tìm hai số biết tổng và '
                        'hiệu của hai số đó. - Số cây lớp 4A trồng (số lớn) là: $(150 + 12) : 2 = 81\\text{ '
                        '(cây)}$. - Số cây lớp 4B trồng (số bé) là: $150 - 81 = 69\\text{ (cây)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó** để giải '
                 'quyết tình huống sau: Hai lớp 4A và 4B trồng được tất cả $150$ cây. Lớp 4A trồng được '
                 'nhiều hơn lớp 4B là $12$ cây. Hỏi mỗi lớp trồng được bao nhiêu cây? Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số cây lớp 4A trồng (số lớn) là: $(150 + 12) : 2 = 81\\text{ (cây)}$. - Số cây '
                        'lớp 4B trồng (số bé) là: $150 - 81 = 69\\text{ (cây)}$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25, 26: Tìm hai số biết tổng và hiệu của hai số đó: - Số '
                        'cây lớp 4A trồng (số lớn) là: $(150 + 12) : 2 = 81\\text{ (cây)}$.\n'
                        '- Số cây lớp 4B trồng (số bé) là: $150 - 81 = 69\\text{ (cây)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tuổi bố và tuổi con cộng lại là $58$ tuổi. Bố hơn con $28$ tuổi. Hỏi con bao nhiêu tuổi?',
            'answer': ['15'],
            'unit': 'tuổi',
            'solution': 'Tuổi con (số bé) là: $(58 - 28) : 2 = 15\\text{ (tuổi)}$.\n'
                        'Đáp số: **$15\\text{ tuổi}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd06-vuong-goc-song-song',
  'context_title': 'Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song',
  'context': 'SGK Toán 4 · Chủ đề 6: Hai đường thẳng vuông góc, hai đường thẳng song song; hình bình hành, '
             'hình thoi.',
  'title': 'Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ',
  'icon': '📏',
  'description': 'Nhận biết hai đường thẳng vuông góc và cách dùng ê-ke để kiểm tra, vẽ hai đường thẳng '
                 'vuông góc.',
  'requirements': ['Nhận biết được hai đường thẳng vuông góc với nhau tạo thành $4$ góc vuông.',
                   'Sử dụng được ê-ke để kiểm tra hai đường thẳng có vuông góc với nhau hay không.',
                   'Vẽ được một đường thẳng đi qua một điểm cho trước và vuông góc với một đường thẳng cho '
                   'trước.'],
  'definition': '- **Hai đường thẳng vuông góc**: Khi kéo dài hai cạnh góc vuông của hình chữ nhật, ta được '
                'hai đường thẳng vuông góc với nhau.\n'
                '- Hai đường thẳng vuông góc cắt nhau tạo thành **$4$ góc vuông** (mỗi góc $90^\\circ$) có '
                'chung đỉnh.',
  'theory': '### 1. Kiểm tra hai đường thẳng vuông góc\n'
            '- Dùng góc vuông của ê-ke đặt vào góc tạo bởi hai đường thẳng. Nếu hai đường thẳng trùng với '
            'hai cạnh góc vuông của ê-ke thì chúng vuông góc với nhau.\n'
            '### 2. Vẽ đường thẳng đi qua điểm $E$ và vuông góc với đường thẳng $AB$\n'
            '- Đặt một cạnh góc vuông của ê-ke trùng với đường thẳng $AB$.\n'
            '- Dịch chuyển ê-ke dọc theo $AB$ sao cho cạnh góc vuông thứ hai của ê-ke đi qua điểm $E$, rồi '
            'vạch đường thẳng dọc theo cạnh đó.',
  'formulas': [{'category': 'I. Hai đường thẳng vuông góc',
                'items': [{'name': 'Đặc điểm', 'formula': 'Cắt nhau tạo thành $4$ góc vuông ($90^\\circ$)'},
                          {'name': 'Trong hình chữ nhật ABCD',
                           'formula': '$AB \\perp AD$ · $AB \\perp BC$ · $CD \\perp AD$ · $CD \\perp BC$'}]}],
  'example': 'Cho hình chữ nhật $ABCD$. Hãy nêu các cặp cạnh vuông góc với nhau trong hình chữ nhật đó.',
  'example_answer': 'Trong hình chữ nhật $ABCD$ có $4$ góc vuông ở $A, B, C, D$ nên có $4$ cặp cạnh vuông '
                    'góc là: **$AB$ và $AD$**, **$AB$ và $BC$**, **$BC$ và $CD$**, **$CD$ và $DA$**.',
  'real_life': '- Mép tường thẳng đứng vuông góc với mặt sàn nhà; hai thanh gỗ làm khung cửa sổ vuông góc '
               'với nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường thẳng vuông góc cắt nhau tạo thành mấy góc vuông?',
            'options': ['$1$ góc vuông', '$4$ góc vuông', '$2$ góc vuông', '$3$ góc vuông'],
            'answer': 1,
            'solution': 'Hai đường thẳng vuông góc cắt nhau tạo thành **$4$ góc vuông**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dụng cụ thường dùng cùng với thước thẳng để vẽ hai đường thẳng vuông góc là:',
            'options': ['Compa', 'Cân đĩa', 'Ê-ke', 'Nhiệt kế'],
            'answer': 2,
            'solution': 'Ta dùng **ê-ke** để kiểm tra và vẽ hai đường thẳng vuông góc.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Đặc điểm**?',
            'options': ['$AB \\perp AD$ · $AB \\perp BC$ · $CD \\perp AD$ · $CD \\perp BC$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        'Cắt nhau tạo thành $4$ góc vuông ($90^\\circ$)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 27, 28: Hai đường thẳng vuông góc và thực '
                        'hành vẽ, **Đặc điểm** được xác định bởi: Cắt nhau tạo thành $4$ góc vuông '
                        '($90^\\circ$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ**, nội dung/biểu thức $AB '
                 '\\perp AD$ · $AB \\perp BC$ · $CD \\perp AD$ · $CD \\perp BC$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Trong hình chữ nhật ABCD', 'Đặc điểm', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ, biểu thức/quy tắc $AB '
                        '\\perp AD$ · $AB \\perp BC$ · $CD \\perp AD$ · $CD \\perp BC$ chính là nội dung của '
                        '**Trong hình chữ nhật ABCD**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong hình vuông $MNPQ$, cạnh $MN$ vuông góc với những cạnh nào?',
            'options': ['Chỉ cạnh $NP$', 'Cạnh $MQ$ và cạnh $NP$', 'Chỉ cạnh $MQ$', 'Cạnh $PQ$'],
            'answer': 1,
            'solution': 'Cạnh $MN$ kề và tạo góc vuông với cả hai cạnh **$MQ$ và $NP$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ** (Chủ đề 6: Đường thẳng '
                 'vuông góc. Đường thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Nhận biết được hai đường thẳng vuông góc với nhau tạo thành $4$ góc vuông.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ: '
                        'Nhận biết được hai đường thẳng vuông góc với nhau tạo thành $4$ góc vuông.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Nếu hai đường thẳng cắt nhau tạo thành $1$ góc vuông thì $3$ góc còn lại cũng '
                 'đều là góc vuông."',
            'answer': True,
            'solution': 'Hai đường thẳng vuông góc tạo thành $4$ góc vuông $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ**, quy tắc **Đặc điểm** được '
                 'xác định bởi Cắt nhau tạo thành $4$ góc vuông ($90^\\circ$) và áp dụng trực tiếp vào bài '
                 'toán: “Cho hình chữ nhật $ABCD$. Hãy nêu các cặp cạnh vuông góc với nhau trong hình chữ '
                 'nhật đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đặc điểm** (Cắt nhau tạo thành $4$ góc vuông '
                        '($90^\\circ$)) là kiến thức cốt lõi của Bài 27, 28: Hai đường thẳng vuông góc và '
                        'thực hành vẽ. Trong hình chữ nhật $ABCD$ có $4$ góc vuông ở $A, B, C, D$ nên có $4$ '
                        'cặp cạnh vuông góc là: **$AB$ và $AD$**, **$AB$ và $BC$**, **$BC$ và $CD$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ** để giải quyết '
                 'tình huống sau: Cho hình chữ nhật $ABCD$. Hãy nêu các cặp cạnh vuông góc với nhau trong '
                 'hình chữ nhật đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Trong hình chữ nhật $ABCD$ có $4$ góc vuông ở $A, B, C, D$ nên có $4$ cặp cạnh '
                        'vuông góc là: **$AB$ và $AD$**, **$AB$ và $BC$**, **$BC$ và $CD$**, **$CD$ v...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 27, 28: Hai đường thẳng vuông góc và thực hành vẽ: Trong '
                        'hình chữ nhật $ABCD$ có $4$ góc vuông ở $A, B, C, D$ nên có $4$ cặp cạnh vuông góc '
                        'là: **$AB$ và $AD$**, **$AB$ và $BC$**, **$BC$ và $CD$**, **$CD$ và $DA$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khung cửa sổ hình chữ nhật được chia đôi bởi $1$ thanh gỗ ngang vuông góc với hai cạnh '
                 'dọc của khung cửa. Hỏi bên trong khung cửa sổ có tất cả bao nhiêu góc vuông?',
            'answer': ['8'],
            'unit': 'góc vuông',
            'solution': 'Có $4$ góc vuông ở $4$ đỉnh khung cửa và $4$ góc vuông tại hai đầu thanh gỗ ngang: '
                        '$4 + 4 = 8\\text{ (góc vuông)}$.\n'
                        'Đáp số: **$8\\text{ góc vuông}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd06-vuong-goc-song-song',
  'context_title': 'Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song',
  'context': 'SGK Toán 4 · Chủ đề 6: Hai đường thẳng vuông góc, hai đường thẳng song song; hình bình hành, '
             'hình thoi.',
  'title': 'Bài 29, 30: Hai đường thẳng song song và thực hành vẽ',
  'icon': '🛤️',
  'description': 'Nhận biết hai đường thẳng song song không bao giờ cắt nhau và cách vẽ hai đường thẳng song '
                 'song bằng ê-ke.',
  'requirements': ['Nhận biết được hai đường thẳng song song là hai đường thẳng không bao giờ cắt nhau.',
                   'Nắm vững tính chất: Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì song song '
                   'với nhau.',
                   'Vẽ được đường thẳng đi qua một điểm và song song với một đường thẳng cho trước.'],
  'definition': '- **Hai đường thẳng song song**: Kéo dài $2$ cạnh đối diện của hình chữ nhật, ta được $2$ '
                'đường thẳng song song với nhau.\n'
                '- Hai đường thẳng song song với nhau thì **không bao giờ cắt nhau** ($0$ điểm chung).\n'
                '- **Tính chất**: Nếu $a \\perp c$ và $b \\perp c$ thì $a$ song song với $b$.',
  'theory': '### 1. Nhận biết trong hình chữ nhật $ABCD$\n'
            '- Cạnh $AB$ song song với cạnh $DC$; cạnh $AD$ song song với cạnh $BC$.\n'
            '### 2. Cách vẽ đường thẳng đi qua $E$ và song song với $AB$\n'
            '- Bước 1: Dùng ê-ke vẽ đường thẳng $MN$ đi qua $E$ và vuông góc với $AB$.\n'
            '- Bước 2: Dùng ê-ke vẽ đường thẳng $CD$ đi qua $E$ và vuông góc với $MN$. Khi đó $CD$ song song '
            'với $AB$.',
  'formulas': [{'category': 'I. Hai đường thẳng song song',
                'items': [{'name': 'Đặc điểm', 'formula': 'Không bao giờ cắt nhau'},
                          {'name': 'Tính chất dùng để vẽ',
                           'formula': 'Nếu $a \\perp c$ và $b \\perp c$ thì $a$ song song với $b$'}]}],
  'example': 'Cho đường thẳng $a$ và đường thẳng $b$ cùng vuông góc với đường thẳng $d$. Hỏi đường thẳng $a$ '
             'và đường thẳng $b$ có quan hệ gì với nhau?',
  'example_answer': 'Vì hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $d$ nên **$a$ và $b$ song '
                    'song với nhau**.',
  'real_life': '- Hai thanh ray của đường tàu hỏa; các vạch kẻ phân làn trên sân chạy điền kinh; các bậc '
               'thang ngang của chiếc thang.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường thẳng song song với nhau thì:',
            'options': ['Cắt nhau tại $1$ điểm',
                        'Cắt nhau tạo thành $4$ góc vuông',
                        'Không bao giờ cắt nhau',
                        'Luôn tạo thành góc nhọn'],
            'answer': 2,
            'solution': 'Hai đường thẳng song song **không bao giờ cắt nhau**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hình chữ nhật $ABCD$, cạnh $AB$ song song với cạnh nào?',
            'options': ['Cạnh $AD$', 'Cạnh $BC$', 'Cả $AD$ và $BC$', 'Cạnh $DC$'],
            'answer': 3,
            'solution': 'Hai cạnh đối diện của hình chữ nhật song song với nhau nên $AB$ song song với '
                        '**$DC$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 29, 30: Hai đường thẳng song song và thực hành vẽ**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Đặc điểm**?',
            'options': ['Không bao giờ cắt nhau',
                        'Nếu $a \\perp c$ và $b \\perp c$ thì $a$ song song với $b$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 29, 30: Hai đường thẳng song song và thực '
                        'hành vẽ, **Đặc điểm** được xác định bởi: Không bao giờ cắt nhau.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29, 30: Hai đường thẳng song song và thực hành vẽ**, nội dung/biểu thức Nếu $a '
                 '\\perp c$ và $b \\perp c$ thì $a$ song song với $b$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Đặc điểm', 'Tính chất dùng để vẽ', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 29, 30: Hai đường thẳng song song và thực hành vẽ, biểu thức/quy tắc Nếu '
                        '$a \\perp c$ và $b \\perp c$ thì $a$ song song với $b$ chính là nội dung của **Tính '
                        'chất dùng để vẽ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai đường thẳng phân biệt $m$ và $n$ cùng vuông góc với đường thẳng $p$. Khi đó hai '
                 'đường thẳng $m$ và $n$:',
            'options': ['Vuông góc với nhau', 'Cắt nhau', 'Song song với nhau', 'Tạo thành góc tù'],
            'answer': 2,
            'solution': 'Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì **song song với nhau**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 29, 30: Hai đường thẳng song song và thực hành vẽ** (Chủ đề 6: Đường thẳng '
                 'vuông góc. Đường thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Nhận biết được hai đường thẳng song song là hai đường thẳng không bao giờ cắt '
                        'nhau.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 29, 30: Hai đường thẳng song song và thực hành vẽ: '
                        'Nhận biết được hai đường thẳng song song là hai đường thẳng không bao giờ cắt '
                        'nhau.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hai cạnh đối diện của một hình chữ nhật luôn song song và bằng nhau."',
            'answer': True,
            'solution': 'Đó là tính chất cơ bản của hình chữ nhật $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 29, 30: Hai đường thẳng song song và thực hành vẽ**, quy tắc **Đặc điểm** được '
                 'xác định bởi Không bao giờ cắt nhau và áp dụng trực tiếp vào bài toán: “Cho đường thẳng '
                 '$a$ và đường thẳng $b$ cùng vuông góc với đường thẳng $d$. Hỏi đường thẳng $a$ và đường '
                 'thẳng $b$ có quan hệ gì với nhau?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đặc điểm** (Không bao giờ cắt nhau) là kiến thức cốt '
                        'lõi của Bài 29, 30: Hai đường thẳng song song và thực hành vẽ. Vì hai đường thẳng '
                        '$a$ và $b$ cùng vuông góc với đường thẳng $d$ nên **$a$ và $b$ song song với '
                        'nhau**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 29, 30: Hai đường thẳng song song và thực hành vẽ** để giải quyết '
                 'tình huống sau: Cho đường thẳng $a$ và đường thẳng $b$ cùng vuông góc với đường thẳng $d$. '
                 'Hỏi đường thẳng $a$ và đường thẳng $b$ có quan hệ gì với nhau? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Vì hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $d$ nên **$a$ và $b$ '
                        'song song với nhau**.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 29, 30: Hai đường thẳng song song và thực hành vẽ: Vì '
                        'hai đường thẳng $a$ và $b$ cùng vuông góc với đường thẳng $d$ nên **$a$ và $b$ song '
                        'song với nhau**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một chiếc thang tre có $2$ thanh dọc và $6$ bậc thang ngang. Biết tất cả các bậc thang '
                 'ngang đều vuông góc với hai thanh dọc. Hỏi bậc thang thứ nhất song song với mấy bậc thang '
                 'ngang còn lại?',
            'answer': ['5'],
            'unit': 'bậc',
            'solution': 'Bậc thang thứ nhất song song với cả **$5$** bậc thang ngang còn lại.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd06-vuong-goc-song-song',
  'context_title': 'Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song',
  'context': 'SGK Toán 4 · Chủ đề 6: Hai đường thẳng vuông góc, hai đường thẳng song song; hình bình hành, '
             'hình thoi.',
  'title': 'Bài 31: Hình bình hành, hình thoi',
  'icon': '💠',
  'description': 'Nhận biết đặc điểm về cạnh của hình bình hành và hình thoi; tính chu vi hình bình hành, '
                 'hình thoi.',
  'requirements': ['Nhận biết được **hình bình hành** có hai cặp cạnh đối diện song song và bằng nhau.',
                   'Nhận biết được **hình thoi** có hai cặp cạnh đối diện song song và bốn cạnh có độ dài '
                   'bằng nhau.',
                   'Tính được chu vi của hình bình hành và hình thoi.'],
  'definition': '- **Hình bình hành**: có **$2$ cặp cạnh đối diện song song và bằng nhau** ($a = c, b = '
                'd$).\n'
                '- **Hình thoi**: có **$2$ cặp cạnh đối diện song song và $4$ cạnh có độ dài bằng nhau** ($a '
                '= b = c = d$).',
  'theory': '### 1. Đặc điểm và chu vi của hình bình hành\n'
            '- Trong hình bình hành $ABCD$: $AB$ song song với $DC$ và $AB = DC$; $AD$ song song với $BC$ và '
            '$AD = BC$.\n'
            '- Chu vi hình bình hành có hai cạnh kề $a, b$: $P = (a + b) \\times 2$.\n'
            '### 2. Đặc điểm và chu vi của hình thoi\n'
            '- Hình thoi $MNPQ$ có $MN = NP = PQ = QM = a$.\n'
            '- Chu vi hình thoi cạnh $a$: $P = a \\times 4$.',
  'formulas': [{'category': 'I. Hình bình hành',
                'items': [{'name': 'Đặc điểm cạnh',
                           'formula': 'Hai cặp cạnh đối diện song song và bằng nhau'},
                          {'name': 'Chu vi', 'formula': '$P = (a + b) \\times 2$'}]},
               {'category': 'II. Hình thoi',
                'items': [{'name': 'Đặc điểm cạnh',
                           'formula': 'Hai cặp cạnh đối diện song song · $4$ cạnh bằng nhau'},
                          {'name': 'Chu vi', 'formula': '$P = a \\times 4$'}]}],
  'example': 'Hình bình hành $ABCD$ có $AB = 8\\text{ cm}$, $BC = 5\\text{ cm}$. Tìm độ dài cạnh $CD, AD$ và '
             'tính chu vi hình bình hành đó.',
  'example_answer': 'Vì các cạnh đối diện của hình bình hành bằng nhau nên $CD = AB = 8\\text{ cm}$ và $AD = '
                    'BC = 5\\text{ cm}$.\n'
                    'Chu vi hình bình hành $ABCD$ là: $(8 + 5) \\times 2 = 26\\text{ (cm)}$.',
  'real_life': '- Khung con diều giấy, họa tiết thổ cẩm hoặc mắt lưới sắt B40 có dạng hình thoi; bậc cầu '
               'thang nhìn nghiêng có dạng hình bình hành.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình có hai cặp cạnh đối diện song song và bốn cạnh bằng nhau là:',
            'options': ['Hình chữ nhật', 'Hình tam giác', 'Hình tứ giác bất kỳ', 'Hình thoi'],
            'answer': 3,
            'solution': 'Đó là đặc điểm của **hình thoi**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình bình hành $ABCD$ có $AB = 8\\text{ cm}$ và $BC = 5\\text{ cm}$. Độ dài cạnh $CD$ (đối '
                 'diện với $AB$) là:',
            'options': ['$8\\text{ cm}$', '$5\\text{ cm}$', '$13\\text{ cm}$', '$3\\text{ cm}$'],
            'answer': 0,
            'solution': 'Hai cạnh đối diện của hình bình hành bằng nhau nên $CD = AB = 8\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 31: Hình bình hành, hình thoi**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Đặc điểm cạnh**?',
            'options': ['$P = (a + b) \\times 2$',
                        'Hai cặp cạnh đối diện song song và bằng nhau',
                        'Hai cặp cạnh đối diện song song · $4$ cạnh bằng nhau',
                        '$P = a \\times 4$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 31: Hình bình hành, hình thoi, **Đặc điểm '
                        'cạnh** được xác định bởi: Hai cặp cạnh đối diện song song và bằng nhau.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Hình bình hành, hình thoi**, nội dung/biểu thức $P = (a + b) \\times 2$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Đặc điểm cạnh', 'Phân tích số', 'Chu vi', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 31: Hình bình hành, hình thoi, biểu thức/quy tắc $P = (a + b) \\times 2$ '
                        'chính là nội dung của **Chu vi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình thoi có độ dài cạnh là $7\\text{ cm}$. Chu vi của hình thoi đó là:',
            'options': ['$14\\text{ cm}$', '$49\\text{ cm}$', '$21\\text{ cm}$', '$28\\text{ cm}$'],
            'answer': 3,
            'solution': 'Bốn cạnh hình thoi bằng nhau nên chu vi là: $7 \\times 4 = 28\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Hình bình hành, hình thoi** (Chủ đề 6: Đường thẳng vuông góc. Đường '
                 'thẳng song song), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được **hình bình hành** có hai cặp cạnh đối diện song song và bằng nhau.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 31: Hình bình hành, hình thoi: Nhận biết được **hình '
                        'bình hành** có hai cặp cạnh đối diện song song và bằng nhau.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hình bình hành nào cũng có $4$ cạnh dài bằng nhau."',
            'answer': False,
            'solution': 'Hình bình hành chỉ có các cặp cạnh **đối diện** bằng nhau; hai cạnh kề nhau không '
                        'nhất thiết bằng nhau $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 31: Hình bình hành, hình thoi**, quy tắc **Đặc điểm cạnh** được xác định bởi '
                 'Hai cặp cạnh đối diện song song và bằng nhau và áp dụng trực tiếp vào bài toán: “Hình bình '
                 'hành $ABCD$ có $AB = 8\\text{ cm}$, $BC = 5\\text{ cm}$. Tìm độ dài cạnh $CD, AD$ và tính '
                 'chu vi hình bình hành đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Đặc điểm cạnh** (Hai cặp cạnh đối diện song song và '
                        'bằng nhau) là kiến thức cốt lõi của Bài 31: Hình bình hành, hình thoi. Vì các cạnh '
                        'đối diện của hình bình hành bằng nhau nên $CD = AB = 8\\text{ cm}$ và $AD = BC = '
                        '5\\text{ cm}$. Chu vi hình bình hành $ABCD$ là: $(8 + 5) \\times 2 = 26\\text{ '
                        '(cm)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 31: Hình bình hành, hình thoi** để giải quyết tình huống sau: '
                 'Hình bình hành $ABCD$ có $AB = 8\\text{ cm}$, $BC = 5\\text{ cm}$. Tìm độ dài cạnh $CD, '
                 'AD$ và tính chu vi hình bình hành đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Vì các cạnh đối diện của hình bình hành bằng nhau nên $CD = AB = 8\\text{ cm}$ và '
                        '$AD = BC = 5\\text{ cm}$. Chu vi hình bình hành $ABCD$ là: $(8 + 5) \\times 2 = '
                        '26\\text{ (cm)}$...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 31: Hình bình hành, hình thoi: Vì các cạnh đối diện của '
                        'hình bình hành bằng nhau nên $CD = AB = 8\\text{ cm}$ và $AD = BC = 5\\text{ cm}$.\n'
                        'Chu vi hình bình hành $ABCD$ là: $(8 + 5) \\times 2 = 26\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bác An làm một khung diều hình thoi, mỗi cạnh dài $35\\text{ cm}$. Hỏi bác An cần bao '
                 'nhiêu xăng-ti-mét nan tre để làm bốn cạnh của khung diều đó?',
            'answer': ['140'],
            'unit': 'cm',
            'solution': 'Tổng độ dài nan tre cần dùng là chu vi hình thoi: $35 \\times 4 = 140\\text{ '
                        '(cm)}$.\n'
                        'Đáp số: **$140\\text{ cm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd06-vuong-goc-song-song',
  'context_title': 'Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song',
  'context': 'SGK Toán 4 · Chủ đề 6: Hai đường thẳng vuông góc, hai đường thẳng song song; hình bình hành, '
             'hình thoi.',
  'title': 'Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi',
  'icon': '📐',
  'description': 'Tổng hợp kiến thức về hai đường thẳng vuông góc, song song và các bài toán chu vi hình '
                 'bình hành, hình thoi.',
  'requirements': ['So sánh điểm giống nhau và khác nhau giữa hình chữ nhật, hình vuông, hình bình hành, '
                   'hình thoi.',
                   'Vẽ hoàn chỉnh hình chữ nhật, hình vuông, hình bình hành, hình thoi trên giấy kẻ ô vuông.',
                   'Giải được bài toán tìm cạnh khi biết chu vi của hình bình hành, hình thoi.'],
  'definition': '- Cả bốn hình (**hình chữ nhật, hình vuông, hình bình hành, hình thoi**) đều có **hai cặp '
                'cạnh đối diện song song và bằng nhau**.\n'
                '- Hình vuông và hình thoi có thêm tính chất **$4$ cạnh bằng nhau**; hình chữ nhật và hình '
                'vuông có thêm tính chất **$4$ góc vuông**.',
  'theory': '### 1. Tìm cạnh của hình bình hành và hình thoi khi biết chu vi\n'
            '- Với hình thoi có chu vi $P$: độ dài một cạnh là $a = P : 4$.\n'
            '- Với hình bình hành có chu vi $P$ và một cạnh $a$: nửa chu vi là $a + b = P : 2 \\Rightarrow$ '
            'cạnh kề $b = (P : 2) - a$.',
  'formulas': [{'category': 'I. Tìm cạnh từ chu vi',
                'items': [{'name': 'Cạnh hình thoi', 'formula': '$a = P : 4$'},
                          {'name': 'Cạnh kề hình bình hành', 'formula': '$b = (P : 2) - a$'}]}],
  'example': 'Một hình bình hành có chu vi là $36\\text{ cm}$, độ dài một cạnh là $11\\text{ cm}$. Tìm độ '
             'dài cạnh kề với cạnh đó.',
  'example_answer': 'Nửa chu vi (tổng hai cạnh kề) của hình bình hành là: $36 : 2 = 18\\text{ (cm)}$.\n'
                    'Độ dài cạnh kề là: $18 - 11 = 7\\text{ (cm)}$.',
  'real_life': '- Thiết kế hàng rào, khung cửa sắt trang trí kết hợp các thanh song song, vuông góc và hình '
               'thoi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các hình sau, hình nào vừa có $4$ góc vuông vừa có $4$ cạnh bằng nhau?',
            'options': ['Hình vuông', 'Hình bình hành', 'Hình chữ nhật', 'Hình thoi'],
            'answer': 0,
            'solution': '**Hình vuông** có $4$ góc vuông và $4$ cạnh bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình thoi có chu vi bằng $40\\text{ cm}$. Độ dài mỗi cạnh của hình thoi đó là:',
            'options': ['$20\\text{ cm}$', '$10\\text{ cm}$', '$8\\text{ cm}$', '$160\\text{ cm}$'],
            'answer': 1,
            'solution': 'Độ dài cạnh hình thoi là: $40 : 4 = 10\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 32: Luyện tập chung về vuông góc, song song, hình bình '
                 'hành, hình thoi**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Cạnh hình thoi**?',
            'options': ['$b = (P : 2) - a$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$a = P : 4$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 32: Luyện tập chung về vuông góc, song song, '
                        'hình bình hành, hình thoi, **Cạnh hình thoi** được xác định bởi: $a = P : 4$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi**, nội '
                 'dung/biểu thức $b = (P : 2) - a$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cạnh hình thoi', 'Phân tích số', 'Quy tắc 5', 'Cạnh kề hình bình hành'],
            'answer': 3,
            'solution': 'Trong Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi, '
                        'biểu thức/quy tắc $b = (P : 2) - a$ chính là nội dung của **Cạnh kề hình bình '
                        'hành**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình bình hành có chu vi $36\\text{ cm}$, một cạnh dài $11\\text{ cm}$. Độ dài cạnh kề '
                 'với cạnh đó là:',
            'options': ['$7\\text{ cm}$', '$14\\text{ cm}$', '$25\\text{ cm}$', '$9\\text{ cm}$'],
            'answer': 0,
            'solution': 'Tổng hai cạnh kề (nửa chu vi) là $36 : 2 = 18\\text{ (cm)}$. Cạnh kề dài: $18 - 11 '
                        '= 7\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi** '
                 '(Chủ đề 6: Đường thẳng vuông góc. Đường thẳng song song), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'So sánh điểm giống nhau và khác nhau giữa hình chữ nhật, hình vuông, hình bình '
                        'hành, hình thoi.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 32: Luyện tập chung về vuông góc, song song, hình bình '
                        'hành, hình thoi: So sánh điểm giống nhau và khác nhau giữa hình chữ nhật, hình '
                        'vuông, hình bình hành, hình thoi.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì vuông góc với '
                 'nhau."',
            'answer': False,
            'solution': 'Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì **song song** với nhau '
                        '$\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi**, quy '
                 'tắc **Cạnh hình thoi** được xác định bởi $a = P : 4$ và áp dụng trực tiếp vào bài toán: '
                 '“Một hình bình hành có chu vi là $36\\text{ cm}$, độ dài một cạnh là $11\\text{ cm}$. Tìm '
                 'độ dài cạnh kề với cạnh đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cạnh hình thoi** ($a = P : 4$) là kiến thức cốt lõi '
                        'của Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình thoi. Nửa '
                        'chu vi (tổng hai cạnh kề) của hình bình hành là: $36 : 2 = 18\\text{ (cm)}$. Độ dài '
                        'cạnh kề là: $18 - 11 = 7\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 32: Luyện tập chung về vuông góc, song song, hình bình hành, hình '
                 'thoi** để giải quyết tình huống sau: Một hình bình hành có chu vi là $36\\text{ cm}$, độ '
                 'dài một cạnh là $11\\text{ cm}$. Tìm độ dài cạnh kề với cạnh đó. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Nửa chu vi (tổng hai cạnh kề) của hình bình hành là: $36 : 2 = 18\\text{ (cm)}$. Độ '
                        'dài cạnh kề là: $18 - 11 = 7\\text{ (cm)}$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 32: Luyện tập chung về vuông góc, song song, hình bình '
                        'hành, hình thoi: Nửa chu vi (tổng hai cạnh kề) của hình bình hành là: $36 : 2 = '
                        '18\\text{ (cm)}$.\n'
                        'Độ dài cạnh kề là: $18 - 11 = 7\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bồn hoa hình bình hành có hai cạnh kề nhau dài $4\\text{ m}$ và $6\\text{ m}$. Tính '
                 'chu vi của bồn hoa đó theo đơn vị mét.',
            'answer': ['20'],
            'unit': 'm',
            'solution': 'Chu vi bồn hoa hình bình hành là: $(4 + 6) \\times 2 = 20\\text{ (m)}$.\n'
                        'Đáp số: **$20\\text{ m}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 4 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 33: Ôn tập các số đến lớp triệu',
  'icon': '🔢',
  'description': 'Hệ thống hóa kiến thức về đọc, viết, hàng và lớp, so sánh, làm tròn số đến lớp triệu; số '
                 'chẵn, số lẻ.',
  'requirements': ['Đọc, viết, xác định hàng và lớp của các số tự nhiên đến lớp triệu.',
                   'So sánh, sắp xếp và làm tròn các số đến hàng trăm nghìn, hàng triệu.',
                   'Củng cố dấu hiệu số chẵn, số lẻ và dãy số tự nhiên.'],
  'definition': '- Ba lớp từ phải sang trái: **Lớp đơn vị** (đơn vị, chục, trăm) $\\rightarrow$ **Lớp '
                'nghìn** (nghìn, chục nghìn, trăm nghìn) $\\rightarrow$ **Lớp triệu** (triệu, chục triệu, '
                'trăm triệu).\n'
                '- Số chẵn tận cùng là $0, 2, 4, 6, 8$; số lẻ tận cùng là $1, 3, 5, 7, 9$.',
  'theory': '### 1. Giá trị theo vị trí của chữ số\n'
            '- Trong số $15\\,708\\,420$: chữ số $7$ thuộc hàng trăm nghìn, lớp nghìn, có giá trị là '
            '$700\\,000$.\n'
            '### 2. Làm tròn số đến hàng trăm nghìn, hàng triệu\n'
            '- Làm tròn $2\\,750\\,000$ đến hàng triệu: chữ số hàng trăm nghìn là $7 \\ge 5 \\rightarrow '
            '3\\,000\\,000$.',
  'formulas': [{'category': 'I. Hàng và lớp',
                'items': [{'name': 'Cấu trúc', 'formula': 'Lớp triệu $\\mid$ Lớp nghìn $\\mid$ Lớp đơn vị'},
                          {'name': 'Làm tròn',
                           'formula': 'Xét chữ số ngay bên phải hàng làm tròn: $< 5$ xuống, $\\ge 5$ lên'}]}],
  'example': 'Cho số $8\\,462\\,500$. Hãy nêu hàng và lớp của chữ số $4$, sau đó làm tròn số đã cho đến hàng '
             'trăm nghìn.',
  'example_answer': 'Chữ số $4$ thuộc **hàng trăm nghìn, lớp nghìn**.\n'
                    'Chữ số hàng chục nghìn là $6 \\ge 5$ nên làm tròn đến hàng trăm nghìn được '
                    '**$8\\,500\\,000$**.',
  'real_life': '- Đọc và so sánh số liệu thống kê kinh tế, dân số các tỉnh thành.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Làm tròn số $2\\,750\\,000$ đến hàng triệu ta được:',
            'options': ['$2\\,000\\,000$', '$3\\,000\\,000$', '$2\\,800\\,000$', '$2\\,700\\,000$'],
            'answer': 1,
            'solution': 'Chữ số hàng trăm nghìn là $7 \\ge 5$ nên làm tròn lên đến hàng triệu được '
                        '**$3\\,000\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong số $34\\,506\\,789$, các chữ số thuộc lớp triệu là:',
            'options': ['$5, 0, 6$', '$7, 8, 9$', '$3, 4$', '$3, 4, 5$'],
            'answer': 2,
            'solution': 'Tách lớp $34 \\mid 506 \\mid 789$: các chữ số thuộc lớp triệu là **$3, 4$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 33: Ôn tập các số đến lớp triệu**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Cấu trúc**?',
            'options': ['Xét chữ số ngay bên phải hàng làm tròn: $< 5$ xuống, $\\ge 5$ lên',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        'Lớp triệu $\\mid$ Lớp nghìn $\\mid$ Lớp đơn vị'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 33: Ôn tập các số đến lớp triệu, **Cấu trúc** '
                        'được xác định bởi: Lớp triệu $\\mid$ Lớp nghìn $\\mid$ Lớp đơn vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33: Ôn tập các số đến lớp triệu**, nội dung/biểu thức Xét chữ số ngay bên phải '
                 'hàng làm tròn: $< 5$ xuống, $\\ge 5$ lên là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Làm tròn', 'Cấu trúc', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 33: Ôn tập các số đến lớp triệu, biểu thức/quy tắc Xét chữ số ngay bên '
                        'phải hàng làm tròn: $< 5$ xuống, $\\ge 5$ lên chính là nội dung của **Làm tròn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số lớn nhất có sáu chữ số mà tổng các chữ số bằng $15$ là:',
            'options': ['$951\\,000$', '$960\\,000$', '$690\\,000$', '$906\\,000$'],
            'answer': 1,
            'solution': 'Chữ số hàng trăm nghìn lớn nhất là $9$, hàng chục nghìn là $15 - 9 = 6$, các hàng '
                        'còn lại là $0 \\rightarrow 960\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Ôn tập các số đến lớp triệu** (Chủ đề 7: Ôn tập học kì 1), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Đọc, viết, xác định hàng và lớp của các số tự nhiên đến lớp triệu.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 33: Ôn tập các số đến lớp triệu: Đọc, viết, xác định '
                        'hàng và lớp của các số tự nhiên đến lớp triệu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số liền sau của một số lẻ luôn là một số chẵn."',
            'answer': True,
            'solution': 'Số lẻ cộng thêm $1$ luôn có tận cùng là $0, 2, 4, 6, 8$ nên là số chẵn '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 33: Ôn tập các số đến lớp triệu**, quy tắc **Cấu trúc** được xác định bởi Lớp '
                 'triệu $\\mid$ Lớp nghìn $\\mid$ Lớp đơn vị và áp dụng trực tiếp vào bài toán: “Cho số '
                 '$8\\,462\\,500$. Hãy nêu hàng và lớp của chữ số $4$, sau đó làm tròn số đã cho đến hàng '
                 'trăm nghìn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cấu trúc** (Lớp triệu $\\mid$ Lớp nghìn $\\mid$ Lớp '
                        'đơn vị) là kiến thức cốt lõi của Bài 33: Ôn tập các số đến lớp triệu. Chữ số $4$ '
                        'thuộc **hàng trăm nghìn, lớp nghìn**. Chữ số hàng chục nghìn là $6 \\ge 5$ nên làm '
                        'tròn đến hàng trăm nghìn được **$8\\,500\\,000$**...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 33: Ôn tập các số đến lớp triệu** để giải quyết tình huống sau: '
                 'Cho số $8\\,462\\,500$. Hãy nêu hàng và lớp của chữ số $4$, sau đó làm tròn số đã cho đến '
                 'hàng trăm nghìn. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Chữ số $4$ thuộc **hàng trăm nghìn, lớp nghìn**. Chữ số hàng chục nghìn là $6 \\ge '
                        '5$ nên làm tròn đến hàng trăm nghìn được **$8\\,500\\,000$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 33: Ôn tập các số đến lớp triệu: Chữ số $4$ thuộc **hàng '
                        'trăm nghìn, lớp nghìn**.\n'
                        'Chữ số hàng chục nghìn là $6 \\ge 5$ nên làm tròn đến hàng trăm nghìn được '
                        '**$8\\,500\\,000$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số chẵn lớn nhất có bốn chữ số khác nhau.',
            'answer': ['9876'],
            'unit': None,
            'solution': 'Chọn từ trái sang phải các chữ số lớn nhất khác nhau và tận cùng chẵn: **$9876$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 4 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 34: Ôn tập phép cộng, phép trừ',
  'icon': '➕',
  'description': 'Củng cố phép cộng, phép trừ các số có nhiều chữ số, tính chất phép cộng, biểu thức chứa '
                 'chữ và bài toán tổng – hiệu.',
  'requirements': ['Thực hiện thành thạo phép cộng, phép trừ các số có nhiều chữ số.',
                   'Vận dụng tính chất giao hoán, kết hợp để tính hợp lý và tính giá trị biểu thức chứa chữ.',
                   'Giải thành thạo bài toán tìm hai số khi biết tổng và hiệu của hai số đó.'],
  'definition': '- **Tính chất phép cộng**: $a + b = b + a$; $(a + b) + c = a + (b + c)$.\n'
                '- **Bài toán Tổng – Hiệu**: $\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$; '
                '$\\text{Số bé} = (\\text{Tổng} - \\text{Hiệu}) : 2$.',
  'theory': '### 1. Tính bằng cách thuận tiện\n'
            '- Nhóm các số hạng để xuất hiện số tròn trăm, tròn nghìn.\n'
            '### 2. Bài toán Tổng – Hiệu kết hợp hình học\n'
            '- Nếu biết chu vi hình chữ nhật là $P$ thì tổng chiều dài và chiều rộng là nửa chu vi $P : 2$. '
            'Kết hợp với hiệu giữa chiều dài và chiều rộng để tìm từng cạnh.',
  'formulas': [{'category': 'I. Giải toán Tổng – Hiệu',
                'items': [{'name': 'Số lớn & Số bé',
                           'formula': '$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$'},
                          {'name': 'Hình chữ nhật',
                           'formula': '$\\text{Dài} + \\text{Rộng} = \\text{Nửa chu vi} = P : 2$'}]}],
  'example': 'Hai kho chứa tất cả $6\\,500$ tấn thóc. Kho A chứa nhiều hơn kho B là $900$ tấn thóc. Hỏi mỗi '
             'kho chứa bao nhiêu tấn thóc?',
  'example_answer': '- Số thóc ở kho A (số lớn) là: $(6\\,500 + 900) : 2 = 3\\,700\\text{ (tấn)}$.\n'
                    '- Số thóc ở kho B (số bé) là: $6\\,500 - 3\\,700 = 2\\,800\\text{ (tấn)}$.',
  'real_life': '- Tính diện tích thửa ruộng khi biết chu vi và chiều dài hơn chiều rộng bao nhiêu mét.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai kho có $6\\,500$ tấn thóc, kho A nhiều hơn kho B là $900$ tấn. Số thóc ở kho A là:',
            'options': ['$2\\,800$ tấn', '$3\\,250$ tấn', '$3\\,700$ tấn', '$7\\,400$ tấn'],
            'answer': 2,
            'solution': 'Kho A (số lớn) có: $(6\\,500 + 900) : 2 = 3\\,700\\text{ (tấn)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a = 150, b = 250$, giá trị của biểu thức $a + b \\times 2$ là:',
            'options': ['$800$', '$550$', '$400$', '$650$'],
            'answer': 3,
            'solution': 'Nhân trước: $150 + 250 \\times 2 = 150 + 500 = 650$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 34: Ôn tập phép cộng, phép trừ**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Số lớn & Số bé**?',
            'options': ['$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$',
                        '$\\text{Dài} + \\text{Rộng} = \\text{Nửa chu vi} = P : 2$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 34: Ôn tập phép cộng, phép trừ, **Số lớn & Số '
                        'bé** được xác định bởi: $\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Ôn tập phép cộng, phép trừ**, nội dung/biểu thức $\\text{Dài} + '
                 '\\text{Rộng} = \\text{Nửa chu vi} = P : 2$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số lớn & Số bé', 'Hình chữ nhật', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 34: Ôn tập phép cộng, phép trừ, biểu thức/quy tắc $\\text{Dài} + '
                        '\\text{Rộng} = \\text{Nửa chu vi} = P : 2$ chính là nội dung của **Hình chữ '
                        'nhật**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của hai số chẵn liên tiếp là $46$. Hai số đó là:',
            'options': ['$20$ và $26$', '$21$ và $25$', '$22$ và $24$', '$23$ và $23$'],
            'answer': 2,
            'solution': 'Hai số chẵn liên tiếp có hiệu bằng $2$. Số bé là $(46 - 2) : 2 = 22$, số lớn là '
                        '$24$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Ôn tập phép cộng, phép trừ** (Chủ đề 7: Ôn tập học kì 1), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Thực hiện thành thạo phép cộng, phép trừ các số có nhiều chữ số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 34: Ôn tập phép cộng, phép trừ: Thực hiện thành thạo '
                        'phép cộng, phép trừ các số có nhiều chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Nếu tổng hai số là $120$ và hiệu hai số là $40$ thì số bé bằng $40$."',
            'answer': True,
            'solution': 'Số bé là $(120 - 40) : 2 = 40$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 34: Ôn tập phép cộng, phép trừ**, quy tắc **Số lớn & Số bé** được xác định bởi '
                 '$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$ và áp dụng trực tiếp vào bài '
                 'toán: “Hai kho chứa tất cả $6\\,500$ tấn thóc. Kho A chứa nhiều hơn kho B là $900$ tấn '
                 'thóc. Hỏi mỗi kho chứa bao nhiêu tấn thóc?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Số lớn & Số bé** ($\\text{Lớn} = (S + H) : 2$ · '
                        '$\\text{Bé} = (S - H) : 2$) là kiến thức cốt lõi của Bài 34: Ôn tập phép cộng, phép '
                        'trừ. - Số thóc ở kho A (số lớn) là: $(6\\,500 + 900) : 2 = 3\\,700\\text{ (tấn)}$. '
                        '- Số thóc ở kho B (số bé) là: $6\\,500 - 3\\,700 = 2\\,800\\text{ (tấn)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 34: Ôn tập phép cộng, phép trừ** để giải quyết tình huống sau: '
                 'Hai kho chứa tất cả $6\\,500$ tấn thóc. Kho A chứa nhiều hơn kho B là $900$ tấn thóc. Hỏi '
                 'mỗi kho chứa bao nhiêu tấn thóc? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['- Số thóc ở kho A (số lớn) là: $(6\\,500 + 900) : 2 = 3\\,700\\text{ (tấn)}$. - Số '
                        'thóc ở kho B (số bé) là: $6\\,500 - 3\\,700 = 2\\,800\\text{ (tấn)}$.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 34: Ôn tập phép cộng, phép trừ: - Số thóc ở kho A (số '
                        'lớn) là: $(6\\,500 + 900) : 2 = 3\\,700\\text{ (tấn)}$.\n'
                        '- Số thóc ở kho B (số bé) là: $6\\,500 - 3\\,700 = 2\\,800\\text{ (tấn)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một thửa ruộng hình chữ nhật có nửa chu vi là $150\\text{ m}$, chiều dài hơn chiều rộng '
                 '$30\\text{ m}$. Tính diện tích thửa ruộng đó theo mét vuông (viết số liền).',
            'answer': ['5400'],
            'unit': 'm²',
            'solution': 'Chiều dài: $(150 + 30) : 2 = 90\\text{ (m)}$; chiều rộng: $150 - 90 = 60\\text{ '
                        '(m)}$. Diện tích: $90 \\times 60 = 5\\,400\\text{ (m}^2\\text{)}$.\n'
                        'Đáp số: **$5400$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 4 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 35: Ôn tập hình học',
  'icon': '📐',
  'description': 'Hệ thống hóa kiến thức về góc nhọn, góc vuông, góc tù, góc bẹt; hai đường thẳng vuông góc, '
                 'song song; hình bình hành, hình thoi.',
  'requirements': ['Phân biệt chính xác góc nhọn, góc vuông, góc tù, góc bẹt qua hình vẽ và số đo góc.',
                   'Xác định đúng các cặp cạnh vuông góc và các cặp cạnh song song trong các hình phẳng.',
                   'Tính được chu vi, diện tích hình chữ nhật, hình vuông và chu vi hình bình hành, hình '
                   'thoi.'],
  'definition': '- **Góc**: $\\text{Nhọn} < 90^\\circ = \\text{Vuông} < \\text{Tù} < 180^\\circ = '
                '\\text{Bẹt}$.\n'
                '- **Hình bình hành**: $2$ cặp cạnh đối diện song song và bằng nhau.\n'
                '- **Hình thoi**: $2$ cặp cạnh đối diện song song và $4$ cạnh bằng nhau.',
  'theory': '### 1. Quan hệ vuông góc và song song trong hình chữ nhật $ABCD$\n'
            '- Các cặp cạnh đối diện song song: $AB$ và $DC$; $AD$ và $BC$.\n'
            '- Các cặp cạnh kề nhau vuông góc: $AB \\perp AD$, $AB \\perp BC$, $DC \\perp AD$, $DC \\perp '
            'BC$.\n'
            '### 2. Tổng hợp công thức chu vi và diện tích\n'
            '- Hình chữ nhật: $P = (a + b) \\times 2$, $S = a \\times b$.\n'
            '- Hình vuông: $P = a \\times 4$, $S = a \\times a$.',
  'formulas': [{'category': 'I. Góc và Tứ giác',
                'items': [{'name': 'Phân loại góc',
                           'formula': 'Nhọn ($< 90^\\circ$) · Vuông ($90^\\circ$) · Tù ($90^\\circ < \\alpha '
                                      '< 180^\\circ$) · Bẹt ($180^\\circ$)'},
                          {'name': 'Chu vi hình thoi', 'formula': '$P = a \\times 4$'}]}],
  'example': 'Một mảnh bìa hình vuông có chu vi bằng chu vi của hình chữ nhật có chiều dài $12\\text{ cm}$, '
             'chiều rộng $6\\text{ cm}$. Tính diện tích mảnh bìa hình vuông đó.',
  'example_answer': 'Chu vi hình chữ nhật (cũng là chu vi hình vuông) là: $(12 + 6) \\times 2 = 36\\text{ '
                    '(cm)}$.\n'
                    'Cạnh hình vuông là: $36 : 4 = 9\\text{ (cm)}$.\n'
                    'Diện tích mảnh bìa hình vuông là: $9 \\times 9 = 81\\text{ (cm}^2\\text{)}$.',
  'real_life': '- Đo đạc và thiết kế bồn hoa, sân chơi trong khuôn viên trường học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc có số đo bằng $90^\\circ$ là:',
            'options': ['Góc nhọn', 'Góc tù', 'Góc bẹt', 'Góc vuông'],
            'answer': 3,
            'solution': 'Góc có số đo $90^\\circ$ là **góc vuông**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đặc điểm đúng của hình thoi là:',
            'options': ['Có $4$ cạnh bằng nhau',
                        'Có $4$ góc vuông',
                        'Chỉ có $1$ cặp cạnh song song',
                        'Có $3$ cạnh bằng nhau'],
            'answer': 0,
            'solution': 'Hình thoi có **$4$ cạnh bằng nhau** và hai cặp cạnh đối diện song song.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 35: Ôn tập hình học**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Phân loại góc**?',
            'options': ['$P = a \\times 4$',
                        'Nhọn ($< 90^\\circ$) · Vuông ($90^\\circ$) · Tù ($90^\\circ < \\alpha < '
                        '180^\\circ$) · Bẹt ($180^\\circ$)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 35: Ôn tập hình học, **Phân loại góc** được '
                        'xác định bởi: Nhọn ($< 90^\\circ$) · Vuông ($90^\\circ$) · Tù ($90^\\circ < \\alpha '
                        '< 180^\\circ$) · Bẹt ($180^\\circ$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Ôn tập hình học**, nội dung/biểu thức $P = a \\times 4$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Phân loại góc', 'Phân tích số', 'Chu vi hình thoi', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 35: Ôn tập hình học, biểu thức/quy tắc $P = a \\times 4$ chính là nội '
                        'dung của **Chu vi hình thoi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình vuông có diện tích bằng $64\\text{ cm}^2$. Chu vi của hình vuông đó là:',
            'options': ['$16\\text{ cm}$', '$24\\text{ cm}$', '$64\\text{ cm}$', '$32\\text{ cm}$'],
            'answer': 3,
            'solution': 'Vì $8 \\times 8 = 64$ nên cạnh hình vuông là $8\\text{ cm}$. Chu vi là: $8 \\times '
                        '4 = 32\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Ôn tập hình học** (Chủ đề 7: Ôn tập học kì 1), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Phân biệt chính xác góc nhọn, góc vuông, góc tù, góc bẹt qua hình vẽ và số đo góc.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 35: Ôn tập hình học: Phân biệt chính xác góc nhọn, góc '
                        'vuông, góc tù, góc bẹt qua hình vẽ và số đo góc.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trong một hình bình hành, hai cạnh đối diện luôn song song và có độ dài bằng '
                 'nhau."',
            'answer': True,
            'solution': 'Đó là tính chất cơ bản của hình bình hành $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 35: Ôn tập hình học**, quy tắc **Phân loại góc** được xác định bởi Nhọn ($< '
                 '90^\\circ$) · Vuông ($90^\\circ$) · Tù ($90^\\circ < \\alpha < 180^\\circ$) · Bẹt '
                 '($180^\\circ$) và áp dụng trực tiếp vào bài toán: “Một mảnh bìa hình vuông có chu vi bằng '
                 'chu vi của hình chữ nhật có chiều dài $12\\text{ cm}$, chiều rộng $6\\text{ cm}$. Tính '
                 'diện tích mảnh b...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Phân loại góc** (Nhọn ($< 90^\\circ$) · Vuông '
                        '($90^\\circ$) · Tù ($90^\\circ < \\alpha < 180^\\circ$) · Bẹt ($180^\\circ$)) là '
                        'kiến thức cốt lõi của Bài 35: Ôn tập hình học. Chu vi hình chữ nhật (cũng là chu vi '
                        'hình vuông) là: $(12 + 6) \\times 2 = 36\\text{ (cm)}$. Cạnh hình vuông là: $36 : 4 '
                        '= 9\\text{ (cm)}$. Diệ...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 35: Ôn tập hình học** để giải quyết tình huống sau: Một mảnh bìa '
                 'hình vuông có chu vi bằng chu vi của hình chữ nhật có chiều dài $12\\text{ cm}$, chiều '
                 'rộng $6\\text{ cm}$. Tính diện tích mảnh bìa hình vuông đó. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Chu vi hình chữ nhật (cũng là chu vi hình vuông) là: $(12 + 6) \\times 2 = '
                        '36\\text{ (cm)}$. Cạnh hình vuông là: $36 : 4 = 9\\text{ (cm)}$. Diện tích mảnh '
                        'bìa...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 35: Ôn tập hình học: Chu vi hình chữ nhật (cũng là chu '
                        'vi hình vuông) là: $(12 + 6) \\times 2 = 36\\text{ (cm)}$.\n'
                        'Cạnh hình vuông là: $36 : 4 = 9\\text{ (cm)}$.\n'
                        'Diện tích mảnh bìa hình vuông là: $9 \\times 9 = 81\\text{ (cm}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khung tranh hình chữ nhật có chiều dài $45\\text{ cm}$, chiều rộng $25\\text{ cm}$. '
                 'Hỏi chu vi của khung tranh đó bằng bao nhiêu đề-xi-mét?',
            'answer': ['14'],
            'unit': 'dm',
            'solution': 'Chu vi khung tranh là: $(45 + 25) \\times 2 = 140\\text{ (cm)} = 14\\text{ (dm)}$.\n'
                        'Đáp số: **$14\\text{ dm}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 4 · Chủ đề 7: Ôn tập tổng hợp kiến thức học kì 1.',
  'title': 'Bài 36, 37: Ôn tập đo lường và ôn tập chung',
  'icon': '⚖️',
  'description': 'Hệ thống hóa các đơn vị đo khối lượng (yến, tạ, tấn), diện tích (dm², m², mm²), thời gian '
                 '(giây, thế kỉ) và giải toán tổng hợp.',
  'requirements': ['Đổi thành thạo các đơn vị đo khối lượng, diện tích, thời gian đã học trong học kì 1.',
                   'So sánh và thực hiện bốn phép tính với các số đo đại lượng.',
                   'Giải được bài toán thực tế tổng hợp có đến ba bước tính.'],
  'definition': '- **Khối lượng**: $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1\\,000\\text{ kg}$.\n'
                '- **Diện tích**: $1\\text{ m}^2 = 100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$; $1\\text{ '
                'cm}^2 = 100\\text{ mm}^2$.\n'
                '- **Thời gian**: $1\\text{ thế kỉ} = 100\\text{ năm}$; $1\\text{ phút} = 60\\text{ giây}$.',
  'theory': '### 1. Ôn tập đổi đơn vị kép\n'
            '- Ví dụ: $4\\text{ tạ } 5\\text{ kg} = 405\\text{ kg}$; $3\\text{ m}^2\\text{ } 25\\text{ dm}^2 '
            '= 325\\text{ dm}^2$; $2\\text{ phút } 30\\text{ giây} = 150\\text{ giây}$.\n'
            '### 2. Bài toán thu hoạch trên diện tích ruộng\n'
            '- Tính diện tích thửa ruộng $\\rightarrow$ tìm xem diện tích đó gấp bao nhiêu lần diện tích mẫu '
            '$\\rightarrow$ nhân với sản lượng mẫu.',
  'formulas': [{'category': 'I. Quy đổi trọng tâm',
                'items': [{'name': 'Khối lượng & Diện tích',
                           'formula': '$1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ m}^2 = 100\\text{ '
                                      'dm}^2$'},
                          {'name': 'Thời gian',
                           'formula': '$1\\text{ thế kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ '
                                      'giây}$'}]}],
  'example': 'Một thửa ruộng hình chữ nhật dài $50\\text{ m}$, rộng $20\\text{ m}$. Trung bình cứ '
             '$100\\text{ m}^2$ thu hoạch được $60\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch được bao '
             'nhiêu tạ thóc?',
  'example_answer': 'Diện tích thửa ruộng là: $50 \\times 20 = 1\\,000\\text{ (m}^2\\text{)}$.\n'
                    '$1\\,000\\text{ m}^2$ gấp $100\\text{ m}^2$ số lần là: $1\\,000 : 100 = 10\\text{ '
                    '(lần)}$.\n'
                    'Số thóc thu hoạch được là: $60 \\times 10 = 600\\text{ (kg)} = 6\\text{ (tạ)}$.',
  'real_life': '- Tính sản lượng lúa thu hoạch của gia đình theo tạ, tấn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $6\\text{ yến } 8\\text{ kg} = \\dots\\text{ kg}$?',
            'options': ['$68\\text{ kg}$', '$608\\text{ kg}$', '$680\\text{ kg}$', '$14\\text{ kg}$'],
            'answer': 0,
            'solution': 'Vì $6\\text{ yến} = 60\\text{ kg}$ nên $60 + 8 = 68\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $7\\text{ m}^2\\text{ } 5\\text{ dm}^2 = \\dots\\text{ dm}^2$?',
            'options': ['$75\\text{ dm}^2$',
                        '$705\\text{ dm}^2$',
                        '$750\\text{ dm}^2$',
                        '$7\\,005\\text{ dm}^2$'],
            'answer': 1,
            'solution': 'Vì $7\\text{ m}^2 = 700\\text{ dm}^2$ nên $700 + 5 = 705\\text{ (dm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 36, 37: Ôn tập đo lường và ôn tập chung**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Khối lượng & Diện tích**?',
            'options': ['$1\\text{ thế kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ giây}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ m}^2 = 100\\text{ dm}^2$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 36, 37: Ôn tập đo lường và ôn tập chung, '
                        '**Khối lượng & Diện tích** được xác định bởi: $1\\text{ tấn} = 1\\,000\\text{ kg}$ '
                        '· $1\\text{ m}^2 = 100\\text{ dm}^2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36, 37: Ôn tập đo lường và ôn tập chung**, nội dung/biểu thức $1\\text{ thế '
                 'kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ giây}$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Khối lượng & Diện tích', 'Phân tích số', 'Quy tắc 5', 'Thời gian'],
            'answer': 3,
            'solution': 'Trong Bài 36, 37: Ôn tập đo lường và ôn tập chung, biểu thức/quy tắc $1\\text{ thế '
                        'kỉ} = 100\\text{ năm}$ · $1\\text{ phút} = 60\\text{ giây}$ chính là nội dung của '
                        '**Thời gian**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Chiến thắng Điện Biên Phủ diễn ra vào năm $1954$. Tính đến năm $2024$ là kỷ niệm bao nhiêu '
                 'năm và năm $1954$ thuộc thế kỉ nào?',
            'options': ['$70$ năm; thế kỉ $\\text{XX}$',
                        '$70$ năm; thế kỉ $\\text{XIX}$',
                        '$60$ năm; thế kỉ $\\text{XX}$',
                        '$70$ năm; thế kỉ $\\text{XXI}$'],
            'answer': 0,
            'solution': 'Ta có $2024 - 1954 = 70$ năm, và năm $1954$ thuộc **thế kỉ $\\text{XX}$**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 36, 37: Ôn tập đo lường và ôn tập chung** (Chủ đề 7: Ôn tập học kì 1), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Đổi thành thạo các đơn vị đo khối lượng, diện tích, thời gian đã học trong học kì '
                        '1.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 36, 37: Ôn tập đo lường và ôn tập chung: Đổi thành '
                        'thạo các đơn vị đo khối lượng, diện tích, thời gian đã học trong học kì 1.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{1}{2}\\text{ tấn} = 500\\text{ kg}$."',
            'answer': True,
            'solution': 'Vì $1\\text{ tấn} = 1\\,000\\text{ kg}$ nên nửa tấn là $1\\,000 : 2 = 500\\text{ '
                        'kg}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 36, 37: Ôn tập đo lường và ôn tập chung**, quy tắc **Khối lượng & Diện tích** '
                 'được xác định bởi $1\\text{ tấn} = 1\\,000\\text{ kg}$ · $1\\text{ m}^2 = 100\\text{ '
                 'dm}^2$ và áp dụng trực tiếp vào bài toán: “Một thửa ruộng hình chữ nhật dài $50\\text{ '
                 'm}$, rộng $20\\text{ m}$. Trung bình cứ $100\\text{ m}^2$ thu hoạch được $60\\text{ kg}$ '
                 'thóc. Hỏi c...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khối lượng & Diện tích** ($1\\text{ tấn} = '
                        '1\\,000\\text{ kg}$ · $1\\text{ m}^2 = 100\\text{ dm}^2$) là kiến thức cốt lõi của '
                        'Bài 36, 37: Ôn tập đo lường và ôn tập chung. Diện tích thửa ruộng là: $50 \\times '
                        '20 = 1\\,000\\text{ (m}^2\\text{)}$. $1\\,000\\text{ m}^2$ gấp $100\\text{ m}^2$ số '
                        'lần là: $1\\,000 : 100 = 10\\text{ (lần)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 36, 37: Ôn tập đo lường và ôn tập chung** để giải quyết tình '
                 'huống sau: Một thửa ruộng hình chữ nhật dài $50\\text{ m}$, rộng $20\\text{ m}$. Trung '
                 'bình cứ $100\\text{ m}^2$ thu hoạch được $60\\text{ kg}$ thóc. Hỏi cả thửa ruộng thu hoạch '
                 'được bao nhiêu tạ thóc? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Diện tích thửa ruộng là: $50 \\times 20 = 1\\,000\\text{ (m}^2\\text{)}$. '
                        '$1\\,000\\text{ m}^2$ gấp $100\\text{ m}^2$ số lần là: $1\\,000 : 100 = 10\\text{ '
                        '(lần)}$....',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 36, 37: Ôn tập đo lường và ôn tập chung: Diện tích thửa '
                        'ruộng là: $50 \\times 20 = 1\\,000\\text{ (m}^2\\text{)}$.\n'
                        '$1\\,000\\text{ m}^2$ gấp $100\\text{ m}^2$ số lần là: $1\\,000 : 100 = 10\\text{ '
                        '(lần)}$.\n'
                        'Số thóc thu hoạch được là: $60 \\times 10 = 600\\text{ (kg)} = 6\\text{ (tạ)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai xe tải chở tất cả $8$ tấn gạo. Xe thứ nhất chở nhiều hơn xe thứ hai $6$ tạ gạo. Hỏi xe '
                 'thứ nhất chở bao nhiêu ki-lô-gam gạo (viết số liền)?',
            'answer': ['4300'],
            'unit': 'kg',
            'solution': 'Đổi $8\\text{ tấn} = 8\\,000\\text{ kg}$; $6\\text{ tạ} = 600\\text{ kg}$. Xe thứ '
                        'nhất chở: $(8\\,000 + 600) : 2 = 4\\,300\\text{ (kg)}$.\n'
                        'Đáp số: **$4300$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd08-phep-nhan-va-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân và phép chia',
  'context': 'SGK Toán 4 · Chủ đề 8: Phép nhân, phép chia với số có một, hai chữ số; tính chất phép nhân; '
             'trung bình cộng; rút về đơn vị.',
  'title': 'Bài 38, 39: Nhân và chia với số có một chữ số',
  'icon': '✖️',
  'description': 'Thực hiện phép nhân và phép chia số có nhiều chữ số với (cho) số có một chữ số.',
  'requirements': ['Đặt tính và tính đúng phép nhân số có nhiều chữ số với số có một chữ số.',
                   'Đặt tính dọc và chia đúng số có nhiều chữ số cho số có một chữ số (chia hết và chia có '
                   'dư).',
                   'Giải được bài toán thực tế liên quan đến nhân, chia với số có một chữ số.'],
  'definition': '- **Nhân với số có một chữ số**: đặt tính thẳng cột, nhân lần lượt từ phải sang trái (từ '
                'hàng đơn vị đến hàng cao nhất), nhớ sang hàng kế tiếp.\n'
                '- **Chia cho số có một chữ số**: chia lần lượt từ trái sang phải (từ hàng cao nhất xuống '
                'hàng đơn vị); ở mỗi lượt chia thực hiện: chia $\\rightarrow$ nhân $\\rightarrow$ trừ '
                '$\\rightarrow$ hạ.',
  'theory': '### 1. Phép nhân số có nhiều chữ số\n'
            '- Ví dụ: $24\\,135 \\times 4 = 96\\,540$.\n'
            '### 2. Phép chia cho số có một chữ số\n'
            '- Ví dụ: $128\\,472 : 6 = 21\\,412$.\n'
            '- Chú ý: Từ lượt chia thứ hai trở đi, nếu hạ chữ số xuống mà số tạo thành bé hơn số chia thì '
            'phải **viết $0$ vào thương**.',
  'formulas': [{'category': 'I. Quy tắc nhân – chia',
                'items': [{'name': 'Nhân',
                           'formula': 'Tính từ phải sang trái · Cộng phần nhớ vào hàng liền trước'},
                          {'name': 'Chia',
                           'formula': 'Tính từ trái sang phải · Số dư luôn bé hơn số chia ($r < b$)'}]}],
  'example': 'Đặt tính rồi tính: a) $24\\,135 \\times 4$; b) $128\\,472 : 6$.',
  'example_answer': 'a) $24\\,135 \\times 4 = 96\\,540$.\nb) $128\\,472 : 6 = 21\\,412$.',
  'real_life': '- Tính tổng tiền lương hoặc chia đều kinh phí hỗ trợ cho các hộ gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $24\\,135 \\times 4$ là:',
            'options': ['$96\\,440$', '$96\\,540$', '$86\\,540$', '$96\\,520$'],
            'answer': 1,
            'solution': 'Nhân từ phải sang trái ta được **$96\\,540$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $128\\,472 : 6$ là:',
            'options': ['$21\\,402$', '$20\\,412$', '$21\\,412$', '$21\\,312$'],
            'answer': 2,
            'solution': 'Chia lần lượt từ trái sang phải ta được **$21\\,412$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 38, 39: Nhân và chia với số có một chữ số**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Nhân**?',
            'options': ['Tính từ trái sang phải · Số dư luôn bé hơn số chia ($r < b$)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        'Tính từ phải sang trái · Cộng phần nhớ vào hàng liền trước'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 38, 39: Nhân và chia với số có một chữ số, '
                        '**Nhân** được xác định bởi: Tính từ phải sang trái · Cộng phần nhớ vào hàng liền '
                        'trước.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38, 39: Nhân và chia với số có một chữ số**, nội dung/biểu thức Tính từ trái '
                 'sang phải · Số dư luôn bé hơn số chia ($r < b$) là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Chia', 'Nhân', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 38, 39: Nhân và chia với số có một chữ số, biểu thức/quy tắc Tính từ trái '
                        'sang phải · Số dư luôn bé hơn số chia ($r < b$) chính là nội dung của **Chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x \\times 5 = 135\\,250$:',
            'options': ['$27\\,500$', '$27\\,050$', '$27\\,005$', '$25\\,050$'],
            'answer': 1,
            'solution': 'Thừa số $x = 135\\,250 : 5 = 27\\,050$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 38, 39: Nhân và chia với số có một chữ số** (Chủ đề 8: Phép nhân và phép '
                 'chia), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Đặt tính và tính đúng phép nhân số có nhiều chữ số với số có một chữ số.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 38, 39: Nhân và chia với số có một chữ số: Đặt tính và '
                        'tính đúng phép nhân số có nhiều chữ số với số có một chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $180\\,036 : 9$ có thương bằng $20\\,004$."',
            'answer': True,
            'solution': 'Vì $20\\,004 \\times 9 = 180\\,036$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 38, 39: Nhân và chia với số có một chữ số**, quy tắc **Nhân** được xác định '
                 'bởi Tính từ phải sang trái · Cộng phần nhớ vào hàng liền trước và áp dụng trực tiếp vào '
                 'bài toán: “Đặt tính rồi tính: a) $24\\,135 \\times 4$; b) $128\\,472 : 6$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhân** (Tính từ phải sang trái · Cộng phần nhớ vào '
                        'hàng liền trước) là kiến thức cốt lõi của Bài 38, 39: Nhân và chia với số có một '
                        'chữ số. a) $24\\,135 \\times 4 = 96\\,540$. b) $128\\,472 : 6 = 21\\,412$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 38, 39: Nhân và chia với số có một chữ số** để giải quyết tình '
                 'huống sau: Đặt tính rồi tính: a) $24\\,135 \\times 4$; b) $128\\,472 : 6$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'a) $24\\,135 \\times 4 = 96\\,540$. b) $128\\,472 : 6 = 21\\,412$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 38, 39: Nhân và chia với số có một chữ số: a) $24\\,135 '
                        '\\times 4 = 96\\,540$.\n'
                        'b) $128\\,472 : 6 = 21\\,412$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một nhà máy trong $6$ ngày sản xuất được $150\\,600$ chiếc khẩu trang. Biết số khẩu trang '
                 'sản xuất mỗi ngày là như nhau, hỏi trong $1$ ngày nhà máy sản xuất được bao nhiêu chiếc '
                 'khẩu trang (viết số liền)?',
            'answer': ['25100'],
            'unit': 'chiếc',
            'solution': 'Số khẩu trang sản xuất trong $1$ ngày là: $150\\,600 : 6 = 25\\,100\\text{ '
                        '(chiếc)}$.\n'
                        'Đáp số: **$25100$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd08-phep-nhan-va-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân và phép chia',
  'context': 'SGK Toán 4 · Chủ đề 8: Phép nhân, phép chia với số có một, hai chữ số; tính chất phép nhân; '
             'trung bình cộng; rút về đơn vị.',
  'title': 'Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000',
  'icon': '⚡',
  'description': 'Tính chất giao hoán, kết hợp, phân phối của phép nhân và quy tắc nhân, chia nhẩm với 10, '
                 '100, 1 000.',
  'requirements': ['Nắm vững tính chất giao hoán ($a \\times b = b \\times a$), kết hợp ($(a \\times b) '
                   '\\times c = a \\times (b \\times c)$) và tính chất phân phối của phép nhân đối với phép '
                   'cộng ($a \\times (b + c) = a \\times b + a \\times c$).',
                   'Nhân, chia nhẩm nhanh một số tự nhiên với (cho) $10, 100, 1\\,000, \\dots$',
                   'Vận dụng các tính chất để tính bằng cách thuận tiện nhất.'],
  'definition': '- **Giao hoán**: $a \\times b = b \\times a$. **Kết hợp**: $(a \\times b) \\times c = a '
                '\\times (b \\times c)$.\n'
                '- **Phân phối của phép nhân đối với phép cộng (trừ)**: $a \\times (b + c) = a \\times b + a '
                '\\times c$ và $a \\times (b - c) = a \\times b - a \\times c$.\n'
                '- **Nhân với $10, 100, 1\\,000$**: viết thêm $1, 2, 3$ chữ số $0$ vào bên phải số đó. '
                '**Chia số tròn chục, trăm, nghìn cho $10, 100, 1\\,000$**: bỏ bớt $1, 2, 3$ chữ số $0$ ở '
                'tận cùng bên phải.',
  'theory': '### 1. Các cặp nhân tạo số tròn chục, trăm, nghìn cần nhớ\n'
            '- $2 \\times 5 = 10$; $4 \\times 25 = 100$; $8 \\times 125 = 1\\,000$.\n'
            '- Ví dụ: $125 \\times 8 \\times 7 = (125 \\times 8) \\times 7 = 1\\,000 \\times 7 = 7\\,000$.\n'
            '### 2. Đặt thừa số chung nhờ tính chất phân phối\n'
            '- Ví dụ: $36 \\times 7 + 36 \\times 3 = 36 \\times (7 + 3) = 36 \\times 10 = 360$.\n'
            '- Ví dụ: $23 \\times 99 + 23 = 23 \\times 99 + 23 \\times 1 = 23 \\times (99 + 1) = 23 \\times '
            '100 = 2\\,300$.',
  'formulas': [{'category': 'I. Tính chất phép nhân',
                'items': [{'name': 'Giao hoán & Kết hợp',
                           'formula': '$a \\times b = b \\times a$ · $(a \\times b) \\times c = a \\times (b '
                                      '\\times c)$'},
                          {'name': 'Phân phối',
                           'formula': '$a \\times (b + c) = a \\times b + a \\times c$ · $a \\times (b - c) '
                                      '= a \\times b - a \\times c$'}]},
               {'category': 'II. Nhân, chia nhẩm 10, 100, 1 000',
                'items': [{'name': 'Nhân / Chia',
                           'formula': 'Nhân: thêm $1, 2, 3$ chữ số $0$ · Chia: bớt $1, 2, 3$ chữ số $0$'}]}],
  'example': 'Tính bằng cách thuận tiện nhất: a) $25 \\times 19 \\times 4$; b) $48 \\times 63 + 48 \\times '
             '37$.',
  'example_answer': 'a) $25 \\times 19 \\times 4 = (25 \\times 4) \\times 19 = 100 \\times 19 = 1\\,900$.\n'
                    'b) $48 \\times 63 + 48 \\times 37 = 48 \\times (63 + 37) = 48 \\times 100 = 4\\,800$.',
  'real_life': '- Tính nhẩm nhanh tổng tiền khi mua $10, 100$ sản phẩm cùng giá hoặc mua hai loại hàng có '
               'cùng số lượng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $456 \\times 100$ là:',
            'options': ['$4\\,560$', '$456\\,000$', '$45\\,600$', '$4\\,560\\,000$'],
            'answer': 2,
            'solution': 'Nhân với $100$ ta viết thêm $2$ chữ số $0$ vào bên phải $\\rightarrow$ '
                        '**$45\\,600$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức $a \\times (b + c) = a \\times b + a \\times c$ biểu thị tính chất nào?',
            'options': ['Tính chất giao hoán',
                        'Tính chất kết hợp',
                        'Nhân với số $1$',
                        'Tính chất phân phối của phép nhân đối với phép cộng'],
            'answer': 3,
            'solution': 'Đó là **tính chất phân phối của phép nhân đối với phép cộng**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia '
                 'với 10, 100, 1 000**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Giao hoán & Kết '
                 'hợp**?',
            'options': ['$a \\times b = b \\times a$ · $(a \\times b) \\times c = a \\times (b \\times c)$',
                        '$a \\times (b + c) = a \\times b + a \\times c$ · $a \\times (b - c) = a \\times b '
                        '- a \\times c$',
                        'Nhân: thêm $1, 2, 3$ chữ số $0$ · Chia: bớt $1, 2, 3$ chữ số $0$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 40, 41, 42: Các tính chất của phép nhân và '
                        'nhân, chia với 10, 100, 1 000, **Giao hoán & Kết hợp** được xác định bởi: $a '
                        '\\times b = b \\times a$ · $(a \\times b) \\times c = a \\times (b \\times c)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000**, '
                 'nội dung/biểu thức $a \\times (b + c) = a \\times b + a \\times c$ · $a \\times (b - c) = '
                 'a \\times b - a \\times c$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Giao hoán & Kết hợp', 'Phân phối', 'Nhân / Chia', 'Phân tích số'],
            'answer': 1,
            'solution': 'Trong Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000, '
                        'biểu thức/quy tắc $a \\times (b + c) = a \\times b + a \\times c$ · $a \\times (b - '
                        'c) = a \\times b - a \\times c$ chính là nội dung của **Phân phối**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tính nhanh biểu thức $125 \\times 8 \\times 7$ ta được kết quả là:',
            'options': ['$1\\,000$', '$8\\,750$', '$7\\,000$', '$875$'],
            'answer': 2,
            'solution': 'Ta có $(125 \\times 8) \\times 7 = 1\\,000 \\times 7 = 7\\,000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000** '
                 '(Chủ đề 8: Phép nhân và phép chia), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Nắm vững tính chất giao hoán ($a \\times b = b \\times a$), kết hợp ($(a \\times b) '
                        '\\times c = a \\times (b \\times c)$) và tính chất phân phối của phép nhân đối với '
                        'phép cộng ($a \\times (b + c) = a \\times b + a \\times c$).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia '
                        'với 10, 100, 1 000: Nắm vững tính chất giao hoán ($a \\times b = b \\times a$), kết '
                        'hợp ($(a \\times b) \\times c = a \\times (b \\times c)$) và tính chất phân phối '
                        'của phép nhân đối với phép cộng ($a \\times (b + c) = a \\times b + a \\times c$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $23 \\times 99 + 23$ bằng $2\\,300$."',
            'answer': True,
            'solution': 'Ta có $23 \\times 99 + 23 \\times 1 = 23 \\times (99 + 1) = 23 \\times 100 = '
                        '2\\,300$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000**, '
                 'quy tắc **Giao hoán & Kết hợp** được xác định bởi $a \\times b = b \\times a$ · $(a '
                 '\\times b) \\times c = a \\times (b \\times c)$ và áp dụng trực tiếp vào bài toán: “Tính '
                 'bằng cách thuận tiện nhất: a) $25 \\times 19 \\times 4$; b) $48 \\times 63 + 48 \\times '
                 '37$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Giao hoán & Kết hợp** ($a \\times b = b \\times a$ · '
                        '$(a \\times b) \\times c = a \\times (b \\times c)$) là kiến thức cốt lõi của Bài '
                        '40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, 100, 1 000. a) $25 '
                        '\\times 19 \\times 4 = (25 \\times 4) \\times 19 = 100 \\times 19 = 1\\,900$. b) '
                        '$48 \\times 63 + 48 \\times 37 = 48 \\times (63 + 37) = 48 \\times 100 = '
                        '4\\,800$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia với 10, '
                 '100, 1 000** để giải quyết tình huống sau: Tính bằng cách thuận tiện nhất: a) $25 \\times '
                 '19 \\times 4$; b) $48 \\times 63 + 48 \\times 37$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['a) $25 \\times 19 \\times 4 = (25 \\times 4) \\times 19 = 100 \\times 19 = '
                        '1\\,900$. b) $48 \\times 63 + 48 \\times 37 = 48 \\times (63 + 37) = 48 \\times 100 '
                        '= 4\\,800$...',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 40, 41, 42: Các tính chất của phép nhân và nhân, chia '
                        'với 10, 100, 1 000: a) $25 \\times 19 \\times 4 = (25 \\times 4) \\times 19 = 100 '
                        '\\times 19 = 1\\,900$.\n'
                        'b) $48 \\times 63 + 48 \\times 37 = 48 \\times (63 + 37) = 48 \\times 100 = '
                        '4\\,800$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức: $36 \\times 75 + 36 \\times 25$.',
            'answer': ['3600'],
            'unit': None,
            'solution': 'Áp dụng tính chất phân phối: $36 \\times (75 + 25) = 36 \\times 100 = 3\\,600$.\n'
                        'Đáp số: **$3600$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd08-phep-nhan-va-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân và phép chia',
  'context': 'SGK Toán 4 · Chủ đề 8: Phép nhân, phép chia với số có một, hai chữ số; tính chất phép nhân; '
             'trung bình cộng; rút về đơn vị.',
  'title': 'Bài 43: Nhân với số có hai chữ số',
  'icon': '📝',
  'description': 'Quy tắc đặt tính và tính tích riêng thứ nhất, tích riêng thứ hai khi nhân với số có hai '
                 'chữ số.',
  'requirements': ['Đặt tính và tính đúng phép nhân với số có hai chữ số.',
                   'Hiểu và nhớ quy tắc: **tích riêng thứ hai phải viết lùi sang bên trái một cột** (vì đó '
                   'là tích với chữ số hàng chục).',
                   'Vận dụng tính diện tích hình chữ nhật có số đo hai chữ số và giải toán thực tế.'],
  'definition': '- Khi đặt tính nhân một số với số có hai chữ số $\\overline{bc}$:\n'
                '  1. Tìm **tích riêng thứ nhất** (nhân với chữ số hàng đơn vị $c$).\n'
                '  2. Tìm **tích riêng thứ hai** (nhân với chữ số hàng chục $b$), viết **lùi sang bên trái '
                'một cột** so với tích riêng thứ nhất.\n'
                '  3. Cộng hai tích riêng lại để được tích chung.',
  'theory': '### 1. Ví dụ minh họa\n'
            '- Tính $36 \\times 23$:\n'
            '  - Tích riêng thứ nhất: $36 \\times 3 = 108$.\n'
            '  - Tích riêng thứ hai: $36 \\times 2 = 72$ (thực chất là $72$ chục $= 720$, nên viết chữ số '
            '$2$ thẳng dưới chữ số $0$ của $108$).\n'
            '  - Cộng lại: $108 + 720 = 828$.\n'
            '### 2. Lỗi thường gặp cần tránh\n'
            '- Quên viết lùi tích riêng thứ hai sang trái $1$ cột sẽ dẫn đến kết quả sai ($108 + 72 = 180$ '
            'là sai!).',
  'formulas': [{'category': 'I. Nhân với số có hai chữ số',
                'items': [{'name': 'Bản chất',
                           'formula': '$A \\times \\overline{bc} = A \\times c + A \\times b0$'},
                          {'name': 'Quy tắc viết',
                           'formula': 'Tích riêng thứ hai viết lùi sang trái $1$ cột (dưới hàng chục)'}]}],
  'example': 'Đặt tính rồi tính: $47 \\times 25$.',
  'example_answer': '- Tích riêng thứ nhất: $47 \\times 5 = 235$.\n'
                    '- Tích riêng thứ hai: $47 \\times 2 = 94$ (viết lùi $1$ cột thành $940$).\n'
                    '- Cộng hai tích riêng: $235 + 940 = 1\\,175$.',
  'real_life': '- Tính tổng số ghế trong rạp chiếu phim có $24$ hàng, mỗi hàng $35$ ghế.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đặt tính nhân với số có hai chữ số, tích riêng thứ hai phải được viết như thế nào so '
                 'với tích riêng thứ nhất?',
            'options': ['Thẳng cột hàng đơn vị',
                        'Lùi sang bên phải một cột',
                        'Lùi sang bên trái hai cột',
                        'Lùi sang bên trái một cột'],
            'answer': 3,
            'solution': 'Tích riêng thứ hai là số chục nên phải viết **lùi sang bên trái một cột**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $36 \\times 23$ là:',
            'options': ['$828$', '$180$', '$728$', '$818$'],
            'answer': 0,
            'solution': 'Ta có $36 \\times 3 = 108$ và $36 \\times 20 = 720 \\Rightarrow 108 + 720 = 828$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 43: Nhân với số có hai chữ số**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Bản chất**?',
            'options': ['Tích riêng thứ hai viết lùi sang trái $1$ cột (dưới hàng chục)',
                        '$A \\times \\overline{bc} = A \\times c + A \\times b0$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 43: Nhân với số có hai chữ số, **Bản chất** '
                        'được xác định bởi: $A \\times \\overline{bc} = A \\times c + A \\times b0$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 43: Nhân với số có hai chữ số**, nội dung/biểu thức Tích riêng thứ hai viết '
                 'lùi sang trái $1$ cột (dưới hàng chục) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Bản chất', 'Phân tích số', 'Quy tắc viết', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 43: Nhân với số có hai chữ số, biểu thức/quy tắc Tích riêng thứ hai viết '
                        'lùi sang trái $1$ cột (dưới hàng chục) chính là nội dung của **Quy tắc viết**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $47 \\times 25$ là:',
            'options': ['$1\\,075$', '$329$', '$1\\,185$', '$1\\,175$'],
            'answer': 3,
            'solution': 'Ta có $47 \\times 5 = 235$; $47 \\times 20 = 940 \\Rightarrow 235 + 940 = 1\\,175$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 43: Nhân với số có hai chữ số** (Chủ đề 8: Phép nhân và phép chia), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đặt tính và tính đúng phép nhân với số có hai chữ số.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 43: Nhân với số có hai chữ số: Đặt tính và tính đúng '
                        'phép nhân với số có hai chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khi đặt tính $124 \\times 15$, nếu một bạn quên viết lùi tích riêng thứ hai mà '
                 'viết thẳng cột như cộng thì kết quả sai thu được là $744$."',
            'answer': True,
            'solution': 'Tích riêng thứ nhất là $620$, tích riêng thứ hai là $124$; viết thẳng cột cộng lại '
                        'ra $620 + 124 = 744$ (trong khi đáp án đúng là $1\\,860$) $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 43: Nhân với số có hai chữ số**, quy tắc **Bản chất** được xác định bởi $A '
                 '\\times \\overline{bc} = A \\times c + A \\times b0$ và áp dụng trực tiếp vào bài toán: '
                 '“Đặt tính rồi tính: $47 \\times 25$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Bản chất** ($A \\times \\overline{bc} = A \\times c '
                        '+ A \\times b0$) là kiến thức cốt lõi của Bài 43: Nhân với số có hai chữ số. - Tích '
                        'riêng thứ nhất: $47 \\times 5 = 235$. - Tích riêng thứ hai: $47 \\times 2 = 94$ '
                        '(viết lùi $1$ cột thành $940$). - Cộng hai tích riêng...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 43: Nhân với số có hai chữ số** để giải quyết tình huống sau: Đặt '
                 'tính rồi tính: $47 \\times 25$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        '- Tích riêng thứ nhất: $47 \\times 5 = 235$. - Tích riêng thứ hai: $47 \\times 2 = '
                        '94$ (viết lùi $1$ cột thành $940$). - Cộng hai tích riêng: $235 + 940 = 1\\,175$...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 43: Nhân với số có hai chữ số: - Tích riêng thứ nhất: '
                        '$47 \\times 5 = 235$.\n'
                        '- Tích riêng thứ hai: $47 \\times 2 = 94$ (viết lùi $1$ cột thành $940$).\n'
                        '- Cộng hai tích riêng: $235 + 940 = 1\\,175$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hội trường có $25$ dãy ghế, mỗi dãy ghế có $32$ chỗ ngồi. Hỏi hội trường đó có tất cả '
                 'bao nhiêu chỗ ngồi?',
            'answer': ['800'],
            'unit': 'chỗ ngồi',
            'solution': 'Tổng số chỗ ngồi là: $32 \\times 25 = 800\\text{ (chỗ ngồi)}$.\n'
                        'Đáp số: **$800\\text{ chỗ ngồi}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd08-phep-nhan-va-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân và phép chia',
  'context': 'SGK Toán 4 · Chủ đề 8: Phép nhân, phép chia với số có một, hai chữ số; tính chất phép nhân; '
             'trung bình cộng; rút về đơn vị.',
  'title': 'Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương',
  'icon': '➗',
  'description': 'Kỹ thuật ước lượng thương (làm tròn đến hàng chục) và thực hiện phép chia cho số có hai '
                 'chữ số.',
  'requirements': ['Biết làm tròn số bị chia và số chia đến hàng chục để ước lượng thương trong mỗi lượt '
                   'chia.',
                   'Đặt tính dọc và thực hiện đúng phép chia cho số có hai chữ số (chia hết và chia có dư).',
                   'Biết điều chỉnh giảm thương xuống $1$ đơn vị khi tích ước lượng lớn hơn số bị chia.'],
  'definition': '- Khi chia cho số có $2$ chữ số ($\\overline{ab}$), ở mỗi lượt chia ta lấy $2$ chữ số (hoặc '
                '$3$ chữ số) từ trái sang phải để chia.\n'
                '- **Mẹo ước lượng thương**: làm tròn số chia đến hàng chục để nhẩm thương nhanh, đảm bảo số '
                'dư $r < \\overline{ab}$.',
  'theory': '### 1. Thực hành chia và ước lượng thương\n'
            '- Ví dụ 1: $672 : 21$. Lượt 1: lấy $67 : 21$, nhẩm $6 : 2 = 3$; thử $3 \\times 21 = 63$, $67 - '
            '63 = 4$. Lượt 2: hạ $2$ được $42 : 21 = 2$, dư $0$. Vậy $672 : 21 = 32$.\n'
            '- Ví dụ 2: $864 : 24$. Lượt 1: $86 : 24 = 3$ (vì $3 \\times 24 = 72$, dư $14$). Lượt 2: hạ $4$ '
            'được $144 : 24 = 6$. Vậy $864 : 24 = 36$.\n'
            '### 2. Rút gọn chữ số $0$ tận cùng khi chia hai số tròn chục\n'
            '- Khi cả số bị chia và số chia đều có chữ số $0$ ở tận cùng, ta có thể cùng划 bỏ một số lượng '
            'chữ số $0$ bằng nhau ở tận cùng hai số: $360 : 40 = 36 : 4 = 9$.',
  'formulas': [{'category': 'I. Chia cho số có hai chữ số',
                'items': [{'name': 'Ước lượng thương',
                           'formula': 'Làm tròn số chia đến hàng chục để nhẩm thương'},
                          {'name': 'Chia hai số tròn chục',
                           'formula': '$a0 : b0 = a : b$',
                           'note': 'Ví dụ: $420 : 60 = 42 : 6 = 7$'}]}],
  'example': 'Đặt tính rồi tính: $672 : 21$ và $864 : 24$.',
  'example_answer': '- $672 : 21 = 32$.\n- $864 : 24 = 36$.',
  'real_life': '- Tính số thùng hàng cần đóng khi biết tổng số gói bánh và mỗi thùng đựng $24$ gói.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính nhẩm: $540 : 90 = ?$',
            'options': ['$6$', '$60$', '$54$', '$450$'],
            'answer': 0,
            'solution': 'Cùng bỏ $1$ chữ số $0$ ở tận cùng: $540 : 90 = 54 : 9 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $672 : 21$ là:',
            'options': ['$23$', '$32$', '$31$', '$42$'],
            'answer': 1,
            'solution': 'Ta có $67 : 21 = 3$ (dư $4$), hạ $2$ được $42 : 21 = 2 \\rightarrow 32$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Ước lượng thương**?',
            'options': ['$a0 : b0 = a : b$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Làm tròn số chia đến hàng chục để nhẩm thương',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 44, 45: Chia cho số có hai chữ số và ước '
                        'lượng thương, **Ước lượng thương** được xác định bởi: Làm tròn số chia đến hàng '
                        'chục để nhẩm thương.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương**, nội dung/biểu thức '
                 '$a0 : b0 = a : b$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Ước lượng thương', 'Phân tích số', 'Quy tắc 5', 'Chia hai số tròn chục'],
            'answer': 3,
            'solution': 'Trong Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương, biểu thức/quy tắc '
                        '$a0 : b0 = a : b$ chính là nội dung của **Chia hai số tròn chục**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một mảnh đất hình chữ nhật có diện tích $720\\text{ m}^2$ và chiều rộng $18\\text{ m}$. '
                 'Chiều dài mảnh đất đó là:',
            'options': ['$40\\text{ m}$', '$4\\text{ m}$', '$36\\text{ m}$', '$45\\text{ m}$'],
            'answer': 0,
            'solution': 'Chiều dài bằng diện tích chia chiều rộng: $720 : 18 = 40\\text{ (m)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương** (Chủ đề 8: Phép nhân '
                 'và phép chia), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Biết làm tròn số bị chia và số chia đến hàng chục để ước lượng thương trong mỗi '
                        'lượt chia.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương: '
                        'Biết làm tròn số bị chia và số chia đến hàng chục để ước lượng thương trong mỗi '
                        'lượt chia.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phép chia $864 : 24$ có thương bằng $36$."',
            'answer': True,
            'solution': 'Thử lại: $36 \\times 24 = 864$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương**, quy tắc **Ước lượng '
                 'thương** được xác định bởi Làm tròn số chia đến hàng chục để nhẩm thương và áp dụng trực '
                 'tiếp vào bài toán: “Đặt tính rồi tính: $672 : 21$ và $864 : 24$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Ước lượng thương** (Làm tròn số chia đến hàng chục '
                        'để nhẩm thương) là kiến thức cốt lõi của Bài 44, 45: Chia cho số có hai chữ số và '
                        'ước lượng thương. - $672 : 21 = 32$. - $864 : 24 = 36$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương** để giải '
                 'quyết tình huống sau: Đặt tính rồi tính: $672 : 21$ và $864 : 24$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- $672 : 21 = 32$. - $864 : 24 = 36$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 44, 45: Chia cho số có hai chữ số và ước lượng thương: - '
                        '$672 : 21 = 32$.\n'
                        '- $864 : 24 = 36$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Người ta xếp $1\\,080$ hộp sữa vào các thùng, mỗi thùng $24$ hộp. Hỏi xếp được tất cả bao '
                 'nhiêu thùng sữa?',
            'answer': ['45'],
            'unit': 'thùng',
            'solution': 'Số thùng sữa xếp được là: $1\\,080 : 24 = 45\\text{ (thùng)}$.\n'
                        'Đáp số: **$45\\text{ thùng}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd08-phep-nhan-va-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân và phép chia',
  'context': 'SGK Toán 4 · Chủ đề 8: Phép nhân, phép chia với số có một, hai chữ số; tính chất phép nhân; '
             'trung bình cộng; rút về đơn vị.',
  'title': 'Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị',
  'icon': '📊',
  'description': 'Quy tắc tìm số trung bình cộng của nhiều số và phương pháp giải bài toán liên quan đến rút '
                 'về đơn vị.',
  'requirements': ['Thuộc và vận dụng đúng quy tắc tìm số trung bình cộng: lấy tổng các số chia cho số các '
                   'số hạng.',
                   'Tìm được tổng của các số khi biết số trung bình cộng và số các số hạng.',
                   'Giải thành thạo hai dạng bài toán liên quan đến rút về đơn vị.'],
  'definition': '- **Số trung bình cộng**: Muốn tìm số trung bình cộng của nhiều số, ta tính **tổng của các '
                'số đó**, rồi **chia tổng đó cho số các số hạng**.\n'
                '- **Bài toán rút về đơn vị**:\n'
                '  - **Bước 1 (Rút về đơn vị)**: Tìm giá trị của **$1$ phần** (thực hiện phép chia).\n'
                '  - **Bước 2**: Tìm giá trị của **nhiều phần** (thực hiện phép nhân) hoặc tìm **số phần** '
                '(thực hiện phép chia).',
  'theory': '### 1. Tìm số trung bình cộng\n'
            '- Trung bình cộng của $2$ số $a, b$: $(a + b) : 2$.\n'
            '- Trung bình cộng của $3$ số $a, b, c$: $(a + b + c) : 3$.\n'
            '- Lưu ý: Nếu biết trung bình cộng của $n$ số là $M$ thì tổng của $n$ số đó là $S = M \\times '
            'n$.\n'
            '### 2. Hai dạng bài toán rút về đơn vị\n'
            '- **Dạng 1**: Mua $6$ quyển vở hết $42\\,000$ đồng. Hỏi mua $9$ quyển vở hết bao nhiêu tiền? '
            '($1$ quyển: $42\\,000 : 6 = 7\\,000$ đồng $\\rightarrow 9$ quyển: $7\\,000 \\times 9 = '
            '63\\,000$ đồng).\n'
            '- **Dạng 2**: Có $40$ cái bánh xếp đều vào $5$ hộp. Hỏi có $72$ cái bánh thì xếp được mấy hộp '
            'như thế? ($1$ hộp: $40 : 5 = 8$ cái $\\rightarrow$ số hộp: $72 : 8 = 9$ hộp).',
  'formulas': [{'category': 'I. Số trung bình cộng',
                'items': [{'name': 'Công thức',
                           'formula': '$\\text{TBC} = \\text{Tổng các số} : \\text{Số các số hạng}$'},
                          {'name': 'Tìm tổng từ TBC',
                           'formula': '$\\text{Tổng các số} = \\text{TBC} \\times \\text{Số các số hạng}$'}]},
               {'category': 'II. Rút về đơn vị',
                'items': [{'name': 'Bước 1',
                           'formula': 'Giá trị $1$ đơn vị $= \\text{Tổng giá trị} : \\text{Số đơn vị}$'},
                          {'name': 'Bước 2',
                           'formula': 'Nhân với số đơn vị mới (hoặc lấy tổng mới chia cho giá trị $1$ đơn '
                                      'vị)'}]}],
  'example': 'Một ô tô trong $3$ giờ đầu đi được $135\\text{ km}$, trong $2$ giờ sau đi được $95\\text{ '
             'km}$. Hỏi trung bình mỗi giờ ô tô đi được bao nhiêu ki-lô-mét?',
  'example_answer': 'Tổng số giờ ô tô đã đi là: $3 + 2 = 5\\text{ (giờ)}$.\n'
                    'Tổng quãng đường ô tô đi được là: $135 + 95 = 230\\text{ (km)}$.\n'
                    'Trung bình mỗi giờ ô tô đi được là: $230 : 5 = 46\\text{ (km)}$.',
  'real_life': '- Tính điểm trung bình học tập, chiều cao trung bình của các bạn trong tổ; tính giá tiền mua '
               'hàng theo đơn giá.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số trung bình cộng của ba số $12, 18$ và $21$ là:',
            'options': ['$51$', '$17$', '$16$', '$18$'],
            'answer': 1,
            'solution': 'Ta có $(12 + 18 + 21) : 3 = 51 : 3 = 17$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mua $6$ quyển vở như nhau hết $42\\,000$ đồng. Hỏi mua $9$ quyển vở như thế hết bao nhiêu '
                 'tiền?',
            'options': ['$54\\,000$ đồng', '$72\\,000$ đồng', '$63\\,000$ đồng', '$378\\,000$ đồng'],
            'answer': 2,
            'solution': 'Giá $1$ quyển vở là: $42\\,000 : 6 = 7\\,000$ (đồng). Mua $9$ quyển hết: $7\\,000 '
                        '\\times 9 = 63\\,000$ (đồng).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về '
                 'đơn vị**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Công thức**?',
            'options': ['$\\text{Tổng các số} = \\text{TBC} \\times \\text{Số các số hạng}$',
                        'Giá trị $1$ đơn vị $= \\text{Tổng giá trị} : \\text{Số đơn vị}$',
                        'Nhân với số đơn vị mới (hoặc lấy tổng mới chia cho giá trị $1$ đơn vị)',
                        '$\\text{TBC} = \\text{Tổng các số} : \\text{Số các số hạng}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 46, 47, 48: Tìm số trung bình cộng và bài '
                        'toán rút về đơn vị, **Công thức** được xác định bởi: $\\text{TBC} = \\text{Tổng các '
                        'số} : \\text{Số các số hạng}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị**, nội dung/biểu '
                 'thức $\\text{Tổng các số} = \\text{TBC} \\times \\text{Số các số hạng}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Tìm tổng từ TBC', 'Công thức', 'Bước 1', 'Bước 2'],
            'answer': 0,
            'solution': 'Trong Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị, biểu '
                        'thức/quy tắc $\\text{Tổng các số} = \\text{TBC} \\times \\text{Số các số hạng}$ '
                        'chính là nội dung của **Tìm tổng từ TBC**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trung bình cộng của hai số là $45$, biết một trong hai số là $38$. Số còn lại là:',
            'options': ['$7$', '$52$', '$83$', '$41$'],
            'answer': 1,
            'solution': 'Tổng của hai số là: $45 \\times 2 = 90$. Số còn lại là: $90 - 38 = 52$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị** (Chủ đề 8: '
                 'Phép nhân và phép chia), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Thuộc và vận dụng đúng quy tắc tìm số trung bình cộng: lấy tổng các số chia cho số '
                        'các số hạng.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về '
                        'đơn vị: Thuộc và vận dụng đúng quy tắc tìm số trung bình cộng: lấy tổng các số chia '
                        'cho số các số hạng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Số trung bình cộng của bốn số $32, 35, 30$ và $31$ là $32$."',
            'answer': True,
            'solution': 'Tổng bốn số là $32 + 35 + 30 + 31 = 128$; trung bình cộng là $128 : 4 = 32$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị**, quy tắc **Công '
                 'thức** được xác định bởi $\\text{TBC} = \\text{Tổng các số} : \\text{Số các số hạng}$ và '
                 'áp dụng trực tiếp vào bài toán: “Một ô tô trong $3$ giờ đầu đi được $135\\text{ km}$, '
                 'trong $2$ giờ sau đi được $95\\text{ km}$. Hỏi trung bình mỗi giờ ô tô đi được bao '
                 'nhiêu...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Công thức** ($\\text{TBC} = \\text{Tổng các số} : '
                        '\\text{Số các số hạng}$) là kiến thức cốt lõi của Bài 46, 47, 48: Tìm số trung bình '
                        'cộng và bài toán rút về đơn vị. Tổng số giờ ô tô đã đi là: $3 + 2 = 5\\text{ '
                        '(giờ)}$. Tổng quãng đường ô tô đi được là: $135 + 95 = 230\\text{ (km)}$. Trung '
                        'bình mỗi giờ ô tô...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về đơn vị** để '
                 'giải quyết tình huống sau: Một ô tô trong $3$ giờ đầu đi được $135\\text{ km}$, trong $2$ '
                 'giờ sau đi được $95\\text{ km}$. Hỏi trung bình mỗi giờ ô tô đi được bao nhiêu ki-lô-mét? '
                 'Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Tổng số giờ ô tô đã đi là: $3 + 2 = 5\\text{ (giờ)}$. Tổng quãng đường ô tô đi được '
                        'là: $135 + 95 = 230\\text{ (km)}$. Trung bình mỗi giờ ô tô đi được là: $230 : 5 = '
                        '46\\text{ (km)}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 46, 47, 48: Tìm số trung bình cộng và bài toán rút về '
                        'đơn vị: Tổng số giờ ô tô đã đi là: $3 + 2 = 5\\text{ (giờ)}$.\n'
                        'Tổng quãng đường ô tô đi được là: $135 + 95 = 230\\text{ (km)}$.\n'
                        'Trung bình mỗi giờ ô tô đi được là: $230 : 5 = 46\\text{ (km)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $48\\text{ kg}$ gạo chia đều vào $8$ túi. Hỏi có $90\\text{ kg}$ gạo thì chia đều được '
                 'vào bao nhiêu túi như thế?',
            'answer': ['15'],
            'unit': 'túi',
            'solution': 'Mỗi túi đựng: $48 : 8 = 6\\text{ (kg)}$. Số túi để đựng $90\\text{ kg}$ gạo là: $90 '
                        ': 6 = 15\\text{ (túi)}$.\n'
                        'Đáp số: **$15\\text{ túi}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd09-thong-ke-xac-suat',
  'context_title': 'Chủ đề 9: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 4 · Chủ đề 9: Dãy số liệu thống kê; biểu đồ cột; số lần xuất hiện của một sự kiện.',
  'title': 'Bài 49: Dãy số liệu thống kê',
  'icon': '📋',
  'description': 'Nhận biết dãy số liệu thống kê, sắp xếp dãy số liệu và tính số trung bình cộng của dãy số '
                 'liệu.',
  'requirements': ['Đọc được số liệu thứ nhất, thứ hai, ... và biết dãy số liệu có bao nhiêu số.',
                   'Sắp xếp được dãy số liệu theo thứ tự từ bé đến lớn hoặc từ lớn đến bé.',
                   'Tìm được số lớn nhất, số bé nhất, tổng và trung bình cộng của dãy số liệu.'],
  'definition': '- Khi ghi lại các số liệu thu thập được theo một thứ tự nhất định, ta được một **dãy số '
                'liệu thống kê**.\n'
                '- Từ dãy số liệu, ta xác định được: tổng số các số liệu, số liệu thứ $k$, giá trị lớn nhất, '
                'giá trị bé nhất và số trung bình cộng.',
  'theory': '### 1. Đọc dãy số liệu\n'
            '- Ví dụ: Chiều cao (tính theo $\\text{cm}$) của $4$ bạn lần lượt là: $135, 128, 142, 130$.\n'
            '- Dãy trên có $4$ số liệu; số liệu thứ nhất là $135$, số liệu thứ ba là $142$.\n'
            '### 2. Xử lý số liệu\n'
            '- Sắp xếp từ bé đến lớn: $128, 130, 135, 142$.\n'
            '- Tính trung bình cộng của dãy: $(135 + 128 + 142 + 130) : 4$.',
  'formulas': [{'category': 'I. Khai thác dãy số liệu',
                'items': [{'name': 'Khoảng chênh lệch',
                           'formula': '$\\text{Số lớn nhất} - \\text{Số bé nhất}$'},
                          {'name': 'Trung bình cộng của dãy',
                           'formula': '$\\text{TBC} = \\text{Tổng các số liệu} : \\text{Số các số liệu}$'}]}],
  'example': 'Dãy số liệu ghi số cây trồng được của $4$ tổ là: $15, 18, 12, 19$. Hỏi trung bình mỗi tổ trồng '
             'được bao nhiêu cây?',
  'example_answer': 'Trung bình mỗi tổ trồng được số cây là: $(15 + 18 + 12 + 19) : 4 = 64 : 4 = 16\\text{ '
                    '(cây)}$.\n'
                    'Đáp số: **$16\\text{ cây}$**.',
  'real_life': '- Ghi chép lượng điện tiêu thụ trong $6$ tháng đầu năm hoặc số trang sách đọc được mỗi ngày.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho dãy số liệu chiều cao (đơn vị $\\text{cm}$): $135, 128, 142, 130$. Số liệu thứ ba '
                 'trong dãy là:',
            'options': ['$135$', '$128$', '$142$', '$130$'],
            'answer': 2,
            'solution': 'Đếm từ trái sang phải: thứ nhất là $135$, thứ hai là $128$, **thứ ba là $142$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dãy số liệu $135, 128, 142, 130$ có tất cả mấy số liệu?',
            'options': ['$3$ số liệu', '$5$ số liệu', '$135$ số liệu', '$4$ số liệu'],
            'answer': 3,
            'solution': 'Dãy gồm **$4$ số liệu**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 49: Dãy số liệu thống kê**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Khoảng chênh lệch**?',
            'options': ['$\\text{Số lớn nhất} - \\text{Số bé nhất}$',
                        '$\\text{TBC} = \\text{Tổng các số liệu} : \\text{Số các số liệu}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 49: Dãy số liệu thống kê, **Khoảng chênh '
                        'lệch** được xác định bởi: $\\text{Số lớn nhất} - \\text{Số bé nhất}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 49: Dãy số liệu thống kê**, nội dung/biểu thức $\\text{TBC} = \\text{Tổng các '
                 'số liệu} : \\text{Số các số liệu}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Khoảng chênh lệch', 'Trung bình cộng của dãy', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 49: Dãy số liệu thống kê, biểu thức/quy tắc $\\text{TBC} = \\text{Tổng '
                        'các số liệu} : \\text{Số các số liệu}$ chính là nội dung của **Trung bình cộng của '
                        'dãy**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho dãy số cân nặng của $4$ bao gạo: $45\\text{ kg}, 52\\text{ kg}, 38\\text{ kg}, '
                 '49\\text{ kg}$. Bao nặng nhất hơn bao nhẹ nhất bao nhiêu ki-lô-gam?',
            'options': ['$7\\text{ kg}$', '$11\\text{ kg}$', '$14\\text{ kg}$', '$4\\text{ kg}$'],
            'answer': 2,
            'solution': 'Bao nặng nhất là $52\\text{ kg}$, bao nhẹ nhất là $38\\text{ kg}$. Hiệu là: $52 - '
                        '38 = 14\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 49: Dãy số liệu thống kê** (Chủ đề 9: Làm quen với yếu tố thống kê, xác '
                 'suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Đọc được số liệu thứ nhất, thứ hai, ... và biết dãy số liệu có bao nhiêu số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 49: Dãy số liệu thống kê: Đọc được số liệu thứ nhất, '
                        'thứ hai, ... và biết dãy số liệu có bao nhiêu số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khi sắp xếp dãy số liệu $15, 18, 12, 19$ theo thứ tự từ bé đến lớn ta được '
                 '$12, 15, 18, 19$."',
            'answer': True,
            'solution': 'Ta có $12 < 15 < 18 < 19$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 49: Dãy số liệu thống kê**, quy tắc **Khoảng chênh lệch** được xác định bởi '
                 '$\\text{Số lớn nhất} - \\text{Số bé nhất}$ và áp dụng trực tiếp vào bài toán: “Dãy số liệu '
                 'ghi số cây trồng được của $4$ tổ là: $15, 18, 12, 19$. Hỏi trung bình mỗi tổ trồng được '
                 'bao nhiêu cây?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Khoảng chênh lệch** ($\\text{Số lớn nhất} - '
                        '\\text{Số bé nhất}$) là kiến thức cốt lõi của Bài 49: Dãy số liệu thống kê. Trung '
                        'bình mỗi tổ trồng được số cây là: $(15 + 18 + 12 + 19) : 4 = 64 : 4 = 16\\text{ '
                        '(cây)}$. Đáp số: **$16\\text{ cây}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 49: Dãy số liệu thống kê** để giải quyết tình huống sau: Dãy số '
                 'liệu ghi số cây trồng được của $4$ tổ là: $15, 18, 12, 19$. Hỏi trung bình mỗi tổ trồng '
                 'được bao nhiêu cây? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trung bình mỗi tổ trồng được số cây là: $(15 + 18 + 12 + 19) : 4 = 64 : 4 = '
                        '16\\text{ (cây)}$. Đáp số: **$16\\text{ cây}$**.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 49: Dãy số liệu thống kê: Trung bình mỗi tổ trồng được '
                        'số cây là: $(15 + 18 + 12 + 19) : 4 = 64 : 4 = 16\\text{ (cây)}$.\n'
                        'Đáp số: **$16\\text{ cây}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Dãy số liệu ghi số ki-lô-mét bác Ba chạy bộ trong $5$ ngày liên tiếp là: $4, 6, 5, 7, 8$. '
                 'Hỏi trung bình mỗi ngày bác Ba chạy được bao nhiêu ki-lô-mét?',
            'answer': ['6'],
            'unit': 'km',
            'solution': 'Trung bình mỗi ngày bác Ba chạy được: $(4 + 6 + 5 + 7 + 8) : 5 = 30 : 5 = 6\\text{ '
                        '(km)}$.\n'
                        'Đáp số: **$6\\text{ km}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd09-thong-ke-xac-suat',
  'context_title': 'Chủ đề 9: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 4 · Chủ đề 9: Dãy số liệu thống kê; biểu đồ cột; số lần xuất hiện của một sự kiện.',
  'title': 'Bài 50: Biểu đồ cột',
  'icon': '📊',
  'description': 'Cách đọc, mô tả và phân tích số liệu được biểu diễn trên biểu đồ cột.',
  'requirements': ['Nhận biết cấu tạo của biểu đồ cột (tên biểu đồ, trục ngang ghi đối tượng, trục đứng ghi '
                   'số liệu, độ cao các cột).',
                   'Đọc được số liệu của từng cột và so sánh thông qua chiều cao của các cột.',
                   'Thực hiện được các phép tính tổng, hiệu, trung bình cộng từ số liệu trên biểu đồ cột.'],
  'definition': '- **Biểu đồ cột** dùng các cột hình chữ nhật có độ rộng bằng nhau để biểu diễn số liệu '
                '(trục đứng bắt đầu từ vạch $0$).\n'
                '- **Trục ngang** ghi tên các đối tượng; **trục đứng** ghi các vạch số liệu.\n'
                '- Cột nào **cao hơn** ($h_1 > h_2$) thì biểu diễn số liệu **lớn hơn**.',
  'theory': '### 1. Các bước đọc biểu đồ cột\n'
            '- Bước 1: Đọc tên biểu đồ để biết biểu đồ nói về nội dung gì.\n'
            '- Bước 2: Nhìn tên đối tượng ở chân cột, gióng đỉnh cột sang trục đứng (hoặc đọc số ghi trên '
            'đỉnh cột) để biết giá trị.\n'
            '### 2. Tính toán từ biểu đồ cột\n'
            '- Ví dụ: Biểu đồ số học sinh đạt giải của 4 lớp: 4A ($8$ bạn), 4B ($12$ bạn), 4C ($10$ bạn), 4D '
            '($6$ bạn).\n'
            '  - Lớp 4B có cột cao nhất ($12$ bạn); lớp 4D có cột thấp nhất ($6$ bạn).\n'
            '  - Tổng số học sinh đạt giải là: $8 + 12 + 10 + 6 = 36$ (bạn).',
  'formulas': [{'category': 'I. Biểu đồ cột',
                'items': [{'name': 'Quan sát trực quan',
                           'formula': 'Cột cao nhất $\\leftrightarrow$ Giá trị lớn nhất · Cột thấp nhất '
                                      '$\\leftrightarrow$ Giá trị bé nhất'},
                          {'name': 'Trung bình mỗi cột',
                           'formula': '$\\text{Tổng giá trị các cột} : \\text{Số cột}$'}]}],
  'example': 'Biểu đồ cột biểu diễn số học sinh đạt giải của khối 4: lớp 4A ($8$), lớp 4B ($12$), lớp 4C '
             '($10$), lớp 4D ($6$). Tính trung bình mỗi lớp có bao nhiêu học sinh đạt giải?',
  'example_answer': 'Tổng số học sinh đạt giải của $4$ lớp là: $8 + 12 + 10 + 6 = 36\\text{ (học sinh)}$.\n'
                    'Trung bình mỗi lớp có: $36 : 4 = 9\\text{ (học sinh đạt giải)}$.',
  'real_life': '- Xem biểu đồ lượng mưa các tháng trong năm, biểu đồ sản lượng xuất khẩu gạo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong biểu đồ cột, cột cao nhất biểu diễn:',
            'options': ['Số liệu bé nhất', 'Tổng các số liệu', 'Trung bình cộng', 'Số liệu lớn nhất'],
            'answer': 3,
            'solution': 'Cột cao nhất ứng với **số liệu lớn nhất**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ cột số học sinh đạt giải của 4 lớp: 4A ($8$), 4B ($12$), 4C ($10$), 4D ($6$). Tổng '
                 'số học sinh đạt giải của cả 4 lớp là:',
            'options': ['$36$ học sinh', '$32$ học sinh', '$34$ học sinh', '$40$ học sinh'],
            'answer': 0,
            'solution': 'Tổng là: $8 + 12 + 10 + 6 = 36\\text{ (học sinh)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 50: Biểu đồ cột**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Quan sát trực quan**?',
            'options': ['$\\text{Tổng giá trị các cột} : \\text{Số cột}$',
                        'Cột cao nhất $\\leftrightarrow$ Giá trị lớn nhất · Cột thấp nhất $\\leftrightarrow$ '
                        'Giá trị bé nhất',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 50: Biểu đồ cột, **Quan sát trực quan** được '
                        'xác định bởi: Cột cao nhất $\\leftrightarrow$ Giá trị lớn nhất · Cột thấp nhất '
                        '$\\leftrightarrow$ Giá trị bé nhất.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 50: Biểu đồ cột**, nội dung/biểu thức $\\text{Tổng giá trị các cột} : '
                 '\\text{Số cột}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quan sát trực quan', 'Phân tích số', 'Trung bình mỗi cột', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 50: Biểu đồ cột, biểu thức/quy tắc $\\text{Tổng giá trị các cột} : '
                        '\\text{Số cột}$ chính là nội dung của **Trung bình mỗi cột**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Theo biểu đồ trên (4A: $8$, 4B: $12$, 4C: $10$, 4D: $6$), lớp 4B có nhiều hơn lớp 4D bao '
                 'nhiêu học sinh đạt giải?',
            'options': ['$4$ học sinh', '$2$ học sinh', '$18$ học sinh', '$6$ học sinh'],
            'answer': 3,
            'solution': 'Ta lấy $12 - 6 = 6\\text{ (học sinh)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 50: Biểu đồ cột** (Chủ đề 9: Làm quen với yếu tố thống kê, xác suất), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết cấu tạo của biểu đồ cột (tên biểu đồ, trục ngang ghi đối tượng, trục đứng '
                        'ghi số liệu, độ cao các cột).',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 50: Biểu đồ cột: Nhận biết cấu tạo của biểu đồ cột '
                        '(tên biểu đồ, trục ngang ghi đối tượng, trục đứng ghi số liệu, độ cao các cột).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Theo biểu đồ trên (4A: $8$, 4B: $12$, 4C: $10$, 4D: $6$), trung bình mỗi lớp '
                 'có $9$ học sinh đạt giải."',
            'answer': True,
            'solution': 'Tổng là $36$, chia cho $4$ lớp được $36 : 4 = 9$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 50: Biểu đồ cột**, quy tắc **Quan sát trực quan** được xác định bởi Cột cao '
                 'nhất $\\leftrightarrow$ Giá trị lớn nhất · Cột thấp nhất $\\leftrightarrow$ Giá trị bé '
                 'nhất và áp dụng trực tiếp vào bài toán: “Biểu đồ cột biểu diễn số học sinh đạt giải của '
                 'khối 4: lớp 4A ($8$), lớp 4B ($12$), lớp 4C ($10$), lớp 4D ($6$). Tính trung bình mỗi lớp '
                 'có...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quan sát trực quan** (Cột cao nhất '
                        '$\\leftrightarrow$ Giá trị lớn nhất · Cột thấp nhất $\\leftrightarrow$ Giá trị bé '
                        'nhất) là kiến thức cốt lõi của Bài 50: Biểu đồ cột. Tổng số học sinh đạt giải của '
                        '$4$ lớp là: $8 + 12 + 10 + 6 = 36\\text{ (học sinh)}$. Trung bình mỗi lớp có: $36 : '
                        '4 = 9\\text{ (học sinh đạt giải)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 50: Biểu đồ cột** để giải quyết tình huống sau: Biểu đồ cột biểu '
                 'diễn số học sinh đạt giải của khối 4: lớp 4A ($8$), lớp 4B ($12$), lớp 4C ($10$), lớp 4D '
                 '($6$). Tính trung bình mỗi lớp có bao nhiêu học sinh đạt giải? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Tổng số học sinh đạt giải của $4$ lớp là: $8 + 12 + 10 + 6 = 36\\text{ (học '
                        'sinh)}$. Trung bình mỗi lớp có: $36 : 4 = 9\\text{ (học sinh đạt giải)}$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 50: Biểu đồ cột: Tổng số học sinh đạt giải của $4$ lớp '
                        'là: $8 + 12 + 10 + 6 = 36\\text{ (học sinh)}$.\n'
                        'Trung bình mỗi lớp có: $36 : 4 = 9\\text{ (học sinh đạt giải)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biểu đồ cột ghi số quyển sách $3$ bạn đọc trong mùa hè: Lan đọc $11$ quyển, Mai đọc $15$ '
                 'quyển, Hùng đọc $10$ quyển. Hỏi trung bình mỗi bạn đọc được bao nhiêu quyển sách?',
            'answer': ['12'],
            'unit': 'quyển',
            'solution': 'Trung bình mỗi bạn đọc được: $(11 + 15 + 10) : 3 = 36 : 3 = 12\\text{ (quyển)}$.\n'
                        'Đáp số: **$12\\text{ quyển}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd09-thong-ke-xac-suat',
  'context_title': 'Chủ đề 9: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 4 · Chủ đề 9: Dãy số liệu thống kê; biểu đồ cột; số lần xuất hiện của một sự kiện.',
  'title': 'Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung',
  'icon': '🎲',
  'description': 'Kiểm đếm và tính toán số lần lặp lại của một sự kiện khi thực hiện thí nghiệm, trò chơi '
                 'nhiều lần.',
  'requirements': ['Kiểm đếm được số lần xuất hiện của mỗi khả năng khi lặp lại thí nghiệm nhiều lần.',
                   'Nắm vững quy tắc: Tổng số lần thực hiện thí nghiệm bằng tổng số lần xuất hiện của tất cả '
                   'các khả năng.',
                   'Giải được bài toán tìm số lần xuất hiện của sự kiện còn lại.'],
  'definition': '- Khi thực hiện một thí nghiệm hoặc trò chơi $N$ lần, ta đếm được một sự kiện xảy ra $k$ '
                'lần. Số $k$ gọi là **số lần xuất hiện** của sự kiện đó.\n'
                '- **Quy tắc bảo toàn số lần thử**: $\\text{Tổng số lần thử} = \\text{Tổng số lần xuất hiện '
                'của tất cả các kết quả}$.',
  'theory': '### 1. Ví dụ tung đồng xu nhiều lần\n'
            '- Tung một đồng xu $10$ lần liên tiếp, nếu mặt sấp xuất hiện $4$ lần thì mặt ngửa xuất hiện $10 '
            '- 4 = 6$ lần.\n'
            '### 2. Ví dụ gieo xúc xắc hoặc lấy bóng từ hộp\n'
            '- Khi thực hiện ngẫu nhiên, số lần xuất hiện của mỗi mặt có thể khác nhau ở mỗi đợt thử, không '
            'bắt buộc phải chia đều bằng nhau.',
  'formulas': [{'category': 'I. Số lần xuất hiện của sự kiện',
                'items': [{'name': 'Quan hệ tổng',
                           'formula': '$N = n_1 + n_2 + \\dots + n_k$ (tổng số lần thử)'},
                          {'name': 'Tìm sự kiện còn lại (2 khả năng)', 'formula': '$n_2 = N - n_1$'}]}],
  'example': 'Gieo một con xúc xắc $30$ lần, người ta ghi lại số lần xuất hiện các mặt như sau: mặt $1$ chấm '
             '($4$ lần), mặt $2$ chấm ($6$ lần), mặt $3$ chấm ($5$ lần), mặt $4$ chấm ($3$ lần), mặt $5$ '
             'chấm ($7$ lần). Hỏi mặt $6$ chấm xuất hiện bao nhiêu lần?',
  'example_answer': 'Tổng số lần xuất hiện từ mặt $1$ chấm đến mặt $5$ chấm là: $4 + 6 + 5 + 3 + 7 = '
                    '25\\text{ (lần)}$.\n'
                    'Số lần mặt $6$ chấm xuất hiện là: $30 - 25 = 5\\text{ (lần)}$.',
  'real_life': '- Thống kê số trận thắng, hòa, thua của một đội bóng sau một mùa giải.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tung một đồng xu $10$ lần liên tiếp, biết mặt sấp xuất hiện $4$ lần. Hỏi mặt ngửa xuất '
                 'hiện mấy lần?',
            'options': ['$6$ lần', '$4$ lần', '$10$ lần', '$14$ lần'],
            'answer': 0,
            'solution': 'Số lần mặt ngửa xuất hiện là: $10 - 4 = 6\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hộp có bóng xanh và bóng đỏ. Nam lấy ra $1$ quả bóng, xem màu rồi trả lại vào hộp, '
                 'lặp lại $20$ lần thì thấy có $13$ lần lấy được bóng xanh. Số lần lấy được bóng đỏ là:',
            'options': ['$13$ lần', '$7$ lần', '$20$ lần', '$33$ lần'],
            'answer': 1,
            'solution': 'Số lần lấy được bóng đỏ là: $20 - 13 = 7\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập '
                 'chung**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Quan hệ tổng**?',
            'options': ['$n_2 = N - n_1$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$N = n_1 + n_2 + \\dots + n_k$ (tổng số lần thử)',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 51, 52: Số lần xuất hiện của một sự kiện và '
                        'luyện tập chung, **Quan hệ tổng** được xác định bởi: $N = n_1 + n_2 + \\dots + n_k$ '
                        '(tổng số lần thử).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung**, nội dung/biểu '
                 'thức $n_2 = N - n_1$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quan hệ tổng', 'Phân tích số', 'Quy tắc 5', 'Tìm sự kiện còn lại (2 khả năng)'],
            'answer': 3,
            'solution': 'Trong Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung, biểu '
                        'thức/quy tắc $n_2 = N - n_1$ chính là nội dung của **Tìm sự kiện còn lại (2 khả '
                        'năng)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Gieo một con xúc xắc $30$ lần: mặt $1$ chấm ($4$ lần), mặt $2$ chấm ($6$ lần), mặt $3$ '
                 'chấm ($5$ lần), mặt $4$ chấm ($3$ lần), mặt $5$ chấm ($7$ lần). Mặt $6$ chấm xuất hiện mấy '
                 'lần?',
            'options': ['$5$ lần', '$4$ lần', '$6$ lần', '$25$ lần'],
            'answer': 0,
            'solution': 'Tổng $5$ mặt đầu là $4+6+5+3+7 = 25$ lần. Mặt $6$ chấm xuất hiện: $30 - 25 = '
                        '5\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung** (Chủ đề 9: Làm '
                 'quen với yếu tố thống kê, xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Kiểm đếm được số lần xuất hiện của mỗi khả năng khi lặp lại thí nghiệm nhiều lần.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập '
                        'chung: Kiểm đếm được số lần xuất hiện của mỗi khả năng khi lặp lại thí nghiệm nhiều '
                        'lần.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khi gieo một con xúc xắc $12$ lần thì mặt $6$ chấm chắc chắn phải xuất hiện '
                 'đúng $2$ lần."',
            'answer': False,
            'solution': 'Kết quả mỗi lần gieo là ngẫu nhiên nên mặt $6$ chấm không nhất thiết xuất hiện đúng '
                        '$2$ lần $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung**, quy tắc **Quan '
                 'hệ tổng** được xác định bởi $N = n_1 + n_2 + \\dots + n_k$ (tổng số lần thử) và áp dụng '
                 'trực tiếp vào bài toán: “Gieo một con xúc xắc $30$ lần, người ta ghi lại số lần xuất hiện '
                 'các mặt như sau: mặt $1$ chấm ($4$ lần), mặt $2$ chấm ($6$ lần), mặt $3$ ch...”. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quan hệ tổng** ($N = n_1 + n_2 + \\dots + n_k$ (tổng '
                        'số lần thử)) là kiến thức cốt lõi của Bài 51, 52: Số lần xuất hiện của một sự kiện '
                        'và luyện tập chung. Tổng số lần xuất hiện từ mặt $1$ chấm đến mặt $5$ chấm là: $4 + '
                        '6 + 5 + 3 + 7 = 25\\text{ (lần)}$. Số lần mặt $6$ chấm xuất hiện là: $30 - 25 = '
                        '5\\text{ (lần)}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập chung** để '
                 'giải quyết tình huống sau: Gieo một con xúc xắc $30$ lần, người ta ghi lại số lần xuất '
                 'hiện các mặt như sau: mặt $1$ chấm ($4$ lần), mặt $2$ chấm ($6$ lần), mặt $3$ chấm ($5$ '
                 'lần), mặt $4$ chấm ($3$ lần), mặt $5$ chấm ($7$ lần). Hỏi mặt $6$ chấm xuất hiện bao nhiêu '
                 'lần? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Tổng số lần xuất hiện từ mặt $1$ chấm đến mặt $5$ chấm là: $4 + 6 + 5 + 3 + 7 = '
                        '25\\text{ (lần)}$. Số lần mặt $6$ chấm xuất hiện là: $30 - 25 = 5\\text{ (lần)}$...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 51, 52: Số lần xuất hiện của một sự kiện và luyện tập '
                        'chung: Tổng số lần xuất hiện từ mặt $1$ chấm đến mặt $5$ chấm là: $4 + 6 + 5 + 3 + '
                        '7 = 25\\text{ (lần)}$.\n'
                        'Số lần mặt $6$ chấm xuất hiện là: $30 - 25 = 5\\text{ (lần)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cầu thủ thực hiện $25$ quả sút phạt đền, trong đó số lần sút vào khung thành nhiều hơn '
                 'số lần sút trượt là $15$ lần. Hỏi cầu thủ đó đã sút vào khung thành bao nhiêu lần?',
            'answer': ['20'],
            'unit': 'lần',
            'solution': 'Áp dụng bài toán Tổng – Hiệu: Số lần sút vào (số lớn) là $(25 + 15) : 2 = 20\\text{ '
                        '(lần)}$.\n'
                        'Đáp số: **$20\\text{ lần}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd10-phan-so',
  'context_title': 'Chủ đề 10: Phân số',
  'context': 'SGK Toán 4 · Chủ đề 10: Khái niệm phân số; tính chất cơ bản; rút gọn, quy đồng và so sánh phân '
             'số.',
  'title': 'Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên',
  'icon': '🍰',
  'description': 'Nhận biết phân số, tử số, mẫu số; mối liên hệ giữa phép chia số tự nhiên và phân số; so '
                 'sánh phân số với 1.',
  'requirements': ['Nhận biết được phân số $\\dfrac{a}{b}$ ($b \\ne 0$) gồm tử số $a$ (trên vạch ngang) và '
                   'mẫu số $b$ (dưới vạch ngang).',
                   'Biết viết thương của phép chia hai số tự nhiên $a : b$ ($b \\ne 0$) dưới dạng phân số '
                   '$\\dfrac{a}{b}$.',
                   'Nhận biết phân số bé hơn $1$ ($a < b$), bằng $1$ ($a = b$) và lớn hơn $1$ ($a > b$).'],
  'definition': '- Mỗi **phân số** có **tử số** và **mẫu số**. Tử số là số tự nhiên viết trên gạch ngang; '
                'mẫu số là số tự nhiên **khác $0$** viết dưới gạch ngang.\n'
                '- **Thương của phép chia** số tự nhiên cho số tự nhiên (khác $0$) có thể viết thành một '
                'phân số, tử số là số bị chia và mẫu số là số chia: $a : b = \\dfrac{a}{b}$ ($b \\ne 0$).',
  'theory': '### 1. Ý nghĩa của tử số và mẫu số\n'
            '- Phân số $\\dfrac{3}{5}$ đọc là "ba phần năm": mẫu số $5$ cho biết hình được chia thành $5$ '
            'phần bằng nhau, tử số $3$ cho biết đã tô màu $3$ phần.\n'
            '### 2. So sánh phân số với $1$\n'
            '- Nếu **tử số bé hơn mẫu số** thì phân số **bé hơn $1$**: $\\dfrac{3}{5} < 1$.\n'
            '- Nếu **tử số bằng mẫu số** thì phân số **bằng $1$**: $\\dfrac{7}{7} = 1$.\n'
            '- Nếu **tử số lớn hơn mẫu số** thì phân số **lớn hơn $1$**: $\\dfrac{7}{3} > 1$.\n'
            '- Mọi số tự nhiên đều viết được thành phân số có mẫu số là $1$: $n = \\dfrac{n}{1}$.',
  'formulas': [{'category': 'I. Phân số và phép chia',
                'items': [{'name': 'Ký hiệu',
                           'formula': '$a : b = \\dfrac{a}{b}$ ($b \\ne 0$; $a$ là tử số, $b$ là mẫu số)'},
                          {'name': 'Số tự nhiên dạng phân số', 'formula': '$a = \\dfrac{a}{1}$'}]},
               {'category': 'II. So sánh với 1',
                'items': [{'name': 'Quy tắc',
                           'formula': '$\\dfrac{a}{b} < 1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 '
                                      '\\Leftrightarrow a = b$ · $\\dfrac{a}{b} > 1 \\Leftrightarrow a > '
                                      'b$'}]}],
  'example': 'Viết thương của các phép chia $4 : 7$ và $9 : 5$ dưới dạng phân số, rồi cho biết phân số nào '
             'bé hơn $1$, phân số nào lớn hơn $1$.',
  'example_answer': '- $4 : 7 = \\dfrac{4}{7}$; vì $4 < 7$ nên $\\dfrac{4}{7} < 1$.\n'
                    '- $9 : 5 = \\dfrac{9}{5}$; vì $9 > 5$ nên $\\dfrac{9}{5} > 1$.',
  'real_life': '- Chia đều $3$ cái bánh cho $4$ bạn thì mỗi bạn được $\\dfrac{3}{4}$ cái bánh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số "năm phần chín" được viết là:',
            'options': ['$\\dfrac{9}{5}$', '$\\dfrac{5}{9}$', '$5,9$', '$59$'],
            'answer': 1,
            'solution': 'Tử số là $5$, mẫu số là $9$ nên viết là **$\\dfrac{5}{9}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Thương của phép chia $4 : 7$ được viết dưới dạng phân số là:',
            'options': ['$\\dfrac{7}{4}$', '$47$', '$\\dfrac{4}{7}$', '$\\dfrac{3}{7}$'],
            'answer': 2,
            'solution': 'Số bị chia là tử số, số chia là mẫu số: $4 : 7 = \\dfrac{4}{7}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự '
                 'nhiên**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Ký hiệu**?',
            'options': ['$a = \\dfrac{a}{1}$',
                        '$\\dfrac{a}{b} < 1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 \\Leftrightarrow a '
                        '= b$ · $\\dfrac{a}{b} > 1 \\Leftrightarrow a > b$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$a : b = \\dfrac{a}{b}$ ($b \\ne 0$; $a$ là tử số, $b$ là mẫu số)'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 53, 54: Khái niệm phân số. Phân số và phép '
                        'chia số tự nhiên, **Ký hiệu** được xác định bởi: $a : b = \\dfrac{a}{b}$ ($b \\ne '
                        '0$; $a$ là tử số, $b$ là mẫu số).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên**, nội dung/biểu '
                 'thức $a = \\dfrac{a}{1}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số tự nhiên dạng phân số', 'Ký hiệu', 'Quy tắc', 'Phân tích số'],
            'answer': 0,
            'solution': 'Trong Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên, biểu '
                        'thức/quy tắc $a = \\dfrac{a}{1}$ chính là nội dung của **Số tự nhiên dạng phân '
                        'số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các phân số $\\dfrac{5}{6}, \\dfrac{7}{7}, \\dfrac{8}{5}, \\dfrac{3}{4}$, phân số '
                 'nào lớn hơn $1$?',
            'options': ['$\\dfrac{5}{6}$', '$\\dfrac{8}{5}$', '$\\dfrac{7}{7}$', '$\\dfrac{3}{4}$'],
            'answer': 1,
            'solution': 'Phân số **$\\dfrac{8}{5}$** có tử số $8$ lớn hơn mẫu số $5$ nên $\\dfrac{8}{5} > '
                        '1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên** (Chủ đề 10: '
                 'Phân số), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức '
                 'của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Nhận biết được phân số $\\dfrac{a}{b}$ ($b \\ne 0$) gồm tử số $a$ (trên vạch ngang) '
                        'và mẫu số $b$ (dưới vạch ngang).',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự '
                        'nhiên: Nhận biết được phân số $\\dfrac{a}{b}$ ($b \\ne 0$) gồm tử số $a$ (trên vạch '
                        'ngang) và mẫu số $b$ (dưới vạch ngang).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Mọi phân số có tử số bằng mẫu số (khác $0$) đều bằng $1$."',
            'answer': True,
            'solution': 'Vì $a : a = 1$ nên $\\dfrac{a}{a} = 1$ ($a \\ne 0$) $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên**, quy tắc **Ký '
                 'hiệu** được xác định bởi $a : b = \\dfrac{a}{b}$ ($b \\ne 0$; $a$ là tử số, $b$ là mẫu số) '
                 'và áp dụng trực tiếp vào bài toán: “Viết thương của các phép chia $4 : 7$ và $9 : 5$ dưới '
                 'dạng phân số, rồi cho biết phân số nào bé hơn $1$, phân số nào lớn hơn $1$.”. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Ký hiệu** ($a : b = \\dfrac{a}{b}$ ($b \\ne 0$; $a$ '
                        'là tử số, $b$ là mẫu số)) là kiến thức cốt lõi của Bài 53, 54: Khái niệm phân số. '
                        'Phân số và phép chia số tự nhiên. - $4 : 7 = \\dfrac{4}{7}$; vì $4 < 7$ nên '
                        '$\\dfrac{4}{7} < 1$. - $9 : 5 = \\dfrac{9}{5}$; vì $9 > 5$ nên $\\dfrac{9}{5} > '
                        '1$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự nhiên** để '
                 'giải quyết tình huống sau: Viết thương của các phép chia $4 : 7$ và $9 : 5$ dưới dạng phân '
                 'số, rồi cho biết phân số nào bé hơn $1$, phân số nào lớn hơn $1$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        '- $4 : 7 = \\dfrac{4}{7}$; vì $4 < 7$ nên $\\dfrac{4}{7} < 1$. - $9 : 5 = '
                        '\\dfrac{9}{5}$; vì $9 > 5$ nên $\\dfrac{9}{5} > 1$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 53, 54: Khái niệm phân số. Phân số và phép chia số tự '
                        'nhiên: - $4 : 7 = \\dfrac{4}{7}$; vì $4 < 7$ nên $\\dfrac{4}{7} < 1$.\n'
                        '- $9 : 5 = \\dfrac{9}{5}$; vì $9 > 5$ nên $\\dfrac{9}{5} > 1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Chia đều $5\\text{ l}$ sữa vào $8$ chai như nhau. Hỏi mỗi chai có mấy phần lít sữa (viết '
                 'dưới dạng a/b)?',
            'answer': ['5/8'],
            'unit': 'l',
            'solution': 'Mỗi chai có $5 : 8 = \\dfrac{5}{8}\\text{ (l)}$.\nĐáp số: **$5/8$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd10-phan-so',
  'context_title': 'Chủ đề 10: Phân số',
  'context': 'SGK Toán 4 · Chủ đề 10: Khái niệm phân số; tính chất cơ bản; rút gọn, quy đồng và so sánh phân '
             'số.',
  'title': 'Bài 55: Tính chất cơ bản của phân số',
  'icon': '⚖️',
  'description': 'Nhận biết hai phân số bằng nhau và hai tính chất cơ bản của phân số (nhân hoặc chia cả tử '
                 'và mẫu cho cùng một số).',
  'requirements': ['Hiểu và phát biểu được hai tính chất cơ bản của phân số.',
                   'Tìm được các phân số bằng với phân số đã cho bằng cách nhân hoặc chia cả tử và mẫu với '
                   'cùng một số tự nhiên khác $0$.',
                   'Điền được số thích hợp vào ô trống trong đẳng thức hai phân số bằng nhau.'],
  'definition': '- **Tính chất 1 (Nhân)**: Nếu nhân cả tử số và mẫu số của một phân số với **cùng một số tự '
                'nhiên khác $0$** thì được một phân số **bằng** phân số đã cho.\n'
                '- **Tính chất 2 (Chia)**: Nếu cả tử số và mẫu số của một phân số cùng chia hết cho một số '
                'tự nhiên khác $0$ thì sau khi chia ta được một phân số **bằng** phân số đã cho.',
  'theory': '### 1. Minh họa bằng công thức\n'
            '- Nhân cả tử và mẫu với $m$ ($m \\ne 0$): $\\dfrac{2}{3} = \\dfrac{2 \\times 4}{3 \\times 4} = '
            '\\dfrac{8}{12}$.\n'
            '- Chia cả tử và mẫu cho $n$ ($n \\ne 0$): $\\dfrac{15}{20} = \\dfrac{15 : 5}{20 : 5} = '
            '\\dfrac{3}{4}$.\n'
            '### 2. Lưu ý quan trọng\n'
            '- Chỉ đúng khi **nhân hoặc chia** cả tử và mẫu với cùng một số khác $0$; **không** áp dụng cho '
            'phép cộng hoặc phép trừ thêm cùng một số vào tử và mẫu.',
  'formulas': [{'category': 'I. Tính chất cơ bản của phân số',
                'items': [{'name': 'Nhân cả tử và mẫu',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m}$ ($m \\ne 0$)'},
                          {'name': 'Chia cả tử và mẫu',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{a : n}{b : n}$ ($n \\ne 0$)'}]}],
  'example': 'Tìm số thích hợp điền vào chỗ chấm: a) $\\dfrac{3}{5} = \\dfrac{\\dots}{20}$; b) '
             '$\\dfrac{24}{36} = \\dfrac{2}{\\dots}$.',
  'example_answer': 'a) Mẫu số nhân với $4$ ($5 \\times 4 = 20$) nên tử số cũng nhân với $4$: $3 \\times 4 = '
                    '12$. Vậy điền số **$12$**.\n'
                    'b) Tử số chia cho $12$ ($24 : 12 = 2$) nên mẫu số cũng chia cho $12$: $36 : 12 = 3$. '
                    'Vậy điền số **$3$**.',
  'real_life': '- Cắt chiếc bánh thành $4$ phần rồi ăn $2$ phần cũng giống như cắt thành $2$ phần rồi ăn $1$ '
               'phần ($\\dfrac{2}{4} = \\dfrac{1}{2}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi nhân cả tử số và mẫu số của phân số $\\dfrac{2}{3}$ với $4$, ta được phân số nào?',
            'options': ['$\\dfrac{8}{3}$', '$\\dfrac{2}{12}$', '$\\dfrac{8}{12}$', '$\\dfrac{6}{7}$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{2 \\times 4}{3 \\times 4} = \\dfrac{8}{12}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số nào dưới đây bằng phân số $\\dfrac{1}{2}$?',
            'options': ['$\\dfrac{2}{3}$', '$\\dfrac{1}{4}$', '$\\dfrac{4}{6}$', '$\\dfrac{3}{6}$'],
            'answer': 3,
            'solution': 'Vì $\\dfrac{1 \\times 3}{2 \\times 3} = \\dfrac{3}{6}$ nên **$\\dfrac{3}{6} = '
                        '\\dfrac{1}{2}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 55: Tính chất cơ bản của phân số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Nhân cả tử và mẫu**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m}$ ($m \\ne 0$)',
                        '$\\dfrac{a}{b} = \\dfrac{a : n}{b : n}$ ($n \\ne 0$)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 55: Tính chất cơ bản của phân số, **Nhân cả '
                        'tử và mẫu** được xác định bởi: $\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m}$ '
                        '($m \\ne 0$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 55: Tính chất cơ bản của phân số**, nội dung/biểu thức $\\dfrac{a}{b} = '
                 '\\dfrac{a : n}{b : n}$ ($n \\ne 0$) là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Nhân cả tử và mẫu', 'Chia cả tử và mẫu', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 55: Tính chất cơ bản của phân số, biểu thức/quy tắc $\\dfrac{a}{b} = '
                        '\\dfrac{a : n}{b : n}$ ($n \\ne 0$) chính là nội dung của **Chia cả tử và mẫu**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm trong đẳng thức $\\dfrac{4}{7} = \\dfrac{20}{\\dots}$ là:',
            'options': ['$28$', '$14$', '$35$', '$23$'],
            'answer': 2,
            'solution': 'Tử số nhân với $5$ ($4 \\times 5 = 20$) nên mẫu số là: $7 \\times 5 = 35$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 55: Tính chất cơ bản của phân số** (Chủ đề 10: Phân số), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Hiểu và phát biểu được hai tính chất cơ bản của phân số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 55: Tính chất cơ bản của phân số: Hiểu và phát biểu '
                        'được hai tính chất cơ bản của phân số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Hai phân số $\\dfrac{4}{6}$ và $\\dfrac{6}{9}$ bằng nhau."',
            'answer': True,
            'solution': 'Cùng chia tử và mẫu thì $\\dfrac{4}{6} = \\dfrac{2}{3}$ và $\\dfrac{6}{9} = '
                        '\\dfrac{2}{3}$ nên hai phân số bằng nhau $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 55: Tính chất cơ bản của phân số**, quy tắc **Nhân cả tử và mẫu** được xác '
                 'định bởi $\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m}$ ($m \\ne 0$) và áp dụng trực '
                 'tiếp vào bài toán: “Tìm số thích hợp điền vào chỗ chấm: a) $\\dfrac{3}{5} = '
                 '\\dfrac{\\dots}{20}$; b) $\\dfrac{24}{36} = \\dfrac{2}{\\dots}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhân cả tử và mẫu** ($\\dfrac{a}{b} = \\dfrac{a '
                        '\\times m}{b \\times m}$ ($m \\ne 0$)) là kiến thức cốt lõi của Bài 55: Tính chất '
                        'cơ bản của phân số. a) Mẫu số nhân với $4$ ($5 \\times 4 = 20$) nên tử số cũng nhân '
                        'với $4$: $3 \\times 4 = 12$. Vậy điền số **$12$**. b) Tử số chia cho $12$ ($24 : 12 '
                        '= 2$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 55: Tính chất cơ bản của phân số** để giải quyết tình huống sau: '
                 'Tìm số thích hợp điền vào chỗ chấm: a) $\\dfrac{3}{5} = \\dfrac{\\dots}{20}$; b) '
                 '$\\dfrac{24}{36} = \\dfrac{2}{\\dots}$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['a) Mẫu số nhân với $4$ ($5 \\times 4 = 20$) nên tử số cũng nhân với $4$: $3 \\times '
                        '4 = 12$. Vậy điền số **$12$**. b) Tử số chia cho $12$ ($24 : 12 = 2$) nên...',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 55: Tính chất cơ bản của phân số: a) Mẫu số nhân với $4$ '
                        '($5 \\times 4 = 20$) nên tử số cũng nhân với $4$: $3 \\times 4 = 12$. Vậy điền số '
                        '**$12$**.\n'
                        'b) Tử số chia cho $12$ ($24 : 12 = 2$) nên mẫu số cũng chia cho $12$: $36 : 12 = '
                        '3$. Vậy điền số **$3$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số tự nhiên $x$ biết $\\dfrac{x}{8} = \\dfrac{15}{24}$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta thấy mẫu số $24 : 3 = 8$, nên tử số $x = 15 : 3 = 5$.\nĐáp số: **$5$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd10-phan-so',
  'context_title': 'Chủ đề 10: Phân số',
  'context': 'SGK Toán 4 · Chủ đề 10: Khái niệm phân số; tính chất cơ bản; rút gọn, quy đồng và so sánh phân '
             'số.',
  'title': 'Bài 56: Rút gọn phân số',
  'icon': '✂️',
  'description': 'Cách rút gọn một phân số về phân số tối giản dựa vào tính chất cơ bản của phân số.',
  'requirements': ['Nhận biết được thế nào là **phân số tối giản**.',
                   'Rút gọn được phân số về phân số tối giản bằng cách chia cả tử và mẫu cho ước chung lớn '
                   'hơn $1$.',
                   'Vận dụng rút gọn phân số trong kết quả tính toán và bài toán thực tế.'],
  'definition': '- **Phân số tối giản** là phân số có tử số và mẫu số không cùng chia hết cho số tự nhiên '
                'nào lớn hơn $1$ (ví dụ $\\dfrac{2}{3}, \\dfrac{3}{5}, \\dfrac{7}{8}$).\n'
                '- **Cách rút gọn phân số**: Chia cả tử số và mẫu số cho cùng một số tự nhiên lớn hơn $1$; '
                'cứ làm như thế cho đến khi nhận được **phân số tối giản**.',
  'theory': '### 1. Các bước rút gọn phân số\n'
            '- Ví dụ: Rút gọn $\\dfrac{18}{24}$.\n'
            '  - Cách làm từng bước: $\\dfrac{18}{24} = \\dfrac{18 : 2}{24 : 2} = \\dfrac{9}{12} = \\dfrac{9 '
            ': 3}{12 : 3} = \\dfrac{3}{4}$.\n'
            '  - Cách làm nhanh: Nhận thấy $18$ và $24$ cùng chia hết cho $6$ nên $\\dfrac{18}{24} = '
            '\\dfrac{18 : 6}{24 : 6} = \\dfrac{3}{4}$ ($\\dfrac{3}{4}$ là phân số tối giản).',
  'formulas': [{'category': 'I. Rút gọn phân số',
                'items': [{'name': 'Công thức',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{a : k}{b : k}$ ($k > 1$) cho đến khi tối '
                                      'giản'},
                          {'name': 'Dấu hiệu chia hết',
                           'formula': 'Tận cùng chẵn $\\rightarrow : 2$ · Tận cùng $0, 5 \\rightarrow : 5$ · '
                                      'Tổng chữ số chia hết cho $3, 9 \\rightarrow : 3, 9$'}]}],
  'example': 'Rút gọn các phân số $\\dfrac{15}{25}$ và $\\dfrac{36}{48}$ về phân số tối giản.',
  'example_answer': '- $\\dfrac{15}{25} = \\dfrac{15 : 5}{25 : 5} = \\dfrac{3}{5}$.\n'
                    '- $\\dfrac{36}{48} = \\dfrac{36 : 12}{48 : 12} = \\dfrac{3}{4}$.',
  'real_life': '- Viết tỉ lệ học sinh nam so với cả lớp dưới dạng phân số gọn nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Rút gọn phân số $\\dfrac{15}{25}$ ta được phân số tối giản là:',
            'options': ['$\\dfrac{5}{3}$', '$\\dfrac{15}{25}$', '$\\dfrac{1}{5}$', '$\\dfrac{3}{5}$'],
            'answer': 3,
            'solution': 'Chia cả tử số và mẫu số cho $5$: $\\dfrac{15 : 5}{25 : 5} = \\dfrac{3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số tối giản của phân số $\\dfrac{12}{18}$ là:',
            'options': ['$\\dfrac{2}{3}$', '$\\dfrac{6}{9}$', '$\\dfrac{4}{6}$', '$\\dfrac{3}{2}$'],
            'answer': 0,
            'solution': 'Chia cả tử và mẫu cho $6$: $\\dfrac{12 : 6}{18 : 6} = \\dfrac{2}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 56: Rút gọn phân số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Công thức**?',
            'options': ['Tận cùng chẵn $\\rightarrow : 2$ · Tận cùng $0, 5 \\rightarrow : 5$ · Tổng chữ số '
                        'chia hết cho $3, 9 \\rightarrow : 3, 9$',
                        '$\\dfrac{a}{b} = \\dfrac{a : k}{b : k}$ ($k > 1$) cho đến khi tối giản',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 56: Rút gọn phân số, **Công thức** được xác '
                        'định bởi: $\\dfrac{a}{b} = \\dfrac{a : k}{b : k}$ ($k > 1$) cho đến khi tối giản.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 56: Rút gọn phân số**, nội dung/biểu thức Tận cùng chẵn $\\rightarrow : 2$ · '
                 'Tận cùng $0, 5 \\rightarrow : 5$ · Tổng chữ số chia hết cho $3, 9 \\rightarrow : 3, 9$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Công thức', 'Phân tích số', 'Dấu hiệu chia hết', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 56: Rút gọn phân số, biểu thức/quy tắc Tận cùng chẵn $\\rightarrow : 2$ · '
                        'Tận cùng $0, 5 \\rightarrow : 5$ · Tổng chữ số chia hết cho $3, 9 \\rightarrow : 3, '
                        '9$ chính là nội dung của **Dấu hiệu chia hết**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các phân số $\\dfrac{4}{6}, \\dfrac{8}{9}, \\dfrac{10}{15}, \\dfrac{9}{12}$, phân số '
                 'nào là phân số tối giản?',
            'options': ['$\\dfrac{4}{6}$', '$\\dfrac{10}{15}$', '$\\dfrac{9}{12}$', '$\\dfrac{8}{9}$'],
            'answer': 3,
            'solution': 'Tử số $8$ và mẫu số $9$ không cùng chia hết cho số nào lớn hơn $1$ nên '
                        '**$\\dfrac{8}{9}$** là phân số tối giản.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 56: Rút gọn phân số** (Chủ đề 10: Phân số), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được thế nào là **phân số tối giản**.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 56: Rút gọn phân số: Nhận biết được thế nào là **phân '
                        'số tối giản**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Phân số $\\dfrac{6}{9}$ đã là phân số tối giản."',
            'answer': False,
            'solution': 'Cả $6$ và $9$ còn cùng chia hết cho $3$ ($\\dfrac{6}{9} = \\dfrac{2}{3}$) nên chưa '
                        'tối giản $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 56: Rút gọn phân số**, quy tắc **Công thức** được xác định bởi $\\dfrac{a}{b} '
                 '= \\dfrac{a : k}{b : k}$ ($k > 1$) cho đến khi tối giản và áp dụng trực tiếp vào bài toán: '
                 '“Rút gọn các phân số $\\dfrac{15}{25}$ và $\\dfrac{36}{48}$ về phân số tối giản.”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Công thức** ($\\dfrac{a}{b} = \\dfrac{a : k}{b : k}$ '
                        '($k > 1$) cho đến khi tối giản) là kiến thức cốt lõi của Bài 56: Rút gọn phân số. - '
                        '$\\dfrac{15}{25} = \\dfrac{15 : 5}{25 : 5} = \\dfrac{3}{5}$. - $\\dfrac{36}{48} = '
                        '\\dfrac{36 : 12}{48 : 12} = \\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 56: Rút gọn phân số** để giải quyết tình huống sau: Rút gọn các '
                 'phân số $\\dfrac{15}{25}$ và $\\dfrac{36}{48}$ về phân số tối giản. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        '- $\\dfrac{15}{25} = \\dfrac{15 : 5}{25 : 5} = \\dfrac{3}{5}$. - $\\dfrac{36}{48} = '
                        '\\dfrac{36 : 12}{48 : 12} = \\dfrac{3}{4}$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 56: Rút gọn phân số: - $\\dfrac{15}{25} = \\dfrac{15 : '
                        '5}{25 : 5} = \\dfrac{3}{5}$.\n'
                        '- $\\dfrac{36}{48} = \\dfrac{36 : 12}{48 : 12} = \\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một lớp học có $32$ học sinh, trong đó có $12$ học sinh nam. Phân số tối giản chỉ số phần '
                 'học sinh nam so với học sinh cả lớp là bao nhiêu (viết dạng a/b)?',
            'answer': ['3/8'],
            'unit': None,
            'solution': 'Ta có phân số $\\dfrac{12}{32} = \\dfrac{12 : 4}{32 : 4} = \\dfrac{3}{8}$.\n'
                        'Đáp số: **$3/8$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd10-phan-so',
  'context_title': 'Chủ đề 10: Phân số',
  'context': 'SGK Toán 4 · Chủ đề 10: Khái niệm phân số; tính chất cơ bản; rút gọn, quy đồng và so sánh phân '
             'số.',
  'title': 'Bài 57: Quy đồng mẫu số các phân số',
  'icon': '🔄',
  'description': 'Cách quy đồng mẫu số hai phân số trong trường hợp mẫu số này chia hết cho mẫu số kia.',
  'requirements': ['Hiểu quy đồng mẫu số là biến đổi các phân số về các phân số mới bằng chúng và có **cùng '
                   'mẫu số**.',
                   'Chọn được **mẫu số chung** khi một mẫu số chia hết cho các mẫu số còn lại.',
                   'Thực hiện đúng các bước quy đồng mẫu số của hai hoặc ba phân số.'],
  'definition': '- **Quy đồng mẫu số** hai phân số $\\dfrac{a}{b}$ và $\\dfrac{c}{d}$ là viết chúng thành '
                'hai phân số mới có **cùng mẫu số** (gọi là **mẫu số chung**).\n'
                '- Khi mẫu số $d$ chia hết cho mẫu số $b$ ($d = b \\times k$), ta lấy **mẫu số lớn $d$** làm '
                '**mẫu số chung**.',
  'theory': '### 1. Các bước quy đồng mẫu số hai phân số $\\dfrac{a}{b}$ và $\\dfrac{c}{d}$ (với $d$ chia '
            'hết cho $b$)\n'
            '- Bước 1: Chọn mẫu số chung là $d$. Tìm thừa số phụ $k = d : b$.\n'
            '- Bước 2: Nhân cả tử số và mẫu số của $\\dfrac{a}{b}$ với $k$: $\\dfrac{a}{b} = \\dfrac{a '
            '\\times k}{b \\times k} = \\dfrac{a \\times k}{d}$.\n'
            '- Bước 3: Giữ nguyên phân số $\\dfrac{c}{d}$.',
  'formulas': [{'category': 'I. Quy đồng mẫu số (d chia hết cho b)',
                'items': [{'name': 'Mẫu số chung', 'formula': '$\\text{MSC} = d$ · Thừa số phụ $k = d : b$'},
                          {'name': 'Biến đổi',
                           'formula': '$\\dfrac{a}{b} = \\dfrac{a \\times k}{d}$ và giữ nguyên '
                                      '$\\dfrac{c}{d}$'}]}],
  'example': 'Quy đồng mẫu số hai phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{12}$.',
  'example_answer': 'Vì $12 : 4 = 3$ nên chọn mẫu số chung là $12$.\n'
                    'Ta có: $\\dfrac{3}{4} = \\dfrac{3 \\times 3}{4 \\times 3} = \\dfrac{9}{12}$ và giữ '
                    'nguyên phân số $\\dfrac{5}{12}$.',
  'real_life': '- Đưa các phần bánh được chia khác nhau về cùng một cỡ miếng cắt để dễ so sánh và cộng trừ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi quy đồng mẫu số hai phân số $\\dfrac{2}{5}$ và $\\dfrac{7}{15}$, mẫu số chung nhỏ nhất '
                 'nên chọn là:',
            'options': ['$15$', '$5$', '$75$', '$20$'],
            'answer': 0,
            'solution': 'Vì $15$ chia hết cho $5$ ($15 : 5 = 3$) nên chọn mẫu số chung là **$15$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Quy đồng mẫu số hai phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{12}$ ta được:',
            'options': ['$\\dfrac{3}{12}$ và $\\dfrac{5}{12}$',
                        '$\\dfrac{9}{12}$ và $\\dfrac{5}{12}$',
                        '$\\dfrac{12}{16}$ và $\\dfrac{5}{12}$',
                        '$\\dfrac{9}{12}$ và $\\dfrac{15}{36}$'],
            'answer': 1,
            'solution': 'Nhân cả tử và mẫu của $\\dfrac{3}{4}$ với $3$ được **$\\dfrac{9}{12}$ và giữ nguyên '
                        '$\\dfrac{5}{12}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 57: Quy đồng mẫu số các phân số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Mẫu số chung**?',
            'options': ['$\\dfrac{a}{b} = \\dfrac{a \\times k}{d}$ và giữ nguyên $\\dfrac{c}{d}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$\\text{MSC} = d$ · Thừa số phụ $k = d : b$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 57: Quy đồng mẫu số các phân số, **Mẫu số '
                        'chung** được xác định bởi: $\\text{MSC} = d$ · Thừa số phụ $k = d : b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 57: Quy đồng mẫu số các phân số**, nội dung/biểu thức $\\dfrac{a}{b} = '
                 '\\dfrac{a \\times k}{d}$ và giữ nguyên $\\dfrac{c}{d}$ là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Mẫu số chung', 'Phân tích số', 'Quy tắc 5', 'Biến đổi'],
            'answer': 3,
            'solution': 'Trong Bài 57: Quy đồng mẫu số các phân số, biểu thức/quy tắc $\\dfrac{a}{b} = '
                        '\\dfrac{a \\times k}{d}$ và giữ nguyên $\\dfrac{c}{d}$ chính là nội dung của **Biến '
                        'đổi**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Quy đồng mẫu số ba phân số $\\dfrac{1}{2}, \\dfrac{2}{3}$ và $\\dfrac{5}{6}$ với mẫu số '
                 'chung là $6$, ta được:',
            'options': ['$\\dfrac{3}{6}, \\dfrac{4}{6}$ và $\\dfrac{5}{6}$',
                        '$\\dfrac{1}{6}, \\dfrac{2}{6}$ và $\\dfrac{5}{6}$',
                        '$\\dfrac{2}{6}, \\dfrac{4}{6}$ và $\\dfrac{5}{6}$',
                        '$\\dfrac{3}{6}, \\dfrac{2}{6}$ và $\\dfrac{5}{6}$'],
            'answer': 0,
            'solution': 'Ta có $\\dfrac{1}{2} = \\dfrac{3}{6}$; $\\dfrac{2}{3} = \\dfrac{4}{6}$ và giữ '
                        'nguyên $\\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 57: Quy đồng mẫu số các phân số** (Chủ đề 10: Phân số), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Hiểu quy đồng mẫu số là biến đổi các phân số về các phân số mới bằng chúng và có '
                        '**cùng mẫu số**.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 57: Quy đồng mẫu số các phân số: Hiểu quy đồng mẫu số '
                        'là biến đổi các phân số về các phân số mới bằng chúng và có **cùng mẫu số**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Khi quy đồng mẫu số hai phân số $\\dfrac{2}{7}$ và $\\dfrac{9}{14}$ với mẫu số '
                 'chung là $14$, phân số $\\dfrac{2}{7}$ trở thành $\\dfrac{4}{14}$."',
            'answer': True,
            'solution': 'Vì $14 : 7 = 2$ nên $\\dfrac{2}{7} = \\dfrac{2 \\times 2}{7 \\times 2} = '
                        '\\dfrac{4}{14}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 57: Quy đồng mẫu số các phân số**, quy tắc **Mẫu số chung** được xác định bởi '
                 '$\\text{MSC} = d$ · Thừa số phụ $k = d : b$ và áp dụng trực tiếp vào bài toán: “Quy đồng '
                 'mẫu số hai phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{12}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Mẫu số chung** ($\\text{MSC} = d$ · Thừa số phụ $k = '
                        'd : b$) là kiến thức cốt lõi của Bài 57: Quy đồng mẫu số các phân số. Vì $12 : 4 = '
                        '3$ nên chọn mẫu số chung là $12$. Ta có: $\\dfrac{3}{4} = \\dfrac{3 \\times 3}{4 '
                        '\\times 3} = \\dfrac{9}{12}$ và giữ nguyên phân số...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 57: Quy đồng mẫu số các phân số** để giải quyết tình huống sau: '
                 'Quy đồng mẫu số hai phân số $\\dfrac{3}{4}$ và $\\dfrac{5}{12}$. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Vì $12 : 4 = 3$ nên chọn mẫu số chung là $12$. Ta có: $\\dfrac{3}{4} = \\dfrac{3 '
                        '\\times 3}{4 \\times 3} = \\dfrac{9}{12}$ và giữ nguyên phân số $\\dfrac{5}{12}$...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 57: Quy đồng mẫu số các phân số: Vì $12 : 4 = 3$ nên '
                        'chọn mẫu số chung là $12$.\n'
                        'Ta có: $\\dfrac{3}{4} = \\dfrac{3 \\times 3}{4 \\times 3} = \\dfrac{9}{12}$ và giữ '
                        'nguyên phân số $\\dfrac{5}{12}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Khi quy đồng mẫu số hai phân số $\\dfrac{5}{8}$ và $\\dfrac{19}{24}$ với mẫu số chung là '
                 '$24$, tử số mới của phân số $\\dfrac{5}{8}$ là bao nhiêu?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Thừa số phụ là $24 : 8 = 3$. Tử số mới là: $5 \\times 3 = 15$.\nĐáp số: **$15$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd10-phan-so',
  'context_title': 'Chủ đề 10: Phân số',
  'context': 'SGK Toán 4 · Chủ đề 10: Khái niệm phân số; tính chất cơ bản; rút gọn, quy đồng và so sánh phân '
             'số.',
  'title': 'Bài 58, 59: So sánh phân số và luyện tập chung',
  'icon': '⚖️',
  'description': 'Quy tắc so sánh hai phân số cùng mẫu số, cùng tử số hoặc khác mẫu số; sắp xếp các phân số.',
  'requirements': ['So sánh được hai phân số có **cùng mẫu số** (tử số lớn hơn thì lớn hơn).',
                   'So sánh được hai phân số có **cùng tử số** (mẫu số bé hơn thì lớn hơn).',
                   'So sánh được hai phân số **khác mẫu số** bằng cách quy đồng mẫu số rồi so sánh.'],
  'definition': '- **Cùng mẫu số**: Trong hai phân số có cùng mẫu số, phân số nào có **tử số lớn hơn** thì '
                '**lớn hơn**.\n'
                '- **Cùng tử số**: Trong hai phân số (khác $0$) có cùng tử số, phân số nào có **mẫu số bé '
                'hơn** thì **lớn hơn**.\n'
                '- **Khác mẫu số**: Muốn so sánh hai phân số khác mẫu số, ta **quy đồng mẫu số** hai phân số '
                'đó rồi so sánh hai phân số cùng mẫu.',
  'theory': '### 1. Ví dụ các trường hợp so sánh\n'
            '- Cùng mẫu số: $\\dfrac{3}{7} < \\dfrac{5}{7}$ (vì $3 < 5$).\n'
            '- Cùng tử số: $\\dfrac{2}{5} > \\dfrac{2}{9}$ (vì cùng tử số $2$, mẫu số $5 < 9$).\n'
            '- Khác mẫu số: So sánh $\\dfrac{3}{4}$ và $\\dfrac{5}{8}$. Quy đồng $\\dfrac{3}{4} = '
            '\\dfrac{6}{8}$; vì $\\dfrac{6}{8} > \\dfrac{5}{8}$ nên $\\dfrac{3}{4} > \\dfrac{5}{8}$.\n'
            '### 2. So sánh qua số trung gian $1$\n'
            '- Nếu $\\dfrac{a}{b} < 1$ và $\\dfrac{c}{d} > 1$ thì $\\dfrac{a}{b} < \\dfrac{c}{d}$ (ví dụ '
            '$\\dfrac{7}{8} < 1 < \\dfrac{9}{5}$).',
  'formulas': [{'category': 'I. Ba quy tắc so sánh phân số',
                'items': [{'name': 'Cùng mẫu số',
                           'formula': '$a > b \\Leftrightarrow \\dfrac{a}{m} > \\dfrac{b}{m}$'},
                          {'name': 'Cùng tử số (a > 0)',
                           'formula': '$m < n \\Leftrightarrow \\dfrac{a}{m} > \\dfrac{a}{n}$'},
                          {'name': 'Khác mẫu số',
                           'formula': 'Quy đồng mẫu số $\\rightarrow$ So sánh tử số'}]}],
  'example': 'Sắp xếp các phân số $\\dfrac{5}{6}, \\dfrac{2}{3}, \\dfrac{3}{4}$ theo thứ tự từ bé đến lớn.',
  'example_answer': 'Quy đồng mẫu số với mẫu số chung là $12$: $\\dfrac{5}{6} = \\dfrac{10}{12}$; '
                    '$\\dfrac{2}{3} = \\dfrac{8}{12}$; $\\dfrac{3}{4} = \\dfrac{9}{12}$.\n'
                    'Vì $\\dfrac{8}{12} < \\dfrac{9}{12} < \\dfrac{10}{12}$ nên thứ tự từ bé đến lớn là: '
                    '**$\\dfrac{2}{3}; \\dfrac{3}{4}; \\dfrac{5}{6}$**.',
  'real_life': '- So sánh xem ai ăn nhiều bánh hơn hoặc ai đã hoàn thành phần công việc nhiều hơn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hai phân số $\\dfrac{5}{9}$ và $\\dfrac{7}{9}$, phân số nào lớn hơn?',
            'options': ['$\\dfrac{5}{9}$', '$\\dfrac{7}{9}$', 'Hai phân số bằng nhau', 'Không so sánh được'],
            'answer': 1,
            'solution': 'Hai phân số cùng mẫu số $9$, vì $7 > 5$ nên **$\\dfrac{7}{9} > \\dfrac{5}{9}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Sắp xếp các phân số $\\dfrac{5}{6}, \\dfrac{2}{3}, \\dfrac{3}{4}$ theo thứ tự từ bé đến '
                 'lớn ta được:',
            'options': ['$\\dfrac{5}{6}, \\dfrac{3}{4}, \\dfrac{2}{3}$',
                        '$\\dfrac{3}{4}, \\dfrac{2}{3}, \\dfrac{5}{6}$',
                        '$\\dfrac{2}{3}, \\dfrac{3}{4}, \\dfrac{5}{6}$',
                        '$\\dfrac{2}{3}, \\dfrac{5}{6}, \\dfrac{3}{4}$'],
            'answer': 2,
            'solution': 'Quy đồng mẫu $12$: $\\dfrac{2}{3}=\\dfrac{8}{12}, \\dfrac{3}{4}=\\dfrac{9}{12}, '
                        '\\dfrac{5}{6}=\\dfrac{10}{12} \\rightarrow \\dfrac{2}{3}, \\dfrac{3}{4}, '
                        '\\dfrac{5}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 58, 59: So sánh phân số và luyện tập chung**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Cùng mẫu số**?',
            'options': ['$m < n \\Leftrightarrow \\dfrac{a}{m} > \\dfrac{a}{n}$',
                        'Quy đồng mẫu số $\\rightarrow$ So sánh tử số',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$a > b \\Leftrightarrow \\dfrac{a}{m} > \\dfrac{b}{m}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 58, 59: So sánh phân số và luyện tập chung, '
                        '**Cùng mẫu số** được xác định bởi: $a > b \\Leftrightarrow \\dfrac{a}{m} > '
                        '\\dfrac{b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 58, 59: So sánh phân số và luyện tập chung**, nội dung/biểu thức $m < n '
                 '\\Leftrightarrow \\dfrac{a}{m} > \\dfrac{a}{n}$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Cùng tử số (a > 0)', 'Cùng mẫu số', 'Khác mẫu số', 'Phân tích số'],
            'answer': 0,
            'solution': 'Trong Bài 58, 59: So sánh phân số và luyện tập chung, biểu thức/quy tắc $m < n '
                        '\\Leftrightarrow \\dfrac{a}{m} > \\dfrac{a}{n}$ chính là nội dung của **Cùng tử số '
                        '(a > 0)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Lan ăn $\\dfrac{3}{8}$ cái bánh, Mai ăn $\\dfrac{1}{2}$ cái bánh đó. Hỏi ai ăn nhiều bánh '
                 'hơn?',
            'options': ['Lan ăn nhiều hơn',
                        'Mai ăn nhiều hơn',
                        'Hai bạn ăn bằng nhau',
                        'Không xác định được'],
            'answer': 1,
            'solution': 'Quy đồng: $\\dfrac{1}{2} = \\dfrac{4}{8} > \\dfrac{3}{8}$ nên **Mai ăn nhiều hơn**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 58, 59: So sánh phân số và luyện tập chung** (Chủ đề 10: Phân số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh được hai phân số có **cùng mẫu số** (tử số lớn hơn thì lớn hơn).',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 58, 59: So sánh phân số và luyện tập chung: So sánh '
                        'được hai phân số có **cùng mẫu số** (tử số lớn hơn thì lớn hơn).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{2}{5} > \\dfrac{2}{7}$."',
            'answer': True,
            'solution': 'Hai phân số có cùng tử số là $2$, mẫu số $5 < 7$ nên $\\dfrac{2}{5} > '
                        '\\dfrac{2}{7}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 58, 59: So sánh phân số và luyện tập chung**, quy tắc **Cùng mẫu số** được xác '
                 'định bởi $a > b \\Leftrightarrow \\dfrac{a}{m} > \\dfrac{b}{m}$ và áp dụng trực tiếp vào '
                 'bài toán: “Sắp xếp các phân số $\\dfrac{5}{6}, \\dfrac{2}{3}, \\dfrac{3}{4}$ theo thứ tự '
                 'từ bé đến lớn.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cùng mẫu số** ($a > b \\Leftrightarrow \\dfrac{a}{m} '
                        '> \\dfrac{b}{m}$) là kiến thức cốt lõi của Bài 58, 59: So sánh phân số và luyện tập '
                        'chung. Quy đồng mẫu số với mẫu số chung là $12$: $\\dfrac{5}{6} = \\dfrac{10}{12}$; '
                        '$\\dfrac{2}{3} = \\dfrac{8}{12}$; $\\dfrac{3}{4} = \\dfrac{9}{12}$. V...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 58, 59: So sánh phân số và luyện tập chung** để giải quyết tình '
                 'huống sau: Sắp xếp các phân số $\\dfrac{5}{6}, \\dfrac{2}{3}, \\dfrac{3}{4}$ theo thứ tự '
                 'từ bé đến lớn. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Quy đồng mẫu số với mẫu số chung là $12$: $\\dfrac{5}{6} = \\dfrac{10}{12}$; '
                        '$\\dfrac{2}{3} = \\dfrac{8}{12}$; $\\dfrac{3}{4} = \\dfrac{9}{12}$. Vì '
                        '$\\dfrac{8}{12} < \\dfrac{9}{12} < \\dfrac{10}{12}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 58, 59: So sánh phân số và luyện tập chung: Quy đồng mẫu '
                        'số với mẫu số chung là $12$: $\\dfrac{5}{6} = \\dfrac{10}{12}$; $\\dfrac{2}{3} = '
                        '\\dfrac{8}{12}$; $\\dfrac{3}{4} = \\dfrac{9}{12}$.\n'
                        'Vì $\\dfrac{8}{12} < \\dfrac{9}{12} < \\dfrac{10}{12}$ nên thứ tự từ bé đến lớn là: '
                        '**$\\dfrac{2}{3}; \\dfrac{3}{4}; \\dfrac{5}{6}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong các phân số $\\dfrac{3}{10}, \\dfrac{4}{5}, \\dfrac{7}{10}, \\dfrac{1}{2}$, phân số '
                 'lớn nhất là phân số nào (viết dạng a/b)?',
            'answer': ['4/5'],
            'unit': None,
            'solution': 'Quy đồng mẫu $10$: $\\dfrac{4}{5} = \\dfrac{8}{10}$ lớn hơn $\\dfrac{7}{10}, '
                        '\\dfrac{5}{10}, \\dfrac{3}{10}$ nên phân số lớn nhất là **$4/5$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd11-cong-tru-phan-so',
  'context_title': 'Chủ đề 11: Phép cộng, phép trừ phân số',
  'context': 'SGK Toán 4 · Chủ đề 11: Phép cộng và phép trừ phân số (cùng mẫu số và khác mẫu số).',
  'title': 'Bài 60: Phép cộng phân số',
  'icon': '➕',
  'description': 'Quy tắc cộng hai phân số cùng mẫu số và cộng hai phân số khác mẫu số; tính chất của phép '
                 'cộng phân số.',
  'requirements': ['Thực hiện được phép cộng hai phân số **cùng mẫu số** (cộng tử số, giữ nguyên mẫu số).',
                   'Thực hiện được phép cộng hai phân số **khác mẫu số** (quy đồng mẫu số rồi cộng).',
                   'Vận dụng tính chất giao hoán, kết hợp của phép cộng phân số để tính thuận tiện.'],
  'definition': '- **Cộng hai phân số cùng mẫu số**: Muốn cộng hai phân số cùng mẫu số, ta **cộng hai tử số '
                'với nhau** và **giữ nguyên mẫu số**: $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$.\n'
                '- **Cộng hai phân số khác mẫu số**: Muốn cộng hai phân số khác mẫu số, ta **quy đồng mẫu '
                'số** hai phân số đó, rồi cộng hai phân số cùng mẫu.',
  'theory': '### 1. Ví dụ cộng cùng mẫu và khác mẫu\n'
            '- Cùng mẫu số: $\\dfrac{3}{8} + \\dfrac{4}{8} = \\dfrac{3 + 4}{8} = \\dfrac{7}{8}$ (tuyệt đối '
            'không cộng mẫu số với mẫu số!).\n'
            '- Khác mẫu số: $\\dfrac{1}{4} + \\dfrac{3}{8} = \\dfrac{2}{8} + \\dfrac{3}{8} = '
            '\\dfrac{5}{8}$.\n'
            '### 2. Cộng số tự nhiên với phân số\n'
            '- Viết số tự nhiên thành phân số có cùng mẫu số với phân số kia: $2 + \\dfrac{1}{3} = '
            '\\dfrac{6}{3} + \\dfrac{1}{3} = \\dfrac{7}{3}$.',
  'formulas': [{'category': 'I. Phép cộng phân số',
                'items': [{'name': 'Cùng mẫu số',
                           'formula': '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$'},
                          {'name': 'Khác mẫu số',
                           'formula': 'Quy đồng mẫu số $\\rightarrow$ Cộng hai tử số $\\rightarrow$ Rút gọn '
                                      '(nếu có)'}]}],
  'example': 'Một vòi nước giờ thứ nhất chảy được $\\dfrac{2}{9}$ bể, giờ thứ hai chảy được $\\dfrac{1}{3}$ '
             'bể. Hỏi sau hai giờ vòi nước đó chảy được bao nhiêu phần của bể?',
  'example_answer': 'Quy đồng: $\\dfrac{1}{3} = \\dfrac{3}{9}$.\n'
                    'Sau hai giờ vòi chảy được số phần bể là: $\\dfrac{2}{9} + \\dfrac{3}{9} = '
                    '\\dfrac{5}{9}\\text{ (bể)}$.',
  'real_life': '- Tính tổng số phần công việc làm được trong hai ngày hoặc tổng lượng nước chảy vào bể.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $\\dfrac{3}{8} + \\dfrac{4}{8}$ là:',
            'options': ['$\\dfrac{7}{16}$', '$\\dfrac{1}{8}$', '$\\dfrac{7}{8}$', '$\\dfrac{12}{8}$'],
            'answer': 2,
            'solution': 'Cộng hai tử số và giữ nguyên mẫu số: $\\dfrac{3 + 4}{8} = \\dfrac{7}{8}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn cộng hai phân số khác mẫu số, bước đầu tiên ta cần làm là:',
            'options': ['Cộng tử với tử, mẫu với mẫu',
                        'Nhân hai phân số',
                        'Giữ nguyên mẫu số lớn',
                        'Quy đồng mẫu số hai phân số'],
            'answer': 3,
            'solution': 'Trước hết ta phải **quy đồng mẫu số** hai phân số.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 60: Phép cộng phân số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Cùng mẫu số**?',
            'options': ['$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$',
                        'Quy đồng mẫu số $\\rightarrow$ Cộng hai tử số $\\rightarrow$ Rút gọn (nếu có)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 60: Phép cộng phân số, **Cùng mẫu số** được '
                        'xác định bởi: $\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 60: Phép cộng phân số**, nội dung/biểu thức Quy đồng mẫu số $\\rightarrow$ '
                 'Cộng hai tử số $\\rightarrow$ Rút gọn (nếu có) là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Cùng mẫu số', 'Khác mẫu số', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 60: Phép cộng phân số, biểu thức/quy tắc Quy đồng mẫu số $\\rightarrow$ '
                        'Cộng hai tử số $\\rightarrow$ Rút gọn (nếu có) chính là nội dung của **Khác mẫu '
                        'số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $\\dfrac{1}{2} + \\dfrac{1}{4}$ là:',
            'options': ['$\\dfrac{2}{6}$', '$\\dfrac{1}{6}$', '$\\dfrac{3}{4}$', '$\\dfrac{2}{4}$'],
            'answer': 2,
            'solution': 'Quy đồng $\\dfrac{1}{2} = \\dfrac{2}{4}$, sau đó $\\dfrac{2}{4} + \\dfrac{1}{4} = '
                        '\\dfrac{3}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 60: Phép cộng phân số** (Chủ đề 11: Phép cộng, phép trừ phân số), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Thực hiện được phép cộng hai phân số **cùng mẫu số** (cộng tử số, giữ nguyên mẫu '
                        'số).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 60: Phép cộng phân số: Thực hiện được phép cộng hai '
                        'phân số **cùng mẫu số** (cộng tử số, giữ nguyên mẫu số).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{2}{3} + \\dfrac{1}{6} = \\dfrac{3}{9}$."',
            'answer': False,
            'solution': 'Quy đồng: $\\dfrac{4}{6} + \\dfrac{1}{6} = \\dfrac{5}{6}$ (cộng cả tử lẫn mẫu ra '
                        '$\\dfrac{3}{9}$ là sai quy tắc) $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 60: Phép cộng phân số**, quy tắc **Cùng mẫu số** được xác định bởi '
                 '$\\dfrac{a}{m} + \\dfrac{b}{m} = \\dfrac{a + b}{m}$ và áp dụng trực tiếp vào bài toán: '
                 '“Một vòi nước giờ thứ nhất chảy được $\\dfrac{2}{9}$ bể, giờ thứ hai chảy được '
                 '$\\dfrac{1}{3}$ bể. Hỏi sau hai giờ vòi nước đó chảy được bao nh...”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cùng mẫu số** ($\\dfrac{a}{m} + \\dfrac{b}{m} = '
                        '\\dfrac{a + b}{m}$) là kiến thức cốt lõi của Bài 60: Phép cộng phân số. Quy đồng: '
                        '$\\dfrac{1}{3} = \\dfrac{3}{9}$. Sau hai giờ vòi chảy được số phần bể là: '
                        '$\\dfrac{2}{9} + \\dfrac{3}{9} = \\dfrac{5}{9}\\text{ (bể)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 60: Phép cộng phân số** để giải quyết tình huống sau: Một vòi '
                 'nước giờ thứ nhất chảy được $\\dfrac{2}{9}$ bể, giờ thứ hai chảy được $\\dfrac{1}{3}$ bể. '
                 'Hỏi sau hai giờ vòi nước đó chảy được bao nhiêu phần của bể? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Quy đồng: $\\dfrac{1}{3} = \\dfrac{3}{9}$. Sau hai giờ vòi chảy được số phần bể là: '
                        '$\\dfrac{2}{9} + \\dfrac{3}{9} = \\dfrac{5}{9}\\text{ (bể)}$.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 60: Phép cộng phân số: Quy đồng: $\\dfrac{1}{3} = '
                        '\\dfrac{3}{9}$.\n'
                        'Sau hai giờ vòi chảy được số phần bể là: $\\dfrac{2}{9} + \\dfrac{3}{9} = '
                        '\\dfrac{5}{9}\\text{ (bể)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính bằng cách thuận tiện: $\\dfrac{3}{7} + \\dfrac{5}{9} + \\dfrac{4}{7} + \\dfrac{4}{9} '
                 '= ?$ (viết kết quả là số tự nhiên).',
            'answer': ['2'],
            'unit': None,
            'solution': 'Nhóm các phân số cùng mẫu số: $\\left(\\dfrac{3}{7} + \\dfrac{4}{7}\\right) + '
                        '\\left(\\dfrac{5}{9} + \\dfrac{4}{9}\\right) = \\dfrac{7}{7} + \\dfrac{9}{9} = 1 + '
                        '1 = 2$.\n'
                        'Đáp số: **$2$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd11-cong-tru-phan-so',
  'context_title': 'Chủ đề 11: Phép cộng, phép trừ phân số',
  'context': 'SGK Toán 4 · Chủ đề 11: Phép cộng và phép trừ phân số (cùng mẫu số và khác mẫu số).',
  'title': 'Bài 61: Phép trừ phân số',
  'icon': '➖',
  'description': 'Quy tắc trừ hai phân số cùng mẫu số, trừ hai phân số khác mẫu số và trừ số tự nhiên với '
                 'phân số.',
  'requirements': ['Thực hiện được phép trừ hai phân số **cùng mẫu số** (trừ tử số, giữ nguyên mẫu số).',
                   'Thực hiện được phép trừ hai phân số **khác mẫu số** (quy đồng mẫu số rồi trừ).',
                   'Thực hiện được phép trừ một số tự nhiên và một phân số.'],
  'definition': '- **Trừ hai phân số cùng mẫu số**: Muốn trừ hai phân số cùng mẫu số, ta **lấy tử số của '
                'phân số thứ nhất trừ đi tử số của phân số thứ hai** và **giữ nguyên mẫu số**: '
                '$\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a - b}{m}$.\n'
                '- **Trừ hai phân số khác mẫu số**: Ta **quy đồng mẫu số** hai phân số đó, rồi trừ hai phân '
                'số cùng mẫu.',
  'theory': '### 1. Ví dụ trừ phân số cùng mẫu và khác mẫu\n'
            '- Cùng mẫu số: $\\dfrac{7}{9} - \\dfrac{2}{9} = \\dfrac{7 - 2}{9} = \\dfrac{5}{9}$.\n'
            '- Khác mẫu số (kết hợp rút gọn): $\\dfrac{5}{6} - \\dfrac{1}{3} = \\dfrac{5}{6} - \\dfrac{2}{6} '
            '= \\dfrac{3}{6} = \\dfrac{1}{2}$.\n'
            '### 2. Trừ số tự nhiên cho phân số\n'
            '- Ví dụ: $1 - \\dfrac{3}{5} = \\dfrac{5}{5} - \\dfrac{3}{5} = \\dfrac{2}{5}$; $2 - '
            '\\dfrac{3}{4} = \\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$.',
  'formulas': [{'category': 'I. Phép trừ phân số',
                'items': [{'name': 'Cùng mẫu số',
                           'formula': '$\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a - b}{m}$'},
                          {'name': 'Số tự nhiên trừ phân số',
                           'formula': '$1 - \\dfrac{a}{b} = \\dfrac{b - a}{b}$ · $n - \\dfrac{a}{b} = '
                                      '\\dfrac{n \\times b - a}{b}$'}]}],
  'example': 'Tính: a) $\\dfrac{7}{8} - \\dfrac{1}{4}$; b) $2 - \\dfrac{3}{4}$.',
  'example_answer': 'a) $\\dfrac{7}{8} - \\dfrac{1}{4} = \\dfrac{7}{8} - \\dfrac{2}{8} = \\dfrac{5}{8}$.\n'
                    'b) $2 - \\dfrac{3}{4} = \\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$.',
  'real_life': '- Tính phần bánh, phần vải hoặc phần quãng đường còn lại sau khi đã dùng một phần.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép trừ $\\dfrac{7}{9} - \\dfrac{2}{9}$ là:',
            'options': ['$\\dfrac{5}{0}$', '$\\dfrac{9}{9}$', '$\\dfrac{5}{18}$', '$\\dfrac{5}{9}$'],
            'answer': 3,
            'solution': 'Trừ hai tử số và giữ nguyên mẫu số: $\\dfrac{7 - 2}{9} = \\dfrac{5}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả rút gọn tối giản của phép tính $\\dfrac{5}{6} - \\dfrac{1}{3}$ là:',
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{4}{3}$', '$\\dfrac{4}{6}$', '$\\dfrac{1}{3}$'],
            'answer': 0,
            'solution': 'Quy đồng: $\\dfrac{5}{6} - \\dfrac{2}{6} = \\dfrac{3}{6} = \\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 61: Phép trừ phân số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Cùng mẫu số**?',
            'options': ['$1 - \\dfrac{a}{b} = \\dfrac{b - a}{b}$ · $n - \\dfrac{a}{b} = \\dfrac{n \\times b '
                        '- a}{b}$',
                        '$\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a - b}{m}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 61: Phép trừ phân số, **Cùng mẫu số** được '
                        'xác định bởi: $\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a - b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 61: Phép trừ phân số**, nội dung/biểu thức $1 - \\dfrac{a}{b} = \\dfrac{b - '
                 'a}{b}$ · $n - \\dfrac{a}{b} = \\dfrac{n \\times b - a}{b}$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Cùng mẫu số', 'Phân tích số', 'Số tự nhiên trừ phân số', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 61: Phép trừ phân số, biểu thức/quy tắc $1 - \\dfrac{a}{b} = \\dfrac{b - '
                        'a}{b}$ · $n - \\dfrac{a}{b} = \\dfrac{n \\times b - a}{b}$ chính là nội dung của '
                        '**Số tự nhiên trừ phân số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x + \\dfrac{2}{5} = \\dfrac{9}{10}$:',
            'options': ['$\\dfrac{7}{5}$', '$\\dfrac{11}{10}$', '$\\dfrac{7}{10}$', '$\\dfrac{1}{2}$'],
            'answer': 3,
            'solution': 'Ta có $x = \\dfrac{9}{10} - \\dfrac{2}{5} = \\dfrac{9}{10} - \\dfrac{4}{10} = '
                        '\\dfrac{5}{10} = \\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 61: Phép trừ phân số** (Chủ đề 11: Phép cộng, phép trừ phân số), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thực hiện được phép trừ hai phân số **cùng mẫu số** (trừ tử số, giữ nguyên mẫu số).',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 61: Phép trừ phân số: Thực hiện được phép trừ hai phân '
                        'số **cùng mẫu số** (trừ tử số, giữ nguyên mẫu số).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$2 - \\dfrac{3}{4} = \\dfrac{5}{4}$."',
            'answer': True,
            'solution': 'Đổi $2 = \\dfrac{8}{4}$, ta có $\\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$ '
                        '$\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 61: Phép trừ phân số**, quy tắc **Cùng mẫu số** được xác định bởi '
                 '$\\dfrac{a}{m} - \\dfrac{b}{m} = \\dfrac{a - b}{m}$ và áp dụng trực tiếp vào bài toán: '
                 '“Tính: a) $\\dfrac{7}{8} - \\dfrac{1}{4}$; b) $2 - \\dfrac{3}{4}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cùng mẫu số** ($\\dfrac{a}{m} - \\dfrac{b}{m} = '
                        '\\dfrac{a - b}{m}$) là kiến thức cốt lõi của Bài 61: Phép trừ phân số. a) '
                        '$\\dfrac{7}{8} - \\dfrac{1}{4} = \\dfrac{7}{8} - \\dfrac{2}{8} = \\dfrac{5}{8}$. b) '
                        '$2 - \\dfrac{3}{4} = \\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 61: Phép trừ phân số** để giải quyết tình huống sau: Tính: a) '
                 '$\\dfrac{7}{8} - \\dfrac{1}{4}$; b) $2 - \\dfrac{3}{4}$. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'a) $\\dfrac{7}{8} - \\dfrac{1}{4} = \\dfrac{7}{8} - \\dfrac{2}{8} = \\dfrac{5}{8}$. '
                        'b) $2 - \\dfrac{3}{4} = \\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 61: Phép trừ phân số: a) $\\dfrac{7}{8} - \\dfrac{1}{4} '
                        '= \\dfrac{7}{8} - \\dfrac{2}{8} = \\dfrac{5}{8}$.\n'
                        'b) $2 - \\dfrac{3}{4} = \\dfrac{8}{4} - \\dfrac{3}{4} = \\dfrac{5}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bình nước đang có $\\dfrac{7}{8}\\text{ l}$ nước, bạn An rót ra $\\dfrac{1}{2}\\text{ '
                 'l}$ nước để tưới cây. Hỏi trong bình còn lại mấy phần lít nước (viết dạng a/b)?',
            'answer': ['3/8'],
            'unit': 'l',
            'solution': 'Lượng nước còn lại là: $\\dfrac{7}{8} - \\dfrac{1}{2} = \\dfrac{7}{8} - '
                        '\\dfrac{4}{8} = \\dfrac{3}{8}\\text{ (l)}$.\n'
                        'Đáp số: **$3/8$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd11-cong-tru-phan-so',
  'context_title': 'Chủ đề 11: Phép cộng, phép trừ phân số',
  'context': 'SGK Toán 4 · Chủ đề 11: Phép cộng và phép trừ phân số (cùng mẫu số và khác mẫu số).',
  'title': 'Bài 62: Luyện tập chung cộng, trừ phân số',
  'icon': '🧮',
  'description': 'Vận dụng phối hợp phép cộng và phép trừ phân số để tính giá trị biểu thức và giải toán hai '
                 'bước tính.',
  'requirements': ['Tính đúng giá trị biểu thức có cả phép cộng và phép trừ phân số.',
                   'Tìm thành phần chưa biết trong phép cộng, phép trừ phân số.',
                   'Giải được bài toán tìm phần còn lại của một đơn vị ($1 - \\text{tổng đã dùng}$).'],
  'definition': '- Trong bài toán tìm **phần còn lại** của cả một tấm vải, cả một bể nước hay cả một quãng '
                'đường, ta coi toàn bộ ban đầu là **$1$ đơn vị**.\n'
                '- Công thức: $\\text{Phần còn lại} = 1 - (\\text{Phần thứ nhất} + \\text{Phần thứ hai})$.',
  'theory': '### 1. Bài toán tìm phần còn lại sau hai lần sử dụng\n'
            '- Ví dụ: Một tấm vải ngày đầu bán $\\dfrac{2}{5}$ tấm, ngày thứ hai bán $\\dfrac{3}{10}$ tấm. '
            'Tìm phần tấm vải còn lại.\n'
            '  - Bước 1: Cả hai ngày bán được: $\\dfrac{2}{5} + \\dfrac{3}{10} = \\dfrac{4}{10} + '
            '\\dfrac{3}{10} = \\dfrac{7}{10}$ (tấm vải).\n'
            '  - Bước 2: Phần tấm vải còn lại: $1 - \\dfrac{7}{10} = \\dfrac{10}{10} - \\dfrac{7}{10} = '
            '\\dfrac{3}{10}$ (tấm vải).',
  'formulas': [{'category': 'I. Bài toán phần còn lại',
                'items': [{'name': 'Tổng phần đã dùng', 'formula': '$S = \\dfrac{a}{b} + \\dfrac{c}{d}$'},
                          {'name': 'Phần còn lại', 'formula': '$1 - S$'}]}],
  'example': 'Một tấm vải, ngày đầu bán được $\\dfrac{2}{5}$ tấm, ngày hôm sau bán được $\\dfrac{3}{10}$ '
             'tấm. Hỏi còn lại bao nhiêu phần của tấm vải?',
  'example_answer': 'Số phần tấm vải đã bán trong hai ngày là: $\\dfrac{2}{5} + \\dfrac{3}{10} = '
                    '\\dfrac{4}{10} + \\dfrac{3}{10} = \\dfrac{7}{10}$ (tấm).\n'
                    'Số phần tấm vải còn lại là: $1 - \\dfrac{7}{10} = \\dfrac{3}{10}$ (tấm).',
  'real_life': '- Tính phần diện tích vườn còn lại để trồng hoa sau khi đã trồng rau và cây ăn quả.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $1 - \\dfrac{4}{9}$ là:',
            'options': ['$\\dfrac{5}{9}$', '$\\dfrac{3}{9}$', '$\\dfrac{4}{8}$', '$\\dfrac{9}{5}$'],
            'answer': 0,
            'solution': 'Ta có $1 - \\dfrac{4}{9} = \\dfrac{9}{9} - \\dfrac{4}{9} = \\dfrac{5}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\dfrac{2}{7} + \\dfrac{4}{7} - \\dfrac{1}{7}$ là:',
            'options': ['$\\dfrac{6}{7}$', '$\\dfrac{5}{7}$', '$\\dfrac{7}{7}$', '$\\dfrac{5}{21}$'],
            'answer': 1,
            'solution': 'Cùng mẫu số $7$: $\\dfrac{2 + 4 - 1}{7} = \\dfrac{5}{7}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 62: Luyện tập chung cộng, trừ phân số**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Tổng phần đã dùng**?',
            'options': ['$1 - S$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$S = \\dfrac{a}{b} + \\dfrac{c}{d}$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 62: Luyện tập chung cộng, trừ phân số, **Tổng '
                        'phần đã dùng** được xác định bởi: $S = \\dfrac{a}{b} + \\dfrac{c}{d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 62: Luyện tập chung cộng, trừ phân số**, nội dung/biểu thức $1 - S$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Tổng phần đã dùng', 'Phân tích số', 'Quy tắc 5', 'Phần còn lại'],
            'answer': 3,
            'solution': 'Trong Bài 62: Luyện tập chung cộng, trừ phân số, biểu thức/quy tắc $1 - S$ chính là '
                        'nội dung của **Phần còn lại**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một tấm vải ngày đầu bán $\\dfrac{2}{5}$ tấm, ngày sau bán $\\dfrac{3}{10}$ tấm. Phần tấm '
                 'vải còn lại là:',
            'options': ['$\\dfrac{3}{10}$', '$\\dfrac{7}{10}$', '$\\dfrac{1}{2}$', '$\\dfrac{1}{10}$'],
            'answer': 0,
            'solution': 'Đã bán $\\dfrac{2}{5} + \\dfrac{3}{10} = \\dfrac{7}{10}$; còn lại $1 - '
                        '\\dfrac{7}{10} = \\dfrac{3}{10}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 62: Luyện tập chung cộng, trừ phân số** (Chủ đề 11: Phép cộng, phép trừ phân '
                 'số), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Tính đúng giá trị biểu thức có cả phép cộng và phép trừ phân số.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 62: Luyện tập chung cộng, trừ phân số: Tính đúng giá '
                        'trị biểu thức có cả phép cộng và phép trừ phân số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $\\dfrac{5}{6} - \\left(\\dfrac{1}{3} + '
                 '\\dfrac{1}{6}\\right)$ bằng $\\dfrac{1}{3}$."',
            'answer': True,
            'solution': 'Trong ngoặc: $\\dfrac{2}{6} + \\dfrac{1}{6} = \\dfrac{3}{6}$; trừ tiếp: '
                        '$\\dfrac{5}{6} - \\dfrac{3}{6} = \\dfrac{2}{6} = \\dfrac{1}{3}$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 62: Luyện tập chung cộng, trừ phân số**, quy tắc **Tổng phần đã dùng** được '
                 'xác định bởi $S = \\dfrac{a}{b} + \\dfrac{c}{d}$ và áp dụng trực tiếp vào bài toán: “Một '
                 'tấm vải, ngày đầu bán được $\\dfrac{2}{5}$ tấm, ngày hôm sau bán được $\\dfrac{3}{10}$ '
                 'tấm. Hỏi còn lại bao nhiêu phần của tấm vải?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Tổng phần đã dùng** ($S = \\dfrac{a}{b} + '
                        '\\dfrac{c}{d}$) là kiến thức cốt lõi của Bài 62: Luyện tập chung cộng, trừ phân số. '
                        'Số phần tấm vải đã bán trong hai ngày là: $\\dfrac{2}{5} + \\dfrac{3}{10} = '
                        '\\dfrac{4}{10} + \\dfrac{3}{10} = \\dfrac{7}{10}$ (tấm). Số phần tấm...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 62: Luyện tập chung cộng, trừ phân số** để giải quyết tình huống '
                 'sau: Một tấm vải, ngày đầu bán được $\\dfrac{2}{5}$ tấm, ngày hôm sau bán được '
                 '$\\dfrac{3}{10}$ tấm. Hỏi còn lại bao nhiêu phần của tấm vải? Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Số phần tấm vải đã bán trong hai ngày là: $\\dfrac{2}{5} + \\dfrac{3}{10} = '
                        '\\dfrac{4}{10} + \\dfrac{3}{10} = \\dfrac{7}{10}$ (tấm). Số phần tấm vải còn lại '
                        'là...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 62: Luyện tập chung cộng, trừ phân số: Số phần tấm vải '
                        'đã bán trong hai ngày là: $\\dfrac{2}{5} + \\dfrac{3}{10} = \\dfrac{4}{10} + '
                        '\\dfrac{3}{10} = \\dfrac{7}{10}$ (tấm).\n'
                        'Số phần tấm vải còn lại là: $1 - \\dfrac{7}{10} = \\dfrac{3}{10}$ (tấm).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bác Tư dùng $\\dfrac{1}{4}$ diện tích vườn để đào ao và $\\dfrac{1}{2}$ diện tích vườn để '
                 'trồng cây ăn quả, phần còn lại trồng rau. Hỏi diện tích trồng rau chiếm mấy phần diện tích '
                 'vườn (viết dạng a/b)?',
            'answer': ['1/4'],
            'unit': None,
            'solution': 'Phần diện tích đào ao và trồng cây: $\\dfrac{1}{4} + \\dfrac{1}{2} = '
                        '\\dfrac{3}{4}$. Phần trồng rau: $1 - \\dfrac{3}{4} = \\dfrac{1}{4}$.\n'
                        'Đáp số: **$1/4$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd12-nhan-chia-phan-so',
  'context_title': 'Chủ đề 12: Phép nhân, phép chia phân số',
  'context': 'SGK Toán 4 · Chủ đề 12: Phép nhân phân số; phép chia phân số; tìm phân số của một số.',
  'title': 'Bài 63: Phép nhân phân số',
  'icon': '✖️',
  'description': 'Quy tắc nhân hai phân số, nhân phân số với số tự nhiên và các tính chất của phép nhân phân '
                 'số.',
  'requirements': ['Thực hiện đúng phép nhân hai phân số: lấy tử số nhân với tử số, mẫu số nhân với mẫu số.',
                   'Thực hiện được phép nhân phân số với số tự nhiên ($\\dfrac{a}{b} \\times n = \\dfrac{a '
                   '\\times n}{b}$).',
                   'Vận dụng tính diện tích hình chữ nhật, hình vuông có số đo cạnh là phân số.'],
  'definition': '- **Quy tắc nhân hai phân số**: Muốn nhân hai phân số, ta lấy **tử số nhân với tử số**, '
                '**mẫu số nhân với mẫu số**: $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b '
                '\\times d}$.\n'
                '- **Nhân phân số với số tự nhiên**: $\\dfrac{a}{b} \\times n = \\dfrac{a \\times n}{b}$ '
                '(chỉ nhân tử số với số tự nhiên và giữ nguyên mẫu số).',
  'theory': '### 1. Ví dụ phép nhân phân số\n'
            '- Ví dụ 1: $\\dfrac{2}{3} \\times \\dfrac{4}{5} = \\dfrac{2 \\times 4}{3 \\times 5} = '
            '\\dfrac{8}{15}$.\n'
            '- Ví dụ 2: $\\dfrac{3}{4} \\times 2 = \\dfrac{3 \\times 2}{4} = \\dfrac{6}{4} = '
            '\\dfrac{3}{2}$.\n'
            '### 2. Tính chất của phép nhân phân số\n'
            '- Phép nhân phân số cũng có tính chất giao hoán, kết hợp, nhân với $1$ và tính chất phân phối '
            'đối với phép cộng như số tự nhiên.',
  'formulas': [{'category': 'I. Phép nhân phân số',
                'items': [{'name': 'Nhân hai phân số',
                           'formula': '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times '
                                      'd}$'},
                          {'name': 'Nhân với số tự nhiên',
                           'formula': '$\\dfrac{a}{b} \\times n = \\dfrac{a \\times n}{b}$ · $n \\times '
                                      '\\dfrac{a}{b} = \\dfrac{n \\times a}{b}$'}]}],
  'example': 'Một hình chữ nhật có chiều dài $\\dfrac{4}{5}\\text{ m}$ và chiều rộng $\\dfrac{2}{3}\\text{ '
             'm}$. Tính diện tích hình chữ nhật đó.',
  'example_answer': 'Diện tích hình chữ nhật là: $\\dfrac{4}{5} \\times \\dfrac{2}{3} = \\dfrac{4 \\times '
                    '2}{5 \\times 3} = \\dfrac{8}{15}\\text{ (m}^2\\text{)}$.',
  'real_life': '- Tính diện tích tấm kính, tấm bìa có kích thước là các phân số của mét.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $\\dfrac{2}{3} \\times \\dfrac{1}{5}$ là:',
            'options': ['$\\dfrac{3}{8}$', '$\\dfrac{2}{15}$', '$\\dfrac{2}{8}$', '$\\dfrac{10}{3}$'],
            'answer': 1,
            'solution': 'Tử nhân tử, mẫu nhân mẫu: $\\dfrac{2 \\times 1}{3 \\times 5} = \\dfrac{2}{15}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả tối giản của phép nhân $\\dfrac{3}{4} \\times 2$ là:',
            'options': ['$\\dfrac{6}{8}$', '$\\dfrac{3}{8}$', '$\\dfrac{3}{2}$', '$\\dfrac{5}{4}$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{3 \\times 2}{4} = \\dfrac{6}{4} = \\dfrac{3}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 63: Phép nhân phân số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Nhân hai phân số**?',
            'options': ['$\\dfrac{a}{b} \\times n = \\dfrac{a \\times n}{b}$ · $n \\times \\dfrac{a}{b} = '
                        '\\dfrac{n \\times a}{b}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 63: Phép nhân phân số, **Nhân hai phân số** '
                        'được xác định bởi: $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b '
                        '\\times d}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 63: Phép nhân phân số**, nội dung/biểu thức $\\dfrac{a}{b} \\times n = '
                 '\\dfrac{a \\times n}{b}$ · $n \\times \\dfrac{a}{b} = \\dfrac{n \\times a}{b}$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Nhân với số tự nhiên', 'Nhân hai phân số', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 63: Phép nhân phân số, biểu thức/quy tắc $\\dfrac{a}{b} \\times n = '
                        '\\dfrac{a \\times n}{b}$ · $n \\times \\dfrac{a}{b} = \\dfrac{n \\times a}{b}$ '
                        'chính là nội dung của **Nhân với số tự nhiên**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình vuông có cạnh dài $\\dfrac{3}{5}\\text{ m}$. Diện tích của hình vuông đó là:',
            'options': ['$\\dfrac{12}{5}\\text{ m}^2$',
                        '$\\dfrac{9}{25}\\text{ m}^2$',
                        '$\\dfrac{6}{25}\\text{ m}^2$',
                        '$\\dfrac{9}{5}\\text{ m}^2$'],
            'answer': 1,
            'solution': 'Diện tích hình vuông: $S = \\dfrac{3}{5} \\times \\dfrac{3}{5} = '
                        '\\dfrac{9}{25}\\text{ (m}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 63: Phép nhân phân số** (Chủ đề 12: Phép nhân, phép chia phân số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Thực hiện đúng phép nhân hai phân số: lấy tử số nhân với tử số, mẫu số nhân với mẫu '
                        'số.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 63: Phép nhân phân số: Thực hiện đúng phép nhân hai '
                        'phân số: lấy tử số nhân với tử số, mẫu số nhân với mẫu số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{5}{6} \\times 3 = \\dfrac{15}{18}$."',
            'answer': False,
            'solution': 'Khi nhân phân số với $3$, ta chỉ nhân tử số với $3$: $\\dfrac{5 \\times 3}{6} = '
                        '\\dfrac{15}{6} = \\dfrac{5}{2}$ (nhân cả mẫu với $3$ là sai) $\\rightarrow$ '
                        '**Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 63: Phép nhân phân số**, quy tắc **Nhân hai phân số** được xác định bởi '
                 '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$ và áp dụng trực '
                 'tiếp vào bài toán: “Một hình chữ nhật có chiều dài $\\dfrac{4}{5}\\text{ m}$ và chiều rộng '
                 '$\\dfrac{2}{3}\\text{ m}$. Tính diện tích hình chữ nhật đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Nhân hai phân số** ($\\dfrac{a}{b} \\times '
                        '\\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$) là kiến thức cốt lõi của Bài '
                        '63: Phép nhân phân số. Diện tích hình chữ nhật là: $\\dfrac{4}{5} \\times '
                        '\\dfrac{2}{3} = \\dfrac{4 \\times 2}{5 \\times 3} = \\dfrac{8}{15}\\text{ '
                        '(m}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 63: Phép nhân phân số** để giải quyết tình huống sau: Một hình '
                 'chữ nhật có chiều dài $\\dfrac{4}{5}\\text{ m}$ và chiều rộng $\\dfrac{2}{3}\\text{ m}$. '
                 'Tính diện tích hình chữ nhật đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Diện tích hình chữ nhật là: $\\dfrac{4}{5} \\times \\dfrac{2}{3} = \\dfrac{4 '
                        '\\times 2}{5 \\times 3} = \\dfrac{8}{15}\\text{ (m}^2\\text{)}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 63: Phép nhân phân số: Diện tích hình chữ nhật là: '
                        '$\\dfrac{4}{5} \\times \\dfrac{2}{3} = \\dfrac{4 \\times 2}{5 \\times 3} = '
                        '\\dfrac{8}{15}\\text{ (m}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị biểu thức: $\\dfrac{3}{7} \\times \\dfrac{4}{9} + \\dfrac{3}{7} \\times '
                 '\\dfrac{5}{9}$ (viết kết quả tối giản dạng a/b).',
            'answer': ['3/7'],
            'unit': None,
            'solution': 'Áp dụng tính chất phân phối: $\\dfrac{3}{7} \\times \\left(\\dfrac{4}{9} + '
                        '\\dfrac{5}{9}\\right) = \\dfrac{3}{7} \\times 1 = \\dfrac{3}{7}$.\n'
                        'Đáp số: **$3/7$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd12-nhan-chia-phan-so',
  'context_title': 'Chủ đề 12: Phép nhân, phép chia phân số',
  'context': 'SGK Toán 4 · Chủ đề 12: Phép nhân phân số; phép chia phân số; tìm phân số của một số.',
  'title': 'Bài 64: Phép chia phân số',
  'icon': '➗',
  'description': 'Nhận biết phân số đảo ngược và quy tắc chia hai phân số (nhân với phân số thứ hai đảo '
                 'ngược).',
  'requirements': ['Tìm được **phân số đảo ngược** của một phân số khác $0$.',
                   'Thực hiện đúng phép chia hai phân số: lấy phân số thứ nhất nhân với phân số thứ hai đảo '
                   'ngược.',
                   'Thực hiện được phép chia phân số cho số tự nhiên khác $0$ và chia số tự nhiên cho phân '
                   'số.'],
  'definition': '- **Phân số đảo ngược** của phân số $\\dfrac{c}{d}$ ($c, d \\ne 0$) là phân số '
                '$\\dfrac{d}{c}$ (hai phân số đảo ngược nhân với nhau luôn bằng $1$).\n'
                '- **Quy tắc chia hai phân số**: Muốn chia hai phân số, ta lấy **phân số thứ nhất nhân với '
                'phân số đảo ngược của phân số thứ hai**: $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} '
                '\\times \\dfrac{d}{c}$.',
  'theory': '### 1. Ví dụ chia hai phân số\n'
            '- Ví dụ: $\\dfrac{3}{5} : \\dfrac{2}{7} = \\dfrac{3}{5} \\times \\dfrac{7}{2} = '
            '\\dfrac{21}{10}$.\n'
            '- Ví dụ: $\\dfrac{3}{4} : \\dfrac{1}{2} = \\dfrac{3}{4} \\times \\dfrac{2}{1} = \\dfrac{6}{4} = '
            '\\dfrac{3}{2}$.\n'
            '### 2. Chia phân số với số tự nhiên ($n \\ne 0$)\n'
            '- Chia phân số cho $n$: $\\dfrac{a}{b} : n = \\dfrac{a}{b \\times n}$ (ví dụ $\\dfrac{4}{7} : 2 '
            '= \\dfrac{4}{14} = \\dfrac{2}{7}$).\n'
            '- Chia số tự nhiên cho phân số: $n : \\dfrac{c}{d} = n \\times \\dfrac{d}{c}$.',
  'formulas': [{'category': 'I. Phép chia phân số',
                'items': [{'name': 'Phân số đảo ngược của c/d',
                           'formula': '$\\dfrac{d}{c}$ ($\\dfrac{c}{d} \\times \\dfrac{d}{c} = 1$)'},
                          {'name': 'Chia hai phân số',
                           'formula': '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times '
                                      '\\dfrac{d}{c}$'},
                          {'name': 'Chia cho số tự nhiên',
                           'formula': '$\\dfrac{a}{b} : n = \\dfrac{a}{b \\times n}$ ($n \\ne 0$)'}]}],
  'example': 'Có $\\dfrac{3}{4}\\text{ l}$ nước cam rót đều vào các cốc, mỗi cốc chứa $\\dfrac{1}{8}\\text{ '
             'l}$. Hỏi rót được bao nhiêu cốc nước cam?',
  'example_answer': 'Số cốc nước cam rót được là: $\\dfrac{3}{4} : \\dfrac{1}{8} = \\dfrac{3}{4} \\times '
                    '\\dfrac{8}{1} = \\dfrac{24}{4} = 6\\text{ (cốc)}$.\n'
                    'Đáp số: **$6\\text{ cốc}$**.',
  'real_life': '- Tìm chiều rộng hình chữ nhật khi biết diện tích và chiều dài; chia lượng nước hoặc bột vào '
               'các túi nhỏ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số đảo ngược của phân số $\\dfrac{4}{9}$ là:',
            'options': ['$\\dfrac{4}{9}$', '$\\dfrac{1}{4}$', '$\\dfrac{9}{4}$', '$\\dfrac{5}{9}$'],
            'answer': 2,
            'solution': 'Đổi chỗ tử số và mẫu số của $\\dfrac{4}{9}$ ta được **$\\dfrac{9}{4}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn chia một phân số cho một phân số khác $0$, ta lấy phân số thứ nhất:',
            'options': ['Chia tử cho tử, mẫu cho mẫu',
                        'Cộng với phân số thứ hai',
                        'Nhân với phân số thứ hai',
                        'Nhân với phân số đảo ngược của phân số thứ hai'],
            'answer': 3,
            'solution': 'Theo quy tắc: $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times '
                        '\\dfrac{d}{c}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 64: Phép chia phân số**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Phân số đảo ngược của c/d**?',
            'options': ['$\\dfrac{d}{c}$ ($\\dfrac{c}{d} \\times \\dfrac{d}{c} = 1$)',
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$',
                        '$\\dfrac{a}{b} : n = \\dfrac{a}{b \\times n}$ ($n \\ne 0$)',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 64: Phép chia phân số, **Phân số đảo ngược '
                        'của c/d** được xác định bởi: $\\dfrac{d}{c}$ ($\\dfrac{c}{d} \\times \\dfrac{d}{c} '
                        '= 1$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 64: Phép chia phân số**, nội dung/biểu thức $\\dfrac{a}{b} : \\dfrac{c}{d} = '
                 '\\dfrac{a}{b} \\times \\dfrac{d}{c}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phân số đảo ngược của c/d',
                        'Chia hai phân số',
                        'Chia cho số tự nhiên',
                        'Phân tích số'],
            'answer': 1,
            'solution': 'Trong Bài 64: Phép chia phân số, biểu thức/quy tắc $\\dfrac{a}{b} : \\dfrac{c}{d} = '
                        '\\dfrac{a}{b} \\times \\dfrac{d}{c}$ chính là nội dung của **Chia hai phân số**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả rút gọn tối giản của phép chia $\\dfrac{3}{4} : \\dfrac{1}{2}$ là:',
            'options': ['$\\dfrac{3}{8}$', '$\\dfrac{2}{3}$', '$\\dfrac{3}{2}$', '$\\dfrac{4}{6}$'],
            'answer': 2,
            'solution': 'Ta có $\\dfrac{3}{4} : \\dfrac{1}{2} = \\dfrac{3}{4} \\times \\dfrac{2}{1} = '
                        '\\dfrac{6}{4} = \\dfrac{3}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 64: Phép chia phân số** (Chủ đề 12: Phép nhân, phép chia phân số), khẳng '
                 'định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Tìm được **phân số đảo ngược** của một phân số khác $0$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 64: Phép chia phân số: Tìm được **phân số đảo ngược** '
                        'của một phân số khác $0$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{4}{7} : 2 = \\dfrac{2}{7}$."',
            'answer': True,
            'solution': 'Ta có $\\dfrac{4}{7} : 2 = \\dfrac{4}{7 \\times 2} = \\dfrac{4}{14} = '
                        '\\dfrac{2}{7}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 64: Phép chia phân số**, quy tắc **Phân số đảo ngược của c/d** được xác định '
                 'bởi $\\dfrac{d}{c}$ ($\\dfrac{c}{d} \\times \\dfrac{d}{c} = 1$) và áp dụng trực tiếp vào '
                 'bài toán: “Có $\\dfrac{3}{4}\\text{ l}$ nước cam rót đều vào các cốc, mỗi cốc chứa '
                 '$\\dfrac{1}{8}\\text{ l}$. Hỏi rót được bao nhiêu cốc nước cam?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Phân số đảo ngược của c/d** ($\\dfrac{d}{c}$ '
                        '($\\dfrac{c}{d} \\times \\dfrac{d}{c} = 1$)) là kiến thức cốt lõi của Bài 64: Phép '
                        'chia phân số. Số cốc nước cam rót được là: $\\dfrac{3}{4} : \\dfrac{1}{8} = '
                        '\\dfrac{3}{4} \\times \\dfrac{8}{1} = \\dfrac{24}{4} = 6\\text{ (cốc)}$. Đáp số: '
                        '**$6\\text{ cốc}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 64: Phép chia phân số** để giải quyết tình huống sau: Có '
                 '$\\dfrac{3}{4}\\text{ l}$ nước cam rót đều vào các cốc, mỗi cốc chứa $\\dfrac{1}{8}\\text{ '
                 'l}$. Hỏi rót được bao nhiêu cốc nước cam? Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Số cốc nước cam rót được là: $\\dfrac{3}{4} : \\dfrac{1}{8} = \\dfrac{3}{4} \\times '
                        '\\dfrac{8}{1} = \\dfrac{24}{4} = 6\\text{ (cốc)}$. Đáp số: **$6\\text{ cốc}$**.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 64: Phép chia phân số: Số cốc nước cam rót được là: '
                        '$\\dfrac{3}{4} : \\dfrac{1}{8} = \\dfrac{3}{4} \\times \\dfrac{8}{1} = '
                        '\\dfrac{24}{4} = 6\\text{ (cốc)}$.\n'
                        'Đáp số: **$6\\text{ cốc}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $\\dfrac{3}{4}\\text{ l}$ nước cam rót đều vào các cốc, mỗi cốc $\\dfrac{1}{8}\\text{ '
                 'l}$. Hỏi rót được tất cả bao nhiêu cốc?',
            'answer': ['6'],
            'unit': 'cốc',
            'solution': 'Ta có $\\dfrac{3}{4} : \\dfrac{1}{8} = \\dfrac{3}{4} \\times \\dfrac{8}{1} = '
                        '6\\text{ (cốc)}$.\n'
                        'Đáp số: **$6\\text{ cốc}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd12-nhan-chia-phan-so',
  'context_title': 'Chủ đề 12: Phép nhân, phép chia phân số',
  'context': 'SGK Toán 4 · Chủ đề 12: Phép nhân phân số; phép chia phân số; tìm phân số của một số.',
  'title': 'Bài 65, 66: Tìm phân số của một số và luyện tập chung',
  'icon': '🎯',
  'description': 'Quy tắc tìm phân số của một số và giải các bài toán thực tế có một hoặc hai bước tính.',
  'requirements': ['Thuộc và áp dụng đúng quy tắc: Muốn tìm $\\dfrac{m}{n}$ của một số $a$, ta lấy $a '
                   '\\times \\dfrac{m}{n}$.',
                   'Tính nhẩm nhanh phân số của một số bằng cách lấy $a : n \\times m$.',
                   'Giải được bài toán thực tế có hai bước tính liên quan đến tìm phân số của một số.'],
  'definition': '- **Quy tắc**: Muốn tìm **phân số $\\dfrac{m}{n}$ của một số $a$** cho trước, ta lấy số $a$ '
                '**nhân** với phân số $\\dfrac{m}{n}$: $a \\times \\dfrac{m}{n}$ (hoặc lấy $a : n \\times '
                'm$).',
  'theory': '### 1. Ý nghĩa trực quan\n'
            '- Tìm $\\dfrac{2}{3}$ của $18$ quả cam: chia $18$ quả cam thành $3$ phần bằng nhau thì $1$ phần '
            'có $18 : 3 = 6$ (quả); lấy $2$ phần thì có $6 \\times 2 = 12$ (quả).\n'
            '- Viết gọn bằng một phép nhân: $18 \\times \\dfrac{2}{3} = 12$ (quả).\n'
            '### 2. Bài toán hai bước tính\n'
            '- Biết tổng ban đầu là $A$, đã bán (hoặc đã dùng) $\\dfrac{m}{n}$ tổng đó, tìm số lượng còn '
            'lại:\n'
            '  - Bước 1: Số lượng đã bán là $A \\times \\dfrac{m}{n}$.\n'
            '  - Bước 2: Số lượng còn lại là $A - \\text{Số lượng đã bán}$.',
  'formulas': [{'category': 'I. Tìm phân số của một số',
                'items': [{'name': 'Công thức',
                           'formula': '$\\dfrac{m}{n} \\text{ của } a = a \\times \\dfrac{m}{n} = (a : n) '
                                      '\\times m$',
                           'note': 'Ví dụ: $\\dfrac{3}{4}$ của $20$ là $20 \\times \\dfrac{3}{4} = 15$'}]}],
  'example': 'Một thửa ruộng thu hoạch được $1\\,200\\text{ kg}$ thóc. Người ta đã bán đi $\\dfrac{3}{4}$ số '
             'thóc đó. Hỏi còn lại bao nhiêu ki-lô-gam thóc?',
  'example_answer': 'Số ki-lô-gam thóc đã bán là: $1\\,200 \\times \\dfrac{3}{4} = 900\\text{ (kg)}$.\n'
                    'Số ki-lô-gam thóc còn lại là: $1\\,200 - 900 = 300\\text{ (kg)}$.',
  'real_life': '- Tính giá tiền sản phẩm sau khi giảm giá $\\dfrac{1}{5}$ giá niêm yết; tính diện tích đất '
               'trồng cây khi biết tỉ lệ phân số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': '$\\dfrac{1}{2}$ của $30$ là:',
            'options': ['$60$', '$2$', '$32$', '$15$'],
            'answer': 3,
            'solution': 'Ta có $30 \\times \\dfrac{1}{2} = 15$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': '$\\dfrac{2}{5}$ của $45\\text{ kg}$ là:',
            'options': ['$18\\text{ kg}$', '$9\\text{ kg}$', '$90\\text{ kg}$', '$112\\text{ kg}$'],
            'answer': 0,
            'solution': 'Ta có $45 \\times \\dfrac{2}{5} = (45 : 5) \\times 2 = 18\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 65, 66: Tìm phân số của một số và luyện tập chung**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Công thức**?',
            'options': ['$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$\\dfrac{m}{n} \\text{ của } a = a \\times \\dfrac{m}{n} = (a : n) \\times m$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$() \\rightarrow \\times, : \\rightarrow +, -$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 65, 66: Tìm phân số của một số và luyện tập '
                        'chung, **Công thức** được xác định bởi: $\\dfrac{m}{n} \\text{ của } a = a \\times '
                        '\\dfrac{m}{n} = (a : n) \\times m$. (Ví dụ: $\\dfrac{3}{4}$ của $20$ là $20 \\times '
                        '\\dfrac{3}{4} = 15$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 65, 66: Tìm phân số của một số và luyện tập chung**, nội dung/biểu thức '
                 '$\\dfrac{m}{n} \\text{ của } a = a \\times \\dfrac{m}{n} = (a : n) \\times m$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Phân tích số', 'Quy tắc 5', 'Công thức', 'Quy tắc'],
            'answer': 2,
            'solution': 'Trong Bài 65, 66: Tìm phân số của một số và luyện tập chung, biểu thức/quy tắc '
                        '$\\dfrac{m}{n} \\text{ của } a = a \\times \\dfrac{m}{n} = (a : n) \\times m$ chính '
                        'là nội dung của **Công thức**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một thửa ruộng thu được $1\\,200\\text{ kg}$ thóc, người ta bán đi $\\dfrac{3}{4}$ số thóc '
                 'đó. Số thóc còn lại là:',
            'options': ['$900\\text{ kg}$', '$400\\text{ kg}$', '$1\\,600\\text{ kg}$', '$300\\text{ kg}$'],
            'answer': 3,
            'solution': 'Đã bán: $1\\,200 \\times \\dfrac{3}{4} = 900\\text{ (kg)}$. Còn lại: $1\\,200 - 900 '
                        '= 300\\text{ (kg)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 65, 66: Tìm phân số của một số và luyện tập chung** (Chủ đề 12: Phép nhân, '
                 'phép chia phân số), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Thuộc và áp dụng đúng quy tắc: Muốn tìm $\\dfrac{m}{n}$ của một số $a$, ta lấy $a '
                        '\\times \\dfrac{m}{n}$.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 65, 66: Tìm phân số của một số và luyện tập chung: '
                        'Thuộc và áp dụng đúng quy tắc: Muốn tìm $\\dfrac{m}{n}$ của một số $a$, ta lấy $a '
                        '\\times \\dfrac{m}{n}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{3}{4}$ giờ bằng $45$ phút."',
            'answer': True,
            'solution': 'Đổi $1\\text{ giờ} = 60\\text{ phút}$; $\\dfrac{3}{4}$ của $60$ phút là $60 \\times '
                        '\\dfrac{3}{4} = 45$ phút $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 65, 66: Tìm phân số của một số và luyện tập chung**, quy tắc **Công thức** '
                 'được xác định bởi $\\dfrac{m}{n} \\text{ của } a = a \\times \\dfrac{m}{n} = (a : n) '
                 '\\times m$ và áp dụng trực tiếp vào bài toán: “Một thửa ruộng thu hoạch được '
                 '$1\\,200\\text{ kg}$ thóc. Người ta đã bán đi $\\dfrac{3}{4}$ số thóc đó. Hỏi còn lại bao '
                 'nhiêu ki-lô-gam thóc?”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Công thức** ($\\dfrac{m}{n} \\text{ của } a = a '
                        '\\times \\dfrac{m}{n} = (a : n) \\times m$) là kiến thức cốt lõi của Bài 65, 66: '
                        'Tìm phân số của một số và luyện tập chung. Số ki-lô-gam thóc đã bán là: $1\\,200 '
                        '\\times \\dfrac{3}{4} = 900\\text{ (kg)}$. Số ki-lô-gam thóc còn lại là: $1\\,200 - '
                        '900 = 300\\text{ (kg)}$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 65, 66: Tìm phân số của một số và luyện tập chung** để giải quyết '
                 'tình huống sau: Một thửa ruộng thu hoạch được $1\\,200\\text{ kg}$ thóc. Người ta đã bán '
                 'đi $\\dfrac{3}{4}$ số thóc đó. Hỏi còn lại bao nhiêu ki-lô-gam thóc? Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Số ki-lô-gam thóc đã bán là: $1\\,200 \\times \\dfrac{3}{4} = 900\\text{ (kg)}$. Số '
                        'ki-lô-gam thóc còn lại là: $1\\,200 - 900 = 300\\text{ (kg)}$.',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 65, 66: Tìm phân số của một số và luyện tập chung: Số '
                        'ki-lô-gam thóc đã bán là: $1\\,200 \\times \\dfrac{3}{4} = 900\\text{ (kg)}$.\n'
                        'Số ki-lô-gam thóc còn lại là: $1\\,200 - 900 = 300\\text{ (kg)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mảnh vườn hình chữ nhật có chiều dài $60\\text{ m}$, chiều rộng bằng $\\dfrac{2}{3}$ '
                 'chiều dài. Tính diện tích mảnh vườn đó theo mét vuông (viết số liền).',
            'answer': ['2400'],
            'unit': 'm²',
            'solution': 'Chiều rộng mảnh vườn là: $60 \\times \\dfrac{2}{3} = 40\\text{ (m)}$. Diện tích '
                        'mảnh vườn là: $60 \\times 40 = 2\\,400\\text{ (m}^2\\text{)}$.\n'
                        'Đáp số: **$2400$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd13-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 13: Ôn tập cuối năm',
  'context': 'SGK Toán 4 · Chủ đề 13: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 67, 68: Ôn tập số tự nhiên và các phép tính',
  'icon': '🔢',
  'description': 'Hệ thống hóa kiến thức về số tự nhiên đến lớp triệu, bốn phép tính, các tính chất và các '
                 'bài toán điển hình.',
  'requirements': ['Đọc, viết, xác định hàng và lớp, so sánh, làm tròn các số tự nhiên đến lớp triệu.',
                   'Thực hiện thành thạo bốn phép tính và vận dụng tính chất giao hoán, kết hợp, phân phối '
                   'để tính nhanh.',
                   'Giải được các bài toán trung bình cộng, tìm hai số khi biết tổng và hiệu, rút về đơn '
                   'vị.'],
  'definition': '- **Tính chất phân phối**: $a \\times (b + c) = a \\times b + a \\times c$.\n'
                '- **Trung bình cộng**: $\\text{TBC} = \\text{Tổng} : \\text{Số các số hạng}$.\n'
                '- **Tổng – Hiệu**: $\\text{Số lớn} = (\\text{Tổng} + \\text{Hiệu}) : 2$; $\\text{Số bé} = '
                '(\\text{Tổng} - \\text{Hiệu}) : 2$.',
  'theory': '### 1. Mẹo tính nhanh với số tự nhiên\n'
            '- Nhân với $101$: $58 \\times 101 = 58 \\times (100 + 1) = 5\\,800 + 58 = 5\\,858$.\n'
            '- Nhân với $99$: $45 \\times 99 = 45 \\times (100 - 1) = 4\\,500 - 45 = 4\\,455$.\n'
            '### 2. Tổng hợp giải toán\n'
            '- Nếu biết trung bình cộng của hai số là $M$ thì **tổng của hai số** là $S = M \\times 2$.',
  'formulas': [{'category': 'I. Công thức giải toán trọng tâm',
                'items': [{'name': 'Trung bình cộng',
                           'formula': '$\\text{TBC} = \\text{Tổng} : n \\Leftrightarrow \\text{Tổng} = '
                                      '\\text{TBC} \\times n$'},
                          {'name': 'Tổng – Hiệu',
                           'formula': '$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$'}]}],
  'example': 'Trung bình cộng của hai số là $50$, hiệu của hai số là $16$. Tìm hai số đó.',
  'example_answer': 'Tổng của hai số là: $50 \\times 2 = 100$.\n'
                    'Số lớn là: $(100 + 16) : 2 = 58$.\n'
                    'Số bé là: $100 - 58 = 42$.',
  'real_life': '- Tính chi phí bình quân mỗi người trong chuyến du lịch hè của gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của chữ số $8$ trong số $3\\,845\\,120$ là:',
            'options': ['$800\\,000$', '$8\\,000$', '$80\\,000$', '$8\\,000\\,000$'],
            'answer': 0,
            'solution': 'Tách lớp $3 \\mid 845 \\mid 120$: chữ số $8$ ở hàng trăm nghìn nên có giá trị là '
                        '**$800\\,000$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $9\\,000 : 100$ là:',
            'options': ['$9$', '$90$', '$900$', '$9\\,000$'],
            'answer': 1,
            'solution': 'Chia cho $100$ ta bỏ bớt $2$ chữ số $0$ ở tận cùng $\\rightarrow$ **$90$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 67, 68: Ôn tập số tự nhiên và các phép tính**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Trung bình cộng**?',
            'options': ['$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        '$\\text{TBC} = \\text{Tổng} : n \\Leftrightarrow \\text{Tổng} = \\text{TBC} \\times '
                        'n$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 67, 68: Ôn tập số tự nhiên và các phép tính, '
                        '**Trung bình cộng** được xác định bởi: $\\text{TBC} = \\text{Tổng} : n '
                        '\\Leftrightarrow \\text{Tổng} = \\text{TBC} \\times n$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 67, 68: Ôn tập số tự nhiên và các phép tính**, nội dung/biểu thức $\\text{Lớn} '
                 '= (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Trung bình cộng', 'Phân tích số', 'Quy tắc 5', 'Tổng – Hiệu'],
            'answer': 3,
            'solution': 'Trong Bài 67, 68: Ôn tập số tự nhiên và các phép tính, biểu thức/quy tắc '
                        '$\\text{Lớn} = (S + H) : 2$ · $\\text{Bé} = (S - H) : 2$ chính là nội dung của '
                        '**Tổng – Hiệu**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trung bình cộng của hai số là $60$, biết hiệu của hai số đó là $20$. Số lớn là:',
            'options': ['$70$', '$40$', '$50$', '$80$'],
            'answer': 0,
            'solution': 'Tổng hai số là $60 \\times 2 = 120$. Số lớn là: $(120 + 20) : 2 = 70$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 67, 68: Ôn tập số tự nhiên và các phép tính** (Chủ đề 13: Ôn tập cuối năm), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Đọc, viết, xác định hàng và lớp, so sánh, làm tròn các số tự nhiên đến lớp triệu.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 67, 68: Ôn tập số tự nhiên và các phép tính: Đọc, '
                        'viết, xác định hàng và lớp, so sánh, làm tròn các số tự nhiên đến lớp triệu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$58 \\times 101 = 5\\,858$."',
            'answer': True,
            'solution': 'Ta có $58 \\times (100 + 1) = 5\\,800 + 58 = 5\\,858$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 67, 68: Ôn tập số tự nhiên và các phép tính**, quy tắc **Trung bình cộng** '
                 'được xác định bởi $\\text{TBC} = \\text{Tổng} : n \\Leftrightarrow \\text{Tổng} = '
                 '\\text{TBC} \\times n$ và áp dụng trực tiếp vào bài toán: “Trung bình cộng của hai số là '
                 '$50$, hiệu của hai số là $16$. Tìm hai số đó.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Trung bình cộng** ($\\text{TBC} = \\text{Tổng} : n '
                        '\\Leftrightarrow \\text{Tổng} = \\text{TBC} \\times n$) là kiến thức cốt lõi của '
                        'Bài 67, 68: Ôn tập số tự nhiên và các phép tính. Tổng của hai số là: $50 \\times 2 '
                        '= 100$. Số lớn là: $(100 + 16) : 2 = 58$. Số bé là: $100 - 58 = 42$.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 67, 68: Ôn tập số tự nhiên và các phép tính** để giải quyết tình '
                 'huống sau: Trung bình cộng của hai số là $50$, hiệu của hai số là $16$. Tìm hai số đó. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Tổng của hai số là: $50 \\times 2 = 100$. Số lớn là: $(100 + 16) : 2 = 58$. Số bé '
                        'là: $100 - 58 = 42$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 67, 68: Ôn tập số tự nhiên và các phép tính: Tổng của '
                        'hai số là: $50 \\times 2 = 100$.\n'
                        'Số lớn là: $(100 + 16) : 2 = 58$.\n'
                        'Số bé là: $100 - 58 = 42$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tổng số tuổi của hai mẹ con là $48$ tuổi, biết tuổi mẹ hơn tuổi con $24$ tuổi. Hỏi con bao '
                 'nhiêu tuổi?',
            'answer': ['12'],
            'unit': 'tuổi',
            'solution': 'Tuổi con (số bé) là: $(48 - 24) : 2 = 12\\text{ (tuổi)}$.\n'
                        'Đáp số: **$12\\text{ tuổi}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd13-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 13: Ôn tập cuối năm',
  'context': 'SGK Toán 4 · Chủ đề 13: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 69: Ôn tập phân số',
  'icon': '🍰',
  'description': 'Củng cố khái niệm phân số, tính chất cơ bản, rút gọn phân số, quy đồng mẫu số và so sánh '
                 'các phân số.',
  'requirements': ['Đọc, viết, nêu ý nghĩa tử số, mẫu số và quan hệ giữa phân số với phép chia số tự nhiên.',
                   'Rút gọn phân số về phân số tối giản và quy đồng mẫu số các phân số.',
                   'So sánh và sắp xếp các phân số bằng nhiều cách (cùng mẫu, cùng tử, so sánh với $1$).'],
  'definition': '- **Tính chất cơ bản**: $\\dfrac{a}{b} = \\dfrac{a \\times m}{b \\times m} = \\dfrac{a : '
                'n}{b : n}$ ($m, n \\ne 0$).\n'
                '- **So sánh**: cùng mẫu số $\\rightarrow$ tử lớn hơn thì lớn hơn; cùng tử số $\\rightarrow$ '
                'mẫu bé hơn thì lớn hơn.',
  'theory': '### 1. Các phương pháp so sánh phân số nhanh\n'
            '- Cách 1: Quy đồng mẫu số.\n'
            '- Cách 2: Quy đồng tử số (so sánh hai mẫu số).\n'
            '- Cách 3: So sánh qua số trung gian $1$ (phân số có tử $< $ mẫu thì $< 1$; tử $> $ mẫu thì $> '
            '1$).\n'
            '- Cách 4 (Phần bù tới $1$): Ví dụ $\\dfrac{7}{8} = 1 - \\dfrac{1}{8}$ và $\\dfrac{8}{9} = 1 - '
            '\\dfrac{1}{9}$; vì $\\dfrac{1}{8} > \\dfrac{1}{9}$ nên $\\dfrac{7}{8} < \\dfrac{8}{9}$.',
  'formulas': [{'category': 'I. Tóm tắt kiến thức phân số',
                'items': [{'name': 'So với 1',
                           'formula': '$\\dfrac{a}{b} < 1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 '
                                      '\\Leftrightarrow a = b$ · $\\dfrac{a}{b} > 1 \\Leftrightarrow a > b$'},
                          {'name': 'Rút gọn',
                           'formula': 'Chia cả tử và mẫu cho ước chung lớn nhất để được phân số tối giản'}]}],
  'example': 'Không quy đồng mẫu số, hãy so sánh hai phân số $\\dfrac{9}{11}$ và $\\dfrac{13}{10}$.',
  'example_answer': 'Ta thấy $\\dfrac{9}{11} < 1$ (vì $9 < 11$) và $\\dfrac{13}{10} > 1$ (vì $13 > 10$).\n'
                    'Vậy **$\\dfrac{9}{11} < \\dfrac{13}{10}$**.',
  'real_life': '- So sánh tỉ lệ hoàn thành kế hoạch của các tổ sản xuất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân số nào dưới đây bằng phân số $\\dfrac{3}{4}$?',
            'options': ['$\\dfrac{6}{12}$', '$\\dfrac{9}{12}$', '$\\dfrac{12}{9}$', '$\\dfrac{7}{8}$'],
            'answer': 1,
            'solution': 'Nhân cả tử và mẫu của $\\dfrac{3}{4}$ với $3$ ta được **$\\dfrac{9}{12}$**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các phân số $\\dfrac{4}{9}, \\dfrac{9}{9}, \\dfrac{11}{9}, \\dfrac{7}{9}$, phân số '
                 'lớn nhất là:',
            'options': ['$\\dfrac{4}{9}$', '$\\dfrac{9}{9}$', '$\\dfrac{11}{9}$', '$\\dfrac{7}{9}$'],
            'answer': 2,
            'solution': 'Cùng mẫu số $9$, tử số $11$ lớn nhất nên **$\\dfrac{11}{9}$** lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 69: Ôn tập phân số**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **So với 1**?',
            'options': ['Chia cả tử và mẫu cho ước chung lớn nhất để được phân số tối giản',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên',
                        '$\\dfrac{a}{b} < 1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 \\Leftrightarrow a '
                        '= b$ · $\\dfrac{a}{b} > 1 \\Leftrightarrow a > b$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 69: Ôn tập phân số, **So với 1** được xác '
                        'định bởi: $\\dfrac{a}{b} < 1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 '
                        '\\Leftrightarrow a = b$ · $\\dfrac{a}{b} > 1 \\Leftrightarrow a > b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 69: Ôn tập phân số**, nội dung/biểu thức Chia cả tử và mẫu cho ước chung lớn '
                 'nhất để được phân số tối giản là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Rút gọn', 'So với 1', 'Phân tích số', 'Quy tắc 5'],
            'answer': 0,
            'solution': 'Trong Bài 69: Ôn tập phân số, biểu thức/quy tắc Chia cả tử và mẫu cho ước chung lớn '
                        'nhất để được phân số tối giản chính là nội dung của **Rút gọn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số tự nhiên $x$ biết $\\dfrac{18}{27} = \\dfrac{x}{3}$:',
            'options': ['$6$', '$2$', '$9$', '$3$'],
            'answer': 1,
            'solution': 'Rút gọn: $\\dfrac{18 : 9}{27 : 9} = \\dfrac{2}{3} \\Rightarrow x = 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 69: Ôn tập phân số** (Chủ đề 13: Ôn tập cuối năm), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'Đọc, viết, nêu ý nghĩa tử số, mẫu số và quan hệ giữa phân số với phép chia số tự '
                        'nhiên.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 69: Ôn tập phân số: Đọc, viết, nêu ý nghĩa tử số, mẫu '
                        'số và quan hệ giữa phân số với phép chia số tự nhiên.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{7}{8} > \\dfrac{8}{9}$."',
            'answer': False,
            'solution': 'Vì $1 - \\dfrac{7}{8} = \\dfrac{1}{8} > \\dfrac{1}{9} = 1 - \\dfrac{8}{9}$ nên '
                        '$\\dfrac{7}{8} < \\dfrac{8}{9}$ $\\rightarrow$ **Sai**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 69: Ôn tập phân số**, quy tắc **So với 1** được xác định bởi $\\dfrac{a}{b} < '
                 '1 \\Leftrightarrow a < b$ · $\\dfrac{a}{b} = 1 \\Leftrightarrow a = b$ · $\\dfrac{a}{b} > '
                 '1 \\Leftrightarrow a > b$ và áp dụng trực tiếp vào bài toán: “Không quy đồng mẫu số, hãy '
                 'so sánh hai phân số $\\dfrac{9}{11}$ và $\\dfrac{13}{10}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **So với 1** ($\\dfrac{a}{b} < 1 \\Leftrightarrow a < '
                        'b$ · $\\dfrac{a}{b} = 1 \\Leftrightarrow a = b$ · $\\dfrac{a}{b} > 1 '
                        '\\Leftrightarrow a > b$) là kiến thức cốt lõi của Bài 69: Ôn tập phân số. Ta thấy '
                        '$\\dfrac{9}{11} < 1$ (vì $9 < 11$) và $\\dfrac{13}{10} > 1$ (vì $13 > 10$). Vậy '
                        '**$\\dfrac{9}{11} < \\dfrac{13}{10}$**.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 69: Ôn tập phân số** để giải quyết tình huống sau: Không quy đồng '
                 'mẫu số, hãy so sánh hai phân số $\\dfrac{9}{11}$ và $\\dfrac{13}{10}$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.',
                        'Ta thấy $\\dfrac{9}{11} < 1$ (vì $9 < 11$) và $\\dfrac{13}{10} > 1$ (vì $13 > 10$). '
                        'Vậy **$\\dfrac{9}{11} < \\dfrac{13}{10}$**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 69: Ôn tập phân số: Ta thấy $\\dfrac{9}{11} < 1$ (vì $9 '
                        '< 11$) và $\\dfrac{13}{10} > 1$ (vì $13 > 10$).\n'
                        'Vậy **$\\dfrac{9}{11} < \\dfrac{13}{10}$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn phân số $\\dfrac{24}{36}$ về phân số tối giản (viết dưới dạng a/b).',
            'answer': ['2/3'],
            'unit': None,
            'solution': 'Chia cả tử số và mẫu số cho $12$: $\\dfrac{24 : 12}{36 : 12} = \\dfrac{2}{3}$.\n'
                        'Đáp số: **$2/3$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd13-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 13: Ôn tập cuối năm',
  'context': 'SGK Toán 4 · Chủ đề 13: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 70: Ôn tập phép tính với phân số',
  'icon': '🧮',
  'description': 'Hệ thống hóa bốn phép tính cộng, trừ, nhân, chia phân số, tính giá trị biểu thức phân số '
                 'và giải toán.',
  'requirements': ['Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia phân số.',
                   'Tính đúng giá trị biểu thức có nhiều phép tính với phân số (nhân chia trước, cộng trừ '
                   'sau).',
                   'Giải được bài toán thực tế kết hợp tìm phân số của một số và các phép tính phân số.'],
  'definition': '- **Cộng, trừ phân số**: $\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$ (khác '
                'mẫu phải quy đồng mẫu số).\n'
                '- **Nhân phân số**: $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times '
                'd}$.\n'
                '- **Chia phân số**: $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$.',
  'theory': '### 1. Thứ tự thực hiện phép tính trong biểu thức phân số\n'
            '- Hoàn toàn giống với số tự nhiên: Trong ngoặc trước $\\rightarrow$ Nhân, chia trước '
            '$\\rightarrow$ Cộng, trừ sau.\n'
            '- Ví dụ: $\\dfrac{2}{3} + \\dfrac{1}{2} \\times \\dfrac{4}{9} = \\dfrac{2}{3} + \\dfrac{2}{9} = '
            '\\dfrac{6}{9} + \\dfrac{2}{9} = \\dfrac{8}{9}$.\n'
            '### 2. Tính bằng cách thuận tiện với phân số\n'
            '- Vận dụng tính chất phân phối: $\\dfrac{a}{b} \\times \\dfrac{c}{d} + \\dfrac{a}{b} \\times '
            '\\dfrac{e}{d} = \\dfrac{a}{b} \\times \\left(\\dfrac{c}{d} + \\dfrac{e}{d}\\right)$.',
  'formulas': [{'category': 'I. Bốn phép tính phân số',
                'items': [{'name': 'Cộng & Trừ',
                           'formula': '$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$'},
                          {'name': 'Nhân & Chia',
                           'formula': '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times '
                                      'd}$ · $\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times '
                                      '\\dfrac{d}{c}$'}]}],
  'example': 'Tính giá trị của biểu thức: $\\dfrac{3}{5} + \\dfrac{2}{5} \\times \\dfrac{1}{2}$.',
  'example_answer': 'Thực hiện phép nhân trước: $\\dfrac{2}{5} \\times \\dfrac{1}{2} = \\dfrac{1}{5}$.\n'
                    'Thực hiện phép cộng sau: $\\dfrac{3}{5} + \\dfrac{1}{5} = \\dfrac{4}{5}$.',
  'real_life': '- Tính diện tích và chu vi các hình có kích thước là phân số; tính lượng hàng hóa đã bán qua '
               'nhiều đợt.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\dfrac{3}{5} + \\dfrac{2}{5} \\times \\dfrac{1}{2}$ là:',
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{5}{10}$', '$\\dfrac{4}{5}$', '$\\dfrac{7}{10}$'],
            'answer': 2,
            'solution': 'Nhân trước: $\\dfrac{2}{5} \\times \\dfrac{1}{2} = \\dfrac{1}{5}$; cộng sau: '
                        '$\\dfrac{3}{5} + \\dfrac{1}{5} = \\dfrac{4}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tìm $x$ biết $x : \\dfrac{2}{3} = \\dfrac{9}{4}$:',
            'options': ['$\\dfrac{27}{8}$', '$\\dfrac{18}{7}$', '$\\dfrac{2}{3}$', '$\\dfrac{3}{2}$'],
            'answer': 3,
            'solution': 'Số bị chia $x = \\dfrac{9}{4} \\times \\dfrac{2}{3} = \\dfrac{18}{12} = '
                        '\\dfrac{3}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 70: Ôn tập phép tính với phân số**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Cộng & Trừ**?',
            'options': ['$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$',
                        '$\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$ · '
                        '$\\dfrac{a}{b} : \\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 70: Ôn tập phép tính với phân số, **Cộng & '
                        'Trừ** được xác định bởi: $\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm '
                        'b}{m}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 70: Ôn tập phép tính với phân số**, nội dung/biểu thức $\\dfrac{a}{b} \\times '
                 '\\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$ · $\\dfrac{a}{b} : \\dfrac{c}{d} = '
                 '\\dfrac{a}{b} \\times \\dfrac{d}{c}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cộng & Trừ', 'Nhân & Chia', 'Phân tích số', 'Quy tắc 5'],
            'answer': 1,
            'solution': 'Trong Bài 70: Ôn tập phép tính với phân số, biểu thức/quy tắc $\\dfrac{a}{b} '
                        '\\times \\dfrac{c}{d} = \\dfrac{a \\times c}{b \\times d}$ · $\\dfrac{a}{b} : '
                        '\\dfrac{c}{d} = \\dfrac{a}{b} \\times \\dfrac{d}{c}$ chính là nội dung của **Nhân & '
                        'Chia**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình chữ nhật có diện tích $\\dfrac{15}{16}\\text{ m}^2$ và chiều dài '
                 '$\\dfrac{5}{4}\\text{ m}$. Chiều rộng của hình chữ nhật đó là:',
            'options': ['$\\dfrac{4}{3}\\text{ m}$',
                        '$\\dfrac{75}{64}\\text{ m}$',
                        '$\\dfrac{3}{4}\\text{ m}$',
                        '$\\dfrac{1}{2}\\text{ m}$'],
            'answer': 2,
            'solution': 'Chiều rộng bằng diện tích chia chiều dài: $\\dfrac{15}{16} : \\dfrac{5}{4} = '
                        '\\dfrac{15}{16} \\times \\dfrac{4}{5} = \\dfrac{3}{4}\\text{ (m)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 70: Ôn tập phép tính với phân số** (Chủ đề 13: Ôn tập cuối năm), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.',
                        'Thực hiện thành thạo bốn phép tính cộng, trừ, nhân, chia phân số.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 70: Ôn tập phép tính với phân số: Thực hiện thành thạo '
                        'bốn phép tính cộng, trừ, nhân, chia phân số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Giá trị của biểu thức $\\dfrac{5}{7} \\times \\dfrac{3}{8} + \\dfrac{5}{7} '
                 '\\times \\dfrac{5}{8}$ bằng $\\dfrac{5}{7}$."',
            'answer': True,
            'solution': 'Đặt $\\dfrac{5}{7}$ làm thừa số chung: $\\dfrac{5}{7} \\times \\left(\\dfrac{3}{8} '
                        '+ \\dfrac{5}{8}\\right) = \\dfrac{5}{7} \\times 1 = \\dfrac{5}{7}$ $\\rightarrow$ '
                        '**Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 70: Ôn tập phép tính với phân số**, quy tắc **Cộng & Trừ** được xác định bởi '
                 '$\\dfrac{a}{m} \\pm \\dfrac{b}{m} = \\dfrac{a \\pm b}{m}$ và áp dụng trực tiếp vào bài '
                 'toán: “Tính giá trị của biểu thức: $\\dfrac{3}{5} + \\dfrac{2}{5} \\times '
                 '\\dfrac{1}{2}$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Cộng & Trừ** ($\\dfrac{a}{m} \\pm \\dfrac{b}{m} = '
                        '\\dfrac{a \\pm b}{m}$) là kiến thức cốt lõi của Bài 70: Ôn tập phép tính với phân '
                        'số. Thực hiện phép nhân trước: $\\dfrac{2}{5} \\times \\dfrac{1}{2} = '
                        '\\dfrac{1}{5}$. Thực hiện phép cộng sau: $\\dfrac{3}{5} + \\dfrac{1}{5} = '
                        '\\dfrac{4}{5}$...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 70: Ôn tập phép tính với phân số** để giải quyết tình huống sau: '
                 'Tính giá trị của biểu thức: $\\dfrac{3}{5} + \\dfrac{2}{5} \\times \\dfrac{1}{2}$. Kết quả '
                 'và hướng giải nào dưới đây là **đúng**?',
            'options': ['Thực hiện phép nhân trước: $\\dfrac{2}{5} \\times \\dfrac{1}{2} = \\dfrac{1}{5}$. '
                        'Thực hiện phép cộng sau: $\\dfrac{3}{5} + \\dfrac{1}{5} = \\dfrac{4}{5}$.',
                        'Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 70: Ôn tập phép tính với phân số: Thực hiện phép nhân '
                        'trước: $\\dfrac{2}{5} \\times \\dfrac{1}{2} = \\dfrac{1}{5}$.\n'
                        'Thực hiện phép cộng sau: $\\dfrac{3}{5} + \\dfrac{1}{5} = \\dfrac{4}{5}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng có $120\\text{ kg}$ đường. Buổi sáng bán được $\\dfrac{1}{3}$ số đường đó, '
                 'buổi chiều bán được $\\dfrac{2}{5}$ số đường ban đầu. Hỏi cả hai buổi cửa hàng bán được '
                 'bao nhiêu ki-lô-gam đường?',
            'answer': ['88'],
            'unit': 'kg',
            'solution': 'Buổi sáng bán: $120 \\times \\dfrac{1}{3} = 40\\text{ (kg)}$. Buổi chiều bán: $120 '
                        '\\times \\dfrac{2}{5} = 48\\text{ (kg)}$. Cả hai buổi bán: $40 + 48 = 88\\text{ '
                        '(kg)}$.\n'
                        'Đáp số: **$88\\text{ kg}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd13-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 13: Ôn tập cuối năm',
  'context': 'SGK Toán 4 · Chủ đề 13: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 71: Ôn tập hình học và đo lường',
  'icon': '📐',
  'description': 'Hệ thống hóa kiến thức về góc, đường thẳng vuông góc, song song, hình bình hành, hình thoi '
                 'và các đơn vị đo đại lượng.',
  'requirements': ['Nhận diện và nêu đúng tính chất của góc nhọn, góc vuông, góc tù, góc bẹt, hình bình '
                   'hành, hình thoi.',
                   'Chuyển đổi thành thạo các đơn vị đo khối lượng (yến, tạ, tấn), diện tích ($\\text{m}^2, '
                   '\\text{dm}^2, \\text{cm}^2, \\text{mm}^2$) và thời gian (giây, thế kỉ).',
                   'Giải được bài toán thực tế kết hợp hình học (diện tích, chu vi) và phân số.'],
  'definition': '- **Góc**: nhọn ($< 90^\\circ$), vuông ($= 90^\\circ$), tù ($90^\\circ < \\alpha < '
                '180^\\circ$), bẹt ($= 180^\\circ$).\n'
                '- **Đo lường**: $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1\\,000\\text{ kg}$; '
                '$1\\text{ m}^2 = 100\\text{ dm}^2 = 10\\,000\\text{ cm}^2$; $1\\text{ thế kỉ} = 100\\text{ '
                'năm}$.',
  'theory': '### 1. Đổi đơn vị có chứa phân số\n'
            '- Ví dụ: $\\dfrac{1}{2}\\text{ m}^2 = 100 \\times \\dfrac{1}{2} = 50\\text{ dm}^2$.\n'
            '- Ví dụ: $\\dfrac{3}{5}\\text{ tấn} = 1\\,000 \\times \\dfrac{3}{5} = 600\\text{ kg}$.\n'
            '- Ví dụ: $\\dfrac{2}{3}\\text{ phút} = 60 \\times \\dfrac{2}{3} = 40\\text{ giây}$.\n'
            '### 2. Bài toán diện tích hình chữ nhật kết hợp phân số\n'
            '- Biết chiều dài $a$ và chiều rộng bằng $\\dfrac{m}{n}$ chiều dài $\\rightarrow$ tính chiều '
            'rộng $b = a \\times \\dfrac{m}{n}$ rồi tính diện tích $S = a \\times b$.',
  'formulas': [{'category': 'I. Đổi đơn vị với phân số',
                'items': [{'name': 'Quy tắc',
                           'formula': 'Lấy số quy đổi của $1$ đơn vị lớn nhân với phân số'},
                          {'name': 'Ví dụ mẫu',
                           'formula': '$\\dfrac{1}{4}\\text{ thế kỉ} = 25\\text{ năm}$ · '
                                      '$\\dfrac{1}{2}\\text{ m}^2 = 50\\text{ dm}^2$'}]}],
  'example': 'Đổi các đơn vị sau: a) $\\dfrac{3}{4}\\text{ tấn} = \\dots\\text{ kg}$; b) $4\\text{ '
             'm}^2\\text{ } 15\\text{ dm}^2 = \\dots\\text{ dm}^2$.',
  'example_answer': 'a) Vì $1\\text{ tấn} = 1\\,000\\text{ kg}$ nên $\\dfrac{3}{4}\\text{ tấn} = 1\\,000 '
                    '\\times \\dfrac{3}{4} = 750\\text{ kg}$.\n'
                    'b) $4\\text{ m}^2\\text{ } 15\\text{ dm}^2 = 400\\text{ dm}^2 + 15\\text{ dm}^2 = '
                    '415\\text{ dm}^2$.',
  'real_life': '- Tính diện tích sân trường, vườn cây và sản lượng thu hoạch.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc lớn hơn góc vuông nhưng bé hơn góc bẹt được gọi là:',
            'options': ['Góc nhọn', 'Góc vuông', 'Góc bẹt', 'Góc tù'],
            'answer': 3,
            'solution': 'Góc lớn hơn $90^\\circ$ và bé hơn $180^\\circ$ là **góc tù**.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $2\\text{ tấn } 30\\text{ kg} = \\dots\\text{ kg}$?',
            'options': ['$2\\,030\\text{ kg}$',
                        '$230\\text{ kg}$',
                        '$2\\,300\\text{ kg}$',
                        '$20\\,030\\text{ kg}$'],
            'answer': 0,
            'solution': 'Ta có $2\\,000\\text{ kg} + 30\\text{ kg} = 2\\,030\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 71: Ôn tập hình học và đo lường**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Quy tắc**?',
            'options': ['$\\dfrac{1}{4}\\text{ thế kỉ} = 25\\text{ năm}$ · $\\dfrac{1}{2}\\text{ m}^2 = '
                        '50\\text{ dm}^2$',
                        'Lấy số quy đổi của $1$ đơn vị lớn nhân với phân số',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 71: Ôn tập hình học và đo lường, **Quy tắc** '
                        'được xác định bởi: Lấy số quy đổi của $1$ đơn vị lớn nhân với phân số.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 71: Ôn tập hình học và đo lường**, nội dung/biểu thức $\\dfrac{1}{4}\\text{ '
                 'thế kỉ} = 25\\text{ năm}$ · $\\dfrac{1}{2}\\text{ m}^2 = 50\\text{ dm}^2$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Quy tắc', 'Phân tích số', 'Ví dụ mẫu', 'Quy tắc 5'],
            'answer': 2,
            'solution': 'Trong Bài 71: Ôn tập hình học và đo lường, biểu thức/quy tắc $\\dfrac{1}{4}\\text{ '
                        'thế kỉ} = 25\\text{ năm}$ · $\\dfrac{1}{2}\\text{ m}^2 = 50\\text{ dm}^2$ chính là '
                        'nội dung của **Ví dụ mẫu**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đổi đơn vị: $\\dfrac{3}{5}\\text{ m}^2 = \\dots\\text{ dm}^2$?',
            'options': ['$35\\text{ dm}^2$', '$600\\text{ dm}^2$', '$20\\text{ dm}^2$', '$60\\text{ dm}^2$'],
            'answer': 3,
            'solution': 'Vì $1\\text{ m}^2 = 100\\text{ dm}^2$ nên $\\dfrac{3}{5}\\text{ m}^2 = 100 \\times '
                        '\\dfrac{3}{5} = 60\\text{ (dm}^2\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 71: Ôn tập hình học và đo lường** (Chủ đề 13: Ôn tập cuối năm), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận diện và nêu đúng tính chất của góc nhọn, góc vuông, góc tù, góc bẹt, hình bình '
                        'hành, hình thoi.',
                        'Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 71: Ôn tập hình học và đo lường: Nhận diện và nêu đúng '
                        'tính chất của góc nhọn, góc vuông, góc tù, góc bẹt, hình bình hành, hình thoi.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "$\\dfrac{2}{3}$ phút bằng $40$ giây."',
            'answer': True,
            'solution': 'Vì $1\\text{ phút} = 60\\text{ giây}$ nên $60 \\times \\dfrac{2}{3} = 40\\text{ '
                        'giây}$ $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 71: Ôn tập hình học và đo lường**, quy tắc **Quy tắc** được xác định bởi Lấy '
                 'số quy đổi của $1$ đơn vị lớn nhân với phân số và áp dụng trực tiếp vào bài toán: “Đổi các '
                 'đơn vị sau: a) $\\dfrac{3}{4}\\text{ tấn} = \\dots\\text{ kg}$; b) $4\\text{ m}^2\\text{ } '
                 '15\\text{ dm}^2 = \\dots\\text{ dm}^2$.”. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Quy tắc** (Lấy số quy đổi của $1$ đơn vị lớn nhân '
                        'với phân số) là kiến thức cốt lõi của Bài 71: Ôn tập hình học và đo lường. a) Vì '
                        '$1\\text{ tấn} = 1\\,000\\text{ kg}$ nên $\\dfrac{3}{4}\\text{ tấn} = 1\\,000 '
                        '\\times \\dfrac{3}{4} = 750\\text{ kg}$. b)...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 71: Ôn tập hình học và đo lường** để giải quyết tình huống sau: '
                 'Đổi các đơn vị sau: a) $\\dfrac{3}{4}\\text{ tấn} = \\dots\\text{ kg}$; b) $4\\text{ '
                 'm}^2\\text{ } 15\\text{ dm}^2 = \\dots\\text{ dm}^2$. Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'a) Vì $1\\text{ tấn} = 1\\,000\\text{ kg}$ nên $\\dfrac{3}{4}\\text{ tấn} = 1\\,000 '
                        '\\times \\dfrac{3}{4} = 750\\text{ kg}$. b) $4\\text{ m}^2\\text{ } 15\\text{ dm}^2 '
                        '= 400\\text{ dm}^2 + 15\\text{ dm}^2 = 415\\text{ dm}^2$...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 71: Ôn tập hình học và đo lường: a) Vì $1\\text{ tấn} = '
                        '1\\,000\\text{ kg}$ nên $\\dfrac{3}{4}\\text{ tấn} = 1\\,000 \\times \\dfrac{3}{4} '
                        '= 750\\text{ kg}$.\n'
                        'b) $4\\text{ m}^2\\text{ } 15\\text{ dm}^2 = 400\\text{ dm}^2 + 15\\text{ dm}^2 = '
                        '415\\text{ dm}^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khu đất hình bình hành có cạnh đáy dài $45\\text{ m}$, cạnh kề với nó bằng '
                 '$\\dfrac{2}{3}$ cạnh đáy. Tính chu vi của khu đất đó theo đơn vị mét.',
            'answer': ['150'],
            'unit': 'm',
            'solution': 'Cạnh kề dài: $45 \\times \\dfrac{2}{3} = 30\\text{ (m)}$. Chu vi khu đất là: $(45 + '
                        '30) \\times 2 = 150\\text{ (m)}$.\n'
                        'Đáp số: **$150\\text{ m}$**.',
            'alt': None,
            'note': None}]},
 {'topic': 'l4-cd13-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 13: Ôn tập cuối năm',
  'context': 'SGK Toán 4 · Chủ đề 13: Ôn tập tổng hợp cuối năm học.',
  'title': 'Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung',
  'icon': '🏁',
  'description': 'Hệ thống hóa kiến thức về dãy số liệu, biểu đồ cột, số lần xuất hiện của sự kiện và giải '
                 'toán tổng hợp cuối lớp 4.',
  'requirements': ['Đọc, phân tích dãy số liệu thống kê và biểu đồ cột.',
                   'Tính được số trung bình cộng, phân số chỉ tỉ lệ từ biểu đồ cột và bảng thống kê.',
                   'Kiểm đếm số lần xuất hiện của một sự kiện và giải bài toán tổng hợp cuối năm.'],
  'definition': '- **Dãy số liệu & Biểu đồ cột**: giúp so sánh độ lớn, tính tổng $S$ và số trung bình cộng '
                '$S : n$.\n'
                '- **Số lần xuất hiện của sự kiện**: tổng số lần xuất hiện của các khả năng bằng tổng số lần '
                'thử $N = n_1 + n_2 + \\dots + n_k$.',
  'theory': '### 1. Kết hợp thống kê với phân số và trung bình cộng\n'
            '- Từ biểu đồ cột, ta tìm được phân số $\\dfrac{a}{S}$ chỉ số lượng của đối tượng $A$ so với '
            'tổng số lượng $S$ của cả nhóm.\n'
            '### 2. Tổng kết chương trình Toán lớp 4\n'
            '- Nắm vững số tự nhiên đến lớp triệu ($1\\,000\\,000$), phân số $\\dfrac{a}{b}$ và $4$ phép '
            'tính phân số, các bài toán điển hình, hình học và đo lường.',
  'formulas': [{'category': 'I. Tổng hợp kiến thức Lớp 4',
                'items': [{'name': 'Thống kê',
                           'formula': 'Trung bình cộng $= \\text{Tổng số liệu} : \\text{Số các số liệu}$'},
                          {'name': 'Xác suất thực nghiệm',
                           'formula': '$\\text{Tổng số lần thử} = n_1 + n_2 + \\dots + n_k$'}]}],
  'example': 'Biểu đồ cột cho biết số cây khối 4 trồng được trong $3$ ngày: Ngày 1 ($40$ cây), Ngày 2 ($50$ '
             'cây), Ngày 3 ($60$ cây). Tính trung bình mỗi ngày khối 4 trồng được bao nhiêu cây và phân số '
             'chỉ số cây trồng Ngày 1 so với tổng số cây.',
  'example_answer': 'Tổng số cây trồng trong $3$ ngày là: $40 + 50 + 60 = 150\\text{ (cây)}$.\n'
                    'Trung bình mỗi ngày trồng được: $150 : 3 = 50\\text{ (cây)}$.\n'
                    'Phân số chỉ số cây Ngày 1 so với tổng số cây là: $\\dfrac{40}{150} = \\dfrac{4}{15}$.',
  'real_life': '- Lập bảng tổng kết điểm các môn học cuối năm và theo dõi kế hoạch đọc sách mùa hè.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho dãy số liệu số quyển vở của 4 bạn: $10, 12, 14, 16$. Trung bình mỗi bạn có bao nhiêu '
                 'quyển vở?',
            'options': ['$13$ quyển', '$12$ quyển', '$14$ quyển', '$52$ quyển'],
            'answer': 0,
            'solution': 'Trung bình cộng: $(10 + 12 + 14 + 16) : 4 = 52 : 4 = 13\\text{ (quyển)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Quay một chiếc kim trên mặt đồng hồ trò chơi gồm $2$ phần màu xanh và màu vàng $15$ lần, '
                 'kim dừng ở phần màu xanh $9$ lần. Số lần kim dừng ở phần màu vàng là:',
            'options': ['$9$ lần', '$6$ lần', '$15$ lần', '$24$ lần'],
            'answer': 1,
            'solution': 'Số lần dừng ở màu vàng là: $15 - 9 = 6\\text{ (lần)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thống kê**?',
            'options': ['$\\text{Tổng số lần thử} = n_1 + n_2 + \\dots + n_k$',
                        '$\\overline{abcde} = a0\\,000 + b\\,000 + c00 + d0 + e$',
                        'Trung bình cộng $= \\text{Tổng số liệu} : \\text{Số các số liệu}$',
                        'Chữ số ngay bên phải hàng làm tròn: $< 5 \\rightarrow$ xuống · $\\ge 5 '
                        '\\rightarrow$ lên'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập '
                        'chung, **Thống kê** được xác định bởi: Trung bình cộng $= \\text{Tổng số liệu} : '
                        '\\text{Số các số liệu}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung**, nội dung/biểu thức '
                 '$\\text{Tổng số lần thử} = n_1 + n_2 + \\dots + n_k$ là quy tắc hoặc công thức của mục nào '
                 'sau đây?',
            'options': ['Thống kê', 'Phân tích số', 'Quy tắc 5', 'Xác suất thực nghiệm'],
            'answer': 3,
            'solution': 'Trong Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung, biểu thức/quy tắc '
                        '$\\text{Tổng số lần thử} = n_1 + n_2 + \\dots + n_k$ chính là nội dung của **Xác '
                        'suất thực nghiệm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một lớp có $18$ học sinh nữ và $12$ học sinh nam. Phân số tối giản chỉ số học sinh nữ so '
                 'với tổng số học sinh cả lớp là:',
            'options': ['$\\dfrac{3}{5}$', '$\\dfrac{18}{12}$', '$\\dfrac{2}{5}$', '$\\dfrac{3}{2}$'],
            'answer': 0,
            'solution': 'Tổng số học sinh cả lớp là $18 + 12 = 30$. Phân số chỉ số học sinh nữ là '
                        '$\\dfrac{18}{30} = \\dfrac{3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung** (Chủ đề 13: Ôn tập cuối '
                 'năm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Đọc, viết, nêu giá trị các chữ số theo hàng của số trong phạm vi $100\\,000$.',
                        'Đọc, phân tích dãy số liệu thống kê và biểu đồ cột.',
                        'Viết được số thành tổng các chục nghìn, nghìn, trăm, chục, đơn vị.',
                        'So sánh, sắp xếp thứ tự và làm tròn số đến hàng nghìn, hàng chục nghìn.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung: '
                        'Đọc, phân tích dãy số liệu thống kê và biểu đồ cột.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: "Trên biểu đồ cột, nếu cột A cao gấp đôi cột B thì số liệu của cột A gấp $2$ '
                 'lần số liệu của cột B (khi trục đứng bắt đầu từ vạch $0$)."',
            'answer': True,
            'solution': 'Chiều cao cột tỉ lệ thuận với số liệu biểu diễn $\\rightarrow$ **Đúng**.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung**, quy tắc **Thống kê** được '
                 'xác định bởi Trung bình cộng $= \\text{Tổng số liệu} : \\text{Số các số liệu}$ và áp dụng '
                 'trực tiếp vào bài toán: “Biểu đồ cột cho biết số cây khối 4 trồng được trong $3$ ngày: '
                 'Ngày 1 ($40$ cây), Ngày 2 ($50$ cây), Ngày 3 ($60$ cây). Tính trung bình mỗi n...”. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Quy tắc **Thống kê** (Trung bình cộng $= \\text{Tổng số liệu} '
                        ': \\text{Số các số liệu}$) là kiến thức cốt lõi của Bài 72, 73: Ôn tập thống kê, '
                        'xác suất và ôn tập chung. Tổng số cây trồng trong $3$ ngày là: $40 + 50 + 60 = '
                        '150\\text{ (cây)}$. Trung bình mỗi ngày trồng được: $150 : 3 = 50\\text{ (cây)}$. '
                        'Phân số...'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung** để giải quyết '
                 'tình huống sau: Biểu đồ cột cho biết số cây khối 4 trồng được trong $3$ ngày: Ngày 1 ($40$ '
                 'cây), Ngày 2 ($50$ cây), Ngày 3 ($60$ cây). Tính trung bình mỗi ngày khối 4 trồng được bao '
                 'nhiêu cây và phân số chỉ số cây trồng Ngày 1 so với tổng số cây. Kết quả và hướng giải nào '
                 'dưới đây là **đúng**?',
            'options': ['Trong số $74\\,629$, chữ số $4$ ở hàng nghìn nên có giá trị là **$4\\,000$**. Vì '
                        'chữ số hàng trăm là $6 \\ge 5$ nên làm tròn đến hàng nghìn được **$75\\,000$**...',
                        'Thực hiện phép nhân trước: $12\\,000 \\times 4 = 48\\,000$. Thực hiện phép trừ sau: '
                        '$65\\,000 - 48\\,000 = 17\\,000$.',
                        'Tổng số cây trồng trong $3$ ngày là: $40 + 50 + 60 = 150\\text{ (cây)}$. Trung bình '
                        'mỗi ngày trồng được: $150 : 3 = 50\\text{ (cây)}$. Phân số chỉ số cây Ngà...',
                        '- Số chẵn liền sau của $1\\,998$ là: $1\\,998 + 2 = 2\\,000$. - Số lẻ liền trước '
                        'của $2\\,025$ là: $2\\,025 - 2 = 2\\,023$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 72, 73: Ôn tập thống kê, xác suất và ôn tập chung: Tổng '
                        'số cây trồng trong $3$ ngày là: $40 + 50 + 60 = 150\\text{ (cây)}$.\n'
                        'Trung bình mỗi ngày trồng được: $150 : 3 = 50\\text{ (cây)}$.\n'
                        'Phân số chỉ số cây Ngày 1 so với tổng số cây là: $\\dfrac{40}{150} = '
                        '\\dfrac{4}{15}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một kho gạo có $240$ tạ gạo. Ngày thứ nhất kho xuất đi $\\dfrac{1}{4}$ số gạo, ngày thứ '
                 'hai xuất đi $\\dfrac{1}{3}$ số gạo còn lại sau ngày thứ nhất. Hỏi sau hai ngày trong kho '
                 'còn lại bao nhiêu tạ gạo?',
            'answer': ['120'],
            'unit': 'tạ',
            'solution': 'Ngày 1 xuất: $240 \\times \\dfrac{1}{4} = 60$ (tạ), còn lại $240 - 60 = 180$ (tạ). '
                        'Ngày 2 xuất: $180 \\times \\dfrac{1}{3} = 60$ (tạ). Còn lại cuối cùng: $180 - 60 = '
                        '120$ (tạ).\n'
                        'Đáp số: **$120\\text{ tạ}$**.',
            'alt': None,
            'note': None}]}]
