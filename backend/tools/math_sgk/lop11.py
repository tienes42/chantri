"""Dữ liệu bài học SGK Toán Lớp 11 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 11 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học (title).
Mỗi bài học gồm đầy đủ Yêu cầu cần đạt (requirements), Định nghĩa, Lý thuyết, Công thức, Ví dụ, Ứng dụng thực tế
và đúng 10 câu hỏi luyện tập theo 3 mức độ: 4 Nhận biết + 4 Thông hiểu + 2 Vận dụng.
"""

GRADE = 11

LESSONS = [{'topic': 'l11-ch01-luong-giac',
  'context_title': 'Chương I: Hàm số lượng giác và phương trình lượng giác',
  'context': 'Chương I · SGK Toán 11: Góc lượng giác, công thức lượng giác, hàm số và phương trình lượng '
             'giác.',
  'title': 'Bài 1: Giá trị lượng giác của góc lượng giác',
  'icon': '📐',
  'description': 'Góc lượng giác, đơn vị radian, đường tròn lượng giác, giá trị lượng giác của góc lượng '
                 'giác và hệ thức cơ bản.',
  'requirements': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa độ '
                   'và radian.',
                   'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin \\alpha, '
                   '\\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                   'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên quan '
                   'đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
  'definition': 'Góc lượng giác có tia đầu $Ou$, tia cuối $Ov$ kí hiệu là $(Ou, Ov)$. Cung tròn có độ dài '
                'bằng bán kính $R$ thì chắn góc ở tâm có số đo $1\\text{ rad}$, với $180^\\circ = '
                '\\pi\\text{ rad}$. Trên đường tròn lượng giác tâm $O$ bán kính $R = 1$, gốc $A(1; 0)$, nếu '
                'điểm $M(x_0; y_0)$ biểu diễn góc lượng giác $\\alpha$ thì $\\cos \\alpha = x_0$, $\\sin '
                '\\alpha = y_0$, $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha}$ ($\\cos \\alpha '
                '\\ne 0$) và $\\cot \\alpha = \\dfrac{\\cos \\alpha}{\\sin \\alpha}$ ($\\sin \\alpha \\ne '
                '0$).',
  'theory': '1. Đổi đơn vị: $\\alpha\\text{ (rad)} = \\dfrac{a \\cdot \\pi}{180}$ với $a^\\circ$; độ dài '
            'cung tròn $l = R\\alpha$ ($\\alpha$ tính bằng radian). 2. Hệ thức cơ bản: $\\sin^2 \\alpha + '
            '\\cos^2 \\alpha = 1$; $1 + \\tan^2 \\alpha = \\dfrac{1}{\\cos^2 \\alpha}$; $1 + \\cot^2 \\alpha '
            '= \\dfrac{1}{\\sin^2 \\alpha}$; $\\tan \\alpha \\cdot \\cot \\alpha = 1$. 3. Quy tắc góc liên '
            "quan đặc biệt: ''Cos đối, sin bù, phụ chéo, khác $\\pi$ tang và côtang''.",
  'formulas': [{'category': 'Đổi đơn vị và hệ thức lượng giác cơ bản',
                'items': [{'name': 'Đổi độ và radian',
                           'formula': '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                                      'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'},
                          {'name': 'Độ dài cung tròn',
                           'formula': '$l = R \\cdot \\alpha \\quad (\\alpha \\text{ tính bằng rad})$'},
                          {'name': 'Hệ thức cơ bản',
                           'formula': '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1, \\quad 1 + \\tan^2 \\alpha = '
                                      '\\dfrac{1}{\\cos^2 \\alpha}, \\quad 1 + \\cot^2 \\alpha = '
                                      '\\dfrac{1}{\\sin^2 \\alpha}$'}]}],
  'example': 'Cho $\\sin \\alpha = \\dfrac{3}{5}$ và $\\dfrac{\\pi}{2} < \\alpha < \\pi$. Tính $\\cos '
             '\\alpha$ và $\\tan \\alpha$.',
  'example_answer': 'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos \\alpha = '
                    '-\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = -\\dfrac{4}{5}$. Suy ra '
                    '$\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} = -\\dfrac{3}{4}$.',
  'real_life': 'Tính quãng đường di chuyển của đầu kim đồng hồ, cabin vòng quay Mặt Trời hoặc vệ tinh quay '
               'quanh Trái Đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc có số đo $120^\\circ$ đổi sang đơn vị radian là:',
            'options': ['$\\dfrac{2\\pi}{3}$',
                        '$\\dfrac{\\pi}{3}$',
                        '$\\dfrac{3\\pi}{4}$',
                        '$\\dfrac{5\\pi}{6}$'],
            'answer': 0,
            'solution': 'Ta có $120^\\circ = \\dfrac{120\\pi}{180} = \\dfrac{2\\pi}{3}\\text{ (rad)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với mọi góc lượng giác $\\alpha$, hệ thức nào dưới đây luôn đúng?',
            'options': ['$\\sin^2 \\alpha - \\cos^2 \\alpha = 1$',
                        '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$',
                        '$\\sin \\alpha + \\cos \\alpha = 1$',
                        '$\\tan^2 \\alpha + \\cot^2 \\alpha = 1$'],
            'answer': 1,
            'solution': 'Hệ thức lượng giác cơ bản đúng với mọi $\\alpha$ là $\\sin^2 \\alpha + \\cos^2 '
                        '\\alpha = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 1: Giá trị lượng giác của góc lượng giác**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Đổi độ và radian**?',
            'options': ['$l = R \\cdot \\alpha \\quad (\\alpha \\text{ tính bằng rad})$',
                        '$\\sin^2 \\alpha + \\cos^2 \\alpha = 1, \\quad 1 + \\tan^2 \\alpha = '
                        '\\dfrac{1}{\\cos^2 \\alpha}, \\quad 1 + \\cot^2 \\alpha = \\dfrac{1}{\\sin^2 '
                        '\\alpha}$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) = '
                        '\\cos a \\cos b \\mp \\sin a \\sin b$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 1: Giá trị lượng giác của góc lượng giác, '
                        '**Đổi độ và radian** được xác định bởi: $a^\\circ = \\dfrac{\\pi a}{180}\\text{ '
                        'rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Giá trị lượng giác của góc lượng giác**, nội dung/biểu thức $l = R \\cdot '
                 '\\alpha \\quad (\\alpha \\text{ tính bằng rad})$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Đổi độ và radian',
                        'Hệ thức cơ bản',
                        'Công thức cộng sin và cos',
                        'Độ dài cung tròn'],
            'answer': 3,
            'solution': 'Trong Bài 1: Giá trị lượng giác của góc lượng giác, biểu thức/quy tắc $l = R \\cdot '
                        '\\alpha \\quad (\\alpha \\text{ tính bằng rad})$ chính là nội dung của **Độ dài '
                        'cung tròn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\cos \\alpha = -\\dfrac{3}{5}$ với $\\pi < \\alpha < \\dfrac{3\\pi}{2}$. Giá trị của '
                 '$\\sin \\alpha$ bằng:',
            'options': ['$-\\dfrac{4}{5}$', '$\\dfrac{4}{5}$', '$-\\dfrac{3}{4}$', '$\\dfrac{3}{4}$'],
            'answer': 0,
            'solution': 'Do $\\pi < \\alpha < \\dfrac{3\\pi}{2}$ nên $\\sin \\alpha < 0$. Vậy $\\sin \\alpha '
                        '= -\\sqrt{1 - \\cos^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = -\\dfrac{4}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Giá trị lượng giác của góc lượng giác** (Chương I: Hàm số lượng giác và '
                 'phương trình lượng giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Thuộc và áp dụng được công thức cộng cho $\\sin(a \\pm b), \\cos(a \\pm b), \\tan(a '
                        '\\pm b)$.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Vận dụng được công thức nhân đôi $\\sin 2a, \\cos 2a, \\tan 2a$ và công thức hạ '
                        'bậc.',
                        'Biến đổi được tích thành tổng và tổng thành tích để rút gọn biểu thức lượng giác.'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 1: Giá trị lượng giác của góc lượng giác: Nhận biết '
                        'được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa độ và '
                        'radian.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho góc lượng giác $\\alpha$ thỏa mãn $\\tan \\alpha = 2$ và $0 < \\alpha < '
                 '\\dfrac{\\pi}{2}$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Giá trị của $\\cot \\alpha$ bằng $\\dfrac{1}{2}$.',
                           'Giá trị của $\\cos \\alpha$ dương và $\\sin \\alpha$ dương.',
                           'Giá trị của $\\cos^2 \\alpha$ bằng $\\dfrac{1}{5}$.',
                           'Giá trị của biểu thức $P = \\dfrac{\\sin \\alpha + \\cos \\alpha}{\\sin \\alpha '
                           '- \\cos \\alpha}$ bằng $2$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $\\cot \\alpha = \\dfrac{1}{\\tan \\alpha} = \\dfrac{1}{2}$. b) Đúng vì '
                        '$\\alpha \\in \\left(0; \\dfrac{\\pi}{2}\\right)$ thuộc góc phần tư thứ I. c) Đúng '
                        'vì $\\cos^2 \\alpha = \\dfrac{1}{1 + \\tan^2 \\alpha} = \\dfrac{1}{5}$. d) Sai vì '
                        'chia cả tử và mẫu cho $\\cos \\alpha$ được $P = \\dfrac{\\tan \\alpha + 1}{\\tan '
                        '\\alpha - 1} = \\dfrac{2 + 1}{2 - 1} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 1: Giá trị lượng giác '
                 'của góc lượng giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được khái niệm góc lượng '
                           'giác, hệ thức Chasles và đổi được số đo góc giữa độ và radian.',
                           'Quy tắc/công thức **Đổi độ và radian** trong bài được xác định bởi: $a^\\circ = '
                           '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$.',
                           'Trong mọi trường hợp, **Đổi độ và radian** luôn được tính bằng công thức '
                           '$\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) '
                           '= \\cos a \\cos b \\mp \\sin a \\sin b$ (thuộc Công thức cộng sin và cos) mà '
                           'không cần điều kiện của Bài 1: Giá trị lượng giác của góc lượng giác.',
                           'Với bài toán minh họa: “Cho $\\sin \\alpha = \\dfrac{3}{5}$ và $\\dfrac{\\pi}{2} '
                           '< \\alpha < \\pi$. Tính $\\cos \\alpha$ và $\\tan \\alpha$.”, lời giải đúng là: '
                           'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                           '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                           '-\\dfrac{4}{5}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Giá trị lượng giác của góc lượng giác. '
                        'b) **Đúng** theo công thức trọng tâm **Đổi độ và radian** ($a^\\circ = \\dfrac{\\pi '
                        'a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$). c) **Sai** vì $\\sin(a \\pm b) = '
                        '\\sin a \\cos b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) = \\cos a \\cos b \\mp '
                        '\\sin a \\sin b$ là công thức của nội dung khác, không phải quy tắc chung của **Đổi '
                        'độ và radian**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 1: Giá trị lượng giác của góc lượng giác** để giải quyết tình '
                 'huống sau: Cho $\\sin \\alpha = \\dfrac{3}{5}$ và $\\dfrac{\\pi}{2} < \\alpha < \\pi$. '
                 'Tính $\\cos \\alpha$ và $\\tan \\alpha$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm '
                        '\\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Giá trị lượng giác của góc lượng giác: Vì '
                        '$\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos \\alpha = '
                        '-\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = -\\dfrac{4}{5}$. Suy '
                        'ra $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} = -\\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đường tròn có bán kính $R = 15\\text{ cm}$. Tính độ dài cung tròn (đơn vị: cm) trên '
                 'đường tròn đó có số đo bằng $\\dfrac{2}{5}\\text{ rad}$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Áp dụng công thức độ dài cung tròn $l = R \\cdot \\alpha = 15 \\cdot \\dfrac{2}{5} '
                        '= 6\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch01-luong-giac',
  'context_title': 'Chương I: Hàm số lượng giác và phương trình lượng giác',
  'context': 'Chương I · SGK Toán 11: Góc lượng giác, công thức lượng giác, hàm số và phương trình lượng '
             'giác.',
  'title': 'Bài 2: Công thức lượng giác',
  'icon': '🔄',
  'description': 'Công thức cộng, công thức nhân đôi, công thức hạ bậc, công thức biến đổi tích thành tổng '
                 'và tổng thành tích.',
  'requirements': ['Thuộc và áp dụng được công thức cộng cho $\\sin(a \\pm b), \\cos(a \\pm b), \\tan(a \\pm '
                   'b)$.',
                   'Vận dụng được công thức nhân đôi $\\sin 2a, \\cos 2a, \\tan 2a$ và công thức hạ bậc.',
                   'Biến đổi được tích thành tổng và tổng thành tích để rút gọn biểu thức lượng giác.'],
  'definition': 'Các công thức lượng giác biểu diễn giá trị lượng giác của tổng, hiệu $a \\pm b$, góc nhân '
                'đôi $2a$ theo giá trị lượng giác của $a, b$, cũng như chuyển đổi giữa tổng và tích các hàm '
                'lượng giác.',
  'theory': '1. Công thức cộng: $\\cos(a - b) = \\cos a \\cos b + \\sin a \\sin b$; $\\cos(a + b) = \\cos a '
            '\\cos b - \\sin a \\sin b$; $\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b$. 2. Công '
            'thức nhân đôi: $\\sin 2a = 2\\sin a \\cos a$; $\\cos 2a = \\cos^2 a - \\sin^2 a = 2\\cos^2 a - '
            '1 = 1 - 2\\sin^2 a$. 3. Tổng thành tích: $\\cos u + \\cos v = 2\\cos\\dfrac{u + '
            'v}{2}\\cos\\dfrac{u - v}{2}$; $\\sin u + \\sin v = 2\\sin\\dfrac{u + v}{2}\\cos\\dfrac{u - '
            'v}{2}$.',
  'formulas': [{'category': 'Công thức cộng và nhân đôi',
                'items': [{'name': 'Công thức cộng sin và cos',
                           'formula': '$\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b, \\quad '
                                      '\\cos(a \\pm b) = \\cos a \\cos b \\mp \\sin a \\sin b$'},
                          {'name': 'Công thức cộng tang',
                           'formula': '$\\tan(a \\pm b) = \\dfrac{\\tan a \\pm \\tan b}{1 \\mp \\tan a \\tan '
                                      'b}$'},
                          {'name': 'Công thức nhân đôi',
                           'formula': '$\\sin 2a = 2\\sin a \\cos a, \\quad \\cos 2a = 2\\cos^2 a - 1 = 1 - '
                                      '2\\sin^2 a$'},
                          {'name': 'Công thức hạ bậc',
                           'formula': '$\\cos^2 a = \\dfrac{1 + \\cos 2a}{2}, \\quad \\sin^2 a = \\dfrac{1 - '
                                      '\\cos 2a}{2}$'}]}],
  'example': 'Tính giá trị chính xác của $\\sin 75^\\circ$ bằng công thức cộng.',
  'example_answer': 'Ta có $\\sin 75^\\circ = \\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ \\cos 30^\\circ '
                    '+ \\cos 45^\\circ \\sin 30^\\circ = \\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2} '
                    '+ \\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2} = \\dfrac{\\sqrt{6} + \\sqrt{2}}{4}$.',
  'real_life': 'Tổng hợp hai dao động điều hòa cùng tần số trong vật lí và xử lí tín hiệu âm thanh, sóng vô '
               'tuyến.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với mọi góc lượng giác $a, b$, công thức nào dưới đây đúng?',
            'options': ['$\\cos(a - b) = \\cos a \\cos b - \\sin a \\sin b$',
                        '$\\cos(a - b) = \\cos a \\cos b + \\sin a \\sin b$',
                        '$\\cos(a - b) = \\sin a \\cos b - \\cos a \\sin b$',
                        '$\\cos(a - b) = \\sin a \\cos b + \\cos a \\sin b$'],
            'answer': 1,
            'solution': 'Theo công thức cộng đối với côsin: $\\cos(a - b) = \\cos a \\cos b + \\sin a \\sin '
                        'b$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức nhân đôi nào dưới đây đúng?',
            'options': ['$\\sin 2a = \\sin a \\cos a$',
                        '$\\sin 2a = 2\\sin a$',
                        '$\\sin 2a = 2\\sin a \\cos a$',
                        '$\\sin 2a = \\cos^2 a - \\sin^2 a$'],
            'answer': 2,
            'solution': 'Theo công thức nhân đôi, $\\sin 2a = 2\\sin a \\cos a$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 2: Công thức lượng giác**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Công thức cộng sin và cos**?',
            'options': ['$\\tan(a \\pm b) = \\dfrac{\\tan a \\pm \\tan b}{1 \\mp \\tan a \\tan b}$',
                        '$\\sin 2a = 2\\sin a \\cos a, \\quad \\cos 2a = 2\\cos^2 a - 1 = 1 - 2\\sin^2 a$',
                        '$\\cos^2 a = \\dfrac{1 + \\cos 2a}{2}, \\quad \\sin^2 a = \\dfrac{1 - \\cos 2a}{2}$',
                        '$\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) = '
                        '\\cos a \\cos b \\mp \\sin a \\sin b$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 2: Công thức lượng giác, **Công thức cộng sin '
                        'và cos** được xác định bởi: $\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin '
                        'b, \\quad \\cos(a \\pm b) = \\cos a \\cos b \\mp \\sin a \\sin b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Công thức lượng giác**, nội dung/biểu thức $\\tan(a \\pm b) = \\dfrac{\\tan '
                 'a \\pm \\tan b}{1 \\mp \\tan a \\tan b}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Công thức cộng tang',
                        'Công thức cộng sin và cos',
                        'Công thức nhân đôi',
                        'Công thức hạ bậc'],
            'answer': 0,
            'solution': 'Trong Bài 2: Công thức lượng giác, biểu thức/quy tắc $\\tan(a \\pm b) = '
                        '\\dfrac{\\tan a \\pm \\tan b}{1 \\mp \\tan a \\tan b}$ chính là nội dung của **Công '
                        'thức cộng tang**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\sin a = \\dfrac{1}{3}$. Giá trị của $\\cos 2a$ bằng:',
            'options': ['$\\dfrac{8}{9}$', '$\\dfrac{7}{9}$', '$-\\dfrac{7}{9}$', '$\\dfrac{5}{9}$'],
            'answer': 1,
            'solution': 'Áp dụng công thức nhân đôi: $\\cos 2a = 1 - 2\\sin^2 a = 1 - 2 \\cdot '
                        '\\left(\\dfrac{1}{3}\\right)^2 = \\dfrac{7}{9}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Công thức lượng giác** (Chương I: Hàm số lượng giác và phương trình lượng '
                 'giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Thuộc và áp dụng được công thức cộng cho $\\sin(a \\pm b), \\cos(a \\pm b), \\tan(a '
                        '\\pm b)$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 2: Công thức lượng giác: Thuộc và áp dụng được công '
                        'thức cộng cho $\\sin(a \\pm b), \\cos(a \\pm b), \\tan(a \\pm b)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai góc nhọn $a$ và $b$ thỏa mãn $\\tan a = \\dfrac{1}{2}$ và $\\tan b = '
                 '\\dfrac{1}{3}$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Công thức tính $\\tan(a + b)$ là $\\tan(a + b) = \\dfrac{\\tan a + \\tan b}{1 - '
                           '\\tan a \\tan b}$.',
                           'Giá trị của $\\tan(a + b)$ bằng $1$.',
                           'Tổng hai góc $a + b$ bằng $45^\\circ$.',
                           'Giá trị của $\\tan 2a$ bằng $1$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\tan(a + b) = \\dfrac{\\dfrac{1}{2} + \\dfrac{1}{3}}{1 - '
                        '\\dfrac{1}{6}} = \\dfrac{\\dfrac{5}{6}}{\\dfrac{5}{6}} = 1$. c) Đúng vì $a, b \\in '
                        '(0^\\circ; 90^\\circ)$ và $\\tan(a + b) = 1 \\Rightarrow a + b = 45^\\circ$. d) Sai '
                        'vì $\\tan 2a = \\dfrac{2\\tan a}{1 - \\tan^2 a} = \\dfrac{1}{1 - \\dfrac{1}{4}} = '
                        '\\dfrac{4}{3} \\ne 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 2: Công thức lượng '
                 'giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thuộc và áp dụng được công thức '
                           'cộng cho $\\sin(a \\pm b), \\cos(a \\pm b), \\tan(a \\pm b)$.',
                           'Quy tắc/công thức **Công thức cộng sin và cos** trong bài được xác định bởi: '
                           '$\\sin(a \\pm b) = \\sin a \\cos b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) '
                           '= \\cos a \\cos b \\mp \\sin a \\sin b$.',
                           'Trong mọi trường hợp, **Công thức cộng sin và cos** luôn được tính bằng công '
                           'thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 2: Công thức lượng giác.',
                           'Với bài toán minh họa: “Tính giá trị chính xác của $\\sin 75^\\circ$ bằng công '
                           'thức cộng.”, lời giải đúng là: Ta có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Công thức lượng giác. b) **Đúng** theo '
                        'công thức trọng tâm **Công thức cộng sin và cos** ($\\sin(a \\pm b) = \\sin a \\cos '
                        'b \\pm \\cos a \\sin b, \\quad \\cos(a \\pm b) = \\cos a \\cos b \\mp \\sin a \\sin '
                        'b$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                        '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức '
                        'của nội dung khác, không phải quy tắc chung của **Công thức cộng sin và cos**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 2: Công thức lượng giác** để giải quyết tình huống sau: Tính giá '
                 'trị chính xác của $\\sin 75^\\circ$ bằng công thức cộng. Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm '
                        '\\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).',
                        'Ta có...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Công thức lượng giác: Ta có $\\sin 75^\\circ = '
                        '\\sin(45^\\circ + 30^\\circ) = \\sin 45^\\circ \\cos 30^\\circ + \\cos 45^\\circ '
                        '\\sin 30^\\circ = \\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2} + '
                        '\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2} = \\dfrac{\\sqrt{6} + \\sqrt{2}}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = \\cos 75^\\circ \\cos 15^\\circ$ (viết dưới dạng số thập '
                 'phân).',
            'answer': ['0,25', '0.25'],
            'unit': None,
            'solution': 'Áp dụng công thức biến đổi tích thành tổng: $P = \\dfrac{1}{2}(\\cos 90^\\circ + '
                        '\\cos 60^\\circ) = \\dfrac{1}{2}\\left(0 + \\dfrac{1}{2}\\right) = \\dfrac{1}{4} = '
                        '0,25$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch01-luong-giac',
  'context_title': 'Chương I: Hàm số lượng giác và phương trình lượng giác',
  'context': 'Chương I · SGK Toán 11: Góc lượng giác, công thức lượng giác, hàm số và phương trình lượng '
             'giác.',
  'title': 'Bài 3: Hàm số lượng giác',
  'icon': '〰️',
  'description': 'Tập xác định, tập giá trị, tính chẵn lẻ, tính tuần hoàn, sự biến thiên và đồ thị của bốn '
                 'hàm số lượng giác cơ bản.',
  'requirements': ['Xác định được tập xác định, tập giá trị, tính chẵn lẻ và chu kì tuần hoàn của các hàm số '
                   '$y = \\sin x, y = \\cos x, y = \\tan x, y = \\cot x$.',
                   'Nhận biết được dáng điệu đồ thị và các khoảng đồng biến, nghịch biến của hàm số lượng '
                   'giác.',
                   'Tìm được giá trị lớn nhất, giá trị nhỏ nhất của các biểu thức chứa hàm số lượng giác.'],
  'definition': 'Các hàm số $y = \\sin x$ và $y = \\cos x$ xác định trên $\\mathbb{R}$, có tập giá trị là '
                '$[-1; 1]$ và tuần hoàn với chu kì $T = 2\\pi$. Hàm số $y = \\tan x$ xác định khi $x \\ne '
                '\\dfrac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{R} \\cap \\mathbb{Z}$) và $y = \\cot x$ xác '
                'định khi $x \\ne k\\pi$ ($k \\in \\mathbb{Z}$), đều tuần hoàn với chu kì $T = \\pi$.',
  'theory': '1. Tính chẵn lẻ: chỉ có hàm số $y = \\cos x$ là hàm số chẵn ($\\cos(-x) = \\cos x$), còn ba hàm '
            'số $y = \\sin x, y = \\tan x, y = \\cot x$ đều là hàm số lẻ. 2. Chu kì của hàm số $y = \\sin(ax '
            '+ b)$ và $y = \\cos(ax + b)$ ($a \\ne 0$) là $T = \\dfrac{2\\pi}{|a|}$; chu kì của $y = '
            '\\tan(ax + b)$ và $y = \\cot(ax + b)$ là $T = \\dfrac{\\pi}{|a|}$.',
  'formulas': [{'category': 'Đặc trưng bốn hàm số lượng giác',
                'items': [{'name': 'Tập giá trị của sin và cos',
                           'formula': '$-1 \\le \\sin x \\le 1, \\quad -1 \\le \\cos x \\le 1 \\quad '
                                      '(\\forall x \\in \\mathbb{R})$'},
                          {'name': 'Điều kiện xác định tan và cot',
                           'formula': '$\\tan x: x \\ne \\dfrac{\\pi}{2} + k\\pi; \\quad \\cot x: x \\ne '
                                      'k\\pi \\quad (k \\in \\mathbb{Z})$'},
                          {'name': 'Chu kì tuần hoàn',
                           'formula': '$T_{\\sin(ax+b)} = T_{\\cos(ax+b)} = \\dfrac{2\\pi}{|a|}, \\quad '
                                      'T_{\\tan(ax+b)} = T_{\\cot(ax+b)} = \\dfrac{\\pi}{|a|}$'}]}],
  'example': 'Tìm tập giá trị, giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = 3\\sin 2x - 1$.',
  'example_answer': 'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                    '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là $[-4; '
                    '2]$, $\\max y = 2$ và $\\min y = -4$.',
  'real_life': 'Mô tả dao động của con lắc, dòng điện xoay chiều hình sin và chu kì thủy triều lên xuống '
               'hàng ngày.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các hàm số lượng giác sau, hàm số nào là hàm số chẵn?',
            'options': ['$y = \\sin x$', '$y = \\tan x$', '$y = \\cos x$', '$y = \\cot x$'],
            'answer': 2,
            'solution': 'Vì $\\cos(-x) = \\cos x, \\forall x \\in \\mathbb{R}$ nên hàm số $y = \\cos x$ là '
                        'hàm số chẵn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tập xác định của hàm số $y = \\cot x$ là:',
            'options': ['$\\mathbb{R} \\setminus \\left\\{\\dfrac{\\pi}{2} + k\\pi \\mid k \\in '
                        '\\mathbb{Z}\\right\\}$',
                        '$\\mathbb{R}$',
                        '$[-1; 1]$',
                        '$\\mathbb{R} \\setminus \\{k\\pi \\mid k \\in \\mathbb{Z}\\}$'],
            'answer': 3,
            'solution': 'Biểu thức $\\cot x = \\dfrac{\\cos x}{\\sin x}$ xác định khi $\\sin x \\ne 0 '
                        '\\Leftrightarrow x \\ne k\\pi, k \\in \\mathbb{Z}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 3: Hàm số lượng giác**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Tập giá trị của sin và cos**?',
            'options': ['$-1 \\le \\sin x \\le 1, \\quad -1 \\le \\cos x \\le 1 \\quad (\\forall x \\in '
                        '\\mathbb{R})$',
                        '$\\tan x: x \\ne \\dfrac{\\pi}{2} + k\\pi; \\quad \\cot x: x \\ne k\\pi \\quad (k '
                        '\\in \\mathbb{Z})$',
                        '$T_{\\sin(ax+b)} = T_{\\cos(ax+b)} = \\dfrac{2\\pi}{|a|}, \\quad T_{\\tan(ax+b)} = '
                        'T_{\\cot(ax+b)} = \\dfrac{\\pi}{|a|}$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 3: Hàm số lượng giác, **Tập giá trị của sin '
                        'và cos** được xác định bởi: $-1 \\le \\sin x \\le 1, \\quad -1 \\le \\cos x \\le 1 '
                        '\\quad (\\forall x \\in \\mathbb{R})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Hàm số lượng giác**, nội dung/biểu thức $\\tan x: x \\ne \\dfrac{\\pi}{2} + '
                 'k\\pi; \\quad \\cot x: x \\ne k\\pi \\quad (k \\in \\mathbb{Z})$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Tập giá trị của sin và cos',
                        'Điều kiện xác định tan và cot',
                        'Chu kì tuần hoàn',
                        'Đổi độ và radian'],
            'answer': 1,
            'solution': 'Trong Bài 3: Hàm số lượng giác, biểu thức/quy tắc $\\tan x: x \\ne \\dfrac{\\pi}{2} '
                        '+ k\\pi; \\quad \\cot x: x \\ne k\\pi \\quad (k \\in \\mathbb{Z})$ chính là nội '
                        'dung của **Điều kiện xác định tan và cot**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Chu kì tuần hoàn của hàm số $y = \\sin 2x$ là:',
            'options': ['$2\\pi$', '$4\\pi$', '$\\pi$', '$\\dfrac{\\pi}{2}$'],
            'answer': 2,
            'solution': 'Chu kì của hàm số $y = \\sin(ax + b)$ là $T = \\dfrac{2\\pi}{|a|} = '
                        '\\dfrac{2\\pi}{2} = \\pi$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Hàm số lượng giác** (Chương I: Hàm số lượng giác và phương trình lượng '
                 'giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Xác định được tập xác định, tập giá trị, tính chẵn lẻ và chu kì tuần hoàn của các '
                        'hàm số $y = \\sin x, y = \\cos x, y = \\tan x, y = \\cot x$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 3: Hàm số lượng giác: Xác định được tập xác định, tập '
                        'giá trị, tính chẵn lẻ và chu kì tuần hoàn của các hàm số $y = \\sin x, y = \\cos x, '
                        'y = \\tan x, y = \\cot x$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = f(x) = 2\\cos x + 3$ xác định trên $\\mathbb{R}$. Xét tính đúng sai của '
                 'các mệnh đề sau:',
            'statements': ['Hàm số $f(x)$ là hàm số chẵn trên $\\mathbb{R}$.',
                           'Hàm số $f(x)$ tuần hoàn với chu kì $T = 2\\pi$.',
                           'Giá trị lớn nhất của hàm số $f(x)$ bằng $5$.',
                           'Giá trị nhỏ nhất của hàm số $f(x)$ bằng $3$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $f(-x) = 2\\cos(-x) + 3 = 2\\cos x + 3 = f(x)$. b) Đúng vì $\\cos x$ có '
                        'chu kì $2\\pi$. c) Đúng vì $\\cos x \\le 1 \\Rightarrow y \\le 5$. d) Sai vì $\\cos '
                        'x \\ge -1 \\Rightarrow \\min y = 2(-1) + 3 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 3: Hàm số lượng giác**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được tập xác định, tập '
                           'giá trị, tính chẵn lẻ và chu kì tuần hoàn của các hàm số $y = \\sin x, y = \\cos '
                           'x, y = \\tan x, y = \\cot x$.',
                           'Quy tắc/công thức **Tập giá trị của sin và cos** trong bài được xác định bởi: '
                           '$-1 \\le \\sin x \\le 1, \\quad -1 \\le \\cos x \\le 1 \\quad (\\forall x \\in '
                           '\\mathbb{R})$.',
                           'Trong mọi trường hợp, **Tập giá trị của sin và cos** luôn được tính bằng công '
                           'thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 3: Hàm số lượng giác.',
                           'Với bài toán minh họa: “Tìm tập giá trị, giá trị lớn nhất và giá trị nhỏ nhất '
                           'của hàm số $y = 3\\sin 2x - 1$.”, lời giải đúng là: Với mọi $x \\in '
                           '\\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le 3\\sin 2x \\le '
                           '3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập gi...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Hàm số lượng giác. b) **Đúng** theo '
                        'công thức trọng tâm **Tập giá trị của sin và cos** ($-1 \\le \\sin x \\le 1, \\quad '
                        '-1 \\le \\cos x \\le 1 \\quad (\\forall x \\in \\mathbb{R})$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Tập giá trị của sin và cos**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 3: Hàm số lượng giác** để giải quyết tình huống sau: Tìm tập giá '
                 'trị, giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = 3\\sin 2x - 1$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm '
                        '\\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Hàm số lượng giác: Với mọi $x \\in \\mathbb{R}$, ta '
                        'có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le 3\\sin 2x \\le 3 \\Rightarrow -4 '
                        '\\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là $[-4; 2]$, $\\max y = 2$ và $\\min y '
                        '= -4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Huyết áp của một người thay đổi theo thời gian $t$ (giây) được mô hình hóa bởi hàm số '
                 '$p(t) = 100 + 20\\sin(2\\pi t)$ (mmHg). Tính huyết áp cao nhất của người đó (đơn vị: '
                 'mmHg).',
            'answer': ['120'],
            'unit': None,
            'solution': 'Vì $\\sin(2\\pi t) \\le 1$ nên huyết áp cao nhất là $\\max p(t) = 100 + 20 \\cdot 1 '
                        '= 120\\text{ (mmHg)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch01-luong-giac',
  'context_title': 'Chương I: Hàm số lượng giác và phương trình lượng giác',
  'context': 'Chương I · SGK Toán 11: Góc lượng giác, công thức lượng giác, hàm số và phương trình lượng '
             'giác.',
  'title': 'Bài 4: Phương trình lượng giác cơ bản',
  'icon': '🎯',
  'description': 'Phương trình tương đương và công thức nghiệm của bốn phương trình lượng giác cơ bản sin x '
                 '= m, cos x = m, tan x = m, cot x = m.',
  'requirements': ['Nhận biết điều kiện có nghiệm của phương trình $\\sin x = m$ và $\\cos x = m$ là $|m| '
                   '\\le 1$.',
                   'Giải thành thạo bốn phương trình lượng giác cơ bản $\\sin x = m, \\cos x = m, \\tan x = '
                   'm, \\cot x = m$ theo cả đơn vị radian và độ.',
                   'Tìm được số nghiệm của phương trình lượng giác trên một khoảng hoặc đoạn cho trước.'],
  'definition': 'Các phương trình lượng giác cơ bản là các phương trình có dạng $\\sin x = m$, $\\cos x = '
                'm$, $\\tan x = m$, $\\cot x = m$, trong đó $m$ là số thực cho trước.',
  'theory': '1. Phương trình $\\sin x = \\sin \\alpha \\Leftrightarrow x = \\alpha + k2\\pi$ hoặc $x = \\pi '
            '- \\alpha + k2\\pi$ ($k \\in \\mathbb{Z}$). 2. Phương trình $\\cos x = \\cos \\alpha '
            '\\Leftrightarrow x = \\pm \\alpha + k2\\pi$ ($k \\in \\mathbb{Z}$). 3. Phương trình $\\tan x = '
            '\\tan \\alpha \\Leftrightarrow x = \\alpha + k\\pi$ ($k \\in \\mathbb{Z}$) và $\\cot x = \\cot '
            '\\alpha \\Leftrightarrow x = \\alpha + k\\pi$ ($k \\in \\mathbb{Z}$).',
  'formulas': [{'category': 'Công thức nghiệm phương trình lượng giác cơ bản',
                'items': [{'name': 'Phương trình sin u = sin v',
                           'formula': '$u = v + k2\\pi \\text{ hoặc } u = \\pi - v + k2\\pi \\quad (k \\in '
                                      '\\mathbb{Z})$'},
                          {'name': 'Phương trình cos u = cos v',
                           'formula': '$u = \\pm v + k2\\pi \\quad (k \\in \\mathbb{Z})$'},
                          {'name': 'Phương trình tan u = tan v và cot u = cot v',
                           'formula': '$u = v + k\\pi \\quad (k \\in \\mathbb{Z})$'},
                          {'name': 'Trường hợp đặc biệt',
                           'formula': '$\\sin x = 0 \\Leftrightarrow x = k\\pi; \\quad \\cos x = 0 '
                                      '\\Leftrightarrow x = \\dfrac{\\pi}{2} + k\\pi$'}]}],
  'example': 'Giải phương trình $\\cos x = \\dfrac{1}{2}$.',
  'example_answer': 'Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm '
                    '\\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).',
  'real_life': 'Xác định các thời điểm trong ngày mà mực nước thủy triều hoặc điện áp xoay chiều đạt đến một '
               'ngưỡng quy định.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình $\\sin x = m$ có nghiệm khi và chỉ khi:',
            'options': ['$m > 1$', '$m < -1$', '$m \\in \\mathbb{R}$', '$-1 \\le m \\le 1$'],
            'answer': 3,
            'solution': 'Vì $-1 \\le \\sin x \\le 1$ với mọi $x \\in \\mathbb{R}$ nên phương trình $\\sin x '
                        '= m$ có nghiệm khi và chỉ khi $-1 \\le m \\le 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $\\tan x = 1$ là:',
            'options': ['$x = \\dfrac{\\pi}{4} + k\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$x = \\dfrac{\\pi}{4} + k2\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$x = \\pm \\dfrac{\\pi}{4} + k\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$x = \\dfrac{\\pi}{2} + k\\pi \\quad (k \\in \\mathbb{Z})$'],
            'answer': 0,
            'solution': 'Ta có $\\tan x = 1 = \\tan \\dfrac{\\pi}{4} \\Leftrightarrow x = \\dfrac{\\pi}{4} + '
                        'k\\pi$ ($k \\in \\mathbb{Z}$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 4: Phương trình lượng giác cơ bản**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Phương trình sin u = sin v**?',
            'options': ['$u = \\pm v + k2\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$u = v + k2\\pi \\text{ hoặc } u = \\pi - v + k2\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$u = v + k\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$\\sin x = 0 \\Leftrightarrow x = k\\pi; \\quad \\cos x = 0 \\Leftrightarrow x = '
                        '\\dfrac{\\pi}{2} + k\\pi$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 4: Phương trình lượng giác cơ bản, **Phương '
                        'trình sin u = sin v** được xác định bởi: $u = v + k2\\pi \\text{ hoặc } u = \\pi - '
                        'v + k2\\pi \\quad (k \\in \\mathbb{Z})$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Phương trình lượng giác cơ bản**, nội dung/biểu thức $u = \\pm v + k2\\pi '
                 '\\quad (k \\in \\mathbb{Z})$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phương trình sin u = sin v',
                        'Phương trình tan u = tan v và cot u = cot v',
                        'Phương trình cos u = cos v',
                        'Trường hợp đặc biệt'],
            'answer': 2,
            'solution': 'Trong Bài 4: Phương trình lượng giác cơ bản, biểu thức/quy tắc $u = \\pm v + k2\\pi '
                        '\\quad (k \\in \\mathbb{Z})$ chính là nội dung của **Phương trình cos u = cos v**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Họ nghiệm của phương trình $2\\sin x - \\sqrt{3} = 0$ là:',
            'options': ['$x = \\pm \\dfrac{\\pi}{3} + k2\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$x = \\dfrac{\\pi}{6} + k2\\pi$ hoặc $x = \\dfrac{5\\pi}{6} + k2\\pi \\quad (k \\in '
                        '\\mathbb{Z})$',
                        '$x = \\dfrac{\\pi}{3} + k\\pi \\quad (k \\in \\mathbb{Z})$',
                        '$x = \\dfrac{\\pi}{3} + k2\\pi$ hoặc $x = \\dfrac{2\\pi}{3} + k2\\pi \\quad (k \\in '
                        '\\mathbb{Z})$'],
            'answer': 3,
            'solution': 'Ta có $\\sin x = \\dfrac{\\sqrt{3}}{2} = \\sin \\dfrac{\\pi}{3} \\Leftrightarrow x '
                        '= \\dfrac{\\pi}{3} + k2\\pi$ hoặc $x = \\pi - \\dfrac{\\pi}{3} + k2\\pi = '
                        '\\dfrac{2\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Phương trình lượng giác cơ bản** (Chương I: Hàm số lượng giác và phương '
                 'trình lượng giác), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết điều kiện có nghiệm của phương trình $\\sin x = m$ và $\\cos x = m$ là '
                        '$|m| \\le 1$.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 4: Phương trình lượng giác cơ bản: Nhận biết điều kiện '
                        'có nghiệm của phương trình $\\sin x = m$ và $\\cos x = m$ là $|m| \\le 1$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình lượng giác $\\cos 2x = 0$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Phương trình tương đương với $2x = \\dfrac{\\pi}{2} + k\\pi$ ($k \\in '
                           '\\mathbb{Z}$).',
                           'Họ nghiệm của phương trình là $x = \\dfrac{\\pi}{4} + k\\dfrac{\\pi}{2}$ ($k '
                           '\\in \\mathbb{Z}$).',
                           'Giá trị $x = \\dfrac{\\pi}{4}$ là một nghiệm của phương trình.',
                           'Trên khoảng $(0; \\pi)$, phương trình có đúng $1$ nghiệm.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì chia hai vế cho $2$. c) Đúng với $k = 0$. d) Sai vì trên $(0; '
                        '\\pi)$, $x = \\dfrac{\\pi}{4} + k\\dfrac{\\pi}{2} \\in (0; \\pi)$ có $2$ nghiệm ứng '
                        'với $k = 0$ ($x = \\dfrac{\\pi}{4}$) và $k = 1$ ($x = \\dfrac{3\\pi}{4}$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 4: Phương trình lượng '
                 'giác cơ bản**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết điều kiện có nghiệm của '
                           'phương trình $\\sin x = m$ và $\\cos x = m$ là $|m| \\le 1$.',
                           'Quy tắc/công thức **Phương trình sin u = sin v** trong bài được xác định bởi: $u '
                           '= v + k2\\pi \\text{ hoặc } u = \\pi - v + k2\\pi \\quad (k \\in \\mathbb{Z})$.',
                           'Trong mọi trường hợp, **Phương trình sin u = sin v** luôn được tính bằng công '
                           'thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 4: Phương trình lượng giác cơ bản.',
                           'Với bài toán minh họa: “Giải phương trình $\\cos x = \\dfrac{1}{2}$.”, lời giải '
                           'đúng là: Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} '
                           '\\Leftrightarrow x = \\pm \\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Phương trình lượng giác cơ bản. b) '
                        '**Đúng** theo công thức trọng tâm **Phương trình sin u = sin v** ($u = v + k2\\pi '
                        '\\text{ hoặc } u = \\pi - v + k2\\pi \\quad (k \\in \\mathbb{Z})$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Phương trình sin u = sin v**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 4: Phương trình lượng giác cơ bản** để giải quyết tình huống sau: '
                 'Giải phương trình $\\cos x = \\dfrac{1}{2}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có $\\cos x = \\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm '
                        '\\dfrac{\\pi}{3} + k2\\pi$ ($k \\in \\mathbb{Z}$).',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Phương trình lượng giác cơ bản: Ta có $\\cos x = '
                        '\\dfrac{1}{2} = \\cos \\dfrac{\\pi}{3} \\Leftrightarrow x = \\pm \\dfrac{\\pi}{3} + '
                        'k2\\pi$ ($k \\in \\mathbb{Z}$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Phương trình $\\sin x = \\dfrac{1}{2}$ có bao nhiêu nghiệm thuộc đoạn $[0; 2\\pi]$?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Trên đoạn $[0; 2\\pi]$, phương trình $\\sin x = \\dfrac{1}{2}$ có đúng $2$ nghiệm '
                        'là $x = \\dfrac{\\pi}{6}$ và $x = \\dfrac{5\\pi}{6}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch02-day-so-cap-so',
  'context_title': 'Chương II: Dãy số. Cấp số cộng và cấp số nhân',
  'context': 'Chương II · SGK Toán 11: Dãy số, cấp số cộng và cấp số nhân.',
  'title': 'Bài 5: Dãy số',
  'icon': '🔢',
  'description': 'Khái niệm dãy số hữu hạn, dãy số vô hạn, các cách cho một dãy số, dãy số tăng, dãy số giảm '
                 'và dãy số bị chặn.',
  'requirements': ['Nhận biết được dãy số, số hạng đầu $u_1$, số hạng tổng quát $u_n$ và cách cho dãy số '
                   'bằng công thức hoặc hệ thức truy hồi.',
                   'Xét được tính tăng, giảm của một dãy số thông qua hiệu $u_{n+1} - u_n$.',
                   'Chứng minh được một dãy số bị chặn trên, bị chặn dưới hoặc bị chặn.'],
  'definition': 'Mỗi hàm số $u$ xác định trên tập các số nguyên dương $\\mathbb{N}^*$ được gọi là một dãy số '
                'vô hạn, kí hiệu $(u_n)$ với $u_n = u(n)$. Dãy $(u_n)$ là dãy số tăng nếu $u_{n+1} > u_n, '
                '\\forall n \\in \\mathbb{N}^*$; là dãy số giảm nếu $u_{n+1} < u_n, \\forall n \\in '
                '\\mathbb{N}^*$. Dãy $(u_n)$ gọi là bị chặn nếu tồn tại $m, M \\in \\mathbb{R}$ sao cho $m '
                '\\le u_n \\le M, \\forall n \\in \\mathbb{N}^*$.',
  'theory': '1. Để xét tính tăng, giảm của dãy số $(u_n)$, ta xét dấu của hiệu $H = u_{n+1} - u_n$: nếu $H > '
            '0$ thì dãy tăng; nếu $H < 0$ thì dãy giảm. 2. Nếu $u_n > 0, \\forall n \\in \\mathbb{N}^*$, ta '
            'có thể so sánh tỉ số $\\dfrac{u_{n+1}}{u_n}$ với $1$.',
  'formulas': [{'category': 'Tính đơn điệu và bị chặn của dãy số',
                'items': [{'name': 'Dãy số tăng',
                           'formula': '$u_{n+1} - u_n > 0, \\quad \\forall n \\in \\mathbb{N}^*$'},
                          {'name': 'Dãy số giảm',
                           'formula': '$u_{n+1} - u_n < 0, \\quad \\forall n \\in \\mathbb{N}^*$'},
                          {'name': 'Dãy số bị chặn',
                           'formula': '$\\exists m, M \\in \\mathbb{R}: m \\le u_n \\le M, \\quad \\forall n '
                                      '\\in \\mathbb{N}^*$'}]}],
  'example': 'Cho dãy số $(u_n)$ với $u_n = \\dfrac{n}{n + 1}$. Chứng minh $(u_n)$ là dãy số tăng và bị '
             'chặn.',
  'example_answer': 'Ta có $u_{n+1} - u_n = \\dfrac{n + 1}{n + 2} - \\dfrac{n}{n + 1} = \\dfrac{(n + 1)^2 - '
                    'n(n + 2)}{(n + 1)(n + 2)} = \\dfrac{1}{(n + 1)(n + 2)} > 0, \\forall n \\in '
                    '\\mathbb{N}^*$ nên $(u_n)$ là dãy tăng. Mặt khác $0 < \\dfrac{n}{n + 1} < 1, \\forall n '
                    '\\in \\mathbb{N}^*$ nên $(u_n)$ bị chặn.',
  'real_life': 'Mô tả số lượng tế bào phân chia theo từng thế hệ, dãy số Fibonacci trong tự nhiên và dư nợ '
               'trả góp hàng tháng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = 2n + 1$ ($n \\in \\mathbb{N}^*$). Số hạng '
                 'thứ $5$ của dãy số là:',
            'options': ['$u_5 = 11$', '$u_5 = 9$', '$u_5 = 10$', '$u_5 = 13$'],
            'answer': 0,
            'solution': 'Thay $n = 5$ vào công thức $u_n = 2n + 1$ ta được $u_5 = 2 \\cdot 5 + 1 = 11$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dãy số $(u_n)$ được gọi là dãy số tăng nếu với mọi $n \\in \\mathbb{N}^*$ ta có:',
            'options': ['$u_{n+1} < u_n$', '$u_{n+1} > u_n$', '$u_{n+1} = u_n$', '$u_{n+1} \\le u_n$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, dãy số $(u_n)$ là dãy số tăng nếu $u_{n+1} > u_n$ với mọi $n \\in '
                        '\\mathbb{N}^*$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 5: Dãy số**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Dãy số tăng**?',
            'options': ['$u_{n+1} - u_n < 0, \\quad \\forall n \\in \\mathbb{N}^*$',
                        '$\\exists m, M \\in \\mathbb{R}: m \\le u_n \\le M, \\quad \\forall n \\in '
                        '\\mathbb{N}^*$',
                        '$u_{n+1} - u_n > 0, \\quad \\forall n \\in \\mathbb{N}^*$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 5: Dãy số, **Dãy số tăng** được xác định bởi: '
                        '$u_{n+1} - u_n > 0, \\quad \\forall n \\in \\mathbb{N}^*$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Dãy số**, nội dung/biểu thức $u_{n+1} - u_n < 0, \\quad \\forall n \\in '
                 '\\mathbb{N}^*$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Dãy số tăng', 'Dãy số bị chặn', 'Đổi độ và radian', 'Dãy số giảm'],
            'answer': 3,
            'solution': 'Trong Bài 5: Dãy số, biểu thức/quy tắc $u_{n+1} - u_n < 0, \\quad \\forall n \\in '
                        '\\mathbb{N}^*$ chính là nội dung của **Dãy số giảm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các dãy số $(u_n)$ cho bởi số hạng tổng quát dưới đây, dãy số nào là dãy số giảm?',
            'options': ['$u_n = \\dfrac{1}{n}$', '$u_n = 3n - 2$', '$u_n = n^2$', '$u_n = 2^n$'],
            'answer': 0,
            'solution': 'Với $u_n = \\dfrac{1}{n}$, ta có $u_{n+1} - u_n = \\dfrac{1}{n + 1} - \\dfrac{1}{n} '
                        '= -\\dfrac{1}{n(n + 1)} < 0, \\forall n \\in \\mathbb{N}^*$, nên dãy giảm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Dãy số** (Chương II: Dãy số. Cấp số cộng và cấp số nhân), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Nhận biết được dãy số, số hạng đầu $u_1$, số hạng tổng quát $u_n$ và cách cho dãy '
                        'số bằng công thức hoặc hệ thức truy hồi.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 5: Dãy số: Nhận biết được dãy số, số hạng đầu $u_1$, '
                        'số hạng tổng quát $u_n$ và cách cho dãy số bằng công thức hoặc hệ thức truy hồi.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho dãy số $(u_n)$ xác định bởi $u_n = \\dfrac{2n + 1}{n + 1}$ với $n \\in \\mathbb{N}^*$. '
                 'Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Số hạng đầu tiên của dãy số là $u_1 = \\dfrac{3}{2}$.',
                           'Ta có $u_n = 2 - \\dfrac{1}{n + 1}$ với mọi $n \\in \\mathbb{N}^*$.',
                           'Dãy số $(u_n)$ là một dãy số giảm.',
                           'Dãy số $(u_n)$ bị chặn trên bởi $2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $u_1 = \\dfrac{2 \\cdot 1 + 1}{1 + 1} = \\dfrac{3}{2}$. b) Đúng vì '
                        '$\\dfrac{2(n + 1) - 1}{n + 1} = 2 - \\dfrac{1}{n + 1}$. c) Sai vì $u_{n+1} - u_n = '
                        '\\dfrac{1}{(n + 1)(n + 2)} > 0$ nên dãy tăng. d) Đúng vì $u_n = 2 - \\dfrac{1}{n + '
                        '1} < 2, \\forall n \\in \\mathbb{N}^*$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 5: Dãy số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được dãy số, số hạng đầu '
                           '$u_1$, số hạng tổng quát $u_n$ và cách cho dãy số bằng công thức hoặc hệ thức '
                           'truy hồi.',
                           'Quy tắc/công thức **Dãy số tăng** trong bài được xác định bởi: $u_{n+1} - u_n > '
                           '0, \\quad \\forall n \\in \\mathbb{N}^*$.',
                           'Trong mọi trường hợp, **Dãy số tăng** luôn được tính bằng công thức $a^\\circ = '
                           '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 5: Dãy số.',
                           'Với bài toán minh họa: “Cho dãy số $(u_n)$ với $u_n = \\dfrac{n}{n + 1}$. Chứng '
                           'minh $(u_n)$ là dãy số tăng và bị chặn.”, lời giải đúng là: Ta có $u_{n+1} - u_n '
                           '= \\dfrac{n + 1}{n + 2} - \\dfrac{n}{n + 1} = \\dfrac{(n + 1)^2 - n(n + 2)}{(n + '
                           '1)(n + 2)} = \\dfrac{1}{(n + 1)(n + 2)} > 0, \\forall n \\in \\mathbb{N}^*$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Dãy số. b) **Đúng** theo công thức '
                        'trọng tâm **Dãy số tăng** ($u_{n+1} - u_n > 0, \\quad \\forall n \\in '
                        '\\mathbb{N}^*$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                        '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức '
                        'của nội dung khác, không phải quy tắc chung của **Dãy số tăng**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 5: Dãy số** để giải quyết tình huống sau: Cho dãy số $(u_n)$ với '
                 '$u_n = \\dfrac{n}{n + 1}$. Chứng minh $(u_n)$ là dãy số tăng và bị chặn. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Ta có $u_{n+1} - u_n = \\dfrac{n + 1}{n + 2} - \\dfrac{n}{n + 1} = \\dfrac{(n + '
                        '1)^2 - n(n + 2)}{(n + 1)(n + 2)} = \\dfrac{1}{(n + 1)(n + 2)} > 0, \\forall n \\in '
                        '\\mathbb{N}^*$...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Dãy số: Ta có $u_{n+1} - u_n = \\dfrac{n + 1}{n + 2} '
                        '- \\dfrac{n}{n + 1} = \\dfrac{(n + 1)^2 - n(n + 2)}{(n + 1)(n + 2)} = \\dfrac{1}{(n '
                        '+ 1)(n + 2)} > 0, \\forall n \\in \\mathbb{N}^*$ nên $(u_n)$ là dãy tăng. Mặt khác '
                        '$0 < \\dfrac{n}{n + 1} < 1, \\forall n \\in \\mathbb{N}^*$ nên $(u_n)$ bị chặn.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho dãy số $(u_n)$ xác định bởi hệ thức truy hồi $u_1 = 2$ và $u_{n+1} = 2u_n - 1$ với mọi '
                 '$n \\ge 1$. Tính số hạng $u_4$.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Ta tính lần lượt: $u_2 = 2 \\cdot 2 - 1 = 3$; $u_3 = 2 \\cdot 3 - 1 = 5$; $u_4 = 2 '
                        '\\cdot 5 - 1 = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch02-day-so-cap-so',
  'context_title': 'Chương II: Dãy số. Cấp số cộng và cấp số nhân',
  'context': 'Chương II · SGK Toán 11: Dãy số, cấp số cộng và cấp số nhân.',
  'title': 'Bài 6: Cấp số cộng',
  'icon': '➕',
  'description': 'Định nghĩa cấp số cộng, công sai, số hạng tổng quát, tính chất các số hạng và tổng n số '
                 'hạng đầu của một cấp số cộng.',
  'requirements': ['Nhận biết được một dãy số là cấp số cộng và xác định được số hạng đầu $u_1$, công sai '
                   '$d$.',
                   'Sử dụng được công thức số hạng tổng quát $u_n = u_1 + (n - 1)d$ và công thức tổng $S_n$.',
                   'Giải quyết được các bài toán thực tế có quy luật tăng hoặc giảm đều theo cấp số cộng.'],
  'definition': 'Cấp số cộng là một dãy số (hữu hạn hoặc vô hạn), trong đó kể từ số hạng thứ hai, mỗi số '
                'hạng đều bằng số hạng đứng ngay trước nó cộng với một số không đổi $d$. Số $d$ được gọi là '
                'công sai của cấp số cộng: $u_{n+1} = u_n + d$ ($n \\in \\mathbb{N}^*$).',
  'theory': '1. Số hạng tổng quát: $u_n = u_1 + (n - 1)d$ với $n \\ge 2$. 2. Tính chất trung bình cộng: $u_k '
            '= \\dfrac{u_{k-1} + u_{k+1}}{2}$ với $k \\ge 2$. 3. Tổng $n$ số hạng đầu: $S_n = \\dfrac{n(u_1 '
            '+ u_n)}{2} = \\dfrac{n[2u_1 + (n - 1)d]}{2}$.',
  'formulas': [{'category': 'Công thức cấp số cộng',
                'items': [{'name': 'Định nghĩa công sai',
                           'formula': '$u_{n+1} = u_n + d \\Leftrightarrow d = u_{n+1} - u_n$'},
                          {'name': 'Số hạng tổng quát',
                           'formula': '$u_n = u_1 + (n - 1)d \\quad (n \\ge 2)$'},
                          {'name': 'Tính chất ba số hạng liên tiếp',
                           'formula': '$u_k = \\dfrac{u_{k-1} + u_{k+1}}{2} \\quad (k \\ge 2)$'},
                          {'name': 'Tổng n số hạng đầu',
                           'formula': '$S_n = \\dfrac{n(u_1 + u_n)}{2} = \\dfrac{n[2u_1 + (n - 1)d]}{2}$'}]}],
  'example': 'Cho cấp số cộng $(u_n)$ có $u_1 = 3$ và công sai $d = 4$. Tính $u_{10}$ và tổng $S_{10}$.',
  'example_answer': 'Ta có $u_{10} = u_1 + 9d = 3 + 9 \\cdot 4 = 39$. Tổng $10$ số hạng đầu là $S_{10} = '
                    '\\dfrac{10(u_1 + u_{10})}{2} = \\dfrac{10 \\cdot (3 + 39)}{2} = 210$.',
  'real_life': 'Tính tổng số ghế trong rạp hát có số ghế mỗi hàng tăng đều, hoặc tính số tiền tiết kiệm gửi '
               'góp tăng đều hàng tháng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho cấp số cộng $(u_n)$ có số hạng đầu $u_1 = 2$ và công sai $d = 3$. Giá trị của $u_4$ '
                 'bằng:',
            'options': ['$14$', '$11$', '$8$', '$9$'],
            'answer': 1,
            'solution': 'Áp dụng công thức $u_4 = u_1 + 3d = 2 + 3 \\cdot 3 = 11$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dãy số nào dưới đây là một cấp số cộng?',
            'options': ['$1; 2; 4; 8; 16$', '$1; 3; 6; 10; 15$', '$1; 4; 7; 10; 13$', '$2; 4; 7; 11; 16$'],
            'answer': 2,
            'solution': 'Dãy $1; 4; 7; 10; 13$ có hiệu hai số hạng liên tiếp luôn bằng $d = 3$ nên là cấp số '
                        'cộng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 6: Cấp số cộng**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Định nghĩa công sai**?',
            'options': ['$u_n = u_1 + (n - 1)d \\quad (n \\ge 2)$',
                        '$u_k = \\dfrac{u_{k-1} + u_{k+1}}{2} \\quad (k \\ge 2)$',
                        '$S_n = \\dfrac{n(u_1 + u_n)}{2} = \\dfrac{n[2u_1 + (n - 1)d]}{2}$',
                        '$u_{n+1} = u_n + d \\Leftrightarrow d = u_{n+1} - u_n$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 6: Cấp số cộng, **Định nghĩa công sai** được '
                        'xác định bởi: $u_{n+1} = u_n + d \\Leftrightarrow d = u_{n+1} - u_n$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Cấp số cộng**, nội dung/biểu thức $u_n = u_1 + (n - 1)d \\quad (n \\ge 2)$ '
                 'là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Số hạng tổng quát',
                        'Định nghĩa công sai',
                        'Tính chất ba số hạng liên tiếp',
                        'Tổng n số hạng đầu'],
            'answer': 0,
            'solution': 'Trong Bài 6: Cấp số cộng, biểu thức/quy tắc $u_n = u_1 + (n - 1)d \\quad (n \\ge '
                        '2)$ chính là nội dung của **Số hạng tổng quát**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho cấp số cộng $(u_n)$ có $u_1 = -2$ và $u_6 = 13$. Công sai $d$ của cấp số cộng bằng:',
            'options': ['$2$', '$3$', '$4$', '$-3$'],
            'answer': 1,
            'solution': 'Ta có $u_6 = u_1 + 5d \\Leftrightarrow 13 = -2 + 5d \\Leftrightarrow 5d = 15 '
                        '\\Leftrightarrow d = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Cấp số cộng** (Chương II: Dãy số. Cấp số cộng và cấp số nhân), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Nhận biết được một dãy số là cấp số cộng và xác định được số hạng đầu $u_1$, công '
                        'sai $d$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 6: Cấp số cộng: Nhận biết được một dãy số là cấp số '
                        'cộng và xác định được số hạng đầu $u_1$, công sai $d$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho cấp số cộng $(u_n)$ có số hạng tổng quát $u_n = 3n + 1$ ($n \\in \\mathbb{N}^*$). Xét '
                 'tính đúng sai của các mệnh đề sau:',
            'statements': ['Số hạng đầu của cấp số cộng là $u_1 = 4$.',
                           'Công sai của cấp số cộng là $d = 3$.',
                           'Số $100$ là số hạng thứ $34$ của cấp số cộng.',
                           'Tổng của $10$ số hạng đầu tiên của cấp số cộng bằng $175$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $u_1 = 3 \\cdot 1 + 1 = 4$. b) Đúng vì $u_{n+1} - u_n = 3$. c) Sai vì '
                        '$3n + 1 = 100 \\Leftrightarrow n = 33$ (số hạng thứ 33). d) Đúng vì $u_{10} = 31 '
                        '\\Rightarrow S_{10} = \\dfrac{10(4 + 31)}{2} = 175$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 6: Cấp số cộng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được một dãy số là cấp '
                           'số cộng và xác định được số hạng đầu $u_1$, công sai $d$.',
                           'Quy tắc/công thức **Định nghĩa công sai** trong bài được xác định bởi: $u_{n+1} '
                           '= u_n + d \\Leftrightarrow d = u_{n+1} - u_n$.',
                           'Trong mọi trường hợp, **Định nghĩa công sai** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 6: Cấp số cộng.',
                           'Với bài toán minh họa: “Cho cấp số cộng $(u_n)$ có $u_1 = 3$ và công sai $d = '
                           '4$. Tính $u_{10}$ và tổng $S_{10}$.”, lời giải đúng là: Ta có $u_{10} = u_1 + 9d '
                           '= 3 + 9 \\cdot 4 = 39$. Tổng $10$ số hạng đầu là $S_{10} = \\dfrac{10(u_1 + '
                           'u_{10})}{2} = \\dfrac{10 \\cdot (3 + 39)}{2} = 210$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Cấp số cộng. b) **Đúng** theo công thức '
                        'trọng tâm **Định nghĩa công sai** ($u_{n+1} = u_n + d \\Leftrightarrow d = u_{n+1} '
                        '- u_n$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                        '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức '
                        'của nội dung khác, không phải quy tắc chung của **Định nghĩa công sai**. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 6: Cấp số cộng** để giải quyết tình huống sau: Cho cấp số cộng '
                 '$(u_n)$ có $u_1 = 3$ và công sai $d = 4$. Tính $u_{10}$ và tổng $S_{10}$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Ta có $u_{10} = u_1 + 9d = 3 + 9 \\cdot 4 = 39$. Tổng $10$ số hạng đầu là $S_{10} = '
                        '\\dfrac{10(u_1 + u_{10})}{2} = \\dfrac{10 \\cdot (3 + 39)}{2} = 210$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Cấp số cộng: Ta có $u_{10} = u_1 + 9d = 3 + 9 \\cdot '
                        '4 = 39$. Tổng $10$ số hạng đầu là $S_{10} = \\dfrac{10(u_1 + u_{10})}{2} = '
                        '\\dfrac{10 \\cdot (3 + 39)}{2} = 210$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một rạp hát có $15$ hàng ghế. Hàng thứ nhất có $20$ ghế, mỗi hàng sau có nhiều hơn hàng '
                 'ngay trước nó $2$ ghế. Hỏi rạp hát đó có tất cả bao nhiêu ghế?',
            'answer': ['510'],
            'unit': None,
            'solution': 'Số ghế ở các hàng lập thành cấp số cộng với $u_1 = 20, d = 2, n = 15$. Tổng số ghế '
                        'là $S_{15} = \\dfrac{15 \\cdot [2 \\cdot 20 + (15 - 1) \\cdot 2]}{2} = 15 \\cdot 34 '
                        '= 510$ (ghế).',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch02-day-so-cap-so',
  'context_title': 'Chương II: Dãy số. Cấp số cộng và cấp số nhân',
  'context': 'Chương II · SGK Toán 11: Dãy số, cấp số cộng và cấp số nhân.',
  'title': 'Bài 7: Cấp số nhân',
  'icon': '✖️',
  'description': 'Định nghĩa cấp số nhân, công bội, số hạng tổng quát, tính chất nhân và tổng n số hạng đầu '
                 'của một cấp số nhân.',
  'requirements': ['Nhận biết được một dãy số là cấp số nhân và xác định được số hạng đầu $u_1$, công bội '
                   '$q$.',
                   'Áp dụng được công thức số hạng tổng quát $u_n = u_1 \\cdot q^{n-1}$ và tổng $S_n = '
                   '\\dfrac{u_1(1 - q^n)}{1 - q}$ ($q \\ne 1$).',
                   'Giải quyết được bài toán lãi kép, sự nhân đôi của vi khuẩn hoặc sự suy giảm theo tỉ lệ '
                   'phần trăm.'],
  'definition': 'Cấp số nhân là một dãy số (hữu hạn hoặc vô hạn), trong đó kể từ số hạng thứ hai, mỗi số '
                'hạng đều bằng tích của số hạng đứng ngay trước nó với một số không đổi $q$. Số $q$ được gọi '
                'là công bội của cấp số nhân: $u_{n+1} = u_n \\cdot q$ ($n \\in \\mathbb{N}^*$).',
  'theory': '1. Số hạng tổng quát: $u_n = u_1 \\cdot q^{n-1}$ ($n \\ge 2$). 2. Tính chất: $u_k^2 = u_{k-1} '
            '\\cdot u_{k+1}$ ($k \\ge 2$). 3. Tổng $n$ số hạng đầu (khi $q \\ne 1$): $S_n = \\dfrac{u_1(1 - '
            'q^n)}{1 - q}$.',
  'formulas': [{'category': 'Công thức cấp số nhân',
                'items': [{'name': 'Định nghĩa công bội', 'formula': '$u_{n+1} = u_n \\cdot q$'},
                          {'name': 'Số hạng tổng quát',
                           'formula': '$u_n = u_1 \\cdot q^{n-1} \\quad (n \\ge 2)$'},
                          {'name': 'Tính chất ba số hạng liên tiếp',
                           'formula': '$u_k^2 = u_{k-1} \\cdot u_{k+1} \\quad (k \\ge 2)$'},
                          {'name': 'Tổng n số hạng đầu (q ≠ 1)',
                           'formula': '$S_n = \\dfrac{u_1(1 - q^n)}{1 - q} = \\dfrac{u_1(q^n - 1)}{q - '
                                      '1}$'}]}],
  'example': 'Cho cấp số nhân $(u_n)$ có $u_1 = 2$ và công bội $q = 3$. Tính $u_5$ và tổng $S_5$.',
  'example_answer': 'Ta có $u_5 = u_1 \\cdot q^4 = 2 \\cdot 3^4 = 162$. Tổng $5$ số hạng đầu là $S_5 = '
                    '\\dfrac{2(3^5 - 1)}{3 - 1} = 3^5 - 1 = 242$.',
  'real_life': 'Tính lãi suất kép ngân hàng, sự tăng trưởng dân số, chu kì phân đôi của tế bào và bài toán '
               'hạt thóc trên bàn cờ vua.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho cấp số nhân $(u_n)$ có số hạng đầu $u_1 = 3$ và công bội $q = 2$. Giá trị của $u_4$ '
                 'bằng:',
            'options': ['$18$', '$12$', '$24$', '$48$'],
            'answer': 2,
            'solution': 'Ta có $u_4 = u_1 \\cdot q^3 = 3 \\cdot 2^3 = 24$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dãy số nào dưới đây là một cấp số nhân?',
            'options': ['$2; 4; 6; 8$', '$1; 2; 3; 4$', '$1; 4; 9; 16$', '$2; 6; 18; 54$'],
            'answer': 3,
            'solution': 'Dãy $2; 6; 18; 54$ có tỉ số hai số hạng liên tiếp luôn bằng $q = 3$ nên là cấp số '
                        'nhân.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 7: Cấp số nhân**, công thức hoặc quy tắc nào sau đây '
                 'biểu diễn đúng **Định nghĩa công bội**?',
            'options': ['$u_{n+1} = u_n \\cdot q$',
                        '$u_n = u_1 \\cdot q^{n-1} \\quad (n \\ge 2)$',
                        '$u_k^2 = u_{k-1} \\cdot u_{k+1} \\quad (k \\ge 2)$',
                        '$S_n = \\dfrac{u_1(1 - q^n)}{1 - q} = \\dfrac{u_1(q^n - 1)}{q - 1}$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 7: Cấp số nhân, **Định nghĩa công bội** được '
                        'xác định bởi: $u_{n+1} = u_n \\cdot q$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Cấp số nhân**, nội dung/biểu thức $u_n = u_1 \\cdot q^{n-1} \\quad (n \\ge '
                 '2)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa công bội',
                        'Số hạng tổng quát',
                        'Tính chất ba số hạng liên tiếp',
                        'Tổng n số hạng đầu (q ≠ 1)'],
            'answer': 1,
            'solution': 'Trong Bài 7: Cấp số nhân, biểu thức/quy tắc $u_n = u_1 \\cdot q^{n-1} \\quad (n '
                        '\\ge 2)$ chính là nội dung của **Số hạng tổng quát**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho cấp số nhân $(u_n)$ có $u_1 = 1$ và $q = 2$. Tổng của $6$ số hạng đầu tiên $S_6$ bằng:',
            'options': ['$64$', '$31$', '$63$', '$127$'],
            'answer': 2,
            'solution': 'Áp dụng công thức $S_6 = \\dfrac{u_1(q^6 - 1)}{q - 1} = \\dfrac{1 \\cdot (2^6 - '
                        '1)}{2 - 1} = 63$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Cấp số nhân** (Chương II: Dãy số. Cấp số cộng và cấp số nhân), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Nhận biết được một dãy số là cấp số nhân và xác định được số hạng đầu $u_1$, công '
                        'bội $q$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 7: Cấp số nhân: Nhận biết được một dãy số là cấp số '
                        'nhân và xác định được số hạng đầu $u_1$, công bội $q$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho cấp số nhân $(u_n)$ có các số hạng dương thỏa mãn $u_1 = 2$ và $u_3 = 18$. Xét tính '
                 'đúng sai của các mệnh đề sau:',
            'statements': ['Công bội của cấp số nhân là $q = 3$.',
                           'Số hạng thứ hai của cấp số nhân là $u_2 = 6$.',
                           'Số hạng thứ năm của cấp số nhân là $u_5 = 162$.',
                           'Tổng $4$ số hạng đầu tiên của cấp số nhân bằng $100$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $u_3 = u_1 q^2 \\Rightarrow q^2 = 9 \\Rightarrow q = 3$ (do $u_n > 0$). '
                        'b) Đúng vì $u_2 = 2 \\cdot 3 = 6$. c) Đúng vì $u_5 = 2 \\cdot 3^4 = 162$. d) Sai vì '
                        '$S_4 = \\dfrac{2(3^4 - 1)}{3 - 1} = 80 \\ne 100$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 7: Cấp số nhân**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được một dãy số là cấp '
                           'số nhân và xác định được số hạng đầu $u_1$, công bội $q$.',
                           'Quy tắc/công thức **Định nghĩa công bội** trong bài được xác định bởi: $u_{n+1} '
                           '= u_n \\cdot q$.',
                           'Trong mọi trường hợp, **Định nghĩa công bội** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 7: Cấp số nhân.',
                           'Với bài toán minh họa: “Cho cấp số nhân $(u_n)$ có $u_1 = 2$ và công bội $q = '
                           '3$. Tính $u_5$ và tổng $S_5$.”, lời giải đúng là: Ta có $u_5 = u_1 \\cdot q^4 = '
                           '2 \\cdot 3^4 = 162$. Tổng $5$ số hạng đầu là $S_5 = \\dfrac{2(3^5 - 1)}{3 - 1} = '
                           '3^5 - 1 = 242$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Cấp số nhân. b) **Đúng** theo công thức '
                        'trọng tâm **Định nghĩa công bội** ($u_{n+1} = u_n \\cdot q$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa công bội**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 7: Cấp số nhân** để giải quyết tình huống sau: Cho cấp số nhân '
                 '$(u_n)$ có $u_1 = 2$ và công bội $q = 3$. Tính $u_5$ và tổng $S_5$. Kết quả và hướng giải '
                 'nào dưới đây là **đúng**?',
            'options': ['Ta có $u_5 = u_1 \\cdot q^4 = 2 \\cdot 3^4 = 162$. Tổng $5$ số hạng đầu là $S_5 = '
                        '\\dfrac{2(3^5 - 1)}{3 - 1} = 3^5 - 1 = 242$.',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Cấp số nhân: Ta có $u_5 = u_1 \\cdot q^4 = 2 \\cdot '
                        '3^4 = 162$. Tổng $5$ số hạng đầu là $S_5 = \\dfrac{2(3^5 - 1)}{3 - 1} = 3^5 - 1 = '
                        '242$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số dương $x$ sao cho ba số $4; x; 9$ theo thứ tự đó lập thành một cấp số nhân.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Theo tính chất cấp số nhân, ta có $x^2 = 4 \\cdot 9 = 36$. Vì $x > 0$ nên $x = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch03-thong-ke-ghep-nhom',
  'context_title': 'Chương III: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm',
  'context': 'Chương III · SGK Toán 11: Mẫu số liệu ghép nhóm và các số đặc trưng đo xu thế trung tâm (số '
             'trung bình, trung vị, tứ phân vị, mốt).',
  'title': 'Bài 8: Mẫu số liệu ghép nhóm',
  'icon': '📋',
  'description': 'Khái niệm mẫu số liệu ghép nhóm, cách chuyển mẫu số liệu không ghép nhóm sang ghép nhóm, '
                 'tần số, độ dài nhóm và giá trị đại diện.',
  'requirements': ['Hiểu được mục đích ghép nhóm số liệu để thuận tiện cho việc tổ chức, đọc và phân tích '
                   'mẫu số liệu lớn.',
                   'Xác định được đầu mút trái, đầu mút phải, độ dài nhóm $d = a_{i+1} - a_i$ và giá trị đại '
                   'diện $x_i = \\dfrac{a_i + a_{i+1}}{2}$.',
                   'Lập được bảng tần số ghép nhóm từ mẫu số liệu thô.'],
  'definition': 'Mẫu số liệu ghép nhóm là mẫu số liệu cho dưới dạng bảng tần số của các nhóm số liệu, trong '
                'đó mỗi nhóm có dạng $[a; b)$ gồm các giá trị $x$ thỏa mãn $a \\le x < b$ (nhóm cuối cùng có '
                'thể lấy cả đầu mút phải $[a; b]$).',
  'theory': '1. Độ dài của nhóm $[a_i; a_{i+1})$ là $d_i = a_{i+1} - a_i$. 2. Giá trị đại diện của nhóm '
            '$[a_i; a_{i+1})$ là trung bình cộng hai đầu mút: $x_i = \\dfrac{a_i + a_{i+1}}{2}$. 3. Tổng các '
            'tần số của tất cả các nhóm bằng cỡ mẫu: $n = n_1 + n_2 + \\dots + n_k$.',
  'formulas': [{'category': 'Các thông số của nhóm số liệu [a; b)',
                'items': [{'name': 'Độ dài nhóm', 'formula': '$d = b - a$'},
                          {'name': 'Giá trị đại diện của nhóm', 'formula': '$x_i = \\dfrac{a + b}{2}$'},
                          {'name': 'Cỡ mẫu', 'formula': '$n = n_1 + n_2 + \\dots + n_k$'}]}],
  'example': 'Cho nhóm số liệu $[150; 160)$ trong bảng chiều cao học sinh. Tìm độ dài nhóm và giá trị đại '
             'diện của nhóm đó.',
  'example_answer': 'Độ dài của nhóm $[150; 160)$ là $d = 160 - 150 = 10$. Giá trị đại diện của nhóm là $x_i '
                    '= \\dfrac{150 + 160}{2} = 155$.',
  'real_life': 'Phân loại học sinh theo các mức điểm thi, thống kê cơ cấu dân số theo các nhóm độ tuổi lao '
               'động.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Độ dài của nhóm số liệu $[12; 18)$ bằng bao nhiêu?',
            'options': ['$15$', '$30$', '$12$', '$6$'],
            'answer': 3,
            'solution': 'Độ dài của nhóm $[a; b)$ là $b - a = 18 - 12 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị đại diện của nhóm $[40; 50)$ là:',
            'options': ['$45$', '$10$', '$40$', '$50$'],
            'answer': 0,
            'solution': 'Giá trị đại diện là $\\dfrac{40 + 50}{2} = 45$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 8: Mẫu số liệu ghép nhóm**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Độ dài nhóm**?',
            'options': ['$x_i = \\dfrac{a + b}{2}$',
                        '$d = b - a$',
                        '$n = n_1 + n_2 + \\dots + n_k$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 8: Mẫu số liệu ghép nhóm, **Độ dài nhóm** '
                        'được xác định bởi: $d = b - a$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Mẫu số liệu ghép nhóm**, nội dung/biểu thức $x_i = \\dfrac{a + b}{2}$ là '
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Độ dài nhóm', 'Cỡ mẫu', 'Giá trị đại diện của nhóm', 'Đổi độ và radian'],
            'answer': 2,
            'solution': 'Trong Bài 8: Mẫu số liệu ghép nhóm, biểu thức/quy tắc $x_i = \\dfrac{a + b}{2}$ '
                        'chính là nội dung của **Giá trị đại diện của nhóm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một giá trị số liệu $x = 20$ sẽ được xếp vào nhóm nào trong các nhóm $[10; 15), [15; 20), '
                 '[20; 25), [25; 30)$?',
            'options': ['$[15; 20)$', 'Cả hai nhóm $[15; 20)$ và $[20; 25)$', '$[25; 30)$', '$[20; 25)$'],
            'answer': 3,
            'solution': 'Nhóm $[20; 25)$ gồm các giá trị $x$ thỏa mãn $20 \\le x < 25$ nên $x = 20$ thuộc '
                        'nhóm $[20; 25)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Mẫu số liệu ghép nhóm** (Chương III: Các số đặc trưng đo xu thế trung tâm '
                 'của mẫu số liệu ghép nhóm), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và '
                 'bản chất kiến thức của bài?',
            'options': ['Hiểu được mục đích ghép nhóm số liệu để thuận tiện cho việc tổ chức, đọc và phân '
                        'tích mẫu số liệu lớn.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 8: Mẫu số liệu ghép nhóm: Hiểu được mục đích ghép nhóm '
                        'số liệu để thuận tiện cho việc tổ chức, đọc và phân tích mẫu số liệu lớn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Khảo sát thời gian hoàn thành bài tập (phút) của một lớp học thu được bảng ghép nhóm: $[5; '
                 '10)$ có 8 em; $[10; 15)$ có 14 em; $[15; 20)$ có 12 em; $[20; 25)$ có 6 em. Xét tính đúng '
                 'sai của các mệnh đề sau:',
            'statements': ['Cỡ mẫu của cuộc khảo sát là $n = 40$ học sinh.',
                           'Độ dài của mỗi nhóm trong bảng đều bằng $5$ phút.',
                           'Giá trị đại diện của nhóm $[15; 20)$ là $17,5$ phút.',
                           'Số học sinh hoàn thành bài tập dưới $15$ phút là $14$ em.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $n = 8 + 14 + 12 + 6 = 40$. b) Đúng vì $10 - 5 = 15 - 10 = 20 - 15 = 25 '
                        '- 20 = 5$. c) Đúng vì $\\dfrac{15 + 20}{2} = 17,5$. d) Sai vì dưới $15$ phút gồm '
                        'hai nhóm $[5; 10)$ và $[10; 15)$ có $8 + 14 = 22$ em.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 8: Mẫu số liệu ghép '
                 'nhóm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được mục đích ghép nhóm số '
                           'liệu để thuận tiện cho việc tổ chức, đọc và phân tích mẫu số liệu lớn.',
                           'Quy tắc/công thức **Độ dài nhóm** trong bài được xác định bởi: $d = b - a$.',
                           'Trong mọi trường hợp, **Độ dài nhóm** luôn được tính bằng công thức $a^\\circ = '
                           '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 8: Mẫu số liệu ghép nhóm.',
                           'Với bài toán minh họa: “Cho nhóm số liệu $[150; 160)$ trong bảng chiều cao học '
                           'sinh. Tìm độ dài nhóm và giá trị đại diện của nhóm đó.”, lời giải đúng là: Độ '
                           'dài của nhóm $[150; 160)$ là $d = 160 - 150 = 10$. Giá trị đại diện của nhóm là '
                           '$x_i = \\dfrac{150 + 160}{2} = 155$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Mẫu số liệu ghép nhóm. b) **Đúng** theo '
                        'công thức trọng tâm **Độ dài nhóm** ($d = b - a$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Độ dài nhóm**. d) **Đúng** theo lời giải ví dụ minh '
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 8: Mẫu số liệu ghép nhóm** để giải quyết tình huống sau: Cho nhóm '
                 'số liệu $[150; 160)$ trong bảng chiều cao học sinh. Tìm độ dài nhóm và giá trị đại diện '
                 'của nhóm đó. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Độ dài của nhóm $[150; 160)$ là $d = 160 - 150 = 10$. Giá trị đại diện của nhóm là '
                        '$x_i = \\dfrac{150 + 160}{2} = 155$.',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Mẫu số liệu ghép nhóm: Độ dài của nhóm $[150; 160)$ '
                        'là $d = 160 - 150 = 10$. Giá trị đại diện của nhóm là $x_i = \\dfrac{150 + 160}{2} '
                        '= 155$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bảng tần số ghép nhóm gồm 4 nhóm có tần số lần lượt là $7; 12; x; 9$. Biết cỡ mẫu là '
                 '$n = 40$. Tìm giá trị của $x$.',
            'answer': ['12'],
            'unit': None,
            'solution': 'Tổng các tần số bằng cỡ mẫu: $7 + 12 + x + 9 = 40 \\Leftrightarrow 28 + x = 40 '
                        '\\Leftrightarrow x = 12$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch03-thong-ke-ghep-nhom',
  'context_title': 'Chương III: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm',
  'context': 'Chương III · SGK Toán 11: Mẫu số liệu ghép nhóm và các số đặc trưng đo xu thế trung tâm (số '
             'trung bình, trung vị, tứ phân vị, mốt).',
  'title': 'Bài 9: Các số đặc trưng đo xu thế trung tâm',
  'icon': '🎯',
  'description': 'Công thức tính và ý nghĩa của số trung bình, trung vị, tứ phân vị và mốt của mẫu số liệu '
                 'ghép nhóm.',
  'requirements': ['Tính được số trung bình cộng $\\bar{x}$ của mẫu số liệu ghép nhóm thông qua giá trị đại '
                   'diện các nhóm.',
                   'Xác định được nhóm chứa trung vị, nhóm chứa tứ phân vị, nhóm chứa mốt và tính được $M_e, '
                   'Q_1, Q_2, Q_3, M_o$.',
                   'Giải thích được ý nghĩa của các số đặc trưng đo xu thế trung tâm trong thực tiễn.'],
  'definition': 'Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm gồm: số trung bình '
                '$\\bar{x}$ (tính theo giá trị đại diện), trung vị $M_e$ (chia mẫu thành 2 phần bằng nhau), '
                'tứ phân vị $Q_1, Q_2, Q_3$ (chia mẫu thành 4 phần bằng nhau) và mốt $M_o$ (nằm trong nhóm '
                'có tần số lớn nhất).',
  'theory': '1. Số trung bình: $\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$. 2. Trung vị '
            '$M_e = Q_2 = u_m + \\dfrac{\\dfrac{n}{2} - C}{n_m}(u_{m+1} - u_m)$, trong đó $[u_m; u_{m+1})$ '
            'là nhóm chứa trung vị, $n_m$ là tần số nhóm đó, $C$ là tần số tích lũy của các nhóm đứng trước. '
            '3. Mốt $M_o = u_m + \\dfrac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})}(u_{m+1} - u_m)$ '
            'trên nhóm có tần số lớn nhất.',
  'formulas': [{'category': 'Các số đặc trưng đo xu thế trung tâm',
                'items': [{'name': 'Số trung bình',
                           'formula': '$\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$'},
                          {'name': 'Trung vị (Tứ phân vị thứ hai)',
                           'formula': '$M_e = Q_2 = u_m + \\dfrac{\\dfrac{n}{2} - C}{n_m} \\cdot (u_{m+1} - '
                                      'u_m)$'},
                          {'name': 'Tứ phân vị thứ r (r = 1, 2, 3)',
                           'formula': '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} '
                                      '- u_m)$'},
                          {'name': 'Mốt',
                           'formula': '$M_o = u_m + \\dfrac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - '
                                      'n_{m+1})} \\cdot (u_{m+1} - u_m)$'}]}],
  'example': 'Điểm kiểm tra của 20 học sinh được ghép thành 3 nhóm: $[4; 6)$ có 4 em; $[6; 8)$ có 10 em; '
             '$[8; 10]$ có 6 em. Tính điểm trung bình $\\bar{x}$ và trung vị $M_e$.',
  'example_answer': 'Giá trị đại diện là $5; 7; 9$. Điểm trung bình $\\bar{x} = \\dfrac{4 \\cdot 5 + 10 '
                    '\\cdot 7 + 6 \\cdot 9}{20} = \\dfrac{144}{20} = 7,2$. Cỡ mẫu $n = 20 \\Rightarrow '
                    '\\dfrac{n}{2} = 10$ thuộc nhóm $[6; 8)$ ($n_m = 10, C = 4$). Trung vị $M_e = 6 + '
                    '\\dfrac{10 - 4}{10} \\cdot (8 - 6) = 7,2$.',
  'real_life': 'Báo cáo mức lương trung vị của ngành công nghệ thông tin và xác định cỡ giày phổ biến nhất '
               '(mốt) để nhập hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong mẫu số liệu ghép nhóm có các nhóm cùng độ dài, nhóm chứa mốt $M_o$ là nhóm:',
            'options': ['Có tần số lớn nhất.',
                        'Có tần số nhỏ nhất.',
                        'Đứng ở vị trí đầu tiên.',
                        'Đứng ở vị trí cuối cùng.'],
            'answer': 0,
            'solution': 'Nhóm chứa mốt của mẫu số liệu ghép nhóm (với các nhóm có cùng độ dài) là nhóm có '
                        'tần số lớn nhất.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tứ phân vị thứ hai $Q_2$ của mẫu số liệu ghép nhóm luôn bằng số đặc trưng nào dưới đây?',
            'options': ['Số trung bình $\\bar{x}$',
                        'Trung vị $M_e$',
                        'Mốt $M_o$',
                        'Tứ phân vị thứ nhất $Q_1$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, tứ phân vị thứ hai $Q_2$ chính là trung vị $M_e$ của mẫu số liệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 9: Các số đặc trưng đo xu thế trung tâm**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Số trung bình**?',
            'options': ['$M_e = Q_2 = u_m + \\dfrac{\\dfrac{n}{2} - C}{n_m} \\cdot (u_{m+1} - u_m)$',
                        '$Q_r = u_m + \\dfrac{\\dfrac{r \\cdot n}{4} - C}{n_m} \\cdot (u_{m+1} - u_m)$',
                        '$\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$',
                        '$M_o = u_m + \\dfrac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})} \\cdot '
                        '(u_{m+1} - u_m)$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 9: Các số đặc trưng đo xu thế trung tâm, **Số '
                        'trung bình** được xác định bởi: $\\bar{x} = \\dfrac{n_1 x_1 + n_2 x_2 + \\dots + '
                        'n_k x_k}{n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Các số đặc trưng đo xu thế trung tâm**, nội dung/biểu thức $M_e = Q_2 = u_m '
                 '+ \\dfrac{\\dfrac{n}{2} - C}{n_m} \\cdot (u_{m+1} - u_m)$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Số trung bình',
                        'Tứ phân vị thứ r (r = 1, 2, 3)',
                        'Mốt',
                        'Trung vị (Tứ phân vị thứ hai)'],
            'answer': 3,
            'solution': 'Trong Bài 9: Các số đặc trưng đo xu thế trung tâm, biểu thức/quy tắc $M_e = Q_2 = '
                        'u_m + \\dfrac{\\dfrac{n}{2} - C}{n_m} \\cdot (u_{m+1} - u_m)$ chính là nội dung của '
                        '**Trung vị (Tứ phân vị thứ hai)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một mẫu số liệu ghép nhóm gồm 3 nhóm: $[0; 10)$ có tần số $2$; $[10; 20)$ có tần số $5$; '
                 '$[20; 30)$ có tần số $3$. Số trung bình $\\bar{x}$ của mẫu số liệu là:',
            'options': ['$16$', '$15$', '$14$', '$18$'],
            'answer': 0,
            'solution': 'Giá trị đại diện là $5; 15; 25$ và $n = 10$. Số trung bình $\\bar{x} = \\dfrac{2 '
                        '\\cdot 5 + 5 \\cdot 15 + 3 \\cdot 25}{10} = \\dfrac{160}{10} = 16$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Các số đặc trưng đo xu thế trung tâm** (Chương III: Các số đặc trưng đo '
                 'xu thế trung tâm của mẫu số liệu ghép nhóm), khẳng định nào sau đây phản ánh **đúng** yêu '
                 'cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Tính được số trung bình cộng $\\bar{x}$ của mẫu số liệu ghép nhóm thông qua giá trị '
                        'đại diện các nhóm.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 9: Các số đặc trưng đo xu thế trung tâm: Tính được số '
                        'trung bình cộng $\\bar{x}$ của mẫu số liệu ghép nhóm thông qua giá trị đại diện các '
                        'nhóm.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho mẫu số liệu ghép nhóm về chiều cao (cm) của $30$ cây giống gồm 3 nhóm: $[10; 20)$ có '
                 '$6$ cây; $[20; 30)$ có $15$ cây; $[30; 40)$ có $9$ cây. Xét tính đúng sai của các mệnh đề '
                 'sau:',
            'statements': ['Nhóm chứa mốt của mẫu số liệu là nhóm $[20; 30)$.',
                           'Số trung bình của mẫu số liệu là $\\bar{x} = 26\\text{ cm}$.',
                           'Nhóm chứa trung vị $M_e$ là nhóm $[20; 30)$.',
                           'Giá trị trung vị của mẫu số liệu là $M_e = 25\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì nhóm $[20; 30)$ có tần số lớn nhất bằng $15$. b) Đúng vì $\\bar{x} = '
                        '\\dfrac{6 \\cdot 15 + 15 \\cdot 25 + 9 \\cdot 35}{30} = 26$. c) Đúng vì '
                        '$\\dfrac{n}{2} = 15$, tần số tích lũy nhóm 1 là $6 < 15 \\le 21$. d) Sai vì $M_e = '
                        '20 + \\dfrac{15 - 6}{15} \\cdot 10 = 26\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 9: Các số đặc trưng đo '
                 'xu thế trung tâm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Tính được số trung bình cộng '
                           '$\\bar{x}$ của mẫu số liệu ghép nhóm thông qua giá trị đại diện các nhóm.',
                           'Quy tắc/công thức **Số trung bình** trong bài được xác định bởi: $\\bar{x} = '
                           '\\dfrac{n_1 x_1 + n_2 x_2 + \\dots + n_k x_k}{n}$.',
                           'Trong mọi trường hợp, **Số trung bình** luôn được tính bằng công thức $a^\\circ '
                           '= \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 9: Các số đặc trưng đo xu thế trung tâm.',
                           'Với bài toán minh họa: “Điểm kiểm tra của 20 học sinh được ghép thành 3 nhóm: '
                           '$[4; 6)$ có 4 em; $[6; 8)$ có 10 em; $[8; 10]$ có 6 em. Tính điểm trung bình '
                           '$\\bar{x}$...”, lời giải đúng là: Giá trị đại diện là $5; 7; 9$. Điểm trung bình '
                           '$\\bar{x} = \\dfrac{4 \\cdot 5 + 10 \\cdot 7 + 6 \\cdot 9}{20} = '
                           '\\dfrac{144}{20} = 7,2$. Cỡ mẫu $n = 20 \\Rightarrow \\dfrac{n}{2} = 10$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Các số đặc trưng đo xu thế trung tâm. '
                        'b) **Đúng** theo công thức trọng tâm **Số trung bình** ($\\bar{x} = \\dfrac{n_1 x_1 '
                        '+ n_2 x_2 + \\dots + n_k x_k}{n}$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi '
                        'a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Số trung bình**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 9: Các số đặc trưng đo xu thế trung tâm** để giải quyết tình '
                 'huống sau: Điểm kiểm tra của 20 học sinh được ghép thành 3 nhóm: $[4; 6)$ có 4 em; $[6; '
                 '8)$ có 10 em; $[8; 10]$ có 6 em. Tính điểm trung bình $\\bar{x}$ và trung vị $M_e$. Kết '
                 'quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Giá trị đại diện là $5; 7; 9$. Điểm trung bình $\\bar{x} = \\dfrac{4 \\cdot 5 + 10 '
                        '\\cdot 7 + 6 \\cdot 9}{20} = \\dfrac{144}{20} = 7,2$. Cỡ mẫu $n = 20 \\Rightarrow '
                        '\\dfrac{n}{2} = 10$...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Các số đặc trưng đo xu thế trung tâm: Giá trị đại '
                        'diện là $5; 7; 9$. Điểm trung bình $\\bar{x} = \\dfrac{4 \\cdot 5 + 10 \\cdot 7 + 6 '
                        '\\cdot 9}{20} = \\dfrac{144}{20} = 7,2$. Cỡ mẫu $n = 20 \\Rightarrow \\dfrac{n}{2} '
                        '= 10$ thuộc nhóm $[6; 8)$ ($n_m = 10, C = 4$). Trung vị $M_e = 6 + \\dfrac{10 - '
                        '4}{10} \\cdot (8 - 6) = 7,2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho mẫu số liệu ghép nhóm gồm 3 nhóm liên tiếp: $[10; 20)$ có tần số $5$; $[20; 30)$ có '
                 'tần số $10$; $[30; 40)$ có tần số $5$. Tính mốt $M_o$ của mẫu số liệu ghép nhóm này.',
            'answer': ['25'],
            'unit': None,
            'solution': 'Nhóm chứa mốt là $[20; 30)$ với $u_m = 20, n_m = 10, n_{m-1} = 5, n_{m+1} = 5$. Áp '
                        'dụng công thức: $M_o = 20 + \\dfrac{10 - 5}{(10 - 5) + (10 - 5)} \\cdot 10 = 25$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch04-quan-he-song-song',
  'context_title': 'Chương IV: Quan hệ song song trong không gian',
  'context': 'Chương IV · SGK Toán 11: Đường thẳng và mặt phẳng trong không gian, quan hệ song song và phép '
             'chiếu song song.',
  'title': 'Bài 10: Đường thẳng và mặt phẳng trong không gian',
  'icon': '📐',
  'description': 'Các tính chất thừa nhận của hình học không gian, các cách xác định mặt phẳng, hình chóp, '
                 'hình tứ diện và cách tìm giao tuyến của hai mặt phẳng.',
  'requirements': ['Nắm vững các tính chất thừa nhận của hình học không gian và $4$ cách xác định một mặt '
                   'phẳng.',
                   'Tìm được giao tuyến của hai mặt phẳng phân biệt và giao điểm của đường thẳng với mặt '
                   'phẳng.',
                   'Nhận biết được các yếu tố đỉnh, cạnh bên, mặt bên, mặt đáy của hình chóp và hình tứ '
                   'diện.'],
  'definition': 'Điểm, đường thẳng và mặt phẳng là ba đối tượng cơ bản của hình học không gian. Một mặt '
                'phẳng hoàn toàn được xác định khi biết nó đi qua ba điểm không thẳng hàng, hoặc qua một '
                'đường thẳng và một điểm không thuộc đường thẳng đó, hoặc qua hai đường thẳng cắt nhau.',
  'theory': '1. Nếu một đường thẳng có hai điểm phân biệt thuộc một mặt phẳng thì mọi điểm của đường thẳng '
            'đều thuộc mặt phẳng đó. 2. Nếu hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường '
            'thẳng chung duy nhất (gọi là giao tuyến) đi qua mọi điểm chung của hai mặt phẳng đó.',
  'formulas': [{'category': 'Kí hiệu và phương pháp tìm giao tuyến, giao điểm',
                'items': [{'name': 'Điểm thuộc đường thẳng và mặt phẳng',
                           'formula': '$A \\in d, \\quad A \\in (P), \\quad d \\subset (P)$'},
                          {'name': 'Tìm giao tuyến hai mặt phẳng',
                           'formula': '$\\begin{cases} A \\in (\\alpha) \\cap (\\beta) \\\\ B \\in (\\alpha) '
                                      '\\cap (\\beta) \\end{cases} \\Rightarrow (\\alpha) \\cap (\\beta) = '
                                      'AB$'},
                          {'name': 'Số mặt và cạnh của tứ diện',
                           'formula': '$\\text{Tứ diện } ABCD \\text{ có } 4 \\text{ đỉnh, } 6 \\text{ cạnh, '
                                      '} 4 \\text{ mặt tam giác}$'}]}],
  'example': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Tìm giao tuyến của hai mặt '
             'phẳng $(SAC)$ và $(SBD)$.',
  'example_answer': 'Ta có $S$ là điểm chung thứ nhất của $(SAC)$ và $(SBD)$. Trong mặt phẳng $(ABCD)$, gọi '
                    '$O = AC \\cap BD$ thì $O \\in AC \\subset (SAC)$ và $O \\in BD \\subset (SBD)$ nên $O$ '
                    'là điểm chung thứ hai. Vậy $(SAC) \\cap (SBD) = SO$.',
  'real_life': 'Ứng dụng nguyên lí ba điểm không thẳng hàng xác định một mặt phẳng để làm giá đỡ máy ảnh 3 '
               'chân (tripod) luôn đứng vững trên mọi địa hình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Qua ba điểm phân biệt không thẳng hàng trong không gian, có bao nhiêu mặt phẳng đi qua cả '
                 'ba điểm đó?',
            'options': ['$2$', '$1$', '$3$', 'Vô số'],
            'answer': 1,
            'solution': 'Theo tính chất thừa nhận, có một và chỉ một mặt phẳng đi qua ba điểm không thẳng '
                        'hàng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình tứ diện có tất cả bao nhiêu cạnh?',
            'options': ['$4$', '$8$', '$6$', '$5$'],
            'answer': 2,
            'solution': 'Hình tứ diện $ABCD$ có $4$ đỉnh, $4$ mặt và $6$ cạnh ($AB, AC, AD, BC, BD, CD$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 10: Đường thẳng và mặt phẳng trong không gian**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Điểm thuộc đường thẳng và mặt phẳng**?',
            'options': ['$\\begin{cases} A \\in (\\alpha) \\cap (\\beta) \\\\ B \\in (\\alpha) \\cap '
                        '(\\beta) \\end{cases} \\Rightarrow (\\alpha) \\cap (\\beta) = AB$',
                        '$\\text{Tứ diện } ABCD \\text{ có } 4 \\text{ đỉnh, } 6 \\text{ cạnh, } 4 \\text{ '
                        'mặt tam giác}$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$A \\in d, \\quad A \\in (P), \\quad d \\subset (P)$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 10: Đường thẳng và mặt phẳng trong không '
                        'gian, **Điểm thuộc đường thẳng và mặt phẳng** được xác định bởi: $A \\in d, \\quad '
                        'A \\in (P), \\quad d \\subset (P)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Đường thẳng và mặt phẳng trong không gian**, nội dung/biểu thức '
                 '$\\begin{cases} A \\in (\\alpha) \\cap (\\beta) \\\\ B \\in (\\alpha) \\cap (\\beta) '
                 '\\end{cases} \\Rightarrow (\\alpha) \\cap (\\beta) = AB$ là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Tìm giao tuyến hai mặt phẳng',
                        'Điểm thuộc đường thẳng và mặt phẳng',
                        'Số mặt và cạnh của tứ diện',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 10: Đường thẳng và mặt phẳng trong không gian, biểu thức/quy tắc '
                        '$\\begin{cases} A \\in (\\alpha) \\cap (\\beta) \\\\ B \\in (\\alpha) \\cap '
                        '(\\beta) \\end{cases} \\Rightarrow (\\alpha) \\cap (\\beta) = AB$ chính là nội dung '
                        'của **Tìm giao tuyến hai mặt phẳng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là tứ giác có hai đường chéo $AC$ và $BD$ cắt nhau '
                 'tại $I$. Giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$ là đường thẳng:',
            'options': ['$SA$', '$SI$', '$SC$', '$AB$'],
            'answer': 1,
            'solution': 'Hai mặt phẳng $(SAC)$ và $(SBD)$ có điểm chung $S$ và $I = AC \\cap BD$ nên giao '
                        'tuyến là đường thẳng $SI$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Đường thẳng và mặt phẳng trong không gian** (Chương IV: Quan hệ song '
                 'song trong không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản '
                 'chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Nắm vững các tính chất thừa nhận của hình học không gian và $4$ cách xác định một '
                        'mặt phẳng.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 10: Đường thẳng và mặt phẳng trong không gian: Nắm '
                        'vững các tính chất thừa nhận của hình học không gian và $4$ cách xác định một mặt '
                        'phẳng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là tứ giác lồi có các cặp cạnh đối không song song. '
                 'Gọi $M$ là trung điểm của $SA$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Hình chóp $S.ABCD$ có $4$ mặt bên và $1$ mặt đáy.',
                           'Đường thẳng $BM$ nằm trong mặt phẳng $(SAB)$.',
                           'Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng $SO$ với $O = AC '
                           '\\cap BD$.',
                           'Trong mặt phẳng $(ABCD)$, nếu $E = AB \\cap CD$ thì giao tuyến của $(SAB)$ và '
                           '$(SCD)$ là đường thẳng $SE$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $B \\in (SAB)$ và $M \\in SA \\subset (SAB)$. c) Sai vì $O = AC '
                        '\\cap BD$ là điểm chung của $(SAC)$ và $(SBD)$, không thuộc $(SAB)$ và $(SCD)$. d) '
                        'Đúng vì $E \\in AB \\subset (SAB)$ và $E \\in CD \\subset (SCD)$ nên $(SAB) \\cap '
                        '(SCD) = SE$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 10: Đường thẳng và mặt '
                 'phẳng trong không gian**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nắm vững các tính chất thừa nhận '
                           'của hình học không gian và $4$ cách xác định một mặt phẳng.',
                           'Quy tắc/công thức **Điểm thuộc đường thẳng và mặt phẳng** trong bài được xác '
                           'định bởi: $A \\in d, \\quad A \\in (P), \\quad d \\subset (P)$.',
                           'Trong mọi trường hợp, **Điểm thuộc đường thẳng và mặt phẳng** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 10: Đường thẳng và mặt phẳng '
                           'trong không gian.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành '
                           'tâm $O$. Tìm giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$.”, lời giải đúng '
                           'là: Ta có $S$ là điểm chung thứ nhất của $(SAC)$ và $(SBD)$. Trong mặt phẳng '
                           '$(ABCD)$, gọi $O = AC \\cap BD$ thì $O \\in AC \\subset (SAC)$ và $O \\in BD '
                           '\\subset (SBD)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Đường thẳng và mặt phẳng trong không '
                        'gian. b) **Đúng** theo công thức trọng tâm **Điểm thuộc đường thẳng và mặt phẳng** '
                        '($A \\in d, \\quad A \\in (P), \\quad d \\subset (P)$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Điểm thuộc đường thẳng và mặt phẳng**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 10: Đường thẳng và mặt phẳng trong không gian** để giải quyết '
                 'tình huống sau: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Tìm giao '
                 'tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Ta có $S$ là điểm chung thứ nhất của $(SAC)$ và $(SBD)$. Trong mặt phẳng $(ABCD)$, '
                        'gọi $O = AC \\cap BD$ thì $O \\in AC \\subset (SAC)$ và $O \\in BD \\subset '
                        '(SBD)$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Đường thẳng và mặt phẳng trong không gian: Ta có $S$ '
                        'là điểm chung thứ nhất của $(SAC)$ và $(SBD)$. Trong mặt phẳng $(ABCD)$, gọi $O = '
                        'AC \\cap BD$ thì $O \\in AC \\subset (SAC)$ và $O \\in BD \\subset (SBD)$ nên $O$ '
                        'là điểm chung thứ hai. Vậy $(SAC) \\cap (SBD) = SO$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chóp có đáy là đa giác đều $7$ cạnh thì có tất cả bao nhiêu mặt (tính cả mặt bên '
                 'và mặt đáy)?',
            'answer': ['8'],
            'unit': None,
            'solution': 'Hình chóp có đáy là $n$-giác có $n$ mặt bên và $1$ mặt đáy, tổng cộng là $n + 1 = 7 '
                        '+ 1 = 8$ mặt.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch04-quan-he-song-song',
  'context_title': 'Chương IV: Quan hệ song song trong không gian',
  'context': 'Chương IV · SGK Toán 11: Đường thẳng và mặt phẳng trong không gian, quan hệ song song và phép '
             'chiếu song song.',
  'title': 'Bài 11: Hai đường thẳng song song',
  'icon': '⏸️',
  'description': 'Vị trí tương đối của hai đường thẳng trong không gian (đồng phẳng, chéo nhau), tính chất '
                 'bắc cầu và định lí về giao tuyến của ba mặt phẳng.',
  'requirements': ['Phân biệt được hai đường thẳng song song (đồng phẳng và không có điểm chung) với hai '
                   'đường thẳng chéo nhau (không đồng phẳng).',
                   'Vận dụng được định lí về ba đường giao tuyến của ba mặt phẳng đôi một cắt nhau.',
                   'Chứng minh được hai đường thẳng song song trong không gian dựa vào đường trung bình hoặc '
                   'định lí Thalès.'],
  'definition': 'Hai đường thẳng trong không gian gọi là song song nếu chúng nằm trong cùng một mặt phẳng và '
                'không có điểm chung. Hai đường thẳng gọi là chéo nhau nếu không có mặt phẳng nào chứa cả '
                'hai đường thẳng đó.',
  'theory': '1. Qua một điểm không thuộc đường thẳng $a$, có một và chỉ một đường thẳng song song với $a$. '
            '2. Định lí ba đường giao tuyến: Nếu ba mặt phẳng đôi một cắt nhau theo ba giao tuyến phân biệt '
            'thì ba giao tuyến ấy hoặc đồng quy hoặc đôi một song song. 3. Hai đường thẳng phân biệt cùng '
            'song song với đường thẳng thứ ba thì song song với nhau.',
  'formulas': [{'category': 'Định lí giao tuyến song song',
                'items': [{'name': 'Tính chất bắc cầu',
                           'formula': '$a \\parallel c \\text{ và } b \\parallel c \\quad (a \\ne b) '
                                      '\\Rightarrow a \\parallel b$'},
                          {'name': 'Hệ quả giao tuyến song song',
                           'formula': '$\\begin{cases} a \\subset (\\alpha), b \\subset (\\beta) \\\\ a '
                                      '\\parallel b \\\\ (\\alpha) \\cap (\\beta) = d \\end{cases} '
                                      '\\Rightarrow d \\parallel a \\parallel b$'}]}],
  'example': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Tìm giao tuyến của hai mặt phẳng '
             '$(SAB)$ và $(SCD)$.',
  'example_answer': 'Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng '
                    'song song $AB \\parallel CD$. Vậy giao tuyến của $(SAB)$ và $(SCD)$ là đường thẳng $Sx$ '
                    'đi qua $S$ và song song với $AB, CD$.',
  'real_life': 'Các mép tường thẳng đứng trong phòng học đôi một song song, trong khi đường cầu vượt và '
               'đường cao tốc bên dưới là hai đường thẳng chéo nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong không gian, hai đường thẳng chéo nhau là hai đường thẳng:',
            'options': ['Cùng nằm trong một mặt phẳng và không có điểm chung.',
                        'Có đúng một điểm chung.',
                        'Không cùng nằm trong bất kì mặt phẳng nào.',
                        'Vuông góc với nhau trong cùng một mặt phẳng.'],
            'answer': 2,
            'solution': 'Hai đường thẳng chéo nhau là hai đường thẳng không đồng phẳng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Đường thẳng $MN$ '
                 'song song với đường thẳng nào dưới đây?',
            'options': ['$AD$', '$BD$', '$CD$', '$BC$'],
            'answer': 3,
            'solution': 'Trong tam giác $ABC$, $MN$ là đường trung bình nên $MN \\parallel BC$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 11: Hai đường thẳng song song**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Tính chất bắc cầu**?',
            'options': ['$a \\parallel c \\text{ và } b \\parallel c \\quad (a \\ne b) \\Rightarrow a '
                        '\\parallel b$',
                        '$\\begin{cases} a \\subset (\\alpha), b \\subset (\\beta) \\\\ a \\parallel b \\\\ '
                        '(\\alpha) \\cap (\\beta) = d \\end{cases} \\Rightarrow d \\parallel a \\parallel b$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$l = R \\cdot \\alpha \\quad (\\alpha \\text{ tính bằng rad})$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 11: Hai đường thẳng song song, **Tính chất '
                        'bắc cầu** được xác định bởi: $a \\parallel c \\text{ và } b \\parallel c \\quad (a '
                        '\\ne b) \\Rightarrow a \\parallel b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Hai đường thẳng song song**, nội dung/biểu thức $\\begin{cases} a \\subset '
                 '(\\alpha), b \\subset (\\beta) \\\\ a \\parallel b \\\\ (\\alpha) \\cap (\\beta) = d '
                 '\\end{cases} \\Rightarrow d \\parallel a \\parallel b$ là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Tính chất bắc cầu',
                        'Hệ quả giao tuyến song song',
                        'Đổi độ và radian',
                        'Độ dài cung tròn'],
            'answer': 1,
            'solution': 'Trong Bài 11: Hai đường thẳng song song, biểu thức/quy tắc $\\begin{cases} a '
                        '\\subset (\\alpha), b \\subset (\\beta) \\\\ a \\parallel b \\\\ (\\alpha) \\cap '
                        '(\\beta) = d \\end{cases} \\Rightarrow d \\parallel a \\parallel b$ chính là nội '
                        'dung của **Hệ quả giao tuyến song song**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng '
                 '$(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và:',
            'options': ['Song song với $AB$.',
                        'Song song với $AC$.',
                        'Song song với $AD$.',
                        'Cắt $BC$ tại trung điểm của $BC$.'],
            'answer': 2,
            'solution': 'Vì $AD \\subset (SAD), BC \\subset (SBC)$ và $AD \\parallel BC$, nên giao tuyến của '
                        '$(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và song song với $AD, BC$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Hai đường thẳng song song** (Chương IV: Quan hệ song song trong không '
                 'gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Phân biệt được hai đường thẳng song song (đồng phẳng và không có điểm chung) với '
                        'hai đường thẳng chéo nhau (không đồng phẳng).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 11: Hai đường thẳng song song: Phân biệt được hai '
                        'đường thẳng song song (đồng phẳng và không có điểm chung) với hai đường thẳng chéo '
                        'nhau (không đồng phẳng).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tứ diện $ABCD$. Gọi $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$. '
                 'Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Đường thẳng $MN$ song song với đường thẳng $AC$.',
                           'Hai đường thẳng $MN$ và $PQ$ song song với nhau.',
                           'Tứ giác $MNPQ$ là một hình bình hành.',
                           'Hai đường thẳng $MP$ và $NQ$ chéo nhau.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $MN$ là đường trung bình của $\\triangle ABC$. b) Đúng vì $MN \\parallel '
                        'AC$ và $PQ \\parallel AC$. c) Đúng vì $MN \\parallel PQ$ và $MN = PQ = '
                        '\\dfrac{1}{2}AC$. d) Sai vì $MP$ và $NQ$ là hai đường chéo của hình bình hành '
                        '$MNPQ$ nên cắt nhau tại trung điểm mỗi đường.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 11: Hai đường thẳng '
                 'song song**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phân biệt được hai đường thẳng '
                           'song song (đồng phẳng và không có điểm chung) với hai đường thẳng chéo nhau '
                           '(không đồng phẳng).',
                           'Quy tắc/công thức **Tính chất bắc cầu** trong bài được xác định bởi: $a '
                           '\\parallel c \\text{ và } b \\parallel c \\quad (a \\ne b) \\Rightarrow a '
                           '\\parallel b$.',
                           'Trong mọi trường hợp, **Tính chất bắc cầu** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 11: Hai đường thẳng song song.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. '
                           'Tìm giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$.”, lời giải đúng là: Hai mặt '
                           'phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song '
                           'song $AB \\parallel CD$. Vậy giao tuyến của $(SAB)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Hai đường thẳng song song. b) **Đúng** '
                        'theo công thức trọng tâm **Tính chất bắc cầu** ($a \\parallel c \\text{ và } b '
                        '\\parallel c \\quad (a \\ne b) \\Rightarrow a \\parallel b$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Tính chất bắc cầu**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 11: Hai đường thẳng song song** để giải quyết tình huống sau: Cho '
                 'hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Tìm giao tuyến của hai mặt phẳng '
                 '$(SAB)$ và $(SCD)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng '
                        'song song $AB \\parallel CD$. Vậy giao tuyến của $(SAB)$ và $(SCD)$ là đ...',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Hai đường thẳng song song: Hai mặt phẳng $(SAB)$ và '
                        '$(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AB \\parallel '
                        'CD$. Vậy giao tuyến của $(SAB)$ và $(SCD)$ là đường thẳng $Sx$ đi qua $S$ và song '
                        'song với $AB, CD$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tứ diện $ABCD$ có $AC = 8\\text{ cm}$ và $BD = 6\\text{ cm}$. Gọi $M, N, P, Q$ lần '
                 'lượt là trung điểm của $AB, BC, CD, DA$. Tính chu vi của tứ giác $MNPQ$ (đơn vị: cm).',
            'answer': ['14'],
            'unit': None,
            'solution': 'Theo tính chất đường trung bình, ta có $MN = PQ = \\dfrac{1}{2}AC = 4\\text{ cm}$ '
                        'và $NP = QM = \\dfrac{1}{2}BD = 3\\text{ cm}$. Chu vi hình bình hành $MNPQ$ là $4 + '
                        '3 + 4 + 3 = 14\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch04-quan-he-song-song',
  'context_title': 'Chương IV: Quan hệ song song trong không gian',
  'context': 'Chương IV · SGK Toán 11: Đường thẳng và mặt phẳng trong không gian, quan hệ song song và phép '
             'chiếu song song.',
  'title': 'Bài 12: Đường thẳng và mặt phẳng song song',
  'icon': '🛫',
  'description': 'Vị trí tương đối giữa đường thẳng và mặt phẳng, dấu hiệu nhận biết và tính chất của đường '
                 'thẳng song song với mặt phẳng.',
  'requirements': ['Nhận biết được $3$ vị trí tương đối giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$: nằm '
                   'trong, cắt nhau và song song.',
                   "Vận dụng định lí dấu hiệu nhận biết: nếu $d \\not\\subset (\\alpha), d \\parallel d'$ và "
                   "$d' \\subset (\\alpha)$ thì $d \\parallel (\\alpha)$.",
                   'Sử dụng tính chất của đường thẳng song song với mặt phẳng để xác định giao tuyến và '
                   'thiết diện.'],
  'definition': 'Đường thẳng $d$ được gọi là song song với mặt phẳng $(\\alpha)$ nếu $d$ và $(\\alpha)$ '
                'không có điểm chung nào, kí hiệu $d \\parallel (\\alpha)$.',
  'theory': '1. Định lí nhận biết: Nếu đường thẳng $d$ không nằm trong mặt phẳng $(\\alpha)$ và $d$ song '
            "song với một đường thẳng $d'$ nằm trong $(\\alpha)$ thì $d \\parallel (\\alpha)$. 2. Định lí "
            'tính chất: Nếu $d \\parallel (\\alpha)$ thì mọi mặt phẳng $(\\beta)$ chứa $d$ và cắt '
            "$(\\alpha)$ theo giao tuyến $d'$ đều có $d' \\parallel d$.",
  'formulas': [{'category': 'Đường thẳng song song với mặt phẳng',
                'items': [{'name': 'Dấu hiệu nhận biết',
                           'formula': "$\\begin{cases} d \\not\\subset (\\alpha) \\\\ d \\parallel d' \\\\ "
                                      "d' \\subset (\\alpha) \\end{cases} \\Rightarrow d \\parallel "
                                      '(\\alpha)$'},
                          {'name': 'Tính chất giao tuyến',
                           'formula': '$\\begin{cases} d \\parallel (\\alpha) \\\\ d \\subset (\\beta) \\\\ '
                                      "(\\alpha) \\cap (\\beta) = d' \\end{cases} \\Rightarrow d' \\parallel "
                                      'd$'}]}],
  'example': 'Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Chứng minh $MN '
             '\\parallel (BCD)$.',
  'example_answer': 'Trong tam giác $ABC$, $M, N$ là trung điểm của $AB, AC$ nên $MN \\parallel BC$. Mà $MN '
                    '\\not\\subset (BCD)$ và $BC \\subset (BCD)$, suy ra $MN \\parallel (BCD)$.',
  'real_life': 'Sử dụng thước thủy (ống nước thăng bằng) để kiểm tra xà ngang hoặc mặt bàn có song song với '
               'mặt sàn nhà hay không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đường thẳng $d$ và mặt phẳng $(\\alpha)$ được gọi là song song với nhau nếu:',
            'options': ['Chúng có đúng một điểm chung.',
                        'Chúng có hai điểm chung phân biệt.',
                        'Chúng có vô số điểm chung.',
                        'Chúng không có điểm chung.'],
            'answer': 3,
            'solution': 'Theo định nghĩa, $d \\parallel (\\alpha)$ khi và chỉ khi $d$ và $(\\alpha)$ không '
                        'có điểm chung.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường thẳng $a$ không nằm trong mặt phẳng $(P)$. Điều kiện đủ để $a \\parallel (P)$ '
                 'là:',
            'options': ['$a$ song song với một đường thẳng $b$ nằm trong $(P)$.',
                        '$a$ cắt một đường thẳng $b$ nằm trong $(P)$.',
                        '$a$ chéo với một đường thẳng $b$ nằm trong $(P)$.',
                        '$a$ vuông góc với một đường thẳng $b$ nằm trong $(P)$.'],
            'answer': 0,
            'solution': 'Theo định lí nhận biết, nếu $a \\not\\subset (P), a \\parallel b$ và $b \\subset '
                        '(P)$ thì $a \\parallel (P)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 12: Đường thẳng và mặt phẳng song song**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Dấu hiệu nhận biết**?',
            'options': ['$\\begin{cases} d \\parallel (\\alpha) \\\\ d \\subset (\\beta) \\\\ (\\alpha) '
                        "\\cap (\\beta) = d' \\end{cases} \\Rightarrow d' \\parallel d$",
                        "$\\begin{cases} d \\not\\subset (\\alpha) \\\\ d \\parallel d' \\\\ d' \\subset "
                        '(\\alpha) \\end{cases} \\Rightarrow d \\parallel (\\alpha)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$l = R \\cdot \\alpha \\quad (\\alpha \\text{ tính bằng rad})$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 12: Đường thẳng và mặt phẳng song song, **Dấu '
                        'hiệu nhận biết** được xác định bởi: $\\begin{cases} d \\not\\subset (\\alpha) \\\\ '
                        "d \\parallel d' \\\\ d' \\subset (\\alpha) \\end{cases} \\Rightarrow d \\parallel "
                        '(\\alpha)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Đường thẳng và mặt phẳng song song**, nội dung/biểu thức $\\begin{cases} d '
                 "\\parallel (\\alpha) \\\\ d \\subset (\\beta) \\\\ (\\alpha) \\cap (\\beta) = d' "
                 "\\end{cases} \\Rightarrow d' \\parallel d$ là quy tắc hoặc công thức của mục nào sau đây?",
            'options': ['Dấu hiệu nhận biết', 'Đổi độ và radian', 'Tính chất giao tuyến', 'Độ dài cung tròn'],
            'answer': 2,
            'solution': 'Trong Bài 12: Đường thẳng và mặt phẳng song song, biểu thức/quy tắc $\\begin{cases} '
                        "d \\parallel (\\alpha) \\\\ d \\subset (\\beta) \\\\ (\\alpha) \\cap (\\beta) = d' "
                        "\\end{cases} \\Rightarrow d' \\parallel d$ chính là nội dung của **Tính chất giao "
                        'tuyến**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Đường thẳng $AB$ song song với mặt '
                 'phẳng nào dưới đây?',
            'options': ['$(SAC)$', '$(SBD)$', '$(SBC)$', '$(SCD)$'],
            'answer': 3,
            'solution': 'Vì $AB \\not\\subset (SCD), AB \\parallel CD$ và $CD \\subset (SCD)$ nên $AB '
                        '\\parallel (SCD)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Đường thẳng và mặt phẳng song song** (Chương IV: Quan hệ song song trong '
                 'không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Nhận biết được $3$ vị trí tương đối giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$: '
                        'nằm trong, cắt nhau và song song.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 12: Đường thẳng và mặt phẳng song song: Nhận biết được '
                        '$3$ vị trí tương đối giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$: nằm trong, cắt '
                        'nhau và song song.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tứ diện $ABCD$. Gọi $G_1, G_2$ lần lượt là trọng tâm của tam giác $ABC$ và tam giác '
                 '$ABD$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Gọi $M$ là trung điểm của $AB$ thì $G_1 \\in MC$ và $G_2 \\in MD$.',
                           'Tỉ số $\\dfrac{MG_1}{MC} = \\dfrac{MG_2}{MD} = \\dfrac{1}{3}$.',
                           'Đường thẳng $G_1G_2$ song song với đường thẳng $CD$.',
                           'Đường thẳng $G_1G_2$ cắt mặt phẳng $(BCD)$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng theo định nghĩa trọng tâm. b) Đúng vì tính chất trọng tâm tam giác. c) Đúng '
                        'theo định lí Thalès đảo trong $\\triangle MCD$. d) Sai vì $G_1G_2 \\parallel CD$ và '
                        '$CD \\subset (BCD)$ nên $G_1G_2 \\parallel (BCD)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 12: Đường thẳng và mặt '
                 'phẳng song song**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được $3$ vị trí tương '
                           'đối giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$: nằm trong, cắt nhau và song '
                           'song.',
                           'Quy tắc/công thức **Dấu hiệu nhận biết** trong bài được xác định bởi: '
                           "$\\begin{cases} d \\not\\subset (\\alpha) \\\\ d \\parallel d' \\\\ d' \\subset "
                           '(\\alpha) \\end{cases} \\Rightarrow d \\parallel (\\alpha)$.',
                           'Trong mọi trường hợp, **Dấu hiệu nhận biết** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 12: Đường thẳng và mặt phẳng song song.',
                           'Với bài toán minh họa: “Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm '
                           'của $AB$ và $AC$. Chứng minh $MN \\parallel (BCD)$.”, lời giải đúng là: Trong '
                           'tam giác $ABC$, $M, N$ là trung điểm của $AB, AC$ nên $MN \\parallel BC$. Mà $MN '
                           '\\not\\subset (BCD)$ và $BC \\subset (BCD)$, suy ra $MN \\parallel (BCD)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Đường thẳng và mặt phẳng song song. b) '
                        '**Đúng** theo công thức trọng tâm **Dấu hiệu nhận biết** ($\\begin{cases} d '
                        "\\not\\subset (\\alpha) \\\\ d \\parallel d' \\\\ d' \\subset (\\alpha) "
                        '\\end{cases} \\Rightarrow d \\parallel (\\alpha)$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Dấu hiệu nhận biết**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 12: Đường thẳng và mặt phẳng song song** để giải quyết tình huống '
                 'sau: Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Chứng minh '
                 '$MN \\parallel (BCD)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Trong tam giác $ABC$, $M, N$ là trung điểm của $AB, AC$ nên $MN \\parallel BC$. Mà '
                        '$MN \\not\\subset (BCD)$ và $BC \\subset (BCD)$, suy ra $MN \\parallel (BCD)$...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Đường thẳng và mặt phẳng song song: Trong tam giác '
                        '$ABC$, $M, N$ là trung điểm của $AB, AC$ nên $MN \\parallel BC$. Mà $MN '
                        '\\not\\subset (BCD)$ và $BC \\subset (BCD)$, suy ra $MN \\parallel (BCD)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tứ diện $ABCD$ có $CD = 12\\text{ cm}$. Gọi $G_1, G_2$ lần lượt là trọng tâm của tam '
                 'giác $ABC$ và tam giác $ABD$. Tính độ dài đoạn thẳng $G_1G_2$ (đơn vị: cm).',
            'answer': ['4'],
            'unit': None,
            'solution': 'Gọi $M$ là trung điểm của $AB$. Trong $\\triangle MCD$ ta có $\\dfrac{MG_1}{MC} = '
                        '\\dfrac{MG_2}{MD} = \\dfrac{1}{3} \\Rightarrow \\dfrac{G_1G_2}{CD} = \\dfrac{1}{3} '
                        '\\Rightarrow G_1G_2 = \\dfrac{12}{3} = 4\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch04-quan-he-song-song',
  'context_title': 'Chương IV: Quan hệ song song trong không gian',
  'context': 'Chương IV · SGK Toán 11: Đường thẳng và mặt phẳng trong không gian, quan hệ song song và phép '
             'chiếu song song.',
  'title': 'Bài 13: Hai mặt phẳng song song',
  'icon': '📚',
  'description': 'Định nghĩa, dấu hiệu nhận biết và tính chất của hai mặt phẳng song song, định lí Thalès '
                 'trong không gian, hình lăng trụ và hình hộp.',
  'requirements': ['Phát biểu và vận dụng được định lí dấu hiệu nhận biết hai mặt phẳng song song.',
                   'Nắm được tính chất giao tuyến của một mặt phẳng cắt hai mặt phẳng song song và định lí '
                   'Thalès trong không gian.',
                   'Nhận biết được các tính chất cơ bản của hình lăng trụ, hình hộp và hình chóp cụt.'],
  'definition': 'Hai mặt phẳng $(\\alpha)$ và $(\\beta)$ được gọi là song song với nhau nếu chúng không có '
                'điểm chung, kí hiệu $(\\alpha) \\parallel (\\beta)$. Hình lăng trụ là hình đa diện có hai '
                'mặt đáy nằm trên hai mặt phẳng song song và các cạnh bên đôi một song song.',
  'theory': '1. Dấu hiệu nhận biết: Nếu mặt phẳng $(\\alpha)$ chứa hai đường thẳng cắt nhau $a, b$ và cả $a, '
            'b$ đều song song với mặt phẳng $(\\beta)$ thì $(\\alpha) \\parallel (\\beta)$. 2. Tính chất: '
            'Cho hai mặt phẳng song song $(\\alpha) \\parallel (\\beta)$, nếu mặt phẳng $(\\gamma)$ cắt '
            '$(\\alpha)$ theo giao tuyến $a$ thì $(\\gamma)$ cũng cắt $(\\beta)$ theo giao tuyến $b$ và $a '
            '\\parallel b$.',
  'formulas': [{'category': 'Hai mặt phẳng song song và định lí Thalès',
                'items': [{'name': 'Dấu hiệu nhận biết',
                           'formula': '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ a '
                                      '\\parallel (\\beta), b \\parallel (\\beta) \\end{cases} \\Rightarrow '
                                      '(\\alpha) \\parallel (\\beta)$'},
                          {'name': 'Tính chất giao tuyến',
                           'formula': '$\\begin{cases} (\\alpha) \\parallel (\\beta) \\\\ (\\gamma) \\cap '
                                      '(\\alpha) = a, (\\gamma) \\cap (\\beta) = b \\end{cases} \\Rightarrow '
                                      'a \\parallel b$'},
                          {'name': 'Định lí Thalès trong không gian',
                           'formula': '$\\text{Ba mặt phẳng song song chắn trên } d_1, d_2 \\text{ các đoạn '
                                      'tương ứng tỉ lệ}$'}]}],
  'example': "Cho hình hộp $ABCD.A'B'C'D'$. Chứng minh hai mặt phẳng $(BDA')$ và $(B'D'C)$ song song với "
             'nhau.',
  'example_answer': "Tứ giác $BDD'B'$ là hình bình hành nên $BD \\parallel B'D' \\Rightarrow BD \\parallel "
                    "(B'D'C)$. Tứ giác $A'B'CD$ là hình bình hành nên $A'D \\parallel B'C \\Rightarrow A'D "
                    "\\parallel (B'D'C)$. Trong $(BDA')$, hai đường thẳng $BD$ và $A'D$ cắt nhau tại $D$, "
                    "nên $(BDA') \\parallel (B'D'C)$.",
  'real_life': 'Các tầng sàn bê tông của một tòa nhà cao tầng hoặc các ngăn kệ sách được thiết kế song song '
               'với nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu mặt phẳng $(P)$ chứa hai đường thẳng cắt nhau $a, b$ và cả $a, b$ đều song song với '
                 'mặt phẳng $(Q)$ thì:',
            'options': ['$(P)$ song song với $(Q)$.',
                        '$(P)$ cắt $(Q)$.',
                        '$(P)$ trùng với $(Q)$.',
                        '$(P)$ vuông góc với $(Q)$.'],
            'answer': 0,
            'solution': 'Theo định lí dấu hiệu nhận biết hai mặt phẳng song song, $(P) \\parallel (Q)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Các mặt bên của một hình lăng trụ luôn là hình gì?',
            'options': ['Hình tam giác', 'Hình bình hành', 'Hình thang cân', 'Hình thoi'],
            'answer': 1,
            'solution': 'Theo tính chất của hình lăng trụ, các mặt bên đều là các hình bình hành.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 13: Hai mặt phẳng song song**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Dấu hiệu nhận biết**?',
            'options': ['$\\begin{cases} (\\alpha) \\parallel (\\beta) \\\\ (\\gamma) \\cap (\\alpha) = a, '
                        '(\\gamma) \\cap (\\beta) = b \\end{cases} \\Rightarrow a \\parallel b$',
                        '$\\text{Ba mặt phẳng song song chắn trên } d_1, d_2 \\text{ các đoạn tương ứng tỉ '
                        'lệ}$',
                        '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ a \\parallel '
                        '(\\beta), b \\parallel (\\beta) \\end{cases} \\Rightarrow (\\alpha) \\parallel '
                        '(\\beta)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 13: Hai mặt phẳng song song, **Dấu hiệu nhận '
                        'biết** được xác định bởi: $\\begin{cases} a, b \\subset (\\alpha), a \\cap b = '
                        '\\{I\\} \\\\ a \\parallel (\\beta), b \\parallel (\\beta) \\end{cases} \\Rightarrow '
                        '(\\alpha) \\parallel (\\beta)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Hai mặt phẳng song song**, nội dung/biểu thức $\\begin{cases} (\\alpha) '
                 '\\parallel (\\beta) \\\\ (\\gamma) \\cap (\\alpha) = a, (\\gamma) \\cap (\\beta) = b '
                 '\\end{cases} \\Rightarrow a \\parallel b$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Dấu hiệu nhận biết',
                        'Định lí Thalès trong không gian',
                        'Đổi độ và radian',
                        'Tính chất giao tuyến'],
            'answer': 3,
            'solution': 'Trong Bài 13: Hai mặt phẳng song song, biểu thức/quy tắc $\\begin{cases} (\\alpha) '
                        '\\parallel (\\beta) \\\\ (\\gamma) \\cap (\\alpha) = a, (\\gamma) \\cap (\\beta) = '
                        'b \\end{cases} \\Rightarrow a \\parallel b$ chính là nội dung của **Tính chất giao '
                        'tuyến**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai mặt phẳng song song $(\\alpha)$ và $(\\beta)$. Mặt phẳng $(\\gamma)$ cắt '
                 '$(\\alpha)$ và $(\\beta)$ lần lượt theo hai giao tuyến $a$ và $b$. Khẳng định nào sau đây '
                 'đúng?',
            'options': ['$a$ và $b$ song song với nhau.',
                        '$a$ và $b$ cắt nhau.',
                        '$a$ và $b$ chéo nhau.',
                        '$a$ và $b$ trùng nhau.'],
            'answer': 0,
            'solution': 'Hai giao tuyến $a, b$ cùng nằm trong $(\\gamma)$ và không có điểm chung (vì '
                        '$(\\alpha) \\parallel (\\beta)$) nên $a \\parallel b$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Hai mặt phẳng song song** (Chương IV: Quan hệ song song trong không '
                 'gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Phát biểu và vận dụng được định lí dấu hiệu nhận biết hai mặt phẳng song song.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 13: Hai mặt phẳng song song: Phát biểu và vận dụng '
                        'được định lí dấu hiệu nhận biết hai mặt phẳng song song.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hình hộp $ABCD.A'B'C'D'$. Xét tính đúng sai của các mệnh đề sau:",
            'statements': ['Hình hộp có $6$ mặt đều là hình bình hành.',
                           "Hai mặt phẳng $(ABCD)$ và $(A'B'C'D')$ song song với nhau.",
                           "Hai mặt phẳng $(ABB'A')$ và $(CDD'C')$ cắt nhau.",
                           "Bốn đường chéo $AC', BD', CA', DB'$ đồng quy tại trung điểm của mỗi đường."],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng theo định nghĩa hình hộp. b) Đúng vì là hai mặt đáy của hình hộp. c) Sai vì '
                        'hai mặt đối diện của hình hộp song song với nhau. d) Đúng theo tính chất đường chéo '
                        'của hình hộp.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 13: Hai mặt phẳng song '
                 'song**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phát biểu và vận dụng được định lí '
                           'dấu hiệu nhận biết hai mặt phẳng song song.',
                           'Quy tắc/công thức **Dấu hiệu nhận biết** trong bài được xác định bởi: '
                           '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ a \\parallel '
                           '(\\beta), b \\parallel (\\beta) \\end{cases} \\Rightarrow (\\alpha) \\parallel '
                           '(\\beta)$.',
                           'Trong mọi trường hợp, **Dấu hiệu nhận biết** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 13: Hai mặt phẳng song song.',
                           "Với bài toán minh họa: “Cho hình hộp $ABCD.A'B'C'D'$. Chứng minh hai mặt phẳng "
                           "$(BDA')$ và $(B'D'C)$ song song với nhau.”, lời giải đúng là: Tứ giác $BDD'B'$ "
                           "là hình bình hành nên $BD \\parallel B'D' \\Rightarrow BD \\parallel (B'D'C)$. "
                           "Tứ giác $A'B'CD$ là hình bình hành nên $A'D \\parallel B'C \\Rightarrow A'D "
                           "\\parallel (B'D'C)$..."],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Hai mặt phẳng song song. b) **Đúng** '
                        'theo công thức trọng tâm **Dấu hiệu nhận biết** ($\\begin{cases} a, b \\subset '
                        '(\\alpha), a \\cap b = \\{I\\} \\\\ a \\parallel (\\beta), b \\parallel (\\beta) '
                        '\\end{cases} \\Rightarrow (\\alpha) \\parallel (\\beta)$). c) **Sai** vì $a^\\circ '
                        '= \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Dấu hiệu nhận biết**. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 13: Hai mặt phẳng song song** để giải quyết tình huống sau: Cho '
                 "hình hộp $ABCD.A'B'C'D'$. Chứng minh hai mặt phẳng $(BDA')$ và $(B'D'C)$ song song với "
                 'nhau. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        "Tứ giác $BDD'B'$ là hình bình hành nên $BD \\parallel B'D' \\Rightarrow BD "
                        "\\parallel (B'D'C)$. Tứ giác $A'B'CD$ là hình bình hành nên $A'D \\parallel B'C "
                        "\\Rightarrow A'D \\parallel (B'D'C)$...",
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': "Lời giải chi tiết theo Bài 13: Hai mặt phẳng song song: Tứ giác $BDD'B'$ là hình "
                        "bình hành nên $BD \\parallel B'D' \\Rightarrow BD \\parallel (B'D'C)$. Tứ giác "
                        "$A'B'CD$ là hình bình hành nên $A'D \\parallel B'C \\Rightarrow A'D \\parallel "
                        "(B'D'C)$. Trong $(BDA')$, hai đường thẳng $BD$ và $A'D$ cắt nhau tại $D$, nên "
                        "$(BDA') \\parallel (B'D'C)$."},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình lăng trụ ngũ giác có tất cả bao nhiêu cạnh?',
            'answer': ['15'],
            'unit': None,
            'solution': 'Hình lăng trụ $n$-giác có $3n$ cạnh ($n$ cạnh đáy dưới, $n$ cạnh đáy trên và $n$ '
                        'cạnh bên). Với $n = 5$, số cạnh là $3 \\cdot 5 = 15$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch04-quan-he-song-song',
  'context_title': 'Chương IV: Quan hệ song song trong không gian',
  'context': 'Chương IV · SGK Toán 11: Đường thẳng và mặt phẳng trong không gian, quan hệ song song và phép '
             'chiếu song song.',
  'title': 'Bài 14: Phép chiếu song song',
  'icon': '☀️',
  'description': 'Khái niệm phép chiếu song song, các tính chất bảo toàn của phép chiếu song song và quy tắc '
                 'vẽ hình biểu diễn của một hình không gian.',
  'requirements': ['Nhận biết được mặt phẳng chiếu, phương chiếu và ảnh của một điểm, một hình qua phép '
                   'chiếu song song.',
                   'Nêu được các tính chất của phép chiếu song song: bảo toàn tính thẳng hàng, thứ tự điểm, '
                   'tính song song và tỉ số độ dài hai đoạn thẳng song song.',
                   'Vận dụng để vẽ đúng hình biểu diễn của các hình không gian trên mặt phẳng.'],
  'definition': 'Cho mặt phẳng $(\\alpha)$ và đường thẳng $\\Delta$ cắt $(\\alpha)$. Với mỗi điểm $M$ trong '
                'không gian, đường thẳng đi qua $M$ song song hoặc trùng với $\\Delta$ cắt $(\\alpha)$ tại '
                "$M'$. Phép đặt tương ứng mỗi điểm $M$ với điểm $M'$ như vậy gọi là phép chiếu song song lên "
                'mặt phẳng $(\\alpha)$ theo phương $\\Delta$.',
  'theory': '1. Phép chiếu song song biến ba điểm thẳng hàng thành ba điểm thẳng hàng và không làm thay đổi '
            'thứ tự ba điểm đó. 2. Phép chiếu song song biến đường thẳng thành đường thẳng, tia thành tia, '
            'đoạn thẳng thành đoạn thẳng. 3. Phép chiếu song song biến hai đường thẳng song song thành hai '
            'đường thẳng song song hoặc trùng nhau, và giữ nguyên tỉ số độ dài của hai đoạn thẳng cùng nằm '
            'trên một đường thẳng hoặc trên hai đường thẳng song song.',
  'formulas': [{'category': 'Tính chất bảo toàn của phép chiếu song song',
                'items': [{'name': 'Bảo toàn tỉ số đoạn thẳng song song',
                           'formula': '$AB \\parallel CD \\quad (\\text{không song song với }\\Delta) '
                                      "\\Rightarrow \\dfrac{A'B'}{C'D'} = \\dfrac{AB}{CD}$"},
                          {'name': 'Bảo toàn trung điểm',
                           'formula': "$I \\text{ là trung điểm của } AB \\Rightarrow I' \\text{ là trung "
                                      "điểm của } A'B'$"},
                          {'name': 'Hình biểu diễn của hình bình hành',
                           'formula': '$\\text{Hình bình hành, hình chữ nhật, hình thoi, hình vuông} '
                                      '\\mapsto \\text{Hình bình hành}$'}]}],
  'example': 'Qua phép chiếu song song, hình biểu diễn của một tam giác đều và một hình chữ nhật (nằm trong '
             'mặt phẳng không song song với phương chiếu) là những hình gì?',
  'example_answer': 'Do phép chiếu song song không bảo toàn độ dài và góc nhưng bảo toàn tính thẳng hàng và '
                    'tính song song nên: hình biểu diễn của tam giác đều là một tam giác bất kì; hình biểu '
                    'diễn của hình chữ nhật là một hình bình hành.',
  'real_life': 'Hiện tượng bóng nắng của tòa nhà hoặc hàng cây trên mặt đất phẳng dưới các tia sáng mặt trời '
               'song song.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tính chất nào dưới đây KHÔNG phải là tính chất của phép chiếu song song?',
            'options': ['Biến ba điểm thẳng hàng thành ba điểm thẳng hàng.',
                        'Biến hai đường thẳng vuông góc thành hai đường thẳng luôn vuông góc.',
                        'Biến trung điểm của đoạn thẳng thành trung điểm của đoạn thẳng ảnh.',
                        'Biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau.'],
            'answer': 1,
            'solution': 'Phép chiếu song song nói chung không bảo toàn số đo góc nên không biến hai đường '
                        'thẳng vuông góc thành hai đường thẳng vuông góc.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình biểu diễn của một hình vuông qua phép chiếu song song (mặt phẳng chứa hình vuông '
                 'không song song với phương chiếu) là:',
            'options': ['Một hình thang không phải hình bình hành.',
                        'Một tứ giác lồi bất kì.',
                        'Một hình bình hành.',
                        'Một đoạn thẳng.'],
            'answer': 2,
            'solution': 'Vì phép chiếu song song bảo toàn tính song song và tỉ số hai cạnh đối nên hình '
                        'vuông có hình biểu diễn là một hình bình hành.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 14: Phép chiếu song song**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Bảo toàn tỉ số đoạn thẳng song song**?',
            'options': ["$I \\text{ là trung điểm của } AB \\Rightarrow I' \\text{ là trung điểm của } A'B'$",
                        '$\\text{Hình bình hành, hình chữ nhật, hình thoi, hình vuông} \\mapsto \\text{Hình '
                        'bình hành}$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$AB \\parallel CD \\quad (\\text{không song song với }\\Delta) \\Rightarrow '
                        "\\dfrac{A'B'}{C'D'} = \\dfrac{AB}{CD}$"],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 14: Phép chiếu song song, **Bảo toàn tỉ số '
                        'đoạn thẳng song song** được xác định bởi: $AB \\parallel CD \\quad (\\text{không '
                        "song song với }\\Delta) \\Rightarrow \\dfrac{A'B'}{C'D'} = \\dfrac{AB}{CD}$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Phép chiếu song song**, nội dung/biểu thức $I \\text{ là trung điểm của } '
                 "AB \\Rightarrow I' \\text{ là trung điểm của } A'B'$ là quy tắc hoặc công thức của mục nào "
                 'sau đây?',
            'options': ['Bảo toàn trung điểm',
                        'Bảo toàn tỉ số đoạn thẳng song song',
                        'Hình biểu diễn của hình bình hành',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 14: Phép chiếu song song, biểu thức/quy tắc $I \\text{ là trung điểm của '
                        "} AB \\Rightarrow I' \\text{ là trung điểm của } A'B'$ chính là nội dung của **Bảo "
                        'toàn trung điểm**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho đoạn thẳng $AB$ có điểm $M$ thuộc đoạn $AB$ sao cho $AM = 2MB$. Qua phép chiếu song '
                 "song theo phương không song song với $AB$, ảnh của $A, B, M$ lần lượt là $A', B', M'$. Tỉ "
                 "số $\\dfrac{A'M'}{A'B'}$ bằng:",
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{2}{3}$', '$2$', '$\\dfrac{1}{3}$'],
            'answer': 1,
            'solution': 'Do phép chiếu song song bảo toàn tỉ số hai đoạn thẳng cùng nằm trên một đường thẳng '
                        "nên $\\dfrac{A'M'}{A'B'} = \\dfrac{AM}{AB} = \\dfrac{2}{3}$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Phép chiếu song song** (Chương IV: Quan hệ song song trong không gian), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Nhận biết được mặt phẳng chiếu, phương chiếu và ảnh của một điểm, một hình qua phép '
                        'chiếu song song.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 14: Phép chiếu song song: Nhận biết được mặt phẳng '
                        'chiếu, phương chiếu và ảnh của một điểm, một hình qua phép chiếu song song.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét phép chiếu song song lên mặt phẳng $(P)$ theo phương $\\Delta$ cắt $(P)$. Xét tính '
                 'đúng sai của các mệnh đề sau:',
            'statements': ['Nếu đường thẳng $a$ song song với phương chiếu $\\Delta$ thì hình chiếu của $a$ '
                           'trên $(P)$ là một điểm.',
                           'Nếu $G$ là trọng tâm của tam giác $ABC$ (mặt phẳng $(ABC)$ không song song với '
                           "$\\Delta$) thì ảnh $G'$ là trọng tâm của tam giác $A'B'C'$.",
                           'Hình chiếu song song của một hình thang luôn là một hình bình hành.',
                           'Hình chiếu song song của một đường tròn là một đường elip (hoặc đường tròn, hoặc '
                           'đoạn thẳng).'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì mọi điểm trên $a$ đều có đường chiếu trùng với $a$ cắt $(P)$ tại 1 điểm. '
                        'b) Đúng vì phép chiếu song song bảo toàn trung điểm và tỉ số chia $\\dfrac{2}{3}$. '
                        'c) Sai vì hình chiếu của hình thang là hình thang có đúng tỉ số hai đáy ban đầu. d) '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 14: Phép chiếu song '
                 'song**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được mặt phẳng chiếu, '
                           'phương chiếu và ảnh của một điểm, một hình qua phép chiếu song song.',
                           'Quy tắc/công thức **Bảo toàn tỉ số đoạn thẳng song song** trong bài được xác '
                           'định bởi: $AB \\parallel CD \\quad (\\text{không song song với }\\Delta) '
                           "\\Rightarrow \\dfrac{A'B'}{C'D'} = \\dfrac{AB}{CD}$.",
                           'Trong mọi trường hợp, **Bảo toàn tỉ số đoạn thẳng song song** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 14: Phép chiếu song song.',
                           'Với bài toán minh họa: “Qua phép chiếu song song, hình biểu diễn của một tam '
                           'giác đều và một hình chữ nhật (nằm trong mặt phẳng không song song với phương '
                           'chiếu) là...”, lời giải đúng là: Do phép chiếu song song không bảo toàn độ dài '
                           'và góc nhưng bảo toàn tính thẳng hàng và tính song song nên: hình biểu diễn của '
                           'tam giác đều l...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Phép chiếu song song. b) **Đúng** theo '
                        'công thức trọng tâm **Bảo toàn tỉ số đoạn thẳng song song** ($AB \\parallel CD '
                        "\\quad (\\text{không song song với }\\Delta) \\Rightarrow \\dfrac{A'B'}{C'D'} = "
                        '\\dfrac{AB}{CD}$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, '
                        '\\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là '
                        'công thức của nội dung khác, không phải quy tắc chung của **Bảo toàn tỉ số đoạn '
                        'thẳng song song**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 14: Phép chiếu song song** để giải quyết tình huống sau: Qua phép '
                 'chiếu song song, hình biểu diễn của một tam giác đều và một hình chữ nhật (nằm trong mặt '
                 'phẳng không song song với phương chiếu) là những hình gì? Kết quả và hướng giải nào dưới '
                 'đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Do phép chiếu song song không bảo toàn độ dài và góc nhưng bảo toàn tính thẳng hàng '
                        'và tính song song nên: hình biểu diễn của tam giác đều là một tam giác...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Phép chiếu song song: Do phép chiếu song song không '
                        'bảo toàn độ dài và góc nhưng bảo toàn tính thẳng hàng và tính song song nên: hình '
                        'biểu diễn của tam giác đều là một tam giác bất kì; hình biểu diễn của hình chữ nhật '
                        'là một hình bình hành.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cái cột thẳng đứng cao $4\\text{ m}$ có bóng trên mặt đất phẳng dài $6\\text{ m}$. '
                 'Cùng thời điểm đó, một tòa tháp gần đó có bóng trên mặt đất dài $30\\text{ m}$. Tính chiều '
                 'cao của tòa tháp (đơn vị: mét).',
            'answer': ['20'],
            'unit': None,
            'solution': 'Các tia nắng mặt trời coi như song song nên tỉ số chiều cao và chiều dài bóng được '
                        'bảo toàn: $\\dfrac{h}{30} = \\dfrac{4}{6} \\Rightarrow h = 20\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch05-gioi-han-lien-tuc',
  'context_title': 'Chương V: Giới hạn. Hàm số liên tục',
  'context': 'Chương V · SGK Toán 11: Giới hạn của dãy số, giới hạn của hàm số và hàm số liên tục.',
  'title': 'Bài 15: Giới hạn của dãy số',
  'icon': '♾️',
  'description': 'Giới hạn hữu hạn, giới hạn vô cực của dãy số, các phép toán về giới hạn và tổng của cấp số '
                 'nhân lùi vô hạn.',
  'requirements': ['Nhận biết được giới hạn bằng $0$ của các dãy số cơ bản $\\lim_{n \\to +\\infty} '
                   '\\dfrac{1}{n^k} = 0$ ($k \\in \\mathbb{N}^*$) và $\\lim_{n \\to +\\infty} q^n = 0$ ($|q| '
                   '< 1$).',
                   'Vận dụng các định lí về giới hạn hữu hạn để tính giới hạn của dãy phân thức và căn thức.',
                   'Tính được tổng của cấp số nhân lùi vô hạn $S = \\dfrac{u_1}{1 - q}$ với $|q| < 1$.'],
  'definition': 'Ta nói dãy số $(u_n)$ có giới hạn là $0$ khi $n \\to +\\infty$, kí hiệu $\\lim_{n \\to '
                '+\\infty} u_n = 0$, nếu $|u_n|$ có thể nhỏ hơn một số dương bé tùy ý kể từ một số hạng nào '
                'đó trở đi. Dãy số $(u_n)$ có giới hạn là số thực $L$ nếu $\\lim_{n \\to +\\infty} (u_n - L) '
                '= 0$.',
  'theory': '1. Giới hạn cơ bản: $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0$ ($k \\ge 1$); $\\lim_{n \\to '
            '+\\infty} q^n = 0$ nếu $|q| < 1$; $\\lim_{n \\to +\\infty} c = c$. 2. Với phân thức '
            '$\\dfrac{P(n)}{Q(n)}$, ta chia cả tử và mẫu cho lũy thừa bậc cao nhất của $n$. 3. Cấp số nhân '
            'vô hạn $(u_n)$ có công bội $q$ thỏa mãn $|q| < 1$ được gọi là cấp số nhân lùi vô hạn, có tổng '
            'là $S = u_1 + u_2 + \\dots = \\dfrac{u_1}{1 - q}$.',
  'formulas': [{'category': 'Giới hạn dãy số và cấp số nhân lùi vô hạn',
                'items': [{'name': 'Giới hạn cơ bản bằng 0',
                           'formula': '$\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\quad (k \\in '
                                      '\\mathbb{N}^*), \\quad \\lim_{n \\to +\\infty} q^n = 0 \\quad (|q| < '
                                      '1)$'},
                          {'name': 'Tổng cấp số nhân lùi vô hạn',
                           'formula': '$S = u_1 + u_1q + u_1q^2 + \\dots = \\dfrac{u_1}{1 - q} \\quad (|q| < '
                                      '1)$'},
                          {'name': 'Giới hạn vô cực',
                           'formula': '$\\lim_{n \\to +\\infty} n^k = +\\infty \\quad (k \\in '
                                      '\\mathbb{N}^*), \\quad \\lim_{n \\to +\\infty} q^n = +\\infty \\quad '
                                      '(q > 1)$'}]}],
  'example': 'Tính giới hạn $\\lim_{n \\to +\\infty} \\dfrac{3n^2 - 2n + 1}{n^2 + 4}$ và tổng $S = 1 + '
             '\\dfrac{1}{2} + \\dfrac{1}{4} + \\dfrac{1}{8} + \\dots$',
  'example_answer': 'Chia cả tử và mẫu cho $n^2$: $\\lim_{n \\to +\\infty} \\dfrac{3 - \\dfrac{2}{n} + '
                    '\\dfrac{1}{n^2}}{1 + \\dfrac{4}{n^2}} = \\dfrac{3 - 0 + 0}{1 + 0} = 3$. Tổng $S$ là '
                    'tổng của cấp số nhân lùi vô hạn với $u_1 = 1, q = \\dfrac{1}{2}$ nên $S = \\dfrac{1}{1 '
                    '- \\dfrac{1}{2}} = 2$.',
  'real_life': 'Biểu diễn số thập phân vô hạn tuần hoàn dưới dạng phân số tối giản và tính tổng quãng đường '
               'quả bóng nảy nhiều lần đến khi dừng hẳn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các giới hạn dưới đây, giới hạn nào bằng $0$?',
            'options': ['$\\lim_{n \\to +\\infty} \\left(\\dfrac{4}{3}\\right)^n$',
                        '$\\lim_{n \\to +\\infty} n^2$',
                        '$\\lim_{n \\to +\\infty} \\left(\\dfrac{2}{3}\\right)^n$',
                        '$\\lim_{n \\to +\\infty} 2^n$'],
            'answer': 2,
            'solution': 'Vì $\\left|\\dfrac{2}{3}\\right| < 1$ nên $\\lim_{n \\to +\\infty} '
                        '\\left(\\dfrac{2}{3}\\right)^n = 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của $\\lim_{n \\to +\\infty} \\dfrac{4n + 1}{2n - 3}$ bằng:',
            'options': ['$-2$', '$4$', '$-\\dfrac{1}{3}$', '$2$'],
            'answer': 3,
            'solution': 'Chia cả tử và mẫu cho $n$: $\\lim_{n \\to +\\infty} \\dfrac{4 + \\dfrac{1}{n}}{2 - '
                        '\\dfrac{3}{n}} = \\dfrac{4}{2} = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 15: Giới hạn của dãy số**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Giới hạn cơ bản bằng 0**?',
            'options': ['$\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\quad (k \\in \\mathbb{N}^*), \\quad '
                        '\\lim_{n \\to +\\infty} q^n = 0 \\quad (|q| < 1)$',
                        '$S = u_1 + u_1q + u_1q^2 + \\dots = \\dfrac{u_1}{1 - q} \\quad (|q| < 1)$',
                        '$\\lim_{n \\to +\\infty} n^k = +\\infty \\quad (k \\in \\mathbb{N}^*), \\quad '
                        '\\lim_{n \\to +\\infty} q^n = +\\infty \\quad (q > 1)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 15: Giới hạn của dãy số, **Giới hạn cơ bản '
                        'bằng 0** được xác định bởi: $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\quad (k '
                        '\\in \\mathbb{N}^*), \\quad \\lim_{n \\to +\\infty} q^n = 0 \\quad (|q| < 1)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Giới hạn của dãy số**, nội dung/biểu thức $S = u_1 + u_1q + u_1q^2 + '
                 '\\dots = \\dfrac{u_1}{1 - q} \\quad (|q| < 1)$ là quy tắc hoặc công thức của mục nào sau '
                 'đây?',
            'options': ['Giới hạn cơ bản bằng 0',
                        'Tổng cấp số nhân lùi vô hạn',
                        'Giới hạn vô cực',
                        'Đổi độ và radian'],
            'answer': 1,
            'solution': 'Trong Bài 15: Giới hạn của dãy số, biểu thức/quy tắc $S = u_1 + u_1q + u_1q^2 + '
                        '\\dots = \\dfrac{u_1}{1 - q} \\quad (|q| < 1)$ chính là nội dung của **Tổng cấp số '
                        'nhân lùi vô hạn**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tổng của cấp số nhân lùi vô hạn $S = 1 - \\dfrac{1}{3} + \\dfrac{1}{9} - \\dfrac{1}{27} + '
                 '\\dots$ bằng:',
            'options': ['$\\dfrac{3}{2}$', '$\\dfrac{4}{3}$', '$\\dfrac{3}{4}$', '$\\dfrac{2}{3}$'],
            'answer': 2,
            'solution': 'Đây là cấp số nhân lùi vô hạn với $u_1 = 1$ và $q = -\\dfrac{1}{3}$. Vậy $S = '
                        '\\dfrac{1}{1 - \\left(-\\dfrac{1}{3}\\right)} = \\dfrac{3}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Giới hạn của dãy số** (Chương V: Giới hạn. Hàm số liên tục), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Nhận biết được giới hạn bằng $0$ của các dãy số cơ bản $\\lim_{n \\to +\\infty} '
                        '\\dfrac{1}{n^k} = 0$ ($k \\in \\mathbb{N}^*$) và $\\lim_{n \\to +\\infty} q^n = 0$ '
                        '($|q| < 1$).'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 15: Giới hạn của dãy số: Nhận biết được giới hạn bằng '
                        '$0$ của các dãy số cơ bản $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0$ ($k \\in '
                        '\\mathbb{N}^*$) và $\\lim_{n \\to +\\infty} q^n = 0$ ($|q| < 1$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai dãy số $(u_n)$ và $(v_n)$ với $u_n = \\dfrac{2n^2 + 1}{n^2 + 3}$ và $v_n = '
                 '\\dfrac{3n - 1}{n + 2}$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Giới hạn $\\lim_{n \\to +\\infty} u_n = 2$.',
                           'Giới hạn $\\lim_{n \\to +\\infty} v_n = 3$.',
                           'Giới hạn $\\lim_{n \\to +\\infty} (u_n + v_n) = 5$.',
                           'Giới hạn $\\lim_{n \\to +\\infty} \\dfrac{u_n}{v_n} = 0$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì bậc tử bằng bậc mẫu, hệ số $\\dfrac{2}{1} = 2$. b) Đúng vì '
                        '$\\dfrac{3}{1} = 3$. c) Đúng vì $2 + 3 = 5$. d) Sai vì $\\lim_{n \\to +\\infty} '
                        '\\dfrac{u_n}{v_n} = \\dfrac{2}{3} \\ne 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 15: Giới hạn của dãy '
                 'số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được giới hạn bằng $0$ '
                           'của các dãy số cơ bản $\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0$ ($k \\in '
                           '\\mathbb{N}^*$) và $\\lim_{n \\to +\\infty} q^n = 0$ ($|q| < 1$).',
                           'Quy tắc/công thức **Giới hạn cơ bản bằng 0** trong bài được xác định bởi: '
                           '$\\lim_{n \\to +\\infty} \\dfrac{1}{n^k} = 0 \\quad (k \\in \\mathbb{N}^*), '
                           '\\quad \\lim_{n \\to +\\infty} q^n = 0 \\quad (|q| < 1)$.',
                           'Trong mọi trường hợp, **Giới hạn cơ bản bằng 0** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 15: Giới hạn của dãy số.',
                           'Với bài toán minh họa: “Tính giới hạn $\\lim_{n \\to +\\infty} \\dfrac{3n^2 - 2n '
                           '+ 1}{n^2 + 4}$ và tổng $S = 1 + \\dfrac{1}{2} + \\dfrac{1}{4} + \\dfrac{1}{8} + '
                           '\\dots$”, lời giải đúng là: Chia cả tử và mẫu cho $n^2$: $\\lim_{n \\to '
                           '+\\infty} \\dfrac{3 - \\dfrac{2}{n} + \\dfrac{1}{n^2}}{1 + \\dfrac{4}{n^2}} = '
                           '\\dfrac{3 - 0 + 0}{1 + 0} = 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Giới hạn của dãy số. b) **Đúng** theo '
                        'công thức trọng tâm **Giới hạn cơ bản bằng 0** ($\\lim_{n \\to +\\infty} '
                        '\\dfrac{1}{n^k} = 0 \\quad (k \\in \\mathbb{N}^*), \\quad \\lim_{n \\to +\\infty} '
                        'q^n = 0 \\quad (|q| < 1)$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ '
                        'rad}, \\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ '
                        'là công thức của nội dung khác, không phải quy tắc chung của **Giới hạn cơ bản bằng '
                        '0**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 15: Giới hạn của dãy số** để giải quyết tình huống sau: Tính giới '
                 'hạn $\\lim_{n \\to +\\infty} \\dfrac{3n^2 - 2n + 1}{n^2 + 4}$ và tổng $S = 1 + '
                 '\\dfrac{1}{2} + \\dfrac{1}{4} + \\dfrac{1}{8} + \\dots$ Kết quả và hướng giải nào dưới đây '
                 'là **đúng**?',
            'options': ['Chia cả tử và mẫu cho $n^2$: $\\lim_{n \\to +\\infty} \\dfrac{3 - \\dfrac{2}{n} + '
                        '\\dfrac{1}{n^2}}{1 + \\dfrac{4}{n^2}} = \\dfrac{3 - 0 + 0}{1 + 0} = 3$. Tổng $S$...',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Giới hạn của dãy số: Chia cả tử và mẫu cho $n^2$: '
                        '$\\lim_{n \\to +\\infty} \\dfrac{3 - \\dfrac{2}{n} + \\dfrac{1}{n^2}}{1 + '
                        '\\dfrac{4}{n^2}} = \\dfrac{3 - 0 + 0}{1 + 0} = 3$. Tổng $S$ là tổng của cấp số nhân '
                        'lùi vô hạn với $u_1 = 1, q = \\dfrac{1}{2}$ nên $S = \\dfrac{1}{1 - \\dfrac{1}{2}} '
                        '= 2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một quả bóng cao su được thả rơi tự do từ độ cao $10\\text{ m}$ xuống mặt đất. Mỗi lần '
                 'chạm đất, quả bóng lại nảy lên theo phương thẳng đứng đến độ cao bằng $\\dfrac{3}{5}$ độ '
                 'cao của lần rơi ngay trước đó. Tính tổng quãng đường (cả rơi xuống và nảy lên) mà quả bóng '
                 'đi được cho đến khi dừng hẳn (đơn vị: mét).',
            'answer': ['40'],
            'unit': None,
            'solution': 'Quãng đường rơi lần đầu là $10\\text{ m}$. Các lần nảy lên và rơi xuống tiếp theo '
                        'tạo thành $2$ lần tổng CSN lùi vô hạn có $u_1 = 10 \\cdot \\dfrac{3}{5} = 6$ và $q '
                        '= \\dfrac{3}{5}$. Tổng quãng đường là $S = 10 + 2 \\cdot \\dfrac{6}{1 - '
                        '\\dfrac{3}{5}} = 10 + 30 = 40\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch05-gioi-han-lien-tuc',
  'context_title': 'Chương V: Giới hạn. Hàm số liên tục',
  'context': 'Chương V · SGK Toán 11: Giới hạn của dãy số, giới hạn của hàm số và hàm số liên tục.',
  'title': 'Bài 16: Giới hạn của hàm số',
  'icon': '🔍',
  'description': 'Giới hạn hữu hạn của hàm số tại một điểm, tại vô cực, giới hạn một bên và giới hạn vô cực '
                 'của hàm số.',
  'requirements': ['Hiểu được khái niệm giới hạn của hàm số tại một điểm $\\lim_{x \\to x_0} f(x)$, giới hạn '
                   'một bên $\\lim_{x \\to x_0^+} f(x), \\lim_{x \\to x_0^-} f(x)$ và giới hạn tại vô cực.',
                   'Khử được dạng vô định $\\dfrac{0}{0}$ bằng cách phân tích đa thức thành nhân tử hoặc '
                   'nhân lượng liên hợp.',
                   'Tính được giới hạn một bên và giới hạn tại $\\pm\\infty$ của các hàm phân thức, căn '
                   'thức.'],
  'definition': 'Cho khoảng $K$ chứa điểm $x_0$ và hàm số $y = f(x)$ xác định trên $K \\setminus \\{x_0\\}$. '
                'Ta nói hàm số $f(x)$ có giới hạn là số $L$ khi $x$ dần tới $x_0$, kí hiệu $\\lim_{x \\to '
                'x_0} f(x) = L$, nếu với dãy số $(x_n)$ bất kì ($x_n \\in K \\setminus \\{x_0\\}$) và $x_n '
                '\\to x_0$ thì $f(x_n) \\to L$.',
  'theory': '1. Định lí giới hạn một bên: $\\lim_{x \\to x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^-} '
            'f(x) = \\lim_{x \\to x_0^+} f(x) = L$. 2. Khử dạng $\\dfrac{0}{0}$: khi $\\lim_{x \\to x_0} '
            'P(x) = \\lim_{x \\to x_0} Q(x) = 0$, ta phân tích $P(x) = (x - x_0)P_1(x)$ và $Q(x) = (x - '
            'x_0)Q_1(x)$ rồi rút gọn nhân tử $(x - x_0)$. 3. Lưu ý khi $x \\to -\\infty$: $\\sqrt{A(x)^2} = '
            '|A(x)|$, đặc biệt với $x < 0$ thì $\\sqrt{x^2} = -x$.',
  'formulas': [{'category': 'Giới hạn của hàm số',
                'items': [{'name': 'Điều kiện tồn tại giới hạn tại một điểm',
                           'formula': '$\\lim_{x \\to x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^+} '
                                      'f(x) = \\lim_{x \\to x_0^-} f(x) = L$'},
                          {'name': 'Hằng đẳng thức khử dạng 0/0',
                           'formula': '$x^2 - x_0^2 = (x - x_0)(x + x_0), \\quad \\sqrt{A} - \\sqrt{B} = '
                                      '\\dfrac{A - B}{\\sqrt{A} + \\sqrt{B}}$'},
                          {'name': 'Giới hạn cơ bản tại vô cực',
                           'formula': '$\\lim_{x \\to \\pm\\infty} \\dfrac{c}{x^k} = 0 \\quad (k \\in '
                                      '\\mathbb{N}^*)$'}]}],
  'example': 'Tính giới hạn $\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - 2}$.',
  'example_answer': 'Với $x \\ne 2$, ta có $\\dfrac{x^2 - 4}{x - 2} = \\dfrac{(x - 2)(x + 2)}{x - 2} = x + '
                    '2$. Suy ra $\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} (x + 2) = 2 + 2 '
                    '= 4$.',
  'real_life': 'Tính vận tốc tức thời của vật chuyển động và xác định hành vi tiệm cận của các đại lượng vật '
               'lí khi tiến gần điểm tới hạn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của $\\lim_{x \\to 1} (3x^2 - 2x + 4)$ bằng:',
            'options': ['$4$', '$3$', '$9$', '$5$'],
            'answer': 3,
            'solution': 'Thay trực tiếp $x = 1$ vào hàm đa thức: $3 \\cdot 1^2 - 2 \\cdot 1 + 4 = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hàm số $y = f(x)$ có giới hạn là $L$ khi $x \\to x_0$ khi và chỉ khi:',
            'options': ['$\\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = L$',
                        '$\\lim_{x \\to x_0^+} f(x) = L$',
                        '$\\lim_{x \\to x_0^-} f(x) = L$',
                        '$f(x_0) = L$'],
            'answer': 0,
            'solution': 'Giới hạn tại điểm $x_0$ tồn tại và bằng $L$ khi và chỉ khi hai giới hạn một bên '
                        'bằng nhau và bằng $L$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 16: Giới hạn của hàm số**, công thức hoặc quy tắc nào '
                 'sau đây biểu diễn đúng **Điều kiện tồn tại giới hạn tại một điểm**?',
            'options': ['$x^2 - x_0^2 = (x - x_0)(x + x_0), \\quad \\sqrt{A} - \\sqrt{B} = \\dfrac{A - '
                        'B}{\\sqrt{A} + \\sqrt{B}}$',
                        '$\\lim_{x \\to x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = \\lim_{x '
                        '\\to x_0^-} f(x) = L$',
                        '$\\lim_{x \\to \\pm\\infty} \\dfrac{c}{x^k} = 0 \\quad (k \\in \\mathbb{N}^*)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 16: Giới hạn của hàm số, **Điều kiện tồn tại '
                        'giới hạn tại một điểm** được xác định bởi: $\\lim_{x \\to x_0} f(x) = L '
                        '\\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = L$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Giới hạn của hàm số**, nội dung/biểu thức $x^2 - x_0^2 = (x - x_0)(x + '
                 'x_0), \\quad \\sqrt{A} - \\sqrt{B} = \\dfrac{A - B}{\\sqrt{A} + \\sqrt{B}}$ là quy tắc '
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Điều kiện tồn tại giới hạn tại một điểm',
                        'Giới hạn cơ bản tại vô cực',
                        'Hằng đẳng thức khử dạng 0/0',
                        'Đổi độ và radian'],
            'answer': 2,
            'solution': 'Trong Bài 16: Giới hạn của hàm số, biểu thức/quy tắc $x^2 - x_0^2 = (x - x_0)(x + '
                        'x_0), \\quad \\sqrt{A} - \\sqrt{B} = \\dfrac{A - B}{\\sqrt{A} + \\sqrt{B}}$ chính '
                        'là nội dung của **Hằng đẳng thức khử dạng 0/0**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của $\\lim_{x \\to 3} \\dfrac{x^2 - 9}{x - 3}$ bằng:',
            'options': ['$3$', '$0$', '$9$', '$6$'],
            'answer': 3,
            'solution': 'Ta có $\\lim_{x \\to 3} \\dfrac{(x - 3)(x + 3)}{x - 3} = \\lim_{x \\to 3} (x + 3) = '
                        '6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Giới hạn của hàm số** (Chương V: Giới hạn. Hàm số liên tục), khẳng định '
                 'nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Hiểu được khái niệm giới hạn của hàm số tại một điểm $\\lim_{x \\to x_0} f(x)$, '
                        'giới hạn một bên $\\lim_{x \\to x_0^+} f(x), \\lim_{x \\to x_0^-} f(x)$ và giới hạn '
                        'tại vô cực.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 16: Giới hạn của hàm số: Hiểu được khái niệm giới hạn '
                        'của hàm số tại một điểm $\\lim_{x \\to x_0} f(x)$, giới hạn một bên $\\lim_{x \\to '
                        'x_0^+} f(x), \\lim_{x \\to x_0^-} f(x)$ và giới hạn tại vô cực.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $f(x) = \\dfrac{2x + 1}{x - 1}$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Giới hạn $\\lim_{x \\to 2} f(x) = 5$.',
                           'Giới hạn $\\lim_{x \\to +\\infty} f(x) = 2$.',
                           'Giới hạn một bên $\\lim_{x \\to 1^+} f(x) = +\\infty$.',
                           'Giới hạn một bên $\\lim_{x \\to 1^-} f(x) = +\\infty$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $\\dfrac{2 \\cdot 2 + 1}{2 - 1} = 5$. b) Đúng vì $\\lim_{x \\to '
                        '+\\infty} \\dfrac{2 + \\dfrac{1}{x}}{1 - \\dfrac{1}{x}} = 2$. c) Đúng vì khi $x '
                        '\\to 1^+$, tử tiến tới $3 > 0$ và mẫu $x - 1 > 0$ tiến tới $0$. d) Sai vì khi $x '
                        '\\to 1^-$, mẫu $x - 1 < 0$ nên $\\lim_{x \\to 1^-} f(x) = -\\infty$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 16: Giới hạn của hàm '
                 'số**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được khái niệm giới hạn của '
                           'hàm số tại một điểm $\\lim_{x \\to x_0} f(x)$, giới hạn một bên $\\lim_{x \\to '
                           'x_0^+} f(x), \\lim_{x \\to x_0^-} f(x)$ và giới hạn tại vô cực.',
                           'Quy tắc/công thức **Điều kiện tồn tại giới hạn tại một điểm** trong bài được xác '
                           'định bởi: $\\lim_{x \\to x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^+} '
                           'f(x) = \\lim_{x \\to x_0^-} f(x) = L$.',
                           'Trong mọi trường hợp, **Điều kiện tồn tại giới hạn tại một điểm** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 16: Giới hạn của hàm số.',
                           'Với bài toán minh họa: “Tính giới hạn $\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - '
                           '2}$.”, lời giải đúng là: Với $x \\ne 2$, ta có $\\dfrac{x^2 - 4}{x - 2} = '
                           '\\dfrac{(x - 2)(x + 2)}{x - 2} = x + 2$. Suy ra $\\lim_{x \\to 2} \\dfrac{x^2 - '
                           '4}{x - 2} = \\lim_{x \\to 2} (x + 2) = 2 + 2 = 4$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Giới hạn của hàm số. b) **Đúng** theo '
                        'công thức trọng tâm **Điều kiện tồn tại giới hạn tại một điểm** ($\\lim_{x \\to '
                        'x_0} f(x) = L \\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} '
                        'f(x) = L$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                        '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức '
                        'của nội dung khác, không phải quy tắc chung của **Điều kiện tồn tại giới hạn tại '
                        'một điểm**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 16: Giới hạn của hàm số** để giải quyết tình huống sau: Tính giới '
                 'hạn $\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - 2}$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Với $x \\ne 2$, ta có $\\dfrac{x^2 - 4}{x - 2} = \\dfrac{(x - 2)(x + 2)}{x - 2} = x '
                        '+ 2$. Suy ra $\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} (x + 2) = '
                        '2 + 2 = 4$...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Giới hạn của hàm số: Với $x \\ne 2$, ta có '
                        '$\\dfrac{x^2 - 4}{x - 2} = \\dfrac{(x - 2)(x + 2)}{x - 2} = x + 2$. Suy ra '
                        '$\\lim_{x \\to 2} \\dfrac{x^2 - 4}{x - 2} = \\lim_{x \\to 2} (x + 2) = 2 + 2 = 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giới hạn $L = \\lim_{x \\to 0} \\dfrac{\\sqrt{x + 4} - 2}{x}$ (viết kết quả dưới dạng '
                 'số thập phân).',
            'answer': ['0,25', '0.25'],
            'unit': None,
            'solution': 'Nhân lượng liên hợp: $L = \\lim_{x \\to 0} \\dfrac{(x + 4) - 4}{x(\\sqrt{x + 4} + '
                        '2)} = \\lim_{x \\to 0} \\dfrac{1}{\\sqrt{x + 4} + 2} = \\dfrac{1}{2 + 2} = 0,25$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch05-gioi-han-lien-tuc',
  'context_title': 'Chương V: Giới hạn. Hàm số liên tục',
  'context': 'Chương V · SGK Toán 11: Giới hạn của dãy số, giới hạn của hàm số và hàm số liên tục.',
  'title': 'Bài 17: Hàm số liên tục',
  'icon': '🔗',
  'description': 'Khái niệm hàm số liên tục tại một điểm, liên tục trên một khoảng hoặc đoạn và định lí về '
                 'sự tồn tại nghiệm của phương trình.',
  'requirements': ['Xét được tính liên tục của hàm số tại một điểm theo điều kiện $\\lim_{x \\to x_0} f(x) = '
                   'f(x_0)$.',
                   'Nhận biết được tính liên tục của các hàm đa thức, phân thức hữu tỉ, căn thức và lượng '
                   'giác trên tập xác định của chúng.',
                   'Vận dụng tính chất hàm số liên tục trên đoạn $[a; b]$ thỏa mãn $f(a) \\cdot f(b) < 0$ để '
                   'chứng minh phương trình $f(x) = 0$ có nghiệm.'],
  'definition': 'Cho hàm số $y = f(x)$ xác định trên khoảng $K$ và $x_0 \\in K$. Hàm số $y = f(x)$ được gọi '
                'là liên tục tại $x_0$ nếu $\\lim_{x \\to x_0} f(x) = f(x_0)$. Hàm số không liên tục tại '
                '$x_0$ được gọi là gián đoạn tại điểm đó.',
  'theory': '1. Hàm số liên tục trên đoạn $[a; b]$ nếu nó liên tục trên khoảng $(a; b)$ và $\\lim_{x \\to '
            'a^+} f(x) = f(a)$, $\\lim_{x \\to b^-} f(x) = f(b)$. 2. Tổng, hiệu, tích, thương (với mẫu khác '
            '$0$) của hai hàm số liên tục tại một điểm là hàm số liên tục tại điểm đó. 3. Định lí giá trị '
            'trung gian: Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \\cdot f(b) < 0$ thì tồn '
            'tại ít nhất một điểm $c \\in (a; b)$ sao cho $f(c) = 0$.',
  'formulas': [{'category': 'Điều kiện liên tục và sự tồn tại nghiệm',
                'items': [{'name': 'Liên tục tại một điểm',
                           'formula': '$\\lim_{x \\to x_0} f(x) = f(x_0) \\Leftrightarrow \\lim_{x \\to '
                                      'x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = f(x_0)$'},
                          {'name': 'Điều kiện phương trình f(x) = 0 có nghiệm trên (a; b)',
                           'formula': '$f(x) \\text{ liên tục trên } [a; b] \\text{ và } f(a) \\cdot f(b) < '
                                      '0$'}]}],
  'example': 'Tìm giá trị của tham số $m$ để hàm số $f(x) = \\begin{cases} \\dfrac{x^2 - 1}{x - 1} & '
             '\\text{khi } x \\ne 1 \\\\ m & \\text{khi } x = 1 \\end{cases}$ liên tục tại $x = 1$.',
  'example_answer': 'Ta có $f(1) = m$ và $\\lim_{x \\to 1} f(x) = \\lim_{x \\to 1} \\dfrac{x^2 - 1}{x - 1} = '
                    '\\lim_{x \\to 1} (x + 1) = 2$. Để hàm số liên tục tại $x = 1$ thì $\\lim_{x \\to 1} '
                    'f(x) = f(1) \\Leftrightarrow m = 2$.',
  'real_life': 'Biểu diễn các quá trình biến đổi nhiệt độ, mực nước biển diễn ra liên tục và tìm nghiệm xấp '
               'xỉ bằng phương pháp chia đôi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa điểm $x_0$. Hàm số $f(x)$ liên '
                 'tục tại $x_0$ khi và chỉ khi:',
            'options': ['$\\lim_{x \\to x_0} f(x) = f(x_0)$',
                        '$\\lim_{x \\to x_0} f(x) = 0$',
                        '$f(x_0) = 0$',
                        '$\\lim_{x \\to +\\infty} f(x) = f(x_0)$'],
            'answer': 0,
            'solution': 'Theo định nghĩa, hàm số $f(x)$ liên tục tại $x_0$ khi và chỉ khi $\\lim_{x \\to '
                        'x_0} f(x) = f(x_0)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hàm số $y = \\dfrac{x + 2}{x - 3}$ gián đoạn tại điểm nào dưới đây?',
            'options': ['$x = -2$', '$x = 3$', '$x = 0$', '$x = 1$'],
            'answer': 1,
            'solution': 'Hàm phân thức hữu tỉ liên tục trên từng khoảng xác định và gián đoạn tại điểm làm '
                        'mẫu bằng $0$ là $x = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 17: Hàm số liên tục**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Liên tục tại một điểm**?',
            'options': ['$f(x) \\text{ liên tục trên } [a; b] \\text{ và } f(a) \\cdot f(b) < 0$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$\\lim_{x \\to x_0} f(x) = f(x_0) \\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = '
                        '\\lim_{x \\to x_0^-} f(x) = f(x_0)$',
                        '$l = R \\cdot \\alpha \\quad (\\alpha \\text{ tính bằng rad})$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 17: Hàm số liên tục, **Liên tục tại một '
                        'điểm** được xác định bởi: $\\lim_{x \\to x_0} f(x) = f(x_0) \\Leftrightarrow '
                        '\\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = f(x_0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Hàm số liên tục**, nội dung/biểu thức $f(x) \\text{ liên tục trên } [a; b] '
                 '\\text{ và } f(a) \\cdot f(b) < 0$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Liên tục tại một điểm',
                        'Đổi độ và radian',
                        'Độ dài cung tròn',
                        'Điều kiện phương trình f(x) = 0 có nghiệm trên (a; b)'],
            'answer': 3,
            'solution': 'Trong Bài 17: Hàm số liên tục, biểu thức/quy tắc $f(x) \\text{ liên tục trên } [a; '
                        'b] \\text{ và } f(a) \\cdot f(b) < 0$ chính là nội dung của **Điều kiện phương '
                        'trình f(x) = 0 có nghiệm trên (a; b)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu hàm số $y = f(x)$ liên tục trên đoạn $[a; b]$ và $f(a) \\cdot f(b) < 0$ thì phương '
                 'trình $f(x) = 0$:',
            'options': ['Có ít nhất một nghiệm trong khoảng $(a; b)$.',
                        'Vô nghiệm trên khoảng $(a; b)$.',
                        'Có duy nhất một nghiệm trong khoảng $(a; b)$.',
                        'Có đúng hai nghiệm trong khoảng $(a; b)$.'],
            'answer': 0,
            'solution': 'Theo hệ quả định lí giá trị trung gian, phương trình $f(x) = 0$ có ít nhất một '
                        'nghiệm $c \\in (a; b)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Hàm số liên tục** (Chương V: Giới hạn. Hàm số liên tục), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xét được tính liên tục của hàm số tại một điểm theo điều kiện $\\lim_{x \\to x_0} '
                        'f(x) = f(x_0)$.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 17: Hàm số liên tục: Xét được tính liên tục của hàm số '
                        'tại một điểm theo điều kiện $\\lim_{x \\to x_0} f(x) = f(x_0)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $f(x) = \\begin{cases} 2x + 1 & \\text{khi } x \\ge 1 \\\\ x^2 + a & \\text{khi '
                 '} x < 1 \\end{cases}$ với $a$ là tham số thực. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Giá trị của hàm số tại $x = 1$ là $f(1) = 3$.',
                           'Giới hạn bên phải $\\lim_{x \\to 1^+} f(x) = 3$.',
                           'Giới hạn bên trái $\\lim_{x \\to 1^-} f(x) = 1 + a$.',
                           'Hàm số liên tục tại $x = 1$ khi và chỉ khi $a = 3$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $f(1) = 2 \\cdot 1 + 1 = 3$. b) Đúng vì $\\lim_{x \\to 1^+} (2x + 1) = '
                        '3$. c) Đúng vì $\\lim_{x \\to 1^-} (x^2 + a) = 1 + a$. d) Sai vì hàm số liên tục '
                        'tại $x = 1 \\Leftrightarrow 1 + a = 3 \\Leftrightarrow a = 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 17: Hàm số liên tục**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xét được tính liên tục của hàm số '
                           'tại một điểm theo điều kiện $\\lim_{x \\to x_0} f(x) = f(x_0)$.',
                           'Quy tắc/công thức **Liên tục tại một điểm** trong bài được xác định bởi: '
                           '$\\lim_{x \\to x_0} f(x) = f(x_0) \\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = '
                           '\\lim_{x \\to x_0^-} f(x) = f(x_0)$.',
                           'Trong mọi trường hợp, **Liên tục tại một điểm** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 17: Hàm số liên tục.',
                           'Với bài toán minh họa: “Tìm giá trị của tham số $m$ để hàm số $f(x) = '
                           '\\begin{cases} \\dfrac{x^2 - 1}{x - 1} & \\text{khi } x \\ne 1 \\\\ m & '
                           '\\text{khi } x = 1 \\end{cases}$...”, lời giải đúng là: Ta có $f(1) = m$ và '
                           '$\\lim_{x \\to 1} f(x) = \\lim_{x \\to 1} \\dfrac{x^2 - 1}{x - 1} = \\lim_{x '
                           '\\to 1} (x + 1) = 2$. Để hàm số liên tục tại $x = 1$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Hàm số liên tục. b) **Đúng** theo công '
                        'thức trọng tâm **Liên tục tại một điểm** ($\\lim_{x \\to x_0} f(x) = f(x_0) '
                        '\\Leftrightarrow \\lim_{x \\to x_0^+} f(x) = \\lim_{x \\to x_0^-} f(x) = f(x_0)$). '
                        'c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                        'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung '
                        'khác, không phải quy tắc chung của **Liên tục tại một điểm**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 17: Hàm số liên tục** để giải quyết tình huống sau: Tìm giá trị '
                 'của tham số $m$ để hàm số $f(x) = \\begin{cases} \\dfrac{x^2 - 1}{x - 1} & \\text{khi } x '
                 '\\ne 1 \\\\ m & \\text{khi } x = 1 \\end{cases}$ liên tục tại $x = 1$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Ta có $f(1) = m$ và $\\lim_{x \\to 1} f(x) = \\lim_{x \\to 1} \\dfrac{x^2 - 1}{x - '
                        '1} = \\lim_{x \\to 1} (x + 1) = 2$. Để hàm số liên tục tại $x = 1$ thì $\\lim_{x '
                        '\\to 1} f(x) = f(1) \\Leftrightarrow m = 2$...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Hàm số liên tục: Ta có $f(1) = m$ và $\\lim_{x \\to '
                        '1} f(x) = \\lim_{x \\to 1} \\dfrac{x^2 - 1}{x - 1} = \\lim_{x \\to 1} (x + 1) = 2$. '
                        'Để hàm số liên tục tại $x = 1$ thì $\\lim_{x \\to 1} f(x) = f(1) \\Leftrightarrow m '
                        '= 2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hàm số $f(x) = \\begin{cases} \\dfrac{x^2 - 9}{x - 3} & \\text{khi } x \\ne 3 \\\\ 2m '
                 '& \\text{khi } x = 3 \\end{cases}$. Tìm giá trị của $m$ để hàm số liên tục tại $x = 3$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Ta có $\\lim_{x \\to 3} f(x) = \\lim_{x \\to 3} (x + 3) = 6$ và $f(3) = 2m$. Để hàm '
                        'số liên tục tại $x = 3$ thì $2m = 6 \\Leftrightarrow m = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch06-mu-logarit',
  'context_title': 'Chương VI: Hàm số mũ và hàm số lôgarit',
  'context': 'Chương VI · SGK Toán 11: Lũy thừa với số mũ thực, lôgarit, hàm số mũ, hàm số lôgarit và phương '
             'trình, bất phương trình mũ - lôgarit.',
  'title': 'Bài 18: Lũy thừa với số mũ thực',
  'icon': '⚡',
  'description': 'Lũy thừa với số mũ nguyên, căn bậc n, lũy thừa với số mũ hữu tỉ, số mũ thực và các tính '
                 'chất biến đổi lũy thừa.',
  'requirements': ['Hiểu được khái niệm căn bậc $n$, lũy thừa với số mũ nguyên, số mũ hữu tỉ '
                   '$a^{\\frac{m}{n}} = \\sqrt[n]{a^m}$ và số mũ thực.',
                   'Vận dụng thành thạo các quy tắc nhân, chia hai lũy thừa cùng cơ số và lũy thừa của một '
                   'lũy thừa.',
                   'Áp dụng công thức lãi kép $A = P(1 + r)^N$ để giải các bài toán tài chính thực tế.'],
  'definition': 'Cho số thực dương $a$ và số hữu tỉ $r = \\dfrac{m}{n}$ ($m \\in \\mathbb{Z}, n \\in '
                '\\mathbb{N}, n \\ge 2$). Lũy thừa của $a$ với số mũ $r$ được xác định bởi $a^r = '
                'a^{\\frac{m}{n}} = \\sqrt[n]{a^m}$. Khái niệm này được mở rộng cho số mũ thực $\\alpha \\in '
                '\\mathbb{R}$ bất kì với $a > 0$.',
  'theory': '1. Với $a, b > 0$ và $\\alpha, \\beta \\in \\mathbb{R}$: $a^\\alpha \\cdot a^\\beta = '
            'a^{\\alpha + \\beta}$; $\\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}$; '
            '$(a^\\alpha)^\\beta = a^{\\alpha\\beta}$; $(ab)^\\alpha = a^\\alpha b^\\alpha$. 2. So sánh lũy '
            'thừa: nếu $a > 1$ thì $a^\\alpha > a^\\beta \\Leftrightarrow \\alpha > \\beta$; nếu $0 < a < 1$ '
            'thì $a^\\alpha > a^\\beta \\Leftrightarrow \\alpha < \\beta$.',
  'formulas': [{'category': 'Các tính chất của lũy thừa với số mũ thực (a, b > 0)',
                'items': [{'name': 'Liên hệ căn bậc n và mũ hữu tỉ',
                           'formula': '$a^{\\frac{m}{n}} = \\sqrt[n]{a^m} \\quad (a > 0, m \\in \\mathbb{Z}, '
                                      'n \\ge 2)$'},
                          {'name': 'Quy tắc nhân, chia, lũy thừa tầng',
                           'formula': '$a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}, \\quad '
                                      '\\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}, \\quad '
                                      '(a^\\alpha)^\\beta = a^{\\alpha\\beta}$'},
                          {'name': 'Công thức lãi kép', 'formula': '$A = P(1 + r)^N$'}]}],
  'example': 'Rút gọn biểu thức $P = a^{\\frac{4}{3}} \\cdot \\sqrt[3]{a^2}$ với $a > 0$.',
  'example_answer': 'Ta có $\\sqrt[3]{a^2} = a^{\\frac{2}{3}}$. Do đó $P = a^{\\frac{4}{3}} \\cdot '
                    'a^{\\frac{2}{3}} = a^{\\frac{4}{3} + \\frac{2}{3}} = a^2$.',
  'real_life': 'Tính tiền vốn lẫn lãi khi gửi tiết kiệm ngân hàng theo thể thức lãi kép và tính chu kì bán '
               'rã chất phóng xạ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a$ là số thực dương tùy ý, biểu thức $\\sqrt[3]{a^5}$ viết dưới dạng lũy thừa với số '
                 'mũ hữu tỉ là:',
            'options': ['$a^{\\frac{3}{5}}$', '$a^{\\frac{5}{3}}$', '$a^{15}$', '$a^2$'],
            'answer': 1,
            'solution': 'Theo định nghĩa lũy thừa với số mũ hữu tỉ: $\\sqrt[3]{a^5} = a^{\\frac{5}{3}}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a > 0$ và $\\alpha, \\beta \\in \\mathbb{R}$, đẳng thức nào dưới đây đúng?',
            'options': ['$a^\\alpha \\cdot a^\\beta = a^{\\alpha \\cdot \\beta}$',
                        '$a^\\alpha + a^\\beta = a^{\\alpha + \\beta}$',
                        '$a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}$',
                        '$(a^\\alpha)^\\beta = a^{\\alpha + \\beta}$'],
            'answer': 2,
            'solution': 'Nhân hai lũy thừa cùng cơ số dương ta giữ nguyên cơ số và cộng hai số mũ: '
                        '$a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 18: Lũy thừa với số mũ thực**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Liên hệ căn bậc n và mũ hữu tỉ**?',
            'options': ['$a^\\alpha \\cdot a^\\beta = a^{\\alpha + \\beta}, \\quad '
                        '\\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}, \\quad (a^\\alpha)^\\beta = '
                        'a^{\\alpha\\beta}$',
                        '$A = P(1 + r)^N$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$a^{\\frac{m}{n}} = \\sqrt[n]{a^m} \\quad (a > 0, m \\in \\mathbb{Z}, n \\ge 2)$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 18: Lũy thừa với số mũ thực, **Liên hệ căn '
                        'bậc n và mũ hữu tỉ** được xác định bởi: $a^{\\frac{m}{n}} = \\sqrt[n]{a^m} \\quad '
                        '(a > 0, m \\in \\mathbb{Z}, n \\ge 2)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Lũy thừa với số mũ thực**, nội dung/biểu thức $a^\\alpha \\cdot a^\\beta = '
                 'a^{\\alpha + \\beta}, \\quad \\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}, \\quad '
                 '(a^\\alpha)^\\beta = a^{\\alpha\\beta}$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quy tắc nhân, chia, lũy thừa tầng',
                        'Liên hệ căn bậc n và mũ hữu tỉ',
                        'Công thức lãi kép',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 18: Lũy thừa với số mũ thực, biểu thức/quy tắc $a^\\alpha \\cdot a^\\beta '
                        '= a^{\\alpha + \\beta}, \\quad \\dfrac{a^\\alpha}{a^\\beta} = a^{\\alpha - \\beta}, '
                        '\\quad (a^\\alpha)^\\beta = a^{\\alpha\\beta}$ chính là nội dung của **Quy tắc '
                        'nhân, chia, lũy thừa tầng**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $P = 8^{\\frac{2}{3}} + 9^{\\frac{1}{2}}$ bằng:',
            'options': ['$6$', '$7$', '$10$', '$5$'],
            'answer': 1,
            'solution': 'Ta có $8^{\\frac{2}{3}} = (2^3)^{\\frac{2}{3}} = 2^2 = 4$ và $9^{\\frac{1}{2}} = '
                        '\\sqrt{9} = 3$. Vậy $P = 4 + 3 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Lũy thừa với số mũ thực** (Chương VI: Hàm số mũ và hàm số lôgarit), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Hiểu được khái niệm căn bậc $n$, lũy thừa với số mũ nguyên, số mũ hữu tỉ '
                        '$a^{\\frac{m}{n}} = \\sqrt[n]{a^m}$ và số mũ thực.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 18: Lũy thừa với số mũ thực: Hiểu được khái niệm căn '
                        'bậc $n$, lũy thừa với số mũ nguyên, số mũ hữu tỉ $a^{\\frac{m}{n}} = '
                        '\\sqrt[n]{a^m}$ và số mũ thực.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho số thực dương $a > 0$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Biểu thức $a^0 = 1$ với mọi $a > 0$.',
                           'Biểu thức $a^{-2} = \\dfrac{1}{a^2}$ với mọi $a > 0$.',
                           'Rút gọn biểu thức $A = a^{\\frac{1}{2}} \\cdot \\sqrt[4]{a}$ ta được $A = '
                           'a^{\\frac{3}{4}}$.',
                           'Nếu $0 < a < 1$ thì $a^{\\sqrt{3}} > a^{\\sqrt{2}}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng. c) Đúng vì $a^{\\frac{1}{2}} \\cdot a^{\\frac{1}{4}} = '
                        'a^{\\frac{3}{4}}$. d) Sai vì với cơ số $0 < a < 1$ và $\\sqrt{3} > \\sqrt{2}$ thì '
                        '$a^{\\sqrt{3}} < a^{\\sqrt{2}}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 18: Lũy thừa với số mũ '
                 'thực**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được khái niệm căn bậc $n$, '
                           'lũy thừa với số mũ nguyên, số mũ hữu tỉ $a^{\\frac{m}{n}} = \\sqrt[n]{a^m}$ và '
                           'số mũ thực.',
                           'Quy tắc/công thức **Liên hệ căn bậc n và mũ hữu tỉ** trong bài được xác định '
                           'bởi: $a^{\\frac{m}{n}} = \\sqrt[n]{a^m} \\quad (a > 0, m \\in \\mathbb{Z}, n '
                           '\\ge 2)$.',
                           'Trong mọi trường hợp, **Liên hệ căn bậc n và mũ hữu tỉ** luôn được tính bằng '
                           'công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                           'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) '
                           'mà không cần điều kiện của Bài 18: Lũy thừa với số mũ thực.',
                           'Với bài toán minh họa: “Rút gọn biểu thức $P = a^{\\frac{4}{3}} \\cdot '
                           '\\sqrt[3]{a^2}$ với $a > 0$.”, lời giải đúng là: Ta có $\\sqrt[3]{a^2} = '
                           'a^{\\frac{2}{3}}$. Do đó $P = a^{\\frac{4}{3}} \\cdot a^{\\frac{2}{3}} = '
                           'a^{\\frac{4}{3} + \\frac{2}{3}} = a^2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Lũy thừa với số mũ thực. b) **Đúng** '
                        'theo công thức trọng tâm **Liên hệ căn bậc n và mũ hữu tỉ** ($a^{\\frac{m}{n}} = '
                        '\\sqrt[n]{a^m} \\quad (a > 0, m \\in \\mathbb{Z}, n \\ge 2)$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Liên hệ căn bậc n và mũ hữu tỉ**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 18: Lũy thừa với số mũ thực** để giải quyết tình huống sau: Rút '
                 'gọn biểu thức $P = a^{\\frac{4}{3}} \\cdot \\sqrt[3]{a^2}$ với $a > 0$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Ta có $\\sqrt[3]{a^2} = a^{\\frac{2}{3}}$. Do đó $P = a^{\\frac{4}{3}} \\cdot '
                        'a^{\\frac{2}{3}} = a^{\\frac{4}{3} + \\frac{2}{3}} = a^2$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Lũy thừa với số mũ thực: Ta có $\\sqrt[3]{a^2} = '
                        'a^{\\frac{2}{3}}$. Do đó $P = a^{\\frac{4}{3}} \\cdot a^{\\frac{2}{3}} = '
                        'a^{\\frac{4}{3} + \\frac{2}{3}} = a^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một người gửi $100$ triệu đồng vào ngân hàng với lãi suất $6\\%$/năm theo hình thức lãi '
                 'kép. Hỏi sau $5$ năm người đó nhận được cả vốn lẫn lãi là bao nhiêu triệu đồng (làm tròn '
                 'đến hàng phần mười)?',
            'answer': ['133,8', '133.8'],
            'unit': None,
            'solution': 'Áp dụng công thức lãi kép: $A = 100 \\cdot (1 + 0,06)^5 = 100 \\cdot 1,06^5 '
                        '\\approx 133,8$ (triệu đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch06-mu-logarit',
  'context_title': 'Chương VI: Hàm số mũ và hàm số lôgarit',
  'context': 'Chương VI · SGK Toán 11: Lũy thừa với số mũ thực, lôgarit, hàm số mũ, hàm số lôgarit và phương '
             'trình, bất phương trình mũ - lôgarit.',
  'title': 'Bài 19: Lôgarit',
  'icon': '🧮',
  'description': 'Khái niệm lôgarit, các quy tắc tính lôgarit của một tích, một thương, một lũy thừa, công '
                 'thức đổi cơ số, lôgarit thập phân và lôgarit tự nhiên.',
  'requirements': ['Hiểu được định nghĩa lôgarit: với $0 < a \\ne 1, b > 0$ thì $\\alpha = \\log_a b '
                   '\\Leftrightarrow a^\\alpha = b$.',
                   'Vận dụng thành thạo các quy tắc tính lôgarit và công thức đổi cơ số $\\log_a b = '
                   '\\dfrac{\\log_c b}{\\log_c a}$.',
                   'Sử dụng được lôgarit thập phân $\\log x$ và lôgarit tự nhiên $\\ln x$ trong tính toán.'],
  'definition': 'Cho hai số thực dương $a, b$ với $a \\ne 1$. Số thực $\\alpha$ thỏa mãn đẳng thức '
                '$a^\\alpha = b$ được gọi là lôgarit cơ số $a$ của $b$ và kí hiệu là $\\log_a b$. Như vậy '
                '$\\alpha = \\log_a b \\Leftrightarrow a^\\alpha = b$.',
  'theory': '1. Tính chất cơ bản: $\\log_a 1 = 0$; $\\log_a a = 1$; $a^{\\log_a b} = b$; $\\log_a '
            '(a^\\alpha) = \\alpha$. 2. Quy tắc tính ($0 < a \\ne 1; M, N > 0$): $\\log_a(MN) = \\log_a M + '
            '\\log_a N$; $\\log_a\\left(\\dfrac{M}{N}\\right) = \\log_a M - \\log_a N$; $\\log_a(M^\\alpha) '
            '= \\alpha \\log_a M$. 3. Đổi cơ số: $\\log_a b = \\dfrac{\\log_c b}{\\log_c a}$; hệ quả '
            '$\\log_{a^\\alpha} b = \\dfrac{1}{\\alpha}\\log_a b$ và $\\log_a b = \\dfrac{1}{\\log_b a}$. 4. '
            'Lôgarit thập phân: $\\log b = \\log_{10} b$; lôgarit tự nhiên: $\\ln b = \\log_e b$ ($e '
            '\\approx 2,71828$).',
  'formulas': [{'category': 'Các quy tắc tính lôgarit (0 < a ≠ 1; M, N > 0)',
                'items': [{'name': 'Định nghĩa và tính chất cơ bản',
                           'formula': '$\\log_a b = \\alpha \\Leftrightarrow a^\\alpha = b; \\quad \\log_a 1 '
                                      '= 0, \\quad \\log_a a = 1$'},
                          {'name': 'Lôgarit của tích, thương, lũy thừa',
                           'formula': '$\\log_a(MN) = \\log_a M + \\log_a N, \\quad '
                                      '\\log_a\\left(\\dfrac{M}{N}\\right) = \\log_a M - \\log_a N, \\quad '
                                      '\\log_a(M^\\alpha) = \\alpha\\log_a M$'},
                          {'name': 'Công thức đổi cơ số',
                           'formula': '$\\log_a b = \\dfrac{\\log_c b}{\\log_c a}, \\quad \\log_{a^\\alpha} '
                                      'b = \\dfrac{1}{\\alpha}\\log_a b$'}]}],
  'example': 'Cho $\\log_2 3 = a$. Tính $\\log_4 18$ theo $a$.',
  'example_answer': 'Ta có $\\log_4 18 = \\log_{2^2}(2 \\cdot 3^2) = \\dfrac{1}{2}(\\log_2 2 + 2\\log_2 3) = '
                    '\\dfrac{1}{2}(1 + 2a) = \\dfrac{1}{2} + a$.',
  'real_life': 'Đo độ pH trong hóa học ($\\text{pH} = -\\log[\\text{H}^+]$), độ mạnh động đất theo thang '
               'Richter và mức cường độ âm (dB).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a$ là số thực dương khác $1$, giá trị của $\\log_a (a^3)$ bằng:',
            'options': ['$1$', '$\\dfrac{1}{3}$', '$3$', '$0$'],
            'answer': 2,
            'solution': 'Theo tính chất cơ bản của lôgarit, $\\log_a (a^3) = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Với $a, b$ là hai số thực dương tùy ý, $\\ln(ab)$ bằng:',
            'options': ['$\\ln a \\cdot \\ln b$',
                        '$\\ln a - \\ln b$',
                        '$\\dfrac{\\ln a}{\\ln b}$',
                        '$\\ln a + \\ln b$'],
            'answer': 3,
            'solution': 'Theo quy tắc lôgarit của một tích: $\\ln(ab) = \\ln a + \\ln b$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 19: Lôgarit**, công thức hoặc quy tắc nào sau đây biểu '
                 'diễn đúng **Định nghĩa và tính chất cơ bản**?',
            'options': ['$\\log_a b = \\alpha \\Leftrightarrow a^\\alpha = b; \\quad \\log_a 1 = 0, \\quad '
                        '\\log_a a = 1$',
                        '$\\log_a(MN) = \\log_a M + \\log_a N, \\quad \\log_a\\left(\\dfrac{M}{N}\\right) = '
                        '\\log_a M - \\log_a N, \\quad \\log_a(M^\\alpha) = \\alpha\\log_a M$',
                        '$\\log_a b = \\dfrac{\\log_c b}{\\log_c a}, \\quad \\log_{a^\\alpha} b = '
                        '\\dfrac{1}{\\alpha}\\log_a b$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 19: Lôgarit, **Định nghĩa và tính chất cơ '
                        'bản** được xác định bởi: $\\log_a b = \\alpha \\Leftrightarrow a^\\alpha = b; '
                        '\\quad \\log_a 1 = 0, \\quad \\log_a a = 1$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Lôgarit**, nội dung/biểu thức $\\log_a(MN) = \\log_a M + \\log_a N, \\quad '
                 '\\log_a\\left(\\dfrac{M}{N}\\right) = \\log_a M - \\log_a N, \\quad \\log_a(M^\\alpha) = '
                 '\\alpha\\log_a M$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa và tính chất cơ bản',
                        'Lôgarit của tích, thương, lũy thừa',
                        'Công thức đổi cơ số',
                        'Đổi độ và radian'],
            'answer': 1,
            'solution': 'Trong Bài 19: Lôgarit, biểu thức/quy tắc $\\log_a(MN) = \\log_a M + \\log_a N, '
                        '\\quad \\log_a\\left(\\dfrac{M}{N}\\right) = \\log_a M - \\log_a N, \\quad '
                        '\\log_a(M^\\alpha) = \\alpha\\log_a M$ chính là nội dung của **Lôgarit của tích, '
                        'thương, lũy thừa**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $P = \\log_2 8 + \\log_3 \\dfrac{1}{9}$ bằng:',
            'options': ['$5$', '$-1$', '$1$', '$3$'],
            'answer': 2,
            'solution': 'Ta có $\\log_2 8 = \\log_2 (2^3) = 3$ và $\\log_3 \\dfrac{1}{9} = \\log_3 (3^{-2}) '
                        '= -2$. Vậy $P = 3 + (-2) = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Lôgarit** (Chương VI: Hàm số mũ và hàm số lôgarit), khẳng định nào sau '
                 'đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Hiểu được định nghĩa lôgarit: với $0 < a \\ne 1, b > 0$ thì $\\alpha = \\log_a b '
                        '\\Leftrightarrow a^\\alpha = b$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 19: Lôgarit: Hiểu được định nghĩa lôgarit: với $0 < a '
                        '\\ne 1, b > 0$ thì $\\alpha = \\log_a b \\Leftrightarrow a^\\alpha = b$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai số thực dương $a, b$ thỏa mãn $\\log_2 a = 3$ và $\\log_2 b = 5$. Xét tính đúng '
                 'sai của các mệnh đề sau:',
            'statements': ['Giá trị của $a$ bằng $8$.',
                           'Giá trị của $\\log_2(ab)$ bằng $8$.',
                           'Giá trị của $\\log_2\\left(\\dfrac{a^2}{b}\\right)$ bằng $1$.',
                           'Giá trị của $\\log_a b$ bằng $\\dfrac{3}{5}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $a = 2^3 = 8$. b) Đúng vì $\\log_2(ab) = \\log_2 a + \\log_2 b = 3 + 5 = '
                        '8$. c) Đúng vì $2\\log_2 a - \\log_2 b = 6 - 5 = 1$. d) Sai vì theo công thức đổi '
                        'cơ số $\\log_a b = \\dfrac{\\log_2 b}{\\log_2 a} = \\dfrac{5}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 19: Lôgarit**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được định nghĩa lôgarit: với '
                           '$0 < a \\ne 1, b > 0$ thì $\\alpha = \\log_a b \\Leftrightarrow a^\\alpha = b$.',
                           'Quy tắc/công thức **Định nghĩa và tính chất cơ bản** trong bài được xác định '
                           'bởi: $\\log_a b = \\alpha \\Leftrightarrow a^\\alpha = b; \\quad \\log_a 1 = 0, '
                           '\\quad \\log_a a = 1$.',
                           'Trong mọi trường hợp, **Định nghĩa và tính chất cơ bản** luôn được tính bằng '
                           'công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                           'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) '
                           'mà không cần điều kiện của Bài 19: Lôgarit.',
                           'Với bài toán minh họa: “Cho $\\log_2 3 = a$. Tính $\\log_4 18$ theo $a$.”, lời '
                           'giải đúng là: Ta có $\\log_4 18 = \\log_{2^2}(2 \\cdot 3^2) = '
                           '\\dfrac{1}{2}(\\log_2 2 + 2\\log_2 3) = \\dfrac{1}{2}(1 + 2a) = \\dfrac{1}{2} + '
                           'a$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Lôgarit. b) **Đúng** theo công thức '
                        'trọng tâm **Định nghĩa và tính chất cơ bản** ($\\log_a b = \\alpha \\Leftrightarrow '
                        'a^\\alpha = b; \\quad \\log_a 1 = 0, \\quad \\log_a a = 1$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa và tính chất cơ bản**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 19: Lôgarit** để giải quyết tình huống sau: Cho $\\log_2 3 = a$. '
                 'Tính $\\log_4 18$ theo $a$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Ta có $\\log_4 18 = \\log_{2^2}(2 \\cdot 3^2) = \\dfrac{1}{2}(\\log_2 2 + 2\\log_2 '
                        '3) = \\dfrac{1}{2}(1 + 2a) = \\dfrac{1}{2} + a$.',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Lôgarit: Ta có $\\log_4 18 = \\log_{2^2}(2 \\cdot '
                        '3^2) = \\dfrac{1}{2}(\\log_2 2 + 2\\log_2 3) = \\dfrac{1}{2}(1 + 2a) = '
                        '\\dfrac{1}{2} + a$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $T = \\log_2 3 \\cdot \\log_3 4 \\cdot \\log_4 8$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Áp dụng công thức đổi cơ số: $T = \\log_2 3 \\cdot \\dfrac{\\log_2 4}{\\log_2 3} '
                        '\\cdot \\dfrac{\\log_2 8}{\\log_2 4} = \\log_2 8 = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch06-mu-logarit',
  'context_title': 'Chương VI: Hàm số mũ và hàm số lôgarit',
  'context': 'Chương VI · SGK Toán 11: Lũy thừa với số mũ thực, lôgarit, hàm số mũ, hàm số lôgarit và phương '
             'trình, bất phương trình mũ - lôgarit.',
  'title': 'Bài 20: Hàm số mũ và hàm số lôgarit',
  'icon': '📈',
  'description': 'Tập xác định, tập giá trị, sự biến thiên và đồ thị của hàm số mũ y = a^x và hàm số lôgarit '
                 'y = log_a x.',
  'requirements': ['Xác định được tập xác định, tập giá trị và điểm đặc biệt của hàm số mũ $y = a^x$ và hàm '
                   'số lôgarit $y = \\log_a x$ ($0 < a \\ne 1$).',
                   'Nhận biết được tính đồng biến khi $a > 1$ và nghịch biến khi $0 < a < 1$ của cả hai hàm '
                   'số.',
                   'Tìm được tập xác định của hàm số lôgarit hợp $y = \\log_a u(x)$.'],
  'definition': 'Cho cơ số $a > 0, a \\ne 1$. Hàm số $y = a^x$ được gọi là hàm số mũ cơ số $a$ (tập xác định '
                '$\\mathbb{R}$, tập giá trị $(0; +\\infty)$). Hàm số $y = \\log_a x$ được gọi là hàm số '
                'lôgarit cơ số $a$ (tập xác định $(0; +\\infty)$, tập giá trị $\\mathbb{R}$).',
  'theory': '1. Cả hai hàm số $y = a^x$ và $y = \\log_a x$ đều đồng biến trên tập xác định khi $a > 1$ và '
            'nghịch biến trên tập xác định khi $0 < a < 1$. 2. Đồ thị hàm số $y = a^x$ luôn đi qua $(0; 1)$ '
            'và nhận trục hoành $Ox$ làm tiệm cận ngang. 3. Đồ thị hàm số $y = \\log_a x$ luôn đi qua $(1; '
            '0)$ và nhận trục tung $Oy$ làm tiệm cận đứng.',
  'formulas': [{'category': 'Đặc trưng hàm số mũ và hàm số lôgarit (0 < a ≠ 1)',
                'items': [{'name': 'Hàm số mũ y = a^x',
                           'formula': '$D = \\mathbb{R}, \\quad T = (0; +\\infty), \\quad \\text{đi qua } '
                                      '(0; 1)$'},
                          {'name': 'Hàm số lôgarit y = log_a x',
                           'formula': '$D = (0; +\\infty), \\quad T = \\mathbb{R}, \\quad \\text{đi qua } '
                                      '(1; 0)$'},
                          {'name': 'Chiều biến thiên',
                           'formula': '$a > 1 \\Rightarrow \\text{đồng biến}; \\quad 0 < a < 1 \\Rightarrow '
                                      '\\text{nghịch biến}$'}]}],
  'example': 'Tìm tập xác định của hàm số $y = \\log_3 (2x - 4)$.',
  'example_answer': 'Hàm số xác định khi và chỉ khi biểu thức trong lôgarit dương: $2x - 4 > 0 '
                    '\\Leftrightarrow x > 2$. Vậy tập xác định của hàm số là $D = (2; +\\infty)$.',
  'real_life': 'Mô hình hóa sự tăng trưởng dân số theo hàm số mũ $P(t) = P_0 e^{rt}$ và sự phân rã phóng xạ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tập xác định của hàm số $y = \\log_2 x$ là:',
            'options': ['$\\mathbb{R}$',
                        '$[0; +\\infty)$',
                        '$\\mathbb{R} \\setminus \\{0\\}$',
                        '$(0; +\\infty)$'],
            'answer': 3,
            'solution': 'Hàm số lôgarit $y = \\log_2 x$ có tập xác định là $D = (0; +\\infty)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các hàm số dưới đây, hàm số nào nghịch biến trên $\\mathbb{R}$?',
            'options': ['$y = \\left(\\dfrac{1}{2}\\right)^x$',
                        '$y = 2^x$',
                        '$y = e^x$',
                        '$y = \\log_{\\frac{1}{2}} x$'],
            'answer': 0,
            'solution': 'Hàm số mũ $y = \\left(\\dfrac{1}{2}\\right)^x$ có cơ số $a = \\dfrac{1}{2} \\in (0; '
                        '1)$ nên nghịch biến trên toàn bộ $\\mathbb{R}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 20: Hàm số mũ và hàm số lôgarit**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hàm số mũ y = a^x**?',
            'options': ['$D = (0; +\\infty), \\quad T = \\mathbb{R}, \\quad \\text{đi qua } (1; 0)$',
                        '$D = \\mathbb{R}, \\quad T = (0; +\\infty), \\quad \\text{đi qua } (0; 1)$',
                        '$a > 1 \\Rightarrow \\text{đồng biến}; \\quad 0 < a < 1 \\Rightarrow \\text{nghịch '
                        'biến}$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 20: Hàm số mũ và hàm số lôgarit, **Hàm số mũ '
                        'y = a^x** được xác định bởi: $D = \\mathbb{R}, \\quad T = (0; +\\infty), \\quad '
                        '\\text{đi qua } (0; 1)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Hàm số mũ và hàm số lôgarit**, nội dung/biểu thức $D = (0; +\\infty), '
                 '\\quad T = \\mathbb{R}, \\quad \\text{đi qua } (1; 0)$ là quy tắc hoặc công thức của mục '
                 'nào sau đây?',
            'options': ['Hàm số mũ y = a^x',
                        'Chiều biến thiên',
                        'Hàm số lôgarit y = log_a x',
                        'Đổi độ và radian'],
            'answer': 2,
            'solution': 'Trong Bài 20: Hàm số mũ và hàm số lôgarit, biểu thức/quy tắc $D = (0; +\\infty), '
                        '\\quad T = \\mathbb{R}, \\quad \\text{đi qua } (1; 0)$ chính là nội dung của **Hàm '
                        'số lôgarit y = log_a x**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tập xác định của hàm số $y = \\ln(x - 3)$ là:',
            'options': ['$[3; +\\infty)$',
                        '$(-\\infty; 3)$',
                        '$\\mathbb{R} \\setminus \\{3\\}$',
                        '$(3; +\\infty)$'],
            'answer': 3,
            'solution': 'Điều kiện xác định: $x - 3 > 0 \\Leftrightarrow x > 3$, nên $D = (3; +\\infty)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Hàm số mũ và hàm số lôgarit** (Chương VI: Hàm số mũ và hàm số lôgarit), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Xác định được tập xác định, tập giá trị và điểm đặc biệt của hàm số mũ $y = a^x$ và '
                        'hàm số lôgarit $y = \\log_a x$ ($0 < a \\ne 1$).',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 20: Hàm số mũ và hàm số lôgarit: Xác định được tập xác '
                        'định, tập giá trị và điểm đặc biệt của hàm số mũ $y = a^x$ và hàm số lôgarit $y = '
                        '\\log_a x$ ($0 < a \\ne 1$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số mũ $f(x) = 3^x$ và hàm số lôgarit $g(x) = \\log_3 x$. Xét tính đúng sai của các '
                 'mệnh đề sau:',
            'statements': ['Hàm số $f(x) = 3^x$ đồng biến trên $\\mathbb{R}$.',
                           'Đồ thị hàm số $f(x) = 3^x$ luôn đi qua điểm $(0; 1)$.',
                           'Hàm số $g(x) = \\log_3 x$ có tập xác định là $\\mathbb{R}$.',
                           'Đồ thị của hai hàm số $f(x)$ và $g(x)$ đối xứng với nhau qua đường phân giác $y '
                           '= x$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì cơ số $a = 3 > 1$. b) Đúng vì $3^0 = 1$. c) Sai vì tập xác định của '
                        '$g(x) = \\log_3 x$ là $(0; +\\infty)$. d) Đúng vì $y = 3^x$ và $y = \\log_3 x$ là '
                        'hai hàm ngược nhau.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 20: Hàm số mũ và hàm số '
                 'lôgarit**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được tập xác định, tập '
                           'giá trị và điểm đặc biệt của hàm số mũ $y = a^x$ và hàm số lôgarit $y = \\log_a '
                           'x$ ($0 < a \\ne 1$).',
                           'Quy tắc/công thức **Hàm số mũ y = a^x** trong bài được xác định bởi: $D = '
                           '\\mathbb{R}, \\quad T = (0; +\\infty), \\quad \\text{đi qua } (0; 1)$.',
                           'Trong mọi trường hợp, **Hàm số mũ y = a^x** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 20: Hàm số mũ và hàm số lôgarit.',
                           'Với bài toán minh họa: “Tìm tập xác định của hàm số $y = \\log_3 (2x - 4)$.”, '
                           'lời giải đúng là: Hàm số xác định khi và chỉ khi biểu thức trong lôgarit dương: '
                           '$2x - 4 > 0 \\Leftrightarrow x > 2$. Vậy tập xác định của hàm số là $D = (2; '
                           '+\\infty)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Hàm số mũ và hàm số lôgarit. b) '
                        '**Đúng** theo công thức trọng tâm **Hàm số mũ y = a^x** ($D = \\mathbb{R}, \\quad T '
                        '= (0; +\\infty), \\quad \\text{đi qua } (0; 1)$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Hàm số mũ y = a^x**. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 20: Hàm số mũ và hàm số lôgarit** để giải quyết tình huống sau: '
                 'Tìm tập xác định của hàm số $y = \\log_3 (2x - 4)$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Hàm số xác định khi và chỉ khi biểu thức trong lôgarit dương: $2x - 4 > 0 '
                        '\\Leftrightarrow x > 2$. Vậy tập xác định của hàm số là $D = (2; +\\infty)$.',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Hàm số mũ và hàm số lôgarit: Hàm số xác định khi và '
                        'chỉ khi biểu thức trong lôgarit dương: $2x - 4 > 0 \\Leftrightarrow x > 2$. Vậy tập '
                        'xác định của hàm số là $D = (2; +\\infty)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Có bao nhiêu giá trị nguyên của $x$ thuộc tập xác định của hàm số $y = \\log_2 (9 - x^2)$?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Điều kiện xác định: $9 - x^2 > 0 \\Leftrightarrow -3 < x < 3$. Các giá trị nguyên '
                        'của $x$ là $\\{-2; -1; 0; 1; 2\\}$, có tất cả $5$ giá trị.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch06-mu-logarit',
  'context_title': 'Chương VI: Hàm số mũ và hàm số lôgarit',
  'context': 'Chương VI · SGK Toán 11: Lũy thừa với số mũ thực, lôgarit, hàm số mũ, hàm số lôgarit và phương '
             'trình, bất phương trình mũ - lôgarit.',
  'title': 'Bài 21: Phương trình, bất phương trình mũ và lôgarit',
  'icon': '🔑',
  'description': 'Cách giải phương trình, bất phương trình mũ và lôgarit cơ bản bằng phương pháp đưa về cùng '
                 'cơ số hoặc lấy lôgarit.',
  'requirements': ['Giải được phương trình mũ cơ bản $a^x = b$ và phương trình lôgarit cơ bản $\\log_a x = '
                   'b$ (kết hợp điều kiện xác định).',
                   'Giải được bất phương trình mũ và bất phương trình lôgarit bằng cách chú ý chiều bất đẳng '
                   'thức khi $a > 1$ và khi $0 < a < 1$.',
                   'Vận dụng giải các bài toán thực tế về thời gian gửi tiết kiệm và dân số.'],
  'definition': 'Phương trình mũ cơ bản có dạng $a^x = b$ ($0 < a \\ne 1$): có nghiệm duy nhất $x = \\log_a '
                'b$ khi $b > 0$ và vô nghiệm khi $b \\le 0$. Phương trình lôgarit cơ bản có dạng $\\log_a x '
                '= b$ ($0 < a \\ne 1$): luôn có nghiệm duy nhất $x = a^b > 0$ với mọi $b \\in \\mathbb{R}$.',
  'theory': '1. Đưa về cùng cơ số ($0 < a \\ne 1$): $a^{f(x)} = a^{g(x)} \\Leftrightarrow f(x) = g(x)$; '
            '$\\log_a f(x) = \\log_a g(x) \\Leftrightarrow f(x) = g(x) > 0$. 2. Bất phương trình mũ: nếu $a '
            '> 1$ thì $a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x)$ (giữ chiều); nếu $0 < a < 1$ thì '
            '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) < g(x)$ (đổi chiều). 3. Bất phương trình lôgarit: '
            'luôn phải đặt điều kiện xác định $f(x) > 0, g(x) > 0$ và đổi chiều khi $0 < a < 1$.',
  'formulas': [{'category': 'Phương trình và bất phương trình mũ - lôgarit (0 < a ≠ 1)',
                'items': [{'name': 'Phương trình cơ bản',
                           'formula': '$a^x = b \\quad (b > 0) \\Leftrightarrow x = \\log_a b; \\quad '
                                      '\\log_a x = b \\Leftrightarrow x = a^b$'},
                          {'name': 'Bất phương trình khi a > 1 (giữ chiều)',
                           'formula': '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x); \\quad \\log_a '
                                      'f(x) > \\log_a g(x) \\Leftrightarrow f(x) > g(x) > 0$'},
                          {'name': 'Bất phương trình khi 0 < a < 1 (đổi chiều)',
                           'formula': '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) < g(x); \\quad \\log_a '
                                      'f(x) > \\log_a g(x) \\Leftrightarrow 0 < f(x) < g(x)$'}]}],
  'example': 'Giải bất phương trình $\\log_{\\frac{1}{2}} (x - 1) \\ge -2$.',
  'example_answer': 'Điều kiện: $x - 1 > 0 \\Leftrightarrow x > 1$. Vì cơ số $a = \\dfrac{1}{2} \\in (0; 1)$ '
                    'nên bất phương trình tương đương với $x - 1 \\le \\left(\\dfrac{1}{2}\\right)^{-2} = 4 '
                    '\\Leftrightarrow x \\le 5$. Kết hợp điều kiện ta được nghiệm $1 < x \\le 5$.',
  'real_life': 'Tính số năm tối thiểu cần gửi ngân hàng để số tiền tiết kiệm tăng gấp đôi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $2^{x - 1} = 8$ là:',
            'options': ['$x = 4$', '$x = 3$', '$x = 2$', '$x = 5$'],
            'answer': 0,
            'solution': 'Ta có $2^{x - 1} = 2^3 \\Leftrightarrow x - 1 = 3 \\Leftrightarrow x = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $\\log_3 (x - 2) = 2$ là:',
            'options': ['$x = 8$', '$x = 11$', '$x = 10$', '$x = 7$'],
            'answer': 1,
            'solution': 'Ta có $x - 2 = 3^2 = 9 \\Leftrightarrow x = 11$ (thỏa mãn điều kiện $x > 2$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 21: Phương trình, bất phương trình mũ và lôgarit**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Phương trình cơ bản**?',
            'options': ['$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x); \\quad \\log_a f(x) > \\log_a '
                        'g(x) \\Leftrightarrow f(x) > g(x) > 0$',
                        '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) < g(x); \\quad \\log_a f(x) > \\log_a '
                        'g(x) \\Leftrightarrow 0 < f(x) < g(x)$',
                        '$a^x = b \\quad (b > 0) \\Leftrightarrow x = \\log_a b; \\quad \\log_a x = b '
                        '\\Leftrightarrow x = a^b$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 21: Phương trình, bất phương trình mũ và '
                        'lôgarit, **Phương trình cơ bản** được xác định bởi: $a^x = b \\quad (b > 0) '
                        '\\Leftrightarrow x = \\log_a b; \\quad \\log_a x = b \\Leftrightarrow x = a^b$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Phương trình, bất phương trình mũ và lôgarit**, nội dung/biểu thức '
                 '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x); \\quad \\log_a f(x) > \\log_a g(x) '
                 '\\Leftrightarrow f(x) > g(x) > 0$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Phương trình cơ bản',
                        'Bất phương trình khi 0 < a < 1 (đổi chiều)',
                        'Đổi độ và radian',
                        'Bất phương trình khi a > 1 (giữ chiều)'],
            'answer': 3,
            'solution': 'Trong Bài 21: Phương trình, bất phương trình mũ và lôgarit, biểu thức/quy tắc '
                        '$a^{f(x)} > a^{g(x)} \\Leftrightarrow f(x) > g(x); \\quad \\log_a f(x) > \\log_a '
                        'g(x) \\Leftrightarrow f(x) > g(x) > 0$ chính là nội dung của **Bất phương trình khi '
                        'a > 1 (giữ chiều)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tập nghiệm của bất phương trình $\\left(\\dfrac{1}{3}\\right)^x > \\dfrac{1}{9}$ là:',
            'options': ['$(-\\infty; 2)$', '$(2; +\\infty)$', '$(0; 2)$', '$(-\\infty; 3)$'],
            'answer': 0,
            'solution': 'Vì cơ số $\\dfrac{1}{3} \\in (0; 1)$ nên $\\left(\\dfrac{1}{3}\\right)^x > '
                        '\\left(\\dfrac{1}{3}\\right)^2 \\Leftrightarrow x < 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Phương trình, bất phương trình mũ và lôgarit** (Chương VI: Hàm số mũ và '
                 'hàm số lôgarit), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Giải được phương trình mũ cơ bản $a^x = b$ và phương trình lôgarit cơ bản $\\log_a '
                        'x = b$ (kết hợp điều kiện xác định).',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 21: Phương trình, bất phương trình mũ và lôgarit: Giải '
                        'được phương trình mũ cơ bản $a^x = b$ và phương trình lôgarit cơ bản $\\log_a x = '
                        'b$ (kết hợp điều kiện xác định).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho bất phương trình lôgarit $\\log_2 (2x - 4) < 3$. Xét tính đúng sai của các mệnh đề '
                 'sau:',
            'statements': ['Điều kiện xác định của bất phương trình là $x > 2$.',
                           'Vì cơ số $2 > 1$ nên bất phương trình tương đương với $2x - 4 < 8$ (kết hợp điều '
                           'kiện).',
                           'Tập nghiệm của bất phương trình là $(-\\infty; 6)$.',
                           'Có đúng $3$ nghiệm nguyên thỏa mãn bất phương trình đã cho.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $2x - 4 > 0 \\Leftrightarrow x > 2$. b) Đúng vì $2^3 = 8$. c) Sai vì kết '
                        'hợp điều kiện $x > 2$, tập nghiệm phải là $(2; 6)$. d) Đúng vì các nghiệm nguyên '
                        'trong $(2; 6)$ là $\\{3; 4; 5\\}$, gồm $3$ giá trị.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 21: Phương trình, bất '
                 'phương trình mũ và lôgarit**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Giải được phương trình mũ cơ bản '
                           '$a^x = b$ và phương trình lôgarit cơ bản $\\log_a x = b$ (kết hợp điều kiện xác '
                           'định).',
                           'Quy tắc/công thức **Phương trình cơ bản** trong bài được xác định bởi: $a^x = b '
                           '\\quad (b > 0) \\Leftrightarrow x = \\log_a b; \\quad \\log_a x = b '
                           '\\Leftrightarrow x = a^b$.',
                           'Trong mọi trường hợp, **Phương trình cơ bản** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 21: Phương trình, bất phương trình mũ và lôgarit.',
                           'Với bài toán minh họa: “Giải bất phương trình $\\log_{\\frac{1}{2}} (x - 1) \\ge '
                           '-2$.”, lời giải đúng là: Điều kiện: $x - 1 > 0 \\Leftrightarrow x > 1$. Vì cơ số '
                           '$a = \\dfrac{1}{2} \\in (0; 1)$ nên bất phương trình tương đương với $x - 1 \\le '
                           '\\left(\\dfrac{1}{2}\\right)^{-2} = 4 \\Leftrightarrow x \\le 5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Phương trình, bất phương trình mũ và '
                        'lôgarit. b) **Đúng** theo công thức trọng tâm **Phương trình cơ bản** ($a^x = b '
                        '\\quad (b > 0) \\Leftrightarrow x = \\log_a b; \\quad \\log_a x = b '
                        '\\Leftrightarrow x = a^b$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ '
                        'rad}, \\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ '
                        'là công thức của nội dung khác, không phải quy tắc chung của **Phương trình cơ '
                        'bản**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 21: Phương trình, bất phương trình mũ và lôgarit** để giải quyết '
                 'tình huống sau: Giải bất phương trình $\\log_{\\frac{1}{2}} (x - 1) \\ge -2$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Điều kiện: $x - 1 > 0 \\Leftrightarrow x > 1$. Vì cơ số $a = \\dfrac{1}{2} \\in (0; '
                        '1)$ nên bất phương trình tương đương với $x - 1 \\le '
                        '\\left(\\dfrac{1}{2}\\right)^{-2} = 4 \\Leftrightarrow x \\le 5$...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Phương trình, bất phương trình mũ và lôgarit: Điều '
                        'kiện: $x - 1 > 0 \\Leftrightarrow x > 1$. Vì cơ số $a = \\dfrac{1}{2} \\in (0; 1)$ '
                        'nên bất phương trình tương đương với $x - 1 \\le \\left(\\dfrac{1}{2}\\right)^{-2} '
                        '= 4 \\Leftrightarrow x \\le 5$. Kết hợp điều kiện ta được nghiệm $1 < x \\le 5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính tổng tất cả các nghiệm của phương trình $3^{x^2 - 4x + 5} = 9$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $3^{x^2 - 4x + 5} = 3^2 \\Leftrightarrow x^2 - 4x + 5 = 2 \\Leftrightarrow '
                        'x^2 - 4x + 3 = 0 \\Leftrightarrow x = 1$ hoặc $x = 3$. Tổng các nghiệm bằng $1 + 3 '
                        '= 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 22: Hai đường thẳng vuông góc',
  'icon': '➕',
  'description': 'Góc giữa hai đường thẳng bất kì trong không gian và định nghĩa, tính chất của hai đường '
                 'thẳng vuông góc trong không gian.',
  'requirements': ['Xác định được góc giữa hai đường thẳng $a$ và $b$ trong không gian với số đo thuộc đoạn '
                   '$[0^\\circ; 90^\\circ]$.',
                   'Hiểu được hai đường thẳng vuông góc trong không gian có thể cắt nhau hoặc chéo nhau.',
                   "Chứng minh được hai đường thẳng vuông góc thông qua quan hệ song song ($a \\parallel a'$ "
                   "và $a' \\perp b \\Rightarrow a \\perp b$)."],
  'definition': "Góc giữa hai đường thẳng $a$ và $b$ trong không gian là góc giữa hai đường thẳng $a'$ và "
                "$b'$ cùng đi qua một điểm $O$ và lần lượt song song (hoặc trùng) với $a$ và $b$. Hai đường "
                'thẳng $a$ và $b$ được gọi là vuông góc với nhau, kí hiệu $a \\perp b$, nếu góc giữa chúng '
                'bằng $90^\\circ$.',
  'theory': '1. Góc giữa hai đường thẳng trong không gian luôn thỏa mãn $0^\\circ \\le (a, b) \\le '
            '90^\\circ$. 2. Nếu một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó '
            'cũng vuông góc với đường thẳng còn lại: $a \\parallel b$ và $c \\perp a \\Rightarrow c \\perp '
            'b$. 3. Hai đường thẳng vuông góc trong không gian có thể cắt nhau hoặc chéo nhau.',
  'formulas': [{'category': 'Góc và sự vuông góc của hai đường thẳng',
                'items': [{'name': 'Khoảng giá trị góc giữa hai đường thẳng',
                           'formula': '$0^\\circ \\le (a, b) \\le 90^\\circ$'},
                          {'name': 'Hai đường thẳng vuông góc',
                           'formula': '$a \\perp b \\Leftrightarrow (a, b) = 90^\\circ$'},
                          {'name': 'Quan hệ giữa song song và vuông góc',
                           'formula': '$\\begin{cases} a \\parallel b \\\\ c \\perp a \\end{cases} '
                                      '\\Rightarrow c \\perp b$'}]}],
  'example': "Cho hình lập phương $ABCD.A'B'C'D'$. Tính góc giữa hai đường thẳng $AB$ và $B'C'$; góc giữa "
             "$AB$ và $A'C'$.",
  'example_answer': "Vì $B'C' \\parallel BC$ và $AB \\perp BC$ nên $(AB, B'C') = (AB, BC) = 90^\\circ$. Vì "
                    "$A'C' \\parallel AC$ và $\\triangle ABC$ vuông cân tại $B$ nên $(AB, A'C') = (AB, AC) = "
                    '\\widehat{BAC} = 45^\\circ$.',
  'real_life': 'Kiểm tra độ vuông góc giữa cột trụ thẳng đứng và các thanh xà ngang nằm ở các tầng khác nhau '
               'của công trình xây dựng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Góc $\\varphi$ giữa hai đường thẳng bất kì trong không gian luôn thỏa mãn:',
            'options': ['$0^\\circ \\le \\varphi \\le 180^\\circ$',
                        '$0^\\circ \\le \\varphi \\le 90^\\circ$',
                        '$0^\\circ < \\varphi < 90^\\circ$',
                        '$0^\\circ \\le \\varphi \\le 360^\\circ$'],
            'answer': 1,
            'solution': 'Góc giữa hai đường thẳng trong không gian luôn không vượt quá $90^\\circ$, tức là '
                        '$0^\\circ \\le \\varphi \\le 90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai đường thẳng song song $a$ và $b$. Nếu đường thẳng $c$ vuông góc với $a$ thì:',
            'options': ['$c$ song song với $b$.',
                        '$c$ trùng với $b$.',
                        '$c$ vuông góc với $b$.',
                        'Góc giữa $c$ và $b$ bằng $45^\\circ$.'],
            'answer': 2,
            'solution': 'Nếu $a \\parallel b$ và $c \\perp a$ thì góc giữa $c$ và $b$ bằng góc giữa $c$ và '
                        '$a$, tức bằng $90^\\circ$, nên $c \\perp b$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 22: Hai đường thẳng vuông góc**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Khoảng giá trị góc giữa hai đường thẳng**?',
            'options': ['$a \\perp b \\Leftrightarrow (a, b) = 90^\\circ$',
                        '$\\begin{cases} a \\parallel b \\\\ c \\perp a \\end{cases} \\Rightarrow c \\perp '
                        'b$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$0^\\circ \\le (a, b) \\le 90^\\circ$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 22: Hai đường thẳng vuông góc, **Khoảng giá '
                        'trị góc giữa hai đường thẳng** được xác định bởi: $0^\\circ \\le (a, b) \\le '
                        '90^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Hai đường thẳng vuông góc**, nội dung/biểu thức $a \\perp b '
                 '\\Leftrightarrow (a, b) = 90^\\circ$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Hai đường thẳng vuông góc',
                        'Khoảng giá trị góc giữa hai đường thẳng',
                        'Quan hệ giữa song song và vuông góc',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 22: Hai đường thẳng vuông góc, biểu thức/quy tắc $a \\perp b '
                        '\\Leftrightarrow (a, b) = 90^\\circ$ chính là nội dung của **Hai đường thẳng vuông '
                        'góc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho hình lập phương $ABCD.A'B'C'D'$. Góc giữa hai đường thẳng $AB'$ và $BC'$ bằng:",
            'options': ['$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$30^\\circ$'],
            'answer': 1,
            'solution': "Vì $BC' \\parallel AD'$ nên $(AB', BC') = (AB', AD')$. Tam giác $AB'D'$ có $AB' = "
                        "AD' = B'D'$ (đường chéo các mặt hình vuông bằng nhau) nên là tam giác đều, suy ra "
                        'góc bằng $60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Hai đường thẳng vuông góc** (Chương VII: Quan hệ vuông góc trong không '
                 'gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của '
                 'bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Xác định được góc giữa hai đường thẳng $a$ và $b$ trong không gian với số đo thuộc '
                        'đoạn $[0^\\circ; 90^\\circ]$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 22: Hai đường thẳng vuông góc: Xác định được góc giữa '
                        'hai đường thẳng $a$ và $b$ trong không gian với số đo thuộc đoạn $[0^\\circ; '
                        '90^\\circ]$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Xét tính đúng sai của các mệnh đề "
                 'sau:',
            'statements': ["Hai đường thẳng $AA'$ và $BC$ vuông góc với nhau.",
                           "Hai đường thẳng $AA'$ và $BC$ cắt nhau.",
                           "Góc giữa hai đường thẳng $AC$ và $B'D'$ bằng $90^\\circ$.",
                           "Góc giữa hai đường thẳng $AB$ và $CD'$ bằng $45^\\circ$."],
            'answer': [True, False, True, True],
            'solution': "a) Đúng vì $BC \\parallel AD$ và $AA' \\perp AD$. b) Sai vì $AA'$ và $BC$ chéo "
                        "nhau. c) Đúng vì $B'D' \\parallel BD$ và $AC \\perp BD$. d) Đúng vì $AB \\parallel "
                        "CD$ nên $(AB, CD') = (CD, CD') = 45^\\circ$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 22: Hai đường thẳng '
                 'vuông góc**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được góc giữa hai đường '
                           'thẳng $a$ và $b$ trong không gian với số đo thuộc đoạn $[0^\\circ; 90^\\circ]$.',
                           'Quy tắc/công thức **Khoảng giá trị góc giữa hai đường thẳng** trong bài được xác '
                           'định bởi: $0^\\circ \\le (a, b) \\le 90^\\circ$.',
                           'Trong mọi trường hợp, **Khoảng giá trị góc giữa hai đường thẳng** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 22: Hai đường thẳng vuông góc.',
                           "Với bài toán minh họa: “Cho hình lập phương $ABCD.A'B'C'D'$. Tính góc giữa hai "
                           "đường thẳng $AB$ và $B'C'$; góc giữa $AB$ và $A'C'$.”, lời giải đúng là: Vì "
                           "$B'C' \\parallel BC$ và $AB \\perp BC$ nên $(AB, B'C') = (AB, BC) = 90^\\circ$. "
                           "Vì $A'C' \\parallel AC$ và $\\triangle ABC$ vuông cân tại $B$..."],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Hai đường thẳng vuông góc. b) **Đúng** '
                        'theo công thức trọng tâm **Khoảng giá trị góc giữa hai đường thẳng** ($0^\\circ '
                        '\\le (a, b) \\le 90^\\circ$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ '
                        'rad}, \\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ '
                        'là công thức của nội dung khác, không phải quy tắc chung của **Khoảng giá trị góc '
                        'giữa hai đường thẳng**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 22: Hai đường thẳng vuông góc** để giải quyết tình huống sau: Cho '
                 "hình lập phương $ABCD.A'B'C'D'$. Tính góc giữa hai đường thẳng $AB$ và $B'C'$; góc giữa "
                 "$AB$ và $A'C'$. Kết quả và hướng giải nào dưới đây là **đúng**?",
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        "Vì $B'C' \\parallel BC$ và $AB \\perp BC$ nên $(AB, B'C') = (AB, BC) = 90^\\circ$. "
                        "Vì $A'C' \\parallel AC$ và $\\triangle ABC$ vuông cân tại $B$ nên $(AB, A'C') = "
                        '(AB, AC) = \\widehat{BAC} = 45^\\circ$...'],
            'answer': 3,
            'solution': "Lời giải chi tiết theo Bài 22: Hai đường thẳng vuông góc: Vì $B'C' \\parallel BC$ "
                        "và $AB \\perp BC$ nên $(AB, B'C') = (AB, BC) = 90^\\circ$. Vì $A'C' \\parallel AC$ "
                        "và $\\triangle ABC$ vuông cân tại $B$ nên $(AB, A'C') = (AB, AC) = \\widehat{BAC} = "
                        '45^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tứ diện $ABCD$ có $AB = CD = 2a$. Gọi $M, N, P$ lần lượt là trung điểm của $BC, AD, '
                 'AC$ và biết $MN = a\\sqrt{3}$. Tính số đo góc giữa hai đường thẳng $AB$ và $CD$ (đơn vị: '
                 'độ).',
            'answer': ['60'],
            'unit': None,
            'solution': 'Trong $\\triangle ABC$ và $\\triangle ACD$, ta có $MP \\parallel AB, MP = a$ và $NP '
                        '\\parallel CD, NP = a$. Trong $\\triangle MNP$, $\\cos \\widehat{MPN} = \\dfrac{a^2 '
                        '+ a^2 - 3a^2}{2a^2} = -\\dfrac{1}{2} \\Rightarrow \\widehat{MPN} = 120^\\circ$. Suy '
                        'ra góc giữa $AB$ và $CD$ là $180^\\circ - 120^\\circ = 60^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 23: Đường thẳng vuông góc với mặt phẳng',
  'icon': '📍',
  'description': 'Định nghĩa, điều kiện để đường thẳng vuông góc với mặt phẳng, tính chất và liên hệ giữa '
                 'quan hệ song song với quan hệ vuông góc.',
  'requirements': ['Hiểu được định nghĩa đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ thì $d$ vuông '
                   'góc với mọi đường thẳng nằm trong $(\\alpha)$.',
                   'Vận dụng định lí điều kiện: nếu $d$ vuông góc với hai đường thẳng cắt nhau nằm trong '
                   '$(\\alpha)$ thì $d \\perp (\\alpha)$.',
                   'Chứng minh được đường thẳng vuông góc với mặt phẳng và hai đường thẳng vuông góc trong '
                   'hình chóp.'],
  'definition': 'Đường thẳng $d$ được gọi là vuông góc với mặt phẳng $(\\alpha)$, kí hiệu $d \\perp '
                '(\\alpha)$, nếu $d$ vuông góc với mọi đường thẳng $a$ nằm trong mặt phẳng $(\\alpha)$.',
  'theory': '1. Định lí nhận biết: Nếu một đường thẳng vuông góc với hai đường thẳng cắt nhau cùng thuộc một '
            'mặt phẳng thì nó vuông góc với mặt phẳng ấy. 2. Tính chất: Hai đường thẳng phân biệt cùng vuông '
            'góc với một mặt phẳng thì song song với nhau; hai mặt phẳng phân biệt cùng vuông góc với một '
            'đường thẳng thì song song với nhau. 3. Muốn chứng minh $d \\perp a$, ta thường chứng minh $a '
            '\\perp (\\alpha)$ chứa $d$.',
  'formulas': [{'category': 'Đường thẳng vuông góc với mặt phẳng',
                'items': [{'name': 'Định nghĩa',
                           'formula': '$d \\perp (\\alpha) \\Leftrightarrow d \\perp a, \\quad \\forall a '
                                      '\\subset (\\alpha)$'},
                          {'name': 'Dấu hiệu nhận biết',
                           'formula': '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ d '
                                      '\\perp a, d \\perp b \\end{cases} \\Rightarrow d \\perp (\\alpha)$'},
                          {'name': 'Liên hệ song song và vuông góc',
                           'formula': '$\\begin{cases} a \\perp (\\alpha) \\\\ b \\perp (\\alpha) '
                                      '\\end{cases} \\quad (a \\ne b) \\Rightarrow a \\parallel b$'}]}],
  'example': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$ và tam giác $ABC$ vuông tại $B$. Chứng minh $BC '
             '\\perp (SAB)$.',
  'example_answer': 'Vì $SA \\perp (ABC)$ và $BC \\subset (ABC)$ nên $BC \\perp SA$. Mặt khác tam giác $ABC$ '
                    'vuông tại $B$ nên $BC \\perp AB$. Trong $(SAB)$, hai đường thẳng $SA$ và $AB$ cắt nhau '
                    'tại $A$, suy ra $BC \\perp (SAB)$.',
  'real_life': 'Sử dụng dây dọi để kiểm tra cột nhà có vuông góc với mặt sàn nằm ngang hay không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ thì $d$:',
            'options': ['Chỉ vuông góc với hai đường thẳng trong $(\\alpha)$.',
                        'Song song với mọi đường thẳng trong $(\\alpha)$.',
                        'Vuông góc với mọi đường thẳng nằm trong $(\\alpha)$.',
                        'Cắt mọi đường thẳng trong $(\\alpha)$.'],
            'answer': 2,
            'solution': 'Theo định nghĩa, nếu $d \\perp (\\alpha)$ thì $d$ vuông góc với mọi đường thẳng nằm '
                        'trong $(\\alpha)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Để chứng minh đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$, ta cần chứng minh $d$ '
                 'vuông góc với:',
            'options': ['Hai đường thẳng song song nằm trong $(\\alpha)$.',
                        'Một đường thẳng bất kì nằm trong $(\\alpha)$.',
                        'Một đường thẳng song song với $(\\alpha)$.',
                        'Hai đường thẳng cắt nhau nằm trong $(\\alpha)$.'],
            'answer': 3,
            'solution': 'Theo định lí nhận biết, $d$ vuông góc với hai đường thẳng cắt nhau nằm trong '
                        '$(\\alpha)$ thì $d \\perp (\\alpha)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 23: Đường thẳng vuông góc với mặt phẳng**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Định nghĩa**?',
            'options': ['$d \\perp (\\alpha) \\Leftrightarrow d \\perp a, \\quad \\forall a \\subset '
                        '(\\alpha)$',
                        '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ d \\perp a, d '
                        '\\perp b \\end{cases} \\Rightarrow d \\perp (\\alpha)$',
                        '$\\begin{cases} a \\perp (\\alpha) \\\\ b \\perp (\\alpha) \\end{cases} \\quad (a '
                        '\\ne b) \\Rightarrow a \\parallel b$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 23: Đường thẳng vuông góc với mặt phẳng, '
                        '**Định nghĩa** được xác định bởi: $d \\perp (\\alpha) \\Leftrightarrow d \\perp a, '
                        '\\quad \\forall a \\subset (\\alpha)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Đường thẳng vuông góc với mặt phẳng**, nội dung/biểu thức $\\begin{cases} '
                 'a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ d \\perp a, d \\perp b \\end{cases} '
                 '\\Rightarrow d \\perp (\\alpha)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa',
                        'Dấu hiệu nhận biết',
                        'Liên hệ song song và vuông góc',
                        'Đổi độ và radian'],
            'answer': 1,
            'solution': 'Trong Bài 23: Đường thẳng vuông góc với mặt phẳng, biểu thức/quy tắc '
                        '$\\begin{cases} a, b \\subset (\\alpha), a \\cap b = \\{I\\} \\\\ d \\perp a, d '
                        '\\perp b \\end{cases} \\Rightarrow d \\perp (\\alpha)$ chính là nội dung của **Dấu '
                        'hiệu nhận biết**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông và $SA \\perp (ABCD)$. Đường thẳng $BD$ '
                 'vuông góc với mặt phẳng nào dưới đây?',
            'options': ['$(SAB)$', '$(SAD)$', '$(SAC)$', '$(SBC)$'],
            'answer': 2,
            'solution': 'Ta có $BD \\perp AC$ (hai đường chéo hình vuông) và $BD \\perp SA$ (do $SA \\perp '
                        '(ABCD)$). Mà $AC \\cap SA = \\{A\\}$ trong $(SAC)$ nên $BD \\perp (SAC)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Đường thẳng vuông góc với mặt phẳng** (Chương VII: Quan hệ vuông góc '
                 'trong không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Hiểu được định nghĩa đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ thì $d$ '
                        'vuông góc với mọi đường thẳng nằm trong $(\\alpha)$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 23: Đường thẳng vuông góc với mặt phẳng: Hiểu được '
                        'định nghĩa đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ thì $d$ vuông góc '
                        'với mọi đường thẳng nằm trong $(\\alpha)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$ và đáy $ABC$ là tam giác vuông tại $B$. Kẻ $AH '
                 '\\perp SB$ tại $H$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Đường thẳng $SA$ vuông góc với đường thẳng $BC$.',
                           'Đường thẳng $BC$ vuông góc với mặt phẳng $(SAB)$.',
                           'Đường thẳng $AH$ vuông góc với đường thẳng $BC$.',
                           'Đường thẳng $AH$ vuông góc với mặt phẳng $(SBC)$.'],
            'answer': [True, True, True, True],
            'solution': 'a) Đúng vì $SA \\perp (ABC)$ và $BC \\subset (ABC)$. b) Đúng vì $BC \\perp AB$ và '
                        '$BC \\perp SA$. c) Đúng vì $BC \\perp (SAB)$ và $AH \\subset (SAB)$. d) Đúng vì $AH '
                        '\\perp SB$ và $AH \\perp BC$, mà $SB \\cap BC = \\{B\\}$ trong $(SBC)$ nên $AH '
                        '\\perp (SBC)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 23: Đường thẳng vuông '
                 'góc với mặt phẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được định nghĩa đường thẳng '
                           '$d$ vuông góc với mặt phẳng $(\\alpha)$ thì $d$ vuông góc với mọi đường thẳng '
                           'nằm trong $(\\alpha)$.',
                           'Quy tắc/công thức **Định nghĩa** trong bài được xác định bởi: $d \\perp '
                           '(\\alpha) \\Leftrightarrow d \\perp a, \\quad \\forall a \\subset (\\alpha)$.',
                           'Trong mọi trường hợp, **Định nghĩa** luôn được tính bằng công thức $a^\\circ = '
                           '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 23: Đường thẳng vuông góc với mặt phẳng.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$ và tam giác '
                           '$ABC$ vuông tại $B$. Chứng minh $BC \\perp (SAB)$.”, lời giải đúng là: Vì $SA '
                           '\\perp (ABC)$ và $BC \\subset (ABC)$ nên $BC \\perp SA$. Mặt khác tam giác $ABC$ '
                           'vuông tại $B$ nên $BC \\perp AB$. Trong $(SAB)$, hai đườ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Đường thẳng vuông góc với mặt phẳng. '
                        'b) **Đúng** theo công thức trọng tâm **Định nghĩa** ($d \\perp (\\alpha) '
                        '\\Leftrightarrow d \\perp a, \\quad \\forall a \\subset (\\alpha)$). c) **Sai** vì '
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa**. d) **Đúng** theo lời giải ví dụ minh '
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 23: Đường thẳng vuông góc với mặt phẳng** để giải quyết tình '
                 'huống sau: Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$ và tam giác $ABC$ vuông tại $B$. '
                 'Chứng minh $BC \\perp (SAB)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $SA \\perp (ABC)$ và $BC \\subset (ABC)$ nên $BC \\perp SA$. Mặt khác tam giác '
                        '$ABC$ vuông tại $B$ nên $BC \\perp AB$. Trong $(SAB)$, hai đường thẳng $SA$ v...',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Đường thẳng vuông góc với mặt phẳng: Vì $SA \\perp '
                        '(ABC)$ và $BC \\subset (ABC)$ nên $BC \\perp SA$. Mặt khác tam giác $ABC$ vuông tại '
                        '$B$ nên $BC \\perp AB$. Trong $(SAB)$, hai đường thẳng $SA$ và $AB$ cắt nhau tại '
                        '$A$, suy ra $BC \\perp (SAB)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, $SA = 3\\text{ cm}$, tam giác $ABC$ vuông tại '
                 '$B$ với $AB = 4\\text{ cm}, BC = 12\\text{ cm}$. Tính độ dài đoạn thẳng $SC$ (đơn vị: cm).',
            'answer': ['13'],
            'unit': None,
            'solution': 'Trong $\\triangle ABC$ vuông tại $B$: $AC^2 = AB^2 + BC^2 = 4^2 + 12^2 = 160$. Vì '
                        '$SA \\perp (ABC) \\Rightarrow SA \\perp AC$, trong $\\triangle SAC$ vuông tại $A$: '
                        '$SC = \\sqrt{SA^2 + AC^2} = \\sqrt{9 + 160} = \\sqrt{169} = 13\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng',
  'icon': '📐',
  'description': 'Phép chiếu vuông góc, định lí ba đường vuông góc và cách xác định, tính góc giữa đường '
                 'thẳng và mặt phẳng.',
  'requirements': ['Xác định được hình chiếu vuông góc của một điểm, một đường thẳng lên một mặt phẳng.',
                   'Vận dụng được định lí ba đường vuông góc.',
                   'Xác định và tính được góc giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$ thông qua góc '
                   "giữa $d$ và hình chiếu $d'$ của nó trên $(\\alpha)$."],
  'definition': 'Phép chiếu song song lên mặt phẳng $(\\alpha)$ theo phương $\\Delta$ vuông góc với '
                '$(\\alpha)$ gọi là phép chiếu vuông góc lên mặt phẳng $(\\alpha)$. Nếu đường thẳng $d$ '
                "không vuông góc với mặt phẳng $(\\alpha)$ thì góc giữa $d$ và hình chiếu $d'$ của nó trên "
                '$(\\alpha)$ gọi là góc giữa đường thẳng $d$ và mặt phẳng $(\\alpha)$.',
  'theory': '1. Nếu $d \\perp (\\alpha)$ thì góc giữa $d$ và $(\\alpha)$ bằng $90^\\circ$; nếu $d \\parallel '
            '(\\alpha)$ hoặc $d \\subset (\\alpha)$ thì góc bằng $0^\\circ$. Do đó $0^\\circ \\le (d, '
            '(\\alpha)) \\le 90^\\circ$. 2. Định lí ba đường vuông góc: Cho đường thẳng $a$ nằm trong '
            '$(\\alpha)$ và đường thẳng $b$ không nằm trong $(\\alpha)$ đồng thời không vuông góc với '
            "$(\\alpha)$. Gọi $b'$ là hình chiếu vuông góc của $b$ trên $(\\alpha)$. Khi đó $a \\perp b "
            "\\Leftrightarrow a \\perp b'$. 3. Quy tắc tìm góc giữa $SA$ và $(ABC)$ khi biết $SH \\perp "
            '(ABC)$: giao điểm là $A$, chân đường cao là $H$, góc cần tìm là $\\widehat{SAH}$.',
  'formulas': [{'category': 'Góc giữa đường thẳng và mặt phẳng',
                'items': [{'name': 'Khoảng giá trị của góc',
                           'formula': '$0^\\circ \\le (d, (\\alpha)) \\le 90^\\circ$'},
                          {'name': 'Công thức tính trong tam giác vuông SAH',
                           'formula': '$SH \\perp (\\alpha) \\text{ tại } H, SA \\cap (\\alpha) = \\{A\\} '
                                      '\\Rightarrow (SA, (\\alpha)) = \\widehat{SAH}, \\quad '
                                      '\\sin\\widehat{SAH} = \\dfrac{SH}{SA}$'},
                          {'name': 'Định lí ba đường vuông góc',
                           'formula': "$a \\subset (\\alpha), b' \\text{ là hình chiếu của } b \\text{ trên "
                                      '} (\\alpha) \\Rightarrow (a \\perp b \\Leftrightarrow a \\perp '
                                      "b')$"}]}],
  'example': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, $SA \\perp (ABCD)$ và $SA = '
             'a\\sqrt{6}$. Tính góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$.',
  'example_answer': 'Vì $SA \\perp (ABCD)$ tại $A$ nên $AC$ là hình chiếu vuông góc của $SC$ trên $(ABCD)$. '
                    'Suy ra góc giữa $SC$ và $(ABCD)$ là $\\widehat{SCA}$. Trong $\\triangle SAC$ vuông tại '
                    '$A$, ta có $AC = a\\sqrt{2}$ nên $\\tan \\widehat{SCA} = \\dfrac{SA}{AC} = '
                    '\\dfrac{a\\sqrt{6}}{a\\sqrt{2}} = \\sqrt{3} \\Rightarrow \\widehat{SCA} = 60^\\circ$.',
  'real_life': 'Tính góc nghiêng của dốc cầu hoặc thang cuốn so với mặt đất nằm ngang.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường thẳng $d$ không vuông góc với mặt phẳng $(\\alpha)$ và có hình chiếu vuông góc '
                 "trên $(\\alpha)$ là đường thẳng $d'$. Góc giữa $d$ và $(\\alpha)$ là:",
            'options': ["Góc phụ với góc giữa $d$ và $d'$.",
                        'Góc bằng $90^\\circ$.',
                        'Góc giữa $d$ và một đường thẳng bất kì trong $(\\alpha)$.',
                        "Góc giữa hai đường thẳng $d$ và $d'$."],
            'answer': 3,
            'solution': 'Theo định nghĩa, góc giữa $d$ và $(\\alpha)$ là góc giữa $d$ và hình chiếu vuông '
                        "góc $d'$ của nó trên $(\\alpha)$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu đường thẳng $d$ vuông góc với mặt phẳng $(\\alpha)$ thì góc giữa $d$ và $(\\alpha)$ '
                 'bằng:',
            'options': ['$90^\\circ$', '$0^\\circ$', '$45^\\circ$', '$60^\\circ$'],
            'answer': 0,
            'solution': 'Khi $d \\perp (\\alpha)$, theo định nghĩa góc giữa $d$ và $(\\alpha)$ bằng '
                        '$90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt '
                 'phẳng**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Khoảng giá trị của góc**?',
            'options': ['$SH \\perp (\\alpha) \\text{ tại } H, SA \\cap (\\alpha) = \\{A\\} \\Rightarrow '
                        '(SA, (\\alpha)) = \\widehat{SAH}, \\quad \\sin\\widehat{SAH} = \\dfrac{SH}{SA}$',
                        '$0^\\circ \\le (d, (\\alpha)) \\le 90^\\circ$',
                        "$a \\subset (\\alpha), b' \\text{ là hình chiếu của } b \\text{ trên } (\\alpha) "
                        "\\Rightarrow (a \\perp b \\Leftrightarrow a \\perp b')$",
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 24: Phép chiếu vuông góc. Góc giữa đường '
                        'thẳng và mặt phẳng, **Khoảng giá trị của góc** được xác định bởi: $0^\\circ \\le '
                        '(d, (\\alpha)) \\le 90^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng**, nội dung/biểu '
                 'thức $SH \\perp (\\alpha) \\text{ tại } H, SA \\cap (\\alpha) = \\{A\\} \\Rightarrow (SA, '
                 '(\\alpha)) = \\widehat{SAH}, \\quad \\sin\\widehat{SAH} = \\dfrac{SH}{SA}$ là quy tắc hoặc '
                 'công thức của mục nào sau đây?',
            'options': ['Khoảng giá trị của góc',
                        'Định lí ba đường vuông góc',
                        'Công thức tính trong tam giác vuông SAH',
                        'Đổi độ và radian'],
            'answer': 2,
            'solution': 'Trong Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng, biểu '
                        'thức/quy tắc $SH \\perp (\\alpha) \\text{ tại } H, SA \\cap (\\alpha) = \\{A\\} '
                        '\\Rightarrow (SA, (\\alpha)) = \\widehat{SAH}, \\quad \\sin\\widehat{SAH} = '
                        '\\dfrac{SH}{SA}$ chính là nội dung của **Công thức tính trong tam giác vuông '
                        'SAH**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, $SA = a\\sqrt{3}$ và $AB = a$. Góc giữa đường '
                 'thẳng $SB$ và mặt phẳng $(ABC)$ bằng:',
            'options': ['$30^\\circ$', '$45^\\circ$', '$90^\\circ$', '$60^\\circ$'],
            'answer': 3,
            'solution': 'Hình chiếu của $SB$ trên $(ABC)$ là $AB$ nên góc là $\\widehat{SBA}$. Ta có $\\tan '
                        '\\widehat{SBA} = \\dfrac{SA}{AB} = \\sqrt{3} \\Rightarrow \\widehat{SBA} = '
                        '60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng** (Chương VII: '
                 'Quan hệ vuông góc trong không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Xác định được hình chiếu vuông góc của một điểm, một đường thẳng lên một mặt phẳng.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt '
                        'phẳng: Xác định được hình chiếu vuông góc của một điểm, một đường thẳng lên một mặt '
                        'phẳng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, $SA \\perp (ABCD)$ và $SA = '
                 'a$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Hình chiếu vuông góc của đường thẳng $SB$ trên mặt phẳng $(ABCD)$ là đường thẳng '
                           '$AB$.',
                           'Góc giữa đường thẳng $SB$ và mặt phẳng $(ABCD)$ bằng $45^\\circ$.',
                           'Hình chiếu vuông góc của đường thẳng $SC$ trên mặt phẳng $(ABCD)$ là đường thẳng '
                           '$AC$.',
                           'Góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ bằng $45^\\circ$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $SA \\perp (ABCD)$. b) Đúng vì $\\triangle SAB$ vuông cân tại $A '
                        '\\Rightarrow \\widehat{SBA} = 45^\\circ$. c) Đúng vì $A$ là hình chiếu của $S$ trên '
                        '$(ABCD)$. d) Sai vì $\\tan \\widehat{SCA} = \\dfrac{SA}{AC} = '
                        '\\dfrac{a}{a\\sqrt{2}} = \\dfrac{1}{\\sqrt{2}} \\ne 1$ nên $\\widehat{SCA} \\ne '
                        '45^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 24: Phép chiếu vuông '
                 'góc. Góc giữa đường thẳng và mặt phẳng**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định được hình chiếu vuông góc '
                           'của một điểm, một đường thẳng lên một mặt phẳng.',
                           'Quy tắc/công thức **Khoảng giá trị của góc** trong bài được xác định bởi: '
                           '$0^\\circ \\le (d, (\\alpha)) \\le 90^\\circ$.',
                           'Trong mọi trường hợp, **Khoảng giá trị của góc** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và '
                           'mặt phẳng.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh '
                           '$a$, $SA \\perp (ABCD)$ và $SA = a\\sqrt{6}$. Tính góc giữa đường thẳng $SC$ và '
                           'mặt ph...”, lời giải đúng là: Vì $SA \\perp (ABCD)$ tại $A$ nên $AC$ là hình '
                           'chiếu vuông góc của $SC$ trên $(ABCD)$. Suy ra góc giữa $SC$ và $(ABCD)$ là '
                           '$\\widehat{SCA}$. T...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: Phép chiếu vuông góc. Góc giữa đường '
                        'thẳng và mặt phẳng. b) **Đúng** theo công thức trọng tâm **Khoảng giá trị của góc** '
                        '($0^\\circ \\le (d, (\\alpha)) \\le 90^\\circ$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Khoảng giá trị của góc**. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt phẳng** để '
                 'giải quyết tình huống sau: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, '
                 '$SA \\perp (ABCD)$ và $SA = a\\sqrt{6}$. Tính góc giữa đường thẳng $SC$ và mặt phẳng '
                 '$(ABCD)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Vì $SA \\perp (ABCD)$ tại $A$ nên $AC$ là hình chiếu vuông góc của $SC$ trên '
                        '$(ABCD)$. Suy ra góc giữa $SC$ và $(ABCD)$ là $\\widehat{SCA}$. Trong $\\triangle '
                        'SAC$...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Phép chiếu vuông góc. Góc giữa đường thẳng và mặt '
                        'phẳng: Vì $SA \\perp (ABCD)$ tại $A$ nên $AC$ là hình chiếu vuông góc của $SC$ trên '
                        '$(ABCD)$. Suy ra góc giữa $SC$ và $(ABCD)$ là $\\widehat{SCA}$. Trong $\\triangle '
                        'SAC$ vuông tại $A$, ta có $AC = a\\sqrt{2}$ nên $\\tan \\widehat{SCA} = '
                        '\\dfrac{SA}{AC} = \\dfrac{a\\sqrt{6}}{a\\sqrt{2}} = \\sqrt{3} \\Rightarrow '
                        '\\widehat{SCA} = 60^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một chiếc thang dài $6\\text{ m}$ tựa vào bức tường thẳng đứng, đầu trên của thang chạm '
                 'tường ở độ cao $3\\text{ m}$ so với mặt đất phẳng nằm ngang. Tính góc tạo bởi chiếc thang '
                 'và mặt đất (đơn vị: độ).',
            'answer': ['30'],
            'unit': None,
            'solution': 'Gọi $\\alpha$ là góc giữa chiếc thang và mặt đất. Trong tam giác vuông tạo bởi '
                        'thang, tường và mặt đất, ta có $\\sin \\alpha = \\dfrac{3}{6} = \\dfrac{1}{2} '
                        '\\Rightarrow \\alpha = 30^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 25: Hai mặt phẳng vuông góc và góc nhị diện',
  'icon': '📖',
  'description': 'Góc giữa hai mặt phẳng, góc nhị diện, góc phẳng nhị diện, điều kiện hai mặt phẳng vuông '
                 'góc và tính chất của hình lăng trụ đứng, hình chóp đều.',
  'requirements': ['Nhận biết được góc nhị diện $[P, d, Q]$ và xác định được góc phẳng nhị diện tương ứng.',
                   'Vận dụng điều kiện hai mặt phẳng vuông góc: $(\\alpha) \\perp (\\beta)$ khi $(\\alpha)$ '
                   'chứa một đường thẳng vuông góc với $(\\beta)$.',
                   'Nắm được tính chất của hình lăng trụ đứng, lăng trụ đều, hình hộp chữ nhật, hình lập '
                   'phương và hình chóp đều.'],
  'definition': 'Hai mặt phẳng $(\\alpha)$ và $(\\beta)$ được gọi là vuông góc với nhau, kí hiệu $(\\alpha) '
                '\\perp (\\beta)$, nếu góc giữa hai mặt phẳng đó bằng $90^\\circ$. Góc nhị diện tạo bởi hai '
                'nửa mặt phẳng $(P), (Q)$ có chung bờ $d$ được kí hiệu là $[P, d, Q]$, có số đo từ '
                '$0^\\circ$ đến $180^\\circ$.',
  'theory': '1. Định lí nhận biết: Nếu một mặt phẳng chứa một đường thẳng vuông góc với một mặt phẳng khác '
            'thì hai mặt phẳng đó vuông góc với nhau. 2. Tính chất: Nếu hai mặt phẳng cắt nhau và cùng vuông '
            'góc với mặt phẳng thứ ba thì giao tuyến của chúng vuông góc với mặt phẳng thứ ba đó. 3. Hình '
            'chóp đều có đáy là đa giác đều và chân đường cao trùng với tâm của đáy.',
  'formulas': [{'category': 'Hai mặt phẳng vuông góc và góc nhị diện',
                'items': [{'name': 'Dấu hiệu hai mặt phẳng vuông góc',
                           'formula': '$\\begin{cases} d \\subset (\\alpha) \\\\ d \\perp (\\beta) '
                                      '\\end{cases} \\Rightarrow (\\alpha) \\perp (\\beta)$'},
                          {'name': 'Định lí giao tuyến vuông góc',
                           'formula': '$\\begin{cases} (\\alpha) \\perp (\\gamma), (\\beta) \\perp (\\gamma) '
                                      '\\\\ (\\alpha) \\cap (\\beta) = d \\end{cases} \\Rightarrow d \\perp '
                                      '(\\gamma)$'},
                          {'name': 'Góc phẳng nhị diện [P, d, Q]',
                           'formula': '$Ox \\subset (P), Oy \\subset (Q), Ox \\perp d, Oy \\perp d '
                                      '\\Rightarrow \\widehat{xOy} \\text{ là góc phẳng nhị diện}$'}]}],
  'example': 'Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$, $SA \\perp (ABC)$ và $SA = '
             '\\dfrac{a\\sqrt{3}}{2}$. Tính số đo góc nhị diện $[S, BC, A]$.',
  'example_answer': 'Gọi $M$ là trung điểm của $BC$. Vì $\\triangle ABC$ đều nên $AM \\perp BC$ và $AM = '
                    '\\dfrac{a\\sqrt{3}}{2}$. Do $SA \\perp (ABC) \\Rightarrow SA \\perp BC$, suy ra $BC '
                    '\\perp (SAM) \\Rightarrow SM \\perp BC$. Vậy $\\widehat{SMA}$ là góc phẳng nhị diện của '
                    '$[S, BC, A]$. Trong $\\triangle SAM$ vuông tại $A$ có $SA = AM = '
                    '\\dfrac{a\\sqrt{3}}{2}$ nên $\\widehat{SMA} = 45^\\circ$.',
  'real_life': 'Đo độ mở của cánh cửa hoặc laptop thông qua góc nhị diện giữa hai mặt phẳng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Điều kiện đủ để mặt phẳng $(\\alpha)$ vuông góc với mặt phẳng $(\\beta)$ là:',
            'options': ['$(\\alpha)$ chứa một đường thẳng vuông góc với $(\\beta)$.',
                        '$(\\alpha)$ chứa một đường thẳng song song với $(\\beta)$.',
                        '$(\\alpha)$ và $(\\beta)$ có một đường thẳng chung.',
                        'Mọi đường thẳng trong $(\\alpha)$ đều vuông góc với $(\\beta)$.'],
            'answer': 0,
            'solution': 'Theo định lí nhận biết, nếu mặt phẳng $(\\alpha)$ chứa một đường thẳng vuông góc '
                        'với $(\\beta)$ thì $(\\alpha) \\perp (\\beta)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo của một góc nhị diện luôn nhận giá trị trong đoạn nào dưới đây?',
            'options': ['$[0^\\circ; 90^\\circ]$',
                        '$[0^\\circ; 180^\\circ]$',
                        '$[0^\\circ; 360^\\circ]$',
                        '$[90^\\circ; 180^\\circ]$'],
            'answer': 1,
            'solution': 'Góc phẳng nhị diện là góc giữa hai tia nên có số đo từ $0^\\circ$ đến $180^\\circ$ '
                        '(khác với góc giữa hai mặt phẳng chỉ từ $0^\\circ$ đến $90^\\circ$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 25: Hai mặt phẳng vuông góc và góc nhị diện**, công thức '
                 'hoặc quy tắc nào sau đây biểu diễn đúng **Dấu hiệu hai mặt phẳng vuông góc**?',
            'options': ['$\\begin{cases} (\\alpha) \\perp (\\gamma), (\\beta) \\perp (\\gamma) \\\\ '
                        '(\\alpha) \\cap (\\beta) = d \\end{cases} \\Rightarrow d \\perp (\\gamma)$',
                        '$Ox \\subset (P), Oy \\subset (Q), Ox \\perp d, Oy \\perp d \\Rightarrow '
                        '\\widehat{xOy} \\text{ là góc phẳng nhị diện}$',
                        '$\\begin{cases} d \\subset (\\alpha) \\\\ d \\perp (\\beta) \\end{cases} '
                        '\\Rightarrow (\\alpha) \\perp (\\beta)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 25: Hai mặt phẳng vuông góc và góc nhị diện, '
                        '**Dấu hiệu hai mặt phẳng vuông góc** được xác định bởi: $\\begin{cases} d \\subset '
                        '(\\alpha) \\\\ d \\perp (\\beta) \\end{cases} \\Rightarrow (\\alpha) \\perp '
                        '(\\beta)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Hai mặt phẳng vuông góc và góc nhị diện**, nội dung/biểu thức '
                 '$\\begin{cases} (\\alpha) \\perp (\\gamma), (\\beta) \\perp (\\gamma) \\\\ (\\alpha) \\cap '
                 '(\\beta) = d \\end{cases} \\Rightarrow d \\perp (\\gamma)$ là quy tắc hoặc công thức của '
                 'mục nào sau đây?',
            'options': ['Dấu hiệu hai mặt phẳng vuông góc',
                        'Góc phẳng nhị diện [P, d, Q]',
                        'Đổi độ và radian',
                        'Định lí giao tuyến vuông góc'],
            'answer': 3,
            'solution': 'Trong Bài 25: Hai mặt phẳng vuông góc và góc nhị diện, biểu thức/quy tắc '
                        '$\\begin{cases} (\\alpha) \\perp (\\gamma), (\\beta) \\perp (\\gamma) \\\\ '
                        '(\\alpha) \\cap (\\beta) = d \\end{cases} \\Rightarrow d \\perp (\\gamma)$ chính là '
                        'nội dung của **Định lí giao tuyến vuông góc**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai mặt phẳng $(\\alpha)$ và $(\\beta)$ cắt nhau theo giao tuyến $d$ và cùng vuông góc '
                 'với mặt phẳng $(\\gamma)$. Khẳng định nào dưới đây đúng?',
            'options': ['$d \\perp (\\gamma)$',
                        '$d \\parallel (\\gamma)$',
                        '$d \\subset (\\gamma)$',
                        '$(\\alpha) \\perp (\\beta)$'],
            'answer': 0,
            'solution': 'Nếu hai mặt phẳng cắt nhau cùng vuông góc với mặt phẳng thứ ba thì giao tuyến $d$ '
                        'của chúng vuông góc với mặt phẳng thứ ba đó.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Hai mặt phẳng vuông góc và góc nhị diện** (Chương VII: Quan hệ vuông góc '
                 'trong không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Nhận biết được góc nhị diện $[P, d, Q]$ và xác định được góc phẳng nhị diện tương '
                        'ứng.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 25: Hai mặt phẳng vuông góc và góc nhị diện: Nhận biết '
                        'được góc nhị diện $[P, d, Q]$ và xác định được góc phẳng nhị diện tương ứng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp tứ giác đều $S.ABCD$ có tâm đáy là $O$ và $M$ là trung điểm của cạnh $BC$. '
                 'Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Đường thẳng $SO$ vuông góc với mặt phẳng $(ABCD)$.',
                           'Mặt phẳng $(SAC)$ vuông góc với mặt phẳng $(ABCD)$.',
                           'Hai mặt phẳng $(SAC)$ và $(SBD)$ vuông góc với nhau.',
                           'Góc phẳng nhị diện $[S, BC, O]$ là góc $\\widehat{SCO}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng theo tính chất hình chóp đều. b) Đúng vì $(SAC)$ chứa $SO \\perp (ABCD)$. '
                        'c) Đúng vì $BD \\perp AC$ và $BD \\perp SO \\Rightarrow BD \\perp (SAC) '
                        '\\Rightarrow (SBD) \\perp (SAC)$. d) Sai vì $OM \\perp BC$ và $SM \\perp BC$ nên '
                        'góc phẳng nhị diện $[S, BC, O]$ là góc $\\widehat{SMO}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 25: Hai mặt phẳng vuông '
                 'góc và góc nhị diện**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Nhận biết được góc nhị diện $[P, '
                           'd, Q]$ và xác định được góc phẳng nhị diện tương ứng.',
                           'Quy tắc/công thức **Dấu hiệu hai mặt phẳng vuông góc** trong bài được xác định '
                           'bởi: $\\begin{cases} d \\subset (\\alpha) \\\\ d \\perp (\\beta) \\end{cases} '
                           '\\Rightarrow (\\alpha) \\perp (\\beta)$.',
                           'Trong mọi trường hợp, **Dấu hiệu hai mặt phẳng vuông góc** luôn được tính bằng '
                           'công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                           'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) '
                           'mà không cần điều kiện của Bài 25: Hai mặt phẳng vuông góc và góc nhị diện.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh '
                           '$a$, $SA \\perp (ABC)$ và $SA = \\dfrac{a\\sqrt{3}}{2}$. Tính số đo góc nhị diện '
                           '$[S, BC, A]$...”, lời giải đúng là: Gọi $M$ là trung điểm của $BC$. Vì '
                           '$\\triangle ABC$ đều nên $AM \\perp BC$ và $AM = \\dfrac{a\\sqrt{3}}{2}$. Do $SA '
                           '\\perp (ABC) \\Rightarrow SA \\perp BC$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Hai mặt phẳng vuông góc và góc nhị '
                        'diện. b) **Đúng** theo công thức trọng tâm **Dấu hiệu hai mặt phẳng vuông góc** '
                        '($\\begin{cases} d \\subset (\\alpha) \\\\ d \\perp (\\beta) \\end{cases} '
                        '\\Rightarrow (\\alpha) \\perp (\\beta)$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi '
                        'a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Dấu hiệu hai mặt phẳng vuông góc**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 25: Hai mặt phẳng vuông góc và góc nhị diện** để giải quyết tình '
                 'huống sau: Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$, $SA \\perp (ABC)$ '
                 'và $SA = \\dfrac{a\\sqrt{3}}{2}$. Tính số đo góc nhị diện $[S, BC, A]$. Kết quả và hướng '
                 'giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Gọi $M$ là trung điểm của $BC$. Vì $\\triangle ABC$ đều nên $AM \\perp BC$ và $AM = '
                        '\\dfrac{a\\sqrt{3}}{2}$. Do $SA \\perp (ABC) \\Rightarrow SA \\perp BC$, suy r...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Hai mặt phẳng vuông góc và góc nhị diện: Gọi $M$ là '
                        'trung điểm của $BC$. Vì $\\triangle ABC$ đều nên $AM \\perp BC$ và $AM = '
                        '\\dfrac{a\\sqrt{3}}{2}$. Do $SA \\perp (ABC) \\Rightarrow SA \\perp BC$, suy ra $BC '
                        '\\perp (SAM) \\Rightarrow SM \\perp BC$. Vậy $\\widehat{SMA}$ là góc phẳng nhị diện '
                        'của $[S, BC, A]$. Trong $\\triangle SAM$ vuông tại $A$ có $SA = AM = '
                        '\\dfrac{a\\sqrt{3}}{2}$ nên $\\widehat{SMA} = 45^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có ba kích thước $AB = 3\\text{ cm}, AD = 4\\text{ "
                 "cm}, AA' = 12\\text{ cm}$. Tính độ dài đường chéo $AC'$ của hình hộp chữ nhật (đơn vị: "
                 'cm).',
            'answer': ['13'],
            'unit': None,
            'solution': "Độ dài đường chéo của hình hộp chữ nhật là $AC' = \\sqrt{AB^2 + AD^2 + AA'^2} = "
                        '\\sqrt{3^2 + 4^2 + 12^2} = \\sqrt{169} = 13\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 26: Khoảng cách trong không gian',
  'icon': '📏',
  'description': 'Khoảng cách từ một điểm đến một đường thẳng, đến một mặt phẳng, khoảng cách giữa hai mặt '
                 'phẳng song song và khoảng cách giữa hai đường thẳng chéo nhau.',
  'requirements': ['Xác định và tính được khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ thông qua hình chiếu '
                   'vuông góc $H$ của $M$ trên $(P)$.',
                   'Chuyển được khoảng cách từ một điểm bất kì về khoảng cách từ chân đường cao của hình '
                   'chóp.',
                   'Nhận biết được đường vuông góc chung và tính được khoảng cách giữa hai đường thẳng chéo '
                   'nhau.'],
  'definition': 'Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$, kí hiệu $d(M, (P))$, là độ dài đoạn thẳng '
                '$MH$, trong đó $H$ là hình chiếu vuông góc của $M$ trên $(P)$. Khoảng cách giữa hai đường '
                'thẳng chéo nhau $a$ và $b$, kí hiệu $d(a, b)$, là độ dài đoạn vuông góc chung của $a$ và '
                '$b$.',
  'theory': '1. Nếu $d \\parallel (P)$ thì $d(d, (P)) = d(M, (P))$ với $M \\in d$ bất kì. 2. Nếu $(P) '
            '\\parallel (Q)$ thì $d((P), (Q)) = d(M, (Q))$ với $M \\in (P)$ bất kì. 3. Khoảng cách giữa hai '
            'đường thẳng chéo nhau $a$ và $b$ bằng khoảng cách giữa $a$ và mặt phẳng $(P)$ chứa $b$ song '
            'song với $a$: $d(a, b) = d(a, (P)) = d(M, (P))$ ($M \\in a$).',
  'formulas': [{'category': 'Các công thức tính khoảng cách trong không gian',
                'items': [{'name': 'Hệ thức đường cao tam giác vuông SAH',
                           'formula': '$\\dfrac{1}{AH^2} = \\dfrac{1}{SA^2} + \\dfrac{1}{AM^2}$'},
                          {'name': 'Đổi điểm tính khoảng cách',
                           'formula': '$AB \\cap (P) = \\{I\\} \\Rightarrow \\dfrac{d(A, (P))}{d(B, (P))} = '
                                      '\\dfrac{IA}{IB}$'},
                          {'name': 'Khoảng cách hai đường chéo nhau',
                           'formula': '$a \\parallel (P), b \\subset (P), M \\in a \\Rightarrow d(a, b) = '
                                      'd(M, (P))$'}]}],
  'example': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, $SA = 3a$, tam giác $ABC$ vuông tại $A$ với $AB = '
             '4a$. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ trong trường hợp $AC \\perp (SAB)$... '
             'Ta xét bài toán chuẩn: Cho $SA \\perp (ABC)$, $\\triangle ABC$ vuông tại $B$, $SA = 3a, AB = '
             '4a$. Tính $d(A, (SBC))$.',
  'example_answer': 'Vì $BC \\perp AB$ và $BC \\perp SA$ nên $BC \\perp (SAB) \\Rightarrow (SBC) \\perp '
                    '(SAB)$ theo giao tuyến $SB$. Trong $\\triangle SAB$ vuông tại $A$, kẻ $AH \\perp SB$ '
                    'tại $H$ thì $AH \\perp (SBC)$. Vậy $d(A, (SBC)) = AH = \\dfrac{SA \\cdot '
                    'AB}{\\sqrt{SA^2 + AB^2}} = \\dfrac{3a \\cdot 4a}{5a} = \\dfrac{12a}{5}$.',
  'real_life': 'Tính khoảng cách an toàn tối thiểu giữa hai đường dây điện cao thế hoặc hai đường ống dẫn '
               'khí chéo nhau trong không gian.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho điểm $M$ và mặt phẳng $(P)$, gọi $H$ là hình chiếu vuông góc của $M$ trên $(P)$. '
                 'Khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ bằng độ dài đoạn thẳng:',
            'options': ['$MA$ với $A \\in (P)$ bất kì', '$MH$', '$MO$', '$0$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, khoảng cách từ $M$ đến $(P)$ là độ dài đoạn vuông góc $MH$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Khoảng cách giữa hai mặt phẳng "
                 "$(ABCD)$ và $(A'B'C'D')$ bằng:",
            'options': ['$a\\sqrt{2}$', '$a\\sqrt{3}$', '$a$', '$\\dfrac{a}{2}$'],
            'answer': 2,
            'solution': "Vì $AA' \\perp (ABCD)$ và $AA' \\perp (A'B'C'D')$ nên khoảng cách giữa hai mặt đáy "
                        "là $AA' = a$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 26: Khoảng cách trong không gian**, công thức hoặc quy '
                 'tắc nào sau đây biểu diễn đúng **Hệ thức đường cao tam giác vuông SAH**?',
            'options': ['$AB \\cap (P) = \\{I\\} \\Rightarrow \\dfrac{d(A, (P))}{d(B, (P))} = '
                        '\\dfrac{IA}{IB}$',
                        '$a \\parallel (P), b \\subset (P), M \\in a \\Rightarrow d(a, b) = d(M, (P))$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$\\dfrac{1}{AH^2} = \\dfrac{1}{SA^2} + \\dfrac{1}{AM^2}$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 26: Khoảng cách trong không gian, **Hệ thức '
                        'đường cao tam giác vuông SAH** được xác định bởi: $\\dfrac{1}{AH^2} = '
                        '\\dfrac{1}{SA^2} + \\dfrac{1}{AM^2}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Khoảng cách trong không gian**, nội dung/biểu thức $AB \\cap (P) = \\{I\\} '
                 '\\Rightarrow \\dfrac{d(A, (P))}{d(B, (P))} = \\dfrac{IA}{IB}$ là quy tắc hoặc công thức '
                 'của mục nào sau đây?',
            'options': ['Đổi điểm tính khoảng cách',
                        'Hệ thức đường cao tam giác vuông SAH',
                        'Khoảng cách hai đường chéo nhau',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 26: Khoảng cách trong không gian, biểu thức/quy tắc $AB \\cap (P) = '
                        '\\{I\\} \\Rightarrow \\dfrac{d(A, (P))}{d(B, (P))} = \\dfrac{IA}{IB}$ chính là nội '
                        'dung của **Đổi điểm tính khoảng cách**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. Khoảng cách giữa hai đường thẳng "
                 "chéo nhau $AA'$ và $BC$ bằng:",
            'options': ['$a\\sqrt{2}$', '$a$', '$\\dfrac{a\\sqrt{2}}{2}$', '$2a$'],
            'answer': 1,
            'solution': "Ta có $AB \\perp AA'$ và $AB \\perp BC$ nên $AB$ là đoạn vuông góc chung của $AA'$ "
                        "và $BC$. Vậy $d(AA', BC) = AB = a$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Khoảng cách trong không gian** (Chương VII: Quan hệ vuông góc trong '
                 'không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Xác định và tính được khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ thông qua hình '
                        'chiếu vuông góc $H$ của $M$ trên $(P)$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 26: Khoảng cách trong không gian: Xác định và tính '
                        'được khoảng cách từ điểm $M$ đến mặt phẳng $(P)$ thông qua hình chiếu vuông góc $H$ '
                        'của $M$ trên $(P)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật với $AB = 3a, AD = 4a$, cạnh bên $SA '
                 '\\perp (ABCD)$ và $SA = 5a$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Khoảng cách từ điểm $S$ đến mặt phẳng $(ABCD)$ bằng $5a$.',
                           'Khoảng cách từ điểm $B$ đến mặt phẳng $(SAD)$ bằng $3a$.',
                           'Khoảng cách từ điểm $D$ đến mặt phẳng $(SAB)$ bằng $4a$.',
                           'Khoảng cách giữa hai đường thẳng $SA$ và $BC$ bằng $4a$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $SA \\perp (ABCD) \\Rightarrow d(S, (ABCD)) = SA = 5a$. b) Đúng vì $BA '
                        '\\perp (SAD) \\Rightarrow d(B, (SAD)) = AB = 3a$. c) Đúng vì $DA \\perp (SAB) '
                        '\\Rightarrow d(D, (SAB)) = AD = 4a$. d) Sai vì $AB \\perp SA$ và $AB \\perp BC$ nên '
                        '$d(SA, BC) = AB = 3a$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 26: Khoảng cách trong '
                 'không gian**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Xác định và tính được khoảng cách '
                           'từ điểm $M$ đến mặt phẳng $(P)$ thông qua hình chiếu vuông góc $H$ của $M$ trên '
                           '$(P)$.',
                           'Quy tắc/công thức **Hệ thức đường cao tam giác vuông SAH** trong bài được xác '
                           'định bởi: $\\dfrac{1}{AH^2} = \\dfrac{1}{SA^2} + \\dfrac{1}{AM^2}$.',
                           'Trong mọi trường hợp, **Hệ thức đường cao tam giác vuông SAH** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 26: Khoảng cách trong không '
                           'gian.',
                           'Với bài toán minh họa: “Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, $SA = 3a$, '
                           'tam giác $ABC$ vuông tại $A$ với $AB = 4a$. Tính khoảng cách từ điểm $A$ đến mặt '
                           'phẳng...”, lời giải đúng là: Vì $BC \\perp AB$ và $BC \\perp SA$ nên $BC \\perp '
                           '(SAB) \\Rightarrow (SBC) \\perp (SAB)$ theo giao tuyến $SB$. Trong $\\triangle '
                           'SAB$ vuông tại $A$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Khoảng cách trong không gian. b) '
                        '**Đúng** theo công thức trọng tâm **Hệ thức đường cao tam giác vuông SAH** '
                        '($\\dfrac{1}{AH^2} = \\dfrac{1}{SA^2} + \\dfrac{1}{AM^2}$). c) **Sai** vì $a^\\circ '
                        '= \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Hệ thức đường cao tam giác vuông SAH**. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 26: Khoảng cách trong không gian** để giải quyết tình huống sau: '
                 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, $SA = 3a$, tam giác $ABC$ vuông tại $A$ với '
                 '$AB = 4a$. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ trong trường hợp $AC \\perp '
                 '(SAB)$... Ta xét bài toán chuẩn: Cho $SA \\perp (ABC)$, $\\triangle ABC$ vuông tại $B$, '
                 '$SA = 3a, AB = 4a$. Tính $d(A, (SBC))$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Vì $BC \\perp AB$ và $BC \\perp SA$ nên $BC \\perp (SAB) \\Rightarrow (SBC) \\perp '
                        '(SAB)$ theo giao tuyến $SB$. Trong $\\triangle SAB$ vuông tại $A$, kẻ $AH \\perp '
                        'SB$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Khoảng cách trong không gian: Vì $BC \\perp AB$ và '
                        '$BC \\perp SA$ nên $BC \\perp (SAB) \\Rightarrow (SBC) \\perp (SAB)$ theo giao '
                        'tuyến $SB$. Trong $\\triangle SAB$ vuông tại $A$, kẻ $AH \\perp SB$ tại $H$ thì $AH '
                        '\\perp (SBC)$. Vậy $d(A, (SBC)) = AH = \\dfrac{SA \\cdot AB}{\\sqrt{SA^2 + AB^2}} = '
                        '\\dfrac{3a \\cdot 4a}{5a} = \\dfrac{12a}{5}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình chóp $S.ABC$ có $SA \\perp (ABC)$, tam giác $ABC$ vuông tại $B$, biết $SA = '
                 '6\\text{ cm}$ và $AB = 8\\text{ cm}$. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ '
                 '(đơn vị: cm).',
            'answer': ['4,8', '4.8'],
            'unit': None,
            'solution': 'Kẻ $AH \\perp SB$ tại $H$. Do $BC \\perp (SAB) \\Rightarrow BC \\perp AH$, suy ra '
                        '$AH \\perp (SBC)$. Vậy $d(A, (SBC)) = AH = \\dfrac{SA \\cdot AB}{\\sqrt{SA^2 + '
                        'AB^2}} = \\dfrac{6 \\cdot 8}{\\sqrt{6^2 + 8^2}} = 4,8\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch07-quan-he-vuong-goc',
  'context_title': 'Chương VII: Quan hệ vuông góc trong không gian',
  'context': 'Chương VII · SGK Toán 11: Quan hệ vuông góc trong không gian, góc, khoảng cách và thể tích '
             'khối đa diện.',
  'title': 'Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt đều',
  'icon': '🧊',
  'description': 'Công thức tính thể tích khối chóp, khối lăng trụ, khối hộp chữ nhật, khối lập phương và '
                 'khối chóp cụt đều.',
  'requirements': ['Thuộc và áp dụng được công thức tính thể tích khối chóp $V = \\dfrac{1}{3}Sh$ và thể '
                   'tích khối lăng trụ $V = Sh$.',
                   "Tính được thể tích khối chóp cụt đều $V = \\dfrac{1}{3}h(S + \\sqrt{SS'} + S')$.",
                   'Vận dụng tính thể tích các vật thể kiến trúc, bồn chứa nước, kim tự tháp trong thực tế.'],
  'definition': 'Thể tích của mỗi khối đa diện là một số dương đo phần không gian mà khối đa diện đó chiếm '
                'chỗ. Thể tích khối chóp có diện tích đáy $S$ và chiều cao $h$ là $V = \\dfrac{1}{3}Sh$; thể '
                'tích khối lăng trụ có diện tích đáy $S$ và chiều cao $h$ là $V = Sh$.',
  'theory': '1. Thể tích khối hộp chữ nhật có ba kích thước $a, b, c$ là $V = abc$; thể tích khối lập phương '
            'cạnh $a$ là $V = a^3$. 2. Thể tích khối chóp cụt đều có chiều cao $h$ và diện tích hai đáy $S, '
            "S'$ là $V = \\dfrac{1}{3}h(S + \\sqrt{SS'} + S')$. 3. Tỉ số thể tích (công thức Simson cho khối "
            "chóp tam giác): $\\dfrac{V_{S.A'B'C'}}{V_{S.ABC}} = \\dfrac{SA'}{SA} \\cdot \\dfrac{SB'}{SB} "
            "\\cdot \\dfrac{SC'}{SC}$.",
  'formulas': [{'category': 'Công thức thể tích khối đa diện',
                'items': [{'name': 'Thể tích khối chóp', 'formula': '$V = \\dfrac{1}{3} S \\cdot h$'},
                          {'name': 'Thể tích khối lăng trụ', 'formula': '$V = S \\cdot h$'},
                          {'name': 'Thể tích khối hộp chữ nhật và lập phương',
                           'formula': '$V_{\\text{hộp}} = a \\cdot b \\cdot c, \\quad V_{\\text{lập phương}} '
                                      '= a^3$'},
                          {'name': 'Thể tích khối chóp cụt đều',
                           'formula': "$V = \\dfrac{1}{3} h \\left(S + \\sqrt{S \\cdot S'} + S'\\right)$"}]}],
  'example': 'Tính thể tích khối chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $a$ và chiều cao $SO = 2a$.',
  'example_answer': 'Diện tích đáy hình vuông là $S = a^2$. Thể tích khối chóp là $V = \\dfrac{1}{3} S '
                    '\\cdot SO = \\dfrac{1}{3} a^2 \\cdot 2a = \\dfrac{2a^3}{3}$.',
  'real_life': 'Tính thể tích bê tông đúc trụ cầu (khối lăng trụ), dung tích phễu chứa xi măng (khối chóp '
               'cụt) và thể tích Kim tự tháp Ai Cập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Thể tích $V$ của khối chóp có diện tích đáy $S$ và chiều cao $h$ được tính theo công thức:',
            'options': ['$V = Sh$',
                        '$V = \\dfrac{1}{2}Sh$',
                        '$V = \\dfrac{1}{3}Sh$',
                        '$V = \\dfrac{1}{6}Sh$'],
            'answer': 2,
            'solution': 'Thể tích khối chóp bằng một phần ba tích của diện tích đáy và chiều cao: $V = '
                        '\\dfrac{1}{3}Sh$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Thể tích của khối lăng trụ có diện tích đáy $S = 12\\text{ cm}^2$ và chiều cao $h = '
                 '5\\text{ cm}$ bằng:',
            'options': ['$20\\text{ cm}^3$', '$30\\text{ cm}^3$', '$17\\text{ cm}^3$', '$60\\text{ cm}^3$'],
            'answer': 3,
            'solution': 'Thể tích khối lăng trụ là $V = S \\cdot h = 12 \\cdot 5 = 60\\text{ '
                        '(cm}^3\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt '
                 'đều**, công thức hoặc quy tắc nào sau đây biểu diễn đúng **Thể tích khối chóp**?',
            'options': ['$V = \\dfrac{1}{3} S \\cdot h$',
                        '$V = S \\cdot h$',
                        '$V_{\\text{hộp}} = a \\cdot b \\cdot c, \\quad V_{\\text{lập phương}} = a^3$',
                        "$V = \\dfrac{1}{3} h \\left(S + \\sqrt{S \\cdot S'} + S'\\right)$"],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 27: Thể tích khối chóp, khối lăng trụ và khối '
                        'chóp cụt đều, **Thể tích khối chóp** được xác định bởi: $V = \\dfrac{1}{3} S \\cdot '
                        'h$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt đều**, nội dung/biểu '
                 'thức $V = S \\cdot h$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Thể tích khối chóp',
                        'Thể tích khối lăng trụ',
                        'Thể tích khối hộp chữ nhật và lập phương',
                        'Thể tích khối chóp cụt đều'],
            'answer': 1,
            'solution': 'Trong Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt đều, biểu thức/quy '
                        'tắc $V = S \\cdot h$ chính là nội dung của **Thể tích khối lăng trụ**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho khối chóp $S.ABC$ có $SA \\perp (ABC)$, tam giác $ABC$ vuông tại $A$ với $AB = 3a, AC '
                 '= 4a$ và $SA = 2a$. Thể tích của khối chóp $S.ABC$ bằng:',
            'options': ['$12a^3$', '$6a^3$', '$4a^3$', '$8a^3$'],
            'answer': 2,
            'solution': 'Diện tích đáy $S_{ABC} = \\dfrac{1}{2}AB \\cdot AC = 6a^2$. Thể tích $V = '
                        '\\dfrac{1}{3} S_{ABC} \\cdot SA = \\dfrac{1}{3} \\cdot 6a^2 \\cdot 2a = 4a^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt đều** (Chương VII: '
                 'Quan hệ vuông góc trong không gian), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần '
                 'đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        'Thuộc và áp dụng được công thức tính thể tích khối chóp $V = \\dfrac{1}{3}Sh$ và '
                        'thể tích khối lăng trụ $V = Sh$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt '
                        'đều: Thuộc và áp dụng được công thức tính thể tích khối chóp $V = \\dfrac{1}{3}Sh$ '
                        'và thể tích khối lăng trụ $V = Sh$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy $ABC$ là tam giác đều cạnh $2a$ và cạnh bên "
                 "$AA' = 3a$. Xét tính đúng sai của các mệnh đề sau:",
            'statements': ['Chiều cao của khối lăng trụ bằng $3a$.',
                           'Diện tích mặt đáy $ABC$ bằng $a^2\\sqrt{3}$.',
                           "Thể tích của khối lăng trụ $ABC.A'B'C'$ bằng $3a^3\\sqrt{3}$.",
                           "Thể tích của khối chóp $A'.ABC$ bằng $3a^3\\sqrt{3}$."],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì lăng trụ đứng có cạnh bên là đường cao. b) Đúng vì $S_{ABC} = '
                        '\\dfrac{(2a)^2\\sqrt{3}}{4} = a^2\\sqrt{3}$. c) Đúng vì $V = S \\cdot h = '
                        "a^2\\sqrt{3} \\cdot 3a = 3a^3\\sqrt{3}$. d) Sai vì khối chóp $A'.ABC$ có cùng đáy "
                        "và chiều cao với lăng trụ nên $V_{A'.ABC} = \\dfrac{1}{3} V_{\\text{lăng trụ}} = "
                        'a^3\\sqrt{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 27: Thể tích khối chóp, '
                 'khối lăng trụ và khối chóp cụt đều**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thuộc và áp dụng được công thức '
                           'tính thể tích khối chóp $V = \\dfrac{1}{3}Sh$ và thể tích khối lăng trụ $V = '
                           'Sh$.',
                           'Quy tắc/công thức **Thể tích khối chóp** trong bài được xác định bởi: $V = '
                           '\\dfrac{1}{3} S \\cdot h$.',
                           'Trong mọi trường hợp, **Thể tích khối chóp** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp '
                           'cụt đều.',
                           'Với bài toán minh họa: “Tính thể tích khối chóp tứ giác đều $S.ABCD$ có cạnh đáy '
                           'bằng $a$ và chiều cao $SO = 2a$.”, lời giải đúng là: Diện tích đáy hình vuông là '
                           '$S = a^2$. Thể tích khối chóp là $V = \\dfrac{1}{3} S \\cdot SO = \\dfrac{1}{3} '
                           'a^2 \\cdot 2a = \\dfrac{2a^3}{3}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Thể tích khối chóp, khối lăng trụ và '
                        'khối chóp cụt đều. b) **Đúng** theo công thức trọng tâm **Thể tích khối chóp** ($V '
                        '= \\dfrac{1}{3} S \\cdot h$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ '
                        'rad}, \\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ '
                        'là công thức của nội dung khác, không phải quy tắc chung của **Thể tích khối '
                        'chóp**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt đều** để '
                 'giải quyết tình huống sau: Tính thể tích khối chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng '
                 '$a$ và chiều cao $SO = 2a$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Diện tích đáy hình vuông là $S = a^2$. Thể tích khối chóp là $V = \\dfrac{1}{3} S '
                        '\\cdot SO = \\dfrac{1}{3} a^2 \\cdot 2a = \\dfrac{2a^3}{3}$.',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Thể tích khối chóp, khối lăng trụ và khối chóp cụt '
                        'đều: Diện tích đáy hình vuông là $S = a^2$. Thể tích khối chóp là $V = '
                        '\\dfrac{1}{3} S \\cdot SO = \\dfrac{1}{3} a^2 \\cdot 2a = \\dfrac{2a^3}{3}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khối chóp cụt tứ giác đều có hai đáy là hai hình vuông có cạnh lần lượt bằng $2\\text{ '
                 'dm}$ và $4\\text{ dm}$, chiều cao của khối chóp cụt bằng $3\\text{ dm}$. Tính thể tích của '
                 'khối chóp cụt đều đó (đơn vị: $\\text{dm}^3$).',
            'answer': ['28'],
            'unit': None,
            'solution': "Diện tích hai đáy là $S = 2^2 = 4\\text{ dm}^2$ và $S' = 4^2 = 16\\text{ dm}^2$. "
                        'Thể tích là $V = \\dfrac{1}{3} \\cdot 3 \\cdot (4 + \\sqrt{4 \\cdot 16} + 16) = 4 + '
                        '8 + 16 = 28\\text{ (dm}^3\\text{)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch08-quy-tac-xac-suat',
  'context_title': 'Chương VIII: Các quy tắc tính xác suất',
  'context': 'Chương VIII · SGK Toán 11: Biến cố hợp, biến cố giao, biến cố độc lập, công thức cộng xác suất '
             'và công thức nhân xác suất.',
  'title': 'Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập',
  'icon': '🎲',
  'description': 'Khái niệm biến cố hợp A ∪ B, biến cố giao AB, hai biến cố xung khắc và hai biến cố độc lập '
                 'trong phép thử ngẫu nhiên.',
  'requirements': ['Mô tả và xác định được biến cố hợp $A \\cup B$ và biến cố giao $A \\cap B$ (viết tắt là '
                   '$AB$).',
                   'Phân biệt được hai biến cố xung khắc ($A \\cap B = \\varnothing$) và hai biến cố độc '
                   'lập.',
                   'Biểu diễn được các biến cố phức tạp thông qua biến cố hợp, biến cố giao và biến cố đối.'],
  'definition': "Cho hai biến cố $A$ và $B$. Biến cố ''$A$ hoặc $B$ xảy ra'' gọi là biến cố hợp của $A$ và "
                "$B$, kí hiệu $A \\cup B$. Biến cố ''Cả $A$ và $B$ đều xảy ra'' gọi là biến cố giao của $A$ "
                'và $B$, kí hiệu $A \\cap B$ hoặc $AB$. Hai biến cố $A$ và $B$ gọi là độc lập nếu việc xảy '
                'ra hay không xảy ra của biến cố này không làm ảnh hưởng tới xác suất xảy ra của biến cố '
                'kia.',
  'theory': '1. Hai biến cố $A$ và $B$ gọi là xung khắc nếu chúng không đồng thời xảy ra trong một phép thử, '
            'tức $A \\cap B = \\varnothing$. 2. Nếu $A$ và $B$ là hai biến cố độc lập thì các cặp biến cố '
            '$(A, \\overline{B})$, $(\\overline{A}, B)$ và $(\\overline{A}, \\overline{B})$ cũng độc lập.',
  'formulas': [{'category': 'Các phép toán trên biến cố',
                'items': [{'name': 'Biến cố hợp (ít nhất 1 biến cố xảy ra)', 'formula': '$A \\cup B$'},
                          {'name': 'Biến cố giao (cả 2 biến cố cùng xảy ra)', 'formula': '$AB = A \\cap B$'},
                          {'name': 'Hai biến cố xung khắc', 'formula': '$A \\cap B = \\varnothing$'},
                          {'name': 'Biến cố đối của A ∪ B',
                           'formula': '$\\overline{A \\cup B} = \\overline{A} \\cap \\overline{B}$'}]}],
  'example': "Gieo một con xúc xắc cân đối. Gọi $A$ là biến cố ''Số chấm là số chẵn'' và $B$ là biến cố ''Số "
             "chấm lớn hơn $4$''. Tìm tập hợp kết quả thuận lợi cho $A \\cup B$ và $AB$.",
  'example_answer': 'Ta có $A = \\{2; 4; 6\\}$ và $B = \\{5; 6\\}$. Khi đó biến cố hợp là $A \\cup B = \\{2; '
                    '4; 5; 6\\}$ và biến cố giao là $AB = A \\cap B = \\{6\\}$.',
  'real_life': 'Phân tích độ tin cậy của hệ thống máy phát điện dự phòng hoạt động độc lập trong bệnh viện.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Cho hai biến cố $A$ và $B$. Biến cố ''Cả $A$ và $B$ đều xảy ra'' được gọi là:",
            'options': ['Biến cố hợp của $A$ và $B$.',
                        'Biến cố đối của $A$.',
                        'Hai biến cố xung khắc.',
                        'Biến cố giao của $A$ và $B$.'],
            'answer': 3,
            'solution': "Biến cố ''Cả $A$ và $B$ đều xảy ra'' là biến cố giao của $A$ và $B$, kí hiệu $AB$ "
                        'hoặc $A \\cap B$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai biến cố $A$ và $B$ được gọi là xung khắc nếu:',
            'options': ['$A \\cap B = \\varnothing$',
                        '$A \\cup B = \\Omega$',
                        '$A = B$',
                        '$P(AB) = P(A)P(B)$'],
            'answer': 0,
            'solution': 'Hai biến cố xung khắc là hai biến cố không có kết quả thuận lợi chung, tức là $A '
                        '\\cap B = \\varnothing$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập**, công '
                 'thức hoặc quy tắc nào sau đây biểu diễn đúng **Biến cố hợp (ít nhất 1 biến cố xảy ra)**?',
            'options': ['$AB = A \\cap B$',
                        '$A \\cup B$',
                        '$A \\cap B = \\varnothing$',
                        '$\\overline{A \\cup B} = \\overline{A} \\cap \\overline{B}$'],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 28: Biến cố hợp, biến cố giao, biến cố độc '
                        'lập, **Biến cố hợp (ít nhất 1 biến cố xảy ra)** được xác định bởi: $A \\cup B$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập**, nội dung/biểu thức $AB = A '
                 '\\cap B$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Biến cố hợp (ít nhất 1 biến cố xảy ra)',
                        'Hai biến cố xung khắc',
                        'Biến cố giao (cả 2 biến cố cùng xảy ra)',
                        'Biến cố đối của A ∪ B'],
            'answer': 2,
            'solution': 'Trong Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập, biểu thức/quy tắc $AB = A '
                        '\\cap B$ chính là nội dung của **Biến cố giao (cả 2 biến cố cùng xảy ra)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai xạ thủ độc lập nhau cùng bắn vào một bia. Gọi $A$ là biến cố xạ thủ thứ nhất bắn trúng '
                 "và $B$ là biến cố xạ thủ thứ hai bắn trúng. Biến cố ''Có ít nhất một xạ thủ bắn trúng "
                 "bia'' là:",
            'options': ['$AB$',
                        '$\\overline{A} \\cap \\overline{B}$',
                        '$A \\cap \\overline{B}$',
                        '$A \\cup B$'],
            'answer': 3,
            'solution': "''Có ít nhất một xạ thủ bắn trúng'' nghĩa là $A$ xảy ra hoặc $B$ xảy ra, tức là "
                        'biến cố hợp $A \\cup B$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập** (Chương VIII: Các quy tắc '
                 'tính xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến '
                 'thức của bài?',
            'options': ['Mô tả và xác định được biến cố hợp $A \\cup B$ và biến cố giao $A \\cap B$ (viết '
                        'tắt là $AB$).',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập: Mô tả '
                        'và xác định được biến cố hợp $A \\cup B$ và biến cố giao $A \\cap B$ (viết tắt là '
                        '$AB$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Chọn ngẫu nhiên một số tự nhiên từ tập hợp $\\{1; 2; 3; 4; 5; 6; 7; 8; 9; 10\\}$. Gọi $A$ '
                 "là biến cố ''Số được chọn là số nguyên tố'' và $B$ là biến cố ''Số được chọn là số chẵn''. "
                 'Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Tập hợp các kết quả thuận lợi cho biến cố $A$ là $\\{2; 3; 5; 7\\}$.',
                           'Số kết quả thuận lợi cho biến cố $B$ là $5$.',
                           'Hai biến cố $A$ và $B$ là hai biến cố xung khắc.',
                           'Biến cố hợp $A \\cup B$ có tất cả $8$ kết quả thuận lợi.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $B = \\{2; 4; 6; 8; 10\\}$ có $5$ phần tử. c) Sai vì $A \\cap B '
                        '= \\{2\\} \\ne \\varnothing$. d) Đúng vì $A \\cup B = \\{2; 3; 4; 5; 6; 7; 8; '
                        '10\\}$ có $8$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 28: Biến cố hợp, biến '
                 'cố giao, biến cố độc lập**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Mô tả và xác định được biến cố hợp '
                           '$A \\cup B$ và biến cố giao $A \\cap B$ (viết tắt là $AB$).',
                           'Quy tắc/công thức **Biến cố hợp (ít nhất 1 biến cố xảy ra)** trong bài được xác '
                           'định bởi: $A \\cup B$.',
                           'Trong mọi trường hợp, **Biến cố hợp (ít nhất 1 biến cố xảy ra)** luôn được tính '
                           'bằng công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad '
                           '\\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc '
                           'Đổi độ và radian) mà không cần điều kiện của Bài 28: Biến cố hợp, biến cố giao, '
                           'biến cố độc lập.',
                           "Với bài toán minh họa: “Gieo một con xúc xắc cân đối. Gọi $A$ là biến cố ''Số "
                           "chấm là số chẵn'' và $B$ là biến cố ''Số chấm lớn hơn $4$''. Tìm tập hợp kết quả "
                           'thuận...”, lời giải đúng là: Ta có $A = \\{2; 4; 6\\}$ và $B = \\{5; 6\\}$. Khi '
                           'đó biến cố hợp là $A \\cup B = \\{2; 4; 5; 6\\}$ và biến cố giao là $AB = A '
                           '\\cap B = \\{6\\}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 28: Biến cố hợp, biến cố giao, biến cố độc '
                        'lập. b) **Đúng** theo công thức trọng tâm **Biến cố hợp (ít nhất 1 biến cố xảy '
                        'ra)** ($A \\cup B$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, '
                        '\\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là '
                        'công thức của nội dung khác, không phải quy tắc chung của **Biến cố hợp (ít nhất 1 '
                        'biến cố xảy ra)**. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập** để giải quyết '
                 "tình huống sau: Gieo một con xúc xắc cân đối. Gọi $A$ là biến cố ''Số chấm là số chẵn'' và "
                 "$B$ là biến cố ''Số chấm lớn hơn $4$''. Tìm tập hợp kết quả thuận lợi cho $A \\cup B$ và "
                 '$AB$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có $A = \\{2; 4; 6\\}$ và $B = \\{5; 6\\}$. Khi đó biến cố hợp là $A \\cup B = '
                        '\\{2; 4; 5; 6\\}$ và biến cố giao là $AB = A \\cap B = \\{6\\}$.',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28: Biến cố hợp, biến cố giao, biến cố độc lập: Ta có $A '
                        '= \\{2; 4; 6\\}$ và $B = \\{5; 6\\}$. Khi đó biến cố hợp là $A \\cup B = \\{2; 4; '
                        '5; 6\\}$ và biến cố giao là $AB = A \\cap B = \\{6\\}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Gieo một con xúc xắc cân đối 1 lần. Gọi $A$ là biến cố ''Số chấm chia hết cho 2'' và $B$ "
                 "là biến cố ''Số chấm chia hết cho 3''. Biến cố hợp $A \\cup B$ có bao nhiêu kết quả thuận "
                 'lợi?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $A = \\{2; 4; 6\\}$ và $B = \\{3; 6\\}$. Khi đó $A \\cup B = \\{2; 3; 4; '
                        '6\\}$ có $4$ kết quả thuận lợi.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch08-quy-tac-xac-suat',
  'context_title': 'Chương VIII: Các quy tắc tính xác suất',
  'context': 'Chương VIII · SGK Toán 11: Biến cố hợp, biến cố giao, biến cố độc lập, công thức cộng xác suất '
             'và công thức nhân xác suất.',
  'title': 'Bài 29: Công thức cộng xác suất',
  'icon': '➕',
  'description': 'Công thức cộng xác suất cho hai biến cố xung khắc và công thức cộng xác suất cho hai biến '
                 'cố bất kì.',
  'requirements': ['Vận dụng được công thức cộng xác suất cho hai biến cố xung khắc: $P(A \\cup B) = P(A) + '
                   'P(B)$.',
                   'Vận dụng được công thức cộng xác suất tổng quát cho hai biến cố bất kì: $P(A \\cup B) = '
                   'P(A) + P(B) - P(AB)$.',
                   'Giải quyết các bài toán thống kê, khảo sát tập hợp bằng công thức cộng xác suất.'],
  'definition': 'Cho hai biến cố $A$ và $B$ bất kì. Khi đó xác suất của biến cố hợp $A \\cup B$ được tính '
                'bởi công thức cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(AB)$.',
  'theory': '1. Trường hợp đặc biệt: nếu hai biến cố $A$ và $B$ xung khắc ($AB = \\varnothing$) thì $P(AB) = '
            '0$, do đó $P(A \\cup B) = P(A) + P(B)$. 2. Hệ quả biến cố đối: $P(\\overline{A}) = 1 - P(A)$ vì '
            '$A$ và $\\overline{A}$ xung khắc và $A \\cup \\overline{A} = \\Omega$.',
  'formulas': [{'category': 'Công thức cộng xác suất',
                'items': [{'name': 'Cho hai biến cố xung khắc',
                           'formula': '$A \\cap B = \\varnothing \\Rightarrow P(A \\cup B) = P(A) + P(B)$'},
                          {'name': 'Cho hai biến cố bất kì',
                           'formula': '$P(A \\cup B) = P(A) + P(B) - P(AB)$'},
                          {'name': 'Quy tắc biến cố đối', 'formula': '$P(\\overline{A}) = 1 - P(A)$'}]}],
  'example': 'Cho hai biến cố $A$ và $B$ có $P(A) = 0,4$, $P(B) = 0,5$ và $P(AB) = 0,2$. Tính $P(A \\cup '
             'B)$.',
  'example_answer': 'Áp dụng công thức cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(AB) = 0,4 + 0,5 - 0,2 '
                    '= 0,7$.',
  'real_life': 'Tính tỉ lệ khách hàng sử dụng ít nhất một trong hai dịch vụ ngân hàng điện tử hoặc thẻ tín '
               'dụng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ bất kì. Công thức cộng xác suất nào dưới đây đúng?',
            'options': ['$P(A \\cup B) = P(A) + P(B) - P(AB)$',
                        '$P(A \\cup B) = P(A) + P(B) + P(AB)$',
                        '$P(A \\cup B) = P(A) \\cdot P(B)$',
                        '$P(A \\cup B) = P(A) - P(B)$'],
            'answer': 0,
            'solution': 'Công thức cộng xác suất tổng quát cho hai biến cố bất kì là $P(A \\cup B) = P(A) + '
                        'P(B) - P(AB)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu hai biến cố $A$ và $B$ xung khắc với $P(A) = 0,25$ và $P(B) = 0,35$ thì $P(A \\cup B)$ '
                 'bằng:',
            'options': ['$0,10$', '$0,60$', '$0,0875$', '$0,50$'],
            'answer': 1,
            'solution': 'Vì $A$ và $B$ xung khắc nên $P(A \\cup B) = P(A) + P(B) = 0,25 + 0,35 = 0,60$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 29: Công thức cộng xác suất**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Cho hai biến cố xung khắc**?',
            'options': ['$P(A \\cup B) = P(A) + P(B) - P(AB)$',
                        '$P(\\overline{A}) = 1 - P(A)$',
                        '$A \\cap B = \\varnothing \\Rightarrow P(A \\cup B) = P(A) + P(B)$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 29: Công thức cộng xác suất, **Cho hai biến '
                        'cố xung khắc** được xác định bởi: $A \\cap B = \\varnothing \\Rightarrow P(A \\cup '
                        'B) = P(A) + P(B)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Công thức cộng xác suất**, nội dung/biểu thức $P(A \\cup B) = P(A) + P(B) '
                 '- P(AB)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cho hai biến cố xung khắc',
                        'Quy tắc biến cố đối',
                        'Đổi độ và radian',
                        'Cho hai biến cố bất kì'],
            'answer': 3,
            'solution': 'Trong Bài 29: Công thức cộng xác suất, biểu thức/quy tắc $P(A \\cup B) = P(A) + '
                        'P(B) - P(AB)$ chính là nội dung của **Cho hai biến cố bất kì**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một lớp có $50$ học sinh, trong đó có $30$ em giỏi Tiếng Anh, $25$ em giỏi Tin học và $15$ '
                 'em giỏi cả hai môn. Chọn ngẫu nhiên $1$ học sinh. Xác suất để chọn được học sinh giỏi ít '
                 'nhất một trong hai môn là:',
            'options': ['$0,8$', '$0,7$', '$0,9$', '$0,5$'],
            'answer': 0,
            'solution': 'Theo công thức cộng: $P(A \\cup B) = \\dfrac{30}{50} + \\dfrac{25}{50} - '
                        '\\dfrac{15}{50} = \\dfrac{40}{50} = 0,8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Công thức cộng xác suất** (Chương VIII: Các quy tắc tính xác suất), '
                 'khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Vận dụng được công thức cộng xác suất cho hai biến cố xung khắc: $P(A \\cup B) = '
                        'P(A) + P(B)$.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 29: Công thức cộng xác suất: Vận dụng được công thức '
                        'cộng xác suất cho hai biến cố xung khắc: $P(A \\cup B) = P(A) + P(B)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai biến cố $A$ và $B$ có $P(A) = 0,5$, $P(B) = 0,6$ và $P(A \\cup B) = 0,8$. Xét tính '
                 'đúng sai của các mệnh đề sau:',
            'statements': ['Xác suất của biến cố đối $\\overline{A}$ là $P(\\overline{A}) = 0,5$.',
                           'Hai biến cố $A$ và $B$ là hai biến cố xung khắc.',
                           'Xác suất của biến cố giao $AB$ là $P(AB) = 0,3$.',
                           'Xác suất để cả hai biến cố $A$ và $B$ đều không xảy ra là $0,2$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $1 - 0,5 = 0,5$. b) Sai vì $P(A) + P(B) = 1,1 \\ne P(A \\cup B)$. c) '
                        'Đúng vì $P(AB) = P(A) + P(B) - P(A \\cup B) = 0,5 + 0,6 - 0,8 = 0,3$. d) Đúng vì '
                        '$P(\\overline{A \\cup B}) = 1 - P(A \\cup B) = 1 - 0,8 = 0,2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 29: Công thức cộng xác '
                 'suất**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Vận dụng được công thức cộng xác '
                           'suất cho hai biến cố xung khắc: $P(A \\cup B) = P(A) + P(B)$.',
                           'Quy tắc/công thức **Cho hai biến cố xung khắc** trong bài được xác định bởi: $A '
                           '\\cap B = \\varnothing \\Rightarrow P(A \\cup B) = P(A) + P(B)$.',
                           'Trong mọi trường hợp, **Cho hai biến cố xung khắc** luôn được tính bằng công '
                           'thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 29: Công thức cộng xác suất.',
                           'Với bài toán minh họa: “Cho hai biến cố $A$ và $B$ có $P(A) = 0,4$, $P(B) = 0,5$ '
                           'và $P(AB) = 0,2$. Tính $P(A \\cup B)$.”, lời giải đúng là: Áp dụng công thức '
                           'cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(AB) = 0,4 + 0,5 - 0,2 = 0,7$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 29: Công thức cộng xác suất. b) **Đúng** '
                        'theo công thức trọng tâm **Cho hai biến cố xung khắc** ($A \\cap B = \\varnothing '
                        '\\Rightarrow P(A \\cup B) = P(A) + P(B)$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi '
                        'a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Cho hai biến cố xung khắc**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 29: Công thức cộng xác suất** để giải quyết tình huống sau: Cho '
                 'hai biến cố $A$ và $B$ có $P(A) = 0,4$, $P(B) = 0,5$ và $P(AB) = 0,2$. Tính $P(A \\cup '
                 'B)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Áp dụng công thức cộng xác suất: $P(A \\cup B) = P(A) + P(B) - P(AB) = 0,4 + 0,5 - '
                        '0,2 = 0,7$.',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Công thức cộng xác suất: Áp dụng công thức cộng xác '
                        'suất: $P(A \\cup B) = P(A) + P(B) - P(AB) = 0,4 + 0,5 - 0,2 = 0,7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tại một hội thảo có $100$ đại biểu tham dự, trong đó $60$ người nói được tiếng Anh, $45$ '
                 'người nói được tiếng Pháp và $25$ người nói được cả tiếng Anh và tiếng Pháp. Chọn ngẫu '
                 'nhiên một đại biểu. Tính xác suất để đại biểu đó không nói được cả hai thứ tiếng Anh và '
                 'Pháp.',
            'answer': ['0,2', '0.2'],
            'unit': None,
            'solution': 'Xác suất nói được ít nhất 1 thứ tiếng là $P(A \\cup B) = 0,6 + 0,45 - 0,25 = 0,8$. '
                        'Vậy xác suất không nói được cả 2 thứ tiếng là $1 - 0,8 = 0,2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch08-quy-tac-xac-suat',
  'context_title': 'Chương VIII: Các quy tắc tính xác suất',
  'context': 'Chương VIII · SGK Toán 11: Biến cố hợp, biến cố giao, biến cố độc lập, công thức cộng xác suất '
             'và công thức nhân xác suất.',
  'title': 'Bài 30: Công thức nhân xác suất cho hai biến cố độc lập',
  'icon': '✖️',
  'description': 'Công thức nhân xác suất cho hai biến cố độc lập và cách kết hợp quy tắc nhân, quy tắc '
                 'cộng, biến cố đối để giải toán xác suất.',
  'requirements': ['Phát biểu và áp dụng được công thức nhân xác suất cho hai biến cố độc lập: $P(AB) = P(A) '
                   '\\cdot P(B)$.',
                   'Kiểm tra được tính độc lập của hai biến cố dựa vào đẳng thức $P(AB) = P(A) \\cdot P(B)$.',
                   'Kết hợp công thức nhân xác suất và biến cố đối để tính xác suất có ít nhất một biến cố '
                   'xảy ra: $P(A \\cup B) = 1 - P(\\overline{A})P(\\overline{B})$.'],
  'definition': 'Nếu hai biến cố $A$ và $B$ độc lập với nhau thì xác suất của biến cố giao $AB$ bằng tích '
                'xác suất của hai biến cố đó: $P(AB) = P(A) \\cdot P(B)$.',
  'theory': '1. Hai biến cố $A$ và $B$ độc lập khi và chỉ khi $P(AB) = P(A) \\cdot P(B)$. 2. Khi $A$ và $B$ '
            'độc lập, xác suất để có ít nhất một biến cố xảy ra là $P(A \\cup B) = 1 - '
            'P(\\overline{A}\\overline{B}) = 1 - P(\\overline{A}) \\cdot P(\\overline{B})$.',
  'formulas': [{'category': 'Công thức nhân xác suất cho các biến cố độc lập',
                'items': [{'name': 'Hai biến cố độc lập', 'formula': '$P(AB) = P(A) \\cdot P(B)$'},
                          {'name': 'Cặp biến cố độc lập suy ra',
                           'formula': '$P(A\\overline{B}) = P(A) \\cdot P(\\overline{B}), \\quad '
                                      'P(\\overline{A}\\overline{B}) = P(\\overline{A}) \\cdot '
                                      'P(\\overline{B})$'},
                          {'name': 'Xác suất có ít nhất một biến cố xảy ra',
                           'formula': '$P(A \\cup B) = 1 - P(\\overline{A}) \\cdot P(\\overline{B})$'}]}],
  'example': 'Hai vận động viên A và B độc lập nhau cùng bắn mỗi người một viên đạn vào bia. Xác suất bắn '
             'trúng của A là $0,8$ và của B là $0,7$. Tính xác suất để có ít nhất một người bắn trúng bia.',
  'example_answer': 'Xác suất cả hai người cùng bắn trượt là $P(\\overline{A}\\overline{B}) = '
                    'P(\\overline{A}) \\cdot P(\\overline{B}) = (1 - 0,8)(1 - 0,7) = 0,2 \\cdot 0,3 = 0,06$. '
                    'Vậy xác suất có ít nhất một người bắn trúng là $P(A \\cup B) = 1 - 0,06 = 0,94$.',
  'real_life': 'Tính xác suất hoạt động an toàn của tàu vũ trụ hoặc máy bay thương mại có nhiều động cơ hoạt '
               'động độc lập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố $A$ và $B$ độc lập với nhau. Khẳng định nào dưới đây đúng?',
            'options': ['$P(AB) = P(A) + P(B)$',
                        '$P(AB) = P(A) \\cdot P(B)$',
                        '$P(AB) = 0$',
                        '$P(A \\cup B) = P(A) \\cdot P(B)$'],
            'answer': 1,
            'solution': 'Theo công thức nhân xác suất cho hai biến cố độc lập, $P(AB) = P(A) \\cdot P(B)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hai biến cố độc lập $A$ và $B$ có $P(A) = 0,4$ và $P(B) = 0,5$. Xác suất của biến cố '
                 'giao $AB$ bằng:',
            'options': ['$0,90$', '$0,10$', '$0,20$', '$0,45$'],
            'answer': 2,
            'solution': 'Vì $A$ và $B$ độc lập nên $P(AB) = P(A) \\cdot P(B) = 0,4 \\cdot 0,5 = 0,20$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 30: Công thức nhân xác suất cho hai biến cố độc lập**, '
                 'công thức hoặc quy tắc nào sau đây biểu diễn đúng **Hai biến cố độc lập**?',
            'options': ['$P(A\\overline{B}) = P(A) \\cdot P(\\overline{B}), \\quad '
                        'P(\\overline{A}\\overline{B}) = P(\\overline{A}) \\cdot P(\\overline{B})$',
                        '$P(A \\cup B) = 1 - P(\\overline{A}) \\cdot P(\\overline{B})$',
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$',
                        '$P(AB) = P(A) \\cdot P(B)$'],
            'answer': 3,
            'solution': 'Theo bảng công thức trọng tâm của Bài 30: Công thức nhân xác suất cho hai biến cố '
                        'độc lập, **Hai biến cố độc lập** được xác định bởi: $P(AB) = P(A) \\cdot P(B)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Công thức nhân xác suất cho hai biến cố độc lập**, nội dung/biểu thức '
                 '$P(A\\overline{B}) = P(A) \\cdot P(\\overline{B}), \\quad P(\\overline{A}\\overline{B}) = '
                 'P(\\overline{A}) \\cdot P(\\overline{B})$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Cặp biến cố độc lập suy ra',
                        'Hai biến cố độc lập',
                        'Xác suất có ít nhất một biến cố xảy ra',
                        'Đổi độ và radian'],
            'answer': 0,
            'solution': 'Trong Bài 30: Công thức nhân xác suất cho hai biến cố độc lập, biểu thức/quy tắc '
                        '$P(A\\overline{B}) = P(A) \\cdot P(\\overline{B}), \\quad '
                        'P(\\overline{A}\\overline{B}) = P(\\overline{A}) \\cdot P(\\overline{B})$ chính là '
                        'nội dung của **Cặp biến cố độc lập suy ra**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai biến cố độc lập $A$ và $B$ với $P(A) = 0,6$ và $P(B) = 0,5$. Xác suất để biến cố '
                 '$A$ xảy ra nhưng biến cố $B$ không xảy ra là:',
            'options': ['$0,20$', '$0,30$', '$0,10$', '$0,80$'],
            'answer': 1,
            'solution': 'Vì $A$ và $\\overline{B}$ độc lập nên $P(A\\overline{B}) = P(A) \\cdot '
                        'P(\\overline{B}) = 0,6 \\cdot (1 - 0,5) = 0,30$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Công thức nhân xác suất cho hai biến cố độc lập** (Chương VIII: Các quy '
                 'tắc tính xác suất), khẳng định nào sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất '
                 'kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Phát biểu và áp dụng được công thức nhân xác suất cho hai biến cố độc lập: $P(AB) = '
                        'P(A) \\cdot P(B)$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 2,
            'solution': 'Theo yêu cầu cần đạt của Bài 30: Công thức nhân xác suất cho hai biến cố độc lập: '
                        'Phát biểu và áp dụng được công thức nhân xác suất cho hai biến cố độc lập: $P(AB) = '
                        'P(A) \\cdot P(B)$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Hai máy tự động hoạt động độc lập với nhau. Trong một ngày làm việc, xác suất máy I bị '
                 'hỏng là $0,1$ và xác suất máy II bị hỏng là $0,2$. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Xác suất máy I hoạt động tốt trong ngày là $0,9$.',
                           'Xác suất cả hai máy cùng bị hỏng trong ngày là $0,02$.',
                           'Xác suất cả hai máy cùng hoạt động tốt trong ngày là $0,72$.',
                           'Xác suất có đúng một máy bị hỏng trong ngày là $0,3$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $1 - 0,1 = 0,9$. b) Đúng vì $0,1 \\cdot 0,2 = 0,02$. c) Đúng vì $0,9 '
                        '\\cdot 0,8 = 0,72$. d) Sai vì xác suất có đúng 1 máy hỏng là $0,1 \\cdot 0,8 + 0,9 '
                        '\\cdot 0,2 = 0,08 + 0,18 = 0,26 \\ne 0,3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 30: Công thức nhân xác '
                 'suất cho hai biến cố độc lập**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Phát biểu và áp dụng được công '
                           'thức nhân xác suất cho hai biến cố độc lập: $P(AB) = P(A) \\cdot P(B)$.',
                           'Quy tắc/công thức **Hai biến cố độc lập** trong bài được xác định bởi: $P(AB) = '
                           'P(A) \\cdot P(B)$.',
                           'Trong mọi trường hợp, **Hai biến cố độc lập** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 30: Công thức nhân xác suất cho hai biến cố độc lập.',
                           'Với bài toán minh họa: “Hai vận động viên A và B độc lập nhau cùng bắn mỗi người '
                           'một viên đạn vào bia. Xác suất bắn trúng của A là $0,8$ và của B là $0,7$. Tính '
                           'xác...”, lời giải đúng là: Xác suất cả hai người cùng bắn trượt là '
                           '$P(\\overline{A}\\overline{B}) = P(\\overline{A}) \\cdot P(\\overline{B}) = (1 - '
                           '0,8)(1 - 0,7) = 0,2 \\cdot 0,3 = 0,06$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 30: Công thức nhân xác suất cho hai biến '
                        'cố độc lập. b) **Đúng** theo công thức trọng tâm **Hai biến cố độc lập** ($P(AB) = '
                        'P(A) \\cdot P(B)$). c) **Sai** vì $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, '
                        '\\quad \\alpha\\text{ rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là '
                        'công thức của nội dung khác, không phải quy tắc chung của **Hai biến cố độc lập**. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 30: Công thức nhân xác suất cho hai biến cố độc lập** để giải '
                 'quyết tình huống sau: Hai vận động viên A và B độc lập nhau cùng bắn mỗi người một viên '
                 'đạn vào bia. Xác suất bắn trúng của A là $0,8$ và của B là $0,7$. Tính xác suất để có ít '
                 'nhất một người bắn trúng bia. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...',
                        'Xác suất cả hai người cùng bắn trượt là $P(\\overline{A}\\overline{B}) = '
                        'P(\\overline{A}) \\cdot P(\\overline{B}) = (1 - 0,8)(1 - 0,7) = 0,2 \\cdot 0,3 = '
                        '0,06$....'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Công thức nhân xác suất cho hai biến cố độc lập: Xác '
                        'suất cả hai người cùng bắn trượt là $P(\\overline{A}\\overline{B}) = '
                        'P(\\overline{A}) \\cdot P(\\overline{B}) = (1 - 0,8)(1 - 0,7) = 0,2 \\cdot 0,3 = '
                        '0,06$. Vậy xác suất có ít nhất một người bắn trúng là $P(A \\cup B) = 1 - 0,06 = '
                        '0,94$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hệ thống bảo vệ gồm hai rơ-le hoạt động độc lập. Xác suất mỗi rơ-le đóng mạch thành '
                 'công khi có sự cố đều bằng $0,9$. Tính xác suất để hệ thống bảo vệ hoạt động (tức có ít '
                 'nhất một rơ-le đóng mạch thành công) khi có sự cố.',
            'answer': ['0,99', '0.99'],
            'unit': None,
            'solution': 'Xác suất cả hai rơ-le đều thất bại là $(1 - 0,9) \\cdot (1 - 0,9) = 0,01$. Vậy xác '
                        'suất có ít nhất một rơ-le thành công là $1 - 0,01 = 0,99$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch09-dao-ham',
  'context_title': 'Chương IX: Đạo hàm',
  'context': 'Chương IX · SGK Toán 11: Định nghĩa, ý nghĩa của đạo hàm, các quy tắc tính đạo hàm và đạo hàm '
             'cấp hai.',
  'title': 'Bài 31: Định nghĩa và ý nghĩa của đạo hàm',
  'icon': '📈',
  'description': 'Định nghĩa đạo hàm tại một điểm bằng giới hạn, ý nghĩa hình học (hệ số góc tiếp tuyến) và '
                 'ý nghĩa vật lí (vận tốc tức thời) của đạo hàm.',
  'requirements': ["Hiểu được định nghĩa đạo hàm tại điểm $x_0$: $f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) "
                   '- f(x_0)}{x - x_0}$.',
                   'Viết được phương trình tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $M(x_0; f(x_0))$ '
                   "với hệ số góc $k = f'(x_0)$.",
                   "Nắm được ý nghĩa vật lí của đạo hàm: vận tốc tức thời $v(t_0) = s'(t_0)$."],
  'definition': 'Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ và điểm $x_0 \\in (a; b)$. Nếu tồn tại '
                'giới hạn hữu hạn $\\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0}$ thì giới hạn đó được '
                "gọi là đạo hàm của hàm số $y = f(x)$ tại điểm $x_0$, kí hiệu là $f'(x_0)$ hoặc $y'(x_0)$.",
  'theory': "1. Ý nghĩa hình học: đạo hàm $f'(x_0)$ là hệ số góc của tiếp tuyến với đồ thị hàm số $y = f(x)$ "
            "tại điểm $M_0(x_0; f(x_0))$. Phương trình tiếp tuyến tại $M_0$ là $y = f'(x_0)(x - x_0) + "
            'f(x_0)$. 2. Ý nghĩa vật lí: nếu quãng đường chuyển động là $s = s(t)$ thì vận tốc tức thời tại '
            "thời điểm $t_0$ là $v(t_0) = s'(t_0)$; nếu điện lượng là $Q = Q(t)$ thì cường độ dòng điện tức "
            "thời là $I(t_0) = Q'(t_0)$.",
  'formulas': [{'category': 'Định nghĩa và ý nghĩa của đạo hàm',
                'items': [{'name': 'Định nghĩa đạo hàm tại một điểm',
                           'formula': "$f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0} = "
                                      '\\lim_{\\Delta x \\to 0} \\dfrac{f(x_0 + \\Delta x) - f(x_0)}{\\Delta '
                                      'x}$'},
                          {'name': 'Phương trình tiếp tuyến tại M(x_0; y_0)',
                           'formula': "$y = f'(x_0)(x - x_0) + f(x_0)$"},
                          {'name': 'Vận tốc và cường độ dòng điện tức thời',
                           'formula': "$v(t_0) = s'(t_0), \\quad I(t_0) = Q'(t_0)$"}]}],
  'example': "Cho hàm số $f(x) = x^2$. Biết $f'(2) = 4$, hãy viết phương trình tiếp tuyến của parabol $y = "
             'x^2$ tại điểm $M(2; 4)$.',
  'example_answer': "Hệ số góc của tiếp tuyến tại $M(2; 4)$ là $k = f'(2) = 4$. Phương trình tiếp tuyến là "
                    '$y = 4(x - 2) + 4 \\Leftrightarrow y = 4x - 4$.',
  'real_life': "Đồng hồ đo tốc độ (công-tơ-mét) trên xe máy và ô tô hiển thị vận tốc tức thời $v(t) = s'(t)$ "
               'của xe.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hàm số $y = f(x)$ có đạo hàm tại điểm $x_0$. Hệ số góc $k$ của tiếp tuyến với đồ thị '
                 'hàm số tại điểm $M_0(x_0; f(x_0))$ là:',
            'options': ['$k = f(x_0)$', '$k = x_0$', "$k = f'(x_0)$", "$k = -\\dfrac{1}{f'(x_0)}$"],
            'answer': 2,
            'solution': 'Theo ý nghĩa hình học của đạo hàm, hệ số góc của tiếp tuyến tại $M_0(x_0; f(x_0))$ '
                        "là $k = f'(x_0)$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Cho hàm số $y = f(x)$ xác định trên khoảng $(a; b)$ chứa $x_0$. Đạo hàm $f'(x_0)$ được "
                 'định nghĩa bởi giới hạn nào dưới đây?',
            'options': ['$\\lim_{x \\to x_0} \\dfrac{f(x) + f(x_0)}{x - x_0}$',
                        '$\\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x + x_0}$',
                        '$\\lim_{x \\to 0} \\dfrac{f(x) - f(x_0)}{x - x_0}$',
                        '$\\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0}$'],
            'answer': 3,
            'solution': "Theo định nghĩa, $f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0}$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 31: Định nghĩa và ý nghĩa của đạo hàm**, công thức hoặc '
                 'quy tắc nào sau đây biểu diễn đúng **Định nghĩa đạo hàm tại một điểm**?',
            'options': ["$f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0} = \\lim_{\\Delta x "
                        '\\to 0} \\dfrac{f(x_0 + \\Delta x) - f(x_0)}{\\Delta x}$',
                        "$y = f'(x_0)(x - x_0) + f(x_0)$",
                        "$v(t_0) = s'(t_0), \\quad I(t_0) = Q'(t_0)$",
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 0,
            'solution': 'Theo bảng công thức trọng tâm của Bài 31: Định nghĩa và ý nghĩa của đạo hàm, **Định '
                        "nghĩa đạo hàm tại một điểm** được xác định bởi: $f'(x_0) = \\lim_{x \\to x_0} "
                        '\\dfrac{f(x) - f(x_0)}{x - x_0} = \\lim_{\\Delta x \\to 0} \\dfrac{f(x_0 + \\Delta '
                        'x) - f(x_0)}{\\Delta x}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Trong **Bài 31: Định nghĩa và ý nghĩa của đạo hàm**, nội dung/biểu thức $y = f'(x_0)(x - "
                 'x_0) + f(x_0)$ là quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa đạo hàm tại một điểm',
                        'Phương trình tiếp tuyến tại M(x_0; y_0)',
                        'Vận tốc và cường độ dòng điện tức thời',
                        'Đổi độ và radian'],
            'answer': 1,
            'solution': "Trong Bài 31: Định nghĩa và ý nghĩa của đạo hàm, biểu thức/quy tắc $y = f'(x_0)(x - "
                        'x_0) + f(x_0)$ chính là nội dung của **Phương trình tiếp tuyến tại M(x_0; y_0)**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho hàm số $y = f(x)$ có đồ thị $(C)$ thỏa mãn $f(1) = 2$ và $f'(1) = -3$. Phương trình "
                 'tiếp tuyến của $(C)$ tại điểm có hoành độ $x_0 = 1$ là:',
            'options': ['$y = -3x - 1$', '$y = 2x - 3$', '$y = -3x + 5$', '$y = -3x + 2$'],
            'answer': 2,
            'solution': "Phương trình tiếp tuyến là $y = f'(1)(x - 1) + f(1) = -3(x - 1) + 2 = -3x + 5$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Định nghĩa và ý nghĩa của đạo hàm** (Chương IX: Đạo hàm), khẳng định nào '
                 'sau đây phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).',
                        "Hiểu được định nghĩa đạo hàm tại điểm $x_0$: $f'(x_0) = \\lim_{x \\to x_0} "
                        '\\dfrac{f(x) - f(x_0)}{x - x_0}$.'],
            'answer': 3,
            'solution': 'Theo yêu cầu cần đạt của Bài 31: Định nghĩa và ý nghĩa của đạo hàm: Hiểu được định '
                        "nghĩa đạo hàm tại điểm $x_0$: $f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - "
                        'f(x_0)}{x - x_0}$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một vật rơi tự do theo phương trình quãng đường $s(t) = 5t^2$ ($s$ tính bằng mét, $t$ tính '
                 "bằng giây). Biết đạo hàm của $s(t)$ tại thời điểm $t_0$ là $s'(t_0) = 10t_0$. Xét tính "
                 'đúng sai của các mệnh đề sau:',
            'statements': ['Quãng đường vật rơi được sau $2$ giây đầu tiên là $20\\text{ m}$.',
                           'Vận tốc tức thời của vật tại thời điểm $t = 2$ giây là $20\\text{ m/s}$.',
                           'Vận tốc tức thời của vật tại thời điểm $t = 3$ giây là $45\\text{ m/s}$.',
                           'Tại thời điểm vận tốc tức thời đạt $40\\text{ m/s}$ thì vật đã rơi được $4$ '
                           'giây.'],
            'answer': [True, True, False, True],
            'solution': "a) Đúng vì $s(2) = 5 \\cdot 2^2 = 20\\text{ m}$. b) Đúng vì $v(2) = s'(2) = 10 "
                        "\\cdot 2 = 20\\text{ m/s}$. c) Sai vì $v(3) = s'(3) = 10 \\cdot 3 = 30\\text{ m/s}$ "
                        '(còn $45\\text{ m}$ là quãng đường $s(3)$). d) Đúng vì $10t = 40 \\Leftrightarrow t '
                        '= 4\\text{ s}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 31: Định nghĩa và ý '
                 'nghĩa của đạo hàm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được định nghĩa đạo hàm tại '
                           "điểm $x_0$: $f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0}$.",
                           'Quy tắc/công thức **Định nghĩa đạo hàm tại một điểm** trong bài được xác định '
                           "bởi: $f'(x_0) = \\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0} = "
                           '\\lim_{\\Delta x \\to 0} \\dfrac{f(x_0 + \\Delta x) - f(x_0)}{\\Delta x}$.',
                           'Trong mọi trường hợp, **Định nghĩa đạo hàm tại một điểm** luôn được tính bằng '
                           'công thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ '
                           'rad} = \\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) '
                           'mà không cần điều kiện của Bài 31: Định nghĩa và ý nghĩa của đạo hàm.',
                           "Với bài toán minh họa: “Cho hàm số $f(x) = x^2$. Biết $f'(2) = 4$, hãy viết "
                           'phương trình tiếp tuyến của parabol $y = x^2$ tại điểm $M(2; 4)$.”, lời giải '
                           "đúng là: Hệ số góc của tiếp tuyến tại $M(2; 4)$ là $k = f'(2) = 4$. Phương trình "
                           'tiếp tuyến là $y = 4(x - 2) + 4 \\Leftrightarrow y = 4x - 4$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 31: Định nghĩa và ý nghĩa của đạo hàm. b) '
                        "**Đúng** theo công thức trọng tâm **Định nghĩa đạo hàm tại một điểm** ($f'(x_0) = "
                        '\\lim_{x \\to x_0} \\dfrac{f(x) - f(x_0)}{x - x_0} = \\lim_{\\Delta x \\to 0} '
                        '\\dfrac{f(x_0 + \\Delta x) - f(x_0)}{\\Delta x}$). c) **Sai** vì $a^\\circ = '
                        '\\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa đạo hàm tại một điểm**. d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 31: Định nghĩa và ý nghĩa của đạo hàm** để giải quyết tình huống '
                 "sau: Cho hàm số $f(x) = x^2$. Biết $f'(2) = 4$, hãy viết phương trình tiếp tuyến của "
                 'parabol $y = x^2$ tại điểm $M(2; 4)$. Kết quả và hướng giải nào dưới đây là **đúng**?',
            'options': ["Hệ số góc của tiếp tuyến tại $M(2; 4)$ là $k = f'(2) = 4$. Phương trình tiếp tuyến "
                        'là $y = 4(x - 2) + 4 \\Leftrightarrow y = 4x - 4$.',
                        'Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Định nghĩa và ý nghĩa của đạo hàm: Hệ số góc của '
                        "tiếp tuyến tại $M(2; 4)$ là $k = f'(2) = 4$. Phương trình tiếp tuyến là $y = 4(x - "
                        '2) + 4 \\Leftrightarrow y = 4x - 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm $M(2; 3)$ đi qua điểm $A(0; -5)$. Tính '
                 "giá trị đạo hàm $f'(2)$.",
            'answer': ['4'],
            'unit': None,
            'solution': "Hệ số góc của tiếp tuyến đi qua hai điểm $M(2; 3)$ và $A(0; -5)$ là $f'(2) = k = "
                        '\\dfrac{3 - (-5)}{2 - 0} = \\dfrac{8}{2} = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch09-dao-ham',
  'context_title': 'Chương IX: Đạo hàm',
  'context': 'Chương IX · SGK Toán 11: Định nghĩa, ý nghĩa của đạo hàm, các quy tắc tính đạo hàm và đạo hàm '
             'cấp hai.',
  'title': 'Bài 32: Các quy tắc tính đạo hàm',
  'icon': '⚙️',
  'description': 'Bảng đạo hàm của các hàm số sơ cấp cơ bản, quy tắc đạo hàm của tổng, hiệu, tích, thương và '
                 'quy tắc đạo hàm của hàm hợp.',
  'requirements': ['Thuộc lòng bảng đạo hàm của hàm lũy thừa, căn thức, hàm lượng giác, hàm số mũ và hàm số '
                   'lôgarit.',
                   "Vận dụng thành thạo quy tắc đạo hàm của tổng, hiệu $(u \\pm v)'$, tích $(uv)' = u'v + "
                   "uv'$ và thương $\\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$.",
                   "Tính được đạo hàm của hàm hợp $y'_x = y'_u \\cdot u'_x$."],
  'definition': 'Các quy tắc tính đạo hàm cho phép tìm đạo hàm của các hàm số sơ cấp và hàm hợp một cách '
                'nhanh chóng mà không cần tính trực tiếp giới hạn theo định nghĩa.',
  'theory': "1. Đạo hàm cơ bản: $(c)' = 0$; $(x^n)' = nx^{n-1}$; $(\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}$; "
            "$(\\sin x)' = \\cos x$; $(\\cos x)' = -\\sin x$; $(\\tan x)' = \\dfrac{1}{\\cos^2 x}$; $(e^x)' "
            "= e^x$; $(a^x)' = a^x \\ln a$; $(\\ln x)' = \\dfrac{1}{x}$; $(\\log_a x)' = \\dfrac{1}{x \\ln "
            "a}$. 2. Quy tắc hàm hợp: nếu $y = f(u)$ và $u = u(x)$ thì $y'_x = f'(u) \\cdot u'(x)$.",
  'formulas': [{'category': 'Bảng đạo hàm và các quy tắc tính',
                'items': [{'name': 'Quy tắc tích và thương',
                           'formula': "$(uv)' = u'v + uv', \\quad \\left(\\dfrac{u}{v}\\right)' = "
                                      "\\dfrac{u'v - uv'}{v^2}$"},
                          {'name': 'Đạo hàm lũy thừa và căn thức',
                           'formula': "$(x^n)' = nx^{n-1}, \\quad (\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}, "
                                      "\\quad (\\sqrt{u})' = \\dfrac{u'}{2\\sqrt{u}}$"},
                          {'name': 'Đạo hàm lượng giác',
                           'formula': "$(\\sin x)' = \\cos x, \\quad (\\cos x)' = -\\sin x, \\quad (\\tan "
                                      "x)' = \\dfrac{1}{\\cos^2 x}$"},
                          {'name': 'Đạo hàm mũ và lôgarit',
                           'formula': "$(e^x)' = e^x, \\quad (a^x)' = a^x \\ln a, \\quad (\\ln x)' = "
                                      "\\dfrac{1}{x}, \\quad (\\log_a x)' = \\dfrac{1}{x \\ln a}$"}]}],
  'example': 'Tính đạo hàm của các hàm số: a) $y = x^3 - 4x^2 + 5x - 2$; b) $y = \\ln(x^2 + 1)$.',
  'example_answer': "a) $y' = 3x^2 - 8x + 5$. b) Áp dụng đạo hàm hàm hợp $(\\ln u)' = \\dfrac{u'}{u}$, ta có "
                    "$y' = \\dfrac{(x^2 + 1)'}{x^2 + 1} = \\dfrac{2x}{x^2 + 1}$.",
  'real_life': 'Tính tốc độ biến thiên của công suất điện, tốc độ phản ứng hóa học và độ nhạy của các hàm '
               'chi phí kinh tế.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đạo hàm của hàm số $y = x^4 - 3x^2 + 2$ là:',
            'options': ["$y' = 4x^3 - 3x$", "$y' = x^3 - 6x$", "$y' = 4x^3 - 6x + 2$", "$y' = 4x^3 - 6x$"],
            'answer': 3,
            'solution': "Ta có $y' = (x^4)' - 3(x^2)' + (2)' = 4x^3 - 6x$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khẳng định nào dưới đây đúng?',
            'options': ["$(\\sin x)' = \\cos x$",
                        "$(\\sin x)' = -\\cos x$",
                        "$(\\cos x)' = \\sin x$",
                        "$(\\ln x)' = e^x$"],
            'answer': 0,
            'solution': "Theo bảng đạo hàm cơ bản: $(\\sin x)' = \\cos x$ và $(\\cos x)' = -\\sin x$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 32: Các quy tắc tính đạo hàm**, công thức hoặc quy tắc '
                 'nào sau đây biểu diễn đúng **Quy tắc tích và thương**?',
            'options': ["$(x^n)' = nx^{n-1}, \\quad (\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}, \\quad "
                        "(\\sqrt{u})' = \\dfrac{u'}{2\\sqrt{u}}$",
                        "$(uv)' = u'v + uv', \\quad \\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$",
                        "$(\\sin x)' = \\cos x, \\quad (\\cos x)' = -\\sin x, \\quad (\\tan x)' = "
                        '\\dfrac{1}{\\cos^2 x}$',
                        "$(e^x)' = e^x, \\quad (a^x)' = a^x \\ln a, \\quad (\\ln x)' = \\dfrac{1}{x}, \\quad "
                        "(\\log_a x)' = \\dfrac{1}{x \\ln a}$"],
            'answer': 1,
            'solution': 'Theo bảng công thức trọng tâm của Bài 32: Các quy tắc tính đạo hàm, **Quy tắc tích '
                        "và thương** được xác định bởi: $(uv)' = u'v + uv', \\quad "
                        "\\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Trong **Bài 32: Các quy tắc tính đạo hàm**, nội dung/biểu thức $(x^n)' = nx^{n-1}, \\quad "
                 "(\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}, \\quad (\\sqrt{u})' = \\dfrac{u'}{2\\sqrt{u}}$ là "
                 'quy tắc hoặc công thức của mục nào sau đây?',
            'options': ['Quy tắc tích và thương',
                        'Đạo hàm lượng giác',
                        'Đạo hàm lũy thừa và căn thức',
                        'Đạo hàm mũ và lôgarit'],
            'answer': 2,
            'solution': "Trong Bài 32: Các quy tắc tính đạo hàm, biểu thức/quy tắc $(x^n)' = nx^{n-1}, "
                        "\\quad (\\sqrt{x})' = \\dfrac{1}{2\\sqrt{x}}, \\quad (\\sqrt{u})' = "
                        "\\dfrac{u'}{2\\sqrt{u}}$ chính là nội dung của **Đạo hàm lũy thừa và căn thức**."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đạo hàm của hàm số $y = \\dfrac{2x + 1}{x - 1}$ ($x \\ne 1$) là:',
            'options': ["$y' = \\dfrac{3}{(x - 1)^2}$",
                        "$y' = -\\dfrac{1}{(x - 1)^2}$",
                        "$y' = \\dfrac{2}{(x - 1)^2}$",
                        "$y' = -\\dfrac{3}{(x - 1)^2}$"],
            'answer': 3,
            'solution': "Áp dụng quy tắc thương: $y' = \\dfrac{2(x - 1) - (2x + 1) \\cdot 1}{(x - 1)^2} = "
                        '-\\dfrac{3}{(x - 1)^2}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Các quy tắc tính đạo hàm** (Chương IX: Đạo hàm), khẳng định nào sau đây '
                 'phản ánh **đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Thuộc lòng bảng đạo hàm của hàm lũy thừa, căn thức, hàm lượng giác, hàm số mũ và '
                        'hàm số lôgarit.',
                        'Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 0,
            'solution': 'Theo yêu cầu cần đạt của Bài 32: Các quy tắc tính đạo hàm: Thuộc lòng bảng đạo hàm '
                        'của hàm lũy thừa, căn thức, hàm lượng giác, hàm số mũ và hàm số lôgarit.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho các hàm số sơ cấp và hàm hợp. Xét tính đúng sai của các mệnh đề sau:',
            'statements': ["Đạo hàm của hàm số $y = e^{2x}$ là $y' = 2e^{2x}$.",
                           "Đạo hàm của hàm số $y = \\cos 3x$ là $y' = 3\\sin 3x$.",
                           "Đạo hàm của hàm số $y = \\sqrt{x^2 + 1}$ là $y' = \\dfrac{x}{\\sqrt{x^2 + 1}}$.",
                           "Với $f(x) = x \\ln x$ ($x > 0$) thì $f'(e) = 2$."],
            'answer': [True, False, True, True],
            'solution': "a) Đúng vì $(e^u)' = u' e^u = 2e^{2x}$. b) Sai vì $(\\cos 3x)' = -3\\sin 3x$. c) "
                        "Đúng vì $(\\sqrt{u})' = \\dfrac{2x}{2\\sqrt{x^2 + 1}} = \\dfrac{x}{\\sqrt{x^2 + "
                        "1}}$. d) Đúng vì $f'(x) = \\ln x + x \\cdot \\dfrac{1}{x} = \\ln x + 1 \\Rightarrow "
                        "f'(e) = \\ln e + 1 = 2$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 32: Các quy tắc tính '
                 'đạo hàm**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Thuộc lòng bảng đạo hàm của hàm '
                           'lũy thừa, căn thức, hàm lượng giác, hàm số mũ và hàm số lôgarit.',
                           "Quy tắc/công thức **Quy tắc tích và thương** trong bài được xác định bởi: $(uv)' "
                           "= u'v + uv', \\quad \\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$.",
                           'Trong mọi trường hợp, **Quy tắc tích và thương** luôn được tính bằng công thức '
                           '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 32: Các quy tắc tính đạo hàm.',
                           'Với bài toán minh họa: “Tính đạo hàm của các hàm số: a) $y = x^3 - 4x^2 + 5x - '
                           "2$; b) $y = \\ln(x^2 + 1)$.”, lời giải đúng là: a) $y' = 3x^2 - 8x + 5$. b) Áp "
                           "dụng đạo hàm hàm hợp $(\\ln u)' = \\dfrac{u'}{u}$, ta có $y' = \\dfrac{(x^2 + "
                           "1)'}{x^2 + 1} = \\dfrac{2x}{x^2 + 1}$..."],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 32: Các quy tắc tính đạo hàm. b) **Đúng** '
                        "theo công thức trọng tâm **Quy tắc tích và thương** ($(uv)' = u'v + uv', \\quad "
                        "\\left(\\dfrac{u}{v}\\right)' = \\dfrac{u'v - uv'}{v^2}$). c) **Sai** vì $a^\\circ "
                        '= \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Quy tắc tích và thương**. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 32: Các quy tắc tính đạo hàm** để giải quyết tình huống sau: Tính '
                 'đạo hàm của các hàm số: a) $y = x^3 - 4x^2 + 5x - 2$; b) $y = \\ln(x^2 + 1)$. Kết quả và '
                 'hướng giải nào dưới đây là **đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        "a) $y' = 3x^2 - 8x + 5$. b) Áp dụng đạo hàm hàm hợp $(\\ln u)' = \\dfrac{u'}{u}$, "
                        "ta có $y' = \\dfrac{(x^2 + 1)'}{x^2 + 1} = \\dfrac{2x}{x^2 + 1}$.",
                        'Ta có...',
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 1,
            'solution': "Lời giải chi tiết theo Bài 32: Các quy tắc tính đạo hàm: a) $y' = 3x^2 - 8x + 5$. "
                        "b) Áp dụng đạo hàm hàm hợp $(\\ln u)' = \\dfrac{u'}{u}$, ta có $y' = \\dfrac{(x^2 + "
                        "1)'}{x^2 + 1} = \\dfrac{2x}{x^2 + 1}$."},
           {'level': 'vandung',
            'type': 'short',
            'q': "Cho hàm số $f(x) = x^3 - 3x^2 + 2x - 1$. Tính tổng các nghiệm của phương trình $f'(x) = "
                 '2$.',
            'answer': ['2'],
            'unit': None,
            'solution': "Ta có $f'(x) = 3x^2 - 6x + 2$. Phương trình $f'(x) = 2 \\Leftrightarrow 3x^2 - 6x = "
                        '0 \\Leftrightarrow x = 0$ hoặc $x = 2$. Tổng các nghiệm bằng $0 + 2 = 2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l11-ch09-dao-ham',
  'context_title': 'Chương IX: Đạo hàm',
  'context': 'Chương IX · SGK Toán 11: Định nghĩa, ý nghĩa của đạo hàm, các quy tắc tính đạo hàm và đạo hàm '
             'cấp hai.',
  'title': 'Bài 33: Đạo hàm cấp hai',
  'icon': '🚀',
  'description': 'Khái niệm đạo hàm cấp hai của một hàm số và ý nghĩa cơ học của đạo hàm cấp hai (gia tốc '
                 'tức thời của chuyển động).',
  'requirements': ["Hiểu được định nghĩa đạo hàm cấp hai $f''(x) = [f'(x)]'$ là đạo hàm của đạo hàm cấp một.",
                   'Tính được đạo hàm cấp hai của các hàm đa thức, lượng giác, mũ và lôgarit.',
                   "Vận dụng ý nghĩa cơ học của đạo hàm cấp hai để tính gia tốc tức thời $a(t) = s''(t)$ của "
                   'chuyển động.'],
  'definition': "Cho hàm số $y = f(x)$ có đạo hàm $y' = f'(x)$ tại mọi điểm $x \\in (a; b)$. Nếu hàm số $y' "
                "= f'(x)$ lại có đạo hàm tại $x$ thì ta gọi đạo hàm của $y'$ là đạo hàm cấp hai của hàm số "
                "$y = f(x)$ tại $x$, kí hiệu là $y''$ hoặc $f''(x)$.",
  'theory': "1. Quy tắc tính: $f''(x) = [f'(x)]'$. 2. Ý nghĩa cơ học: một chất điểm chuyển động theo phương "
            'trình $s = s(t)$ thì gia tốc tức thời của chất điểm tại thời điểm $t$ là đạo hàm cấp hai của '
            "quãng đường theo thời gian: $a(t) = v'(t) = s''(t)$.",
  'formulas': [{'category': 'Đạo hàm cấp hai và gia tốc tức thời',
                'items': [{'name': 'Định nghĩa đạo hàm cấp hai', 'formula': "$f''(x) = [f'(x)]'$"},
                          {'name': 'Gia tốc tức thời của chuyển động', 'formula': "$a(t) = v'(t) = s''(t)$"},
                          {'name': 'Phương trình dao động điều hòa',
                           'formula': "$x(t) = A\\cos(\\omega t + \\varphi) \\Rightarrow a(t) = x''(t) = "
                                      '-\\omega^2 x(t)$'}]}],
  'example': 'Tìm đạo hàm cấp hai của hàm số $y = x^4 - 3x^2 + \\sin 2x$.',
  'example_answer': "Ta có đạo hàm cấp một: $y' = 4x^3 - 6x + 2\\cos 2x$. Lấy đạo hàm một lần nữa ta được "
                    "đạo hàm cấp hai: $y'' = (y')' = 12x^2 - 6 - 4\\sin 2x$.",
  'real_life': 'Tính gia tốc tăng tốc của tên lửa đẩy, lực quán tính khi phanh xe và gia tốc trong dao động '
               'điều hòa của con lắc lò xo.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Cho hàm số $f(x) = x^3 + 2x^2 - 5x + 1$. Đạo hàm cấp hai $f''(x)$ của hàm số là:",
            'options': ["$f''(x) = 6x + 4$", "$f''(x) = 3x^2 + 4x - 5$", "$f''(x) = 6x + 2$", "$f''(x) = 6$"],
            'answer': 0,
            'solution': "Ta có $f'(x) = 3x^2 + 4x - 5 \\Rightarrow f''(x) = (3x^2 + 4x - 5)' = 6x + 4$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một chất điểm chuyển động có phương trình quãng đường $s = s(t)$ theo thời gian $t$. Gia '
                 'tốc tức thời $a(t)$ của chất điểm tại thời điểm $t$ bằng:',
            'options': ["$s'(t)$", "$s''(t)$", '$s(t)$', '$\\dfrac{s(t)}{t}$'],
            'answer': 1,
            'solution': 'Theo ý nghĩa cơ học của đạo hàm cấp hai, gia tốc tức thời tại thời điểm $t$ là '
                        "$a(t) = s''(t)$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo nội dung trọng tâm của **Bài 33: Đạo hàm cấp hai**, công thức hoặc quy tắc nào sau '
                 'đây biểu diễn đúng **Định nghĩa đạo hàm cấp hai**?',
            'options': ["$a(t) = v'(t) = s''(t)$",
                        "$x(t) = A\\cos(\\omega t + \\varphi) \\Rightarrow a(t) = x''(t) = -\\omega^2 x(t)$",
                        "$f''(x) = [f'(x)]'$",
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$'],
            'answer': 2,
            'solution': 'Theo bảng công thức trọng tâm của Bài 33: Đạo hàm cấp hai, **Định nghĩa đạo hàm cấp '
                        "hai** được xác định bởi: $f''(x) = [f'(x)]'$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Trong **Bài 33: Đạo hàm cấp hai**, nội dung/biểu thức $a(t) = v'(t) = s''(t)$ là quy tắc "
                 'hoặc công thức của mục nào sau đây?',
            'options': ['Định nghĩa đạo hàm cấp hai',
                        'Phương trình dao động điều hòa',
                        'Đổi độ và radian',
                        'Gia tốc tức thời của chuyển động'],
            'answer': 3,
            'solution': "Trong Bài 33: Đạo hàm cấp hai, biểu thức/quy tắc $a(t) = v'(t) = s''(t)$ chính là "
                        'nội dung của **Gia tốc tức thời của chuyển động**.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho hàm số $y = \\sin x$. Đạo hàm cấp hai $y''$ của hàm số là:",
            'options': ["$y'' = -\\sin x$", "$y'' = \\sin x$", "$y'' = -\\cos x$", "$y'' = \\cos x$"],
            'answer': 0,
            'solution': "Ta có $y' = \\cos x \\Rightarrow y'' = (\\cos x)' = -\\sin x$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Đạo hàm cấp hai** (Chương IX: Đạo hàm), khẳng định nào sau đây phản ánh '
                 '**đúng** yêu cầu cần đạt và bản chất kiến thức của bài?',
            'options': ['Nhận biết được khái niệm góc lượng giác, hệ thức Chasles và đổi được số đo góc giữa '
                        'độ và radian.',
                        "Hiểu được định nghĩa đạo hàm cấp hai $f''(x) = [f'(x)]'$ là đạo hàm của đạo hàm cấp "
                        'một.',
                        'Xác định được điểm biểu diễn trên đường tròn lượng giác và các giá trị $\\sin '
                        '\\alpha, \\cos \\alpha, \\tan \\alpha, \\cot \\alpha$.',
                        'Vận dụng các hệ thức lượng giác cơ bản và giá trị lượng giác của các góc có liên '
                        'quan đặc biệt (đối nhau, bù nhau, phụ nhau, hơn kém $\\pi$).'],
            'answer': 1,
            'solution': 'Theo yêu cầu cần đạt của Bài 33: Đạo hàm cấp hai: Hiểu được định nghĩa đạo hàm cấp '
                        "hai $f''(x) = [f'(x)]'$ là đạo hàm của đạo hàm cấp một."},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một chất điểm chuyển động thẳng theo phương trình $s(t) = t^3 - 3t^2 + 9t + 2$ ($s$ tính '
                 'bằng mét, $t$ tính bằng giây). Xét tính đúng sai của các mệnh đề sau:',
            'statements': ['Vận tốc tức thời của chất điểm tại thời điểm $t$ là $v(t) = 3t^2 - 6t + 9\\text{ '
                           '(m/s)}$.',
                           'Gia tốc tức thời của chất điểm tại thời điểm $t$ là $a(t) = 6t - 6\\text{ '
                           '(m/s}^2\\text{)}$.',
                           'Gia tốc của chất điểm tại thời điểm $t = 2$ giây bằng $6\\text{ m/s}^2$.',
                           'Tại thời điểm gia tốc bằng $0$, vận tốc của chất điểm cũng bằng $0$.'],
            'answer': [True, True, True, False],
            'solution': "a) Đúng vì $v(t) = s'(t) = 3t^2 - 6t + 9$. b) Đúng vì $a(t) = s''(t) = 6t - 6$. c) "
                        'Đúng vì $a(2) = 6 \\cdot 2 - 6 = 6\\text{ m/s}^2$. d) Sai vì $a(t) = 0 '
                        '\\Leftrightarrow t = 1\\text{ s}$, khi đó vận tốc là $v(1) = 3 - 6 + 9 = 6\\text{ '
                        'm/s} \\ne 0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các mệnh đề sau khi tổng hợp kiến thức **Bài 33: Đạo hàm cấp hai**:',
            'statements': ['Một trong các yêu cầu cần đạt của bài học là: Hiểu được định nghĩa đạo hàm cấp '
                           "hai $f''(x) = [f'(x)]'$ là đạo hàm của đạo hàm cấp một.",
                           'Quy tắc/công thức **Định nghĩa đạo hàm cấp hai** trong bài được xác định bởi: '
                           "$f''(x) = [f'(x)]'$.",
                           'Trong mọi trường hợp, **Định nghĩa đạo hàm cấp hai** luôn được tính bằng công '
                           'thức $a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                           '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ (thuộc Đổi độ và radian) mà '
                           'không cần điều kiện của Bài 33: Đạo hàm cấp hai.',
                           'Với bài toán minh họa: “Tìm đạo hàm cấp hai của hàm số $y = x^4 - 3x^2 + \\sin '
                           "2x$.”, lời giải đúng là: Ta có đạo hàm cấp một: $y' = 4x^3 - 6x + 2\\cos 2x$. "
                           "Lấy đạo hàm một lần nữa ta được đạo hàm cấp hai: $y'' = (y')' = 12x^2 - 6 - "
                           '4\\sin 2x$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 33: Đạo hàm cấp hai. b) **Đúng** theo công '
                        "thức trọng tâm **Định nghĩa đạo hàm cấp hai** ($f''(x) = [f'(x)]'$). c) **Sai** vì "
                        '$a^\\circ = \\dfrac{\\pi a}{180}\\text{ rad}, \\quad \\alpha\\text{ rad} = '
                        '\\left(\\dfrac{180\\alpha}{\\pi}\\right)^\\circ$ là công thức của nội dung khác, '
                        'không phải quy tắc chung của **Định nghĩa đạo hàm cấp hai**. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng kiến thức **Bài 33: Đạo hàm cấp hai** để giải quyết tình huống sau: Tìm đạo hàm '
                 'cấp hai của hàm số $y = x^4 - 3x^2 + \\sin 2x$. Kết quả và hướng giải nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $\\dfrac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$. Ta có $\\cos '
                        '\\alpha = -\\sqrt{1 - \\sin^2 \\alpha} = -\\sqrt{1 - \\dfrac{9}{25}} = '
                        '-\\dfrac{4}{5}$. Suy...',
                        'Ta có...',
                        "Ta có đạo hàm cấp một: $y' = 4x^3 - 6x + 2\\cos 2x$. Lấy đạo hàm một lần nữa ta "
                        "được đạo hàm cấp hai: $y'' = (y')' = 12x^2 - 6 - 4\\sin 2x$.",
                        'Với mọi $x \\in \\mathbb{R}$, ta có $-1 \\le \\sin 2x \\le 1 \\Rightarrow -3 \\le '
                        '3\\sin 2x \\le 3 \\Rightarrow -4 \\le 3\\sin 2x - 1 \\le 2$. Vậy tập giá trị là '
                        '$[-4; 2]$...'],
            'answer': 2,
            'solution': "Lời giải chi tiết theo Bài 33: Đạo hàm cấp hai: Ta có đạo hàm cấp một: $y' = 4x^3 - "
                        "6x + 2\\cos 2x$. Lấy đạo hàm một lần nữa ta được đạo hàm cấp hai: $y'' = (y')' = "
                        '12x^2 - 6 - 4\\sin 2x$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Cho hàm số $f(x) = e^{2x} + x^2$. Tính giá trị của $f''(0)$.",
            'answer': ['6'],
            'unit': None,
            'solution': "Ta có $f'(x) = 2e^{2x} + 2x \\Rightarrow f''(x) = 4e^{2x} + 2$. Thay $x = 0$ ta "
                        "được $f''(0) = 4e^0 + 2 = 6$.",
            'alt': None,
            'note': None}]}]
