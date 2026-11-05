# -*- coding: utf-8 -*-
"""
Dữ liệu bài học Vật lí Lớp 10 — Bộ sách Kết nối tri thức với cuộc sống (NXB Giáo dục Việt Nam).
Biên soạn bám sát Chương trình Giáo dục phổ thông 2018 môn Vật lí và SGK Vật lí 10 KNTT (Chương I – Chương VII, Bài 1 – Bài 34).
Chuẩn hóa 100% hiển thị toán học & công thức vật lí bằng KaTeX ($ ... $).
"""

from ._helpers import F, G, mcq, short, tf4

GRADE = 10

LESSONS = [
    # =========================================================================
    # CHƯƠNG I. MỞ ĐẦU (Bài 1 -> Bài 3)
    # =========================================================================
    {
        "topic": "do-luong",
        "title": "Chương I. Mở đầu: Làm quen với Vật lí, An toàn thực hành và Sai số phép đo",
        "icon": "📏",
        "description": "Khám phá đối tượng, phương pháp nghiên cứu Vật lí, quy tắc an toàn trong phòng thực hành và cách tính sai số, ghi kết quả đo các đại lượng vật lí.",
        "requirements": [
            r"Nêu được đối tượng nghiên cứu của Vật lí học và mục tiêu của môn Vật lí; phân tích được ảnh hưởng của Vật lí đối với sự phát triển của khoa học, công nghệ và đời sống.",
            r"Nêu được ví dụ về phương pháp tìm hiểu thế giới tự nhiên dưới góc độ vật lí (phương pháp thực nghiệm và phương pháp mô hình).",
            r"Thảo luận để nêu được các quy tắc an toàn trong nghiên cứu và học tập môn Vật lí tại phòng thực hành.",
            r"Nêu được một số loại sai số đơn giản hay gặp khi đo các đại lượng vật lí (sai số hệ thống, sai số ngẫu nhiên) và cách khắc phục chúng.",
            r"Tính được giá trị trung bình $\overline{A}$, sai số tuyệt đối $\Delta A$, sai số tỉ đối $\delta A$ và biểu diễn đúng kết quả đo dưới dạng $A = \overline{A} \pm \Delta A$.",
            r"Xác định được số chữ số có nghĩa (CSCN) trong kết quả đo và thực hiện đúng quy tắc làm tròn số khi xử lí số liệu thực nghiệm.",
        ],
        "definition": r"""
**Vật lí học** là ngành khoa học tự nhiên nghiên cứu các dạng vận động tổng quát nhất của vật chất (chất và trường), năng lượng và tương tác giữa chúng ở cả cấp độ vi mô (nguyên tử, hạt nhân) lẫn vĩ mô (hành tinh, thiên hà). Trong thực nghiệm vật lí, **phép đo** là sự so sánh một đại lượng vật lí cần đo với đại lượng cùng loại được chọn làm đơn vị; mọi kết quả đo đều gắn liền với **sai số phép đo** và phải được biểu diễn kèm độ không đảm bảo đo dưới dạng $A = \overline{A} \pm \Delta A$.
""",
        "theory": r"""
### Bài 1. Làm quen với Vật lí

- **Đối tượng nghiên cứu của Vật lí:** Các dạng vận động của vật chất (chất, trường) và năng lượng.
- **Các lĩnh vực nghiên cứu chính:** Cơ học, Nhiệt học, Điện học, Điện từ học, Quang học, Âm học, Vật lí nguyên tử và hạt nhân, Vật lí lượng tử, Thuyết tương đối.
- **Mục tiêu học tập môn Vật lí:** Giúp học sinh nắm vững kiến thức, kĩ năng cốt lõi về mô hình hệ vật lí, năng lượng, sóng, lực và trường; vận dụng giải quyết vấn đề thực tiễn và định hướng nghề nghiệp thuộc khối Khoa học, Công nghệ, Kĩ thuật và Toán học (STEM).
- **Vai trò của Vật lí đối với khoa học, công nghệ và đời sống:**
  + Là cơ sở của khoa học tự nhiên (giải thích cơ chế phản ứng hóa học, hiện tượng sinh học, thiên văn học).
  + Là nền tảng của các cuộc cách mạng công nghiệp: Cách mạng công nghiệp lần thứ nhất (thế kỉ XVIII, gắn với máy hơi nước của James Watt năm $1765$ dựa trên Nhiệt học), lần thứ hai (cuối thế kỉ XIX, gắn với máy phát điện và cảm ứng điện từ của Faraday), lần thứ ba (nửa sau thế kỉ XX, gắn với bán dẫn, vi mạch, laser, tự động hóa) và lần thứ tư (đầu thế kỉ XXI, gắn với trí tuệ nhân tạo, Internet vạn vật, công nghệ nano, điện toán lượng tử).
- **Phương pháp nghiên cứu Vật lí:**
  1. **Phương pháp thực nghiệm:** Gồm $5$ bước tuần tự:
     - Bước $1$: Xác định vấn đề cần nghiên cứu (quan sát hiện tượng tự nhiên).
     - Bước $2$: Quan sát, thu thập thông tin.
     - Bước $3$: Đưa ra dự đoán khoa học (giả thuyết).
     - Bước $4$: Tiến hành thí nghiệm kiểm tra dự đoán.
     - Bước $5$: Kết luận (nếu thí nghiệm xác nhận thì giả thuyết trở thành định luật, nếu bác bỏ thì điều chỉnh giả thuyết).
  2. **Phương pháp mô hình:** Sử dụng các mô hình để mô tả, nghiên cứu tính chất của đối tượng thực:
     - *Mô hình vật chất:* Quả địa cầu, mô hình hệ Mặt Trời, mô hình máy phát điện thu nhỏ.
     - *Mô hình lí thuyết:* Chất điểm (vật có kích thước rất nhỏ so với quãng đường đi được), tia sáng, khí lí tưởng.
     - *Mô hình toán học:* Các công thức, phương trình, vectơ, đồ thị như $d = v \cdot t$ hay $\overrightarrow{F} = m\overrightarrow{a}$.

### Bài 2. Các quy tắc an toàn trong phòng thực hành Vật lí

- **An toàn khi sử dụng thiết bị thí nghiệm:**
  + Đọc kĩ hướng dẫn sử dụng, quan sát các kí hiệu cảnh báo và nắm rõ thông số định mức trước khi vận hành.
  + **Thiết bị điện:** Điện áp định mức thông thường của bộ biến áp nguồn trong phòng thí nghiệm học sinh là $6\text{ V}$, $12\text{ V}$ hoặc $24\text{ V}$, nhưng nguồn cấp đầu vào là điện xoay chiều $220\text{ V}$ rất nguy hiểm. Chỉ cắm phích điện khi công tắc nguồn ở vị trí ngắt (OFF); tuyệt đối không chạm tay trực tiếp vào dây dẫn hở, ổ cắm; kiểm tra mạch điện được giáo viên duyệt trước khi đóng điện.
  + **Thiết bị nhiệt và thủy tinh:** Không chạm tay trực tiếp vào vật đang nung nóng; dùng kẹp gỗ hoặc găng tay cách nhiệt; kiểm tra dụng cụ thủy tinh không bị nứt vỡ trước khi đun.
  + **Thiết bị quang học và laser:** Tuyệt đối không chiếu tia laser trực tiếp vào mắt người vì chùm tia có năng lượng tập trung cao gây tổn thương võng mạc.
- **Nguy cơ mất an toàn và biển báo trong phòng thực hành:**
  + **Biển báo cấm:** Hình tròn, viền đỏ, nền trắng, hình vẽ màu đen và có vạch chéo đỏ (ví dụ: Cấm lửa, Cấm uống nước, Không được vào).
  + **Biển báo cảnh báo nguy hiểm:** Hình tam giác đều, viền đen hoặc đỏ, nền vàng, hình vẽ màu đen (ví dụ: Cảnh báo điện áp cao, Chất dễ cháy, Chất độc, Nơi có chất phóng xạ, Dụng cụ sắc nhọn, Nhiệt độ cao).
  + **Biển báo bắt buộc thực hiện:** Hình tròn, nền xanh lam, hình vẽ màu trắng (ví dụ: Phải đeo kính bảo hộ, Phải mặc áo choàng phòng thí nghiệm).
  + **Biển báo chỉ dẫn an toàn, cấp cứu:** Hình chữ nhật hoặc hình vuông, nền xanh lá cây hoặc đỏ, hình vẽ màu trắng (ví dụ: Lối thoát hiểm, Bình chữa cháy, Nơi sơ cứu).

### Bài 3. Thực hành tính sai số trong phép đo. Ghi kết quả đo

- **Phân loại phép đo:**
  + **Phép đo trực tiếp:** Giá trị của đại lượng cần đo được đọc trực tiếp trên vạch chia hoặc màn hình dụng cụ đo (ví dụ: đo chiều dài bằng thước, đo khối lượng bằng cân, đo thời gian bằng đồng hồ bấm giây).
  + **Phép đo gián tiếp:** Giá trị của đại lượng cần đo được xác định thông qua các đại lượng đo trực tiếp bằng một công thức vật lí (ví dụ: đo tốc độ trung bình thông qua quãng đường $s$ và thời gian $t$ theo công thức $v = \dfrac{s}{t}$; đo khối lượng riêng theo $\rho = \dfrac{m}{V}$).
- **Phân loại sai số:**
  + **Sai số hệ thống:** Có tính quy luật, lặp lại như nhau ở mọi lần đo (làm kết quả đo luôn lớn hơn hoặc luôn nhỏ hơn giá trị thực). Nguyên nhân do dụng cụ đo chưa hiệu chỉnh điểm $0$ hoặc do độ chia nhỏ nhất (ĐCNN) của dụng cụ. Cách khắc phục: Hiệu chỉnh dụng cụ về vạch $0$ trước khi đo, sử dụng dụng cụ có độ chính xác cao. Sai số dụng cụ $\Delta A_{\text{dc}}$ thường được lấy bằng nửa độ chia nhỏ nhất hoặc một độ chia nhỏ nhất của dụng cụ.
  + **Sai số ngẫu nhiên:** Không có quy luật rõ ràng, xuất phát từ thao tác của người đo (đặt mắt lệch, bấm đồng hồ chậm hoặc sớm) hoặc điều kiện bên ngoài (gió, nhiệt độ thay đổi). Cách khắc phục: Thực hiện phép đo nhiều lần trong cùng điều kiện rồi lấy giá trị trung bình.
- **Chữ số có nghĩa (CSCN):**
  + Tất cả các chữ số khác $0$ đều là chữ số có nghĩa.
  + Các chữ số $0$ nằm giữa hai chữ số khác $0$ là chữ số có nghĩa (ví dụ: $105$ có $3$ CSCN).
  + Các chữ số $0$ ở bên phải chữ số khác $0$ trong số thập phân là chữ số có nghĩa (ví dụ: $2,50$ có $3$ CSCN).
  + Các chữ số $0$ ở đầu (bên trái chữ số khác $0$ đầu tiên) **không** phải là chữ số có nghĩa (ví dụ: $0,0042$ chỉ có $2$ CSCN là $4$ và $2$).
- **Quy tắc ghi kết quả đo:**
  + Sai số tuyệt đối $\Delta A$ thường chỉ được viết đến $1$ hoặc tối đa $2$ chữ số có nghĩa.
  + Giá trị trung bình $\overline{A}$ được làm tròn đến bậc thập phân tương ứng với bậc thập phân cuối cùng của $\Delta A$.
""",
        "formulas": [
            G(
                "Giá trị trung bình và sai số tuyệt đối (Đo trực tiếp)",
                F(
                    r"Giá trị trung bình qua $n$ lần đo",
                    r"$\overline{A} = \dfrac{A_1 + A_2 + \dots + A_n}{n}$",
                    r"$A_1, A_2, \dots, A_n$ là kết quả của $n$ lần đo trực tiếp",
                ),
                F(
                    "Sai số tuyệt đối của từng lần đo",
                    r"$\Delta A_i = |\overline{A} - A_i|$",
                    r"với $i = 1, 2, \dots, n$",
                ),
                F(
                    "Sai số tuyệt đối trung bình (sai số ngẫu nhiên)",
                    r"$\overline{\Delta A} = \dfrac{\Delta A_1 + \Delta A_2 + \dots + \Delta A_n}{n}$",
                    r"Đặc trưng cho mức độ phân tán của các lần đo",
                ),
                F(
                    "Sai số tuyệt đối của phép đo",
                    r"$\Delta A = \overline{\Delta A} + \Delta A_{\text{dc}}$",
                    r"$\Delta A_{\text{dc}}$ là sai số dụng cụ (thường lấy bằng $\dfrac{1}{2}$ hoặc $1$ ĐCNN)",
                ),
                F(
                    "Cách ghi kết quả đo",
                    r"$A = \overline{A} \pm \Delta A$",
                    r"$\overline{A}$ được làm tròn đến cùng hàng thập phân với $\Delta A$",
                ),
            ),
            G(
                "Sai số tỉ đối và quy tắc tính sai số phép đo gián tiếp",
                F(
                    "Sai số tỉ đối",
                    r"$\delta A = \dfrac{\Delta A}{\overline{A}} \cdot 100\%$",
                    r"$\delta A$ càng nhỏ thì phép đo càng chính xác",
                ),
                F(
                    r"Sai số của tổng hoặc hiệu $F = X \pm Y - Z$",
                    r"$\Delta F = \Delta X + \Delta Y + \Delta Z$",
                    r"Sai số tuyệt đối của một tổng hay hiệu bằng tổng các sai số tuyệt đối thành phần",
                ),
                F(
                    r"Sai số của tích hoặc thương $F = X^m \cdot Y^n \cdot Z^k$",
                    r"$\delta F = |m|\delta X + |n|\delta Y + |k|\delta Z$",
                    r"Sai số tỉ đối của tích hay thương bằng tổng các sai số tỉ đối nhân với số mũ tương ứng",
                ),
                F(
                    r"Ví dụ sai số đo tốc độ $v = \dfrac{s}{t}$",
                    r"$\delta v = \delta s + \delta t = \dfrac{\Delta s}{\overline{s}} + \dfrac{\Delta t}{\overline{t}} \implies \Delta v = \overline{v} \cdot \delta v$",
                    r"Áp dụng cho phép đo gián tiếp tốc độ trung bình",
                ),
            ),
        ],
        "example": r"""
Một học sinh dùng thước có độ chia nhỏ nhất $\text{ĐCNN} = 1\text{ mm}$ để đo chiều dài $s$ của một bàn học trong $4$ lần đo liên tiếp và thu được bảng số liệu: $s_1 = 1200\text{ mm}$, $s_2 = 1202\text{ mm}$, $s_3 = 1201\text{ mm}$, $s_4 = 1201\text{ mm}$. Lấy sai số dụng cụ bằng một độ chia nhỏ nhất ($\Delta s_{\text{dc}} = 1\text{ mm}$).
1. Tính giá trị trung bình $\overline{s}$ và sai số tuyệt đối trung bình $\overline{\Delta s}$.
2. Tính sai số tuyệt đối $\Delta s$, sai số tỉ đối $\delta s$ và viết kết quả đo $s$.
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. Giá trị trung bình của chiều dài bàn học qua $4$ lần đo là:
   $$\overline{s} = \dfrac{s_1 + s_2 + s_3 + s_4}{4} = \dfrac{1200 + 1202 + 1201 + 1201}{4} = 1201\text{ mm}$$
   Sai số tuyệt đối của từng lần đo:
   - $\Delta s_1 = |1201 - 1200| = 1\text{ mm}$
   - $\Delta s_2 = |1201 - 1202| = 1\text{ mm}$
   - $\Delta s_3 = |1201 - 1201| = 0\text{ mm}$
   - $\Delta s_4 = |1201 - 1201| = 0\text{ mm}$
   Sai số tuyệt đối trung bình của $4$ lần đo:
   $$\overline{\Delta s} = \dfrac{1 + 1 + 0 + 0}{4} = 0,5\text{ mm}$$
2. Sai số tuyệt đối của phép đo là:
   $$\Delta s = \overline{\Delta s} + \Delta s_{\text{dc}} = 0,5 + 1 = 1,5\text{ mm}$$
   (Nếu làm tròn sai số tuyệt đối đến hàng đơn vị theo độ chia nhỏ nhất của thước thì $\Delta s \approx 2\text{ mm}$; giữ $2$ chữ số có nghĩa thì $\Delta s = 1,5\text{ mm}$).
   Sai số tỉ đối của phép đo là:
   $$\delta s = \dfrac{\Delta s}{\overline{s}} \cdot 100\% = \dfrac{1,5}{1201} \cdot 100\% \approx 0,12\%$$
   Biểu diễn kết quả đo:
   $$s = (1201,0 \pm 1,5)\text{ mm} \quad \text{hoặc} \quad s = (1201 \pm 2)\text{ mm}$$
""",
        "real_life": r"""
Trong sản xuất cơ khí chính xác, chế tạo linh kiện bán dẫn và y sinh học, việc kiểm soát sai số phép đo đóng vai trò sống còn: một trục động cơ phản lực có đường kính $d = (50,000 \pm 0,005)\text{ mm}$ đòi hỏi sai số tỉ đối nhỏ hơn $0,01\%$; nếu vượt quá giới hạn dung sai này, ổ trục sẽ bị kẹt hoặc rung lắc mạnh khi quay ở tốc độ hàng chục nghìn vòng trên phút. Tương tự, các quy tắc an toàn bức xạ, an toàn điện và biển cảnh báo chuẩn quốc tế ISO $7010$ giúp bảo vệ kĩ thuật viên trong các phòng thí nghiệm bệnh viện, nhà máy điện và trung tâm nghiên cứu.
""",
        "game_title": "Phòng Thí Nghiệm Chuẩn Hóa: Thử Thách Đo Lường & Sai Số",
        "game_description": "Thực hành chọn dụng cụ đo phù hợp, nhận diện biển báo an toàn, đọc vạch chia và xử lí bảng số liệu thực nghiệm với sai số nhỏ nhất.",
        "game_type": "game_dodai",
        "quiz": [
            mcq(
                "biet",
                r"Đối tượng nghiên cứu chính của Vật lí học là gì?",
                [
                    r"Các dạng vận động của vật chất (chất, trường) và năng lượng.",
                    r"Cấu tạo chất và sự biến đổi các chất thông qua phản ứng hóa học.",
                    r"Sự sinh trưởng, phát triển và di truyền của các cơ thể sống.",
                    r"Cấu trúc địa chất và sự phân bố dân cư trên bề mặt Trái Đất.",
                ],
                0,
                r"Theo Bài 1 SGK Vật lí 10 KNTT, đối tượng nghiên cứu của Vật lí tập trung vào các dạng vận động của vật chất (chất, trường) và năng lượng.",
            ),
            mcq(
                "biet",
                r"Trong phòng thực hành Vật lí, biển báo có hình tam giác đều, viền đen (hoặc đỏ), nền màu vàng và hình vẽ màu đen thuộc nhóm biển báo nào?",
                [
                    r"Biển báo cấm.",
                    r"Biển báo cảnh báo nguy hiểm.",
                    r"Biển báo bắt buộc thực hiện.",
                    r"Biển báo chỉ dẫn thoát hiểm.",
                ],
                1,
                r"Theo Bài 2 SGK Vật lí 10 KNTT, biển báo hình tam giác đều nền vàng, viền đen (hoặc đỏ), hình vẽ đen là biển báo cảnh báo nguy hiểm (ví dụ: cảnh báo điện áp cao, tia laser, chất dễ cháy).",
            ),
            mcq(
                "biet",
                r"Gọi $\overline{A}$ là giá trị trung bình, $\Delta A$ là sai số tuyệt đối của phép đo đại lượng $A$. Sai số tỉ đối $\delta A$ của phép đo được xác định bởi công thức nào sau đây?",
                [
                    r"$\delta A = \dfrac{\Delta A}{\overline{A}} \cdot 100\%$",
                    r"$\delta A = \dfrac{\overline{A}}{\Delta A} \cdot 100\%$",
                    r"$\delta A = (\overline{A} + \Delta A) \cdot 100\%$",
                    r"$\delta A = (\overline{A} - \Delta A) \cdot 100\%$",
                ],
                0,
                r"Theo Bài 3 SGK Vật lí 10 KNTT, sai số tỉ đối là tỉ số phần trăm giữa sai số tuyệt đối và giá trị trung bình của đại lượng đo: $\delta A = \dfrac{\Delta A}{\overline{A}} \cdot 100\%$.",
            ),
            mcq(
                "biet",
                r"Số chữ số có nghĩa (CSCN) trong kết quả đo $L = 0,0250\text{ m}$ là bao nhiêu?",
                [
                    r"$2$ chữ số có nghĩa.",
                    r"$3$ chữ số có nghĩa.",
                    r"$4$ chữ số có nghĩa.",
                    r"$5$ chữ số có nghĩa.",
                ],
                1,
                r"Các chữ số $0$ ở bên trái chữ số khác $0$ đầu tiên không phải là chữ số có nghĩa. Do đó trong số $0,0250$, các chữ số có nghĩa là $2, 5, 0$ (gồm $3$ CSCN).",
            ),
            mcq(
                "hieu",
                r"Khi đo tốc độ trung bình của một chiếc xe đồ chơi bằng công thức $v = \dfrac{s}{t}$, người ta đo được quãng đường với sai số tỉ đối $\delta s = 1,5\%$ và thời gian với sai số tỉ đối $\delta t = 2,0\%$. Sai số tỉ đối $\delta v$ của phép đo tốc độ là:",
                [
                    r"$0,5\%$",
                    r"$1,75\%$",
                    r"$3,0\%$",
                    r"$3,5\%$",
                ],
                3,
                r"Áp dụng quy tắc tính sai số của một thương $v = \dfrac{s}{t}$, ta có: $\delta v = \delta s + \delta t = 1,5\% + 2,0\% = 3,5\%$.",
            ),
            mcq(
                "hieu",
                r"Hành động nào sau đây **vi phạm** quy tắc an toàn khi làm thí nghiệm với nguồn điện trong phòng thực hành Vật lí?",
                [
                    r"Ngắt công tắc nguồn điện trước khi lắp ráp hoặc tháo dỡ mạch điện.",
                    r"Kiểm tra độ kín của vỏ cách điện trên các dây nối trước khi sử dụng.",
                    r"Dùng tay ướt rút trực tiếp dây dẫn đang có điện ra khỏi ổ cắm nguồn $220\text{ V}$.",
                    r"Báo ngay cho giáo viên hướng dẫn khi phát hiện có mùi khét hoặc tia lửa điện.",
                ],
                2,
                r"Nước thường dẫn điện tốt; việc dùng tay ướt kéo dây dẫn trực tiếp khỏi ổ cắm $220\text{ V}$ gây nguy cơ điện giật nghiêm trọng và làm đứt, hở lõi dây điện.",
            ),
            tf4(
                "hieu",
                r"Một nhóm học sinh tiến hành thí nghiệm đo đường kính của một viên bi thép bằng thước kẹp và thảo luận về các phương pháp nghiên cứu cũng như sai số phép đo.",
                [
                    r"Phép đo đường kính viên bi bằng cách đọc trực tiếp giá trị trên thước kẹp là phép đo trực tiếp.",
                    r"Nếu thước kẹp chưa được hiệu chỉnh về đúng vạch số $0$ trước khi đo thì sẽ gây ra sai số ngẫu nhiên.",
                    r"Để giảm sai số ngẫu nhiên, học sinh cần thực hiện đo nhiều lần ở các vị trí khác nhau của viên bi rồi lấy giá trị trung bình.",
                    r"Khi tính thể tích viên bi theo công thức $V = \dfrac{1}{6}\pi d^3$, sai số tỉ đối của thể tích liên hệ với sai số tỉ đối của đường kính theo hệ thức $\delta V = 3\delta d$ (bỏ qua sai số của số $\pi$).",
                ],
                [True, False, True, True],
                r"""- **a) Đúng:** Đọc trực tiếp kết quả trên dụng cụ đo là phép đo trực tiếp.
- **b) Sai:** Dụng cụ đo lệch vạch số $0$ gây ra **sai số hệ thống** (lặp lại như nhau ở mọi lần đo), không phải sai số ngẫu nhiên.
- **c) Đúng:** Đo lặp lại nhiều lần và lấy giá trị trung bình là biện pháp cơ bản để giảm sai số ngẫu nhiên.
- **d) Đúng:** Với $V = \dfrac{1}{6}\pi d^3$, theo quy tắc sai số lũy thừa ta có $\delta V = 3\delta d$.""",
            ),
            tf4(
                "hieu",
                r"Trong giờ thực hành đo thời gian rơi của một vật bằng đồng hồ đo thời gian hiện số và cổng quang điện, một học sinh thu được $3$ lần đo là: $t_1 = 0,402\text{ s}$; $t_2 = 0,406\text{ s}$; $t_3 = 0,404\text{ s}$. Biết sai số dụng cụ là $\Delta t_{\text{dc}} = 0,001\text{ s}$.",
                [
                    r"Giá trị trung bình của thời gian rơi qua $3$ lần đo là $\overline{t} = 0,404\text{ s}$.",
                    r"Sai số tuyệt đối trung bình của $3$ lần đo là $\overline{\Delta t} = 0,002\text{ s}$.",
                    r"Sai số tuyệt đối của phép đo là $\Delta t = \overline{\Delta t} + \Delta t_{\text{dc}} = 0,003\text{ s}$.",
                    r"Sai số tỉ đối của phép đo này xấp xỉ bằng $0,58\%$.",
                ],
                [True, False, False, True],
                r"""- **a) Đúng:** $\overline{t} = \dfrac{0,402 + 0,406 + 0,404}{3} = 0,404\text{ s}$.
- **b) Sai:** Ta có $\Delta t_1 = 0,002\text{ s}$; $\Delta t_2 = 0,002\text{ s}$; $\Delta t_3 = 0\text{ s}$. Do đó $\overline{\Delta t} = \dfrac{0,002 + 0,002 + 0}{3} \approx 0,00133\text{ s} \neq 0,002\text{ s}$.
- **c) Sai:** Sai số tuyệt đối của phép đo là $\Delta t = \overline{\Delta t} + \Delta t_{\text{dc}} \approx 0,00133 + 0,001 = 0,00233\text{ s}$ (làm tròn $1$ chữ số có nghĩa là $0,002\text{ s}$).
- **d) Đúng:** Sai số tỉ đối $\delta t = \dfrac{0,00233}{0,404} \cdot 100\% \approx 0,58\%$.""",
            ),
            mcq(
                "vandung",
                r"Một học sinh đo quãng đường đi được của viên bi là $s = (2,00 \pm 0,02)\text{ m}$ trong khoảng thời gian $t = (0,50 \pm 0,01)\text{ s}$. Kết quả đo tốc độ trung bình $v = \dfrac{s}{t}$ của viên bi được viết đúng là:",
                [
                    r"$v = (4,00 \pm 0,12)\text{ m/s}$",
                    r"$v = (4,00 \pm 0,03)\text{ m/s}$",
                    r"$v = (4,00 \pm 0,08)\text{ m/s}$",
                    r"$v = (4,00 \pm 0,04)\text{ m/s}$",
                ],
                0,
                r"""Giá trị trung bình của tốc độ: $\overline{v} = \dfrac{\overline{s}}{\overline{t}} = \dfrac{2,00}{0,50} = 4,00\text{ m/s}$.
Sai số tỉ đối: $\delta v = \delta s + \delta t = \dfrac{0,02}{2,00} + \dfrac{0,01}{0,50} = 0,01 + 0,02 = 0,03 = 3\%$.
Sai số tuyệt đối của tốc độ: $\Delta v = \overline{v} \cdot \delta v = 4,00 \cdot 0,03 = 0,12\text{ m/s}$.
Vậy $v = (4,00 \pm 0,12)\text{ m/s}$.""",
            ),
            short(
                "vandung",
                r"Một học sinh đo gia tốc rơi tự do theo công thức $g = \dfrac{2s}{t^2}$, trong đó quãng đường rơi đo được có sai số tỉ đối $\delta s = 1,2\%$ và thời gian rơi đo được có sai số tỉ đối $\delta t = 1,4\%$. Hãy tính sai số tỉ đối $\delta g$ của phép đo gia tốc rơi tự do theo đơn vị phần trăm ($\text{\%}$), chỉ ghi phần số.",
                ["4", "4,0", "4.0"],
                r"Từ công thức $g = \dfrac{2s}{t^2}$, áp dụng quy tắc tính sai số của thương và lũy thừa: $\delta g = \delta s + 2\delta t = 1,2\% + 2 \cdot 1,4\% = 1,2\% + 2,8\% = 4\%$.",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG II – PHẦN 1. ĐỘNG HỌC: ĐỘ DỊCH CHUYỂN, VẬN TỐC & CĐTĐ (Bài 4 -> Bài 7)
    # =========================================================================
    {
        "topic": "chuyen-dong-thang",
        "title": "Chương II – Phần 1. Động học: Độ dịch chuyển, Vận tốc và Chuyển động thẳng đều",
        "icon": "🤖",
        "description": "Phân biệt quãng đường và độ dịch chuyển, tốc độ và vận tốc, tổng hợp vận tốc và khảo sát đồ thị độ dịch chuyển theo thời gian của chuyển động thẳng.",
        "requirements": [
            r"Từ hình ảnh hoặc ví dụ thực tiễn, định nghĩa được độ dịch chuyển $\overrightarrow{d}$ và phân biệt được độ dịch chuyển với quãng đường đi được $s$.",
            r"Lập luận để rút ra được công thức tính tốc độ trung bình $v_{\text{tb}} = \dfrac{s}{t}$, định nghĩa được tốc độ theo một phương và rút ra được công thức tính vận tốc $\overrightarrow{v} = \dfrac{\overrightarrow{d}}{t}$.",
            r"Thực hiện thí nghiệm hoặc thảo luận để thiết kế phương án đo được tốc độ của vật chuyển động bằng dụng cụ thực hành (cổng quang điện và đồng hồ đo thời gian hiện số).",
            r"Vận dụng được công thức tổng hợp hai độ dịch chuyển và công thức cộng vận tốc $\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$ trong trường hợp các vận tốc cùng phương hoặc vuông góc.",
            r"Thực hiện thí nghiệm (hoặc dựa trên số liệu cho trước), vẽ được đồ thị độ dịch chuyển – thời gian ($d - t$) trong chuyển động thẳng và tính được vận tốc từ độ dốc (hệ số góc) của đồ thị.",
        ],
        "definition": r"""
**Độ dịch chuyển** $\overrightarrow{d}$ là một đại lượng vectơ nối từ vị trí đầu đến vị trí cuối của vật chuyển động, cho biết cả độ dài và hướng của sự thay đổi vị trí. **Vận tốc** $\overrightarrow{v} = \dfrac{\Delta \overrightarrow{d}}{\Delta t}$ là đại lượng vectơ đặc trưng cho tốc độ và hướng thay đổi vị trí của vật. **Chuyển động thẳng đều** là chuyển động có quỹ đạo là đường thẳng và có vận tốc không đổi theo thời gian (cả về hướng và độ lớn), với phương trình tọa độ – độ dịch chuyển là $d = v \cdot t$ hay $x = x_0 + v(t - t_0)$.
""",
        "theory": r"""
### Bài 4. Độ dịch chuyển và quãng đường đi được

- **Hệ quy chiếu:** Gồm một vật làm mốc gắn với hệ tọa độ (để xác định vị trí của vật) và một mốc thời gian gắn với đồng hồ (để xác định thời điểm).
- **Quãng đường đi được ($s$):** Là đại lượng vô hướng, luôn không âm ($s \ge 0$), cho biết tổng chiều dài quỹ đạo mà vật đã đi qua trong suốt quá trình chuyển động.
- **Độ dịch chuyển ($\overrightarrow{d}$):** Là đại lượng vectơ có gốc tại vị trí ban đầu, ngọn tại vị trí cuối cùng của vật.
  + Trên một trục tọa độ $Ox$, nếu vật đi từ tọa độ $x_1$ đến tọa độ $x_2$ thì giá trị đại số của độ dịch chuyển là $d = \Delta x = x_2 - x_1$.
  + Giá trị $d$ có thể dương ($d > 0$, khi vật chuyển động cùng chiều dương trục tọa độ), âm ($d < 0$, khi vật chuyển động ngược chiều dương) hoặc bằng $0$ (khi vị trí cuối trùng vị trí đầu).
- **So sánh quãng đường $s$ và độ lớn độ dịch chuyển $|d|$:**
  + Luôn có $|d| \le s$.
  + Dấu bằng $|d| = s$ **chỉ xảy ra** khi vật chuyển động thẳng và không đổi chiều trong suốt thời gian khảo sát.
- **Tổng hợp độ dịch chuyển:** Nếu vật thực hiện liên tiếp hai độ dịch chuyển $\overrightarrow{d}_1$ và $\overrightarrow{d}_2$ thì độ dịch chuyển tổng hợp là $\overrightarrow{d} = \overrightarrow{d}_1 + \overrightarrow{d}_2$ (quy tắc cộng vectơ).

### Bài 5. Tốc độ và vận tốc

- **Tốc độ:** Là đại lượng vô hướng ($v \ge 0$) đặc trưng cho tính nhanh chậm của chuyển động:
  + **Tốc độ trung bình:** $v_{\text{tb}} = \dfrac{s}{t} = \dfrac{s_1 + s_2 + \dots}{t_1 + t_2 + \dots}$.
  + **Tốc độ tức thời:** Là tốc độ tại một thời điểm xác định (hoặc tính trong khoảng thời gian $\Delta t$ rất ngắn), chính là số chỉ của **tốc kế** trên xe máy, ô tô.
- **Vận tốc:** Là đại lượng vectơ đặc trưng cho sự nhanh chậm và chiều của sự thay đổi vị trí:
  + **Vận tốc trung bình:** $\overrightarrow{v}_{\text{tb}} = \dfrac{\overrightarrow{d}}{t} = \dfrac{\Delta \overrightarrow{d}}{\Delta t}$. Về giá trị đại số trên trục $Ox$: $v_{\text{tb}} = \dfrac{x_2 - x_1}{t_2 - t_1}$.
  + **Vận tốc tức thời:** Là vận tốc tại một thời điểm xác định, có phương tiếp tuyến với quỹ đạo, chiều là chiều chuyển động và độ lớn bằng tốc độ tức thời tại thời điểm đó.
- **Tổng hợp vận tốc (Công thức cộng vận tốc):**
  + Gọi $(1)$ là vật chuyển động (hệ quy chiếu chuyển động: thuyền, hành khách), $(2)$ là hệ quy chiếu chuyển động (dòng nước, đoàn tàu), $(3)$ là hệ quy chiếu đứng yên (bờ sông, mặt đất).
  + Công thức vectơ: $\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$.
  + Trong đó: $\overrightarrow{v}_{13}$ là vận tốc tuyệt đối (của vật đối với hệ đứng yên); $\overrightarrow{v}_{12}$ là vận tốc tương đối (của vật đối với hệ chuyển động); $\overrightarrow{v}_{23}$ là vận tốc kéo theo (của hệ chuyển động đối với hệ đứng yên).

### Bài 6. Thực hành: Đo tốc độ của vật chuyển động

- **Dụng cụ thí nghiệm:** Máng nghiêng, viên bi thép (hoặc xe lăn có tấm chắn sáng), hai cổng quang điện $E, F$ nối với đồng hồ đo thời gian hiện số, thước thẳng hoặc thước kẹp.
- **Hai phương pháp đo tốc độ trong phòng thực hành:**
  1. **Đo tốc độ trung bình trên một đoạn đường:** Đặt hai cổng quang điện tại hai vị trí $A$ và $B$ cách nhau một khoảng $s = AB$. Chuyển đồng hồ sang chế độ $A \leftrightarrow B$ để đo thời gian $t$ viên bi đi từ cổng $A$ đến cổng $B$. Khi đó tốc độ trung bình là $v_{\text{tb}} = \dfrac{s}{t}$.
  2. **Đo tốc độ tức thời tại một vị trí:** Đặt một cổng quang điện tại vị trí cần đo. Đo đường kính $d$ của viên bi (hoặc chiều rộng tấm chắn sáng gắn trên xe). Chuyển đồng hồ sang chế độ $A$ (hoặc $B$) để đo thời gian $\Delta t$ viên bi chắn chùm tia hồng ngoại tại cổng quang điện. Vì $\Delta t$ rất nhỏ nên tốc độ tức thời của viên bi khi qua cổng là $v = \dfrac{d}{\Delta t}$.

### Bài 7. Đồ thị độ dịch chuyển – thời gian

- **Chuyển động thẳng đều:** Vật chuyển động trên đường thẳng với tốc độ không đổi. Khi không đổi chiều, độ dịch chuyển tỉ lệ thuận với thời gian: $d = v \cdot t$. Nếu tại $t = 0$ vật ở tọa độ $x_0$ thì phương trình tọa độ là $x = x_0 + v \cdot t$.
- **Đặc điểm đồ thị độ dịch chuyển – thời gian ($d - t$ hoặc $x - t$):**
  + Vật **đứng yên**: Đồ thị là đường thẳng song song với trục thời gian $Ot$ (hệ số góc $v = 0$).
  + Vật **chuyển động thẳng đều theo chiều dương**: Đồ thị là đường thẳng xiên lên phía trên (hệ số góc $v > 0$).
  + Vật **chuyển động thẳng đều theo chiều âm**: Đồ thị là đường thẳng xiên xuống phía dưới (hệ số góc $v < 0$).
  + Vật **chuyển động biến đổi**: Đồ thị là một đường cong.
- **Ý nghĩa của độ dốc (hệ số góc) trên đồ thị $d - t$:**
  + Vận tốc của vật trong giai đoạn chuyển động thẳng đều chính bằng **độ dốc (hệ số góc)** của đường biểu diễn: $v = \dfrac{d_2 - d_1}{t_2 - t_1} = \dfrac{\Delta d}{\Delta t}$.
  + Đường thẳng nào có độ dốc lớn hơn (dốc đứng hơn) thì vật đó chuyển động với tốc độ lớn hơn.
""",
        "formulas": [
            G(
                "Độ dịch chuyển, Tốc độ và Vận tốc",
                F(
                    "Độ dịch chuyển trên trục tọa độ",
                    r"$d = \Delta x = x_2 - x_1$",
                    r"$x_1, x_2$ là tọa độ đầu và tọa độ cuối ($\text{m}$)",
                ),
                F(
                    "Tốc độ trung bình",
                    r"$v_{\text{tb}} = \dfrac{s}{t}$",
                    r"$s$ là tổng quãng đường đi được ($\text{m}$), $t$ là tổng thời gian ($\text{s}$)",
                ),
                F(
                    "Vận tốc trung bình",
                    r"$\overrightarrow{v}_{\text{tb}} = \dfrac{\overrightarrow{d}}{t} = \dfrac{\Delta \overrightarrow{d}}{\Delta t}$",
                    r"Đơn vị trong hệ SI là $\text{m/s}$; đổi đơn vị: $1\text{ m/s} = 3,6\text{ km/h}$",
                ),
                F(
                    "Đo tốc độ tức thời qua cổng quang điện",
                    r"$v = \dfrac{d_{\text{bi}}}{\Delta t}$",
                    r"$d_{\text{bi}}$ là đường kính viên bi (hoặc bề rộng tấm chắn sáng), $\Delta t$ là thời gian chắn cổng",
                ),
            ),
            G(
                "Công thức cộng vận tốc",
                F(
                    "Biểu thức vectơ tổng quát",
                    r"$\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$",
                    r"$(1)$ vật, $(2)$ hệ quy chiếu chuyển động, $(3)$ hệ quy chiếu đứng yên",
                ),
                F(
                    r"Hai vận tốc cùng chiều ($\overrightarrow{v}_{12} \uparrow\uparrow \overrightarrow{v}_{23}$)",
                    r"$v_{13} = v_{12} + v_{23}$",
                    r"Ví dụ: Thuyền chạy xuôi dòng nước ($v_{\text{xuôi}} = v_{\text{thuyền/nước}} + v_{\text{nước/bờ}}$)",
                ),
                F(
                    r"Hai vận tốc ngược chiều ($\overrightarrow{v}_{12} \uparrow\downarrow \overrightarrow{v}_{23}$)",
                    r"$v_{13} = |v_{12} - v_{23}|$",
                    r"Ví dụ: Thuyền chạy ngược dòng nước ($v_{\text{ngược}} = v_{\text{thuyền/nước}} - v_{\text{nước/bờ}}$)",
                ),
                F(
                    r"Hai vận tốc vuông góc ($\overrightarrow{v}_{12} \perp \overrightarrow{v}_{23}$)",
                    r"$v_{13} = \sqrt{v_{12}^2 + v_{23}^2}$",
                    r"Ví dụ: Thuyền hướng mũi vuông góc với bờ sông có nước chảy",
                ),
            ),
            G(
                r"Chuyển động thẳng đều và Đồ thị $d - t$",
                F(
                    "Phương trình độ dịch chuyển và tọa độ",
                    r"$d = v \cdot t \quad ; \quad x = x_0 + v(t - t_0)$",
                    r"$v > 0$ khi chuyển động cùng chiều dương, $v < 0$ khi ngược chiều dương",
                ),
                F(
                    r"Vận tốc từ độ dốc đồ thị $d - t$",
                    r"$v = \dfrac{d_2 - d_1}{t_2 - t_1} = \dfrac{\Delta d}{\Delta t}$",
                    r"Hệ số góc của đường thẳng trên đồ thị độ dịch chuyển – thời gian",
                ),
            ),
        ],
        "example": r"""
Một người bơi dọc theo chiều dài $50\text{ m}$ của một bể bơi từ đầu bể $A$ đến cuối bể $B$ hết $t_1 = 20\text{ s}$, rồi lập tức bơi quay lại vị trí xuất phát $A$ hết $t_2 = 30\text{ s}$. Chọn trục tọa độ $Ox$ trùng với đường bơi, gốc tại $A$, chiều dương từ $A$ đến $B$.
1. Tính quãng đường đi được, độ dịch chuyển, tốc độ trung bình và vận tốc trung bình của người đó trong lượt bơi đi từ $A$ đến $B$.
2. Tính quãng đường đi được, độ dịch chuyển, tốc độ trung bình và vận tốc trung bình của người đó trong cả quá trình bơi đi và về ($A \to B \to A$).
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. **Xét lượt bơi đi từ $A$ đến $B$ ($t_1 = 20\text{ s}$):**
   - Quãng đường đi được: $s_1 = 50\text{ m}$.
   - Độ dịch chuyển: $d_1 = x_B - x_A = 50 - 0 = 50\text{ m}$.
   - Tốc độ trung bình: $v_{\text{tb1}} = \dfrac{s_1}{t_1} = \dfrac{50}{20} = 2,5\text{ m/s}$.
   - Vận tốc trung bình: $v_1 = \dfrac{d_1}{t_1} = \dfrac{50}{20} = 2,5\text{ m/s}$.
2. **Xét cả quá trình bơi đi và về $A \to B \to A$ ($t = t_1 + t_2 = 20 + 30 = 50\text{ s}$):**
   - Tổng quãng đường đi được: $s = s_1 + s_2 = 50 + 50 = 100\text{ m}$.
   - Độ dịch chuyển tổng hợp (do vị trí cuối trùng vị trí đầu tại $A$):
     $$d = d_1 + d_2 = 50 + (-50) = 0\text{ m}$$
   - Tốc độ trung bình trên cả quá trình:
     $$v_{\text{tb}} = \dfrac{s}{t_1 + t_2} = \dfrac{100}{20 + 30} = 2,0\text{ m/s}$$
   - Vận tốc trung bình trên cả quá trình:
     $$v = \dfrac{d}{t_1 + t_2} = \dfrac{0}{50} = 0\text{ m/s}$$
""",
        "real_life": r"""
Trên các ứng dụng bản đồ vệ tinh GPS như Google Maps, khoảng cách chim bay nối từ vị trí xuất phát đến điểm đích kèm theo hướng la bàn chính là **độ dịch chuyển** $\overrightarrow{d}$, còn lộ trình thực tế men theo các con phố mà xe phải lăn bánh là **quãng đường** $s$. Trong hàng hải và hàng không, phi công luôn phải áp dụng **công thức cộng vận tốc** $\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$ để bù góc lệch do gió tạt ngang, đảm bảo máy bay bay đúng hành trình về sân bay đích.
""",
        "game_title": "Lập Trình Robot Tự Hành: Điều Hướng Độ Dịch Chuyển & Đồ Thị",
        "game_description": "Điều khiển robot di chuyển trên lưới tọa độ, đọc đồ thị d - t và giải bài toán qua sông có dòng nước chảy.",
        "game_type": "game_robot",
        "quiz": [
            mcq(
                "biet",
                r"Trong trường hợp nào sau đây, độ lớn của độ dịch chuyển $|d|$ bằng quãng đường đi được $s$ của vật?",
                [
                    r"Vật chuyển động tròn đều được một vòng.",
                    r"Vật chuyển động thẳng và không đổi chiều.",
                    r"Vật chuyển động thẳng từ $A$ đến $B$ rồi quay về $A$.",
                    r"Vật dao động qua lại quanh một vị trí cân bằng.",
                ],
                1,
                r"Theo Bài 4 SGK Vật lí 10 KNTT, quãng đường đi được chỉ có độ lớn bằng độ dịch chuyển ($s = |d|$) khi vật chuyển động thẳng và không đổi chiều.",
            ),
            mcq(
                "biet",
                r"Số chỉ của tốc kế gắn trên xe máy hoặc ô tô đang chạy trên đường cho biết đại lượng nào sau đây?",
                [
                    r"Tốc độ trung bình của xe trên cả hành trình.",
                    r"Tốc độ tức thời của xe tại thời điểm quan sát.",
                    r"Độ dịch chuyển của xe từ lúc khởi hành.",
                    r"Vận tốc trung bình của xe kèm hướng chuyển động.",
                ],
                1,
                r"Theo Bài 5 SGK Vật lí 10 KNTT, tốc kế trên xe hiển thị tốc độ tức thời của xe tại thời điểm đang xét.",
            ),
            mcq(
                "biet",
                r"Trên đồ thị độ dịch chuyển – thời gian ($d - t$) của một chất điểm chuyển động thẳng, nếu đường biểu diễn là một đường thẳng song song với trục thời gian $Ot$ thì chất điểm đang ở trạng thái nào?",
                [
                    r"Chuyển động thẳng đều theo chiều dương.",
                    r"Chuyển động thẳng đều theo chiều âm.",
                    r"Đứng yên tại một vị trí xác định.",
                    r"Chuyển động thẳng nhanh dần đều.",
                ],
                2,
                r"Theo Bài 7 SGK Vật lí 10 KNTT, đường biểu diễn trên đồ thị $d - t$ song song với trục $Ot$ cho thấy độ dịch chuyển $d$ không đổi theo thời gian, nghĩa là vật đang đứng yên ($v = 0$).",
            ),
            mcq(
                "biet",
                r"Gọi $\overrightarrow{v}_{12}$ là vận tốc của thuyền so với nước, $\overrightarrow{v}_{23}$ là vận tốc của nước so với bờ và $\overrightarrow{v}_{13}$ là vận tốc của thuyền so với bờ. Công thức cộng vận tốc đúng là:",
                [
                    r"$\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$",
                    r"$\overrightarrow{v}_{13} = \overrightarrow{v}_{12} - \overrightarrow{v}_{23}$",
                    r"$v_{13} = v_{12} + v_{23}$ với mọi hướng chuyển động.",
                    r"$\overrightarrow{v}_{12} = \overrightarrow{v}_{13} + \overrightarrow{v}_{23}$",
                ],
                0,
                r"Theo Bài 5 SGK Vật lí 10 KNTT, công thức tổng hợp vận tốc dưới dạng vectơ luôn là $\overrightarrow{v}_{13} = \overrightarrow{v}_{12} + \overrightarrow{v}_{23}$.",
            ),
            mcq(
                "hieu",
                r"Một người đi bộ từ nhà hướng về phía Đông $300\text{ m}$, sau đó rẽ vuông góc sang phía Bắc đi tiếp $400\text{ m}$ thì dừng lại. Quãng đường đi được $s$ và độ lớn độ dịch chuyển $d$ của người đó lần lượt là:",
                [
                    r"$s = 700\text{ m}$ và $d = 500\text{ m}$",
                    r"$s = 500\text{ m}$ và $d = 700\text{ m}$",
                    r"$s = 700\text{ m}$ và $d = 700\text{ m}$",
                    r"$s = 700\text{ m}$ và $d = 100\text{ m}$",
                ],
                0,
                r"Quãng đường là tổng chiều dài đã đi: $s = 300 + 400 = 700\text{ m}$. Hai độ dịch chuyển thành phần vuông góc nhau (Đông và Bắc) nên độ lớn độ dịch chuyển tổng hợp là $d = \sqrt{300^2 + 400^2} = 500\text{ m}$.",
            ),
            mcq(
                "hieu",
                r"Trong bài thực hành đo tốc độ tức thời của viên bi qua cổng quang điện, viên bi có đường kính $d = 2,0\text{ cm}$ đi qua cổng quang điện làm chắn chùm tia sáng trong khoảng thời gian $\Delta t = 0,025\text{ s}$. Tốc độ tức thời của viên bi tại cổng quang điện là:",
                [
                    r"$0,50\text{ m/s}$",
                    r"$0,80\text{ m/s}$",
                    r"$1,25\text{ m/s}$",
                    r"$2,00\text{ m/s}$",
                ],
                1,
                r"Đổi $d = 2,0\text{ cm} = 0,02\text{ m}$. Tốc độ tức thời của viên bi khi qua cổng quang điện là $v = \dfrac{d}{\Delta t} = \dfrac{0,02}{0,025} = 0,80\text{ m/s}$.",
            ),
            tf4(
                "hieu",
                r"Một ô tô chuyển động trên một đường thẳng có đồ thị độ dịch chuyển – thời gian ($d - t$) gồm $3$ giai đoạn: Từ $t_0 = 0$ đến $t_1 = 2\text{ h}$, $d$ tăng đều từ $0\text{ km}$ lên $100\text{ km}$; từ $t_1 = 2\text{ h}$ đến $t_2 = 3\text{ h}$, $d$ giữ nguyên ở giá trị $100\text{ km}$; từ $t_2 = 3\text{ h}$ đến $t_3 = 5\text{ h}$, $d$ giảm đều từ $100\text{ km}$ về $20\text{ km}$.",
                [
                    r"Trong giai đoạn từ $0$ đến $2\text{ h}$, ô tô chuyển động thẳng đều theo chiều dương với vận tốc $50\text{ km/h}$.",
                    r"Từ $t_1 = 2\text{ h}$ đến $t_2 = 3\text{ h}$, ô tô dừng lại nghỉ ngơi nên vận tốc bằng $0\text{ km/h}$.",
                    r"Trong giai đoạn từ $3\text{ h}$ đến $5\text{ h}$, vận tốc của ô tô là $-40\text{ km/h}$ (xe chạy ngược chiều dương).",
                    r"Sau $5\text{ h}$ chuyển động, tổng quãng đường ô tô đi được bằng độ lớn độ dịch chuyển và bằng $20\text{ km}$.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** Vận tốc trong $2\text{ h}$ đầu là $v_1 = \dfrac{100 - 0}{2 - 0} = 50\text{ km/h}$.
- **b) Đúng:** Độ dịch chuyển không đổi ($d = 100\text{ km}$), xe đứng yên ($v_2 = 0$).
- **c) Đúng:** Vận tốc từ $3\text{ h}$ đến $5\text{ h}$ là $v_3 = \dfrac{20 - 100}{5 - 3} = \dfrac{-80}{2} = -40\text{ km/h}$.
- **d) Sai:** Sau $5\text{ h}$, độ dịch chuyển là $d = 20\text{ km}$, nhưng tổng quãng đường xe đã đi là $s = 100 + 0 + |20 - 100| = 180\text{ km}$.""",
            ),
            tf4(
                "hieu",
                r"Một chiếc ca nô chuyển động trên một dòng sông thẳng có nước chảy đều với tốc độ $v_{\text{nước}} = 2\text{ m/s}$ so với bờ. Biết tốc độ của ca nô so với nước luôn không đổi và bằng $v_{\text{ca nô/nước}} = 6\text{ m/s}$.",
                [
                    r"Khi ca nô chạy xuôi dòng, tốc độ của ca nô so với bờ là $8\text{ m/s}$.",
                    r"Khi ca nô chạy ngược dòng, tốc độ của ca nô so với bờ là $4\text{ m/s}$.",
                    r"Thời gian ca nô đi xuôi dòng một đoạn sông dài $480\text{ m}$ là $80\text{ s}$.",
                    r"Nếu người lái hướng mũi ca nô vuông góc với bờ sông thì tốc độ của ca nô so với bờ là $\sqrt{6^2 + 2^2} = 2\sqrt{10}\text{ m/s}$.",
                ],
                [True, True, False, True],
                r"""- **a) Đúng:** $v_{\text{xuôi}} = 6 + 2 = 8\text{ m/s}$.
- **b) Đúng:** $v_{\text{ngược}} = 6 - 2 = 4\text{ m/s}$.
- **c) Sai:** Thời gian đi xuôi dòng đoạn sông $480\text{ m}$ là $t = \dfrac{480}{8} = 60\text{ s} \neq 80\text{ s}$.
- **d) Đúng:** Khi $\overrightarrow{v}_{12} \perp \overrightarrow{v}_{23}$, độ lớn vận tốc tổng hợp là $v_{13} = \sqrt{6^2 + 2^2} = \sqrt{40} = 2\sqrt{10}\text{ m/s}$.""",
            ),
            mcq(
                "vandung",
                r"Một ô tô đi trên quãng đường thẳng từ $A$ đến $B$. Nửa quãng đường đầu ô tô đi với tốc độ không đổi $v_1 = 40\text{ km/h}$, nửa quãng đường còn lại ô tô đi với tốc độ không đổi $v_2 = 60\text{ km/h}$. Tốc độ trung bình của ô tô trên cả quãng đường $AB$ là:",
                [
                    r"$50\text{ km/h}$",
                    r"$48\text{ km/h}$",
                    r"$45\text{ km/h}$",
                    r"$52\text{ km/h}$",
                ],
                1,
                r"""Gọi $s$ là tổng quãng đường $AB$. Thời gian đi nửa quãng đường đầu là $t_1 = \dfrac{s}{2v_1}$, thời gian đi nửa quãng đường sau là $t_2 = \dfrac{s}{2v_2}$.
Tốc độ trung bình trên cả quãng đường là:
$$v_{\text{tb}} = \dfrac{s}{t_1 + t_2} = \dfrac{s}{\dfrac{s}{2v_1} + \dfrac{s}{2v_2}} = \dfrac{2v_1 v_2}{v_1 + v_2} = \dfrac{2 \cdot 40 \cdot 60}{40 + 60} = 48\text{ km/h}$$""",
            ),
            short(
                "vandung",
                r"Hai bến sông $A$ và $B$ cùng nằm trên một bờ sông thẳng, cách nhau $36\text{ km}$. Một ca nô đi xuôi dòng từ $A$ đến $B$ mất $1,5\text{ h}$ và đi ngược dòng từ $B$ về $A$ mất $3\text{ h}$. Biết tốc độ của ca nô so với nước và tốc độ của dòng nước so với bờ là không đổi. Tính tốc độ của dòng nước so với bờ theo đơn vị $\text{km/h}$ (chỉ ghi phần số).",
                ["6", "6,0", "6.0"],
                r"""Tốc độ ca nô khi xuôi dòng: $v_{\text{xuôi}} = v_{12} + v_{23} = \dfrac{36}{1,5} = 24\text{ km/h}$.
Tốc độ ca nô khi ngược dòng: $v_{\text{ngược}} = v_{12} - v_{23} = \dfrac{36}{3} = 12\text{ km/h}$.
Trừ hai vế rồi chia cho $2$, ta được tốc độ dòng nước so với bờ:
$$v_{23} = \dfrac{v_{\text{xuôi}} - v_{\text{ngược}}}{2} = \dfrac{24 - 12}{2} = 6\text{ km/h}$$""",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG II – PHẦN 2. ĐỘNG HỌC: GIA TỐC, CĐBĐĐ, RƠI TỰ DO & NÉM (Bài 8 -> Bài 12)
    # =========================================================================
    {
        "topic": "gia-toc",
        "title": "Chương II – Phần 2. Động học: Gia tốc, Chuyển động biến đổi, Sự rơi tự do và Chuyển động ném",
        "icon": "🚀",
        "description": "Nghiên cứu khái niệm gia tốc, các công thức của chuyển động thẳng biến đổi đều, đồ thị vận tốc theo thời gian, sự rơi tự do và chuyển động ném ngang, ném xiên.",
        "requirements": [
            r"Thực hiện thí nghiệm và lập luận dựa vào sự biến đổi vận tốc trong chuyển động thẳng, rút ra được công thức tính gia tốc $\overrightarrow{a} = \dfrac{\Delta \overrightarrow{v}}{\Delta t}$; nêu được ý nghĩa, đơn vị của gia tốc ($\text{m/s}^2$).",
            r"Thực hiện thí nghiệm (hoặc dựa trên số liệu cho trước), vẽ được đồ thị vận tốc – thời gian ($v - t$) trong chuyển động thẳng; vận dụng đồ thị $v - t$ để tính được gia tốc (từ độ dốc) và độ dịch chuyển (từ diện tích giới hạn bởi đồ thị).",
            r"Rút ra được các công thức của chuyển động thẳng biến đổi đều (không dùng tích phân) và vận dụng được các công thức $v = v_0 + at$, $d = v_0 t + \dfrac{1}{2}at^2$, $v^2 - v_0^2 = 2ad$.",
            r"Thảo luận để thiết kế phương án hoặc lựa chọn phương án và thực hiện phương án, đo được gia tốc rơi tự do $g$ bằng dụng cụ thực hành.",
            r"Mô tả và giải thích được chuyển động ném ngang, ném xiên khi vật có vận tốc không đổi theo phương nằm ngang và có chuyển động thẳng biến đổi đều với gia tốc $\overrightarrow{g}$ theo phương thẳng đứng.",
            r"Thực hiện được dự án hay đề tài nghiên cứu tìm điều kiện ném vật trong không khí ở độ cao hoặc góc ném sao cho tầm bay xa đạt giá trị cực đại.",
        ],
        "definition": r"""
**Gia tốc** $\overrightarrow{a} = \dfrac{\Delta \overrightarrow{v}}{\Delta t}$ là đại lượng vectơ đặc trưng cho độ biến thiên nhanh hay chậm của vận tốc theo thời gian, có đơn vị trong hệ SI là $\text{m/s}^2$. **Chuyển động thẳng biến đổi đều** là chuyển động có quỹ đạo là đường thẳng và có gia tốc $\overrightarrow{a}$ không đổi theo thời gian (nhanh dần đều khi $\overrightarrow{a}$ cùng chiều $\overrightarrow{v}$, tức $a \cdot v > 0$; chậm dần đều khi $\overrightarrow{a}$ ngược chiều $\overrightarrow{v}$, tức $a \cdot v < 0$).
""",
        "theory": r"""
### Bài 8. Chuyển động biến đổi. Gia tốc

- **Chuyển động biến đổi:** Là chuyển động có vận tốc thay đổi theo thời gian (thay đổi về độ lớn, về hướng hoặc cả hai).
- **Gia tốc trung bình:** $\overrightarrow{a}_{\text{tb}} = \dfrac{\Delta \overrightarrow{v}}{\Delta t} = \dfrac{\overrightarrow{v}_2 - \overrightarrow{v}_1}{t_2 - t_1}$.
- **Trong chuyển động thẳng:** Các vectơ vận tốc cùng nằm trên một đường thẳng nên ta xét giá trị đại số: $a = \dfrac{v - v_0}{t - t_0} = \dfrac{\Delta v}{\Delta t}$.
  + Đơn vị của gia tốc trong hệ SI là mét trên giây bình phương ($\text{m/s}^2$).
  + Dấu của tích $a \cdot v$:
    - Khi $\overrightarrow{a}$ cùng chiều $\overrightarrow{v}$ ($a \cdot v > 0$): Độ lớn vận tốc tăng theo thời gian (chuyển động **nhanh dần**).
    - Khi $\overrightarrow{a}$ ngược chiều $\overrightarrow{v}$ ($a \cdot v < 0$): Độ lớn vận tốc giảm theo thời gian (chuyển động **chậm dần**).

### Bài 9. Chuyển động thẳng biến đổi đều

- **Định nghĩa:** Chuyển động thẳng có gia tốc tức thời không đổi theo thời gian ($a = \text{hằng số} \neq 0$).
  + **Chuyển động thẳng nhanh dần đều:** Độ lớn vận tốc tăng đều theo thời gian ($a \cdot v > 0$).
  + **Chuyển động thẳng chậm dần đều:** Độ lớn vận tốc giảm đều theo thời gian ($a \cdot v < 0$).
- **Đồ thị vận tốc – thời gian ($v - t$):**
  + Trong chuyển động thẳng biến đổi đều, đồ thị $v - t$ là một đường thẳng xiên góc xuất phát từ điểm $(0, v_0)$.
  + **Độ dốc (hệ số góc)** của đường thẳng trên đồ thị $v - t$ cho biết giá trị đại số của gia tốc: $a = \dfrac{v_2 - v_1}{t_2 - t_1}$.
  + **Diện tích hình phẳng** (hình thang hoặc hình tam giác) giới hạn bởi đồ thị $v - t$, trục hoành $Ot$ và hai đường thẳng đứng $t = 0$, $t$ cho biết độ dịch chuyển $d$:
    $$d = \dfrac{v_0 + v}{2} \cdot t = v_0 t + \dfrac{1}{2}at^2$$
- **Hệ các công thức của chuyển động thẳng biến đổi đều:**
  1. Công thức vận tốc: $v = v_0 + a t$.
  2. Công thức độ dịch chuyển: $d = \dfrac{v_0 + v}{2} \cdot t = v_0 t + \dfrac{1}{2}a t^2$.
  3. Phương trình tọa độ: $x = x_0 + d = x_0 + v_0 t + \dfrac{1}{2}a t^2$ (đồ thị $x - t$ hoặc $d - t$ là một nhánh parabol).
  4. Công thức độc lập với thời gian: $v^2 - v_0^2 = 2 a d$.

### Bài 10. Sự rơi tự do

- **Sự rơi trong không khí:** Trong không khí, các vật rơi nhanh chậm khác nhau chủ yếu là do **lực cản của không khí** tác dụng lên chúng khác nhau, không phải do vật nặng hay nhẹ. Trong chân không (ống Newton đã hút hết không khí), mọi vật nặng nhẹ khác nhau (viên bi chì và chiếc lông chim) đều rơi nhanh như nhau.
- **Định nghĩa sự rơi tự do:** Là sự rơi chỉ dưới tác dụng của trọng lực (bỏ qua lực cản của không khí hoặc khi lực cản rất nhỏ so với trọng lực).
- **Đặc điểm của chuyển động rơi tự do:**
  + Phương thẳng đứng, chiều từ trên xuống dưới.
  + Là chuyển động thẳng nhanh dần đều với vận tốc đầu $v_0 = 0$ và gia tốc không đổi gọi là **gia tốc rơi tự do** (gia tốc trọng trường) kí hiệu là $g$.
  + Tại một nơi nhất định trên Trái Đất và ở gần mặt đất, mọi vật đều rơi tự do với cùng một gia tốc $g$. Giá trị của $g$ phụ thuộc vào vĩ độ địa lí và độ cao (thường lấy $g \approx 9,8\text{ m/s}^2$ hoặc $g \approx 10\text{ m/s}^2$).

### Bài 11. Thực hành: Đo gia tốc rơi tự do

- **Nguyên lí thí nghiệm:** Thả một trụ thép rơi tự do từ nam châm điện (vị trí $A$, $v_0 = 0$) đi qua cổng quang điện (vị trí $B$) cách $A$ một quãng đường $s$.
- **Xử lí số liệu:**
  + Từ công thức $s = \dfrac{1}{2}gt^2 \implies g = \dfrac{2s}{t^2}$.
  + Nếu vẽ đồ thị phụ thuộc của quãng đường $s$ theo bình phương thời gian $t^2$, ta thu được một đường thẳng đi qua gốc tọa độ có hệ số góc $k = \dfrac{s}{t^2} = \dfrac{1}{2}g \implies g = 2k$.

### Bài 12. Chuyển động ném

- **Phương pháp phân tích chuyển động:** Chia chuyển động ném của vật trong mặt phẳng thẳng đứng $Oxy$ thành hai chuyển động thành phần độc lập theo hai trục vuông góc:
  + Theo phương nằm ngang $Ox$: Không có lực tác dụng (bỏ qua sức cản không khí) nên $a_x = 0$, vật chuyển động thẳng đều.
  + Theo phương thẳng đứng $Oy$: Chỉ chịu tác dụng của trọng lực nên vật chuyển động thẳng biến đổi đều với gia tốc $g$.
- **1. Chuyển động ném ngang (từ độ cao $H$ với vận tốc đầu $\overrightarrow{v}_0$ nằm ngang):**
  + Chọn gốc $O$ tại vị trí ném, $Ox$ nằm ngang cùng chiều $\overrightarrow{v}_0$, $Oy$ thẳng đứng hướng xuống:
    - Theo $Ox$: $v_x = v_0$, $d_x = x = v_0 t$.
    - Theo $Oy$: $v_y = gt$, $d_y = y = \dfrac{1}{2}gt^2$.
  + Phương trình quỹ đạo (nhánh parabol): $y = \dfrac{g}{2v_0^2}x^2$.
  + Thời gian rơi từ lúc ném đến khi chạm đất ($y = H$): $t_{\text{rơi}} = \sqrt{\dfrac{2H}{g}}$ (chỉ phụ thuộc độ cao $H$, không phụ thuộc $v_0$).
  + Tầm bay xa theo phương ngang: $L = x_{\max} = v_0 \cdot t_{\text{rơi}} = v_0\sqrt{\dfrac{2H}{g}}$.
- **2. Chuyển động ném xiên (từ mặt đất với vận tốc đầu $v_0$ hợp với phương ngang góc $\alpha$):**
  + Phân tích vận tốc ban đầu: $v_{0x} = v_0\cos\alpha$; $v_{0y} = v_0\sin\alpha$.
  + Tầm bay cao cực đại (khi $v_y = 0$ tại đỉnh parabol): $H = \dfrac{v_{0y}^2}{2g} = \dfrac{v_0^2\sin^2\alpha}{2g}$.
  + Thời gian từ lúc ném đến lúc đạt độ cao cực đại: $t_H = \dfrac{v_0\sin\alpha}{g}$; tổng thời gian bay (chạm đất cùng độ cao ném): $t_{\text{bay}} = 2t_H = \dfrac{2v_0\sin\alpha}{g}$.
  + Tầm bay xa trên mặt đất phẳng: $L = v_{0x} \cdot t_{\text{bay}} = \dfrac{v_0^2\sin 2\alpha}{g}$. Với cùng $v_0$, tầm bay xa đạt cực đại $L_{\max} = \dfrac{v_0^2}{g}$ khi góc ném $\alpha = 45^\circ$ (bỏ qua sức cản không khí).
""",
        "formulas": [
            G(
                "Gia tốc và Chuyển động thẳng biến đổi đều",
                F(
                    "Gia tốc trong chuyển động thẳng",
                    r"$a = \dfrac{\Delta v}{\Delta t} = \dfrac{v - v_0}{t - t_0}$",
                    r"Đơn vị: $\text{m/s}^2$; nhanh dần khi $a \cdot v > 0$, chậm dần khi $a \cdot v < 0$",
                ),
                F(
                    "Vận tốc tức thời theo thời gian",
                    r"$v = v_0 + a t$",
                    r"$v_0$ là vận tốc ban đầu tại $t_0 = 0$",
                ),
                F(
                    "Độ dịch chuyển trong CĐTBĐĐ",
                    r"$d = \dfrac{v_0 + v}{2}t = v_0 t + \dfrac{1}{2}at^2$",
                    r"Khi vật chuyển động không đổi chiều thì quãng đường $s = |d|$",
                ),
                F(
                    "Hệ thức độc lập với thời gian",
                    r"$v^2 - v_0^2 = 2 a d$",
                    r"Liên hệ trực tiếp giữa $v, v_0, a$ và độ dịch chuyển $d$",
                ),
            ),
            G(
                r"Sự rơi tự do ($v_0 = 0, a = g$)",
                F(
                    r"Vận tốc và quãng đường rơi sau thời gian $t$",
                    r"$v = g t \quad ; \quad s = h = \dfrac{1}{2}gt^2$",
                    r"$g \approx 9,8\text{ m/s}^2$ là gia tốc rơi tự do",
                ),
                F(
                    r"Vận tốc và thời gian khi rơi từ độ cao $h$",
                    r"$v = \sqrt{2gh} \quad ; \quad t = \sqrt{\dfrac{2h}{g}}$",
                    r"Suy ra trực tiếp từ $v^2 = 2gh$ và $h = \dfrac{1}{2}gt^2$",
                ),
            ),
            G(
                "Chuyển động ném ngang và ném xiên",
                F(
                    r"Ném ngang từ độ cao $H$ với vận tốc $v_0$",
                    r"$t = \sqrt{\dfrac{2H}{g}} \quad ; \quad L = v_0\sqrt{\dfrac{2H}{g}} \quad ; \quad v = \sqrt{v_0^2 + (gt)^2}$",
                    r"$t$ là thời gian rơi, $L$ là tầm bay xa, $v$ là độ lớn vận tốc lúc chạm đất",
                ),
                F(
                    r"Ném xiên góc $\alpha$ từ mặt đất",
                    r"$H = \dfrac{v_0^2\sin^2\alpha}{2g} \quad ; \quad L = \dfrac{v_0^2\sin 2\alpha}{g}$",
                    r"$H$ là tầm bay cao cực đại, $L$ là tầm bay xa ($L_{\max}$ khi $\alpha = 45^\circ$)",
                ),
            ),
        ],
        "example": r"""
Một người đứng trên đỉnh một tháp cao $H = 45\text{ m}$ ném một quả bóng nhỏ theo phương nằm ngang với vận tốc ban đầu $v_0 = 20\text{ m/s}$. Bỏ qua sức cản của không khí và lấy gia tốc rơi tự do $g = 10\text{ m/s}^2$.
1. Viết phương trình tọa độ theo phương ngang $x(t)$, phương thẳng đứng $y(t)$ và phương trình quỹ đạo của quả bóng.
2. Tính thời gian quả bóng bay trong không khí, tầm bay xa $L$ và độ lớn vận tốc của quả bóng ngay trước khi chạm đất.
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. Chọn hệ trục tọa độ $Oxy$ có gốc $O$ tại vị trí ném, trục $Ox$ nằm ngang hướng theo $\overrightarrow{v}_0$, trục $Oy$ thẳng đứng hướng xuống dưới, gốc thời gian $t = 0$ lúc ném:
   - Phương trình tọa độ theo trục $Ox$:
     $$x = v_0 t = 20t \text{ (m)}$$
   - Phương trình tọa độ theo trục $Oy$:
     $$y = \dfrac{1}{2}gt^2 = \dfrac{1}{2} \cdot 10 \cdot t^2 = 5t^2 \text{ (m)}$$
   - Khử $t = \dfrac{x}{20}$ thế vào $y$, ta được phương trình quỹ đạo:
     $$y = 5 \cdot \left(\dfrac{x}{20}\right)^2 = \dfrac{x^2}{80} \text{ (m)}$$
     Quỹ đạo là một nhánh parabol.
2. Khi quả bóng chạm đất thì $y = H = 45\text{ m}$:
   - Thời gian quả bóng bay trong không khí:
     $$t = \sqrt{\dfrac{2H}{g}} = \sqrt{\dfrac{2 \cdot 45}{10}} = \sqrt{9} = 3\text{ s}$$
   - Tầm bay xa theo phương ngang của quả bóng:
     $$L = v_0 \cdot t = 20 \cdot 3 = 60\text{ m}$$
   - Ngay trước khi chạm đất ($t = 3\text{ s}$), các thành phần vận tốc là:
     $$v_x = v_0 = 20\text{ m/s} \quad ; \quad v_y = gt = 10 \cdot 3 = 30\text{ m/s}$$
     Độ lớn vận tốc của quả bóng ngay trước khi chạm đất:
     $$v = \sqrt{v_x^2 + v_y^2} = \sqrt{20^2 + 30^2} = \sqrt{1300} = 10\sqrt{13} \approx 36,06\text{ m/s}$$
""",
        "real_life": r"""
Trong an toàn giao thông đường bộ, công thức $d = -\dfrac{v_0^2}{2a}$ giải thích vì sao khi tốc độ xe $v_0$ tăng gấp đôi thì **quãng đường phanh tối thiểu** tăng lên gấp $4$ lần — đó là cơ sở khoa học để quy định khoảng cách an toàn tối thiểu trên đường cao tốc. Trong thể thao (đẩy tạ, ném lao, bóng rổ, sút phạt bóng đá) và cứu hộ hàng không (thả hàng cứu trợ từ máy bay bay ngang), các vận động viên và phi công vận dụng quy luật chuyển động ném xiên và ném ngang để tính toán góc ném và vị trí thả chính xác.
""",
        "game_title": "Phòng Thử Nghiệm Gia Tốc & Đường Đạn Parabol",
        "game_description": "Mô phỏng phanh xe khẩn cấp, đo gia tốc rơi tự do qua cổng quang điện và căn chỉnh góc ném xiên, vận tốc đầu để trúng mục tiêu.",
        "game_type": "game_giatoc",
        "quiz": [
            mcq(
                "biet",
                r"Đơn vị chuẩn của gia tốc trong hệ đơn vị quốc tế SI là:",
                [
                    r"$\text{m/s}$",
                    r"$\text{m/s}^2$",
                    r"$\text{km/h}$",
                    r"$\text{m}\cdot\text{s}^2$",
                ],
                1,
                r"Theo Bài 8 SGK Vật lí 10 KNTT, vì $a = \dfrac{\Delta v}{\Delta t}$ trong đó $\Delta v$ có đơn vị $\text{m/s}$ và $\Delta t$ có đơn vị $\text{s}$ nên đơn vị của gia tốc là $\text{m/s}^2$.",
            ),
            mcq(
                "biet",
                r"Trong chuyển động thẳng biến đổi đều, hệ thức liên hệ độc lập với thời gian giữa vận tốc $v$, vận tốc đầu $v_0$, gia tốc $a$ và độ dịch chuyển $d$ là:",
                [
                    r"$v^2 - v_0^2 = 2ad$",
                    r"$v - v_0 = 2ad$",
                    r"$v^2 + v_0^2 = 2ad$",
                    r"$v^2 - v_0^2 = ad$",
                ],
                0,
                r"Theo Bài 9 SGK Vật lí 10 KNTT, công thức liên hệ giữa vận tốc, gia tốc và độ dịch chuyển là $v^2 - v_0^2 = 2ad$.",
            ),
            mcq(
                "biet",
                r"Chuyển động của vật nào dưới đây trong không khí có thể được coi gần đúng là sự rơi tự do?",
                [
                    r"Một chiếc lá khô đang rơi lảo đảo từ trên cây xuống đất.",
                    r"Một vận động viên nhảy dù đang bung dù hạ cánh.",
                    r"Một viên bi thép đặc được thả rơi từ độ cao $3\text{ m}$ xuống mặt đất.",
                    r"Một chiếc máy bay giấy được phóng đi trong lớp học.",
                ],
                2,
                r"Theo Bài 10 SGK Vật lí 10 KNTT, viên bi thép đặc có trọng lượng lớn hơn rất nhiều so với lực cản của không khí nên chuyển động rơi của nó được coi là rơi tự do.",
            ),
            mcq(
                "biet",
                r"Trong chuyển động ném xiên từ mặt đất (bỏ qua sức cản của không khí), với cùng một độ lớn vận tốc ban đầu $v_0$, tầm bay xa $L$ của vật đạt giá trị cực đại khi góc ném $\alpha$ (hợp với phương ngang) bằng:",
                [
                    r"$30^\circ$",
                    r"$45^\circ$",
                    r"$60^\circ$",
                    r"$90^\circ$",
                ],
                1,
                r"Theo Bài 12 SGK Vật lí 10 KNTT, từ công thức $L = \dfrac{v_0^2\sin 2\alpha}{g}$, tầm bay xa đạt cực đại khi $\sin 2\alpha = 1 \iff 2\alpha = 90^\circ \iff \alpha = 45^\circ$.",
            ),
            mcq(
                "hieu",
                r"Một đoàn tàu đang chạy với tốc độ $72\text{ km/h}$ thì hãm phanh chuyển động thẳng chậm dần đều, sau $10\text{ s}$ tốc độ giảm xuống còn $36\text{ km/h}$. Chọn chiều dương là chiều chuyển động của đoàn tàu. Gia tốc của đoàn tàu có giá trị là:",
                [
                    r"$a = 1,0\text{ m/s}^2$",
                    r"$a = -1,0\text{ m/s}^2$",
                    r"$a = -3,6\text{ m/s}^2$",
                    r"$a = 2,0\text{ m/s}^2$",
                ],
                1,
                r"Đổi $v_0 = 72\text{ km/h} = 20\text{ m/s}$; $v = 36\text{ km/h} = 10\text{ m/s}$. Gia tốc của tàu là $a = \dfrac{v - v_0}{\Delta t} = \dfrac{10 - 20}{10} = -1,0\text{ m/s}^2$.",
            ),
            mcq(
                "hieu",
                r"Một vật được thả rơi tự do từ độ cao $h = 19,6\text{ m}$ xuống mặt đất tại nơi có gia tốc rơi tự do $g = 9,8\text{ m/s}^2$. Thời gian rơi $t$ và tốc độ $v$ của vật ngay khi chạm đất là:",
                [
                    r"$t = 2,0\text{ s}$ và $v = 19,6\text{ m/s}$",
                    r"$t = 4,0\text{ s}$ và $v = 39,2\text{ m/s}$",
                    r"$t = 2,0\text{ s}$ và $v = 9,8\text{ m/s}$",
                    r"$t = 1,4\text{ s}$ và $v = 19,6\text{ m/s}$",
                ],
                0,
                r"Thời gian rơi: $t = \sqrt{\dfrac{2h}{g}} = \sqrt{\dfrac{2 \cdot 19,6}{9,8}} = \sqrt{4} = 2,0\text{ s}$. Tốc độ khi chạm đất: $v = gt = 9,8 \cdot 2,0 = 19,6\text{ m/s}$.",
            ),
            tf4(
                "hieu",
                r"Một chất điểm chuyển động dọc theo trục $Ox$ có đồ thị vận tốc – thời gian ($v - t$) gồm hai đoạn thẳng: Từ $t = 0$ đến $t_1 = 4\text{ s}$, vận tốc tăng đều từ $v_0 = 2\text{ m/s}$ lên $v_1 = 10\text{ m/s}$; từ $t_1 = 4\text{ s}$ đến $t_2 = 6\text{ s}$, vận tốc giảm đều từ $10\text{ m/s}$ về $0\text{ m/s}$.",
                [
                    r"Trong khoảng thời gian từ $0$ đến $4\text{ s}$, chất điểm chuyển động thẳng nhanh dần đều với gia tốc $a_1 = 2\text{ m/s}^2$.",
                    r"Tại thời điểm $t_1 = 4\text{ s}$, chất điểm bắt đầu đổi chiều chuyển động để quay về vị trí xuất phát.",
                    r"Trong khoảng thời gian từ $4\text{ s}$ đến $6\text{ s}$, gia tốc của chất điểm có giá trị là $a_2 = -5\text{ m/s}^2$.",
                    r"Tổng độ dịch chuyển của chất điểm trong cả $6\text{ s}$ chuyển động là $d = 34\text{ m}$.",
                ],
                [True, False, True, True],
                r"""- **a) Đúng:** Gia tốc trong $4\text{ s}$ đầu là $a_1 = \dfrac{10 - 2}{4 - 0} = 2\text{ m/s}^2 > 0$ và $v > 0$ nên là chuyển động thẳng nhanh dần đều.
