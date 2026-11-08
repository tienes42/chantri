"""Dữ liệu bài học SGK Toán Lớp 8 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 8 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 8

LESSONS = [{'topic': 'l8-ch01-da-thuc',
  'context_title': 'Chương I: Đa thức',
  'context': 'Chương I · SGK Toán 8: Đơn thức nhiều biến, đa thức nhiều biến và các phép tính cộng, trừ, '
             'nhân, chia đa thức.',
  'title': 'Bài 1: Đơn thức',
  'icon': '🔣',
  'description': 'Khái niệm đơn thức nhiều biến, đơn thức thu gọn, bậc của đơn thức, đơn thức đồng dạng và '
                 'cộng, trừ đơn thức đồng dạng.',
  'requirements': ['Nhận biết được đơn thức nhiều biến, đơn thức thu gọn, hệ số, phần biến và bậc của một '
                   'đơn thức.',
                   'Nhận biết được các đơn thức đồng dạng và thực hiện được phép cộng, phép trừ các đơn thức '
                   'đồng dạng.',
                   'Vận dụng kiến thức của **Bài 1: Đơn thức** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': 'Đơn thức là biểu thức đại số chỉ gồm một số hoặc một biến, hoặc có dạng tích của những số '
                'và biến. Hai đơn thức đồng dạng là hai đơn thức với hệ số khác $0$ và có phần biến giống '
                'nhau.',
  'theory': '1. Đơn thức thu gọn và bậc của đơn thức:\n'
            '- Đơn thức thu gọn là đơn thức chỉ gồm một số, hoặc có dạng tích của một số với những biến, mỗi '
            'biến chỉ xuất hiện một lần và đã được nâng lên lũy thừa với số mũ nguyên dương.\n'
            '- Trong đơn thức thu gọn, phần số gọi là hệ số, phần còn lại gọi là phần biến. Tổng số mũ của '
            'các biến trong một đơn thức thu gọn với hệ số khác $0$ gọi là bậc của đơn thức đó.\n'
            '2. Đơn thức đồng dạng:\n'
            '- Hai đơn thức đồng dạng là hai đơn thức có hệ số khác $0$ và có phần biến giống nhau.\n'
            '- Muốn cộng (hay trừ) các đơn thức đồng dạng, ta cộng (hay trừ) các hệ số với nhau và giữ '
            'nguyên phần biến.',
  'formulas': [{'category': 'Đơn thức và đơn thức đồng dạng',
                'items': [{'name': 'Bậc của đơn thức $a x^m y^n z^p$ ($a \\neq 0$)',
                           'formula': '$\\text{Bậc} = m + n + p$'},
                          {'name': 'Cộng, trừ hai đơn thức đồng dạng',
                           'formula': '$a x^m y^n + b x^m y^n = (a + b)x^m y^n; \\quad a x^m y^n - b x^m y^n '
                                      '= (a - b)x^m y^n$'}]}],
  'example': 'Thu gọn đơn thức $A = (-2x^2y) \\cdot 3xy^3$, chỉ ra hệ số, phần biến và bậc của đơn thức thu '
             'gọn.',
  'example_answer': 'Ta có: $A = (-2 \\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$.\n'
                    'Hệ số là $-6$, phần biến là $x^3y^4$, bậc của đơn thức là $3 + 4 = 7$.',
  'real_life': 'Biểu thức tính thể tích của một khối hộp chữ nhật có đáy là hình vuông cạnh $x$ và chiều cao '
               '$2y$ là một đơn thức: $V = 2x^2y$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức nào sau đây là một đơn thức?',
            'options': ['$-5x^2y^3$', '$2x + 3y$', '$\\dfrac{x}{y^2}$', '$x^2 - y$'],
            'answer': 0,
            'solution': '$-5x^2y^3$ là tích của một số với các lũy thừa của biến nên là một đơn thức.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Bậc của đơn thức $4x^3y^2z$ là:',
            'options': ['$5$', '$6$', '$4$', '$3$'],
            'answer': 1,
            'solution': 'Tổng số mũ của các biến $x, y, z$ là $3 + 2 + 1 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Đơn thức**, quy tắc hoặc công thức nào sau đây xác định đúng **Bậc của đơn '
                 'thức $a x^m y^n z^p$ ($a \\neq 0$)**?',
            'options': ['$\\text{Bậc} = m - n + p$',
                        'Đảo ngược vế của quy tắc: $\\text{Bậc} = m + n + p$',
                        '$\\text{Bậc} = m + n + p$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\text{Bậc} = m + n + p$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Đơn thức, **Bậc của đơn thức $a x^m y^n z^p$ '
                        '($a \\neq 0$)** được xác định bởi: $\\text{Bậc} = m + n + p$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Đơn thức**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Cộng, '
                 'trừ hai đơn thức đồng dạng**?',
            'options': ['$a x^m y^n - b x^m y^n = (a + b)x^m y^n; \\quad a x^m y^n - b x^m y^n = (a - b)x^m '
                        'y^n$',
                        'Đảo ngược vế của quy tắc: $a x^m y^n + b x^m y^n = (a + b)x^m y^n; \\quad a x^m y^n '
                        '- b x^m y^n = (a - b)x^m y^n$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a x^m y^n + b x^m y^n = (a + '
                        'b)x^m y^n; \\quad a x^m y^n - b x^m y^n = (a - b)x^m y^n$',
                        '$a x^m y^n + b x^m y^n = (a + b)x^m y^n; \\quad a x^m y^n - b x^m y^n = (a - b)x^m '
                        'y^n$'],
            'answer': 3,
            'solution': 'Trong Bài 1: Đơn thức, **Cộng, trừ hai đơn thức đồng dạng** có công thức/quy tắc '
                        'là: $a x^m y^n + b x^m y^n = (a + b)x^m y^n; \\quad a x^m y^n - b x^m y^n = (a - '
                        'b)x^m y^n$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $5x^2y - 8x^2y + 2x^2y$ là:',
            'options': ['$-x^2y$', '$x^2y$', '$-3x^2y$', '$-x^6y^3$'],
            'answer': 0,
            'solution': 'Ta có $(5 - 8 + 2)x^2y = -1x^2y = -x^2y$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Đơn thức**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được đơn thức nhiều biến, đơn thức thu gọn, hệ số, phần biến và bậc của '
                        'một đơn thức. (với dấu ngược lại)',
                        'Nhận biết được đơn thức nhiều biến, đơn thức thu gọn, hệ số, phần biến và bậc của '
                        'một đơn thức.',
                        'Đảo ngược vế của quy tắc: Nhận biết được đơn thức nhiều biến, đơn thức thu gọn, hệ '
                        'số, phần biến và bậc của một đơn thức.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được đơn thức nhiều '
                        'biến, đơn thức thu gọn, hệ số, phần biến và bậc của một đơn thức.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Đơn thức: Nhận biết được đơn thức nhiều biến, đơn '
                        'thức thu gọn, hệ số, phần biến và bậc của một đơn thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai đơn thức $M = 3x^2y^3$ và $N = -7x^2y^3$. Xét các khẳng định sau:',
            'statements': ['Hai đơn thức $M$ và $N$ là hai đơn thức đồng dạng.',
                           'Bậc của đơn thức $M$ bằng $5$.',
                           'Tổng của hai đơn thức là $M + N = -4x^4y^6$.',
                           'Hiệu của hai đơn thức là $M - N = 10x^2y^3$.'],
            'answer': [True, True, False, True],
            'solution': 'a), b) Đúng (bậc là $2 + 3 = 5$). c) Sai vì khi cộng hai đơn thức đồng dạng ta giữ '
                        'nguyên phần biến: $M + N = -4x^2y^3$. d) Đúng vì $3 - (-7) = 10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 1: Đơn thức**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đơn thức nhiều biến, đơn '
                           'thức thu gọn, hệ số, phần biến và bậc của một đơn thức.',
                           'Trong **Bài 1: Đơn thức**, quy tắc/công thức **Bậc của đơn thức $a x^m y^n z^p$ '
                           '($a \\neq 0$)** được viết là: $\\text{Bậc} = m + n + p$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\text{Bậc} = m - n + p$ thì kết quả của '
                           '**Bậc của đơn thức $a x^m y^n z^p$ ($a \\neq 0$)** trong **Bài 1: Đơn thức** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Thu gọn đơn thức $A = (-2x^2y) \\cdot 3xy^3$, chỉ ra hệ số, '
                           'phần biến và bậc của đơn thức thu gọn.”, kết quả giải đúng là: Ta có: $A = (-2 '
                           '\\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$. Hệ số là $-6$, phần biến là '
                           '$x^3y^4$, bậc của đơn thức là $3 + 4 = 7$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Đơn thức. b) **Đúng** theo công thức '
                        '**Bậc của đơn thức $a x^m y^n z^p$ ($a \\neq 0$)** ($\\text{Bậc} = m + n + p$). c) '
                        '**Sai** vì công thức đúng của **Bậc của đơn thức $a x^m y^n z^p$ ($a \\neq 0$)** '
                        'phải là $\\text{Bậc} = m + n + p$ chứ không phải $\\text{Bậc} = m - n + p$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Đơn thức** để giải bài toán sau: Thu gọn đơn '
                 'thức $A = (-2x^2y) \\cdot 3xy^3$, chỉ ra hệ số, phần biến và bậc của đơn thức thu gọn. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có: $A = (-2 \\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$. Hệ số là $-6$, '
                        'phần biến là $x^3y^4$, bậc của đơn thức là $3 - 4 = 7$.',
                        'Ta có: $A = (-2 \\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$. Hệ số là $-6$, '
                        'phần biến là $x^3y^4$, bậc của đơn thức là $3 + 4 = 6$.',
                        'Ta có: $A = (-2 \\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$. Hệ số là $-6$, '
                        'phần biến là $x^3y^4$, bậc của đơn thức là $3 + 4 = 7$.',
                        'Ta có: $A = (-4 \\cdot 3)(x^2 \\cdot x)(y \\cdot y^3) = -6x^3y^4$. Hệ số là $-6$, '
                        'phần biến là $x^3y^4$, bậc của đơn thức là $3 + 4 = 7$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Đơn thức: Ta có: $A = (-2 \\cdot 3)(x^2 \\cdot x)(y '
                        '\\cdot y^3) = -6x^3y^4$.\n'
                        'Hệ số là $-6$, phần biến là $x^3y^4$, bậc của đơn thức là $3 + 4 = 7$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của đơn thức $P = 2x^2y^3$ tại $x = -2$ và $y = 1$.',
            'answer': ['8'],
            'unit': None,
            'solution': 'Thay $x = -2, y = 1$ vào $P$: $P = 2 \\cdot (-2)^2 \\cdot 1^3 = 2 \\cdot 4 \\cdot 1 '
                        '= 8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch01-da-thuc',
  'context_title': 'Chương I: Đa thức',
  'context': 'Chương I · SGK Toán 8: Đơn thức nhiều biến, đa thức nhiều biến và các phép tính cộng, trừ, '
             'nhân, chia đa thức.',
  'title': 'Bài 2: Đa thức',
  'icon': '📝',
  'description': 'Khái niệm đa thức nhiều biến, thu gọn đa thức, bậc của đa thức và tính giá trị của đa '
                 'thức.',
  'requirements': ['Nhận biết được đa thức nhiều biến và các hạng tử của đa thức.',
                   'Thu gọn được đa thức và xác định được bậc của đa thức đã thu gọn.',
                   'Tính được giá trị của đa thức khi biết giá trị của các biến.'],
  'definition': 'Đa thức là một tổng của những đơn thức; mỗi đơn thức trong tổng gọi là một hạng tử của đa '
                'thức đó. Bậc của một đa thức là bậc của hạng tử có bậc cao nhất trong dạng thu gọn của đa '
                'thức đó.',
  'theory': '1. Đa thức thu gọn: Đa thức thu gọn là đa thức không có hai hạng tử nào đồng dạng. Để thu gọn '
            'một đa thức, ta nhóm các hạng tử đồng dạng với nhau và cộng các hạng tử đồng dạng đó.\n'
            '2. Bậc của đa thức:\n'
            '- Khi tìm bậc của một đa thức, trước hết ta phải thu gọn đa thức đó.\n'
            '- Một số khác $0$ tùy ý được coi là một đa thức bậc $0$. Số $0$ (đa thức không) không có bậc.',
  'formulas': [{'category': 'Thu gọn và xác định bậc của đa thức',
                'items': [{'name': 'Định nghĩa bậc của đa thức $P$',
                           'formula': '$\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng thu gọn của '
                                      '} P\\}$'},
                          {'name': 'Giá trị của đa thức $P(x, y)$ tại $x = a, y = b$',
                           'formula': 'Thu gọn $P(x, y)$ rồi thay $x = a, y = b$ vào tính'}]}],
  'example': 'Thu gọn và tìm bậc của đa thức $P = 2x^2y - 3xy + 5x^2y^2 - 2x^2y + 4xy - 1$.',
  'example_answer': 'Nhóm các hạng tử đồng dạng: $P = (2x^2y - 2x^2y) + 5x^2y^2 + (-3xy + 4xy) - 1 = 5x^2y^2 '
                    '+ xy - 1$.\n'
                    'Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 0$. Vậy bậc của đa thức $P$ là '
                    '$4$.',
  'real_life': 'Biểu thức tính diện tích toàn phần của hình hộp chữ nhật có ba kích thước $x, y, z$ là đa '
               'thức bậc hai: $S_{tp} = 2xy + 2yz + 2zx$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bậc của đa thức $A = 3x^3y - 5xy^2 + 2x - 7$ là:',
            'options': ['$3$', '$4$', '$2$', '$7$'],
            'answer': 1,
            'solution': 'Hạng tử $3x^3y$ có bậc cao nhất là $3 + 1 = 4$, nên bậc của đa thức $A$ là $4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Thu gọn đa thức $B = 4x^2 - 3xy + x^2 + 3xy$ ta được:',
            'options': ['$5x^2 - 6xy$', '$3x^2$', '$5x^2$', '$5x^4$'],
            'answer': 2,
            'solution': 'Ta có $B = (4x^2 + x^2) + (-3xy + 3xy) = 5x^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Đa thức**, quy tắc hoặc công thức nào sau đây xác định đúng **Định nghĩa '
                 'bậc của đa thức $P$**?',
            'options': ['$\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng thu gọn của } P\\}$ (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng '
                        'thu gọn của } P\\}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\deg(P) = \\max\\{\\text{bậc '
                        'của các hạng tử trong dạng thu gọn của } P\\}$',
                        '$\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng thu gọn của } P\\}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Đa thức, **Định nghĩa bậc của đa thức $P$** '
                        'được xác định bởi: $\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng thu '
                        'gọn của } P\\}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Đa thức**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Giá trị '
                 'của đa thức $P(x, y)$ tại $x = a, y = b$**?',
            'options': ['Thu gọn $P(x, y)$ rồi thay $x = a, y = b$ vào tính',
                        'Thu gọn $P(x, y)$ rồi thay $x = a, y = b$ vào tính (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thu gọn $P(x, y)$ rồi thay $x = a, y = b$ vào tính',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thu gọn $P(x, y)$ rồi thay $x = '
                        'a, y = b$ vào tính'],
            'answer': 0,
            'solution': 'Trong Bài 2: Đa thức, **Giá trị của đa thức $P(x, y)$ tại $x = a, y = b$** có công '
                        'thức/quy tắc là: Thu gọn $P(x, y)$ rồi thay $x = a, y = b$ vào tính.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bậc của đa thức $P = x^4y - 2x^2y^2 + 3xy - x^4y + 1$ sau khi thu gọn là:',
            'options': ['$5$', '$4$', '$2$', '$0$'],
            'answer': 1,
            'solution': 'Thu gọn: $P = -2x^2y^2 + 3xy + 1$. Hạng tử $-2x^2y^2$ có bậc $2 + 2 = 4$ cao nhất '
                        'nên bậc của $P$ là $4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Đa thức**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được đa thức nhiều biến và các hạng tử của đa thức. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được đa thức nhiều biến và các hạng tử của đa '
                        'thức.',
                        'Nhận biết được đa thức nhiều biến và các hạng tử của đa thức.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được đa thức nhiều '
                        'biến và các hạng tử của đa thức.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Đa thức: Nhận biết được đa thức nhiều biến và các '
                        'hạng tử của đa thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đa thức $Q = 3x^2y - 2xy^2 + x^2y + 2xy^2 - 5$. Xét các khẳng định sau:',
            'statements': ['Dạng thu gọn của đa thức là $Q = 4x^2y - 5$.',
                           'Đa thức $Q$ sau khi thu gọn có $2$ hạng tử.',
                           'Bậc của đa thức $Q$ là $3$.',
                           'Tại $x = 1, y = 2$, giá trị của đa thức $Q$ bằng $11$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $Q = 4x^2y - 5$ có bậc là $2 + 1 = 3$. d) Sai vì tại $x = 1, y = '
                        '2$ thì $Q = 4 \\cdot 1^2 \\cdot 2 - 5 = 3 \\neq 11$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 2: Đa thức**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đa thức nhiều biến và các '
                           'hạng tử của đa thức.',
                           'Trong **Bài 2: Đa thức**, quy tắc/công thức **Định nghĩa bậc của đa thức $P$** '
                           'được viết là: $\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng thu gọn '
                           'của } P\\}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\deg(P) = \\max\\{\\text{bậc của các hạng '
                           'tử trong dạng thu gọn của } P\\}$ (với dấu ngược lại) thì kết quả của **Định '
                           'nghĩa bậc của đa thức $P$** trong **Bài 2: Đa thức** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Thu gọn và tìm bậc của đa thức $P = 2x^2y - 3xy + 5x^2y^2 - '
                           '2x^2y + 4xy - 1$.”, kết quả giải đúng là: Nhóm các hạng tử đồng dạng: $P = '
                           '(2x^2y - 2x^2y) + 5x^2y^2 + (-3xy + 4xy) - 1 = 5x^2y^2 + xy - 1$. Các hạng tử '
                           'của dạng thu gọn có bậc...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Đa thức. b) **Đúng** theo công thức '
                        '**Định nghĩa bậc của đa thức $P$** ($\\deg(P) = \\max\\{\\text{bậc của các hạng tử '
                        'trong dạng thu gọn của } P\\}$). c) **Sai** vì công thức đúng của **Định nghĩa bậc '
                        'của đa thức $P$** phải là $\\deg(P) = \\max\\{\\text{bậc của các hạng tử trong dạng '
                        'thu gọn của } P\\}$ chứ không phải $\\deg(P) = \\max\\{\\text{bậc của các hạng tử '
                        'trong dạng thu gọn của } P\\}$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Đa thức** để giải bài toán sau: Thu gọn và tìm '
                 'bậc của đa thức $P = 2x^2y - 3xy + 5x^2y^2 - 2x^2y + 4xy - 1$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Nhóm các hạng tử đồng dạng: $P = (2x^2y - 2x^2y) - 5x^2y^2 + (-3xy + 4xy) - 1 = '
                        '5x^2y^2 + xy - 1$. Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 0$...',
                        'Nhóm các hạng tử đồng dạng: $P = (2x^2y - 2x^2y) + 5x^2y^2 + (-3xy + 4xy) - 1 = '
                        '5x^2y^2 + xy - 1$. Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 1$...',
                        'Nhóm các hạng tử đồng dạng: $P = (2x^2y - 2x^2y) + 5x^2y^4 + (-3xy + 4xy) - 1 = '
                        '5x^2y^2 + xy - 1$. Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 0$...',
                        'Nhóm các hạng tử đồng dạng: $P = (2x^2y - 2x^2y) + 5x^2y^2 + (-3xy + 4xy) - 1 = '
                        '5x^2y^2 + xy - 1$. Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 0$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Đa thức: Nhóm các hạng tử đồng dạng: $P = (2x^2y - '
                        '2x^2y) + 5x^2y^2 + (-3xy + 4xy) - 1 = 5x^2y^2 + xy - 1$.\n'
                        'Các hạng tử của dạng thu gọn có bậc lần lượt là $4; 2; 0$. Vậy bậc của đa thức $P$ '
                        'là $4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của đa thức $M = 3x^2y - 2xy + 1$ tại $x = 2$ và $y = -1$.',
            'answer': ['-7'],
            'unit': None,
            'solution': 'Thay $x = 2, y = -1$ vào $M$: $M = 3 \\cdot 2^2 \\cdot (-1) - 2 \\cdot 2 \\cdot '
                        '(-1) + 1 = -12 + 4 + 1 = -7$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch01-da-thuc',
  'context_title': 'Chương I: Đa thức',
  'context': 'Chương I · SGK Toán 8: Đơn thức nhiều biến, đa thức nhiều biến và các phép tính cộng, trừ, '
             'nhân, chia đa thức.',
  'title': 'Bài 3: Phép cộng và phép trừ đa thức',
  'icon': '➕',
  'description': 'Quy tắc cộng, trừ hai đa thức nhiều biến và vận dụng tính chất của phép cộng đa thức.',
  'requirements': ['Thực hiện được phép cộng và phép trừ hai đa thức nhiều biến.',
                   'Vận dụng được tính chất giao hoán, kết hợp và quy tắc dấu ngoặc trong tính toán đa thức.',
                   'Vận dụng kiến thức của **Bài 3: Phép cộng và phép trừ đa thức** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Cộng (hay trừ) hai đa thức tức là thu gọn đa thức nhận được sau khi nối hai đa thức đã cho '
                'bởi dấu $+$ (hay dấu $-$) và áp dụng quy tắc bỏ dấu ngoặc.',
  'theory': 'Các bước cộng, trừ hai đa thức $A$ và $B$:\n'
            '1. Lập đa thức tổng $A + B$ hoặc hiệu $A - B$.\n'
            '2. Bỏ dấu ngoặc: Khi bỏ dấu ngoặc có dấu $+$ đằng trước thì giữ nguyên dấu của các hạng tử '
            'trong ngoặc; khi bỏ dấu ngoặc có dấu $-$ đằng trước thì phải đổi dấu tất cả các hạng tử trong '
            'ngoặc.\n'
            '3. Nhóm các hạng tử đồng dạng và thu gọn.',
  'formulas': [{'category': 'Quy tắc cộng, trừ đa thức nhiều biến',
                'items': [{'name': 'Bỏ dấu ngoặc trước có dấu cộng',
                           'formula': '$A + (B - C + D) = A + B - C + D$'},
                          {'name': 'Bỏ dấu ngoặc trước có dấu trừ',
                           'formula': '$A - (B - C + D) = A - B + C - D$'},
                          {'name': 'Tính chất giao hoán và kết hợp',
                           'formula': '$A + B = B + A; \\quad (A + B) + C = A + (B + C)$'}]}],
  'example': 'Cho hai đa thức $M = 3x^2 - 2xy + y^2$ và $N = x^2 + 2xy - 3y^2$. Tính $M + N$ và $M - N$.',
  'example_answer': '- $M + N = (3x^2 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$.\n'
                    '- $M - N = (3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$.',
  'real_life': 'Tính tổng diện tích các phòng hoặc hiệu thể tích giữa hai chi tiết máy có kích thước phụ '
               'thuộc vào hai biến $x, y$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $A = 2x + 3y$ và $B = x - 2y$. Tổng $A + B$ bằng:',
            'options': ['$3x + 5y$', '$x + y$', '$3x + y$', '$3x - y$'],
            'answer': 2,
            'solution': '$A + B = (2x + x) + (3y - 2y) = 3x + y$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $P = 4x^2 - y^2$ và $Q = x^2 - 3y^2$. Hiệu $P - Q$ bằng:',
            'options': ['$3x^2 - 4y^2$', '$5x^2 - 4y^2$', '$3x^2 - 2y^2$', '$3x^2 + 2y^2$'],
            'answer': 3,
            'solution': '$P - Q = (4x^2 - y^2) - (x^2 - 3y^2) = 4x^2 - y^2 - x^2 + 3y^2 = 3x^2 + 2y^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Phép cộng và phép trừ đa thức**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Bỏ dấu ngoặc trước có dấu cộng**?',
            'options': ['$A + (B - C + D) = A + B - C + D$',
                        '$A - (B - C + D) = A + B - C + D$',
                        'Đảo ngược vế của quy tắc: $A + (B - C + D) = A + B - C + D$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $A + (B - C + D) = A + B - C + '
                        'D$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Phép cộng và phép trừ đa thức, **Bỏ dấu ngoặc '
                        'trước có dấu cộng** được xác định bởi: $A + (B - C + D) = A + B - C + D$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Phép cộng và phép trừ đa thức**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Bỏ dấu ngoặc trước có dấu trừ**?',
            'options': ['$A - (B - C - D) = A - B + C - D$',
                        '$A - (B - C + D) = A - B + C - D$',
                        'Đảo ngược vế của quy tắc: $A - (B - C + D) = A - B + C - D$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $A - (B - C + D) = A - B + C - '
                        'D$'],
            'answer': 1,
            'solution': 'Trong Bài 3: Phép cộng và phép trừ đa thức, **Bỏ dấu ngoặc trước có dấu trừ** có '
                        'công thức/quy tắc là: $A - (B - C + D) = A - B + C - D$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đa thức $C$ thỏa mãn $C + (2x^2y - 3xy) = 5x^2y + xy - 1$ là:',
            'options': ['$7x^2y - 2xy - 1$', '$3x^2y - 2xy - 1$', '$3x^2y + 4xy - 1$', '$3x^2y + 4xy + 1$'],
            'answer': 2,
            'solution': '$C = (5x^2y + xy - 1) - (2x^2y - 3xy) = 3x^2y + 4xy - 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Phép cộng và phép trừ đa thức**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Thực hiện được phép cộng và phép trừ hai đa thức nhiều biến. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép cộng và phép trừ hai đa thức nhiều '
                        'biến.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép cộng và '
                        'phép trừ hai đa thức nhiều biến.',
                        'Thực hiện được phép cộng và phép trừ hai đa thức nhiều biến.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Phép cộng và phép trừ đa thức: Thực hiện được phép '
                        'cộng và phép trừ hai đa thức nhiều biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai đa thức $A = x^2 - 2xy + 3y^2$ và $B = -x^2 + 2xy + y^2$. Xét các khẳng định sau:',
            'statements': ['Tổng của hai đa thức là $A + B = 4y^2$.',
                           'Hiệu của hai đa thức là $A - B = 2x^2 - 4xy + 2y^2$.',
                           'Giá trị của đa thức tổng $A + B$ luôn không âm với mọi giá trị thực của $x, y$.',
                           'Tại $x = 5, y = -1$, giá trị của $A + B$ phụ thuộc vào giá trị của $x$ và bằng '
                           '$25$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b) Đúng. c) Đúng vì $A + B = 4y^2 \\ge 0$ với mọi $x, y \\in \\mathbb{R}$. d) '
                        'Sai vì $A + B = 4y^2$ không phụ thuộc vào $x$ và tại $y = -1$ thì $A + B = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 3: Phép cộng và phép trừ đa '
                 'thức**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép cộng và phép trừ hai '
                           'đa thức nhiều biến.',
                           'Trong **Bài 3: Phép cộng và phép trừ đa thức**, quy tắc/công thức **Bỏ dấu ngoặc '
                           'trước có dấu cộng** được viết là: $A + (B - C + D) = A + B - C + D$.',
                           'Nếu áp dụng sai dấu/phép tính thành $A - (B - C + D) = A + B - C + D$ thì kết '
                           'quả của **Bỏ dấu ngoặc trước có dấu cộng** trong **Bài 3: Phép cộng và phép trừ '
                           'đa thức** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho hai đa thức $M = 3x^2 - 2xy + y^2$ và $N = x^2 + 2xy - '
                           '3y^2$. Tính $M + N$ và $M - N$.”, kết quả giải đúng là: - $M + N = (3x^2 + x^2) '
                           '+ (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$. - $M - N = (3x^2 - x^2) + (-2xy - '
                           '2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Phép cộng và phép trừ đa thức. b) '
                        '**Đúng** theo công thức **Bỏ dấu ngoặc trước có dấu cộng** ($A + (B - C + D) = A + '
                        'B - C + D$). c) **Sai** vì công thức đúng của **Bỏ dấu ngoặc trước có dấu cộng** '
                        'phải là $A + (B - C + D) = A + B - C + D$ chứ không phải $A - (B - C + D) = A + B - '
                        'C + D$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Phép cộng và phép trừ đa thức** để giải bài toán '
                 'sau: Cho hai đa thức $M = 3x^2 - 2xy + y^2$ và $N = x^2 + 2xy - 3y^2$. Tính $M + N$ và $M '
                 '- N$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- $M + N = (3x^2 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$. - $M - N = '
                        '(3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$.',
                        '- $M - N = (3x^2 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$. - $M - N = '
                        '(3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$.',
                        '- $M + N = (3x^2 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$. - $M - N = '
                        '(3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^1$.',
                        '- $M + N = (3x^4 + x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$. - $M - N = '
                        '(3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Phép cộng và phép trừ đa thức: - $M + N = (3x^2 + '
                        'x^2) + (-2xy + 2xy) + (y^2 - 3y^2) = 4x^2 - 2y^2$.\n'
                        '- $M - N = (3x^2 - x^2) + (-2xy - 2xy) + (y^2 + 3y^2) = 2x^2 - 4xy + 4y^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $M = 5x^2y + 3xy - 2$ và $N = 5x^2y + xy + 4$. Tính giá trị của đa thức $P = M - N$ '
                 'tại $x = 2$ và $y = 3$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Ta có $P = M - N = 2xy - 6$. Tại $x = 2, y = 3$ thì $P = 2 \\cdot 2 \\cdot 3 - 6 = '
                        '12 - 6 = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch01-da-thuc',
  'context_title': 'Chương I: Đa thức',
  'context': 'Chương I · SGK Toán 8: Đơn thức nhiều biến, đa thức nhiều biến và các phép tính cộng, trừ, '
             'nhân, chia đa thức.',
  'title': 'Bài 4: Phép nhân đa thức',
  'icon': '✖️',
  'description': 'Quy tắc nhân hai đơn thức nhiều biến, nhân đơn thức với đa thức và nhân hai đa thức nhiều '
                 'biến.',
  'requirements': ['Thực hiện được phép nhân hai đơn thức và nhân một đơn thức với một đa thức nhiều biến.',
                   'Thực hiện được phép nhân hai đa thức nhiều biến và rút gọn biểu thức đại số.',
                   'Vận dụng kiến thức của **Bài 4: Phép nhân đa thức** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': 'Muốn nhân hai đơn thức, ta nhân hai hệ số với nhau và nhân hai phần biến với nhau. Muốn '
                'nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng '
                'các tích với nhau. Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa thức '
                'này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.',
  'theory': '1. Nhân đơn thức với đa thức: $A \\cdot (B + C - D) = AB + AC - AD$.\n'
            '2. Nhân hai đa thức: $(A + B)(C + D) = AC + AD + BC + BD$. Sau khi nhân, ta thu gọn các hạng tử '
            'đồng dạng (nếu có).\n'
            '3. Tính chất: Phép nhân đa thức có tính chất giao hoán $A \\cdot B = B \\cdot A$, kết hợp $(A '
            '\\cdot B) \\cdot C = A \\cdot (B \\cdot C)$ và phân phối đối với phép cộng.',
  'formulas': [{'category': 'Công thức nhân đơn thức và đa thức nhiều biến',
                'items': [{'name': 'Nhân hai đơn thức',
                           'formula': '$(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$'},
                          {'name': 'Nhân đơn thức với đa thức', 'formula': '$A(B + C) = AB + AC$'},
                          {'name': 'Nhân đa thức với đa thức',
                           'formula': '$(A + B)(C + D) = AC + AD + BC + BD$'}]}],
  'example': 'Thực hiện phép nhân và rút gọn: $P = (x + 2y)(2x - y) - 2x^2$.',
  'example_answer': 'Ta có $(x + 2y)(2x - y) = 2x^2 - xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$.\n'
                    'Do đó $P = 2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.',
  'real_life': 'Tính diện tích mặt sàn khi mở rộng cả chiều dài và chiều rộng của căn phòng theo hai hướng '
               'khác nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tích của hai đơn thức $(-2x^2y)$ và $(5xy^3)$ là:',
            'options': ['$-10x^2y^3$', '$10x^3y^4$', '$3x^3y^4$', '$-10x^3y^4$'],
            'answer': 3,
            'solution': '$(-2x^2y) \\cdot (5xy^3) = (-2 \\cdot 5)(x^2 \\cdot x)(y \\cdot y^3) = -10x^3y^4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $3xy(2x - y)$ là:',
            'options': ['$6x^2y - 3xy^2$', '$6xy - 3xy^2$', '$6x^2y - y$', '$5x^2y - 3xy^2$'],
            'answer': 0,
            'solution': '$3xy(2x - y) = 3xy \\cdot 2x - 3xy \\cdot y = 6x^2y - 3xy^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Phép nhân đa thức**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Nhân hai đơn thức**?',
            'options': ['$(ax^m y^n) : (bx^p y^q) = (ab) x^{m+p} y^{n+q}$',
                        '$(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$',
                        'Đảo ngược vế của quy tắc: $(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $(ax^m y^n) \\cdot (bx^p y^q) = '
                        '(ab) x^{m+p} y^{n+q}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: Phép nhân đa thức, **Nhân hai đơn thức** được '
                        'xác định bởi: $(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Phép nhân đa thức**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Nhân đơn thức với đa thức**?',
            'options': ['$A(B - C) = AB + AC$',
                        'Đảo ngược vế của quy tắc: $A(B + C) = AB + AC$',
                        '$A(B + C) = AB + AC$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $A(B + C) = AB + AC$'],
            'answer': 2,
            'solution': 'Trong Bài 4: Phép nhân đa thức, **Nhân đơn thức với đa thức** có công thức/quy tắc '
                        'là: $A(B + C) = AB + AC$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khai triển và rút gọn tích $(x - y)(x + 2y)$ ta được:',
            'options': ['$x^2 - xy - 2y^2$', '$x^2 + 3xy - 2y^2$', '$x^2 - 2y^2$', '$x^2 + xy - 2y^2$'],
            'answer': 3,
            'solution': '$(x - y)(x + 2y) = x^2 + 2xy - xy - 2y^2 = x^2 + xy - 2y^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: Phép nhân đa thức**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Thực hiện được phép nhân hai đơn thức và nhân một đơn thức với một đa thức nhiều '
                        'biến.',
                        'Thực hiện được phép nhân hai đơn thức và nhân một đơn thức với một đa thức nhiều '
                        'biến. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép nhân hai đơn thức và nhân một đơn '
                        'thức với một đa thức nhiều biến.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép nhân hai '
                        'đơn thức và nhân một đơn thức với một đa thức nhiều biến.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 4: Phép nhân đa thức: Thực hiện được phép nhân hai '
                        'đơn thức và nhân một đơn thức với một đa thức nhiều biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $A = (x + y)(x^2 - xy + y^2)$. Xét các khẳng định sau:',
            'statements': ['Khi nhân hai đa thức chưa thu gọn, ta nhận được $6$ hạng tử trước khi rút gọn.',
                           'Các hạng tử $-x^2y$ và $+x^2y$ triệt tiêu nhau, các hạng tử $xy^2$ và $-xy^2$ '
                           'triệt tiêu nhau.',
                           'Sau khi thu gọn, ta được $A = x^3 + y^3$.',
                           'Tại $x = 2, y = -1$, giá trị của biểu thức $A$ bằng $9$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $(x + y)(x^2 - xy + y^2) = x^3 + y^3$. d) Sai vì tại $x = 2, y = '
                        '-1$ thì $A = 2^3 + (-1)^3 = 8 - 1 = 7 \\neq 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 4: Phép nhân đa thức**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép nhân hai đơn thức và '
                           'nhân một đơn thức với một đa thức nhiều biến.',
                           'Trong **Bài 4: Phép nhân đa thức**, quy tắc/công thức **Nhân hai đơn thức** được '
                           'viết là: $(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $(ax^m y^n) : (bx^p y^q) = (ab) x^{m+p} '
                           'y^{n+q}$ thì kết quả của **Nhân hai đơn thức** trong **Bài 4: Phép nhân đa '
                           'thức** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Thực hiện phép nhân và rút gọn: $P = (x + 2y)(2x - y) - '
                           '2x^2$.”, kết quả giải đúng là: Ta có $(x + 2y)(2x - y) = 2x^2 - xy + 4xy - 2y^2 '
                           '= 2x^2 + 3xy - 2y^2$. Do đó $P = 2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Phép nhân đa thức. b) **Đúng** theo '
                        'công thức **Nhân hai đơn thức** ($(ax^m y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} '
                        'y^{n+q}$). c) **Sai** vì công thức đúng của **Nhân hai đơn thức** phải là $(ax^m '
                        'y^n) \\cdot (bx^p y^q) = (ab) x^{m+p} y^{n+q}$ chứ không phải $(ax^m y^n) : (bx^p '
                        'y^q) = (ab) x^{m+p} y^{n+q}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: Phép nhân đa thức** để giải bài toán sau: Thực '
                 'hiện phép nhân và rút gọn: $P = (x + 2y)(2x - y) - 2x^2$. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có $(x - 2y)(2x - y) = 2x^2 - xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$. Do đó $P = '
                        '2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.',
                        'Ta có $(x + 2y)(2x - y) = 2x^2 - xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$. Do đó $P = '
                        '2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.',
                        'Ta có $(x + 2y)(2x - y) = 2x^2 - xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$. Do đó $P = '
                        '2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^1$.',
                        'Ta có $(x + 2y)(2x - y) = 2x^4 - xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$. Do đó $P = '
                        '2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Phép nhân đa thức: Ta có $(x + 2y)(2x - y) = 2x^2 - '
                        'xy + 4xy - 2y^2 = 2x^2 + 3xy - 2y^2$.\n'
                        'Do đó $P = 2x^2 + 3xy - 2y^2 - 2x^2 = 3xy - 2y^2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn biểu thức $M = x(x - y) + y(x + y)$ rồi tính giá trị của $M$ tại $x = 3$ và $y = '
                 '4$.',
            'answer': ['25'],
            'unit': None,
            'solution': 'Ta có $M = x^2 - xy + xy + y^2 = x^2 + y^2$. Tại $x = 3, y = 4$ thì $M = 3^2 + 4^2 '
                        '= 9 + 16 = 25$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch01-da-thuc',
  'context_title': 'Chương I: Đa thức',
  'context': 'Chương I · SGK Toán 8: Đơn thức nhiều biến, đa thức nhiều biến và các phép tính cộng, trừ, '
             'nhân, chia đa thức.',
  'title': 'Bài 5: Phép chia đa thức cho đơn thức',
  'icon': '➗',
  'description': 'Điều kiện chia hết và quy tắc chia đơn thức cho đơn thức, chia đa thức cho đơn thức.',
  'requirements': ['Nhận biết được khi nào một đơn thức (hoặc đa thức) chia hết cho một đơn thức khác $0$.',
                   'Thực hiện được phép chia đơn thức cho đơn thức và phép chia đa thức cho đơn thức.',
                   'Vận dụng kiến thức của **Bài 5: Phép chia đa thức cho đơn thức** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Đơn thức $A$ chia hết cho đơn thức $B$ ($B \\neq 0$) khi mỗi biến của $B$ đều là biến của '
                '$A$ với số mũ không lớn hơn số mũ của nó trong $A$. Đa thức $A$ chia hết cho đơn thức $B$ '
                'nếu mọi hạng tử của $A$ đều chia hết cho $B$.',
  'theory': '1. Chia đơn thức cho đơn thức: Muốn chia đơn thức $A$ cho đơn thức $B$ (trường hợp chia hết), '
            'ta chia hệ số của đơn thức $A$ cho hệ số của đơn thức $B$, chia lũy thừa của từng biến trong '
            '$A$ cho lũy thừa của cùng biến đó trong $B$ rồi nhân các kết quả với nhau.\n'
            '2. Chia đa thức cho đơn thức: Muốn chia đa thức $A$ cho đơn thức $B$ (trường hợp chia hết), ta '
            'chia từng hạng tử của $A$ cho $B$ rồi cộng các kết quả với nhau.',
  'formulas': [{'category': 'Quy tắc chia đơn thức và đa thức cho đơn thức',
                'items': [{'name': 'Chia hai đơn thức',
                           'formula': '$(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b '
                                      '\\neq 0, m \\ge p, n \\ge q)$'},
                          {'name': 'Chia đa thức cho đơn thức',
                           'formula': '$(A + B - C) : D = (A : D) + (B : D) - (C : D)$'}]}],
  'example': 'Thực hiện phép chia: $(15x^3y^2 - 6x^2y^3 + 3x^2y^2) : (3x^2y^2)$.',
  'example_answer': 'Chia từng hạng tử của đa thức cho $3x^2y^2$:\n'
                    '$(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : 3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + 1$.',
  'real_life': 'Tính chiều cao của hình hộp chữ nhật khi biết đa thức biểu thị thể tích và đơn thức biểu thị '
               'diện tích mặt đáy.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép chia đơn thức $(18x^4y^3) : (6x^2y)$ là:',
            'options': ['$3x^2y^2$', '$3x^2y^3$', '$12x^2y^2$', '$3x^6y^4$'],
            'answer': 0,
            'solution': '$(18x^4y^3) : (6x^2y) = (18 : 6) \\cdot x^{4-2} \\cdot y^{3-1} = 3x^2y^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn thức $10x^3y^2$ KHÔNG chia hết cho đơn thức nào sau đây?',
            'options': ['$2x^3y$', '$5x^2y^3$', '$-5xy^2$', '$10x^2y^2$'],
            'answer': 1,
            'solution': 'Số mũ của biến $y$ trong $5x^2y^3$ là $3$, lớn hơn số mũ của $y$ trong $10x^3y^2$ '
                        '(là $2$), nên không chia hết.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Phép chia đa thức cho đơn thức**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Chia hai đơn thức**?',
            'options': ['$(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\le '
                        'p, n \\ge q)$',
                        '$(ax^m y^n) : (bx^p y^q) = \\dfrac{b}{a} x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\ge '
                        'p, n \\ge q)$',
                        '$(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\ge '
                        'p, n \\ge q)$',
                        '$(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 2, m \\ge '
                        'p, n \\ge q)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Phép chia đa thức cho đơn thức, **Chia hai đơn '
                        'thức** được xác định bởi: $(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} '
                        '\\quad (b \\neq 0, m \\ge p, n \\ge q)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Phép chia đa thức cho đơn thức**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Chia đa thức cho đơn thức**?',
            'options': ['$(A - B - C) : D = (A : D) + (B : D) - (C : D)$',
                        'Đảo ngược vế của quy tắc: $(A + B - C) : D = (A : D) + (B : D) - (C : D)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $(A + B - C) : D = (A : D) + (B '
                        ': D) - (C : D)$',
                        '$(A + B - C) : D = (A : D) + (B : D) - (C : D)$'],
            'answer': 3,
            'solution': 'Trong Bài 5: Phép chia đa thức cho đơn thức, **Chia đa thức cho đơn thức** có công '
                        'thức/quy tắc là: $(A + B - C) : D = (A : D) + (B : D) - (C : D)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thương của phép chia $(8x^3y - 12x^2y^2 + 4xy) : (4xy)$ là:',
            'options': ['$2x^2 - 3xy + 1$', '$2x^2 - 3xy$', '$2x^2y - 3xy + 1$', '$4x^2 - 8xy + 1$'],
            'answer': 0,
            'solution': 'Chia từng hạng tử cho $4xy$ ta được $2x^2 - 3xy + 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Phép chia đa thức cho đơn thức**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được khi nào một đơn thức (hoặc đa thức) không chia hết cho một đơn thức '
                        'khác $0$.',
                        'Nhận biết được khi nào một đơn thức (hoặc đa thức) chia hết cho một đơn thức khác '
                        '$0$.',
                        'Nhận biết được khi nào một đơn thức (hoặc đa thức) chia hết cho một đơn thức khác '
                        '$1$.',
                        'Nhận biết được khi nào một đơn thức (hoặc đa thức) chia hết cho một đơn thức khác '
                        '$2$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Phép chia đa thức cho đơn thức: Nhận biết được khi '
                        'nào một đơn thức (hoặc đa thức) chia hết cho một đơn thức khác $0$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đa thức $A = 9x^4y^2 - 6x^3y^3 + 3x^2y^2$ và đơn thức $B = 3x^2y^2$. Xét các khẳng '
                 'định sau:',
            'statements': ['Mọi hạng tử của đa thức $A$ đều chia hết cho đơn thức $B$.',
                           'Thương của phép chia $A : B$ là $Q = 3x^2 - 2xy + 1$.',
                           'Đa thức thương $Q$ có bậc là $2$.',
                           'Đa thức $A$ cũng chia hết cho đơn thức $C = 3x^3y^2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì hạng tử $3x^2y^2$ có số mũ của $x$ là $2 < 3$ nên không '
                        'chia hết cho $3x^3y^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 5: Phép chia đa thức cho '
                 'đơn thức**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được khi nào một đơn thức '
                           '(hoặc đa thức) chia hết cho một đơn thức khác $0$.',
                           'Trong **Bài 5: Phép chia đa thức cho đơn thức**, quy tắc/công thức **Chia hai '
                           'đơn thức** được viết là: $(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} '
                           'y^{n-q} \\quad (b \\neq 0, m \\ge p, n \\ge q)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} '
                           'x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\le p, n \\ge q)$ thì kết quả của **Chia '
                           'hai đơn thức** trong **Bài 5: Phép chia đa thức cho đơn thức** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Thực hiện phép chia: $(15x^3y^2 - 6x^2y^3 + 3x^2y^2) : '
                           '(3x^2y^2)$.”, kết quả giải đúng là: Chia từng hạng tử của đa thức cho $3x^2y^2$: '
                           '$(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : 3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + '
                           '1$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Phép chia đa thức cho đơn thức. b) '
                        '**Đúng** theo công thức **Chia hai đơn thức** ($(ax^m y^n) : (bx^p y^q) = '
                        '\\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\ge p, n \\ge q)$). c) **Sai** '
                        'vì công thức đúng của **Chia hai đơn thức** phải là $(ax^m y^n) : (bx^p y^q) = '
                        '\\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 0, m \\ge p, n \\ge q)$ chứ không '
                        'phải $(ax^m y^n) : (bx^p y^q) = \\dfrac{a}{b} x^{m-p} y^{n-q} \\quad (b \\neq 0, m '
                        '\\le p, n \\ge q)$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Phép chia đa thức cho đơn thức** để giải bài '
                 'toán sau: Thực hiện phép chia: $(15x^3y^2 - 6x^2y^3 + 3x^2y^2) : (3x^2y^2)$. Cách giải và '
                 'kết quả nào dưới đây là **đúng**?',
            'options': ['Chia từng hạng tử của đa thức cho $3x^2y^2$: $(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : '
                        '3x^2y^2) - (3x^2y^2 : 3x^2y^2) = 5x - 2y + 1$.',
                        'Chia từng hạng tử của đa thức cho $3x^2y^2$: $(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : '
                        '3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + 2$.',
                        'Chia từng hạng tử của đa thức cho $3x^2y^2$: $(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : '
                        '3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + 1$.',
                        'Chia từng hạng tử của đa thức cho $3x^2y^4$: $(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : '
                        '3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + 1$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Phép chia đa thức cho đơn thức: Chia từng hạng tử của '
                        'đa thức cho $3x^2y^2$:\n'
                        '$(15x^3y^2 : 3x^2y^2) - (6x^2y^3 : 3x^2y^2) + (3x^2y^2 : 3x^2y^2) = 5x - 2y + 1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = (12x^3y^2 - 8x^2y^3) : (4x^2y^2)$ tại $x = 5$ và $y = 2$.',
            'answer': ['11'],
            'unit': None,
            'solution': 'Rút gọn $P = 3x - 2y$. Thay $x = 5, y = 2$ ta được $P = 3 \\cdot 5 - 2 \\cdot 2 = '
                        '15 - 4 = 11$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch02-hang-dang-thuc',
  'context_title': 'Chương II: Hằng đẳng thức đáng nhớ và ứng dụng',
  'context': 'Chương II · SGK Toán 8: Bảy hằng đẳng thức đáng nhớ và các phương pháp phân tích đa thức thành '
             'nhân tử.',
  'title': 'Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu',
  'icon': '✨',
  'description': 'Khái niệm hằng đẳng thức và ba hằng đẳng thức đáng nhớ: hiệu hai bình phương, bình phương '
                 'của một tổng, bình phương của một hiệu.',
  'requirements': ['Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức).',
                   'Mô tả và vận dụng được ba hằng đẳng thức: hiệu hai bình phương, bình phương của một '
                   'tổng, bình phương của một hiệu để khai triển, rút gọn và tính nhanh.',
                   'Vận dụng kiến thức của **Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một '
                   'hiệu** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Hằng đẳng thức là đẳng thức mà hai vế luôn cùng nhận một giá trị khi thay các chữ trong '
                'đẳng thức bằng các số tùy ý. Ba hằng đẳng thức bậc hai cơ bản là: $A^2 - B^2 = (A - B)(A + '
                'B)$; $(A + B)^2 = A^2 + 2AB + B^2$; $(A - B)^2 = A^2 - 2AB + B^2$.',
  'theory': 'Với $A, B$ là hai biểu thức tùy ý, ta có:\n'
            '1. Hiệu hai bình phương: $A^2 - B^2 = (A - B)(A + B)$.\n'
            '2. Bình phương của một tổng: $(A + B)^2 = A^2 + 2AB + B^2$.\n'
            '3. Bình phương của một hiệu: $(A - B)^2 = A^2 - 2AB + B^2$.',
  'formulas': [{'category': 'Ba hằng đẳng thức bậc hai',
                'items': [{'name': 'Hiệu hai bình phương', 'formula': '$A^2 - B^2 = (A - B)(A + B)$'},
                          {'name': 'Bình phương của một tổng', 'formula': '$(A + B)^2 = A^2 + 2AB + B^2$'},
                          {'name': 'Bình phương của một hiệu', 'formula': '$(A - B)^2 = A^2 - 2AB + B^2$'}]}],
  'example': 'Tính nhanh: a) $101^2$; b) $64^2 - 36^2$.',
  'example_answer': 'a) $101^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + 200 + 1 = '
                    '10201$.\n'
                    'b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2800$.',
  'real_life': 'Tính nhẩm nhanh diện tích phần lối đi bao quanh một bồn hoa hình vuông hoặc tính nhẩm tích '
               'hai số gần số tròn chục (như $49 \\cdot 51 = 50^2 - 1^2 = 2499$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khai triển hằng đẳng thức $(x + 3)^2$ ta được:',
            'options': ['$x^2 + 3x + 9$', '$x^2 + 6x + 9$', '$x^2 + 9$', '$x^2 - 6x + 9$'],
            'answer': 1,
            'solution': '$(x + 3)^2 = x^2 + 2 \\cdot x \\cdot 3 + 3^2 = x^2 + 6x + 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức $x^2 - 25$ viết dưới dạng tích là:',
            'options': ['$(x - 5)^2$', '$(x - 25)(x + 25)$', '$(x - 5)(x + 5)$', '$(x + 5)^2$'],
            'answer': 2,
            'solution': '$x^2 - 25 = x^2 - 5^2 = (x - 5)(x + 5)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Hiệu hai bình phương**?',
            'options': ['$A^2 - B^2 = (A - B)(A - B)$',
                        '$A^2 - B^1 = (A - B)(A + B)$',
                        '$A^4 - B^2 = (A - B)(A + B)$',
                        '$A^2 - B^2 = (A - B)(A + B)$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 6: Hiệu hai bình phương. Bình phương của một tổng '
                        'hay một hiệu, **Hiệu hai bình phương** được xác định bởi: $A^2 - B^2 = (A - B)(A + '
                        'B)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Bình phương của một tổng**?',
            'options': ['$(A + B)^2 = A^2 + 2AB + B^2$',
                        '$(A - B)^2 = A^2 + 2AB + B^2$',
                        '$(A + B)^2 = A^2 + 2AB + B^1$',
                        '$(A + B)^4 = A^2 + 2AB + B^2$'],
            'answer': 0,
            'solution': 'Trong Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu, **Bình '
                        'phương của một tổng** có công thức/quy tắc là: $(A + B)^2 = A^2 + 2AB + B^2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biểu thức $4x^2 - 12xy + 9y^2$ viết dưới dạng bình phương của một hiệu là:',
            'options': ['$(4x - 9y)^2$', '$(2x - 3y)^2$', '$(2x + 3y)^2$', '$(2x - 9y)^2$'],
            'answer': 1,
            'solution': '$4x^2 - 12xy + 9y^2 = (2x)^2 - 2 \\cdot (2x) \\cdot (3y) + (3y)^2 = (2x - 3y)^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một '
                 'hiệu**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức).',
                        'Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được khái niệm đồng '
                        'nhất thức (hằng đẳng thức).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay '
                        'một hiệu: Nhận biết được khái niệm đồng nhất thức (hằng đẳng thức).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau với mọi $x, y \\in \\mathbb{R}$:',
            'statements': ['$(x - 2y)^2 = x^2 - 4xy + 4y^2$.',
                           '$(3x - 1)(3x + 1) = 9x^2 - 1$.',
                           '$(x - y)^2 = -(y - x)^2$.',
                           'Giá trị của biểu thức $x^2 + 8x + 16$ tại $x = 96$ bằng $10000$.'],
            'answer': [True, True, False, True],
            'solution': 'a), b) Đúng. c) Sai vì $(x - y)^2 = (y - x)^2$. d) Đúng vì $x^2 + 8x + 16 = (x + '
                        '4)^2 = (96 + 4)^2 = 100^2 = 10000$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 6: Hiệu hai bình phương. '
                 'Bình phương của một tổng hay một hiệu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được khái niệm đồng nhất thức '
                           '(hằng đẳng thức).',
                           'Trong **Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay một hiệu**, '
                           'quy tắc/công thức **Hiệu hai bình phương** được viết là: $A^2 - B^2 = (A - B)(A '
                           '+ B)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $A^2 - B^2 = (A - B)(A - B)$ thì kết quả của '
                           '**Hiệu hai bình phương** trong **Bài 6: Hiệu hai bình phương. Bình phương của '
                           'một tổng hay một hiệu** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính nhanh: a) $101^2$; b) $64^2 - 36^2$.”, kết quả giải '
                           'đúng là: a) $101^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + '
                           '200 + 1 = 10201$. b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = '
                           '2800$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Hiệu hai bình phương. Bình phương của '
                        'một tổng hay một hiệu. b) **Đúng** theo công thức **Hiệu hai bình phương** ($A^2 - '
                        'B^2 = (A - B)(A + B)$). c) **Sai** vì công thức đúng của **Hiệu hai bình phương** '
                        'phải là $A^2 - B^2 = (A - B)(A + B)$ chứ không phải $A^2 - B^2 = (A - B)(A - B)$. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 6: Hiệu hai bình phương. Bình phương của một tổng '
                 'hay một hiệu** để giải bài toán sau: Tính nhanh: a) $101^2$; b) $64^2 - 36^2$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $101^2 = (100 - 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + 200 + 1 = '
                        '10201$. b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2800$.',
                        'a) $101^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + 200 + 1 = '
                        '10201$. b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2799$.',
                        'a) $103^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + 200 + 1 = '
                        '10201$. b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2800$.',
                        'a) $101^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + 200 + 1 = '
                        '10201$. b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2800$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Hiệu hai bình phương. Bình phương của một tổng hay '
                        'một hiệu: a) $101^2 = (100 + 1)^2 = 100^2 + 2 \\cdot 100 \\cdot 1 + 1^2 = 10000 + '
                        '200 + 1 = 10201$.\n'
                        'b) $64^2 - 36^2 = (64 - 36)(64 + 36) = 28 \\cdot 100 = 2800$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $A = 85^2 - 15^2$.',
            'answer': ['7000'],
            'unit': None,
            'solution': 'Ta có $A = (85 - 15)(85 + 15) = 70 \\cdot 100 = 7000$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch02-hang-dang-thuc',
  'context_title': 'Chương II: Hằng đẳng thức đáng nhớ và ứng dụng',
  'context': 'Chương II · SGK Toán 8: Bảy hằng đẳng thức đáng nhớ và các phương pháp phân tích đa thức thành '
             'nhân tử.',
  'title': 'Bài 7: Lập phương của một tổng. Lập phương của một hiệu',
  'icon': '🧊',
  'description': 'Hai hằng đẳng thức lập phương của một tổng và lập phương của một hiệu.',
  'requirements': ['Mô tả được hằng đẳng thức lập phương của một tổng và lập phương của một hiệu.',
                   'Vận dụng hai hằng đẳng thức này để khai triển hoặc viết biểu thức dưới dạng lập phương '
                   'và tính nhanh giá trị biểu thức.',
                   'Vận dụng kiến thức của **Bài 7: Lập phương của một tổng. Lập phương của một hiệu** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Với hai biểu thức $A, B$ tùy ý, ta có: $(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$ và $(A - '
                'B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$.',
  'theory': '1. Lập phương của một tổng: $(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$.\n'
            '2. Lập phương của một hiệu: $(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$ (lưu ý các dấu đan xen $+, '
            '-, +, -$).',
  'formulas': [{'category': 'Lập phương của một tổng hay một hiệu',
                'items': [{'name': 'Lập phương của một tổng',
                           'formula': '$(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$'},
                          {'name': 'Lập phương của một hiệu',
                           'formula': '$(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$'}]}],
  'example': 'Viết biểu thức $P = x^3 - 6x^2 + 12x - 8$ dưới dạng lập phương của một hiệu và tính giá trị '
             'của $P$ tại $x = 12$.',
  'example_answer': 'Ta có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$.\n'
                    'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$.',
  'real_life': 'Tính phần thể tích tăng thêm của một khối lập phương cạnh $a$ khi tăng mỗi cạnh thêm một '
               'đoạn bằng $b$: $\\Delta V = (a + b)^3 - a^3 = 3a^2b + 3ab^2 + b^3$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khai triển hằng đẳng thức $(x + 1)^3$ ta được:',
            'options': ['$x^3 + x^2 + x + 1$', '$x^3 + 1$', '$x^3 + 3x^2 + 3x + 1$', '$x^3 - 3x^2 + 3x - 1$'],
            'answer': 2,
            'solution': '$(x + 1)^3 = x^3 + 3 \\cdot x^2 \\cdot 1 + 3 \\cdot x \\cdot 1^2 + 1^3 = x^3 + 3x^2 '
                        '+ 3x + 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức $x^3 - 3x^2y + 3xy^2 - y^3$ viết gọn là:',
            'options': ['$(x + y)^3$', '$x^3 - y^3$', '$(y - x)^3$', '$(x - y)^3$'],
            'answer': 3,
            'solution': 'Theo hằng đẳng thức lập phương của một hiệu: $x^3 - 3x^2y + 3xy^2 - y^3 = (x - '
                        'y)^3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Lập phương của một tổng. Lập phương của một hiệu**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Lập phương của một tổng**?',
            'options': ['$(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$',
                        '$(A - B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$',
                        '$(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^2$',
                        '$(A + B)^6 = A^3 + 3A^2B + 3AB^2 + B^3$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Lập phương của một tổng. Lập phương của một '
                        'hiệu, **Lập phương của một tổng** được xác định bởi: $(A + B)^3 = A^3 + 3A^2B + '
                        '3AB^2 + B^3$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Lập phương của một tổng. Lập phương của một hiệu**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Lập phương của một hiệu**?',
            'options': ['$(A - B)^3 = A^3 - 3A^2B - 3AB^2 - B^3$',
                        '$(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$',
                        '$(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^2$',
                        '$(A - B)^6 = A^3 - 3A^2B + 3AB^2 - B^3$'],
            'answer': 1,
            'solution': 'Trong Bài 7: Lập phương của một tổng. Lập phương của một hiệu, **Lập phương của một '
                        'hiệu** có công thức/quy tắc là: $(A - B)^3 = A^3 - 3A^2B + 3AB^2 - B^3$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong khai triển của $(2x - 1)^3$, hệ số của hạng tử chứa $x^2$ là:',
            'options': ['$12$', '$-6$', '$-12$', '$6$'],
            'answer': 2,
            'solution': 'Ta có $(2x - 1)^3 = (2x)^3 - 3 \\cdot (2x)^2 \\cdot 1 + 3 \\cdot (2x) \\cdot 1^2 - '
                        '1^3 = 8x^3 - 12x^2 + 6x - 1$. Hệ số của $x^2$ là $-12$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Lập phương của một tổng. Lập phương của một hiệu**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Mô tả được hằng đẳng thức lập phương của một tổng và lập phương của một hiệu. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được hằng đẳng thức lập phương của một tổng và lập '
                        'phương của một hiệu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được hằng đẳng thức lập '
                        'phương của một tổng và lập phương của một hiệu.',
                        'Mô tả được hằng đẳng thức lập phương của một tổng và lập phương của một hiệu.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Lập phương của một tổng. Lập phương của một hiệu: '
                        'Mô tả được hằng đẳng thức lập phương của một tổng và lập phương của một hiệu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $Q = x^3 + 9x^2 + 27x + 27$. Xét các khẳng định sau:',
            'statements': ['Biểu thức $Q$ viết được dưới dạng lập phương của một tổng là $(x + 3)^3$.',
                           'Tại $x = -3$, giá trị của biểu thức $Q$ bằng $0$.',
                           'Tại $x = 7$, giá trị của biểu thức $Q$ bằng $1000$.',
                           'Hiệu $Q - (x + 3)^3$ phụ thuộc vào biến $x$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $Q = (x + 3)^3$. d) Sai vì $Q = (x + 3)^3$ là hằng đẳng thức nên '
                        '$Q - (x + 3)^3 = 0$ với mọi $x$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 7: Lập phương của một tổng. '
                 'Lập phương của một hiệu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được hằng đẳng thức lập phương của '
                           'một tổng và lập phương của một hiệu.',
                           'Trong **Bài 7: Lập phương của một tổng. Lập phương của một hiệu**, quy tắc/công '
                           'thức **Lập phương của một tổng** được viết là: $(A + B)^3 = A^3 + 3A^2B + 3AB^2 '
                           '+ B^3$.',
                           'Nếu áp dụng sai dấu/phép tính thành $(A - B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$ thì '
                           'kết quả của **Lập phương của một tổng** trong **Bài 7: Lập phương của một tổng. '
                           'Lập phương của một hiệu** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Viết biểu thức $P = x^3 - 6x^2 + 12x - 8$ dưới dạng lập '
                           'phương của một hiệu và tính giá trị của $P$ tại $x = 12$.”, kết quả giải đúng '
                           'là: Ta có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - '
                           '2)^3$. Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Lập phương của một tổng. Lập phương của '
                        'một hiệu. b) **Đúng** theo công thức **Lập phương của một tổng** ($(A + B)^3 = A^3 '
                        '+ 3A^2B + 3AB^2 + B^3$). c) **Sai** vì công thức đúng của **Lập phương của một '
                        'tổng** phải là $(A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3$ chứ không phải $(A - B)^3 = '
                        'A^3 + 3A^2B + 3AB^2 + B^3$. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Lập phương của một tổng. Lập phương của một '
                 'hiệu** để giải bài toán sau: Viết biểu thức $P = x^3 - 6x^2 + 12x - 8$ dưới dạng lập '
                 'phương của một hiệu và tính giá trị của $P$ tại $x = 12$. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Ta có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$. '
                        'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$.',
                        'Ta có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 - 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$. '
                        'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$.',
                        'Ta có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$. '
                        'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 999$.',
                        'Ta có: $P = x^6 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$. '
                        'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Lập phương của một tổng. Lập phương của một hiệu: Ta '
                        'có: $P = x^3 - 3 \\cdot x^2 \\cdot 2 + 3 \\cdot x \\cdot 2^2 - 2^3 = (x - 2)^3$.\n'
                        'Thay $x = 12$ vào $P$, ta được $P = (12 - 2)^3 = 10^3 = 1000$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $A = x^3 - 3x^2 + 3x - 1$ tại $x = 11$.',
            'answer': ['1000'],
            'unit': None,
            'solution': 'Ta có $A = (x - 1)^3$. Tại $x = 11$ thì $A = (11 - 1)^3 = 10^3 = 1000$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch02-hang-dang-thuc',
  'context_title': 'Chương II: Hằng đẳng thức đáng nhớ và ứng dụng',
  'context': 'Chương II · SGK Toán 8: Bảy hằng đẳng thức đáng nhớ và các phương pháp phân tích đa thức thành '
             'nhân tử.',
  'title': 'Bài 8: Tổng và hiệu hai lập phương',
  'icon': '🎇',
  'description': 'Hai hằng đẳng thức tổng hai lập phương và hiệu hai lập phương.',
  'requirements': ['Mô tả được hằng đẳng thức tổng hai lập phương và hiệu hai lập phương.',
                   'Vận dụng hai hằng đẳng thức này để viết đa thức dưới dạng tích hoặc rút gọn biểu thức '
                   'đại số.',
                   'Vận dụng kiến thức của **Bài 8: Tổng và hiệu hai lập phương** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Với hai biểu thức $A, B$ tùy ý, ta có: $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$ và $A^3 - B^3 '
                '= (A - B)(A^2 + AB + B^2)$.',
  'theory': '1. Tổng hai lập phương: $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$ (biểu thức $A^2 - AB + B^2$ được '
            'gọi quy ước là bình phương thiếu của hiệu $A - B$).\n'
            '2. Hiệu hai lập phương: $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$ (biểu thức $A^2 + AB + B^2$ được '
            'gọi quy ước là bình phương thiếu của tổng $A + B$).',
  'formulas': [{'category': 'Tổng và hiệu hai lập phương',
                'items': [{'name': 'Tổng hai lập phương', 'formula': '$A^3 + B^3 = (A + B)(A^2 - AB + B^2)$'},
                          {'name': 'Hiệu hai lập phương',
                           'formula': '$A^3 - B^3 = (A - B)(A^2 + AB + B^2)$'}]}],
  'example': 'Rút gọn biểu thức $M = (x + 2)(x^2 - 2x + 4) - (x - 1)(x^2 + x + 1)$.',
  'example_answer': 'Áp dụng hằng đẳng thức tổng và hiệu hai lập phương:\n'
                    '$M = (x^3 + 2^3) - (x^3 - 1^3) = x^3 + 8 - x^3 + 1 = 9$.',
  'real_life': 'Đơn giản hóa các phép tính thể tích phần chênh lệch giữa hai khối lập phương có cạnh $A$ và '
               'cạnh $B$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hằng đẳng thức tổng hai lập phương $A^3 + B^3$ bằng:',
            'options': ['$(A + B)(A^2 + AB + B^2)$',
                        '$(A - B)(A^2 + AB + B^2)$',
                        '$(A + B)(A^2 - 2AB + B^2)$',
                        '$(A + B)(A^2 - AB + B^2)$'],
            'answer': 3,
            'solution': 'Theo hằng đẳng thức tổng hai lập phương: $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Viết biểu thức $x^3 - 8$ dưới dạng tích ta được:',
            'options': ['$(x - 2)(x^2 + 2x + 4)$',
                        '$(x - 2)(x^2 - 2x + 4)$',
                        '$(x + 2)(x^2 - 2x + 4)$',
                        '$(x - 2)(x^2 + 4x + 4)$'],
            'answer': 0,
            'solution': '$x^3 - 8 = x^3 - 2^3 = (x - 2)(x^2 + 2x + 4)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Tổng và hiệu hai lập phương**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Tổng hai lập phương**?',
            'options': ['$A^3 - B^3 = (A + B)(A^2 - AB + B^2)$',
                        '$A^3 + B^3 = (A + B)(A^2 - AB + B^2)$',
                        '$A^3 + B^3 = (A + B)(A^2 - AB + B^1)$',
                        '$A^6 + B^3 = (A + B)(A^2 - AB + B^2)$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 8: Tổng và hiệu hai lập phương, **Tổng hai lập '
                        'phương** được xác định bởi: $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Tổng và hiệu hai lập phương**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Hiệu hai lập phương**?',
            'options': ['$A^3 - B^3 = (A - B)(A^2 - AB + B^2)$',
                        '$A^3 - B^3 = (A - B)(A^2 + AB + B^1)$',
                        '$A^3 - B^3 = (A - B)(A^2 + AB + B^2)$',
                        '$A^6 - B^3 = (A - B)(A^2 + AB + B^2)$'],
            'answer': 2,
            'solution': 'Trong Bài 8: Tổng và hiệu hai lập phương, **Hiệu hai lập phương** có công thức/quy '
                        'tắc là: $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Rút gọn biểu thức $(2x + 1)(4x^2 - 2x + 1)$ ta được kết quả là:',
            'options': ['$8x^3 - 1$', '$2x^3 + 1$', '$4x^3 + 1$', '$8x^3 + 1$'],
            'answer': 3,
            'solution': '$(2x + 1)[(2x)^2 - 2x \\cdot 1 + 1^2] = (2x)^3 + 1^3 = 8x^3 + 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 8: Tổng và hiệu hai lập phương**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Mô tả được hằng đẳng thức tổng hai lập phương và hiệu hai lập phương.',
                        'Mô tả được hằng đẳng thức tổng hai lập phương và hiệu hai lập phương. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được hằng đẳng thức tổng hai lập phương và hiệu hai '
                        'lập phương.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được hằng đẳng thức tổng '
                        'hai lập phương và hiệu hai lập phương.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 8: Tổng và hiệu hai lập phương: Mô tả được hằng đẳng '
                        'thức tổng hai lập phương và hiệu hai lập phương.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $P = (x - 3)(x^2 + 3x + 9) - x^3$. Xét các khẳng định sau:',
            'statements': ['Tích $(x - 3)(x^2 + 3x + 9)$ bằng $x^3 - 27$.',
                           'Sau khi rút gọn, giá trị của biểu thức $P$ bằng $-27$ với mọi $x$.',
                           'Biểu thức $P$ có giá trị phụ thuộc vào biến $x$.',
                           'Biểu thức $x^3 + 27$ phân tích được thành $(x + 3)(x^2 - 3x + 9)$.'],
            'answer': [True, True, False, True],
            'solution': 'a), b), d) Đúng vì $(x - 3)(x^2 + 3x + 9) = x^3 - 3^3 = x^3 - 27 \\Rightarrow P = '
                        'x^3 - 27 - x^3 = -27$. c) Sai vì $P = -27$ không phụ thuộc vào $x$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 8: Tổng và hiệu hai lập '
                 'phương**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được hằng đẳng thức tổng hai lập '
                           'phương và hiệu hai lập phương.',
                           'Trong **Bài 8: Tổng và hiệu hai lập phương**, quy tắc/công thức **Tổng hai lập '
                           'phương** được viết là: $A^3 + B^3 = (A + B)(A^2 - AB + B^2)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $A^3 - B^3 = (A + B)(A^2 - AB + B^2)$ thì '
                           'kết quả của **Tổng hai lập phương** trong **Bài 8: Tổng và hiệu hai lập phương** '
                           'vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Rút gọn biểu thức $M = (x + 2)(x^2 - 2x + 4) - (x - 1)(x^2 + '
                           'x + 1)$.”, kết quả giải đúng là: Áp dụng hằng đẳng thức tổng và hiệu hai lập '
                           'phương: $M = (x^3 + 2^3) - (x^3 - 1^3) = x^3 + 8 - x^3 + 1 = 9$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Tổng và hiệu hai lập phương. b) '
                        '**Đúng** theo công thức **Tổng hai lập phương** ($A^3 + B^3 = (A + B)(A^2 - AB + '
                        'B^2)$). c) **Sai** vì công thức đúng của **Tổng hai lập phương** phải là $A^3 + B^3 '
                        '= (A + B)(A^2 - AB + B^2)$ chứ không phải $A^3 - B^3 = (A + B)(A^2 - AB + B^2)$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 8: Tổng và hiệu hai lập phương** để giải bài toán '
                 'sau: Rút gọn biểu thức $M = (x + 2)(x^2 - 2x + 4) - (x - 1)(x^2 + x + 1)$. Cách giải và '
                 'kết quả nào dưới đây là **đúng**?',
            'options': ['Áp dụng hằng đẳng thức tổng và hiệu hai lập phương: $M = (x^3 - 2^3) - (x^3 - 1^3) '
                        '= x^3 + 8 - x^3 + 1 = 9$.',
                        'Áp dụng hằng đẳng thức tổng và hiệu hai lập phương: $M = (x^3 + 2^3) - (x^3 - 1^3) '
                        '= x^3 + 8 - x^3 + 1 = 9$.',
                        'Áp dụng hằng đẳng thức tổng và hiệu hai lập phương: $M = (x^3 + 2^3) - (x^3 - 1^3) '
                        '= x^3 + 8 - x^3 + 1 = 8$.',
                        'Áp dụng hằng đẳng thức tổng và hiệu hai lập phương: $M = (x^6 + 2^3) - (x^3 - 1^3) '
                        '= x^3 + 8 - x^3 + 1 = 9$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Tổng và hiệu hai lập phương: Áp dụng hằng đẳng thức '
                        'tổng và hiệu hai lập phương:\n'
                        '$M = (x^3 + 2^3) - (x^3 - 1^3) = x^3 + 8 - x^3 + 1 = 9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $A = (x + 3)(x^2 - 3x + 9) - x^3$ tại $x = 2026$.',
            'answer': ['27'],
            'unit': None,
            'solution': 'Ta có $A = (x^3 + 3^3) - x^3 = 27$ với mọi $x$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch02-hang-dang-thuc',
  'context_title': 'Chương II: Hằng đẳng thức đáng nhớ và ứng dụng',
  'context': 'Chương II · SGK Toán 8: Bảy hằng đẳng thức đáng nhớ và các phương pháp phân tích đa thức thành '
             'nhân tử.',
  'title': 'Bài 9: Phân tích đa thức thành nhân tử',
  'icon': '🧩',
  'description': 'Khái niệm phân tích đa thức thành nhân tử và các phương pháp đặt nhân tử chung, dùng hằng '
                 'đẳng thức, nhóm hạng tử.',
  'requirements': ['Nhận biết được thế nào là phân tích đa thức thành nhân tử.',
                   'Vận dụng được các phương pháp cơ bản: đặt nhân tử chung, sử dụng hằng đẳng thức, nhóm '
                   'các hạng tử để phân tích đa thức thành nhân tử.',
                   'Vận dụng kiến thức của **Bài 9: Phân tích đa thức thành nhân tử** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Phân tích đa thức thành nhân tử (hay thừa số) là biến đổi đa thức đó thành một tích của '
                'những đa thức.',
  'theory': 'Ba phương pháp cơ bản để phân tích đa thức thành nhân tử:\n'
            '1. Phương pháp đặt nhân tử chung: Dựa trên tính chất phân phối $AB + AC = A(B + C)$.\n'
            '2. Phương pháp sử dụng hằng đẳng thức: Vận dụng trực tiếp $7$ hằng đẳng thức đáng nhớ để biến '
            'tổng thành tích.\n'
            '3. Phương pháp nhóm hạng tử: Nhóm các hạng tử một cách thích hợp để xuất hiện hằng đẳng thức '
            'hoặc nhân tử chung mới.',
  'formulas': [{'category': 'Các phương pháp phân tích đa thức thành nhân tử',
                'items': [{'name': 'Đặt nhân tử chung',
                           'formula': '$A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$'},
                          {'name': 'Dùng hằng đẳng thức hiệu hai bình phương',
                           'formula': '$A^2 - B^2 = (A - B)(A + B)$'},
                          {'name': 'Nhóm hạng tử',
                           'formula': '$ac + ad + bc + bd = a(c + d) + b(c + d) = (a + b)(c + d)$'}]}],
  'example': 'Phân tích đa thức $P = x^2 - 2xy + y^2 - 9$ thành nhân tử.',
  'example_answer': 'Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức:\n'
                    '$P = (x^2 - 2xy + y^2) - 9 = (x - y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.',
  'real_life': 'Giải các bài toán tìm kích thước hình học hoặc tính nhẩm nhanh các biểu thức số phức tạp '
               'bằng cách đặt thừa số chung.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân tích đa thức $3x^2 - 6x$ thành nhân tử ta được:',
            'options': ['$3x(x - 2)$', '$3(x^2 - 6x)$', '$3x(x + 2)$', '$x(3x - 2)$'],
            'answer': 0,
            'solution': 'Đặt nhân tử chung $3x$ ra ngoài: $3x^2 - 6x = 3x(x - 2)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân tích đa thức $x^2 - 4y^2$ thành nhân tử ta được:',
            'options': ['$(x - 4y)(x + 4y)$', '$(x - 2y)(x + 2y)$', '$(x - 2y)^2$', '$(x + 2y)^2$'],
            'answer': 1,
            'solution': '$x^2 - 4y^2 = x^2 - (2y)^2 = (x - 2y)(x + 2y)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Phân tích đa thức thành nhân tử**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Đặt nhân tử chung**?',
            'options': ['$A \\cdot B - A \\cdot C - A \\cdot D = A(B + C - D)$',
                        'Đảo ngược vế của quy tắc: $A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$',
                        '$A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $A \\cdot B + A \\cdot C - A '
                        '\\cdot D = A(B + C - D)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 9: Phân tích đa thức thành nhân tử, **Đặt nhân tử '
                        'chung** được xác định bởi: $A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Phân tích đa thức thành nhân tử**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Dùng hằng đẳng thức hiệu hai bình phương**?',
            'options': ['$A^2 - B^2 = (A - B)(A - B)$',
                        '$A^2 - B^1 = (A - B)(A + B)$',
                        '$A^4 - B^2 = (A - B)(A + B)$',
                        '$A^2 - B^2 = (A - B)(A + B)$'],
            'answer': 3,
            'solution': 'Trong Bài 9: Phân tích đa thức thành nhân tử, **Dùng hằng đẳng thức hiệu hai bình '
                        'phương** có công thức/quy tắc là: $A^2 - B^2 = (A - B)(A + B)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phân tích đa thức $x^2 + xy - 3x - 3y$ thành nhân tử ta được:',
            'options': ['$(x + y)(x - 3)$', '$(x - y)(x - 3)$', '$(x + y)(x + 3)$', '$x(x + y - 3)$'],
            'answer': 0,
            'solution': 'Nhóm hạng tử: $(x^2 + xy) - (3x + 3y) = x(x + y) - 3(x + y) = (x + y)(x - 3)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 9: Phân tích đa thức thành nhân tử**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được thế nào là phân tích đa thức thành nhân tử. (với dấu ngược lại)',
                        'Nhận biết được thế nào là phân tích đa thức thành nhân tử.',
                        'Đảo ngược vế của quy tắc: Nhận biết được thế nào là phân tích đa thức thành nhân '
                        'tử.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được thế nào là phân '
                        'tích đa thức thành nhân tử.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 9: Phân tích đa thức thành nhân tử: Nhận biết được '
                        'thế nào là phân tích đa thức thành nhân tử.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đa thức $A = 2x^3 - 8x$. Xét các khẳng định sau:',
            'statements': ['Đặt nhân tử chung $2x$ ta được $A = 2x(x^2 - 4)$.',
                           'Phân tích tiếp $x^2 - 4$ bằng hằng đẳng thức ta được $A = 2x(x - 2)(x + 2)$.',
                           'Tại $x = 2$, giá trị của đa thức $A$ bằng $0$.',
                           'Chỉ có duy nhất một giá trị nguyên của $x$ làm cho $A = 0$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $A = 2x(x - 2)(x + 2) = 0$ có $3$ giá trị nguyên của $x$ '
                        'là $x \\in \\{0; 2; -2\\}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 9: Phân tích đa thức thành '
                 'nhân tử**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được thế nào là phân tích đa '
                           'thức thành nhân tử.',
                           'Trong **Bài 9: Phân tích đa thức thành nhân tử**, quy tắc/công thức **Đặt nhân '
                           'tử chung** được viết là: $A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $A \\cdot B - A \\cdot C - A \\cdot D = A(B '
                           '+ C - D)$ thì kết quả của **Đặt nhân tử chung** trong **Bài 9: Phân tích đa thức '
                           'thành nhân tử** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Phân tích đa thức $P = x^2 - 2xy + y^2 - 9$ thành nhân tử.”, '
                           'kết quả giải đúng là: Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức: $P = (x^2 '
                           '- 2xy + y^2) - 9 = (x - y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Phân tích đa thức thành nhân tử. b) '
                        '**Đúng** theo công thức **Đặt nhân tử chung** ($A \\cdot B + A \\cdot C - A \\cdot '
                        'D = A(B + C - D)$). c) **Sai** vì công thức đúng của **Đặt nhân tử chung** phải là '
                        '$A \\cdot B + A \\cdot C - A \\cdot D = A(B + C - D)$ chứ không phải $A \\cdot B - '
                        'A \\cdot C - A \\cdot D = A(B + C - D)$. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 9: Phân tích đa thức thành nhân tử** để giải bài '
                 'toán sau: Phân tích đa thức $P = x^2 - 2xy + y^2 - 9$ thành nhân tử. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức: $P = (x^2 - 2xy - y^2) - 9 = (x - '
                        'y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.',
                        'Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức: $P = (x^2 - 2xy + y^2) - 9 = (x - '
                        'y)^2 - 3^2 = (x - y - 3)(x - y + 2)$.',
                        'Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức: $P = (x^2 - 2xy + y^2) - 9 = (x - '
                        'y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.',
                        'Nhóm ba hạng tử đầu để xuất hiện hằng đẳng thức: $P = (x^4 - 2xy + y^2) - 9 = (x - '
                        'y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Phân tích đa thức thành nhân tử: Nhóm ba hạng tử đầu '
                        'để xuất hiện hằng đẳng thức:\n'
                        '$P = (x^2 - 2xy + y^2) - 9 = (x - y)^2 - 3^2 = (x - y - 3)(x - y + 3)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính nhanh giá trị của biểu thức $S = 73 \\cdot 64 + 73 \\cdot 36 - 7300$.',
            'answer': ['0'],
            'unit': None,
            'solution': 'Ta có $S = 73(64 + 36) - 7300 = 73 \\cdot 100 - 7300 = 7300 - 7300 = 0$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch03-tu-giac',
  'context_title': 'Chương III: Tứ giác',
  'context': 'Chương III · SGK Toán 8: Tứ giác, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và '
             'hình vuông.',
  'title': 'Bài 10: Tứ giác',
  'icon': '四边形',
  'description': 'Khái niệm tứ giác, tứ giác lồi và định lí tổng các góc của một tứ giác.',
  'requirements': ['Mô tả được tứ giác, tứ giác lồi và các yếu tố đỉnh, cạnh, đường chéo, góc của tứ giác.',
                   'Giải thích và vận dụng được định lí về tổng các góc trong một tứ giác lồi bằng '
                   '$360^\\circ$.',
                   'Vận dụng kiến thức của **Bài 10: Tứ giác** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': 'Tứ giác lồi là tứ giác luôn nằm về một phía của đường thẳng chứa một cạnh bất kì của tứ '
                'giác đó. Tổng các góc của một tứ giác bằng $360^\\circ$.',
  'theory': '1. Các yếu tố của tứ giác $ABCD$: Gồm $4$ đỉnh $A, B, C, D$; $4$ cạnh $AB, BC, CD, DA$ và $2$ '
            'đường chéo $AC, BD$. Khi nói đến tứ giác mà không chú thích gì thêm, ta hiểu đó là tứ giác '
            'lồi.\n'
            '2. Định lí tổng các góc của một tứ giác: Trong tứ giác $ABCD$, ta luôn có $\\widehat{A} + '
            '\\widehat{B} + \\widehat{C} + \\widehat{D} = 360^\\circ$ (chứng minh bằng cách kẻ đường chéo '
            '$AC$ chia tứ giác thành hai tam giác có tổng các góc là $180^\\circ + 180^\\circ = '
            '360^\\circ$).',
  'formulas': [{'category': 'Hệ thức góc trong tứ giác',
                'items': [{'name': 'Tổng bốn góc trong tứ giác $ABCD$',
                           'formula': '$\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = '
                                      '360^\\circ$'},
                          {'name': 'Tính góc còn lại khi biết 3 góc',
                           'formula': '$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + '
                                      '\\widehat{C})$'}]}],
  'example': 'Cho tứ giác $ABCD$ có $\\widehat{A} = 110^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = '
             '75^\\circ$. Tính số đo góc $\\widehat{D}$.',
  'example_answer': 'Áp dụng định lí tổng các góc của một tứ giác:\n'
                    '$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C}) = 360^\\circ '
                    '- (110^\\circ + 80^\\circ + 75^\\circ) = 95^\\circ$.',
  'real_life': 'Kiểm tra độ chính xác khi đo đạc bốn góc của một thửa đất hình tứ giác (tổng bốn góc phải '
               'bằng $360^\\circ$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng số đo bốn góc của một tứ giác lồi bằng:',
            'options': ['$180^\\circ$', '$360^\\circ$', '$270^\\circ$', '$540^\\circ$'],
            'answer': 1,
            'solution': 'Định lí: Tổng các góc của một tứ giác bằng $360^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong tứ giác $ABCD$, hai đường chéo của tứ giác là:',
            'options': ['$AB$ và $CD$', '$AD$ và $BC$', '$AC$ và $BD$', '$AB$ và $AC$'],
            'answer': 2,
            'solution': 'Đường chéo nối hai đỉnh đối nhau của tứ giác $ABCD$ là $AC$ và $BD$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Tứ giác**, quy tắc hoặc công thức nào sau đây xác định đúng **Tổng bốn góc '
                 'trong tứ giác $ABCD$**?',
            'options': ['$\\widehat{A} - \\widehat{B} + \\widehat{C} + \\widehat{D} = 360^\\circ$',
                        '$\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = 359^\\circ$',
                        '$\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = 362^\\circ$',
                        '$\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = 360^\\circ$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 10: Tứ giác, **Tổng bốn góc trong tứ giác $ABCD$** '
                        'được xác định bởi: $\\widehat{A} + \\widehat{B} + \\widehat{C} + \\widehat{D} = '
                        '360^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Tứ giác**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tính góc '
                 'còn lại khi biết 3 góc**?',
            'options': ['$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C})$',
                        '$\\widehat{D} = 360^\\circ - (\\widehat{A} - \\widehat{B} + \\widehat{C})$',
                        '$\\widehat{D} = 359^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C})$',
                        '$\\widehat{D} = 362^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C})$'],
            'answer': 0,
            'solution': 'Trong Bài 10: Tứ giác, **Tính góc còn lại khi biết 3 góc** có công thức/quy tắc là: '
                        '$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C})$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tứ giác $MNPQ$ có $\\widehat{M} = 90^\\circ, \\widehat{N} = 100^\\circ, \\widehat{P} = '
                 '70^\\circ$. Số đo góc $\\widehat{Q}$ là:',
            'options': ['$90^\\circ$', '$100^\\circ$', '$80^\\circ$', '$110^\\circ$'],
            'answer': 1,
            'solution': '$\\widehat{Q} = 360^\\circ - (90^\\circ + 100^\\circ + 70^\\circ) = 360^\\circ - '
                        '260^\\circ = 100^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 10: Tứ giác**, nhận định nào sau đây là **chính xác**?',
            'options': ['Mô tả được tứ giác, tứ giác lồi và các yếu tố đỉnh, cạnh, đường chéo, góc của tứ '
                        'giác. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được tứ giác, tứ giác lồi và các yếu tố đỉnh, cạnh, '
                        'đường chéo, góc của tứ giác.',
                        'Mô tả được tứ giác, tứ giác lồi và các yếu tố đỉnh, cạnh, đường chéo, góc của tứ '
                        'giác.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được tứ giác, tứ giác lồi '
                        'và các yếu tố đỉnh, cạnh, đường chéo, góc của tứ giác.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 10: Tứ giác: Mô tả được tứ giác, tứ giác lồi và các '
                        'yếu tố đỉnh, cạnh, đường chéo, góc của tứ giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về các góc của một tứ giác lồi:',
            'statements': ['Một tứ giác có thể có cả bốn góc đều là góc vuông.',
                           'Một tứ giác có thể có cả bốn góc đều là góc nhọn.',
                           'Một tứ giác có nhiều nhất ba góc tù.',
                           'Nếu tứ giác $ABCD$ có $\\widehat{A} = \\widehat{B} = \\widehat{C} = '
                           '\\widehat{D}$ thì mỗi góc bằng $90^\\circ$.'],
            'answer': [True, False, True, True],
            'solution': 'a), c), d) Đúng. b) Sai vì nếu cả bốn góc đều nhọn ($< 90^\\circ$) thì tổng bốn góc '
                        'nhỏ hơn $360^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 10: Tứ giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được tứ giác, tứ giác lồi và các '
                           'yếu tố đỉnh, cạnh, đường chéo, góc của tứ giác.',
                           'Trong **Bài 10: Tứ giác**, quy tắc/công thức **Tổng bốn góc trong tứ giác '
                           '$ABCD$** được viết là: $\\widehat{A} + \\widehat{B} + \\widehat{C} + '
                           '\\widehat{D} = 360^\\circ$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\widehat{A} - \\widehat{B} + \\widehat{C} '
                           '+ \\widehat{D} = 360^\\circ$ thì kết quả của **Tổng bốn góc trong tứ giác '
                           '$ABCD$** trong **Bài 10: Tứ giác** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho tứ giác $ABCD$ có $\\widehat{A} = 110^\\circ, '
                           '\\widehat{B} = 80^\\circ, \\widehat{C} = 75^\\circ$. Tính số đo góc '
                           '$\\widehat{D}$.”, kết quả giải đúng là: Áp dụng định lí tổng các góc của một tứ '
                           'giác: $\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C}) '
                           '= 360^\\circ - (110^\\circ + 80^\\circ + 75^\\circ) = 95^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Tứ giác. b) **Đúng** theo công thức '
                        '**Tổng bốn góc trong tứ giác $ABCD$** ($\\widehat{A} + \\widehat{B} + \\widehat{C} '
                        '+ \\widehat{D} = 360^\\circ$). c) **Sai** vì công thức đúng của **Tổng bốn góc '
                        'trong tứ giác $ABCD$** phải là $\\widehat{A} + \\widehat{B} + \\widehat{C} + '
                        '\\widehat{D} = 360^\\circ$ chứ không phải $\\widehat{A} - \\widehat{B} + '
                        '\\widehat{C} + \\widehat{D} = 360^\\circ$. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 10: Tứ giác** để giải bài toán sau: Cho tứ giác '
                 '$ABCD$ có $\\widehat{A} = 110^\\circ, \\widehat{B} = 80^\\circ, \\widehat{C} = 75^\\circ$. '
                 'Tính số đo góc $\\widehat{D}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Áp dụng định lí tổng các góc của một tứ giác: $\\widehat{D} = 360^\\circ - '
                        '(\\widehat{A} - \\widehat{B} + \\widehat{C}) = 360^\\circ - (110^\\circ + 80^\\circ '
                        '+ 75^\\circ) = 95^\\circ$...',
                        'Áp dụng định lí tổng các góc của một tứ giác: $\\widehat{D} = 360^\\circ - '
                        '(\\widehat{A} + \\widehat{B} + \\widehat{C}) = 360^\\circ - (110^\\circ + 80^\\circ '
                        '+ 75^\\circ) = 94^\\circ$...',
                        'Áp dụng định lí tổng các góc của một tứ giác: $\\widehat{D} = 362^\\circ - '
                        '(\\widehat{A} + \\widehat{B} + \\widehat{C}) = 360^\\circ - (110^\\circ + 80^\\circ '
                        '+ 75^\\circ) = 95^\\circ$...',
                        'Áp dụng định lí tổng các góc của một tứ giác: $\\widehat{D} = 360^\\circ - '
                        '(\\widehat{A} + \\widehat{B} + \\widehat{C}) = 360^\\circ - (110^\\circ + 80^\\circ '
                        '+ 75^\\circ) = 95^\\circ$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Tứ giác: Áp dụng định lí tổng các góc của một tứ '
                        'giác:\n'
                        '$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C}) = '
                        '360^\\circ - (110^\\circ + 80^\\circ + 75^\\circ) = 95^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tứ giác $ABCD$ có $\\widehat{A} = 60^\\circ, \\widehat{B} = 120^\\circ$ và '
                 '$\\widehat{C} = \\widehat{D}$. Tính số đo góc $\\widehat{C}$ (đơn vị độ).',
            'answer': ['90'],
            'unit': None,
            'solution': 'Ta có $\\widehat{C} + \\widehat{D} = 360^\\circ - (60^\\circ + 120^\\circ) = '
                        '180^\\circ$. Vì $\\widehat{C} = \\widehat{D}$ nên $\\widehat{C} = '
                        '\\dfrac{180^\\circ}{2} = 90^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch03-tu-giac',
  'context_title': 'Chương III: Tứ giác',
  'context': 'Chương III · SGK Toán 8: Tứ giác, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và '
             'hình vuông.',
  'title': 'Bài 11: Hình thang cân',
  'icon': '📐',
  'description': 'Định nghĩa hình thang, hình thang cân, tính chất và dấu hiệu nhận biết hình thang cân.',
  'requirements': ['Nhận biết được hình thang, hình thang vuông và hình thang cân.',
                   'Giải thích được tính chất về cạnh bên, đường chéo của hình thang cân.',
                   'Nhận biết và vận dụng được dấu hiệu nhận biết hình thang cân.'],
  'definition': 'Hình thang là tứ giác có hai cạnh đối song song. Hình thang cân là hình thang có hai góc kề '
                'một đáy bằng nhau.',
  'theory': '1. Hình thang: Hai cạnh song song gọi là hai đáy, hai cạnh còn lại gọi là hai cạnh bên. Hình '
            'thang có một góc vuông gọi là hình thang vuông.\n'
            '2. Tính chất của hình thang cân:\n'
            '- Trong hình thang cân, hai cạnh bên bằng nhau.\n'
            '- Trong hình thang cân, hai đường chéo bằng nhau.\n'
            '3. Dấu hiệu nhận biết hình thang cân:\n'
            '- Hình thang có hai góc kề một đáy bằng nhau là hình thang cân.\n'
            '- Hình thang có hai đường chéo bằng nhau là hình thang cân.',
  'formulas': [{'category': 'Hệ thức trong hình thang và hình thang cân ($AB \\parallel CD$)',
                'items': [{'name': 'Hai góc kề một cạnh bên',
                           'formula': '$\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + '
                                      '\\widehat{C} = 180^\\circ$'},
                          {'name': 'Tính chất hình thang cân $ABCD$ ($AB \\parallel CD$)',
                           'formula': '$\\widehat{A} = \\widehat{B}, \\; \\widehat{C} = \\widehat{D}, \\; AD '
                                      '= BC, \\; AC = BD$'},
                          {'name': 'Diện tích hình thang',
                           'formula': '$S = \\dfrac{(a + b) \\cdot h}{2}$ ($a, b$ là hai đáy, $h$ là chiều '
                                      'cao)'}]}],
  'example': 'Cho hình thang cân $ABCD$ có $AB \\parallel CD$ và $\\widehat{D} = 70^\\circ$. Tính số đo các '
             'góc $\\widehat{C}, \\widehat{A}, \\widehat{B}$.',
  'example_answer': 'Vì $ABCD$ là hình thang cân ($AB \\parallel CD$) nên hai góc kề một đáy bằng nhau: '
                    '$\\widehat{C} = \\widehat{D} = 70^\\circ$.\n'
                    'Vì $AB \\parallel CD$ nên $\\widehat{A} + \\widehat{D} = 180^\\circ \\Rightarrow '
                    '\\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$, và $\\widehat{B} = \\widehat{A} = '
                    '110^\\circ$.',
  'real_life': 'Mặt cắt của con đê chắn lũ, mặt bàn học ghép theo nhóm hoặc khung thang chữ A đều có dạng '
               'hình thang cân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một hình thang cân, khẳng định nào sau đây là ĐÚNG?',
            'options': ['Hai đáy bằng nhau',
                        'Hai đường chéo vuông góc với nhau',
                        'Hai đường chéo bằng nhau',
                        'Bốn góc đều bằng nhau'],
            'answer': 2,
            'solution': 'Theo định lí tính chất hình thang cân: Trong hình thang cân, hai cạnh bên bằng nhau '
                        'và hai đường chéo bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình thang $ABCD$ ($AB \\parallel CD$) là hình thang cân nếu có thêm điều kiện nào sau '
                 'đây?',
            'options': ['$AB = CD$',
                        '$\\widehat{A} = \\widehat{C}$',
                        '$AD \\parallel BC$',
                        '$\\widehat{C} = \\widehat{D}$'],
            'answer': 3,
            'solution': 'Hình thang có hai góc kề một đáy ($\\widehat{C} = \\widehat{D}$) bằng nhau là hình '
                        'thang cân.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Hình thang cân**, quy tắc hoặc công thức nào sau đây xác định đúng **Hai '
                 'góc kề một cạnh bên**?',
            'options': ['$\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + \\widehat{C} = '
                        '180^\\circ$',
                        '$\\widehat{A} - \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + \\widehat{C} = '
                        '180^\\circ$',
                        '$\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + \\widehat{C} = '
                        '179^\\circ$',
                        '$\\widehat{A} + \\widehat{D} = 182^\\circ; \\quad \\widehat{B} + \\widehat{C} = '
                        '180^\\circ$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: Hình thang cân, **Hai góc kề một cạnh bên** '
                        'được xác định bởi: $\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + '
                        '\\widehat{C} = 180^\\circ$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Hình thang cân**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Tính chất hình thang cân $ABCD$ ($AB \\parallel CD$)**?',
            'options': ['$\\widehat{A} = \\widehat{B}, \\; \\widehat{C} = \\widehat{D}, \\; AD = BC, \\; AC '
                        '= BD$ (với dấu ngược lại)',
                        '$\\widehat{A} = \\widehat{B}, \\; \\widehat{C} = \\widehat{D}, \\; AD = BC, \\; AC '
                        '= BD$',
                        'Đảo ngược vế của quy tắc: $\\widehat{A} = \\widehat{B}, \\; \\widehat{C} = '
                        '\\widehat{D}, \\; AD = BC, \\; AC = BD$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\widehat{A} = \\widehat{B}, '
                        '\\; \\widehat{C} = \\widehat{D}, \\; AD = BC, \\; AC = BD$'],
            'answer': 1,
            'solution': 'Trong Bài 11: Hình thang cân, **Tính chất hình thang cân $ABCD$ ($AB \\parallel '
                        'CD$)** có công thức/quy tắc là: $\\widehat{A} = \\widehat{B}, \\; \\widehat{C} = '
                        '\\widehat{D}, \\; AD = BC, \\; AC = BD$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình thang cân $ABCD$ ($AB \\parallel CD$) có $\\widehat{A} = 115^\\circ$. Số đo góc '
                 '$\\widehat{C}$ là:',
            'options': ['$115^\\circ$', '$75^\\circ$', '$65^\\circ$', '$55^\\circ$'],
            'answer': 2,
            'solution': 'Vì $AB \\parallel CD$ nên $\\widehat{D} = 180^\\circ - \\widehat{A} = 180^\\circ - '
                        '115^\\circ = 65^\\circ$. Do hình thang cân nên $\\widehat{C} = \\widehat{D} = '
                        '65^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: Hình thang cân**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được hình thang, hình thang vuông và hình thang cân. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được hình thang, hình thang vuông và hình thang '
                        'cân.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hình thang, hình '
                        'thang vuông và hình thang cân.',
                        'Nhận biết được hình thang, hình thang vuông và hình thang cân.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 11: Hình thang cân: Nhận biết được hình thang, hình '
                        'thang vuông và hình thang cân.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình thang cân $ABCD$ ($AB \\parallel CD, AB < CD$) có $AD = 5\\text{ cm}$ và $AC = '
                 '8\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Độ dài cạnh bên $BC$ bằng $5\\text{ cm}$.',
                           'Độ dài đường chéo $BD$ bằng $8\\text{ cm}$.',
                           'Hai góc $\\widehat{A}$ và $\\widehat{C}$ có tổng bằng $180^\\circ$.',
                           'Tứ giác bất kì chỉ cần có hai cạnh đối bằng nhau là hình thang cân.'],
            'answer': [True, True, True, False],
            'solution': 'a), b) Đúng. c) Đúng vì $\\widehat{A} + \\widehat{D} = 180^\\circ$ và $\\widehat{D} '
                        '= \\widehat{C}$ nên $\\widehat{A} + \\widehat{C} = 180^\\circ$. d) Sai vì trước hết '
                        'tứ giác đó phải là hình thang (có hai đáy song song).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 11: Hình thang cân**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hình thang, hình thang '
                           'vuông và hình thang cân.',
                           'Trong **Bài 11: Hình thang cân**, quy tắc/công thức **Hai góc kề một cạnh bên** '
                           'được viết là: $\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad \\widehat{B} + '
                           '\\widehat{C} = 180^\\circ$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\widehat{A} - \\widehat{D} = 180^\\circ; '
                           '\\quad \\widehat{B} + \\widehat{C} = 180^\\circ$ thì kết quả của **Hai góc kề '
                           'một cạnh bên** trong **Bài 11: Hình thang cân** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho hình thang cân $ABCD$ có $AB \\parallel CD$ và '
                           '$\\widehat{D} = 70^\\circ$. Tính số đo các góc $\\widehat{C}, \\widehat{A}, '
                           '\\widehat{B}$.”, kết quả giải đúng là: Vì $ABCD$ là hình thang cân ($AB '
                           '\\parallel CD$) nên hai góc kề một đáy bằng nhau: $\\widehat{C} = \\widehat{D} = '
                           '70^\\circ$. Vì $AB \\parallel CD$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Hình thang cân. b) **Đúng** theo công '
                        'thức **Hai góc kề một cạnh bên** ($\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad '
                        '\\widehat{B} + \\widehat{C} = 180^\\circ$). c) **Sai** vì công thức đúng của **Hai '
                        'góc kề một cạnh bên** phải là $\\widehat{A} + \\widehat{D} = 180^\\circ; \\quad '
                        '\\widehat{B} + \\widehat{C} = 180^\\circ$ chứ không phải $\\widehat{A} - '
                        '\\widehat{D} = 180^\\circ; \\quad \\widehat{B} + \\widehat{C} = 180^\\circ$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: Hình thang cân** để giải bài toán sau: Cho hình '
                 'thang cân $ABCD$ có $AB \\parallel CD$ và $\\widehat{D} = 70^\\circ$. Tính số đo các góc '
                 '$\\widehat{C}, \\widehat{A}, \\widehat{B}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $ABCD$ là hình thang cân ($AB \\parallel CD$) nên hai góc kề một đáy bằng nhau: '
                        '$\\widehat{C} = \\widehat{D} = 70^\\circ$. Vì $AB \\parallel CD$ nên...',
                        'Vì $ABCD$ là hình thang cân ($AB \\parallel CD$) nên hai góc kề một đáy bằng nhau: '
                        '$\\widehat{C} = \\widehat{D} = 80^\\circ$. Vì $AB \\parallel CD$ nên...',
                        'Vì $ABCD$ là hình thang cân ($AB \\parallel CD$) nên hai góc kề một đáy bằng nhau: '
                        '$\\widehat{C} = \\widehat{D} = 69^\\circ$. Vì $AB \\parallel CD$ nên...',
                        'Vì $ABCD$ là hình thang cân ($AB \\parallel CD$) nên hai góc kề một đáy bằng nhau: '
                        '$\\widehat{C} = \\widehat{D} = 72^\\circ$. Vì $AB \\parallel CD$ nên...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Hình thang cân: Vì $ABCD$ là hình thang cân ($AB '
                        '\\parallel CD$) nên hai góc kề một đáy bằng nhau: $\\widehat{C} = \\widehat{D} = '
                        '70^\\circ$.\n'
                        'Vì $AB \\parallel CD$ nên $\\widehat{A} + \\widehat{D} = 180^\\circ \\Rightarrow '
                        '\\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$, và $\\widehat{B} = '
                        '\\widehat{A} = 110^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình thang cân có độ dài hai đáy là $6\\text{ cm}$ và $10\\text{ cm}$, độ dài một cạnh '
                 'bên là $5\\text{ cm}$. Tính chu vi của hình thang cân đó (đơn vị $\\text{cm}$).',
            'answer': ['26'],
            'unit': None,
            'solution': 'Trong hình thang cân, hai cạnh bên bằng nhau và cùng bằng $5\\text{ cm}$. Chu vi là '
                        '$6 + 10 + 5 + 5 = 26\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch03-tu-giac',
  'context_title': 'Chương III: Tứ giác',
  'context': 'Chương III · SGK Toán 8: Tứ giác, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và '
             'hình vuông.',
  'title': 'Bài 12: Hình bình hành',
  'icon': '▱',
  'description': 'Định nghĩa, tính chất về cạnh, góc, đường chéo và các dấu hiệu nhận biết hình bình hành.',
  'requirements': ['Nhận biết được hình bình hành và giải thích được các tính chất của hình bình hành (cạnh '
                   'đối, góc đối, hai đường chéo).',
                   'Vận dụng được các dấu hiệu nhận biết hình bình hành trong chứng minh hình học.',
                   'Vận dụng kiến thức của **Bài 12: Hình bình hành** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': 'Hình bình hành là tứ giác có các cạnh đối song song.',
  'theory': '1. Tính chất của hình bình hành:\n'
            '- Các cạnh đối bằng nhau.\n'
            '- Các góc đối bằng nhau.\n'
            '- Hai đường chéo cắt nhau tại trung điểm của mỗi đường.\n'
            '2. Năm dấu hiệu nhận biết hình bình hành:\n'
            '- Tứ giác có các cạnh đối song song.\n'
            '- Tứ giác có các cạnh đối bằng nhau.\n'
            '- Tứ giác có hai cạnh đối song song và bằng nhau.\n'
            '- Tứ giác có các góc đối bằng nhau.\n'
            '- Tứ giác có hai đường chéo cắt nhau tại trung điểm của mỗi đường.',
  'formulas': [{'category': 'Tính chất và công thức hình bình hành $ABCD$',
                'items': [{'name': 'Tính chất cạnh và góc',
                           'formula': '$AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; '
                                      '\\widehat{B} = \\widehat{D}$'},
                          {'name': 'Giao điểm $O$ của hai đường chéo',
                           'formula': '$OA = OC = \\dfrac{1}{2}AC; \\quad OB = OD = \\dfrac{1}{2}BD$'},
                          {'name': 'Chu vi và diện tích hình bình hành',
                           'formula': '$P = 2(a + b); \\quad S = a \\cdot h$'}]}],
  'example': 'Cho hình bình hành $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Biết $AB = 7\\text{ '
             'cm}, BC = 5\\text{ cm}$ và $AC = 10\\text{ cm}$. Tính chu vi hình bình hành $ABCD$ và độ dài '
             '$OA$.',
  'example_answer': '- Chu vi hình bình hành $ABCD$ là $P = 2(AB + BC) = 2(7 + 5) = 24\\text{ (cm)}$.\n'
                    '- Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = \\dfrac{1}{2}AC '
                    '= 5\\text{ (cm)}$.',
  'real_life': 'Cơ cấu nâng hạ hình bình hành của xe thang cứu hỏa hoặc đèn bàn học giúp mặt sàn / chao đèn '
               'luôn giữ phương song song với mặt đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong hình bình hành, khẳng định nào sau đây là ĐÚNG?',
            'options': ['Hai đường chéo luôn bằng nhau',
                        'Hai đường chéo luôn vuông góc với nhau',
                        'Bốn cạnh luôn bằng nhau',
                        'Hai đường chéo cắt nhau tại trung điểm của mỗi đường'],
            'answer': 3,
            'solution': 'Tính chất của hình bình hành: Hai đường chéo cắt nhau tại trung điểm của mỗi đường.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tứ giác $ABCD$ là hình bình hành nếu có điều kiện nào sau đây?',
            'options': ['$AB \\parallel CD$ và $AB = CD$',
                        '$AB \\parallel CD$ và $AD = BC$',
                        '$AB = BC$ và $CD = DA$',
                        '$AC = BD$'],
            'answer': 0,
            'solution': 'Tứ giác có hai cạnh đối song song và bằng nhau ($AB \\parallel CD$ và $AB = CD$) là '
                        'hình bình hành.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Hình bình hành**, quy tắc hoặc công thức nào sau đây xác định đúng **Tính '
                 'chất cạnh và góc**?',
            'options': ['$AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; \\widehat{B} = '
                        '\\widehat{D}$ (với dấu ngược lại)',
                        '$AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; \\widehat{B} = '
                        '\\widehat{D}$',
                        'Đảo ngược vế của quy tắc: $AB = CD, \\; AD = BC; \\quad \\widehat{A} = '
                        '\\widehat{C}, \\; \\widehat{B} = \\widehat{D}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $AB = CD, \\; AD = BC; \\quad '
                        '\\widehat{A} = \\widehat{C}, \\; \\widehat{B} = \\widehat{D}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Hình bình hành, **Tính chất cạnh và góc** được '
                        'xác định bởi: $AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; '
                        '\\widehat{B} = \\widehat{D}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Hình bình hành**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Giao điểm $O$ của hai đường chéo**?',
            'options': ['$OA = OC = \\dfrac{2}{2}AC; \\quad OB = OD = \\dfrac{1}{2}BD$',
                        '$OA = OC = \\dfrac{2}{1}AC; \\quad OB = OD = \\dfrac{1}{2}BD$',
                        '$OA = OC = \\dfrac{1}{2}AC; \\quad OB = OD = \\dfrac{1}{2}BD$',
                        '$AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; \\widehat{B} = '
                        '\\widehat{D}$'],
            'answer': 2,
            'solution': 'Trong Bài 12: Hình bình hành, **Giao điểm $O$ của hai đường chéo** có công thức/quy '
                        'tắc là: $OA = OC = \\dfrac{1}{2}AC; \\quad OB = OD = \\dfrac{1}{2}BD$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình bình hành $ABCD$ có $\\widehat{A} = 65^\\circ$. Số đo của góc $\\widehat{B}$ và '
                 'góc $\\widehat{C}$ lần lượt là:',
            'options': ['$\\widehat{B} = 65^\\circ; \\widehat{C} = 115^\\circ$',
                        '$\\widehat{B} = 125^\\circ; \\widehat{C} = 65^\\circ$',
                        '$\\widehat{B} = 115^\\circ; \\widehat{C} = 115^\\circ$',
                        '$\\widehat{B} = 115^\\circ; \\widehat{C} = 65^\\circ$'],
            'answer': 3,
            'solution': 'Trong hình bình hành, hai góc đối bằng nhau nên $\\widehat{C} = \\widehat{A} = '
                        '65^\\circ$; hai góc kề bù nhau nên $\\widehat{B} = 180^\\circ - 65^\\circ = '
                        '115^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Hình bình hành**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được hình bình hành và giải thích được các tính chất của hình bình hành '
                        '(cạnh đối, góc đối, hai đường chéo).',
                        'Nhận biết được hình bình hành và giải thích được các tính chất của hình bình hành '
                        '(cạnh đối, góc đối, hai đường chéo). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được hình bình hành và giải thích được các tính '
                        'chất của hình bình hành (cạnh đối, góc đối, hai đường chéo).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hình bình hành '
                        'và giải thích được các tính chất của hình bình hành (cạnh đối, góc đối, hai đường '
                        'chéo).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Hình bình hành: Nhận biết được hình bình hành và '
                        'giải thích được các tính chất của hình bình hành (cạnh đối, góc đối, hai đường '
                        'chéo).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình bình hành $ABCD$ có giao điểm hai đường chéo là $O$. Gọi $M, N$ lần lượt là trung '
                 'điểm của $AB$ và $CD$. Xét các khẳng định sau:',
            'statements': ['Ta có $AB = CD$ và $AB \\parallel CD$.',
                           'Hai đoạn thẳng $AM$ và $CN$ song song và bằng nhau.',
                           'Tứ giác $AMCN$ là một hình bình hành.',
                           'Đường thẳng $MN$ không đi qua điểm $O$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng vì $AM \\parallel CN$ và $AM = \\dfrac{1}{2}AB = \\dfrac{1}{2}CD = '
                        'CN$. d) Sai vì trong hình bình hành $AMCN$, hai đường chéo $AC$ và $MN$ cắt nhau '
                        'tại trung điểm $O$ của $AC$ nên $MN$ đi qua $O$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 12: Hình bình hành**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hình bình hành và giải '
                           'thích được các tính chất của hình bình hành (cạnh đối, góc đối, hai đường chéo).',
                           'Trong **Bài 12: Hình bình hành**, quy tắc/công thức **Tính chất cạnh và góc** '
                           'được viết là: $AB = CD, \\; AD = BC; \\quad \\widehat{A} = \\widehat{C}, \\; '
                           '\\widehat{B} = \\widehat{D}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $AB = CD, \\; AD = BC; \\quad \\widehat{A} = '
                           '\\widehat{C}, \\; \\widehat{B} = \\widehat{D}$ (với dấu ngược lại) thì kết quả '
                           'của **Tính chất cạnh và góc** trong **Bài 12: Hình bình hành** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Cho hình bình hành $ABCD$ có hai đường chéo $AC$ và $BD$ cắt '
                           'nhau tại $O$. Biết $AB = 7\\text{ cm}, BC = 5\\text{ cm}$ và $AC = 10\\text{ '
                           'cm}$...”, kết quả giải đúng là: - Chu vi hình bình hành $ABCD$ là $P = 2(AB + '
                           'BC) = 2(7 + 5) = 24\\text{ (cm)}$. - Vì hai đường chéo cắt nhau tại trung điểm '
                           '$O$ của mỗi...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Hình bình hành. b) **Đúng** theo công '
                        'thức **Tính chất cạnh và góc** ($AB = CD, \\; AD = BC; \\quad \\widehat{A} = '
                        '\\widehat{C}, \\; \\widehat{B} = \\widehat{D}$). c) **Sai** vì công thức đúng của '
                        '**Tính chất cạnh và góc** phải là $AB = CD, \\; AD = BC; \\quad \\widehat{A} = '
                        '\\widehat{C}, \\; \\widehat{B} = \\widehat{D}$ chứ không phải $AB = CD, \\; AD = '
                        'BC; \\quad \\widehat{A} = \\widehat{C}, \\; \\widehat{B} = \\widehat{D}$ (với dấu '
                        'ngược lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Hình bình hành** để giải bài toán sau: Cho hình '
                 'bình hành $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Biết $AB = 7\\text{ cm}, '
                 'BC = 5\\text{ cm}$ và $AC = 10\\text{ cm}$. Tính chu vi hình bình hành $ABCD$ và độ dài '
                 '$OA$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- Chu vi hình bình hành $ABCD$ là $P = 2(AB - BC) = 2(7 + 5) = 24\\text{ (cm)}$. - '
                        'Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = '
                        '\\dfrac{1}{2}AC = 5\\text{ (cm)}$...',
                        '- Chu vi hình bình hành $ABCD$ là $P = 2(AB + BC) = 2(7 + 5) = 24\\text{ (cm)}$. - '
                        'Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = '
                        '\\dfrac{1}{2}AC = 5\\text{ (cm)}$...',
                        '- Chu vi hình bình hành $ABCD$ là $P = 2(AB + BC) = 2(7 + 5) = 24\\text{ (cm)}$. - '
                        'Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = '
                        '\\dfrac{2}{1}AC = 5\\text{ (cm)}$...',
                        '- Chu vi hình bình hành $ABCD$ là $P = 4(AB + BC) = 2(7 + 5) = 24\\text{ (cm)}$. - '
                        'Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = '
                        '\\dfrac{1}{2}AC = 5\\text{ (cm)}$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Hình bình hành: - Chu vi hình bình hành $ABCD$ là $P '
                        '= 2(AB + BC) = 2(7 + 5) = 24\\text{ (cm)}$.\n'
                        '- Vì hai đường chéo cắt nhau tại trung điểm $O$ của mỗi đường nên $OA = '
                        '\\dfrac{1}{2}AC = 5\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình bình hành $ABCD$ có $\\widehat{A} - \\widehat{B} = 40^\\circ$. Tính số đo góc '
                 '$\\widehat{A}$ (đơn vị độ).',
            'answer': ['110'],
            'unit': None,
            'solution': 'Vì $\\widehat{A} + \\widehat{B} = 180^\\circ$ và $\\widehat{A} - \\widehat{B} = '
                        '40^\\circ$ nên $\\widehat{A} = \\dfrac{180^\\circ + 40^\\circ}{2} = 110^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch03-tu-giac',
  'context_title': 'Chương III: Tứ giác',
  'context': 'Chương III · SGK Toán 8: Tứ giác, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và '
             'hình vuông.',
  'title': 'Bài 13: Hình chữ nhật',
  'icon': '▭',
  'description': 'Định nghĩa, tính chất, dấu hiệu nhận biết hình chữ nhật và tính chất đường trung tuyến ứng '
                 'với cạnh huyền trong tam giác vuông.',
  'requirements': ['Mô tả được định nghĩa, tính chất của hình chữ nhật và tính chất đường trung tuyến ứng '
                   'với cạnh huyền của tam giác vuông.',
                   'Vận dụng được các dấu hiệu nhận biết hình chữ nhật trong giải toán và thực tiễn.',
                   'Vận dụng kiến thức của **Bài 13: Hình chữ nhật** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': 'Hình chữ nhật là tứ giác có bốn góc vuông.',
  'theory': '1. Tính chất của hình chữ nhật: Hình chữ nhật có tất cả các tính chất của hình bình hành và '
            'hình thang cân. Đặc biệt: Trong hình chữ nhật, hai đường chéo bằng nhau và cắt nhau tại trung '
            'điểm của mỗi đường.\n'
            '2. Dấu hiệu nhận biết hình chữ nhật:\n'
            '- Tứ giác có ba góc vuông là hình chữ nhật.\n'
            '- Hình thang cân có một góc vuông là hình chữ nhật.\n'
            '- Hình bình hành có một góc vuông là hình chữ nhật.\n'
            '- Hình bình hành có hai đường chéo bằng nhau là hình chữ nhật.\n'
            '3. Áp dụng vào tam giác vuông: Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng '
            'nửa cạnh huyền. Ngược lại, nếu một tam giác có đường trung tuyến ứng với một cạnh bằng nửa cạnh '
            'ấy thì tam giác đó là tam giác vuông.',
  'formulas': [{'category': 'Hệ thức hình chữ nhật và tam giác vuông',
                'items': [{'name': 'Hai đường chéo hình chữ nhật $ABCD$ (tâm $O$)',
                           'formula': '$AC = BD$ và $OA = OB = OC = OD = \\dfrac{1}{2}AC$'},
                          {'name': 'Trung tuyến $AM$ ứng với cạnh huyền $BC$ ($\\widehat{A} = 90^\\circ$)',
                           'formula': '$AM = BM = CM = \\dfrac{1}{2}BC$'},
                          {'name': 'Chu vi và diện tích hình chữ nhật cạnh $a, b$',
                           'formula': '$P = 2(a + b); \\quad S = a \\cdot b$'}]}],
  'example': 'Cho $\\triangle ABC$ vuông tại $A$ có cạnh huyền $BC = 16\\text{ cm}$. Gọi $M$ là trung điểm '
             'của $BC$. Tính độ dài đoạn thẳng $AM$.',
  'example_answer': 'Trong tam giác vuông $\\triangle ABC$, $AM$ là đường trung tuyến ứng với cạnh huyền '
                    '$BC$.\n'
                    'Theo tính chất đường trung tuyến trong tam giác vuông, ta có $AM = \\dfrac{1}{2}BC = '
                    '\\dfrac{1}{2} \\cdot 16 = 8\\text{ (cm)}$.',
  'real_life': 'Người thợ mộc hoặc thợ xây kiểm tra một khung cửa hình bình hành đã vuông góc (thành hình '
               'chữ nhật) hay chưa bằng cách đo xem hai đường chéo có bằng nhau hay không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình bình hành $ABCD$ trở thành hình chữ nhật khi có thêm điều kiện nào sau đây?',
            'options': ['$AC = BD$', '$AC \\perp BD$', '$AB = BC$', '$AC$ là phân giác góc $\\widehat{A}$'],
            'answer': 0,
            'solution': 'Hình bình hành có hai đường chéo bằng nhau ($AC = BD$) là hình chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một tam giác vuông, đường trung tuyến ứng với cạnh huyền có độ dài bằng:',
            'options': ['Độ dài cạnh huyền',
                        'Nửa độ dài cạnh huyền',
                        'Hai lần độ dài cạnh huyền',
                        'Nửa độ dài cạnh góc vuông'],
            'answer': 1,
            'solution': 'Định lí: Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh '
                        'huyền.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Hình chữ nhật**, quy tắc hoặc công thức nào sau đây xác định đúng **Hai '
                 'đường chéo hình chữ nhật $ABCD$ (tâm $O$)**?',
            'options': ['$AC = BD$ và $OA = OB = OC = OD = \\dfrac{2}{2}AC$',
                        '$AC = BD$ và $OA = OB = OC = OD = \\dfrac{2}{1}AC$',
                        '$AC = BD$ và $OA = OB = OC = OD = \\dfrac{1}{2}AC$',
                        '$AM = BM = CM = \\dfrac{1}{2}BC$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Hình chữ nhật, **Hai đường chéo hình chữ nhật '
                        '$ABCD$ (tâm $O$)** được xác định bởi: $AC = BD$ và $OA = OB = OC = OD = '
                        '\\dfrac{1}{2}AC$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Hình chữ nhật**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Trung tuyến $AM$ ứng với cạnh huyền $BC$ ($\\widehat{A} = 90^\\circ$)**?',
            'options': ['$AM = BM = CM = \\dfrac{2}{2}BC$',
                        '$AM = BM = CM = \\dfrac{2}{1}BC$',
                        '$AC = BD$ và $OA = OB = OC = OD = \\dfrac{1}{2}AC$',
                        '$AM = BM = CM = \\dfrac{1}{2}BC$'],
            'answer': 3,
            'solution': 'Trong Bài 13: Hình chữ nhật, **Trung tuyến $AM$ ứng với cạnh huyền $BC$ '
                        '($\\widehat{A} = 90^\\circ$)** có công thức/quy tắc là: $AM = BM = CM = '
                        '\\dfrac{1}{2}BC$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chữ nhật $ABCD$ có hai đường chéo cắt nhau tại $O$. Biết $OA = 5\\text{ cm}$, độ '
                 'dài đường chéo $BD$ bằng:',
            'options': ['$10\\text{ cm}$', '$5\\text{ cm}$', '$2,5\\text{ cm}$', '$20\\text{ cm}$'],
            'answer': 0,
            'solution': 'Trong hình chữ nhật, $BD = AC = 2 \\cdot OA = 2 \\cdot 5 = 10\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Hình chữ nhật**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Mô tả được định nghĩa, tính chất của hình chữ nhật và tính chất đường trung tuyến '
                        'ứng với cạnh huyền của tam giác vuông. (với dấu ngược lại)',
                        'Mô tả được định nghĩa, tính chất của hình chữ nhật và tính chất đường trung tuyến '
                        'ứng với cạnh huyền của tam giác vuông.',
                        'Đảo ngược vế của quy tắc: Mô tả được định nghĩa, tính chất của hình chữ nhật và '
                        'tính chất đường trung tuyến ứng với cạnh huyền của tam giác vuông.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được định nghĩa, tính '
                        'chất của hình chữ nhật và tính chất đường trung tuyến ứng với cạnh huyền của tam '
                        'giác vuông.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Hình chữ nhật: Mô tả được định nghĩa, tính chất '
                        'của hình chữ nhật và tính chất đường trung tuyến ứng với cạnh huyền của tam giác '
                        'vuông.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$, gọi $M$ là trung điểm của cạnh huyền $BC$. Lấy điểm '
                 '$D$ đối xứng với $A$ qua $M$ (tức là $M$ là trung điểm của $AD$). Xét các khẳng định sau:',
            'statements': ['Tứ giác $ABDC$ có hai đường chéo cắt nhau tại trung điểm $M$ của mỗi đường nên '
                           'là hình bình hành.',
                           'Hình bình hành $ABDC$ có $\\widehat{BAC} = 90^\\circ$ nên là hình chữ nhật.',
                           'Độ dài đường trung tuyến $AM$ bằng $\\dfrac{1}{2}BC$.',
                           '$\\triangle AMB$ là một tam giác vuông tại $M$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $MA = MB$ nên $\\triangle AMB$ là tam giác cân tại $M$ '
                        '(chỉ vuông tại $M$ khi $\\triangle ABC$ vuông cân).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 13: Hình chữ nhật**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được định nghĩa, tính chất của '
                           'hình chữ nhật và tính chất đường trung tuyến ứng với cạnh huyền của tam giác '
                           'vuông.',
                           'Trong **Bài 13: Hình chữ nhật**, quy tắc/công thức **Hai đường chéo hình chữ '
                           'nhật $ABCD$ (tâm $O$)** được viết là: $AC = BD$ và $OA = OB = OC = OD = '
                           '\\dfrac{1}{2}AC$.',
                           'Nếu áp dụng sai dấu/phép tính thành $AC = BD$ và $OA = OB = OC = OD = '
                           '\\dfrac{2}{2}AC$ thì kết quả của **Hai đường chéo hình chữ nhật $ABCD$ (tâm '
                           '$O$)** trong **Bài 13: Hình chữ nhật** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho $\\triangle ABC$ vuông tại $A$ có cạnh huyền $BC = '
                           '16\\text{ cm}$. Gọi $M$ là trung điểm của $BC$. Tính độ dài đoạn thẳng $AM$.”, '
                           'kết quả giải đúng là: Trong tam giác vuông $\\triangle ABC$, $AM$ là đường trung '
                           'tuyến ứng với cạnh huyền $BC$. Theo tính chất đường trung tuyến trong tam '
                           'giá...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Hình chữ nhật. b) **Đúng** theo công '
                        'thức **Hai đường chéo hình chữ nhật $ABCD$ (tâm $O$)** ($AC = BD$ và $OA = OB = OC '
                        '= OD = \\dfrac{1}{2}AC$). c) **Sai** vì công thức đúng của **Hai đường chéo hình '
                        'chữ nhật $ABCD$ (tâm $O$)** phải là $AC = BD$ và $OA = OB = OC = OD = '
                        '\\dfrac{1}{2}AC$ chứ không phải $AC = BD$ và $OA = OB = OC = OD = \\dfrac{2}{2}AC$. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Hình chữ nhật** để giải bài toán sau: Cho '
                 '$\\triangle ABC$ vuông tại $A$ có cạnh huyền $BC = 16\\text{ cm}$. Gọi $M$ là trung điểm '
                 'của $BC$. Tính độ dài đoạn thẳng $AM$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Trong tam giác vuông $\\triangle ABC$, $AM$ là đường trung tuyến ứng với cạnh huyền '
                        '$BC$. Theo tính chất đường trung tuyến trong tam giác vuông, ta có...',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Hình chữ nhật: Trong tam giác vuông $\\triangle '
                        'ABC$, $AM$ là đường trung tuyến ứng với cạnh huyền $BC$.\n'
                        'Theo tính chất đường trung tuyến trong tam giác vuông, ta có $AM = \\dfrac{1}{2}BC '
                        '= \\dfrac{1}{2} \\cdot 16 = 8\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$ có cạnh huyền $BC = 24\\text{ cm}$. Tính độ dài đường '
                 'trung tuyến $AM$ ứng với cạnh huyền $BC$ (đơn vị $\\text{cm}$).',
            'answer': ['12'],
            'unit': None,
            'solution': 'Độ dài đường trung tuyến ứng với cạnh huyền bằng một nửa cạnh huyền: $AM = '
                        '\\dfrac{24}{2} = 12\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch03-tu-giac',
  'context_title': 'Chương III: Tứ giác',
  'context': 'Chương III · SGK Toán 8: Tứ giác, hình thang cân, hình bình hành, hình chữ nhật, hình thoi và '
             'hình vuông.',
  'title': 'Bài 14: Hình thoi và hình vuông',
  'icon': '💠',
  'description': 'Định nghĩa, tính chất và dấu hiệu nhận biết của hình thoi và hình vuông.',
  'requirements': ['Mô tả được định nghĩa, các tính chất về cạnh, góc, đường chéo và dấu hiệu nhận biết của '
                   'hình thoi.',
                   'Mô tả được định nghĩa, các tính chất và dấu hiệu nhận biết của hình vuông.',
                   'Vận dụng kiến thức của **Bài 14: Hình thoi và hình vuông** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Hình thoi là tứ giác có bốn cạnh bằng nhau. Hình vuông là tứ giác có bốn góc vuông và bốn '
                'cạnh bằng nhau (hình vuông vừa là hình chữ nhật, vừa là hình thoi).',
  'theory': '1. Hình thoi:\n'
            '- Tính chất: Hình thoi có tất cả các tính chất của hình bình hành. Đặc biệt, trong hình thoi: '
            'Hai đường chéo vuông góc với nhau; hai đường chéo là các đường phân giác của các góc của hình '
            'thoi.\n'
            '- Dấu hiệu nhận biết: Hình bình hành có hai cạnh kề bằng nhau; hoặc có hai đường chéo vuông góc '
            'với nhau; hoặc có một đường chéo là đường phân giác của một góc là hình thoi.\n'
            '2. Hình vuông:\n'
            '- Tính chất: Có đầy đủ tính chất của hình chữ nhật và hình thoi (hai đường chéo bằng nhau, '
            'vuông góc với nhau tại trung điểm mỗi đường và là phân giác các góc).\n'
            '- Dấu hiệu nhận biết: Hình chữ nhật có hai cạnh kề bằng nhau (hoặc hai đường chéo vuông góc, '
            'hoặc một đường chéo là phân giác một góc); Hình thoi có một góc vuông (hoặc hai đường chéo bằng '
            'nhau).',
  'formulas': [{'category': 'Hệ thức trong hình thoi và hình vuông',
                'items': [{'name': 'Tính chất đường chéo hình thoi $ABCD$',
                           'formula': '$AC \\perp BD$ tại trung điểm $O$ và phân giác các góc'},
                          {'name': 'Diện tích hình thoi có hai đường chéo $d_1, d_2$',
                           'formula': '$S = \\dfrac{1}{2} d_1 \\cdot d_2$'},
                          {'name': 'Chu vi và diện tích hình vuông cạnh $a$',
                           'formula': '$P = 4a; \\quad S = a^2$'}]}],
  'example': 'Một mảnh vườn hình thoi có độ dài hai đường chéo là $12\\text{ m}$ và $16\\text{ m}$. Tính '
             'diện tích mảnh vườn đó.',
  'example_answer': 'Diện tích mảnh vườn hình thoi là:\n'
                    '$S = \\dfrac{1}{2} \\cdot 12 \\cdot 16 = 96\\text{ (m}^2\\text{)}$.',
  'real_life': 'Hoa văn gạch lát nền hình vuông, lưới sắt cửa xếp kéo tay hoặc biển báo giao thông có dạng '
               'hình thoi và hình vuông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một hình thoi, hai đường chéo có tính chất nào sau đây?',
            'options': ['Luôn bằng nhau và không vuông góc',
                        'Vuông góc với nhau và cắt nhau tại trung điểm mỗi đường',
                        'Song song với nhau',
                        'Bằng độ dài cạnh của hình thoi'],
            'answer': 1,
            'solution': 'Trong hình thoi, hai đường chéo vuông góc với nhau tại trung điểm của mỗi đường và '
                        'là phân giác của các góc.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình chữ nhật $ABCD$ trở thành hình vuông khi có thêm điều kiện nào sau đây?',
            'options': ['$AB = CD$', '$AC = BD$', '$AB = BC$', '$\\widehat{A} = 90^\\circ$'],
            'answer': 2,
            'solution': 'Hình chữ nhật có hai cạnh kề bằng nhau ($AB = BC$) là hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Hình thoi và hình vuông**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Tính chất đường chéo hình thoi $ABCD$**?',
            'options': ['$AC \\perp BD$ tại trung điểm $O$ và phân giác các góc (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $AC \\perp BD$ tại trung điểm $O$ và phân giác các góc',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $AC \\perp BD$ tại trung điểm '
                        '$O$ và phân giác các góc',
                        '$AC \\perp BD$ tại trung điểm $O$ và phân giác các góc'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 14: Hình thoi và hình vuông, **Tính chất đường '
                        'chéo hình thoi $ABCD$** được xác định bởi: $AC \\perp BD$ tại trung điểm $O$ và '
                        'phân giác các góc.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Hình thoi và hình vuông**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Diện tích hình thoi có hai đường chéo $d_1, d_2$**?',
            'options': ['$S = \\dfrac{1}{2} d_1 \\cdot d_2$',
                        '$S = \\dfrac{1}{2} d_1 : d_2$',
                        '$S = \\dfrac{2}{1} d_1 \\cdot d_2$',
                        '$S = \\dfrac{2}{2} d_1 \\cdot d_2$'],
            'answer': 0,
            'solution': 'Trong Bài 14: Hình thoi và hình vuông, **Diện tích hình thoi có hai đường chéo '
                        '$d_1, d_2$** có công thức/quy tắc là: $S = \\dfrac{1}{2} d_1 \\cdot d_2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hình thoi $ABCD$ là hình vuông nếu có thêm điều kiện nào sau đây?',
            'options': ['$AC \\perp BD$', '$AC = BD$', '$AB = BC$', '$AB \\parallel CD$'],
            'answer': 1,
            'solution': 'Hình thoi đã có $AC \\perp BD, AB = BC, AB \\parallel CD$. Thêm điều kiện hai đường '
                        'chéo bằng nhau ($AC = BD$) thì hình thoi trở thành hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 14: Hình thoi và hình vuông**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Mô tả được định nghĩa, các tính chất về cạnh, góc, đường chéo và dấu hiệu nhận biết '
                        'của hình thoi. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được định nghĩa, các tính chất về cạnh, góc, đường '
                        'chéo và dấu hiệu nhận biết của hình thoi.',
                        'Mô tả được định nghĩa, các tính chất về cạnh, góc, đường chéo và dấu hiệu nhận biết '
                        'của hình thoi.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được định nghĩa, các tính '
                        'chất về cạnh, góc, đường chéo và dấu hiệu nhận biết của hình thoi.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 14: Hình thoi và hình vuông: Mô tả được định nghĩa, '
                        'các tính chất về cạnh, góc, đường chéo và dấu hiệu nhận biết của hình thoi.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về hình thoi và hình vuông:',
            'statements': ['Mọi hình vuông đều là hình chữ nhật và cũng là hình thoi.',
                           'Trong hình vuông, mỗi đường chéo tạo với cạnh hình vuông một góc $45^\\circ$.',
                           'Hình bình hành có một đường chéo là đường phân giác của một góc là hình thoi.',
                           'Mọi hình thoi đều có hai đường chéo bằng nhau.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì hai đường chéo của hình thoi chỉ bằng nhau khi hình thoi '
                        'đó là hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 14: Hình thoi và hình '
                 'vuông**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được định nghĩa, các tính chất về '
                           'cạnh, góc, đường chéo và dấu hiệu nhận biết của hình thoi.',
                           'Trong **Bài 14: Hình thoi và hình vuông**, quy tắc/công thức **Tính chất đường '
                           'chéo hình thoi $ABCD$** được viết là: $AC \\perp BD$ tại trung điểm $O$ và phân '
                           'giác các góc.',
                           'Nếu áp dụng sai dấu/phép tính thành $AC \\perp BD$ tại trung điểm $O$ và phân '
                           'giác các góc (với dấu ngược lại) thì kết quả của **Tính chất đường chéo hình '
                           'thoi $ABCD$** trong **Bài 14: Hình thoi và hình vuông** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một mảnh vườn hình thoi có độ dài hai đường chéo là '
                           '$12\\text{ m}$ và $16\\text{ m}$. Tính diện tích mảnh vườn đó.”, kết quả giải '
                           'đúng là: Diện tích mảnh vườn hình thoi là: $S = \\dfrac{1}{2} \\cdot 12 \\cdot '
                           '16 = 96\\text{ (m}^2\\text{)}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Hình thoi và hình vuông. b) **Đúng** '
                        'theo công thức **Tính chất đường chéo hình thoi $ABCD$** ($AC \\perp BD$ tại trung '
                        'điểm $O$ và phân giác các góc). c) **Sai** vì công thức đúng của **Tính chất đường '
                        'chéo hình thoi $ABCD$** phải là $AC \\perp BD$ tại trung điểm $O$ và phân giác các '
                        'góc chứ không phải $AC \\perp BD$ tại trung điểm $O$ và phân giác các góc (với dấu '
                        'ngược lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 14: Hình thoi và hình vuông** để giải bài toán sau: '
                 'Một mảnh vườn hình thoi có độ dài hai đường chéo là $12\\text{ m}$ và $16\\text{ m}$. Tính '
                 'diện tích mảnh vườn đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Diện tích mảnh vườn hình thoi là: $S = \\dfrac{1}{2} : 12 \\cdot 16 = 96\\text{ '
                        '(m}^2\\text{)}$.',
                        'Diện tích mảnh vườn hình thoi là: $S = \\dfrac{2}{1} \\cdot 12 \\cdot 16 = '
                        '96\\text{ (m}^2\\text{)}$.',
                        'Diện tích mảnh vườn hình thoi là: $S = \\dfrac{2}{2} \\cdot 12 \\cdot 16 = '
                        '96\\text{ (m}^2\\text{)}$.',
                        'Diện tích mảnh vườn hình thoi là: $S = \\dfrac{1}{2} \\cdot 12 \\cdot 16 = '
                        '96\\text{ (m}^2\\text{)}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Hình thoi và hình vuông: Diện tích mảnh vườn hình '
                        'thoi là:\n'
                        '$S = \\dfrac{1}{2} \\cdot 12 \\cdot 16 = 96\\text{ (m}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính diện tích của một hình thoi có độ dài hai đường chéo lần lượt là $10\\text{ cm}$ và '
                 '$14\\text{ cm}$ (đơn vị $\\text{cm}^2$).',
            'answer': ['70'],
            'unit': None,
            'solution': 'Diện tích hình thoi là $S = \\dfrac{1}{2} \\cdot 10 \\cdot 14 = 70\\text{ '
                        '(cm}^2\\text{)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch04-dinh-li-thales',
  'context_title': 'Chương IV: Định lí Thalès',
  'context': 'Chương IV · SGK Toán 8: Định lí Thalès trong tam giác, đường trung bình của tam giác và tính '
             'chất đường phân giác của tam giác.',
  'title': 'Bài 15: Định lí Thalès trong tam giác',
  'icon': '📐',
  'description': 'Tỉ số của hai đoạn thẳng, đoạn thẳng tỉ lệ, định lí Thalès thuận, định lí Thalès đảo và hệ '
                 'quả trong tam giác.',
  'requirements': ['Nhận biết được tỉ số của hai đoạn thẳng và các đoạn thẳng tỉ lệ.',
                   'Giải thích và vận dụng được định lí Thalès thuận, định lí Thalès đảo và hệ quả của định '
                   'lí Thalès trong tam giác.',
                   'Vận dụng kiến thức của **Bài 15: Định lí Thalès trong tam giác** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Định lí Thalès: Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn '
                'lại thì nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ.',
  'theory': "Cho $\\triangle ABC$, đường thẳng $d$ cắt hai cạnh $AB, AC$ lần lượt tại $B', C'$:\n"
            "1. Định lí Thalès thuận: Nếu $B'C' \\parallel BC$ thì $\\dfrac{AB'}{AB} = \\dfrac{AC'}{AC}$; "
            "$\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$; $\\dfrac{B'B}{AB} = \\dfrac{C'C}{AC}$.\n"
            "2. Hệ quả của định lí Thalès: Nếu $B'C' \\parallel BC$ thì $\\dfrac{AB'}{AB} = \\dfrac{AC'}{AC} "
            "= \\dfrac{B'C'}{BC}$.\n"
            '3. Định lí Thalès đảo: Nếu một đường thẳng cắt hai cạnh của một tam giác và định ra trên hai '
            "cạnh này những đoạn thẳng tương ứng tỉ lệ ($\\dfrac{AB'}{AB} = \\dfrac{AC'}{AC}$ hoặc "
            "$\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$) thì đường thẳng đó song song với cạnh còn lại của tam "
            "giác ($B'C' \\parallel BC$).",
  'formulas': [{'category': "Định lí Thalès và hệ quả trong $\\triangle ABC$ ($B' \\in AB, C' \\in AC$)",
                'items': [{'name': 'Định lí Thalès thuận',
                           'formula': "$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{B'B} = "
                                      "\\dfrac{AC'}{C'C}$"},
                          {'name': 'Hệ quả định lí Thalès',
                           'formula': "$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{AB} = \\dfrac{AC'}{AC} "
                                      "= \\dfrac{B'C'}{BC}$"},
                          {'name': 'Định lí Thalès đảo',
                           'formula': "$\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C} \\Rightarrow B'C' \\parallel "
                                      'BC$'}]}],
  'example': 'Cho $\\triangle ABC$, lấy $M \\in AB, N \\in AC$ sao cho $MN \\parallel BC$. Biết $AM = '
             '4\\text{ cm}, MB = 6\\text{ cm}$ và $AN = 5\\text{ cm}$. Tính độ dài $NC$.',
  'example_answer': 'Trong $\\triangle ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có:\n'
                    '$\\dfrac{AM}{MB} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{4}{6} = \\dfrac{5}{NC} '
                    '\\Rightarrow NC = \\dfrac{6 \\cdot 5}{4} = 7,5\\text{ (cm)}$.',
  'real_life': 'Đo chiều cao của cây cổ thụ hoặc tòa tháp thông qua bóng nắng trên mặt đất cùng thời điểm '
               'với một chiếc cọc tiêu chuẩn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đoạn thẳng $AB = 6\\text{ cm}$ và $CD = 1,5\\text{ dm}$. Tỉ số $\\dfrac{AB}{CD}$ bằng:',
            'options': ['$4$', '$\\dfrac{1}{4}$', '$\\dfrac{2}{5}$', '$\\dfrac{5}{2}$'],
            'answer': 2,
            'solution': 'Đổi về cùng đơn vị: $CD = 1,5\\text{ dm} = 15\\text{ cm}$. Khi đó $\\dfrac{AB}{CD} '
                        '= \\dfrac{6}{15} = \\dfrac{2}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$, đường thẳng $d$ song song với $BC$ cắt $AB, AC$ lần lượt tại $D, E$. '
                 'Theo định lí Thalès, hệ thức nào sau đây đúng?',
            'options': ['$\\dfrac{AD}{AB} = \\dfrac{EC}{AC}$',
                        '$\\dfrac{AD}{AE} = \\dfrac{EC}{DB}$',
                        '$AD \\cdot AE = DB \\cdot EC$',
                        '$\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$'],
            'answer': 3,
            'solution': 'Vì $DE \\parallel BC$ nên theo định lí Thalès: $\\dfrac{AD}{DB} = \\dfrac{AE}{EC}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Định lí Thalès trong tam giác**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Định lí Thalès thuận**?',
            'options': ["$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$",
                        "$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$ (với dấu "
                        'ngược lại)',
                        "$B'C' \\parallel BC \\Rightarrow \\dfrac{B'B}{AB'} = \\dfrac{AC'}{C'C}$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $B'C' \\parallel BC "
                        "\\Rightarrow \\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$"],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Định lí Thalès trong tam giác, **Định lí '
                        "Thalès thuận** được xác định bởi: $B'C' \\parallel BC \\Rightarrow "
                        "\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Định lí Thalès trong tam giác**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Hệ quả định lí Thalès**?',
            'options': ["$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{AB} = \\dfrac{AC'}{AC} = "
                        "\\dfrac{B'C'}{BC}$ (với dấu ngược lại)",
                        "$B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{AB} = \\dfrac{AC'}{AC} = "
                        "\\dfrac{B'C'}{BC}$",
                        "$B'C' \\parallel BC \\Rightarrow \\dfrac{AB}{AB'} = \\dfrac{AC'}{AC} = "
                        "\\dfrac{B'C'}{BC}$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $B'C' \\parallel BC "
                        "\\Rightarrow \\dfrac{AB'}{AB} = \\dfrac{AC'}{AC} = \\dfrac{B'C'}{BC}$"],
            'answer': 1,
            'solution': 'Trong Bài 15: Định lí Thalès trong tam giác, **Hệ quả định lí Thalès** có công '
                        "thức/quy tắc là: $B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{AB} = "
                        "\\dfrac{AC'}{AC} = \\dfrac{B'C'}{BC}$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có $D \\in AB, E \\in AC$ và $DE \\parallel BC$. Biết $AD = 3\\text{ '
                 'cm}, AB = 9\\text{ cm}$ và $BC = 12\\text{ cm}$. Độ dài đoạn thẳng $DE$ là:',
            'options': ['$6\\text{ cm}$', '$3\\text{ cm}$', '$4\\text{ cm}$', '$8\\text{ cm}$'],
            'answer': 2,
            'solution': 'Theo hệ quả của định lí Thalès: $\\dfrac{DE}{BC} = \\dfrac{AD}{AB} \\Rightarrow '
                        '\\dfrac{DE}{12} = \\dfrac{3}{9} = \\dfrac{1}{3} \\Rightarrow DE = 4\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Định lí Thalès trong tam giác**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được tỉ số của hai đoạn thẳng và các đoạn thẳng tỉ lệ. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được tỉ số của hai đoạn thẳng và các đoạn thẳng '
                        'tỉ lệ.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được tỉ số của hai '
                        'đoạn thẳng và các đoạn thẳng tỉ lệ.',
                        'Nhận biết được tỉ số của hai đoạn thẳng và các đoạn thẳng tỉ lệ.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Định lí Thalès trong tam giác: Nhận biết được tỉ '
                        'số của hai đoạn thẳng và các đoạn thẳng tỉ lệ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có $AB = 8\\text{ cm}, AC = 12\\text{ cm}$. Trên cạnh $AB$ lấy điểm '
                 '$M$ sao cho $AM = 2\\text{ cm}$, trên cạnh $AC$ lấy điểm $N$ sao cho $AN = 3\\text{ cm}$. '
                 'Xét các khẳng định sau:',
            'statements': ['Tỉ số $\\dfrac{AM}{AB}$ bằng $\\dfrac{1}{4}$.',
                           'Ta có $\\dfrac{AM}{AB} = \\dfrac{AN}{AC} = \\dfrac{1}{4}$.',
                           'Theo định lí Thalès đảo, đường thẳng $MN$ song song với cạnh $BC$.',
                           'Tỉ số $\\dfrac{MN}{BC}$ bằng $\\dfrac{1}{3}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $MN \\parallel BC$ nên theo hệ quả định lí Thalès: '
                        '$\\dfrac{MN}{BC} = \\dfrac{AM}{AB} = \\dfrac{1}{4}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 15: Định lí Thalès trong '
                 'tam giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được tỉ số của hai đoạn thẳng '
                           'và các đoạn thẳng tỉ lệ.',
                           'Trong **Bài 15: Định lí Thalès trong tam giác**, quy tắc/công thức **Định lí '
                           "Thalès thuận** được viết là: $B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{B'B} "
                           "= \\dfrac{AC'}{C'C}$.",
                           "Nếu áp dụng sai dấu/phép tính thành $B'C' \\parallel BC \\Rightarrow "
                           "\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$ (với dấu ngược lại) thì kết quả của "
                           '**Định lí Thalès thuận** trong **Bài 15: Định lí Thalès trong tam giác** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Cho $\\triangle ABC$, lấy $M \\in AB, N \\in AC$ sao cho $MN '
                           '\\parallel BC$. Biết $AM = 4\\text{ cm}, MB = 6\\text{ cm}$ và $AN = 5\\text{ '
                           'cm}$...”, kết quả giải đúng là: Trong $\\triangle ABC$, vì $MN \\parallel BC$ '
                           'nên theo định lí Thalès ta có...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Định lí Thalès trong tam giác. b) '
                        "**Đúng** theo công thức **Định lí Thalès thuận** ($B'C' \\parallel BC \\Rightarrow "
                        "\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$). c) **Sai** vì công thức đúng của **Định lí "
                        "Thalès thuận** phải là $B'C' \\parallel BC \\Rightarrow \\dfrac{AB'}{B'B} = "
                        "\\dfrac{AC'}{C'C}$ chứ không phải $B'C' \\parallel BC \\Rightarrow "
                        "\\dfrac{AB'}{B'B} = \\dfrac{AC'}{C'C}$ (với dấu ngược lại). d) **Đúng** theo lời "
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Định lí Thalès trong tam giác** để giải bài '
                 'toán sau: Cho $\\triangle ABC$, lấy $M \\in AB, N \\in AC$ sao cho $MN \\parallel BC$. '
                 'Biết $AM = 4\\text{ cm}, MB = 6\\text{ cm}$ và $AN = 5\\text{ cm}$. Tính độ dài $NC$. Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Trong $\\triangle ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có: '
                        '$\\dfrac{AM}{MB} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{4}{6} = \\dfrac{5}{NC} '
                        '\\Rightarrow NC = \\dfrac{6 \\cdot 5}{4} = 7,5\\text{ (cm)}$...',
                        'Trong $\\triangle ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có: '
                        '$\\dfrac{AM}{MB} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{4}{6} = \\dfrac{5}{NC} '
                        '\\Rightarrow NC = \\dfrac{6 : 5}{4} = 7,5\\text{ (cm)}$...',
                        'Trong $\\triangle ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có: '
                        '$\\dfrac{MB}{AM} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{4}{6} = \\dfrac{5}{NC} '
                        '\\Rightarrow NC = \\dfrac{6 \\cdot 5}{4} = 7,5\\text{ (cm)}$...',
                        'Trong $\\triangle ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có: '
                        '$\\dfrac{AM}{MB} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{8}{6} = \\dfrac{5}{NC} '
                        '\\Rightarrow NC = \\dfrac{6 \\cdot 5}{4} = 7,5\\text{ (cm)}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Định lí Thalès trong tam giác: Trong $\\triangle '
                        'ABC$, vì $MN \\parallel BC$ nên theo định lí Thalès ta có:\n'
                        '$\\dfrac{AM}{MB} = \\dfrac{AN}{NC} \\Rightarrow \\dfrac{4}{6} = \\dfrac{5}{NC} '
                        '\\Rightarrow NC = \\dfrac{6 \\cdot 5}{4} = 7,5\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ có $M \\in AB, N \\in AC$ sao cho $MN \\parallel BC$. Biết $AM = '
                 '6\\text{ cm}, MB = 3\\text{ cm}$ và $NC = 4\\text{ cm}$. Tính độ dài đoạn thẳng $AN$ (đơn '
                 'vị $\\text{cm}$).',
            'answer': ['8'],
            'unit': None,
            'solution': 'Theo định lí Thalès: $\\dfrac{AN}{NC} = \\dfrac{AM}{MB} \\Rightarrow \\dfrac{AN}{4} '
                        '= \\dfrac{6}{3} = 2 \\Rightarrow AN = 8\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch04-dinh-li-thales',
  'context_title': 'Chương IV: Định lí Thalès',
  'context': 'Chương IV · SGK Toán 8: Định lí Thalès trong tam giác, đường trung bình của tam giác và tính '
             'chất đường phân giác của tam giác.',
  'title': 'Bài 16: Đường trung bình của tam giác',
  'icon': '➖',
  'description': 'Định nghĩa và tính chất đường trung bình của tam giác.',
  'requirements': ['Nhận biết được đường trung bình của một tam giác (một tam giác có $3$ đường trung bình).',
                   'Giải thích và vận dụng được tính chất đường trung bình của tam giác (song song với cạnh '
                   'thứ ba và bằng nửa cạnh ấy).',
                   'Vận dụng kiến thức của **Bài 16: Đường trung bình của tam giác** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Đường trung bình của tam giác là đoạn thẳng nối trung điểm hai cạnh của tam giác. Đường '
                'trung bình của tam giác thì song song với cạnh thứ ba và bằng nửa cạnh ấy.',
  'theory': '1. Định lí đường trung bình: Trong $\\triangle ABC$, nếu $M$ là trung điểm của $AB$ và $N$ là '
            'trung điểm của $AC$ thì $MN$ là đường trung bình của $\\triangle ABC$, khi đó:\n'
            '$MN \\parallel BC$ và $MN = \\dfrac{1}{2}BC$.\n'
            '2. Hệ quả quan trọng: Nếu một đường thẳng đi qua trung điểm một cạnh của tam giác và song song '
            'với cạnh thứ hai thì nó đi qua trung điểm của cạnh thứ ba.',
  'formulas': [{'category': 'Tính chất đường trung bình của $\\triangle ABC$',
                'items': [{'name': 'Với $M, N$ là trung điểm của $AB, AC$',
                           'formula': '$MN \\parallel BC$ và $MN = \\dfrac{1}{2}BC$'},
                          {'name': 'Tính cạnh đáy từ đường trung bình', 'formula': '$BC = 2 \\cdot MN$'}]}],
  'example': 'Để đo khoảng cách giữa hai địa điểm $B$ và $C$ bị ngăn cách bởi một cái hồ, người ta chọn điểm '
             '$A$ trên bờ và xác định trung điểm $M$ của $AB$, trung điểm $N$ của $AC$. Đo được $MN = '
             '42\\text{ m}$, hãy tính khoảng cách $BC$.',
  'example_answer': 'Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của '
                    '$\\triangle ABC$.\n'
                    'Do đó $MN = \\dfrac{1}{2}BC \\Rightarrow BC = 2 \\cdot MN = 2 \\cdot 42 = 84\\text{ '
                    '(m)}$.',
  'real_life': 'Đo khoảng cách giữa hai vị trí bị chướng ngại vật che khuất và thiết kế thanh ngang giữa của '
               'thang chữ A bằng một nửa khoảng cách hai chân thang.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đường trung bình của tam giác là đoạn thẳng nối:',
            'options': ['Một đỉnh với trung điểm cạnh đối diện',
                        'Một đỉnh và vuông góc với cạnh đối diện',
                        'Hai đỉnh bất kì của tam giác',
                        'Trung điểm hai cạnh của tam giác'],
            'answer': 3,
            'solution': 'Đoạn thẳng nối trung điểm hai cạnh của tam giác là đường trung bình của tam giác.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có $D, E$ lần lượt là trung điểm của $AB, AC$. Biết $BC = 14\\text{ '
                 'cm}$, độ dài đoạn thẳng $DE$ bằng:',
            'options': ['$7\\text{ cm}$', '$28\\text{ cm}$', '$14\\text{ cm}$', '$3,5\\text{ cm}$'],
            'answer': 0,
            'solution': '$DE$ là đường trung bình của $\\triangle ABC$ nên $DE = \\dfrac{1}{2}BC = '
                        '\\dfrac{14}{2} = 7\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Đường trung bình của tam giác**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Với $M, N$ là trung điểm của $AB, AC$**?',
            'options': ['$MN \\parallel BC$ và $MN = \\dfrac{2}{2}BC$',
                        '$MN \\parallel BC$ và $MN = \\dfrac{1}{2}BC$',
                        '$MN \\parallel BC$ và $MN = \\dfrac{2}{1}BC$',
                        '$BC = 2 \\cdot MN$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Đường trung bình của tam giác, **Với $M, N$ là '
                        'trung điểm của $AB, AC$** được xác định bởi: $MN \\parallel BC$ và $MN = '
                        '\\dfrac{1}{2}BC$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Đường trung bình của tam giác**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tính cạnh đáy từ đường trung bình**?',
            'options': ['$BC = 2 : MN$', '$BC = 1 \\cdot MN$', '$BC = 2 \\cdot MN$', '$BC = 4 \\cdot MN$'],
            'answer': 2,
            'solution': 'Trong Bài 16: Đường trung bình của tam giác, **Tính cạnh đáy từ đường trung bình** '
                        'có công thức/quy tắc là: $BC = 2 \\cdot MN$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có chu vi bằng $30\\text{ cm}$. Gọi $M, N, P$ lần lượt là trung điểm '
                 'của các cạnh $AB, BC, CA$. Chu vi của $\\triangle MNP$ bằng:',
            'options': ['$60\\text{ cm}$', '$10\\text{ cm}$', '$30\\text{ cm}$', '$15\\text{ cm}$'],
            'answer': 3,
            'solution': 'Ba cạnh $MN, NP, PM$ là ba đường trung bình của $\\triangle ABC$ nên chu vi '
                        '$\\triangle MNP$ bằng một nửa chu vi $\\triangle ABC$: $30 : 2 = 15\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Đường trung bình của tam giác**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được đường trung bình của một tam giác (một tam giác có $3$ đường trung '
                        'bình).',
                        'Nhận biết được đường trung bình của một tam giác (một tam giác có $4$ đường trung '
                        'bình).',
                        'Nhận biết được đường trung bình của một tam giác (một tam giác có $2$ đường trung '
                        'bình).',
                        'Nhận biết được đường trung bình của một tam giác (một tam giác có $6$ đường trung '
                        'bình).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Đường trung bình của tam giác: Nhận biết được '
                        'đường trung bình của một tam giác (một tam giác có $3$ đường trung bình).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$, gọi $M$ là trung điểm của $AB$. Qua $M$ kẻ đường thẳng song song với '
                 '$BC$ cắt $AC$ tại $N$. Xét các khẳng định sau:',
            'statements': ['Điểm $N$ là trung điểm của cạnh $AC$.',
                           'Đoạn thẳng $MN$ là đường trung bình của $\\triangle ABC$.',
                           'Độ dài đoạn thẳng $BC$ bằng $2MN$.',
                           'Tứ giác $BMNC$ là một hình bình hành.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì tứ giác $BMNC$ có $MN \\parallel BC$ nhưng $MN = '
                        '\\dfrac{1}{2}BC \\neq BC$ nên chỉ là hình thang, không phải hình bình hành.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 16: Đường trung bình của '
                 'tam giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đường trung bình của một '
                           'tam giác (một tam giác có $3$ đường trung bình).',
                           'Trong **Bài 16: Đường trung bình của tam giác**, quy tắc/công thức **Với $M, N$ '
                           'là trung điểm của $AB, AC$** được viết là: $MN \\parallel BC$ và $MN = '
                           '\\dfrac{1}{2}BC$.',
                           'Nếu áp dụng sai dấu/phép tính thành $MN \\parallel BC$ và $MN = \\dfrac{2}{2}BC$ '
                           'thì kết quả của **Với $M, N$ là trung điểm của $AB, AC$** trong **Bài 16: Đường '
                           'trung bình của tam giác** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Để đo khoảng cách giữa hai địa điểm $B$ và $C$ bị ngăn cách '
                           'bởi một cái hồ, người ta chọn điểm $A$ trên bờ và xác định trung điểm $M$ c...”, '
                           'kết quả giải đúng là: Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là '
                           'đường trung bình của $\\triangle ABC$. Do đó $MN = \\dfrac{1}{2}BC \\Rightarrow '
                           'BC = 2 \\cdot MN = 2 \\cdot 42 = 84\\text{ (m)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Đường trung bình của tam giác. b) '
                        '**Đúng** theo công thức **Với $M, N$ là trung điểm của $AB, AC$** ($MN \\parallel '
                        'BC$ và $MN = \\dfrac{1}{2}BC$). c) **Sai** vì công thức đúng của **Với $M, N$ là '
                        'trung điểm của $AB, AC$** phải là $MN \\parallel BC$ và $MN = \\dfrac{1}{2}BC$ chứ '
                        'không phải $MN \\parallel BC$ và $MN = \\dfrac{2}{2}BC$. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Đường trung bình của tam giác** để giải bài '
                 'toán sau: Để đo khoảng cách giữa hai địa điểm $B$ và $C$ bị ngăn cách bởi một cái hồ, '
                 'người ta chọn điểm $A$ trên bờ và xác định trung điểm $M$ của $AB$, trung điểm $N$ của '
                 '$AC$. Đo được $MN = 42\\text{ m}$, hãy tính khoảng cách $BC$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của '
                        '$\\triangle ABC$. Do đó $MN = \\dfrac{1}{2}BC \\Rightarrow BC = 2 : MN = 2 \\cdot '
                        '42 = 84\\text{ (m)}$...',
                        'Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của '
                        '$\\triangle ABC$. Do đó $MN = \\dfrac{1}{2}BC \\Rightarrow BC = 2 \\cdot MN = 2 '
                        '\\cdot 42 = 84\\text{ (m)}$...',
                        'Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của '
                        '$\\triangle ABC$. Do đó $MN = \\dfrac{2}{1}BC \\Rightarrow BC = 2 \\cdot MN = 2 '
                        '\\cdot 42 = 84\\text{ (m)}$...',
                        'Vì $M, N$ lần lượt là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của '
                        '$\\triangle ABC$. Do đó $MN = \\dfrac{2}{2}BC \\Rightarrow BC = 2 \\cdot MN = 2 '
                        '\\cdot 42 = 84\\text{ (m)}$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Đường trung bình của tam giác: Vì $M, N$ lần lượt là '
                        'trung điểm của $AB, AC$ nên $MN$ là đường trung bình của $\\triangle ABC$.\n'
                        'Do đó $MN = \\dfrac{1}{2}BC \\Rightarrow BC = 2 \\cdot MN = 2 \\cdot 42 = 84\\text{ '
                        '(m)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ có $M, N$ lần lượt là trung điểm của $AB, AC$. Biết $MN = 9\\text{ '
                 'cm}$, tính độ dài cạnh $BC$ (đơn vị $\\text{cm}$).',
            'answer': ['18'],
            'unit': None,
            'solution': 'Vì $MN$ là đường trung bình của $\\triangle ABC$ nên $BC = 2 \\cdot MN = 2 \\cdot 9 '
                        '= 18\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch04-dinh-li-thales',
  'context_title': 'Chương IV: Định lí Thalès',
  'context': 'Chương IV · SGK Toán 8: Định lí Thalès trong tam giác, đường trung bình của tam giác và tính '
             'chất đường phân giác của tam giác.',
  'title': 'Bài 17: Tính chất đường phân giác của tam giác',
  'icon': '✂️',
  'description': 'Định lí tính chất đường phân giác của tam giác và vận dụng tính độ dài các đoạn thẳng.',
  'requirements': ['Giải thích được định lí về tính chất đường phân giác trong của tam giác.',
                   'Vận dụng được tính chất đường phân giác của tam giác để tính độ dài đoạn thẳng và chứng '
                   'minh hệ thức tỉ lệ.',
                   'Vận dụng kiến thức của **Bài 17: Tính chất đường phân giác của tam giác** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Trong một tam giác, đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng tỉ '
                'lệ với hai cạnh kề hai đoạn ấy.',
  'theory': '1. Định lí tính chất đường phân giác: Trong $\\triangle ABC$, nếu $AD$ là đường phân giác của '
            'góc $\\widehat{BAC}$ ($D \\in BC$) thì:\n'
            '$\\dfrac{DB}{DC} = \\dfrac{AB}{AC}$ hay $\\dfrac{DB}{AB} = \\dfrac{DC}{AC}$.\n'
            '2. Kết hợp tính chất dãy tỉ số bằng nhau: Khi biết $AB, AC$ và độ dài cả cạnh $BC = DB + DC$, '
            'ta tính được:\n'
            '$\\dfrac{DB}{AB} = \\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{BC}{AB + AC}$.',
  'formulas': [{'category': 'Tính chất đường phân giác $AD$ trong $\\triangle ABC$ ($D \\in BC$)',
                'items': [{'name': 'Hệ thức tỉ lệ cơ bản',
                           'formula': '$\\dfrac{DB}{DC} = \\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = '
                                      '\\dfrac{DC}{AC}$'},
                          {'name': 'Tính $DB, DC$ theo $BC$',
                           'formula': '$DB = \\dfrac{AB}{AB + AC} \\cdot BC; \\quad DC = \\dfrac{AC}{AB + '
                                      'AC} \\cdot BC$'}]}],
  'example': 'Cho $\\triangle ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ cm}, BC = 10\\text{ cm}$ và đường '
             'phân giác $AD$ ($D \\in BC$). Tính độ dài các đoạn thẳng $DB$ và $DC$.',
  'example_answer': 'Theo tính chất đường phân giác của $\\triangle ABC$, ta có:\n'
                    '$\\dfrac{DB}{AB} = \\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{10}{6 + 9} = '
                    '\\dfrac{10}{15} = \\dfrac{2}{3}$.\n'
                    'Suy ra $DB = 6 \\cdot \\dfrac{2}{3} = 4\\text{ (cm)}$ và $DC = 9 \\cdot \\dfrac{2}{3} = '
                    '6\\text{ (cm)}$.',
  'real_life': 'Chia một mảnh đất hình tam giác từ một đỉnh sao cho mặt tiền chia thành hai phần tỉ lệ với '
               'hai cạnh bên.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có $AD$ là tia phân giác của góc $\\widehat{A}$ ($D \\in BC$). Hệ '
                 'thức nào sau đây là đúng?',
            'options': ['$\\dfrac{DB}{DC} = \\dfrac{AB}{AC}$',
                        '$\\dfrac{DB}{DC} = \\dfrac{AC}{AB}$',
                        '$\\dfrac{AB}{DB} = \\dfrac{BC}{AC}$',
                        '$DB = DC$'],
            'answer': 0,
            'solution': 'Theo tính chất đường phân giác của tam giác: $\\dfrac{DB}{DC} = \\dfrac{AB}{AC}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle MNP$ có đường phân giác $MK$ ($K \\in NP$). Biết $MN = 5\\text{ cm}, MP = '
                 '8\\text{ cm}$, tỉ số $\\dfrac{KN}{KP}$ bằng:',
            'options': ['$\\dfrac{8}{5}$', '$\\dfrac{5}{8}$', '$\\dfrac{5}{13}$', '$\\dfrac{8}{13}$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{KN}{KP} = \\dfrac{MN}{MP} = \\dfrac{5}{8}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Tính chất đường phân giác của tam giác**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Hệ thức tỉ lệ cơ bản**?',
            'options': ['$\\dfrac{DB}{DC} = \\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC}$ (với dấu ngược lại)',
                        '$\\dfrac{DC}{DB} = \\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC}$',
                        '$\\dfrac{DB}{DC} = \\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{DB}{DC} = '
                        '\\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Tính chất đường phân giác của tam giác, **Hệ '
                        'thức tỉ lệ cơ bản** được xác định bởi: $\\dfrac{DB}{DC} = \\dfrac{AB}{AC} '
                        '\\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Tính chất đường phân giác của tam giác**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Tính $DB, DC$ theo $BC$**?',
            'options': ['$DB = \\dfrac{AB}{AB - AC} \\cdot BC; \\quad DC = \\dfrac{AC}{AB + AC} \\cdot BC$',
                        '$DB = \\dfrac{AB + AC}{AB} \\cdot BC; \\quad DC = \\dfrac{AC}{AB + AC} \\cdot BC$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $DB = \\dfrac{AB}{AB + AC} '
                        '\\cdot BC; \\quad DC = \\dfrac{AC}{AB + AC} \\cdot BC$',
                        '$DB = \\dfrac{AB}{AB + AC} \\cdot BC; \\quad DC = \\dfrac{AC}{AB + AC} \\cdot BC$'],
            'answer': 3,
            'solution': 'Trong Bài 17: Tính chất đường phân giác của tam giác, **Tính $DB, DC$ theo $BC$** '
                        'có công thức/quy tắc là: $DB = \\dfrac{AB}{AB + AC} \\cdot BC; \\quad DC = '
                        '\\dfrac{AC}{AB + AC} \\cdot BC$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ có đường phân giác $AD$ ($D \\in BC$). Biết $AB = 4\\text{ cm}, AC = '
                 '6\\text{ cm}$ và $BD = 2\\text{ cm}$. Độ dài đoạn thẳng $CD$ là:',
            'options': ['$3\\text{ cm}$', '$4\\text{ cm}$', '$5\\text{ cm}$', '$2\\text{ cm}$'],
            'answer': 0,
            'solution': 'Ta có $\\dfrac{BD}{CD} = \\dfrac{AB}{AC} \\Rightarrow \\dfrac{2}{CD} = '
                        '\\dfrac{4}{6} \\Rightarrow CD = 3\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Tính chất đường phân giác của tam giác**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Giải thích được định lí về tính chất đường phân giác trong của tam giác. (với dấu '
                        'ngược lại)',
                        'Giải thích được định lí về tính chất đường phân giác trong của tam giác.',
                        'Đảo ngược vế của quy tắc: Giải thích được định lí về tính chất đường phân giác '
                        'trong của tam giác.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải thích được định lí về tính '
                        'chất đường phân giác trong của tam giác.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Tính chất đường phân giác của tam giác: Giải '
                        'thích được định lí về tính chất đường phân giác trong của tam giác.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có $AB = 8\\text{ cm}, AC = 12\\text{ cm}, BC = 15\\text{ cm}$ và '
                 'đường phân giác $AD$ ($D \\in BC$). Xét các khẳng định sau:',
            'statements': ['Tỉ số $\\dfrac{DB}{DC} = \\dfrac{8}{12} = \\dfrac{2}{3}$.',
                           'Ta có $\\dfrac{DB}{2} = \\dfrac{DC}{3} = \\dfrac{BC}{5} = 3$.',
                           'Độ dài đoạn thẳng $DB = 6\\text{ cm}$ và $DC = 9\\text{ cm}$.',
                           'Điểm $D$ là trung điểm của cạnh $BC$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $DB = 6\\text{ cm} \\neq DC = 9\\text{ cm}$ (phân giác '
                        'chỉ đi qua trung điểm khi tam giác cân tại $A$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 17: Tính chất đường phân '
                 'giác của tam giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải thích được định lí về tính chất '
                           'đường phân giác trong của tam giác.',
                           'Trong **Bài 17: Tính chất đường phân giác của tam giác**, quy tắc/công thức **Hệ '
                           'thức tỉ lệ cơ bản** được viết là: $\\dfrac{DB}{DC} = \\dfrac{AB}{AC} '
                           '\\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{DB}{DC} = \\dfrac{AB}{AC} '
                           '\\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$ (với dấu ngược lại) thì kết '
                           'quả của **Hệ thức tỉ lệ cơ bản** trong **Bài 17: Tính chất đường phân giác của '
                           'tam giác** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho $\\triangle ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ '
                           'cm}, BC = 10\\text{ cm}$ và đường phân giác $AD$ ($D \\in BC$). Tính độ dài các '
                           'đo...”, kết quả giải đúng là: Theo tính chất đường phân giác của $\\triangle '
                           'ABC$, ta có: $\\dfrac{DB}{AB} = \\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = '
                           '\\dfrac{10}{6 + 9} = \\dfrac{10}{15} = \\dfrac{2}{3}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Tính chất đường phân giác của tam '
                        'giác. b) **Đúng** theo công thức **Hệ thức tỉ lệ cơ bản** ($\\dfrac{DB}{DC} = '
                        '\\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$). c) **Sai** vì '
                        'công thức đúng của **Hệ thức tỉ lệ cơ bản** phải là $\\dfrac{DB}{DC} = '
                        '\\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = \\dfrac{DC}{AC}$ chứ không phải '
                        '$\\dfrac{DB}{DC} = \\dfrac{AB}{AC} \\Leftrightarrow \\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC}$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Tính chất đường phân giác của tam giác** để '
                 'giải bài toán sau: Cho $\\triangle ABC$ có $AB = 6\\text{ cm}, AC = 9\\text{ cm}, BC = '
                 '10\\text{ cm}$ và đường phân giác $AD$ ($D \\in BC$). Tính độ dài các đoạn thẳng $DB$ và '
                 '$DC$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Theo tính chất đường phân giác của $\\triangle ABC$, ta có: $\\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC} = \\dfrac{DB - DC}{AB + AC} = \\dfrac{10}{6 + 9} = \\dfrac{10}{15} '
                        '= \\dfrac{2}{3}$...',
                        'Theo tính chất đường phân giác của $\\triangle ABC$, ta có: $\\dfrac{AB}{DB} = '
                        '\\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{10}{6 + 9} = \\dfrac{10}{15} '
                        '= \\dfrac{2}{3}$...',
                        'Theo tính chất đường phân giác của $\\triangle ABC$, ta có: $\\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{10}{6 + 9} = \\dfrac{10}{15} '
                        '= \\dfrac{2}{3}$...',
                        'Theo tính chất đường phân giác của $\\triangle ABC$, ta có: $\\dfrac{DB}{AB} = '
                        '\\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{20}{6 + 9} = \\dfrac{10}{15} '
                        '= \\dfrac{2}{3}$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Tính chất đường phân giác của tam giác: Theo tính '
                        'chất đường phân giác của $\\triangle ABC$, ta có:\n'
                        '$\\dfrac{DB}{AB} = \\dfrac{DC}{AC} = \\dfrac{DB + DC}{AB + AC} = \\dfrac{10}{6 + 9} '
                        '= \\dfrac{10}{15} = \\dfrac{2}{3}$.\n'
                        'Suy ra $DB = 6 \\cdot \\dfrac{2}{3} = 4\\text{ (cm)}$ và $DC = 9 \\cdot '
                        '\\dfrac{2}{3} = 6\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ có $AB = 5\\text{ cm}, AC = 7\\text{ cm}, BC = 18\\text{ cm}$. Đường '
                 'phân giác góc $\\widehat{A}$ cắt $BC$ tại $D$. Tính độ dài đoạn thẳng $BD$ (đơn vị '
                 '$\\text{cm}$).',
            'answer': ['7,5', '7.5'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{BD}{5} = \\dfrac{CD}{7} = \\dfrac{18}{5 + 7} = 1,5 \\Rightarrow BD = '
                        '5 \\cdot 1,5 = 7,5\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch05-du-lieu-bieu-do',
  'context_title': 'Chương V: Dữ liệu và biểu đồ',
  'context': 'Chương V · SGK Toán 8: Thu thập, phân loại dữ liệu (rời rạc, liên tục), lựa chọn biểu đồ và '
             'phân tích số liệu thống kê.',
  'title': 'Bài 18: Thu thập và phân loại dữ liệu',
  'icon': '📊',
  'description': 'Thu thập dữ liệu trực tiếp, gián tiếp và phân loại số liệu rời rạc, số liệu liên tục.',
  'requirements': ['Thực hiện và lí giải được việc thu thập dữ liệu bằng phương pháp trực tiếp hay gián '
                   'tiếp.',
                   'Phân biệt được dữ liệu định량 rời rạc và dữ liệu định lượng liên tục.',
                   'Nhận biết được tính hợp lí và tính đại diện của dữ liệu thống kê.'],
  'definition': 'Dữ liệu là số (số liệu) được chia thành hai loại: Số liệu rời rạc (nhận các giá trị rời '
                'rạc, thường là kết quả của phép đếm) và số liệu liên tục (có thể nhận mọi giá trị thực '
                'trong một khoảng nào đó, thường là kết quả của phép đo).',
  'theory': '1. Phương pháp thu thập dữ liệu:\n'
            '- Thu thập trực tiếp: Quan sát, làm thí nghiệm, lập bảng hỏi, phỏng vấn.\n'
            '- Thu thập gián tiếp: Tra cứu từ sách báo, Internet, Niên giám thống kê.\n'
            '2. Phân loại chi tiết dữ liệu:\n'
            '- Số liệu rời rạc: Số học sinh trong lớp, số bàn thắng trong trận đấu, cỡ giày.\n'
            '- Số liệu liên tục: Chiều cao, cân nặng, thời gian chạy $100\\text{ m}$, nhiệt độ không khí.',
  'formulas': [{'category': 'Sơ đồ phân loại dữ liệu lớp 8',
                'items': [{'name': 'Số liệu (Dữ liệu định lượng)',
                           'formula': 'Chia thành: Số liệu rời rạc (đếm) và Số liệu liên tục (đo lường)'},
                          {'name': 'Dữ liệu không là số (Định tính)',
                           'formula': 'Chia thành: Có thể sắp thứ tự và Không thể sắp thứ tự'}]}],
  'example': 'Phân loại các dữ liệu sau: a) Số lượng huy chương của các đoàn thể thao; b) Chiều cao của các '
             'cây thông trong vườn ươm.',
  'example_answer': 'a) Số lượng huy chương là số tự nhiên thu được từ phép đếm nên là số liệu rời rạc.\n'
                    'b) Chiều cao của cây có thể nhận giá trị thực bất kì trong một khoảng (do đo đạc) nên '
                    'là số liệu liên tục.',
  'real_life': 'Thu thập dữ liệu lượng mưa từ cổng thông tin Tổng cục Thống kê (gián tiếp, số liệu liên tục) '
               'hoặc đếm số xe ô tô qua trạm thu phí (trực tiếp, số liệu rời rạc).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dữ liệu nào sau đây là số liệu liên tục?',
            'options': ['Số lượng thành viên trong mỗi gia đình ở tổ dân phố',
                        'Cân nặng (tính theo $\\text{kg}$) của các bạn học sinh lớp 8A',
                        'Số quyển sách mỗi học sinh đọc trong mùa hè',
                        'Số bàn thắng ghi được của các đội bóng'],
            'answer': 1,
            'solution': 'Cân nặng là kết quả của phép đo và có thể nhận giá trị thực bất kì trong một khoảng '
                        'nên là số liệu liên tục.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Dữ liệu nào sau đây là số liệu rời rạc?',
            'options': ['Thời gian hoàn thành cự li chạy $200\\text{ m}$ của các vận động viên',
                        'Chiều dài của các chiếc lá cây bàng',
                        'Số chiếc máy tính có trong mỗi phòng thực hành của trường',
                        'Nhiệt độ cơ thể của bệnh nhân đo trong ngày'],
            'answer': 2,
            'solution': 'Số chiếc máy tính nhận các giá trị nguyên không âm rời rạc nên là số liệu rời rạc.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Thu thập và phân loại dữ liệu**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Số liệu (Dữ liệu định lượng)**?',
            'options': ['Chia thành: Số liệu rời rạc (đếm) và Số liệu liên tục (đo lường) (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Chia thành: Số liệu rời rạc (đếm) và Số liệu liên tục (đo '
                        'lường)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chia thành: Số liệu rời rạc '
                        '(đếm) và Số liệu liên tục (đo lường)',
                        'Chia thành: Số liệu rời rạc (đếm) và Số liệu liên tục (đo lường)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 18: Thu thập và phân loại dữ liệu, **Số liệu (Dữ '
                        'liệu định lượng)** được xác định bởi: Chia thành: Số liệu rời rạc (đếm) và Số liệu '
                        'liên tục (đo lường).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Thu thập và phân loại dữ liệu**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Dữ liệu không là số (Định tính)**?',
            'options': ['Chia thành: Có thể sắp thứ tự và Không thể sắp thứ tự',
                        'Chia thành: Có thể sắp thứ tự và Không thể sắp thứ tự (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Chia thành: Có thể sắp thứ tự và Không thể sắp thứ tự',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Chia thành: Có thể sắp thứ tự '
                        'và Không thể sắp thứ tự'],
            'answer': 0,
            'solution': 'Trong Bài 18: Thu thập và phân loại dữ liệu, **Dữ liệu không là số (Định tính)** có '
                        'công thức/quy tắc là: Chia thành: Có thể sắp thứ tự và Không thể sắp thứ tự.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bạn An tra cứu dân số của các tỉnh Đồng bằng sông Cửu Long trên trang web của Tổng cục '
                 'Thống kê. Phương pháp thu thập dữ liệu của An là:',
            'options': ['Thu thập trực tiếp bằng thực nghiệm',
                        'Thu thập gián tiếp',
                        'Thu thập trực tiếp bằng phỏng vấn',
                        'Thu thập trực tiếp bằng quan sát'],
            'answer': 1,
            'solution': 'Lấy dữ liệu từ nguồn có sẵn (trang web Tổng cục Thống kê) là phương pháp thu thập '
                        'gián tiếp.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 18: Thu thập và phân loại dữ liệu**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Thực hiện và lí giải được việc thu thập dữ liệu bằng phương pháp trực tiếp hay gián '
                        'tiếp. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện và lí giải được việc thu thập dữ liệu bằng '
                        'phương pháp trực tiếp hay gián tiếp.',
                        'Thực hiện và lí giải được việc thu thập dữ liệu bằng phương pháp trực tiếp hay gián '
                        'tiếp.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện và lí giải được việc '
                        'thu thập dữ liệu bằng phương pháp trực tiếp hay gián tiếp.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 18: Thu thập và phân loại dữ liệu: Thực hiện và lí '
                        'giải được việc thu thập dữ liệu bằng phương pháp trực tiếp hay gián tiếp.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về phân loại dữ liệu:',
            'statements': ['Số đôi giày bán được mỗi ngày của một cửa hàng là số liệu rời rạc.',
                           'Lượng nước tiêu thụ (tính bằng $\\text{m}^3$) của các hộ gia đình là số liệu '
                           'liên tục.',
                           'Xếp loại học lực (Tốt, Khá, Đạt, Chưa đạt) là số liệu rời rạc.',
                           'Khi đo chiều cao học sinh lớp 8 (tính bằng $\\text{cm}$), giá trị $450\\text{ '
                           'cm}$ là dữ liệu không hợp lí.'],
            'answer': [True, True, False, True],
            'solution': 'a), b), d) Đúng. c) Sai vì xếp loại học lực là dữ liệu không là số (định tính có '
                        'thể sắp thứ tự).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 18: Thu thập và phân loại '
                 'dữ liệu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện và lí giải được việc thu thập '
                           'dữ liệu bằng phương pháp trực tiếp hay gián tiếp.',
                           'Trong **Bài 18: Thu thập và phân loại dữ liệu**, quy tắc/công thức **Số liệu (Dữ '
                           'liệu định lượng)** được viết là: Chia thành: Số liệu rời rạc (đếm) và Số liệu '
                           'liên tục (đo lường).',
                           'Nếu áp dụng sai dấu/phép tính thành Chia thành: Số liệu rời rạc (đếm) và Số liệu '
                           'liên tục (đo lường) (với dấu ngược lại) thì kết quả của **Số liệu (Dữ liệu định '
                           'lượng)** trong **Bài 18: Thu thập và phân loại dữ liệu** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Phân loại các dữ liệu sau: a) Số lượng huy chương của các '
                           'đoàn thể thao; b) Chiều cao của các cây thông trong vườn ươm.”, kết quả giải '
                           'đúng là: a) Số lượng huy chương là số tự nhiên thu được từ phép đếm nên là số '
                           'liệu rời rạc. b) Chiều cao của cây có thể nhận giá trị thực bất kì...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Thu thập và phân loại dữ liệu. b) '
                        '**Đúng** theo công thức **Số liệu (Dữ liệu định lượng)** (Chia thành: Số liệu rời '
                        'rạc (đếm) và Số liệu liên tục (đo lường)). c) **Sai** vì công thức đúng của **Số '
                        'liệu (Dữ liệu định lượng)** phải là Chia thành: Số liệu rời rạc (đếm) và Số liệu '
                        'liên tục (đo lường) chứ không phải Chia thành: Số liệu rời rạc (đếm) và Số liệu '
                        'liên tục (đo lường) (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 18: Thu thập và phân loại dữ liệu** để giải bài '
                 'toán sau: Phân loại các dữ liệu sau: a) Số lượng huy chương của các đoàn thể thao; b) '
                 'Chiều cao của các cây thông trong vườn ươm. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        'a) Số lượng huy chương là số tự nhiên thu được từ phép đếm nên là số liệu rời rạc. '
                        'b) Chiều cao của cây có thể nhận giá trị thực bất kì trong một khoả...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Thu thập và phân loại dữ liệu: a) Số lượng huy '
                        'chương là số tự nhiên thu được từ phép đếm nên là số liệu rời rạc.\n'
                        'b) Chiều cao của cây có thể nhận giá trị thực bất kì trong một khoảng (do đo đạc) '
                        'nên là số liệu liên tục.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong các dữ liệu sau: (1) Số học sinh giỏi của các lớp; (2) Chiều cao của học sinh; (3) '
                 'Số xe đạp trong nhà xe; (4) Số bàn học trong mỗi phòng; (5) Nhiệt độ nước đun sôi. Có bao '
                 'nhiêu dữ liệu là số liệu rời rạc?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Các dữ liệu (1), (3), (4) là số liệu rời rạc (đếm số lượng); còn (2) và (5) là số '
                        'liệu liên tục. Vậy có $3$ dữ liệu là số liệu rời rạc.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch05-du-lieu-bieu-do',
  'context_title': 'Chương V: Dữ liệu và biểu đồ',
  'context': 'Chương V · SGK Toán 8: Thu thập, phân loại dữ liệu (rời rạc, liên tục), lựa chọn biểu đồ và '
             'phân tích số liệu thống kê.',
  'title': 'Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ',
  'icon': '📊',
  'description': 'Lựa chọn dạng biểu đồ thích hợp (cột, cột kép, hình quạt tròn, đoạn thẳng) và chuyển đổi '
                 'dữ liệu giữa bảng và biểu đồ.',
  'requirements': ['Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp (biểu đồ cột, cột kép, '
                   'hình quạt tròn, đoạn thẳng).',
                   'Chuyển đổi được dữ liệu từ dạng biểu diễn này sang dạng biểu diễn khác.',
                   'Vận dụng kiến thức của **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Mỗi dạng biểu đồ có ưu thế riêng: Biểu đồ cột dùng để so sánh các nhóm; biểu đồ cột kép '
                'dùng để so sánh hai bộ dữ liệu tương ứng; biểu đồ hình quạt tròn dùng để biểu diễn tỉ lệ '
                'phần trăm các phần trong tổng thể; biểu đồ đoạn thẳng dùng để biểu diễn xu thế theo thời '
                'gian.',
  'theory': 'Nguyên tắc lựa chọn biểu đồ phù hợp:\n'
            '1. Biểu đồ cột: So sánh độ lớn của các đối tượng khác nhau.\n'
            '2. Biểu đồ cột kép: So sánh trực tiếp hai tập dữ liệu cùng loại trên các tiêu chí giống nhau.\n'
            '3. Biểu đồ hình quạt tròn: Thể hiện cơ cấu, tỉ lệ phần trăm của từng thành phần trong tổng thể '
            '$100\\%$.\n'
            '4. Biểu đồ đoạn thẳng: Thể hiện sự biến đổi (tăng, giảm) của một đại lượng qua các mốc thời '
            'gian.',
  'formulas': [{'category': 'Chuyển đổi số liệu khi lập biểu đồ',
                'items': [{'name': 'Tính tỉ lệ phần trăm để vẽ biểu đồ quạt tròn',
                           'formula': '$p_i\\% = \\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$)'},
                          {'name': 'Chênh lệch giữa hai cột trong biểu đồ cột kép',
                           'formula': '$\\Delta = |A_i - B_i|$'}]}],
  'example': 'Để biểu diễn đồng thời số học sinh nam và số học sinh nữ của 4 lớp 8A, 8B, 8C, 8D nhằm so sánh '
             'trực quan nam và nữ ở từng lớp, ta nên chọn loại biểu đồ nào?',
  'example_answer': 'Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 4 đối tượng '
                    '(lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ cột kép.',
  'real_life': 'Trình bày báo cáo kinh doanh (so sánh doanh thu và chi phí qua các quý bằng biểu đồ cột kép; '
               'cơ cấu thị phần bằng biểu đồ quạt tròn).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Để so sánh sản lượng lúa xuất khẩu của hai quốc gia Việt Nam và Thái Lan qua các năm '
                 '$2020, 2021, 2022, 2023$, loại biểu đồ thích hợp nhất là:',
            'options': ['Biểu đồ hình quạt tròn', 'Biểu đồ tranh', 'Biểu đồ cột kép', 'Biểu đồ cột đơn'],
            'answer': 2,
            'solution': 'Để so sánh song song hai bộ số liệu (hai quốc gia) qua cùng các năm, ta dùng biểu '
                        'đồ cột kép.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Để biểu diễn tỉ lệ phần trăm các loại sách (Giáo khoa, Tham khảo, Văn học, Khoa học) trong '
                 'tổng số sách của thư viện, ta nên chọn:',
            'options': ['Biểu đồ đoạn thẳng', 'Biểu đồ cột kép', 'Sơ đồ cây', 'Biểu đồ hình quạt tròn'],
            'answer': 3,
            'solution': 'Biểu đồ hình quạt tròn thích hợp nhất để biểu diễn tỉ lệ phần trăm các phần trong '
                        'toàn bộ dữ liệu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Tính tỉ lệ phần trăm để vẽ biểu đồ quạt tròn**?',
            'options': ['$p_i\\% = \\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$)',
                        '$p_i\\% = \\dfrac{n_i}{N} : 100\\%$ (với $N = \\sum n_i$)',
                        '$p_i\\% = \\dfrac{N}{n_i} \\cdot 100\\%$ (với $N = \\sum n_i$)',
                        '$p_i\\% = \\dfrac{n_i}{N} \\cdot 102\\%$ (với $N = \\sum n_i$)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ, **Tính '
                        'tỉ lệ phần trăm để vẽ biểu đồ quạt tròn** được xác định bởi: $p_i\\% = '
                        '\\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Chênh lệch giữa hai cột trong biểu đồ cột kép**?',
            'options': ['$\\Delta = |A_i + B_i|$',
                        '$\\Delta = |A_i - B_i|$',
                        'Đảo ngược vế của quy tắc: $\\Delta = |A_i - B_i|$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\Delta = |A_i - B_i|$'],
            'answer': 1,
            'solution': 'Trong Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ, **Chênh lệch giữa hai cột trong '
                        'biểu đồ cột kép** có công thức/quy tắc là: $\\Delta = |A_i - B_i|$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bảng thống kê số lượng xe bán ra của một đại lí trong 4 quý là: Quý I ($20$ xe), Quý II '
                 '($30$ xe), Quý III ($25$ xe), Quý IV ($25$ xe). Nếu chuyển sang biểu đồ hình quạt tròn thì '
                 'Quý II chiếm bao nhiêu phần trăm?',
            'options': ['$25\\%$', '$20\\%$', '$30\\%$', '$35\\%$'],
            'answer': 2,
            'solution': 'Tổng số xe cả năm là $20 + 30 + 25 + 25 = 100$ (xe). Tỉ lệ Quý II là '
                        '$\\dfrac{30}{100} \\cdot 100\\% = 30\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp (biểu đồ cột, cột '
                        'kép, hình quạt tròn, đoạn thẳng). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ '
                        'thích hợp (biểu đồ cột, cột kép, hình quạt tròn, đoạn thẳng).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Lựa chọn và biểu diễn được dữ '
                        'liệu vào bảng, biểu đồ thích hợp (biểu đồ cột, cột kép, hình quạt tròn, đoạn '
                        'thẳng).',
                        'Lựa chọn và biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp (biểu đồ cột, cột '
                        'kép, hình quạt tròn, đoạn thẳng).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ: Lựa chọn và '
                        'biểu diễn được dữ liệu vào bảng, biểu đồ thích hợp (biểu đồ cột, cột kép, hình quạt '
                        'tròn, đoạn thẳng).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về việc lựa chọn và chuyển đổi biểu đồ:',
            'statements': ['Biểu đồ đoạn thẳng rất phù hợp để biểu diễn xu thế thay đổi của mực nước sông '
                           'theo các tháng trong năm.',
                           'Khi chuyển dữ liệu từ biểu đồ cột sang bảng thống kê, các số liệu thực tế vẫn '
                           'được giữ nguyên.',
                           'Có thể dùng một biểu đồ hình quạt tròn duy nhất để biểu diễn trực tiếp chiều cao '
                           '(tính bằng $\\text{cm}$) của $5$ bạn học sinh.',
                           'Trong biểu đồ cột kép, hai cột của cùng một nhóm dữ liệu thường được tô hai màu '
                           '(hoặc kí hiệu) khác nhau và giải thích trong phần chú giải.'],
            'answer': [True, True, False, True],
            'solution': 'a), b), d) Đúng. c) Sai vì chiều cao của 5 bạn không phải là các thành phần tạo nên '
                        'một tổng thể $100\\%$, phải dùng biểu đồ cột.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 19: Biểu diễn dữ liệu bằng '
                 'bảng, biểu đồ**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Lựa chọn và biểu diễn được dữ liệu vào '
                           'bảng, biểu đồ thích hợp (biểu đồ cột, cột kép, hình quạt tròn, đoạn thẳng).',
                           'Trong **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ**, quy tắc/công thức **Tính '
                           'tỉ lệ phần trăm để vẽ biểu đồ quạt tròn** được viết là: $p_i\\% = '
                           '\\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$).',
                           'Nếu áp dụng sai dấu/phép tính thành $p_i\\% = \\dfrac{n_i}{N} : 100\\%$ (với $N '
                           '= \\sum n_i$) thì kết quả của **Tính tỉ lệ phần trăm để vẽ biểu đồ quạt tròn** '
                           'trong **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Để biểu diễn đồng thời số học sinh nam và số học sinh nữ của '
                           '4 lớp 8A, 8B, 8C, 8D nhằm so sánh trực quan nam và nữ ở từng lớp, ta nên c...”, '
                           'kết quả giải đúng là: Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học '
                           'sinh nữ) trên cùng 4 đối tượng (lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích '
                           'hợp...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ. '
                        'b) **Đúng** theo công thức **Tính tỉ lệ phần trăm để vẽ biểu đồ quạt tròn** '
                        '($p_i\\% = \\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$)). c) **Sai** vì '
                        'công thức đúng của **Tính tỉ lệ phần trăm để vẽ biểu đồ quạt tròn** phải là $p_i\\% '
                        '= \\dfrac{n_i}{N} \\cdot 100\\%$ (với $N = \\sum n_i$) chứ không phải $p_i\\% = '
                        '\\dfrac{n_i}{N} : 100\\%$ (với $N = \\sum n_i$). d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ** để giải '
                 'bài toán sau: Để biểu diễn đồng thời số học sinh nam và số học sinh nữ của 4 lớp 8A, 8B, '
                 '8C, 8D nhằm so sánh trực quan nam và nữ ở từng lớp, ta nên chọn loại biểu đồ nào? Cách '
                 'giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 4 đối '
                        'tượng (lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ...',
                        'Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 5 đối '
                        'tượng (lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ...',
                        'Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 3 đối '
                        'tượng (lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ...',
                        'Ta cần so sánh hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 8 đối '
                        'tượng (lớp 8A, 8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Biểu diễn dữ liệu bằng bảng, biểu đồ: Ta cần so sánh '
                        'hai bộ dữ liệu (số học sinh nam và số học sinh nữ) trên cùng 4 đối tượng (lớp 8A, '
                        '8B, 8C, 8D), do đó lựa chọn thích hợp nhất là biểu đồ cột kép.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một cửa hàng thống kê số áo sơ mi bán được trong 3 ngày thứ Sáu, thứ Bảy, Chủ nhật lần '
                 'lượt là $12; 18; 30$ (chiếc). Nếu chuyển sang biểu đồ hình quạt tròn thì ngày Chủ nhật '
                 'chiếm bao nhiêu phần trăm?',
            'answer': ['50'],
            'unit': None,
            'solution': 'Tổng số áo bán trong 3 ngày là $12 + 18 + 30 = 60$ (chiếc). Tỉ lệ ngày Chủ nhật là '
                        '$\\dfrac{30}{60} \\cdot 100\\% = 50\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch05-du-lieu-bieu-do',
  'context_title': 'Chương V: Dữ liệu và biểu đồ',
  'context': 'Chương V · SGK Toán 8: Thu thập, phân loại dữ liệu (rời rạc, liên tục), lựa chọn biểu đồ và '
             'phân tích số liệu thống kê.',
  'title': 'Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ',
  'icon': '🔍',
  'description': 'Phân tích số liệu, nhận biết những điểm không hợp lí khi biểu diễn dữ liệu và rút ra kết '
                 'luận từ biểu đồ.',
  'requirements': ['Phát hiện được vấn đề hoặc quy luật đơn giản dựa trên phân tích các số liệu thu được ở '
                   'dạng bảng và biểu đồ.',
                   'Nhận biết được mối liên hệ toán học giữa các số liệu và tránh những nhận định sai lệch '
                   'do gốc trục đứng không bắt đầu từ $0$.',
                   'Vận dụng kiến thức của **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Phân tích số liệu thống kê dựa vào biểu đồ là việc đọc, so sánh các số liệu, tính toán tốc '
                'độ tăng trưởng hoặc tỉ lệ để tìm ra xu hướng, quy luật và đưa ra quyết định hợp lí.',
  'theory': '1. Lưu ý khi đọc biểu đồ cột và đoạn thẳng: Cần quan sát kĩ gốc của trục đứng có bắt đầu từ số '
            '$0$ hay không. Nếu trục đứng bị cắt bớt (bắt đầu từ một số lớn hơn $0$), tỉ lệ chiều cao giữa '
            'các cột trên hình vẽ sẽ không phản ánh đúng tỉ lệ thực tế giữa các số liệu.\n'
            '2. So sánh hai biểu đồ hình quạt tròn: Khi so sánh hai biểu đồ hình quạt tròn của hai tổng thể '
            'khác nhau, phải nhân tỉ lệ phần trăm với quy mô tổng thể của mỗi biểu đồ mới so sánh được số '
            'lượng thực tế.',
  'formulas': [{'category': 'Các phép tính phân tích số liệu thống kê',
                'items': [{'name': 'Giá trị trung bình cộng',
                           'formula': '$\\bar{x} = \\dfrac{x_1 + x_2 + \\cdots + x_n}{n}$'},
                          {'name': 'Tỉ số giữa hai giá trị thực tế',
                           'formula': '$k = \\dfrac{y_2}{y_1}$ (dựa vào số liệu, không chỉ nhìn chiều cao '
                                      'cột nếu gốc trục $\\neq 0$)'}]}],
  'example': 'Trên một biểu đồ cột có gốc trục đứng bắt đầu từ $90$, cột A biểu diễn số liệu $95$ và cột B '
             'biểu diễn số liệu $100$. Chiều cao cột B gấp đôi chiều cao cột A trên hình vẽ, có thể kết luận '
             'giá trị của B gấp đôi A không?',
  'example_answer': 'Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $90$ nên độ cao hiển thị tỉ '
                    'lệ với $95 - 90 = 5$ và $100 - 90 = 10$ (gấp đôi trên hình), nhưng thực tế tỉ số của B '
                    'so với A chỉ là $\\dfrac{100}{95} \\approx 1,05$.',
  'real_life': 'Đọc hiểu đúng các biểu đồ quảng cáo, báo cáo tài chính để không bị đánh lừa thị giác bởi '
               'cách chọn tỉ lệ trục tọa độ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đọc một biểu đồ cột để so sánh tỉ lệ gấp nhau giữa hai đại lượng, ta cần chú ý điều gì '
                 'trước tiên trên trục đứng?',
            'options': ['Chỉ cần ước lượng bằng mắt độ cao của hai cột',
                        'Chỉ cần nhìn màu sắc của hai cột',
                        'Đo chiều rộng của mỗi cột bằng thước kẻ',
                        'Xem gốc của trục đứng có bắt đầu từ $0$ hay không và đọc số liệu cụ thể'],
            'answer': 3,
            'solution': 'Nếu gốc trục đứng không bắt đầu từ $0$, chiều cao cột không tỉ lệ thuận với giá trị '
                        'thực, nên phải đọc số liệu cụ thể.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trường A có $500$ học sinh với $20\\%$ học sinh giỏi; trường B có $1000$ học sinh với '
                 '$15\\%$ học sinh giỏi. Khẳng định nào sau đây đúng?',
            'options': ['Trường B có nhiều học sinh giỏi hơn trường A',
                        'Trường A có nhiều học sinh giỏi hơn trường B',
                        'Hai trường có số học sinh giỏi bằng nhau',
                        'Không tính được số học sinh giỏi của mỗi trường'],
            'answer': 0,
            'solution': 'Trường A có $500 \\cdot 20\\% = 100$ học sinh giỏi; trường B có $1000 \\cdot 15\\% '
                        '= 150$ học sinh giỏi. Vậy trường B nhiều hơn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Giá trị trung bình cộng**?',
            'options': ['$\\bar{x} = \\dfrac{x_1 - x_2 + \\cdots + x_n}{n}$',
                        '$\\bar{x} = \\dfrac{x_1 + x_2 + \\cdots + x_n}{n}$',
                        '$\\bar{x} = \\dfrac{n}{x_1 + x_2 + \\cdots + x_n}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\bar{x} = \\dfrac{x_1 + x_2 + '
                        '\\cdots + x_n}{n}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ, '
                        '**Giá trị trung bình cộng** được xác định bởi: $\\bar{x} = \\dfrac{x_1 + x_2 + '
                        '\\cdots + x_n}{n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Tỉ số giữa hai giá trị thực tế**?',
            'options': ['$k = \\dfrac{y_2}{y_1}$ (dựa vào số liệu, không chỉ nhìn chiều cao cột nếu gốc trục '
                        '$\\neq 1$)',
                        '$k = \\dfrac{y_1}{y_2}$ (dựa vào số liệu, không chỉ nhìn chiều cao cột nếu gốc trục '
                        '$\\neq 0$)',
                        '$k = \\dfrac{y_2}{y_1}$ (dựa vào số liệu, không chỉ nhìn chiều cao cột nếu gốc trục '
                        '$\\neq 0$)',
                        '$k = \\dfrac{y_2}{y_1}$ (dựa vào số liệu, không chỉ nhìn chiều cao cột nếu gốc trục '
                        '$\\neq 2$)'],
            'answer': 2,
            'solution': 'Trong Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ, **Tỉ số giữa hai giá trị '
                        'thực tế** có công thức/quy tắc là: $k = \\dfrac{y_2}{y_1}$ (dựa vào số liệu, không '
                        'chỉ nhìn chiều cao cột nếu gốc trục $\\neq 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Sản lượng cam của một trang trại trong 3 năm $2022, 2023, 2024$ lần lượt là $40$ tấn, $50$ '
                 'tấn và $65$ tấn. Tốc độ tăng trưởng năm $2024$ so với năm $2023$ là:',
            'options': ['$25\\%$', '$15\\%$', '$62,5\\%$', '$30\\%$'],
            'answer': 3,
            'solution': 'Tốc độ tăng trưởng năm $2024$ so với năm $2023$ là $\\dfrac{65 - 50}{50} \\cdot '
                        '100\\% = \\dfrac{15}{50} \\cdot 100\\% = 30\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Phát hiện được vấn đề hoặc quy luật đơn giản dựa trên phân tích các số liệu thu '
                        'được ở dạng bảng và biểu đồ.',
                        'Phát hiện được vấn đề hoặc quy luật đơn giản dựa trên phân tích các số liệu thu '
                        'được ở dạng bảng và biểu đồ. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Phát hiện được vấn đề hoặc quy luật đơn giản dựa trên '
                        'phân tích các số liệu thu được ở dạng bảng và biểu đồ.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phát hiện được vấn đề hoặc quy '
                        'luật đơn giản dựa trên phân tích các số liệu thu được ở dạng bảng và biểu đồ.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ: Phát '
                        'hiện được vấn đề hoặc quy luật đơn giản dựa trên phân tích các số liệu thu được ở '
                        'dạng bảng và biểu đồ.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Biểu đồ cột kép thống kê điểm trung bình môn Toán và Ngữ văn của 3 tổ trong lớp 8A: Tổ 1 '
                 '(Toán $8,0$; Văn $7,5$), Tổ 2 (Toán $8,5$; Văn $8,0$), Tổ 3 (Toán $7,5$; Văn $8,5$). Xét '
                 'các khẳng định sau:',
            'statements': ['Ở Tổ 1 và Tổ 2, điểm trung bình môn Toán cao hơn môn Ngữ văn.',
                           'Ở Tổ 3, điểm trung bình môn Ngữ văn cao hơn môn Toán là $1,0$ điểm.',
                           'Tổ 2 có điểm trung bình môn Toán cao nhất trong 3 tổ.',
                           'Điểm trung bình môn Toán của cả 3 tổ cộng lại rồi chia $3$ bằng $8,5$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì trung bình cộng điểm Toán của 3 tổ là $\\dfrac{8,0 + 8,5 '
                        '+ 7,5}{3} = 8,0$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 20: Phân tích số liệu thống '
                 'kê dựa vào biểu đồ**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Phát hiện được vấn đề hoặc quy luật đơn '
                           'giản dựa trên phân tích các số liệu thu được ở dạng bảng và biểu đồ.',
                           'Trong **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ**, quy tắc/công thức '
                           '**Giá trị trung bình cộng** được viết là: $\\bar{x} = \\dfrac{x_1 + x_2 + '
                           '\\cdots + x_n}{n}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\bar{x} = \\dfrac{x_1 - x_2 + \\cdots + '
                           'x_n}{n}$ thì kết quả của **Giá trị trung bình cộng** trong **Bài 20: Phân tích '
                           'số liệu thống kê dựa vào biểu đồ** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Trên một biểu đồ cột có gốc trục đứng bắt đầu từ $90$, cột A '
                           'biểu diễn số liệu $95$ và cột B biểu diễn số liệu $100$. Chiều cao cột B g...”, '
                           'kết quả giải đúng là: Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu '
                           'từ $90$ nên độ cao hiển thị tỉ lệ với $95 - 90 = 5$ và $100 - 90 = 10$ (gấp '
                           'đô...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Phân tích số liệu thống kê dựa vào '
                        'biểu đồ. b) **Đúng** theo công thức **Giá trị trung bình cộng** ($\\bar{x} = '
                        '\\dfrac{x_1 + x_2 + \\cdots + x_n}{n}$). c) **Sai** vì công thức đúng của **Giá trị '
                        'trung bình cộng** phải là $\\bar{x} = \\dfrac{x_1 + x_2 + \\cdots + x_n}{n}$ chứ '
                        'không phải $\\bar{x} = \\dfrac{x_1 - x_2 + \\cdots + x_n}{n}$. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ** để '
                 'giải bài toán sau: Trên một biểu đồ cột có gốc trục đứng bắt đầu từ $90$, cột A biểu diễn '
                 'số liệu $95$ và cột B biểu diễn số liệu $100$. Chiều cao cột B gấp đôi chiều cao cột A '
                 'trên hình vẽ, có thể kết luận giá trị của B gấp đôi A không? Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $90$ nên độ cao hiển '
                        'thị tỉ lệ với $95 + 90 = 5$ và $100 - 90 = 10$ (gấp đôi trên hình), n...',
                        'Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $90$ nên độ cao hiển '
                        'thị tỉ lệ với $95 - 90 = 5$ và $100 - 90 = 10$ (gấp đôi trên hình), n...',
                        'Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $90$ nên độ cao hiển '
                        'thị tỉ lệ với $95 - 90 = 5$ và $100 - 90 = 9$ (gấp đôi trên hình), n...',
                        'Không thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $92$ nên độ cao hiển '
                        'thị tỉ lệ với $95 - 90 = 5$ và $100 - 90 = 10$ (gấp đôi trên hình), n...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Phân tích số liệu thống kê dựa vào biểu đồ: Không '
                        'thể kết luận B gấp đôi A. Do gốc trục đứng bắt đầu từ $90$ nên độ cao hiển thị tỉ '
                        'lệ với $95 - 90 = 5$ và $100 - 90 = 10$ (gấp đôi trên hình), nhưng thực tế tỉ số '
                        'của B so với A chỉ là $\\dfrac{100}{95} \\approx 1,05$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Năm $2023$, tổng thu nhập của gia đình bác Nam là $200$ triệu đồng, trong đó chi cho giáo '
                 'dục chiếm $15\\%$. Năm $2024$, tổng thu nhập là $250$ triệu đồng và chi cho giáo dục chiếm '
                 '$16\\%$. Hỏi năm $2024$ gia đình bác Nam chi cho giáo dục nhiều hơn năm $2023$ bao nhiêu '
                 'triệu đồng?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Năm $2023$ chi $200 \\cdot 15\\% = 30$ (triệu đồng). Năm $2024$ chi $250 \\cdot '
                        '16\\% = 40$ (triệu đồng). Chênh lệch là $40 - 30 = 10$ (triệu đồng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch06-phan-thuc-dai-so',
  'context_title': 'Chương VI: Phân thức đại số',
  'context': 'Chương VI · SGK Toán 8: Phân thức đại số, tính chất cơ bản, rút gọn, quy đồng mẫu thức và các '
             'phép tính cộng, trừ, nhân, chia phân thức.',
  'title': 'Bài 21: Phân thức đại số',
  'icon': '➗',
  'description': 'Khái niệm phân thức đại số, hai phân thức bằng nhau và điều kiện xác định của phân thức '
                 'đại số.',
  'requirements': ['Nhận biết được phân thức đại số, tử thức và mẫu thức.',
                   'Nhận biết được điều kiện để hai phân thức bằng nhau.',
                   'Tìm được điều kiện xác định và tính được giá trị của phân thức đại số tại giá trị của '
                   'biến thỏa mãn điều kiện xác định.'],
  'definition': 'Một phân thức đại số (hay nói gọn là phân thức) là một biểu thức có dạng $\\dfrac{A}{B}$, '
                'trong đó $A, B$ là những đa thức và $B$ khác đa thức $0$ ($A$ là tử thức, $B$ là mẫu thức). '
                'Hai phân thức $\\dfrac{A}{B}$ và $\\dfrac{C}{D}$ gọi là bằng nhau nếu $A \\cdot D = B '
                '\\cdot C$.',
  'theory': '1. Chú ý: Mỗi đa thức cũng được coi là một phân thức với mẫu thức bằng $1$.\n'
            '2. Hai phân thức bằng nhau: $\\dfrac{A}{B} = \\dfrac{C}{D}$ nếu $A \\cdot D = B \\cdot C$.\n'
            '3. Điều kiện xác định của phân thức $\\dfrac{A}{B}$: Là điều kiện của biến để giá trị của mẫu '
            'thức $B$ khác $0$ ($B \\neq 0$).',
  'formulas': [{'category': 'Khái niệm và điều kiện xác định của phân thức',
                'items': [{'name': 'Hai phân thức bằng nhau',
                           'formula': '$\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot '
                                      'C \\quad (B, D \\neq 0)$'},
                          {'name': 'Điều kiện xác định của $\\dfrac{A}{B}$', 'formula': '$B \\neq 0$'}]}],
  'example': 'Tìm điều kiện xác định của phân thức $P = \\dfrac{x + 2}{x - 3}$ và tính giá trị của $P$ tại '
             '$x = 5$.',
  'example_answer': '- Điều kiện xác định của phân thức $P$ là $x - 3 \\neq 0$, hay $x \\neq 3$.\n'
                    '- Tại $x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 + 2}{5 - 3} = \\dfrac{7}{2} '
                    '= 3,5$.',
  'real_life': 'Biểu thức tính vận tốc trung bình trên quãng đường $s$ khi thời gian đi là $x - 2$ (giờ) có '
               'dạng phân thức $v = \\dfrac{s}{x - 2}$ với điều kiện $x > 2$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Điều kiện xác định của phân thức $\\dfrac{2x + 1}{x - 4}$ là:',
            'options': ['$x \\neq 4$', '$x \\neq -4$', '$x \\neq \\dfrac{-1}{2}$', '$x > 4$'],
            'answer': 0,
            'solution': 'Phân thức xác định khi mẫu thức khác $0$: $x - 4 \\neq 0 \\Leftrightarrow x \\neq '
                        '4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai phân thức $\\dfrac{A}{B}$ và $\\dfrac{C}{D}$ bằng nhau khi và chỉ khi:',
            'options': ['$A \\cdot C = B \\cdot D$',
                        '$A \\cdot D = B \\cdot C$',
                        '$A + D = B + C$',
                        '$A = C$ và $B \\neq D$'],
            'answer': 1,
            'solution': 'Theo định nghĩa hai phân thức bằng nhau: $\\dfrac{A}{B} = \\dfrac{C}{D} '
                        '\\Leftrightarrow A \\cdot D = B \\cdot C$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Phân thức đại số**, quy tắc hoặc công thức nào sau đây xác định đúng **Hai '
                 'phân thức bằng nhau**?',
            'options': ['$\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A : D = B \\cdot C \\quad (B, D '
                        '\\neq 0)$',
                        '$\\dfrac{B}{A} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, '
                        'D \\neq 0)$',
                        '$\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, '
                        'D \\neq 0)$',
                        '$\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, '
                        'D \\neq 2)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 21: Phân thức đại số, **Hai phân thức bằng nhau** '
                        'được xác định bởi: $\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B '
                        '\\cdot C \\quad (B, D \\neq 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Phân thức đại số**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Điều kiện xác định của $\\dfrac{A}{B}$**?',
            'options': ['$B \\neq 1$',
                        '$B \\neq 2$',
                        '$\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, '
                        'D \\neq 0)$',
                        '$B \\neq 0$'],
            'answer': 3,
            'solution': 'Trong Bài 21: Phân thức đại số, **Điều kiện xác định của $\\dfrac{A}{B}$** có công '
                        'thức/quy tắc là: $B \\neq 0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phân thức nào sau đây bằng với phân thức $\\dfrac{x}{x + 1}$?',
            'options': ['$\\dfrac{x^2}{x(x + 1)}$',
                        '$\\dfrac{x + 1}{x + 2}$',
                        '$\\dfrac{2x}{x + 1}$',
                        '$\\dfrac{x^2}{x^2 + 1}$'],
            'answer': 0,
            'solution': 'Vì $x \\cdot x(x + 1) = (x + 1) \\cdot x^2$ nên $\\dfrac{x}{x + 1} = '
                        '\\dfrac{x^2}{x(x + 1)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 21: Phân thức đại số**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được phân thức đại số, tử thức và mẫu thức. (với dấu ngược lại)',
                        'Nhận biết được phân thức đại số, tử thức và mẫu thức.',
                        'Đảo ngược vế của quy tắc: Nhận biết được phân thức đại số, tử thức và mẫu thức.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được phân thức đại '
                        'số, tử thức và mẫu thức.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 21: Phân thức đại số: Nhận biết được phân thức đại '
                        'số, tử thức và mẫu thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phân thức $Q = \\dfrac{x^2 - 1}{x - 1}$. Xét các khẳng định sau:',
            'statements': ['Điều kiện xác định của phân thức $Q$ là $x \\neq 1$.',
                           'Vì $(x^2 - 1) \\cdot 1 = (x - 1)(x + 1)$ nên $\\dfrac{x^2 - 1}{x - 1} = x + 1$ '
                           'với mọi $x \\neq 1$.',
                           'Tại $x = 3$, giá trị của phân thức $Q$ bằng $4$.',
                           'Tại $x = 1$, giá trị của phân thức $Q$ bằng $2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì tại $x = 1$ mẫu thức bằng $0$, phân thức không xác định.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 21: Phân thức đại số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được phân thức đại số, tử thức '
                           'và mẫu thức.',
                           'Trong **Bài 21: Phân thức đại số**, quy tắc/công thức **Hai phân thức bằng '
                           'nhau** được viết là: $\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A \\cdot D '
                           '= B \\cdot C \\quad (B, D \\neq 0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{A}{B} = \\dfrac{C}{D} '
                           '\\Leftrightarrow A : D = B \\cdot C \\quad (B, D \\neq 0)$ thì kết quả của **Hai '
                           'phân thức bằng nhau** trong **Bài 21: Phân thức đại số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm điều kiện xác định của phân thức $P = \\dfrac{x + 2}{x - '
                           '3}$ và tính giá trị của $P$ tại $x = 5$.”, kết quả giải đúng là: - Điều kiện xác '
                           'định của phân thức $P$ là $x - 3 \\neq 0$, hay $x \\neq 3$. - Tại $x = 5$ (thỏa '
                           'mãn $x \\neq 3$), ta có $P = \\dfrac{5 + 2}{5 - 3} = \\dfrac{7}{2} = 3,5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Phân thức đại số. b) **Đúng** theo '
                        'công thức **Hai phân thức bằng nhau** ($\\dfrac{A}{B} = \\dfrac{C}{D} '
                        '\\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, D \\neq 0)$). c) **Sai** vì '
                        'công thức đúng của **Hai phân thức bằng nhau** phải là $\\dfrac{A}{B} = '
                        '\\dfrac{C}{D} \\Leftrightarrow A \\cdot D = B \\cdot C \\quad (B, D \\neq 0)$ chứ '
                        'không phải $\\dfrac{A}{B} = \\dfrac{C}{D} \\Leftrightarrow A : D = B \\cdot C '
                        '\\quad (B, D \\neq 0)$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 21: Phân thức đại số** để giải bài toán sau: Tìm '
                 'điều kiện xác định của phân thức $P = \\dfrac{x + 2}{x - 3}$ và tính giá trị của $P$ tại '
                 '$x = 5$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- Điều kiện xác định của phân thức $P$ là $x - 3 \\neq 0$, hay $x \\neq 3$. - Tại '
                        '$x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 - 2}{5 - 3} = \\dfrac{7}{2} = '
                        '3,5$...',
                        '- Điều kiện xác định của phân thức $P$ là $x - 3 \\neq 0$, hay $x \\neq 3$. - Tại '
                        '$x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 - 3}{5 + 2} = \\dfrac{7}{2} = '
                        '3,5$...',
                        '- Điều kiện xác định của phân thức $P$ là $x - 3 \\neq 0$, hay $x \\neq 3$. - Tại '
                        '$x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 + 2}{5 - 3} = \\dfrac{7}{2} = '
                        '3,5$...',
                        '- Điều kiện xác định của phân thức $P$ là $x - 6 \\neq 0$, hay $x \\neq 3$. - Tại '
                        '$x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 + 2}{5 - 3} = \\dfrac{7}{2} = '
                        '3,5$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Phân thức đại số: - Điều kiện xác định của phân thức '
                        '$P$ là $x - 3 \\neq 0$, hay $x \\neq 3$.\n'
                        '- Tại $x = 5$ (thỏa mãn $x \\neq 3$), ta có $P = \\dfrac{5 + 2}{5 - 3} = '
                        '\\dfrac{7}{2} = 3,5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của phân thức $A = \\dfrac{3x + 6}{x + 1}$ tại $x = 2$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Tại $x = 2$ (thỏa mãn $x \\neq -1$), ta có $A = \\dfrac{3 \\cdot 2 + 6}{2 + 1} = '
                        '\\dfrac{12}{3} = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch06-phan-thuc-dai-so',
  'context_title': 'Chương VI: Phân thức đại số',
  'context': 'Chương VI · SGK Toán 8: Phân thức đại số, tính chất cơ bản, rút gọn, quy đồng mẫu thức và các '
             'phép tính cộng, trừ, nhân, chia phân thức.',
  'title': 'Bài 22: Tính chất cơ bản của phân thức đại số',
  'icon': '🔄',
  'description': 'Tính chất cơ bản của phân thức, quy tắc đổi dấu, cách rút gọn phân thức và quy đồng mẫu '
                 'thức nhiều phân thức.',
  'requirements': ['Mô tả được tính chất cơ bản của phân thức đại số và quy tắc đổi dấu.',
                   'Thực hiện được việc rút gọn phân thức đại số.',
                   'Tìm được mẫu thức chung và quy đồng được mẫu thức của hai hay nhiều phân thức.'],
  'definition': 'Nếu nhân cả tử và mẫu của một phân thức với cùng một đa thức khác đa thức $0$ thì được một '
                'phân thức bằng phân thức đã cho. Nếu chia cả tử và mẫu của một phân thức cho một nhân tử '
                'chung của chúng thì được một phân thức bằng phân thức đã cho.',
  'theory': '1. Tính chất cơ bản: $\\dfrac{A}{B} = \\dfrac{A \\cdot M}{B \\cdot M}$ ($M \\neq 0$) và '
            '$\\dfrac{A}{B} = \\dfrac{A : N}{B : N}$ ($N$ là nhân tử chung).\n'
            '2. Quy tắc đổi dấu: Nếu đổi dấu cả tử và mẫu của một phân thức thì được một phân thức bằng phân '
            'thức đã cho: $\\dfrac{A}{B} = \\dfrac{-A}{-B}$.\n'
            '3. Rút gọn phân thức: Phân tích tử và mẫu thành nhân tử (nếu cần) để tìm nhân tử chung rồi chia '
            'cả tử và mẫu cho nhân tử chung đó.\n'
            '4. Quy đồng mẫu thức: Phân tích các mẫu thức thành nhân tử, chọn mẫu thức chung (MTC), tìm nhân '
            'tử phụ của mỗi mẫu thức rồi nhân cả tử và mẫu của mỗi phân thức với nhân tử phụ tương ứng.',
  'formulas': [{'category': 'Tính chất cơ bản và quy tắc đổi dấu',
                'items': [{'name': 'Nhân cả tử và mẫu với $M \\neq 0$',
                           'formula': '$\\dfrac{A}{B} = \\dfrac{A \\cdot M}{B \\cdot M}$'},
                          {'name': 'Chia cả tử và mẫu cho nhân tử chung $N$',
                           'formula': '$\\dfrac{A}{B} = \\dfrac{A : N}{B : N}$'},
                          {'name': 'Quy tắc đổi dấu',
                           'formula': '$\\dfrac{A}{B} = \\dfrac{-A}{-B} = -\\dfrac{-A}{B} = '
                                      '-\\dfrac{A}{-B}$'}]}],
  'example': 'Rút gọn phân thức $P = \\dfrac{x^2 - 4x + 4}{x^2 - 4}$ (với $x \\neq \\pm 2$).',
  'example_answer': 'Phân tích tử và mẫu thành nhân tử:\n'
                    '$P = \\dfrac{(x - 2)^2}{(x - 2)(x + 2)} = \\dfrac{x - 2}{x + 2}$.',
  'real_life': 'Đơn giản hóa các công thức vật lí (như điện trở tương đương của mạch điện song song) trước '
               'khi thay số tính toán.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Theo quy tắc đổi dấu phân thức, đẳng thức nào sau đây là ĐÚNG?',
            'options': ['$\\dfrac{x - y}{2 - x} = \\dfrac{y - x}{2 - x}$',
                        '$\\dfrac{x - y}{2 - x} = \\dfrac{y - x}{x - 2}$',
                        '$\\dfrac{x - y}{2 - x} = \\dfrac{x - y}{x - 2}$',
                        '$\\dfrac{x - y}{2 - x} = \\dfrac{x + y}{x + 2}$'],
            'answer': 1,
            'solution': 'Đổi dấu cả tử và mẫu: $\\dfrac{x - y}{2 - x} = \\dfrac{-(x - y)}{-(2 - x)} = '
                        '\\dfrac{y - x}{x - 2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Rút gọn phân thức $\\dfrac{6x^2y^3}{9xy^4}$ (với $x, y \\neq 0$) ta được:',
            'options': ['$\\dfrac{2y}{3x}$', '$\\dfrac{3x}{2y}$', '$\\dfrac{2x}{3y}$', '$\\dfrac{2x^2}{3y}$'],
            'answer': 2,
            'solution': 'Chia cả tử và mẫu cho nhân tử chung $3xy^3$ ta được $\\dfrac{2x}{3y}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Tính chất cơ bản của phân thức đại số**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Nhân cả tử và mẫu với $M \\neq 0$**?',
            'options': ['$\\dfrac{A}{B} = \\dfrac{A : M}{B \\cdot M}$',
                        '$\\dfrac{B}{A} = \\dfrac{A \\cdot M}{B \\cdot M}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A}{B} = \\dfrac{A '
                        '\\cdot M}{B \\cdot M}$',
                        '$\\dfrac{A}{B} = \\dfrac{A \\cdot M}{B \\cdot M}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 22: Tính chất cơ bản của phân thức đại số, **Nhân '
                        'cả tử và mẫu với $M \\neq 0$** được xác định bởi: $\\dfrac{A}{B} = \\dfrac{A \\cdot '
                        'M}{B \\cdot M}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: Tính chất cơ bản của phân thức đại số**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Chia cả tử và mẫu cho nhân tử chung $N$**?',
            'options': ['$\\dfrac{A}{B} = \\dfrac{A : N}{B : N}$',
                        '$\\dfrac{A}{B} = \\dfrac{A : N}{B : N}$ (với dấu ngược lại)',
                        '$\\dfrac{B}{A} = \\dfrac{A : N}{B : N}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A}{B} = \\dfrac{A : '
                        'N}{B : N}$'],
            'answer': 0,
            'solution': 'Trong Bài 22: Tính chất cơ bản của phân thức đại số, **Chia cả tử và mẫu cho nhân '
                        'tử chung $N$** có công thức/quy tắc là: $\\dfrac{A}{B} = \\dfrac{A : N}{B : N}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Mẫu thức chung đơn giản nhất của hai phân thức $\\dfrac{1}{2x - 2}$ và $\\dfrac{3}{x^2 - '
                 '1}$ là:',
            'options': ['$(x - 1)(x + 1)$', '$2(x - 1)(x + 1)$', '$2(x - 1)^2(x + 1)$', '$2(x^2 + 1)$'],
            'answer': 1,
            'solution': 'Ta có $2x - 2 = 2(x - 1)$ và $x^2 - 1 = (x - 1)(x + 1)$ nên mẫu thức chung là $2(x '
                        '- 1)(x + 1)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 22: Tính chất cơ bản của phân thức đại số**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Mô tả được tính chất cơ bản của phân thức đại số và quy tắc đổi dấu. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được tính chất cơ bản của phân thức đại số và quy '
                        'tắc đổi dấu.',
                        'Mô tả được tính chất cơ bản của phân thức đại số và quy tắc đổi dấu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được tính chất cơ bản của '
                        'phân thức đại số và quy tắc đổi dấu.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 22: Tính chất cơ bản của phân thức đại số: Mô tả được '
                        'tính chất cơ bản của phân thức đại số và quy tắc đổi dấu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phân thức $A = \\dfrac{x^2 - 9}{3x + 9}$ (với $x \\neq -3$). Xét các khẳng định sau:',
            'statements': ['Tử thức phân tích được thành $(x - 3)(x + 3)$.',
                           'Mẫu thức phân tích được thành $3(x + 3)$.',
                           'Nhân tử chung của tử và mẫu là $x + 3$, rút gọn được $A = \\dfrac{x - 3}{3}$.',
                           'Tại $x = 6$, giá trị của phân thức $A$ bằng $2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì tại $x = 6$ thì $A = \\dfrac{6 - 3}{3} = 1 \\neq 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 22: Tính chất cơ bản của '
                 'phân thức đại số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được tính chất cơ bản của phân '
                           'thức đại số và quy tắc đổi dấu.',
                           'Trong **Bài 22: Tính chất cơ bản của phân thức đại số**, quy tắc/công thức '
                           '**Nhân cả tử và mẫu với $M \\neq 0$** được viết là: $\\dfrac{A}{B} = \\dfrac{A '
                           '\\cdot M}{B \\cdot M}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{A}{B} = \\dfrac{A : M}{B \\cdot M}$ '
                           'thì kết quả của **Nhân cả tử và mẫu với $M \\neq 0$** trong **Bài 22: Tính chất '
                           'cơ bản của phân thức đại số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Rút gọn phân thức $P = \\dfrac{x^2 - 4x + 4}{x^2 - 4}$ (với '
                           '$x \\neq \\pm 2$).”, kết quả giải đúng là: Phân tích tử và mẫu thành nhân tử: $P '
                           '= \\dfrac{(x - 2)^2}{(x - 2)(x + 2)} = \\dfrac{x - 2}{x + 2}$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Tính chất cơ bản của phân thức đại số. '
                        'b) **Đúng** theo công thức **Nhân cả tử và mẫu với $M \\neq 0$** ($\\dfrac{A}{B} = '
                        '\\dfrac{A \\cdot M}{B \\cdot M}$). c) **Sai** vì công thức đúng của **Nhân cả tử và '
                        'mẫu với $M \\neq 0$** phải là $\\dfrac{A}{B} = \\dfrac{A \\cdot M}{B \\cdot M}$ chứ '
                        'không phải $\\dfrac{A}{B} = \\dfrac{A : M}{B \\cdot M}$. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 22: Tính chất cơ bản của phân thức đại số** để giải '
                 'bài toán sau: Rút gọn phân thức $P = \\dfrac{x^2 - 4x + 4}{x^2 - 4}$ (với $x \\neq \\pm '
                 '2$). Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Phân tích tử và mẫu thành nhân tử: $P = \\dfrac{(x - 2)^2}{(x - 2)(x - 2)} = '
                        '\\dfrac{x - 2}{x + 2}$.',
                        'Phân tích tử và mẫu thành nhân tử: $P = \\dfrac{(x - 2)(x + 2)}{(x - 2)^2} = '
                        '\\dfrac{x - 2}{x + 2}$.',
                        'Phân tích tử và mẫu thành nhân tử: $P = \\dfrac{(x - 4)^2}{(x - 2)(x + 2)} = '
                        '\\dfrac{x - 2}{x + 2}$.',
                        'Phân tích tử và mẫu thành nhân tử: $P = \\dfrac{(x - 2)^2}{(x - 2)(x + 2)} = '
                        '\\dfrac{x - 2}{x + 2}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Tính chất cơ bản của phân thức đại số: Phân tích tử '
                        'và mẫu thành nhân tử:\n'
                        '$P = \\dfrac{(x - 2)^2}{(x - 2)(x + 2)} = \\dfrac{x - 2}{x + 2}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn phân thức $M = \\dfrac{x^2 + 6x + 9}{x + 3}$ (với $x \\neq -3$) rồi tính giá trị '
                 'của $M$ tại $x = 7$.',
            'answer': ['10'],
            'unit': None,
            'solution': 'Ta có $M = \\dfrac{(x + 3)^2}{x + 3} = x + 3$. Tại $x = 7$, $M = 7 + 3 = 10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch06-phan-thuc-dai-so',
  'context_title': 'Chương VI: Phân thức đại số',
  'context': 'Chương VI · SGK Toán 8: Phân thức đại số, tính chất cơ bản, rút gọn, quy đồng mẫu thức và các '
             'phép tính cộng, trừ, nhân, chia phân thức.',
  'title': 'Bài 23: Phép cộng và phép trừ phân thức đại số',
  'icon': '➕',
  'description': 'Quy tắc cộng, trừ hai phân thức cùng mẫu, khác mẫu và các tính chất của phép cộng phân '
                 'thức.',
  'requirements': ['Thực hiện được phép cộng và phép trừ hai phân thức cùng mẫu thức hoặc khác mẫu thức.',
                   'Vận dụng được tính chất giao hoán, kết hợp và quy tắc dấu ngoặc để rút gọn biểu thức '
                   'phân thức.',
                   'Vận dụng kiến thức của **Bài 23: Phép cộng và phép trừ phân thức đại số** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Muốn cộng (hoặc trừ) hai phân thức có cùng mẫu thức, ta cộng (hoặc trừ) các tử thức với '
                'nhau và giữ nguyên mẫu thức. Muốn cộng (hoặc trừ) hai phân thức có mẫu thức khác nhau, ta '
                'quy đồng mẫu thức rồi cộng (hoặc trừ) các phân thức có cùng mẫu thức vừa tìm được.',
  'theory': '1. Cộng, trừ hai phân thức cùng mẫu: $\\dfrac{A}{M} + \\dfrac{B}{M} = \\dfrac{A + B}{M}$ và '
            '$\\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$.\n'
            '2. Cộng, trừ hai phân thức khác mẫu: Quy đồng mẫu thức rồi thực hiện cộng, trừ hai phân thức '
            'cùng mẫu.\n'
            '3. Phân thức đối: Phân thức đối của $\\dfrac{A}{B}$ là $-\\dfrac{A}{B} = \\dfrac{-A}{B} = '
            '\\dfrac{A}{-B}$.',
  'formulas': [{'category': 'Công thức cộng, trừ phân thức đại số',
                'items': [{'name': 'Cộng, trừ cùng mẫu thức',
                           'formula': '$\\dfrac{A}{M} + \\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad '
                                      '\\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$'},
                          {'name': 'Cộng, trừ khác mẫu thức',
                           'formula': '$\\dfrac{A}{B} \\pm \\dfrac{C}{D} = \\dfrac{A \\cdot D \\pm B \\cdot '
                                      'C}{B \\cdot D}$'}]}],
  'example': 'Thực hiện phép tính: $P = \\dfrac{x}{x - 2} + \\dfrac{4}{2 - x}$ (với $x \\neq 2$).',
  'example_answer': 'Áp dụng quy tắc đổi dấu cho phân thức thứ hai: $\\dfrac{4}{2 - x} = -\\dfrac{4}{x - '
                    '2}$.\n'
                    'Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$.',
  'real_life': 'Tính tổng thời gian cả đi lẫn về của một ca nô xuôi dòng và ngược dòng trên sông: $T = '
               '\\dfrac{s}{v + v_n} + \\dfrac{s}{v - v_n}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép cộng $\\dfrac{2x - 1}{x + 3} + \\dfrac{x + 10}{x + 3}$ (với $x \\neq -3$) '
                 'sau khi rút gọn là:',
            'options': ['$\\dfrac{3x + 9}{2x + 6}$', '$\\dfrac{x - 11}{x + 3}$', '$3$', '$1$'],
            'answer': 2,
            'solution': '$\\dfrac{(2x - 1) + (x + 10)}{x + 3} = \\dfrac{3x + 9}{x + 3} = \\dfrac{3(x + 3)}{x '
                        '+ 3} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phân thức đối của phân thức $\\dfrac{x - 2}{x + 1}$ là:',
            'options': ['$\\dfrac{x + 2}{x + 1}$',
                        '$\\dfrac{x + 1}{x - 2}$',
                        '$\\dfrac{2 - x}{-x - 1}$',
                        '$\\dfrac{2 - x}{x + 1}$'],
            'answer': 3,
            'solution': 'Phân thức đối của $\\dfrac{x - 2}{x + 1}$ là $-\\dfrac{x - 2}{x + 1} = \\dfrac{2 - '
                        'x}{x + 1}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Phép cộng và phép trừ phân thức đại số**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Cộng, trừ cùng mẫu thức**?',
            'options': ['$\\dfrac{A}{M} + \\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - '
                        '\\dfrac{B}{M} = \\dfrac{A - B}{M}$',
                        '$\\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - '
                        '\\dfrac{B}{M} = \\dfrac{A - B}{M}$',
                        '$\\dfrac{M}{A} + \\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - '
                        '\\dfrac{B}{M} = \\dfrac{A - B}{M}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A}{M} + \\dfrac{B}{M} '
                        '= \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 23: Phép cộng và phép trừ phân thức đại số, '
                        '**Cộng, trừ cùng mẫu thức** được xác định bởi: $\\dfrac{A}{M} + \\dfrac{B}{M} = '
                        '\\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Phép cộng và phép trừ phân thức đại số**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Cộng, trừ khác mẫu thức**?',
            'options': ['$\\dfrac{A}{B} \\pm \\dfrac{C}{D} = \\dfrac{A : D \\pm B \\cdot C}{B \\cdot D}$',
                        '$\\dfrac{A}{B} \\pm \\dfrac{C}{D} = \\dfrac{A \\cdot D \\pm B \\cdot C}{B \\cdot '
                        'D}$',
                        '$\\dfrac{B}{A} \\pm \\dfrac{C}{D} = \\dfrac{A \\cdot D \\pm B \\cdot C}{B \\cdot '
                        'D}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A}{B} \\pm '
                        '\\dfrac{C}{D} = \\dfrac{A \\cdot D \\pm B \\cdot C}{B \\cdot D}$'],
            'answer': 1,
            'solution': 'Trong Bài 23: Phép cộng và phép trừ phân thức đại số, **Cộng, trừ khác mẫu thức** '
                        'có công thức/quy tắc là: $\\dfrac{A}{B} \\pm \\dfrac{C}{D} = \\dfrac{A \\cdot D '
                        '\\pm B \\cdot C}{B \\cdot D}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thực hiện phép trừ $\\dfrac{x^2}{x - 1} - \\dfrac{1}{x - 1}$ (với $x \\neq 1$) ta được:',
            'options': ['$x - 1$', '$\\dfrac{1}{x + 1}$', '$x + 1$', '$x^2 - 1$'],
            'answer': 2,
            'solution': '$\\dfrac{x^2 - 1}{x - 1} = \\dfrac{(x - 1)(x + 1)}{x - 1} = x + 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 23: Phép cộng và phép trừ phân thức đại số**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng và phép trừ hai phân thức cùng mẫu thức hoặc khác mẫu '
                        'thức. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép cộng và phép trừ hai phân thức cùng '
                        'mẫu thức hoặc khác mẫu thức.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép cộng và '
                        'phép trừ hai phân thức cùng mẫu thức hoặc khác mẫu thức.',
                        'Thực hiện được phép cộng và phép trừ hai phân thức cùng mẫu thức hoặc khác mẫu '
                        'thức.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 23: Phép cộng và phép trừ phân thức đại số: Thực hiện '
                        'được phép cộng và phép trừ hai phân thức cùng mẫu thức hoặc khác mẫu thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $A = \\dfrac{1}{x} + \\dfrac{1}{x + 1}$ (với $x \\neq 0, x \\neq -1$). Xét '
                 'các khẳng định sau:',
            'statements': ['Mẫu thức chung của hai phân thức là $x(x + 1)$.',
                           'Sau khi quy đồng và cộng hai phân thức, ta được $A = \\dfrac{2x + 1}{x(x + 1)}$.',
                           'Nếu lấy $\\dfrac{1}{x} - \\dfrac{1}{x + 1}$ thì kết quả là $\\dfrac{1}{x(x + '
                           '1)}$.',
                           'Tại $x = 1$, giá trị của biểu thức $A$ bằng $2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì tại $x = 1$ thì $A = \\dfrac{1}{1} + \\dfrac{1}{2} = '
                        '\\dfrac{3}{2} \\neq 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 23: Phép cộng và phép trừ '
                 'phân thức đại số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép cộng và phép trừ hai '
                           'phân thức cùng mẫu thức hoặc khác mẫu thức.',
                           'Trong **Bài 23: Phép cộng và phép trừ phân thức đại số**, quy tắc/công thức '
                           '**Cộng, trừ cùng mẫu thức** được viết là: $\\dfrac{A}{M} + \\dfrac{B}{M} = '
                           '\\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A + '
                           'B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$ thì kết quả của '
                           '**Cộng, trừ cùng mẫu thức** trong **Bài 23: Phép cộng và phép trừ phân thức đại '
                           'số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Thực hiện phép tính: $P = \\dfrac{x}{x - 2} + \\dfrac{4}{2 - '
                           'x}$ (với $x \\neq 2$).”, kết quả giải đúng là: Áp dụng quy tắc đổi dấu cho phân '
                           'thức thứ hai: $\\dfrac{4}{2 - x} = -\\dfrac{4}{x - 2}$. Khi đó $P = \\dfrac{x}{x '
                           '- 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Phép cộng và phép trừ phân thức đại '
                        'số. b) **Đúng** theo công thức **Cộng, trừ cùng mẫu thức** ($\\dfrac{A}{M} + '
                        '\\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A '
                        '- B}{M}$). c) **Sai** vì công thức đúng của **Cộng, trừ cùng mẫu thức** phải là '
                        '$\\dfrac{A}{M} + \\dfrac{B}{M} = \\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - '
                        '\\dfrac{B}{M} = \\dfrac{A - B}{M}$ chứ không phải $\\dfrac{A}{M} - \\dfrac{B}{M} = '
                        '\\dfrac{A + B}{M}; \\quad \\dfrac{A}{M} - \\dfrac{B}{M} = \\dfrac{A - B}{M}$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 23: Phép cộng và phép trừ phân thức đại số** để '
                 'giải bài toán sau: Thực hiện phép tính: $P = \\dfrac{x}{x - 2} + \\dfrac{4}{2 - x}$ (với '
                 '$x \\neq 2$). Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Áp dụng quy tắc đổi dấu cho phân thức thứ hai: $\\dfrac{4}{2 - x} = -\\dfrac{4}{x - '
                        '2}$. Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$...',
                        'Áp dụng quy tắc đổi dấu cho phân thức thứ hai: $\\dfrac{4}{2 + x} = -\\dfrac{4}{x - '
                        '2}$. Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$...',
                        'Áp dụng quy tắc đổi dấu cho phân thức thứ hai: $\\dfrac{2 - x}{4} = -\\dfrac{4}{x - '
                        '2}$. Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$...',
                        'Áp dụng quy tắc đổi dấu cho phân thức thứ hai: $\\dfrac{8}{2 - x} = -\\dfrac{4}{x - '
                        '2}$. Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Phép cộng và phép trừ phân thức đại số: Áp dụng quy '
                        'tắc đổi dấu cho phân thức thứ hai: $\\dfrac{4}{2 - x} = -\\dfrac{4}{x - 2}$.\n'
                        'Khi đó $P = \\dfrac{x}{x - 2} - \\dfrac{4}{x - 2} = \\dfrac{x - 4}{x - 2}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn biểu thức $P = \\dfrac{2x}{x + 4} + \\dfrac{8}{x + 4}$ (với $x \\neq -4$) ta được '
                 'kết quả là một số không đổi bằng bao nhiêu?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Ta có $P = \\dfrac{2x + 8}{x + 4} = \\dfrac{2(x + 4)}{x + 4} = 2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch06-phan-thuc-dai-so',
  'context_title': 'Chương VI: Phân thức đại số',
  'context': 'Chương VI · SGK Toán 8: Phân thức đại số, tính chất cơ bản, rút gọn, quy đồng mẫu thức và các '
             'phép tính cộng, trừ, nhân, chia phân thức.',
  'title': 'Bài 24: Phép nhân và phép chia phân thức đại số',
  'icon': '✖️',
  'description': 'Quy tắc nhân hai phân thức, phân thức nghịch đảo và quy tắc chia hai phân thức đại số.',
  'requirements': ['Thực hiện được phép nhân và phép chia hai phân thức đại số.',
                   'Vận dụng được các tính chất giao hoán, kết hợp, phân phối của phép nhân phân thức để rút '
                   'gọn biểu thức.',
                   'Vận dụng kiến thức của **Bài 24: Phép nhân và phép chia phân thức đại số** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Muốn nhân hai phân thức, ta nhân các tử thức với nhau, các mẫu thức với nhau: '
                '$\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$. Muốn chia phân thức '
                '$\\dfrac{A}{B}$ cho phân thức $\\dfrac{C}{D}$ khác $0$, ta nhân $\\dfrac{A}{B}$ với phân '
                'thức nghịch đảo $\\dfrac{D}{C}$.',
  'theory': '1. Phép nhân phân thức: $\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$. '
            'Có các tính chất giao hoán, kết hợp và phân phối đối với phép cộng.\n'
            '2. Phân thức nghịch đảo: Hai phân thức được gọi là nghịch đảo của nhau nếu tích của chúng bằng '
            '$1$. Với $\\dfrac{C}{D} \\neq 0$, phân thức nghịch đảo của $\\dfrac{C}{D}$ là $\\dfrac{D}{C}$.\n'
            '3. Phép chia phân thức: $\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot \\dfrac{D}{C}$ '
            '(với $\\dfrac{C}{D} \\neq 0$).',
  'formulas': [{'category': 'Công thức nhân và chia phân thức đại số',
                'items': [{'name': 'Phép nhân hai phân thức',
                           'formula': '$\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot '
                                      'D}$'},
                          {'name': 'Phép chia hai phân thức',
                           'formula': '$\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot \\dfrac{D}{C} = '
                                      '\\dfrac{A \\cdot D}{B \\cdot C} \\quad (C \\neq 0)$'}]}],
  'example': 'Thực hiện phép tính: $M = \\dfrac{x^2 - 1}{2x} : \\dfrac{x - 1}{4x^2}$ (với $x \\neq 0, x '
             '\\neq 1$).',
  'example_answer': 'Ta có: $M = \\dfrac{(x - 1)(x + 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.',
  'real_life': 'Tính tỉ số năng suất lao động hoặc tỉ số thời gian hoàn thành công việc giữa hai phương án '
               'sản xuất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phân thức nghịch đảo của phân thức $\\dfrac{2x - 3}{x + 5}$ (với $x \\neq \\dfrac{3}{2}, x '
                 '\\neq -5$) là:',
            'options': ['$\\dfrac{3 - 2x}{x + 5}$',
                        '$\\dfrac{-2x + 3}{-x - 5}$',
                        '$\\dfrac{x - 5}{2x + 3}$',
                        '$\\dfrac{x + 5}{2x - 3}$'],
            'answer': 3,
            'solution': 'Phân thức nghịch đảo của $\\dfrac{A}{B}$ là $\\dfrac{B}{A}$, tức là $\\dfrac{x + '
                        '5}{2x - 3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép nhân $\\dfrac{3x}{4y^2} \\cdot \\dfrac{8y}{9x^2}$ (với $x, y \\neq 0$) '
                 'là:',
            'options': ['$\\dfrac{2}{3xy}$', '$\\dfrac{3}{2xy}$', '$\\dfrac{2x}{3y}$', '$\\dfrac{24}{36}$'],
            'answer': 0,
            'solution': '$\\dfrac{3x \\cdot 8y}{4y^2 \\cdot 9x^2} = \\dfrac{24xy}{36x^2y^2} = '
                        '\\dfrac{2}{3xy}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Phép nhân và phép chia phân thức đại số**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Phép nhân hai phân thức**?',
            'options': ['$\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$',
                        '$\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$',
                        '$\\dfrac{B}{A} \\cdot \\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A}{B} \\cdot '
                        '\\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 24: Phép nhân và phép chia phân thức đại số, '
                        '**Phép nhân hai phân thức** được xác định bởi: $\\dfrac{A}{B} \\cdot \\dfrac{C}{D} '
                        '= \\dfrac{A \\cdot C}{B \\cdot D}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Phép nhân và phép chia phân thức đại số**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Phép chia hai phân thức**?',
            'options': ['$\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} : \\dfrac{D}{C} = \\dfrac{A \\cdot '
                        'D}{B \\cdot C} \\quad (C \\neq 0)$',
                        '$\\dfrac{B}{A} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot \\dfrac{D}{C} = \\dfrac{A '
                        '\\cdot D}{B \\cdot C} \\quad (C \\neq 0)$',
                        '$\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot \\dfrac{D}{C} = \\dfrac{A '
                        '\\cdot D}{B \\cdot C} \\quad (C \\neq 0)$',
                        '$\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot \\dfrac{D}{C} = \\dfrac{A '
                        '\\cdot D}{B \\cdot C} \\quad (C \\neq 2)$'],
            'answer': 2,
            'solution': 'Trong Bài 24: Phép nhân và phép chia phân thức đại số, **Phép chia hai phân thức** '
                        'có công thức/quy tắc là: $\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A}{B} \\cdot '
                        '\\dfrac{D}{C} = \\dfrac{A \\cdot D}{B \\cdot C} \\quad (C \\neq 0)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép chia $\\dfrac{x^2 - 4}{x + 1} : \\dfrac{x - 2}{x + 1}$ (với $x \\neq -1, '
                 'x \\neq 2$) là:',
            'options': ['$x - 2$', '$\\dfrac{x + 2}{(x + 1)^2}$', '$1$', '$x + 2$'],
            'answer': 3,
            'solution': '$\\dfrac{(x - 2)(x + 2)}{x + 1} \\cdot \\dfrac{x + 1}{x - 2} = x + 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 24: Phép nhân và phép chia phân thức đại số**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép nhân và phép chia hai phân thức đại số.',
                        'Thực hiện được phép nhân và phép chia hai phân thức đại số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép nhân và phép chia hai phân thức đại '
                        'số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép nhân và '
                        'phép chia hai phân thức đại số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 24: Phép nhân và phép chia phân thức đại số: Thực '
                        'hiện được phép nhân và phép chia hai phân thức đại số.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $P = \\left(\\dfrac{1}{x - 1} + \\dfrac{1}{x + 1}\\right) \\cdot \\dfrac{x^2 '
                 '- 1}{2}$ (với $x \\neq \\pm 1$). Xét các khẳng định sau:',
            'statements': ['Tổng trong ngoặc bằng $\\dfrac{2x}{x^2 - 1}$.',
                           'Sau khi nhân với $\\dfrac{x^2 - 1}{2}$, biểu thức rút gọn thành $P = x$.',
                           'Tại $x = 5$, giá trị của biểu thức $P$ bằng $5$.',
                           'Tại $x = 1$, giá trị của biểu thức $P$ bằng $1$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $x = 1$ không thỏa mãn điều kiện xác định ($x \\neq \\pm '
                        '1$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 24: Phép nhân và phép chia '
                 'phân thức đại số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép nhân và phép chia '
                           'hai phân thức đại số.',
                           'Trong **Bài 24: Phép nhân và phép chia phân thức đại số**, quy tắc/công thức '
                           '**Phép nhân hai phân thức** được viết là: $\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = '
                           '\\dfrac{A \\cdot C}{B \\cdot D}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A '
                           '\\cdot C}{B \\cdot D}$ thì kết quả của **Phép nhân hai phân thức** trong **Bài '
                           '24: Phép nhân và phép chia phân thức đại số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Thực hiện phép tính: $M = \\dfrac{x^2 - 1}{2x} : \\dfrac{x - '
                           '1}{4x^2}$ (với $x \\neq 0, x \\neq 1$).”, kết quả giải đúng là: Ta có: $M = '
                           '\\dfrac{(x - 1)(x + 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: Phép nhân và phép chia phân thức đại '
                        'số. b) **Đúng** theo công thức **Phép nhân hai phân thức** ($\\dfrac{A}{B} \\cdot '
                        '\\dfrac{C}{D} = \\dfrac{A \\cdot C}{B \\cdot D}$). c) **Sai** vì công thức đúng của '
                        '**Phép nhân hai phân thức** phải là $\\dfrac{A}{B} \\cdot \\dfrac{C}{D} = \\dfrac{A '
                        '\\cdot C}{B \\cdot D}$ chứ không phải $\\dfrac{A}{B} : \\dfrac{C}{D} = \\dfrac{A '
                        '\\cdot C}{B \\cdot D}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 24: Phép nhân và phép chia phân thức đại số** để '
                 'giải bài toán sau: Thực hiện phép tính: $M = \\dfrac{x^2 - 1}{2x} : \\dfrac{x - 1}{4x^2}$ '
                 '(với $x \\neq 0, x \\neq 1$). Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có: $M = \\dfrac{(x - 1)(x - 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.',
                        'Ta có: $M = \\dfrac{(x - 1)(x + 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.',
                        'Ta có: $M = \\dfrac{2x}{(x - 1)(x + 1)} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.',
                        'Ta có: $M = \\dfrac{(x - 2)(x + 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Phép nhân và phép chia phân thức đại số: Ta có: $M = '
                        '\\dfrac{(x - 1)(x + 1)}{2x} \\cdot \\dfrac{4x^2}{x - 1} = 2x(x + 1)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn biểu thức $A = \\dfrac{3x + 6}{x - 1} \\cdot \\dfrac{x - 1}{x + 2}$ (với $x \\neq '
                 '1, x \\neq -2$) ta được một hằng số bằng bao nhiêu?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Ta có $A = \\dfrac{3(x + 2)}{x - 1} \\cdot \\dfrac{x - 1}{x + 2} = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch07-phuong-trinh-ham-so-bac-nhat',
  'context_title': 'Chương VII: Phương trình bậc nhất và hàm số bậc nhất',
  'context': 'Chương VII · SGK Toán 8: Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương '
             'trình, hàm số bậc nhất và hệ số góc của đường thẳng.',
  'title': 'Bài 25: Phương trình bậc nhất một ẩn',
  'icon': '⚖️',
  'description': 'Khái niệm phương trình một ẩn, nghiệm của phương trình và cách giải phương trình bậc nhất '
                 'một ẩn.',
  'requirements': ['Nhận biết được phương trình một ẩn, nghiệm của phương trình và phương trình bậc nhất một '
                   'ẩn $ax + b = 0$ ($a \\neq 0$).',
                   'Giải được phương trình bậc nhất một ẩn và các phương trình đưa được về dạng phương trình '
                   'bậc nhất một ẩn.',
                   'Vận dụng kiến thức của **Bài 25: Phương trình bậc nhất một ẩn** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Phương trình dạng $ax + b = 0$, với $a$ và $b$ là hai số đã cho và $a \\neq 0$, được gọi là '
                'phương trình bậc nhất một ẩn $x$. Phương trình bậc nhất $ax + b = 0$ ($a \\neq 0$) luôn có '
                'một nghiệm duy nhất $x = -\\dfrac{b}{a}$.',
  'theory': '1. Hai quy tắc biến đổi phương trình:\n'
            '- Quy tắc chuyển vế: Trong một phương trình, ta có thể chuyển một hạng tử từ vế này sang vế kia '
            'và đổi dấu hạng tử đó.\n'
            '- Quy tắc nhân (hoặc chia) với một số: Trong một phương trình, ta có thể nhân (hoặc chia) cả '
            'hai vế với cùng một số khác $0$.\n'
            '2. Cách giải phương trình bậc nhất $ax + b = 0$ ($a \\neq 0$): $ax + b = 0 \\Leftrightarrow ax '
            '= -b \\Leftrightarrow x = -\\dfrac{b}{a}$.',
  'formulas': [{'category': 'Phương trình bậc nhất một ẩn',
                'items': [{'name': 'Dạng tổng quát', 'formula': '$ax + b = 0 \\quad (a \\neq 0)$'},
                          {'name': 'Nghiệm duy nhất', 'formula': '$x = -\\dfrac{b}{a}$'},
                          {'name': 'Quy tắc biến đổi tương đương',
                           'formula': '$A(x) + B(x) = C(x) \\Leftrightarrow A(x) = C(x) - B(x)$'}]}],
  'example': 'Giải phương trình: $3(x - 1) - (x - 5) = 10$.',
  'example_answer': 'Khai triển và thu gọn:\n'
                    '$3x - 3 - x + 5 = 10 \\Leftrightarrow 2x + 2 = 10 \\Leftrightarrow 2x = 8 '
                    '\\Leftrightarrow x = 4$.\n'
                    'Vậy phương trình có nghiệm là $x = 4$.',
  'real_life': 'Tính số sản phẩm cần bán ra để đạt mức lợi nhuận mục tiêu khi biết chi phí cố định và lãi '
               'trên mỗi sản phẩm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình nào sau đây là phương trình bậc nhất một ẩn?',
            'options': ['$2x - 5 = 0$', '$0x + 3 = 0$', '$x^2 - 4 = 0$', '$\\dfrac{1}{x} + 2 = 0$'],
            'answer': 0,
            'solution': 'Phương trình bậc nhất một ẩn có dạng $ax + b = 0$ với $a \\neq 0$. Ở đây $2x - 5 = '
                        '0$ có $a = 2 \\neq 0, b = -5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $3x - 12 = 0$ là:',
            'options': ['$x = -4$', '$x = 4$', '$x = 9$', '$x = 3$'],
            'answer': 1,
            'solution': '$3x - 12 = 0 \\Leftrightarrow 3x = 12 \\Leftrightarrow x = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Phương trình bậc nhất một ẩn**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Dạng tổng quát**?',
            'options': ['$ax - b = 0 \\quad (a \\neq 0)$',
                        '$ax + b = 0 \\quad (a \\neq 1)$',
                        '$ax + b = 0 \\quad (a \\neq 0)$',
                        '$ax + b = 2 \\quad (a \\neq 0)$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 25: Phương trình bậc nhất một ẩn, **Dạng tổng '
                        'quát** được xác định bởi: $ax + b = 0 \\quad (a \\neq 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Phương trình bậc nhất một ẩn**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Nghiệm duy nhất**?',
            'options': ['$x = -\\dfrac{b}{a}$ (với dấu ngược lại)',
                        '$x = -\\dfrac{a}{b}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $x = -\\dfrac{b}{a}$',
                        '$x = -\\dfrac{b}{a}$'],
            'answer': 3,
            'solution': 'Trong Bài 25: Phương trình bậc nhất một ẩn, **Nghiệm duy nhất** có công thức/quy '
                        'tắc là: $x = -\\dfrac{b}{a}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $5x - 3 = 2x + 9$ là:',
            'options': ['$x = 4$', '$x = 2$', '$x = -4$', '$x = \\dfrac{6}{7}$'],
            'answer': 0,
            'solution': 'Chuyển vế: $5x - 2x = 9 + 3 \\Leftrightarrow 3x = 12 \\Leftrightarrow x = 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 25: Phương trình bậc nhất một ẩn**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được phương trình một ẩn, nghiệm của phương trình và phương trình bậc '
                        'nhất một ẩn $ax - b = 0$ ($a \\neq 0$).',
                        'Nhận biết được phương trình một ẩn, nghiệm của phương trình và phương trình bậc '
                        'nhất một ẩn $ax + b = 0$ ($a \\neq 0$).',
                        'Nhận biết được phương trình một ẩn, nghiệm của phương trình và phương trình bậc '
                        'nhất một ẩn $ax + b = 0$ ($a \\neq 1$).',
                        'Nhận biết được phương trình một ẩn, nghiệm của phương trình và phương trình bậc '
                        'nhất một ẩn $ax + b = 2$ ($a \\neq 0$).'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 25: Phương trình bậc nhất một ẩn: Nhận biết được '
                        'phương trình một ẩn, nghiệm của phương trình và phương trình bậc nhất một ẩn $ax + '
                        'b = 0$ ($a \\neq 0$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình $\\dfrac{2x - 1}{3} - \\dfrac{x + 2}{2} = 1$. Xét các khẳng định sau:',
            'statements': ['Mẫu số chung của các phân số trong phương trình là $6$.',
                           'Nhân cả hai vế với $6$ ta được $2(2x - 1) - 3(x + 2) = 6$.',
                           'Thu gọn vế trái ta được phương trình bậc nhất $x - 8 = 6$.',
                           'Nghiệm của phương trình đã cho là $x = 2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì từ $x - 8 = 6$ suy ra $x = 14 \\neq 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 25: Phương trình bậc nhất '
                 'một ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được phương trình một ẩn, '
                           'nghiệm của phương trình và phương trình bậc nhất một ẩn $ax + b = 0$ ($a \\neq '
                           '0$).',
                           'Trong **Bài 25: Phương trình bậc nhất một ẩn**, quy tắc/công thức **Dạng tổng '
                           'quát** được viết là: $ax + b = 0 \\quad (a \\neq 0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $ax - b = 0 \\quad (a \\neq 0)$ thì kết quả '
                           'của **Dạng tổng quát** trong **Bài 25: Phương trình bậc nhất một ẩn** vẫn không '
                           'thay đổi.',
                           'Xét ví dụ của bài: “Giải phương trình: $3(x - 1) - (x - 5) = 10$.”, kết quả giải '
                           'đúng là: Khai triển và thu gọn: $3x - 3 - x + 5 = 10 \\Leftrightarrow 2x + 2 = '
                           '10 \\Leftrightarrow 2x = 8 \\Leftrightarrow x = 4$. Vậy phương trình...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Phương trình bậc nhất một ẩn. b) '
                        '**Đúng** theo công thức **Dạng tổng quát** ($ax + b = 0 \\quad (a \\neq 0)$). c) '
                        '**Sai** vì công thức đúng của **Dạng tổng quát** phải là $ax + b = 0 \\quad (a '
                        '\\neq 0)$ chứ không phải $ax - b = 0 \\quad (a \\neq 0)$. d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 25: Phương trình bậc nhất một ẩn** để giải bài toán '
                 'sau: Giải phương trình: $3(x - 1) - (x - 5) = 10$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Khai triển và thu gọn: $3x - 3 - x - 5 = 10 \\Leftrightarrow 2x + 2 = 10 '
                        '\\Leftrightarrow 2x = 8 \\Leftrightarrow x = 4$. Vậy phương trình có nghiệm là $x = '
                        '4$...',
                        'Khai triển và thu gọn: $3x - 3 - x + 5 = 10 \\Leftrightarrow 2x + 2 = 10 '
                        '\\Leftrightarrow 2x = 8 \\Leftrightarrow x = 4$. Vậy phương trình có nghiệm là $x = '
                        '3$...',
                        'Khai triển và thu gọn: $3x - 3 - x + 5 = 10 \\Leftrightarrow 2x + 2 = 10 '
                        '\\Leftrightarrow 2x = 8 \\Leftrightarrow x = 4$. Vậy phương trình có nghiệm là $x = '
                        '4$...',
                        'Khai triển và thu gọn: $3x - 6 - x + 5 = 10 \\Leftrightarrow 2x + 2 = 10 '
                        '\\Leftrightarrow 2x = 8 \\Leftrightarrow x = 4$. Vậy phương trình có nghiệm là $x = '
                        '4$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Phương trình bậc nhất một ẩn: Khai triển và thu '
                        'gọn:\n'
                        '$3x - 3 - x + 5 = 10 \\Leftrightarrow 2x + 2 = 10 \\Leftrightarrow 2x = 8 '
                        '\\Leftrightarrow x = 4$.\n'
                        'Vậy phương trình có nghiệm là $x = 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm nghiệm của phương trình $4(x + 2) - 2(x - 1) = 20$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $4x + 8 - 2x + 2 = 20 \\Leftrightarrow 2x + 10 = 20 \\Leftrightarrow 2x = 10 '
                        '\\Leftrightarrow x = 5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch07-phuong-trinh-ham-so-bac-nhat',
  'context_title': 'Chương VII: Phương trình bậc nhất và hàm số bậc nhất',
  'context': 'Chương VII · SGK Toán 8: Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương '
             'trình, hàm số bậc nhất và hệ số góc của đường thẳng.',
  'title': 'Bài 26: Giải bài toán bằng cách lập phương trình',
  'icon': '📝',
  'description': 'Các bước giải bài toán thực tế (chuyển động, năng suất, phần trăm) bằng cách lập phương '
                 'trình bậc nhất một ẩn.',
  'requirements': ['Nắm vững ba bước giải bài toán bằng cách lập phương trình bậc nhất một ẩn.',
                   'Giải quyết được các bài toán thực tiễn (chuyển động, năng suất, toán có nội dung hình '
                   'học, phần trăm) bằng cách lập phương trình.',
                   'Vận dụng kiến thức của **Bài 26: Giải bài toán bằng cách lập phương trình** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giải bài toán bằng cách lập phương trình gồm 3 bước: Bước 1 (Lập phương trình: chọn ẩn và '
                'đặt điều kiện, biểu diễn các đại lượng chưa biết theo ẩn và lập phương trình); Bước 2 (Giải '
                'phương trình); Bước 3 (Kiểm tra điều kiện và kết luận).',
  'theory': '1. Ba bước giải bài toán bằng cách lập phương trình:\n'
            '- Bước 1: Chọn ẩn số $x$ và đặt điều kiện thích hợp cho ẩn; biểu diễn các đại lượng chưa biết '
            'theo ẩn và các đại lượng đã biết; lập phương trình biểu thị mối quan hệ giữa các đại lượng.\n'
            '- Bước 2: Giải phương trình vừa lập được.\n'
            '- Bước 3: Kiểm tra xem nghiệm có thỏa mãn điều kiện của ẩn hay không, rồi trả lời bài toán.\n'
            '2. Các mối quan hệ thường gặp:\n'
            '- Toán chuyển động: $\\text{Quãng đường} = \\text{Vận tốc} \\times \\text{Thời gian}$ ($s = v '
            '\\cdot t$).\n'
            '- Toán năng suất: $\\text{Khối lượng công việc} = \\text{Năng suất} \\times \\text{Thời gian}$.',
  'formulas': [{'category': 'Các công thức lập phương trình thực tế',
                'items': [{'name': 'Toán chuyển động',
                           'formula': '$s = v \\cdot t \\Rightarrow t = \\dfrac{s}{v}; \\quad v = '
                                      '\\dfrac{s}{t}$'},
                          {'name': 'Toán năng suất',
                           'formula': '$A = N \\cdot t$ ($A$: tổng sản phẩm, $N$: năng suất mỗi ngày/giờ, '
                                      '$t$: thời gian)'},
                          {'name': 'Toán giảm giá $p\\%$',
                           'formula': '$\\text{Giá sau giảm} = \\text{Giá niêm yết} \\cdot (1 - p\\%)$'}]}],
  'example': 'Một ô tô đi từ $A$ đến $B$ với vận tốc $50\\text{ km/h}$ rồi quay về từ $B$ đến $A$ với vận '
             'tốc $40\\text{ km/h}$. Tổng thời gian cả đi và về là $4,5$ giờ. Tính độ dài quãng đường $AB$.',
  'example_answer': 'Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x > 0$).\n'
                    'Thời gian đi là $\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ).\n'
                    'Theo đề bài ta có phương trình: $\\dfrac{x}{50} + \\dfrac{x}{40} = 4,5 \\Leftrightarrow '
                    '\\dfrac{4x + 5x}{200} = \\dfrac{900}{200} \\Leftrightarrow 9x = 900 \\Leftrightarrow x '
                    '= 100$ (thỏa mãn).\n'
                    'Vậy quãng đường $AB$ dài $100\\text{ km}$.',
  'real_life': 'Tính toán thời gian hoàn thành dự án khi tăng năng suất lao động hoặc tính giá gốc của mặt '
               'hàng trước khi khuyến mãi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu gọi $x\\text{ (km)}$ ($x > 0$) là độ dài quãng đường $AB$ thì thời gian một người đi '
                 'xe đạp hết quãng đường đó với vận tốc $15\\text{ km/h}$ là:',
            'options': ['$15x$ (giờ)', '$\\dfrac{x}{15}$ (giờ)', '$\\dfrac{15}{x}$ (giờ)', '$x - 15$ (giờ)'],
            'answer': 1,
            'solution': 'Thời gian bằng quãng đường chia cho vận tốc: $t = \\dfrac{x}{15}$ (giờ).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng của hai số bằng $50$. Nếu gọi số thứ nhất là $x$ thì số thứ hai được biểu diễn theo '
                 '$x$ là:',
            'options': ['$x - 50$', '$50 + x$', '$50 - x$', '$\\dfrac{50}{x}$'],
            'answer': 2,
            'solution': 'Vì tổng hai số bằng $50$ nên số thứ hai là $50 - x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Giải bài toán bằng cách lập phương trình**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Toán chuyển động**?',
            'options': ['$s = v : t \\Rightarrow t = \\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$',
                        '$s = v \\cdot t \\Rightarrow t = \\dfrac{v}{s}; \\quad v = \\dfrac{s}{t}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $s = v \\cdot t \\Rightarrow t '
                        '= \\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$',
                        '$s = v \\cdot t \\Rightarrow t = \\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 26: Giải bài toán bằng cách lập phương trình, '
                        '**Toán chuyển động** được xác định bởi: $s = v \\cdot t \\Rightarrow t = '
                        '\\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Giải bài toán bằng cách lập phương trình**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Toán năng suất**?',
            'options': ['$A = N \\cdot t$ ($A$: tổng sản phẩm, $N$: năng suất mỗi ngày/giờ, $t$: thời gian)',
                        '$A = N : t$ ($A$: tổng sản phẩm, $N$: năng suất mỗi ngày/giờ, $t$: thời gian)',
                        'Đảo ngược vế của quy tắc: $A = N \\cdot t$ ($A$: tổng sản phẩm, $N$: năng suất mỗi '
                        'ngày/giờ, $t$: thời gian)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $A = N \\cdot t$ ($A$: tổng sản '
                        'phẩm, $N$: năng suất mỗi ngày/giờ, $t$: thời gian)'],
            'answer': 0,
            'solution': 'Trong Bài 26: Giải bài toán bằng cách lập phương trình, **Toán năng suất** có công '
                        'thức/quy tắc là: $A = N \\cdot t$ ($A$: tổng sản phẩm, $N$: năng suất mỗi ngày/giờ, '
                        '$t$: thời gian).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình chữ nhật có chiều dài hơn chiều rộng $6\\text{ m}$ và chu vi bằng $40\\text{ m}$. '
                 'Nếu gọi chiều rộng là $x\\text{ (m)}$ ($x > 0$) thì phương trình tìm $x$ là:',
            'options': ['$x + (x + 6) = 40$',
                        '$2(x + x + 6) = 40$',
                        '$x(x + 6) = 40$',
                        '$2(x + x - 6) = 40$'],
            'answer': 1,
            'solution': 'Chiều dài là $x + 6$, chu vi hình chữ nhật là $2(x + x + 6) = 40$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 26: Giải bài toán bằng cách lập phương trình**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Nắm vững ba bước giải bài toán bằng cách lập phương trình bậc nhất một ẩn. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nắm vững ba bước giải bài toán bằng cách lập phương trình '
                        'bậc nhất một ẩn.',
                        'Nắm vững ba bước giải bài toán bằng cách lập phương trình bậc nhất một ẩn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nắm vững ba bước giải bài toán '
                        'bằng cách lập phương trình bậc nhất một ẩn.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 26: Giải bài toán bằng cách lập phương trình: Nắm '
                        'vững ba bước giải bài toán bằng cách lập phương trình bậc nhất một ẩn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một xưởng may theo kế hoạch mỗi ngày phải may $30$ bộ quần áo. Nhờ cải tiến kĩ thuật, thực '
                 'tế mỗi ngày xưởng may được $40$ bộ nên đã hoàn thành trước kế hoạch $3$ ngày (với cùng '
                 'tổng số bộ quần áo). Gọi $x$ (bộ, $x \\in \\mathbb{N}^*$) là số bộ quần áo theo kế hoạch. '
                 'Xét các khẳng định sau:',
            'statements': ['Thời gian may theo kế hoạch là $\\dfrac{x}{30}$ (ngày).',
                           'Thời gian may thực tế là $\\dfrac{x}{40}$ (ngày).',
                           'Phương trình biểu thị bài toán là $\\dfrac{x}{30} - \\dfrac{x}{40} = 3$.',
                           'Giải phương trình ta tìm được số bộ quần áo theo kế hoạch là $x = 240$ (bộ).'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $\\dfrac{x}{30} - \\dfrac{x}{40} = 3 \\Leftrightarrow '
                        '\\dfrac{x}{120} = 3 \\Leftrightarrow x = 360$ (bộ).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 26: Giải bài toán bằng cách '
                 'lập phương trình**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nắm vững ba bước giải bài toán bằng cách '
                           'lập phương trình bậc nhất một ẩn.',
                           'Trong **Bài 26: Giải bài toán bằng cách lập phương trình**, quy tắc/công thức '
                           '**Toán chuyển động** được viết là: $s = v \\cdot t \\Rightarrow t = '
                           '\\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $s = v : t \\Rightarrow t = \\dfrac{s}{v}; '
                           '\\quad v = \\dfrac{s}{t}$ thì kết quả của **Toán chuyển động** trong **Bài 26: '
                           'Giải bài toán bằng cách lập phương trình** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một ô tô đi từ $A$ đến $B$ với vận tốc $50\\text{ km/h}$ rồi '
                           'quay về từ $B$ đến $A$ với vận tốc $40\\text{ km/h}$. Tổng thời gian cả đi '
                           'v...”, kết quả giải đúng là: Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x '
                           '> 0$). Thời gian đi là $\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ '
                           '(giờ)....'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Giải bài toán bằng cách lập phương '
                        'trình. b) **Đúng** theo công thức **Toán chuyển động** ($s = v \\cdot t '
                        '\\Rightarrow t = \\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$). c) **Sai** vì công thức '
                        'đúng của **Toán chuyển động** phải là $s = v \\cdot t \\Rightarrow t = '
                        '\\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$ chứ không phải $s = v : t \\Rightarrow t = '
                        '\\dfrac{s}{v}; \\quad v = \\dfrac{s}{t}$. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 26: Giải bài toán bằng cách lập phương trình** để '
                 'giải bài toán sau: Một ô tô đi từ $A$ đến $B$ với vận tốc $50\\text{ km/h}$ rồi quay về từ '
                 '$B$ đến $A$ với vận tốc $40\\text{ km/h}$. Tổng thời gian cả đi và về là $4,5$ giờ. Tính '
                 'độ dài quãng đường $AB$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x < 0$). Thời gian đi là '
                        '$\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ). Theo đề bài ta...',
                        'Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x > 0$). Thời gian đi là '
                        '$\\dfrac{50}{x}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ). Theo đề bài ta...',
                        'Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x > 2$). Thời gian đi là '
                        '$\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ). Theo đề bài ta...',
                        'Gọi độ dài quãng đường $AB$ là $x\\text{ (km)}$ ($x > 0$). Thời gian đi là '
                        '$\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ). Theo đề bài ta...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Giải bài toán bằng cách lập phương trình: Gọi độ dài '
                        'quãng đường $AB$ là $x\\text{ (km)}$ ($x > 0$).\n'
                        'Thời gian đi là $\\dfrac{x}{50}$ (giờ), thời gian về là $\\dfrac{x}{40}$ (giờ).\n'
                        'Theo đề bài ta có phương trình: $\\dfrac{x}{50} + \\dfrac{x}{40} = 4,5 '
                        '\\Leftrightarrow \\dfrac{4x + 5x}{200} = \\dfrac{900}{200} \\Leftrightarrow 9x = '
                        '900 \\Leftrightarrow x = 100$ (thỏa mãn).\n'
                        'Vậy quãng đường $AB$ dài $100\\text{ km}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Năm nay tuổi bố gấp $4$ lần tuổi con. Biết rằng $5$ năm nữa, tổng số tuổi của hai bố con '
                 'là $55$ tuổi. Tính số tuổi của con hiện nay.',
            'answer': ['9'],
            'unit': None,
            'solution': 'Gọi tuổi con hiện nay là $x$ ($x > 0$), tuổi bố hiện nay là $4x$. Sau $5$ năm nữa: '
                        '$(x + 5) + (4x + 5) = 55 \\Leftrightarrow 5x + 10 = 55 \\Leftrightarrow 5x = 45 '
                        '\\Leftrightarrow x = 9$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch07-phuong-trinh-ham-so-bac-nhat',
  'context_title': 'Chương VII: Phương trình bậc nhất và hàm số bậc nhất',
  'context': 'Chương VII · SGK Toán 8: Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương '
             'trình, hàm số bậc nhất và hệ số góc của đường thẳng.',
  'title': 'Bài 27: Khái niệm hàm số và đồ thị của hàm số',
  'icon': '📈',
  'description': 'Khái niệm hàm số, giá trị của hàm số, mặt phẳng tọa độ Oxy, tọa độ của một điểm và đồ thị '
                 'của hàm số.',
  'requirements': ['Nhận biết được những mô hình thực tế dẫn đến khái niệm hàm số và tính được giá trị của '
                   'hàm số tại giá trị cho trước của biến.',
                   'Xác định được tọa độ của một điểm trên mặt phẳng tọa độ $Oxy$ và xác định một điểm khi '
                   'biết tọa độ của nó.',
                   'Nhận biết được đồ thị của hàm số $y = f(x)$.'],
  'definition': 'Nếu đại lượng $y$ phụ thuộc vào đại lượng thay đổi $x$ sao cho với mỗi giá trị của $x$ ta '
                'luôn xác định được chỉ một giá trị tương ứng của $y$ thì $y$ được gọi là hàm số của $x$ và '
                '$x$ gọi là biến số.',
  'theory': '1. Kí hiệu hàm số: Khi $y$ là hàm số của $x$, ta thường viết $y = f(x), y = g(x), \\ldots$ Giá '
            'trị của hàm số $y = f(x)$ tại $x = a$ được kí hiệu là $f(a)$.\n'
            '2. Mặt phẳng tọa độ $Oxy$: Gồm trục hoành $Ox$ (nằm ngang) và trục tung $Oy$ (thẳng đứng) vuông '
            'góc với nhau tại gốc tọa độ $O(0; 0)$. Mỗi điểm $M$ được xác định bởi cặp số $(x_0; y_0)$, '
            'trong đó $x_0$ là hoành độ và $y_0$ là tung độ.\n'
            '3. Đồ thị của hàm số: Đồ thị của hàm số $y = f(x)$ là tập hợp tất cả các điểm biểu diễn các cặp '
            'giá trị tương ứng $(x; y)$ trên mặt phẳng tọa độ.',
  'formulas': [{'category': 'Hàm số và tọa độ điểm trên mặt phẳng $Oxy$',
                'items': [{'name': 'Giá trị hàm số $y = f(x)$ tại $x = x_0$', 'formula': '$y_0 = f(x_0)$'},
                          {'name': 'Điểm thuộc trục hoành $Ox$', 'formula': '$M(x_0; 0)$ (tung độ bằng $0$)'},
                          {'name': 'Điểm thuộc trục tung $Oy$', 'formula': '$N(0; y_0)$ (hoành độ bằng $0$)'},
                          {'name': 'Điểm $M(x_0; y_0)$ thuộc đồ thị $y = f(x)$',
                           'formula': '$y_0 = f(x_0)$'}]}],
  'example': 'Cho hàm số $y = f(x) = 2x^2 - 1$. Tính $f(0), f(-2)$ và kiểm tra điểm $A(2; 7)$ có thuộc đồ '
             'thị hàm số không.',
  'example_answer': '- Ta có $f(0) = 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$.\n'
                    '- Vì $f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thuộc đồ thị của hàm số.',
  'real_life': 'Xác định vị trí trên bản đồ GPS bằng cặp tọa độ (kinh độ, vĩ độ) hoặc vị trí ghế ngồi trong '
               'rạp chiếu phim (số hàng, số cột).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trên mặt phẳng tọa độ $Oxy$, điểm $M(3; -5)$ có hoành độ và tung độ lần lượt là:',
            'options': ['Hoành độ bằng $-5$, tung độ bằng $3$',
                        'Hoành độ bằng $3$, tung độ bằng $5$',
                        'Hoành độ bằng $3$, tung độ bằng $-5$',
                        'Hoành độ bằng $0$, tung độ bằng $-5$'],
            'answer': 2,
            'solution': 'Trong kí hiệu $M(x_0; y_0)$, số đứng trước $x_0 = 3$ là hoành độ, số đứng sau $y_0 '
                        '= -5$ là tung độ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho hàm số $y = f(x) = 3x - 4$. Giá trị của $f(2)$ bằng:',
            'options': ['$-2$', '$6$', '$10$', '$2$'],
            'answer': 3,
            'solution': 'Thay $x = 2$ vào công thức hàm số: $f(2) = 3 \\cdot 2 - 4 = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Khái niệm hàm số và đồ thị của hàm số**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Giá trị hàm số $y = f(x)$ tại $x = x_0$**?',
            'options': ['$y_0 = f(x_0)$',
                        '$y_0 = f(x_0)$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $y_0 = f(x_0)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $y_0 = f(x_0)$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 27: Khái niệm hàm số và đồ thị của hàm số, **Giá '
                        'trị hàm số $y = f(x)$ tại $x = x_0$** được xác định bởi: $y_0 = f(x_0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Khái niệm hàm số và đồ thị của hàm số**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Điểm thuộc trục hoành $Ox$**?',
            'options': ['$M(x_0; 1)$ (tung độ bằng $0$)',
                        '$M(x_0; 0)$ (tung độ bằng $0$)',
                        '$M(x_0; 0)$ (tung độ bằng $1$)',
                        '$M(x_0; 2)$ (tung độ bằng $0$)'],
            'answer': 1,
            'solution': 'Trong Bài 27: Khái niệm hàm số và đồ thị của hàm số, **Điểm thuộc trục hoành $Ox$** '
                        'có công thức/quy tắc là: $M(x_0; 0)$ (tung độ bằng $0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Điểm nào sau đây thuộc đồ thị của hàm số $y = -2x + 3$?',
            'options': ['$B(1; -1)$', '$C(2; 1)$', '$A(1; 1)$', '$D(0; -3)$'],
            'answer': 2,
            'solution': 'Thay $x = 1$ vào $y = -2x + 3$ ta được $y = -2 \\cdot 1 + 3 = 1$, nên điểm $A(1; '
                        '1)$ thuộc đồ thị hàm số.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 27: Khái niệm hàm số và đồ thị của hàm số**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết được những mô hình thực tế dẫn đến khái niệm hàm số và tính được giá trị '
                        'của hàm số tại giá trị cho trước của biến. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được những mô hình thực tế dẫn đến khái niệm '
                        'hàm số và tính được giá trị của hàm số tại giá trị cho trước của biến.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được những mô hình '
                        'thực tế dẫn đến khái niệm hàm số và tính được giá trị của hàm số tại giá trị cho '
                        'trước của biến.',
                        'Nhận biết được những mô hình thực tế dẫn đến khái niệm hàm số và tính được giá trị '
                        'của hàm số tại giá trị cho trước của biến.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 27: Khái niệm hàm số và đồ thị của hàm số: Nhận biết '
                        'được những mô hình thực tế dẫn đến khái niệm hàm số và tính được giá trị của hàm số '
                        'tại giá trị cho trước của biến.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trên mặt phẳng tọa độ $Oxy$, cho hàm số $y = f(x) = x^2 - 2x$. Xét các khẳng định sau:',
            'statements': ['Đồ thị hàm số đi qua gốc tọa độ $O(0; 0)$.',
                           'Giá trị của hàm số tại $x = -1$ là $f(-1) = 3$.',
                           'Điểm $M(4; 0)$ nằm trên trục hoành $Ox$.',
                           'Điểm $N(0; 5)$ nằm trên trục hoành $Ox$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $f(0) = 0$. b) Đúng vì $f(-1) = (-1)^2 - 2(-1) = 3$. c) Đúng vì tung độ '
                        'bằng $0$. d) Sai vì $N(0; 5)$ có hoành độ bằng $0$ nên nằm trên trục tung $Oy$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 27: Khái niệm hàm số và đồ '
                 'thị của hàm số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được những mô hình thực tế dẫn '
                           'đến khái niệm hàm số và tính được giá trị của hàm số tại giá trị cho trước của '
                           'biến.',
                           'Trong **Bài 27: Khái niệm hàm số và đồ thị của hàm số**, quy tắc/công thức **Giá '
                           'trị hàm số $y = f(x)$ tại $x = x_0$** được viết là: $y_0 = f(x_0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $y_0 = f(x_0)$ (với dấu ngược lại) thì kết '
                           'quả của **Giá trị hàm số $y = f(x)$ tại $x = x_0$** trong **Bài 27: Khái niệm '
                           'hàm số và đồ thị của hàm số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho hàm số $y = f(x) = 2x^2 - 1$. Tính $f(0), f(-2)$ và kiểm '
                           'tra điểm $A(2; 7)$ có thuộc đồ thị hàm số không.”, kết quả giải đúng là: - Ta có '
                           '$f(0) = 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$. - Vì $f(2) = '
                           '2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thu...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Khái niệm hàm số và đồ thị của hàm số. '
                        'b) **Đúng** theo công thức **Giá trị hàm số $y = f(x)$ tại $x = x_0$** ($y_0 = '
                        'f(x_0)$). c) **Sai** vì công thức đúng của **Giá trị hàm số $y = f(x)$ tại $x = '
                        'x_0$** phải là $y_0 = f(x_0)$ chứ không phải $y_0 = f(x_0)$ (với dấu ngược lại). d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 27: Khái niệm hàm số và đồ thị của hàm số** để giải '
                 'bài toán sau: Cho hàm số $y = f(x) = 2x^2 - 1$. Tính $f(0), f(-2)$ và kiểm tra điểm $A(2; '
                 '7)$ có thuộc đồ thị hàm số không. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- Ta có $f(0) = 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$. - Vì '
                        '$f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thuộc đồ thị của h...',
                        '- Ta có $f(0) = 2 \\cdot 0^2 + 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$. - Vì '
                        '$f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thuộc đồ thị của h...',
                        '- Ta có $f(0) = 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$. - Vì '
                        '$f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 6)$ thuộc đồ thị của h...',
                        '- Ta có $f(2) = 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$. - Vì '
                        '$f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thuộc đồ thị của h...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Khái niệm hàm số và đồ thị của hàm số: - Ta có $f(0) '
                        '= 2 \\cdot 0^2 - 1 = -1$; $f(-2) = 2 \\cdot (-2)^2 - 1 = 7$.\n'
                        '- Vì $f(2) = 2 \\cdot 2^2 - 1 = 7 = y_A$ nên điểm $A(2; 7)$ thuộc đồ thị của hàm '
                        'số.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hàm số $y = f(x) = 4x - 5$. Tìm giá trị của $x$ sao cho $f(x) = 7$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Ta có $4x - 5 = 7 \\Leftrightarrow 4x = 12 \\Leftrightarrow x = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch07-phuong-trinh-ham-so-bac-nhat',
  'context_title': 'Chương VII: Phương trình bậc nhất và hàm số bậc nhất',
  'context': 'Chương VII · SGK Toán 8: Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương '
             'trình, hàm số bậc nhất và hệ số góc của đường thẳng.',
  'title': 'Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất',
  'icon': '📉',
  'description': 'Định nghĩa hàm số bậc nhất y = ax + b (a khác 0) và cách vẽ đồ thị của hàm số bậc nhất.',
  'requirements': ['Nhận biết được hàm số bậc nhất $y = ax + b$ ($a \\neq 0$).',
                   'Thiết lập được bảng giá trị và vẽ được đồ thị của hàm số bậc nhất (là một đường thẳng).',
                   'Vận dụng được hàm số bậc nhất vào các bài toán thực tiễn.'],
  'definition': 'Hàm số bậc nhất là hàm số cho bởi công thức $y = ax + b$, trong đó $a, b$ là các số cho '
                'trước và $a \\neq 0$. Đồ thị của hàm số $y = ax + b$ ($a \\neq 0$) là một đường thẳng.',
  'theory': '1. Đồ thị của hàm số $y = ax$ ($a \\neq 0$): Khi $b = 0$, đồ thị của hàm số $y = ax$ là một '
            'đường thẳng đi qua gốc tọa độ $O(0; 0)$ và điểm $A(1; a)$.\n'
            '2. Đồ thị của hàm số $y = ax + b$ ($a \\neq 0, b \\neq 0$):\n'
            '- Là một đường thẳng cắt trục tung tại điểm có tung độ bằng $b$, tức là điểm $P(0; b)$, và cắt '
            'trục hoành tại điểm $Q\\left(-\\dfrac{b}{a}; 0\\right)$.\n'
            '- Cách vẽ: Xác định hai điểm phân biệt thuộc đồ thị (thường chọn giao điểm với hai trục tọa độ '
            '$P(0; b)$ và $Q\\left(-\\dfrac{b}{a}; 0\\right)$), rồi kẻ đường thẳng đi qua hai điểm đó.',
  'formulas': [{'category': 'Hàm số bậc nhất và giao điểm với hai trục tọa độ',
                'items': [{'name': 'Công thức hàm số bậc nhất', 'formula': '$y = ax + b \\quad (a \\neq 0)$'},
                          {'name': 'Giao điểm với trục tung $Oy$ (cho $x = 0$)', 'formula': '$P(0; b)$'},
                          {'name': 'Giao điểm với trục hoành $Ox$ (cho $y = 0$)',
                           'formula': '$Q\\left(-\\dfrac{b}{a}; 0\\right)$'}]}],
  'example': 'Cho hàm số bậc nhất $y = 2x - 4$. Tìm tọa độ giao điểm của đồ thị hàm số với trục tung $Oy$ và '
             'trục hoành $Ox$.',
  'example_answer': '- Cho $x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$.\n'
                    '- Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$: Đồ thị cắt trục hoành $Ox$ '
                    'tại điểm $Q(2; 0)$.',
  'real_life': 'Biểu diễn tổng chi phí thuê sân bóng hoặc cước viễn thông bao gồm phí thuê bao cố định $b$ '
               'và phí theo giờ sử dụng $ax$: $y = ax + b$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hàm số nào sau đây là hàm số bậc nhất?',
            'options': ['$y = 0x + 2$', '$y = 2x^2 + 1$', '$y = \\dfrac{3}{x} - 1$', '$y = -3x + 5$'],
            'answer': 3,
            'solution': 'Hàm số bậc nhất có dạng $y = ax + b$ với $a \\neq 0$. Ở đây $y = -3x + 5$ có $a = '
                        '-3 \\neq 0, b = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đồ thị của hàm số bậc nhất $y = 3x - 6$ cắt trục tung $Oy$ tại điểm có tọa độ là:',
            'options': ['$(0; -6)$', '$(-6; 0)$', '$(2; 0)$', '$(0; 2)$'],
            'answer': 0,
            'solution': 'Thay $x = 0$ vào $y = 3x - 6$ được $y = -6$, nên giao điểm với trục tung là $(0; '
                        '-6)$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Công thức hàm số bậc nhất**?',
            'options': ['$y = ax - b \\quad (a \\neq 0)$',
                        '$y = ax + b \\quad (a \\neq 0)$',
                        '$y = ax + b \\quad (a \\neq 1)$',
                        '$y = ax + b \\quad (a \\neq 2)$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất, '
                        '**Công thức hàm số bậc nhất** được xác định bởi: $y = ax + b \\quad (a \\neq 0)$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Giao điểm với trục tung $Oy$ (cho $x = 0$)**?',
            'options': ['$P(1; b)$', '$P(2; b)$', '$P(0; b)$', '$y = ax + b \\quad (a \\neq 0)$'],
            'answer': 2,
            'solution': 'Trong Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất, **Giao điểm với trục '
                        'tung $Oy$ (cho $x = 0$)** có công thức/quy tắc là: $P(0; b)$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Đồ thị của hàm số $y = 2x + 8$ cắt trục hoành $Ox$ tại điểm có tọa độ là:',
            'options': ['$(4; 0)$', '$(0; 8)$', '$(0; -4)$', '$(-4; 0)$'],
            'answer': 3,
            'solution': 'Cho $y = 0 \\Rightarrow 2x + 8 = 0 \\Rightarrow x = -4$. Vậy giao điểm với trục '
                        'hoành là $(-4; 0)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được hàm số bậc nhất $y = ax + b$ ($a \\neq 0$).',
                        'Nhận biết được hàm số bậc nhất $y = ax - b$ ($a \\neq 0$).',
                        'Nhận biết được hàm số bậc nhất $y = ax + b$ ($a \\neq 1$).',
                        'Nhận biết được hàm số bậc nhất $y = ax + b$ ($a \\neq 2$).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất: '
                        'Nhận biết được hàm số bậc nhất $y = ax + b$ ($a \\neq 0$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = (m - 1)x + 3$. Xét các khẳng định sau:',
            'statements': ['Hàm số đã cho là hàm số bậc nhất khi và chỉ khi $m \\neq 1$.',
                           'Với mọi $m \\neq 1$, đồ thị hàm số luôn cắt trục tung tại điểm $A(0; 3)$.',
                           'Khi $m = 3$, hàm số trở thành $y = 2x + 3$.',
                           'Khi $m = 3$, đồ thị hàm số đi qua gốc tọa độ $O(0; 0)$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $b = 3 \\neq 0$ nên đồ thị không đi qua gốc tọa độ $O(0; '
                        '0)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 28: Hàm số bậc nhất và đồ '
                 'thị của hàm số bậc nhất**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hàm số bậc nhất $y = ax + '
                           'b$ ($a \\neq 0$).',
                           'Trong **Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất**, quy tắc/công '
                           'thức **Công thức hàm số bậc nhất** được viết là: $y = ax + b \\quad (a \\neq '
                           '0)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $y = ax - b \\quad (a \\neq 0)$ thì kết quả '
                           'của **Công thức hàm số bậc nhất** trong **Bài 28: Hàm số bậc nhất và đồ thị của '
                           'hàm số bậc nhất** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho hàm số bậc nhất $y = 2x - 4$. Tìm tọa độ giao điểm của '
                           'đồ thị hàm số với trục tung $Oy$ và trục hoành $Ox$.”, kết quả giải đúng là: - '
                           'Cho $x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$. '
                           '- Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 28: Hàm số bậc nhất và đồ thị của hàm số '
                        'bậc nhất. b) **Đúng** theo công thức **Công thức hàm số bậc nhất** ($y = ax + b '
                        '\\quad (a \\neq 0)$). c) **Sai** vì công thức đúng của **Công thức hàm số bậc '
                        'nhất** phải là $y = ax + b \\quad (a \\neq 0)$ chứ không phải $y = ax - b \\quad (a '
                        '\\neq 0)$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất** '
                 'để giải bài toán sau: Cho hàm số bậc nhất $y = 2x - 4$. Tìm tọa độ giao điểm của đồ thị '
                 'hàm số với trục tung $Oy$ và trục hoành $Ox$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['- Cho $x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$. + '
                        'Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$: Đồ thị cắt tr...',
                        '- Cho $x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$. - '
                        'Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$: Đồ thị cắt tr...',
                        '- Cho $x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$. - '
                        'Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 1$: Đồ thị cắt tr...',
                        '- Cho $x = 2 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$. - '
                        'Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$: Đồ thị cắt tr...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28: Hàm số bậc nhất và đồ thị của hàm số bậc nhất: - Cho '
                        '$x = 0 \\Rightarrow y = -4$: Đồ thị cắt trục tung $Oy$ tại điểm $P(0; -4)$.\n'
                        '- Cho $y = 0 \\Rightarrow 2x - 4 = 0 \\Rightarrow x = 2$: Đồ thị cắt trục hoành '
                        '$Ox$ tại điểm $Q(2; 0)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm giá trị của $b$ để đồ thị hàm số bậc nhất $y = 2x + b$ đi qua điểm $M(3; 10)$.',
            'answer': ['4'],
            'unit': None,
            'solution': 'Thay $x = 3, y = 10$ vào $y = 2x + b$: $10 = 2 \\cdot 3 + b \\Rightarrow b = 10 - 6 '
                        '= 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch07-phuong-trinh-ham-so-bac-nhat',
  'context_title': 'Chương VII: Phương trình bậc nhất và hàm số bậc nhất',
  'context': 'Chương VII · SGK Toán 8: Phương trình bậc nhất một ẩn, giải bài toán bằng cách lập phương '
             'trình, hàm số bậc nhất và hệ số góc của đường thẳng.',
  'title': 'Bài 29: Hệ số góc của đường thẳng',
  'icon': '📐',
  'description': 'Hệ số góc của đường thẳng y = ax + b (a khác 0) và điều kiện để hai đường thẳng song song, '
                 'cắt nhau, trùng nhau.',
  'requirements': ['Nhận biết được hệ số góc $a$ của đường thẳng $y = ax + b$ ($a \\neq 0$) và mối liên hệ '
                   'với góc tạo bởi đường thẳng và trục $Ox$.',
                   'Sử dụng được hệ số góc của đường thẳng để nhận biết và tìm điều kiện cho hai đường thẳng '
                   'song song, cắt nhau hoặc trùng nhau.',
                   'Vận dụng kiến thức của **Bài 29: Hệ số góc của đường thẳng** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Trên mặt phẳng tọa độ $Oxy$, hệ số $a$ trong phương trình đường thẳng $y = ax + b$ ($a '
                '\\neq 0$) được gọi là hệ số góc của đường thẳng đó.',
  'theory': '1. Ý nghĩa hình học của hệ số góc $a$:\n'
            '- Khi $a > 0$, góc tạo bởi đường thẳng $y = ax + b$ và trục $Ox$ là góc nhọn.\n'
            '- Khi $a < 0$, góc tạo bởi đường thẳng $y = ax + b$ và trục $Ox$ là góc tù.\n'
            "2. Vị trí tương đối của hai đường thẳng $d: y = ax + b$ ($a \\neq 0$) và $d': y = a'x + b'$ "
            "($a' \\neq 0$):\n"
            "- Hai đường thẳng song song: $d \\parallel d' \\Leftrightarrow a = a'$ và $b \\neq b'$.\n"
            "- Hai đường thẳng trùng nhau: $d \\equiv d' \\Leftrightarrow a = a'$ và $b = b'$.\n"
            "- Hai đường thẳng cắt nhau: $d$ cắt $d' \\Leftrightarrow a \\neq a'$.",
  'formulas': [{'category': 'Hệ số góc và vị trí tương đối của hai đường thẳng',
                'items': [{'name': "Hai đường thẳng song song ($d \\parallel d'$)",
                           'formula': "$a = a'$ và $b \\neq b'$"},
                          {'name': "Hai đường thẳng trùng nhau ($d \\equiv d'$)",
                           'formula': "$a = a'$ và $b = b'$"},
                          {'name': "Hai đường thẳng cắt nhau ($d$ cắt $d'$)", 'formula': "$a \\neq a'$"}]}],
  'example': 'Tìm giá trị của $m$ để đường thẳng $d: y = (m - 2)x + 5$ ($m \\neq 2$) song song với đường '
             "thẳng $d': y = 3x - 1$.",
  'example_answer': "Để hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$.\n"
                    'Do $5 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 5$ (thỏa mãn $m '
                    '\\neq 2$).',
  'real_life': 'So sánh tốc độ tăng trưởng của hai đại lượng tuyến tính qua độ dốc (hệ số góc) của hai đường '
               'thẳng trên biểu đồ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hệ số góc của đường thẳng $y = -4x + 7$ là:',
            'options': ['$-4$', '$7$', '$4$', '$\\dfrac{7}{4}$'],
            'answer': 0,
            'solution': 'Đường thẳng $y = ax + b$ có hệ số góc là $a = -4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đường thẳng nào sau đây song song với đường thẳng $y = 2x - 3$?',
            'options': ['$y = -2x - 3$', '$y = 2x + 5$', '$y = 2x - 3$', '$y = 3x - 2$'],
            'answer': 1,
            'solution': 'Đường thẳng $y = 2x + 5$ có cùng hệ số góc $a = 2$ và $b = 5 \\neq -3$ nên song '
                        'song với $y = 2x - 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Hệ số góc của đường thẳng**, quy tắc hoặc công thức nào sau đây xác định '
                 "đúng **Hai đường thẳng song song ($d \\parallel d'$)**?",
            'options': ["$a = a'$ và $b \\neq b'$ (với dấu ngược lại)",
                        "Đảo ngược vế của quy tắc: $a = a'$ và $b \\neq b'$",
                        "$a = a'$ và $b \\neq b'$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $a = a'$ và $b \\neq b'$"],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 29: Hệ số góc của đường thẳng, **Hai đường thẳng '
                        "song song ($d \\parallel d'$)** được xác định bởi: $a = a'$ và $b \\neq b'$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Hệ số góc của đường thẳng**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 "diễn đúng **Hai đường thẳng trùng nhau ($d \\equiv d'$)**?",
            'options': ["$a = a'$ và $b = b'$ (với dấu ngược lại)",
                        "Đảo ngược vế của quy tắc: $a = a'$ và $b = b'$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $a = a'$ và $b = b'$",
                        "$a = a'$ và $b = b'$"],
            'answer': 3,
            'solution': 'Trong Bài 29: Hệ số góc của đường thẳng, **Hai đường thẳng trùng nhau ($d \\equiv '
                        "d'$)** có công thức/quy tắc là: $a = a'$ và $b = b'$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai đường thẳng $y = (m + 1)x + 2$ ($m \\neq -1$) và $y = 3x + 2$ cắt nhau khi và chỉ khi:',
            'options': ['$m \\neq 2$ và $m \\neq -1$', '$m = 2$', '$m = 3$', '$m \\neq 3$'],
            'answer': 0,
            'solution': "Hai đường thẳng cắt nhau khi $a \\neq a' \\Leftrightarrow m + 1 \\neq 3 "
                        '\\Leftrightarrow m \\neq 2$ (kết hợp điều kiện $m \\neq -1$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 29: Hệ số góc của đường thẳng**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được hệ số góc $a$ của đường thẳng $y = ax - b$ ($a \\neq 0$) và mối liên '
                        'hệ với góc tạo bởi đường thẳng và trục $Ox$.',
                        'Nhận biết được hệ số góc $a$ của đường thẳng $y = ax + b$ ($a \\neq 0$) và mối liên '
                        'hệ với góc tạo bởi đường thẳng và trục $Ox$.',
                        'Nhận biết được hệ số góc $a$ của đường thẳng $y = ax + b$ ($a \\neq 1$) và mối liên '
                        'hệ với góc tạo bởi đường thẳng và trục $Ox$.',
                        'Nhận biết được hệ số góc $a$ của đường thẳng $y = ax + b$ ($a \\neq 2$) và mối liên '
                        'hệ với góc tạo bởi đường thẳng và trục $Ox$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 29: Hệ số góc của đường thẳng: Nhận biết được hệ số '
                        'góc $a$ của đường thẳng $y = ax + b$ ($a \\neq 0$) và mối liên hệ với góc tạo bởi '
                        'đường thẳng và trục $Ox$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai đường thẳng $d_1: y = 3x - 2$ và $d_2: y = -2x + 3$. Xét các khẳng định sau:',
            'statements': ['Đường thẳng $d_1$ có hệ số góc dương ($a_1 = 3 > 0$) nên tạo với trục $Ox$ một '
                           'góc nhọn.',
                           'Đường thẳng $d_2$ có hệ số góc âm ($a_2 = -2 < 0$) nên tạo với trục $Ox$ một góc '
                           'tù.',
                           'Hai đường thẳng $d_1$ và $d_2$ cắt nhau vì $3 \\neq -2$.',
                           'Giao điểm của hai đường thẳng $d_1$ và $d_2$ là điểm $I(2; 4)$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì giải $3x - 2 = -2x + 3 \\Rightarrow 5x = 5 \\Rightarrow '
                        'x = 1, y = 1$, nên giao điểm là $I(1; 1)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 29: Hệ số góc của đường '
                 'thẳng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hệ số góc $a$ của đường '
                           'thẳng $y = ax + b$ ($a \\neq 0$) và mối liên hệ với góc tạo bởi đường thẳng và '
                           'trục $Ox$.',
                           'Trong **Bài 29: Hệ số góc của đường thẳng**, quy tắc/công thức **Hai đường thẳng '
                           "song song ($d \\parallel d'$)** được viết là: $a = a'$ và $b \\neq b'$.",
                           "Nếu áp dụng sai dấu/phép tính thành $a = a'$ và $b \\neq b'$ (với dấu ngược lại) "
                           "thì kết quả của **Hai đường thẳng song song ($d \\parallel d'$)** trong **Bài "
                           '29: Hệ số góc của đường thẳng** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm giá trị của $m$ để đường thẳng $d: y = (m - 2)x + 5$ ($m '
                           "\\neq 2$) song song với đường thẳng $d': y = 3x - 1$.”, kết quả giải đúng là: Để "
                           "hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$. Do "
                           '$5 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 29: Hệ số góc của đường thẳng. b) **Đúng** '
                        "theo công thức **Hai đường thẳng song song ($d \\parallel d'$)** ($a = a'$ và $b "
                        "\\neq b'$). c) **Sai** vì công thức đúng của **Hai đường thẳng song song ($d "
                        "\\parallel d'$)** phải là $a = a'$ và $b \\neq b'$ chứ không phải $a = a'$ và $b "
                        "\\neq b'$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài "
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 29: Hệ số góc của đường thẳng** để giải bài toán '
                 'sau: Tìm giá trị của $m$ để đường thẳng $d: y = (m - 2)x + 5$ ($m \\neq 2$) song song với '
                 "đường thẳng $d': y = 3x - 1$. Cách giải và kết quả nào dưới đây là **đúng**?",
            'options': ["Để hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$. Do "
                        '$5 \\neq -1$ luôn đúng nên ta có: $m + 2 = 3 \\Leftrightarrow m = 5$ (...',
                        "Để hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$. Do "
                        '$5 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 4$ (...',
                        "Để hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$. Do "
                        '$5 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 5$ (...',
                        "Để hai đường thẳng $d$ và $d'$ song song với nhau thì $a = a'$ và $b \\neq b'$. Do "
                        '$10 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 5$ (...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Hệ số góc của đường thẳng: Để hai đường thẳng $d$ và '
                        "$d'$ song song với nhau thì $a = a'$ và $b \\neq b'$.\n"
                        'Do $5 \\neq -1$ luôn đúng nên ta có: $m - 2 = 3 \\Leftrightarrow m = 5$ (thỏa mãn '
                        '$m \\neq 2$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm hệ số góc $a$ của đường thẳng $y = ax + 1$ biết đường thẳng đó đi qua điểm $A(2; 7)$.',
            'answer': ['3'],
            'unit': None,
            'solution': 'Thay $x = 2, y = 7$ vào $y = ax + 1$: $7 = 2a + 1 \\Rightarrow 2a = 6 \\Rightarrow '
                        'a = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch08-xac-suat',
  'context_title': 'Chương VIII: Mở đầu về tính xác suất của biến cố',
  'context': 'Chương VIII · SGK Toán 8: Kết quả có thể, kết quả thuận lợi, cách tính xác suất của biến cố '
             'bằng tỉ số và xác suất thực nghiệm.',
  'title': 'Bài 30: Kết quả có thể và kết quả thuận lợi',
  'icon': '🎲',
  'description': 'Nhận biết kết quả có thể của một hành động, thực nghiệm ngẫu nhiên và liệt kê các kết quả '
                 'thuận lợi cho một biến cố.',
  'requirements': ['Nhận biết và liệt kê được tập hợp tất cả các kết quả có thể của một phép thử ngẫu nhiên '
                   'đơn giản.',
                   'Xác định và đếm được số kết quả thuận lợi cho một biến cố.',
                   'Vận dụng kiến thức của **Bài 30: Kết quả có thể và kết quả thuận lợi** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Một kết quả có thể của hành động, thực nghiệm làm cho biến cố $E$ xảy ra được gọi là một '
                'kết quả thuận lợi cho biến cố $E$.',
  'theory': '1. Kết quả có thể: Khi thực hiện một hành động hay thực nghiệm ngẫu nhiên (gieo xúc xắc, rút '
            'thẻ, chọn bóng), ta xác định được tập hợp tất cả các kết quả có thể xảy ra.\n'
            '2. Kết quả thuận lợi cho biến cố $E$: Để tìm các kết quả thuận lợi cho biến cố $E$, ta kiểm tra '
            'trong tập hợp tất cả các kết quả có thể xem những kết quả nào thỏa mãn điều kiện phát biểu '
            'trong biến cố $E$.',
  'formulas': [{'category': 'Đếm số kết quả có thể và kết quả thuận lợi',
                'items': [{'name': 'Số phần tử không gian mẫu',
                           'formula': '$n$: tổng số kết quả có thể của phép thử'},
                          {'name': 'Số kết quả thuận lợi cho biến cố $E$',
                           'formula': '$k$: số kết quả trong $n$ kết quả có thể làm cho $E$ xảy ra ($0 \\le '
                                      'k \\le n$)'}]}],
  'example': 'Từ một hộp đựng $9$ tấm thẻ ghi các số $1; 2; 3; 4; 5; 6; 7; 8; 9$, rút ngẫu nhiên một tấm '
             "thẻ. Hãy liệt kê các kết quả thuận lợi cho biến cố $E$: 'Rút được tấm thẻ ghi số chính "
             "phương'.",
  'example_answer': 'Các kết quả có thể là $9$ tấm thẻ ghi số từ $1$ đến $9$.\n'
                    'Các số chính phương trong phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$.\n'
                    'Vậy có $3$ kết quả thuận lợi cho biến cố $E$ là rút được thẻ ghi số $1$, số $4$ hoặc số '
                    '$9$.',
  'real_life': 'Đếm số vé số trúng giải trong tổng số vé phát hành hoặc số phương án chọn đề thi thuận lợi '
               'cho học sinh.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Gieo một con xúc xắc $6$ mặt cân đối. Các kết quả thuận lợi cho biến cố 'Số chấm xuất hiện "
                 "là số lẻ' là:",
            'options': ['$2$ chấm; $4$ chấm; $6$ chấm',
                        '$1$ chấm; $3$ chấm; $5$ chấm',
                        '$1$ chấm; $2$ chấm; $3$ chấm',
                        '$3$ chấm; $5$ chấm'],
            'answer': 1,
            'solution': 'Các mặt có số chấm lẻ từ $1$ đến $6$ là mặt $1$ chấm, $3$ chấm và $5$ chấm.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Chọn ngẫu nhiên một chữ cái trong từ 'TOAN'. Số kết quả có thể của hành động này là:",
            'options': ['$3$', '$2$', '$4$', '$5$'],
            'answer': 2,
            'solution': "Từ 'TOAN' gồm $4$ chữ cái khác nhau là T, O, A, N nên có $4$ kết quả có thể.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Kết quả có thể và kết quả thuận lợi**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Số phần tử không gian mẫu**?',
            'options': ['$n$: tổng số kết quả có thể của phép thử (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $n$: tổng số kết quả có thể của phép thử',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $n$: tổng số kết quả có thể của '
                        'phép thử',
                        '$n$: tổng số kết quả có thể của phép thử'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 30: Kết quả có thể và kết quả thuận lợi, **Số phần '
                        'tử không gian mẫu** được xác định bởi: $n$: tổng số kết quả có thể của phép thử.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Kết quả có thể và kết quả thuận lợi**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Số kết quả thuận lợi cho biến cố $E$**?',
            'options': ['$k$: số kết quả trong $n$ kết quả có thể làm cho $E$ xảy ra ($0 \\le k \\le n$)',
                        '$k$: số kết quả trong $n$ kết quả có thể làm cho $E$ xảy ra ($0 \\ge k \\le n$)',
                        '$k$: số kết quả trong $n$ kết quả có thể làm cho $E$ xảy ra ($1 \\le k \\le n$)',
                        '$k$: số kết quả trong $n$ kết quả có thể làm cho $E$ xảy ra ($2 \\le k \\le n$)'],
            'answer': 0,
            'solution': 'Trong Bài 30: Kết quả có thể và kết quả thuận lợi, **Số kết quả thuận lợi cho biến '
                        'cố $E$** có công thức/quy tắc là: $k$: số kết quả trong $n$ kết quả có thể làm cho '
                        '$E$ xảy ra ($0 \\le k \\le n$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Rút ngẫu nhiên một thẻ từ hộp gồm $12$ thẻ đánh số từ $1$ đến $12$. Có bao nhiêu kết quả '
                 "thuận lợi cho biến cố 'Số trên thẻ rút được chia hết cho $4$'?",
            'options': ['$4$', '$3$', '$2$', '$6$'],
            'answer': 1,
            'solution': 'Các số từ $1$ đến $12$ chia hết cho $4$ là $4; 8; 12$, nên có $3$ kết quả thuận '
                        'lợi.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 30: Kết quả có thể và kết quả thuận lợi**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết và liệt kê được tập hợp tất cả các kết quả có thể của một phép thử ngẫu '
                        'nhiên đơn giản. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và liệt kê được tập hợp tất cả các kết quả có '
                        'thể của một phép thử ngẫu nhiên đơn giản.',
                        'Nhận biết và liệt kê được tập hợp tất cả các kết quả có thể của một phép thử ngẫu '
                        'nhiên đơn giản.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và liệt kê được tập '
                        'hợp tất cả các kết quả có thể của một phép thử ngẫu nhiên đơn giản.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 30: Kết quả có thể và kết quả thuận lợi: Nhận biết và '
                        'liệt kê được tập hợp tất cả các kết quả có thể của một phép thử ngẫu nhiên đơn '
                        'giản.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một hộp có $10$ quả bóng được đánh số từ $1$ đến $10$. Lấy ngẫu nhiên một quả bóng. Xét '
                 'các khẳng định sau:',
            'statements': ['Tổng số kết quả có thể của phép thử là $10$.',
                           "Biến cố $A$: 'Quả bóng lấy ra ghi số nguyên tố' có $4$ kết quả thuận lợi (là các "
                           'số $2; 3; 5; 7$).',
                           "Biến cố $B$: 'Quả bóng lấy ra ghi số lớn hơn $7$' có $3$ kết quả thuận lợi (là "
                           'các số $8; 9; 10$).',
                           "Biến cố $C$: 'Quả bóng lấy ra ghi số có hai chữ số' có $2$ kết quả thuận lợi."],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì từ $1$ đến $10$ chỉ có duy nhất số $10$ là số có hai chữ '
                        'số ($1$ kết quả thuận lợi).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 30: Kết quả có thể và kết '
                 'quả thuận lợi**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết và liệt kê được tập hợp tất cả '
                           'các kết quả có thể của một phép thử ngẫu nhiên đơn giản.',
                           'Trong **Bài 30: Kết quả có thể và kết quả thuận lợi**, quy tắc/công thức **Số '
                           'phần tử không gian mẫu** được viết là: $n$: tổng số kết quả có thể của phép thử.',
                           'Nếu áp dụng sai dấu/phép tính thành $n$: tổng số kết quả có thể của phép thử '
                           '(với dấu ngược lại) thì kết quả của **Số phần tử không gian mẫu** trong **Bài '
                           '30: Kết quả có thể và kết quả thuận lợi** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Từ một hộp đựng $9$ tấm thẻ ghi các số $1; 2; 3; 4; 5; 6; 7; '
                           '8; 9$, rút ngẫu nhiên một tấm thẻ. Hãy liệt kê các kết quả thuận lợi cho b...”, '
                           'kết quả giải đúng là: Các kết quả có thể là $9$ tấm thẻ ghi số từ $1$ đến $9$. '
                           'Các số chính phương trong phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = '
                           '3^2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 30: Kết quả có thể và kết quả thuận lợi. '
                        'b) **Đúng** theo công thức **Số phần tử không gian mẫu** ($n$: tổng số kết quả có '
                        'thể của phép thử). c) **Sai** vì công thức đúng của **Số phần tử không gian mẫu** '
                        'phải là $n$: tổng số kết quả có thể của phép thử chứ không phải $n$: tổng số kết '
                        'quả có thể của phép thử (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh '
                        'họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 30: Kết quả có thể và kết quả thuận lợi** để giải '
                 'bài toán sau: Từ một hộp đựng $9$ tấm thẻ ghi các số $1; 2; 3; 4; 5; 6; 7; 8; 9$, rút ngẫu '
                 "nhiên một tấm thẻ. Hãy liệt kê các kết quả thuận lợi cho biến cố $E$: 'Rút được tấm thẻ "
                 "ghi số chính phương'. Cách giải và kết quả nào dưới đây là **đúng**?",
            'options': ['Các kết quả có thể là $10$ tấm thẻ ghi số từ $1$ đến $9$. Các số chính phương trong '
                        'phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$. Vậy có $3$ k...',
                        'Các kết quả có thể là $9$ tấm thẻ ghi số từ $1$ đến $9$. Các số chính phương trong '
                        'phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$. Vậy có $2$ k...',
                        'Các kết quả có thể là $18$ tấm thẻ ghi số từ $1$ đến $9$. Các số chính phương trong '
                        'phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$. Vậy có $3$ k...',
                        'Các kết quả có thể là $9$ tấm thẻ ghi số từ $1$ đến $9$. Các số chính phương trong '
                        'phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$. Vậy có $3$ k...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Kết quả có thể và kết quả thuận lợi: Các kết quả có '
                        'thể là $9$ tấm thẻ ghi số từ $1$ đến $9$.\n'
                        'Các số chính phương trong phạm vi từ $1$ đến $9$ là $1 = 1^2; 4 = 2^2; 9 = 3^2$.\n'
                        'Vậy có $3$ kết quả thuận lợi cho biến cố $E$ là rút được thẻ ghi số $1$, số $4$ '
                        'hoặc số $9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp chứa $20$ tấm thẻ cùng loại được đánh số từ $1$ đến $20$. Rút ngẫu nhiên một tấm '
                 "thẻ. Hỏi có bao nhiêu kết quả thuận lợi cho biến cố 'Số ghi trên thẻ là số chia hết cho cả "
                 "$2$ và $3$'?",
            'answer': ['3'],
            'unit': None,
            'solution': 'Số chia hết cho cả $2$ và $3$ là bội của $6$. Từ $1$ đến $20$ có các số $6; 12; '
                        '18$, vậy có $3$ kết quả thuận lợi.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch08-xac-suat',
  'context_title': 'Chương VIII: Mở đầu về tính xác suất của biến cố',
  'context': 'Chương VIII · SGK Toán 8: Kết quả có thể, kết quả thuận lợi, cách tính xác suất của biến cố '
             'bằng tỉ số và xác suất thực nghiệm.',
  'title': 'Bài 31: Cách tính xác suất của biến cố bằng tỉ số',
  'icon': '🎯',
  'description': 'Công thức tính xác suất của biến cố bằng tỉ số giữa số kết quả thuận lợi và tổng số kết '
                 'quả có thể đồng khả năng.',
  'requirements': ['Mô tả và vận dụng được công thức tính xác suất của biến cố bằng tỉ số khi các kết quả có '
                   'thể là đồng khả năng.',
                   'Giải quyết được các bài toán tính xác suất thực tế (rút thẻ, chọn bóng, gieo xúc xắc).',
                   'Vận dụng kiến thức của **Bài 31: Cách tính xác suất của biến cố bằng tỉ số** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giả sử rằng các kết quả có thể của một hành động hay thực nghiệm là đồng khả năng. Khi đó, '
                'xác suất của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số giữa số kết quả thuận lợi cho biến '
                'cố $E$ và tổng số kết quả có thể.',
  'theory': 'Các bước tính xác suất của biến cố $E$ khi các kết quả có thể là đồng khả năng:\n'
            '1. Đếm tổng số kết quả có thể (gọi là $n$).\n'
            '2. Chỉ ra các kết quả thuận lợi cho biến cố $E$ và đếm số kết quả thuận lợi đó (gọi là $k$).\n'
            '3. Tính xác suất theo công thức tỉ số: $P(E) = \\dfrac{k}{n}$.',
  'formulas': [{'category': 'Công thức xác suất cổ điển (đồng khả năng)',
                'items': [{'name': 'Xác suất của biến cố $E$',
                           'formula': '$P(E) = \\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số '
                                      'kết quả có thể}} = \\dfrac{k}{n}$'},
                          {'name': 'Tính chất xác suất', 'formula': '$0 \\le P(E) \\le 1$'}]}],
  'example': 'Một túi đựng $5$ viên bi đỏ, $3$ viên bi xanh và $2$ viên bi vàng có cùng kích thước và khối '
             "lượng. Lấy ngẫu nhiên một viên bi từ túi. Tính xác suất của biến cố $A$: 'Lấy được viên bi màu "
             "đỏ'.",
  'example_answer': 'Tổng số kết quả có thể đồng khả năng là $n = 5 + 3 + 2 = 10$.\n'
                    'Số kết quả thuận lợi cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$.\n'
                    'Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{5}{10} = \\dfrac{1}{2} = 0,5$.',
  'real_life': 'Tính xác suất trúng thưởng trong chương trình bốc thăm trúng thưởng hoặc xác suất chọn ngẫu '
               'nhiên một sản phẩm đạt chuẩn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Gieo một con xúc xắc $6$ mặt cân đối và đồng chất. Xác suất của biến cố 'Số chấm xuất hiện "
                 "lớn hơn $4$' là:",
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{2}{3}$', '$\\dfrac{1}{3}$', '$\\dfrac{1}{6}$'],
            'answer': 2,
            'solution': 'Có $6$ kết quả đồng khả năng, trong đó có $2$ kết quả thuận lợi là mặt $5$ chấm và '
                        '$6$ chấm. Xác suất là $\\dfrac{2}{6} = \\dfrac{1}{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một hộp có $4$ quả bóng xanh và $6$ quả bóng trắng cùng kích thước. Lấy ngẫu nhiên '
                 '$1$ quả bóng. Xác suất lấy được quả bóng xanh là:',
            'options': ['$\\dfrac{3}{5}$', '$\\dfrac{2}{3}$', '$\\dfrac{1}{4}$', '$\\dfrac{2}{5}$'],
            'answer': 3,
            'solution': 'Tổng số quả bóng là $4 + 6 = 10$. Xác suất lấy được bóng xanh là $\\dfrac{4}{10} = '
                        '\\dfrac{2}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Cách tính xác suất của biến cố bằng tỉ số**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Xác suất của biến cố $E$**?',
            'options': ['$P(E) = \\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có '
                        'thể}} = \\dfrac{k}{n}$',
                        '$P(E) = \\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có '
                        'thể}} = \\dfrac{k}{n}$ (với dấu ngược lại)',
                        '$P(E) = \\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có '
                        'thể}} = \\dfrac{n}{k}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(E) = \\dfrac{\\text{Số kết '
                        'quả thuận lợi cho } E}{\\text{Tổng số kết quả có thể}} = \\dfrac{k}{n}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 31: Cách tính xác suất của biến cố bằng tỉ số, '
                        '**Xác suất của biến cố $E$** được xác định bởi: $P(E) = \\dfrac{\\text{Số kết quả '
                        'thuận lợi cho } E}{\\text{Tổng số kết quả có thể}} = \\dfrac{k}{n}$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Cách tính xác suất của biến cố bằng tỉ số**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Tính chất xác suất**?',
            'options': ['$0 \\ge P(E) \\le 1$',
                        '$0 \\le P(E) \\le 1$',
                        '$0 \\le P(E) \\le 2$',
                        '$2 \\le P(E) \\le 1$'],
            'answer': 1,
            'solution': 'Trong Bài 31: Cách tính xác suất của biến cố bằng tỉ số, **Tính chất xác suất** có '
                        'công thức/quy tắc là: $0 \\le P(E) \\le 1$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Rút ngẫu nhiên một thẻ từ hộp gồm $15$ thẻ được đánh số từ $1$ đến $15$. Xác suất của biến '
                 "cố 'Số trên thẻ rút được là bội của $5$' là:",
            'options': ['$\\dfrac{1}{3}$', '$\\dfrac{1}{15}$', '$\\dfrac{1}{5}$', '$\\dfrac{3}{5}$'],
            'answer': 2,
            'solution': 'Các bội của $5$ từ $1$ đến $15$ là $5; 10; 15$ ($3$ kết quả thuận lợi). Xác suất là '
                        '$\\dfrac{3}{15} = \\dfrac{1}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 31: Cách tính xác suất của biến cố bằng tỉ số**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Mô tả và vận dụng được công thức tính xác suất của biến cố bằng tỉ số khi các kết '
                        'quả có thể là đồng khả năng. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả và vận dụng được công thức tính xác suất của biến '
                        'cố bằng tỉ số khi các kết quả có thể là đồng khả năng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả và vận dụng được công '
                        'thức tính xác suất của biến cố bằng tỉ số khi các kết quả có thể là đồng khả năng.',
                        'Mô tả và vận dụng được công thức tính xác suất của biến cố bằng tỉ số khi các kết '
                        'quả có thể là đồng khả năng.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 31: Cách tính xác suất của biến cố bằng tỉ số: Mô tả '
                        'và vận dụng được công thức tính xác suất của biến cố bằng tỉ số khi các kết quả có '
                        'thể là đồng khả năng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Lớp 8A có $40$ học sinh, trong đó có $18$ học sinh nam và $22$ học sinh nữ. Giáo viên gọi '
                 'ngẫu nhiên $1$ học sinh lên bảng. Xét các khẳng định sau:',
            'statements': ['Tổng số kết quả có thể đồng khả năng là $40$.',
                           'Xác suất gọi được một học sinh nam là $\\dfrac{18}{40} = 0,45$.',
                           'Xác suất gọi được một học sinh nữ là $\\dfrac{22}{40} = 0,55$.',
                           'Tổng xác suất gọi được học sinh nam và xác suất gọi được học sinh nữ lớn hơn '
                           '$1$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $0,45 + 0,55 = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 31: Cách tính xác suất của '
                 'biến cố bằng tỉ số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả và vận dụng được công thức tính '
                           'xác suất của biến cố bằng tỉ số khi các kết quả có thể là đồng khả năng.',
                           'Trong **Bài 31: Cách tính xác suất của biến cố bằng tỉ số**, quy tắc/công thức '
                           '**Xác suất của biến cố $E$** được viết là: $P(E) = \\dfrac{\\text{Số kết quả '
                           'thuận lợi cho } E}{\\text{Tổng số kết quả có thể}} = \\dfrac{k}{n}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $P(E) = \\dfrac{\\text{Số kết quả thuận lợi '
                           'cho } E}{\\text{Tổng số kết quả có thể}} = \\dfrac{k}{n}$ (với dấu ngược lại) '
                           'thì kết quả của **Xác suất của biến cố $E$** trong **Bài 31: Cách tính xác suất '
                           'của biến cố bằng tỉ số** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một túi đựng $5$ viên bi đỏ, $3$ viên bi xanh và $2$ viên bi '
                           'vàng có cùng kích thước và khối lượng. Lấy ngẫu nhiên một viên bi từ túi....”, '
                           'kết quả giải đúng là: Tổng số kết quả có thể đồng khả năng là $n = 5 + 3 + 2 = '
                           '10$. Số kết quả thuận lợi cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$. '
                           'Vậ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 31: Cách tính xác suất của biến cố bằng tỉ '
                        'số. b) **Đúng** theo công thức **Xác suất của biến cố $E$** ($P(E) = '
                        '\\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có thể}} = '
                        '\\dfrac{k}{n}$). c) **Sai** vì công thức đúng của **Xác suất của biến cố $E$** phải '
                        'là $P(E) = \\dfrac{\\text{Số kết quả thuận lợi cho } E}{\\text{Tổng số kết quả có '
                        'thể}} = \\dfrac{k}{n}$ chứ không phải $P(E) = \\dfrac{\\text{Số kết quả thuận lợi '
                        'cho } E}{\\text{Tổng số kết quả có thể}} = \\dfrac{k}{n}$ (với dấu ngược lại). d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 31: Cách tính xác suất của biến cố bằng tỉ số** để '
                 'giải bài toán sau: Một túi đựng $5$ viên bi đỏ, $3$ viên bi xanh và $2$ viên bi vàng có '
                 'cùng kích thước và khối lượng. Lấy ngẫu nhiên một viên bi từ túi. Tính xác suất của biến '
                 "cố $A$: 'Lấy được viên bi màu đỏ'. Cách giải và kết quả nào dưới đây là **đúng**?",
            'options': ['Tổng số kết quả có thể đồng khả năng là $n = 5 + 3 + 2 = 10$. Số kết quả thuận lợi '
                        'cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$. Vậy xác suất của...',
                        'Tổng số kết quả có thể đồng khả năng là $n = 5 - 3 + 2 = 10$. Số kết quả thuận lợi '
                        'cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$. Vậy xác suất của...',
                        'Tổng số kết quả có thể đồng khả năng là $n = 5 + 3 + 2 = 10$. Số kết quả thuận lợi '
                        'cho biến cố $A$ (lấy được viên bi đỏ) là $k = 4$. Vậy xác suất của...',
                        'Tổng số kết quả có thể đồng khả năng là $n = 10 + 3 + 2 = 10$. Số kết quả thuận lợi '
                        'cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$. Vậy xác suất của...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Cách tính xác suất của biến cố bằng tỉ số: Tổng số '
                        'kết quả có thể đồng khả năng là $n = 5 + 3 + 2 = 10$.\n'
                        'Số kết quả thuận lợi cho biến cố $A$ (lấy được viên bi đỏ) là $k = 5$.\n'
                        'Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{5}{10} = \\dfrac{1}{2} = 0,5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hộp có $25$ chiếc thẻ cùng loại ghi các số từ $1$ đến $25$. Rút ngẫu nhiên một chiếc '
                 "thẻ. Tính xác suất (viết dưới dạng số thập phân) của biến cố 'Số ghi trên thẻ là số chính "
                 "phương'.",
            'answer': ['0,2', '0.2'],
            'unit': None,
            'solution': 'Các số chính phương từ $1$ đến $25$ là $1; 4; 9; 16; 25$ (có $5$ số). Xác suất là '
                        '$\\dfrac{5}{25} = 0,2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch08-xac-suat',
  'context_title': 'Chương VIII: Mở đầu về tính xác suất của biến cố',
  'context': 'Chương VIII · SGK Toán 8: Kết quả có thể, kết quả thuận lợi, cách tính xác suất của biến cố '
             'bằng tỉ số và xác suất thực nghiệm.',
  'title': 'Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng',
  'icon': '🔬',
  'description': 'Khái niệm xác suất thực nghiệm của một biến cố qua nhiều lần thử và ứng dụng ước lượng xác '
                 'suất lí thuyết.',
  'requirements': ['Tính được xác suất thực nghiệm của một biến cố trong một số phép thử lặp lại.',
                   'Nhận biết được khi số lần thực nghiệm rất lớn thì xác suất thực nghiệm xấp xỉ với xác '
                   'suất lí thuyết và vận dụng vào bài toán ước lượng.',
                   'Vận dụng kiến thức của **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và '
                   'ứng dụng** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giả sử trong $n$ lần thực nghiệm hoặc quan sát, biến cố $E$ xảy ra $k$ lần. Khi đó tỉ số '
                '$\\dfrac{k}{n}$ được gọi là xác suất thực nghiệm của biến cố $E$, tức là bằng số lần biến '
                'cố $E$ xảy ra chia cho tổng số lần thực nghiệm.',
  'theory': '1. Công thức xác suất thực nghiệm: Trong $n$ lần thực hiện phép thử, nếu biến cố $E$ xuất hiện '
            '$k$ lần thì xác suất thực nghiệm của $E$ là $\\dfrac{k}{n}$.\n'
            '2. Mối liên hệ giữa xác suất thực nghiệm và xác suất: Khi số lần thực nghiệm hay quan sát $n$ '
            'ngày càng lớn thì xác suất thực nghiệm của biến cố $E$ ngày càng gần với xác suất thực sự '
            '$P(E)$ của biến cố đó: $P(E) \\approx \\dfrac{k}{n}$.',
  'formulas': [{'category': 'Xác suất thực nghiệm và ước lượng',
                'items': [{'name': 'Xác suất thực nghiệm của biến cố $E$',
                           'formula': '$P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ '
                                      'lần thử)'},
                          {'name': 'Ước lượng xác suất khi $n$ lớn',
                           'formula': '$P(E) \\approx \\dfrac{k}{n}$'}]}],
  'example': 'Một nhà máy kiểm tra ngẫu nhiên $500$ bóng đèn vừa sản xuất thì thấy có $5$ bóng đèn bị lỗi. '
             "Tính xác suất thực nghiệm của biến cố 'Bóng đèn được chọn không bị lỗi' và ước lượng số bóng "
             'đèn đạt chuẩn trong lô hàng $10000$ bóng.',
  'example_answer': '- Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 - 5 = 495$ (bóng).\n'
                    '- Xác suất thực nghiệm bóng đèn không bị lỗi là $\\dfrac{495}{500} = 0,99$.\n'
                    '- Trong lô $10000$ bóng, ước lượng số bóng đèn đạt chuẩn là $10000 \\cdot 0,99 = 9900$ '
                    '(bóng).',
  'real_life': 'Kiểm định chất lượng sản phẩm công nghiệp, ước lượng tỉ lệ hạt giống nảy mầm hoặc ước lượng '
               'số lượng cá trong hồ nuôi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tung một đồng xu $50$ lần liên tiếp thì thấy có $28$ lần xuất hiện mặt ngửa. Xác suất thực '
                 "nghiệm của biến cố 'Xuất hiện mặt ngửa' là:",
            'options': ['$\\dfrac{22}{50} = 0,44$',
                        '$\\dfrac{1}{2} = 0,5$',
                        '$\\dfrac{28}{22}$',
                        '$\\dfrac{28}{50} = 0,56$'],
            'answer': 3,
            'solution': 'Xác suất thực nghiệm bằng số lần xuất hiện mặt ngửa chia cho tổng số lần tung: '
                        '$\\dfrac{28}{50} = 0,56$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi số lần thực nghiệm $n$ ngày càng lớn thì xác suất thực nghiệm của một biến cố sẽ:',
            'options': ['Ngày càng gần với xác suất lí thuyết của biến cố đó',
                        'Luôn tăng lên đến $1$',
                        'Luôn giảm về $0$',
                        'Không có liên hệ gì với xác suất của biến cố'],
            'answer': 0,
            'solution': 'Theo quy luật số lớn trong thống kê, khi $n$ ngày càng lớn thì xác suất thực nghiệm '
                        'xấp xỉ xác suất lí thuyết.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Xác suất thực nghiệm của biến cố $E$**?',
            'options': ['$P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử) (với '
                        'dấu ngược lại)',
                        '$P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử)',
                        '$P_{\\text{tn}}(E) = \\dfrac{n}{k}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P_{\\text{tn}}(E) = '
                        '\\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác '
                        'suất và ứng dụng, **Xác suất thực nghiệm của biến cố $E$** được xác định bởi: '
                        '$P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Ước lượng xác suất khi $n$ lớn**?',
            'options': ['$P(E) \\approx \\dfrac{k}{n}$ (với dấu ngược lại)',
                        '$P(E) \\approx \\dfrac{n}{k}$',
                        '$P(E) \\approx \\dfrac{k}{n}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(E) \\approx \\dfrac{k}{n}$'],
            'answer': 2,
            'solution': 'Trong Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng dụng, **Ước '
                        'lượng xác suất khi $n$ lớn** có công thức/quy tắc là: $P(E) \\approx '
                        '\\dfrac{k}{n}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một xạ thủ bắn $100$ viên đạn vào bia thì có $85$ viên trúng tâm. Xác suất thực nghiệm của '
                 "biến cố 'Xạ thủ bắn trượt tâm' là:",
            'options': ['$0,85$', '$0,5$', '$0,25$', '$0,15$'],
            'answer': 3,
            'solution': 'Số viên bắn trượt tâm là $100 - 85 = 15$ (viên). Xác suất thực nghiệm bắn trượt tâm '
                        'là $\\dfrac{15}{100} = 0,15$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và '
                 'ứng dụng**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được xác suất thực nghiệm của một biến cố trong một số phép thử lặp lại.',
                        'Tính được xác suất thực nghiệm của một biến cố trong một số phép thử lặp lại. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được xác suất thực nghiệm của một biến cố trong một '
                        'số phép thử lặp lại.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được xác suất thực nghiệm '
                        'của một biến cố trong một số phép thử lặp lại.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác '
                        'suất và ứng dụng: Tính được xác suất thực nghiệm của một biến cố trong một số phép '
                        'thử lặp lại.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Gieo thử nghiệm $200$ hạt giống cải thì thấy có $184$ hạt nảy mầm. Xét các khẳng định sau:',
            'statements': ["Xác suất thực nghiệm của biến cố 'Hạt giống nảy mầm' là $\\dfrac{184}{200} = "
                           '0,92$ (hay $92\\%$).',
                           "Xác suất thực nghiệm của biến cố 'Hạt giống không nảy mầm' là $0,08$ (hay "
                           '$8\\%$).',
                           'Ta có thể ước lượng xác suất một hạt giống loại này nảy mầm là khoảng $0,92$.',
                           'Nếu gieo $1000$ hạt giống cùng loại thì chắc chắn chỉ có không quá $500$ hạt nảy '
                           'mầm.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì ước lượng có khoảng $1000 \\cdot 0,92 = 920$ hạt nảy '
                        'mầm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 32: Mối liên hệ giữa xác '
                 'suất thực nghiệm với xác suất và ứng dụng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được xác suất thực nghiệm của một '
                           'biến cố trong một số phép thử lặp lại.',
                           'Trong **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất và ứng '
                           'dụng**, quy tắc/công thức **Xác suất thực nghiệm của biến cố $E$** được viết là: '
                           '$P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ lần thử).',
                           'Nếu áp dụng sai dấu/phép tính thành $P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số '
                           'lần $E$ xảy ra trong $n$ lần thử) (với dấu ngược lại) thì kết quả của **Xác suất '
                           'thực nghiệm của biến cố $E$** trong **Bài 32: Mối liên hệ giữa xác suất thực '
                           'nghiệm với xác suất và ứng dụng** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một nhà máy kiểm tra ngẫu nhiên $500$ bóng đèn vừa sản xuất '
                           "thì thấy có $5$ bóng đèn bị lỗi. Tính xác suất thực nghiệm của biến cố 'Bón...”, "
                           'kết quả giải đúng là: - Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 - 5 '
                           '= 495$ (bóng). - Xác suất thực nghiệm bóng đèn không bị lỗi là '
                           '$\\dfrac{495}{500} = 0,99$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 32: Mối liên hệ giữa xác suất thực nghiệm '
                        'với xác suất và ứng dụng. b) **Đúng** theo công thức **Xác suất thực nghiệm của '
                        'biến cố $E$** ($P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong '
                        '$n$ lần thử)). c) **Sai** vì công thức đúng của **Xác suất thực nghiệm của biến cố '
                        '$E$** phải là $P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra trong $n$ '
                        'lần thử) chứ không phải $P_{\\text{tn}}(E) = \\dfrac{k}{n}$ ($k$: số lần $E$ xảy ra '
                        'trong $n$ lần thử) (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác '
                 'suất và ứng dụng** để giải bài toán sau: Một nhà máy kiểm tra ngẫu nhiên $500$ bóng đèn '
                 "vừa sản xuất thì thấy có $5$ bóng đèn bị lỗi. Tính xác suất thực nghiệm của biến cố 'Bóng "
                 "đèn được chọn không bị lỗi' và ước lượng số bóng đèn đạt chuẩn trong lô hàng $10000$ bóng. "
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 + 5 = 495$ (bóng). - Xác suất '
                        'thực nghiệm bóng đèn không bị lỗi là $\\dfrac{495}{500} = 0,99$....',
                        '- Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 - 5 = 495$ (bóng). - Xác suất '
                        'thực nghiệm bóng đèn không bị lỗi là $\\dfrac{495}{500} = 0,99$....',
                        '- Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 - 5 = 495$ (bóng). - Xác suất '
                        'thực nghiệm bóng đèn không bị lỗi là $\\dfrac{500}{495} = 0,99$....',
                        '- Số bóng đèn không bị lỗi trong mẫu kiểm tra là $502 - 5 = 495$ (bóng). - Xác suất '
                        'thực nghiệm bóng đèn không bị lỗi là $\\dfrac{495}{500} = 0,99$....'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Mối liên hệ giữa xác suất thực nghiệm với xác suất '
                        'và ứng dụng: - Số bóng đèn không bị lỗi trong mẫu kiểm tra là $500 - 5 = 495$ '
                        '(bóng).\n'
                        '- Xác suất thực nghiệm bóng đèn không bị lỗi là $\\dfrac{495}{500} = 0,99$.\n'
                        '- Trong lô $10000$ bóng, ước lượng số bóng đèn đạt chuẩn là $10000 \\cdot 0,99 = '
                        '9900$ (bóng).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Theo dõi $400$ khách hàng vào siêu thị thì thấy có $120$ người mua trái cây. Nếu trong '
                 'ngày có $2000$ khách hàng vào siêu thị thì ước lượng có khoảng bao nhiêu người mua trái '
                 'cây?',
            'answer': ['600'],
            'unit': None,
            'solution': 'Xác suất thực nghiệm khách mua trái cây là $\\dfrac{120}{400} = 0,3$. Với $2000$ '
                        'khách thì ước lượng có $2000 \\cdot 0,3 = 600$ (người).',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch09-tam-giac-dong-dang',
  'context_title': 'Chương IX: Tam giác đồng dạng',
  'context': 'Chương IX · SGK Toán 8: Hai tam giác đồng dạng, ba trường hợp đồng dạng của tam giác, định lí '
             'Pythagore và hình đồng dạng.',
  'title': 'Bài 33: Hai tam giác đồng dạng',
  'icon': '🔺',
  'description': 'Định nghĩa hai tam giác đồng dạng, tỉ số đồng dạng và các tính chất cơ bản của hai tam '
                 'giác đồng dạng.',
  'requirements': ['Mô tả được định nghĩa của hai tam giác đồng dạng và tỉ số đồng dạng.',
                   'Giải thích được tính chất của hai tam giác đồng dạng và định lí về tam giác tạo bởi '
                   'đường thẳng cắt hai cạnh và song song với cạnh còn lại.',
                   'Vận dụng kiến thức của **Bài 33: Hai tam giác đồng dạng** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': "Tam giác $\\triangle A'B'C'$ gọi là đồng dạng với tam giác $\\triangle ABC$, kí hiệu "
                "$\\triangle A'B'C' \\sim \\triangle ABC$, nếu $\\widehat{A'} = \\widehat{A}, \\widehat{B'} "
                "= \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = "
                "\\dfrac{C'A'}{CA} = k$ ($k$ gọi là tỉ số đồng dạng).",
  'theory': '1. Tính chất của quan hệ đồng dạng:\n'
            '- Mỗi tam giác đồng dạng với chính nó theo tỉ số $k = 1$.\n'
            "- Nếu $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số $k$ thì $\\triangle ABC \\sim "
            "\\triangle A'B'C'$ theo tỉ số $\\dfrac{1}{k}$. Tỉ số chu vi của hai tam giác đồng dạng cũng "
            'bằng tỉ số đồng dạng $k$.\n'
            "- Nếu $\\triangle A'B'C' \\sim \\triangle A''B''C''$ và $\\triangle A''B''C'' \\sim \\triangle "
            "ABC$ thì $\\triangle A'B'C' \\sim \\triangle ABC$.\n"
            '2. Định lí: Nếu một đường thẳng cắt hai cạnh của một tam giác và song song với cạnh còn lại thì '
            'nó tạo thành một tam giác mới đồng dạng với tam giác đã cho.',
  'formulas': [{'category': 'Định nghĩa và tính chất hai tam giác đồng dạng',
                'items': [{'name': "Định nghĩa $\\triangle A'B'C' \\sim \\triangle ABC$",
                           'formula': "$\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, "
                                      "\\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = "
                                      "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$"},
                          {'name': 'Tỉ số chu vi của hai tam giác đồng dạng',
                           'formula': "$\\dfrac{P_{\\triangle A'B'C'}}{P_{\\triangle ABC}} = k$"},
                          {'name': 'Đường thẳng song song $MN \\parallel BC$',
                           'formula': '$\\triangle AMN \\sim \\triangle ABC$'}]}],
  'example': "Cho $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = \\dfrac{2}{3}$. Biết "
             "chu vi của $\\triangle ABC$ là $36\\text{ cm}$, tính chu vi của $\\triangle A'B'C'$.",
  'example_answer': "Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = \\dfrac{2}{3}$ "
                    'nên tỉ số chu vi của hai tam giác cũng bằng $\\dfrac{2}{3}$.\n'
                    "Do đó chu vi của $\\triangle A'B'C'$ là: $36 \\cdot \\dfrac{2}{3} = 24\\text{ (cm)}$.",
  'real_life': 'Bản vẽ thiết kế kiến trúc của mái nhà hình tam giác đồng dạng với mái nhà thực tế theo tỉ lệ '
               'bản vẽ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Nếu $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = \\dfrac{3}{5}$ thì "
                 "$\\triangle ABC \\sim \\triangle A'B'C'$ theo tỉ số đồng dạng nào?",
            'options': ['$\\dfrac{5}{3}$', '$\\dfrac{3}{5}$', '$\\dfrac{9}{25}$', '$1$'],
            'answer': 0,
            'solution': "Nếu $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số $k$ thì $\\triangle ABC "
                        "\\sim \\triangle A'B'C'$ theo tỉ số $\\dfrac{1}{k} = \\dfrac{5}{3}$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC = \\triangle DEF$. Khi đó $\\triangle ABC \\sim \\triangle DEF$ theo '
                 'tỉ số đồng dạng bằng:',
            'options': ['$2$', '$1$', '$\\dfrac{1}{2}$', '$0$'],
            'answer': 1,
            'solution': 'Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 33: Hai tam giác đồng dạng**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 "**Định nghĩa $\\triangle A'B'C' \\sim \\triangle ABC$**?",
            'options': ["$\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = "
                        "\\widehat{C}$ và $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$ "
                        '(với dấu ngược lại)',
                        "$\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = "
                        "\\widehat{C}$ và $\\dfrac{AB}{A'B'} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$",
                        "$\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = "
                        "\\widehat{C}$ và $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $\\widehat{A'} = \\widehat{A}, "
                        "\\widehat{B'} = \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$"],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 33: Hai tam giác đồng dạng, **Định nghĩa '
                        "$\\triangle A'B'C' \\sim \\triangle ABC$** được xác định bởi: $\\widehat{A'} = "
                        "\\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và "
                        "$\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 33: Hai tam giác đồng dạng**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Tỉ số chu vi của hai tam giác đồng dạng**?',
            'options': ["$\\dfrac{P_{\\triangle A'B'C'}}{P_{\\triangle ABC}} = k$ (với dấu ngược lại)",
                        "Đảo ngược vế của quy tắc: $\\dfrac{P_{\\triangle A'B'C'}}{P_{\\triangle ABC}} = k$",
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{P_{\\triangle '
                        "A'B'C'}}{P_{\\triangle ABC}} = k$",
                        "$\\dfrac{P_{\\triangle A'B'C'}}{P_{\\triangle ABC}} = k$"],
            'answer': 3,
            'solution': 'Trong Bài 33: Hai tam giác đồng dạng, **Tỉ số chu vi của hai tam giác đồng dạng** '
                        "có công thức/quy tắc là: $\\dfrac{P_{\\triangle A'B'C'}}{P_{\\triangle ABC}} = k$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC \\sim \\triangle MNP$, biết $AB = 4\\text{ cm}, BC = 6\\text{ cm}, MN '
                 '= 8\\text{ cm}$. Độ dài cạnh $NP$ bằng:',
            'options': ['$12\\text{ cm}$', '$3\\text{ cm}$', '$10\\text{ cm}$', '$16\\text{ cm}$'],
            'answer': 0,
            'solution': 'Vì $\\triangle ABC \\sim \\triangle MNP$ nên $\\dfrac{AB}{MN} = \\dfrac{BC}{NP} '
                        '\\Rightarrow \\dfrac{4}{8} = \\dfrac{6}{NP} \\Rightarrow NP = 12\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 33: Hai tam giác đồng dạng**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Mô tả được định nghĩa của hai tam giác đồng dạng và tỉ số đồng dạng. (với dấu ngược '
                        'lại)',
                        'Mô tả được định nghĩa của hai tam giác đồng dạng và tỉ số đồng dạng.',
                        'Đảo ngược vế của quy tắc: Mô tả được định nghĩa của hai tam giác đồng dạng và tỉ số '
                        'đồng dạng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được định nghĩa của hai '
                        'tam giác đồng dạng và tỉ số đồng dạng.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 33: Hai tam giác đồng dạng: Mô tả được định nghĩa của '
                        'hai tam giác đồng dạng và tỉ số đồng dạng.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ có $M \\in AB, N \\in AC$ sao cho $MN \\parallel BC$ và '
                 '$\\dfrac{AM}{AB} = \\dfrac{1}{3}$. Xét các khẳng định sau:',
            'statements': ['Tam giác $\\triangle AMN$ đồng dạng với tam giác $\\triangle ABC$.',
                           'Tỉ số đồng dạng của $\\triangle AMN$ so với $\\triangle ABC$ là $k = '
                           '\\dfrac{1}{3}$.',
                           'Góc $\\widehat{AMN}$ bằng góc $\\widehat{ABC}$ và góc $\\widehat{ANM}$ bằng góc '
                           '$\\widehat{ACB}$.',
                           'Chu vi của $\\triangle ABC$ gấp $9$ lần chu vi của $\\triangle AMN$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì tỉ số chu vi bằng tỉ số đồng dạng nên chu vi $\\triangle '
                        'ABC$ gấp $3$ lần chu vi $\\triangle AMN$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 33: Hai tam giác đồng '
                 'dạng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được định nghĩa của hai tam giác '
                           'đồng dạng và tỉ số đồng dạng.',
                           'Trong **Bài 33: Hai tam giác đồng dạng**, quy tắc/công thức **Định nghĩa '
                           "$\\triangle A'B'C' \\sim \\triangle ABC$** được viết là: $\\widehat{A'} = "
                           "\\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và "
                           "$\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$.",
                           "Nếu áp dụng sai dấu/phép tính thành $\\widehat{A'} = \\widehat{A}, \\widehat{B'} "
                           "= \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = "
                           "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$ (với dấu ngược lại) thì kết quả của "
                           "**Định nghĩa $\\triangle A'B'C' \\sim \\triangle ABC$** trong **Bài 33: Hai tam "
                           'giác đồng dạng** vẫn không thay đổi.',
                           "Xét ví dụ của bài: “Cho $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng "
                           'dạng $k = \\dfrac{2}{3}$. Biết chu vi của $\\triangle ABC$ là $36\\text{ cm}$, '
                           "t...”, kết quả giải đúng là: Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ "
                           'số đồng dạng $k = \\dfrac{2}{3}$ nên tỉ số chu vi của hai tam giác cũng bằng '
                           '$\\dfrac{2}{3}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 33: Hai tam giác đồng dạng. b) **Đúng** '
                        "theo công thức **Định nghĩa $\\triangle A'B'C' \\sim \\triangle ABC$** "
                        "($\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, \\widehat{C'} = "
                        "\\widehat{C}$ và $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$). "
                        "c) **Sai** vì công thức đúng của **Định nghĩa $\\triangle A'B'C' \\sim \\triangle "
                        "ABC$** phải là $\\widehat{A'} = \\widehat{A}, \\widehat{B'} = \\widehat{B}, "
                        "\\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = "
                        "\\dfrac{C'A'}{CA} = k$ chứ không phải $\\widehat{A'} = \\widehat{A}, \\widehat{B'} "
                        "= \\widehat{B}, \\widehat{C'} = \\widehat{C}$ và $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} = k$ (với dấu ngược lại). d) **Đúng** theo "
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 33: Hai tam giác đồng dạng** để giải bài toán sau: '
                 "Cho $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = \\dfrac{2}{3}$. "
                 "Biết chu vi của $\\triangle ABC$ là $36\\text{ cm}$, tính chu vi của $\\triangle A'B'C'$. "
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ["Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = "
                        '\\dfrac{3}{3}$ nên tỉ số chu vi của hai tam giác cũng bằng $\\dfrac{2}{3}$. Do đó '
                        'chu...',
                        "Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = "
                        '\\dfrac{3}{2}$ nên tỉ số chu vi của hai tam giác cũng bằng $\\dfrac{2}{3}$. Do đó '
                        'chu...',
                        "Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = "
                        '\\dfrac{2}{3}$ nên tỉ số chu vi của hai tam giác cũng bằng $\\dfrac{2}{3}$. Do đó '
                        'chu...',
                        "Vì $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = "
                        '\\dfrac{4}{3}$ nên tỉ số chu vi của hai tam giác cũng bằng $\\dfrac{2}{3}$. Do đó '
                        'chu...'],
            'answer': 2,
            'solution': "Lời giải chi tiết theo Bài 33: Hai tam giác đồng dạng: Vì $\\triangle A'B'C' \\sim "
                        '\\triangle ABC$ theo tỉ số đồng dạng $k = \\dfrac{2}{3}$ nên tỉ số chu vi của hai '
                        'tam giác cũng bằng $\\dfrac{2}{3}$.\n'
                        "Do đó chu vi của $\\triangle A'B'C'$ là: $36 \\cdot \\dfrac{2}{3} = 24\\text{ "
                        '(cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC \\sim \\triangle DEF$ theo tỉ số đồng dạng $k = 2$. Biết chu vi của '
                 '$\\triangle DEF$ bằng $15\\text{ cm}$, tính chu vi của $\\triangle ABC$ (đơn vị '
                 '$\\text{cm}$).',
            'answer': ['30'],
            'unit': None,
            'solution': 'Chu vi của $\\triangle ABC$ bằng $k \\cdot 15 = 2 \\cdot 15 = 30\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch09-tam-giac-dong-dang',
  'context_title': 'Chương IX: Tam giác đồng dạng',
  'context': 'Chương IX · SGK Toán 8: Hai tam giác đồng dạng, ba trường hợp đồng dạng của tam giác, định lí '
             'Pythagore và hình đồng dạng.',
  'title': 'Bài 34: Ba trường hợp đồng dạng của hai tam giác',
  'icon': '📐',
  'description': 'Ba trường hợp đồng dạng của hai tam giác: cạnh - cạnh - cạnh (c.c.c), cạnh - góc - cạnh '
                 '(c.g.c) và góc - góc (g.g).',
  'requirements': ['Giải thích và vận dụng được ba trường hợp đồng dạng của hai tam giác: c.c.c, c.g.c và '
                   'g.g.',
                   'Vận dụng các trường hợp đồng dạng để tính độ dài đoạn thẳng, chứng minh hai góc bằng '
                   'nhau và hệ thức tích.',
                   'Vận dụng kiến thức của **Bài 34: Ba trường hợp đồng dạng của hai tam giác** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Hai tam giác đồng dạng nếu: (1) Ba cạnh của tam giác này tỉ lệ với ba cạnh của tam giác kia '
                '(c.c.c); hoặc (2) Hai cạnh của tam giác này tỉ lệ với hai cạnh của tam giác kia và hai góc '
                'tạo bởi các cặp cạnh đó bằng nhau (c.g.c); hoặc (3) Hai góc của tam giác này lần lượt bằng '
                'hai góc của tam giác kia (g.g).',
  'theory': "Ba trường hợp đồng dạng của $\\triangle A'B'C'$ và $\\triangle ABC$:\n"
            "1. Trường hợp thứ nhất (c.c.c): Nếu $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA}$ "
            "thì $\\triangle A'B'C' \\sim \\triangle ABC$.\n"
            "2. Trường hợp thứ hai (c.g.c): Nếu $\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$ và $\\widehat{A'} = "
            "\\widehat{A}$ thì $\\triangle A'B'C' \\sim \\triangle ABC$.\n"
            "3. Trường hợp thứ ba (g.g): Nếu $\\widehat{A'} = \\widehat{A}$ và $\\widehat{B'} = "
            "\\widehat{B}$ thì $\\triangle A'B'C' \\sim \\triangle ABC$.",
  'formulas': [{'category': 'Ba trường hợp đồng dạng của hai tam giác',
                'items': [{'name': 'Trường hợp cạnh - cạnh - cạnh (c.c.c)',
                           'formula': "$\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} "
                                      "\\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$"},
                          {'name': 'Trường hợp cạnh - góc - cạnh (c.g.c)',
                           'formula': "$\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$ và $\\widehat{A'} = "
                                      "\\widehat{A} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$"},
                          {'name': 'Trường hợp góc - góc (g.g)',
                           'formula': "$\\widehat{A'} = \\widehat{A}$ và $\\widehat{B'} = \\widehat{B} "
                                      "\\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$"}]}],
  'example': 'Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, AC = 6\\text{ cm}$. Trên cạnh $AB$ lấy điểm $D$ '
             'sao cho $AD = 3\\text{ cm}$, trên cạnh $AC$ lấy điểm $E$ sao cho $AE = 2\\text{ cm}$. Chứng '
             'minh $\\triangle ADE \\sim \\triangle ACB$.',
  'example_answer': 'Xét $\\triangle ADE$ và $\\triangle ACB$ có:\n'
                    '- Góc $\\widehat{A}$ chung;\n'
                    '- $\\dfrac{AD}{AC} = \\dfrac{3}{6} = \\dfrac{1}{2}$ và $\\dfrac{AE}{AB} = \\dfrac{2}{4} '
                    '= \\dfrac{1}{2} \\Rightarrow \\dfrac{AD}{AC} = \\dfrac{AE}{AB}$.\n'
                    'Vậy $\\triangle ADE \\sim \\triangle ACB$ (c.g.c).',
  'real_life': 'Ứng dụng nguyên lí buồng tối (máy ảnh) hoặc bóng nắng để đo chiều cao vật thể dựa vào hai '
               'tam giác đồng dạng (g.g).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ và $\\triangle DEF$ có $\\widehat{A} = \\widehat{D}$ và $\\widehat{B} '
                 '= \\widehat{E}$. Khi đó $\\triangle ABC \\sim \\triangle DEF$ theo trường hợp nào?',
            'options': ['Cạnh - góc - cạnh (c.g.c)',
                        'Góc - góc (g.g)',
                        'Cạnh - cạnh - cạnh (c.c.c)',
                        'Cạnh huyền - cạnh góc vuông'],
            'answer': 1,
            'solution': 'Hai góc của tam giác này lần lượt bằng hai góc của tam giác kia nên đồng dạng theo '
                        'trường hợp góc - góc (g.g).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tam giác $\\triangle ABC$ có độ dài ba cạnh là $3\\text{ cm}, 4\\text{ cm}, 5\\text{ cm}$. '
                 'Tam giác nào có độ dài ba cạnh dưới đây đồng dạng với $\\triangle ABC$?',
            'options': ['$4\\text{ cm}; 5\\text{ cm}; 6\\text{ cm}$',
                        '$3\\text{ cm}; 4\\text{ cm}; 6\\text{ cm}$',
                        '$6\\text{ cm}; 8\\text{ cm}; 10\\text{ cm}$',
                        '$9\\text{ cm}; 16\\text{ cm}; 25\\text{ cm}$'],
            'answer': 2,
            'solution': 'Vì $\\dfrac{6}{3} = \\dfrac{8}{4} = \\dfrac{10}{5} = 2$ nên hai tam giác đồng dạng '
                        'theo trường hợp c.c.c.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Ba trường hợp đồng dạng của hai tam giác**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Trường hợp cạnh - cạnh - cạnh (c.c.c)**?',
            'options': ["$\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle "
                        "A'B'C' \\sim \\triangle ABC$ (với dấu ngược lại)",
                        "$\\dfrac{AB}{A'B'} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle "
                        "A'B'C' \\sim \\triangle ABC$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle A'B'C' \\sim "
                        '\\triangle ABC$',
                        "$\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle "
                        "A'B'C' \\sim \\triangle ABC$"],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 34: Ba trường hợp đồng dạng của hai tam giác, '
                        "**Trường hợp cạnh - cạnh - cạnh (c.c.c)** được xác định bởi: $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle A'B'C' \\sim "
                        '\\triangle ABC$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Ba trường hợp đồng dạng của hai tam giác**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Trường hợp cạnh - góc - cạnh (c.g.c)**?',
            'options': ["$\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$ và $\\widehat{A'} = \\widehat{A} "
                        "\\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$",
                        "$\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$ và $\\widehat{A'} = \\widehat{A} "
                        "\\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$ (với dấu ngược lại)",
                        "$\\dfrac{AB}{A'B'} = \\dfrac{A'C'}{AC}$ và $\\widehat{A'} = \\widehat{A} "
                        "\\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{A'C'}{AC}$ và $\\widehat{A'} = \\widehat{A} \\Rightarrow \\triangle A'B'C' "
                        '\\sim \\triangle ABC$'],
            'answer': 0,
            'solution': 'Trong Bài 34: Ba trường hợp đồng dạng của hai tam giác, **Trường hợp cạnh - góc - '
                        "cạnh (c.g.c)** có công thức/quy tắc là: $\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$ và "
                        "$\\widehat{A'} = \\widehat{A} \\Rightarrow \\triangle A'B'C' \\sim \\triangle "
                        'ABC$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ và $\\triangle MNP$ có $\\widehat{A} = \\widehat{M} = 70^\\circ, AB = '
                 '6\\text{ cm}, AC = 9\\text{ cm}, MN = 4\\text{ cm}$. Để $\\triangle ABC \\sim \\triangle '
                 'MNP$ theo trường hợp c.g.c thì độ dài cạnh $MP$ phải bằng:',
            'options': ['$4\\text{ cm}$', '$6\\text{ cm}$', '$8\\text{ cm}$', '$13,5\\text{ cm}$'],
            'answer': 1,
            'solution': 'Để $\\triangle ABC \\sim \\triangle MNP$ (c.g.c) khi có $\\widehat{A} = '
                        '\\widehat{M}$ thì cần $\\dfrac{AB}{MN} = \\dfrac{AC}{MP} \\Rightarrow \\dfrac{6}{4} '
                        '= \\dfrac{9}{MP} \\Rightarrow MP = 6\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 34: Ba trường hợp đồng dạng của hai tam giác**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Giải thích và vận dụng được ba trường hợp đồng dạng của hai tam giác: c.c.c, c.g.c '
                        'và g.g. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Giải thích và vận dụng được ba trường hợp đồng dạng của '
                        'hai tam giác: c.c.c, c.g.c và g.g.',
                        'Giải thích và vận dụng được ba trường hợp đồng dạng của hai tam giác: c.c.c, c.g.c '
                        'và g.g.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải thích và vận dụng được ba '
                        'trường hợp đồng dạng của hai tam giác: c.c.c, c.g.c và g.g.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 34: Ba trường hợp đồng dạng của hai tam giác: Giải '
                        'thích và vận dụng được ba trường hợp đồng dạng của hai tam giác: c.c.c, c.g.c và '
                        'g.g.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình thang $ABCD$ ($AB \\parallel CD$) có hai đường chéo $AC$ và $BD$ cắt nhau tại '
                 '$O$. Biết $AB = 4\\text{ cm}, CD = 8\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Hai góc so le trong $\\widehat{OAB} = \\widehat{OCD}$ và $\\widehat{OBA} = '
                           '\\widehat{ODC}$.',
                           '$\\triangle OAB \\sim \\triangle OCD$ theo trường hợp góc - góc (g.g).',
                           'Tỉ số đồng dạng của $\\triangle OAB$ so với $\\triangle OCD$ là $\\dfrac{AB}{CD} '
                           '= \\dfrac{1}{2}$.',
                           'Nếu $OA = 3\\text{ cm}$ thì độ dài $OC = 9\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $\\dfrac{OA}{OC} = \\dfrac{1}{2} \\Rightarrow OC = 2 '
                        '\\cdot OA = 6\\text{ cm} \\neq 9\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 34: Ba trường hợp đồng dạng '
                 'của hai tam giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải thích và vận dụng được ba trường '
                           'hợp đồng dạng của hai tam giác: c.c.c, c.g.c và g.g.',
                           'Trong **Bài 34: Ba trường hợp đồng dạng của hai tam giác**, quy tắc/công thức '
                           "**Trường hợp cạnh - cạnh - cạnh (c.c.c)** được viết là: $\\dfrac{A'B'}{AB} = "
                           "\\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle A'B'C' \\sim "
                           '\\triangle ABC$.',
                           "Nếu áp dụng sai dấu/phép tính thành $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = "
                           "\\dfrac{C'A'}{CA} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$ (với dấu "
                           'ngược lại) thì kết quả của **Trường hợp cạnh - cạnh - cạnh (c.c.c)** trong **Bài '
                           '34: Ba trường hợp đồng dạng của hai tam giác** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, AC = 6\\text{ '
                           'cm}$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = 3\\text{ cm}$, trên cạnh $AC$ '
                           'lấy...”, kết quả giải đúng là: Xét $\\triangle ADE$ và $\\triangle ACB$ có: - '
                           'Góc $\\widehat{A}$ chung; - $\\dfrac{AD}{AC} = \\dfrac{3}{6} = \\dfrac{1}{2}$ '
                           'và...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 34: Ba trường hợp đồng dạng của hai tam '
                        'giác. b) **Đúng** theo công thức **Trường hợp cạnh - cạnh - cạnh (c.c.c)** '
                        "($\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow \\triangle "
                        "A'B'C' \\sim \\triangle ABC$). c) **Sai** vì công thức đúng của **Trường hợp cạnh - "
                        "cạnh - cạnh (c.c.c)** phải là $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = "
                        "\\dfrac{C'A'}{CA} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$ chứ không "
                        "phải $\\dfrac{A'B'}{AB} = \\dfrac{B'C'}{BC} = \\dfrac{C'A'}{CA} \\Rightarrow "
                        "\\triangle A'B'C' \\sim \\triangle ABC$ (với dấu ngược lại). d) **Đúng** theo lời "
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 34: Ba trường hợp đồng dạng của hai tam giác** để '
                 'giải bài toán sau: Cho $\\triangle ABC$ có $AB = 4\\text{ cm}, AC = 6\\text{ cm}$. Trên '
                 'cạnh $AB$ lấy điểm $D$ sao cho $AD = 3\\text{ cm}$, trên cạnh $AC$ lấy điểm $E$ sao cho '
                 '$AE = 2\\text{ cm}$. Chứng minh $\\triangle ADE \\sim \\triangle ACB$. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Xét $\\triangle ADE$ và $\\triangle ACB$ có: + Góc $\\widehat{A}$ chung; - '
                        '$\\dfrac{AD}{AC} = \\dfrac{3}{6} = \\dfrac{1}{2}$ và...',
                        'Xét $\\triangle ADE$ và $\\triangle ACB$ có: - Góc $\\widehat{A}$ chung; - '
                        '$\\dfrac{AC}{AD} = \\dfrac{3}{6} = \\dfrac{1}{2}$ và...',
                        'Xét $\\triangle ADE$ và $\\triangle ACB$ có: - Góc $\\widehat{A}$ chung; - '
                        '$\\dfrac{AD}{AC} = \\dfrac{6}{6} = \\dfrac{1}{2}$ và...',
                        'Xét $\\triangle ADE$ và $\\triangle ACB$ có: - Góc $\\widehat{A}$ chung; - '
                        '$\\dfrac{AD}{AC} = \\dfrac{3}{6} = \\dfrac{1}{2}$ và...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 34: Ba trường hợp đồng dạng của hai tam giác: Xét '
                        '$\\triangle ADE$ và $\\triangle ACB$ có:\n'
                        '- Góc $\\widehat{A}$ chung;\n'
                        '- $\\dfrac{AD}{AC} = \\dfrac{3}{6} = \\dfrac{1}{2}$ và $\\dfrac{AE}{AB} = '
                        '\\dfrac{2}{4} = \\dfrac{1}{2} \\Rightarrow \\dfrac{AD}{AC} = \\dfrac{AE}{AB}$.\n'
                        'Vậy $\\triangle ADE \\sim \\triangle ACB$ (c.g.c).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cùng một thời điểm, tia nắng mặt trời tạo với mặt đất những góc bằng nhau. Một cột cờ cao '
                 '$h\\text{ (m)}$ có bóng trên mặt đất dài $12\\text{ m}$, trong khi một cọc tiêu thẳng đứng '
                 'cao $1,5\\text{ m}$ có bóng dài $2\\text{ m}$. Tính chiều cao $h$ của cột cờ (đơn vị mét).',
            'answer': ['9'],
            'unit': None,
            'solution': 'Hai tam giác vuông tạo bởi vật và bóng nắng đồng dạng (g.g) nên $\\dfrac{h}{1,5} = '
                        '\\dfrac{12}{2} = 6 \\Rightarrow h = 6 \\cdot 1,5 = 9\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch09-tam-giac-dong-dang',
  'context_title': 'Chương IX: Tam giác đồng dạng',
  'context': 'Chương IX · SGK Toán 8: Hai tam giác đồng dạng, ba trường hợp đồng dạng của tam giác, định lí '
             'Pythagore và hình đồng dạng.',
  'title': 'Bài 35: Định lí Pythagore và ứng dụng',
  'icon': '📐',
  'description': 'Định lí Pythagore thuận, định lí Pythagore đảo và các ứng dụng tính độ dài trong thực '
                 'tiễn.',
  'requirements': ['Giải thích được định lí Pythagore thuận và định lí Pythagore đảo.',
                   'Tính được độ dài cạnh trong tam giác vuông bằng cách sử dụng định lí Pythagore và giải '
                   'quyết các bài toán thực tiễn.',
                   'Vận dụng kiến thức của **Bài 35: Định lí Pythagore và ứng dụng** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Định lí Pythagore: Trong một tam giác vuông, bình phương của cạnh huyền bằng tổng các bình '
                'phương của hai cạnh góc vuông. Định lí Pythagore đảo: Nếu một tam giác có bình phương của '
                'một cạnh bằng tổng các bình phương của hai cạnh kia thì tam giác đó là tam giác vuông.',
  'theory': '1. Định lí Pythagore thuận: Trong $\\triangle ABC$ vuông tại $A$, ta có:\n'
            '$BC^2 = AB^2 + AC^2$.\n'
            'Từ đó suy ra: $BC = \\sqrt{AB^2 + AC^2}$; $AB = \\sqrt{BC^2 - AC^2}$; $AC = \\sqrt{BC^2 - '
            'AB^2}$.\n'
            '2. Định lí Pythagore đảo: Trong $\\triangle ABC$, nếu $BC^2 = AB^2 + AC^2$ thì $\\triangle ABC$ '
            'vuông tại $A$ ($\\widehat{A} = 90^\\circ$).',
  'formulas': [{'category': 'Hệ thức Pythagore trong $\\triangle ABC$ vuông tại $A$',
                'items': [{'name': 'Định lí Pythagore', 'formula': '$BC^2 = AB^2 + AC^2$'},
                          {'name': 'Tính cạnh huyền', 'formula': '$BC = \\sqrt{AB^2 + AC^2}$'},
                          {'name': 'Tính cạnh góc vuông',
                           'formula': '$AB = \\sqrt{BC^2 - AC^2}; \\quad AC = \\sqrt{BC^2 - AB^2}$'},
                          {'name': 'Đường chéo hình chữ nhật kích thước $a, b$',
                           'formula': '$d = \\sqrt{a^2 + b^2}$'}]}],
  'example': 'Một chiếc thang dài $5\\text{ m}$ dựa vào một bức tường thẳng đứng, chân thang cách chân tường '
             '$3\\text{ m}$. Hỏi đầu trên của thang chạm tường ở độ cao bao nhiêu mét?',
  'example_answer': 'Thang, tường và mặt đất tạo thành một tam giác vuông có cạnh huyền $5\\text{ m}$ và một '
                    'cạnh góc vuông $3\\text{ m}$.\n'
                    'Áp dụng định lí Pythagore, độ cao $h$ của đầu thang là:\n'
                    '$h = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4\\text{ (m)}$.',
  'real_life': 'Thợ xây dùng bộ ba Pythagore ($3 - 4 - 5$, tức là $30\\text{ cm} - 40\\text{ cm} - 50\\text{ '
               'cm}$) để lấy góc vuông cho móng nhà; tính kích thước đường chéo màn hình tivi (theo inch).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$. Hệ thức nào sau đây là đúng theo định lí Pythagore?',
            'options': ['$AB^2 = BC^2 + AC^2$',
                        '$AC^2 = AB^2 + BC^2$',
                        '$BC^2 = AB^2 + AC^2$',
                        '$BC = AB + AC$'],
            'answer': 2,
            'solution': 'Trong $\\triangle ABC$ vuông tại $A$, cạnh huyền là $BC$ nên $BC^2 = AB^2 + AC^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tam giác có bộ ba độ dài cạnh nào sau đây là một tam giác vuông?',
            'options': ['$4\\text{ cm}; 5\\text{ cm}; 6\\text{ cm}$',
                        '$2\\text{ cm}; 3\\text{ cm}; 4\\text{ cm}$',
                        '$5\\text{ cm}; 6\\text{ cm}; 7\\text{ cm}$',
                        '$6\\text{ cm}; 8\\text{ cm}; 10\\text{ cm}$'],
            'answer': 3,
            'solution': 'Vì $6^2 + 8^2 = 36 + 64 = 100 = 10^2$ nên theo định lí Pythagore đảo, đó là tam '
                        'giác vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Định lí Pythagore và ứng dụng**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Định lí Pythagore**?',
            'options': ['$BC^2 = AB^2 + AC^2$',
                        '$BC^2 = AB^2 - AC^2$',
                        '$BC^2 = AB^2 + AC^1$',
                        '$BC^4 = AB^2 + AC^2$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 35: Định lí Pythagore và ứng dụng, **Định lí '
                        'Pythagore** được xác định bởi: $BC^2 = AB^2 + AC^2$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Định lí Pythagore và ứng dụng**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tính cạnh huyền**?',
            'options': ['$BC = \\sqrt{AB^2 - AC^2}$',
                        '$BC = \\sqrt{AB^2 + AC^2}$',
                        '$BC = \\sqrt{AB^2 + AC^1}$',
                        '$BC = \\sqrt{AB^4 + AC^2}$'],
            'answer': 1,
            'solution': 'Trong Bài 35: Định lí Pythagore và ứng dụng, **Tính cạnh huyền** có công thức/quy '
                        'tắc là: $BC = \\sqrt{AB^2 + AC^2}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$ có $AB = 5\\text{ cm}$ và $BC = 13\\text{ cm}$. Độ dài '
                 'cạnh góc vuông $AC$ bằng:',
            'options': ['$8\\text{ cm}$', '$\\sqrt{194}\\text{ cm}$', '$12\\text{ cm}$', '$10\\text{ cm}$'],
            'answer': 2,
            'solution': 'Áp dụng định lí Pythagore: $AC = \\sqrt{BC^2 - AB^2} = \\sqrt{13^2 - 5^2} = '
                        '\\sqrt{169 - 25} = \\sqrt{144} = 12\\text{ (cm)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 35: Định lí Pythagore và ứng dụng**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Giải thích được định lí Pythagore thuận và định lí Pythagore đảo. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Giải thích được định lí Pythagore thuận và định lí '
                        'Pythagore đảo.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải thích được định lí '
                        'Pythagore thuận và định lí Pythagore đảo.',
                        'Giải thích được định lí Pythagore thuận và định lí Pythagore đảo.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 35: Định lí Pythagore và ứng dụng: Giải thích được '
                        'định lí Pythagore thuận và định lí Pythagore đảo.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chữ nhật $ABCD$ có chiều rộng $AB = 9\\text{ cm}$ và chiều dài $BC = 12\\text{ '
                 'cm}$. Xét các khẳng định sau:',
            'statements': ['Tam giác $\\triangle ABC$ là tam giác vuông tại $B$.',
                           'Theo định lí Pythagore, ta có $AC^2 = AB^2 + BC^2 = 9^2 + 12^2 = 225$.',
                           'Độ dài đường chéo $AC$ bằng $15\\text{ cm}$.',
                           'Độ dài đường chéo $BD$ bằng $21\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì hai đường chéo hình chữ nhật bằng nhau nên $BD = AC = '
                        '15\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 35: Định lí Pythagore và '
                 'ứng dụng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải thích được định lí Pythagore thuận '
                           'và định lí Pythagore đảo.',
                           'Trong **Bài 35: Định lí Pythagore và ứng dụng**, quy tắc/công thức **Định lí '
                           'Pythagore** được viết là: $BC^2 = AB^2 + AC^2$.',
                           'Nếu áp dụng sai dấu/phép tính thành $BC^2 = AB^2 - AC^2$ thì kết quả của **Định '
                           'lí Pythagore** trong **Bài 35: Định lí Pythagore và ứng dụng** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Một chiếc thang dài $5\\text{ m}$ dựa vào một bức tường '
                           'thẳng đứng, chân thang cách chân tường $3\\text{ m}$. Hỏi đầu trên của thang '
                           'chạm...”, kết quả giải đúng là: Thang, tường và mặt đất tạo thành một tam giác '
                           'vuông có cạnh huyền $5\\text{ m}$ và một cạnh góc vuông $3\\text{ m}$. Áp dụng '
                           'định lí Pyt...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 35: Định lí Pythagore và ứng dụng. b) '
                        '**Đúng** theo công thức **Định lí Pythagore** ($BC^2 = AB^2 + AC^2$). c) **Sai** vì '
                        'công thức đúng của **Định lí Pythagore** phải là $BC^2 = AB^2 + AC^2$ chứ không '
                        'phải $BC^2 = AB^2 - AC^2$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 35: Định lí Pythagore và ứng dụng** để giải bài '
                 'toán sau: Một chiếc thang dài $5\\text{ m}$ dựa vào một bức tường thẳng đứng, chân thang '
                 'cách chân tường $3\\text{ m}$. Hỏi đầu trên của thang chạm tường ở độ cao bao nhiêu mét? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thang, tường và mặt đất tạo thành một tam giác vuông có cạnh huyền $5\\text{ m}$ và '
                        'một cạnh góc vuông $3\\text{ m}$. Áp dụng định lí Pythagore, độ cao...',
                        'Thang, tường và mặt đất tạo thành một tam giác vuông có cạnh huyền $6\\text{ m}$ và '
                        'một cạnh góc vuông $3\\text{ m}$. Áp dụng định lí Pythagore, độ cao...',
                        'Thang, tường và mặt đất tạo thành một tam giác vuông có cạnh huyền $5\\text{ m}$ và '
                        'một cạnh góc vuông $2\\text{ m}$. Áp dụng định lí Pythagore, độ cao...',
                        'Thang, tường và mặt đất tạo thành một tam giác vuông có cạnh huyền $10\\text{ m}$ '
                        'và một cạnh góc vuông $3\\text{ m}$. Áp dụng định lí Pythagore, độ cao...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 35: Định lí Pythagore và ứng dụng: Thang, tường và mặt '
                        'đất tạo thành một tam giác vuông có cạnh huyền $5\\text{ m}$ và một cạnh góc vuông '
                        '$3\\text{ m}$.\n'
                        'Áp dụng định lí Pythagore, độ cao $h$ của đầu thang là:\n'
                        '$h = \\sqrt{5^2 - 3^2} = \\sqrt{25 - 9} = \\sqrt{16} = 4\\text{ (m)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$ có hai cạnh góc vuông $AB = 8\\text{ cm}$ và $AC = '
                 '15\\text{ cm}$. Tính độ dài cạnh huyền $BC$ (đơn vị $\\text{cm}$).',
            'answer': ['17'],
            'unit': None,
            'solution': 'Ta có $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = '
                        '\\sqrt{289} = 17\\text{ (cm)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch09-tam-giac-dong-dang',
  'context_title': 'Chương IX: Tam giác đồng dạng',
  'context': 'Chương IX · SGK Toán 8: Hai tam giác đồng dạng, ba trường hợp đồng dạng của tam giác, định lí '
             'Pythagore và hình đồng dạng.',
  'title': 'Bài 36: Các trường hợp đồng dạng của hai tam giác vuông',
  'icon': '📐',
  'description': 'Các trường hợp đồng dạng của hai tam giác vuông và tỉ số đường cao, tỉ số diện tích của '
                 'hai tam giác đồng dạng.',
  'requirements': ['Giải thích và vận dụng được các trường hợp đồng dạng của hai tam giác vuông (góc nhọn, '
                   'hai cạnh góc vuông, cạnh huyền - cạnh góc vuông).',
                   'Vận dụng được tính chất tỉ số hai đường cao tương ứng bằng tỉ số đồng dạng $k$ và tỉ số '
                   'diện tích bằng $k^2$.',
                   'Vận dụng kiến thức của **Bài 36: Các trường hợp đồng dạng của hai tam giác vuông** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Hai tam giác vuông đồng dạng nếu: (1) Tam giác vuông này có một góc nhọn bằng góc nhọn của '
                'tam giác vuông kia; hoặc (2) Hai cạnh góc vuông của tam giác vuông này tỉ lệ với hai cạnh '
                'góc vuông của tam giác vuông kia; hoặc (3) Cạnh huyền và một cạnh góc vuông của tam giác '
                'vuông này tỉ lệ với cạnh huyền và một cạnh góc vuông của tam giác vuông kia.',
  'theory': "1. Ba dấu hiệu đồng dạng của hai tam giác vuông $\\triangle A'B'C'$ (vuông tại $A'$) và "
            '$\\triangle ABC$ (vuông tại $A$):\n'
            "- Có một cặp góc nhọn bằng nhau: $\\widehat{B'} = \\widehat{B}$ (hoặc $\\widehat{C'} = "
            '\\widehat{C}$).\n'
            "- Hai cạnh góc vuông tương ứng tỉ lệ: $\\dfrac{A'B'}{AB} = \\dfrac{A'C'}{AC}$.\n"
            "- Cạnh huyền và một cạnh góc vuông tương ứng tỉ lệ: $\\dfrac{B'C'}{BC} = \\dfrac{A'B'}{AB}$.\n"
            '2. Tỉ số đường cao và tỉ số diện tích của hai tam giác đồng dạng (theo tỉ số đồng dạng $k$):\n'
            '- Tỉ số hai đường cao tương ứng (cũng như hai trung tuyến, hai phân giác tương ứng) bằng tỉ số '
            'đồng dạng $k$.\n'
            '- Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng ($k^2$).',
  'formulas': [{'category': 'Tam giác vuông đồng dạng và tỉ số diện tích',
                'items': [{'name': 'Trường hợp cạnh huyền - cạnh góc vuông',
                           'formula': "$\\widehat{A'} = \\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = "
                                      "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle "
                                      'ABC$'},
                          {'name': 'Tỉ số hai đường cao tương ứng',
                           'formula': "$\\triangle A'B'C' \\sim \\triangle ABC$ (tỉ số $k$) $\\Rightarrow "
                                      "\\dfrac{A'H'}{AH} = k$"},
                          {'name': 'Tỉ số diện tích hai tam giác đồng dạng',
                           'formula': "$\\dfrac{S_{\\triangle A'B'C'}}{S_{\\triangle ABC}} = k^2$"}]}],
  'example': 'Cho $\\triangle ABC$ vuông tại $A$ có đường cao $AH \\perp BC$ ($H \\in BC$). Chứng minh '
             '$\\triangle HBA \\sim \\triangle ABC$ và $AB^2 = BH \\cdot BC$.',
  'example_answer': 'Xét hai tam giác vuông $\\triangle HBA$ (vuông tại $H$) và $\\triangle ABC$ (vuông tại '
                    '$A$) có góc nhọn $\\widehat{B}$ chung.\n'
                    'Do đó $\\triangle HBA \\sim \\triangle ABC$ (g.g).\n'
                    'Suy ra $\\dfrac{HB}{AB} = \\dfrac{AB}{BC} \\Rightarrow AB^2 = BH \\cdot BC$.',
  'real_life': 'Tính diện tích thực tế của một khu đất hình tam giác từ diện tích đo được trên bản đồ (nhân '
               'với bình phương mẫu số tỉ lệ bản đồ).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) và $\\triangle DEF$ (vuông tại $D$) '
                 'đồng dạng với nhau nếu có thêm điều kiện nào sau đây?',
            'options': ['$AB = DE$',
                        '$BC = EF$',
                        '$\\widehat{B} + \\widehat{C} = 90^\\circ$',
                        '$\\widehat{B} = \\widehat{E}$'],
            'answer': 3,
            'solution': 'Hai tam giác vuông có một cặp góc nhọn bằng nhau ($\\widehat{B} = \\widehat{E}$) '
                        'thì đồng dạng với nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Nếu $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = 3$ thì tỉ số diện "
                 "tích $\\dfrac{S_{\\triangle A'B'C'}}{S_{\\triangle ABC}}$ bằng:",
            'options': ['$9$', '$3$', '$6$', '$\\dfrac{1}{9}$'],
            'answer': 0,
            'solution': 'Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng: $k^2 = '
                        '3^2 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Các trường hợp đồng dạng của hai tam giác vuông**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Trường hợp cạnh huyền - cạnh góc vuông**?',
            'options': ["$\\widehat{A'} = \\widehat{A} = 100^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$",
                        "$\\widehat{A'} = \\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$",
                        "$\\widehat{A'} = \\widehat{A} = 90^\\circ$ và $\\dfrac{BC}{B'C'} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$",
                        "$\\widehat{A'} = \\widehat{A} = 92^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$"],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 36: Các trường hợp đồng dạng của hai tam giác '
                        "vuông, **Trường hợp cạnh huyền - cạnh góc vuông** được xác định bởi: $\\widehat{A'} "
                        "= \\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = \\dfrac{A'B'}{AB} \\Rightarrow "
                        "\\triangle A'B'C' \\sim \\triangle ABC$."},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Các trường hợp đồng dạng của hai tam giác vuông**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Tỉ số hai đường cao tương ứng**?',
            'options': ["$\\triangle A'B'C' \\sim \\triangle ABC$ (tỉ số $k$) $\\Rightarrow "
                        "\\dfrac{A'H'}{AH} = k$ (với dấu ngược lại)",
                        "$\\triangle A'B'C' \\sim \\triangle ABC$ (tỉ số $k$) $\\Rightarrow "
                        "\\dfrac{AH}{A'H'} = k$",
                        "$\\triangle A'B'C' \\sim \\triangle ABC$ (tỉ số $k$) $\\Rightarrow "
                        "\\dfrac{A'H'}{AH} = k$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $\\triangle A'B'C' \\sim "
                        "\\triangle ABC$ (tỉ số $k$) $\\Rightarrow \\dfrac{A'H'}{AH} = k$"],
            'answer': 2,
            'solution': 'Trong Bài 36: Các trường hợp đồng dạng của hai tam giác vuông, **Tỉ số hai đường '
                        "cao tương ứng** có công thức/quy tắc là: $\\triangle A'B'C' \\sim \\triangle ABC$ "
                        "(tỉ số $k$) $\\Rightarrow \\dfrac{A'H'}{AH} = k$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai tam giác vuông $\\triangle ABC$ (vuông tại $A$) có $AB = 3\\text{ cm}, BC = '
                 "5\\text{ cm}$ và $\\triangle A'B'C'$ (vuông tại $A'$) có $A'B' = 6\\text{ cm}, B'C' = "
                 '10\\text{ cm}$. Khi đó:',
            'options': ["$\\triangle A'B'C' \\sim \\triangle ABC$ với tỉ số đồng dạng $k = 4$",
                        'Hai tam giác không đồng dạng',
                        "$\\triangle A'B'C' = \\triangle ABC$",
                        "$\\triangle A'B'C' \\sim \\triangle ABC$ với tỉ số đồng dạng $k = 2$"],
            'answer': 3,
            'solution': "Ta có $\\dfrac{B'C'}{BC} = \\dfrac{10}{5} = 2$ và $\\dfrac{A'B'}{AB} = "
                        "\\dfrac{6}{3} = 2$ nên $\\triangle A'B'C' \\sim \\triangle ABC$ (cạnh huyền - cạnh "
                        'góc vuông) với $k = 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 36: Các trường hợp đồng dạng của hai tam giác vuông**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Giải thích và vận dụng được các trường hợp đồng dạng của hai tam giác vuông (góc '
                        'nhọn, hai cạnh góc vuông, cạnh huyền - cạnh góc vuông).',
                        'Giải thích và vận dụng được các trường hợp đồng dạng của hai tam giác vuông (góc '
                        'nhọn, hai cạnh góc vuông, cạnh huyền + cạnh góc vuông).',
                        'Đảo ngược vế của quy tắc: Giải thích và vận dụng được các trường hợp đồng dạng của '
                        'hai tam giác vuông (góc nhọn, hai cạnh góc vuông, cạnh huyền - cạnh góc vuông).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải thích và vận dụng được các '
                        'trường hợp đồng dạng của hai tam giác vuông (góc nhọn, hai cạnh góc vuông, cạnh '
                        'huyền - cạnh góc vuông).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 36: Các trường hợp đồng dạng của hai tam giác vuông: '
                        'Giải thích và vận dụng được các trường hợp đồng dạng của hai tam giác vuông (góc '
                        'nhọn, hai cạnh góc vuông, cạnh huyền - cạnh góc vuông).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho $\\triangle ABC$ vuông tại $A$ ($AB = 6\\text{ cm}, AC = 8\\text{ cm}, BC = 10\\text{ '
                 'cm}$), kẻ đường cao $AH \\perp BC$ tại $H$. Xét các khẳng định sau:',
            'statements': ['Hai tam giác vuông $\\triangle HBA$ và $\\triangle ABC$ đồng dạng với nhau.',
                           'Hai tam giác vuông $\\triangle HAC$ và $\\triangle ABC$ đồng dạng với nhau.',
                           'Ta có hệ thức $AH \\cdot BC = AB \\cdot AC$, suy ra $AH = 4,8\\text{ cm}$.',
                           'Độ dài đoạn thẳng $BH$ bằng $5\\text{ cm}$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng ($AH = \\dfrac{6 \\cdot 8}{10} = 4,8\\text{ cm}$). d) Sai vì $AB^2 '
                        '= BH \\cdot BC \\Rightarrow BH = \\dfrac{6^2}{10} = 3,6\\text{ cm} \\neq 5\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 36: Các trường hợp đồng '
                 'dạng của hai tam giác vuông**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải thích và vận dụng được các trường '
                           'hợp đồng dạng của hai tam giác vuông (góc nhọn, hai cạnh góc vuông, cạnh huyền - '
                           'cạnh góc vuông).',
                           'Trong **Bài 36: Các trường hợp đồng dạng của hai tam giác vuông**, quy tắc/công '
                           "thức **Trường hợp cạnh huyền - cạnh góc vuông** được viết là: $\\widehat{A'} = "
                           "\\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = \\dfrac{A'B'}{AB} \\Rightarrow "
                           "\\triangle A'B'C' \\sim \\triangle ABC$.",
                           "Nếu áp dụng sai dấu/phép tính thành $\\widehat{A'} = \\widehat{A} = 100^\\circ$ "
                           "và $\\dfrac{B'C'}{BC} = \\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim "
                           '\\triangle ABC$ thì kết quả của **Trường hợp cạnh huyền - cạnh góc vuông** trong '
                           '**Bài 36: Các trường hợp đồng dạng của hai tam giác vuông** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho $\\triangle ABC$ vuông tại $A$ có đường cao $AH \\perp '
                           'BC$ ($H \\in BC$). Chứng minh $\\triangle HBA \\sim \\triangle ABC$ và $AB^2 = '
                           'BH \\cdot BC$...”, kết quả giải đúng là: Xét hai tam giác vuông $\\triangle HBA$ '
                           '(vuông tại $H$) và $\\triangle ABC$ (vuông tại $A$) có góc nhọn $\\widehat{B}$ '
                           'chung. Do đó $\\triangle HBA \\sim \\triangle ABC$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 36: Các trường hợp đồng dạng của hai tam '
                        'giác vuông. b) **Đúng** theo công thức **Trường hợp cạnh huyền - cạnh góc vuông** '
                        "($\\widehat{A'} = \\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$). c) **Sai** "
                        'vì công thức đúng của **Trường hợp cạnh huyền - cạnh góc vuông** phải là '
                        "$\\widehat{A'} = \\widehat{A} = 90^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$ chứ không "
                        "phải $\\widehat{A'} = \\widehat{A} = 100^\\circ$ và $\\dfrac{B'C'}{BC} = "
                        "\\dfrac{A'B'}{AB} \\Rightarrow \\triangle A'B'C' \\sim \\triangle ABC$. d) **Đúng** "
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 36: Các trường hợp đồng dạng của hai tam giác '
                 'vuông** để giải bài toán sau: Cho $\\triangle ABC$ vuông tại $A$ có đường cao $AH \\perp '
                 'BC$ ($H \\in BC$). Chứng minh $\\triangle HBA \\sim \\triangle ABC$ và $AB^2 = BH \\cdot '
                 'BC$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Xét hai tam giác vuông $\\triangle HBA$ (vuông tại $H$) và $\\triangle ABC$ (vuông '
                        'tại $A$) có góc nhọn $\\widehat{B}$ chung. Do đó $\\triangle HBA \\sim \\triangle '
                        'ABC$...',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 36: Các trường hợp đồng dạng của hai tam giác vuông: Xét '
                        'hai tam giác vuông $\\triangle HBA$ (vuông tại $H$) và $\\triangle ABC$ (vuông tại '
                        '$A$) có góc nhọn $\\widehat{B}$ chung.\n'
                        'Do đó $\\triangle HBA \\sim \\triangle ABC$ (g.g).\n'
                        'Suy ra $\\dfrac{HB}{AB} = \\dfrac{AB}{BC} \\Rightarrow AB^2 = BH \\cdot BC$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': "Cho $\\triangle A'B'C' \\sim \\triangle ABC$ theo tỉ số đồng dạng $k = 2$. Biết diện tích "
                 "của $\\triangle ABC$ bằng $15\\text{ cm}^2$, tính diện tích của $\\triangle A'B'C'$ (đơn "
                 'vị $\\text{cm}^2$).',
            'answer': ['60'],
            'unit': None,
            'solution': "Ta có $\\dfrac{S_{\\triangle A'B'C'}}{S_{\\triangle ABC}} = k^2 = 2^2 = 4 "
                        "\\Rightarrow S_{\\triangle A'B'C'} = 4 \\cdot 15 = 60\\text{ (cm}^2\\text{)}$.",
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch09-tam-giac-dong-dang',
  'context_title': 'Chương IX: Tam giác đồng dạng',
  'context': 'Chương IX · SGK Toán 8: Hai tam giác đồng dạng, ba trường hợp đồng dạng của tam giác, định lí '
             'Pythagore và hình đồng dạng.',
  'title': 'Bài 37: Hình đồng dạng',
  'icon': '🖼️',
  'description': 'Nhận biết các cặp hình đồng dạng phối cảnh, hình đồng dạng và tỉ số đồng dạng trong toán '
                 'học và thực tiễn.',
  'requirements': ['Nhận biết được hai hình đồng dạng phối cảnh (vị tự) và tâm phối cảnh.',
                   'Nhận biết được hai hình đồng dạng và vẻ đẹp của các hình đồng dạng trong tự nhiên, nghệ '
                   'thuật, kiến trúc.',
                   'Vận dụng kiến thức của **Bài 37: Hình đồng dạng** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': "Nếu với mỗi điểm $M$ thuộc hình $\\mathcal{H}$, lấy điểm $M'$ trên tia $OM$ sao cho $OM' = "
                "k \\cdot OM$ ($k > 0$) thì các điểm $M'$ tạo thành hình $\\mathcal{H}'$ gọi là đồng dạng "
                'phối cảnh với hình $\\mathcal{H}$ theo tâm $O$ và tỉ số vị tự $k$. Một hình '
                "$\\mathcal{H}''$ bằng hình $\\mathcal{H}'$ thì gọi là đồng dạng với hình $\\mathcal{H}$ "
                'theo tỉ số $k$.',
  'theory': '1. Hình đồng dạng phối cảnh: Với tâm phối cảnh $O$ và tỉ số $k > 0$, mọi khoảng cách giữa hai '
            "điểm bất kì trong hình $\\mathcal{H}'$ đều bằng $k$ lần khoảng cách giữa hai điểm tương ứng "
            'trong hình $\\mathcal{H}$.\n'
            '2. Hình đồng dạng trong thực tiễn:\n'
            '- Hai hình vuông bất kì luôn đồng dạng với nhau; hai hình tròn bất kì luôn đồng dạng với nhau; '
            'hai tam giác đều bất kì luôn đồng dạng với nhau.\n'
            '- Khi phóng to hay thu nhỏ một bức ảnh theo đúng tỉ lệ khung hình, ta nhận được các hình đồng '
            'dạng.',
  'formulas': [{'category': 'Quan hệ kích thước của hai hình đồng dạng',
                'items': [{'name': 'Định nghĩa tâm phối cảnh $O$, tỉ số $k$',
                           'formula': "$OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot AB$"},
                          {'name': 'Tỉ số chu vi và diện tích hai hình đồng dạng',
                           'formula': "$\\dfrac{P'}{P} = k; \\quad \\dfrac{S'}{S} = k^2$"}]}],
  'example': 'Một bức ảnh hình chữ nhật có kích thước $10\\text{ cm} \\times 15\\text{ cm}$ được phóng to '
             'thành một bức ảnh đồng dạng có chiều rộng $30\\text{ cm}$. Tính tỉ số đồng dạng $k$ và chiều '
             'dài của bức ảnh sau khi phóng to.',
  'example_answer': 'Tỉ số đồng dạng của bức ảnh mới so với bức ảnh ban đầu là $k = \\dfrac{30}{10} = 3$.\n'
                    'Chiều dài của bức ảnh sau khi phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$.',
  'real_life': 'Phóng to, thu nhỏ ảnh trên màn hình điện thoại, máy chiếu phim hoặc chế tạo mô hình máy bay, '
               'ô tô thu nhỏ theo tỉ lệ $1:18, 1:24$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cặp hình nào sau đây luôn luôn là hai hình đồng dạng với nhau?',
            'options': ['Hai hình vuông bất kì',
                        'Hai hình chữ nhật bất kì',
                        'Hai hình thoi bất kì',
                        'Hai tam giác cân bất kì'],
            'answer': 0,
            'solution': 'Hai hình vuông bất kì luôn có các góc bằng $90^\\circ$ và tỉ số các cạnh tương ứng '
                        'bằng nhau nên luôn đồng dạng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': "Cho hình $\\mathcal{H}'$ đồng dạng phối cảnh với hình $\\mathcal{H}$ theo tỉ số $k = 3$. "
                 'Nếu đoạn thẳng $AB$ trên hình $\\mathcal{H}$ dài $4\\text{ cm}$ thì đoạn thẳng tương ứng '
                 "$A'B'$ trên hình $\\mathcal{H}'$ dài:",
            'options': ['$4\\text{ cm}$', '$12\\text{ cm}$', '$7\\text{ cm}$', '$\\dfrac{4}{3}\\text{ cm}$'],
            'answer': 1,
            'solution': "Ta có $A'B' = k \\cdot AB = 3 \\cdot 4 = 12\\text{ (cm)}$.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 37: Hình đồng dạng**, quy tắc hoặc công thức nào sau đây xác định đúng **Định '
                 'nghĩa tâm phối cảnh $O$, tỉ số $k$**?',
            'options': ["$OM' = k : OM \\Rightarrow A'B' = k \\cdot AB$",
                        "Đảo ngược vế của quy tắc: $OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot AB$",
                        "$OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot AB$",
                        "Trường hợp trái ngược: không thỏa mãn điều kiện của $OM' = k \\cdot OM \\Rightarrow "
                        "A'B' = k \\cdot AB$"],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 37: Hình đồng dạng, **Định nghĩa tâm phối cảnh '
                        "$O$, tỉ số $k$** được xác định bởi: $OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot "
                        'AB$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 37: Hình đồng dạng**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Tỉ số chu vi và diện tích hai hình đồng dạng**?',
            'options': ["$\\dfrac{P'}{P} = k; \\quad \\dfrac{S'}{S} = k^3$",
                        "$\\dfrac{P}{P'} = k; \\quad \\dfrac{S'}{S} = k^2$",
                        "$\\dfrac{P'}{P} = k; \\quad \\dfrac{S'}{S} = k^4$",
                        "$\\dfrac{P'}{P} = k; \\quad \\dfrac{S'}{S} = k^2$"],
            'answer': 3,
            'solution': 'Trong Bài 37: Hình đồng dạng, **Tỉ số chu vi và diện tích hai hình đồng dạng** có '
                        "công thức/quy tắc là: $\\dfrac{P'}{P} = k; \\quad \\dfrac{S'}{S} = k^2$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai hình chữ nhật $\\mathcal{H}_1$ (kích thước $4\\text{ cm} \\times 6\\text{ cm}$) và '
                 '$\\mathcal{H}_2$ (kích thước $6\\text{ cm} \\times x\\text{ cm}$) đồng dạng với nhau ($x > '
                 '6$). Giá trị của $x$ là:',
            'options': ['$9$', '$8$', '$10$', '$12$'],
            'answer': 0,
            'solution': 'Vì hai hình chữ nhật đồng dạng nên tỉ số chiều rộng và chiều dài tương ứng bằng '
                        'nhau: $\\dfrac{4}{6} = \\dfrac{6}{x} \\Rightarrow x = 9$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 37: Hình đồng dạng**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được hai hình đồng dạng phối cảnh (vị tự) và tâm phối cảnh. (với dấu '
                        'ngược lại)',
                        'Nhận biết được hai hình đồng dạng phối cảnh (vị tự) và tâm phối cảnh.',
                        'Đảo ngược vế của quy tắc: Nhận biết được hai hình đồng dạng phối cảnh (vị tự) và '
                        'tâm phối cảnh.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hai hình đồng '
                        'dạng phối cảnh (vị tự) và tâm phối cảnh.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 37: Hình đồng dạng: Nhận biết được hai hình đồng dạng '
                        'phối cảnh (vị tự) và tâm phối cảnh.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của các khẳng định sau về hình đồng dạng:',
            'statements': ['Hai hình tròn bất kì luôn là hai hình đồng dạng.',
                           'Hai tam giác đều bất kì luôn là hai hình đồng dạng.',
                           "Nếu hình $\\mathcal{H}'$ đồng dạng với hình $\\mathcal{H}$ theo tỉ số $k = "
                           "\\dfrac{1}{2}$ thì hình $\\mathcal{H}'$ là hình thu nhỏ của hình $\\mathcal{H}$.",
                           'Hai hình chữ nhật bất kì có chu vi bằng nhau thì luôn đồng dạng với nhau.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai (ví dụ hình chữ nhật $1 \\times 5$ và $2 \\times 4$ có cùng '
                        'chu vi $12$ nhưng $\\dfrac{1}{2} \\neq \\dfrac{5}{4}$ nên không đồng dạng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 37: Hình đồng dạng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hai hình đồng dạng phối '
                           'cảnh (vị tự) và tâm phối cảnh.',
                           'Trong **Bài 37: Hình đồng dạng**, quy tắc/công thức **Định nghĩa tâm phối cảnh '
                           "$O$, tỉ số $k$** được viết là: $OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot "
                           'AB$.',
                           "Nếu áp dụng sai dấu/phép tính thành $OM' = k : OM \\Rightarrow A'B' = k \\cdot "
                           'AB$ thì kết quả của **Định nghĩa tâm phối cảnh $O$, tỉ số $k$** trong **Bài 37: '
                           'Hình đồng dạng** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một bức ảnh hình chữ nhật có kích thước $10\\text{ cm} '
                           '\\times 15\\text{ cm}$ được phóng to thành một bức ảnh đồng dạng có chiều rộng '
                           '$30\\text{ cm}$...”, kết quả giải đúng là: Tỉ số đồng dạng của bức ảnh mới so '
                           'với bức ảnh ban đầu là $k = \\dfrac{30}{10} = 3$. Chiều dài của bức ảnh sau khi '
                           'phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 37: Hình đồng dạng. b) **Đúng** theo công '
                        "thức **Định nghĩa tâm phối cảnh $O$, tỉ số $k$** ($OM' = k \\cdot OM \\Rightarrow "
                        "A'B' = k \\cdot AB$). c) **Sai** vì công thức đúng của **Định nghĩa tâm phối cảnh "
                        "$O$, tỉ số $k$** phải là $OM' = k \\cdot OM \\Rightarrow A'B' = k \\cdot AB$ chứ "
                        "không phải $OM' = k : OM \\Rightarrow A'B' = k \\cdot AB$. d) **Đúng** theo lời "
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 37: Hình đồng dạng** để giải bài toán sau: Một bức '
                 'ảnh hình chữ nhật có kích thước $10\\text{ cm} \\times 15\\text{ cm}$ được phóng to thành '
                 'một bức ảnh đồng dạng có chiều rộng $30\\text{ cm}$. Tính tỉ số đồng dạng $k$ và chiều dài '
                 'của bức ảnh sau khi phóng to. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tỉ số đồng dạng của bức ảnh mới so với bức ảnh ban đầu là $k = \\dfrac{30}{10} = '
                        '3$. Chiều dài của bức ảnh sau khi phóng to là $15 : 3 = 45\\text{ (cm)}$...',
                        'Tỉ số đồng dạng của bức ảnh mới so với bức ảnh ban đầu là $k = \\dfrac{10}{30} = '
                        '3$. Chiều dài của bức ảnh sau khi phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$...',
                        'Tỉ số đồng dạng của bức ảnh mới so với bức ảnh ban đầu là $k = \\dfrac{30}{10} = '
                        '3$. Chiều dài của bức ảnh sau khi phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$...',
                        'Tỉ số đồng dạng của bức ảnh mới so với bức ảnh ban đầu là $k = \\dfrac{60}{10} = '
                        '3$. Chiều dài của bức ảnh sau khi phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 37: Hình đồng dạng: Tỉ số đồng dạng của bức ảnh mới so '
                        'với bức ảnh ban đầu là $k = \\dfrac{30}{10} = 3$.\n'
                        'Chiều dài của bức ảnh sau khi phóng to là $15 \\cdot 3 = 45\\text{ (cm)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một mô hình chiếc cầu được làm đồng dạng với chiếc cầu thực tế theo tỉ lệ $1 : 500$. Biết '
                 'chiều dài của mô hình là $0,8\\text{ m}$, tính chiều dài thực tế của chiếc cầu đó (đơn vị '
                 'mét).',
            'answer': ['400'],
            'unit': None,
            'solution': 'Chiều dài thực tế của chiếc cầu là $0,8 \\cdot 500 = 400\\text{ (m)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch10-hinh-chop-deu',
  'context_title': 'Chương X: Một số hình khối trong thực tiễn',
  'context': 'Chương X · SGK Toán 8: Hình chóp tam giác đều và hình chóp tứ giác đều (diện tích xung quanh '
             'và thể tích).',
  'title': 'Bài 38: Hình chóp tam giác đều',
  'icon': '🔺',
  'description': 'Các yếu tố đỉnh, mặt đáy, mặt bên, cạnh bên, trung đoạn và công thức diện tích xung quanh, '
                 'thể tích của hình chóp tam giác đều.',
  'requirements': ['Mô tả được đỉnh, mặt đáy, mặt bên, cạnh bên, đường cao và trung đoạn của hình chóp tam '
                   'giác đều.',
                   'Tính được diện tích xung quanh và thể tích của hình chóp tam giác đều trong giải toán và '
                   'thực tiễn.',
                   'Vận dụng kiến thức của **Bài 38: Hình chóp tam giác đều** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Hình chóp tam giác đều có đáy là một tam giác đều và các mặt bên là các tam giác cân bằng '
                'nhau có chung một đỉnh. Đường cao kẻ từ đỉnh của mỗi mặt bên gọi là một trung đoạn của hình '
                'chóp tam giác đều.',
  'theory': '1. Các yếu tố của hình chóp tam giác đều $S.ABC$:\n'
            '- Đỉnh $S$, mặt đáy $\\triangle ABC$ là tam giác đều ($AB = BC = CA$).\n'
            '- Các mặt bên $\\triangle SAB, \\triangle SBC, \\triangle SCA$ là các tam giác cân bằng nhau '
            'tại đỉnh $S$ ($SA = SB = SC$).\n'
            '- Chân đường cao $SO$ của hình chóp trùng với trọng tâm (cũng là giao điểm ba đường trung trực) '
            'của mặt đáy $\\triangle ABC$.\n'
            '- Các trung đoạn của hình chóp tam giác đều bằng nhau (kí hiệu là $d$).\n'
            '2. Công thức tính diện tích xung quanh và thể tích:\n'
            '- Diện tích xung quanh bằng tích của nửa chu vi đáy với trung đoạn: $S_{xq} = p \\cdot d$.\n'
            '- Thể tích bằng một phần ba tích của diện tích đáy với chiều cao: $V = \\dfrac{1}{3} '
            'S_{\\text{đáy}} \\cdot h$.',
  'formulas': [{'category': 'Công thức hình chóp tam giác đều',
                'items': [{'name': 'Diện tích xung quanh (cạnh đáy $a$, trung đoạn $d$)',
                           'formula': '$S_{xq} = p \\cdot d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi '
                                      'đáy)'},
                          {'name': 'Diện tích toàn phần', 'formula': '$S_{tp} = S_{xq} + S_{\\text{đáy}}$'},
                          {'name': 'Thể tích hình chóp tam giác đều',
                           'formula': '$V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h$ ($h$: chiều cao hình '
                                      'chóp)'}]}],
  'example': 'Cho hình chóp tam giác đều $S.ABC$ có độ dài cạnh đáy bằng $6\\text{ cm}$ và độ dài trung đoạn '
             '$SI = 8\\text{ cm}$. Tính diện tích xung quanh của hình chóp.',
  'example_answer': 'Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{6 + 6 + 6}{2} = 9\\text{ (cm)}$.\n'
                    'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = 72\\text{ '
                    '(cm}^2\\text{)}$.',
  'real_life': 'Thiết kế hộp quà trang trí, khối rubik Pyraminx hoặc giàn đèn pha lê có dạng hình chóp tam '
               'giác đều.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Mặt đáy của một hình chóp tam giác đều là hình gì?',
            'options': ['Tam giác vuông', 'Tam giác đều', 'Tam giác cân bất kì', 'Hình vuông'],
            'answer': 1,
            'solution': 'Hình chóp tam giác đều có mặt đáy là một tam giác đều và các mặt bên là các tam '
                        'giác cân bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích xung quanh $S_{xq}$ của hình chóp tam giác đều có nửa chu vi đáy '
                 '$p$ và trung đoạn $d$ là:',
            'options': ['$S_{xq} = 2p \\cdot d$',
                        '$S_{xq} = \\dfrac{1}{3} p \\cdot d$',
                        '$S_{xq} = p \\cdot d$',
                        '$S_{xq} = \\dfrac{1}{2} p \\cdot d$'],
            'answer': 2,
            'solution': 'Diện tích xung quanh của hình chóp tam giác đều bằng tích của nửa chu vi đáy với '
                        'trung đoạn: $S_{xq} = p \\cdot d$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38: Hình chóp tam giác đều**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Diện tích xung quanh (cạnh đáy $a$, trung đoạn $d$)**?',
            'options': ['$S_{xq} = p : d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy)',
                        '$S_{xq} = p \\cdot d = \\dfrac{2}{3a} \\cdot d$ ($p$: nửa chu vi đáy)',
                        '$S_{xq} = p \\cdot d = \\dfrac{3a}{4} \\cdot d$ ($p$: nửa chu vi đáy)',
                        '$S_{xq} = p \\cdot d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 38: Hình chóp tam giác đều, **Diện tích xung quanh '
                        '(cạnh đáy $a$, trung đoạn $d$)** được xác định bởi: $S_{xq} = p \\cdot d = '
                        '\\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy).'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 38: Hình chóp tam giác đều**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Diện tích toàn phần**?',
            'options': ['$S_{tp} = S_{xq} + S_{\\text{đáy}}$',
                        '$S_{tp} = S_{xq} - S_{\\text{đáy}}$',
                        'Đảo ngược vế của quy tắc: $S_{tp} = S_{xq} + S_{\\text{đáy}}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $S_{tp} = S_{xq} + '
                        'S_{\\text{đáy}}$'],
            'answer': 0,
            'solution': 'Trong Bài 38: Hình chóp tam giác đều, **Diện tích toàn phần** có công thức/quy tắc '
                        'là: $S_{tp} = S_{xq} + S_{\\text{đáy}}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình chóp tam giác đều có diện tích đáy bằng $18\\text{ cm}^2$ và chiều cao bằng '
                 '$10\\text{ cm}$. Thể tích của hình chóp đó là:',
            'options': ['$180\\text{ cm}^3$', '$60\\text{ cm}^3$', '$90\\text{ cm}^3$', '$30\\text{ cm}^3$'],
            'answer': 1,
            'solution': 'Thể tích hình chóp là $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} '
                        '\\cdot 18 \\cdot 10 = 60\\text{ (cm}^3\\text{)}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 38: Hình chóp tam giác đều**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Mô tả được đỉnh, mặt đáy, mặt bên, cạnh bên, đường cao và trung đoạn của hình chóp '
                        'tam giác đều. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được đỉnh, mặt đáy, mặt bên, cạnh bên, đường cao và '
                        'trung đoạn của hình chóp tam giác đều.',
                        'Mô tả được đỉnh, mặt đáy, mặt bên, cạnh bên, đường cao và trung đoạn của hình chóp '
                        'tam giác đều.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được đỉnh, mặt đáy, mặt '
                        'bên, cạnh bên, đường cao và trung đoạn của hình chóp tam giác đều.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 38: Hình chóp tam giác đều: Mô tả được đỉnh, mặt đáy, '
                        'mặt bên, cạnh bên, đường cao và trung đoạn của hình chóp tam giác đều.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp tam giác đều $S.ABC$ có cạnh đáy $AB = 10\\text{ cm}$ và trung đoạn $SM = '
                 '12\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Hình chóp tam giác đều $S.ABC$ có tất cả $4$ mặt (gồm $1$ mặt đáy và $3$ mặt '
                           'bên).',
                           'Chu vi đáy của hình chóp bằng $30\\text{ cm}$ và nửa chu vi đáy là $p = '
                           '15\\text{ cm}$.',
                           'Diện tích một mặt bên của hình chóp là $\\dfrac{1}{2} \\cdot 10 \\cdot 12 = '
                           '60\\text{ cm}^2$.',
                           'Diện tích xung quanh của hình chóp bằng $360\\text{ cm}^2$.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng. d) Sai vì $S_{xq} = p \\cdot d = 15 \\cdot 12 = 180\\text{ cm}^2$ '
                        '(bằng tổng diện tích $3$ mặt bên).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 38: Hình chóp tam giác '
                 'đều**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được đỉnh, mặt đáy, mặt bên, cạnh '
                           'bên, đường cao và trung đoạn của hình chóp tam giác đều.',
                           'Trong **Bài 38: Hình chóp tam giác đều**, quy tắc/công thức **Diện tích xung '
                           'quanh (cạnh đáy $a$, trung đoạn $d$)** được viết là: $S_{xq} = p \\cdot d = '
                           '\\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy).',
                           'Nếu áp dụng sai dấu/phép tính thành $S_{xq} = p : d = \\dfrac{3a}{2} \\cdot d$ '
                           '($p$: nửa chu vi đáy) thì kết quả của **Diện tích xung quanh (cạnh đáy $a$, '
                           'trung đoạn $d$)** trong **Bài 38: Hình chóp tam giác đều** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho hình chóp tam giác đều $S.ABC$ có độ dài cạnh đáy bằng '
                           '$6\\text{ cm}$ và độ dài trung đoạn $SI = 8\\text{ cm}$. Tính diện tích xung '
                           'q...”, kết quả giải đúng là: Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{6 '
                           '+ 6 + 6}{2} = 9\\text{ (cm)}$. Diện tích xung quanh của hình chóp là: $S_{xq} = '
                           'p \\cdot d = 9 \\cdot 8 = 72\\text{ (cm}^2\\text{)}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 38: Hình chóp tam giác đều. b) **Đúng** '
                        'theo công thức **Diện tích xung quanh (cạnh đáy $a$, trung đoạn $d$)** ($S_{xq} = p '
                        '\\cdot d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy)). c) **Sai** vì công thức '
                        'đúng của **Diện tích xung quanh (cạnh đáy $a$, trung đoạn $d$)** phải là $S_{xq} = '
                        'p \\cdot d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy) chứ không phải $S_{xq} '
                        '= p : d = \\dfrac{3a}{2} \\cdot d$ ($p$: nửa chu vi đáy). d) **Đúng** theo lời giải '
                        'ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 38: Hình chóp tam giác đều** để giải bài toán sau: '
                 'Cho hình chóp tam giác đều $S.ABC$ có độ dài cạnh đáy bằng $6\\text{ cm}$ và độ dài trung '
                 'đoạn $SI = 8\\text{ cm}$. Tính diện tích xung quanh của hình chóp. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{6 - 6 + 6}{2} = 9\\text{ (cm)}$. '
                        'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = '
                        '72\\text{ (cm}^2\\text{)}$...',
                        'Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{2}{6 + 6 + 6} = 9\\text{ (cm)}$. '
                        'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = '
                        '72\\text{ (cm}^2\\text{)}$...',
                        'Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{12 + 6 + 6}{2} = 9\\text{ (cm)}$. '
                        'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = '
                        '72\\text{ (cm}^2\\text{)}$...',
                        'Nửa chu vi mặt đáy tam giác đều là: $p = \\dfrac{6 + 6 + 6}{2} = 9\\text{ (cm)}$. '
                        'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = '
                        '72\\text{ (cm}^2\\text{)}$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 38: Hình chóp tam giác đều: Nửa chu vi mặt đáy tam giác '
                        'đều là: $p = \\dfrac{6 + 6 + 6}{2} = 9\\text{ (cm)}$.\n'
                        'Diện tích xung quanh của hình chóp là: $S_{xq} = p \\cdot d = 9 \\cdot 8 = '
                        '72\\text{ (cm}^2\\text{)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính diện tích xung quanh của một hình chóp tam giác đều có độ dài cạnh đáy bằng $8\\text{ '
                 'cm}$ và trung đoạn bằng $10\\text{ cm}$ (đơn vị $\\text{cm}^2$).',
            'answer': ['120'],
            'unit': None,
            'solution': 'Nửa chu vi đáy là $p = \\dfrac{3 \\cdot 8}{2} = 12\\text{ (cm)}$. Diện tích xung '
                        'quanh là $S_{xq} = 12 \\cdot 10 = 120\\text{ (cm}^2\\text{)}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l8-ch10-hinh-chop-deu',
  'context_title': 'Chương X: Một số hình khối trong thực tiễn',
  'context': 'Chương X · SGK Toán 8: Hình chóp tam giác đều và hình chóp tứ giác đều (diện tích xung quanh '
             'và thể tích).',
  'title': 'Bài 39: Hình chóp tứ giác đều',
  'icon': '⛺',
  'description': 'Các yếu tố đỉnh, mặt đáy, mặt bên, trung đoạn, chiều cao và công thức diện tích xung '
                 'quanh, thể tích của hình chóp tứ giác đều.',
  'requirements': ['Mô tả được đỉnh, mặt đáy (hình vuông), mặt bên (tam giác cân), đường cao và trung đoạn '
                   'của hình chóp tứ giác đều.',
                   'Tính được diện tích xung quanh, diện tích toàn phần và thể tích của hình chóp tứ giác '
                   'đều trong các bài toán thực tiễn.',
                   'Vận dụng kiến thức của **Bài 39: Hình chóp tứ giác đều** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': 'Hình chóp tứ giác đều có mặt đáy là một hình vuông và $4$ mặt bên là các tam giác cân bằng '
                'nhau có chung một đỉnh. Chân đường cao của hình chóp tứ giác đều trùng với giao điểm hai '
                'đường chéo của mặt đáy.',
  'theory': '1. Các yếu tố của hình chóp tứ giác đều $S.ABCD$:\n'
            '- Đỉnh $S$; mặt đáy $ABCD$ là hình vuông cạnh $a$; $4$ mặt bên $\\triangle SAB, \\triangle SBC, '
            '\\triangle SCD, \\triangle SDA$ là các tam giác cân bằng nhau tại đỉnh $S$.\n'
            '- Đường cao $SO$ ($O$ là giao điểm của hai đường chéo $AC$ và $BD$); trung đoạn $SI = d$ (đường '
            'cao của tam giác cân mặt bên).\n'
            '- Quan hệ Pythagore giữa chiều cao $h = SO$, trung đoạn $d = SI$ và cạnh đáy $a$: $d^2 = h^2 + '
            '\\left(\\dfrac{a}{2}\\right)^2$.\n'
            '2. Công thức tính diện tích và thể tích:\n'
            '- Diện tích xung quanh: $S_{xq} = p \\cdot d = 2a \\cdot d$ (với $p = \\dfrac{4a}{2} = 2a$ là '
            'nửa chu vi đáy).\n'
            '- Thể tích: $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} a^2 h$.',
  'formulas': [{'category': 'Công thức hình chóp tứ giác đều (cạnh đáy $a$, trung đoạn $d$, cao $h$)',
                'items': [{'name': 'Diện tích xung quanh', 'formula': '$S_{xq} = p \\cdot d = 2a \\cdot d$'},
                          {'name': 'Diện tích toàn phần',
                           'formula': '$S_{tp} = S_{xq} + S_{\\text{đáy}} = 2ad + a^2$'},
                          {'name': 'Thể tích hình chóp tứ giác đều',
                           'formula': '$V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} a^2 h$'},
                          {'name': 'Hệ thức Pythagore liên hệ $d, h, a$',
                           'formula': '$d^2 = h^2 + \\left(\\dfrac{a}{2}\\right)^2$'}]}],
  'example': 'Một mái che giếng trời có dạng hình chóp tứ giác đều với cạnh đáy $a = 2\\text{ m}$ và chiều '
             'cao $h = 1,2\\text{ m}$. Tính thể tích phần không gian bên trong mái che và độ dài trung đoạn '
             'của mái che.',
  'example_answer': '- Diện tích đáy hình vuông là: $S_{\\text{đáy}} = 2^2 = 4\\text{ (m}^2\\text{)}$.\n'
                    '- Thể tích phần không gian bên trong là: $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = '
                    '\\dfrac{1}{3} \\cdot 4 \\cdot 1,2 = 1,6\\text{ (m}^3\\text{)}$.\n'
                    '- Độ dài trung đoạn là: $d = \\sqrt{h^2 + \\left(\\dfrac{a}{2}\\right)^2} = '
                    '\\sqrt{1,2^2 + 1^2} = \\sqrt{2,44} \\approx 1,56\\text{ (m)}$.',
  'real_life': 'Kiến trúc Kim tự tháp Ai Cập, Kim tự tháp kính bảo tàng Louvre (Pháp), mái nhà chòi nghỉ mát '
               'hoặc lều cắm trại 4 mặt.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Mặt đáy của một hình chóp tứ giác đều là hình gì?',
            'options': ['Hình thoi bất kì', 'Hình chữ nhật bất kì', 'Hình vuông', 'Hình bình hành'],
            'answer': 2,
            'solution': 'Hình chóp tứ giác đều có đáy là một hình vuông và $4$ mặt bên là các tam giác cân '
                        'bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thể tích $V$ của hình chóp tứ giác đều có cạnh đáy bằng $a$ và chiều cao '
                 '$h$ là:',
            'options': ['$V = a^2 h$',
                        '$V = \\dfrac{1}{2} a^2 h$',
                        '$V = \\dfrac{1}{3} \\cdot 4a \\cdot h$',
                        '$V = \\dfrac{1}{3} a^2 h$'],
            'answer': 3,
            'solution': 'Diện tích đáy hình vuông là $S_{\\text{đáy}} = a^2$, nên thể tích là $V = '
                        '\\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} a^2 h$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39: Hình chóp tứ giác đều**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Diện tích xung quanh**?',
            'options': ['$S_{xq} = p \\cdot d = 2a \\cdot d$',
                        '$S_{xq} = p : d = 2a \\cdot d$',
                        'Đảo ngược vế của quy tắc: $S_{xq} = p \\cdot d = 2a \\cdot d$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $S_{xq} = p \\cdot d = 2a '
                        '\\cdot d$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 39: Hình chóp tứ giác đều, **Diện tích xung '
                        'quanh** được xác định bởi: $S_{xq} = p \\cdot d = 2a \\cdot d$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 39: Hình chóp tứ giác đều**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Diện tích toàn phần**?',
            'options': ['$S_{tp} = S_{xq} - S_{\\text{đáy}} = 2ad + a^2$',
                        '$S_{tp} = S_{xq} + S_{\\text{đáy}} = 2ad + a^2$',
                        '$S_{tp} = S_{xq} + S_{\\text{đáy}} = 2ad + a^1$',
                        '$S_{tp} = S_{xq} + S_{\\text{đáy}} = 2ad + a^4$'],
            'answer': 1,
            'solution': 'Trong Bài 39: Hình chóp tứ giác đều, **Diện tích toàn phần** có công thức/quy tắc '
                        'là: $S_{tp} = S_{xq} + S_{\\text{đáy}} = 2ad + a^2$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hình chóp tứ giác đều có độ dài cạnh đáy $a = 6\\text{ cm}$ và độ dài trung đoạn $d = '
                 '5\\text{ cm}$. Diện tích toàn phần của hình chóp đó là:',
            'options': ['$60\\text{ cm}^2$', '$36\\text{ cm}^2$', '$96\\text{ cm}^2$', '$156\\text{ cm}^2$'],
            'answer': 2,
            'solution': 'Ta có $S_{xq} = 2a \\cdot d = 2 \\cdot 6 \\cdot 5 = 60\\text{ cm}^2$ và '
                        '$S_{\\text{đáy}} = 6^2 = 36\\text{ cm}^2$. Vậy $S_{tp} = 60 + 36 = 96\\text{ '
                        'cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 39: Hình chóp tứ giác đều**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Mô tả được đỉnh, mặt đáy (hình vuông), mặt bên (tam giác cân), đường cao và trung '
                        'đoạn của hình chóp tứ giác đều. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Mô tả được đỉnh, mặt đáy (hình vuông), mặt bên (tam giác '
                        'cân), đường cao và trung đoạn của hình chóp tứ giác đều.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Mô tả được đỉnh, mặt đáy (hình '
                        'vuông), mặt bên (tam giác cân), đường cao và trung đoạn của hình chóp tứ giác đều.',
                        'Mô tả được đỉnh, mặt đáy (hình vuông), mặt bên (tam giác cân), đường cao và trung '
                        'đoạn của hình chóp tứ giác đều.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 39: Hình chóp tứ giác đều: Mô tả được đỉnh, mặt đáy '
                        '(hình vuông), mặt bên (tam giác cân), đường cao và trung đoạn của hình chóp tứ giác '
                        'đều.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy $a = 6\\text{ cm}$ và chiều cao $SO = '
                 '4\\text{ cm}$. Xét các khẳng định sau:',
            'statements': ['Diện tích mặt đáy $ABCD$ bằng $36\\text{ cm}^2$.',
                           'Thể tích của hình chóp $S.ABCD$ bằng $48\\text{ cm}^3$.',
                           'Độ dài trung đoạn $SI$ của hình chóp bằng $\\sqrt{4^2 + 3^2} = 5\\text{ cm}$.',
                           'Hình chóp tứ giác đều $S.ABCD$ có tất cả $4$ cạnh.'],
            'answer': [True, True, True, False],
            'solution': 'a), b), c) Đúng ($V = \\dfrac{1}{3} \\cdot 36 \\cdot 4 = 48\\text{ cm}^3$). d) Sai '
                        'vì hình chóp tứ giác đều có $8$ cạnh ($4$ cạnh đáy và $4$ cạnh bên).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 39: Hình chóp tứ giác '
                 'đều**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Mô tả được đỉnh, mặt đáy (hình vuông), '
                           'mặt bên (tam giác cân), đường cao và trung đoạn của hình chóp tứ giác đều.',
                           'Trong **Bài 39: Hình chóp tứ giác đều**, quy tắc/công thức **Diện tích xung '
                           'quanh** được viết là: $S_{xq} = p \\cdot d = 2a \\cdot d$.',
                           'Nếu áp dụng sai dấu/phép tính thành $S_{xq} = p : d = 2a \\cdot d$ thì kết quả '
                           'của **Diện tích xung quanh** trong **Bài 39: Hình chóp tứ giác đều** vẫn không '
                           'thay đổi.',
                           'Xét ví dụ của bài: “Một mái che giếng trời có dạng hình chóp tứ giác đều với '
                           'cạnh đáy $a = 2\\text{ m}$ và chiều cao $h = 1,2\\text{ m}$. Tính thể tích '
                           'phần...”, kết quả giải đúng là: - Diện tích đáy hình vuông là: $S_{\\text{đáy}} '
                           '= 2^2 = 4\\text{ (m}^2\\text{)}$. - Thể tích phần không gian bên trong là...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 39: Hình chóp tứ giác đều. b) **Đúng** '
                        'theo công thức **Diện tích xung quanh** ($S_{xq} = p \\cdot d = 2a \\cdot d$). c) '
                        '**Sai** vì công thức đúng của **Diện tích xung quanh** phải là $S_{xq} = p \\cdot d '
                        '= 2a \\cdot d$ chứ không phải $S_{xq} = p : d = 2a \\cdot d$. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 39: Hình chóp tứ giác đều** để giải bài toán sau: '
                 'Một mái che giếng trời có dạng hình chóp tứ giác đều với cạnh đáy $a = 2\\text{ m}$ và '
                 'chiều cao $h = 1,2\\text{ m}$. Tính thể tích phần không gian bên trong mái che và độ dài '
                 'trung đoạn của mái che. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['- Diện tích đáy hình vuông là: $S_{\\text{đáy}} = 2^2 = 4\\text{ (m}^2\\text{)}$. - '
                        'Thể tích phần không gian bên trong là...',
                        '- Diện tích đáy hình vuông là: $S_{\\text{đáy}} = 2^2 = 4\\text{ (m}^2\\text{)}$. + '
                        'Thể tích phần không gian bên trong là...',
                        '- Diện tích đáy hình vuông là: $S_{\\text{đáy}} = 2^2 = 4\\text{ (m}^1\\text{)}$. - '
                        'Thể tích phần không gian bên trong là...',
                        '- Diện tích đáy hình vuông là: $S_{\\text{đáy}} = 4^2 = 4\\text{ (m}^2\\text{)}$. - '
                        'Thể tích phần không gian bên trong là...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 39: Hình chóp tứ giác đều: - Diện tích đáy hình vuông '
                        'là: $S_{\\text{đáy}} = 2^2 = 4\\text{ (m}^2\\text{)}$.\n'
                        '- Thể tích phần không gian bên trong là: $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot '
                        'h = \\dfrac{1}{3} \\cdot 4 \\cdot 1,2 = 1,6\\text{ (m}^3\\text{)}$.\n'
                        '- Độ dài trung đoạn là: $d = \\sqrt{h^2 + \\left(\\dfrac{a}{2}\\right)^2} = '
                        '\\sqrt{1,2^2 + 1^2} = \\sqrt{2,44} \\approx 1,56\\text{ (m)}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chóp tứ giác đều có độ dài cạnh đáy bằng $10\\text{ cm}$ và chiều cao bằng '
                 '$12\\text{ cm}$. Tính thể tích của hình chóp tứ giác đều đó (đơn vị $\\text{cm}^3$).',
            'answer': ['400'],
            'unit': None,
            'solution': 'Diện tích đáy là $S_{\\text{đáy}} = 10^2 = 100\\text{ (cm}^2\\text{)}$. Thể tích là '
                        '$V = \\dfrac{1}{3} \\cdot 100 \\cdot 12 = 400\\text{ (cm}^3\\text{)}$.',
            'alt': None,
            'note': None}]}]


# Đồng bộ game_type, game_title, game_description và đảm bảo 4 phương án trắc nghiệm phân biệt
from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("math", 8, _l)
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
