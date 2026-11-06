"""Dữ liệu bài học SGK Toán Lớp 9 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 9 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 9

LESSONS = [{'topic': 'l9-ch01-he-phuong-trinh',
  'context_title': 'Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn',
  'context': 'Chương I · SGK Toán 9: Phương trình và hệ hai phương trình bậc nhất hai ẩn.',
  'title': 'Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn',
  'icon': '📈',
  'description': 'Nhận biết phương trình, hệ hai phương trình bậc nhất hai ẩn và nghiệm của hệ.',
  'requirements': ['Nhận biết được phương trình bậc nhất hai ẩn $ax + by = c$ ($a \\neq 0$ hoặc $b \\neq 0$) '
                   'và nghiệm của nó.',
                   'Nhận biết được hệ hai phương trình bậc nhất hai ẩn và nghiệm của hệ.',
                   'Biểu diễn được tập nghiệm của phương trình bậc nhất hai ẩn trên mặt phẳng tọa độ.'],
  'definition': 'Phương trình bậc nhất hai ẩn $x$ và $y$ là hệ thức dạng $ax + by = c$, trong đó $a, b, c$ '
                'là các số đã biết ($a \\neq 0$ hoặc $b \\neq 0$). Cặp số $(x_0; y_0)$ thỏa mãn $ax_0 + by_0 '
                '= c$ được gọi là một nghiệm của phương trình.',
  'theory': '1. Mỗi phương trình bậc nhất hai ẩn $ax + by = c$ luôn có vô số nghiệm. Trong mặt phẳng tọa độ '
            '$Oxy$, tập hợp các điểm biểu diễn các nghiệm của phương trình $ax + by = c$ là một đường '
            'thẳng.\n'
            '2. Hệ hai phương trình bậc nhất hai ẩn có dạng $\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + '
            'b_2y = c_2 \\end{cases}$.\n'
            '3. Nếu hai phương trình ấy có nghiệm chung $(x_0; y_0)$ thì $(x_0; y_0)$ được gọi là một nghiệm '
            'của hệ phương trình.',
  'formulas': [{'category': 'Phương trình và hệ phương trình bậc nhất hai ẩn',
                'items': [{'name': 'Phương trình bậc nhất hai ẩn',
                           'formula': '$ax + by = c$ ($a^2 + b^2 \\neq 0$)',
                           'note': 'Tập nghiệm biểu diễn bởi một đường thẳng'},
                          {'name': 'Hệ hai phương trình bậc nhất hai ẩn',
                           'formula': '$\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + b_2y = c_2 '
                                      '\\end{cases}$',
                           'note': 'Nghiệm của hệ là giao điểm hai đường thẳng'}]}],
  'example': 'Kiểm tra xem cặp số $(2; -1)$ có phải là nghiệm của hệ phương trình $\\begin{cases} 2x - y = 5 '
             '\\\\ x + 3y = -1 \\end{cases}$ hay không.',
  'example_answer': 'Thay $x = 2, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 + 1 = 5$ (thỏa '
                    'mãn).\n'
                    'Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - 3 = -1$ (thỏa '
                    'mãn).\n'
                    'Vậy cặp số $(2; -1)$ là nghiệm của hệ phương trình đã cho.',
  'real_life': 'Biểu diễn mối quan hệ giữa số lượng hai loại mặt hàng mua được với tổng số tiền cố định '
               'trong bài toán chi tiêu gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình nào sau đây là phương trình bậc nhất hai ẩn $x, y$?',
            'options': ['$2x - 3y = 5$', '$0x + 0y = 1$', '$x^2 + y = 4$', '$2xy - y = 3$'],
            'answer': 0,
            'solution': 'Phương trình bậc nhất hai ẩn có dạng $ax + by = c$ với $a \\neq 0$ hoặc $b \\neq '
                        '0$, nên $2x - 3y = 5$ thỏa mãn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cặp số nào sau đây là một nghiệm của phương trình $3x - y = 2$?',
            'options': ['$(1; -1)$', '$(1; 1)$', '$(0; 2)$', '$(2; 0)$'],
            'answer': 1,
            'solution': 'Thay $x = 1, y = 1$ vào phương trình ta được $3 \\cdot 1 - 1 = 2$ (đúng).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Phương trình bậc nhất hai ẩn**?',
            'options': ['$ax - by = c$ ($a^2 + b^2 \\neq 0$)',
                        '$ax + by = c$ ($a^2 + b^2 \\neq 1$)',
                        '$ax + by = c$ ($a^2 + b^2 \\neq 0$)',
                        '$ax + by = c$ ($a^4 + b^2 \\neq 0$)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Khái niệm phương trình và hệ hai phương trình '
                        'bậc nhất hai ẩn, **Phương trình bậc nhất hai ẩn** được xác định bởi: $ax + by = c$ '
                        '($a^2 + b^2 \\neq 0$). (Tập nghiệm biểu diễn bởi một đường thẳng)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Hệ hai phương trình bậc nhất hai ẩn**?',
            'options': ['$\\begin{cases} a_1x - b_1y = c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$',
                        'Đảo ngược vế của quy tắc: $\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + b_2y = c_2 '
                        '\\end{cases}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\begin{cases} a_1x + b_1y = '
                        'c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$',
                        '$\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$'],
            'answer': 3,
            'solution': 'Trong Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn, **Hệ '
                        'hai phương trình bậc nhất hai ẩn** có công thức/quy tắc là: $\\begin{cases} a_1x + '
                        'b_1y = c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cặp số $(1; -2)$ là nghiệm của hệ phương trình nào dưới đây?',
            'options': ['$\\begin{cases} 2x + y = 0 \\\\ x - y = 3 \\end{cases}$',
                        '$\\begin{cases} 2x - y = 0 \\\\ x + y = 3 \\end{cases}$',
                        '$\\begin{cases} x + 2y = 3 \\\\ 2x - y = 4 \\end{cases}$',
                        '$\\begin{cases} x - y = -1 \\\\ 2x + y = 0 \\end{cases}$'],
            'answer': 0,
            'solution': 'Thay $x = 1, y = -2$ vào hệ $\\begin{cases} 2x + y = 0 \\\\ x - y = 3 \\end{cases}$ '
                        'ta có $2(1) + (-2) = 0$ và $1 - (-2) = 3$ đều đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất '
                 'hai ẩn**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được phương trình bậc nhất hai ẩn $ax - by = c$ ($a \\neq 0$ hoặc $b '
                        '\\neq 0$) và nghiệm của nó.',
                        'Nhận biết được phương trình bậc nhất hai ẩn $ax + by = c$ ($a \\neq 0$ hoặc $b '
                        '\\neq 0$) và nghiệm của nó.',
                        'Nhận biết được phương trình bậc nhất hai ẩn $ax + by = c$ ($a \\neq 0$ hoặc $b '
                        '\\neq 1$) và nghiệm của nó.',
                        'Nhận biết được phương trình bậc nhất hai ẩn $ax + by = c$ ($a \\neq 2$ hoặc $b '
                        '\\neq 0$) và nghiệm của nó.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Khái niệm phương trình và hệ hai phương trình bậc '
                        'nhất hai ẩn: Nhận biết được phương trình bậc nhất hai ẩn $ax + by = c$ ($a \\neq 0$ '
                        'hoặc $b \\neq 0$) và nghiệm của nó.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình bậc nhất hai ẩn $2x + y = 4$ (1).',
            'statements': ['Cặp số $(1; 2)$ là một nghiệm của phương trình (1).',
                           'Phương trình (1) có duy nhất một nghiệm.',
                           'Tất cả các nghiệm của phương trình (1) được viết dưới dạng $(x; 4 - 2x)$ với $x '
                           '\\in \\mathbb{R}$.',
                           'Đường thẳng biểu diễn tập nghiệm của phương trình (1) đi qua gốc tọa độ $O(0; '
                           '0)$.'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng vì $2(1) + 2 = 4$. b) Sai vì phương trình bậc nhất hai ẩn có vô số nghiệm. '
                        'c) Đúng vì rút $y = 4 - 2x$. d) Sai vì $2(0) + 0 = 0 \\neq 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 1: Khái niệm phương trình '
                 'và hệ hai phương trình bậc nhất hai ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được phương trình bậc nhất hai '
                           'ẩn $ax + by = c$ ($a \\neq 0$ hoặc $b \\neq 0$) và nghiệm của nó.',
                           'Trong **Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn**, '
                           'quy tắc/công thức **Phương trình bậc nhất hai ẩn** được viết là: $ax + by = c$ '
                           '($a^2 + b^2 \\neq 0$).',
                           'Nếu áp dụng sai dấu/phép tính thành $ax - by = c$ ($a^2 + b^2 \\neq 0$) thì kết '
                           'quả của **Phương trình bậc nhất hai ẩn** trong **Bài 1: Khái niệm phương trình '
                           'và hệ hai phương trình bậc nhất hai ẩn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Kiểm tra xem cặp số $(2; -1)$ có phải là nghiệm của hệ '
                           'phương trình $\\begin{cases} 2x - y = 5 \\\\ x + 3y = -1 \\end{cases}$ hay '
                           'không.”, kết quả giải đúng là: Thay $x = 2, y = -1$ vào phương trình thứ nhất: '
                           '$2 \\cdot 2 - (-1) = 4 + 1 = 5$ (thỏa mãn). Thay $x = 2, y = -1$ vào phương '
                           'trình thứ ha...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 1: Khái niệm phương trình và hệ hai phương '
                        'trình bậc nhất hai ẩn. b) **Đúng** theo công thức **Phương trình bậc nhất hai ẩn** '
                        '($ax + by = c$ ($a^2 + b^2 \\neq 0$)). c) **Sai** vì công thức đúng của **Phương '
                        'trình bậc nhất hai ẩn** phải là $ax + by = c$ ($a^2 + b^2 \\neq 0$) chứ không phải '
                        '$ax - by = c$ ($a^2 + b^2 \\neq 0$). d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Khái niệm phương trình và hệ hai phương trình '
                 'bậc nhất hai ẩn** để giải bài toán sau: Kiểm tra xem cặp số $(2; -1)$ có phải là nghiệm '
                 'của hệ phương trình $\\begin{cases} 2x - y = 5 \\\\ x + 3y = -1 \\end{cases}$ hay không. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thay $x = 2, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 - 1 = 5$ '
                        '(thỏa mãn). Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - '
                        '3 = -1$...',
                        'Thay $x = 2, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 + 1 = 5$ '
                        '(thỏa mãn). Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - '
                        '3 = -2$...',
                        'Thay $x = 2, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 + 1 = 5$ '
                        '(thỏa mãn). Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - '
                        '3 = -1$...',
                        'Thay $x = 4, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 + 1 = 5$ '
                        '(thỏa mãn). Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - '
                        '3 = -1$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Khái niệm phương trình và hệ hai phương trình bậc '
                        'nhất hai ẩn: Thay $x = 2, y = -1$ vào phương trình thứ nhất: $2 \\cdot 2 - (-1) = 4 '
                        '+ 1 = 5$ (thỏa mãn).\n'
                        'Thay $x = 2, y = -1$ vào phương trình thứ hai: $2 + 3 \\cdot (-1) = 2 - 3 = -1$ '
                        '(thỏa mãn).\n'
                        'Vậy cặp số $(2; -1)$ là nghiệm của hệ phương trình đã cho.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm giá trị của tham số $m$ để cặp số $(2; -1)$ là nghiệm của phương trình $mx - 3y = 7$.',
            'answer': ['2'],
            'unit': None,
            'solution': 'Thay $x = 2, y = -1$ vào phương trình: $m \\cdot 2 - 3 \\cdot (-1) = 7 \\Rightarrow '
                        '2m + 3 = 7 \\Rightarrow m = 2$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch01-he-phuong-trinh',
  'context_title': 'Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn',
  'context': 'Chương I · SGK Toán 9: Phương trình và hệ hai phương trình bậc nhất hai ẩn.',
  'title': 'Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn',
  'icon': '🧮',
  'description': 'Giải hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế và phương pháp cộng đại số.',
  'requirements': ['Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế.',
                   'Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp cộng đại số.',
                   'Sử dụng được máy tính cầm tay để tìm nghiệm của hệ hai phương trình bậc nhất hai ẩn.'],
  'definition': 'Giải hệ phương trình là tìm tất cả các nghiệm (tập nghiệm) của hệ phương trình đó. Hai '
                'phương pháp đại số thông dụng là phương pháp thế và phương pháp cộng đại số.',
  'theory': '1. Phương pháp thế: Biểu diễn một ẩn theo ẩn kia từ một phương trình rồi thế vào phương trình '
            'còn lại để được phương trình một ẩn.\n'
            '2. Phương pháp cộng đại số: Nhân hai vế của mỗi phương trình với số thích hợp (nếu cần) sao cho '
            'hệ số của một ẩn bằng nhau hoặc đối nhau, rồi cộng hay trừ từng vế hai phương trình để khử bớt '
            'một ẩn.\n'
            '3. Hệ hai phương trình bậc nhất hai ẩn có thể có nghiệm duy nhất, vô nghiệm hoặc vô số nghiệm.',
  'formulas': [{'category': 'Các quy tắc biến đổi hệ phương trình',
                'items': [{'name': 'Phương pháp thế',
                           'formula': 'Từ $ax + by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq 0$)',
                           'note': 'Thế biểu thức của $y$ vào phương trình còn lại'},
                          {'name': 'Phương pháp cộng đại số',
                           'formula': 'Cộng hoặc trừ từng vế hai phương trình',
                           'note': 'Triệt tiêu một ẩn để đưa về phương trình bậc nhất một ẩn'}]}],
  'example': 'Giải hệ phương trình $\\begin{cases} 2x + y = 5 \\\\ 3x - y = 5 \\end{cases}$ bằng phương pháp '
             'cộng đại số.',
  'example_answer': 'Cộng từng vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$.\n'
                    'Thay $x = 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                    '1$.\n'
                    'Vậy hệ phương trình có nghiệm duy nhất là $(2; 1)$.',
  'real_life': 'Tính toán nhanh giá tiền của từng món hàng khi biết tổng hóa đơn của hai lần mua khác nhau.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi cộng từng vế hai phương trình của hệ $\\begin{cases} x + 2y = 4 \\\\ 3x - 2y = 8 '
                 '\\end{cases}$, ta thu được phương trình nào?',
            'options': ['$2x = 4$', '$4x = 12$', '$4x + 4y = 12$', '$-2x = -4$'],
            'answer': 1,
            'solution': 'Cộng từng vế: $(x + 3x) + (2y - 2y) = 4 + 8 \\Rightarrow 4x = 12$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của hệ phương trình $\\begin{cases} x + y = 5 \\\\ x - y = 1 \\end{cases}$ là:',
            'options': ['$(2; 3)$', '$(4; 1)$', '$(3; 2)$', '$(1; 4)$'],
            'answer': 2,
            'solution': 'Cộng hai vế được $2x = 6 \\Rightarrow x = 3$, suy ra $y = 5 - 3 = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Phương pháp thế**?',
            'options': ['Từ $ax - by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq 0$)',
                        'Từ $ax + by = c \\Rightarrow y = \\dfrac{b}{c - ax}$ ($b \\neq 0$)',
                        'Từ $ax + by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq 2$)',
                        'Từ $ax + by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq 0$)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn, '
                        '**Phương pháp thế** được xác định bởi: Từ $ax + by = c \\Rightarrow y = \\dfrac{c - '
                        'ax}{b}$ ($b \\neq 0$). (Thế biểu thức của $y$ vào phương trình còn lại)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Phương pháp cộng đại số**?',
            'options': ['Cộng hoặc trừ từng vế hai phương trình',
                        'Cộng hoặc trừ từng vế hai phương trình (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Cộng hoặc trừ từng vế hai phương trình',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Cộng hoặc trừ từng vế hai '
                        'phương trình'],
            'answer': 0,
            'solution': 'Trong Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn, **Phương pháp cộng đại số** '
                        'có công thức/quy tắc là: Cộng hoặc trừ từng vế hai phương trình.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hệ phương trình $\\begin{cases} 2x - y = 3 \\\\ -4x + 2y = -6 \\end{cases}$ có bao nhiêu '
                 'nghiệm?',
            'options': ['Vô nghiệm', 'Vô số nghiệm', 'Một nghiệm duy nhất', 'Hai nghiệm phân biệt'],
            'answer': 1,
            'solution': 'Nhân hai vế phương trình thứ nhất với $-2$ ta được phương trình thứ hai, nên hệ có '
                        'vô số nghiệm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương '
                        'pháp thế.',
                        'Giải được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giải được hệ hai phương trình '
                        'bậc nhất hai ẩn bằng phương pháp thế.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn: Giải '
                        'được hệ hai phương trình bậc nhất hai ẩn bằng phương pháp thế.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hệ phương trình $\\begin{cases} 3x + 2y = 8 \\\\ x - y = 1 \\end{cases}$.',
            'statements': ['Từ phương trình thứ hai của hệ, ta có thể biểu diễn $x = y + 1$.',
                           'Thế $x = y + 1$ vào phương trình thứ nhất, ta được phương trình $5y + 3 = 8$.',
                           'Nghiệm của hệ phương trình đã cho là $(2; 1)$.',
                           'Tổng $x_0 + y_0$ của nghiệm $(x_0; y_0)$ bằng $4$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $x - y = 1 \\Rightarrow x = y + 1$. b) Đúng vì $3(y + 1) + 2y = 8 '
                        '\\Rightarrow 5y + 3 = 8$. c) Đúng vì $y = 1 \\Rightarrow x = 2$. d) Sai vì $x_0 + '
                        'y_0 = 2 + 1 = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 2: Giải hệ hai phương trình '
                 'bậc nhất hai ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải được hệ hai phương trình bậc nhất '
                           'hai ẩn bằng phương pháp thế.',
                           'Trong **Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn**, quy tắc/công thức '
                           '**Phương pháp thế** được viết là: Từ $ax + by = c \\Rightarrow y = \\dfrac{c - '
                           'ax}{b}$ ($b \\neq 0$).',
                           'Nếu áp dụng sai dấu/phép tính thành Từ $ax - by = c \\Rightarrow y = \\dfrac{c - '
                           'ax}{b}$ ($b \\neq 0$) thì kết quả của **Phương pháp thế** trong **Bài 2: Giải hệ '
                           'hai phương trình bậc nhất hai ẩn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Giải hệ phương trình $\\begin{cases} 2x + y = 5 \\\\ 3x - y '
                           '= 5 \\end{cases}$ bằng phương pháp cộng đại số.”, kết quả giải đúng là: Cộng '
                           'từng vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$. Thay $x '
                           '= 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                           '1$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 2: Giải hệ hai phương trình bậc nhất hai '
                        'ẩn. b) **Đúng** theo công thức **Phương pháp thế** (Từ $ax + by = c \\Rightarrow y '
                        '= \\dfrac{c - ax}{b}$ ($b \\neq 0$)). c) **Sai** vì công thức đúng của **Phương '
                        'pháp thế** phải là Từ $ax + by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq '
                        '0$) chứ không phải Từ $ax - by = c \\Rightarrow y = \\dfrac{c - ax}{b}$ ($b \\neq '
                        '0$). d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn** để '
                 'giải bài toán sau: Giải hệ phương trình $\\begin{cases} 2x + y = 5 \\\\ 3x - y = 5 '
                 '\\end{cases}$ bằng phương pháp cộng đại số. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Cộng từng vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$. Thay '
                        '$x = 2$ vào phương trình $2x - y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                        '1$...',
                        'Cộng từng vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$. Thay '
                        '$x = 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                        '2$...',
                        'Cộng từng vế hai phương trình của hệ, ta được: $5x = 20 \\Rightarrow x = 2$. Thay '
                        '$x = 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                        '1$...',
                        'Cộng từng vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$. Thay '
                        '$x = 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow y = '
                        '1$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Giải hệ hai phương trình bậc nhất hai ẩn: Cộng từng '
                        'vế hai phương trình của hệ, ta được: $5x = 10 \\Rightarrow x = 2$.\n'
                        'Thay $x = 2$ vào phương trình $2x + y = 5$, ta có: $2 \\cdot 2 + y = 5 \\Rightarrow '
                        'y = 1$.\n'
                        'Vậy hệ phương trình có nghiệm duy nhất là $(2; 1)$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Biết hệ phương trình $\\begin{cases} 2x + 3y = 13 \\\\ x - 2y = -4 \\end{cases}$ có nghiệm '
                 'duy nhất $(x_0; y_0)$. Tính tích $x_0 \\cdot y_0$.',
            'answer': ['6'],
            'unit': None,
            'solution': 'Từ phương trình thứ hai: $x = 2y - 4$. Thế vào phương trình đầu: $2(2y - 4) + 3y = '
                        '13 \\Rightarrow 7y = 21 \\Rightarrow y_0 = 3 \\Rightarrow x_0 = 2$. Tích $x_0 '
                        '\\cdot y_0 = 2 \\cdot 3 = 6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch01-he-phuong-trinh',
  'context_title': 'Chương I: Phương trình và hệ hai phương trình bậc nhất hai ẩn',
  'context': 'Chương I · SGK Toán 9: Phương trình và hệ hai phương trình bậc nhất hai ẩn.',
  'title': 'Bài 3: Giải bài toán bằng cách lập hệ phương trình',
  'icon': '📝',
  'description': 'Vận dụng hệ hai phương trình bậc nhất hai ẩn để giải các bài toán thực tiễn.',
  'requirements': ['Nắm vững 3 bước giải bài toán bằng cách lập hệ phương trình.',
                   'Giải quyết được các bài toán thực tiễn (chuyển động, năng suất, phần trăm, hóa học) gắn '
                   'với hệ hai phương trình bậc nhất hai ẩn.',
                   'Vận dụng kiến thức của **Bài 3: Giải bài toán bằng cách lập hệ phương trình** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giải bài toán bằng cách lập hệ phương trình là quá trình chuyển bài toán thực tế sang mô '
                'hình hệ hai phương trình bậc nhất hai ẩn, giải hệ rồi đối chiếu điều kiện để kết luận.',
  'theory': 'Các bước giải bài toán bằng cách lập hệ phương trình:\n'
            '- Bước 1 (Lập hệ phương trình): Chọn hai ẩn số và đặt điều kiện thích hợp cho chúng; biểu diễn '
            'các đại lượng chưa biết theo ẩn và các đại lượng đã biết; lập hai phương trình biểu thị mối '
            'quan hệ giữa các đại lượng.\n'
            '- Bước 2 (Giải hệ phương trình): Giải hệ hai phương trình vừa nhận được.\n'
            '- Bước 3 (Trả lời): Kiểm tra xem nghiệm tìm được có thỏa mãn điều kiện của ẩn hay không, rồi '
            'kết luận.',
  'formulas': [{'category': 'Các mối quan hệ đại lượng thường gặp',
                'items': [{'name': 'Bài toán chuyển động',
                           'formula': '$s = v \\cdot t$',
                           'note': 'Quãng đường = Vận tốc $\\times$ Thời gian'},
                          {'name': 'Bài toán làm chung công việc',
                           'formula': '$\\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{T}$',
                           'note': '$x, y$ là thời gian làm riêng hoàn thành công việc'}]}],
  'example': 'Tổng của hai số bằng $59$. Hai lần số thứ nhất bé hơn ba lần số thứ hai là $7$. Tìm hai số đó.',
  'example_answer': 'Gọi số thứ nhất là $x$ và số thứ hai là $y$.\n'
                    'Theo đề bài, ta có hệ phương trình: $\\begin{cases} x + y = 59 \\\\ 3y - 2x = 7 '
                    '\\end{cases} \\Leftrightarrow \\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 7 '
                    '\\end{cases}$.\n'
                    'Cộng từng vế hai phương trình được $5y = 125 \\Rightarrow y = 25$, suy ra $x = 59 - 25 '
                    '= 34$.\n'
                    'Vậy hai số cần tìm là $34$ và $25$.',
  'real_life': 'Tính vận tốc riêng của ca nô và vận tốc dòng nước khi xuôi dòng và ngược dòng trên sông.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu gọi chữ số hàng chục là $x$ và chữ số hàng đơn vị là $y$ ($x \\in \\mathbb{N}^*, y '
                 '\\in \\mathbb{N}, x \\le 9, y \\le 9$) thì số tự nhiên có hai chữ số $\\overline{xy}$ được '
                 'biểu diễn là:',
            'options': ['$x + y$', '$10y + x$', '$10x + y$', '$x \\cdot y$'],
            'answer': 2,
            'solution': 'Giá trị của số tự nhiên có hai chữ số $\\overline{xy}$ là $10x + y$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một ca nô có vận tốc riêng là $x$ (km/h) chạy trên sông có vận tốc dòng nước là $y$ (km/h) '
                 '($x > y > 0$). Vận tốc của ca nô khi đi ngược dòng là:',
            'options': ['$x + y$ (km/h)', '$y - x$ (km/h)', '$\\dfrac{x}{y}$ (km/h)', '$x - y$ (km/h)'],
            'answer': 3,
            'solution': 'Vận tốc ngược dòng bằng vận tốc thực trừ đi vận tốc dòng nước: $x - y$ (km/h).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Giải bài toán bằng cách lập hệ phương trình**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Bài toán chuyển động**?',
            'options': ['$s = v \\cdot t$',
                        '$s = v : t$',
                        'Đảo ngược vế của quy tắc: $s = v \\cdot t$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $s = v \\cdot t$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Giải bài toán bằng cách lập hệ phương trình, '
                        '**Bài toán chuyển động** được xác định bởi: $s = v \\cdot t$. (Quãng đường = Vận '
                        'tốc $\\times$ Thời gian)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Giải bài toán bằng cách lập hệ phương trình**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Bài toán làm chung công việc**?',
            'options': ['$\\dfrac{1}{x} - \\dfrac{1}{y} = \\dfrac{1}{T}$',
                        '$\\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{T}$',
                        '$\\dfrac{x}{1} + \\dfrac{1}{y} = \\dfrac{1}{T}$',
                        '$\\dfrac{2}{x} + \\dfrac{1}{y} = \\dfrac{1}{T}$'],
            'answer': 1,
            'solution': 'Trong Bài 3: Giải bài toán bằng cách lập hệ phương trình, **Bài toán làm chung công '
                        'việc** có công thức/quy tắc là: $\\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{T}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hai người thợ cùng làm một công việc trong $6$ giờ thì xong. Nếu gọi $x, y$ (giờ) lần lượt '
                 'là thời gian mỗi người làm một mình xong công việc ($x, y > 6$), phương trình biểu thị '
                 'năng suất làm chung trong 1 giờ là:',
            'options': ['$x + y = 6$',
                        '$\\dfrac{1}{x} + \\dfrac{1}{y} = 6$',
                        '$\\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{6}$',
                        '$6x + 6y = 1$'],
            'answer': 2,
            'solution': 'Trong 1 giờ, người thứ nhất làm được $\\dfrac{1}{x}$ công việc, người thứ hai làm '
                        'được $\\dfrac{1}{y}$ công việc, cả hai làm được $\\dfrac{1}{6}$ công việc.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Giải bài toán bằng cách lập hệ phương trình**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Nắm vững 4 bước giải bài toán bằng cách lập hệ phương trình.',
                        'Nắm vững 2 bước giải bài toán bằng cách lập hệ phương trình.',
                        'Nắm vững 6 bước giải bài toán bằng cách lập hệ phương trình.',
                        'Nắm vững 3 bước giải bài toán bằng cách lập hệ phương trình.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Giải bài toán bằng cách lập hệ phương trình: Nắm '
                        'vững 3 bước giải bài toán bằng cách lập hệ phương trình.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một mảnh vườn hình chữ nhật có chu vi $34$ m. Nếu tăng chiều dài thêm $3$ m và tăng chiều '
                 'rộng thêm $2$ m thì diện tích tăng thêm $45\\text{ m}^2$. Gọi chiều dài và chiều rộng ban '
                 'đầu của mảnh vườn lần lượt là $x, y$ (m) ($x > y > 0$).',
            'statements': ['Phương trình biểu thị chu vi mảnh vườn ban đầu là $x + y = 34$.',
                           'Diện tích mảnh vườn sau khi tăng kích thước là $(x + 3)(y + 2)$ ($\\text{m}^2$).',
                           'Hệ phương trình lập được là $\\begin{cases} x + y = 17 \\\\ 2x + 3y = 39 '
                           '\\end{cases}$.',
                           'Chiều dài ban đầu của mảnh vườn là $12$ m và chiều rộng ban đầu là $5$ m.'],
            'answer': [False, True, True, True],
            'solution': 'a) Sai vì nửa chu vi là $x + y = 17$. b) Đúng. c) Đúng vì $(x + 3)(y + 2) - xy = 45 '
                        '\\Rightarrow 2x + 3y = 39$. d) Đúng vì giải hệ được $x = 12, y = 5$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 3: Giải bài toán bằng cách '
                 'lập hệ phương trình**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nắm vững 3 bước giải bài toán bằng cách '
                           'lập hệ phương trình.',
                           'Trong **Bài 3: Giải bài toán bằng cách lập hệ phương trình**, quy tắc/công thức '
                           '**Bài toán chuyển động** được viết là: $s = v \\cdot t$.',
                           'Nếu áp dụng sai dấu/phép tính thành $s = v : t$ thì kết quả của **Bài toán '
                           'chuyển động** trong **Bài 3: Giải bài toán bằng cách lập hệ phương trình** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Tổng của hai số bằng $59$. Hai lần số thứ nhất bé hơn ba lần '
                           'số thứ hai là $7$. Tìm hai số đó.”, kết quả giải đúng là: Gọi số thứ nhất là $x$ '
                           'và số thứ hai là $y$. Theo đề bài, ta có hệ phương trình...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 3: Giải bài toán bằng cách lập hệ phương '
                        'trình. b) **Đúng** theo công thức **Bài toán chuyển động** ($s = v \\cdot t$). c) '
                        '**Sai** vì công thức đúng của **Bài toán chuyển động** phải là $s = v \\cdot t$ chứ '
                        'không phải $s = v : t$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Giải bài toán bằng cách lập hệ phương trình** để '
                 'giải bài toán sau: Tổng của hai số bằng $59$. Hai lần số thứ nhất bé hơn ba lần số thứ hai '
                 'là $7$. Tìm hai số đó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Gọi số thứ nhất là $x$ và số thứ hai là $y$. Theo đề bài, ta có hệ phương trình: '
                        '$\\begin{cases} x + y = 59 \\\\ 3y - 2x = 7 \\end{cases} \\Leftrightarrow '
                        '\\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 7 \\end{cases}$...',
                        'Gọi số thứ nhất là $x$ và số thứ hai là $y$. Theo đề bài, ta có hệ phương trình: '
                        '$\\begin{cases} x - y = 59 \\\\ 3y - 2x = 7 \\end{cases} \\Leftrightarrow '
                        '\\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 7 \\end{cases}$...',
                        'Gọi số thứ nhất là $x$ và số thứ hai là $y$. Theo đề bài, ta có hệ phương trình: '
                        '$\\begin{cases} x + y = 59 \\\\ 3y - 2x = 7 \\end{cases} \\Leftrightarrow '
                        '\\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 6 \\end{cases}$...',
                        'Gọi số thứ nhất là $x$ và số thứ hai là $y$. Theo đề bài, ta có hệ phương trình: '
                        '$\\begin{cases} x + y = 61 \\\\ 3y - 2x = 7 \\end{cases} \\Leftrightarrow '
                        '\\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 7 \\end{cases}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Giải bài toán bằng cách lập hệ phương trình: Gọi số '
                        'thứ nhất là $x$ và số thứ hai là $y$.\n'
                        'Theo đề bài, ta có hệ phương trình: $\\begin{cases} x + y = 59 \\\\ 3y - 2x = 7 '
                        '\\end{cases} \\Leftrightarrow \\begin{cases} 2x + 2y = 118 \\\\ -2x + 3y = 7 '
                        '\\end{cases}$.\n'
                        'Cộng từng vế hai phương trình được $5y = 125 \\Rightarrow y = 25$, suy ra $x = 59 - '
                        '25 = 34$.\n'
                        'Vậy hai số cần tìm là $34$ và $25$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Vừa gà vừa chó bó lại cho tròn, $36$ con đủ $100$ chân chẵn. Hỏi có bao nhiêu con chó?',
            'answer': ['14'],
            'unit': None,
            'solution': 'Gọi số gà là $x$, số chó là $y$ ($x, y \\in \\mathbb{N}^*$). Ta có hệ '
                        '$\\begin{cases} x + y = 36 \\\\ 2x + 4y = 100 \\end{cases} \\Rightarrow y = 14, x = '
                        '22$. Vậy có $14$ con chó.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch02-bat-phuong-trinh',
  'context_title': 'Chương II: Phương trình và bất phương trình bậc nhất một ẩn',
  'context': 'Chương II · SGK Toán 9: Phương trình và bất phương trình bậc nhất một ẩn.',
  'title': 'Bài 4: Phương trình quy về phương trình bậc nhất một ẩn',
  'icon': '🔗',
  'description': 'Giải phương trình tích và phương trình chứa ẩn ở mẫu quy về phương trình bậc nhất một ẩn.',
  'requirements': ['Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 0$.',
                   'Tìm được điều kiện xác định và giải được phương trình chứa ẩn ở mẫu quy về phương trình '
                   'bậc nhất.',
                   'Vận dụng kiến thức của **Bài 4: Phương trình quy về phương trình bậc nhất một ẩn** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Phương trình tích là phương trình có dạng $A(x) \\cdot B(x) = 0$. Phương trình chứa ẩn ở '
                'mẫu là phương trình có biểu thức chứa ẩn nằm ở mẫu thức.',
  'theory': '1. Muốn giải phương trình tích $(a_1x + b_1)(a_2x + b_2) = 0$, ta giải hai phương trình $a_1x + '
            'b_1 = 0$ và $a_2x + b_2 = 0$, rồi lấy tất cả các nghiệm của chúng.\n'
            '2. Các bước giải phương trình chứa ẩn ở mẫu:\n'
            '- Bước 1: Tìm điều kiện xác định (ĐKXĐ) của phương trình (cho các mẫu thức khác $0$).\n'
            '- Bước 2: Quy đồng mẫu hai vế của phương trình rồi khử mẫu.\n'
            '- Bước 3: Giải phương trình vừa nhận được.\n'
            '- Bước 4: Kiểm tra điều kiện xác định và kết luận nghiệm.',
  'formulas': [{'category': 'Phương trình tích và phương trình chứa ẩn ở mẫu',
                'items': [{'name': 'Phương trình tích',
                           'formula': '$A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$',
                           'note': 'Lấy hợp tất cả các nghiệm'},
                          {'name': 'Điều kiện xác định',
                           'formula': 'Mẫu thức $M(x) \\neq 0$',
                           'note': 'Bắt buộc đối chiếu nghiệm với ĐKXĐ'}]}],
  'example': 'Giải phương trình $\\dfrac{x + 2}{x - 2} - \\dfrac{1}{x} = \\dfrac{2}{x(x - 2)}$.',
  'example_answer': 'ĐKXĐ: $x \\neq 0$ và $x \\neq 2$.\n'
                    'Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 \\Rightarrow x^2 + 2x - x + 2 = 2 '
                    '\\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = 0$.\n'
                    'Suy ra $x = 0$ (loại vì không thỏa mãn ĐKXĐ) hoặc $x = -1$ (thỏa mãn ĐKXĐ).\n'
                    'Vậy nghiệm của phương trình là $x = -1$.',
  'real_life': 'Tính thời gian hoàn thành công việc hoặc vận tốc chuyển động trong các bài toán có biểu thức '
               'phân thức.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tập nghiệm của phương trình tích $(x - 3)(2x + 4) = 0$ là:',
            'options': ['$S = \\{2; -3\\}$', '$S = \\{3; 4\\}$', '$S = \\{-2\\}$', '$S = \\{-2; 3\\}$'],
            'answer': 3,
            'solution': 'Ta có $x - 3 = 0 \\Rightarrow x = 3$ hoặc $2x + 4 = 0 \\Rightarrow x = -2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Điều kiện xác định của phương trình $\\dfrac{2x + 1}{x - 5} = 3$ là:',
            'options': ['$x \\neq 5$', '$x \\neq -5$', '$x \\neq -\\dfrac{1}{2}$', '$x > 5$'],
            'answer': 0,
            'solution': 'Phương trình xác định khi mẫu thức $x - 5 \\neq 0 \\Leftrightarrow x \\neq 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: Phương trình quy về phương trình bậc nhất một ẩn**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Phương trình tích**?',
            'options': ['$A(x) : B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$',
                        '$A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$',
                        '$A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 1$',
                        '$A(x) \\cdot B(x) = 2 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: Phương trình quy về phương trình bậc nhất một '
                        'ẩn, **Phương trình tích** được xác định bởi: $A(x) \\cdot B(x) = 0 \\Leftrightarrow '
                        'A(x) = 0$ hoặc $B(x) = 0$. (Lấy hợp tất cả các nghiệm)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: Phương trình quy về phương trình bậc nhất một ẩn**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Điều kiện xác định**?',
            'options': ['Mẫu thức $M(x) \\neq 1$',
                        'Mẫu thức $M(x) \\neq 2$',
                        'Mẫu thức $M(x) \\neq 0$',
                        '$A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$'],
            'answer': 2,
            'solution': 'Trong Bài 4: Phương trình quy về phương trình bậc nhất một ẩn, **Điều kiện xác '
                        'định** có công thức/quy tắc là: Mẫu thức $M(x) \\neq 0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số nghiệm của phương trình $\\dfrac{x}{x - 1} = \\dfrac{1}{x - 1}$ là:',
            'options': ['$1$', '$2$', 'Vô số', '$0$'],
            'answer': 3,
            'solution': 'ĐKXĐ: $x \\neq 1$. Khử mẫu được $x = 1$ (không thỏa mãn ĐKXĐ), nên phương trình vô '
                        'nghiệm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: Phương trình quy về phương trình bậc nhất một ẩn**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 0$.',
                        'Giải được phương trình tích có dạng $(a_1x - b_1)(a_2x + b_2) = 0$.',
                        'Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 1$.',
                        'Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 2$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 4: Phương trình quy về phương trình bậc nhất một ẩn: '
                        'Giải được phương trình tích có dạng $(a_1x + b_1)(a_2x + b_2) = 0$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình $x^2 - 4 + (x - 2)(2x + 1) = 0$ (1).',
            'statements': ['Ta có thể phân tích $x^2 - 4 = (x - 2)(x + 2)$.',
                           'Phương trình (1) đưa được về phương trình tích $(x - 2)(3x + 3) = 0$.',
                           '$x = 2$ là nghiệm duy nhất của phương trình (1).',
                           'Tổng các nghiệm của phương trình (1) bằng $1$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $(x - 2)[(x + 2) + (2x + 1)] = (x - 2)(3x + 3) = 0$. c) Sai vì '
                        'phương trình có hai nghiệm $x = 2$ và $x = -1$. d) Đúng vì $2 + (-1) = 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 4: Phương trình quy về '
                 'phương trình bậc nhất một ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Giải được phương trình tích có dạng '
                           '$(a_1x + b_1)(a_2x + b_2) = 0$.',
                           'Trong **Bài 4: Phương trình quy về phương trình bậc nhất một ẩn**, quy tắc/công '
                           'thức **Phương trình tích** được viết là: $A(x) \\cdot B(x) = 0 \\Leftrightarrow '
                           'A(x) = 0$ hoặc $B(x) = 0$.',
                           'Nếu áp dụng sai dấu/phép tính thành $A(x) : B(x) = 0 \\Leftrightarrow A(x) = 0$ '
                           'hoặc $B(x) = 0$ thì kết quả của **Phương trình tích** trong **Bài 4: Phương '
                           'trình quy về phương trình bậc nhất một ẩn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Giải phương trình $\\dfrac{x + 2}{x - 2} - \\dfrac{1}{x} = '
                           '\\dfrac{2}{x(x - 2)}$.”, kết quả giải đúng là: ĐKXĐ: $x \\neq 0$ và $x \\neq 2$. '
                           'Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 \\Rightarrow x^2 + 2x - x + 2 = 2 '
                           '\\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = 0$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 4: Phương trình quy về phương trình bậc '
                        'nhất một ẩn. b) **Đúng** theo công thức **Phương trình tích** ($A(x) \\cdot B(x) = '
                        '0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = 0$). c) **Sai** vì công thức đúng của '
                        '**Phương trình tích** phải là $A(x) \\cdot B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc '
                        '$B(x) = 0$ chứ không phải $A(x) : B(x) = 0 \\Leftrightarrow A(x) = 0$ hoặc $B(x) = '
                        '0$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: Phương trình quy về phương trình bậc nhất một '
                 'ẩn** để giải bài toán sau: Giải phương trình $\\dfrac{x + 2}{x - 2} - \\dfrac{1}{x} = '
                 '\\dfrac{2}{x(x - 2)}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['ĐKXĐ: $x \\neq 0$ và $x \\neq 2$. Quy đồng và khử mẫu: $x(x - 2) - (x - 2) = 2 '
                        '\\Rightarrow x^2 + 2x - x + 2 = 2 \\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = '
                        '0$...',
                        'ĐKXĐ: $x \\neq 0$ và $x \\neq 2$. Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 '
                        '\\Rightarrow x^2 + 2x - x + 2 = 2 \\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = '
                        '0$...',
                        'ĐKXĐ: $x \\neq 0$ và $x \\neq 2$. Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 '
                        '\\Rightarrow x^2 + 2x - x + 2 = 2 \\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = '
                        '1$...',
                        'ĐKXĐ: $x \\neq 2$ và $x \\neq 2$. Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 '
                        '\\Rightarrow x^2 + 2x - x + 2 = 2 \\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = '
                        '0$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: Phương trình quy về phương trình bậc nhất một ẩn: '
                        'ĐKXĐ: $x \\neq 0$ và $x \\neq 2$.\n'
                        'Quy đồng và khử mẫu: $x(x + 2) - (x - 2) = 2 \\Rightarrow x^2 + 2x - x + 2 = 2 '
                        '\\Rightarrow x^2 + x = 0 \\Rightarrow x(x + 1) = 0$.\n'
                        'Suy ra $x = 0$ (loại vì không thỏa mãn ĐKXĐ) hoặc $x = -1$ (thỏa mãn ĐKXĐ).\n'
                        'Vậy nghiệm của phương trình là $x = -1$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Giải phương trình $\\dfrac{3}{x + 1} + \\dfrac{2}{x - 2} = \\dfrac{4x + 2}{(x + 1)(x - '
                 '2)}$ được nghiệm $x$ bằng bao nhiêu?',
            'answer': ['6'],
            'unit': None,
            'solution': 'ĐKXĐ: $x \\neq -1, x \\neq 2$. Khử mẫu: $3(x - 2) + 2(x + 1) = 4x + 2 \\Rightarrow '
                        '5x - 4 = 4x + 2 \\Rightarrow x = 6$ (thỏa mãn ĐKXĐ).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch02-bat-phuong-trinh',
  'context_title': 'Chương II: Phương trình và bất phương trình bậc nhất một ẩn',
  'context': 'Chương II · SGK Toán 9: Phương trình và bất phương trình bậc nhất một ẩn.',
  'title': 'Bài 5: Bất đẳng thức và tính chất',
  'icon': '⚖️',
  'description': 'Nhận biết bất đẳng thức và vận dụng tính chất liên hệ giữa thứ tự với phép cộng, phép '
                 'nhân.',
  'requirements': ['Nhận biết được thứ tự trên tập hợp số thực và khái niệm bất đẳng thức.',
                   'Mô tả được tính chất bắc cầu, tính chất liên hệ giữa thứ tự và phép cộng, phép nhân.',
                   'Vận dụng kiến thức của **Bài 5: Bất đẳng thức và tính chất** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Hệ thức dạng $a < b$ (hay $a > b, a \\le b, a \\ge b$) được gọi là bất đẳng thức, trong đó '
                '$a$ là vế trái và $b$ là vế phải.',
  'theory': '1. Tính chất liên hệ với phép cộng: Khi cộng cùng một số vào cả hai vế của một bất đẳng thức '
            'thì được bất đẳng thức mới cùng chiều: Nếu $a < b$ thì $a + c < b + c$.\n'
            '2. Tính chất liên hệ với phép nhân:\n'
            '- Khi nhân cả hai vế của bất đẳng thức với cùng một số dương thì được bất đẳng thức mới cùng '
            'chiều: Nếu $a < b$ và $c > 0$ thì $ac < bc$.\n'
            '- Khi nhân cả hai vế của bất đẳng thức với cùng một số âm thì được bất đẳng thức mới ngược '
            'chiều: Nếu $a < b$ và $c < 0$ thì $ac > bc$.',
  'formulas': [{'category': 'Tính chất cơ bản của bất đẳng thức',
                'items': [{'name': 'Cộng cùng một số',
                           'formula': '$a < b \\Rightarrow a + c < b + c$',
                           'note': 'Giữ nguyên chiều bất đẳng thức'},
                          {'name': 'Nhân với số dương',
                           'formula': '$a < b, c > 0 \\Rightarrow ac < bc$',
                           'note': 'Giữ nguyên chiều bất đẳng thức'},
                          {'name': 'Nhân với số âm',
                           'formula': '$a < b, c < 0 \\Rightarrow ac > bc$',
                           'note': 'Đổi chiều bất đẳng thức'}]}],
  'example': 'Cho $a < b$. Hãy so sánh $-3a + 5$ và $-3b + 5$.',
  'example_answer': 'Vì $a < b$ và $-3 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$.\n'
                    'Cộng $5$ vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > -3b + 5$.',
  'real_life': 'Diễn tả biển báo giới hạn tốc độ tối đa $v \\le 60$ km/h hoặc trọng tải cầu tối đa trên '
               'đường bộ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Biển báo giao thông ghi số $50$ (tốc độ tối đa cho phép là $50$ km/h) được biểu thị bằng '
                 'bất đẳng thức nào cho vận tốc $v$ (km/h)?',
            'options': ['$v \\le 50$', '$v < 50$', '$v \\ge 50$', '$v > 50$'],
            'answer': 0,
            'solution': 'Tốc độ tối đa $50$ km/h nghĩa là vận tốc $v$ không vượt quá $50$, tức là $v \\le '
                        '50$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho $a > b$. Khẳng định nào sau đây là đúng?',
            'options': ['$-2a > -2b$', '$a + 3 > b + 3$', '$a - 5 < b - 5$', '$3a < 3b$'],
            'answer': 1,
            'solution': 'Cộng $3$ vào hai vế của $a > b$ ta được $a + 3 > b + 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Bất đẳng thức và tính chất**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Cộng cùng một số**?',
            'options': ['$a < b \\Rightarrow a - c < b + c$',
                        'Đảo ngược vế của quy tắc: $a < b \\Rightarrow a + c < b + c$',
                        '$a < b \\Rightarrow a + c < b + c$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a < b \\Rightarrow a + c < b + '
                        'c$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Bất đẳng thức và tính chất, **Cộng cùng một '
                        'số** được xác định bởi: $a < b \\Rightarrow a + c < b + c$. (Giữ nguyên chiều bất '
                        'đẳng thức)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Bất đẳng thức và tính chất**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Nhân với số dương**?',
            'options': ['$a < b, c < 0 \\Rightarrow ac < bc$',
                        '$a < b, c > 1 \\Rightarrow ac < bc$',
                        '$a < b, c > 2 \\Rightarrow ac < bc$',
                        '$a < b, c > 0 \\Rightarrow ac < bc$'],
            'answer': 3,
            'solution': 'Trong Bài 5: Bất đẳng thức và tính chất, **Nhân với số dương** có công thức/quy tắc '
                        'là: $a < b, c > 0 \\Rightarrow ac < bc$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết $-4a + 1 > -4b + 1$. Kết luận nào sau đây là đúng về hai số $a$ và $b$?',
            'options': ['$a < b$', '$a > b$', '$a = b$', '$a \\ge b$'],
            'answer': 0,
            'solution': 'Trừ $1$ ở hai vế được $-4a > -4b$. Nhân hai vế với $-\\dfrac{1}{4} < 0$ (đổi chiều) '
                        'ta được $a < b$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Bất đẳng thức và tính chất**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được thứ tự trên tập hợp số thực và khái niệm bất đẳng thức. (với dấu '
                        'ngược lại)',
                        'Nhận biết được thứ tự trên tập hợp số thực và khái niệm bất đẳng thức.',
                        'Đảo ngược vế của quy tắc: Nhận biết được thứ tự trên tập hợp số thực và khái niệm '
                        'bất đẳng thức.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được thứ tự trên tập '
                        'hợp số thực và khái niệm bất đẳng thức.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Bất đẳng thức và tính chất: Nhận biết được thứ tự '
                        'trên tập hợp số thực và khái niệm bất đẳng thức.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai số thực $x, y$ thỏa mãn $x < y$.',
            'statements': ['$2x - 7 < 2y - 7$.',
                           '$-5x > -5y$.',
                           '$3 - x < 3 - y$.',
                           'Nếu $x > 0$ thì $x^2 < y^2$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì nhân với $2 > 0$ rồi trừ $7$. b) Đúng vì nhân với $-5 < 0$ đổi chiều. c) '
                        'Sai vì $-x > -y \\Rightarrow 3 - x > 3 - y$. d) Đúng vì $0 < x < y \\Rightarrow x^2 '
                        '< xy < y^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 5: Bất đẳng thức và tính '
                 'chất**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được thứ tự trên tập hợp số '
                           'thực và khái niệm bất đẳng thức.',
                           'Trong **Bài 5: Bất đẳng thức và tính chất**, quy tắc/công thức **Cộng cùng một '
                           'số** được viết là: $a < b \\Rightarrow a + c < b + c$.',
                           'Nếu áp dụng sai dấu/phép tính thành $a < b \\Rightarrow a - c < b + c$ thì kết '
                           'quả của **Cộng cùng một số** trong **Bài 5: Bất đẳng thức và tính chất** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Cho $a < b$. Hãy so sánh $-3a + 5$ và $-3b + 5$.”, kết quả '
                           'giải đúng là: Vì $a < b$ và $-3 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a '
                           '> -3b$. Cộng $5$ vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > '
                           '-3b + 5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 5: Bất đẳng thức và tính chất. b) **Đúng** '
                        'theo công thức **Cộng cùng một số** ($a < b \\Rightarrow a + c < b + c$). c) '
                        '**Sai** vì công thức đúng của **Cộng cùng một số** phải là $a < b \\Rightarrow a + '
                        'c < b + c$ chứ không phải $a < b \\Rightarrow a - c < b + c$. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Bất đẳng thức và tính chất** để giải bài toán '
                 'sau: Cho $a < b$. Hãy so sánh $-3a + 5$ và $-3b + 5$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì $a < b$ và $-3 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$. Cộng $5$ '
                        'vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a - 5 > -3b + 5$...',
                        'Vì $a < b$ và $-3 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$. Cộng $5$ '
                        'vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > -3b + 4$...',
                        'Vì $a < b$ và $-3 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$. Cộng $5$ '
                        'vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > -3b + 5$...',
                        'Vì $a < b$ và $-6 < 0$ nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$. Cộng $5$ '
                        'vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > -3b + 5$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Bất đẳng thức và tính chất: Vì $a < b$ và $-3 < 0$ '
                        'nên khi nhân hai vế với $-3$ ta được: $-3a > -3b$.\n'
                        'Cộng $5$ vào hai vế của bất đẳng thức $-3a > -3b$, ta được: $-3a + 5 > -3b + 5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Với mọi số thực $x$, giá trị nhỏ nhất của biểu thức $P = x^2 + 2x + 5$ bằng bao nhiêu?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta có $P = (x + 1)^2 + 4$. Vì $(x + 1)^2 \\ge 0$ với mọi $x \\in \\mathbb{R}$ nên '
                        '$P \\ge 4$. Giá trị nhỏ nhất bằng $4$ khi $x = -1$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch02-bat-phuong-trinh',
  'context_title': 'Chương II: Phương trình và bất phương trình bậc nhất một ẩn',
  'context': 'Chương II · SGK Toán 9: Phương trình và bất phương trình bậc nhất một ẩn.',
  'title': 'Bài 6: Bất phương trình bậc nhất một ẩn',
  'icon': '📏',
  'description': 'Nhận biết và giải bất phương trình bậc nhất một ẩn, ứng dụng vào thực tiễn.',
  'requirements': ['Nhận biết được bất phương trình bậc nhất một ẩn và nghiệm của nó.',
                   'Giải được bất phương trình bậc nhất một ẩn $ax + b < 0$ (hoặc $ax + b > 0, ax + b \\le '
                   '0, ax + b \\ge 0$).',
                   'Vận dụng kiến thức của **Bài 6: Bất phương trình bậc nhất một ẩn** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Bất phương trình dạng $ax + b < 0$ (hoặc $ax + b > 0, ax + b \\le 0, ax + b \\ge 0$) trong '
                'đó $a, b$ là hai số đã cho, $a \\neq 0$, được gọi là bất phương trình bậc nhất một ẩn $x$.',
  'theory': 'Cách giải bất phương trình bậc nhất một ẩn $ax + b < 0$ ($a \\neq 0$):\n'
            '- Chuyển hạng tử tự do sang vế phải: $ax < -b$.\n'
            '- Nếu $a > 0$ thì chia hai vế cho $a$ và giữ nguyên chiều: $x < -\\dfrac{b}{a}$.\n'
            '- Nếu $a < 0$ thì chia hai vế cho $a$ và đổi chiều bất phương trình: $x > -\\dfrac{b}{a}$.',
  'formulas': [{'category': 'Nghiệm của bất phương trình $ax + b < 0$',
                'items': [{'name': 'Trường hợp $a > 0$',
                           'formula': '$ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$',
                           'note': 'Chia cho số dương: giữ nguyên chiều'},
                          {'name': 'Trường hợp $a < 0$',
                           'formula': '$ax + b < 0 \\Leftrightarrow x > -\\dfrac{b}{a}$',
                           'note': 'Chia cho số âm: đổi chiều'}]}],
  'example': 'Giải bất phương trình $-3x + 12 \\ge 0$.',
  'example_answer': 'Ta có: $-3x + 12 \\ge 0 \\Leftrightarrow -3x \\ge -12$.\n'
                    'Chia cả hai vế cho $-3 < 0$ (đổi chiều bất phương trình): $x \\le 4$.\n'
                    'Vậy nghiệm của bất phương trình là $x \\le 4$.',
  'real_life': 'Xác định số lượng sản phẩm tối thiểu cần bán để cửa hàng bắt đầu có lãi.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bất phương trình nào sau đây là bất phương trình bậc nhất một ẩn?',
            'options': ['$0x + 3 < 0$', '$2x - 5 > 0$', '$x^2 - 1 \\le 0$', '$2x + y \\ge 1$'],
            'answer': 1,
            'solution': 'Bất phương trình bậc nhất một ẩn có dạng $ax + b > 0$ với $a \\neq 0$, nên $2x - 5 '
                        '> 0$ thỏa mãn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nghiệm của bất phương trình $2x - 6 > 0$ là:',
            'options': ['$x < 3$', '$x > -3$', '$x > 3$', '$x < -3$'],
            'answer': 2,
            'solution': 'Ta có $2x - 6 > 0 \\Leftrightarrow 2x > 6 \\Leftrightarrow x > 3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 6: Bất phương trình bậc nhất một ẩn**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Trường hợp $a > 0$**?',
            'options': ['$ax - b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$',
                        '$ax + b < 0 \\Leftrightarrow x < -\\dfrac{a}{b}$',
                        '$ax + b < 2 \\Leftrightarrow x < -\\dfrac{b}{a}$',
                        '$ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 6: Bất phương trình bậc nhất một ẩn, **Trường hợp '
                        '$a > 0$** được xác định bởi: $ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$. '
                        '(Chia cho số dương: giữ nguyên chiều)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 6: Bất phương trình bậc nhất một ẩn**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Trường hợp $a < 0$**?',
            'options': ['$ax + b < 0 \\Leftrightarrow x > -\\dfrac{b}{a}$',
                        '$ax - b < 0 \\Leftrightarrow x > -\\dfrac{b}{a}$',
                        '$ax + b < 0 \\Leftrightarrow x > -\\dfrac{a}{b}$',
                        '$ax + b < 2 \\Leftrightarrow x > -\\dfrac{b}{a}$'],
            'answer': 0,
            'solution': 'Trong Bài 6: Bất phương trình bậc nhất một ẩn, **Trường hợp $a < 0$** có công '
                        'thức/quy tắc là: $ax + b < 0 \\Leftrightarrow x > -\\dfrac{b}{a}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nghiệm của bất phương trình $5 - 2x \\le 1$ là:',
            'options': ['$x \\le 2$', '$x \\ge 2$', '$x \\ge -2$', '$x \\le 3$'],
            'answer': 1,
            'solution': 'Ta có $5 - 2x \\le 1 \\Leftrightarrow -2x \\le -4 \\Leftrightarrow x \\ge 2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 6: Bất phương trình bậc nhất một ẩn**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận biết được bất phương trình bậc nhất một ẩn và nghiệm của nó. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được bất phương trình bậc nhất một ẩn và nghiệm '
                        'của nó.',
                        'Nhận biết được bất phương trình bậc nhất một ẩn và nghiệm của nó.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được bất phương trình '
                        'bậc nhất một ẩn và nghiệm của nó.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 6: Bất phương trình bậc nhất một ẩn: Nhận biết được '
                        'bất phương trình bậc nhất một ẩn và nghiệm của nó.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho bất phương trình $3(x - 1) < 5x + 3$ (1).',
            'statements': ['Sau khi khai triển và thu gọn, bất phương trình (1) tương đương với $-2x < 6$.',
                           'Nghiệm của bất phương trình (1) là $x < -3$.',
                           'Số $0$ là một nghiệm của bất phương trình (1).',
                           'Số nguyên âm nhỏ nhất thỏa mãn bất phương trình (1) là $-2$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng vì $3x - 3 < 5x + 3 \\Leftrightarrow -2x < 6$. b) Sai vì chia cho $-2$ đổi '
                        'chiều được $x > -3$. c) Đúng vì $0 > -3$. d) Đúng vì các số nguyên âm lớn hơn $-3$ '
                        'là $-2; -1$, nhỏ nhất là $-2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 6: Bất phương trình bậc '
                 'nhất một ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được bất phương trình bậc nhất '
                           'một ẩn và nghiệm của nó.',
                           'Trong **Bài 6: Bất phương trình bậc nhất một ẩn**, quy tắc/công thức **Trường '
                           'hợp $a > 0$** được viết là: $ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $ax - b < 0 \\Leftrightarrow x < '
                           '-\\dfrac{b}{a}$ thì kết quả của **Trường hợp $a > 0$** trong **Bài 6: Bất phương '
                           'trình bậc nhất một ẩn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Giải bất phương trình $-3x + 12 \\ge 0$.”, kết quả giải đúng '
                           'là: Ta có: $-3x + 12 \\ge 0 \\Leftrightarrow -3x \\ge -12$. Chia cả hai vế cho '
                           '$-3 < 0$ (đổi chiều bất phương trình): $x \\le 4$. Vậy nghiệm củ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 6: Bất phương trình bậc nhất một ẩn. b) '
                        '**Đúng** theo công thức **Trường hợp $a > 0$** ($ax + b < 0 \\Leftrightarrow x < '
                        '-\\dfrac{b}{a}$). c) **Sai** vì công thức đúng của **Trường hợp $a > 0$** phải là '
                        '$ax + b < 0 \\Leftrightarrow x < -\\dfrac{b}{a}$ chứ không phải $ax - b < 0 '
                        '\\Leftrightarrow x < -\\dfrac{b}{a}$. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 6: Bất phương trình bậc nhất một ẩn** để giải bài '
                 'toán sau: Giải bất phương trình $-3x + 12 \\ge 0$. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có: $-3x + 12 \\ge 0 \\Leftrightarrow -3x \\ge -12$. Chia cả hai vế cho $-3 < 0$ '
                        '(đổi chiều bất phương trình): $x \\ge 4$. Vậy nghiệm của bất phương tr...',
                        'Ta có: $-3x + 12 \\ge 0 \\Leftrightarrow -3x \\ge -12$. Chia cả hai vế cho $-3 < 0$ '
                        '(đổi chiều bất phương trình): $x \\le 3$. Vậy nghiệm của bất phương tr...',
                        'Ta có: $-3x + 24 \\ge 0 \\Leftrightarrow -3x \\ge -12$. Chia cả hai vế cho $-3 < 0$ '
                        '(đổi chiều bất phương trình): $x \\le 4$. Vậy nghiệm của bất phương tr...',
                        'Ta có: $-3x + 12 \\ge 0 \\Leftrightarrow -3x \\ge -12$. Chia cả hai vế cho $-3 < 0$ '
                        '(đổi chiều bất phương trình): $x \\le 4$. Vậy nghiệm của bất phương tr...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 6: Bất phương trình bậc nhất một ẩn: Ta có: $-3x + 12 '
                        '\\ge 0 \\Leftrightarrow -3x \\ge -12$.\n'
                        'Chia cả hai vế cho $-3 < 0$ (đổi chiều bất phương trình): $x \\le 4$.\n'
                        'Vậy nghiệm của bất phương trình là $x \\le 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bạn có $100$ nghìn đồng, mua một quyển sổ giá $25$ nghìn đồng và các cây bút giá $6$ '
                 'nghìn đồng một cây. Hỏi bạn đó mua được tối đa bao nhiêu cây bút?',
            'answer': ['12'],
            'unit': None,
            'solution': 'Gọi $x$ ($x \\in \\mathbb{N}^*$) là số cây bút mua được. Ta có $25 + 6x \\le 100 '
                        '\\Leftrightarrow 6x \\le 75 \\Leftrightarrow x \\le 12,5$. Vậy mua được tối đa $12$ '
                        'cây bút.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch03-can-thuc',
  'context_title': 'Chương III: Căn bậc hai và căn bậc ba',
  'context': 'Chương III · SGK Toán 9: Căn bậc hai và căn bậc ba.',
  'title': 'Bài 7: Căn bậc hai và căn thức bậc hai',
  'icon': '√',
  'description': 'Tính căn bậc hai của số thực không âm, tìm điều kiện xác định của căn thức bậc hai và áp '
                 'dụng hằng đẳng thức căn bậc hai.',
  'requirements': ['Nhận biết được căn bậc hai của một số thực không âm và tính được giá trị bằng máy tính '
                   'cầm tay.',
                   'Tìm được điều kiện xác định của căn thức bậc hai $\\sqrt{A}$.',
                   'Áp dụng được hằng đẳng thức $\\sqrt{A^2} = |A|$.'],
  'definition': 'Căn bậc hai của số thực không âm $a$ là số thực $x$ sao cho $x^2 = a$. Mỗi số dương $a$ có '
                'đúng hai căn bậc hai là $\\sqrt{a}$ (căn bậc hai số học) và $-\\sqrt{a}$.',
  'theory': '1. Với $A$ là một biểu thức đại số, ta gọi $\\sqrt{A}$ là căn thức bậc hai của $A$. Biểu thức '
            '$\\sqrt{A}$ xác định khi $A$ nhận giá trị không âm ($A \\ge 0$).\n'
            '2. Với mọi số thực $a$, ta có $\\sqrt{a^2} = |a|$. Mở rộng cho biểu thức $A$: $\\sqrt{A^2} = '
            '|A| = A$ nếu $A \\ge 0$ và bằng $-A$ nếu $A < 0$.',
  'formulas': [{'category': 'Căn thức bậc hai',
                'items': [{'name': 'Điều kiện xác định',
                           'formula': '$\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 0$',
                           'note': 'Biểu thức dưới dấu căn không âm'},
                          {'name': 'Hằng đẳng thức căn bậc hai',
                           'formula': '$\\sqrt{A^2} = |A|$',
                           'note': '$|A| = A$ khi $A \\ge 0$; $|A| = -A$ khi $A < 0$'}]}],
  'example': 'Tìm điều kiện xác định của căn thức $\\sqrt{2x - 6}$ và rút gọn biểu thức $P = \\sqrt{(x - '
             '3)^2}$ khi $x < 3$.',
  'example_answer': 'Căn thức $\\sqrt{2x - 6}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$.\n'
                    'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$, do đó $P = 3 - x$.',
  'real_life': 'Tính vận tốc chạm đất của vật rơi tự do theo công thức $v = \\sqrt{2gh}$ từ độ cao $h$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Các căn bậc hai của số $16$ là:',
            'options': ['Chỉ có $4$', 'Chỉ có $-4$', '$4$ và $-4$', '$8$ và $-8$'],
            'answer': 2,
            'solution': 'Vì $4^2 = 16$ và $(-4)^2 = 16$ nên $16$ có hai căn bậc hai là $4$ và $-4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Điều kiện xác định của căn thức $\\sqrt{x - 4}$ là:',
            'options': ['$x > 4$', '$x \\le 4$', '$x \\neq 4$', '$x \\ge 4$'],
            'answer': 3,
            'solution': 'Căn thức $\\sqrt{x - 4}$ xác định khi $x - 4 \\ge 0 \\Leftrightarrow x \\ge 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Căn bậc hai và căn thức bậc hai**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Điều kiện xác định**?',
            'options': ['$\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 0$',
                        '$\\sqrt{A}$ xác định $\\Leftrightarrow A \\le 0$',
                        '$\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 1$',
                        '$\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 2$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Căn bậc hai và căn thức bậc hai, **Điều kiện '
                        'xác định** được xác định bởi: $\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 0$. '
                        '(Biểu thức dưới dấu căn không âm)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Căn bậc hai và căn thức bậc hai**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Hằng đẳng thức căn bậc hai**?',
            'options': ['$\\sqrt{A^3} = |A|$',
                        '$\\sqrt{A^2} = |A|$',
                        '$\\sqrt{A^1} = |A|$',
                        '$\\sqrt{A^4} = |A|$'],
            'answer': 1,
            'solution': 'Trong Bài 7: Căn bậc hai và căn thức bậc hai, **Hằng đẳng thức căn bậc hai** có '
                        'công thức/quy tắc là: $\\sqrt{A^2} = |A|$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\sqrt{(2 - \\sqrt{5})^2}$ bằng:',
            'options': ['$2 - \\sqrt{5}$', '$2 + \\sqrt{5}$', '$\\sqrt{5} - 2$', '$-\\sqrt{5} - 2$'],
            'answer': 2,
            'solution': 'Ta có $\\sqrt{(2 - \\sqrt{5})^2} = |2 - \\sqrt{5}| = \\sqrt{5} - 2$ (vì $\\sqrt{5} '
                        '> \\sqrt{4} = 2$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Căn bậc hai và căn thức bậc hai**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được căn bậc hai của một số thực không âm và tính được giá trị bằng máy '
                        'tính cầm tay. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được căn bậc hai của một số thực không âm và '
                        'tính được giá trị bằng máy tính cầm tay.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được căn bậc hai của '
                        'một số thực không âm và tính được giá trị bằng máy tính cầm tay.',
                        'Nhận biết được căn bậc hai của một số thực không âm và tính được giá trị bằng máy '
                        'tính cầm tay.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Căn bậc hai và căn thức bậc hai: Nhận biết được '
                        'căn bậc hai của một số thực không âm và tính được giá trị bằng máy tính cầm tay.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $A = \\sqrt{9x^2}$ và căn thức $B = \\sqrt{6 - 2x}$.',
            'statements': ['Căn thức $B$ xác định khi và chỉ khi $x \\le 3$.',
                           'Với mọi số thực $x$, ta luôn có $A = 3x$.',
                           'Khi $x = -2$ thì $A = 6$ và $B = \\sqrt{10}$.',
                           'Phương trình $A = 12$ có đúng một nghiệm là $x = 4$.'],
            'answer': [True, False, True, False],
            'solution': 'a) Đúng vì $6 - 2x \\ge 0 \\Leftrightarrow x \\le 3$. b) Sai vì $A = |3x| = 3|x|$. '
                        'c) Đúng vì $A = 3|-2| = 6$ và $B = \\sqrt{6 - 2(-2)} = \\sqrt{10}$. d) Sai vì $3|x| '
                        '= 12 \\Leftrightarrow x = \\pm 4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 7: Căn bậc hai và căn thức '
                 'bậc hai**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được căn bậc hai của một số '
                           'thực không âm và tính được giá trị bằng máy tính cầm tay.',
                           'Trong **Bài 7: Căn bậc hai và căn thức bậc hai**, quy tắc/công thức **Điều kiện '
                           'xác định** được viết là: $\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 0$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\sqrt{A}$ xác định $\\Leftrightarrow A '
                           '\\le 0$ thì kết quả của **Điều kiện xác định** trong **Bài 7: Căn bậc hai và căn '
                           'thức bậc hai** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tìm điều kiện xác định của căn thức $\\sqrt{2x - 6}$ và rút '
                           'gọn biểu thức $P = \\sqrt{(x - 3)^2}$ khi $x < 3$.”, kết quả giải đúng là: Căn '
                           'thức $\\sqrt{2x - 6}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$. Ta '
                           'có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 7: Căn bậc hai và căn thức bậc hai. b) '
                        '**Đúng** theo công thức **Điều kiện xác định** ($\\sqrt{A}$ xác định '
                        '$\\Leftrightarrow A \\ge 0$). c) **Sai** vì công thức đúng của **Điều kiện xác '
                        'định** phải là $\\sqrt{A}$ xác định $\\Leftrightarrow A \\ge 0$ chứ không phải '
                        '$\\sqrt{A}$ xác định $\\Leftrightarrow A \\le 0$. d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Căn bậc hai và căn thức bậc hai** để giải bài '
                 'toán sau: Tìm điều kiện xác định của căn thức $\\sqrt{2x - 6}$ và rút gọn biểu thức $P = '
                 '\\sqrt{(x - 3)^2}$ khi $x < 3$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Căn thức $\\sqrt{2x - 6}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$. '
                        'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$, do đ...',
                        'Căn thức $\\sqrt{2x - 6}$ xác định khi $2x - 6 \\le 0 \\Leftrightarrow x \\ge 3$. '
                        'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$, do đ...',
                        'Căn thức $\\sqrt{2x - 6}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$. '
                        'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 1$, do đ...',
                        'Căn thức $\\sqrt{2x - 12}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$. '
                        'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$, do đ...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 7: Căn bậc hai và căn thức bậc hai: Căn thức $\\sqrt{2x '
                        '- 6}$ xác định khi $2x - 6 \\ge 0 \\Leftrightarrow x \\ge 3$.\n'
                        'Ta có $P = \\sqrt{(x - 3)^2} = |x - 3|$. Vì $x < 3$ nên $x - 3 < 0$, do đó $P = 3 - '
                        'x$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Rút gọn và tính giá trị của biểu thức $M = \\sqrt{(3 - \\sqrt{7})^2} + \\sqrt{7}$ ta được '
                 'kết quả bằng bao nhiêu?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Vì $3 = \\sqrt{9} > \\sqrt{7}$ nên $\\sqrt{(3 - \\sqrt{7})^2} = 3 - \\sqrt{7}$. Suy '
                        'ra $M = 3 - \\sqrt{7} + \\sqrt{7} = 3$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch03-can-thuc',
  'context_title': 'Chương III: Căn bậc hai và căn bậc ba',
  'context': 'Chương III · SGK Toán 9: Căn bậc hai và căn bậc ba.',
  'title': 'Bài 8: Khai căn bậc hai với phép nhân và phép chia',
  'icon': '✖️',
  'description': 'Vận dụng quy tắc khai căn bậc hai của một tích và một thương để tính toán, rút gọn biểu '
                 'thức.',
  'requirements': ['Thực hiện được phép khai căn bậc hai của một tích và nhân các căn bậc hai.',
                   'Thực hiện được phép khai căn bậc hai của một thương và chia các căn bậc hai.',
                   'Vận dụng kiến thức của **Bài 8: Khai căn bậc hai với phép nhân và phép chia** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Với các biểu thức không âm $A, B$, căn bậc hai của một tích bằng tích các căn bậc hai, và '
                'căn bậc hai của một thương ($B > 0$) bằng thương các căn bậc hai.',
  'theory': '1. Khai căn bậc hai và phép nhân: Với $A \\ge 0, B \\ge 0$, ta có $\\sqrt{A \\cdot B} = '
            '\\sqrt{A} \\cdot \\sqrt{B}$.\n'
            '2. Khai căn bậc hai và phép chia: Với $A \\ge 0, B > 0$, ta có $\\sqrt{\\dfrac{A}{B}} = '
            '\\dfrac{\\sqrt{A}}{\\sqrt{B}}$.',
  'formulas': [{'category': 'Liên hệ giữa phép khai căn bậc hai với phép nhân và phép chia',
                'items': [{'name': 'Khai căn một tích',
                           'formula': '$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ ($A \\ge 0, B \\ge '
                                      '0$)',
                           'note': 'Chiều ngược lại: $\\sqrt{A} \\cdot \\sqrt{B} = \\sqrt{A \\cdot B}$'},
                          {'name': 'Khai căn một thương',
                           'formula': '$\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ ($A \\ge 0, B '
                                      '> 0$)',
                           'note': 'Chiều ngược lại: $\\dfrac{\\sqrt{A}}{\\sqrt{B}} = '
                                   '\\sqrt{\\dfrac{A}{B}}$'}]}],
  'example': 'Tính giá trị của các biểu thức: a) $\\sqrt{12} \\cdot \\sqrt{3}$; b) '
             '$\\dfrac{\\sqrt{50}}{\\sqrt{2}}$.',
  'example_answer': 'a) $\\sqrt{12} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$.\n'
                    'b) $\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$.',
  'real_life': 'Tính độ dài đường chéo màn hình tivi hoặc khoảng cách nhìn xa trên biển từ ngọn hải đăng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\sqrt{2} \\cdot \\sqrt{18}$ bằng:',
            'options': ['$36$', '$9$', '$12$', '$6$'],
            'answer': 3,
            'solution': 'Ta có $\\sqrt{2} \\cdot \\sqrt{18} = \\sqrt{2 \\cdot 18} = \\sqrt{36} = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của biểu thức $\\dfrac{\\sqrt{75}}{\\sqrt{3}}$ bằng:',
            'options': ['$5$', '$25$', '$15$', '$\\sqrt{5}$'],
            'answer': 0,
            'solution': 'Ta có $\\dfrac{\\sqrt{75}}{\\sqrt{3}} = \\sqrt{\\dfrac{75}{3}} = \\sqrt{25} = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Khai căn bậc hai với phép nhân và phép chia**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Khai căn một tích**?',
            'options': ['$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ ($A \\le 0, B \\ge 0$)',
                        '$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ ($A \\ge 0, B \\ge 0$)',
                        '$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ ($A \\ge 0, B \\ge 1$)',
                        '$\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ ($A \\ge 2, B \\ge 0$)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 8: Khai căn bậc hai với phép nhân và phép chia, '
                        '**Khai căn một tích** được xác định bởi: $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot '
                        '\\sqrt{B}$ ($A \\ge 0, B \\ge 0$). (Chiều ngược lại: $\\sqrt{A} \\cdot \\sqrt{B} = '
                        '\\sqrt{A \\cdot B}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Khai căn bậc hai với phép nhân và phép chia**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Khai căn một thương**?',
            'options': ['$\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ ($A \\le 0, B > 0$)',
                        '$\\sqrt{\\dfrac{B}{A}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ ($A \\ge 0, B > 0$)',
                        '$\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ ($A \\ge 0, B > 0$)',
                        '$\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ ($A \\ge 2, B > 0$)'],
            'answer': 2,
            'solution': 'Trong Bài 8: Khai căn bậc hai với phép nhân và phép chia, **Khai căn một thương** '
                        'có công thức/quy tắc là: $\\sqrt{\\dfrac{A}{B}} = \\dfrac{\\sqrt{A}}{\\sqrt{B}}$ '
                        '($A \\ge 0, B > 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Với $a < 0$, rút gọn biểu thức $\\sqrt{16a^2b^4}$ ta được kết quả là:',
            'options': ['$4ab^2$', '$4a^2b^2$', '$-16ab^2$', '$-4ab^2$'],
            'answer': 3,
            'solution': 'Ta có $\\sqrt{16a^2b^4} = 4|a|b^2$. Vì $a < 0$ nên $|a| = -a$, suy ra kết quả là '
                        '$-4ab^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 8: Khai căn bậc hai với phép nhân và phép chia**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép khai căn bậc hai của một tích và nhân các căn bậc hai.',
                        'Thực hiện được phép khai căn bậc hai của một tích và nhân các căn bậc hai. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép khai căn bậc hai của một tích và nhân '
                        'các căn bậc hai.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép khai căn '
                        'bậc hai của một tích và nhân các căn bậc hai.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 8: Khai căn bậc hai với phép nhân và phép chia: Thực '
                        'hiện được phép khai căn bậc hai của một tích và nhân các căn bậc hai.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hai biểu thức $M = \\sqrt{0,36 \\cdot 25}$ và $N = \\sqrt{\\dfrac{49x^2}{9}}$ với $x < '
                 '0$.',
            'statements': ['Giá trị của biểu thức $M$ bằng $3$.',
                           'Ta có thể viết $M = \\sqrt{0,36} \\cdot \\sqrt{25} = 0,6 \\cdot 5$.',
                           'Biểu thức $N$ rút gọn bằng $\\dfrac{7x}{3}$.',
                           'Khi $x = -3$ thì $M + N = 10$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $0,6 \\cdot 5 = 3$. b) Đúng. c) Sai vì $x < 0$ nên $N = \\dfrac{7|x|}{3} '
                        '= -\\dfrac{7x}{3}$. d) Đúng vì khi $x = -3$ thì $N = 7$, suy ra $M + N = 3 + 7 = '
                        '10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 8: Khai căn bậc hai với '
                 'phép nhân và phép chia**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép khai căn bậc hai của '
                           'một tích và nhân các căn bậc hai.',
                           'Trong **Bài 8: Khai căn bậc hai với phép nhân và phép chia**, quy tắc/công thức '
                           '**Khai căn một tích** được viết là: $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot '
                           '\\sqrt{B}$ ($A \\ge 0, B \\ge 0$).',
                           'Nếu áp dụng sai dấu/phép tính thành $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot '
                           '\\sqrt{B}$ ($A \\le 0, B \\ge 0$) thì kết quả của **Khai căn một tích** trong '
                           '**Bài 8: Khai căn bậc hai với phép nhân và phép chia** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính giá trị của các biểu thức: a) $\\sqrt{12} \\cdot '
                           '\\sqrt{3}$; b) $\\dfrac{\\sqrt{50}}{\\sqrt{2}}$.”, kết quả giải đúng là: a) '
                           '$\\sqrt{12} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$. b) '
                           '$\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 8: Khai căn bậc hai với phép nhân và phép '
                        'chia. b) **Đúng** theo công thức **Khai căn một tích** ($\\sqrt{A \\cdot B} = '
                        '\\sqrt{A} \\cdot \\sqrt{B}$ ($A \\ge 0, B \\ge 0$)). c) **Sai** vì công thức đúng '
                        'của **Khai căn một tích** phải là $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot \\sqrt{B}$ '
                        '($A \\ge 0, B \\ge 0$) chứ không phải $\\sqrt{A \\cdot B} = \\sqrt{A} \\cdot '
                        '\\sqrt{B}$ ($A \\le 0, B \\ge 0$). d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 8: Khai căn bậc hai với phép nhân và phép chia** để '
                 'giải bài toán sau: Tính giá trị của các biểu thức: a) $\\sqrt{12} \\cdot \\sqrt{3}$; b) '
                 '$\\dfrac{\\sqrt{50}}{\\sqrt{2}}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['a) $\\sqrt{12} : \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$. b) '
                        '$\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$.',
                        'a) $\\sqrt{12} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$. b) '
                        '$\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$.',
                        'a) $\\sqrt{12} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$. b) '
                        '$\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{2}{50}} = \\sqrt{25} = 5$.',
                        'a) $\\sqrt{24} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$. b) '
                        '$\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 8: Khai căn bậc hai với phép nhân và phép chia: a) '
                        '$\\sqrt{12} \\cdot \\sqrt{3} = \\sqrt{12 \\cdot 3} = \\sqrt{36} = 6$.\n'
                        'b) $\\dfrac{\\sqrt{50}}{\\sqrt{2}} = \\sqrt{\\dfrac{50}{2}} = \\sqrt{25} = 5$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $P = (\\sqrt{20} - \\sqrt{5}) \\cdot \\sqrt{5}$.',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ta có $P = \\sqrt{20 \\cdot 5} - \\sqrt{5 \\cdot 5} = \\sqrt{100} - 5 = 10 - 5 = '
                        '5$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch03-can-thuc',
  'context_title': 'Chương III: Căn bậc hai và căn bậc ba',
  'context': 'Chương III · SGK Toán 9: Căn bậc hai và căn bậc ba.',
  'title': 'Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai',
  'icon': '✨',
  'description': 'Đưa thừa số ra ngoài hoặc vào trong dấu căn, trục căn thức ở mẫu và rút gọn biểu thức chứa '
                 'căn.',
  'requirements': ['Thực hiện được phép đưa thừa số ra ngoài dấu căn và đưa thừa số vào trong dấu căn.',
                   'Thực hiện được phép trục căn thức ở mẫu.',
                   'Rút gọn được các biểu thức chứa căn thức bậc hai.'],
  'definition': 'Các phép biến đổi đơn giản căn thức bậc hai gồm: đưa thừa số ra ngoài dấu căn, đưa thừa số '
                'vào trong dấu căn và khử căn thức ở mẫu (trục căn thức ở mẫu).',
  'theory': '1. Đưa thừa số ra ngoài dấu căn: $\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 0$).\n'
            '2. Đưa thừa số vào trong dấu căn: Nếu $A \\ge 0, B \\ge 0$ thì $A\\sqrt{B} = \\sqrt{A^2B}$; nếu '
            '$A < 0, B \\ge 0$ thì $A\\sqrt{B} = -\\sqrt{A^2B}$.\n'
            '3. Trục căn thức ở mẫu: Nhân cả tử và mẫu với biểu thức liên hợp của mẫu để làm mất dấu căn ở '
            'mẫu.',
  'formulas': [{'category': 'Các phép biến đổi căn thức bậc hai',
                'items': [{'name': 'Đưa thừa số ra ngoài dấu căn',
                           'formula': '$\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 0$)',
                           'note': 'Nếu $A \\ge 0$ thì $\\sqrt{A^2B} = A\\sqrt{B}$'},
                          {'name': 'Trục căn thức dạng đơn thức',
                           'formula': '$\\dfrac{A}{\\sqrt{B}} = \\dfrac{A\\sqrt{B}}{B}$ ($B > 0$)',
                           'note': 'Nhân cả tử và mẫu với $\\sqrt{B}$'},
                          {'name': 'Trục căn thức bằng biểu thức liên hợp',
                           'formula': '$\\dfrac{C}{\\sqrt{A} \\pm \\sqrt{B}} = \\dfrac{C(\\sqrt{A} \\mp '
                                      '\\sqrt{B})}{A - B}$',
                           'note': '$A \\ge 0, B \\ge 0, A \\neq B$'}]}],
  'example': 'Rút gọn biểu thức $A = 3\\sqrt{8} - \\sqrt{50} + \\dfrac{2}{\\sqrt{2} - 1}$.',
  'example_answer': 'Ta có $3\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; '
                    '$\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = 2\\sqrt{2} + 2$.\n'
                    'Do đó $A = 6\\sqrt{2} - 5\\sqrt{2} + 2\\sqrt{2} + 2 = 3\\sqrt{2} + 2$.',
  'real_life': 'Đơn giản hóa các công thức tính chu kì dao động của con lắc đơn $T = '
               '2\\pi\\sqrt{\\dfrac{l}{g}}$ trong vật lí.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đưa thừa số ra ngoài dấu căn của $\\sqrt{27}$ ta được:',
            'options': ['$3\\sqrt{3}$', '$9\\sqrt{3}$', '$3\\sqrt{9}$', '$\\sqrt{3}$'],
            'answer': 0,
            'solution': 'Ta có $\\sqrt{27} = \\sqrt{9 \\cdot 3} = 3\\sqrt{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khử căn thức ở mẫu của biểu thức $\\dfrac{6}{\\sqrt{3}}$ ta được kết quả là:',
            'options': ['$3\\sqrt{3}$', '$2\\sqrt{3}$', '$6\\sqrt{3}$', '$\\sqrt{3}$'],
            'answer': 1,
            'solution': 'Ta có $\\dfrac{6}{\\sqrt{3}} = \\dfrac{6\\sqrt{3}}{3} = 2\\sqrt{3}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Đưa thừa số ra ngoài dấu căn**?',
            'options': ['$\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\le 0$)',
                        '$\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 1$)',
                        '$\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 0$)',
                        '$\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 2$)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn '
                        'thức bậc hai, **Đưa thừa số ra ngoài dấu căn** được xác định bởi: $\\sqrt{A^2B} = '
                        '|A|\\sqrt{B}$ ($B \\ge 0$). (Nếu $A \\ge 0$ thì $\\sqrt{A^2B} = A\\sqrt{B}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Trục căn thức dạng đơn thức**?',
            'options': ['$\\dfrac{A}{\\sqrt{B}} = \\dfrac{A\\sqrt{B}}{B}$ ($B < 0$)',
                        '$\\dfrac{A}{\\sqrt{B}} = \\dfrac{A\\sqrt{B}}{B}$ ($B > 1$)',
                        '$\\dfrac{A}{\\sqrt{B}} = \\dfrac{A\\sqrt{B}}{B}$ ($B > 2$)',
                        '$\\dfrac{A}{\\sqrt{B}} = \\dfrac{A\\sqrt{B}}{B}$ ($B > 0$)'],
            'answer': 3,
            'solution': 'Trong Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai, **Trục '
                        'căn thức dạng đơn thức** có công thức/quy tắc là: $\\dfrac{A}{\\sqrt{B}} = '
                        '\\dfrac{A\\sqrt{B}}{B}$ ($B > 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Rút gọn biểu thức $\\sqrt{12} + \\sqrt{75} - 2\\sqrt{3}$ ta được:',
            'options': ['$5\\sqrt{3}$', '$7\\sqrt{3}$', '$3\\sqrt{3}$', '$6\\sqrt{3}$'],
            'answer': 0,
            'solution': 'Ta có $\\sqrt{12} + \\sqrt{75} - 2\\sqrt{3} = 2\\sqrt{3} + 5\\sqrt{3} - 2\\sqrt{3} '
                        '= 5\\sqrt{3}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc '
                 'hai**, nhận định nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép đưa thừa số ra ngoài dấu căn và đưa thừa số vào trong dấu căn. '
                        '(với dấu ngược lại)',
                        'Thực hiện được phép đưa thừa số ra ngoài dấu căn và đưa thừa số vào trong dấu căn.',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép đưa thừa số ra ngoài dấu căn và đưa '
                        'thừa số vào trong dấu căn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép đưa thừa số '
                        'ra ngoài dấu căn và đưa thừa số vào trong dấu căn.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn '
                        'thức bậc hai: Thực hiện được phép đưa thừa số ra ngoài dấu căn và đưa thừa số vào '
                        'trong dấu căn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho biểu thức $P = \\dfrac{1}{\\sqrt{3} - \\sqrt{2}} - \\dfrac{1}{\\sqrt{3} + \\sqrt{2}}$.',
            'statements': ['Biểu thức liên hợp của $\\sqrt{3} - \\sqrt{2}$ là $\\sqrt{3} + \\sqrt{2}$.',
                           'Ta có $(\\sqrt{3} - \\sqrt{2})(\\sqrt{3} + \\sqrt{2}) = 1$.',
                           'Trục căn thức ở mẫu ta được $\\dfrac{1}{\\sqrt{3} - \\sqrt{2}} = \\sqrt{3} + '
                           '\\sqrt{2}$.',
                           'Giá trị rút gọn của biểu thức $P$ bằng $2\\sqrt{3}$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $3 - 2 = 1$. c) Đúng. d) Sai vì $P = (\\sqrt{3} + \\sqrt{2}) - '
                        '(\\sqrt{3} - \\sqrt{2}) = 2\\sqrt{2}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 9: Biến đổi đơn giản và rút '
                 'gọn biểu thức chứa căn thức bậc hai**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thực hiện được phép đưa thừa số ra ngoài '
                           'dấu căn và đưa thừa số vào trong dấu căn.',
                           'Trong **Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức bậc hai**, '
                           'quy tắc/công thức **Đưa thừa số ra ngoài dấu căn** được viết là: $\\sqrt{A^2B} = '
                           '|A|\\sqrt{B}$ ($B \\ge 0$).',
                           'Nếu áp dụng sai dấu/phép tính thành $\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\le 0$) '
                           'thì kết quả của **Đưa thừa số ra ngoài dấu căn** trong **Bài 9: Biến đổi đơn '
                           'giản và rút gọn biểu thức chứa căn thức bậc hai** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Rút gọn biểu thức $A = 3\\sqrt{8} - \\sqrt{50} + '
                           '\\dfrac{2}{\\sqrt{2} - 1}$.”, kết quả giải đúng là: Ta có $3\\sqrt{8} = 3 \\cdot '
                           '2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; $\\dfrac{2}{\\sqrt{2} - 1} '
                           '= \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = 2\\sqrt{2} + 2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 9: Biến đổi đơn giản và rút gọn biểu thức '
                        'chứa căn thức bậc hai. b) **Đúng** theo công thức **Đưa thừa số ra ngoài dấu căn** '
                        '($\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 0$)). c) **Sai** vì công thức đúng của '
                        '**Đưa thừa số ra ngoài dấu căn** phải là $\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\ge 0$) '
                        'chứ không phải $\\sqrt{A^2B} = |A|\\sqrt{B}$ ($B \\le 0$). d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn '
                 'thức bậc hai** để giải bài toán sau: Rút gọn biểu thức $A = 3\\sqrt{8} - \\sqrt{50} + '
                 '\\dfrac{2}{\\sqrt{2} - 1}$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $3\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; '
                        '$\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} - 1)}{2 - 1} = 2\\sqrt{2} + 2$...',
                        'Ta có $3\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; '
                        '$\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = 2\\sqrt{2} + 1$...',
                        'Ta có $3\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; '
                        '$\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = 2\\sqrt{2} + 2$...',
                        'Ta có $6\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = 5\\sqrt{2}$; '
                        '$\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = 2\\sqrt{2} + 2$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 9: Biến đổi đơn giản và rút gọn biểu thức chứa căn thức '
                        'bậc hai: Ta có $3\\sqrt{8} = 3 \\cdot 2\\sqrt{2} = 6\\sqrt{2}$; $\\sqrt{50} = '
                        '5\\sqrt{2}$; $\\dfrac{2}{\\sqrt{2} - 1} = \\dfrac{2(\\sqrt{2} + 1)}{2 - 1} = '
                        '2\\sqrt{2} + 2$.\n'
                        'Do đó $A = 6\\sqrt{2} - 5\\sqrt{2} + 2\\sqrt{2} + 2 = 3\\sqrt{2} + 2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $S = \\dfrac{4}{\\sqrt{5} - 1} - \\sqrt{5}$.',
            'answer': ['1'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{4}{\\sqrt{5} - 1} = \\dfrac{4(\\sqrt{5} + 1)}{5 - 1} = \\sqrt{5} + '
                        '1$. Suy ra $S = \\sqrt{5} + 1 - \\sqrt{5} = 1$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch03-can-thuc',
  'context_title': 'Chương III: Căn bậc hai và căn bậc ba',
  'context': 'Chương III · SGK Toán 9: Căn bậc hai và căn bậc ba.',
  'title': 'Bài 10: Căn bậc ba và căn thức bậc ba',
  'icon': '🧊',
  'description': 'Nhận biết và tính căn bậc ba của một số thực, rút gọn biểu thức chứa căn thức bậc ba.',
  'requirements': ['Nhận biết được khái niệm căn bậc ba của một số thực và tính được bằng máy tính cầm tay.',
                   'Rút gọn được các biểu thức chứa căn thức bậc ba.',
                   'Vận dụng kiến thức của **Bài 10: Căn bậc ba và căn thức bậc ba** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Căn bậc ba của số thực $a$ là số thực $x$ thỏa mãn $x^3 = a$, kí hiệu là $\\sqrt[3]{a}$. '
                'Mỗi số thực $a$ đều có duy nhất một căn bậc ba.',
  'theory': '1. Với mọi số thực $a$, ta luôn có $(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$.\n'
            '2. Căn bậc ba của số dương là số dương, căn bậc ba của số âm là số âm, căn bậc ba của số $0$ là '
            'số $0$.\n'
            '3. Căn thức bậc ba $\\sqrt[3]{A}$ xác định với mọi giá trị của biến làm cho $A$ xác định (không '
            'cần điều kiện $A \\ge 0$).',
  'formulas': [{'category': 'Tính chất của căn bậc ba',
                'items': [{'name': 'Định nghĩa',
                           'formula': '$(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$',
                           'note': 'Đúng với mọi $a \\in \\mathbb{R}$'},
                          {'name': 'Căn bậc ba của tích và thương',
                           'formula': '$\\sqrt[3]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$; '
                                      '$\\sqrt[3]{\\dfrac{a}{b}} = \\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b '
                                      '\\neq 0$)',
                           'note': 'Áp dụng cho mọi số thực'}]}],
  'example': 'Tính giá trị của biểu thức $A = \\sqrt[3]{27} + \\sqrt[3]{-64} - \\sqrt[3]{8}$.',
  'example_answer': 'Ta có $\\sqrt[3]{27} = 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$.\n'
                    'Do đó $A = 3 + (-4) - 2 = -3$.',
  'real_life': 'Tính độ dài cạnh của một bể chứa nước hình lập phương khi biết thể tích $V$ theo công thức '
               '$a = \\sqrt[3]{V}$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Căn bậc ba của $-27$ là:',
            'options': ['$3$', '$-3$', '$-9$', 'Không tồn tại'],
            'answer': 1,
            'solution': 'Vì $(-3)^3 = -27$ nên $\\sqrt[3]{-27} = -3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biểu thức $\\sqrt[3]{8x^3}$ rút gọn bằng:',
            'options': ['$2|x|$', '$8x$', '$2x$', '$-2x$'],
            'answer': 2,
            'solution': 'Ta có $\\sqrt[3]{8x^3} = \\sqrt[3]{(2x)^3} = 2x$ với mọi số thực $x$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Căn bậc ba và căn thức bậc ba**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Định nghĩa**?',
            'options': ['$(\\sqrt[4]{a})^3 = \\sqrt[3]{a^3} = a$',
                        '$(\\sqrt[3]{a})^3 = \\sqrt[3]{a^2} = a$',
                        '$(\\sqrt[6]{a})^3 = \\sqrt[3]{a^3} = a$',
                        '$(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 10: Căn bậc ba và căn thức bậc ba, **Định nghĩa** '
                        'được xác định bởi: $(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$. (Đúng với mọi $a \\in '
                        '\\mathbb{R}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Căn bậc ba và căn thức bậc ba**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Căn bậc ba của tích và thương**?',
            'options': ['$\\sqrt[3]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$; $\\sqrt[3]{\\dfrac{a}{b}} = '
                        '\\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$)',
                        '$\\sqrt[3]{ab} = \\sqrt[3]{a} : \\sqrt[3]{b}$; $\\sqrt[3]{\\dfrac{a}{b}} = '
                        '\\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$)',
                        '$\\sqrt[3]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$; $\\sqrt[3]{\\dfrac{b}{a}} = '
                        '\\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$)',
                        '$\\sqrt[6]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$; $\\sqrt[3]{\\dfrac{a}{b}} = '
                        '\\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$)'],
            'answer': 0,
            'solution': 'Trong Bài 10: Căn bậc ba và căn thức bậc ba, **Căn bậc ba của tích và thương** có '
                        'công thức/quy tắc là: $\\sqrt[3]{ab} = \\sqrt[3]{a} \\cdot \\sqrt[3]{b}$; '
                        '$\\sqrt[3]{\\dfrac{a}{b}} = \\dfrac{\\sqrt[3]{a}}{\\sqrt[3]{b}}$ ($b \\neq 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nghiệm của phương trình $\\sqrt[3]{2x - 1} = -3$ là:',
            'options': ['$x = 14$', '$x = -13$', '$x = -4$', '$x = 5$'],
            'answer': 1,
            'solution': 'Lập phương hai vế: $2x - 1 = (-3)^3 = -27 \\Rightarrow 2x = -26 \\Rightarrow x = '
                        '-13$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 10: Căn bậc ba và căn thức bậc ba**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được khái niệm căn bậc ba của một số thực và tính được bằng máy tính cầm '
                        'tay. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được khái niệm căn bậc ba của một số thực và '
                        'tính được bằng máy tính cầm tay.',
                        'Nhận biết được khái niệm căn bậc ba của một số thực và tính được bằng máy tính cầm '
                        'tay.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được khái niệm căn '
                        'bậc ba của một số thực và tính được bằng máy tính cầm tay.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 10: Căn bậc ba và căn thức bậc ba: Nhận biết được '
                        'khái niệm căn bậc ba của một số thực và tính được bằng máy tính cầm tay.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét các mệnh đề về căn bậc ba:',
            'statements': ['Mọi số thực âm đều có căn bậc ba là một số thực âm.',
                           'Căn thức $\\sqrt[3]{x - 5}$ chỉ xác định khi $x \\ge 5$.',
                           'Giá trị của biểu thức $\\sqrt[3]{2} \\cdot \\sqrt[3]{4}$ bằng $2$.',
                           'Với mọi $a < b$, ta luôn có $\\sqrt[3]{a} < \\sqrt[3]{b}$.'],
            'answer': [True, False, True, True],
            'solution': 'a) Đúng. b) Sai vì căn bậc ba xác định với mọi $x \\in \\mathbb{R}$. c) Đúng vì '
                        '$\\sqrt[3]{2 \\cdot 4} = \\sqrt[3]{8} = 2$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 10: Căn bậc ba và căn thức '
                 'bậc ba**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được khái niệm căn bậc ba của '
                           'một số thực và tính được bằng máy tính cầm tay.',
                           'Trong **Bài 10: Căn bậc ba và căn thức bậc ba**, quy tắc/công thức **Định '
                           'nghĩa** được viết là: $(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$.',
                           'Nếu áp dụng sai dấu/phép tính thành $(\\sqrt[4]{a})^3 = \\sqrt[3]{a^3} = a$ thì '
                           'kết quả của **Định nghĩa** trong **Bài 10: Căn bậc ba và căn thức bậc ba** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Tính giá trị của biểu thức $A = \\sqrt[3]{27} + '
                           '\\sqrt[3]{-64} - \\sqrt[3]{8}$.”, kết quả giải đúng là: Ta có $\\sqrt[3]{27} = '
                           '3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$. Do đó $A = 3 + (-4) - 2 = -3$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 10: Căn bậc ba và căn thức bậc ba. b) '
                        '**Đúng** theo công thức **Định nghĩa** ($(\\sqrt[3]{a})^3 = \\sqrt[3]{a^3} = a$). '
                        'c) **Sai** vì công thức đúng của **Định nghĩa** phải là $(\\sqrt[3]{a})^3 = '
                        '\\sqrt[3]{a^3} = a$ chứ không phải $(\\sqrt[4]{a})^3 = \\sqrt[3]{a^3} = a$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 10: Căn bậc ba và căn thức bậc ba** để giải bài '
                 'toán sau: Tính giá trị của biểu thức $A = \\sqrt[3]{27} + \\sqrt[3]{-64} - \\sqrt[3]{8}$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $\\sqrt[3]{27} = 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$. Do đó $A = 3 '
                        '- (-4) - 2 = -3$.',
                        'Ta có $\\sqrt[3]{27} = 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$. Do đó $A = 3 '
                        '+ (-4) - 2 = -2$.',
                        'Ta có $\\sqrt[6]{27} = 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$. Do đó $A = 3 '
                        '+ (-4) - 2 = -3$.',
                        'Ta có $\\sqrt[3]{27} = 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$. Do đó $A = 3 '
                        '+ (-4) - 2 = -3$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 10: Căn bậc ba và căn thức bậc ba: Ta có $\\sqrt[3]{27} '
                        '= 3$; $\\sqrt[3]{-64} = -4$; $\\sqrt[3]{8} = 2$.\n'
                        'Do đó $A = 3 + (-4) - 2 = -3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khối lập phương có thể tích bằng $125\\text{ cm}^3$. Tính diện tích một mặt của khối '
                 'lập phương đó (đơn vị: $\\text{cm}^2$).',
            'answer': ['25'],
            'unit': None,
            'solution': 'Cạnh khối lập phương là $a = \\sqrt[3]{125} = 5$ (cm). Diện tích một mặt là $a^2 = '
                        '5^2 = 25$ ($\\text{cm}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch04-he-thuc-luong-tam-giac-vuong',
  'context_title': 'Chương IV: Hệ thức lượng trong tam giác vuông',
  'context': 'Chương IV · SGK Toán 9: Hệ thức lượng trong tam giác vuông.',
  'title': 'Bài 11: Tỉ số lượng giác của góc nhọn',
  'icon': '📐',
  'description': 'Định nghĩa sin, côsin, tang, côtang của góc nhọn và tỉ số lượng giác của hai góc phụ nhau.',
  'requirements': ['Nhận biết được các tỉ số lượng giác của góc nhọn ($\\sin, \\cos, \\tan, \\cot$) trong '
                   'tam giác vuông.',
                   'Nhớ bảng giá trị lượng giác của các góc đặc biệt $30^\\circ, 45^\\circ, 60^\\circ$.',
                   'Vận dụng được tính chất tỉ số lượng giác của hai góc phụ nhau.'],
  'definition': 'Trong một tam giác vuông, đối với góc nhọn $\\alpha$: $\\sin \\alpha$ là tỉ số giữa cạnh '
                'đối và cạnh huyền; $\\cos \\alpha$ là tỉ số giữa cạnh kề và cạnh huyền; $\\tan \\alpha$ là '
                'tỉ số giữa cạnh đối và cạnh kề; $\\cot \\alpha$ là tỉ số giữa cạnh kề và cạnh đối.',
  'theory': '1. Cho góc nhọn $\\alpha$, ta luôn có $0 < \\sin \\alpha < 1$, $0 < \\cos \\alpha < 1$, $\\tan '
            '\\alpha \\cdot \\cot \\alpha = 1$.\n'
            '2. Định lí về hai góc phụ nhau: Nếu hai góc phụ nhau (tổng số đo bằng $90^\\circ$) thì sin góc '
            'này bằng côsin góc kia, tang góc này bằng côtang góc kia.',
  'formulas': [{'category': 'Tỉ số lượng giác của góc nhọn $\\alpha$',
                'items': [{'name': 'Sin và Côsin',
                           'formula': '$\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; '
                                      '$\\cos \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$',
                           'note': '$0 < \\sin \\alpha, \\cos \\alpha < 1$'},
                          {'name': 'Tang và Côtang',
                           'formula': '$\\tan \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh kề}}$; $\\cot '
                                      '\\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh đối}}$',
                           'note': '$\\tan \\alpha \\cdot \\cot \\alpha = 1$'},
                          {'name': 'Hai góc phụ nhau ($\\alpha + \\beta = 90^\\circ$)',
                           'formula': '$\\sin \\alpha = \\cos \\beta$; $\\tan \\alpha = \\cot \\beta$',
                           'note': 'Ví dụ: $\\sin 30^\\circ = \\cos 60^\\circ = \\dfrac{1}{2}$'}]}],
  'example': 'Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ cm, $AC = 4$ cm. Tính các tỉ số lượng giác của '
             'góc $B$.',
  'example_answer': 'Theo định lí Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm).\n'
                    'Ta có: $\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                    '\\dfrac{3}{5}$; $\\tan B = \\dfrac{AC}{AB} = \\dfrac{4}{3}$; $\\cot B = \\dfrac{AB}{AC} '
                    '= \\dfrac{3}{4}$.',
  'real_life': 'Xác định độ dốc của con đường đèo hoặc góc nghiêng an toàn khi bắc thang dựa vào tường.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ vuông tại $A$. Tỉ số $\\sin B$ bằng:',
            'options': ['$\\dfrac{AB}{BC}$', '$\\dfrac{AC}{AB}$', '$\\dfrac{AC}{BC}$', '$\\dfrac{AB}{AC}$'],
            'answer': 2,
            'solution': 'Đối với góc $B$, cạnh đối là $AC$ và cạnh huyền là $BC$, nên $\\sin B = '
                        '\\dfrac{AC}{BC}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị của $\\sin 30^\\circ$ bằng:',
            'options': ['$\\dfrac{\\sqrt{3}}{2}$',
                        '$\\dfrac{\\sqrt{2}}{2}$',
                        '$\\sqrt{3}$',
                        '$\\dfrac{1}{2}$'],
            'answer': 3,
            'solution': 'Theo bảng giá trị lượng giác đặc biệt, $\\sin 30^\\circ = \\dfrac{1}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Tỉ số lượng giác của góc nhọn**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Sin và Côsin**?',
            'options': ['$\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$',
                        '$\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh '
                        'huyền}}$; $\\cos \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\sin \\alpha = '
                        '\\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: Tỉ số lượng giác của góc nhọn, **Sin và '
                        'Côsin** được xác định bởi: $\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh '
                        'huyền}}$; $\\cos \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$. ($0 < '
                        '\\sin \\alpha, \\cos \\alpha < 1$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Tỉ số lượng giác của góc nhọn**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Tang và Côtang**?',
            'options': ['$\\tan \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh kề}}$; $\\cot \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh đối}}$ (với dấu ngược lại)',
                        '$\\tan \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh kề}}$; $\\cot \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh đối}}$',
                        'Đảo ngược vế của quy tắc: $\\tan \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh '
                        'kề}}$; $\\cot \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh đối}}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\tan \\alpha = '
                        '\\dfrac{\\text{Cạnh đối}}{\\text{Cạnh kề}}$; $\\cot \\alpha = \\dfrac{\\text{Cạnh '
                        'kề}}{\\text{Cạnh đối}}$'],
            'answer': 1,
            'solution': 'Trong Bài 11: Tỉ số lượng giác của góc nhọn, **Tang và Côtang** có công thức/quy '
                        'tắc là: $\\tan \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh kề}}$; $\\cot '
                        '\\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh đối}}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho hai góc nhọn $\\alpha$ và $\\beta$ phụ nhau ($\\alpha + \\beta = 90^\\circ$). Khẳng '
                 'định nào sau đây là sai?',
            'options': ['$\\sin \\alpha = \\cos \\beta$',
                        '$\\tan \\alpha = \\cot \\beta$',
                        '$\\sin \\alpha = \\sin \\beta$',
                        '$\\cos \\alpha = \\sin \\beta$'],
            'answer': 2,
            'solution': 'Hai góc phụ nhau thì sin góc này bằng côsin góc kia, không phải $\\sin \\alpha = '
                        '\\sin \\beta$ (trừ khi $\\alpha = \\beta = 45^\\circ$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: Tỉ số lượng giác của góc nhọn**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết được các tỉ số lượng giác của góc nhọn ($\\sin, \\cos, \\tan, \\cot$) '
                        'trong tam giác vuông. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được các tỉ số lượng giác của góc nhọn ($\\sin, '
                        '\\cos, \\tan, \\cot$) trong tam giác vuông.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được các tỉ số lượng '
                        'giác của góc nhọn ($\\sin, \\cos, \\tan, \\cot$) trong tam giác vuông.',
                        'Nhận biết được các tỉ số lượng giác của góc nhọn ($\\sin, \\cos, \\tan, \\cot$) '
                        'trong tam giác vuông.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 11: Tỉ số lượng giác của góc nhọn: Nhận biết được các '
                        'tỉ số lượng giác của góc nhọn ($\\sin, \\cos, \\tan, \\cot$) trong tam giác vuông.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$ cm, $AC = 8$ cm, $BC = 10$ cm.',
            'statements': ['$\\sin C = \\dfrac{3}{5}$.',
                           '$\\tan B = \\dfrac{4}{3}$.',
                           '$\\cos B = \\sin C$.',
                           '$\\tan B + \\cot B = 1$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $\\sin C = \\dfrac{AB}{BC} = \\dfrac{6}{10} = \\dfrac{3}{5}$. b) Đúng vì '
                        '$\\tan B = \\dfrac{AC}{AB} = \\dfrac{8}{6} = \\dfrac{4}{3}$. c) Đúng vì $B$ và $C$ '
                        'phụ nhau. d) Sai vì $\\tan B \\cdot \\cot B = 1$, còn $\\tan B + \\cot B = '
                        '\\dfrac{4}{3} + \\dfrac{3}{4} = \\dfrac{25}{12}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 11: Tỉ số lượng giác của '
                 'góc nhọn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được các tỉ số lượng giác của '
                           'góc nhọn ($\\sin, \\cos, \\tan, \\cot$) trong tam giác vuông.',
                           'Trong **Bài 11: Tỉ số lượng giác của góc nhọn**, quy tắc/công thức **Sin và '
                           'Côsin** được viết là: $\\sin \\alpha = \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh '
                           'huyền}}$; $\\cos \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\sin \\alpha = \\dfrac{\\text{Cạnh '
                           'đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = \\dfrac{\\text{Cạnh '
                           'kề}}{\\text{Cạnh huyền}}$ (với dấu ngược lại) thì kết quả của **Sin và Côsin** '
                           'trong **Bài 11: Tỉ số lượng giác của góc nhọn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ cm, $AC = 4$ '
                           'cm. Tính các tỉ số lượng giác của góc $B$.”, kết quả giải đúng là: Theo định lí '
                           'Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Ta có: '
                           '$\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                           '\\dfrac{3}{5}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 11: Tỉ số lượng giác của góc nhọn. b) '
                        '**Đúng** theo công thức **Sin và Côsin** ($\\sin \\alpha = \\dfrac{\\text{Cạnh '
                        'đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = \\dfrac{\\text{Cạnh kề}}{\\text{Cạnh '
                        'huyền}}$). c) **Sai** vì công thức đúng của **Sin và Côsin** phải là $\\sin \\alpha '
                        '= \\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$ chứ không phải $\\sin \\alpha = '
                        '\\dfrac{\\text{Cạnh đối}}{\\text{Cạnh huyền}}$; $\\cos \\alpha = '
                        '\\dfrac{\\text{Cạnh kề}}{\\text{Cạnh huyền}}$ (với dấu ngược lại). d) **Đúng** theo '
                        'lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: Tỉ số lượng giác của góc nhọn** để giải bài '
                 'toán sau: Cho tam giác $ABC$ vuông tại $A$ có $AB = 3$ cm, $AC = 4$ cm. Tính các tỉ số '
                 'lượng giác của góc $B$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Theo định lí Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Ta '
                        'có: $\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                        '\\dfrac{3}{5}$...',
                        'Theo định lí Pythagore: $BC = \\sqrt{AB^2 - AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Ta '
                        'có: $\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                        '\\dfrac{3}{5}$...',
                        'Theo định lí Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Ta '
                        'có: $\\sin B = \\dfrac{BC}{AC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                        '\\dfrac{3}{5}$...',
                        'Theo định lí Pythagore: $BC = \\sqrt{AB^4 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Ta '
                        'có: $\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                        '\\dfrac{3}{5}$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 11: Tỉ số lượng giác của góc nhọn: Theo định lí '
                        'Pythagore: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{3^2 + 4^2} = 5$ (cm).\n'
                        'Ta có: $\\sin B = \\dfrac{AC}{BC} = \\dfrac{4}{5}$; $\\cos B = \\dfrac{AB}{BC} = '
                        '\\dfrac{3}{5}$; $\\tan B = \\dfrac{AC}{AB} = \\dfrac{4}{3}$; $\\cot B = '
                        '\\dfrac{AB}{AC} = \\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tính giá trị của biểu thức $M = \\sin 35^\\circ - \\cos 55^\\circ + \\tan 45^\\circ$.',
            'answer': ['1'],
            'unit': None,
            'solution': 'Vì $35^\\circ + 55^\\circ = 90^\\circ$ nên $\\sin 35^\\circ = \\cos 55^\\circ$. Do '
                        'đó $M = 0 + \\tan 45^\\circ = 1$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch04-he-thuc-luong-tam-giac-vuong',
  'context_title': 'Chương IV: Hệ thức lượng trong tam giác vuông',
  'context': 'Chương IV · SGK Toán 9: Hệ thức lượng trong tam giác vuông.',
  'title': 'Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng',
  'icon': '🗼',
  'description': 'Biểu diễn cạnh góc vuông theo cạnh huyền hoặc cạnh góc vuông còn lại và giải tam giác '
                 'vuông.',
  'requirements': ['Thiết lập và vận dụng được các hệ thức giữa cạnh và góc trong tam giác vuông.',
                   'Giải được tam giác vuông và ứng dụng vào đo chiều cao, khoảng cách thực tế.',
                   'Vận dụng kiến thức của **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và '
                   'ứng dụng** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh huyền nhân với sin góc đối hoặc nhân với '
                'côsin góc kề; mỗi cạnh góc vuông bằng cạnh góc vuông kia nhân với tang góc đối hoặc nhân '
                'với côtang góc kề.',
  'theory': '1. Cho tam giác $ABC$ vuông tại $A$ có cạnh huyền $a = BC$, hai cạnh góc vuông $b = AC, c = '
            'AB$:\n'
            '- $b = a \\cdot \\sin B = a \\cdot \\cos C$; $c = a \\cdot \\sin C = a \\cdot \\cos B$.\n'
            '- $b = c \\cdot \\tan B = c \\cdot \\cot C$; $c = b \\cdot \\tan C = b \\cdot \\cot B$.\n'
            '2. Giải tam giác vuông là tìm tất cả các cạnh và các góc chưa biết của tam giác vuông khi biết '
            'hai yếu tố (trong đó có ít nhất một cạnh).',
  'formulas': [{'category': 'Hệ thức giữa cạnh và góc trong $\\triangle ABC$ vuông tại $A$',
                'items': [{'name': 'Tính theo cạnh huyền $a$',
                           'formula': '$b = a \\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$',
                           'note': 'Cạnh góc vuông = Cạnh huyền $\\times$ sin góc đối (hoặc cos góc kề)'},
                          {'name': 'Tính theo cạnh góc vuông kia',
                           'formula': '$b = c \\tan B = c \\cot C$; $c = b \\tan C = b \\cot B$',
                           'note': 'Cạnh góc vuông = Cạnh kia $\\times$ tan góc đối (hoặc cot góc kề)'}]}],
  'example': 'Một chiếc thang dài $4$ m đặt dựa vào tường sao cho góc giữa thang và mặt đất bằng '
             '$60^\\circ$. Tính khoảng cách từ chân thang đến chân tường.',
  'example_answer': 'Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc $60^\\circ$: $d = '
                    '4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = 2$ (m).',
  'real_life': 'Đo chiều cao của tháp, tòa nhà hoặc cây cổ thụ thông qua chiều dài bóng nắng và góc tạo bởi '
               'tia nắng mặt trời với mặt đất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có $BC = a, AC = b, AB = c$. Hệ thức nào sau đây là đúng?',
            'options': ['$b = a \\cdot \\tan B$',
                        '$b = c \\cdot \\sin B$',
                        '$c = a \\cdot \\tan C$',
                        '$b = a \\cdot \\sin B$'],
            'answer': 3,
            'solution': 'Cạnh góc vuông $b = AC$ bằng cạnh huyền $a = BC$ nhân với $\\sin$ của góc đối $B$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có $AB = 10$ cm và $\\widehat{B} = 45^\\circ$. Độ dài '
                 'cạnh $AC$ bằng:',
            'options': ['$10$ cm', '$10\\sqrt{2}$ cm', '$5$ cm', '$5\\sqrt{2}$ cm'],
            'answer': 0,
            'solution': 'Ta có $AC = AB \\cdot \\tan B = 10 \\cdot \\tan 45^\\circ = 10 \\cdot 1 = 10$ (cm).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Tính theo cạnh huyền $a$**?',
            'options': ['$b = a \\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$ (với dấu ngược lại)',
                        '$b = a \\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$',
                        'Đảo ngược vế của quy tắc: $b = a \\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $b = a \\sin B = a \\cos C$; $c '
                        '= a \\sin C = a \\cos B$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác '
                        'vuông và ứng dụng, **Tính theo cạnh huyền $a$** được xác định bởi: $b = a \\sin B = '
                        'a \\cos C$; $c = a \\sin C = a \\cos B$. (Cạnh góc vuông = Cạnh huyền $\\times$ sin '
                        'góc đối (hoặc cos góc kề))'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tính theo cạnh góc vuông kia**?',
            'options': ['$b = c \\tan B = c \\cot C$; $c = b \\tan C = b \\cot B$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $b = c \\tan B = c \\cot C$; $c = b \\tan C = b \\cot B$',
                        '$b = c \\tan B = c \\cot C$; $c = b \\tan C = b \\cot B$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $b = c \\tan B = c \\cot C$; $c '
                        '= b \\tan C = b \\cot B$'],
            'answer': 2,
            'solution': 'Trong Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng, '
                        '**Tính theo cạnh góc vuông kia** có công thức/quy tắc là: $b = c \\tan B = c \\cot '
                        'C$; $c = b \\tan C = b \\cot B$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Tia nắng mặt trời tạo với mặt đất một góc $60^\\circ$ và bóng của một cột cờ trên mặt đất '
                 'dài $6$ m. Chiều cao của cột cờ bằng:',
            'options': ['$3\\sqrt{3}$ m', '$2\\sqrt{3}$ m', '$12$ m', '$6\\sqrt{3}$ m'],
            'answer': 3,
            'solution': 'Chiều cao cột cờ là $h = 6 \\cdot \\tan 60^\\circ = 6\\sqrt{3}$ (m).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và '
                 'ứng dụng**, nhận định nào sau đây là **chính xác**?',
            'options': ['Thiết lập và vận dụng được các hệ thức giữa cạnh và góc trong tam giác vuông.',
                        'Thiết lập và vận dụng được các hệ thức giữa cạnh và góc trong tam giác vuông. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thiết lập và vận dụng được các hệ thức giữa cạnh và góc '
                        'trong tam giác vuông.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thiết lập và vận dụng được các '
                        'hệ thức giữa cạnh và góc trong tam giác vuông.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác '
                        'vuông và ứng dụng: Thiết lập và vận dụng được các hệ thức giữa cạnh và góc trong '
                        'tam giác vuông.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có cạnh huyền $BC = 12$ cm và $\\widehat{B} = 30^\\circ$.',
            'statements': ['Số đo góc $C$ bằng $60^\\circ$.',
                           'Độ dài cạnh $AC = 6$ cm.',
                           'Độ dài cạnh $AB = 6\\sqrt{3}$ cm.',
                           'Diện tích tam giác $ABC$ bằng $36\\sqrt{3}\\text{ cm}^2$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ$. b) Đúng vì $AC = BC '
                        '\\cdot \\sin 30^\\circ = 6$ cm. c) Đúng vì $AB = BC \\cdot \\cos 30^\\circ = '
                        '6\\sqrt{3}$ cm. d) Sai vì $S = \\dfrac{1}{2} AB \\cdot AC = 18\\sqrt{3}\\text{ '
                        'cm}^2$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 12: Một số hệ thức giữa '
                 'cạnh, góc trong tam giác vuông và ứng dụng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Thiết lập và vận dụng được các hệ thức '
                           'giữa cạnh và góc trong tam giác vuông.',
                           'Trong **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng '
                           'dụng**, quy tắc/công thức **Tính theo cạnh huyền $a$** được viết là: $b = a '
                           '\\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$.',
                           'Nếu áp dụng sai dấu/phép tính thành $b = a \\sin B = a \\cos C$; $c = a \\sin C '
                           '= a \\cos B$ (với dấu ngược lại) thì kết quả của **Tính theo cạnh huyền $a$** '
                           'trong **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông và ứng dụng** '
                           'vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một chiếc thang dài $4$ m đặt dựa vào tường sao cho góc giữa '
                           'thang và mặt đất bằng $60^\\circ$. Tính khoảng cách từ chân thang đến chân...”, '
                           'kết quả giải đúng là: Khoảng cách từ chân thang đến chân tường là cạnh góc vuông '
                           'kề với góc $60^\\circ$: $d = 4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = '
                           '2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 12: Một số hệ thức giữa cạnh, góc trong '
                        'tam giác vuông và ứng dụng. b) **Đúng** theo công thức **Tính theo cạnh huyền $a$** '
                        '($b = a \\sin B = a \\cos C$; $c = a \\sin C = a \\cos B$). c) **Sai** vì công thức '
                        'đúng của **Tính theo cạnh huyền $a$** phải là $b = a \\sin B = a \\cos C$; $c = a '
                        '\\sin C = a \\cos B$ chứ không phải $b = a \\sin B = a \\cos C$; $c = a \\sin C = a '
                        '\\cos B$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác '
                 'vuông và ứng dụng** để giải bài toán sau: Một chiếc thang dài $4$ m đặt dựa vào tường sao '
                 'cho góc giữa thang và mặt đất bằng $60^\\circ$. Tính khoảng cách từ chân thang đến chân '
                 'tường. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc $60^\\circ$: '
                        '$d = 4 : \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = 2$ (m).',
                        'Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc $60^\\circ$: '
                        '$d = 4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = 2$ (m).',
                        'Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc $60^\\circ$: '
                        '$d = 4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{2}{1} = 2$ (m).',
                        'Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc $62^\\circ$: '
                        '$d = 4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = 2$ (m).'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 12: Một số hệ thức giữa cạnh, góc trong tam giác vuông '
                        'và ứng dụng: Khoảng cách từ chân thang đến chân tường là cạnh góc vuông kề với góc '
                        '$60^\\circ$: $d = 4 \\cdot \\cos 60^\\circ = 4 \\cdot \\dfrac{1}{2} = 2$ (m).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một máy bay cất cánh theo phương hợp với mặt đất một góc $30^\\circ$. Sau khi bay được '
                 'quãng đường $10$ km thì máy bay đạt độ cao bao nhiêu kilômét so với mặt đất?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Độ cao máy bay đạt được là $h = 10 \\cdot \\sin 30^\\circ = 10 \\cdot \\dfrac{1}{2} '
                        '= 5$ (km).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch05-duong-tron',
  'context_title': 'Chương V: Đường tròn',
  'context': 'Chương V · SGK Toán 9: Đường tròn.',
  'title': 'Bài 13: Mở đầu về đường tròn',
  'icon': '⭕',
  'description': 'Nhận biết đường tròn, vị trí của điểm đối với đường tròn và tính đối xứng của đường tròn.',
  'requirements': ['Nhận biết được đường tròn $(O; R)$ và xác định được vị trí tương đối của một điểm đối '
                   'với đường tròn.',
                   'Nhận biết được tâm đối xứng và trục đối xứng của đường tròn.',
                   'Vận dụng kiến thức của **Bài 13: Mở đầu về đường tròn** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': 'Đường tròn tâm $O$ bán kính $R$ ($R > 0$), kí hiệu là $(O; R)$, là hình gồm tất cả các điểm '
                'cách điểm $O$ một khoảng bằng $R$.',
  'theory': '1. Cho đường tròn $(O; R)$ và điểm $M$:\n'
            '- Điểm $M$ nằm trên đường tròn $\\Leftrightarrow OM = R$.\n'
            '- Điểm $M$ nằm trong đường tròn $\\Leftrightarrow OM < R$.\n'
            '- Điểm $M$ nằm ngoài đường tròn $\\Leftrightarrow OM > R$.\n'
            '2. Đường tròn là hình có tâm đối xứng (tâm $O$) và có vô số trục đối xứng (bất kì đường kính '
            'nào cũng là trục đối xứng).',
  'formulas': [{'category': 'Vị trí điểm $M$ đối với đường tròn $(O; R)$',
                'items': [{'name': 'Điểm thuộc đường tròn', 'formula': '$OM = R$', 'note': '$M \\in (O; R)$'},
                          {'name': 'Điểm nằm trong và ngoài',
                           'formula': '$OM < R$ (trong); $OM > R$ (ngoài)',
                           'note': 'So sánh khoảng cách $OM$ với bán kính $R$'}]}],
  'example': 'Cho hình chữ nhật $ABCD$ có $AB = 6$ cm, $BC = 8$ cm. Chứng minh bốn điểm $A, B, C, D$ cùng '
             'thuộc một đường tròn và tính bán kính đường tròn đó.',
  'example_answer': 'Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên $OA = '
                    'OB = OC = OD = \\dfrac{AC}{2}$.\n'
                    'Theo định lí Pythagore: $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{6^2 + 8^2} = 10$ (cm).\n'
                    'Vậy bốn điểm $A, B, C, D$ cùng thuộc đường tròn $(O; 5\\text{ cm})$.',
  'real_life': 'Xác định vùng phủ sóng của trạm phát Wi-Fi hoặc radar trong phạm vi bán kính $R$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường tròn $(O; 5\\text{ cm})$ và điểm $M$ cách $O$ một khoảng $4$ cm. Vị trí của điểm '
                 '$M$ đối với đường tròn $(O)$ là:',
            'options': ['Nằm trong đường tròn',
                        'Nằm trên đường tròn',
                        'Nằm ngoài đường tròn',
                        'Trùng với tâm $O$'],
            'answer': 0,
            'solution': 'Vì $OM = 4\\text{ cm} < R = 5\\text{ cm}$ nên điểm $M$ nằm trong đường tròn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một đường tròn có bao nhiêu trục đối xứng?',
            'options': ['$1$', 'Vô số', '$2$', '$4$'],
            'answer': 1,
            'solution': 'Mọi đường thẳng đi qua tâm của đường tròn đều là trục đối xứng, nên đường tròn có '
                        'vô số trục đối xứng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Mở đầu về đường tròn**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Điểm thuộc đường tròn**?',
            'options': ['$OM = R$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $OM = R$',
                        '$OM = R$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $OM = R$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Mở đầu về đường tròn, **Điểm thuộc đường '
                        'tròn** được xác định bởi: $OM = R$. ($M \\in (O; R)$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Mở đầu về đường tròn**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Điểm nằm trong và ngoài**?',
            'options': ['$OM < R$ (trong); $OM < R$ (ngoài)',
                        'Đảo ngược vế của quy tắc: $OM < R$ (trong); $OM > R$ (ngoài)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $OM < R$ (trong); $OM > R$ '
                        '(ngoài)',
                        '$OM < R$ (trong); $OM > R$ (ngoài)'],
            'answer': 3,
            'solution': 'Trong Bài 13: Mở đầu về đường tròn, **Điểm nằm trong và ngoài** có công thức/quy '
                        'tắc là: $OM < R$ (trong); $OM > R$ (ngoài).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có cạnh huyền $BC = 10$ cm. Bán kính đường tròn đi qua ba '
                 'đỉnh $A, B, C$ bằng:',
            'options': ['$5$ cm', '$10$ cm', '$2,5$ cm', '$5\\sqrt{2}$ cm'],
            'answer': 0,
            'solution': 'Tâm đường tròn đi qua ba đỉnh của tam giác vuông là trung điểm cạnh huyền, nên bán '
                        'kính $R = \\dfrac{BC}{2} = 5$ cm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Mở đầu về đường tròn**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được đường tròn $(O; R)$ và xác định được vị trí tương đối của một điểm '
                        'đối với đường tròn. (với dấu ngược lại)',
                        'Nhận biết được đường tròn $(O; R)$ và xác định được vị trí tương đối của một điểm '
                        'đối với đường tròn.',
                        'Đảo ngược vế của quy tắc: Nhận biết được đường tròn $(O; R)$ và xác định được vị '
                        'trí tương đối của một điểm đối với đường tròn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được đường tròn $(O; '
                        'R)$ và xác định được vị trí tương đối của một điểm đối với đường tròn.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Mở đầu về đường tròn: Nhận biết được đường tròn '
                        '$(O; R)$ và xác định được vị trí tương đối của một điểm đối với đường tròn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $(O; 5)$ với $O$ là gốc tọa độ và điểm $A(3; '
                 '4)$.',
            'statements': ['Khoảng cách từ gốc tọa độ $O$ đến điểm $A$ là $OA = 5$.',
                           'Điểm $A(3; 4)$ nằm trên đường tròn $(O; 5)$.',
                           'Điểm $B(-3; 4)$ nằm ngoài đường tròn $(O; 5)$.',
                           'Điểm $C(3; -4)$ đối xứng với điểm $A$ qua trục hoành và cũng thuộc đường tròn '
                           '$(O; 5)$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $OA = \\sqrt{3^2 + 4^2} = 5$. b) Đúng vì $OA = R = 5$. c) Sai vì $OB = '
                        '\\sqrt{(-3)^2 + 4^2} = 5 = R$ nên $B$ thuộc đường tròn. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 13: Mở đầu về đường tròn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đường tròn $(O; R)$ và '
                           'xác định được vị trí tương đối của một điểm đối với đường tròn.',
                           'Trong **Bài 13: Mở đầu về đường tròn**, quy tắc/công thức **Điểm thuộc đường '
                           'tròn** được viết là: $OM = R$.',
                           'Nếu áp dụng sai dấu/phép tính thành $OM = R$ (với dấu ngược lại) thì kết quả của '
                           '**Điểm thuộc đường tròn** trong **Bài 13: Mở đầu về đường tròn** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Cho hình chữ nhật $ABCD$ có $AB = 6$ cm, $BC = 8$ cm. Chứng '
                           'minh bốn điểm $A, B, C, D$ cùng thuộc một đường tròn và tính bán kính đường...”, '
                           'kết quả giải đúng là: Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì '
                           '$ABCD$ là hình chữ nhật nên $OA = OB = OC = OD = \\dfrac{AC}{2}$. Theo định lí '
                           'Pyth...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 13: Mở đầu về đường tròn. b) **Đúng** theo '
                        'công thức **Điểm thuộc đường tròn** ($OM = R$). c) **Sai** vì công thức đúng của '
                        '**Điểm thuộc đường tròn** phải là $OM = R$ chứ không phải $OM = R$ (với dấu ngược '
                        'lại). d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Mở đầu về đường tròn** để giải bài toán sau: '
                 'Cho hình chữ nhật $ABCD$ có $AB = 6$ cm, $BC = 8$ cm. Chứng minh bốn điểm $A, B, C, D$ '
                 'cùng thuộc một đường tròn và tính bán kính đường tròn đó. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên '
                        '$OA = OB = OC = OD = \\dfrac{AC}{2}$. Theo định lí Pythagore: $AC = \\sqrt{AB^2 - '
                        'BC^2} = \\sqrt{6^2 + 8^2} = 10$...',
                        'Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên '
                        '$OA = OB = OC = OD = \\dfrac{2}{AC}$. Theo định lí Pythagore: $AC = \\sqrt{AB^2 + '
                        'BC^2} = \\sqrt{6^2 + 8^2} = 10$...',
                        'Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên '
                        '$OA = OB = OC = OD = \\dfrac{AC}{2}$. Theo định lí Pythagore: $AC = \\sqrt{AB^2 + '
                        'BC^2} = \\sqrt{6^2 + 8^2} = 10$...',
                        'Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên '
                        '$OA = OB = OC = OD = \\dfrac{AC}{4}$. Theo định lí Pythagore: $AC = \\sqrt{AB^2 + '
                        'BC^2} = \\sqrt{6^2 + 8^2} = 10$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 13: Mở đầu về đường tròn: Gọi $O$ là giao điểm hai đường '
                        'chéo $AC$ và $BD$. Vì $ABCD$ là hình chữ nhật nên $OA = OB = OC = OD = '
                        '\\dfrac{AC}{2}$.\n'
                        'Theo định lí Pythagore: $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{6^2 + 8^2} = 10$ (cm).\n'
                        'Vậy bốn điểm $A, B, C, D$ cùng thuộc đường tròn $(O; 5\\text{ cm})$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho hình vuông $ABCD$ có cạnh bằng $4\\sqrt{2}$ cm. Tính bán kính đường tròn đi qua bốn '
                 'đỉnh của hình vuông đó (đơn vị: cm).',
            'answer': ['4'],
            'unit': None,
            'solution': 'Đường chéo hình vuông là $AC = 4\\sqrt{2} \\cdot \\sqrt{2} = 8$ (cm). Bán kính '
                        'đường tròn là $R = \\dfrac{AC}{2} = 4$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch05-duong-tron',
  'context_title': 'Chương V: Đường tròn',
  'context': 'Chương V · SGK Toán 9: Đường tròn.',
  'title': 'Bài 14: Cung và dây của một đường tròn',
  'icon': '🏹',
  'description': 'Nhận biết dây, đường kính, góc ở tâm, số đo cung và mối liên hệ giữa đường kính và dây.',
  'requirements': ['So sánh được độ dài của đường kính và dây của đường tròn.',
                   'Nhận biết được góc ở tâm, cung tròn và cách tính số đo của cung tròn.',
                   'Vận dụng kiến thức của **Bài 14: Cung và dây của một đường tròn** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Đoạn thẳng nối hai điểm trên đường tròn gọi là dây (dây cung). Dây đi qua tâm là đường '
                'kính. Góc ở tâm là góc có đỉnh trùng với tâm của đường tròn.',
  'theory': '1. Trong một đường tròn, đường kính là dây lớn nhất: Nếu $AB$ là một dây bất kì của $(O; R)$ '
            'thì $AB \\le 2R$.\n'
            '2. Số đo của cung nhỏ bằng số đo của góc ở tâm chắn cung đó. Số đo của cung lớn bằng hiệu giữa '
            '$360^\\circ$ và số đo của cung nhỏ.\n'
            '3. Quan hệ vuông góc giữa đường kính và dây: Đường kính vuông góc với một dây thì đi qua trung '
            'điểm của dây ấy.',
  'formulas': [{'category': 'Dây cung và góc ở tâm',
                'items': [{'name': 'Bất đẳng thức dây cung',
                           'formula': '$AB \\le 2R$',
                           'note': 'Đường kính là dây lớn nhất của đường tròn'},
                          {'name': 'Đường kính vuông góc với dây',
                           'formula': '$OI \\perp AB \\Rightarrow IA = IB = \\dfrac{AB}{2}$',
                           'note': '$R^2 = OI^2 + \\left(\\dfrac{AB}{2}\\right)^2$'},
                          {'name': 'Số đo cung',
                           'formula': '$\\text{sđ}\\overset{\\frown}{AB}_{\\text{nhỏ}} = \\widehat{AOB}$',
                           'note': '$\\text{sđ}\\overset{\\frown}{AB}_{\\text{lớn}} = 360^\\circ - '
                                   '\\text{sđ}\\overset{\\frown}{AB}_{\\text{nhỏ}}$'}]}],
  'example': 'Cho đường tròn $(O; 13\\text{ cm})$ và dây $AB = 24$ cm. Tính khoảng cách từ tâm $O$ đến dây '
             '$AB$.',
  'example_answer': 'Kẻ $OH \\perp AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = \\dfrac{AB}{2} = '
                    '12$ (cm).\n'
                    'Áp dụng định lí Pythagore trong tam giác vuông $OAH$: $OH = \\sqrt{OA^2 - AH^2} = '
                    '\\sqrt{13^2 - 12^2} = 5$ (cm).',
  'real_life': 'Tính khẩu độ và chiều cao của nhịp cầu vòm bắc qua sông dựa vào bán kính cung tròn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một đường tròn có bán kính $R = 6$ cm, độ dài của dây lớn nhất bằng:',
            'options': ['$6$ cm', '$12$ cm', '$3$ cm', '$6\\sqrt{2}$ cm'],
            'answer': 1,
            'solution': 'Dây lớn nhất là đường kính có độ dài $2R = 2 \\cdot 6 = 12$ cm.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường tròn $(O)$ và hai điểm $A, B$ trên đường tròn sao cho $\\widehat{AOB} = '
                 '80^\\circ$. Số đo của cung lớn $AB$ bằng:',
            'options': ['$80^\\circ$', '$100^\\circ$', '$280^\\circ$', '$160^\\circ$'],
            'answer': 2,
            'solution': 'Số đo cung nhỏ $AB$ là $80^\\circ$, nên số đo cung lớn $AB$ là $360^\\circ - '
                        '80^\\circ = 280^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Cung và dây của một đường tròn**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Bất đẳng thức dây cung**?',
            'options': ['$AB \\ge 2R$',
                        'Đảo ngược vế của quy tắc: $AB \\le 2R$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $AB \\le 2R$',
                        '$AB \\le 2R$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 14: Cung và dây của một đường tròn, **Bất đẳng '
                        'thức dây cung** được xác định bởi: $AB \\le 2R$. (Đường kính là dây lớn nhất của '
                        'đường tròn)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Cung và dây của một đường tròn**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Đường kính vuông góc với dây**?',
            'options': ['$OI \\perp AB \\Rightarrow IA = IB = \\dfrac{AB}{2}$',
                        '$OI \\perp AB \\Rightarrow IA = IB = \\dfrac{AB}{3}$',
                        '$OI \\perp AB \\Rightarrow IA = IB = \\dfrac{2}{AB}$',
                        '$OI \\perp AB \\Rightarrow IA = IB = \\dfrac{AB}{4}$'],
            'answer': 0,
            'solution': 'Trong Bài 14: Cung và dây của một đường tròn, **Đường kính vuông góc với dây** có '
                        'công thức/quy tắc là: $OI \\perp AB \\Rightarrow IA = IB = \\dfrac{AB}{2}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho đường tròn $(O; 5\\text{ cm})$, khoảng cách từ tâm $O$ đến dây $AB$ bằng $3$ cm. Độ '
                 'dài dây $AB$ bằng:',
            'options': ['$4$ cm', '$8$ cm', '$6$ cm', '$10$ cm'],
            'answer': 1,
            'solution': 'Gọi $H$ là hình chiếu của $O$ trên $AB$, ta có $AH = \\sqrt{5^2 - 3^2} = 4$ cm '
                        '$\\Rightarrow AB = 2AH = 8$ cm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 14: Cung và dây của một đường tròn**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['So sánh được độ dài của đường kính và dây của đường tròn. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: So sánh được độ dài của đường kính và dây của đường tròn.',
                        'So sánh được độ dài của đường kính và dây của đường tròn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của So sánh được độ dài của đường '
                        'kính và dây của đường tròn.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 14: Cung và dây của một đường tròn: So sánh được độ '
                        'dài của đường kính và dây của đường tròn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đường tròn $(O; 10\\text{ cm})$ và dây $CD = 16$ cm. Gọi $M$ là trung điểm của dây '
                 '$CD$.',
            'statements': ['Đường thẳng $OM$ vuông góc với dây $CD$ tại $M$.',
                           'Độ dài đoạn thẳng $OM$ bằng $6$ cm.',
                           'Tam giác $OCD$ là tam giác đều.',
                           'Khoảng cách từ $M$ đến điểm chính giữa của cung nhỏ $CD$ bằng $4$ cm.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $OD = OC$ và $MD = MC$. b) Đúng vì $OM = \\sqrt{10^2 - 8^2} = 6$ cm. c) '
                        'Sai vì $CD = 16 \\neq OC = 10$. d) Đúng vì độ dài đoạn nối là $R - OM = 10 - 6 = 4$ '
                        'cm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 14: Cung và dây của một '
                 'đường tròn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: So sánh được độ dài của đường kính và '
                           'dây của đường tròn.',
                           'Trong **Bài 14: Cung và dây của một đường tròn**, quy tắc/công thức **Bất đẳng '
                           'thức dây cung** được viết là: $AB \\le 2R$.',
                           'Nếu áp dụng sai dấu/phép tính thành $AB \\ge 2R$ thì kết quả của **Bất đẳng thức '
                           'dây cung** trong **Bài 14: Cung và dây của một đường tròn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho đường tròn $(O; 13\\text{ cm})$ và dây $AB = 24$ cm. '
                           'Tính khoảng cách từ tâm $O$ đến dây $AB$.”, kết quả giải đúng là: Kẻ $OH \\perp '
                           'AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = \\dfrac{AB}{2} = 12$ '
                           '(cm). Áp dụng định lí Pythagore trong tam giá...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 14: Cung và dây của một đường tròn. b) '
                        '**Đúng** theo công thức **Bất đẳng thức dây cung** ($AB \\le 2R$). c) **Sai** vì '
                        'công thức đúng của **Bất đẳng thức dây cung** phải là $AB \\le 2R$ chứ không phải '
                        '$AB \\ge 2R$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 14: Cung và dây của một đường tròn** để giải bài '
                 'toán sau: Cho đường tròn $(O; 13\\text{ cm})$ và dây $AB = 24$ cm. Tính khoảng cách từ tâm '
                 '$O$ đến dây $AB$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Kẻ $OH \\perp AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = '
                        '\\dfrac{AB}{3} = 12$ (cm). Áp dụng định lí Pythagore trong tam giác vuông $OAH$...',
                        'Kẻ $OH \\perp AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = '
                        '\\dfrac{2}{AB} = 12$ (cm). Áp dụng định lí Pythagore trong tam giác vuông $OAH$...',
                        'Kẻ $OH \\perp AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = '
                        '\\dfrac{AB}{4} = 12$ (cm). Áp dụng định lí Pythagore trong tam giác vuông $OAH$...',
                        'Kẻ $OH \\perp AB$ tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = '
                        '\\dfrac{AB}{2} = 12$ (cm). Áp dụng định lí Pythagore trong tam giác vuông $OAH$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 14: Cung và dây của một đường tròn: Kẻ $OH \\perp AB$ '
                        'tại $H$, khi đó $H$ là trung điểm của $AB$ nên $AH = \\dfrac{AB}{2} = 12$ (cm).\n'
                        'Áp dụng định lí Pythagore trong tam giác vuông $OAH$: $OH = \\sqrt{OA^2 - AH^2} = '
                        '\\sqrt{13^2 - 12^2} = 5$ (cm).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho đường tròn $(O; R)$ có dây $AB = 6$ cm và khoảng cách từ tâm $O$ đến dây $AB$ bằng $4$ '
                 'cm. Tính bán kính $R$ của đường tròn (đơn vị: cm).',
            'answer': ['5'],
            'unit': None,
            'solution': 'Nửa dây cung là $\\dfrac{AB}{2} = 3$ cm. Bán kính $R = \\sqrt{3^2 + 4^2} = 5$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch05-duong-tron',
  'context_title': 'Chương V: Đường tròn',
  'context': 'Chương V · SGK Toán 9: Đường tròn.',
  'title': 'Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên',
  'icon': '🍕',
  'description': 'Tính độ dài cung tròn, diện tích hình quạt tròn và diện tích hình vành khuyên.',
  'requirements': ['Tính được độ dài cung tròn có số đo $n^\\circ$.',
                   'Tính được diện tích hình quạt tròn và diện tích hình vành khuyên.',
                   'Vận dụng kiến thức của **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình '
                   'vành khuyên** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Hình quạt tròn là phần hình tròn giới hạn bởi một cung tròn và hai bán kính đi qua hai mút '
                'của cung đó. Hình vành khuyên là phần nằm giữa hai đường tròn đồng tâm.',
  'theory': '1. Trên đường tròn bán kính $R$, độ dài $l$ của một cung $n^\\circ$ được tính theo công thức $l '
            '= \\dfrac{\\pi R n}{180}$.\n'
            '2. Diện tích $S_q$ của hình quạt tròn bán kính $R$ ứng với cung $n^\\circ$ là $S_q = '
            '\\dfrac{\\pi R^2 n}{360} = \\dfrac{lR}{2}$.\n'
            '3. Diện tích $S_v$ của hình vành khuyên tạo bởi hai đường tròn đồng tâm có bán kính $R$ và $r$ '
            '($R > r$) là $S_v = \\pi(R^2 - r^2)$.',
  'formulas': [{'category': 'Độ dài cung, diện tích hình quạt tròn và hình vành khuyên',
                'items': [{'name': 'Độ dài cung $n^\\circ$',
                           'formula': '$l = \\dfrac{\\pi R n}{180}$',
                           'note': 'Chu vi đường tròn: $C = 2\\pi R$'},
                          {'name': 'Diện tích hình quạt tròn',
                           'formula': '$S_q = \\dfrac{\\pi R^2 n}{360} = \\dfrac{lR}{2}$',
                           'note': 'Diện tích hình tròn: $S = \\pi R^2$'},
                          {'name': 'Diện tích hình vành khuyên',
                           'formula': '$S_v = \\pi(R^2 - r^2)$ ($R > r$)',
                           'note': 'Giới hạn bởi hai đường tròn đồng tâm'}]}],
  'example': 'Tính độ dài cung $60^\\circ$ và diện tích hình quạt tròn tương ứng của một đường tròn có bán '
             'kính $R = 6$ cm.',
  'example_answer': 'Độ dài cung là $l = \\dfrac{\\pi \\cdot 6 \\cdot 60}{180} = 2\\pi$ (cm).\n'
                    'Diện tích hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                    '($\\text{cm}^2$).',
  'real_life': 'Tính diện tích mặt quạt giấy, diện tích miếng bánh pizza hoặc diện tích mặt cắt ngang của '
               'ống nước hình trụ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính độ dài $l$ của cung $n^\\circ$ trên đường tròn bán kính $R$ là:',
            'options': ['$l = \\dfrac{\\pi R^2 n}{360}$',
                        '$l = \\dfrac{\\pi R n}{360}$',
                        '$l = \\dfrac{\\pi R n}{180}$',
                        '$l = \\dfrac{2\\pi R n}{180}$'],
            'answer': 2,
            'solution': 'Theo công thức SGK, độ dài cung $n^\\circ$ là $l = \\dfrac{\\pi R n}{180}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Diện tích hình quạt tròn bán kính $R = 6$ cm ứng với cung $90^\\circ$ là:',
            'options': ['$6\\pi\\text{ cm}^2$',
                        '$12\\pi\\text{ cm}^2$',
                        '$36\\pi\\text{ cm}^2$',
                        '$9\\pi\\text{ cm}^2$'],
            'answer': 3,
            'solution': 'Ta có $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 90}{360} = 9\\pi$ ($\\text{cm}^2$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên**, quy '
                 'tắc hoặc công thức nào sau đây xác định đúng **Độ dài cung $n^\\circ$**?',
            'options': ['$l = \\dfrac{\\pi R n}{180}$',
                        '$l = \\dfrac{\\pi R n}{190}$',
                        '$l = \\dfrac{180}{\\pi R n}$',
                        '$l = \\dfrac{\\pi R n}{182}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn '
                        'và hình vành khuyên, **Độ dài cung $n^\\circ$** được xác định bởi: $l = '
                        '\\dfrac{\\pi R n}{180}$. (Chu vi đường tròn: $C = 2\\pi R$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên**, '
                 'biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Diện tích hình quạt tròn**?',
            'options': ['$S_q = \\dfrac{\\pi R^3 n}{360} = \\dfrac{lR}{2}$',
                        '$S_q = \\dfrac{\\pi R^2 n}{360} = \\dfrac{lR}{2}$',
                        '$S_q = \\dfrac{360}{\\pi R^2 n} = \\dfrac{lR}{2}$',
                        '$S_q = \\dfrac{\\pi R^4 n}{360} = \\dfrac{lR}{2}$'],
            'answer': 1,
            'solution': 'Trong Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành khuyên, '
                        '**Diện tích hình quạt tròn** có công thức/quy tắc là: $S_q = \\dfrac{\\pi R^2 '
                        'n}{360} = \\dfrac{lR}{2}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Diện tích hình vành khuyên giới hạn bởi hai đường tròn đồng tâm có bán kính $R = 5$ cm và '
                 '$r = 3$ cm là:',
            'options': ['$8\\pi\\text{ cm}^2$',
                        '$4\\pi\\text{ cm}^2$',
                        '$16\\pi\\text{ cm}^2$',
                        '$34\\pi\\text{ cm}^2$'],
            'answer': 2,
            'solution': 'Ta có $S_v = \\pi(R^2 - r^2) = \\pi(5^2 - 3^2) = 16\\pi$ ($\\text{cm}^2$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình '
                 'vành khuyên**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được độ dài cung tròn có số đo $n^\\circ$. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được độ dài cung tròn có số đo $n^\\circ$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được độ dài cung tròn có '
                        'số đo $n^\\circ$.',
                        'Tính được độ dài cung tròn có số đo $n^\\circ$.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và '
                        'hình vành khuyên: Tính được độ dài cung tròn có số đo $n^\\circ$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đường tròn $(O; 10\\text{ cm})$ và cung $AB$ có số đo $72^\\circ$.',
            'statements': ['Chu vi của đường tròn $(O)$ bằng $20\\pi$ cm.',
                           'Độ dài của cung $AB$ bằng $4\\pi$ cm.',
                           'Diện tích hình quạt tròn $OAB$ bằng $20\\pi\\text{ cm}^2$.',
                           'Nếu tăng bán kính lên gấp đôi và giữ nguyên số đo cung thì diện tích hình quạt '
                           'tăng gấp đôi.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $C = 2\\pi R = 20\\pi$ cm. b) Đúng vì $l = \\dfrac{\\pi \\cdot 10 \\cdot '
                        '72}{180} = 4\\pi$ cm. c) Đúng vì $S_q = \\dfrac{lR}{2} = \\dfrac{4\\pi \\cdot '
                        '10}{2} = 20\\pi\\text{ cm}^2$. d) Sai vì diện tích tỉ lệ với $R^2$ nên tăng gấp $4$ '
                        'lần.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 15: Độ dài của cung tròn. '
                 'Diện tích hình quạt tròn và hình vành khuyên**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được độ dài cung tròn có số đo '
                           '$n^\\circ$.',
                           'Trong **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và hình vành '
                           'khuyên**, quy tắc/công thức **Độ dài cung $n^\\circ$** được viết là: $l = '
                           '\\dfrac{\\pi R n}{180}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $l = \\dfrac{\\pi R n}{190}$ thì kết quả của '
                           '**Độ dài cung $n^\\circ$** trong **Bài 15: Độ dài của cung tròn. Diện tích hình '
                           'quạt tròn và hình vành khuyên** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính độ dài cung $60^\\circ$ và diện tích hình quạt tròn '
                           'tương ứng của một đường tròn có bán kính $R = 6$ cm.”, kết quả giải đúng là: Độ '
                           'dài cung là $l = \\dfrac{\\pi \\cdot 6 \\cdot 60}{180} = 2\\pi$ (cm). Diện tích '
                           'hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 15: Độ dài của cung tròn. Diện tích hình '
                        'quạt tròn và hình vành khuyên. b) **Đúng** theo công thức **Độ dài cung '
                        '$n^\\circ$** ($l = \\dfrac{\\pi R n}{180}$). c) **Sai** vì công thức đúng của **Độ '
                        'dài cung $n^\\circ$** phải là $l = \\dfrac{\\pi R n}{180}$ chứ không phải $l = '
                        '\\dfrac{\\pi R n}{190}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn '
                 'và hình vành khuyên** để giải bài toán sau: Tính độ dài cung $60^\\circ$ và diện tích hình '
                 'quạt tròn tương ứng của một đường tròn có bán kính $R = 6$ cm. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Độ dài cung là $l = \\dfrac{\\pi \\cdot 6 \\cdot 60}{180} = 2\\pi$ (cm). Diện tích '
                        'hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                        '($\\text{cm}^2$...',
                        'Độ dài cung là $l = \\dfrac{\\pi : 6 \\cdot 60}{180} = 2\\pi$ (cm). Diện tích hình '
                        'quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                        '($\\text{cm}^2$...',
                        'Độ dài cung là $l = \\dfrac{180}{\\pi \\cdot 6 \\cdot 60} = 2\\pi$ (cm). Diện tích '
                        'hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                        '($\\text{cm}^2$...',
                        'Độ dài cung là $l = \\dfrac{\\pi \\cdot 12 \\cdot 60}{180} = 2\\pi$ (cm). Diện tích '
                        'hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                        '($\\text{cm}^2$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 15: Độ dài của cung tròn. Diện tích hình quạt tròn và '
                        'hình vành khuyên: Độ dài cung là $l = \\dfrac{\\pi \\cdot 6 \\cdot 60}{180} = '
                        '2\\pi$ (cm).\n'
                        'Diện tích hình quạt tròn là $S_q = \\dfrac{\\pi \\cdot 6^2 \\cdot 60}{360} = 6\\pi$ '
                        '($\\text{cm}^2$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình quạt tròn có bán kính $R = 8$ cm và độ dài cung tương ứng là $l = 5$ cm. Tính '
                 'diện tích của hình quạt tròn đó (đơn vị: $\\text{cm}^2$).',
            'answer': ['20'],
            'unit': None,
            'solution': 'Áp dụng công thức $S_q = \\dfrac{l \\cdot R}{2} = \\dfrac{5 \\cdot 8}{2} = 20$ '
                        '($\\text{cm}^2$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch05-duong-tron',
  'context_title': 'Chương V: Đường tròn',
  'context': 'Chương V · SGK Toán 9: Đường tròn.',
  'title': 'Bài 16: Vị trí tương đối của đường thẳng và đường tròn',
  'icon': '📏',
  'description': 'Xác định 3 vị trí tương đối của đường thẳng và đường tròn, tính chất của tiếp tuyến và hai '
                 'tiếp tuyến cắt nhau.',
  'requirements': ['Nhận biết được 3 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                   'nhau, không giao nhau).',
                   'Nắm vững dấu hiệu nhận biết và tính chất của tiếp tuyến đường tròn.',
                   'Vận dụng được tính chất của hai tiếp tuyến cắt nhau.'],
  'definition': 'Đường thẳng và đường tròn chỉ có một điểm chung được gọi là tiếp xúc nhau, đường thẳng đó '
                'gọi là tiếp tuyến của đường tròn và điểm chung gọi là tiếp điểm.',
  'theory': '1. Gọi $d$ là khoảng cách từ tâm $O$ đến đường thẳng $a$, $R$ là bán kính:\n'
            '- Đường thẳng $a$ và $(O; R)$ cắt nhau $\\Leftrightarrow d < R$ (có 2 điểm chung).\n'
            '- Đường thẳng $a$ và $(O; R)$ tiếp xúc nhau $\\Leftrightarrow d = R$ (có 1 điểm chung).\n'
            '- Đường thẳng $a$ và $(O; R)$ không giao nhau $\\Leftrightarrow d > R$ (không có điểm chung).\n'
            '2. Tiếp tuyến vuông góc với bán kính đi qua tiếp điểm.\n'
            '3. Định lí hai tiếp tuyến cắt nhau: Nếu hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $M$ '
            '(với $A, B$ là hai tiếp điểm) thì $MA = MB$, $MO$ là tia phân giác của $\\widehat{AMB}$ và $OM$ '
            'là tia phân giác của $\\widehat{AOB}$.',
  'formulas': [{'category': 'Tiếp tuyến của đường tròn',
                'items': [{'name': 'Điều kiện tiếp xúc',
                           'formula': '$d = R$ và $a \\perp OA$ tại $A \\in (O)$',
                           'note': 'Tiếp tuyến vuông góc với bán kính tại tiếp điểm'},
                          {'name': 'Tính chất hai tiếp tuyến cắt nhau',
                           'formula': '$MA = MB$; $\\widehat{AMO} = \\widehat{BMO}$; $\\widehat{AOM} = '
                                      '\\widehat{BOM}$',
                           'note': '$OM$ là đường trung trực của đoạn $AB$'}]}],
  'example': 'Từ điểm $M$ nằm ngoài đường tròn $(O; 5\\text{ cm})$ sao cho $OM = 13$ cm, kẻ tiếp tuyến $MA$ '
             'với đường tròn ($A$ là tiếp điểm). Tính độ dài đoạn $MA$.',
  'example_answer': 'Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ vuông '
                    'tại $A$.\n'
                    'Theo định lí Pythagore: $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{13^2 - 5^2} = 12$ (cm).',
  'real_life': 'Bánh xe lăn trên mặt đường phẳng minh họa hình ảnh đường tròn tiếp xúc với đường thẳng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho đường tròn $(O; 6\\text{ cm})$ và đường thẳng $a$ cách tâm $O$ một khoảng $d = 6$ cm. '
                 'Vị trí tương đối của đường thẳng $a$ và đường tròn $(O)$ là:',
            'options': ['Cắt nhau', 'Không giao nhau', 'Trùng nhau', 'Tiếp xúc nhau'],
            'answer': 3,
            'solution': 'Vì $d = R = 6$ cm nên đường thẳng $a$ và đường tròn $(O)$ tiếp xúc nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu đường thẳng $d$ là tiếp tuyến của đường tròn $(O)$ tại tiếp điểm $A$ thì:',
            'options': ['$d \\perp OA$ tại $A$', '$d // OA$', '$d$ đi qua tâm $O$', '$OA > R$'],
            'answer': 0,
            'solution': 'Theo tính chất tiếp tuyến, tiếp tuyến vuông góc với bán kính tại tiếp điểm.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Vị trí tương đối của đường thẳng và đường tròn**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Điều kiện tiếp xúc**?',
            'options': ['$d = R$ và $a \\perp OA$ tại $A \\notin (O)$',
                        '$d = R$ và $a \\perp OA$ tại $A \\in (O)$',
                        'Đảo ngược vế của quy tắc: $d = R$ và $a \\perp OA$ tại $A \\in (O)$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $d = R$ và $a \\perp OA$ tại $A '
                        '\\in (O)$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Vị trí tương đối của đường thẳng và đường '
                        'tròn, **Điều kiện tiếp xúc** được xác định bởi: $d = R$ và $a \\perp OA$ tại $A '
                        '\\in (O)$. (Tiếp tuyến vuông góc với bán kính tại tiếp điểm)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Vị trí tương đối của đường thẳng và đường tròn**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Tính chất hai tiếp tuyến cắt nhau**?',
            'options': ['$MA = MB$; $\\widehat{AMO} = \\widehat{BMO}$; $\\widehat{AOM} = \\widehat{BOM}$ '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $MA = MB$; $\\widehat{AMO} = \\widehat{BMO}$; '
                        '$\\widehat{AOM} = \\widehat{BOM}$',
                        '$MA = MB$; $\\widehat{AMO} = \\widehat{BMO}$; $\\widehat{AOM} = \\widehat{BOM}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $MA = MB$; $\\widehat{AMO} = '
                        '\\widehat{BMO}$; $\\widehat{AOM} = \\widehat{BOM}$'],
            'answer': 2,
            'solution': 'Trong Bài 16: Vị trí tương đối của đường thẳng và đường tròn, **Tính chất hai tiếp '
                        'tuyến cắt nhau** có công thức/quy tắc là: $MA = MB$; $\\widehat{AMO} = '
                        '\\widehat{BMO}$; $\\widehat{AOM} = \\widehat{BOM}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Từ điểm $M$ ngoài đường tròn $(O)$, kẻ hai tiếp tuyến $MA, MB$ ($A, B$ là hai tiếp điểm). '
                 'Nếu $\\widehat{AMB} = 60^\\circ$ thì số đo $\\widehat{AMO}$ bằng:',
            'options': ['$60^\\circ$', '$120^\\circ$', '$45^\\circ$', '$30^\\circ$'],
            'answer': 3,
            'solution': 'Theo tính chất hai tiếp tuyến cắt nhau, $MO$ là tia phân giác của $\\widehat{AMB}$ '
                        'nên $\\widehat{AMO} = \\dfrac{60^\\circ}{2} = 30^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Vị trí tương đối của đường thẳng và đường tròn**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được 3 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                        'nhau, không giao nhau).',
                        'Nhận biết được 4 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                        'nhau, không giao nhau).',
                        'Nhận biết được 2 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                        'nhau, không giao nhau).',
                        'Nhận biết được 6 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                        'nhau, không giao nhau).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Vị trí tương đối của đường thẳng và đường tròn: '
                        'Nhận biết được 3 vị trí tương đối của đường thẳng và đường tròn (cắt nhau, tiếp xúc '
                        'nhau, không giao nhau).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Từ điểm $M$ cách tâm $O$ của đường tròn $(O; 3\\text{ cm})$ một khoảng $OM = 5$ cm, kẻ hai '
                 'tiếp tuyến $MA, MB$ tới đường tròn ($A, B$ là hai tiếp điểm).',
            'statements': ['Tam giác $OAM$ vuông tại $A$.',
                           'Độ dài đoạn tiếp tuyến $MA = 4$ cm.',
                           'Độ dài đoạn tiếp tuyến $MB = 5$ cm.',
                           'Đường thẳng $OM$ vuông góc với dây $AB$ tại trung điểm của $AB$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $MA \\perp OA$. b) Đúng vì $MA = \\sqrt{5^2 - 3^2} = 4$ cm. c) Sai vì '
                        '$MB = MA = 4$ cm. d) Đúng vì $OA = OB$ và $MA = MB$ nên $OM$ là trung trực của '
                        '$AB$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 16: Vị trí tương đối của '
                 'đường thẳng và đường tròn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được 3 vị trí tương đối của '
                           'đường thẳng và đường tròn (cắt nhau, tiếp xúc nhau, không giao nhau).',
                           'Trong **Bài 16: Vị trí tương đối của đường thẳng và đường tròn**, quy tắc/công '
                           'thức **Điều kiện tiếp xúc** được viết là: $d = R$ và $a \\perp OA$ tại $A \\in '
                           '(O)$.',
                           'Nếu áp dụng sai dấu/phép tính thành $d = R$ và $a \\perp OA$ tại $A \\notin (O)$ '
                           'thì kết quả của **Điều kiện tiếp xúc** trong **Bài 16: Vị trí tương đối của '
                           'đường thẳng và đường tròn** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Từ điểm $M$ nằm ngoài đường tròn $(O; 5\\text{ cm})$ sao cho '
                           '$OM = 13$ cm, kẻ tiếp tuyến $MA$ với đường tròn ($A$ là tiếp điểm). Tính độ...”, '
                           'kết quả giải đúng là: Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp '
                           'MA$, suy ra tam giác $OAM$ vuông tại $A$. Theo định lí Pythagore: $MA = '
                           '\\sqrt{OM^2 - OA^2} = \\sqrt{13^2 - 5^2} = 12$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 16: Vị trí tương đối của đường thẳng và '
                        'đường tròn. b) **Đúng** theo công thức **Điều kiện tiếp xúc** ($d = R$ và $a \\perp '
                        'OA$ tại $A \\in (O)$). c) **Sai** vì công thức đúng của **Điều kiện tiếp xúc** phải '
                        'là $d = R$ và $a \\perp OA$ tại $A \\in (O)$ chứ không phải $d = R$ và $a \\perp '
                        'OA$ tại $A \\notin (O)$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Vị trí tương đối của đường thẳng và đường '
                 'tròn** để giải bài toán sau: Từ điểm $M$ nằm ngoài đường tròn $(O; 5\\text{ cm})$ sao cho '
                 '$OM = 13$ cm, kẻ tiếp tuyến $MA$ với đường tròn ($A$ là tiếp điểm). Tính độ dài đoạn $MA$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ '
                        'vuông tại $A$. Theo định lí Pythagore: $MA = \\sqrt{OM^2 + OA^2} = \\sqrt{13^2 - '
                        '5^2} = 12$...',
                        'Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ '
                        'vuông tại $A$. Theo định lí Pythagore: $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{13^2 - '
                        '5^2} = 12$...',
                        'Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ '
                        'vuông tại $A$. Theo định lí Pythagore: $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{13^2 - '
                        '5^2} = 11$...',
                        'Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ '
                        'vuông tại $A$. Theo định lí Pythagore: $MA = \\sqrt{OM^4 - OA^2} = \\sqrt{13^2 - '
                        '5^2} = 12$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 16: Vị trí tương đối của đường thẳng và đường tròn: Vì '
                        '$MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$, suy ra tam giác $OAM$ '
                        'vuông tại $A$.\n'
                        'Theo định lí Pythagore: $MA = \\sqrt{OM^2 - OA^2} = \\sqrt{13^2 - 5^2} = 12$ (cm).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Từ điểm $M$ nằm ngoài đường tròn $(O; 6\\text{ cm})$, kẻ hai tiếp tuyến $MA, MB$ ($A, B$ '
                 'là tiếp điểm) biết $MA = 8$ cm. Tính khoảng cách $OM$ (đơn vị: cm).',
            'answer': ['10'],
            'unit': None,
            'solution': 'Trong tam giác vuông $OAM$ tại $A$: $OM = \\sqrt{OA^2 + MA^2} = \\sqrt{6^2 + 8^2} = '
                        '10$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch05-duong-tron',
  'context_title': 'Chương V: Đường tròn',
  'context': 'Chương V · SGK Toán 9: Đường tròn.',
  'title': 'Bài 17: Vị trí tương đối của hai đường tròn',
  'icon': '♾️',
  'description': 'Nhận biết các vị trí tương đối của hai đường tròn: cắt nhau, tiếp xúc nhau và không giao '
                 'nhau.',
  'requirements': ["Nhận biết được vị trí tương đối của hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge r$) "
                   "thông qua hệ thức giữa $OO'$ với $R, r$.",
                   'Vận dụng được tính chất đường nối tâm để giải các bài toán hình học.',
                   'Vận dụng kiến thức của **Bài 17: Vị trí tương đối của hai đường tròn** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Hai đường tròn phân biệt có thể có $2$ điểm chung (cắt nhau), $1$ điểm chung (tiếp xúc '
                'ngoài hoặc tiếp xúc trong), hoặc không có điểm chung nào (ngoài nhau, đựng nhau hoặc đồng '
                'tâm).',
  'theory': "Cho hai đường tròn $(O; R)$ và $(O'; r)$ với $R \\ge r$ và đặt $d = OO'$:\n"
            '1. Hai đường tròn cắt nhau $\\Leftrightarrow R - r < d < R + r$ (có $2$ điểm chung).\n'
            '2. Hai đường tròn tiếp xúc ngoài $\\Leftrightarrow d = R + r$; tiếp xúc trong $\\Leftrightarrow '
            'd = R - r > 0$ (có $1$ điểm chung).\n'
            "3. Hai đường tròn ở ngoài nhau $\\Leftrightarrow d > R + r$; đường tròn $(O)$ đựng $(O')$ "
            '$\\Leftrightarrow d < R - r$ (không có điểm chung).',
  'formulas': [{'category': "Hệ thức giữa đoạn nối tâm $d = OO'$ và hai bán kính ($R \\ge r$)",
                'items': [{'name': 'Hai đường tròn cắt nhau',
                           'formula': '$R - r < d < R + r$',
                           'note': 'Có $2$ điểm chung'},
                          {'name': 'Hai đường tròn tiếp xúc nhau',
                           'formula': '$d = R + r$ (tiếp xúc ngoài); $d = R - r$ (tiếp xúc trong)',
                           'note': 'Có $1$ điểm chung nằm trên đường nối tâm'},
                          {'name': 'Hai đường tròn không giao nhau',
                           'formula': '$d > R + r$ (ngoài nhau); $d < R - r$ (đựng nhau)',
                           'note': 'Không có điểm chung'}]}],
  'example': "Cho hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 3\\text{ cm})$ có $OO' = 7$ cm. Xác định vị "
             'trí tương đối của hai đường tròn.',
  'example_answer': 'Ta có $R - r = 5 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm).\n'
                    "Vì $2 < 7 < 8$ (tức là $R - r < OO' < R + r$) nên hai đường tròn cắt nhau.",
  'real_life': 'Cơ cấu truyền động bánh răng ăn khớp trong đồng hồ hoặc động cơ cơ khí minh họa hai đường '
               'tròn tiếp xúc ngoài.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': "Cho hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 2\\text{ cm})$ có khoảng cách hai tâm $OO' "
                 '= 7$ cm. Vị trí tương đối của hai đường tròn là:',
            'options': ['Tiếp xúc ngoài', 'Tiếp xúc trong', 'Cắt nhau', 'Ở ngoài nhau'],
            'answer': 0,
            'solution': "Vì $OO' = 5 + 2 = 7$ cm ($d = R + r$) nên hai đường tròn tiếp xúc ngoài.",
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai đường tròn cắt nhau có bao nhiêu điểm chung?',
            'options': ['$1$', '$2$', '$0$', '$3$'],
            'answer': 1,
            'solution': 'Hai đường tròn cắt nhau có đúng $2$ điểm chung.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Vị trí tương đối của hai đường tròn**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Hai đường tròn cắt nhau**?',
            'options': ['$R - r < d < R - r$',
                        'Đảo ngược vế của quy tắc: $R - r < d < R + r$',
                        '$R - r < d < R + r$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $R - r < d < R + r$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Vị trí tương đối của hai đường tròn, **Hai '
                        'đường tròn cắt nhau** được xác định bởi: $R - r < d < R + r$. (Có $2$ điểm chung)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Vị trí tương đối của hai đường tròn**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Hai đường tròn tiếp xúc nhau**?',
            'options': ['$d = R - r$ (tiếp xúc ngoài); $d = R - r$ (tiếp xúc trong)',
                        'Đảo ngược vế của quy tắc: $d = R + r$ (tiếp xúc ngoài); $d = R - r$ (tiếp xúc '
                        'trong)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $d = R + r$ (tiếp xúc ngoài); '
                        '$d = R - r$ (tiếp xúc trong)',
                        '$d = R + r$ (tiếp xúc ngoài); $d = R - r$ (tiếp xúc trong)'],
            'answer': 3,
            'solution': 'Trong Bài 17: Vị trí tương đối của hai đường tròn, **Hai đường tròn tiếp xúc nhau** '
                        'có công thức/quy tắc là: $d = R + r$ (tiếp xúc ngoài); $d = R - r$ (tiếp xúc '
                        'trong).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Cho hai đường tròn $(O; 6\\text{ cm})$ và $(O'; 2\\text{ cm})$ tiếp xúc trong với nhau. "
                 "Khoảng cách $OO'$ bằng:",
            'options': ['$4$ cm', '$8$ cm', '$3$ cm', '$12$ cm'],
            'answer': 0,
            'solution': "Hai đường tròn tiếp xúc trong nên $OO' = R - r = 6 - 2 = 4$ (cm).",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Vị trí tương đối của hai đường tròn**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ["Nhận biết được vị trí tương đối của hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\le "
                        "r$) thông qua hệ thức giữa $OO'$ với $R, r$.",
                        "Nhận biết được vị trí tương đối của hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge "
                        "r$) thông qua hệ thức giữa $OO'$ với $R, r$.",
                        'Đảo ngược vế của quy tắc: Nhận biết được vị trí tương đối của hai đường tròn $(O; '
                        "R)$ và $(O'; r)$ ($R \\ge r$) thông qua hệ thức giữa $OO'$ với $R, r$.",
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được vị trí tương đối '
                        "của hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge r$) thông qua hệ thức giữa $OO'$ "
                        'với $R, r$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Vị trí tương đối của hai đường tròn: Nhận biết '
                        "được vị trí tương đối của hai đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge r$) thông "
                        "qua hệ thức giữa $OO'$ với $R, r$."},
           {'level': 'hieu',
            'type': 'tf4',
            'q': "Cho hai đường tròn $(O; 8\\text{ cm})$ và $(O'; 5\\text{ cm})$.",
            'statements': ["Khi $OO' = 15$ cm thì hai đường tròn ở ngoài nhau.",
                           "Khi $OO' = 13$ cm thì hai đường tròn tiếp xúc ngoài.",
                           "Khi $OO' = 10$ cm thì hai đường tròn cắt nhau tại hai điểm phân biệt.",
                           "Khi $OO' = 2$ cm thì hai đường tròn tiếp xúc trong."],
            'answer': [True, True, True, False],
            'solution': 'Ta có $R + r = 13$ cm và $R - r = 3$ cm. a) Đúng vì $15 > 13$. b) Đúng vì $13 = R + '
                        "r$. c) Đúng vì $3 < 10 < 13$. d) Sai vì $2 < 3$ nên $(O)$ đựng $(O')$.",
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 17: Vị trí tương đối của '
                 'hai đường tròn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được vị trí tương đối của hai '
                           "đường tròn $(O; R)$ và $(O'; r)$ ($R \\ge r$) thông qua hệ thức giữa $OO'$ với "
                           '$R, r$.',
                           'Trong **Bài 17: Vị trí tương đối của hai đường tròn**, quy tắc/công thức **Hai '
                           'đường tròn cắt nhau** được viết là: $R - r < d < R + r$.',
                           'Nếu áp dụng sai dấu/phép tính thành $R - r < d < R - r$ thì kết quả của **Hai '
                           'đường tròn cắt nhau** trong **Bài 17: Vị trí tương đối của hai đường tròn** vẫn '
                           'không thay đổi.',
                           "Xét ví dụ của bài: “Cho hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 3\\text{ "
                           "cm})$ có $OO' = 7$ cm. Xác định vị trí tương đối của hai đường tròn.”, kết quả "
                           'giải đúng là: Ta có $R - r = 5 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm). Vì $2 '
                           "< 7 < 8$ (tức là $R - r < OO' < R + r$) nên hai đường tròn cắt nhau."],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 17: Vị trí tương đối của hai đường tròn. '
                        'b) **Đúng** theo công thức **Hai đường tròn cắt nhau** ($R - r < d < R + r$). c) '
                        '**Sai** vì công thức đúng của **Hai đường tròn cắt nhau** phải là $R - r < d < R + '
                        'r$ chứ không phải $R - r < d < R - r$. d) **Đúng** theo lời giải ví dụ minh họa '
                        'trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Vị trí tương đối của hai đường tròn** để giải '
                 "bài toán sau: Cho hai đường tròn $(O; 5\\text{ cm})$ và $(O'; 3\\text{ cm})$ có $OO' = 7$ "
                 'cm. Xác định vị trí tương đối của hai đường tròn. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Ta có $R - r = 5 - 3 = 2$ (cm) và $R - r = 5 + 3 = 8$ (cm). Vì $2 < 7 < 8$ (tức là '
                        "$R - r < OO' < R + r$) nên hai đường tròn cắt nhau.",
                        'Ta có $R - r = 5 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm). Vì $2 < 7 < 7$ (tức là '
                        "$R - r < OO' < R + r$) nên hai đường tròn cắt nhau.",
                        'Ta có $R - r = 5 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm). Vì $2 < 7 < 8$ (tức là '
                        "$R - r < OO' < R + r$) nên hai đường tròn cắt nhau.",
                        'Ta có $R - r = 10 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm). Vì $2 < 7 < 8$ (tức là '
                        "$R - r < OO' < R + r$) nên hai đường tròn cắt nhau."],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 17: Vị trí tương đối của hai đường tròn: Ta có $R - r = '
                        '5 - 3 = 2$ (cm) và $R + r = 5 + 3 = 8$ (cm).\n'
                        "Vì $2 < 7 < 8$ (tức là $R - r < OO' < R + r$) nên hai đường tròn cắt nhau."},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai bánh răng hình tròn tiếp xúc ngoài với nhau có bán kính lần lượt là $12$ cm và $8$ cm. '
                 'Khoảng cách giữa hai trục tâm của hai bánh răng bằng bao nhiêu xentimét?',
            'answer': ['20'],
            'unit': None,
            'solution': 'Vì hai bánh răng tiếp xúc ngoài nên khoảng cách hai tâm là $d = R + r = 12 + 8 = '
                        '20$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch06-ham-so-phuong-trinh-bac-hai',
  'context_title': 'Chương VI: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn',
  'context': 'Chương VI · SGK Toán 9: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn.',
  'title': 'Bài 18: Hàm số y = ax² (a ≠ 0)',
  'icon': '📉',
  'description': 'Nhận biết hàm số y = ax² (a ≠ 0), vẽ đồ thị parabol và nêu tính chất đối xứng của đồ thị.',
  'requirements': ['Tính được giá trị của hàm số $y = ax^2$ ($a \\neq 0$) và lập bảng giá trị.',
                   'Nhận biết được tính chất và vẽ được đồ thị (parabol) của hàm số $y = ax^2$ ($a \\neq '
                   '0$).',
                   'Vận dụng kiến thức của **Bài 18: Hàm số y = ax² (a ≠ 0)** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Đồ thị của hàm số $y = ax^2$ ($a \\neq 0$) là một đường cong đi qua gốc tọa độ $O(0; 0)$, '
                'nhận trục $Oy$ làm trục đối xứng, được gọi là một parabol với đỉnh $O$.',
  'theory': 'Tính chất của đồ thị hàm số $y = ax^2$ ($a \\neq 0$):\n'
            '- Nếu $a > 0$ thì đồ thị nằm phía trên trục hoành, $O$ là điểm thấp nhất của đồ thị.\n'
            '- Nếu $a < 0$ thì đồ thị nằm phía dưới trục hoành, $O$ là điểm cao nhất của đồ thị.',
  'formulas': [{'category': 'Hàm số $y = ax^2$ ($a \\neq 0$)',
                'items': [{'name': 'Đỉnh và trục đối xứng',
                           'formula': 'Đỉnh $O(0; 0)$, trục đối xứng $Oy$',
                           'note': 'Điểm $(x_0; y_0)$ và $(-x_0; y_0)$ đối xứng nhau qua $Oy$'},
                          {'name': 'Bề lõm của parabol',
                           'formula': '$a > 0$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay '
                                      'xuống dưới ($y \\le 0$)',
                           'note': '$O$ là điểm thấp nhất ($a > 0$) hoặc cao nhất ($a < 0$)'}]}],
  'example': 'Cho hàm số $y = ax^2$. Tìm hệ số $a$ biết đồ thị hàm số đi qua điểm $M(2; -8)$.',
  'example_answer': 'Vì đồ thị hàm số đi qua điểm $M(2; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = '
                    'ax^2$, ta có:\n'
                    '$-8 = a \\cdot 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$.',
  'real_life': 'Mặt cắt của chảo thu sóng vệ tinh (parabol) hoặc quỹ đạo của tia nước phun lên từ đài phun '
               'nước.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đồ thị của hàm số $y = 2x^2$ đi qua điểm nào sau đây?',
            'options': ['$(1; -2)$', '$(1; 2)$', '$(2; 4)$', '$(-1; -2)$'],
            'answer': 1,
            'solution': 'Thay $x = 1$ vào $y = 2x^2$ ta được $y = 2 \\cdot 1^2 = 2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trục đối xứng của đồ thị hàm số $y = -3x^2$ là:',
            'options': ['Trục hoành $Ox$', 'Đường thẳng $y = x$', 'Trục tung $Oy$', 'Đường thẳng $x = -3$'],
            'answer': 2,
            'solution': 'Đồ thị hàm số $y = ax^2$ ($a \\neq 0$) luôn nhận trục tung $Oy$ làm trục đối xứng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Hàm số y = ax² (a ≠ 0)**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Đỉnh và trục đối xứng**?',
            'options': ['Đỉnh $O(1; 0)$, trục đối xứng $Oy$',
                        'Đỉnh $O(0; 1)$, trục đối xứng $Oy$',
                        'Đỉnh $O(2; 0)$, trục đối xứng $Oy$',
                        'Đỉnh $O(0; 0)$, trục đối xứng $Oy$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 18: Hàm số y = ax² (a ≠ 0), **Đỉnh và trục đối '
                        'xứng** được xác định bởi: Đỉnh $O(0; 0)$, trục đối xứng $Oy$. (Điểm $(x_0; y_0)$ và '
                        '$(-x_0; y_0)$ đối xứng nhau qua $Oy$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Hàm số y = ax² (a ≠ 0)**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Bề lõm của parabol**?',
            'options': ['$a > 0$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay xuống dưới ($y '
                        '\\le 0$)',
                        '$a > 0$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay xuống dưới ($y '
                        '\\ge 0$)',
                        '$a > 0$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay xuống dưới ($y '
                        '\\le 1$)',
                        '$a > 2$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay xuống dưới ($y '
                        '\\le 0$)'],
            'answer': 0,
            'solution': 'Trong Bài 18: Hàm số y = ax² (a ≠ 0), **Bề lõm của parabol** có công thức/quy tắc '
                        'là: $a > 0$: bề lõm quay lên trên ($y \\ge 0$); $a < 0$: bề lõm quay xuống dưới ($y '
                        '\\le 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết đồ thị hàm số $y = ax^2$ đi qua điểm $A(-3; 9)$. Giá trị của hệ số $a$ là:',
            'options': ['$a = -1$', '$a = 1$', '$a = 3$', '$a = -3$'],
            'answer': 1,
            'solution': 'Thay $x = -3, y = 9$ vào $y = ax^2$ ta có $9 = a \\cdot (-3)^2 = 9a \\Rightarrow a '
                        '= 1$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 18: Hàm số y = ax² (a ≠ 0)**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Tính được giá trị của hàm số $y = ax^3$ ($a \\neq 0$) và lập bảng giá trị.',
                        'Tính được giá trị của hàm số $y = ax^2$ ($a \\neq 1$) và lập bảng giá trị.',
                        'Tính được giá trị của hàm số $y = ax^2$ ($a \\neq 0$) và lập bảng giá trị.',
                        'Tính được giá trị của hàm số $y = ax^4$ ($a \\neq 0$) và lập bảng giá trị.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 18: Hàm số y = ax² (a ≠ 0): Tính được giá trị của hàm '
                        'số $y = ax^2$ ($a \\neq 0$) và lập bảng giá trị.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho hàm số $y = -\\dfrac{1}{2}x^2$ có đồ thị là parabol $(P)$.',
            'statements': ['Đồ thị $(P)$ nằm hoàn toàn phía dưới trục hoành (trừ gốc tọa độ $O$).',
                           'Gốc tọa độ $O(0; 0)$ là điểm cao nhất của đồ thị $(P)$.',
                           'Điểm $M(2; 2)$ thuộc đồ thị $(P)$.',
                           'Hai điểm $A(-4; -8)$ và $B(4; -8)$ cùng thuộc $(P)$ và đối xứng nhau qua trục '
                           '$Oy$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $a = -\\dfrac{1}{2} < 0$. b) Đúng. c) Sai vì tại $x = 2$ thì $y = -2 '
                        '\\neq 2$. d) Đúng vì tại $x = \\pm 4$ thì $y = -8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 18: Hàm số y = ax² (a ≠ '
                 '0)**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được giá trị của hàm số $y = ax^2$ '
                           '($a \\neq 0$) và lập bảng giá trị.',
                           'Trong **Bài 18: Hàm số y = ax² (a ≠ 0)**, quy tắc/công thức **Đỉnh và trục đối '
                           'xứng** được viết là: Đỉnh $O(0; 0)$, trục đối xứng $Oy$.',
                           'Nếu áp dụng sai dấu/phép tính thành Đỉnh $O(1; 0)$, trục đối xứng $Oy$ thì kết '
                           'quả của **Đỉnh và trục đối xứng** trong **Bài 18: Hàm số y = ax² (a ≠ 0)** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Cho hàm số $y = ax^2$. Tìm hệ số $a$ biết đồ thị hàm số đi '
                           'qua điểm $M(2; -8)$.”, kết quả giải đúng là: Vì đồ thị hàm số đi qua điểm $M(2; '
                           '-8)$ nên thay $x = 2, y = -8$ vào công thức $y = ax^2$, ta có: $-8 = a \\cdot '
                           '2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 18: Hàm số y = ax² (a ≠ 0). b) **Đúng** '
                        'theo công thức **Đỉnh và trục đối xứng** (Đỉnh $O(0; 0)$, trục đối xứng $Oy$). c) '
                        '**Sai** vì công thức đúng của **Đỉnh và trục đối xứng** phải là Đỉnh $O(0; 0)$, '
                        'trục đối xứng $Oy$ chứ không phải Đỉnh $O(1; 0)$, trục đối xứng $Oy$. d) **Đúng** '
                        'theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 18: Hàm số y = ax² (a ≠ 0)** để giải bài toán sau: '
                 'Cho hàm số $y = ax^2$. Tìm hệ số $a$ biết đồ thị hàm số đi qua điểm $M(2; -8)$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì đồ thị hàm số đi qua điểm $M(2; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = '
                        'ax^2$, ta có: $-8 = a : 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$...',
                        'Vì đồ thị hàm số đi qua điểm $M(2; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = '
                        'ax^2$, ta có: $-8 = a \\cdot 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -1$...',
                        'Vì đồ thị hàm số đi qua điểm $M(4; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = '
                        'ax^2$, ta có: $-8 = a \\cdot 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$...',
                        'Vì đồ thị hàm số đi qua điểm $M(2; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = '
                        'ax^2$, ta có: $-8 = a \\cdot 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 18: Hàm số y = ax² (a ≠ 0): Vì đồ thị hàm số đi qua điểm '
                        '$M(2; -8)$ nên thay $x = 2, y = -8$ vào công thức $y = ax^2$, ta có:\n'
                        '$-8 = a \\cdot 2^2 \\Rightarrow 4a = -8 \\Rightarrow a = -2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Quãng đường rơi tự do của một vật được tính theo công thức $s = 5t^2$ (với $s$ tính bằng '
                 'mét, $t$ tính bằng giây). Hỏi sau $4$ giây vật rơi được quãng đường bao nhiêu mét?',
            'answer': ['80'],
            'unit': None,
            'solution': 'Thay $t = 4$ vào công thức $s = 5t^2$, ta được $s = 5 \\cdot 4^2 = 5 \\cdot 16 = '
                        '80$ (m).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch06-ham-so-phuong-trinh-bac-hai',
  'context_title': 'Chương VI: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn',
  'context': 'Chương VI · SGK Toán 9: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn.',
  'title': 'Bài 19: Phương trình bậc hai một ẩn',
  'icon': '🧮',
  'description': 'Nhận biết phương trình bậc hai một ẩn và giải bằng công thức nghiệm hoặc công thức nghiệm '
                 'thu gọn.',
  'requirements': ['Nhận biết được phương trình bậc hai một ẩn $ax^2 + bx + c = 0$ ($a \\neq 0$).',
                   "Tính được biệt thức $\\Delta$ (hoặc $\\Delta'$) và giải được phương trình bậc hai một "
                   'ẩn.',
                   'Vận dụng kiến thức của **Bài 19: Phương trình bậc hai một ẩn** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Phương trình bậc hai một ẩn (nói gọn là phương trình bậc hai) là phương trình có dạng $ax^2 '
                '+ bx + c = 0$, trong đó $x$ là ẩn; $a, b, c$ là những số cho trước gọi là các hệ số và $a '
                '\\neq 0$.',
  'theory': 'Xét phương trình $ax^2 + bx + c = 0$ ($a \\neq 0$) và biệt thức $\\Delta = b^2 - 4ac$:\n'
            '- Nếu $\\Delta > 0$ thì phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{-b + '
            '\\sqrt{\\Delta}}{2a}$, $x_2 = \\dfrac{-b - \\sqrt{\\Delta}}{2a}$.\n'
            '- Nếu $\\Delta = 0$ thì phương trình có nghiệm kép: $x_1 = x_2 = -\\dfrac{b}{2a}$.\n'
            '- Nếu $\\Delta < 0$ thì phương trình vô nghiệm.',
  'formulas': [{'category': 'Công thức nghiệm của phương trình bậc hai $ax^2 + bx + c = 0$ ($a \\neq 0$)',
                'items': [{'name': 'Biệt thức $\\Delta$',
                           'formula': '$\\Delta = b^2 - 4ac$',
                           'note': 'Khi $\\Delta > 0$: $x_{1,2} = \\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$'},
                          {'name': "Biệt thức thu gọn $\\Delta'$ ($b = 2b'$)",
                           'formula': "$\\Delta' = b'^2 - ac$",
                           'note': "Khi $\\Delta' > 0$: $x_{1,2} = \\dfrac{-b' \\pm "
                                   "\\sqrt{\\Delta'}}{a}$"}]}],
  'example': 'Giải phương trình $x^2 - 5x + 6 = 0$.',
  'example_answer': 'Ta có $a = 1, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = 25 - '
                    '24 = 1 > 0$.\n'
                    'Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{5 + 1}{2} = 3$ và $x_2 = \\dfrac{5 '
                    '- 1}{2} = 2$.',
  'real_life': 'Xác định thời điểm quả bóng được ném lên cao chạm đất hoặc đạt độ cao cho trước.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phương trình nào sau đây là phương trình bậc hai một ẩn?',
            'options': ['$0x^2 + 4x - 5 = 0$', '$x^3 - x^2 + 1 = 0$', '$2x^2 - 3x + 1 = 0$', '$2x - 7 = 0$'],
            'answer': 2,
            'solution': 'Phương trình $2x^2 - 3x + 1 = 0$ có dạng $ax^2 + bx + c = 0$ với $a = 2 \\neq 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Biệt thức $\\Delta$ của phương trình $x^2 - 4x + 3 = 0$ bằng:',
            'options': ['$28$', '$-8$', '$16$', '$4$'],
            'answer': 3,
            'solution': 'Ta có $\\Delta = (-4)^2 - 4 \\cdot 1 \\cdot 3 = 16 - 12 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Phương trình bậc hai một ẩn**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Biệt thức $\\Delta$**?',
            'options': ['$\\Delta = b^2 - 4ac$',
                        '$\\Delta = b^2 + 4ac$',
                        '$\\Delta = b^1 - 4ac$',
                        '$\\Delta = b^4 - 4ac$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Phương trình bậc hai một ẩn, **Biệt thức '
                        '$\\Delta$** được xác định bởi: $\\Delta = b^2 - 4ac$. (Khi $\\Delta > 0$: $x_{1,2} '
                        '= \\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Phương trình bậc hai một ẩn**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 "diễn đúng **Biệt thức thu gọn $\\Delta'$ ($b = 2b'$)**?",
            'options': ["$\\Delta' = b'^2 + ac$",
                        "$\\Delta' = b'^2 - ac$",
                        "$\\Delta' = b'^1 - ac$",
                        "$\\Delta' = b'^4 - ac$"],
            'answer': 1,
            'solution': "Trong Bài 19: Phương trình bậc hai một ẩn, **Biệt thức thu gọn $\\Delta'$ ($b = "
                        "2b'$)** có công thức/quy tắc là: $\\Delta' = b'^2 - ac$."},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phương trình $x^2 - 6x + 9 = 0$ có nghiệm là:',
            'options': ['Hai nghiệm $x = 3$ và $x = -3$',
                        'Nghiệm kép $x_1 = x_2 = -3$',
                        'Nghiệm kép $x_1 = x_2 = 3$',
                        'Vô nghiệm'],
            'answer': 2,
            'solution': "Ta có $\\Delta' = (-3)^2 - 1 \\cdot 9 = 0$, phương trình có nghiệm kép $x_1 = x_2 = "
                        '3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Phương trình bậc hai một ẩn**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được phương trình bậc hai một ẩn $ax^2 - bx + c = 0$ ($a \\neq 0$).',
                        'Nhận biết được phương trình bậc hai một ẩn $ax^2 + bx + c = 0$ ($a \\neq 1$).',
                        'Nhận biết được phương trình bậc hai một ẩn $ax^4 + bx + c = 0$ ($a \\neq 0$).',
                        'Nhận biết được phương trình bậc hai một ẩn $ax^2 + bx + c = 0$ ($a \\neq 0$).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Phương trình bậc hai một ẩn: Nhận biết được '
                        'phương trình bậc hai một ẩn $ax^2 + bx + c = 0$ ($a \\neq 0$).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình bậc hai $2x^2 - 5x + 2 = 0$ (1).',
            'statements': ['Các hệ số của phương trình (1) là $a = 2, b = -5, c = 2$.',
                           'Biệt thức $\\Delta$ của phương trình (1) bằng $9$.',
                           'Phương trình (1) có hai nghiệm phân biệt là $x_1 = 2$ và $x_2 = \\dfrac{1}{2}$.',
                           'Phương trình (1) có một nghiệm nguyên âm.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\Delta = (-5)^2 - 4 \\cdot 2 \\cdot 2 = 9$. c) Đúng vì $x_1 = '
                        '\\dfrac{5 + 3}{4} = 2, x_2 = \\dfrac{5 - 3}{4} = \\dfrac{1}{2}$. d) Sai vì cả hai '
                        'nghiệm đều dương.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 19: Phương trình bậc hai '
                 'một ẩn**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được phương trình bậc hai một '
                           'ẩn $ax^2 + bx + c = 0$ ($a \\neq 0$).',
                           'Trong **Bài 19: Phương trình bậc hai một ẩn**, quy tắc/công thức **Biệt thức '
                           '$\\Delta$** được viết là: $\\Delta = b^2 - 4ac$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\Delta = b^2 + 4ac$ thì kết quả của **Biệt '
                           'thức $\\Delta$** trong **Bài 19: Phương trình bậc hai một ẩn** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Giải phương trình $x^2 - 5x + 6 = 0$.”, kết quả giải đúng '
                           'là: Ta có $a = 1, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 '
                           '\\cdot 6 = 25 - 24 = 1 > 0$. Phương trình có hai nghiệm phân biệt...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 19: Phương trình bậc hai một ẩn. b) '
                        '**Đúng** theo công thức **Biệt thức $\\Delta$** ($\\Delta = b^2 - 4ac$). c) **Sai** '
                        'vì công thức đúng của **Biệt thức $\\Delta$** phải là $\\Delta = b^2 - 4ac$ chứ '
                        'không phải $\\Delta = b^2 + 4ac$. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Phương trình bậc hai một ẩn** để giải bài toán '
                 'sau: Giải phương trình $x^2 - 5x + 6 = 0$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $a = 1, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = '
                        '25 - 24 = 1 > 0$. Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{5 + 1}{2} = '
                        '3$...',
                        'Ta có $a = 1, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = '
                        '25 - 24 = 1 > 0$. Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{5 - 1}{2} = '
                        '3$...',
                        'Ta có $a = 1, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = '
                        '25 - 24 = 1 > 0$. Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{2}{5 + 1} = '
                        '3$...',
                        'Ta có $a = 2, b = -5, c = 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = '
                        '25 - 24 = 1 > 0$. Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{5 + 1}{2} = '
                        '3$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 19: Phương trình bậc hai một ẩn: Ta có $a = 1, b = -5, c '
                        '= 6$. Biệt thức $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 6 = 25 - 24 = 1 > 0$.\n'
                        'Phương trình có hai nghiệm phân biệt: $x_1 = \\dfrac{5 + 1}{2} = 3$ và $x_2 = '
                        '\\dfrac{5 - 1}{2} = 2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm giá trị của tham số $m$ để phương trình $x^2 - 4x + m = 0$ có nghiệm kép.',
            'answer': ['4'],
            'unit': None,
            'solution': "Phương trình có nghiệm kép khi $\\Delta' = (-2)^2 - 1 \\cdot m = 0 \\Leftrightarrow "
                        '4 - m = 0 \\Leftrightarrow m = 4$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch06-ham-so-phuong-trinh-bac-hai',
  'context_title': 'Chương VI: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn',
  'context': 'Chương VI · SGK Toán 9: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn.',
  'title': 'Bài 20: Định lí Viète và ứng dụng',
  'icon': '🔑',
  'description': 'Vận dụng định lí Viète để tính tổng, tích các nghiệm, nhẩm nghiệm và tìm hai số biết tổng '
                 'và tích.',
  'requirements': ['Phát biểu và vận dụng được định lí Viète để tính tổng và tích hai nghiệm của phương '
                   'trình bậc hai.',
                   'Nhẩm nghiệm phương trình bậc hai trong các trường hợp $a + b + c = 0$ hoặc $a - b + c = '
                   '0$.',
                   'Tìm được hai số khi biết tổng và tích của chúng.'],
  'definition': 'Định lí Viète: Nếu $x_1, x_2$ là hai nghiệm của phương trình $ax^2 + bx + c = 0$ ($a \\neq '
                '0$) thì $x_1 + x_2 = -\\dfrac{b}{a}$ và $x_1x_2 = \\dfrac{c}{a}$.',
  'theory': '1. Nhẩm nghiệm:\n'
            '- Nếu $a + b + c = 0$ thì phương trình có một nghiệm là $x_1 = 1$, nghiệm kia là $x_2 = '
            '\\dfrac{c}{a}$.\n'
            '- Nếu $a - b + c = 0$ thì phương trình có một nghiệm là $x_1 = -1$, nghiệm kia là $x_2 = '
            '-\\dfrac{c}{a}$.\n'
            '2. Tìm hai số biết tổng $S$ và tích $P$: Nếu hai số có tổng bằng $S$ và tích bằng $P$ ($S^2 - '
            '4P \\ge 0$) thì hai số đó là nghiệm của phương trình $x^2 - Sx + P = 0$.',
  'formulas': [{'category': 'Hệ thức Viète và ứng dụng',
                'items': [{'name': 'Hệ thức Viète',
                           'formula': '$S = x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$',
                           'note': 'Điều kiện có nghiệm: $\\Delta \\ge 0$'},
                          {'name': 'Biểu thức đối xứng thường gặp',
                           'formula': '$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$',
                           'note': 'Biểu diễn qua tổng $S$ và tích $P$'},
                          {'name': 'Phương trình tìm hai số',
                           'formula': '$x^2 - Sx + P = 0$ ($S^2 - 4P \\ge 0$)',
                           'note': 'Khi biết tổng $S$ và tích $P$'}]}],
  'example': 'Không giải phương trình, hãy tính $x_1^2 + x_2^2$ với $x_1, x_2$ là hai nghiệm của phương '
             'trình $x^2 - 5x + 3 = 0$.',
  'example_answer': 'Vì $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai nghiệm '
                    '$x_1, x_2$.\n'
                    'Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 3$.\n'
                    'Do đó $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = 5^2 - 2 \\cdot 3 = 19$.',
  'real_life': 'Tìm chiều dài và chiều rộng của một mảnh đất hình chữ nhật khi biết chu vi và diện tích của '
               'nó.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Gọi $x_1, x_2$ là hai nghiệm của phương trình $x^2 - 7x + 10 = 0$. Tổng $x_1 + x_2$ bằng:',
            'options': ['$-7$', '$10$', '$-10$', '$7$'],
            'answer': 3,
            'solution': 'Theo định lí Viète, $x_1 + x_2 = -\\dfrac{b}{a} = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hai số có tổng bằng $8$ và tích bằng $15$ là nghiệm của phương trình nào sau đây?',
            'options': ['$x^2 - 8x + 15 = 0$',
                        '$x^2 + 8x + 15 = 0$',
                        '$x^2 - 15x + 8 = 0$',
                        '$x^2 - 8x - 15 = 0$'],
            'answer': 0,
            'solution': 'Hai số có tổng $S = 8$, tích $P = 15$ là nghiệm của phương trình $x^2 - Sx + P = '
                        '0$, tức là $x^2 - 8x + 15 = 0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 20: Định lí Viète và ứng dụng**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Hệ thức Viète**?',
            'options': ['$S = x_1 - x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$',
                        '$S = x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$',
                        '$S = x_1 + x_2 = -\\dfrac{a}{b}$; $P = x_1x_2 = \\dfrac{c}{a}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $S = x_1 + x_2 = '
                        '-\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 20: Định lí Viète và ứng dụng, **Hệ thức Viète** '
                        'được xác định bởi: $S = x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$. '
                        '(Điều kiện có nghiệm: $\\Delta \\ge 0$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 20: Định lí Viète và ứng dụng**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Biểu thức đối xứng thường gặp**?',
            'options': ['$x_1^2 - x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$',
                        '$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^1 - 2P$',
                        '$x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$',
                        '$x_1^4 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$'],
            'answer': 2,
            'solution': 'Trong Bài 20: Định lí Viète và ứng dụng, **Biểu thức đối xứng thường gặp** có công '
                        'thức/quy tắc là: $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = S^2 - 2P$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phương trình $2025x^2 - 2026x + 1 = 0$ có hai nghiệm là:',
            'options': ['$x_1 = -1; x_2 = -\\dfrac{1}{2025}$',
                        '$x_1 = 1; x_2 = 2025$',
                        '$x_1 = -1; x_2 = \\dfrac{1}{2025}$',
                        '$x_1 = 1; x_2 = \\dfrac{1}{2025}$'],
            'answer': 3,
            'solution': 'Vì $a + b + c = 2025 - 2026 + 1 = 0$ nên phương trình có nghiệm $x_1 = 1$ và $x_2 = '
                        '\\dfrac{c}{a} = \\dfrac{1}{2025}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 20: Định lí Viète và ứng dụng**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Phát biểu và vận dụng được định lí Viète để tính tổng và tích hai nghiệm của phương '
                        'trình bậc hai.',
                        'Phát biểu và vận dụng được định lí Viète để tính tổng và tích hai nghiệm của phương '
                        'trình bậc hai. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Phát biểu và vận dụng được định lí Viète để tính tổng và '
                        'tích hai nghiệm của phương trình bậc hai.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phát biểu và vận dụng được định '
                        'lí Viète để tính tổng và tích hai nghiệm của phương trình bậc hai.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 20: Định lí Viète và ứng dụng: Phát biểu và vận dụng '
                        'được định lí Viète để tính tổng và tích hai nghiệm của phương trình bậc hai.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho phương trình bậc hai $x^2 - 6x + 4 = 0$ có hai nghiệm $x_1, x_2$.',
            'statements': ['Theo định lí Viète, ta có $x_1 + x_2 = 6$ và $x_1x_2 = 4$.',
                           'Hai nghiệm $x_1, x_2$ của phương trình đều là số dương.',
                           'Giá trị của biểu thức $x_1^2 + x_2^2$ bằng $36$.',
                           'Giá trị của biểu thức $\\dfrac{1}{x_1} + \\dfrac{1}{x_2}$ bằng $\\dfrac{3}{2}$.'],
            'answer': [True, True, False, True],
            'solution': "a) Đúng. b) Đúng vì $\\Delta' = 5 > 0, S = 6 > 0, P = 4 > 0$. c) Sai vì $x_1^2 + "
                        'x_2^2 = S^2 - 2P = 36 - 8 = 28$. d) Đúng vì $\\dfrac{x_1 + x_2}{x_1x_2} = '
                        '\\dfrac{6}{4} = \\dfrac{3}{2}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 20: Định lí Viète và ứng '
                 'dụng**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Phát biểu và vận dụng được định lí Viète '
                           'để tính tổng và tích hai nghiệm của phương trình bậc hai.',
                           'Trong **Bài 20: Định lí Viète và ứng dụng**, quy tắc/công thức **Hệ thức Viète** '
                           'được viết là: $S = x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $S = x_1 - x_2 = -\\dfrac{b}{a}$; $P = '
                           'x_1x_2 = \\dfrac{c}{a}$ thì kết quả của **Hệ thức Viète** trong **Bài 20: Định '
                           'lí Viète và ứng dụng** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Không giải phương trình, hãy tính $x_1^2 + x_2^2$ với $x_1, '
                           'x_2$ là hai nghiệm của phương trình $x^2 - 5x + 3 = 0$.”, kết quả giải đúng là: '
                           'Vì $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai '
                           'nghiệm $x_1, x_2$. Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 3$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 20: Định lí Viète và ứng dụng. b) **Đúng** '
                        'theo công thức **Hệ thức Viète** ($S = x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = '
                        '\\dfrac{c}{a}$). c) **Sai** vì công thức đúng của **Hệ thức Viète** phải là $S = '
                        'x_1 + x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$ chứ không phải $S = x_1 - '
                        'x_2 = -\\dfrac{b}{a}$; $P = x_1x_2 = \\dfrac{c}{a}$. d) **Đúng** theo lời giải ví '
                        'dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 20: Định lí Viète và ứng dụng** để giải bài toán '
                 'sau: Không giải phương trình, hãy tính $x_1^2 + x_2^2$ với $x_1, x_2$ là hai nghiệm của '
                 'phương trình $x^2 - 5x + 3 = 0$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai nghiệm '
                        '$x_1, x_2$. Theo định lí Viète: $x_1 - x_2 = 5$ và $x_1x_2 = 3$. Do đ...',
                        'Vì $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai nghiệm '
                        '$x_1, x_2$. Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 3$. Do đ...',
                        'Vì $\\Delta = (-5)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai nghiệm '
                        '$x_1, x_2$. Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 2$. Do đ...',
                        'Vì $\\Delta = (-10)^2 - 4 \\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai '
                        'nghiệm $x_1, x_2$. Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 3$. Do đ...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 20: Định lí Viète và ứng dụng: Vì $\\Delta = (-5)^2 - 4 '
                        '\\cdot 1 \\cdot 3 = 13 > 0$ nên phương trình có hai nghiệm $x_1, x_2$.\n'
                        'Theo định lí Viète: $x_1 + x_2 = 5$ và $x_1x_2 = 3$.\n'
                        'Do đó $x_1^2 + x_2^2 = (x_1 + x_2)^2 - 2x_1x_2 = 5^2 - 2 \\cdot 3 = 19$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho phương trình $x^2 - 4x + 1 = 0$ có hai nghiệm $x_1, x_2$. Tính giá trị của biểu thức '
                 '$A = x_1^2 + x_2^2$.',
            'answer': ['14'],
            'unit': None,
            'solution': 'Theo định lí Viète: $x_1 + x_2 = 4$ và $x_1x_2 = 1$. Do đó $A = (x_1 + x_2)^2 - '
                        '2x_1x_2 = 4^2 - 2 \\cdot 1 = 14$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch06-ham-so-phuong-trinh-bac-hai',
  'context_title': 'Chương VI: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn',
  'context': 'Chương VI · SGK Toán 9: Hàm số y = ax² (a ≠ 0). Phương trình bậc hai một ẩn.',
  'title': 'Bài 21: Giải bài toán bằng cách lập phương trình',
  'icon': '🎯',
  'description': 'Vận dụng phương trình bậc hai một ẩn để giải các bài toán thực tế về hình học, chuyển '
                 'động, năng suất.',
  'requirements': ['Biểu diễn được các đại lượng chưa biết qua một ẩn và lập phương trình bậc hai.',
                   'Giải được phương trình và đối chiếu điều kiện thực tế để trả lời bài toán.',
                   'Vận dụng kiến thức của **Bài 21: Giải bài toán bằng cách lập phương trình** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giải bài toán bằng cách lập phương trình bậc hai gồm 3 bước: Lập phương trình (chọn ẩn, đặt '
                'điều kiện, lập phương trình); Giải phương trình; Kiểm tra điều kiện và kết luận.',
  'theory': 'Khi giải bài toán bằng cách lập phương trình bậc hai, phương trình thường có hai nghiệm nhưng '
            'cần kiểm tra chặt chẽ điều kiện thực tế của ẩn (ví dụ: số người, số sản phẩm phải là số nguyên '
            'dương; độ dài hình học, vận tốc, thời gian phải là số dương) để loại nghiệm không phù hợp.',
  'formulas': [{'category': 'Các mô hình bài toán thực tế',
                'items': [{'name': 'Hình chữ nhật',
                           'formula': 'Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 + y^2}$',
                           'note': '$x, y > 0$ là hai kích thước'},
                          {'name': 'Chuyển động đều',
                           'formula': '$t = \\dfrac{s}{v}$',
                           'note': 'Hiệu hoặc tổng thời gian dẫn tới phương trình chứa ẩn ở mẫu quy về bậc '
                                   'hai'}]}],
  'example': 'Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng $4$ m và diện tích bằng $60\\text{ '
             'm}^2$. Tính chiều rộng của mảnh đất.',
  'example_answer': 'Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là $x + 4$ (m).\n'
                    'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                    '\\Leftrightarrow x^2 + 4x - 60 = 0$.\n'
                    'Giải phương trình được $x_1 = 6$ (thỏa mãn) và $x_2 = -10$ (loại).\n'
                    'Vậy chiều rộng của mảnh đất là $6$ m.',
  'real_life': 'Thiết kế lối đi xung quanh vườn hoa hình chữ nhật sao cho diện tích phần trồng hoa đạt mức '
               'quy định.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Gọi $x$ ($x \\in \\mathbb{N}^*$) là số tự nhiên nhỏ hơn trong hai số tự nhiên liên tiếp có '
                 'tích bằng $72$. Phương trình lập được là:',
            'options': ['$x(x + 1) = 72$', '$x(x - 1) = 72$', '$x + (x + 1) = 72$', '$x^2 + 72 = 0$'],
            'answer': 0,
            'solution': 'Hai số tự nhiên liên tiếp là $x$ và $x + 1$, tích của chúng bằng $72$ nên $x(x + 1) '
                        '= 72$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một tam giác vuông có hai cạnh góc vuông hơn kém nhau $2$ cm. Nếu gọi cạnh góc vuông nhỏ '
                 'là $x$ (cm) ($x > 0$) thì diện tích tam giác vuông đó là:',
            'options': ['$x(x + 2)$ ($\\text{cm}^2$)',
                        '$\\dfrac{1}{2}x(x + 2)$ ($\\text{cm}^2$)',
                        '$\\dfrac{1}{2}x(x - 2)$ ($\\text{cm}^2$)',
                        '$2x(x + 2)$ ($\\text{cm}^2$)'],
            'answer': 1,
            'solution': 'Cạnh góc vuông lớn là $x + 2$ (cm), diện tích tam giác vuông là $\\dfrac{1}{2}x(x + '
                        '2)$ ($\\text{cm}^2$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Giải bài toán bằng cách lập phương trình**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Hình chữ nhật**?',
            'options': ['Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 - y^2}$',
                        'Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 + y^1}$',
                        'Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 + y^2}$',
                        'Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^4 + y^2}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 21: Giải bài toán bằng cách lập phương trình, '
                        '**Hình chữ nhật** được xác định bởi: Diện tích $S = x \\cdot y$; Đường chéo $d = '
                        '\\sqrt{x^2 + y^2}$. ($x, y > 0$ là hai kích thước)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Giải bài toán bằng cách lập phương trình**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Chuyển động đều**?',
            'options': ['$t = \\dfrac{s}{v}$ (với dấu ngược lại)',
                        '$t = \\dfrac{v}{s}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $t = \\dfrac{s}{v}$',
                        '$t = \\dfrac{s}{v}$'],
            'answer': 3,
            'solution': 'Trong Bài 21: Giải bài toán bằng cách lập phương trình, **Chuyển động đều** có công '
                        'thức/quy tắc là: $t = \\dfrac{s}{v}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một tổ công nhân dự định làm $120$ sản phẩm. Nếu gọi năng suất dự định là $x$ (sản '
                 'phẩm/giờ, $x \\in \\mathbb{N}^*$), khi tăng năng suất thêm $5$ sản phẩm/giờ thì thời gian '
                 'hoàn thành giảm đi bao nhiêu giờ?',
            'options': ['$\\dfrac{120}{x} - \\dfrac{120}{x + 5}$ (giờ)',
                        '$\\dfrac{120}{x + 5} - \\dfrac{120}{x}$ (giờ)',
                        '$\\dfrac{120}{x} + \\dfrac{120}{x + 5}$ (giờ)',
                        '$120(x + 5) - 120x$ (giờ)'],
            'answer': 0,
            'solution': 'Thời gian dự định là $\\dfrac{120}{x}$ giờ, thời gian thực tế là $\\dfrac{120}{x + '
                        '5}$ giờ, nên thời gian giảm đi là $\\dfrac{120}{x} - \\dfrac{120}{x + 5}$ giờ.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 21: Giải bài toán bằng cách lập phương trình**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Biểu diễn được các đại lượng chưa biết qua một ẩn và lập phương trình bậc hai. (với '
                        'dấu ngược lại)',
                        'Biểu diễn được các đại lượng chưa biết qua một ẩn và lập phương trình bậc hai.',
                        'Đảo ngược vế của quy tắc: Biểu diễn được các đại lượng chưa biết qua một ẩn và lập '
                        'phương trình bậc hai.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Biểu diễn được các đại lượng '
                        'chưa biết qua một ẩn và lập phương trình bậc hai.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 21: Giải bài toán bằng cách lập phương trình: Biểu '
                        'diễn được các đại lượng chưa biết qua một ẩn và lập phương trình bậc hai.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một mảnh vườn hình chữ nhật có chu vi $28$ m và diện tích $48\\text{ m}^2$. Gọi chiều rộng '
                 'của mảnh vườn là $x$ (m) ($0 < x < 7$).',
            'statements': ['Nửa chu vi của mảnh vườn bằng $14$ m.',
                           'Chiều dài của mảnh vườn được biểu diễn theo $x$ là $14 - x$ (m).',
                           'Phương trình biểu thị diện tích mảnh vườn là $x^2 - 14x + 48 = 0$.',
                           'Chiều rộng của mảnh vườn là $8$ m.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $28 : 2 = 14$ m. b) Đúng. c) Đúng vì $x(14 - x) = 48 \\Leftrightarrow '
                        'x^2 - 14x + 48 = 0$. d) Sai vì $0 < x < 7$ nên chiều rộng là $x = 6$ m (chiều dài '
                        'là $8$ m).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 21: Giải bài toán bằng cách '
                 'lập phương trình**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Biểu diễn được các đại lượng chưa biết '
                           'qua một ẩn và lập phương trình bậc hai.',
                           'Trong **Bài 21: Giải bài toán bằng cách lập phương trình**, quy tắc/công thức '
                           '**Hình chữ nhật** được viết là: Diện tích $S = x \\cdot y$; Đường chéo $d = '
                           '\\sqrt{x^2 + y^2}$.',
                           'Nếu áp dụng sai dấu/phép tính thành Diện tích $S = x \\cdot y$; Đường chéo $d = '
                           '\\sqrt{x^2 - y^2}$ thì kết quả của **Hình chữ nhật** trong **Bài 21: Giải bài '
                           'toán bằng cách lập phương trình** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng $4$ m '
                           'và diện tích bằng $60\\text{ m}^2$. Tính chiều rộng của mảnh đất.”, kết quả giải '
                           'đúng là: Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là '
                           '$x + 4$ (m). Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có p...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 21: Giải bài toán bằng cách lập phương '
                        'trình. b) **Đúng** theo công thức **Hình chữ nhật** (Diện tích $S = x \\cdot y$; '
                        'Đường chéo $d = \\sqrt{x^2 + y^2}$). c) **Sai** vì công thức đúng của **Hình chữ '
                        'nhật** phải là Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 + y^2}$ chứ '
                        'không phải Diện tích $S = x \\cdot y$; Đường chéo $d = \\sqrt{x^2 - y^2}$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 21: Giải bài toán bằng cách lập phương trình** để '
                 'giải bài toán sau: Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng $4$ m và diện '
                 'tích bằng $60\\text{ m}^2$. Tính chiều rộng của mảnh đất. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là $x - 4$ (m). '
                        'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                        '\\Leftrightarrow x^2 + 4x - 60 = 0$...',
                        'Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là $x + 4$ (m). '
                        'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                        '\\Leftrightarrow x^2 + 4x - 60 = 1$...',
                        'Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là $x + 4$ (m). '
                        'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                        '\\Leftrightarrow x^2 + 4x - 60 = 0$...',
                        'Gọi chiều rộng của mảnh đất là $x$ (m) ($x > 2$), khi đó chiều dài là $x + 4$ (m). '
                        'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                        '\\Leftrightarrow x^2 + 4x - 60 = 0$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 21: Giải bài toán bằng cách lập phương trình: Gọi chiều '
                        'rộng của mảnh đất là $x$ (m) ($x > 0$), khi đó chiều dài là $x + 4$ (m).\n'
                        'Vì diện tích mảnh đất là $60\\text{ m}^2$ nên ta có phương trình: $x(x + 4) = 60 '
                        '\\Leftrightarrow x^2 + 4x - 60 = 0$.\n'
                        'Giải phương trình được $x_1 = 6$ (thỏa mãn) và $x_2 = -10$ (loại).\n'
                        'Vậy chiều rộng của mảnh đất là $6$ m.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một giải cờ vua đấu vòng tròn một lượt (mỗi kỳ thủ đấu với từng kỳ thủ khác đúng 1 '
                 'ván), ban tổ chức đếm được tổng cộng $45$ ván cờ. Hỏi có bao nhiêu kỳ thủ tham gia giải?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Gọi số kỳ thủ là $x$ ($x \\in \\mathbb{N}, x \\ge 2$). Số ván cờ là $\\dfrac{x(x - '
                        '1)}{2} = 45 \\Leftrightarrow x^2 - x - 90 = 0 \\Rightarrow x = 10$ (nhận) hoặc $x = '
                        '-9$ (loại).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch07-tan-so-thong-ke',
  'context_title': 'Chương VII: Tần số và tần số tương đối',
  'context': 'Chương VII · SGK Toán 9: Tần số và tần số tương đối.',
  'title': 'Bài 22: Bảng tần số và biểu đồ tần số',
  'icon': '📊',
  'description': 'Lập bảng tần số và đọc, phân tích dữ liệu từ biểu đồ tần số.',
  'requirements': ['Xác định được tần số của một giá trị trong mẫu dữ liệu thống kê.',
                   'Lập được bảng tần số và đọc, giải thích được biểu đồ tần số (biểu đồ cột, biểu đồ đoạn '
                   'thẳng).',
                   'Vận dụng kiến thức của **Bài 22: Bảng tần số và biểu đồ tần số** để giải bài tập minh '
                   'họa và bài toán thực tiễn.'],
  'definition': 'Số lần xuất hiện của một giá trị trong mẫu dữ liệu được gọi là tần số của giá trị đó. Bảng '
                'biểu diễn các giá trị cùng với tần số của chúng được gọi là bảng tần số.',
  'theory': '1. Tổng tất cả các tần số của các giá trị khác nhau trong bảng tần số luôn bằng cỡ mẫu $N$ ($N '
            '= m_1 + m_2 + \\dots + m_k$).\n'
            '2. Để biểu diễn trực quan bảng tần số, người ta thường dùng biểu đồ tần số dạng cột hoặc biểu '
            'đồ đoạn thẳng.',
  'formulas': [{'category': 'Tần số và cỡ mẫu',
                'items': [{'name': 'Cỡ mẫu',
                           'formula': '$N = m_1 + m_2 + \\dots + m_k$',
                           'note': '$m_i$ là tần số của giá trị $x_i$'}]}],
  'example': 'Điểm kiểm tra của 10 học sinh là: $7, 8, 8, 9, 7, 10, 8, 9, 8, 7$. Tìm tần số của điểm $8$.',
  'example_answer': 'Trong dãy dữ liệu trên, giá trị $8$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m = '
                    '4$.',
  'real_life': 'Thống kê số lượng từng cỡ giày bán được trong tháng của một cửa hàng để lên kế hoạch nhập '
               'hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số lần xuất hiện của một giá trị trong mẫu dữ liệu thống kê được gọi là:',
            'options': ['Cỡ mẫu', 'Tần số của giá trị đó', 'Số trung bình', 'Tần số tương đối'],
            'answer': 1,
            'solution': 'Theo định nghĩa, số lần xuất hiện của một giá trị trong mẫu dữ liệu gọi là tần số '
                        'của giá trị đó.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Cho mẫu dữ liệu về số con trong 8 hộ gia đình: $1, 2, 2, 1, 3, 2, 2, 1$. Tần số của giá '
                 'trị $2$ là:',
            'options': ['$3$', '$2$', '$4$', '$8$'],
            'answer': 2,
            'solution': 'Số $2$ xuất hiện $4$ lần trong mẫu dữ liệu nên tần số của nó là $4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: Bảng tần số và biểu đồ tần số**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Cỡ mẫu**?',
            'options': ['$N = m_1 - m_2 + \\dots + m_k$',
                        'Đảo ngược vế của quy tắc: $N = m_1 + m_2 + \\dots + m_k$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $N = m_1 + m_2 + \\dots + m_k$',
                        '$N = m_1 + m_2 + \\dots + m_k$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 22: Bảng tần số và biểu đồ tần số, **Cỡ mẫu** được '
                        'xác định bởi: $N = m_1 + m_2 + \\dots + m_k$. ($m_i$ là tần số của giá trị $x_i$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo định nghĩa trong **Bài 22: Bảng tần số và biểu đồ tần số**, khẳng định nào dưới đây '
                 'là **đúng**?',
            'options': ['Số lần xuất hiện của một giá trị trong mẫu dữ liệu được gọi là tần số của giá trị '
                        'đó. Bảng biểu diễn các giá trị cùng với tần số c...',
                        'Số lần xuất hiện của một giá trị trong mẫu dữ liệu được gọi là tần số của giá trị '
                        'đó. Bảng biểu diễn các giá trị cùng với tần số c... (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Số lần xuất hiện của một giá trị trong mẫu dữ liệu được '
                        'gọi là tần số của giá trị đó. Bảng biểu diễn các giá trị cùng với tần số c...',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Số lần xuất hiện của một giá '
                        'trị trong mẫu dữ liệu được gọi là tần số của giá trị đó. Bảng biểu diễn các giá trị '
                        'cùng với tần số c...'],
            'answer': 0,
            'solution': 'Theo định nghĩa của Bài 22: Bảng tần số và biểu đồ tần số: Số lần xuất hiện của một '
                        'giá trị trong mẫu dữ liệu được gọi là tần số của giá trị đó. Bảng biểu diễn các giá '
                        'trị cùng với tần số c...'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một bảng tần số thống kê điểm thi của một lớp có 4 mức điểm $6, 7, 8, 9$ với tần số lần '
                 'lượt là $5, 12, x, 8$. Biết sĩ số lớp là $40$ học sinh, giá trị của $x$ là:',
            'options': ['$25$', '$15$', '$10$', '$12$'],
            'answer': 1,
            'solution': 'Tổng các tần số bằng cỡ mẫu $N = 40 \\Rightarrow 5 + 12 + x + 8 = 40 \\Rightarrow x '
                        '= 15$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 22: Bảng tần số và biểu đồ tần số**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Xác định được tần số của một giá trị trong mẫu dữ liệu thống kê. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Xác định được tần số của một giá trị trong mẫu dữ liệu '
                        'thống kê.',
                        'Xác định được tần số của một giá trị trong mẫu dữ liệu thống kê.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Xác định được tần số của một '
                        'giá trị trong mẫu dữ liệu thống kê.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 22: Bảng tần số và biểu đồ tần số: Xác định được tần '
                        'số của một giá trị trong mẫu dữ liệu thống kê.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Khảo sát số quyển sách đọc trong tháng của một nhóm học sinh thu được bảng tần số: giá trị '
                 '$1$ (tần số $4$), giá trị $2$ (tần số $10$), giá trị $3$ (tần số $6$).',
            'statements': ['Tổng số học sinh được khảo sát (cỡ mẫu) là $N = 20$.',
                           'Tần số của giá trị $2$ quyển sách là $10$.',
                           'Giá trị có tần số lớn nhất là $3$ quyển sách.',
                           'Có tổng cộng $16$ học sinh đọc từ $2$ quyển sách trở lên.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $N = 4 + 10 + 6 = 20$. b) Đúng. c) Sai vì giá trị $2$ có tần số lớn nhất '
                        'là $10$. d) Đúng vì $10 + 6 = 16$ học sinh.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 22: Bảng tần số và biểu đồ '
                 'tần số**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Xác định được tần số của một giá trị '
                           'trong mẫu dữ liệu thống kê.',
                           'Trong **Bài 22: Bảng tần số và biểu đồ tần số**, quy tắc/công thức **Cỡ mẫu** '
                           'được viết là: $N = m_1 + m_2 + \\dots + m_k$.',
                           'Nếu áp dụng sai dấu/phép tính thành $N = m_1 - m_2 + \\dots + m_k$ thì kết quả '
                           'của **Cỡ mẫu** trong **Bài 22: Bảng tần số và biểu đồ tần số** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Điểm kiểm tra của 10 học sinh là: $7, 8, 8, 9, 7, 10, 8, 9, '
                           '8, 7$. Tìm tần số của điểm $8$.”, kết quả giải đúng là: Trong dãy dữ liệu trên, '
                           'giá trị $8$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m = 4$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 22: Bảng tần số và biểu đồ tần số. b) '
                        '**Đúng** theo công thức **Cỡ mẫu** ($N = m_1 + m_2 + \\dots + m_k$). c) **Sai** vì '
                        'công thức đúng của **Cỡ mẫu** phải là $N = m_1 + m_2 + \\dots + m_k$ chứ không phải '
                        '$N = m_1 - m_2 + \\dots + m_k$. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 22: Bảng tần số và biểu đồ tần số** để giải bài '
                 'toán sau: Điểm kiểm tra của 10 học sinh là: $7, 8, 8, 9, 7, 10, 8, 9, 8, 7$. Tìm tần số '
                 'của điểm $8$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Trong dãy dữ liệu trên, giá trị $9$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m '
                        '= 4$.',
                        'Trong dãy dữ liệu trên, giá trị $8$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m '
                        '= 3$.',
                        'Trong dãy dữ liệu trên, giá trị $16$ xuất hiện $4$ lần nên tần số của điểm $8$ là '
                        '$m = 4$.',
                        'Trong dãy dữ liệu trên, giá trị $8$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m '
                        '= 4$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 22: Bảng tần số và biểu đồ tần số: Trong dãy dữ liệu '
                        'trên, giá trị $8$ xuất hiện $4$ lần nên tần số của điểm $8$ là $m = 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gieo một con xúc xắc 20 lần, kết quả số chấm xuất hiện từ 1 đến 5 chấm có tần số lần lượt '
                 'là $3, 4, 2, 5, 3$. Hỏi mặt 6 chấm xuất hiện bao nhiêu lần?',
            'answer': ['3'],
            'unit': None,
            'solution': 'Tần số xuất hiện mặt 6 chấm là $20 - (3 + 4 + 2 + 5 + 3) = 20 - 17 = 3$ (lần).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch07-tan-so-thong-ke',
  'context_title': 'Chương VII: Tần số và tần số tương đối',
  'context': 'Chương VII · SGK Toán 9: Tần số và tần số tương đối.',
  'title': 'Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối',
  'icon': '🥧',
  'description': 'Tính tần số tương đối, lập bảng tần số tương đối và đọc biểu đồ hình quạt tròn, biểu đồ '
                 'cột.',
  'requirements': ['Tính được tần số tương đối của một giá trị trong mẫu dữ liệu.',
                   'Lập được bảng tần số tương đối và vẽ/đọc được biểu đồ tần số tương đối (biểu đồ cột, '
                   'biểu đồ hình quạt tròn).',
                   'Vận dụng kiến thức của **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Tần số tương đối $f_i$ của giá trị $x_i$ là tỉ số giữa tần số $m_i$ của giá trị đó và cỡ '
                'mẫu $N$: $f_i = \\dfrac{m_i}{N}$ (thường được viết dưới dạng phần trăm).',
  'theory': '1. Tổng tất cả các tần số tương đối của các giá trị khác nhau trong mẫu dữ liệu luôn bằng $1$ '
            '(tức là $100\\%$). Từ tần số tương đối $f_i$ và cỡ mẫu $N$, ta tính lại được tần số $m_i = N '
            '\\cdot f_i$.\n'
            '2. Biểu đồ hình quạt tròn rất thích hợp để biểu diễn bảng tần số tương đối.',
  'formulas': [{'category': 'Công thức tần số tương đối',
                'items': [{'name': 'Tần số tương đối',
                           'formula': '$f_i = \\dfrac{m_i}{N} \\cdot 100\\%$',
                           'note': '$m_i$ là tần số, $N$ là cỡ mẫu'},
                          {'name': 'Tính tần số từ tần số tương đối',
                           'formula': '$m_i = N \\cdot f_i$',
                           'note': 'Tổng $f_1 + f_2 + \\dots + f_k = 100\\%$'}]}],
  'example': 'Trong một lớp 40 học sinh, có 10 học sinh đạt điểm Giỏi. Tính tần số tương đối của mức điểm '
             'Giỏi.',
  'example_answer': 'Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{10}{40} \\cdot 100\\% = 25\\%$.',
  'real_life': 'Thống kê tỉ lệ phần trăm thị phần của các hãng điện thoại hoặc tỉ lệ các nhóm máu trong cộng '
               'đồng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho mẫu dữ liệu có cỡ mẫu $N = 50$, một giá trị có tần số $m = 15$. Tần số tương đối của '
                 'giá trị đó là:',
            'options': ['$15\\%$', '$50\\%$', '$30\\%$', '$35\\%$'],
            'answer': 2,
            'solution': 'Ta có $f = \\dfrac{15}{50} \\cdot 100\\% = 30\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tổng các tần số tương đối của tất cả các giá trị trong bảng tần số tương đối luôn bằng:',
            'options': ['$50\\%$', 'Cỡ mẫu $N$', '$10\\%$', '$100\\%$'],
            'answer': 3,
            'solution': 'Tổng tất cả các tần số tương đối luôn bằng $1$ hay $100\\%$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Tần số tương đối**?',
            'options': ['$f_i = \\dfrac{m_i}{N} \\cdot 100\\%$',
                        '$f_i = \\dfrac{m_i}{N} : 100\\%$',
                        '$f_i = \\dfrac{N}{m_i} \\cdot 100\\%$',
                        '$f_i = \\dfrac{m_i}{N} \\cdot 102\\%$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 23: Bảng tần số tương đối và biểu đồ tần số tương '
                        'đối, **Tần số tương đối** được xác định bởi: $f_i = \\dfrac{m_i}{N} \\cdot 100\\%$. '
                        '($m_i$ là tần số, $N$ là cỡ mẫu)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Tính tần số từ tần số tương đối**?',
            'options': ['$m_i = N : f_i$',
                        '$m_i = N \\cdot f_i$',
                        'Đảo ngược vế của quy tắc: $m_i = N \\cdot f_i$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $m_i = N \\cdot f_i$'],
            'answer': 1,
            'solution': 'Trong Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối, **Tính tần số từ '
                        'tần số tương đối** có công thức/quy tắc là: $m_i = N \\cdot f_i$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Khảo sát 200 khách hàng về mức độ hài lòng, tần số tương đối của mức 'Rất hài lòng' là "
                 "$45\\%$. Số khách hàng chọn 'Rất hài lòng' là:",
            'options': ['$45$', '$110$', '$90$', '$100$'],
            'answer': 2,
            'solution': 'Tần số là $m = 200 \\cdot 45\\% = 90$ (khách hàng).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được tần số tương đối của một giá trị trong mẫu dữ liệu. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tính được tần số tương đối của một giá trị trong mẫu dữ '
                        'liệu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được tần số tương đối của '
                        'một giá trị trong mẫu dữ liệu.',
                        'Tính được tần số tương đối của một giá trị trong mẫu dữ liệu.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 23: Bảng tần số tương đối và biểu đồ tần số tương '
                        'đối: Tính được tần số tương đối của một giá trị trong mẫu dữ liệu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một cuộc khảo sát phương tiện đến trường của học sinh khối 9 cho kết quả tần số tương đối: '
                 'Xe đạp ($50\\%$), Xe buýt ($20\\%$), Đi bộ ($15\\%$), Người thân đưa đón ($x\\%$).',
            'statements': ['Giá trị của $x$ bằng $15$.',
                           'Trên biểu đồ hình quạt tròn, hình quạt biểu diễn học sinh đi xe đạp chiếm một '
                           'nửa hình tròn.',
                           'Số đo cung tương ứng với hình quạt biểu diễn học sinh đi xe buýt là $72^\\circ$.',
                           'Nếu có $60$ học sinh đi xe buýt thì tổng số học sinh được khảo sát là $200$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $100 - (50 + 20 + 15) = 15$. b) Đúng vì $50\\%$ ứng với nửa hình tròn. '
                        'c) Đúng vì $20\\% \\cdot 360^\\circ = 72^\\circ$. d) Sai vì $N = 60 : 20\\% = 300$ '
                        'học sinh.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 23: Bảng tần số tương đối '
                 'và biểu đồ tần số tương đối**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Tính được tần số tương đối của một giá '
                           'trị trong mẫu dữ liệu.',
                           'Trong **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối**, quy '
                           'tắc/công thức **Tần số tương đối** được viết là: $f_i = \\dfrac{m_i}{N} \\cdot '
                           '100\\%$.',
                           'Nếu áp dụng sai dấu/phép tính thành $f_i = \\dfrac{m_i}{N} : 100\\%$ thì kết quả '
                           'của **Tần số tương đối** trong **Bài 23: Bảng tần số tương đối và biểu đồ tần số '
                           'tương đối** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Trong một lớp 40 học sinh, có 10 học sinh đạt điểm Giỏi. '
                           'Tính tần số tương đối của mức điểm Giỏi.”, kết quả giải đúng là: Tần số tương '
                           'đối của mức điểm Giỏi là $f = \\dfrac{10}{40} \\cdot 100\\% = 25\\%$.'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 23: Bảng tần số tương đối và biểu đồ tần '
                        'số tương đối. b) **Đúng** theo công thức **Tần số tương đối** ($f_i = '
                        '\\dfrac{m_i}{N} \\cdot 100\\%$). c) **Sai** vì công thức đúng của **Tần số tương '
                        'đối** phải là $f_i = \\dfrac{m_i}{N} \\cdot 100\\%$ chứ không phải $f_i = '
                        '\\dfrac{m_i}{N} : 100\\%$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 23: Bảng tần số tương đối và biểu đồ tần số tương '
                 'đối** để giải bài toán sau: Trong một lớp 40 học sinh, có 10 học sinh đạt điểm Giỏi. Tính '
                 'tần số tương đối của mức điểm Giỏi. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{10}{40} \\cdot 100\\% = 25\\%$.',
                        'Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{10}{40} : 100\\% = 25\\%$.',
                        'Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{40}{10} \\cdot 100\\% = 25\\%$.',
                        'Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{20}{40} \\cdot 100\\% = 25\\%$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 23: Bảng tần số tương đối và biểu đồ tần số tương đối: '
                        'Tần số tương đối của mức điểm Giỏi là $f = \\dfrac{10}{40} \\cdot 100\\% = 25\\%$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một mẫu dữ liệu gồm $80$ số liệu, giá trị $x_1$ xuất hiện $20$ lần. Tần số tương đối '
                 'của $x_1$ bằng bao nhiêu phần trăm (chỉ ghi số)?',
            'answer': ['25'],
            'unit': None,
            'solution': 'Tần số tương đối của $x_1$ là $f_1 = \\dfrac{20}{80} \\cdot 100\\% = 25\\%$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch07-tan-so-thong-ke',
  'context_title': 'Chương VII: Tần số và tần số tương đối',
  'context': 'Chương VII · SGK Toán 9: Tần số và tần số tương đối.',
  'title': 'Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ',
  'icon': '📶',
  'description': 'Lập bảng tần số, tần số tương đối ghép nhóm và đọc biểu đồ tần số ghép nhóm.',
  'requirements': ['Hiểu được ý nghĩa của việc ghép nhóm dữ liệu và lập được bảng tần số, tần số tương đối '
                   'ghép nhóm.',
                   'Đọc và phân tích được biểu đồ tần số tương đối ghép nhóm (dạng cột và dạng đoạn thẳng).',
                   'Vận dụng kiến thức của **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi mẫu số liệu có nhiều giá trị khác nhau, người ta thường chia miền giá trị thành các nửa '
                'khoảng $[a; b)$ (gọi là các nhóm) và đếm số giá trị rơi vào mỗi nhóm để lập bảng tần số '
                'ghép nhóm.',
  'theory': '1. Nhóm $[a; b)$ gồm các giá trị $x$ thỏa mãn $a \\le x < b$. Độ dài của nhóm $[a; b)$ là $b - '
            'a$, giá trị đại diện của nhóm là $c = \\dfrac{a + b}{2}$.\n'
            '2. Tần số tương đối của một nhóm là tỉ số giữa tần số của nhóm đó và cỡ mẫu $N$.',
  'formulas': [{'category': 'Số liệu ghép nhóm',
                'items': [{'name': 'Quy ước nhóm $[a; b)$',
                           'formula': '$a \\le x < b$',
                           'note': 'Bao gồm đầu mút trái $a$, không bao gồm đầu mút phải $b$'},
                          {'name': 'Giá trị đại diện của nhóm',
                           'formula': '$c_i = \\dfrac{a_i + b_i}{2}$',
                           'note': 'Dùng để vẽ biểu đồ đoạn thẳng'}]}],
  'example': 'Cho nhóm chiều cao $[155; 160)$ (cm). Hỏi học sinh cao $160$ cm có thuộc nhóm này không? Tìm '
             'giá trị đại diện của nhóm.',
  'example_answer': 'Nhóm $[155; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ cm không '
                    'thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$).\n'
                    'Giá trị đại diện của nhóm là $\\dfrac{155 + 160}{2} = 157,5$ (cm).',
  'real_life': 'Phân nhóm thời gian chờ xe buýt, chiều cao học sinh hoặc mức thu nhập bình quân trong các '
               'cuộc điều tra dân số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị nào sau đây thuộc nhóm $[10; 15)$?',
            'options': ['$15$', '$9,9$', '$15,5$', '$10$'],
            'answer': 3,
            'solution': 'Nhóm $[10; 15)$ gồm các số $x$ thỏa mãn $10 \\le x < 15$, nên số $10$ thuộc nhóm '
                        'này.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Giá trị đại diện của nhóm $[20; 30)$ là:',
            'options': ['$25$', '$20$', '$30$', '$10$'],
            'answer': 0,
            'solution': 'Giá trị đại diện là trung bình cộng hai đầu mút: $\\dfrac{20 + 30}{2} = 25$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Quy ước nhóm $[a; b)$**?',
            'options': ['$a \\ge x < b$',
                        '$a \\le x < b$',
                        'Đảo ngược vế của quy tắc: $a \\le x < b$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a \\le x < b$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 24: Bảng tần số, tần số tương đối ghép nhóm và '
                        'biểu đồ, **Quy ước nhóm $[a; b)$** được xác định bởi: $a \\le x < b$. (Bao gồm đầu '
                        'mút trái $a$, không bao gồm đầu mút phải $b$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Giá trị đại diện của nhóm**?',
            'options': ['$c_i = \\dfrac{a_i - b_i}{2}$',
                        '$c_i = \\dfrac{2}{a_i + b_i}$',
                        '$c_i = \\dfrac{a_i + b_i}{2}$',
                        '$c_i = \\dfrac{a_i + b_i}{4}$'],
            'answer': 2,
            'solution': 'Trong Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ, **Giá trị đại '
                        'diện của nhóm** có công thức/quy tắc là: $c_i = \\dfrac{a_i + b_i}{2}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thời gian hoàn thành bài tập (phút) của 40 học sinh được chia thành 4 nhóm: $[5; 10)$, '
                 '$[10; 15)$, $[15; 20)$, $[20; 25)$ với tần số lần lượt là $6, 14, 12, 8$. Tần số tương đối '
                 'của nhóm $[10; 15)$ là:',
            'options': ['$14\\%$', '$30\\%$', '$20\\%$', '$35\\%$'],
            'answer': 3,
            'solution': 'Tần số tương đối của nhóm $[10; 15)$ là $f = \\dfrac{14}{40} \\cdot 100\\% = '
                        '35\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Hiểu được ý nghĩa của việc ghép nhóm dữ liệu và lập được bảng tần số, tần số tương '
                        'đối ghép nhóm.',
                        'Hiểu được ý nghĩa của việc ghép nhóm dữ liệu và lập được bảng tần số, tần số tương '
                        'đối ghép nhóm. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Hiểu được ý nghĩa của việc ghép nhóm dữ liệu và lập được '
                        'bảng tần số, tần số tương đối ghép nhóm.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hiểu được ý nghĩa của việc ghép '
                        'nhóm dữ liệu và lập được bảng tần số, tần số tương đối ghép nhóm.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu '
                        'đồ: Hiểu được ý nghĩa của việc ghép nhóm dữ liệu và lập được bảng tần số, tần số '
                        'tương đối ghép nhóm.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Khảo sát cân nặng (kg) của 50 học sinh thu được bảng ghép nhóm: $[40; 45)$ có 10 em, $[45; '
                 '50)$ có 20 em, $[50; 55)$ có 15 em, $[55; 60)$ có 5 em.',
            'statements': ['Một học sinh nặng đúng $45$ kg được xếp vào nhóm $[45; 50)$.',
                           'Tần số tương đối của nhóm $[45; 50)$ là $40\\%$.',
                           'Giá trị đại diện của nhóm $[50; 55)$ là $52,5$ kg.',
                           'Tỉ lệ học sinh có cân nặng dưới $50$ kg là $50\\%$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì $\\dfrac{20}{50} \\cdot 100\\% = 40\\%$. c) Đúng vì $\\dfrac{50 '
                        '+ 55}{2} = 52,5$. d) Sai vì dưới $50$ kg có $10 + 20 = 30$ em, chiếm '
                        '$\\dfrac{30}{50} = 60\\%$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 24: Bảng tần số, tần số '
                 'tương đối ghép nhóm và biểu đồ**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Hiểu được ý nghĩa của việc ghép nhóm dữ '
                           'liệu và lập được bảng tần số, tần số tương đối ghép nhóm.',
                           'Trong **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ**, quy '
                           'tắc/công thức **Quy ước nhóm $[a; b)$** được viết là: $a \\le x < b$.',
                           'Nếu áp dụng sai dấu/phép tính thành $a \\ge x < b$ thì kết quả của **Quy ước '
                           'nhóm $[a; b)$** trong **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu '
                           'đồ** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho nhóm chiều cao $[155; 160)$ (cm). Hỏi học sinh cao $160$ '
                           'cm có thuộc nhóm này không? Tìm giá trị đại diện của nhóm.”, kết quả giải đúng '
                           'là: Nhóm $[155; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ '
                           'cm không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 24: Bảng tần số, tần số tương đối ghép '
                        'nhóm và biểu đồ. b) **Đúng** theo công thức **Quy ước nhóm $[a; b)$** ($a \\le x < '
                        'b$). c) **Sai** vì công thức đúng của **Quy ước nhóm $[a; b)$** phải là $a \\le x < '
                        'b$ chứ không phải $a \\ge x < b$. d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu '
                 'đồ** để giải bài toán sau: Cho nhóm chiều cao $[155; 160)$ (cm). Hỏi học sinh cao $160$ cm '
                 'có thuộc nhóm này không? Tìm giá trị đại diện của nhóm. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Nhóm $[155; 160)$ gồm các giá trị $155 \\ge x < 160$, nên học sinh cao $160$ cm '
                        'không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$). Giá trị đạ...',
                        'Nhóm $[155; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ cm '
                        'không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$). Giá trị đạ...',
                        'Nhóm $[155; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ cm '
                        'không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 164)$). Giá trị đạ...',
                        'Nhóm $[157; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ cm '
                        'không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$). Giá trị đạ...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 24: Bảng tần số, tần số tương đối ghép nhóm và biểu đồ: '
                        'Nhóm $[155; 160)$ gồm các giá trị $155 \\le x < 160$, nên học sinh cao $160$ cm '
                        'không thuộc nhóm này (mà thuộc nhóm tiếp theo $[160; 165)$).\n'
                        'Giá trị đại diện của nhóm là $\\dfrac{155 + 160}{2} = 157,5$ (cm).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho dãy số liệu: $12; 15; 18; 20; 14; 19; 22; 16; 11; 25$. Khi ghép dãy số liệu này vào '
                 'các nhóm $[10; 15), [15; 20), [20; 25), [25; 30)$ thì tần số của nhóm $[15; 20)$ bằng bao '
                 'nhiêu?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Các giá trị thỏa mãn $15 \\le x < 20$ trong dãy là: $15; 18; 19; 16$ (có $4$ giá '
                        'trị).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch08-xac-suat',
  'context_title': 'Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản',
  'context': 'Chương VIII · SGK Toán 9: Xác suất của biến cố trong một số mô hình xác suất đơn giản.',
  'title': 'Bài 25: Phép thử ngẫu nhiên và không gian mẫu',
  'icon': '🎲',
  'description': 'Nhận biết phép thử ngẫu nhiên, xác định không gian mẫu và các kết quả thuận lợi cho một '
                 'biến cố.',
  'requirements': ['Nhận biết được phép thử ngẫu nhiên và xác định được không gian mẫu $\\Omega$.',
                   'Liệt kê và đếm được số kết quả thuận lợi cho một biến cố liên quan tới phép thử.',
                   'Vận dụng kiến thức của **Bài 25: Phép thử ngẫu nhiên và không gian mẫu** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Phép thử ngẫu nhiên (gọi tắt là phép thử) là một hoạt động mà ta không thể biết trước được '
                'kết quả của nó, nhưng biết tất cả các kết quả có thể xảy ra. Tập hợp tất cả các kết quả có '
                'thể xảy ra của phép thử gọi là không gian mẫu, kí hiệu là $\\Omega$.',
  'theory': '1. Mỗi kết quả có thể xảy ra của phép thử là một phần tử của không gian mẫu $\\Omega$.\n'
            '2. Một kết quả có thể của phép thử làm cho biến cố $E$ xảy ra được gọi là kết quả thuận lợi cho '
            'biến cố $E$.',
  'formulas': [{'category': 'Không gian mẫu của một số phép thử thông dụng',
                'items': [{'name': 'Gieo 1 đồng xu 2 lần',
                           'formula': '$\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$',
                           'note': 'Số phần tử $n(\\Omega) = 4$'},
                          {'name': 'Gieo 2 con xúc xắc',
                           'formula': '$\\Omega = \\{(i; j) \\mid 1 \\le i, j \\le 6\\}$',
                           'note': 'Số phần tử $n(\\Omega) = 6 \\cdot 6 = 36$'}]}],
  'example': 'Gieo một đồng xu cân đối hai lần liên tiếp. Viết không gian mẫu $\\Omega$ và liệt kê các kết '
             "quả thuận lợi cho biến cố $A$: 'Có đúng một lần xuất hiện mặt sấp (S)'.",
  'example_answer': 'Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, '
                    '\\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $4$ phần tử.\n'
                    'Các kết quả thuận lợi cho biến cố $A$ là: $\\text{SN}$ và $\\text{NS}$ (có $2$ kết quả '
                    'thuận lợi).',
  'real_life': 'Xác định tất cả các kịch bản kết quả có thể xảy ra khi bốc thăm chia bảng thi đấu thể thao.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Gieo một con xúc xắc cân đối và đồng chất 1 lần. Số phần tử của không gian mẫu $\\Omega$ '
                 'là:',
            'options': ['$6$', '$12$', '$36$', '$2$'],
            'answer': 0,
            'solution': 'Không gian mẫu $\\Omega = \\{1; 2; 3; 4; 5; 6\\}$ có $6$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tung một đồng xu cân đối hai lần liên tiếp. Không gian mẫu $\\Omega$ có bao nhiêu phần tử?',
            'options': ['$2$', '$4$', '$6$', '$8$'],
            'answer': 1,
            'solution': 'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$4$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Phép thử ngẫu nhiên và không gian mẫu**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Gieo 1 đồng xu 2 lần**?',
            'options': ['$\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, '
                        '\\text{NN}\\}$',
                        '$\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 25: Phép thử ngẫu nhiên và không gian mẫu, **Gieo '
                        '1 đồng xu 2 lần** được xác định bởi: $\\Omega = \\{\\text{SS}, \\text{SN}, '
                        '\\text{NS}, \\text{NN}\\}$. (Số phần tử $n(\\Omega) = 4$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Phép thử ngẫu nhiên và không gian mẫu**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Gieo 2 con xúc xắc**?',
            'options': ['$\\Omega = \\{(i; j) \\mid 1 \\ge i, j \\le 6\\}$',
                        '$\\Omega = \\{(i; j) \\mid 1 \\le i, j \\le 5\\}$',
                        '$\\Omega = \\{(i; j) \\mid 2 \\le i, j \\le 6\\}$',
                        '$\\Omega = \\{(i; j) \\mid 1 \\le i, j \\le 6\\}$'],
            'answer': 3,
            'solution': 'Trong Bài 25: Phép thử ngẫu nhiên và không gian mẫu, **Gieo 2 con xúc xắc** có công '
                        'thức/quy tắc là: $\\Omega = \\{(i; j) \\mid 1 \\le i, j \\le 6\\}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hộp có 4 quả bóng đánh số $1, 2, 3, 4$. Lấy ngẫu nhiên đồng thời 2 quả bóng từ hộp. Số '
                 'phần tử của không gian mẫu là:',
            'options': ['$6$', '$8$', '$12$', '$16$'],
            'answer': 0,
            'solution': 'Các cặp bóng có thể lấy ra là: $\\{1; 2\\}, \\{1; 3\\}, \\{1; 4\\}, \\{2; 3\\}, '
                        '\\{2; 4\\}, \\{3; 4\\}$, gồm $6$ phần tử.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 25: Phép thử ngẫu nhiên và không gian mẫu**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết được phép thử ngẫu nhiên và xác định được không gian mẫu $\\Omega$. (với '
                        'dấu ngược lại)',
                        'Nhận biết được phép thử ngẫu nhiên và xác định được không gian mẫu $\\Omega$.',
                        'Đảo ngược vế của quy tắc: Nhận biết được phép thử ngẫu nhiên và xác định được không '
                        'gian mẫu $\\Omega$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được phép thử ngẫu '
                        'nhiên và xác định được không gian mẫu $\\Omega$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 25: Phép thử ngẫu nhiên và không gian mẫu: Nhận biết '
                        'được phép thử ngẫu nhiên và xác định được không gian mẫu $\\Omega$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Gieo đồng thời hai con xúc xắc cân đối và đồng chất (con thứ nhất màu đỏ, con thứ hai màu '
                 'xanh).',
            'statements': ['Số phần tử của không gian mẫu là $36$.',
                           "Biến cố $A$: 'Số chấm trên hai con xúc xắc bằng nhau' có $6$ kết quả thuận lợi.",
                           "Biến cố $B$: 'Tổng số chấm trên hai con xúc xắc bằng $12$' có $2$ kết quả thuận "
                           'lợi.',
                           "Biến cố $C$: 'Tổng số chấm trên hai con xúc xắc bằng $4$' có $3$ kết quả thuận "
                           'lợi.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $6 \\cdot 6 = 36$. b) Đúng: $(1;1), (2;2), (3;3), (4;4), (5;5), (6;6)$. '
                        'c) Sai vì chỉ có $1$ kết quả $(6;6)$. d) Đúng: $(1;3), (2;2), (3;1)$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 25: Phép thử ngẫu nhiên và '
                 'không gian mẫu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được phép thử ngẫu nhiên và '
                           'xác định được không gian mẫu $\\Omega$.',
                           'Trong **Bài 25: Phép thử ngẫu nhiên và không gian mẫu**, quy tắc/công thức '
                           '**Gieo 1 đồng xu 2 lần** được viết là: $\\Omega = \\{\\text{SS}, \\text{SN}, '
                           '\\text{NS}, \\text{NN}\\}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\Omega = \\{\\text{SS}, \\text{SN}, '
                           '\\text{NS}, \\text{NN}\\}$ (với dấu ngược lại) thì kết quả của **Gieo 1 đồng xu '
                           '2 lần** trong **Bài 25: Phép thử ngẫu nhiên và không gian mẫu** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Gieo một đồng xu cân đối hai lần liên tiếp. Viết không gian '
                           "mẫu $\\Omega$ và liệt kê các kết quả thuận lợi cho biến cố $A$: 'Có đúng "
                           'một...”, kết quả giải đúng là: Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian '
                           'mẫu là $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $4$ '
                           'phần tử. Các k...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 25: Phép thử ngẫu nhiên và không gian mẫu. '
                        'b) **Đúng** theo công thức **Gieo 1 đồng xu 2 lần** ($\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$). c) **Sai** vì công thức đúng của **Gieo 1 '
                        'đồng xu 2 lần** phải là $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, '
                        '\\text{NN}\\}$ chứ không phải $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, '
                        '\\text{NN}\\}$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ minh họa trong '
                        'bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 25: Phép thử ngẫu nhiên và không gian mẫu** để giải '
                 'bài toán sau: Gieo một đồng xu cân đối hai lần liên tiếp. Viết không gian mẫu $\\Omega$ và '
                 "liệt kê các kết quả thuận lợi cho biến cố $A$: 'Có đúng một lần xuất hiện mặt sấp (S)'. "
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $5$ phần tử. Các kết quả thuận lợ...',
                        'Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $3$ phần tử. Các kết quả thuận lợ...',
                        'Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $4$ phần tử. Các kết quả thuận lợ...',
                        'Kí hiệu S là mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, '
                        '\\text{SN}, \\text{NS}, \\text{NN}\\}$ gồm $8$ phần tử. Các kết quả thuận lợ...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 25: Phép thử ngẫu nhiên và không gian mẫu: Kí hiệu S là '
                        'mặt sấp, N là mặt ngửa. Không gian mẫu là $\\Omega = \\{\\text{SS}, \\text{SN}, '
                        '\\text{NS}, \\text{NN}\\}$ gồm $4$ phần tử.\n'
                        'Các kết quả thuận lợi cho biến cố $A$ là: $\\text{SN}$ và $\\text{NS}$ (có $2$ kết '
                        'quả thuận lợi).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Từ các chữ số $1, 2, 3$, lập ngẫu nhiên một số tự nhiên có hai chữ số khác nhau. Hỏi không '
                 'gian mẫu của phép thử này có bao nhiêu phần tử?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Không gian mẫu là $\\Omega = \\{12; 13; 21; 23; 31; 32\\}$, có $6$ phần tử.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch08-xac-suat',
  'context_title': 'Chương VIII: Xác suất của biến cố trong một số mô hình xác suất đơn giản',
  'context': 'Chương VIII · SGK Toán 9: Xác suất của biến cố trong một số mô hình xác suất đơn giản.',
  'title': 'Bài 26: Xác suất của biến cố liên quan tới phép thử',
  'icon': '🎯',
  'description': 'Tính xác suất của biến cố trong phép thử có các kết quả đồng khả năng.',
  'requirements': ['Nhận biết được tính đồng khả năng của các kết quả trong phép thử ngẫu nhiên.',
                   'Tính được xác suất của biến cố $E$ theo công thức $P(E) = \\dfrac{n(E)}{n(\\Omega)}$.',
                   'Vận dụng kiến thức của **Bài 26: Xác suất của biến cố liên quan tới phép thử** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Giả sử rằng các kết quả có thể của một phép thử là đồng khả năng. Khi đó, xác suất của biến '
                'cố $E$, kí hiệu là $P(E)$, bằng tỉ số giữa số kết quả thuận lợi cho biến cố $E$ và tổng số '
                'phần tử của không gian mẫu $\\Omega$.',
  'theory': 'Các bước tính xác suất của biến cố $E$:\n'
            '- Bước 1: Mô tả không gian mẫu $\\Omega$ và tính số phần tử $n(\\Omega)$, kiểm tra tính đồng '
            'khả năng của các kết quả.\n'
            '- Bước 2: Xác định các kết quả thuận lợi cho biến cố $E$ và đếm số kết quả thuận lợi $n(E)$.\n'
            '- Bước 3: Tính xác suất $P(E) = \\dfrac{n(E)}{n(\\Omega)}$.',
  'formulas': [{'category': 'Công thức xác suất cổ điển',
                'items': [{'name': 'Xác suất của biến cố $E$',
                           'formula': '$P(E) = \\dfrac{n(E)}{n(\\Omega)}$',
                           'note': '$0 \\le P(E) \\le 1$'}]}],
  'example': "Gieo đồng thời hai đồng xu cân đối. Tính xác suất của biến cố $E$: 'Có ít nhất một đồng xu "
             "xuất hiện mặt ngửa (N)'.",
  'example_answer': 'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                    '$n(\\Omega) = 4$ kết quả đồng khả năng.\n'
                    'Các kết quả thuận lợi cho biến cố $E$ là $\\text{SN}, \\text{NS}, \\text{NN}$, nên '
                    '$n(E) = 3$.\n'
                    'Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{3}{4}$.',
  'real_life': 'Đánh giá cơ hội trúng thưởng trong các trò chơi quay số ngẫu nhiên hoặc kiểm tra chất lượng '
               'lô hàng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Giả sử phép thử có không gian mẫu $\\Omega$ gồm các kết quả đồng khả năng và $n(E)$ là số '
                 'kết quả thuận lợi cho biến cố $E$. Công thức tính xác suất của $E$ là:',
            'options': ['$P(E) = \\dfrac{n(\\Omega)}{n(E)}$',
                        '$P(E) = \\dfrac{n(E)}{n(\\Omega)}$',
                        '$P(E) = n(E) \\cdot n(\\Omega)$',
                        '$P(E) = 1 - n(E)$'],
            'answer': 1,
            'solution': 'Theo định nghĩa, $P(E) = \\dfrac{n(E)}{n(\\Omega)}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Chọn ngẫu nhiên một số trong tập hợp $\\{1; 2; 3; 4; 5; 6; 7; 8; 9; 10\\}$. Xác suất để '
                 'chọn được một số nguyên tố là:',
            'options': ['$\\dfrac{1}{2}$', '$\\dfrac{3}{10}$', '$\\dfrac{2}{5}$', '$\\dfrac{1}{5}$'],
            'answer': 2,
            'solution': 'Các số nguyên tố từ $1$ đến $10$ là $2, 3, 5, 7$ (có $4$ số). Vậy xác suất là '
                        '$\\dfrac{4}{10} = \\dfrac{2}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Xác suất của biến cố liên quan tới phép thử**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Xác suất của biến cố $E$**?',
            'options': ['$P(E) = \\dfrac{n(E)}{n(\\Omega)}$ (với dấu ngược lại)',
                        '$P(E) = \\dfrac{n(\\Omega)}{n(E)}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $P(E) = '
                        '\\dfrac{n(E)}{n(\\Omega)}$',
                        '$P(E) = \\dfrac{n(E)}{n(\\Omega)}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 26: Xác suất của biến cố liên quan tới phép thử, '
                        '**Xác suất của biến cố $E$** được xác định bởi: $P(E) = \\dfrac{n(E)}{n(\\Omega)}$. '
                        '($0 \\le P(E) \\le 1$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Theo định nghĩa trong **Bài 26: Xác suất của biến cố liên quan tới phép thử**, khẳng định '
                 'nào dưới đây là **đúng**?',
            'options': ['Giả sử rằng các kết quả có thể của một phép thử là đồng khả năng. Khi đó, xác suất '
                        'của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số...',
                        'Giả sử rằng các kết quả có thể của một phép thử là đồng khả năng. Khi đó, xác suất '
                        'của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số... (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Giả sử rằng các kết quả có thể của một phép thử là đồng '
                        'khả năng. Khi đó, xác suất của biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số...',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Giả sử rằng các kết quả có thể '
                        'của một phép thử là đồng khả năng. Khi đó, xác suất của biến cố $E$, kí hiệu là '
                        '$P(E)$, bằng tỉ số...'],
            'answer': 0,
            'solution': 'Theo định nghĩa của Bài 26: Xác suất của biến cố liên quan tới phép thử: Giả sử '
                        'rằng các kết quả có thể của một phép thử là đồng khả năng. Khi đó, xác suất của '
                        'biến cố $E$, kí hiệu là $P(E)$, bằng tỉ số...'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': "Gieo đồng thời hai con xúc xắc cân đối. Xác suất của biến cố 'Tổng số chấm xuất hiện trên "
                 "hai con xúc xắc bằng $7$' là:",
            'options': ['$\\dfrac{1}{12}$', '$\\dfrac{1}{6}$', '$\\dfrac{7}{36}$', '$\\dfrac{5}{36}$'],
            'answer': 1,
            'solution': 'Có $6$ kết quả thuận lợi: $(1;6), (2;5), (3;4), (4;3), (5;2), (6;1)$ trên tổng số '
                        '$36$ kết quả. Xác suất là $\\dfrac{6}{36} = \\dfrac{1}{6}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 26: Xác suất của biến cố liên quan tới phép thử**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được tính đồng khả năng của các kết quả trong phép thử ngẫu nhiên. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được tính đồng khả năng của các kết quả trong '
                        'phép thử ngẫu nhiên.',
                        'Nhận biết được tính đồng khả năng của các kết quả trong phép thử ngẫu nhiên.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được tính đồng khả '
                        'năng của các kết quả trong phép thử ngẫu nhiên.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 26: Xác suất của biến cố liên quan tới phép thử: Nhận '
                        'biết được tính đồng khả năng của các kết quả trong phép thử ngẫu nhiên.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Một túi chứa 3 viên bi đỏ ($Đ_1, Đ_2, Đ_3$) và 2 viên bi xanh ($X_1, X_2$) có cùng kích '
                 'thước. Lấy ngẫu nhiên đồng thời 2 viên bi từ túi.',
            'statements': ['Số phần tử của không gian mẫu là $10$.',
                           "Số kết quả thuận lợi cho biến cố $A$: 'Hai viên bi lấy ra cùng màu xanh' là $1$.",
                           "Xác suất của biến cố $B$: 'Hai viên bi lấy ra cùng màu đỏ' là $\\dfrac{3}{10}$.",
                           "Xác suất của biến cố $C$: 'Hai viên bi lấy ra khác màu' là $\\dfrac{2}{5}$."],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng (số cách chọn 2 trong 5 viên là $10$). b) Đúng: chỉ có $\\{X_1, X_2\\}$. c) '
                        'Đúng: có 3 cặp bi đỏ nên $P(B) = \\dfrac{3}{10}$. d) Sai vì có $3 \\cdot 2 = 6$ cặp '
                        'khác màu, xác suất là $\\dfrac{6}{10} = \\dfrac{3}{5}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 26: Xác suất của biến cố '
                 'liên quan tới phép thử**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được tính đồng khả năng của '
                           'các kết quả trong phép thử ngẫu nhiên.',
                           'Trong **Bài 26: Xác suất của biến cố liên quan tới phép thử**, quy tắc/công thức '
                           '**Xác suất của biến cố $E$** được viết là: $P(E) = \\dfrac{n(E)}{n(\\Omega)}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $P(E) = \\dfrac{n(E)}{n(\\Omega)}$ (với dấu '
                           'ngược lại) thì kết quả của **Xác suất của biến cố $E$** trong **Bài 26: Xác suất '
                           'của biến cố liên quan tới phép thử** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Gieo đồng thời hai đồng xu cân đối. Tính xác suất của biến '
                           "cố $E$: 'Có ít nhất một đồng xu xuất hiện mặt ngửa (N)'.”, kết quả giải đúng là: "
                           'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ '
                           'có $n(\\Omega) = 4$ kết quả đồng khả năng. Các kết quả thuận lợ...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 26: Xác suất của biến cố liên quan tới '
                        'phép thử. b) **Đúng** theo công thức **Xác suất của biến cố $E$** ($P(E) = '
                        '\\dfrac{n(E)}{n(\\Omega)}$). c) **Sai** vì công thức đúng của **Xác suất của biến '
                        'cố $E$** phải là $P(E) = \\dfrac{n(E)}{n(\\Omega)}$ chứ không phải $P(E) = '
                        '\\dfrac{n(E)}{n(\\Omega)}$ (với dấu ngược lại). d) **Đúng** theo lời giải ví dụ '
                        'minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 26: Xác suất của biến cố liên quan tới phép thử** '
                 'để giải bài toán sau: Gieo đồng thời hai đồng xu cân đối. Tính xác suất của biến cố $E$: '
                 "'Có ít nhất một đồng xu xuất hiện mặt ngửa (N)'. Cách giải và kết quả nào dưới đây là "
                 '**đúng**?',
            'options': ['Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$n(\\Omega) = 5$ kết quả đồng khả năng. Các kết quả thuận lợi cho biến cố $E$...',
                        'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$n(\\Omega) = 3$ kết quả đồng khả năng. Các kết quả thuận lợi cho biến cố $E$...',
                        'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$n(\\Omega) = 8$ kết quả đồng khả năng. Các kết quả thuận lợi cho biến cố $E$...',
                        'Không gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$n(\\Omega) = 4$ kết quả đồng khả năng. Các kết quả thuận lợi cho biến cố $E$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 26: Xác suất của biến cố liên quan tới phép thử: Không '
                        'gian mẫu $\\Omega = \\{\\text{SS}, \\text{SN}, \\text{NS}, \\text{NN}\\}$ có '
                        '$n(\\Omega) = 4$ kết quả đồng khả năng.\n'
                        'Các kết quả thuận lợi cho biến cố $E$ là $\\text{SN}, \\text{NS}, \\text{NN}$, nên '
                        '$n(E) = 3$.\n'
                        'Vậy xác suất của biến cố $E$ là $P(E) = \\dfrac{3}{4}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Gieo một đồng xu cân đối 2 lần liên tiếp. Tính xác suất để cả 2 lần đều xuất hiện mặt sấp '
                 '(viết kết quả dưới dạng số thập phân).',
            'answer': ['0,25', '0.25'],
            'unit': None,
            'solution': 'Không gian mẫu có $4$ phần tử, chỉ có $1$ kết quả thuận lợi là SS. Vậy xác suất là '
                        '$\\dfrac{1}{4} = 0,25$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch09-duong-tron-ngoai-noi-tiep',
  'context_title': 'Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp',
  'context': 'Chương IX · SGK Toán 9: Đường tròn ngoại tiếp và đường tròn nội tiếp.',
  'title': 'Bài 27: Góc nội tiếp',
  'icon': '📐',
  'description': 'Nhận biết góc nội tiếp và vận dụng mối liên hệ giữa số đo góc nội tiếp với số đo cung bị '
                 'chắn, góc ở tâm.',
  'requirements': ['Nhận biết được góc nội tiếp của một đường tròn.',
                   'Giải thích và vận dụng được định lí về số đo góc nội tiếp bằng nửa số đo cung bị chắn.',
                   'Vận dụng được các hệ quả của góc nội tiếp (khẳng định góc nội tiếp chắn nửa đường tròn '
                   'là góc vuông).'],
  'definition': 'Góc nội tiếp là góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây cung của đường '
                'tròn đó. Cung nằm bên trong góc được gọi là cung bị chắn.',
  'theory': '1. Định lí: Trong một đường tròn, số đo của góc nội tiếp bằng nửa số đo của cung bị chắn.\n'
            '2. Hệ quả:\n'
            '- Các góc nội tiếp bằng nhau chắn các cung bằng nhau.\n'
            '- Các góc nội tiếp cùng chắn một cung (hoặc chắn các cung bằng nhau) thì bằng nhau.\n'
            '- Góc nội tiếp (nhỏ hơn hoặc bằng $90^\\circ$) có số đo bằng nửa số đo của góc ở tâm cùng chắn '
            'một cung.\n'
            '- Góc nội tiếp chắn nửa đường tròn là góc vuông ($90^\\circ$).',
  'formulas': [{'category': 'Định lí và hệ quả góc nội tiếp',
                'items': [{'name': 'Số đo góc nội tiếp',
                           'formula': '$\\widehat{AMB} = \\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                                      '\\dfrac{1}{2}\\widehat{AOB}$',
                           'note': 'Bằng nửa số đo cung bị chắn (hoặc góc ở tâm cùng chắn một cung)'},
                          {'name': 'Góc nội tiếp chắn nửa đường tròn',
                           'formula': '$AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = '
                                      '90^\\circ$',
                           'note': 'Tính chất rất thường dùng trong chứng minh vuông góc'}]}],
  'example': 'Cho ba điểm $A, B, C$ thuộc đường tròn $(O)$ sao cho góc ở tâm $\\widehat{BOC} = 110^\\circ$ '
             '($A$ thuộc cung lớn $BC$). Tính số đo góc nội tiếp $\\widehat{BAC}$.',
  'example_answer': 'Góc nội tiếp $\\widehat{BAC}$ và góc ở tâm $\\widehat{BOC}$ cùng chắn cung nhỏ $BC$, do '
                    'đó:\n'
                    '$\\widehat{BAC} = \\dfrac{1}{2}\\widehat{BOC} = \\dfrac{110^\\circ}{2} = 55^\\circ$.',
  'real_life': 'Xác định vị trí đặt ghế khán đài hình cung tròn sao cho mọi khán giả đều có cùng một góc '
               'nhìn về phía sân khấu.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trong một đường tròn, số đo của góc nội tiếp bằng:',
            'options': ['Số đo của cung bị chắn',
                        'Hai lần số đo của cung bị chắn',
                        'Nửa số đo của cung bị chắn',
                        'Số đo của góc ở tâm cùng chắn một cung'],
            'answer': 2,
            'solution': 'Theo định lí góc nội tiếp, số đo góc nội tiếp bằng nửa số đo của cung bị chắn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Góc nội tiếp chắn nửa đường tròn có số đo bằng:',
            'options': ['$180^\\circ$', '$45^\\circ$', '$60^\\circ$', '$90^\\circ$'],
            'answer': 3,
            'solution': 'Góc nội tiếp chắn nửa đường tròn là góc vuông, có số đo bằng $90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Góc nội tiếp**, quy tắc hoặc công thức nào sau đây xác định đúng **Số đo '
                 'góc nội tiếp**?',
            'options': ['$\\widehat{AMB} = \\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                        '\\dfrac{1}{2}\\widehat{AOB}$',
                        '$\\widehat{AMB} = \\dfrac{2}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                        '\\dfrac{1}{2}\\widehat{AOB}$',
                        '$\\widehat{AMB} = \\dfrac{2}{1}\\text{sđ}\\overset{\\frown}{AB} = '
                        '\\dfrac{1}{2}\\widehat{AOB}$',
                        '$AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = 90^\\circ$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 27: Góc nội tiếp, **Số đo góc nội tiếp** được xác '
                        'định bởi: $\\widehat{AMB} = \\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                        '\\dfrac{1}{2}\\widehat{AOB}$. (Bằng nửa số đo cung bị chắn (hoặc góc ở tâm cùng '
                        'chắn một cung))'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Góc nội tiếp**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Góc '
                 'nội tiếp chắn nửa đường tròn**?',
            'options': ['$AB$ là đường kính, $M \\notin (O) \\Rightarrow \\widehat{AMB} = 90^\\circ$',
                        '$AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = 90^\\circ$',
                        '$AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = 89^\\circ$',
                        '$AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = 92^\\circ$'],
            'answer': 1,
            'solution': 'Trong Bài 27: Góc nội tiếp, **Góc nội tiếp chắn nửa đường tròn** có công thức/quy '
                        'tắc là: $AB$ là đường kính, $M \\in (O) \\Rightarrow \\widehat{AMB} = 90^\\circ$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho đường tròn $(O)$ và hai góc nội tiếp $\\widehat{MAN}, \\widehat{MBN}$ cùng chắn cung '
                 'nhỏ $MN$. Biết $\\widehat{MAN} = 40^\\circ$, tổng $\\widehat{MBN} + \\widehat{MON}$ bằng:',
            'options': ['$80^\\circ$', '$100^\\circ$', '$120^\\circ$', '$160^\\circ$'],
            'answer': 2,
            'solution': 'Ta có $\\widehat{MBN} = \\widehat{MAN} = 40^\\circ$ và $\\widehat{MON} = '
                        '2\\widehat{MAN} = 80^\\circ$. Tổng bằng $40^\\circ + 80^\\circ = 120^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 27: Góc nội tiếp**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được góc nội tiếp của một đường tròn. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được góc nội tiếp của một đường tròn.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được góc nội tiếp của '
                        'một đường tròn.',
                        'Nhận biết được góc nội tiếp của một đường tròn.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 27: Góc nội tiếp: Nhận biết được góc nội tiếp của một '
                        'đường tròn.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho đường tròn $(O)$ có đường kính $AB$ và điểm $C$ thuộc đường tròn ($C \\neq A, B$) sao '
                 'cho $\\widehat{CAB} = 30^\\circ$.',
            'statements': ['Góc $\\widehat{ACB}$ là góc nội tiếp chắn nửa đường tròn nên $\\widehat{ACB} = '
                           '90^\\circ$.',
                           'Số đo của cung nhỏ $BC$ bằng $60^\\circ$.',
                           'Góc ở tâm $\\widehat{BOC}$ có số đo bằng $30^\\circ$.',
                           'Tam giác $OBC$ là tam giác đều.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng. b) Đúng vì $\\text{sđ}\\overset{\\frown}{BC} = 2\\widehat{CAB} = '
                        '60^\\circ$. c) Sai vì $\\widehat{BOC} = \\text{sđ}\\overset{\\frown}{BC} = '
                        '60^\\circ$. d) Đúng vì $\\triangle OBC$ cân tại $O$ có $\\widehat{BOC} = '
                        '60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 27: Góc nội tiếp**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được góc nội tiếp của một '
                           'đường tròn.',
                           'Trong **Bài 27: Góc nội tiếp**, quy tắc/công thức **Số đo góc nội tiếp** được '
                           'viết là: $\\widehat{AMB} = \\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                           '\\dfrac{1}{2}\\widehat{AOB}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\widehat{AMB} = '
                           '\\dfrac{2}{2}\\text{sđ}\\overset{\\frown}{AB} = \\dfrac{1}{2}\\widehat{AOB}$ thì '
                           'kết quả của **Số đo góc nội tiếp** trong **Bài 27: Góc nội tiếp** vẫn không thay '
                           'đổi.',
                           'Xét ví dụ của bài: “Cho ba điểm $A, B, C$ thuộc đường tròn $(O)$ sao cho góc ở '
                           'tâm $\\widehat{BOC} = 110^\\circ$ ($A$ thuộc cung lớn $BC$). Tính số đo góc '
                           'nộ...”, kết quả giải đúng là: Góc nội tiếp $\\widehat{BAC}$ và góc ở tâm '
                           '$\\widehat{BOC}$ cùng chắn cung nhỏ $BC$, do đó: $\\widehat{BAC} = '
                           '\\dfrac{1}{2}\\widehat{BOC} = \\dfrac{110^\\circ}{2} = 55^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 27: Góc nội tiếp. b) **Đúng** theo công '
                        'thức **Số đo góc nội tiếp** ($\\widehat{AMB} = '
                        '\\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = \\dfrac{1}{2}\\widehat{AOB}$). c) '
                        '**Sai** vì công thức đúng của **Số đo góc nội tiếp** phải là $\\widehat{AMB} = '
                        '\\dfrac{1}{2}\\text{sđ}\\overset{\\frown}{AB} = \\dfrac{1}{2}\\widehat{AOB}$ chứ '
                        'không phải $\\widehat{AMB} = \\dfrac{2}{2}\\text{sđ}\\overset{\\frown}{AB} = '
                        '\\dfrac{1}{2}\\widehat{AOB}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài '
                        'học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 27: Góc nội tiếp** để giải bài toán sau: Cho ba '
                 'điểm $A, B, C$ thuộc đường tròn $(O)$ sao cho góc ở tâm $\\widehat{BOC} = 110^\\circ$ ($A$ '
                 'thuộc cung lớn $BC$). Tính số đo góc nội tiếp $\\widehat{BAC}$. Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Góc nội tiếp $\\widehat{BAC}$ và góc ở tâm $\\widehat{BOC}$ cùng chắn cung nhỏ '
                        '$BC$, do đó: $\\widehat{BAC} = \\dfrac{1}{2}\\widehat{BOC} = \\dfrac{110^\\circ}{2} '
                        '= 55^\\circ$...',
                        'Góc nội tiếp $\\widehat{BAC}$ và góc ở tâm $\\widehat{BOC}$ cùng chắn cung nhỏ '
                        '$BC$, do đó: $\\widehat{BAC} = \\dfrac{2}{2}\\widehat{BOC} = \\dfrac{110^\\circ}{2} '
                        '= 55^\\circ$...',
                        'Góc nội tiếp $\\widehat{BAC}$ và góc ở tâm $\\widehat{BOC}$ cùng chắn cung nhỏ '
                        '$BC$, do đó: $\\widehat{BAC} = \\dfrac{2}{1}\\widehat{BOC} = \\dfrac{110^\\circ}{2} '
                        '= 55^\\circ$...',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 27: Góc nội tiếp: Góc nội tiếp $\\widehat{BAC}$ và góc ở '
                        'tâm $\\widehat{BOC}$ cùng chắn cung nhỏ $BC$, do đó:\n'
                        '$\\widehat{BAC} = \\dfrac{1}{2}\\widehat{BOC} = \\dfrac{110^\\circ}{2} = '
                        '55^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cho tam giác $ABC$ có ba đỉnh nằm trên đường tròn $(O)$, biết $\\widehat{B} = 50^\\circ$ '
                 'và $\\widehat{C} = 65^\\circ$ ($O$ nằm trong tam giác $ABC$). Tính số đo góc ở tâm '
                 '$\\widehat{BOC}$ (đơn vị: độ).',
            'answer': ['130'],
            'unit': None,
            'solution': 'Trong $\\triangle ABC$: $\\widehat{BAC} = 180^\\circ - (50^\\circ + 65^\\circ) = '
                        '65^\\circ$. Góc ở tâm $\\widehat{BOC}$ cùng chắn cung $BC$ với góc nội tiếp '
                        '$\\widehat{BAC}$ nên $\\widehat{BOC} = 2 \\cdot 65^\\circ = 130^\\circ$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch09-duong-tron-ngoai-noi-tiep',
  'context_title': 'Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp',
  'context': 'Chương IX · SGK Toán 9: Đường tròn ngoại tiếp và đường tròn nội tiếp.',
  'title': 'Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác',
  'icon': '🔺',
  'description': 'Xác định tâm, bán kính đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác.',
  'requirements': ['Nhận biết và xác định được tâm, bán kính đường tròn ngoại tiếp tam giác (đặc biệt là tam '
                   'giác vuông, tam giác đều).',
                   'Nhận biết và xác định được tâm, bán kính đường tròn nội tiếp tam giác.',
                   'Vận dụng kiến thức của **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một '
                   'tam giác** để giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Đường tròn đi qua ba đỉnh của tam giác gọi là đường tròn ngoại tiếp tam giác. Đường tròn '
                'tiếp xúc với ba cạnh của tam giác gọi là đường tròn nội tiếp tam giác.',
  'theory': '1. Tâm đường tròn ngoại tiếp tam giác là giao điểm của ba đường trung trực của tam giác đó.\n'
            '- Tâm đường tròn ngoại tiếp tam giác vuông là trung điểm của cạnh huyền, bán kính $R = '
            '\\dfrac{\\text{cạnh huyền}}{2}$.\n'
            '- Đối với tam giác đều cạnh $a$, tâm đường tròn ngoại tiếp và nội tiếp trùng nhau tại trọng tâm '
            '$G$, với $R = \\dfrac{a\\sqrt{3}}{3}$ và $r = \\dfrac{a\\sqrt{3}}{6}$.\n'
            '2. Tâm đường tròn nội tiếp tam giác là giao điểm của ba đường phân giác trong của tam giác đó.',
  'formulas': [{'category': 'Bán kính đường tròn ngoại tiếp ($R$) và nội tiếp ($r$)',
                'items': [{'name': 'Tam giác vuông (cạnh huyền $a$)',
                           'formula': '$R = \\dfrac{a}{2}$',
                           'note': 'Tâm ngoại tiếp là trung điểm cạnh huyền'},
                          {'name': 'Tam giác đều cạnh $a$',
                           'formula': '$R = \\dfrac{a\\sqrt{3}}{3}$; $r = \\dfrac{a\\sqrt{3}}{6}$',
                           'note': 'Tâm ngoại tiếp và nội tiếp trùng với trọng tâm'}]}],
  'example': 'Tính bán kính đường tròn ngoại tiếp $R$ và bán kính đường tròn nội tiếp $r$ của tam giác đều '
             '$ABC$ có cạnh bằng $6$ cm.',
  'example_answer': 'Áp dụng công thức cho tam giác đều cạnh $a = 6$ cm:\n'
                    '$R = \\dfrac{6\\sqrt{3}}{3} = 2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = '
                    '\\sqrt{3}$ (cm).',
  'real_life': 'Xác định vị trí đặt trạm phát sóng cách đều ba khu dân cư (tâm đường tròn ngoại tiếp) hoặc '
               'cách đều ba tuyến đường lớn (tâm đường tròn nội tiếp).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tâm của đường tròn nội tiếp một tam giác là giao điểm của ba đường nào trong tam giác đó?',
            'options': ['Ba đường trung trực',
                        'Ba đường cao',
                        'Ba đường trung tuyến',
                        'Ba đường phân giác trong'],
            'answer': 3,
            'solution': 'Tâm đường tròn nội tiếp cách đều ba cạnh của tam giác nên là giao điểm của ba đường '
                        'phân giác trong.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Tâm của đường tròn ngoại tiếp tam giác vuông là:',
            'options': ['Trung điểm của cạnh huyền',
                        'Đỉnh góc vuông',
                        'Trọng tâm của tam giác',
                        'Trung điểm của cạnh góc vuông lớn'],
            'answer': 0,
            'solution': 'Tâm đường tròn ngoại tiếp tam giác vuông là trung điểm của cạnh huyền.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác**, quy tắc '
                 'hoặc công thức nào sau đây xác định đúng **Tam giác vuông (cạnh huyền $a$)**?',
            'options': ['$R = \\dfrac{a}{3}$',
                        '$R = \\dfrac{a}{2}$',
                        '$R = \\dfrac{2}{a}$',
                        '$R = \\dfrac{a}{4}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp '
                        'của một tam giác, **Tam giác vuông (cạnh huyền $a$)** được xác định bởi: $R = '
                        '\\dfrac{a}{2}$. (Tâm ngoại tiếp là trung điểm cạnh huyền)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác**, biểu '
                 'thức hoặc quy tắc nào dưới đây biểu diễn đúng **Tam giác đều cạnh $a$**?',
            'options': ['$R = \\dfrac{a\\sqrt{4}}{3}$; $r = \\dfrac{a\\sqrt{3}}{6}$',
                        '$R = \\dfrac{a\\sqrt{3}}{3}$; $r = \\dfrac{a\\sqrt{3}}{5}$',
                        '$R = \\dfrac{a\\sqrt{3}}{3}$; $r = \\dfrac{a\\sqrt{3}}{6}$',
                        '$R = \\dfrac{a\\sqrt{6}}{3}$; $r = \\dfrac{a\\sqrt{3}}{6}$'],
            'answer': 2,
            'solution': 'Trong Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác, **Tam '
                        'giác đều cạnh $a$** có công thức/quy tắc là: $R = \\dfrac{a\\sqrt{3}}{3}$; $r = '
                        '\\dfrac{a\\sqrt{3}}{6}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tam giác đều $ABC$ có cạnh bằng $2\\sqrt{3}$ cm. Bán kính đường tròn ngoại tiếp tam '
                 'giác $ABC$ bằng:',
            'options': ['$1$ cm', '$\\sqrt{3}$ cm', '$3$ cm', '$2$ cm'],
            'answer': 3,
            'solution': 'Áp dụng công thức $R = \\dfrac{a\\sqrt{3}}{3} = \\dfrac{2\\sqrt{3} \\cdot '
                        '\\sqrt{3}}{3} = 2$ (cm).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một '
                 'tam giác**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết và xác định được tâm, bán kính đường tròn ngoại tiếp tam giác (đặc biệt '
                        'là tam giác vuông, tam giác đều).',
                        'Nhận biết và xác định được tâm, bán kính đường tròn ngoại tiếp tam giác (đặc biệt '
                        'là tam giác vuông, tam giác đều). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và xác định được tâm, bán kính đường tròn ngoại '
                        'tiếp tam giác (đặc biệt là tam giác vuông, tam giác đều).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và xác định được tâm, '
                        'bán kính đường tròn ngoại tiếp tam giác (đặc biệt là tam giác vuông, tam giác '
                        'đều).'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của '
                        'một tam giác: Nhận biết và xác định được tâm, bán kính đường tròn ngoại tiếp tam '
                        'giác (đặc biệt là tam giác vuông, tam giác đều).'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác $ABC$ vuông tại $A$ có $AB = 6$ cm, $AC = 8$ cm.',
            'statements': ['Độ dài cạnh huyền $BC$ bằng $10$ cm.',
                           'Bán kính đường tròn ngoại tiếp tam giác $ABC$ là $R = 5$ cm.',
                           'Tâm đường tròn ngoại tiếp tam giác $ABC$ nằm bên trong tam giác $ABC$.',
                           'Trong tam giác đều, bán kính đường tròn ngoại tiếp gấp đôi bán kính đường tròn '
                           'nội tiếp ($R = 2r$).'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $BC = \\sqrt{6^2 + 8^2} = 10$ cm. b) Đúng vì $R = \\dfrac{BC}{2} = 5$ '
                        'cm. c) Sai vì tâm nằm tại trung điểm cạnh huyền $BC$. d) Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 28: Đường tròn ngoại tiếp '
                 'và đường tròn nội tiếp của một tam giác**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết và xác định được tâm, bán kính '
                           'đường tròn ngoại tiếp tam giác (đặc biệt là tam giác vuông, tam giác đều).',
                           'Trong **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một tam giác**, '
                           'quy tắc/công thức **Tam giác vuông (cạnh huyền $a$)** được viết là: $R = '
                           '\\dfrac{a}{2}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $R = \\dfrac{a}{3}$ thì kết quả của **Tam '
                           'giác vuông (cạnh huyền $a$)** trong **Bài 28: Đường tròn ngoại tiếp và đường '
                           'tròn nội tiếp của một tam giác** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Tính bán kính đường tròn ngoại tiếp $R$ và bán kính đường '
                           'tròn nội tiếp $r$ của tam giác đều $ABC$ có cạnh bằng $6$ cm.”, kết quả giải '
                           'đúng là: Áp dụng công thức cho tam giác đều cạnh $a = 6$ cm: $R = '
                           '\\dfrac{6\\sqrt{3}}{3} = 2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = '
                           '\\sqrt{3}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 28: Đường tròn ngoại tiếp và đường tròn '
                        'nội tiếp của một tam giác. b) **Đúng** theo công thức **Tam giác vuông (cạnh huyền '
                        '$a$)** ($R = \\dfrac{a}{2}$). c) **Sai** vì công thức đúng của **Tam giác vuông '
                        '(cạnh huyền $a$)** phải là $R = \\dfrac{a}{2}$ chứ không phải $R = \\dfrac{a}{3}$. '
                        'd) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp '
                 'của một tam giác** để giải bài toán sau: Tính bán kính đường tròn ngoại tiếp $R$ và bán '
                 'kính đường tròn nội tiếp $r$ của tam giác đều $ABC$ có cạnh bằng $6$ cm. Cách giải và kết '
                 'quả nào dưới đây là **đúng**?',
            'options': ['Áp dụng công thức cho tam giác đều cạnh $a = 7$ cm: $R = \\dfrac{6\\sqrt{3}}{3} = '
                        '2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = \\sqrt{3}$ (cm).',
                        'Áp dụng công thức cho tam giác đều cạnh $a = 6$ cm: $R = \\dfrac{6\\sqrt{3}}{3} = '
                        '2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = \\sqrt{3}$ (cm).',
                        'Áp dụng công thức cho tam giác đều cạnh $a = 6$ cm: $R = \\dfrac{6\\sqrt{3}}{3} = '
                        '2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = \\sqrt{2}$ (cm).',
                        'Áp dụng công thức cho tam giác đều cạnh $a = 12$ cm: $R = \\dfrac{6\\sqrt{3}}{3} = '
                        '2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = \\sqrt{3}$ (cm).'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 28: Đường tròn ngoại tiếp và đường tròn nội tiếp của một '
                        'tam giác: Áp dụng công thức cho tam giác đều cạnh $a = 6$ cm:\n'
                        '$R = \\dfrac{6\\sqrt{3}}{3} = 2\\sqrt{3}$ (cm) và $r = \\dfrac{6\\sqrt{3}}{6} = '
                        '\\sqrt{3}$ (cm).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một tam giác đều có bán kính đường tròn nội tiếp bằng $3$ cm. Tính bán kính đường tròn '
                 'ngoại tiếp của tam giác đều đó (đơn vị: cm).',
            'answer': ['6'],
            'unit': None,
            'solution': 'Trong tam giác đều, trọng tâm chia đường cao theo tỉ lệ $2 : 1$ nên $R = 2r = 2 '
                        '\\cdot 3 = 6$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch09-duong-tron-ngoai-noi-tiep',
  'context_title': 'Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp',
  'context': 'Chương IX · SGK Toán 9: Đường tròn ngoại tiếp và đường tròn nội tiếp.',
  'title': 'Bài 29: Tứ giác nội tiếp',
  'icon': '💠',
  'description': 'Nhận biết tứ giác nội tiếp, tính chất tổng hai góc đối và tâm, bán kính đường tròn ngoại '
                 'tiếp hình chữ nhật, hình vuông.',
  'requirements': ['Nhận biết được tứ giác nội tiếp đường tròn và vận dụng tính chất tổng hai góc đối bằng '
                   '$180^\\circ$.',
                   'Xác định được tâm và bán kính đường tròn ngoại tiếp hình chữ nhật, hình vuông.',
                   'Vận dụng kiến thức của **Bài 29: Tứ giác nội tiếp** để giải bài tập minh họa và bài toán '
                   'thực tiễn.'],
  'definition': 'Một tứ giác có bốn đỉnh nằm trên một đường tròn được gọi là tứ giác nội tiếp đường tròn '
                '(hoặc tứ giác nội tiếp), và đường tròn đó được gọi là đường tròn ngoại tiếp tứ giác.',
  'theory': '1. Định lí: Trong một tứ giác nội tiếp, tổng số đo hai góc đối diện bằng $180^\\circ$.\n'
            '2. Hình chữ nhật và hình vuông luôn là các tứ giác nội tiếp. Tâm đường tròn ngoại tiếp của '
            'chúng là giao điểm của hai đường chéo, bán kính bằng một nửa độ dài đường chéo.',
  'formulas': [{'category': 'Tính chất tứ giác nội tiếp',
                'items': [{'name': 'Tổng hai góc đối',
                           'formula': '$\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + '
                                      '\\widehat{D} = 180^\\circ$',
                           'note': 'Áp dụng cho tứ giác $ABCD$ nội tiếp'},
                          {'name': 'Hình chữ nhật ($a, b$) và hình vuông ($a$)',
                           'formula': '$R_{\\text{HCN}} = \\dfrac{\\sqrt{a^2 + b^2}}{2}$; $R_{\\text{HV}} = '
                                      '\\dfrac{a\\sqrt{2}}{2}$',
                           'note': 'Tâm là giao điểm hai đường chéo'}]}],
  'example': 'Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$, biết $\\widehat{A} = 70^\\circ$ và $\\widehat{B} '
             '= 105^\\circ$. Tính số đo các góc $C$ và $D$.',
  'example_answer': 'Vì tứ giác $ABCD$ nội tiếp nên tổng hai góc đối bằng $180^\\circ$:\n'
                    '$\\widehat{C} = 180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$;\n'
                    '$\\widehat{D} = 180^\\circ - \\widehat{B} = 180^\\circ - 105^\\circ = 75^\\circ$.',
  'real_life': 'Cắt một tấm gỗ mặt bàn hình chữ nhật hoặc hình vuông từ một khúc gỗ tròn sao cho tận dụng '
               'tối đa đường kính khúc gỗ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$. Khẳng định nào sau đây là đúng?',
            'options': ['$\\widehat{A} + \\widehat{C} = 180^\\circ$',
                        '$\\widehat{A} + \\widehat{B} = 180^\\circ$',
                        '$\\widehat{A} = \\widehat{C}$',
                        '$\\widehat{B} + \\widehat{D} = 90^\\circ$'],
            'answer': 0,
            'solution': 'Trong một tứ giác nội tiếp, tổng hai góc đối diện bằng $180^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Hình nào sau đây luôn nội tiếp được trong một đường tròn?',
            'options': ['Hình bình hành',
                        'Hình chữ nhật',
                        'Hình thoi (không phải hình vuông)',
                        'Hình thang thường'],
            'answer': 1,
            'solution': 'Hình chữ nhật có bốn góc vuông (tổng hai góc đối bằng $180^\\circ$) nên luôn nội '
                        'tiếp đường tròn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Tứ giác nội tiếp**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Tổng hai góc đối**?',
            'options': ['$\\widehat{A} - \\widehat{C} = 180^\\circ$ và $\\widehat{B} + \\widehat{D} = '
                        '180^\\circ$',
                        '$\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + \\widehat{D} = '
                        '179^\\circ$',
                        '$\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + \\widehat{D} = '
                        '180^\\circ$',
                        '$\\widehat{A} + \\widehat{C} = 182^\\circ$ và $\\widehat{B} + \\widehat{D} = '
                        '180^\\circ$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 29: Tứ giác nội tiếp, **Tổng hai góc đối** được '
                        'xác định bởi: $\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + '
                        '\\widehat{D} = 180^\\circ$. (Áp dụng cho tứ giác $ABCD$ nội tiếp)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Tứ giác nội tiếp**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Hình chữ nhật ($a, b$) và hình vuông ($a$)**?',
            'options': ['$R_{\\text{HCN}} = \\dfrac{\\sqrt{a^2 - b^2}}{2}$; $R_{\\text{HV}} = '
                        '\\dfrac{a\\sqrt{2}}{2}$',
                        '$R_{\\text{HCN}} = \\dfrac{\\sqrt{a^2 + b^2}}{2}$; $R_{\\text{HV}} = '
                        '\\dfrac{a\\sqrt{2}}{1}$',
                        '$R_{\\text{HCN}} = \\dfrac{\\sqrt{a^4 + b^2}}{2}$; $R_{\\text{HV}} = '
                        '\\dfrac{a\\sqrt{2}}{2}$',
                        '$R_{\\text{HCN}} = \\dfrac{\\sqrt{a^2 + b^2}}{2}$; $R_{\\text{HV}} = '
                        '\\dfrac{a\\sqrt{2}}{2}$'],
            'answer': 3,
            'solution': 'Trong Bài 29: Tứ giác nội tiếp, **Hình chữ nhật ($a, b$) và hình vuông ($a$)** có '
                        'công thức/quy tắc là: $R_{\\text{HCN}} = \\dfrac{\\sqrt{a^2 + b^2}}{2}$; '
                        '$R_{\\text{HV}} = \\dfrac{a\\sqrt{2}}{2}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho tứ giác $MNPQ$ nội tiếp đường tròn $(O)$ có $\\widehat{M} = 2\\widehat{P}$. Số đo góc '
                 '$P$ bằng:',
            'options': ['$60^\\circ$', '$120^\\circ$', '$90^\\circ$', '$45^\\circ$'],
            'answer': 0,
            'solution': 'Vì $\\widehat{M} + \\widehat{P} = 180^\\circ$ và $\\widehat{M} = 2\\widehat{P}$ nên '
                        '$3\\widehat{P} = 180^\\circ \\Rightarrow \\widehat{P} = 60^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 29: Tứ giác nội tiếp**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết được tứ giác nội tiếp đường tròn và vận dụng tính chất tổng hai góc đối '
                        'bằng $190^\\circ$.',
                        'Nhận biết được tứ giác nội tiếp đường tròn và vận dụng tính chất tổng hai góc đối '
                        'bằng $180^\\circ$.',
                        'Nhận biết được tứ giác nội tiếp đường tròn và vận dụng tính chất tổng hai góc đối '
                        'bằng $179^\\circ$.',
                        'Nhận biết được tứ giác nội tiếp đường tròn và vận dụng tính chất tổng hai góc đối '
                        'bằng $182^\\circ$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 29: Tứ giác nội tiếp: Nhận biết được tứ giác nội tiếp '
                        'đường tròn và vận dụng tính chất tổng hai góc đối bằng $180^\\circ$.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác nhọn $ABC$ có hai đường cao $BD$ và $CE$ cắt nhau tại $H$ ($D \\in AC, E \\in '
                 'AB$).',
            'statements': ['Tứ giác $ADHE$ có $\\widehat{ADH} + \\widehat{AEH} = 90^\\circ + 90^\\circ = '
                           '180^\\circ$.',
                           'Bốn điểm $A, D, H, E$ cùng nằm trên đường tròn đường kính $AH$.',
                           'Bốn điểm $B, C, D, E$ cùng nằm trên đường tròn đường kính $BC$.',
                           'Nếu $\\widehat{BAC} = 60^\\circ$ thì góc $\\widehat{DHE} = 60^\\circ$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng. b) Đúng vì hai tam giác vuông $ADH, AEH$ có chung cạnh huyền $AH$. c) Đúng '
                        'vì $\\widehat{BDC} = \\widehat{BEC} = 90^\\circ$. d) Sai vì $\\widehat{DHE} = '
                        '180^\\circ - \\widehat{DAE} = 120^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 29: Tứ giác nội tiếp**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được tứ giác nội tiếp đường '
                           'tròn và vận dụng tính chất tổng hai góc đối bằng $180^\\circ$.',
                           'Trong **Bài 29: Tứ giác nội tiếp**, quy tắc/công thức **Tổng hai góc đối** được '
                           'viết là: $\\widehat{A} + \\widehat{C} = 180^\\circ$ và $\\widehat{B} + '
                           '\\widehat{D} = 180^\\circ$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\widehat{A} - \\widehat{C} = 180^\\circ$ '
                           'và $\\widehat{B} + \\widehat{D} = 180^\\circ$ thì kết quả của **Tổng hai góc '
                           'đối** trong **Bài 29: Tứ giác nội tiếp** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$, biết '
                           '$\\widehat{A} = 70^\\circ$ và $\\widehat{B} = 105^\\circ$. Tính số đo các góc '
                           '$C$ và $D$...”, kết quả giải đúng là: Vì tứ giác $ABCD$ nội tiếp nên tổng hai '
                           'góc đối bằng $180^\\circ$: $\\widehat{C} = 180^\\circ - \\widehat{A} = '
                           '180^\\circ - 70^\\circ = 110^\\circ$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 29: Tứ giác nội tiếp. b) **Đúng** theo '
                        'công thức **Tổng hai góc đối** ($\\widehat{A} + \\widehat{C} = 180^\\circ$ và '
                        '$\\widehat{B} + \\widehat{D} = 180^\\circ$). c) **Sai** vì công thức đúng của '
                        '**Tổng hai góc đối** phải là $\\widehat{A} + \\widehat{C} = 180^\\circ$ và '
                        '$\\widehat{B} + \\widehat{D} = 180^\\circ$ chứ không phải $\\widehat{A} - '
                        '\\widehat{C} = 180^\\circ$ và $\\widehat{B} + \\widehat{D} = 180^\\circ$. d) '
                        '**Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 29: Tứ giác nội tiếp** để giải bài toán sau: Cho tứ '
                 'giác $ABCD$ nội tiếp đường tròn $(O)$, biết $\\widehat{A} = 70^\\circ$ và $\\widehat{B} = '
                 '105^\\circ$. Tính số đo các góc $C$ và $D$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì tứ giác $ABCD$ nội tiếp nên tổng hai góc đối bằng $180^\\circ$: $\\widehat{C} = '
                        '180^\\circ + \\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$...',
                        'Vì tứ giác $ABCD$ nội tiếp nên tổng hai góc đối bằng $180^\\circ$: $\\widehat{C} = '
                        '180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ = 109^\\circ$...',
                        'Vì tứ giác $ABCD$ nội tiếp nên tổng hai góc đối bằng $180^\\circ$: $\\widehat{C} = '
                        '180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$...',
                        'Vì tứ giác $ABCD$ nội tiếp nên tổng hai góc đối bằng $182^\\circ$: $\\widehat{C} = '
                        '180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$...'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Tứ giác nội tiếp: Vì tứ giác $ABCD$ nội tiếp nên '
                        'tổng hai góc đối bằng $180^\\circ$:\n'
                        '$\\widehat{C} = 180^\\circ - \\widehat{A} = 180^\\circ - 70^\\circ = 110^\\circ$;\n'
                        '$\\widehat{D} = 180^\\circ - \\widehat{B} = 180^\\circ - 105^\\circ = 75^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình chữ nhật có chiều rộng $9$ cm và chiều dài $12$ cm. Tính bán kính đường tròn '
                 'ngoại tiếp hình chữ nhật đó (đơn vị: cm).',
            'answer': ['7,5', '7.5'],
            'unit': None,
            'solution': 'Độ dài đường chéo hình chữ nhật là $d = \\sqrt{9^2 + 12^2} = 15$ (cm). Bán kính '
                        'đường tròn ngoại tiếp là $R = \\dfrac{15}{2} = 7,5$ (cm).',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch09-duong-tron-ngoai-noi-tiep',
  'context_title': 'Chương IX: Đường tròn ngoại tiếp và đường tròn nội tiếp',
  'context': 'Chương IX · SGK Toán 9: Đường tròn ngoại tiếp và đường tròn nội tiếp.',
  'title': 'Bài 30: Đa giác đều',
  'icon': '🛑',
  'description': 'Nhận biết đa giác đều, tính số đo góc của đa giác đều và phép quay giữ nguyên đa giác đều.',
  'requirements': ['Nhận biết được đa giác đều và tính được số đo mỗi góc của $n$-giác đều.',
                   'Nhận biết được phép quay và xác định được các phép quay giữ nguyên một đa giác đều.',
                   'Vận dụng kiến thức của **Bài 30: Đa giác đều** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': 'Đa giác đều là đa giác lồi có tất cả các cạnh bằng nhau và tất cả các góc bằng nhau (ví dụ: '
                'tam giác đều, hình vuông, ngũ giác đều, lục giác đều).',
  'theory': '1. Tổng các góc của một đa giác lồi $n$ cạnh là $(n - 2) \\cdot 180^\\circ$. Do đó mỗi góc của '
            '$n$-giác đều có số đo bằng $\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$.\n'
            '2. Mọi đa giác đều đều có một đường tròn ngoại tiếp và một đường tròn nội tiếp đồng tâm $O$ '
            '(gọi là tâm của đa giác đều).\n'
            '3. Các phép quay tâm $O$ góc quay $\\alpha = k \\cdot \\dfrac{360^\\circ}{n}$ ($k \\in '
            '\\mathbb{Z}$) biến đa giác đều $n$ cạnh thành chính nó.',
  'formulas': [{'category': 'Công thức góc và phép quay của $n$-giác đều',
                'items': [{'name': 'Số đo mỗi góc của $n$-giác đều',
                           'formula': '$\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$',
                           'note': 'Ví dụ: Lục giác đều ($n = 6$) có góc $120^\\circ$'},
                          {'name': 'Góc quay nhỏ nhất giữ nguyên $n$-giác đều',
                           'formula': '$\\alpha_{\\min} = \\dfrac{360^\\circ}{n}$',
                           'note': 'Quay quanh tâm $O$ của đa giác đều'}]}],
  'example': 'Tính số đo mỗi góc trong của một ngũ giác đều và góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác '
             'đều thành chính nó.',
  'example_answer': 'Với ngũ giác đều ($n = 5$), số đo mỗi góc trong là $\\dfrac{(5 - 2) \\cdot '
                    '180^\\circ}{5} = 108^\\circ$.\n'
                    'Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều thành chính nó là '
                    '$\\dfrac{360^\\circ}{5} = 72^\\circ$.',
  'real_life': 'Cấu trúc tổ ong hình lục giác đều, biển báo giao thông hình bát giác đều, cánh quạt trần '
               'quay quanh trục.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số đo mỗi góc của một lục giác đều ($6$ cạnh) bằng:',
            'options': ['$108^\\circ$', '$120^\\circ$', '$135^\\circ$', '$60^\\circ$'],
            'answer': 1,
            'solution': 'Áp dụng công thức với $n = 6$: $\\dfrac{(6 - 2) \\cdot 180^\\circ}{6} = '
                        '120^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phép quay thuận chiều tâm $O$ góc quay nhỏ nhất bằng bao nhiêu độ sẽ biến một hình vuông '
                 'tâm $O$ thành chính nó?',
            'options': ['$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$180^\\circ$'],
            'answer': 2,
            'solution': 'Với hình vuông ($n = 4$), góc quay nhỏ nhất giữ nguyên hình là '
                        '$\\dfrac{360^\\circ}{4} = 90^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Đa giác đều**, quy tắc hoặc công thức nào sau đây xác định đúng **Số đo '
                 'mỗi góc của $n$-giác đều**?',
            'options': ['$\\dfrac{(n + 2) \\cdot 180^\\circ}{n}$',
                        '$\\dfrac{n}{(n - 2) \\cdot 180^\\circ}$',
                        '$\\dfrac{(n - 4) \\cdot 180^\\circ}{n}$',
                        '$\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 30: Đa giác đều, **Số đo mỗi góc của $n$-giác '
                        'đều** được xác định bởi: $\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$. (Ví dụ: Lục giác '
                        'đều ($n = 6$) có góc $120^\\circ$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Đa giác đều**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Góc '
                 'quay nhỏ nhất giữ nguyên $n$-giác đều**?',
            'options': ['$\\alpha_{\\min} = \\dfrac{360^\\circ}{n}$',
                        '$\\alpha_{\\min} = \\dfrac{370^\\circ}{n}$',
                        '$\\alpha_{\\min} = \\dfrac{n}{360^\\circ}$',
                        '$\\alpha_{\\min} = \\dfrac{362^\\circ}{n}$'],
            'answer': 0,
            'solution': 'Trong Bài 30: Đa giác đều, **Góc quay nhỏ nhất giữ nguyên $n$-giác đều** có công '
                        'thức/quy tắc là: $\\alpha_{\\min} = \\dfrac{360^\\circ}{n}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cho lục giác đều $ABCDEF$ nội tiếp đường tròn $(O; 5\\text{ cm})$. Độ dài cạnh $AB$ của '
                 'lục giác đều bằng:',
            'options': ['$5\\sqrt{3}$ cm', '$5$ cm', '$10$ cm', '$2,5$ cm'],
            'answer': 1,
            'solution': 'Trong lục giác đều, tam giác $OAB$ cân tại $O$ có $\\widehat{AOB} = '
                        '\\dfrac{360^\\circ}{6} = 60^\\circ$ nên là tam giác đều, suy ra $AB = R = 5$ cm.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 30: Đa giác đều**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được đa giác đều và tính được số đo mỗi góc của $n$-giác đều. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được đa giác đều và tính được số đo mỗi góc của '
                        '$n$-giác đều.',
                        'Nhận biết được đa giác đều và tính được số đo mỗi góc của $n$-giác đều.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được đa giác đều và '
                        'tính được số đo mỗi góc của $n$-giác đều.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 30: Đa giác đều: Nhận biết được đa giác đều và tính '
                        'được số đo mỗi góc của $n$-giác đều.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho tam giác đều $ABC$ nội tiếp đường tròn tâm $O$.',
            'statements': ['Góc ở tâm $\\widehat{AOB}$ có số đo bằng $120^\\circ$.',
                           'Phép quay thuận chiều $120^\\circ$ tâm $O$ biến đỉnh $A$ thành đỉnh $B$ (hoặc '
                           '$C$).',
                           'Phép quay tâm $O$ góc $60^\\circ$ biến tam giác đều $ABC$ thành chính nó.',
                           'Mỗi góc trong của một bát giác đều ($8$ cạnh) có số đo bằng $135^\\circ$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $\\dfrac{360^\\circ}{3} = 120^\\circ$. b) Đúng. c) Sai vì góc quay phải '
                        'là bội của $120^\\circ$. d) Đúng vì $\\dfrac{(8 - 2) \\cdot 180^\\circ}{8} = '
                        '135^\\circ$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 30: Đa giác đều**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được đa giác đều và tính được '
                           'số đo mỗi góc của $n$-giác đều.',
                           'Trong **Bài 30: Đa giác đều**, quy tắc/công thức **Số đo mỗi góc của $n$-giác '
                           'đều** được viết là: $\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$.',
                           'Nếu áp dụng sai dấu/phép tính thành $\\dfrac{(n + 2) \\cdot 180^\\circ}{n}$ thì '
                           'kết quả của **Số đo mỗi góc của $n$-giác đều** trong **Bài 30: Đa giác đều** vẫn '
                           'không thay đổi.',
                           'Xét ví dụ của bài: “Tính số đo mỗi góc trong của một ngũ giác đều và góc quay '
                           'nhỏ nhất quanh tâm $O$ biến ngũ giác đều thành chính nó.”, kết quả giải đúng là: '
                           'Với ngũ giác đều ($n = 5$), số đo mỗi góc trong là $\\dfrac{(5 - 2) \\cdot '
                           '180^\\circ}{5} = 108^\\circ$. Góc quay nhỏ nhất quanh tâm $O$ bi...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 30: Đa giác đều. b) **Đúng** theo công '
                        'thức **Số đo mỗi góc của $n$-giác đều** ($\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$). '
                        'c) **Sai** vì công thức đúng của **Số đo mỗi góc của $n$-giác đều** phải là '
                        '$\\dfrac{(n - 2) \\cdot 180^\\circ}{n}$ chứ không phải $\\dfrac{(n + 2) \\cdot '
                        '180^\\circ}{n}$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 30: Đa giác đều** để giải bài toán sau: Tính số đo '
                 'mỗi góc trong của một ngũ giác đều và góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều '
                 'thành chính nó. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Với ngũ giác đều ($n = 5$), số đo mỗi góc trong là $\\dfrac{(5 + 2) \\cdot '
                        '180^\\circ}{5} = 108^\\circ$. Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều...',
                        'Với ngũ giác đều ($n = 5$), số đo mỗi góc trong là $\\dfrac{5}{(5 - 2) \\cdot '
                        '180^\\circ} = 108^\\circ$. Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều...',
                        'Với ngũ giác đều ($n = 10$), số đo mỗi góc trong là $\\dfrac{(5 - 2) \\cdot '
                        '180^\\circ}{5} = 108^\\circ$. Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều...',
                        'Với ngũ giác đều ($n = 5$), số đo mỗi góc trong là $\\dfrac{(5 - 2) \\cdot '
                        '180^\\circ}{5} = 108^\\circ$. Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Đa giác đều: Với ngũ giác đều ($n = 5$), số đo mỗi '
                        'góc trong là $\\dfrac{(5 - 2) \\cdot 180^\\circ}{5} = 108^\\circ$.\n'
                        'Góc quay nhỏ nhất quanh tâm $O$ biến ngũ giác đều thành chính nó là '
                        '$\\dfrac{360^\\circ}{5} = 72^\\circ$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đa giác đều có số đo mỗi góc trong bằng $144^\\circ$. Hỏi đa giác đều đó có bao nhiêu '
                 'cạnh?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Ta có $\\dfrac{(n - 2) \\cdot 180^\\circ}{n} = 144^\\circ \\Rightarrow 180n - 360 = '
                        '144n \\Rightarrow 36n = 360 \\Rightarrow n = 10$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch10-hinh-tru-non-cau',
  'context_title': 'Chương X: Một số hình khối trong thực tiễn',
  'context': 'Chương X · SGK Toán 9: Một số hình khối trong thực tiễn.',
  'title': 'Bài 31: Hình trụ và hình nón',
  'icon': '🎩',
  'description': 'Tính diện tích xung quanh, diện tích toàn phần và thể tích của hình trụ, hình nón.',
  'requirements': ['Nhận biết được các yếu tố (bán kính đáy, chiều cao, đường sinh) của hình trụ và hình '
                   'nón.',
                   'Tính được diện tích xung quanh, diện tích toàn phần và thể tích của hình trụ, hình nón.',
                   'Vận dụng kiến thức của **Bài 31: Hình trụ và hình nón** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': 'Khi quay một hình chữ nhật một vòng quanh một cạnh cố định ta được một hình trụ. Khi quay '
                'một tam giác vuông một vòng quanh một cạnh góc vuông cố định ta được một hình nón.',
  'theory': '1. Hình trụ có bán kính đáy $r$ và chiều cao $h$: diện tích xung quanh $S_{xq} = 2\\pi rh$, '
            'diện tích toàn phần $S_{tp} = 2\\pi rh + 2\\pi r^2$, thể tích $V = \\pi r^2h$.\n'
            '2. Hình nón có bán kính đáy $r$, chiều cao $h$ và đường sinh $l = \\sqrt{r^2 + h^2}$: diện tích '
            'xung quanh $S_{xq} = \\pi rl$, diện tích toàn phần $S_{tp} = \\pi rl + \\pi r^2$, thể tích $V = '
            '\\dfrac{1}{3}\\pi r^2h$.',
  'formulas': [{'category': 'Công thức diện tích và thể tích hình trụ, hình nón',
                'items': [{'name': 'Hình trụ ($r, h$)',
                           'formula': '$S_{xq} = 2\\pi rh$; $V = \\pi r^2h$',
                           'note': '$S_{tp} = 2\\pi rh + 2\\pi r^2$'},
                          {'name': 'Hình nón ($r, h, l$)',
                           'formula': '$S_{xq} = \\pi rl$; $V = \\dfrac{1}{3}\\pi r^2h$',
                           'note': 'Hệ thức Pythagore: $l^2 = r^2 + h^2$'}]}],
  'example': 'Cho một hình nón có bán kính đáy $r = 3$ cm và chiều cao $h = 4$ cm. Tính độ dài đường sinh, '
             'diện tích xung quanh và thể tích của hình nón.',
  'example_answer': 'Độ dài đường sinh là $l = \\sqrt{r^2 + h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm).\n'
                    'Diện tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                    '($\\text{cm}^2$).\n'
                    'Thể tích hình nón là $V = \\dfrac{1}{3}\\pi r^2h = \\dfrac{1}{3}\\pi \\cdot 3^2 \\cdot '
                    '4 = 12\\pi$ ($\\text{cm}^3$).',
  'real_life': 'Tính lượng tôn cần dùng để gò lon sữa đặc (hình trụ) hoặc diện tích lá cọ cần để chằm chiếc '
               'nón lá (hình nón).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính thể tích $V$ của hình trụ có bán kính đáy $r$ và chiều cao $h$ là:',
            'options': ['$V = \\dfrac{1}{3}\\pi r^2h$',
                        '$V = 2\\pi rh$',
                        '$V = \\pi r^2h$',
                        '$V = \\pi rh^2$'],
            'answer': 2,
            'solution': 'Thể tích hình trụ bằng diện tích đáy nhân với chiều cao: $V = \\pi r^2h$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình nón có bán kính đáy $r = 6$ cm và chiều cao $h = 8$ cm. Độ dài đường sinh $l$ của '
                 'hình nón bằng:',
            'options': ['$14$ cm', '$2\\sqrt{7}$ cm', '$100$ cm', '$10$ cm'],
            'answer': 3,
            'solution': 'Ta có $l = \\sqrt{r^2 + h^2} = \\sqrt{6^2 + 8^2} = 10$ (cm).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Hình trụ và hình nón**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Hình trụ ($r, h$)**?',
            'options': ['$S_{xq} = 2\\pi rh$; $V = \\pi r^2h$',
                        '$S_{xq} = 3\\pi rh$; $V = \\pi r^2h$',
                        '$S_{xq} = 1\\pi rh$; $V = \\pi r^2h$',
                        '$S_{xq} = 4\\pi rh$; $V = \\pi r^2h$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 31: Hình trụ và hình nón, **Hình trụ ($r, h$)** '
                        'được xác định bởi: $S_{xq} = 2\\pi rh$; $V = \\pi r^2h$. ($S_{tp} = 2\\pi rh + '
                        '2\\pi r^2$)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Hình trụ và hình nón**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Hình nón ($r, h, l$)**?',
            'options': ['$S_{xq} = \\pi rl$; $V = \\dfrac{2}{3}\\pi r^2h$',
                        '$S_{xq} = \\pi rl$; $V = \\dfrac{1}{3}\\pi r^2h$',
                        '$S_{xq} = \\pi rl$; $V = \\dfrac{3}{1}\\pi r^2h$',
                        '$S_{xq} = 2\\pi rh$; $V = \\pi r^2h$'],
            'answer': 1,
            'solution': 'Trong Bài 31: Hình trụ và hình nón, **Hình nón ($r, h, l$)** có công thức/quy tắc '
                        'là: $S_{xq} = \\pi rl$; $V = \\dfrac{1}{3}\\pi r^2h$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Một hình trụ và một hình nón có cùng bán kính đáy $r$ và cùng chiều cao $h$. Tỉ số giữa '
                 'thể tích hình trụ và thể tích hình nón đó bằng:',
            'options': ['$\\dfrac{1}{3}$', '$2$', '$3$', '$9$'],
            'answer': 2,
            'solution': 'Vì $V_{\\text{trụ}} = \\pi r^2h$ và $V_{\\text{nón}} = \\dfrac{1}{3}\\pi r^2h$ nên '
                        '$\\dfrac{V_{\\text{trụ}}}{V_{\\text{nón}}} = 3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 31: Hình trụ và hình nón**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết được các yếu tố (bán kính đáy, chiều cao, đường sinh) của hình trụ và '
                        'hình nón. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được các yếu tố (bán kính đáy, chiều cao, đường '
                        'sinh) của hình trụ và hình nón.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được các yếu tố (bán '
                        'kính đáy, chiều cao, đường sinh) của hình trụ và hình nón.',
                        'Nhận biết được các yếu tố (bán kính đáy, chiều cao, đường sinh) của hình trụ và '
                        'hình nón.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 31: Hình trụ và hình nón: Nhận biết được các yếu tố '
                        '(bán kính đáy, chiều cao, đường sinh) của hình trụ và hình nón.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho một lon nước ngọt hình trụ có bán kính đáy $r = 3$ cm và chiều cao $h = 10$ cm.',
            'statements': ['Diện tích một mặt đáy của lon nước là $9\\pi\\text{ cm}^2$.',
                           'Diện tích xung quanh của lon nước là $60\\pi\\text{ cm}^2$.',
                           'Diện tích toàn phần của lon nước là $69\\pi\\text{ cm}^2$.',
                           'Thể tích của lon nước là $90\\pi\\text{ cm}^3$.'],
            'answer': [True, True, False, True],
            'solution': 'a) Đúng vì $S_{\\text{đáy}} = \\pi r^2 = 9\\pi\\text{ cm}^2$. b) Đúng vì $S_{xq} = '
                        '2\\pi rh = 60\\pi\\text{ cm}^2$. c) Sai vì $S_{tp} = 60\\pi + 2 \\cdot 9\\pi = '
                        '78\\pi\\text{ cm}^2$. d) Đúng vì $V = \\pi r^2h = 90\\pi\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 31: Hình trụ và hình nón**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được các yếu tố (bán kính đáy, '
                           'chiều cao, đường sinh) của hình trụ và hình nón.',
                           'Trong **Bài 31: Hình trụ và hình nón**, quy tắc/công thức **Hình trụ ($r, h$)** '
                           'được viết là: $S_{xq} = 2\\pi rh$; $V = \\pi r^2h$.',
                           'Nếu áp dụng sai dấu/phép tính thành $S_{xq} = 3\\pi rh$; $V = \\pi r^2h$ thì kết '
                           'quả của **Hình trụ ($r, h$)** trong **Bài 31: Hình trụ và hình nón** vẫn không '
                           'thay đổi.',
                           'Xét ví dụ của bài: “Cho một hình nón có bán kính đáy $r = 3$ cm và chiều cao $h '
                           '= 4$ cm. Tính độ dài đường sinh, diện tích xung quanh và thể tích của hình...”, '
                           'kết quả giải đúng là: Độ dài đường sinh là $l = \\sqrt{r^2 + h^2} = \\sqrt{3^2 + '
                           '4^2} = 5$ (cm). Diện tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot '
                           '5 = 15\\pi$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 31: Hình trụ và hình nón. b) **Đúng** theo '
                        'công thức **Hình trụ ($r, h$)** ($S_{xq} = 2\\pi rh$; $V = \\pi r^2h$). c) **Sai** '
                        'vì công thức đúng của **Hình trụ ($r, h$)** phải là $S_{xq} = 2\\pi rh$; $V = \\pi '
                        'r^2h$ chứ không phải $S_{xq} = 3\\pi rh$; $V = \\pi r^2h$. d) **Đúng** theo lời '
                        'giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 31: Hình trụ và hình nón** để giải bài toán sau: '
                 'Cho một hình nón có bán kính đáy $r = 3$ cm và chiều cao $h = 4$ cm. Tính độ dài đường '
                 'sinh, diện tích xung quanh và thể tích của hình nón. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Độ dài đường sinh là $l = \\sqrt{r^2 + h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Diện '
                        'tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                        '($\\text{cm}^2$...',
                        'Độ dài đường sinh là $l = \\sqrt{r^2 - h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Diện '
                        'tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                        '($\\text{cm}^2$...',
                        'Độ dài đường sinh là $l = \\sqrt{r^2 + h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Diện '
                        'tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                        '($\\text{cm}^1$...',
                        'Độ dài đường sinh là $l = \\sqrt{r^4 + h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm). Diện '
                        'tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                        '($\\text{cm}^2$...'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Hình trụ và hình nón: Độ dài đường sinh là $l = '
                        '\\sqrt{r^2 + h^2} = \\sqrt{3^2 + 4^2} = 5$ (cm).\n'
                        'Diện tích xung quanh là $S_{xq} = \\pi rl = \\pi \\cdot 3 \\cdot 5 = 15\\pi$ '
                        '($\\text{cm}^2$).\n'
                        'Thể tích hình nón là $V = \\dfrac{1}{3}\\pi r^2h = \\dfrac{1}{3}\\pi \\cdot 3^2 '
                        '\\cdot 4 = 12\\pi$ ($\\text{cm}^3$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một chiếc phễu hình nón có bán kính đáy $r = 5$ cm và chiều cao $h = 12$ cm. Biết diện '
                 'tích xung quanh của phễu là $k\\pi$ ($\\text{cm}^2$), tìm giá trị của $k$.',
            'answer': ['65'],
            'unit': None,
            'solution': 'Đường sinh của hình nón là $l = \\sqrt{5^2 + 12^2} = 13$ (cm). Diện tích xung quanh '
                        'là $S_{xq} = \\pi rl = \\pi \\cdot 5 \\cdot 13 = 65\\pi$ ($\\text{cm}^2$), suy ra '
                        '$k = 65$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l9-ch10-hinh-tru-non-cau',
  'context_title': 'Chương X: Một số hình khối trong thực tiễn',
  'context': 'Chương X · SGK Toán 9: Một số hình khối trong thực tiễn.',
  'title': 'Bài 32: Hình cầu',
  'icon': '🌐',
  'description': 'Nhận biết hình cầu, mặt cầu và tính diện tích mặt cầu, thể tích hình cầu.',
  'requirements': ['Nhận biết được hình cầu, tâm, bán kính, đường kính và mặt cắt phẳng của hình cầu.',
                   'Tính được diện tích mặt cầu và thể tích của hình cầu.',
                   'Vận dụng kiến thức của **Bài 32: Hình cầu** để giải bài tập minh họa và bài toán thực '
                   'tiễn.'],
  'definition': 'Khi quay nửa hình tròn tâm $O$ bán kính $R$ một vòng quanh đường kính cố định thì được một '
                'hình cầu tâm $O$ bán kính $R$. Nửa đường tròn trong phép quay tạo nên mặt cầu.',
  'theory': '1. Khi cắt hình cầu bởi một mặt phẳng thì phần chung của mặt phẳng và hình cầu là một hình '
            'tròn; mặt cắt đi qua tâm được gọi là hình tròn lớn (bán kính $R$).\n'
            '2. Công thức diện tích mặt cầu bán kính $R$: $S = 4\\pi R^2$.\n'
            '3. Công thức thể tích hình cầu bán kính $R$: $V = \\dfrac{4}{3}\\pi R^3$.',
  'formulas': [{'category': 'Diện tích mặt cầu và thể tích hình cầu bán kính $R$',
                'items': [{'name': 'Diện tích mặt cầu',
                           'formula': '$S = 4\\pi R^2 = \\pi d^2$',
                           'note': '$d = 2R$ là đường kính hình cầu'},
                          {'name': 'Thể tích hình cầu',
                           'formula': '$V = \\dfrac{4}{3}\\pi R^3$',
                           'note': 'Tỉ lệ thuận với lập phương bán kính'}]}],
  'example': 'Một quả bóng đá hình cầu có bán kính $R = 11$ cm. Tính diện tích bề mặt và thể tích của quả '
             'bóng theo $\\pi$.',
  'example_answer': 'Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 11^2 = 484\\pi$ ($\\text{cm}^2$).\n'
                    'Thể tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 11^3 = '
                    '\\dfrac{5324\\pi}{3}$ ($\\text{cm}^3$).',
  'real_life': 'Tính diện tích da cần may một quả bóng rổ hoặc dung tích bồn chứa khí hóa lỏng hình cầu '
               'trong nhà máy.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Công thức tính diện tích mặt cầu có bán kính $R$ là:',
            'options': ['$S = \\pi R^2$',
                        '$S = 2\\pi R^2$',
                        '$S = \\dfrac{4}{3}\\pi R^3$',
                        '$S = 4\\pi R^2$'],
            'answer': 3,
            'solution': 'Diện tích mặt cầu bán kính $R$ được tính theo công thức $S = 4\\pi R^2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một hình cầu có bán kính $R = 3$ cm. Thể tích của hình cầu đó bằng:',
            'options': ['$36\\pi\\text{ cm}^3$',
                        '$12\\pi\\text{ cm}^3$',
                        '$27\\pi\\text{ cm}^3$',
                        '$108\\pi\\text{ cm}^3$'],
            'answer': 0,
            'solution': 'Ta có $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 3^3 = 36\\pi$ '
                        '($\\text{cm}^3$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Hình cầu**, quy tắc hoặc công thức nào sau đây xác định đúng **Diện tích '
                 'mặt cầu**?',
            'options': ['$S = 5\\pi R^2 = \\pi d^2$',
                        '$S = 4\\pi R^2 = \\pi d^2$',
                        '$S = 4\\pi R^2 = \\pi d^1$',
                        '$S = 8\\pi R^2 = \\pi d^2$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 32: Hình cầu, **Diện tích mặt cầu** được xác định '
                        'bởi: $S = 4\\pi R^2 = \\pi d^2$. ($d = 2R$ là đường kính hình cầu)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Hình cầu**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Thể '
                 'tích hình cầu**?',
            'options': ['$V = \\dfrac{5}{3}\\pi R^3$',
                        '$V = \\dfrac{3}{4}\\pi R^3$',
                        '$V = \\dfrac{4}{3}\\pi R^3$',
                        '$V = \\dfrac{8}{3}\\pi R^3$'],
            'answer': 2,
            'solution': 'Trong Bài 32: Hình cầu, **Thể tích hình cầu** có công thức/quy tắc là: $V = '
                        '\\dfrac{4}{3}\\pi R^3$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu diện tích mặt cầu bằng $100\\pi\\text{ cm}^2$ thì bán kính $R$ của mặt cầu đó bằng:',
            'options': ['$10$ cm', '$25$ cm', '$50$ cm', '$5$ cm'],
            'answer': 3,
            'solution': 'Từ $4\\pi R^2 = 100\\pi \\Rightarrow R^2 = 25 \\Rightarrow R = 5$ (cm).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 32: Hình cầu**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được hình cầu, tâm, bán kính, đường kính và mặt cắt phẳng của hình cầu.',
                        'Nhận biết được hình cầu, tâm, bán kính, đường kính và mặt cắt phẳng của hình cầu. '
                        '(với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết được hình cầu, tâm, bán kính, đường kính và mặt '
                        'cắt phẳng của hình cầu.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được hình cầu, tâm, '
                        'bán kính, đường kính và mặt cắt phẳng của hình cầu.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 32: Hình cầu: Nhận biết được hình cầu, tâm, bán kính, '
                        'đường kính và mặt cắt phẳng của hình cầu.'},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Cho một quả địa cầu mô hình dạng hình cầu có đường kính $d = 12$ cm.',
            'statements': ['Bán kính của quả địa cầu là $R = 6$ cm.',
                           'Chu vi của đường tròn lớn (đường xích đạo trên mô hình) là $12\\pi$ cm.',
                           'Diện tích bề mặt của quả địa cầu là $144\\pi\\text{ cm}^2$.',
                           'Thể tích của quả địa cầu là $144\\pi\\text{ cm}^3$.'],
            'answer': [True, True, True, False],
            'solution': 'a) Đúng vì $R = \\dfrac{d}{2} = 6$ cm. b) Đúng vì $C = 2\\pi R = 12\\pi$ cm. c) '
                        'Đúng vì $S = 4\\pi R^2 = 144\\pi\\text{ cm}^2$. d) Sai vì $V = \\dfrac{4}{3}\\pi '
                        '\\cdot 6^3 = 288\\pi\\text{ cm}^3$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf4',
            'q': 'Xét tính đúng sai của mỗi mệnh đề sau về kiến thức trong **Bài 32: Hình cầu**:',
            'statements': ['Nội dung trọng tâm của bài học yêu cầu: Nhận biết được hình cầu, tâm, bán kính, '
                           'đường kính và mặt cắt phẳng của hình cầu.',
                           'Trong **Bài 32: Hình cầu**, quy tắc/công thức **Diện tích mặt cầu** được viết '
                           'là: $S = 4\\pi R^2 = \\pi d^2$.',
                           'Nếu áp dụng sai dấu/phép tính thành $S = 5\\pi R^2 = \\pi d^2$ thì kết quả của '
                           '**Diện tích mặt cầu** trong **Bài 32: Hình cầu** vẫn không thay đổi.',
                           'Xét ví dụ của bài: “Một quả bóng đá hình cầu có bán kính $R = 11$ cm. Tính diện '
                           'tích bề mặt và thể tích của quả bóng theo $\\pi$.”, kết quả giải đúng là: Diện '
                           'tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 11^2 = 484\\pi$ ($\\text{cm}^2$). '
                           'Thể tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 11^3 '
                           '= \\dfrac{5324\\pi}{3}$...'],
            'answer': [True, True, False, True],
            'solution': 'a) **Đúng** theo yêu cầu cần đạt của Bài 32: Hình cầu. b) **Đúng** theo công thức '
                        '**Diện tích mặt cầu** ($S = 4\\pi R^2 = \\pi d^2$). c) **Sai** vì công thức đúng '
                        'của **Diện tích mặt cầu** phải là $S = 4\\pi R^2 = \\pi d^2$ chứ không phải $S = '
                        '5\\pi R^2 = \\pi d^2$. d) **Đúng** theo lời giải ví dụ minh họa trong bài học.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 32: Hình cầu** để giải bài toán sau: Một quả bóng '
                 'đá hình cầu có bán kính $R = 11$ cm. Tính diện tích bề mặt và thể tích của quả bóng theo '
                 '$\\pi$. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi : 11^2 = 484\\pi$ ($\\text{cm}^2$). Thể '
                        'tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 11^3 = '
                        '\\dfrac{5324\\pi}{3}$...',
                        'Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 11^2 = 484\\pi$ '
                        '($\\text{cm}^2$). Thể tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = '
                        '\\dfrac{4}{3}\\pi \\cdot 11^3 = \\dfrac{5324\\pi}{3}$...',
                        'Diện tích mặt cầu là $S = 4\\pi R^2 = 4\\pi \\cdot 11^2 = 484\\pi$ '
                        '($\\text{cm}^2$). Thể tích hình cầu là $V = \\dfrac{3}{4}\\pi R^3 = '
                        '\\dfrac{4}{3}\\pi \\cdot 11^3 = \\dfrac{5324\\pi}{3}$...',
                        'Diện tích mặt cầu là $S = 8\\pi R^2 = 4\\pi \\cdot 11^2 = 484\\pi$ '
                        '($\\text{cm}^2$). Thể tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = '
                        '\\dfrac{4}{3}\\pi \\cdot 11^3 = \\dfrac{5324\\pi}{3}$...'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Hình cầu: Diện tích mặt cầu là $S = 4\\pi R^2 = '
                        '4\\pi \\cdot 11^2 = 484\\pi$ ($\\text{cm}^2$).\n'
                        'Thể tích hình cầu là $V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot 11^3 = '
                        '\\dfrac{5324\\pi}{3}$ ($\\text{cm}^3$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Nếu bán kính của một hình cầu tăng lên gấp $2$ lần thì thể tích của hình cầu đó tăng lên '
                 'gấp bao nhiêu lần?',
            'answer': ['8'],
            'unit': None,
            'solution': "Vì $V = \\dfrac{4}{3}\\pi R^3$ nên khi bán kính mới là $R' = 2R$ thì $V' = "
                        '\\dfrac{4}{3}\\pi(2R)^3 = 8V$, tức là tăng gấp $8$ lần.',
            'alt': None,
            'note': None}]}]