- **b) Sai:** Từ $4\text{ s}$ đến $6\text{ s}$, vận tốc giảm từ $10\text{ m/s}$ về $0\text{ m/s}$ nhưng vẫn mang dấu dương ($v > 0$), tức vật chỉ chuyển động chậm dần đều theo chiều dương chứ **chưa đổi chiều** chuyển động.
- **c) Đúng:** $a_2 = \dfrac{0 - 10}{6 - 4} = -5\text{ m/s}^2$.
- **d) Đúng:** Độ dịch chuyển bằng diện tích dưới đồ thị $v - t$: $d = d_1 + d_2 = \dfrac{2 + 10}{2} \cdot 4 + \dfrac{10 + 0}{2} \cdot 2 = 24 + 10 = 34\text{ m}$.""",
            ),
            tf4(
                "hieu",
                r"Tại cùng một thời điểm và từ cùng một độ cao $H = 20\text{ m}$ so với mặt đất phẳng ngang, viên bi $A$ được thả rơi tự do không vận tốc đầu, còn viên bi $B$ được ném theo phương nằm ngang với tốc độ đầu $v_0 = 15\text{ m/s}$. Bỏ qua sức cản của không khí và lấy $g = 10\text{ m/s}^2$.",
                [
                    r"Chuyển động thành phần theo phương thẳng đứng của viên bi $B$ hoàn toàn giống chuyển động rơi tự do của viên bi $A$.",
                    r"Viên bi $A$ chạm đất trước viên bi $B$ vì viên bi $B$ phải đi một quãng đường cong dài hơn.",
                    r"Cả hai viên bi $A$ và $B$ đều chạm đất sau khoảng thời gian $t = 2\text{ s}$ kể từ lúc thả hoặc ném.",
                    r"Khoảng cách giữa hai viên bi ngay khi chúng vừa chạm đất bằng tầm bay xa của viên bi $B$ và bằng $30\text{ m}$.",
                ],
                [True, False, True, True],
                r"""- **a) Đúng:** Theo phương thẳng đứng, cả hai viên bi đều có vận tốc đầu theo phương đứng bằng $0$ và chịu cùng gia tốc $g$.
