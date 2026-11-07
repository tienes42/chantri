"""Vật lý Lớp 10 (SGK Vật lí 10 - Kết nối tri thức với cuộc sống): 7 Chương - 27 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 10

CH1 = ("l10-ch01-mo-dau", "Chương I: Mở đầu", "Chương I · SGK Vật lí 10: Đối tượng nghiên cứu Vật lí, quy tắc an toàn và sai số phép đo.")
CH2 = ("l10-ch02-dong-hoc", "Chương II: Động học", "Chương II · SGK Vật lí 10: Độ dịch chuyển, vận tốc, gia tốc, chuyển động biến đổi đều, rơi tự do và ném ngang.")
CH3 = ("l10-ch03-dong-luc-hoc", "Chương III: Động lực học", "Chương III · SGK Vật lí 10: Tổng hợp lực, ba định luật Newton, trọng lực, lực căng, ma sát và lực cản.")
CH4 = ("l10-ch04-nang-luong-cong-cong-suat", "Chương IV: Năng lượng, Công, Công suất", "Chương IV · SGK Vật lí 10: Công, công suất, động năng, thế năng, định luật bảo toàn cơ năng và hiệu suất.")
CH5 = ("l10-ch05-dong-luong", "Chương V: Động lượng", "Chương V · SGK Vật lí 10: Động lượng, xung lượng của lực, định luật bảo toàn động lượng và va chạm.")
CH6 = ("l10-ch06-chuyen-dong-tron", "Chương VI: Chuyển động tròn", "Chương VI · SGK Vật lí 10: Động học chuyển động tròn đều, tốc độ góc, gia tốc hướng tâm và lực hướng tâm.")
CH7 = ("l10-ch07-bien-dang-ap-suat", "Chương VII: Biến dạng của vật rắn. Áp suất chất lỏng", "Chương VII · SGK Vật lí 10: Moment lực, cân bằng vật rắn, biến dạng lò xo, định luật Hooke và áp suất chất lỏng.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Làm quen với Vật lí",
        icon="🔬",
        description="Đối tượng nghiên cứu của Vật lí, vai trò của Vật lí đối với khoa học công nghệ và hai phương pháp nghiên cứu chính.",
        requirements=[
            "Nêu được đối tượng nghiên cứu của Vật lí là các dạng vận động của vật chất (chất, trường) và năng lượng.",
            "Phân biệt được hai phương pháp nghiên cứu chủ đạo của Vật lí: phương pháp thực nghiệm và phương pháp mô hình.",
            "Trình bày được 5 bước của chu trình phương pháp thực nghiệm do Galileo Galilei đặt nền móng.",
        ],
        definition="Đối tượng nghiên cứu của Vật lí là các dạng vận động của vật chất (chất và trường) và năng lượng. Hai phương pháp nghiên cứu cơ bản của Vật lí là phương pháp thực nghiệm và phương pháp mô hình.",
        theory=(
            "### 1. Đối tượng và mục tiêu của Vật lí\n"
            "- **Đối tượng nghiên cứu**: các dạng vận động của vật chất (cơ, nhiệt, điện, từ, quang, nguyên tử và hạt nhân) và năng lượng.\n"
            "- **Mục tiêu**: khám phá các quy luật tổng quát chi phối sự vận động của vật chất và năng lượng ở mọi cấp độ từ vi mô ($10^{-18}\\text{ m}$) đến vĩ mô ($10^{26}\\text{ m}$).\n\n"
            "### 2. Hai phương pháp nghiên cứu Vật lí\n"
            "1. **Phương pháp thực nghiệm** (5 bước): Xác định vấn đề cần nghiên cứu $\\to$ Quan sát, thu thập thông tin $\\to$ Đưa ra dự đoán (giả thuyết) $\\to$ Tiến hành thí nghiệm kiểm tra dự đoán $\\to$ Kết luận.\n"
            "2. **Phương pháp mô hình**: dùng các mô hình vật chất, mô hình lí thuyết (chất điểm, tia sáng, khí lí tưởng) hoặc mô hình toán học (công thức, đồ thị) để nghiên cứu đối tượng thực."
        ),
        formulas=[
            G(
                "Chu trình nghiên cứu Vật lí",
                F("5 bước của phương pháp thực nghiệm", "$\\text{Vấn đề} \\to \\text{Quan sát} \\to \\text{Giả thuyết} \\to \\text{Thí nghiệm kiểm chứng} \\to \\text{Kết luận}$", "Nếu thí nghiệm mâu thuẫn với giả thuyết thì phải điều chỉnh hoặc thay giả thuyết mới."),
                F("Ba loại mô hình thường dùng trong Vật lí", "$\\text{Mô hình vật lí} = \\{\\text{Mô hình vật chất},\\ \\text{Mô hình lí thuyết (chất điểm, tia sáng)},\\ \\text{Mô hình toán học}\\}$", "Ví dụ: công thức $s = \\dfrac{1}{2}gt^2$ là một mô hình toán học của sự rơi tự do."),
            )
        ],
        example="Khi nghiên cứu chuyển động của Trái Đất quanh Mặt Trời, vì kích thước của Trái Đất rất nhỏ so với khoảng cách từ Trái Đất đến Mặt Trời nên các nhà vật lí coi Trái Đất như một điểm có khối lượng gọi là 'chất điểm'. Cách làm này thuộc phương pháp nghiên cứu nào?",
        example_answer="Việc thay thế Trái Đất bằng khái niệm 'chất điểm' để đơn giản hóa bài toán thuộc **phương pháp mô hình** (mô hình lí thuyết).",
        real_life="Sự ra đời của máy hơi nước (cuộc cách mạng công nghiệp lần thứ nhất), máy phát điện (lần thứ hai), máy tính bán dẫn và Internet (lần thứ ba) đều bắt nguồn từ các thành tựu nghiên cứu Vật lí.",
        quiz=[
            mcq("biet", "Đối tượng nghiên cứu chính của môn Vật lí là gì?", ["Các dạng vận động của vật chất và năng lượng", "Sự sinh trưởng và phát triển của các loài sinh vật", "Cấu tạo lịch sử các triều đại phong kiến", "Ngữ pháp và từ vựng của các ngôn ngữ"], 0, "Vật lí nghiên cứu các dạng vận động của vật chất (chất, trường) và năng lượng."),
            mcq("biet", "Trong phương pháp thực nghiệm, bước nào có vai trò quyết định để kiểm tra tính đúng đắn của giả thuyết đã đề ra?", ["Tiến hành thí nghiệm kiểm tra dự đoán", "Viết báo cáo tổng kết trước khi quan sát", "Bỏ qua mọi số liệu thực tế", "Chỉ dựa vào suy luận chủ quan"], 0, "Thí nghiệm kiểm chứng là tiêu chuẩn khách quan quyết định giả thuyết đúng hay sai."),
            mcq("hieu", "Khái niệm 'tia sáng', 'chất điểm' và 'khí lí tưởng' trong Vật lí thuộc loại mô hình nào?", ["Mô hình lí thuyết", "Mô hình vật chất thu nhỏ", "Dụng cụ đo trực tiếp", "Sai số ngẫu nhiên"], 0, "Chất điểm, tia sáng, khí lí tưởng là các mô hình lí thuyết dùng để lược bỏ các yếu tố phụ không quan trọng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đối tượng và phương pháp nghiên cứu Vật lí:", [
                "Galileo Galilei (thí nghiệm thả rơi hai quả cầu tại tháp nghiêng Pisa) được coi là cha đẻ của phương pháp thực nghiệm.",
                "Phương pháp thực nghiệm gồm 5 bước khép kín từ xác định vấn đề đến thí nghiệm kiểm chứng và kết luận.",
                "Nếu kết quả thí nghiệm chính xác mà trái ngược với dự đoán thì ta phải sửa lại số liệu thí nghiệm cho khớp với dự đoán.",
                "Công thức $v = g \\cdot t$ là một mô hình toán học mô tả tốc độ rơi tự do theo thời gian.",
            ], [True, True, False, True], "Ý c) sai vì khi thí nghiệm phản bác giả thuyết thì phải chỉnh sửa hoặc bác bỏ giả thuyết chứ tuyệt đối không được làm sai lệch số liệu thí nghiệm."),
            short("vandung", "Quy trình của phương pháp thực nghiệm trong nghiên cứu Vật lí gồm mấy bước cơ bản (từ xác định vấn đề đến kết luận)?", ["5"], "Quy trình phương pháp thực nghiệm gồm $5$ bước cơ bản."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Các quy tắc an toàn trong phòng thực hành Vật lí",
        icon="⚠️",
        description="Quy tắc an toàn khi làm việc với thiết bị điện, nguồn nhiệt, tia laser, hóa chất và hệ thống biển cảnh báo.",
        requirements=[
            "Nhận biết được ý nghĩa của các biển báo an toàn thông dụng trong phòng thực hành (cảnh báo hình tam giác vàng, cấm hình tròn gạch đỏ, bắt buộc hình tròn nền xanh).",
            "Nêu được các nguy cơ mất an toàn khi sử dụng thiết bị điện, nguồn nhiệt, tia laser và chất phóng xạ.",
            "Thực hiện đúng các quy tắc an toàn và trang bị bảo hộ trong phòng thực hành Vật lí.",
        ],
        definition="Tuân thủ các quy tắc an toàn trong phòng thực hành Vật lí và nhận biết đúng các biển cảnh báo giúp bảo vệ sức khỏe, tính mạng của người học và giữ gìn trang thiết bị thí nghiệm.",
        theory=(
            "### 1. An toàn khi làm thí nghiệm Vật lí\n"
            "- **An toàn điện**: chỉ cắm nguồn điện khi giáo viên đã kiểm tra mạch; dùng điện áp thấp một chiều ($6\\text{ V} - 12\\text{ V}$) trong thí nghiệm học sinh; không chạm tay ướt vào ổ điện $220\\text{ V}$.\n"
            "- **An toàn quang học và nhiệt**: tuyệt đối **không chiếu tia laser trực tiếp vào mắt**; dùng kẹp gỗ khi cầm ống nghiệm đang đun nóng.\n\n"
            "### 2. Hệ thống biển báo an toàn trong phòng thí nghiệm\n"
            "- **Biển báo cấm**: hình tròn, viền đỏ, nền trắng, có gạch chéo đỏ (ví dụ: cấm lửa, cấm uống nước).\n"
            "- **Biển báo cảnh báo nguy hiểm**: hình tam giác đều, viền đen hoặc đỏ, nền vàng (ví dụ: cảnh báo điện áp cao $\\lightning$, cảnh báo tia laser, cảnh báo chất dễ cháy, cảnh báo bề mặt nóng).\n"
            "- **Biển báo bắt buộc thực hiện**: hình tròn, nền xanh lam, hình vẽ trắng (ví dụ: bắt buộc đeo kính bảo hộ, đeo găng tay)."
        ),
        formulas=[
            G(
                "Quy ước hình dạng và màu sắc biển báo an toàn",
                F("Biển cảnh báo nguy hiểm và Biển cấm", "$\\triangle\\text{ Nền vàng, viền đen}: \\text{Cảnh báo nguy hiểm}; \\qquad \\oslash\\text{ Tròn viền đỏ gạch chéo}: \\text{Biển cấm}$", "Biển hình tròn nền xanh lam hình trắng là biển bắt buộc thực hiện (như đeo kính bảo hộ)."),
                F("Quy tắc lắp mạch điện thực hành", "$\\text{Lắp mạch (Khóa } K \\text{ mở)} \\to \\text{Giáo viên kiểm tra} \\to \\text{Cấp nguồn \\& Đóng khóa } K$", "Khi kết thúc thí nghiệm hoặc thay đổi linh kiện, phải ngắt nguồn điện trước tiên."),
            )
        ],
        example="Trong bài thực hành quang học khảo sát khúc xạ ánh sáng bằng đèn phát tia laser, vì sao học sinh phải đặt mắt nhìn từ phía trên xuống vệt tia sáng trên bảng chia độ mà tuyệt đối không được cúi ngang nhìn thẳng vào đầu phát tia laser?",
        example_answer="Vì chùm tia laser có năng lượng tập trung rất cao trên một diện tích cực nhỏ; nếu chiếu thẳng vào mắt sẽ làm tổn thương nghiêm trọng võng mạc mắt, thậm chí gây mù vĩnh viễn.",
        real_life="Trên các trạm biến áp điện cao thế ngoài đường phố luôn gắn biển hình tam giác vàng có tia sét đen ghi 'Điện áp cao – Nguy hiểm chết người' để cảnh báo mọi người tránh xa.",
        quiz=[
            mcq("biet", "Biển báo an toàn có dạng **hình tam giác đều, nền màu vàng, viền đen** trong phòng thực hành thuộc loại biển báo nào?", ["Biển cảnh báo nguy hiểm (điện cao áp, tia laser, chất dễ cháy...)", "Biển cấm thực hiện", "Biển bắt buộc phải thực hiện", "Biển chỉ dẫn lối thoát hiểm"], 0, "Biển hình tam giác nền vàng viền đen dùng để cảnh báo các nguy cơ mất an toàn."),
            mcq("biet", "Khi thực hành với nguồn phát tia laser trong phòng thí nghiệm, hành động nào sau đây bị **nghiêm cấm** tuyệt đối?", ["Chiếu thẳng tia laser vào mắt mình hoặc mắt bạn học", "Chiếu tia laser là là trên mặt bảng chia độ", "Tắt nguồn đèn laser sau khi đo xong", "Đọc giá trị góc tới trên thước đo độ"], 0, "Tia laser chiếu thẳng vào mắt sẽ gây bỏng võng mạc rất nguy hiểm."),
            mcq("hieu", "Khi đang làm thí nghiệm điện trong phòng thực hành mà phát hiện dây dẫn bị hở lớp vỏ cách điện và bốc khói, việc đầu tiên cần làm ngay là gì?", ["Ngắt ngay nguồn điện (cầu dao/công tắc nguồn) và báo cho giáo viên phụ trách", "Dùng tay trần nắm trực tiếp vào chỗ dây hở để kéo ra", "Đổ một cốc nước lạnh lên bộ nguồn điện đang cắm", "Tiếp tục tăng điện áp lên mức tối đa"], 0, "Phải ngắt ngay nguồn điện và báo giáo viên; tuyệt đối không chạm tay trần hoặc đổ nước vào thiết bị đang mang điện."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về quy tắc an toàn trong phòng thực hành:", [
                "Chỉ được đóng công tắc cấp nguồn điện cho mạch thí nghiệm sau khi giáo viên đã kiểm tra sơ đồ mạch.",
                "Biển báo hình tròn viền đỏ có vạch gạch chéo đỏ trên nền trắng là biển báo cấm.",
                "Khi đun nóng chất lỏng trong ống nghiệm trên đèn cồn, nên hướng miệng ống nghiệm thẳng vào mặt người đối diện.",
                "Trước khi rời phòng thực hành, cần tắt các thiết bị điện, thu dọn dụng cụ gọn gang và rửa tay sạch sẽ.",
            ], [True, True, False, True], "Ý c) sai vì khi đun ống nghiệm phải hướng miệng ống về phía không có người để tránh chất lỏng sôi bắn vào người."),
            short("vandung", "Hệ thống biển báo an toàn cơ bản trong phòng thực hành gồm mấy nhóm chính (Biển cấm, Biển cảnh báo nguy hiểm, Biển bắt buộc thực hiện)?", ["3"], "Có $3$ nhóm biển báo an toàn cơ bản: biển cấm, biển cảnh báo nguy hiểm và biển bắt buộc thực hiện."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 3: Thực hành tính sai số trong phép đo. Ghi kết quả đo",
        icon="📐",
        description="Phép đo trực tiếp và gián tiếp, sai số hệ thống và ngẫu nhiên, cách tính giá trị trung bình, sai số tuyệt đối, sai số tỉ đối và ghi kết quả đo.",
        requirements=[
            "Phân biệt được phép đo trực tiếp và phép đo gián tiếp; phân biệt sai số hệ thống (sai số dụng cụ) và sai số ngẫu nhiên.",
            "Tính được giá trị trung bình $\\bar{A}$, sai số tuyệt đối trung bình $\\overline{\\Delta A}$, sai số tuyệt đối $\\Delta A = \\overline{\\Delta A} + \\Delta A_{\\text{dc}}$ và sai số tỉ đối $\\delta A = \\dfrac{\\Delta A}{\\bar{A}} \\cdot 100\\%$.",
            "Biểu diễn đúng kết quả đo dưới dạng $A = \\bar{A} \\pm \\Delta A$ và vận dụng quy tắc tính sai số của phép đo gián tiếp.",
        ],
        definition="Kết quả của một phép đo đại lượng $A$ được biểu diễn dưới dạng $A = \\bar{A} \\pm \\Delta A$, trong đó $\\bar{A}$ là giá trị trung bình của các lần đo và $\\Delta A = \\overline{\\Delta A} + \\Delta A_{\\text{dc}}$ là sai số tuyệt đối của phép đo.",
        theory=(
            "### 1. Phân loại phép đo và các loại sai số\n"
            "- **Phép đo trực tiếp**: đọc trực tiếp kết quả trên dụng cụ đo (đo chiều dài bằng thước, đo thời gian bằng đồng hồ).\n"
            "- **Phép đo gián tiếp**: xác định đại lượng thông qua công thức liên hệ với các đại lượng đo trực tiếp (ví dụ tính tốc độ $v = \\dfrac{s}{t}$).\n"
            "- **Sai số hệ thống**: có tính quy luật, lặp lại như nhau ở mọi lần đo (do dụng cụ chưa hiệu chỉnh số $0$ hoặc giới hạn độ chia nhỏ nhất). Sai số dụng cụ $\\Delta A_{\\text{dc}}$ thường lấy bằng $1$ hoặc $\\dfrac{1}{2}$ độ chia nhỏ nhất (ĐCNN).\n"
            "- **Sai số ngẫu nhiên**: không có quy luật rõ ràng (do thao tác người đo, điều kiện bên ngoài), khắc phục bằng cách **đo nhiều lần rồi lấy trung bình**.\n\n"
            "### 2. Công thức tính sai số và cách ghi kết quả đo\n"
            "- Giá trị trung bình của $n$ lần đo: $\\bar{A} = \\dfrac{A_1 + A_2 + \\dots + A_n}{n}$.\n"
            "- Sai số tuyệt đối của mỗi lần đo: $\\Delta A_i = |\\bar{A} - A_i|$; sai số ngẫu nhiên trung bình: $\\overline{\\Delta A} = \\dfrac{\\Delta A_1 + \\dots + \\Delta A_n}{n}$.\n"
            "- **Sai số tuyệt đối của phép đo**: $\\Delta A = \\overline{\\Delta A} + \\Delta A_{\\text{dc}}$.\n"
            "- **Sai số tỉ đối**: $\\delta A = \\dfrac{\\Delta A}{\\bar{A}} \\cdot 100\\%$ ($\\delta A$ càng nhỏ thì phép đo càng chính xác).\n"
            "- **Sai số phép đo gián tiếp**: Tổng/Hiệu thì cộng sai số tuyệt đối ($\\Delta(X \\pm Y) = \\Delta X + \\Delta Y$); Tích/Thương/Lũy thừa thì cộng sai số tỉ đối ($\\delta(X \\cdot Y) = \\delta(X/Y) = \\delta X + \\delta Y$; $\\delta(X^k) = k \\cdot \\delta X$)."
        ),
        formulas=[
            G(
                "Công thức tính sai số và ghi kết quả đo",
                F("Giá trị trung bình và Sai số tuyệt đối", "$\\bar{A} = \\dfrac{1}{n}\\sum_{i=1}^n A_i; \\qquad \\Delta A = \\overline{\\Delta A} + \\Delta A_{\\text{dc}}; \\qquad A = \\bar{A} \\pm \\Delta A$", "Trong đó $\\overline{\\Delta A} = \\dfrac{|\\bar{A}-A_1| + \\dots + |\\bar{A}-A_n|}{n}$."),
                F("Sai số tỉ đối và Sai số phép đo gián tiếp", "$\\delta A = \\dfrac{\\Delta A}{\\bar{A}} \\cdot 100\\%; \\qquad \\text{Nếu } F = \\dfrac{X^m \\cdot Y^n}{Z^k} \\implies \\delta F = m\\,\\delta X + n\\,\\delta Y + k\\,\\delta Z$", "Sai số tuyệt đối $\\Delta A$ thường chỉ viết đến 1 hoặc tối đa 2 chữ số có nghĩa, còn $\\bar{A}$ làm tròn đến cùng bậc thập phân với $\\Delta A$."),
            )
        ],
        example="Một học sinh đo quãng đường đi của xe lăn cho kết quả $s = 1{,}20 \\pm 0{,}03\\text{ (m)}$ và thời gian chuyển động là $t = 2{,}00 \\pm 0{,}04\\text{ (s)}$. Hãy tính sai số tỉ đối của quãng đường $\\delta s$, của thời gian $\\delta t$ và sai số tỉ đối của tốc độ trung bình $\\delta v$ (với $v = \\dfrac{s}{t}$).",
        example_answer="Ta có $\\delta s = \\dfrac{0{,}03}{1{,}20} \\cdot 100\\% = 2{,}5\\%$ và $\\delta t = \\dfrac{0{,}04}{2{,}00} \\cdot 100\\% = 2{,}0\\%$. Vì $v = \\dfrac{s}{t}$ nên sai số tỉ đối của phép đo tốc độ là $\\delta v = \\delta s + \\delta t = 2{,}5\\% + 2{,}0\\% = 4{,}5\\%$.",
        real_life="Trong sản xuất linh kiện cơ khí chính xác và vi mạch điện tử, mọi kích thước chi tiết đều được quy định kèm dung sai ($\\bar{d} \\pm \\Delta d$) để đảm bảo lắp ghép chuẩn xác.",
        quiz=[
            mcq("biet", "Kết quả của phép đo đại lượng $A$ có giá trị trung bình $\\bar{A}$ và sai số tuyệt đối $\\Delta A$ được ghi chuẩn xác theo biểu thức nào?", ["$A = \\bar{A} \\pm \\Delta A$", "$A = \\bar{A} \\cdot \\Delta A$", "$A = \\dfrac{\\bar{A}}{\\Delta A}$", "$A = \\Delta A \\pm \\bar{A}$"], 0, "Cách ghi chuẩn kết quả đo là $A = \\bar{A} \\pm \\Delta A$."),
            mcq("biet", "Công thức tính sai số tỉ đối $\\delta A$ của một phép đo là gì?", ["$\\delta A = \\dfrac{\\Delta A}{\\bar{A}} \\cdot 100\\%$", "$\\delta A = \\dfrac{\\bar{A}}{\\Delta A} \\cdot 100\\%$", "$\\delta A = (\\bar{A} + \\Delta A) \\cdot 100\\%$", "$\\delta A = (\\bar{A} - \\Delta A) \\cdot 100\\%$"], 0, "Sai số tỉ đối bằng tỉ số phần trăm giữa sai số tuyệt đối $\\Delta A$ và giá trị trung bình $\\bar{A}$: $\\delta A = \\dfrac{\\Delta A}{\\bar{A}} \\cdot 100\\%$."),
            mcq("hieu", "Cho tốc độ được tính gián tiếp theo công thức $v = \\dfrac{s}{t}$. Sai số tỉ đối $\\delta v$ liên hệ với sai số tỉ đối của quãng đường ($\\delta s$) và thời gian ($\\delta t$) theo hệ thức nào?", ["$\\delta v = \\delta s + \\delta t$", "$\\delta v = \\delta s - \\delta t$", "$\\delta v = \\dfrac{\\delta s}{\\delta t}$", "$\\delta v = \\delta s \\cdot \\delta t$"], 0, "Sai số tỉ đối của một thương (hoặc một tích) bằng tổng các sai số tỉ đối của các thừa số thành phần: $\\delta v = \\delta s + \\delta t$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sai số phép đo:", [
                "Sai số tỉ đối $\\delta A$ càng nhỏ thì phép đo càng chính xác.",
                "Để giảm sai số ngẫu nhiên, ta tiến hành đo nhiều lần trong cùng điều kiện rồi lấy giá trị trung bình.",
                "Sai số do chưa hiệu chỉnh kim của cân hoặc ampe kế về đúng vạch số $0$ trước khi đo là sai số ngẫu nhiên.",
                "Nếu $L = 20{,}0 \\pm 0{,}4\\text{ cm}$ thì sai số tỉ đối của phép đo chiều dài này là $\\delta L = 2\\%$.",
            ], [True, True, False, True], "Ý c) sai vì chưa chỉnh kim về vạch số $0$ làm mọi lần đo đều lệch một lượng cố định theo cùng một chiều, đó là sai số hệ thống."),
            short("vandung", "Đo chiều dài một con lắc đơn cho kết quả $\\ell = 80{,}0 \\pm 0{,}8\\text{ (cm)}$. Sai số tỉ đối $\\delta \\ell$ của phép đo này bằng bao nhiêu phần trăm ($\\%$)?", ["1"], "Áp dụng công thức $\\delta \\ell = \\dfrac{\\Delta \\ell}{\\bar{\\ell}} \\cdot 100\\% = \\dfrac{0{,}8}{80{,}0} \\cdot 100\\% = 1\\%$.", unit="%"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 4: Độ dịch chuyển và quãng đường đi được",
        icon="🧭",
        description="Phân biệt quãng đường đi được s và vectơ độ dịch chuyển d, tổng hợp độ dịch chuyển và điều kiện để |d| = s.",
        requirements=[
            "Định nghĩa được độ dịch chuyển $\\vec{d}$ là một đại lượng vectơ nối điểm đầu và điểm cuối của chuyển động (cho biết cả độ dài và hướng sự thay đổi vị trí của vật).",
            "Phân biệt được quãng đường đi được $s$ (vô hướng, luôn không âm) và độ dịch chuyển $d$ (đại số/vectơ); nêu điều kiện để độ lớn độ dịch chuyển bằng quãng đường ($|d| = s$).",
            "Tính được quãng đường và độ dịch chuyển trong chuyển động thẳng có đổi chiều và chuyển động theo hai phương vuông góc ($d = \\sqrt{d_1^2 + d_2^2}$).",
        ],
        definition="Độ dịch chuyển ($\\vec{d}$) là một đại lượng vectơ có gốc tại vị trí ban đầu, hướng từ vị trí đầu đến vị trí cuối và độ lớn bằng khoảng cách thẳng nối từ vị trí đầu đến vị trí cuối của vật.",
        theory=(
            "### 1. Phân biệt Độ dịch chuyển và Quãng đường đi được\n"
            "- **Quãng đường đi được ($s$)**: độ dài thực tế của quỹ đạo mà vật đã đi qua ($s \\ge 0$, đại lượng vô hướng).\n"
            "- **Độ dịch chuyển ($\\vec{d}$)**: đại lượng vectơ cho biết độ dài và hướng của sự thay đổi vị trí từ điểm xuất phát $A$ đến điểm kết thúc $B$.\n"
            "- Trên trục tọa độ $Ox$: độ dịch chuyển đại số là $d = \\Delta x = x_2 - x_1$ (có thể dương, âm hoặc bằng $0$).\n\n"
            "### 2. Quan hệ giữa $|d|$ và $s$ & Tổng hợp độ dịch chuyển\n"
            "- Tổng quát: $|d| \\le s$.\n"
            "- Khi vật **chuyển động thẳng và không đổi chiều** (theo chiều dương): $d = s$.\n"
            "- Khi vật đi một vòng rồi quay về đúng vị trí xuất phát ban đầu ($B \\equiv A$): $s > 0$ nhưng độ dịch chuyển **$d = 0$**.\n"
            "- Tổng hợp hai độ dịch chuyển liên tiếp: $\\vec{d} = \\vec{d}_1 + \\vec{d}_2$. Nếu $\\vec{d}_1 \\perp \\vec{d}_2$ thì $d = \\sqrt{d_1^2 + d_2^2}$."
        ),
        formulas=[
            G(
                "Quãng đường và Độ dịch chuyển",
                F("Độ dịch chuyển trên trục tọa độ Ox", "$d = \\Delta x = x_2 - x_1; \\qquad |d| \\le s$", "Dấu bằng $|d| = s$ chỉ xảy ra khi vật chuyển động thẳng và không đổi chiều."),
                F("Tổng hợp hai độ dịch chuyển vuông góc", "$\\vec{d} = \\vec{d}_1 + \\vec{d}_2 \\implies d = \\sqrt{d_1^2 + d_2^2} \\quad (\\text{khi } \\vec{d}_1 \\perp \\vec{d}_2)$", "Áp dụng định lí Pythagore khi vật đi theo hai hướng vuông góc (ví dụ hướng Bắc rồi rẽ sang hướng Đông)."),
            )
        ],
        example="Một người đi bộ từ vị trí $A$ về hướng Bắc một đoạn $d_1 = 300\\text{ m}$ đến điểm $B$, sau đó rẽ vuông góc sang hướng Đông đi thêm $d_2 = 400\\text{ m}$ đến điểm $C$. Hãy tính quãng đường $s$ người đó đã đi được và độ lớn độ dịch chuyển $d$ từ $A$ đến $C$.",
        example_answer="Quãng đường người đó đã đi là $s = d_1 + d_2 = 300 + 400 = 700\\text{ m}$. Vì hướng Bắc vuông góc với hướng Đông ($\\vec{d}_1 \\perp \\vec{d}_2$) nên độ lớn độ dịch chuyển là $d = AC = \\sqrt{d_1^2 + d_2^2} = \\sqrt{300^2 + 400^2} = 500\\text{ m}$.",
        real_life="Ứng dụng bản đồ số (Google Maps) hiển thị cả 'khoảng cách đường chim bay' (độ lớn của độ dịch chuyển $d$) và 'lộ trình di chuyển theo đường phố' (quãng đường $s$).",
        quiz=[
            mcq("biet", "Đại lượng nào sau đây là đại lượng **vectơ**, cho biết cả độ dài và hướng của sự thay đổi vị trí của vật?", ["Độ dịch chuyển $\\vec{d}$", "Quãng đường đi được $s$", "Thời gian chuyển động $t$", "Khối lượng của vật $m$"], 0, "Độ dịch chuyển $\\vec{d}$ là đại lượng vectơ nối điểm đầu tới điểm cuối chuyển động."),
            mcq("biet", "Trong trường hợp nào sau đây, độ lớn của độ dịch chuyển $|d|$ bằng đúng quãng đường đi được $s$?", ["Khi vật chuyển động thẳng và không đổi chiều", "Khi vật chuyển động tròn một vòng quanh sân", "Khi vật đi từ $A$ đến $B$ rồi quay ngược lại $A$", "Khi vật chuyển động theo đường gấp khúc"], 0, "Độ lớn độ dịch chuyển chỉ bằng quãng đường đi được khi vật chuyển động thẳng và không đổi chiều."),
            mcq("hieu", "Một vận động viên bơi dọc theo bể bơi dài $50\\text{ m}$ từ đầu bể $A$ đến cuối bể $B$, rồi bơi ngược về đúng đầu bể $A$ ban đầu. Quãng đường đi được $s$ và độ dịch chuyển $d$ của vận động viên sau cả hai lượt bơi là bao nhiêu?", ["$s = 100\\text{ m}$ và $d = 0\\text{ m}$", "$s = 100\\text{ m}$ và $d = 100\\text{ m}$", "$s = 50\\text{ m}$ và $d = 50\\text{ m}$", "$s = 0\\text{ m}$ và $d = 100\\text{ m}$"], 0, "Tổng quãng đường bơi cả đi lẫn về là $s = 50 + 50 = 100\\text{ m}$; vì điểm cuối trùng với điểm đầu ($A$) nên độ dịch chuyển $d = 0\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về độ dịch chuyển và quãng đường:", [
                "Quãng đường đi được $s$ là đại lượng vô hướng và luôn không âm ($s \\ge 0$).",
                "Độ lớn của độ dịch chuyển luôn nhỏ hơn hoặc bằng quãng đường đi được ($|d| \\le s$).",
                "Nếu chọn chiều dương là chiều từ Tây sang Đông, vật đi từ Đông sang Tây một đoạn $10\\text{ m}$ có giá trị độ dịch chuyển đại số là $d = -10\\text{ m}$.",
                "Hai vật có cùng độ dịch chuyển từ $A$ đến $B$ thì bắt buộc phải đi trên cùng một quỹ đạo và đi cùng một quãng đường.",
            ], [True, True, True, False], "Ý d) sai vì hai vật xuất phát cùng từ $A$ và kết thúc cùng tại $B$ luôn có cùng độ dịch chuyển $\\vec{AB}$ dù đi theo các con đường ngoằn ngoèo dài ngắn khác nhau."),
            short("vandung", "Một ca nô chạy thẳng về hướng Đông một đoạn $6\\text{ km}$, sau đó rẽ vuông góc chạy thẳng về hướng Bắc một đoạn $8\\text{ km}$. Độ lớn độ dịch chuyển $d$ của ca nô kể từ điểm xuất phát bằng bao nhiêu $\\text{km}$?", ["10"], "Vì hai hướng Đông và Bắc vuông góc nhau nên $d = \\sqrt{6^2 + 8^2} = \\sqrt{100} = 10\\text{ km}$.", unit="km"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 5: Tốc độ và vận tốc",
        icon="🚤",
        description="Phân biệt tốc độ trung bình v_tb = s/t và vận tốc trung bình v = d/t, vận tốc tức thời và công thức cộng vận tốc.",
        requirements=[
            "Phân biệt được tốc độ trung bình $v_{\\text{tb}} = \\dfrac{s}{t}$ (vô hướng) và vận tốc trung bình $\\vec{v} = \\dfrac{\\vec{d}}{t}$ (vectơ).",
            "Nêu được vận tốc tức thời là vận tốc tại một thời điểm xác định (độ lớn của nó hiển thị trên tốc kế của xe).",
            "Vận dụng được công thức cộng vận tốc $\\vec{v}_{13} = \\vec{v}_{12} + \\vec{v}_{23}$ trong trường hợp cùng phương và vuông góc.",
        ],
        definition="Tốc độ trung bình được tính bằng thương số giữa quãng đường đi được và thời gian: $v_{\\text{tb}} = \\dfrac{s}{t}$. Vận tốc trung bình là đại lượng vectơ được tính bằng thương số giữa độ dịch chuyển và thời gian: $\\vec{v} = \\dfrac{\\vec{d}}{t}$.",
        theory=(
            "### 1. Tốc độ trung bình, Vận tốc trung bình và Vận tốc tức thời\n"
            "- **Tốc độ trung bình**: $v_{\\text{tb}} = \\dfrac{s}{\\Delta t}$ (vô hướng, luôn $\\ge 0$). Nếu đi nhiều chặng: $v_{\\text{tb}} = \\dfrac{s_1 + s_2}{t_1 + t_2}$.\n"
            "- **Vận tốc trung bình**: $\\vec{v} = \\dfrac{\\vec{d}}{\\Delta t}$ (có phương và chiều trùng với độ dịch chuyển $\\vec{d}$).\n"
            "- **Vận tốc tức thời**: vận tốc trong khoảng thời gian $\\Delta t$ rất nhỏ tại một thời điểm đang xét.\n\n"
            "### 2. Tính tương đối của chuyển động – Công thức cộng vận tốc\n"
            "- Kí hiệu: $(1)$ là **vật chuyển động** (thuyền), $(2)$ là **hệ quy chiếu chuyển động** (dòng nước), $(3)$ là **hệ quy chiếu đứng yên** (bờ sông):\n"
            "  $$\\vec{v}_{13} = \\vec{v}_{12} + \\vec{v}_{23}$$\n"
            "  - **Cùng chiều** (thuyền xuôi dòng): $v_{13} = v_{12} + v_{23}$.\n"
            "  - **Ngược chiều** (thuyền ngược dòng, $v_{12} > v_{23}$): $v_{13} = v_{12} - v_{23}$.\n"
            "  - **Vuông góc** ($\\vec{v}_{12} \\perp \\vec{v}_{23}$): $v_{13} = \\sqrt{v_{12}^2 + v_{23}^2}$."
        ),
        formulas=[
            G(
                "Tốc độ, Vận tốc và Công thức cộng vận tốc",
                F("Tốc độ trung bình và Vận tốc trung bình", "$v_{\\text{tb}} = \\dfrac{s}{t} = \\dfrac{s_1 + s_2}{t_1 + t_2}; \\qquad \\vec{v} = \\dfrac{\\vec{d}}{t}$", "Chỉ khi vật chuyển động thẳng và không đổi chiều thì độ lớn vận tốc trung bình mới bằng tốc độ trung bình ($|v| = v_{\\text{tb}}$)."),
                F("Công thức cộng vận tốc", "$\\vec{v}_{13} = \\vec{v}_{12} + \\vec{v}_{23} \\implies \\begin{cases} \\text{Xuôi dòng: } v_{13} = v_{12} + v_{23} \\\\ \\text{Ngược dòng: } v_{13} = |v_{12} - v_{23}| \\\\ \\text{Vuông góc: } v_{13} = \\sqrt{v_{12}^2 + v_{23}^2} \\end{cases}$", "Trong đó $\\vec{v}_{13}$ là vận tốc tuyệt đối (so với bờ), $\\vec{v}_{12}$ là vận tốc tương đối (so với nước), $\\vec{v}_{23}$ là vận tốc kéo theo (của nước so với bờ)."),
            )
        ],
        example="Một chiếc thuyền máy chạy trên sông với vận tốc so với nước đứng yên là $v_{12} = 18\\text{ km/h}$. Nước sông chảy đều với vận tốc so với bờ là $v_{23} = 4\\text{ km/h}$. Tính vận tốc của thuyền so với bờ sông khi: (a) Thuyền chạy xuôi dòng; (b) Thuyền chạy ngược dòng.",
        example_answer="(a) Khi chạy xuôi dòng ($\\vec{v}_{12} \\uparrow\\uparrow \\vec{v}_{23}$): $v_{\\text{xuôi}} = v_{12} + v_{23} = 18 + 4 = 22\\text{ km/h}$. (b) Khi chạy ngược dòng ($\\vec{v}_{12} \\uparrow\\downarrow \\vec{v}_{23}$): $v_{\\text{ngược}} = v_{12} - v_{23} = 18 - 4 = 14\\text{ km/h}$.",
        real_life="Phi công lái máy bay và thuyền trưởng lái tàu biển luôn phải tính toán công thức cộng vận tốc với vận tốc gió hoặc dòng hải lưu để giữ đúng hướng bay và hải trình dự kiến.",
        quiz=[
            mcq("biet", "Đại lượng được xác định bằng thương số giữa độ dịch chuyển $\\vec{d}$ của vật và thời gian $\\Delta t$ thực hiện độ dịch chuyển đó được gọi là gì?", ["Vận tốc trung bình $\\vec{v} = \\dfrac{\\vec{d}}{\\Delta t}$", "Tốc độ trung bình $v_{\\text{tb}} = \\dfrac{s}{\\Delta t}$", "Gia tốc $a$", "Động lượng $p$"], 0, "Thương số giữa độ dịch chuyển $\\vec{d}$ và thời gian $\\Delta t$ là vận tốc trung bình $\\vec{v}$."),
            mcq("biet", "Biểu thức vectơ của công thức cộng vận tốc giữa vật $(1)$, hệ quy chiếu chuyển động $(2)$ và hệ quy chiếu đứng yên $(3)$ là gì?", ["$\\vec{v}_{13} = \\vec{v}_{12} + \\vec{v}_{23}$", "$\\vec{v}_{13} = \\vec{v}_{12} - \\vec{v}_{23}$", "$\\vec{v}_{13} = \\vec{v}_{12} \\cdot \\vec{v}_{23}$", "$v_{13} = v_{12} + v_{23}$ trong mọi trường hợp"], 0, "Công thức cộng vận tốc dạng tổng quát là $\\vec{v}_{13} = \\vec{v}_{12} + \\vec{v}_{23}$."),
            mcq("hieu", "Một ca nô có vận tốc đối với nước là $v_{12} = 15\\text{ km/h}$ chạy ngược dòng nước đang chảy với vận tốc $v_{23} = 3\\text{ km/h}$ đối với bờ. Vận tốc của ca nô đối với bờ là bao nhiêu?", ["$12\\text{ km/h}$", "$18\\text{ km/h}$", "$5\\text{ km/h}$", "$45\\text{ km/h}$"], 0, "Khi chạy ngược dòng, hai vectơ vận tốc ngược chiều nhau nên $v_{13} = v_{12} - v_{23} = 15 - 3 = 12\\text{ km/h}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tốc độ và vận tốc:", [
                "Tốc độ trung bình là đại lượng vô hướng, còn vận tốc trung bình là đại lượng vectơ.",
                "Số chỉ trên đồng hồ tốc kế trước mặt người lái xe máy cho biết độ lớn của vận tốc tức thời tại thời điểm đó.",
                "Một vật chạy một vòng tròn quay về điểm xuất phát trong $10\\text{ s}$ thì có cả tốc độ trung bình và vận tốc trung bình đều bằng $0$.",
                "Khi thuyền hướng mũi bơi vuông góc ngang qua dòng sông với $v_{12} = 3\\text{ m/s}$ và nước chảy $v_{23} = 4\\text{ m/s}$ thì độ lớn vận tốc thuyền so với bờ là $5\\text{ m/s}$.",
            ], [True, True, False, True], "Ý c) sai vì khi chạy hết một vòng tròn, quãng đường $s > 0$ nên tốc độ trung bình $v_{\\text{tb}} = \\dfrac{s}{t} > 0$, chỉ có vận tốc trung bình $\\vec{v} = \\dfrac{\\vec{d}}{t} = \\vec{0}$."),
            short("vandung", "Một người đi xe đạp đi nửa thời gian đầu với tốc độ $v_1 = 12\\text{ km/h}$ và nửa thời gian sau với tốc độ $v_2 = 16\\text{ km/h}$. Tốc độ trung bình của người đó trên cả quãng đường bằng bao nhiêu $\\text{km/h}$?", ["14"], "Khi đi trong hai khoảng thời gian bằng nhau ($t_1 = t_2 = \\dfrac{t}{2}$), tốc độ trung bình là $v_{\\text{tb}} = \\dfrac{v_1 + v_2}{2} = \\dfrac{12 + 16}{2} = 14\\text{ km/h}$.", unit="km/h"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 6: Đồ thị độ dịch chuyển – thời gian",
        icon="📉",
        description="Phương trình chuyển động thẳng đều x = x₀ + v.t, cách vẽ đồ thị độ dịch chuyển – thời gian (d – t) và ý nghĩa hệ số góc.",
        requirements=[
            "Viết được công thức độ dịch chuyển $d = v \\cdot t$ và phương trình tọa độ của chuyển động thẳng đều $x = x_0 + v \\cdot t$.",
            "Đọc được trạng thái chuyển động của vật (chuyển động thẳng đều theo chiều dương, theo chiều âm hoặc đứng yên) từ đồ thị độ dịch chuyển – thời gian ($d - t$).",
            "Tính được vận tốc $v$ (kể cả dấu) từ độ dốc (hệ số góc) của đường thẳng trên đồ thị $d - t$: $v = \\dfrac{d_2 - d_1}{t_2 - t_1}$.",
        ],
        definition="Trong chuyển động thẳng đều, độ dịch chuyển biến thiên bậc nhất theo thời gian ($d = v \\cdot t$ hay $x = x_0 + v \\cdot t$), nên đồ thị độ dịch chuyển – thời gian ($d - t$) là một đường thẳng có hệ số góc (độ dốc) bằng vận tốc $v = \\dfrac{d_2 - d_1}{t_2 - t_1}$.",
        theory=(
            "### 1. Chuyển động thẳng đều và phương trình tọa độ\n"
            "- **Chuyển động thẳng đều** là chuyển động có quỹ đạo là đường thẳng và có vận tốc không đổi theo thời gian.\n"
            "- Độ dịch chuyển: $d = v \\cdot t$.\n"
            "- Phương trình tọa độ trên trục $Ox$: $x = x_0 + d = x_0 + v \\cdot t$ (với $v > 0$ nếu vật đi theo chiều dương trục $Ox$, $v < 0$ nếu vật đi ngược chiều dương trục $Ox$).\n\n"
            "### 2. Đặc điểm đồ thị độ dịch chuyển – thời gian ($d - t$)\n"
            "- **Đoạn thẳng đi lên từ trái sang phải** ($d_2 > d_1$): vật chuyển động thẳng đều **theo chiều dương** ($v > 0$).\n"
            "- **Đoạn thẳng nằm ngang song song với trục $Ot$** ($d_2 = d_1$): vật **đứng yên** ($v = 0$).\n"
            "- **Đoạn thẳng đi xuống từ trái sang phải** ($d_2 < d_1$): vật chuyển động thẳng đều **theo chiều âm** (quay ngược về gốc, $v < 0$).\n"
            "- **Hệ số góc (độ dốc)**: $v = \\dfrac{\\Delta d}{\\Delta t} = \\dfrac{d_2 - d_1}{t_2 - t_1}$."
        ),
        formulas=[
            G(
                "Phương trình và Độ dốc đồ thị d - t",
                F("Độ dịch chuyển và phương trình chuyển động thẳng đều", "$d = v \\cdot t; \\qquad x = x_0 + v \\cdot t$", "Trong đó $x_0$ là tọa độ ban đầu lúc $t = 0$, $v$ là vận tốc đại số ($v > 0$ hoặc $v < 0$)."),
                F("Xác định vận tốc từ hệ số góc đồ thị d - t", "$v = \\dfrac{d_2 - d_1}{t_2 - t_1} = \\dfrac{x_2 - x_1}{t_2 - t_1}$", "Khác với đồ thị quãng đường $s - t$ (luôn không giảm), đồ thị độ dịch chuyển $d - t$ có thể dốc xuống khi vật quay đầu đi ngược chiều dương."),
            )
        ],
        example="Từ đồ thị độ dịch chuyển – thời gian ($d - t$) của một chất điểm chuyển động dọc theo trục $Ox$: tại $t_1 = 1\\text{ s}$ chất điểm có $d_1 = 20\\text{ m}$, đến $t_2 = 5\\text{ s}$ chất điểm có $d_2 = 4\\text{ m}$. Hãy tính vận tốc $v$ của chất điểm trong giai đoạn này và nêu chiều chuyển động.",
        example_answer="Vận tốc của chất điểm là $v = \\dfrac{d_2 - d_1}{t_2 - t_1} = \\dfrac{4 - 20}{5 - 1} = \\dfrac{-16}{4} = -4\\text{ m/s}$. Vì $v < 0$ nên chất điểm đang chuyển động thẳng đều theo chiều âm của trục $Ox$ với tốc độ $|v| = 4\\text{ m/s}$.",
        real_life="Cảm biến siêu âm nối với máy tính trong phòng thực hành Vật lí tự động vẽ đồ thị $d - t$ theo thời gian thực khi học sinh tiến lại gần hoặc lùi ra xa cảm biến.",
        quiz=[
            mcq("biet", "Hệ số góc (độ dốc) $\\dfrac{d_2 - d_1}{t_2 - t_1}$ của đường biểu diễn trên đồ thị độ dịch chuyển – thời gian ($d - t$) cho biết đại lượng vật lí nào?", ["Vận tốc $v$ của vật", "Gia tốc $a$ của vật", "Khối lượng $m$ của vật", "Lực tác dụng $F$ lên vật"], 0, "Độ dốc của đồ thị $d - t$ bằng thương số $\\dfrac{\\Delta d}{\\Delta t}$ chính là vận tốc $v$ của vật."),
            mcq("biet", "Trên đồ thị độ dịch chuyển – thời gian ($d - t$), đoạn thẳng dốc xuống từ trái sang phải ($d$ giảm dần theo $t$) biểu diễn chuyển động như thế nào?", ["Vật đang chuyển động thẳng đều theo chiều âm ($v < 0$)", "Vật đang đứng yên ($v = 0$)", "Vật đang chuyển động thẳng đều theo chiều dương ($v > 0$)", "Vật đang rơi tự do từ trên cao"], 0, "Khi đường thẳng trên đồ thị $d - t$ dốc xuống, $d_2 < d_1$ nên vận tốc $v = \\dfrac{d_2 - d_1}{t_2 - t_1} < 0$, tức vật đang đi ngược chiều dương."),
            mcq("hieu", "Một chất điểm chuyển động thẳng đều dọc theo trục $Ox$ có phương trình tọa độ $x = 15 - 5t$ (với $x$ tính bằng $\\text{m}$, $t$ tính bằng $\\text{s}$). Tọa độ ban đầu $x_0$ và vận tốc $v$ của chất điểm là:", ["$x_0 = 15\\text{ m}$ và $v = -5\\text{ m/s}$", "$x_0 = 15\\text{ m}$ và $v = 5\\text{ m/s}$", "$x_0 = -5\\text{ m}$ và $v = 15\\text{ m/s}$", "$x_0 = 10\\text{ m}$ và $v = -5\\text{ m/s}$"], 0, "Đối chiếu với $x = x_0 + v \\cdot t$, ta có $x_0 = 15\\text{ m}$ và $v = -5\\text{ m/s}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đồ thị độ dịch chuyển – thời gian ($d - t$):", [
                "Khi vật chuyển động thẳng đều theo chiều dương, đồ thị $d - t$ là đường thẳng đi lên.",
                "Khi vật đứng yên, đồ thị $d - t$ là đoạn thẳng song song với trục thời gian $Ot$.",
                "Đồ thị quãng đường – thời gian ($s - t$) cũng có thể đi xuống giống như đồ thị độ dịch chuyển – thời gian ($d - t$).",
                "Giao điểm của hai đường biểu diễn trên cùng đồ thị tọa độ – thời gian ($x - t$) cho biết thời điểm và vị trí hai vật gặp nhau.",
            ], [True, True, False, True], "Ý c) sai vì quãng đường $s$ chỉ có thể tăng hoặc giữ nguyên theo thời gian chứ không bao giờ giảm, còn độ dịch chuyển $d$ giảm khi vật quay đầu."),
            short("vandung", "Trên đồ thị độ dịch chuyển – thời gian của một xe chạy thẳng đều, tại $t_1 = 2\\text{ s}$ xe ở vị trí $d_1 = 10\\text{ m}$ và tại $t_2 = 6\\text{ s}$ xe ở vị trí $d_2 = 34\\text{ m}$. Vận tốc của xe bằng bao nhiêu $\\text{m/s}$?", ["6"], "Áp dụng công thức $v = \\dfrac{d_2 - d_1}{t_2 - t_1} = \\dfrac{34 - 10}{6 - 2} = \\dfrac{24}{4} = 6\\text{ m/s}$.", unit="m/s"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 7: Gia tốc và chuyển động thẳng biến đổi đều",
        icon="🏎️",
        description="Khái niệm gia tốc a = Δv/Δt (m/s²), phân biệt chuyển động thẳng nhanh dần đều (a.v > 0) và chậm dần đều (a.v < 0).",
        requirements=[
            "Định nghĩa được gia tốc là đại lượng vectơ đặc trưng cho độ biến thiên nhanh hay chậm của vận tốc: $a = \\dfrac{\\Delta v}{\\Delta t} = \\dfrac{v - v_0}{t - t_0}$ (đơn vị $\\text{m/s}^2$).",
            "Phân biệt được chuyển động thẳng nhanh dần đều ($\\vec{a}$ cùng chiều $\\vec{v}$, tức $a \\cdot v > 0$) và chuyển động thẳng chậm dần đều ($\\vec{a}$ ngược chiều $\\vec{v}$, tức $a \\cdot v < 0$).",
            "Đọc và tính được gia tốc của vật từ đồ thị vận tốc – thời gian ($v - t$).",
        ],
        definition="Gia tốc là đại lượng cho biết sự thay đổi nhanh hay chậm của vận tốc theo thời gian, được xác định bằng thương số giữa độ biến thiên vận tốc $\\Delta v$ và khoảng thời gian $\\Delta t$: $a = \\dfrac{\\Delta v}{\\Delta t} = \\dfrac{v - v_0}{\\Delta t}$ (đơn vị $\\text{m/s}^2$).",
        theory=(
            "### 1. Khái niệm Gia tốc\n"
            "- Biểu thức vectơ: $\\vec{a} = \\dfrac{\\Delta \\vec{v}}{\\Delta t} = \\dfrac{\\vec{v} - \\vec{v}_0}{t - t_0}$.\n"
            "- Biểu thức đại số (trên trục chuyển động): $a = \\dfrac{v - v_0}{\\Delta t}$, đơn vị trong hệ SI là **mét trên giây bình phương** ($\\text{m/s}^2$).\n\n"
            "### 2. Chuyển động thẳng biến đổi đều\n"
            "- Là chuyển động có quỹ đạo là đường thẳng và có độ lớn vận tốc tăng đều hoặc giảm đều theo thời gian (gia tốc $\\vec{a}$ là hằng số khác $\\vec{0}$):\n"
            "  - **Chuyển động thẳng nhanh dần đều**: độ lớn vận tốc tăng đều theo thời gian; vectơ gia tốc cùng chiều với vectơ vận tốc ($\\vec{a} \\uparrow\\uparrow \\vec{v} \\iff a \\cdot v > 0$).\n"
            "  - **Chuyển động thẳng chậm dần đều**: độ lớn vận tốc giảm đều theo thời gian; vectơ gia tốc ngược chiều với vectơ vận tốc ($\\vec{a} \\uparrow\\downarrow \\vec{v} \\iff a \\cdot v < 0$)."
        ),
        formulas=[
            G(
                "Gia tốc và Dấu của gia tốc",
                F("Công thức tính gia tốc", "$a = \\dfrac{\\Delta v}{\\Delta t} = \\dfrac{v - v_0}{t - t_0} \\implies v = v_0 + a\\Delta t$", "Trong đó $v_0, v$ phải đổi về cùng đơn vị $\\text{m/s}$, $\\Delta t$ tính bằng $\\text{s}$ thì $a$ có đơn vị $\\text{m/s}^2$."),
                F("Điều kiện nhanh dần đều và chậm dần đều", "$\\text{Nhanh dần đều: } \\vec{a} \\uparrow\\uparrow \\vec{v} \\ (a \\cdot v > 0); \\qquad \\text{Chậm dần đều: } \\vec{a} \\uparrow\\downarrow \\vec{v} \\ (a \\cdot v < 0)$", "Trong chuyển động thẳng đều ($v = \\text{const}$) thì gia tốc bằng không ($a = 0$)."),
            )
        ],
        example="Một đoàn tàu đang chạy thẳng với vận tốc $v_0 = 54\\text{ km/h}$ thì hãm phanh chuyển động thẳng chậm dần đều và sau $\\Delta t = 10\\text{ s}$ vận tốc giảm xuống còn $v = 18\\text{ km/h}$. Chọn chiều dương là chiều chuyển động của tàu, hãy tính gia tốc $a$ của đoàn tàu.",
        example_answer="Đổi đơn vị: $v_0 = \\dfrac{54}{3{,}6} = 15\\text{ m/s}$ và $v = \\dfrac{18}{3{,}6} = 5\\text{ m/s}$. Gia tốc của đoàn tàu là $a = \\dfrac{v - v_0}{\\Delta t} = \\dfrac{5 - 15}{10} = -1\\text{ m/s}^2$ (dấu âm chứng tỏ $\\vec{a}$ ngược chiều chuyển động).",
        real_life="Thông số khả năng tăng tốc của các dòng xe ô tô thể thao thường được công bố theo thời gian tăng tốc từ $0$ lên $100\\text{ km/h}$ (ví dụ trong $3{,}5\\text{ s}$, ứng với gia tốc rất lớn gần $8\\text{ m/s}^2$).",
        quiz=[
            mcq("biet", "Đơn vị của gia tốc trong hệ thống đo lường quốc tế SI là gì?", ["$\\text{m/s}^2$", "$\\text{m/s}$", "$\\text{m}\\cdot\\text{s}^2$", "$\\text{km/h}$"], 0, "Vì $a = \\dfrac{\\Delta v}{\\Delta t}$ với $\\Delta v$ tính bằng $\\text{m/s}$ và $\\Delta t$ tính bằng $\\text{s}$ nên đơn vị gia tốc là $\\text{m/s}^2$."),
            mcq("biet", "Trong chuyển động thẳng **chậm dần đều**, mối quan hệ về chiều và dấu giữa vectơ gia tốc $\\vec{a}$ và vectơ vận tốc $\\vec{v}$ là gì?", ["$\\vec{a}$ luôn ngược chiều với $\\vec{v}$ ($a \\cdot v < 0$)", "$\\vec{a}$ luôn cùng chiều với $\\vec{v}$ ($a \\cdot v > 0$)", "$\\vec{a}$ luôn vuông góc với $\\vec{v}$", "Gia tốc luôn bằng $0$ ($a = 0$)"], 0, "Trong chuyển động thẳng chậm dần đều, vận tốc giảm dần nên gia tốc $\\vec{a}$ luôn ngược chiều với vận tốc $\\vec{v}$ ($a \\cdot v < 0$)."),
            mcq("hieu", "Một ô tô khởi hành từ trạng thái đứng yên ($v_0 = 0$), sau $5\\text{ s}$ đạt vận tốc $10\\text{ m/s}$. Gia tốc của ô tô trong thời gian đó bằng bao nhiêu?", ["$2\\text{ m/s}^2$", "$50\\text{ m/s}^2$", "$0{,}5\\text{ m/s}^2$", "$5\\text{ m/s}^2$"], 0, "Ta có $a = \\dfrac{v - v_0}{t} = \\dfrac{10 - 0}{5} = 2\\text{ m/s}^2$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về gia tốc và chuyển động biến đổi đều:", [
                "Gia tốc đặc trưng cho sự biến thiên nhanh hay chậm của vận tốc.",
                "Khi vật chuyển động thẳng đều thì gia tốc của vật bằng $0$.",
                "Cứ gia tốc mang dấu âm ($a < 0$) thì chuyển động chắc chắn là chậm dần đều.",
                "Trên đồ thị vận tốc – thời gian ($v - t$), độ dốc của đường thẳng biểu diễn chính là gia tốc $a$.",
            ], [True, True, False, True], "Ý c) sai vì nếu vật chuyển động theo chiều âm ($v < 0$) mà có $a < 0$ thì $a \\cdot v > 0$, vật lại đang chuyển động nhanh dần đều theo chiều âm."),
            short("vandung", "Một xe máy đang chạy với vận tốc $v_0 = 4\\text{ m/s}$ thì tăng tốc chuyển động thẳng nhanh dần đều, sau $t = 4\\text{ s}$ đạt vận tốc $v = 12\\text{ m/s}$. Gia tốc của xe máy bằng bao nhiêu $\\text{m/s}^2$?", ["2"], "Áp dụng công thức $a = \\dfrac{v - v_0}{t} = \\dfrac{12 - 4}{4} = 2\\text{ m/s}^2$.", unit="m/s²"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 8: Các công thức của chuyển động thẳng biến đổi đều",
        icon="🧮",
        description="Bộ 4 công thức cơ bản của chuyển động thẳng biến đổi đều và ý nghĩa diện tích dưới đồ thị vận tốc – thời gian (v – t).",
        requirements=[
            "Viết và vận dụng được công thức vận tốc $v = v_0 + at$ và công thức độ dịch chuyển $d = \\dfrac{v_0 + v}{2}t = v_0 t + \\dfrac{1}{2}at^2$.",
            "Viết và vận dụng được hệ thức độc lập với thời gian $v^2 - v_0^2 = 2ad$ để giải các bài toán không cho trước thời gian $t$.",
            "Tính được độ dịch chuyển của vật bằng diện tích hình thang (hoặc tam giác) giới hạn bởi đồ thị $v - t$ và trục thời gian.",
        ],
        definition="Trong chuyển động thẳng biến đổi đều với vận tốc đầu $v_0$ và gia tốc không đổi $a$, vận tốc và độ dịch chuyển tại thời điểm $t$ được xác định bởi hệ công thức: $v = v_0 + at$, $d = v_0 t + \\dfrac{1}{2}at^2$ và $v^2 - v_0^2 = 2ad$.",
        theory=(
            "### 1. Bộ 4 công thức của chuyển động thẳng biến đổi đều (chọn $t_0 = 0$)\n"
            "1. **Công thức vận tốc**: $v = v_0 + a \\cdot t$.\n"
            "2. **Độ dịch chuyển theo vận tốc trung bình**: $d = v_{\\text{tb}} \\cdot t = \\dfrac{v_0 + v}{2} \\cdot t$.\n"
            "3. **Công thức độ dịch chuyển theo thời gian**: $d = v_0 t + \\dfrac{1}{2}at^2$ (phương trình tọa độ: $x = x_0 + v_0 t + \\dfrac{1}{2}at^2$).\n"
            "4. **Hệ thức độc lập với thời gian**:\n"
            "   $$v^2 - v_0^2 = 2ad$$\n\n"
            "### 2. Tính độ dịch chuyển từ đồ thị $v - t$\n"
            "- Trên đồ thị vận tốc – thời gian ($v - t$), **diện tích hình phẳng** giới hạn bởi đường biểu diễn $v(t)$, trục hoành $Ot$ và hai đường thẳng đứng $t = 0, t = t_1$ bằng độ dịch chuyển $d$ của vật."
        ),
        formulas=[
            G(
                "Bộ công thức chuyển động thẳng biến đổi đều",
                F("Vận tốc và Độ dịch chuyển theo thời gian t", "$v = v_0 + at; \\qquad d = v_0 t + \\dfrac{1}{2}at^2 = \\dfrac{v_0 + v}{2}t$", "Nếu vật chuyển động thẳng không đổi chiều thì quãng đường $s = |d|$."),
                F("Hệ thức độc lập với thời gian", "$v^2 - v_0^2 = 2ad \\implies d = \\dfrac{v^2 - v_0^2}{2a}$", "Khi xe phanh dừng lại hẳn thì vận tốc cuối $v = 0$, quãng đường hãm phanh là $s_{\\text{dừng}} = \\dfrac{-v_0^2}{2a}$."),
            )
        ],
        example="Một ô tô đang chạy với vận tốc $v_0 = 20\\text{ m/s}$ thì người lái xe đạp phanh, xe chuyển động thẳng chậm dần đều với gia tốc $a = -4\\text{ m/s}^2$ cho đến khi dừng hẳn. Hãy tính quãng đường ô tô đi thêm được kể từ lúc bắt đầu hãm phanh đến khi dừng hẳn.",
        example_answer="Khi xe dừng hẳn thì vận tốc cuối là $v = 0\\text{ m/s}$. Áp dụng hệ thức độc lập thời gian $v^2 - v_0^2 = 2ad$, ta có: $d = \\dfrac{v^2 - v_0^2}{2a} = \\dfrac{0^2 - 20^2}{2 \\cdot (-4)} = \\dfrac{-400}{-8} = 50\\text{ m}$.",
        real_life="Cảnh sát điều tra tai nạn giao thông đo chiều dài vết trượt lốp phanh $d$ trên mặt đường nhựa để tính ngược ra tốc độ ban đầu $v_0 = \\sqrt{-2ad}$ của xe trước khi phanh.",
        quiz=[
            mcq("biet", "Trong chuyển động thẳng biến đổi đều, hệ thức liên hệ giữa vận tốc đầu $v_0$, vận tốc sau $v$, gia tốc $a$ và độ dịch chuyển $d$ (không phụ thuộc thời gian $t$) là gì?", ["$v^2 - v_0^2 = 2ad$", "$v - v_0 = 2ad$", "$v^2 + v_0^2 = 2ad$", "$v^2 - v_0^2 = ad$"], 0, "Hệ thức độc lập với thời gian trong chuyển động thẳng biến đổi đều là $v^2 - v_0^2 = 2ad$."),
            mcq("biet", "Công thức tính độ dịch chuyển $d$ theo thời gian $t$ của chuyển động thẳng biến đổi đều có vận tốc ban đầu $v_0$ và gia tốc $a$ là gì?", ["$d = v_0 t + \\dfrac{1}{2}at^2$", "$d = v_0 t + at^2$", "$d = v_0 + \\dfrac{1}{2}at^2$", "$d = \\dfrac{1}{2}v_0 t^2 + at$"], 0, "Độ dịch chuyển của chuyển động thẳng biến đổi đều là $d = v_0 t + \\dfrac{1}{2}at^2$."),
            mcq("hieu", "Một chất điểm bắt đầu chuyển động nhanh dần đều từ trạng thái đứng yên ($v_0 = 0$) với gia tốc $a = 2\\text{ m/s}^2$. Sau thời gian $t = 4\\text{ s}$, quãng đường chất điểm đi được là bao nhiêu?", ["$16\\text{ m}$", "$8\\text{ m}$", "$32\\text{ m}$", "$4\\text{ m}$"], 0, "Vì $v_0 = 0$ nên $s = d = \\dfrac{1}{2}at^2 = \\dfrac{1}{2} \\cdot 2 \\cdot 4^2 = 16\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về công thức chuyển động thẳng biến đổi đều:", [
                "Trong chuyển động thẳng biến đổi đều, độ dịch chuyển $d$ là hàm bậc hai đối với thời gian $t$.",
                "Diện tích giới hạn dưới đường biểu diễn trên đồ thị vận tốc – thời gian ($v - t$) cho biết độ dịch chuyển của vật.",
                "Một vật có phương trình tọa độ $x = 4 + 6t + 2t^2\\text{ (m)}$ có vận tốc ban đầu $v_0 = 6\\text{ m/s}$ và gia tốc $a = 2\\text{ m/s}^2$.",
                "Khi vật hãm phanh dừng lại hẳn thì vận tốc cuối cùng bằng $0$ ($v = 0$).",
            ], [True, True, False, True], "Ý c) sai vì đối chiếu với $x = x_0 + v_0 t + \\dfrac{1}{2}at^2$, hệ số của $t^2$ là $\\dfrac{1}{2}a = 2 \\implies a = 4\\text{ m/s}^2$."),
            short("vandung", "Một đoàn tàu bắt đầu rời ga ($v_0 = 0$) chuyển động thẳng nhanh dần đều với gia tốc $a = 1\\text{ m/s}^2$. Sau khi đi được quãng đường $d = 50\\text{ m}$ thì vận tốc của đoàn tàu đạt bao nhiêu $\\text{m/s}$?", ["10"], "Áp dụng công thức $v^2 - v_0^2 = 2ad \\implies v = \\sqrt{2 \\cdot 1 \\cdot 50} = \\sqrt{100} = 10\\text{ m/s}$.", unit="m/s"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 9: Sự rơi tự do",
        icon="🍏",
        description="Định nghĩa sự rơi tự do, đặc điểm của chuyển động rơi tự do, gia tốc rơi tự do g và bộ công thức rơi tự do.",
        requirements=[
            "Định nghĩa được sự rơi tự do là sự rơi chỉ dưới tác dụng của trọng lực (bỏ qua sức cản của không khí).",
            "Nêu được các đặc điểm của chuyển động rơi tự do: phương thẳng đứng, chiều từ trên xuống dưới, là chuyển động thẳng nhanh dần đều với $v_0 = 0$ và gia tốc $a = g \\approx 9{,}8\\text{ m/s}^2$.",
            "Vận dụng được các công thức rơi tự do: $v = gt$, $h = s = \\dfrac{1}{2}gt^2$, $v = \\sqrt{2gh}$ và $t = \\sqrt{\\dfrac{2h}{g}}$.",
        ],
        definition="Sự rơi tự do là sự rơi của các vật trong không gian chỉ chịu tác dụng của trọng lực (trong chân không hoặc khi lực cản của không khí không đáng kể so với trọng lực). Chuyển động rơi tự do là chuyển động thẳng nhanh dần đều theo phương thẳng đứng từ trên xuống với gia tốc rơi tự do $g$.",
        theory=(
            "### 1. Sự rơi trong không khí và Sự rơi tự do\n"
            "- Trong không khí, các vật rơi nhanh chậm khác nhau là do **lực cản của không khí** tác dụng lên chúng khác nhau (không phải do vật nặng hay nhẹ).\n"
            "- Trong ống chân không (ống Newton), mọi vật dù nặng hay nhẹ (viên bi chì và chiếc lông chim) đều **rơi nhanh như nhau**.\n\n"
            "### 2. Đặc điểm và Công thức của chuyển động rơi tự do\n"
            "- **Phương**: thẳng đứng (phương của dây dọi). **Chiều**: từ trên xuống dưới.\n"
            "- **Tính chất**: chuyển động thẳng nhanh dần đều với vận tốc đầu $v_0 = 0$ và gia tốc $a = g$ (tại cùng một nơi trên Trái Đất, mọi vật rơi tự do với cùng gia tốc $g \\approx 9{,}8\\text{ m/s}^2$ hoặc lấy tròn $g = 10\\text{ m/s}^2$).\n"
            "- **Các công thức** (thả rơi từ độ cao $h$ tại thời điểm $t = 0$):\n"
            "  $$v = g \\cdot t; \\qquad s = h = \\dfrac{1}{2}gt^2 \\implies t = \\sqrt{\\dfrac{2h}{g}}; \\qquad v^2 = 2gh \\implies v = \\sqrt{2gh}$$"
        ),
        formulas=[
            G(
                "Bộ công thức của sự rơi tự do",
                F("Vận tốc và Quãng đường rơi sau thời gian t", "$v = g \\cdot t; \\qquad s = \\dfrac{1}{2}gt^2$", "Trong đó $g \\approx 9{,}8\\text{ m/s}^2$ (hoặc $10\\text{ m/s}^2$) là gia tốc rơi tự do."),
                F("Thời gian rơi và Vận tốc chạm đất từ độ cao h", "$t = \\sqrt{\\dfrac{2h}{g}}; \\qquad v = \\sqrt{2gh}$", "Thời gian rơi và vận tốc chạm đất chỉ phụ thuộc độ cao $h$ và gia tốc $g$, không phụ thuộc khối lượng $m$ của vật."),
            )
        ],
        example="Một hòn đá được thả rơi tự do từ miệng một vực sâu xuống đáy vực. Sau thời gian $t = 3\\text{ s}$ kể từ lúc thả thì hòn đá chạm đáy vực. Lấy $g = 10\\text{ m/s}^2$, hãy tính độ sâu $h$ của vực và vận tốc $v$ của hòn đá ngay khi chạm đáy.",
        example_answer="Độ sâu của vực bằng quãng đường hòn đá rơi trong $3\\text{ s}$: $h = \\dfrac{1}{2}gt^2 = \\dfrac{1}{2} \\cdot 10 \\cdot 3^2 = 45\\text{ m}$. Vận tốc của hòn đá ngay khi chạm đáy là $v = g \\cdot t = 10 \\cdot 3 = 30\\text{ m/s}$.",
        real_life="Các tháp thử nghiệm vi trọng lực (Drop Tower) thả rơi tự do các khoang thí nghiệm trong ống chân không cao hàng trăm mét để mô phỏng trạng thái không trọng lượng trên trạm vũ trụ.",
        quiz=[
            mcq("biet", "Sự rơi tự do là sự rơi của vật khi nào?", ["Khi vật chỉ chịu tác dụng của trọng lực (bỏ qua sức cản của không khí)", "Khi vật rơi trong nước biển", "Khi vận động viên nhảy dù đã bung dù lớn", "Khi chiếc lá khô bay lượn trong gió mạnh"], 0, "Sự rơi tự do là sự rơi chỉ dưới tác dụng của trọng lực."),
            mcq("biet", "Khi thả một vật rơi tự do từ độ cao $h$ (với $v_0 = 0$), công thức tính vận tốc $v$ của vật ngay trước khi chạm đất theo $g$ và $h$ là gì?", ["$v = \\sqrt{2gh}$", "$v = 2gh$", "$v = \\sqrt{gh}$", "$v = \\dfrac{1}{2}gh^2$"], 0, "Từ hệ thức $v^2 - v_0^2 = 2gh$ với $v_0 = 0$, ta có $v = \\sqrt{2gh}$."),
            mcq("hieu", "Trong một ống thủy tinh đã hút hết không khí (chân không), nếu thả rơi đồng thời một viên bi sắt nặng $50\\text{ g}$ và một chiếc lông chim nhẹ $0{,}5\\text{ g}$ từ cùng một độ cao thì hiện tượng gì xảy ra?", ["Viên bi sắt và chiếc lông chim rơi nhanh như nhau và chạm đáy ống cùng một lúc", "Viên bi sắt rơi nhanh gấp $100$ lần chiếc lông chim", "Chiếc lông chim lơ lửng không rơi xuống", "Chiếc lông chim chạm đáy trước viên bi sắt"], 0, "Trong chân không, mọi vật dù nặng hay nhẹ đều rơi tự do với cùng một gia tốc $g$ nên chạm đáy cùng một lúc."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự rơi tự do:", [
                "Chuyển động rơi tự do là chuyển động thẳng nhanh dần đều có phương thẳng đứng, chiều từ trên xuống.",
                "Trong không khí, tờ giấy vo tròn rơi nhanh hơn tờ giấy để phẳng là vì tờ giấy vo tròn chịu lực cản không khí nhỏ hơn.",
                "Thời gian rơi tự do của một vật từ độ cao $h$ tỉ lệ thuận với khối lượng $m$ của vật đó.",
                "Lấy $g = 10\\text{ m/s}^2$, một vật rơi tự do trong $2\\text{ s}$ đi được quãng đường là $20\\text{ m}$.",
            ], [True, True, False, True], "Ý c) sai vì thời gian rơi tự do $t = \\sqrt{\\dfrac{2h}{g}}$ không phụ thuộc vào khối lượng $m$ của vật."),
            short("vandung", "Thả một vật rơi tự do từ độ cao $h = 80\\text{ m}$ xuống mặt đất tại nơi có gia tốc rơi tự do $g = 10\\text{ m/s}^2$. Thời gian từ lúc thả đến lúc vật chạm đất bằng bao nhiêu giây ($\\text{s}$)?", ["4"], "Áp dụng công thức $t = \\sqrt{\\dfrac{2h}{g}} = \\sqrt{\\dfrac{2 \\cdot 80}{10}} = \\sqrt{16} = 4\\text{ s}$.", unit="s"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 10: Chuyển động ném",
        icon="🏀",
        description="Phân tích chuyển động ném ngang thành hai chuyển động thành phần vuông góc, công thức thời gian rơi và tầm bay xa L = v₀.√(2h/g).",
        requirements=[
            "Phân tích được chuyển động ném ngang từ độ cao $h$ với vận tốc đầu $v_0$ thành hai chuyển động độc lập: chuyển động thẳng đều theo phương ngang ($x = v_0 t$) và rơi tự do theo phương thẳng đứng ($y = \\dfrac{1}{2}gt^2$).",
            "Viết và vận dụng được công thức tính thời gian rơi $t = \\sqrt{\\dfrac{2h}{g}}$ và tầm bay xa $L = v_0 \\cdot t = v_0 \\sqrt{\\dfrac{2h}{g}}$ của vật ném ngang.",
            "Nêu được quỹ đạo của vật ném ngang là một nhánh parabol và nhận biết sơ lược chuyển động ném xiên.",
        ],
        definition="Chuyển động của vật bị ném ngang từ độ cao $h$ với vận tốc đầu $v_0$ (bỏ qua sức cản không khí) là tổng hợp của hai chuyển động thành phần độc lập: chuyển động thẳng đều theo phương nằm ngang với vận tốc $v_0$ và chuyển động rơi tự do theo phương thẳng đứng với gia tốc $g$.",
        theory=(
            "### 1. Phân tích chuyển động ném ngang\n"
            "- Chọn hệ trục tọa độ $Oxy$ tại vị trí ném $O$: trục $Ox$ nằm ngang cùng chiều $\\vec{v}_0$, trục $Oy$ thẳng đứng hướng xuống:\n"
            "  - **Theo phương ngang $Ox$** (không có lực tác dụng): chuyển động thẳng đều với $v_x = v_0$ và tọa độ $x = v_0 \\cdot t$.\n"
            "  - **Theo phương thẳng đứng $Oy$** (chỉ chịu trọng lực): chuyển động rơi tự do với $v_y = g \\cdot t$ và tọa độ $y = \\dfrac{1}{2}gt^2$.\n"
            "- **Phương trình quỹ đạo**: Khử $t = \\dfrac{x}{v_0}$ ta được $y = \\dfrac{g}{2v_0^2}x^2$ (một **nhánh parabol** có đỉnh tại $O$).\n\n"
            "### 2. Thời gian chuyển động và Tầm bay xa\n"
            "- **Thời gian chạm đất**: chỉ phụ thuộc độ cao $h$, bằng đúng thời gian rơi tự do từ độ cao $h$:\n"
            "  $$t = \\sqrt{\\dfrac{2h}{g}}$$\n"
            "- **Tầm bay xa theo phương ngang ($L$)**:\n"
            "  $$L = x_{\\max} = v_0 \\cdot t = v_0 \\sqrt{\\dfrac{2h}{g}}$$\n"
            "- **Vận tốc của vật tại thời điểm $t$**: $v = \\sqrt{v_x^2 + v_y^2} = \\sqrt{v_0^2 + (gt)^2} = \\sqrt{v_0^2 + 2gh}$."
        ),
        formulas=[
            G(
                "Các công thức của chuyển động ném ngang",
                F("Thời gian rơi và Tầm bay xa của vật ném ngang", "$t = \\sqrt{\\dfrac{2h}{g}}; \\qquad L = v_0 \\cdot t = v_0 \\sqrt{\\dfrac{2h}{g}}$", "Thời gian rơi $t$ của vật ném ngang chỉ phụ thuộc độ cao $h$, không phụ thuộc vận tốc ném $v_0$."),
                F("Phương trình quỹ đạo và Vận tốc chạm đất", "$y = \\dfrac{g}{2v_0^2}x^2; \\qquad v_{\\text{chạm đất}} = \\sqrt{v_0^2 + (gt)^2} = \\sqrt{v_0^2 + 2gh}$", "Quỹ đạo của chuyển động ném ngang là một nhánh đường parabol."),
            )
        ],
        example="Từ độ cao $h = 20\\text{ m}$ so với mặt đất, một vật được ném theo phương nằm ngang với vận tốc ban đầu $v_0 = 15\\text{ m/s}$ (lấy $g = 10\\text{ m/s}^2$, bỏ qua sức cản không khí). Hãy tính thời gian chuyển động $t$ và tầm bay xa $L$ của vật trên mặt đất.",
        example_answer="Thời gian từ lúc ném đến khi chạm đất là $t = \\sqrt{\\dfrac{2h}{g}} = \\sqrt{\\dfrac{2 \\cdot 20}{10}} = 2\\text{ s}$. Tầm bay xa theo phương ngang của vật là $L = v_0 \\cdot t = 15 \\cdot 2 = 30\\text{ m}$.",
        real_life="Máy bay cứu trợ bay ngang ở độ cao $h$ với vận tốc $v_0$ phải thả kiện hàng cứu trợ từ vị trí cách điểm đích một khoảng ngang $L = v_0 \\sqrt{\\dfrac{2h}{g}}$ để kiện hàng rơi trúng bãi tập kết.",
        quiz=[
            mcq("biet", "Bỏ qua sức cản của không khí, quỹ đạo chuyển động của một vật được ném theo phương nằm ngang là đường gì?", ["Một nhánh parabol", "Một đường thẳng xiên góc", "Một đường tròn", "Một đường thẳng đứng"], 0, "Vì $y = \\dfrac{g}{2v_0^2}x^2$ nên quỹ đạo của vật ném ngang là một nhánh parabol."),
            mcq("biet", "Một vật được ném ngang từ độ cao $h$ với vận tốc đầu $v_0$ tại nơi có gia tốc rơi tự do $g$. Công thức tính tầm bay xa $L$ của vật là gì?", ["$L = v_0 \\sqrt{\\dfrac{2h}{g}}$", "$L = v_0 \\cdot \\dfrac{2h}{g}$", "$L = v_0 \\sqrt{\\dfrac{h}{2g}}$", "$L = \\dfrac{1}{2}gt^2$"], 0, "Tầm bay xa của vật ném ngang là $L = v_0 \\cdot t = v_0 \\sqrt{\\dfrac{2h}{g}}$."),
            mcq("hieu", "Ở cùng một độ cao $h$, viên bi $A$ được thả rơi tự do đồng thời cùng lúc với viên bi $B$ được ném theo phương nằm ngang với vận tốc $v_0 = 10\\text{ m/s}$ (bỏ qua sức cản không khí). Nhận xét nào sau đây là đúng?", ["Hai viên bi $A$ và $B$ chạm mặt đất phẳng ngang cùng một lúc", "Viên bi $A$ chạm đất trước viên bi $B$", "Viên bi $B$ chạm đất trước viên bi $A$", "Viên bi $B$ bay mãi không chạm đất"], 0, "Chuyển động theo phương thẳng đứng của viên bi $B$ cũng là rơi tự do từ độ cao $h$, nên thời gian rơi $t = \\sqrt{\\dfrac{2h}{g}}$ của hai bi hoàn toàn bằng nhau."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về chuyển động ném ngang:", [
                "Hình chiếu chuyển động của vật ném ngang trên phương nằm ngang là chuyển động thẳng đều với vận tốc $v_0$.",
                "Hình chiếu chuyển động của vật ném ngang trên phương thẳng đứng là chuyển động rơi tự do.",
                "Nếu giữ nguyên độ cao $h$ và tăng vận tốc ném ngang $v_0$ lên gấp đôi thì thời gian rơi đến lúc chạm đất cũng tăng gấp đôi.",
                "Nếu giữ nguyên độ cao $h$ và tăng vận tốc ném ngang $v_0$ lên gấp đôi thì tầm bay xa $L$ tăng gấp đôi.",
            ], [True, True, False, True], "Ý c) sai vì thời gian rơi $t = \\sqrt{\\dfrac{2h}{g}}$ chỉ phụ thuộc vào độ cao $h$, không phụ thuộc vào vận tốc ném ngang $v_0$."),
            short("vandung", "Một quả bóng được ném theo phương nằm ngang từ độ cao $h = 45\\text{ m}$ với vận tốc đầu $v_0 = 12\\text{ m/s}$. Lấy $g = 10\\text{ m/s}^2$, tầm bay xa $L$ của quả bóng theo phương ngang bằng bao nhiêu mét ($\\text{m}$)?", ["36"], "Thời gian rơi là $t = \\sqrt{\\dfrac{2h}{g}} = \\sqrt{\\dfrac{90}{10}} = 3\\text{ s}$. Tầm bay xa là $L = v_0 \\cdot t = 12 \\cdot 3 = 36\\text{ m}$.", unit="m"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 11: Tổng hợp và phân tích lực. Cân bằng lực",
        icon="📐",
        description="Khái niệm hợp lực, quy tắc hình bình hành, điều kiện cân bằng của chất điểm và cách phân tích lực.",
        requirements=[
            "Phát biểu được quy tắc hình bình hành để tổng hợp hai lực đồng quy: $\\vec{F} = \\vec{F}_1 + \\vec{F}_2$ và tính độ lớn $F = \\sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \\cos\\alpha}$.",
            "Vận dụng được các trường hợp đặc biệt của hai lực đồng quy (cùng chiều, ngược chiều, vuông góc) và điều kiện $|F_1 - F_2| \\le F \\le F_1 + F_2$.",
            "Nêu được điều kiện cân bằng của một vật (chất điểm) là hợp lực của tất cả các lực tác dụng lên vật bằng không ($\\sum \\vec{F} = \\vec{0}$).",
        ],
        definition="Tổng hợp lực là phép thay thế các lực tác dụng đồng thời vào cùng một vật bằng một lực có tác dụng giống hệt như các lực ấy; lực thay thế đó gọi là hợp lực ($\\vec{F} = \\vec{F}_1 + \\vec{F}_2 + \\dots$). Điều kiện cân bằng của chất điểm là hợp lực tác dụng lên nó bằng không ($\\vec{F} = \\vec{0}$).",
        theory=(
            "### 1. Quy tắc hình bình hành và độ lớn hợp lực\n"
            "- Nếu hai lực đồng quy $\\vec{F}_1, \\vec{F}_2$ làm thành hai cạnh của một hình bình hành thì đường chéo kẻ từ điểm đồng quy biểu diễn hợp lực $\\vec{F} = \\vec{F}_1 + \\vec{F}_2$:\n"
            "  $$F = \\sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \\cos\\alpha}$$\n"
            "- **Các trường hợp đặc biệt**:\n"
            "  - Cùng phương, cùng chiều ($\\alpha = 0^\\circ$): $F = F_{\\max} = F_1 + F_2$.\n"
            "  - Cùng phương, ngược chiều ($\\alpha = 180^\\circ$): $F = F_{\\min} = |F_1 - F_2|$.\n"
            "  - Vuông góc nhau ($\\alpha = 90^\\circ$): $F = \\sqrt{F_1^2 + F_2^2}$.\n"
            "  - Với mọi góc $\\alpha$: $|F_1 - F_2| \\le F \\le F_1 + F_2$.\n\n"
            "### 2. Cân bằng lực và Phân tích lực\n"
            "- **Hai lực cân bằng**: cùng tác dụng vào một vật, cùng giá, ngược chiều và có cùng độ lớn ($\\vec{F}_1 + \\vec{F}_2 = \\vec{0} \\iff \\vec{F}_1 = -\\vec{F}_2$).\n"
            "- **Phân tích lực**: phép thay thế một lực thành hai lực thành phần theo hai phương có tác dụng thực tế (ví dụ trên mặt phẳng nghiêng góc $\\alpha$, trọng lực $\\vec{P}$ phân tích thành $P_t = P\\sin\\alpha$ và $P_n = P\\cos\\alpha$)."
        ),
        formulas=[
            G(
                "Công thức tổng hợp hai lực đồng quy và Cân bằng lực",
                F("Độ lớn hợp lực của hai lực đồng quy hợp góc α", "$F = \\sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \\cos\\alpha}; \\qquad |F_1 - F_2| \\le F \\le F_1 + F_2$", "Khi $\\alpha = 0^\\circ \\implies F = F_1 + F_2$; khi $\\alpha = 180^\\circ \\implies F = |F_1 - F_2|$; khi $\\alpha = 90^\\circ \\implies F = \\sqrt{F_1^2 + F_2^2}$."),
                F("Điều kiện cân bằng của chất điểm", "$\\vec{F}_{\\text{hl}} = \\vec{F}_1 + \\vec{F}_2 + \\dots + \\vec{F}_n = \\vec{0}$", "Nếu vật cân bằng dưới tác dụng của 3 lực không song song thì hợp của 2 lực bất kì phải cân bằng với lực thứ ba: $\\vec{F}_1 + \\vec{F}_2 = -\\vec{F}_3$."),
            )
        ],
        example="Hai lực đồng quy $\\vec{F}_1$ và $\\vec{F}_2$ có độ lớn lần lượt là $F_1 = 9\\text{ N}$ và $F_2 = 12\\text{ N}$ tác dụng vào cùng một vật theo hai phương vuông góc với nhau ($\\alpha = 90^\\circ$). Hãy tính độ lớn hợp lực $F$ của hai lực đó.",
        example_answer="Vì hai lực vuông góc với nhau ($\\alpha = 90^\\circ$) nên độ lớn hợp lực là $F = \\sqrt{F_1^2 + F_2^2} = \\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15\\text{ N}$.",
        real_life="Hai tàu kéo cùng dùng dây cáp kéo một chiếc sà lan lớn đi dọc theo luồng kênh chính là ứng dụng thực tế của quy tắc hình bình hành tổng hợp hai lực đồng quy.",
        quiz=[
            mcq("biet", "Cho hai lực đồng quy có độ lớn $F_1$ và $F_2$. Độ lớn hợp lực $F$ của chúng luôn thỏa mãn bất đẳng thức nào sau đây?", ["$|F_1 - F_2| \\le F \\le F_1 + F_2$", "$F = F_1 + F_2$ trong mọi trường hợp", "$F > F_1 + F_2$", "$F < |F_1 - F_2|$"], 0, "Độ lớn hợp lực của hai lực đồng quy luôn nằm trong đoạn từ $|F_1 - F_2|$ đến $F_1 + F_2$."),
            mcq("biet", "Điều kiện để một vật (coi là chất điểm) đứng cân bằng là gì?", ["Hợp lực của tất cả các lực tác dụng lên vật bằng không ($\\sum \\vec{F} = \\vec{0}$)", "Không có bất kì lực nào tồn tại trong vũ trụ", "Các lực tác dụng lên vật phải cùng phương cùng chiều", "Khối lượng của vật phải bằng $0$"], 0, "Chất điểm cân bằng khi hợp lực của tất cả các lực tác dụng lên nó bằng $\\vec{0}$."),
            mcq("hieu", "Cho hai lực đồng quy có độ lớn $F_1 = 7\\text{ N}$ và $F_2 = 13\\text{ N}$. Giá trị nào sau đây **không thể** là độ lớn hợp lực của hai lực này?", ["$22\\text{ N}$", "$6\\text{ N}$", "$15\\text{ N}$", "$20\\text{ N}$"], 0, "Ta có $|7 - 13| \\le F \\le 7 + 13 \\iff 6\\text{ N} \\le F \\le 20\\text{ N}$, nên hợp lực không thể bằng $22\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tổng hợp và cân bằng lực:", [
                "Khi hai lực đồng quy cùng phương, cùng chiều ($\\alpha = 0^\\circ$) thì độ lớn hợp lực đạt cực đại $F = F_1 + F_2$.",
                "Khi hai lực đồng quy cùng phương, ngược chiều ($\\alpha = 180^\\circ$) thì độ lớn hợp lực đạt cực tiểu $F = |F_1 - F_2|$.",
                "Hai lực cân bằng là hai lực có cùng giá, cùng độ lớn, ngược chiều nhưng tác dụng vào hai vật khác nhau.",
                "Phân tích lực là phép toán ngược với tổng hợp lực và cũng tuân theo quy tắc hình bình hành.",
            ], [True, True, False, True], "Ý c) sai vì hai lực cân bằng phải cùng tác dụng vào **một vật** (nếu tác dụng vào hai vật khác nhau thì đó là cặp lực – phản lực)."),
            short("vandung", "Hai lực đồng quy có độ lớn $F_1 = 6\\text{ N}$ và $F_2 = 8\\text{ N}$ có phương vuông góc với nhau ($\\alpha = 90^\\circ$). Độ lớn hợp lực $F$ của hai lực này bằng bao nhiêu Newton ($\\text{N}$)?", ["10"], "Áp dụng công thức $F = \\sqrt{F_1^2 + F_2^2} = \\sqrt{6^2 + 8^2} = \\sqrt{100} = 10\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 12: Định luật 1 và Định luật 2 Newton",
        icon="🍎",
        description="Định luật 1 Newton và quán tính, khối lượng là số đo mức quán tính, Định luật 2 Newton a = F/m hay F = m.a.",
        requirements=[
            "Phát biểu được Định luật 1 Newton và giải thích được các hiện tượng thực tế liên quan đến quán tính của vật.",
            "Nêu được khối lượng $m$ là đại lượng đặc trưng cho mức quán tính của vật (khối lượng càng lớn thì mức quán tính càng lớn).",
            "Phát biểu và vận dụng được biểu thức Định luật 2 Newton: $\\vec{a} = \\dfrac{\\vec{F}}{m}$ hay $\\vec{F} = m\\vec{a}$.",
        ],
        definition="Định luật 1 Newton: Nếu một vật không chịu tác dụng của lực nào hoặc chịu tác dụng của các lực có hợp lực bằng không, thì vật đang đứng yên sẽ tiếp tục đứng yên, đang chuyển động sẽ tiếp tục chuyển động thẳng đều. Định luật 2 Newton: Gia tốc của một vật cùng hướng với lực tác dụng lên vật; độ lớn của gia tốc tỉ lệ thuận với độ lớn của lực và tỉ lệ nghịch với khối lượng của vật ($\\vec{a} = \\dfrac{\\vec{F}}{m}$).",
        theory=(
            "### 1. Định luật 1 Newton và Quán tính\n"
            "- Lực **không phải** là nguyên nhân duy trì chuyển động, mà là nguyên nhân **làm biến đổi vận tốc** (gây ra gia tốc) của vật.\n"
            "- **Quán tính** là tính chất của mọi vật có xu hướng bảo toàn vận tốc cả về hướng và độ lớn (khi xe phanh gấp, người ngồi trên xe chúi về phía trước; khi xe rẽ phải, người nghiêng sang trái).\n"
            "- **Khối lượng ($m$)** là đại lượng đặc trưng cho **mức quán tính** của vật: vật có khối lượng càng lớn thì mức quán tính càng lớn (càng khó thay đổi vận tốc).\n\n"
            "### 2. Định luật 2 Newton\n"
            "- Hệ thức vectơ và độ lớn:\n"
            "  $$\\vec{a} = \\dfrac{\\vec{F}_{\\text{hl}}}{m} \\iff \\vec{F}_{\\text{hl}} = m \\cdot \\vec{a} \\implies F = m \\cdot a$$\n"
            "- Đơn vị lực: $1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2$."
        ),
        formulas=[
            G(
                "Định luật 1 và Định luật 2 Newton",
                F("Hệ thức Định luật 1 Newton", "$\\sum \\vec{F} = \\vec{0} \\implies \\vec{a} = \\vec{0} \\iff \\vec{v} = \\text{const}$", "Vật đứng yên ($v = 0$) hoặc chuyển động thẳng đều ($\\vec{v} = \\text{const}$)."),
                F("Hệ thức Định luật 2 Newton", "$\\vec{a} = \\dfrac{\\vec{F}}{m} \\iff \\vec{F} = m\\vec{a} \\implies a = \\dfrac{F}{m}$", "Trong đó $F$ là độ lớn hợp lực ($\\text{N}$), $m$ là khối lượng ($\\text{kg}$), $a$ là gia tốc ($\\text{m/s}^2$)."),
            )
        ],
        example="Tác dụng một hợp lực không đổi có độ lớn $F = 30\\text{ N}$ lên một vật có khối lượng $m = 6\\text{ kg}$ đang đứng yên trên mặt phẳng ngang nhẵn. Hãy tính độ lớn gia tốc $a$ của vật và vận tốc của vật sau $t = 4\\text{ s}$.",
        example_answer="Theo định luật 2 Newton, độ lớn gia tốc của vật là $a = \\dfrac{F}{m} = \\dfrac{30}{6} = 5\\text{ m/s}^2$. Sau $t = 4\\text{ s}$, vận tốc của vật là $v = v_0 + at = 0 + 5 \\cdot 4 = 20\\text{ m/s}$.",
        real_life="Hành khách ngồi trên ô tô bắt buộc phải thắt dây an toàn (seatbelt) để khi xe không may phanh gấp, dây an toàn giữ cơ thể lại không bị lao về phía trước theo quán tính.",
        quiz=[
            mcq("biet", "Biểu thức nào sau đây là biểu thức đúng của Định luật 2 Newton?", ["$\\vec{a} = \\dfrac{\\vec{F}}{m}$", "$\\vec{a} = m \\cdot \\vec{F}$", "$\\vec{a} = \\dfrac{m}{\\vec{F}}$", "$F = \\dfrac{m}{a}$"], 0, "Theo định luật 2 Newton, gia tốc $\\vec{a} = \\dfrac{\\vec{F}}{m}$ hay $\\vec{F} = m\\vec{a}$."),
            mcq("biet", "Đại lượng vật lí nào đặc trưng cho **mức quán tính** của một vật?", ["Khối lượng $m$ của vật", "Vận tốc $v$ của vật", "Thể tích $V$ của vật", "Nhiệt độ $T$ của vật"], 0, "Khối lượng là đại lượng đặc trưng cho mức quán tính của vật; khối lượng càng lớn thì mức quán tính càng lớn."),
            mcq("hieu", "Khi xe buýt đang chạy thẳng về phía trước mà bất ngờ đạp phanh gấp, hành khách ngồi trên xe sẽ có xu hướng chuyển động như thế nào? Vì sao?", ["Ngả người về phía trước do theo quán tính phần thân trên vẫn giữ vận tốc tiến về trước", "Ngả người ra phía sau do lực đẩy của phanh", "Bay thẳng đứng lên trần xe", "Đứng yên tuyệt đối không hề nghiêng ngả"], 0, "Khi xe phanh gấp, chân người dừng lại cùng sàn xe nhưng phần thân trên theo quán tính vẫn giữ vận tốc cũ lao về phía trước."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Định luật 1 và Định luật 2 Newton:", [
                "Một vật đang chuyển động mà tất cả các lực tác dụng lên nó bỗng nhiên cân bằng nhau ($\\sum \\vec{F} = \\vec{0}$) thì vật sẽ tiếp tục chuyển động thẳng đều.",
                "Vectơ gia tốc $\\vec{a}$ của vật luôn cùng phương và cùng chiều với vectơ hợp lực $\\vec{F}$ tác dụng lên vật.",
                "Một xe tải chở đầy hàng có mức quán tính nhỏ hơn một chiếc xe đạp.",
                "Đơn vị $1\\text{ N}$ tương đương với $1\\text{ kg}\\cdot\\text{m/s}^2$.",
            ], [True, True, False, True], "Ý c) sai vì xe tải chở đầy hàng có khối lượng lớn hơn rất nhiều nên có mức quán tính lớn hơn xe đạp rất nhiều."),
            short("vandung", "Một hợp lực có độ lớn $F = 24\\text{ N}$ tác dụng vào một vật có khối lượng $m = 8\\text{ kg}$. Độ lớn gia tốc $a$ mà vật thu được bằng bao nhiêu $\\text{m/s}^2$?", ["3"], "Áp dụng định luật 2 Newton: $a = \\dfrac{F}{m} = \\dfrac{24}{8} = 3\\text{ m/s}^2$.", unit="m/s²"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 13: Định luật 3 Newton",
        icon="🤝",
        description="Nội dung và biểu thức Định luật 3 Newton F_AB = -F_BA, đặc điểm của cặp lực và phản lực.",
        requirements=[
            "Phát biểu và viết được biểu thức của Định luật 3 Newton: trong mọi trường hợp, khi vật $A$ tác dụng lên vật $B$ một lực thì vật $B$ cũng tác dụng trở lại vật $A$ một lực ($\\vec{F}_{AB} = -\\vec{F}_{BA}$).",
            "Nêu được 4 đặc điểm của cặp lực và phản lực: cùng giá, cùng độ lớn, ngược chiều và đặt vào hai vật khác nhau (nên không triệt tiêu nhau).",
            "Giải thích được nguyên tắc đẩy nước khi bơi, bước đi trên đường và lực tương tác khi hai vật va chạm.",
        ],
        definition="Định luật 3 Newton: Trong mọi trường hợp, khi vật $A$ tác dụng lên vật $B$ một lực thì đồng thời vật $B$ cũng tác dụng trở lại vật $A$ một lực. Hai lực này là hai lực trực đối (cùng giá, cùng độ lớn nhưng ngược chiều và đặt vào hai vật khác nhau): $\\vec{F}_{AB} = -\\vec{F}_{BA}$.",
        theory=(
            "### 1. Định luật 3 Newton\n"
            "- Tương tác giữa các vật luôn có tính chất **hai chiều**:\n"
            "  $$\\vec{F}_{AB} = -\\vec{F}_{BA} \\implies F_{AB} = F_{BA}$$\n"
            "- Một trong hai lực gọi là **lực tác dụng**, lực kia gọi là **phản lực**.\n\n"
            "### 2. Đặc điểm của cặp Lực và Phản lực\n"
            "1. Luôn **xuất hiện và mất đi đồng thời**.\n"
            "2. Luôn **cùng bản chất** (cùng là lực đàn hồi, cùng là lực hấp dẫn, cùng là lực điện...).\n"
            "3. Là hai lực **trực đối**: cùng phương (cùng giá), ngược chiều và có cùng độ lớn ($F_{AB} = F_{BA}$).\n"
            "4. Đặt vào **hai vật khác nhau** (một lực đặt lên vật $B$, một lực đặt lên vật $A$) nên **không bao giờ cân bằng (không triệt tiêu) nhau**."
        ),
        formulas=[
            G(
                "Biểu thức Định luật 3 Newton",
                F("Hệ thức vectơ và độ lớn của cặp lực – phản lực", "$\\vec{F}_{AB} = -\\vec{F}_{BA}; \\qquad F_{AB} = F_{BA}$", "Dù vật $A$ có khối lượng lớn hơn vật $B$ rất nhiều thì độ lớn lực $A$ tác dụng lên $B$ vẫn bằng đúng độ lớn lực $B$ tác dụng lại $A$."),
                F("Tỉ số gia tốc của hai vật tương tác cô lập", "$m_A a_A = m_B a_B \\implies \\dfrac{a_A}{a_B} = \\dfrac{m_B}{m_A}$", "Vật nào có khối lượng nhỏ hơn sẽ thu được gia tốc lớn hơn khi va chạm."),
            )
        ],
        example="Một viên bi sắt số 1 có khối lượng $m_1 = 0{,}2\\text{ kg}$ đang lăn đến va chạm vào viên bi sắt số 2 có khối lượng $m_2 = 0{,}4\\text{ kg}$. Trong lúc va chạm, viên bi 1 thu được gia tốc có độ lớn $a_1 = 6\\text{ m/s}^2$. Hãy tính độ lớn lực tương tác giữa hai viên bi và độ lớn gia tốc $a_2$ của viên bi 2.",
        example_answer="Độ lớn lực viên bi 2 tác dụng lên viên bi 1 là $F_{21} = m_1 a_1 = 0{,}2 \\cdot 6 = 1{,}2\\text{ N}$. Theo định luật 3 Newton, lực viên bi 1 tác dụng lên viên bi 2 cũng có độ lớn $F_{12} = F_{21} = 1{,}2\\text{ N}$. Gia tốc của viên bi 2 là $a_2 = \\dfrac{F_{12}}{m_2} = \\dfrac{1{,}2}{0{,}4} = 3\\text{ m/s}^2$.",
        real_life="Khi vận động viên bơi lội dùng tay và chân đẩy nước về phía sau, nước đồng thời tác dụng một phản lực bằng độ lớn và hướng về phía trước đẩy cơ thể người bơi tiến lên.",
        quiz=[
            mcq("biet", "Biểu thức vectơ của Định luật 3 Newton khi vật $A$ tương tác với vật $B$ là gì?", ["$\\vec{F}_{AB} = -\\vec{F}_{BA}$", "$\\vec{F}_{AB} = \\vec{F}_{BA}$", "$\\vec{F}_{AB} = 2\\vec{F}_{BA}$", "$\\vec{F}_{AB} \\cdot \\vec{F}_{BA} = 0$"], 0, "Theo định luật 3 Newton, hai lực tương tác giữa hai vật là hai lực trực đối: $\\vec{F}_{AB} = -\\vec{F}_{BA}$."),
            mcq("biet", "Vì sao cặp lực và phản lực trong Định luật 3 Newton **không** cân bằng (không triệt tiêu) nhau dù chúng cùng giá, ngược chiều và cùng độ lớn?", ["Vì chúng đặt vào hai vật khác nhau", "Vì chúng có độ lớn khác nhau", "Vì chúng không xuất hiện cùng một lúc", "Vì chúng có phương vuông góc với nhau"], 0, "Hai lực chỉ cân bằng khi cùng đặt vào một vật; cặp lực và phản lực đặt vào hai vật khác nhau nên không triệt tiêu nhau."),
            mcq("hieu", "Khi một con muỗi bay va vào kính chắn gió của một chiếc ô tô đang chạy nhanh, hãy so sánh độ lớn lực $F_1$ mà ô tô tác dụng lên con muỗi và độ lớn lực $F_2$ mà con muỗi tác dụng lên ô tô?", ["$F_1 = F_2$ (hai lực có độ lớn bằng nhau theo định luật 3 Newton)", "$F_1$ lớn gấp hàng triệu lần $F_2$", "$F_2$ lớn hơn $F_1$", "$F_2 = 0$ còn $F_1 > 0$"], 0, "Theo định luật 3 Newton, lực tương tác giữa hai vật luôn có độ lớn bằng nhau ($F_1 = F_2$); con muỗi bị biến dạng mạnh chỉ vì khối lượng của nó rất nhỏ so với ô tô."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Định luật 3 Newton:", [
                "Lực và phản lực luôn xuất hiện và mất đi đồng thời.",
                "Lực và phản lực luôn cùng bản chất vật lí.",
                "Khi ta dùng búa đóng đinh với lực $50\\text{ N}$ thì chiếc đinh cũng tác dụng lại đầu búa một lực có độ lớn $50\\text{ N}$.",
                "Trọng lực và phản lực của mặt bàn tác dụng lên quyển sách nằm yên trên bàn là cặp lực – phản lực của định luật 3 Newton.",
            ], [True, True, True, False], "Ý d) sai vì trọng lực và phản lực của mặt bàn cùng đặt vào quyển sách nên là hai lực cân bằng (không phải cặp lực – phản lực đặt vào hai vật khác nhau)."),
            short("vandung", "Hai học sinh trượt patin đứng đối diện nhau trên sân băng: học sinh $A$ ($m_A = 40\\text{ kg}$) đẩy học sinh $B$ ($m_B = 50\\text{ kg}$) bằng một lực có độ lớn $80\\text{ N}$. Độ lớn phản lực mà học sinh $B$ tác dụng trở lại học sinh $A$ bằng bao nhiêu Newton ($\\text{N}$)?", ["80"], "Theo định luật 3 Newton, độ lớn phản lực bằng đúng độ lớn lực tác dụng: $F_{BA} = F_{AB} = 80\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 14: Trọng lực và lực căng",
        icon="🏗️",
        description="Biểu thức trọng lực P = m.g, khái niệm trọng tâm của vật rắn và đặc điểm của lực căng dây T.",
        requirements=[
            "Viết được biểu thức vectơ của trọng lực $\\vec{P} = m\\vec{g}$ và nêu được điểm đặt của trọng lực là trọng tâm $G$ của vật.",
            "Nêu được trọng lượng của một vật giảm nhẹ khi đưa vật lên cao hoặc từ địa cực về xích đạo do $g$ thay đổi.",
            "Xác định được điểm đặt, phương, chiều và độ lớn của lực căng dây $\\vec{T}$ tác dụng lên vật được treo hoặc kéo bằng dây.",
        ],
        definition="Trọng lực là lực hấp dẫn giữa Trái Đất và vật, đặt tại trọng tâm của vật và được xác định bởi công thức $\\vec{P} = m\\vec{g}$ (độ lớn $P = mg$). Khi một sợi dây bị kéo căng, ở mọi điểm trên dây xuất hiện lực căng dây $\\vec{T}$ có phương trùng với sợi dây và chiều hướng từ hai đầu dây vào phần giữa sợi dây.",
        theory=(
            "### 1. Trọng lực và Trọng tâm\n"
            "- Biểu thức: $\\vec{P} = m\\vec{g}$, độ lớn $P = m \\cdot g$ (đơn vị $\\text{N}$).\n"
            "- **Điểm đặt**: tại **trọng tâm $G$** của vật. Với các vật phẳng mỏng đồng chất có tâm đối xứng (hình tròn, hình vuông, hình chữ nhật, hình bình hành), trọng tâm $G$ nằm ngay tại tâm đối xứng của hình.\n"
            "- Khối lượng $m$ của vật không thay đổi theo vị trí, nhưng gia tốc rơi tự do $g$ phụ thuộc vào độ cao và vĩ độ địa lí nên **trọng lượng $P = mg$ thay đổi nhẹ theo vị trí**.\n\n"
            "### 2. Lực căng dây ($\\vec{T}$)\n"
            "- Xuất hiện khi sợi dây bị kéo căng.\n"
            "- **Điểm đặt**: tại điểm mà đầu dây buộc vào vật.\n"
            "- **Phương**: trùng với phương của sợi dây.\n"
            "- **Chiều**: hướng từ vật vào phía phần giữa của sợi dây (chống lại xu hướng kéo dãn dây).\n"
            "- Khi treo vật đứng yên bằng dây thẳng đứng: $T = P = mg$."
        ),
        formulas=[
            G(
                "Trọng lực và Lực căng dây",
                F("Biểu thức trọng lực và trọng lượng", "$\\vec{P} = m\\vec{g} \\implies P = m \\cdot g$", "Trong đó $m$ là khối lượng ($\\text{kg}$), $g \\approx 9{,}8\\text{ m/s}^2$ là gia tốc trọng trường."),
                F("Lực căng dây khi treo vật chuyển động thẳng đứng", "$\\text{Đứng yên/Thẳng đều: } T = mg; \\qquad \\text{Nhanh dần đi lên: } T = m(g + a); \\qquad \\text{Nhanh dần đi xuống: } T = m(g - a)$", "Sợi dây chỉ chịu được lực căng tối đa $T_{\\max}$; nếu $T > T_{\\max}$ thì dây bị đứt."),
            )
        ],
        example="Một đèn chùm có khối lượng $m = 5\\text{ kg}$ được treo đứng yên vào trần nhà bằng một sợi dây cáp nhẹ thẳng đứng tại nơi có $g = 9{,}8\\text{ m/s}^2$. Hãy tính trọng lượng $P$ của đèn chùm và độ lớn lực căng $T$ của sợi dây cáp.",
        example_answer="Trọng lượng của đèn chùm là $P = m \\cdot g = 5 \\cdot 9{,}8 = 49\\text{ N}$. Vì đèn chùm đứng yên cân bằng dưới tác dụng của trọng lực $\\vec{P}$ và lực căng dây $\\vec{T}$ nên độ lớn lực căng dây là $T = P = 49\\text{ N}$.",
        real_life="Khi thiết kế cáp treo du lịch hoặc cáp thang máy, các kĩ sư phải tính toán lực căng dây lớn nhất $T = m(g + a)$ lúc buồng thang tăng tốc đi lên để chọn cáp thép có hệ số an toàn cao.",
        quiz=[
            mcq("biet", "Điểm đặt của trọng lực tác dụng lên một vật rắn được gọi là gì?", ["Trọng tâm của vật", "Quang tâm của vật", "Tiêu điểm của vật", "Điểm cực Bắc của vật"], 0, "Điểm đặt của trọng lực tác dụng lên vật gọi là trọng tâm của vật."),
            mcq("biet", "Lực căng dây $\\vec{T}$ do sợi dây tác dụng lên vật buộc ở đầu dây có phương và chiều như thế nào?", ["Phương trùng với sợi dây, chiều hướng từ đầu dây vào phần giữa của sợi dây", "Phương vuông góc với sợi dây", "Phương trùng với sợi dây, chiều hướng từ giữa dây đẩy ra ngoài vật", "Luôn có phương nằm ngang trong mọi trường hợp"], 0, "Dây chỉ chịu lực kéo nên lực căng dây luôn dọc theo sợi dây và hướng từ đầu dây vào giữa dây."),
            mcq("hieu", "Một vật đồng chất phẳng mỏng có dạng hình chữ nhật hoặc hình tròn thì trọng tâm $G$ của vật nằm ở đâu?", ["Nằm tại tâm đối xứng hình học (giao điểm hai đường chéo hoặc tâm hình tròn)", "Nằm ở một góc bất kì trên mép ngoài của vật", "Nằm ở bên ngoài không gian cách vật $1\\text{ m}$", "Không có trọng tâm xác định"], 0, "Đối với vật đồng chất và có dạng hình học đối xứng, trọng tâm nằm tại tâm đối xứng của vật."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về trọng lực và lực căng dây:", [
                "Công thức vectơ của trọng lực là $\\vec{P} = m\\vec{g}$.",
                "Khi đưa một vật từ mặt đất lên trạm vũ trụ ở độ cao lớn, khối lượng $m$ không đổi nhưng trọng lượng $P$ giảm đi.",
                "Một sợi dây mềm không chỉ kéo được vật mà còn có thể đẩy được vật dọc theo dây.",
                "Khi treo một vật nặng $m = 3\\text{ kg}$ đứng yên vào đầu một sợi dây nhẹ tại nơi có $g = 10\\text{ m/s}^2$, lực căng của sợi dây bằng $30\\text{ N}$.",
            ], [True, True, False, True], "Ý c) sai vì dây mềm bị chùng lại khi nén nên chỉ có thể tác dụng lực kéo (lực căng dây) chứ không đẩy được vật."),
            short("vandung", "Một buồng thang máy có tổng khối lượng $m = 500\\text{ kg}$ đang được dây cáp kéo chuyển động thẳng đều đi lên tại nơi có $g = 10\\text{ m/s}^2$. Lực căng $T$ của dây cáp bằng bao nhiêu Newton ($\\text{N}$)?", ["5000"], "Vì thang máy chuyển động thẳng đều ($a = 0$) nên lực căng cáp cân bằng với trọng lực: $T = P = mg = 500 \\cdot 10 = 5000\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 15: Lực ma sát",
        icon="🛷",
        description="Đặc điểm của lực ma sát nghỉ và lực ma sát trượt, hệ số ma sát trượt μ và công thức F_mst = μ.N.",
        requirements=[
            "Nêu được điều kiện xuất hiện và đặc điểm của lực ma sát nghỉ ($0 \\le F_{\\text{msn}} \\le F_{\\text{msn max}}$).",
            "Viết và vận dụng được công thức tính độ lớn lực ma sát trượt: $F_{\\text{mst}} = \\mu \\cdot N$, trong đó $\\mu$ là hệ số ma sát trượt và $N$ là độ lớn áp lực pháp tuyến.",
            "Tính được áp lực $N$ và lực ma sát trượt khi vật trượt trên mặt phẳng nằm ngang ($N = mg$) và trên mặt phẳng nghiêng góc $\\alpha$ ($N = mg\\cos\\alpha$).",
        ],
        definition="Lực ma sát trượt xuất hiện ở mặt tiếp xúc khi vật trượt trên một bề mặt, có hướng ngược với hướng của vận tốc tương đối và có độ lớn tỉ lệ với độ lớn của áp lực: $F_{\\text{mst}} = \\mu \\cdot N$.",
        theory=(
            "### 1. Lực ma sát nghỉ\n"
            "- Xuất hiện ở mặt tiếp xúc để giữ cho vật đứng yên khi vật chịu lực kéo song song với mặt tiếp xúc.\n"
            "- Khi vật vẫn đứng yên, độ lớn lực ma sát nghỉ bằng đúng độ lớn thành phần lực kéo song song mặt tiếp xúc ($F_{\\text{msn}} = F_k$) và có giá trị cực đại $F_{\\text{msn max}}$. Khi $F_k > F_{\\text{msn max}}$, vật bắt đầu trượt.\n\n"
            "### 2. Lực ma sát trượt\n"
            "- **Hướng**: cùng phương và ngược chiều với vận tốc tương đối của vật so với mặt tiếp xúc.\n"
            "- **Công thức độ lớn**:\n"
            "  $$F_{\\text{mst}} = \\mu \\cdot N$$\n"
            "  - $\\mu$: **hệ số ma sát trượt** (không có đơn vị), phụ thuộc vào bản chất và tình trạng (nhẵn, nhám, khô, ướt) của hai mặt tiếp xúc, **không phụ thuộc vào diện tích tiếp xúc**.\n"
            "  - $N$: độ lớn áp lực (phản lực pháp tuyến). Khi kéo ngang trên mặt phẳng nằm ngang: $N = P = mg$; khi vật trượt trên mặt phẳng nghiêng góc $\\alpha$: $N = mg\\cos\\alpha$."
        ),
        formulas=[
            G(
                "Công thức lực ma sát trượt trên mặt ngang và mặt nghiêng",
                F("Độ lớn lực ma sát trượt tổng quát", "$F_{\\text{mst}} = \\mu \\cdot N$", "Trong đó $\\mu = \\dfrac{F_{\\text{mst}}}{N}$ là hệ số ma sát trượt (không đơn vị), $N$ là áp lực vuông góc với mặt tiếp xúc ($\\text{N}$)."),
                F("Áp lực N và Gia tốc trên mặt phẳng ngang / mặt nghiêng", "$\\text{Mặt ngang (kéo ngang): } N = mg,\\ a = \\dfrac{F_k - \\mu mg}{m}; \\qquad \\text{Mặt nghiêng góc } \\alpha: N = mg\\cos\\alpha,\\ F_{\\text{mst}} = \\mu mg\\cos\\alpha$", "Để kéo vật chuyển động thẳng đều trên mặt phẳng ngang ($a = 0$) bằng lực ngang thì $F_k = F_{\\text{mst}} = \\mu mg$."),
            )
        ],
        example="Một thùng gỗ có khối lượng $m = 20\\text{ kg}$ được kéo trượt thẳng đều trên mặt sàn nằm ngang bằng một lực kéo nằm ngang $F_k$. Biết hệ số ma sát trượt giữa đáy thùng và mặt sàn là $\\mu = 0{,}25$ và lấy $g = 10\\text{ m/s}^2$. Hãy tính độ lớn lực ma sát trượt $F_{\\text{mst}}$ và lực kéo $F_k$.",
        example_answer="Trên mặt sàn nằm ngang với lực kéo nằm ngang, áp lực bằng trọng lượng của thùng: $N = P = mg = 20 \\cdot 10 = 200\\text{ N}$. Lực ma sát trượt có độ lớn là $F_{\\text{mst}} = \\mu \\cdot N = 0{,}25 \\cdot 200 = 50\\text{ N}$. Vì thùng chuyển động thẳng đều ($a = 0$) nên $F_k = F_{\\text{mst}} = 50\\text{ N}$.",
        real_life="Hệ số ma sát trượt giữa lốp cao su ô tô và mặt đường nhựa khô khoảng $\\mu \\approx 0{,}7$, nhưng khi mặt đường đóng băng chỉ còn $\\mu \\approx 0{,}1$ nên xe rất dễ bị trượt nếu không lắp xích chống trượt.",
        quiz=[
            mcq("biet", "Công thức tính độ lớn của lực ma sát trượt $F_{\\text{mst}}$ theo hệ số ma sát trượt $\\mu$ và độ lớn áp lực $N$ là gì?", ["$F_{\\text{mst}} = \\mu \\cdot N$", "$F_{\\text{mst}} = \\dfrac{\\mu}{N}$", "$F_{\\text{mst}} = \\dfrac{N}{\\mu}$", "$F_{\\text{mst}} = \\mu + N$"], 0, "Độ lớn lực ma sát trượt tỉ lệ thuận với độ lớn của áp lực: $F_{\\text{mst}} = \\mu \\cdot N$."),
            mcq("biet", "Hệ số ma sát trượt $\\mu$ giữa hai mặt tiếp xúc phụ thuộc vào yếu tố nào sau đây?", ["Bản chất vật liệu và tình trạng bề mặt (nhẵn, nhám, khô, ướt) của hai mặt tiếp xúc", "Diện tích lớn hay nhỏ của mặt tiếp xúc", "Tốc độ chuyển động nhanh hay chậm của vật", "Thời gian vật đã trượt trên mặt phẳng"], 0, "Hệ số ma sát trượt $\\mu$ chỉ phụ thuộc vào vật liệu và tình trạng của hai bề mặt tiếp xúc."),
            mcq("hieu", "Một vật trượt tự do trên mặt phẳng nghiêng một góc $\\alpha$ so với phương ngang. Khi đó độ lớn áp lực $N$ của vật lên mặt phẳng nghiêng bằng bao nhiêu?", ["$N = mg\\cos\\alpha$", "$N = mg\\sin\\alpha$", "$N = mg$", "$N = mg\\tan\\alpha$"], 0, "Trên mặt phẳng nghiêng góc $\\alpha$, thành phần trọng lực vuông góc với mặt nghiêng là $P_n = mg\\cos\\alpha$, do đó áp lực $N = mg\\cos\\alpha$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về lực ma sát:", [
                "Hệ số ma sát trượt $\\mu$ là đại lượng không có đơn vị.",
                "Nếu đặt viên gạch nằm ngang hay dựng đứng trên mặt bàn rồi kéo trượt thì độ lớn lực ma sát trượt vẫn như nhau (vì không phụ thuộc diện tích tiếp xúc).",
                "Khi vật đang đứng yên trên bàn mà chịu lực kéo ngang $5\\text{ N}$ vẫn chưa chuyển động thì lực ma sát nghỉ lúc đó bằng $0\\text{ N}$.",
                "Lực ma sát nghỉ đóng vai trò là lực phát động giúp bánh xe ô tô và bàn chân người đẩy cơ thể tiến về phía trước.",
            ], [True, True, False, True], "Ý c) sai vì khi vật vẫn đứng yên dưới tác dụng của lực kéo ngang $5\\text{ N}$ thì lực ma sát nghỉ cân bằng với lực kéo và có độ lớn bằng $5\\text{ N}$."),
            short("vandung", "Kéo một vật có khối lượng $m = 10\\text{ kg}$ trượt trên mặt sàn nằm ngang bằng lực ngang. Biết hệ số ma sát trượt giữa vật và sàn là $\\mu = 0{,}3$ và lấy $g = 10\\text{ m/s}^2$. Độ lớn lực ma sát trượt $F_{\\text{mst}}$ tác dụng lên vật bằng bao nhiêu Newton ($\\text{N}$)?", ["30"], "Ta có $N = mg = 10 \\cdot 10 = 100\\text{ N}$. Lực ma sát trượt là $F_{\\text{mst}} = \\mu N = 0{,}3 \\cdot 100 = 30\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 16: Lực cản và lực nâng",
        icon="✈️",
        description="Lực cản của chất lưu (không khí, nước), tốc độ giới hạn khi rơi trong chất lưu, lực nâng khí động học và lực đẩy Archimedes.",
        requirements=[
            "Nêu được lực cản của chất lưu (không khí, nước) cùng phương ngược chiều chuyển động và phụ thuộc vào hình dạng, kích thước cũng như tốc độ của vật.",
            "Giải thích được hiện tượng một vật rơi trong chất lưu sau một thời gian sẽ đạt tốc độ giới hạn không đổi (khi $F_{\\text{cản}} + F_A = P$).",
            "Phân biệt được lực đẩy Archimedes ($F_A = \\rho g V$) và lực nâng khí động học tác dụng lên cánh máy bay.",
        ],
        definition="Chất lưu là thuật ngữ dùng để chỉ chất lỏng và chất khí. Mọi vật chuyển động trong chất lưu luôn chịu tác dụng của lực cản (ngược chiều chuyển động, tăng khi tốc độ tăng) và lực nâng (lực đẩy Archimedes hoặc lực nâng khí động học).",
        theory=(
            "### 1. Lực cản của chất lưu và Tốc độ giới hạn\n"
            "- **Lực cản của chất lưu ($\\vec{F}_c$)**: đặt tại trọng tâm, cùng phương và ngược chiều với vận tốc chuyển động của vật.\n"
            "- Độ lớn lực cản phụ thuộc vào **hình dạng của vật** (hình khí động học thuôn nhọn có lực cản nhỏ nhất), **diện tích mặt cản** và **tăng lên khi tốc độ của vật tăng**.\n"
            "- **Chuyển động rơi trong chất lưu**: Khi vật rơi xuống, tốc độ $v$ tăng làm lực cản $F_c$ tăng dần. Đến khi $F_c + F_A = P$ thì hợp lực bằng $0$, vật không tăng tốc nữa mà chuyển động thẳng đều với **tốc độ giới hạn**.\n\n"
            "### 2. Lực nâng của chất lưu\n"
            "- **Lực đẩy Archimedes**: tác dụng lên mọi vật nhúng trong chất lưu có khối lượng riêng $\\rho$: $F_A = \\rho \\cdot g \\cdot V$.\n"
            "- **Lực nâng khí động học**: tác dụng lên cánh máy bay, cánh chim khi chuyển động nhờ thiết kế mặt trên cánh cong hơn mặt dưới (dòng khí qua mặt trên nhanh hơn, áp suất nhỏ hơn áp suất ở mặt dưới cánh)."
        ),
        formulas=[
            G(
                "Lực đẩy Archimedes và Cân bằng lực khi đạt tốc độ giới hạn",
                F("Công thức lực đẩy Archimedes theo khối lượng riêng ρ", "$F_A = \\rho \\cdot g \\cdot V$", "Trong đó $\\rho$ là khối lượng riêng của chất lưu ($\\text{kg/m}^3$), $g \\approx 9{,}8\\text{ m/s}^2$, $V$ là thể tích phần chất lưu bị vật chiếm chỗ ($\\text{m}^3$)."),
                F("Điều kiện cân bằng khi vật rơi đạt tốc độ giới hạn", "$F_{\\text{cản}} + F_A = P = m \\cdot g$", "Khi mở dù nhảy, diện tích dù lớn làm $F_{\\text{cản}}$ tăng vọt, giúp giảm tốc độ giới hạn xuống mức an toàn ($\\approx 5\\text{ m/s}$) trước khi chạm đất."),
            )
        ],
        example="Một người nhảy dù có tổng khối lượng cả người và dù là $m = 80\\text{ kg}$. Sau khi bung dù một thời gian, người đó rơi thẳng đứng đều với tốc độ giới hạn không đổi xuống đất (bỏ qua lực đẩy Archimedes của không khí, lấy $g = 9{,}8\\text{ m/s}^2$). Hãy tính độ lớn lực cản của không khí tác dụng lên chiếc dù lúc này.",
        example_answer="Khi người nhảy dù rơi thẳng đều với tốc độ giới hạn ($a = 0$), lực cản của không khí cân bằng với trọng lực của hệ người và dù: $F_{\\text{cản}} = P = m \\cdot g = 80 \\cdot 9{,}8 = 784\\text{ N}$.",
        real_life="Cánh máy bay dân dụng được thiết kế có tiết diện khí động học cong lồi ở mặt trên và phẳng hơn ở mặt dưới để tạo ra lực nâng hàng trăm tấn giúp máy bay cất cánh.",
        quiz=[
            mcq("biet", "Độ lớn lực cản của chất lưu (không khí, nước) tác dụng lên một vật chuyển động phụ thuộc vào những yếu tố nào?", ["Hình dạng, kích thước của vật và tốc độ chuyển động của vật trong chất lưu", "Chỉ phụ thuộc vào khối lượng của vật", "Chỉ phụ thuộc vào màu sắc sơn bên ngoài vật", "Không phụ thuộc vào tốc độ của vật"], 0, "Lực cản của chất lưu phụ thuộc vào hình dạng, diện tích mặt cản của vật và tốc độ chuyển động."),
            mcq("biet", "Khi một giọt mưa rơi từ đám mây rất cao xuống đất, vì sao khi gần chạm đất giọt mưa lại chuyển động gần như thẳng đều với tốc độ giới hạn không đổi (mà không tăng tốc mãi)?", ["Vì khi tốc độ tăng đến một giá trị nhất định, lực cản của không khí tăng lên cân bằng với trọng lực tác dụng lên giọt mưa", "Vì gần mặt đất gia tốc trọng trường $g$ bằng $0$", "Vì khối lượng của giọt mưa biến mất hoàn toàn", "Vì không khí đẩy giọt mưa bay ngược lên trời"], 0, "Khi $F_{\\text{cản}} = P$ thì hợp lực bằng $0$, gia tốc $a = 0$ nên giọt mưa rơi đều với tốc độ giới hạn."),
            mcq("hieu", "Một tàu ngầm đang lặn lơ lửng đứng yên ở một độ sâu xác định dưới mặt biển. Khi muốn tàu ngầm nổi lên mặt biển, thủy thủ đoàn bơm khí nén đẩy bớt nước ra khỏi các khoang chứa nước dằn của tàu nhằm mục đích gì?", ["Làm giảm trọng lượng $P$ của tàu ngầm để lực đẩy Archimedes $F_A > P$ đẩy tàu nổi lên", "Làm giảm thể tích vỏ ngoài của tàu ngầm", "Làm tăng trọng lượng $P$ của tàu ngầm", "Làm mất lực đẩy Archimedes của nước biển"], 0, "Thể tích vỏ ngoài $V$ không đổi nên $F_A = \\rho g V$ không đổi; bơm nước ra làm giảm trọng lượng $P$ của tàu ($P < F_A$) nên hợp lực hướng lên đẩy tàu nổi lên."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về lực cản và lực nâng của chất lưu:", [
                "Thuật ngữ 'chất lưu' dùng để gọi chung chất lỏng và chất khí.",
                "Tốc độ của vật chuyển động trong chất lưu càng lớn thì độ lớn lực cản của chất lưu càng lớn.",
                "Lực nâng giúp máy bay nặng hàng trăm tấn bay được trên bầu trời chủ yếu là lực đẩy Archimedes của không khí.",
                "Một vật có thể tích $0{,}01\\text{ m}^3$ nhúng chìm hoàn toàn trong nước ($\\rho = 1000\\text{ kg/m}^3, g = 10\\text{ m/s}^2$) chịu lực đẩy Archimedes bằng $100\\text{ N}$.",
            ], [True, True, False, True], "Ý c) sai vì máy bay bay được là nhờ lực nâng khí động học tác dụng lên cánh máy bay khi máy bay chuyển động nhanh (còn khinh khí cầu mới bay nhờ lực đẩy Archimedes)."),
            short("vandung", "Một vận động viên nhảy dù có tổng khối lượng cả người và dù là $m = 75\\text{ kg}$ đang rơi thẳng đều với tốc độ ổn định trước khi tiếp đất tại nơi có $g = 10\\text{ m/s}^2$. Độ lớn lực cản của không khí lúc đó bằng bao nhiêu Newton ($\\text{N}$)?", ["750"], "Khi rơi thẳng đều ($a = 0$), lực cản cân bằng với trọng lực: $F_{\\text{cản}} = P = mg = 75 \\cdot 10 = 750\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 17: Công và công suất",
        icon="⚙️",
        description="Công tổng quát của một lực không đổi A = F.s.cosα, phân biệt công phát động và công cản, công suất P = A/t = F.v.",
        requirements=[
            "Viết và vận dụng được công thức tổng quát tính công của một lực không đổi: $A = F \\cdot s \\cdot \\cos\\alpha$ (hay $A = F \\cdot d \\cdot \\cos\\alpha$), với $\\alpha = (\\widehat{\\vec{F}, \\vec{d}})$.",
            "Biện luận được dấu của công theo góc $\\alpha$: công phát động ($0^\\circ \\le \\alpha < 90^\\circ \\implies A > 0$), công bằng không ($\\alpha = 90^\\circ \\implies A = 0$) và công cản ($90^\\circ < \\alpha \\le 180^\\circ \\implies A < 0$).",
            "Vận dụng được công thức công suất trung bình $\\mathcal{P} = \\dfrac{A}{t}$ và công suất tức thời $\\mathcal{P} = F \\cdot v \\cdot \\cos\\alpha$.",
        ],
        definition="Công của một lực không đổi $\\vec{F}$ làm vật dịch chuyển một đoạn $s$ theo hướng hợp với hướng của lực một góc $\\alpha$ được xác định bởi biểu thức: $A = F \\cdot s \\cdot \\cos\\alpha$ (đơn vị Joule – $\\text{J}$). Công suất là đại lượng đặc trưng cho tốc độ sinh công: $\\mathcal{P} = \\dfrac{A}{t} = F \\cdot v \\cdot \\cos\\alpha$ (đơn vị Oát – $\\text{W}$).",
        theory=(
            "### 1. Công của một lực không đổi\n"
            "- Biểu thức tổng quát:\n"
            "  $$A = F \\cdot s \\cdot \\cos\\alpha$$\n"
            "  trong đó $\\alpha = (\\widehat{\\vec{F}, \\vec{d}})$ là góc hợp bởi vectơ lực $\\vec{F}$ và vectơ độ dịch chuyển $\\vec{d}$ (với $s = |d|$ khi chuyển động thẳng một chiều).\n"
            "- **Các trường hợp của góc $\\alpha$**:\n"
            "  - $0^\\circ \\le \\alpha < 90^\\circ$ ($\\cos\\alpha > 0$): $A > 0$, lực sinh **công phát động** (đặc biệt khi $\\alpha = 0^\\circ \\implies A = F \\cdot s$).\n"
            "  - $\\alpha = 90^\\circ$ ($\\cos 90^\\circ = 0$): $A = 0$, lực vuông góc với hướng dịch chuyển **không sinh công**.\n"
            "  - $90^\\circ < \\alpha \\le 180^\\circ$ ($\\cos\\alpha < 0$): $A < 0$, lực sinh **công cản** (đặc biệt lực ma sát trượt có $\\alpha = 180^\\circ \\implies A_{\\text{ms}} = -F_{\\text{ms}} \\cdot s$).\n\n"
            "### 2. Công suất và liên hệ với lực, vận tốc\n"
            "- Công suất trung bình: $\\mathcal{P} = \\dfrac{A}{t}$.\n"
            "- Liên hệ giữa công suất, lực kéo và tốc độ: $\\mathcal{P} = F \\cdot v \\cdot \\cos\\alpha$ (khi $\\vec{F} \\uparrow\\uparrow \\vec{v}$ thì $\\mathcal{P} = F \\cdot v$)."
        ),
        formulas=[
            G(
                "Công thức tổng quát của Công và Công suất",
                F("Biểu thức tính công của lực không đổi", "$A = F \\cdot s \\cdot \\cos\\alpha$", "Trong đó $0^\\circ \\le \\alpha < 90^\\circ: A > 0$ (công phát động); $\\alpha = 90^\\circ: A = 0$; $90^\\circ < \\alpha \\le 180^\\circ: A < 0$ (công cản)."),
                F("Công suất và liên hệ giữa lực kéo với vận tốc", "$\\mathcal{P} = \\dfrac{A}{t} = F \\cdot v \\cdot \\cos\\alpha$", "Với một động cơ có công suất cực đại $\\mathcal{P}$ không đổi, khi xe lên dốc cần lực kéo $F$ lớn thì phải đi số nhỏ để giảm vận tốc $v$."),
            )
        ],
        example="Một người kéo một thùng hàng trượt trên sàn nhà nằm ngang đi được quãng đường $s = 10\\text{ m}$ bằng một sợi dây hợp với phương nằm ngang một góc $\\alpha = 60^\\circ$. Biết lực kéo có độ lớn $F = 80\\text{ N}$. Hãy tính công của lực kéo trên quãng đường đó.",
        example_answer="Áp dụng công thức tính công: $A = F \\cdot s \\cdot \\cos\\alpha = 80 \\cdot 10 \\cdot \\cos 60^\\circ = 800 \\cdot 0{,}5 = 400\\text{ J}$.",
        real_life="Khi ô tô chạy lên dốc cao, người lái xe phải gạt về số thấp (số 1 hoặc số 2): vì công suất động cơ $\\mathcal{P} = F \\cdot v$ giới hạn nên việc giảm tốc độ $v$ giúp tăng lực kéo $F$ của bánh xe để vượt dốc.",
        quiz=[
            mcq("biet", "Công thức tổng quát tính công $A$ của một lực không đổi $\\vec{F}$ làm vật dịch chuyển quãng đường $s$ theo hướng hợp với $\\vec{F}$ một góc $\\alpha$ là gì?", ["$A = F \\cdot s \\cdot \\cos\\alpha$", "$A = F \\cdot s \\cdot \\sin\\alpha$", "$A = F \\cdot s \\cdot \\tan\\alpha$", "$A = \\dfrac{F \\cdot s}{\\cos\\alpha}$"], 0, "Công của lực không đổi được xác định bởi $A = F \\cdot s \\cdot \\cos\\alpha$."),
            mcq("biet", "Khi lực tác dụng $\\vec{F}$ hợp với hướng dịch chuyển $\\vec{d}$ một góc tù ($90^\\circ < \\alpha \\le 180^\\circ$) thì công của lực đó có tính chất gì?", ["$A < 0$, gọi là công cản", "$A > 0$, gọi là công phát động", "$A = 0$, lực không sinh công", "$A$ luôn bằng vô cùng"], 0, "Khi $90^\\circ < \\alpha \\le 180^\\circ$ thì $\\cos\\alpha < 0$ nên $A < 0$ (công cản)."),
            mcq("hieu", "Một vật trượt trên mặt bàn nằm ngang chịu tác dụng của trọng lực $\\vec{P}$, phản lực pháp tuyến $\\vec{N}$, lực kéo $\\vec{F}_k$ (cùng chiều chuyển động) và lực ma sát trượt $\\vec{F}_{\\text{mst}}$. Những lực nào **không** sinh công ($A = 0$)?", ["Trọng lực $\\vec{P}$ và phản lực pháp tuyến $\\vec{N}$ (vì vuông góc với mặt bàn, $\\alpha = 90^\\circ$)", "Lực kéo $\\vec{F}_k$ và lực ma sát $\\vec{F}_{\\text{mst}}$", "Chỉ có lực ma sát $\\vec{F}_{\\text{mst}}$", "Không có lực nào bằng $0$"], 0, "Vì $\\vec{P}$ và $\\vec{N}$ có phương thẳng đứng vuông góc với độ dịch chuyển ngang ($\\alpha = 90^\\circ, \\cos 90^\\circ = 0$) nên $A_P = A_N = 0$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về công và công suất:", [
                "Công là một đại lượng vô hướng, có thể dương, âm hoặc bằng không.",
                "Lực ma sát trượt ngược chiều chuyển động ($\\alpha = 180^\\circ$) thực hiện công cản $A_{\\text{ms}} = -F_{\\text{mst}} \\cdot s$.",
                "Đơn vị $1\\text{ kWh}$ là đơn vị đo công suất.",
                "Một ô tô chạy thẳng đều với vận tốc $v = 20\\text{ m/s}$ dưới lực kéo $F = 1500\\text{ N}$ cùng hướng chuyển động thì công suất của lực kéo là $30\\,000\\text{ W} = 30\\text{ kW}$.",
            ], [True, True, False, True], "Ý c) sai vì $1\\text{ kWh} = 3{,}6 \\cdot 10^6\\text{ J}$ là đơn vị của công (năng lượng), còn đơn vị công suất là $\\text{W}$ hoặc $\\text{kW}$."),
            short("vandung", "Một người kéo một kiện hàng đi được quãng đường $s = 20\\text{ m}$ trên sàn ngang bằng lực kéo $F = 100\\text{ N}$ hợp với phương ngang góc $\\alpha = 60^\\circ$ ($\\cos 60^\\circ = 0{,}5$). Công của lực kéo bằng bao nhiêu Joule ($\\text{J}$)?", ["1000"], "Áp dụng công thức $A = F \\cdot s \\cdot \\cos 60^\\circ = 100 \\cdot 20 \\cdot 0{,}5 = 1000\\text{ J}$.", unit="J"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 18: Động năng và thế năng",
        icon="🏹",
        description="Công thức động năng W_đ = ½mv², định lí động năng W_đ2 - W_đ1 = A, thế năng trọng trường W_t = mgh và công của trọng lực.",
        requirements=[
            "Viết được công thức động năng $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$ và chứng minh, vận dụng được định lí động năng: độ biến thiên động năng bằng công của ngoại lực ($W_{\\text{đ}2} - W_{\\text{đ}1} = A$).",
            "Viết và vận dụng được công thức thế năng trọng trường $W_{\\text{t}} = mgh$ (phụ thuộc vào việc chọn gốc thế năng).",
            "Nêu được công của trọng lực không phụ thuộc hình dạng đường đi mà chỉ phụ thuộc hiệu độ cao điểm đầu và điểm cuối: $A_P = W_{\\text{t}1} - W_{\\text{t}2} = mg(h_1 - h_2)$.",
        ],
        definition="Động năng của một vật có khối lượng $m$ đang chuyển động với tốc độ $v$ là $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$; độ biến thiên động năng của vật bằng tổng công của các ngoại lực tác dụng lên vật ($W_{\\text{đ}2} - W_{\\text{đ}1} = A$). Thế năng trọng trường của vật ở độ cao $h$ so với gốc thế năng là $W_{\\text{t}} = mgh$.",
        theory=(
            "### 1. Động năng và Định lí động năng\n"
            "- **Động năng**: $W_{\\text{đ}} = \\dfrac{1}{2}mv^2$ (vô hướng, luôn $\\ge 0$, phụ thuộc hệ quy chiếu).\n"
            "- **Định lí động năng**:\n"
            "  $$\\Delta W_{\\text{đ}} = W_{\\text{đ}2} - W_{\\text{đ}1} = \\dfrac{1}{2}mv_2^2 - \\dfrac{1}{2}mv_1^2 = A_{\\text{ngoại lực}}$$\n"
            "  - Nếu ngoại lực sinh công dương ($A > 0$) thì động năng của vật tăng ($W_{\\text{đ}2} > W_{\\text{đ}1}$).\n"
            "  - Nếu ngoại lực sinh công âm ($A < 0$, như lực cản, lực phanh) thì động năng của vật giảm.\n\n"
            "### 2. Thế năng trọng trường và Công của trọng lực\n"
            "- Chọn mặt phẳng ngang làm **mốc (gốc) thế năng** ($W_{\\text{t}} = 0$): tại độ cao $h$ so với mốc, thế năng trọng trường là $W_{\\text{t}} = mgh$ ($h > 0$ nếu ở trên mốc, $h < 0$ nếu ở dưới mốc).\n"
            "- **Liên hệ với công của trọng lực**: Khi vật đi từ độ cao $h_1$ đến độ cao $h_2$:\n"
            "  $$A_{12} = W_{\\text{t}1} - W_{\\text{t}2} = mg(h_1 - h_2)$$"
        ),
        formulas=[
            G(
                "Định lí động năng và Thế năng trọng trường",
                F("Động năng và Định lí động năng", "$W_{\\text{đ}} = \\dfrac{1}{2}mv^2; \\qquad W_{\\text{đ}2} - W_{\\text{đ}1} = \\dfrac{1}{2}mv_2^2 - \\dfrac{1}{2}mv_1^2 = A$", "Độ biến thiên động năng của vật bằng công của hợp lực tác dụng lên vật."),
                F("Thế năng trọng trường và Công của trọng lực", "$W_{\\text{t}} = mgh; \\qquad A_{12} = W_{\\text{t}1} - W_{\\text{t}2} = mg(h_1 - h_2)$", "Hiệu thế năng giữa hai điểm không phụ thuộc vào việc chọn gốc thế năng."),
            )
        ],
        example="Một viên đạn có khối lượng $m = 20\\text{ g} = 0{,}02\\text{ kg}$ đang bay ngang với vận tốc $v_1 = 200\\text{ m/s}$ thì xuyên qua một tấm gỗ dày và bay ra ngoài với vận tốc $v_2 = 100\\text{ m/s}$. Hãy tính độ biến thiên động năng của viên đạn và công của lực cản tấm gỗ tác dụng lên viên đạn.",
        example_answer="Động năng đầu của viên đạn là $W_{\\text{đ}1} = \\dfrac{1}{2}mv_1^2 = \\dfrac{1}{2} \\cdot 0{,}02 \\cdot 200^2 = 400\\text{ J}$. Động năng sau khi xuyên qua gỗ là $W_{\\text{đ}2} = \\dfrac{1}{2}mv_2^2 = \\dfrac{1}{2} \\cdot 0{,}02 \\cdot 100^2 = 100\\text{ J}$. Theo định lí động năng, công của lực cản tấm gỗ bằng độ biến thiên động năng: $A_c = W_{\\text{đ}2} - W_{\\text{đ}1} = 100 - 400 = -300\\text{ J}$.",
        real_life="Búa máy đóng cọc bê tông được nâng lên độ cao lớn để tích trữ thế năng trọng trường $W_{\\text{t}} = mgh$, khi thả rơi sẽ chuyển hóa thành động năng cực lớn để đóng sâu cọc xuống nền đất.",
        quiz=[
            mcq("biet", "Nội dung nào sau đây phát biểu đúng **Định lí động năng**?", ["Độ biến thiên động năng của một vật bằng công của ngoại lực tác dụng lên vật ($W_{\\text{đ}2} - W_{\\text{đ}1} = A$)", "Tổng động năng của mọi vật luôn bằng không", "Động năng của vật tỉ lệ nghịch với vận tốc của vật", "Độ biến thiên động năng luôn bằng thế năng trọng trường"], 0, "Theo định lí động năng: $W_{\\text{đ}2} - W_{\\text{đ}1} = A$."),
            mcq("biet", "Tại nơi có gia tốc trọng trường $g$, một vật có khối lượng $m$ ở độ cao $h$ so với mốc thế năng có thế năng trọng trường được tính bằng công thức nào?", ["$W_{\\text{t}} = mgh$", "$W_{\\text{t}} = \\dfrac{1}{2}mgh^2$", "$W_{\\text{t}} = \\dfrac{mg}{h}$", "$W_{\\text{t}} = \\dfrac{1}{2}mv^2$"], 0, "Thế năng trọng trường của vật ở độ cao $h$ so với mốc thế năng là $W_{\\text{t}} = mgh$."),
            mcq("hieu", "Một vật trượt từ đỉnh một mặt phẳng nghiêng cao $h = 3\\text{ m}$ xuống chân mặt phẳng nghiêng có chiều dài $s = 6\\text{ m}$. Công của trọng lực tác dụng lên vật phụ thuộc vào yếu tố nào?", ["Chỉ phụ thuộc vào trọng lượng $mg$ và hiệu độ cao $h = 3\\text{ m}$ giữa đỉnh và chân dốc ($A_P = mgh$), không phụ thuộc hình dạng đường đi", "Phụ thuộc vào hệ số ma sát của mặt nghiêng", "Chỉ phụ thuộc vào vận tốc đầu của vật", "Bằng $0$ vì trọng lực vuông góc với mặt nghiêng"], 0, "Trọng lực là lực thế nên công của trọng lực chỉ phụ thuộc vào vị trí điểm đầu và điểm cuối: $A_P = mg(h_1 - h_2) = mgh$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về động năng và thế năng:", [
                "Động năng của một vật luôn không âm ($W_{\\text{đ}} \\ge 0$), còn thế năng trọng trường có thể dương, âm hoặc bằng $0$ tùy thuộc vị trí gốc thế năng.",
                "Nếu tổng công của ngoại lực tác dụng lên vật là công cản ($A < 0$) thì động năng của vật giảm đi.",
                "Hiệu thế năng của một vật giữa hai độ cao $A$ và $B$ thay đổi khi ta chọn gốc thế năng khác nhau.",
                "Một vật nặng $2\\text{ kg}$ ở độ cao $5\\text{ m}$ so với mặt đất (gốc thế năng, $g = 10\\text{ m/s}^2$) có thế năng trọng trường là $100\\text{ J}$.",
            ], [True, True, False, True], "Ý c) sai vì giá trị thế năng tại từng điểm phụ thuộc gốc thế năng, nhưng **hiệu thế năng** $W_{\\text{t}A} - W_{\\text{t}B} = mg(h_A - h_B)$ thì không phụ thuộc vào việc chọn gốc thế năng."),
            short("vandung", "Một vật có động năng ban đầu $W_{\\text{đ}1} = 25\\text{ J}$. Sau khi chịu tác dụng của một lực kéo thực hiện công phát động $A = 45\\text{ J}$ (bỏ qua ma sát), động năng $W_{\\text{đ}2}$ của vật bằng bao nhiêu Joule ($\\text{J}$)?", ["70"], "Theo định lí động năng: $W_{\\text{đ}2} = W_{\\text{đ}1} + A = 25 + 45 = 70\\text{ J}$.", unit="J"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 19: Cơ năng và định luật bảo toàn cơ năng. Hiệu suất",
        icon="🎡",
        description="Cơ năng W = W_đ + W_t, định luật bảo toàn cơ năng khi vật chỉ chịu tác dụng của trọng lực và công thức hiệu suất H = (W_ích/W_tp).100%.",
        requirements=[
            "Phát biểu và vận dụng được định luật bảo toàn cơ năng: khi vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực thì cơ năng của vật được bảo toàn ($W = \\dfrac{1}{2}mv^2 + mgh = \\text{const}$).",
            "Vận dụng được hệ quả bảo toàn cơ năng để tìm vận tốc cực đại ở vị trí thấp nhất và độ cao cực đại ($v_{\\max} = \\sqrt{2gh_{\\max}}$).",
            "Tính được hiệu suất của một quá trình hoặc động cơ theo công thức $H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\% = \\dfrac{A_{\\text{ích}}}{A_{\\text{tp}}} \\cdot 100\\%$.",
        ],
        definition="Khi một vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực (bỏ qua ma sát và lực cản), cơ năng của vật là một đại lượng bảo toàn: $W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}mv^2 + mgh = \\text{const}$. Hiệu suất của thiết bị là tỉ số giữa năng lượng có ích và năng lượng toàn phần: $H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\%$.",
        theory=(
            "### 1. Định luật bảo toàn cơ năng trong trọng trường\n"
            "- Cơ năng của vật: $W = W_{\\text{đ}} + W_{\\text{t}} = \\dfrac{1}{2}mv^2 + mgh$.\n"
            "- Khi vật chỉ chịu tác dụng của trọng lực (hoặc thêm phản lực pháp tuyến $\\vec{N}$, lực căng dây $\\vec{T}$ vuông góc với quỹ đạo không sinh công):\n"
            "  $$W_1 = W_2 \\iff \\dfrac{1}{2}mv_1^2 + mgh_1 = \\dfrac{1}{2}mv_2^2 + mgh_2$$\n"
            "- Tại vị trí cao nhất ($h_{\\max}, v = 0$): $W = W_{\\text{t max}} = mgh_{\\max}$. Tại vị trí thấp nhất ($h = 0, v_{\\max}$): $W = W_{\\text{đ max}} = \\dfrac{1}{2}mv_{\\max}^2 \\implies v_{\\max} = \\sqrt{2gh_{\\max}}$.\n"
            "- *Chú ý*: Nếu có lực ma sát hoặc lực cản sinh công $A_{\\text{cản}} < 0$ thì cơ năng không bảo toàn và độ biến thiên cơ năng bằng công của lực cản: $W_2 - W_1 = A_{\\text{cản}}$.\n\n"
            "### 2. Hiệu suất của máy móc, động cơ\n"
            "- Biểu thức hiệu suất:\n"
            "  $$H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\% = \\dfrac{A_{\\text{ích}}}{A_{\\text{tp}}} \\cdot 100\\% = \\dfrac{\\mathcal{P}_{\\text{ích}}}{\\mathcal{P}_{\\text{tp}}} \\cdot 100\\%$$\n"
            "- Vì luôn có năng lượng hao phí ($W_{\\text{hp}} > 0$) nên hiệu suất của mọi máy thực tế luôn nhỏ hơn $100\\%$ ($H < 100\\%$)."
        ),
        formulas=[
            G(
                "Định luật bảo toàn cơ năng và Hiệu suất",
                F("Phương trình bảo toàn cơ năng", "$\\dfrac{1}{2}mv_1^2 + mgh_1 = \\dfrac{1}{2}mv_2^2 + mgh_2 = \\text{const}$", "Chỉ áp dụng khi bỏ qua ma sát và sức cản môi trường. Khi có lực cản: $W_2 - W_1 = A_{\\text{cản}}$."),
                F("Công thức tính hiệu suất", "$H = \\dfrac{A_{\\text{ích}}}{A_{\\text{tp}}} \\cdot 100\\% = \\dfrac{\\mathcal{P}_{\\text{ích}}}{\\mathcal{P}_{\\text{tp}}} \\cdot 100\\% \\quad (W_{\\text{tp}} = W_{\\text{ích}} + W_{\\text{hp}})$", "Hiệu suất của mọi động cơ thực tế luôn nhỏ hơn $100\\%$."),
            )
        ],
        example="Từ mặt đất, một vật nhỏ được ném thẳng đứng lên cao với vận tốc ban đầu $v_0 = 10\\text{ m/s}$. Bỏ qua sức cản của không khí và lấy $g = 10\\text{ m/s}^2$. Dùng định luật bảo toàn cơ năng, hãy tính độ cao cực đại $h_{\\max}$ mà vật đạt tới và độ cao tại đó động năng bằng thế năng ($W_{\\text{đ}} = W_{\\text{t}}$).",
        example_answer="Chọn gốc thế năng tại mặt đất ($h_0 = 0$). Cơ năng tại mặt đất bằng cơ năng tại đỉnh cao nhất ($v = 0$): $\\dfrac{1}{2}mv_0^2 = mgh_{\\max} \\implies h_{\\max} = \\dfrac{v_0^2}{2g} = \\dfrac{10^2}{2 \\cdot 10} = 5\\text{ m}$. Tại vị trí có $W_{\\text{đ}} = W_{\\text{t}}$ thì $W = 2W_{\\text{t}} = mgh_{\\max} \\implies h = \\dfrac{h_{\\max}}{2} = 2{,}5\\text{ m}$.",
        real_life="Tàu lượn siêu tốc (Roller Coaster) chỉ dùng động cơ kéo toa tàu lên đỉnh dốc cao nhất lúc ban đầu, sau đó toa tàu tự lao xuống và vượt qua các vòng xoắn nhờ sự chuyển hóa liên tục giữa thế năng và động năng.",
        quiz=[
            mcq("biet", "Định luật bảo toàn cơ năng ($W = W_{\\text{đ}} + W_{\\text{t}} = \\text{const}$) được áp dụng đúng trong điều kiện nào?", ["Khi vật chỉ chịu tác dụng của trọng lực (hoặc lực đàn hồi) và bỏ qua mọi lực ma sát, lực cản", "Khi vật trượt có ma sát rất lớn trên mặt sàn nhám", "Khi quả cầu rơi chậm dần trong dầu nhớt đặc", "Khi ô tô đang đạp phanh gấp làm lốp xe bốc khói"], 0, "Cơ năng chỉ bảo toàn khi vật chuyển động chỉ dưới tác dụng của các lực thế (trọng lực, lực đàn hồi), không có ma sát hay lực cản."),
            mcq("biet", "Công thức tính hiệu suất $H$ của một thiết bị tiêu thụ năng lượng toàn phần $W_{\\text{tp}}$ và sinh ra năng lượng có ích $W_{\\text{ích}}$ là gì?", ["$H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\%$", "$H = \\dfrac{W_{\\text{tp}}}{W_{\\text{ích}}} \\cdot 100\\%$", "$H = (W_{\\text{tp}} - W_{\\text{ích}}) \\cdot 100\\%$", "$H = \\dfrac{W_{\\text{hp}}}{W_{\\text{ích}}} \\cdot 100\\%$"], 0, "Hiệu suất bằng tỉ số phần trăm giữa năng lượng có ích và năng lượng toàn phần: $H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\%$."),
            mcq("hieu", "Một con lắc đơn gồm quả nặng treo vào sợi dây không dãn đang dao động không ma sát quanh vị trí cân bằng thấp nhất $O$. Tại vị trí thấp nhất $O$, động năng và thế năng của quả nặng có giá trị như thế nào?", ["Động năng đạt cực đại và thế năng đạt cực tiểu", "Thế năng đạt cực đại và động năng bằng $0$", "Động năng và thế năng đều bằng $0$", "Cơ năng bằng $0$"], 0, "Tại vị trí cân bằng thấp nhất $O$, độ cao thấp nhất nên thế năng cực tiểu, toàn bộ thế năng đã chuyển hóa thành động năng nên động năng đạt cực đại."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về bảo toàn cơ năng và hiệu suất:", [
                "Khi vật rơi tự do từ độ cao $h$, thế năng giảm bao nhiêu thì động năng tăng thêm bấy nhiêu.",
                "Nếu có lực ma sát trượt tác dụng lên vật thì cơ năng của vật giảm dần và chuyển hóa thành nhiệt năng.",
                "Trong thực tế có thể chế tạo được động cơ vĩnh cửu có hiệu suất lớn hơn $100\\%$.",
                "Một vật được thả trượt không vận tốc đầu từ đỉnh dốc nhẵn không ma sát cao $h = 1{,}8\\text{ m}$ ($g = 10\\text{ m/s}^2$) có tốc độ ở chân dốc là $v = \\sqrt{2gh} = 6\\text{ m/s}$.",
            ], [True, True, False, True], "Ý c) sai vì theo định luật bảo toàn năng lượng, luôn có hao phí nên hiệu suất mọi máy thực tế luôn nhỏ hơn $100\\%$."),
            short("vandung", "Một động cơ điện tiêu thụ công suất điện toàn phần $\\mathcal{P}_{\\text{tp}} = 500\\text{ W}$ và sinh ra công suất cơ học có ích $\\mathcal{P}_{\\text{ích}} = 425\\text{ W}$. Hiệu suất $H$ của động cơ bằng bao nhiêu phần trăm ($\\%$)?", ["85"], "Áp dụng công thức $H = \\dfrac{\\mathcal{P}_{\\text{ích}}}{\\mathcal{P}_{\\text{tp}}} \\cdot 100\\% = \\dfrac{425}{500} \\cdot 100\\% = 85\\%$.", unit="%"),
        ],
    ),
    bai(
        topic=CH5[0], chapter_title=CH5[1], chapter_desc=CH5[2],
        title="Bài 20: Động lượng và xung lượng của lực",
        icon="🎱",
        description="Khái niệm vectơ động lượng p = m.v (kg.m/s), xung lượng của lực F.Δt và định lí biến thiên động lượng F.Δt = Δp.",
        requirements=[
            "Định nghĩa được động lượng của một vật là đại lượng vectơ cùng hướng với vận tốc: $\\vec{p} = m\\vec{v}$ (đơn vị $\\text{kg}\\cdot\\text{m/s}$ hoặc $\\text{N}\\cdot\\text{s}$).",
            "Tính được động lượng của một hệ nhiều vật $\\vec{p} = \\vec{p}_1 + \\vec{p}_2$ theo quy tắc tổng hợp vectơ.",
            "Viết và vận dụng được hệ thức liên hệ giữa xung lượng của lực và độ biến thiên động lượng: $\\vec{F}\\Delta t = \\Delta\\vec{p} = \\vec{p}_2 - \\vec{p}_1$.",
        ],
        definition="Động lượng của một vật có khối lượng $m$ đang chuyển động với vận tốc $\\vec{v}$ là đại lượng vectơ được xác định bởi công thức $\\vec{p} = m\\vec{v}$ (đơn vị $\\text{kg}\\cdot\\text{m/s}$). Độ biến thiên động lượng của một vật trong khoảng thời gian $\\Delta t$ bằng xung lượng của hợp lực tác dụng lên vật trong khoảng thời gian đó: $\\vec{F}\\Delta t = \\Delta\\vec{p} = \\vec{p}_2 - \\vec{p}_1$.",
        theory=(
            "### 1. Động lượng\n"
            "- Biểu thức vectơ: $\\vec{p} = m\\vec{v}$ ($\\vec{p}$ luôn **cùng phương, cùng chiều** với vận tốc $\\vec{v}$).\n"
            "- Độ lớn: $p = m \\cdot v$, đơn vị trong hệ SI là $\\text{kg}\\cdot\\text{m/s}$ (hoặc $\\text{N}\\cdot\\text{s}$). Liên hệ giữa động lượng và động năng: $p = \\sqrt{2m W_{\\text{đ}}}$.\n"
            "- **Động lượng của hệ hai vật**: $\\vec{p} = \\vec{p}_1 + \\vec{p}_2$ (cùng chiều: $p = p_1 + p_2$; ngược chiều: $p = |p_1 - p_2|$; vuông góc: $p = \\sqrt{p_1^2 + p_2^2}$).\n\n"
            "### 2. Xung lượng của lực và Định lí biến thiên động lượng\n"
            "- Khi lực $\\vec{F}$ không đổi tác dụng lên vật trong khoảng thời gian $\\Delta t$, tích $\\vec{F}\\Delta t$ gọi là **xung lượng của lực** (đơn vị $\\text{N}\\cdot\\text{s}$).\n"
            "- Từ định luật 2 Newton $\\vec{F} = m\\vec{a} = m\\dfrac{\\vec{v}_2 - \\vec{v}_1}{\\Delta t}$, ta thu được dạng tổng quát:\n"
            "  $$\\vec{F}\\Delta t = \\Delta\\vec{p} = \\vec{p}_2 - \\vec{p}_1 \\iff \\vec{F} = \\dfrac{\\Delta\\vec{p}}{\\Delta t}$$\n"
            "- Ý nghĩa: Với cùng độ biến thiên động lượng $\\Delta\\vec{p}$, nếu kéo dài thời gian va chạm $\\Delta t$ thì lực va chạm $F = \\dfrac{|\\Delta p|}{\\Delta t}$ sẽ giảm đi rất nhiều."
        ),
        formulas=[
            G(
                "Động lượng và Xung lượng của lực",
                F("Biểu thức động lượng và liên hệ với động năng", "$\\vec{p} = m\\vec{v} \\implies p = m \\cdot v; \\qquad p = \\sqrt{2m W_{\\text{đ}}}$", "Đơn vị của động lượng là $\\text{kg}\\cdot\\text{m/s}$ hoặc $\\text{N}\\cdot\\text{s}$."),
                F("Định lí xung lượng của lực – độ biến thiên động lượng", "$\\vec{F} \\cdot \\Delta t = \\Delta \\vec{p} = \\vec{p}_2 - \\vec{p}_1 \\implies F = \\dfrac{|\\Delta\\vec{p}|}{\\Delta t}$", "Chú ý xét dấu vectơ khi vật bật ngược chiều sau va chạm: nếu đi tới với $v_1 > 0$ và bật ngược lại với $v_2 < 0$ thì $|\\Delta p| = m(|v_2| + |v_1|)$."),
            )
        ],
        example="Một quả bóng có khối lượng $m = 0{,}4\\text{ kg}$ đang nằm yên trên mặt cỏ thì được cầu thủ sút một lực trong thời gian tiếp xúc $\\Delta t = 0{,}02\\text{ s}$, làm quả bóng bay đi với tốc độ $v = 25\\text{ m/s}$. Hãy tính độ biến thiên động lượng của quả bóng và độ lớn trung bình của lực sút.",
        example_answer="Ban đầu quả bóng đứng yên nên $p_1 = 0$. Ngay sau khi sút, động lượng quả bóng là $p_2 = mv = 0{,}4 \\cdot 25 = 10\\text{ kg}\\cdot\\text{m/s}$. Độ biến thiên động lượng là $\\Delta p = p_2 - p_1 = 10\\text{ kg}\\cdot\\text{m/s}$. Độ lớn lực sút trung bình là $F = \\dfrac{\\Delta p}{\\Delta t} = \\dfrac{10}{0{,}02} = 500\\text{ N}$.",
        real_life="Túi khí an toàn trên ô tô, đệm mút dày dưới xà nhảy cao và động tác chùng gối khi nhảy từ trên cao xuống đất đều nhằm mục đích tăng thời gian va chạm $\\Delta t$ để giảm lực xung kích $F = \\dfrac{\\Delta p}{\\Delta t}$, tránh chấn thương.",
        quiz=[
            mcq("biet", "Công thức định nghĩa vectơ động lượng $\\vec{p}$ của một vật có khối lượng $m$ đang chuyển động với vận tốc $\\vec{v}$ là gì?", ["$\\vec{p} = m\\vec{v}$", "$p = \\dfrac{1}{2}mv^2$", "$\\vec{p} = m\\vec{a}$", "$\\vec{p} = \\dfrac{\\vec{v}}{m}$"], 0, "Vectơ động lượng của vật bằng tích khối lượng $m$ và vectơ vận tốc $\\vec{v}$: $\\vec{p} = m\\vec{v}$."),
            mcq("biet", "Đơn vị của động lượng trong hệ SI là gì?", ["$\\text{kg}\\cdot\\text{m/s}$ (hoặc $\\text{N}\\cdot\\text{s}$)", "$\\text{kg}\\cdot\\text{m/s}^2$", "$\\text{J/s}$", "$\\text{N/m}$"], 0, "Vì $p = m \\cdot v$ nên đơn vị động lượng là $\\text{kg}\\cdot\\text{m/s}$, tương đương với đơn vị xung lượng lực $\\text{N}\\cdot\\text{s}$."),
            mcq("hieu", "Vì sao khi bắt một quả bóng đang bay rất nhanh, thủ môn luôn có động tác co tay lùi dần về phía sau theo đà bóng thay vì giữ cứng đơ bàn tay?", ["Để kéo dài thời gian tiếp xúc $\\Delta t$ khi dừng bóng, từ đó làm giảm độ lớn lực va đập $F = \\dfrac{\\Delta p}{\\Delta t}$ tác dụng lên tay", "Để làm giảm thời gian tiếp xúc $\\Delta t$ xuống gần bằng $0$", "Để làm tăng độ biến thiên động lượng $\\Delta p$ của quả bóng", "Để làm tăng khối lượng của quả bóng"], 0, "Độ biến thiên động lượng $\\Delta p = 0 - mv$ là xác định; việc lùi tay theo bóng giúp tăng thời gian dừng bóng $\\Delta t$, làm giảm lực đập $F$ không gây đau tay."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về động lượng và xung lượng của lực:", [
                "Vectơ động lượng $\\vec{p}$ luôn cùng hướng với vectơ vận tốc $\\vec{v}$ của vật.",
                "Độ biến thiên động lượng của một vật trong khoảng thời gian $\\Delta t$ bằng xung lượng của hợp lực tác dụng lên vật trong khoảng thời gian đó.",
                "Hai vật có cùng khối lượng và chuyển động với cùng tốc độ theo hai hướng vuông góc nhau thì có vectơ động lượng bằng nhau.",
                "Một vật có khối lượng $m = 2\\text{ kg}$ chuyển động với tốc độ $v = 6\\text{ m/s}$ có độ lớn động lượng là $12\\text{ kg}\\cdot\\text{m/s}$.",
            ], [True, True, False, True], "Ý c) sai vì động lượng là đại lượng vectơ; hai vật chuyển động theo hai hướng vuông góc thì hai vectơ động lượng khác hướng nên $\\vec{p}_1 \\ne \\vec{p}_2$."),
            short("vandung", "Một vật có khối lượng $m = 5\\text{ kg}$ đang chuyển động thẳng với vận tốc $v = 8\\text{ m/s}$. Độ lớn động lượng $p$ của vật bằng bao nhiêu $\\text{kg}\\cdot\\text{m/s}$?", ["40"], "Áp dụng công thức $p = m \\cdot v = 5 \\cdot 8 = 40\\text{ kg}\\cdot\\text{m/s}$.", unit="kg.m/s"),
        ],
    ),
    bai(
        topic=CH5[0], chapter_title=CH5[1], chapter_desc=CH5[2],
        title="Bài 21: Định luật bảo toàn động lượng và các loại va chạm",
        icon="🚀",
        description="Hệ kín (hệ cô lập), định luật bảo toàn động lượng, phân biệt va chạm đàn hồi và va chạm mềm, chuyển động bằng phản lực.",
        requirements=[
            "Nêu được khái niệm hệ kín (hệ cô lập) và phát biểu, viết được biểu thức của Định luật bảo toàn động lượng: $\\vec{p}_1 + \\vec{p}_2 = \\vec{p}_1' + \\vec{p}_2'$.",
            "Phân biệt được va chạm đàn hồi (bảo toàn cả động lượng và động năng) và va chạm mềm (hai vật dính vào nhau chuyển động cùng vận tốc $v' = \\dfrac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$, động năng giảm chuyển thành nhiệt).",
            "Giải thích được hiện tượng súng giật lùi khi bắn và nguyên tắc chuyển động bằng phản lực của tên lửa.",
        ],
        definition="Định luật bảo toàn động lượng: Động lượng toàn phần của một hệ kín (hệ cô lập) là một đại lượng bảo toàn: $\\vec{p}_{\\text{trước}} = \\vec{p}_{\\text{sau}} \\iff m_1\\vec{v}_1 + m_2\\vec{v}_2 = m_1\\vec{v}_1' + m_2\\vec{v}_2'$.",
        theory=(
            "### 1. Hệ kín và Định luật bảo toàn động lượng\n"
            "- **Hệ kín (hệ cô lập)**: hệ nhiều vật không có ngoại lực tác dụng, hoặc các ngoại lực cân bằng nhau, hoặc nội lực rất lớn so với ngoại lực trong thời gian cực ngắn (như lúc va chạm, đạn nổ, pháo hoa nổ).\n"
            "- **Định luật bảo toàn động lượng**:\n"
            "  $$m_1\\vec{v}_1 + m_2\\vec{v}_2 = m_1\\vec{v}_1' + m_2\\vec{v}_2'$$\n\n"
            "### 2. Hai loại va chạm và Chuyển động bằng phản lực\n"
            "1. **Va chạm đàn hồi**: sau va chạm hai vật tách rời nhau, không để lại biến dạng dư; **cả động lượng và động năng đều được bảo toàn**.\n"
            "2. **Va chạm mềm (hoàn toàn không đàn hồi)**: sau va chạm hai vật **dính vào nhau** và chuyển động với cùng một vận tốc $\\vec{v}'$:\n"
            "   $$m_1\\vec{v}_1 + m_2\\vec{v}_2 = (m_1 + m_2)\\vec{v}' \\implies \\vec{v}' = \\dfrac{m_1\\vec{v}_1 + m_2\\vec{v}_2}{m_1 + m_2}$$\n"
            "   (Trong va chạm mềm, động lượng được bảo toàn nhưng **động năng giảm** do một phần chuyển hóa thành nhiệt năng và công làm biến dạng vật).\n"
            "3. **Chuyển động bằng phản lực (Tên lửa, súng giật)**: Ban đầu hệ đứng yên ($\\vec{p} = \\vec{0}$), khi lượng khí (hoặc viên đạn) khối lượng $m$ phụt về phía sau với vận tốc $\\vec{v}$ thì phần vỏ tên lửa (hoặc khẩu súng) khối lượng $M$ tiến về phía trước với vận tốc $\\vec{V} = -\\dfrac{m}{M}\\vec{v}$."
        ),
        formulas=[
            G(
                "Định luật bảo toàn động lượng, Va chạm mềm và Phản lực",
                F("Vận tốc sau va chạm mềm (hai vật dính vào nhau)", "$\\vec{v}' = \\dfrac{m_1\\vec{v}_1 + m_2\\vec{v}_2}{m_1 + m_2}$", "Khi chiếu lên trục chuyển động, phải lấy đúng dấu đại số của $v_1$ và $v_2$ theo chiều dương đã chọn."),
                F("Vận tốc giật lùi / chuyển động bằng phản lực", "$m\\vec{v} + M\\vec{V} = \\vec{0} \\implies \\vec{V} = -\\dfrac{m}{M}\\vec{v}; \\qquad V = \\dfrac{m}{M}v$", "Vỏ tên lửa tiến về phía trước ngược chiều với luồng khí phụt ra phía sau."),
            )
        ],
        example="Một toa xe lăn có khối lượng $m_1 = 3\\text{ kg}$ chuyển động thẳng với vận tốc $v_1 = 4\\text{ m/s}$ đến va chạm mềm vào một toa xe thứ hai có khối lượng $m_2 = 1\\text{ kg}$ đang đứng yên ($v_2 = 0$) trên cùng đường ray ngang. Sau va chạm hai xe móc dính vào nhau và cùng chuyển động. Hãy tính vận tốc $v'$ của hai xe ngay sau va chạm.",
        example_answer="Chọn chiều dương là chiều chuyển động của xe thứ nhất. Áp dụng định luật bảo toàn động lượng cho va chạm mềm: $m_1 v_1 + m_2 v_2 = (m_1 + m_2)v' \\implies v' = \\dfrac{m_1 v_1 + 0}{m_1 + m_2} = \\dfrac{3 \\cdot 4}{3 + 1} = \\dfrac{12}{4} = 3\\text{ m/s}$.",
        real_life="Tên lửa vũ trụ có thể bay và tăng tốc trong môi trường chân không ngoài vũ trụ (nơi không có không khí để đẩy) hoàn toàn nhờ nguyên lí bảo toàn động lượng của chuyển động bằng phản lực khi phụt luồng khí nóng ra phía sau.",
        quiz=[
            mcq("biet", "Định luật bảo toàn động lượng chỉ nghiệm đúng đối với hệ vật thỏa mãn điều kiện nào?", ["Hệ kín (hệ cô lập) hoặc hệ có tổng ngoại lực bằng không", "Hệ chịu tác dụng của lực ma sát rất lớn", "Hệ chỉ gồm một vật đang rơi tự do dưới trọng lực", "Mọi hệ bất kì không cần điều kiện"], 0, "Động lượng của một hệ được bảo toàn khi hệ đó là hệ kín (hệ cô lập)."),
            mcq("biet", "Trong **va chạm mềm** giữa hai vật (sau va chạm hai vật dính vào nhau và chuyển động cùng vận tốc), đại lượng nào được bảo toàn và đại lượng nào không bảo toàn?", ["Động lượng của hệ được bảo toàn, còn động năng của hệ giảm đi (không bảo toàn)", "Cả động lượng và động năng đều được bảo toàn", "Động năng được bảo toàn, còn động lượng không bảo toàn", "Cả động lượng và động năng đều tăng lên gấp đôi"], 0, "Trong va chạm mềm, động lượng toàn phần bảo toàn nhưng một phần động năng biến thành nhiệt năng và năng lượng biến dạng."),
            mcq("hieu", "Khi bắn súng trường, người xạ thủ luôn phải tì chặt báng súng vào hõm vai vì sao?", ["Vì khi viên đạn bay về phía trước với động lượng $\\vec{p}$, thân súng sẽ giật lùi về phía sau với vận tốc $\\vec{V} = -\\dfrac{m}{M}\\vec{v}$ theo bảo toàn động lượng", "Vì viên đạn kéo thân súng bay về phía trước", "Vì thuốc súng làm báng súng lạnh đi", "Để làm giảm vận tốc của viên đạn"], 0, "Theo định luật bảo toàn động lượng ($m\\vec{v} + M\\vec{V} = \\vec{0}$), khi đạn lao về trước thì súng giật lùi về phía sau."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về bảo toàn động lượng và va chạm:", [
                "Trong va chạm hoàn toàn đàn hồi, cả động lượng và động năng của hệ đều được bảo toàn.",
                "Tên lửa vũ trụ chuyển động được trong khoảng không chân không nhờ nguyên tắc chuyển động bằng phản lực.",
                "Trong vụ nổ của một viên đạn đang bay, nội lực cực lớn so với trọng lực trong thời gian nổ rất ngắn nên động lượng của hệ ngay trước và ngay sau khi nổ được coi là bảo toàn.",
                "Khi hai vật có cùng khối lượng chuyển động ngược chiều với cùng tốc độ đến va chạm mềm dính vào nhau thì sau va chạm cả hai tiếp tục bay nhanh gấp đôi.",
            ], [True, True, True, False], "Ý d) sai vì hai vật cùng khối lượng chạy ngược chiều cùng tốc độ có tổng động lượng $\\vec{p}_1 + \\vec{p}_2 = \\vec{0}$, nên sau khi dính vào nhau cả hai dừng lại ($v' = 0$)."),
            short("vandung", "Một quả cầu đất sét nặng $m_1 = 2\\text{ kg}$ bay ngang với vận tốc $v_1 = 6\\text{ m/s}$ đến đập và dính chặt vào một khúc gỗ nặng $m_2 = 4\\text{ kg}$ đang nằm yên trên mặt sàn nhẵn không ma sát. Vận tốc $v'$ của hệ ngay sau va chạm bằng bao nhiêu $\\text{m/s}$?", ["2"], "Áp dụng công thức va chạm mềm: $v' = \\dfrac{m_1 v_1}{m_1 + m_2} = \\dfrac{2 \\cdot 6}{2 + 4} = \\dfrac{12}{6} = 2\\text{ m/s}$.", unit="m/s"),
        ],
    ),
    bai(
        topic=CH6[0], chapter_title=CH6[1], chapter_desc=CH6[2],
        title="Bài 22: Động học của chuyển động tròn đều",
        icon="🎡",
        description="Đơn vị góc radian (rad), tốc độ dài v, tốc độ góc ω = θ/t = 2π/T = 2πf, chu kì T, tần số f và hệ thức v = ω.r.",
        requirements=[
            "Đổi được số đo góc giữa độ ($^\\circ$) và radian ($\\text{rad}$) theo hệ thức $180^\\circ = \\pi\\text{ rad}$, và tính độ dài cung tròn $s = \\theta \\cdot r$.",
            "Định nghĩa và viết được công thức tốc độ góc $\\omega = \\dfrac{\\theta}{t} = \\dfrac{2\\pi}{T} = 2\\pi f$ (đơn vị $\\text{rad/s}$), chu kì $T$ ($\\text{s}$) và tần số $f$ ($\\text{Hz}$).",
            "Vận dụng được công thức liên hệ giữa tốc độ dài và tốc độ góc: $v = \\omega \\cdot r$, đồng thời nêu được hướng của vectơ vận tốc $\\vec{v}$ luôn tiếp tuyến với đường tròn quỹ đạo.",
        ],
        definition="Chuyển động tròn đều là chuyển động có quỹ đạo là một đường tròn và có tốc độ không đổi trên mọi cung tròn. Trong chuyển động tròn đều, tốc độ góc $\\omega = \\dfrac{\\theta}{t} = \\dfrac{2\\pi}{T} = 2\\pi f$ (đơn vị $\\text{rad/s}$) và tốc độ dài $v = \\omega \\cdot r$ luôn không đổi, nhưng hướng của vectơ vận tốc $\\vec{v}$ luôn thay đổi (luôn tiếp tuyến với đường tròn).",
        theory=(
            "### 1. Độ dịch chuyển góc và Tốc độ góc\n"
            "- **Đơn vị radian ($\\text{rad}$)**: cung tròn có độ dài $s$ bằng bán kính $r$ thì chắn góc ở tâm là $1\\text{ rad}$: $\\theta(\\text{rad}) = \\dfrac{s}{r}$. Đổi góc: $360^\\circ = 2\\pi\\text{ rad}$; $180^\\circ = \\pi\\text{ rad} \\implies \\alpha(\\text{rad}) = \\alpha(^\\circ) \\cdot \\dfrac{\\pi}{180^\\circ}$.\n"
            "- **Tốc độ góc ($\\omega$)**: góc mà bán kính nối tâm với vật quét được trong một đơn vị thời gian:\n"
            "  $$\\omega = \\dfrac{\\theta}{t} \\quad (\\text{đơn vị: } \\text{rad/s})$$\n\n"
            "### 2. Chu kì, Tần số và Liên hệ giữa tốc độ dài – tốc độ góc\n"
            "- **Chu kì ($T$)**: thời gian vật đi hết một vòng tròn (đơn vị $\\text{s}$): $T = \\dfrac{t}{N} = \\dfrac{2\\pi}{\\omega}$.\n"
            "- **Tần số ($f$)**: số vòng vật đi được trong $1\\text{ giây}$ (đơn vị $\\text{Hz}$ hoặc vòng/s): $f = \\dfrac{1}{T} = \\dfrac{\\omega}{2\\pi}$.\n"
            "- **Liên hệ giữa tốc độ dài $v$ và tốc độ góc $\\omega$**:\n"
            "  $$v = \\dfrac{s}{t} = \\dfrac{\\theta \\cdot r}{t} = \\omega \\cdot r = \\dfrac{2\\pi r}{T} = 2\\pi f r$$\n"
            "- Vectơ vận tốc $\\vec{v}$ tại mỗi điểm luôn **tiếp tuyến với đường tròn quỹ đạo** nên có phương liên tục thay đổi."
        ),
        formulas=[
            G(
                "Các công thức động học chuyển động tròn đều",
                F("Chu kì, tần số và tốc độ góc", "$\\omega = \\dfrac{\\theta}{t} = \\dfrac{2\\pi}{T} = 2\\pi f; \\qquad T = \\dfrac{1}{f}$", "Trong đó $T$ tính bằng $\\text{s}$, $f$ tính bằng $\\text{Hz}$, $\\omega$ tính bằng $\\text{rad/s}$ ($360^\\circ = 2\\pi\\text{ rad}$)."),
                F("Liên hệ giữa tốc độ dài và tốc độ góc", "$v = \\omega \\cdot r = \\dfrac{2\\pi r}{T} = 2\\pi f r$", "Trên cùng một vật rắn quay quanh trục (như cánh quạt, kim đồng hồ), mọi điểm có cùng $\\omega$, điểm nào xa trục quay hơn ($r$ lớn hơn) thì có tốc độ dài $v$ lớn hơn."),
            )
        ],
        example="Một cánh quạt trần quay đều với tốc độ góc $\\omega = 10\\text{ rad/s}$. Xét một điểm ở đầu mút cánh quạt cách trục quay một khoảng $r = 0{,}6\\text{ m}$. Hãy tính tốc độ dài $v$ của điểm đó.",
        example_answer="Áp dụng công thức liên hệ giữa tốc độ dài và tốc độ góc: $v = \\omega \\cdot r = 10 \\cdot 0{,}6 = 6\\text{ m/s}$.",
        real_life="Các vệ tinh địa tĩnh (vệ tinh viễn thông Vinasat-1, Vinasat-2) chuyển động tròn đều trong mặt phẳng xích đạo với chu kì $T = 24\\text{ h}$ bằng đúng chu kì tự quay của Trái Đất nên luôn đứng yên tương đối so với các chảo ăng-ten mặt đất.",
        quiz=[
            mcq("biet", "Công thức liên hệ giữa tốc độ dài $v$, tốc độ góc $\\omega$ và bán kính quỹ đạo $r$ của một chất điểm chuyển động tròn đều là gì?", ["$v = \\omega \\cdot r$", "$v = \\dfrac{\\omega}{r}$", "$\\omega = v \\cdot r$", "$v = \\omega^2 \\cdot r$"], 0, "Trong chuyển động tròn đều, tốc độ dài bằng tích tốc độ góc và bán kính quỹ đạo: $v = \\omega \\cdot r$."),
            mcq("biet", "Đơn vị của tốc độ góc $\\omega$ trong hệ SI là gì?", ["$\\text{rad/s}$", "$\\text{m/s}$", "$\\text{m/s}^2$", "$\\text{N}\\cdot\\text{m}$"], 0, "Tốc độ góc $\\omega = \\dfrac{\\theta}{t}$ có đơn vị chuẩn trong hệ SI là radian trên giây ($\\text{rad/s}$)."),
            mcq("hieu", "Trong chuyển động tròn đều, phát biểu nào sau đây là **đúng** khi nói về vectơ vận tốc $\\vec{v}$ của vật?", ["Vectơ vận tốc $\\vec{v}$ có độ lớn không đổi nhưng có hướng luôn thay đổi (luôn tiếp tuyến với quỹ đạo tròn)", "Vectơ vận tốc $\\vec{v}$ không đổi cả về hướng và độ lớn", "Vectơ vận tốc $\\vec{v}$ luôn hướng thẳng vào tâm đường tròn", "Độ lớn vận tốc tăng đều theo thời gian"], 0, "Trong chuyển động tròn đều, tốc độ $v = |\\vec{v}|$ không đổi nhưng phương của $\\vec{v}$ luôn tiếp tuyến với đường tròn nên hướng của $\\vec{v}$ thay đổi liên tục."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về chuyển động tròn đều:", [
                "Góc một vòng tròn $360^\\circ$ tương ứng với $2\\pi\\text{ rad}$ và góc $180^\\circ$ tương ứng với $\\pi\\text{ rad}$.",
                "Liên hệ giữa tốc độ góc $\\omega$, chu kì $T$ và tần số $f$ là $\\omega = \\dfrac{2\\pi}{T} = 2\\pi f$.",
                "Trên một chiếc kim phút đồng hồ đang chạy, điểm ở đầu mút kim và điểm ở giữa kim có cùng tốc độ dài $v$.",
                "Một bánh xe quay đều với tần số $f = 5\\text{ Hz}$ thì có chu kì quay là $T = 0{,}2\\text{ s}$.",
            ], [True, True, False, True], "Ý c) sai vì hai điểm trên cùng một kim đồng hồ có cùng tốc độ góc $\\omega$, nhưng điểm ở đầu mút có bán kính $r$ lớn hơn nên có tốc độ dài $v = \\omega r$ lớn hơn."),
            short("vandung", "Một chất điểm chuyển động tròn đều trên đường tròn bán kính $r = 0{,}5\\text{ m}$ với tốc độ góc $\\omega = 8\\text{ rad/s}$. Tốc độ dài $v$ của chất điểm bằng bao nhiêu $\\text{m/s}$?", ["4"], "Áp dụng công thức $v = \\omega \\cdot r = 8 \\cdot 0{,}5 = 4\\text{ m/s}$.", unit="m/s"),
        ],
    ),
    bai(
        topic=CH6[0], chapter_title=CH6[1], chapter_desc=CH6[2],
        title="Bài 23: Gia tốc hướng tâm và lực hướng tâm",
        icon="🎠",
        description="Đặc điểm và công thức gia tốc hướng tâm a_ht = v²/r = ω²r, lực hướng tâm F_ht = m.v²/r = m.ω²r và ứng dụng thực tiễn.",
        requirements=[
            "Giải thích được vì sao chuyển động tròn đều có tốc độ không đổi nhưng vẫn có gia tốc (do hướng của vectơ vận tốc thay đổi liên tục) và gia tốc này luôn hướng vào tâm quỹ đạo.",
            "Viết và vận dụng được công thức tính độ lớn gia tốc hướng tâm: $a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 r$.",
            "Viết và vận dụng được công thức độ lớn lực hướng tâm $F_{\\text{ht}} = m a_{\\text{ht}} = \\dfrac{mv^2}{r} = m\\omega^2 r$ và chỉ ra bản chất lực đóng vai trò lực hướng tâm trong các bài toán thực tế.",
        ],
        definition="Trong chuyển động tròn đều, tuy độ lớn vận tốc không đổi nhưng hướng của vận tốc luôn thay đổi nên vật có gia tốc luôn hướng vào tâm quỹ đạo gọi là gia tốc hướng tâm: $a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 r$. Hợp lực tác dụng lên vật gây ra gia tốc hướng tâm gọi là lực hướng tâm: $F_{\\text{ht}} = m a_{\\text{ht}} = \\dfrac{mv^2}{r} = m\\omega^2 r$.",
        theory=(
            "### 1. Gia tốc hướng tâm\n"
            "- **Phương và chiều**: luôn nằm dọc theo bán kính và **hướng vào tâm** của đường tròn quỹ đạo ($\\vec{a}_{\\text{ht}} \\perp \\vec{v}$).\n"
            "- **Độ lớn**:\n"
            "  $$a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 \\cdot r$$\n\n"
            "### 2. Lực hướng tâm và các ví dụ thực tế\n"
            "- Lực hướng tâm **không phải là một loại lực mới**, mà là **hợp lực** của các lực thực tế đã học tác dụng lên vật làm vật chuyển động tròn đều:\n"
            "  $$F_{\\text{ht}} = m \\cdot a_{\\text{ht}} = \\dfrac{mv^2}{r} = m\\omega^2 r$$\n"
            "- **Ví dụ bản chất của lực hướng tâm**:\n"
            "  - Vệ tinh nhân tạo / Mặt Trăng quay quanh Trái Đất: **lực hấp dẫn (trọng lực)** đóng vai trò lực hướng tâm.\n"
            "  - Ô tô chạy qua đoạn đường vòng phẳng nằm ngang: **lực ma sát nghỉ** hướng vào tâm khúc cua đóng vai trò lực hướng tâm ($v_{\\max} = \\sqrt{\\mu g r}$).\n"
            "  - Khúc cua đường cao tốc, đường sắt được làm nghiêng một góc $\\alpha$ về phía tâm cong để hợp lực của trọng lực $\\vec{P}$ và phản lực $\\vec{N}$ đóng vai trò lực hướng tâm giúp xe không bị trượt văng ra ngoài."
        ),
        formulas=[
            G(
                "Công thức Gia tốc hướng tâm và Lực hướng tâm",
                F("Độ lớn gia tốc hướng tâm", "$a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 \\cdot r$", "Vectơ gia tốc hướng tâm $\\vec{a}_{\\text{ht}}$ luôn vuông góc với vectơ vận tốc tiếp tuyến $\\vec{v}$ và hướng vào tâm quỹ đạo."),
                F("Độ lớn lực hướng tâm", "$F_{\\text{ht}} = m \\cdot a_{\\text{ht}} = \\dfrac{mv^2}{r} = m\\omega^2 r$", "Trong đó $m$ là khối lượng vật ($\\text{kg}$), $v$ là tốc độ dài ($\\text{m/s}$), $\\omega$ là tốc độ góc ($\\text{rad/s}$), $r$ là bán kính quỹ đạo ($\\text{m}$)."),
            )
        ],
        example="Một xe ô tô có khối lượng $m = 1000\\text{ kg}$ chạy đều qua một khúc cua tròn phẳng nằm ngang có bán kính $r = 50\\text{ m}$ với tốc độ $v = 10\\text{ m/s}$ ($36\\text{ km/h}$). Hãy tính gia tốc hướng tâm $a_{\\text{ht}}$ và độ lớn lực hướng tâm $F_{\\text{ht}}$ tác dụng lên ô tô.",
        example_answer="Gia tốc hướng tâm của ô tô là $a_{\\text{ht}} = \\dfrac{v^2}{r} = \\dfrac{10^2}{50} = 2\\text{ m/s}^2$. Độ lớn lực hướng tâm (do lực ma sát nghỉ của mặt đường cung cấp) là $F_{\\text{ht}} = m \\cdot a_{\\text{ht}} = 1000 \\cdot 2 = 2000\\text{ N}$.",
        real_life="Tại các khúc cua trên đường cao tốc hoặc đường đua lòng chảo, mặt đường luôn được thiết kế nghiêng dốc về phía tâm khúc cua để hợp lực của phản lực mặt đường và trọng lực tạo thành lực hướng tâm giữ xe an toàn.",
        quiz=[
            mcq("biet", "Trong chuyển động tròn đều có bán kính $r$, tốc độ dài $v$ và tốc độ góc $\\omega$, công thức tính độ lớn gia tốc hướng tâm $a_{\\text{ht}}$ là gì?", ["$a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 r$", "$a_{\\text{ht}} = \\dfrac{v}{r} = \\omega r$", "$a_{\\text{ht}} = v^2 \\cdot r$", "$a_{\\text{ht}} = \\dfrac{\\omega^2}{r}$"], 0, "Độ lớn gia tốc hướng tâm là $a_{\\text{ht}} = \\dfrac{v^2}{r} = \\omega^2 r$."),
            mcq("biet", "Khi Mặt Trăng chuyển động gần như tròn đều xung quanh Trái Đất, lực nào đóng vai trò là lực hướng tâm giữ Mặt Trăng trên quỹ đạo?", ["Lực hấp dẫn giữa Trái Đất và Mặt Trăng", "Lực ma sát của không khí", "Lực đàn hồi của lò xo", "Lực đẩy Archimedes"], 0, "Lực hấp dẫn giữa Trái Đất và Mặt Trăng luôn hướng về tâm Trái Đất và đóng vai trò là lực hướng tâm."),
            mcq("hieu", "Một chất điểm chuyển động tròn đều trên đường tròn bán kính $r = 2\\text{ m}$ với tốc độ dài $v = 6\\text{ m/s}$. Gia tốc hướng tâm của chất điểm có độ lớn là bao nhiêu?", ["$18\\text{ m/s}^2$", "$3\\text{ m/s}^2$", "$12\\text{ m/s}^2$", "$36\\text{ m/s}^2$"], 0, "Ta có $a_{\\text{ht}} = \\dfrac{v^2}{r} = \\dfrac{6^2}{2} = \\dfrac{36}{2} = 18\\text{ m/s}^2$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về gia tốc hướng tâm và lực hướng tâm:", [
                "Vectơ gia tốc hướng tâm luôn hướng vào tâm của quỹ đạo tròn và vuông góc với vectơ vận tốc dài.",
                "Lực hướng tâm không phải là một loại lực mới thêm vào các lực đã biết mà là hợp lực của các lực tác dụng lên vật gây ra gia tốc hướng tâm.",
                "Trong chuyển động tròn đều, vì tốc độ $v$ không đổi nên gia tốc hướng tâm bằng $0$.",
                "Khi xe chạy vào khúc cua với tốc độ càng lớn ($v$ tăng) hoặc bán kính cua càng hẹp ($r$ nhỏ) thì lực hướng tâm cần thiết $F_{\\text{ht}} = \\dfrac{mv^2}{r}$ càng lớn, nên xe càng dễ bị trượt văng ra ngoài nếu vượt quá ma sát nghỉ cực đại.",
            ], [True, True, False, True], "Ý c) sai vì hướng của vectơ vận tốc luôn thay đổi nên chuyển động tròn đều luôn có gia tốc hướng tâm $a_{\\text{ht}} = \\dfrac{v^2}{r} > 0$."),
            short("vandung", "Một vật nhỏ có khối lượng $m = 0{,}5\\text{ kg}$ buộc vào đầu dây quay tròn đều trên mặt bàn ngang nhẵn với bán kính $r = 1\\text{ m}$ và tốc độ dài $v = 4\\text{ m/s}$. Độ lớn lực hướng tâm $F_{\\text{ht}}$ tác dụng lên vật bằng bao nhiêu Newton ($\\text{N}$)?", ["8"], "Áp dụng công thức $F_{\\text{ht}} = \\dfrac{mv^2}{r} = \\dfrac{0{,}5 \\cdot 4^2}{1} = 8\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH7[0], chapter_title=CH7[1], chapter_desc=CH7[2],
        title="Bài 24: Moment lực. Cân bằng của vật rắn",
        icon="⚖️",
        description="Moment lực M = F.d, ngẫu lực và moment ngẫu lực, quy tắc moment lực và điều kiện cân bằng tổng quát của vật rắn.",
        requirements=[
            "Tính được moment lực $M = F \\cdot d$ đối với một trục quay và vận dụng được quy tắc moment lực ($\\sum M_{\\text{ngược chiều kim đồng hồ}} = \\sum M_{\\text{cùng chiều kim đồng hồ}}$).",
            "Nêu được định nghĩa ngẫu lực (hệ hai lực song song, ngược chiều, có độ lớn bằng nhau cùng tác dụng vào một vật) và công thức moment ngẫu lực $M = F \\cdot d$.",
            "Phát biểu được hai điều kiện cân bằng tổng quát của một vật rắn: tổng các lực bằng không ($\\sum \\vec{F} = \\vec{0}$) và tổng các moment lực đối với một trục quay bất kì bằng không ($\\sum M = 0$).",
        ],
        definition="Quy tắc moment lực: Muốn cho một vật có trục quay cố định ở trạng thái cân bằng, thì tổng các moment lực có xu hướng làm vật quay theo chiều kim đồng hồ phải bằng tổng các moment lực có xu hướng làm vật quay theo chiều ngược lại. Ngẫu lực là hệ hai lực song song, ngược chiều, có độ lớn bằng nhau và cùng đặt vào một vật; moment của ngẫu lực là $M = F \\cdot d$ (với $d$ là khoảng cách giữa hai giá của hai lực).",
        theory=(
            "### 1. Moment lực và Quy tắc moment lực\n"
            "- **Moment lực**: $M = F \\cdot d$ (đơn vị $\\text{N}\\cdot\\text{m}$), trong đó $d$ là cánh tay đòn (khoảng cách vuông góc từ trục quay $O$ đến giá của lực).\n"
            "- **Quy tắc moment lực** (điều kiện cân bằng của vật có trục quay cố định):\n"
            "  $$\\sum M_{\\text{thuận}} = \\sum M_{\\text{ngược}} \\iff F_1 d_1 = F_2 d_2$$\n\n"
            "### 2. Ngẫu lực và Điều kiện cân bằng tổng quát của vật rắn\n"
            "- **Ngẫu lực**: Hệ hai lực $\\vec{F}_1, \\vec{F}_2$ song song, ngược chiều, có cùng độ lớn ($F_1 = F_2 = F$) và cùng tác dụng vào một vật (ví dụ hai tay xoay vô lăng ô tô, vặn vòi nước).\n"
            "  - Ngẫu lực có hợp lực $\\vec{F}_1 + \\vec{F}_2 = \\vec{0}$ nên không làm tịnh tiến vật mà **chỉ có tác dụng làm quay vật**.\n"
            "  - **Moment của ngẫu lực**: $M = F \\cdot d$ (với $d$ là khoảng cách vuông góc giữa hai giá của hai lực, không phụ thuộc vị trí trục quay vuông góc mặt phẳng ngẫu lực).\n"
            "- **Điều kiện cân bằng tổng quát của vật rắn**:\n"
            "  1. Tổng các lực tác dụng lên vật bằng không: $\\sum \\vec{F} = \\vec{0}$.\n"
            "  2. Tổng các moment lực tác dụng lên vật đối với một điểm (trục quay) bất kì bằng không: $\\sum M = 0$."
        ),
        formulas=[
            G(
                "Moment lực, Moment ngẫu lực và Điều kiện cân bằng vật rắn",
                F("Moment lực và Moment của ngẫu lực", "$M_{\\text{lực}} = F \\cdot d_O; \\qquad M_{\\text{ngẫu lực}} = F \\cdot d_{12}$", "Trong ngẫu lực, $F$ là độ lớn của mỗi lực và $d_{12}$ là khoảng cách giữa hai giá của hai lực (như đường kính vô lăng)."),
                F("Hai điều kiện cân bằng tổng quát của vật rắn", "$\\begin{cases} \\sum \\vec{F} = \\vec{0} \\quad (\\text{không tịnh tiến}) \\\\ \\sum M = 0 \\quad (\\text{không quay}) \\end{cases}$", "Quy tắc moment: $\\sum M_{\\text{cùng chiều KĐH}} = \\sum M_{\\text{ngược chiều KĐH}}$."),
            )
        ],
        example="Một người lái xe dùng hai tay tác dụng một ngẫu lực vào vành vô lăng ô tô có đường kính $d = 0{,}4\\text{ m}$. Biết lực của mỗi tay tiếp tuyến với vành vô lăng và có độ lớn $F = 15\\text{ N}$. Hãy tính moment của ngẫu lực đó.",
        example_answer="Khoảng cách giữa hai giá của hai lực tiếp tuyến ở hai đầu đường kính vô lăng chính bằng đường kính $d = 0{,}4\\text{ m}$. Moment của ngẫu lực là $M = F \\cdot d = 15 \\cdot 0{,}4 = 6\\text{ N}\\cdot\\text{m}$.",
        real_life="Khi xoay vô lăng ô tô, bẻ cổ xe đạp, vặn chìa khóa hay dùng tua-vít vặn ốc vít, hai ngón tay hoặc hai bàn tay ta luôn tạo ra một ngẫu lực để làm vật quay quanh trục mà không bị đẩy lệch sang bên.",
        quiz=[
            mcq("biet", "Hệ hai lực song song, ngược chiều, có độ lớn bằng nhau và cùng tác dụng vào một vật rắn (không cùng giá) được gọi là gì?", ["Ngẫu lực", "Hai lực cân bằng", "Cặp lực và phản lực của định luật 3 Newton", "Hợp lực hướng tâm"], 0, "Hệ hai lực song song, ngược chiều, cùng độ lớn và cùng đặt vào một vật (hai giá cách nhau khoảng $d > 0$) được gọi là ngẫu lực."),
            mcq("biet", "Để một vật rắn bất kì ở trạng thái cân bằng hoàn toàn (vừa không chuyển động tịnh tiến vừa không quay), cần thỏa mãn đồng thời những điều kiện nào?", ["Tổng các lực tác dụng lên vật bằng $\\vec{0}$ ($\\sum \\vec{F} = \\vec{0}$) và tổng các moment lực đối với một trục quay bất kì bằng $0$ ($\\sum M = 0$)", "Chỉ cần tổng các lực bằng $\\vec{0}$", "Chỉ cần một lực duy nhất bằng $0$", "Vật phải có khối lượng bằng $0$"], 0, "Điều kiện cân bằng tổng quát của vật rắn gồm $\\sum \\vec{F} = \\vec{0}$ và $\\sum M = 0$."),
            mcq("hieu", "Moment của một ngẫu lực gồm hai lực có độ lớn $F_1 = F_2 = F$ và khoảng cách giữa hai giá của hai lực là $d$ được tính theo công thức nào?", ["$M = F \\cdot d$", "$M = 2F \\cdot d$", "$M = \\dfrac{1}{2}F \\cdot d$", "$M = 0$"], 0, "Moment của ngẫu lực bằng $M = F_1 d_1 + F_2 d_2 = F(d_1 + d_2) = F \\cdot d$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về moment lực và ngẫu lực:", [
                "Moment của ngẫu lực không phụ thuộc vào vị trí của trục quay vuông góc với mặt phẳng chứa ngẫu lực.",
                "Ngẫu lực chỉ có tác dụng làm quay vật chứ không làm vật chuyển động tịnh tiến.",
                "Nếu một lực có giá đi qua trục quay cố định của vật thì moment của lực đó đối với trục quay có giá trị cực đại.",
                "Một thanh nhẹ nằm ngang có trục quay $O$ ở giữa: bên trái cách $O$ đoạn $0{,}4\\text{ m}$ treo vật $30\\text{ N}$, bên phải cách $O$ đoạn $0{,}6\\text{ m}$ treo vật $20\\text{ N}$ thì thanh cân bằng.",
            ], [True, True, False, True], "Ý c) sai vì khi giá của lực đi qua trục quay thì cánh tay đòn $d = 0$, nên moment lực bằng $0$ ($M = 0$)."),
            short("vandung", "Hai lực của một ngẫu lực có độ lớn $F = 25\\text{ N}$, khoảng cách giữa hai giá của ngẫu lực là $d = 0{,}2\\text{ m}$. Moment của ngẫu lực này bằng bao nhiêu $\\text{N}\\cdot\\text{m}$?", ["5"], "Áp dụng công thức moment ngẫu lực: $M = F \\cdot d = 25 \\cdot 0{,}2 = 5\\text{ N}\\cdot\\text{m}$.", unit="N.m"),
        ],
    ),
    bai(
        topic=CH7[0], chapter_title=CH7[1], chapter_desc=CH7[2],
        title="Bài 25: Biến dạng của vật rắn. Đặc tính của lò xo",
        icon="🔩",
        description="Biến dạng đàn hồi và biến dạng dẻo, biến dạng kéo và biến dạng nén, giới hạn đàn hồi và độ cứng k của lò xo.",
        requirements=[
            "Phân biệt được biến dạng đàn hồi (vật tự lấy lại hình dạng, kích thước ban đầu khi thôi tác dụng lực) và biến dạng dẻo (vật không tự lấy lại hình dạng ban đầu).",
            "Phân biệt được biến dạng kéo (chiều dài tăng: $\\Delta l = l - l_0 > 0$) và biến dạng nén (chiều dài giảm: $|\\Delta l| = l_0 - l$).",
            "Nêu được khái niệm giới hạn đàn hồi và đặc tính độ cứng $k$ (đơn vị $\\text{N/m}$) của lò xo.",
        ],
        definition="Biến dạng đàn hồi là biến dạng mà khi ngoại lực ngừng tác dụng, vật rắn tự khôi phục lại hình dạng và kích thước ban đầu. Nếu ngoại lực vượt quá một giá trị giới hạn thì vật không lấy lại được hình dạng ban đầu nữa — giới hạn đó gọi là giới hạn đàn hồi.",
        theory=(
            "### 1. Biến dạng đàn hồi, Biến dạng kéo và Biến dạng nén\n"
            "- **Biến dạng đàn hồi**: lò xo thép, dây cao su, quả bóng cao su khi bị kéo/nén vừa phải sẽ tự trở lại hình dạng cũ khi thôi lực tác dụng. Nếu biến dạng còn giữ lại sau khi thôi lực (như nặn đất sét, uốn dây chì) thì gọi là **biến dạng dẻo (biến dạng còn dư)**.\n"
            "- **Biến dạng kéo**: tác dụng cặp lực kéo dọc trục hướng ra ngoài làm chiều dài vật **tăng lên** ($l > l_0$, ví dụ dây cáp cẩu hàng, lò xo treo vật nặng).\n"
            "- **Biến dạng nén**: tác dụng cặp lực ép dọc trục hướng vào trong làm chiều dài vật **giảm đi** ($l < l_0$, ví dụ trụ cột bê tông đỡ mái nhà, chân bàn, lò xo bị ép).\n\n"
            "### 2. Đặc tính của lò xo và Giới hạn đàn hồi\n"
            "- **Độ biến dạng của lò xo**: $\\Delta l = l - l_0$ (độ lớn $|\\Delta l| = |l - l_0|$).\n"
            "- Trong **giới hạn đàn hồi**, độ lớn lực tác dụng làm biến dạng lò xo tỉ lệ thuận với độ biến dạng $|\\Delta l|$. Hệ số tỉ lệ $k = \\dfrac{F}{|\\Delta l|}$ gọi là **độ cứng (hệ số đàn hồi)** của lò xo (đơn vị $\\text{N/m}$)."
        ),
        formulas=[
            G(
                "Độ biến dạng và Độ cứng của lò xo",
                F("Độ biến dạng của lò xo", "$\\Delta l = l - l_0 \\implies \\begin{cases} l > l_0: \\text{Biến dạng kéo } (\\Delta l > 0) \\\\ l < l_0: \\text{Biến dạng nén } (\\Delta l < 0) \\end{cases}$", "Trong đó $l_0$ là chiều dài tự nhiên của lò xo khi chưa biến dạng."),
                F("Độ cứng k của lò xo trong giới hạn đàn hồi", "$k = \\dfrac{F}{|\\Delta l|} = \\dfrac{F}{|l - l_0|} \\quad (\\text{đơn vị: } \\text{N/m})$", "Lò xo có độ cứng $k$ càng lớn thì càng khó bị kéo dãn hoặc nén ngắn lại."),
            )
        ],
        example="Một lò xo có chiều dài tự nhiên $l_0 = 20\\text{ cm}$. Khi chịu lực kéo $F = 6\\text{ N}$ dọc theo trục trong giới hạn đàn hồi thì lò xo có chiều dài $l = 24\\text{ cm}$. Hãy xác định đây là biến dạng kéo hay nén, tính độ biến dạng $|\\Delta l|$ theo mét và độ cứng $k$ của lò xo.",
        example_answer="Vì $l = 24\\text{ cm} > l_0 = 20\\text{ cm}$ nên lò xo chịu **biến dạng kéo**. Độ biến dạng là $|\\Delta l| = 24 - 20 = 4\\text{ cm} = 0{,}04\\text{ m}$. Độ cứng của lò xo là $k = \\dfrac{F}{|\\Delta l|} = \\dfrac{6}{0{,}04} = 150\\text{ N/m}$.",
        real_life="Các trụ cầu bê tông và móng tòa nhà cao tầng chịu biến dạng nén, trong khi dây cáp của cầu dây văng (như cầu Cần Thơ, cầu Mỹ Thuận) chịu biến dạng kéo.",
        quiz=[
            mcq("biet", "Khi kéo dãn một lò xo vượt quá **giới hạn đàn hồi** của nó rồi buông tay ra thì hiện tượng gì xảy ra?", ["Lò xo bị biến dạng dẻo (hỏng) và không thể tự quay về chiều dài tự nhiên $l_0$ ban đầu", "Lò xo vẫn trở về đúng chiều dài tự nhiên $l_0$", "Lò xo tự động ngắn lại bằng $0$", "Khối lượng của lò xo tăng gấp đôi"], 0, "Khi vượt quá giới hạn đàn hồi, vật mất tính đàn hồi và không thể tự lấy lại kích thước ban đầu."),
            mcq("biet", "Đơn vị chuẩn của độ cứng (hệ số đàn hồi) $k$ của lò xo trong hệ SI là gì?", ["$\\text{N/m}$", "$\\text{N}\\cdot\\text{m}$", "$\\text{N/m}^2$", "$\\text{kg/m}^3$"], 0, "Vì $k = \\dfrac{F}{|\\Delta l|}$ với $F$ tính bằng $\\text{N}$ và $|\\Delta l|$ tính bằng $\\text{m}$ nên đơn vị của $k$ là $\\text{N/m}$."),
            mcq("hieu", "Các trụ cột bê tông chống đỡ mái nhà và mặt cầu chủ yếu chịu loại biến dạng nào dưới đây?", ["Biến dạng nén", "Biến dạng kéo", "Biến dạng xoắn đứt", "Không chịu biến dạng nào"], 0, "Trọng lượng của mái nhà và mặt cầu ép thẳng đứng xuống làm các trụ cột ngắn đi một lượng rất nhỏ, đó là biến dạng nén."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về biến dạng của vật rắn và lò xo:", [
                "Biến dạng của cục đất sét khi nặn tượng là biến dạng dẻo (không đàn hồi).",
                "Dây cáp thép đang treo thùng hàng của cần cẩu chịu biến dạng kéo.",
                "Độ cứng $k$ của một lò xo phụ thuộc vào độ lớn lực kéo tác dụng lên lò xo.",
                "Một lò xo có chiều dài tự nhiên $30\\text{ cm}$ khi bị nén ngắn còn $25\\text{ cm}$ có độ lớn biến dạng là $|\\Delta l| = 5\\text{ cm} = 0{,}05\\text{ m}$.",
            ], [True, True, False, True], "Ý c) sai vì độ cứng $k$ là đặc trưng riêng của bản thân chiếc lò xo (phụ thuộc chất liệu, tiết diện dây, bán kính vòng và chiều dài tự nhiên), không phụ thuộc lực kéo $F$."),
            short("vandung", "Một lò xo có chiều dài tự nhiên $l_0 = 25\\text{ cm}$. Khi tác dụng lực kéo $F = 10\\text{ N}$ trong giới hạn đàn hồi thì lò xo dài $l = 30\\text{ cm}$ (tức dãn thêm $\\Delta l = 0{,}05\\text{ m}$). Độ cứng $k$ của lò xo bằng bao nhiêu $\\text{N/m}$?", ["200"], "Độ biến dạng $\\Delta l = 30 - 25 = 5\\text{ cm} = 0{,}05\\text{ m}$. Độ cứng của lò xo là $k = \\dfrac{F}{\\Delta l} = \\dfrac{10}{0{,}05} = 200\\text{ N/m}$.", unit="N/m"),
        ],
    ),
    bai(
        topic=CH7[0], chapter_title=CH7[1], chapter_desc=CH7[2],
        title="Bài 26: Định luật Hooke",
        icon="🌀",
        description="Phát biểu và công thức Định luật Hooke F_đh = k.|Δl|, hướng của lực đàn hồi và thế năng đàn hồi W_t = ½k(Δl)².",
        requirements=[
            "Phát biểu và viết được công thức của Định luật Hooke: trong giới hạn đàn hồi, độ lớn của lực đàn hồi của lò xo tỉ lệ thuận với độ biến dạng của lò xo ($F_{\\text{đh}} = k \\cdot |\\Delta l|$).",
            "Xác định được điểm đặt, phương và chiều của lực đàn hồi (luôn ngược chiều với biến dạng: hướng vào trong khi lò xo dãn, hướng ra ngoài khi lò xo nén).",
            "Vận dụng được công thức Định luật Hooke khi treo vật thẳng đứng ($k|\\Delta l| = mg$) và công thức thế năng đàn hồi $W_{\\text{t}} = \\dfrac{1}{2}k(\\Delta l)^2$.",
        ],
        definition="Định luật Hooke: Trong giới hạn đàn hồi, độ lớn của lực đàn hồi của lò xo tỉ lệ thuận với độ biến dạng của lò xo: $F_{\\text{đh}} = k \\cdot |\\Delta l|$, trong đó $k$ là độ cứng của lò xo (đơn vị $\\text{N/m}$) và $|\\Delta l| = |l - l_0|$ là độ biến dạng của lò xo (đơn vị $\\text{m}$).",
        theory=(
            "### 1. Đặc điểm của lực đàn hồi và Định luật Hooke\n"
            "- **Điểm đặt**: ở hai đầu của lò xo (tác dụng lên vật tiếp xúc với đầu lò xo).\n"
            "- **Phương**: trùng với phương của trục lò xo.\n"
            "- **Chiều**: luôn **ngược với chiều biến dạng** của lò xo (khi lò xo bị kéo dãn thì lực đàn hồi hướng vào giữa lò xo; khi lò xo bị nén thì lực đàn hồi hướng đẩy ra hai đầu).\n"
            "- **Định luật Hooke (Robert Hooke)**:\n"
            "  $$F_{\\text{đh}} = k \\cdot |\\Delta l| = k \\cdot |l - l_0|$$\n"
            "- Đồ thị biểu diễn sự phụ thuộc của $F_{\\text{đh}}$ vào $|\\Delta l|$ trong giới hạn đàn hồi là **đoạn thẳng đi qua gốc tọa độ $O$** có hệ số góc bằng $k$.\n\n"
            "### 2. Lò xo treo thẳng đứng và Thế năng đàn hồi\n"
            "- Khi treo vật nặng khối lượng $m$ nằm cân bằng ở đầu dưới lò xo thẳng đứng: $F_{\\text{đh}} = P \\iff k \\cdot \\Delta l = m \\cdot g \\implies \\Delta l = \\dfrac{mg}{k}$.\n"
            "- **Thế năng đàn hồi** của lò xo khi biến dạng một đoạn $\\Delta l$: $W_{\\text{t đh}} = \\dfrac{1}{2}k(\\Delta l)^2$ (đơn vị $\\text{J}$)."
        ),
        formulas=[
            G(
                "Định luật Hooke và Thế năng đàn hồi",
                F("Biểu thức Định luật Hooke", "$F_{\\text{đh}} = k \\cdot |\\Delta l| = k \\cdot |l - l_0|$", "Lưu ý bắt buộc phải đổi độ biến dạng $|\\Delta l|$ ra đơn vị mét ($\\text{m}$) trước khi nhân với $k$ ($\\text{N/m}$)."),
                F("Cân bằng khi treo vật thẳng đứng và Thế năng đàn hồi", "$k \\cdot \\Delta l = m \\cdot g \\implies \\Delta l = \\dfrac{mg}{k}; \\qquad W_{\\text{t đh}} = \\dfrac{1}{2}k(\\Delta l)^2$", "Khi treo vật vào lò xo thẳng đứng cân bằng, độ giãn $\\Delta l$ tỉ lệ thuận với khối lượng $m$."),
            )
        ],
        example="Một lò xo có chiều dài tự nhiên $l_0 = 30\\text{ cm}$ và độ cứng $k = 100\\text{ N/m}$ được treo thẳng đứng. Khi treo vào đầu dưới của lò xo một vật có khối lượng $m = 400\\text{ g} = 0{,}4\\text{ kg}$ tại nơi có $g = 10\\text{ m/s}^2$, hãy tính độ giãn $\\Delta l$ và chiều dài $l$ của lò xo khi vật nằm cân bằng.",
        example_answer="Khi vật nằm cân bằng, lực đàn hồi của lò xo cân bằng với trọng lực của vật: $F_{\\text{đh}} = P \\iff k \\cdot \\Delta l = mg \\implies \\Delta l = \\dfrac{mg}{k} = \\dfrac{0{,}4 \\cdot 10}{100} = 0{,}04\\text{ m} = 4\\text{ cm}$. Chiều dài của lò xo khi đó là $l = l_0 + \\Delta l = 30 + 4 = 34\\text{ cm}$.",
        real_life="Hệ thống lò xo giảm xóc trên ô tô, xe máy và lực kế lò xo trong phòng thí nghiệm đều được thiết kế và chia vạch dựa trên sự tỉ lệ bậc nhất của Định luật Hooke.",
        quiz=[
            mcq("biet", "Trong giới hạn đàn hồi, công thức của Định luật Hooke tính độ lớn lực đàn hồi $F_{\\text{đh}}$ của lò xo có độ cứng $k$ và độ biến dạng $|\\Delta l|$ là gì?", ["$F_{\\text{đh}} = k \\cdot |\\Delta l|$", "$F_{\\text{đh}} = \\dfrac{k}{|\\Delta l|}$", "$F_{\\text{đh}} = \\dfrac{1}{2}k(\\Delta l)^2$", "$F_{\\text{đh}} = k + |\\Delta l|$"], 0, "Theo định luật Hooke, trong giới hạn đàn hồi: $F_{\\text{đh}} = k \\cdot |\\Delta l|$."),
            mcq("biet", "Chiều của lực đàn hồi xuất hiện ở hai đầu lò xo khi lò xo bị biến dạng luôn có đặc điểm gì?", ["Luôn ngược với chiều biến dạng của lò xo (chống lại nguyên nhân gây biến dạng)", "Luôn cùng chiều với chiều biến dạng của lò xo", "Luôn hướng thẳng đứng từ trên xuống dưới", "Luôn vuông góc với trục của lò xo"], 0, "Lực đàn hồi luôn có xu hướng đưa lò xo về chiều dài tự nhiên nên ngược chiều với biến dạng."),
            mcq("hieu", "Một lò xo có độ cứng $k = 50\\text{ N/m}$. Để lò xo dãn ra một đoạn $\\Delta l = 6\\text{ cm} = 0{,}06\\text{ m}$ trong giới hạn đàn hồi thì độ lớn lực đàn hồi của lò xo bằng bao nhiêu?", ["$3\\text{ N}$", "$300\\text{ N}$", "$0{,}3\\text{ N}$", "$56\\text{ N}$"], 0, "Đổi $\\Delta l = 6\\text{ cm} = 0{,}06\\text{ m}$. Theo định luật Hooke: $F_{\\text{đh}} = k \\cdot \\Delta l = 50 \\cdot 0{,}06 = 3\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Định luật Hooke:", [
                "Trong giới hạn đàn hồi, đồ thị biểu diễn độ lớn lực đàn hồi $F_{\\text{đh}}$ theo độ biến dạng $|\\Delta l|$ là một đoạn thẳng đi qua gốc tọa độ.",
                "Định luật Hooke vẫn luôn nghiệm đúng ngay cả khi ta kéo lò xo vượt xa giới hạn đàn hồi làm lò xo bị dãn đứt.",
                "Khi lò xo bị nén lại một đoạn $|\\Delta l|$, lực đàn hồi của lò xo vẫn được tính bằng công thức $F_{\\text{đh}} = k|\\Delta l|$.",
                "Một lò xo có $k = 200\\text{ N/m}$ khi dãn $\\Delta l = 0{,}1\\text{ m}$ tích trữ thế năng đàn hồi là $W_{\\text{t}} = \\dfrac{1}{2}k(\\Delta l)^2 = 1\\text{ J}$.",
            ], [True, False, True, True], "Ý b) sai vì định luật Hooke chỉ nghiệm đúng trong giới hạn đàn hồi của lò xo."),
            short("vandung", "Treo một vật có khối lượng $m = 0{,}6\\text{ kg}$ vào đầu dưới của một lò xo thẳng đứng có độ cứng $k = 120\\text{ N/m}$ tại nơi có $g = 10\\text{ m/s}^2$. Khi vật nằm cân bằng, lò xo dãn ra một đoạn $\\Delta l$ bằng bao nhiêu $\\text{cm}$?", ["5"], "Khi cân bằng: $k\\Delta l = mg \\implies \\Delta l = \\dfrac{0{,}6 \\cdot 10}{120} = 0{,}05\\text{ m} = 5\\text{ cm}$.", unit="cm"),
        ],
    ),
    bai(
        topic=CH7[0], chapter_title=CH7[1], chapter_desc=CH7[2],
        title="Bài 27: Khối lượng riêng và áp suất chất lỏng",
        icon="🌊",
        description="Khối lượng riêng ρ = m/V, áp suất trên bề mặt p = F/S, phương trình cơ bản của thủy tĩnh học p = p₀ + ρ.g.h và độ chênh lệch áp suất Δp = ρ.g.Δh.",
        requirements=[
            "Viết và vận dụng được công thức khối lượng riêng $\\rho = \\dfrac{m}{V}$ (đơn vị $\\text{kg/m}^3$) và áp suất $p = \\dfrac{F}{S}$ (đơn vị $\\text{Pa} = \\text{N/m}^2$).",
            "Thiết lập và vận dụng được công thức tính áp suất tuyệt đối tại độ sâu $h$ trong chất lỏng đứng yên: $p = p_0 + \\rho g h$ (trong đó $p_0$ là áp suất khí quyển trên mặt thoáng).",
            "Vận dụng được công thức độ chênh lệch áp suất giữa hai điểm trong lòng chất lỏng: $\\Delta p = p_2 - p_1 = \\rho g \\Delta h = \\rho g (h_2 - h_1)$.",
        ],
        definition="Tại một điểm nằm ở độ sâu $h$ trong lòng chất lỏng đứng yên có khối lượng riêng $\\rho$, áp suất tuyệt đối $p$ bằng tổng áp suất khí quyển $p_0$ trên mặt thoáng và áp suất thủy tĩnh $\\rho g h$ của cột chất lỏng: $p = p_0 + \\rho g h$. Độ chênh lệch áp suất giữa hai độ sâu $h_1$ và $h_2$ là $\\Delta p = \\rho g \\Delta h$.",
        theory=(
            "### 1. Khối lượng riêng và Áp suất\n"
            "- **Khối lượng riêng**: $\\rho = \\dfrac{m}{V}$ (đơn vị $\\text{kg/m}^3$, với $1\\text{ g/cm}^3 = 1000\\text{ kg/m}^3$).\n"
            "- **Áp suất**: $p = \\dfrac{F_N}{S}$ (đơn vị $\\text{Pa} = \\text{N/m}^2$; các đơn vị khác: $1\\text{ atm} \\approx 1{,}013 \\cdot 10^5\\text{ Pa} \\approx 760\\text{ mmHg}$; $1\\text{ bar} = 10^5\\text{ Pa}$).\n\n"
            "### 2. Phương trình cơ bản của chất lỏng đứng yên (Thủy tĩnh học)\n"
            "- Xét cột chất lỏng đứng yên có khối lượng riêng $\\rho$ ở độ sâu $h$ so với mặt thoáng (nơi có áp suất khí quyển $p_0$):\n"
            "  - **Áp suất do riêng cột chất lỏng gây ra (áp suất thủy tĩnh)**: $p_{\\text{lỏng}} = \\rho \\cdot g \\cdot h$.\n"
            "  - **Áp suất toàn phần (tuyệt đối) tại độ sâu $h$**:\n"
            "    $$p = p_0 + \\rho \\cdot g \\cdot h$$\n"
            "- **Độ chênh lệch áp suất giữa hai điểm ở độ sâu $h_1$ và $h_2$**:\n"
            "  $$\\Delta p = p_2 - p_1 = \\rho \\cdot g \\cdot (h_2 - h_1) = \\rho \\cdot g \\cdot \\Delta h$$\n"
            "- Mọi điểm nằm trên cùng một mặt phẳng nằm ngang trong cùng một chất lỏng đứng yên đều có áp suất bằng nhau."
        ),
        formulas=[
            G(
                "Khối lượng riêng và Phương trình áp suất chất lỏng",
                F("Khối lượng riêng và Áp suất bề mặt", "$\\rho = \\dfrac{m}{V}; \\qquad p = \\dfrac{F}{S} \\quad (1\\text{ Pa} = 1\\text{ N/m}^2;\\ 1\\text{ atm} \\approx 10^5\\text{ Pa})$", "Trong đó $\\rho$ tính bằng $\\text{kg/m}^3$, $F$ là áp lực vuông góc ($\\text{N}$), $S$ là diện tích bị ép ($\\text{m}^2$)."),
                F("Áp suất tuyệt đối tại độ sâu h và Độ chênh lệch áp suất", "$p = p_0 + \\rho g h; \\qquad \\Delta p = p_2 - p_1 = \\rho g \\Delta h = \\rho g (h_2 - h_1)$", "Trong nước ($\\rho = 1000\\text{ kg/m}^3, g = 10\\text{ m/s}^2$), cứ lặn sâu thêm $\\Delta h = 10\\text{ m}$ thì áp suất tăng thêm $\\Delta p = 10^5\\text{ Pa} \\approx 1\\text{ atm}$."),
            )
        ],
        example="Một tàu ngầm đang lặn ở độ sâu $h = 30\\text{ m}$ dưới mặt nước biển. Biết khối lượng riêng của nước biển là $\\rho = 1030\\text{ kg/m}^3$, gia tốc trọng trường $g = 10\\text{ m/s}^2$ và áp suất khí quyển trên mặt biển là $p_0 = 10^5\\text{ Pa} = 100\\text{ kPa}$. Hãy tính áp suất tuyệt đối $p$ tại vỏ tàu ngầm theo đơn vị $\\text{kPa}$.",
        example_answer="Áp suất do cột nước biển gây ra ở độ sâu $30\\text{ m}$ là $\\Delta p = \\rho g h = 1030 \\cdot 10 \\cdot 30 = 309\\,000\\text{ Pa} = 309\\text{ kPa}$. Áp suất tuyệt đối tại độ sâu đó là $p = p_0 + \\rho g h = 100 + 309 = 409\\text{ kPa}$.",
        real_life="Khi thợ lặn lặn sâu dưới biển, cứ xuống sâu thêm $10\\text{ m}$ thì áp suất tăng thêm khoảng $1\\text{ atm}$; vì vậy khi ngoi lên mặt nước thợ lặn phải lên từ từ theo quy trình giảm áp để tránh khí nitơ hòa tan trong máu thoát ra đột ngột gây bệnh giảm áp.",
        quiz=[
            mcq("biet", "Tại một điểm ở độ sâu $h$ trong lòng chất lỏng đứng yên có khối lượng riêng $\\rho$ (với áp suất khí quyển trên mặt thoáng là $p_0$, gia tốc trọng trường $g$), áp suất tuyệt đối $p$ được tính theo công thức nào?", ["$p = p_0 + \\rho g h$", "$p = p_0 - \\rho g h$", "$p = \\dfrac{p_0}{\\rho g h}$", "$p = p_0 + \\dfrac{\\rho g}{h}$"], 0, "Áp suất tuyệt đối tại độ sâu $h$ bằng tổng áp suất khí quyển $p_0$ và áp suất cột chất lỏng $\\rho g h$: $p = p_0 + \\rho g h$."),
            mcq("biet", "Độ chênh lệch áp suất $\\Delta p = p_2 - p_1$ giữa hai điểm có độ chênh lệch độ sâu $\\Delta h = h_2 - h_1$ trong cùng một chất lỏng đứng yên có khối lượng riêng $\\rho$ là gì?", ["$\\Delta p = \\rho g \\Delta h$", "$\\Delta p = p_0 + \\rho g \\Delta h$", "$\\Delta p = \\dfrac{\\rho g}{\\Delta h}$", "$\\Delta p = 0$"], 0, "Khi lấy hiệu $p_2 - p_1 = (p_0 + \\rho g h_2) - (p_0 + \\rho g h_1)$, áp suất khí quyển $p_0$ triệt tiêu nên $\\Delta p = \\rho g \\Delta h$."),
            mcq("hieu", "Trong một hồ nước ngọt có khối lượng riêng $\\rho = 1000\\text{ kg/m}^3$ và $g = 9{,}8\\text{ m/s}^2$, độ chênh lệch áp suất giữa hai điểm cách nhau $\\Delta h = 5\\text{ m}$ theo phương thẳng đứng bằng bao nhiêu?", ["$49\\,000\\text{ Pa}$ ($49\\text{ kPa}$)", "$9800\\text{ Pa}$", "$5000\\text{ Pa}$", "$100\\,000\\text{ Pa}$"], 0, "Ta có $\\Delta p = \\rho g \\Delta h = 1000 \\cdot 9{,}8 \\cdot 5 = 49\\,000\\text{ Pa}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về khối lượng riêng và áp suất chất lỏng:", [
                "Áp suất tại các điểm nằm trên cùng một mặt phẳng nằm ngang trong lòng một chất lỏng đứng yên luôn bằng nhau.",
                "Áp suất tại đáy một bình chứa nước phụ thuộc vào hình dạng to hay nhỏ của miệng bình chứ không phụ thuộc vào độ cao cột nước.",
                "Độ chênh lệch áp suất giữa hai mức độ sâu trong chất lỏng không phụ thuộc vào áp suất khí quyển $p_0$.",
                "Tại độ sâu $h = 10\\text{ m}$ dưới mặt hồ nước ngọt ($\\rho = 1000\\text{ kg/m}^3, g = 10\\text{ m/s}^2, p_0 = 10^5\\text{ Pa}$), áp suất tuyệt đối là $2 \\cdot 10^5\\text{ Pa}$.",
            ], [True, False, True, True], "Ý b) sai vì áp suất chất lỏng $p = p_0 + \\rho g h$ chỉ phụ thuộc bản chất chất lỏng ($\\rho$) và độ sâu $h$, không phụ thuộc hình dạng bình chứa (nghịch lí thủy tĩnh)."),
            short("vandung", "Tại một đáy hồ nước ngọt sâu $h = 8\\text{ m}$ (biết $\\rho = 1000\\text{ kg/m}^3$, lấy $g = 10\\text{ m/s}^2$ và áp suất khí quyển $p_0 = 100\\text{ kPa}$), áp suất tuyệt đối $p$ bằng bao nhiêu $\\text{kPa}$?", ["180"], "Áp suất cột nước là $\\rho g h = 1000 \\cdot 10 \\cdot 8 = 80\\,000\\text{ Pa} = 80\\text{ kPa}$. Áp suất tuyệt đối tại đáy hồ là $p = p_0 + \\rho g h = 100 + 80 = 180\\text{ kPa}$.", unit="kPa"),
        ],
    ),
]
