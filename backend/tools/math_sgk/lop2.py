"""Dữ liệu bài học SGK Toán Lớp 2 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 2 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 2

LESSONS = [{'topic': 'l2-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 2 · Chủ đề 1: Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép '
             'cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.',
  'title': 'Bài 1: Ôn tập các số đến 100',
  'icon': '🔁',
  'description': 'Ôn tập đọc, viết, cấu tạo chục – đơn vị và so sánh, sắp xếp các số trong phạm vi 100.',
  'requirements': ['Đếm, đọc, viết được các số trong phạm vi $100$.',
                   'Phân tích được số có hai chữ số thành tổng của số chục và số đơn vị (ví dụ $47 = 40 + '
                   '7$).',
                   'So sánh và sắp xếp được các số trong phạm vi $100$.'],
  'definition': 'Mỗi **số có hai chữ số** $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị, viết thành tổng là '
                '$\\overline{ab} = a0 + b$. Ví dụ: Số $47$ gồm $4$ chục và $7$ đơn vị, viết là $47 = 40 + '
                '7$.',
  'theory': '- **Các số tròn chục:** $10, 20, 30, 40, 50, 60, 70, 80, 90$ (có chữ số hàng đơn vị bằng $0$).\n'
            '- **So sánh hai số:**\n'
            '  + Số có nhiều chữ số hơn thì lớn hơn ($100 > 99$, $25 > 9$).\n'
            '  + Hai số có hai chữ số: so sánh chữ số hàng chục trước; nếu hàng chục bằng nhau thì so sánh '
            'chữ số hàng đơn vị ($86 > 68$; $54 < 59$).',
  'formulas': [{'category': 'Cấu tạo và so sánh số đến 100',
                'items': [{'name': 'Viết thành tổng',
                           'formula': '$\\overline{ab} = a0 + b$',
                           'note': 'Ví dụ: $63 = 60 + 3$.'},
                          {'name': 'So sánh',
                           'formula': 'So sánh hàng chục trước $\\rightarrow$ hàng đơn vị sau',
                           'note': 'Ví dụ: $86 > 68$ vì $8 > 6$.'}]}],
  'example': 'Viết số $74$ thành tổng của chục và đơn vị, rồi so sánh $74$ với $47$.',
  'example_answer': 'Ta có $74 = 70 + 4$. So sánh hàng chục: $7 > 4$ nên $74 > 47$.',
  'real_life': 'Đọc số nhà, số trang sách, số ghế ngồi trong rạp hát.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số gồm $7$ chục và $4$ đơn vị là:',
            'options': ['$74$', '$47$', '$704$', '$11$'],
            'answer': 0,
            'solution': '$7$ chục là $70$, thêm $4$ đơn vị: $70 + 4 = 74$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số $63$ được viết thành tổng của số chục và số đơn vị là:',
            'options': ['$6 + 3$', '$60 + 3$', '$30 + 6$', '$60 + 30$'],
            'answer': 1,
            'solution': 'Số $63$ gồm $6$ chục ($60$) và $3$ đơn vị nên $63 = 60 + 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Ôn tập các số đến 100**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Viết thành tổng**?',
            'options': ['$\\overline{ab} = a0 - b$',
                        'Đảo ngược vế của quy tắc: $\\overline{ab} = a0 + b$',
                        '$\\overline{ab} = a0 + b$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{ab} = a0 + b$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Ôn tập các số đến 100, **Viết thành tổng** được '
                        'xác định bởi: $\\overline{ab} = a0 + b$. (Ví dụ: $63 = 60 + 3$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Ôn tập các số đến 100**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **So sánh**?',
            'options': ['So sánh hàng chục trước $\\rightarrow$ hàng đơn vị sau (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: So sánh hàng chục trước $\\rightarrow$ hàng đơn vị sau',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của So sánh hàng chục trước '
                        '$\\rightarrow$ hàng đơn vị sau',
                        'So sánh hàng chục trước $\\rightarrow$ hàng đơn vị sau'],
            'answer': 3,
            'solution': 'Trong Bài 1: Ôn tập các số đến 100, **So sánh** có công thức/quy tắc là: So sánh '
                        'hàng chục trước $\\rightarrow$ hàng đơn vị sau.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các số $58, 85, 79, 81$, số lớn nhất là:',
            'options': ['$85$', '$58$', '$79$', '$81$'],
            'answer': 0,
            'solution': 'Hai số có hàng chục lớn nhất là $85$ và $81$. Vì $5 > 1$ nên $85 > 81$. Số lớn nhất '
                        'là $85$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Ôn tập các số đến 100**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đếm, đọc, viết được các số trong phạm vi $110$.',
                        'Đếm, đọc, viết được các số trong phạm vi $100$.',
                        'Đếm, đọc, viết được các số trong phạm vi $99$.',
                        'Đếm, đọc, viết được các số trong phạm vi $102$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Ôn tập các số đến 100: Đếm, đọc, viết được các số '
                        'trong phạm vi $100$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$86 > 68$.”',
            'answer': True,
            'solution': 'So sánh hàng chục: $8 > 6$ nên $86 > 68$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 1: Ôn tập các số đến 100**, quy tắc **Viết thành tổng** được xác định bởi '
                 '$\\overline{ab} = a0 + b$ và khi áp dụng cho ví dụ “Viết số $74$ thành tổng của chục và '
                 'đơn vị, rồi so sánh $74$ với $47$.” ta có lời giải: Ta có $74 = 70 + 4$. So sánh hàng '
                 'chục: $7 > 4$ nên $74 > 47$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Viết thành tổng** ($\\overline{ab} = a0 '
                        '+ b$) và lời giải ví dụ minh họa của Bài 1: Ôn tập các số đến 100.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Ôn tập các số đến 100** để giải bài toán sau: '
                 'Viết số $74$ thành tổng của chục và đơn vị, rồi so sánh $74$ với $47$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Ta có $74 = 70 - 4$. So sánh hàng chục: $7 > 4$ nên $74 > 47$.',
                        'Ta có $74 = 70 + 4$. So sánh hàng chục: $7 > 4$ nên $74 > 46$.',
                        'Ta có $74 = 70 + 4$. So sánh hàng chục: $7 > 4$ nên $74 > 47$.',
                        'Ta có $76 = 70 + 4$. So sánh hàng chục: $7 > 4$ nên $74 > 47$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Ôn tập các số đến 100: Ta có $74 = 70 + 4$. So sánh '
                        'hàng chục: $7 > 4$ nên $74 > 47$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số lớn nhất có hai chữ số khác nhau là số nào?',
            'answer': ['98'],
            'unit': None,
            'solution': 'Hàng chục lớn nhất là $9$, hàng đơn vị lớn nhất khác $9$ là $8$. Vậy số cần tìm là '
                        '$98$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 2 · Chủ đề 1: Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép '
             'cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.',
  'title': 'Bài 2: Tia số. Số liền trước, số liền sau',
  'icon': '📏',
  'description': 'Nhận biết tia số, vị trí các số trên tia số và tìm số liền trước, số liền sau của một số.',
  'requirements': ['Nhận biết được tia số và điền được số thích hợp vào các vạch trên tia số.',
                   'Tìm được số liền trước và số liền sau của một số tự nhiên.',
                   'Hiểu rằng trên tia số, số bên trái luôn bé hơn số bên phải.'],
  'definition': '- **Tia số** là một tia có gốc tại vạch số $0$, các vạch cách đều nhau biểu diễn các số '
                'tăng dần từ trái sang phải.\n'
                '- **Số liền trước** của số $n$ (với $n > 0$) là $n - 1$.\n'
                '- **Số liền sau** của số $n$ là $n + 1$.',
  'theory': '- Trên tia số, mỗi số (khác $0$) luôn **lớn hơn** các số ở bên trái nó và **bé hơn** các số ở '
            'bên phải nó.\n'
            '- Ví dụ với số $40$: số liền trước của $40$ là $40 - 1 = 39$; số liền sau của $40$ là $40 + 1 = '
            '41$.\n'
            '- Ba số $39, 40, 41$ là **ba số tự nhiên liên tiếp**.',
  'formulas': [{'category': 'Quy tắc tia số và số liền trước – liền sau',
                'items': [{'name': 'Số liền trước của n',
                           'formula': '$n - 1$ (bé hơn $n$ là $1$ đơn vị)',
                           'note': 'Ví dụ: Liền trước của $70$ là $69$.'},
                          {'name': 'Số liền sau của n',
                           'formula': '$n + 1$ (lớn hơn $n$ là $1$ đơn vị)',
                           'note': 'Ví dụ: Liền sau của $59$ là $60$.'},
                          {'name': 'Thứ tự trên tia số', 'formula': 'Số bên trái $<$ Số bên phải'}]}],
  'example': 'Tìm số liền trước và số liền sau của số $59$.',
  'example_answer': 'Số liền trước của $59$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 + 1 = 60$.',
  'real_life': 'Xem vạch chia trên thước đo, tìm số nhà đứng liền kề trên cùng dãy phố.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền sau của số $59$ là:',
            'options': ['$58$', '$60$', '$50$', '$69$'],
            'answer': 1,
            'solution': 'Số liền sau lớn hơn $1$ đơn vị: $59 + 1 = 60$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền trước của số $70$ là:',
            'options': ['$71$', '$60$', '$69$', '$80$'],
            'answer': 2,
            'solution': 'Số liền trước bé hơn $1$ đơn vị: $70 - 1 = 69$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Tia số. Số liền trước, số liền sau**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Số liền trước của n**?',
            'options': ['$n + 1$ (bé hơn $n$ là $1$ đơn vị)',
                        '$n - 1$ (bé hơn $n$ là $2$ đơn vị)',
                        '$n - 2$ (bé hơn $n$ là $1$ đơn vị)',
                        '$n - 1$ (bé hơn $n$ là $1$ đơn vị)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Tia số. Số liền trước, số liền sau, **Số liền '
                        'trước của n** được xác định bởi: $n - 1$ (bé hơn $n$ là $1$ đơn vị). (Ví dụ: Liền '
                        'trước của $70$ là $69$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Tia số. Số liền trước, số liền sau**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Số liền sau của n**?',
            'options': ['$n + 1$ (lớn hơn $n$ là $1$ đơn vị)',
                        '$n - 1$ (lớn hơn $n$ là $1$ đơn vị)',
                        '$n + 1$ (lớn hơn $n$ là $2$ đơn vị)',
                        '$n + 2$ (lớn hơn $n$ là $1$ đơn vị)'],
            'answer': 0,
            'solution': 'Trong Bài 2: Tia số. Số liền trước, số liền sau, **Số liền sau của n** có công '
                        'thức/quy tắc là: $n + 1$ (lớn hơn $n$ là $1$ đơn vị).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trên tia số, các vạch số $30, 40, ?, 60$ cách đều nhau. Số thích hợp điền vào dấu $?$ là:',
            'options': ['$45$', '$50$', '$55$', '$41$'],
            'answer': 1,
            'solution': 'Mỗi vạch cách nhau $10$ đơn vị: $30, 40, 50, 60$. Vậy số cần điền là $50$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Tia số. Số liền trước, số liền sau**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết được tia số và điền được số thích hợp vào các vạch trên tia số. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được tia số và điền được số thích hợp vào các '
                        'vạch trên tia số.',
                        'Nhận biết được tia số và điền được số thích hợp vào các vạch trên tia số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được tia số và điền '
                        'được số thích hợp vào các vạch trên tia số.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Tia số. Số liền trước, số liền sau: Nhận biết được '
                        'tia số và điền được số thích hợp vào các vạch trên tia số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trên tia số nằm ngang, số đứng bên trái luôn lớn hơn số đứng bên phải.”',
            'answer': False,
            'solution': 'Trên tia số, các số viết tăng dần từ trái sang phải nên số bên trái luôn bé hơn số '
                        'bên phải. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 2: Tia số. Số liền trước, số liền sau**, quy tắc **Số liền trước của n** được '
                 'xác định bởi $n - 1$ (bé hơn $n$ là $1$ đơn vị) và khi áp dụng cho ví dụ “Tìm số liền '
                 'trước và số liền sau của số $59$.” ta có lời giải: Số liền trước của $59$ là $59 - 1 = '
                 '58$. Số liền sau của $59$ là $59 + 1 = 60$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số liền trước của n** ($n - 1$ (bé hơn '
                        '$n$ là $1$ đơn vị)) và lời giải ví dụ minh họa của Bài 2: Tia số. Số liền trước, số '
                        'liền sau.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Tia số. Số liền trước, số liền sau** để giải bài '
                 'toán sau: Tìm số liền trước và số liền sau của số $59$. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Số liền trước của $59$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 - 1 = 60$.',
                        'Số liền trước của $59$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 + 1 = 59$.',
                        'Số liền trước của $61$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 + 1 = 60$.',
                        'Số liền trước của $59$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 + 1 = 60$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Tia số. Số liền trước, số liền sau: Số liền trước của '
                        '$59$ là $59 - 1 = 58$. Số liền sau của $59$ là $59 + 1 = 60$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biết số liền trước của một số là $89$. Hỏi số liền sau của số đó là bao nhiêu?',
            'answer': ['91'],
            'unit': None,
            'solution': 'Số liền trước là $89$ nên số đó là $89 + 1 = 90$. Vậy số liền sau của $90$ là $90 + '
                        '1 = 91$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 2 · Chủ đề 1: Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép '
             'cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.',
  'title': 'Bài 3: Các thành phần của phép cộng, phép trừ',
  'icon': '🏷️',
  'description': 'Nhận biết tên gọi các thành phần: số hạng, tổng trong phép cộng; số bị trừ, số trừ, hiệu '
                 'trong phép trừ.',
  'requirements': ['Nhận biết và gọi đúng tên các thành phần của phép cộng: **số hạng**, **tổng**.',
                   'Nhận biết và gọi đúng tên các thành phần của phép trừ: **số bị trừ**, **số trừ**, '
                   '**hiệu**.',
                   'Tính được tổng khi biết các số hạng, tính được hiệu khi biết số bị trừ và số trừ.'],
  'definition': '- **Trong phép cộng $a + b = c$:** $a$ và $b$ gọi là **số hạng**, $c$ gọi là **tổng** (biểu '
                'thức $a + b$ cũng gọi là một tổng).\n'
                '- **Trong phép trừ $a - b = c$:** $a$ gọi là **số bị trừ**, $b$ gọi là **số trừ**, $c$ gọi '
                'là **hiệu** (biểu thức $a - b$ cũng gọi là một hiệu).',
  'theory': '- **Ví dụ phép cộng:** $25 + 13 = 38$. Trong đó $25$ và $13$ là các số hạng; $38$ là tổng.\n'
            '- **Ví dụ phép trừ:** $68 - 23 = 45$. Trong đó $68$ là số bị trừ (số ban đầu đem đi trừ), $23$ '
            'là số trừ (số bớt đi), $45$ là hiệu (kết quả còn lại).\n'
            '- **Lưu ý từ khóa:** Đề yêu cầu “Tính tổng của $a$ và $b$” tức là tính $a + b$; “Tính hiệu của '
            '$a$ và $b$” tức là tính $a - b$.',
  'formulas': [{'category': 'Tên gọi thành phần phép cộng và phép trừ',
                'items': [{'name': 'Phép cộng',
                           'formula': '$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$',
                           'note': 'Ví dụ: $42 + 15 = 57$ ($57$ là tổng).'},
                          {'name': 'Phép trừ',
                           'formula': '$\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$',
                           'note': 'Ví dụ: $68 - 23 = 45$ ($68$: số bị trừ, $23$: số trừ, $45$: hiệu).'}]}],
  'example': 'a) Tính tổng của hai số hạng $34$ và $25$.\n'
             'b) Tìm hiệu biết số bị trừ là $75$ và số trừ là $30$.',
  'example_answer': 'a) Tổng của $34$ và $25$ là: $34 + 25 = 59$.\n'
                    'b) Hiệu của $75$ và $30$ là: $75 - 30 = 45$.',
  'real_life': 'Đọc và hiểu chính xác yêu cầu của các bài toán đố, bảng thống kê tổng cộng và chênh lệch.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép cộng $42 + 15 = 57$, số $57$ được gọi là:',
            'options': ['Số hạng', 'Hiệu', 'Tổng', 'Số trừ'],
            'answer': 2,
            'solution': 'Kết quả của phép cộng được gọi là tổng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép trừ $68 - 23 = 45$, số bị trừ là số nào?',
            'options': ['$23$', '$45$', '$91$', '$68$'],
            'answer': 3,
            'solution': 'Số đứng trước dấu trừ là số bị trừ, vậy số bị trừ là $68$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Các thành phần của phép cộng, phép trừ**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Phép cộng**?',
            'options': ['$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$',
                        '$\\text{Số hạng} - \\text{Số hạng} = \\text{Tổng}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số hạng} + \\text{Số '
                        'hạng} = \\text{Tổng}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Các thành phần của phép cộng, phép trừ, **Phép '
                        'cộng** được xác định bởi: $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$. (Ví '
                        'dụ: $42 + 15 = 57$ ($57$ là tổng).)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Các thành phần của phép cộng, phép trừ**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Phép trừ**?',
            'options': ['$\\text{Số bị trừ} + \\text{Số trừ} = \\text{Hiệu}$',
                        '$\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bị trừ} - \\text{Số '
                        'trừ} = \\text{Hiệu}$'],
            'answer': 1,
            'solution': 'Trong Bài 3: Các thành phần của phép cộng, phép trừ, **Phép trừ** có công thức/quy '
                        'tắc là: $\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của hai số hạng $34$ và $25$ là:',
            'options': ['$9$', '$58$', '$59$', '$69$'],
            'answer': 2,
            'solution': 'Tổng là kết quả phép cộng: $34 + 25 = 59$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Các thành phần của phép cộng, phép trừ**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết và gọi đúng tên các thành phần của phép cộng: **số hạng**, **tổng**. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và gọi đúng tên các thành phần của phép cộng: '
                        '**số hạng**, **tổng**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và gọi đúng tên các '
                        'thành phần của phép cộng: **số hạng**, **tổng**.',
                        'Nhận biết và gọi đúng tên các thành phần của phép cộng: **số hạng**, **tổng**.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Các thành phần của phép cộng, phép trừ: Nhận biết '
                        'và gọi đúng tên các thành phần của phép cộng: **số hạng**, **tổng**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Hiệu của $75$ và $30$ là $105$.”',
            'answer': False,
            'solution': 'Hiệu là kết quả của phép trừ: $75 - 30 = 45$ (còn $105$ là tổng). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 3: Các thành phần của phép cộng, phép trừ**, quy tắc **Phép cộng** được xác '
                 'định bởi $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$ và khi áp dụng cho ví dụ “a) '
                 'Tính tổng của hai số hạng $34$ và $25$. b) Tìm hiệu biết số bị trừ là $75$ và số trừ là '
                 '$30$.” ta có lời giải: a) Tổng của $34$ và $25$ là: $34 + 25 = 59$. b) Hiệu của $75$ và '
                 '$30$ là: $75 - 30 = 45$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Phép cộng** ($\\text{Số hạng} + '
                        '\\text{Số hạng} = \\text{Tổng}$) và lời giải ví dụ minh họa của Bài 3: Các thành '
                        'phần của phép cộng, phép trừ.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Các thành phần của phép cộng, phép trừ** để giải '
                 'bài toán sau: a) Tính tổng của hai số hạng $34$ và $25$.\n'
                 'b) Tìm hiệu biết số bị trừ là $75$ và số trừ là $30$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['a) Tổng của $34$ và $25$ là: $34 + 25 = 59$. b) Hiệu của $75$ và $30$ là: $75 - 30 '
                        '= 45$.',
                        'a) Tổng của $34$ và $25$ là: $34 - 25 = 59$. b) Hiệu của $75$ và $30$ là: $75 - 30 '
                        '= 45$.',
                        'a) Tổng của $34$ và $25$ là: $34 + 25 = 59$. b) Hiệu của $75$ và $30$ là: $75 - 30 '
                        '= 44$.',
                        'a) Tổng của $68$ và $25$ là: $34 + 25 = 59$. b) Hiệu của $75$ và $30$ là: $75 - 30 '
                        '= 45$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Các thành phần của phép cộng, phép trừ: a) Tổng của '
                        '$34$ và $25$ là: $34 + 25 = 59$.\n'
                        'b) Hiệu của $75$ và $30$ là: $75 - 30 = 45$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm hiệu, biết số bị trừ là $89$ và số trừ là $42$.',
            'answer': ['47'],
            'unit': None,
            'solution': 'Ta có $\\text{Hiệu} = \\text{Số bị trừ} - \\text{Số trừ} = 89 - 42 = 47$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 2 · Chủ đề 1: Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép '
             'cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.',
  'title': 'Bài 4: Hơn, kém nhau bao nhiêu',
  'icon': '📊',
  'description': 'Cách tìm phần hơn hoặc phần kém nhau giữa hai đại lượng bằng phép trừ.',
  'requirements': ['Hiểu ý nghĩa bài toán tìm hai số hơn, kém nhau bao nhiêu đơn vị.',
                   'Biết quy tắc: lấy số lớn trừ đi số bé để tìm phần hơn (hoặc phần kém).',
                   'Trình bày hoàn chỉnh bài giải có lời văn (Lời giải, Phép tính, Đáp số).'],
  'definition': 'Muốn biết **số lớn hơn số bé bao nhiêu đơn vị** (hoặc **số bé kém số lớn bao nhiêu đơn '
                'vị**), ta luôn lấy **số lớn trừ đi số bé**.',
  'theory': '- Ví dụ: Có $7$ con thỏ và $4$ củ cà rốt. Số thỏ nhiều hơn số cà rốt là $7 - 4 = 3$ (con), và '
            'số cà rốt cũng ít hơn số thỏ là $7 - 4 = 3$ (củ).\n'
            '- **Lưu ý quan trọng:** Dù câu hỏi dùng từ “nhiều hơn bao nhiêu”, “cao hơn bao nhiêu” hay “ít '
            'hơn bao nhiêu”, “kém bao nhiêu”, khi tìm **phần chênh lệch** giữa hai số đã biết, ta đều dùng '
            '**phép trừ** ($\\text{Số lớn} - \\text{Số bé}$).',
  'formulas': [{'category': 'Bài toán hơn, kém nhau bao nhiêu',
                'items': [{'name': 'Công thức chung',
                           'formula': '$\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} - \\text{Số bé}$',
                           'note': 'Ví dụ: An $12$ tuổi, em $7$ tuổi $\\Rightarrow$ em kém An $12 - 7 = 5$ '
                                   'tuổi.'}]}],
  'example': 'Lớp 2A có $35$ bạn, lớp 2B có $32$ bạn. Hỏi lớp 2A có nhiều hơn lớp 2B bao nhiêu bạn?',
  'example_answer': 'Lớp 2A có nhiều hơn lớp 2B số bạn là:\n$35 - 32 = 3$ (bạn)\nĐáp số: $3$ bạn.',
  'real_life': 'Tính chênh lệch chiều cao, chênh lệch số tuổi giữa hai anh em, chênh lệch điểm số giữa hai '
               'đội.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Muốn biết số lớn hơn số bé bao nhiêu đơn vị, ta thực hiện phép tính gì?',
            'options': ['Lấy số lớn cộng số bé',
                        'Lấy số bé trừ số lớn',
                        'Giữ nguyên số lớn',
                        'Lấy số lớn trừ số bé'],
            'answer': 3,
            'solution': 'Để tìm phần hơn (hoặc kém) giữa hai số, ta lấy số lớn trừ đi số bé.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'An có $15$ viên bi, Bình có $10$ viên bi. An có nhiều hơn Bình số viên bi là:',
            'options': ['$5$ viên bi', '$25$ viên bi', '$15$ viên bi', '$10$ viên bi'],
            'answer': 0,
            'solution': 'Lấy số lớn trừ số bé: $15 - 10 = 5$ (viên bi).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Hơn, kém nhau bao nhiêu**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Công thức chung**?',
            'options': ['$\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} + \\text{Số bé}$',
                        '$\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} - \\text{Số bé}$',
                        'Đảo ngược vế của quy tắc: $\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} - \\text{Số '
                        'bé}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Phần hơn (hoặc kém)} = '
                        '\\text{Số lớn} - \\text{Số bé}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: Hơn, kém nhau bao nhiêu, **Công thức chung** '
                        'được xác định bởi: $\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} - \\text{Số bé}$. '
                        '(Ví dụ: An $12$ tuổi, em $7$ tuổi $\\Rightarrow$ em kém An $12 - 7 = 5$ tuổi.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo định nghĩa trong **Bài 4: Hơn, kém nhau bao nhiêu**, khẳng định nào dưới đây là '
                 '**đúng**?',
            'options': ['Muốn biết **số bé hơn số bé bao nhiêu đơn vị** (hoặc **số bé kém số lớn bao nhiêu '
                        'đơn vị**), ta luôn lấy **số lớn trừ đi số bé**.',
                        'Đảo ngược vế của quy tắc: Muốn biết **số lớn hơn số bé bao nhiêu đơn vị** (hoặc '
                        '**số bé kém số lớn bao nhiêu đơn vị**), ta luôn lấy **số lớn trừ đi số bé**.',
                        'Muốn biết **số lớn hơn số bé bao nhiêu đơn vị** (hoặc **số bé kém số lớn bao nhiêu '
                        'đơn vị**), ta luôn lấy **số lớn trừ đi số bé**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Muốn biết **số lớn hơn số bé '
                        'bao nhiêu đơn vị** (hoặc **số bé kém số lớn bao nhiêu đơn vị**), ta luôn lấy **số '
                        'lớn trừ đi số bé**.'],
            'answer': 2,
            'solution': 'Theo định nghĩa của Bài 4: Hơn, kém nhau bao nhiêu: Muốn biết **số lớn hơn số bé '
                        'bao nhiêu đơn vị** (hoặc **số bé kém số lớn bao nhiêu đơn vị**), ta luôn lấy **số '
                        'lớn trừ đi số bé**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bình cao $98\\text{ cm}$, em của Bình cao $86\\text{ cm}$. Hỏi Bình cao hơn em bao nhiêu '
                 'xăng-ti-mét?',
            'options': ['$184\\text{ cm}$', '$2\\text{ cm}$', '$14\\text{ cm}$', '$12\\text{ cm}$'],
            'answer': 3,
            'solution': 'Bình cao hơn em là: $98 - 86 = 12$ ($\\text{cm}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: Hơn, kém nhau bao nhiêu**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu ý nghĩa bài toán tìm hai số hơn, kém nhau bao nhiêu đơn vị.',
                        'Hiểu ý nghĩa bài toán tìm hai số hơn, kém nhau bao nhiêu đơn vị. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Hiểu ý nghĩa bài toán tìm hai số hơn, kém nhau bao nhiêu '
                        'đơn vị.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu ý nghĩa bài toán tìm hai '
                        'số hơn, kém nhau bao nhiêu đơn vị.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 4: Hơn, kém nhau bao nhiêu: Hiểu ý nghĩa bài toán tìm '
                        'hai số hơn, kém nhau bao nhiêu đơn vị.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Băng giấy màu xanh dài $28\\text{ cm}$, băng giấy màu đỏ dài $20\\text{ cm}$. Nhận định: '
                 '“Băng giấy màu đỏ ngắn hơn băng giấy màu xanh $8\\text{ cm}$.”',
            'answer': True,
            'solution': 'Ta có $28 - 20 = 8$ ($\\text{cm}$), nên băng giấy đỏ ngắn hơn băng giấy xanh '
                        '$8\\text{ cm}$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 4: Hơn, kém nhau bao nhiêu**, quy tắc **Công thức chung** được xác định bởi '
                 '$\\text{Phần hơn (hoặc kém)} = \\text{Số lớn} - \\text{Số bé}$ và khi áp dụng cho ví dụ '
                 '“Lớp 2A có $35$ bạn, lớp 2B có $32$ bạn. Hỏi lớp 2A có nhiều hơn lớp 2B bao nhiêu bạn?” ta '
                 'có lời giải: Lớp 2A có nhiều hơn lớp 2B số bạn là: $35 - 32 = 3$ (bạn) Đáp số: $3$ bạn.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Công thức chung** ($\\text{Phần hơn '
                        '(hoặc kém)} = \\text{Số lớn} - \\text{Số bé}$) và lời giải ví dụ minh họa của Bài '
                        '4: Hơn, kém nhau bao nhiêu.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: Hơn, kém nhau bao nhiêu** để giải bài toán sau: '
                 'Lớp 2A có $35$ bạn, lớp 2B có $32$ bạn. Hỏi lớp 2A có nhiều hơn lớp 2B bao nhiêu bạn? Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Lớp 2A có nhiều hơn lớp 2B số bạn là: $35 + 32 = 3$ (bạn) Đáp số: $3$ bạn.',
                        'Lớp 2A có nhiều hơn lớp 2B số bạn là: $35 - 32 = 3$ (bạn) Đáp số: $3$ bạn.',
                        'Lớp 2A có nhiều hơn lớp 2B số bạn là: $35 - 32 = 3$ (bạn) Đáp số: $2$ bạn.',
                        'Lớp 2A có nhiều hơn lớp 2B số bạn là: $70 - 32 = 3$ (bạn) Đáp số: $3$ bạn.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Hơn, kém nhau bao nhiêu: Lớp 2A có nhiều hơn lớp 2B '
                        'số bạn là:\n'
                        '$35 - 32 = 3$ (bạn)\n'
                        'Đáp số: $3$ bạn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mẹ năm nay $36$ tuổi, Lan $6$ tuổi. Hỏi Lan kém mẹ bao nhiêu tuổi?',
            'answer': ['30'],
            'unit': None,
            'solution': 'Số tuổi Lan kém mẹ là: $36 - 6 = 30$ (tuổi).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd01-on-tap-va-bo-sung',
  'context_title': 'Chủ đề 1: Ôn tập và bổ sung',
  'context': 'SGK Toán 2 · Chủ đề 1: Ôn các số đến 100, tia số, số liền trước – liền sau, thành phần phép '
             'cộng, phép trừ, bài toán hơn – kém nhau bao nhiêu.',
  'title': 'Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100',
  'icon': '🧮',
  'description': 'Củng cố đặt tính và tính cộng, trừ không nhớ trong phạm vi 100, tính nhẩm và giải toán.',
  'requirements': ['Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $100$.',
                   'Tính đúng biểu thức có hai dấu phép tính cộng, trừ.',
                   'Giải được các bài toán thực tế kết hợp tìm tổng, hiệu và hơn kém nhau bao nhiêu.'],
  'definition': 'Khi đặt tính phép cộng, phép trừ (không nhớ) trong phạm vi $100$, ta viết **hàng đơn vị '
                'thẳng cột hàng đơn vị, hàng chục thẳng cột hàng chục**, rồi thực hiện tính **từ phải sang '
                'trái**.',
  'theory': '- **Tính nhẩm các số tròn chục:** $40 + 50 = 90$; $80 - 30 = 50$.\n'
            '- **Tính nhẩm số có hai chữ số với số có một chữ số:** Cộng hoặc trừ ở hàng đơn vị rồi giữ '
            'nguyên hàng chục, ví dụ: $62 + 7 = 69$; $48 - 5 = 43$.\n'
            '- **Biểu thức hai dấu phép tính:** Tính lần lượt từ trái sang phải, ví dụ: $50 + 20 - 30 = 70 - '
            '30 = 40$.',
  'formulas': [{'category': 'Ôn tập cộng, trừ không nhớ phạm vi 100',
                'items': [{'name': 'Đặt tính',
                           'formula': 'Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái'},
                          {'name': 'Dãy tính 2 bước',
                           'formula': 'Thực hiện từ trái sang phải',
                           'note': 'Ví dụ: $75 - 25 + 18 = 50 + 18 = 68$.'}]}],
  'example': 'Tính: a) $43 + 26$; b) $79 - 35$; c) $60 - 20 + 15$.',
  'example_answer': 'a) $43 + 26 = 69$.\nb) $79 - 35 = 44$.\nc) $60 - 20 + 15 = 40 + 15 = 55$.',
  'real_life': 'Tính tổng tiền mua dụng cụ học tập, kiểm tra số sách trong tủ sách lớp học.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $54 + 35$ là:',
            'options': ['$89$', '$81$', '$98$', '$19$'],
            'answer': 0,
            'solution': 'Hàng đơn vị: $4 + 5 = 9$; hàng chục: $5 + 3 = 8$. Vậy $54 + 35 = 89$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $97 - 42$ là:',
            'options': ['$45$', '$55$', '$54$', '$35$'],
            'answer': 1,
            'solution': 'Hàng đơn vị: $7 - 2 = 5$; hàng chục: $9 - 4 = 5$. Vậy $97 - 42 = 55$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Đặt tính**?',
            'options': ['Đơn vị thẳng đơn vị, chục thẳng chục; tính từ trái sang phải',
                        'Đảo ngược vế của quy tắc: Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang '
                        'trái',
                        'Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đơn vị thẳng đơn vị, chục thẳng '
                        'chục; tính từ phải sang trái'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong '
                        'phạm vi 100, **Đặt tính** được xác định bởi: Đơn vị thẳng đơn vị, chục thẳng chục; '
                        'tính từ phải sang trái.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Dãy tính 2 bước**?',
            'options': ['Thực hiện từ phải sang trái',
                        'Đảo ngược vế của quy tắc: Thực hiện từ trái sang phải',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện từ trái sang phải',
                        'Thực hiện từ trái sang phải'],
            'answer': 3,
            'solution': 'Trong Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100, **Dãy tính 2 '
                        'bước** có công thức/quy tắc là: Thực hiện từ trái sang phải.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $80 - 30 + 24$ là:',
            'options': ['$74$', '$64$', '$50$', '$84$'],
            'answer': 0,
            'solution': 'Tính từ trái sang phải: $80 - 30 = 50$, sau đó $50 + 24 = 74$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi '
                 '100**, nhận định nào sau đây là **chính xác**?',
            'options': ['Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $110$.',
                        'Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $100$.',
                        'Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $99$.',
                        'Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $102$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm '
                        'vi 100: Thực hiện thành thạo phép cộng, phép trừ (không nhớ) trong phạm vi $100$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Tổng của $60$ và $8$ lớn hơn hiệu của $79$ và $10$.”',
            'answer': False,
            'solution': 'Tổng của $60$ và $8$ là $60 + 8 = 68$; hiệu của $79$ và $10$ là $79 - 10 = 69$. Vì '
                        '$68 < 69$ nên nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi 100**, quy tắc **Đặt '
                 'tính** được xác định bởi Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái và '
                 'khi áp dụng cho ví dụ “Tính: a) $43 + 26$; b) $79 - 35$; c) $60 - 20 + 15$.” ta có lời '
                 'giải: a) $43 + 26 = 69$. b) $79 - 35 = 44$. c) $60 - 20 + 15 = 40 + 15 = 55$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đặt tính** (Đơn vị thẳng đơn vị, chục '
                        'thẳng chục; tính từ phải sang trái) và lời giải ví dụ minh họa của Bài 5: Ôn tập '
                        'phép cộng, phép trừ (không nhớ) trong phạm vi 100.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong '
                 'phạm vi 100** để giải bài toán sau: Tính: a) $43 + 26$; b) $79 - 35$; c) $60 - 20 + 15$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $43 - 26 = 69$. b) $79 - 35 = 44$. c) $60 - 20 + 15 = 40 + 15 = 55$.',
                        'a) $43 + 26 = 69$. b) $79 - 35 = 44$. c) $60 - 20 + 15 = 40 + 15 = 54$.',
                        'a) $43 + 26 = 69$. b) $79 - 35 = 44$. c) $60 - 20 + 15 = 40 + 15 = 55$.',
                        'a) $86 + 26 = 69$. b) $79 - 35 = 44$. c) $60 - 20 + 15 = 40 + 15 = 55$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Ôn tập phép cộng, phép trừ (không nhớ) trong phạm vi '
                        '100: a) $43 + 26 = 69$.\n'
                        'b) $79 - 35 = 44$.\n'
                        'c) $60 - 20 + 15 = 40 + 15 = 55$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bến xe có $48$ ô tô, sau đó có $15$ ô tô rời bến. Hỏi trong bến còn lại bao nhiêu ô '
                 'tô?',
            'answer': ['33'],
            'unit': None,
            'solution': 'Số ô tô còn lại trong bến là: $48 - 15 = 33$ (ô tô).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 7: Phép cộng (qua 10) trong phạm vi 20',
  'icon': '➕',
  'description': 'Thực hiện phép cộng qua 10 trong phạm vi 20 bằng phương pháp tách số làm tròn 10.',
  'requirements': ['Hiểu cách tính cộng qua $10$ bằng phương pháp **gộp cho đủ chục ($10$) rồi cộng với số '
                   'còn lại**.',
                   'Thực hiện được các phép cộng dạng $9, 8, 7, 6$ cộng với một số qua $10$.',
                   'Vận dụng kiến thức của **Bài 7: Phép cộng (qua 10) trong phạm vi 20** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '**Phép cộng (qua $10$) trong phạm vi $20$** là phép cộng hai số có một chữ số mà tổng của '
                'chúng lớn hơn $10$ (từ $11$ đến $18$). Phương pháp tính nhanh nhất là **tách số hạng thứ '
                'hai để gộp với số hạng thứ nhất cho đủ $10$, rồi cộng tiếp phần còn lại**.',
  'theory': '- **Ví dụ 1: Tính $9 + 4$.**\n'
            '  + Tách $4 = 1 + 3$.\n'
            '  + Gộp $9 + 1 = 10$, rồi lấy $10 + 3 = 13$. Vậy $9 + 4 = 13$.\n'
            '- **Ví dụ 2: Tính $8 + 5$.**\n'
            '  + Vì $8$ cần thêm $2$ để đủ $10$, ta tách $5 = 2 + 3$.\n'
            '  + Ta có $8 + 2 = 10$, rồi $10 + 3 = 13$. Vậy $8 + 5 = 13$.\n'
            '- **Ví dụ 3: Tính $7 + 6$.**\n'
            '  + Vì $7$ cần thêm $3$ để đủ $10$, ta tách $6 = 3 + 3 \\Rightarrow 7 + 3 = 10$, $10 + 3 = 13$.',
  'formulas': [{'category': 'Quy tắc gộp đủ chục (làm tròn 10)',
                'items': [{'name': '9 cộng với một số',
                           'formula': 'Tách $1$ ở số sau để $9 + 1 = 10$',
                           'note': 'Ví dụ: $9 + 5 = 9 + 1 + 4 = 10 + 4 = 14$.'},
                          {'name': '8 cộng với một số',
                           'formula': 'Tách $2$ ở số sau để $8 + 2 = 10$',
                           'note': 'Ví dụ: $8 + 6 = 8 + 2 + 4 = 10 + 4 = 14$.'},
                          {'name': '7 cộng với một số',
                           'formula': 'Tách $3$ ở số sau để $7 + 3 = 10$',
                           'note': 'Ví dụ: $7 + 5 = 7 + 3 + 2 = 10 + 2 = 12$.'}]}],
  'example': 'Tính $8 + 7$ bằng cách tách số làm tròn $10$.',
  'example_answer': 'Tách $7 = 2 + 5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 15$.',
  'real_life': 'Tính nhẩm nhanh tổng số quả trứng khi hộp thứ nhất có $8$ quả (còn trống $2$ ô là đầy hộp '
               '$10$) và có thêm $6$ quả bên ngoài.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $8 + 6$ là:',
            'options': ['$13$', '$14$', '$15$', '$12$'],
            'answer': 1,
            'solution': 'Tách $6 = 2 + 4$. Ta có $8 + 2 = 10$, $10 + 4 = 14$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Để tính $9 + 5$ theo cách làm tròn $10$, ta tách số $5$ thành:',
            'options': ['$2$ và $3$', '$5$ và $0$', '$1$ và $4$', '$3$ và $3$'],
            'answer': 2,
            'solution': 'Vì $9$ cần thêm $1$ để được $10$ nên ta tách $5$ thành $1$ và $4$ ($9 + 1 + 4 = '
                        '14$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Phép cộng (qua 10) trong phạm vi 20**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **9 cộng với một số**?',
            'options': ['Tách $1$ ở số sau để $9 - 1 = 10$',
                        'Tách $1$ ở số sau để $9 + 1 = 9$',
                        'Tách $2$ ở số sau để $9 + 1 = 10$',
                        'Tách $1$ ở số sau để $9 + 1 = 10$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Phép cộng (qua 10) trong phạm vi 20, **9 cộng '
                        'với một số** được xác định bởi: Tách $1$ ở số sau để $9 + 1 = 10$. (Ví dụ: $9 + 5 = '
                        '9 + 1 + 4 = 10 + 4 = 14$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Phép cộng (qua 10) trong phạm vi 20**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **8 cộng với một số**?',
            'options': ['Tách $2$ ở số sau để $8 + 2 = 10$',
                        'Tách $2$ ở số sau để $8 - 2 = 10$',
                        'Tách $2$ ở số sau để $8 + 2 = 9$',
                        'Tách $4$ ở số sau để $8 + 2 = 10$'],
            'answer': 0,
            'solution': 'Trong Bài 7: Phép cộng (qua 10) trong phạm vi 20, **8 cộng với một số** có công '
                        'thức/quy tắc là: Tách $2$ ở số sau để $8 + 2 = 10$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $7 + 8$ là:',
            'options': ['$14$', '$15$', '$16$', '$13$'],
            'answer': 1,
            'solution': 'Tách $8 = 3 + 5$: $7 + 3 = 10$, $10 + 5 = 15$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Phép cộng (qua 10) trong phạm vi 20**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Hiểu cách tính cộng qua $11$ bằng phương pháp **gộp cho đủ chục ($10$) rồi cộng với '
                        'số còn lại**.',
                        'Hiểu cách tính cộng qua $10$ bằng phương pháp **gộp cho đủ chục ($9$) rồi cộng với '
                        'số còn lại**.',
                        'Hiểu cách tính cộng qua $10$ bằng phương pháp **gộp cho đủ chục ($10$) rồi cộng với '
                        'số còn lại**.',
                        'Hiểu cách tính cộng qua $20$ bằng phương pháp **gộp cho đủ chục ($10$) rồi cộng với '
                        'số còn lại**.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Phép cộng (qua 10) trong phạm vi 20: Hiểu cách '
                        'tính cộng qua $10$ bằng phương pháp **gộp cho đủ chục ($10$) rồi cộng với số còn '
                        'lại**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$6 + 5 = 12$.”',
            'answer': False,
            'solution': 'Tách $5 = 4 + 1$: $6 + 4 = 10$, $10 + 1 = 11$ (không phải $12$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 7: Phép cộng (qua 10) trong phạm vi 20**, quy tắc **9 cộng với một số** được '
                 'xác định bởi Tách $1$ ở số sau để $9 + 1 = 10$ và khi áp dụng cho ví dụ “Tính $8 + 7$ bằng '
                 'cách tách số làm tròn $10$.” ta có lời giải: Tách $7 = 2 + 5$. Ta có $8 + 2 = 10$, rồi lấy '
                 '$10 + 5 = 15$. Vậy $8 + 7 = 15$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **9 cộng với một số** (Tách $1$ ở số sau '
                        'để $9 + 1 = 10$) và lời giải ví dụ minh họa của Bài 7: Phép cộng (qua 10) trong '
                        'phạm vi 20.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Phép cộng (qua 10) trong phạm vi 20** để giải '
                 'bài toán sau: Tính $8 + 7$ bằng cách tách số làm tròn $10$. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Tách $7 = 2 - 5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 15$.',
                        'Tách $7 = 2 + 5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 14$.',
                        'Tách $14 = 2 + 5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 15$.',
                        'Tách $7 = 2 + 5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 15$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 7: Phép cộng (qua 10) trong phạm vi 20: Tách $7 = 2 + '
                        '5$. Ta có $8 + 2 = 10$, rồi lấy $10 + 5 = 15$. Vậy $8 + 7 = 15$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có một khay đựng được $10$ quả trứng, hiện trong khay đang có $8$ quả trứng. Mẹ mua thêm '
                 '$5$ quả trứng nữa. Sau khi xếp đầy khay $10$ quả thì tất cả có bao nhiêu quả trứng?',
            'answer': ['13'],
            'unit': None,
            'solution': 'Tổng số quả trứng là: $8 + 5 = 8 + 2 + 3 = 10 + 3 = 13$ (quả trứng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 8: Bảng cộng (qua 10)',
  'icon': '📋',
  'description': 'Hệ thống và ghi nhớ bảng cộng (qua 10) trong phạm vi 20; vận dụng tính chất giao hoán.',
  'requirements': ['Thuộc và vận dụng được bảng cộng (qua $10$) để tính nhẩm nhanh.',
                   'Nhận biết quy luật của các cột, các hàng trong bảng cộng.',
                   'Sử dụng tính chất đổi chỗ các số hạng ($a + b = b + a$) để nhẩm các phép cộng số bé với '
                   'số lớn.'],
  'definition': '**Bảng cộng (qua $10$)** tổng hợp các phép cộng từ $9 + 2$ đến $2 + 9$. Khi đổi chỗ hai số '
                'hạng thì tổng không thay đổi ($a + b = b + a$), ví dụ $3 + 8 = 8 + 3 = 11$.',
  'theory': '- **Các phép cộng có tổng bằng $11$:** $9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$.\n'
            '- **Các phép cộng hai số giống nhau (gấp đôi):**\n'
            '  $6 + 6 = 12$; $7 + 7 = 14$; $8 + 8 = 16$; $9 + 9 = 18$.\n'
            '- **Mẹo tính nhẩm nhanh:** Khi gặp số nhỏ cộng số lớn như $4 + 9$, ta nhẩm ngay $9 + 4 = 13$.',
  'formulas': [{'category': 'Các phép cộng trọng tâm trong Bảng cộng (qua 10)',
                'items': [{'name': 'Các tổng bằng 11', 'formula': '$9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$'},
                          {'name': 'Cặp số giống nhau',
                           'formula': '$6 + 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 18$'},
                          {'name': 'Tính chất giao hoán',
                           'formula': '$a + b = b + a$',
                           'note': 'Ví dụ: $5 + 8 = 8 + 5 = 13$.'}]}],
  'example': 'Tính nhẩm: $4 + 8$; $7 + 7$; $6 + 9$.',
  'example_answer': '- $4 + 8 = 8 + 4 = 12$.\n- $7 + 7 = 14$.\n- $6 + 9 = 9 + 6 = 15$.',
  'real_life': 'Tính nhẩm nhanh điểm số trong các trò chơi thể thao, đếm tổng số đồ vật.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bằng $11$?',
            'options': ['$9 + 3$', '$6 + 6$', '$7 + 4$', '$8 + 2$'],
            'answer': 2,
            'solution': 'Ta có $7 + 4 = 11$ (còn $9 + 3 = 12$, $6 + 6 = 12$, $8 + 2 = 10$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $8 + 8$ là:',
            'options': ['$14$', '$18$', '$15$', '$16$'],
            'answer': 3,
            'solution': 'Theo bảng cộng, $8 + 8 = 16$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Bảng cộng (qua 10)**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Các tổng bằng 11**?',
            'options': ['$9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$',
                        '$9 - 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$',
                        '$9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 10$',
                        '$18 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 8: Bảng cộng (qua 10), **Các tổng bằng 11** được '
                        'xác định bởi: $9 + 2 = 8 + 3 = 7 + 4 = 6 + 5 = 11$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Bảng cộng (qua 10)**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Cặp số giống nhau**?',
            'options': ['$6 - 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 18$',
                        '$6 + 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 18$',
                        '$6 + 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 17$',
                        '$12 + 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 18$'],
            'answer': 1,
            'solution': 'Trong Bài 8: Bảng cộng (qua 10), **Cặp số giống nhau** có công thức/quy tắc là: $6 '
                        '+ 6 = 12;\\ 7 + 7 = 14;\\ 8 + 8 = 16;\\ 9 + 9 = 18$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $6 + 7 \\dots 5 + 9$ là:',
            'options': ['$>$', '$=$', '$<$', '$+$'],
            'answer': 2,
            'solution': 'Ta có $6 + 7 = 13$ và $5 + 9 = 14$. Vì $13 < 14$ nên điền dấu $<$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 8: Bảng cộng (qua 10)**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Thuộc và vận dụng được bảng cộng (qua $11$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng (qua $9$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng (qua $20$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng (qua $10$) để tính nhẩm nhanh.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 8: Bảng cộng (qua 10): Thuộc và vận dụng được bảng '
                        'cộng (qua $10$) để tính nhẩm nhanh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$6 + 8 = 8 + 6 = 14$.”',
            'answer': True,
            'solution': 'Khi đổi chỗ hai số hạng thì tổng không đổi và đều bằng $14$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 8: Bảng cộng (qua 10)**, quy tắc **Các tổng bằng 11** được xác định bởi $9 + 2 '
                 '= 8 + 3 = 7 + 4 = 6 + 5 = 11$ và khi áp dụng cho ví dụ “Tính nhẩm: $4 + 8$; $7 + 7$; $6 + '
                 '9$.” ta có lời giải: - $4 + 8 = 8 + 4 = 12$. - $7 + 7 = 14$. - $6 + 9 = 9 + 6 = 15$.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Các tổng bằng 11** ($9 + 2 = 8 + 3 = 7 + '
                        '4 = 6 + 5 = 11$) và lời giải ví dụ minh họa của Bài 8: Bảng cộng (qua 10).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 8: Bảng cộng (qua 10)** để giải bài toán sau: Tính '
                 'nhẩm: $4 + 8$; $7 + 7$; $6 + 9$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- $4 + 8 = 8 + 4 = 12$. - $7 + 7 = 14$. - $6 + 9 = 9 + 6 = 15$.',
                        '- $4 - 8 = 8 + 4 = 12$. - $7 + 7 = 14$. - $6 + 9 = 9 + 6 = 15$.',
                        '- $4 + 8 = 8 + 4 = 12$. - $7 + 7 = 14$. - $6 + 9 = 9 + 6 = 14$.',
                        '- $8 + 8 = 8 + 4 = 12$. - $7 + 7 = 14$. - $6 + 9 = 9 + 6 = 15$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 8: Bảng cộng (qua 10): - $4 + 8 = 8 + 4 = 12$.\n'
                        '- $7 + 7 = 14$.\n'
                        '- $6 + 9 = 9 + 6 = 15$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính tổng của số lớn nhất có một chữ số và $7$.',
            'answer': ['16'],
            'unit': None,
            'solution': 'Số lớn nhất có một chữ số là $9$. Tổng của $9$ và $7$ là: $9 + 7 = 16$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 9: Bài toán về thêm, bớt một số đơn vị',
  'icon': '📝',
  'description': 'Giải bài toán có lời văn về thêm hoặc bớt một số đơn vị và cách trình bày bài giải chuẩn.',
  'requirements': ['Nhận biết dạng toán **thêm một số đơn vị** (dùng phép cộng) và **bớt một số đơn vị** '
                   '(dùng phép trừ).',
                   'Biết trình bày bài giải gồm 3 phần: Câu lời giải, Phép tính (kèm đơn vị trong ngoặc) và '
                   'Đáp số.',
                   'Vận dụng kiến thức của **Bài 9: Bài toán về thêm, bớt một số đơn vị** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '- **Bài toán về thêm một số đơn vị:** Cho biết số có ban đầu và số thêm vào, hỏi có tất cả '
                'bao nhiêu $\\rightarrow$ dùng **phép cộng**.\n'
                '- **Bài toán về bớt một số đơn vị:** Cho biết số có ban đầu và số bớt đi, hỏi còn lại bao '
                'nhiêu $\\rightarrow$ dùng **phép trừ**.',
  'theory': '- **Cách trình bày Bài giải ở lớp 2:**\n'
            '  1. Viết câu lời giải (dựa vào câu hỏi của đề bài, bỏ từ “Hỏi”, thay “bao nhiêu” bằng “số ... '
            'là:”).\n'
            '  2. Viết phép tính và ghi tên đơn vị trong dấu ngoặc đơn `(...)`.\n'
            '  3. Viết `Đáp số:` kèm theo kết quả và tên đơn vị (không có dấu ngoặc).',
  'formulas': [{'category': 'Quy tắc giải bài toán thêm, bớt',
                'items': [{'name': 'Thêm một số đơn vị',
                           'formula': '$\\text{Số có tất cả} = \\text{Số ban đầu} + \\text{Số thêm vào}$',
                           'note': 'Từ khóa: mua thêm, tặng thêm, bay tới...'},
                          {'name': 'Bớt một số đơn vị',
                           'formula': '$\\text{Số còn lại} = \\text{Số ban đầu} - \\text{Số bớt đi}$',
                           'note': 'Từ khóa: đã bán, cho đi, bay đi, ăn hết...'}]}],
  'example': 'Mai có $8$ bông hoa, bạn tặng Mai thêm $7$ bông hoa nữa. Hỏi Mai có tất cả bao nhiêu bông hoa?',
  'example_answer': 'Bài giải:\nMai có tất cả số bông hoa là:\n$8 + 7 = 15$ (bông)\nĐáp số: $15$ bông hoa.',
  'real_life': 'Tính số sách vở được thưởng thêm hoặc số tiền tiêu vặt còn lại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bài toán có từ khóa “được tặng thêm ... Hỏi có tất cả bao nhiêu” thường giải bằng phép '
                 'tính nào?',
            'options': ['Phép trừ', 'Phép nhân', 'Không cần tính', 'Phép cộng'],
            'answer': 3,
            'solution': '“Tặng thêm” và hỏi “có tất cả” là bài toán thêm một số đơn vị nên dùng phép cộng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên xe buýt có $16$ hành khách, đến trạm có $4$ hành khách xuống xe. Phép tính tìm số '
                 'hành khách còn lại trên xe là:',
            'options': ['$16 - 4 = 12$', '$16 + 4 = 20$', '$16 - 12 = 4$', '$12 + 4 = 16$'],
            'answer': 0,
            'solution': 'Khách xuống xe là bớt đi $4$ người nên ta tính: $16 - 4 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Bài toán về thêm, bớt một số đơn vị**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Thêm một số đơn vị**?',
            'options': ['$\\text{Số có tất cả} = \\text{Số ban đầu} - \\text{Số thêm vào}$',
                        '$\\text{Số có tất cả} = \\text{Số ban đầu} + \\text{Số thêm vào}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số có tất cả} = \\text{Số ban đầu} + \\text{Số '
                        'thêm vào}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số có tất cả} = '
                        '\\text{Số ban đầu} + \\text{Số thêm vào}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 9: Bài toán về thêm, bớt một số đơn vị, **Thêm một '
                        'số đơn vị** được xác định bởi: $\\text{Số có tất cả} = \\text{Số ban đầu} + '
                        '\\text{Số thêm vào}$. (Từ khóa: mua thêm, tặng thêm, bay tới...)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Bài toán về thêm, bớt một số đơn vị**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Bớt một số đơn vị**?',
            'options': ['$\\text{Số còn lại} = \\text{Số ban đầu} + \\text{Số bớt đi}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số còn lại} = \\text{Số ban đầu} - \\text{Số bớt '
                        'đi}$',
                        '$\\text{Số còn lại} = \\text{Số ban đầu} - \\text{Số bớt đi}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số còn lại} = \\text{Số '
                        'ban đầu} - \\text{Số bớt đi}$'],
            'answer': 2,
            'solution': 'Trong Bài 9: Bài toán về thêm, bớt một số đơn vị, **Bớt một số đơn vị** có công '
                        'thức/quy tắc là: $\\text{Số còn lại} = \\text{Số ban đầu} - \\text{Số bớt đi}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổ Một trồng được $9$ cây xanh, sau đó các bạn trồng thêm $6$ cây nữa. Hỏi tổ Một trồng '
                 'được tất cả bao nhiêu cây xanh?',
            'options': ['$3$ cây', '$14$ cây', '$16$ cây', '$15$ cây'],
            'answer': 3,
            'solution': 'Trồng thêm $6$ cây nên tổng số cây là: $9 + 6 = 15$ (cây).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 9: Bài toán về thêm, bớt một số đơn vị**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết dạng toán **thêm một số đơn vị** (dùng phép cộng) và **bớt một số đơn '
                        'vị** (dùng phép trừ).',
                        'Nhận biết dạng toán **thêm một số đơn vị** (dùng phép cộng) và **bớt một số đơn '
                        'vị** (dùng phép trừ). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết dạng toán **thêm một số đơn vị** (dùng phép '
                        'cộng) và **bớt một số đơn vị** (dùng phép trừ).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết dạng toán **thêm một '
                        'số đơn vị** (dùng phép cộng) và **bớt một số đơn vị** (dùng phép trừ).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 9: Bài toán về thêm, bớt một số đơn vị: Nhận biết '
                        'dạng toán **thêm một số đơn vị** (dùng phép cộng) và **bớt một số đơn vị** (dùng '
                        'phép trừ).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trong phần trình bày bài giải toán có lời văn, tên đơn vị ở dòng Đáp số không '
                 'cần viết trong dấu ngoặc đơn.”',
            'answer': True,
            'solution': 'Ở dòng phép tính đơn vị đặt trong ngoặc đơn, còn ở dòng Đáp số viết thẳng tên đơn '
                        'vị không có ngoặc. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 9: Bài toán về thêm, bớt một số đơn vị**, quy tắc **Thêm một số đơn vị** được '
                 'xác định bởi $\\text{Số có tất cả} = \\text{Số ban đầu} + \\text{Số thêm vào}$ và khi áp '
                 'dụng cho ví dụ “Mai có $8$ bông hoa, bạn tặng Mai thêm $7$ bông hoa nữa. Hỏi Mai có tất cả '
                 'bao nhiêu bông hoa?” ta có lời giải: Bài giải: Mai có tất cả số bông hoa là: $8 + 7 = 15$ '
                 '(bông) Đáp số: $15$ bông hoa.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thêm một số đơn vị** ($\\text{Số có tất '
                        'cả} = \\text{Số ban đầu} + \\text{Số thêm vào}$) và lời giải ví dụ minh họa của Bài '
                        '9: Bài toán về thêm, bớt một số đơn vị.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 9: Bài toán về thêm, bớt một số đơn vị** để giải '
                 'bài toán sau: Mai có $8$ bông hoa, bạn tặng Mai thêm $7$ bông hoa nữa. Hỏi Mai có tất cả '
                 'bao nhiêu bông hoa? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Bài giải: Mai có tất cả số bông hoa là: $8 - 7 = 15$ (bông) Đáp số: $15$ bông hoa.',
                        'Bài giải: Mai có tất cả số bông hoa là: $8 + 7 = 15$ (bông) Đáp số: $15$ bông hoa.',
                        'Bài giải: Mai có tất cả số bông hoa là: $8 + 7 = 15$ (bông) Đáp số: $14$ bông hoa.',
                        'Bài giải: Mai có tất cả số bông hoa là: $16 + 7 = 15$ (bông) Đáp số: $15$ bông '
                        'hoa.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 9: Bài toán về thêm, bớt một số đơn vị: Bài giải:\n'
                        'Mai có tất cả số bông hoa là:\n'
                        '$8 + 7 = 15$ (bông)\n'
                        'Đáp số: $15$ bông hoa.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mai có $8$ bông hoa, Mai được bạn tặng thêm $7$ bông hoa nữa. Hỏi Mai có tất cả bao nhiêu '
                 'bông hoa?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Số bông hoa Mai có tất cả là: $8 + 7 = 15$ (bông hoa).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 11: Phép trừ (qua 10) trong phạm vi 20',
  'icon': '➖',
  'description': 'Thực hiện phép trừ qua 10 trong phạm vi 20 bằng cách trừ để được 10 rồi trừ tiếp.',
  'requirements': ['Hiểu và thực hiện được phép trừ (qua $10$) trong phạm vi $20$ bằng hai cách: **trừ để '
                   'được $10$ rồi trừ số còn lại** hoặc **dựa vào phép cộng**.',
                   'Tính đúng các phép trừ có số bị trừ từ $11$ đến $18$.',
                   'Vận dụng kiến thức của **Bài 11: Phép trừ (qua 10) trong phạm vi 20** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': '**Phép trừ (qua $10$) trong phạm vi $20$** là phép trừ dạng $\\overline{1a} - b$ mà chữ số '
                'hàng đơn vị $a < b$ (ví dụ $13 - 5$). Ta tách số trừ $b$ để trừ cho tròn $10$ trước, rồi '
                'lấy $10$ trừ tiếp phần còn lại.',
  'theory': '- **Cách 1 (Trừ về $10$ rồi trừ tiếp):** Tính $13 - 5$.\n'
            '  + Để $13$ trừ về $10$ cần trừ đi $3$, nên ta tách $5 = 3 + 2$.\n'
            '  + Bước 1: $13 - 3 = 10$. Bước 2: $10 - 2 = 8$. Vậy $13 - 5 = 8$.\n'
            '- **Cách 2 (Dựa vào bảng cộng qua $10$):**\n'
            '  + Vì đã thuộc $8 + 5 = 13$ nên suy ra ngay $13 - 5 = 8$.',
  'formulas': [{'category': 'Hai cách tính trừ qua 10',
                'items': [{'name': 'Cách 1: Trừ về 10',
                           'formula': '$14 - 6 = 14 - 4 - 2 = 10 - 2 = 8$',
                           'note': 'Tách $6 = 4 + 2$ để $14 - 4 = 10$.'},
                          {'name': 'Cách 2: Dựa vào phép cộng',
                           'formula': 'Nếu $a + b = c$ thì $c - b = a$',
                           'note': 'Vì $8 + 6 = 14$ nên $14 - 6 = 8$.'}]}],
  'example': 'Tính $12 - 5$ bằng cách trừ để được $10$ rồi trừ tiếp.',
  'example_answer': 'Tách $5 = 2 + 3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.',
  'real_life': 'Tính số viên bi, số cái bánh còn lại khi có mười mấy cái và cho bạn một số cái.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Để tính $13 - 5$ bằng cách trừ về $10$, ta tách số $5$ thành:',
            'options': ['$3$ và $2$', '$1$ và $4$', '$5$ và $0$', '$2$ và $2$'],
            'answer': 0,
            'solution': 'Để $13$ giảm về $10$ cần trừ $3$, nên ta tách $5$ thành $3$ và $2$ ($13 - 3 - 2 = '
                        '8$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $15 - 7$ là:',
            'options': ['$9$', '$8$', '$7$', '$22$'],
            'answer': 1,
            'solution': 'Vì $8 + 7 = 15$ (hoặc $15 - 5 - 2 = 8$) nên $15 - 7 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Phép trừ (qua 10) trong phạm vi 20**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Cách 1: Trừ về 10**?',
            'options': ['$14 + 6 = 14 - 4 - 2 = 10 - 2 = 8$',
                        '$14 - 6 = 14 - 4 - 2 = 10 - 2 = 7$',
                        '$14 - 6 = 14 - 4 - 2 = 10 - 2 = 8$',
                        '$28 - 6 = 14 - 4 - 2 = 10 - 2 = 8$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: Phép trừ (qua 10) trong phạm vi 20, **Cách 1: '
                        'Trừ về 10** được xác định bởi: $14 - 6 = 14 - 4 - 2 = 10 - 2 = 8$. (Tách $6 = 4 + '
                        '2$ để $14 - 4 = 10$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Phép trừ (qua 10) trong phạm vi 20**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Cách 2: Dựa vào phép cộng**?',
            'options': ['Nếu $a - b = c$ thì $c - b = a$',
                        'Đảo ngược vế của quy tắc: Nếu $a + b = c$ thì $c - b = a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nếu $a + b = c$ thì $c - b = a$',
                        'Nếu $a + b = c$ thì $c - b = a$'],
            'answer': 3,
            'solution': 'Trong Bài 11: Phép trừ (qua 10) trong phạm vi 20, **Cách 2: Dựa vào phép cộng** có '
                        'công thức/quy tắc là: Nếu $a + b = c$ thì $c - b = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $11 - 4$ là:',
            'options': ['$7$', '$6$', '$8$', '$5$'],
            'answer': 0,
            'solution': 'Tách $4 = 1 + 3$: $11 - 1 = 10$, $10 - 3 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: Phép trừ (qua 10) trong phạm vi 20**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Hiểu và thực hiện được phép trừ (qua $11$) trong phạm vi $20$ bằng hai cách: **trừ '
                        'để được $10$ rồi trừ số còn lại** hoặc **dựa vào phép cộng**.',
                        'Hiểu và thực hiện được phép trừ (qua $10$) trong phạm vi $20$ bằng hai cách: **trừ '
                        'để được $10$ rồi trừ số còn lại** hoặc **dựa vào phép cộng**.',
                        'Hiểu và thực hiện được phép trừ (qua $10$) trong phạm vi $20$ bằng hai cách: **trừ '
                        'để được $9$ rồi trừ số còn lại** hoặc **dựa vào phép cộng**.',
                        'Hiểu và thực hiện được phép trừ (qua $20$) trong phạm vi $20$ bằng hai cách: **trừ '
                        'để được $10$ rồi trừ số còn lại** hoặc **dựa vào phép cộng**.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 11: Phép trừ (qua 10) trong phạm vi 20: Hiểu và thực '
                        'hiện được phép trừ (qua $10$) trong phạm vi $20$ bằng hai cách: **trừ để được $10$ '
                        'rồi trừ số còn lại** hoặc **dựa vào phép cộng**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$12 - 4 = 9$.”',
            'answer': False,
            'solution': 'Ta có $12 - 2 = 10$, $10 - 2 = 8$ nên $12 - 4 = 8$ chứ không phải $9$. Nhận định '
                        'Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 11: Phép trừ (qua 10) trong phạm vi 20**, quy tắc **Cách 1: Trừ về 10** được '
                 'xác định bởi $14 - 6 = 14 - 4 - 2 = 10 - 2 = 8$ và khi áp dụng cho ví dụ “Tính $12 - 5$ '
                 'bằng cách trừ để được $10$ rồi trừ tiếp.” ta có lời giải: Tách $5 = 2 + 3$. Ta có $12 - 2 '
                 '= 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cách 1: Trừ về 10** ($14 - 6 = 14 - 4 - '
                        '2 = 10 - 2 = 8$) và lời giải ví dụ minh họa của Bài 11: Phép trừ (qua 10) trong '
                        'phạm vi 20.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: Phép trừ (qua 10) trong phạm vi 20** để giải '
                 'bài toán sau: Tính $12 - 5$ bằng cách trừ để được $10$ rồi trừ tiếp. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Tách $5 = 2 - 3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.',
                        'Tách $5 = 2 + 3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 6$.',
                        'Tách $5 = 2 + 3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.',
                        'Tách $10 = 2 + 3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 11: Phép trừ (qua 10) trong phạm vi 20: Tách $5 = 2 + '
                        '3$. Ta có $12 - 2 = 10$, sau đó $10 - 3 = 7$. Vậy $12 - 5 = 7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hiền có $14$ chiếc nhãn vở, Hiền đã dùng hết $6$ chiếc. Hỏi Hiền còn lại bao nhiêu chiếc '
                 'nhãn vở?',
            'answer': ['8'],
            'unit': None,
            'solution': 'Số nhãn vở Hiền còn lại là: $14 - 6 = 8$ (chiếc).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 12: Bảng trừ (qua 10)',
  'icon': '📉',
  'description': 'Hệ thống và ghi nhớ bảng trừ (qua 10) trong phạm vi 20; tính dãy tính hai bước.',
  'requirements': ['Thuộc và vận dụng bảng trừ (qua $10$) để tính nhẩm nhanh.',
                   'Lập được hai phép trừ từ một phép cộng trong phạm vi $20$.',
                   'Thực hiện được dãy tính có hai dấu phép tính cộng, trừ qua $10$.'],
  'definition': '**Bảng trừ (qua $10$)** tổng hợp các phép trừ từ $11 - 2$ đến $18 - 9$. Mỗi phép cộng $a + '
                'b = c$ trong bảng cộng luôn cho ta hai phép trừ tương ứng: $c - a = b$ và $c - b = a$.',
  'theory': '- **Quy luật trong bảng trừ:**\n'
            '  + $11 - 2 = 9, 11 - 3 = 8, 11 - 4 = 7, \\dots, 11 - 9 = 2$.\n'
            '  + Các phép trừ có hiệu bằng nhau theo đường chéo: $11 - 2 = 12 - 3 = 13 - 4 = \\dots = 9$.\n'
            '- **Biểu thức có hai dấu phép tính:** Luôn thực hiện từ trái sang phải, ví dụ: $9 + 4 - 5 = 13 '
            '- 5 = 8$.',
  'formulas': [{'category': 'Liên hệ Bảng cộng – Bảng trừ qua 10',
                'items': [{'name': 'Từ cộng suy ra trừ',
                           'formula': '$a + b = c \\Rightarrow c - a = b$ và $c - b = a$',
                           'note': 'Ví dụ: $7 + 9 = 16 \\Rightarrow 16 - 7 = 9;\\ 16 - 9 = 7$.'},
                          {'name': 'Hiệu của các cặp gấp đôi',
                           'formula': '$12 - 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 9$'}]}],
  'example': 'Tính: a) $16 - 9$; b) $9 + 5 - 6$.',
  'example_answer': 'a) Vì $9 + 7 = 16$ nên $16 - 9 = 7$.\n'
                    'b) Tính từ trái sang phải: $9 + 5 = 14$, rồi $14 - 6 = 8$.',
  'real_life': 'Tính nhẩm nhanh số tiền thừa hoặc số lượng đồ vật còn thiếu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Biết $7 + 9 = 16$. Phép trừ nào dưới đây đúng?',
            'options': ['$16 - 9 = 6$', '$16 - 7 = 9$', '$9 - 7 = 16$', '$16 - 16 = 7$'],
            'answer': 1,
            'solution': 'Từ $7 + 9 = 16$ suy ra $16 - 7 = 9$ và $16 - 9 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $17 - 8$ là:',
            'options': ['$8$', '$7$', '$9$', '$6$'],
            'answer': 2,
            'solution': 'Vì $8 + 9 = 17$ nên $17 - 8 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Bảng trừ (qua 10)**, quy tắc hoặc công thức nào sau đây xác định đúng **Từ '
                 'cộng suy ra trừ**?',
            'options': ['$a - b = c \\Rightarrow c - a = b$ và $c - b = a$',
                        'Đảo ngược vế của quy tắc: $a + b = c \\Rightarrow c - a = b$ và $c - b = a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a + b = c \\Rightarrow c - a = '
                        'b$ và $c - b = a$',
                        '$a + b = c \\Rightarrow c - a = b$ và $c - b = a$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Bảng trừ (qua 10), **Từ cộng suy ra trừ** được '
                        'xác định bởi: $a + b = c \\Rightarrow c - a = b$ và $c - b = a$. (Ví dụ: $7 + 9 = '
                        '16 \\Rightarrow 16 - 7 = 9;\\ 16 - 9 = 7$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Bảng trừ (qua 10)**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Hiệu của các cặp gấp đôi**?',
            'options': ['$12 - 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 9$',
                        '$12 + 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 9$',
                        '$12 - 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 8$',
                        '$24 - 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 9$'],
            'answer': 0,
            'solution': 'Trong Bài 12: Bảng trừ (qua 10), **Hiệu của các cặp gấp đôi** có công thức/quy tắc '
                        'là: $12 - 6 = 6;\\ 14 - 7 = 7;\\ 16 - 8 = 8;\\ 18 - 9 = 9$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $9 + 4 - 5$ là:',
            'options': ['$18$', '$8$', '$0$', '$10$'],
            'answer': 1,
            'solution': 'Tính từ trái sang phải: $9 + 4 = 13$, sau đó $13 - 5 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Bảng trừ (qua 10)**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Thuộc và vận dụng bảng trừ (qua $11$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng bảng trừ (qua $9$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng bảng trừ (qua $10$) để tính nhẩm nhanh.',
                        'Thuộc và vận dụng bảng trừ (qua $20$) để tính nhẩm nhanh.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Bảng trừ (qua 10): Thuộc và vận dụng bảng trừ '
                        '(qua $10$) để tính nhẩm nhanh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Hai phép tính $14 - 5$ và $15 - 6$ có cùng kết quả bằng $9$.”',
            'answer': True,
            'solution': 'Ta có $14 - 5 = 9$ và $15 - 6 = 9$ nên hai phép tính cùng có kết quả bằng $9$. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 12: Bảng trừ (qua 10)**, quy tắc **Từ cộng suy ra trừ** được xác định bởi $a + '
                 'b = c \\Rightarrow c - a = b$ và $c - b = a$ và khi áp dụng cho ví dụ “Tính: a) $16 - 9$; '
                 'b) $9 + 5 - 6$.” ta có lời giải: a) Vì $9 + 7 = 16$ nên $16 - 9 = 7$. b) Tính từ trái sang '
                 'phải: $9 + 5 = 14$, rồi $14 - 6 = 8$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Từ cộng suy ra trừ** ($a + b = c '
                        '\\Rightarrow c - a = b$ và $c - b = a$) và lời giải ví dụ minh họa của Bài 12: Bảng '
                        'trừ (qua 10).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Bảng trừ (qua 10)** để giải bài toán sau: Tính: '
                 'a) $16 - 9$; b) $9 + 5 - 6$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) Vì $9 - 7 = 16$ nên $16 - 9 = 7$. b) Tính từ trái sang phải: $9 + 5 = 14$, rồi '
                        '$14 - 6 = 8$.',
                        'a) Vì $9 + 7 = 16$ nên $16 - 9 = 7$. b) Tính từ trái sang phải: $9 + 5 = 14$, rồi '
                        '$14 - 6 = 7$.',
                        'a) Vì $18 + 7 = 16$ nên $16 - 9 = 7$. b) Tính từ trái sang phải: $9 + 5 = 14$, rồi '
                        '$14 - 6 = 8$.',
                        'a) Vì $9 + 7 = 16$ nên $16 - 9 = 7$. b) Tính từ trái sang phải: $9 + 5 = 14$, rồi '
                        '$14 - 6 = 8$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 12: Bảng trừ (qua 10): a) Vì $9 + 7 = 16$ nên $16 - 9 = '
                        '7$.\n'
                        'b) Tính từ trái sang phải: $9 + 5 = 14$, rồi $14 - 6 = 8$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số thích hợp điền vào chỗ chấm: $16 - 8 + \\dots = 15$.',
            'answer': ['7'],
            'unit': None,
            'solution': 'Ta có $16 - 8 = 8$. Để $8 + \\dots = 15$ thì số cần điền là $15 - 8 = 7$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd02-cong-tru-pham-vi-20',
  'context_title': 'Chủ đề 2: Phép cộng, phép trừ trong phạm vi 20',
  'context': 'SGK Toán 2 · Chủ đề 2: Cộng, trừ qua 10 trong phạm vi 20, bảng cộng – bảng trừ qua 10, bài '
             'toán thêm/bớt, nhiều hơn/ít hơn một số đơn vị.',
  'title': 'Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị',
  'icon': '⚖️',
  'description': 'Giải bài toán tìm số lớn (nhiều hơn một số đơn vị) hoặc tìm số bé (ít hơn một số đơn vị).',
  'requirements': ['Giải được bài toán về **nhiều hơn một số đơn vị** (tìm số lớn bằng phép cộng).',
                   'Giải được bài toán về **ít hơn một số đơn vị** (tìm số bé bằng phép trừ).',
                   'Phân biệt rõ câu hỏi tìm số mới với câu hỏi tìm phần hơn kém.'],
  'definition': '- Khi tìm một đại lượng **nhiều hơn** đại lượng đã biết $k$ đơn vị (tức là tìm **số lớn**), '
                'ta lấy số đã biết **cộng** với $k$.\n'
                '- Khi tìm một đại lượng **ít hơn** đại lượng đã biết $k$ đơn vị (tức là tìm **số bé**), ta '
                'lấy số đã biết **trừ** đi $k$.',
  'theory': '- **Ví dụ 1 (Nhiều hơn):** Tổ Một có $9$ bạn, tổ Hai có nhiều hơn tổ Một $3$ bạn. Số bạn tổ Hai '
            'là: $9 + 3 = 12$ (bạn).\n'
            '- **Ví dụ 2 (Ít hơn):** Cành trên có $13$ con chim, cành dưới có ít hơn cành trên $5$ con. Số '
            'chim ở cành dưới là: $13 - 5 = 8$ (con).\n'
            '- **Cẩn thận tránh bẫy ngược lời văn:** Nếu đề nói “Hùng có $14$ viên bi, Hùng có **nhiều hơn** '
            'Dũng $5$ viên bi. Hỏi Dũng có mấy viên?”, thì Hùng nhiều hơn Dũng nghĩa là Dũng **ít hơn** Hùng '
            '$5$ viên, ta phải làm phép trừ $14 - 5 = 9$!',
  'formulas': [{'category': 'Công thức giải toán Nhiều hơn – Ít hơn',
                'items': [{'name': 'Tìm số lớn (nhiều hơn)',
                           'formula': '$\\text{Số lớn} = \\text{Số bé} + \\text{Phần hơn}$',
                           'note': 'Ví dụ: $9 + 3 = 12$.'},
                          {'name': 'Tìm số bé (ít hơn)',
                           'formula': '$\\text{Số bé} = \\text{Số lớn} - \\text{Phần kém}$',
                           'note': 'Ví dụ: $13 - 5 = 8$.'}]}],
  'example': 'Cành trên có $13$ con chim, cành dưới có ít hơn cành trên $5$ con chim. Hỏi cành dưới có bao '
             'nhiêu con chim?',
  'example_answer': 'Bài giải:\nCành dưới có số con chim là:\n$13 - 5 = 8$ (con)\nĐáp số: $8$ con chim.',
  'real_life': 'Tính số tuổi của anh hoặc em khi biết tuổi một người và số tuổi chênh lệch.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tổ Một có $9$ bạn, tổ Hai có nhiều hơn tổ Một $3$ bạn. Phép tính tìm số bạn của tổ Hai là:',
            'options': ['$9 - 3 = 6$', '$12 - 3 = 9$', '$9 + 3 = 12$', '$9 + 9 = 18$'],
            'answer': 2,
            'solution': 'Tổ Hai nhiều hơn tổ Một $3$ bạn nên lấy $9 + 3 = 12$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cành trên có $13$ con chim, cành dưới có ít hơn cành trên $5$ con. Hỏi cành dưới có bao '
                 'nhiêu con chim?',
            'options': ['$18$ con', '$7$ con', '$9$ con', '$8$ con'],
            'answer': 3,
            'solution': 'Cành dưới ít hơn cành trên $5$ con nên có: $13 - 5 = 8$ (con chim).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Tìm số lớn (nhiều hơn)**?',
            'options': ['$\\text{Số lớn} = \\text{Số bé} + \\text{Phần hơn}$',
                        '$\\text{Số lớn} = \\text{Số bé} - \\text{Phần hơn}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số lớn} = \\text{Số bé} + \\text{Phần hơn}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số lớn} = \\text{Số bé} '
                        '+ \\text{Phần hơn}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị, '
                        '**Tìm số lớn (nhiều hơn)** được xác định bởi: $\\text{Số lớn} = \\text{Số bé} + '
                        '\\text{Phần hơn}$. (Ví dụ: $9 + 3 = 12$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Tìm số bé (ít hơn)**?',
            'options': ['$\\text{Số bé} = \\text{Số lớn} + \\text{Phần kém}$',
                        '$\\text{Số bé} = \\text{Số lớn} - \\text{Phần kém}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số bé} = \\text{Số lớn} - \\text{Phần kém}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bé} = \\text{Số lớn} '
                        '- \\text{Phần kém}$'],
            'answer': 1,
            'solution': 'Trong Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị, **Tìm số bé (ít hơn)** '
                        'có công thức/quy tắc là: $\\text{Số bé} = \\text{Số lớn} - \\text{Phần kém}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bao thứ nhất có $15\\text{ kg}$ gạo, bao thứ nhất nặng hơn bao thứ hai $6\\text{ kg}$. Hỏi '
                 'bao thứ hai có mấy ki-lô-gam gạo?',
            'options': ['$21\\text{ kg}$', '$8\\text{ kg}$', '$9\\text{ kg}$', '$11\\text{ kg}$'],
            'answer': 2,
            'solution': 'Bao thứ nhất nặng hơn bao thứ hai $6\\text{ kg}$ nghĩa là bao thứ hai nhẹ hơn (ít '
                        'hơn) bao thứ nhất $6\\text{ kg}$: $15 - 6 = 9$ ($\\text{kg}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Giải được bài toán về **ít hơn một số đơn vị** (tìm số lớn bằng phép cộng).',
                        'Đảo ngược vế của quy tắc: Giải được bài toán về **nhiều hơn một số đơn vị** (tìm số '
                        'lớn bằng phép cộng).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải được bài toán về **nhiều '
                        'hơn một số đơn vị** (tìm số lớn bằng phép cộng).',
                        'Giải được bài toán về **nhiều hơn một số đơn vị** (tìm số lớn bằng phép cộng).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị: Giải '
                        'được bài toán về **nhiều hơn một số đơn vị** (tìm số lớn bằng phép cộng).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Anh $12$ tuổi, em ít hơn anh $4$ tuổi thì em $8$ tuổi.”',
            'answer': True,
            'solution': 'Số tuổi của em là $12 - 4 = 8$ (tuổi). Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị**, quy tắc **Tìm số lớn (nhiều '
                 'hơn)** được xác định bởi $\\text{Số lớn} = \\text{Số bé} + \\text{Phần hơn}$ và khi áp '
                 'dụng cho ví dụ “Cành trên có $13$ con chim, cành dưới có ít hơn cành trên $5$ con chim. '
                 'Hỏi cành dưới có bao nhiêu con chim?” ta có lời giải: Bài giải: Cành dưới có số con chim '
                 'là: $13 - 5 = 8$ (con) Đáp số: $8$ con chim.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tìm số lớn (nhiều hơn)** ($\\text{Số '
                        'lớn} = \\text{Số bé} + \\text{Phần hơn}$) và lời giải ví dụ minh họa của Bài 13: '
                        'Bài toán về nhiều hơn, ít hơn một số đơn vị.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị** '
                 'để giải bài toán sau: Cành trên có $13$ con chim, cành dưới có ít hơn cành trên $5$ con '
                 'chim. Hỏi cành dưới có bao nhiêu con chim? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Bài giải: Cành dưới có số con chim là: $13 - 5 = 8$ (con) Đáp số: $8$ con chim.',
                        'Bài giải: Cành dưới có số con chim là: $13 + 5 = 8$ (con) Đáp số: $8$ con chim.',
                        'Bài giải: Cành dưới có số con chim là: $13 - 5 = 8$ (con) Đáp số: $7$ con chim.',
                        'Bài giải: Cành dưới có số con chim là: $26 - 5 = 8$ (con) Đáp số: $8$ con chim.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 13: Bài toán về nhiều hơn, ít hơn một số đơn vị: Bài '
                        'giải:\n'
                        'Cành dưới có số con chim là:\n'
                        '$13 - 5 = 8$ (con)\n'
                        'Đáp số: $8$ con chim.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Nhà Lan nuôi $8$ con gà mái, số gà trống nhiều hơn số gà mái $5$ con. Hỏi nhà Lan nuôi bao '
                 'nhiêu con gà trống?',
            'answer': ['13'],
            'unit': None,
            'solution': 'Số con gà trống nhà Lan nuôi là: $8 + 5 = 13$ (con).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd03-khoi-luong-dung-tich',
  'context_title': 'Chủ đề 3: Làm quen với khối lượng, dung tích',
  'context': 'SGK Toán 2 · Chủ đề 3: Nặng hơn – nhẹ hơn, ki-lô-gam (kg), lít (l), thực hành cân, đong.',
  'title': 'Bài 15: Ki-lô-gam',
  'icon': '⚖️',
  'description': 'Nhận biết nặng hơn, nhẹ hơn và đơn vị đo khối lượng ki-lô-gam (kg).',
  'requirements': ['Nhận biết được vật nào **nặng hơn**, **nhẹ hơn** hoặc **nặng bằng nhau** thông qua cân '
                   'đĩa.',
                   'Nhận biết đơn vị đo khối lượng **ki-lô-gam** (viết tắt là $\\text{kg}$); đọc, viết và '
                   'tính toán với số đo $\\text{kg}$.',
                   'Vận dụng kiến thức của **Bài 15: Ki-lô-gam** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': '- **Ki-lô-gam** là đơn vị đo khối lượng (độ nặng, nhẹ của vật), viết tắt là $\\text{kg}$.\n'
                '- Trên **cân hai đĩa**: đĩa nào trĩu thấp xuống thì vật trên đĩa đó **nặng hơn**; nếu hai '
                'đĩa **thăng bằng** (ngang nhau) thì hai bên **nặng bằng nhau**.',
  'theory': '- **Cách đọc, viết:** $1\\text{ kg}$ đọc là một ki-lô-gam; $5\\text{ kg}$ đọc là năm '
            'ki-lô-gam.\n'
            '- **Xác định khối lượng trên cân đĩa:** Nếu đĩa bên trái đặt quả bí ngô, đĩa bên phải đặt quả '
            'cân $2\\text{ kg}$ và quả cân $1\\text{ kg}$ mà cân thăng bằng, thì quả bí ngô nặng $2\\text{ '
            'kg} + 1\\text{ kg} = 3\\text{ kg}$.\n'
            '- **Lưu ý:** Không thể chỉ nhìn kích thước to hay nhỏ để kết luận vật nào nặng hơn (quả bóng '
            'bay rất to nhưng nhẹ hơn viên bi sắt nhỏ), muốn biết chính xác phải dùng cân.',
  'formulas': [{'category': 'Đơn vị khối lượng ki-lô-gam (kg)',
                'items': [{'name': 'Ký hiệu',
                           'formula': 'Ki-lô-gam viết tắt là $\\text{kg}$',
                           'note': 'Ví dụ: $10\\text{ kg}$ đọc là mười ki-lô-gam.'},
                          {'name': 'Cân đĩa thăng bằng',
                           'formula': 'Khối lượng đĩa trái $=$ Khối lượng đĩa phải'},
                          {'name': 'Cộng, trừ khối lượng',
                           'formula': '$a\\text{ kg} \\pm b\\text{ kg} = (a \\pm b)\\text{ kg}$',
                           'note': 'Ví dụ: $15\\text{ kg} - 6\\text{ kg} = 9\\text{ kg}$.'}]}],
  'example': 'Trên cân đĩa thăng bằng, đĩa bên trái có túi đường, đĩa bên phải có quả cân $2\\text{ kg}$ và '
             'quả cân $1\\text{ kg}$. Hỏi túi đường nặng bao nhiêu ki-lô-gam?',
  'example_answer': 'Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $2\\text{ kg} + 1\\text{ '
                    'kg} = 3\\text{ kg}$.',
  'real_life': 'Cân gạo, cân hoa quả ở chợ hoặc siêu thị, theo dõi cân nặng cơ thể của em.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị đo khối lượng “ki-lô-gam” được viết tắt là:',
            'options': ['$\\text{kl}$', '$\\text{l}$', '$\\text{cm}$', '$\\text{kg}$'],
            'answer': 3,
            'solution': 'Ki-lô-gam viết tắt là $\\text{kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên cân hai đĩa, đĩa đựng quả dưa hấu thấp xuống và đĩa đựng quả cam nâng cao lên. Khi '
                 'đó:',
            'options': ['Quả dưa hấu nặng hơn quả cam',
                        'Quả dưa hấu nhẹ hơn quả cam',
                        'Hai quả nặng bằng nhau',
                        'Không so sánh được'],
            'answer': 0,
            'solution': 'Đĩa nào thấp xuống thì vật trên đĩa đó nặng hơn, nên quả dưa hấu nặng hơn quả cam.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Ki-lô-gam**, quy tắc hoặc công thức nào sau đây xác định đúng **Ký hiệu**?',
            'options': ['Ki-lô-gam viết tắt là $\\text{kg}$ (với dấu ngược lại)',
                        'Ki-lô-gam viết tắt là $\\text{kg}$',
                        'Đảo ngược vế của quy tắc: Ki-lô-gam viết tắt là $\\text{kg}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Ki-lô-gam viết tắt là '
                        '$\\text{kg}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Ki-lô-gam, **Ký hiệu** được xác định bởi: '
                        'Ki-lô-gam viết tắt là $\\text{kg}$. (Ví dụ: $10\\text{ kg}$ đọc là mười '
                        'ki-lô-gam.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Ki-lô-gam**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Cân '
                 'đĩa thăng bằng**?',
            'options': ['Khối lượng đĩa trái $=$ Khối lượng đĩa phải (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Khối lượng đĩa trái $=$ Khối lượng đĩa phải',
                        'Khối lượng đĩa trái $=$ Khối lượng đĩa phải',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Khối lượng đĩa trái $=$ Khối '
                        'lượng đĩa phải'],
            'answer': 2,
            'solution': 'Trong Bài 15: Ki-lô-gam, **Cân đĩa thăng bằng** có công thức/quy tắc là: Khối lượng '
                        'đĩa trái $=$ Khối lượng đĩa phải.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $15\\text{ kg} - 6\\text{ kg}$ là:',
            'options': ['$21\\text{ kg}$', '$9\\text{ l}$', '$11\\text{ kg}$', '$9\\text{ kg}$'],
            'answer': 3,
            'solution': 'Ta có $15 - 6 = 9$, giữ nguyên đơn vị $\\text{kg}$ được $9\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Ki-lô-gam**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được vật nào **nặng hơn**, **nhẹ hơn** hoặc **nặng bằng nhau** thông qua '
                        'cân đĩa.',
                        'Nhận biết được vật nào **nặng hơn**, **nhẹ hơn** hoặc **nặng bằng nhau** thông qua '
                        'cân đĩa. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được vật nào **nặng hơn**, **nhẹ hơn** hoặc '
                        '**nặng bằng nhau** thông qua cân đĩa.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được vật nào **nặng '
                        'hơn**, **nhẹ hơn** hoặc **nặng bằng nhau** thông qua cân đĩa.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Ki-lô-gam: Nhận biết được vật nào **nặng hơn**, '
                        '**nhẹ hơn** hoặc **nặng bằng nhau** thông qua cân đĩa.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Vật có kích thước to hơn thì luôn luôn nặng hơn vật nhỏ hơn.”',
            'answer': False,
            'solution': 'Kích thước to chưa chắc đã nặng hơn (ví dụ quả bóng bay to nhưng nhẹ hơn hòn đá '
                        'nhỏ). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 15: Ki-lô-gam**, quy tắc **Ký hiệu** được xác định bởi Ki-lô-gam viết tắt là '
                 '$\\text{kg}$ và khi áp dụng cho ví dụ “Trên cân đĩa thăng bằng, đĩa bên trái có túi đường, '
                 'đĩa bên phải có quả cân $2\\text{ kg}$ và quả cân $1\\text{ kg}$. Hỏi túi đường nặng...” '
                 'ta có lời giải: Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $2\\text{ kg} '
                 '+ 1\\text{ kg} = 3\\text{ kg}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ký hiệu** (Ki-lô-gam viết tắt là '
                        '$\\text{kg}$) và lời giải ví dụ minh họa của Bài 15: Ki-lô-gam.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Ki-lô-gam** để giải bài toán sau: Trên cân đĩa '
                 'thăng bằng, đĩa bên trái có túi đường, đĩa bên phải có quả cân $2\\text{ kg}$ và quả cân '
                 '$1\\text{ kg}$. Hỏi túi đường nặng bao nhiêu ki-lô-gam? Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $2\\text{ kg} - '
                        '1\\text{ kg} = 3\\text{ kg}$.',
                        'Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $2\\text{ kg} + '
                        '1\\text{ kg} = 3\\text{ kg}$.',
                        'Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $2\\text{ kg} + '
                        '1\\text{ kg} = 2\\text{ kg}$.',
                        'Vì cân thăng bằng nên túi đường nặng bằng tổng hai quả cân: $4\\text{ kg} + '
                        '1\\text{ kg} = 3\\text{ kg}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 15: Ki-lô-gam: Vì cân thăng bằng nên túi đường nặng bằng '
                        'tổng hai quả cân: $2\\text{ kg} + 1\\text{ kg} = 3\\text{ kg}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bao gạo nặng $25\\text{ kg}$, bao ngô nhẹ hơn bao gạo $4\\text{ kg}$. Hỏi bao ngô nặng bao '
                 'nhiêu ki-lô-gam?',
            'answer': ['21', '21kg', '21 kg'],
            'unit': None,
            'solution': 'Bao ngô nặng là: $25 - 4 = 21$ ($\\text{kg}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd03-khoi-luong-dung-tich',
  'context_title': 'Chủ đề 3: Làm quen với khối lượng, dung tích',
  'context': 'SGK Toán 2 · Chủ đề 3: Nặng hơn – nhẹ hơn, ki-lô-gam (kg), lít (l), thực hành cân, đong.',
  'title': 'Bài 16: Lít',
  'icon': '🥛',
  'description': 'Nhận biết biểu tượng dung tích (nhiều hơn, ít hơn) và đơn vị đo dung tích lít (l).',
  'requirements': ['Nhận biết đơn vị đo dung tích là **lít**, viết tắt là $\\text{l}$.',
                   'Đọc, viết và thực hiện phép cộng, phép trừ các số đo dung tích theo đơn vị $\\text{l}$.',
                   'Giải được bài toán thực tế về đong chất lỏng (nước, sữa, dầu ăn, mật ong).'],
  'definition': '**Lít** là đơn vị dùng để đo **dung tích** (sức chứa hoặc lượng chất lỏng như nước, sữa, '
                'dầu ăn, xăng), viết tắt là $\\text{l}$.',
  'theory': '- **Cách đọc, viết:** $1\\text{ l}$ đọc là một lít; $10\\text{ l}$ đọc là mười lít.\n'
            '- Để đong chất lỏng, người ta thường dùng **ca $1\\text{ l}$**, **chai $1\\text{ l}$** hoặc '
            '**can $2\\text{ l}, 5\\text{ l}$**.\n'
            '- Nếu rót hết nước từ một bình sang đầy $3$ ca $1\\text{ l}$ thì bình đó chứa $3\\text{ l}$ '
            'nước.\n'
            '- **Tính toán với đơn vị lít:** Cộng hoặc trừ các số rồi giữ nguyên đơn vị $\\text{l}$ ở kết '
            'quả.',
  'formulas': [{'category': 'Đơn vị dung tích lít (l)',
                'items': [{'name': 'Ký hiệu',
                           'formula': 'Lít viết tắt là $\\text{l}$',
                           'note': 'Ví dụ: $7\\text{ l}$ đọc là bảy lít.'},
                          {'name': 'Cộng, trừ dung tích',
                           'formula': '$a\\text{ l} \\pm b\\text{ l} = (a \\pm b)\\text{ l}$',
                           'note': 'Ví dụ: $8\\text{ l} + 5\\text{ l} = 13\\text{ l}$.'}]}],
  'example': 'Can thứ nhất đựng $8\\text{ l}$ nước, can thứ hai đựng $5\\text{ l}$ nước. Hỏi cả hai can đựng '
             'bao nhiêu lít nước?',
  'example_answer': 'Cả hai can đựng số lít nước là: $8\\text{ l} + 5\\text{ l} = 13\\text{ l}$.',
  'real_life': 'Đong nước nấu canh, mua hộp sữa tươi $1\\text{ l}$, chai dầu ăn $2\\text{ l}$ hoặc đổ xăng '
               'xe máy.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị nào dưới đây được dùng để đo lượng nước chứa trong can?',
            'options': ['Lít ($\\text{l}$)', 'Ki-lô-gam ($\\text{kg}$)', 'Xăng-ti-mét ($\\text{cm}$)', 'Giờ'],
            'answer': 0,
            'solution': 'Lượng chất lỏng (dung tích) được đo bằng đơn vị lít ($\\text{l}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo “$7\\text{ l}$” được đọc là:',
            'options': ['Bảy ki-lô-gam', 'Bảy lít', 'Bảy mét', 'Bảy xăng-ti-mét'],
            'answer': 1,
            'solution': 'Ký hiệu $\\text{l}$ là lít nên $7\\text{ l}$ đọc là bảy lít.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Lít**, quy tắc hoặc công thức nào sau đây xác định đúng **Ký hiệu**?',
            'options': ['Lít viết tắt là $\\text{l}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Lít viết tắt là $\\text{l}$',
                        'Lít viết tắt là $\\text{l}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Lít viết tắt là $\\text{l}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Lít, **Ký hiệu** được xác định bởi: Lít viết '
                        'tắt là $\\text{l}$. (Ví dụ: $7\\text{ l}$ đọc là bảy lít.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Lít**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Cộng, trừ '
                 'dung tích**?',
            'options': ['$a\\text{ l} \\pm b\\text{ l} = (a \\pm b)\\text{ l}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $a\\text{ l} \\pm b\\text{ l} = (a \\pm b)\\text{ l}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a\\text{ l} \\pm b\\text{ l} = '
                        '(a \\pm b)\\text{ l}$',
                        '$a\\text{ l} \\pm b\\text{ l} = (a \\pm b)\\text{ l}$'],
            'answer': 3,
            'solution': 'Trong Bài 16: Lít, **Cộng, trừ dung tích** có công thức/quy tắc là: $a\\text{ l} '
                        '\\pm b\\text{ l} = (a \\pm b)\\text{ l}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong thùng có $16\\text{ l}$ nước, mẹ đã lấy ra $7\\text{ l}$ nước để tưới rau. Hỏi trong '
                 'thùng còn lại bao nhiêu lít nước?',
            'options': ['$9\\text{ l}$', '$23\\text{ l}$', '$8\\text{ l}$', '$7\\text{ l}$'],
            'answer': 0,
            'solution': 'Lấy ra $7\\text{ l}$ là bớt đi: $16\\text{ l} - 7\\text{ l} = 9\\text{ l}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Lít**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết đơn vị đo dung tích là **lít**, viết tắt là $\\text{l}$. (với dấu ngược '
                        'lại)',
                        'Nhận biết đơn vị đo dung tích là **lít**, viết tắt là $\\text{l}$.',
                        'Đảo ngược vế của quy tắc: Nhận biết đơn vị đo dung tích là **lít**, viết tắt là '
                        '$\\text{l}$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết đơn vị đo dung tích '
                        'là **lít**, viết tắt là $\\text{l}$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Lít: Nhận biết đơn vị đo dung tích là **lít**, '
                        'viết tắt là $\\text{l}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$4\\text{ l} + 9\\text{ l} = 13\\text{ l}$.”',
            'answer': True,
            'solution': 'Ta có $4 + 9 = 13$, giữ nguyên đơn vị $\\text{l}$ là $13\\text{ l}$. Nhận định '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 16: Lít**, quy tắc **Ký hiệu** được xác định bởi Lít viết tắt là $\\text{l}$ '
                 'và khi áp dụng cho ví dụ “Can thứ nhất đựng $8\\text{ l}$ nước, can thứ hai đựng $5\\text{ '
                 'l}$ nước. Hỏi cả hai can đựng bao nhiêu lít nước?” ta có lời giải: Cả hai can đựng số lít '
                 'nước là: $8\\text{ l} + 5\\text{ l} = 13\\text{ l}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ký hiệu** (Lít viết tắt là $\\text{l}$) '
                        'và lời giải ví dụ minh họa của Bài 16: Lít.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Lít** để giải bài toán sau: Can thứ nhất đựng '
                 '$8\\text{ l}$ nước, can thứ hai đựng $5\\text{ l}$ nước. Hỏi cả hai can đựng bao nhiêu lít '
                 'nước? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Cả hai can đựng số lít nước là: $8\\text{ l} - 5\\text{ l} = 13\\text{ l}$.',
                        'Cả hai can đựng số lít nước là: $8\\text{ l} + 5\\text{ l} = 12\\text{ l}$.',
                        'Cả hai can đựng số lít nước là: $8\\text{ l} + 5\\text{ l} = 13\\text{ l}$.',
                        'Cả hai can đựng số lít nước là: $16\\text{ l} + 5\\text{ l} = 13\\text{ l}$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 16: Lít: Cả hai can đựng số lít nước là: $8\\text{ l} + '
                        '5\\text{ l} = 13\\text{ l}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rót hết nước từ một cái xô ra đầy $1$ can $5\\text{ l}$ và $1$ can $3\\text{ l}$. Hỏi lúc '
                 'đầu trong xô có bao nhiêu lít nước?',
            'answer': ['8', '8l', '8 l'],
            'unit': None,
            'solution': 'Lượng nước lúc đầu trong xô là: $5 + 3 = 8$ ($\\text{l}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd03-khoi-luong-dung-tich',
  'context_title': 'Chủ đề 3: Làm quen với khối lượng, dung tích',
  'context': 'SGK Toán 2 · Chủ đề 3: Nặng hơn – nhẹ hơn, ki-lô-gam (kg), lít (l), thực hành cân, đong.',
  'title': 'Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít',
  'icon': '🧪',
  'description': 'Thực hành cân đồ vật, đong nước, ước lượng khối lượng – dung tích và giải bài toán thực '
                 'tế.',
  'requirements': ['Phân biệt đúng trường hợp dùng đơn vị khối lượng ($\\text{kg}$) và đơn vị dung tích '
                   '($\\text{l}$).',
                   'Biết đọc vạch số trên cân đồng hồ và tổng hợp các quả cân trên cân đĩa.',
                   'Giải được bài toán có lời văn liên quan đến $\\text{kg}$ và $\\text{l}$.'],
  'definition': '- Dùng **ki-lô-gam ($\\text{kg}$)** khi nói về độ nặng của vật (cân gạo, cân thịt, cân nặng '
                'của người).\n'
                '- Dùng **lít ($\\text{l}$)** khi nói về lượng chất lỏng (đong nước, sữa, mật ong, xăng '
                'dầu).\n'
                '- Chỉ thực hiện cộng, trừ hai số đo khi chúng có **cùng một đơn vị đo**.',
  'theory': '- **Trên cân đồng hồ:** Kim của cân chỉ vào vạch số mấy thì vật trên đĩa cân nặng bấy nhiêu '
            'ki-lô-gam.\n'
            '- **Bài toán đong nước nhiều lần:** Nếu dùng ca $2\\text{ l}$ múc đầy $3$ lần đổ vào bình thì '
            'bình có $2\\text{ l} + 2\\text{ l} + 2\\text{ l} = 6\\text{ l}$ nước.\n'
            '- **Lưu ý:** Không thể cộng một số đo đơn vị $\\text{kg}$ với một số đo đơn vị $\\text{l}$.',
  'formulas': [{'category': 'Quy tắc tính toán với đơn vị đo',
                'items': [{'name': 'Cùng đơn vị',
                           'formula': 'Chỉ cộng hoặc trừ các số đo có cùng đơn vị ($\\text{kg}$ với '
                                      '$\\text{kg}$, $\\text{l}$ với $\\text{l}$)'},
                          {'name': 'Cân đồng hồ',
                           'formula': 'Kim cân chỉ số $k \\Rightarrow$ vật nặng $k\\text{ kg}$'}]}],
  'example': 'Con gà cân nặng $3\\text{ kg}$, con vịt cân nặng $2\\text{ kg}$, con ngỗng nặng bằng cả con gà '
             'và con vịt gộp lại. Hỏi con ngỗng nặng mấy ki-lô-gam?',
  'example_answer': 'Con ngỗng cân nặng là: $3\\text{ kg} + 2\\text{ kg} = 5\\text{ kg}$.',
  'real_life': 'Ước lượng cân nặng của cặp sách đi học, lượng nước uống cần thiết mỗi ngày (khoảng $1\\text{ '
               'l}$ đến $2\\text{ l}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đặt một quả mít lên cân đồng hồ, kim cân chỉ đúng vạch số $6$. Quả mít đó cân nặng:',
            'options': ['$6\\text{ l}$', '$6\\text{ kg}$', '$6\\text{ cm}$', '$16\\text{ kg}$'],
            'answer': 1,
            'solution': 'Cân đồng hồ đo khối lượng theo đơn vị $\\text{kg}$, kim chỉ số $6$ nên quả mít nặng '
                        '$6\\text{ kg}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dùng ca $1\\text{ l}$ múc đầy $5$ ca nước đổ vào bình (không bị tràn). Khi đó trong bình '
                 'có:',
            'options': ['$1\\text{ l}$ nước',
                        '$5\\text{ kg}$ nước',
                        '$5\\text{ l}$ nước',
                        '$6\\text{ l}$ nước'],
            'answer': 2,
            'solution': 'Mỗi ca là $1\\text{ l}$, $5$ ca như vậy có $5\\text{ l}$ nước.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Cùng đơn vị**?',
            'options': ['Chỉ cộng hoặc trừ các số đo có cùng đơn vị ($\\text{kg}$ với $\\text{kg}$, '
                        '$\\text{l}$ với $\\text{l}$) (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Chỉ cộng hoặc trừ các số đo có cùng đơn vị ($\\text{kg}$ '
                        'với $\\text{kg}$, $\\text{l}$ với $\\text{l}$)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chỉ cộng hoặc trừ các số đo có '
                        'cùng đơn vị ($\\text{kg}$ với $\\text{kg}$, $\\text{l}$ với $\\text{l}$)',
                        'Chỉ cộng hoặc trừ các số đo có cùng đơn vị ($\\text{kg}$ với $\\text{kg}$, '
                        '$\\text{l}$ với $\\text{l}$)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Thực hành và trải nghiệm với các đơn vị '
                        'ki-lô-gam, lít, **Cùng đơn vị** được xác định bởi: Chỉ cộng hoặc trừ các số đo có '
                        'cùng đơn vị ($\\text{kg}$ với $\\text{kg}$, $\\text{l}$ với $\\text{l}$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít**, biểu thức hoặc '
                 'quy tắc nào dưới đây biểu diễn đúng **Cân đồng hồ**?',
            'options': ['Kim cân chỉ số $k \\Rightarrow$ vật nặng $k\\text{ kg}$',
                        'Kim cân chỉ số $k \\Rightarrow$ vật nặng $k\\text{ kg}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Kim cân chỉ số $k \\Rightarrow$ vật nặng $k\\text{ kg}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Kim cân chỉ số $k \\Rightarrow$ '
                        'vật nặng $k\\text{ kg}$'],
            'answer': 0,
            'solution': 'Trong Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít, **Cân đồng '
                        'hồ** có công thức/quy tắc là: Kim cân chỉ số $k \\Rightarrow$ vật nặng $k\\text{ '
                        'kg}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Can đỏ đựng $10\\text{ l}$ dầu, can xanh đựng ít hơn can đỏ $3\\text{ l}$ dầu. Hỏi cả hai '
                 'can đựng bao nhiêu lít dầu?',
            'options': ['$7\\text{ l}$', '$17\\text{ l}$', '$13\\text{ l}$', '$23\\text{ l}$'],
            'answer': 1,
            'solution': 'Can xanh đựng: $10 - 3 = 7$ ($\\text{l}$). Cả hai can đựng: $10 + 7 = 17$ '
                        '($\\text{l}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, '
                 'lít**, nhận định nào sau đây là **chính xác**?',
            'options': ['Phân biệt đúng trường hợp dùng đơn vị khối lượng ($\\text{kg}$) và đơn vị dung tích '
                        '($\\text{l}$). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Phân biệt đúng trường hợp dùng đơn vị khối lượng '
                        '($\\text{kg}$) và đơn vị dung tích ($\\text{l}$).',
                        'Phân biệt đúng trường hợp dùng đơn vị khối lượng ($\\text{kg}$) và đơn vị dung tích '
                        '($\\text{l}$).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phân biệt đúng trường hợp dùng '
                        'đơn vị khối lượng ($\\text{kg}$) và đơn vị dung tích ($\\text{l}$).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Thực hành và trải nghiệm với các đơn vị '
                        'ki-lô-gam, lít: Phân biệt đúng trường hợp dùng đơn vị khối lượng ($\\text{kg}$) và '
                        'đơn vị dung tích ($\\text{l}$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$36\\text{ kg} + 9\\text{ kg} = 45\\text{ l}$.”',
            'answer': False,
            'solution': 'Tổng của hai số đo đơn vị $\\text{kg}$ phải có đơn vị là $\\text{kg}$ ($45\\text{ '
                        'kg}$), không thể đổi thành đơn vị lít ($\\text{l}$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, lít**, quy tắc **Cùng '
                 'đơn vị** được xác định bởi Chỉ cộng hoặc trừ các số đo có cùng đơn vị ($\\text{kg}$ với '
                 '$\\text{kg}$, $\\text{l}$ với $\\text{l}$) và khi áp dụng cho ví dụ “Con gà cân nặng '
                 '$3\\text{ kg}$, con vịt cân nặng $2\\text{ kg}$, con ngỗng nặng bằng cả con gà và con vịt '
                 'gộp lại. Hỏi con ngỗng nặng mấy...” ta có lời giải: Con ngỗng cân nặng là: $3\\text{ kg} + '
                 '2\\text{ kg} = 5\\text{ kg}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cùng đơn vị** (Chỉ cộng hoặc trừ các số '
                        'đo có cùng đơn vị ($\\text{kg}$ với $\\text{kg}$, $\\text{l}$ với $\\text{l}$)) và '
                        'lời giải ví dụ minh họa của Bài 17: Thực hành và trải nghiệm với các đơn vị '
                        'ki-lô-gam, lít.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Thực hành và trải nghiệm với các đơn vị '
                 'ki-lô-gam, lít** để giải bài toán sau: Con gà cân nặng $3\\text{ kg}$, con vịt cân nặng '
                 '$2\\text{ kg}$, con ngỗng nặng bằng cả con gà và con vịt gộp lại. Hỏi con ngỗng nặng mấy '
                 'ki-lô-gam? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Con ngỗng cân nặng là: $3\\text{ kg} - 2\\text{ kg} = 5\\text{ kg}$.',
                        'Con ngỗng cân nặng là: $3\\text{ kg} + 2\\text{ kg} = 4\\text{ kg}$.',
                        'Con ngỗng cân nặng là: $6\\text{ kg} + 2\\text{ kg} = 5\\text{ kg}$.',
                        'Con ngỗng cân nặng là: $3\\text{ kg} + 2\\text{ kg} = 5\\text{ kg}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 17: Thực hành và trải nghiệm với các đơn vị ki-lô-gam, '
                        'lít: Con ngỗng cân nặng là: $3\\text{ kg} + 2\\text{ kg} = 5\\text{ kg}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bình có một can $12\\text{ l}$ đang chứa đầy nước. Bình rót nước từ can đó vào đầy một '
                 'bình $4\\text{ l}$ và một chai $2\\text{ l}$. Hỏi trong can còn lại bao nhiêu lít nước?',
            'answer': ['6', '6l', '6 l'],
            'unit': None,
            'solution': 'Sau hai lần rót, số lít nước còn lại trong can là: $12 - 4 - 2 = 6$ ($\\text{l}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd04-cong-tru-co-nho-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép cộng, phép trừ (có nhớ) trong phạm vi 100',
  'context': 'SGK Toán 2 · Chủ đề 4: Cộng, trừ có nhớ số có hai chữ số với số có một hoặc hai chữ số.',
  'title': 'Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số',
  'icon': '🧮',
  'description': 'Đặt tính và tính phép cộng (có nhớ) số có hai chữ số với số có một chữ số.',
  'requirements': ['Đặt tính đúng: số có một chữ số viết thẳng cột với hàng đơn vị của số có hai chữ số.',
                   'Thực hiện cộng từ phải sang trái: khi hàng đơn vị cộng lại từ $10$ trở lên, viết chữ số '
                   'hàng đơn vị và **nhớ $1$ sang hàng chục**.',
                   'Vận dụng kiến thức của **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ '
                   'số** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi cộng số có hai chữ số với số có một chữ số mà tổng ở hàng đơn vị từ $10$ trở lên, ta '
                '**viết chữ số đơn vị** của kết quả đó và **nhớ $1$ chục** cộng thêm vào chữ số hàng chục.',
  'theory': '- **Ví dụ 1: Tính $37 + 5$.**\n'
            '  + Hàng đơn vị: $7 + 5 = 12$, viết $2$ **nhớ $1$**.\n'
            '  + Hàng chục: $3$ thêm $1$ bằng $4$, viết $4$.\n'
            '  + Vậy $37 + 5 = 42$.\n'
            '- **Ví dụ 2 (Tổng tròn chục): Tính $24 + 6$.**\n'
            '  + Hàng đơn vị: $4 + 6 = 10$, viết $0$ **nhớ $1$**.\n'
            '  + Hàng chục: $2$ thêm $1$ bằng $3$, viết $3$. Vậy $24 + 6 = 30$.',
  'formulas': [{'category': 'Quy tắc cộng có nhớ (2 chữ số + 1 chữ số)',
                'items': [{'name': 'Bước 1 (Hàng đơn vị)',
                           'formula': 'Cộng hai chữ số đơn vị được $\\overline{1c} \\rightarrow$ viết $c$, '
                                      'nhớ $1$'},
                          {'name': 'Bước 2 (Hàng chục)',
                           'formula': 'Lấy chữ số hàng chục thêm $1$ (đã nhớ) rồi viết vào hàng chục',
                           'note': 'Ví dụ: $58 + 7 = 65$ ($8 + 7 = 15$ viết $5$ nhớ $1$; $5 + 1 = 6$).'}]}],
  'example': 'Đặt tính rồi tính: a) $36 + 8$; b) $45 + 5$.',
  'example_answer': 'a) $6 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 = 44$.\n'
                    'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = 50$.',
  'real_life': 'Tính tổng số sách trên giá khi có $47$ quyển và mua thêm $6$ quyển.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $36 + 8$ là:',
            'options': ['$34$', '$116$', '$44$', '$43$'],
            'answer': 2,
            'solution': 'Hàng đơn vị: $6 + 8 = 14$, viết $4$ nhớ $1$; hàng chục: $3 + 1 = 4$. Vậy $36 + 8 = '
                        '44$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $53 + 7$ là:',
            'options': ['$50$', '$510$', '$61$', '$60$'],
            'answer': 3,
            'solution': 'Hàng đơn vị: $3 + 7 = 10$, viết $0$ nhớ $1$; hàng chục: $5 + 1 = 6$. Vậy $53 + 7 = '
                        '60$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Bước 1 (Hàng đơn vị)**?',
            'options': ['Cộng hai chữ số đơn vị được $\\overline{1c} \\rightarrow$ viết $c$, nhớ $1$',
                        'Cộng hai chữ số đơn vị được $\\overline{1c} \\rightarrow$ viết $c$, nhớ $2$',
                        'Lấy chữ số hàng chục thêm $1$ (đã nhớ) rồi viết vào hàng chục',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có '
                        'một chữ số, **Bước 1 (Hàng đơn vị)** được xác định bởi: Cộng hai chữ số đơn vị được '
                        '$\\overline{1c} \\rightarrow$ viết $c$, nhớ $1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Bước 2 (Hàng chục)**?',
            'options': ['Lấy chữ số hàng chục thêm $2$ (đã nhớ) rồi viết vào hàng chục',
                        'Lấy chữ số hàng chục thêm $1$ (đã nhớ) rồi viết vào hàng chục',
                        'Cộng hai chữ số đơn vị được $\\overline{1c} \\rightarrow$ viết $c$, nhớ $1$',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 1,
            'solution': 'Trong Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số, **Bước 2 '
                        '(Hàng chục)** có công thức/quy tắc là: Lấy chữ số hàng chục thêm $1$ (đã nhớ) rồi '
                        'viết vào hàng chục.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi đặt tính phép cộng $65 + 9$, sau khi tính $5 + 9 = 14$ (viết $4$ nhớ $1$), ở hàng chục '
                 'ta tính như thế nào?',
            'options': ['Giữ nguyên $6$',
                        'Lấy $6$ trừ $1$ bằng $5$',
                        'Lấy $6$ thêm $1$ bằng $7$',
                        'Lấy $6$ cộng $4$ bằng $10$'],
            'answer': 2,
            'solution': 'Có nhớ $1$ chục từ hàng đơn vị sang nên ở hàng chục ta lấy $6$ thêm $1$ bằng $7$ '
                        '($65 + 9 = 74$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ '
                 'số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Đặt tính đúng: số có một chữ số viết thẳng cột với hàng đơn vị của số có hai chữ '
                        'số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đặt tính đúng: số có một chữ số viết thẳng cột với hàng '
                        'đơn vị của số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt tính đúng: số có một chữ số '
                        'viết thẳng cột với hàng đơn vị của số có hai chữ số.',
                        'Đặt tính đúng: số có một chữ số viết thẳng cột với hàng đơn vị của số có hai chữ '
                        'số.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một '
                        'chữ số: Đặt tính đúng: số có một chữ số viết thẳng cột với hàng đơn vị của số có '
                        'hai chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$78 + 6 = 74$.”',
            'answer': False,
            'solution': 'Hàng đơn vị $8 + 6 = 14$ viết $4$ nhớ $1$, hàng chục $7 + 1 = 8$ nên $78 + 6 = 84$ '
                        '(quên nhớ $1$ mới ra $74$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số**, quy tắc **Bước '
                 '1 (Hàng đơn vị)** được xác định bởi Cộng hai chữ số đơn vị được $\\overline{1c} '
                 '\\rightarrow$ viết $c$, nhớ $1$ và khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $36 + 8$; '
                 'b) $45 + 5$.” ta có lời giải: a) $6 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 '
                 '\\Rightarrow 36 + 8 = 44$. b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng.... Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Bước 1 (Hàng đơn vị)** (Cộng hai chữ số '
                        'đơn vị được $\\overline{1c} \\rightarrow$ viết $c$, nhớ $1$) và lời giải ví dụ minh '
                        'họa của Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có '
                 'một chữ số** để giải bài toán sau: Đặt tính rồi tính: a) $36 + 8$; b) $45 + 5$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $6 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 = 44$. '
                        'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = '
                        '50$...',
                        'a) $6 - 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 = 44$. '
                        'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = '
                        '50$...',
                        'a) $6 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 = 44$. '
                        'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = '
                        '49$...',
                        'a) $12 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 = 44$. '
                        'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = '
                        '50$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Phép cộng (có nhớ) số có hai chữ số với số có một '
                        'chữ số: a) $6 + 8 = 14$, viết $4$ nhớ $1$; $3$ thêm $1$ bằng $4 \\Rightarrow 36 + 8 '
                        '= 44$.\n'
                        'b) $5 + 5 = 10$, viết $0$ nhớ $1$; $4$ thêm $1$ bằng $5 \\Rightarrow 45 + 5 = 50$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Sợi dây thứ nhất dài $48\\text{ cm}$, sợi dây thứ hai dài hơn sợi dây thứ nhất $7\\text{ '
                 'cm}$. Hỏi sợi dây thứ hai dài bao nhiêu xăng-ti-mét?',
            'answer': ['55', '55cm', '55 cm'],
            'unit': None,
            'solution': 'Độ dài sợi dây thứ hai là: $48 + 7 = 55$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd04-cong-tru-co-nho-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép cộng, phép trừ (có nhớ) trong phạm vi 100',
  'context': 'SGK Toán 2 · Chủ đề 4: Cộng, trừ có nhớ số có hai chữ số với số có một hoặc hai chữ số.',
  'title': 'Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số',
  'icon': '➕',
  'description': 'Đặt tính và tính phép cộng (có nhớ) hai số có hai chữ số trong phạm vi 100.',
  'requirements': ['Đặt tính thẳng cột và thực hiện đúng phép cộng (có nhớ) hai số có hai chữ số.',
                   'Nhận biết trường hợp hai số có hai chữ số cộng lại bằng $100$ (ví dụ $65 + 35 = 100$).',
                   'Giải được bài toán thực tế có phép cộng (có nhớ) hai số có hai chữ số.'],
  'definition': 'Khi cộng hai số có hai chữ số mà hàng đơn vị có tổng từ $10$ trở lên, ta **viết chữ số hàng '
                'đơn vị** và **nhớ $1$** vào tổng của hai chữ số hàng chục.',
  'theory': '- **Ví dụ 1: Tính $46 + 28$.**\n'
            '  + Hàng đơn vị: $6 + 8 = 14$, viết $4$ **nhớ $1$**.\n'
            '  + Hàng chục: $4 + 2 = 6$, thêm $1$ bằng $7$, viết $7$.\n'
            '  + Vậy $46 + 28 = 74$.\n'
            '- **Ví dụ 2 (Tổng bằng $100$): Tính $73 + 27$.**\n'
            '  + Hàng đơn vị: $3 + 7 = 10$, viết $0$ nhớ $1$.\n'
            '  + Hàng chục: $7 + 2 = 9$, thêm $1$ bằng $10$, viết $10$. Vậy $73 + 27 = 100$.',
  'formulas': [{'category': 'Quy tắc cộng có nhớ hai số có hai chữ số',
                'items': [{'name': 'Thứ tự đặt tính và tính',
                           'formula': 'Đặt thẳng cột; tính từ phải sang trái (hàng đơn vị trước)'},
                          {'name': 'Nhớ 1 sang hàng chục',
                           'formula': 'Đơn vị cộng lại $\\ge 10 \\rightarrow$ viết chữ số đơn vị, cộng thêm '
                                      '$1$ vào hàng chục',
                           'note': 'Ví dụ: $29 + 47 = 76$.'}]}],
  'example': 'Đặt tính rồi tính: a) $37 + 25$; b) $58 + 26$.',
  'example_answer': 'a) $7 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + 25 = '
                    '62$.\n'
                    'b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $1$ bằng $8 \\Rightarrow 58 + 26 = '
                    '84$.',
  'real_life': 'Tính tổng số học sinh nam và nữ của cả khối lớp Hai.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đặt tính phép cộng hai số có hai chữ số, ta bắt đầu tính từ hàng nào trước?',
            'options': ['Từ trái sang phải (hàng chục trước)',
                        'Tính hàng nào trước cũng được',
                        'Chỉ cộng hàng chục',
                        'Từ phải sang trái (hàng đơn vị trước)'],
            'answer': 3,
            'solution': 'Ta luôn tính từ phải sang trái (từ hàng đơn vị trước) để nếu tổng đơn vị từ $10$ '
                        'trở lên thì nhớ $1$ sang hàng chục.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $29 + 47$ là:',
            'options': ['$76$', '$66$', '$616$', '$75$'],
            'answer': 0,
            'solution': 'Hàng đơn vị: $9 + 7 = 16$, viết $6$ nhớ $1$; hàng chục: $2 + 4 + 1 = 7$. Vậy $29 + '
                        '47 = 76$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Thứ tự đặt tính và tính**?',
            'options': ['Đặt thẳng cột; tính từ trái sang phải (hàng đơn vị trước)',
                        'Đặt thẳng cột; tính từ phải sang trái (hàng đơn vị trước)',
                        'Đảo ngược vế của quy tắc: Đặt thẳng cột; tính từ phải sang trái (hàng đơn vị trước)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt thẳng cột; tính từ phải '
                        'sang trái (hàng đơn vị trước)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có '
                        'hai chữ số, **Thứ tự đặt tính và tính** được xác định bởi: Đặt thẳng cột; tính từ '
                        'phải sang trái (hàng đơn vị trước).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Nhớ 1 sang hàng chục**?',
            'options': ['Đơn vị cộng lại $\\le 10 \\rightarrow$ viết chữ số đơn vị, cộng thêm $1$ vào hàng '
                        'chục',
                        'Đơn vị cộng lại $\\ge 10 \\rightarrow$ viết chữ số đơn vị, cộng thêm $2$ vào hàng '
                        'chục',
                        'Đơn vị cộng lại $\\ge 10 \\rightarrow$ viết chữ số đơn vị, cộng thêm $1$ vào hàng '
                        'chục',
                        'Đơn vị cộng lại $\\ge 20 \\rightarrow$ viết chữ số đơn vị, cộng thêm $1$ vào hàng '
                        'chục'],
            'answer': 2,
            'solution': 'Trong Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số, **Nhớ 1 '
                        'sang hàng chục** có công thức/quy tắc là: Đơn vị cộng lại $\\ge 10 \\rightarrow$ '
                        'viết chữ số đơn vị, cộng thêm $1$ vào hàng chục.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một cửa hàng buổi sáng bán được $46\\text{ l}$ dầu, buổi chiều bán được $38\\text{ l}$ '
                 'dầu. Cả ngày cửa hàng bán được:',
            'options': ['$74\\text{ l}$ dầu',
                        '$82\\text{ l}$ dầu',
                        '$12\\text{ l}$ dầu',
                        '$84\\text{ l}$ dầu'],
            'answer': 3,
            'solution': 'Cả ngày bán được: $46 + 38 = 84$ ($\\text{l}$ dầu).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ '
                 'số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Đặt tính thẳng cột và thực hiện đúng phép cộng (có nhớ) hai số có hai chữ số.',
                        'Đặt tính thẳng cột và thực hiện đúng phép cộng (có nhớ) hai số có hai chữ số. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đặt tính thẳng cột và thực hiện đúng phép cộng (có nhớ) '
                        'hai số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt tính thẳng cột và thực hiện '
                        'đúng phép cộng (có nhớ) hai số có hai chữ số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai '
                        'chữ số: Đặt tính thẳng cột và thực hiện đúng phép cộng (có nhớ) hai số có hai chữ '
                        'số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$58 + 26 = 84$.”',
            'answer': True,
            'solution': 'Hàng đơn vị: $8 + 6 = 14$ viết $4$ nhớ $1$; hàng chục: $5 + 2 + 1 = 8$. Kết quả '
                        '$84$ là Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số**, quy tắc **Thứ '
                 'tự đặt tính và tính** được xác định bởi Đặt thẳng cột; tính từ phải sang trái (hàng đơn vị '
                 'trước) và khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $37 + 25$; b) $58 + 26$.” ta có lời '
                 'giải: a) $7 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + 25 '
                 '= 62$. b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thứ tự đặt tính và tính** (Đặt thẳng '
                        'cột; tính từ phải sang trái (hàng đơn vị trước)) và lời giải ví dụ minh họa của Bài '
                        '20: Phép cộng (có nhớ) số có hai chữ số với số có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có '
                 'hai chữ số** để giải bài toán sau: Đặt tính rồi tính: a) $37 + 25$; b) $58 + 26$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $7 - 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + 25 '
                        '= 62$. b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $1$ bằng...',
                        'a) $7 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + 25 '
                        '= 62$. b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $1$ bằng...',
                        'a) $7 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + 25 '
                        '= 62$. b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $2$ bằng...',
                        'a) $14 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow 37 + '
                        '25 = 62$. b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $1$ bằng...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Phép cộng (có nhớ) số có hai chữ số với số có hai '
                        'chữ số: a) $7 + 5 = 12$ viết $2$ nhớ $1$; $3 + 2 = 5$ thêm $1$ bằng $6 \\Rightarrow '
                        '37 + 25 = 62$.\n'
                        'b) $8 + 6 = 14$ viết $4$ nhớ $1$; $5 + 2 = 7$ thêm $1$ bằng $8 \\Rightarrow 58 + 26 '
                        '= 84$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Khối lớp Hai có $47$ bạn nam và $39$ bạn nữ. Hỏi khối lớp Hai có tất cả bao nhiêu bạn?',
            'answer': ['86'],
            'unit': None,
            'solution': 'Tổng số bạn của khối lớp Hai là: $47 + 39 = 86$ (bạn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd04-cong-tru-co-nho-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép cộng, phép trừ (có nhớ) trong phạm vi 100',
  'context': 'SGK Toán 2 · Chủ đề 4: Cộng, trừ có nhớ số có hai chữ số với số có một hoặc hai chữ số.',
  'title': 'Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số',
  'icon': '➖',
  'description': 'Đặt tính và tính phép trừ (có nhớ) số có hai chữ số cho số có một chữ số.',
  'requirements': ['Hiểu cách mượn $1$ chục ($10$ đơn vị) khi chữ số hàng đơn vị của số bị trừ bé hơn số '
                   'trừ.',
                   'Thực hiện đúng thao tác trừ ở hàng đơn vị rồi bớt $1$ ở hàng chục của số bị trừ.',
                   'Vận dụng kiến thức của **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ '
                   'số** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi trừ số có hai chữ số cho số có một chữ số mà chữ số đơn vị của số bị trừ **bé hơn** số '
                'trừ, ta **lấy thêm $1$ chục ($10$ đơn vị)** để trừ ở hàng đơn vị, viết kết quả và **nhớ '
                '$1$** (bớt đi $1$ ở chữ số hàng chục).',
  'theory': '- **Ví dụ 1: Tính $42 - 7$.**\n'
            '  + Hàng đơn vị: $2$ không trừ được $7$, lấy $12 - 7 = 5$, viết $5$ **nhớ $1$**.\n'
            '  + Hàng chục: $4 - 1 = 3$, viết $3$.\n'
            '  + Vậy $42 - 7 = 35$.\n'
            '- **Ví dụ 2 (Số tròn chục trừ đi một số): Tính $50 - 6$.**\n'
            '  + Hàng đơn vị: $0$ không trừ được $6$, lấy $10 - 6 = 4$, viết $4$ **nhớ $1$**.\n'
            '  + Hàng chục: $5 - 1 = 4$, viết $4$. Vậy $50 - 6 = 44$.',
  'formulas': [{'category': 'Quy tắc trừ có nhớ (2 chữ số − 1 chữ số)',
                'items': [{'name': 'Bước 1 (Hàng đơn vị)',
                           'formula': '$b < c \\rightarrow$ lấy $(10 + b) - c$, viết kết quả và nhớ $1$'},
                          {'name': 'Bước 2 (Hàng chục)',
                           'formula': 'Lấy chữ số hàng chục trừ đi $1$ (đã nhớ)',
                           'note': 'Ví dụ: $52 - 8 = 44$ ($12 - 8 = 4$ nhớ $1$; $5 - 1 = 4$).'}]}],
  'example': 'Đặt tính rồi tính: a) $63 - 8$; b) $70 - 4$.',
  'example_answer': 'a) $13 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$.\n'
                    'b) $10 - 4 = 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.',
  'real_life': 'Tính số tiền còn lại hoặc số quả trứng còn lại khi lấy bớt ra từ hộp tròn chục.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $50 - 6$ là:',
            'options': ['$44$', '$56$', '$46$', '$54$'],
            'answer': 0,
            'solution': 'Lấy $10 - 6 = 4$ viết $4$ nhớ $1$; $5 - 1 = 4$. Vậy $50 - 6 = 44$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $42 - 7$ là:',
            'options': ['$45$', '$35$', '$36$', '$49$'],
            'answer': 1,
            'solution': 'Lấy $12 - 7 = 5$ viết $5$ nhớ $1$; $4 - 1 = 3$. Vậy $42 - 7 = 35$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Bước 1 (Hàng đơn vị)**?',
            'options': ['$b < c \\rightarrow$ lấy $(10 - b) - c$, viết kết quả và nhớ $1$',
                        '$b < c \\rightarrow$ lấy $(10 + b) - c$, viết kết quả và nhớ $2$',
                        '$b < c \\rightarrow$ lấy $(10 + b) - c$, viết kết quả và nhớ $1$',
                        '$b < c \\rightarrow$ lấy $(20 + b) - c$, viết kết quả và nhớ $1$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có '
                        'một chữ số, **Bước 1 (Hàng đơn vị)** được xác định bởi: $b < c \\rightarrow$ lấy '
                        '$(10 + b) - c$, viết kết quả và nhớ $1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Bước 2 (Hàng chục)**?',
            'options': ['Lấy chữ số hàng chục trừ đi $2$ (đã nhớ)',
                        '$b < c \\rightarrow$ lấy $(10 + b) - c$, viết kết quả và nhớ $1$',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)',
                        'Lấy chữ số hàng chục trừ đi $1$ (đã nhớ)'],
            'answer': 3,
            'solution': 'Trong Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số, **Bước 2 '
                        '(Hàng chục)** có công thức/quy tắc là: Lấy chữ số hàng chục trừ đi $1$ (đã nhớ).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hùng có $34$ viên bi, Hùng có nhiều hơn Dũng $8$ viên bi. Hỏi Dũng có bao nhiêu viên bi?',
            'options': ['$26$ viên bi', '$42$ viên bi', '$24$ viên bi', '$36$ viên bi'],
            'answer': 0,
            'solution': 'Hùng nhiều hơn Dũng $8$ viên nghĩa là Dũng ít hơn Hùng $8$ viên: $34 - 8 = 26$ '
                        '(viên bi).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ '
                 'số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Hiểu cách mượn $1$ chục ($10$ đơn vị) khi chữ số hàng đơn vị của số bị trừ lớn hơn '
                        'số trừ.',
                        'Hiểu cách mượn $1$ chục ($10$ đơn vị) khi chữ số hàng đơn vị của số bị trừ bé hơn '
                        'số trừ.',
                        'Hiểu cách mượn $1$ chục ($9$ đơn vị) khi chữ số hàng đơn vị của số bị trừ bé hơn số '
                        'trừ.',
                        'Hiểu cách mượn $2$ chục ($10$ đơn vị) khi chữ số hàng đơn vị của số bị trừ bé hơn '
                        'số trừ.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một '
                        'chữ số: Hiểu cách mượn $1$ chục ($10$ đơn vị) khi chữ số hàng đơn vị của số bị trừ '
                        'bé hơn số trừ.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$81 - 5 = 76$.”',
            'answer': True,
            'solution': 'Lấy $11 - 5 = 6$ viết $6$ nhớ $1$; $8 - 1 = 7$. Vậy $81 - 5 = 76$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số**, quy tắc **Bước '
                 '1 (Hàng đơn vị)** được xác định bởi $b < c \\rightarrow$ lấy $(10 + b) - c$, viết kết quả '
                 'và nhớ $1$ và khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $63 - 8$; b) $70 - 4$.” ta có '
                 'lời giải: a) $13 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$. b) $10 - '
                 '4 = 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Bước 1 (Hàng đơn vị)** ($b < c '
                        '\\rightarrow$ lấy $(10 + b) - c$, viết kết quả và nhớ $1$) và lời giải ví dụ minh '
                        'họa của Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có '
                 'một chữ số** để giải bài toán sau: Đặt tính rồi tính: a) $63 - 8$; b) $70 - 4$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $13 + 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$. b) $10 - 4 '
                        '= 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.',
                        'a) $13 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$. b) $10 - 4 '
                        '= 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 65$.',
                        'a) $13 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$. b) $10 - 4 '
                        '= 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.',
                        'a) $26 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$. b) $10 - 4 '
                        '= 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 22: Phép trừ (có nhớ) số có hai chữ số cho số có một chữ '
                        'số: a) $13 - 8 = 5$ viết $5$ nhớ $1$; $6 - 1 = 5 \\Rightarrow 63 - 8 = 55$.\n'
                        'b) $10 - 4 = 6$ viết $6$ nhớ $1$; $7 - 1 = 6 \\Rightarrow 70 - 4 = 66$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một sợi dây dài $60\\text{ cm}$, bạn An cắt đi một đoạn dài $8\\text{ cm}$. Hỏi đoạn dây '
                 'còn lại dài bao nhiêu xăng-ti-mét?',
            'answer': ['52', '52cm', '52 cm'],
            'unit': None,
            'solution': 'Độ dài đoạn dây còn lại là: $60 - 8 = 52$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd04-cong-tru-co-nho-pham-vi-100',
  'context_title': 'Chủ đề 4: Phép cộng, phép trừ (có nhớ) trong phạm vi 100',
  'context': 'SGK Toán 2 · Chủ đề 4: Cộng, trừ có nhớ số có hai chữ số với số có một hoặc hai chữ số.',
  'title': 'Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số',
  'icon': '🎯',
  'description': 'Đặt tính và tính phép trừ (có nhớ) hai số có hai chữ số; thử lại phép tính và giải toán.',
  'requirements': ['Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số (bao gồm cả '
                   '$100$ trừ đi một số).',
                   'Biết kiểm tra kết quả phép trừ bằng phép cộng ($\\text{Hiệu} + \\text{Số trừ} = '
                   '\\text{Số bị trừ}$).',
                   'Tính đúng biểu thức có hai dấu phép tính và giải bài toán thực tế.'],
  'definition': 'Khi trừ hai số có hai chữ số mà chữ số đơn vị của số bị trừ bé hơn chữ số đơn vị của số '
                'trừ, ta **mượn $10$ để trừ ở hàng đơn vị**, viết kết quả rồi **nhớ $1$ vào hàng chục của số '
                'trừ** (hoặc bớt $1$ ở hàng chục của số bị trừ) trước khi trừ hàng chục.',
  'theory': '- **Ví dụ: Tính $63 - 28$.**\n'
            '  + Hàng đơn vị: $3$ không trừ được $8$, lấy $13 - 8 = 5$, viết $5$ **nhớ $1$**.\n'
            '  + Hàng chục: $2$ thêm $1$ bằng $3$, lấy $6 - 3 = 3$, viết $3$.\n'
            '  + Vậy $63 - 28 = 35$.\n'
            '- **Kiểm tra (thử lại):** Lấy $35 + 28 = 63$ (đúng bằng số bị trừ).\n'
            '- **Lỗi tuyệt đối tránh:** Không bao giờ được lấy chữ số đơn vị ở dưới trừ ngược chữ số đơn vị '
            'ở trên!',
  'formulas': [{'category': 'Quy tắc trừ có nhớ hai số có hai chữ số',
                'items': [{'name': 'Quy tắc trừ',
                           'formula': 'Hàng đơn vị mượn $10$ để trừ $\\rightarrow$ trả $1$ vào hàng chục của '
                                      'số trừ',
                           'note': 'Ví dụ: $72 - 35 = 37$ ($12 - 5 = 7$; $3 + 1 = 4$; $7 - 4 = 3$).'},
                          {'name': 'Cách thử lại phép trừ',
                           'formula': '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                           'note': 'Ví dụ: $37 + 35 = 72$.'}]}],
  'example': 'Đặt tính rồi tính: a) $81 - 46$; b) Tính dãy tính $45 + 18 - 30$.',
  'example_answer': 'a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow 81 - 46 '
                    '= 35$.\n'
                    'b) $45 + 18 - 30 = 63 - 30 = 33$.',
  'real_life': 'Tính số sách còn lại trong thư viện sau khi cho học sinh mượn, tìm số hạng chưa biết.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $72 - 35$ là:',
            'options': ['$47$', '$37$', '$43$', '$33$'],
            'answer': 1,
            'solution': 'Hàng đơn vị: $12 - 5 = 7$ viết $7$ nhớ $1$; hàng chục: $3 + 1 = 4$, $7 - 4 = 3$. '
                        'Vậy $72 - 35 = 37$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $45 + 18 - 30$ là:',
            'options': ['$63$', '$93$', '$33$', '$23$'],
            'answer': 2,
            'solution': 'Tính từ trái sang phải: $45 + 18 = 63$, sau đó $63 - 30 = 33$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Quy tắc trừ**?',
            'options': ['Hàng đơn vị mượn $11$ để trừ $\\rightarrow$ trả $1$ vào hàng chục của số trừ',
                        'Hàng đơn vị mượn $10$ để trừ $\\rightarrow$ trả $2$ vào hàng chục của số trừ',
                        'Hàng đơn vị mượn $20$ để trừ $\\rightarrow$ trả $1$ vào hàng chục của số trừ',
                        'Hàng đơn vị mượn $10$ để trừ $\\rightarrow$ trả $1$ vào hàng chục của số trừ'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có '
                        'hai chữ số, **Quy tắc trừ** được xác định bởi: Hàng đơn vị mượn $10$ để trừ '
                        '$\\rightarrow$ trả $1$ vào hàng chục của số trừ. (Ví dụ: $72 - 35 = 37$ ($12 - 5 = '
                        '7$; $3 + 1 = 4$; $7 - 4 = 3$).)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Cách thử lại phép trừ**?',
            'options': ['$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        '$\\text{Hiệu} - \\text{Số trừ} = \\text{Số bị trừ}$',
                        'Đảo ngược vế của quy tắc: $\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Hiệu} + \\text{Số trừ} '
                        '= \\text{Số bị trừ}$'],
            'answer': 0,
            'solution': 'Trong Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số, **Cách thử '
                        'lại phép trừ** có công thức/quy tắc là: $\\text{Hiệu} + \\text{Số trừ} = \\text{Số '
                        'bị trừ}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm số thích hợp điền vào dấu $?$ trong phép tính $? + 27 = 54$:',
            'options': ['$81$', '$27$', '$37$', '$33$'],
            'answer': 1,
            'solution': 'Muốn tìm số hạng chưa biết, ta lấy tổng trừ đi số hạng kia: $54 - 27 = 27$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ '
                 'số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số (bao '
                        'gồm cả $110$ trừ đi một số).',
                        'Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số (bao '
                        'gồm cả $99$ trừ đi một số).',
                        'Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số (bao '
                        'gồm cả $100$ trừ đi một số).',
                        'Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số (bao '
                        'gồm cả $102$ trừ đi một số).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai '
                        'chữ số: Thực hiện thành thạo phép trừ (có nhớ) số có hai chữ số cho số có hai chữ '
                        'số (bao gồm cả $100$ trừ đi một số).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Bạn Na tính $64 - 27 = 43$. Nhận định: “Bạn Na đã tính đúng.”',
            'answer': False,
            'solution': 'Hàng đơn vị phải lấy $14 - 7 = 7$ nhớ $1$, hàng chục $6 - 3 = 3$, kết quả đúng là '
                        '$37$ (Na đã lấy $7 - 4 = 3$ là trừ ngược). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số**, quy tắc **Quy '
                 'tắc trừ** được xác định bởi Hàng đơn vị mượn $10$ để trừ $\\rightarrow$ trả $1$ vào hàng '
                 'chục của số trừ và khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $81 - 46$; b) Tính dãy '
                 'tính $45 + 18 - 30$.” ta có lời giải: a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là '
                 '$5$, $8 - 5 = 3 \\Rightarrow 81 - 46 = 35$. b) $45 + 18 - 30 = 63 - 30 = 33$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy tắc trừ** (Hàng đơn vị mượn $10$ để '
                        'trừ $\\rightarrow$ trả $1$ vào hàng chục của số trừ) và lời giải ví dụ minh họa của '
                        'Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có '
                 'hai chữ số** để giải bài toán sau: Đặt tính rồi tính: a) $81 - 46$; b) Tính dãy tính $45 + '
                 '18 - 30$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow 81 - '
                        '46 = 35$. b) $45 - 18 - 30 = 63 - 30 = 33$.',
                        'a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow 81 - '
                        '46 = 35$. b) $45 + 18 - 30 = 63 - 30 = 32$.',
                        'a) $22 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow 81 - '
                        '46 = 35$. b) $45 + 18 - 30 = 63 - 30 = 33$.',
                        'a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow 81 - '
                        '46 = 35$. b) $45 + 18 - 30 = 63 - 30 = 33$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 23: Phép trừ (có nhớ) số có hai chữ số cho số có hai chữ '
                        'số: a) $11 - 6 = 5$ viết $5$ nhớ $1$; $4$ thêm $1$ là $5$, $8 - 5 = 3 \\Rightarrow '
                        '81 - 46 = 35$.\n'
                        'b) $45 + 18 - 30 = 63 - 30 = 33$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Thư viện có $63$ quyển truyện, đã cho học sinh mượn $28$ quyển. Hỏi thư viện còn lại bao '
                 'nhiêu quyển truyện?',
            'answer': ['35'],
            'unit': None,
            'solution': 'Số quyển truyện thư viện còn lại là: $63 - 28 = 35$ (quyển).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd05-lam-quen-hinh-phang',
  'context_title': 'Chủ đề 5: Làm quen với hình phẳng',
  'context': 'SGK Toán 2 · Chủ đề 5: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường '
             'gấp khúc, hình tứ giác, gấp – cắt – ghép hình, vẽ đoạn thẳng.',
  'title': 'Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng',
  'icon': '📏',
  'description': 'Nhận biết điểm, đoạn thẳng, đường thẳng, đường cong và cách kiểm tra ba điểm thẳng hàng.',
  'requirements': ['Nhận biết và đọc tên được **điểm**, **đoạn thẳng**, **đường thẳng**, **đường cong**.',
                   'Phân biệt được đoạn thẳng (bị giới hạn bởi hai đầu) và đường thẳng (kéo dài mãi về hai '
                   'phía).',
                   'Nhận biết **ba điểm thẳng hàng** và biết dùng thước thẳng để kiểm tra.'],
  'definition': '- **Đoạn thẳng $AB$** là hình nối từ điểm $A$ đến điểm $B$ (bị giới hạn bởi hai đầu $A$ và '
                '$B$).\n'
                '- **Đường thẳng $AB$** là vạch thẳng đi qua hai điểm $A, B$ và kéo dài mãi về hai phía.\n'
                '- **Đường cong** là đường uốn lượn không thẳng.\n'
                '- **Ba điểm thẳng hàng** là ba điểm cùng nằm trên một đường thẳng.',
  'theory': '- Điểm thường được ký hiệu bằng một dấu chấm nhỏ và đặt tên bằng chữ cái in hoa ($A, B, C, M, '
            'N, \\dots$).\n'
            '- **Cách kiểm tra ba điểm $A, B, C$ có thẳng hàng không:** Đặt mép thước thẳng đi qua hai điểm '
            '$A$ và $B$; nếu điểm $C$ cũng nằm sát trên mép thước đó thì ba điểm $A, B, C$ thẳng hàng.',
  'formulas': [{'category': 'Phân biệt các khái niệm hình học cơ bản',
                'items': [{'name': 'Đoạn thẳng AB',
                           'formula': 'Có hai đầu mút $A$ và $B$, đo được độ dài cụ thể'},
                          {'name': 'Đường thẳng AB',
                           'formula': 'Kéo dài mãi về cả hai phía, không bị giới hạn'},
                          {'name': 'Ba điểm thẳng hàng',
                           'formula': 'Cùng nằm trên một đường thẳng (cùng trùng mép thước thẳng)'}]}],
  'example': 'Cho ba điểm $A, B, C$ cùng nằm trên một đường thẳng theo thứ tự đó. Hãy kể tên các đoạn thẳng '
             'có trên hình.',
  'example_answer': 'Trên hình có $3$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn '
                    '$AC$.',
  'real_life': 'Xếp hàng tập thể dục thẳng hàng, căng dây xây tường thẳng, đường chạy cong trên sân vận '
               'động.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Ba điểm thẳng hàng là ba điểm:',
            'options': ['Cùng nằm trên một đường cong',
                        'Tạo thành một hình tam giác',
                        'Cùng nằm trên một đường thẳng',
                        'Luôn cách đều nhau'],
            'answer': 2,
            'solution': 'Theo định nghĩa, ba điểm thẳng hàng là ba điểm cùng nằm trên một đường thẳng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Để kiểm tra xem ba điểm trên trang giấy có thẳng hàng hay không, ta dùng dụng cụ nào?',
            'options': ['Cân đĩa', 'Ca đong $1\\text{ l}$', 'Đồng hồ', 'Thước thẳng'],
            'answer': 3,
            'solution': 'Ta đặt mép thước thẳng đi qua các điểm để kiểm tra chúng có cùng nằm trên một đường '
                        'thẳng hay không.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Đoạn thẳng AB**?',
            'options': ['Có hai đầu mút $A$ và $B$, đo được độ dài cụ thể',
                        'Có hai đầu mút $A$ và $B$, đo được độ dài cụ thể (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Có hai đầu mút $A$ và $B$, đo được độ dài cụ thể',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Có hai đầu mút $A$ và $B$, đo '
                        'được độ dài cụ thể'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba '
                        'điểm thẳng hàng, **Đoạn thẳng AB** được xác định bởi: Có hai đầu mút $A$ và $B$, đo '
                        'được độ dài cụ thể.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Đường thẳng AB**?',
            'options': ['Kéo dài mãi về cả hai phía, không bị giới hạn (với dấu ngược lại)',
                        'Kéo dài mãi về cả hai phía, không bị giới hạn',
                        'Đảo ngược vế của quy tắc: Kéo dài mãi về cả hai phía, không bị giới hạn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Kéo dài mãi về cả hai phía, '
                        'không bị giới hạn'],
            'answer': 1,
            'solution': 'Trong Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, '
                        '**Đường thẳng AB** có công thức/quy tắc là: Kéo dài mãi về cả hai phía, không bị '
                        'giới hạn.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trên một đoạn thẳng $AC$ có lấy thêm điểm $B$ nằm giữa $A$ và $C$. Hỏi trên hình có tất cả '
                 'bao nhiêu đoạn thẳng?',
            'options': ['$1$ đoạn thẳng', '$2$ đoạn thẳng', '$3$ đoạn thẳng', '$4$ đoạn thẳng'],
            'answer': 2,
            'solution': 'Có $2$ đoạn thẳng nhỏ là $AB, BC$ và $1$ đoạn thẳng lớn ghép lại là $AC$. Tổng cộng '
                        'có $2 + 1 = 3$ đoạn thẳng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm '
                 'thẳng hàng**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết và đọc tên được **điểm**, **đoạn thẳng**, **đường thẳng**, **đường '
                        'cong**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và đọc tên được **điểm**, **đoạn thẳng**, '
                        '**đường thẳng**, **đường cong**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và đọc tên được '
                        '**điểm**, **đoạn thẳng**, **đường thẳng**, **đường cong**.',
                        'Nhận biết và đọc tên được **điểm**, **đoạn thẳng**, **đường thẳng**, **đường '
                        'cong**.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba '
                        'điểm thẳng hàng: Nhận biết và đọc tên được **điểm**, **đoạn thẳng**, **đường '
                        'thẳng**, **đường cong**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Đoạn thẳng $AB$ kéo dài mãi về hai phía.”',
            'answer': False,
            'solution': 'Đoạn thẳng $AB$ bị giới hạn bởi hai đầu $A$ và $B$; hình kéo dài mãi về hai phía là '
                        'đường thẳng. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng**, quy tắc '
                 '**Đoạn thẳng AB** được xác định bởi Có hai đầu mút $A$ và $B$, đo được độ dài cụ thể và '
                 'khi áp dụng cho ví dụ “Cho ba điểm $A, B, C$ cùng nằm trên một đường thẳng theo thứ tự đó. '
                 'Hãy kể tên các đoạn thẳng có trên hình.” ta có lời giải: Trên hình có $3$ đoạn thẳng là: '
                 'đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn $AC$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đoạn thẳng AB** (Có hai đầu mút $A$ và '
                        '$B$, đo được độ dài cụ thể) và lời giải ví dụ minh họa của Bài 25: Điểm, đoạn '
                        'thẳng, đường thẳng, đường cong, ba điểm thẳng hàng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba '
                 'điểm thẳng hàng** để giải bài toán sau: Cho ba điểm $A, B, C$ cùng nằm trên một đường '
                 'thẳng theo thứ tự đó. Hãy kể tên các đoạn thẳng có trên hình. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Trên hình có $3$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn '
                        '$AC$.',
                        'Trên hình có $4$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn '
                        '$AC$.',
                        'Trên hình có $2$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn '
                        '$AC$.',
                        'Trên hình có $6$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và đoạn thẳng lớn '
                        '$AC$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 25: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm '
                        'thẳng hàng: Trên hình có $3$ đoạn thẳng là: đoạn thẳng $AB$, đoạn thẳng $BC$ và '
                        'đoạn thẳng lớn $AC$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hàng cây trồng thẳng tắp có $4$ cây ở các vị trí $A, B, C, D$ theo thứ tự đó. Hỏi có '
                 'mấy bộ gồm $3$ cây thẳng hàng có chứa cả hai cây $A$ và $B$?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Vì cả $4$ cây cùng nằm trên một đường thẳng nên các bộ $3$ cây chứa $A, B$ là $(A, '
                        'B, C)$ và $(A, B, D)$, tức là có $2$ bộ.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd05-lam-quen-hinh-phang',
  'context_title': 'Chủ đề 5: Làm quen với hình phẳng',
  'context': 'SGK Toán 2 · Chủ đề 5: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường '
             'gấp khúc, hình tứ giác, gấp – cắt – ghép hình, vẽ đoạn thẳng.',
  'title': 'Bài 26: Đường gấp khúc. Hình tứ giác',
  'icon': '📐',
  'description': 'Nhận biết đường gấp khúc, hình tứ giác và cách tính độ dài đường gấp khúc.',
  'requirements': ['Nhận biết và đọc tên được **đường gấp khúc**; tính được **độ dài đường gấp khúc**.',
                   'Nhận dạng được **hình tứ giác** (có $4$ đỉnh và $4$ cạnh).',
                   'Vận dụng kiến thức của **Bài 26: Đường gấp khúc. Hình tứ giác** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': '- **Đường gấp khúc** gồm nhiều đoạn thẳng nối tiếp nhau và không có hai đoạn thẳng nối tiếp '
                'nào cùng nằm trên một đường thẳng.\n'
                '- **Độ dài đường gấp khúc** bằng **tổng độ dài các đoạn thẳng** tạo thành đường gấp khúc '
                'đó.\n'
                '- **Hình tứ giác** là hình phẳng có **$4$ cạnh** và **$4$ đỉnh**.',
  'theory': '- **Ví dụ đường gấp khúc $ABCD$:** gồm $3$ đoạn thẳng là $AB, BC$ và $CD$. Nếu $AB = 3\\text{ '
            'cm}, BC = 4\\text{ cm}, CD = 2\\text{ cm}$ thì độ dài đường gấp khúc $ABCD$ là $3 + 4 + 2 = '
            '9\\text{ cm}$.\n'
            '- **Về hình tứ giác:** Hình vuông và hình chữ nhật đã học ở lớp 1 đều có $4$ cạnh và $4$ đỉnh '
            'nên chúng đều là những **hình tứ giác đặc biệt**.',
  'formulas': [{'category': 'Đường gấp khúc và Hình tứ giác',
                'items': [{'name': 'Độ dài đường gấp khúc ABC',
                           'formula': '$\\text{Độ dài} = AB + BC$',
                           'note': 'Tổng độ dài tất cả các đoạn thẳng thành phần.'},
                          {'name': 'Độ dài đường gấp khúc ABCD',
                           'formula': '$\\text{Độ dài} = AB + BC + CD$'},
                          {'name': 'Đặc điểm hình tứ giác',
                           'formula': 'Có $4$ cạnh thẳng và $4$ đỉnh',
                           'note': 'Hình vuông, hình chữ nhật cũng là hình tứ giác.'}]}],
  'example': 'Đường gấp khúc $MNPQ$ gồm ba đoạn thẳng có độ dài: $MN = 5\\text{ cm}$, $NP = 3\\text{ cm}$, '
             '$PQ = 6\\text{ cm}$. Tính độ dài đường gấp khúc $MNPQ$.',
  'example_answer': 'Độ dài đường gấp khúc $MNPQ$ là:\n'
                    '$5 + 3 + 6 = 14$ ($\\text{cm}$)\n'
                    'Đáp số: $14\\text{ cm}$.',
  'real_life': 'Tính tổng quãng đường đi học qua nhiều ngã rẽ, nhận dạng mặt bàn, cánh diều hình tứ giác.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình phẳng có $4$ cạnh và $4$ đỉnh được gọi là hình gì?',
            'options': ['Hình tam giác', 'Hình tròn', 'Đường gấp khúc', 'Hình tứ giác'],
            'answer': 3,
            'solution': 'Hình có $4$ cạnh và $4$ đỉnh được gọi là hình tứ giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đường gấp khúc $ABC$ gồm mấy đoạn thẳng?',
            'options': ['$2$ đoạn thẳng', '$1$ đoạn thẳng', '$3$ đoạn thẳng', '$4$ đoạn thẳng'],
            'answer': 0,
            'solution': 'Đường gấp khúc $ABC$ gồm $2$ đoạn thẳng nối tiếp là $AB$ và $BC$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Đường gấp khúc. Hình tứ giác**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Độ dài đường gấp khúc ABC**?',
            'options': ['$\\text{Độ dài} = AB - BC$',
                        '$\\text{Độ dài} = AB + BC$',
                        'Đảo ngược vế của quy tắc: $\\text{Độ dài} = AB + BC$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Độ dài} = AB + BC$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 26: Đường gấp khúc. Hình tứ giác, **Độ dài đường '
                        'gấp khúc ABC** được xác định bởi: $\\text{Độ dài} = AB + BC$. (Tổng độ dài tất cả '
                        'các đoạn thẳng thành phần.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Đường gấp khúc. Hình tứ giác**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Độ dài đường gấp khúc ABCD**?',
            'options': ['$\\text{Độ dài} = AB - BC + CD$',
                        'Đảo ngược vế của quy tắc: $\\text{Độ dài} = AB + BC + CD$',
                        '$\\text{Độ dài} = AB + BC + CD$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Độ dài} = AB + BC + '
                        'CD$'],
            'answer': 2,
            'solution': 'Trong Bài 26: Đường gấp khúc. Hình tứ giác, **Độ dài đường gấp khúc ABCD** có công '
                        'thức/quy tắc là: $\\text{Độ dài} = AB + BC + CD$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đường gấp khúc có ba đoạn thẳng dài lần lượt là $4\\text{ cm}$, $5\\text{ cm}$ và '
                 '$3\\text{ cm}$. Độ dài đường gấp khúc đó là:',
            'options': ['$9\\text{ cm}$', '$7\\text{ cm}$', '$11\\text{ cm}$', '$12\\text{ cm}$'],
            'answer': 3,
            'solution': 'Độ dài đường gấp khúc là: $4 + 5 + 3 = 12$ ($\\text{cm}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 26: Đường gấp khúc. Hình tứ giác**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết và đọc tên được **đường gấp khúc**; tính được **độ dài đường gấp khúc**.',
                        'Nhận biết và đọc tên được **đường gấp khúc**; tính được **độ dài đường gấp khúc**. '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và đọc tên được **đường gấp khúc**; tính được '
                        '**độ dài đường gấp khúc**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và đọc tên được '
                        '**đường gấp khúc**; tính được **độ dài đường gấp khúc**.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 26: Đường gấp khúc. Hình tứ giác: Nhận biết và đọc '
                        'tên được **đường gấp khúc**; tính được **độ dài đường gấp khúc**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Hình vuông và hình chữ nhật cũng là các hình tứ giác.”',
            'answer': True,
            'solution': 'Hình vuông và hình chữ nhật đều có $4$ cạnh và $4$ đỉnh nên đều là hình tứ giác. '
                        'Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 26: Đường gấp khúc. Hình tứ giác**, quy tắc **Độ dài đường gấp khúc ABC** được '
                 'xác định bởi $\\text{Độ dài} = AB + BC$ và khi áp dụng cho ví dụ “Đường gấp khúc $MNPQ$ '
                 'gồm ba đoạn thẳng có độ dài: $MN = 5\\text{ cm}$, $NP = 3\\text{ cm}$, $PQ = 6\\text{ '
                 'cm}$. Tính độ dài đường gấp kh...” ta có lời giải: Độ dài đường gấp khúc $MNPQ$ là: $5 + 3 '
                 '+ 6 = 14$ ($\\text{cm}$) Đáp số: $14\\text{ cm}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Độ dài đường gấp khúc ABC** ($\\text{Độ '
                        'dài} = AB + BC$) và lời giải ví dụ minh họa của Bài 26: Đường gấp khúc. Hình tứ '
                        'giác.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 26: Đường gấp khúc. Hình tứ giác** để giải bài toán '
                 'sau: Đường gấp khúc $MNPQ$ gồm ba đoạn thẳng có độ dài: $MN = 5\\text{ cm}$, $NP = '
                 '3\\text{ cm}$, $PQ = 6\\text{ cm}$. Tính độ dài đường gấp khúc $MNPQ$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Độ dài đường gấp khúc $MNPQ$ là: $5 - 3 + 6 = 14$ ($\\text{cm}$) Đáp số: $14\\text{ '
                        'cm}$.',
                        'Độ dài đường gấp khúc $MNPQ$ là: $5 + 3 + 6 = 14$ ($\\text{cm}$) Đáp số: $14\\text{ '
                        'cm}$.',
                        'Độ dài đường gấp khúc $MNPQ$ là: $5 + 3 + 6 = 14$ ($\\text{cm}$) Đáp số: $13\\text{ '
                        'cm}$.',
                        'Độ dài đường gấp khúc $MNPQ$ là: $10 + 3 + 6 = 14$ ($\\text{cm}$) Đáp số: '
                        '$14\\text{ cm}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 26: Đường gấp khúc. Hình tứ giác: Độ dài đường gấp khúc '
                        '$MNPQ$ là:\n'
                        '$5 + 3 + 6 = 14$ ($\\text{cm}$)\n'
                        'Đáp số: $14\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đường gấp khúc $ABCD$ có độ dài là $17\\text{ cm}$, biết đoạn $AB = 6\\text{ cm}$ và $BC = '
                 '4\\text{ cm}$. Hỏi đoạn thẳng $CD$ dài bao nhiêu xăng-ti-mét?',
            'answer': ['7', '7cm', '7 cm'],
            'unit': None,
            'solution': 'Tổng hai đoạn $AB$ và $BC$ là $6 + 4 = 10$ ($\\text{cm}$). Độ dài đoạn $CD$ là $17 '
                        '- 10 = 7$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd05-lam-quen-hinh-phang',
  'context_title': 'Chủ đề 5: Làm quen với hình phẳng',
  'context': 'SGK Toán 2 · Chủ đề 5: Điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường '
             'gấp khúc, hình tứ giác, gấp – cắt – ghép hình, vẽ đoạn thẳng.',
  'title': 'Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng',
  'icon': '✏️',
  'description': 'Cách dùng thước thẳng vẽ đoạn thẳng có độ dài cho trước và thực hành gấp, cắt, ghép hình.',
  'requirements': ['Vẽ được đoạn thẳng có độ dài cho trước (theo đơn vị $\\text{cm}$) bằng thước thẳng.',
                   'Thực hiện được việc gấp, cắt, ghép hình để tạo ra hình tứ giác, hình tam giác.',
                   'Đếm được số đoạn thẳng, số hình tam giác, số hình tứ giác trong hình vẽ.'],
  'definition': '**Cách vẽ đoạn thẳng có độ dài $a\\text{ cm}$:**\n'
                '1. Đặt thước thẳng lên trang giấy, tay trái giữ thước.\n'
                '2. Dùng bút chấm một điểm trùng với **vạch $0$** và chấm một điểm trùng với **vạch số '
                '$a$**.\n'
                '3. Nối hai điểm dọc theo mép thước, nhấc thước ra và đặt tên hai đầu đoạn thẳng.',
  'theory': '- **Cắt, ghép hình:**\n'
            '  + Nếu cắt một hình chữ nhật theo một đường thẳng đi qua hai cạnh đối diện, ta có thể được $2$ '
            'hình tứ giác.\n'
            '  + Nếu cắt một hình vuông theo đường nối hai đỉnh đối diện, ta được $2$ hình tam giác.\n'
            '- Khi vẽ đoạn thẳng, luôn bắt đầu từ **vạch $0$** của thước (không bắt đầu từ vạch $1$).',
  'formulas': [{'category': 'Quy tắc vẽ đoạn thẳng và đếm hình',
                'items': [{'name': 'Vẽ đoạn thẳng dài a cm',
                           'formula': 'Chấm điểm đầu ở vạch $0$, điểm cuối ở vạch $a$, nối thẳng hai điểm'},
                          {'name': 'Quãng đường gồm nhiều đoạn bằng nhau',
                           'formula': 'Cộng độ dài các đoạn thẳng lại với nhau',
                           'note': 'Ví dụ: $3$ đoạn mỗi đoạn $5\\text{ cm} \\Rightarrow 5 + 5 + 5 = '
                                   '15\\text{ cm}$.'}]}],
  'example': 'Nêu cách vẽ đoạn thẳng $AB$ có độ dài $6\\text{ cm}$.',
  'example_answer': 'Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $0$, chấm điểm $B$ trùng vạch $6$, '
                    'dùng bút nối từ $A$ đến $B$ dọc theo mép thước.',
  'real_life': 'Kẻ lề vở, vẽ khung tranh, gấp giấy Origami thủ công.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi vẽ đoạn thẳng dài $6\\text{ cm}$ bằng thước thẳng, em chấm điểm đầu tiên ở vạch số mấy '
                 'của thước?',
            'options': ['Vạch số $0$', 'Vạch số $1$', 'Vạch số $6$', 'Vạch số $10$'],
            'answer': 0,
            'solution': 'Khi vẽ đoạn thẳng, điểm đầu tiên luôn chấm ở vạch số $0$, điểm thứ hai chấm ở vạch '
                        'số $6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình nào dưới đây KHÔNG phải là hình tứ giác?',
            'options': ['Hình vuông', 'Hình tam giác', 'Hình chữ nhật', 'Hình cánh diều $4$ cạnh'],
            'answer': 1,
            'solution': 'Hình tam giác chỉ có $3$ cạnh nên không phải là hình tứ giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Vẽ đoạn thẳng dài a cm**?',
            'options': ['Chấm điểm đầu ở vạch $1$, điểm cuối ở vạch $a$, nối thẳng hai điểm',
                        'Chấm điểm đầu ở vạch $2$, điểm cuối ở vạch $a$, nối thẳng hai điểm',
                        'Chấm điểm đầu ở vạch $0$, điểm cuối ở vạch $a$, nối thẳng hai điểm',
                        'Cộng độ dài các đoạn thẳng lại với nhau'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn '
                        'thẳng, **Vẽ đoạn thẳng dài a cm** được xác định bởi: Chấm điểm đầu ở vạch $0$, điểm '
                        'cuối ở vạch $a$, nối thẳng hai điểm.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Quãng đường gồm nhiều đoạn bằng nhau**?',
            'options': ['Cộng độ dài các đoạn thẳng lại với nhau (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Cộng độ dài các đoạn thẳng lại với nhau',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Cộng độ dài các đoạn thẳng lại '
                        'với nhau',
                        'Cộng độ dài các đoạn thẳng lại với nhau'],
            'answer': 3,
            'solution': 'Trong Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng, **Quãng đường gồm '
                        'nhiều đoạn bằng nhau** có công thức/quy tắc là: Cộng độ dài các đoạn thẳng lại với '
                        'nhau.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một con kiến bò theo đường gấp khúc gồm $3$ đoạn thẳng, mỗi đoạn dài $5\\text{ cm}$. Hỏi '
                 'con kiến đã bò được quãng đường dài bao nhiêu xăng-ti-mét?',
            'options': ['$15\\text{ cm}$', '$8\\text{ cm}$', '$10\\text{ cm}$', '$53\\text{ cm}$'],
            'answer': 0,
            'solution': 'Quãng đường con kiến bò được là: $5 + 5 + 5 = 15$ ($\\text{cm}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Vẽ được đoạn thẳng có độ dài cho trước (theo đơn vị $\\text{cm}$) bằng thước thẳng. '
                        '(với dấu ngược lại)',
                        'Vẽ được đoạn thẳng có độ dài cho trước (theo đơn vị $\\text{cm}$) bằng thước thẳng.',
                        'Đảo ngược vế của quy tắc: Vẽ được đoạn thẳng có độ dài cho trước (theo đơn vị '
                        '$\\text{cm}$) bằng thước thẳng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Vẽ được đoạn thẳng có độ dài '
                        'cho trước (theo đơn vị $\\text{cm}$) bằng thước thẳng.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn '
                        'thẳng: Vẽ được đoạn thẳng có độ dài cho trước (theo đơn vị $\\text{cm}$) bằng thước '
                        'thẳng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu chấm điểm $M$ ở vạch số $1$ và điểm $N$ ở vạch số $5$ trên thước kẻ rồi '
                 'nối lại thì đoạn thẳng $MN$ dài $5\\text{ cm}$.”',
            'answer': False,
            'solution': 'Từ vạch $1$ đến vạch $5$ chỉ dài $5 - 1 = 4\\text{ cm}$ chứ không phải $5\\text{ '
                        'cm}$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng**, quy tắc **Vẽ đoạn '
                 'thẳng dài a cm** được xác định bởi Chấm điểm đầu ở vạch $0$, điểm cuối ở vạch $a$, nối '
                 'thẳng hai điểm và khi áp dụng cho ví dụ “Nêu cách vẽ đoạn thẳng $AB$ có độ dài $6\\text{ '
                 'cm}$.” ta có lời giải: Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $0$, chấm điểm '
                 '$B$ trùng vạch $6$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Vẽ đoạn thẳng dài a cm** (Chấm điểm đầu '
                        'ở vạch $0$, điểm cuối ở vạch $a$, nối thẳng hai điểm) và lời giải ví dụ minh họa '
                        'của Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn '
                 'thẳng** để giải bài toán sau: Nêu cách vẽ đoạn thẳng $AB$ có độ dài $6\\text{ cm}$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $1$, chấm điểm $B$ trùng vạch '
                        '$6$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.',
                        'Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $0$, chấm điểm $B$ trùng vạch '
                        '$5$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.',
                        'Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $0$, chấm điểm $B$ trùng vạch '
                        '$6$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.',
                        'Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $2$, chấm điểm $B$ trùng vạch '
                        '$6$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 27: Thực hành gấp, cắt, ghép, xếp hình. Vẽ đoạn thẳng: '
                        'Đặt thước thẳng trên giấy, chấm điểm $A$ trùng vạch $0$, chấm điểm $B$ trùng vạch '
                        '$6$, dùng bút nối từ $A$ đến $B$ dọc theo mép thước.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đoạn thẳng $AB$ dài $8\\text{ cm}$, đoạn thẳng $CD$ dài hơn đoạn thẳng $AB$ là $4\\text{ '
                 'cm}$. Hỏi khi vẽ đoạn thẳng $CD$ từ vạch $0$ của thước thì điểm $D$ phải chấm ở vạch số '
                 'mấy?',
            'answer': ['12'],
            'unit': None,
            'solution': 'Đoạn thẳng $CD$ dài $8 + 4 = 12$ ($\\text{cm}$). Vì điểm $C$ ở vạch $0$ nên điểm '
                        '$D$ phải chấm ở vạch số $12$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd06-ngay-gio-thang',
  'context_title': 'Chủ đề 6: Ngày – giờ, giờ – phút, ngày – tháng',
  'context': 'SGK Toán 2 · Chủ đề 6: Một ngày có 24 giờ, một giờ có 60 phút, xem đồng hồ (kim phút chỉ số 3, '
             'số 6), ngày – tháng, xem lịch.',
  'title': 'Bài 29: Ngày – giờ, giờ – phút',
  'icon': '⏰',
  'description': 'Nhận biết 1 ngày có 24 giờ, 1 giờ có 60 phút; cách đọc giờ theo buổi và khi kim phút chỉ '
                 'số 3, số 6.',
  'requirements': ['Biết $1$ ngày $= 24$ giờ, $1$ giờ $= 60$ phút.',
                   'Chuyển đổi được cách gọi giờ từ $13$ giờ đến $24$ giờ sang giờ buổi chiều, buổi tối, '
                   'buổi đêm.',
                   'Đọc được đồng hồ khi kim phút chỉ số $12$ (giờ đúng), số $3$ ($15$ phút) và số $6$ ($30$ '
                   'phút hay giờ rưỡi).'],
  'definition': '- **$1$ ngày $= 24$ giờ** (tính từ $12$ giờ đêm hôm trước đến $12$ giờ đêm hôm sau).\n'
                '- **$1$ giờ $= 60$ phút**.\n'
                '- Khi kim dài (kim phút) chỉ số $3$ là **$15$ phút**; chỉ số $6$ là **$30$ phút** (còn gọi '
                'là **rưỡi**).',
  'theory': '- **Các buổi trong ngày ($24$ giờ):**\n'
            '  + Buổi sáng: từ $1$ giờ sáng đến $10$ giờ sáng.\n'
            '  + Buổi trưa: $11$ giờ trưa, $12$ giờ trưa.\n'
            '  + Buổi chiều: từ $13$ giờ ($1$ giờ chiều) đến $18$ giờ ($6$ giờ chiều).\n'
            '  + Buổi tối: từ $19$ giờ ($7$ giờ tối) đến $21$ giờ ($9$ giờ tối).\n'
            '  + Buổi đêm: từ $22$ giờ ($10$ giờ đêm) đến $24$ giờ ($12$ giờ đêm).\n'
            '- **Mẹo đổi giờ chiều, tối, đêm:** Lấy số giờ theo thang $24$ trừ đi $12$ (ví dụ: $17$ giờ '
            '$\\rightarrow 17 - 12 = 5$ giờ chiều; $20$ giờ $\\rightarrow 20 - 12 = 8$ giờ tối).',
  'formulas': [{'category': 'Quan hệ Ngày – Giờ – Phút và cách đọc đồng hồ',
                'items': [{'name': 'Quy đổi đơn vị', 'formula': '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút'},
                          {'name': 'Đổi giờ chiều/tối/đêm',
                           'formula': 'Giờ buổi chiều, tối $+$ $12 =$ Giờ theo thang $24$',
                           'note': 'Ví dụ: $5$ giờ chiều $= 5 + 12 = 17$ giờ.'},
                          {'name': 'Vị trí kim phút',
                           'formula': 'Chỉ số $12 \\rightarrow 0$ phút; chỉ số $3 \\rightarrow 15$ phút; chỉ '
                                      'số $6 \\rightarrow 30$ phút (rưỡi)'}]}],
  'example': 'a) $15$ giờ còn gọi là mấy giờ chiều?\n'
             'b) Đồng hồ có kim ngắn nằm giữa số $8$ và số $9$, kim dài chỉ số $6$. Đồng hồ chỉ mấy giờ?',
  'example_answer': 'a) Vì $15 - 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ chiều**.\n'
                    'b) Đồng hồ chỉ **$8$ giờ $30$ phút** (hay **$8$ giờ rưỡi**).',
  'real_life': 'Đọc giờ tàu chạy, giờ phát sóng chương trình truyền hình (như Thời sự lúc $19$ giờ tối).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một ngày có bao nhiêu giờ và một giờ có bao nhiêu phút?',
            'options': ['$12$ giờ và $60$ phút',
                        '$24$ giờ và $60$ phút',
                        '$24$ giờ và $30$ phút',
                        '$60$ giờ và $24$ phút'],
            'answer': 1,
            'solution': 'Một ngày có $24$ giờ và một giờ có $60$ phút.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên đồng hồ, kim ngắn ở giữa số $9$ và số $10$, kim dài chỉ đúng số $6$. Đồng hồ chỉ:',
            'options': ['$9$ giờ đúng', '$6$ giờ $9$ phút', '$9$ giờ $30$ phút', '$9$ giờ $15$ phút'],
            'answer': 2,
            'solution': 'Kim dài chỉ số $6$ ứng với $30$ phút, nên đồng hồ chỉ $9$ giờ $30$ phút (hay $9$ '
                        'giờ rưỡi).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Ngày – giờ, giờ – phút**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Quy đổi đơn vị**?',
            'options': ['$2$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút',
                        '$1$ ngày $= 24$ giờ; $1$ giờ $= 59$ phút',
                        'Giờ buổi chiều, tối $+$ $12 =$ Giờ theo thang $24$',
                        '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 29: Ngày – giờ, giờ – phút, **Quy đổi đơn vị** '
                        'được xác định bởi: $1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Ngày – giờ, giờ – phút**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Đổi giờ chiều/tối/đêm**?',
            'options': ['Giờ buổi chiều, tối $+$ $12 =$ Giờ theo thang $24$',
                        'Giờ buổi chiều, tối $+$ $13 =$ Giờ theo thang $24$',
                        'Giờ buổi chiều, tối $+$ $12 =$ Giờ theo thang $23$',
                        'Giờ buổi chiều, tối $+$ $24 =$ Giờ theo thang $24$'],
            'answer': 0,
            'solution': 'Trong Bài 29: Ngày – giờ, giờ – phút, **Đổi giờ chiều/tối/đêm** có công thức/quy '
                        'tắc là: Giờ buổi chiều, tối $+$ $12 =$ Giờ theo thang $24$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': '$17$ giờ còn được gọi là mấy giờ?',
            'options': ['$7$ giờ chiều', '$5$ giờ chiều', '$5$ giờ sáng', '$7$ giờ tối'],
            'answer': 1,
            'solution': 'Ta lấy $17 - 12 = 5$, nên $17$ giờ còn gọi là $5$ giờ chiều.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 29: Ngày – giờ, giờ – phút**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Biết $2$ ngày $= 24$ giờ, $1$ giờ $= 60$ phút.',
                        'Biết $1$ ngày $= 24$ giờ, $1$ giờ $= 59$ phút.',
                        'Biết $1$ ngày $= 24$ giờ, $1$ giờ $= 60$ phút.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 29: Ngày – giờ, giờ – phút: Biết $1$ ngày $= 24$ giờ, '
                        '$1$ giờ $= 60$ phút.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$8$ giờ tối còn được gọi là $20$ giờ.”',
            'answer': True,
            'solution': 'Vì $8 + 12 = 20$ nên $8$ giờ tối chính là $20$ giờ. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 29: Ngày – giờ, giờ – phút**, quy tắc **Quy đổi đơn vị** được xác định bởi $1$ '
                 'ngày $= 24$ giờ; $1$ giờ $= 60$ phút và khi áp dụng cho ví dụ “a) $15$ giờ còn gọi là mấy '
                 'giờ chiều? b) Đồng hồ có kim ngắn nằm giữa số $8$ và số $9$, kim dài chỉ số $6$. Đồng hồ '
                 'chỉ mấy giờ?” ta có lời giải: a) Vì $15 - 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ '
                 'chiều**. b) Đồng hồ chỉ **$8$ giờ $30$ phút** (hay **$8$ giờ rưỡi**).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy đổi đơn vị** ($1$ ngày $= 24$ giờ; '
                        '$1$ giờ $= 60$ phút) và lời giải ví dụ minh họa của Bài 29: Ngày – giờ, giờ – '
                        'phút.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 29: Ngày – giờ, giờ – phút** để giải bài toán sau: '
                 'a) $15$ giờ còn gọi là mấy giờ chiều?\n'
                 'b) Đồng hồ có kim ngắn nằm giữa số $8$ và số $9$, kim dài chỉ số $6$. Đồng hồ chỉ mấy giờ? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) Vì $15 + 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ chiều**. b) Đồng hồ chỉ **$8$ '
                        'giờ $30$ phút** (hay **$8$ giờ rưỡi**).',
                        'a) Vì $15 - 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ chiều**. b) Đồng hồ chỉ **$8$ '
                        'giờ $30$ phút** (hay **$7$ giờ rưỡi**).',
                        'a) Vì $30 - 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ chiều**. b) Đồng hồ chỉ **$8$ '
                        'giờ $30$ phút** (hay **$8$ giờ rưỡi**).',
                        'a) Vì $15 - 12 = 3$ nên $15$ giờ còn gọi là **$3$ giờ chiều**. b) Đồng hồ chỉ **$8$ '
                        'giờ $30$ phút** (hay **$8$ giờ rưỡi**).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 29: Ngày – giờ, giờ – phút: a) Vì $15 - 12 = 3$ nên $15$ '
                        'giờ còn gọi là **$3$ giờ chiều**.\n'
                        'b) Đồng hồ chỉ **$8$ giờ $30$ phút** (hay **$8$ giờ rưỡi**).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Chương trình phim hoạt hình bắt đầu lúc $19$ giờ, tức là bắt đầu lúc mấy giờ tối?',
            'answer': ['7'],
            'unit': None,
            'solution': 'Ta có $19 - 12 = 7$, vậy $19$ giờ là $7$ giờ tối.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd06-ngay-gio-thang',
  'context_title': 'Chủ đề 6: Ngày – giờ, giờ – phút, ngày – tháng',
  'context': 'SGK Toán 2 · Chủ đề 6: Một ngày có 24 giờ, một giờ có 60 phút, xem đồng hồ (kim phút chỉ số 3, '
             'số 6), ngày – tháng, xem lịch.',
  'title': 'Bài 30: Ngày – tháng',
  'icon': '📅',
  'description': 'Nhận biết số ngày trong từng tháng và cách tra cứu thứ, ngày trên tờ lịch tháng.',
  'requirements': ['Biết một tháng thường có $30$ hoặc $31$ ngày (riêng tháng Hai có $28$ hoặc $29$ ngày).',
                   'Đọc được tờ lịch tháng: biết tháng đó có bao nhiêu ngày, một ngày cụ thể là thứ mấy.',
                   'Vận dụng quy luật $1$ tuần có $7$ ngày để tìm các ngày cùng thứ trong tháng.'],
  'definition': '- Một năm có $12$ tháng (từ tháng $1$ đến tháng $12$).\n'
                '- Các tháng có **$31$ ngày**: tháng $1, 3, 5, 7, 8, 10, 12$.\n'
                '- Các tháng có **$30$ ngày**: tháng $4, 6, 9, 11$.\n'
                '- Riêng **tháng $2$** có $28$ ngày (hoặc $29$ ngày vào năm nhuận).',
  'theory': '- **Cách đọc tờ lịch tháng:**\n'
            '  + Nhìn số lớn nhất ở cuối bảng lịch để biết tháng đó có $28, 29, 30$ hay $31$ ngày.\n'
            '  + Các ngày nằm trong **cùng một cột (hoặc hàng) của một thứ** luôn cách nhau $7$ ngày.\n'
            '- **Ví dụ:** Nếu ngày $3$ tháng $6$ là Thứ Hai thì các ngày Thứ Hai tiếp theo trong tháng $6$ '
            'là: ngày $10$ ($3 + 7$), ngày $17$ ($10 + 7$) và ngày $24$ ($17 + 7$).',
  'formulas': [{'category': 'Số ngày trong tháng và quy luật lịch tháng',
                'items': [{'name': 'Tháng 31 ngày',
                           'formula': 'Tháng $1, 3, 5, 7, 8, 10, 12$ (các đốt lồi trên nắm tay)'},
                          {'name': 'Tháng 30 ngày', 'formula': 'Tháng $4, 6, 9, 11$'},
                          {'name': 'Cùng thứ tuần sau',
                           'formula': 'Ngày tuần sau $=$ Ngày tuần này $+ 7$'}]}],
  'example': 'Ngày $5$ tháng $9$ là Thứ Năm. Hỏi Thứ Năm tuần tiếp theo của tháng $9$ là ngày bao nhiêu?',
  'example_answer': 'Vì $1$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng $9$).',
  'real_life': 'Xem lịch tháng để lên kế hoạch học tập, biết ngày khai giảng ($5/9$), ngày Quốc tế Thiếu nhi '
               '($1/6$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tháng Ba có tất cả bao nhiêu ngày?',
            'options': ['$30$ ngày', '$28$ ngày', '$31$ ngày', '$29$ ngày'],
            'answer': 2,
            'solution': 'Tháng Ba thuộc nhóm các tháng có $31$ ngày ($1, 3, 5, 7, 8, 10, 12$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tháng Tư có tất cả bao nhiêu ngày?',
            'options': ['$31$ ngày', '$28$ ngày', '$29$ ngày', '$30$ ngày'],
            'answer': 3,
            'solution': 'Tháng Tư thuộc nhóm các tháng có $30$ ngày ($4, 6, 9, 11$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Ngày – tháng**, quy tắc hoặc công thức nào sau đây xác định đúng **Tháng '
                 '31 ngày**?',
            'options': ['Tháng $1, 3, 5, 7, 8, 10, 12$ (các đốt lồi trên nắm tay)',
                        'Tháng $2, 3, 5, 7, 8, 10, 12$ (các đốt lồi trên nắm tay)',
                        'Tháng $1, 3, 5, 7, 8, 10, 11$ (các đốt lồi trên nắm tay)',
                        'Tháng $4, 6, 9, 11$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 30: Ngày – tháng, **Tháng 31 ngày** được xác định '
                        'bởi: Tháng $1, 3, 5, 7, 8, 10, 12$ (các đốt lồi trên nắm tay).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Ngày – tháng**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Tháng 30 ngày**?',
            'options': ['Tháng $5, 6, 9, 11$',
                        'Tháng $4, 6, 9, 11$',
                        'Tháng $4, 6, 9, 10$',
                        'Tháng $8, 6, 9, 11$'],
            'answer': 1,
            'solution': 'Trong Bài 30: Ngày – tháng, **Tháng 30 ngày** có công thức/quy tắc là: Tháng $4, 6, '
                        '9, 11$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu ngày $30$ tháng $4$ là Thứ Ba thì ngày $1$ tháng $5$ (ngay hôm sau) là thứ mấy?',
            'options': ['Thứ Hai', 'Thứ Năm', 'Thứ Tư', 'Chủ nhật'],
            'answer': 2,
            'solution': 'Tháng $4$ có $30$ ngày, nên ngay sau ngày $30$ tháng $4$ là ngày $1$ tháng $5$. '
                        'Liền sau Thứ Ba là Thứ Tư.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 30: Ngày – tháng**, nhận định nào sau đây là **chính xác**?',
            'options': ['Biết một tháng thường có $40$ hoặc $31$ ngày (riêng tháng Hai có $28$ hoặc $29$ '
                        'ngày).',
                        'Biết một tháng thường có $30$ hoặc $31$ ngày (riêng tháng Hai có $28$ hoặc $28$ '
                        'ngày).',
                        'Biết một tháng thường có $60$ hoặc $31$ ngày (riêng tháng Hai có $28$ hoặc $29$ '
                        'ngày).',
                        'Biết một tháng thường có $30$ hoặc $31$ ngày (riêng tháng Hai có $28$ hoặc $29$ '
                        'ngày).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 30: Ngày – tháng: Biết một tháng thường có $30$ hoặc '
                        '$31$ ngày (riêng tháng Hai có $28$ hoặc $29$ ngày).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Ngày $5$ tháng $9$ là Thứ Năm. Nhận định: “Ngày $12$ tháng $9$ là Thứ Sáu.”',
            'answer': False,
            'solution': 'Ta có $5 + 7 = 12$ nên ngày $12$ tháng $9$ phải cùng thứ với ngày $5$ tháng $9$, '
                        'tức là Thứ Năm. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 30: Ngày – tháng**, quy tắc **Tháng 31 ngày** được xác định bởi Tháng $1, 3, '
                 '5, 7, 8, 10, 12$ (các đốt lồi trên nắm tay) và khi áp dụng cho ví dụ “Ngày $5$ tháng $9$ '
                 'là Thứ Năm. Hỏi Thứ Năm tuần tiếp theo của tháng $9$ là ngày bao nhiêu?” ta có lời giải: '
                 'Vì $1$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng $9$).. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tháng 31 ngày** (Tháng $1, 3, 5, 7, 8, '
                        '10, 12$ (các đốt lồi trên nắm tay)) và lời giải ví dụ minh họa của Bài 30: Ngày – '
                        'tháng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 30: Ngày – tháng** để giải bài toán sau: Ngày $5$ '
                 'tháng $9$ là Thứ Năm. Hỏi Thứ Năm tuần tiếp theo của tháng $9$ là ngày bao nhiêu? Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $1$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng '
                        '$9$).',
                        'Vì $1$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 - 7 = 12$ (tháng '
                        '$9$).',
                        'Vì $1$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng '
                        '$8$).',
                        'Vì $2$ tuần có $7$ ngày nên Thứ Năm tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng '
                        '$9$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 30: Ngày – tháng: Vì $1$ tuần có $7$ ngày nên Thứ Năm '
                        'tuần tiếp theo là ngày: $5 + 7 = 12$ (tháng $9$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Thứ Hai tuần này là ngày $8$. Hỏi Thứ Hai tuần sau (trong cùng tháng đó) là ngày bao '
                 'nhiêu?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Thứ Hai tuần sau cách Thứ Hai tuần này $7$ ngày: $8 + 7 = 15$ (ngày $15$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd06-ngay-gio-thang',
  'context_title': 'Chủ đề 6: Ngày – giờ, giờ – phút, ngày – tháng',
  'context': 'SGK Toán 2 · Chủ đề 6: Một ngày có 24 giờ, một giờ có 60 phút, xem đồng hồ (kim phút chỉ số 3, '
             'số 6), ngày – tháng, xem lịch.',
  'title': 'Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch',
  'icon': '⌚',
  'description': 'Thực hành đọc giờ (15 phút, 30 phút), tính khoảng thời gian và giải bài toán về lịch.',
  'requirements': ['Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $15$ phút, giờ '
                   'hơn $30$ phút.',
                   'Tính được khoảng thời gian diễn ra một hoạt động đơn giản.',
                   'Kết hợp thông tin từ đồng hồ và tờ lịch để giải quyết tình huống thực tiễn.'],
  'definition': '- Khi kim ngắn qua số $a$ một chút và kim dài chỉ số $3$, đồng hồ chỉ **$a$ giờ $15$ '
                'phút**.\n'
                '- Khoảng thời gian từ $a$ giờ đến $b$ giờ (cùng buổi) là $(b - a)$ giờ.',
  'theory': '- **Đồng hồ điện tử:** Hiển thị dạng `14:30` nghĩa là $14$ giờ $30$ phút (hay $2$ giờ $30$ phút '
            'chiều).\n'
            '- **Tính thời gian hoạt động:** Lan bắt đầu học bài lúc $7$ giờ tối và học xong lúc $8$ giờ '
            'tối, vậy Lan đã học trong $8 - 7 = 1$ giờ ($60$ phút).\n'
            '- **Tính số ngày:** Nếu đi du lịch $3$ ngày bắt đầu từ ngày $10$ thì các ngày đi là ngày $10, '
            '11, 12$.',
  'formulas': [{'category': 'Tổng hợp kỹ năng xem giờ và lịch',
                'items': [{'name': 'Kim phút chỉ số 3',
                           'formula': 'Đọc là $\\dots$ giờ $15$ phút',
                           'note': 'Ví dụ: Kim ngắn qua số $3$, kim dài chỉ số $3 \\rightarrow 3$ giờ $15$ '
                                   'phút.'},
                          {'name': 'Kim phút chỉ số 6',
                           'formula': 'Đọc là $\\dots$ giờ $30$ phút (hoặc $\\dots$ giờ rưỡi)'},
                          {'name': 'Khoảng thời gian',
                           'formula': 'Từ $a$ giờ đến $b$ giờ là $(b - a)$ giờ'}]}],
  'example': 'Bố bắt đầu sửa xe lúc $8$ giờ sáng và sửa xong lúc $10$ giờ sáng. Hỏi bố sửa xe trong mấy giờ?',
  'example_answer': 'Thời gian bố sửa xe là: $10 - 8 = 2$ (giờ).',
  'real_life': 'Tự lập thời gian biểu học tập và sinh hoạt hằng ngày tại nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kim ngắn chỉ qua số $3$ (chưa đến số $4$), kim dài chỉ đúng số $3$. Đồng hồ chỉ:',
            'options': ['$4$ giờ $15$ phút', '$3$ giờ $3$ phút', '$3$ giờ $30$ phút', '$3$ giờ $15$ phút'],
            'answer': 3,
            'solution': 'Kim ngắn qua số $3$ là $3$ giờ, kim dài chỉ số $3$ là $15$ phút. Vậy đồng hồ chỉ '
                        '$3$ giờ $15$ phút.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Lan bắt đầu làm bài lúc $7$ giờ tối và làm xong lúc $8$ giờ tối. Lan đã làm bài trong bao '
                 'lâu?',
            'options': ['$1$ giờ', '$15$ phút', '$30$ phút', '$2$ giờ'],
            'answer': 0,
            'solution': 'Từ $7$ giờ tối đến $8$ giờ tối là $8 - 7 = 1$ giờ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Kim phút chỉ số 3**?',
            'options': ['Đọc là $\\dots$ giờ $16$ phút',
                        'Đọc là $\\dots$ giờ $15$ phút',
                        'Đọc là $\\dots$ giờ $14$ phút',
                        'Đọc là $\\dots$ giờ $30$ phút'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem '
                        'lịch, **Kim phút chỉ số 3** được xác định bởi: Đọc là $\\dots$ giờ $15$ phút. (Ví '
                        'dụ: Kim ngắn qua số $3$, kim dài chỉ số $3 \\rightarrow 3$ giờ $15$ phút.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Kim phút chỉ số 6**?',
            'options': ['Đọc là $\\dots$ giờ $40$ phút (hoặc $\\dots$ giờ rưỡi)',
                        'Đọc là $\\dots$ giờ $29$ phút (hoặc $\\dots$ giờ rưỡi)',
                        'Đọc là $\\dots$ giờ $30$ phút (hoặc $\\dots$ giờ rưỡi)',
                        'Đọc là $\\dots$ giờ $60$ phút (hoặc $\\dots$ giờ rưỡi)'],
            'answer': 2,
            'solution': 'Trong Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch, **Kim phút chỉ số 6** '
                        'có công thức/quy tắc là: Đọc là $\\dots$ giờ $30$ phút (hoặc $\\dots$ giờ rưỡi).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đồng hồ điện tử hiện `16:15`. Thời gian đó ứng với cách đọc nào buổi chiều?',
            'options': ['$6$ giờ $15$ phút chiều',
                        '$4$ giờ $30$ phút chiều',
                        '$6$ giờ $30$ phút chiều',
                        '$4$ giờ $15$ phút chiều'],
            'answer': 3,
            'solution': 'Vì $16 - 12 = 4$ nên `16:15` là $4$ giờ $15$ phút chiều.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $15$ phút, '
                        'giờ hơn $30$ phút.',
                        'Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $16$ phút, '
                        'giờ hơn $30$ phút.',
                        'Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $15$ phút, '
                        'giờ hơn $29$ phút.',
                        'Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $30$ phút, '
                        'giờ hơn $30$ phút.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch: '
                        'Đọc chính xác đồng hồ kim và đồng hồ điện tử ở các mốc giờ đúng, giờ hơn $15$ phút, '
                        'giờ hơn $30$ phút.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Từ $8$ giờ sáng đến $8$ giờ $30$ phút sáng là $30$ phút.”',
            'answer': True,
            'solution': 'Khoảng thời gian từ $8$ giờ đúng đến $8$ giờ $30$ phút chính là $30$ phút. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch**, quy tắc **Kim phút chỉ '
                 'số 3** được xác định bởi Đọc là $\\dots$ giờ $15$ phút và khi áp dụng cho ví dụ “Bố bắt '
                 'đầu sửa xe lúc $8$ giờ sáng và sửa xong lúc $10$ giờ sáng. Hỏi bố sửa xe trong mấy giờ?” '
                 'ta có lời giải: Thời gian bố sửa xe là: $10 - 8 = 2$ (giờ).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Kim phút chỉ số 3** (Đọc là $\\dots$ giờ '
                        '$15$ phút) và lời giải ví dụ minh họa của Bài 31: Thực hành và trải nghiệm xem đồng '
                        'hồ, xem lịch.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem '
                 'lịch** để giải bài toán sau: Bố bắt đầu sửa xe lúc $8$ giờ sáng và sửa xong lúc $10$ giờ '
                 'sáng. Hỏi bố sửa xe trong mấy giờ? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thời gian bố sửa xe là: $10 + 8 = 2$ (giờ).',
                        'Thời gian bố sửa xe là: $10 - 8 = 2$ (giờ).',
                        'Thời gian bố sửa xe là: $10 - 8 = 1$ (giờ).',
                        'Thời gian bố sửa xe là: $20 - 8 = 2$ (giờ).'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 31: Thực hành và trải nghiệm xem đồng hồ, xem lịch: Thời '
                        'gian bố sửa xe là: $10 - 8 = 2$ (giờ).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Chủ nhật tuần này là ngày $21$ tháng $11$. Hỏi Chủ nhật tuần trước là ngày bao nhiêu tháng '
                 '$11$?',
            'answer': ['14'],
            'unit': None,
            'solution': 'Chủ nhật tuần trước cách Chủ nhật tuần này $7$ ngày nên là ngày: $21 - 7 = 14$ '
                        '(tháng $11$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 2 · Chủ đề 7: Ôn phép cộng, phép trừ trong phạm vi 20, 100; ôn hình phẳng; ôn đo '
             'lường (kg, l, giờ, ngày tháng).',
  'title': 'Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100',
  'icon': '📝',
  'description': 'Củng cố cộng, trừ nhẩm qua 10 trong phạm vi 20 và đặt tính cộng, trừ có nhớ trong phạm vi '
                 '100.',
  'requirements': ['Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $10$) trong phạm vi $20$.',
                   'Đặt tính và tính đúng phép cộng, phép trừ (có nhớ) trong phạm vi $100$.',
                   'Giải được bài toán có lời văn về thêm, bớt, nhiều hơn, ít hơn, hơn kém nhau bao nhiêu.'],
  'definition': 'Hệ thống kiến thức số và phép tính học kì 1:\n'
                '- $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$.\n'
                '- $\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$.',
  'theory': '- **Tìm thành phần chưa biết:** Nếu $? + b = c$ thì $? = c - b$.\n'
            '- **Thứ tự thực hiện dãy tính có hai dấu phép tính:** Luôn thực hiện lần lượt từ trái sang '
            'phải, ví dụ: $63 - 25 + 12 = 38 + 12 = 50$.\n'
            '- Khi đặt tính có nhớ, luôn kiểm tra lại xem đã cộng $1$ (ở phép cộng có nhớ) hoặc trừ $1$ (ở '
            'phép trừ có nhớ) ở hàng chục hay chưa.',
  'formulas': [{'category': 'Tổng hợp công thức Số và Phép tính học kì 1',
                'items': [{'name': 'Thành phần phép tính',
                           'formula': '$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng};\\ \\text{Số bị '
                                      'trừ} - \\text{Số trừ} = \\text{Hiệu}$'},
                          {'name': 'Tìm số hạng',
                           'formula': '$\\text{Số hạng chưa biết} = \\text{Tổng} - \\text{Số hạng đã biết}$',
                           'note': 'Ví dụ: $? + 8 = 15 \\Rightarrow ? = 15 - 8 = 7$.'}]}],
  'example': 'Tính: $63 - 25 + 12 = ?$',
  'example_answer': 'Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 + 12 = 50$. Vậy $63 - 25 + 12 = '
                    '50$.',
  'real_life': 'Kiểm tra tổng số sản phẩm, số sách quyên góp, điểm thi đua cuối học kì 1.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép tính $54 - 19 = 35$, số $35$ được gọi là:',
            'options': ['Hiệu', 'Số bị trừ', 'Số trừ', 'Tổng'],
            'answer': 0,
            'solution': 'Kết quả của phép trừ được gọi là hiệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào dấu $?$ trong phép tính $? + 8 = 15$ là:',
            'options': ['$23$', '$7$', '$8$', '$6$'],
            'answer': 1,
            'solution': 'Ta lấy tổng trừ số hạng đã biết: $15 - 8 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Thành phần phép tính**?',
            'options': ['$\\text{Số hạng} - \\text{Số hạng} = \\text{Tổng};\\ \\text{Số bị trừ} - \\text{Số '
                        'trừ} = \\text{Hiệu}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng};\\ '
                        '\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$',
                        '$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng};\\ \\text{Số bị trừ} - \\text{Số '
                        'trừ} = \\text{Hiệu}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số hạng} + \\text{Số '
                        'hạng} = \\text{Tổng};\\ \\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, '
                        '100, **Thành phần phép tính** được xác định bởi: $\\text{Số hạng} + \\text{Số hạng} '
                        '= \\text{Tổng};\\ \\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Tìm số hạng**?',
            'options': ['$\\text{Số hạng chưa biết} = \\text{Tổng} + \\text{Số hạng đã biết}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số hạng chưa biết} = \\text{Tổng} - \\text{Số '
                        'hạng đã biết}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số hạng chưa biết} = '
                        '\\text{Tổng} - \\text{Số hạng đã biết}$',
                        '$\\text{Số hạng chưa biết} = \\text{Tổng} - \\text{Số hạng đã biết}$'],
            'answer': 3,
            'solution': 'Trong Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100, **Tìm số hạng** có '
                        'công thức/quy tắc là: $\\text{Số hạng chưa biết} = \\text{Tổng} - \\text{Số hạng đã '
                        'biết}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $63 - 25 + 12$ là:',
            'options': ['$50$', '$26$', '$38$', '$40$'],
            'answer': 0,
            'solution': 'Tính từ trái sang phải: $63 - 25 = 38$, rồi lấy $38 + 12 = 50$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $11$) trong phạm vi $20$.',
                        'Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $10$) trong phạm vi $20$.',
                        'Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $10$) trong phạm vi $19$.',
                        'Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $20$) trong phạm vi $20$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100: '
                        'Tính nhẩm thành thạo bảng cộng, bảng trừ (qua $10$) trong phạm vi $20$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Tổng của $47$ và $35$ bằng $82$.”',
            'answer': True,
            'solution': 'Ta có $47 + 35$: $7 + 5 = 12$ viết $2$ nhớ $1$; $4 + 3 + 1 = 8$, được $82$. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100**, quy tắc **Thành phần '
                 'phép tính** được xác định bởi $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng};\\ '
                 '\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$ và khi áp dụng cho ví dụ “Tính: $63 - '
                 '25 + 12 = ?$” ta có lời giải: Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 + 12 '
                 '= 50$. Vậy $63 - 25 + 12 = 50$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thành phần phép tính** ($\\text{Số hạng} '
                        '+ \\text{Số hạng} = \\text{Tổng};\\ \\text{Số bị trừ} - \\text{Số trừ} = '
                        '\\text{Hiệu}$) và lời giải ví dụ minh họa của Bài 33: Ôn tập phép cộng, phép trừ '
                        'trong phạm vi 20, 100.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, '
                 '100** để giải bài toán sau: Tính: $63 - 25 + 12 = ?$ Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 - 12 = 50$. Vậy $63 - 25 + '
                        '12 = 50$.',
                        'Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 + 12 = 50$. Vậy $63 - 25 + '
                        '12 = 49$.',
                        'Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 + 12 = 50$. Vậy $63 - 25 + '
                        '12 = 50$.',
                        'Tính từ trái sang phải: $65 - 25 = 38$, sau đó lấy $38 + 12 = 50$. Vậy $63 - 25 + '
                        '12 = 50$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 33: Ôn tập phép cộng, phép trừ trong phạm vi 20, 100: '
                        'Tính từ trái sang phải: $63 - 25 = 38$, sau đó lấy $38 + 12 = 50$. Vậy $63 - 25 + '
                        '12 = 50$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Đội Một trồng được $52$ cây hoa, đội Hai trồng được ít hơn đội Một $16$ cây hoa. Hỏi đội '
                 'Hai trồng được bao nhiêu cây hoa?',
            'answer': ['36'],
            'unit': None,
            'solution': 'Số cây hoa đội Hai trồng được là: $52 - 16 = 36$ (cây).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 2 · Chủ đề 7: Ôn phép cộng, phép trừ trong phạm vi 20, 100; ôn hình phẳng; ôn đo '
             'lường (kg, l, giờ, ngày tháng).',
  'title': 'Bài 34: Ôn tập hình phẳng',
  'icon': '📐',
  'description': 'Ôn tập điểm, đoạn thẳng, đường thẳng, đường cong, ba điểm thẳng hàng, đường gấp khúc và '
                 'hình tứ giác.',
  'requirements': ['Nhận diện đúng điểm, đoạn thẳng, đường thẳng, ba điểm thẳng hàng, đường gấp khúc, hình '
                   'tam giác, hình tứ giác.',
                   'Tính thành thạo độ dài đường gấp khúc có $2, 3$ hoặc $4$ đoạn thẳng.',
                   'Đếm đúng số hình tam giác, số hình tứ giác trong một hình vẽ.'],
  'definition': '- **Ba điểm thẳng hàng:** cùng nằm trên một đường thẳng.\n'
                '- **Độ dài đường gấp khúc:** bằng tổng độ dài các đoạn thẳng tạo nên đường gấp khúc đó.\n'
                '- **Hình tứ giác:** hình phẳng có $4$ đỉnh và $4$ cạnh.',
  'theory': '- Khi tính độ dài đường gấp khúc, ta cộng lần lượt độ dài các đoạn thẳng từ trái sang phải và '
            'ghi kèm đơn vị $\\text{cm}$.\n'
            '- Khi tìm độ dài một đoạn thẳng chưa biết của đường gấp khúc, ta lấy tổng độ dài cả đường gấp '
            'khúc trừ đi độ dài các đoạn thẳng đã biết.',
  'formulas': [{'category': 'Ôn tập công thức Hình phẳng học kì 1',
                'items': [{'name': 'Độ dài đường gấp khúc', 'formula': '$L = d_1 + d_2 + \\dots + d_n$'},
                          {'name': 'Tìm đoạn thẳng chưa biết',
                           'formula': '$d_2 = L - d_1$',
                           'note': 'Ví dụ: Đường gấp khúc $ABC$ dài $15\\text{ cm}$, $AB = 8\\text{ cm} '
                                   '\\Rightarrow BC = 15 - 8 = 7\\text{ cm}$.'}]}],
  'example': 'Đường gấp khúc $ABC$ gồm hai đoạn thẳng $AB = 9\\text{ cm}$ và $BC = 7\\text{ cm}$. Tính độ '
             'dài đường gấp khúc $ABC$.',
  'example_answer': 'Độ dài đường gấp khúc $ABC$ là: $9 + 7 = 16$ ($\\text{cm}$).',
  'real_life': 'Đo đạc kích thước đồ vật và tính quãng đường gấp khúc trong thực tế.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đường gấp khúc gồm hai đoạn thẳng dài $8\\text{ cm}$ và $7\\text{ cm}$ có độ dài là:',
            'options': ['$14\\text{ cm}$', '$15\\text{ cm}$', '$16\\text{ cm}$', '$1\\text{ cm}$'],
            'answer': 1,
            'solution': 'Độ dài đường gấp khúc là: $8 + 7 = 15$ ($\\text{cm}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình tứ giác có mấy đỉnh và mấy cạnh?',
            'options': ['$3$ đỉnh, $3$ cạnh',
                        '$4$ đỉnh, $3$ cạnh',
                        '$4$ đỉnh, $4$ cạnh',
                        '$5$ đỉnh, $5$ cạnh'],
            'answer': 2,
            'solution': 'Hình tứ giác luôn có $4$ đỉnh và $4$ cạnh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Ôn tập hình phẳng**, quy tắc hoặc công thức nào sau đây xác định đúng **Độ '
                 'dài đường gấp khúc**?',
            'options': ['$L = d_1 - d_2 + \\dots + d_n$',
                        'Đảo ngược vế của quy tắc: $L = d_1 + d_2 + \\dots + d_n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $L = d_1 + d_2 + \\dots + d_n$',
                        '$L = d_1 + d_2 + \\dots + d_n$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 34: Ôn tập hình phẳng, **Độ dài đường gấp khúc** '
                        'được xác định bởi: $L = d_1 + d_2 + \\dots + d_n$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Ôn tập hình phẳng**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Tìm đoạn thẳng chưa biết**?',
            'options': ['$d_2 = L - d_1$',
                        '$d_2 = L + d_1$',
                        'Đảo ngược vế của quy tắc: $d_2 = L - d_1$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $d_2 = L - d_1$'],
            'answer': 0,
            'solution': 'Trong Bài 34: Ôn tập hình phẳng, **Tìm đoạn thẳng chưa biết** có công thức/quy tắc '
                        'là: $d_2 = L - d_1$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình vuông được chia đôi bởi một đoạn thẳng nối trung điểm hai cạnh đối diện. Khi đó '
                 'trên hình có tất cả bao nhiêu hình tứ giác?',
            'options': ['$1$ hình tứ giác', '$3$ hình tứ giác', '$2$ hình tứ giác', '$4$ hình tứ giác'],
            'answer': 1,
            'solution': 'Có $2$ hình chữ nhật nhỏ và $1$ hình vuông lớn ban đầu, tất cả đều là hình tứ giác: '
                        '$2 + 1 = 3$ (hình tứ giác).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 34: Ôn tập hình phẳng**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận diện đúng điểm, đoạn thẳng, đường thẳng, ba điểm thẳng hàng, đường gấp khúc, '
                        'hình tam giác, hình tứ giác. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận diện đúng điểm, đoạn thẳng, đường thẳng, ba điểm '
                        'thẳng hàng, đường gấp khúc, hình tam giác, hình tứ giác.',
                        'Nhận diện đúng điểm, đoạn thẳng, đường thẳng, ba điểm thẳng hàng, đường gấp khúc, '
                        'hình tam giác, hình tứ giác.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận diện đúng điểm, đoạn '
                        'thẳng, đường thẳng, ba điểm thẳng hàng, đường gấp khúc, hình tam giác, hình tứ '
                        'giác.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 34: Ôn tập hình phẳng: Nhận diện đúng điểm, đoạn '
                        'thẳng, đường thẳng, ba điểm thẳng hàng, đường gấp khúc, hình tam giác, hình tứ '
                        'giác.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Ba đỉnh của một hình tam giác là ba điểm thẳng hàng.”',
            'answer': False,
            'solution': 'Ba đỉnh của một hình tam giác không cùng nằm trên một đường thẳng nên không thẳng '
                        'hàng. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 34: Ôn tập hình phẳng**, quy tắc **Độ dài đường gấp khúc** được xác định bởi '
                 '$L = d_1 + d_2 + \\dots + d_n$ và khi áp dụng cho ví dụ “Đường gấp khúc $ABC$ gồm hai đoạn '
                 'thẳng $AB = 9\\text{ cm}$ và $BC = 7\\text{ cm}$. Tính độ dài đường gấp khúc $ABC$.” ta có '
                 'lời giải: Độ dài đường gấp khúc $ABC$ là: $9 + 7 = 16$ ($\\text{cm}$).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Độ dài đường gấp khúc** ($L = d_1 + d_2 '
                        '+ \\dots + d_n$) và lời giải ví dụ minh họa của Bài 34: Ôn tập hình phẳng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 34: Ôn tập hình phẳng** để giải bài toán sau: Đường '
                 'gấp khúc $ABC$ gồm hai đoạn thẳng $AB = 9\\text{ cm}$ và $BC = 7\\text{ cm}$. Tính độ dài '
                 'đường gấp khúc $ABC$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Độ dài đường gấp khúc $ABC$ là: $9 - 7 = 16$ ($\\text{cm}$).',
                        'Độ dài đường gấp khúc $ABC$ là: $9 + 7 = 15$ ($\\text{cm}$).',
                        'Độ dài đường gấp khúc $ABC$ là: $18 + 7 = 16$ ($\\text{cm}$).',
                        'Độ dài đường gấp khúc $ABC$ là: $9 + 7 = 16$ ($\\text{cm}$).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 34: Ôn tập hình phẳng: Độ dài đường gấp khúc $ABC$ là: '
                        '$9 + 7 = 16$ ($\\text{cm}$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đường gấp khúc gồm $3$ đoạn thẳng dài lần lượt là $12\\text{ cm}$, $18\\text{ cm}$ và '
                 '$25\\text{ cm}$. Tính độ dài đường gấp khúc đó theo xăng-ti-mét.',
            'answer': ['55', '55cm', '55 cm'],
            'unit': None,
            'solution': 'Độ dài đường gấp khúc là: $12 + 18 + 25 = 30 + 25 = 55$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd07-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 7: Ôn tập học kì 1',
  'context': 'SGK Toán 2 · Chủ đề 7: Ôn phép cộng, phép trừ trong phạm vi 20, 100; ôn hình phẳng; ôn đo '
             'lường (kg, l, giờ, ngày tháng).',
  'title': 'Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1',
  'icon': '🏆',
  'description': 'Ôn tập các đơn vị đo khối lượng (kg), dung tích (l), độ dài (cm) và thời gian (giờ – phút, '
                 'ngày – tháng).',
  'requirements': ['Sử dụng đúng các đơn vị đo đã học: $\\text{cm}$ (độ dài), $\\text{kg}$ (khối lượng), '
                   '$\\text{l}$ (dung tích), giờ – phút – ngày – tháng (thời gian).',
                   'Đọc đúng giờ trên đồng hồ và tra cứu thông tin trên tờ lịch tháng.',
                   'Giải được các bài toán thực tế tổng hợp cuối học kì 1.'],
  'definition': 'Hệ thống các đơn vị đo lường học kì 1:\n'
                '- **Độ dài:** xăng-ti-mét ($\\text{cm}$).\n'
                '- **Khối lượng:** ki-lô-gam ($\\text{kg}$).\n'
                '- **Dung tích:** lít ($\\text{l}$).\n'
                '- **Thời gian:** $1$ ngày $= 24$ giờ, $1$ giờ $= 60$ phút, $1$ tuần lễ $= 7$ ngày.',
  'theory': '- Khi thực hiện phép tính có kèm đơn vị đo, phải giữ nguyên đơn vị đo ở kết quả.\n'
            '- Đổi giờ chiều, tối: $13$ giờ $= 1$ giờ chiều, ..., $18$ giờ $= 6$ giờ chiều, $19$ giờ $= 7$ '
            'giờ tối, ..., $21$ giờ $= 9$ giờ tối.',
  'formulas': [{'category': 'Tổng hợp Đo lường học kì 1',
                'items': [{'name': 'Các đơn vị cơ bản',
                           'formula': 'Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: '
                                      '$\\text{l}$'},
                          {'name': 'Quan hệ thời gian',
                           'formula': '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần $= 7$ ngày'}]}],
  'example': 'Buổi sáng cửa hàng bán được $35\\text{ kg}$ gạo, buổi chiều bán được nhiều hơn buổi sáng '
             '$18\\text{ kg}$ gạo. Hỏi buổi chiều cửa hàng bán được bao nhiêu ki-lô-gam gạo?',
  'example_answer': 'Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $35 + 18 = 53$ ($\\text{kg}$).',
  'real_life': 'Tổng kết học kì 1 và vận dụng đo lường, tính toán trong sinh hoạt gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị dùng để đo khối lượng (độ nặng) của một bao gạo là:',
            'options': ['Lít ($\\text{l}$)', 'Giờ', 'Ki-lô-gam ($\\text{kg}$)', 'Xăng-ti-mét ($\\text{cm}$)'],
            'answer': 2,
            'solution': 'Khối lượng của bao gạo được đo bằng đơn vị ki-lô-gam ($\\text{kg}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kim dài chỉ số $12$, kim ngắn chỉ số $4$. Đồng hồ chỉ mấy giờ?',
            'options': ['$12$ giờ $4$ phút', '$4$ giờ $30$ phút', '$12$ giờ', '$4$ giờ'],
            'answer': 3,
            'solution': 'Kim dài chỉ số $12$ là giờ đúng, kim ngắn chỉ số $4$ nên đồng hồ chỉ $4$ giờ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Các đơn vị cơ bản**?',
            'options': ['Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: $\\text{l}$',
                        'Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: $\\text{l}$ (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung '
                        'tích: $\\text{l}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Độ dài: $\\text{cm}$; Khối '
                        'lượng: $\\text{kg}$; Dung tích: $\\text{l}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1, '
                        '**Các đơn vị cơ bản** được xác định bởi: Độ dài: $\\text{cm}$; Khối lượng: '
                        '$\\text{kg}$; Dung tích: $\\text{l}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Quan hệ thời gian**?',
            'options': ['$2$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần $= 7$ ngày',
                        '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần $= 7$ ngày',
                        '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần $= 6$ ngày',
                        'Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: $\\text{l}$'],
            'answer': 1,
            'solution': 'Trong Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1, **Quan hệ thời gian** có '
                        'công thức/quy tắc là: $1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần $= 7$ '
                        'ngày.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Con lợn cân nặng $65\\text{ kg}$, con chó nhẹ hơn con lợn $48\\text{ kg}$. Con chó cân '
                 'nặng:',
            'options': ['$27\\text{ kg}$', '$23\\text{ kg}$', '$17\\text{ kg}$', '$113\\text{ kg}$'],
            'answer': 2,
            'solution': 'Con chó cân nặng là: $65 - 48 = 17$ ($\\text{kg}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Sử dụng đúng các đơn vị đo đã học: $\\text{cm}$ (độ dài), $\\text{kg}$ (khối '
                        'lượng), $\\text{l}$ (dung tích), giờ – phút – ngày – tháng (thời gian). (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Sử dụng đúng các đơn vị đo đã học: $\\text{cm}$ (độ dài), '
                        '$\\text{kg}$ (khối lượng), $\\text{l}$ (dung tích), giờ – phút – ngày – tháng (thời '
                        'gian).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Sử dụng đúng các đơn vị đo đã '
                        'học: $\\text{cm}$ (độ dài), $\\text{kg}$ (khối lượng), $\\text{l}$ (dung tích), giờ '
                        '– phút – ngày – tháng (thời gian).',
                        'Sử dụng đúng các đơn vị đo đã học: $\\text{cm}$ (độ dài), $\\text{kg}$ (khối '
                        'lượng), $\\text{l}$ (dung tích), giờ – phút – ngày – tháng (thời gian).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1: Sử dụng '
                        'đúng các đơn vị đo đã học: $\\text{cm}$ (độ dài), $\\text{kg}$ (khối lượng), '
                        '$\\text{l}$ (dung tích), giờ – phút – ngày – tháng (thời gian).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu ngày $10$ tháng $12$ là Thứ Sáu thì ngày $17$ tháng $12$ cũng là Thứ Sáu.”',
            'answer': True,
            'solution': 'Vì $10 + 7 = 17$ (cách nhau đúng $1$ tuần lễ) nên ngày $17$ tháng $12$ cũng là Thứ '
                        'Sáu. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1**, quy tắc **Các đơn vị cơ bản** '
                 'được xác định bởi Độ dài: $\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: $\\text{l}$ '
                 'và khi áp dụng cho ví dụ “Buổi sáng cửa hàng bán được $35\\text{ kg}$ gạo, buổi chiều bán '
                 'được nhiều hơn buổi sáng $18\\text{ kg}$ gạo. Hỏi buổi chiều cửa hàng bán...” ta có lời '
                 'giải: Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $35 + 18 = 53$ ($\\text{kg}$).. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Các đơn vị cơ bản** (Độ dài: '
                        '$\\text{cm}$; Khối lượng: $\\text{kg}$; Dung tích: $\\text{l}$) và lời giải ví dụ '
                        'minh họa của Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1** để '
                 'giải bài toán sau: Buổi sáng cửa hàng bán được $35\\text{ kg}$ gạo, buổi chiều bán được '
                 'nhiều hơn buổi sáng $18\\text{ kg}$ gạo. Hỏi buổi chiều cửa hàng bán được bao nhiêu '
                 'ki-lô-gam gạo? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $35 + 18 = 53$ ($\\text{kg}$).',
                        'Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $35 - 18 = 53$ ($\\text{kg}$).',
                        'Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $35 + 18 = 52$ ($\\text{kg}$).',
                        'Buổi chiều cửa hàng bán được số ki-lô-gam gạo là: $70 + 18 = 53$ ($\\text{kg}$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 35: Ôn tập đo lường và Ôn tập chung học kì 1: Buổi chiều '
                        'cửa hàng bán được số ki-lô-gam gạo là: $35 + 18 = 53$ ($\\text{kg}$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng buổi sáng bán được $46\\text{ l}$ dầu, buổi chiều bán được $38\\text{ l}$ '
                 'dầu. Hỏi cả ngày cửa hàng đó bán được bao nhiêu lít dầu?',
            'answer': ['84', '84l', '84 l'],
            'unit': None,
            'solution': 'Cả ngày cửa hàng bán được số lít dầu là: $46 + 38 = 84$ ($\\text{l}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 37: Phép nhân và Thừa số, tích',
  'icon': '✖️',
  'description': 'Nhận biết ý nghĩa phép nhân là tổng các số hạng bằng nhau; gọi tên thừa số và tích.',
  'requirements': ['Hiểu ý nghĩa của phép nhân: tổng của nhiều số hạng bằng nhau được viết gọn thành phép '
                   'nhân.',
                   'Nhận biết và gọi đúng tên các thành phần của phép nhân: **thừa số**, **tích**.',
                   'Biết tính chất đổi chỗ các thừa số ($a \\times b = b \\times a$).'],
  'definition': '- **Phép nhân** (dấu $\\times$) là cách viết gọn của một tổng các số hạng **bằng nhau**. Ví '
                'dụ: $2 + 2 + 2 = 6$ ($2$ được lấy $3$ lần), viết thành $2 \\times 3 = 6$.\n'
                '- Trong phép nhân $a \\times b = c$: $a$ và $b$ gọi là **thừa số**, $c$ gọi là **tích** '
                '(biểu thức $a \\times b$ cũng gọi là một tích).',
  'theory': '- **Cách chuyển từ tổng sang tích:**\n'
            '  + Thừa số thứ nhất là **số hạng lặp lại** (số được lấy).\n'
            '  + Thừa số thứ hai là **số lần lặp lại** (số số hạng).\n'
            '  + Ví dụ: $5 + 5 + 5 + 5 = 20$ ($5$ được lấy $4$ lần) $\\rightarrow 5 \\times 4 = 20$, đọc là '
            '“năm nhân bốn bằng hai mươi”.\n'
            '- **Tính chất đổi chỗ:** Khi đổi chỗ hai thừa số thì tích không thay đổi: $2 \\times 5 = 5 '
            '\\times 2 = 10$.',
  'formulas': [{'category': 'Ý nghĩa và thành phần của phép nhân',
                'items': [{'name': 'Từ tổng sang tích',
                           'formula': '$\\underbrace{a + a + \\dots + a}_{b\\text{ số hạng}} = a \\times b$',
                           'note': 'Ví dụ: $4 + 4 + 4 = 4 \\times 3 = 12$.'},
                          {'name': 'Thành phần phép nhân',
                           'formula': '$\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$'},
                          {'name': 'Tính chất giao hoán',
                           'formula': '$a \\times b = b \\times a$',
                           'note': 'Ví dụ: $5 \\times 4 = 4 \\times 5 = 20$.'}]}],
  'example': 'Viết tổng $3 + 3 + 3 + 3 = 12$ thành phép nhân rồi chỉ rõ các thừa số và tích.',
  'example_answer': 'Số $3$ được lấy $4$ lần nên viết thành phép nhân: $3 \\times 4 = 12$. Trong đó $3$ và '
                    '$4$ là các **thừa số**, $12$ là **tích**.',
  'real_life': 'Tính nhanh tổng số chân gà, số bánh xe ô tô, số bút trong các hộp có số lượng đều nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng $4 + 4 + 4$ được viết thành phép nhân nào dưới đây?',
            'options': ['$4 \\times 4$', '$3 + 4$', '$4 \\times 12$', '$4 \\times 3$'],
            'answer': 3,
            'solution': 'Số $4$ được lấy $3$ lần nên viết thành phép nhân $4 \\times 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép nhân $5 \\times 6 = 30$, số $30$ được gọi là gì?',
            'options': ['Tích', 'Thừa số', 'Thương', 'Tổng'],
            'answer': 0,
            'solution': 'Kết quả của phép nhân được gọi là tích.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 37: Phép nhân và Thừa số, tích**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Từ tổng sang tích**?',
            'options': ['$\\underbrace{a - a + \\dots + a}_{b\\text{ số hạng}} = a \\times b$',
                        '$\\underbrace{a + a + \\dots + a}_{b\\text{ số hạng}} = a \\times b$',
                        'Đảo ngược vế của quy tắc: $\\underbrace{a + a + \\dots + a}_{b\\text{ số hạng}} = a '
                        '\\times b$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\underbrace{a + a + \\dots + '
                        'a}_{b\\text{ số hạng}} = a \\times b$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 37: Phép nhân và Thừa số, tích, **Từ tổng sang '
                        'tích** được xác định bởi: $\\underbrace{a + a + \\dots + a}_{b\\text{ số hạng}} = a '
                        '\\times b$. (Ví dụ: $4 + 4 + 4 = 4 \\times 3 = 12$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 37: Phép nhân và Thừa số, tích**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Thành phần phép nhân**?',
            'options': ['$\\text{Thừa số} : \\text{Thừa số} = \\text{Tích}$',
                        'Đảo ngược vế của quy tắc: $\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$',
                        '$\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Thừa số} \\times '
                        '\\text{Thừa số} = \\text{Tích}$'],
            'answer': 2,
            'solution': 'Trong Bài 37: Phép nhân và Thừa số, tích, **Thành phần phép nhân** có công thức/quy '
                        'tắc là: $\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho phép nhân $6 \\times 3 = 18$. Tổng các số hạng bằng nhau tương ứng với phép nhân đó '
                 'là:',
            'options': ['$6 + 3 = 9$', '$3 + 3 + 3 = 9$', '$6 + 6 = 12$', '$6 + 6 + 6 = 18$'],
            'answer': 3,
            'solution': '$6 \\times 3$ nghĩa là $6$ được lấy $3$ lần: $6 + 6 + 6 = 18$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 37: Phép nhân và Thừa số, tích**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Hiểu ý nghĩa của phép nhân: tổng của nhiều số hạng bằng nhau được viết gọn thành '
                        'phép nhân.',
                        'Hiểu ý nghĩa của phép nhân: tổng của nhiều số hạng bằng nhau được viết gọn thành '
                        'phép nhân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu ý nghĩa của phép nhân: tổng của nhiều số hạng bằng '
                        'nhau được viết gọn thành phép nhân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu ý nghĩa của phép nhân: '
                        'tổng của nhiều số hạng bằng nhau được viết gọn thành phép nhân.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 37: Phép nhân và Thừa số, tích: Hiểu ý nghĩa của phép '
                        'nhân: tổng của nhiều số hạng bằng nhau được viết gọn thành phép nhân.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$5 \\times 4 = 4 \\times 5$.”',
            'answer': True,
            'solution': 'Khi đổi chỗ hai thừa số trong một tích thì tích không thay đổi ($20 = 20$). Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 37: Phép nhân và Thừa số, tích**, quy tắc **Từ tổng sang tích** được xác định '
                 'bởi $\\underbrace{a + a + \\dots + a}_{b\\text{ số hạng}} = a \\times b$ và khi áp dụng '
                 'cho ví dụ “Viết tổng $3 + 3 + 3 + 3 = 12$ thành phép nhân rồi chỉ rõ các thừa số và tích.” '
                 'ta có lời giải: Số $3$ được lấy $4$ lần nên viết thành phép nhân: $3 \\times 4 = 12$. '
                 'Trong đó $3$ và $4$ là các **thừa số**, $12$ là **tích**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Từ tổng sang tích** ($\\underbrace{a + a '
                        '+ \\dots + a}_{b\\text{ số hạng}} = a \\times b$) và lời giải ví dụ minh họa của '
                        'Bài 37: Phép nhân và Thừa số, tích.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 37: Phép nhân và Thừa số, tích** để giải bài toán '
                 'sau: Viết tổng $3 + 3 + 3 + 3 = 12$ thành phép nhân rồi chỉ rõ các thừa số và tích. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số $3$ được lấy $4$ lần nên viết thành phép nhân: $3 : 4 = 12$. Trong đó $3$ và $4$ '
                        'là các **thừa số**, $12$ là **tích**.',
                        'Số $3$ được lấy $4$ lần nên viết thành phép nhân: $3 \\times 4 = 12$. Trong đó $3$ '
                        'và $4$ là các **thừa số**, $12$ là **tích**.',
                        'Số $3$ được lấy $4$ lần nên viết thành phép nhân: $3 \\times 4 = 12$. Trong đó $3$ '
                        'và $4$ là các **thừa số**, $11$ là **tích**.',
                        'Số $6$ được lấy $4$ lần nên viết thành phép nhân: $3 \\times 4 = 12$. Trong đó $3$ '
                        'và $4$ là các **thừa số**, $12$ là **tích**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 37: Phép nhân và Thừa số, tích: Số $3$ được lấy $4$ lần '
                        'nên viết thành phép nhân: $3 \\times 4 = 12$. Trong đó $3$ và $4$ là các **thừa '
                        'số**, $12$ là **tích**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm tích, biết hai thừa số lần lượt là $2$ và $2$ (gợi ý: $2$ được lấy $2$ lần).',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $2 \\times 2 = 2 + 2 = 4$. Vậy tích bằng $4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 39: Bảng nhân 2',
  'icon': '2️⃣',
  'description': 'Lập và học thuộc bảng nhân 2; vận dụng bảng nhân 2 để tính nhẩm và giải toán.',
  'requirements': ['Lập và học thuộc lòng bảng nhân $2$ (từ $2 \\times 1 = 2$ đến $2 \\times 10 = 20$).',
                   'Đếm thêm $2$ thành thạo ($2, 4, 6, 8, 10, 12, 14, 16, 18, 20$).',
                   'Giải được bài toán có lời văn vận dụng bảng nhân $2$.'],
  'definition': '**Bảng nhân $2$** gồm các phép nhân có thừa số thứ nhất là $2$ và thừa số thứ hai tăng dần '
                'từ $1$ đến $10$. Các tích trong bảng nhân $2$ tạo thành dãy số đếm thêm $2$: $2, 4, 6, 8, '
                '10, 12, 14, 16, 18, 20$.',
  'theory': '- **Toàn bộ bảng nhân $2$:**\n'
            '  $2 \\times 1 = 2$; $2 \\times 2 = 4$; $2 \\times 3 = 6$; $2 \\times 4 = 8$; $2 \\times 5 = '
            '10$;\n'
            '  $2 \\times 6 = 12$; $2 \\times 7 = 14$; $2 \\times 8 = 16$; $2 \\times 9 = 18$; $2 \\times 10 '
            '= 20$.\n'
            '- **Nhận xét:** Mỗi tích sau bằng tích ngay trước nó cộng thêm $2$ đơn vị.',
  'formulas': [{'category': 'Bảng nhân 2',
                'items': [{'name': 'Nửa đầu (1 đến 5)',
                           'formula': '$2 \\times 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 '
                                      '= 8;\\ 2 \\times 5 = 10$'},
                          {'name': 'Nửa sau (6 đến 10)',
                           'formula': '$2 \\times 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 '
                                      '\\times 9 = 18;\\ 2 \\times 10 = 20$'},
                          {'name': 'Đếm thêm 2', 'formula': '$2, 4, 6, 8, 10, 12, 14, 16, 18, 20$'}]}],
  'example': 'Mỗi con gà có $2$ chân. Hỏi $6$ con gà có tất cả bao nhiêu cái chân?',
  'example_answer': 'Số chân của $6$ con gà là:\n$2 \\times 6 = 12$ (cái chân)\nĐáp số: $12$ cái chân.',
  'real_life': 'Đếm đũa theo đôi ($2$ chiếc), đếm dép theo đôi, tính số bánh của những chiếc xe đạp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $2 \\times 8$ là:',
            'options': ['$16$', '$10$', '$14$', '$18$'],
            'answer': 0,
            'solution': 'Theo bảng nhân $2$, ta có $2 \\times 8 = 16$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong dãy số đếm thêm $2$: $2, 4, 6, 8, ?, 12$, số thích hợp điền vào dấu $?$ là:',
            'options': ['$9$', '$10$', '$11$', '$14$'],
            'answer': 1,
            'solution': 'Đếm thêm $2$ từ $8$: $8 + 2 = 10$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39: Bảng nhân 2**, quy tắc hoặc công thức nào sau đây xác định đúng **Nửa đầu '
                 '(1 đến 5)**?',
            'options': ['$2 : 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 \\times 5 '
                        '= 10$',
                        '$2 \\times 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 '
                        '\\times 5 = 9$',
                        '$2 \\times 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 '
                        '\\times 5 = 10$',
                        '$4 \\times 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 '
                        '\\times 5 = 10$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 39: Bảng nhân 2, **Nửa đầu (1 đến 5)** được xác '
                        'định bởi: $2 \\times 1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = '
                        '8;\\ 2 \\times 5 = 10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 39: Bảng nhân 2**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Nửa '
                 'sau (6 đến 10)**?',
            'options': ['$2 : 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 \\times 9 = 18;\\ 2 '
                        '\\times 10 = 20$',
                        '$2 \\times 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 \\times 9 = 18;\\ 2 '
                        '\\times 10 = 19$',
                        '$4 \\times 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 \\times 9 = 18;\\ 2 '
                        '\\times 10 = 20$',
                        '$2 \\times 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 \\times 9 = 18;\\ 2 '
                        '\\times 10 = 20$'],
            'answer': 3,
            'solution': 'Trong Bài 39: Bảng nhân 2, **Nửa sau (6 đến 10)** có công thức/quy tắc là: $2 '
                        '\\times 6 = 12;\\ 2 \\times 7 = 14;\\ 2 \\times 8 = 16;\\ 2 \\times 9 = 18;\\ 2 '
                        '\\times 10 = 20$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mỗi đôi đũa có $2$ chiếc đũa. Hỏi $7$ đôi đũa có tất cả bao nhiêu chiếc đũa?',
            'options': ['$14$ chiếc', '$9$ chiếc', '$12$ chiếc', '$16$ chiếc'],
            'answer': 0,
            'solution': '$2$ chiếc được lấy $7$ lần: $2 \\times 7 = 14$ (chiếc đũa).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 39: Bảng nhân 2**, nhận định nào sau đây là **chính xác**?',
            'options': ['Lập và học thuộc lòng bảng nhân $2$ (từ $2 : 1 = 2$ đến $2 \\times 10 = 20$).',
                        'Lập và học thuộc lòng bảng nhân $2$ (từ $2 \\times 1 = 2$ đến $2 \\times 10 = 20$).',
                        'Lập và học thuộc lòng bảng nhân $2$ (từ $2 \\times 1 = 2$ đến $2 \\times 10 = 19$).',
                        'Lập và học thuộc lòng bảng nhân $4$ (từ $2 \\times 1 = 2$ đến $2 \\times 10 = '
                        '20$).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 39: Bảng nhân 2: Lập và học thuộc lòng bảng nhân $2$ '
                        '(từ $2 \\times 1 = 2$ đến $2 \\times 10 = 20$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$2 \\times 9 = 18$ và $2 \\times 6 = 14$.”',
            'answer': False,
            'solution': 'Ta có $2 \\times 9 = 18$ là đúng, nhưng $2 \\times 6 = 12$ (chứ không phải $14$, vì '
                        '$2 \\times 7 = 14$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 39: Bảng nhân 2**, quy tắc **Nửa đầu (1 đến 5)** được xác định bởi $2 \\times '
                 '1 = 2;\\ 2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 \\times 5 = 10$ và khi '
                 'áp dụng cho ví dụ “Mỗi con gà có $2$ chân. Hỏi $6$ con gà có tất cả bao nhiêu cái chân?” '
                 'ta có lời giải: Số chân của $6$ con gà là: $2 \\times 6 = 12$ (cái chân) Đáp số: $12$ cái '
                 'chân.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nửa đầu (1 đến 5)** ($2 \\times 1 = 2;\\ '
                        '2 \\times 2 = 4;\\ 2 \\times 3 = 6;\\ 2 \\times 4 = 8;\\ 2 \\times 5 = 10$) và lời '
                        'giải ví dụ minh họa của Bài 39: Bảng nhân 2.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 39: Bảng nhân 2** để giải bài toán sau: Mỗi con gà '
                 'có $2$ chân. Hỏi $6$ con gà có tất cả bao nhiêu cái chân? Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Số chân của $6$ con gà là: $2 : 6 = 12$ (cái chân) Đáp số: $12$ cái chân.',
                        'Số chân của $6$ con gà là: $2 \\times 6 = 12$ (cái chân) Đáp số: $11$ cái chân.',
                        'Số chân của $6$ con gà là: $2 \\times 6 = 12$ (cái chân) Đáp số: $12$ cái chân.',
                        'Số chân của $12$ con gà là: $2 \\times 6 = 12$ (cái chân) Đáp số: $12$ cái chân.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 39: Bảng nhân 2: Số chân của $6$ con gà là:\n'
                        '$2 \\times 6 = 12$ (cái chân)\n'
                        'Đáp số: $12$ cái chân.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi chiếc xe đạp có $2$ bánh xe. Hỏi $9$ chiếc xe đạp như thế có tất cả bao nhiêu bánh xe?',
            'answer': ['18'],
            'unit': None,
            'solution': 'Số bánh xe của $9$ chiếc xe đạp là: $2 \\times 9 = 18$ (bánh xe).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 40: Bảng nhân 5',
  'icon': '5️⃣',
  'description': 'Lập và học thuộc bảng nhân 5; vận dụng bảng nhân 5 để tính nhẩm và giải toán.',
  'requirements': ['Lập và học thuộc lòng bảng nhân $5$ (từ $5 \\times 1 = 5$ đến $5 \\times 10 = 50$).',
                   'Đếm thêm $5$ thành thạo ($5, 10, 15, 20, 25, 30, 35, 40, 45, 50$).',
                   'Giải được bài toán có lời văn vận dụng bảng nhân $5$.'],
  'definition': '**Bảng nhân $5$** gồm các phép nhân có thừa số thứ nhất là $5$ và thừa số thứ hai tăng dần '
                'từ $1$ đến $10$. Các tích trong bảng nhân $5$ luôn có chữ số tận cùng là **$5$** hoặc '
                '**$0$**.',
  'theory': '- **Toàn bộ bảng nhân $5$:**\n'
            '  $5 \\times 1 = 5$; $5 \\times 2 = 10$; $5 \\times 3 = 15$; $5 \\times 4 = 20$; $5 \\times 5 = '
            '25$;\n'
            '  $5 \\times 6 = 30$; $5 \\times 7 = 35$; $5 \\times 8 = 40$; $5 \\times 9 = 45$; $5 \\times 10 '
            '= 50$.\n'
            '- **Ứng dụng:** Xem số phút trên mặt đồng hồ (mỗi khoảng giữa hai số liên tiếp trên đồng hồ là '
            '$5$ phút: kim phút chỉ số $3$ là $5 \\times 3 = 15$ phút; chỉ số $6$ là $5 \\times 6 = 30$ '
            'phút).',
  'formulas': [{'category': 'Bảng nhân 5',
                'items': [{'name': 'Nửa đầu (1 đến 5)',
                           'formula': '$5 \\times 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times '
                                      '4 = 20;\\ 5 \\times 5 = 25$'},
                          {'name': 'Nửa sau (6 đến 10)',
                           'formula': '$5 \\times 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 '
                                      '\\times 9 = 45;\\ 5 \\times 10 = 50$'},
                          {'name': 'Đếm thêm 5', 'formula': '$5, 10, 15, 20, 25, 30, 35, 40, 45, 50$'}]}],
  'example': 'Mỗi bàn tay có $5$ ngón tay. Hỏi $8$ bàn tay có tất cả bao nhiêu ngón tay?',
  'example_answer': 'Số ngón tay của $8$ bàn tay là:\n$5 \\times 8 = 40$ (ngón tay)\nĐáp số: $40$ ngón tay.',
  'real_life': 'Đếm số ngón tay, số cánh hoa mai $5$ cánh, nhẩm số phút trên đồng hồ kim.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $5 \\times 9$ là:',
            'options': ['$40$', '$45$', '$14$', '$50$'],
            'answer': 1,
            'solution': 'Theo bảng nhân $5$, ta có $5 \\times 9 = 45$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $5 \\times 6$ là:',
            'options': ['$25$', '$35$', '$30$', '$11$'],
            'answer': 2,
            'solution': 'Theo bảng nhân $5$, ta có $5 \\times 6 = 30$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 40: Bảng nhân 5**, quy tắc hoặc công thức nào sau đây xác định đúng **Nửa đầu '
                 '(1 đến 5)**?',
            'options': ['$5 : 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 \\times '
                        '5 = 25$',
                        '$5 \\times 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 '
                        '\\times 5 = 24$',
                        '$10 \\times 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 '
                        '\\times 5 = 25$',
                        '$5 \\times 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 '
                        '\\times 5 = 25$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 40: Bảng nhân 5, **Nửa đầu (1 đến 5)** được xác '
                        'định bởi: $5 \\times 1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = '
                        '20;\\ 5 \\times 5 = 25$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 40: Bảng nhân 5**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Nửa '
                 'sau (6 đến 10)**?',
            'options': ['$5 \\times 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 \\times 9 = 45;\\ 5 '
                        '\\times 10 = 50$',
                        '$5 : 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 \\times 9 = 45;\\ 5 '
                        '\\times 10 = 50$',
                        '$5 \\times 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 \\times 9 = 45;\\ 5 '
                        '\\times 10 = 49$',
                        '$10 \\times 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 \\times 9 = 45;\\ 5 '
                        '\\times 10 = 50$'],
            'answer': 0,
            'solution': 'Trong Bài 40: Bảng nhân 5, **Nửa sau (6 đến 10)** có công thức/quy tắc là: $5 '
                        '\\times 6 = 30;\\ 5 \\times 7 = 35;\\ 5 \\times 8 = 40;\\ 5 \\times 9 = 45;\\ 5 '
                        '\\times 10 = 50$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mỗi bạn có $5$ que tính. Hỏi $7$ bạn có tất cả bao nhiêu que tính?',
            'options': ['$12$ que tính', '$35$ que tính', '$30$ que tính', '$40$ que tính'],
            'answer': 1,
            'solution': '$5$ que tính được lấy $7$ lần: $5 \\times 7 = 35$ (que tính).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 40: Bảng nhân 5**, nhận định nào sau đây là **chính xác**?',
            'options': ['Lập và học thuộc lòng bảng nhân $5$ (từ $5 : 1 = 5$ đến $5 \\times 10 = 50$).',
                        'Lập và học thuộc lòng bảng nhân $5$ (từ $5 \\times 1 = 5$ đến $5 \\times 10 = 49$).',
                        'Lập và học thuộc lòng bảng nhân $5$ (từ $5 \\times 1 = 5$ đến $5 \\times 10 = 50$).',
                        'Lập và học thuộc lòng bảng nhân $10$ (từ $5 \\times 1 = 5$ đến $5 \\times 10 = '
                        '50$).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 40: Bảng nhân 5: Lập và học thuộc lòng bảng nhân $5$ '
                        '(từ $5 \\times 1 = 5$ đến $5 \\times 10 = 50$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Tất cả các tích trong bảng nhân $5$ đều có chữ số hàng đơn vị là $0$ hoặc '
                 '$5$.”',
            'answer': True,
            'solution': 'Các tích trong bảng nhân $5$ là $5, 10, 15, 20, 25, 30, 35, 40, 45, 50$ đều tận '
                        'cùng bằng $0$ hoặc $5$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 40: Bảng nhân 5**, quy tắc **Nửa đầu (1 đến 5)** được xác định bởi $5 \\times '
                 '1 = 5;\\ 5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 \\times 5 = 25$ và '
                 'khi áp dụng cho ví dụ “Mỗi bàn tay có $5$ ngón tay. Hỏi $8$ bàn tay có tất cả bao nhiêu '
                 'ngón tay?” ta có lời giải: Số ngón tay của $8$ bàn tay là: $5 \\times 8 = 40$ (ngón tay) '
                 'Đáp số: $40$ ngón tay.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nửa đầu (1 đến 5)** ($5 \\times 1 = 5;\\ '
                        '5 \\times 2 = 10;\\ 5 \\times 3 = 15;\\ 5 \\times 4 = 20;\\ 5 \\times 5 = 25$) và '
                        'lời giải ví dụ minh họa của Bài 40: Bảng nhân 5.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 40: Bảng nhân 5** để giải bài toán sau: Mỗi bàn tay '
                 'có $5$ ngón tay. Hỏi $8$ bàn tay có tất cả bao nhiêu ngón tay? Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Số ngón tay của $8$ bàn tay là: $5 : 8 = 40$ (ngón tay) Đáp số: $40$ ngón tay.',
                        'Số ngón tay của $8$ bàn tay là: $5 \\times 8 = 40$ (ngón tay) Đáp số: $39$ ngón '
                        'tay.',
                        'Số ngón tay của $16$ bàn tay là: $5 \\times 8 = 40$ (ngón tay) Đáp số: $40$ ngón '
                        'tay.',
                        'Số ngón tay của $8$ bàn tay là: $5 \\times 8 = 40$ (ngón tay) Đáp số: $40$ ngón '
                        'tay.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 40: Bảng nhân 5: Số ngón tay của $8$ bàn tay là:\n'
                        '$5 \\times 8 = 40$ (ngón tay)\n'
                        'Đáp số: $40$ ngón tay.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi túi có $5\\text{ kg}$ gạo. Hỏi $8$ túi như thế có tất cả bao nhiêu ki-lô-gam gạo?',
            'answer': ['40', '40kg', '40 kg'],
            'unit': None,
            'solution': 'Số ki-lô-gam gạo của $8$ túi là: $5 \\times 8 = 40$ ($\\text{kg}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 41: Phép chia và Số bị chia, số chia, thương',
  'icon': '➗',
  'description': 'Nhận biết ý nghĩa phép chia, mối liên hệ giữa phép nhân và phép chia; gọi tên số bị chia, '
                 'số chia, thương.',
  'requirements': ['Hiểu hai ý nghĩa của phép chia: **chia thành các phần bằng nhau** và **chia theo nhóm**.',
                   'Biết mối liên hệ giữa phép nhân và phép chia: từ $1$ phép nhân lập được $2$ phép chia '
                   'tương ứng.',
                   'Gọi đúng tên các thành phần của phép chia: **số bị chia**, **số chia**, **thương**.'],
  'definition': '- **Phép chia** (ký hiệu dấu $:$) dùng để chia đều một số lượng thành các phần bằng nhau '
                'hoặc chia theo từng nhóm bằng nhau.\n'
                '- Trong phép chia $a : b = c$: $a$ gọi là **số bị chia**, $b$ gọi là **số chia**, $c$ gọi '
                'là **thương** (biểu thức $a : b$ cũng gọi là một thương).',
  'theory': '- **Hai tình huống thực tế của phép chia $8 : 2 = 4$:**\n'
            '  + *Chia thành các phần bằng nhau:* Có $8$ cái kẹo chia đều cho $2$ bạn, mỗi bạn được $4$ cái '
            'kẹo ($8 : 2 = 4$).\n'
            '  + *Chia theo nhóm:* Có $8$ cái kẹo chia cho mỗi bạn $2$ cái kẹo thì có $4$ bạn được nhận kẹo '
            '($8 : 2 = 4$).\n'
            '- **Liên hệ Nhân – Chia:** Từ phép nhân $2 \\times 4 = 8$, ta viết được hai phép chia: $8 : 2 = '
            '4$ và $8 : 4 = 2$.',
  'formulas': [{'category': 'Thành phần phép chia và liên hệ Nhân – Chia',
                'items': [{'name': 'Thành phần phép chia',
                           'formula': '$\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$',
                           'note': 'Ví dụ: $20 : 5 = 4$ ($20$: số bị chia, $5$: số chia, $4$: thương).'},
                          {'name': 'Từ nhân suy ra chia',
                           'formula': '$a \\times b = c \\Rightarrow c : a = b$ và $c : b = a$',
                           'note': 'Ví dụ: $2 \\times 9 = 18 \\Rightarrow 18 : 2 = 9;\\ 18 : 9 = 2$.'}]}],
  'example': 'Từ phép nhân $5 \\times 3 = 15$, hãy viết hai phép chia tương ứng và nêu số bị chia, số chia, '
             'thương của phép chia thứ nhất.',
  'example_answer': 'Hai phép chia là $15 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ là '
                    '**số bị chia**, $5$ là **số chia**, $3$ là **thương**.',
  'real_life': 'Chia đều bánh kẹo, chia lớp học thành các tổ hoặc nhóm học tập có số bạn bằng nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong phép chia $20 : 5 = 4$, số chia là số nào?',
            'options': ['$20$', '$4$', '$5$', '$25$'],
            'answer': 2,
            'solution': 'Số đứng sau dấu chia là số chia, vậy số chia là $5$ (còn $20$ là số bị chia, $4$ là '
                        'thương).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Từ phép nhân $2 \\times 9 = 18$, ta lập được phép chia đúng nào dưới đây?',
            'options': ['$18 : 3 = 6$', '$9 : 2 = 18$', '$18 : 9 = 3$', '$18 : 2 = 9$'],
            'answer': 3,
            'solution': 'Từ $2 \\times 9 = 18$ ta lập được hai phép chia là $18 : 2 = 9$ và $18 : 9 = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 41: Phép chia và Số bị chia, số chia, thương**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Thành phần phép chia**?',
            'options': ['$\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$',
                        '$\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bị chia} : \\text{Số '
                        'chia} = \\text{Thương}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 41: Phép chia và Số bị chia, số chia, thương, '
                        '**Thành phần phép chia** được xác định bởi: $\\text{Số bị chia} : \\text{Số chia} = '
                        '\\text{Thương}$. (Ví dụ: $20 : 5 = 4$ ($20$: số bị chia, $5$: số chia, $4$: '
                        'thương).)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 41: Phép chia và Số bị chia, số chia, thương**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Từ nhân suy ra chia**?',
            'options': ['$a : b = c \\Rightarrow c : a = b$ và $c : b = a$',
                        '$a \\times b = c \\Rightarrow c : a = b$ và $c : b = a$',
                        'Đảo ngược vế của quy tắc: $a \\times b = c \\Rightarrow c : a = b$ và $c : b = a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\times b = c \\Rightarrow c '
                        ': a = b$ và $c : b = a$'],
            'answer': 1,
            'solution': 'Trong Bài 41: Phép chia và Số bị chia, số chia, thương, **Từ nhân suy ra chia** có '
                        'công thức/quy tắc là: $a \\times b = c \\Rightarrow c : a = b$ và $c : b = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong phép chia $14 : 2 = 7$, số $14$ và số $7$ lần lượt được gọi là:',
            'options': ['Số chia và thương', 'Thừa số và tích', 'Số bị chia và thương', 'Số bị trừ và hiệu'],
            'answer': 2,
            'solution': 'Số $14$ đứng trước dấu chia là số bị chia, kết quả $7$ là thương.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 41: Phép chia và Số bị chia, số chia, thương**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Hiểu hai ý nghĩa của phép chia: **chia thành các phần bằng nhau** và **chia theo '
                        'nhóm**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu hai ý nghĩa của phép chia: **chia thành các phần '
                        'bằng nhau** và **chia theo nhóm**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu hai ý nghĩa của phép chia: '
                        '**chia thành các phần bằng nhau** và **chia theo nhóm**.',
                        'Hiểu hai ý nghĩa của phép chia: **chia thành các phần bằng nhau** và **chia theo '
                        'nhóm**.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 41: Phép chia và Số bị chia, số chia, thương: Hiểu '
                        'hai ý nghĩa của phép chia: **chia thành các phần bằng nhau** và **chia theo '
                        'nhóm**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Thương của $12$ và $2$ là $24$.”',
            'answer': False,
            'solution': 'Thương là kết quả của phép chia: $12 : 2 = 6$ (không phải $24$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 41: Phép chia và Số bị chia, số chia, thương**, quy tắc **Thành phần phép '
                 'chia** được xác định bởi $\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$ và khi áp '
                 'dụng cho ví dụ “Từ phép nhân $5 \\times 3 = 15$, hãy viết hai phép chia tương ứng và nêu '
                 'số bị chia, số chia, thương của phép chia thứ nhất.” ta có lời giải: Hai phép chia là $15 '
                 ': 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ là **số bị chia**, $5$ là '
                 '**số chia**, $3$ là **thươn.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thành phần phép chia** ($\\text{Số bị '
                        'chia} : \\text{Số chia} = \\text{Thương}$) và lời giải ví dụ minh họa của Bài 41: '
                        'Phép chia và Số bị chia, số chia, thương.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 41: Phép chia và Số bị chia, số chia, thương** để '
                 'giải bài toán sau: Từ phép nhân $5 \\times 3 = 15$, hãy viết hai phép chia tương ứng và '
                 'nêu số bị chia, số chia, thương của phép chia thứ nhất. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Hai phép chia là $15 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ '
                        'là **số bị chia**, $5$ là **số chia**, $3$ là **thương**.',
                        'Hai phép chia là $16 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ '
                        'là **số bị chia**, $5$ là **số chia**, $3$ là **thương**.',
                        'Hai phép chia là $15 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ '
                        'là **số bị chia**, $5$ là **số chia**, $2$ là **thương**.',
                        'Hai phép chia là $30 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ '
                        'là **số bị chia**, $5$ là **số chia**, $3$ là **thương**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 41: Phép chia và Số bị chia, số chia, thương: Hai phép '
                        'chia là $15 : 5 = 3$ và $15 : 3 = 5$. Trong phép chia $15 : 5 = 3$: $15$ là **số bị '
                        'chia**, $5$ là **số chia**, $3$ là **thương**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biết tích của hai thừa số $5$ và $6$ là $30$, tức là $5 \\times 6 = 30$. Vậy thương của '
                 '$30$ và $5$ bằng bao nhiêu?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Vì $5 \\times 6 = 30$ nên $30 : 5 = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 43: Bảng chia 2',
  'icon': '➗',
  'description': 'Lập và học thuộc bảng chia 2 từ bảng nhân 2; vận dụng giải toán thực tế.',
  'requirements': ['Lập và học thuộc lòng bảng chia $2$ (từ $2 : 2 = 1$ đến $20 : 2 = 10$).',
                   'Vận dụng bảng chia $2$ để tính nhẩm nhanh và giải bài toán chia thành $2$ phần bằng nhau '
                   'hoặc chia theo nhóm $2$.',
                   'Vận dụng kiến thức của **Bài 43: Bảng chia 2** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': '**Bảng chia $2$** được lập trực tiếp từ bảng nhân $2$: lấy các tích ($2, 4, 6, \\dots, 20$) '
                'chia cho $2$, ta được thương tăng dần từ $1$ đến $10$.',
  'theory': '- **Toàn bộ bảng chia $2$:**\n'
            '  $2 : 2 = 1$; $4 : 2 = 2$; $6 : 2 = 3$; $8 : 2 = 4$; $10 : 2 = 5$;\n'
            '  $12 : 2 = 6$; $14 : 2 = 7$; $16 : 2 = 8$; $18 : 2 = 9$; $20 : 2 = 10$.\n'
            '- **Cách nhẩm nhanh:** Muốn tính $16 : 2$, ta nhẩm xem $2$ nhân mấy bằng $16$: vì $2 \\times 8 '
            '= 16$ nên $16 : 2 = 8$.',
  'formulas': [{'category': 'Bảng chia 2',
                'items': [{'name': 'Nửa đầu (từ 2 đến 10)',
                           'formula': '$2 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$'},
                          {'name': 'Nửa sau (từ 12 đến 20)',
                           'formula': '$12 : 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = '
                                      '10$'}]}],
  'example': 'Có $18$ học sinh chia đều thành các nhóm, mỗi nhóm có $2$ bạn. Hỏi chia được tất cả bao nhiêu '
             'nhóm?',
  'example_answer': 'Số nhóm học sinh chia được là:\n$18 : 2 = 9$ (nhóm)\nĐáp số: $9$ nhóm.',
  'real_life': 'Xếp các chiếc tất, chiếc đũa, chiếc giày thành từng đôi ($2$ chiếc).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $16 : 2$ là:',
            'options': ['$7$', '$14$', '$32$', '$8$'],
            'answer': 3,
            'solution': 'Vì $2 \\times 8 = 16$ nên $16 : 2 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $10 : 2$ là:',
            'options': ['$5$', '$4$', '$8$', '$20$'],
            'answer': 0,
            'solution': 'Vì $2 \\times 5 = 10$ nên $10 : 2 = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 43: Bảng chia 2**, quy tắc hoặc công thức nào sau đây xác định đúng **Nửa đầu '
                 '(từ 2 đến 10)**?',
            'options': ['$3 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$',
                        '$2 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$',
                        '$2 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 4$',
                        '$4 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 43: Bảng chia 2, **Nửa đầu (từ 2 đến 10)** được '
                        'xác định bởi: $2 : 2 = 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 43: Bảng chia 2**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Nửa '
                 'sau (từ 12 đến 20)**?',
            'options': ['$13 : 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = 10$',
                        '$12 : 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = 9$',
                        '$12 : 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = 10$',
                        '$24 : 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = 10$'],
            'answer': 2,
            'solution': 'Trong Bài 43: Bảng chia 2, **Nửa sau (từ 12 đến 20)** có công thức/quy tắc là: $12 '
                        ': 2 = 6;\\ 14 : 2 = 7;\\ 16 : 2 = 8;\\ 18 : 2 = 9;\\ 20 : 2 = 10$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mẹ có $14$ cái bánh chia đều vào $2$ hộp. Hỏi mỗi hộp có mấy cái bánh?',
            'options': ['$6$ cái bánh', '$8$ cái bánh', '$12$ cái bánh', '$7$ cái bánh'],
            'answer': 3,
            'solution': 'Chia đều $14$ cái bánh vào $2$ hộp: $14 : 2 = 7$ (cái bánh).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 43: Bảng chia 2**, nhận định nào sau đây là **chính xác**?',
            'options': ['Lập và học thuộc lòng bảng chia $2$ (từ $2 : 2 = 1$ đến $20 : 2 = 10$).',
                        'Lập và học thuộc lòng bảng chia $3$ (từ $2 : 2 = 1$ đến $20 : 2 = 10$).',
                        'Lập và học thuộc lòng bảng chia $2$ (từ $2 : 2 = 1$ đến $20 : 2 = 9$).',
                        'Lập và học thuộc lòng bảng chia $4$ (từ $2 : 2 = 1$ đến $20 : 2 = 10$).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 43: Bảng chia 2: Lập và học thuộc lòng bảng chia $2$ '
                        '(từ $2 : 2 = 1$ đến $20 : 2 = 10$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$20\\text{ kg} : 2 = 10\\text{ kg}$.”',
            'answer': True,
            'solution': 'Ta có $20 : 2 = 10$, giữ nguyên đơn vị $\\text{kg}$ được $10\\text{ kg}$. Nhận định '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 43: Bảng chia 2**, quy tắc **Nửa đầu (từ 2 đến 10)** được xác định bởi $2 : 2 '
                 '= 1;\\ 4 : 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$ và khi áp dụng cho ví dụ “Có '
                 '$18$ học sinh chia đều thành các nhóm, mỗi nhóm có $2$ bạn. Hỏi chia được tất cả bao nhiêu '
                 'nhóm?” ta có lời giải: Số nhóm học sinh chia được là: $18 : 2 = 9$ (nhóm) Đáp số: $9$ '
                 'nhóm.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nửa đầu (từ 2 đến 10)** ($2 : 2 = 1;\\ 4 '
                        ': 2 = 2;\\ 6 : 2 = 3;\\ 8 : 2 = 4;\\ 10 : 2 = 5$) và lời giải ví dụ minh họa của '
                        'Bài 43: Bảng chia 2.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 43: Bảng chia 2** để giải bài toán sau: Có $18$ học '
                 'sinh chia đều thành các nhóm, mỗi nhóm có $2$ bạn. Hỏi chia được tất cả bao nhiêu nhóm? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số nhóm học sinh chia được là: $19 : 2 = 9$ (nhóm) Đáp số: $9$ nhóm.',
                        'Số nhóm học sinh chia được là: $18 : 2 = 9$ (nhóm) Đáp số: $9$ nhóm.',
                        'Số nhóm học sinh chia được là: $18 : 2 = 9$ (nhóm) Đáp số: $8$ nhóm.',
                        'Số nhóm học sinh chia được là: $36 : 2 = 9$ (nhóm) Đáp số: $9$ nhóm.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 43: Bảng chia 2: Số nhóm học sinh chia được là:\n'
                        '$18 : 2 = 9$ (nhóm)\n'
                        'Đáp số: $9$ nhóm.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có $18$ học sinh chia đều thành các nhóm, mỗi nhóm có $2$ bạn. Hỏi chia được tất cả bao '
                 'nhiêu nhóm?',
            'answer': ['9'],
            'unit': None,
            'solution': 'Số nhóm học sinh chia được là: $18 : 2 = 9$ (nhóm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd08-phep-nhan-phep-chia',
  'context_title': 'Chủ đề 8: Phép nhân, phép chia',
  'context': 'SGK Toán 2 · Chủ đề 8: Ý nghĩa phép nhân, phép chia; thừa số – tích; số bị chia – số chia – '
             'thương; bảng nhân 2, 5 và bảng chia 2, 5.',
  'title': 'Bài 44: Bảng chia 5',
  'icon': '🎯',
  'description': 'Lập và học thuộc bảng chia 5 từ bảng nhân 5; giải các bài toán tổng hợp về phép nhân, phép '
                 'chia.',
  'requirements': ['Lập và học thuộc lòng bảng chia $5$ (từ $5 : 5 = 1$ đến $50 : 5 = 10$).',
                   'Phân biệt đúng bài toán dùng phép nhân và bài toán dùng phép chia.',
                   'Giải thành thạo bài toán có lời văn liên quan đến bảng nhân, bảng chia $2$ và $5$.'],
  'definition': '**Bảng chia $5$** được lập trực tiếp từ bảng nhân $5$: lấy các tích ($5, 10, 15, \\dots, '
                '50$) chia cho $5$, ta được thương tăng dần từ $1$ đến $10$.',
  'theory': '- **Toàn bộ bảng chia $5$:**\n'
            '  $5 : 5 = 1$; $10 : 5 = 2$; $15 : 5 = 3$; $20 : 5 = 4$; $25 : 5 = 5$;\n'
            '  $30 : 5 = 6$; $35 : 5 = 7$; $40 : 5 = 8$; $45 : 5 = 9$; $50 : 5 = 10$.\n'
            '- **Cách phân biệt bài toán Nhân và Chia:**\n'
            '  + Cho biết giá trị $1$ phần, hỏi nhiều phần có tất cả bao nhiêu $\\rightarrow$ dùng **phép '
            'nhân**.\n'
            '  + Cho biết tổng số lượng, chia đều thành các phần hoặc các nhóm bằng nhau $\\rightarrow$ dùng '
            '**phép chia**.',
  'formulas': [{'category': 'Bảng chia 5',
                'items': [{'name': 'Nửa đầu (từ 5 đến 25)',
                           'formula': '$5 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$'},
                          {'name': 'Nửa sau (từ 30 đến 50)',
                           'formula': '$30 : 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = '
                                      '10$'}]}],
  'example': 'Có $15$ quả cam xếp đều vào $5$ đĩa. Hỏi mỗi đĩa có mấy quả cam?',
  'example_answer': 'Mỗi đĩa có số quả cam là:\n$15 : 5 = 3$ (quả cam)\nĐáp số: $3$ quả cam.',
  'real_life': 'Xếp học sinh thành các hàng $5$ bạn, chia vở thưởng đều cho $5$ bạn học sinh giỏi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $35 : 5$ là:',
            'options': ['$7$', '$5$', '$6$', '$8$'],
            'answer': 0,
            'solution': 'Vì $5 \\times 7 = 35$ nên $35 : 5 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Có $40$ quyển vở chia đều cho $5$ bạn. Mỗi bạn được mấy quyển vở?',
            'options': ['$35$ quyển', '$8$ quyển', '$45$ quyển', '$9$ quyển'],
            'answer': 1,
            'solution': 'Mỗi bạn được số quyển vở là: $40 : 5 = 8$ (quyển).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 44: Bảng chia 5**, quy tắc hoặc công thức nào sau đây xác định đúng **Nửa đầu '
                 '(từ 5 đến 25)**?',
            'options': ['$6 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$',
                        '$5 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 4$',
                        '$5 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$',
                        '$10 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 44: Bảng chia 5, **Nửa đầu (từ 5 đến 25)** được '
                        'xác định bởi: $5 : 5 = 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 44: Bảng chia 5**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Nửa '
                 'sau (từ 30 đến 50)**?',
            'options': ['$40 : 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = 10$',
                        '$30 : 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = 9$',
                        '$60 : 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = 10$',
                        '$30 : 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = 10$'],
            'answer': 3,
            'solution': 'Trong Bài 44: Bảng chia 5, **Nửa sau (từ 30 đến 50)** có công thức/quy tắc là: $30 '
                        ': 5 = 6;\\ 35 : 5 = 7;\\ 40 : 5 = 8;\\ 45 : 5 = 9;\\ 50 : 5 = 10$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $45 : 5 \\dots 2 \\times 4$ là:',
            'options': ['$>$', '$<$', '$=$', '$:$'],
            'answer': 0,
            'solution': 'Ta có $45 : 5 = 9$ và $2 \\times 4 = 8$. Vì $9 > 8$ nên điền dấu $>$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 44: Bảng chia 5**, nhận định nào sau đây là **chính xác**?',
            'options': ['Lập và học thuộc lòng bảng chia $6$ (từ $5 : 5 = 1$ đến $50 : 5 = 10$).',
                        'Lập và học thuộc lòng bảng chia $5$ (từ $5 : 5 = 1$ đến $50 : 5 = 10$).',
                        'Lập và học thuộc lòng bảng chia $5$ (từ $5 : 5 = 1$ đến $50 : 5 = 9$).',
                        'Lập và học thuộc lòng bảng chia $10$ (từ $5 : 5 = 1$ đến $50 : 5 = 10$).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 44: Bảng chia 5: Lập và học thuộc lòng bảng chia $5$ '
                        '(từ $5 : 5 = 1$ đến $50 : 5 = 10$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$25 : 5 = 5$ và $50 : 5 = 10$.”',
            'answer': True,
            'solution': 'Theo bảng chia $5$, $25 : 5 = 5$ và $50 : 5 = 10$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 44: Bảng chia 5**, quy tắc **Nửa đầu (từ 5 đến 25)** được xác định bởi $5 : 5 '
                 '= 1;\\ 10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$ và khi áp dụng cho ví dụ “Có '
                 '$15$ quả cam xếp đều vào $5$ đĩa. Hỏi mỗi đĩa có mấy quả cam?” ta có lời giải: Mỗi đĩa có '
                 'số quả cam là: $15 : 5 = 3$ (quả cam) Đáp số: $3$ quả cam.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nửa đầu (từ 5 đến 25)** ($5 : 5 = 1;\\ '
                        '10 : 5 = 2;\\ 15 : 5 = 3;\\ 20 : 5 = 4;\\ 25 : 5 = 5$) và lời giải ví dụ minh họa '
                        'của Bài 44: Bảng chia 5.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 44: Bảng chia 5** để giải bài toán sau: Có $15$ quả '
                 'cam xếp đều vào $5$ đĩa. Hỏi mỗi đĩa có mấy quả cam? Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Mỗi đĩa có số quả cam là: $16 : 5 = 3$ (quả cam) Đáp số: $3$ quả cam.',
                        'Mỗi đĩa có số quả cam là: $15 : 5 = 3$ (quả cam) Đáp số: $2$ quả cam.',
                        'Mỗi đĩa có số quả cam là: $15 : 5 = 3$ (quả cam) Đáp số: $3$ quả cam.',
                        'Mỗi đĩa có số quả cam là: $30 : 5 = 3$ (quả cam) Đáp số: $3$ quả cam.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 44: Bảng chia 5: Mỗi đĩa có số quả cam là:\n'
                        '$15 : 5 = 3$ (quả cam)\n'
                        'Đáp số: $3$ quả cam.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rót đều $30\\text{ l}$ mật ong vào các can, mỗi can chứa $5\\text{ l}$. Hỏi rót được tất '
                 'cả mấy can mật ong?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Số can mật ong rót được là: $30 : 5 = 6$ (can).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd09-lam-quen-voi-hinh-khoi',
  'context_title': 'Chủ đề 9: Làm quen với hình khối',
  'context': 'SGK Toán 2 · Chủ đề 9: Nhận dạng khối trụ, khối cầu qua vật thật và mô hình.',
  'title': 'Bài 46: Khối trụ, khối cầu',
  'icon': '🧊',
  'description': 'Nhận dạng khối trụ, khối cầu và tìm hiểu đặc điểm mặt đáy, khả năng lăn của từng khối.',
  'requirements': ['Nhận dạng được **khối trụ** và **khối cầu** qua mô hình và vật thật.',
                   'Hiểu đặc điểm: khối cầu lăn được về mọi phía; khối trụ có $2$ mặt đáy là hình tròn bằng '
                   'nhau.',
                   'Vận dụng kiến thức của **Bài 46: Khối trụ, khối cầu** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '- **Khối cầu:** tròn đều về mọi phía, không có mặt phẳng nào, lăn được theo mọi hướng.\n'
                '- **Khối trụ:** có $2$ mặt đáy phẳng là **hình tròn** bằng nhau và mặt xung quanh cong; khi '
                'đặt đứng thì đứng vững, khi đặt nằm ngang thì lăn được.',
  'theory': '- **Thử nghiệm lăn và xếp chồng:**\n'
            '  + **Khối cầu** (như quả bóng, viên bi): lăn được về mọi hướng nhưng không thể xếp chồng vững '
            'chắc lên nhau.\n'
            '  + **Khối trụ** (như khúc gỗ tròn, hộp sữa tròn): có thể đặt đứng và xếp chồng theo hai mặt '
            'đáy phẳng hình tròn, hoặc đặt nằm để lăn.',
  'formulas': [{'category': 'Đặc điểm Khối cầu và Khối trụ',
                'items': [{'name': 'Khối cầu', 'formula': 'Tròn đều mọi phía, $0$ mặt phẳng, lăn mọi hướng'},
                          {'name': 'Khối trụ',
                           'formula': 'Có $2$ mặt đáy là hình tròn bằng nhau + mặt xung quanh cong'}]}],
  'example': 'Vì sao người ta làm quả bóng đá có dạng khối cầu mà không làm dạng khối lập phương?',
  'example_answer': 'Vì **khối cầu** tròn đều về mọi phía và lăn được dễ dàng theo mọi hướng trên sân cỏ.',
  'real_life': 'Nhận biết hình dạng quả địa cầu, quả bóng, lon nước ngọt, hộp sữa ông thọ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khối trụ có mấy mặt đáy là hình tròn?',
            'options': ['$1$ mặt đáy', '$2$ mặt đáy', '$3$ mặt đáy', 'Không có mặt đáy nào'],
            'answer': 1,
            'solution': 'Khối trụ có $2$ mặt đáy phẳng là $2$ hình tròn bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khối nào dưới đây tròn đều về mọi phía và lăn được theo mọi hướng?',
            'options': ['Khối trụ', 'Khối lập phương', 'Khối cầu', 'Khối hộp chữ nhật'],
            'answer': 2,
            'solution': 'Khối cầu tròn đều về mọi phía nên lăn được theo mọi hướng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 46: Khối trụ, khối cầu**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Khối cầu**?',
            'options': ['Tròn đều mọi phía, $1$ mặt phẳng, lăn mọi hướng',
                        'Tròn đều mọi phía, $2$ mặt phẳng, lăn mọi hướng',
                        'Có $2$ mặt đáy là hình tròn bằng nhau + mặt xung quanh cong',
                        'Tròn đều mọi phía, $0$ mặt phẳng, lăn mọi hướng'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 46: Khối trụ, khối cầu, **Khối cầu** được xác định '
                        'bởi: Tròn đều mọi phía, $0$ mặt phẳng, lăn mọi hướng.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 46: Khối trụ, khối cầu**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Khối trụ**?',
            'options': ['Có $2$ mặt đáy là hình tròn bằng nhau + mặt xung quanh cong',
                        'Có $2$ mặt đáy là hình tròn bằng nhau - mặt xung quanh cong',
                        'Có $1$ mặt đáy là hình tròn bằng nhau + mặt xung quanh cong',
                        'Có $4$ mặt đáy là hình tròn bằng nhau + mặt xung quanh cong'],
            'answer': 0,
            'solution': 'Trong Bài 46: Khối trụ, khối cầu, **Khối trụ** có công thức/quy tắc là: Có $2$ mặt '
                        'đáy là hình tròn bằng nhau + mặt xung quanh cong.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi đặt nằm ngang trên mặt bàn phẳng, khối trụ có đặc điểm gì?',
            'options': ['Không thể lăn được',
                        'Lăn được dọc theo mặt cong xung quanh',
                        'Có $6$ mặt vuông',
                        'Biến thành khối cầu'],
            'answer': 1,
            'solution': 'Khi đặt nằm ngang, mặt xung quanh cong của khối trụ tiếp xúc với mặt bàn nên lăn '
                        'được.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 46: Khối trụ, khối cầu**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận dạng được **khối trụ** và **khối cầu** qua mô hình và vật thật. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Nhận dạng được **khối trụ** và **khối cầu** qua mô hình '
                        'và vật thật.',
                        'Nhận dạng được **khối trụ** và **khối cầu** qua mô hình và vật thật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận dạng được **khối trụ** và '
                        '**khối cầu** qua mô hình và vật thật.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 46: Khối trụ, khối cầu: Nhận dạng được **khối trụ** '
                        'và **khối cầu** qua mô hình và vật thật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Khối cầu có thể đặt chồng lên nhau thật cao và thật vững giống như khối lập '
                 'phương.”',
            'answer': False,
            'solution': 'Khối cầu không có mặt phẳng nào nên rất dễ lăn, không thể xếp chồng vững như khối '
                        'lập phương. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 46: Khối trụ, khối cầu**, quy tắc **Khối cầu** được xác định bởi Tròn đều mọi '
                 'phía, $0$ mặt phẳng, lăn mọi hướng và khi áp dụng cho ví dụ “Vì sao người ta làm quả bóng '
                 'đá có dạng khối cầu mà không làm dạng khối lập phương?” ta có lời giải: Vì **khối cầu** '
                 'tròn đều về mọi phía và lăn được dễ dàng theo mọi hướng trên sân cỏ.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Khối cầu** (Tròn đều mọi phía, $0$ mặt '
                        'phẳng, lăn mọi hướng) và lời giải ví dụ minh họa của Bài 46: Khối trụ, khối cầu.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 46: Khối trụ, khối cầu** để giải bài toán sau: Vì '
                 'sao người ta làm quả bóng đá có dạng khối cầu mà không làm dạng khối lập phương? Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        'Vì **khối cầu** tròn đều về mọi phía và lăn được dễ dàng theo mọi hướng trên sân '
                        'cỏ.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 46: Khối trụ, khối cầu: Vì **khối cầu** tròn đều về mọi '
                        'phía và lăn được dễ dàng theo mọi hướng trên sân cỏ.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai mặt đáy của một khối trụ là hai hình phẳng có cùng tên gọi. Mỗi mặt đáy đó có mấy cạnh '
                 'thẳng?',
            'answer': ['0'],
            'unit': None,
            'solution': 'Hai mặt đáy của khối trụ là hình tròn, mà hình tròn là đường cong khép kín nên có '
                        '$0$ cạnh thẳng.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd09-lam-quen-voi-hinh-khoi',
  'context_title': 'Chủ đề 9: Làm quen với hình khối',
  'context': 'SGK Toán 2 · Chủ đề 9: Nhận dạng khối trụ, khối cầu qua vật thật và mô hình.',
  'title': 'Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu',
  'icon': '⚽',
  'description': 'Phân loại các đồ vật quen thuộc trong đời sống có dạng khối trụ và khối cầu.',
  'requirements': ['Nhận biết và kể tên được các đồ vật thực tế có dạng khối trụ, khối cầu.',
                   'Phân loại đúng các đồ vật theo nhóm hình khối tương ứng.',
                   'Vận dụng kiến thức của **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Đồ vật dạng khối cầu:** quả bóng đá, quả bóng bàn, viên bi ve, quả địa cầu, quả cam '
                'tròn.\n'
                '- **Đồ vật dạng khối trụ:** lon nước ngọt, hộp sữa đặc, cục pin tiểu, cây nến trụ, cái '
                'trống trường, khúc gỗ tròn.',
  'theory': '- Khi phân loại đồ vật trong thực tế:\n'
            '  + Hãy quan sát xem vật đó có **hai đầu phẳng hình tròn** và thân dài tròn không '
            '$\\rightarrow$ nếu có thì đó là **khối trụ**.\n'
            '  + Nếu vật đó **tròn xoe như quả bóng** $\\rightarrow$ đó là **khối cầu**.',
  'formulas': [{'category': 'Ví dụ thực tế về Khối trụ và Khối cầu',
                'items': [{'name': 'Vật dạng khối cầu',
                           'formula': 'Quả bóng đá, quả bóng rổ, viên bi, quả địa cầu'},
                          {'name': 'Vật dạng khối trụ',
                           'formula': 'Lon nước ngọt, hộp sữa tròn, cục pin, cái trống, ống nhựa'}]}],
  'example': 'Cho các đồ vật: quả bóng rổ, cục pin, viên bi, lon nước ngọt. Hãy chia chúng thành hai nhóm: '
             'dạng khối cầu và dạng khối trụ.',
  'example_answer': '- Nhóm dạng **khối cầu**: quả bóng rổ, viên bi.\n'
                    '- Nhóm dạng **khối trụ**: cục pin, lon nước ngọt.',
  'real_life': 'Ứng dụng hình dạng khối trụ làm bánh xe lu đường, làm ống dẫn nước, cột nhà.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Quả bóng đá có dạng hình khối gì?',
            'options': ['Khối trụ', 'Khối lập phương', 'Khối cầu', 'Khối hộp chữ nhật'],
            'answer': 2,
            'solution': 'Quả bóng đá tròn đều về mọi phía nên có dạng khối cầu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Lon sữa bò (hoặc lon nước ngọt) có dạng hình khối gì?',
            'options': ['Khối cầu', 'Khối lập phương', 'Khối hộp chữ nhật', 'Khối trụ'],
            'answer': 3,
            'solution': 'Lon sữa bò có $2$ mặt đáy hình tròn và thân cong nên có dạng khối trụ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Vật dạng khối cầu**?',
            'options': ['Quả bóng đá, quả bóng rổ, viên bi, quả địa cầu',
                        'Quả bóng đá, quả bóng rổ, viên bi, quả địa cầu (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Quả bóng đá, quả bóng rổ, viên bi, quả địa cầu',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Quả bóng đá, quả bóng rổ, viên '
                        'bi, quả địa cầu'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối '
                        'cầu, **Vật dạng khối cầu** được xác định bởi: Quả bóng đá, quả bóng rổ, viên bi, '
                        'quả địa cầu.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Vật dạng khối trụ**?',
            'options': ['Lon nước ngọt, hộp sữa tròn, cục pin, cái trống, ống nhựa (với dấu ngược lại)',
                        'Lon nước ngọt, hộp sữa tròn, cục pin, cái trống, ống nhựa',
                        'Đảo ngược vế của quy tắc: Lon nước ngọt, hộp sữa tròn, cục pin, cái trống, ống nhựa',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Lon nước ngọt, hộp sữa tròn, '
                        'cục pin, cái trống, ống nhựa'],
            'answer': 1,
            'solution': 'Trong Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu, **Vật dạng khối '
                        'trụ** có công thức/quy tắc là: Lon nước ngọt, hộp sữa tròn, cục pin, cái trống, ống '
                        'nhựa.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các đồ vật sau: viên bi, cục pin, hộp bút chữ nhật, viên gạch, đồ vật nào có dạng '
                 'khối cầu?',
            'options': ['Cục pin', 'Hộp bút', 'Viên bi', 'Viên gạch'],
            'answer': 2,
            'solution': 'Viên bi tròn đều nên có dạng khối cầu (cục pin là khối trụ; hộp bút, viên gạch là '
                        'khối hộp chữ nhật).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết và kể tên được các đồ vật thực tế có dạng khối trụ, khối cầu. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và kể tên được các đồ vật thực tế có dạng khối '
                        'trụ, khối cầu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và kể tên được các đồ '
                        'vật thực tế có dạng khối trụ, khối cầu.',
                        'Nhận biết và kể tên được các đồ vật thực tế có dạng khối trụ, khối cầu.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối '
                        'cầu: Nhận biết và kể tên được các đồ vật thực tế có dạng khối trụ, khối cầu.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Cái trống trường có dạng khối trụ.”',
            'answer': True,
            'solution': 'Cái trống có $2$ mặt trống hình tròn và thân trống cong nên có dạng khối trụ. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu**, quy tắc **Vật dạng '
                 'khối cầu** được xác định bởi Quả bóng đá, quả bóng rổ, viên bi, quả địa cầu và khi áp dụng '
                 'cho ví dụ “Cho các đồ vật: quả bóng rổ, cục pin, viên bi, lon nước ngọt. Hãy chia chúng '
                 'thành hai nhóm: dạng khối cầu và dạng khối trụ.” ta có lời giải: - Nhóm dạng **khối cầu**: '
                 'quả bóng rổ, viên bi. - Nhóm dạng **khối trụ**: cục pin, lon nước ngọt.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Vật dạng khối cầu** (Quả bóng đá, quả '
                        'bóng rổ, viên bi, quả địa cầu) và lời giải ví dụ minh họa của Bài 47: Thực hành '
                        'nhận biết đồ vật dạng khối trụ, khối cầu.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối '
                 'cầu** để giải bài toán sau: Cho các đồ vật: quả bóng rổ, cục pin, viên bi, lon nước ngọt. '
                 'Hãy chia chúng thành hai nhóm: dạng khối cầu và dạng khối trụ. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['- Nhóm dạng **khối cầu**: quả bóng rổ, viên bi. - Nhóm dạng **khối trụ**: cục pin, '
                        'lon nước ngọt.',
                        '- Nhóm dạng **khối cầu**: quả bóng rổ, viên bi. + Nhóm dạng **khối trụ**: cục pin, '
                        'lon nước ngọt.',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 47: Thực hành nhận biết đồ vật dạng khối trụ, khối cầu: '
                        '- Nhóm dạng **khối cầu**: quả bóng rổ, viên bi.\n'
                        '- Nhóm dạng **khối trụ**: cục pin, lon nước ngọt.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên bàn có $4$ quả bóng bàn, $2$ cục pin và $3$ viên bi. Hỏi trên bàn có tất cả bao nhiêu '
                 'đồ vật có dạng khối cầu?',
            'answer': ['7'],
            'unit': None,
            'solution': 'Quả bóng bàn ($4$ quả) và viên bi ($3$ viên) đều có dạng khối cầu: $4 + 3 = 7$ (đồ '
                        'vật).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd09-lam-quen-voi-hinh-khoi',
  'context_title': 'Chủ đề 9: Làm quen với hình khối',
  'context': 'SGK Toán 2 · Chủ đề 9: Nhận dạng khối trụ, khối cầu qua vật thật và mô hình.',
  'title': 'Bài 47B: Luyện tập chung về các hình khối',
  'icon': '🏰',
  'description': 'Tổng hợp phân biệt và đếm 4 loại hình khối đã học: khối lập phương, khối hộp chữ nhật, '
                 'khối trụ, khối cầu.',
  'requirements': ['Phân biệt được cả $4$ loại hình khối đã học ở lớp 1 và lớp 2: **khối lập phương**, '
                   '**khối hộp chữ nhật**, **khối trụ**, **khối cầu**.',
                   'Đếm đúng số lượng từng loại hình khối trong các mô hình lắp ghép (rô-bốt, tàu hỏa, lâu '
                   'đài).',
                   'Vận dụng kiến thức của **Bài 47B: Luyện tập chung về các hình khối** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Bốn hình khối cơ bản ở Tiểu học:\n'
                '1. **Khối lập phương:** $6$ mặt phẳng đều là hình vuông.\n'
                '2. **Khối hộp chữ nhật:** $6$ mặt phẳng là hình chữ nhật.\n'
                '3. **Khối trụ:** $2$ mặt đáy phẳng hình tròn và mặt xung quanh cong.\n'
                '4. **Khối cầu:** tròn đều mọi phía, không có mặt phẳng.',
  'theory': '- Khi xây tháp hoặc xếp hình mô hình, người ta thường đặt **khối lập phương**, **khối hộp chữ '
            'nhật** hoặc **khối trụ (đặt đứng)** ở bên dưới làm chân đế vì chúng có mặt phẳng đứng vững; còn '
            '**khối cầu** thường đặt trên đỉnh hoặc đặt trong rãnh.',
  'formulas': [{'category': 'Tổng hợp 4 loại hình khối',
                'items': [{'name': 'Có 6 mặt phẳng',
                           'formula': 'Khối lập phương ($6$ mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ '
                                      'nhật)'},
                          {'name': 'Có mặt cong',
                           'formula': 'Khối trụ ($2$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng)'}]}],
  'example': 'Một mô hình chú rô-bốt được ghép bởi: đầu là $1$ khối cầu, thân là $1$ khối hộp chữ nhật, $2$ '
             'cánh tay và $2$ chân là $4$ khối trụ. Hỏi mô hình có tất cả bao nhiêu khối trụ?',
  'example_answer': 'Mô hình có $2$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 4$ khối trụ.',
  'real_life': 'Thiết kế đồ chơi lắp ghép, nhận diện các khối kiến trúc xung quanh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bạn Nam muốn xây một cái tháp cao bằng các khối sao cho chân tháp đứng thật vững và không '
                 'bị lăn. Nam nên chọn khối nào dưới đây làm chân tháp?',
            'options': ['Khối cầu', 'Quả bóng nhựa', 'Viên bi', 'Khối lập phương'],
            'answer': 3,
            'solution': 'Khối lập phương có các mặt phẳng đều là hình vuông nên đặt đứng rất vững.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình ghép gồm: $3$ lon nước ngọt, $2$ quả bóng và $1$ hộp quà vuông. Số khối trụ trong '
                 'hình ghép đó là:',
            'options': ['$3$', '$1$', '$2$', '$6$'],
            'answer': 0,
            'solution': 'Chỉ có $3$ lon nước ngọt có dạng khối trụ, nên có $3$ khối trụ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 47B: Luyện tập chung về các hình khối**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Có 6 mặt phẳng**?',
            'options': ['Khối lập phương ($7$ mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ nhật)',
                        'Khối lập phương ($6$ mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ nhật)',
                        'Khối lập phương ($6$ mặt vuông); Khối hộp chữ nhật ($5$ mặt chữ nhật)',
                        'Khối lập phương ($12$ mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ nhật)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 47B: Luyện tập chung về các hình khối, **Có 6 mặt '
                        'phẳng** được xác định bởi: Khối lập phương ($6$ mặt vuông); Khối hộp chữ nhật ($6$ '
                        'mặt chữ nhật).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 47B: Luyện tập chung về các hình khối**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Có mặt cong**?',
            'options': ['Khối trụ ($3$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng)',
                        'Khối trụ ($1$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng)',
                        'Khối trụ ($2$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng)',
                        'Khối trụ ($4$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng)'],
            'answer': 2,
            'solution': 'Trong Bài 47B: Luyện tập chung về các hình khối, **Có mặt cong** có công thức/quy '
                        'tắc là: Khối trụ ($2$ đáy tròn); Khối cầu (tròn đều, không có mặt phẳng).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Điểm khác nhau cơ bản giữa khối trụ và khối hộp chữ nhật là gì?',
            'options': ['Khối trụ không lăn được',
                        'Khối hộp chữ nhật tròn đều mọi phía',
                        'Hai khối hoàn toàn giống nhau',
                        'Khối trụ có $2$ mặt đáy là hình tròn, còn khối hộp chữ nhật có các mặt là hình chữ '
                        'nhật'],
            'answer': 3,
            'solution': 'Khối trụ có $2$ mặt đáy tròn và thân cong, còn khối hộp chữ nhật có $6$ mặt phẳng '
                        'là hình chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 47B: Luyện tập chung về các hình khối**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Phân biệt được cả $4$ loại hình khối đã học ở lớp 1 và lớp 2: **khối lập phương**, '
                        '**khối hộp chữ nhật**, **khối trụ**, **khối cầu**.',
                        'Phân biệt được cả $5$ loại hình khối đã học ở lớp 1 và lớp 2: **khối lập phương**, '
                        '**khối hộp chữ nhật**, **khối trụ**, **khối cầu**.',
                        'Phân biệt được cả $4$ loại hình khối đã học ở lớp 1 và lớp 1: **khối lập phương**, '
                        '**khối hộp chữ nhật**, **khối trụ**, **khối cầu**.',
                        'Phân biệt được cả $8$ loại hình khối đã học ở lớp 1 và lớp 2: **khối lập phương**, '
                        '**khối hộp chữ nhật**, **khối trụ**, **khối cầu**.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 47B: Luyện tập chung về các hình khối: Phân biệt được '
                        'cả $4$ loại hình khối đã học ở lớp 1 và lớp 2: **khối lập phương**, **khối hộp chữ '
                        'nhật**, **khối trụ**, **khối cầu**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trong 4 hình khối đã học (khối lập phương, khối hộp chữ nhật, khối trụ, khối '
                 'cầu), chỉ có khối cầu là không có mặt phẳng nào.”',
            'answer': True,
            'solution': 'Khối lập phương, khối hộp chữ nhật có $6$ mặt phẳng; khối trụ có $2$ mặt đáy phẳng; '
                        'riêng khối cầu không có mặt phẳng nào. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 47B: Luyện tập chung về các hình khối**, quy tắc **Có 6 mặt phẳng** được xác '
                 'định bởi Khối lập phương ($6$ mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ nhật) và khi áp '
                 'dụng cho ví dụ “Một mô hình chú rô-bốt được ghép bởi: đầu là $1$ khối cầu, thân là $1$ '
                 'khối hộp chữ nhật, $2$ cánh tay và $2$ chân là $4$ khối trụ. Hỏi...” ta có lời giải: Mô '
                 'hình có $2$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 4$ khối trụ.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Có 6 mặt phẳng** (Khối lập phương ($6$ '
                        'mặt vuông); Khối hộp chữ nhật ($6$ mặt chữ nhật)) và lời giải ví dụ minh họa của '
                        'Bài 47B: Luyện tập chung về các hình khối.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 47B: Luyện tập chung về các hình khối** để giải bài '
                 'toán sau: Một mô hình chú rô-bốt được ghép bởi: đầu là $1$ khối cầu, thân là $1$ khối hộp '
                 'chữ nhật, $2$ cánh tay và $2$ chân là $4$ khối trụ. Hỏi mô hình có tất cả bao nhiêu khối '
                 'trụ? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Mô hình có $2$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 - 2 = 4$ khối '
                        'trụ.',
                        'Mô hình có $2$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 4$ khối '
                        'trụ.',
                        'Mô hình có $2$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 3$ khối '
                        'trụ.',
                        'Mô hình có $4$ cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 4$ khối '
                        'trụ.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 47B: Luyện tập chung về các hình khối: Mô hình có $2$ '
                        'cánh tay và $2$ chân đều là khối trụ, tức là có $2 + 2 = 4$ khối trụ.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đoàn tàu đồ chơi được ghép từ $1$ khối hộp chữ nhật làm thân tàu, $2$ khối lập phương '
                 'làm buồng lái, $1$ khối trụ làm ống khói và $4$ khối trụ nhỏ làm bánh xe. Hỏi đoàn tàu có '
                 'tất cả bao nhiêu khối trụ?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Số khối trụ gồm $1$ ống khói và $4$ bánh xe: $1 + 4 = 5$ (khối trụ).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd10-cac-so-trong-pham-vi-1000',
  'context_title': 'Chủ đề 10: Các số trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 10: Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; '
             'viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.',
  'title': 'Bài 48: Đơn vị, chục, trăm, nghìn',
  'icon': '🔢',
  'description': 'Nhận biết mối quan hệ giữa các hàng đơn vị, chục, trăm, nghìn và số 1000.',
  'requirements': ['Nắm vững mối quan hệ: $10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ '
                   'nghìn ($1000$).',
                   'Đếm, đọc, viết được các số tròn trăm từ $100$ đến $900$ và số $1000$.',
                   'Vận dụng kiến thức của **Bài 48: Đơn vị, chục, trăm, nghìn** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': '- **$10$ đơn vị $= 1$ chục** ($10$).\n'
                '- **$10$ chục $= 1$ trăm** ($100$).\n'
                '- **$10$ trăm $= 1$ nghìn** ($1000$).',
  'theory': '- **Các số tròn trăm:** $100$ (một trăm), $200$ (hai trăm), $300$ (ba trăm), $400$ (bốn trăm), '
            '$500$ (năm trăm), $600$ (sáu trăm), $700$ (bảy trăm), $800$ (tám trăm), $900$ (chín trăm).\n'
            '- Các số tròn trăm đều có chữ số hàng chục và chữ số hàng đơn vị bằng $0$.\n'
            '- Đếm thêm $1$ trăm vào $900$ ($9$ trăm) ta được $10$ trăm, tức là **$1$ nghìn**, viết là '
            '**$1000$** (gồm chữ số $1$ và ba chữ số $0$).',
  'formulas': [{'category': 'Quan hệ giữa Đơn vị, Chục, Trăm, Nghìn',
                'items': [{'name': 'Đổi đơn vị sang chục', 'formula': '$10$ đơn vị $= 1$ chục ($10$)'},
                          {'name': 'Đổi chục sang trăm', 'formula': '$10$ chục $= 1$ trăm ($100$)'},
                          {'name': 'Đổi trăm sang nghìn', 'formula': '$10$ trăm $= 1$ nghìn ($1000$)'}]}],
  'example': 'Điền số thích hợp vào chỗ chấm: $5$ trăm $= \\dots$; $10$ trăm $= \\dots$',
  'example_answer': 'Ta có $5$ trăm $= 500$; $10$ trăm $= 1$ nghìn $= 1000$.',
  'real_life': 'Đếm các tờ tiền mệnh giá $100$ đồng, $1000$ đồng hoặc các xấp giấy $100$ tờ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': '$10$ trăm bằng bao nhiêu?',
            'options': ['$1000$', '$100$', '$110$', '$10$'],
            'answer': 0,
            'solution': '$10$ trăm bằng $1$ nghìn, viết là $1000$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số “bảy trăm” được viết là:',
            'options': ['$70$', '$700$', '$7000$', '$7$'],
            'answer': 1,
            'solution': 'Bảy trăm là số tròn trăm có $7$ trăm, $0$ chục, $0$ đơn vị, viết là $700$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 48: Đơn vị, chục, trăm, nghìn**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Đổi đơn vị sang chục**?',
            'options': ['$11$ đơn vị $= 1$ chục ($10$)',
                        '$10$ đơn vị $= 1$ chục ($9$)',
                        '$10$ đơn vị $= 1$ chục ($10$)',
                        '$20$ đơn vị $= 1$ chục ($10$)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 48: Đơn vị, chục, trăm, nghìn, **Đổi đơn vị sang '
                        'chục** được xác định bởi: $10$ đơn vị $= 1$ chục ($10$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 48: Đơn vị, chục, trăm, nghìn**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Đổi chục sang trăm**?',
            'options': ['$11$ chục $= 1$ trăm ($100$)',
                        '$10$ chục $= 1$ trăm ($99$)',
                        '$20$ chục $= 1$ trăm ($100$)',
                        '$10$ chục $= 1$ trăm ($100$)'],
            'answer': 3,
            'solution': 'Trong Bài 48: Đơn vị, chục, trăm, nghìn, **Đổi chục sang trăm** có công thức/quy '
                        'tắc là: $10$ chục $= 1$ trăm ($100$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các số $350, 900, 105, 90$, số nào là số tròn trăm?',
            'options': ['$900$', '$350$', '$105$', '$90$'],
            'answer': 0,
            'solution': 'Số tròn trăm là số có hàng trăm từ $1$ đến $9$ và cả hàng chục, hàng đơn vị đều '
                        'bằng $0$, đó là số $900$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 48: Đơn vị, chục, trăm, nghìn**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nắm vững mối quan hệ: $11$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ '
                        'nghìn ($1000$).',
                        'Nắm vững mối quan hệ: $10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ '
                        'nghìn ($1000$).',
                        'Nắm vững mối quan hệ: $10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ '
                        'nghìn ($999$).',
                        'Nắm vững mối quan hệ: $20$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ '
                        'nghìn ($1000$).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 48: Đơn vị, chục, trăm, nghìn: Nắm vững mối quan hệ: '
                        '$10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$1$ trăm bằng $10$ chục, và $1$ nghìn bằng $10$ trăm.”',
            'answer': True,
            'solution': 'Theo quy tắc lập số: $10$ chục $= 1$ trăm, $10$ trăm $= 1$ nghìn. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 48: Đơn vị, chục, trăm, nghìn**, quy tắc **Đổi đơn vị sang chục** được xác '
                 'định bởi $10$ đơn vị $= 1$ chục ($10$) và khi áp dụng cho ví dụ “Điền số thích hợp vào chỗ '
                 'chấm: $5$ trăm $= \\dots$; $10$ trăm $= \\dots$” ta có lời giải: Ta có $5$ trăm $= 500$; '
                 '$10$ trăm $= 1$ nghìn $= 1000$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đổi đơn vị sang chục** ($10$ đơn vị $= '
                        '1$ chục ($10$)) và lời giải ví dụ minh họa của Bài 48: Đơn vị, chục, trăm, nghìn.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 48: Đơn vị, chục, trăm, nghìn** để giải bài toán '
                 'sau: Điền số thích hợp vào chỗ chấm: $5$ trăm $= \\dots$; $10$ trăm $= \\dots$ Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $6$ trăm $= 500$; $10$ trăm $= 1$ nghìn $= 1000$.',
                        'Ta có $5$ trăm $= 500$; $10$ trăm $= 1$ nghìn $= 999$.',
                        'Ta có $5$ trăm $= 500$; $10$ trăm $= 1$ nghìn $= 1000$.',
                        'Ta có $10$ trăm $= 500$; $10$ trăm $= 1$ nghìn $= 1000$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 48: Đơn vị, chục, trăm, nghìn: Ta có $5$ trăm $= 500$; '
                        '$10$ trăm $= 1$ nghìn $= 1000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mỗi hộp bánh có $100$ cái bánh. Hỏi $8$ hộp bánh như thế có tất cả bao nhiêu cái bánh?',
            'answer': ['800'],
            'unit': None,
            'solution': '$8$ hộp bánh có $8$ trăm cái bánh, tức là $800$ cái bánh.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd10-cac-so-trong-pham-vi-1000',
  'context_title': 'Chủ đề 10: Các số trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 10: Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; '
             'viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.',
  'title': 'Bài 49: Các số tròn trăm, tròn chục và so sánh',
  'icon': '💯',
  'description': 'Đếm, đọc, viết và so sánh các số tròn trăm, tròn chục có ba chữ số.',
  'requirements': ['Đếm, đọc, viết được các số tròn chục trong phạm vi $1000$ (như $110, 120, \\dots, 990$).',
                   'So sánh được các số tròn trăm và các số tròn chục có ba chữ số.',
                   'Vận dụng kiến thức của **Bài 49: Các số tròn trăm, tròn chục và so sánh** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Số tròn trăm** có dạng $\\overline{a00}$ (cả hàng chục và hàng đơn vị đều là $0$).\n'
                '- **Số tròn chục** có ba chữ số có dạng $\\overline{ab0}$ (chữ số hàng đơn vị là $0$), ví '
                'dụ: $230, 450, 990$.',
  'theory': '- **Đếm thêm $10$ (một chục):** $100, 110, 120, 130, \\dots, 190, 200$.\n'
            '- **Cách đọc số tròn chục có ba chữ số:** $520$ đọc là năm trăm hai mươi.\n'
            '- **So sánh các số tròn trăm, tròn chục:**\n'
            '  + So sánh chữ số hàng trăm trước: $300 < 500$ vì $3 < 5$.\n'
            '  + Nếu hàng trăm bằng nhau thì so sánh chữ số hàng chục: $460 > 430$ vì cùng $4$ trăm và $6 > '
            '3$.',
  'formulas': [{'category': 'Quy tắc đọc và so sánh số tròn trăm, tròn chục',
                'items': [{'name': 'Số tròn chục 3 chữ số',
                           'formula': 'Chữ số hàng đơn vị bằng $0$ ($\\overline{ab0}$)',
                           'note': 'Ví dụ: $520$ gồm $5$ trăm và $2$ chục.'},
                          {'name': 'So sánh',
                           'formula': 'So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì so sánh hàng '
                                      'chục',
                           'note': 'Ví dụ: $460 > 430$.'}]}],
  'example': 'a) Điền số tiếp theo vào dãy số tròn chục: $370, 380, 390, \\dots$\nb) So sánh $620$ và $590$.',
  'example_answer': 'a) Thêm $1$ chục vào $390$ được $400$.\nb) So sánh hàng trăm: $6 > 5$ nên $620 > 590$.',
  'real_life': 'Đếm tiền hoặc đếm số lượng sản phẩm đóng theo túi $10$ cái.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số $520$ được đọc là:',
            'options': ['Năm trăm linh hai', 'Năm trăm hai mươi', 'Năm mươi hai', 'Hai trăm năm mươi'],
            'answer': 1,
            'solution': 'Số $520$ gồm $5$ trăm và $2$ chục nên đọc là năm trăm hai mươi.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $460 \\dots 430$ là:',
            'options': ['$<$', '$=$', '$>$', '$+$'],
            'answer': 2,
            'solution': 'Hai số có cùng $4$ trăm, so sánh hàng chục có $6 > 3$ nên $460 > 430$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 49: Các số tròn trăm, tròn chục và so sánh**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Số tròn chục 3 chữ số**?',
            'options': ['Chữ số hàng đơn vị bằng $1$ ($\\overline{ab0}$)',
                        'Chữ số hàng đơn vị bằng $2$ ($\\overline{ab0}$)',
                        'So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì so sánh hàng chục',
                        'Chữ số hàng đơn vị bằng $0$ ($\\overline{ab0}$)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 49: Các số tròn trăm, tròn chục và so sánh, **Số '
                        'tròn chục 3 chữ số** được xác định bởi: Chữ số hàng đơn vị bằng $0$ '
                        '($\\overline{ab0}$). (Ví dụ: $520$ gồm $5$ trăm và $2$ chục.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 49: Các số tròn trăm, tròn chục và so sánh**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **So sánh**?',
            'options': ['So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì so sánh hàng chục',
                        'So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì so sánh hàng chục (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì '
                        'so sánh hàng chục',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của So sánh hàng trăm trước '
                        '$\\rightarrow$ nếu bằng nhau thì so sánh hàng chục'],
            'answer': 0,
            'solution': 'Trong Bài 49: Các số tròn trăm, tròn chục và so sánh, **So sánh** có công thức/quy '
                        'tắc là: So sánh hàng trăm trước $\\rightarrow$ nếu bằng nhau thì so sánh hàng '
                        'chục.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong dãy số tròn chục cách đều: $280, 290, ?, 310$, số thích hợp điền vào dấu $?$ là:',
            'options': ['$291$', '$300$', '$200$', '$320$'],
            'answer': 1,
            'solution': 'Mỗi số tăng thêm $10$ đơn vị ($1$ chục): $290$ thêm $10$ là $300$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 49: Các số tròn trăm, tròn chục và so sánh**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Đếm, đọc, viết được các số tròn chục trong phạm vi $1010$ (như $110, 120, \\dots, '
                        '990$).',
                        'Đếm, đọc, viết được các số tròn chục trong phạm vi $1000$ (như $110, 120, \\dots, '
                        '989$).',
                        'Đếm, đọc, viết được các số tròn chục trong phạm vi $1000$ (như $110, 120, \\dots, '
                        '990$).',
                        'Đếm, đọc, viết được các số tròn chục trong phạm vi $1002$ (như $110, 120, \\dots, '
                        '990$).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 49: Các số tròn trăm, tròn chục và so sánh: Đếm, đọc, '
                        'viết được các số tròn chục trong phạm vi $1000$ (như $110, 120, \\dots, 990$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Mọi số tròn trăm (như $200, 500$) cũng đồng thời có chữ số hàng đơn vị bằng '
                 '$0$.”',
            'answer': True,
            'solution': 'Số tròn trăm có cả chữ số hàng chục và hàng đơn vị đều bằng $0$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 49: Các số tròn trăm, tròn chục và so sánh**, quy tắc **Số tròn chục 3 chữ '
                 'số** được xác định bởi Chữ số hàng đơn vị bằng $0$ ($\\overline{ab0}$) và khi áp dụng cho '
                 'ví dụ “a) Điền số tiếp theo vào dãy số tròn chục: $370, 380, 390, \\dots$ b) So sánh $620$ '
                 'và $590$.” ta có lời giải: a) Thêm $1$ chục vào $390$ được $400$. b) So sánh hàng trăm: $6 '
                 '> 5$ nên $620 > 590$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số tròn chục 3 chữ số** (Chữ số hàng đơn '
                        'vị bằng $0$ ($\\overline{ab0}$)) và lời giải ví dụ minh họa của Bài 49: Các số tròn '
                        'trăm, tròn chục và so sánh.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 49: Các số tròn trăm, tròn chục và so sánh** để '
                 'giải bài toán sau: a) Điền số tiếp theo vào dãy số tròn chục: $370, 380, 390, \\dots$\n'
                 'b) So sánh $620$ và $590$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) Thêm $1$ chục vào $390$ được $400$. b) So sánh hàng trăm: $6 < 5$ nên $620 > '
                        '590$.',
                        'a) Thêm $1$ chục vào $390$ được $400$. b) So sánh hàng trăm: $6 > 5$ nên $620 > '
                        '589$.',
                        'a) Thêm $2$ chục vào $390$ được $400$. b) So sánh hàng trăm: $6 > 5$ nên $620 > '
                        '590$.',
                        'a) Thêm $1$ chục vào $390$ được $400$. b) So sánh hàng trăm: $6 > 5$ nên $620 > '
                        '590$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 49: Các số tròn trăm, tròn chục và so sánh: a) Thêm $1$ '
                        'chục vào $390$ được $400$.\n'
                        'b) So sánh hàng trăm: $6 > 5$ nên $620 > 590$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số tròn chục lớn nhất có ba chữ số là số nào?',
            'answer': ['990'],
            'unit': None,
            'solution': 'Số có ba chữ số lớn nhất mà chữ số hàng đơn vị bằng $0$ là số $990$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd10-cac-so-trong-pham-vi-1000',
  'context_title': 'Chủ đề 10: Các số trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 10: Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; '
             'viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.',
  'title': 'Bài 51: Số có ba chữ số',
  'icon': '🔢',
  'description': 'Đọc, viết các số có ba chữ số và phân tích cấu tạo hàng trăm, hàng chục, hàng đơn vị.',
  'requirements': ['Nhận biết số có ba chữ số gồm ba hàng: **hàng trăm, hàng chục, hàng đơn vị** (từ trái '
                   'sang phải).',
                   'Đọc và viết đúng mọi số có ba chữ số (từ $100$ đến $999$), chú ý các trường hợp có chữ '
                   'số $0, 1, 4, 5$.',
                   'Vận dụng kiến thức của **Bài 51: Số có ba chữ số** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': '**Số có ba chữ số** $\\overline{abc}$ (với $a \\neq 0$) gồm chữ số **hàng trăm** $a$, chữ '
                'số **hàng chục** $b$ và chữ số **hàng đơn vị** $c$ (viết lần lượt từ trái sang phải).',
  'theory': '- **Quy tắc đọc các trường hợp đặc biệt:**\n'
            '  + Khi chữ số hàng chục là $0$ và hàng đơn vị khác $0$, ta đọc chữ số $0$ ở hàng chục là '
            '**“linh”** (hoặc “lẻ”): $205$ đọc là *hai trăm linh năm*; $705$ đọc là *bảy trăm linh năm*.\n'
            '  + Khi hàng chục từ $2$ trở lên và hàng đơn vị là $1$, đọc là **“mốt”**: $251$ đọc là *hai '
            'trăm năm mươi mốt*.\n'
            '  + Khi hàng chục từ $1$ trở lên và hàng đơn vị là $5$, đọc là **“lăm”**: $625$ đọc là *sáu '
            'trăm hai mươi lăm*; $915$ đọc là *chín trăm mười lăm*.',
  'formulas': [{'category': 'Cấu tạo và cách đọc số có ba chữ số',
                'items': [{'name': 'Thứ tự các hàng',
                           'formula': 'Hàng trăm (trái) $\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng '
                                      'đơn vị (phải)'},
                          {'name': 'Hàng chục bằng 0',
                           'formula': '$\\overline{a0c}$ đọc là “$a$ trăm linh $c$”',
                           'note': 'Ví dụ: $608$ đọc là sáu trăm linh tám.'},
                          {'name': 'Số liền trước – liền sau',
                           'formula': 'Liền sau của $399$ là $400$; liền sau của $999$ là $1000$'}]}],
  'example': 'Viết số gồm $6$ trăm, $0$ chục và $8$ đơn vị, rồi nêu cách đọc số đó.',
  'example_answer': 'Số gồm $6$ trăm, $0$ chục và $8$ đơn vị viết là **$608$**, đọc là **sáu trăm linh '
                    'tám**.',
  'real_life': 'Đọc số phòng học, số phòng khách sạn (phòng $305$), biển số nhà, số trang sách dày.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số gồm $6$ trăm, $0$ chục và $8$ đơn vị được viết là:',
            'options': ['$68$', '$680$', '$608$', '$806$'],
            'answer': 2,
            'solution': 'Hàng trăm là $6$, hàng chục là $0$, hàng đơn vị là $8$, viết là $608$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số “bảy trăm linh năm” được viết là:',
            'options': ['$75$', '$750$', '$7005$', '$705$'],
            'answer': 3,
            'solution': 'Bảy trăm là $7$ ở hàng trăm, linh là $0$ ở hàng chục, năm là $5$ ở hàng đơn vị '
                        '$\\rightarrow 705$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 51: Số có ba chữ số**, quy tắc hoặc công thức nào sau đây xác định đúng **Thứ '
                 'tự các hàng**?',
            'options': ['Hàng trăm (trái) $\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng đơn vị (phải)',
                        'Hàng trăm (trái) $\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng đơn vị (phải) '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hàng trăm (trái) $\\rightarrow$ Hàng chục (giữa) '
                        '$\\rightarrow$ Hàng đơn vị (phải)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hàng trăm (trái) $\\rightarrow$ '
                        'Hàng chục (giữa) $\\rightarrow$ Hàng đơn vị (phải)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 51: Số có ba chữ số, **Thứ tự các hàng** được xác '
                        'định bởi: Hàng trăm (trái) $\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng đơn '
                        'vị (phải).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 51: Số có ba chữ số**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Hàng chục bằng 0**?',
            'options': ['$\\overline{a0c}$ đọc là “$a$ trăm linh $c$” (với dấu ngược lại)',
                        '$\\overline{a0c}$ đọc là “$a$ trăm linh $c$”',
                        'Đảo ngược vế của quy tắc: $\\overline{a0c}$ đọc là “$a$ trăm linh $c$”',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{a0c}$ đọc là “$a$ '
                        'trăm linh $c$”'],
            'answer': 1,
            'solution': 'Trong Bài 51: Số có ba chữ số, **Hàng chục bằng 0** có công thức/quy tắc là: '
                        '$\\overline{a0c}$ đọc là “$a$ trăm linh $c$”.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số liền sau của số $399$ là số nào?',
            'options': ['$398$', '$390$', '$400$', '$300$'],
            'answer': 2,
            'solution': 'Số liền sau của $399$ lớn hơn $399$ là $1$ đơn vị: $399 + 1 = 400$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 51: Số có ba chữ số**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết số có ba chữ số gồm ba hàng: **hàng trăm, hàng chục, hàng đơn vị** (từ '
                        'phải sang trái).',
                        'Đảo ngược vế của quy tắc: Nhận biết số có ba chữ số gồm ba hàng: **hàng trăm, hàng '
                        'chục, hàng đơn vị** (từ trái sang phải).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết số có ba chữ số gồm '
                        'ba hàng: **hàng trăm, hàng chục, hàng đơn vị** (từ trái sang phải).',
                        'Nhận biết số có ba chữ số gồm ba hàng: **hàng trăm, hàng chục, hàng đơn vị** (từ '
                        'trái sang phải).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 51: Số có ba chữ số: Nhận biết số có ba chữ số gồm ba '
                        'hàng: **hàng trăm, hàng chục, hàng đơn vị** (từ trái sang phải).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $915$ đọc là chín trăm mười lăm.”',
            'answer': True,
            'solution': 'Số $915$ gồm $9$ trăm, $1$ chục, $5$ đơn vị nên đọc là chín trăm mười lăm. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 51: Số có ba chữ số**, quy tắc **Thứ tự các hàng** được xác định bởi Hàng trăm '
                 '(trái) $\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng đơn vị (phải) và khi áp dụng '
                 'cho ví dụ “Viết số gồm $6$ trăm, $0$ chục và $8$ đơn vị, rồi nêu cách đọc số đó.” ta có '
                 'lời giải: Số gồm $6$ trăm, $0$ chục và $8$ đơn vị viết là **$608$**, đọc là **sáu trăm '
                 'linh tám**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thứ tự các hàng** (Hàng trăm (trái) '
                        '$\\rightarrow$ Hàng chục (giữa) $\\rightarrow$ Hàng đơn vị (phải)) và lời giải ví '
                        'dụ minh họa của Bài 51: Số có ba chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 51: Số có ba chữ số** để giải bài toán sau: Viết số '
                 'gồm $6$ trăm, $0$ chục và $8$ đơn vị, rồi nêu cách đọc số đó. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Số gồm $6$ trăm, $0$ chục và $8$ đơn vị viết là **$608$**, đọc là **sáu trăm linh '
                        'tám**.',
                        'Số gồm $7$ trăm, $0$ chục và $8$ đơn vị viết là **$608$**, đọc là **sáu trăm linh '
                        'tám**.',
                        'Số gồm $6$ trăm, $0$ chục và $8$ đơn vị viết là **$607$**, đọc là **sáu trăm linh '
                        'tám**.',
                        'Số gồm $12$ trăm, $0$ chục và $8$ đơn vị viết là **$608$**, đọc là **sáu trăm linh '
                        'tám**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 51: Số có ba chữ số: Số gồm $6$ trăm, $0$ chục và $8$ '
                        'đơn vị viết là **$608$**, đọc là **sáu trăm linh tám**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số bé nhất có ba chữ số khác nhau là số nào?',
            'answer': ['102'],
            'unit': None,
            'solution': 'Để số có ba chữ số là bé nhất và các chữ số khác nhau: hàng trăm nhỏ nhất khác $0$ '
                        'là $1$, hàng chục nhỏ nhất là $0$, hàng đơn vị nhỏ nhất khác $1$ và $0$ là $2$. Vậy '
                        'số đó là $102$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd10-cac-so-trong-pham-vi-1000',
  'context_title': 'Chủ đề 10: Các số trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 10: Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; '
             'viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.',
  'title': 'Bài 52: Viết số thành tổng các trăm, chục, đơn vị',
  'icon': '🧩',
  'description': 'Phân tích số có ba chữ số thành tổng các trăm, chục, đơn vị và ngược lại.',
  'requirements': ['Viết được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $836 = 800 '
                   '+ 30 + 6$).',
                   'Viết được số có ba chữ số khi biết tổng các trăm, chục, đơn vị.',
                   'Vận dụng kiến thức của **Bài 52: Viết số thành tổng các trăm, chục, đơn vị** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Mỗi số có ba chữ số $\\overline{abc}$ đều viết được thành **tổng của các trăm, chục và đơn '
                'vị**:\n'
                '$\\overline{abc} = a00 + b0 + c$.',
  'theory': '- **Trường hợp cả ba chữ số đều khác $0$:**\n'
            '  $375$ gồm $3$ trăm, $7$ chục, $5$ đơn vị $\\rightarrow 375 = 300 + 70 + 5$.\n'
            '- **Trường hợp có chữ số $0$ ở hàng chục hoặc hàng đơn vị:** Ta lược bỏ số hạng bằng $0$ trong '
            'tổng:\n'
            '  + $507$ gồm $5$ trăm, $0$ chục, $7$ đơn vị $\\rightarrow 507 = 500 + 7$.\n'
            '  + $640$ gồm $6$ trăm, $4$ chục, $0$ đơn vị $\\rightarrow 640 = 600 + 40$.',
  'formulas': [{'category': 'Biểu diễn số thành tổng các trăm, chục, đơn vị',
                'items': [{'name': 'Dạng tổng quát',
                           'formula': '$\\overline{abc} = a00 + b0 + c$',
                           'note': 'Ví dụ: $836 = 800 + 30 + 6$.'},
                          {'name': 'Khi hàng chục bằng 0',
                           'formula': '$\\overline{a0c} = a00 + c$',
                           'note': 'Ví dụ: $507 = 500 + 7$.'},
                          {'name': 'Khi hàng đơn vị bằng 0',
                           'formula': '$\\overline{ab0} = a00 + b0$',
                           'note': 'Ví dụ: $640 = 600 + 40$.'}]}],
  'example': 'a) Viết số $846$ và số $507$ thành tổng các trăm, chục, đơn vị.\nb) Tính tổng $400 + 50 + 9$.',
  'example_answer': 'a) $846 = 800 + 40 + 6$; $507 = 500 + 7$.\nb) $400 + 50 + 9 = 459$.',
  'real_life': 'Đếm tổng số tiền khi có các tờ $100$ đồng, $10$ đồng và $1$ đồng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số $836$ được viết thành tổng các trăm, chục, đơn vị là:',
            'options': ['$8 + 3 + 6$', '$800 + 36 + 6$', '$80 + 30 + 6$', '$800 + 30 + 6$'],
            'answer': 3,
            'solution': 'Số $836$ gồm $8$ trăm ($800$), $3$ chục ($30$) và $6$ đơn vị nên $836 = 800 + 30 + '
                        '6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng $300 + 8$ bằng số nào dưới đây?',
            'options': ['$308$', '$38$', '$380$', '$803$'],
            'answer': 0,
            'solution': 'Tổng gồm $3$ trăm ($300$), $0$ chục và $8$ đơn vị nên bằng $308$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 52: Viết số thành tổng các trăm, chục, đơn vị**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Dạng tổng quát**?',
            'options': ['$\\overline{abc} = a00 - b0 + c$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Đảo ngược vế của quy tắc: $\\overline{abc} = a00 + b0 + c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{abc} = a00 + b0 + '
                        'c$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 52: Viết số thành tổng các trăm, chục, đơn vị, '
                        '**Dạng tổng quát** được xác định bởi: $\\overline{abc} = a00 + b0 + c$. (Ví dụ: '
                        '$836 = 800 + 30 + 6$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 52: Viết số thành tổng các trăm, chục, đơn vị**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Khi hàng chục bằng 0**?',
            'options': ['$\\overline{a0c} = a00 - c$',
                        'Đảo ngược vế của quy tắc: $\\overline{a0c} = a00 + c$',
                        '$\\overline{a0c} = a00 + c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{a0c} = a00 + c$'],
            'answer': 2,
            'solution': 'Trong Bài 52: Viết số thành tổng các trăm, chục, đơn vị, **Khi hàng chục bằng 0** '
                        'có công thức/quy tắc là: $\\overline{a0c} = a00 + c$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong số $749$, giá trị của chữ số $4$ là bao nhiêu?',
            'options': ['$4$', '$400$', '$74$', '$40$'],
            'answer': 3,
            'solution': 'Chữ số $4$ trong số $749$ đứng ở hàng chục nên có giá trị là $4$ chục hay $40$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 52: Viết số thành tổng các trăm, chục, đơn vị**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Viết được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $836 '
                        '= 800 + 30 + 6$).',
                        'Viết được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $836 '
                        '= 800 - 30 + 6$).',
                        'Viết được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $836 '
                        '= 800 + 30 + 5$).',
                        'Viết được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $838 '
                        '= 800 + 30 + 6$).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 52: Viết số thành tổng các trăm, chục, đơn vị: Viết '
                        'được số có ba chữ số thành tổng của số trăm, số chục và số đơn vị (ví dụ $836 = 800 '
                        '+ 30 + 6$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$507 = 500 + 70$.”',
            'answer': False,
            'solution': 'Số $507$ gồm $5$ trăm và $7$ đơn vị nên $507 = 500 + 7$ (còn $500 + 70 = 570$). '
                        'Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 52: Viết số thành tổng các trăm, chục, đơn vị**, quy tắc **Dạng tổng quát** '
                 'được xác định bởi $\\overline{abc} = a00 + b0 + c$ và khi áp dụng cho ví dụ “a) Viết số '
                 '$846$ và số $507$ thành tổng các trăm, chục, đơn vị. b) Tính tổng $400 + 50 + 9$.” ta có '
                 'lời giải: a) $846 = 800 + 40 + 6$; $507 = 500 + 7$. b) $400 + 50 + 9 = 459$.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Dạng tổng quát** ($\\overline{abc} = a00 '
                        '+ b0 + c$) và lời giải ví dụ minh họa của Bài 52: Viết số thành tổng các trăm, '
                        'chục, đơn vị.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 52: Viết số thành tổng các trăm, chục, đơn vị** để '
                 'giải bài toán sau: a) Viết số $846$ và số $507$ thành tổng các trăm, chục, đơn vị.\n'
                 'b) Tính tổng $400 + 50 + 9$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $846 = 800 - 40 + 6$; $507 = 500 + 7$. b) $400 + 50 + 9 = 459$.',
                        'a) $846 = 800 + 40 + 6$; $507 = 500 + 7$. b) $400 + 50 + 9 = 459$.',
                        'a) $846 = 800 + 40 + 6$; $507 = 500 + 7$. b) $400 + 50 + 9 = 458$.',
                        'a) $848 = 800 + 40 + 6$; $507 = 500 + 7$. b) $400 + 50 + 9 = 459$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 52: Viết số thành tổng các trăm, chục, đơn vị: a) $846 = '
                        '800 + 40 + 6$; $507 = 500 + 7$.\n'
                        'b) $400 + 50 + 9 = 459$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số thích hợp điền vào chỗ chấm: $629 = 600 + \\dots + 9$.',
            'answer': ['20'],
            'unit': None,
            'solution': 'Số $629$ gồm $6$ trăm ($600$), $2$ chục ($20$) và $9$ đơn vị nên số cần điền là '
                        '$20$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd10-cac-so-trong-pham-vi-1000',
  'context_title': 'Chủ đề 10: Các số trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 10: Đơn vị, chục, trăm, nghìn; số tròn trăm, tròn chục; số có ba chữ số; '
             'viết số thành tổng các trăm, chục, đơn vị; so sánh các số có ba chữ số.',
  'title': 'Bài 53: So sánh các số có ba chữ số',
  'icon': '⚖️',
  'description': 'Quy tắc so sánh hai số có ba chữ số theo thứ tự hàng trăm, hàng chục, hàng đơn vị.',
  'requirements': ['So sánh thành thạo hai số có ba chữ số theo thứ tự: **Hàng trăm $\\rightarrow$ Hàng chục '
                   '$\\rightarrow$ Hàng đơn vị**.',
                   'Sắp xếp được nhóm không quá $4$ số trong phạm vi $1000$ theo thứ tự từ bé đến lớn hoặc '
                   'từ lớn đến bé.',
                   'Lập được số lớn nhất, số bé nhất có ba chữ số từ các thẻ số cho trước.'],
  'definition': '**Quy tắc so sánh hai số có ba chữ số:**\n'
                '1. So sánh chữ số **hàng trăm** trước: số nào có hàng trăm lớn hơn thì lớn hơn.\n'
                '2. Nếu hàng trăm bằng nhau, so sánh chữ số **hàng chục**.\n'
                '3. Nếu hàng trăm và hàng chục đều bằng nhau, so sánh chữ số **hàng đơn vị**.',
  'theory': '- **Ví dụ 1:** $582 < 610$ (vì ở hàng trăm $5 < 6$).\n'
            '- **Ví dụ 2:** $582 < 591$ (vì cùng $5$ trăm, ở hàng chục $8 < 9$).\n'
            '- **Ví dụ 3:** $582 > 580$ (vì cùng $5$ trăm và $8$ chục, ở hàng đơn vị $2 > 0$).\n'
            '- Mọi số có ba chữ số luôn lớn hơn các số có một hoặc hai chữ số, và bé hơn $1000$.',
  'formulas': [{'category': 'Quy tắc so sánh và lập số có ba chữ số',
                'items': [{'name': 'Thứ tự so sánh',
                           'formula': 'Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị'},
                          {'name': 'Lập số lớn nhất',
                           'formula': 'Chọn chữ số lớn nhất đặt ở hàng trăm, rồi giảm dần sang phải',
                           'note': 'Ví dụ: Từ $3, 0, 7$ lập được số lớn nhất là $730$.'}]}],
  'example': 'Sắp xếp các số $457, 475, 447, 574$ theo thứ tự từ bé đến lớn.',
  'example_answer': 'Số $574$ có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng chục: '
                    '$4 < 5 < 7$ nên $447 < 457 < 475$.\n'
                    'Vậy thứ tự từ bé đến lớn là: **$447, 457, 475, 574$**.',
  'real_life': 'So sánh giá sản phẩm, quãng đường giữa các thành phố, điểm thi đua của các trường.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số $519, 591, 195, 559$, số lớn nhất là:',
            'options': ['$591$', '$519$', '$195$', '$559$'],
            'answer': 0,
            'solution': 'Ba số có $5$ trăm là $519, 591, 559$. So sánh hàng chục: $9 > 5 > 1$ nên $591$ là '
                        'số lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $607 \\dots 670$ là:',
            'options': ['$>$', '$<$', '$=$', 'Không so sánh được'],
            'answer': 1,
            'solution': 'Hai số cùng có $6$ trăm; ở hàng chục $0 < 7$ nên $607 < 670$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 53: So sánh các số có ba chữ số**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Thứ tự so sánh**?',
            'options': ['Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng '
                        'đơn vị',
                        'Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hàng trăm $\\rightarrow$ Hàng '
                        'chục $\\rightarrow$ Hàng đơn vị'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 53: So sánh các số có ba chữ số, **Thứ tự so '
                        'sánh** được xác định bởi: Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng '
                        'đơn vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 53: So sánh các số có ba chữ số**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Lập số lớn nhất**?',
            'options': ['Chọn chữ số lớn nhất đặt ở hàng trăm, rồi giảm dần sang phải (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Chọn chữ số lớn nhất đặt ở hàng trăm, rồi giảm dần sang '
                        'phải',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chọn chữ số lớn nhất đặt ở hàng '
                        'trăm, rồi giảm dần sang phải',
                        'Chọn chữ số lớn nhất đặt ở hàng trăm, rồi giảm dần sang phải'],
            'answer': 3,
            'solution': 'Trong Bài 53: So sánh các số có ba chữ số, **Lập số lớn nhất** có công thức/quy tắc '
                        'là: Chọn chữ số lớn nhất đặt ở hàng trăm, rồi giảm dần sang phải.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Từ ba thẻ số $3, 0, 7$, số có ba chữ số lớn nhất lập được (mỗi thẻ dùng một lần) là:',
            'options': ['$730$', '$703$', '$370$', '$037$'],
            'answer': 0,
            'solution': 'Để được số lớn nhất, chọn chữ số lớn nhất ($7$) ở hàng trăm, tiếp theo là $3$ ở '
                        'hàng chục và $0$ ở hàng đơn vị $\\rightarrow 730$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 53: So sánh các số có ba chữ số**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['So sánh thành thạo hai số có ba chữ số theo thứ tự: **Hàng trăm $\\rightarrow$ Hàng '
                        'chục $\\rightarrow$ Hàng đơn vị**. (với dấu ngược lại)',
                        'So sánh thành thạo hai số có ba chữ số theo thứ tự: **Hàng trăm $\\rightarrow$ Hàng '
                        'chục $\\rightarrow$ Hàng đơn vị**.',
                        'Đảo ngược vế của quy tắc: So sánh thành thạo hai số có ba chữ số theo thứ tự: '
                        '**Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của So sánh thành thạo hai số có ba '
                        'chữ số theo thứ tự: **Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn '
                        'vị**.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 53: So sánh các số có ba chữ số: So sánh thành thạo '
                        'hai số có ba chữ số theo thứ tự: **Hàng trăm $\\rightarrow$ Hàng chục '
                        '$\\rightarrow$ Hàng đơn vị**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$478 > 487$.”',
            'answer': False,
            'solution': 'Hai số có cùng $4$ trăm, nhưng ở hàng chục $7 < 8$ nên $478 < 487$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 53: So sánh các số có ba chữ số**, quy tắc **Thứ tự so sánh** được xác định '
                 'bởi Hàng trăm $\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị và khi áp dụng cho ví dụ '
                 '“Sắp xếp các số $457, 475, 447, 574$ theo thứ tự từ bé đến lớn.” ta có lời giải: Số $574$ '
                 'có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng chục: $4 < 5 < 7$ '
                 'nên $447 < 457 < 475$. Vậy thứ tự từ.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thứ tự so sánh** (Hàng trăm '
                        '$\\rightarrow$ Hàng chục $\\rightarrow$ Hàng đơn vị) và lời giải ví dụ minh họa của '
                        'Bài 53: So sánh các số có ba chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 53: So sánh các số có ba chữ số** để giải bài toán '
                 'sau: Sắp xếp các số $457, 475, 447, 574$ theo thứ tự từ bé đến lớn. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Số $574$ có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng '
                        'chục: $4 > 5 < 7$ nên $447 < 457 < 475$. Vậy thứ tự từ bé đến lớn là...',
                        'Số $574$ có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng '
                        'chục: $4 < 5 < 7$ nên $447 < 457 < 474$. Vậy thứ tự từ bé đến lớn là...',
                        'Số $574$ có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng '
                        'chục: $4 < 5 < 7$ nên $447 < 457 < 475$. Vậy thứ tự từ bé đến lớn là...',
                        'Số $576$ có $5$ trăm nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng '
                        'chục: $4 < 5 < 7$ nên $447 < 457 < 475$. Vậy thứ tự từ bé đến lớn là...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 53: So sánh các số có ba chữ số: Số $574$ có $5$ trăm '
                        'nên lớn nhất. Ba số còn lại cùng có $4$ trăm, so sánh hàng chục: $4 < 5 < 7$ nên '
                        '$447 < 457 < 475$.\n'
                        'Vậy thứ tự từ bé đến lớn là: **$447, 457, 475, 574$**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Từ ba chữ số $4, 0, 8$ (mỗi chữ số dùng đúng một lần), em lập được số có ba chữ số bé nhất '
                 'là số nào?',
            'answer': ['408'],
            'unit': None,
            'solution': 'Chữ số hàng trăm phải khác $0$ và bé nhất nên chọn $4$, chữ số hàng chục bé nhất là '
                        '$0$, hàng đơn vị là $8$. Vậy số bé nhất lập được là $408$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd11-do-dai-va-tien-viet-nam',
  'context_title': 'Chủ đề 11: Độ dài và đơn vị đo độ dài. Tiền Việt Nam',
  'context': 'SGK Toán 2 · Chủ đề 11: Đề-xi-mét, mét, ki-lô-mét; giới thiệu tiền Việt Nam; thực hành trải '
             'nghiệm đo độ dài.',
  'title': 'Bài 55: Đề-xi-mét. Mét. Ki-lô-mét',
  'icon': '📏',
  'description': 'Nhận biết các đơn vị đo độ dài đề-xi-mét (dm), mét (m), ki-lô-mét (km) và mối quan hệ giữa '
                 'chúng.',
  'requirements': ['Nhận biết tên gọi, ký hiệu các đơn vị đo độ dài: **đề-xi-mét ($\\text{dm}$)**, **mét ($\\text{m}$)**, **ki-lô-mét ($\\text{km}$)**.',
                   'Thuộc và vận dụng mối quan hệ: $1\\text{ dm} = 10\\text{ cm}$; $1\\text{ m} = 10\\text{ '
                   'dm} = 100\\text{ cm}$; $1\\text{ km} = 1000\\text{ m}$.',
                   'Thực hiện được các phép tính cộng, trừ, nhân, chia với số đo độ dài.'],
  'definition': 'Các đơn vị đo độ dài thông dụng:\n'
                '- **Đề-xi-mét** (viết tắt là $\\text{dm}$): $1\\text{ dm} = 10\\text{ cm}$.\n'
                '- **Mét** (viết tắt là $\\text{m}$): $1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$.\n'
                '- **Ki-lô-mét** (viết tắt là $\\text{km}$): $1\\text{ km} = 1000\\text{ m}$.',
  'theory': '- **Khi nào dùng từng đơn vị?**\n'
            '  + Dùng $\\text{cm}, \\text{dm}$ để đo các đồ vật nhỏ (bút chì, hộp bút, quyển vở, gang tay).\n'
            '  + Dùng $\\text{m}$ để đo chiều dài lớp học, chiều cao cái cây, ngôi nhà, tấm vải.\n'
            '  + Dùng $\\text{km}$ để đo những quãng đường dài (quãng đường giữa hai tỉnh, hai thành phố, '
            'chiều dài con sông).\n'
            '- **Lưu ý khi tính toán:** Nếu hai số đo khác đơn vị (như $1\\text{ m} - 35\\text{ cm}$), phải '
            '**đổi về cùng một đơn vị** ($100\\text{ cm} - 35\\text{ cm} = 65\\text{ cm}$) rồi mới tính.',
  'formulas': [{'category': 'Bảng quy đổi đơn vị đo độ dài',
                'items': [{'name': 'Đề-xi-mét và Xăng-ti-mét',
                           'formula': '$1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$'},
                          {'name': 'Mét với Đề-xi-mét, Xăng-ti-mét',
                           'formula': '$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$'},
                          {'name': 'Ki-lô-mét và Mét',
                           'formula': '$1\\text{ km} = 1000\\text{ m}$; $1000\\text{ m} = 1\\text{ km}$'}]}],
  'example': 'Đổi các đơn vị sau: a) $3\\text{ dm} = \\dots\\text{ cm}$; b) $2\\text{ m} = \\dots\\text{ '
             'dm}$; c) $1\\text{ km} = \\dots\\text{ m}$.',
  'example_answer': 'a) $3\\text{ dm} = 30\\text{ cm}$.\n'
                    'b) $2\\text{ m} = 20\\text{ dm}$.\n'
                    'c) $1\\text{ km} = 1000\\text{ m}$.',
  'real_life': 'Đọc cột mốc giao thông trên quốc lộ (ví dụ “Hà Nội $35\\text{ km}$”), đo chiều cao cơ thể '
               '($125\\text{ cm}$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Điền số thích hợp vào chỗ chấm: $1\\text{ dm} = \\dots\\text{ cm}$',
            'options': ['$1$', '$10$', '$100$', '$1000$'],
            'answer': 1,
            'solution': 'Ta có $1\\text{ dm} = 10\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị thích hợp nhất để đo quãng đường từ Hà Nội đến Hải Phòng là:',
            'options': ['$\\text{cm}$', '$\\text{dm}$', '$\\text{km}$', '$\\text{m}$'],
            'answer': 2,
            'solution': 'Quãng đường giữa hai thành phố rất dài nên dùng đơn vị ki-lô-mét ($\\text{km}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 55: Đề-xi-mét. Mét. Ki-lô-mét**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Đề-xi-mét và Xăng-ti-mét**?',
            'options': ['$2\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$',
                        '$1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 2\\text{ dm}$',
                        '$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$',
                        '$1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 55: Đề-xi-mét. Mét. Ki-lô-mét, **Đề-xi-mét và '
                        'Xăng-ti-mét** được xác định bởi: $1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = '
                        '1\\text{ dm}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 55: Đề-xi-mét. Mét. Ki-lô-mét**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Mét với Đề-xi-mét, Xăng-ti-mét**?',
            'options': ['$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$',
                        '$2\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$',
                        '$1\\text{ m} = 10\\text{ dm} = 99\\text{ cm}$',
                        '$1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$'],
            'answer': 0,
            'solution': 'Trong Bài 55: Đề-xi-mét. Mét. Ki-lô-mét, **Mét với Đề-xi-mét, Xăng-ti-mét** có công '
                        'thức/quy tắc là: $1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Điền số thích hợp vào chỗ chấm: $1\\text{ m} = \\dots\\text{ cm}$',
            'options': ['$10$', '$100$', '$1000$', '$50$'],
            'answer': 1,
            'solution': 'Ta có $1\\text{ m} = 10\\text{ dm} = 100\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 55: Đề-xi-mét. Mét. Ki-lô-mét**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết tên gọi, ký hiệu các đơn vị đo độ dài: **đề-xi-mét ($\\text{dm}$)**, **mét '
                        '($\\text{m}$)**, **ki-lô-mét ($\\text{km}$)**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết tên gọi, ký hiệu các đơn vị đo độ dài: '
                        '**đề-xi-mét ($\\text{dm}$)**, **mét ($\\text{m}$)**, **ki-lô-mét ($\\text{km}$)**.',
                        'Nhận biết tên gọi, ký hiệu các đơn vị đo độ dài: **đề-xi-mét ($\\text{dm}$)**, **mét '
                        '($\\text{m}$)**, **ki-lô-mét ($\\text{km}$)**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết tên gọi, ký hiệu các '
                        'đơn vị đo độ dài: **đề-xi-mét ($\\text{dm}$)**, **mét ($\\text{m}$)**, **ki-lô-mét '
                        '($\\text{km}$)**.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 55: Đề-xi-mét. Mét. Ki-lô-mét: Nhận biết tên gọi, ký '
                        'hiệu các đơn vị đo độ dài: **đề-xi-mét ($\\text{dm}$)**, **mét ($\\text{m}$)**, '
                        '**ki-lô-mét ($\\text{km}$)**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$2\\text{ m} = 20\\text{ dm}$.”',
            'answer': True,
            'solution': 'Vì $1\\text{ m} = 10\\text{ dm}$ nên $2\\text{ m} = 20\\text{ dm}$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 55: Đề-xi-mét. Mét. Ki-lô-mét**, quy tắc **Đề-xi-mét và Xăng-ti-mét** được xác '
                 'định bởi $1\\text{ dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$ và khi áp dụng cho '
                 'ví dụ “Đổi các đơn vị sau: a) $3\\text{ dm} = \\dots\\text{ cm}$; b) $2\\text{ m} = '
                 '\\dots\\text{ dm}$; c) $1\\text{ km} = \\dots\\text{ m}$.” ta có lời giải: a) $3\\text{ '
                 'dm} = 30\\text{ cm}$. b) $2\\text{ m} = 20\\text{ dm}$. c) $1\\text{ km} = 1000\\text{ '
                 'm}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đề-xi-mét và Xăng-ti-mét** ($1\\text{ '
                        'dm} = 10\\text{ cm}$; $10\\text{ cm} = 1\\text{ dm}$) và lời giải ví dụ minh họa '
                        'của Bài 55: Đề-xi-mét. Mét. Ki-lô-mét.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 55: Đề-xi-mét. Mét. Ki-lô-mét** để giải bài toán '
                 'sau: Đổi các đơn vị sau: a) $3\\text{ dm} = \\dots\\text{ cm}$; b) $2\\text{ m} = '
                 '\\dots\\text{ dm}$; c) $1\\text{ km} = \\dots\\text{ m}$. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['a) $4\\text{ dm} = 30\\text{ cm}$. b) $2\\text{ m} = 20\\text{ dm}$. c) $1\\text{ '
                        'km} = 1000\\text{ m}$.',
                        'a) $3\\text{ dm} = 30\\text{ cm}$. b) $2\\text{ m} = 20\\text{ dm}$. c) $1\\text{ '
                        'km} = 999\\text{ m}$.',
                        'a) $6\\text{ dm} = 30\\text{ cm}$. b) $2\\text{ m} = 20\\text{ dm}$. c) $1\\text{ '
                        'km} = 1000\\text{ m}$.',
                        'a) $3\\text{ dm} = 30\\text{ cm}$. b) $2\\text{ m} = 20\\text{ dm}$. c) $1\\text{ '
                        'km} = 1000\\text{ m}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 55: Đề-xi-mét. Mét. Ki-lô-mét: a) $3\\text{ dm} = '
                        '30\\text{ cm}$.\n'
                        'b) $2\\text{ m} = 20\\text{ dm}$.\n'
                        'c) $1\\text{ km} = 1000\\text{ m}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một sợi dây dài $1\\text{ m}$, bạn Nam cắt đi $35\\text{ cm}$. Hỏi phần dây còn lại dài '
                 'bao nhiêu xăng-ti-mét?',
            'answer': ['65', '65cm', '65 cm'],
            'unit': None,
            'solution': 'Đổi $1\\text{ m} = 100\\text{ cm}$. Phần dây còn lại dài là: $100 - 35 = 65$ '
                        '($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd11-do-dai-va-tien-viet-nam',
  'context_title': 'Chủ đề 11: Độ dài và đơn vị đo độ dài. Tiền Việt Nam',
  'context': 'SGK Toán 2 · Chủ đề 11: Đề-xi-mét, mét, ki-lô-mét; giới thiệu tiền Việt Nam; thực hành trải '
             'nghiệm đo độ dài.',
  'title': 'Bài 56: Giới thiệu tiền Việt Nam',
  'icon': '💵',
  'description': 'Nhận biết đơn vị tiền Việt Nam (đồng), mệnh giá các tờ tiền nhỏ và bài toán mua bán, đổi '
                 'tiền.',
  'requirements': ['Nhận biết đơn vị tiền Việt Nam là **đồng**.',
                   'Nhận diện được các tờ tiền mệnh giá $100$ đồng, $200$ đồng, $500$ đồng, $1000$ đồng.',
                   'Thực hiện được việc gộp tiền, đổi tiền và tính tiền thừa đơn giản.'],
  'definition': '- Đơn vị tiền của nước Việt Nam là **đồng**.\n'
                '- Giá trị của mỗi tờ tiền được ghi bằng số và chữ trên mặt tờ tiền (ví dụ: $100$ đồng, '
                '$200$ đồng, $500$ đồng, $1000$ đồng).',
  'theory': '- **Cách đổi tiền ngang giá trị:**\n'
            '  + $1$ tờ $500$ đồng $= 2$ tờ $200$ đồng $+ 1$ tờ $100$ đồng ($200 + 200 + 100 = 500$).\n'
            '  + $1$ tờ $1000$ đồng $= 2$ tờ $500$ đồng ($500 + 500 = 1000$).\n'
            '  + $1$ tờ $1000$ đồng $= 5$ tờ $200$ đồng ($200 \\times 5 = 1000$).\n'
            '- **Bài toán mua hàng:** $\\text{Tiền còn lại} = \\text{Tiền đang có} - \\text{Tổng tiền mua '
            'hàng}$.',
  'formulas': [{'category': 'Mệnh giá và quy đổi tiền Việt Nam',
                'items': [{'name': 'Đơn vị tiền tệ', 'formula': 'Đồng'},
                          {'name': 'Quy đổi 1000 đồng',
                           'formula': '$1000\\text{ đồng} = 500\\text{ đồng} + 500\\text{ đồng} = 5$ tờ '
                                      '$200\\text{ đồng} = 10$ tờ $100\\text{ đồng}$'},
                          {'name': 'Tính tiền thừa',
                           'formula': '$\\text{Tiền thừa} = \\text{Tiền đưa} - \\text{Giá tiền món đồ}$'}]}],
  'example': 'Trong ví của Mai có $1$ tờ $500$ đồng và $2$ tờ $200$ đồng. Hỏi trong ví của Mai có tất cả bao '
             'nhiêu tiền?',
  'example_answer': 'Số tiền trong ví của Mai là: $500 + 200 + 200 = 900$ (đồng).',
  'real_life': 'Giúp em biết tiết kiệm tiền vào heo đất, biết tính tiền khi đi siêu thị hoặc mua đồ dùng học '
               'tập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị tiền của nước Việt Nam là gì?',
            'options': ['Mét', 'Ki-lô-gam', 'Đồng', 'Lít'],
            'answer': 2,
            'solution': 'Tiền Việt Nam có đơn vị là đồng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một tờ giấy bạc mệnh giá $1000$ đồng có thể đổi được mấy tờ $500$ đồng?',
            'options': ['$1$ tờ', '$5$ tờ', '$10$ tờ', '$2$ tờ'],
            'answer': 3,
            'solution': 'Vì $500 + 500 = 1000$ nên $1$ tờ $1000$ đồng đổi được $2$ tờ $500$ đồng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 56: Giới thiệu tiền Việt Nam**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Đơn vị tiền tệ**?',
            'options': ['Đồng',
                        'Đồng (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đồng',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đồng'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 56: Giới thiệu tiền Việt Nam, **Đơn vị tiền tệ** '
                        'được xác định bởi: Đồng.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 56: Giới thiệu tiền Việt Nam**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Quy đổi 1000 đồng**?',
            'options': ['$1000\\text{ đồng} = 500\\text{ đồng} - 500\\text{ đồng} = 5$ tờ $200\\text{ đồng} '
                        '= 10$ tờ $100\\text{ đồng}$',
                        '$1000\\text{ đồng} = 500\\text{ đồng} + 500\\text{ đồng} = 5$ tờ $200\\text{ đồng} '
                        '= 10$ tờ $100\\text{ đồng}$',
                        '$1000\\text{ đồng} = 500\\text{ đồng} + 500\\text{ đồng} = 5$ tờ $200\\text{ đồng} '
                        '= 10$ tờ $99\\text{ đồng}$',
                        '$1002\\text{ đồng} = 500\\text{ đồng} + 500\\text{ đồng} = 5$ tờ $200\\text{ đồng} '
                        '= 10$ tờ $100\\text{ đồng}$'],
            'answer': 1,
            'solution': 'Trong Bài 56: Giới thiệu tiền Việt Nam, **Quy đổi 1000 đồng** có công thức/quy tắc '
                        'là: $1000\\text{ đồng} = 500\\text{ đồng} + 500\\text{ đồng} = 5$ tờ $200\\text{ '
                        'đồng} = 10$ tờ $100\\text{ đồng}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Lan có $1$ tờ $1000$ đồng, Lan mua một chiếc nhãn vở hết $600$ đồng. Hỏi Lan được trả lại '
                 'bao nhiêu tiền thừa?',
            'options': ['$300$ đồng', '$500$ đồng', '$400$ đồng', '$200$ đồng'],
            'answer': 2,
            'solution': 'Số tiền thừa của Lan là: $1000 - 600 = 400$ (đồng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 56: Giới thiệu tiền Việt Nam**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết đơn vị tiền Việt Nam là **đồng**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết đơn vị tiền Việt Nam là **đồng**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết đơn vị tiền Việt Nam '
                        'là **đồng**.',
                        'Nhận biết đơn vị tiền Việt Nam là **đồng**.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 56: Giới thiệu tiền Việt Nam: Nhận biết đơn vị tiền '
                        'Việt Nam là **đồng**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Hai tờ $500$ đồng có tổng giá trị bằng một tờ $1000$ đồng.”',
            'answer': True,
            'solution': 'Ta có $500 + 500 = 1000$ (đồng). Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 56: Giới thiệu tiền Việt Nam**, quy tắc **Đơn vị tiền tệ** được xác định bởi '
                 'Đồng và khi áp dụng cho ví dụ “Trong ví của Mai có $1$ tờ $500$ đồng và $2$ tờ $200$ đồng. '
                 'Hỏi trong ví của Mai có tất cả bao nhiêu tiền?” ta có lời giải: Số tiền trong ví của Mai '
                 'là: $500 + 200 + 200 = 900$ (đồng).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đơn vị tiền tệ** (Đồng) và lời giải ví '
                        'dụ minh họa của Bài 56: Giới thiệu tiền Việt Nam.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 56: Giới thiệu tiền Việt Nam** để giải bài toán '
                 'sau: Trong ví của Mai có $1$ tờ $500$ đồng và $2$ tờ $200$ đồng. Hỏi trong ví của Mai có '
                 'tất cả bao nhiêu tiền? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số tiền trong ví của Mai là: $500 + 200 + 200 = 900$ (đồng).',
                        'Số tiền trong ví của Mai là: $500 - 200 + 200 = 900$ (đồng).',
                        'Số tiền trong ví của Mai là: $500 + 200 + 200 = 899$ (đồng).',
                        'Số tiền trong ví của Mai là: $502 + 200 + 200 = 900$ (đồng).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 56: Giới thiệu tiền Việt Nam: Số tiền trong ví của Mai '
                        'là: $500 + 200 + 200 = 900$ (đồng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'An bỏ vào lợn đất $1$ tờ $500$ đồng, $1$ tờ $200$ đồng và $1$ tờ $100$ đồng. Hỏi An đã bỏ '
                 'vào lợn đất tất cả bao nhiêu đồng?',
            'answer': ['800'],
            'unit': None,
            'solution': 'Tổng số tiền An bỏ vào lợn đất là: $500 + 200 + 100 = 800$ (đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd11-do-dai-va-tien-viet-nam',
  'context_title': 'Chủ đề 11: Độ dài và đơn vị đo độ dài. Tiền Việt Nam',
  'context': 'SGK Toán 2 · Chủ đề 11: Đề-xi-mét, mét, ki-lô-mét; giới thiệu tiền Việt Nam; thực hành trải '
             'nghiệm đo độ dài.',
  'title': 'Bài 57: Thực hành và trải nghiệm đo độ dài',
  'icon': '🏃',
  'description': 'Ước lượng và thực hành đo độ dài bằng thước mét; giải bài toán thực tế về độ dài và tiền '
                 'Việt Nam.',
  'requirements': ['Ước lượng hợp lý kích thước các đồ vật quen thuộc theo đơn vị $\\text{cm}, \\text{dm}, '
                   '\\text{m}, \\text{km}$.',
                   'Thực hiện được các phép tính với số đo độ dài và tiền Việt Nam.',
                   'Vận dụng kiến thức của **Bài 57: Thực hành và trải nghiệm đo độ dài** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Để **ước lượng độ dài** chuẩn xác:\n'
                '- Một gang tay học sinh lớp 2 dài khoảng $1\\text{ dm}$ đến $15\\text{ cm}$.\n'
                '- Một bước chân dài khoảng $4\\text{ dm}$ đến $5\\text{ dm}$.\n'
                '- Một sải tay dang rộng dài khoảng $1\\text{ m}$.',
  'theory': '- **Chọn đơn vị đo phù hợp:**\n'
            '  + Chiều dài chiếc bút chì: khoảng $15\\text{ cm}$ (hoặc gần $2\\text{ dm}$).\n'
            '  + Chiều cao cánh cửa ra vào: khoảng $2\\text{ m}$.\n'
            '  + Chiều dài phòng học: khoảng $8\\text{ m}$.\n'
            '  + Quãng đường từ TP. Hồ Chí Minh đi Vũng Tàu: khoảng $100\\text{ km}$.',
  'formulas': [{'category': 'Mốc ước lượng độ dài thực tế',
                'items': [{'name': 'Đồ vật nhỏ',
                           'formula': 'Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ '
                                      '(khoảng $2\\text{ dm}$)'},
                          {'name': 'Vật vừa',
                           'formula': 'Sải tay $\\approx 1\\text{ m}$; Cánh cửa cao $\\approx 2\\text{ m}$; '
                                      'Phòng học dài $\\approx 8\\text{ m}$'},
                          {'name': 'Quãng đường xa',
                           'formula': 'Đo bằng đơn vị $\\text{km}$ ($1\\text{ km} = 1000\\text{ m}$)'}]}],
  'example': 'Tính: a) $35\\text{ m} + 28\\text{ m}$; b) $5\\text{ dm} \\times 6$.',
  'example_answer': 'a) $35\\text{ m} + 28\\text{ m} = 63\\text{ m}$.\n'
                    'b) $5\\text{ dm} \\times 6 = 30\\text{ dm}$ (hay $3\\text{ m}$).',
  'real_life': 'Đo chiều cao các bạn trong tổ bằng thước dây, ước lượng chiều rộng sân trường bằng bước '
               'chân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $35\\text{ m} + 28\\text{ m}$ là:',
            'options': ['$53\\text{ m}$', '$63\\text{ cm}$', '$7\\text{ m}$', '$63\\text{ m}$'],
            'answer': 3,
            'solution': 'Ta có $35 + 28 = 63$, giữ nguyên đơn vị $\\text{m}$ là $63\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Chiều cao của cánh cửa lớp học thường vào khoảng bao nhiêu?',
            'options': ['$2\\text{ m}$', '$2\\text{ cm}$', '$2\\text{ dm}$', '$2\\text{ km}$'],
            'answer': 0,
            'solution': 'Cánh cửa lớp học cao hơn đầu người lớn một chút, tức là khoảng $2\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 57: Thực hành và trải nghiệm đo độ dài**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Đồ vật nhỏ**?',
            'options': ['Cục tẩy $\\approx 5\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ '
                        'dm}$)',
                        'Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ '
                        'dm}$)',
                        'Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $1\\text{ '
                        'dm}$)',
                        'Cục tẩy $\\approx 8\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ '
                        'dm}$)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 57: Thực hành và trải nghiệm đo độ dài, **Đồ vật '
                        'nhỏ** được xác định bởi: Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx '
                        '15\\text{ cm}$ (khoảng $2\\text{ dm}$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 57: Thực hành và trải nghiệm đo độ dài**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Vật vừa**?',
            'options': ['Sải tay $\\approx 2\\text{ m}$; Cánh cửa cao $\\approx 2\\text{ m}$; Phòng học dài '
                        '$\\approx 8\\text{ m}$',
                        'Sải tay $\\approx 1\\text{ m}$; Cánh cửa cao $\\approx 2\\text{ m}$; Phòng học dài '
                        '$\\approx 7\\text{ m}$',
                        'Sải tay $\\approx 1\\text{ m}$; Cánh cửa cao $\\approx 2\\text{ m}$; Phòng học dài '
                        '$\\approx 8\\text{ m}$',
                        'Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ '
                        'dm}$)'],
            'answer': 2,
            'solution': 'Trong Bài 57: Thực hành và trải nghiệm đo độ dài, **Vật vừa** có công thức/quy tắc '
                        'là: Sải tay $\\approx 1\\text{ m}$; Cánh cửa cao $\\approx 2\\text{ m}$; Phòng học '
                        'dài $\\approx 8\\text{ m}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cắt một sợi dây dài $20\\text{ dm}$ thành $5$ đoạn bằng nhau. Hỏi mỗi đoạn dây dài bao '
                 'nhiêu đề-xi-mét?',
            'options': ['$15\\text{ dm}$', '$25\\text{ dm}$', '$5\\text{ dm}$', '$4\\text{ dm}$'],
            'answer': 3,
            'solution': 'Mỗi đoạn dây dài là: $20 : 5 = 4$ ($\\text{dm}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 57: Thực hành và trải nghiệm đo độ dài**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Ước lượng hợp lý kích thước các đồ vật quen thuộc theo đơn vị $\\text{cm}, '
                        '\\text{dm}, \\text{m}, \\text{km}$.',
                        'Ước lượng hợp lý kích thước các đồ vật quen thuộc theo đơn vị $\\text{cm}, '
                        '\\text{dm}, \\text{m}, \\text{km}$. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Ước lượng hợp lý kích thước các đồ vật quen thuộc theo '
                        'đơn vị $\\text{cm}, \\text{dm}, \\text{m}, \\text{km}$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Ước lượng hợp lý kích thước các '
                        'đồ vật quen thuộc theo đơn vị $\\text{cm}, \\text{dm}, \\text{m}, \\text{km}$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 57: Thực hành và trải nghiệm đo độ dài: Ước lượng hợp '
                        'lý kích thước các đồ vật quen thuộc theo đơn vị $\\text{cm}, \\text{dm}, \\text{m}, '
                        '\\text{km}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Một chiếc bút chì của học sinh dài khoảng $2\\text{ m}$.”',
            'answer': False,
            'solution': 'Chiếc bút chì chỉ dài khoảng $15\\text{ cm}$ đến $20\\text{ cm}$ ($2\\text{ dm}$), '
                        'không thể dài $2\\text{ m}$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 57: Thực hành và trải nghiệm đo độ dài**, quy tắc **Đồ vật nhỏ** được xác định '
                 'bởi Cục tẩy $\\approx 4\\text{ cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ '
                 'dm}$) và khi áp dụng cho ví dụ “Tính: a) $35\\text{ m} + 28\\text{ m}$; b) $5\\text{ dm} '
                 '\\times 6$.” ta có lời giải: a) $35\\text{ m} + 28\\text{ m} = 63\\text{ m}$. b) $5\\text{ '
                 'dm} \\times 6 = 30\\text{ dm}$ (hay $3\\text{ m}$).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đồ vật nhỏ** (Cục tẩy $\\approx 4\\text{ '
                        'cm}$; Bút chì $\\approx 15\\text{ cm}$ (khoảng $2\\text{ dm}$)) và lời giải ví dụ '
                        'minh họa của Bài 57: Thực hành và trải nghiệm đo độ dài.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 57: Thực hành và trải nghiệm đo độ dài** để giải '
                 'bài toán sau: Tính: a) $35\\text{ m} + 28\\text{ m}$; b) $5\\text{ dm} \\times 6$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $35\\text{ m} - 28\\text{ m} = 63\\text{ m}$. b) $5\\text{ dm} \\times 6 = '
                        '30\\text{ dm}$ (hay $3\\text{ m}$).',
                        'a) $35\\text{ m} + 28\\text{ m} = 63\\text{ m}$. b) $5\\text{ dm} \\times 6 = '
                        '30\\text{ dm}$ (hay $3\\text{ m}$).',
                        'a) $35\\text{ m} + 28\\text{ m} = 63\\text{ m}$. b) $5\\text{ dm} \\times 6 = '
                        '30\\text{ dm}$ (hay $2\\text{ m}$).',
                        'a) $70\\text{ m} + 28\\text{ m} = 63\\text{ m}$. b) $5\\text{ dm} \\times 6 = '
                        '30\\text{ dm}$ (hay $3\\text{ m}$).'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 57: Thực hành và trải nghiệm đo độ dài: a) $35\\text{ m} '
                        '+ 28\\text{ m} = 63\\text{ m}$.\n'
                        'b) $5\\text{ dm} \\times 6 = 30\\text{ dm}$ (hay $3\\text{ m}$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Con ốc sên thứ nhất bò được $4\\text{ dm}$, con ốc sên thứ hai bò được $35\\text{ cm}$. '
                 'Hỏi cả hai con ốc sên bò được tất cả bao nhiêu xăng-ti-mét?',
            'answer': ['75', '75cm', '75 cm'],
            'unit': None,
            'solution': 'Đổi $4\\text{ dm} = 40\\text{ cm}$. Cả hai con bò được: $40 + 35 = 75$ '
                        '($\\text{cm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd12-cong-tru-pham-vi-1000',
  'context_title': 'Chủ đề 12: Phép cộng, phép trừ trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 12: Phép cộng, phép trừ (không nhớ, có nhớ) trong phạm vi 1000; cộng, trừ '
             'nhẩm số tròn trăm, tròn chục.',
  'title': 'Bài 59: Phép cộng (không nhớ) trong phạm vi 1000',
  'icon': '➕',
  'description': 'Đặt tính và tính phép cộng (không nhớ) trong phạm vi 1000; cộng nhẩm các số tròn trăm, '
                 'tròn chục.',
  'requirements': ['Đặt tính đúng: các chữ số cùng hàng viết thẳng cột với nhau (đơn vị thẳng đơn vị, chục '
                   'thẳng chục, trăm thẳng trăm).',
                   'Tính đúng từ phải sang trái (hàng đơn vị $\\rightarrow$ hàng chục $\\rightarrow$ hàng '
                   'trăm).',
                   'Cộng nhẩm được các số tròn trăm, tròn chục trong phạm vi $1000$.'],
  'definition': 'Khi thực hiện **phép cộng (không nhớ) trong phạm vi $1000$**, ta đặt tính thẳng cột theo '
                'từng hàng rồi cộng lần lượt **từ phải sang trái**: hàng đơn vị cộng hàng đơn vị, hàng chục '
                'cộng hàng chục, hàng trăm cộng hàng trăm.',
  'theory': '- **Ví dụ 1 (Ba chữ số cộng ba chữ số): Tính $342 + 215$.**\n'
            '  + Hàng đơn vị: $2 + 5 = 7$, viết $7$.\n'
            '  + Hàng chục: $4 + 1 = 5$, viết $5$.\n'
            '  + Hàng trăm: $3 + 2 = 5$, viết $5$. Vậy $342 + 215 = 557$.\n'
            '- **Ví dụ 2 (Ba chữ số cộng hai chữ số): Tính $352 + 41$.**\n'
            '  + Chữ số $4$ (hàng chục) thẳng cột với $5$; chữ số $1$ (hàng đơn vị) thẳng cột với $2$. Kết '
            'quả: $352 + 41 = 393$.\n'
            '- **Cộng nhẩm số tròn trăm:** $400 + 300 = 700$ ($4$ trăm $+ 3$ trăm $= 7$ trăm); $600 + 400 = '
            '1000$.',
  'formulas': [{'category': 'Quy tắc cộng không nhớ trong phạm vi 1000',
                'items': [{'name': 'Đặt tính thẳng cột',
                           'formula': 'Đơn vị thẳng đơn vị, Chục thẳng chục, Trăm thẳng trăm'},
                          {'name': 'Thứ tự cộng',
                           'formula': 'Từ phải sang trái: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm',
                           'note': 'Ví dụ: $235 + 142 = 377$.'},
                          {'name': 'Cộng nhẩm tròn trăm',
                           'formula': '$a00 + b00 = (a + b)00$',
                           'note': 'Ví dụ: $400 + 300 = 700$.'}]}],
  'example': 'Đặt tính rồi tính: a) $235 + 142$; b) $520 + 68$.',
  'example_answer': 'a) $5 + 2 = 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$.\n'
                    'b) $0 + 8 = 8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 588$.',
  'real_life': 'Tính tổng số học sinh của trường, tổng số cây trồng được của hai khối lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $400 + 300$ là:',
            'options': ['$700$', '$70$', '$7000$', '$100$'],
            'answer': 0,
            'solution': '$4$ trăm $+ 3$ trăm $= 7$ trăm $= 700$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đặt tính $352 + 41$, chữ số $4$ của số $41$ phải viết thẳng cột với chữ số nào của số '
                 '$352$?',
            'options': ['Chữ số $3$', 'Chữ số $5$', 'Chữ số $2$', 'Không cần thẳng cột'],
            'answer': 1,
            'solution': 'Chữ số $4$ của số $41$ ở hàng chục nên phải thẳng cột với chữ số hàng chục của '
                        '$352$ là chữ số $5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 59: Phép cộng (không nhớ) trong phạm vi 1000**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Đặt tính thẳng cột**?',
            'options': ['Đơn vị thẳng đơn vị, Chục thẳng chục, Trăm thẳng trăm (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đơn vị thẳng đơn vị, Chục thẳng chục, Trăm thẳng trăm',
                        'Đơn vị thẳng đơn vị, Chục thẳng chục, Trăm thẳng trăm',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đơn vị thẳng đơn vị, Chục thẳng '
                        'chục, Trăm thẳng trăm'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 59: Phép cộng (không nhớ) trong phạm vi 1000, '
                        '**Đặt tính thẳng cột** được xác định bởi: Đơn vị thẳng đơn vị, Chục thẳng chục, '
                        'Trăm thẳng trăm.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 59: Phép cộng (không nhớ) trong phạm vi 1000**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Thứ tự cộng**?',
            'options': ['Từ trái sang phải: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm',
                        'Đảo ngược vế của quy tắc: Từ phải sang trái: Đơn vị $\\rightarrow$ Chục '
                        '$\\rightarrow$ Trăm',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Từ phải sang trái: Đơn vị '
                        '$\\rightarrow$ Chục $\\rightarrow$ Trăm',
                        'Từ phải sang trái: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm'],
            'answer': 3,
            'solution': 'Trong Bài 59: Phép cộng (không nhớ) trong phạm vi 1000, **Thứ tự cộng** có công '
                        'thức/quy tắc là: Từ phải sang trái: Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $235 + 142$ là:',
            'options': ['$377$', '$367$', '$387$', '$93$'],
            'answer': 0,
            'solution': 'Hàng đơn vị: $5 + 2 = 7$; hàng chục: $3 + 4 = 7$; hàng trăm: $2 + 1 = 3$. Vậy $235 '
                        '+ 142 = 377$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 59: Phép cộng (không nhớ) trong phạm vi 1000**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Đặt tính đúng: các chữ số cùng hàng viết thẳng cột với nhau (đơn vị thẳng đơn vị, '
                        'chục thẳng chục, trăm thẳng trăm). (với dấu ngược lại)',
                        'Đặt tính đúng: các chữ số cùng hàng viết thẳng cột với nhau (đơn vị thẳng đơn vị, '
                        'chục thẳng chục, trăm thẳng trăm).',
                        'Đảo ngược vế của quy tắc: Đặt tính đúng: các chữ số cùng hàng viết thẳng cột với '
                        'nhau (đơn vị thẳng đơn vị, chục thẳng chục, trăm thẳng trăm).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt tính đúng: các chữ số cùng '
                        'hàng viết thẳng cột với nhau (đơn vị thẳng đơn vị, chục thẳng chục, trăm thẳng '
                        'trăm).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 59: Phép cộng (không nhớ) trong phạm vi 1000: Đặt '
                        'tính đúng: các chữ số cùng hàng viết thẳng cột với nhau (đơn vị thẳng đơn vị, chục '
                        'thẳng chục, trăm thẳng trăm).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$600 + 400 = 1000$.”',
            'answer': True,
            'solution': '$6$ trăm $+ 4$ trăm $= 10$ trăm $= 1$ nghìn ($1000$). Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 59: Phép cộng (không nhớ) trong phạm vi 1000**, quy tắc **Đặt tính thẳng cột** '
                 'được xác định bởi Đơn vị thẳng đơn vị, Chục thẳng chục, Trăm thẳng trăm và khi áp dụng cho '
                 'ví dụ “Đặt tính rồi tính: a) $235 + 142$; b) $520 + 68$.” ta có lời giải: a) $5 + 2 = 7$; '
                 '$3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$. b) $0 + 8 = 8$; $2 + 6 = 8$; hạ $5 '
                 '\\Rightarrow 520 + 68 = 588$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đặt tính thẳng cột** (Đơn vị thẳng đơn '
                        'vị, Chục thẳng chục, Trăm thẳng trăm) và lời giải ví dụ minh họa của Bài 59: Phép '
                        'cộng (không nhớ) trong phạm vi 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 59: Phép cộng (không nhớ) trong phạm vi 1000** để '
                 'giải bài toán sau: Đặt tính rồi tính: a) $235 + 142$; b) $520 + 68$. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['a) $5 - 2 = 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$. b) $0 + 8 = '
                        '8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 588$.',
                        'a) $5 + 2 = 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$. b) $0 + 8 = '
                        '8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 587$.',
                        'a) $5 + 2 = 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$. b) $0 + 8 = '
                        '8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 588$.',
                        'a) $10 + 2 = 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$. b) $0 + 8 = '
                        '8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 588$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 59: Phép cộng (không nhớ) trong phạm vi 1000: a) $5 + 2 '
                        '= 7$; $3 + 4 = 7$; $2 + 1 = 3 \\Rightarrow 235 + 142 = 377$.\n'
                        'b) $0 + 8 = 8$; $2 + 6 = 8$; hạ $5 \\Rightarrow 520 + 68 = 588$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Con đường từ nhà An đến bưu điện dài $350\\text{ m}$, từ bưu điện đến trường dài '
                 '$420\\text{ m}$. Hỏi quãng đường từ nhà An đi qua bưu điện đến trường dài bao nhiêu mét?',
            'answer': ['770', '770m', '770 m'],
            'unit': None,
            'solution': 'Tổng độ dài quãng đường là: $350 + 420 = 770$ ($\\text{m}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd12-cong-tru-pham-vi-1000',
  'context_title': 'Chủ đề 12: Phép cộng, phép trừ trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 12: Phép cộng, phép trừ (không nhớ, có nhớ) trong phạm vi 1000; cộng, trừ '
             'nhẩm số tròn trăm, tròn chục.',
  'title': 'Bài 60: Phép cộng (có nhớ) trong phạm vi 1000',
  'icon': '🧮',
  'description': 'Thực hiện phép cộng (có nhớ không quá một lượt) các số trong phạm vi 1000.',
  'requirements': ['Thực hiện được phép cộng (có nhớ $1$ lần từ hàng đơn vị sang hàng chục, hoặc từ hàng '
                   'chục sang hàng trăm) trong phạm vi $1000$.',
                   'Giải được bài toán có lời văn vận dụng phép cộng có nhớ trong phạm vi $1000$.',
                   'Vận dụng kiến thức của **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Trong phép cộng phạm vi $1000$ (có nhớ một lượt):\n'
                '- Nếu tổng ở **hàng đơn vị** từ $10$ trở lên, ta viết chữ số đơn vị và **nhớ $1$ sang hàng '
                'chục**.\n'
                '- Nếu tổng ở **hàng chục** từ $10$ trở lên, ta viết chữ số hàng chục và **nhớ $1$ sang hàng '
                'trăm**.',
  'theory': '- **Ví dụ 1 (Nhớ sang hàng chục): Tính $265 + 127$.**\n'
            '  + Đơn vị: $5 + 7 = 12$, viết $2$ **nhớ $1$**.\n'
            '  + Chục: $6 + 2 = 8$, thêm $1$ bằng $9$, viết $9$.\n'
            '  + Trăm: $2 + 1 = 3$, viết $3$. Kết quả: $392$.\n'
            '- **Ví dụ 2 (Nhớ sang hàng trăm): Tính $473 + 254$.**\n'
            '  + Đơn vị: $3 + 4 = 7$, viết $7$.\n'
            '  + Chục: $7 + 5 = 12$, viết $2$ **nhớ $1$**.\n'
            '  + Trăm: $4 + 2 = 6$, thêm $1$ bằng $7$, viết $7$. Kết quả: $727$.',
  'formulas': [{'category': 'Quy tắc cộng có nhớ trong phạm vi 1000',
                'items': [{'name': 'Nhớ từ đơn vị sang chục',
                           'formula': 'Đơn vị cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng chục',
                           'note': 'Ví dụ: $456 + 238 = 694$.'},
                          {'name': 'Nhớ từ chục sang trăm',
                           'formula': 'Chục cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng trăm',
                           'note': 'Ví dụ: $382 + 145 = 527$.'}]}],
  'example': 'Đặt tính rồi tính: a) $538 + 245$; b) $374 + 162$.',
  'example_answer': 'a) $8 + 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + 245 = '
                    '783$.\n'
                    'b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 \\Rightarrow 374 + 162 = '
                    '536$.',
  'real_life': 'Tính tổng sản lượng nông sản thu hoạch, tổng lượng nước trong hai bể chứa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $456 + 238$ là:',
            'options': ['$684$', '$694$', '$614$', '$218$'],
            'answer': 1,
            'solution': 'Đơn vị: $6 + 8 = 14$ viết $4$ nhớ $1$; chục: $5 + 3 + 1 = 9$; trăm: $4 + 2 = 6$. '
                        'Vậy $456 + 238 = 694$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $362 + 9$ là:',
            'options': ['$452$', '$361$', '$371$', '$3611$'],
            'answer': 2,
            'solution': 'Đơn vị: $2 + 9 = 11$ viết $1$ nhớ $1$; chục: $6 + 1 = 7$; hạ $3$ trăm. Vậy $362 + 9 '
                        '= 371$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Nhớ từ đơn vị sang chục**?',
            'options': ['Đơn vị cộng lại $\\le 10 \\rightarrow$ nhớ $1$ vào hàng chục',
                        'Đơn vị cộng lại $\\ge 10 \\rightarrow$ nhớ $2$ vào hàng chục',
                        'Đơn vị cộng lại $\\ge 20 \\rightarrow$ nhớ $1$ vào hàng chục',
                        'Đơn vị cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng chục'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 60: Phép cộng (có nhớ) trong phạm vi 1000, **Nhớ '
                        'từ đơn vị sang chục** được xác định bởi: Đơn vị cộng lại $\\ge 10 \\rightarrow$ nhớ '
                        '$1$ vào hàng chục. (Ví dụ: $456 + 238 = 694$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Nhớ từ chục sang trăm**?',
            'options': ['Chục cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng trăm',
                        'Chục cộng lại $\\le 10 \\rightarrow$ nhớ $1$ vào hàng trăm',
                        'Chục cộng lại $\\ge 10 \\rightarrow$ nhớ $2$ vào hàng trăm',
                        'Chục cộng lại $\\ge 20 \\rightarrow$ nhớ $1$ vào hàng trăm'],
            'answer': 0,
            'solution': 'Trong Bài 60: Phép cộng (có nhớ) trong phạm vi 1000, **Nhớ từ chục sang trăm** có '
                        'công thức/quy tắc là: Chục cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng trăm.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $485 + 260$ là:',
            'options': ['$645$', '$745$', '$755$', '$6145$'],
            'answer': 1,
            'solution': 'Đơn vị: $5 + 0 = 5$; chục: $8 + 6 = 14$ viết $4$ nhớ $1$; trăm: $4 + 2 + 1 = 7$. '
                        'Vậy $485 + 260 = 745$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng (có nhớ $2$ lần từ hàng đơn vị sang hàng chục, hoặc từ '
                        'hàng chục sang hàng trăm) trong phạm vi $1000$.',
                        'Thực hiện được phép cộng (có nhớ $1$ lần từ hàng đơn vị sang hàng chục, hoặc từ '
                        'hàng chục sang hàng trăm) trong phạm vi $999$.',
                        'Thực hiện được phép cộng (có nhớ $1$ lần từ hàng đơn vị sang hàng chục, hoặc từ '
                        'hàng chục sang hàng trăm) trong phạm vi $1000$.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 60: Phép cộng (có nhớ) trong phạm vi 1000: Thực hiện '
                        'được phép cộng (có nhớ $1$ lần từ hàng đơn vị sang hàng chục, hoặc từ hàng chục '
                        'sang hàng trăm) trong phạm vi $1000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$362 + 9 = 452$.”',
            'answer': False,
            'solution': 'Chữ số $9$ là $9$ đơn vị nên $362 + 9 = 371$ (viết nhầm $9$ thẳng hàng chục mới ra '
                        '$452$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000**, quy tắc **Nhớ từ đơn vị sang '
                 'chục** được xác định bởi Đơn vị cộng lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng chục và '
                 'khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $538 + 245$; b) $374 + 162$.” ta có lời giải: '
                 'a) $8 + 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + 245 = '
                 '783$. b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nhớ từ đơn vị sang chục** (Đơn vị cộng '
                        'lại $\\ge 10 \\rightarrow$ nhớ $1$ vào hàng chục) và lời giải ví dụ minh họa của '
                        'Bài 60: Phép cộng (có nhớ) trong phạm vi 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 60: Phép cộng (có nhớ) trong phạm vi 1000** để giải '
                 'bài toán sau: Đặt tính rồi tính: a) $538 + 245$; b) $374 + 162$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['a) $8 - 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + '
                        '245 = 783$. b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 '
                        '\\Rightarrow 374 + 162 = 536$...',
                        'a) $8 + 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + '
                        '245 = 783$. b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 '
                        '\\Rightarrow 374 + 162 = 535$...',
                        'a) $16 + 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + '
                        '245 = 783$. b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 '
                        '\\Rightarrow 374 + 162 = 536$...',
                        'a) $8 + 5 = 13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + '
                        '245 = 783$. b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 '
                        '\\Rightarrow 374 + 162 = 536$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 60: Phép cộng (có nhớ) trong phạm vi 1000: a) $8 + 5 = '
                        '13$ viết $3$ nhớ $1$; $3 + 4 + 1 = 8$; $5 + 2 = 7 \\Rightarrow 538 + 245 = 783$.\n'
                        'b) $4 + 2 = 6$; $7 + 6 = 13$ viết $3$ nhớ $1$; $3 + 1 + 1 = 5 \\Rightarrow 374 + '
                        '162 = 536$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Thùng thứ nhất có $245\\text{ l}$ nước, thùng thứ hai có nhiều hơn thùng thứ nhất '
                 '$136\\text{ l}$ nước. Hỏi thùng thứ hai có bao nhiêu lít nước?',
            'answer': ['381', '381l', '381 l'],
            'unit': None,
            'solution': 'Số lít nước ở thùng thứ hai là: $245 + 136 = 381$ ($\\text{l}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd12-cong-tru-pham-vi-1000',
  'context_title': 'Chủ đề 12: Phép cộng, phép trừ trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 12: Phép cộng, phép trừ (không nhớ, có nhớ) trong phạm vi 1000; cộng, trừ '
             'nhẩm số tròn trăm, tròn chục.',
  'title': 'Bài 61: Phép trừ (không nhớ) trong phạm vi 1000',
  'icon': '➖',
  'description': 'Đặt tính và tính phép trừ (không nhớ) trong phạm vi 1000; trừ nhẩm số tròn trăm, tròn '
                 'chục.',
  'requirements': ['Đặt tính thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $1000$ từ phải '
                   'sang trái.',
                   'Trừ nhẩm nhanh các số tròn trăm, tròn chục.',
                   'Vận dụng kiến thức của **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi thực hiện **phép trừ (không nhớ) trong phạm vi $1000$**, ta đặt tính thẳng cột theo '
                'từng hàng rồi trừ lần lượt **từ phải sang trái**: hàng đơn vị trừ hàng đơn vị, hàng chục '
                'trừ hàng chục, hàng trăm trừ hàng trăm.',
  'theory': '- **Ví dụ: Tính $786 - 354$.**\n'
            '  + Hàng đơn vị: $6 - 4 = 2$, viết $2$.\n'
            '  + Hàng chục: $8 - 5 = 3$, viết $3$.\n'
            '  + Hàng trăm: $7 - 3 = 4$, viết $4$. Vậy $786 - 354 = 432$.\n'
            '- **Trừ nhẩm số tròn trăm, tròn chục:**\n'
            '  + $800 - 300 = 500$ ($8$ trăm $- 3$ trăm $= 5$ trăm).\n'
            '  + $1000 - 400 = 600$ ($10$ trăm $- 4$ trăm $= 6$ trăm).\n'
            '  + $650 - 30 = 620$.',
  'formulas': [{'category': 'Quy tắc trừ không nhớ trong phạm vi 1000',
                'items': [{'name': 'Thứ tự trừ',
                           'formula': 'Đặt thẳng cột; trừ từ phải sang trái (Đơn vị $\\rightarrow$ Chục '
                                      '$\\rightarrow$ Trăm)',
                           'note': 'Ví dụ: $869 - 425 = 444$.'},
                          {'name': 'Trừ nhẩm tròn trăm',
                           'formula': '$a00 - b00 = (a - b)00$; $1000 - b00 = (10 - b)00$',
                           'note': 'Ví dụ: $1000 - 300 = 700$.'}]}],
  'example': 'Tính: a) $869 - 425$; b) $500 - 200 + 300$.',
  'example_answer': 'a) $9 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$.\n'
                    'b) $500 - 200 + 300 = 300 + 300 = 600$.',
  'real_life': 'Tính số mét đường còn lại chưa trải nhựa, số tiền còn lại sau khi mua hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $869 - 425$ là:',
            'options': ['$434$', '$454$', '$444$', '$1294$'],
            'answer': 2,
            'solution': 'Đơn vị: $9 - 5 = 4$; chục: $6 - 2 = 4$; trăm: $8 - 4 = 4$. Vậy $869 - 425 = 444$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính nhẩm $1000 - 400$ là:',
            'options': ['$500$', '$700$', '$60$', '$600$'],
            'answer': 3,
            'solution': '$10$ trăm $- 4$ trăm $= 6$ trăm $= 600$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Thứ tự trừ**?',
            'options': ['Đặt thẳng cột; trừ từ phải sang trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm)',
                        'Đặt thẳng cột; trừ từ trái sang phải (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                        'Trăm)',
                        'Đảo ngược vế của quy tắc: Đặt thẳng cột; trừ từ phải sang trái (Đơn vị '
                        '$\\rightarrow$ Chục $\\rightarrow$ Trăm)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt thẳng cột; trừ từ phải sang '
                        'trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 61: Phép trừ (không nhớ) trong phạm vi 1000, **Thứ '
                        'tự trừ** được xác định bởi: Đặt thẳng cột; trừ từ phải sang trái (Đơn vị '
                        '$\\rightarrow$ Chục $\\rightarrow$ Trăm). (Ví dụ: $869 - 425 = 444$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Trừ nhẩm tròn trăm**?',
            'options': ['$a00 + b00 = (a - b)00$; $1000 - b00 = (10 - b)00$',
                        '$a00 - b00 = (a - b)00$; $1000 - b00 = (10 - b)00$',
                        '$a00 - b00 = (a - b)00$; $1000 - b00 = (10 - b)1$',
                        '$a00 - b00 = (a - b)2$; $1000 - b00 = (10 - b)00$'],
            'answer': 1,
            'solution': 'Trong Bài 61: Phép trừ (không nhớ) trong phạm vi 1000, **Trừ nhẩm tròn trăm** có '
                        'công thức/quy tắc là: $a00 - b00 = (a - b)00$; $1000 - b00 = (10 - b)00$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $680 - 50 + 20$ là:',
            'options': ['$610$', '$630$', '$650$', '$750$'],
            'answer': 2,
            'solution': 'Tính từ trái sang phải: $680 - 50 = 630$, sau đó $630 + 20 = 650$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Đặt tính thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $1000$ từ '
                        'trái sang phải.',
                        'Đặt tính thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $999$ từ '
                        'phải sang trái.',
                        'Đặt tính thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $1002$ từ '
                        'phải sang trái.',
                        'Đặt tính thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $1000$ từ '
                        'phải sang trái.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 61: Phép trừ (không nhớ) trong phạm vi 1000: Đặt tính '
                        'thẳng cột và thực hiện đúng phép trừ (không nhớ) trong phạm vi $1000$ từ phải sang '
                        'trái.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$579 - 45 = 129$.”',
            'answer': False,
            'solution': 'Số $45$ gồm $4$ chục và $5$ đơn vị, trừ đúng cột phải là $579 - 45 = 534$ (viết '
                        'lệch $45$ sang hàng trăm mới ra $129$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000**, quy tắc **Thứ tự trừ** được xác '
                 'định bởi Đặt thẳng cột; trừ từ phải sang trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ '
                 'Trăm) và khi áp dụng cho ví dụ “Tính: a) $869 - 425$; b) $500 - 200 + 300$.” ta có lời '
                 'giải: a) $9 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$. b) $500 - 200 '
                 '+ 300 = 300 + 300 = 600$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thứ tự trừ** (Đặt thẳng cột; trừ từ phải '
                        'sang trái (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm)) và lời giải ví dụ minh '
                        'họa của Bài 61: Phép trừ (không nhớ) trong phạm vi 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 61: Phép trừ (không nhớ) trong phạm vi 1000** để '
                 'giải bài toán sau: Tính: a) $869 - 425$; b) $500 - 200 + 300$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['a) $9 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$. b) $500 - '
                        '200 + 300 = 300 + 300 = 600$.',
                        'a) $9 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$. b) $500 - '
                        '200 - 300 = 300 + 300 = 600$.',
                        'a) $9 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$. b) $500 - '
                        '200 + 300 = 300 + 300 = 599$.',
                        'a) $18 - 5 = 4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$. b) $500 - '
                        '200 + 300 = 300 + 300 = 600$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 61: Phép trừ (không nhớ) trong phạm vi 1000: a) $9 - 5 = '
                        '4$; $6 - 2 = 4$; $8 - 4 = 4 \\Rightarrow 869 - 425 = 444$.\n'
                        'b) $500 - 200 + 300 = 300 + 300 = 600$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một kho thóc có $785\\text{ kg}$ thóc, người ta đã lấy ra $250\\text{ kg}$ thóc. Hỏi trong '
                 'kho còn lại bao nhiêu ki-lô-gam thóc?',
            'answer': ['535', '535kg', '535 kg'],
            'unit': None,
            'solution': 'Số ki-lô-gam thóc còn lại trong kho là: $785 - 250 = 535$ ($\\text{kg}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd12-cong-tru-pham-vi-1000',
  'context_title': 'Chủ đề 12: Phép cộng, phép trừ trong phạm vi 1000',
  'context': 'SGK Toán 2 · Chủ đề 12: Phép cộng, phép trừ (không nhớ, có nhớ) trong phạm vi 1000; cộng, trừ '
             'nhẩm số tròn trăm, tròn chục.',
  'title': 'Bài 62: Phép trừ (có nhớ) trong phạm vi 1000',
  'icon': '🎯',
  'description': 'Thực hiện phép trừ (có nhớ không quá một lượt) trong phạm vi 1000 và giải bài toán thực '
                 'tế.',
  'requirements': ['Thực hiện được phép trừ (có nhớ $1$ lượt ở hàng chục hoặc hàng trăm) trong phạm vi '
                   '$1000$.',
                   'Biết thử lại phép trừ bằng phép cộng ($\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị '
                   'trừ}$).',
                   'Giải được bài toán có lời văn vận dụng phép trừ có nhớ trong phạm vi $1000$.'],
  'definition': 'Trong phép trừ phạm vi $1000$ (có nhớ một lượt):\n'
                '- Khi chữ số ở một hàng của số bị trừ **bé hơn** chữ số cùng hàng của số trừ, ta **mượn '
                '$10$** ở hàng ngay bên trái để trừ, viết kết quả rồi **nhớ $1$** trả vào chữ số hàng bên '
                'trái của số trừ.',
  'theory': '- **Ví dụ 1 (Mượn ở hàng chục): Tính $452 - 128$.**\n'
            '  + Đơn vị: $2$ không trừ được $8$, lấy $12 - 8 = 4$, viết $4$ **nhớ $1$**.\n'
            '  + Chục: $2$ thêm $1$ bằng $3$; $5 - 3 = 2$, viết $2$.\n'
            '  + Trăm: $4 - 1 = 3$, viết $3$. Kết quả: $324$.\n'
            '- **Ví dụ 2 (Mượn ở hàng trăm): Tính $746 - 382$.**\n'
            '  + Đơn vị: $6 - 2 = 4$, viết $4$.\n'
            '  + Chục: $4$ không trừ được $8$, lấy $14 - 8 = 6$, viết $6$ **nhớ $1$**.\n'
            '  + Trăm: $3$ thêm $1$ bằng $4$; $7 - 4 = 3$, viết $3$. Kết quả: $364$.',
  'formulas': [{'category': 'Quy tắc trừ có nhớ trong phạm vi 1000',
                'items': [{'name': 'Quy tắc mượn – trả',
                           'formula': 'Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $10$ để trừ, nhớ $1$ '
                                      'sang hàng kế tiếp bên trái'},
                          {'name': 'Kiểm tra kết quả',
                           'formula': '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                           'note': 'Ví dụ: $324 + 128 = 452$.'}]}],
  'example': 'Đặt tính rồi tính: a) $671 - 236$; b) $740 - 50 + 10$.',
  'example_answer': 'a) $11 - 6 = 5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - 236 = '
                    '435$.\n'
                    'b) $740 - 50 + 10 = 690 + 10 = 700$.',
  'real_life': 'Tính số học sinh nam khi biết tổng số học sinh toàn trường và số học sinh nữ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trường Tiểu học có $465$ học sinh, trong đó có $238$ học sinh nữ. Số học sinh nam của '
                 'trường là:',
            'options': ['$237$ học sinh', '$703$ học sinh', '$233$ học sinh', '$227$ học sinh'],
            'answer': 3,
            'solution': 'Số học sinh nam là: $465 - 238 = 227$ ($15 - 8 = 7$ nhớ $1$; $6 - 4 = 2$; $4 - 2 = '
                        '2$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $740 - 50 + 10$ là:',
            'options': ['$700$', '$680$', '$800$', '$690$'],
            'answer': 0,
            'solution': 'Tính từ trái sang phải: $740 - 50 = 690$, sau đó $690 + 10 = 700$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 62: Phép trừ (có nhớ) trong phạm vi 1000**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Quy tắc mượn – trả**?',
            'options': ['Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $11$ để trừ, nhớ $1$ sang hàng kế '
                        'tiếp bên trái',
                        'Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $10$ để trừ, nhớ $1$ sang hàng kế '
                        'tiếp bên trái',
                        'Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $10$ để trừ, nhớ $2$ sang hàng kế '
                        'tiếp bên trái',
                        'Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $20$ để trừ, nhớ $1$ sang hàng kế '
                        'tiếp bên trái'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 62: Phép trừ (có nhớ) trong phạm vi 1000, **Quy '
                        'tắc mượn – trả** được xác định bởi: Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm '
                        '$10$ để trừ, nhớ $1$ sang hàng kế tiếp bên trái.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 62: Phép trừ (có nhớ) trong phạm vi 1000**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Kiểm tra kết quả**?',
            'options': ['$\\text{Hiệu} - \\text{Số trừ} = \\text{Số bị trừ}$',
                        'Đảo ngược vế của quy tắc: $\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        '$\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Hiệu} + \\text{Số trừ} '
                        '= \\text{Số bị trừ}$'],
            'answer': 2,
            'solution': 'Trong Bài 62: Phép trừ (có nhớ) trong phạm vi 1000, **Kiểm tra kết quả** có công '
                        'thức/quy tắc là: $\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $835 - 271$ là:',
            'options': ['$664$', '$544$', '$644$', '$564$'],
            'answer': 3,
            'solution': 'Đơn vị: $5 - 1 = 4$; chục: $13 - 7 = 6$ nhớ $1$; trăm: $2 + 1 = 3$, $8 - 3 = 5$. '
                        'Vậy $835 - 271 = 564$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 62: Phép trừ (có nhớ) trong phạm vi 1000**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Thực hiện được phép trừ (có nhớ $1$ lượt ở hàng chục hoặc hàng trăm) trong phạm vi '
                        '$1000$.',
                        'Thực hiện được phép trừ (có nhớ $2$ lượt ở hàng chục hoặc hàng trăm) trong phạm vi '
                        '$1000$.',
                        'Thực hiện được phép trừ (có nhớ $1$ lượt ở hàng chục hoặc hàng trăm) trong phạm vi '
                        '$999$.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 62: Phép trừ (có nhớ) trong phạm vi 1000: Thực hiện '
                        'được phép trừ (có nhớ $1$ lượt ở hàng chục hoặc hàng trăm) trong phạm vi $1000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$746 - 382 = 464$.”',
            'answer': False,
            'solution': 'Ở hàng chục lấy $14 - 8 = 6$ phải nhớ $1$ sang hàng trăm ($3 + 1 = 4$, $7 - 4 = '
                        '3$), nên kết quả đúng là $364$ chứ không phải $464$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 62: Phép trừ (có nhớ) trong phạm vi 1000**, quy tắc **Quy tắc mượn – trả** '
                 'được xác định bởi Chữ số trên $<$ chữ số dưới $\\rightarrow$ thêm $10$ để trừ, nhớ $1$ '
                 'sang hàng kế tiếp bên trái và khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $671 - 236$; b) '
                 '$740 - 50 + 10$.” ta có lời giải: a) $11 - 6 = 5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - '
                 '2 = 4 \\Rightarrow 671 - 236 = 435$. b) $740 - 50 + 10 = 690 + 10 = 700$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy tắc mượn – trả** (Chữ số trên $<$ '
                        'chữ số dưới $\\rightarrow$ thêm $10$ để trừ, nhớ $1$ sang hàng kế tiếp bên trái) và '
                        'lời giải ví dụ minh họa của Bài 62: Phép trừ (có nhớ) trong phạm vi 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 62: Phép trừ (có nhớ) trong phạm vi 1000** để giải '
                 'bài toán sau: Đặt tính rồi tính: a) $671 - 236$; b) $740 - 50 + 10$. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['a) $11 - 6 = 5$ nhớ $1$; $3 - 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - '
                        '236 = 435$. b) $740 - 50 + 10 = 690 + 10 = 700$.',
                        'a) $11 - 6 = 5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - '
                        '236 = 435$. b) $740 - 50 + 10 = 690 + 10 = 700$.',
                        'a) $11 - 6 = 5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - '
                        '236 = 435$. b) $740 - 50 + 10 = 690 + 10 = 699$.',
                        'a) $22 - 6 = 5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - '
                        '236 = 435$. b) $740 - 50 + 10 = 690 + 10 = 700$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 62: Phép trừ (có nhớ) trong phạm vi 1000: a) $11 - 6 = '
                        '5$ nhớ $1$; $3 + 1 = 4$, $7 - 4 = 3$; $6 - 2 = 4 \\Rightarrow 671 - 236 = 435$.\n'
                        'b) $740 - 50 + 10 = 690 + 10 = 700$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một con đường dài $900\\text{ m}$. Đội công nhân đã sửa được $350\\text{ m}$. Hỏi còn bao '
                 'nhiêu mét đường chưa được sửa?',
            'answer': ['550', '550m', '550 m'],
            'unit': None,
            'solution': 'Số mét đường chưa sửa là: $900 - 350 = 550$ ($\\text{m}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd13-thong-ke-xac-suat',
  'context_title': 'Chủ đề 13: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 2 · Chủ đề 13: Thu thập, phân loại, kiểm đếm số liệu; biểu đồ tranh; chắc chắn, có '
             'thể, không thể; thực hành trải nghiệm.',
  'title': 'Bài 64: Thu thập, phân loại, kiểm đếm số liệu',
  'icon': '📊',
  'description': 'Thực hiện thu thập, phân loại đối tượng và kiểm đếm số lượng để ghi vào bảng thống kê.',
  'requirements': ['Biết **thu thập** và **phân loại** các đối tượng theo tiêu chí cho trước (màu sắc, hình '
                   'dạng, con vật, môn thể thao yêu thích).',
                   'Biết **kiểm đếm** chính xác số lượng mỗi loại (bằng cách đếm hoặc gạch vạch kiểm đếm) và '
                   'ghi kết quả.',
                   'Vận dụng kiến thức của **Bài 64: Thu thập, phân loại, kiểm đếm số liệu** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Quá trình thống kê cơ bản gồm $3$ bước:\n'
                '1. **Thu thập:** Tập hợp các thông tin, đối tượng cần tìm hiểu.\n'
                '2. **Phân loại:** Chia các đối tượng thành từng nhóm có cùng đặc điểm.\n'
                '3. **Kiểm đếm:** Đếm số lượng đối tượng trong mỗi nhóm và ghi lại bằng con số.',
  'theory': '- Khi kiểm đếm nhiều đối tượng lộn xộn, người ta thường dùng **vạch kiểm đếm**: mỗi đối tượng '
            'gạch $1$ vạch thẳng, cứ đủ $5$ đối tượng tạo thành một cụm $5$ vạch.\n'
            '- Sau khi kiểm đếm xong, ta dễ dàng trả lời các câu hỏi: Loại nào có nhiều nhất? Loại nào có ít '
            'nhất? Hai loại hơn kém nhau bao nhiêu?',
  'formulas': [{'category': 'Quy trình thống kê số liệu',
                'items': [{'name': '3 bước thực hiện',
                           'formula': 'Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm'},
                          {'name': 'Tổng số đối tượng',
                           'formula': 'Bằng tổng số lượng của tất cả các nhóm cộng lại'}]}],
  'example': 'Khảo sát màu sắc yêu thích của các bạn trong nhóm: Đỏ, Xanh, Đỏ, Vàng, Đỏ, Xanh. Hãy phân loại '
             'và kiểm đếm số bạn thích mỗi màu.',
  'example_answer': 'Có $3$ màu sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng cộng '
                    'có $3 + 2 + 1 = 6$ bạn.',
  'real_life': 'Kiểm đếm số phiếu bầu lớp trưởng, số bạn đăng ký từng câu lạc bộ năng khiếu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong tổ 1, màu sắc yêu thích của $5$ bạn lần lượt là: đỏ, xanh, đỏ, vàng, đỏ. Số bạn '
                 'thích màu đỏ là:',
            'options': ['$3$ bạn', '$1$ bạn', '$2$ bạn', '$5$ bạn'],
            'answer': 0,
            'solution': 'Đếm từ “đỏ” xuất hiện $3$ lần, vậy có $3$ bạn thích màu đỏ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi chia một rổ gồm các khối lập phương, khối trụ, khối cầu thành $3$ nhóm riêng theo hình '
                 'dạng, hoạt động đó gọi là:',
            'options': ['Đo độ dài', 'Phân loại', 'Xem lịch', 'Đặt tính'],
            'answer': 1,
            'solution': 'Chia các đồ vật thành từng nhóm có cùng đặc điểm gọi là phân loại.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 64: Thu thập, phân loại, kiểm đếm số liệu**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **3 bước thực hiện**?',
            'options': ['Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm',
                        'Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thu thập $\\rightarrow$ Phân '
                        'loại $\\rightarrow$ Kiểm đếm'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 64: Thu thập, phân loại, kiểm đếm số liệu, **3 '
                        'bước thực hiện** được xác định bởi: Thu thập $\\rightarrow$ Phân loại '
                        '$\\rightarrow$ Kiểm đếm.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 64: Thu thập, phân loại, kiểm đếm số liệu**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Tổng số đối tượng**?',
            'options': ['Bằng tổng số lượng của tất cả các nhóm cộng lại (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Bằng tổng số lượng của tất cả các nhóm cộng lại',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Bằng tổng số lượng của tất cả '
                        'các nhóm cộng lại',
                        'Bằng tổng số lượng của tất cả các nhóm cộng lại'],
            'answer': 3,
            'solution': 'Trong Bài 64: Thu thập, phân loại, kiểm đếm số liệu, **Tổng số đối tượng** có công '
                        'thức/quy tắc là: Bằng tổng số lượng của tất cả các nhóm cộng lại.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Sau khi kiểm đếm các hình phẳng trong hộp, Mai ghi được: Hình tam giác: $8$ hình; Hình '
                 'vuông: $5$ hình; Hình tròn: $10$ hình. Hình nào có số lượng ít nhất?',
            'options': ['Hình vuông', 'Hình tam giác', 'Hình tròn', 'Ba loại bằng nhau'],
            'answer': 0,
            'solution': 'Vì $5 < 8 < 10$ nên hình vuông có số lượng ít nhất ($5$ hình).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 64: Thu thập, phân loại, kiểm đếm số liệu**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Biết **thu thập** và **phân loại** các đối tượng theo tiêu chí cho trước (màu sắc, '
                        'hình dạng, con vật, môn thể thao yêu thích). (với dấu ngược lại)',
                        'Biết **thu thập** và **phân loại** các đối tượng theo tiêu chí cho trước (màu sắc, '
                        'hình dạng, con vật, môn thể thao yêu thích).',
                        'Đảo ngược vế của quy tắc: Biết **thu thập** và **phân loại** các đối tượng theo '
                        'tiêu chí cho trước (màu sắc, hình dạng, con vật, môn thể thao yêu thích).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Biết **thu thập** và **phân '
                        'loại** các đối tượng theo tiêu chí cho trước (màu sắc, hình dạng, con vật, môn thể '
                        'thao yêu thích).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 64: Thu thập, phân loại, kiểm đếm số liệu: Biết **thu '
                        'thập** và **phân loại** các đối tượng theo tiêu chí cho trước (màu sắc, hình dạng, '
                        'con vật, môn thể thao yêu thích).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu trong giỏ có $6$ quả táo, $4$ quả cam và $5$ quả xoài thì trong giỏ có tất '
                 'cả $15$ quả.”',
            'answer': True,
            'solution': 'Tổng số quả trong giỏ là $6 + 4 + 5 = 15$ (quả). Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 64: Thu thập, phân loại, kiểm đếm số liệu**, quy tắc **3 bước thực hiện** được '
                 'xác định bởi Thu thập $\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm và khi áp dụng cho '
                 'ví dụ “Khảo sát màu sắc yêu thích của các bạn trong nhóm: Đỏ, Xanh, Đỏ, Vàng, Đỏ, Xanh. '
                 'Hãy phân loại và kiểm đếm số bạn thích mỗi màu.” ta có lời giải: Có $3$ màu sắc: màu Đỏ có '
                 '$3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng cộng có $3 + 2 + 1 = 6$ bạn.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **3 bước thực hiện** (Thu thập '
                        '$\\rightarrow$ Phân loại $\\rightarrow$ Kiểm đếm) và lời giải ví dụ minh họa của '
                        'Bài 64: Thu thập, phân loại, kiểm đếm số liệu.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 64: Thu thập, phân loại, kiểm đếm số liệu** để giải '
                 'bài toán sau: Khảo sát màu sắc yêu thích của các bạn trong nhóm: Đỏ, Xanh, Đỏ, Vàng, Đỏ, '
                 'Xanh. Hãy phân loại và kiểm đếm số bạn thích mỗi màu. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Có $3$ màu sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng '
                        'cộng có $3 - 2 + 1 = 6$ bạn.',
                        'Có $3$ màu sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng '
                        'cộng có $3 + 2 + 1 = 5$ bạn.',
                        'Có $3$ màu sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng '
                        'cộng có $3 + 2 + 1 = 6$ bạn.',
                        'Có $6$ màu sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng '
                        'cộng có $3 + 2 + 1 = 6$ bạn.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 64: Thu thập, phân loại, kiểm đếm số liệu: Có $3$ màu '
                        'sắc: màu Đỏ có $3$ bạn, màu Xanh có $2$ bạn, màu Vàng có $1$ bạn. Tổng cộng có $3 + '
                        '2 + 1 = 6$ bạn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Kiểm đếm số xe đi qua cổng trường trong $5$ phút: có $4$ ô tô, $9$ xe máy và $3$ xe đạp. '
                 'Hỏi có tất cả bao nhiêu chiếc xe đã đi qua cổng trường?',
            'answer': ['16'],
            'unit': None,
            'solution': 'Tổng số xe đi qua cổng trường là: $4 + 9 + 3 = 16$ (chiếc xe).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd13-thong-ke-xac-suat',
  'context_title': 'Chủ đề 13: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 2 · Chủ đề 13: Thu thập, phân loại, kiểm đếm số liệu; biểu đồ tranh; chắc chắn, có '
             'thể, không thể; thực hành trải nghiệm.',
  'title': 'Bài 65: Biểu đồ tranh',
  'icon': '🖼️',
  'description': 'Đọc, mô tả và nhận xét số liệu được biểu diễn trên biểu đồ tranh.',
  'requirements': ['Nhận biết được **biểu đồ tranh** (dùng các hình vẽ giống nhau để biểu thị số lượng đối '
                   'tượng trong từng nhóm).',
                   'Đọc được số liệu từ biểu đồ tranh (cả trường hợp $1$ hình ứng với $1$ đối tượng và $1$ '
                   'hình ứng với $2$ hoặc $5$ đối tượng).',
                   'Trả lời được các câu hỏi so sánh, tổng hợp từ biểu đồ tranh.'],
  'definition': '**Biểu đồ tranh** là bảng dùng các hình vẽ (biểu tượng) để thể hiện số lượng của từng loại '
                'đối tượng. Mỗi hình vẽ có thể biểu thị $1$ đối tượng hoặc một số đối tượng theo quy ước ghi '
                'chú ở biểu đồ.',
  'theory': '- **Cách đọc biểu đồ tranh:**\n'
            '  + Bước 1: Đọc kỹ dòng ghi chú xem **mỗi hình vẽ ứng với mấy đơn vị** ($1, 2$ hay $5$).\n'
            '  + Bước 2: Đếm số hình ở mỗi hàng (hoặc mỗi cột) rồi nhân với giá trị của $1$ hình.\n'
            '- **Ví dụ:** Nếu biểu đồ số sách đọc được có An: 📘📘📘, Bình: 📘📘📘📘📘, Chi: 📘📘 và ghi chú **mỗi 📘 '
            '$= 2$ quyển**, thì Bình đọc được $2 \\times 5 = 10$ quyển, Chi đọc được $2 \\times 2 = 4$ '
            'quyển.',
  'formulas': [{'category': 'Công thức đọc Biểu đồ tranh',
                'items': [{'name': 'Khi 1 hình = 1 đối tượng', 'formula': 'Số lượng $=$ Số hình đếm được'},
                          {'name': 'Khi 1 hình = k đối tượng',
                           'formula': 'Số lượng $= k \\times \\text{Số hình}$',
                           'note': 'Ví dụ: Mỗi hình $= 2$ quyển, có $5$ hình $\\Rightarrow 2 \\times 5 = 10$ '
                                   'quyển.'}]}],
  'example': 'Biểu đồ tranh trái cây yêu thích: Táo 🍎🍎🍎🍎🍎, Cam 🍊🍊🍊, Chuối 🍌🍌🍌🍌 (mỗi hình ứng với $1$ bạn). '
             'Loại quả nào được nhiều bạn thích nhất và nhiều hơn cam mấy bạn?',
  'example_answer': 'Táo có $5$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** được nhiều bạn thích nhất '
                    'và nhiều hơn cam là $5 - 3 = 2$ (bạn).',
  'real_life': 'Xem bảng thi đua bông hoa điểm tốt của các tổ, xem biểu đồ thời tiết (ngày nắng, ngày mưa) '
               'trong tháng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ dùng các hình vẽ (biểu tượng) để thể hiện số lượng đối tượng được gọi là gì?',
            'options': ['Bảng cửu chương', 'Biểu đồ tranh', 'Tia số', 'Tờ lịch tháng'],
            'answer': 1,
            'solution': 'Biểu đồ dùng hình vẽ để biểu thị số lượng gọi là biểu đồ tranh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trên biểu đồ tranh vật nuôi: Gà ⭐⭐⭐⭐, Vịt ⭐⭐, Ngan ⭐⭐⭐ (mỗi ⭐ $= 1$ con). Con vật nào có '
                 'ít nhất?',
            'options': ['Gà', 'Ngan', 'Vịt', 'Ba con bằng nhau'],
            'answer': 2,
            'solution': 'Vịt chỉ có $2$ ngôi sao (ứng với $2$ con) nên Vịt ít nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 65: Biểu đồ tranh**, quy tắc hoặc công thức nào sau đây xác định đúng **Khi 1 '
                 'hình = 1 đối tượng**?',
            'options': ['Số lượng $=$ Số hình đếm được (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Số lượng $=$ Số hình đếm được',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Số lượng $=$ Số hình đếm được',
                        'Số lượng $=$ Số hình đếm được'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 65: Biểu đồ tranh, **Khi 1 hình = 1 đối tượng** '
                        'được xác định bởi: Số lượng $=$ Số hình đếm được.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 65: Biểu đồ tranh**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Khi 1 hình = k đối tượng**?',
            'options': ['Số lượng $= k \\times \\text{Số hình}$',
                        'Số lượng $= k : \\text{Số hình}$',
                        'Đảo ngược vế của quy tắc: Số lượng $= k \\times \\text{Số hình}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Số lượng $= k \\times \\text{Số '
                        'hình}$'],
            'answer': 0,
            'solution': 'Trong Bài 65: Biểu đồ tranh, **Khi 1 hình = k đối tượng** có công thức/quy tắc là: '
                        'Số lượng $= k \\times \\text{Số hình}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biểu đồ tranh số sách đã đọc: An 📘📘📘, Bình 📘📘📘📘📘, Chi 📘📘 (biết mỗi 📘 $= 2$ quyển sách). '
                 'Hỏi Bình đọc nhiều hơn Chi bao nhiêu quyển sách?',
            'options': ['$3$ quyển', '$6$ quyển', '$10$ quyển', '$4$ quyển'],
            'answer': 1,
            'solution': 'Bình đọc $2 \\times 5 = 10$ quyển; Chi đọc $2 \\times 2 = 4$ quyển. Bình đọc nhiều '
                        'hơn Chi: $10 - 4 = 6$ (quyển).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 65: Biểu đồ tranh**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được **biểu đồ tranh** (dùng các hình vẽ giống nhau để biểu thị số lượng '
                        'đối tượng trong từng nhóm). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được **biểu đồ tranh** (dùng các hình vẽ giống '
                        'nhau để biểu thị số lượng đối tượng trong từng nhóm).',
                        'Nhận biết được **biểu đồ tranh** (dùng các hình vẽ giống nhau để biểu thị số lượng '
                        'đối tượng trong từng nhóm).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được **biểu đồ '
                        'tranh** (dùng các hình vẽ giống nhau để biểu thị số lượng đối tượng trong từng '
                        'nhóm).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 65: Biểu đồ tranh: Nhận biết được **biểu đồ tranh** '
                        '(dùng các hình vẽ giống nhau để biểu thị số lượng đối tượng trong từng nhóm).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trên biểu đồ tranh (khi mỗi hình vẽ đều biểu thị số lượng như nhau), hàng nào '
                 'có nhiều hình vẽ nhất thì loại đối tượng đó có số lượng nhiều nhất.”',
            'answer': True,
            'solution': 'Khi mỗi hình có cùng giá trị, số hình càng nhiều thì số lượng thực tế càng lớn. '
                        'Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 65: Biểu đồ tranh**, quy tắc **Khi 1 hình = 1 đối tượng** được xác định bởi Số '
                 'lượng $=$ Số hình đếm được và khi áp dụng cho ví dụ “Biểu đồ tranh trái cây yêu thích: Táo '
                 '🍎🍎🍎🍎🍎, Cam 🍊🍊🍊, Chuối 🍌🍌🍌🍌 (mỗi hình ứng với $1$ bạn). Loại quả nào được nhiều bạn thích '
                 'nhất và...” ta có lời giải: Táo có $5$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** '
                 'được nhiều bạn thích nhất và nhiều hơn cam là $5 - 3 = 2$ (bạn).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Khi 1 hình = 1 đối tượng** (Số lượng $=$ '
                        'Số hình đếm được) và lời giải ví dụ minh họa của Bài 65: Biểu đồ tranh.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 65: Biểu đồ tranh** để giải bài toán sau: Biểu đồ '
                 'tranh trái cây yêu thích: Táo 🍎🍎🍎🍎🍎, Cam 🍊🍊🍊, Chuối 🍌🍌🍌🍌 (mỗi hình ứng với $1$ bạn). Loại '
                 'quả nào được nhiều bạn thích nhất và nhiều hơn cam mấy bạn? Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Táo có $5$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** được nhiều bạn thích '
                        'nhất và nhiều hơn cam là $5 + 3 = 2$ (bạn).',
                        'Táo có $5$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** được nhiều bạn thích '
                        'nhất và nhiều hơn cam là $5 - 3 = 1$ (bạn).',
                        'Táo có $10$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** được nhiều bạn thích '
                        'nhất và nhiều hơn cam là $5 - 3 = 2$ (bạn).',
                        'Táo có $5$ bạn, Cam có $3$ bạn, Chuối có $4$ bạn. Vậy **Táo** được nhiều bạn thích '
                        'nhất và nhiều hơn cam là $5 - 3 = 2$ (bạn).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 65: Biểu đồ tranh: Táo có $5$ bạn, Cam có $3$ bạn, Chuối '
                        'có $4$ bạn. Vậy **Táo** được nhiều bạn thích nhất và nhiều hơn cam là $5 - 3 = 2$ '
                        '(bạn).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biểu đồ tranh số cây hoa trồng được của $3$ tổ: Tổ 1 có $4$ bông hoa, Tổ 2 có $3$ bông '
                 'hoa, Tổ 3 có $2$ bông hoa. Biết mỗi hình bông hoa trên biểu đồ ứng với $5$ cây hoa thật. '
                 'Hỏi Tổ 1 trồng được bao nhiêu cây hoa thật?',
            'answer': ['20'],
            'unit': None,
            'solution': 'Mỗi hình ứng với $5$ cây, Tổ 1 có $4$ hình nên trồng được: $5 \\times 4 = 20$ (cây '
                        'hoa).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd13-thong-ke-xac-suat',
  'context_title': 'Chủ đề 13: Làm quen với yếu tố thống kê, xác suất',
  'context': 'SGK Toán 2 · Chủ đề 13: Thu thập, phân loại, kiểm đếm số liệu; biểu đồ tranh; chắc chắn, có '
             'thể, không thể; thực hành trải nghiệm.',
  'title': 'Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ đề 13)',
  'icon': '🎲',
  'description': 'Sử dụng đúng các thuật ngữ chắc chắn, có thể, không thể để mô tả khả năng xảy ra của một '
                 'sự kiện.',
  'requirements': ['Hiểu và phân biệt được ba mức khả năng xảy ra của một sự kiện: **chắc chắn**, **có '
                   'thể**, **không thể**.',
                   'Sử dụng đúng ba từ này trong các trò chơi rút thẻ, lấy bóng trong hộp, gieo xúc xắc và '
                   'hiện tượng tự nhiên.',
                   'Vận dụng kiến thức của **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ '
                   'đề 13)** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- **Chắc chắn:** sự việc **luôn luôn xảy ra** trong mọi trường hợp.\n'
                '- **Có thể:** sự việc **có lúc xảy ra, có lúc không xảy ra** (chưa biết trước chắc chắn).\n'
                '- **Không thể:** sự việc **không bao giờ xảy ra**.',
  'theory': '- **Ví dụ với hộp bóng:**\n'
            '  + Hộp 1 **chỉ có bóng đỏ**: Lấy ngẫu nhiên $1$ quả bóng từ hộp 1 thì **chắc chắn** lấy được '
            'bóng đỏ, và **không thể** lấy được bóng xanh.\n'
            '  + Hộp 2 **có cả bóng đỏ và bóng xanh**: Lấy ngẫu nhiên $1$ quả bóng từ hộp 2 thì **có thể** '
            'lấy được bóng đỏ, cũng **có thể** lấy được bóng xanh.\n'
            '- **Ví dụ tự nhiên:** Mặt Trời mọc ở đằng đông là **chắc chắn**; Mặt Trời mọc ở đằng tây là '
            '**không thể**; chiều mai trời mưa là **có thể**.',
  'formulas': [{'category': 'Ba mức khả năng xảy ra (Xác suất sơ cấp)',
                'items': [{'name': 'Chắc chắn', 'formula': 'Luôn luôn xảy ra ($100\\%$ trường hợp đều đúng)'},
                          {'name': 'Có thể',
                           'formula': 'Có thể xảy ra hoặc không xảy ra (khi có từ $2$ khả năng trở lên)'},
                          {'name': 'Không thể', 'formula': 'Không bao giờ xảy ra ($0$ trường hợp)'}]}],
  'example': 'Trong hộp có $3$ viên bi đỏ và $2$ viên bi xanh. Không nhìn vào hộp, Nam lấy ra $1$ viên bi. '
             'Hãy điền từ “chắc chắn”, “có thể” hoặc “không thể” vào chỗ chấm:\n'
             'a) Nam … lấy được viên bi đỏ.\n'
             'b) Nam … lấy được viên bi vàng.',
  'example_answer': 'a) Nam **có thể** lấy được viên bi đỏ (vì trong hộp có cả bi đỏ và bi xanh).\n'
                    'b) Nam **không thể** lấy được viên bi vàng (vì trong hộp không có viên bi vàng nào).',
  'real_life': 'Dự đoán thời tiết trước khi ra ngoài (trời nhiều mây đen thì *có thể* sắp mưa nên mang theo '
               'áo mưa).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hộp chỉ có $5$ viên bi màu đỏ. Không nhìn vào hộp, lấy ra $1$ viên bi thì sự kiện '
                 '“lấy được viên bi màu đỏ” là:',
            'options': ['Có thể', 'Không thể', 'Chắc chắn', 'Không đoán được'],
            'answer': 2,
            'solution': 'Vì trong hộp toàn là bi đỏ nên lấy ra $1$ viên chắc chắn là bi đỏ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hộp chỉ có các quả bóng màu xanh. Lấy ra $1$ quả bóng từ hộp, sự kiện “lấy được quả '
                 'bóng màu vàng” là:',
            'options': ['Chắc chắn', 'Có thể', 'Luôn xảy ra', 'Không thể'],
            'answer': 3,
            'solution': 'Trong hộp không có bóng vàng nên không thể lấy được bóng vàng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ đề 13)**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Chắc chắn**?',
            'options': ['Luôn luôn xảy ra ($100\\%$ trường hợp đều đúng)',
                        'Luôn luôn xảy ra ($110\\%$ trường hợp đều đúng)',
                        'Luôn luôn xảy ra ($99\\%$ trường hợp đều đúng)',
                        'Luôn luôn xảy ra ($102\\%$ trường hợp đều đúng)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 66: Chắc chắn, có thể, không thể (Thực hành trải '
                        'nghiệm Chủ đề 13), **Chắc chắn** được xác định bởi: Luôn luôn xảy ra ($100\\%$ '
                        'trường hợp đều đúng).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ đề 13)**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Có thể**?',
            'options': ['Có thể xảy ra hoặc không xảy ra (khi có từ $3$ khả năng trở lên)',
                        'Có thể xảy ra hoặc không xảy ra (khi có từ $2$ khả năng trở lên)',
                        'Có thể xảy ra hoặc không xảy ra (khi có từ $1$ khả năng trở lên)',
                        'Có thể xảy ra hoặc không xảy ra (khi có từ $4$ khả năng trở lên)'],
            'answer': 1,
            'solution': 'Trong Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ đề 13), **Có '
                        'thể** có công thức/quy tắc là: Có thể xảy ra hoặc không xảy ra (khi có từ $2$ khả '
                        'năng trở lên).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong hộp có $3$ quả bóng đỏ và $2$ quả bóng xanh. Lấy ngẫu nhiên $1$ quả bóng. Câu nào '
                 'dưới đây đúng?',
            'options': ['Chắc chắn lấy được bóng đỏ',
                        'Không thể lấy được bóng xanh',
                        'Có thể lấy được bóng xanh',
                        'Chắc chắn lấy được bóng vàng'],
            'answer': 2,
            'solution': 'Vì hộp có cả bóng đỏ và bóng xanh nên khi lấy $1$ quả thì có thể lấy được bóng xanh '
                        '(hoặc bóng đỏ).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ '
                 'đề 13)**, nhận định nào sau đây là **chính xác**?',
            'options': ['Hiểu và phân biệt được ba mức khả năng xảy ra của một sự kiện: **chắc chắn**, **có '
                        'thể**, **không thể**. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu và phân biệt được ba mức khả năng xảy ra của một sự '
                        'kiện: **chắc chắn**, **có thể**, **không thể**.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu và phân biệt được ba mức '
                        'khả năng xảy ra của một sự kiện: **chắc chắn**, **có thể**, **không thể**.',
                        'Hiểu và phân biệt được ba mức khả năng xảy ra của một sự kiện: **chắc chắn**, **có '
                        'thể**, **không thể**.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 66: Chắc chắn, có thể, không thể (Thực hành trải '
                        'nghiệm Chủ đề 13): Hiểu và phân biệt được ba mức khả năng xảy ra của một sự kiện: '
                        '**chắc chắn**, **có thể**, **không thể**.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Gieo một con xúc xắc $1$ lần thì chắc chắn xuất hiện mặt $6$ chấm.”',
            'answer': False,
            'solution': 'Con xúc xắc có $6$ mặt (từ $1$ chấm đến $6$ chấm) nên khi gieo chỉ *có thể* ra mặt '
                        '$6$ chấm chứ không chắc chắn. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm Chủ đề 13)**, quy tắc '
                 '**Chắc chắn** được xác định bởi Luôn luôn xảy ra ($100\\%$ trường hợp đều đúng) và khi áp '
                 'dụng cho ví dụ “Trong hộp có $3$ viên bi đỏ và $2$ viên bi xanh. Không nhìn vào hộp, Nam '
                 'lấy ra $1$ viên bi. Hãy điền từ “chắc chắn”, “có thể” hoặc “kh...” ta có lời giải: a) Nam '
                 '**có thể** lấy được viên bi đỏ (vì trong hộp có cả bi đỏ và bi xanh). b) Nam **không thể** '
                 'lấy được viên bi vàng (vì trong hộp k.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Chắc chắn** (Luôn luôn xảy ra ($100\\%$ '
                        'trường hợp đều đúng)) và lời giải ví dụ minh họa của Bài 66: Chắc chắn, có thể, '
                        'không thể (Thực hành trải nghiệm Chủ đề 13).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 66: Chắc chắn, có thể, không thể (Thực hành trải '
                 'nghiệm Chủ đề 13)** để giải bài toán sau: Trong hộp có $3$ viên bi đỏ và $2$ viên bi xanh. '
                 'Không nhìn vào hộp, Nam lấy ra $1$ viên bi. Hãy điền từ “chắc chắn”, “có thể” hoặc “không '
                 'thể” vào chỗ chấm:\n'
                 'a) Nam … lấy được viên bi đỏ.\n'
                 'b) Nam … lấy được viên bi vàng. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) Nam **có thể** lấy được viên bi đỏ (vì trong hộp có cả bi đỏ và bi xanh). b) Nam '
                        '**không thể** lấy được viên bi vàng (vì trong hộp không có viên bi...',
                        'Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 66: Chắc chắn, có thể, không thể (Thực hành trải nghiệm '
                        'Chủ đề 13): a) Nam **có thể** lấy được viên bi đỏ (vì trong hộp có cả bi đỏ và bi '
                        'xanh).\n'
                        'b) Nam **không thể** lấy được viên bi vàng (vì trong hộp không có viên bi vàng '
                        'nào).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong túi có $4$ chiếc kẹo dâu và $3$ chiếc kẹo cam. Không nhìn vào túi, phải lấy ra ít '
                 'nhất bao nhiêu chiếc kẹo để CHẮC CHẮN có ít nhất $1$ chiếc kẹo dâu?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Trường hợp xấu nhất là lấy trúng hết $3$ chiếc kẹo cam trước, chiếc thứ $4$ lấy ra '
                        'chắc chắn sẽ là kẹo dâu. Vậy cần lấy ít nhất $3 + 1 = 4$ (chiếc kẹo).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd14-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 14: Ôn tập cuối năm',
  'context': 'SGK Toán 2 · Chủ đề 14: Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học '
             'và đo lường; kiểm đếm số liệu và lựa chọn khả năng.',
  'title': 'Bài 68: Ôn tập các số trong phạm vi 1000',
  'icon': '🔢',
  'description': 'Hệ thống lại cách đọc, viết, cấu tạo hàng trăm – chục – đơn vị, tia số và so sánh các số '
                 'trong phạm vi 1000.',
  'requirements': ['Đọc, viết, xác định số liền trước – liền sau và cấu tạo các số trong phạm vi $1000$.',
                   'Viết số thành tổng các trăm, chục, đơn vị và so sánh, sắp xếp các số có ba chữ số.',
                   'Vận dụng kiến thức của **Bài 68: Ôn tập các số trong phạm vi 1000** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Số có ba chữ số $\\overline{abc}$ gồm $a$ trăm, $b$ chục, $c$ đơn vị ($\\overline{abc} = '
                'a00 + b0 + c$). Khi so sánh các số trong phạm vi $1000$, ta so sánh số chữ số trước, sau đó '
                'so sánh từng hàng từ trái sang phải (Trăm $\\rightarrow$ Chục $\\rightarrow$ Đơn vị).',
  'theory': '- **Các số đặc biệt cần nhớ:**\n'
            '  + Số bé nhất có một chữ số là $0$; lớn nhất có một chữ số là $9$.\n'
            '  + Số bé nhất có hai chữ số là $10$; lớn nhất có hai chữ số là $99$.\n'
            '  + Số bé nhất có ba chữ số là $100$; lớn nhất có ba chữ số là $999$.\n'
            '  + Số bé nhất có ba chữ số giống nhau là $111$; lớn nhất có ba chữ số khác nhau là $987$.',
  'formulas': [{'category': 'Tổng hợp kiến thức Số trong phạm vi 1000',
                'items': [{'name': 'Cấu tạo thập phân',
                           'formula': '$10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn '
                                      '($1000$)'},
                          {'name': 'Phân tích thành tổng', 'formula': '$\\overline{abc} = a00 + b0 + c$'},
                          {'name': 'So sánh', 'formula': 'Trăm $\\rightarrow$ Chục $\\rightarrow$ Đơn vị'}]}],
  'example': 'Viết số lớn nhất có ba chữ số khác nhau thành tổng các trăm, chục, đơn vị.',
  'example_answer': 'Số lớn nhất có ba chữ số khác nhau là $987$. Ta có: $987 = 900 + 80 + 7$.',
  'real_life': 'Đọc các số liệu thống kê, bảng giá, số thứ tự trong phạm vi $1000$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số “chín trăm mười lăm” được viết là:',
            'options': ['$951$', '$9015$', '$905$', '$915$'],
            'answer': 3,
            'solution': 'Chín trăm ($900$), mười ($10$), lăm ($5$) viết là $915$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền trước của số $1000$ là số nào?',
            'options': ['$999$', '$900$', '$990$', '$989$'],
            'answer': 0,
            'solution': 'Số liền trước của $1000$ là $1000 - 1 = 999$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 68: Ôn tập các số trong phạm vi 1000**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Cấu tạo thập phân**?',
            'options': ['$11$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$)',
                        '$10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$)',
                        '$10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($999$)',
                        '$20$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 68: Ôn tập các số trong phạm vi 1000, **Cấu tạo '
                        'thập phân** được xác định bởi: $10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ '
                        'trăm $= 1$ nghìn ($1000$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 68: Ôn tập các số trong phạm vi 1000**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Phân tích thành tổng**?',
            'options': ['$\\overline{abc} = a00 - b0 + c$',
                        'Đảo ngược vế của quy tắc: $\\overline{abc} = a00 + b0 + c$',
                        '$\\overline{abc} = a00 + b0 + c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{abc} = a00 + b0 + '
                        'c$'],
            'answer': 2,
            'solution': 'Trong Bài 68: Ôn tập các số trong phạm vi 1000, **Phân tích thành tổng** có công '
                        'thức/quy tắc là: $\\overline{abc} = a00 + b0 + c$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Các số $385, 538, 358, 835$ được sắp xếp theo thứ tự từ bé đến lớn là:',
            'options': ['$385, 358, 538, 835$',
                        '$835, 538, 385, 358$',
                        '$358, 538, 385, 835$',
                        '$358, 385, 538, 835$'],
            'answer': 3,
            'solution': 'So sánh từ hàng trăm đến hàng chục: $358 < 385 < 538 < 835$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 68: Ôn tập các số trong phạm vi 1000**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Đọc, viết, xác định số liền trước – liền sau và cấu tạo các số trong phạm vi '
                        '$1000$.',
                        'Đọc, viết, xác định số liền trước – liền sau và cấu tạo các số trong phạm vi '
                        '$1010$.',
                        'Đọc, viết, xác định số liền trước – liền sau và cấu tạo các số trong phạm vi $999$.',
                        'Đọc, viết, xác định số liền trước – liền sau và cấu tạo các số trong phạm vi '
                        '$1002$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 68: Ôn tập các số trong phạm vi 1000: Đọc, viết, xác '
                        'định số liền trước – liền sau và cấu tạo các số trong phạm vi $1000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $504$ gồm $5$ trăm và $4$ chục.”',
            'answer': False,
            'solution': 'Số $504$ gồm $5$ trăm, $0$ chục và $4$ đơn vị (không phải $4$ chục). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 68: Ôn tập các số trong phạm vi 1000**, quy tắc **Cấu tạo thập phân** được xác '
                 'định bởi $10$ đơn vị $= 1$ chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$) và '
                 'khi áp dụng cho ví dụ “Viết số lớn nhất có ba chữ số khác nhau thành tổng các trăm, chục, '
                 'đơn vị.” ta có lời giải: Số lớn nhất có ba chữ số khác nhau là $987$. Ta có: $987 = 900 + '
                 '80 + 7$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cấu tạo thập phân** ($10$ đơn vị $= 1$ '
                        'chục; $10$ chục $= 1$ trăm; $10$ trăm $= 1$ nghìn ($1000$)) và lời giải ví dụ minh '
                        'họa của Bài 68: Ôn tập các số trong phạm vi 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 68: Ôn tập các số trong phạm vi 1000** để giải bài '
                 'toán sau: Viết số lớn nhất có ba chữ số khác nhau thành tổng các trăm, chục, đơn vị. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số lớn nhất có ba chữ số khác nhau là $987$. Ta có: $987 = 900 - 80 + 7$.',
                        'Số lớn nhất có ba chữ số khác nhau là $987$. Ta có: $987 = 900 + 80 + 7$.',
                        'Số lớn nhất có ba chữ số khác nhau là $987$. Ta có: $987 = 900 + 80 + 6$.',
                        'Số lớn nhất có ba chữ số khác nhau là $989$. Ta có: $987 = 900 + 80 + 7$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 68: Ôn tập các số trong phạm vi 1000: Số lớn nhất có ba '
                        'chữ số khác nhau là $987$. Ta có: $987 = 900 + 80 + 7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số lớn nhất có ba chữ số khác nhau là số nào?',
            'answer': ['987'],
            'unit': None,
            'solution': 'Chọn chữ số hàng trăm lớn nhất là $9$, hàng chục lớn nhất khác $9$ là $8$, hàng đơn '
                        'vị lớn nhất khác $9$ và $8$ là $7$. Vậy số đó là $987$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd14-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 14: Ôn tập cuối năm',
  'context': 'SGK Toán 2 · Chủ đề 14: Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học '
             'và đo lường; kiểm đếm số liệu và lựa chọn khả năng.',
  'title': 'Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000',
  'icon': '🧮',
  'description': 'Củng cố kỹ năng cộng, trừ (không nhớ và có nhớ) trong phạm vi 100 và 1000; giải bài toán '
                 'có lời văn.',
  'requirements': ['Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi $100$ và '
                   '$1000$.',
                   'Vận dụng thành phần phép tính (số hạng, tổng; số bị trừ, số trừ, hiệu) và giải bài toán '
                   'thực tế.',
                   'Vận dụng kiến thức của **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000** '
                   'để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': '- Khi đặt tính cộng hoặc trừ trong phạm vi $1000$, các chữ số cùng một hàng phải viết '
                '**thẳng cột** với nhau.\n'
                '- Thực hiện tính **từ phải sang trái** (Đơn vị $\\rightarrow$ Chục $\\rightarrow$ Trăm) và '
                'thực hiện nhớ (hoặc trả $1$) đúng quy tắc.',
  'theory': '- **Kiểm tra phép cộng và phép trừ:**\n'
            '  + $\\text{Tổng} - \\text{Số hạng này} = \\text{Số hạng kia}$.\n'
            '  + $\\text{Hiệu} + \\text{Số trừ} = \\text{Số bị trừ}$.\n'
            '- **Giải toán có lời văn:** Đọc kỹ xem đại lượng cần tìm là đại lượng lớn hơn (cộng) hay đại '
            'lượng bé hơn (trừ), hay tìm tổng/phần còn lại.',
  'formulas': [{'category': 'Ôn tập Cộng – Trừ trong phạm vi 100 và 1000',
                'items': [{'name': 'Thành phần phép cộng',
                           'formula': '$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$'},
                          {'name': 'Thành phần phép trừ',
                           'formula': '$\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$'},
                          {'name': 'Thứ tự dãy tính', 'formula': 'Tính lần lượt từ trái sang phải'}]}],
  'example': 'Đặt tính rồi tính: a) $458 + 271$; b) $642 - 129$.',
  'example_answer': 'a) $8 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + 271 = '
                    '729$.\n'
                    'b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 \\Rightarrow 642 - 129 = '
                    '513$.',
  'real_life': 'Tính toán thu chi, kiểm kê số lượng hàng hóa, sách vở trong thư viện.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $527 + 246$ là:',
            'options': ['$773$', '$763$', '$783$', '$281$'],
            'answer': 0,
            'solution': 'Đơn vị: $7 + 6 = 13$ viết $3$ nhớ $1$; chục: $2 + 4 + 1 = 7$; trăm: $5 + 2 = 7$. '
                        'Vậy $527 + 246 = 773$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $654 - 238$ là:',
            'options': ['$426$', '$416$', '$316$', '$424$'],
            'answer': 1,
            'solution': 'Đơn vị: $14 - 8 = 6$ nhớ $1$; chục: $3 + 1 = 4, 5 - 4 = 1$; trăm: $6 - 2 = 4$. Vậy '
                        '$654 - 238 = 416$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Thành phần phép cộng**?',
            'options': ['$\\text{Số hạng} - \\text{Số hạng} = \\text{Tổng}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$',
                        '$\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số hạng} + \\text{Số '
                        'hạng} = \\text{Tổng}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 '
                        'và 1000, **Thành phần phép cộng** được xác định bởi: $\\text{Số hạng} + \\text{Số '
                        'hạng} = \\text{Tổng}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000**, biểu thức hoặc '
                 'quy tắc nào dưới đây biểu diễn đúng **Thành phần phép trừ**?',
            'options': ['$\\text{Số bị trừ} + \\text{Số trừ} = \\text{Hiệu}$',
                        'Đảo ngược vế của quy tắc: $\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Số bị trừ} - \\text{Số '
                        'trừ} = \\text{Hiệu}$',
                        '$\\text{Số bị trừ} - \\text{Số trừ} = \\text{Hiệu}$'],
            'answer': 3,
            'solution': 'Trong Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000, **Thành phần '
                        'phép trừ** có công thức/quy tắc là: $\\text{Số bị trừ} - \\text{Số trừ} = '
                        '\\text{Hiệu}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tìm hiệu của số lớn nhất có ba chữ số và số tròn trăm bé nhất.',
            'options': ['$899$', '$800$', '$989$', '$900$'],
            'answer': 0,
            'solution': 'Số lớn nhất có ba chữ số là $999$, số tròn trăm bé nhất là $100$. Hiệu là: $999 - '
                        '100 = 899$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi $110$ '
                        'và $1000$.',
                        'Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi $100$ '
                        'và $1000$.',
                        'Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi $100$ '
                        'và $999$.',
                        'Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi $102$ '
                        'và $1000$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và '
                        '1000: Tính nhẩm và đặt tính rồi tính thành thạo phép cộng, phép trừ trong phạm vi '
                        '$100$ và $1000$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$345 + 155 = 500$.”',
            'answer': True,
            'solution': 'Đơn vị: $5 + 5 = 10$ viết $0$ nhớ $1$; chục: $4 + 5 + 1 = 10$ viết $0$ nhớ $1$; '
                        'trăm: $3 + 1 + 1 = 5$. Kết quả $500$ là Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và 1000**, quy tắc **Thành '
                 'phần phép cộng** được xác định bởi $\\text{Số hạng} + \\text{Số hạng} = \\text{Tổng}$ và '
                 'khi áp dụng cho ví dụ “Đặt tính rồi tính: a) $458 + 271$; b) $642 - 129$.” ta có lời giải: '
                 'a) $8 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + 271 = '
                 '729$. b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thành phần phép cộng** ($\\text{Số hạng} '
                        '+ \\text{Số hạng} = \\text{Tổng}$) và lời giải ví dụ minh họa của Bài 69: Ôn tập '
                        'phép cộng, phép trừ trong phạm vi 100 và 1000.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và '
                 '1000** để giải bài toán sau: Đặt tính rồi tính: a) $458 + 271$; b) $642 - 129$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $8 - 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + '
                        '271 = 729$. b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 '
                        '\\Rightarrow 642 - 129 = 513$...',
                        'a) $8 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + '
                        '271 = 729$. b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 '
                        '\\Rightarrow 642 - 129 = 512$...',
                        'a) $8 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + '
                        '271 = 729$. b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 '
                        '\\Rightarrow 642 - 129 = 513$...',
                        'a) $16 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow 458 + '
                        '271 = 729$. b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 '
                        '\\Rightarrow 642 - 129 = 513$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 69: Ôn tập phép cộng, phép trừ trong phạm vi 100 và '
                        '1000: a) $8 + 1 = 9$; $5 + 7 = 12$ viết $2$ nhớ $1$; $4 + 2 + 1 = 7 \\Rightarrow '
                        '458 + 271 = 729$.\n'
                        'b) $12 - 9 = 3$ nhớ $1$; $2 + 1 = 3, 4 - 3 = 1$; $6 - 1 = 5 \\Rightarrow 642 - 129 '
                        '= 513$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Con trâu cân nặng $350\\text{ kg}$, con bò nhẹ hơn con trâu $125\\text{ kg}$. Hỏi con bò '
                 'cân nặng bao nhiêu ki-lô-gam?',
            'answer': ['225', '225kg', '225 kg'],
            'unit': None,
            'solution': 'Cân nặng của con bò là: $350 - 125 = 225$ ($\\text{kg}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd14-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 14: Ôn tập cuối năm',
  'context': 'SGK Toán 2 · Chủ đề 14: Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học '
             'và đo lường; kiểm đếm số liệu và lựa chọn khả năng.',
  'title': 'Bài 71: Ôn tập phép nhân, phép chia',
  'icon': '✖️',
  'description': 'Hệ thống lại bảng nhân 2, 5 và bảng chia 2, 5; giải bài toán thực tế về nhân, chia.',
  'requirements': ['Thuộc lòng và tính nhẩm nhanh bảng nhân $2$, bảng nhân $5$, bảng chia $2$, bảng chia '
                   '$5$.',
                   'Nắm chắc tên gọi thừa số – tích, số bị chia – số chia – thương và mối quan hệ ngược nhau '
                   'giữa nhân và chia.',
                   'Giải được bài toán có lời văn bằng một phép nhân hoặc một phép chia.'],
  'definition': '- **Phép nhân:** $\\text{Thừa số} \\times \\text{Thừa số} = \\text{Tích}$.\n'
                '- **Phép chia:** $\\text{Số bị chia} : \\text{Số chia} = \\text{Thương}$.\n'
                '- Nếu $a \\times b = c$ thì $c : a = b$ và $c : b = a$.',
  'theory': '- Khi tính dãy tính có phép nhân (hoặc phép chia) ở bên trái và phép cộng (hoặc phép trừ) ở bên '
            'phải như $5 \\times 6 + 15$, ta tính từ trái sang phải: $5 \\times 6 = 30$, rồi $30 + 15 = 45$.',
  'formulas': [{'category': 'Tổng hợp Bảng nhân 2, 5 và Bảng chia 2, 5',
                'items': [{'name': 'Bảng 2',
                           'formula': '$2 \\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 '
                                      '\\dots 20 : 2 = 10$'},
                          {'name': 'Bảng 5',
                           'formula': '$5 \\times 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 '
                                      '\\dots 50 : 5 = 10$'}]}],
  'example': 'Mỗi bàn học có $2$ bạn ngồi. Hỏi $8$ bàn học như thế có tất cả bao nhiêu bạn ngồi?',
  'example_answer': 'Số bạn ngồi ở $8$ bàn học là:\n$2 \\times 8 = 16$ (bạn)\nĐáp số: $16$ bạn.',
  'real_life': 'Tính tổng số lượng đồ vật đóng theo hộp $2$ chiếc hoặc $5$ chiếc, chia đều phần thưởng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $5 \\times 8$ là:',
            'options': ['$13$', '$40$', '$35$', '$45$'],
            'answer': 1,
            'solution': 'Theo bảng nhân $5$, ta có $5 \\times 8 = 40$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $18 : 2$ là:',
            'options': ['$8$', '$16$', '$9$', '$20$'],
            'answer': 2,
            'solution': 'Vì $2 \\times 9 = 18$ nên $18 : 2 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 71: Ôn tập phép nhân, phép chia**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Bảng 2**?',
            'options': ['$2 : 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 = 10$',
                        '$2 \\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 '
                        '= 9$',
                        '$4 \\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 '
                        '= 10$',
                        '$2 \\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 '
                        '= 10$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 71: Ôn tập phép nhân, phép chia, **Bảng 2** được '
                        'xác định bởi: $2 \\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 '
                        '\\dots 20 : 2 = 10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 71: Ôn tập phép nhân, phép chia**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Bảng 5**?',
            'options': ['$5 \\times 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 \\dots 50 : 5 '
                        '= 10$',
                        '$5 : 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 \\dots 50 : 5 = 10$',
                        '$5 \\times 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 \\dots 50 : 5 '
                        '= 9$',
                        '$10 \\times 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 \\dots 50 : 5 '
                        '= 10$'],
            'answer': 0,
            'solution': 'Trong Bài 71: Ôn tập phép nhân, phép chia, **Bảng 5** có công thức/quy tắc là: $5 '
                        '\\times 1 = 5 \\dots 5 \\times 10 = 50 \\Leftrightarrow 5 : 5 = 1 \\dots 50 : 5 = '
                        '10$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $5 \\times 7 - 15$ là:',
            'options': ['$25$', '$20$', '$50$', '$35$'],
            'answer': 1,
            'solution': 'Ta có $5 \\times 7 = 35$, sau đó lấy $35 - 15 = 20$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 71: Ôn tập phép nhân, phép chia**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Thuộc lòng và tính nhẩm nhanh bảng nhân $3$, bảng nhân $5$, bảng chia $2$, bảng '
                        'chia $5$.',
                        'Thuộc lòng và tính nhẩm nhanh bảng nhân $2$, bảng nhân $5$, bảng chia $2$, bảng '
                        'chia $4$.',
                        'Thuộc lòng và tính nhẩm nhanh bảng nhân $2$, bảng nhân $5$, bảng chia $2$, bảng '
                        'chia $5$.',
                        'Thuộc lòng và tính nhẩm nhanh bảng nhân $4$, bảng nhân $5$, bảng chia $2$, bảng '
                        'chia $5$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 71: Ôn tập phép nhân, phép chia: Thuộc lòng và tính '
                        'nhẩm nhanh bảng nhân $2$, bảng nhân $5$, bảng chia $2$, bảng chia $5$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Tích của $2$ và $10$ bằng thương của $50$ và $5$.”',
            'answer': False,
            'solution': 'Tích của $2$ và $10$ là $2 \\times 10 = 20$, còn thương của $50$ và $5$ là $50 : 5 '
                        '= 10$. Vì $20 \\neq 10$ nên nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 71: Ôn tập phép nhân, phép chia**, quy tắc **Bảng 2** được xác định bởi $2 '
                 '\\times 1 = 2 \\dots 2 \\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 = 10$ và '
                 'khi áp dụng cho ví dụ “Mỗi bàn học có $2$ bạn ngồi. Hỏi $8$ bàn học như thế có tất cả bao '
                 'nhiêu bạn ngồi?” ta có lời giải: Số bạn ngồi ở $8$ bàn học là: $2 \\times 8 = 16$ (bạn) '
                 'Đáp số: $16$ bạn.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Bảng 2** ($2 \\times 1 = 2 \\dots 2 '
                        '\\times 10 = 20 \\Leftrightarrow 2 : 2 = 1 \\dots 20 : 2 = 10$) và lời giải ví dụ '
                        'minh họa của Bài 71: Ôn tập phép nhân, phép chia.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 71: Ôn tập phép nhân, phép chia** để giải bài toán '
                 'sau: Mỗi bàn học có $2$ bạn ngồi. Hỏi $8$ bàn học như thế có tất cả bao nhiêu bạn ngồi? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số bạn ngồi ở $8$ bàn học là: $2 : 8 = 16$ (bạn) Đáp số: $16$ bạn.',
                        'Số bạn ngồi ở $8$ bàn học là: $2 \\times 8 = 16$ (bạn) Đáp số: $15$ bạn.',
                        'Số bạn ngồi ở $16$ bàn học là: $2 \\times 8 = 16$ (bạn) Đáp số: $16$ bạn.',
                        'Số bạn ngồi ở $8$ bàn học là: $2 \\times 8 = 16$ (bạn) Đáp số: $16$ bạn.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 71: Ôn tập phép nhân, phép chia: Số bạn ngồi ở $8$ bàn '
                        'học là:\n'
                        '$2 \\times 8 = 16$ (bạn)\n'
                        'Đáp số: $16$ bạn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cô giáo có $35$ quyển truyện, cô thưởng đều cho mỗi bạn $5$ quyển truyện. Hỏi có bao nhiêu '
                 'bạn được cô thưởng truyện?',
            'answer': ['7'],
            'unit': None,
            'solution': 'Số bạn được thưởng truyện là: $35 : 5 = 7$ (bạn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd14-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 14: Ôn tập cuối năm',
  'context': 'SGK Toán 2 · Chủ đề 14: Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học '
             'và đo lường; kiểm đếm số liệu và lựa chọn khả năng.',
  'title': 'Bài 72: Ôn tập hình học và đo lường',
  'icon': '📐',
  'description': 'Ôn tập đường gấp khúc, hình tứ giác, khối trụ – khối cầu và các đơn vị đo độ dài, khối '
                 'lượng, dung tích, thời gian, tiền tệ.',
  'requirements': ['Nhận diện đúng các hình phẳng (tam giác, tứ giác, đường gấp khúc) và hình khối (khối lập '
                   'phương, khối hộp chữ nhật, khối trụ, khối cầu).',
                   'Tính được độ dài đường gấp khúc; đổi và tính toán với các đơn vị $\\text{cm}, '
                   '\\text{dm}, \\text{m}, \\text{km}, \\text{kg}, \\text{l}$, giờ – phút, ngày – tháng, '
                   'đồng.',
                   'Vận dụng kiến thức của **Bài 72: Ôn tập hình học và đo lường** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Tổng hợp các mối quan hệ đo lường lớp 2:\n'
                '- **Độ dài:** $1\\text{ km} = 1000\\text{ m}$; $1\\text{ m} = 10\\text{ dm} = 100\\text{ '
                'cm}$; $1\\text{ dm} = 10\\text{ cm}$.\n'
                '- **Thời gian:** $1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút; $1$ tuần lễ $= 7$ ngày.',
  'theory': '- **Đường gấp khúc:** Muốn tính độ dài đường gấp khúc gồm các đoạn thẳng có cùng độ dài (ví dụ '
            '$3$ đoạn, mỗi đoạn dài $5\\text{ cm}$), ta có thể dùng phép cộng $5 + 5 + 5 = 15\\text{ cm}$ '
            'hoặc dùng phép nhân $5 \\times 3 = 15\\text{ cm}$.\n'
            '- Khi thực hiện phép tính với các số đo khác đơn vị (như $\\text{m}$ và $\\text{dm}$), luôn đổi '
            'về cùng đơn vị trước khi tính.',
  'formulas': [{'category': 'Tổng hợp Hình học và Đo lường lớp 2',
                'items': [{'name': 'Đường gấp khúc n đoạn bằng nhau',
                           'formula': 'Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$',
                           'note': 'Ví dụ: $3$ đoạn mỗi đoạn $5\\text{ cm} \\Rightarrow 5 \\times 3 = '
                                   '15\\text{ cm}$.'},
                          {'name': 'Quy đổi độ dài',
                           'formula': '$1\\text{ km} = 1000\\text{ m};\\ 1\\text{ m} = 10\\text{ dm} = '
                                      '100\\text{ cm};\\ 1\\text{ dm} = 10\\text{ cm}$'},
                          {'name': 'Quy đổi thời gian',
                           'formula': '$1$ ngày $= 24$ giờ; $1$ giờ $= 60$ phút'}]}],
  'example': 'Một đường gấp khúc gồm $4$ đoạn thẳng, mỗi đoạn thẳng đều dài $5\\text{ cm}$. Tính độ dài '
             'đường gấp khúc đó.',
  'example_answer': 'Độ dài đường gấp khúc đó là: $5 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 + 5 + 5 + 5 = '
                    '20\\text{ cm}$).',
  'real_life': 'Đo đạc kích thước đồ vật, đọc giờ tàu chạy, tính tiền mua hàng trong đời sống.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đường gấp khúc gồm $3$ đoạn thẳng, mỗi đoạn dài $5\\text{ cm}$. Độ dài đường gấp khúc đó '
                 'là:',
            'options': ['$8\\text{ cm}$', '$10\\text{ cm}$', '$15\\text{ cm}$', '$53\\text{ cm}$'],
            'answer': 2,
            'solution': 'Ta có $5 \\times 3 = 15$ ($\\text{cm}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số thích hợp điền vào chỗ chấm $1\\text{ km} = \\dots\\text{ m}$ là:',
            'options': ['$10$', '$100$', '$1$', '$1000$'],
            'answer': 3,
            'solution': 'Ta có $1\\text{ km} = 1000\\text{ m}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 72: Ôn tập hình học và đo lường**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Đường gấp khúc n đoạn bằng nhau**?',
            'options': ['Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$',
                        'Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a : n$',
                        'Đảo ngược vế của quy tắc: Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nếu mỗi đoạn dài $a$ thì tổng '
                        'độ dài là $a \\times n$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 72: Ôn tập hình học và đo lường, **Đường gấp khúc '
                        'n đoạn bằng nhau** được xác định bởi: Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a '
                        '\\times n$. (Ví dụ: $3$ đoạn mỗi đoạn $5\\text{ cm} \\Rightarrow 5 \\times 3 = '
                        '15\\text{ cm}$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 72: Ôn tập hình học và đo lường**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Quy đổi độ dài**?',
            'options': ['$2\\text{ km} = 1000\\text{ m};\\ 1\\text{ m} = 10\\text{ dm} = 100\\text{ cm};\\ '
                        '1\\text{ dm} = 10\\text{ cm}$',
                        '$1\\text{ km} = 1000\\text{ m};\\ 1\\text{ m} = 10\\text{ dm} = 100\\text{ cm};\\ '
                        '1\\text{ dm} = 10\\text{ cm}$',
                        '$1\\text{ km} = 1000\\text{ m};\\ 1\\text{ m} = 10\\text{ dm} = 100\\text{ cm};\\ '
                        '1\\text{ dm} = 9\\text{ cm}$',
                        'Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$'],
            'answer': 1,
            'solution': 'Trong Bài 72: Ôn tập hình học và đo lường, **Quy đổi độ dài** có công thức/quy tắc '
                        'là: $1\\text{ km} = 1000\\text{ m};\\ 1\\text{ m} = 10\\text{ dm} = 100\\text{ '
                        'cm};\\ 1\\text{ dm} = 10\\text{ cm}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bộ phim bắt đầu chiếu lúc $20$ giờ và kết thúc lúc $21$ giờ $30$ phút. Vậy bộ phim bắt đầu '
                 'lúc mấy giờ tối?',
            'options': ['$6$ giờ tối', '$7$ giờ tối', '$8$ giờ tối', '$9$ giờ tối'],
            'answer': 2,
            'solution': 'Ta lấy $20 - 12 = 8$, vậy $20$ giờ là $8$ giờ tối.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 72: Ôn tập hình học và đo lường**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận diện đúng các hình phẳng (tam giác, tứ giác, đường gấp khúc) và hình khối '
                        '(khối lập phương, khối hộp chữ nhật, khối trụ, khối cầu). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận diện đúng các hình phẳng (tam giác, tứ giác, đường '
                        'gấp khúc) và hình khối (khối lập phương, khối hộp chữ nhật, khối trụ, khối cầu).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận diện đúng các hình phẳng '
                        '(tam giác, tứ giác, đường gấp khúc) và hình khối (khối lập phương, khối hộp chữ '
                        'nhật, khối trụ, khối cầu).',
                        'Nhận diện đúng các hình phẳng (tam giác, tứ giác, đường gấp khúc) và hình khối '
                        '(khối lập phương, khối hộp chữ nhật, khối trụ, khối cầu).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 72: Ôn tập hình học và đo lường: Nhận diện đúng các '
                        'hình phẳng (tam giác, tứ giác, đường gấp khúc) và hình khối (khối lập phương, khối '
                        'hộp chữ nhật, khối trụ, khối cầu).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Hình tứ giác có $4$ đỉnh và $4$ cạnh, còn khối cầu không có mặt phẳng nào.”',
            'answer': True,
            'solution': 'Hình tứ giác là hình phẳng có $4$ đỉnh, $4$ cạnh; khối cầu tròn đều mọi phía và '
                        'không có mặt phẳng nào. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 72: Ôn tập hình học và đo lường**, quy tắc **Đường gấp khúc n đoạn bằng nhau** '
                 'được xác định bởi Nếu mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$ và khi áp dụng cho '
                 'ví dụ “Một đường gấp khúc gồm $4$ đoạn thẳng, mỗi đoạn thẳng đều dài $5\\text{ cm}$. Tính '
                 'độ dài đường gấp khúc đó.” ta có lời giải: Độ dài đường gấp khúc đó là: $5 \\times 4 = 20$ '
                 '($\\text{cm}$) (hoặc $5 + 5 + 5 + 5 = 20\\text{ cm}$).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đường gấp khúc n đoạn bằng nhau** (Nếu '
                        'mỗi đoạn dài $a$ thì tổng độ dài là $a \\times n$) và lời giải ví dụ minh họa của '
                        'Bài 72: Ôn tập hình học và đo lường.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 72: Ôn tập hình học và đo lường** để giải bài toán '
                 'sau: Một đường gấp khúc gồm $4$ đoạn thẳng, mỗi đoạn thẳng đều dài $5\\text{ cm}$. Tính độ '
                 'dài đường gấp khúc đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Độ dài đường gấp khúc đó là: $5 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 + 5 + 5 + 5 '
                        '= 20\\text{ cm}$).',
                        'Độ dài đường gấp khúc đó là: $5 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 - 5 + 5 + 5 '
                        '= 20\\text{ cm}$).',
                        'Độ dài đường gấp khúc đó là: $5 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 + 5 + 5 + 5 '
                        '= 19\\text{ cm}$).',
                        'Độ dài đường gấp khúc đó là: $10 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 + 5 + 5 + '
                        '5 = 20\\text{ cm}$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 72: Ôn tập hình học và đo lường: Độ dài đường gấp khúc '
                        'đó là: $5 \\times 4 = 20$ ($\\text{cm}$) (hoặc $5 + 5 + 5 + 5 = 20\\text{ cm}$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cây tre cao $5\\text{ m}$, người ta chặt bớt phần ngọn dài $15\\text{ dm}$. Hỏi phần '
                 'thân tre còn lại dài bao nhiêu đề-xi-mét?',
            'answer': ['35', '35dm', '35 dm'],
            'unit': None,
            'solution': 'Đổi $5\\text{ m} = 50\\text{ dm}$. Phần thân tre còn lại dài là: $50 - 15 = 35$ '
                        '($\\text{dm}$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l2-cd14-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 14: Ôn tập cuối năm',
  'context': 'SGK Toán 2 · Chủ đề 14: Ôn tập các số trong phạm vi 1000; phép cộng, trừ, nhân, chia; hình học '
             'và đo lường; kiểm đếm số liệu và lựa chọn khả năng.',
  'title': 'Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung cuối năm)',
  'icon': '🏁',
  'description': 'Ôn tập đọc biểu đồ tranh, mô tả khả năng chắc chắn – có thể – không thể và giải toán tổng '
                 'hợp cuối năm.',
  'requirements': ['Đọc, phân tích và trả lời đúng các câu hỏi từ bảng kiểm đếm và biểu đồ tranh.',
                   'Xác định đúng khả năng xảy ra của sự kiện bằng các từ **chắc chắn**, **có thể**, **không '
                   'thể**.',
                   'Giải quyết các bài toán thực tiễn tổng hợp hoàn chỉnh chương trình Toán lớp 2.'],
  'definition': 'Tổng kết yếu tố Thống kê – Xác suất và giải toán cuối năm:\n'
                '- **Biểu đồ tranh:** Đếm số biểu tượng và nhân với giá trị của $1$ biểu tượng.\n'
                '- **Khả năng xảy ra:** Chắc chắn (luôn đúng), Có thể (chưa biết chắc), Không thể (không bao '
                'giờ xảy ra).',
  'theory': '- Khi đọc biểu đồ tranh, ta có thể tìm được: nhóm nhiều nhất, nhóm ít nhất, tổng số lượng các '
            'nhóm và phần chênh lệch giữa hai nhóm.\n'
            '- Hoàn thành chương trình Toán 2 giúp em nắm vững các số đến $1000$, bốn phép tính ($+, -, '
            '\\times, :$), hình học, đo lường và thống kê cơ bản để sẵn sàng bước vào lớp 3.',
  'formulas': [{'category': 'Tổng hợp Thống kê – Xác suất và Giải toán',
                'items': [{'name': 'Chênh lệch trên biểu đồ',
                           'formula': '$\\text{Chênh lệch} = \\text{Số lượng nhiều hơn} - \\text{Số lượng ít '
                                      'hơn}$'},
                          {'name': 'Tổng số liệu',
                           'formula': '$\\text{Tổng} = \\text{Nhóm 1} + \\text{Nhóm 2} + \\text{Nhóm 3} + '
                                      '\\dots$'}]}],
  'example': 'Trong hộp có $5$ tấm thẻ ghi các số $2, 4, 6, 8, 10$. Rút ngẫu nhiên $1$ tấm thẻ. Sự kiện “rút '
             'được tấm thẻ ghi số lớn hơn $1$” là chắc chắn, có thể hay không thể?',
  'example_answer': 'Vì cả $5$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ nên sự kiện rút được tấm thẻ ghi số lớn '
                    'hơn $1$ là **chắc chắn**.',
  'real_life': 'Tổng kết số điểm tốt, số quyển sách đọc được trong cả năm học lớp 2 và lập kế hoạch vui hè.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hộp có các tấm thẻ ghi số $10, 20, 30, 40$. Không nhìn vào hộp, rút ra $1$ tấm thẻ '
                 'thì tấm thẻ đó:',
            'options': ['Không thể ghi số tròn chục',
                        'Chắc chắn ghi số $50$',
                        'Có thể ghi số $15$',
                        'Chắc chắn ghi số tròn chục'],
            'answer': 3,
            'solution': 'Tất cả các số $10, 20, 30, 40$ trong hộp đều là số tròn chục, nên rút ra $1$ thẻ '
                        'chắc chắn ghi số tròn chục.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu đồ tranh số cây trồng được của ba lớp: Lớp 2A có $5$ hình cây, Lớp 2B có $6$ hình '
                 'cây, Lớp 2C có $4$ hình cây (mỗi hình $= 1$ cây). Cả ba lớp trồng được tất cả:',
            'options': ['$15$ cây', '$11$ cây', '$14$ cây', '$16$ cây'],
            'answer': 0,
            'solution': 'Tổng số cây cả ba lớp trồng được là: $5 + 6 + 4 = 15$ (cây).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung cuối năm)**, '
                 'quy tắc hoặc công thức nào sau đây xác định đúng **Chênh lệch trên biểu đồ**?',
            'options': ['$\\text{Chênh lệch} = \\text{Số lượng nhiều hơn} + \\text{Số lượng ít hơn}$',
                        '$\\text{Chênh lệch} = \\text{Số lượng nhiều hơn} - \\text{Số lượng ít hơn}$',
                        'Đảo ngược vế của quy tắc: $\\text{Chênh lệch} = \\text{Số lượng nhiều hơn} - '
                        '\\text{Số lượng ít hơn}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Chênh lệch} = \\text{Số '
                        'lượng nhiều hơn} - \\text{Số lượng ít hơn}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng '
                        '(Ôn tập chung cuối năm), **Chênh lệch trên biểu đồ** được xác định bởi: '
                        '$\\text{Chênh lệch} = \\text{Số lượng nhiều hơn} - \\text{Số lượng ít hơn}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung cuối năm)**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tổng số liệu**?',
            'options': ['$\\text{Tổng} = \\text{Nhóm 1} - \\text{Nhóm 2} + \\text{Nhóm 3} + \\dots$',
                        '$\\text{Tổng} = \\text{Nhóm 1} + \\text{Nhóm 2} + \\text{Nhóm 2} + \\dots$',
                        '$\\text{Tổng} = \\text{Nhóm 1} + \\text{Nhóm 2} + \\text{Nhóm 3} + \\dots$',
                        '$\\text{Tổng} = \\text{Nhóm 2} + \\text{Nhóm 2} + \\text{Nhóm 3} + \\dots$'],
            'answer': 2,
            'solution': 'Trong Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung cuối năm), '
                        '**Tổng số liệu** có công thức/quy tắc là: $\\text{Tổng} = \\text{Nhóm 1} + '
                        '\\text{Nhóm 2} + \\text{Nhóm 3} + \\dots$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trên biểu đồ tranh số bàn thắng của $3$ cầu thủ: Nam ⚽⚽⚽, Hải ⚽⚽, Minh ⚽⚽⚽⚽ (biết mỗi ⚽ $= '
                 '2$ bàn thắng). Hỏi Minh ghi được nhiều hơn Hải mấy bàn thắng?',
            'options': ['$2$ bàn thắng', '$6$ bàn thắng', '$8$ bàn thắng', '$4$ bàn thắng'],
            'answer': 3,
            'solution': 'Minh ghi được $2 \\times 4 = 8$ bàn, Hải ghi được $2 \\times 2 = 4$ bàn. Minh ghi '
                        'nhiều hơn Hải: $8 - 4 = 4$ (bàn thắng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập '
                 'chung cuối năm)**, nhận định nào sau đây là **chính xác**?',
            'options': ['Đọc, phân tích và trả lời đúng các câu hỏi từ bảng kiểm đếm và biểu đồ tranh.',
                        'Đọc, phân tích và trả lời đúng các câu hỏi từ bảng kiểm đếm và biểu đồ tranh. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đọc, phân tích và trả lời đúng các câu hỏi từ bảng kiểm '
                        'đếm và biểu đồ tranh.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc, phân tích và trả lời đúng '
                        'các câu hỏi từ bảng kiểm đếm và biểu đồ tranh.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn '
                        'tập chung cuối năm): Đọc, phân tích và trả lời đúng các câu hỏi từ bảng kiểm đếm và '
                        'biểu đồ tranh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Khi tung một đồng xu lên cao, đồng xu rơi xuống đất là sự kiện chắc chắn xảy '
                 'ra.”',
            'answer': True,
            'solution': 'Mọi vật tung lên cao đều rơi xuống đất do trọng lực nên đây là sự kiện chắc chắn. '
                        'Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung cuối năm)**, '
                 'quy tắc **Chênh lệch trên biểu đồ** được xác định bởi $\\text{Chênh lệch} = \\text{Số '
                 'lượng nhiều hơn} - \\text{Số lượng ít hơn}$ và khi áp dụng cho ví dụ “Trong hộp có $5$ tấm '
                 'thẻ ghi các số $2, 4, 6, 8, 10$. Rút ngẫu nhiên $1$ tấm thẻ. Sự kiện “rút được tấm thẻ ghi '
                 'số lớn hơn $1$” là chắc...” ta có lời giải: Vì cả $5$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ '
                 'nên sự kiện rút được tấm thẻ ghi số lớn hơn $1$ là **chắc chắn**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Chênh lệch trên biểu đồ** ($\\text{Chênh '
                        'lệch} = \\text{Số lượng nhiều hơn} - \\text{Số lượng ít hơn}$) và lời giải ví dụ '
                        'minh họa của Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập chung '
                        'cuối năm).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng '
                 '(Ôn tập chung cuối năm)** để giải bài toán sau: Trong hộp có $5$ tấm thẻ ghi các số $2, 4, '
                 '6, 8, 10$. Rút ngẫu nhiên $1$ tấm thẻ. Sự kiện “rút được tấm thẻ ghi số lớn hơn $1$” là '
                 'chắc chắn, có thể hay không thể? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì cả $5$ số $2, 4, 6, 8, 10$ đều bé hơn $1$ nên sự kiện rút được tấm thẻ ghi số '
                        'lớn hơn $1$ là **chắc chắn**.',
                        'Vì cả $5$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ nên sự kiện rút được tấm thẻ ghi số '
                        'lớn hơn $1$ là **chắc chắn**.',
                        'Vì cả $5$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ nên sự kiện rút được tấm thẻ ghi số '
                        'lớn hơn $2$ là **chắc chắn**.',
                        'Vì cả $10$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ nên sự kiện rút được tấm thẻ ghi số '
                        'lớn hơn $1$ là **chắc chắn**.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 74: Ôn tập kiểm đếm số liệu và lựa chọn khả năng (Ôn tập '
                        'chung cuối năm): Vì cả $5$ số $2, 4, 6, 8, 10$ đều lớn hơn $1$ nên sự kiện rút được '
                        'tấm thẻ ghi số lớn hơn $1$ là **chắc chắn**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng có $50\\text{ kg}$ đường, buổi sáng bán được $15\\text{ kg}$ đường, buổi '
                 'chiều bán được $20\\text{ kg}$ đường. Hỏi cửa hàng còn lại bao nhiêu ki-lô-gam đường?',
            'answer': ['15', '15kg', '15 kg'],
            'unit': None,
            'solution': 'Số ki-lô-gam đường cửa hàng còn lại là: $50 - 15 - 20 = 15$ ($\\text{kg}$).',
            'alt': None,
            'note': None}]}]


# Đồng bộ game_type, game_title, game_description và đảm bảo 4 phương án trắc nghiệm phân biệt
from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("math", 2, _l)
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