- **b) Sai:** Thời gian rơi của vật ném ngang là $t = \sqrt{\dfrac{2H}{g}}$, không phụ thuộc vào $v_0$, nên hai viên bi chạm đất **cùng một lúc**.
- **c) Đúng:** $t = \sqrt{\dfrac{2 \cdot 20}{10}} = 2\text{ s}$.
- **d) Đúng:** Viên bi $A$ rơi thẳng đứng xuống chân đường cao, viên bi $B$ chạm đất cách chân đường cao một đoạn bằng tầm bay xa $L = v_0 t = 15 \cdot 2 = 30\text{ m}$.""",
            ),
            mcq(
                "vandung",
                r"Một ô tô đang chạy trên đường thẳng với tốc độ $v_0 = 54\text{ km/h}$ thì người lái xe phát hiện chướng ngại vật nên đạp phanh. Kể từ lúc hãm phanh, ô tô chuyển động thẳng chậm dần đều với gia tốc có độ lớn $3,0\text{ m/s}^2$ cho đến khi dừng hẳn. Quãng đường ô tô đi thêm được kể từ lúc bắt đầu hãm phanh đến khi dừng lại là:",
                [
                    r"$37,5\text{ m}$",
                    r"$75,0\text{ m}$",
                    r"$22,5\text{ m}$",
                    r"$45,0\text{ m}$",
                ],
                0,
                r"""Đổi $v_0 = 54\text{ km/h} = 15\text{ m/s}$. Chọn chiều dương là chiều chuyển động thì $a = -3,0\text{ m/s}^2$, khi dừng hẳn $v = 0$.
