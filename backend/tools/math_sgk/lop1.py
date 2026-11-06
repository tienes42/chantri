"""Dữ liệu bài học SGK Toán Lớp 1 — Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Cấu trúc 3 cấp: Lớp 1 ➔ Chương/Chủ đề (topic) ➔ Từng Bài học độc lập (title).
Mỗi bài học chỉ chứa kiến thức, công thức, ví dụ và 10 câu hỏi của riêng bài học đó.
"""

GRADE = 1

LESSONS = [{'topic': 'l1-cd01-cac-so-tu-0-den-10',
  'context_title': 'Chủ đề 1: Các số từ 0 đến 10',
  'context': 'SGK Toán 1 · Chủ đề 1: Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.',
  'title': 'Bài 1: Các số 0, 1, 2, 3, 4, 5',
  'icon': '🔢',
  'description': 'Đếm, đọc, viết các số từ 0 đến 5 và nhận biết ý nghĩa của số 0.',
  'requirements': ['Đếm, đọc, viết được các số $0, 1, 2, 3, 4, 5$.',
                   'Nhận biết được số $0$ dùng để chỉ không có đồ vật nào.',
                   'Nhận biết thứ tự các số từ $0$ đến $5$.'],
  'definition': '**Số** dùng để chỉ số lượng đồ vật trong một nhóm. Nhóm không có đồ vật nào được ghi bằng '
                'số $0$. Các số theo thứ tự từ bé đến lớn trong phạm vi $5$ là: $0, 1, 2, 3, 4, 5$.',
  'theory': '- Khi đếm đồ vật, ta chỉ vào từng vật và đếm lần lượt $1, 2, 3, 4, 5$ (mỗi vật đếm đúng $1$ '
            'lần, không bỏ sót).\n'
            '- Số cuối cùng vừa đếm chính là số lượng đồ vật của cả nhóm.\n'
            '- **Số $0$:** chiếc đĩa không có quả cam nào, ta nói có $0$ quả cam.\n'
            '- Trong dãy $0, 1, 2, 3, 4, 5$, mỗi số đứng sau bằng số đứng ngay trước nó thêm $1$ đơn vị.',
  'formulas': [{'category': 'Quy tắc đếm và đọc số từ 0 đến 5',
                'items': [{'name': 'Dãy số từ 0 đến 5',
                           'formula': '$0, 1, 2, 3, 4, 5$',
                           'note': 'Đọc: không, một, hai, ba, bốn, năm.'},
                          {'name': 'Ý nghĩa số 0',
                           'formula': '$0$ chỉ không có đồ vật nào',
                           'note': 'Ví dụ: lọ hoa không có bông nào là $0$ bông hoa.'},
                          {'name': 'Số liền sau',
                           'formula': 'Số đứng ngay sau lớn hơn $1$ đơn vị',
                           'note': 'Liền sau $3$ là $4$; liền sau $4$ là $5$.'}]}],
  'example': 'Trên bàn có 4 quyển vở, trong hộp không có cái bút nào. Hãy viết số chỉ số quyển vở và số chỉ '
             'số cái bút.',
  'example_answer': 'Đếm số quyển vở: $1, 2, 3, 4$ nên viết số $4$. Trong hộp không có bút nào nên viết số '
                    '$0$.',
  'real_life': 'Đếm số ngón tay trên một bàn tay ($5$ ngón), số chân ghế ($4$ chân), số chiếc bánh trên đĩa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đếm số quả táo: 🍎🍎🍎🍎. Có bao nhiêu quả táo?',
            'options': ['$4$', '$3$', '$5$', '$2$'],
            'answer': 0,
            'solution': 'Đếm lần lượt từng quả: $1, 2, 3, 4$. Vậy có $4$ quả táo.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Chiếc đĩa không có quả cam nào. Số chỉ số quả cam trên đĩa là:',
            'options': ['$1$', '$0$', '$5$', '$2$'],
            'answer': 1,
            'solution': 'Không có quả nào thì ta dùng số $0$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 1: Các số 0, 1, 2, 3, 4, 5**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Dãy số từ 0 đến 5**?',
            'options': ['$1, 1, 2, 3, 4, 5$',
                        '$0, 1, 2, 3, 4, 4$',
                        '$0, 1, 2, 3, 4, 5$',
                        '$2, 1, 2, 3, 4, 5$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 1: Các số 0, 1, 2, 3, 4, 5, **Dãy số từ 0 đến 5** '
                        'được xác định bởi: $0, 1, 2, 3, 4, 5$. (Đọc: không, một, hai, ba, bốn, năm.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 1: Các số 0, 1, 2, 3, 4, 5**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Ý nghĩa số 0**?',
            'options': ['$1$ chỉ không có đồ vật nào',
                        '$2$ chỉ không có đồ vật nào',
                        '$0, 1, 2, 3, 4, 5$',
                        '$0$ chỉ không có đồ vật nào'],
            'answer': 3,
            'solution': 'Trong Bài 1: Các số 0, 1, 2, 3, 4, 5, **Ý nghĩa số 0** có công thức/quy tắc là: $0$ '
                        'chỉ không có đồ vật nào.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong dãy số $0, 1, 2, 3, 4, 5$, số đứng ngay sau số $3$ là số nào?',
            'options': ['$4$', '$2$', '$5$', '$1$'],
            'answer': 0,
            'solution': 'Đếm theo thứ tự: $0, 1, 2, 3, 4, 5$. Số đứng ngay sau số $3$ là số $4$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 1: Các số 0, 1, 2, 3, 4, 5**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đếm, đọc, viết được các số $1, 1, 2, 3, 4, 5$.',
                        'Đếm, đọc, viết được các số $0, 1, 2, 3, 4, 5$.',
                        'Đếm, đọc, viết được các số $0, 1, 2, 3, 4, 4$.',
                        'Đếm, đọc, viết được các số $2, 1, 2, 3, 4, 5$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 1: Các số 0, 1, 2, 3, 4, 5: Đếm, đọc, viết được các '
                        'số $0, 1, 2, 3, 4, 5$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $5$ đọc là năm và đứng ngay sau số $4$ trong dãy số từ $0$ đến $5$.”',
            'answer': True,
            'solution': 'Trong dãy $0, 1, 2, 3, 4, 5$, số $5$ đọc là năm và đứng liền sau số $4$ nên nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 1: Các số 0, 1, 2, 3, 4, 5**, quy tắc **Dãy số từ 0 đến 5** được xác định bởi '
                 '$0, 1, 2, 3, 4, 5$ và khi áp dụng cho ví dụ “Trên bàn có 4 quyển vở, trong hộp không có '
                 'cái bút nào. Hãy viết số chỉ số quyển vở và số chỉ số cái bút.” ta có lời giải: Đếm số '
                 'quyển vở: $1, 2, 3, 4$ nên viết số $4$. Trong hộp không có bút nào nên viết số $0$.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Dãy số từ 0 đến 5** ($0, 1, 2, 3, 4, 5$) '
                        'và lời giải ví dụ minh họa của Bài 1: Các số 0, 1, 2, 3, 4, 5.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 1: Các số 0, 1, 2, 3, 4, 5** để giải bài toán sau: '
                 'Trên bàn có 4 quyển vở, trong hộp không có cái bút nào. Hãy viết số chỉ số quyển vở và số '
                 'chỉ số cái bút. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đếm số quyển vở: $2, 2, 3, 4$ nên viết số $4$. Trong hộp không có bút nào nên viết '
                        'số $0$.',
                        'Đếm số quyển vở: $1, 2, 3, 4$ nên viết số $4$. Trong hộp không có bút nào nên viết '
                        'số $1$.',
                        'Đếm số quyển vở: $1, 2, 3, 4$ nên viết số $4$. Trong hộp không có bút nào nên viết '
                        'số $0$.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 1: Các số 0, 1, 2, 3, 4, 5: Đếm số quyển vở: $1, 2, 3, '
                        '4$ nên viết số $4$. Trong hộp không có bút nào nên viết số $0$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một bàn tay có $5$ ngón tay. Nếu em cụp xuống $1$ ngón tay thì còn mấy ngón tay đang xòe '
                 'ra?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Có $5$ ngón tay, cụp xuống $1$ ngón thì còn $4$ ngón tay đang xòe ($1, 2, 3, 4$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd01-cac-so-tu-0-den-10',
  'context_title': 'Chủ đề 1: Các số từ 0 đến 10',
  'context': 'SGK Toán 1 · Chủ đề 1: Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.',
  'title': 'Bài 2: Các số 6, 7, 8, 9, 10',
  'icon': '🔢',
  'description': 'Đếm, đọc, viết các số 6, 7, 8, 9, 10 và đếm xuôi, đếm ngược trong phạm vi 10.',
  'requirements': ['Đếm, đọc, viết được các số $6, 7, 8, 9, 10$.',
                   'Đếm xuôi từ $0$ đến $10$ và đếm ngược từ $10$ về $0$.',
                   'Tìm được số liền trước, số liền sau trong phạm vi $10$.'],
  'definition': 'Tiếp theo số $5$ là các số $6$ (sáu), $7$ (bảy), $8$ (tám), $9$ (chín), $10$ (mười). Số '
                '$10$ là số có hai chữ số: chữ số $1$ đứng trước, chữ số $0$ đứng sau.',
  'theory': '- **Dãy số từ $0$ đến $10$:** $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$.\n'
            '- **Đếm xuôi:** bắt đầu từ $0$ đếm tăng dần lên $10$.\n'
            '- **Đếm ngược:** bắt đầu từ $10$ đếm lùi dần về $0$: $10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0$.\n'
            '- Phân biệt chữ số $6$ (vòng tròn ở dưới) và chữ số $9$ (vòng tròn ở trên).',
  'formulas': [{'category': 'Dãy số từ 0 đến 10',
                'items': [{'name': 'Đếm xuôi',
                           'formula': '$0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$',
                           'note': 'Số liền sau bằng số đó thêm $1$.'},
                          {'name': 'Đếm ngược',
                           'formula': '$10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0$',
                           'note': 'Số liền trước bằng số đó bớt $1$.'}]}],
  'example': 'Điền số còn thiếu vào dãy số: $6, 7, \\dots, 9, \\dots$',
  'example_answer': 'Đếm tiếp sau $7$ là $8$, sau $9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 10$.',
  'real_life': 'Đếm $7$ sắc cầu vồng, $8$ chân con cua, $10$ ngón tay trên hai bàn tay.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số “chín” được viết là:',
            'options': ['$6$', '$9$', '$7$', '$10$'],
            'answer': 1,
            'solution': 'Số chín được viết là $9$ (vòng tròn ở phía trên).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đếm số quả táo: 🍎🍎🍎🍎🍎🍎🍎. Có bao nhiêu quả táo?',
            'options': ['$6$', '$8$', '$7$', '$9$'],
            'answer': 2,
            'solution': 'Đếm lần lượt từ $1$ đến $7$, có tất cả $7$ quả táo.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 2: Các số 6, 7, 8, 9, 10**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Đếm xuôi**?',
            'options': ['$1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$',
                        '$0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9$',
                        '$2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$',
                        '$0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 2: Các số 6, 7, 8, 9, 10, **Đếm xuôi** được xác '
                        'định bởi: $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10$. (Số liền sau bằng số đó thêm $1$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 2: Các số 6, 7, 8, 9, 10**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Đếm ngược**?',
            'options': ['$10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0$',
                        '$11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0$',
                        '$10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1$',
                        '$20, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0$'],
            'answer': 0,
            'solution': 'Trong Bài 2: Các số 6, 7, 8, 9, 10, **Đếm ngược** có công thức/quy tắc là: $10, 9, '
                        '8, 7, 6, 5, 4, 3, 2, 1, 0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong dãy số từ $0$ đến $10$, số đứng liền sau số $6$ là số nào?',
            'options': ['$5$', '$7$', '$8$', '$9$'],
            'answer': 1,
            'solution': 'Đếm tiếp sau $6$ là $7$. Vậy số liền sau của $6$ là $7$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 2: Các số 6, 7, 8, 9, 10**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đếm, đọc, viết được các số $7, 7, 8, 9, 10$.',
                        'Đếm, đọc, viết được các số $6, 7, 8, 9, 9$.',
                        'Đếm, đọc, viết được các số $6, 7, 8, 9, 10$.',
                        'Đếm, đọc, viết được các số $12, 7, 8, 9, 10$.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 2: Các số 6, 7, 8, 9, 10: Đếm, đọc, viết được các số '
                        '$6, 7, 8, 9, 10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Khi đếm ngược từ $10$ về $0$, ngay sau số $8$ là số $7$.”',
            'answer': True,
            'solution': 'Đếm ngược: $10, 9, 8, 7, 6, \\dots$ nên ngay sau số $8$ là số $7$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 2: Các số 6, 7, 8, 9, 10**, quy tắc **Đếm xuôi** được xác định bởi $0, 1, 2, '
                 '3, 4, 5, 6, 7, 8, 9, 10$ và khi áp dụng cho ví dụ “Điền số còn thiếu vào dãy số: $6, 7, '
                 '\\dots, 9, \\dots$” ta có lời giải: Đếm tiếp sau $7$ là $8$, sau $9$ là $10$. Dãy số đầy '
                 'đủ là $6, 7, 8, 9, 10$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đếm xuôi** ($0, 1, 2, 3, 4, 5, 6, 7, 8, '
                        '9, 10$) và lời giải ví dụ minh họa của Bài 2: Các số 6, 7, 8, 9, 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 2: Các số 6, 7, 8, 9, 10** để giải bài toán sau: '
                 'Điền số còn thiếu vào dãy số: $6, 7, \\dots, 9, \\dots$ Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Đếm tiếp sau $8$ là $8$, sau $9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 10$.',
                        'Đếm tiếp sau $7$ là $8$, sau $9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 9$.',
                        'Đếm tiếp sau $14$ là $8$, sau $9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 10$.',
                        'Đếm tiếp sau $7$ là $8$, sau $9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 10$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 2: Các số 6, 7, 8, 9, 10: Đếm tiếp sau $7$ là $8$, sau '
                        '$9$ là $10$. Dãy số đầy đủ là $6, 7, 8, 9, 10$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hai bàn tay của em có tất cả bao nhiêu ngón tay?',
            'answer': ['10'],
            'unit': None,
            'solution': 'Mỗi bàn tay có $5$ ngón, đếm cả hai bàn tay từ $1$ đến $10$ được $10$ ngón tay.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd01-cac-so-tu-0-den-10',
  'context_title': 'Chủ đề 1: Các số từ 0 đến 10',
  'context': 'SGK Toán 1 · Chủ đề 1: Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.',
  'title': 'Bài 3: Nhiều hơn, ít hơn, bằng nhau',
  'icon': '⚖️',
  'description': 'So sánh số lượng hai nhóm đồ vật bằng cách ghép đôi (nối 1 – 1).',
  'requirements': ['Biết cách ghép đôi (nối từng cặp $1 - 1$) giữa hai nhóm đồ vật.',
                   'Nhận biết và sử dụng đúng các từ: “nhiều hơn”, “ít hơn”, “bằng nhau”.',
                   'Vận dụng kiến thức của **Bài 3: Nhiều hơn, ít hơn, bằng nhau** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Khi ghép mỗi đồ vật của nhóm thứ nhất với $1$ đồ vật của nhóm thứ hai:\n'
                '- Nhóm nào còn thừa ra thì **nhiều hơn**, nhóm kia **ít hơn**.\n'
                '- Nếu không nhóm nào còn thừa thì số lượng hai nhóm **bằng nhau**.',
  'theory': '- Ví dụ: Có $4$ cái cốc và $3$ cái thìa. Đặt mỗi cái thìa vào $1$ cái cốc thì còn thừa $1$ cái '
            'cốc.\n'
            '- Ta nói: Số cốc **nhiều hơn** số thìa, hay số thìa **ít hơn** số cốc.\n'
            '- Nếu có $4$ cái cốc và $4$ cái thìa, mỗi cốc đều có đúng $1$ thìa, ta nói số cốc **bằng** số '
            'thìa.',
  'formulas': [{'category': 'Quy tắc ghép đôi so sánh',
                'items': [{'name': 'Nhiều hơn – Ít hơn',
                           'formula': 'Nhóm có vật thừa ra $\\rightarrow$ nhiều hơn; nhóm kia $\\rightarrow$ '
                                      'ít hơn'},
                          {'name': 'Bằng nhau',
                           'formula': 'Ghép vừa đủ từng cặp $1 - 1$, không thừa vật nào $\\rightarrow$ bằng '
                                      'nhau'}]}],
  'example': 'Có $5$ bạn thỏ và $4$ củ cà rốt. Hỏi số thỏ nhiều hơn hay ít hơn số cà rốt?',
  'example_answer': 'Mỗi bạn thỏ nhận $1$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 > 4$). Vậy số thỏ '
                    '**nhiều hơn** số cà rốt.',
  'real_life': 'Kiểm tra xem số ghế trong phòng họp có đủ cho số người ngồi hay không mà chưa cần đếm hết.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Khi ghép đôi mỗi con ong với $1$ bông hoa, nếu còn thừa $2$ bông hoa thì:',
            'options': ['Số hoa ít hơn số ong',
                        'Số hoa bằng số ong',
                        'Số hoa nhiều hơn số ong',
                        'Không so sánh được'],
            'answer': 2,
            'solution': 'Nhóm hoa còn thừa ra $2$ bông nên số hoa nhiều hơn số ong.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Có $3$ cái bát và $3$ cái thìa. Khi đó số bát như thế nào so với số thìa?',
            'options': ['Nhiều hơn', 'Ít hơn', 'Lớn hơn $1$', 'Bằng nhau'],
            'answer': 3,
            'solution': 'Cả hai nhóm đều có $3$ đồ vật, ghép vừa khít từng cặp nên số bát bằng số thìa.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 3: Nhiều hơn, ít hơn, bằng nhau**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Nhiều hơn – Ít hơn**?',
            'options': ['Nhóm có vật thừa ra $\\rightarrow$ nhiều hơn; nhóm kia $\\rightarrow$ ít hơn',
                        'Nhóm có vật thừa ra $\\rightarrow$ ít hơn; nhóm kia $\\rightarrow$ ít hơn',
                        'Đảo ngược vế của quy tắc: Nhóm có vật thừa ra $\\rightarrow$ nhiều hơn; nhóm kia '
                        '$\\rightarrow$ ít hơn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhóm có vật thừa ra '
                        '$\\rightarrow$ nhiều hơn; nhóm kia $\\rightarrow$ ít hơn'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 3: Nhiều hơn, ít hơn, bằng nhau, **Nhiều hơn – Ít '
                        'hơn** được xác định bởi: Nhóm có vật thừa ra $\\rightarrow$ nhiều hơn; nhóm kia '
                        '$\\rightarrow$ ít hơn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 3: Nhiều hơn, ít hơn, bằng nhau**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Bằng nhau**?',
            'options': ['Ghép vừa đủ từng cặp $1 + 1$, không thừa vật nào $\\rightarrow$ bằng nhau',
                        'Ghép vừa đủ từng cặp $1 - 1$, không thừa vật nào $\\rightarrow$ bằng nhau',
                        'Ghép vừa đủ từng cặp $1 - 2$, không thừa vật nào $\\rightarrow$ bằng nhau',
                        'Ghép vừa đủ từng cặp $2 - 1$, không thừa vật nào $\\rightarrow$ bằng nhau'],
            'answer': 1,
            'solution': 'Trong Bài 3: Nhiều hơn, ít hơn, bằng nhau, **Bằng nhau** có công thức/quy tắc là: '
                        'Ghép vừa đủ từng cặp $1 - 1$, không thừa vật nào $\\rightarrow$ bằng nhau.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết số bút chì nhiều hơn số cục tẩy. Câu nào dưới đây đúng?',
            'options': ['Số cục tẩy nhiều hơn số bút chì',
                        'Số cục tẩy bằng số bút chì',
                        'Số cục tẩy ít hơn số bút chì',
                        'Không có cục tẩy nào'],
            'answer': 2,
            'solution': 'Nếu bút chì nhiều hơn cục tẩy thì ngược lại, số cục tẩy ít hơn số bút chì.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 3: Nhiều hơn, ít hơn, bằng nhau**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Biết cách ghép đôi (nối từng cặp $1 + 1$) giữa hai nhóm đồ vật.',
                        'Biết cách ghép đôi (nối từng cặp $1 - 2$) giữa hai nhóm đồ vật.',
                        'Biết cách ghép đôi (nối từng cặp $2 - 1$) giữa hai nhóm đồ vật.',
                        'Biết cách ghép đôi (nối từng cặp $1 - 1$) giữa hai nhóm đồ vật.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 3: Nhiều hơn, ít hơn, bằng nhau: Biết cách ghép đôi '
                        '(nối từng cặp $1 - 1$) giữa hai nhóm đồ vật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Có $4$ con thỏ 🐰🐰🐰🐰 và $3$ củ cà rốt 🥕🥕🥕. Nhận định: “Số thỏ ít hơn số cà rốt.”',
            'answer': False,
            'solution': 'Ghép mỗi con thỏ với $1$ củ cà rốt thì thừa $1$ con thỏ, nên số thỏ nhiều hơn số cà '
                        'rốt. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 3: Nhiều hơn, ít hơn, bằng nhau**, quy tắc **Nhiều hơn – Ít hơn** được xác '
                 'định bởi Nhóm có vật thừa ra $\\rightarrow$ nhiều hơn; nhóm kia $\\rightarrow$ ít hơn và '
                 'khi áp dụng cho ví dụ “Có $5$ bạn thỏ và $4$ củ cà rốt. Hỏi số thỏ nhiều hơn hay ít hơn số '
                 'cà rốt?” ta có lời giải: Mỗi bạn thỏ nhận $1$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt '
                 '($5 > 4$). Vậy số thỏ **nhiều hơn** số cà rốt.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Nhiều hơn – Ít hơn** (Nhóm có vật thừa '
                        'ra $\\rightarrow$ nhiều hơn; nhóm kia $\\rightarrow$ ít hơn) và lời giải ví dụ minh '
                        'họa của Bài 3: Nhiều hơn, ít hơn, bằng nhau.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 3: Nhiều hơn, ít hơn, bằng nhau** để giải bài toán '
                 'sau: Có $5$ bạn thỏ và $4$ củ cà rốt. Hỏi số thỏ nhiều hơn hay ít hơn số cà rốt? Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Mỗi bạn thỏ nhận $1$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 > 4$). Vậy số '
                        'thỏ **nhiều hơn** số cà rốt.',
                        'Mỗi bạn thỏ nhận $1$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 < 4$). Vậy số '
                        'thỏ **nhiều hơn** số cà rốt.',
                        'Mỗi bạn thỏ nhận $1$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 > 3$). Vậy số '
                        'thỏ **nhiều hơn** số cà rốt.',
                        'Mỗi bạn thỏ nhận $2$ củ cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 > 4$). Vậy số '
                        'thỏ **nhiều hơn** số cà rốt.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 3: Nhiều hơn, ít hơn, bằng nhau: Mỗi bạn thỏ nhận $1$ củ '
                        'cà rốt thì còn $1$ bạn thỏ chưa có cà rốt ($5 > 4$). Vậy số thỏ **nhiều hơn** số cà '
                        'rốt.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên bàn có $6$ cái tách trà nhưng mới có $5$ cái đĩa lót. Cần lấy thêm mấy cái đĩa nữa để '
                 'số đĩa bằng số tách trà?',
            'answer': ['1'],
            'unit': None,
            'solution': 'Có $5$ cái đĩa cho $6$ cái tách nên còn thiếu $1$ cái đĩa để ghép đủ $6$ cặp.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd01-cac-so-tu-0-den-10',
  'context_title': 'Chủ đề 1: Các số từ 0 đến 10',
  'context': 'SGK Toán 1 · Chủ đề 1: Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.',
  'title': 'Bài 4: So sánh số',
  'icon': '🔍',
  'description': 'Sử dụng các dấu >, <, = để so sánh hai số và sắp xếp các số trong phạm vi 10.',
  'requirements': ['Nhận biết và sử dụng đúng các dấu $>$, $<$, $=$ khi so sánh hai số trong phạm vi $10$.',
                   'Xếp được thứ tự các số (không quá $4$ số) từ bé đến lớn hoặc từ lớn đến bé.',
                   'Tìm được số lớn nhất, số bé nhất trong một nhóm số.'],
  'definition': 'Để so sánh hai số, ta dùng các dấu:\n'
                '- Dấu $>$ (lớn hơn), ví dụ: $7 > 4$.\n'
                '- Dấu $<$ (bé hơn), ví dụ: $4 < 7$.\n'
                '- Dấu $=$ (bằng), ví dụ: $6 = 6$.',
  'theory': '- Trong dãy số từ $0$ đến $10$: số đứng trước **bé hơn** số đứng sau; số đứng sau **lớn hơn** '
            'số đứng trước.\n'
            '- Số $0$ là số bé nhất, số $10$ là số lớn nhất trong các số từ $0$ đến $10$.\n'
            '- **Mẹo nhớ:** Đầu nhọn của dấu $>$ hoặc $<$ luôn chỉ về phía số bé hơn.',
  'formulas': [{'category': 'Quy tắc so sánh số trong phạm vi 10',
                'items': [{'name': 'Lớn hơn',
                           'formula': '$a > b$ khi $a$ đứng sau $b$ trong dãy số',
                           'note': 'Ví dụ: $8 > 5$.'},
                          {'name': 'Bé hơn',
                           'formula': '$a < b$ khi $a$ đứng trước $b$ trong dãy số',
                           'note': 'Ví dụ: $3 < 6$.'},
                          {'name': 'Bằng nhau',
                           'formula': '$a = b$ khi hai số giống nhau',
                           'note': 'Ví dụ: $9 = 9$.'}]}],
  'example': 'a) Điền dấu $>, <, =$ vào chỗ chấm: $7 \\dots 9$.\n'
             'b) Xếp các số $6, 2, 9, 4$ theo thứ tự từ bé đến lớn.',
  'example_answer': 'a) Vì $7$ đứng trước $9$ nên $7 < 9$.\nb) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.',
  'real_life': 'So sánh số điểm thi đua giữa các tổ, xem bạn nào có nhiều bông hoa điểm tốt nhất.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $8 \\dots 5$ là:',
            'options': ['$<$', '$=$', '$+$', '$>$'],
            'answer': 3,
            'solution': 'Trong dãy số, $8$ đứng sau $5$ nên $8$ lớn hơn $5$, ta viết $8 > 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số $3, 8, 1, 6$, số bé nhất là:',
            'options': ['$1$', '$3$', '$8$', '$6$'],
            'answer': 0,
            'solution': 'Vì $1 < 3 < 6 < 8$ nên số bé nhất là $1$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 4: So sánh số**, quy tắc hoặc công thức nào sau đây xác định đúng **Lớn hơn**?',
            'options': ['$a < b$ khi $a$ đứng sau $b$ trong dãy số',
                        '$a > b$ khi $a$ đứng sau $b$ trong dãy số',
                        'Đảo ngược vế của quy tắc: $a > b$ khi $a$ đứng sau $b$ trong dãy số',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a > b$ khi $a$ đứng sau $b$ '
                        'trong dãy số'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 4: So sánh số, **Lớn hơn** được xác định bởi: $a > '
                        'b$ khi $a$ đứng sau $b$ trong dãy số. (Ví dụ: $8 > 5$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 4: So sánh số**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Bé '
                 'hơn**?',
            'options': ['$a > b$ khi $a$ đứng trước $b$ trong dãy số',
                        'Đảo ngược vế của quy tắc: $a < b$ khi $a$ đứng trước $b$ trong dãy số',
                        '$a < b$ khi $a$ đứng trước $b$ trong dãy số',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a < b$ khi $a$ đứng trước $b$ '
                        'trong dãy số'],
            'answer': 2,
            'solution': 'Trong Bài 4: So sánh số, **Bé hơn** có công thức/quy tắc là: $a < b$ khi $a$ đứng '
                        'trước $b$ trong dãy số.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Các số $7, 2, 10, 5$ viết theo thứ tự từ bé đến lớn là:',
            'options': ['$10, 7, 5, 2$', '$2, 7, 5, 10$', '$5, 2, 7, 10$', '$2, 5, 7, 10$'],
            'answer': 3,
            'solution': 'So sánh: $2 < 5 < 7 < 10$, nên thứ tự từ bé đến lớn là $2, 5, 7, 10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 4: So sánh số**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết và sử dụng đúng các dấu $>$, $<$, $=$ khi so sánh hai số trong phạm vi '
                        '$10$.',
                        'Nhận biết và sử dụng đúng các dấu $>$, $<$, $=$ khi so sánh hai số trong phạm vi '
                        '$11$.',
                        'Nhận biết và sử dụng đúng các dấu $>$, $<$, $=$ khi so sánh hai số trong phạm vi '
                        '$9$.',
                        'Nhận biết và sử dụng đúng các dấu $>$, $<$, $=$ khi so sánh hai số trong phạm vi '
                        '$20$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 4: So sánh số: Nhận biết và sử dụng đúng các dấu $>$, '
                        '$<$, $=$ khi so sánh hai số trong phạm vi $10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $0$ bé hơn tất cả các số $1, 2, 3, \\dots, 10$.”',
            'answer': True,
            'solution': 'Số $0$ đứng đầu tiên trong dãy số từ $0$ đến $10$ nên bé hơn mọi số đứng sau nó. '
                        'Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 4: So sánh số**, quy tắc **Lớn hơn** được xác định bởi $a > b$ khi $a$ đứng '
                 'sau $b$ trong dãy số và khi áp dụng cho ví dụ “a) Điền dấu $>, <, =$ vào chỗ chấm: $7 '
                 '\\dots 9$. b) Xếp các số $6, 2, 9, 4$ theo thứ tự từ bé đến lớn.” ta có lời giải: a) Vì '
                 '$7$ đứng trước $9$ nên $7 < 9$. b) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Lớn hơn** ($a > b$ khi $a$ đứng sau $b$ '
                        'trong dãy số) và lời giải ví dụ minh họa của Bài 4: So sánh số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 4: So sánh số** để giải bài toán sau: a) Điền dấu '
                 '$>, <, =$ vào chỗ chấm: $7 \\dots 9$.\n'
                 'b) Xếp các số $6, 2, 9, 4$ theo thứ tự từ bé đến lớn. Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['a) Vì $7$ đứng trước $9$ nên $7 > 9$. b) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.',
                        'a) Vì $7$ đứng trước $9$ nên $7 < 9$. b) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.',
                        'a) Vì $7$ đứng trước $9$ nên $7 < 9$. b) Sắp xếp từ bé đến lớn: $2, 4, 6, 8$.',
                        'a) Vì $14$ đứng trước $9$ nên $7 < 9$. b) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 4: So sánh số: a) Vì $7$ đứng trước $9$ nên $7 < 9$.\n'
                        'b) Sắp xếp từ bé đến lớn: $2, 4, 6, 9$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Em hãy tìm số tự nhiên lớn hơn $7$ nhưng bé hơn $9$.',
            'answer': ['8'],
            'unit': None,
            'solution': 'Trên dãy số $7, 8, 9$, số lớn hơn $7$ và bé hơn $9$ là số $8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd01-cac-so-tu-0-den-10',
  'context_title': 'Chủ đề 1: Các số từ 0 đến 10',
  'context': 'SGK Toán 1 · Chủ đề 1: Đếm, đọc, viết, so sánh và tách – gộp các số từ 0 đến 10.',
  'title': 'Bài 5: Mấy và mấy',
  'icon': '🧩',
  'description': 'Tách một số thành hai phần và gộp hai phần thành một số trong phạm vi 10.',
  'requirements': ['Nhận biết được cấu tạo số (“mấy và mấy”) thông qua thao tác tách – gộp đồ vật.',
                   'Nêu được các cách tách – gộp các số từ $2$ đến $10$.',
                   'Vận dụng kiến thức đếm, so sánh, tách – gộp để giải bài tập tổng hợp Chủ đề 1.'],
  'definition': '**Mấy và mấy** là cách nói về cấu tạo của một số: một nhóm đồ vật có thể **tách** thành hai '
                'phần, và khi **gộp** hai phần đó lại ta được số lượng ban đầu. Ví dụ: $5$ gồm $2$ và $3$; '
                'gộp $2$ và $3$ được $5$.',
  'theory': '- **Tách số:** $6$ gồm $1$ và $5$; $2$ và $4$; hoặc $3$ và $3$.\n'
            '- **Gộp số:** Gộp $4$ và $3$ được $7$; gộp $5$ và $5$ được $10$.\n'
            '- Nắm vững cấu tạo số (đặc biệt là các cặp số gộp thành $10$: $1$ và $9$, $2$ và $8$, $3$ và '
            '$7$, $4$ và $6$, $5$ và $5$) là nền tảng để học phép cộng, phép trừ.',
  'formulas': [{'category': 'Cấu tạo một số thông dụng (Mấy và mấy)',
                'items': [{'name': 'Số 5', 'formula': '$5$ gồm $1$ và $4$; $2$ và $3$'},
                          {'name': 'Số 8',
                           'formula': '$8$ gồm $1$ và $7$; $2$ và $6$; $3$ và $5$; $4$ và $4$'},
                          {'name': 'Số 10',
                           'formula': '$10$ gồm $1$ và $9$; $2$ và $8$; $3$ và $7$; $4$ và $6$; $5$ và '
                                      '$5$'}]}],
  'example': 'Mẹ có $9$ cái bánh, mẹ xếp vào đĩa thứ nhất $4$ cái bánh. Hỏi đĩa thứ hai có mấy cái bánh?',
  'example_answer': 'Vì $9$ gồm $4$ và $5$ nên đĩa thứ hai có $5$ cái bánh.',
  'real_life': 'Chia kẹo hoặc chia bút màu thành hai hộp nhỏ cho hai anh em.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Gộp $3$ quả bóng và $4$ quả bóng được mấy quả bóng?',
            'options': ['$7$', '$6$', '$8$', '$5$'],
            'answer': 0,
            'solution': 'Gộp $3$ và $4$ được $7$ quả bóng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số $6$ gồm $2$ và mấy?',
            'options': ['$3$', '$4$', '$5$', '$6$'],
            'answer': 1,
            'solution': 'Từ $2$ đếm thêm $3, 4, 5, 6$ (đếm thêm $4$ lần). Vậy $6$ gồm $2$ và $4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 5: Mấy và mấy**, quy tắc hoặc công thức nào sau đây xác định đúng **Số 5**?',
            'options': ['$6$ gồm $1$ và $4$; $2$ và $3$',
                        '$5$ gồm $1$ và $4$; $2$ và $2$',
                        '$5$ gồm $1$ và $4$; $2$ và $3$',
                        '$10$ gồm $1$ và $4$; $2$ và $3$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 5: Mấy và mấy, **Số 5** được xác định bởi: $5$ gồm '
                        '$1$ và $4$; $2$ và $3$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 5: Mấy và mấy**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng **Số '
                 '8**?',
            'options': ['$9$ gồm $1$ và $7$; $2$ và $6$; $3$ và $5$; $4$ và $4$',
                        '$8$ gồm $1$ và $7$; $2$ và $6$; $3$ và $5$; $4$ và $3$',
                        '$16$ gồm $1$ và $7$; $2$ và $6$; $3$ và $5$; $4$ và $4$',
                        '$8$ gồm $1$ và $7$; $2$ và $6$; $3$ và $5$; $4$ và $4$'],
            'answer': 3,
            'solution': 'Trong Bài 5: Mấy và mấy, **Số 8** có công thức/quy tắc là: $8$ gồm $1$ và $7$; $2$ '
                        'và $6$; $3$ và $5$; $4$ và $4$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số $8$ gồm $3$ và số nào dưới đây?',
            'options': ['$5$', '$4$', '$6$', '$2$'],
            'answer': 0,
            'solution': 'Ta có $8$ gồm $3$ và $5$ (gộp $3$ và $5$ được $8$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 5: Mấy và mấy**, nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận biết được cấu tạo số (“mấy và mấy”) thông qua thao tác tách – gộp đồ vật. (với '
                        'dấu ngược lại)',
                        'Nhận biết được cấu tạo số (“mấy và mấy”) thông qua thao tác tách – gộp đồ vật.',
                        'Đảo ngược vế của quy tắc: Nhận biết được cấu tạo số (“mấy và mấy”) thông qua thao '
                        'tác tách – gộp đồ vật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết được cấu tạo số (“mấy '
                        'và mấy”) thông qua thao tác tách – gộp đồ vật.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 5: Mấy và mấy: Nhận biết được cấu tạo số (“mấy và '
                        'mấy”) thông qua thao tác tách – gộp đồ vật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $10$ gồm $4$ và $6$, hoặc gồm $5$ và $5$.”',
            'answer': True,
            'solution': 'Gộp $4$ và $6$ được $10$, gộp $5$ và $5$ cũng được $10$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 5: Mấy và mấy**, quy tắc **Số 5** được xác định bởi $5$ gồm $1$ và $4$; $2$ và '
                 '$3$ và khi áp dụng cho ví dụ “Mẹ có $9$ cái bánh, mẹ xếp vào đĩa thứ nhất $4$ cái bánh. '
                 'Hỏi đĩa thứ hai có mấy cái bánh?” ta có lời giải: Vì $9$ gồm $4$ và $5$ nên đĩa thứ hai có '
                 '$5$ cái bánh.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số 5** ($5$ gồm $1$ và $4$; $2$ và $3$) '
                        'và lời giải ví dụ minh họa của Bài 5: Mấy và mấy.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 5: Mấy và mấy** để giải bài toán sau: Mẹ có $9$ cái '
                 'bánh, mẹ xếp vào đĩa thứ nhất $4$ cái bánh. Hỏi đĩa thứ hai có mấy cái bánh? Cách giải và '
                 'kết quả nào dưới đây là **đúng**?',
            'options': ['Vì $10$ gồm $4$ và $5$ nên đĩa thứ hai có $5$ cái bánh.',
                        'Vì $9$ gồm $4$ và $5$ nên đĩa thứ hai có $4$ cái bánh.',
                        'Vì $9$ gồm $4$ và $5$ nên đĩa thứ hai có $5$ cái bánh.',
                        'Vì $18$ gồm $4$ và $5$ nên đĩa thứ hai có $5$ cái bánh.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 5: Mấy và mấy: Vì $9$ gồm $4$ và $5$ nên đĩa thứ hai có '
                        '$5$ cái bánh.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lan có $9$ bông hoa, Lan cắm vào lọ xanh $4$ bông hoa, số hoa còn lại cắm vào lọ đỏ. Hỏi '
                 'lọ đỏ có mấy bông hoa?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Vì $9$ gồm $4$ và $5$ nên lọ đỏ có $5$ bông hoa.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd02-hinh-phang',
  'context_title': 'Chủ đề 2: Làm quen với một số hình phẳng',
  'context': 'SGK Toán 1 · Chủ đề 2: Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật; lắp '
             'ghép, xếp hình.',
  'title': 'Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật',
  'icon': '🔷',
  'description': 'Nhận dạng và phân biệt hình vuông, hình tròn, hình tam giác, hình chữ nhật qua đồ vật thật '
                 'và mô hình.',
  'requirements': ['Nhận dạng được hình vuông, hình tròn, hình tam giác, hình chữ nhật.',
                   'Phân biệt được các hình dựa vào số cạnh và đặc điểm đường bao.',
                   'Liên hệ được với các đồ vật quen thuộc trong cuộc sống.'],
  'definition': '- **Hình vuông:** có $4$ cạnh thẳng dài bằng nhau.\n'
                '- **Hình chữ nhật:** có $4$ cạnh thẳng, gồm $2$ cạnh dài bằng nhau và $2$ cạnh ngắn bằng '
                'nhau.\n'
                '- **Hình tam giác:** có $3$ cạnh thẳng.\n'
                '- **Hình tròn:** có đường bao cong khép kín, không có cạnh thẳng và không có góc.',
  'theory': '- Một hình phẳng dù được tô màu khác nhau, có kích thước to hay nhỏ, đặt thẳng hay xoay nghiêng '
            'thì tên gọi của hình vẫn không thay đổi.\n'
            '- Đồ vật thực tế: khăn mùi soa, viên gạch hoa (hình vuông); mặt đồng hồ treo tường, chiếc đĩa '
            '(hình tròn); cờ đuôi nheo, biển báo giao thông (hình tam giác); mặt bảng lớp, bìa quyển vở '
            '(hình chữ nhật).',
  'formulas': [{'category': 'Đặc điểm nhận dạng hình phẳng',
                'items': [{'name': 'Hình tam giác',
                           'formula': 'Có $3$ cạnh thẳng',
                           'note': 'Ví dụ: biển báo nguy hiểm.'},
                          {'name': 'Hình vuông',
                           'formula': 'Có $4$ cạnh thẳng dài bằng nhau',
                           'note': 'Ví dụ: mặt viên gạch hoa.'},
                          {'name': 'Hình chữ nhật',
                           'formula': 'Có $4$ cạnh ($2$ cạnh dài, $2$ cạnh ngắn)',
                           'note': 'Ví dụ: mặt bảng lớp, cánh cửa.'},
                          {'name': 'Hình tròn',
                           'formula': 'Đường cong khép kín, $0$ cạnh thẳng',
                           'note': 'Ví dụ: mặt đồng hồ tròn, đĩa tròn.'}]}],
  'example': 'Quan sát mặt bảng lớp học và chiếc đĩa tròn. Mỗi vật có dạng hình gì?',
  'example_answer': 'Mặt bảng lớp học có dạng **hình chữ nhật** (có $2$ cạnh dài và $2$ cạnh ngắn); chiếc '
                    'đĩa có dạng **hình tròn**.',
  'real_life': 'Nhận biết biển báo giao thông hình tam giác, hình tròn trên đường phố và các đồ dùng trong '
               'gia đình.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình nào dưới đây có $3$ cạnh?',
            'options': ['Hình vuông', 'Hình tam giác', 'Hình tròn', 'Hình chữ nhật'],
            'answer': 1,
            'solution': 'Hình tam giác là hình có $3$ cạnh.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mặt chiếc đồng hồ treo tường loại tròn có dạng hình gì?',
            'options': ['Hình vuông', 'Hình tam giác', 'Hình tròn', 'Hình chữ nhật'],
            'answer': 2,
            'solution': 'Mặt đồng hồ là đường cong khép kín, không có cạnh thẳng nên có dạng hình tròn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Hình tam giác**?',
            'options': ['Có $4$ cạnh thẳng', 'Có $2$ cạnh thẳng', 'Có $6$ cạnh thẳng', 'Có $3$ cạnh thẳng'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ '
                        'nhật, **Hình tam giác** được xác định bởi: Có $3$ cạnh thẳng. (Ví dụ: biển báo nguy '
                        'hiểm.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Hình vuông**?',
            'options': ['Có $4$ cạnh thẳng dài bằng nhau',
                        'Có $5$ cạnh thẳng dài bằng nhau',
                        'Có $3$ cạnh thẳng dài bằng nhau',
                        'Có $8$ cạnh thẳng dài bằng nhau'],
            'answer': 0,
            'solution': 'Trong Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật, **Hình vuông** có '
                        'công thức/quy tắc là: Có $4$ cạnh thẳng dài bằng nhau.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hình vuông và hình chữ nhật giống nhau ở điểm nào?',
            'options': ['Đều không có cạnh', 'Đều có $4$ cạnh', 'Đều có $3$ cạnh', 'Đều là đường cong'],
            'answer': 1,
            'solution': 'Cả hình vuông và hình chữ nhật đều có $4$ cạnh thẳng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận dạng được hình vuông, hình tròn, hình tam giác, hình chữ nhật. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Nhận dạng được hình vuông, hình tròn, hình tam giác, hình '
                        'chữ nhật.',
                        'Nhận dạng được hình vuông, hình tròn, hình tam giác, hình chữ nhật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận dạng được hình vuông, hình '
                        'tròn, hình tam giác, hình chữ nhật.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ '
                        'nhật: Nhận dạng được hình vuông, hình tròn, hình tam giác, hình chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu xoay nghiêng một hình tam giác thì nó không còn là hình tam giác nữa.”',
            'answer': False,
            'solution': 'Khi xoay nghiêng, hình đó vẫn có $3$ cạnh thẳng nên vẫn là hình tam giác. Nhận định '
                        'Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật**, quy tắc **Hình tam '
                 'giác** được xác định bởi Có $3$ cạnh thẳng và khi áp dụng cho ví dụ “Quan sát mặt bảng lớp '
                 'học và chiếc đĩa tròn. Mỗi vật có dạng hình gì?” ta có lời giải: Mặt bảng lớp học có dạng '
                 '**hình chữ nhật** (có $2$ cạnh dài và $2$ cạnh ngắn); chiếc đĩa có dạng **hình tròn**.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hình tam giác** (Có $3$ cạnh thẳng) và '
                        'lời giải ví dụ minh họa của Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ '
                        'nhật.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ '
                 'nhật** để giải bài toán sau: Quan sát mặt bảng lớp học và chiếc đĩa tròn. Mỗi vật có dạng '
                 'hình gì? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Mặt bảng lớp học có dạng **hình chữ nhật** (có $3$ cạnh dài và $2$ cạnh ngắn); '
                        'chiếc đĩa có dạng **hình tròn**.',
                        'Mặt bảng lớp học có dạng **hình chữ nhật** (có $2$ cạnh dài và $1$ cạnh ngắn); '
                        'chiếc đĩa có dạng **hình tròn**.',
                        'Mặt bảng lớp học có dạng **hình chữ nhật** (có $4$ cạnh dài và $2$ cạnh ngắn); '
                        'chiếc đĩa có dạng **hình tròn**.',
                        'Mặt bảng lớp học có dạng **hình chữ nhật** (có $2$ cạnh dài và $2$ cạnh ngắn); '
                        'chiếc đĩa có dạng **hình tròn**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 7: Hình vuông, hình tròn, hình tam giác, hình chữ nhật: '
                        'Mặt bảng lớp học có dạng **hình chữ nhật** (có $2$ cạnh dài và $2$ cạnh ngắn); '
                        'chiếc đĩa có dạng **hình tròn**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình vuông có tất cả bao nhiêu cạnh?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Theo đặc điểm nhận dạng, hình vuông có $4$ cạnh dài bằng nhau.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd02-hinh-phang',
  'context_title': 'Chủ đề 2: Làm quen với một số hình phẳng',
  'context': 'SGK Toán 1 · Chủ đề 2: Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật; lắp '
             'ghép, xếp hình.',
  'title': 'Bài 8: Thực hành lắp ghép, xếp hình',
  'icon': '🧱',
  'description': 'Sử dụng que tính và các tấm bìa hình phẳng để xếp, ghép thành những hình mới.',
  'requirements': ['Dùng que tính xếp được hình tam giác, hình vuông, hình chữ nhật.',
                   'Ghép được hai hay nhiều hình phẳng thành một hình mới theo mẫu.',
                   'Vận dụng kiến thức của **Bài 8: Thực hành lắp ghép, xếp hình** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': '**Lắp ghép, xếp hình** là việc dùng các que tính hoặc ghép các mảnh bìa hình vuông, hình '
                'tam giác, hình chữ nhật, hình tròn để tạo thành một hình phẳng mới hoặc các hình quen thuộc '
                '(ngôi nhà, chiếc thuyền, con cá).',
  'theory': '- Dùng các que tính dài bằng nhau:\n'
            '  + Cần ít nhất $3$ que tính để xếp $1$ hình tam giác.\n'
            '  + Cần ít nhất $4$ que tính để xếp $1$ hình vuông.\n'
            '- Ghép hình:\n'
            '  + Ghép $2$ hình tam giác vuông cân bằng nhau có thể tạo thành $1$ hình vuông hoặc $1$ hình '
            'tam giác lớn.\n'
            '  + Ghép $2$ hình vuông bằng nhau đặt sát cạnh nhau được $1$ hình chữ nhật.',
  'formulas': [{'category': 'Quy tắc xếp và ghép hình',
                'items': [{'name': 'Xếp hình tam giác', 'formula': 'Cần $3$ que tính cho $3$ cạnh'},
                          {'name': 'Xếp hình vuông',
                           'formula': 'Cần $4$ que tính dài bằng nhau cho $4$ cạnh'},
                          {'name': 'Ghép 2 hình vuông',
                           'formula': '$2$ hình vuông bằng nhau ghép sát cạnh $\\rightarrow 1$ hình chữ '
                                      'nhật'}]}],
  'example': 'Cắt một tờ giấy hình vuông theo đường chéo nối hai góc đối diện thì thu được mấy hình tam '
             'giác?',
  'example_answer': 'Đường cắt chia hình vuông thành $2$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu '
                    'được $2$ hình tam giác.',
  'real_life': 'Chơi bộ xếp hình Tangram, ghép gạch lát nền, gấp và cắt dán thủ công.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dùng các que tính dài bằng nhau, cần ít nhất mấy que tính để xếp được $1$ hình tam giác?',
            'options': ['$2$', '$4$', '$3$', '$5$'],
            'answer': 2,
            'solution': 'Hình tam giác có $3$ cạnh nên cần ít nhất $3$ que tính.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Ghép $2$ hình vuông bằng nhau sát cạnh nhau thì ta được một hình gì?',
            'options': ['Hình tròn', 'Hình tam giác', 'Hình vuông nhỏ hơn', 'Hình chữ nhật'],
            'answer': 3,
            'solution': 'Ghép $2$ hình vuông bằng nhau sát cạnh nhau sẽ tạo thành $1$ hình chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 8: Thực hành lắp ghép, xếp hình**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Xếp hình tam giác**?',
            'options': ['Cần $3$ que tính cho $3$ cạnh',
                        'Cần $4$ que tính cho $3$ cạnh',
                        'Cần $3$ que tính cho $2$ cạnh',
                        'Cần $6$ que tính cho $3$ cạnh'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 8: Thực hành lắp ghép, xếp hình, **Xếp hình tam '
                        'giác** được xác định bởi: Cần $3$ que tính cho $3$ cạnh.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 8: Thực hành lắp ghép, xếp hình**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Xếp hình vuông**?',
            'options': ['Cần $5$ que tính dài bằng nhau cho $4$ cạnh',
                        'Cần $4$ que tính dài bằng nhau cho $4$ cạnh',
                        'Cần $4$ que tính dài bằng nhau cho $3$ cạnh',
                        'Cần $8$ que tính dài bằng nhau cho $4$ cạnh'],
            'answer': 1,
            'solution': 'Trong Bài 8: Thực hành lắp ghép, xếp hình, **Xếp hình vuông** có công thức/quy tắc '
                        'là: Cần $4$ que tính dài bằng nhau cho $4$ cạnh.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Cắt một tờ giấy hình vuông theo đường thẳng nối hai góc đối diện, ta được hai hình gì?',
            'options': ['$2$ hình tròn', '$2$ hình chữ nhật', '$2$ hình tam giác', '$2$ hình vuông'],
            'answer': 2,
            'solution': 'Mỗi mảnh giấy sau khi cắt có $3$ cạnh nên là $2$ hình tam giác.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 8: Thực hành lắp ghép, xếp hình**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Dùng que tính xếp được hình tam giác, hình vuông, hình chữ nhật. (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Dùng que tính xếp được hình tam giác, hình vuông, hình '
                        'chữ nhật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Dùng que tính xếp được hình tam '
                        'giác, hình vuông, hình chữ nhật.',
                        'Dùng que tính xếp được hình tam giác, hình vuông, hình chữ nhật.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 8: Thực hành lắp ghép, xếp hình: Dùng que tính xếp '
                        'được hình tam giác, hình vuông, hình chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Chỉ cần $3$ que tính dài bằng nhau là xếp được một hình vuông.”',
            'answer': False,
            'solution': 'Hình vuông có $4$ cạnh nên cần ít nhất $4$ que tính, $3$ que tính chỉ xếp được hình '
                        'tam giác. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 8: Thực hành lắp ghép, xếp hình**, quy tắc **Xếp hình tam giác** được xác định '
                 'bởi Cần $3$ que tính cho $3$ cạnh và khi áp dụng cho ví dụ “Cắt một tờ giấy hình vuông '
                 'theo đường chéo nối hai góc đối diện thì thu được mấy hình tam giác?” ta có lời giải: '
                 'Đường cắt chia hình vuông thành $2$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu được '
                 '$2$ hình tam giác.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Xếp hình tam giác** (Cần $3$ que tính '
                        'cho $3$ cạnh) và lời giải ví dụ minh họa của Bài 8: Thực hành lắp ghép, xếp hình.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 8: Thực hành lắp ghép, xếp hình** để giải bài toán '
                 'sau: Cắt một tờ giấy hình vuông theo đường chéo nối hai góc đối diện thì thu được mấy hình '
                 'tam giác? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đường cắt chia hình vuông thành $2$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu '
                        'được $2$ hình tam giác.',
                        'Đường cắt chia hình vuông thành $3$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu '
                        'được $2$ hình tam giác.',
                        'Đường cắt chia hình vuông thành $2$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu '
                        'được $1$ hình tam giác.',
                        'Đường cắt chia hình vuông thành $4$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu '
                        'được $2$ hình tam giác.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 8: Thực hành lắp ghép, xếp hình: Đường cắt chia hình '
                        'vuông thành $2$ phần bằng nhau, mỗi phần có $3$ cạnh nên ta thu được $2$ hình tam '
                        'giác.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bạn Hà dùng que tính xếp $1$ hình tam giác và $1$ hình vuông rời nhau (không dùng chung '
                 'cạnh nào). Hỏi Hà cần tất cả bao nhiêu que tính?',
            'answer': ['7'],
            'unit': None,
            'solution': 'Hình tam giác cần $3$ que tính, hình vuông cần $4$ que tính. Đếm gộp $3$ và $4$ '
                        'được $7$ que tính.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd02-hinh-phang',
  'context_title': 'Chủ đề 2: Làm quen với một số hình phẳng',
  'context': 'SGK Toán 1 · Chủ đề 2: Nhận dạng hình vuông, hình tròn, hình tam giác, hình chữ nhật; lắp '
             'ghép, xếp hình.',
  'title': 'Bài 9: Luyện tập chung về hình phẳng',
  'icon': '🎨',
  'description': 'Đếm số lượng mỗi loại hình phẳng trong hình vẽ phức hợp và tìm quy luật dãy hình.',
  'requirements': ['Đếm đúng số hình vuông, hình tròn, hình tam giác, hình chữ nhật trong một bức tranh '
                   'ghép.',
                   'Nhận biết quy luật lặp lại của một dãy hình phẳng để tìm hình tiếp theo.',
                   'Vận dụng kiến thức của **Bài 9: Luyện tập chung về hình phẳng** để giải bài tập minh họa '
                   'và bài toán thực tiễn.'],
  'definition': 'Khi đếm hình trong bức tranh ghép, ta đếm lần lượt từng loại hình (từ trên xuống dưới hoặc '
                'từ trái sang phải) và đánh dấu để không đếm sót hoặc đếm lặp lại.',
  'theory': '- **Cách đếm hình:** Tách riêng từng yêu cầu: đếm hết hình tròn, rồi đếm hình tam giác, hình '
            'vuông, hình chữ nhật.\n'
            '- **Quy luật dãy hình:** Quan sát nhóm hình lặp đi lặp lại. Ví dụ: Vuông – Tròn – Vuông – Tròn '
            '– $\\dots$ thì nhóm lặp là (Vuông, Tròn), hình tiếp theo sau Tròn sẽ là Vuông.',
  'formulas': [{'category': 'Kỹ năng đếm hình và tìm quy luật',
                'items': [{'name': 'Đếm theo loại',
                           'formula': 'Đếm từ trên xuống dưới, từ trái sang phải cho từng loại hình'},
                          {'name': 'Dãy hình có quy luật',
                           'formula': 'Tìm cụm $2$ hoặc $3$ hình lặp lại liên tiếp'}]}],
  'example': 'Hình ngôi nhà được ghép bởi: mái nhà là $1$ hình tam giác, thân nhà là $1$ hình vuông, $2$ ô '
             'cửa sổ là $2$ hình vuông nhỏ và $1$ cửa ra vào hình chữ nhật. Có tất cả bao nhiêu hình vuông?',
  'example_answer': 'Đếm các hình vuông gồm: $1$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa sổ). '
                    'Tổng cộng có $3$ hình vuông.',
  'real_life': 'Trang trí đường diềm vở vẽ, xếp gạch lát sân theo quy luật màu sắc và hình dạng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Cho dãy hình lặp lại: ⭕ 🔺 ⭕ 🔺 ⭕ ... Hình tiếp theo vào chỗ chấm là:',
            'options': ['Hình tròn ⭕', 'Hình vuông 🟦', 'Hình chữ nhật', 'Hình tam giác 🔺'],
            'answer': 3,
            'solution': 'Quy luật là cứ $1$ hình tròn đến $1$ hình tam giác. Sau hình tròn ⭕ là hình tam '
                        'giác 🔺.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một bức tranh ông mặt trời và đám mây có $1$ hình tròn làm mặt trời và $5$ hình tam giác '
                 'làm tia nắng. Hỏi có mấy hình tam giác?',
            'options': ['$5$', '$1$', '$6$', '$4$'],
            'answer': 0,
            'solution': 'Đề bài cho biết có $5$ hình tam giác làm tia nắng.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 9: Luyện tập chung về hình phẳng**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Đếm theo loại**?',
            'options': ['Đếm từ trên xuống dưới, từ phải sang trái cho từng loại hình',
                        'Đếm từ trên xuống dưới, từ trái sang phải cho từng loại hình',
                        'Đảo ngược vế của quy tắc: Đếm từ trên xuống dưới, từ trái sang phải cho từng loại '
                        'hình',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đếm từ trên xuống dưới, từ trái '
                        'sang phải cho từng loại hình'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 9: Luyện tập chung về hình phẳng, **Đếm theo '
                        'loại** được xác định bởi: Đếm từ trên xuống dưới, từ trái sang phải cho từng loại '
                        'hình.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 9: Luyện tập chung về hình phẳng**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Dãy hình có quy luật**?',
            'options': ['Tìm cụm $3$ hoặc $3$ hình lặp lại liên tiếp',
                        'Tìm cụm $2$ hoặc $2$ hình lặp lại liên tiếp',
                        'Tìm cụm $2$ hoặc $3$ hình lặp lại liên tiếp',
                        'Tìm cụm $4$ hoặc $3$ hình lặp lại liên tiếp'],
            'answer': 2,
            'solution': 'Trong Bài 9: Luyện tập chung về hình phẳng, **Dãy hình có quy luật** có công '
                        'thức/quy tắc là: Tìm cụm $2$ hoặc $3$ hình lặp lại liên tiếp.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bạn Nam xếp hình chiếc xe gồm: thân xe là $2$ hình chữ nhật, bánh xe là $2$ hình tròn, đầu '
                 'xe là $1$ hình vuông. Chiếc xe có tất cả bao nhiêu hình phẳng?',
            'options': ['$4$', '$3$', '$6$', '$5$'],
            'answer': 3,
            'solution': 'Đếm tất cả các hình: $2$ hình chữ nhật, $2$ hình tròn và $1$ hình vuông, gộp lại '
                        'được $5$ hình phẳng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 9: Luyện tập chung về hình phẳng**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Đếm đúng số hình vuông, hình tròn, hình tam giác, hình chữ nhật trong một bức tranh '
                        'ghép.',
                        'Đếm đúng số hình vuông, hình tròn, hình tam giác, hình chữ nhật trong một bức tranh '
                        'ghép. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đếm đúng số hình vuông, hình tròn, hình tam giác, hình '
                        'chữ nhật trong một bức tranh ghép.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đếm đúng số hình vuông, hình '
                        'tròn, hình tam giác, hình chữ nhật trong một bức tranh ghép.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 9: Luyện tập chung về hình phẳng: Đếm đúng số hình '
                        'vuông, hình tròn, hình tam giác, hình chữ nhật trong một bức tranh ghép.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trong một hình ghép có $3$ hình vuông và $2$ hình tròn thì số hình vuông nhiều '
                 'hơn số hình tròn.”',
            'answer': True,
            'solution': 'Vì $3 > 2$ nên số hình vuông nhiều hơn số hình tròn. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 9: Luyện tập chung về hình phẳng**, quy tắc **Đếm theo loại** được xác định '
                 'bởi Đếm từ trên xuống dưới, từ trái sang phải cho từng loại hình và khi áp dụng cho ví dụ '
                 '“Hình ngôi nhà được ghép bởi: mái nhà là $1$ hình tam giác, thân nhà là $1$ hình vuông, '
                 '$2$ ô cửa sổ là $2$ hình vuông nhỏ và $1$ cửa ra...” ta có lời giải: Đếm các hình vuông '
                 'gồm: $1$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa sổ). Tổng cộng có $3$ hình '
                 'vuông.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đếm theo loại** (Đếm từ trên xuống dưới, '
                        'từ trái sang phải cho từng loại hình) và lời giải ví dụ minh họa của Bài 9: Luyện '
                        'tập chung về hình phẳng.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 9: Luyện tập chung về hình phẳng** để giải bài toán '
                 'sau: Hình ngôi nhà được ghép bởi: mái nhà là $1$ hình tam giác, thân nhà là $1$ hình '
                 'vuông, $2$ ô cửa sổ là $2$ hình vuông nhỏ và $1$ cửa ra vào hình chữ nhật. Có tất cả bao '
                 'nhiêu hình vuông? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đếm các hình vuông gồm: $2$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa '
                        'sổ). Tổng cộng có $3$ hình vuông.',
                        'Đếm các hình vuông gồm: $1$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa '
                        'sổ). Tổng cộng có $3$ hình vuông.',
                        'Đếm các hình vuông gồm: $1$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa '
                        'sổ). Tổng cộng có $2$ hình vuông.',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 9: Luyện tập chung về hình phẳng: Đếm các hình vuông '
                        'gồm: $1$ hình vuông lớn (thân nhà) và $2$ hình vuông nhỏ (cửa sổ). Tổng cộng có $3$ '
                        'hình vuông.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bạn An dùng que tính xếp $2$ hình tam giác rời nhau (không chung cạnh). Hỏi bạn An đã dùng '
                 'tất cả bao nhiêu que tính?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Mỗi hình tam giác dùng $3$ que tính. Hai hình tam giác rời nhau dùng $6$ que tính '
                        '($1, 2, 3, 4, 5, 6$).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd03-cong-tru-pham-vi-10',
  'context_title': 'Chủ đề 3: Phép cộng, phép trừ trong phạm vi 10',
  'context': 'SGK Toán 1 · Chủ đề 3: Ý nghĩa, cách tính và bảng cộng, bảng trừ trong phạm vi 10.',
  'title': 'Bài 10: Phép cộng trong phạm vi 10',
  'icon': '➕',
  'description': 'Nhận biết ý nghĩa phép cộng (gộp lại, thêm vào), tính chất đổi chỗ và phép cộng với số 0.',
  'requirements': ['Nhận biết ý nghĩa của phép cộng là gộp lại hoặc thêm vào.',
                   'Thực hiện được phép cộng hai số trong phạm vi $10$.',
                   'Biết tính chất cộng với $0$ ($a + 0 = a$) và đổi chỗ hai số trong phép cộng ($a + b = b '
                   '+ a$).'],
  'definition': '**Phép cộng** (ký hiệu dấu $+$) được dùng khi **gộp** hai nhóm đồ vật lại với nhau hoặc '
                '**thêm vào** một nhóm. Ví dụ: Gộp $3$ quả bóng và $2$ quả bóng được $5$ quả bóng, viết là '
                '$3 + 2 = 5$ (đọc: ba cộng hai bằng năm).',
  'theory': '- **Cách tính bằng đếm thêm:** Để tính $5 + 2$, ta bắt đầu từ $5$ đếm thêm $2$ bước: $6, 7$. '
            'Vậy $5 + 2 = 7$.\n'
            '- **Dựa vào cấu tạo số (mấy và mấy):** Vì gộp $4$ và $3$ được $7$ nên $4 + 3 = 7$.\n'
            '- **Số $0$ trong phép cộng:** Bất kỳ số nào cộng với $0$ (hoặc $0$ cộng với số đó) đều bằng '
            'chính số đó: $4 + 0 = 4$, $0 + 4 = 4$.\n'
            '- **Tính chất đổi chỗ:** Khi đổi chỗ hai số trong phép cộng thì kết quả không thay đổi: $2 + 6 '
            '= 6 + 2 = 8$.',
  'formulas': [{'category': 'Quy tắc phép cộng trong phạm vi 10',
                'items': [{'name': 'Ý nghĩa phép cộng',
                           'formula': 'Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$',
                           'note': 'Ví dụ: $3 + 2 = 5$.'},
                          {'name': 'Cộng với số 0',
                           'formula': '$a + 0 = 0 + a = a$',
                           'note': 'Ví dụ: $6 + 0 = 6$; $0 + 9 = 9$.'},
                          {'name': 'Đổi chỗ hai số',
                           'formula': '$a + b = b + a$',
                           'note': 'Ví dụ: $3 + 5 = 5 + 3 = 8$.'}]}],
  'example': 'Có $4$ con chim đậu trên cành, sau đó có thêm $3$ con chim bay tới. Hỏi trên cành có tất cả '
             'mấy con chim?',
  'example_answer': '“Bay tới” là thêm vào nên ta thực hiện phép cộng: $4 + 3 = 7$ (con chim).',
  'real_life': 'Tính tổng số bút màu khi gộp hộp bút của hai bạn hoặc khi được mẹ mua thêm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $3 + 4$ là:',
            'options': ['$7$', '$6$', '$8$', '$5$'],
            'answer': 0,
            'solution': 'Đếm thêm $4$ bắt đầu từ $3$: $4, 5, 6, 7$. Vậy $3 + 4 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $5 + 0$ là:',
            'options': ['$0$', '$5$', '$1$', '$50$'],
            'answer': 1,
            'solution': 'Số nào cộng với $0$ cũng bằng chính số đó: $5 + 0 = 5$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 10: Phép cộng trong phạm vi 10**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Ý nghĩa phép cộng**?',
            'options': ['Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$',
                        'Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Gộp lại / Thêm vào '
                        '$\\rightarrow$ dùng dấu $+$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 10: Phép cộng trong phạm vi 10, **Ý nghĩa phép '
                        'cộng** được xác định bởi: Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$. (Ví dụ: '
                        '$3 + 2 = 5$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 10: Phép cộng trong phạm vi 10**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Cộng với số 0**?',
            'options': ['$a - 0 = 0 + a = a$',
                        '$a + 0 = 1 + a = a$',
                        '$a + 2 = 0 + a = a$',
                        '$a + 0 = 0 + a = a$'],
            'answer': 3,
            'solution': 'Trong Bài 10: Phép cộng trong phạm vi 10, **Cộng với số 0** có công thức/quy tắc '
                        'là: $a + 0 = 0 + a = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Có $4$ quả bóng đỏ, gộp thêm $2$ quả bóng xanh. Phép tính thích hợp để tìm tổng số quả '
                 'bóng là:',
            'options': ['$4 + 2 = 6$', '$4 - 2 = 2$', '$2 + 2 = 4$', '$4 + 0 = 4$'],
            'answer': 0,
            'solution': 'Gộp thêm $2$ quả bóng ta dùng phép cộng: $4 + 2 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 10: Phép cộng trong phạm vi 10**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết ý nghĩa của phép cộng là gộp lại hoặc thêm vào. (với dấu ngược lại)',
                        'Nhận biết ý nghĩa của phép cộng là gộp lại hoặc thêm vào.',
                        'Đảo ngược vế của quy tắc: Nhận biết ý nghĩa của phép cộng là gộp lại hoặc thêm vào.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết ý nghĩa của phép cộng '
                        'là gộp lại hoặc thêm vào.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 10: Phép cộng trong phạm vi 10: Nhận biết ý nghĩa của '
                        'phép cộng là gộp lại hoặc thêm vào.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$2 + 7 = 7 + 2$.”',
            'answer': True,
            'solution': 'Ta có $2 + 7 = 9$ và $7 + 2 = 9$. Khi đổi chỗ các số trong phép cộng, kết quả không '
                        'đổi nên nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 10: Phép cộng trong phạm vi 10**, quy tắc **Ý nghĩa phép cộng** được xác định '
                 'bởi Gộp lại / Thêm vào $\\rightarrow$ dùng dấu $+$ và khi áp dụng cho ví dụ “Có $4$ con '
                 'chim đậu trên cành, sau đó có thêm $3$ con chim bay tới. Hỏi trên cành có tất cả mấy con '
                 'chim?” ta có lời giải: “Bay tới” là thêm vào nên ta thực hiện phép cộng: $4 + 3 = 7$ (con '
                 'chim).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ý nghĩa phép cộng** (Gộp lại / Thêm vào '
                        '$\\rightarrow$ dùng dấu $+$) và lời giải ví dụ minh họa của Bài 10: Phép cộng trong '
                        'phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 10: Phép cộng trong phạm vi 10** để giải bài toán '
                 'sau: Có $4$ con chim đậu trên cành, sau đó có thêm $3$ con chim bay tới. Hỏi trên cành có '
                 'tất cả mấy con chim? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['“Bay tới” là thêm vào nên ta thực hiện phép cộng: $4 - 3 = 7$ (con chim).',
                        '“Bay tới” là thêm vào nên ta thực hiện phép cộng: $4 + 3 = 6$ (con chim).',
                        '“Bay tới” là thêm vào nên ta thực hiện phép cộng: $4 + 3 = 7$ (con chim).',
                        '“Bay tới” là thêm vào nên ta thực hiện phép cộng: $8 + 3 = 7$ (con chim).'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 10: Phép cộng trong phạm vi 10: “Bay tới” là thêm vào '
                        'nên ta thực hiện phép cộng: $4 + 3 = 7$ (con chim).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong giỏ có $6$ quả táo, mẹ bỏ thêm vào giỏ $3$ quả táo nữa. Hỏi trong giỏ có tất cả bao '
                 'nhiêu quả táo?',
            'answer': ['9'],
            'unit': None,
            'solution': 'Ta có phép cộng: $6 + 3 = 9$ (quả táo).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd03-cong-tru-pham-vi-10',
  'context_title': 'Chủ đề 3: Phép cộng, phép trừ trong phạm vi 10',
  'context': 'SGK Toán 1 · Chủ đề 3: Ý nghĩa, cách tính và bảng cộng, bảng trừ trong phạm vi 10.',
  'title': 'Bài 11: Phép trừ trong phạm vi 10',
  'icon': '➖',
  'description': 'Nhận biết ý nghĩa phép trừ (bớt đi, tách ra) và phép trừ với số 0 trong phạm vi 10.',
  'requirements': ['Nhận biết ý nghĩa của phép trừ là bớt đi hoặc tách ra để tìm phần còn lại.',
                   'Thực hiện được phép trừ các số trong phạm vi $10$.',
                   'Biết quy tắc trừ đi $0$ ($a - 0 = a$) và hai số giống nhau trừ nhau ($a - a = 0$).'],
  'definition': '**Phép trừ** (ký hiệu dấu $-$) được dùng khi **bớt đi** một số đồ vật hoặc **tách** một '
                'nhóm thành hai phần để tìm phần còn lại. Ví dụ: Có $6$ quả cam, ăn bớt $1$ quả còn lại $5$ '
                'quả, viết là $6 - 1 = 5$ (đọc: sáu trừ một bằng năm).',
  'theory': '- **Cách tính bằng đếm bớt (đếm lùi):** Để tính $8 - 3$, ta đếm lùi $3$ bước từ $8$: $7, 6, 5$. '
            'Vậy $8 - 3 = 5$.\n'
            '- **Dựa vào cấu tạo số:** Vì $7$ gồm $2$ và $5$ nên khi tách $2$ ra khỏi $7$ ta còn $5$, tức là '
            '$7 - 2 = 5$.\n'
            '- **Số $0$ trong phép trừ:**\n'
            '  + Một số trừ đi $0$ thì vẫn bằng chính số đó: $6 - 0 = 6$.\n'
            '  + Một số trừ đi chính nó thì bằng $0$: $6 - 6 = 0$.',
  'formulas': [{'category': 'Quy tắc phép trừ trong phạm vi 10',
                'items': [{'name': 'Ý nghĩa phép trừ',
                           'formula': 'Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu $-$',
                           'note': 'Ví dụ: $7 - 3 = 4$.'},
                          {'name': 'Trừ đi 0', 'formula': '$a - 0 = a$', 'note': 'Ví dụ: $8 - 0 = 8$.'},
                          {'name': 'Trừ chính nó',
                           'formula': '$a - a = 0$',
                           'note': 'Ví dụ: $8 - 8 = 0$.'}]}],
  'example': 'Trong bến có $8$ chiếc ô tô, sau đó $3$ chiếc ô tô rời bến. Hỏi trong bến còn lại mấy chiếc ô '
             'tô?',
  'example_answer': '“Rời bến” là bớt đi nên ta dùng phép trừ: $8 - 3 = 5$ (chiếc ô tô).',
  'real_life': 'Tính số kẹo còn lại sau khi chia cho bạn, số trang truyện còn lại chưa đọc.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $9 - 5$ là:',
            'options': ['$5$', '$4$', '$3$', '$14$'],
            'answer': 1,
            'solution': 'Đếm lùi $5$ bước từ $9$: $8, 7, 6, 5, 4$. Vậy $9 - 5 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $7 - 0$ là:',
            'options': ['$0$', '$6$', '$7$', '$1$'],
            'answer': 2,
            'solution': 'Một số trừ đi $0$ thì bằng chính số đó: $7 - 0 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 11: Phép trừ trong phạm vi 10**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Ý nghĩa phép trừ**?',
            'options': ['Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu $-$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu '
                        '$-$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Bớt đi / Tách ra tìm phần còn '
                        'lại $\\rightarrow$ dùng dấu $-$',
                        'Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu $-$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 11: Phép trừ trong phạm vi 10, **Ý nghĩa phép '
                        'trừ** được xác định bởi: Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu '
                        '$-$. (Ví dụ: $7 - 3 = 4$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 11: Phép trừ trong phạm vi 10**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Trừ đi 0**?',
            'options': ['$a - 0 = a$', '$a + 0 = a$', '$a - 1 = a$', '$a - 2 = a$'],
            'answer': 0,
            'solution': 'Trong Bài 11: Phép trừ trong phạm vi 10, **Trừ đi 0** có công thức/quy tắc là: $a - '
                        '0 = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Có $7$ bông hoa gồm hoa đỏ và hoa vàng, trong đó có $2$ bông hoa vàng. Phép tính tìm số '
                 'bông hoa đỏ là:',
            'options': ['$7 + 2 = 9$', '$7 - 2 = 5$', '$7 - 7 = 0$', '$5 - 2 = 3$'],
            'answer': 1,
            'solution': 'Tách $2$ bông vàng ra khỏi $7$ bông hoa ta dùng phép trừ: $7 - 2 = 5$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 11: Phép trừ trong phạm vi 10**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết ý nghĩa của phép trừ là bớt đi hoặc tách ra để tìm phần còn lại. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết ý nghĩa của phép trừ là bớt đi hoặc tách ra để '
                        'tìm phần còn lại.',
                        'Nhận biết ý nghĩa của phép trừ là bớt đi hoặc tách ra để tìm phần còn lại.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết ý nghĩa của phép trừ '
                        'là bớt đi hoặc tách ra để tìm phần còn lại.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 11: Phép trừ trong phạm vi 10: Nhận biết ý nghĩa của '
                        'phép trừ là bớt đi hoặc tách ra để tìm phần còn lại.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$8 - 8 = 8$.”',
            'answer': False,
            'solution': 'Có $8$ bớt đi cả $8$ thì còn $0$, tức là $8 - 8 = 0$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 11: Phép trừ trong phạm vi 10**, quy tắc **Ý nghĩa phép trừ** được xác định '
                 'bởi Bớt đi / Tách ra tìm phần còn lại $\\rightarrow$ dùng dấu $-$ và khi áp dụng cho ví dụ '
                 '“Trong bến có $8$ chiếc ô tô, sau đó $3$ chiếc ô tô rời bến. Hỏi trong bến còn lại mấy '
                 'chiếc ô tô?” ta có lời giải: “Rời bến” là bớt đi nên ta dùng phép trừ: $8 - 3 = 5$ (chiếc '
                 'ô tô).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ý nghĩa phép trừ** (Bớt đi / Tách ra tìm '
                        'phần còn lại $\\rightarrow$ dùng dấu $-$) và lời giải ví dụ minh họa của Bài 11: '
                        'Phép trừ trong phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 11: Phép trừ trong phạm vi 10** để giải bài toán '
                 'sau: Trong bến có $8$ chiếc ô tô, sau đó $3$ chiếc ô tô rời bến. Hỏi trong bến còn lại mấy '
                 'chiếc ô tô? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['“Rời bến” là bớt đi nên ta dùng phép trừ: $8 + 3 = 5$ (chiếc ô tô).',
                        '“Rời bến” là bớt đi nên ta dùng phép trừ: $8 - 3 = 4$ (chiếc ô tô).',
                        '“Rời bến” là bớt đi nên ta dùng phép trừ: $16 - 3 = 5$ (chiếc ô tô).',
                        '“Rời bến” là bớt đi nên ta dùng phép trừ: $8 - 3 = 5$ (chiếc ô tô).'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 11: Phép trừ trong phạm vi 10: “Rời bến” là bớt đi nên '
                        'ta dùng phép trừ: $8 - 3 = 5$ (chiếc ô tô).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên cành có $7$ con chim, sau đó $3$ con bay đi. Hỏi trên cành còn lại mấy con chim?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Ta thực hiện phép trừ: $7 - 3 = 4$ (con chim).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd03-cong-tru-pham-vi-10',
  'context_title': 'Chủ đề 3: Phép cộng, phép trừ trong phạm vi 10',
  'context': 'SGK Toán 1 · Chủ đề 3: Ý nghĩa, cách tính và bảng cộng, bảng trừ trong phạm vi 10.',
  'title': 'Bài 12: Bảng cộng, bảng trừ trong phạm vi 10',
  'icon': '📋',
  'description': 'Ghi nhớ bảng cộng, bảng trừ trong phạm vi 10 và mối liên hệ giữa phép cộng với phép trừ.',
  'requirements': ['Thuộc và vận dụng được bảng cộng, bảng trừ trong phạm vi $10$ để tính nhẩm nhanh.',
                   'Nhận biết được các cặp số cộng lại bằng $10$ (bảng tròn $10$).',
                   'Hiểu mối liên hệ giữa phép cộng và phép trừ: từ $1$ phép cộng viết được $2$ phép trừ '
                   'tương ứng.'],
  'definition': '**Bảng cộng, bảng trừ trong phạm vi $10$** hệ thống toàn bộ các phép tính cộng, trừ có kết '
                'quả không vượt quá $10$. Khi biết $a + b = c$, ta suy ra được hai phép trừ: $c - a = b$ và '
                '$c - b = a$.',
  'theory': '- **Các phép cộng bằng $10$ (rất quan trọng):**\n'
            '  $1 + 9 = 10$; $2 + 8 = 10$; $3 + 7 = 10$; $4 + 6 = 10$; $5 + 5 = 10$.\n'
            '- **Các phép trừ từ $10$:**\n'
            '  $10 - 1 = 9$; $10 - 2 = 8$; $10 - 3 = 7$; $10 - 4 = 6$; $10 - 5 = 5$.\n'
            '- **Liên hệ Cộng – Trừ:** Vì $3 + 5 = 8$ nên $8 - 3 = 5$ và $8 - 5 = 3$.',
  'formulas': [{'category': 'Bảng tròn 10 và liên hệ Cộng – Trừ',
                'items': [{'name': 'Các cặp số có tổng bằng 10',
                           'formula': '$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$'},
                          {'name': 'Trừ từ 10',
                           'formula': '$10 - 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 5$'},
                          {'name': 'Mối liên hệ Cộng – Trừ',
                           'formula': 'Nếu $a + b = c$ thì $c - a = b$ và $c - b = a$',
                           'note': 'Ví dụ: $6 + 3 = 9 \\Rightarrow 9 - 6 = 3;\\ 9 - 3 = 6$.'}]}],
  'example': 'Từ phép cộng $4 + 6 = 10$, em hãy viết hai phép trừ tương ứng.',
  'example_answer': 'Hai phép trừ tương ứng là: $10 - 4 = 6$ và $10 - 6 = 4$.',
  'real_life': 'Tính nhẩm nhanh tiền thừa khi mua món đồ giá $6$ nghìn đồng bằng tờ $10$ nghìn đồng ($10 - 6 '
               '= 4$).',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bằng $10$?',
            'options': ['$4 + 5$', '$7 + 2$', '$6 + 4$', '$10 - 1$'],
            'answer': 2,
            'solution': 'Ta có $6 + 4 = 10$ (các phép tính còn lại đều có kết quả bằng $9$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $10 - 3$ là:',
            'options': ['$6$', '$8$', '$5$', '$7$'],
            'answer': 3,
            'solution': 'Vì $3 + 7 = 10$ nên $10 - 3 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 12: Bảng cộng, bảng trừ trong phạm vi 10**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Các cặp số có tổng bằng 10**?',
            'options': ['$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$',
                        '$1 - 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$',
                        '$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 9$',
                        '$2 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 12: Bảng cộng, bảng trừ trong phạm vi 10, **Các '
                        'cặp số có tổng bằng 10** được xác định bởi: $1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 '
                        '= 10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 12: Bảng cộng, bảng trừ trong phạm vi 10**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Trừ từ 10**?',
            'options': ['$10 + 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 5$',
                        '$10 - 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 5$',
                        '$10 - 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 4$',
                        '$20 - 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 5$'],
            'answer': 1,
            'solution': 'Trong Bài 12: Bảng cộng, bảng trừ trong phạm vi 10, **Trừ từ 10** có công thức/quy '
                        'tắc là: $10 - 1 = 9;\\ 10 - 2 = 8;\\ 10 - 3 = 7;\\ 10 - 4 = 6;\\ 10 - 5 = 5$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Biết $6 + 3 = 9$. Phép trừ nào dưới đây đúng?',
            'options': ['$9 - 3 = 5$', '$6 - 3 = 9$', '$9 - 6 = 3$', '$9 - 9 = 3$'],
            'answer': 2,
            'solution': 'Từ $6 + 3 = 9$ suy ra $9 - 6 = 3$ và $9 - 3 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 12: Bảng cộng, bảng trừ trong phạm vi 10**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Thuộc và vận dụng được bảng cộng, bảng trừ trong phạm vi $11$ để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng, bảng trừ trong phạm vi $9$ để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng, bảng trừ trong phạm vi $20$ để tính nhẩm nhanh.',
                        'Thuộc và vận dụng được bảng cộng, bảng trừ trong phạm vi $10$ để tính nhẩm nhanh.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 12: Bảng cộng, bảng trừ trong phạm vi 10: Thuộc và '
                        'vận dụng được bảng cộng, bảng trừ trong phạm vi $10$ để tính nhẩm nhanh.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Từ phép cộng $2 + 8 = 10$, ta suy ra được $10 - 8 = 2$.”',
            'answer': True,
            'solution': 'Lấy kết quả $10$ trừ đi một số trong phép cộng sẽ được số kia: $10 - 8 = 2$. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 12: Bảng cộng, bảng trừ trong phạm vi 10**, quy tắc **Các cặp số có tổng bằng '
                 '10** được xác định bởi $1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$ và khi áp dụng cho ví '
                 'dụ “Từ phép cộng $4 + 6 = 10$, em hãy viết hai phép trừ tương ứng.” ta có lời giải: Hai '
                 'phép trừ tương ứng là: $10 - 4 = 6$ và $10 - 6 = 4$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Các cặp số có tổng bằng 10** ($1 + 9 = 2 '
                        '+ 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$) và lời giải ví dụ minh họa của Bài 12: Bảng '
                        'cộng, bảng trừ trong phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 12: Bảng cộng, bảng trừ trong phạm vi 10** để giải '
                 'bài toán sau: Từ phép cộng $4 + 6 = 10$, em hãy viết hai phép trừ tương ứng. Cách giải và '
                 'kết quả nào dưới đây là **đúng**?',
            'options': ['Hai phép trừ tương ứng là: $10 - 4 = 6$ và $10 - 6 = 4$.',
                        'Hai phép trừ tương ứng là: $10 + 4 = 6$ và $10 - 6 = 4$.',
                        'Hai phép trừ tương ứng là: $10 - 4 = 6$ và $10 - 6 = 3$.',
                        'Hai phép trừ tương ứng là: $20 - 4 = 6$ và $10 - 6 = 4$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 12: Bảng cộng, bảng trừ trong phạm vi 10: Hai phép trừ '
                        'tương ứng là: $10 - 4 = 6$ và $10 - 6 = 4$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số thích hợp điền vào chỗ chấm trong phép tính $4 + \\dots = 10$ là số nào?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Vì $10 - 4 = 6$ (hoặc cặp tròn chục $4$ và $6$) nên số cần điền là $6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd03-cong-tru-pham-vi-10',
  'context_title': 'Chủ đề 3: Phép cộng, phép trừ trong phạm vi 10',
  'context': 'SGK Toán 1 · Chủ đề 3: Ý nghĩa, cách tính và bảng cộng, bảng trừ trong phạm vi 10.',
  'title': 'Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi 10',
  'icon': '🎯',
  'description': 'Thực hiện dãy tính có hai dấu phép tính cộng, trừ và giải toán qua tranh vẽ, tình huống '
                 'thực tế.',
  'requirements': ['Tính được biểu thức có hai dấu phép tính cộng, trừ theo thứ tự từ trái sang phải.',
                   'So sánh được kết quả của hai phép tính.',
                   'Viết được phép tính cộng hoặc trừ phù hợp với tình huống thực tế.'],
  'definition': 'Với dãy tính có **hai dấu phép tính** cộng, trừ (ví dụ $8 - 3 + 2$), ta thực hiện lần lượt '
                '**từ trái sang phải**: tính phép tính bên trái trước, được kết quả bao nhiêu rồi mới thực '
                'hiện phép tính tiếp theo.',
  'theory': '- Ví dụ 1: Tính $4 + 3 + 2$. Bước 1: $4 + 3 = 7$. Bước 2: $7 + 2 = 9$. Vậy $4 + 3 + 2 = 9$.\n'
            '- Ví dụ 2: Tính $9 - 4 + 3$. Bước 1: $9 - 4 = 5$. Bước 2: $5 + 3 = 8$. Vậy $9 - 4 + 3 = 8$.\n'
            '- Khi so sánh hai phép tính (như $3 + 5 \\dots 10 - 2$), ta tính kết quả mỗi bên trước rồi mới '
            'điền dấu $>, <, =$.',
  'formulas': [{'category': 'Quy tắc tính dãy tính và giải toán',
                'items': [{'name': 'Hai dấu phép tính',
                           'formula': 'Tính lần lượt từ trái sang phải',
                           'note': 'Ví dụ: $7 - 2 + 4 = 5 + 4 = 9$.'},
                          {'name': 'Tìm số chưa biết',
                           'formula': 'Nếu $a + ? = c$ thì $? = c - a$',
                           'note': 'Ví dụ: $2 + ? = 9 \\Rightarrow ? = 9 - 2 = 7$.'}]}],
  'example': 'Tính: $10 - 4 - 3 = ?$',
  'example_answer': 'Tính từ trái sang phải: $10 - 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = 3$.',
  'real_life': 'Tính số hành khách trên xe buýt sau khi có người xuống xe và có người mới lên xe tại trạm '
               'dừng.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $3 + 2 + 4$ là:',
            'options': ['$8$', '$10$', '$7$', '$9$'],
            'answer': 3,
            'solution': 'Tính từ trái sang phải: $3 + 2 = 5$, sau đó $5 + 4 = 9$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $8 - 3 + 2$ là:',
            'options': ['$7$', '$3$', '$9$', '$6$'],
            'answer': 0,
            'solution': 'Tính từ trái sang phải: $8 - 3 = 5$, sau đó $5 + 2 = 7$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi 10**, quy tắc hoặc '
                 'công thức nào sau đây xác định đúng **Hai dấu phép tính**?',
            'options': ['Tính lần lượt từ phải sang trái',
                        'Tính lần lượt từ trái sang phải',
                        'Đảo ngược vế của quy tắc: Tính lần lượt từ trái sang phải',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính lần lượt từ trái sang '
                        'phải'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 13: Luyện tập chung về phép cộng, phép trừ trong '
                        'phạm vi 10, **Hai dấu phép tính** được xác định bởi: Tính lần lượt từ trái sang '
                        'phải. (Ví dụ: $7 - 2 + 4 = 5 + 4 = 9$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi 10**, biểu thức '
                 'hoặc quy tắc nào dưới đây biểu diễn đúng **Tìm số chưa biết**?',
            'options': ['Nếu $a - ? = c$ thì $? = c - a$',
                        'Đảo ngược vế của quy tắc: Nếu $a + ? = c$ thì $? = c - a$',
                        'Nếu $a + ? = c$ thì $? = c - a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nếu $a + ? = c$ thì $? = c - '
                        'a$'],
            'answer': 2,
            'solution': 'Trong Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi 10, **Tìm số '
                        'chưa biết** có công thức/quy tắc là: Nếu $a + ? = c$ thì $? = c - a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $5 + 3 \\dots 10 - 2$ là:',
            'options': ['$>$', '$<$', '$-$', '$=$'],
            'answer': 3,
            'solution': 'Ta có $5 + 3 = 8$ và $10 - 2 = 8$. Vì $8 = 8$ nên điền dấu $=$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi '
                 '10**, nhận định nào sau đây là **chính xác**?',
            'options': ['Tính được biểu thức có hai dấu phép tính cộng, trừ theo thứ tự từ trái sang phải.',
                        'Tính được biểu thức có hai dấu phép tính cộng, trừ theo thứ tự từ phải sang trái.',
                        'Đảo ngược vế của quy tắc: Tính được biểu thức có hai dấu phép tính cộng, trừ theo '
                        'thứ tự từ trái sang phải.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tính được biểu thức có hai dấu '
                        'phép tính cộng, trừ theo thứ tự từ trái sang phải.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm '
                        'vi 10: Tính được biểu thức có hai dấu phép tính cộng, trừ theo thứ tự từ trái sang '
                        'phải.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Kết quả của phép tính $6 + 4 - 5$ bằng $5$.”',
            'answer': True,
            'solution': 'Tính từ trái sang phải: $6 + 4 = 10$, rồi $10 - 5 = 5$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi 10**, quy tắc **Hai '
                 'dấu phép tính** được xác định bởi Tính lần lượt từ trái sang phải và khi áp dụng cho ví dụ '
                 '“Tính: $10 - 4 - 3 = ?$” ta có lời giải: Tính từ trái sang phải: $10 - 4 = 6$, rồi lấy $6 '
                 '- 3 = 3$. Vậy $10 - 4 - 3 = 3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Hai dấu phép tính** (Tính lần lượt từ '
                        'trái sang phải) và lời giải ví dụ minh họa của Bài 13: Luyện tập chung về phép '
                        'cộng, phép trừ trong phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 13: Luyện tập chung về phép cộng, phép trừ trong '
                 'phạm vi 10** để giải bài toán sau: Tính: $10 - 4 - 3 = ?$ Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Tính từ trái sang phải: $10 + 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = 3$.',
                        'Tính từ trái sang phải: $10 - 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = 3$.',
                        'Tính từ trái sang phải: $10 - 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = 2$.',
                        'Tính từ trái sang phải: $20 - 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = 3$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 13: Luyện tập chung về phép cộng, phép trừ trong phạm vi '
                        '10: Tính từ trái sang phải: $10 - 4 = 6$, rồi lấy $6 - 3 = 3$. Vậy $10 - 4 - 3 = '
                        '3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lan có $2$ cái kẹo. Mẹ cho Lan thêm một số kẹo nữa thì Lan có tất cả $9$ cái kẹo. Hỏi mẹ '
                 'đã cho Lan mấy cái kẹo?',
            'answer': ['7'],
            'unit': None,
            'solution': 'Số kẹo mẹ cho thêm là: $9 - 2 = 7$ (cái kẹo).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd04-hinh-khoi-vi-tri',
  'context_title': 'Chủ đề 4: Làm quen với một số hình khối',
  'context': 'SGK Toán 1 · Chủ đề 4: Khối lập phương, khối hộp chữ nhật; vị trí và định hướng trong không '
             'gian.',
  'title': 'Bài 14: Khối lập phương, khối hộp chữ nhật',
  'icon': '🧊',
  'description': 'Nhận dạng khối lập phương, khối hộp chữ nhật thông qua đồ vật thật và mô hình.',
  'requirements': ['Nhận dạng được khối lập phương và khối hộp chữ nhật.',
                   'Biết đặc điểm các mặt của khối lập phương (đều là hình vuông) và khối hộp chữ nhật (các '
                   'mặt là hình chữ nhật).',
                   'Kể tên được các đồ vật thực tế có dạng khối lập phương, khối hộp chữ nhật.'],
  'definition': '- **Khối lập phương:** là hình khối có $6$ mặt đều là **hình vuông** bằng nhau (ví dụ: con '
                'xúc xắc, khối rubik).\n'
                '- **Khối hộp chữ nhật:** là hình khối có $6$ mặt là **hình chữ nhật** (có thể có $2$ mặt là '
                'hình vuông), ví dụ: hộp sữa giấy, viên gạch, hộp bút.',
  'theory': '- **Phân biệt hình phẳng và hình khối:** Hình vuông, hình chữ nhật là hình phẳng vẽ trên mặt '
            'giấy; còn khối lập phương, khối hộp chữ nhật là hình khối có thể cầm nắm và xếp chồng lên nhau '
            'được.\n'
            '- Vì các mặt đều phẳng nên cả khối lập phương và khối hộp chữ nhật đều đặt đứng vững, dễ xếp '
            'chồng thành tháp, tường nhà.',
  'formulas': [{'category': 'Đặc điểm nhận dạng hình khối',
                'items': [{'name': 'Khối lập phương',
                           'formula': 'Có $6$ mặt đều là hình vuông',
                           'note': 'Ví dụ: con xúc xắc, khối rubik.'},
                          {'name': 'Khối hộp chữ nhật',
                           'formula': 'Có $6$ mặt là hình chữ nhật',
                           'note': 'Ví dụ: viên gạch, hộp sữa giấy, bao diêm.'}]}],
  'example': 'Trong các đồ vật: con xúc xắc, hộp sữa tươi, chiếc đĩa tròn, đồ vật nào có dạng khối lập '
             'phương? Đồ vật nào có dạng khối hộp chữ nhật?',
  'example_answer': 'Con xúc xắc có dạng **khối lập phương**; hộp sữa tươi có dạng **khối hộp chữ nhật**.',
  'real_life': 'Xếp các hộp quà, thùng carton, gạch xây nhà hoặc lắp ráp đồ chơi hình khối.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Con xúc xắc có dạng hình khối gì?',
            'options': ['Khối lập phương', 'Khối hộp chữ nhật', 'Hình tròn', 'Hình tam giác'],
            'answer': 0,
            'solution': 'Con xúc xắc có $6$ mặt đều là hình vuông nên có dạng khối lập phương.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Mỗi mặt của khối lập phương là hình gì?',
            'options': ['Hình tròn', 'Hình vuông', 'Hình tam giác', 'Hình chữ nhật dài'],
            'answer': 1,
            'solution': 'Tất cả $6$ mặt của khối lập phương đều là hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 14: Khối lập phương, khối hộp chữ nhật**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Khối lập phương**?',
            'options': ['Có $7$ mặt đều là hình vuông',
                        'Có $5$ mặt đều là hình vuông',
                        'Có $6$ mặt đều là hình vuông',
                        'Có $12$ mặt đều là hình vuông'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 14: Khối lập phương, khối hộp chữ nhật, **Khối lập '
                        'phương** được xác định bởi: Có $6$ mặt đều là hình vuông. (Ví dụ: con xúc xắc, khối '
                        'rubik.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 14: Khối lập phương, khối hộp chữ nhật**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Khối hộp chữ nhật**?',
            'options': ['Có $7$ mặt là hình chữ nhật',
                        'Có $5$ mặt là hình chữ nhật',
                        'Có $12$ mặt là hình chữ nhật',
                        'Có $6$ mặt là hình chữ nhật'],
            'answer': 3,
            'solution': 'Trong Bài 14: Khối lập phương, khối hộp chữ nhật, **Khối hộp chữ nhật** có công '
                        'thức/quy tắc là: Có $6$ mặt là hình chữ nhật.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Viên gạch xây nhà hoặc hộp sữa giấy thường có dạng hình gì?',
            'options': ['Khối hộp chữ nhật', 'Khối lập phương', 'Hình vuông', 'Hình tròn'],
            'answer': 0,
            'solution': 'Viên gạch và hộp sữa giấy là hình khối có các mặt là hình chữ nhật nên có dạng khối '
                        'hộp chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 14: Khối lập phương, khối hộp chữ nhật**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Nhận dạng được khối lập phương và khối hộp chữ nhật. (với dấu ngược lại)',
                        'Nhận dạng được khối lập phương và khối hộp chữ nhật.',
                        'Đảo ngược vế của quy tắc: Nhận dạng được khối lập phương và khối hộp chữ nhật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận dạng được khối lập phương '
                        'và khối hộp chữ nhật.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 14: Khối lập phương, khối hộp chữ nhật: Nhận dạng '
                        'được khối lập phương và khối hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Khối lập phương có các mặt là hình vuông nên khối lập phương chính là hình '
                 'vuông.”',
            'answer': False,
            'solution': 'Hình vuông là hình phẳng, còn khối lập phương là hình khối trong không gian có các '
                        'mặt là hình vuông. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 14: Khối lập phương, khối hộp chữ nhật**, quy tắc **Khối lập phương** được xác '
                 'định bởi Có $6$ mặt đều là hình vuông và khi áp dụng cho ví dụ “Trong các đồ vật: con xúc '
                 'xắc, hộp sữa tươi, chiếc đĩa tròn, đồ vật nào có dạng khối lập phương? Đồ vật nào có dạng '
                 'khối hộp chữ nhật?” ta có lời giải: Con xúc xắc có dạng **khối lập phương**; hộp sữa tươi '
                 'có dạng **khối hộp chữ nhật**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Khối lập phương** (Có $6$ mặt đều là '
                        'hình vuông) và lời giải ví dụ minh họa của Bài 14: Khối lập phương, khối hộp chữ '
                        'nhật.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 14: Khối lập phương, khối hộp chữ nhật** để giải '
                 'bài toán sau: Trong các đồ vật: con xúc xắc, hộp sữa tươi, chiếc đĩa tròn, đồ vật nào có '
                 'dạng khối lập phương? Đồ vật nào có dạng khối hộp chữ nhật? Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Con xúc xắc có dạng **khối lập phương**; hộp sữa tươi có dạng **khối hộp chữ '
                        'nhật**.',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 14: Khối lập phương, khối hộp chữ nhật: Con xúc xắc có '
                        'dạng **khối lập phương**; hộp sữa tươi có dạng **khối hộp chữ nhật**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một khối lập phương có tất cả bao nhiêu mặt là hình vuông?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Khối lập phương (như con xúc xắc có các mặt từ $1$ chấm đến $6$ chấm) có tất cả $6$ '
                        'mặt là hình vuông.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd04-hinh-khoi-vi-tri',
  'context_title': 'Chủ đề 4: Làm quen với một số hình khối',
  'context': 'SGK Toán 1 · Chủ đề 4: Khối lập phương, khối hộp chữ nhật; vị trí và định hướng trong không '
             'gian.',
  'title': 'Bài 15: Vị trí, định hướng trong không gian',
  'icon': '🧭',
  'description': 'Nhận biết và mô tả vị trí: trên – dưới, trước – sau, phải – trái, ở giữa.',
  'requirements': ['Nhận biết và sử dụng đúng các từ chỉ vị trí: trên – dưới, trước – sau, bên phải – bên '
                   'trái, ở giữa.',
                   'Xác định được vị trí tương đối giữa các đồ vật hoặc con người trong tranh và trong thực '
                   'tế.',
                   'Vận dụng kiến thức của **Bài 15: Vị trí, định hướng trong không gian** để giải bài tập '
                   'minh họa và bài toán thực tiễn.'],
  'definition': 'Các cặp từ dùng để chỉ vị trí trong không gian:\n'
                '- **Trên – dưới** (theo chiều thẳng đứng).\n'
                '- **Trước – sau** (theo hướng nhìn hoặc hướng xếp hàng).\n'
                '- **Bên phải – bên trái** (xác định theo tay phải, tay trái).\n'
                '- **Ở giữa** (nằm xen giữa hai vật ở hai bên).',
  'theory': '- Nếu vật A ở **trên** vật B thì vật B ở **dưới** vật A.\n'
            '- Nếu bạn A đứng **trước** bạn B thì bạn B đứng **sau** bạn A.\n'
            '- Khi ba vật xếp theo thứ tự A – B – C trên một hàng thì vật B nằm **ở giữa** A và C, vật A ở '
            'bên trái B, vật C ở bên phải B.',
  'formulas': [{'category': 'Các mối quan hệ vị trí',
                'items': [{'name': 'Trên – Dưới', 'formula': 'A ở trên B $\\Leftrightarrow$ B ở dưới A'},
                          {'name': 'Trước – Sau',
                           'formula': 'A đứng trước B $\\Leftrightarrow$ B đứng sau A'},
                          {'name': 'Ở giữa', 'formula': 'Trong hàng A – B – C thì B đứng ở giữa A và C'}]}],
  'example': 'Trên bàn học, từ trái sang phải có: hộp bút, quyển vở, bình nước. Đồ vật nào ở giữa? Đồ vật '
             'nào ở bên phải quyển vở?',
  'example_answer': '**Quyển vở** nằm ở giữa hộp bút và bình nước. **Bình nước** nằm ở bên phải quyển vở.',
  'real_life': 'Đi đường đúng lề bên phải, sắp xếp sách vở ngăn trên – ngăn dưới, xếp hàng vào lớp.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Quyển sách đặt ở trên mặt bàn. Khi đó mặt bàn ở vị trí nào so với quyển sách?',
            'options': ['Ở trên', 'Ở dưới', 'Ở bên trái', 'Ở giữa'],
            'answer': 1,
            'solution': 'Quyển sách ở trên mặt bàn thì mặt bàn ở dưới quyển sách.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Ba bạn xếp hàng dọc: An đứng đầu hàng, Bình đứng sau An, Chi đứng sau Bình. Bạn nào đứng ở '
                 'giữa?',
            'options': ['An', 'Chi', 'Bình', 'Không có ai'],
            'answer': 2,
            'solution': 'Thứ tự hàng là An – Bình – Chi nên bạn đứng ở giữa là Bình.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 15: Vị trí, định hướng trong không gian**, quy tắc hoặc công thức nào sau đây '
                 'xác định đúng **Trên – Dưới**?',
            'options': ['A ở trên B $\\Leftrightarrow$ B ở dưới A (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: A ở trên B $\\Leftrightarrow$ B ở dưới A',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của A ở trên B $\\Leftrightarrow$ B '
                        'ở dưới A',
                        'A ở trên B $\\Leftrightarrow$ B ở dưới A'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 15: Vị trí, định hướng trong không gian, **Trên – '
                        'Dưới** được xác định bởi: A ở trên B $\\Leftrightarrow$ B ở dưới A.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 15: Vị trí, định hướng trong không gian**, biểu thức hoặc quy tắc nào dưới '
                 'đây biểu diễn đúng **Trước – Sau**?',
            'options': ['A đứng trước B $\\Leftrightarrow$ B đứng sau A',
                        'A đứng trước B $\\Leftrightarrow$ B đứng sau A (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: A đứng trước B $\\Leftrightarrow$ B đứng sau A',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của A đứng trước B '
                        '$\\Leftrightarrow$ B đứng sau A'],
            'answer': 0,
            'solution': 'Trong Bài 15: Vị trí, định hướng trong không gian, **Trước – Sau** có công thức/quy '
                        'tắc là: A đứng trước B $\\Leftrightarrow$ B đứng sau A.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trên kệ đồ chơi, từ trái sang phải có: quả bóng, con gấu bông, chiếc ô tô. Đồ vật ở bên '
                 'phải con gấu bông là:',
            'options': ['Quả bóng', 'Chiếc ô tô', 'Con gấu bông', 'Không có đồ vật nào'],
            'answer': 1,
            'solution': 'Từ trái sang phải là: quả bóng – con gấu bông – chiếc ô tô. Vậy bên phải con gấu '
                        'bông là chiếc ô tô.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 15: Vị trí, định hướng trong không gian**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Nhận biết và sử dụng đúng các từ chỉ vị trí: trên – dưới, trước – sau, bên phải – '
                        'bên trái, ở giữa. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết và sử dụng đúng các từ chỉ vị trí: trên – dưới, '
                        'trước – sau, bên phải – bên trái, ở giữa.',
                        'Nhận biết và sử dụng đúng các từ chỉ vị trí: trên – dưới, trước – sau, bên phải – '
                        'bên trái, ở giữa.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết và sử dụng đúng các '
                        'từ chỉ vị trí: trên – dưới, trước – sau, bên phải – bên trái, ở giữa.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 15: Vị trí, định hướng trong không gian: Nhận biết và '
                        'sử dụng đúng các từ chỉ vị trí: trên – dưới, trước – sau, bên phải – bên trái, ở '
                        'giữa.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Con mèo nằm dưới gầm bàn, lọ hoa đặt trên mặt bàn. Nhận định: “Lọ hoa ở dưới con mèo.”',
            'answer': False,
            'solution': 'Lọ hoa trên mặt bàn còn con mèo dưới gầm bàn nên lọ hoa ở trên con mèo. Nhận định '
                        'Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 15: Vị trí, định hướng trong không gian**, quy tắc **Trên – Dưới** được xác '
                 'định bởi A ở trên B $\\Leftrightarrow$ B ở dưới A và khi áp dụng cho ví dụ “Trên bàn học, '
                 'từ trái sang phải có: hộp bút, quyển vở, bình nước. Đồ vật nào ở giữa? Đồ vật nào ở bên '
                 'phải quyển vở?” ta có lời giải: **Quyển vở** nằm ở giữa hộp bút và bình nước. **Bình '
                 'nước** nằm ở bên phải quyển vở.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Trên – Dưới** (A ở trên B '
                        '$\\Leftrightarrow$ B ở dưới A) và lời giải ví dụ minh họa của Bài 15: Vị trí, định '
                        'hướng trong không gian.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 15: Vị trí, định hướng trong không gian** để giải '
                 'bài toán sau: Trên bàn học, từ trái sang phải có: hộp bút, quyển vở, bình nước. Đồ vật nào '
                 'ở giữa? Đồ vật nào ở bên phải quyển vở? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        '**Quyển vở** nằm ở giữa hộp bút và bình nước. **Bình nước** nằm ở bên phải quyển '
                        'vở.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 15: Vị trí, định hướng trong không gian: **Quyển vở** '
                        'nằm ở giữa hộp bút và bình nước. **Bình nước** nằm ở bên phải quyển vở.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong một hàng dọc có $3$ bạn: bạn Nam đứng đầu hàng, bạn Mai đứng ở giữa, bạn Việt đứng '
                 'cuối hàng. Hỏi có mấy bạn đứng trước bạn Việt?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Thứ tự là Nam – Mai – Việt nên đứng trước bạn Việt có $2$ bạn là Nam và Mai.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd04-hinh-khoi-vi-tri',
  'context_title': 'Chủ đề 4: Làm quen với một số hình khối',
  'context': 'SGK Toán 1 · Chủ đề 4: Khối lập phương, khối hộp chữ nhật; vị trí và định hướng trong không '
             'gian.',
  'title': 'Bài 16: Luyện tập chung về hình khối và vị trí',
  'icon': '🏗️',
  'description': 'Thực hành đếm số khối lập phương, khối hộp chữ nhật trong hình ghép và xác định vị trí đồ '
                 'vật.',
  'requirements': ['Đếm đúng số khối lập phương, khối hộp chữ nhật trong các hình xếp tầng.',
                   'Kết hợp nhận dạng hình khối với xác định vị trí trên – dưới, trái – phải, ở giữa.',
                   'Vận dụng kiến thức của **Bài 16: Luyện tập chung về hình khối và vị trí** để giải bài '
                   'tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi đếm số hình khối được xếp thành nhiều tầng (như bậc thang, cái tháp), ta đếm số khối ở '
                '**từng tầng** (hoặc từng cột) rồi cộng lại để không bỏ sót các khối nằm khuất ở tầng dưới.',
  'theory': '- Ví dụ: Một cái tháp có tầng dưới gồm $3$ khối lập phương, tầng trên đặt $1$ khối lập phương '
            'lên giữa. Tổng số khối lập phương là $3 + 1 = 4$ khối.\n'
            '- Khi ghép $2$ khối lập phương bằng nhau đặt sát cạnh nhau (hoặc chồng lên nhau), ta được một '
            'hình có dạng **khối hộp chữ nhật**.',
  'formulas': [{'category': 'Phương pháp đếm khối và ghép khối',
                'items': [{'name': 'Đếm theo tầng',
                           'formula': 'Tổng số khối = Số khối tầng dưới $+$ Số khối tầng giữa $+$ Số khối '
                                      'tầng trên'},
                          {'name': 'Ghép 2 khối lập phương',
                           'formula': '$2$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 1$ khối hộp '
                                      'chữ nhật'}]}],
  'example': 'Bạn Việt xếp các khối lập phương thành một cái tháp: tầng dưới cùng có $3$ khối, tầng giữa có '
             '$2$ khối, tầng trên cùng có $1$ khối. Cái tháp có tất cả bao nhiêu khối lập phương?',
  'example_answer': 'Tổng số khối lập phương là: $3 + 2 + 1 = 6$ (khối lập phương).',
  'real_life': 'Đếm số thùng hàng xếp trong kho, lắp ghép mô hình bằng gạch đồ chơi Lego.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Ghép $2$ khối lập phương bằng nhau đặt chồng khít lên nhau thì tạo thành một khối có dạng '
                 'gì?',
            'options': ['Hình tròn', 'Hình tam giác', 'Khối hộp chữ nhật', 'Vẫn là khối lập phương'],
            'answer': 2,
            'solution': 'Khi chồng $2$ khối lập phương bằng nhau lên nhau, chiều cao tăng gấp đôi nên tạo '
                        'thành khối hộp chữ nhật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Một bậc thang đồ chơi có cột bên trái gồm $1$ khối lập phương, cột bên phải gồm $2$ khối '
                 'lập phương. Có tất cả mấy khối lập phương?',
            'options': ['$2$', '$4$', '$1$', '$3$'],
            'answer': 3,
            'solution': 'Ta có $1 + 2 = 3$ (khối lập phương).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 16: Luyện tập chung về hình khối và vị trí**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Đếm theo tầng**?',
            'options': ['Tổng số khối = Số khối tầng dưới $+$ Số khối tầng giữa $+$ Số khối tầng trên',
                        'Tổng số khối = Số khối tầng dưới $+$ Số khối tầng giữa $+$ Số khối tầng trên (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Tổng số khối = Số khối tầng dưới $+$ Số khối tầng giữa '
                        '$+$ Số khối tầng trên',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Tổng số khối = Số khối tầng '
                        'dưới $+$ Số khối tầng giữa $+$ Số khối tầng trên'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 16: Luyện tập chung về hình khối và vị trí, **Đếm '
                        'theo tầng** được xác định bởi: Tổng số khối = Số khối tầng dưới $+$ Số khối tầng '
                        'giữa $+$ Số khối tầng trên.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 16: Luyện tập chung về hình khối và vị trí**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Ghép 2 khối lập phương**?',
            'options': ['$3$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 1$ khối hộp chữ nhật',
                        '$2$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 1$ khối hộp chữ nhật',
                        '$2$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 2$ khối hộp chữ nhật',
                        '$4$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 1$ khối hộp chữ nhật'],
            'answer': 1,
            'solution': 'Trong Bài 16: Luyện tập chung về hình khối và vị trí, **Ghép 2 khối lập phương** có '
                        'công thức/quy tắc là: $2$ khối lập phương bằng nhau ghép sát nhau $\\rightarrow 1$ '
                        'khối hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Xếp $3$ khối hộp chữ nhật chồng lên nhau: khối màu đỏ ở dưới cùng, khối màu vàng ở giữa, '
                 'khối màu xanh ở trên cùng. Khối nào nằm ngay trên khối màu vàng?',
            'options': ['Khối màu đỏ', 'Khối màu vàng', 'Khối màu xanh', 'Không có khối nào'],
            'answer': 2,
            'solution': 'Vì khối vàng ở giữa và khối xanh ở trên cùng nên khối màu xanh nằm ngay trên khối '
                        'màu vàng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 16: Luyện tập chung về hình khối và vị trí**, nhận định nào '
                 'sau đây là **chính xác**?',
            'options': ['Đếm đúng số khối lập phương, khối hộp chữ nhật trong các hình xếp tầng. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Đếm đúng số khối lập phương, khối hộp chữ nhật trong các '
                        'hình xếp tầng.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đếm đúng số khối lập phương, '
                        'khối hộp chữ nhật trong các hình xếp tầng.',
                        'Đếm đúng số khối lập phương, khối hộp chữ nhật trong các hình xếp tầng.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 16: Luyện tập chung về hình khối và vị trí: Đếm đúng '
                        'số khối lập phương, khối hộp chữ nhật trong các hình xếp tầng.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu tầng dưới có $4$ khối lập phương và tầng trên có $2$ khối lập phương thì '
                 'cả hình có $6$ khối lập phương.”',
            'answer': True,
            'solution': 'Ta có $4 + 2 = 6$ khối lập phương. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 16: Luyện tập chung về hình khối và vị trí**, quy tắc **Đếm theo tầng** được '
                 'xác định bởi Tổng số khối = Số khối tầng dưới $+$ Số khối tầng giữa $+$ Số khối tầng trên '
                 'và khi áp dụng cho ví dụ “Bạn Việt xếp các khối lập phương thành một cái tháp: tầng dưới '
                 'cùng có $3$ khối, tầng giữa có $2$ khối, tầng trên cùng có $1$ khối. Cái...” ta có lời '
                 'giải: Tổng số khối lập phương là: $3 + 2 + 1 = 6$ (khối lập phương).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đếm theo tầng** (Tổng số khối = Số khối '
                        'tầng dưới $+$ Số khối tầng giữa $+$ Số khối tầng trên) và lời giải ví dụ minh họa '
                        'của Bài 16: Luyện tập chung về hình khối và vị trí.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 16: Luyện tập chung về hình khối và vị trí** để '
                 'giải bài toán sau: Bạn Việt xếp các khối lập phương thành một cái tháp: tầng dưới cùng có '
                 '$3$ khối, tầng giữa có $2$ khối, tầng trên cùng có $1$ khối. Cái tháp có tất cả bao nhiêu '
                 'khối lập phương? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Tổng số khối lập phương là: $3 + 2 + 1 = 6$ (khối lập phương).',
                        'Tổng số khối lập phương là: $3 - 2 + 1 = 6$ (khối lập phương).',
                        'Tổng số khối lập phương là: $3 + 2 + 1 = 5$ (khối lập phương).',
                        'Tổng số khối lập phương là: $6 + 2 + 1 = 6$ (khối lập phương).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 16: Luyện tập chung về hình khối và vị trí: Tổng số khối '
                        'lập phương là: $3 + 2 + 1 = 6$ (khối lập phương).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Giá sách có $3$ ngăn: ngăn trên cùng có $4$ quyển truyện, ngăn ở giữa có $3$ quyển, ngăn '
                 'dưới cùng có $2$ quyển. Hỏi ngăn ở giữa và ngăn dưới cùng có tất cả bao nhiêu quyển '
                 'truyện?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Ngăn ở giữa ($3$ quyển) cộng ngăn dưới cùng ($2$ quyển) là: $3 + 2 = 5$ (quyển '
                        'truyện).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd05-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 5: Ôn tập học kì 1',
  'context': 'SGK Toán 1 · Chủ đề 5: Ôn tập các số, phép cộng, phép trừ trong phạm vi 10 và hình học.',
  'title': 'Bài 17: Ôn tập các số trong phạm vi 10',
  'icon': '📝',
  'description': 'Hệ thống lại kỹ năng đếm, đọc, viết, so sánh, sắp xếp và cấu tạo các số từ 0 đến 10.',
  'requirements': ['Đếm, đọc, viết thành thạo các số từ $0$ đến $10$.',
                   'So sánh, xếp thứ tự các số từ bé đến lớn và từ lớn đến bé.',
                   'Nắm vững cấu tạo số (mấy và mấy) trong phạm vi $10$.'],
  'definition': 'Dãy số tự nhiên từ $0$ đến $10$ theo thứ tự tăng dần là: $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '
                '10$. Số đứng trước luôn bé hơn số đứng sau.',
  'theory': '- **So sánh và sắp xếp:** Muốn xếp theo thứ tự từ bé đến lớn, ta tìm số bé nhất viết trước rồi '
            'tăng dần; ngược lại từ lớn đến bé thì viết số lớn nhất trước.\n'
            '- **Tìm số theo điều kiện:** Ví dụ các số lớn hơn $6$ và bé hơn $10$ là $7, 8, 9$.\n'
            '- **Cấu tạo số:** Nếu $a$ gồm $b$ và $c$ thì $b + c = a$.',
  'formulas': [{'category': 'Hệ thống kiến thức số từ 0 đến 10',
                'items': [{'name': 'Thứ tự tăng dần',
                           'formula': '$0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$'},
                          {'name': 'Thứ tự giảm dần',
                           'formula': '$10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0$'}]}],
  'example': 'Cho các số $3, 8, 6, 5$. Hãy tìm số lớn nhất, số bé nhất và xếp các số theo thứ tự từ lớn đến '
             'bé.',
  'example_answer': 'Số lớn nhất là $8$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 3$.',
  'real_life': 'Đọc số tầng thang máy, xếp thứ tự danh sách học sinh, kiểm đếm đồ dùng học tập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số lớn nhất trong các số $3, 8, 6, 5$ là:',
            'options': ['$3$', '$6$', '$5$', '$8$'],
            'answer': 3,
            'solution': 'Vì $3 < 5 < 6 < 8$ nên số lớn nhất là $8$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số $7$ gồm $4$ và mấy?',
            'options': ['$3$', '$2$', '$4$', '$5$'],
            'answer': 0,
            'solution': 'Vì $4 + 3 = 7$ nên $7$ gồm $4$ và $3$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 17: Ôn tập các số trong phạm vi 10**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Thứ tự tăng dần**?',
            'options': ['$0 > 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$',
                        '$0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$',
                        '$0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 9$',
                        '$2 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 17: Ôn tập các số trong phạm vi 10, **Thứ tự tăng '
                        'dần** được xác định bởi: $0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 17: Ôn tập các số trong phạm vi 10**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Thứ tự giảm dần**?',
            'options': ['$10 < 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0$',
                        '$10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 1$',
                        '$10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0$',
                        '$20 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0$'],
            'answer': 2,
            'solution': 'Trong Bài 17: Ôn tập các số trong phạm vi 10, **Thứ tự giảm dần** có công thức/quy '
                        'tắc là: $10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Có bao nhiêu số lớn hơn $5$ nhưng bé hơn $9$?',
            'options': ['$2$ số', '$4$ số', '$1$ số', '$3$ số'],
            'answer': 3,
            'solution': 'Các số lớn hơn $5$ và bé hơn $9$ là $6, 7, 8$. Vậy có $3$ số.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 17: Ôn tập các số trong phạm vi 10**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Đếm, đọc, viết thành thạo các số từ $0$ đến $10$.',
                        'Đếm, đọc, viết thành thạo các số từ $1$ đến $10$.',
                        'Đếm, đọc, viết thành thạo các số từ $0$ đến $9$.',
                        'Đếm, đọc, viết thành thạo các số từ $2$ đến $10$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 17: Ôn tập các số trong phạm vi 10: Đếm, đọc, viết '
                        'thành thạo các số từ $0$ đến $10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Các số $9, 4, 7, 1$ được viết theo thứ tự từ lớn đến bé.”',
            'answer': False,
            'solution': 'Vì $4 < 7$ nên thứ tự từ lớn đến bé đúng phải là $9, 7, 4, 1$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 17: Ôn tập các số trong phạm vi 10**, quy tắc **Thứ tự tăng dần** được xác '
                 'định bởi $0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10$ và khi áp dụng cho ví dụ “Cho các số '
                 '$3, 8, 6, 5$. Hãy tìm số lớn nhất, số bé nhất và xếp các số theo thứ tự từ lớn đến bé.” ta '
                 'có lời giải: Số lớn nhất là $8$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, '
                 '3$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Thứ tự tăng dần** ($0 < 1 < 2 < 3 < 4 < '
                        '5 < 6 < 7 < 8 < 9 < 10$) và lời giải ví dụ minh họa của Bài 17: Ôn tập các số trong '
                        'phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 17: Ôn tập các số trong phạm vi 10** để giải bài '
                 'toán sau: Cho các số $3, 8, 6, 5$. Hãy tìm số lớn nhất, số bé nhất và xếp các số theo thứ '
                 'tự từ lớn đến bé. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Số lớn nhất là $9$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 3$.',
                        'Số lớn nhất là $8$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 3$.',
                        'Số lớn nhất là $8$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 2$.',
                        'Số lớn nhất là $16$, số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 3$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 17: Ôn tập các số trong phạm vi 10: Số lớn nhất là $8$, '
                        'số bé nhất là $3$. Thứ tự từ lớn đến bé là: $8, 6, 5, 3$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số chẵn lớn nhất có một chữ số là số nào?',
            'answer': ['8'],
            'unit': None,
            'solution': 'Các số có một chữ số là từ $0$ đến $9$. Trong các số $0, 2, 4, 6, 8$ thì số lớn '
                        'nhất là $8$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd05-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 5: Ôn tập học kì 1',
  'context': 'SGK Toán 1 · Chủ đề 5: Ôn tập các số, phép cộng, phép trừ trong phạm vi 10 và hình học.',
  'title': 'Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10',
  'icon': '➕',
  'description': 'Củng cố tính nhẩm bảng cộng, bảng trừ, tính biểu thức hai dấu phép tính và giải toán trong '
                 'phạm vi 10.',
  'requirements': ['Tính nhẩm nhanh các phép cộng, phép trừ trong phạm vi $10$.',
                   'Thực hiện thành thạo dãy tính có hai dấu phép tính cộng, trừ.',
                   'Giải được bài toán thực tế có một hoặc hai bước tính đơn giản trong phạm vi $10$.'],
  'definition': '- Khi đổi chỗ các số trong phép cộng thì kết quả không đổi: $a + b = b + a$.\n'
                '- Từ một phép cộng $a + b = c$, ta viết được hai phép trừ: $c - a = b$ và $c - b = a$.',
  'theory': '- **Tính chất số $0$:** $a + 0 = 0 + a = a$; $a - 0 = a$; $a - a = 0$.\n'
            '- **Hai dấu phép tính:** Luôn thực hiện từ trái sang phải. Ví dụ: $5 - 2 + 3 = 3 + 3 = 6$.\n'
            '- **So sánh biểu thức:** Tính giá trị của từng vế rồi so sánh hai số vừa tìm được.',
  'formulas': [{'category': 'Các quy tắc tính nhẩm trọng tâm',
                'items': [{'name': 'Số 0 trong cộng, trừ',
                           'formula': '$a + 0 = a;\\ a - 0 = a;\\ a - a = 0$'},
                          {'name': 'Liên hệ Cộng – Trừ',
                           'formula': '$a + b = c \\Rightarrow c - a = b$ và $c - b = a$'},
                          {'name': 'Dãy tính 2 bước',
                           'formula': 'Tính lần lượt từ trái sang phải',
                           'note': 'Ví dụ: $10 - 3 - 4 = 7 - 4 = 3$.'}]}],
  'example': 'Điền dấu $>, <, =$ thích hợp vào chỗ chấm: $4 + 3 \\dots 9 - 2$.',
  'example_answer': 'Ta có $4 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 - '
                    '2$.',
  'real_life': 'Tính số bút chì, số quyển vở sau khi cho bạn mượn và được mẹ mua thêm.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $10 - 4$ là:',
            'options': ['$6$', '$5$', '$7$', '$4$'],
            'answer': 0,
            'solution': 'Vì $4 + 6 = 10$ nên $10 - 4 = 6$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bé nhất?',
            'options': ['$2 + 5$', '$10 - 6$', '$9 - 1$', '$4 + 4$'],
            'answer': 1,
            'solution': 'Tính từng phép tính: $2 + 5 = 7$; $9 - 1 = 8$; $4 + 4 = 8$; $10 - 6 = 4$. Bé nhất '
                        'là $4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Số 0 trong cộng, trừ**?',
            'options': ['$a - 0 = a;\\ a - 0 = a;\\ a - a = 0$',
                        '$a + 0 = a;\\ a - 0 = a;\\ a - a = 1$',
                        '$a + 0 = a;\\ a - 0 = a;\\ a - a = 0$',
                        '$a + 2 = a;\\ a - 0 = a;\\ a - a = 0$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10, '
                        '**Số 0 trong cộng, trừ** được xác định bởi: $a + 0 = a;\\ a - 0 = a;\\ a - a = 0$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Liên hệ Cộng – Trừ**?',
            'options': ['$a - b = c \\Rightarrow c - a = b$ và $c - b = a$',
                        'Đảo ngược vế của quy tắc: $a + b = c \\Rightarrow c - a = b$ và $c - b = a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a + b = c \\Rightarrow c - a = '
                        'b$ và $c - b = a$',
                        '$a + b = c \\Rightarrow c - a = b$ và $c - b = a$'],
            'answer': 3,
            'solution': 'Trong Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10, **Liên hệ Cộng – Trừ** '
                        'có công thức/quy tắc là: $a + b = c \\Rightarrow c - a = b$ và $c - b = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Hà có $5$ bút chì. Hà cho em $2$ bút chì, sau đó mẹ mua thêm cho Hà $3$ bút chì. Hỏi lúc '
                 'này Hà có mấy bút chì?',
            'options': ['$6$ bút chì', '$10$ bút chì', '$4$ bút chì', '$5$ bút chì'],
            'answer': 0,
            'solution': 'Ta có phép tính: $5 - 2 + 3 = 3 + 3 = 6$ (bút chì).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Tính nhẩm nhanh các phép cộng, phép trừ trong phạm vi $11$.',
                        'Tính nhẩm nhanh các phép cộng, phép trừ trong phạm vi $10$.',
                        'Tính nhẩm nhanh các phép cộng, phép trừ trong phạm vi $9$.',
                        'Tính nhẩm nhanh các phép cộng, phép trừ trong phạm vi $20$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10: Tính '
                        'nhẩm nhanh các phép cộng, phép trừ trong phạm vi $10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Kết quả của phép tính $5 + 4$ lớn hơn $10$.”',
            'answer': False,
            'solution': 'Ta có $5 + 4 = 9$, mà $9 < 10$ nên kết quả bé hơn $10$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10**, quy tắc **Số 0 trong cộng, '
                 'trừ** được xác định bởi $a + 0 = a;\\ a - 0 = a;\\ a - a = 0$ và khi áp dụng cho ví dụ '
                 '“Điền dấu $>, <, =$ thích hợp vào chỗ chấm: $4 + 3 \\dots 9 - 2$.” ta có lời giải: Ta có '
                 '$4 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 - 2$.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số 0 trong cộng, trừ** ($a + 0 = a;\\ a '
                        '- 0 = a;\\ a - a = 0$) và lời giải ví dụ minh họa của Bài 18: Ôn tập phép cộng, '
                        'phép trừ trong phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10** '
                 'để giải bài toán sau: Điền dấu $>, <, =$ thích hợp vào chỗ chấm: $4 + 3 \\dots 9 - 2$. '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $4 - 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 '
                        '- 2$.',
                        'Ta có $4 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 '
                        '- 1$.',
                        'Ta có $4 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 '
                        '- 2$.',
                        'Ta có $8 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 '
                        '- 2$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 18: Ôn tập phép cộng, phép trừ trong phạm vi 10: Ta có '
                        '$4 + 3 = 7$ và $9 - 2 = 7$. Vì $7 = 7$ nên ta điền dấu $=$, tức là $4 + 3 = 9 - '
                        '2$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong vườn có $10$ cây ăn quả gồm cây cam và cây bưởi, trong đó có $6$ cây cam. Hỏi trong '
                 'vườn có mấy cây bưởi?',
            'answer': ['4'],
            'unit': None,
            'solution': 'Số cây bưởi trong vườn là: $10 - 6 = 4$ (cây).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd05-on-tap-hoc-ki-1',
  'context_title': 'Chủ đề 5: Ôn tập học kì 1',
  'context': 'SGK Toán 1 · Chủ đề 5: Ôn tập các số, phép cộng, phép trừ trong phạm vi 10 và hình học.',
  'title': 'Bài 19: Ôn tập hình học và Ôn tập chung học kì 1',
  'icon': '🏆',
  'description': 'Ôn tập nhận dạng hình phẳng, hình khối, vị trí trong không gian và giải bài toán tổng hợp '
                 'học kì 1.',
  'requirements': ['Phân biệt rõ các hình phẳng (vuông, tròn, tam giác, chữ nhật) và các hình khối (khối lập '
                   'phương, khối hộp chữ nhật).',
                   'Đếm đúng số hình phẳng, hình khối trong các mô hình lắp ghép.',
                   'Vận dụng tổng hợp kiến thức số học và hình học để giải quyết tình huống thực tế.'],
  'definition': '- **Hình phẳng:** Hình vuông ($4$ cạnh bằng nhau), hình chữ nhật ($4$ cạnh), hình tam giác '
                '($3$ cạnh), hình tròn (đường cong kín).\n'
                '- **Hình khối:** Khối lập phương ($6$ mặt đều là hình vuông), khối hộp chữ nhật ($6$ mặt là '
                'hình chữ nhật).',
  'theory': '- Khi đếm số hình tam giác hoặc hình vuông trên hình vẽ có đường kẻ chia nhỏ, cần đếm các '
            '**hình đơn** trước rồi đếm các **hình ghép** từ $2$ hình nhỏ trở lên.\n'
            '- Ví dụ: Một hình vuông được kẻ $1$ đường chéo nối hai góc đối diện sẽ tạo ra $2$ hình tam giác '
            'bên trong $1$ hình vuông.',
  'formulas': [{'category': 'Tổng hợp hình học học kì 1',
                'items': [{'name': 'Số cạnh hình phẳng',
                           'formula': 'Tam giác: $3$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: '
                                      '$0$ cạnh thẳng'},
                          {'name': 'Đếm hình có ghép',
                           'formula': 'Tổng số hình = Số hình đơn $+$ Số hình ghép từ $2$ phần trở lên'}]}],
  'example': 'Một tờ bìa hình chữ nhật được cắt bởi $1$ đường chéo nối hai góc đối diện. Hỏi thu được mấy '
             'hình tam giác?',
  'example_answer': 'Đường chéo chia tờ bìa hình chữ nhật thành $2$ mảnh, mỗi mảnh có $3$ cạnh nên thu được '
                    '$2$ hình tam giác.',
  'real_life': 'Nhận dạng hình học trong kiến trúc nhà cửa, đồ chơi lắp ghép và kiểm tra tổng kết cuối học '
               'kì 1.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Hình nào có $4$ cạnh dài bằng nhau?',
            'options': ['Hình tròn', 'Hình vuông', 'Hình tam giác', 'Hình chữ nhật dài'],
            'answer': 1,
            'solution': 'Hình vuông có $4$ cạnh thẳng dài bằng nhau.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đồ vật nào dưới đây có dạng khối hộp chữ nhật?',
            'options': ['Quả bóng bàn', 'Chiếc đĩa tròn', 'Hộp sữa giấy', 'Khăn tay vuông'],
            'answer': 2,
            'solution': 'Hộp sữa giấy là hình khối có các mặt là hình chữ nhật nên có dạng khối hộp chữ '
                        'nhật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 19: Ôn tập hình học và Ôn tập chung học kì 1**, quy tắc hoặc công thức nào sau '
                 'đây xác định đúng **Số cạnh hình phẳng**?',
            'options': ['Tam giác: $4$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $0$ cạnh thẳng',
                        'Tam giác: $3$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $1$ cạnh thẳng',
                        'Tam giác: $6$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $0$ cạnh thẳng',
                        'Tam giác: $3$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $0$ cạnh thẳng'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 19: Ôn tập hình học và Ôn tập chung học kì 1, **Số '
                        'cạnh hình phẳng** được xác định bởi: Tam giác: $3$ cạnh; Hình vuông, Hình chữ nhật: '
                        '$4$ cạnh; Hình tròn: $0$ cạnh thẳng.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 19: Ôn tập hình học và Ôn tập chung học kì 1**, biểu thức hoặc quy tắc nào '
                 'dưới đây biểu diễn đúng **Đếm hình có ghép**?',
            'options': ['Tổng số hình = Số hình đơn $+$ Số hình ghép từ $2$ phần trở lên',
                        'Tổng số hình = Số hình đơn $+$ Số hình ghép từ $3$ phần trở lên',
                        'Tổng số hình = Số hình đơn $+$ Số hình ghép từ $1$ phần trở lên',
                        'Tổng số hình = Số hình đơn $+$ Số hình ghép từ $4$ phần trở lên'],
            'answer': 0,
            'solution': 'Trong Bài 19: Ôn tập hình học và Ôn tập chung học kì 1, **Đếm hình có ghép** có '
                        'công thức/quy tắc là: Tổng số hình = Số hình đơn $+$ Số hình ghép từ $2$ phần trở '
                        'lên.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Ghép $2$ hình tam giác vuông cân bằng nhau theo cạnh dài nhất thì tạo thành được $1$ hình '
                 'vuông. Nếu có $6$ hình tam giác như thế thì ghép được mấy hình vuông rời nhau?',
            'options': ['$2$ hình vuông', '$3$ hình vuông', '$4$ hình vuông', '$6$ hình vuông'],
            'answer': 1,
            'solution': 'Cứ $2$ hình tam giác ghép được $1$ hình vuông. Có $6$ hình tam giác ($2 + 2 + 2 = '
                        '6$) nên ghép được $3$ hình vuông.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 19: Ôn tập hình học và Ôn tập chung học kì 1**, nhận định '
                 'nào sau đây là **chính xác**?',
            'options': ['Phân biệt rõ các hình phẳng (vuông, tròn, tam giác, chữ nhật) và các hình khối '
                        '(khối lập phương, khối hộp chữ nhật). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Phân biệt rõ các hình phẳng (vuông, tròn, tam giác, chữ '
                        'nhật) và các hình khối (khối lập phương, khối hộp chữ nhật).',
                        'Phân biệt rõ các hình phẳng (vuông, tròn, tam giác, chữ nhật) và các hình khối '
                        '(khối lập phương, khối hộp chữ nhật).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Phân biệt rõ các hình phẳng '
                        '(vuông, tròn, tam giác, chữ nhật) và các hình khối (khối lập phương, khối hộp chữ '
                        'nhật).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 19: Ôn tập hình học và Ôn tập chung học kì 1: Phân '
                        'biệt rõ các hình phẳng (vuông, tròn, tam giác, chữ nhật) và các hình khối (khối lập '
                        'phương, khối hộp chữ nhật).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Mọi mặt của khối lập phương đều là hình vuông.”',
            'answer': True,
            'solution': 'Khối lập phương có $6$ mặt và tất cả các mặt đều là hình vuông. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 19: Ôn tập hình học và Ôn tập chung học kì 1**, quy tắc **Số cạnh hình phẳng** '
                 'được xác định bởi Tam giác: $3$ cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $0$ '
                 'cạnh thẳng và khi áp dụng cho ví dụ “Một tờ bìa hình chữ nhật được cắt bởi $1$ đường chéo '
                 'nối hai góc đối diện. Hỏi thu được mấy hình tam giác?” ta có lời giải: Đường chéo chia tờ '
                 'bìa hình chữ nhật thành $2$ mảnh, mỗi mảnh có $3$ cạnh nên thu được $2$ hình tam giác.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số cạnh hình phẳng** (Tam giác: $3$ '
                        'cạnh; Hình vuông, Hình chữ nhật: $4$ cạnh; Hình tròn: $0$ cạnh thẳng) và lời giải '
                        'ví dụ minh họa của Bài 19: Ôn tập hình học và Ôn tập chung học kì 1.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 19: Ôn tập hình học và Ôn tập chung học kì 1** để '
                 'giải bài toán sau: Một tờ bìa hình chữ nhật được cắt bởi $1$ đường chéo nối hai góc đối '
                 'diện. Hỏi thu được mấy hình tam giác? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Đường chéo chia tờ bìa hình chữ nhật thành $3$ mảnh, mỗi mảnh có $3$ cạnh nên thu '
                        'được $2$ hình tam giác.',
                        'Đường chéo chia tờ bìa hình chữ nhật thành $2$ mảnh, mỗi mảnh có $3$ cạnh nên thu '
                        'được $1$ hình tam giác.',
                        'Đường chéo chia tờ bìa hình chữ nhật thành $4$ mảnh, mỗi mảnh có $3$ cạnh nên thu '
                        'được $2$ hình tam giác.',
                        'Đường chéo chia tờ bìa hình chữ nhật thành $2$ mảnh, mỗi mảnh có $3$ cạnh nên thu '
                        'được $2$ hình tam giác.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 19: Ôn tập hình học và Ôn tập chung học kì 1: Đường chéo '
                        'chia tờ bìa hình chữ nhật thành $2$ mảnh, mỗi mảnh có $3$ cạnh nên thu được $2$ '
                        'hình tam giác.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một hình vuông lớn được kẻ một đường thẳng nối hai góc đối diện (chia đôi hình vuông). Hỏi '
                 'trên hình vẽ có tất cả bao nhiêu hình tam giác?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Đường chéo chia hình vuông thành $2$ hình tam giác.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd06-cac-so-den-100',
  'context_title': 'Chủ đề 6: Các số đến 100',
  'context': 'SGK Toán 1 · Chủ đề 6: Số có hai chữ số, chục và đơn vị, so sánh số, bảng các số từ 1 đến 100.',
  'title': 'Bài 21: Số có hai chữ số',
  'icon': '💯',
  'description': 'Nhận biết chục và đơn vị, số tròn chục; đếm, đọc, viết các số có hai chữ số đến 99.',
  'requirements': ['Nhận biết $10$ đơn vị bằng $1$ chục; nhận biết các số tròn chục ($10, 20, \\dots, 90$).',
                   'Đếm, đọc, viết được các số từ $11$ đến $99$.',
                   'Nêu được cấu tạo của số có hai chữ số gồm mấy chục và mấy đơn vị.'],
  'definition': '- **$10$ đơn vị $= 1$ chục.**\n'
                '- **Số có hai chữ số** gồm chữ số **hàng chục** viết ở bên trái và chữ số **hàng đơn vị** '
                'viết ở bên phải. Ví dụ: Số $36$ gồm $3$ chục và $6$ đơn vị.',
  'theory': '- **Các số từ $11$ đến $19$:** gồm $1$ chục và $1, 2, \\dots, 9$ đơn vị. Đọc là: mười một '
            '($11$), mười hai ($12$), ..., mười lăm ($15$), ..., mười chín ($19$).\n'
            '- **Các số tròn chục:** $10, 20, 30, 40, 50, 60, 70, 80, 90$ đều có chữ số hàng đơn vị là $0$.\n'
            '- **Lưu ý cách đọc số từ $20$ đến $99$:**\n'
            '  + Hàng đơn vị là $1$ (từ $21$ trở đi) đọc là **mốt**: $21$ đọc là hai mươi mốt.\n'
            '  + Hàng đơn vị là $4$ (từ $24$ trở đi) đọc là **tư** (hoặc bốn): $34$ đọc là ba mươi tư.\n'
            '  + Hàng đơn vị là $5$ (từ $15$ trở đi) đọc là **lăm**: $75$ đọc là bảy mươi lăm.',
  'formulas': [{'category': 'Cấu tạo và cách đọc số có hai chữ số',
                'items': [{'name': 'Quy đổi chục – đơn vị', 'formula': '$1$ chục $= 10$ đơn vị'},
                          {'name': 'Cấu tạo số',
                           'formula': 'Số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 0$)',
                           'note': 'Ví dụ: $45$ gồm $4$ chục và $5$ đơn vị.'},
                          {'name': 'Các số tròn chục',
                           'formula': '$10, 20, 30, 40, 50, 60, 70, 80, 90$',
                           'note': 'Chữ số hàng đơn vị bằng $0$.'}]}],
  'example': 'Viết số gồm $6$ chục và $2$ đơn vị, rồi nêu cách đọc số đó.',
  'example_answer': 'Số gồm $6$ chục và $2$ đơn vị viết là $62$, đọc là **sáu mươi hai**.',
  'real_life': 'Đếm trứng theo vỉ $10$ quả ($1$ chục), đếm đũa theo bó $1$ chục chiếc, đọc số nhà và số '
               'trang sách.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số gồm $3$ chục và $6$ đơn vị được viết là:',
            'options': ['$63$', '$306$', '$36$', '$9$'],
            'answer': 2,
            'solution': 'Chữ số hàng chục là $3$ viết bên trái, chữ số hàng đơn vị là $6$ viết bên phải, ta '
                        'được số $36$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số “bảy mươi lăm” được viết là:',
            'options': ['$705$', '$57$', '$7$', '$75$'],
            'answer': 3,
            'solution': 'Bảy mươi là $7$ chục, lăm là $5$ đơn vị, viết là $75$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 21: Số có hai chữ số**, quy tắc hoặc công thức nào sau đây xác định đúng **Quy '
                 'đổi chục – đơn vị**?',
            'options': ['$1$ chục $= 10$ đơn vị',
                        '$2$ chục $= 10$ đơn vị',
                        '$1$ chục $= 9$ đơn vị',
                        'Số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 0$)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 21: Số có hai chữ số, **Quy đổi chục – đơn vị** '
                        'được xác định bởi: $1$ chục $= 10$ đơn vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 21: Số có hai chữ số**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Cấu tạo số**?',
            'options': ['Số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 1$)',
                        'Số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 0$)',
                        'Số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 2$)',
                        '$1$ chục $= 10$ đơn vị'],
            'answer': 1,
            'solution': 'Trong Bài 21: Số có hai chữ số, **Cấu tạo số** có công thức/quy tắc là: Số '
                        '$\\overline{ab}$ gồm $a$ chục và $b$ đơn vị ($a \\neq 0$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Trong các số $45, 60, 61, 9$, số nào là số tròn chục?',
            'options': ['$45$', '$61$', '$60$', '$9$'],
            'answer': 2,
            'solution': 'Số tròn chục là số có hai chữ số và chữ số hàng đơn vị bằng $0$, đó là số $60$ ($6$ '
                        'chục).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 21: Số có hai chữ số**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Nhận biết $11$ đơn vị bằng $1$ chục; nhận biết các số tròn chục ($10, 20, \\dots, '
                        '90$).',
                        'Nhận biết $10$ đơn vị bằng $1$ chục; nhận biết các số tròn chục ($10, 20, \\dots, '
                        '89$).',
                        'Nhận biết $20$ đơn vị bằng $1$ chục; nhận biết các số tròn chục ($10, 20, \\dots, '
                        '90$).',
                        'Nhận biết $10$ đơn vị bằng $1$ chục; nhận biết các số tròn chục ($10, 20, \\dots, '
                        '90$).'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 21: Số có hai chữ số: Nhận biết $10$ đơn vị bằng $1$ '
                        'chục; nhận biết các số tròn chục ($10, 20, \\dots, 90$).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $15$ đọc là mười lăm và gồm $1$ chục và $5$ đơn vị.”',
            'answer': True,
            'solution': 'Số $15$ có chữ số hàng chục là $1$, hàng đơn vị là $5$ và đọc là mười lăm. Nhận '
                        'định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 21: Số có hai chữ số**, quy tắc **Quy đổi chục – đơn vị** được xác định bởi '
                 '$1$ chục $= 10$ đơn vị và khi áp dụng cho ví dụ “Viết số gồm $6$ chục và $2$ đơn vị, rồi '
                 'nêu cách đọc số đó.” ta có lời giải: Số gồm $6$ chục và $2$ đơn vị viết là $62$, đọc là '
                 '**sáu mươi hai**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Quy đổi chục – đơn vị** ($1$ chục $= 10$ '
                        'đơn vị) và lời giải ví dụ minh họa của Bài 21: Số có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 21: Số có hai chữ số** để giải bài toán sau: Viết '
                 'số gồm $6$ chục và $2$ đơn vị, rồi nêu cách đọc số đó. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Số gồm $6$ chục và $2$ đơn vị viết là $62$, đọc là **sáu mươi hai**.',
                        'Số gồm $7$ chục và $2$ đơn vị viết là $62$, đọc là **sáu mươi hai**.',
                        'Số gồm $6$ chục và $2$ đơn vị viết là $61$, đọc là **sáu mươi hai**.',
                        'Số gồm $12$ chục và $2$ đơn vị viết là $62$, đọc là **sáu mươi hai**.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 21: Số có hai chữ số: Số gồm $6$ chục và $2$ đơn vị viết '
                        'là $62$, đọc là **sáu mươi hai**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mẹ mua $5$ bó đũa, mỗi bó có $1$ chục chiếc đũa. Hỏi mẹ đã mua tất cả bao nhiêu chiếc đũa?',
            'answer': ['50'],
            'unit': None,
            'solution': 'Mỗi bó có $1$ chục chiếc, $5$ bó có $5$ chục chiếc đũa. Mà $5$ chục $= 50$ nên mẹ '
                        'mua $50$ chiếc đũa.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd06-cac-so-den-100',
  'context_title': 'Chủ đề 6: Các số đến 100',
  'context': 'SGK Toán 1 · Chủ đề 6: Số có hai chữ số, chục và đơn vị, so sánh số, bảng các số từ 1 đến 100.',
  'title': 'Bài 22: So sánh số có hai chữ số',
  'icon': '⚖️',
  'description': 'Quy tắc so sánh hai số có hai chữ số theo hàng chục và hàng đơn vị.',
  'requirements': ['Biết so sánh hai số có hai chữ số bằng cách so sánh chữ số hàng chục trước, hàng đơn vị '
                   'sau.',
                   'Sắp xếp được nhóm không quá $4$ số trong phạm vi $100$ theo thứ tự từ bé đến lớn hoặc từ '
                   'lớn đến bé.',
                   'Vận dụng kiến thức của **Bài 22: So sánh số có hai chữ số** để giải bài tập minh họa và '
                   'bài toán thực tiễn.'],
  'definition': 'Khi so sánh hai số có hai chữ số:\n'
                '- **Bước 1:** So sánh chữ số **hàng chục** trước. Số nào có chữ số hàng chục lớn hơn thì số '
                'đó lớn hơn.\n'
                '- **Bước 2:** Nếu chữ số hàng chục bằng nhau thì so sánh chữ số **hàng đơn vị**. Số nào có '
                'chữ số hàng đơn vị lớn hơn thì lớn hơn.',
  'theory': '- Ví dụ 1: So sánh $58$ và $85$. Hàng chục có $5 < 8$ nên $58 < 85$.\n'
            '- Ví dụ 2: So sánh $47$ và $43$. Hai số có cùng $4$ chục; xét hàng đơn vị có $7 > 3$ nên $47 > '
            '43$.\n'
            '- Nếu cả chữ số hàng chục và chữ số hàng đơn vị đều giống nhau thì hai số bằng nhau ($64 = '
            '64$).\n'
            '- Mọi số có một chữ số ($0$ đến $9$) đều bé hơn mọi số có hai chữ số ($10$ đến $99$).',
  'formulas': [{'category': 'Quy tắc so sánh hai số có hai chữ số',
                'items': [{'name': 'Khác chữ số hàng chục',
                           'formula': 'Hàng chục lớn hơn $\\rightarrow$ số đó lớn hơn',
                           'note': 'Ví dụ: $62 > 49$ vì $6 > 4$.'},
                          {'name': 'Cùng chữ số hàng chục',
                           'formula': 'So sánh tiếp chữ số hàng đơn vị',
                           'note': 'Ví dụ: $73 < 78$ vì cùng $7$ chục và $3 < 8$.'}]}],
  'example': 'Xếp các số $47, 74, 40, 70$ theo thứ tự từ bé đến lớn.',
  'example_answer': 'Nhóm có $4$ chục gồm $40 < 47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ chục '
                    'nên thứ tự từ bé đến lớn là: $40, 47, 70, 74$.',
  'real_life': 'So sánh số tuổi của các thành viên trong gia đình, so sánh giá tiền hoặc điểm số.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Dấu thích hợp điền vào chỗ chấm $58 \\dots 85$ là:',
            'options': ['$>$', '$=$', '$+$', '$<$'],
            'answer': 3,
            'solution': 'So sánh chữ số hàng chục: $5 < 8$ nên $58 < 85$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong các số $52, 25, 50, 20$, số bé nhất là:',
            'options': ['$20$', '$52$', '$25$', '$50$'],
            'answer': 0,
            'solution': 'Hai số có hàng chục bé hơn là $25$ và $20$. Vì $0 < 5$ nên $20 < 25$. Vậy số bé '
                        'nhất là $20$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 22: So sánh số có hai chữ số**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Khác chữ số hàng chục**?',
            'options': ['Hàng chục bé hơn $\\rightarrow$ số đó lớn hơn',
                        'Hàng chục lớn hơn $\\rightarrow$ số đó lớn hơn',
                        'Đảo ngược vế của quy tắc: Hàng chục lớn hơn $\\rightarrow$ số đó lớn hơn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Hàng chục lớn hơn '
                        '$\\rightarrow$ số đó lớn hơn'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 22: So sánh số có hai chữ số, **Khác chữ số hàng '
                        'chục** được xác định bởi: Hàng chục lớn hơn $\\rightarrow$ số đó lớn hơn. (Ví dụ: '
                        '$62 > 49$ vì $6 > 4$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 22: So sánh số có hai chữ số**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Cùng chữ số hàng chục**?',
            'options': ['So sánh tiếp chữ số hàng đơn vị (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: So sánh tiếp chữ số hàng đơn vị',
                        'So sánh tiếp chữ số hàng đơn vị',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của So sánh tiếp chữ số hàng đơn '
                        'vị'],
            'answer': 2,
            'solution': 'Trong Bài 22: So sánh số có hai chữ số, **Cùng chữ số hàng chục** có công thức/quy '
                        'tắc là: So sánh tiếp chữ số hàng đơn vị.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Các số $47, 74, 40, 70$ xếp theo thứ tự từ bé đến lớn là:',
            'options': ['$47, 40, 70, 74$', '$40, 70, 47, 74$', '$74, 70, 47, 40$', '$40, 47, 70, 74$'],
            'answer': 3,
            'solution': 'So sánh ta có $40 < 47 < 70 < 74$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 22: So sánh số có hai chữ số**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Biết so sánh hai số có hai chữ số bằng cách so sánh chữ số hàng chục trước, hàng '
                        'đơn vị sau.',
                        'Biết so sánh hai số có hai chữ số bằng cách so sánh chữ số hàng chục trước, hàng '
                        'đơn vị sau. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Biết so sánh hai số có hai chữ số bằng cách so sánh chữ '
                        'số hàng chục trước, hàng đơn vị sau.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Biết so sánh hai số có hai chữ '
                        'số bằng cách so sánh chữ số hàng chục trước, hàng đơn vị sau.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 22: So sánh số có hai chữ số: Biết so sánh hai số có '
                        'hai chữ số bằng cách so sánh chữ số hàng chục trước, hàng đơn vị sau.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $69$ lớn hơn số $71$ vì $9 > 1$.”',
            'answer': False,
            'solution': 'Khi so sánh phải xét hàng chục trước: $6$ chục $< 7$ chục nên $69 < 71$. Nhận định '
                        'Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 22: So sánh số có hai chữ số**, quy tắc **Khác chữ số hàng chục** được xác '
                 'định bởi Hàng chục lớn hơn $\\rightarrow$ số đó lớn hơn và khi áp dụng cho ví dụ “Xếp các '
                 'số $47, 74, 40, 70$ theo thứ tự từ bé đến lớn.” ta có lời giải: Nhóm có $4$ chục gồm $40 < '
                 '47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ chục nên thứ tự từ bé đến lớn là: '
                 '$40, 47, 70, 74$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Khác chữ số hàng chục** (Hàng chục lớn '
                        'hơn $\\rightarrow$ số đó lớn hơn) và lời giải ví dụ minh họa của Bài 22: So sánh số '
                        'có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 22: So sánh số có hai chữ số** để giải bài toán '
                 'sau: Xếp các số $47, 74, 40, 70$ theo thứ tự từ bé đến lớn. Cách giải và kết quả nào dưới '
                 'đây là **đúng**?',
            'options': ['Nhóm có $4$ chục gồm $40 > 47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ '
                        'chục nên thứ tự từ bé đến lớn là: $40, 47, 70, 74$.',
                        'Nhóm có $4$ chục gồm $40 < 47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ '
                        'chục nên thứ tự từ bé đến lớn là: $40, 47, 70, 74$.',
                        'Nhóm có $4$ chục gồm $40 < 47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ '
                        'chục nên thứ tự từ bé đến lớn là: $40, 47, 70, 73$.',
                        'Nhóm có $8$ chục gồm $40 < 47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ '
                        'chục nên thứ tự từ bé đến lớn là: $40, 47, 70, 74$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 22: So sánh số có hai chữ số: Nhóm có $4$ chục gồm $40 < '
                        '47$; nhóm có $7$ chục gồm $70 < 74$. Vì $4$ chục $< 7$ chục nên thứ tự từ bé đến '
                        'lớn là: $40, 47, 70, 74$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong các số $38, 83, 79, 80$, số lớn nhất là số nào?',
            'answer': ['83'],
            'unit': None,
            'solution': 'Hai số có hàng chục lớn nhất ($8$ chục) là $83$ và $80$. Vì $83 > 80$ nên số lớn '
                        'nhất là $83$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd06-cac-so-den-100',
  'context_title': 'Chủ đề 6: Các số đến 100',
  'context': 'SGK Toán 1 · Chủ đề 6: Số có hai chữ số, chục và đơn vị, so sánh số, bảng các số từ 1 đến 100.',
  'title': 'Bài 23: Bảng các số từ 1 đến 100',
  'icon': '📅',
  'description': 'Khám phá quy luật bảng các số từ 1 đến 100, làm quen số 100 và tìm số liền trước, số liền '
                 'sau.',
  'requirements': ['Nhận biết số $100$ (một trăm) là số liền sau của $99$ và $100 = 10$ chục.',
                   'Sử dụng bảng các số từ $1$ đến $100$ để tìm số liền trước, số liền sau và nhận biết quy '
                   'luật theo hàng, theo cột.',
                   'Vận dụng cấu tạo số để giải các bài toán lập số trong phạm vi $100$.'],
  'definition': '- **Số $100$** (đọc là **một trăm**) là số đứng liền sau số $99$. Ta có $10$ chục $= 100$.\n'
                '- **Bảng các số từ $1$ đến $100$** gồm $10$ hàng và $10$ cột.',
  'theory': '- **Quy luật trong bảng các số từ $1$ đến $100$:**\n'
            '  + Trong cùng một hàng (từ trái sang phải): hai số cạnh nhau hơn kém nhau $1$ đơn vị.\n'
            '  + Trong cùng một cột (từ trên xuống dưới): số ở ô ngay bên dưới lớn hơn số ở ô ngay bên trên '
            '$10$ đơn vị ($1$ chục).\n'
            '  + Cột cuối cùng bên phải gồm các số tròn chục: $10, 20, 30, 40, 50, 60, 70, 80, 90$ và số '
            '$100$.\n'
            '- **Số lớn nhất có một chữ số** là $9$; **số bé nhất có hai chữ số** là $10$; **số lớn nhất có '
            'hai chữ số** là $99$.',
  'formulas': [{'category': 'Quy luật bảng các số từ 1 đến 100',
                'items': [{'name': 'Đi sang phải 1 ô',
                           'formula': 'Số tăng thêm $1$ đơn vị (số liền sau)',
                           'note': 'Ví dụ: liền sau $39$ là $40$.'},
                          {'name': 'Đi xuống dưới 1 ô',
                           'formula': 'Số tăng thêm $10$ đơn vị ($1$ chục)',
                           'note': 'Ví dụ: ngay dưới $34$ là $44$.'},
                          {'name': 'Các số đặc biệt',
                           'formula': 'Số bé nhất có $2$ chữ số là $10$; lớn nhất có $2$ chữ số là $99$'}]}],
  'example': 'Tìm số có hai chữ số, biết chữ số hàng chục là $6$ và chữ số hàng đơn vị bé hơn chữ số hàng '
             'chục $2$ đơn vị.',
  'example_answer': 'Chữ số hàng đơn vị là: $6 - 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.',
  'real_life': 'Tra cứu số ghế trong rạp chiếu phim, tìm trang sách, kiểm đếm đủ $100$ món đồ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền sau của số $39$ là số nào?',
            'options': ['$40$', '$38$', '$49$', '$30$'],
            'answer': 0,
            'solution': 'Đếm thêm $1$ sau $39$ ta được $40$. Vậy số liền sau của $39$ là $40$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Số liền sau của số $99$ là số nào?',
            'options': ['$98$', '$100$', '$90$', '$10$'],
            'answer': 1,
            'solution': 'Đếm tiếp sau $99$ là $100$ (một trăm).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 23: Bảng các số từ 1 đến 100**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Đi sang phải 1 ô**?',
            'options': ['Số tăng thêm $2$ đơn vị (số liền sau)',
                        'Số tăng thêm $10$ đơn vị ($1$ chục)',
                        'Số tăng thêm $1$ đơn vị (số liền sau)',
                        'Số bé nhất có $2$ chữ số là $10$; lớn nhất có $2$ chữ số là $99$'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 23: Bảng các số từ 1 đến 100, **Đi sang phải 1 ô** '
                        'được xác định bởi: Số tăng thêm $1$ đơn vị (số liền sau). (Ví dụ: liền sau $39$ là '
                        '$40$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 23: Bảng các số từ 1 đến 100**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Đi xuống dưới 1 ô**?',
            'options': ['Số tăng thêm $11$ đơn vị ($1$ chục)',
                        'Số tăng thêm $10$ đơn vị ($2$ chục)',
                        'Số tăng thêm $20$ đơn vị ($1$ chục)',
                        'Số tăng thêm $10$ đơn vị ($1$ chục)'],
            'answer': 3,
            'solution': 'Trong Bài 23: Bảng các số từ 1 đến 100, **Đi xuống dưới 1 ô** có công thức/quy tắc '
                        'là: Số tăng thêm $10$ đơn vị ($1$ chục).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số nào dưới đây lớn hơn $68$ và bé hơn $71$?',
            'options': ['$69$', '$67$', '$72$', '$61$'],
            'answer': 0,
            'solution': 'Các số tự nhiên lớn hơn $68$ và bé hơn $71$ là $69$ và $70$. Trong các phương án có '
                        'số $69$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 23: Bảng các số từ 1 đến 100**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết số $110$ (một trăm) là số liền sau của $99$ và $100 = 10$ chục.',
                        'Nhận biết số $100$ (một trăm) là số liền sau của $99$ và $100 = 10$ chục.',
                        'Nhận biết số $100$ (một trăm) là số liền sau của $99$ và $100 = 9$ chục.',
                        'Nhận biết số $102$ (một trăm) là số liền sau của $99$ và $100 = 10$ chục.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 23: Bảng các số từ 1 đến 100: Nhận biết số $100$ (một '
                        'trăm) là số liền sau của $99$ và $100 = 10$ chục.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Trong bảng các số từ $1$ đến $100$, số nằm ở ô ngay bên dưới số $34$ (cùng '
                 'cột) là số $35$.”',
            'answer': False,
            'solution': 'Đi xuống dưới $1$ ô trong cùng cột thì số tăng thêm $10$ đơn vị, nên ô ngay dưới số '
                        '$34$ là $44$ (còn $35$ nằm bên phải $34$). Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 23: Bảng các số từ 1 đến 100**, quy tắc **Đi sang phải 1 ô** được xác định bởi '
                 'Số tăng thêm $1$ đơn vị (số liền sau) và khi áp dụng cho ví dụ “Tìm số có hai chữ số, biết '
                 'chữ số hàng chục là $6$ và chữ số hàng đơn vị bé hơn chữ số hàng chục $2$ đơn vị.” ta có '
                 'lời giải: Chữ số hàng đơn vị là: $6 - 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đi sang phải 1 ô** (Số tăng thêm $1$ đơn '
                        'vị (số liền sau)) và lời giải ví dụ minh họa của Bài 23: Bảng các số từ 1 đến 100.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 23: Bảng các số từ 1 đến 100** để giải bài toán '
                 'sau: Tìm số có hai chữ số, biết chữ số hàng chục là $6$ và chữ số hàng đơn vị bé hơn chữ '
                 'số hàng chục $2$ đơn vị. Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chữ số hàng đơn vị là: $6 + 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.',
                        'Chữ số hàng đơn vị là: $6 - 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $63$.',
                        'Chữ số hàng đơn vị là: $6 - 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.',
                        'Chữ số hàng đơn vị là: $12 - 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 23: Bảng các số từ 1 đến 100: Chữ số hàng đơn vị là: $6 '
                        '- 2 = 4$. Số gồm $6$ chục và $4$ đơn vị là $64$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Tìm số có hai chữ số, biết chữ số hàng chục là $6$ và chữ số hàng đơn vị bé hơn chữ số '
                 'hàng chục $2$ đơn vị.',
            'answer': ['64'],
            'unit': None,
            'solution': 'Chữ số hàng đơn vị là $6 - 2 = 4$. Số có $6$ chục và $4$ đơn vị là $64$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd07-do-dai',
  'context_title': 'Chủ đề 7: Độ dài và đo độ dài',
  'context': 'SGK Toán 1 · Chủ đề 7: Dài hơn – ngắn hơn, đơn vị xăng-ti-mét, thực hành ước lượng và đo độ '
             'dài.',
  'title': 'Bài 25: Dài hơn, ngắn hơn',
  'icon': '📏',
  'description': 'Nhận biết dài hơn, ngắn hơn, cao hơn, thấp hơn và đo độ dài bằng đơn vị tự quy ước.',
  'requirements': ['Biết cách so sánh trực tiếp độ dài hai vật để nhận ra vật nào dài hơn, ngắn hơn (hoặc '
                   'cao hơn, thấp hơn).',
                   'Tìm được vật dài nhất, vật ngắn nhất trong một nhóm đồ vật.',
                   'Biết đo độ dài bằng các đơn vị tự quy ước như gang tay, sải tay, bước chân, que tính.'],
  'definition': 'Muốn so sánh độ dài hai vật trực tiếp, ta đặt hai vật nằm dọc sát cạnh nhau sao cho **một '
                'đầu của hai vật bằng nhau** (thẳng hàng). Đầu còn lại của vật nào dài thò ra xa hơn thì vật '
                'đó **dài hơn**, vật kia **ngắn hơn**.',
  'theory': '- Khi so sánh chiều cao của hai người hoặc hai cái cây đứng trên cùng mặt đất, ta dùng từ **cao '
            'hơn – thấp hơn – cao bằng nhau**.\n'
            '- Khi chưa có thước kẻ, ta có thể ước lượng và đo độ dài bằng **gang tay**, **sải tay**, **bước '
            'chân** hoặc **que tính**.\n'
            '- Lưu ý: Gang tay của mỗi người dài ngắn khác nhau nên đo cùng một cái bàn có thể ra số gang '
            'tay khác nhau.',
  'formulas': [{'category': 'Quy tắc so sánh độ dài',
                'items': [{'name': 'So sánh trực tiếp',
                           'formula': 'Đặt một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn'},
                          {'name': 'Quan hệ ngược', 'formula': 'A dài hơn B $\\Leftrightarrow$ B ngắn hơn A'},
                          {'name': 'Đo bằng gang tay',
                           'formula': 'Gang tay càng ngắn thì số lần đo trên cùng một vật càng nhiều'}]}],
  'example': 'Bút chì đỏ dài hơn bút chì xanh, bút chì xanh dài hơn bút chì vàng. Hỏi bút chì nào dài nhất, '
             'bút chì nào ngắn nhất?',
  'example_answer': '**Bút chì đỏ** dài nhất và **bút chì vàng** ngắn nhất.',
  'real_life': 'So sánh chiều cao các bạn khi xếp hàng tập thể dục, chọn sợi dây dài hơn để buộc đồ.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Bút chì đỏ dài hơn bút chì xanh. Vậy bút chì xanh như thế nào so với bút chì đỏ?',
            'options': ['Dài hơn', 'Ngắn hơn', 'Dài bằng nhau', 'Cao hơn'],
            'answer': 1,
            'solution': 'Nếu bút chì đỏ dài hơn bút chì xanh thì bút chì xanh ngắn hơn bút chì đỏ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi so sánh chiều cao của hai bạn đứng trên sân phẳng, ta thường dùng cặp từ nào?',
            'options': ['Rộng hơn – hẹp hơn',
                        'Nặng hơn – nhẹ hơn',
                        'Cao hơn – thấp hơn',
                        'Nhiều hơn – ít hơn'],
            'answer': 2,
            'solution': 'Chiều cao của con người hay cây cối được so sánh bằng từ cao hơn – thấp hơn.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 25: Dài hơn, ngắn hơn**, quy tắc hoặc công thức nào sau đây xác định đúng **So '
                 'sánh trực tiếp**?',
            'options': ['Đặt một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Đặt một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn '
                        'là dài hơn',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt một đầu bằng nhau '
                        '$\\rightarrow$ đầu kia vươn xa hơn là dài hơn',
                        'Đặt một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 25: Dài hơn, ngắn hơn, **So sánh trực tiếp** được '
                        'xác định bởi: Đặt một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 25: Dài hơn, ngắn hơn**, biểu thức hoặc quy tắc nào dưới đây biểu diễn đúng '
                 '**Quan hệ ngược**?',
            'options': ['A dài hơn B $\\Leftrightarrow$ B ngắn hơn A',
                        'A dài hơn B $\\Leftrightarrow$ B ngắn hơn A (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: A dài hơn B $\\Leftrightarrow$ B ngắn hơn A',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của A dài hơn B $\\Leftrightarrow$ '
                        'B ngắn hơn A'],
            'answer': 0,
            'solution': 'Trong Bài 25: Dài hơn, ngắn hơn, **Quan hệ ngược** có công thức/quy tắc là: A dài '
                        'hơn B $\\Leftrightarrow$ B ngắn hơn A.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Thước kẻ dài $3$ que tính, hộp bút dài $2$ que tính, cái bàn dài $8$ que tính. Đồ vật nào '
                 'dài nhất?',
            'options': ['Thước kẻ', 'Cái bàn', 'Hộp bút', 'Ba vật bằng nhau'],
            'answer': 1,
            'solution': 'Vì $8 > 3 > 2$ nên cái bàn dài nhất ($8$ que tính).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 25: Dài hơn, ngắn hơn**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Biết cách so sánh trực tiếp độ dài hai vật để nhận ra vật nào dài hơn, ngắn hơn '
                        '(hoặc cao hơn, thấp hơn). (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Biết cách so sánh trực tiếp độ dài hai vật để nhận ra vật '
                        'nào dài hơn, ngắn hơn (hoặc cao hơn, thấp hơn).',
                        'Biết cách so sánh trực tiếp độ dài hai vật để nhận ra vật nào dài hơn, ngắn hơn '
                        '(hoặc cao hơn, thấp hơn).',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Biết cách so sánh trực tiếp độ '
                        'dài hai vật để nhận ra vật nào dài hơn, ngắn hơn (hoặc cao hơn, thấp hơn).'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 25: Dài hơn, ngắn hơn: Biết cách so sánh trực tiếp độ '
                        'dài hai vật để nhận ra vật nào dài hơn, ngắn hơn (hoặc cao hơn, thấp hơn).'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Mai và bố cùng đo chiều dài một cái bàn bằng gang tay: Mai đo được $6$ gang tay, bố đo '
                 'được $4$ gang tay. Nhận định: “Gang tay của Mai dài hơn gang tay của bố.”',
            'answer': False,
            'solution': 'Cùng một cái bàn, gang tay của Mai ngắn hơn nên phải đo nhiều lần hơn ($6 > 4$). '
                        'Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 25: Dài hơn, ngắn hơn**, quy tắc **So sánh trực tiếp** được xác định bởi Đặt '
                 'một đầu bằng nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn và khi áp dụng cho ví dụ '
                 '“Bút chì đỏ dài hơn bút chì xanh, bút chì xanh dài hơn bút chì vàng. Hỏi bút chì nào dài '
                 'nhất, bút chì nào ngắn nhất?” ta có lời giải: **Bút chì đỏ** dài nhất và **bút chì vàng** '
                 'ngắn nhất.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **So sánh trực tiếp** (Đặt một đầu bằng '
                        'nhau $\\rightarrow$ đầu kia vươn xa hơn là dài hơn) và lời giải ví dụ minh họa của '
                        'Bài 25: Dài hơn, ngắn hơn.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 25: Dài hơn, ngắn hơn** để giải bài toán sau: Bút '
                 'chì đỏ dài hơn bút chì xanh, bút chì xanh dài hơn bút chì vàng. Hỏi bút chì nào dài nhất, '
                 'bút chì nào ngắn nhất? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        '**Bút chì đỏ** dài nhất và **bút chì vàng** ngắn nhất.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 25: Dài hơn, ngắn hơn: **Bút chì đỏ** dài nhất và **bút '
                        'chì vàng** ngắn nhất.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cây thước dài bằng $3$ cái kẹp giấy, cây bút chì dài bằng $5$ cái kẹp giấy. Hỏi cây bút '
                 'chì dài hơn cây thước mấy cái kẹp giấy?',
            'answer': ['2'],
            'unit': None,
            'solution': 'Cây bút chì dài hơn cây thước là: $5 - 3 = 2$ (cái kẹp giấy).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd07-do-dai',
  'context_title': 'Chủ đề 7: Độ dài và đo độ dài',
  'context': 'SGK Toán 1 · Chủ đề 7: Dài hơn – ngắn hơn, đơn vị xăng-ti-mét, thực hành ước lượng và đo độ '
             'dài.',
  'title': 'Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)',
  'icon': '📐',
  'description': 'Nhận biết đơn vị xăng-ti-mét (cm) và cách dùng thước thẳng có vạch chia cm để đo độ dài.',
  'requirements': ['Nhận biết **xăng-ti-mét** là đơn vị đo độ dài chuẩn, viết tắt là $\\text{cm}$.',
                   'Đọc và viết đúng các số đo độ dài có đơn vị $\\text{cm}$.',
                   'Biết cách đặt thước thẳng có vạch chia $\\text{cm}$ để đo độ dài đoạn thẳng, đồ vật.'],
  'definition': '**Xăng-ti-mét** là một đơn vị đo độ dài, viết tắt là $\\text{cm}$. Trên thước kẻ học sinh, '
                'khoảng cách giữa hai vạch số liền nhau (như từ vạch $0$ đến vạch $1$) là $1\\text{ cm}$.',
  'theory': '- **Cách đọc, viết:** $1\\text{ cm}$ đọc là một xăng-ti-mét; $15\\text{ cm}$ đọc là mười lăm '
            'xăng-ti-mét.\n'
            '- **Ba bước đo độ dài bằng thước thẳng:**\n'
            '  + Bước 1: Đặt **vạch $0$** của thước trùng với một đầu của vật.\n'
            '  + Bước 2: Đặt mép thước sát và dọc theo chiều dài của vật.\n'
            '  + Bước 3: Nhìn đầu kia của vật trùng với vạch số mấy trên thước thì đọc số đo đó kèm theo đơn '
            'vị $\\text{cm}$.',
  'formulas': [{'category': 'Quy tắc đo độ dài với đơn vị cm',
                'items': [{'name': 'Ký hiệu đơn vị',
                           'formula': 'Xăng-ti-mét viết tắt là $\\text{cm}$',
                           'note': 'Ví dụ: $8\\text{ cm}$ đọc là tám xăng-ti-mét.'},
                          {'name': 'Đặt thước đúng',
                           'formula': 'Đầu vật trùng vạch $0$, đầu kia trùng vạch $a \\Rightarrow$ vật dài '
                                      '$a\\text{ cm}$'},
                          {'name': 'Đặt thước từ vạch khác 0',
                           'formula': 'Một đầu ở vạch $a$, đầu kia ở vạch $b$ ($b > a$) $\\Rightarrow$ dài '
                                      '$(b - a)\\text{ cm}$'}]}],
  'example': 'Một đầu chiếc tẩy đặt trùng với vạch $0$ của thước, đầu kia trùng với vạch số $4$. Hỏi chiếc '
             'tẩy dài bao nhiêu xăng-ti-mét?',
  'example_answer': 'Vì một đầu trùng vạch $0$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $4\\text{ cm}$.',
  'real_life': 'Dùng thước kẻ đo độ dài bút chì, cục tẩy, quyển vở trong cặp sách.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đơn vị đo độ dài “xăng-ti-mét” được viết tắt là:',
            'options': ['$\\text{m}$', '$\\text{kg}$', '$\\text{cm}$', '$\\text{xm}$'],
            'answer': 2,
            'solution': 'Xăng-ti-mét viết tắt là $\\text{cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đo độ dài bằng thước thẳng, ta cần đặt vạch nào của thước trùng với một đầu của vật?',
            'options': ['Vạch $1$', 'Vạch $10$', 'Vạch bất kỳ', 'Vạch $0$'],
            'answer': 3,
            'solution': 'Phải đặt vạch $0$ trùng với một đầu của vật thì vạch ở đầu kia mới chỉ đúng độ dài '
                        'của vật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Ký hiệu đơn vị**?',
            'options': ['Xăng-ti-mét viết tắt là $\\text{cm}$',
                        'Xăng-ti-mét viết tắt là $\\text{cm}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Xăng-ti-mét viết tắt là $\\text{cm}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Xăng-ti-mét viết tắt là '
                        '$\\text{cm}$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 26: Đơn vị đo độ dài (Xăng-ti-mét), **Ký hiệu đơn '
                        'vị** được xác định bởi: Xăng-ti-mét viết tắt là $\\text{cm}$. (Ví dụ: $8\\text{ '
                        'cm}$ đọc là tám xăng-ti-mét.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Đặt thước đúng**?',
            'options': ['Đầu vật trùng vạch $1$, đầu kia trùng vạch $a \\Rightarrow$ vật dài $a\\text{ cm}$',
                        'Đầu vật trùng vạch $0$, đầu kia trùng vạch $a \\Rightarrow$ vật dài $a\\text{ cm}$',
                        'Đầu vật trùng vạch $2$, đầu kia trùng vạch $a \\Rightarrow$ vật dài $a\\text{ cm}$',
                        'Xăng-ti-mét viết tắt là $\\text{cm}$'],
            'answer': 1,
            'solution': 'Trong Bài 26: Đơn vị đo độ dài (Xăng-ti-mét), **Đặt thước đúng** có công thức/quy '
                        'tắc là: Đầu vật trùng vạch $0$, đầu kia trùng vạch $a \\Rightarrow$ vật dài '
                        '$a\\text{ cm}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Số đo “$15\\text{ cm}$” được đọc là:',
            'options': ['Một năm xăng-ti-mét',
                        'Năm mươi mốt xăng-ti-mét',
                        'Mười lăm xăng-ti-mét',
                        'Mười năm xăng-ti-mét'],
            'answer': 2,
            'solution': '$15$ đọc là mười lăm, $\\text{cm}$ đọc là xăng-ti-mét.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)**, nhận định nào sau đây '
                 'là **chính xác**?',
            'options': ['Nhận biết **xăng-ti-mét** là đơn vị đo độ dài chuẩn, viết tắt là $\\text{cm}$. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận biết **xăng-ti-mét** là đơn vị đo độ dài chuẩn, viết '
                        'tắt là $\\text{cm}$.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận biết **xăng-ti-mét** là '
                        'đơn vị đo độ dài chuẩn, viết tắt là $\\text{cm}$.',
                        'Nhận biết **xăng-ti-mét** là đơn vị đo độ dài chuẩn, viết tắt là $\\text{cm}$.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 26: Đơn vị đo độ dài (Xăng-ti-mét): Nhận biết '
                        '**xăng-ti-mét** là đơn vị đo độ dài chuẩn, viết tắt là $\\text{cm}$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu đặt một đầu bút chì ở vạch $1$ và đầu kia ở vạch $8$ của thước thì bút chì '
                 'dài $8\\text{ cm}$.”',
            'answer': False,
            'solution': 'Vì đặt từ vạch $1$ đến vạch $8$ nên độ dài bút chì chỉ là $8 - 1 = 7\\text{ cm}$, '
                        'không phải $8\\text{ cm}$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)**, quy tắc **Ký hiệu đơn vị** được xác định '
                 'bởi Xăng-ti-mét viết tắt là $\\text{cm}$ và khi áp dụng cho ví dụ “Một đầu chiếc tẩy đặt '
                 'trùng với vạch $0$ của thước, đầu kia trùng với vạch số $4$. Hỏi chiếc tẩy dài bao nhiêu '
                 'xăng-ti-mét?” ta có lời giải: Vì một đầu trùng vạch $0$ và đầu kia trùng vạch $4$ nên '
                 'chiếc tẩy dài $4\\text{ cm}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ký hiệu đơn vị** (Xăng-ti-mét viết tắt '
                        'là $\\text{cm}$) và lời giải ví dụ minh họa của Bài 26: Đơn vị đo độ dài '
                        '(Xăng-ti-mét).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 26: Đơn vị đo độ dài (Xăng-ti-mét)** để giải bài '
                 'toán sau: Một đầu chiếc tẩy đặt trùng với vạch $0$ của thước, đầu kia trùng với vạch số '
                 '$4$. Hỏi chiếc tẩy dài bao nhiêu xăng-ti-mét? Cách giải và kết quả nào dưới đây là '
                 '**đúng**?',
            'options': ['Vì một đầu trùng vạch $0$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $4\\text{ '
                        'cm}$.',
                        'Vì một đầu trùng vạch $1$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $4\\text{ '
                        'cm}$.',
                        'Vì một đầu trùng vạch $0$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $3\\text{ '
                        'cm}$.',
                        'Vì một đầu trùng vạch $2$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $4\\text{ '
                        'cm}$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 26: Đơn vị đo độ dài (Xăng-ti-mét): Vì một đầu trùng '
                        'vạch $0$ và đầu kia trùng vạch $4$ nên chiếc tẩy dài $4\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một đoạn thẳng có điểm đầu trùng với vạch $0$ và điểm cuối trùng với vạch $9$ trên thước '
                 'kẻ chia xăng-ti-mét. Đoạn thẳng đó dài bao nhiêu xăng-ti-mét?',
            'answer': ['9', '9cm', '9 cm'],
            'unit': None,
            'solution': 'Điểm đầu ở vạch $0$, điểm cuối ở vạch $9$ nên đoạn thẳng dài $9\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd07-do-dai',
  'context_title': 'Chủ đề 7: Độ dài và đo độ dài',
  'context': 'SGK Toán 1 · Chủ đề 7: Dài hơn – ngắn hơn, đơn vị xăng-ti-mét, thực hành ước lượng và đo độ '
             'dài.',
  'title': 'Bài 27: Thực hành ước lượng và đo độ dài',
  'icon': '✂️',
  'description': 'Ước lượng độ dài theo cm, cộng trừ số đo độ dài và giải bài toán thực tế về độ dài.',
  'requirements': ['Ước lượng được độ dài một số đồ vật quen thuộc theo đơn vị $\\text{cm}$ rồi kiểm tra lại '
                   'bằng thước.',
                   'Thực hiện được phép cộng, phép trừ các số đo độ dài có cùng đơn vị $\\text{cm}$.',
                   'Giải được bài toán thực tế về nối thêm hoặc cắt bớt đoạn dây, băng giấy.'],
  'definition': 'Khi cộng hoặc trừ các số đo độ dài có cùng đơn vị $\\text{cm}$, ta thực hiện cộng hoặc trừ '
                'các số như bình thường rồi **viết thêm đơn vị $\\text{cm}$** vào sau kết quả. Ví dụ: '
                '$6\\text{ cm} + 3\\text{ cm} = 9\\text{ cm}$.',
  'theory': '- **Ước lượng độ dài:** Chiều rộng một ngón tay út của học sinh lớp $1$ khoảng $1\\text{ cm}$; '
            'một gang tay khoảng $12\\text{ cm}$ đến $15\\text{ cm}$; chiếc bút chì mới dài khoảng '
            '$15\\text{ cm}$ đến $18\\text{ cm}$.\n'
            '- **Bài toán nối thêm / cắt bớt:**\n'
            '  + Nối hai đoạn thẳng (không chồng lên nhau) $\\rightarrow$ dùng phép cộng.\n'
            '  + Cắt bớt đi hoặc hỏi đoạn này dài hơn đoạn kia bao nhiêu $\\rightarrow$ dùng phép trừ.',
  'formulas': [{'category': 'Phép tính với số đo độ dài (cm)',
                'items': [{'name': 'Cộng độ dài',
                           'formula': '$a\\text{ cm} + b\\text{ cm} = (a + b)\\text{ cm}$',
                           'note': 'Ví dụ: $5\\text{ cm} + 4\\text{ cm} = 9\\text{ cm}$.'},
                          {'name': 'Trừ độ dài',
                           'formula': '$a\\text{ cm} - b\\text{ cm} = (a - b)\\text{ cm}$',
                           'note': 'Ví dụ: $10\\text{ cm} - 4\\text{ cm} = 6\\text{ cm}$.'}]}],
  'example': 'Sợi dây xanh dài $9\\text{ cm}$, sợi dây đỏ dài $6\\text{ cm}$. Hỏi sợi dây xanh dài hơn sợi '
             'dây đỏ bao nhiêu xăng-ti-mét?',
  'example_answer': 'Sợi dây xanh dài hơn sợi dây đỏ là: $9\\text{ cm} - 6\\text{ cm} = 3\\text{ cm}$.',
  'real_life': 'Đo băng giấy để làm thủ công, ước lượng kích thước hộp bút xem có vừa chiếc thước kẻ '
               '$20\\text{ cm}$ hay không.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $6\\text{ cm} + 3\\text{ cm}$ là:',
            'options': ['$9$', '$3\\text{ cm}$', '$10\\text{ cm}$', '$9\\text{ cm}$'],
            'answer': 3,
            'solution': 'Cộng hai số: $6 + 3 = 9$, giữ nguyên đơn vị $\\text{cm}$ được $9\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đồ vật nào dưới đây phù hợp để đo bằng chiếc thước kẻ học sinh dài $20\\text{ cm}$?',
            'options': ['Chiều dài cái bút chì',
                        'Quãng đường từ nhà đến trường',
                        'Chiều dài một con sông',
                        'Chiều cao tòa nhà $10$ tầng'],
            'answer': 0,
            'solution': 'Chiếc bút chì dài khoảng $15\\text{ cm}$ nên đo dễ dàng bằng thước kẻ $20\\text{ '
                        'cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 27: Thực hành ước lượng và đo độ dài**, quy tắc hoặc công thức nào sau đây xác '
                 'định đúng **Cộng độ dài**?',
            'options': ['$a\\text{ cm} - b\\text{ cm} = (a + b)\\text{ cm}$',
                        '$a\\text{ cm} + b\\text{ cm} = (a + b)\\text{ cm}$',
                        'Đảo ngược vế của quy tắc: $a\\text{ cm} + b\\text{ cm} = (a + b)\\text{ cm}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a\\text{ cm} + b\\text{ cm} = '
                        '(a + b)\\text{ cm}$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 27: Thực hành ước lượng và đo độ dài, **Cộng độ '
                        'dài** được xác định bởi: $a\\text{ cm} + b\\text{ cm} = (a + b)\\text{ cm}$. (Ví '
                        'dụ: $5\\text{ cm} + 4\\text{ cm} = 9\\text{ cm}$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 27: Thực hành ước lượng và đo độ dài**, biểu thức hoặc quy tắc nào dưới đây '
                 'biểu diễn đúng **Trừ độ dài**?',
            'options': ['$a\\text{ cm} + b\\text{ cm} = (a - b)\\text{ cm}$',
                        'Đảo ngược vế của quy tắc: $a\\text{ cm} - b\\text{ cm} = (a - b)\\text{ cm}$',
                        '$a\\text{ cm} - b\\text{ cm} = (a - b)\\text{ cm}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a\\text{ cm} - b\\text{ cm} = '
                        '(a - b)\\text{ cm}$'],
            'answer': 2,
            'solution': 'Trong Bài 27: Thực hành ước lượng và đo độ dài, **Trừ độ dài** có công thức/quy tắc '
                        'là: $a\\text{ cm} - b\\text{ cm} = (a - b)\\text{ cm}$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Sợi dây xanh dài $9\\text{ cm}$, sợi dây đỏ dài $6\\text{ cm}$. Sợi dây xanh dài hơn sợi '
                 'dây đỏ bao nhiêu xăng-ti-mét?',
            'options': ['$15\\text{ cm}$', '$2\\text{ cm}$', '$4\\text{ cm}$', '$3\\text{ cm}$'],
            'answer': 3,
            'solution': 'Lấy độ dài sợi dây xanh trừ độ dài sợi dây đỏ: $9\\text{ cm} - 6\\text{ cm} = '
                        '3\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 27: Thực hành ước lượng và đo độ dài**, nhận định nào sau '
                 'đây là **chính xác**?',
            'options': ['Ước lượng được độ dài một số đồ vật quen thuộc theo đơn vị $\\text{cm}$ rồi kiểm '
                        'tra lại bằng thước.',
                        'Ước lượng được độ dài một số đồ vật quen thuộc theo đơn vị $\\text{cm}$ rồi kiểm '
                        'tra lại bằng thước. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Ước lượng được độ dài một số đồ vật quen thuộc theo đơn '
                        'vị $\\text{cm}$ rồi kiểm tra lại bằng thước.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Ước lượng được độ dài một số đồ '
                        'vật quen thuộc theo đơn vị $\\text{cm}$ rồi kiểm tra lại bằng thước.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 27: Thực hành ước lượng và đo độ dài: Ước lượng được '
                        'độ dài một số đồ vật quen thuộc theo đơn vị $\\text{cm}$ rồi kiểm tra lại bằng '
                        'thước.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$10\\text{ cm} - 4\\text{ cm} = 6\\text{ cm}$.”',
            'answer': True,
            'solution': 'Ta có $10 - 4 = 6$, viết kèm đơn vị $\\text{cm}$ là $6\\text{ cm}$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 27: Thực hành ước lượng và đo độ dài**, quy tắc **Cộng độ dài** được xác định '
                 'bởi $a\\text{ cm} + b\\text{ cm} = (a + b)\\text{ cm}$ và khi áp dụng cho ví dụ “Sợi dây '
                 'xanh dài $9\\text{ cm}$, sợi dây đỏ dài $6\\text{ cm}$. Hỏi sợi dây xanh dài hơn sợi dây '
                 'đỏ bao nhiêu xăng-ti-mét?” ta có lời giải: Sợi dây xanh dài hơn sợi dây đỏ là: $9\\text{ '
                 'cm} - 6\\text{ cm} = 3\\text{ cm}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cộng độ dài** ($a\\text{ cm} + b\\text{ '
                        'cm} = (a + b)\\text{ cm}$) và lời giải ví dụ minh họa của Bài 27: Thực hành ước '
                        'lượng và đo độ dài.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 27: Thực hành ước lượng và đo độ dài** để giải bài '
                 'toán sau: Sợi dây xanh dài $9\\text{ cm}$, sợi dây đỏ dài $6\\text{ cm}$. Hỏi sợi dây xanh '
                 'dài hơn sợi dây đỏ bao nhiêu xăng-ti-mét? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Sợi dây xanh dài hơn sợi dây đỏ là: $9\\text{ cm} + 6\\text{ cm} = 3\\text{ cm}$.',
                        'Sợi dây xanh dài hơn sợi dây đỏ là: $9\\text{ cm} - 6\\text{ cm} = 3\\text{ cm}$.',
                        'Sợi dây xanh dài hơn sợi dây đỏ là: $9\\text{ cm} - 6\\text{ cm} = 2\\text{ cm}$.',
                        'Sợi dây xanh dài hơn sợi dây đỏ là: $18\\text{ cm} - 6\\text{ cm} = 3\\text{ cm}$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 27: Thực hành ước lượng và đo độ dài: Sợi dây xanh dài '
                        'hơn sợi dây đỏ là: $9\\text{ cm} - 6\\text{ cm} = 3\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Bạn Nam nối một đoạn dây dài $5\\text{ cm}$ với một đoạn dây dài $4\\text{ cm}$ (nối sát '
                 'đầu nhau, không chồng lên nhau). Hỏi đoạn dây sau khi nối dài bao nhiêu xăng-ti-mét?',
            'answer': ['9', '9cm', '9 cm'],
            'unit': None,
            'solution': 'Độ dài đoạn dây sau khi nối là: $5\\text{ cm} + 4\\text{ cm} = 9\\text{ cm}$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd08-cong-tru-pham-vi-100',
  'context_title': 'Chủ đề 8: Phép cộng, phép trừ (không nhớ) trong phạm vi 100',
  'context': 'SGK Toán 1 · Chủ đề 8: Cộng, trừ số có hai chữ số với số có một, hai chữ số (không nhớ); tính '
             'nhẩm số tròn chục; bài toán có lời văn.',
  'title': 'Bài 29: Phép cộng số có hai chữ số với số có một chữ số',
  'icon': '🧮',
  'description': 'Đặt tính và tính phép cộng (không nhớ) số có hai chữ số với số có một chữ số.',
  'requirements': ['Biết cách đặt tính thẳng cột: chữ số đơn vị của số có một chữ số thẳng cột với chữ số '
                   'hàng đơn vị của số có hai chữ số.',
                   'Thực hiện tính đúng từ phải sang trái (hàng đơn vị cộng trước, hàng chục hạ xuống).',
                   'Vận dụng kiến thức của **Bài 29: Phép cộng số có hai chữ số với số có một chữ số** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi cộng số có hai chữ số với số có một chữ số (không nhớ), ta viết số có một chữ số '
                '**thẳng cột với hàng đơn vị**, cộng các chữ số hàng đơn vị với nhau, rồi hạ chữ số hàng '
                'chục xuống.',
  'theory': '- **Ví dụ: Tính $42 + 4$.**\n'
            '  + Đặt tính: Viết $42$ ở hàng trên, viết $4$ ở hàng dưới thẳng cột với chữ số $2$ (hàng đơn '
            'vị).\n'
            '  + Tính từ phải sang trái: $2 + 4 = 6$, viết $6$; hạ $4$, viết $4$. Kết quả: $42 + 4 = 46$.\n'
            '- **Lỗi cần tránh:** Không được viết số có một chữ số thẳng cột với hàng chục!',
  'formulas': [{'category': 'Quy tắc cộng số có hai chữ số với số có một chữ số',
                'items': [{'name': 'Đặt tính', 'formula': 'Số có $1$ chữ số phải thẳng cột với hàng đơn vị'},
                          {'name': 'Thứ tự tính',
                           'formula': 'Tính hàng đơn vị trước: $\\overline{ab} + c = \\overline{a(b+c)}$ '
                                      '(với $b + c < 10$)',
                           'note': 'Ví dụ: $34 + 5 = 39$.'}]}],
  'example': 'Đặt tính rồi tính: $63 + 5$.',
  'example_answer': 'Cộng hàng đơn vị: $3 + 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 68$.',
  'real_life': 'Tính tổng số quyển truyện trên kệ khi có sẵn $24$ quyển và mua thêm $5$ quyển nữa.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $34 + 5$ là:',
            'options': ['$39$', '$84$', '$38$', '$29$'],
            'answer': 0,
            'solution': 'Cộng hàng đơn vị: $4 + 5 = 9$; giữ nguyên $3$ chục được $39$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đặt tính $52 + 6$, chữ số $6$ phải viết thẳng cột với chữ số nào của số $52$?',
            'options': ['Chữ số $5$', 'Chữ số $2$', 'Viết ở đâu cũng được', 'Viết bên trái chữ số $5$'],
            'answer': 1,
            'solution': 'Số $6$ là $6$ đơn vị nên phải viết thẳng cột với chữ số hàng đơn vị là chữ số $2$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 29: Phép cộng số có hai chữ số với số có một chữ số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Đặt tính**?',
            'options': ['Số có $2$ chữ số phải thẳng cột với hàng đơn vị',
                        'Tính hàng đơn vị trước: $\\overline{ab} + c = \\overline{a(b+c)}$ (với $b + c < '
                        '10$)',
                        'Số có $1$ chữ số phải thẳng cột với hàng đơn vị',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 29: Phép cộng số có hai chữ số với số có một chữ '
                        'số, **Đặt tính** được xác định bởi: Số có $1$ chữ số phải thẳng cột với hàng đơn '
                        'vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 29: Phép cộng số có hai chữ số với số có một chữ số**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Thứ tự tính**?',
            'options': ['Tính hàng đơn vị trước: $\\overline{ab} - c = \\overline{a(b+c)}$ (với $b + c < '
                        '10$)',
                        'Tính hàng đơn vị trước: $\\overline{ab} + c = \\overline{a(b+c)}$ (với $b + c < 9$)',
                        'Tính hàng đơn vị trước: $\\overline{ab} + c = \\overline{a(b+c)}$ (với $b + c < '
                        '20$)',
                        'Tính hàng đơn vị trước: $\\overline{ab} + c = \\overline{a(b+c)}$ (với $b + c < '
                        '10$)'],
            'answer': 3,
            'solution': 'Trong Bài 29: Phép cộng số có hai chữ số với số có một chữ số, **Thứ tự tính** có '
                        'công thức/quy tắc là: Tính hàng đơn vị trước: $\\overline{ab} + c = '
                        '\\overline{a(b+c)}$ (với $b + c < 10$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bằng $78$?',
            'options': ['$71 + 7$', '$70 + 6$', '$27 + 5$', '$7 + 8$'],
            'answer': 0,
            'solution': 'Ta có $71 + 7 = 78$ ($1 + 7 = 8$, hạ $7$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 29: Phép cộng số có hai chữ số với số có một chữ số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Biết cách đặt tính thẳng cột: chữ số đơn vị của số có một chữ số thẳng cột với chữ '
                        'số hàng đơn vị của số có hai chữ số. (với dấu ngược lại)',
                        'Biết cách đặt tính thẳng cột: chữ số đơn vị của số có một chữ số thẳng cột với chữ '
                        'số hàng đơn vị của số có hai chữ số.',
                        'Đảo ngược vế của quy tắc: Biết cách đặt tính thẳng cột: chữ số đơn vị của số có một '
                        'chữ số thẳng cột với chữ số hàng đơn vị của số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Biết cách đặt tính thẳng cột: '
                        'chữ số đơn vị của số có một chữ số thẳng cột với chữ số hàng đơn vị của số có hai '
                        'chữ số.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 29: Phép cộng số có hai chữ số với số có một chữ số: '
                        'Biết cách đặt tính thẳng cột: chữ số đơn vị của số có một chữ số thẳng cột với chữ '
                        'số hàng đơn vị của số có hai chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$43 + 5 = 93$.”',
            'answer': False,
            'solution': 'Cộng $5$ vào hàng đơn vị ($3 + 5 = 8$), kết quả đúng là $43 + 5 = 48$ chứ không '
                        'phải $93$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 29: Phép cộng số có hai chữ số với số có một chữ số**, quy tắc **Đặt tính** '
                 'được xác định bởi Số có $1$ chữ số phải thẳng cột với hàng đơn vị và khi áp dụng cho ví dụ '
                 '“Đặt tính rồi tính: $63 + 5$.” ta có lời giải: Cộng hàng đơn vị: $3 + 5 = 8$, viết $8$; hạ '
                 '$6$ chục, viết $6$. Vậy $63 + 5 = 68$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đặt tính** (Số có $1$ chữ số phải thẳng '
                        'cột với hàng đơn vị) và lời giải ví dụ minh họa của Bài 29: Phép cộng số có hai chữ '
                        'số với số có một chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 29: Phép cộng số có hai chữ số với số có một chữ '
                 'số** để giải bài toán sau: Đặt tính rồi tính: $63 + 5$. Cách giải và kết quả nào dưới đây '
                 'là **đúng**?',
            'options': ['Cộng hàng đơn vị: $3 - 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 68$.',
                        'Cộng hàng đơn vị: $3 + 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 67$.',
                        'Cộng hàng đơn vị: $3 + 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 68$.',
                        'Cộng hàng đơn vị: $6 + 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 68$.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 29: Phép cộng số có hai chữ số với số có một chữ số: '
                        'Cộng hàng đơn vị: $3 + 5 = 8$, viết $8$; hạ $6$ chục, viết $6$. Vậy $63 + 5 = 68$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trong rổ có $32$ quả trứng, mẹ bỏ thêm vào $6$ quả trứng nữa. Hỏi trong rổ có tất cả bao '
                 'nhiêu quả trứng?',
            'answer': ['38'],
            'unit': None,
            'solution': 'Ta có phép cộng: $32 + 6 = 38$ (quả trứng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd08-cong-tru-pham-vi-100',
  'context_title': 'Chủ đề 8: Phép cộng, phép trừ (không nhớ) trong phạm vi 100',
  'context': 'SGK Toán 1 · Chủ đề 8: Cộng, trừ số có hai chữ số với số có một, hai chữ số (không nhớ); tính '
             'nhẩm số tròn chục; bài toán có lời văn.',
  'title': 'Bài 30: Phép cộng số có hai chữ số với số có hai chữ số',
  'icon': '➕',
  'description': 'Đặt tính và tính phép cộng (không nhớ) hai số có hai chữ số; cộng nhẩm các số tròn chục.',
  'requirements': ['Thực hiện được phép cộng (không nhớ) số có hai chữ số với số có hai chữ số.',
                   'Cộng nhẩm thành thạo các số tròn chục trong phạm vi $100$.',
                   'Vận dụng giải bài toán thực tế có phép cộng hai số có hai chữ số.'],
  'definition': 'Khi cộng hai số có hai chữ số (không nhớ), ta đặt tính sao cho **hàng đơn vị thẳng cột hàng '
                'đơn vị, hàng chục thẳng cột hàng chục**, sau đó cộng từ phải sang trái (hàng đơn vị trước, '
                'hàng chục sau).',
  'theory': '- **Ví dụ: Tính $42 + 35$.**\n'
            '  + Hàng đơn vị: $2 + 5 = 7$, viết $7$.\n'
            '  + Hàng chục: $4 + 3 = 7$, viết $7$.\n'
            '  + Vậy $42 + 35 = 77$.\n'
            '- **Cộng nhẩm hai số tròn chục:** Đổi sang chục rồi cộng. Ví dụ: $30 + 20 = ?$ Ta nhẩm $3$ chục '
            '$+ 2$ chục $= 5$ chục, vậy $30 + 20 = 50$.',
  'formulas': [{'category': 'Quy tắc cộng hai số có hai chữ số',
                'items': [{'name': 'Cộng theo cột',
                           'formula': 'Đơn vị cộng đơn vị, chục cộng chục (từ phải sang trái)',
                           'note': 'Ví dụ: $53 + 24 = 77$.'},
                          {'name': 'Cộng nhẩm số tròn chục',
                           'formula': '$a0 + b0 = (a + b)0$',
                           'note': 'Ví dụ: $40 + 30 = 70$ ($4$ chục $+ 3$ chục $= 7$ chục).'}]}],
  'example': 'Đặt tính rồi tính: $53 + 24$ và tính nhẩm: $50 + 40$.',
  'example_answer': '- $53 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = 77$.\n'
                    '- Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$.',
  'real_life': 'Tính tổng số học sinh của hai lớp 1A và 1B khi đi tham quan dã ngoại.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $40 + 30$ là:',
            'options': ['$7$', '$70$', '$43$', '$700$'],
            'answer': 1,
            'solution': '$4$ chục $+ 3$ chục $= 7$ chục $= 70$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi đặt tính $52 + 36$, ta thực hiện tính theo thứ tự nào?',
            'options': ['Cộng hàng chục trước, rồi cộng hàng đơn vị',
                        'Cộng hàng nào trước cũng được',
                        'Cộng hàng đơn vị trước, rồi cộng hàng chục',
                        'Chỉ cộng hàng chục'],
            'answer': 2,
            'solution': 'Ta luôn tính từ phải sang trái: cộng hàng đơn vị trước ($2 + 6 = 8$), rồi cộng hàng '
                        'chục ($5 + 3 = 8$).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 30: Phép cộng số có hai chữ số với số có hai chữ số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Cộng theo cột**?',
            'options': ['Đơn vị cộng đơn vị, chục cộng chục (từ trái sang phải)',
                        'Đảo ngược vế của quy tắc: Đơn vị cộng đơn vị, chục cộng chục (từ phải sang trái)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đơn vị cộng đơn vị, chục cộng '
                        'chục (từ phải sang trái)',
                        'Đơn vị cộng đơn vị, chục cộng chục (từ phải sang trái)'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 30: Phép cộng số có hai chữ số với số có hai chữ '
                        'số, **Cộng theo cột** được xác định bởi: Đơn vị cộng đơn vị, chục cộng chục (từ '
                        'phải sang trái). (Ví dụ: $53 + 24 = 77$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 30: Phép cộng số có hai chữ số với số có hai chữ số**, biểu thức hoặc quy '
                 'tắc nào dưới đây biểu diễn đúng **Cộng nhẩm số tròn chục**?',
            'options': ['$a0 + b0 = (a + b)0$',
                        '$a0 - b0 = (a + b)0$',
                        '$a0 + b0 = (a + b)1$',
                        '$a0 + b0 = (a + b)2$'],
            'answer': 0,
            'solution': 'Trong Bài 30: Phép cộng số có hai chữ số với số có hai chữ số, **Cộng nhẩm số tròn '
                        'chục** có công thức/quy tắc là: $a0 + b0 = (a + b)0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $45 + 32$ là:',
            'options': ['$73$', '$77$', '$87$', '$67$'],
            'answer': 1,
            'solution': 'Hàng đơn vị: $5 + 2 = 7$; hàng chục: $4 + 3 = 7$. Vậy $45 + 32 = 77$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 30: Phép cộng số có hai chữ số với số có hai chữ số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép cộng (không nhớ) số có hai chữ số với số có hai chữ số. (với '
                        'dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép cộng (không nhớ) số có hai chữ số với '
                        'số có hai chữ số.',
                        'Thực hiện được phép cộng (không nhớ) số có hai chữ số với số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép cộng (không '
                        'nhớ) số có hai chữ số với số có hai chữ số.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 30: Phép cộng số có hai chữ số với số có hai chữ số: '
                        'Thực hiện được phép cộng (không nhớ) số có hai chữ số với số có hai chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$26 + 53 = 79$.”',
            'answer': True,
            'solution': 'Hàng đơn vị: $6 + 3 = 9$; hàng chục: $2 + 5 = 7$. Vậy $26 + 53 = 79$. Nhận định '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 30: Phép cộng số có hai chữ số với số có hai chữ số**, quy tắc **Cộng theo '
                 'cột** được xác định bởi Đơn vị cộng đơn vị, chục cộng chục (từ phải sang trái) và khi áp '
                 'dụng cho ví dụ “Đặt tính rồi tính: $53 + 24$ và tính nhẩm: $50 + 40$.” ta có lời giải: - '
                 '$53 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = 77$. - '
                 'Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cộng theo cột** (Đơn vị cộng đơn vị, '
                        'chục cộng chục (từ phải sang trái)) và lời giải ví dụ minh họa của Bài 30: Phép '
                        'cộng số có hai chữ số với số có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 30: Phép cộng số có hai chữ số với số có hai chữ '
                 'số** để giải bài toán sau: Đặt tính rồi tính: $53 + 24$ và tính nhẩm: $50 + 40$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['- $53 - 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = '
                        '77$. - Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$...',
                        '- $53 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = '
                        '77$. - Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 89$...',
                        '- $55 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = '
                        '77$. - Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$...',
                        '- $53 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = '
                        '77$. - Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$...'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 30: Phép cộng số có hai chữ số với số có hai chữ số: - '
                        '$53 + 24$: hàng đơn vị $3 + 4 = 7$, hàng chục $5 + 2 = 7 \\Rightarrow 53 + 24 = '
                        '77$.\n'
                        '- Nhẩm: $5$ chục $+ 4$ chục $= 9$ chục $\\Rightarrow 50 + 40 = 90$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Lớp 1A có $23$ bạn nữ và $15$ bạn nam. Hỏi lớp 1A có tất cả bao nhiêu bạn?',
            'answer': ['38'],
            'unit': None,
            'solution': 'Tổng số bạn của lớp 1A là: $23 + 15 = 38$ (bạn).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd08-cong-tru-pham-vi-100',
  'context_title': 'Chủ đề 8: Phép cộng, phép trừ (không nhớ) trong phạm vi 100',
  'context': 'SGK Toán 1 · Chủ đề 8: Cộng, trừ số có hai chữ số với số có một, hai chữ số (không nhớ); tính '
             'nhẩm số tròn chục; bài toán có lời văn.',
  'title': 'Bài 31: Phép trừ số có hai chữ số cho số có một chữ số',
  'icon': '➖',
  'description': 'Đặt tính và tính phép trừ (không nhớ) số có hai chữ số cho số có một chữ số.',
  'requirements': ['Đặt tính đúng: viết số có một chữ số thẳng cột với chữ số hàng đơn vị của số có hai chữ '
                   'số.',
                   'Tính đúng từ phải sang trái: trừ hàng đơn vị trước, hạ chữ số hàng chục xuống.',
                   'Vận dụng kiến thức của **Bài 31: Phép trừ số có hai chữ số cho số có một chữ số** để '
                   'giải bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Khi trừ số có hai chữ số cho số có một chữ số (không nhớ), ta viết số có một chữ số **thẳng '
                'cột với hàng đơn vị**, lấy chữ số hàng đơn vị trừ đi số có một chữ số, rồi hạ chữ số hàng '
                'chục xuống.',
  'theory': '- **Ví dụ: Tính $76 - 5$.**\n'
            '  + Hàng đơn vị: $6 - 5 = 1$, viết $1$.\n'
            '  + Hàng chục: hạ $7$, viết $7$.\n'
            '  + Vậy $76 - 5 = 71$.\n'
            '- **Trường hợp hàng đơn vị bằng nhau:** $48 - 8 = 40$ (vì $8 - 8 = 0$, hạ $4$ chục được số tròn '
            'chục $40$).',
  'formulas': [{'category': 'Quy tắc trừ số có hai chữ số cho số có một chữ số',
                'items': [{'name': 'Đặt tính',
                           'formula': 'Số trừ có $1$ chữ số phải thẳng cột với hàng đơn vị'},
                          {'name': 'Cách tính',
                           'formula': '$\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\ge c$)',
                           'note': 'Ví dụ: $76 - 5 = 71$; $54 - 4 = 50$.'}]}],
  'example': 'Đặt tính rồi tính: $89 - 6$ và $65 - 5$.',
  'example_answer': '- $89 - 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$.\n'
                    '- $65 - 5$: hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 60$.',
  'real_life': 'Tính số quả trứng còn lại trong khay $36$ quả sau khi mẹ lấy ra $4$ quả để nấu ăn.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $76 - 5$ là:',
            'options': ['$26$', '$81$', '$71$', '$70$'],
            'answer': 2,
            'solution': 'Trừ hàng đơn vị: $6 - 5 = 1$, hạ $7$ chục được $71$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $48 - 8$ là:',
            'options': ['$48$', '$8$', '$30$', '$40$'],
            'answer': 3,
            'solution': 'Hàng đơn vị: $8 - 8 = 0$, hạ $4$ chục được $40$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 31: Phép trừ số có hai chữ số cho số có một chữ số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Đặt tính**?',
            'options': ['Số trừ có $1$ chữ số phải thẳng cột với hàng đơn vị',
                        'Số trừ có $2$ chữ số phải thẳng cột với hàng đơn vị',
                        '$\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\ge c$)',
                        'Trường hợp sai quy tắc (sai lệch 1 đơn vị so với công thức trong bài)'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 31: Phép trừ số có hai chữ số cho số có một chữ '
                        'số, **Đặt tính** được xác định bởi: Số trừ có $1$ chữ số phải thẳng cột với hàng '
                        'đơn vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 31: Phép trừ số có hai chữ số cho số có một chữ số**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Cách tính**?',
            'options': ['$\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\le c$)',
                        '$\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\ge c$)',
                        'Đảo ngược vế của quy tắc: $\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\ge '
                        'c$)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{ab} - c = '
                        '\\overline{a(b-c)}$ (với $b \\ge c$)'],
            'answer': 1,
            'solution': 'Trong Bài 31: Phép trừ số có hai chữ số cho số có một chữ số, **Cách tính** có công '
                        'thức/quy tắc là: $\\overline{ab} - c = \\overline{a(b-c)}$ (với $b \\ge c$).'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bằng $52$?',
            'options': ['$57 - 2$', '$75 - 5$', '$57 - 5$', '$52 - 2$'],
            'answer': 2,
            'solution': 'Ta có $57 - 5 = 52$ ($7 - 5 = 2$, hạ $5$).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 31: Phép trừ số có hai chữ số cho số có một chữ số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Đặt tính đúng: viết số có một chữ số thẳng cột với chữ số hàng đơn vị của số có hai '
                        'chữ số. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đặt tính đúng: viết số có một chữ số thẳng cột với chữ số '
                        'hàng đơn vị của số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đặt tính đúng: viết số có một '
                        'chữ số thẳng cột với chữ số hàng đơn vị của số có hai chữ số.',
                        'Đặt tính đúng: viết số có một chữ số thẳng cột với chữ số hàng đơn vị của số có hai '
                        'chữ số.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 31: Phép trừ số có hai chữ số cho số có một chữ số: '
                        'Đặt tính đúng: viết số có một chữ số thẳng cột với chữ số hàng đơn vị của số có hai '
                        'chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Bạn Bi đặt tính $45 - 3$ bằng cách viết số $3$ thẳng cột với chữ số $4$ (hàng chục) và ra '
                 'kết quả là $15$. Nhận định: “Bạn Bi đã làm đúng.”',
            'answer': False,
            'solution': 'Số $3$ là $3$ đơn vị nên phải viết thẳng cột với chữ số $5$. Kết quả đúng là $45 - '
                        '3 = 42$. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 31: Phép trừ số có hai chữ số cho số có một chữ số**, quy tắc **Đặt tính** '
                 'được xác định bởi Số trừ có $1$ chữ số phải thẳng cột với hàng đơn vị và khi áp dụng cho '
                 'ví dụ “Đặt tính rồi tính: $89 - 6$ và $65 - 5$.” ta có lời giải: - $89 - 6$: hàng đơn vị '
                 '$9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$. - $65 - 5$: hàng đơn vị $5 - 5 = 0$, hạ $6 '
                 '\\Rightarrow 65 - 5 = 60$.... Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Đặt tính** (Số trừ có $1$ chữ số phải '
                        'thẳng cột với hàng đơn vị) và lời giải ví dụ minh họa của Bài 31: Phép trừ số có '
                        'hai chữ số cho số có một chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 31: Phép trừ số có hai chữ số cho số có một chữ '
                 'số** để giải bài toán sau: Đặt tính rồi tính: $89 - 6$ và $65 - 5$. Cách giải và kết quả '
                 'nào dưới đây là **đúng**?',
            'options': ['- $89 - 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$. - $65 - 5$: '
                        'hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 60$.',
                        '- $89 + 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$. - $65 - 5$: '
                        'hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 60$.',
                        '- $89 - 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$. - $65 - 5$: '
                        'hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 59$.',
                        '- $91 - 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$. - $65 - 5$: '
                        'hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 60$.'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 31: Phép trừ số có hai chữ số cho số có một chữ số: - '
                        '$89 - 6$: hàng đơn vị $9 - 6 = 3$, hạ $8 \\Rightarrow 89 - 6 = 83$.\n'
                        '- $65 - 5$: hàng đơn vị $5 - 5 = 0$, hạ $6 \\Rightarrow 65 - 5 = 60$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'An có $28$ viên bi, An cho bạn $6$ viên bi. Hỏi An còn lại bao nhiêu viên bi?',
            'answer': ['22'],
            'unit': None,
            'solution': 'Số viên bi An còn lại là: $28 - 6 = 22$ (viên bi).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd08-cong-tru-pham-vi-100',
  'context_title': 'Chủ đề 8: Phép cộng, phép trừ (không nhớ) trong phạm vi 100',
  'context': 'SGK Toán 1 · Chủ đề 8: Cộng, trừ số có hai chữ số với số có một, hai chữ số (không nhớ); tính '
             'nhẩm số tròn chục; bài toán có lời văn.',
  'title': 'Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số',
  'icon': '📝',
  'description': 'Thực hiện phép trừ hai số có hai chữ số (không nhớ), trừ nhẩm số tròn chục và giải bài '
                 'toán có lời văn.',
  'requirements': ['Thực hiện được phép trừ (không nhớ) số có hai chữ số cho số có hai chữ số.',
                   'Trừ nhẩm thành thạo các số tròn chục; tính được biểu thức có hai dấu phép tính cộng, '
                   'trừ.',
                   'Viết được phép tính và câu trả lời cho bài toán có lời văn.'],
  'definition': '- Khi trừ số có hai chữ số cho số có hai chữ số (không nhớ), ta đặt tính thẳng cột rồi trừ '
                'từ phải sang trái: **đơn vị trừ đơn vị, chục trừ chục**.\n'
                '- Khi giải **bài toán có lời văn**, ta đọc kỹ cái đã cho và câu hỏi, viết **phép tính** '
                'thích hợp và viết **câu trả lời**.',
  'theory': '- **Ví dụ: Tính $86 - 64$.** Hàng đơn vị: $6 - 4 = 2$, viết $2$; hàng chục: $8 - 6 = 2$, viết '
            '$2$. Vậy $86 - 64 = 22$.\n'
            '- **Trừ nhẩm số tròn chục:** $60 - 20 = ?$ Nhẩm: $6$ chục $- 2$ chục $= 4$ chục, vậy $60 - 20 = '
            '40$.\n'
            '- **Hai dấu phép tính:** Tính lần lượt từ trái sang phải, ví dụ $37 + 12 - 23 = 49 - 23 = 26$.',
  'formulas': [{'category': 'Quy tắc trừ hai số có hai chữ số và giải toán',
                'items': [{'name': 'Trừ theo cột',
                           'formula': 'Đơn vị trừ đơn vị, chục trừ chục (từ phải sang trái)',
                           'note': 'Ví dụ: $68 - 35 = 33$.'},
                          {'name': 'Trừ nhẩm số tròn chục',
                           'formula': '$a0 - b0 = (a - b)0$',
                           'note': 'Ví dụ: $90 - 40 = 50$.'},
                          {'name': 'Hai dấu phép tính',
                           'formula': 'Thực hiện từ trái sang phải',
                           'note': 'Ví dụ: $56 - 20 + 3 = 36 + 3 = 39$.'}]}],
  'example': 'Trên cây có $74$ quả thị, gió làm rụng $21$ quả. Hỏi trên cây còn lại bao nhiêu quả thị?',
  'example_answer': 'Phép tính: $74 - 21 = 53$.\nTrả lời: Trên cây còn lại $53$ quả thị.',
  'real_life': 'Tính số trang sách còn phải đọc, số quả bóng còn lại trong cửa hàng sau khi đã bán.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Phép tính nào dưới đây có kết quả bằng $50$?',
            'options': ['$20 + 20$', '$70 - 30$', '$10 + 30$', '$90 - 40$'],
            'answer': 3,
            'solution': '$9$ chục $- 4$ chục $= 5$ chục $= 50$. Vậy $90 - 40 = 50$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $68 - 35$ là:',
            'options': ['$33$', '$23$', '$32$', '$93$'],
            'answer': 0,
            'solution': 'Hàng đơn vị: $8 - 5 = 3$; hàng chục: $6 - 3 = 3$. Vậy $68 - 35 = 33$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số**, quy tắc hoặc công thức '
                 'nào sau đây xác định đúng **Trừ theo cột**?',
            'options': ['Đơn vị trừ đơn vị, chục trừ chục (từ trái sang phải)',
                        'Đơn vị trừ đơn vị, chục trừ chục (từ phải sang trái)',
                        'Đảo ngược vế của quy tắc: Đơn vị trừ đơn vị, chục trừ chục (từ phải sang trái)',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đơn vị trừ đơn vị, chục trừ '
                        'chục (từ phải sang trái)'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 32: Phép trừ số có hai chữ số cho số có hai chữ '
                        'số, **Trừ theo cột** được xác định bởi: Đơn vị trừ đơn vị, chục trừ chục (từ phải '
                        'sang trái). (Ví dụ: $68 - 35 = 33$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Trừ nhẩm số tròn chục**?',
            'options': ['$a0 + b0 = (a - b)0$',
                        '$a0 - b0 = (a - b)1$',
                        '$a0 - b0 = (a - b)0$',
                        '$a0 - b0 = (a - b)2$'],
            'answer': 2,
            'solution': 'Trong Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số, **Trừ nhẩm số tròn '
                        'chục** có công thức/quy tắc là: $a0 - b0 = (a - b)0$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $37 + 12 - 23$ là:',
            'options': ['$72$', '$49$', '$36$', '$26$'],
            'answer': 3,
            'solution': 'Tính từ trái sang phải: $37 + 12 = 49$, sau đó $49 - 23 = 26$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Thực hiện được phép trừ (không nhớ) số có hai chữ số cho số có hai chữ số.',
                        'Thực hiện được phép trừ (không nhớ) số có hai chữ số cho số có hai chữ số. (với dấu '
                        'ngược lại)',
                        'Đảo ngược vế của quy tắc: Thực hiện được phép trừ (không nhớ) số có hai chữ số cho '
                        'số có hai chữ số.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thực hiện được phép trừ (không '
                        'nhớ) số có hai chữ số cho số có hai chữ số.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số: '
                        'Thực hiện được phép trừ (không nhớ) số có hai chữ số cho số có hai chữ số.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$65 - 25 = 40$.”',
            'answer': True,
            'solution': 'Hàng đơn vị: $5 - 5 = 0$; hàng chục: $6 - 2 = 4$. Vậy $65 - 25 = 40$. Nhận định '
                        'Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số**, quy tắc **Trừ theo cột** '
                 'được xác định bởi Đơn vị trừ đơn vị, chục trừ chục (từ phải sang trái) và khi áp dụng cho '
                 'ví dụ “Trên cây có $74$ quả thị, gió làm rụng $21$ quả. Hỏi trên cây còn lại bao nhiêu quả '
                 'thị?” ta có lời giải: Phép tính: $74 - 21 = 53$. Trả lời: Trên cây còn lại $53$ quả thị.. '
                 'Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Trừ theo cột** (Đơn vị trừ đơn vị, chục '
                        'trừ chục (từ phải sang trái)) và lời giải ví dụ minh họa của Bài 32: Phép trừ số có '
                        'hai chữ số cho số có hai chữ số.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 32: Phép trừ số có hai chữ số cho số có hai chữ '
                 'số** để giải bài toán sau: Trên cây có $74$ quả thị, gió làm rụng $21$ quả. Hỏi trên cây '
                 'còn lại bao nhiêu quả thị? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Phép tính: $74 + 21 = 53$. Trả lời: Trên cây còn lại $53$ quả thị.',
                        'Phép tính: $74 - 21 = 53$. Trả lời: Trên cây còn lại $53$ quả thị.',
                        'Phép tính: $74 - 21 = 53$. Trả lời: Trên cây còn lại $52$ quả thị.',
                        'Phép tính: $76 - 21 = 53$. Trả lời: Trên cây còn lại $53$ quả thị.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 32: Phép trừ số có hai chữ số cho số có hai chữ số: Phép '
                        'tính: $74 - 21 = 53$.\n'
                        'Trả lời: Trên cây còn lại $53$ quả thị.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Trên cây có $74$ quả thị, gió lay làm rụng $21$ quả. Hỏi trên cây còn lại bao nhiêu quả '
                 'thị?',
            'answer': ['53'],
            'unit': None,
            'solution': 'Số quả thị còn lại trên cây là: $74 - 21 = 53$ (quả thị).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd09-thoi-gian-gio-lich',
  'context_title': 'Chủ đề 9: Thời gian. Giờ và lịch',
  'context': 'SGK Toán 1 · Chủ đề 9: Xem giờ đúng trên đồng hồ, các ngày trong tuần, xem lịch tờ hằng ngày.',
  'title': 'Bài 34: Xem giờ đúng trên đồng hồ',
  'icon': '🕘',
  'description': 'Nhận biết kim giờ, kim phút và đọc giờ đúng trên mặt đồng hồ.',
  'requirements': ['Nhận biết trên mặt đồng hồ có $12$ số (từ $1$ đến $12$), kim ngắn chỉ giờ, kim dài chỉ '
                   'phút.',
                   'Đọc được giờ đúng khi kim dài chỉ vào số $12$.',
                   'Gắn được giờ đúng với các hoạt động sinh hoạt hằng ngày.'],
  'definition': '- Trên mặt đồng hồ: **kim ngắn** chỉ **giờ**, **kim dài** chỉ **phút**.\n'
                '- **Giờ đúng:** Khi kim dài chỉ đúng vào số $12$, kim ngắn chỉ vào số nào thì đồng hồ chỉ '
                'mấy giờ.',
  'theory': '- Ví dụ 1: Kim dài chỉ số $12$, kim ngắn chỉ số $8$ $\\rightarrow$ đồng hồ chỉ $8$ giờ.\n'
            '- Ví dụ 2: Lúc $12$ giờ đúng, cả kim ngắn và kim dài đều cùng chỉ vào số $12$.\n'
            '- Cần tránh nhầm lẫn giữa kim ngắn và kim dài: kim dài chỉ số $12$ không có nghĩa là $12$ giờ, '
            'phải nhìn xem **kim ngắn** chỉ vào số mấy.',
  'formulas': [{'category': 'Quy tắc đọc giờ đúng',
                'items': [{'name': 'Kim đồng hồ',
                           'formula': 'Kim ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ chỉ phút'},
                          {'name': 'Giờ đúng',
                           'formula': 'Kim dài chỉ số $12$, kim ngắn chỉ số $k \\Rightarrow k$ giờ',
                           'note': 'Ví dụ: Kim dài chỉ $12$, kim ngắn chỉ $7 \\Rightarrow 7$ giờ.'}]}],
  'example': 'Đồng hồ có kim dài chỉ vào số $12$, kim ngắn chỉ vào số $9$. Hỏi đồng hồ chỉ mấy giờ?',
  'example_answer': 'Vì kim dài chỉ số $12$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.',
  'real_life': 'Xem đồng hồ để thức dậy lúc $6$ giờ sáng, vào lớp lúc $7$ giờ, đi ngủ lúc $9$ giờ tối.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Trên mặt đồng hồ, kim nào dùng để chỉ giờ?',
            'options': ['Kim ngắn', 'Kim dài', 'Cả hai kim', 'Không kim nào'],
            'answer': 0,
            'solution': 'Trên mặt đồng hồ, kim ngắn chỉ giờ và kim dài chỉ phút.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Đồng hồ có kim dài chỉ số $12$, kim ngắn chỉ số $8$. Đồng hồ đang chỉ mấy giờ?',
            'options': ['$12$ giờ', '$8$ giờ', '$2$ giờ', '$4$ giờ'],
            'answer': 1,
            'solution': 'Kim dài chỉ số $12$ (giờ đúng), kim ngắn chỉ số $8$ nên đồng hồ chỉ $8$ giờ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 34: Xem giờ đúng trên đồng hồ**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Kim đồng hồ**?',
            'options': ['Kim ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ chỉ phút (với dấu ngược '
                        'lại)',
                        'Đảo ngược vế của quy tắc: Kim ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ '
                        'chỉ phút',
                        'Kim ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ chỉ phút',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Kim ngắn $\\rightarrow$ chỉ '
                        'giờ; Kim dài $\\rightarrow$ chỉ phút'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 34: Xem giờ đúng trên đồng hồ, **Kim đồng hồ** '
                        'được xác định bởi: Kim ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ chỉ '
                        'phút.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 34: Xem giờ đúng trên đồng hồ**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Giờ đúng**?',
            'options': ['Kim dài chỉ số $13$, kim ngắn chỉ số $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ số $11$, kim ngắn chỉ số $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ số $24$, kim ngắn chỉ số $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ số $12$, kim ngắn chỉ số $k \\Rightarrow k$ giờ'],
            'answer': 3,
            'solution': 'Trong Bài 34: Xem giờ đúng trên đồng hồ, **Giờ đúng** có công thức/quy tắc là: Kim '
                        'dài chỉ số $12$, kim ngắn chỉ số $k \\Rightarrow k$ giờ.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Khi đồng hồ chỉ $10$ giờ đúng thì kim dài và kim ngắn chỉ vào những số nào?',
            'options': ['Kim dài chỉ số $12$, kim ngắn chỉ số $10$',
                        'Kim dài chỉ số $10$, kim ngắn chỉ số $12$',
                        'Cả hai kim đều chỉ số $10$',
                        'Kim dài chỉ số $6$, kim ngắn chỉ số $10$'],
            'answer': 0,
            'solution': 'Lúc $10$ giờ đúng, kim dài chỉ số $12$ và kim ngắn chỉ số $10$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 34: Xem giờ đúng trên đồng hồ**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Nhận biết trên mặt đồng hồ có $13$ số (từ $1$ đến $12$), kim ngắn chỉ giờ, kim dài '
                        'chỉ phút.',
                        'Nhận biết trên mặt đồng hồ có $12$ số (từ $1$ đến $12$), kim ngắn chỉ giờ, kim dài '
                        'chỉ phút.',
                        'Nhận biết trên mặt đồng hồ có $12$ số (từ $1$ đến $11$), kim ngắn chỉ giờ, kim dài '
                        'chỉ phút.',
                        'Nhận biết trên mặt đồng hồ có $24$ số (từ $1$ đến $12$), kim ngắn chỉ giờ, kim dài '
                        'chỉ phút.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 34: Xem giờ đúng trên đồng hồ: Nhận biết trên mặt '
                        'đồng hồ có $12$ số (từ $1$ đến $12$), kim ngắn chỉ giờ, kim dài chỉ phút.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Lúc $3$ giờ đúng, kim dài của đồng hồ chỉ vào số $3$.”',
            'answer': False,
            'solution': 'Lúc $3$ giờ đúng, kim dài phải chỉ vào số $12$, còn kim ngắn mới chỉ vào số $3$. '
                        'Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 34: Xem giờ đúng trên đồng hồ**, quy tắc **Kim đồng hồ** được xác định bởi Kim '
                 'ngắn $\\rightarrow$ chỉ giờ; Kim dài $\\rightarrow$ chỉ phút và khi áp dụng cho ví dụ '
                 '“Đồng hồ có kim dài chỉ vào số $12$, kim ngắn chỉ vào số $9$. Hỏi đồng hồ chỉ mấy giờ?” ta '
                 'có lời giải: Vì kim dài chỉ số $12$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.. Đúng '
                 'hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Kim đồng hồ** (Kim ngắn $\\rightarrow$ '
                        'chỉ giờ; Kim dài $\\rightarrow$ chỉ phút) và lời giải ví dụ minh họa của Bài 34: '
                        'Xem giờ đúng trên đồng hồ.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 34: Xem giờ đúng trên đồng hồ** để giải bài toán '
                 'sau: Đồng hồ có kim dài chỉ vào số $12$, kim ngắn chỉ vào số $9$. Hỏi đồng hồ chỉ mấy giờ? '
                 'Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Vì kim dài chỉ số $13$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.',
                        'Vì kim dài chỉ số $12$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $8$ giờ.',
                        'Vì kim dài chỉ số $12$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.',
                        'Vì kim dài chỉ số $24$ và kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 34: Xem giờ đúng trên đồng hồ: Vì kim dài chỉ số $12$ và '
                        'kim ngắn chỉ số $9$ nên đồng hồ chỉ $9$ giờ.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Mai đi ngủ lúc $9$ giờ tối và thức dậy lúc $6$ giờ sáng hôm sau. Hỏi lúc Mai thức dậy, kim '
                 'ngắn của đồng hồ chỉ vào số mấy?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Lúc Mai thức dậy là $6$ giờ sáng nên kim ngắn chỉ vào số $6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd09-thoi-gian-gio-lich',
  'context_title': 'Chủ đề 9: Thời gian. Giờ và lịch',
  'context': 'SGK Toán 1 · Chủ đề 9: Xem giờ đúng trên đồng hồ, các ngày trong tuần, xem lịch tờ hằng ngày.',
  'title': 'Bài 35: Các ngày trong tuần',
  'icon': '📆',
  'description': 'Nhận biết một tuần lễ có 7 ngày, thứ tự các ngày trong tuần và hôm qua – hôm nay – ngày '
                 'mai.',
  'requirements': ['Biết một tuần lễ có $7$ ngày và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.',
                   'Xác định được thứ của ngày hôm qua và ngày mai khi biết thứ của ngày hôm nay.',
                   'Vận dụng kiến thức của **Bài 35: Các ngày trong tuần** để giải bài tập minh họa và bài '
                   'toán thực tiễn.'],
  'definition': '**Một tuần lễ có $7$ ngày**, theo thứ tự lần lượt là: **Thứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, '
                'Thứ Sáu, Thứ Bảy, Chủ nhật**. Hết Chủ nhật lại quay vòng sang Thứ Hai của tuần tiếp theo.',
  'theory': '- **Hôm qua – Hôm nay – Ngày mai:**\n'
            '  + **Hôm qua** là ngày liền trước ngày hôm nay.\n'
            '  + **Ngày mai** là ngày liền sau ngày hôm nay.\n'
            '- Học sinh thường đi học $5$ ngày trong tuần (từ Thứ Hai đến Thứ Sáu) và nghỉ cuối tuần vào $2$ '
            'ngày (Thứ Bảy, Chủ nhật).',
  'formulas': [{'category': 'Thứ tự các ngày trong tuần lễ',
                'items': [{'name': 'Số ngày trong 1 tuần', 'formula': '$1$ tuần lễ $= 7$ ngày'},
                          {'name': 'Vòng tuần hoàn',
                           'formula': 'Thứ Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư $\\rightarrow$ '
                                      'Thứ Năm $\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ '
                                      'Chủ nhật $\\rightarrow$ Thứ Hai'},
                          {'name': 'Liên hệ hôm qua – ngày mai',
                           'formula': 'Hôm qua $\\rightarrow$ Hôm nay $\\rightarrow$ Ngày mai'}]}],
  'example': 'Nếu hôm nay là Thứ Tư thì hôm qua là thứ mấy và ngày mai là thứ mấy?',
  'example_answer': 'Nếu hôm nay là Thứ Tư thì **hôm qua là Thứ Ba** và **ngày mai là Thứ Năm**.',
  'real_life': 'Xem thời khóa biểu từng thứ trong tuần để chuẩn bị sách vở và đồ dùng học tập.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Một tuần lễ có tất cả mấy ngày?',
            'options': ['$5$ ngày', '$7$ ngày', '$6$ ngày', '$10$ ngày'],
            'answer': 1,
            'solution': 'Một tuần lễ có $7$ ngày (từ Thứ Hai đến Chủ nhật).',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Ngày liền sau Thứ Bảy là ngày nào?',
            'options': ['Thứ Sáu', 'Thứ Hai', 'Chủ nhật', 'Thứ Năm'],
            'answer': 2,
            'solution': 'Theo thứ tự các ngày trong tuần, liền sau Thứ Bảy là Chủ nhật.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 35: Các ngày trong tuần**, quy tắc hoặc công thức nào sau đây xác định đúng '
                 '**Số ngày trong 1 tuần**?',
            'options': ['$2$ tuần lễ $= 7$ ngày',
                        '$1$ tuần lễ $= 6$ ngày',
                        'Thứ Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư $\\rightarrow$ Thứ Năm '
                        '$\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ Chủ nhật '
                        '$\\rightarrow$ Thứ Hai',
                        '$1$ tuần lễ $= 7$ ngày'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 35: Các ngày trong tuần, **Số ngày trong 1 tuần** '
                        'được xác định bởi: $1$ tuần lễ $= 7$ ngày.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 35: Các ngày trong tuần**, biểu thức hoặc quy tắc nào dưới đây biểu diễn '
                 'đúng **Vòng tuần hoàn**?',
            'options': ['Thứ Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư $\\rightarrow$ Thứ Năm '
                        '$\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ Chủ nhật '
                        '$\\rightarrow$ Thứ Hai',
                        'Thứ Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư $\\rightarrow$ Thứ Năm '
                        '$\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ Chủ nhật '
                        '$\\rightarrow$ Thứ Hai (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Thứ Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư '
                        '$\\rightarrow$ Thứ Năm $\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ '
                        'Chủ nhật $\\rightarrow$ Thứ Hai',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Thứ Hai $\\rightarrow$ Thứ Ba '
                        '$\\rightarrow$ Thứ Tư $\\rightarrow$ Thứ Năm $\\rightarrow$ Thứ Sáu $\\rightarrow$ '
                        'Thứ Bảy $\\rightarrow$ Chủ nhật $\\rightarrow$ Thứ Hai'],
            'answer': 0,
            'solution': 'Trong Bài 35: Các ngày trong tuần, **Vòng tuần hoàn** có công thức/quy tắc là: Thứ '
                        'Hai $\\rightarrow$ Thứ Ba $\\rightarrow$ Thứ Tư $\\rightarrow$ Thứ Năm '
                        '$\\rightarrow$ Thứ Sáu $\\rightarrow$ Thứ Bảy $\\rightarrow$ Chủ nhật '
                        '$\\rightarrow$ Thứ Hai.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu hôm nay là Thứ Tư thì ngày hôm qua là thứ mấy?',
            'options': ['Thứ Năm', 'Thứ Ba', 'Thứ Hai', 'Chủ nhật'],
            'answer': 1,
            'solution': 'Hôm qua là ngày liền trước hôm nay. Liền trước Thứ Tư là Thứ Ba.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 35: Các ngày trong tuần**, nhận định nào sau đây là **chính '
                 'xác**?',
            'options': ['Biết một tuần lễ có $8$ ngày và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.',
                        'Biết một tuần lễ có $6$ ngày và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.',
                        'Biết một tuần lễ có $7$ ngày và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.',
                        'Biết một tuần lễ có $14$ ngày và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 35: Các ngày trong tuần: Biết một tuần lễ có $7$ ngày '
                        'và kể đúng thứ tự từ Thứ Hai đến Chủ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu hôm nay là Chủ nhật thì ngày mai là Thứ Hai.”',
            'answer': True,
            'solution': 'Hết ngày Chủ nhật sẽ sang ngày Thứ Hai của tuần lễ tiếp theo. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 35: Các ngày trong tuần**, quy tắc **Số ngày trong 1 tuần** được xác định bởi '
                 '$1$ tuần lễ $= 7$ ngày và khi áp dụng cho ví dụ “Nếu hôm nay là Thứ Tư thì hôm qua là thứ '
                 'mấy và ngày mai là thứ mấy?” ta có lời giải: Nếu hôm nay là Thứ Tư thì **hôm qua là Thứ '
                 'Ba** và **ngày mai là Thứ Năm**.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Số ngày trong 1 tuần** ($1$ tuần lễ $= '
                        '7$ ngày) và lời giải ví dụ minh họa của Bài 35: Các ngày trong tuần.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 35: Các ngày trong tuần** để giải bài toán sau: Nếu '
                 'hôm nay là Thứ Tư thì hôm qua là thứ mấy và ngày mai là thứ mấy? Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Chỉ xét trường hợp đặc biệt bằng $0$ và bỏ qua quy tắc chung',
                        'Thực hiện theo thứ tự ngược lại và bỏ qua điều kiện xác định trong bài',
                        'Đổi ngược dấu của phép tính chính và không kiểm tra lại kết quả',
                        'Nếu hôm nay là Thứ Tư thì **hôm qua là Thứ Ba** và **ngày mai là Thứ Năm**.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 35: Các ngày trong tuần: Nếu hôm nay là Thứ Tư thì **hôm '
                        'qua là Thứ Ba** và **ngày mai là Thứ Năm**.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Em đi học từ Thứ Hai đến Thứ Sáu, nghỉ Thứ Bảy và Chủ nhật. Hỏi mỗi tuần lễ em đi học ở '
                 'trường mấy ngày?',
            'answer': ['5'],
            'unit': None,
            'solution': 'Từ Thứ Hai đến Thứ Sáu gồm: Thứ Hai, Thứ Ba, Thứ Tư, Thứ Năm, Thứ Sáu, tất cả là '
                        '$5$ ngày.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd09-thoi-gian-gio-lich',
  'context_title': 'Chủ đề 9: Thời gian. Giờ và lịch',
  'context': 'SGK Toán 1 · Chủ đề 9: Xem giờ đúng trên đồng hồ, các ngày trong tuần, xem lịch tờ hằng ngày.',
  'title': 'Bài 36: Thực hành xem lịch và giờ',
  'icon': '🗓️',
  'description': 'Đọc thông tin thứ, ngày, tháng trên tờ lịch hằng ngày và giải toán thực tế về thời gian.',
  'requirements': ['Đọc được thứ, ngày, tháng trên tờ lịch bóc hằng ngày.',
                   'Tìm được thứ, ngày của hôm qua, ngày mai hoặc ngày cùng thứ ở tuần sau.',
                   'Kết hợp xem giờ đúng và xem lịch để lập thời gian biểu cá nhân.'],
  'definition': 'Trên **tờ lịch hằng ngày** có ghi rõ: **Tháng** (ở phía trên), **Ngày** (số in to ở giữa) '
                'và **Thứ** (ở phía dưới). Cứ sau $1$ tuần lễ ($7$ ngày) thì thứ trong tuần lại lặp lại.',
  'theory': '- Ví dụ: Tờ lịch hôm nay ghi **Tháng $5$ – Ngày $19$ – Thứ Tư**.\n'
            '  + Hôm qua là Thứ Ba, ngày $18$ tháng $5$ ($19 - 1 = 18$).\n'
            '  + Ngày mai là Thứ Năm, ngày $20$ tháng $5$ ($19 + 1 = 20$).\n'
            '- **Mẹo tính ngày cùng thứ của tuần sau:** Lấy số ngày hôm nay cộng thêm $7$. Ví dụ: Thứ Hai '
            'tuần này là ngày $10$ thì Thứ Hai tuần sau là ngày $10 + 7 = 17$.',
  'formulas': [{'category': 'Quy tắc tính ngày trên lịch',
                'items': [{'name': 'Ngày hôm qua',
                           'formula': 'Ngày hôm nay $- 1$',
                           'note': 'Thứ lùi lại $1$ ngày.'},
                          {'name': 'Ngày mai',
                           'formula': 'Ngày hôm nay $+ 1$',
                           'note': 'Thứ tiến lên $1$ ngày.'},
                          {'name': 'Cùng thứ tuần sau',
                           'formula': 'Ngày hôm nay $+ 7$',
                           'note': 'Ví dụ: Thứ Hai ngày $10 \\rightarrow$ Thứ Hai tuần sau là ngày $17$.'}]}],
  'example': 'Hôm nay là Thứ Sáu, ngày $12$ tháng $10$. Hỏi Chủ nhật tuần này là ngày bao nhiêu tháng $10$?',
  'example_answer': 'Thứ Sáu là ngày $12$, Thứ Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng $10$** '
                    '($12 + 2 = 14$).',
  'real_life': 'Nhớ các ngày lễ lớn (như ngày $19$ tháng $5$ sinh nhật Bác Hồ, ngày $20$ tháng $11$ ngày Nhà '
               'giáo Việt Nam) và ngày sinh nhật của người thân.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Tờ lịch hôm nay ghi: Tháng $5$ – Ngày $19$ – Thứ Năm. Vậy ngày $20$ tháng $5$ là thứ mấy?',
            'options': ['Thứ Tư', 'Thứ Bảy', 'Thứ Sáu', 'Chủ nhật'],
            'answer': 2,
            'solution': 'Ngày $20$ là ngày liền sau ngày $19$. Liền sau Thứ Năm là Thứ Sáu.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Nếu hôm nay là ngày $15$ tháng $3$ thì ngày hôm qua là ngày mấy tháng $3$?',
            'options': ['Ngày $16$', 'Ngày $13$', 'Ngày $10$', 'Ngày $14$'],
            'answer': 3,
            'solution': 'Ngày hôm qua liền trước ngày $15$ nên là ngày $15 - 1 = 14$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 36: Thực hành xem lịch và giờ**, quy tắc hoặc công thức nào sau đây xác định '
                 'đúng **Ngày hôm qua**?',
            'options': ['Ngày hôm nay $- 1$',
                        'Ngày hôm nay $- 2$',
                        'Ngày hôm nay $+ 1$',
                        'Ngày hôm nay $+ 7$'],
            'answer': 0,
            'solution': 'Theo kiến thức trọng tâm của Bài 36: Thực hành xem lịch và giờ, **Ngày hôm qua** '
                        'được xác định bởi: Ngày hôm nay $- 1$. (Thứ lùi lại $1$ ngày.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 36: Thực hành xem lịch và giờ**, biểu thức hoặc quy tắc nào dưới đây biểu '
                 'diễn đúng **Ngày mai**?',
            'options': ['Ngày hôm nay $+ 2$',
                        'Ngày hôm nay $+ 1$',
                        'Ngày hôm nay $- 1$',
                        'Ngày hôm nay $+ 7$'],
            'answer': 1,
            'solution': 'Trong Bài 36: Thực hành xem lịch và giờ, **Ngày mai** có công thức/quy tắc là: Ngày '
                        'hôm nay $+ 1$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Bạn Nam học vẽ vào lúc $8$ giờ sáng Chủ nhật và học trong $2$ giờ. Hỏi Nam học xong lúc '
                 'mấy giờ?',
            'options': ['$9$ giờ', '$11$ giờ', '$10$ giờ', '$6$ giờ'],
            'answer': 2,
            'solution': 'Bắt đầu lúc $8$ giờ, học thêm $2$ giờ: $8 + 2 = 10$ (giờ).',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 36: Thực hành xem lịch và giờ**, nhận định nào sau đây là '
                 '**chính xác**?',
            'options': ['Đọc được thứ, ngày, tháng trên tờ lịch bóc hằng ngày. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Đọc được thứ, ngày, tháng trên tờ lịch bóc hằng ngày.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đọc được thứ, ngày, tháng trên '
                        'tờ lịch bóc hằng ngày.',
                        'Đọc được thứ, ngày, tháng trên tờ lịch bóc hằng ngày.'],
            'answer': 3,
            'solution': 'Theo nội dung cốt lõi của Bài 36: Thực hành xem lịch và giờ: Đọc được thứ, ngày, '
                        'tháng trên tờ lịch bóc hằng ngày.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Nếu Thứ Ba tuần này là ngày $11$ thì Thứ Ba tuần sau là ngày $18$.”',
            'answer': True,
            'solution': 'Một tuần lễ có $7$ ngày nên Thứ Ba tuần sau là ngày $11 + 7 = 18$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 36: Thực hành xem lịch và giờ**, quy tắc **Ngày hôm qua** được xác định bởi '
                 'Ngày hôm nay $- 1$ và khi áp dụng cho ví dụ “Hôm nay là Thứ Sáu, ngày $12$ tháng $10$. Hỏi '
                 'Chủ nhật tuần này là ngày bao nhiêu tháng $10$?” ta có lời giải: Thứ Sáu là ngày $12$, Thứ '
                 'Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng $10$** ($12 + 2 = 14$).. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Ngày hôm qua** (Ngày hôm nay $- 1$) và '
                        'lời giải ví dụ minh họa của Bài 36: Thực hành xem lịch và giờ.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 36: Thực hành xem lịch và giờ** để giải bài toán '
                 'sau: Hôm nay là Thứ Sáu, ngày $12$ tháng $10$. Hỏi Chủ nhật tuần này là ngày bao nhiêu '
                 'tháng $10$? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Thứ Sáu là ngày $12$, Thứ Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng '
                        '$10$** ($12 + 2 = 14$).',
                        'Thứ Sáu là ngày $12$, Thứ Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng '
                        '$10$** ($12 - 2 = 14$).',
                        'Thứ Sáu là ngày $12$, Thứ Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng '
                        '$10$** ($12 + 2 = 13$).',
                        'Thứ Sáu là ngày $24$, Thứ Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng '
                        '$10$** ($12 + 2 = 14$).'],
            'answer': 0,
            'solution': 'Lời giải chi tiết theo Bài 36: Thực hành xem lịch và giờ: Thứ Sáu là ngày $12$, Thứ '
                        'Bảy là ngày $13$, vậy **Chủ nhật là ngày $14$ tháng $10$** ($12 + 2 = 14$).'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Hôm nay là Thứ Hai, ngày $10$. Hỏi Thứ Hai tuần sau là ngày bao nhiêu?',
            'answer': ['17'],
            'unit': None,
            'solution': 'Một tuần lễ có $7$ ngày, nên Thứ Hai tuần sau là ngày: $10 + 7 = 17$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd10-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 10: Ôn tập cuối năm',
  'context': 'SGK Toán 1 · Chủ đề 10: Ôn tập các số và phép tính trong phạm vi 10, 100; ôn tập hình học và '
             'đo lường.',
  'title': 'Bài 38: Ôn tập các số và phép tính trong phạm vi 10',
  'icon': '🌟',
  'description': 'Hệ thống lại cấu tạo số, so sánh số và bảng cộng, bảng trừ trong phạm vi 10.',
  'requirements': ['Nắm chắc thứ tự, so sánh và cấu tạo các số từ $0$ đến $10$.',
                   'Tính nhẩm thành thạo các phép cộng, phép trừ và dãy tính hai bước trong phạm vi $10$.',
                   'Vận dụng kiến thức của **Bài 38: Ôn tập các số và phép tính trong phạm vi 10** để giải '
                   'bài tập minh họa và bài toán thực tiễn.'],
  'definition': 'Trong phạm vi $10$, các cặp số cộng lại bằng $10$ ($1 + 9, 2 + 8, 3 + 7, 4 + 6, 5 + 5$) và '
                'mối liên hệ giữa phép cộng với phép trừ giúp em tính nhẩm nhanh và chính xác.',
  'theory': '- **Tính chất giao hoán của phép cộng:** $a + b = b + a$.\n'
            '- **Tính chất của số $0$:** $a + 0 = 0 + a = a$; $a - 0 = a$; $a - a = 0$.\n'
            '- **Dãy tính có hai dấu phép tính:** Tính lần lượt từ trái sang phải.',
  'formulas': [{'category': 'Ôn tập phạm vi 10',
                'items': [{'name': 'Các cặp số tròn 10',
                           'formula': '$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$'},
                          {'name': 'Quan hệ Cộng – Trừ',
                           'formula': '$a + b = c \\Leftrightarrow c - a = b$ và $c - b = a$'}]}],
  'example': 'Tìm số thích hợp điền vào chỗ chấm: $10 - 7 + \\dots = 9$.',
  'example_answer': 'Ta có $10 - 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 6$.',
  'real_life': 'Tính nhẩm nhanh số lượng đồ vật nhỏ hằng ngày trong phạm vi $10$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $8 + 2$ là:',
            'options': ['$6$', '$9$', '$82$', '$10$'],
            'answer': 3,
            'solution': '$8$ và $2$ là cặp số tròn chục: $8 + 2 = 10$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $10 - 6$ là:',
            'options': ['$4$', '$3$', '$5$', '$6$'],
            'answer': 0,
            'solution': 'Vì $6 + 4 = 10$ nên $10 - 6 = 4$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 38: Ôn tập các số và phép tính trong phạm vi 10**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Các cặp số tròn 10**?',
            'options': ['$1 - 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$',
                        '$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$',
                        '$1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 9$',
                        '$2 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$'],
            'answer': 1,
            'solution': 'Theo kiến thức trọng tâm của Bài 38: Ôn tập các số và phép tính trong phạm vi 10, '
                        '**Các cặp số tròn 10** được xác định bởi: $1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = '
                        '10$.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 38: Ôn tập các số và phép tính trong phạm vi 10**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Quan hệ Cộng – Trừ**?',
            'options': ['$a - b = c \\Leftrightarrow c - a = b$ và $c - b = a$',
                        'Đảo ngược vế của quy tắc: $a + b = c \\Leftrightarrow c - a = b$ và $c - b = a$',
                        '$a + b = c \\Leftrightarrow c - a = b$ và $c - b = a$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a + b = c \\Leftrightarrow c - '
                        'a = b$ và $c - b = a$'],
            'answer': 2,
            'solution': 'Trong Bài 38: Ôn tập các số và phép tính trong phạm vi 10, **Quan hệ Cộng – Trừ** '
                        'có công thức/quy tắc là: $a + b = c \\Leftrightarrow c - a = b$ và $c - b = a$.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Dãy tính $9 - 5 + 4$ có kết quả bằng bao nhiêu?',
            'options': ['$0$', '$7$', '$9$', '$8$'],
            'answer': 3,
            'solution': 'Tính từ trái sang phải: $9 - 5 = 4$, sau đó $4 + 4 = 8$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 38: Ôn tập các số và phép tính trong phạm vi 10**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Nắm chắc thứ tự, so sánh và cấu tạo các số từ $0$ đến $10$.',
                        'Nắm chắc thứ tự, so sánh và cấu tạo các số từ $1$ đến $10$.',
                        'Nắm chắc thứ tự, so sánh và cấu tạo các số từ $0$ đến $9$.',
                        'Nắm chắc thứ tự, so sánh và cấu tạo các số từ $2$ đến $10$.'],
            'answer': 0,
            'solution': 'Theo nội dung cốt lõi của Bài 38: Ôn tập các số và phép tính trong phạm vi 10: Nắm '
                        'chắc thứ tự, so sánh và cấu tạo các số từ $0$ đến $10$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “$3 + 6 = 10 - 1$.”',
            'answer': True,
            'solution': 'Ta có $3 + 6 = 9$ và $10 - 1 = 9$, hai vế cùng bằng $9$. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 38: Ôn tập các số và phép tính trong phạm vi 10**, quy tắc **Các cặp số tròn '
                 '10** được xác định bởi $1 + 9 = 2 + 8 = 3 + 7 = 4 + 6 = 5 + 5 = 10$ và khi áp dụng cho ví '
                 'dụ “Tìm số thích hợp điền vào chỗ chấm: $10 - 7 + \\dots = 9$.” ta có lời giải: Ta có $10 '
                 '- 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 6$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Các cặp số tròn 10** ($1 + 9 = 2 + 8 = 3 '
                        '+ 7 = 4 + 6 = 5 + 5 = 10$) và lời giải ví dụ minh họa của Bài 38: Ôn tập các số và '
                        'phép tính trong phạm vi 10.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 38: Ôn tập các số và phép tính trong phạm vi 10** '
                 'để giải bài toán sau: Tìm số thích hợp điền vào chỗ chấm: $10 - 7 + \\dots = 9$. Cách giải '
                 'và kết quả nào dưới đây là **đúng**?',
            'options': ['Ta có $10 - 7 = 3$. Để $3 - \\dots = 9$ thì số cần điền là $9 - 3 = 6$.',
                        'Ta có $10 - 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 6$.',
                        'Ta có $10 - 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 5$.',
                        'Ta có $20 - 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 6$.'],
            'answer': 1,
            'solution': 'Lời giải chi tiết theo Bài 38: Ôn tập các số và phép tính trong phạm vi 10: Ta có '
                        '$10 - 7 = 3$. Để $3 + \\dots = 9$ thì số cần điền là $9 - 3 = 6$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Số thích hợp điền vào chỗ chấm trong phép tính $\\dots + 4 = 10$ là số nào?',
            'answer': ['6'],
            'unit': None,
            'solution': 'Vì $10 - 4 = 6$ nên số cần điền là $6$.',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd10-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 10: Ôn tập cuối năm',
  'context': 'SGK Toán 1 · Chủ đề 10: Ôn tập các số và phép tính trong phạm vi 10, 100; ôn tập hình học và '
             'đo lường.',
  'title': 'Bài 39: Ôn tập các số và phép tính trong phạm vi 100',
  'icon': '💯',
  'description': 'Ôn tập cấu tạo số có hai chữ số, so sánh số và cộng, trừ (không nhớ) trong phạm vi 100.',
  'requirements': ['Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $100$.',
                   'Đặt tính và tính đúng phép cộng, phép trừ (không nhớ) trong phạm vi $100$.',
                   'Giải được bài toán có lời văn bằng một phép tính cộng hoặc trừ trong phạm vi $100$.'],
  'definition': 'Số có hai chữ số $\\overline{ab}$ gồm $a$ chục và $b$ đơn vị. Khi đặt tính cộng hoặc trừ '
                '(không nhớ), ta viết thẳng cột hàng đơn vị với hàng đơn vị, hàng chục với hàng chục rồi '
                'tính từ phải sang trái.',
  'theory': '- **So sánh số:** So sánh hàng chục trước; nếu hàng chục bằng nhau mới so sánh hàng đơn vị.\n'
            '- **Tính nhẩm số tròn chục:** Cộng, trừ số chục rồi viết thêm chữ số $0$ ở hàng đơn vị.\n'
            '- **Bài toán có lời văn:** Tìm từ khóa “thêm”, “tất cả”, “cả hai” (thường là phép cộng) hoặc '
            '“bớt”, “đã bán”, “cắt đi”, “còn lại” (thường là phép trừ).',
  'formulas': [{'category': 'Ôn tập số và phép tính phạm vi 100',
                'items': [{'name': 'Cấu tạo số', 'formula': '$\\overline{ab} = a$ chục $+ b$ đơn vị'},
                          {'name': 'Đặt tính cộng, trừ',
                           'formula': 'Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái'},
                          {'name': 'Biểu thức 2 bước',
                           'formula': 'Thực hiện lần lượt từ trái sang phải',
                           'note': 'Ví dụ: $56 - 20 + 3 = 36 + 3 = 39$.'}]}],
  'example': 'Cửa hàng có $68$ quả bóng, đã bán $25$ quả. Hỏi cửa hàng còn lại bao nhiêu quả bóng?',
  'example_answer': 'Phép tính: $68 - 25 = 43$.\nTrả lời: Cửa hàng còn lại $43$ quả bóng.',
  'real_life': 'Kiểm đếm sách vở, tính toán số lượng đồ vật trong phạm vi $100$.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Số “sáu mươi tư” được viết là:',
            'options': ['$64$', '$604$', '$46$', '$6$'],
            'answer': 0,
            'solution': 'Sáu mươi là $6$ chục, tư là $4$ đơn vị, viết là $64$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $45 + 32$ là:',
            'options': ['$73$', '$77$', '$67$', '$87$'],
            'answer': 1,
            'solution': 'Hàng đơn vị: $5 + 2 = 7$; hàng chục: $4 + 3 = 7$. Vậy $45 + 32 = 77$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 39: Ôn tập các số và phép tính trong phạm vi 100**, quy tắc hoặc công thức nào '
                 'sau đây xác định đúng **Cấu tạo số**?',
            'options': ['$\\overline{ab} = a$ chục $+ b$ đơn vị (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $\\overline{ab} = a$ chục $+ b$ đơn vị',
                        '$\\overline{ab} = a$ chục $+ b$ đơn vị',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $\\overline{ab} = a$ chục $+ b$ '
                        'đơn vị'],
            'answer': 2,
            'solution': 'Theo kiến thức trọng tâm của Bài 39: Ôn tập các số và phép tính trong phạm vi 100, '
                        '**Cấu tạo số** được xác định bởi: $\\overline{ab} = a$ chục $+ b$ đơn vị.'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 39: Ôn tập các số và phép tính trong phạm vi 100**, biểu thức hoặc quy tắc '
                 'nào dưới đây biểu diễn đúng **Đặt tính cộng, trừ**?',
            'options': ['Đơn vị thẳng đơn vị, chục thẳng chục; tính từ trái sang phải',
                        'Đảo ngược vế của quy tắc: Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang '
                        'trái',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Đơn vị thẳng đơn vị, chục thẳng '
                        'chục; tính từ phải sang trái',
                        'Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang trái'],
            'answer': 3,
            'solution': 'Trong Bài 39: Ôn tập các số và phép tính trong phạm vi 100, **Đặt tính cộng, trừ** '
                        'có công thức/quy tắc là: Đơn vị thẳng đơn vị, chục thẳng chục; tính từ phải sang '
                        'trái.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Kết quả của dãy tính $56 - 20 + 3$ là:',
            'options': ['$39$', '$33$', '$36$', '$79$'],
            'answer': 0,
            'solution': 'Tính từ trái sang phải: $56 - 20 = 36$, rồi lấy $36 + 3 = 39$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 39: Ôn tập các số và phép tính trong phạm vi 100**, nhận '
                 'định nào sau đây là **chính xác**?',
            'options': ['Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $110$.',
                        'Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $100$.',
                        'Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $99$.',
                        'Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $102$.'],
            'answer': 1,
            'solution': 'Theo nội dung cốt lõi của Bài 39: Ôn tập các số và phép tính trong phạm vi 100: '
                        'Đọc, viết, phân tích cấu tạo chục – đơn vị và so sánh thành thạo các số đến $100$.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Số $80$ vừa là số có hai chữ số, vừa là số tròn chục.”',
            'answer': True,
            'solution': 'Số $80$ gồm $2$ chữ số ($8$ và $0$) và có chữ số hàng đơn vị bằng $0$ nên là số '
                        'tròn chục. Nhận định Đúng.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 39: Ôn tập các số và phép tính trong phạm vi 100**, quy tắc **Cấu tạo số** '
                 'được xác định bởi $\\overline{ab} = a$ chục $+ b$ đơn vị và khi áp dụng cho ví dụ “Cửa '
                 'hàng có $68$ quả bóng, đã bán $25$ quả. Hỏi cửa hàng còn lại bao nhiêu quả bóng?” ta có '
                 'lời giải: Phép tính: $68 - 25 = 43$. Trả lời: Cửa hàng còn lại $43$ quả bóng.. Đúng hay '
                 'sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Cấu tạo số** ($\\overline{ab} = a$ chục '
                        '$+ b$ đơn vị) và lời giải ví dụ minh họa của Bài 39: Ôn tập các số và phép tính '
                        'trong phạm vi 100.'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 39: Ôn tập các số và phép tính trong phạm vi 100** '
                 'để giải bài toán sau: Cửa hàng có $68$ quả bóng, đã bán $25$ quả. Hỏi cửa hàng còn lại bao '
                 'nhiêu quả bóng? Cách giải và kết quả nào dưới đây là **đúng**?',
            'options': ['Phép tính: $68 + 25 = 43$. Trả lời: Cửa hàng còn lại $43$ quả bóng.',
                        'Phép tính: $68 - 25 = 43$. Trả lời: Cửa hàng còn lại $42$ quả bóng.',
                        'Phép tính: $68 - 25 = 43$. Trả lời: Cửa hàng còn lại $43$ quả bóng.',
                        'Phép tính: $70 - 25 = 43$. Trả lời: Cửa hàng còn lại $43$ quả bóng.'],
            'answer': 2,
            'solution': 'Lời giải chi tiết theo Bài 39: Ôn tập các số và phép tính trong phạm vi 100: Phép '
                        'tính: $68 - 25 = 43$.\n'
                        'Trả lời: Cửa hàng còn lại $43$ quả bóng.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Cửa hàng có $68$ quả bóng, đã bán $25$ quả bóng. Hỏi cửa hàng còn lại bao nhiêu quả bóng?',
            'answer': ['43'],
            'unit': None,
            'solution': 'Số quả bóng cửa hàng còn lại là: $68 - 25 = 43$ (quả bóng).',
            'alt': None,
            'note': None}]},
 {'topic': 'l1-cd10-on-tap-cuoi-nam',
  'context_title': 'Chủ đề 10: Ôn tập cuối năm',
  'context': 'SGK Toán 1 · Chủ đề 10: Ôn tập các số và phép tính trong phạm vi 10, 100; ôn tập hình học và '
             'đo lường.',
  'title': 'Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm)',
  'icon': '🏆',
  'description': 'Ôn tập tổng hợp về hình phẳng, hình khối, độ dài (cm), xem giờ đúng và xem lịch.',
  'requirements': ['Nhận dạng thành thạo hình vuông, hình tròn, hình tam giác, hình chữ nhật, khối lập '
                   'phương, khối hộp chữ nhật.',
                   'Thực hiện được phép cộng, phép trừ số đo độ dài với đơn vị $\\text{cm}$.',
                   'Đọc đúng giờ đúng trên đồng hồ và xác định thứ, ngày trên tờ lịch.'],
  'definition': 'Tổng hợp kiến thức Hình học và Đo lường lớp 1:\n'
                '- **Độ dài:** Đơn vị xăng-ti-mét ($\\text{cm}$), đặt vạch $0$ trùng một đầu vật khi đo.\n'
                '- **Thời gian:** Giờ đúng (kim dài chỉ số $12$), $1$ tuần lễ có $7$ ngày.',
  'theory': '- **Hình học:** Phân biệt rõ hình phẳng ($2$ chiều) và hình khối ($3$ chiều).\n'
            '- **Đo độ dài:** Khi cắt bớt một đoạn dây, độ dài còn lại bằng độ dài ban đầu trừ đi độ dài '
            'đoạn cắt ra.\n'
            '- **Thời gian:** Kết hợp xem đồng hồ và xem lịch để giải các bài toán thực tế về sinh hoạt hằng '
            'ngày.',
  'formulas': [{'category': 'Tổng hợp Hình học & Đo lường lớp 1',
                'items': [{'name': 'Tính với đơn vị cm',
                           'formula': '$a\\text{ cm} \\pm b\\text{ cm} = (a \\pm b)\\text{ cm}$',
                           'note': 'Ví dụ: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.'},
                          {'name': 'Đồng hồ giờ đúng',
                           'formula': 'Kim dài chỉ $12$, kim ngắn chỉ $k \\Rightarrow k$ giờ'},
                          {'name': 'Tuần lễ',
                           'formula': '$1$ tuần lễ $= 7$ ngày (Thứ Hai $\\rightarrow$ Chủ nhật)'}]}],
  'example': 'Một sợi dây dài $86\\text{ cm}$. Bạn Hà cắt đi một đoạn dài $40\\text{ cm}$. Hỏi đoạn dây còn '
             'lại dài bao nhiêu xăng-ti-mét?',
  'example_answer': 'Đoạn dây còn lại dài là: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.',
  'real_life': 'Vận dụng đo độ dài, xem giờ học bài, xem lịch nghỉ hè và chuẩn bị hành trang lên lớp 2.',
  'quiz': [{'level': 'biet',
            'type': 'mcq',
            'q': 'Đồng hồ chỉ $10$ giờ đúng khi kim dài chỉ số $12$ và kim ngắn chỉ vào số nào?',
            'options': ['$12$', '$10$', '$1$', '$2$'],
            'answer': 1,
            'solution': 'Giờ đúng có kim dài chỉ số $12$, kim ngắn chỉ số $10$ thì là $10$ giờ.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Kết quả của phép tính $35\\text{ cm} + 20\\text{ cm}$ là:',
            'options': ['$55$', '$15\\text{ cm}$', '$55\\text{ cm}$', '$50\\text{ cm}$'],
            'answer': 2,
            'solution': 'Ta có $35 + 20 = 55$, viết kèm đơn vị đo độ dài là $55\\text{ cm}$.',
            'alt': None,
            'note': None},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Trong **Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm)**, quy tắc hoặc công '
                 'thức nào sau đây xác định đúng **Tính với đơn vị cm**?',
            'options': ['$a\\text{ cm} \\pm b\\text{ cm} = (a \\pm b)\\text{ cm}$ (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: $a\\text{ cm} \\pm b\\text{ cm} = (a \\pm b)\\text{ cm}$',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của $a\\text{ cm} \\pm b\\text{ cm} '
                        '= (a \\pm b)\\text{ cm}$',
                        '$a\\text{ cm} \\pm b\\text{ cm} = (a \\pm b)\\text{ cm}$'],
            'answer': 3,
            'solution': 'Theo kiến thức trọng tâm của Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối '
                        'năm), **Tính với đơn vị cm** được xác định bởi: $a\\text{ cm} \\pm b\\text{ cm} = '
                        '(a \\pm b)\\text{ cm}$. (Ví dụ: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.)'},
           {'level': 'biet',
            'type': 'mcq',
            'q': 'Khi học **Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm)**, biểu thức hoặc '
                 'quy tắc nào dưới đây biểu diễn đúng **Đồng hồ giờ đúng**?',
            'options': ['Kim dài chỉ $12$, kim ngắn chỉ $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ $13$, kim ngắn chỉ $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ $11$, kim ngắn chỉ $k \\Rightarrow k$ giờ',
                        'Kim dài chỉ $24$, kim ngắn chỉ $k \\Rightarrow k$ giờ'],
            'answer': 0,
            'solution': 'Trong Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm), **Đồng hồ giờ '
                        'đúng** có công thức/quy tắc là: Kim dài chỉ $12$, kim ngắn chỉ $k \\Rightarrow k$ '
                        'giờ.'},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Nếu hôm nay là Thứ Bảy ngày $20$ thì Chủ nhật ngày mai là ngày bao nhiêu?',
            'options': ['Ngày $19$', 'Ngày $21$', 'Ngày $22$', 'Ngày $27$'],
            'answer': 1,
            'solution': 'Ngày mai liền sau ngày $20$ là ngày $20 + 1 = 21$.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'mcq',
            'q': 'Để nắm vững bản chất của **Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm)**, '
                 'nhận định nào sau đây là **chính xác**?',
            'options': ['Nhận dạng thành thạo hình vuông, hình tròn, hình tam giác, hình chữ nhật, khối lập '
                        'phương, khối hộp chữ nhật. (với dấu ngược lại)',
                        'Đảo ngược vế của quy tắc: Nhận dạng thành thạo hình vuông, hình tròn, hình tam '
                        'giác, hình chữ nhật, khối lập phương, khối hộp chữ nhật.',
                        'Nhận dạng thành thạo hình vuông, hình tròn, hình tam giác, hình chữ nhật, khối lập '
                        'phương, khối hộp chữ nhật.',
                        'Trường hợp trái ngược: không thỏa mãn điều kiện của Nhận dạng thành thạo hình '
                        'vuông, hình tròn, hình tam giác, hình chữ nhật, khối lập phương, khối hộp chữ '
                        'nhật.'],
            'answer': 2,
            'solution': 'Theo nội dung cốt lõi của Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối '
                        'năm): Nhận dạng thành thạo hình vuông, hình tròn, hình tam giác, hình chữ nhật, '
                        'khối lập phương, khối hộp chữ nhật.'},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Nhận định: “Khối hộp chữ nhật có các mặt đều là hình tròn.”',
            'answer': False,
            'solution': 'Các mặt của khối hộp chữ nhật là hình chữ nhật (có thể có $2$ mặt hình vuông), '
                        'không có mặt nào là hình tròn. Nhận định Sai.',
            'alt': None,
            'note': None},
           {'level': 'hieu',
            'type': 'tf',
            'q': 'Trong **Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm)**, quy tắc **Tính với '
                 'đơn vị cm** được xác định bởi $a\\text{ cm} \\pm b\\text{ cm} = (a \\pm b)\\text{ cm}$ và '
                 'khi áp dụng cho ví dụ “Một sợi dây dài $86\\text{ cm}$. Bạn Hà cắt đi một đoạn dài '
                 '$40\\text{ cm}$. Hỏi đoạn dây còn lại dài bao nhiêu xăng-ti-mét?” ta có lời giải: Đoạn dây '
                 'còn lại dài là: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.. Đúng hay sai?',
            'answer': True,
            'solution': 'Khẳng định **Đúng**. Đó chính là quy tắc **Tính với đơn vị cm** ($a\\text{ cm} \\pm '
                        'b\\text{ cm} = (a \\pm b)\\text{ cm}$) và lời giải ví dụ minh họa của Bài 40: Ôn '
                        'tập hình học và đo lường (Ôn tập chung cuối năm).'},
           {'level': 'vandung',
            'type': 'mcq',
            'q': 'Vận dụng trực tiếp kiến thức của **Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối '
                 'năm)** để giải bài toán sau: Một sợi dây dài $86\\text{ cm}$. Bạn Hà cắt đi một đoạn dài '
                 '$40\\text{ cm}$. Hỏi đoạn dây còn lại dài bao nhiêu xăng-ti-mét? Cách giải và kết quả nào '
                 'dưới đây là **đúng**?',
            'options': ['Đoạn dây còn lại dài là: $86\\text{ cm} + 40\\text{ cm} = 46\\text{ cm}$.',
                        'Đoạn dây còn lại dài là: $86\\text{ cm} - 40\\text{ cm} = 45\\text{ cm}$.',
                        'Đoạn dây còn lại dài là: $88\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.',
                        'Đoạn dây còn lại dài là: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.'],
            'answer': 3,
            'solution': 'Lời giải chi tiết theo Bài 40: Ôn tập hình học và đo lường (Ôn tập chung cuối năm): '
                        'Đoạn dây còn lại dài là: $86\\text{ cm} - 40\\text{ cm} = 46\\text{ cm}$.'},
           {'level': 'vandung',
            'type': 'short',
            'q': 'Một sợi dây dài $86\\text{ cm}$. Bạn Hà cắt đi một đoạn dài $40\\text{ cm}$. Hỏi đoạn dây '
                 'còn lại dài bao nhiêu xăng-ti-mét?',
            'answer': ['46', '46cm', '46 cm'],
            'unit': None,
            'solution': 'Độ dài đoạn dây còn lại là: $86 - 40 = 46$ ($\\text{cm}$).',
            'alt': None,
            'note': None}]}]
