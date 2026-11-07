"""Hóa học 11 — Kết nối tri thức với cuộc sống.
Cấu trúc: Lớp 11 -> 6 Chương -> 21 Bài học độc lập.
Mỗi bài có đúng công thức của bài đó, 3+ yêu cầu cần đạt, 10 câu hỏi.
"""
from ._helpers import bai, F, G, mcq, tf, short

GRADE = 11

# =========================================================================
# CHƯƠNG 1: CÂN BẰNG HÓA HỌC
# =========================================================================
CH1_ID = "hoa11_ch1"
CH1_TITLE = "Chương 1: Cân bằng hóa học"
CH1_DESC = "Khái niệm về cân bằng hóa học, hằng số cân bằng Kc, nguyên lí chuyển dịch cân bằng Le Chatelier và cân bằng trong dung dịch nước (pH)"

CH1_LESSONS = [
    bai(1, "Khái niệm về cân bằng hóa học",
        "Phản ứng một chiều, phản ứng thuận nghịch, trạng thái cân bằng hóa học (vt = vn > 0) và biểu thức hằng số cân bằng Kc",
        "Phản ứng một chiều chỉ xảy ra theo chiều từ chất tham gia tạo thành sản phẩm (mũi tên $\\rightarrow$), còn phản ứng thuận nghịch xảy ra đồng thời theo hai chiều ngược nhau trong cùng điều kiện (mũi tên $\\rightleftharpoons$). Cân bằng hóa học là trạng thái của phản ứng thuận nghịch khi tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_t = v_n > 0$); tại trạng thái cân bằng, nồng độ các chất không đổi và đây là cân bằng động. Hằng số cân bằng $K_C$ của phản ứng $a\\text{A} + b\\text{B} \\rightleftharpoons c\\text{C} + d\\text{D}$ chỉ phụ thuộc vào bản chất phản ứng và nhiệt độ (không đưa chất rắn nguyên chất vào biểu thức $K_C$).",
        [
            F("Điều kiện tại Trạng thái cân bằng hóa học", "v_{\\text{thuận}} = v_{\\text{nghịch}} > 0", "Cân bằng hóa học là cân bằng động; nồng độ các chất ở trạng thái cân bằng giữ không đổi"),
            F("Biểu thức Hằng số cân bằng Kc (aA + bB <-> cC + dD)", "K_C = \\frac{[\\text{C}]^c \\cdot [\\text{D}]^d}{[\\text{A}]^a \\cdot [\\text{B}]^b}", "[A], [B], [C], [D] là nồng độ mol ở trạng thái cân bằng; không biểu diễn chất rắn (s) trong Kc"),
        ],
        [
            "Phân biệt được phản ứng một chiều và phản ứng thuận nghịch; nêu được khái niệm trạng thái cân bằng hóa học là cân bằng động",
            "Viết được biểu thức hằng số cân bằng $K_C$ của một phản ứng thuận nghịch (đồng thể và dị thể)",
            "Tính được hằng số cân bằng $K_C$ từ nồng độ cân bằng của các chất",
        ],
        "Cho phản ứng thuận nghịch: $\\text{H}_2(g) + \\text{I}_2(g) \\rightleftharpoons 2\\text{HI}(g)$. Ở $430^\\circ\\text{C}$, nồng độ các chất ở trạng thái cân bằng là $[\\text{H}_2] = [\\text{I}_2] = 0,10\\text{ M}$ và $[\\text{HI}] = 0,70\\text{ M}$. Tính hằng số cân bằng $K_C$ của phản ứng ở nhiệt độ này.",
        "Biểu thức hằng số cân bằng của phản ứng:\n$K_C = \\frac{[\\text{HI}]^2}{[\\text{H}_2] \\cdot [\\text{I}_2]} = \\frac{0,70^2}{0,10 \\cdot 0,10} = \\frac{0,49}{0,01} = 49$.",
        "Sự tạo thành thạch nhũ và sự xâm thực đá vôi trong hang động là một hệ cân bằng thuận nghịch trong tự nhiên: $\\text{CaCO}_3(s) + \\text{CO}_2(aq) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{Ca(HCO}_3)_2(aq)$.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Tại trạng thái cân bằng của một phản ứng thuận nghịch, nhận xét nào sau đây ĐÚNG?", "Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_t = v_n > 0$)", ["Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_t = v_n > 0$)", "Phản ứng thuận và phản ứng nghịch đều dừng lại hoàn toàn ($v_t = v_n = 0$)", "Nồng độ các chất tham gia phải bằng nồng độ các chất sản phẩm", "Các chất tham gia đã phản ứng hết $100\\%$"], "Cân bằng hóa học là cân bằng động: phản ứng không dừng lại mà $v_t = v_n > 0$.", "biet"),
            mcq("Cho cân bằng dị thể: $\\text{C}(s) + \\text{CO}_2(g) \\rightleftharpoons 2\\text{CO}(g)$. Biểu thức hằng số cân bằng $K_C$ của phản ứng là:", "$K_C = \\frac{[\\text{CO}]^2}{[\\text{CO}_2]}$", ["$K_C = \\frac{[\\text{CO}]^2}{[\\text{CO}_2]}$", "$K_C = \\frac{[\\text{CO}]^2}{[\\text{C}]\\cdot[\\text{CO}_2]}$", "$K_C = \\frac{[\\text{CO}_2]}{[\\text{CO}]^2}$", "$K_C = \\frac{2[\\text{CO}]}{[\\text{CO}_2]}$"], "Chất rắn nguyên chất $\\text{C}(s)$ không có mặt trong biểu thức hằng số cân bằng $K_C$.", "hieu"),
            short("Cho cân bằng: $\\text{N}_2\\text{O}_4(g) \\rightleftharpoons 2\\text{NO}_2(g)$. Ở trạng thái cân bằng có $[\\text{N}_2\\text{O}_4] = 0,2\\text{ M}$ và $[\\text{NO}_2] = 0,4\\text{ M}$. Hằng số cân bằng $K_C$ của phản ứng bằng bao nhiêu?", "0,8", ["0,8", "0.8"], "Ta có $K_C = \\frac{[\\text{NO}_2]^2}{[\\text{N}_2\\text{O}_4]} = \\frac{0,4^2}{0,2} = \\frac{0,16}{0,2} = 0,8$.", "vandung"),
        ]
    ),
    bai(2, "Chuyển dịch cân bằng hóa học",
        "Nguyên lí chuyển dịch cân bằng Le Chatelier dưới tác động của nồng độ, áp suất, nhiệt độ và vai trò của chất xúc tác",
        "Nguyên lí chuyển dịch cân bằng Le Chatelier: Một phản ứng thuận nghịch đang ở trạng thái cân bằng khi chịu một tác động từ bên ngoài như biến đổi nồng độ, áp suất, nhiệt độ thì cân bằng sẽ chuyển dịch theo chiều làm giảm tác động bên ngoài đó. Cụ thể: (1) Tăng nồng độ một chất $\\rightarrow$ cân bằng chuyển dịch theo chiều làm giảm nồng độ chất đó; (2) Tăng áp suất chung của hệ $\\rightarrow$ cân bằng chuyển dịch theo chiều làm giảm số mol khí; (3) Tăng nhiệt độ $\\rightarrow$ cân bằng chuyển dịch theo chiều phản ứng thu nhiệt ($\\Delta_r H > 0$). Lưu ý: Chất xúc tác làm tăng đồng thời tốc độ phản ứng thuận và nghịch nên giúp cân bằng nhanh được thiết lập nhưng KHÔNG làm chuyển dịch cân bằng.",
        [
            F("Tác động của Nhiệt độ đến Chuyển dịch cân bằng", "\\begin{cases} \\text{Tăng nhiệt độ } (T \\uparrow) \\implies \\text{Chuyển dịch theo chiều thu nhiệt } (\\Delta_r H > 0) \\\\ \\text{Giảm nhiệt độ } (T \\downarrow) \\implies \\text{Chuyển dịch theo chiều tỏa nhiệt } (\\Delta_r H < 0) \\end{cases}", "Tăng thu - Giảm tỏa"),
            F("Tác động của Áp suất (với hệ có chất khí)", "\\begin{cases} \\text{Tăng áp suất } (P \\uparrow) \\implies \\text{Chuyển dịch theo chiều giảm số mol khí} \\\\ \\text{Nếu } \\sum n_{\\text{khí (trước)}} = \\sum n_{\\text{khí (sau)}} \\implies \\text{Áp suất không làm chuyển dịch cân bằng} \\end{cases}", "Chất xúc tác KHÔNG làm chuyển dịch cân bằng hóa học"),
        ],
        [
            "Phát biểu được nguyên lí chuyển dịch cân bằng Le Chatelier",
            "Vận dụng được nguyên lí Le Chatelier để dự đoán chiều chuyển dịch cân bằng khi thay đổi nồng độ, áp suất, nhiệt độ",
            "Giải thích được điều kiện tối ưu (nhiệt độ, áp suất, xúc tác) trong sản xuất công nghiệp (như tổng hợp $\\text{NH}_3$, sản xuất $\\text{SO}_3$)",
        ],
        "Cho cân bằng tổng hợp ammonia: $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$ có $\\Delta_r H^\\circ_{298} = -91,8\\text{ kJ}$. Để cân bằng chuyển dịch theo chiều thuận (tăng hiệu suất tạo $\\text{NH}_3$), cần tác động vào áp suất và nhiệt độ như thế nào?",
        "- Về áp suất: Phản ứng thuận làm giảm số mol khí (từ $1 + 3 = 4\\text{ mol}$ khí xuống $2\\text{ mol}$ khí), nên cần TĂNG áp suất chung của hệ.\n- Về nhiệt độ: Phản ứng thuận tỏa nhiệt ($\\Delta_r H^\\circ_{298} = -91,8\\text{ kJ} < 0$), nên cần GIẢM nhiệt độ vừa phải (trong công nghiệp duy trì khoảng $400 - 450^\\circ\\text{C}$ kết hợp xúc tác $\\text{Fe}$ để đảm bảo tốc độ phản ứng).",
        "Trong máu người có hệ cân bằng vận chuyển oxygen của hemoglobin ($\\text{Hb} + \\text{O}_2 \\rightleftharpoons \\text{HbO}_2$); khi lên núi cao áp suất riêng phần của $\\text{O}_2$ giảm làm cân bằng chuyển dịch theo chiều nghịch gây thiếu oxygen lên não.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Yếu tố nào sau đây KHÔNG làm chuyển dịch trạng thái cân bằng của một phản ứng thuận nghịch?", "Thêm chất xúc tác vào hệ", ["Thêm chất xúc tác vào hệ", "Thay đổi nhiệt độ của hệ", "Thay đổi nồng độ chất tham gia", "Thay đổi áp suất (khi số mol khí hai vế khác nhau)"], "Chất xúc tác làm tăng tốc độ phản ứng thuận và nghịch như nhau nên không làm chuyển dịch cân bằng.", "biet"),
            mcq("Cho cân bằng hóa học: $2\\text{SO}_2(g) + \\text{O}_2(g) \\rightleftharpoons 2\\text{SO}_3(g)$ có $\\Delta_r H^\\circ_{298} = -198\\text{ kJ} < 0$. Khi tăng nhiệt độ của hệ thì cân bằng chuyển dịch theo chiều nào?", "Chiều nghịch (chiều thu nhiệt)", ["Chiều nghịch (chiều thu nhiệt)", "Chiều thuận (chiều tỏa nhiệt)", "Không chuyển dịch", "Tạo thêm nhiều $\\text{SO}_3$ hơn"], "Vì chiều thuận tỏa nhiệt ($\\Delta_r H < 0$) nên chiều nghịch là chiều thu nhiệt; khi tăng nhiệt độ cân bằng chuyển dịch theo chiều thu nhiệt (chiều nghịch).", "hieu"),
            short("Trong các cân bằng sau: (1) $\\text{H}_2(g) + \\text{I}_2(g) \\rightleftharpoons 2\\text{HI}(g)$; (2) $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$; (3) $2\\text{NO}_2(g) \\rightleftharpoons \\text{N}_2\\text{O}_4(g)$. Cân bằng nào KHÔNG bị chuyển dịch khi thay đổi áp suất chung của hệ (nhập số thứ tự)?", "1", ["1"], "Ở cân bằng (1), tổng số mol khí hai vế bằng nhau ($1 + 1 = 2$) nên áp suất không làm chuyển dịch cân bằng.", "vandung"),
        ]
    ),
    bai(3, "Sự điện li, pH của dung dịch và chuẩn độ acid - base",
        "Chất điện li mạnh, chất điện li yếu, thuyết acid - base Bronsted - Lowry, công thức pH = -lg[H+] và nguyên tắc chuẩn độ acid - base",
        "Sự điện li là quá trình phân li các chất trong nước ra ion. Chất điện li mạnh (acid mạnh $\\text{HCl}, \\text{HNO}_3, \\text{H}_2\\text{SO}_4$; base mạnh $\\text{NaOH}, \\text{KOH}, \\text{Ca(OH)}_2, \\text{Ba(OH)}_2$ và hầu hết các muối tan) phân li hoàn toàn ($\\rightarrow$); chất điện li yếu ($\\text{CH}_3\\text{COOH}, \\text{HF}, \\text{HClO}, \\text{NH}_3, \\text{H}_2\\text{O}$) chỉ phân li một phần ($\\rightleftharpoons$). Theo thuyết Brønsted – Lowry: Acid là chất cho proton ($\\text{H}^+$), Base là chất nhận proton ($\\text{H}^+$). Độ acid - base của dung dịch được đánh giá bằng $\\text{pH} = -\\lg[\\text{H}^+]$ (ở $25^\\circ\\text{C}$: $[\\text{H}^+]\\cdot[\\text{OH}^-] = 10^{-14}$ hay $\\text{pH} + \\text{pOH} = 14$). Chuẩn độ acid - base là phương pháp xác định nồng độ chưa biết của dung dịch acid (hoặc base) bằng một dung dịch chuẩn đã biết nồng độ.",
        [
            F("Thuyết Acid - Base Brønsted – Lowry", "\\text{Acid (cho H}^+\\text{)} \\rightleftharpoons \\text{Base (nhận H}^+\\text{)} + \\text{H}^+", "Ví dụ: CH3COOH là acid (cho H+); NH3 + H2O <-> NH4+ + OH- thì NH3 là base (nhận H+)"),
            F("Tích số ion của nước và Công thức tính pH (ở 25 độ C)", "\\begin{cases} K_w = [\\text{H}^+] \\cdot [\\text{OH}^-] = 10^{-14} \\\\ \\text{pH} = -\\lg[\\text{H}^+] \\iff [\\text{H}^+] = 10^{-\\text{pH}};\\quad \\text{pH} + \\text{pOH} = 14 \\end{cases}", "pH < 7: môi trường acid; pH = 7: trung tính; pH > 7: môi trường kiềm (base)"),
            F("Công thức tại điểm tương đương khi chuẩn độ HCl bằng NaOH", "n_{\\text{H}^+} = n_{\\text{OH}^-} \\iff C_{\\text{HCl}} \\cdot V_{\\text{HCl}} = C_{\\text{NaOH}} \\cdot V_{\\text{NaOH}}", "Dùng chất chỉ thị phenolphthalein nhận biết điểm kết thúc chuẩn độ (không màu chuyển sang hồng nhạt)"),
        ],
        [
            "Phân biệt được chất điện li mạnh, chất điện li yếu, chất không điện li và viết được phương trình điện li",
            "Phát biểu được khái niệm acid, base theo thuyết Brønsted – Lowry và giải thích được môi trường của các dung dịch muối thủy phân ($\\text{AlCl}_3, \\text{Na}_2\\text{CO}_3$)",
            "Tính được $\\text{pH}$ của dung dịch acid mạnh, base mạnh và tính được nồng độ dung dịch từ kết quả chuẩn độ acid - base",
        ],
        "Tính $\\text{pH}$ của: (a) Dung dịch $\\text{HCl}$ $0,01\\text{ M}$; (b) Dung dịch $\\text{NaOH}$ $0,001\\text{ M}$ ở $25^\\circ\\text{C}$.",
        "(a) $\\text{HCl}$ điện li hoàn toàn: $[\\text{H}^+] = C_{\\text{HCl}} = 0,01 = 10^{-2}\\text{ M} \\Rightarrow \\text{pH} = -\\lg(10^{-2}) = 2$.\n(b) $\\text{NaOH}$ điện li hoàn toàn: $[\\text{OH}^-] = 0,001 = 10^{-3}\\text{ M} \\Rightarrow \\text{pOH} = 3 \\Rightarrow \\text{pH} = 14 - 3 = 11$.",
        "Máu người khỏe mạnh có $\\text{pH}$ ổn định trong khoảng $7,35 - 7,45$; dịch vị dạ dày có $\\text{pH}$ từ $1,5 - 3,5$; đất chua ($\\text{pH} < 5$) thường được bà con nông dân bón vôi bột ($\\text{CaO}, \\text{Ca(OH)}_2$) để khử chua.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Theo thuyết Brønsted – Lowry, định nghĩa đúng về acid và base là:", "Acid là chất cho proton ($\\text{H}^+$), base là chất nhận proton ($\\text{H}^+$)", ["Acid là chất cho proton ($\\text{H}^+$), base là chất nhận proton ($\\text{H}^+$)", "Acid là chất nhận proton ($\\text{H}^+$), base là chất cho proton ($\\text{H}^+$)", "Acid là chất cho electron, base là chất nhận electron", "Acid chỉ gồm các chất chứa nguyên tố oxygen"], "Theo Brønsted – Lowry: Acid cho $\\text{H}^+$, Base nhận $\\text{H}^+$.", "biet"),
            mcq("Chất nào sau đây là chất điện li yếu trong dung dịch nước?", "$\\text{CH}_3\\text{COOH}$", ["$\\text{CH}_3\\text{COOH}$", "$\\text{HCl}$", "$\\text{NaOH}$", "$\\text{NaCl}$"], "$\\text{CH}_3\\text{COOH}$ là acid hữu cơ yếu chỉ phân li một phần trong nước, còn $\\text{HCl}, \\text{NaOH}, \\text{NaCl}$ là chất điện li mạnh.", "hieu"),
            short("Để chuẩn độ vừa đủ $10\\text{ mL}$ dung dịch $\\text{HCl}$ chưa biết nồng độ cần dùng hết $15\\text{ mL}$ dung dịch chuẩn $\\text{NaOH}$ $0,1\\text{ M}$. Nồng độ mol của dung dịch $\\text{HCl}$ bằng bao nhiêu $\\text{M}$?", "0,15", ["0,15", "0.15"], "Tại điểm tương đương: $C_{\\text{HCl}} \\cdot 10 = 0,1 \\cdot 15 \\Rightarrow C_{\\text{HCl}} = 0,15\\text{ M}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 2: NITROGEN VÀ SULFUR
# =========================================================================
CH2_ID = "hoa11_ch2"
CH2_TITLE = "Chương 2: Nitrogen và Sulfur"
CH2_DESC = "Đơn chất nitrogen (N2), ammonia (NH3), muối ammonium, hiện tượng phú dưỡng, nitric acid (HNO3), lưu huỳnh (S), SO2 và sulfuric acid (H2SO4)"

CH2_LESSONS = [
    bai(4, "Đơn chất Nitrogen",
        "Liên kết ba bền vững trong phân tử N2, tính trơ ở nhiệt độ thường, tính oxi hóa và tính khử ở nhiệt độ cao",
        "Nguyên tố nitrogen ($\\text{N}, Z = 7$) thuộc ô $7$, chu kì $2$, nhóm $\\text{VA}$. Trong phân tử đơn chất nitrogen ($\\text{N}_2$) có liên kết ba $\\text{N}\\equiv\\text{N}$ ($1\\sigma + 2\\pi$) với năng lượng liên kết rất lớn ($E_b = 945\\text{ kJ/mol}$), nên ở nhiệt độ thường $\\text{N}_2$ rất trơ về mặt hóa học. Ở nhiệt độ cao hoặc có tia lửa điện, xúc tác, $\\text{N}_2$ trở nên hoạt động và vừa thể hiện tính oxi hóa (tác dụng với $\\text{H}_2$ và kim loại mạnh tạo số oxi hóa $-3$), vừa thể hiện tính khử (tác dụng với $\\text{O}_2$ ở $3000^\\circ\\text{C}$ tạo $\\text{NO}$ có số oxi hóa $+2$).",
        [
            F("Tính oxi hóa của N2 (tác dụng với H2 và kim loại)", "\\text{N}_2(g) + 3\\text{H}_2(g) \\underset{\\text{xt Fe}}{\\overset{t^\\circ, p}{\\rightleftharpoons}} 2\\text{NH}_3(g)\\quad (\\Delta_r H^\\circ_{298} = -91,8\\text{ kJ})", "Số oxi hóa của N giảm từ 0 xuống -3 (quy trình Haber-Bosch)"),
            F("Tính khử của N2 (tác dụng với O2 khi có sấm sét)", "\\text{N}_2(g) + \\text{O}_2(g) \\overset{3000^\\circ\\text{C}\\text{ hoặc tia lửa điện}}{\\rightleftharpoons} 2\\text{NO}(g);\\quad 2\\text{NO} + \\text{O}_2 \\rightarrow 2\\text{NO}_2", "NO không màu hóa nâu đỏ ngay trong không khí tạo NO2"),
        ],
        [
            "Giải thích được tính trơ của đơn chất $\\text{N}_2$ ở nhiệt độ thường dựa vào năng lượng liên kết ba $\\text{N}\\equiv\\text{N}$ rất lớn",
            "Trình bày được tính oxi hóa và tính khử của $\\text{N}_2$ ở nhiệt độ cao qua các phương trình hóa học",
            "Nêu được ứng dụng của khí $\\text{N}_2$ (tổng hợp $\\text{NH}_3$, tạo môi trường trơ bảo quản thực phẩm, nitrogen lỏng bảo quản mẫu sinh học)",
        ],
        "Trộn $4\\text{ mol}$ $\\text{N}_2$ với $14\\text{ mol}$ $\\text{H}_2$ trong bình kín có xúc tác thích hợp rồi đun nóng, thu được $1,6\\text{ mol}$ khí $\\text{NH}_3$. Tính hiệu suất của phản ứng tổng hợp $\\text{NH}_3$.",
        "PTHH: $\\text{N}_2 + 3\\text{H}_2 \\rightleftharpoons 2\\text{NH}_3$.\nTa có tỉ lệ: $\\frac{n_{\\text{N}_2}}{1} = 4 < \\frac{n_{\\text{H}_2}}{3} = \\frac{14}{3}$, nên hiệu suất tính theo $\\text{N}_2$.\nSố mol $\\text{N}_2$ đã phản ứng: $n_{\\text{N}_2\\text{ pư}} = \\frac{1}{2}n_{\\text{NH}_3} = 0,8\\text{ mol}$.\nHiệu suất phản ứng: $H = \\frac{0,8}{4} \\cdot 100\\% = 20\\%$.",
        "Câu ca dao 'Lúa chiêm lấp ló đầu bờ / Hễ nghe tiếng sấm phất cờ mà lên' phản ánh quá trình tia chớp biến $\\text{N}_2$ và $\\text{O}_2$ trong không khí thành $\\text{NO} \\rightarrow \\text{NO}_2 \\rightarrow \\text{HNO}_3$ theo nước mưa xuống đất cung cấp đạm tự nhiên ($\\text{NO}_3^-$) cho cây lúa.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Nguyên nhân chính khiến đơn chất nitrogen ($\\text{N}_2$) rất trơ về mặt hóa học ở nhiệt độ thường là:", "Phân tử $\\text{N}_2$ có liên kết ba $\\text{N}\\equiv\\text{N}$ rất bền với năng lượng liên kết lớn ($945\\text{ kJ/mol}$)", ["Phân tử $\\text{N}_2$ có liên kết ba $\\text{N}\\equiv\\text{N}$ rất bền với năng lượng liên kết lớn ($945\\text{ kJ/mol}$)", "Nguyên tử nitrogen có bán kính rất lớn", "Phân tử $\\text{N}_2$ phân cực mạnh", "Nitrogen là một khí hiếm thuộc nhóm $\\text{VIIIA}$"], "Liên kết ba $\\text{N}\\equiv\\text{N}$ cực kì bền vững nên rất khó bị phá vỡ ở nhiệt độ thường.", "biet"),
            mcq("Trong phản ứng tổng hợp ammonia: $\\text{N}_2 + 3\\text{H}_2 \\rightleftharpoons 2\\text{NH}_3$, khí $\\text{N}_2$ đóng vai trò là:", "Chất oxi hóa", ["Chất oxi hóa", "Chất khử", "Vừa là chất oxi hóa vừa là chất khử", "Chất xúc tác"], "Số oxi hóa của $\\text{N}$ giảm từ $0$ (trong $\\text{N}_2$) xuống $-3$ (trong $\\text{NH}_3$), nên $\\text{N}_2$ nhận electron và là chất oxi hóa.", "hieu"),
            short("Để tổng hợp được $0,4\\text{ mol}$ khí $\\text{NH}_3$ với hiệu suất phản ứng đạt $50\\%$, cần đưa vào bình phản ứng tối thiểu bao nhiêu mol khí $\\text{N}_2$ (biết $\\text{H}_2$ lấy dư)?", "0,4", ["0,4", "0.4"], "Theo PTHH $\\text{N}_2 + 3\\text{H}_2 \\rightleftharpoons 2\\text{NH}_3$, lượng $\\text{N}_2$ phản ứng là $\\frac{0,4}{2} = 0,2\\text{ mol}$. Vì $H = 50\\%$ nên $n_{\\text{N}_2\\text{ ban đầu}} = \\frac{0,2}{0,5} = 0,4\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(5, "Ammonia và muối ammonium",
        "Cấu tạo hình chóp tam giác, tính base yếu và tính khử của NH3; tính chất và cách nhận biết muối ammonium (NH4+)",
        "Phân tử ammonia ($\\text{NH}_3$) có dạng hình chóp tam giác với nguyên tử $\\text{N}$ còn một cặp electron chưa liên kết, là chất khí không màu, mùi khai và xốc, nhẹ hơn không khí và tan rất nhiều trong nước (tạo liên kết hydrogen với nước). Về hóa học, $\\text{NH}_3$ có tính base yếu (trong nước nhận $\\text{H}^+$ tạo $\\text{NH}_4^+$ và $\\text{OH}^-$ làm quỳ tím hóa xanh; tác dụng với acid tạo muối ammonium) và tính khử (cháy trong $\\text{O}_2$ tạo $\\text{N}_2$ hoặc tạo $\\text{NO}$ khi có xúc tác $\\text{Pt}$). Muối ammonium (chứa ion $\\text{NH}_4^+$) đều là chất điện li mạnh dễ tan trong nước, kém bền nhiệt và tác dụng với dung dịch kiềm đun nóng giải phóng khí $\\text{NH}_3$ mùi khai.",
        [
            F("Tính base yếu của Ammonia", "\\text{NH}_3 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4^+ + \\text{OH}^-;\\quad \\text{NH}_3 + \\text{HCl} \\rightarrow \\text{NH}_4\\text{Cl}\\text{ (khói trắng)}", "Dung dịch NH3 làm quỳ tím hóa xanh, phenolphthalein hóa hồng"),
            F("Tính khử của Ammonia (đốt cháy có xúc tác Pt)", "4\\text{NH}_3 + 5\\text{O}_2 \\xrightarrow{850^\\circ\\text{C},\\; \\text{Pt}} 4\\text{NO} + 6\\text{H}_2\\text{O}", "Giai đoạn đầu tiên trong quy trình công nghiệp sản xuất HNO3 từ NH3"),
            F("Nhận biết muối Ammonium (NH4+) và Nhiệt phân", "\\text{NH}_4^+ + \\text{OH}^- \\xrightarrow{t^\\circ} \\text{NH}_3\\uparrow + \\text{H}_2\\text{O};\\quad \\text{NH}_4\\text{HCO}_3 \\xrightarrow{t^\\circ} \\text{NH}_3\\uparrow + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}\\uparrow", "Khí NH3 thoát ra làm xanh giấy quỳ tím ẩm"),
        ],
        [
            "Mô tả được cấu tạo phân tử $\\text{NH}_3$ và giải thích được tính tan tốt trong nước, tính base yếu và tính khử của $\\text{NH}_3$",
            "Trình bày được tính chất vật lí, hóa học của muối ammonium (phản ứng với kiềm, phản ứng nhiệt phân)",
            "Nhận biết được ion $\\text{NH}_4^+$ trong dung dịch và nêu được ứng dụng của $\\text{NH}_3$, muối ammonium (phân đạm, bột nở $\\text{NH}_4\\text{HCO}_3$)",
        ],
        "Cho $100\\text{ mL}$ dung dịch $(\\text{NH}_4)_2\\text{SO}_4$ $0,5\\text{ M}$ tác dụng với dung dịch $\\text{NaOH}$ dư, đun nóng. Tính thể tích khí $\\text{NH}_3$ thoát ra ở đkc.",
        "Số mol $(\\text{NH}_4)_2\\text{SO}_4$: $n = 0,1 \\cdot 0,5 = 0,05\\text{ mol}$.\nPhương trình ion rút gọn: $\\text{NH}_4^+ + \\text{OH}^- \\xrightarrow{t^\\circ} \\text{NH}_3\\uparrow + \\text{H}_2\\text{O}$.\nTa có: $n_{\\text{NH}_3} = n_{\\text{NH}_4^+} = 2n_{(\\text{NH}_4)_2\\text{SO}_4} = 2 \\cdot 0,05 = 0,1\\text{ mol}$.\nThể tích khí $\\text{NH}_3$ (đkc): $V = 0,1 \\cdot 24,79 = 2,479\\text{ L}$.",
        "Muối $\\text{NH}_4\\text{HCO}_3$ được dùng làm bột nở trong sản xuất bánh bao vì khi hấp nóng nó phân hủy hoàn toàn thành các chất khí và hơi ($\\text{NH}_3, \\text{CO}_2, \\text{H}_2\\text{O}$) tạo các lỗ xốp làm bánh phồng to.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Nhúng mẩu giấy quỳ tím ẩm vào bình đựng khí ammonia ($\\text{NH}_3$) thì giấy quỳ tím chuyển sang màu gì?", "Màu xanh", ["Màu xanh", "Màu đỏ", "Màu vàng", "Không đổi màu"], "Khí $\\text{NH}_3$ tan trong nước trên giấy quỳ ẩm tạo môi trường kiềm yếu ($\\text{NH}_4^+ + \\text{OH}^-$) làm quỳ tím hóa xanh.", "biet"),
            mcq("Thuốc thử dùng để nhận biết các muối ammonium (chứa ion $\\text{NH}_4^+$) trong dung dịch là:", "Dung dịch kiềm mạnh ($\\text{NaOH}, \\text{KOH}$) đun nóng và giấy quỳ tím ẩm", ["Dung dịch kiềm mạnh ($\\text{NaOH}, \\text{KOH}$) đun nóng và giấy quỳ tím ẩm", "Dung dịch $\\text{HCl}$ loãng", "Dung dịch $\\text{NaCl}$", "Khí $\\text{CO}_2$"], "Khi đun nóng với dung dịch kiềm, muối $\\text{NH}_4^+$ giải phóng khí $\\text{NH}_3$ mùi khai làm xanh giấy quỳ tím ẩm.", "hieu"),
            short("Đun nóng hoàn toàn dung dịch chứa $0,15\\text{ mol}$ $\\text{NH}_4\\text{Cl}$ với dung dịch $\\text{NaOH}$ dư thì thu được tối đa bao nhiêu mol khí $\\text{NH}_3$?", "0,15", ["0,15", "0.15"], "PTHH: $\\text{NH}_4\\text{Cl} + \\text{NaOH} \\xrightarrow{t^\\circ} \\text{NaCl} + \\text{NH}_3\\uparrow + \\text{H}_2\\text{O}$. Số mol $n_{\\text{NH}_3} = n_{\\text{NH}_4\\text{Cl}} = 0,15\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(6, "Một số hợp chất của nitrogen với oxygen",
        "Các oxide của nitrogen (NOx), mưa acid, hiện tượng phú dưỡng (eutrophication) và tính oxi hóa mạnh của nitric acid (HNO3)",
        "Các oxide của nitrogen ($\\text{NO}_x$: $\\text{NO}$ không màu, $\\text{NO}_2$ màu nâu đỏ) sinh ra từ sấm sét và khí thải động cơ đốt trong, là một trong hai tác nhân chính gây mưa acid. Nitric acid ($\\text{HNO}_3$, trong đó $\\text{N}$ có số oxi hóa cực đại $+5$) vừa là một acid mạnh, vừa là một chất oxi hóa rất mạnh: oxi hóa được hầu hết kim loại (trừ $\\text{Au}, \\text{Pt}$) lên số oxi hóa cao nhất và giải phóng các sản phẩm khử ($\\text{NO}_2, \\text{NO}, \\text{N}_2\\text{O}, \\text{N}_2, \\text{NH}_4\\text{NO}_3$) chứ không giải phóng $\\text{H}_2$; lưu ý $\\text{Al}, \\text{Fe}, \\text{Cr}$ bị thụ động hóa trong $\\text{HNO}_3$ đặc, nguội. Hiện tượng phú dưỡng là sự dư thừa dinh dưỡng ($\\text{NO}_3^-, \\text{PO}_4^{3-}$) trong ao hồ làm tảo bùng phát gây cạn kiệt oxygen trong nước.",
        [
            F("Sơ đồ sản xuất Nitric acid trong công nghiệp (3 giai đoạn)", "\\text{NH}_3 \\xrightarrow{+\\text{O}_2,\\text{ Pt, } 850^\\circ\\text{C}} \\text{NO} \\xrightarrow{+\\text{O}_2} \\text{NO}_2 \\xrightarrow{+\\text{O}_2 + \\text{H}_2\\text{O}} \\text{HNO}_3", "4NO2 + O2 + 2H2O -> 4HNO3"),
            F("Kim loại tác dụng với HNO3 (trừ Au, Pt)", "\\text{M} + \\text{HNO}_3 \\rightarrow \\text{M(NO}_3)_n + \\underbrace{(\\text{NO}_2, \\text{NO}, \\text{N}_2\\text{O}, \\text{N}_2, \\text{NH}_4\\text{NO}_3)}_{\\text{Sản phẩm khử}} + \\text{H}_2\\text{O}", "Đặc biệt: Al, Fe, Cr KHÔNG phản ứng với HNO3 đặc, nguội do bị thụ động hóa"),
        ],
        [
            "Nêu được nguồn gốc phát sinh $\\text{NO}_x$, nguyên nhân và hậu quả của hiện tượng mưa acid và hiện tượng phú dưỡng trong ao hồ",
            "Trình bày được cấu tạo phân tử, tính acid mạnh và tính oxi hóa rất mạnh của $\\text{HNO}_3$ đối với kim loại và phi kim",
            "Giải được bài toán kim loại tác dụng với dung dịch $\\text{HNO}_3$ bằng phương pháp bảo toàn electron",
        ],
        "Hòa tan hoàn toàn $5,6\\text{ g}$ sắt ($\\text{Fe} = 56$) bằng dung dịch $\\text{HNO}_3$ đặc, nóng dư, thu được khí $\\text{NO}_2$ màu nâu đỏ (sản phẩm khử duy nhất). Tính thể tích khí $\\text{NO}_2$ ở đkc.",
        "Số mol $\\text{Fe}$: $n_{\\text{Fe}} = \\frac{5,6}{56} = 0,1\\text{ mol}$.\nTrong $\\text{HNO}_3$ dư, $\\text{Fe}$ bị oxi hóa lên $\\text{Fe}^{+3}$ (nhường $3\\text{e}$), còn $\\text{N}^{+5}$ nhận $1\\text{e}$ tạo $\\text{NO}_2$.\nBảo toàn electron: $3n_{\\text{Fe}} = 1 \\cdot n_{\\text{NO}_2} \\Rightarrow n_{\\text{NO}_2} = 0,3\\text{ mol}$.\nThể tích khí $\\text{NO}_2$ (đkc): $V = 0,3 \\cdot 24,79 = 7,437\\text{ L}$.",
        "Nhờ hiện tượng thụ động hóa, người ta có thể dùng các bồn chứa làm bằng nhôm ($\\text{Al}$) hoặc sắt/thép ($\\text{Fe}$) để chuyên chở dung dịch $\\text{HNO}_3$ đặc, nguội.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Kim loại nào sau đây bị thụ động hóa (không phản ứng) trong dung dịch $\\text{HNO}_3$ đặc, nguội?", "Nhôm ($\\text{Al}$) và Sắt ($\\text{Fe}$)", ["Nhôm ($\\text{Al}$) và Sắt ($\\text{Fe}$)", "Đồng ($\\text{Cu}$) và Bạc ($\\text{Ag}$)", "Kẽm ($\\text{Zn}$) và Đồng ($\\text{Cu}$)", "Magnesium ($\\text{Mg}$) và Bạc ($\\text{Ag}$)"], "Ba kim loại $\\text{Al}, \\text{Fe}, \\text{Cr}$ bị thụ động hóa trong $\\text{HNO}_3$ đặc, nguội và $\\text{H}_2\\text{SO}_4$ đặc, nguội.", "biet"),
            mcq("Hiện tượng phú dưỡng (eutrophication) ở các ao, hồ tù đọng xảy ra do nước thải chứa dư thừa hàm lượng các chất dinh dưỡng nào sau đây?", "Các ion nitrate ($\\text{NO}_3^-$) và phosphate ($\\text{PO}_4^{3-}$)", ["Các ion nitrate ($\\text{NO}_3^-$) và phosphate ($\\text{PO}_4^{3-}$)", "Khí oxygen ($\\text{O}_2$) và nitrogen ($\\text{N}_2$)", "Muối ăn ($\\text{NaCl}$) và cát ($\\text{SiO}_2$)", "Kim loại vàng và bạc"], "Sự dư thừa phân bón và chất tẩy rửa chứa hợp chất của $\\text{N}$ và $\\text{P}$ gây hiện tượng phú dưỡng làm tảo nở hoa.", "hieu"),
            short("Hòa tan hoàn toàn $0,1\\text{ mol}$ đồng ($\\text{Cu}$) trong dung dịch $\\text{HNO}_3$ đặc, nóng dư thu được bao nhiêu mol khí $\\text{NO}_2$ (sản phẩm khử duy nhất)?", "0,2", ["0,2", "0.2"], "Bảo toàn electron: $\\text{Cu}$ nhường $2\\text{e}$, $\\text{N}^{+5}$ nhận $1\\text{e}$ tạo $\\text{NO}_2 \\Rightarrow n_{\\text{NO}_2} = 2n_{\\text{Cu}} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(7, "Sulfur và sulfur dioxide",
        "Tính oxi hóa và tính khử của đơn chất lưu huỳnh (S), sulfur dioxide (SO2) và tác hại gây mưa acid của SO2",
        "Nguyên tố sulfur ($\\text{S}, Z = 16$) thuộc ô $16$, chu kì $3$, nhóm $\\text{VIA}$. Đơn chất lưu huỳnh là chất rắn màu vàng, không tan trong nước; với số oxi hóa trung gian $0$, $\\text{S}$ vừa có tính oxi hóa (tác dụng với kim loại và $\\text{H}_2$ xuống số oxi hóa $-2$; đặc biệt tác dụng với thủy ngân $\\text{Hg}$ ngay ở nhiệt độ thường), vừa có tính khử (tác dụng với $\\text{O}_2, \\text{F}_2$ lên $+4, +6$). Sulfur dioxide ($\\text{SO}_2$, số oxi hóa $+4$) là chất khí không màu, mùi hắc, độc, vừa là một oxide acid, vừa có tính oxi hóa (tác dụng với $\\text{H}_2\\text{S}$) và tính khử (làm mất màu dung dịch $\\text{Br}_2, \\text{KMnO}_4$). $\\text{SO}_2$ là tác nhân chính gây mưa acid.",
        [
            F("Tính oxi hóa và tính khử của Lưu huỳnh (S)", "\\underbrace{\\text{Fe} + \\text{S} \\xrightarrow{t^\\circ} \\text{FeS};\\; \\text{Hg} + \\text{S} \\rightarrow \\text{HgS}}_{\\text{S là chất oxi hóa (0 -> -2)}};\\quad \\underbrace{\\text{S} + \\text{O}_2 \\xrightarrow{t^\\circ} \\text{SO}_2}_{\\text{S là chất khử (0 -> +4)}}", "Dùng bột lưu huỳnh rắc lên thủy ngân rơi vãi để thu gom Hg độc hại"),
            F("Tính oxi hóa và tính khử của SO2 (S có số oxi hóa +4)", "\\begin{cases} \\text{Tính oxi hóa: } \\text{SO}_2 + 2\\text{H}_2\\text{S} \\rightarrow 3\\text{S}\\downarrow + 2\\text{H}_2\\text{O} \\\\ \\text{Tính khử: } \\text{SO}_2 + \\text{Br}_2 + 2\\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{SO}_4 + 2\\text{HBr} \\end{cases}", "Khí SO2 làm mất màu dung dịch nước bromine"),
        ],
        [
            "Trình bày được trạng thái tự nhiên, tính chất vật lí và giải thích được tính vừa oxi hóa vừa khử của đơn chất lưu huỳnh ($\\text{S}$)",
            "Giải thích được tính oxi hóa và tính khử của $\\text{SO}_2$ và viết được các phương trình hóa học minh họa",
            "Nêu được nguồn phát thải $\\text{SO}_2$, cơ chế hình thành mưa acid và các biện pháp giảm thiểu phát thải $\\text{SO}_2$",
        ],
        "Dẫn từ từ khí $\\text{SO}_2$ vào $100\\text{ mL}$ dung dịch nước $\\text{Br}_2$ $0,1\\text{ M}$ cho đến khi dung dịch vừa mất màu hoàn toàn. Tính số mol $\\text{SO}_2$ đã phản ứng và số mol $\\text{H}_2\\text{SO}_4$ tạo thành.",
        "Số mol $\\text{Br}_2$: $n_{\\text{Br}_2} = 0,1 \\cdot 0,1 = 0,01\\text{ mol}$.\nPTHH: $\\text{SO}_2 + \\text{Br}_2 + 2\\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{SO}_4 + 2\\text{HBr}$.\nTheo PTHH: $n_{\\text{SO}_2} = n_{\\text{H}_2\\text{SO}_4} = n_{\\text{Br}_2} = 0,01\\text{ mol}$.",
        "Khi nhiệt kế thủy ngân không may bị vỡ, người ta rắc ngay bột lưu huỳnh ($\\text{S}$) lên các giọt thủy ngân để tạo thành $\\text{HgS}$ rắn không bay hơi ngay ở nhiệt độ thường, tránh hít phải hơi thủy ngân cực độc.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Khi nhiệt kế thủy ngân ($\\text{Hg}$) bị vỡ, hóa chất thông dụng được rắc lên để khử độc thủy ngân ngay ở nhiệt độ thường là:", "Bột lưu huỳnh ($\\text{S}$)", ["Bột lưu huỳnh ($\\text{S}$)", "Muối ăn ($\\text{NaCl}$)", "Cát khô ($\\text{SiO}_2$)", "Bột sắt ($\\text{Fe}$)"], "$\\text{Hg}$ tác dụng với $\\text{S}$ ngay ở nhiệt độ thường tạo $\\text{HgS}$ rắn không bay hơi: $\\text{Hg} + \\text{S} \\rightarrow \\text{HgS}$.", "biet"),
            mcq("Trong phản ứng: $\\text{SO}_2 + 2\\text{H}_2\\text{S} \\rightarrow 3\\text{S}\\downarrow + 2\\text{H}_2\\text{O}$, khí $\\text{SO}_2$ đóng vai trò là:", "Chất oxi hóa", ["Chất oxi hóa", "Chất khử", "Môi trường", "Chất xúc tác"], "Số oxi hóa của $\\text{S}$ trong $\\text{SO}_2$ giảm từ $+4$ xuống $0$, nên $\\text{SO}_2$ là chất oxi hóa.", "hieu"),
            short("Đốt cháy hoàn toàn $6,4\\text{ g}$ lưu huỳnh ($\\text{S} = 32$) trong khí $\\text{O}_2$ dư thu được bao nhiêu mol khí $\\text{SO}_2$?", "0,2", ["0,2", "0.2"], "Số mol $n_{\\text{SO}_2} = n_{\\text{S}} = \\frac{6,4}{32} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(8, "Sulfuric acid và muối sulfate",
        "Cách pha loãng H2SO4 đặc an toàn, tính oxi hóa mạnh và tính háo nước của H2SO4 đặc, sản xuất H2SO4 (phương pháp tiếp xúc) và nhận biết ion SO4^2-",
        "Sulfuric acid ($\\text{H}_2\\text{SO}_4$) là chất lỏng sánh như dầu, không màu, không bay hơi và tan vô hạn trong nước tỏa rất nhiều nhiệt; do đó khi pha loãng PHẢI rót từ từ acid đặc vào nước và khuấy nhẹ, tuyệt đối không làm ngược lại. Dung dịch $\\text{H}_2\\text{SO}_4$ loãng có đầy đủ tính chất của một acid mạnh. Dung dịch $\\text{H}_2\\text{SO}_4$ đặc có tính háo nước mạnh (than hóa đường saccharose) và tính oxi hóa rất mạnh: oxi hóa hầu hết kim loại (trừ $\\text{Au}, \\text{Pt}$) lên số oxi hóa cao nhất tạo sản phẩm khử $\\text{SO}_2, \\text{S}, \\text{H}_2\\text{S}$ ($\\text{Al}, \\text{Fe}, \\text{Cr}$ bị thụ động hóa trong $\\text{H}_2\\text{SO}_4$ đặc, nguội). Nhận biết ion $\\text{SO}_4^{2-}$ bằng dung dịch $\\text{Ba}^{2+}$ tạo kết tủa trắng $\\text{BaSO}_4$ không tan trong acid.",
        [
            F("Tính oxi hóa mạnh và tính háo nước của H2SO4 đặc", "\\begin{cases} \\text{Cu} + 2\\text{H}_2\\text{SO}_{4\\text{ đặc}} \\xrightarrow{t^\\circ} \\text{CuSO}_4 + \\text{SO}_2\\uparrow + 2\\text{H}_2\\text{O} \\\\ \\text{C}_{12}\\text{H}_{22}\\text{O}_{11} \\xrightarrow{\\text{H}_2\\text{SO}_4\\text{ đặc}} 12\\text{C} + 11\\text{H}_2\\text{O} \\end{cases}", "Al, Fe, Cr bị thụ động hóa trong H2SO4 đặc, nguội"),
            F("Sản xuất H2SO4 công nghiệp (Phương pháp tiếp xúc - 3 giai đoạn)", "\\text{S (hoặc FeS}_2\\text{)} \\xrightarrow{+\\text{O}_2, t^\\circ} \\text{SO}_2 \\underset{450^\\circ\\text{C},\\; \\text{V}_2\\text{O}_5}{\\overset{+\\text{O}_2}{\\rightleftharpoons}} \\text{SO}_3 \\xrightarrow{+\\text{H}_2\\text{SO}_4\\text{ đặc}} \\text{H}_2\\text{SO}_4\\cdot n\\text{SO}_3\\text{ (Oleum)}", "Dùng H2SO4 98% hấp thụ SO3 tạo oleum rồi mới pha loãng bằng nước"),
            F("Nhận biết ion Sulfate (SO4^2-)", "\\text{Ba}^{2+} + \\text{SO}_4^{2-} \\rightarrow \\text{BaSO}_4\\downarrow\\text{ (kết tủa trắng bền trong acid)}", "Dùng dung dịch BaCl2 hoặc Ba(OH)2, Ba(NO3)2 để nhận biết"),
        ],
        [
            "Trình bày được nguyên tắc pha loãng $\\text{H}_2\\text{SO}_4$ đặc an toàn và cách sơ cứu khi bị bỏng acid",
            "Phân biệt được tính chất hóa học của $\\text{H}_2\\text{SO}_4$ loãng (tính acid) và $\\text{H}_2\\text{SO}_4$ đặc (tính oxi hóa mạnh và tính háo nước)",
            "Trình bày được $3$ giai đoạn sản xuất $\\text{H}_2\\text{SO}_4$ theo phương pháp tiếp xúc và cách nhận biết ion $\\text{SO}_4^{2-}$",
        ],
        "Hòa tan hoàn toàn $12,8\\text{ g}$ đồng ($\\text{Cu} = 64$) vào dung dịch $\\text{H}_2\\text{SO}_4$ đặc, nóng dư. Tính thể tích khí $\\text{SO}_2$ (sản phẩm khử duy nhất, ở đkc) thoát ra.",
        "Số mol $\\text{Cu}$: $n_{\\text{Cu}} = \\frac{12,8}{64} = 0,2\\text{ mol}$.\nPTHH: $\\text{Cu} + 2\\text{H}_2\\text{SO}_{4\\text{ đặc}} \\xrightarrow{t^\\circ} \\text{CuSO}_4 + \\text{SO}_2\\uparrow + 2\\text{H}_2\\text{O}$.\nTheo PTHH: $n_{\\text{SO}_2} = n_{\\text{Cu}} = 0,2\\text{ mol} \\Rightarrow V_{\\text{SO}_2} = 0,2 \\cdot 24,79 = 4,958\\text{ L}$.",
        "Muối $\\text{BaSO}_4$ không tan trong nước và trong dịch vị dạ dày (chứa $\\text{HCl}$) đồng thời cản tia X rất tốt, nên được dùng làm 'thuốc cản quang' cho bệnh nhân uống trước khi chụp X-quang đường tiêu hóa.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Cách pha loãng dung dịch $\\text{H}_2\\text{SO}_4$ đặc nào sau đây là ĐÚNG và an toàn?", "Rót từ từ acid $\\text{H}_2\\text{SO}_4$ đặc vào bình đựng nước và khuấy nhẹ bằng đũa thủy tinh", ["Rót từ từ acid $\\text{H}_2\\text{SO}_4$ đặc vào bình đựng nước và khuấy nhẹ bằng đũa thủy tinh", "Rót thật nhanh nước lạnh vào bình đựng acid $\\text{H}_2\\text{SO}_4$ đặc", "Đổ cùng lúc nước và acid đặc vào ống nghiệm đậy kín", "Đun sôi acid đặc rồi đổ nước vào"], "Vì $\\text{H}_2\\text{SO}_4$ đặc nặng hơn nước và tỏa nhiệt rất lớn khi tan, rót từ từ acid vào nước giúp nhiệt phân tán đều không gây bắn acid.", "biet"),
            mcq("Thuốc thử dùng để nhận biết ion sulfate ($\\text{SO}_4^{2-}$) trong dung dịch là:", "Dung dịch muối $\\text{BaCl}_2$ (hoặc $\\text{Ba(NO}_3)_2$) trong môi trường acid loãng", ["Dung dịch muối $\\text{BaCl}_2$ (hoặc $\\text{Ba(NO}_3)_2$) trong môi trường acid loãng", "Dung dịch $\\text{NaCl}$", "Dung dịch $\\text{NaOH}$", "Quỳ tím"], "Ion $\\text{Ba}^{2+}$ kết hợp với $\\text{SO}_4^{2-}$ tạo kết tủa trắng $\\text{BaSO}_4$ không tan trong các dung dịch acid.", "hieu"),
            short("Cho dung dịch chứa $0,1\\text{ mol}$ $\\text{H}_2\\text{SO}_4$ tác dụng với lượng dư dung dịch $\\text{BaCl}_2$. Tính khối lượng kết tủa $\\text{BaSO}_4$ ($M = 233$) thu được (theo đơn vị gam).", "23,3", ["23,3", "23.3"], "Số mol $n_{\\text{BaSO}_4} = n_{\\text{H}_2\\text{SO}_4} = 0,1\\text{ mol} \\Rightarrow m_{\\text{BaSO}_4} = 0,1 \\cdot 233 = 23,3\\text{ g}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 3: ĐẠI CƯƠNG VỀ HÓA HỌC HỮU CƠ
# =========================================================================
CH3_ID = "hoa11_ch3"
CH3_TITLE = "Chương 3: Đại cương về hóa học hữu cơ"
CH3_DESC = "Nhóm chức, phổ hồng ngoại (IR), phương pháp tách và tinh chế, công thức phân tử (phổ MS) và cấu tạo hóa học (đồng đẳng, đồng phân)"

CH3_LESSONS = [
    bai(9, "Hợp chất hữu cơ và hóa học hữu cơ. Phổ hồng ngoại (IR)",
        "Đặc điểm chung của hợp chất hữu cơ, phân loại nhóm chức và xác định nhóm chức bằng phổ hồng ngoại (IR)",
        "Các hợp chất hữu cơ có liên kết chủ yếu là liên kết cộng hóa trị, nhiệt độ nóng chảy và nhiệt độ sôi thấp, thường không tan trong nước và dễ cháy. Nhóm chức là nguyên tử hoặc nhóm nguyên tử gây ra những tính chất hóa học đặc trưng của hợp chất hữu cơ: alcohol ($-\\text{OH}$), ether ($-\\text{O}-$), amine ($-\\text{NH}_2$), aldehyde ($-\\text{CHO}$), ketone ($-\\text{CO}-$), carboxylic acid ($-\\text{COOH}$), ester ($-\\text{COO}-$). Phổ hồng ngoại (IR) cho phép nhận biết sự có mặt của các nhóm chức dựa vào số sóng hấp thụ đặc trưng ($\\text{cm}^{-1}$): nhóm $-\\text{OH}$ alcohol ($3600 - 3200\\text{ cm}^{-1}$, tù rộng), nhóm $\\text{C}=\\text{O}$ ($1750 - 1680\\text{ cm}^{-1}$, nhọn mạnh).",
        [
            F("Các nhóm chức hữu cơ quan trọng", "\\begin{cases} \\text{Alcohol: } -\\text{OH};\\quad \\text{Aldehyde: } -\\text{CHO};\\quad \\text{Ketone: } -\\text{C(=O)}- \\\\ \\text{Carboxylic acid: } -\\text{COOH};\\quad \\text{Ester: } -\\text{COO}-;\\quad \\text{Amine: } -\\text{NH}_2 \\end{cases}", "Nhóm chức quyết định tính chất hóa học đặc trưng của phân tử"),
            F("Số sóng hấp thụ đặc trưng trên Phổ hồng ngoại (IR)", "\\begin{cases} \\text{Liên kết } \\text{O}-\\text{H (alcohol)}: 3650 - 3200\\text{ cm}^{-1}\\text{ (đỉnh tù, rộng)} \\\\ \\text{Liên kết } \\text{C}=\\text{O (aldehyde, ketone, acid, ester)}: 1750 - 1680\\text{ cm}^{-1}\\text{ (đỉnh nhọn, mạnh)} \\\\ \\text{Liên kết } \\text{O}-\\text{H (trong -COOH)}: 3300 - 2500\\text{ cm}^{-1}\\text{ (rất rộng)} \\end{cases}", "Trục hoành phổ IR là số sóng (cm^-1), trục tung là độ truyền qua (%)"),
        ],
        [
            "Nêu được đặc điểm chung của hợp chất hữu cơ và nhận diện được các nhóm chức cơ bản ($-\\text{OH}, -\\text{CHO}, -\\text{CO}-, -\\text{COOH}, -\\text{COO}-, -\\text{NH}_2$)",
            "Dự đoán được sự có mặt của các nhóm chức thông dụng dựa vào tín hiệu số sóng đặc trưng trên phổ hồng ngoại (IR)",
            "Phân biệt được phổ IR của alcohol, aldehyde/ketone, carboxylic acid và ester",
        ],
        "Một hợp chất hữu cơ $X$ có công thức phân tử $\\text{C}_2\\text{H}_4\\text{O}_2$. Trên phổ hồng ngoại (IR) của $X$ có tín hiệu hấp thụ mạnh ở $1715\\text{ cm}^{-1}$ (liên kết $\\text{C}=\\text{O}$) và một dải hấp thụ rất rộng ở vùng $3000 - 2500\\text{ cm}^{-1}$ (liên kết $\\text{O}-\\text{H}$ của nhóm carboxyl). Xác định công thức cấu tạo của $X$.",
        "Tín hiệu ở $1715\\text{ cm}^{-1}$ kết hợp với dải rộng $3000 - 2500\\text{ cm}^{-1}$ chứng tỏ $X$ có nhóm chức carboxylic acid ($-\\text{COOH}$).\nVới công thức phân tử $\\text{C}_2\\text{H}_4\\text{O}_2$, công thức cấu tạo của $X$ là $\\text{CH}_3-\\text{COOH}$ (acetic acid).",
        "Phổ hồng ngoại (IR) là công cụ không thể thiếu trong phòng thí nghiệm kiểm nghiệm dược phẩm, giúp xác định nhanh độ tinh khiết và cấu trúc nhóm chức của hoạt chất thuốc chỉ trong vài chục giây.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Nhóm chức $-\\text{CHO}$ là nhóm chức đặc trưng của loại hợp chất hữu cơ nào sau đây?", "Aldehyde", ["Aldehyde", "Alcohol", "Carboxylic acid", "Ketone"], "Nhóm $-\\text{CHO}$ là nhóm chức aldehyde (như $\\text{HCHO}, \\text{CH}_3\\text{CHO}$).", "biet"),
            mcq("Trên phổ hồng ngoại (IR), một tín hiệu hấp thụ mạnh và nhọn nằm trong vùng số sóng $1750 - 1680\\text{ cm}^{-1}$ đặc trưng cho liên kết nào?", "Liên kết đôi $\\text{C}=\\text{O}$ (nhóm carbonyl)", ["Liên kết đôi $\\text{C}=\\text{O}$ (nhóm carbonyl)", "Liên kết đơn $\\text{O}-\\text{H}$ của alcohol", "Liên kết đơn $\\text{C}-\\text{C}$", "Liên kết đơn $\\text{C}-\\text{H}$"], "Liên kết $\\text{C}=\\text{O}$ trong aldehyde, ketone, carboxylic acid và ester luôn có đỉnh hấp thụ rất đặc trưng ở vùng $1750 - 1680\\text{ cm}^{-1}$.", "hieu"),
            short("Trong các chất: (1) $\\text{CH}_3\\text{CH}_2\\text{OH}$, (2) $\\text{CH}_3\\text{OCH}_3$, (3) $\\text{CH}_4$, chất nào có đỉnh hấp thụ tù, rộng đặc trưng ở vùng $3600 - 3200\\text{ cm}^{-1}$ trên phổ IR (nhập số thứ tự)?", "1", ["1"], "Chỉ có $\\text{CH}_3\\text{CH}_2\\text{OH}$ (số 1) chứa nhóm $-\\text{OH}$ alcohol hấp thụ ở vùng $3600 - 3200\\text{ cm}^{-1}$.", "vandung"),
        ]
    ),
    bai(10, "Phương pháp tách biệt và tinh chế hợp chất hữu cơ",
        "Nguyên tắc và cách tiến hành 4 phương pháp: chưng cất, chiết (lỏng - lỏng, lỏng - rắn), kết tinh và sắc kí cột",
        "Bốn phương pháp vật lí phổ biến để tách biệt và tinh chế hợp chất hữu cơ gồm: (1) Phương pháp chưng cất: tách các chất lỏng có nhiệt độ sôi khác nhau đáng kể (ví dụ nấu rượu gạo, chưng cất dầu mỏ); (2) Phương pháp chiết: tách các chất dựa vào độ tan khác nhau trong hai dung môi không hòa tan vào nhau (chiết lỏng - lỏng bằng phễu chiết để tách tinh dầu ra khỏi nước; chiết lỏng - rắn như ngâm rượu thuốc, pha trà); (3) Phương pháp kết tinh: tách và tinh chế chất rắn dựa vào sự khác nhau về độ tan của chất rắn theo nhiệt độ (làm đường phèn); (4) Phương pháp sắc kí cột: tách các chất dựa vào sự phân bố khác nhau giữa pha động và pha tĩnh.",
        [
            F("Nguyên tắc 4 phương pháp tách và tinh chế", "\\begin{cases} \\text{Chưng cất: dựa vào sự khác nhau về Nhiệt độ sôi } (t_s) \\\\ \\text{Chiết: dựa vào sự khác nhau về Độ tan trong các dung môi không trộn lẫn} \\\\ \\text{Kết tinh: dựa vào sự thay đổi Độ tan của chất rắn theo nhiệt độ} \\\\ \\text{Sắc kí cột: dựa vào khả năng Hấp phụ và Hòa tan khác nhau giữa pha tĩnh và pha động} \\end{cases}", "Trong phễu chiết: chất lỏng có khối lượng riêng nhỏ hơn (nhẹ hơn) luôn nổi ở lớp trên"),
        ],
        [
            "Trình bày được nguyên tắc và cách thức tiến hành các phương pháp: chưng cất, chiết, kết tinh và sơ lược về sắc kí cột",
            "Lựa chọn được phương pháp thích hợp để tách biệt và tinh chế một hỗn hợp hữu cơ cụ thể",
            "Vận dụng kiến thức để giải thích các quá trình thực tế như nấu rượu, tách tinh dầu sả/bưởi, ngâm rượu dược liệu, kết tinh đường",
        ],
        "Hỗn hợp gồm dầu ăn và nước không tan vào nhau và tách thành hai lớp trong phễu chiết. Hãy cho biết phương pháp dùng để tách riêng hai chất lỏng này và chất nào chảy ra khỏi khóa phễu chiết trước?",
        "- Dùng phương pháp chiết lỏng - lỏng bằng phễu chiết.\n- Vì dầu ăn nhẹ hơn nước ($D_{\\text{dầu}} \\approx 0,8 - 0,9\\text{ g/mL} < D_{\\text{nước}} = 1\\text{ g/mL}$) nên nước nằm ở lớp dưới và dầu ăn nổi ở lớp trên. Khi mở khóa phễu chiết, lớp nước ở dưới sẽ chảy ra trước.",
        "Nghề chưng cất tinh dầu tràm, tinh dầu sả ở Việt Nam sử dụng phương pháp chưng cất lôi cuốn hơi nước, sau đó dùng phương pháp chiết để tách lớp tinh dầu nhẹ nổi phía trên mặt nước.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Phương pháp chưng cất dùng để tách các chất lỏng ra khỏi hỗn hợp dựa trên sự khác nhau về tính chất vật lí nào?", "Nhiệt độ sôi của các chất ở một áp suất nhất định", ["Nhiệt độ sôi của các chất ở một áp suất nhất định", "Màu sắc của các chất lỏng", "Độ dẫn điện của dung dịch", "Khả năng hấp phụ trên cột silica gel"], "Chưng cất dựa vào sự khác nhau về nhiệt độ sôi: chất có nhiệt độ sôi thấp hơn bay hơi trước rồi được làm lạnh ngưng tụ.", "biet"),
            mcq("Việc ngâm các vị thuốc Bắc hoặc nhân sâm vào rượu trắng để lấy các hoạt chất quý tan vào rượu thuộc phương pháp nào?", "Chiết lỏng - rắn", ["Chiết lỏng - rắn", "Chiết lỏng - lỏng", "Chưng cất phân đoạn", "Kết tinh lại"], "Dùng dung môi lỏng (rượu) để hòa tan và tách chất hữu cơ ra khỏi hỗn hợp rắn (dược liệu) gọi là chiết lỏng - rắn.", "hieu"),
            short("Cho $3$ quá trình: (1) Nấu rượu uống từ cơm rượu đã lên men; (2) Làm đường kết tinh từ nước mía cô đặc; (3) Tách lớp tinh dầu bưởi nổi trên mặt nước bằng phễu chiết. Quá trình nào sử dụng phương pháp chưng cất (nhập số thứ tự)?", "1", ["1"], "Nấu rượu (số 1) dựa vào nhiệt độ sôi của $\\text{C}_2\\text{H}_5\\text{OH}$ ($78,3^\\circ\\text{C}$) thấp hơn nước ($100^\\circ\\text{C}$), là phương pháp chưng cất.", "vandung"),
        ]
    ),
    bai(11, "Công thức phân tử hợp chất hữu cơ",
        "Công thức đơn giản nhất (CTĐGN), công thức phân tử (CTPT), xác định phân tử khối bằng phổ khối lượng (MS) và tính toán từ thành phần phần trăm",
        "Công thức phân tử (CTPT) cho biết số lượng nguyên tử của mỗi nguyên tố trong phân tử (ví dụ glucose là $\\text{C}_6\\text{H}_{12}\\text{O}_6$), còn công thức đơn giản nhất (CTĐGN) cho biết tỉ lệ tối giản về số nguyên tử của các nguyên tố trong phân tử (ví dụ của glucose là $\\text{CH}_2\\text{O}$). Với hợp chất $\\text{C}_x\\text{H}_y\\text{O}_z\\text{N}_t$, tỉ lệ $x : y : z : t$ bằng tỉ lệ số mol nguyên tử. Ngày nay, phân tử khối $M$ của hợp chất hữu cơ được xác định nhanh chóng và chính xác bằng phổ khối lượng (MS) dựa trên giá trị $m/z$ của mảnh ion phân tử $[\\text{M}]^+$ (thường là peak có giá trị $m/z$ lớn nhất trên phổ MS).",
        [
            F("Thiết lập Công thức đơn giản nhất cho CxHyOzNt", "x : y : z : t = n_{\\text{C}} : n_{\\text{H}} : n_{\\text{O}} : n_{\\text{N}} = \\frac{\\%m_{\\text{C}}}{12} : \\frac{\\%m_{\\text{H}}}{1} : \\frac{\\%m_{\\text{O}}}{16} : \\frac{\\%m_{\\text{N}}}{14}", "Với %mO = 100% - (%mC + %mH + %mN)"),
            F("Thiết lập trực tiếp Công thức phân tử khi biết M (từ phổ MS)", "\\frac{12x}{\\%m_{\\text{C}}} = \\frac{y}{\\%m_{\\text{H}}} = \\frac{16z}{\\%m_{\\text{O}}} = \\frac{M}{100\\%}", "M được lấy bằng giá trị m/z của peak ion phân tử [M]+ trên phổ khối lượng (MS)"),
        ],
        [
            "Phân biệt được công thức phân tử (CTPT) và công thức đơn giản nhất (CTĐGN) của hợp chất hữu cơ",
            "Xác định được phân tử khối $M$ của hợp chất hữu cơ từ tín hiệu mảnh ion phân tử $[\\text{M}]^+$ trên phổ khối lượng (MS)",
            "Lập được công thức đơn giản nhất và công thức phân tử từ số liệu phân tích phần trăm khối lượng nguyên tố và phổ MS",
        ],
        "Hợp chất hữu cơ $X$ có thành phần phần trăm khối lượng gồm $54,55\\%$ $\\text{C}$; $9,09\\%$ $\\text{H}$; còn lại là $\\text{O}$. Trên phổ khối lượng (MS) của $X$, peak ion phân tử $[\\text{M}]^+$ có giá trị $m/z = 88$. Tìm công thức phân tử của $X$.",
        "- Phần trăm khối lượng $\\text{O}$: $\\%m_{\\text{O}} = 100\\% - (54,55\\% + 9,09\\%) = 36,36\\%$.\n- Từ phổ MS ta có phân tử khối $M_X = 88\\text{ g/mol}$.\n- Gọi CTPT của $X$ là $\\text{C}_x\\text{H}_y\\text{O}_z$: $x = \\frac{88 \\cdot 54,55}{12 \\cdot 100} = 4$; $y = \\frac{88 \\cdot 9,09}{1 \\cdot 100} = 8$; $z = \\frac{88 \\cdot 36,36}{16 \\cdot 100} = 2$.\nVậy công thức phân tử của $X$ là $\\text{C}_4\\text{H}_8\\text{O}_2$.",
        "Kết hợp phổ khối lượng (MS) để tìm công thức phân tử và phổ hồng ngoại (IR) để xác định nhóm chức giúp các nhà hóa học giải mã cấu trúc các hợp chất tự nhiên mới chỉ từ vài miligam mẫu.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Công thức đơn giản nhất của glucose (có công thức phân tử $\\text{C}_6\\text{H}_{12}\\text{O}_6$) là:", "$\\text{CH}_2\\text{O}$", ["$\\text{CH}_2\\text{O}$", "$\\text{C}_2\\text{H}_4\\text{O}_2$", "$\\text{C}_3\\text{H}_6\\text{O}_3$", "$\\text{C}_6\\text{H}_{12}\\text{O}_6$"], "Chia tỉ lệ $6 : 12 : 6$ cho ước chung lớn nhất là $6$ ta được tỉ lệ tối giản $1 : 2 : 1$, tức $\\text{CH}_2\\text{O}$.", "biet"),
            mcq("Trên phổ khối lượng (MS) của một hợp chất hữu cơ $A$, peak ion phân tử $[\\text{M}]^+$ có giá trị $m/z = 60$. Phân tử khối của hợp chất $A$ bằng:", "$60\\text{ amu}$", ["$60\\text{ amu}$", "$30\\text{ amu}$", "$120\\text{ amu}$", "$15\\text{ amu}$"], "Giá trị $m/z$ của peak ion phân tử $[\\text{M}]^+$ (với điện tích $z = +1$) chính bằng phân tử khối $M$ của chất.", "hieu"),
            short("Một hydrocarbon $X$ có công thức đơn giản nhất là $\\text{CH}_3$. Biết phân tử khối của $X$ xác định từ phổ MS là $30$. Số nguyên tử hydrogen trong một phân tử $X$ là bao nhiêu?", "6", ["6"], "Gọi CTPT của $X$ là $(\\text{CH}_3)_n$: $15n = 30 \\Rightarrow n = 2 \\Rightarrow$ CTPT là $\\text{C}_2\\text{H}_6$ (có $6$ nguyên tử $\\text{H}$).", "vandung"),
        ]
    ),
    bai(12, "Cấu tạo hóa học hợp chất hữu cơ",
        "Thuyết cấu tạo hóa học Butlerov, khái niệm đồng đẳng, đồng phân (đồng phân cấu tạo và đồng phân hình học cis - trans) và độ bất bão hòa k",
        "Theo thuyết cấu tạo hóa học: Trong phân tử hợp chất hữu cơ, các nguyên tử liên kết với nhau theo đúng hóa trị và theo một thứ tự nhất định; thứ tự liên kết đó gọi là cấu tạo hóa học; sự thay đổi thứ tự liên kết sẽ tạo ra hợp chất khác. Đồng đẳng là những hợp chất có thành phần phân tử hơn kém nhau một hay nhiều nhóm $-\\text{CH}_2-$ nhưng có tính chất hóa học tương tự nhau. Đồng phân là những hợp chất khác nhau nhưng có cùng công thức phân tử, gồm đồng phân cấu tạo (đồng phân mạch carbon, đồng phân vị trí liên kết bội/nhóm chức, đồng phân loại nhóm chức) và đồng phân lập thể (cis - trans). Độ bất bão hòa $k$ cho biết tổng số liên kết $\\pi$ và số vòng trong phân tử.",
        [
            F("Công thức tính Độ bất bão hòa (k = pi + v) của CxHyOzNtXu", "k = \\pi + v = \\frac{2x + 2 + t - y - u}{2}", "Với X là halogen (F, Cl, Br, I). Nguyên tố O (hóa trị II) không ảnh hưởng đến giá trị của k"),
            F("Phân loại Đồng phân cấu tạo", "\\text{Đồng phân cấu tạo} = \\begin{cases} \\text{Đồng phân mạch carbon (không nhánh / có nhánh)} \\\\ \\text{Đồng phân vị trí nhóm chức hoặc liên kết bội} \\\\ \\text{Đồng phân loại nhóm chức (ví dụ alcohol và ether)} \\end{cases}", "Ngoài ra còn có đồng phân hình học (cis - trans) khi có liên kết đôi C=C hoặc vòng"),
        ],
        [
            "Trình bày được nội dung thuyết cấu tạo hóa học của Butlerov và viết được công thức cấu tạo đầy đủ, thu gọn, khung phân tử",
            "Phân biệt được hiện tượng đồng đẳng và hiện tượng đồng phân; xác định được các loại đồng phân cấu tạo",
            "Vận dụng được công thức tính độ bất bão hòa $k$ để viết đủ số đồng phân ứng với một công thức phân tử cho trước",
        ],
        "Tính độ bất bão hòa $k$ và viết tất cả các đồng phân cấu tạo (gồm cả alcohol và ether) ứng với công thức phân tử $\\text{C}_3\\text{H}_8\\text{O}$.",
        "- Độ bất bão hòa: $k = \\frac{2 \\cdot 3 + 2 - 8}{2} = 0$ (phân tử chỉ chứa liên kết đơn, mạch hở).\n- Các đồng phân cấu tạo của $\\text{C}_3\\text{H}_8\\text{O}$ (có $3$ đồng phân):\n  1. $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{OH}$ (propan-1-ol)\n  2. $\\text{CH}_3-\\text{CH(OH)}-\\text{CH}_3$ (propan-2-ol)\n  3. $\\text{CH}_3-\\text{O}-\\text{CH}_2-\\text{CH}_3$ (ethyl methyl ether).",
        "Hai chất $\\text{C}_2\\text{H}_5\\text{OH}$ (cồn y tế, thể lỏng) và $\\text{CH}_3\\text{OCH}_3$ (dimethyl ether, thể khí dùng làm chất đẩy bình xịt) có cùng công thức phân tử $\\text{C}_2\\text{H}_6\\text{O}$ nhưng thứ tự liên kết khác nhau nên tính chất hoàn toàn khác nhau.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Các chất trong dãy nào sau đây thuộc cùng một dãy đồng đẳng?", "$\\text{CH}_4,\\; \\text{C}_2\\text{H}_6,\\; \\text{C}_3\\text{H}_8,\\; \\text{C}_4\\text{H}_{10}$", ["$\\text{CH}_4,\\; \\text{C}_2\\text{H}_6,\\; \\text{C}_3\\text{H}_8,\\; \\text{C}_4\\text{H}_{10}$", "$\\text{CH}_4,\\; \\text{C}_2\\text{H}_4,\\; \\text{C}_2\\text{H}_2$", "$\\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{OCH}_3$", "$\\text{CH}_3\\text{CHO},\\; \\text{CH}_3\\text{COOH}$"], "Các chất $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8, \\text{C}_4\\text{H}_{10}$ đều là alkane, hơn kém nhau các nhóm $-\\text{CH}_2-$ và có tính chất tương tự nhau.", "biet"),
            mcq("Hai chất $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{OH}$ và $\\text{CH}_3-\\text{CH(OH)}-\\text{CH}_3$ là hai đồng phân thuộc loại nào?", "Đồng phân vị trí nhóm chức", ["Đồng phân vị trí nhóm chức", "Đồng phân mạch carbon", "Đồng phân loại nhóm chức", "Đồng phân hình học cis - trans"], "Cả hai chất đều có mạch $3$ carbon không nhánh và cùng nhóm chức $-\\text{OH}$, chỉ khác nhau vị trí nhóm $-\\text{OH}$ ở $\\text{C}_1$ và $\\text{C}_2$.", "hieu"),
            short("Ứng với công thức phân tử $\\text{C}_4\\text{H}_{10}$ có bao nhiêu đồng phân cấu tạo alkane?", "2", ["2"], "Có $2$ đồng phân: mạch thẳng $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$ (butane) và mạch nhánh $\\text{CH}_3-\\text{CH(CH}_3)-\\text{CH}_3$ (isobutane / 2-methylpropane).", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 4: HYDROCARBON
# =========================================================================
CH4_ID = "hoa11_ch4"
CH4_TITLE = "Chương 4: Hydrocarbon"
CH4_DESC = "Alkane, hydrocarbon không no (alkene, alkyne) và hydrocarbon thơm (arene: benzene, toluene, styrene)"

CH4_LESSONS = [
    bai(13, "Alkane",
        "Danh pháp thay thế IUPAC, bậc carbon, phản ứng thế halogen, cracking, reforming và đốt cháy alkane",
        "Alkane (paraffin) là các hydrocarbon no mạch hở có công thức chung $\\text{C}_n\\text{H}_{2n+2}$ ($n \\ge 1$, độ bất bão hòa $k = 0$). Bậc của nguyên tử carbon bằng số nguyên tử carbon liên kết trực tiếp với nó. Về tính chất hóa học, do chỉ chứa các liên kết $\\sigma$ bền vững nên ở điều kiện thường alkane tương đối trơ (không làm mất màu dung dịch $\\text{Br}_2$ hay $\\text{KMnO}_4$), phản ứng đặc trưng là: (1) Phản ứng thế halogen khi chiếu sáng hoặc đun nóng (nguyên tử $\\text{H}$ ở carbon bậc cao hơn dễ bị thế hơn tạo sản phẩm chính); (2) Phản ứng cracking (bẻ gãy mạch carbon); (3) Phản ứng reforming (chuyển mạch thẳng thành mạch nhánh hoặc vòng thơm làm tăng chỉ số octane của xăng); (4) Phản ứng oxi hóa (đốt cháy tạo $n_{\\text{H}_2\\text{O}} > n_{\\text{CO}_2}$).",
        [
            F("Phản ứng thế Halogen (quy tắc thế vào C bậc cao)", "\\text{CH}_3-\\text{CH}_2-\\text{CH}_3 + \\text{Br}_2 \\xrightarrow{t^\\circ\\text{ hoặc } as} \\begin{cases} \\text{CH}_3-\\text{CHBr}-\\text{CH}_3 + \\text{HBr}\\text{ (sản phẩm chính: 97\\%)} \\\\ \\text{CH}_3-\\text{CH}_2-\\text{CH}_2\\text{Br} + \\text{HBr}\\text{ (sản phẩm phụ: 3\\%)} \\end{cases}", "Nguyên tử H liên kết với C bậc cao hơn (bậc II) dễ bị thế hơn H ở C bậc I"),
            F("Phản ứng đốt cháy hoàn toàn Alkane", "\\text{C}_n\\text{H}_{2n+2} + \\frac{3n+1}{2}\\text{O}_2 \\xrightarrow{t^\\circ} n\\text{CO}_2 + (n+1)\\text{H}_2\\text{O}\\implies \\begin{cases} n_{\\text{alkane}} = n_{\\text{H}_2\\text{O}} - n_{\\text{CO}_2} \\\\ n = \\frac{n_{\\text{CO}_2}}{n_{\\text{H}_2\\text{O}} - n_{\\text{CO}_2}} \\end{cases}", "Đốt cháy alkane luôn thu được n_H2O > n_CO2"),
        ],
        [
            "Gọi được tên theo danh pháp thay thế IUPAC (và tên thông thường) của các alkane mạch thẳng và mạch nhánh ($\\text{C}_1 - \\text{C}_{10}$)",
            "Trình bày được tính chất hóa học của alkane: phản ứng thế halogen (xác định sản phẩm chính), cracking, reforming và phản ứng cháy",
            "Nêu được nguồn gốc và biện pháp giảm ô nhiễm không khí do khí thải động cơ đốt sử dụng nhiên liệu alkane",
        ],
        "Đốt cháy hoàn toàn một alkane $X$ thu được $0,3\\text{ mol}$ $\\text{CO}_2$ và $0,4\\text{ mol}$ $\\text{H}_2\\text{O}$. Xác định công thức phân tử và gọi tên $X$.",
        "Vì $X$ là alkane nên số mol của $X$ là: $n_X = n_{\\text{H}_2\\text{O}} - n_{\\text{CO}_2} = 0,4 - 0,3 = 0,1\\text{ mol}$.\nSố nguyên tử carbon trong $X$: $n = \\frac{n_{\\text{CO}_2}}{n_X} = \\frac{0,3}{0,1} = 3$.\nVậy công thức phân tử của $X$ là $\\text{C}_3\\text{H}_8$ (tên gọi: propane).",
        "Quá trình reforming trong nhà máy lọc dầu chuyển hóa các alkane mạch thẳng (chỉ số octane thấp, dễ gây kích nổ) thành các alkane mạch nhánh và arene có chỉ số octane cao (như xăng RON 95).",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Theo danh pháp thay thế IUPAC, hợp chất $\\text{CH}_3-\\text{CH(CH}_3)-\\text{CH}_2-\\text{CH}_3$ có tên gọi là:", "2-methylbutane", ["2-methylbutane", "3-methylbutane", "isobutane", "2-methylpentane"], "Mạch chính dài nhất có $4$ carbon (butane), đánh số từ đầu gần nhánh methyl ($-\\text{CH}_3$) nhất là vị trí số $2 \\Rightarrow$ 2-methylbutane.", "biet"),
            mcq("Khi cho propane ($\\text{CH}_3-\\text{CH}_2-\\text{CH}_3$) tác dụng với $\\text{Cl}_2$ theo tỉ lệ mol $1:1$ có chiếu sáng, sản phẩm thế monochloro chính thu được là:", "2-chloropropane ($\\text{CH}_3-\\text{CHCl}-\\text{CH}_3$)", ["2-chloropropane ($\\text{CH}_3-\\text{CHCl}-\\text{CH}_3$)", "1-chloropropane ($\\text{CH}_3-\\text{CH}_2-\\text{CH}_2\\text{Cl}$)", "1,2-dichloropropane", "chloromethane"], "Nguyên tử $\\text{H}$ ở carbon bậc II (giữa mạch) dễ bị thế hơn nguyên tử $\\text{H}$ ở carbon bậc I (đầu mạch).", "hieu"),
            short("Đốt cháy hoàn toàn một lượng hỗn hợp hai alkane kế tiếp nhau thu được $0,45\\text{ mol}$ $\\text{CO}_2$ và $0,65\\text{ mol}$ $\\text{H}_2\\text{O}$. Tổng số mol của hai alkane trong hỗn hợp bằng bao nhiêu mol?", "0,2", ["0,2", "0.2"], "Áp dụng công thức đốt cháy alkane: $n_{\\text{hh alkane}} = n_{\\text{H}_2\\text{O}} - n_{\\text{CO}_2} = 0,65 - 0,45 = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(14, "Hydrocarbon không no (Alkene và Alkyne)",
        "Đồng phân hình học cis - trans, quy tắc cộng Markovnikov, phản ứng với KMnO4, trùng hợp và phản ứng thế của alk-1-yne với AgNO3/NH3",
        "Alkene ($\\text{C}_n\\text{H}_{2n}, n \\ge 2$, có $1$ liên kết đôi $\\text{C}=\\text{C}$) và alkyne ($\\text{C}_n\\text{H}_{2n-2}, n \\ge 2$, có $1$ liên kết ba $\\text{C}\\equiv\\text{C}$) là các hydrocarbon không no. Alkene có đồng phân hình học cis - trans khi mỗi nguyên tử $\\text{C}$ mang nối đôi đính với $2$ nhóm nguyên tử khác nhau ($ab\\text{C}=\\text{C}cd$ với $a \neq b$ và $c \neq d$). Do có liên kết $\\pi$ kém bền, chúng dễ tham gia: (1) Phản ứng cộng $\\text{H}_2$ (xúc tác $\\text{Ni}$ tạo alkane; alkyne cộng $\\text{H}_2$ với xúc tác $\\text{Lindlar}$ dừng ở alkene), cộng $\\text{Br}_2$, và cộng $\\text{HX} / \\text{H}_2\\text{O}$ tuân theo quy tắc Markovnikov; (2) Phản ứng làm mất màu dung dịch $\\text{KMnO}_4$; (3) Phản ứng trùng hợp. Đặc biệt, các alk-1-yne ($\\text{R}-\\text{C}\\equiv\\text{CH}$) có nguyên tử $\\text{H}$ linh động tác dụng với dung dịch $\\text{AgNO}_3/\\text{NH}_3$ tạo kết tủa màu vàng nhạt.",
        [
            F("Quy tắc cộng Markovnikov (cộng HX hoặc H-OH vào alkene bất đối xứng)", "\\text{CH}_2=\\text{CH}-\\text{CH}_3 + \\text{HBr} \\rightarrow \\begin{cases} \\text{CH}_3-\\text{CHBr}-\\text{CH}_3\\text{ (sản phẩm chính)} \\\\ \\text{CH}_2\\text{Br}-\\text{CH}_2-\\text{CH}_3\\text{ (sản phẩm phụ)} \\end{cases}", "Nguyên tử H ưu tiên cộng vào C mang nối đôi có nhiều H hơn (bậc thấp hơn), phần X cộng vào C bậc cao hơn"),
            F("Phản ứng oxi hóa Alkene bằng dung dịch KMnO4 loãng", "3\\text{CH}_2=\\text{CH}_2 + 2\\text{KMnO}_4 + 4\\text{H}_2\\text{O} \\rightarrow 3\\text{HO}-\\text{CH}_2-\\text{CH}_2-\\text{OH} + 2\\text{MnO}_2\\downarrow + 2\\text{KOH}", "Dung dịch KMnO4 mất màu tím và xuất hiện kết tủa nâu đen MnO2"),
            F("Phản ứng đặc trưng của Alk-1-yne với AgNO3/NH3", "\\text{HC}\\equiv\\text{CH} + 2\\text{AgNO}_3 + 2\\text{NH}_3 \\rightarrow \\text{AgC}\\equiv\\text{CAg}\\downarrow\\text{ (vàng nhạt)} + 2\\text{NH}_4\\text{NO}_3", "Dùng để nhận biết các alkyne có liên kết ba ở đầu mạch (R-C≡CH)"),
        ],
        [
            "Viết được công thức cấu tạo, đồng phân hình học cis - trans và gọi tên theo danh pháp IUPAC của alkene và alkyne",
            "Vận dụng được quy tắc Markovnikov để xác định sản phẩm chính trong phản ứng cộng $\\text{HX}, \\text{H}_2\\text{O}$ vào hydrocarbon không no bất đối xứng",
            "Phân biệt được alkane, alkene và alk-1-yne bằng các thuốc thử đặc trưng (dung dịch $\\text{AgNO}_3/\\text{NH}_3$ và dung dịch $\\text{Br}_2$)",
        ],
        "Dẫn $0,1\\text{ mol}$ khí acetylene ($\\text{CH}\\equiv\\text{CH}$) vào lượng dư dung dịch $\\text{AgNO}_3$ trong $\\text{NH}_3$. Nêu hiện tượng và tính khối lượng kết tủa thu được.",
        "- Hiện tượng: Xuất hiện kết tủa màu vàng nhạt của silver acetylide ($\\text{C}_2\\text{Ag}_2$).\n- PTHH: $\\text{HC}\\equiv\\text{CH} + 2\\text{AgNO}_3 + 2\\text{NH}_3 \\rightarrow \\text{AgC}\\equiv\\text{CAg}\\downarrow + 2\\text{NH}_4\\text{NO}_3$.\n- Số mol kết tủa $\\text{C}_2\\text{Ag}_2$ ($M = 24 + 2 \\cdot 108 = 240$): $n_{\\text{C}_2\\text{Ag}_2} = n_{\\text{C}_2\\text{H}_2} = 0,1\\text{ mol} \\Rightarrow m = 0,1 \\cdot 240 = 24,0\\text{ g}$.",
        "Đèn xì oxygen - acetylene đốt cháy khí $\\text{C}_2\\text{H}_2$ trong $\\text{O}_2$ tinh khiết tỏa nhiệt lượng rất lớn (ngọn lửa đạt tới $3000^\\circ\\text{C}$), dùng để hàn và cắt các tấm kim loại dày.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Chất nào sau đây có đồng phân hình học (cis - trans)?", "But-2-ene ($\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$)", ["But-2-ene ($\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$)", "But-1-ene ($\\text{CH}_2=\\text{CH}-\\text{CH}_2-\\text{CH}_3$)", "Propene ($\\text{CH}_2=\\text{CH}-\\text{CH}_3$)", "Ethylene ($\\text{CH}_2=\\text{CH}_2$)"], "Ở but-2-ene, mỗi nguyên tử $\\text{C}$ mang nối đôi đều liên kết với $2$ nhóm khác nhau ($-\\text{H}$ và $-\\text{CH}_3$) nên có đồng phân cis và trans.", "biet"),
            mcq("Cho propene ($\\text{CH}_2=\\text{CH}-\\text{CH}_3$) cộng nước ($\\text{H}_2\\text{O}$) có xúc tác $\\text{H}_3\\text{PO}_4$, sản phẩm chính thu được theo quy tắc Markovnikov là:", "Propan-2-ol ($\\text{CH}_3-\\text{CH(OH)}-\\text{CH}_3$)", ["Propan-2-ol ($\\text{CH}_3-\\text{CH(OH)}-\\text{CH}_3$)", "Propan-1-ol ($\\text{CH}_3-\\text{CH}_2-\\text{CH}_2\\text{OH}$)", "Propane ($\\text{CH}_3-\\text{CH}_2-\\text{CH}_3$)", "Acetone ($\\text{CH}_3-\\text{CO}-\\text{CH}_3$)"], "Theo quy tắc Markovnikov, $\\text{H}$ cộng vào $\\text{CH}_2=$, còn nhóm $-\\text{OH}$ cộng vào $-\\text{CH}=$ bậc cao hơn tạo propan-2-ol.", "hieu"),
            short("Một mol propyne ($\\text{CH}\\equiv\\text{C}-\\text{CH}_3$) có thể phản ứng tối đa với bao nhiêu mol $\\text{Br}_2$ trong dung dịch?", "2", ["2"], "Phân tử alkyne có $1$ liên kết ba gồm $1\\sigma + 2\\pi$, nên $1\\text{ mol}$ alkyne cộng tối đa $2\\text{ mol}$ $\\text{Br}_2$.", "vandung"),
        ]
    ),
    bai(15, "Arene (Hydrocarbon thơm)",
        "Cấu trúc vòng benzene, dãy đồng đẳng CnH2n-6 (n >= 6), quy tắc thế vào vòng thơm, phản ứng cộng và oxi hóa nhánh alkyl của toluene",
        "Arene (hydrocarbon thơm) là những hydrocarbon trong phân tử có chứa một hay nhiều vòng benzene. Benzene ($\\text{C}_6\\text{H}_6$) và các alkylbenzene (như toluene $\\text{C}_6\\text{H}_5\\text{CH}_3$) lập thành dãy đồng đẳng có công thức chung $\\text{C}_n\\text{H}_{2n-6}$ ($n \\ge 6$, độ bất bão hòa $k = 4$ gồm $1$ vòng và $3$ liên kết $\\pi$ liên hợp). Vòng benzene có cấu trúc phẳng hình lục giác đều rất bền vững nên có tính thơm (dễ thế, khó cộng, bền với chất oxi hóa): (1) Phản ứng thế nguyên tử $\\text{H}$ của vòng benzene với $\\text{Br}_2$ khan (xúc tác $\\text{FeBr}_3$) và với $\\text{HNO}_3$ đặc (xúc tác $\\text{H}_2\\text{SO}_4$ đặc); nhóm alkyl ($-\\text{CH}_3$ trong toluene) làm vòng hoạt động hơn và định hướng thế vào vị trí ortho (số $2$) và para (số $4$). (2) Phản ứng cộng $\\text{Cl}_2$ (ánh sáng tạo $\\text{C}_6\\text{H}_6\\text{Cl}_6$) và cộng $\\text{H}_2$ (xúc tác $\\text{Ni}, t^\\circ$). (3) Benzene không làm mất màu dung dịch $\\text{KMnO}_4$, nhưng toluene làm mất màu dung dịch $\\text{KMnO}_4$ khi đun nóng.",
        [
            F("Phản ứng thế vào vòng Benzene và Toluene (quy tắc thế o-, p-)", "\\begin{cases} \\text{C}_6\\text{H}_6 + \\text{HNO}_{3\\text{ đặc}} \\xrightarrow{\\text{H}_2\\text{SO}_4\\text{ đặc, } t^\\circ} \\text{C}_6\\text{H}_5\\text{NO}_2 + \\text{H}_2\\text{O} \\\\ \\text{C}_6\\text{H}_5\\text{CH}_3 + 3\\text{HNO}_{3\\text{ đặc}} \\xrightarrow{\\text{H}_2\\text{SO}_4\\text{ đặc, } t^\\circ} \\text{2,4,6-trinitrotoluene (TNT)} + 3\\text{H}_2\\text{O} \\end{cases}", "Nhóm -CH3 định hướng nhóm thế mới vào vị trí ortho (2, 6) và para (4)"),
            F("Phản ứng oxi hóa nhánh Alkyl để phân biệt Toluene và Benzene", "\\text{C}_6\\text{H}_5\\text{CH}_3 + 2\\text{KMnO}_4 \\xrightarrow{t^\\circ} \\text{C}_6\\text{H}_5\\text{COOK} + 2\\text{MnO}_2\\downarrow + \\text{KOH} + \\text{H}_2\\text{O}", "Toluene làm mất màu KMnO4 khi đun nóng; Styrene (C6H5-CH=CH2) làm mất màu KMnO4 ngay ở nhiệt độ thường"),
        ],
        [
            "Mô tả được đặc điểm cấu tạo vòng benzene và gọi tên một số arene tiêu biểu (benzene, toluene, xylene, styrene, naphthalene)",
            "Trình bày được tính chất hóa học đặc trưng của arene: phản ứng thế vào vòng thơm (halogen hóa, nitro hóa), phản ứng cộng vào vòng và phản ứng oxi hóa nhánh alkyl",
            "Trình bày được cách phân biệt $3$ chất lỏng không màu: benzene, toluene và styrene bằng dung dịch $\\text{KMnO}_4$",
        ],
        "Trình bày phương pháp hóa học để phân biệt $3$ chất lỏng không màu đựng trong $3$ lọ mất nhãn: benzene ($\\text{C}_6\\text{H}_6$), toluene ($\\text{C}_6\\text{H}_5\\text{CH}_3$) và styrene ($\\text{C}_6\\text{H}_5-\\text{CH}=\\text{CH}_2$).",
        "Dùng thuốc thử duy nhất là dung dịch $\\text{KMnO}_4$:\n- Ở nhiệt độ thường: Mẫu làm mất màu tím của dung dịch $\\text{KMnO}_4$ ngay lập tức là styrene (do có nối đôi $\\text{C}=\\text{C}$ ở nhánh).\n- Đun nóng hai mẫu còn lại với dung dịch $\\text{KMnO}_4$: Mẫu làm mất màu tím và tạo kết tủa nâu đen $\\text{MnO}_2$ là toluene; mẫu không làm mất màu kể cả khi đun nóng là benzene.",
        "Trùng hợp styrene ($\\text{C}_6\\text{H}_5-\\text{CH}=\\text{CH}_2$) thu được nhựa polystyrene (PS) dùng sản xuất hộp xốp cách nhiệt; nitro hóa toluene thu được thuốc nổ TNT (2,4,6-trinitrotoluene).",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Công thức chung của dãy đồng đẳng benzene (alkylbenzene) là:", "$\\text{C}_n\\text{H}_{2n-6}\\; (n \\ge 6)$", ["$\\text{C}_n\\text{H}_{2n-6}\\; (n \\ge 6)$", "$\\text{C}_n\\text{H}_{2n+2}\\; (n \\ge 1)$", "$\\text{C}_n\\text{H}_{2n}\\; (n \\ge 2)$", "$\\text{C}_n\\text{H}_{2n-2}\\; (n \\ge 2)$"], "Benzene ($\\text{C}_6\\text{H}_6$) và các đồng đẳng có độ bất bão hòa $k = 4$, công thức chung là $\\text{C}_n\\text{H}_{2n-6}$ ($n \\ge 6$).", "biet"),
            mcq("Khi cho toluene ($\\text{C}_6\\text{H}_5\\text{CH}_3$) phản ứng thế với $\\text{Br}_2$ (có mặt bột $\\text{Fe}$ hoặc $\\text{FeBr}_3$, đun nóng, tỉ lệ $1:1$), nguyên tử $\\text{Br}$ ưu tiên thế vào vị trí nào trên vòng benzene?", "Vị trí ortho ($o-$) và para ($p-$)", ["Vị trí ortho ($o-$) và para ($p-$)", "Chỉ thế vào vị trí meta ($m-$)", "Chỉ thế vào nhóm $-\\text{CH}_3$", "Không xảy ra phản ứng"], "Nhóm alkyl ($-\\text{CH}_3$) là nhóm đẩy electron, làm giàu mật độ electron ở vị trí ortho (số $2, 6$) và para (số $4$).", "hieu"),
            short("Đun nóng hoàn toàn $0,1\\text{ mol}$ benzene ($\\text{C}_6\\text{H}_6$) với lượng dư khí $\\text{H}_2$ (xúc tác $\\text{Ni}$, nhiệt độ, áp suất cao) tạo thành cyclohexane ($\\text{C}_6\\text{H}_{12}$). Số mol khí $\\text{H}_2$ đã tham gia phản ứng là bao nhiêu mol?", "0,3", ["0,3", "0.3"], "PTHH: $\\text{C}_6\\text{H}_6 + 3\\text{H}_2 \\xrightarrow{\\text{Ni}, t^\\circ, p} \\text{C}_6\\text{H}_{12}$. Số mol $n_{\\text{H}_2} = 3n_{\\text{C}_6\\text{H}_6} = 3 \\cdot 0,1 = 0,3\\text{ mol}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 5: DẪN XUẤT HALOGEN - ALCOHOL - PHENOL
# =========================================================================
CH5_ID = "hoa11_ch5"
CH5_TITLE = "Chương 5: Dẫn xuất halogen - Alcohol - Phenol"
CH5_DESC = "Dẫn xuất halogen (phản ứng thế nhóm -X và tách HX theo quy tắc Zaitsev), alcohol (bậc alcohol, oxi hóa, nhận biết polyalcohol) và phenol"

CH5_LESSONS = [
    bai(16, "Dẫn xuất halogen",
        "Danh pháp, phản ứng thế nguyên tử halogen bằng nhóm -OH và phản ứng tách hydrogen halide (HX) theo quy tắc Zaitsev",
        "Dẫn xuất halogen thu được khi thay thế nguyên tử hydrogen trong phân tử hydrocarbon bằng một hay nhiều nguyên tử halogen ($\\text{F}, \\text{Cl}, \\text{Br}, \\text{I}$). Do liên kết $\\text{C}^{\\delta+}-\\text{X}^{\\delta-}$ phân cực mạnh về phía nguyên tử halogen nên dẫn xuất halogen có $2$ phản ứng hóa học đặc trưng: (1) Phản ứng thế nguyên tử halogen bằng nhóm $-\\text{OH}$ khi đun sôi với dung dịch kiềm loãng ($\\text{NaOH}$ trong nước) tạo alcohol: $\\text{R}-\\text{X} + \\text{NaOH} \\xrightarrow{t^\\circ} \\text{R}-\\text{OH} + \\text{NaX}$; (2) Phản ứng tách hydrogen halide ($\\text{HX}$) khi đun nóng với kiềm đặc trong dung môi ethanol ($\\text{NaOH}/\\text{C}_2\\text{H}_5\\text{OH}, t^\\circ$) tạo alkene theo quy tắc Zaitsev: nguyên tử halogen $\\text{X}$ ưu tiên tách ra cùng với nguyên tử $\\text{H}$ ở nguyên tử carbon bên cạnh có bậc cao hơn (ít $\\text{H}$ hơn).",
        [
            F("Phản ứng thế nguyên tử Halogen bằng nhóm -OH (thủy phân trong kiềm)", "\\text{CH}_3\\text{CH}_2\\text{Br} + \\text{NaOH} \\xrightarrow{\\text{H}_2\\text{O},\\; t^\\circ} \\text{CH}_3\\text{CH}_2\\text{OH} + \\text{NaBr}", "Xảy ra đối với các dẫn xuất alkyl halide khi đun nóng với dung dịch kiềm trong nước"),
            F("Phản ứng tách HX theo Quy tắc Zaitsev (trong kiềm / alcohol, đun nóng)", "\\text{CH}_3-\\text{CHBr}-\\text{CH}_2-\\text{CH}_3 \\xrightarrow{\\text{NaOH/C}_2\\text{H}_5\\text{OH},\\; t^\\circ} \\begin{cases} \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3\\text{ (sản phẩm chính)} \\\\ \\text{CH}_2=\\text{CH}-\\text{CH}_2-\\text{CH}_3\\text{ (sản phẩm phụ)} \\end{cases} + \\text{HBr}", "Quy tắc Zaitsev: X ưu tiên tách cùng H ở C bên cạnh có bậc cao hơn"),
        ],
        [
            "Nêu được khái niệm, đồng phân, danh pháp thay thế và tính chất vật lí của dẫn xuất halogen",
            "Viết được phương trình phản ứng thế nguyên tử halogen bằng nhóm $-\\text{OH}$ và vận dụng quy tắc Zaitsev để xác định sản phẩm chính của phản ứng tách $\\text{HX}$",
            "Trình bày được ứng dụng của dẫn xuất halogen (nhựa PVC, chất chống dính Teflon, thuốc mê) và tác hại của hợp chất CFC đối với tầng ozone",
        ],
        "Đun nóng 2-bromobutane ($\\text{CH}_3-\\text{CHBr}-\\text{CH}_2-\\text{CH}_3$) với dung dịch $\\text{KOH}$ đặc trong $\\text{C}_2\\text{H}_5\\text{OH}$. Hãy xác định công thức cấu tạo và tên gọi của sản phẩm alkene chính thu được.",
        "Theo quy tắc Zaitsev, nguyên tử $\\text{Br}$ ở $\\text{C}_2$ ưu tiên tách ra cùng nguyên tử $\\text{H}$ ở nguyên tử $\\text{C}_3$ (carbon bậc II, có ít $\\text{H}$ hơn so với $\\text{C}_1$ bậc I).\nDo đó sản phẩm alkene chính là $\\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3$ (but-2-ene).",
        "Các hợp chất CFC (chlorofluorocarbon như $\\text{CF}_2\\text{Cl}_2$) trước đây dùng trong tủ lạnh và điều hòa nhưng khi bay lên tầng bình lưu bị tia UV phân hủy tạo gốc tự do $\\text{Cl}^\\bullet$ phá hủy tầng ozone, nên đã bị cấm theo Nghị định thư Montreal.",
        CH5_ID, CH5_TITLE, CH5_DESC,
        extra_questions=[
            mcq("Đun sôi ethyl chloride ($\\text{CH}_3\\text{CH}_2\\text{Cl}$) với dung dịch $\\text{NaOH}$ loãng trong nước thì thu được sản phẩm hữu cơ là:", "Ethanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$)", ["Ethanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$)", "Ethylene ($\\text{CH}_2=\\text{CH}_2$)", "Ethane ($\\text{CH}_3\\text{CH}_3$)", "Acetic acid ($\\text{CH}_3\\text{COOH}$)"], "Phản ứng thế nguyên tử $\\text{Cl}$ bằng nhóm $-\\text{OH}$: $\\text{C}_2\\text{H}_5\\text{Cl} + \\text{NaOH} \\xrightarrow{\\text{H}_2\\text{O}, t^\\circ} \\text{C}_2\\text{H}_5\\text{OH} + \\text{NaCl}$.", "biet"),
            mcq("Theo quy tắc Zaitsev, trong phản ứng tách $\\text{HX}$ ra khỏi dẫn xuất halogen, nguyên tử halogen ($-\\text{X}$) ưu tiên tách ra cùng với:", "Nguyên tử $\\text{H}$ ở nguyên tử carbon bên cạnh có bậc cao hơn (ít $\\text{H}$ hơn)", ["Nguyên tử $\\text{H}$ ở nguyên tử carbon bên cạnh có bậc cao hơn (ít $\\text{H}$ hơn)", "Nguyên tử $\\text{H}$ ở nguyên tử carbon bên cạnh có bậc thấp hơn (nhiều $\\text{H}$ hơn)", "Nguyên tử $\\text{H}$ gắn trên chính nguyên tử carbon mang halogen", "Nguyên tử carbon ở đầu mạch"], "Quy tắc cộng Markovnikov: $\\text{H}$ vào $\\text{C}$ nhiều $\\text{H}$ hơn; quy tắc tách Zaitsev: $\\text{H}$ tách ra từ $\\text{C}$ bên cạnh ít $\\text{H}$ hơn.", "hieu"),
            short("Đun nóng $0,2\\text{ mol}$ $\\text{C}_2\\text{H}_5\\text{Br}$ với lượng dư dung dịch $\\text{NaOH}$ loãng cho đến khi phản ứng hoàn toàn, sau đó acid hóa dung dịch bằng $\\text{HNO}_3$ rồi thêm $\\text{AgNO}_3$ dư vào thì thu được bao nhiêu mol kết tủa $\\text{AgBr}$?", "0,2", ["0,2", "0.2"], "Bảo toàn nguyên tố $\\text{Br}$: $n_{\\text{AgBr}} = n_{\\text{NaBr}} = n_{\\text{C}_2\\text{H}_5\\text{Br}} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(17, "Alcohol",
        "Bậc alcohol, liên kết hydrogen, phản ứng thế H của nhóm -OH, phản ứng tách nước, oxi hóa alcohol bằng CuO và phản ứng của polyalcohol với Cu(OH)2",
        "Alcohol là những hợp chất hữu cơ trong phân tử có nhóm hydroxyl ($-\\text{OH}$) liên kết trực tiếp với nguyên tử carbon no. Bậc của alcohol bằng bậc của nguyên tử carbon liên kết trực tiếp với nhóm $-\\text{OH}$. Do tạo được liên kết hydrogen liên phân tử nên alcohol có nhiệt độ sôi cao hơn hẳn hydrocarbon/ether cùng phân tử khối và các alcohol đầu dãy tan vô hạn trong nước. Tính chất hóa học: (1) Phản ứng thế $\\text{H}$ của nhóm $-\\text{OH}$ với $\\text{Na}, \\text{K}$ giải phóng $\\text{H}_2$; (2) Phản ứng tách nước ở $140^\\circ\\text{C}$ tạo ether, ở $170^\\circ\\text{C}$ tạo alkene; (3) Oxi hóa không hoàn toàn bằng $\\text{CuO}$ đun nóng: alcohol bậc I tạo aldehyde ($-\\text{CHO}$), alcohol bậc II tạo ketone ($-\\text{CO}-$); (4) Các polyalcohol có ít nhất $2$ nhóm $-\\text{OH}$ liền kề (như ethylene glycol, glycerol) hòa tan được $\\text{Cu(OH)}_2$ tạo dung dịch màu xanh lam đậm.",
        [
            F("Phản ứng với Kim loại kiềm và Phản ứng tách nước của Alcohol", "\\begin{cases} \\text{R}(\\text{OH})_k + k\\text{Na} \\rightarrow \\text{R}(\\text{ONa})_k + \\frac{k}{2}\\text{H}_2\\uparrow \\\\ \\text{C}_2\\text{H}_5\\text{OH} \\xrightarrow{\\text{H}_2\\text{SO}_4\\text{ đặc, } 170^\\circ\\text{C}} \\text{CH}_2=\\text{CH}_2\\uparrow + \\text{H}_2\\text{O}\\text{ (ở } 140^\\circ\\text{C tạo } \\text{C}_2\\text{H}_5\\text{OC}_2\\text{H}_5\\text{)} \\end{cases}", "Số nhóm -OH trong phân tử k = 2 * n_H2 / n_alcohol"),
            F("Oxi hóa không hoàn toàn bằng CuO đun nóng", "\\begin{cases} \\text{Alcohol bậc I: } \\text{R}-\\text{CH}_2\\text{OH} + \\text{CuO} \\xrightarrow{t^\\circ} \\text{R}-\\text{CHO (aldehyde)} + \\text{Cu} + \\text{H}_2\\text{O} \\\\ \\text{Alcohol bậc II: } \\text{R}-\\text{CH(OH)}-\\text{R'} + \\text{CuO} \\xrightarrow{t^\\circ} \\text{R}-\\text{CO}-\\text{R' (ketone)} + \\text{Cu} + \\text{H}_2\\text{O} \\end{cases}", "Alcohol bậc III không bị oxi hóa bởi CuO"),
            F("Phản ứng đặc trưng của Polyalcohol (có >= 2 nhóm -OH kề nhau)", "2\\text{C}_3\\text{H}_5(\\text{OH})_3 + \\text{Cu(OH)}_2 \\rightarrow [\\text{C}_3\\text{H}_5(\\text{OH})_2\\text{O}]_2\\text{Cu\\text{ (dung dịch xanh lam)}} + 2\\text{H}_2\\text{O}", "Dùng Cu(OH)2 để phân biệt glycerol / ethylene glycol với monoalcohol (C2H5OH)"),
        ],
        [
            "Xác định được bậc của alcohol (bậc I, II, III), gọi tên theo danh pháp thay thế và giải thích được nhiệt độ sôi, độ tan của alcohol",
            "Viết được các phương trình phản ứng của alcohol với $\\text{Na}$, tách nước tạo ether/alkene, và oxi hóa alcohol bậc I, bậc II bằng $\\text{CuO}$",
            "Trình bày được phản ứng đặc trưng của polyalcohol (glycerol, ethylene glycol) hòa tan kết tủa $\\text{Cu(OH)}_2$ tạo phức chất màu xanh lam",
        ],
        "Cho $9,2\\text{ g}$ glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$, $M = 92$) tác dụng hoàn toàn với lượng dư kim loại $\\text{Na}$. Tính thể tích khí $\\text{H}_2$ thoát ra ở đkc.",
        "Số mol glycerol: $n = \\frac{9,2}{92} = 0,1\\text{ mol}$.\nVì glycerol có $3$ nhóm $-\\text{OH}$ nên PTHH là:\n$\\text{C}_3\\text{H}_5(\\text{OH})_3 + 3\\text{Na} \\rightarrow \\text{C}_3\\text{H}_5(\\text{ONa})_3 + \\frac{3}{2}\\text{H}_2\\uparrow$.\nSố mol $\\text{H}_2$: $n_{\\text{H}_2} = 1,5 \\cdot 0,1 = 0,15\\text{ mol} \\Rightarrow V_{\\text{H}_2} = 0,15 \\cdot 24,79 = 3,7185\\text{ L}$.",
        "Glycerol có tính giữ ẩm cao và không độc nên được dùng rộng rãi trong kem dưỡng da, son môi và thuốc nhỏ mắt; ngược lại, methanol ($\\text{CH}_3\\text{OH}$) rất độc, uống phải rượu pha cồn công nghiệp chứa methanol có thể gây mù lòa và tử vong.",
        CH5_ID, CH5_TITLE, CH5_DESC,
        extra_questions=[
            mcq("Khi oxi hóa không hoàn toàn một alcohol bậc I ($\\text{R}-\\text{CH}_2\\text{OH}$) bằng bột $\\text{CuO}$ đun nóng thì thu được sản phẩm hữu cơ thuộc loại nào?", "Aldehyde ($\\text{R}-\\text{CHO}$)", ["Aldehyde ($\\text{R}-\\text{CHO}$)", "Ketone ($\\text{R}-\\text{CO}-\\text{R'}$)", "Alkene", "Ether"], "Alcohol bậc I bị $\\text{CuO}$ đun nóng oxi hóa thành aldehyde; alcohol bậc II bị oxi hóa thành ketone.", "biet"),
            mcq("Thuốc thử dùng để phân biệt hai dung dịch không màu là ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$) và glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$) là:", "$\\text{Cu(OH)}_2$ ở nhiệt độ thường", ["$\\text{Cu(OH)}_2$ ở nhiệt độ thường", "Kim loại $\\text{Na}$", "Quỳ tím", "Dung dịch $\\text{NaCl}$"], "Glycerol có $3$ nhóm $-\\text{OH}$ liền kề nên hòa tan được kết tủa $\\text{Cu(OH)}_2$ tạo dung dịch màu xanh lam đậm, còn ethanol không hòa tan được.", "hieu"),
            short("Cho $0,2\\text{ mol}$ ethylene glycol ($\\text{HO}-\\text{CH}_2-\\text{CH}_2-\\text{OH}$) tác dụng hết với kim loại $\\text{Na}$ dư thu được bao nhiêu mol khí $\\text{H}_2$?", "0,2", ["0,2", "0.2"], "Mỗi phân tử ethylene glycol có $2$ nhóm $-\\text{OH}$, nên $n_{\\text{H}_2} = \\frac{2}{2} n_{\\text{alcohol}} = n_{\\text{alcohol}} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(18, "Phenol",
        "Ảnh hưởng qua lại giữa nhóm -OH và vòng benzene trong phân tử phenol (C6H5OH): tính acid yếu và phản ứng thế vòng thơm tạo kết tủa trắng và picric acid",
        "Phenol là những hợp chất hữu cơ trong phân tử có nhóm $-\\text{OH}$ liên kết trực tiếp với nguyên tử carbon của vòng benzene. Chất đầu dãy là phenol ($\\text{C}_6\\text{H}_5\\text{OH}$, $M = 94$), chất rắn kết tinh không màu (để lâu ngoài không khí bị oxi hóa chậm chuyển sang màu hồng), ít tan trong nước lạnh nhưng tan nhiều trong nước nóng và rất độc (gây bỏng da). Trong phân tử phenol, vòng benzene hút electron làm tăng độ phân cực của liên kết $\\text{O}-\\text{H}$ nên phenol có tính acid yếu (tác dụng được với dung dịch $\\text{NaOH}$, nhưng rất yếu không làm đổi màu quỳ tím); ngược lại nhóm $-\\text{OH}$ đẩy electron vào vòng benzene làm tăng mật độ electron ở vị trí ortho và para, giúp phenol dễ dàng tham gia phản ứng thế với dung dịch nước $\\text{Br}_2$ tạo kết tủa trắng và với $\\text{HNO}_3$ đặc tạo kết tủa vàng (picric acid).",
        [
            F("Tính acid yếu của Phenol (tác dụng với Na VÀ dung dịch NaOH)", "\\text{C}_6\\text{H}_5\\text{OH} + \\text{NaOH} \\rightarrow \\text{C}_6\\text{H}_5\\text{ONa} + \\text{H}_2\\text{O}\\quad (\\text{Alcohol } \\text{C}_2\\text{H}_5\\text{OH không tác dụng với NaOH})", "Tính acid của phenol vẫn yếu hơn nấc 1 của H2CO3 (không làm đổi màu quỳ tím)"),
            F("Phản ứng thế vào vòng Benzene (nhận biết Phenol)", "\\begin{cases} \\text{C}_6\\text{H}_5\\text{OH} + 3\\text{Br}_2\\text{ (dd)} \\rightarrow \\text{C}_6\\text{H}_2\\text{Br}_3\\text{OH}\\downarrow\\text{ (trắng)} + 3\\text{HBr} \\\\ \\text{C}_6\\text{H}_5\\text{OH} + 3\\text{HNO}_{3\\text{ đặc}} \\xrightarrow{\\text{H}_2\\text{SO}_4\\text{ đặc, } t^\\circ} \\text{C}_6\\text{H}_2(\\text{NO}_2)_3\\text{OH}\\downarrow\\text{ (vàng)} + 3\\text{H}_2\\text{O} \\end{cases}", "2,4,6-tribromophenol kết tủa trắng; 2,4,6-trinitrophenol (picric acid) kết tủa vàng"),
        ],
        [
            "Phân biệt được cấu tạo của phenol ($-\\text{OH}$ gắn trực tiếp vào vòng benzene) với alcohol thơm ($-\\text{OH}$ gắn vào nhánh alkyl như $\\text{C}_6\\text{H}_5\\text{CH}_2\\text{OH}$)",
            "Giải thích được tính acid yếu của phenol (tác dụng với dung dịch $\\text{NaOH}$) và khả năng thế dễ dàng vào vị trí $2, 4, 6$ của vòng benzene",
            "Viết được phương trình phản ứng của phenol với $\\text{NaOH}$, nước $\\text{Br}_2$, $\\text{HNO}_3$ đặc và tính toán lượng kết tủa",
        ],
        "Nhỏ nước bromine ($\\text{Br}_2$) dư vào dung dịch chứa $4,7\\text{ g}$ phenol ($\\text{C}_6\\text{H}_5\\text{OH}$, $M = 94$). Nêu hiện tượng và tính khối lượng kết tủa thu được.",
        "- Hiện tượng: Nước bromine mất màu và xuất hiện kết tủa màu trắng của 2,4,6-tribromophenol ($\\text{C}_6\\text{H}_2\\text{Br}_3\\text{OH}$, $M = 331$).\n- Số mol phenol: $n_{\\text{C}_6\\text{H}_5\\text{OH}} = \\frac{4,7}{94} = 0,05\\text{ mol}$.\n- PTHH: $\\text{C}_6\\text{H}_5\\text{OH} + 3\\text{Br}_2 \\rightarrow \\text{C}_6\\text{H}_2\\text{Br}_3\\text{OH}\\downarrow + 3\\text{HBr}$.\n- Khối lượng kết tủa: $m = 0,05 \\cdot 331 = 16,55\\text{ g}$.",
        "Phenol là nguyên liệu quan trọng để tổng hợp nhựa phenol-formaldehyde (nhựa bakelite cách điện làm tay cầm xoong nồi, ổ cắm điện), phẩm nhuộm và chất diệt cỏ 2,4-D.",
        CH5_ID, CH5_TITLE, CH5_DESC,
        extra_questions=[
            mcq("Phản ứng nào sau đây chứng minh phenol ($\\text{C}_6\\text{H}_5\\text{OH}$) có tính acid mạnh hơn ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$)?", "Phenol tác dụng được với dung dịch $\\text{NaOH}$, còn $\\text{C}_2\\text{H}_5\\text{OH}$ thì không", ["Phenol tác dụng được với dung dịch $\\text{NaOH}$, còn $\\text{C}_2\\text{H}_5\\text{OH}$ thì không", "Phenol tác dụng được với kim loại $\\text{Na}$ giải phóng $\\text{H}_2$", "Phenol cháy trong khí $\\text{O}_2$ tạo $\\text{CO}_2$ và $\\text{H}_2\\text{O}$", "Phenol làm quỳ tím hóa đỏ đậm"], "Cả phenol và alcohol đều tác dụng với $\\text{Na}$, nhưng chỉ có phenol tác dụng được với dung dịch $\\text{NaOH}$.", "biet"),
            mcq("Khi nhỏ dung dịch nước bromine ($\\text{Br}_2$) vào ống nghiệm đựng dung dịch phenol ($\\text{C}_6\\text{H}_5\\text{OH}$), hiện tượng quan sát được là:", "Nước bromine mất màu và xuất hiện kết tủa màu trắng (2,4,6-tribromophenol)", ["Nước bromine mất màu và xuất hiện kết tủa màu trắng (2,4,6-tribromophenol)", "Sủi bọt khí không màu, không mùi", "Xuất hiện kết tủa màu xanh lam đậm", "Không có hiện tượng gì xảy ra"], "Do ảnh hưởng của nhóm $-\\text{OH}$, phenol thế ngay $3$ nguyên tử $\\text{Br}$ vào vị trí $2, 4, 6$ tạo kết tủa trắng.", "hieu"),
            short("Để trung hòa vừa đủ dung dịch chứa $18,8\\text{ g}$ phenol ($\\text{C}_6\\text{H}_5\\text{OH}$, $M = 94$) cần dùng bao nhiêu mol $\\text{NaOH}$?", "0,2", ["0,2", "0.2"], "PTHH: $\\text{C}_6\\text{H}_5\\text{OH} + \\text{NaOH} \\rightarrow \\text{C}_6\\text{H}_5\\text{ONa} + \\text{H}_2\\text{O}$. Số mol $n_{\\text{NaOH}} = n_{\\text{phenol}} = \\frac{18,8}{94} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 6: HỢP CHẤT CARBONYL - CARBOXYLIC ACID
# =========================================================================
CH6_ID = "hoa11_ch6"
CH6_TITLE = "Chương 6: Hợp chất Carbonyl - Carboxylic acid"
CH6_DESC = "Aldehyde, ketone (phản ứng khử, tráng bạc, Cu(OH)2/OH-, tạo iodoform), carboxylic acid và bài toán tổng hợp hữu cơ"

CH6_LESSONS = [
    bai(19, "Hợp chất carbonyl (Aldehyde và Ketone)",
        "Cấu tạo nhóm C=O, phản ứng khử bằng NaBH4/LiAlH4, phản ứng tráng bạc (thuốc thử Tollens), phản ứng với Cu(OH)2/OH- và phản ứng tạo iodoform (CHI3)",
        "Hợp chất carbonyl chứa nhóm chức carbonyl ($\\text{C}=\\text{O}$), gồm: Aldehyde (nhóm $-\\text{CHO}$ liên kết với gốc hydrocarbon hoặc nguyên tử $\\text{H}$) và Ketone (nhóm $-\\text{CO}-$ liên kết với hai gốc hydrocarbon). Tính chất hóa học: (1) Phản ứng khử bằng $\\text{NaBH}_4$ hoặc $\\text{LiAlH}_4$ (hoặc $\\text{H}_2/\\text{Ni}, t^\\circ$): aldehyde bị khử thành alcohol bậc I, ketone bị khử thành alcohol bậc II; (2) Phản ứng oxi hóa aldehyde (ketone KHÔNG có phản ứng này): làm mất màu nước $\\text{Br}_2$, phản ứng với thuốc thử Tollens ($[\\text{Ag(NH}_3)_2]\\text{OH}$) đun nóng tạo kết tủa bạc ($\\text{Ag}$) sáng bóng, và tác dụng với $\\text{Cu(OH)}_2/\\text{OH}^-$ đun nóng tạo kết tủa $\\text{Cu}_2\\text{O}$ màu đỏ gạch; (3) Các hợp chất có nhóm $\\text{CH}_3-\\text{CO}-$ (như $\\text{CH}_3\\text{CHO}, \\text{CH}_3\\text{COCH}_3$) tác dụng với $\\text{I}_2/\\text{NaOH}$ tạo kết tủa vàng $\\text{CHI}_3$ (phản ứng iodoform).",
        [
            F("Phản ứng khử Aldehyde và Ketone tạo Alcohol", "\\begin{cases} \\text{R}-\\text{CHO} \\xrightarrow{\\text{NaBH}_4\\text{ hoặc } \\text{LiAlH}_4} \\text{R}-\\text{CH}_2\\text{OH (Alcohol bậc I)} \\\\ \\text{R}-\\text{CO}-\\text{R'} \\xrightarrow{\\text{NaBH}_4\\text{ hoặc } \\text{LiAlH}_4} \\text{R}-\\text{CH(OH)}-\\text{R' (Alcohol bậc II)} \\end{cases}", "Khử nhóm C=O thành nhóm CH-OH"),
            F("Phản ứng tráng bạc (Thuốc thử Tollens - phân biệt Aldehyde với Ketone)", "\\begin{cases} \\text{R}-\\text{CHO} + 2[\\text{Ag(NH}_3)_2]\\text{OH} \\xrightarrow{t^\\circ} \\text{R}-\\text{COONH}_4 + 2\\text{Ag}\\downarrow + 3\\text{NH}_3 + \\text{H}_2\\text{O} \\\\ \\text{Riêng } \\text{HCHO} \\text{ (formic aldehyde): } 1\\text{ mol } \\text{HCHO} \\rightarrow 4\\text{ mol } \\text{Ag}\\downarrow \\end{cases}", "Aldehyde tác dụng với Cu(OH)2/NaOH đun nóng tạo kết tủa Cu2O màu đỏ gạch"),
            F("Phản ứng tạo Iodoform (nhận biết nhóm methyl carbonyl CH3-C=O)", "\\text{R}-\\text{CO}-\\text{CH}_3 + 3\\text{I}_2 + 4\\text{NaOH} \\rightarrow \\text{R}-\\text{COONa} + \\text{CHI}_3\\downarrow\\text{ (vàng)} + 3\\text{NaI} + 3\\text{H}_2\\text{O}", "Xảy ra với CH3CHO và các methyl ketone (CH3-CO-R)"),
        ],
        [
            "Phân biệt được cấu tạo và gọi tên theo danh pháp thay thế (và tên thông thường) của các aldehyde và ketone phổ biến",
            "Viết được phương trình hóa học của phản ứng khử, phản ứng oxi hóa aldehyde (bằng nước $\\text{Br}_2$, thuốc thử Tollens, $\\text{Cu(OH)}_2/\\text{OH}^-$) và phản ứng tạo iodoform ($\\text{CHI}_3$)",
            "Giải được bài toán phản ứng tráng bạc (chú ý trường hợp đặc biệt của $\\text{HCHO}$ tạo $4\\text{Ag}$)",
        ],
        "Cho $4,4\\text{ g}$ ethanal ($\\text{CH}_3\\text{CHO}$, $M = 44$) tác dụng hoàn toàn với lượng dư thuốc thử Tollens ($\\text{AgNO}_3/\\text{NH}_3$) đun nóng. Tính khối lượng bạc ($\\text{Ag} = 108$) kết tủa thu được.",
        "Số mol $\\text{CH}_3\\text{CHO}$: $n = \\frac{4,4}{44} = 0,1\\text{ mol}$.\nTheo PTHH tráng bạc của monoaldehyde (trừ $\\text{HCHO}$):\n$n_{\\text{Ag}} = 2n_{\\text{CH}_3\\text{CHO}} = 2 \\cdot 0,1 = 0,2\\text{ mol}$.\nKhối lượng bạc thu được: $m_{\\text{Ag}} = 0,2 \\cdot 108 = 21,6\\text{ g}$.",
        "Dung dịch formalin (chứa $37\\% - 40\\%$ khí $\\text{HCHO}$ trong nước) được dùng để ngâm xác động vật làm tiêu bản sinh học (tuyệt đối cấm dùng bảo quản thực phẩm vì rất độc); acetone ($\\text{CH}_3\\text{COCH}_3$) là dung môi hòa tan sơn móng tay rất tốt.",
        CH6_ID, CH6_TITLE, CH6_DESC,
        extra_questions=[
            mcq("Để phân biệt hai chất lỏng ethanal ($\\text{CH}_3\\text{CHO}$) và acetone ($\\text{CH}_3\\text{COCH}_3$), ta dùng thuốc thử nào sau đây?", "Thuốc thử Tollens ($\\text{AgNO}_3$ trong $\\text{NH}_3$, đun nóng)", ["Thuốc thử Tollens ($\\text{AgNO}_3$ trong $\\text{NH}_3$, đun nóng)", "Dung dịch $\\text{I}_2$ trong $\\text{NaOH}$", "Dung dịch $\\text{NaCl}$", "Quỳ tím"], "$\\text{CH}_3\\text{CHO}$ có phản ứng tráng bạc với thuốc thử Tollens còn $\\text{CH}_3\\text{COCH}_3$ (ketone) không phản ứng (cả hai đều có nhóm $\\text{CH}_3\\text{CO}-$ nên đều tạo kết tủa vàng với $\\text{I}_2/\\text{NaOH}$).", "biet"),
            mcq("Khi đun nóng aldehyde với $\\text{Cu(OH)}_2$ trong môi trường kiềm ($\\text{NaOH}$), kết tủa thu được có công thức và màu sắc là:", "$\\text{Cu}_2\\text{O}$ màu đỏ gạch", ["$\\text{Cu}_2\\text{O}$ màu đỏ gạch", "$\\text{CuO}$ màu đen", "$\\text{Cu}$ màu đỏ", "$\\text{CHI}_3$ màu vàng"], "Aldehyde khử $\\text{Cu(OH)}_2$ trong môi trường kiềm đun nóng tạo kết tủa copper(I) oxide ($\\text{Cu}_2\\text{O}$) màu đỏ gạch.", "hieu"),
            short("Đun nóng hoàn toàn $0,05\\text{ mol}$ methanal ($\\text{HCHO}$) với lượng dư thuốc thử Tollens ($\\text{AgNO}_3/\\text{NH}_3$) thu được tối đa bao nhiêu mol bạc ($\\text{Ag}$) kết tủa?", "0,2", ["0,2", "0.2"], "Riêng với $\\text{HCHO}$, $1\\text{ mol}$ $\\text{HCHO}$ tạo ra $4\\text{ mol}$ $\\text{Ag}$, nên $n_{\\text{Ag}} = 4 \\cdot 0,05 = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(20, "Carboxylic acid",
        "Cấu tạo nhóm -COOH, liên kết hydrogen dạng dimer bền vững, tính acid yếu nhưng mạnh hơn H2CO3 và phản ứng ester hóa thuận nghịch",
        "Carboxylic acid là những hợp chất hữu cơ trong phân tử có nhóm carboxyl ($-\\text{COOH}$) liên kết trực tiếp với nguyên tử carbon hoặc nguyên tử hydrogen. Dãy đồng đẳng carboxylic acid no, đơn chức, mạch hở có công thức chung $\\text{C}_n\\text{H}_{2n+1}\\text{COOH}$ ($n \\ge 0$) hay $\\text{C}_m\\text{H}_{2m}\\text{O}_2$ ($m \\ge 1$, $k = 1$). Do tạo được liên kết hydrogen liên phân tử rất bền (dạng dimer vòng), nhiệt độ sôi của carboxylic acid cao hơn hẳn alcohol, aldehyde, ketone và hydrocarbon có cùng phân tử khối: $t_s(\\text{Acid}) > t_s(\\text{Alcohol}) > t_s(\\text{Aldehyde/Ketone/Ester}) > t_s(\\text{Hydrocarbon})$. Về hóa học, carboxylic acid thể hiện đầy đủ tính chất của một acid yếu (nhưng mạnh hơn $\\text{H}_2\\text{CO}_3$ và phenol) và tham gia phản ứng ester hóa thuận nghịch với alcohol (xúc tác $\\text{H}_2\\text{SO}_4$ đặc, đun nóng).",
        [
            F("So sánh Nhiệt độ sôi của các chất có phân tử khối tương đương", "t_s(\\text{RCOOH}) > t_s(\\text{R'CH}_2\\text{OH}) > t_s(\\text{R''CHO / R''COOR'''}) > t_s(\\text{Hydrocarbon})", "Carboxylic acid có nhiệt độ sôi cao nhất do liên kết hydrogen liên phân tử bền hơn alcohol"),
            F("Tính chất của một Acid (mạnh hơn H2CO3)", "\\begin{cases} 2\\text{RCOOH} + \\text{Mg} \\rightarrow (\\text{RCOO})_2\\text{Mg} + \\text{H}_2\\uparrow \\\\ 2\\text{RCOOH} + \\text{CaCO}_3 \\rightarrow (\\text{RCOO})_2\\text{Ca} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O} \\end{cases}", "Dung dịch carboxylic acid làm quỳ tím hóa đỏ"),
            F("Phản ứng Ester hóa tổng quát", "\\text{RCOOH} + \\text{R'OH} \\underset{t^\\circ}{\\overset{\\text{H}_2\\text{SO}_4\\text{ đặc}}{\\rightleftharpoons}} \\text{RCOOR'} + \\text{H}_2\\text{O}", "Trong phản ứng ester hóa: nhóm -OH tách ra từ phân tử acid, nguyên tử -H tách ra từ phân tử alcohol"),
        ],
        [
            "Viết được công thức cấu tạo, gọi tên theo danh pháp thay thế và tên thông thường ($\\text{HCOOH}$ formic acid, $\\text{CH}_3\\text{COOH}$ acetic acid, $\\text{CH}_2=\\text{CHCOOH}$ acrylic acid, $\\text{C}_6\\text{H}_5\\text{COOH}$ benzoic acid)",
            "Giải thích được thứ tự nhiệt độ sôi $t_s(\\text{Acid}) > t_s(\\text{Alcohol}) > t_s(\\text{Aldehyde}) > t_s(\\text{Alkane})$ khi có phân tử khối xấp xỉ nhau",
            "Viết được phương trình thể hiện tính acid và tính được hiệu suất phản ứng ester hóa",
        ],
        "Đun nóng $0,2\\text{ mol}$ $\\text{CH}_3\\text{COOH}$ với $0,3\\text{ mol}$ $\\text{C}_2\\text{H}_5\\text{OH}$ có mặt $\\text{H}_2\\text{SO}_4$ đặc làm xúc tác, sau phản ứng thu được $0,12\\text{ mol}$ ester $\\text{CH}_3\\text{COOC}_2\\text{H}_5$. Tính hiệu suất của phản ứng ester hóa.",
        "PTHH: $\\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH} \\rightleftharpoons \\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O}$ (tỉ lệ $1 : 1$).\nVì $n_{\\text{CH}_3\\text{COOH}} = 0,2\\text{ mol} < n_{\\text{C}_2\\text{H}_5\\text{OH}} = 0,3\\text{ mol}$ nên hiệu suất phản ứng được tính theo $\\text{CH}_3\\text{COOH}$.\nHiệu suất phản ứng: $H = \\frac{n_{\\text{ester}}}{n_{\\text{CH}_3\\text{COOH ban đầu}}} \\cdot 100\\% = \\frac{0,12}{0,2} \\cdot 100\\% = 60\\%$.",
        "Trong nọc độc của kiến lửa và ong có chứa formic acid ($\\text{HCOOH}$) gây đau rát và sưng tấy; khi bị kiến đốt, bôi một chút vôi tôi ($\\text{Ca(OH)}_2$) hoặc kem đánh răng (có tính kiềm nhẹ) sẽ trung hòa bớt acid và giảm sưng đau.",
        CH6_ID, CH6_TITLE, CH6_DESC,
        extra_questions=[
            mcq("Cho các chất có phân tử khối xấp xỉ nhau: propane ($M = 44$), ethanal ($M = 44$), ethanol ($M = 46$) và formic acid ($M = 46$). Chất có nhiệt độ sôi cao nhất là:", "Formic acid ($\\text{HCOOH}$)", ["Formic acid ($\\text{HCOOH}$)", "Ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$)", "Ethanal ($\\text{CH}_3\\text{CHO}$)", "Propane ($\\text{C}_3\\text{H}_8$)"], "Carboxylic acid tạo được liên kết hydrogen liên phân tử bền hơn alcohol nên có nhiệt độ sôi cao nhất.", "biet"),
            mcq("Trong cơ chế của phản ứng ester hóa giữa $\\text{CH}_3\\text{COOH}$ và $\\text{C}_2\\text{H}_5\\text{OH}$ (xúc tác $\\text{H}_2\\text{SO}_4$ đặc, $t^\\circ$), phân tử nước ($\\text{H}_2\\text{O}$) được tạo thành từ:", "Nhóm $-\\text{OH}$ của phân tử acid $\\text{CH}_3\\text{COOH}$ và nguyên tử $-\\text{H}$ trong nhóm $-\\text{OH}$ của alcohol $\\text{C}_2\\text{H}_5\\text{OH}$", ["Nhóm $-\\text{OH}$ của phân tử acid $\\text{CH}_3\\text{COOH}$ và nguyên tử $-\\text{H}$ trong nhóm $-\\text{OH}$ của alcohol $\\text{C}_2\\text{H}_5\\text{OH}$", "Nguyên tử $-\\text{H}$ của phân tử acid và nhóm $-\\text{OH}$ của phân tử alcohol", "Hai nguyên tử $-\\text{H}$ của nhóm $-\\text{CH}_3$", "Phân tử $\\text{H}_2\\text{SO}_4$ đặc phân hủy"], "Thực nghiệm đánh dấu đồng vị $^{18}\\text{O}$ trên alcohol chứng minh nhóm $-\\text{OH}$ tách ra từ acid và $-\\text{H}$ tách ra từ alcohol.", "hieu"),
            short("Cho $12\\text{ g}$ acetic acid ($\\text{CH}_3\\text{COOH}$, $M = 60$) tác dụng hết với lượng dư đá vôi ($\\text{CaCO}_3$). Tính số mol khí $\\text{CO}_2$ thoát ra.", "0,1", ["0,1", "0.1"], "Số mol $\\text{CH}_3\\text{COOH} = \\frac{12}{60} = 0,2\\text{ mol}$. Theo PTHH: $2\\text{CH}_3\\text{COOH} + \\text{CaCO}_3 \\rightarrow (\\text{CH}_3\\text{COO})_2\\text{Ca} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}$, nên $n_{\\text{CO}_2} = \\frac{1}{2}n_{\\text{acid}} = 0,1\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(21, "Chuỗi chuyển hóa và bài toán tổng hợp dẫn xuất hydrocarbon",
        "Sơ đồ chuyển hóa từ Hydrocarbon -> Dẫn xuất halogen -> Alcohol -> Aldehyde/Ketone -> Carboxylic acid -> Ester và bảo toàn khối lượng",
        "Hệ thống hóa mối liên hệ chuyển hóa giữa các loại hợp chất hữu cơ lớp 11: Từ hydrocarbon (alkane, alkene) qua phản ứng thế halogen hoặc cộng $\\text{HX}/\\text{H}_2\\text{O}$ thu được dẫn xuất halogen và alcohol; oxi hóa không hoàn toàn alcohol bậc I bằng $\\text{CuO}$ thu được aldehyde; oxi hóa aldehyde bằng $\\text{Br}_2 + \\text{H}_2\\text{O}$ (hoặc $\\text{O}_2, xt$) thu được carboxylic acid; cho carboxylic acid phản ứng với alcohol thu được ester. Ngược lại, khử aldehyde/ketone bằng $\\text{NaBH}_4$ hoặc $\\text{LiAlH}_4$ thu lại alcohol.",
        [
            F("Chuỗi chuyển hóa cốt lõi Hóa hữu cơ 11", "\\text{Alkene} \\xrightarrow{+\\text{H}_2\\text{O (H}^+\\text{)}} \\text{Alcohol bậc I} \\underset{+\\text{NaBH}_4}{\\overset{+\\text{CuO}, t^\\circ}{\\rightleftharpoons}} \\text{Aldehyde} \\xrightarrow{+\\text{O}_2\\text{ (xt)}} \\text{Carboxylic acid} \\xrightarrow{+\\text{R'OH}} \\text{Ester}", "Ví dụ: CH2=CH2 -> C2H5OH -> CH3CHO -> CH3COOH -> CH3COOC2H5"),
            F("Bảo toàn khối lượng và Bảo toàn nguyên tố khi đốt cháy CxHyOz", "\\begin{cases} m_X = m_{\\text{C}} + m_{\\text{H}} + m_{\\text{O}} = 12n_{\\text{CO}_2} + 2n_{\\text{H}_2\\text{O}} + 16n_{\\text{O (trong X)}} \\\\ \\text{Bảo toàn O: } n_{\\text{O (trong X)}} + 2n_{\\text{O}_2} = 2n_{\\text{CO}_2} + n_{\\text{H}_2\\text{O}} \\end{cases}", "Với alcohol no, đơn chức, mạch hở: n_alcohol = n_H2O - n_CO2; với aldehyde/ketone/acid no, đơn chức, mạch hở: n_CO2 = n_H2O"),
        ],
        [
            "Lập được sơ đồ chuyển hóa hai chiều giữa hydrocarbon, dẫn xuất halogen, alcohol, aldehyde/ketone và carboxylic acid",
            "Phân biệt được các lọ hóa chất hữu cơ mất nhãn bằng hệ thống thuốc thử đặc trưng ($\\text{Cu(OH)}_2$, thuốc thử Tollens, nước $\\text{Br}_2$, $\\text{Na}_2\\text{CO}_3$, $\\text{Na}$)",
            "Vận dụng định luật bảo toàn nguyên tố và bảo toàn khối lượng để giải bài toán đốt cháy hỗn hợp dẫn xuất hydrocarbon",
        ],
        "Đốt cháy hoàn toàn $m$ gam một hợp chất hữu cơ $X$ (chứa $\\text{C}, \\text{H}, \\text{O}$) cần dùng vừa đủ $0,25\\text{ mol}$ $\\text{O}_2$, thu được $0,2\\text{ mol}$ $\\text{CO}_2$ và $0,2\\text{ mol}$ $\\text{H}_2\\text{O}$. Tính giá trị của $m$ và số mol nguyên tử $\\text{O}$ có trong $m$ gam $X$.",
        "- Áp dụng định luật bảo toàn khối lượng:\n$m_X = m_{\\text{CO}_2} + m_{\\text{H}_2\\text{O}} - m_{\\text{O}_2} = 0,2 \\cdot 44 + 0,2 \\cdot 18 - 0,25 \\cdot 32 = 8,8 + 3,6 - 8,0 = 4,4\\text{ g}$.\n- Bảo toàn nguyên tố $\\text{O}$: $n_{\\text{O (trong X)}} = 2n_{\\text{CO}_2} + n_{\\text{H}_2\\text{O}} - 2n_{\\text{O}_2} = 2 \\cdot 0,2 + 0,2 - 2 \\cdot 0,25 = 0,1\\text{ mol}$.",
        "Từ nguồn nguyên liệu duy nhất là khí ethylene ($\\text{CH}_2=\\text{CH}_2$) tách từ khí mỏ dầu hoặc ethanol sinh học, ngành công nghiệp tổng hợp hữu cơ có thể sản xuất ra hàng loạt dung môi, giấm công nghiệp, hương liệu ester và vật liệu polymer.",
        CH6_ID, CH6_TITLE, CH6_DESC,
        extra_questions=[
            mcq("Khi đốt cháy hoàn toàn một aldehyde no, đơn chức, mạch hở hoặc một carboxylic acid no, đơn chức, mạch hở thì mối quan hệ giữa số mol $\\text{CO}_2$ và số mol $\\text{H}_2\\text{O}$ thu được là:", "$n_{\\text{CO}_2} = n_{\\text{H}_2\\text{O}}$", ["$n_{\\text{CO}_2} = n_{\\text{H}_2\\text{O}}$", "$n_{\\text{CO}_2} > n_{\\text{H}_2\\text{O}}$", "$n_{\\text{CO}_2} < n_{\\text{H}_2\\text{O}}$", "$n_{\\text{CO}_2} = 2n_{\\text{H}_2\\text{O}}$"], "Cả hai loại chất đều có độ bất bão hòa $k = 1$ (công thức dạng $\\text{C}_n\\text{H}_{2n}\\text{O}$ và $\\text{C}_n\\text{H}_{2n}\\text{O}_2$) nên khi đốt cháy luôn có $n_{\\text{CO}_2} = n_{\\text{H}_2\\text{O}}$.", "biet"),
            mcq("Cho sơ đồ chuyển hóa: $\\text{CH}_2=\\text{CH}_2 \\xrightarrow{+\\text{H}_2\\text{O}, \\text{H}^+} X \\xrightarrow{+\\text{CuO}, t^\\circ} Y \\xrightarrow{+\\text{Br}_2 + \\text{H}_2\\text{O}} Z$. Các chất $X, Y, Z$ lần lượt là:", "$\\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{CHO},\\; \\text{CH}_3\\text{COOH}$", ["$\\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{CHO},\\; \\text{CH}_3\\text{COOH}$", "$\\text{C}_2\\text{H}_6,\\; \\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{CHO}$", "$\\text{CH}_3\\text{CHO},\\; \\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{COOH}$", "$\\text{C}_2\\text{H}_5\\text{OH},\\; \\text{CH}_3\\text{COCH}_3,\\; \\text{CH}_3\\text{COOH}$"], "Hydrate hóa $\\text{C}_2\\text{H}_4$ tạo $\\text{C}_2\\text{H}_5\\text{OH}$ ($X$), oxi hóa bằng $\\text{CuO}$ tạo $\\text{CH}_3\\text{CHO}$ ($Y$), oxi hóa tiếp bằng nước $\\text{Br}_2$ tạo $\\text{CH}_3\\text{COOH}$ ($Z$).", "hieu"),
            short("Oxi hóa hoàn toàn $0,2\\text{ mol}$ $\\text{C}_2\\text{H}_5\\text{OH}$ bằng bột $\\text{CuO}$ dư đun nóng thu được $\\text{CH}_3\\text{CHO}$, hơi nước và bao nhiêu gam đồng ($\\text{Cu} = 64$) kim loại?", "12,8", ["12,8", "12.8"], "PTHH: $\\text{C}_2\\text{H}_5\\text{OH} + \\text{CuO} \\xrightarrow{t^\\circ} \\text{CH}_3\\text{CHO} + \\text{Cu} + \\text{H}_2\\text{O}$. Số mol $n_{\\text{Cu}} = 0,2\\text{ mol} \\Rightarrow m_{\\text{Cu}} = 0,2 \\cdot 64 = 12,8\\text{ g}$.", "vandung"),
        ]
    ),
]

LESSONS = (
    CH1_LESSONS + CH2_LESSONS + CH3_LESSONS
    + CH4_LESSONS + CH5_LESSONS + CH6_LESSONS
)