Áp dụng công thức $v^2 - v_0^2 = 2ad$, ta có:
$$d = \dfrac{v^2 - v_0^2}{2a} = \dfrac{0^2 - 15^2}{2 \cdot (-3,0)} = \dfrac{-225}{-6,0} = 37,5\text{ m}$$""",
            ),
            short(
                "vandung",
                r"Một cầu thủ sút một quả bóng từ mặt đất với tốc độ ban đầu $v_0 = 20\text{ m/s}$ theo phương hợp với mặt đất nằm ngang một góc $\alpha = 30^\circ$. Bỏ qua sức cản của không khí và lấy $g = 10\text{ m/s}^2$. Tính độ cao cực đại $H$ mà quả bóng đạt được so với mặt đất theo đơn vị mét ($\text{m}$), chỉ ghi phần số.",
                ["5", "5,0", "5.0"],
                r"Áp dụng công thức tầm bay cao cực đại của chuyển động ném xiên: $H = \dfrac{v_0^2 \sin^2\alpha}{2g} = \dfrac{20^2 \cdot (\sin 30^\circ)^2}{2 \cdot 10} = \dfrac{400 \cdot 0,25}{20} = 5\text{ m}$.",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG III. ĐỘNG LỰC HỌC (Bài 13 -> Bài 22)
    # =========================================================================
    {
        "topic": "dinh-luat-newton",
        "title": "Chương III. Động lực học: Tổng hợp lực, Ba định luật Newton, Các lực cơ học và Moment lực",
        "icon": "🍎",
        "description": "Khảo sát mối liên hệ giữa lực và chuyển động thông qua ba định luật Newton, trọng lực, lực căng, lực ma sát, lực cản, lực nâng và cân bằng của vật rắn.",
        "requirements": [
            r"Biểu diễn được lực bằng vectơ; thực hiện thí nghiệm hoặc vận dụng quy tắc hình bình hành để tổng hợp hai lực đồng quy và phân tích một lực thành hai lực thành phần vuông góc; nêu được điều kiện cân bằng của chất điểm $\sum \overrightarrow{F} = \overrightarrow{0}$.",
            r"Trình bày được nội dung Định luật 1 Newton, khái niệm quán tính và giải thích được một số hiện tượng thực tế liên quan đến quán tính.",
            r"Thực hiện thí nghiệm hoặc sử dụng số liệu cho trước để rút ra được $a \sim F$ và $a \sim \dfrac{1}{m}$, từ đó phát biểu và vận dụng được Định luật 2 Newton $\overrightarrow{a} = \dfrac{\overrightarrow{F}}{m}$ (hay $\overrightarrow{F} = m\overrightarrow{a}$); nêu được khối lượng là đại lượng đặc trưng cho mức quán tính của vật.",
            r"Phát biểu và vận dụng được Định luật 3 Newton về cặp lực và phản lực $\overrightarrow{F}_{AB} = -\overrightarrow{F}_{BA}$.",
            r"Phân biệt được trọng lượng $P = mg$ và khối lượng $m$; mô tả được đặc điểm của lực căng dây, lực ma sát nghỉ, lực ma sát trượt ($F_{\text{mst}} = \mu N$), lực cản của chất lưu và lực nâng (lực đẩy Archimedes).",
            r"Nêu được khái niệm moment lực $M = F \cdot d$, moment ngẫu lực và vận dụng được quy tắc moment lực cho điều kiện cân bằng của vật rắn có trục quay cố định.",
        ],
        "definition": r"""
**Động lực học** nghiên cứu nguyên nhân gây ra sự thay đổi trạng thái chuyển động của các vật dưới tác dụng của **lực**. Nền tảng của Động lực học cổ điển là **Ba định luật Newton** (về quán tính, mối liên hệ giữa gia tốc $\overrightarrow{a} = \dfrac{\overrightarrow{F}_{\text{hl}}}{m}$ và tương tác hai chiều $\overrightarrow{F}_{AB} = -\overrightarrow{F}_{BA}$) cùng với **Quy tắc moment lực** ($M = F \cdot d$) quy định điều kiện cân bằng quay của vật rắn.
""",
        "theory": r"""
### Bài 13. Tổng hợp và phân tích lực. Cân bằng lực

- **Tổng hợp lực:** Là phép thay thế các lực tác dụng đồng thời vào cùng một vật bằng một lực có tác dụng giống hệt như các lực ấy. Lực thay thế này gọi là **hợp lực** $\overrightarrow{F} = \overrightarrow{F}_1 + \overrightarrow{F}_2 + \dots$.
  + **Hai lực cùng phương, cùng chiều:** $F = F_1 + F_2$.
  + **Hai lực cùng phương, ngược chiều:** $F = |F_1 - F_2|$ (hợp lực cùng chiều với lực có độ lớn lớn hơn).
  + **Hai lực đồng quy hợp nhau góc $\alpha$:** Áp dụng quy tắc hình bình hành:
    $$F = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos\alpha} \quad \text{với} \quad |F_1 - F_2| \le F \le F_1 + F_2$$
- **Các lực cân bằng và không cân bằng:**
  + Nếu hợp lực tác dụng lên vật bằng $\overrightarrow{0}$ ($\sum \overrightarrow{F} = \overrightarrow{0}$) thì các lực đó gọi là các lực cân bằng; vật đứng yên sẽ tiếp tục đứng yên, vật đang chuyển động sẽ chuyển động thẳng đều.
- **Phân tích lực:** Là phép thay thế một lực bằng hai hay nhiều lực thành phần có tác dụng giống hệt như lực đó (thường chiếu lên hai trục tọa độ vuông góc $Ox, Oy$: $F_x = F\cos\alpha$, $F_y = F\sin\alpha$).

### Bài 14. Định luật 1 Newton

- **Thí nghiệm lí tưởng của Galileo:** Bác bỏ quan điểm sai lầm của Aristotle (cho rằng phải có lực mới duy trì được chuyển động). Galileo chỉ ra rằng nếu không có ma sát, vật đang chuyển động sẽ giữ nguyên tốc độ mãi mãi.
- **Định luật 1 Newton:** Nếu một vật không chịu tác dụng của lực nào hoặc chịu tác dụng của các lực có hợp lực bằng không ($\overrightarrow{F}_{\text{hl}} = \overrightarrow{0}$), thì vật đang đứng yên sẽ tiếp tục đứng yên, đang chuyển động sẽ tiếp tục chuyển động thẳng đều.
- **Quán tính:** Là tính chất của mọi vật có xu hướng bảo toàn vận tốc cả về hướng và độ lớn. Định luật 1 Newton còn được gọi là định luật quán tính.

### Bài 15. Định luật 2 Newton

- **Nội dung Định luật 2 Newton:** Gia tốc của một vật cùng hướng với lực tác dụng lên vật. Độ lớn của gia tốc tỉ lệ thuận với độ lớn của lực và tỉ lệ nghịch với khối lượng của vật:
  $$\overrightarrow{a} = \dfrac{\overrightarrow{F}_{\text{hl}}}{m} \iff \overrightarrow{F}_{\text{hl}} = m\overrightarrow{a}$$
  Đơn vị của lực trong hệ SI là niutơn ($\text{N}$): $1\text{ N} = 1\text{ kg}\cdot\text{m/s}^2$.
- **Khối lượng và mức quán tính:** Khối lượng $m$ không chỉ chỉ lượng chất mà còn là đại lượng vô hướng dương đặc trưng cho **mức quán tính** của vật (vật có khối lượng càng lớn thì mức quán tính càng lớn, càng khó thay đổi vận tốc).

### Bài 16. Định luật 3 Newton

- **Nội dung Định luật 3 Newton:** Trong mọi trường hợp, khi vật $A$ tác dụng lên vật $B$ một lực thì vật $B$ cũng tác dụng trở lại lên vật $A$ một lực. Hai lực này là hai lực trực đối (cùng giá, cùng độ lớn nhưng ngược chiều):
  $$\overrightarrow{F}_{AB} = -\overrightarrow{F}_{BA}$$
- **Đặc điểm của cặp lực và phản lực:**
  + Luôn xuất hiện và mất đi đồng thời.
  + Cùng bản chất vật lí (cùng là lực đàn hồi, cùng là lực hấp dẫn, hoặc cùng là lực ma sát).
  + Tác dụng vào **hai vật khác nhau** nên **không bao giờ triệt tiêu (cân bằng) nhau**.

### Bài 17. Trọng lực và lực căng

- **Trọng lực ($\overrightarrow{P}$):** Là lực hút của Trái Đất tác dụng lên vật, có điểm đặt tại **trọng tâm** của vật, phương thẳng đứng, chiều từ trên xuống dưới, biểu thức $\overrightarrow{P} = m\overrightarrow{g}$.
- **Trọng lượng ($P$):** Độ lớn của trọng lực tác dụng lên một vật đứng yên trên mặt đất ($P = mg$). Trọng lượng thay đổi theo vị trí địa lí và độ cao (vì $g$ thay đổi), còn khối lượng $m$ của vật thì không đổi.
- **Lực căng dây ($\overrightarrow{T}$):** Xuất hiện khi một sợi dây bị kéo căng, có điểm đặt tại vị trí đầu dây tiếp xúc với vật, phương trùng với phương của sợi dây, chiều hướng từ hai đầu dây vào phần giữa của sợi dây (luôn là lực kéo, không bao giờ là lực đẩy).

### Bài 18. Lực ma sát

- **Lực ma sát nghỉ ($\overrightarrow{F}_{\text{msn}}$):** Xuất hiện ở mặt tiếp xúc khi vật chịu lực kéo nhưng vẫn đứng yên trên bề mặt. Lực ma sát nghỉ cân bằng với ngoại lực thành phần song song mặt tiếp xúc và có giá trị cực đại $F_{\text{msn max}}$.
- **Lực ma sát trượt ($\overrightarrow{F}_{\text{mst}}$):** Xuất hiện ở mặt tiếp xúc khi vật trượt trên một bề mặt, có hướng ngược với hướng chuyển động tương đối của vật so với bề mặt.
  + Độ lớn: $F_{\text{mst}} = \mu N$, trong đó $N$ là độ lớn áp lực (phản lực pháp tuyến) vuông góc với mặt tiếp xúc, $\mu$ là hệ số ma sát trượt (phụ thuộc vào bản chất và tình trạng của hai mặt tiếp xúc, **không phụ thuộc diện tích tiếp xúc**).

### Bài 19. Lực cản và lực nâng

- **Lực cản của chất lưu (không khí, nước):** Tác dụng lên vật chuyển động trong chất lưu, luôn ngược hướng chuyển động và có độ lớn phụ thuộc vào **hình dạng** của vật (hình khí động học giúp giảm lực cản) và **tốc độ** của vật (tốc độ càng lớn thì lực cản càng lớn).
- **Lực nâng trong chất lưu:** Gồm lực nâng khí động học (giúp máy bay, chim bay lên) và **lực đẩy Archimedes** hướng thẳng đứng từ dưới lên: $F_A = \rho g V$ (với $\rho$ là khối lượng riêng của chất lỏng hoặc chất khí, $V$ là thể tích phần chất lỏng hoặc chất khí bị vật chiếm chỗ).

### Bài 20. Một số ví dụ về cách giải các bài toán thuộc phần động lực học

- **Quy trình $4$ bước giải bài toán Động lực học:**
  1. Chọn vật khảo sát và biểu diễn đầy đủ các lực tác dụng lên vật ($\overrightarrow{P}, \overrightarrow{N}, \overrightarrow{T}, \overrightarrow{F}_{\text{k}}, \overrightarrow{F}_{\text{ms}}$).
  2. Chọn hệ trục tọa độ vuông góc $Oxy$ thuận tiện ($Ox$ trùng phương chuyển động, $Oy$ vuông góc phương chuyển động).
  3. Viết phương trình Định luật 2 Newton dạng vectơ: $\overrightarrow{P} + \overrightarrow{N} + \overrightarrow{F}_{\text{k}} + \overrightarrow{F}_{\text{ms}} = m\overrightarrow{a}$.
  4. Chiếu phương trình vectơ lên hai trục $Ox, Oy$ để thu được hệ phương trình đại số và giải tìm đại lượng cần thiết.

### Bài 21. Moment lực. Cân bằng của vật rắn

- **Moment lực đối với một trục quay:** Là đại lượng đặc trưng cho tác dụng làm quay của lực quanh trục ấy, đo bằng tích của độ lớn lực $F$ với cánh tay đòn $d$:
  $$M = F \cdot d \quad (\text{Đơn vị: }\text{N}\cdot\text{m})$$
  Trong đó **cánh tay đòn $d$** là khoảng cách vuông góc từ trục quay đến giá của lực.
- **Quy tắc moment lực (Điều kiện cân bằng của vật có trục quay cố định):** Muốn cho một vật có trục quay cố định ở trạng thái cân bằng, thì tổng các moment lực có xu hướng làm vật quay theo chiều kim đồng hồ phải bằng tổng các moment lực có xu hướng làm vật quay ngược chiều kim đồng hồ.
- **Ngẫu lực:** Là hệ hai lực song song, ngược chiều, có độ lớn bằng nhau ($F_1 = F_2 = F$) và cùng tác dụng vào một vật. Ngẫu lực chỉ làm vật quay chứ không làm vật tịnh tiến. Moment của ngẫu lực: $M = F \cdot d$ (với $d$ là khoảng cách giữa hai giá của hai lực), không phụ thuộc vào vị trí trục quay vuông góc với mặt phẳng chứa ngẫu lực.
- **Điều kiện cân bằng tổng quát của vật rắn:** (1) Tổng các lực tác dụng lên vật bằng $\overrightarrow{0}$ ($\sum \overrightarrow{F} = \overrightarrow{0}$) và (2) Tổng các moment lực đối với một trục quay bất kì bằng $0$ ($\sum M = 0$).

### Bài 22. Thực hành: Tổng hợp lực

- Sử dụng bảng từ, hai lực kế lò xo, thước đo góc và dây chỉ để kiểm nghiệm quy tắc hình bình hành đối với hai lực đồng quy $\overrightarrow{F}_1, \overrightarrow{F}_2$ và đối chiếu với lực thay thế duy nhất $\overrightarrow{F}$.
""",
        "formulas": [
            G(
                "Tổng hợp lực và Ba định luật Newton",
                F(
                    "Độ lớn hợp lực của hai lực đồng quy",
                    r"$F = \sqrt{F_1^2 + F_2^2 + 2F_1 F_2 \cos\alpha}$",
                    r"Khi $\overrightarrow{F}_1 \perp \overrightarrow{F}_2$ ($\alpha = 90^\circ$) thì $F = \sqrt{F_1^2 + F_2^2}$",
                ),
                F(
                    "Định luật 2 Newton",
                    r"$\overrightarrow{a} = \dfrac{\overrightarrow{F}_{\text{hl}}}{m} \iff \overrightarrow{F}_{\text{hl}} = m\overrightarrow{a}$",
                    r"$m$ tính bằng $\text{kg}$, $a$ tính bằng $\text{m/s}^2$, $F_{\text{hl}}$ tính bằng $\text{N}$",
                ),
                F(
                    "Định luật 3 Newton",
                    r"$\overrightarrow{F}_{AB} = -\overrightarrow{F}_{BA} \implies F_{AB} = F_{BA}$",
                    r"Cặp lực và phản lực cùng giá, ngược chiều, đặt vào hai vật khác nhau",
                ),
            ),
            G(
                "Các lực cơ học thường gặp",
                F(
                    "Trọng lực và trọng lượng",
                    r"$\overrightarrow{P} = m\overrightarrow{g} \implies P = mg$",
                    r"Đặt tại trọng tâm vật, hướng thẳng đứng từ trên xuống",
                ),
                F(
                    "Lực ma sát trượt",
                    r"$F_{\text{mst}} = \mu N$",
                    r"$\mu$ là hệ số ma sát trượt, $N$ là áp lực vuông góc lên mặt tiếp xúc",
                ),
                F(
                    r"Áp lực và gia tốc trên mặt phẳng nghiêng góc $\alpha$",
                    r"$N = mg\cos\alpha \quad ; \quad a = g(\sin\alpha - \mu\cos\alpha)$",
                    r"Áp dụng cho vật trượt xuống mặt phẳng nghiêng có hệ số ma sát $\mu$",
                ),
                F(
                    "Lực đẩy Archimedes",
                    r"$F_A = \rho g V$",
                    r"$\rho$ là khối lượng riêng chất lưu ($\text{kg/m}^3$), $V$ là thể tích chất lưu bị chiếm chỗ ($\text{m}^3$)",
                ),
            ),
            G(
                "Moment lực và Cân bằng của vật rắn",
                F(
                    "Moment lực đối với trục quay",
                    r"$M = F \cdot d$",
                    r"$d$ là cánh tay đòn ($\text{m}$), đơn vị của $M$ là $\text{N}\cdot\text{m}$",
                ),
                F(
                    "Quy tắc moment lực",
                    r"$\sum M_{\text{thuận chiều kim đồng hồ}} = \sum M_{\text{ngược chiều kim đồng hồ}}$",
                    r"Ví dụ thanh nhẹ cân bằng quanh trục $O$: $F_1 d_1 = F_2 d_2$",
                ),
                F(
                    "Moment của ngẫu lực",
                    r"$M = F \cdot d$",
                    r"$d$ là khoảng cách vuông góc giữa hai giá của hai lực tạo thành ngẫu lực",
                ),
            ),
        ],
        "example": r"""
Một thùng hàng có khối lượng $m = 20\text{ kg}$ đặt trên mặt sàn nằm ngang. Người ta kéo thùng hàng bằng một lực $\overrightarrow{F}_{\text{k}}$ có độ lớn $F_{\text{k}} = 100\text{ N}$ hướng chếch lên trên và hợp với phương nằm ngang một góc $\alpha = 30^\circ$. Biết hệ số ma sát trượt giữa thùng hàng và sàn nhà là $\mu = 0,2$, lấy $g = 10\text{ m/s}^2$ và $\sqrt{3} \approx 1,732$.
1. Tính độ lớn áp lực $N$ của thùng hàng tác dụng lên mặt sàn và lực ma sát trượt $F_{\text{mst}}$.
2. Tính gia tốc $a$ của thùng hàng và quãng đường thùng hàng đi được sau $4\text{ s}$ kể từ lúc bắt đầu chuyển động ($v_0 = 0$).
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. Chọn hệ trục tọa độ $Oxy$ có trục $Ox$ nằm ngang cùng chiều chuyển động, trục $Oy$ thẳng đứng hướng lên trên.
   Các lực tác dụng lên thùng hàng gồm: Trọng lực $\overrightarrow{P}$, phản lực pháp tuyến $\overrightarrow{N}$, lực kéo $\overrightarrow{F}_{\text{k}}$ và lực ma sát trượt $\overrightarrow{F}_{\text{mst}}$.
   Chiếu phương trình Định luật 2 Newton $\overrightarrow{P} + \overrightarrow{N} + \overrightarrow{F}_{\text{k}} + \overrightarrow{F}_{\text{mst}} = m\overrightarrow{a}$ lên trục $Oy$ (vật không chuyển động theo phương $Oy$ nên $a_y = 0$):
   $$N + F_{\text{k}}\sin\alpha - P = 0 \implies N = mg - F_{\text{k}}\sin 30^\circ = 20 \cdot 10 - 100 \cdot 0,5 = 150\text{ N}$$
   Độ lớn lực ma sát trượt tác dụng lên thùng hàng là:
   $$F_{\text{mst}} = \mu N = 0,2 \cdot 150 = 30\text{ N}$$
2. Chiếu phương trình Định luật 2 Newton lên trục $Ox$:
   $$F_{\text{k}}\cos\alpha - F_{\text{mst}} = ma$$
   Thay số vào phương trình:
   $$100 \cdot \cos 30^\circ - 30 = 20a \implies 50\sqrt{3} - 30 = 20a$$
   $$a = \dfrac{50 \cdot 1,732 - 30}{20} = \dfrac{86,6 - 30}{20} = 2,83\text{ m/s}^2$$
   Quãng đường thùng hàng đi được sau $t = 4\text{ s}$ kể từ lúc đứng yên ($v_0 = 0$) là:
   $$s = \dfrac{1}{2}at^2 = \dfrac{1}{2} \cdot 2,83 \cdot 4^2 = 22,64\text{ m}$$
""",
        "real_life": r"""
Dây đai an toàn và túi khí trên ô tô được thiết kế trực tiếp dựa trên **Định luật 1 Newton** để giữ hành khách không lao về phía trước theo quán tính khi xe phanh gấp hoặc va chạm. Trong khi đó, động cơ tên lửa đẩy tàu vũ trụ rời bệ phóng trong chân không hoạt động dựa trên **Định luật 3 Newton** (phụt luồng khí nóng cực mạnh về phía sau để nhận phản lực đẩy về phía trước), còn cờ lê, tay nắm cửa, cần cẩu tháp đều tối ưu hóa cánh tay đòn $d$ để tạo **moment lực** $M = F \cdot d$ lớn nhất với lực tác dụng nhỏ nhất.
""",
        "game_title": "Đấu Trường Động Lực Học Newton & Cân Bằng Đòn Bẩy",
        "game_description": "Thử nghiệm tổng hợp lực, điều chỉnh lực kéo có ma sát trên mặt phẳng nghiêng và cân bằng hệ thống đòn bẩy bằng moment lực.",
        "game_type": "game_newton",
        "quiz": [
            mcq(
                "biet",
                r"Theo Định luật 1 Newton, khi hợp lực của tất cả các lực tác dụng lên một vật bằng $\overrightarrow{0}$ thì vật đó sẽ:",
                [
                    r"Luôn luôn đứng yên tại chỗ.",
                    r"Chuyển động thẳng nhanh dần đều.",
                    r"Đang đứng yên sẽ tiếp tục đứng yên, đang chuyển động sẽ tiếp tục chuyển động thẳng đều.",
                    r"Chuyển động thẳng chậm dần đều rồi dừng lại.",
                ],
                2,
                r"Theo Bài 14 SGK Vật lí 10 KNTT, khi $\overrightarrow{F}_{\text{hl}} = \overrightarrow{0}$, vật bảo toàn vận tốc: đang đứng yên sẽ tiếp tục đứng yên, đang chuyển động sẽ tiếp tục chuyển động thẳng đều.",
            ),
            mcq(
                "biet",
                r"Đại lượng vật lí nào sau đây đặc trưng cho mức quán tính của một vật?",
                [
                    r"Vận tốc của vật.",
                    r"Khối lượng của vật.",
                    r"Trọng lượng của vật.",
                    r"Hợp lực tác dụng lên vật.",
                ],
                1,
                r"Theo Bài 15 SGK Vật lí 10 KNTT, khối lượng $m$ là đại lượng đặc trưng cho mức quán tính của vật.",
            ),
            mcq(
                "biet",
                r"Theo Định luật 3 Newton, cặp lực và phản lực trong tương tác giữa hai vật có đặc điểm nào sau đây?",
                [
                    r"Đặt vào cùng một vật nên cân bằng nhau.",
                    r"Cùng giá, cùng chiều và cùng độ lớn.",
                    r"Cùng giá, ngược chiều, cùng độ lớn và đặt vào hai vật khác nhau.",
                    r"Lực tác dụng luôn xuất hiện trước phản lực một khoảng thời gian ngắn.",
                ],
                2,
                r"Theo Bài 16 SGK Vật lí 10 KNTT, lực và phản lực là hai lực trực đối ($\overrightarrow{F}_{AB} = -\overrightarrow{F}_{BA}$) xuất hiện đồng thời và đặt vào hai vật khác nhau nên không triệt tiêu nhau.",
            ),
            mcq(
                "biet",
                r"Moment lực $M$ của một lực $\overrightarrow{F}$ đối với một trục quay có cánh tay đòn $d$ được xác định bởi công thức và đơn vị chuẩn trong hệ SI là:",
                [
                    r"$M = F \cdot d$, đơn vị $\text{N}\cdot\text{m}$",
                    r"$M = \dfrac{F}{d}$, đơn vị $\text{N/m}$",
                    r"$M = F \cdot d^2$, đơn vị $\text{N}\cdot\text{m}^2$",
                    r"$M = \dfrac{d}{F}$, đơn vị $\text{m/N}$",
                ],
                0,
                r"Theo Bài 21 SGK Vật lí 10 KNTT, moment lực được tính bằng $M = F \cdot d$, trong đó $F$ có đơn vị $\text{N}$ và $d$ có đơn vị $\text{m}$ nên đơn vị của moment lực là $\text{N}\cdot\text{m}$.",
            ),
            mcq(
                "hieu",
                r"Cho hai lực đồng quy $\overrightarrow{F}_1$ và $\overrightarrow{F}_2$ có độ lớn lần lượt là $F_1 = 6\text{ N}$ và $F_2 = 8\text{ N}$. Nếu góc hợp bởi hai vectơ lực là $\alpha = 90^\circ$ thì độ lớn của hợp lực $\overrightarrow{F}$ bằng:",
                [
                    r"$14\text{ N}$",
                    r"$2\text{ N}$",
                    r"$10\text{ N}$",
                    r"$7\text{ N}$",
                ],
                2,
                r"Khi hai lực đồng quy vuông góc với nhau ($\alpha = 90^\circ$), độ lớn hợp lực là $F = \sqrt{F_1^2 + F_2^2} = \sqrt{6^2 + 8^2} = 10\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Một người dùng cờ lê để vặn một đai ốc. Lực tác dụng có độ lớn $F = 40\text{ N}$ đặt tại đầu cờ lê cách trục quay của đai ốc một khoảng $l = 25\text{ cm}$ theo phương vuông góc với thân cờ lê. Moment của lực này đối với trục quay của đai ốc bằng:",
                [
                    r"$1000\text{ N}\cdot\text{m}$",
                    r"$10\text{ N}\cdot\text{m}$",
                    r"$160\text{ N}\cdot\text{m}$",
                    r"$1,6\text{ N}\cdot\text{m}$",
                ],
                1,
                r"Vì lực vuông góc với thân cờ lê nên cánh tay đòn $d = l = 25\text{ cm} = 0,25\text{ m}$. Moment lực là $M = F \cdot d = 40 \cdot 0,25 = 10\text{ N}\cdot\text{m}$.",
            ),
            tf4(
                "hieu",
                r"Một khúc gỗ có khối lượng $m = 5\text{ kg}$ đặt trên mặt bàn nằm ngang. Hệ số ma sát trượt giữa khúc gỗ và mặt bàn là $\mu = 0,3$, lấy $g = 10\text{ m/s}^2$. Tác dụng vào khúc gỗ một lực kéo nằm ngang có độ lớn $F_{\text{k}}$.",
                [
                    r"Áp lực của khúc gỗ lên mặt bàn nằm ngang có độ lớn bằng trọng lượng của khúc gỗ và bằng $N = 50\text{ N}$.",
                    r"Khi khúc gỗ trượt trên mặt bàn, độ lớn lực ma sát trượt tác dụng lên khúc gỗ là $F_{\text{mst}} = 15\text{ N}$.",
                    r"Nếu xoay khúc gỗ để diện tích mặt tiếp xúc với bàn giảm đi một nửa thì lực ma sát trượt cũng giảm đi một nửa.",
                    r"Khi kéo khúc gỗ bằng lực nằm ngang $F_{\text{k}} = 25\text{ N}$, khúc gỗ sẽ chuyển động với gia tốc $a = 2\text{ m/s}^2$.",
                ],
                [True, True, False, True],
                r"""- **a) Đúng:** Trên mặt ngang và lực kéo nằm ngang, $N = P = mg = 5 \cdot 10 = 50\text{ N}$.
- **b) Đúng:** $F_{\text{mst}} = \mu N = 0,3 \cdot 50 = 15\text{ N}$.
- **c) Sai:** Độ lớn lực ma sát trượt không phụ thuộc vào diện tích mặt tiếp xúc.
- **d) Đúng:** Theo Định luật 2 Newton: $a = \dfrac{F_{\text{k}} - F_{\text{mst}}}{m} = \dfrac{25 - 15}{5} = 2\text{ m/s}^2$.""",
            ),
            tf4(
                "hieu",
                r"Một thanh cứng nhẹ $AB$ dài $1,2\text{ m}$ có thể quay tự do quanh một trục nằm ngang đi qua điểm $O$ trên thanh với $OA = 0,4\text{ m}$ và $OB = 0,8\text{ m}$. Tại đầu $A$ người ta treo một vật nặng có trọng lượng $P_1 = 60\text{ N}$.",
                [
                    r"Moment của trọng lực $\overrightarrow{P}_1$ đối với trục quay $O$ là $M_1 = P_1 \cdot OA = 24\text{ N}\cdot\text{m}$.",
                    r"Để thanh $AB$ nằm ngang cân bằng, cần treo vào đầu $B$ một vật có trọng lượng $P_2 = 120\text{ N}$.",
                    r"Để thanh $AB$ nằm ngang cân bằng, trọng lượng $P_2$ treo tại đầu $B$ phải thỏa mãn $P_2 \cdot OB = P_1 \cdot OA$, suy ra $P_2 = 30\text{ N}$.",
                    r"Khi thanh $AB$ nằm ngang cân bằng và bỏ qua khối lượng của thanh, phản lực của trục quay $O$ tác dụng lên thanh có độ lớn là $N_O = P_1 + P_2 = 90\text{ N}$.",
                ],
                [True, False, True, True],
                r"""- **a) Đúng:** $M_1 = P_1 \cdot OA = 60 \cdot 0,4 = 24\text{ N}\cdot\text{m}$.
- **b) Sai, c) Đúng:** Theo quy tắc moment lực: $P_1 \cdot OA = P_2 \cdot OB \implies 60 \cdot 0,4 = P_2 \cdot 0,8 \implies P_2 = 30\text{ N}$.
- **d) Đúng:** Khi thanh cân bằng tĩnh, tổng các lực hướng lên bằng tổng các lực hướng xuống: $N_O = P_1 + P_2 = 60 + 30 = 90\text{ N}$.""",
            ),
            mcq(
                "vandung",
                r"Một vật có khối lượng $m = 4\text{ kg}$ được thả trượt không vận tốc đầu từ đỉnh một mặt phẳng nghiêng dài $s = 10\text{ m}$, nghiêng góc $\alpha = 30^\circ$ so với phương ngang. Biết hệ số ma sát trượt giữa vật và mặt phẳng nghiêng là $\mu = \dfrac{\sqrt{3}}{6}$, lấy $g = 10\text{ m/s}^2$. Gia tốc $a$ của vật trên mặt phẳng nghiêng là:",
                [
                    r"$2,5\text{ m/s}^2$",
                    r"$5,0\text{ m/s}^2$",
                    r"$7,5\text{ m/s}^2$",
                    r"$3,0\text{ m/s}^2$",
                ],
                0,
                r"""Áp dụng công thức gia tốc của vật trượt xuống mặt phẳng nghiêng có ma sát:
$$a = g(\sin\alpha - \mu\cos\alpha) = 10 \cdot \left(\sin 30^\circ - \dfrac{\sqrt{3}}{6}\cos 30^\circ\right) = 10 \cdot \left(\dfrac{1}{2} - \dfrac{\sqrt{3}}{6} \cdot \dfrac{\sqrt{3}}{2}\right) = 10 \cdot (0,5 - 0,25) = 2,5\text{ m/s}^2$$""",
            ),
            short(
                "vandung",
                r"Một buồng thang máy có tổng khối lượng $m = 800\text{ kg}$ được kéo đi lên thẳng đứng từ trạng thái đứng yên bằng một dây cáp với lực căng không đổi $T = 9200\text{ N}$. Bỏ qua mọi lực cản và lấy $g = 10\text{ m/s}^2$. Tính gia tốc $a$ của thang máy theo đơn vị $\text{m/s}^2$ (dùng dấu phẩy cho số thập phân, chỉ ghi phần số).",
                ["1,5", "1.5"],
                r"""Chọn chiều dương thẳng đứng hướng lên trên. Phương trình Định luật 2 Newton cho thang máy là:
$$T - P = ma \implies a = \dfrac{T - mg}{m} = \dfrac{9200 - 800 \cdot 10}{800} = \dfrac{1200}{800} = 1,5\text{ m/s}^2$$""",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG IV. NĂNG LƯỢNG, CÔNG, CÔNG SUẤT (Bài 23 -> Bài 27)
    # =========================================================================
    {
        "topic": "nang-luong",
        "title": "Chương IV. Năng lượng, Công, Công suất, Động năng, Thế năng và Định luật bảo toàn cơ năng",
        "icon": "⚡",
        "description": "Tìm hiểu sự truyền và chuyển hóa năng lượng thông qua công cơ học, công suất, động năng, thế năng, định luật bảo toàn cơ năng và hiệu suất của thiết bị.",
        "requirements": [
            r"Trình bày được năng lượng có thể truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác và luôn được bảo toàn; chế tạo hoặc phân tích mô hình minh họa định luật bảo toàn năng lượng.",
            r"Nêu được biểu thức tính công bằng tích của lực tác dụng, độ dịch chuyển và côsin góc hợp bởi hai vectơ đó $A = F \cdot d \cdot \cos\theta$; nêu được đơn vị đo công là jun ($\text{J}$).",
            r"Nêu được ý nghĩa vật lí và định nghĩa công suất là tốc độ thực hiện công $\mathcal{P} = \dfrac{A}{t}$; vận dụng được mối liên hệ giữa công suất với lực và tốc độ $\mathcal{P} = F \cdot v$.",
            r"Rút ra được biểu thức tính động năng $W_{\text{đ}} = \dfrac{1}{2}mv^2$ từ công thức chuyển động thẳng biến đổi đều và định luật 2 Newton; nêu được biểu thức thế năng trọng trường $W_{\text{t}} = mgh$.",
            r"Phân tích được sự chuyển hóa qua lại giữa động năng và thế năng của vật; phát biểu và vận dụng được định luật bảo toàn cơ năng $W = W_{\text{đ}} + W_{\text{t}} = \text{hằng số}$ khi chỉ có lực thế tác dụng.",
            r"Nêu được định nghĩa hiệu suất $H = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\%$ và vận dụng giải được các bài toán thực tế về hiệu suất của động cơ, thiết bị.",
        ],
        "definition": r"""
**Năng lượng** là đại lượng vô hướng đặc trưng cho khả năng sinh công của một vật hoặc hệ vật; năng lượng không tự sinh ra hoặc tự mất đi mà chỉ truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác. **Công cơ học** $A = F \cdot s \cdot \cos\theta$ là số đo phần năng lượng được truyền hoặc chuyển hóa khi có lực tác dụng làm vật dịch chuyển, còn **Công suất** $\mathcal{P} = \dfrac{A}{t}$ đặc trưng cho tốc độ sinh công của lực đó.
""",
        "theory": r"""
### Bài 23. Năng lượng. Công cơ học

- **Các dạng năng lượng và Định luật bảo toàn năng lượng:**
  + Năng lượng tồn tại ở nhiều dạng: cơ năng (động năng, thế năng), nhiệt năng (nội năng), điện năng, quang năng, hóa năng, năng lượng hạt nhân.
  + **Định luật bảo toàn và chuyển hóa năng lượng:** Năng lượng không tự nhiên sinh ra và cũng không tự nhiên mất đi; nó chỉ truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác.
- **Công cơ học ($A$):** Việc truyền năng lượng cho vật bằng cách tác dụng lực lên vật làm vật thay đổi trạng thái chuyển động được gọi là thực hiện công cơ học.
  + Khi lực không đổi $\overrightarrow{F}$ tác dụng lên một vật làm vật dịch chuyển một đoạn $s$ (độ lớn độ dịch chuyển $d$) theo hướng hợp với hướng của lực một góc $\theta$, công của lực $\overrightarrow{F}$ là:
    $$A = F \cdot s \cdot \cos\theta = F \cdot d \cdot \cos\theta$$
  + Đơn vị của công và năng lượng trong hệ SI là jun ($\text{J}$): $1\text{ J} = 1\text{ N}\cdot\text{m}$.
  + **Biện luận dấu của công theo góc $\theta$:**
    - $0^\circ \le \theta < 90^\circ \implies \cos\theta > 0 \implies A > 0$: Lực sinh **công phát động** (ví dụ: công của lực kéo động cơ).
    - $\theta = 90^\circ \implies \cos\theta = 0 \implies A = 0$: Lực vuông góc với hướng dịch chuyển **không sinh công** (ví dụ: phản lực pháp tuyến $\overrightarrow{N}$ khi vật trượt trên mặt phẳng).
    - $90^\circ < \theta \le 180^\circ \implies \cos\theta < 0 \implies A < 0$: Lực sinh **công cản** (ví dụ: công của lực ma sát trượt khi $\theta = 180^\circ$, $A_{\text{ms}} = -F_{\text{ms}} \cdot s$).

### Bài 24. Công suất

- **Khái niệm và công thức:** Công suất là đại lượng đặc trưng cho tốc độ thực hiện công, được xác định bằng công thực hiện được trong một đơn vị thời gian:
  $$\mathcal{P} = \dfrac{A}{t}$$
- **Đơn vị đo công suất:**
  + Đơn vị chuẩn trong hệ SI là oát ($\text{W}$): $1\text{ W} = 1\text{ J/s}$, $1\text{ kW} = 10^3\text{ W}$, $1\text{ MW} = 10^6\text{ W}$.
  + Đơn vị thông dụng trong kĩ thuật: Mã lực (ngựa): $1\text{ HP} \approx 746\text{ W}$ (ở Anh) hoặc $1\text{ CV} \approx 736\text{ W}$ (ở Pháp). Lưu ý: $1\text{ kWh} = 3\,600\,000\text{ J}$ là đơn vị của **công (điện năng)**, không phải đơn vị công suất.
- **Mối liên hệ giữa công suất với lực và tốc độ:** Khi lực $\overrightarrow{F}$ cùng hướng chuyển động ($\theta = 0^\circ$):
  $$\mathcal{P} = \dfrac{A}{t} = \dfrac{F \cdot s}{t} = F \cdot v$$
  Công thức này giải thích nguyên tắc hộp số xe máy, ô tô: Với cùng công suất động cơ $\mathcal{P}$, khi lên dốc cần lực kéo $F$ lớn thì phải đi số thấp để giảm tốc độ $v$.

### Bài 25. Động năng, thế năng

- **Động năng ($W_{\text{đ}}$):** Là dạng năng lượng mà vật có được do nó đang chuyển động:
  $$W_{\text{đ}} = \dfrac{1}{2}mv^2$$
  + **Định lí động năng:** Độ biến thiên động năng của một vật bằng tổng công của các ngoại lực tác dụng lên vật trong quá trình đó:
    $$W_{\text{đ2}} - W_{\text{đ1}} = \dfrac{1}{2}mv_2^2 - \dfrac{1}{2}mv_1^2 = A_{\text{ngoại lực}}$$
- **Thế năng trọng trường ($W_{\text{t}}$):** Là dạng năng lượng tương tác giữa Trái Đất và vật, phụ thuộc vào vị trí của vật trong trọng trường. Chọn mốc thế năng ($W_{\text{t}} = 0$) tại mặt đất thì ở độ cao $h$ so với mốc thế năng:
  $$W_{\text{t}} = P \cdot h = mgh$$
  + Giá trị của thế năng phụ thuộc vào việc chọn mốc thế năng ($h > 0 \implies W_{\text{t}} > 0$; $h < 0 \implies W_{\text{t}} < 0$), nhưng hiệu thế năng giữa hai vị trí thì không phụ thuộc mốc thế năng và bằng công của trọng lực: $A_{12} = W_{\text{t1}} - W_{\text{t2}} = mg(h_1 - h_2)$ (công của trọng lực không phụ thuộc hình dạng đường đi).

### Bài 26. Cơ năng và định luật bảo toàn cơ năng

- **Cơ năng ($W$):** Là tổng động năng và thế năng của vật:
  $$W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}mv^2 + mgh$$
- **Sự chuyển hóa giữa động năng và thế năng:** Trong quá trình vật chuyển động (ví dụ: quả bóng rơi, con lắc đơn dao động, vận động viên trượt ván), động năng và thế năng có thể chuyển hóa qua lại lẫn nhau: khi độ cao giảm thì thế năng giảm và động năng tăng; khi độ cao tăng thì thế năng tăng và động năng giảm.
- **Định luật bảo toàn cơ năng:** Khi một vật chuyển động trong trọng trường **chỉ chịu tác dụng của trọng lực** (bỏ qua ma sát và lực cản môi trường, hoặc các lực khác không sinh công), thì cơ năng của vật là một đại lượng bảo toàn:
  $$W_1 = W_2 \iff \dfrac{1}{2}mv_1^2 + mgh_1 = \dfrac{1}{2}mv_2^2 + mgh_2 = \text{hằng số}$$
- **Khi có lực cản, lực ma sát sinh công $A_{\text{cản}}$:** Cơ năng không bảo toàn, độ biến thiên cơ năng bằng công của lực cản (lực không thế): $\Delta W = W_2 - W_1 = A_{\text{cản}}$.

### Bài 27. Hiệu suất

- **Năng lượng có ích và năng lượng hao phí:** Trong mọi máy móc, động cơ, năng lượng toàn phần $W_{\text{tp}}$ cung cấp cho máy luôn bằng tổng năng lượng có ích $W_{\text{ích}}$ và năng lượng hao phí $W_{\text{hp}}$ (thường tỏa nhiệt do ma sát):
  $$W_{\text{tp}} = W_{\text{ích}} + W_{\text{hp}}$$
- **Hiệu suất ($H$):** Là tỉ số giữa năng lượng có ích (hoặc công có ích, công suất có ích) và năng lượng toàn phần (hoặc công toàn phần, công suất toàn phần):
  $$H = \dfrac{W_{\text{ích}}}{W_{\text{tp}}} \cdot 100\% = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\% = \dfrac{\mathcal{P}_{\text{ích}}}{\mathcal{P}_{\text{tp}}} \cdot 100\%$$
  Vì luôn có năng lượng hao phí ($W_{\text{hp}} > 0$) nên hiệu suất của các động cơ thực tế luôn nhỏ hơn $100\%$ ($H < 100\%$).
""",
        "formulas": [
            G(
                "Công cơ học và Công suất",
                F(
                    "Công của lực không đổi",
                    r"$A = F \cdot s \cdot \cos\theta = F \cdot d \cdot \cos\theta$",
                    r"$\theta = (\overrightarrow{F}, \overrightarrow{d})$; đơn vị là jun ($\text{J}$)",
                ),
                F(
                    "Công suất trung bình và tức thời",
                    r"$\mathcal{P} = \dfrac{A}{t} = F \cdot v$",
                    r"Đơn vị chuẩn SI là oát ($\text{W}$), với $1\text{ W} = 1\text{ J/s}$",
                ),
            ),
            G(
                "Động năng, Thế năng và Định luật bảo toàn cơ năng",
                F(
                    "Động năng và Định lí động năng",
                    r"$W_{\text{đ}} = \dfrac{1}{2}mv^2 \quad ; \quad \Delta W_{\text{đ}} = W_{\text{đ2}} - W_{\text{đ1}} = A$",
                    r"$m$ tính bằng $\text{kg}$, $v$ tính bằng $\text{m/s}$, $W_{\text{đ}}$ tính bằng $\text{J}$",
                ),
                F(
                    "Thế năng trọng trường",
                    r"$W_{\text{t}} = mgh$",
                    r"$h$ là độ cao của vật so với mốc thế năng đã chọn ($\text{m}$)",
                ),
                F(
                    "Cơ năng trong trọng trường",
                    r"$W = W_{\text{đ}} + W_{\text{t}} = \dfrac{1}{2}mv^2 + mgh$",
                    r"Khi chỉ có trọng lực sinh công: $W_1 = W_2 = \text{hằng số}$",
                ),
                F(
                    "Độ biến thiên cơ năng khi có lực cản",
                    r"$W_2 - W_1 = A_{\text{cản}} = -F_{\text{cản}} \cdot s$",
                    r"Phần cơ năng giảm đi chuyển hóa thành nhiệt năng do ma sát",
                ),
            ),
            G(
                "Hiệu suất của thiết bị và động cơ",
                F(
                    "Công thức tính hiệu suất",
                    r"$H = \dfrac{W_{\text{ích}}}{W_{\text{tp}}} \cdot 100\% = \dfrac{A_{\text{ích}}}{A_{\text{tp}}} \cdot 100\% = \dfrac{\mathcal{P}_{\text{ích}}}{\mathcal{P}_{\text{tp}}} \cdot 100\%$",
                    r"Với $W_{\text{tp}} = W_{\text{ích}} + W_{\text{hp}}$ và luôn có $H < 100\%$",
                ),
            ),
        ],
        "example": r"""
Một vật nhỏ có khối lượng $m = 0,5\text{ kg}$ được ném thẳng đứng lên cao với tốc độ ban đầu $v_0 = 10\text{ m/s}$ từ độ cao $h_0 = 4\text{ m}$ so với mặt đất. Chọn mốc thế năng tại mặt đất, lấy $g = 10\text{ m/s}^2$ và bỏ qua sức cản của không khí.
1. Tính động năng, thế năng và cơ năng của vật tại vị trí ném.
2. Tìm độ cao cực đại $h_{\max}$ mà vật đạt được so với mặt đất và tốc độ của vật khi vừa chạm đất.
3. Khi chạm đất, vật lún sâu vào đất một đoạn $s = 5\text{ cm}$ rồi dừng hẳn. Tính lực cản trung bình của đất tác dụng lên vật (tính cả công của trọng lực trên đoạn lún $s$).
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. **Tại vị trí ném ($h_0 = 4\text{ m}, v_0 = 10\text{ m/s}$):**
   - Động năng ban đầu của vật:
     $$W_{\text{đ0}} = \dfrac{1}{2}mv_0^2 = \dfrac{1}{2} \cdot 0,5 \cdot 10^2 = 25\text{ J}$$
   - Thế năng ban đầu của vật (so với mặt đất):
     $$W_{\text{t0}} = mgh_0 = 0,5 \cdot 10 \cdot 4 = 20\text{ J}$$
   - Cơ năng của vật tại vị trí ném:
     $$W = W_{\text{đ0}} + W_{\text{t0}} = 25 + 20 = 45\text{ J}$$
2. **Bảo toàn cơ năng khi bỏ qua sức cản không khí ($W = 45\text{ J}$):**
   - Tại độ cao cực đại $h_{\max}$, vận tốc của vật bằng $0$ ($W_{\text{đ}} = 0$) nên toàn bộ cơ năng chuyển thành thế năng:
     $$W = mgh_{\max} \implies h_{\max} = \dfrac{W}{mg} = \dfrac{45}{0,5 \cdot 10} = 9\text{ m}$$
   - Ngay khi chạm đất ($h = 0 \implies W_{\text{t}} = 0$), toàn bộ cơ năng chuyển thành động năng:
     $$W = \dfrac{1}{2}mv_{\text{đất}}^2 \implies v_{\text{đất}} = \sqrt{\dfrac{2W}{m}} = \sqrt{\dfrac{2 \cdot 45}{0,5}} = \sqrt{180} = 6\sqrt{5} \approx 13,42\text{ m/s}$$
3. **Trong giai đoạn lún sâu $s = 5\text{ cm} = 0,05\text{ m}$ vào đất đến khi dừng hẳn ($v_2 = 0$):**
   Áp dụng định lí biến thiên động năng từ lúc chạm đất ($W_{\text{đ1}} = 45\text{ J}$) đến khi dừng hẳn ở độ sâu $s$ ($W_{\text{đ2}} = 0$):
   $$W_{\text{đ2}} - W_{\text{đ1}} = A_{\text{P}} + A_{\text{cản}} \iff 0 - 45 = mg \cdot s - F_{\text{cản}} \cdot s$$
   $$F_{\text{cản}} = \dfrac{45 + 0,5 \cdot 10 \cdot 0,05}{0,05} = \dfrac{45,25}{0,05} = 905\text{ N}$$
   (Nếu bỏ qua công trọng lực trên đoạn lún rất ngắn thì $F_{\text{cản}} = \dfrac{45}{0,05} = 900\text{ N}$).
""",
        "real_life": r"""
Nhà máy thủy điện (như Thủy điện Hòa Bình, Sơn La) và trò chơi tàu lượn siêu tốc (Roller Coaster) là những minh họa sống động của **sự chuyển hóa giữa thế năng trọng trường và động năng**: nước tích trữ ở hồ chứa trên cao có thế năng khổng lồ $W_{\text{t}} = mgh$, khi đổ qua đường ống áp lực sẽ chuyển hóa thành động năng làm quay tua-bin máy phát điện. Trong lĩnh vực ô tô điện và tấm pin mặt trời, việc nâng cao **hiệu suất** $H$ từ $20\%$ lên trên $85\%$ giúp tiết kiệm hàng tỉ $\text{kWh}$ năng lượng mỗi năm.
""",
        "game_title": "Kĩ Sư Đường Ray Tàu Lượn: Bảo Toàn Cơ Năng & Hiệu Suất",
        "game_description": "Thiết kế độ cao các đỉnh dốc tàu lượn siêu tốc, theo dõi thanh biểu đồ Động năng – Thế năng – Cơ năng theo thời gian thực.",
        "game_type": "game_nang_luong",
        "quiz": [
            mcq(
                "biet",
                r"Một lực không đổi $\overrightarrow{F}$ tác dụng lên một vật làm vật dịch chuyển một đoạn $s$ theo hướng hợp với hướng của lực một góc $\theta$. Công $A$ của lực $\overrightarrow{F}$ được tính bằng công thức nào?",
                [
                    r"$A = F \cdot s \cdot \cos\theta$",
                    r"$A = F \cdot s \cdot \sin\theta$",
                    r"$A = F \cdot s \cdot \tan\theta$",
                    r"$A = \dfrac{F \cdot s}{\cos\theta}$",
                ],
                0,
                r"Theo Bài 23 SGK Vật lí 10 KNTT, công của lực không đổi được xác định bởi biểu thức $A = F \cdot s \cdot \cos\theta$.",
            ),
            mcq(
                "biet",
                r"Đơn vị nào sau đây **không phải** là đơn vị của công suất?",
                [
                    r"Oát ($\text{W}$).",
                    r"Jun trên giây ($\text{J/s}$).",
                    r"Kilôoát giờ ($\text{kWh}$).",
                    r"Mã lực ($\text{HP}$).",
                ],
                2,
                r"Theo Bài 24 SGK Vật lí 10 KNTT, $\text{kWh}$ là đơn vị của công (điện năng tiêu thụ, $1\text{ kWh} = 3,6 \cdot 10^6\text{ J}$), không phải đơn vị của công suất.",
            ),
            mcq(
                "biet",
                r"Một vật có khối lượng $m$ đang chuyển động với tốc độ $v$ thì động năng $W_{\text{đ}}$ của vật được xác định bởi biểu thức:",
                [
                    r"$W_{\text{đ}} = \dfrac{1}{2}mv^2$",
                    r"$W_{\text{đ}} = mv^2$",
                    r"$W_{\text{đ}} = \dfrac{1}{2}m^2v$",
                    r"$W_{\text{đ}} = mv$",
                ],
                0,
                r"Theo Bài 25 SGK Vật lí 10 KNTT, động năng của vật khối lượng $m$ chuyển động với tốc độ $v$ là $W_{\text{đ}} = \dfrac{1}{2}mv^2$.",
            ),
            mcq(
                "biet",
                r"Khi một vật được ném thẳng đứng từ dưới lên cao trong trọng trường (bỏ qua sức cản của không khí), trong quá trình vật đi lên thì:",
                [
                    r"Động năng tăng, thế năng giảm, cơ năng không đổi.",
                    r"Động năng giảm, thế năng tăng, cơ năng không đổi.",
                    r"Cả động năng và thế năng đều tăng.",
                    r"Động năng giảm, thế năng tăng, cơ năng giảm dần về $0$.",
                ],
                1,
                r"Theo Bài 26 SGK Vật lí 10 KNTT, khi vật đi lên cao thì độ cao $h$ tăng nên thế năng tăng, tốc độ $v$ giảm nên động năng giảm, nhưng tổng cơ năng $W = W_{\text{đ}} + W_{\text{t}}$ được bảo toàn.",
            ),
            mcq(
                "hieu",
                r"Một người kéo một thùng hàng trượt trên sàn nhà nằm ngang một đoạn $s = 10\text{ m}$ bằng một sợi dây có lực căng không đổi $F = 80\text{ N}$ hợp với phương ngang một góc $\theta = 60^\circ$. Công của lực kéo này thực hiện trên đoạn đường đó là:",
                [
                    r"$800\text{ J}$",
                    r"$400\text{ J}$",
                    r"$400\sqrt{3}\text{ J}$",
                    r"$200\text{ J}$",
                ],
                1,
                r"Áp dụng công thức tính công: $A = F \cdot s \cdot \cos 60^\circ = 80 \cdot 10 \cdot 0,5 = 400\text{ J}$.",
            ),
            mcq(
                "hieu",
                r"Một động cơ điện có công suất tiêu thụ toàn phần là $\mathcal{P}_{\text{tp}} = 2,0\text{ kW}$ dùng để nâng đều một kiện hàng nặng $m = 160\text{ kg}$ lên cao $h = 10\text{ m}$ trong thời gian $t = 10\text{ s}$. Lấy $g = 10\text{ m/s}^2$. Hiệu suất của động cơ điện này là:",
                [
                    r"$60\%$",
                    r"$75\%$",
                    r"$80\%$",
                    r"$85\%$",
                ],
                2,
                r"Công có ích để nâng đều kiện hàng là $A_{\text{ích}} = P \cdot h = mgh = 160 \cdot 10 \cdot 10 = 16\,000\text{ J}$. Công suất có ích là $\mathcal{P}_{\text{ích}} = \dfrac{A_{\text{ích}}}{t} = \dfrac{16\,000}{10} = 1600\text{ W}$. Hiệu suất của động cơ là $H = \dfrac{\mathcal{P}_{\text{ích}}}{\mathcal{P}_{\text{tp}}} \cdot 100\% = \dfrac{1600}{2000} \cdot 100\% = 80\%$.",
            ),
            tf4(
                "hieu",
                r"Một quả cầu nhỏ có khối lượng $m = 0,2\text{ kg}$ được thả rơi tự do không vận tốc đầu từ độ cao $h_A = 10\text{ m}$ so với mặt đất tại nơi có $g = 10\text{ m/s}^2$. Chọn mốc thế năng tại mặt đất và bỏ qua sức cản của không khí.",
                [
                    r"Tại vị trí thả $A$, thế năng của quả cầu là $20\text{ J}$ và động năng bằng $0\text{ J}$.",
                    r"Cơ năng của quả cầu trong suốt quá trình rơi luôn không đổi và bằng $20\text{ J}$.",
                    r"Khi quả cầu rơi đến vị trí $B$ có độ cao $h_B = 5\text{ m}$ thì động năng của quả cầu bằng thế năng của nó ($W_{\text{đ}B} = W_{\text{t}B} = 10\text{ J}$).",
                    r"Tốc độ của quả cầu ngay trước khi chạm đất là $v = 20\text{ m/s}$.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** $W_{\text{t}A} = mgh_A = 0,2 \cdot 10 \cdot 10 = 20\text{ J}$; $v_A = 0 \implies W_{\text{đ}A} = 0\text{ J}$.
- **b) Đúng:** Bỏ qua sức cản không khí nên cơ năng bảo toàn: $W = W_A = 20\text{ J}$.
- **c) Đúng:** Tại $h_B = 5\text{ m} = \dfrac{1}{2}h_A$, thế năng $W_{\text{t}B} = 10\text{ J}$, suy ra động năng $W_{\text{đ}B} = W - W_{\text{t}B} = 20 - 10 = 10\text{ J}$.
- **d) Sai:** Ngay khi chạm đất: $\dfrac{1}{2}mv^2 = mgh_A \implies v = \sqrt{2gh_A} = \sqrt{2 \cdot 10 \cdot 10} = \sqrt{200} = 10\sqrt{2} \approx 14,14\text{ m/s} \neq 20\text{ m/s}$.""",
            ),
            tf4(
                "hieu",
                r"Một ô tô có khối lượng $m = 1,5\text{ tấn} = 1500\text{ kg}$ chuyển động thẳng đều trên đường nằm ngang với tốc độ $v = 72\text{ km/h} = 20\text{ m/s}$. Biết lực cản tổng cộng tác dụng lên ô tô có độ lớn bằng $2000\text{ N}$.",
                [
                    r"Động năng của ô tô khi đang chạy với tốc độ $20\text{ m/s}$ là $W_{\text{đ}} = 300\text{ kJ}$.",
                    r"Vì ô tô chuyển động thẳng đều nên lực kéo của động cơ có độ lớn bằng độ lớn lực cản: $F_{\text{k}} = 2000\text{ N}$.",
                    r"Công suất của lực kéo động cơ ô tô khi đó là $\mathcal{P} = F_{\text{k}} \cdot v = 40\text{ kW}$.",
                    r"Trọng lực tác dụng lên ô tô sinh công dương giúp duy trì tốc độ của xe trên đường nằm ngang.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** $W_{\text{đ}} = \dfrac{1}{2}mv^2 = \dfrac{1}{2} \cdot 1500 \cdot 20^2 = 300\,000\text{ J} = 300\text{ kJ}$.
- **b) Đúng:** Xe chuyển động thẳng đều nên $F_{\text{k}} = F_{\text{cản}} = 2000\text{ N}$.
- **c) Đúng:** $\mathcal{P} = F_{\text{k}} \cdot v = 2000 \cdot 20 = 40\,000\text{ W} = 40\text{ kW}$.
- **d) Sai:** Trên đường nằm ngang, trọng lực vuông góc với hướng dịch chuyển ($\theta = 90^\circ$) nên công của trọng lực bằng $0$.""",
            ),
            mcq(
                "vandung",
                r"Một con lắc đơn gồm quả cầu nhỏ khối lượng $m$ treo vào sợi dây nhẹ không dãn dài $l = 1,0\text{ m}$ tại nơi có $g = 10\text{ m/s}^2$. Kéo quả cầu lệch khỏi vị trí cân bằng để dây treo hợp với phương thẳng đứng góc $\alpha_0 = 60^\circ$ rồi thả nhẹ. Bỏ qua sức cản không khí. Tốc độ của quả cầu khi đi qua vị trí cân bằng (vị trí thấp nhất) là:",
                [
                    r"$\sqrt{10}\text{ m/s}$",
                    r"$2\sqrt{5}\text{ m/s}$",
                    r"$5\text{ m/s}$",
                    r"$10\text{ m/s}$",
                ],
                0,
                r"""Chọn mốc thế năng tại vị trí thấp nhất (vị trí cân bằng). Khi dây lệch góc $\alpha_0 = 60^\circ$, độ cao của quả cầu so với vị trí thấp nhất là:
$$h_0 = l(1 - \cos 60^\circ) = 1,0 \cdot (1 - 0,5) = 0,5\text{ m}$$
Áp dụng định luật bảo toàn cơ năng từ vị trí thả ($v_0 = 0$) đến vị trí cân bằng ($h = 0$):
$$mgh_0 = \dfrac{1}{2}mv_{\max}^2 \implies v_{\max} = \sqrt{2gh_0} = \sqrt{2 \cdot 10 \cdot 0,5} = \sqrt{10}\text{ m/s}$$""",
            ),
            short(
                "vandung",
                r"Một viên đạn có khối lượng $m = 20\text{ g} = 0,02\text{ kg}$ bay ngang với tốc độ $v_1 = 400\text{ m/s}$ xuyên qua một tấm gỗ dày $d = 10\text{ cm} = 0,1\text{ m}$. Sau khi xuyên qua tấm gỗ, tốc độ của viên đạn giảm xuống còn $v_2 = 100\text{ m/s}$. Tính độ lớn lực cản trung bình của tấm gỗ tác dụng lên viên đạn theo đơn vị kilôniutơn ($\text{kN}$), chỉ ghi phần số.",
                ["15", "15,0", "15.0"],
                r"""Áp dụng định lí biến thiên động năng cho viên đạn:
$$\dfrac{1}{2}mv_2^2 - \dfrac{1}{2}mv_1^2 = A_{\text{cản}} = -F_{\text{cản}} \cdot d$$
Thay số:
$$F_{\text{cản}} = \dfrac{m(v_1^2 - v_2^2)}{2d} = \dfrac{0,02 \cdot (400^2 - 100^2)}{2 \cdot 0,1} = 0,1 \cdot (160\,000 - 10\,000) = 15\,000\text{ N} = 15\text{ kN}$$""",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG V. ĐỘNG LƯỢNG (Bài 28 -> Bài 30)
    # =========================================================================
    {
        "topic": "dong-luong",
        "title": "Chương V. Động lượng: Xung lượng của lực, Định luật bảo toàn động lượng và Bài toán va chạm",
        "icon": "🎱",
        "description": "Nghiên cứu đại lượng động lượng, mối liên hệ giữa xung lượng của lực và độ biến thiên động lượng, định luật bảo toàn động lượng trong hệ kín và các loại va chạm.",
        "requirements": [
            r"Từ tình huống thực tế, thảo luận để nêu được ý nghĩa vật lí và định nghĩa động lượng $\overrightarrow{p} = m\overrightarrow{v}$, nêu được đơn vị của động lượng là $\text{kg}\cdot\text{m/s}$ (hoặc $\text{N}\cdot\text{s}$).",
            r"Rút ra được mối liên hệ giữa hợp lực tác dụng lên vật và tốc độ thay đổi của động lượng $\overrightarrow{F} = \dfrac{\Delta \overrightarrow{p}}{\Delta t}$ (dạng tổng quát của Định luật 2 Newton) và công thức xung lượng của lực $\overrightarrow{F}\Delta t = \Delta \overrightarrow{p}$.",
            r"Thực hiện thí nghiệm và thảo luận, phát biểu được định luật bảo toàn động lượng trong hệ kín $\overrightarrow{p}_1 + \overrightarrow{p}_2 = \overrightarrow{p}_1' + \overrightarrow{p}_2'$.",
            r"Vận dụng được định luật bảo toàn động lượng để giải các bài toán va chạm đàn hồi, va chạm mềm và chuyển động bằng phản lực trong một số trường hợp đơn giản.",
            r"Thực hiện phương án thực hành xác định tốc độ và đánh giá được động lượng của hai xe lăn trước và sau va chạm trên đệm không khí hoặc máng ngang.",
        ],
        "definition": r"""
**Động lượng** $\overrightarrow{p} = m\overrightarrow{v}$ là đại lượng vectơ đặc trưng cho khả năng truyền chuyển động của một vật khi tương tác với các vật khác, bằng tích của khối lượng $m$ và vectơ vận tốc $\overrightarrow{v}$ của vật. Trong một **hệ kín** (hệ cô lập không có ngoại lực hoặc tổng ngoại lực triệt tiêu), **tổng động lượng của hệ luôn được bảo toàn** trước và sau mọi quá trình tương tác: $\sum \overrightarrow{p}_{\text{trước}} = \sum \overrightarrow{p}_{\text{sau}}$.
""",
        "theory": r"""
### Bài 28. Động lượng

- **Định nghĩa động lượng:** Động lượng $\overrightarrow{p}$ của một vật khối lượng $m$ đang chuyển động với vận tốc $\overrightarrow{v}$ là đại lượng được xác định bởi công thức:
  $$\overrightarrow{p} = m\overrightarrow{v}$$
  + Vì $m > 0$ nên vectơ động lượng $\overrightarrow{p}$ luôn **cùng hướng với vectơ vận tốc** $\overrightarrow{v}$.
  + Độ lớn: $p = m \cdot v$. Đơn vị của động lượng trong hệ SI là $\text{kg}\cdot\text{m/s}$ (tương đương với $\text{N}\cdot\text{s}$).
  + Mối liên hệ giữa độ lớn động lượng $p$ và động năng $W_{\text{đ}}$ của cùng một vật:
    $$W_{\text{đ}} = \dfrac{1}{2}mv^2 = \dfrac{p^2}{2m} \iff p = \sqrt{2m W_{\text{đ}}}$$
- **Động lượng của một hệ nhiều vật:** Bằng tổng vectơ động lượng của các vật trong hệ: $\overrightarrow{p} = \overrightarrow{p}_1 + \overrightarrow{p}_2 + \dots$.
- **Xung lượng của lực và Định luật 2 Newton dạng tổng quát:**
  + Khi một lực $\overrightarrow{F}$ (không đổi hoặc trung bình) tác dụng lên một vật trong khoảng thời gian ngắn $\Delta t$ thì tích $\overrightarrow{F}\Delta t$ được gọi là **xung lượng của lực** trong khoảng thời gian $\Delta t$ ấy.
  + Biến đổi từ Định luật 2 Newton: $\overrightarrow{F} = m\overrightarrow{a} = m\dfrac{\overrightarrow{v}_2 - \overrightarrow{v}_1}{\Delta t} = \dfrac{m\overrightarrow{v}_2 - m\overrightarrow{v}_1}{\Delta t} = \dfrac{\Delta \overrightarrow{p}}{\Delta t}$.
  + Suy ra **Định lí biến thiên động lượng**: Độ biến thiên động lượng của một vật trong một khoảng thời gian $\Delta t$ bằng xung lượng của tổng các lực tác dụng lên vật trong khoảng thời gian đó:
    $$\Delta \overrightarrow{p} = \overrightarrow{p}_2 - \overrightarrow{p}_1 = \overrightarrow{F}\Delta t$$
  + Ý nghĩa thực tiễn: Cùng một độ biến thiên động lượng $\Delta \overrightarrow{p}$ (ví dụ khi dừng xe hoặc khi tiếp đất), nếu kéo dài thời gian va chạm $\Delta t$ (nhờ đệm mút, túi khí, vùng hấp thụ xung lực, khuỵu chân khi nhảy xuống đất) thì lực va chạm $F = \dfrac{|\Delta p|}{\Delta t}$ tác dụng lên cơ thể sẽ giảm đi rất nhiều, tránh gây chấn thương.

### Bài 29. Định luật bảo toàn động lượng

- **Hệ kín (Hệ cô lập):**
  + Là hệ gồm các vật chỉ tương tác với nhau (nội lực) mà không tương tác với các vật ngoài hệ, hoặc nếu có chịu tác dụng của ngoại lực thì các ngoại lực ấy cân bằng nhau ($\sum \overrightarrow{F}_{\text{ngoại}} = \overrightarrow{0}$).
  + Trong các hiện tượng nổ, bắn súng hoặc va chạm diễn ra trong thời gian rất ngắn $\Delta t \to 0$, nội lực tương tác giữa các vật rất lớn so với ngoại lực (như trọng lực, ma sát) nên hệ được coi gần đúng là hệ kín trong suốt thời gian tương tác.
  + Nếu tổng ngoại lực chỉ bằng $0$ theo một phương xác định (ví dụ phương ngang $Ox$), thì hình chiếu tổng động lượng của hệ trên phương đó được bảo toàn.
- **Định luật bảo toàn động lượng:** Động lượng toàn phần của một hệ kín là một đại lượng bảo toàn:
  $$\overrightarrow{p}_1 + \overrightarrow{p}_2 = \overrightarrow{p}_1' + \overrightarrow{p}_2' \iff m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2 = m_1\overrightarrow{v}_1' + m_2\overrightarrow{v}_2'$$
- **Ứng dụng 1 – Hai loại va chạm cơ bản:**
  1. **Va chạm mềm (Va chạm hoàn toàn không đàn hồi):** Sau va chạm, hai vật dính vào nhau và chuyển động với cùng một vận tốc $\overrightarrow{v}'$:
     $$m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2 = (m_1 + m_2)\overrightarrow{v}' \implies \overrightarrow{v}' = \dfrac{m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2}{m_1 + m_2}$$
     Trong va chạm mềm, động lượng của hệ được bảo toàn nhưng **động năng không bảo toàn** (một phần cơ năng chuyển hóa thành nội năng và nhiệt năng làm biến dạng vật).
  2. **Va chạm đàn hồi:** Sau va chạm, hai vật tách rời nhau và không để lại biến dạng; cả **động lượng** lẫn **động năng** của hệ đều được bảo toàn:
     $$\begin{cases} m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2 = m_1\overrightarrow{v}_1' + m_2\overrightarrow{v}_2' \\ \dfrac{1}{2}m_1 v_1^2 + \dfrac{1}{2}m_2 v_2^2 = \dfrac{1}{2}m_1 {v_1'}^2 + \dfrac{1}{2}m_2 {v_2'}^2 \end{cases}$$
- **Ứng dụng 2 – Chuyển động bằng phản lực (Súng giật, tên lửa):**
  + Xét hệ đứng yên ban đầu ($\overrightarrow{p}_{\text{trước}} = \overrightarrow{0}$), khi một phần khối lượng $m$ phụt ra với vận tốc $\overrightarrow{v}$ thì phần còn lại khối lượng $M$ chuyển động giật lùi theo hướng ngược lại với vận tốc $\overrightarrow{V}$:
    $$m\overrightarrow{v} + M\overrightarrow{V} = \overrightarrow{0} \implies \overrightarrow{V} = -\dfrac{m}{M}\overrightarrow{v}$$

### Bài 30. Thực hành: Xác định động lượng của vật trước và sau va chạm

- **Dụng cụ:** Băng đệm khí nằm ngang (để khử ma sát), hai xe trượt gắn tấm chắn sáng, băng nhám dính (cho thí nghiệm va chạm mềm) hoặc lò xo cản (cho thí nghiệm va chạm đàn hồi), hai cổng quang điện nối với đồng hồ đo thời gian hiện số, cân điện tử.
- **Tiến trình:** Đo khối lượng $m_1, m_2$; đo thời gian tấm chắn sáng đi qua hai cổng quang điện trước và sau va chạm để suy ra $v_1, v_2, v_1', v_2'$ (nhớ quy ước dấu theo chiều dương), từ đó so sánh $p_{\text{trước}} = m_1 v_1 + m_2 v_2$ và $p_{\text{sau}} = m_1 v_1' + m_2 v_2'$.
""",
        "formulas": [
            G(
                "Động lượng và Xung lượng của lực",
                F(
                    "Vectơ động lượng và độ lớn",
                    r"$\overrightarrow{p} = m\overrightarrow{v} \quad ; \quad p = mv$",
                    r"Đơn vị chuẩn SI: $\text{kg}\cdot\text{m/s}$ (hoặc $\text{N}\cdot\text{s}$)",
                ),
                F(
                    "Liên hệ giữa động lượng và động năng",
                    r"$p = \sqrt{2m W_{\text{đ}}} \iff W_{\text{đ}} = \dfrac{p^2}{2m}$",
                    r"$W_{\text{đ}}$ là động năng ($\text{J}$), $m$ là khối lượng ($\text{kg}$)",
                ),
                F(
                    "Tổng hợp động lượng của hai vật",
                    r"$p = \sqrt{p_1^2 + p_2^2 + 2p_1 p_2 \cos\alpha}$",
                    r"$\alpha = (\overrightarrow{p}_1, \overrightarrow{p}_2)$; khi $\overrightarrow{p}_1 \perp \overrightarrow{p}_2$ thì $p = \sqrt{p_1^2 + p_2^2}$",
                ),
                F(
                    "Định lí biến thiên động lượng & Xung lượng",
                    r"$\Delta \overrightarrow{p} = \overrightarrow{p}_2 - \overrightarrow{p}_1 = \overrightarrow{F}\Delta t \iff \overrightarrow{F} = \dfrac{\Delta \overrightarrow{p}}{\Delta t}$",
                    r"$\overrightarrow{F}\Delta t$ là xung lượng của hợp lực trong thời gian $\Delta t$",
                ),
            ),
            G(
                "Định luật bảo toàn động lượng và Va chạm",
                F(
                    "Bảo toàn động lượng trong hệ kín",
                    r"$m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2 = m_1\overrightarrow{v}_1' + m_2\overrightarrow{v}_2'$",
                    r"Khi chiếu lên trục tọa độ, phải kèm dấu đại số của các vận tốc",
                ),
                F(
                    "Va chạm mềm (hai vật dính vào nhau)",
                    r"$\overrightarrow{v}' = \dfrac{m_1\overrightarrow{v}_1 + m_2\overrightarrow{v}_2}{m_1 + m_2}$",
                    r"Phần cơ năng tiêu hao thành nhiệt: $\Delta W = W_{\text{đ trước}} - W_{\text{đ sau}} > 0$",
                ),
                F(
                    "Chuyển động bằng phản lực (hệ đứng yên ban đầu)",
                    r"$M\overrightarrow{V} + m\overrightarrow{v} = \overrightarrow{0} \implies \overrightarrow{V} = -\dfrac{m}{M}\overrightarrow{v}$",
                    r"$\overrightarrow{V}$ ngược hướng với $\overrightarrow{v}$ và tỉ lệ nghịch với khối lượng",
                ),
            ),
        ],
        "example": r"""
Một quả bóng khối lượng $m = 0,4\text{ kg}$ đang bay theo phương nằm ngang với tốc độ $v_1 = 15\text{ m/s}$ thì đập vuông góc vào một bức tường thẳng đứng rồi bật ngược trở lại theo đúng phương cũ với tốc độ $v_2 = 10\text{ m/s}$. Thời gian quả bóng tiếp xúc với tường là $\Delta t = 0,05\text{ s}$. Chọn trục tọa độ $Ox$ nằm ngang, chiều dương là chiều bóng bật ra khỏi tường.
1. Tính động lượng của quả bóng ngay trước khi đập vào tường, ngay sau khi bật ra và độ biến thiên động lượng $\Delta p$ của quả bóng.
2. Tính độ lớn lực trung bình của bức tường tác dụng lên quả bóng trong thời gian va chạm.
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. Chọn chiều dương của trục $Ox$ là chiều quả bóng bật ngược ra khỏi tường:
   - Trước khi đập vào tường, quả bóng bay ngược chiều dương nên vận tốc đại số là $v_{1x} = -15\text{ m/s}$. Động lượng của quả bóng ngay trước va chạm là:
     $$p_1 = m v_{1x} = 0,4 \cdot (-15) = -6,0\text{ kg}\cdot\text{m/s}$$
   - Ngay sau khi bật ra khỏi tường, quả bóng bay theo chiều dương nên vận tốc đại số là $v_{2x} = +10\text{ m/s}$. Động lượng của quả bóng ngay sau va chạm là:
     $$p_2 = m v_{2x} = 0,4 \cdot 10 = +4,0\text{ kg}\cdot\text{m/s}$$
   - Độ biến thiên động lượng của quả bóng trên trục $Ox$ là:
     $$\Delta p = p_2 - p_1 = 4,0 - (-6,0) = +10,0\text{ kg}\cdot\text{m/s}$$
     (Lưu ý sai lầm thường gặp là không lấy dấu âm của $p_1$ mà tính $4,0 - 6,0 = -2,0\text{ kg}\cdot\text{m/s}$).
2. Áp dụng định lí biến thiên động lượng $\Delta p = F \cdot \Delta t$, lực trung bình của tường tác dụng lên quả bóng có giá trị đại số và độ lớn là:
   $$F = \dfrac{\Delta p}{\Delta t} = \dfrac{10,0}{0,05} = 200\text{ N}$$
   Lực $\overrightarrow{F}$ hướng theo chiều dương (vuông góc với tường và hướng ra ngoài).
""",
        "real_life": r"""
Trong thiết kế an toàn ô tô hiện đại, phần đầu và đuôi xe được chế tạo có **vùng hấp thụ xung lực (crumple zone)** dễ biến dạng khi đâm va nhằm kéo dài thời gian va chạm $\Delta t$ từ vài phần nghìn giây lên vài phần mười giây; theo hệ thức $F = \dfrac{|\Delta p|}{\Delta t}$, điều này làm giảm hàng chục lần lực xung kích tác dụng lên khoang hành khách. Ngoài ra, môn thể thao bi-a (bida), nguyên lí giật lùi của pháo binh và chuyển động của loài mực ống, sứa biển bằng cách phụt nước về phía sau đều tuân theo **Định luật bảo toàn động lượng**.
""",
        "game_title": "Bàn Bi-a Vật Lí & Phòng Thí Nghiệm Đệm Không Khí",
        "game_description": "Mô phỏng va chạm đàn hồi và va chạm mềm giữa hai xe trượt trên đệm khí, kiểm nghiệm sự bảo toàn vectơ động lượng.",
        "game_type": "game_dong_luong",
        "quiz": [
            mcq(
                "biet",
                r"Động lượng $\overrightarrow{p}$ của một vật khối lượng $m$ đang chuyển động với vận tốc $\overrightarrow{v}$ được xác định bởi biểu thức:",
                [
                    r"$\overrightarrow{p} = m\overrightarrow{v}$",
                    r"$p = \dfrac{1}{2}mv^2$",
                    r"$\overrightarrow{p} = m\overrightarrow{a}$",
                    r"$\overrightarrow{p} = \dfrac{\overrightarrow{v}}{m}$",
                ],
                0,
                r"Theo Bài 28 SGK Vật lí 10 KNTT, động lượng của vật là đại lượng vectơ bằng tích của khối lượng và vectơ vận tốc: $\overrightarrow{p} = m\overrightarrow{v}$.",
            ),
            mcq(
                "biet",
                r"Đơn vị chuẩn của động lượng trong hệ đơn vị quốc tế SI là:",
                [
                    r"$\text{kg}\cdot\text{m/s}$",
                    r"$\text{kg}\cdot\text{m/s}^2$",
                    r"$\text{N/s}$",
                    r"$\text{J}\cdot\text{s}$",
                ],
                0,
                r"Theo Bài 28 SGK Vật lí 10 KNTT, vì $p = mv$ nên đơn vị của động lượng là $\text{kg}\cdot\text{m/s}$ (hoặc $\text{N}\cdot\text{s}$).",
            ),
            mcq(
                "biet",
                r"Định luật bảo toàn động lượng được áp dụng chính xác cho hệ vật nào sau đây?",
                [
                    r"Hệ vật chuyển động trên mặt phẳng ngang có ma sát lớn.",
                    r"Hệ vật rơi tự do dưới tác dụng của trọng lực trong thời gian dài.",
                    r"Hệ kín (hệ cô lập không có ngoại lực hoặc tổng các ngoại lực bằng $\overrightarrow{0}$).",
                    r"Mọi hệ vật bất kì không phụ thuộc vào ngoại lực.",
                ],
                2,
                r"Theo Bài 29 SGK Vật lí 10 KNTT, định luật bảo toàn động lượng phát biểu rằng động lượng toàn phần của một hệ kín là một đại lượng bảo toàn.",
            ),
            mcq(
                "biet",
                r"Hiện tượng nào sau đây là ứng dụng trực tiếp của chuyển động bằng phản lực?",
                [
                    r"Quả táo rụng từ trên cành cây rơi thẳng xuống đất.",
                    r"Tên lửa đẩy tàu vũ trụ bay lên nhờ phụt luồng khí đốt nóng về phía sau.",
                    r"Xe đạp lăn xuống dốc nghiêng ngày càng nhanh dù không đạp bàn đạp.",
                    r"Cánh quạt trần tiếp tục quay thêm vài vòng sau khi đã ngắt công tắc điện.",
                ],
                1,
                r"Theo Bài 29 SGK Vật lí 10 KNTT, tên lửa hoạt động dựa trên nguyên tắc chuyển động bằng phản lực (bảo toàn động lượng khi phụt khí về phía sau).",
            ),
            mcq(
                "hieu",
                r"Một vật có khối lượng $m = 2\text{ kg}$ đang chuyển động với động năng $W_{\text{đ}} = 16\text{ J}$. Độ lớn động lượng $p$ của vật khi đó bằng:",
                [
                    r"$4\text{ kg}\cdot\text{m/s}$",
                    r"$8\text{ kg}\cdot\text{m/s}$",
                    r"$16\text{ kg}\cdot\text{m/s}$",
                    r"$32\text{ kg}\cdot\text{m/s}$",
                ],
                1,
                r"Áp dụng hệ thức liên hệ giữa động lượng và động năng: $p = \sqrt{2m W_{\text{đ}}} = \sqrt{2 \cdot 2 \cdot 16} = \sqrt{64} = 8\text{ kg}\cdot\text{m/s}$.",
            ),
            mcq(
                "hieu",
                r"Hai vật nhỏ có động lượng lần lượt là $\overrightarrow{p}_1$ và $\overrightarrow{p}_2$ với độ lớn $p_1 = 3\text{ kg}\cdot\text{m/s}$ và $p_2 = 4\text{ kg}\cdot\text{m/s}$. Biết hai vật chuyển động theo hai phương vuông góc với nhau ($\overrightarrow{p}_1 \perp \overrightarrow{p}_2$). Độ lớn động lượng tổng cộng của hệ hai vật là:",
                [
                    r"$7\text{ kg}\cdot\text{m/s}$",
                    r"$1\text{ kg}\cdot\text{m/s}$",
                    r"$5\text{ kg}\cdot\text{m/s}$",
                    r"$12\text{ kg}\cdot\text{m/s}$",
                ],
                2,
                r"Vì $\overrightarrow{p} = \overrightarrow{p}_1 + \overrightarrow{p}_2$ và $\overrightarrow{p}_1 \perp \overrightarrow{p}_2$ nên độ lớn động lượng của hệ là $p = \sqrt{p_1^2 + p_2^2} = \sqrt{3^2 + 4^2} = 5\text{ kg}\cdot\text{m/s}$.",
            ),
            tf4(
                "hieu",
                r"Một cầu thủ bóng đá thực hiện cú sút phạt vào quả bóng có khối lượng $m = 0,45\text{ kg}$ đang nằm yên trên mặt sân cỏ. Sau cú sút với thời gian chân chạm bóng là $\Delta t = 0,02\text{ s}$, quả bóng bay đi với tốc độ $v = 20\text{ m/s}$.",
                [
                    r"Động lượng của quả bóng ngay trước khi sút có độ lớn bằng $0\text{ kg}\cdot\text{m/s}$.",
                    r"Độ lớn động lượng của quả bóng ngay sau khi rời chân cầu thủ là $p = 9,0\text{ kg}\cdot\text{m/s}$.",
                    r"Xung lượng của lực do chân cầu thủ tác dụng lên quả bóng có độ lớn là $9,0\text{ N}\cdot\text{s}$.",
                    r"Độ lớn lực trung bình của chân cầu thủ tác dụng lên quả bóng trong thời gian chạm bóng là $F = 45\text{ N}$.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** Ban đầu bóng đứng yên ($v_0 = 0$) nên $p_0 = 0\text{ kg}\cdot\text{m/s}$.
- **b) Đúng:** $p = mv = 0,45 \cdot 20 = 9,0\text{ kg}\cdot\text{m/s}$.
- **c) Đúng:** Độ lớn xung lượng của lực bằng độ biến thiên động lượng: $|\overrightarrow{F}\Delta t| = |\Delta \overrightarrow{p}| = 9,0\text{ N}\cdot\text{s}$.
- **d) Sai:** Lực trung bình có độ lớn là $F = \dfrac{\Delta p}{\Delta t} = \dfrac{9,0}{0,02} = 450\text{ N} \neq 45\text{ N}$.""",
            ),
            tf4(
                "hieu",
                r"Trên băng đệm khí nằm ngang không ma sát, xe lăn $1$ có khối lượng $m_1 = 0,3\text{ kg}$ đang chuyển động theo chiều dương với tốc độ $v_1 = 2,0\text{ m/s}$ đến va chạm vào xe lăn $2$ có khối lượng $m_2 = 0,2\text{ kg}$ đang đứng yên ($v_2 = 0$). Sau va chạm, hai xe dính vào nhau và chuyển động cùng vận tốc $v'$.",
                [
                    r"Va chạm giữa hai xe lăn trong thí nghiệm này là va chạm mềm.",
                    r"Tổng động lượng của hệ hai xe ngay trước va chạm là $p_{\text{trước}} = 0,6\text{ kg}\cdot\text{m/s}$.",
                    r"Tốc độ chung của hai xe ngay sau va chạm là $v' = 1,2\text{ m/s}$.",
                    r"Tổng động năng của hệ hai xe trước và sau va chạm được bảo toàn hoàn toàn.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** Hai vật sau va chạm dính vào nhau và chuyển động cùng vận tốc là va chạm mềm.
- **b) Đúng:** $p_{\text{trước}} = m_1 v_1 + m_2 v_2 = 0,3 \cdot 2,0 + 0 = 0,6\text{ kg}\cdot\text{m/s}$.
- **c) Đúng:** Theo định luật bảo toàn động lượng: $v' = \dfrac{m_1 v_1}{m_1 + m_2} = \dfrac{0,6}{0,3 + 0,2} = 1,2\text{ m/s}$.
- **d) Sai:** Trong va chạm mềm, động năng **không bảo toàn** ($W_{\text{đ trước}} = \dfrac{1}{2} \cdot 0,3 \cdot 2,0^2 = 0,6\text{ J}$, trong khi $W_{\text{đ sau}} = \dfrac{1}{2} \cdot 0,5 \cdot 1,2^2 = 0,36\text{ J}$, hao hụt $0,24\text{ J}$ chuyển thành nhiệt).""",
            ),
            mcq(
                "vandung",
                r"Một khẩu pháo có khối lượng $M = 500\text{ kg}$ (chưa tính đạn) đang đứng yên trên mặt phẳng ngang không ma sát thì bắn một viên đạn khối lượng $m = 5\text{ kg}$ bay ra khỏi nòng theo phương ngang với tốc độ $v = 300\text{ m/s}$ so với mặt đất. Ngay sau khi bắn, thân pháo giật lùi với tốc độ $V$ bằng:",
                [
                    r"$1,5\text{ m/s}$",
                    r"$3,0\text{ m/s}$",
                    r"$6,0\text{ m/s}$",
                    r"$0,3\text{ m/s}$",
                ],
                1,
                r"""Áp dụng định luật bảo toàn động lượng theo phương ngang cho hệ pháo – đạn (ban đầu đứng yên nên $p_{\text{trước}} = 0$):
$$M V - m v = 0 \implies V = \dfrac{m v}{M} = \dfrac{5 \cdot 300}{500} = 3,0\text{ m/s}$$""",
            ),
            short(
                "vandung",
                r"Viên bi thứ nhất có khối lượng $m_1 = 0,4\text{ kg}$ chuyển động trên mặt phẳng ngang không ma sát với tốc độ $v_1 = 5\text{ m/s}$ đến va chạm mềm vào viên bi thứ hai có khối lượng $m_2 = 0,6\text{ kg}$ đang chuyển động **ngược chiều** với tốc độ $v_2 = 2\text{ m/s}$. Sau va chạm, hai viên bi dính vào nhau. Tính tốc độ chung $v'$ của hai viên bi ngay sau va chạm theo đơn vị $\text{m/s}$ (dùng dấu phẩy cho số thập phân, chỉ ghi phần số).",
                ["0,8", "0.8"],
                r"""Chọn chiều dương là chiều chuyển động ban đầu của viên bi thứ nhất ($v_{1x} = +5\text{ m/s}$, $v_{2x} = -2\text{ m/s}$).
Áp dụng định luật bảo toàn động lượng cho va chạm mềm:
$$(m_1 + m_2)v' = m_1 v_{1x} + m_2 v_{2x} = 0,4 \cdot 5 + 0,6 \cdot (-2) = 2,0 - 1,2 = 0,8\text{ kg}\cdot\text{m/s}$$
Suy ra tốc độ chung của hai viên bi ngay sau va chạm là:
$$v' = \dfrac{0,8}{0,4 + 0,6} = 0,8\text{ m/s}$$""",
            ),
        ],
    },

    # =========================================================================
    # CHƯƠNG VI & VII. CHUYỂN ĐỘNG TRÒN ĐỀU, BIẾN DẠNG VẬT RẮN & ÁP SUẤT CHẤT LỎNG (Bài 31 -> Bài 34)
    # =========================================================================
    {
        "topic": "chuyen-dong-tron-bien-dang-lo-xo",
        "title": "Chương VI & Chương VII. Chuyển động tròn đều, Biến dạng của vật rắn và Áp suất chất lỏng",
        "icon": "🎡",
        "description": "Khảo sát động học và động lực học của chuyển động tròn đều, biến dạng đàn hồi và định luật Hooke của lò xo, cùng khối lượng riêng và áp suất chất lỏng.",
        "requirements": [
            r"Từ tình huống thực tế, thảo luận để nêu được định nghĩa radian ($\text{rad}$) và biểu diễn được độ dịch chuyển góc $\theta$ theo radian; vận dụng được khái niệm tốc độ góc $\omega = \dfrac{\theta}{t} = \dfrac{2\pi}{T} = 2\pi f$ và liên hệ $v = \omega r$.",
            r"Vận dụng được biểu thức gia tốc hướng tâm $a_{\text{ht}} = \dfrac{v^2}{r} = \omega^2 r$ và biểu thức lực hướng tâm $F_{\text{ht}} = m\dfrac{v^2}{r} = m\omega^2 r$; thảo luận và đề xuất giải pháp an toàn cho các tình huống chuyển động tròn trong thực tế (xe qua khúc cua, cầu vồng).",
            r"Thực hiện thí nghiệm đơn giản, nêu được sự biến dạng kéo, biến dạng nén; mô tả được các đặc tính của lò xo: giới hạn đàn hồi, độ biến dạng $\Delta l$, độ cứng $k$.",
            r"Tìm mối liên hệ giữa lực đàn hồi và độ biến dạng của lò xo, từ đó phát biểu và vận dụng được định luật Hooke $F_{\text{đh}} = k|\Delta l|$ trong một số trường hợp đơn giản.",
            r"Nêu được định nghĩa khối lượng riêng $\rho = \dfrac{m}{V}$, áp suất $p = \dfrac{F}{S}$ và thiết lập, vận dụng được công thức tính áp suất chất lỏng $p = p_0 + \rho gh$ và độ chênh lệch áp suất $\Delta p = \rho g\Delta h$.",
        ],
        "definition": r"""
**Chuyển động tròn đều** là chuyển động có quỹ đạo là một đường tròn và có tốc độ (cũng như tốc độ góc $\omega$) không đổi trên mọi cung tròn, luôn chịu tác dụng của hợp lực hướng vào tâm quỹ đạo gọi là **lực hướng tâm** $F_{\text{ht}} = m\dfrac{v^2}{r} = m\omega^2 r$. Đối với môi trường vật chất liên tục, biến dạng đàn hồi của vật rắn tuân theo **Định luật Hooke** $F_{\text{đh}} = k|\Delta l|$, còn trong chất lỏng đứng yên, áp suất tăng tuyến tính theo độ sâu $h$ theo quy luật $p = p_0 + \rho g h$.
""",
        "theory": r"""
### Bài 31. Động học của chuyển động tròn đều

- **Độ dịch chuyển góc ($\theta$) và đơn vị radian ($\text{rad}$):**
  + Khi chất điểm chuyển động trên đường tròn bán kính $r$ đi được cung tròn có độ dài $s$, góc ở tâm chắn cung đó là độ dịch chuyển góc: $\theta = \dfrac{s}{r}$.
  + **Một radian ($1\text{ rad}$)** là góc ở tâm chắn cung có độ dài bằng bán kính đường tròn ($s = r \implies \theta = 1\text{ rad}$).
  + Đổi đơn vị giữa độ và radian: $360^\circ = 2\pi\text{ rad} \implies 180^\circ = \pi\text{ rad} \implies \alpha(\text{rad}) = \alpha^\circ \cdot \dfrac{\pi}{180^\circ}$.
- **Tốc độ góc ($\omega$):** Đặc trưng cho tốc độ quay quanh tâm của bán kính nối tâm tới vật:
  $$\omega = \dfrac{\theta}{t} \quad (\text{Đơn vị: }\text{rad/s})$$
- **Chu kì ($T$) và Tần số ($f$):**
  + **Chu kì ($T$):** Thời gian để vật quay hết một vòng trọn vẹn ($\theta = 2\pi\text{ rad}$): $T = \dfrac{2\pi}{\omega}$ (đơn vị: $\text{s}$).
  + **Tần số ($f$):** Số vòng vật đi được trong $1\text{ s}$: $f = \dfrac{1}{T} = \dfrac{\omega}{2\pi}$ (đơn vị: héc, $\text{Hz}$ hoặc $\text{vòng/s}$).
- **Vận tốc trong chuyển động tròn đều:**
  + Vectơ vận tốc tức thời $\overrightarrow{v}$ luôn có phương **tiếp tuyến** với đường tròn quỹ đạo (nên hướng của $\overrightarrow{v}$ luôn thay đổi liên tục), nhưng độ lớn (tốc độ dài) không đổi:
    $$v = \dfrac{s}{t} = \omega r = \dfrac{2\pi r}{T} = 2\pi f r$$

### Bài 32. Lực hướng tâm và gia tốc hướng tâm

- **Gia tốc hướng tâm ($\overrightarrow{a}_{\text{ht}}$):** Tuy tốc độ dài $v$ không đổi nhưng hướng của vectơ vận tốc $\overrightarrow{v}$ thay đổi liên tục nên chuyển động tròn đều luôn có gia tốc. Vectơ gia tốc này luôn vuông góc với $\overrightarrow{v}$ và hướng vào tâm đường tròn quỹ đạo nên gọi là **gia tốc hướng tâm**:
  $$a_{\text{ht}} = \dfrac{v^2}{r} = \omega^2 r$$
- **Lực hướng tâm ($\overrightarrow{F}_{\text{ht}}$):**
  + Theo Định luật 2 Newton, lực (hoặc hợp lực của các lực) tác dụng vào một vật chuyển động tròn đều và gây ra cho vật gia tốc hướng tâm được gọi là **lực hướng tâm**:
    $$F_{\text{ht}} = m a_{\text{ht}} = m\dfrac{v^2}{r} = m\omega^2 r$$
  + **Lưu ý quan trọng:** Lực hướng tâm **không phải** là một loại lực mới thêm vào các lực đã biết, mà chỉ là tên gọi của một trong các lực đã học (lực hấp dẫn giữa Trái Đất và vệ tinh, lực ma sát nghỉ giữ xe khi vào cua, lực căng dây, lực đàn hồi) hoặc hợp lực của chúng khi đóng vai trò giữ vật trên quỹ đạo tròn.
- **Giải pháp an toàn khi xe qua khúc cua:** Khi ô tô vào khúc cua phẳng bán kính $r$, lực ma sát nghỉ cực đại đóng vai trò lực hướng tâm: $m\dfrac{v^2}{r} \le \mu_{\text{n}} mg \implies v_{\max} = \sqrt{\mu_{\text{n}} g r}$. Để tăng tốc độ giới hạn an toàn, mặt đường ở các đoạn cua cao tốc hoặc đường sắt luôn được làm **nghiêng về phía tâm khúc cua** một góc $\alpha$ sao cho hợp lực của $\overrightarrow{P}$ và $\overrightarrow{N}$ hướng vào tâm ($\tan\alpha = \dfrac{v^2}{gr}$).

### Bài 33. Biến dạng của vật rắn

- **Biến dạng đàn hồi và biến dạng dẻo (biến dạng còn dư):**
  + Khi có ngoại lực tác dụng, vật rắn thay đổi hình dạng hoặc kích thước (gọi là bị biến dạng). Nếu khi thôi tác dụng lực mà vật tự lấy lại hoàn toàn hình dạng và kích thước ban đầu thì biến dạng đó là **biến dạng đàn hồi**; ngược lại nếu vật không lấy lại được hình dạng ban đầu thì là biến dạng dẻo.
  + **Biến dạng kéo:** Kích thước của vật theo phương tác dụng lực tăng lên so với chiều dài tự nhiên $l_0$ ($l > l_0$).
  + **Biến dạng nén:** Kích thước của vật theo phương tác dụng lực giảm xuống so với chiều dài tự nhiên $l_0$ ($l < l_0$).
- **Các đặc tính của lò xo và Định luật Hooke:**
  + **Độ biến dạng của lò xo:** $\Delta l = l - l_0$ (độ dãn khi $\Delta l > 0$, độ nén khi $\Delta l < 0$).
  + **Giới hạn đàn hồi:** Là giá trị lớn nhất của ngoại lực (hoặc độ biến dạng) mà vượt quá nó lò xo không thể khôi phục lại hình dạng ban đầu (bị hỏng tính đàn hồi).
  + **Định luật Hooke:** Trong giới hạn đàn hồi, độ lớn của lực đàn hồi của lò xo tỉ lệ thuận với độ biến dạng của lò xo:
    $$F_{\text{đh}} = k|\Delta l| = k|l - l_0|$$
    Trong đó $k$ là **độ cứng** (hay hệ số đàn hồi) của lò xo, có đơn vị chuẩn trong hệ SI là niutơn trên mét ($\text{N/m}$), phụ thuộc vào bản chất vật liệu, tiết diện dây và chiều dài tự nhiên của lò xo.
  + Khi treo thẳng đứng một vật khối lượng $m$ vào lò xo ở trạng thái cân bằng: $F_{\text{đh}} = P \iff k|\Delta l| = mg$.

### Bài 34. Khối lượng riêng. Áp suất chất lỏng

- **Khối lượng riêng ($\rho$):** Là khối lượng của một đơn vị thể tích chất đó:
  $$\rho = \dfrac{m}{V} \quad (\text{Đơn vị chuẩn SI: }\text{kg/m}^3 \text{ ; } 1\text{ g/cm}^3 = 1000\text{ kg/m}^3)$$
- **Áp lực và Áp suất ($p$):**
  + **Áp lực ($F_N$):** Là lực ép có phương vuông góc với mặt bị ép.
  + **Áp suất ($p$):** Đặc trưng cho tác dụng mạnh hay yếu của áp lực trên một đơn vị diện tích bị ép:
    $$p = \dfrac{F_N}{S}$$
    Đơn vị chuẩn trong hệ SI là paxcan ($\text{Pa}$), với $1\text{ Pa} = 1\text{ N/m}^2$. Các đơn vị khác: $1\text{ atm} \approx 1,013 \cdot 10^5\text{ Pa}$, $1\text{ bar} = 10^5\text{ Pa}$.
- **Áp suất chất lỏng:**
  + Chất lỏng gây ra áp suất theo mọi phương lên đáy bình, thành bình và các vật ở trong lòng nó.
  + Tại một điểm ở độ sâu $h$ so với mặt thoáng của chất lỏng có khối lượng riêng $\rho$, khi mặt thoáng chịu áp suất khí quyển $p_0$, áp suất tuyệt đối tại điểm đó là:
    $$p = p_0 + \rho g h$$
    Trong đó $p_{\text{cl}} = \rho g h$ là áp suất do riêng cột chất lỏng gây ra.
  + **Độ chênh lệch áp suất giữa hai điểm** ở độ sâu $h_1$ và $h_2$ trong cùng một chất lỏng đứng yên:
    $$\Delta p = p_2 - p_1 = \rho g (h_2 - h_1) = \rho g \Delta h$$
    (Mọi điểm nằm trên cùng một mặt phẳng nằm ngang trong lòng một chất lỏng đứng yên thì có áp suất bằng nhau).
""",
        "formulas": [
            G(
                "Động học và Động lực học chuyển động tròn đều",
                F(
                    "Độ dịch chuyển góc và Tốc độ góc",
                    r"$\theta = \dfrac{s}{r} \quad ; \quad \omega = \dfrac{\theta}{t} = \dfrac{2\pi}{T} = 2\pi f$",
                    r"$\theta$ tính bằng $\text{rad}$, $\omega$ tính bằng $\text{rad/s}$, $T$ là chu kì ($\text{s}$), $f$ là tần số ($\text{Hz}$)",
                ),
                F(
                    "Liên hệ giữa tốc độ dài và tốc độ góc",
                    r"$v = \omega r = \dfrac{2\pi r}{T} = 2\pi f r$",
                    r"$r$ là bán kính quỹ đạo tròn ($\text{m}$), $v$ tính bằng $\text{m/s}$",
                ),
                F(
                    "Gia tốc hướng tâm",
                    r"$a_{\text{ht}} = \dfrac{v^2}{r} = \omega^2 r$",
                    r"Vectơ $\overrightarrow{a}_{\text{ht}}$ luôn hướng vào tâm đường tròn quỹ đạo",
                ),
                F(
                    "Lực hướng tâm",
                    r"$F_{\text{ht}} = m a_{\text{ht}} = m\dfrac{v^2}{r} = m\omega^2 r$",
                    r"Hợp lực hướng vào tâm giữ vật chuyển động tròn đều",
                ),
            ),
            G(
                "Biến dạng của vật rắn – Định luật Hooke",
                F(
                    "Biểu thức Định luật Hooke",
                    r"$F_{\text{đh}} = k|\Delta l| = k|l - l_0|$",
                    r"Áp dụng trong giới hạn đàn hồi; $k$ là độ cứng lò xo ($\text{N/m}$)",
                ),
                F(
                    r"Lò xo treo thẳng đứng cân bằng với vật $m$",
                    r"$k\Delta l = mg \implies \Delta l = \dfrac{mg}{k}$",
                    r"$\Delta l$ là độ dãn của lò xo tại vị trí cân bằng ($\text{m}$)",
                ),
            ),
            G(
                "Khối lượng riêng và Áp suất chất lỏng",
                F(
                    "Khối lượng riêng",
                    r"$\rho = \dfrac{m}{V}$",
                    r"Đơn vị chuẩn SI: $\text{kg/m}^3$ ($1\text{ g/cm}^3 = 1000\text{ kg/m}^3$)",
                ),
                F(
                    "Áp suất trên bề mặt bị ép",
                    r"$p = \dfrac{F_N}{S}$",
                    r"$F_N$ là áp lực vuông góc ($\text{N}$), $S$ là diện tích ($\text{m}^2$), đơn vị $\text{Pa} = \text{N/m}^2$",
                ),
                F(
                    r"Áp suất chất lỏng tại độ sâu $h$",
                    r"$p = p_0 + \rho g h \quad ; \quad \Delta p = \rho g \Delta h$",
                    r"$p_0$ là áp suất khí quyển tại mặt thoáng ($\text{Pa}$), $h$ là độ sâu tính từ mặt thoáng ($\text{m}$)",
                ),
            ),
        ],
        "example": r"""
Một lò xo nhẹ có chiều dài tự nhiên $l_0 = 20\text{ cm}$ và độ cứng $k = 100\text{ N/m}$. Lấy gia tốc rơi tự do $g = 10\text{ m/s}^2$.
1. Treo thẳng đứng lò xo và móc vào đầu dưới của nó một quả nặng có khối lượng $m = 500\text{ g}$. Tính độ dãn $\Delta l$ và chiều dài $l$ của lò xo khi quả nặng nằm cân bằng (biết lò xo vẫn trong giới hạn đàn hồi).
2. Đặt hệ lò xo và quả nặng $m = 500\text{ g}$ trên mặt bàn tròn nằm ngang nhẵn (không ma sát). Giữ cố định đầu trong của lò xo tại tâm bàn quay $O$ và cho bàn quay đều quanh trục thẳng đứng đi qua $O$ với tốc độ góc $\omega = 10\text{ rad/s}$. Tính chiều dài $l'$ của lò xo khi quả nặng quay tròn đều ổn định trên mặt bàn.
""",
        "example_answer": r"""
**Lời giải chi tiết:**
1. **Khi treo thẳng đứng quả nặng $m = 500\text{ g} = 0,5\text{ kg}$ ở trạng thái cân bằng:**
   Lực đàn hồi của lò xo cân bằng với trọng lực của quả nặng:
   $$F_{\text{đh}} = P \iff k\Delta l = mg$$
   Độ dãn của lò xo khi cân bằng là:
   $$\Delta l = \dfrac{mg}{k} = \dfrac{0,5 \cdot 10}{100} = 0,05\text{ m} = 5\text{ cm}$$
   Chiều dài của lò xo khi đó là:
   $$l = l_0 + \Delta l = 20 + 5 = 25\text{ cm}$$
2. **Khi quả nặng quay tròn đều trên mặt bàn ngang nhẵn với tốc độ góc $\omega = 10\text{ rad/s}$:**
   Trên phương thẳng đứng, trọng lực $\overrightarrow{P}$ và phản lực $\overrightarrow{N}$ của mặt bàn cân bằng nhau. Trên phương nằm ngang hướng vào tâm $O$, **lực đàn hồi của lò xo đóng vai trò là lực hướng tâm** giữ cho quả nặng chuyển động tròn đều trên đường tròn có bán kính chính bằng chiều dài lúc dãn $r = l' = l_0 + \Delta l'$ của lò xo:
   $$F_{\text{đh}}' = F_{\text{ht}} \iff k(l' - l_0) = m\omega^2 l'$$
   Đổi $l_0 = 20\text{ cm} = 0,20\text{ m}$, thay số vào phương trình:
   $$100 \cdot (l' - 0,20) = 0,5 \cdot 10^2 \cdot l' \iff 100l' - 20 = 50l'$$
   $$50l' = 20 \implies l' = 0,40\text{ m} = 40\text{ cm}$$
   Vậy chiều dài của lò xo khi quay tròn đều là $l' = 40\text{ cm}$ (lò xo dãn thêm $\Delta l' = 20\text{ cm}$).
""",
        "real_life": r"""
Các vệ tinh nhân tạo (như vệ tinh viễn thông VINASAT-$1$, VINASAT-$2$ của Việt Nam) chuyển động tròn đều trên quỹ đạo địa tĩnh nhờ lực hấp dẫn của Trái Đất đóng vai trò **lực hướng tâm** $F_{\text{ht}} = m\omega^2 r$. Trong kĩ thuật xây dựng và cơ khí, hệ thống giảm xóc ô tô, cân lò xo, đệm lò xo được tính toán độ cứng $k$ dựa theo **Định luật Hooke**, còn vỏ tàu ngầm và đập thủy điện (có chân đập dày hơn nhiều so với đỉnh đập) được thiết kế để chịu được **áp suất chất lỏng** $p = p_0 + \rho gh$ tăng rất lớn theo độ sâu dưới lòng biển và hồ chứa.
""",
        "game_title": "Trạm Vũ Trụ Quay Ly Tâm, Lò Xo Hooke & Tàu Ngầm Áp Suất",
        "game_description": "Điều chỉnh tốc độ góc để giữ vệ tinh trên quỹ đạo tròn, khảo sát đồ thị lực đàn hồi của lò xo và lặn tàu ngầm đo áp suất theo độ sâu.",
        "game_type": "game_chuyen_dong_tron_lo_xo",
        "quiz": [
            mcq(
                "biet",
                r"Trong chuyển động tròn đều bán kính $r$ với tốc độ dài $v$ và tốc độ góc $\omega$, công thức tính gia tốc hướng tâm $a_{\text{ht}}$ là:",
                [
                    r"$a_{\text{ht}} = \dfrac{v^2}{r} = \omega^2 r$",
                    r"$a_{\text{ht}} = \dfrac{v}{r} = \omega r^2$",
                    r"$a_{\text{ht}} = v^2 r = \dfrac{\omega^2}{r}$",
                    r"$a_{\text{ht}} = \dfrac{v^2}{2r} = 2\omega^2 r$",
                ],
                0,
                r"Theo Bài 32 SGK Vật lí 10 KNTT, độ lớn gia tốc hướng tâm trong chuyển động tròn đều là $a_{\text{ht}} = \dfrac{v^2}{r} = \omega^2 r$.",
            ),
            mcq(
                "biet",
                r"Theo Định luật Hooke, trong giới hạn đàn hồi, độ lớn lực đàn hồi $F_{\text{đh}}$ của lò xo có độ cứng $k$ khi bị biến dạng một đoạn $|\Delta l|$ được xác định bởi công thức:",
                [
                    r"$F_{\text{đh}} = k|\Delta l|$",
                    r"$F_{\text{đh}} = \dfrac{1}{2}k(\Delta l)^2$",
                    r"$F_{\text{đh}} = \dfrac{k}{|\Delta l|}$",
                    r"$F_{\text{đh}} = k^2|\Delta l|$",
                ],
                0,
                r"Theo Bài 33 SGK Vật lí 10 KNTT, biểu thức Định luật Hooke là $F_{\text{đh}} = k|\Delta l|$, đơn vị của độ cứng $k$ là $\text{N/m}$.",
            ),
            mcq(
                "biet",
                r"Gọi $p_0$ là áp suất khí quyển tại mặt thoáng, $\rho$ là khối lượng riêng của chất lỏng và $g$ là gia tốc trọng trường. Áp suất tuyệt đối $p$ tại một điểm nằm ở độ sâu $h$ trong lòng chất lỏng đứng yên là:",
                [
                    r"$p = p_0 + \rho g h$",
                    r"$p = p_0 - \rho g h$",
                    r"$p = \dfrac{\rho g}{h}$",
                    r"$p = p_0 \cdot \rho g h$",
                ],
                0,
                r"Theo Bài 34 SGK Vật lí 10 KNTT, áp suất tại độ sâu $h$ trong chất lỏng đứng yên là $p = p_0 + \rho g h$.",
            ),
            mcq(
                "biet",
                r"Khi một chất điểm chuyển động tròn đều với chu kì $T = 2,0\text{ s}$ thì tốc độ góc $\omega$ của chất điểm đó bằng:",
                [
                    r"$\pi\text{ rad/s}$",
                    r"$2\pi\text{ rad/s}$",
                    r"$0,5\text{ rad/s}$",
                    r"$4\pi\text{ rad/s}$",
                ],
                0,
                r"Theo Bài 31 SGK Vật lí 10 KNTT, tốc độ góc liên hệ với chu kì theo công thức $\omega = \dfrac{2\pi}{T} = \dfrac{2\pi}{2,0} = \pi\text{ rad/s}$.",
            ),
            mcq(
                "hieu",
                r"Một lò xo nhẹ có chiều dài tự nhiên $l_0 = 30\text{ cm}$. Khi treo thẳng đứng một vật có trọng lượng $P = 12\text{ N}$ vào đầu dưới của lò xo thì khi cân bằng lò xo có chiều dài $l = 36\text{ cm}$ (trong giới hạn đàn hồi). Độ cứng $k$ của lò xo này là:",
                [
                    r"$20\text{ N/m}$",
                    r"$200\text{ N/m}$",
                    r"$33,3\text{ N/m}$",
                    r"$400\text{ N/m}$",
                ],
                1,
                r"Độ biến dạng (độ dãn) của lò xo là $\Delta l = l - l_0 = 36 - 30 = 6\text{ cm} = 0,06\text{ m}$. Khi cân bằng $F_{\text{đh}} = P = 12\text{ N}$, suy ra $k = \dfrac{F_{\text{đh}}}{\Delta l} = \dfrac{12}{0,06} = 200\text{ N/m}$.",
            ),
            mcq(
                "hieu",
                r"Một ô tô có khối lượng $m = 1200\text{ kg}$ chạy đều với tốc độ $v = 36\text{ km/h}$ qua một khúc cua phẳng nằm ngang có dạng cung tròn bán kính $r = 50\text{ m}$. Độ lớn lực hướng tâm giữ cho ô tô chuyển động trên cung tròn đó là:",
                [
                    r"$2400\text{ N}$",
                    r"$1200\text{ N}$",
                    r"$31\,104\text{ N}$",
                    r"$600\text{ N}$",
                ],
                0,
                r"Đổi $v = 36\text{ km/h} = 10\text{ m/s}$. Lực hướng tâm có độ lớn là $F_{\text{ht}} = m\dfrac{v^2}{r} = 1200 \cdot \dfrac{10^2}{50} = 2400\text{ N}$.",
            ),
            tf4(
                "hieu",
                r"Một lồng giặt của máy giặt có dạng hình trụ bán kính $r = 0,25\text{ m}$. Ở chế độ vắt khô, lồng giặt quay tròn đều với tần số $f = 10\text{ vòng/s}$ ($10\text{ Hz}$). Xét một quần áo có khối lượng $m = 0,2\text{ kg}$ nằm áp sát vào thành trong của lồng giặt.",
                [
                    r"Chu kì quay của lồng giặt là $T = 0,1\text{ s}$ và tốc độ góc là $\omega = 20\pi\text{ rad/s}$.",
                    r"Tốc độ dài của quần áo nằm sát thành lồng giặt là $v = 5\pi\text{ m/s} \approx 15,7\text{ m/s}$.",
                    r"Vectơ vận tốc tức thời và vectơ gia tốc hướng tâm của quần áo đều có hướng không đổi theo thời gian.",
                    r"Áp lực của thành lồng giặt tác dụng vào quần áo đóng vai trò lực hướng tâm có độ lớn $F_{\text{ht}} = m\omega^2 r = 20\pi^2\text{ N}$ (lấy $\pi^2 \approx 10$ thì $F_{\text{ht}} \approx 200\text{ N}$).",
                ],
                [True, True, False, True],
                r"""- **a) Đúng:** $T = \dfrac{1}{f} = 0,1\text{ s}$; $\omega = 2\pi f = 20\pi\text{ rad/s}$.
- **b) Đúng:** $v = \omega r = 20\pi \cdot 0,25 = 5\pi\text{ m/s} \approx 15,7\text{ m/s}$.
- **c) Sai:** Trong chuyển động tròn đều, cả vectơ vận tốc $\overrightarrow{v}$ (tiếp tuyến quỹ đạo) và vectơ gia tốc hướng tâm $\overrightarrow{a}_{\text{ht}}$ (luôn hướng vào tâm) đều có **phương, chiều thay đổi liên tục** theo thời gian (chỉ có độ lớn là không đổi).
- **d) Đúng:** $F_{\text{ht}} = m\omega^2 r = 0,2 \cdot (20\pi)^2 \cdot 0,25 = 0,05 \cdot 400\pi^2 = 20\pi^2\text{ N} \approx 200\text{ N}$.""",
            ),
            tf4(
                "hieu",
                r"Một tàu ngầm thám hiểm đang lặn dưới biển ở độ sâu $h = 50\text{ m}$ so với mặt nước biển. Biết khối lượng riêng của nước biển là $\rho = 1025\text{ kg/m}^3$, áp suất khí quyển trên mặt biển là $p_0 = 1,0 \cdot 10^5\text{ Pa}$ và gia tốc trọng trường $g = 10\text{ m/s}^2$.",
                [
                    r"Áp suất do riêng cột nước biển ở độ sâu $50\text{ m}$ gây ra là $p_{\text{cl}} = \rho g h = 5,125 \cdot 10^5\text{ Pa}$.",
                    r"Áp suất tuyệt đối tại vị trí tàu ngầm đang lặn là $p = p_0 + \rho g h = 6,125 \cdot 10^5\text{ Pa}$.",
                    r"Nếu tàu ngầm lặn sâu thêm một đoạn $\Delta h = 20\text{ m}$ nữa thì áp suất tác dụng lên vỏ tàu tăng thêm một lượng $\Delta p = 2,05 \cdot 10^5\text{ Pa}$.",
                    r"Áp lực của nước biển chỉ tác dụng theo phương thẳng đứng từ trên xuống lên mặt trên của tàu ngầm.",
                ],
                [True, True, True, False],
                r"""- **a) Đúng:** $p_{\text{cl}} = \rho g h = 1025 \cdot 10 \cdot 50 = 512\,500\text{ Pa} = 5,125 \cdot 10^5\text{ Pa}$.
- **b) Đúng:** $p = p_0 + \rho g h = 1,0 \cdot 10^5 + 5,125 \cdot 10^5 = 6,125 \cdot 10^5\text{ Pa}$.
- **c) Đúng:** $\Delta p = \rho g \Delta h = 1025 \cdot 10 \cdot 20 = 205\,000\text{ Pa} = 2,05 \cdot 10^5\text{ Pa}$.
- **d) Sai:** Chất lỏng gây ra áp suất theo **mọi phương** và áp lực luôn vuông góc với mọi phần diện tích bề mặt vỏ tàu ngầm bị ép.""",
            ),
            mcq(
                "vandung",
                r"Một cây cầu vồng bắc qua sông có mặt cầu cong lên trên theo một cung tròn trong mặt phẳng thẳng đứng với bán kính cong $r = 40\text{ m}$. Một ô tô có khối lượng $m = 1000\text{ kg}$ chạy qua đỉnh cầu với tốc độ không đổi $v = 36\text{ km/h}$. Lấy $g = 10\text{ m/s}^2$. Độ lớn áp lực $N$ của ô tô đè lên mặt cầu tại điểm cao nhất (đỉnh cầu) là:",
                [
                    r"$10\,000\text{ N}$",
                    r"$7500\text{ N}$",
                    r"$12\,500\text{ N}$",
                    r"$8000\text{ N}$",
                ],
                1,
                r"""Đổi $v = 36\text{ km/h} = 10\text{ m/s}$. Tại đỉnh cầu vồng, tâm cung tròn nằm ở phía dưới nên hợp lực hướng tâm hướng thẳng đứng từ trên xuống dưới:
$$F_{\text{ht}} = P - N = m\dfrac{v^2}{r} \implies N = mg - m\dfrac{v^2}{r}$$
Thay số:
$$N = 1000 \cdot 10 - 1000 \cdot \dfrac{10^2}{40} = 10\,000 - 2500 = 7500\text{ N}$$
Theo Định luật 3 Newton, áp lực của ô tô đè lên mặt cầu có độ lớn bằng phản lực $N = 7500\text{ N}$.""",
            ),
            short(
                "vandung",
                r"Trên một ô cửa sổ quan sát hình tròn của tàu ngầm có diện tích $S = 0,2\text{ m}^2$ đang ở độ sâu $h = 80\text{ m}$ dưới mặt nước biển. Biết khối lượng riêng của nước biển là $\rho = 1025\text{ kg/m}^3$, áp suất khí quyển tại mặt biển là $p_0 = 1,0 \cdot 10^5\text{ Pa}$ và lấy $g = 10\text{ m/s}^2$. Tính độ lớn áp lực $F_N$ của nước biển tác dụng lên mặt ngoài của ô cửa sổ đó theo đơn vị kilôniutơn ($\text{kN}$), chỉ ghi phần số.",
                ["184", "184,0", "184.0"],
                r"""Áp suất tuyệt đối của nước biển tại độ sâu $h = 80\text{ m}$ là:
$$p = p_0 + \rho g h = 1,0 \cdot 10^5 + 1025 \cdot 10 \cdot 80 = 100\,000 + 820\,000 = 920\,000\text{ Pa}$$
Độ lớn áp lực của nước biển tác dụng lên ô cửa sổ diện tích $S = 0,2\text{ m}^2$ là:
$$F_N = p \cdot S = 920\,000 \cdot 0,2 = 184\,000\text{ N} = 184\text{ kN}$$""",
            ),
        ],
    },
]
