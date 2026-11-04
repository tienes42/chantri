from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_12: list[dict[str, Any]] = [
    # =========================================================================
    # CHƯƠNG 1: ESTER – LIPID, XÀ PHÒNG VÀ CHẤT GIẶT RỬA
    # =========================================================================
    lesson(
        grade=12,
        order=1,
        code="H12-C01",
        title="Chương 1: Ester – Lipid, Xà phòng và Chất giặt rửa",
        topic="este-lipit",
        description=(
            "Chương 1 SGK Hóa học 12 Kết nối tri thức: Khái niệm, danh pháp IUPAC, "
            "tính chất vật lý, phản ứng thủy phân của ester; cấu tạo và chuyển hóa "
            "chất béo triglyceride, acid béo omega-3, omega-6; xà phòng và chất giặt rửa."
        ),
        summary=(
            r"Khi thay thế nhóm $-\text{OH}$ ở nhóm carboxyl ($-\text{COOH}$) của carboxylic acid bằng nhóm $-\text{OR'}$ "
            r"thì thu được **ester** có công thức chung đối với ester đơn chức là $\text{RCOOR'}$ (trong đó $\text{R}$ là gốc hydrocarbon "
            r"hoặc nguyên tử $\text{H}$; $\text{R'}$ là gốc hydrocarbon khác $\text{H}$). Ester no, đơn chức, mạch hở có công thức phân tử "
            r"$\text{C}_n\text{H}_{2n}\text{O}_2$ ($n \ge 2$). Do không có nguyên tử $\text{H}$ linh động gắn với nguyên tử $\text{O}$ nên các phân tử "
            r"ester không tạo được liên kết hydrogen liên phân tử, dẫn đến nhiệt độ sôi thấp hơn hẳn so với alcohol và carboxylic acid "
            r"có phân tử khối tương đương và ít tan trong nước. Phản ứng hóa học đặc trưng của ester là **phản ứng thủy phân**: "
            r"thủy phân trong môi trường acid là phản ứng thuận nghịch, còn thủy phân trong môi trường kiềm (phản ứng xà phòng hóa) "
            r"là phản ứng một chiều tạo muối carboxylate và alcohol (hoặc aldehyde, ketone, muối phenolate tùy cấu tạo). "
            r"**Lipid** bao gồm chất béo, sáp, steroid, phospholipid... trong đó **chất béo** là triester (triglyceride) của glycerol "
            r"$\text{C}_3\text{H}_5(\text{OH})_3$ với các acid béo (monocarboxylic acid có số chẵn nguyên tử $\text{C}$ từ $12\text{C}$ đến $24\text{C}$, "
            r"mạch không phân nhánh), có công thức chung $(\text{RCOO})_3\text{C}_3\text{H}_5$. **Xà phòng** là hỗn hợp muối sodium hoặc potassium "
            r"của các acid béo, còn **chất giặt rửa tổng hợp** là các muối sodium alkylsulfate $\text{R}-\text{OSO}_3\text{Na}$ hoặc "
            r"alkylbenzenesulfonate $\text{R}-\text{C}_6\text{H}_4-\text{SO}_3\text{Na}$ có cấu tạo gồm phần đầu phân cực ưa nước và phần đuôi "
            r"hydrocarbon dài kị nước giúp làm sạch vết bẩn dầu mỡ."
        ),
        objectives=[
            r"Nêu được khái niệm về lipid, chất béo, acid béo và đặc điểm cấu tạo phân tử ester $\text{RCOOR'}$, chất béo $(\text{RCOO})_3\text{C}_3\text{H}_5$.",
            r"Viết được công thức cấu tạo và gọi được tên các ester đơn giản theo danh pháp thay thế IUPAC và tên gốc – chức (số nguyên tử $\text{C}$ trong phân tử $\le 5$).",
            r"Giải thích được vì sao ester có nhiệt độ sôi thấp hơn hẳn so với alcohol và carboxylic acid có phân tử khối tương đương và ít tan trong nước dựa trên liên kết hydrogen.",
            r"Trình bày được tính chất hóa học đặc trưng của ester (phản ứng thủy phân trong môi trường acid và môi trường kiềm) và phương pháp điều chế ester bằng phản ứng ester hóa.",
            r"Trình bày được tính chất vật lý, tính chất hóa học của chất béo (phản ứng xà phòng hóa, phản ứng hydrogen hóa chất béo lỏng thành chất béo rắn, phản ứng oxi hóa bởi oxygen không khí gây ôi mỡ) và vai trò của acid béo $\text{omega-3}$, $\text{omega-6}$.",
            r"Nêu được khái niệm, đặc điểm cấu tạo phần ưa nước – phần kị nước, giải thích được cơ chế giặt rửa và so sánh được ưu, nhược điểm của xà phòng với chất giặt rửa tổng hợp, chất giặt rửa tự nhiên.",
        ],
        formulas=[
            {
                "name": "Công thức chung của ester đơn chức và ester no, đơn chức, mạch hở",
                "formula": r"$\text{RCOOR'}$ ($\text{R'}$ là gốc hydrocarbon); ester no, đơn chức, mạch hở: $\text{C}_n\text{H}_{2n}\text{O}_2$ ($n \ge 2$)",
                "note": r"Số đồng phân cấu tạo ester no, đơn chức, mạch hở ứng với $n = 2, 3, 4$ lần lượt là $2^{n-2}$ ($1, 2, 4$ đồng phân).",
            },
            {
                "name": "Phản ứng điều chế ester (phản ứng ester hóa thuận nghịch)",
                "formula": r"$\text{RCOOH} + \text{R'OH} \stackrel{\text{H}_2\text{SO}_4\text{ đặc, } t^\circ}{\rightleftharpoons} \text{RCOOR'} + \text{H}_2\text{O}$",
                "note": r"Nguyên tử $\text{O}$ của nhóm $-\text{OH}$ trong phân tử carboxylic acid kết hợp với nguyên tử $\text{H}$ của nhóm $-\text{OH}$ trong alcohol tách ra tạo $\text{H}_2\text{O}$.",
            },
            {
                "name": "Phản ứng thủy phân ester trong môi trường acid (thuận nghịch)",
                "formula": r"$\text{RCOOR'} + \text{H}_2\text{O} \stackrel{\text{H}^+, t^\circ}{\rightleftharpoons} \text{RCOOH} + \text{R'OH}$",
                "note": r"Phản ứng xảy ra không hoàn toàn, sau phản ứng hỗn hợp tách thành hai lớp nếu ester còn dư ít tan.",
            },
            {
                "name": "Phản ứng thủy phân ester trong môi trường kiềm (phản ứng xà phòng hóa)",
                "formula": r"$\text{RCOOR'} + \text{NaOH} \xrightarrow{t^\circ} \text{RCOONa} + \text{R'OH}$",
                "note": r"Phản ứng một chiều. Trường hợp đặc biệt: $\text{RCOOCH}=\text{CH}-\text{R'} + \text{NaOH} \xrightarrow{t^\circ} \text{RCOONa} + \text{R'CH}_2\text{CHO}$; $\text{RCOOC}_6\text{H}_5 + 2\text{NaOH} \xrightarrow{t^\circ} \text{RCOONa} + \text{C}_6\text{H}_5\text{ONa} + \text{H}_2\text{O}$.",
            },
            {
                "name": "Phản ứng xà phòng hóa chất béo (triglyceride)",
                "formula": r"$(\text{RCOO})_3\text{C}_3\text{H}_5 + 3\text{NaOH} \xrightarrow{t^\circ} 3\text{RCOONa} + \text{C}_3\text{H}_5(\text{OH})_3$",
                "note": r"Bảo toàn khối lượng: $m_{\text{chất béo}} + m_{\text{NaOH}} = m_{\text{muối (xà phòng)}} + m_{\text{glycerol}}$ với $n_{\text{NaOH}} = 3n_{\text{chất béo}} = 3n_{\text{glycerol}}$.",
            },
            {
                "name": "Phản ứng hydrogen hóa chất béo lỏng thành chất béo rắn",
                "formula": r"$(\text{C}_{17}\text{H}_{33}\text{COO})_3\text{C}_3\text{H}_5 + 3\text{H}_2 \xrightarrow{\text{Ni}, t^\circ, p} (\text{C}_{17}\text{H}_{35}\text{COO})_3\text{C}_3\text{H}_5$",
                "note": r"Chuyển triolein ($M = 884\text{ g/mol}$, lỏng) thành tristearin ($M = 890\text{ g/mol}$, rắn) để sản xuất bơ nhân tạo (margarine).",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 1. Ester – Lipid",
                "content": [
                    r"**Khái niệm và danh pháp IUPAC của ester**: Ester đơn chức có công thức chung $\text{RCOOR'}$. Tên gọi của ester $\text{RCOOR'}$ gồm: **Tên gốc $\text{R'}$ + tên gốc carboxylic acid $\text{RCOO}^-$ (đuôi `ate`)**. Ví dụ: $\text{HCOOCH}_3$ là $\text{methyl methanoate}$ ($\text{methyl formate}$); $\text{CH}_3\text{COOC}_2\text{H}_5$ là $\text{ethyl ethanoate}$ ($\text{ethyl acetate}$); $\text{CH}_3\text{COOCH}=\text{CH}_2$ là $\text{vinyl acetate}$; $\text{CH}_2=\text{C(CH}_3)\text{COOCH}_3$ là $\text{methyl methacrylate}$; $\text{C}_6\text{H}_5\text{COOCH}_3$ là $\text{methyl benzoate}$; $\text{CH}_3\text{COOC}_6\text{H}_5$ là $\text{phenyl acetate}$; $\text{CH}_3\text{COOCH}_2\text{CH}_2\text{CH(CH}_3)_2$ là $\text{isoamyl acetate}$ (mùi chuối chín).",
                    r"**Tính chất vật lý của ester**: Các ester thường là chất lỏng hoặc chất rắn ở điều kiện thường, nhẹ hơn nước, rất ít tan trong nước và có mùi thơm đặc trưng của hoa quả (như $\text{isoamyl acetate}$ mùi chuối chín, $\text{benzyl acetate}$ mùi hoa nhài, $\text{ethyl butyrate}$ và $\text{ethyl propionate}$ mùi dứa chín, $\text{geranyl acetate}$ mùi hoa hồng). Do giữa các phân tử ester không có liên kết hydrogen liên phân tử nên ester có nhiệt độ sôi thấp hơn nhiều so với alcohol và carboxylic acid có cùng số nguyên tử carbon hoặc phân tử khối tương đương.",
                    r"**Tính chất hóa học của ester**: Phản ứng đặc trưng là phản ứng thủy phân ở nhóm chức $-\text{COO}-$. Khi đun nóng với dung dịch acid loãng ($\text{H}_2\text{SO}_4$ loãng), phản ứng thủy phân xảy ra thuận nghịch tạo carboxylic acid và alcohol. Khi đun nóng với dung dịch kiềm ($\text{NaOH}, \text{KOH}$), phản ứng xảy ra một chiều (phản ứng xà phòng hóa). Ngoài ra, các ester có gốc không no còn tham gia phản ứng cộng ($\text{H}_2, \text{Br}_2$) và phản ứng trùng hợp (như trùng hợp $\text{methyl methacrylate}$ tạo thủy tinh hữu cơ plexiglas); các ester của formic acid $\text{HCOOR'}$ có khả năng tham gia phản ứng tráng bạc với thuốc thử Tollens.",
                    r"**Điều chế ester**: Ester của alcohol thường được điều chế bằng cách đun sôi hỗn hợp carboxylic acid và alcohol có $\text{H}_2\text{SO}_4$ đặc làm xúc tác (đồng thời hút nước để chuyển dịch cân bằng theo chiều thuận). Riêng $\text{vinyl acetate}$ được điều chế từ acetic acid và acetylene hoặc ethylene; $\text{phenyl acetate}$ phải điều chế từ phenol và acetic anhydride $(\text{CH}_3\text{CO})_2\text{O}$ (không điều chế trực tiếp từ carboxylic acid và phenol).",
                    r"**Khái niệm lipid, chất béo và acid béo**: Lipid là các hợp chất hữu cơ có trong tế bào sống, không tan trong nước nhưng tan trong dung môi hữu cơ không phân cực. Chất béo là triester của glycerol với acid béo, gọi chung là triglyceride. Các acid béo thường gặp gồm: **acid béo no** như palmitic acid $\text{C}_{15}\text{H}_{31}\text{COOH}$ ($M = 256\text{ g/mol}$), stearic acid $\text{C}_{17}\text{H}_{35}\text{COOH}$ ($M = 284\text{ g/mol}$) tạo nên chất béo rắn (tripalmitin $M = 806\text{ g/mol}$, tristearin $M = 890\text{ g/mol}$); **acid béo không no** (có cấu hình $\text{cis}$) như oleic acid $\text{C}_{17}\text{H}_{33}\text{COOH}$ ($1$ liên kết đôi $\text{C}=\text{C}$, $M = 282\text{ g/mol}$), linoleic acid $\text{C}_{17}\text{H}_{31}\text{COOH}$ ($2$ liên kết đôi $\text{C}=\text{C}$, $M = 280\text{ g/mol}$, thuộc nhóm $\text{omega-6}$) và linolenic acid $\text{C}_{17}\text{H}_{29}\text{COOH}$, $\text{DHA}$, $\text{EPA}$ (thuộc nhóm $\text{omega-3}$) tạo nên chất béo lỏng (dầu thực vật, dầu cá).",
                    r"**Tính chất hóa học của chất béo**: Gồm phản ứng thủy phân trong môi trường acid (tạo acid béo và glycerol), phản ứng xà phòng hóa trong môi trường kiềm (tạo muối của acid béo – xà phòng và glycerol), phản ứng hydrogen hóa chất béo lỏng thành chất béo rắn (có xúc tác $\text{Ni}, t^\circ$), và phản ứng oxi hóa nối đôi $\text{C}=\text{C}$ bởi oxygen không khí tạo ra các peroxide và aldehyde có mùi khó chịu (hiện tượng dầu mỡ bị ôi).",
                ],
            },
            {
                "title": "Bài 2. Xà phòng và chất giặt rửa",
                "content": [
                    r"**Khái niệm và cấu tạo**: **Xà phòng** là hỗn hợp muối sodium hoặc potassium của các acid béo (như sodium palmitate $\text{C}_{15}\text{H}_{31}\text{COONa}$, sodium stearate $\text{C}_{17}\text{H}_{35}\text{COONa}$) và các chất phụ gia. **Chất giặt rửa tổng hợp** không phải là muối của acid béo mà thường là các muối sodium alkylsulfate ($\text{R}-\text{OSO}_3\text{Na}$, như $\text{CH}_3[\text{CH}_2]_{11}\text{OSO}_3\text{Na}$) hoặc sodium alkylbenzenesulfonate ($\text{R}-\text{C}_6\text{H}_4-\text{SO}_3\text{Na}$, như $\text{CH}_3[\text{CH}_2]_{11}\text{C}_6\text{H}_4\text{SO}_3\text{Na}$). Cả hai đều có cấu tạo gồm **phần đầu ưa nước** (nhóm $-\text{COO}^-\text{Na}^+$, $-\text{OSO}_3^-\text{Na}^+$, $-\text{SO}_3^-\text{Na}^+$ quay ra phía các phân tử nước) và **phần đuôi kị nước – ưa dầu mỡ** (gốc hydrocarbon mạch dài $\text{R}-$ thâm nhập vào vết bẩn dầu mỡ).",
                    r"**Cơ chế giặt rửa**: Khi hòa tan vào nước, các phân tử xà phòng hoặc chất giặt rửa làm giảm sức căng bề mặt của nước. Đuôi kị nước thâm nhập vào vết dầu mỡ, còn đầu ưa nước hướng ra ngoài tiếp xúc với nước, phân chia vết dầu mỡ thành các hạt rất nhỏ (hệ nhũ tương / micelle) phân tán vào nước và bị rửa trôi khỏi bề mặt vải.",
                    r"**Phương pháp sản xuất và ưu, nhược điểm**: Xà phòng được sản xuất bằng cách đun chất béo với dung dịch $\text{NaOH}$ hoặc $\text{KOH}$ đặc (sau đó thêm dung dịch $\text{NaCl}$ bão hòa để tách xà phòng nổi lên trên), dễ bị phân hủy sinh học nên thân thiện với môi trường, nhưng **không dùng được trong nước cứng** vì tạo kết tủa muối calcium / magnesium của acid béo như $(\text{C}_{17}\text{H}_{35}\text{COO})_2\text{Ca}$ bám lên vải và làm giảm tác dụng giặt rửa. Chất giặt rửa tổng hợp được sản xuất từ dầu mỏ, **dùng được trong nước cứng** vì muối $\text{Ca}^{2+}, \text{Mg}^{2+}$ của acid alkylsulfuric / alkylbenzenesulfonic vẫn tan, nhưng những loại chứa gốc hydrocarbon phân nhánh khó bị vi sinh vật phân hủy, gây ô nhiễm môi trường. Ngoài ra, chất giặt rửa tự nhiên (từ bồ kết, bồ hòn chứa saponin) an toàn cho da và dễ phân hủy sinh học.",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: So sánh nhiệt độ sôi và gọi tên ester",
                "problem": (
                    r"Cho các chất hữu cơ sau: (1) $\text{CH}_3\text{COOC}_2\text{H}_5$, (2) $\text{C}_3\text{H}_7\text{COOH}$, "
                    r"(3) $\text{CH}_3\text{CH}_2\text{CH}_2\text{CH}_2\text{OH}$. Hãy gọi tên chất (1) theo danh pháp IUPAC "
                    r"và sắp xếp các chất theo chiều tăng dần nhiệt độ sôi."
                ),
                "solution": (
                    r"- Chất (1) $\text{CH}_3\text{COOC}_2\text{H}_5$ có gốc alcohol là $\text{ethyl}$ ($-\text{C}_2\text{H}_5$) và gốc acid là "
                    r"$\text{ethanoate}$ ($\text{acetate}$, $\text{CH}_3\text{COO}-$), nên tên gọi là $\text{ethyl ethanoate}$ ($\text{ethyl acetate}$)." "\n"
                    r"- Cả ba chất đều có $4$ nguyên tử $\text{C}$ ($M_{(1)} = M_{(2)} = 88\text{ g/mol}$, $M_{(3)} = 74\text{ g/mol}$). "
                    r"Chất (1) là ester không có liên kết hydrogen liên phân tử nên có nhiệt độ sôi thấp nhất ($77{,}1^\circ\text{C}$). "
                    r"Chất (3) là alcohol và chất (2) là carboxylic acid đều có liên kết hydrogen liên phân tử, nhưng liên kết hydrogen giữa các phân tử "
                    r"carboxylic acid bền hơn alcohol (tạo dimer vòng). Vậy thứ tự nhiệt độ sôi tăng dần là: $(1) < (3) < (2)$."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán xà phòng hóa chất béo",
                "problem": (
                    r"Xà phòng hóa hoàn toàn $44{,}2\text{ g}$ một chất béo $\text{X}$ cần vừa đủ $60\text{ mL}$ dung dịch $\text{NaOH } 2{,}5\text{ M}$ "
                    r"đun nóng. Tính khối lượng xà phòng nguyên chất (muối sodium của acid béo) thu được sau phản ứng."
                ),
                "solution": (
                    r"- Số mol $\text{NaOH}$ phản ứng: $n_{\text{NaOH}} = 0{,}06 \cdot 2{,}5 = 0{,}15\text{ mol}$." "\n"
                    r"- Theo phương trình xà phòng hóa triglyceride: $(\text{RCOO})_3\text{C}_3\text{H}_5 + 3\text{NaOH} \xrightarrow{t^\circ} 3\text{RCOONa} + \text{C}_3\text{H}_5(\text{OH})_3$." "\n"
                    r"- Ta có $n_{\text{C}_3\text{H}_5(\text{OH})_3} = \dfrac{1}{3}n_{\text{NaOH}} = \dfrac{0{,}15}{3} = 0{,}05\text{ mol}$." "\n"
                    r"- Áp dụng định luật bảo toàn khối lượng: $m_{\text{muối}} = m_{\text{X}} + m_{\text{NaOH}} - m_{\text{glycerol}} = 44{,}2 + 0{,}15 \cdot 40 - 0{,}05 \cdot 92 = 45{,}6\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Ester no, đơn chức, mạch hở có công thức chung $\text{C}_n\text{H}_{2n}\text{O}_2$ ($n \ge 2$); nhiệt độ sôi theo thứ tự: $\text{ester} < \text{alcohol} < \text{carboxylic acid}$ có cùng phân tử khối tương đương.",
            r"Thủy phân ester trong môi trường acid ($\text{H}^+, t^\circ$) là phản ứng thuận nghịch; thủy phân trong môi trường kiềm ($\text{OH}^-, t^\circ$) là phản ứng một chiều (phản ứng xà phòng hóa).",
            r"Chất béo là triester của glycerol với acid béo $(\text{RCOO})_3\text{C}_3\text{H}_5$; acid béo $\text{omega-3}$ và $\text{omega-6}$ có liên kết đôi $\text{C}=\text{C}$ đầu tiên ở vị trí carbon số $3$ và số $6$ tính từ nhóm $-\text{CH}_3$ cuối mạch.",
            r"Xà phòng ($\text{RCOONa}$) dễ phân hủy sinh học nhưng tạo kết tủa $(\text{RCOO})_2\text{Ca}$, $(\text{RCOO})_2\text{Mg}$ trong nước cứng; chất giặt rửa tổng hợp ($\text{R}-\text{OSO}_3\text{Na}$) dùng được trong nước cứng.",
        ],
        questions=[
            mcq(
                question=r"Ester $\text{CH}_3\text{COOC}_2\text{H}_5$ có mùi thơm dễ chịu, được dùng làm dung môi trong công nghiệp. Tên gọi của $\text{CH}_3\text{COOC}_2\text{H}_5$ là:",
                options=[
                    r"Methyl acetate.",
                    r"Ethyl acetate.",
                    r"Ethyl formate.",
                    r"Methyl propionate.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Ester $\text{CH}_3\text{COOC}_2\text{H}_5$ được tạo bởi gốc $\text{ethyl}$ ($-\text{C}_2\text{H}_5$) và gốc "
                    r"$\text{acetate}$ ($\text{ethanoate}$, $\text{CH}_3\text{COO}-$), nên có tên là $\text{ethyl acetate}$ ($\text{ethyl ethanoate}$)."
                ),
            ),
            mcq(
                question=r"Công thức phân tử tổng quát của ester no, đơn chức, mạch hở là:",
                options=[
                    r"$\text{C}_n\text{H}_{2n}\text{O}_2$ ($n \ge 2$).",
                    r"$\text{C}_n\text{H}_{2n+2}\text{O}_2$ ($n \ge 2$).",
                    r"$\text{C}_n\text{H}_{2n-2}\text{O}_2$ ($n \ge 3$).",
                    r"$\text{C}_n\text{H}_{2n}\text{O}$ ($n \ge 2$).",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Ester no, đơn chức, mạch hở có $1$ liên kết $\pi$ ở nhóm chức $-\text{COO}-$ (độ bất bão hòa $k = 1$), "
                    r"nên có công thức chung là $\text{C}_n\text{H}_{2n}\text{O}_2$ với $n \ge 2$ (nhỏ nhất là $\text{HCOOCH}_3$, $\text{C}_2\text{H}_4\text{O}_2$)."
                ),
            ),
            mcq(
                question=r"Acid béo nào sau đây là acid béo không no có trong thành phần của nhiều loại dầu thực vật?",
                options=[
                    r"Palmitic acid ($\text{C}_{15}\text{H}_{31}\text{COOH}$).",
                    r"Stearic acid ($\text{C}_{17}\text{H}_{35}\text{COOH}$).",
                    r"Oleic acid ($\text{C}_{17}\text{H}_{33}\text{COOH}$).",
                    r"Acetic acid ($\text{CH}_3\text{COOH}$).",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"$\text{Oleic acid}$ ($\text{C}_{17}\text{H}_{33}\text{COOH}$) là acid béo không no có $1$ liên kết đôi $\text{C}=\text{C}$ dạng $\text{cis}$ "
                    r"trong gốc hydrocarbon. $\text{Palmitic acid}$ và $\text{stearic acid}$ là các acid béo no, còn $\text{acetic acid}$ không phải acid béo."
                ),
            ),
            mcq(
                question=r"Chất nào sau đây là thành phần chính của chất giặt rửa tổng hợp phổ biến?",
                options=[
                    r"$\text{CH}_3[\text{CH}_2]_{11}\text{OSO}_3\text{Na}$.",
                    r"$\text{C}_{15}\text{H}_{31}\text{COONa}$.",
                    r"$\text{C}_{17}\text{H}_{35}\text{COOK}$.",
                    r"$(\text{C}_{17}\text{H}_{35}\text{COO})_3\text{C}_3\text{H}_5$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"$\text{CH}_3[\text{CH}_2]_{11}\text{OSO}_3\text{Na}$ (sodium laurylsulfate) là muối sodium alkylsulfate dùng làm chất giặt rửa tổng hợp. "
                    r"$\text{C}_{15}\text{H}_{31}\text{COONa}$ và $\text{C}_{17}\text{H}_{35}\text{COOK}$ là thành phần của xà phòng, còn $(\text{C}_{17}\text{H}_{35}\text{COO})_3\text{C}_3\text{H}_5$ là chất béo."
                ),
            ),
            mcq(
                question=r"Số đồng phân cấu tạo là ester ứng với công thức phân tử $\text{C}_4\text{H}_8\text{O}_2$ là:",
                options=[
                    r"$2$.",
                    r"$3$.",
                    r"$4$.",
                    r"$5$.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"Ứng với $\text{C}_4\text{H}_8\text{O}_2$ ($n = 4$), số đồng phân ester là $2^{4-2} = 4$ đồng phân: "
                    r"(1) $\text{HCOOCH}_2\text{CH}_2\text{CH}_3$ ($\text{propyl formate}$), "
                    r"(2) $\text{HCOOCH(CH}_3)_2$ ($\text{isopropyl formate}$), "
                    r"(3) $\text{CH}_3\text{COOC}_2\text{H}_5$ ($\text{ethyl acetate}$), "
                    r"(4) $\text{C}_2\text{H}_5\text{COOCH}_3$ ($\text{methyl propionate}$)."
                ),
            ),
            mcq(
                question=r"Đun nóng ester $\text{X}$ có công thức phân tử $\text{C}_4\text{H}_6\text{O}_2$ trong dung dịch $\text{NaOH}$ vừa đủ, thu được muối sodium acetate và một hợp chất hữu cơ $\text{Y}$ có khả năng tham gia phản ứng tráng bạc. Công thức cấu tạo của $\text{X}$ là:",
                options=[
                    r"$\text{CH}_3\text{COOCH}=\text{CH}_2$.",
                    r"$\text{CH}_2=\text{CHCOOCH}_3$.",
                    r"$\text{HCOOCH}=\text{CH}-\text{CH}_3$.",
                    r"$\text{HCOOCH}_2-\text{CH}=\text{CH}_2$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Vì thủy phân $\text{X}$ trong $\text{NaOH}$ tạo sodium acetate ($\text{CH}_3\text{COONa}$) nên $\text{X}$ có gốc $\text{CH}_3\text{COO}-$. "
                    r"Mặt khác $\text{X}$ có công thức phân tử $\text{C}_4\text{H}_6\text{O}_2$, suy ra $\text{X}$ là $\text{vinyl acetate}$ ($\text{CH}_3\text{COOCH}=\text{CH}_2$). "
                    r"Phương trình: $\text{CH}_3\text{COOCH}=\text{CH}_2 + \text{NaOH} \xrightarrow{t^\circ} \text{CH}_3\text{COONa} + \text{CH}_3\text{CHO}$ ($\text{Y}$ là $\text{acetaldehyde}$ tráng bạc)."
                ),
            ),
            tf4(
                stem=(
                    r"Tiến hành thí nghiệm điều chế $\text{ethyl acetate}$ trong phòng thí nghiệm: Cho $1\text{ mL}$ $\text{ethanol}$, "
                    r"$1\text{ mL}$ $\text{acetic acid}$ nguyên chất và vài giọt dung dịch $\text{H}_2\text{SO}_4$ đặc vào ống nghiệm. "
                    r"Lắc đều, đun cách thủy (trong nồi nước nóng $65^\circ\text{C}\text{–}70^\circ\text{C}$) khoảng $5\text{ phút}$, "
                    r"sau đó làm lạnh rồi rót thêm $2\text{ mL}$ dung dịch $\text{NaCl}$ bão hòa vào ống nghiệm."
                ),
                statements=[
                    r"Phản ứng xảy ra trong ống nghiệm là phản ứng ester hóa thuận nghịch: $\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \stackrel{\text{H}_2\text{SO}_4\text{ đặc, } t^\circ}{\rightleftharpoons} \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$.",
                    r"Dung dịch $\text{H}_2\text{SO}_4$ đặc có thể được thay thế bằng dung dịch $\text{HNO}_3$ đặc hoặc $\text{HCl}$ loãng mà hiệu suất thu ester vẫn không thay đổi.",
                    r"Việc thêm dung dịch $\text{NaCl}$ bão hòa vào sau khi làm lạnh làm tăng khối lượng riêng của lớp dung dịch nước và giảm độ tan của $\text{ethyl acetate}$, giúp ester tách lớp nổi lên trên rõ hơn.",
                    r"Trong phản ứng ester hóa trên, nguyên tử oxygen trong phân tử $\text{H}_2\text{O}$ tạo thành có nguồn gốc từ nhóm $-\text{OH}$ của phân tử $\text{ethanol}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Phản ứng giữa $\text{CH}_3\text{COOH}$ và $\text{C}_2\text{H}_5\text{OH}$ có mặt $\text{H}_2\text{SO}_4$ đặc đun nóng là phản ứng ester hóa thuận nghịch." "\n"
                    r"- **b) Sai**: $\text{H}_2\text{SO}_4$ đặc vừa đóng vai trò chất xúc tác vừa là chất hút nước để chuyển dịch cân bằng theo chiều thuận; không thể thay bằng $\text{HCl}$ loãng (có nhiều nước làm cân bằng chuyển dịch nghịch) hay $\text{HNO}_3$ đặc (dễ oxi hóa alcohol và dễ bay hơi)." "\n"
                    r"- **c) Đúng**: Dung dịch $\text{NaCl}$ bão hòa làm giảm độ tan của $\text{CH}_3\text{COOC}_2\text{H}_5$ và tăng khối lượng riêng phần dung dịch bên dưới, giúp lớp ester nhẹ hơn ($D \approx 0{,}9\text{ g/cm}^3$) nổi lên trên bề mặt." "\n"
                    r"- **d) Sai**: Theo cơ chế phản ứng ester hóa, nhóm $-\text{OH}$ tách ra từ phân tử $\text{carboxylic acid}$ ($\text{CH}_3\text{COOH}$) kết hợp với nguyên tử $\text{H}$ của nhóm $-\text{OH}$ trong $\text{alcohol}$ ($\text{C}_2\text{H}_5\text{OH}$) để tạo thành $\text{H}_2\text{O}$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét cấu tạo, tính chất của chất béo, acid béo, xà phòng và chất giặt rửa tổng hợp trong đời sống và sản xuất."
                ),
                statements=[
                    r"Dầu thực vật và dầu cá chứa chủ yếu các triglyceride của acid béo không no nên thường ở trạng thái lỏng ở nhiệt độ phòng ($25^\circ\text{C}$).",
                    r"Khi đun nóng $\text{triolein}$ với dung dịch $\text{NaOH}$ dư sẽ thu được $\text{sodium stearate}$ và $\text{glycerol}$.",
                    r"Không nên dùng xà phòng để giặt quần áo trong nước cứng (chứa nhiều ion $\text{Ca}^{2+}, \text{Mg}^{2+}$) vì tạo kết tủa muối calcium, magnesium của acid béo bám lên sợi vải.",
                    r"Phân tử $\text{linoleic acid}$ ($\text{CH}_3[\text{CH}_2]_4\text{CH}=\text{CHCH}_2\text{CH}=\text{CH}[\text{CH}_2]_7\text{COOH}$) thuộc nhóm acid béo $\text{omega-3}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Các triglyceride chứa chủ yếu gốc acid béo không no (như $\text{oleic acid}, \text{linoleic acid}$) có nhiệt độ nóng chảy thấp nên ở trạng thái lỏng ở $25^\circ\text{C}$." "\n"
                    r"- **b) Sai**: Thủy phân $\text{triolein}$ $(\text{C}_{17}\text{H}_{33}\text{COO})_3\text{C}_3\text{H}_5$ trong dung dịch $\text{NaOH}$ thu được $\text{sodium oleate}$ ($\text{C}_{17}\text{H}_{33}\text{COONa}$) và $\text{glycerol}$, không phải $\text{sodium stearate}$ ($\text{C}_{17}\text{H}_{35}\text{COONa}$)." "\n"
                    r"- **c) Đúng**: Ion $\text{Ca}^{2+}, \text{Mg}^{2+}$ trong nước cứng phản ứng với anion $\text{RCOO}^-$ của xà phòng tạo kết tủa $(\text{RCOO})_2\text{Ca}, (\text{RCOO})_2\text{Mg}$ làm tốn xà phòng và mục vải." "\n"
                    r"- **d) Sai**: Trong phân tử $\text{linoleic acid}$, liên kết đôi $\text{C}=\text{C}$ đầu tiên tính từ đầu nhóm $-\text{CH}_3$ ($\text{CH}_3-[\text{CH}_2]_4-\text{CH}=\text{CH}-...$) nằm ở vị trí nguyên tử carbon số $6$, nên $\text{linoleic acid}$ thuộc nhóm $\text{omega-6}$."
                ),
            ),
            mcq(
                question=(
                    r"Thực hiện phản ứng ester hóa giữa $12{,}0\text{ g}$ $\text{acetic acid}$ ($\text{CH}_3\text{COOH}$) và $13{,}8\text{ g}$ "
                    r"$\text{ethanol}$ ($\text{C}_2\text{H}_5\text{OH}$) có mặt $\text{H}_2\text{SO}_4$ đặc làm xúc tác. Sau khi phản ứng đạt "
                    r"trạng thái cân bằng, tách lấy được $11{,}0\text{ g}$ $\text{ethyl acetate}$. Hiệu suất của phản ứng ester hóa là:"
                ),
                options=[
                    r"$62{,}5\%$.",
                    r"$41{,}7\%$.",
                    r"$75{,}0\%$.",
                    r"$80{,}0\%$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Ta có $n_{\text{CH}_3\text{COOH}} = \dfrac{12{,}0}{60} = 0{,}20\text{ mol}$; "
                    r"$n_{\text{C}_2\text{H}_5\text{OH}} = \dfrac{13{,}8}{46} = 0{,}30\text{ mol}$. "
                    r"Theo phương trình $\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$, "
                    r"tỉ lệ mol phản ứng là $1:1$, mà $0{,}20 < 0{,}30$ nên hiệu suất tính theo $\text{CH}_3\text{COOH}$. "
                    r"Số mol ester thu được là $n_{\text{ester}} = \dfrac{11{,}0}{88} = 0{,}125\text{ mol}$. "
                    r"Vậy hiệu suất phản ứng là $H = \dfrac{0{,}125}{0{,}20} \cdot 100\% = 62{,}5\%$."
                ),
            ),
            short(
                question=(
                    r"Một loại mỡ động vật chứa $50\%$ $\text{tristearin}$ $(\text{C}_{17}\text{H}_{35}\text{COO})_3\text{C}_3\text{H}_5$ ($M = 890\text{ g/mol}$), "
                    r"$30\%$ $\text{tripalmitin}$ $(\text{C}_{15}\text{H}_{31}\text{COO})_3\text{C}_3\text{H}_5$ ($M = 806\text{ g/mol}$) và $20\%$ tạp chất trơ "
                    r"(về khối lượng). Đun nóng $100\text{ kg}$ loại mỡ này với dung dịch $\text{NaOH}$ dư để sản xuất bánh xà phòng chứa $72\%$ khối lượng "
                    r"muối sodium của các acid béo (giả sử hiệu suất phản ứng xà phòng hóa đạt $100\%$). Tính khối lượng xà phòng (theo đơn vị $\text{kg}$, "
                    r"làm tròn kết quả đến hàng phần mười) thu được."
                ),
                answer=["114,7", "114.7"],
                level="vandung",
                solution=(
                    r"- Trong $100\text{ kg}$ mỡ có: $m_{\text{tristearin}} = 50\text{ kg} \Rightarrow n_{\text{tristearin}} = \dfrac{50}{890}\text{ kmol}$, "
                    r"tạo ra $3 \cdot \dfrac{50}{890}\text{ kmol}$ $\text{C}_{17}\text{H}_{35}\text{COONa}$ ($M = 306\text{ g/mol}$), khối lượng muối là $\dfrac{150 \cdot 306}{890} \approx 51{,}573\text{ kg}$." "\n"
                    r"- Khối lượng $\text{tripalmitin}$ là $30\text{ kg} \Rightarrow n_{\text{tripalmitin}} = \dfrac{30}{806}\text{ kmol}$, "
                    r"tạo ra $3 \cdot \dfrac{30}{806}\text{ kmol}$ $\text{C}_{15}\text{H}_{31}\text{COONa}$ ($M = 278\text{ g/mol}$), khối lượng muối là $\dfrac{90 \cdot 278}{806} \approx 31{,}042\text{ kg}$." "\n"
                    r"- Tổng khối lượng muối sodium của các acid béo: $m_{\text{muối}} = 51{,}573 + 31{,}042 = 82{,}615\text{ kg}$." "\n"
                    r"- Khối lượng xà phòng chứa $72\%$ muối: $m_{\text{xà phòng}} = \dfrac{82{,}615}{0{,}72} \approx 114{,}7\text{ kg}$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 2: CARBOHYDRATE
    # =========================================================================
    lesson(
        grade=12,
        order=2,
        code="H12-C02",
        title="Chương 2: Carbohydrate (Glucose, Fructose, Saccharose, Maltose, Tinh bột, Cellulose)",
        topic="carbohydrate",
        description=(
            "Chương 2 SGK Hóa học 12 Kết nối tri thức: Phân loại carbohydrate, cấu tạo mạch hở và mạch vòng "
            "của glucose, fructose; tính chất hóa học và ứng dụng của glucose, fructose, saccharose, maltose, tinh bột, cellulose."
        ),
        summary=(
            r"**Carbohydrate** (gluxit, saccharide) là những hợp chất hữu cơ tạp chức, thường có công thức chung là $\text{C}_n(\text{H}_2\text{O})_m$, "
            r"được chia thành $3$ nhóm chính dựa trên khả năng thủy phân: **monosaccharide** (không bị thủy phân, như $\text{glucose}$ và $\text{fructose}$ "
            r"cùng có công thức phân tử $\text{C}_6\text{H}_{12}\text{O}_6$), **disaccharide** (thủy phân sinh ra $2$ phân tử monosaccharide, như "
            r"$\text{saccharose}$ và $\text{maltose}$ cùng có công thức phân tử $\text{C}_{12}\text{H}_{22}\text{O}_{11}$), và **polysaccharide** "
            r"(thủy phân đến cùng sinh ra nhiều phân tử monosaccharide, như **tinh bột** và $\text{cellulose}$ có công thức chung $(\text{C}_6\text{H}_{10}\text{O}_5)_n$). "
            r"Trong dung dịch, $\text{glucose}$ và $\text{fructose}$ tồn tại chủ yếu ở dạng mạch vòng ($\alpha$ và $\beta$) có nhóm $-\text{OH}$ hemiacetal / hemiketal "
            r"nằm cân bằng với một lượng nhỏ dạng mạch hở, nên chúng vừa thể hiện tính chất của **polyalcohol** (hòa tan $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo dung dịch xanh lam), "
            r"vừa có khả năng tham gia phản ứng tráng bạc với thuốc thử Tollens và tạo kết tủa đỏ gạch $\text{Cu}_2\text{O}$ với $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng "
            r"(trong môi trường kiềm, $\text{fructose}$ chuyển hóa thuận nghịch thành $\text{glucose}$); tuy nhiên chỉ $\text{glucose}$ làm mất màu dung dịch nước $\text{Br}_2$. "
            r"$\text{Saccharose}$ được tạo bởi $1$ gốc $\alpha\text{-glucose}$ và $1$ gốc $\beta\text{-fructose}$ liên kết qua nguyên tử $\text{O}$ giữa $\text{C}_1$ và $\text{C}_2$ "
            r"($\alpha\text{-1,2-glycoside}$) không còn nhóm $-\text{OH}$ hemiacetal nên không mở vòng và không có tính khử, còn $\text{maltose}$ còn nhóm $-\text{OH}$ hemiacetal. "
            r"**Tinh bột** gồm $\text{amylose}$ (mạch không phân nhánh, liên kết $\alpha\text{-1,4-glycoside}$) và $\text{amylopectin}$ (mạch phân nhánh, liên kết "
            r"$\alpha\text{-1,4-glycoside}$ và $\alpha\text{-1,6-glycoside}$), tạo hợp chất màu xanh tím đặc trưng với dung dịch $\text{I}_2$. "
            r"$\text{Cellulose}$ gồm các mắt xích $\beta\text{-glucose}$ liên kết $\beta\text{-1,4-glycoside}$ mạch thẳng không phân nhánh, viết gọn là "
            r"$[\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3]_n$, phản ứng với $\text{HNO}_3$ đặc / $\text{H}_2\text{SO}_4$ đặc tạo $\text{cellulose trinitrate}$ và tan trong nước Schweizer."
        ),
        objectives=[
            r"Phân loại được carbohydrate thành monosaccharide ($\text{glucose}, \text{fructose}$), disaccharide ($\text{saccharose}, \text{maltose}$) và polysaccharide ($\text{tinh bột}, \text{cellulose}$).",
            r"Trình bày được cấu tạo dạng mạch hở và dạng mạch vòng ($\alpha, \beta$) kèm nhóm $-\text{OH}$ hemiacetal / hemiketal của $\text{glucose}$ và $\text{fructose}$.",
            r"Trình bày được tính chất hóa học của $\text{glucose}$ và $\text{fructose}$: tính chất polyalcohol, tính chất aldehyde (tác dụng với thuốc thử Tollens, $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng, nước $\text{Br}_2$), phản ứng của nhóm $-\text{OH}$ hemiacetal với $\text{CH}_3\text{OH}/\text{HCl}$ khan và phản ứng lên men.",
            r"Giải thích được cấu tạo phân tử và trình bày được tính chất hóa học của $\text{saccharose}$ và $\text{maltose}$ (phản ứng với $\text{Cu(OH)}_2$, phản ứng thủy phân).",
            r"Phân biệt được cấu trúc phân tử của $\text{amylose}$, $\text{amylopectin}$ trong tinh bột và cấu trúc mạch thẳng của $\text{cellulose}$.",
            r"Trình bày được tính chất hóa học của tinh bột (thủy phân, phản ứng màu với $\text{I}_2$) và $\text{cellulose}$ (thủy phân, phản ứng với $\text{HNO}_3/\text{H}_2\text{SO}_4$ đặc tạo $\text{cellulose trinitrate}$, hòa tan trong nước Schweizer $[\text{Cu(NH}_3)_4](\text{OH})_2$).",
        ],
        formulas=[
            {
                "name": "Phản ứng hòa tan copper(II) hydroxide ở nhiệt độ thường (tính chất polyalcohol)",
                "formula": r"$2\text{C}_6\text{H}_{12}\text{O}_6 + \text{Cu(OH)}_2 \rightarrow (\text{C}_6\text{H}_{11}\text{O}_6)_2\text{Cu} + 2\text{H}_2\text{O}$",
                "note": r"Xảy ra với các chất có nhiều nhóm $-\text{OH}$ liền kề: $\text{glucose}, \text{fructose}, \text{saccharose}, \text{maltose}$ (tạo dung dịch màu xanh lam).",
            },
            {
                "name": "Phản ứng tráng bạc của glucose và fructose với thuốc thử Tollens",
                "formula": r"$\text{CH}_2\text{OH}[\text{CHOH}]_4\text{CHO} + 2[\text{Ag(NH}_3)_2]\text{OH} \xrightarrow{t^\circ} \text{CH}_2\text{OH}[\text{CHOH}]_4\text{COONH}_4 + 2\text{Ag}\downarrow + 3\text{NH}_3 + \text{H}_2\text{O}$",
                "note": r"$1\text{ mol}$ $\text{glucose}$ hoặc $1\text{ mol}$ $\text{fructose}$ tráng bạc tạo ra $2\text{ mol}$ $\text{Ag}\downarrow$ ($\text{fructose} \stackrel{\text{OH}^-}{\rightleftharpoons} \text{glucose}$).",
            },
            {
                "name": "Phản ứng của glucose với nước bromine (phân biệt glucose và fructose)",
                "formula": r"$\text{CH}_2\text{OH}[\text{CHOH}]_4\text{CHO} + \text{Br}_2 + \text{H}_2\text{O} \rightarrow \text{CH}_2\text{OH}[\text{CHOH}]_4\text{COOH} + 2\text{HBr}$",
                "note": r"Tạo $\text{gluconic acid}$, làm mất màu dung dịch $\text{Br}_2$. $\text{Fructose}$ không làm mất màu nước $\text{Br}_2$.",
            },
            {
                "name": "Phản ứng lên men rượu của glucose",
                "formula": r"$\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2\uparrow$",
                "note": r"Lên men lactic: $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{CH}_3\text{CH(OH)COOH}$.",
            },
            {
                "name": "Phản ứng thủy phân saccharose và tinh bột / cellulose",
                "formula": r"$\text{C}_{12}\text{H}_{22}\text{O}_{11}\text{ (saccharose)} + \text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} \text{C}_6\text{H}_{12}\text{O}_6\text{ (glucose)} + \text{C}_6\text{H}_{12}\text{O}_6\text{ (fructose)}$; $(\text{C}_6\text{H}_{10}\text{O}_5)_n + n\text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} n\text{C}_6\text{H}_{12}\text{O}_6$",
                "note": r"Thủy phân hoàn toàn $1\text{ mol}$ $\text{saccharose}$ rồi đem sản phẩm đi tráng bạc thu được $4\text{ mol}$ $\text{Ag}$.",
            },
            {
                "name": "Phản ứng điều chế cellulose trinitrate (thuốc súng không khói)",
                "formula": r"$[\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3]_n + 3n\text{HNO}_3\text{ (đặc)} \xrightarrow{\text{H}_2\text{SO}_4\text{ đặc, } t^\circ} [\text{C}_6\text{H}_7\text{O}_2(\text{ONO}_2)_3]_n + 3n\text{H}_2\text{O}$",
                "note": r"Khối lượng mol một mắt xích tăng từ $162\text{ g/mol}$ lên $297\text{ g/mol}$.",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 4. Giới thiệu về carbohydrate. Glucose và fructose",
                "content": [
                    r"**Phân loại carbohydrate**: Dựa vào sản phẩm thủy phân, chia thành $3$ nhóm: **Monosaccharide** ($\text{glucose}, \text{fructose}$ – $\text{C}_6\text{H}_{12}\text{O}_6$, không bị thủy phân), **Disaccharide** ($\text{saccharose}, \text{maltose}$ – $\text{C}_{12}\text{H}_{22}\text{O}_{11}$, thủy phân tạo $2$ phân tử monosaccharide) và **Polysaccharide** ($\text{tinh bột}, \text{cellulose}$ – $(\text{C}_6\text{H}_{10}\text{O}_5)_n$, thủy phân đến cùng tạo nhiều phân tử glucose).",
                    r"**Cấu tạo phân tử của glucose và fructose**: Ở dạng mạch hở, $\text{glucose}$ là một polyhydroxy aldehyde có $5$ nhóm $-\text{OH}$ liền kề và $1$ nhóm $-\text{CHO}$ ($\text{CH}_2\text{OH}-[\text{CHOH}]_4-\text{CHO}$), còn $\text{fructose}$ là một polyhydroxy ketone có $5$ nhóm $-\text{OH}$ và $1$ nhóm $-\text{CO}-$ ở vị trí $\text{C}_2$ ($\text{CH}_2\text{OH}-[\text{CHOH}]_3-\text{CO}-\text{CH}_2\text{OH}$). Trong dung dịch nước, chúng tồn tại chủ yếu ở dạng mạch vòng cân bằng với một lượng nhỏ dạng mạch hở: $\text{glucose}$ tạo vòng $6$ cạnh ($\alpha\text{-glucose}$ và $\beta\text{-glucose}$) có nhóm $-\text{OH}$ hemiacetal tại $\text{C}_1$; $\text{fructose}$ tạo vòng $5$ cạnh ($\alpha\text{-fructose}$ và $\beta\text{-fructose}$) có nhóm $-\text{OH}$ hemiketal tại $\text{C}_2$.",
                    r"**Tính chất hóa học của glucose và fructose**: (1) **Tính chất polyalcohol**: Cả $\text{glucose}$ và $\text{fructose}$ đều hòa tan $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo dung dịch phức đồng xanh lam $(\text{C}_6\text{H}_{11}\text{O}_6)_2\text{Cu}$. (2) **Tính chất aldehyde**: Khi đun nóng với thuốc thử Tollens ($[\text{Ag(NH}_3)_2]\text{OH}$) hoặc với $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng, cả $\text{glucose}$ và $\text{fructose}$ đều cho kết tủa bạc $\text{Ag}$ hoặc kết tủa đỏ gạch $\text{Cu}_2\text{O}$ (vì trong môi trường kiềm $\text{fructose}$ chuyển hóa thuận nghịch thành $\text{glucose}$). Tuy nhiên, **chỉ có $\text{glucose}$ làm mất màu dung dịch nước $\text{Br}_2$** tạo $\text{gluconic acid}$, còn $\text{fructose}$ không phản ứng với nước $\text{Br}_2$ (dùng để nhận biết $\text{glucose}$ và $\text{fructose}$). (3) **Tính chất của nhóm $-\text{OH}$ hemiacetal**: $\text{Glucose}$ tác dụng với $\text{CH}_3\text{OH}$ có mặt $\text{HCl}$ khan tạo $\text{methyl }\alpha\text{-glucoside}$ và $\text{methyl }\beta\text{-glucoside}$. (4) **Phản ứng khử và lên men**: Cả hai bị khử bởi $\text{H}_2$ ($\text{Ni}, t^\circ$) tạo $\text{sorbitol}$ $\text{C}_6\text{H}_{14}\text{O}_6$; $\text{glucose}$ lên men nhờ enzyme tạo $\text{ethanol}$ hoặc $\text{lactic acid}$.",
                ],
            },
            {
                "title": "Bài 5. Saccharose và maltose",
                "content": [
                    r"**Cấu tạo phân tử**: $\text{Saccharose}$ ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, đường mía) được tạo nên từ $1$ đơn vị $\alpha\text{-glucose}$ và $1$ đơn vị $\beta\text{-fructose}$ liên kết với nhau qua nguyên tử oxygen giữa $\text{C}_1$ của $\alpha\text{-glucose}$ và $\text{C}_2$ của $\beta\text{-fructose}$ (liên kết $\alpha\text{-1,2-glycoside}$). Do cả hai nhóm $-\text{OH}$ hemiacetal và hemiketal đã tham gia tạo liên kết glycoside nên phân tử $\text{saccharose}$ **không còn nhóm $-\text{OH}$ hemiacetal tự do**, chỉ tồn tại ở dạng mạch vòng và không thể mở vòng. Ngược lại, $\text{maltose}$ ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, đường mạch nha) gồm $2$ đơn vị $\text{glucose}$ liên kết qua $\alpha\text{-1,4-glycoside}$, vẫn còn $1$ nhóm $-\text{OH}$ hemiacetal tự do ở một gốc $\text{glucose}$ nên có thể mở vòng trong dung dịch nước.",
                    r"**Tính chất hóa học**: (1) **Phản ứng với $\text{Cu(OH)}_2$**: Cả $\text{saccharose}$ và $\text{maltose}$ đều có nhiều nhóm $-\text{OH}$ liền kề nên hòa tan $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo dung dịch màu xanh lam $(\text{C}_{12}\text{H}_{21}\text{O}_{11})_2\text{Cu}$. $\text{Saccharose}$ không có tính khử (không tráng bạc, không làm mất màu nước $\text{Br}_2$, không tạo kết tủa đỏ gạch với $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng), còn $\text{maltose}$ có tính khử. (2) **Phản ứng thủy phân**: Khi đun nóng với dung dịch acid vô cơ hoặc nhờ xúc tác enzyme, $\text{saccharose}$ thủy phân tạo thành $\text{glucose}$ và $\text{fructose}$ theo tỉ lệ mol $1 : 1$, còn $\text{maltose}$ thủy phân tạo $2$ phân tử $\text{glucose}$.",
                ],
            },
            {
                "title": "Bài 6. Tinh bột và cellulose",
                "content": [
                    r"**Cấu tạo của tinh bột và cellulose**: Cả hai đều là polysaccharide thiên nhiên có công thức chung $(\text{C}_6\text{H}_{10}\text{O}_5)_n$, nhưng **không phải là đồng phân của nhau** vì hệ số polymer hóa $n$ khác nhau và đơn vị mắt xích khác nhau. **Tinh bột** được tạo thành từ các đơn vị $\alpha\text{-glucose}$, gồm hai thành phần: $\text{amylose}$ (chiếm khoảng $20\text{–}30\%$, mạch không phân nhánh gồm các gốc $\alpha\text{-glucose}$ nối với nhau bằng liên kết $\alpha\text{-1,4-glycoside}$, xoắn thành hình lò xo) và $\text{amylopectin}$ (chiếm khoảng $70\text{–}80\%$, mạch phân nhánh gồm liên kết $\alpha\text{-1,4-glycoside}$ trên mạch chính và liên kết $\alpha\text{-1,6-glycoside}$ tại điểm phân nhánh). **Cellulose** được tạo thành từ các đơn vị $\beta\text{-glucose}$ nối với nhau bằng liên kết $\beta\text{-1,4-glycoside}$, tạo mạch thẳng kéo dài không phân nhánh; mỗi mắt xích $\text{C}_6\text{H}_{10}\text{O}_5$ có $3$ nhóm $-\text{OH}$ tự do nên được viết là $[\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3]_n$.",
                    r"**Tính chất hóa học của tinh bột**: (1) **Phản ứng thủy phân**: Nhờ xúc tác acid vô cơ loãng đun nóng hoặc enzyme ($\text{amylase}$), tinh bột bị thủy phân qua các sản phẩm trung gian ($\text{dextrin} \to \text{maltose}$) đến cuối cùng tạo thành $\text{glucose}$. (2) **Phản ứng màu với dung dịch $\text{I}_2$**: Do cấu trúc mạch $\text{amylose}$ xoắn thành hình lò xo rỗng bên trong, các phân tử $\text{I}_2$ đi vào trong ống xoắn tạo hợp chất bọc có **màu xanh tím** đặc trưng; khi đun nóng, mạch xoắn duỗi ra làm mất màu xanh tím, để nguội màu xanh tím xuất hiện trở lại.",
                    r"**Tính chất hóa học của cellulose**: (1) **Phản ứng thủy phân**: Đun nóng với dung dịch acid vô cơ ($\text{H}_2\text{SO}_4$ đặc $70\%$ hoặc $\text{HCl}$), $\text{cellulose}$ thủy phân đến cùng tạo $\text{glucose}$. (2) **Phản ứng với $\text{HNO}_3$ đặc / $\text{H}_2\text{SO}_4$ đặc**: Tạo $\text{cellulose dinitrate}$ và $\text{cellulose trinitrate}$ $[\text{C}_6\text{H}_7\text{O}_2(\text{ONO}_2)_3]_n$ – chất rất dễ cháy và nổ mạnh không sinh ra khói (thuốc súng không khói). (3) **Phản ứng với nước Schweizer**: $\text{Cellulose}$ không tan trong nước và các dung môi hữu cơ thông thường nhưng tan tốt trong **nước Schweizer** (dung dịch thu được khi hòa tan $\text{Cu(OH)}_2$ trong dung dịch $\text{NH}_3$ đặc, chứa phức $[\text{Cu(NH}_3)_4](\text{OH})_2$).",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Nhận biết các dung dịch carbohydrate",
                "problem": (
                    r"Trình bày phương pháp hóa học để phân biệt $4$ dung dịch mất nhãn riêng biệt: "
                    r"$\text{glucose}$, $\text{fructose}$, $\text{saccharose}$ và $\text{hồ tinh bột}$."
                ),
                "solution": (
                    r"- Nhỏ vài giọt dung dịch $\text{I}_2$ vào $4$ mẫu thử: mẫu thử chuyển sang màu xanh tím là $\text{hồ tinh bột}$." "\n"
                    r"- Cho $3$ mẫu thử còn lại tác dụng với thuốc thử Tollens ($[\text{Ag(NH}_3)_2]\text{OH}$) đun nóng: mẫu thử không xuất hiện kết tủa bạc $\text{Ag}$ là $\text{saccharose}$; hai mẫu xuất hiện lớp bạc sáng là $\text{glucose}$ và $\text{fructose}$." "\n"
                    r"- Nhỏ dung dịch nước $\text{Br}_2$ vào $2$ mẫu thử còn lại: mẫu làm mất màu nước $\text{Br}_2$ là $\text{glucose}$, mẫu không làm mất màu nước $\text{Br}_2$ là $\text{fructose}$."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán thủy phân tinh bột và lên men rượu",
                "problem": (
                    r"Từ $162\text{ g}$ tinh bột nguyên chất, tiến hành thủy phân thành $\text{glucose}$ rồi lên men tạo $\text{ethanol}$. "
                    r"Biết hiệu suất của cả quá trình là $80\%$. Tính khối lượng $\text{ethanol}$ thu được."
                ),
                "solution": (
                    r"- Sơ đồ chuyển hóa theo mắt xích tinh bột: $\text{C}_6\text{H}_{10}\text{O}_5 \xrightarrow{+\text{H}_2\text{O}} \text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$." "\n"
                    r"- Số mol mắt xích tinh bột: $n_{\text{C}_6\text{H}_{10}\text{O}_5} = \dfrac{162}{162} = 1{,}0\text{ mol}$." "\n"
                    r"- Số mol $\text{C}_2\text{H}_5\text{OH}$ thu được với hiệu suất $80\%$: $n_{\text{C}_2\text{H}_5\text{OH}} = 2 \cdot 1{,}0 \cdot 0{,}80 = 1{,}6\text{ mol}$." "\n"
                    r"- Khối lượng $\text{ethanol}$ thu được: $m_{\text{C}_2\text{H}_5\text{OH}} = 1{,}6 \cdot 46 = 73{,}6\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"$\text{Glucose}$ và $\text{fructose}$ đều hòa tan $\text{Cu(OH)}_2$ tạo dung dịch xanh lam và đều tráng bạc với thuốc thử Tollens, nhưng chỉ $\text{glucose}$ làm mất màu dung dịch nước $\text{Br}_2$.",
            r"$\text{Saccharose}$ không còn nhóm $-\text{OH}$ hemiacetal tự do nên không có tính khử (không tráng bạc), nhưng dung dịch sau thủy phân $\text{saccharose}$ có phản ứng tráng bạc.",
            r"Tinh bột gồm $\text{amylose}$ (không phân nhánh, liên kết $\alpha\text{-1,4-glycoside}$) và $\text{amylopectin}$ (phân nhánh, liên kết $\alpha\text{-1,4}$ và $\alpha\text{-1,6-glycoside}$); tinh bột tạo màu xanh tím với dung dịch $\text{I}_2$.",
            r"$\text{Cellulose}$ có cấu trúc mạch thẳng không phân nhánh gồm các mắt xích $\beta\text{-glucose}$ liên kết $\beta\text{-1,4-glycoside}$, tác dụng với $\text{HNO}_3/\text{H}_2\text{SO}_4$ đặc tạo $\text{cellulose trinitrate}$ và tan trong nước Schweizer.",
        ],
        questions=[
            mcq(
                question=r"Chất nào sau đây thuộc loại disaccharide?",
                options=[
                    r"Glucose.",
                    r"Fructose.",
                    r"Saccharose.",
                    r"Cellulose.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"$\text{Saccharose}$ ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) và $\text{maltose}$ thuộc loại disaccharide. "
                    r"$\text{Glucose}$ và $\text{fructose}$ là monosaccharide, còn $\text{cellulose}$ là polysaccharide."
                ),
            ),
            mcq(
                question=r"Nhỏ vài giọt dung dịch iodine ($\text{I}_2$) vào ống nghiệm đựng dung dịch hồ tinh bột để nguội thì quan sát thấy hiện tượng gì?",
                options=[
                    r"Xuất hiện kết tủa màu trắng.",
                    r"Dung dịch chuyển sang màu xanh tím.",
                    r"Xuất hiện kết tủa màu đỏ gạch.",
                    r"Dung dịch chuyển sang màu vàng.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Các phân tử $\text{amylose}$ trong hồ tinh bột có cấu trúc xoắn hình lò xo, giữ các phân tử $\text{I}_2$ tạo hợp chất bọc có màu xanh tím đặc trưng."
                ),
            ),
            mcq(
                question=r"Để phân biệt hai dung dịch $\text{glucose}$ và $\text{fructose}$ đựng trong hai lọ mất nhãn, ta có thể dùng thuốc thử nào sau đây?",
                options=[
                    r"Thuốc thử Tollens ($[\text{Ag(NH}_3)_2]\text{OH}$).",
                    r"$\text{Cu(OH)}_2$ ở nhiệt độ thường.",
                    r"Dung dịch nước bromine ($\text{Br}_2$).",
                    r"Kim loại $\text{Na}$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"$\text{Glucose}$ có nhóm $-\text{CHO}$ bị oxi hóa bởi nước $\text{Br}_2$ làm mất màu dung dịch $\text{Br}_2$, "
                    r"còn $\text{fructose}$ không làm mất màu nước $\text{Br}_2$. Với thuốc thử Tollens hoặc $\text{Cu(OH)}_2$, cả hai đều cho hiện tượng giống nhau."
                ),
            ),
            mcq(
                question=r"Phân tử $\text{cellulose}$ được cấu tạo từ các đơn vị monosaccharide nào liên kết với nhau?",
                options=[
                    r"Các đơn vị $\alpha\text{-glucose}$ liên kết $\alpha\text{-1,4-glycoside}$.",
                    r"Các đơn vị $\beta\text{-glucose}$ liên kết $\beta\text{-1,4-glycoside}$.",
                    r"Các đơn vị $\alpha\text{-glucose}$ và $\beta\text{-fructose}$ liên kết $\alpha\text{-1,2-glycoside}$.",
                    r"Các đơn vị $\beta\text{-fructose}$ liên kết $\beta\text{-1,6-glycoside}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Phân tử $\text{cellulose}$ được tạo thành từ rất nhiều đơn vị $\beta\text{-glucose}$ nối với nhau qua liên kết "
                    r"$\beta\text{-1,4-glycoside}$ tạo thành chuỗi mạch thẳng không phân nhánh."
                ),
            ),
            mcq(
                question=r"Dãy gồm các carbohydrate đều có khả năng hòa tan $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo dung dịch màu xanh lam nhưng KHÔNG tham gia phản ứng tráng bạc là:",
                options=[
                    r"Chỉ có $\text{saccharose}$.",
                    r"$\text{Saccharose}$ và $\text{maltose}$.",
                    r"$\text{Glucose}$ và $\text{fructose}$.",
                    r"$\text{Saccharose}$ và $\text{cellulose}$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"$\text{Saccharose}$ có nhiều nhóm $-\text{OH}$ liền kề nên hòa tan $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo dung dịch xanh lam, "
                    r"nhưng không còn nhóm $-\text{OH}$ hemiacetal nên không mở vòng và không tráng bạc. $\text{Maltose}, \text{glucose}, \text{fructose}$ đều tráng bạc, "
                    r"còn $\text{cellulose}$ không tan và không phản ứng với $\text{Cu(OH)}_2$ ở điều kiện thường."
                ),
            ),
            mcq(
                question=r"Cho sơ đồ chuyển hóa: $\text{Tinh bột} \xrightarrow{(1)} \text{X} \xrightarrow{(2)} \text{Y} \xrightarrow{(3)} \text{CH}_3\text{COOH}$. Hai chất $\text{X}$ và $\text{Y}$ lần lượt là:",
                options=[
                    r"$\text{Glucose}$ và $\text{ethyl alcohol}$.",
                    r"$\text{Saccharose}$ và $\text{glucose}$.",
                    r"$\text{Maltose}$ và $\text{sorbitol}$.",
                    r"$\text{Fructose}$ và $\text{gluconic acid}$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"(1) Thủy phân tinh bột tạo $\text{X}$ là $\text{glucose}$ ($\text{C}_6\text{H}_{12}\text{O}_6$): $(\text{C}_6\text{H}_{10}\text{O}_5)_n + n\text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} n\text{C}_6\text{H}_{12}\text{O}_6$. "
                    r"(2) Lên men $\text{glucose}$ tạo $\text{Y}$ là $\text{ethyl alcohol}$ ($\text{C}_2\text{H}_5\text{OH}$): $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$. "
                    r"(3) Lên men giấm $\text{C}_2\text{H}_5\text{OH} + \text{O}_2 \xrightarrow{\text{enzyme}} \text{CH}_3\text{COOH} + \text{H}_2\text{O}$."
                ),
            ),
            tf4(
                stem=(
                    r"Cho các phát biểu về cấu tạo và tính chất hóa học của $\text{glucose}$, $\text{fructose}$ và $\text{saccharose}$."
                ),
                statements=[
                    r"Trong dung dịch nước, $\text{glucose}$ tồn tại chủ yếu ở dạng mạch vòng $6$ cạnh ($\alpha\text{-glucose}$ và $\beta\text{-glucose}$) có nhóm $-\text{OH}$ hemiacetal tại nguyên tử $\text{C}_1$.",
                    r"Cả $\text{glucose}$ và $\text{fructose}$ đều làm mất màu dung dịch nước bromine ở điều kiện thường vì trong môi trường acid của nước bromine, $\text{fructose}$ chuyển hóa thành $\text{glucose}$.",
                    r"Thủy phân hoàn toàn $1\text{ mol}$ $\text{saccharose}$ trong môi trường acid, trung hòa acid rồi cho toàn bộ sản phẩm tác dụng với lượng dư thuốc thử Tollens đun nóng thì thu được tối đa $4\text{ mol}$ $\text{Ag}$.",
                    r"Phân tử $\text{saccharose}$ được tạo bởi $2$ đơn vị $\alpha\text{-glucose}$ liên kết với nhau qua liên kết $\alpha\text{-1,2-glycoside}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Trong dung dịch, $\text{glucose}$ tồn tại chủ yếu ở hai dạng vòng $6$ cạnh $\alpha$ và $\beta$ có nhóm $-\text{OH}$ hemiacetal ở $\text{C}_1$, nằm cân bằng với một lượng nhỏ dạng mạch hở." "\n"
                    r"- **b) Sai**: Sự chuyển hóa thuận nghịch giữa $\text{fructose}$ và $\text{glucose}$ chỉ xảy ra trong môi trường kiềm ($\text{OH}^-$), không xảy ra trong môi trường acid của nước $\text{Br}_2$; do đó $\text{fructose}$ không làm mất màu nước $\text{Br}_2$." "\n"
                    r"- **c) Đúng**: Thủy phân $1\text{ mol}$ $\text{saccharose}$ tạo ra $1\text{ mol}$ $\text{glucose}$ và $1\text{ mol}$ $\text{fructose}$; mỗi mol monosaccharide này tráng bạc cho $2\text{ mol}$ $\text{Ag}$, tổng cộng thu được $2 + 2 = 4\text{ mol}$ $\text{Ag}$." "\n"
                    r"- **d) Sai**: Phân tử $\text{saccharose}$ được cấu tạo từ $1$ gốc $\alpha\text{-glucose}$ và $1$ gốc $\beta\text{-fructose}$ liên kết qua nguyên tử oxygen giữa $\text{C}_1$ của $\text{glucose}$ và $\text{C}_2$ của $\text{fructose}$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét cấu trúc phân tử, tính chất và ứng dụng của hai polysaccharide thiên nhiên là tinh bột và $\text{cellulose}$."
                ),
                statements=[
                    r"Tinh bột là hỗn hợp của hai polysaccharide là $\text{amylose}$ (mạch không phân nhánh) và $\text{amylopectin}$ (mạch phân nhánh).",
                    r"Tinh bột và $\text{cellulose}$ có cùng công thức phân tử dạng $(\text{C}_6\text{H}_{10}\text{O}_5)_n$ nên chúng là hai đồng phân cấu tạo của nhau.",
                    r"$\text{Cellulose}$ không tan trong nước nhưng tan tốt trong nước Schweizer (dung dịch chứa phức chất $[\text{Cu(NH}_3)_4](\text{OH})_2$).",
                    r"Mỗi mắt xích $\text{C}_6\text{H}_{10}\text{O}_5$ trong phân tử $\text{cellulose}$ có $5$ nhóm $-\text{OH}$ tự do nên có thể tạo ra $\text{cellulose pentanitrate}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Tinh bột gồm $\text{amylose}$ (liên kết $\alpha\text{-1,4-glycoside}$, không phân nhánh) và $\text{amylopectin}$ (liên kết $\alpha\text{-1,4}$ và $\alpha\text{-1,6-glycoside}$, có phân nhánh)." "\n"
                    r"- **b) Sai**: Hệ số polymer hóa $n$ của tinh bột và $\text{cellulose}$ rất khác nhau nên phân tử khối của chúng không bằng nhau; do đó chúng không phải là đồng phân của nhau." "\n"
                    r"- **c) Đúng**: Tính chất đặc trưng của $\text{cellulose}$ là tan trong dung dịch nước Schweizer $[\text{Cu(NH}_3)_4](\text{OH})_2$." "\n"
                    r"- **d) Sai**: Mỗi mắt xích $\text{C}_6\text{H}_{10}\text{O}_5$ của $\text{cellulose}$ chỉ có $3$ nhóm $-\text{OH}$ tự do, viết là $[\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3]_n$, nên phản ứng tối đa với $\text{HNO}_3$ tạo $\text{cellulose trinitrate}$ $[\text{C}_6\text{H}_7\text{O}_2(\text{ONO}_2)_3]_n$."
                ),
            ),
            mcq(
                question=(
                    r"Đun nóng $34{,}2\text{ g}$ $\text{saccharose}$ với dung dịch $\text{H}_2\text{SO}_4$ loãng (hiệu suất phản ứng thủy phân đạt $75\%$). "
                    r"Trung hòa hết acid bằng kiềm rồi cho toàn bộ dung dịch thu được tác dụng với lượng dư thuốc thử Tollens đun nóng. "
                    r"Khối lượng bạc ($\text{Ag}$) kết tủa thu được là:"
                ),
                options=[
                    r"$32{,}4\text{ g}$.",
                    r"$43{,}2\text{ g}$.",
                    r"$16{,}2\text{ g}$.",
                    r"$21{,}6\text{ g}$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Số mol $\text{saccharose}$ ban đầu: $n_{\text{C}_{12}\text{H}_{22}\text{O}_{11}} = \dfrac{34{,}2}{342} = 0{,}10\text{ mol}$. "
                    r"Với hiệu suất thủy phân $H = 75\%$, số mol $\text{saccharose}$ bị thủy phân là $0{,}10 \cdot 0{,}75 = 0{,}075\text{ mol}$. "
                    r"Phần $\text{saccharose}$ dư không tráng bạc; phần bị thủy phân tạo $0{,}075\text{ mol}$ $\text{glucose}$ và $0{,}075\text{ mol}$ $\text{fructose}$. "
                    r"Tổng số mol $\text{Ag}$ tạo thành là $n_{\text{Ag}} = 4n_{\text{saccharose phản ứng}} = 4 \cdot 0{,}075 = 0{,}30\text{ mol}$. "
                    r"Khối lượng $\text{Ag}$ thu được là $m_{\text{Ag}} = 0{,}30 \cdot 108 = 32{,}4\text{ g}$."
                ),
            ),
            short(
                question=(
                    r"Để sản xuất $29{,}7\text{ kg}$ $\text{cellulose trinitrate}$ (hiệu suất phản ứng đạt $90\%$) từ $\text{cellulose}$ và dung dịch $\text{HNO}_3$ đặc "
                    r"(có $\text{H}_2\text{SO}_4$ đặc xúc tác), cần dùng bao nhiêu $\text{kg}$ $\text{cellulose}$ nguyên chất?"
                ),
                answer=["18", "18,0", "18.0"],
                level="vandung",
                solution=(
                    r"- Phương trình phản ứng tính theo $1$ mắt xích: $\text{C}_6\text{H}_7\text{O}_2(\text{OH})_3 + 3\text{HNO}_3 \xrightarrow{\text{H}_2\text{SO}_4\text{ đặc, } t^\circ} \text{C}_6\text{H}_7\text{O}_2(\text{ONO}_2)_3 + 3\text{H}_2\text{O}$." "\n"
                    r"- Khối lượng mol $1$ mắt xích $\text{cellulose}$ là $162\text{ g/mol}$; khối lượng mol $1$ mắt xích $\text{cellulose trinitrate}$ là $297\text{ g/mol}$." "\n"
                    r"- Số $\text{kmol}$ mắt xích $\text{cellulose trinitrate}$ là $n = \dfrac{29{,}7}{297} = 0{,}10\text{ kmol}$." "\n"
                    r"- Với hiệu suất $H = 90\%$, khối lượng $\text{cellulose}$ cần dùng là $m_{\text{cellulose}} = \dfrac{0{,}10 \cdot 162}{0{,}90} = 18\text{ kg}$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 3: HỢP CHẤT CHỨA NITROGEN (AMINE, AMINO ACID, PEPTIDE VÀ PROTEIN)
    # =========================================================================
    lesson(
        grade=12,
        order=3,
        code="H12-C03",
        title="Chương 3: Hợp chất chứa Nitrogen (Amine, Amino acid, Peptide và Protein)",
        topic="amin-amino-acid-protein",
        description=(
            "Chương 3 SGK Hóa học 12 Kết nối tri thức: Phân loại, danh pháp IUPAC và tính chất của amine; "
            "cấu tạo ion lưỡng cực, tính lưỡng tính, tính điện di của amino acid; liên kết peptide, phản ứng màu biuret của peptide và protein, vai trò của enzyme."
        ),
        summary=(
            r"**Amine** là dẫn xuất của ammonia ($\text{NH}_3$) khi thay thế một hay nhiều nguyên tử $\text{H}$ trong phân tử $\text{NH}_3$ bằng gốc hydrocarbon, "
            r"chia thành amine bậc một ($\text{RNH}_2$), bậc hai ($\text{R}_1\text{NHR}_2$) và bậc ba ($\text{R}_1\text{NR}_2\text{R}_3$). "
            r"Do nguyên tử $\text{N}$ còn cặp electron chưa liên kết nên các amine đều có **tính base**: các alkylamine mạch hở có tính base mạnh hơn $\text{NH}_3$ "
            r"(làm quỳ tím hóa xanh, phenolphthalein hóa hồng), còn **aniline** ($\text{C}_6\text{H}_5\text{NH}_2$) có tính base rất yếu (yếu hơn $\text{NH}_3$, "
            r"**không làm đổi màu quỳ tím**) nhưng dễ tham gia phản ứng thế vào nhân thơm với nước $\text{Br}_2$ tạo kết tủa trắng $2,4,6\text{-tribromoaniline}$. "
            r"**Amino acid** là hợp chất hữu cơ tạp chức chứa đồng thời nhóm amino ($-\text{NH}_2$) và nhóm carboxyl ($-\text{COOH}$); các amino acid thiên nhiên "
            r"cấu tạo nên protein đều là $\alpha\text{-amino acid}$, tồn tại chủ yếu ở dạng **ion lưỡng cực** $\text{H}_3\text{N}^+-\text{CH(R)}-\text{COO}^-$, "
            r"có **tính chất lưỡng tính**, tham gia phản ứng ester hóa, phản ứng trùng ngưng và có **tính điện di** (di chuyển về phía cực âm hoặc cực dương tùy theo $\text{pH}$ của môi trường). "
            r"**Peptide** gồm từ $2$ đến $50$ đơn vị $\alpha\text{-amino acid}$ liên kết với nhau qua **liên kết peptide** $-\text{CO}-\text{NH}-$; "
            r"các peptide có từ **$2$ liên kết peptide trở lên** ($\text{tripeptide}$ trở lên) và **protein** tác dụng với $\text{Cu(OH)}_2/\text{OH}^-$ cho **phản ứng màu biuret** (màu tím đặc trưng). "
            r"**Protein** là các polypeptide cao phân tử ($M$ từ vài chục nghìn đến hàng triệu $\text{amu}$), dễ bị **đông tụ** dưới tác dụng của nhiệt, acid, kiềm hoặc muối kim loại nặng; "
            r"**enzyme** có bản chất chủ yếu là protein, đóng vai trò chất xúc tác sinh học có tính chọn lọc cao."
        ),
        objectives=[
            r"Nêu được khái niệm, xác định được bậc của amine (bậc một, bậc hai, bậc ba) và gọi được tên các amine theo danh pháp gốc – chức và danh pháp thay thế IUPAC.",
            r"Trình bày được tính chất vật lý, tính base của amine (tác dụng với nước, dung dịch acid, dung dịch muối $\text{Fe}^{3+}, \text{Cu}^{2+}$), phản ứng với nitrous acid ($\text{HNO}_2$), phản ứng thế ở nhân thơm của $\text{aniline}$ với nước $\text{Br}_2$ và phương pháp điều chế amine.",
            r"Nêu được khái niệm, cấu tạo ion lưỡng cực, danh pháp IUPAC, tên bán hệ thống, tên thông thường và kí hiệu của $5$ $\alpha\text{-amino acid}$ trọng tâm ($\text{Gly}, \text{Ala}, \text{Val}, \text{Glu}, \text{Lys}$).",
            r"Giải thích được tính chất lưỡng tính, sự đổi màu quỳ tím, tính điện di của amino acid ở các giá trị $\text{pH}$ khác nhau, phản ứng ester hóa và phản ứng trùng ngưng của $\varepsilon\text{-}, \omega\text{-amino acid}$.",
            r"Trình bày được khái niệm liên kết peptide ($-\text{CO}-\text{NH}-$), cách biểu diễn và gọi tên peptide, phản ứng thủy phân và phản ứng màu biuret của peptide (từ $\text{tripeptide}$ trở lên).",
            r"Nêu được khái niệm, cấu trúc, tính chất của protein (sự đông tụ, thủy phân, phản ứng màu biuret, phản ứng với $\text{HNO}_3$ đặc) và vai trò của protein, enzyme trong cơ thể sinh vật và công nghiệp.",
        ],
        formulas=[
            {
                "name": "Tính base của amine mạch hở trong nước và phản ứng với dung dịch acid",
                "formula": r"$\text{RNH}_2 + \text{H}_2\text{O} \rightleftharpoons \text{RNH}_3^+ + \text{OH}^-$; $\text{RNH}_2 + \text{HCl} \rightarrow \text{RNH}_3\text{Cl}$",
                "note": r"So sánh lực base: $\text{C}_6\text{H}_5\text{NH}_2 < \text{NH}_3 < \text{CH}_3\text{NH}_2 < \text{C}_2\text{H}_5\text{NH}_2 < (\text{CH}_3)_2\text{NH}$.",
            },
            {
                "name": "Phản ứng của amine với dung dịch muối sắt(III) và phản ứng thế của aniline với nước bromine",
                "formula": r"$3\text{CH}_3\text{NH}_2 + \text{FeCl}_3 + 3\text{H}_2\text{O} \rightarrow \text{Fe(OH)}_3\downarrow\text{ (nâu đỏ)} + 3\text{CH}_3\text{NH}_3\text{Cl}$; $\text{C}_6\text{H}_5\text{NH}_2 + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{NH}_2\downarrow\text{ (trắng)} + 3\text{HBr}$",
                "note": r"Với $\text{CuSO}_4$, dung dịch $\text{CH}_3\text{NH}_2$ hoặc $\text{C}_2\text{H}_5\text{NH}_2$ dư tạo kết tủa xanh $\text{Cu(OH)}_2$ sau đó tan tạo phức xanh thẫm $[\text{Cu(RNH}_2)_4](\text{OH})_2$.",
            },
            {
                "name": "Phản ứng của amine bậc một với nitrous acid (HNO2)",
                "formula": r"$\text{RNH}_2 + \text{HNO}_2 \rightarrow \text{ROH} + \text{N}_2\uparrow + \text{H}_2\text{O}$; $\text{C}_6\text{H}_5\text{NH}_2 + \text{HNO}_2 + \text{HCl} \xrightarrow{0\text{–}5^\circ\text{C}} [\text{C}_6\text{H}_5\text{N}_2]^+\text{Cl}^- + 2\text{H}_2\text{O}$",
                "note": r"Alkylamine bậc một giải phóng khí $\text{N}_2$ ở nhiệt độ thường; $\text{aniline}$ tạo muối diazonium ở $0\text{–}5^\circ\text{C}$ dùng tổng hợp phẩm nhuộm azo.",
            },
            {
                "name": "Tính chất lưỡng tính và sự tồn tại của amino acid theo pH (tính điện di)",
                "formula": r"$\text{H}_3\text{N}^+-\text{CH(R)}-\text{COOH}\text{ (cation, pH thấp)} \stackrel{+\text{OH}^-}{\underset{+\text{H}^+}{\rightleftharpoons}} \text{H}_3\text{N}^+-\text{CH(R)}-\text{COO}^-\text{ (ion lưỡng cực, pH} = \text{pI)} \stackrel{+\text{OH}^-}{\underset{+\text{H}^+}{\rightleftharpoons}} \text{H}_2\text{N}-\text{CH(R)}-\text{COO}^-\text{ (anion, pH cao)}$",
                "note": r"Ở $\text{pH} < \text{pI}$, amino acid tích điện dương di chuyển về cực âm (cathode); ở $\text{pH} > \text{pI}$, amino acid tích điện âm di chuyển về cực dương (anode).",
            },
            {
                "name": "Số liên kết peptide và phương trình thủy phân hoàn toàn n-peptide mạch hở",
                "formula": r"$\text{Peptide gồm } k \text{ mắt xích } \alpha\text{-amino acid} \text{ có } (k - 1) \text{ liên kết peptide } -\text{CO}-\text{NH}-$",
                "note": r"Thủy phân hoàn toàn $1\text{ mol}$ $k\text{-peptide}$ trong môi trường trung tính cần $(k - 1)\text{ mol}$ $\text{H}_2\text{O}$; nếu thủy phân trong dung dịch $\text{NaOH}$ (các mắt xích có $1$ nhóm $-\text{COOH}$) cần $k\text{ mol}$ $\text{NaOH}$ và tạo $1\text{ mol}$ $\text{H}_2\text{O}$.",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 8. Amine",
                "content": [
                    r"**Phân loại và danh pháp IUPAC**: Bậc của amine được tính bằng **số gốc hydrocarbon liên kết trực tiếp với nguyên tử nitrogen**: amine bậc một ($\text{R}-\text{NH}_2$), amine bậc hai ($\text{R}_1-\text{NH}-\text{R}_2$), amine bậc ba ($\text{R}_1-\text{N(R}_2)-\text{R}_3$). Ở điều kiện thường, $4$ amine là **chất khí** có mùi khai tương tự $\text{NH}_3$ và tan nhiều trong nước gồm: $\text{CH}_3\text{NH}_2$ ($\text{methanamine}$ / $\text{methylamine}$), $\text{C}_2\text{H}_5\text{NH}_2$ ($\text{ethanamine}$ / $\text{ethylamine}$), $(\text{CH}_3)_2\text{NH}$ ($\text{N-methylmethanamine}$ / $\text{dimethylamine}$) và $(\text{CH}_3)_3\text{N}$ ($\text{N,N-dimethylmethanamine}$ / $\text{trimethylamine}$). **Aniline** ($\text{C}_6\text{H}_5\text{NH}_2$, tên IUPAC là $\text{benzenamine}$, tên gốc – chức là $\text{phenylamine}$) là chất lỏng không màu, rất độc, ít tan trong nước, dễ bị oxi hóa chuyển sang màu nâu đen khi để ngoài không khí.",
                    r"**Tính chất hóa học của amine**: (1) **Tính base**: Nhóm $-\text{NH}_2$ nhận proton $\text{H}^+$. Các alkylamine có gốc alkyl đẩy electron nên lực base mạnh hơn $\text{NH}_3$ (làm quỳ tím hóa xanh); ngược lại, trong phân tử $\text{aniline}$, vòng benzene hút electron làm giảm mật độ electron trên nguyên tử $\text{N}$ nên $\text{aniline}$ có tính base yếu hơn $\text{NH}_3$ và **không làm đổi màu quỳ tím** (nhưng vẫn tác dụng với $\text{HCl}$ tạo $\text{phenylammonium chloride}$ $\text{C}_6\text{H}_5\text{NH}_3\text{Cl}$ tan trong nước). (2) **Phản ứng với $\text{HNO}_2$**: Alkylamine bậc một tác dụng với $\text{HNO}_2$ ($\text{NaNO}_2 + \text{HCl}$) ở nhiệt độ thường tạo alcohol và sủi bọt khí $\text{N}_2$; $\text{aniline}$ tác dụng với $\text{HNO}_2/\text{HCl}$ ở $0\text{–}5^\circ\text{C}$ tạo muối diazonium $[\text{C}_6\text{H}_5\text{N}_2]^+\text{Cl}^-$. (3) **Phản ứng thế ở nhân thơm của aniline**: Nhóm $-\text{NH}_2$ hoạt hóa nhân benzene, làm $\text{aniline}$ phản ứng rất dễ với nước $\text{Br}_2$ tạo kết tủa trắng $2,4,6\text{-tribromoaniline}$ (dùng nhận biết $\text{aniline}$). (4) **Điều chế amine**: Alkyl hóa $\text{NH}_3$ bằng dẫn xuất halogen hoặc khử hợp chất nitro (như $\text{C}_6\text{H}_5\text{NO}_2 + 6[\text{H}] \xrightarrow{\text{Fe + HCl}, t^\circ} \text{C}_6\text{H}_5\text{NH}_2 + 2\text{H}_2\text{O}$).",
                ],
            },
            {
                "title": "Bài 9. Amino acid và peptide",
                "content": [
                    r"**Năm $\alpha\text{-amino acid}$ trọng tâm**: (1) **Glycine** ($\text{Gly}$, $\text{H}_2\text{N}-\text{CH}_2-\text{COOH}$, $M = 75\text{ g/mol}$, tên thay thế: $\text{aminoethanoic acid}$); (2) **Alanine** ($\text{Ala}$, $\text{CH}_3-\text{CH(NH}_2)-\text{COOH}$, $M = 89\text{ g/mol}$, $\text{2-aminopropanoic acid}$); (3) **Valine** ($\text{Val}$, $(\text{CH}_3)_2\text{CH}-\text{CH(NH}_2)-\text{COOH}$, $M = 117\text{ g/mol}$, $\text{2-amino-3-methylbutanoic acid}$); (4) **Glutamic acid** ($\text{Glu}$, $\text{HOOC}-\text{CH}_2-\text{CH}_2-\text{CH(NH}_2)-\text{COOH}$, $M = 147\text{ g/mol}$, có $1$ nhóm $-\text{NH}_2$ và $2$ nhóm $-\text{COOH}$, làm **quỳ tím hóa đỏ / hồng**, muối monosodium glutamate là **mì chính / bột ngọt**); (5) **Lysine** ($\text{Lys}$, $\text{H}_2\text{N}-[\text{CH}_2]_4-\text{CH(NH}_2)-\text{COOH}$, $M = 146\text{ g/mol}$, có $2$ nhóm $-\text{NH}_2$ và $1$ nhóm $-\text{COOH}$, làm **quỳ tím hóa xanh**). Các amino acid $\text{Gly}, \text{Ala}, \text{Val}$ có $1$ nhóm $-\text{NH}_2$ và $1$ nhóm $-\text{COOH}$ nên **không làm đổi màu quỳ tím**.",
                    r"**Cấu tạo ion lưỡng cực và tính chất vật lý, hóa học của amino acid**: Ở trạng thái tinh thể và trong dung dịch trung tính, amino acid tồn tại chủ yếu ở dạng **ion lưỡng cực** $\text{H}_3\text{N}^+-\text{CH(R)}-\text{COO}^-$, vì vậy các amino acid đều là **chất rắn kết tinh, không màu, vị hơi ngọt, có nhiệt độ nóng chảy cao và dễ tan trong nước**. Về mặt hóa học: (1) **Tính lưỡng tính**: Tác dụng với cả acid vô cơ mạnh ($\text{HCl}$) và base mạnh ($\text{NaOH}, \text{KOH}$). (2) **Tính điện di**: Ở $\text{pH} \approx 6$, $\text{Gly}, \text{Ala}$ tồn tại chủ yếu dạng ion lưỡng cực nên hầu như không dịch chuyển trong điện trường; $\text{Glu}$ tồn tại dạng anion ($\text{HOOC}-...-\text{COO}^-$) di chuyển về phía cực dương (anode); $\text{Lys}$ tồn tại dạng cation ($\text{H}_3\text{N}^+-...$) di chuyển về phía cực âm (cathode). (3) **Phản ứng ester hóa**: Với alcohol ($\text{C}_2\text{H}_5\text{OH}$) khi có khí $\text{HCl}$ khan. (4) **Phản ứng trùng ngưng**: Đun nóng $\varepsilon\text{-aminocaproic acid}$ tạo $\text{polycaproamide}$ (tơ capron / nylon-6) hoặc $\omega\text{-aminoenanthic acid}$ tạo $\text{polyenanthamide}$ (tơ nylon-7).",
                    r"**Peptide**: Là hợp chất chứa từ $2$ đến $50$ gốc $\alpha\text{-amino acid}$ liên kết với nhau bằng **liên kết peptide** ($-\text{CO}-\text{NH}-$). Phân tử peptide mạch hở được biểu diễn bắt đầu từ đầu $\text{N}$ (còn nhóm $-\text{NH}_2$) bên trái đến đầu $\text{C}$ (còn nhóm $-\text{COOH}$) bên phải, ví dụ $\text{Gly}-\text{Ala}-\text{Val}$. Peptide bị thủy phân hoàn toàn tạo các $\alpha\text{-amino acid}$ hoặc thủy phân không hoàn toàn tạo các peptide ngắn hơn. Các peptide có từ **$2$ liên kết peptide trở lên** ($\text{tripeptide}, \text{tetrapeptide}, ...$, trừ $\text{dipeptide}$) tác dụng với $\text{Cu(OH)}_2$ trong môi trường kiềm tạo phức chất có **màu tím đặc trưng (phản ứng màu biuret)**.",
                ],
            },
            {
                "title": "Bài 10. Protein và enzyme",
                "content": [
                    r"**Khái niệm và cấu trúc của protein**: Protein là những polypeptide cao phân tử có phân tử khối từ vài chục nghìn đến vài triệu $\text{amu}$, được chia thành **protein đơn giản** (khi thủy phân đến cùng chỉ tạo hỗn hợp các $\alpha\text{-amino acid}$, như $\text{albumin}$ lòng trắng trứng, $\text{fibroin}$ của tơ tằm, $\text{keratin}$ của tóc và móng) và **protein phức tạp** (gồm protein đơn giản liên kết với thành phần phi protein như nucleic acid, lipid, carbohydrate...). Cấu trúc phân tử protein có $4$ bậc: bậc $1$ (trình tự sắp xếp các $\alpha\text{-amino acid}$), bậc $2$ (xoắn $\alpha$ hoặc gấp nếp $\beta$), bậc $3$ và bậc $4$ (cấu trúc không gian đặc trưng quyết định hoạt tính sinh học).",
                    r"**Tính chất của protein và vai trò của enzyme**: Protein dạng hình sợi ($\text{keratin}, \text{collagen}, \text{fibroin}$) không tan trong nước, còn protein dạng hình cầu ($\text{albumin}, \text{hemoglobin}$) tan trong nước tạo dung dịch keo. Khi đun nóng hoặc cho thêm acid, base, muối kim loại nặng, protein bị **đông tụ** (biến tính do cấu trúc không gian bị phá vỡ, ví dụ luộc trứng hoặc nấu canh cua). Về mặt hóa học, protein bị **thủy phân** (nhờ acid, base hoặc enzyme) tạo các peptide rồi đến các $\alpha\text{-amino acid}$; cho **phản ứng màu biuret** (màu tím với $\text{Cu(OH)}_2/\text{OH}^-$) và tạo hợp chất màu vàng (hoặc kết tủa vàng) với dung dịch $\text{HNO}_3$ đặc. **Enzyme** hầu hết có bản chất là protein, đóng vai trò chất xúc tác sinh học giúp tăng tốc độ phản ứng sinh hóa lên hàng triệu lần ở điều kiện êm dịu (nhiệt độ cơ thể, $\text{pH}$ xác định) và có **tính chọn lọc rất cao** (mỗi enzyme chỉ xúc tác cho một hoặc một số ít phản ứng nhất định).",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: So sánh lực base và nhận biết các hợp chất chứa nitrogen",
                "problem": (
                    r"Sắp xếp các chất sau theo chiều tăng dần lực base: $\text{NH}_3$, $\text{C}_6\text{H}_5\text{NH}_2$, $\text{CH}_3\text{NH}_2$, $(\text{CH}_3)_2\text{NH}$. "
                    r"Nêu hiện tượng khi nhỏ nước $\text{Br}_2$ vào ống nghiệm chứa dung dịch $\text{C}_6\text{H}_5\text{NH}_2$."
                ),
                "solution": (
                    r"- Gốc phenyl ($-\text{C}_6\text{H}_5$) hút electron làm giảm lực base của $\text{aniline}$ yếu hơn $\text{NH}_3$; gốc methyl ($-\text{CH}_3$) đẩy electron làm tăng lực base của alkylamine mạnh hơn $\text{NH}_3$." "\n"
                    r"- Thứ tự tăng dần lực base: $\text{C}_6\text{H}_5\text{NH}_2 < \text{NH}_3 < \text{CH}_3\text{NH}_2 < (\text{CH}_3)_2\text{NH}$." "\n"
                    r"- Khi nhỏ nước $\text{Br}_2$ vào ống nghiệm chứa $\text{C}_6\text{H}_5\text{NH}_2$: Nước $\text{Br}_2$ mất màu và xuất hiện ngay kết tủa trắng $2,4,6\text{-tribromoaniline}$ ($\text{C}_6\text{H}_2\text{Br}_3\text{NH}_2\downarrow$)."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán thủy phân peptide trong dung dịch kiềm",
                "problem": (
                    r"Thủy phân hoàn toàn $0{,}1\text{ mol}$ tripeptide mạch hở $\text{Gly}-\text{Ala}-\text{Val}$ trong dung dịch chứa $0{,}4\text{ mol}$ $\text{NaOH}$ "
                    r"đun nóng, cô cạn dung dịch sau phản ứng thu được $m\text{ g}$ chất rắn khan. Tính giá trị của $m$."
                ),
                "solution": (
                    r"- Phương trình phản ứng: $\text{Gly}-\text{Ala}-\text{Val} + 3\text{NaOH} \xrightarrow{t^\circ} \text{GlyNa} + \text{AlaNa} + \text{ValNa} + \text{H}_2\text{O}$." "\n"
                    r"- Phân tử khối của tripeptide $\text{Gly}-\text{Ala}-\text{Val}$ là: $M = 75 + 89 + 117 - 2 \cdot 18 = 245\text{ g/mol}$." "\n"
                    r"- Với $0{,}1\text{ mol}$ $\text{Gly}-\text{Ala}-\text{Val}$ phản ứng với $0{,}3\text{ mol}$ $\text{NaOH}$ (trong tổng số $0{,}4\text{ mol}$ $\text{NaOH}$ ban đầu), số mol $\text{H}_2\text{O}$ sinh ra là $n_{\text{H}_2\text{O}} = 0{,}1\text{ mol}$." "\n"
                    r"- Bảo toàn khối lượng: $m_{\text{rắn}} = m_{\text{peptide}} + m_{\text{NaOH ban đầu}} - m_{\text{H}_2\text{O}} = 0{,}1 \cdot 245 + 0{,}4 \cdot 40 - 0{,}1 \cdot 18 = 24{,}5 + 16{,}0 - 1{,}8 = 38{,}7\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Bậc của amine bằng số gốc hydrocarbon liên kết trực tiếp với nguyên tử $\text{N}$; $\text{aniline}$ ($\text{C}_6\text{H}_5\text{NH}_2$) có lực base yếu hơn $\text{NH}_3$, không làm đổi màu quỳ tím và tạo kết tủa trắng với nước $\text{Br}_2$.",
            r"Amino acid tồn tại chủ yếu ở dạng ion lưỡng cực $\text{H}_3\text{N}^+-\text{CH(R)}-\text{COO}^-$, có nhiệt độ nóng chảy cao, dễ tan trong nước, có tính lưỡng tính và tính điện di phụ thuộc $\text{pH}$.",
            r"Dung dịch $\text{Gly}, \text{Ala}, \text{Val}$ không làm đổi màu quỳ tím; dung dịch $\text{Glu}$ làm quỳ tím hóa đỏ/hồng; dung dịch $\text{Lys}$ làm quỳ tím hóa xanh.",
            r"Phản ứng màu biuret (tác dụng với $\text{Cu(OH)}_2/\text{OH}^-$ cho màu tím) chỉ xảy ra với các peptide có từ $2$ liên kết peptide trở lên ($\text{tripeptide}$ trở lên) và protein; $\text{dipeptide}$ không có phản ứng màu biuret.",
        ],
        questions=[
            mcq(
                question=r"Amine nào sau đây là amine bậc hai?",
                options=[
                    r"$\text{CH}_3\text{CH}_2\text{NH}_2$.",
                    r"$\text{CH}_3\text{NHCH}_3$.",
                    r"$(\text{CH}_3)_3\text{N}$.",
                    r"$(\text{CH}_3)_2\text{CHNH}_2$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Bậc của amine bằng số nguyên tử $\text{H}$ trong phân tử $\text{NH}_3$ bị thay thế bởi gốc hydrocarbon. "
                    r"Trong $\text{CH}_3\text{NHCH}_3$ ($\text{dimethylamine}$ / $\text{N-methylmethanamine}$), nguyên tử $\text{N}$ liên kết trực tiếp với $2$ gốc $-\text{CH}_3$ nên là amine bậc hai."
                ),
            ),
            mcq(
                question=r"Dung dịch của chất nào sau đây làm quỳ tím chuyển sang màu xanh?",
                options=[
                    r"Aniline ($\text{C}_6\text{H}_5\text{NH}_2$).",
                    r"Glycine ($\text{H}_2\text{N}-\text{CH}_2-\text{COOH}$).",
                    r"Glutamic acid ($\text{HOOC}-[\text{CH}_2]_2-\text{CH(NH}_2)-\text{COOH}$).",
                    r"Lysine ($\text{H}_2\text{N}-[\text{CH}_2]_4-\text{CH(NH}_2)-\text{COOH}$).",
                ],
                answer="D",
                level="biet",
                solution=(
                    r"Phân tử $\text{lysine}$ có $2$ nhóm $-\text{NH}_2$ và chỉ có $1$ nhóm $-\text{COOH}$ nên dung dịch có môi trường kiềm, làm quỳ tím hóa xanh. "
                    r"$\text{Aniline}$ và $\text{glycine}$ không làm đổi màu quỳ tím; $\text{glutamic acid}$ làm quỳ tím hóa đỏ/hồng."
                ),
            ),
            mcq(
                question=r"Chất nào sau đây tác dụng với $\text{Cu(OH)}_2$ trong môi trường kiềm tạo dung dịch có màu tím đặc trưng (phản ứng màu biuret)?",
                options=[
                    r"$\text{Gly}-\text{Ala}$.",
                    r"$\text{Gly}-\text{Ala}-\text{Val}$.",
                    r"$\text{Alanine}$.",
                    r"$\text{Glucose}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Phản ứng màu biuret xảy ra với các peptide có từ $2$ liên kết peptide trở lên ($\text{tripeptide}$ trở lên) và protein. "
                    r"$\text{Gly}-\text{Ala}-\text{Val}$ là $\text{tripeptide}$ ($2$ liên kết peptide) nên có phản ứng màu biuret; $\text{Gly}-\text{Ala}$ là $\text{dipeptide}$ ($1$ liên kết peptide) nên không có phản ứng này."
                ),
            ),
            mcq(
                question=r"Hiện tượng rỉ dịch và đóng váng khi nấu canh cua hoặc khi luộc trứng chín là biểu hiện của quá trình nào đối với protein?",
                options=[
                    r"Sự thủy phân protein thành amino acid.",
                    r"Sự đông tụ protein bởi nhiệt độ.",
                    r"Phản ứng màu biuret của protein.",
                    r"Phản ứng ester hóa của protein.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Khi đun nóng, các protein tan trong nước thịt cua hoặc lòng trắng trứng ($\text{albumin}$) bị biến tính và đông tụ lại thành mảng rắn nổi lên trên."
                ),
            ),
            mcq(
                question=r"Số đồng phân cấu tạo là amine bậc một ứng với công thức phân tử $\text{C}_4\text{H}_{11}\text{N}$ là:",
                options=[
                    r"$2$.",
                    r"$3$.",
                    r"$4$.",
                    r"$8$.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"Amine bậc một có dạng $\text{C}_4\text{H}_9-\text{NH}_2$. Gốc butyl ($-\text{C}_4\text{H}_9$) có $4$ đồng phân cấu tạo "
                    r"($\text{butan-1-amine}$, $\text{butan-2-amine}$, $\text{2-methylpropan-1-amine}$, $\text{2-methylpropan-2-amine}$), "
                    r"nên có $4$ đồng phân amine bậc một (tổng số amine các bậc của $\text{C}_4\text{H}_{11}\text{N}$ là $8$)."
                ),
            ),
            mcq(
                question=r"Trong một tetrapeptide mạch hở có công thức $\text{Gly}-\text{Ala}-\text{Val}-\text{Glu}$, amino acid đầu $\text{N}$ và số liên kết peptide trong phân tử lần lượt là:",
                options=[
                    r"$\text{Gly}$ và $3$ liên kết peptide.",
                    r"$\text{Glu}$ và $3$ liên kết peptide.",
                    r"$\text{Gly}$ và $4$ liên kết peptide.",
                    r"$\text{Glu}$ và $4$ liên kết peptide.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Theo quy ước biểu diễn peptide từ đầu $\text{N}$ (bên trái) sang đầu $\text{C}$ (bên phải), trong $\text{Gly}-\text{Ala}-\text{Val}-\text{Glu}$, "
                    r"amino acid đầu $\text{N}$ (còn nhóm $-\text{NH}_2$ tự do) là $\text{Gly}$, đầu $\text{C}$ là $\text{Glu}$, và số liên kết peptide trong tetrapeptide ($4$ mắt xích) là $4 - 1 = 3$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét tính chất vật lý, tính chất hóa học và cách xử lý trong phòng thí nghiệm của các amine như $\text{methylamine}$, $\text{ethylamine}$ và $\text{aniline}$."
                ),
                statements=[
                    r"Ở điều kiện thường, $\text{methylamine}$ và $\text{ethylamine}$ là các chất khí có mùi khai, tan nhiều trong nước và làm dung dịch phenolphthalein chuyển sang màu hồng.",
                    r"Để rửa sạch ống nghiệm bị dính $\text{aniline}$ (rất ít tan trong nước), người ta tráng ống nghiệm bằng dung dịch $\text{NaOH}$ loãng rồi rửa lại bằng nước.",
                    r"Nhỏ vài giọt nước bromine vào ống nghiệm chứa dung dịch $\text{aniline}$ thì thấy xuất hiện kết tủa màu trắng của $2,4,6\text{-tribromoaniline}$.",
                    r"Khi cho $\text{ethylamine}$ ($\text{C}_2\text{H}_5\text{NH}_2$) tác dụng với dung dịch $\text{HNO}_2$ ở nhiệt độ thường sẽ thu được muối diazonium bền trong dung dịch.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: $\text{CH}_3\text{NH}_2$ và $\text{C}_2\text{H}_5\text{NH}_2$ là chất khí ở điều kiện thường, tan tốt trong nước tạo môi trường base làm hồng phenolphthalein." "\n"
                    r"- **b) Sai**: $\text{Aniline}$ có tính base yếu nên không phản ứng với $\text{NaOH}$. Để rửa sạch ống nghiệm dính $\text{aniline}$, phải tráng bằng dung dịch $\text{HCl}$ để chuyển thành muối $\text{C}_6\text{H}_5\text{NH}_3\text{Cl}$ dễ tan trong nước rồi rửa lại bằng nước." "\n"
                    r"- **c) Đúng**: $\text{C}_6\text{H}_5\text{NH}_2 + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{NH}_2\downarrow\text{ (trắng)} + 3\text{HBr}$." "\n"
                    r"- **d) Sai**: Alkylamine bậc một như $\text{C}_2\text{H}_5\text{NH}_2$ tác dụng với $\text{HNO}_2$ ở nhiệt độ thường tạo alcohol ($\text{C}_2\text{H}_5\text{OH}$) và giải phóng khí $\text{N}_2\uparrow$, không tạo muối diazonium bền như $\text{aniline}$ ở $0\text{–}5^\circ\text{C}$."
                ),
            ),
            tf4(
                stem=(
                    r"Đặt hỗn hợp ba amino acid gồm $\text{glutamic acid}$ ($\text{pI} \approx 3{,}2$), $\text{alanine}$ ($\text{pI} \approx 6{,}0$) và "
                    r"$\text{lysine}$ ($\text{pI} \approx 9{,}7$) ở chính giữa tờ giấy lọc tẩm dung dịch đệm có $\text{pH} = 6{,}0$, sau đó áp một hiệu điện thế "
                    r"một chiều vào hai đầu bản điện cực để thực hiện thí nghiệm điện di."
                ),
                statements=[
                    r"Ở $\text{pH} = 6{,}0$, $\text{alanine}$ tồn tại chủ yếu ở dạng ion lưỡng cực $\text{CH}_3-\text{CH(NH}_3^+)-\text{COO}^-$ có tổng điện tích bằng $0$ nên hầu như không dịch chuyển về các điện cực.",
                    r"Ở $\text{pH} = 6{,}0$, $\text{glutamic acid}$ tồn tại chủ yếu ở dạng cation mang điện tích dương nên di chuyển về phía cực âm (cathode).",
                    r"Ở $\text{pH} = 6{,}0$, $\text{lysine}$ tồn tại chủ yếu ở dạng cation mang điện tích dương nên di chuyển về phía cực âm (cathode).",
                    r"Nếu hạ $\text{pH}$ của dung dịch đệm xuống $\text{pH} = 1{,}0$ (môi trường rất acid), cả ba amino acid trên đều tồn tại chủ yếu ở dạng anion và di chuyển về phía cực dương (anode).",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Tại $\text{pH} = 6{,}0 = \text{pI}_{\text{Ala}}$, $\text{alanine}$ tồn tại chủ yếu ở dạng ion lưỡng cực trung hòa điện nên đứng yên tại vạch xuất phát." "\n"
                    r"- **b) Sai**: Vì $\text{pH} = 6{,}0 > \text{pI}_{\text{Glu}} = 3{,}2$, phân tử $\text{glutamic acid}$ có $2$ nhóm $-\text{COOH}$ bị phân li tạo dạng anion mang điện tích âm (${}^-\text{OOC}-[\text{CH}_2]_2-\text{CH(NH}_3^+)-\text{COO}^-$) nên di chuyển về phía **cực dương (anode)**." "\n"
                    r"- **c) Đúng**: Vì $\text{pH} = 6{,}0 < \text{pI}_{\text{Lys}} = 9{,}7$, phân tử $\text{lysine}$ có $2$ nhóm amino nhận proton tạo dạng cation mang điện tích dương nên di chuyển về phía **cực âm (cathode)**." "\n"
                    r"- **d) Sai**: Ở $\text{pH} = 1{,}0$ (môi trường rất acid, $\text{pH} < \text{pI}$ của cả $3$ chất), cả ba amino acid đều nhận $\text{H}^+$ tồn tại ở dạng **cation** mang điện tích dương và cùng di chuyển về phía cực âm (cathode)."
                ),
            ),
            mcq(
                question=(
                    r"Cho $13{,}35\text{ g}$ $\text{alanine}$ ($\text{H}_2\text{N}-\text{CH(CH}_3)-\text{COOH}$) tác dụng hết với $200\text{ mL}$ dung dịch $\text{HCl } 1{,}0\text{ M}$ "
                    r"thu được dung dịch $\text{X}$. Cho tiếp dung dịch chứa $0{,}40\text{ mol}$ $\text{NaOH}$ vào dung dịch $\text{X}$, sau khi các phản ứng xảy ra hoàn toàn, "
                    r"cô cạn dung dịch thu được bao nhiêu gam chất rắn khan?"
                ),
                options=[
                    r"$28{,}35\text{ g}$.",
                    r"$30{,}35\text{ g}$.",
                    r"$26{,}35\text{ g}$.",
                    r"$16{,}65\text{ g}$.",
                ],
                answer="B",
                level="vandung",
                solution=(
                    r"Ta có $n_{\text{Ala}} = \dfrac{13{,}35}{89} = 0{,}15\text{ mol}$; $n_{\text{HCl}} = 0{,}20 \cdot 1{,}0 = 0{,}20\text{ mol}$; $n_{\text{NaOH}} = 0{,}40\text{ mol}$. "
                    r"Xem như hỗn hợp gồm $0{,}15\text{ mol}$ $\text{Ala}$ và $0{,}20\text{ mol}$ $\text{HCl}$ tác dụng với $0{,}40\text{ mol}$ $\text{NaOH}$. "
                    r"Tổng số mol $\text{H}^+$ linh động từ $\text{Ala}$ và $\text{HCl}$ là $n_{\text{H}^+} = 0{,}15 + 0{,}20 = 0{,}35\text{ mol} < n_{\text{OH}^-} = 0{,}40\text{ mol}$, "
                    r"nên $\text{NaOH}$ còn dư và số mol $\text{H}_2\text{O}$ tạo thành là $n_{\text{H}_2\text{O}} = 0{,}35\text{ mol}$. "
                    r"Bảo toàn khối lượng: $m_{\text{rắn}} = m_{\text{Ala}} + m_{\text{HCl}} + m_{\text{NaOH}} - m_{\text{H}_2\text{O}} = 13{,}35 + 0{,}20 \cdot 36{,}5 + 0{,}40 \cdot 40 - 0{,}35 \cdot 18 = 30{,}35\text{ g}$."
                ),
            ),
            short(
                question=(
                    r"Thủy phân hoàn toàn $32{,}0\text{ g}$ dipeptide mạch hở $\text{Ala}-\text{Ala}$ bằng lượng vừa đủ dung dịch $\text{KOH}$ đun nóng. "
                    r"Cô cạn dung dịch sau phản ứng thu được bao nhiêu gam muối khan?"
                ),
                answer=["50,8", "50.8"],
                level="vandung",
                solution=(
                    r"- Phân tử khối của dipeptide $\text{Ala}-\text{Ala}$ là $M = 89 + 89 - 18 = 160\text{ g/mol} \Rightarrow n_{\text{Ala-Ala}} = \dfrac{32{,}0}{160} = 0{,}20\text{ mol}$." "\n"
                    r"- Phương trình phản ứng: $\text{Ala}-\text{Ala} + 2\text{KOH} \xrightarrow{t^\circ} 2\text{AlaK} + \text{H}_2\text{O}$." "\n"
                    r"- Ta có $n_{\text{KOH}} = 2n_{\text{Ala-Ala}} = 0{,}40\text{ mol}$ và $n_{\text{H}_2\text{O}} = n_{\text{Ala-Ala}} = 0{,}20\text{ mol}$." "\n"
                    r"- Bảo toàn khối lượng: $m_{\text{muối}} = m_{\text{Ala-Ala}} + m_{\text{KOH}} - m_{\text{H}_2\text{O}} = 32{,}0 + 0{,}40 \cdot 56 - 0{,}20 \cdot 18 = 50{,}8\text{ g}$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 4: POLYMER VÀ VẬT LIỆU POLYMER
    # =========================================================================
    lesson(
        grade=12,
        order=4,
        code="H12-C04",
        title="Chương 4: Polymer và Vật liệu Polymer",
        topic="polymer",
        description=(
            "Chương 4 SGK Hóa học 12 Kết nối tri thức: Danh pháp, cấu trúc mạch, tính chất vật lý – hóa học và phương pháp "
            "điều chế polymer (trùng hợp, trùng ngưng); các loại vật liệu polymer: chất dẻo, composite, tơ, cao su và keo dán."
        ),
        summary=(
            r"**Polymer** là những hợp chất có phân tử khối rất lớn do nhiều đơn vị nhỏ gọi là **mắt xích** liên kết với nhau tạo nên; "
            r"số mắt xích $n$ trong phân tử gọi là **hệ số polymer hóa**, các phân tử nhỏ tạo nên từng mắt xích gọi là **monomer**. "
            r"Mạch polymer có $3$ dạng cấu trúc: **mạch không phân nhánh** ($\text{PE}, \text{PVC}, \text{PS}, \text{amylose}, \text{cellulose}, \text{tơ nylon-6,6}$), "
            r"**mạch phân nhánh** ($\text{amylopectin}, \text{glycogen}$) và **mạch mạng không gian** ($\text{cao su lưu hóa}, \text{nhựa bakelite}$). "
            r"Hầu hết polymer là những chất rắn, không bay hơi, không có nhiệt độ nóng chảy xác định và không tan trong nước; những polymer nóng chảy khi đun nóng "
            r"thành chất lỏng nhớt và rắn lại khi để nguội gọi là **chất nhiệt dẻo** (có thể tái chế), còn những polymer bị phân hủy khi đun nóng gọi là **chất nhiệt rắn**. "
            r"Polymer tham gia $3$ loại phản ứng hóa học: **phản ứng giữ nguyên mạch**, **phản ứng phân cắt mạch** (như thủy phân $\text{tinh bột}, \text{cellulose}, \text{tơ nylon-6}, \text{tơ lapsan}$ "
            r"hoặc nhiệt phân $\text{PS}, \text{PMMA}$) và **phản ứng tăng mạch** (như lưu hóa cao su bằng sulfur). "
            r"Hai phương pháp điều chế polymer là **phản ứng trùng hợp** (monomer có liên kết bội $\text{C}=\text{C}$ hoặc vòng kém bền như $\text{caprolactam}$) "
            r"và **phản ứng trùng ngưng** (monomer có ít nhất $2$ nhóm chức có khả năng phản ứng kèm tách phân tử nhỏ như $\text{H}_2\text{O}$). "
            r"**Vật liệu polymer** bao gồm: **chất dẻo** ($\text{PE}, \text{PP}, \text{PVC}, \text{PS}, \text{PMMA}, \text{PPF}$), **vật liệu composite** (vật liệu nền + vật liệu cốt), "
            r"**tơ** (tơ tự nhiên, tơ bán tổng hợp như $\text{tơ visco}, \text{tơ cellulose acetate}$ và tơ tổng hợp như $\text{nylon-6}, \text{nylon-6,6}, \text{nitron/olon}, \text{lapsan}$), "
            r"**cao su** (cao su thiên nhiên $\text{cis-polyisoprene}$ và cao su tổng hợp $\text{buna}, \text{buna-S}, \text{buna-N}, \text{chloroprene}$) và **keo dán**."
        ),
        objectives=[
            r"Nêu được khái niệm polymer, mắt xích, hệ số polymer hóa, monomer và gọi được tên các polymer phổ biến theo danh pháp IUPAC (`poly` + tên monomer).",
            r"Phân biệt được $3$ dạng cấu trúc mạch polymer (không phân nhánh, phân nhánh, mạng không gian), tính chất nhiệt dẻo – nhiệt rắn và $3$ loại phản ứng hóa học của polymer (giữ nguyên mạch, phân cắt mạch, tăng mạch).",
            r"Phân biệt được điều kiện của monomer tham gia phản ứng trùng hợp và phản ứng trùng ngưng; viết được các phương trình hóa học tổng hợp polymer tiêu biểu.",
            r"Trình bày được thành phần, tính chất và ứng dụng của các loại vật liệu polymer: chất dẻo ($\text{PE}, \text{PP}, \text{PVC}, \text{PS}, \text{PMMA}, \text{PPF}$), vật liệu composite, tơ, cao su và keo dán.",
            r"Giải thích được vì sao không giặt quần áo làm từ tơ tằm, len, tơ nylon, tơ visco, tơ cellulose acetate trong nước quá nóng hoặc xà phòng có độ kiềm cao.",
        ],
        formulas=[
            {
                "name": "Phản ứng trùng hợp ethylene (tạo PE), vinyl chloride (tạo PVC) và methyl methacrylate (tạo PMMA)",
                "formula": r"$n\text{CH}_2=\text{CH}_2 \xrightarrow{t^\circ, p, xt} \text{-(CH}_2-\text{CH}_2\text{)-}_n$; $n\text{CH}_2=\text{CHCl} \xrightarrow{t^\circ, p, xt} \text{-(CH}_2-\text{CHCl)-}_n$; $n\text{CH}_2=\text{C(CH}_3)\text{COOCH}_3 \xrightarrow{t^\circ, p, xt} \text{-[-CH}_2-\text{C(CH}_3)(\text{COOCH}_3)\text{-]-}_n$",
                "note": r"$\text{PMMA}$ ($\text{poly(methyl methacrylate)}$) trong suốt, cho ánh sáng truyền qua trên $90\%$, dùng làm thủy tinh hữu cơ (plexiglas).",
            },
            {
                "name": "Phản ứng trùng hợp buta-1,3-diene tạo cao su buna và đồng trùng hợp tạo cao su buna-S, buna-N",
                "formula": r"$n\text{CH}_2=\text{CH}-\text{CH}=\text{CH}_2 \xrightarrow{\text{Na}, t^\circ, p} \text{-(CH}_2-\text{CH}=\text{CH}-\text{CH}_2\text{)-}_n$",
                "note": r"Đồng trùng hợp $\text{buta-1,3-diene}$ với $\text{styrene}$ ($\text{C}_6\text{H}_5\text{CH}=\text{CH}_2$) tạo $\text{cao su buna-S}$; với $\text{acrylonitrile}$ ($\text{CH}_2=\text{CH}-\text{CN}$) tạo $\text{cao su buna-N}$ (chống dầu tốt).",
            },
            {
                "name": "Phản ứng trùng hợp acrylonitrile điều chế tơ nitron (olon)",
                "formula": r"$n\text{CH}_2=\text{CH}-\text{CN} \xrightarrow{t^\circ, p, xt} \text{-[-CH}_2-\text{CH(CN)-]-}_n$",
                "note": r"Tơ nitron ($\text{olon}$) là tơ vinylic tổng hợp bằng phản ứng trùng hợp, bền với nhiệt và giữ nhiệt tốt, dùng dệt vải may quần áo ấm.",
            },
            {
                "name": "Phản ứng trùng ngưng điều chế tơ nylon-6,6 (poly(hexamethylene adipamide))",
                "formula": r"$n\text{H}_2\text{N}-[\text{CH}_2]_6-\text{NH}_2 + n\text{HOOC}-[\text{CH}_2]_4-\text{COOH} \xrightarrow{t^\circ} \text{-[-HN}-[\text{CH}_2]_6-\text{NH}-\text{CO}-[\text{CH}_2]_4-\text{CO-]-}_n + 2n\text{H}_2\text{O}$",
                "note": r"Monomer là $\text{hexamethylenediamine}$ và $\text{adipic acid}$. Khối lượng mol một mắt xích $\text{C}_{12}\text{H}_{22}\text{N}_2\text{O}_2$ là $226\text{ g/mol}$.",
            },
            {
                "name": "Phản ứng điều chế tơ nylon-6 (tơ capron) và tơ lapsan (poly(ethylene terephthalate) – PET)",
                "formula": r"$n\text{H}_2\text{N}-[\text{CH}_2]_5-\text{COOH} \xrightarrow{t^\circ} \text{-[-HN}-[\text{CH}_2]_5-\text{CO-]-}_n + n\text{H}_2\text{O}$; $n\text{HOOC}-\text{C}_6\text{H}_4-\text{COOH} + n\text{HO}-\text{CH}_2\text{CH}_2-\text{OH} \xrightarrow{t^\circ, xt} \text{-[-OC}-\text{C}_6\text{H}_4-\text{COO}-\text{CH}_2\text{CH}_2\text{-O-]-}_n + 2n\text{H}_2\text{O}$",
                "note": r"Tơ $\text{nylon-6}$ có thể điều chế bằng trùng ngưng $\varepsilon\text{-aminocaproic acid}$ hoặc trùng hợp mở vòng $\text{caprolactam}$ ($M_{\text{mắt xích}} = 113\text{ g/mol}$).",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 12. Đại cương về polymer",
                "content": [
                    r"**Khái niệm và danh pháp IUPAC**: Tên của polymer được gọi bằng cách ghép từ `poly` trước tên của monomer tạo nên nó; nếu tên monomer gồm hai từ trở lên hoặc có chữ số chỉ vị trí thì đặt trong dấu ngoặc đơn: $\text{polyethylene}$ ($\text{PE}$), $\text{polypropylene}$ ($\text{PP}$), $\text{polystyrene}$ ($\text{PS}$), $\text{poly(vinyl chloride)}$ ($\text{PVC}$), $\text{poly(methyl methacrylate)}$ ($\text{PMMA}$), $\text{poly(phenol formaldehyde)}$ ($\text{PPF}$), $\text{poly(ethylene terephthalate)}$ ($\text{PET}$).",
                    r"**Cấu trúc mạch và tính chất vật lý**: (1) **Mạch không phân nhánh**: $\text{PE}, \text{PP}, \text{PVC}, \text{PS}, \text{amylose}, \text{cellulose}, \text{cao su thiên nhiên}, \text{tơ nylon-6,6}$. (2) **Mạch phân nhánh**: $\text{amylopectin}, \text{glycogen}$. (3) **Mạch mạng không gian**: $\text{cao su lưu hóa}$ (các chuỗi polyisoprene nối với nhau bằng cầu nối disulfide $-\text{S}-\text{S}-$), $\text{nhựa bakelite}$ ($\text{nhựa resite}$). Đa số polymer có mạch không phân nhánh hoặc phân nhánh thuộc loại **chất nhiệt dẻo** (nóng chảy khi đun nóng, có thể tái chế), còn polymer có cấu trúc mạng không gian thuộc loại **chất nhiệt rắn** (không nóng chảy mà bị phân hủy ở nhiệt độ cao, không thể tái chế bằng cách nấu chảy).",
                    r"**Tính chất hóa học của polymer**: (1) **Phản ứng giữ nguyên mạch polymer**: Xảy ra ở các nhóm thế hoặc liên kết đôi trong mạch mà không làm thay đổi hệ số polymer hóa $n$ (ví dụ: thủy phân $\text{poly(vinyl acetate)}$ trong $\text{NaOH}$ tạo $\text{poly(vinyl alcohol)}$; cộng $\text{HCl}, \text{Br}_2$ vào cao su thiên nhiên; chlor hóa $\text{PVC}$ tạo tơ $\text{clorin}$). (2) **Phản ứng phân cắt mạch polymer**: Các polymer có nhóm chức $-\text{CO}-\text{NH}-$ (polyamide như $\text{nylon-6}, \text{nylon-6,6}, \text{protein}$), $-\text{COO}-$ (polyester như $\text{tơ lapsan}$) hoặc liên kết glycoside ($\text{tinh bột}, \text{cellulose}$) bị thủy phân trong môi trường acid hoặc kiềm; $\text{PS}$ và $\text{PMMA}$ bị nhiệt phân (depolymer hóa) tạo lại monomer ban đầu. (3) **Phản ứng tăng mạch polymer (khâu mạch)**: Khi đun nóng cao su thô với sulfur ($\text{S}$) ở $150^\circ\text{C}$ tạo cầu nối $-\text{S}-\text{S}-$ chuyển mạch thẳng thành mạng không gian (lưu hóa cao su), hoặc đun nóng nhựa $\text{resol}$ tạo nhựa $\text{resite}$ (bakelite).",
                    r"**Phương pháp điều chế polymer**: Gồm **phản ứng trùng hợp** (điều kiện: monomer phải có liên kết bội như $\text{CH}_2=\text{CH}_2, \text{CH}_2=\text{CHCl}, \text{CH}_2=\text{CH}-\text{CH}=\text{CH}_2, \text{CH}_2=\text{CH}-\text{CN}$ hoặc vòng kém bền như $\text{caprolactam}$, $\text{ethylene oxide}$) và **phản ứng trùng ngưng** (điều kiện: monomer phải có ít nhất $2$ nhóm chức có khả năng phản ứng tạo liên kết với nhau và giải phóng phân tử nhỏ như $\text{H}_2\text{O}$).",
                ],
            },
            {
                "title": "Bài 13. Vật liệu polymer",
                "content": [
                    r"**Chất dẻo và Vật liệu composite**: **Chất dẻo** là những vật liệu polymer có tính dẻo (bị biến dạng khi chịu tác dụng của nhiệt, áp suất và vẫn giữ được sự biến dạng đó khi thôi tác dụng), thành phần chính là polymer kết hợp chất hóa dẻo, chất độn, chất phụ gia. Các polymer làm chất dẻo thông dụng gồm $\text{PE}$ (màng bọc, túi nilon), $\text{PP}$ (hộp đựng thực phẩm, bao bì), $\text{PVC}$ (ống dẫn nước, vỏ dây điện), $\text{PS}$ (hộp xốp cách nhiệt), $\text{PMMA}$ (thủy tinh hữu cơ), $\text{PPF}$ (vỏ công tắc điện). **Vật liệu composite** là vật liệu tổ hợp từ ít nhất hai vật liệu khác nhau gồm **vật liệu nền** (nhựa polymer nhiệt dẻo hoặc nhiệt rắn) và **vật liệu cốt** (cốt sợi thủy tinh, sợi carbon hoặc cốt hạt như bột gỗ, bột đá), có độ bền cơ học, độ chịu nhiệt và chống ăn mòn vượt trội.",
                    r"**Tơ**: Là những vật liệu polymer hình sợi dài, mảnh, mềm mại và có độ bền nhất định. Phân loại thành $3$ nhóm: (1) **Tơ tự nhiên**: Bông ($\text{cellulose}$), len, tơ tằm ($\text{protein}$). (2) **Tơ bán tổng hợp (tơ nhân tạo)**: Đi từ polymer thiên nhiên ($\text{cellulose}$) chế biến thêm bằng phương pháp hóa học, gồm **tơ visco** và **tơ cellulose acetate**. (3) **Tơ tổng hợp**: Chế tạo từ các polymer tổng hợp, gồm **tơ polyamide** ($\text{nylon-6}$ / $\text{tơ capron}$, $\text{nylon-6,6}$, $\text{nylon-7}$ / $\text{tơ enang}$ – kém bền với nhiệt, acid và kiềm), **tơ polyester** ($\text{tơ lapsan}$ / $\text{PET}$ – kém bền với acid và kiềm nhưng bền cơ học) và **tơ vinylic** ($\text{tơ nitron}$ / $\text{olon}$ từ $\text{acrylonitrile}$ – bền với nhiệt, acid, kiềm loãng và giữ nhiệt tốt).",
                    r"**Cao su và Keo dán**: **Cao su** là vật liệu polymer có **tính đàn hồi**. **Cao su thiên nhiên** lấy từ mủ cây cao su có bản chất là polymer của $\text{isoprene}$ với cấu hình $\text{cis}$ ($\text{cis-1,4-polyisoprene}$, $(\text{C}_5\text{H}_8)_n$). **Cao su tổng hợp** gồm: $\text{cao su buna}$ (trùng hợp $\text{buta-1,3-diene}$), $\text{cao su buna-S}$ (đồng trùng hợp $\text{buta-1,3-diene}$ với $\text{styrene}$, độ đàn hồi cao dùng làm lốp xe), $\text{cao su buna-N}$ (đồng trùng hợp $\text{buta-1,3-diene}$ với $\text{acrylonitrile}$, tính chống dầu cao), $\text{cao su chloroprene}$ (trùng hợp $\text{chloroprene}$ $\text{CH}_2=\text{CCl}-\text{CH}=\text{CH}_2$, không cháy, bền cơ học) và $\text{cao su isoprene}$. **Keo dán** là vật liệu có khả năng kết dính hai mảnh vật liệu rắn với nhau bằng một màng mỏng bền chắc như **nhựa vá săm** (dung dịch cao su trong dung môi hữu cơ), **keo dán epoxy** (gồm hai thành phần là nhựa epoxy và chất đóng rắn amine) và **keo dán poly(urea-formaldehyde)** (điều chế từ $\text{urea}$ và $\text{formaldehyde}$).",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân loại phương pháp điều chế và bản chất của tơ",
                "problem": (
                    r"Cho các loại tơ sau: (1) tơ tằm, (2) tơ visco, (3) tơ nylon-6,6, (4) tơ nitron (olon), (5) tơ cellulose acetate, (6) bông, (7) tơ lapsan. "
                    r"Hãy phân loại các tơ trên vào nhóm tơ tự nhiên, tơ bán tổng hợp, tơ tổng hợp; đồng thời chỉ rõ tơ nào được điều chế bằng phản ứng trùng ngưng."
                ),
                "solution": (
                    r"- **Tơ tự nhiên**: (1) tơ tằm, (6) bông." "\n"
                    r"- **Tơ bán tổng hợp (nhân tạo)**: (2) tơ visco, (5) tơ cellulose acetate." "\n"
                    r"- **Tơ tổng hợp**: (3) tơ nylon-6,6, (4) tơ nitron (olon), (7) tơ lapsan." "\n"
                    r"- **Tơ điều chế bằng phản ứng trùng ngưng**: (3) tơ nylon-6,6 (trùng ngưng $\text{hexamethylenediamine}$ và $\text{adipic acid}$) và (7) tơ lapsan (trùng ngưng $\text{terephthalic acid}$ và $\text{ethylene glycol}$). Riêng (4) tơ nitron được điều chế bằng phản ứng trùng hợp $\text{acrylonitrile}$ ($\text{CH}_2=\text{CH}-\text{CN}$)."
                ),
            },
            {
                "title": "Ví dụ 2: Tính hệ số polymer hóa n",
                "problem": (
                    r"Một mẫu $\text{poly(vinyl chloride)}$ ($\text{PVC}$) có phân tử khối trung bình là $75000\text{ amu}$. "
                    r"Tính hệ số polymer hóa trung bình $n$ của mẫu $\text{PVC}$ đó."
                ),
                "solution": (
                    r"- Công thức một mắt xích của $\text{PVC}$ là $-\text{CH}_2-\text{CHCl}-$ ($\text{C}_2\text{H}_3\text{Cl}$), có khối lượng mol mắt xích là $M_{\text{mắt xích}} = 12 \cdot 2 + 3 + 35{,}5 = 62{,}5\text{ g/mol}$." "\n"
                    r"- Hệ số polymer hóa trung bình của mẫu $\text{PVC}$ là: $n = \dfrac{75000}{62{,}5} = 1200$."
                ),
            },
        ],
        key_takeaways=[
            r"Mạch mạng không gian gồm $\text{cao su lưu hóa}$ và $\text{nhựa bakelite}$; mạch phân nhánh gồm $\text{amylopectin}$ và $\text{glycogen}$; hầu hết các polymer còn lại có mạch không phân nhánh.",
            r"Tơ bán tổng hợp (nhân tạo) gồm $\text{tơ visco}$ và $\text{tơ cellulose acetate}$; $\text{tơ nitron}$ ($\text{olon}$) điều chế bằng phản ứng trùng hợp $\text{CH}_2=\text{CH}-\text{CN}$, còn $\text{tơ nylon-6,6}$ và $\text{tơ lapsan}$ điều chế bằng phản ứng trùng ngưng.",
            r"Cao su thiên nhiên có cấu hình $\text{cis-polyisoprene}$ $(\text{C}_5\text{H}_8)_n$; lưu hóa cao su bằng sulfur là phản ứng tăng mạch (khâu mạch).",
            r"Các polymer chứa liên kết $-\text{CO}-\text{NH}-$ (tơ tằm, len, tơ nylon) và $-\text{COO}-$ (tơ lapsan, tơ cellulose acetate) kém bền trong môi trường acid hoặc kiềm mạnh.",
        ],
        questions=[
            mcq(
                question=r"Polymer nào sau đây có cấu trúc mạch mạng không gian?",
                options=[
                    r"Polyethylene ($\text{PE}$).",
                    r"Poly(vinyl chloride) ($\text{PVC}$).",
                    r"Amylopectin.",
                    r"Cao su lưu hóa.",
                ],
                answer="D",
                level="biet",
                solution=(
                    r"$\text{Cao su lưu hóa}$ và $\text{nhựa bakelite}$ ($\text{nhựa resite}$) có cấu trúc mạch mạng không gian. "
                    r"$\text{PE}$ và $\text{PVC}$ có mạch không phân nhánh; $\text{amylopectin}$ có mạch phân nhánh."
                ),
            ),
            mcq(
                question=r"Loại tơ nào sau đây thuộc loại tơ bán tổng hợp (tơ nhân tạo)?",
                options=[
                    r"Tơ visco.",
                    r"Tơ tằm.",
                    r"Tơ nylon-6,6.",
                    r"Tơ nitron (olon).",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"$\text{Tơ visco}$ và $\text{tơ cellulose acetate}$ được sản xuất từ polymer thiên nhiên ($\text{cellulose}$) qua chế biến hóa học nên thuộc loại tơ bán tổng hợp (nhân tạo). "
                    r"$\text{Tơ tằm}$ là tơ tự nhiên; $\text{tơ nylon-6,6}$ và $\text{tơ nitron}$ là tơ tổng hợp."
                ),
            ),
            mcq(
                question=r"Monomer được dùng để trùng hợp trực tiếp tạo ra thủy tinh hữu cơ plexiglas là:",
                options=[
                    r"$\text{CH}_2=\text{CHCl}$.",
                    r"$\text{CH}_2=\text{C(CH}_3)\text{COOCH}_3$.",
                    r"$\text{C}_6\text{H}_5\text{CH}=\text{CH}_2$.",
                    r"$\text{CH}_2=\text{CH}-\text{CN}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Thủy tinh hữu cơ plexiglas là $\text{poly(methyl methacrylate)}$ ($\text{PMMA}$), được điều chế bằng phản ứng trùng hợp "
                    r"$\text{methyl methacrylate}$ có công thức cấu tạo $\text{CH}_2=\text{C(CH}_3)\text{COOCH}_3$."
                ),
            ),
            mcq(
                question=r"Cao su buna-S được điều chế bằng phản ứng đồng trùng hợp giữa $\text{buta-1,3-diene}$ ($\text{CH}_2=\text{CH}-\text{CH}=\text{CH}_2$) với chất nào sau đây?",
                options=[
                    r"Sulfur ($\text{S}$).",
                    r"Acrylonitrile ($\text{CH}_2=\text{CH}-\text{CN}$).",
                    r"Styrene ($\text{C}_6\text{H}_5\text{CH}=\text{CH}_2$).",
                    r"Isoprene ($\text{CH}_2=\text{C(CH}_3)-\text{CH}=\text{CH}_2$).",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Đồng trùng hợp $\text{buta-1,3-diene}$ với $\text{styrene}$ ($\text{C}_6\text{H}_5\text{CH}=\text{CH}_2$) có mặt $\text{Na}$ làm xúc tác thu được $\text{cao su buna-S}$."
                ),
            ),
            mcq(
                question=r"Cho các polymer sau: (1) $\text{polyethylene}$, (2) $\text{poly(hexamethylene adipamide)}$ ($\text{nylon-6,6}$), (3) $\text{polyacrylonitrile}$ ($\text{tơ nitron}$), (4) $\text{poly(ethylene terephthalate)}$ ($\text{tơ lapsan}$). Các polymer được điều chế bằng phản ứng trùng ngưng là:",
                options=[
                    r"(1) và (3).",
                    r"(2) và (4).",
                    r"(2), (3) và (4).",
                    r"(1), (2) và (4).",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Chất (2) $\text{nylon-6,6}$ điều chế bằng phản ứng trùng ngưng $\text{hexamethylenediamine}$ và $\text{adipic acid}$; "
                    r"chất (4) $\text{tơ lapsan}$ điều chế bằng phản ứng trùng ngưng $\text{terephthalic acid}$ và $\text{ethylene glycol}$. "
                    r"Chất (1) $\text{PE}$ và chất (3) $\text{tơ nitron}$ điều chế bằng phản ứng trùng hợp."
                ),
            ),
            mcq(
                question=r"Quá trình lưu hóa cao su (đun nóng cao su thiên nhiên với sulfur ở khoảng $150^\circ\text{C}$) thuộc loại phản ứng nào của polymer?",
                options=[
                    r"Phản ứng phân cắt mạch polymer.",
                    r"Phản ứng giữ nguyên mạch polymer.",
                    r"Phản ứng tăng mạch polymer (khâu mạch).",
                    r"Phản ứng trùng ngưng.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"Khi lưu hóa cao su, các nguyên tử sulfur tạo cầu nối disulfide ($-\text{S}-\text{S}-$) liên kết các chuỗi polyisoprene mạch thẳng thành mạng không gian ba chiều, nên thuộc loại **phản ứng tăng mạch polymer (khâu mạch)**."
                ),
            ),
            tf4(
                stem=(
                    r"Xét cấu trúc, tính chất và phương pháp điều chế các polymer thông dụng trong công nghiệp và đời sống."
                ),
                statements=[
                    r"Các polymer nhiệt dẻo như $\text{PE}, \text{PP}, \text{PVC}, \text{PS}$ khi đun nóng sẽ nóng chảy thành chất lỏng nhớt, để nguội lại hóa rắn nên có thể tái chế được.",
                    r"Tơ $\text{nitron}$ ($\text{olon}$) có công thức $\text{-[-CH}_2-\text{CH(CN)-]-}_n$ được điều chế bằng phản ứng trùng ngưng $\text{acrylonitrile}$ nên rất kém bền trong môi trường kiềm.",
                    r"Cao su thiên nhiên là polymer của $\text{isoprene}$ có cấu hình hình học dạng $\text{cis}$, trong mỗi mắt xích $-\text{CH}_2-\text{C(CH}_3)=\text{CH}-\text{CH}_2-$ vẫn còn $1$ liên kết đôi $\text{C}=\text{C}$.",
                    r"Quần áo may bằng vải tơ tằm, len hoặc tơ $\text{nylon-6,6}$ rất bền trong môi trường kiềm nên có thể ngâm giặt thoải mái trong nước xà phòng có độ kiềm cao và đun sôi.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: $\text{PE}, \text{PP}, \text{PVC}, \text{PS}$ là các chất nhiệt dẻo có thể nấu chảy để tái chế." "\n"
                    r"- **b) Sai**: Tơ $\text{nitron}$ ($\text{olon}$) được điều chế bằng **phản ứng trùng hợp** $\text{acrylonitrile}$ ($\text{CH}_2=\text{CH}-\text{CN}$), mạch chính chỉ gồm liên kết $\text{C}-\text{C}$ bền vững với nhiệt, acid và kiềm loãng." "\n"
                    r"- **c) Đúng**: Cao su thiên nhiên là $\text{cis-1,4-polyisoprene}$ $(\text{C}_5\text{H}_8)_n$, mỗi mắt xích còn $1$ liên kết đôi $\text{C}=\text{C}$ nên có thể tham gia phản ứng cộng ($\text{H}_2, \text{Br}_2, \text{HCl}$) và phản ứng lưu hóa." "\n"
                    r"- **d) Sai**: Tơ tằm, len (bản chất protein) và tơ $\text{nylon-6,6}$ (bản chất polyamide) đều chứa nhiều nhóm $-\text{CO}-\text{NH}-$ dễ bị thủy phân cắt mạch trong môi trường kiềm hoặc nước quá nóng."
                ),
            ),
            tf4(
                stem=(
                    r"Cho các nhận định về vật liệu composite, chất dẻo, keo dán và cách xử lý rác thải nhựa bảo vệ môi trường."
                ),
                statements=[
                    r"Vật liệu composite thường gồm hai thành phần chính là vật liệu nền (polymer) và vật liệu cốt (cốt sợi như sợi thủy tinh, sợi carbon hoặc cốt hạt).",
                    r"Thủy tinh hữu cơ ($\text{PMMA}$) và nhựa $\text{PVC}$ chỉ chứa hai nguyên tố hóa học là carbon và hydrogen trong phân tử.",
                    r"Nhựa $\text{poly(ethylene terephthalate)}$ ($\text{PET}$) thuộc loại polyester, được điều chế từ $\text{terephthalic acid}$ và $\text{ethylene glycol}$, dùng phổ biến để sản xuất chai đựng nước uống và tơ $\text{lapsan}$.",
                    r"Nhựa $\text{bakelite}$ ($\text{poly(phenol formaldehyde)}$ dạng mạng không gian) là chất nhiệt dẻo nên khi hỏng có thể đun nóng chảy để đúc lại thành vật dụng mới.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Vật liệu composite gồm vật liệu nền (đảm bảo sự liên kết) và vật liệu cốt (đảm bảo độ bền cơ học)." "\n"
                    r"- **b) Sai**: $\text{PMMA}$ có công thức $(\text{C}_5\text{H}_8\text{O}_2)_n$ chứa thêm nguyên tố $\text{O}$, còn $\text{PVC}$ có công thức $(\text{C}_2\text{H}_3\text{Cl})_n$ chứa thêm nguyên tố $\text{Cl}$." "\n"
                    r"- **c) Đúng**: $\text{PET}$ là polyester thu được từ phản ứng trùng ngưng $\text{HOOC}-\text{C}_6\text{H}_4-\text{COOH}$ và $\text{HOCH}_2\text{CH}_2\text{OH}$." "\n"
                    r"- **d) Sai**: Nhựa $\text{bakelite}$ có cấu trúc mạng không gian thuộc loại **chất nhiệt rắn**, khi đun nóng ở nhiệt độ cao sẽ bị phân hủy chứ không nóng chảy nên không thể tái chế bằng cách nấu chảy."
                ),
            ),
            mcq(
                question=(
                    r"Một đoạn mạch tơ $\text{nylon-6,6}$ có phân tử khối là $56500\text{ amu}$ và một đoạn mạch tơ $\text{capron}$ ($\text{nylon-6}$) "
                    r"có phân tử khối là $33900\text{ amu}$. Số mắt xích trong đoạn mạch tơ $\text{nylon-6,6}$ và đoạn mạch tơ $\text{capron}$ lần lượt là:"
                ),
                options=[
                    r"$250$ và $300$.",
                    r"$300$ và $250$.",
                    r"$250$ và $250$.",
                    r"$500$ và $300$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Một mắt xích của tơ $\text{nylon-6,6}$ là $-\text{HN}-[\text{CH}_2]_6-\text{NH}-\text{CO}-[\text{CH}_2]_4-\text{CO}-$ ($\text{C}_{12}\text{H}_{22}\text{N}_2\text{O}_2$) có $M = 226\text{ g/mol} \Rightarrow n_{\text{nylon-6,6}} = \dfrac{56500}{226} = 250$ mắt xích. "
                    r"Một mắt xích của tơ $\text{capron}$ ($\text{nylon-6}$) là $-\text{HN}-[\text{CH}_2]_5-\text{CO}-$ ($\text{C}_6\text{H}_{11}\text{NO}$) có $M = 113\text{ g/mol} \Rightarrow n_{\text{capron}} = \dfrac{33900}{113} = 300$ mắt xích."
                ),
            ),
            short(
                question=(
                    r"Cao su buna-S thu được từ phản ứng đồng trùng hợp giữa $\text{buta-1,3-diene}$ ($\text{C}_4\text{H}_6$) và $\text{styrene}$ ($\text{C}_8\text{H}_8$). "
                    r"Biết cứ $21{,}2\text{ g}$ một mẫu cao su buna-S này thì phản ứng cộng tối đa với $32{,}0\text{ g}$ $\text{Br}_2$ trong dung dịch. "
                    r"Trong phân tử cao su buna-S trên, tỉ lệ số mắt xích $\text{buta-1,3-diene}$ chia cho số mắt xích $\text{styrene}$ bằng bao nhiêu?"
                ),
                answer=["2", "2,0", "2.0"],
                level="vandung",
                solution=(
                    r"- Gọi số mol mắt xích $\text{buta-1,3-diene}$ ($\text{C}_4\text{H}_6$, $M = 54\text{ g/mol}$, còn $1$ liên kết đôi $\text{C}=\text{C}$ cộng được $1\text{ Br}_2$) và mắt xích $\text{styrene}$ ($\text{C}_8\text{H}_8$, $M = 104\text{ g/mol}$, vòng benzene không cộng dung dịch $\text{Br}_2$) trong $21{,}2\text{ g}$ cao su lần lượt là $x$ và $y$." "\n"
                    r"- Số mol $\text{Br}_2$ phản ứng: $n_{\text{Br}_2} = \dfrac{32{,}0}{160} = 0{,}20\text{ mol} \Rightarrow x = n_{\text{C}_4\text{H}_6} = 0{,}20\text{ mol}$." "\n"
                    r"- Khối lượng mắt xích $\text{C}_4\text{H}_6$ là $0{,}20 \cdot 54 = 10{,}8\text{ g} \Rightarrow m_{\text{C}_8\text{H}_8} = 21{,}2 - 10{,}8 = 10{,}4\text{ g} \Rightarrow y = \dfrac{10{,}4}{104} = 0{,}10\text{ mol}$." "\n"
                    r"- Vậy tỉ lệ số mắt xích $\text{buta-1,3-diene}$ chia cho số mắt xích $\text{styrene}$ là $\dfrac{x}{y} = \dfrac{0{,}20}{0{,}10} = 2$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 5: PIN ĐIỆN VÀ ĐIỆN PHÂN
    # =========================================================================
    lesson(
        grade=12,
        order=5,
        code="H12-C05",
        title="Chương 5: Pin điện và Điện phân",
        topic="dien-hoa",
        description=(
            "Chương 5 SGK Hóa học 12 Kết nối tri thức: Cặp oxi hóa – khử, thế điện cực chuẩn, dãy điện hóa và quy tắc alpha; "
            "cấu tạo, nguyên tắc hoạt động và sức điện động chuẩn của pin Galvani; nguyên tắc điện phân và định luật Faraday."
        ),
        summary=(
            r"Dạng oxi hóa ($\text{M}^{n+}$) và dạng khử ($\text{M}$) của cùng một nguyên tố kim loại tạo nên **cặp oxi hóa – khử** kí hiệu là $\text{M}^{n+}/\text{M}$. "
            r"Đại lượng đánh giá khả năng khử của dạng khử và khả năng oxi hóa của dạng oxi hóa ở điều kiện chuẩn ($C = 1\text{ M}, P = 1\text{ bar}, T = 298\text{ K}$ hay $25^\circ\text{C}$) "
            r"là **thế điện cực chuẩn** $E^\circ_{\text{M}^{n+}/\text{M}}$ (đơn vị $\text{V}$, quy ước $E^\circ_{2\text{H}^+/\text{H}_2} = 0{,}00\text{ V}$): "
            r"**giá trị $E^\circ_{\text{M}^{n+}/\text{M}}$ càng nhỏ thì dạng khử $\text{M}$ có tính khử càng mạnh và dạng oxi hóa $\text{M}^{n+}$ có tính oxi hóa càng yếu**. "
            r"Chiều của phản ứng oxi hóa – khử tự diễn biến giữa hai cặp $\text{X}^{x+}/\text{X}$ và $\text{Y}^{y+}/\text{Y}$ ($E^\circ_{\text{X}^{x+}/\text{X}} < E^\circ_{\text{Y}^{y+}/\text{Y}}$) "
            r"tuân theo **quy tắc alpha ($\alpha$)**: chất oxi hóa mạnh hơn ($\text{Y}^{y+}$) tác dụng với chất khử mạnh hơn ($\text{X}$) tạo chất oxi hóa yếu hơn ($\text{X}^{x+}$) và chất khử yếu hơn ($\text{Y}$). "
            r"Trong **pin điện hóa Galvani**, kim loại mạnh hơn (có $E^\circ$ nhỏ hơn) đóng vai trò **anode (cực âm)** xảy ra quá trình oxi hóa, kim loại yếu hơn (có $E^\circ$ lớn hơn) "
            r"đóng vai trò **cathode (cực dương)** xảy ra quá trình khử; **sức điện động chuẩn của pin** là $E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} > 0$. "
            r"Ngược lại, **điện phân** là quá trình oxi hóa – khử xảy ra trên bề mặt các điện cực dưới tác dụng của dòng điện một chiều đi qua chất điện li nóng chảy hoặc dung dịch chất điện li: "
            r"tại **cathode (cực âm)** xảy ra **quá trình khử** các cation (hoặc $\text{H}_2\text{O}$), tại **anode (cực dương)** xảy ra **quá trình oxi hóa** các anion (hoặc $\text{H}_2\text{O}$ hay kim loại làm anode tan); "
            r"khối lượng chất giải phóng ở điện cực tính theo **định luật Faraday**: $m = \dfrac{A \cdot I \cdot t}{n \cdot F}$ hay $n_{\text{e}} = \dfrac{I \cdot t}{F}$ với $F = 96500\text{ C/mol}$."
        ),
        objectives=[
            r"Biểu diễn được cặp oxi hóa – khử của kim loại $\text{M}^{n+}/\text{M}$ và nêu được giá trị thế điện cực chuẩn $E^\circ_{\text{M}^{n+}/\text{M}}$ là đại lượng đánh giá khả năng khử của dạng khử và khả năng oxi hóa của dạng oxi hóa ở điều kiện chuẩn.",
            r"Sử dụng bảng thế điện cực chuẩn và dãy điện hóa để so sánh tính khử của kim loại, tính oxi hóa của ion kim loại và vận dụng quy tắc alpha ($\alpha$) dự đoán chiều phản ứng oxi hóa – khử.",
            r"Mô tả được cấu tạo, vai trò của cầu muối, các bán phản ứng tại anode, cathode và tính được sức điện động chuẩn $E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$ của pin Galvani; so sánh ưu, nhược điểm của pin nhiên liệu, acquy, pin mặt trời.",
            r"Trình bày được nguyên tắc và thứ tự điện phân nóng chảy, điện phân dung dịch tại cathode và anode.",
            r"Trình bày được ứng dụng của điện phân trong sản xuất kim loại ($\text{Al}, \text{Na}, \text{Mg}, \text{Cu}$), điều chế hóa chất ($\text{NaOH}, \text{Cl}_2$, nước Javel), tinh luyện kim loại và mạ điện.",
            r"Vận dụng được công thức định luật Faraday $n_{\text{e}} = \dfrac{I \cdot t}{F}$ và $m = \dfrac{A \cdot I \cdot t}{n \cdot F}$ để giải các bài toán điện phân thực tiễn.",
        ],
        formulas=[
            {
                "name": "Cặp oxi hóa – khử và cân bằng bán phản ứng",
                "formula": r"$\text{M}^{n+}\text{ (dạng oxi hóa)} + n\text{e} \rightleftharpoons \text{M}\text{ (dạng khử)}$ (kí hiệu: $\text{M}^{n+}/\text{M}$)",
                "note": r"Ví dụ: $\text{Ag}^+/\text{Ag}$, $\text{Cu}^{2+}/\text{Cu}$, $\text{Fe}^{2+}/\text{Fe}$, $\text{Fe}^{3+}/\text{Fe}^{2+}$, $2\text{H}^+/\text{H}_2$.",
            },
            {
                "name": "Sức điện động chuẩn của pin điện hóa Galvani",
                "formula": r"$E^\circ_{\text{pin}} = E^\circ_{\text{cathode (+)}} - E^\circ_{\text{anode (-)}} > 0$",
                "note": r"Anode (cực âm) là cặp có $E^\circ$ nhỏ hơn (xảy ra sự oxi hóa); Cathode (cực dương) là cặp có $E^\circ$ lớn hơn (xảy ra sự khử).",
            },
            {
                "name": "Phản ứng tổng quát trong pin Galvani Zn–Cu",
                "formula": r"$\text{Anode (-): }\text{Zn}(s) \rightarrow \text{Zn}^{2+}(aq) + 2\text{e}$; $\text{Cathode (+): }\text{Cu}^{2+}(aq) + 2\text{e} \rightarrow \text{Cu}(s)$; $\text{Tổng quát: }\text{Zn}(s) + \text{Cu}^{2+}(aq) \rightarrow \text{Zn}^{2+}(aq) + \text{Cu}(s)$",
                "note": r"Với $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0{,}762\text{ V}$ và $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0{,}340\text{ V}$, ta có $E^\circ_{\text{pin Zn–Cu}} = 0{,}340 - (-0{,}762) = 1{,}102\text{ V}$.",
            },
            {
                "name": "Quá trình khử nước tại cathode và oxi hóa nước tại anode khi điện phân dung dịch",
                "formula": r"$\text{Tại cathode (-): }2\text{H}_2\text{O} + 2\text{e} \rightarrow \text{H}_2\uparrow + 2\text{OH}^-$; $\text{Tại anode (+): }2\text{H}_2\text{O} \rightarrow \text{O}_2\uparrow + 4\text{H}^+ + 4\text{e}$",
                "note": r"Các cation từ $\text{Li}^+$ đến $\text{Al}^{3+}$ không bị khử trong dung dịch mà $\text{H}_2\text{O}$ bị khử; các anion gốc acid có oxygen ($\text{SO}_4^{2-}, \text{NO}_3^-, \text{PO}_4^{3-}$) và $\text{F}^-$ không bị oxi hóa mà $\text{H}_2\text{O}$ bị oxi hóa.",
            },
            {
                "name": "Định luật Faraday về điện phân",
                "formula": r"$n_{\text{e}} = \dfrac{q}{F} = \dfrac{I \cdot t}{F}$ và $m = \dfrac{A \cdot I \cdot t}{n \cdot F}$",
                "note": r"$I$ là cường độ dòng điện ($\text{A}$), $t$ là thời gian điện phân ($\text{s}$), $F = 96500\text{ C/mol}$, $A$ là khối lượng mol nguyên tử ($\text{g/mol}$), $n$ là số electron trao đổi.",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 15. Thế điện cực và nguồn điện hoá học",
                "content": [
                    r"**Cặp oxi hóa – khử và thế điện cực chuẩn**: Mỗi kim loại $\text{M}$ nhường $n$ electron tạo cation $\text{M}^{n+}$ theo cân bằng $\text{M}^{n+} + n\text{e} \rightleftharpoons \text{M}$, tạo thành cặp oxi hóa – khử $\text{M}^{n+}/\text{M}$. Thế điện cực chuẩn $E^\circ_{\text{M}^{n+}/\text{M}}$ được đo ở điều kiện chuẩn ($C_{\text{M}^{n+}} = 1\text{ M}$, $P = 1\text{ bar}$ với chất khí, $T = 298\text{ K}$ hay $25^\circ\text{C}$) bằng cách ghép với điện cực chuẩn hydrogen ($E^\circ_{2\text{H}^+/\text{H}_2} = 0{,}00\text{ V}$). Sắp xếp các cặp oxi hóa – khử theo chiều tăng dần của thế điện cực chuẩn $E^\circ$ ta được **dãy điện hóa**: $\text{K}^+/\text{K}$, $\text{Na}^+/\text{Na}$, $\text{Mg}^{2+}/\text{Mg}$, $\text{Al}^{3+}/\text{Al}$, $\text{Zn}^{2+}/\text{Zn}$, $\text{Fe}^{2+}/\text{Fe}$, $\text{Ni}^{2+}/\text{Ni}$, $\text{Sn}^{2+}/\text{Sn}$, $\text{Pb}^{2+}/\text{Pb}$, $2\text{H}^+/\text{H}_2$, $\text{Cu}^{2+}/\text{Cu}$, $\text{Fe}^{3+}/\text{Fe}^{2+}$, $\text{Ag}^+/\text{Ag}$, $\text{Au}^{3+}/\text{Au}$. Từ trái sang phải theo chiều $E^\circ$ tăng dần: **tính oxi hóa của dạng oxi hóa tăng dần, tính khử của dạng khử giảm dần**.",
                    r"**Quy tắc alpha ($\alpha$)**: Phản ứng giữa hai cặp oxi hóa – khử xảy ra theo chiều chất oxi hóa mạnh hơn (cặp có $E^\circ$ lớn hơn) oxi hóa chất khử mạnh hơn (cặp có $E^\circ$ nhỏ hơn) tạo thành chất oxi hóa yếu hơn và chất khử yếu hơn. Ví dụ, do $E^\circ_{\text{Cu}^{2+}/\text{Cu}} (+0{,}34\text{ V}) < E^\circ_{\text{Fe}^{3+}/\text{Fe}^{2+}} (+0{,}77\text{ V}) < E^\circ_{\text{Ag}^+/\text{Ag}} (+0{,}80\text{ V})$, nên $\text{Cu}$ tan trong dung dịch $\text{FeCl}_3$: $\text{Cu} + 2\text{Fe}^{3+} \rightarrow \text{Cu}^{2+} + 2\text{Fe}^{2+}$, và $\text{Fe}^{2+}$ bị $\text{Ag}^+$ oxi hóa hoàn toàn thành $\text{Fe}^{3+}$: $\text{Fe}^{2+} + \text{Ag}^+ \rightarrow \text{Fe}^{3+} + \text{Ag}\downarrow$.",
                    r"**Pin Galvani và các nguồn điện hóa học**: Pin Galvani biến đổi trực tiếp hóa năng của phản ứng oxi hóa – khử tự diễn biến thành điện năng. Trong pin Galvani $\text{X–Y}$ (với $E^\circ_{\text{X}^{x+}/\text{X}} < E^\circ_{\text{Y}^{y+}/\text{Y}}$): Điện cực $\text{X}$ là **anode (cực âm)** xảy ra quá trình oxi hóa $\text{X} \rightarrow \text{X}^{x+} + x\text{e}$ (thanh $\text{X}$ tan dần, khối lượng giảm); điện cực $\text{Y}$ là **cathode (cực dương)** xảy ra quá trình khử $\text{Y}^{y+} + y\text{e} \rightarrow \text{Y}$ (khối lượng thanh $\text{Y}$ tăng lên); dòng electron chạy ở mạch ngoài từ anode sang cathode; **cầu muối** (chứa dung dịch muối bão hòa như $\text{KCl}$ hoặc $\text{KNO}_3$ trong thạch agar) giúp đóng kín mạch điện và duy trì sự trung hòa điện của hai dung dịch (cation trong cầu muối di chuyển về nửa pin cathode, anion di chuyển về nửa pin anode). Ngoài pin Galvani, thực tế còn dùng **acquy chì** (pin thứ cấp có thể sạc lại), **pin nhiên liệu $\text{H}_2\text{–O}_2$** (hiệu suất cao, chỉ tạo sản phẩm là $\text{H}_2\text{O}$ không gây ô nhiễm), **pin lithium-ion** và **pin mặt trời** (chuyển hóa quang năng thành điện năng).",
                ],
            },
            {
                "title": "Bài 16. Điện phân",
                "content": [
                    r"**Nguyên tắc điện phân**: Điện phân là quá trình dùng dòng điện một chiều để thực hiện phản ứng oxi hóa – khử không tự diễn biến. Trong bình điện phân: **Cathode được nối với cực âm của nguồn điện** (thu hút cation về phía mình và xảy ra **quá trình khử**: chất có tính oxi hóa mạnh hơn bị khử trước); **Anode được nối với cực dương của nguồn điện** (thu hút anion về phía mình và xảy ra **quá trình oxi hóa**: chất có tính khử mạnh hơn bị oxi hóa trước). Lưu ý: cả trong pin điện và bình điện phân, **anode luôn là nơi xảy ra sự oxi hóa, cathode luôn là nơi xảy ra sự khử**, nhưng dấu điện cực thì ngược nhau (ở pin điện: anode âm, cathode dương; ở bình điện phân: anode dương, cathode âm).",
                    r"**Điện phân nóng chảy và điện phân dung dịch**: (1) **Điện phân nóng chảy**: Dùng để điều chế các kim loại hoạt động mạnh (nhóm $\text{IA}, \text{IIA}$ và $\text{Al}$) từ muối halide nóng chảy ($2\text{NaCl} \xrightarrow{\text{đpnc}} 2\text{Na} + \text{Cl}_2\uparrow$, $\text{MgCl}_2 \xrightarrow{\text{đpnc}} \text{Mg} + \text{Cl}_2\uparrow$) hoặc oxide nóng chảy ($2\text{Al}_2\text{O}_3 \xrightarrow{\text{đpnc, } \text{Na}_3\text{AlF}_6} 4\text{Al} + 3\text{O}_2\uparrow$). (2) **Điện phân dung dịch với điện cực trơ (graphite, $\text{Pt}$)**: Tại cathode, các ion $\text{Li}^+\to\text{Al}^{3+}$ không bị khử mà $\text{H}_2\text{O}$ bị khử ($2\text{H}_2\text{O} + 2\text{e} \rightarrow \text{H}_2\uparrow + 2\text{OH}^-$); các ion từ $\text{Zn}^{2+}$ đến $\text{Au}^{3+}$ bị khử theo thứ tự tính oxi hóa giảm dần ($\text{Ag}^+ > \text{Fe}^{3+} > \text{Cu}^{2+} > \text{H}^+ > \text{Fe}^{2+} > \text{Zn}^{2+}$). Tại anode, các anion $\text{S}^{2-} > \text{I}^- > \text{Br}^- > \text{Cl}^-$ bị oxi hóa trước; còn các anion chứa oxygen ($\text{SO}_4^{2-}, \text{NO}_3^-, \text{PO}_4^{3-}, \text{CO}_3^{2-}$) và $\text{F}^-$ không bị oxi hóa mà $\text{H}_2\text{O}$ bị oxi hóa ($2\text{H}_2\text{O} \rightarrow \text{O}_2\uparrow + 4\text{H}^+ + 4\text{e}$). Ví dụ: điện phân dung dịch $\text{CuSO}_4$ thu được $\text{Cu}$ ở cathode, khí $\text{O}_2$ ở anode và dung dịch $\text{H}_2\text{SO}_4$ ($\text{pH}$ giảm); điện phân dung dịch $\text{NaCl}$ bão hòa có màng ngăn thu được $\text{H}_2$ ở cathode, $\text{Cl}_2$ ở anode và dung dịch $\text{NaOH}$ ($\text{pH}$ tăng), nếu không có màng ngăn thì tạo nước Javel ($\text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$).",
                    r"**Ứng dụng مạ điện và tinh luyện kim loại**: Khi **mạ điện** (ví dụ mạ bạc hoặc mạ đồng lên vật bằng thép) hoặc **tinh luyện đồng**, người ta dùng **anode tan** làm bằng chính kim loại dùng để mạ hoặc khối đồng thô cần tinh luyện (tại anode: $\text{Cu} \rightarrow \text{Cu}^{2+} + 2\text{e}$), còn **cathode** là vật cần mạ hoặc tấm đồng nguyên chất mỏng (tại cathode: $\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$), nhúng trong dung dịch muối của kim loại đó ($\text{CuSO}_4$); nồng độ ion $\text{Cu}^{2+}$ trong dung dịch không đổi trong suốt quá trình mạ.",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Tính sức điện động chuẩn và viết phản ứng trong pin Galvani",
                "problem": (
                    r"Cho thế điện cực chuẩn của các cặp oxi hóa – khử: $E^\circ_{\text{Ni}^{2+}/\text{Ni}} = -0{,}257\text{ V}$ và "
                    r"$E^\circ_{\text{Ag}^+/\text{Ag}} = +0{,}799\text{ V}$. Thiết lập một pin Galvani $\text{Ni–Ag}$ ở điều kiện chuẩn. "
                    r"Xác định anode, cathode, viết các bán phản ứng, phản ứng tổng quát và tính sức điện động chuẩn $E^\circ_{\text{pin}}$ của pin."
                ),
                "solution": (
                    r"- Vì $E^\circ_{\text{Ni}^{2+}/\text{Ni}} (-0{,}257\text{ V}) < E^\circ_{\text{Ag}^+/\text{Ag}} (+0{,}799\text{ V})$, nên thanh $\text{Ni}$ là **anode (cực âm)** và thanh $\text{Ag}$ là **cathode (cực dương)**." "\n"
                    r"- Bán phản ứng tại anode (-): $\text{Ni}(s) \rightarrow \text{Ni}^{2+}(aq) + 2\text{e}$ (quá trình oxi hóa)." "\n"
                    r"- Bán phản ứng tại cathode (+): $\text{Ag}^+(aq) + 1\text{e} \rightarrow \text{Ag}(s)$ (quá trình khử)." "\n"
                    r"- Phản ứng hóa học xảy ra trong pin: $\text{Ni}(s) + 2\text{Ag}^+(aq) \rightarrow \text{Ni}^{2+}(aq) + 2\text{Ag}(s)$." "\n"
                    r"- Sức điện động chuẩn của pin: $E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = 0{,}799 - (-0{,}257) = 1{,}056\text{ V}$."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán điện phân dung dịch áp dụng định luật Faraday",
                "problem": (
                    r"Điện phân $200\text{ mL}$ dung dịch $\text{CuSO}_4\text{ } 1{,}0\text{ M}$ với điện cực trơ bằng dòng điện một chiều có cường độ "
                    r"không đổi $I = 9{,}65\text{ A}$ trong thời gian $t = 2000\text{ s}$. Tính khối lượng $\text{Cu}$ bám trên cathode và thể tích khí "
                    r"(đkc $25^\circ\text{C}, 1\text{ bar}$) thoát ra ở anode."
                ),
                "solution": (
                    r"- Số mol electron trao đổi ở mỗi điện cực: $n_{\text{e}} = \dfrac{I \cdot t}{F} = \dfrac{9{,}65 \cdot 2000}{96500} = 0{,}20\text{ mol}$." "\n"
                    r"- Số mol $\text{CuSO}_4$ ban đầu: $n_{\text{Cu}^{2+}} = 0{,}20 \cdot 1{,}0 = 0{,}20\text{ mol}$. Tại cathode (-): $\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$, do $2n_{\text{Cu}^{2+}} = 0{,}40\text{ mol} > n_{\text{e}} = 0{,}20\text{ mol}$ nên $\text{Cu}^{2+}$ còn dư." "\n"
                    r"- Số mol $\text{Cu}$ thu được ở cathode: $n_{\text{Cu}} = \dfrac{n_{\text{e}}}{2} = 0{,}10\text{ mol} \Rightarrow m_{\text{Cu}} = 0{,}10 \cdot 64 = 6{,}4\text{ g}$." "\n"
                    r"- Tại anode (+): $2\text{H}_2\text{O} \rightarrow \text{O}_2\uparrow + 4\text{H}^+ + 4\text{e} \Rightarrow n_{\text{O}_2} = \dfrac{n_{\text{e}}}{4} = \dfrac{0{,}20}{4} = 0{,}05\text{ mol} \Rightarrow V_{\text{O}_2\text{ (đkc)}} = 0{,}05 \cdot 24{,}79 = 1{,}2395\text{ L}$."
                ),
            },
        ],
        key_takeaways=[
            r"Thế điện cực chuẩn $E^\circ_{\text{M}^{n+}/\text{M}}$ càng nhỏ thì tính khử của kim loại $\text{M}$ càng mạnh và tính oxi hóa của ion $\text{M}^{n+}$ càng yếu.",
            r"Trong mọi hệ điện hóa (cả pin Galvani và bình điện phân): **Anode luôn xảy ra sự oxi hóa**, **Cathode luôn xảy ra sự khử**.",
            r"Trong pin Galvani: Anode là cực âm (kim loại mạnh hơn), Cathode là cực dương (kim loại yếu hơn), $E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} > 0$.",
            r"Định luật Faraday: $n_{\text{e}} = \dfrac{I \cdot t}{F}$ với $F = 96500\text{ C/mol}$. Khi mạ điện, vật cần mạ gắn vào cathode (-), kim loại dùng để mạ gắn vào anode (+).",
        ],
        questions=[
            mcq(
                question=r"Kí hiệu cặp oxi hóa – khử ứng với bán phản ứng $\text{Fe}^{3+} + 1\text{e} \rightleftharpoons \text{Fe}^{2+}$ là:",
                options=[
                    r"$\text{Fe}^{2+}/\text{Fe}^{3+}$.",
                    r"$\text{Fe}^{3+}/\text{Fe}^{2+}$.",
                    r"$\text{Fe}^{3+}/\text{Fe}$.",
                    r"$\text{Fe}^{2+}/\text{Fe}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Theo quy ước viết cặp oxi hóa – khử $\text{Dạng oxi hóa}/\text{Dạng khử}$, trong cân bằng $\text{Fe}^{3+} + 1\text{e} \rightleftharpoons \text{Fe}^{2+}$, "
                    r"dạng oxi hóa là $\text{Fe}^{3+}$ và dạng khử là $\text{Fe}^{2+}$, nên kí hiệu đúng là $\text{Fe}^{3+}/\text{Fe}^{2+}$."
                ),
            ),
            mcq(
                question=r"Khi pin Galvani $\text{Zn–Cu}$ hoạt động, quá trình nào sau đây xảy ra tại cực âm (anode)?",
                options=[
                    r"$\text{Zn} \rightarrow \text{Zn}^{2+} + 2\text{e}$.",
                    r"$\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$.",
                    r"$\text{Zn}^{2+} + 2\text{e} \rightarrow \text{Zn}$.",
                    r"$\text{Cu} \rightarrow \text{Cu}^{2+} + 2\text{e}$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Trong pin Galvani $\text{Zn–Cu}$, kim loại $\text{Zn}$ có tính khử mạnh hơn $\text{Cu}$ ($E^\circ_{\text{Zn}^{2+}/\text{Zn}} < E^\circ_{\text{Cu}^{2+}/\text{Cu}}$) "
                    r"nên thanh $\text{Zn}$ đóng vai trò là anode (cực âm) và xảy ra quá trình oxi hóa: $\text{Zn} \rightarrow \text{Zn}^{2+} + 2\text{e}$."
                ),
            ),
            mcq(
                question=r"Trong công nghiệp, kim loại aluminium ($\text{Al}$) được sản xuất bằng phương pháp điện phân nóng chảy hợp chất nào sau đây (có mặt cryolite $\text{Na}_3\text{AlF}_6$)?",
                options=[
                    r"$\text{AlCl}_3$.",
                    r"$\text{Al}_2\text{O}_3$.",
                    r"$\text{Al}_2(\text{SO}_4)_3$.",
                    r"$\text{Al(NO}_3)_3$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Trong công nghiệp, $\text{Al}$ được điều chế bằng phương pháp điện phân nóng chảy $\text{Al}_2\text{O}_3$ (tinh chế từ quặng bauxite) có hòa tan trong $\text{Na}_3\text{AlF}_6$ nóng chảy để hạ nhiệt độ nóng chảy: $2\text{Al}_2\text{O}_3 \xrightarrow{\text{đpnc}} 4\text{Al} + 3\text{O}_2\uparrow$."
                ),
            ),
            mcq(
                question=r"Khi điện phân dung dịch $\text{CuSO}_4$ với hai điện cực trơ (graphite), chất khí thoát ra ở anode (cực dương) là:",
                options=[
                    r"Khí $\text{H}_2$.",
                    r"Khí $\text{SO}_2$.",
                    r"Khí $\text{O}_2$.",
                    r"Khí $\text{H}_2\text{S}$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Khi điện phân dung dịch $\text{CuSO}_4$ với điện cực trơ, tại anode (+) ion $\text{SO}_4^{2-}$ không bị oxi hóa mà phân tử $\text{H}_2\text{O}$ bị oxi hóa giải phóng khí $\text{O}_2$: $2\text{H}_2\text{O} \rightarrow \text{O}_2\uparrow + 4\text{H}^+ + 4\text{e}$."
                ),
            ),
            mcq(
                question=(
                    r"Cho biết thế điện cực chuẩn: $E^\circ_{\text{Mg}^{2+}/\text{Mg}} = -2{,}356\text{ V}$; $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0{,}762\text{ V}$; "
                    r"$E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0{,}340\text{ V}$; $E^\circ_{\text{Ag}^+/\text{Ag}} = +0{,}799\text{ V}$. "
                    r"Pin Galvani được ghép từ cặp điện cực chuẩn nào sau đây có sức điện động chuẩn $E^\circ_{\text{pin}}$ lớn nhất?"
                ),
                options=[
                    r"Pin $\text{Zn–Cu}$.",
                    r"Pin $\text{Zn–Ag}$.",
                    r"Pin $\text{Mg–Cu}$.",
                    r"Pin $\text{Mg–Ag}$.",
                ],
                answer="D",
                level="hieu",
                solution=(
                    r"Ta có $E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}}$. Sức điện động chuẩn lớn nhất khi ghép cặp có $E^\circ$ lớn nhất ($\text{Ag}^+/\text{Ag}$) "
                    r"với cặp có $E^\circ$ nhỏ nhất ($\text{Mg}^{2+}/\text{Mg}$): $E^\circ_{\text{pin Mg–Ag}} = 0{,}799 - (-2{,}356) = 3{,}155\text{ V}$."
                ),
            ),
            mcq(
                question=(
                    r"Cho thế điện cực chuẩn: $E^\circ_{\text{Fe}^{2+}/\text{Fe}} = -0{,}44\text{ V}$; $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0{,}34\text{ V}$; "
                    r"$E^\circ_{\text{Fe}^{3+}/\text{Fe}^{2+}} = +0{,}77\text{ V}$; $E^\circ_{\text{Ag}^+/\text{Ag}} = +0{,}80\text{ V}$. "
                    r"Cho lượng dư bột $\text{Fe}$ tác dụng với dung dịch $\text{AgNO}_3$, sau khi các phản ứng kết thúc thu được dung dịch chứa muối nào?"
                ),
                options=[
                    r"$\text{Fe(NO}_3)_2$.",
                    r"$\text{Fe(NO}_3)_3$.",
                    r"$\text{Fe(NO}_3)_3$ và $\text{AgNO}_3$.",
                    r"$\text{Fe(NO}_3)_2$ và $\text{Fe(NO}_3)_3$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Khi cho $\text{Fe}$ dư vào dung dịch $\text{AgNO}_3$, đầu tiên $\text{Fe} + 2\text{Ag}^+ \rightarrow \text{Fe}^{2+} + 2\text{Ag}\downarrow$. "
                    r"Do $\text{Fe}$ còn dư nên không tạo $\text{Fe}^{3+}$ (hoặc nếu tạo $\text{Fe}^{3+}$ thì bị $\text{Fe}$ dư khử ngay về $\text{Fe}^{2+}$ theo phản ứng $\text{Fe} + 2\text{Fe}^{3+} \rightarrow 3\text{Fe}^{2+}$). "
                    r"Vậy dung dịch sau phản ứng chỉ chứa muối $\text{Fe(NO}_3)_2$."
                ),
            ),
            tf4(
                stem=(
                    r"Lắp một pin điện hóa Galvani gồm một thanh kẽm ($\text{Zn}$) nhúng trong cốc đựng dung dịch $\text{ZnSO}_4\text{ } 1\text{ M}$ "
                    r"và một thanh đồng ($\text{Cu}$) nhúng trong cốc đựng dung dịch $\text{CuSO}_4\text{ } 1\text{ M}$ ở $25^\circ\text{C}$, "
                    r"hai cốc được nối với nhau bằng một cầu muối chứa dung dịch $\text{KCl}$ bão hòa. Cho biết $E^\circ_{\text{Zn}^{2+}/\text{Zn}} = -0{,}762\text{ V}$ "
                    r"và $E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0{,}340\text{ V}$."
                ),
                statements=[
                    r"Trong quá trình pin hoạt động, thanh $\text{Zn}$ đóng vai trò là anode (cực âm) bị ăn mòn dần làm khối lượng giảm đi, còn thanh $\text{Cu}$ là cathode (cực dương) có khối lượng tăng lên.",
                    r"Ở mạch ngoài, dòng electron chuyển dời từ điện cực $\text{Cu}$ sang điện cực $\text{Zn}$ qua dây dẫn kim loại.",
                    r"Trong cầu muối, các ion $\text{K}^+$ di chuyển vào cốc đựng dung dịch $\text{CuSO}_4$, còn các ion $\text{Cl}^-$ di chuyển vào cốc đựng dung dịch $\text{ZnSO}_4$ để giữ cho hai dung dịch trung hòa về điện.",
                    r"Sức điện động chuẩn của pin Galvani $\text{Zn–Cu}$ trên bằng $0{,}422\text{ V}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Tại anode (-), $\text{Zn} \rightarrow \text{Zn}^{2+} + 2\text{e}$ nên thanh $\text{Zn}$ tan dần; tại cathode (+), $\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$ bám vào làm khối lượng thanh $\text{Cu}$ tăng." "\n"
                    r"- **b) Sai**: Ở mạch ngoài, dòng electron di chuyển từ cực âm (anode $\text{Zn}$, nơi nhường electron) sang cực dương (cathode $\text{Cu}$, nơi nhận electron)." "\n"
                    r"- **c) Đúng**: Ở cốc anode ($\text{ZnSO}_4$) dư điện tích dương $\text{Zn}^{2+}$ nên hút anion $\text{Cl}^-$ từ cầu muối đi xuống; ở cốc cathode ($\text{CuSO}_4$) thiếu hụt cation $\text{Cu}^{2+}$ nên hút cation $\text{K}^+$ từ cầu muối đi xuống." "\n"
                    r"- **d) Sai**: Sức điện động chuẩn của pin là $E^\circ_{\text{pin}} = E^\circ_{\text{Cu}^{2+}/\text{Cu}} - E^\circ_{\text{Zn}^{2+}/\text{Zn}} = 0{,}340 - (-0{,}762) = 1{,}102\text{ V}$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét quá trình điện phân các dung dịch trong phòng thí nghiệm và ứng dụng mạ điện trong công nghiệp."
                ),
                statements=[
                    r"Khi điện phân dung dịch $\text{NaCl}$ bão hòa với điện cực trơ có màng ngăn xốp, sản phẩm thu được gồm khí $\text{H}_2$ ở cathode, khí $\text{Cl}_2$ ở anode và dung dịch $\text{NaOH}$ làm $\text{pH}$ của dung dịch tăng lên.",
                    r"Khi điện phân dung dịch hỗn hợp gồm $\text{Cu(NO}_3)_2$ và $\text{AgNO}_3$ với điện cực trơ, tại cathode ion $\text{Cu}^{2+}$ bị khử trước ion $\text{Ag}^+$.",
                    r"Để mạ một lớp bạc ($\text{Ag}$) lên một chiếc huy chương bằng đồng ($\text{Cu}$), người ta gắn chiếc huy chương vào cực âm (cathode) và gắn thanh bạc nguyên chất vào cực dương (anode) trong dung dịch muối $\text{AgNO}_3$.",
                    r"Khi điện phân dung dịch $\text{CuSO}_4$ với anode bằng đồng ($\text{Cu}$, anode tan) và cathode bằng đồng, nồng độ ion $\text{Cu}^{2+}$ trong dung dịch giảm dần theo thời gian điện phân.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Phương trình điện phân có màng ngăn: $2\text{NaCl} + 2\text{H}_2\text{O} \xrightarrow{\text{đpdd, mn}} 2\text{NaOH} + \text{H}_2\uparrow\text{ (cathode)} + \text{Cl}_2\uparrow\text{ (anode)}$, tạo $\text{NaOH}$ nên $\text{pH}$ tăng." "\n"
                    r"- **b) Sai**: Do tính oxi hóa của $\text{Ag}^+$ mạnh hơn $\text{Cu}^{2+}$ ($E^\circ_{\text{Ag}^+/\text{Ag}} = +0{,}80\text{ V} > E^\circ_{\text{Cu}^{2+}/\text{Cu}} = +0{,}34\text{ V}$), nên tại cathode ion $\text{Ag}^+$ bị khử thành $\text{Ag}$ trước, hết $\text{Ag}^+$ mới đến $\text{Cu}^{2+}$ bị khử." "\n"
                    r"- **c) Đúng**: Trong kỹ thuật mạ điện, vật cần mạ luôn gắn với cực âm (cathode) để ion kim loại đến nhận electron bám lên bề mặt, còn kim loại dùng để mạ gắn với cực dương (anode tan)." "\n"
                    r"- **d) Sai**: Khi dùng anode bằng $\text{Cu}$ (anode tan), lượng $\text{Cu}$ tan ra ở anode ($\text{Cu} \rightarrow \text{Cu}^{2+} + 2\text{e}$) đúng bằng lượng $\text{Cu}^{2+}$ bị khử bám vào cathode ($\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$), nên nồng độ $\text{Cu}^{2+}$ trong dung dịch không đổi."
                ),
            ),
            mcq(
                question=(
                    r"Điện phân $400\text{ mL}$ dung dịch hỗn hợp gồm $\text{AgNO}_3\text{ } 0{,}25\text{ M}$ và $\text{Cu(NO}_3)_2\text{ } 0{,}50\text{ M}$ "
                    r"với điện cực trơ bằng dòng điện một chiều có cường độ $I = 5{,}0\text{ A}$ trong thời gian $t = 9650\text{ s}$. "
                    r"Giả sử toàn bộ kim loại sinh ra đều bám hết vào cathode. Tổng khối lượng kim loại bám trên cathode sau khi kết thúc điện phân là:"
                ),
                options=[
                    r"$23{,}6\text{ g}$.",
                    r"$17{,}2\text{ g}$.",
                    r"$26{,}8\text{ g}$.",
                    r"$10{,}8\text{ g}$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Số mol electron trao đổi: $n_{\text{e}} = \dfrac{I \cdot t}{F} = \dfrac{5{,}0 \cdot 9650}{96500} = 0{,}50\text{ mol}$. "
                    r"Trong dung dịch có $n_{\text{Ag}^+} = 0{,}40 \cdot 0{,}25 = 0{,}10\text{ mol}$ và $n_{\text{Cu}^{2+}} = 0{,}40 \cdot 0{,}50 = 0{,}20\text{ mol}$. "
                    r"Tại cathode (-): đầu tiên $\text{Ag}^+ + 1\text{e} \rightarrow \text{Ag}$ hết $0{,}10\text{ mol}$ $\text{Ag}^+$ (nhận $0{,}10\text{ mol}$ $\text{e}$); "
                    r"tiếp theo $\text{Cu}^{2+} + 2\text{e} \rightarrow \text{Cu}$ nhận $0{,}50 - 0{,}10 = 0{,}40\text{ mol}$ $\text{e}$, tạo vừa đủ $\dfrac{0{,}40}{2} = 0{,}20\text{ mol}$ $\text{Cu}$. "
                    r"Tổng khối lượng kim loại bám trên cathode là $m = 0{,}10 \cdot 108 + 0{,}20 \cdot 64 = 10{,}8 + 12{,}8 = 23{,}6\text{ g}$."
                ),
            ),
            short(
                question=(
                    r"Trong công nghiệp, người ta sản xuất nhôm ($\text{Al}$, $A = 27\text{ g/mol}$) bằng phương pháp điện phân nóng chảy $\text{Al}_2\text{O}_3$ "
                    r"với cường độ dòng điện $I = 96500\text{ A}$. Giả sử hiệu suất sử dụng dòng điện đạt $100\%$. Trong thời gian $1\text{ giờ}$ ($3600\text{ s}$), "
                    r"bình điện phân đó sản xuất được bao nhiêu $\text{kg}$ nhôm kim loại (làm tròn kết quả đến hàng phần mười)?"
                ),
                answer=["32,4", "32.4"],
                level="vandung",
                solution=(
                    r"- Số mol electron trao đổi trong $t = 3600\text{ s}$ là: $n_{\text{e}} = \dfrac{I \cdot t}{F} = \dfrac{96500 \cdot 3600}{96500} = 3600\text{ mol}$." "\n"
                    r"- Tại cathode (-): $\text{Al}^{3+} + 3\text{e} \rightarrow \text{Al} \Rightarrow n_{\text{Al}} = \dfrac{n_{\text{e}}}{3} = \dfrac{3600}{3} = 1200\text{ mol}$." "\n"
                    r"- Khối lượng $\text{Al}$ thu được là: $m_{\text{Al}} = 1200 \cdot 27 = 32400\text{ g} = 32{,}4\text{ kg}$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 6: ĐẠI CƯƠNG VỀ KIM LOẠI, NHÓM IA, IIA, KIM LOẠI CHUYỂN TIẾP VÀ PHỨC CHẤT
    # =========================================================================
    lesson(
        grade=12,
        order=6,
        code="H12-C06",
        title="Chương 6: Đại cương về Kim loại, Nguyên tố nhóm IA, IIA, Kim loại chuyển tiếp dãy thứ nhất và Phức chất",
        topic="dai-cuong-kim-loai-phuc-chat",
        description=(
            "Chương 6 SGK Hóa học 12 Kết nối tri thức: Cấu tạo, tính chất, tách kim loại, hợp kim, ăn mòn và chống ăn mòn kim loại; "
            "nguyên tố nhóm IA, nhóm IIA và nước cứng; kim loại chuyển tiếp dãy thứ nhất, chuẩn độ Fe(II) và đại cương về phức chất."
        ),
        summary=(
            r"Trong mạng tinh thể kim loại, các nguyên tử và ion dương kim loại nằm ở nút mạng, còn các **electron hóa trị tự do** chuyển động "
            r"hỗn loạn tạo nên **liên kết kim loại** quyết định $4$ tính chất vật lý chung của kim loại: **tính dẻo, tính dẫn điện, tính dẫn nhiệt và ánh kim**. "
            r"Tính chất hóa học chung của kim loại là **tính khử** ($\text{M} \rightarrow \text{M}^{n+} + n\text{e}$). Ba phương pháp tách kim loại từ quặng là "
            r"**điện phân nóng chảy** (kim loại mạnh từ $\text{Li}\to\text{Al}$), **nhiệt luyện** (khử oxide của kim loại trung bình và yếu từ $\text{Zn}$ trở đi bằng $\text{CO}, \text{H}_2, \text{C}, \text{Al}$ ở nhiệt độ cao) "
            r"và **thủy luyện**. **Ăn mòn điện hóa** xảy ra khi hai điện cực khác nhau bản chất tiếp xúc với nhau và cùng tiếp xúc với dung dịch chất điện li; "
            r"có thể bảo vệ kim loại bằng cách sơn phủ cách ly hoặc **phương pháp điện hóa** (gắn kim loại hoạt động hơn như $\text{Zn}$ làm **anode hy sinh** để bảo vệ vỏ tàu biển bằng thép). "
            r"**Kim loại kiềm (nhóm IA, $ns^1$)** và **kim loại kiềm thổ (nhóm IIA, $ns^2$)** có tính khử rất mạnh; **nước cứng** chứa nhiều ion $\text{Ca}^{2+}, \text{Mg}^{2+}$ "
            r"(nước cứng tạm thời chứa $\text{HCO}_3^-$, nước cứng vĩnh cửu chứa $\text{Cl}^-, \text{SO}_4^{2-}$) được làm mềm bằng $\text{Na}_2\text{CO}_3, \text{Na}_3\text{PO}_4$ hoặc nhựa trao đổi ion. "
            r"**Kim loại chuyển tiếp dãy thứ nhất** ($\text{Sc}\to\text{Cu}$, cấu hình $[\text{Ar}]3d^{1\div 10}4s^{1\div 2}$) có nhiều trạng thái oxi hóa, ion có màu sắc và dễ tạo **phức chất**. "
            r"**Phức chất** gồm **nguyên tử trung tâm** $\text{M}^{n+}$ liên kết với các **phối tử** $\text{L}$ bằng liên kết cho – nhận (phối trí), có dạng hình học đường thẳng (số phối trí $2$, như $[\text{Ag(NH}_3)_2]^+$), "
            r"tứ diện hoặc vuông phẳng (số phối trí $4$, như $[\text{Zn(OH)}_4]^{2-}$, $[\text{PtCl}_2(\text{NH}_3)_2]$) và bát diện (số phối trí $6$, như $[\text{Cu(H}_2\text{O)}_6]^{2+}$, $[\text{Co(NH}_3)_6]^{3+}$)."
        ),
        objectives=[
            r"Giải thích được các tính chất vật lý chung của kim loại dựa trên electron tự do; trình bày được tính chất hóa học chung của kim loại, các phương pháp tách kim loại (điện phân nóng chảy, nhiệt luyện, thủy luyện), hợp kim, ăn mòn hóa học – ăn mòn điện hóa và cách chống ăn mòn.",
            r"Nêu được đặc điểm cấu hình electron, tính chất vật lý (màu ngọn lửa đặc trưng), tính khử mạnh của kim loại nhóm $\text{IA}$, nhóm $\text{IIA}$ và ứng dụng của các hợp chất $\text{NaCl}, \text{NaOH}, \text{NaHCO}_3, \text{Na}_2\text{CO}_3$ (quy trình Solvay), $\text{CaCO}_3, \text{Ca(OH)}_2$, thạch cao.",
            r"Phân biệt được nước cứng tạm thời, nước cứng vĩnh cửu, nước cứng toàn phần; giải thích được tác hại của nước cứng và các phương pháp làm mềm nước cứng.",
            r"Viết được cấu hình electron của các nguyên tố chuyển tiếp dãy thứ nhất ($\text{Sc}\to\text{Cu}$, chú ý $\text{Cr}$ và $\text{Cu}$); trình bày được nguyên tắc và thực hiện tính toán chuẩn độ dung dịch $\text{Fe}^{2+}$ bằng dung dịch $\text{KMnO}_4$ trong môi trường $\text{H}_2\text{SO}_4$ loãng.",
            r"Xác định được nguyên tử trung tâm, phối tử, số phối trí, điện tích cầu nội và dạng hình học (đường thẳng, tứ diện, vuông phẳng, bát diện) của phức chất.",
            r"Viết được các phương trình phản ứng thế phối tử tạo phức chất của $\text{Cu}^{2+}, \text{Ag}^+, \text{Zn}^{2+}$ trong dung dịch và nêu được vai trò của các phức chất sinh học – y học ($\text{hemoglobin}, \text{chlorophyll}, \text{cisplatin}$).",
        ],
        formulas=[
            {
                "name": "Phương pháp nhiệt luyện tách kim loại trung bình và yếu (sau Al)",
                "formula": r"$\text{Fe}_2\text{O}_3 + 3\text{CO} \xrightarrow{t^\circ} 2\text{Fe} + 3\text{CO}_2$; $\text{Cr}_2\text{O}_3 + 2\text{Al} \xrightarrow{t^\circ} 2\text{Cr} + \text{Al}_2\text{O}_3\text{ (phản ứng nhiệt nhôm)}$",
                "note": r"Khí $\text{CO}$ hoặc $\text{H}_2$ chỉ khử được các oxide của kim loại đứng **sau $\text{Al}$** trong dãy hoạt động hóa học (như $\text{ZnO}, \text{Fe}_2\text{O}_3, \text{CuO}$), không khử được $\text{MgO}, \text{Al}_2\text{O}_3$.",
            },
            {
                "name": "Quy trình Solvay sản xuất NaHCO3 và soda (Na2CO3) từ NaCl, NH3, CO2",
                "formula": r"$\text{NaCl} + \text{NH}_3 + \text{CO}_2 + \text{H}_2\text{O} \rightarrow \text{NaHCO}_3\downarrow + \text{NH}_4\text{Cl}$; $2\text{NaHCO}_3 \xrightarrow{t^\circ} \text{Na}_2\text{CO}_3 + \text{CO}_2\uparrow + \text{H}_2\text{O}$",
                "note": r"$\text{NaHCO}_3$ ít tan nên kết tinh tách ra trước; $\text{NH}_4\text{Cl}$ cho tác dụng với $\text{Ca(OH)}_2$ để thu hồi và tuần hoàn khí $\text{NH}_3$.",
            },
            {
                "name": "Phản ứng làm mềm nước cứng tạm thời bằng đun sôi hoặc dùng Na2CO3, Na3PO4 làm mềm mọi loại nước cứng",
                "formula": r"$\text{Ca(HCO}_3)_2 \xrightarrow{t^\circ} \text{CaCO}_3\downarrow + \text{CO}_2\uparrow + \text{H}_2\text{O}$; $\text{Ca}^{2+} + \text{CO}_3^{2-} \rightarrow \text{CaCO}_3\downarrow$; $\text{Mg}^{2+} + \text{CO}_3^{2-} \rightarrow \text{MgCO}_3\downarrow$",
                "note": r"Nguyên tắc làm mềm nước cứng là làm giảm nồng độ các ion $\text{Ca}^{2+}$ và $\text{Mg}^{2+}$ trong nước.",
            },
            {
                "name": "Phản ứng chuẩn độ ion Fe(II) bằng dung dịch KMnO4 trong môi trường H2SO4 loãng",
                "formula": r"$10\text{FeSO}_4 + 2\text{KMnO}_4 + 8\text{H}_2\text{SO}_4 \rightarrow 5\text{Fe}_2(\text{SO}_4)_3 + \text{K}_2\text{SO}_4 + 2\text{MnSO}_4 + 8\text{H}_2\text{O}$",
                "note": r"Phương trình ion thu gọn: $5\text{Fe}^{2+} + \text{MnO}_4^- + 8\text{H}^+ \rightarrow 5\text{Fe}^{3+} + \text{Mn}^{2+} + 4\text{H}_2\text{O}$. Tại điểm tương đương: $n_{\text{Fe}^{2+}} = 5n_{\text{KMnO}_4}$.",
            },
            {
                "name": "Phản ứng thế phối tử của phức chất aqua đồng(II) trong dung dịch",
                "formula": r"$[\text{Cu(H}_2\text{O)}_6]^{2+}\text{ (xanh)} + 4\text{NH}_3 \rightarrow [\text{Cu(NH}_3)_4(\text{H}_2\text{O)}_2]^{2+}\text{ (xanh lam thẫm)} + 4\text{H}_2\text{O}$; $[\text{Cu(H}_2\text{O)}_6]^{2+}\text{ (xanh)} + 4\text{Cl}^-\text{ (đặc)} \rightleftharpoons [\text{CuCl}_4]^{2-}\text{ (vàng)} + 6\text{H}_2\text{O}$",
                "note": r"Với dung dịch $\text{NH}_3$, ban đầu tạo kết tủa xanh $\text{Cu(OH)}_2$, sau đó kết tủa tan trong $\text{NH}_3$ dư tạo phức $[\text{Cu(NH}_3)_4(\text{H}_2\text{O)}_2]^{2+}$ màu xanh lam thẫm.",
            },
        ],
        theory_sections=[
            {
                "title": "Bài 18–22. Đại cương về kim loại, Tách kim loại, Hợp kim và Ăn mòn kim loại",
                "content": [
                    r"**Tính chất vật lý và hóa học của kim loại**: Các electron hóa trị tự do trong mạng tinh thể kim loại gây ra tính dẻo (dễ rèn, dát mỏng: $\text{Au}$ dẻo nhất), tính dẫn điện ($\text{Ag} > \text{Cu} > \text{Au} > \text{Al} > \text{Fe}$), tính dẫn nhiệt và ánh kim. Các tính chất vật lý riêng: kim loại nhẹ nhất là $\text{Li}$ ($D = 0{,}53\text{ g/cm}^3$), nặng nhất là $\text{Os}$ ($D = 22{,}6\text{ g/cm}^3$); nhiệt độ nóng chảy thấp nhất là $\text{Hg}$ ($-39^\circ\text{C}$, thể lỏng ở điều kiện thường), cao nhất là $\text{W}$ ($3410^\circ\text{C}$, làm dây tóc bóng đèn); mềm nhất là $\text{Cs}$, cứng nhất là $\text{Cr}$ (cắt được thủy tinh). Về hóa học, kim loại luôn thể hiện **tính khử**: tác dụng với phi kim, nước, dung dịch acid và dung dịch muối. Lưu ý: **$\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong $\text{HNO}_3$ đặc, nguội và $\text{H}_2\text{SO}_4$ đặc, nguội**.",
                    r"**Các phương pháp tách kim loại**: (1) **Điện phân nóng chảy**: Tách các kim loại hoạt động mạnh ($\text{K}, \text{Na}, \text{Ca}, \text{Mg}, \text{Al}$). (2) **Nhiệt luyện**: Dùng chất khử ($\text{C}, \text{CO}, \text{H}_2, \text{Al}$) khử oxide kim loại trung bình và yếu (đứng sau $\text{Al}$ như $\text{Zn}, \text{Fe}, \text{Sn}, \text{Pb}, \text{Cu}$) ở nhiệt độ cao. (3) **Thủy luyện**: Hòa tan hợp chất kim loại bằng dung dịch thích hợp rồi dùng kim loại mạnh hơn đẩy kim loại yếu hơn ($\text{Cu}, \text{Ag}, \text{Au}$) ra khỏi dung dịch.",
                    r"**Ăn mòn kim loại và chống ăn mòn**: Có hai dạng ăn mòn là **ăn mòn hóa học** (electron của kim loại chuyển trực tiếp cho chất oxi hóa trong môi trường, không phát sinh dòng điện) và **ăn mòn điện hóa** (phát sinh dòng điện). **Ba điều kiện cần và đủ để xảy ra ăn mòn điện hóa**: (1) Hai điện cực khác nhau về bản chất (hai kim loại khác nhau hoặc kim loại – phi kim như $\text{Fe}-\text{C}$ trong gang, thép); (2) Hai điện cực tiếp xúc trực tiếp hoặc gián tiếp với nhau qua dây dẫn; (3) Hai điện cực cùng tiếp xúc với một dung dịch chất điện li (như không khí ẩm, nước biển). Khi xảy ra ăn mòn điện hóa, **kim loại có tính khử mạnh hơn luôn đóng vai trò là anode (cực âm) và bị ăn mòn trước**. Để bảo vệ kim loại, dùng **phương pháp bảo vệ bề mặt** (sơn, mạ, bôi dầu mỡ, tráng men) hoặc **phương pháp điện hóa** (gắn tấm $\text{Zn}$ vào vỏ tàu biển bằng thép làm anode hy sinh để $\text{Zn}$ bị ăn mòn thay cho $\text{Fe}$).",
                ],
            },
            {
                "title": "Bài 24–25. Nguyên tố nhóm IA, nhóm IIA và Nước cứng",
                "content": [
                    r"**Nguyên tố nhóm IA (kim loại kiềm) và nhóm IIA (kim loại kiềm thổ)**: Nhóm $\text{IA}$ ($\text{Li}, \text{Na}, \text{K}, \text{Rb}, \text{Cs}$) có cấu hình lớp ngoài cùng $ns^1$, mạng tinh thể lập phương tâm khối rỗng nên mềm, khối lượng riêng nhỏ, nhiệt độ nóng chảy thấp giảm dần từ $\text{Li}\to\text{Cs}$; tính khử rất mạnh tăng dần từ $\text{Li}\to\text{Cs}$, tác dụng mãnh liệt với nước ở nhiệt độ thường ($2\text{M} + 2\text{H}_2\text{O} \rightarrow 2\text{MOH} + \text{H}_2\uparrow$) nên phải bảo quản bằng cách ngâm trong dầu hỏa khan. Màu ngọn lửa đặc trưng của cation kim loại kiềm: $\text{Li}^+$ (đỏ tía), $\text{Na}^+$ (vàng), $\text{K}^+$ (tím). Nhóm $\text{IIA}$ ($\text{Be}, \text{Mg}, \text{Ca}, \text{Sr}, \text{Ba}$) có cấu hình $ns^2$: ở nhiệt độ thường, $\text{Be}$ không tác dụng với nước, $\text{Mg}$ khử chậm nước nóng, còn $\text{Ca}, \text{Sr}, \text{Ba}$ tác dụng mạnh với nước ở nhiệt độ thường. Màu ngọn lửa: $\text{Ca}^{2+}$ (đỏ cam), $\text{Sr}^{2+}$ (đỏ son), $\text{Ba}^{2+}$ (lục vàng).",
                    r"**Hợp chất quan trọng của nhóm IA, IIA và Nước cứng**: $\text{NaHCO}_3$ (baking soda) có tính lưỡng tính, kém bền nhiệt, dùng làm bột nở trong thực phẩm và thuốc giảm đau dạ dày do thừa acid; $\text{Na}_2\text{CO}_3$ (soda) dùng trong công nghiệp thủy tinh, xà phòng, giấy và làm mềm nước cứng; **thạch cao sống** ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$) nung ở khoảng $150^\circ\text{C}$ tạo **thạch cao nung** ($\text{CaSO}_4\cdot 0{,}5\text{H}_2\text{O}$ hoặc $\text{CaSO}_4\cdot\text{H}_2\text{O}$, dùng đúc tượng, bó bột khi gãy xương). **Nước cứng** là nước chứa nhiều ion $\text{Ca}^{2+}$ và $\text{Mg}^{2+}$: **nước cứng tạm thời** chứa anion $\text{HCO}_3^-$ (mất tính cứng khi đun sôi hoặc dùng lượng vừa đủ $\text{Ca(OH)}_2$, hoặc dùng $\text{Na}_2\text{CO}_3, \text{Na}_3\text{PO}_4$); **nước cứng vĩnh cửu** chứa anion $\text{Cl}^-, \text{SO}_4^{2-}$ (không làm mềm được bằng đun sôi hay $\text{Ca(OH)}_2$, phải dùng $\text{Na}_2\text{CO}_3, \text{Na}_3\text{PO}_4$ hoặc phương pháp trao đổi ion); **nước cứng toàn phần** có cả tính cứng tạm thời và vĩnh cửu.",
                ],
            },
            {
                "title": "Bài 27–29. Kim loại chuyển tiếp dãy thứ nhất và Phức chất",
                "content": [
                    r"**Kim loại chuyển tiếp dãy thứ nhất**: Gồm $9$ nguyên tố từ $\text{Sc}$ ($Z = 21$) đến $\text{Cu}$ ($Z = 29$) thuộc chu kì $4$, có cấu hình electron dạng $[\text{Ar}]3d^{1\div 10}4s^{1\div 2}$ (trong đó $\text{Cr}$ với $Z = 24$ có cấu hình $[\text{Ar}]3d^5 4s^1$ đạt bán bão hòa phân lớp $3d$; $\text{Cu}$ với $Z = 29$ có cấu hình $[\text{Ar}]3d^{10} 4s^1$ đạt bão hòa phân lớp $3d$; $\text{Fe}$ với $Z = 26$ có cấu hình $[\text{Ar}]3d^6 4s^2$, ion $\text{Fe}^{2+}$ là $[\text{Ar}]3d^6$, ion $\text{Fe}^{3+}$ là $[\text{Ar}]3d^5$). Khác với kim loại nhóm $\text{IA}, \text{IIA}$, các kim loại chuyển tiếp có độ cứng cao, nhiệt độ nóng chảy và khối lượng riêng lớn, có nhiều trạng thái oxi hóa khác nhau (ví dụ $\text{Mn}$ từ $+2$ đến $+7$, $\text{Cr}$ có $+2, +3, +6$, $\text{Fe}$ có $+2, +3$) và tạo ra các cation có màu sắc đặc trưng trong dung dịch ($\text{Cu}^{2+}$ xanh lam, $\text{Fe}^{2+}$ lục nhạt, $\text{Fe}^{3+}$ vàng nâu, $\text{Cr}^{3+}$ xanh lục). Nồng độ ion $\text{Fe}^{2+}$ được định lượng chính xác bằng phép **chuẩn độ oxi hóa – khử** với dung dịch $\text{KMnO}_4$ trong môi trường $\text{H}_2\text{SO}_4$ loãng (điểm kết thúc chuẩn độ là khi dung dịch xuất hiện màu hồng nhạt bền khoảng $20\text{ giây}$ của giọt $\text{KMnO}_4$ dư đầu tiên).",
                    r"**Đại cương về phức chất**: Phức chất là hợp chất có chứa **nguyên tử trung tâm** $\text{M}$ (thường là cation kim loại chuyển tiếp có orbital trống) liên kết với các **phối tử** $\text{L}$ (phân tử hoặc anion có cặp electron hóa trị riêng như $\text{H}_2\text{O}, \text{NH}_3, \text{CO}, \text{Cl}^-, \text{OH}^-, \text{CN}^-$ hoặc phối tử đa càng như $\text{ethylenediamine}$ $\text{H}_2\text{NCH}_2\text{CH}_2\text{NH}_2$, $\text{EDTA}$) bằng **liên kết cho – nhận (liên kết phối trí)**. Phần đặt trong ngoặc vuông $[\text{ML}_n]^{q\pm}$ gọi là **cầu nội**, các ion bên ngoài ngoặc vuông gọi là **cầu ngoại**. **Số phối trí** của nguyên tử trung tâm là số liên kết $\sigma$ giữa nguyên tử trung tâm với các phối tử, quyết định dạng hình học của phức chất: số phối trí $2$ có **dạng đường thẳng** ($[\text{Ag(NH}_3)_2]^+$, $[\text{Au(CN)}_2]^-$); số phối trí $4$ có **dạng tứ diện** ($[\text{Zn(OH)}_4]^{2-}$, $[\text{CoCl}_4]^{2-}$, $[\text{CuCl}_4]^{2-}$) hoặc **dạng vuông phẳng** ($[\text{PtCl}_4]^{2-}$, $[\text{PtCl}_2(\text{NH}_3)_2]$); số phối trí $6$ có **dạng bát diện** ($[\text{Cu(H}_2\text{O)}_6]^{2+}$, $[\text{Fe(H}_2\text{O)}_6]^{3+}$, $[\text{Co(NH}_3)_6]^{3+}$, $[\text{Fe(CN)}_6]^{4-}$). Phức chất có nhiều ứng dụng quan trọng: $\text{hemoglobin}$ (phức chất của $\text{Fe}^{2+}$ với nhân heme vận chuyển $\text{O}_2$ trong máu), $\text{chlorophyll}$ (diệp lục – phức chất của $\text{Mg}^{2+}$ giúp cây quang hợp), $\text{vitamin B}_{12}$ (phức chất của $\text{Co}^{3+}$), thuốc điều trị ung thư $\text{cisplatin}$ $[\text{PtCl}_2(\text{NH}_3)_2]$.",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Xác định thành phần và dạng hình học của phức chất",
                "problem": (
                    r"Cho các phức chất sau: (1) $[\text{Ag(NH}_3)_2]\text{OH}$, (2) $\text{K}_4[\text{Fe(CN)}_6]$, (3) $[\text{PtCl}_2(\text{NH}_3)_2]$. "
                    r"Hãy xác định nguyên tử trung tâm, phối tử, số phối trí của nguyên tử trung tâm, điện tích của cầu nội và dạng hình học của mỗi phức chất."
                ),
                "solution": (
                    r"- **(1) $[\text{Ag(NH}_3)_2]\text{OH}$**: Cầu nội là $[\text{Ag(NH}_3)_2]^+$ (điện tích $+1$); nguyên tử trung tâm là $\text{Ag}^+$; phối tử là $\text{NH}_3$; số phối trí bằng $2$; dạng hình học là **đường thẳng**." "\n"
                    r"- **(2) $\text{K}_4[\text{Fe(CN)}_6]$**: Cầu nội là $[\text{Fe(CN)}_6]^{4-}$ (điện tích $-4$); nguyên tử trung tâm là $\text{Fe}^{2+}$ (vì $+2 + 6\cdot(-1) = -4$); phối tử là $\text{CN}^-$; số phối trí bằng $6$; dạng hình học là **bát diện**." "\n"
                    r"- **(3) $[\text{PtCl}_2(\text{NH}_3)_2]$**: Phức chất trung hòa điện (điện tích cầu nội bằng $0$); nguyên tử trung tâm là $\text{Pt}^{2+}$; phối tử gồm $2$ phối tử $\text{Cl}^-$ và $2$ phối tử $\text{NH}_3$; số phối trí bằng $4$; dạng hình học là **vuông phẳng**."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán chuẩn độ dung dịch FeSO4 bằng dung dịch KMnO4",
                "problem": (
                    r"Để xác định nồng độ của một dung dịch $\text{FeSO}_4$, người ta lấy chính xác $10{,}0\text{ mL}$ dung dịch $\text{FeSO}_4$ "
                    r"cho vào bình tam giác, thêm khoảng $5\text{ mL}$ dung dịch $\text{H}_2\text{SO}_4\text{ } 2\text{ M}$ rồi chuẩn độ bằng dung dịch "
                    r"$\text{KMnO}_4\text{ } 0{,}020\text{ M}$ trên burette. Thể tích dung dịch $\text{KMnO}_4$ trung bình tiêu tốn tại điểm tương đương là "
                    r"$12{,}5\text{ mL}$. Tính nồng độ mol của dung dịch $\text{FeSO}_4$."
                ),
                "solution": (
                    r"- Phương trình ion của phản ứng chuẩn độ: $5\text{Fe}^{2+} + \text{MnO}_4^- + 8\text{H}^+ \rightarrow 5\text{Fe}^{3+} + \text{Mn}^{2+} + 4\text{H}_2\text{O}$." "\n"
                    r"- Số mol $\text{KMnO}_4$ đã phản ứng: $n_{\text{MnO}_4^-} = 0{,}0125 \cdot 0{,}020 = 2{,}5 \cdot 10^{-4}\text{ mol}$." "\n"
                    r"- Theo tỉ lệ phương trình: $n_{\text{Fe}^{2+}} = 5n_{\text{MnO}_4^-} = 5 \cdot 2{,}5 \cdot 10^{-4} = 1{,}25 \cdot 10^{-3}\text{ mol}$." "\n"
                    r"- Nồng độ mol của dung dịch $\text{FeSO}_4$ là: $C_{\text{M (FeSO}_4\text{)}} = \dfrac{1{,}25 \cdot 10^{-3}}{0{,}010} = 0{,}125\text{ M}$."
                ),
            },
        ],
        key_takeaways=[
            r"Khí $\text{CO}$ hoặc $\text{H}_2$ ở nhiệt độ cao chỉ khử được các oxide kim loại đứng **sau $\text{Al}$** trong dãy hoạt động hóa học; các kim loại từ $\text{Li}$ đến $\text{Al}$ phải điều chế bằng điện phân nóng chảy.",
            r"Trong ăn mòn điện hóa, kim loại hoạt động mạnh hơn đóng vai trò là **anode (cực âm)** và bị oxi hóa (ăn mòn) trước.",
            r"Nước cứng tạm thời chứa $\text{Ca(HCO}_3)_2, \text{Mg(HCO}_3)_2$; hóa chất làm mềm được mọi loại nước cứng là $\text{Na}_2\text{CO}_3$ và $\text{Na}_3\text{PO}_4$.",
            r"Chuẩn độ $\text{Fe}^{2+}$ bằng $\text{KMnO}_4/\text{H}_2\text{SO}_4$ loãng tuân theo tỉ lệ bảo toàn electron: $n_{\text{Fe}^{2+}} = 5n_{\text{KMnO}_4}$.",
            r"Số phối trí của nguyên tử trung tâm trong phức chất bằng tổng số liên kết $\sigma$ giữa nguyên tử trung tâm với các phối tử (với phối tử đơn càng như $\text{H}_2\text{O}, \text{NH}_3, \text{Cl}^-, \text{CN}^-$, số phối trí bằng tổng số phối tử trong cầu nội).",
        ],
        questions=[
            mcq(
                question=r"Để bảo vệ vỏ tàu biển làm bằng thép (hợp kim của $\text{Fe}$ và $\text{C}$) khỏi bị ăn mòn bởi nước biển theo phương pháp điện hóa, người ta gắn vào phần vỏ tàu ngầm dưới nước các tấm kim loại nào sau đây?",
                options=[
                    r"Đồng ($\text{Cu}$).",
                    r"Kẽm ($\text{Zn}$).",
                    r"Chì ($\text{Pb}$).",
                    r"Bạc ($\text{Ag}$).",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Theo phương pháp bảo vệ điện hóa (dùng anode hy sinh), cần gắn vào thép một kim loại có tính khử mạnh hơn $\text{Fe}$ nhưng không tác dụng trực tiếp với nước biển là $\text{Zn}$. Khi đó $\text{Zn}$ là anode bị ăn mòn thay cho vỏ tàu bằng thép (cathode)."
                ),
            ),
            mcq(
                question=r"Hóa chất nào sau đây có thể dùng để làm mềm cả nước cứng tạm thời, nước cứng vĩnh cửu và nước cứng toàn phần?",
                options=[
                    r"$\text{NaCl}$.",
                    r"$\text{HCl}$.",
                    r"$\text{Na}_2\text{CO}_3$.",
                    r"$\text{CaSO}_4$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Ion $\text{CO}_3^{2-}$ trong $\text{Na}_2\text{CO}_3$ (hoặc $\text{PO}_4^{3-}$ trong $\text{Na}_3\text{PO}_4$) kết hợp với toàn bộ ion $\text{Ca}^{2+}$ và $\text{Mg}^{2+}$ trong mọi loại nước cứng tạo kết tủa $\text{CaCO}_3\downarrow$ và $\text{MgCO}_3\downarrow$, làm mềm nước."
                ),
            ),
            mcq(
                question=r"Nguyên tử chromium ($\text{Cr}$, $Z = 24$) là kim loại chuyển tiếp dãy thứ nhất có độ cứng cao nhất trong các kim loại. Cấu hình electron của nguyên tử $\text{Cr}$ ở trạng thái cơ bản là:",
                options=[
                    r"$[\text{Ar}]3d^4 4s^2$.",
                    r"$[\text{Ar}]3d^5 4s^1$.",
                    r"$[\text{Ar}]3d^6 4s^2$.",
                    r"$[\text{Ar}]3d^{10} 4s^1$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Ở nguyên tử $\text{Cr}$ ($Z = 24$), $1$ electron từ phân lớp $4s$ chuyển sang phân lớp $3d$ để đạt cấu hình bán bão hòa bền vững $3d^5$, nên cấu hình electron của $\text{Cr}$ là $[\text{Ar}]3d^5 4s^1$."
                ),
            ),
            mcq(
                question=r"Trong phức chất $[\text{Cu(NH}_3)_4(\text{H}_2\text{O)}_2]\text{SO}_4$, nguyên tử trung tâm và số phối trí của nguyên tử trung tâm lần lượt là:",
                options=[
                    r"$\text{Cu}^{2+}$ và số phối trí bằng $4$.",
                    r"$\text{Cu}^{2+}$ và số phối trí bằng $6$.",
                    r"$\text{Cu}^+$ và số phối trí bằng $6$.",
                    r"$\text{S}^{6+}$ và số phối trí bằng $4$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Cầu nội của phức chất là $[\text{Cu(NH}_3)_4(\text{H}_2\text{O)}_2]^{2+}$, trong đó nguyên tử trung tâm là $\text{Cu}^{2+}$ liên kết với $4$ phối tử $\text{NH}_3$ và $2$ phối tử $\text{H}_2\text{O}$ (đều là phối tử đơn càng), nên số phối trí bằng $4 + 2 = 6$ (dạng hình học bát diện)."
                ),
            ),
            mcq(
                question=(
                    r"Dẫn luồng khí $\text{CO}$ dư đi qua ống sứ đựng hỗn hợp bột gồm $\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}_2\text{O}_3$ và $\text{CuO}$ "
                    r"nung nóng ở nhiệt độ cao. Sau khi các phản ứng xảy ra hoàn toàn, hỗn hợp chất rắn còn lại trong ống sứ gồm:"
                ),
                options=[
                    r"$\text{Mg}, \text{Al}, \text{Fe}, \text{Cu}$.",
                    r"$\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}, \text{Cu}$.",
                    r"$\text{MgO}, \text{Al}, \text{Fe}, \text{Cu}$.",
                    r"$\text{MgO}, \text{Al}_2\text{O}_3, \text{FeO}, \text{Cu}$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Khí $\text{CO}$ ở nhiệt độ cao chỉ khử được oxide của các kim loại đứng sau $\text{Al}$ trong dãy hoạt động hóa học ($\text{Fe}_2\text{O}_3 \rightarrow \text{Fe}$, $\text{CuO} \rightarrow \text{Cu}$), "
                    r"không khử được $\text{MgO}$ và $\text{Al}_2\text{O}_3$. Vậy chất rắn thu được gồm $\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}$ và $\text{Cu}$."
                ),
            ),
            mcq(
                question=(
                    r"Nhỏ từ từ dung dịch $\text{NH}_3$ đến dư vào ống nghiệm đựng dung dịch $\text{CuSO}_4$. Hiện tượng quan sát được là:"
                ),
                options=[
                    r"Có kết tủa màu xanh nhạt xuất hiện và không tan khi thêm $\text{NH}_3$ dư.",
                    r"Ban đầu xuất hiện kết tủa màu xanh nhạt, sau đó kết tủa tan dần tạo dung dịch màu xanh lam thẫm.",
                    r"Dung dịch chuyển ngay sang màu vàng chanh và có khí không màu thoát ra.",
                    r"Xuất hiện kết tủa màu đỏ gạch của $\text{Cu}_2\text{O}$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Ban đầu $\text{NH}_3$ phản ứng tạo kết tủa xanh nhạt $\text{Cu(OH)}_2$: $\text{Cu}^{2+} + 2\text{NH}_3 + 2\text{H}_2\text{O} \rightarrow \text{Cu(OH)}_2\downarrow + 2\text{NH}_4^+$. "
                    r"Khi $\text{NH}_3$ dư, $\text{Cu(OH)}_2$ tan tạo phức chất tan màu xanh lam thẫm: $\text{Cu(OH)}_2 + 4\text{NH}_3 + 2\text{H}_2\text{O} \rightarrow [\text{Cu(NH}_3)_4(\text{H}_2\text{O)}_2]^{2+} + 2\text{OH}^-$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét các tính chất, hợp chất của nguyên tố nhóm $\text{IA}$, nhóm $\text{IIA}$ và hiện tượng ăn mòn kim loại trong tự nhiên."
                ),
                statements=[
                    r"Khi đốt nóng các hợp chất của sodium ($\text{Na}^+$) trên ngọn lửa đèn khí không màu thì ngọn lửa có màu vàng tươi đặc trưng, còn hợp chất của potassium ($\text{K}^+$) cho ngọn lửa màu tím.",
                    r"Để làm mềm nước cứng vĩnh cửu chứa $\text{CaCl}_2$ và $\text{MgSO}_4$, người ta chỉ cần đun sôi nước thật kĩ trước khi sử dụng.",
                    r"Trong công nghiệp, $\text{NaHCO}_3$ và $\text{Na}_2\text{CO}_3$ được sản xuất từ nguyên liệu chính là muối ăn ($\text{NaCl}$), đá vôi ($\text{CaCO}_3$) và ammonia ($\text{NH}_3$) theo phương pháp Solvay.",
                    r"Khi một vật bằng gang (hợp kim $\text{Fe}-\text{C}$) để trong không khí ẩm bị ăn mòn điện hóa, nguyên tố carbon ($\text{C}$) đóng vai trò là anode (cực âm) và bị oxi hóa.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Cation $\text{Na}^+$ cho ngọn lửa màu vàng tươi, cation $\text{K}^+$ cho ngọn lửa màu tím." "\n"
                    r"- **b) Sai**: Đun sôi chỉ làm mềm được nước cứng tạm thời (chứa $\text{HCO}_3^-$), không làm mềm được nước cứng vĩnh cửu (chứa $\text{Cl}^-, \text{SO}_4^{2-}$)." "\n"
                    r"- **c) Đúng**: Quy trình Solvay đi từ $\text{NaCl}$ bão hòa, $\text{NH}_3$ và $\text{CO}_2$ (nung từ đá vôi $\text{CaCO}_3$) để kết tinh $\text{NaHCO}_3$ rồi nhiệt phân thu $\text{Na}_2\text{CO}_3$." "\n"
                    r"- **d) Sai**: Khi gang ($\text{Fe}-\text{C}$) bị ăn mòn điện hóa trong không khí ẩm, sắt ($\text{Fe}$) đóng vai trò là **anode (cực âm)** và bị oxi hóa ($\text{Fe} \rightarrow \text{Fe}^{2+} + 2\text{e}$), còn $\text{C}$ là cathode (cực dương)."
                ),
            ),
            tf4(
                stem=(
                    r"Cho các nhận định về kim loại chuyển tiếp dãy thứ nhất, phép chuẩn độ muối sắt(II) và cấu tạo phức chất."
                ),
                statements=[
                    r"Các nguyên tố kim loại chuyển tiếp dãy thứ nhất (từ $\text{Sc}$ đến $\text{Cu}$) thường có nhiều trạng thái oxi hóa khác nhau do cả electron ở phân lớp $4s$ và phân lớp $3d$ đều có thể tham gia tạo liên kết hóa học.",
                    r"Trong thí nghiệm chuẩn độ dung dịch $\text{FeSO}_4$ bằng dung dịch $\text{KMnO}_4$ trong môi trường $\text{H}_2\text{SO}_4$ loãng, cần phải thêm chất chỉ thị phenolphthalein để xác định điểm tương đương.",
                    r"Trong phức chất $\text{K}_3[\text{Fe(CN)}_6]$, nguyên tử trung tâm là $\text{Fe}^{3+}$ có số phối trí bằng $6$ và phức chất có dạng hình học bát diện.",
                    r"Phức chất $[\text{Ag(NH}_3)_2]^+$ (trong thuốc thử Tollens) có số phối trí của nguyên tử trung tâm $\text{Ag}^+$ bằng $4$ và có dạng hình học tứ diện.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Năng lượng của các electron trên phân lớp $3d$ và $4s$ gần nhau nên các nguyên tố chuyển tiếp sử dụng cả electron $4s$ và $3d$ để tạo liên kết, dẫn đến có nhiều số oxi hóa dương." "\n"
                    r"- **b) Sai**: Trong phép chuẩn độ $\text{FeSO}_4$ bằng $\text{KMnO}_4$ trong môi trường acid, chính dung dịch $\text{KMnO}_4$ đóng vai trò tự chỉ thị (khi vừa dư $1$ giọt $\text{KMnO}_4$ thì dung dịch trong bình tam giác chuyển sang màu hồng nhạt bền khoảng $20\text{ giây}$), không dùng phenolphthalein." "\n"
                    r"- **c) Đúng**: Trong $\text{K}_3[\text{Fe(CN)}_6]$, cầu nội là $[\text{Fe(CN)}_6]^{3-}$, số oxi hóa của $\text{Fe}$ là $+3$, liên kết với $6$ phối tử $\text{CN}^-$ theo hình bát diện." "\n"
                    r"- **d) Sai**: Trong phức chất $[\text{Ag(NH}_3)_2]^+$, nguyên tử trung tâm $\text{Ag}^+$ liên kết với $2$ phối tử $\text{NH}_3$ nên có **số phối trí bằng $2$** và có **dạng hình học đường thẳng**."
                ),
            ),
            mcq(
                question=(
                    r"Hòa tan hoàn toàn $1{,}40\text{ g}$ một mẫu hợp kim sắt (chỉ chứa $\text{Fe}$ và tạp chất trơ không phản ứng) trong dung dịch "
                    r"$\text{H}_2\text{SO}_4$ loãng dư, thu được dung dịch $\text{X}$ (trong đó sắt chỉ tồn tại ở dạng $\text{Fe}^{2+}$). "
                    r"Chuẩn độ toàn bộ dung dịch $\text{X}$ cần vừa đủ $20{,}0\text{ mL}$ dung dịch $\text{KMnO}_4\text{ } 0{,}20\text{ M}$. "
                    r"Phần trăm khối lượng của $\text{Fe}$ trong mẫu hợp kim trên là:"
                ),
                options=[
                    r"$80{,}0\%$.",
                    r"$75{,}0\%$.",
                    r"$90{,}0\%$.",
                    r"$60{,}0\%$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Số mol $\text{KMnO}_4$ phản ứng: $n_{\text{KMnO}_4} = 0{,}020 \cdot 0{,}20 = 0{,}004\text{ mol}$. "
                    r"Theo phương trình chuẩn độ: $5\text{Fe}^{2+} + \text{MnO}_4^- + 8\text{H}^+ \rightarrow 5\text{Fe}^{3+} + \text{Mn}^{2+} + 4\text{H}_2\text{O}$, "
                    r"ta có $n_{\text{Fe}} = n_{\text{Fe}^{2+}} = 5n_{\text{KMnO}_4} = 5 \cdot 0{,}004 = 0{,}020\text{ mol}$. "
                    r"Khối lượng $\text{Fe}$ trong mẫu là $m_{\text{Fe}} = 0{,}020 \cdot 56 = 1{,}12\text{ g}$. "
                    r"Phần trăm khối lượng $\text{Fe}$ là $\%m_{\text{Fe}} = \dfrac{1{,}12}{1{,}40} \cdot 100\% = 80{,}0\%$."
                ),
            ),
            short(
                question=(
                    r"Một mẫu nước cứng chứa $0{,}002\text{ mol}$ $\text{Ca(HCO}_3)_2$ và $0{,}003\text{ mol}$ $\text{MgCl}_2$. "
                    r"Để làm mềm hoàn toàn mẫu nước cứng này, người ta cho vào đó lượng vừa đủ dung dịch $\text{Na}_2\text{CO}_3$. "
                    r"Tính tổng khối lượng kết tủa (theo đơn vị $\text{gam}$, làm tròn kết quả đến hai chữ số thập phân) thu được sau phản ứng."
                ),
                answer=["0,45", "0.45", "0,452", "0.452"],
                level="vandung",
                solution=(
                    r"- Khi cho $\text{Na}_2\text{CO}_3$ vừa đủ vào mẫu nước cứng: "
                    r"$\text{Ca}^{2+} + \text{CO}_3^{2-} \rightarrow \text{CaCO}_3\downarrow$ ($M = 100\text{ g/mol}$) và $\text{Mg}^{2+} + \text{CO}_3^{2-} \rightarrow \text{MgCO}_3\downarrow$ ($M = 84\text{ g/mol}$)." "\n"
                    r"- Ta có $n_{\text{CaCO}_3} = n_{\text{Ca}^{2+}} = 0{,}002\text{ mol}$ và $n_{\text{MgCO}_3} = n_{\text{Mg}^{2+}} = 0{,}003\text{ mol}$." "\n"
                    r"- Tổng khối lượng kết tủa: $m_{\downarrow} = 0{,}002 \cdot 100 + 0{,}003 \cdot 84 = 0{,}20 + 0{,}252 = 0{,}452\text{ g} \approx 0{,}45\text{ g}$."
                ),
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 7: HÓA HỌC TRONG PHÒNG CHỐNG CHÁY NỔ VÀ BẢO VỆ MÔI TRƯỜNG XANH
    # =========================================================================
    lesson(
        grade=12,
        order=7,
        code="H12-C07",
        title="Chương 7: Hóa học trong việc phòng chống cháy nổ và bảo vệ môi trường xanh",
        topic="hoa-hoc-moi-truong",
        description=(
            "Chương 7 SGK Hóa học 12 Kết nối tri thức: Tam giác cháy, chất chữa cháy và an toàn phòng chống cháy nổ; "
            "nguyên nhân và giải pháp giảm thiểu hiệu ứng nhà kính, mưa acid, suy giảm tầng ozone, phú dưỡng; nguyên tắc 3R và Hóa học xanh."
        ),
        summary=(
            r"**Phản ứng cháy** là phản ứng oxi hóa – khử tỏa nhiều nhiệt và phát sáng giữa chất cháy với chất oxi hóa (thường là oxygen không khí). "
            r"Để một đám cháy hình thành và duy trì cần đủ $3$ yếu tố tạo thành **Tam giác cháy**: **Chất cháy**, **Chất oxi hóa** (thường yêu cầu nồng độ $\text{O}_2 > 14\%$ thể tích) "
            r"và **Nguồn nhiệt** (đạt tới nhiệt độ bắt cháy / tự bốc cháy). Nguyên tắc chữa cháy là loại bỏ ít nhất một trong ba yếu tố của tam giác cháy "
            r"bằng các **chất chữa cháy phổ biến**: nước ($\text{H}_2\text{O}$ – thu nhiệt làm lạnh và tạo hơi nước cách ly $\text{O}_2$), khí $\text{CO}_2$ nén lỏng, "
            r"bột chữa cháy ($\text{NaHCO}_3$ nhiệt phân thu nhiệt và giải phóng $\text{CO}_2, \text{H}_2\text{O}$) và bọt chữa cháy; tuyệt đối không dùng nước dập đám cháy xăng dầu "
            r"hoặc đám cháy thiết bị điện đang có điện, và không dùng nước hay khí $\text{CO}_2$ dập đám cháy kim loại mạnh ($\text{Na}, \text{K}, \text{Mg}, \text{Al}$). "
            r"Trong bảo vệ môi trường, hóa học giúp giải quyết các vấn đề toàn cầu: **hiệu ứng nhà kính** (do khí $\text{CO}_2, \text{CH}_4, \text{N}_2\text{O}$), "
            r"**mưa acid** (nước mưa có $\text{pH} < 5{,}6$ do khí thải $\text{SO}_2$ và $\text{NO}_x$ chuyển hóa thành $\text{H}_2\text{SO}_4, \text{HNO}_3$), "
            r"**suy giảm tầng ozone** (do khí $\text{CFC}$ phân hủy bởi tia $\text{UV}$ tạo gốc tự do $\text{Cl}^\bullet$ phá hủy $\text{O}_3$), **hiện tượng phú dưỡng** "
            r"(dư thừa nguyên tố dinh dưỡng $\text{N}, \text{P}$ trong ao hồ) và **ô nhiễm rác thải nhựa** theo nguyên tắc **$3\text{R}$ ($\text{Reduce – Reuse – Recycle}$)** "
            r"cùng $12$ nguyên tắc của **Hóa học xanh** (tối ưu hóa **độ tiết kiệm nguyên tử** $AE$, dùng nguyên liệu tái tạo và xúc tác thân thiện môi trường)."
        ),
        objectives=[
            r"Nêu được khái niệm phản ứng cháy, phản ứng nổ (nổ vật lý, nổ hóa học, nổ bụi), điểm chớp cháy, nhiệt độ tự bốc cháy và $3$ yếu tố trong Tam giác cháy.",
            r"Giải thích được cơ chế hoạt động và phạm vi áp dụng an toàn của các chất chữa cháy phổ biến (nước $\text{H}_2\text{O}$, khí $\text{CO}_2$, bột $\text{NaHCO}_3$, bọt chữa cháy).",
            r"Trình bày được nguyên nhân hóa học, hậu quả và biện pháp giảm thiểu hiệu ứng nhà kính ($\text{CO}_2, \text{CH}_4$), mưa acid ($\text{SO}_2, \text{NO}_x$), suy giảm tầng ozone ($\text{CFC}$) và hiện tượng phú dưỡng ($\text{N}, \text{P}$).",
            r"Vận dụng được nguyên tắc $3\text{R}$ ($\text{Reduce}$ – Tiết giảm, $\text{Reuse}$ – Tái sử dụng, $\text{Recycle}$ – Tái chế) trong xử lý rác thải nhựa và bảo vệ nguồn nước.",
            r"Nêu được tư tưởng cốt lõi của Hóa học xanh và tính được độ tiết kiệm nguyên tử ($AE$) của một phản ứng hóa học.",
        ],
        formulas=[
            {
                "name": "Phản ứng nhiệt phân bột chữa cháy baking soda (NaHCO3)",
                "formula": r"$2\text{NaHCO}_3(s) \xrightarrow{t^\circ} \text{Na}_2\text{CO}_3(s) + \text{CO}_2(g) + \text{H}_2\text{O}(g)\quad (\Delta_{\text{r}}H^\circ_{298} > 0)$",
                "note": r"Phản ứng thu nhiệt giúp hạ nhiệt độ vùng cháy, đồng thời sinh ra khí $\text{CO}_2$ và hơi $\text{H}_2\text{O}$ bao phủ làm giảm nồng độ $\text{O}_2$.",
            },
            {
                "name": "Phản ứng giải thích vì sao không dùng bình chữa cháy CO2 cho đám cháy kim loại Mg",
                "formula": r"$2\text{Mg}(s) + \text{CO}_2(g) \xrightarrow{t^\circ} 2\text{MgO}(s) + \text{C}(s)$",
                "note": r"$\text{Mg}$ là chất khử mạnh tiếp tục cháy mãnh liệt trong khí $\text{CO}_2$ tỏa nhiều nhiệt và sinh ra muội than $\text{C}$ tiếp tục cháy.",
            },
            {
                "name": "Quá trình hình thành mưa acid từ khí thải SO2 và NO2 trong khí quyển",
                "formula": r"$2\text{SO}_2 + \text{O}_2 + 2\text{H}_2\text{O} \xrightarrow{\text{xt}} 2\text{H}_2\text{SO}_4$; $4\text{NO}_2 + \text{O}_2 + 2\text{H}_2\text{O} \rightarrow 4\text{HNO}_3$",
                "note": r"Làm nước mưa có $\text{pH} < 5{,}6$, ăn mòn công trình bằng đá vôi ($\text{CaCO}_3$), kim loại ($\text{Fe}$) và làm chua đất, nước.",
            },
            {
                "name": "Cơ chế gốc tự do Cl phá hủy tầng ozone (O3) bởi hợp chất CFC (như CF2Cl2)",
                "formula": r"$\text{CF}_2\text{Cl}_2 \xrightarrow{\text{UV}} \text{CF}_2\text{Cl}^\bullet + \text{Cl}^\bullet$; $\text{Cl}^\bullet + \text{O}_3 \rightarrow \text{ClO}^\bullet + \text{O}_2$; $\text{ClO}^\bullet + \text{O}^\bullet \rightarrow \text{Cl}^\bullet + \text{O}_2$",
                "note": r"Một gốc tự do $\text{Cl}^\bullet$ được tái sinh liên tục theo dây chuyền nên có thể phá hủy tới hàng trăm nghìn phân tử $\text{O}_3$.",
            },
            {
                "name": "Công thức tính độ tiết kiệm nguyên tử (Atom Economy – AE) trong Hóa học xanh",
                "formula": r"$AE = \dfrac{M_{\text{sản phẩm mong muốn}}}{\sum M_{\text{tất cả các chất phản ứng (theo hệ số cân bằng)}}} \cdot 100\%$",
                "note": r"Các phản ứng cộng và phản ứng trùng hợp không tạo sản phẩm phụ nên có độ tiết kiệm nguyên tử lý tưởng $AE = 100\%$.",
            },
        ],
        theory_sections=[
            {
                "title": "Phần 1. Hóa học về phản ứng cháy, nổ và phòng chống cháy nổ",
                "content": [
                    r"**Tam giác cháy và các thông số an toàn cháy nổ**: Một đám cháy chỉ xảy ra khi hội tụ đủ $3$ yếu tố của **Tam giác cháy**: (1) **Chất cháy** (rắn như gỗ, vải, nhựa; lỏng như xăng, dầu, cồn; khí như $\text{CH}_4, \text{C}_3\text{H}_8, \text{C}_4\text{H}_{10}, \text{H}_2, \text{CO}$), (2) **Chất oxi hóa** (thường là $\text{O}_2$ trong không khí với hàm lượng $\ge 14\%$ thể tích) và (3) **Nguồn nhiệt** (tia lửa điện, ngọn lửa trần, ma sát...). **Điểm chớp cháy** là nhiệt độ thấp nhất ở áp suất khí quyển mà tại đó chất lỏng bay hơi tạo hỗn hợp với không khí bốc cháy chớp nhoáng khi có nguồn lửa (xăng có điểm chớp cháy rất thấp khoảng $-43^\circ\text{C}$ nên cực kì dễ cháy nổ); **nhiệt độ tự bốc cháy** là nhiệt độ thấp nhất mà chất cháy tự bốc cháy trong không khí không cần nguồn lửa trực tiếp. **Phản ứng nổ** gồm nổ vật lý (nổ lốp xe, nổ nồi hơi do áp suất cao mà không có phản ứng hóa học), nổ hóa học (thuốc nổ $\text{TNT}$, pháo hoa, khí gas rò rỉ) và **nổ bụi** (các hạt bụi mịn của bột mì, bụi than, bột nhôm, mùn cưa phân tán trong không khí với nồng độ thích hợp gặp tia lửa gây nổ dữ dội do diện tích bề mặt tiếp xúc cực lớn).",
                    r"**Nguyên tắc chữa cháy và lựa chọn chất chữa cháy**: Để dập tắt đám cháy cần: hạ nhiệt độ vùng cháy xuống dưới nhiệt độ bắt cháy, cách ly chất cháy với $\text{O}_2$ hoặc làm loãng nồng độ $\text{O}_2$ xuống dưới $14\%$. **Nước ($\text{H}_2\text{O}$)** có nhiệt hóa hơi lớn dùng dập đám cháy chất rắn thông thường (gỗ, giấy, vải, than), nhưng **tuyệt đối không dùng nước** cho đám cháy xăng, dầu (vì xăng dầu nhẹ hơn nước và không tan trong nước nên nổi lên trên làm đám cháy lan rộng), đám cháy thiết bị điện đang có điện (vì nước sinh hoạt dẫn điện) và đám cháy kim loại hoạt động mạnh ($\text{Na}, \text{K}, \text{Ca}, \text{Mg}$). **Bình chữa cháy khí $\text{CO}_2$** chứa $\text{CO}_2$ hóa lỏng ở áp suất cao, khi phun ra sẽ bay hơi thu nhiệt làm lạnh đột ngột (tới $-79^\circ\text{C}$, cần cẩn thận tránh bỏng lạnh) và khí $\text{CO}_2$ nặng hơn không khí bao phủ đám cháy, thích hợp chữa đám cháy thiết bị điện, tài liệu, phòng kín, nhưng **không dùng $\text{CO}_2$ cho đám cháy kim loại kiềm, $\text{Mg}, \text{Al}$**. **Bình bột chữa cháy** (như bột $\text{BC}$ chứa $\text{NaHCO}_3$ hoặc bột $\text{ABC}$ chứa $\text{NH}_4\text{H}_2\text{PO}_4$) và **bọt chữa cháy** dùng hiệu quả cho đám cháy xăng dầu, khí cháy, chất rắn.",
                ],
            },
            {
                "title": "Phần 2. Hóa học với bảo vệ môi trường và Hóa học xanh",
                "content": [
                    r"**Các vấn đề môi trường khí quyển và nguồn nước**: (1) **Hiệu ứng nhà kính và biến đổi khí hậu**: Các khí nhà kính chủ yếu là $\text{CO}_2$ (từ đốt nhiên liệu hóa thạch than, dầu mỏ, khí thiên nhiên và phá rừng), $\text{CH}_4$ (từ chăn nuôi, bãi rác, ruộng lúa ngập nước), $\text{N}_2\text{O}$, hơi nước hấp thụ bức xạ hồng ngoại giữ nhiệt cho Trái Đất; nồng độ tăng quá mức gây nóng lên toàn cầu. (2) **Mưa acid**: Nước mưa bình thường hòa tan $\text{CO}_2$ có $\text{pH} \approx 5{,}6$; khi khí thải công nghiệp và giao thông chứa $\text{SO}_2$ và $\text{NO}_x$ ($\text{NO}, \text{NO}_2$) bị oxi hóa trong khí quyển tạo $\text{H}_2\text{SO}_4$ và $\text{HNO}_3$ làm nước mưa có $\text{pH} < 5{,}6$ gọi là mưa acid. Biện pháp xử lý khí $\text{SO}_2$ trong ống khói nhà máy nhiệt điện là phun dung dịch sữa vôi $\text{Ca(OH)}_2$ hoặc bột đá vôi $\text{CaCO}_3$ ướt tạo thạch cao. (3) **Suy giảm tầng ozone**: Tầng $\text{O}_3$ ở tầng bình lưu bảo vệ sinh vật khỏi tia cực tím ($\text{UV}$); các hợp chất **$\text{CFC}$** (chlorofluorocarbon như $\text{CF}_2\text{Cl}_2, \text{CFCl}_3$ trước đây dùng trong tủ lạnh, điều hòa) phát thải lên tầng bình lưu tạo gốc $\text{Cl}^\bullet$ phá hủy $\text{O}_3$ (hiện đã được thay thế bằng $\text{HFC}$, hydrocarbon theo Nghị định thư Montreal). (4) **Hiện tượng phú dưỡng (Eutrophication)**: Khi nước thải sinh hoạt, nông nghiệp chứa dư thừa các hợp chất của **nitrogen ($\text{NO}_3^-, \text{NH}_4^+$)** và **phosphorus ($\text{PO}_4^{3-}$)** chảy vào ao hồ tù đọng làm tảo và rong rêu phát triển bùng nổ (nước hồ chuyển màu xanh lục, có váng), khi tảo chết bị vi khuẩn phân hủy tiêu thụ cạn kiệt $\text{O}_2$ hòa tan trong nước khiến tôm cá chết hàng loạt.",
                    r"**Nguyên tắc 3R và Hóa học xanh**: Để giảm thiểu ô nhiễm rác thải nhựa, cần thực hiện nguyên tắc **$3\text{R}$**: **Reduce (Tiết giảm)** – hạn chế sử dụng túi nilon và đồ nhựa dùng một lần; **Reuse (Tái sử dụng)** – dùng lại nhiều lần các vật dụng còn tốt; **Recycle (Tái chế)** – phân loại nhựa nhiệt dẻo ($\text{PET}, \text{HDPE}, \text{PP}$) để tái chế thành sản phẩm mới, kết hợp sử dụng polymer phân hủy sinh học (như $\text{PLA}$ từ tinh bột ngô). Trong sản xuất hóa chất, **Hóa học xanh (Green Chemistry)** hướng tới thiết kế quy trình giảm thiểu hoặc loại bỏ chất độc hại ngay từ nguồn thông qua $12$ nguyên tắc, tiêu biểu là: ngăn ngừa chất thải ngay từ đầu, tối đa hóa **độ tiết kiệm nguyên tử ($AE$)**, sử dụng nguyên liệu tái tạo (sinh khối thay dầu mỏ), dùng chất xúc tác chọn lọc thay vì tác nhân phản ứng dùng lượng dư, sử dụng dung môi an toàn (như nước, $\text{CO}_2$ siêu tới hạn) và thiết kế sản phẩm có khả năng tự phân hủy sau khi sử dụng.",
                ],
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Giải thích tình huống chữa cháy an toàn trong thực tiễn",
                "problem": (
                    r"Giải thích vì sao: (a) Khi chảo dầu ăn trên bếp bị bốc cháy, tuyệt đối không được đổ nước vào chảo mà nên đậy kín nắp chảo hoặc phủ khăn ướt lên trên (đồng thời tắt bếp)? "
                    r"(b) Không được dùng bình chữa cháy khí $\text{CO}_2$ để dập đám cháy kim loại magnesium ($\text{Mg}$)? "
                ),
                "solution": (
                    r"- **(a)** Dầu ăn nhẹ hơn nước ($D \approx 0{,}9\text{ g/cm}^3$) và không tan trong nước. Nếu đổ nước vào chảo dầu đang cháy ở nhiệt độ rất cao ($> 300^\circ\text{C}$), nước chìm xuống đáy chảo hóa hơi đột ngột làm dầu đang cháy bắn tung tóe ra xung quanh và nổi lên trên mặt nước khiến đám cháy bùng phát dữ dội hơn. Khi đậy kín nắp chảo hoặc phủ chăn/khăn ướt và tắt bếp, ta đã **cách ly dầu cháy với oxygen không khí** và cắt nguồn nhiệt, đám cháy sẽ tắt ngay." "\n"
                    r"- **(b)** Kim loại $\text{Mg}$ có tính khử rất mạnh, ở nhiệt độ cao $\text{Mg}$ tiếp tục cháy mãnh liệt trong khí $\text{CO}_2$ theo phương trình $2\text{Mg} + \text{CO}_2 \xrightarrow{t^\circ} 2\text{MgO} + \text{C}$ (muội than $\text{C}$ lại tiếp tục cháy), làm đám cháy càng nguy hiểm hơn. Đám cháy $\text{Mg}$ phải dập bằng cát khô hoặc bột chữa cháy chuyên dụng lớp $\text{D}$ (như bột $\text{NaCl}$ khô, bột graphite)."
                ),
            },
            {
                "title": "Ví dụ 2: Tính độ tiết kiệm nguyên tử (Atom Economy) theo Hóa học xanh",
                "problem": (
                    r"Xét hai phương pháp điều chế $\text{ethylene oxide}$ ($\text{C}_2\text{H}_4\text{O}$, $M = 44\text{ g/mol}$) trong công nghiệp: "
                    r"Phương pháp 1 (cổ điển): $\text{C}_2\text{H}_4 + \text{Cl}_2 + \text{Ca(OH)}_2 \rightarrow \text{C}_2\text{H}_4\text{O} + \text{CaCl}_2 + \text{H}_2\text{O}$. "
                    r"Phương pháp 2 (Hóa học xanh – oxi hóa trực tiếp có xúc tác $\text{Ag}$): $\text{C}_2\text{H}_4 + 0{,}5\text{O}_2 \xrightarrow{\text{Ag}, t^\circ} \text{C}_2\text{H}_4\text{O}$. "
                    r"Tính độ tiết kiệm nguyên tử $AE$ của mỗi phương pháp và cho biết phương pháp nào ưu việt hơn."
                ),
                "solution": (
                    r"- **Phương pháp 1**: Tổng khối lượng mol các chất phản ứng là $M_{\text{C}_2\text{H}_4} + M_{\text{Cl}_2} + M_{\text{Ca(OH)}_2} = 28 + 71 + 74 = 173\text{ g/mol}$. "
                    r"Độ tiết kiệm nguyên tử là $AE_1 = \dfrac{44}{173} \cdot 100\% \approx 25{,}4\%$ (tạo nhiều chất thải phụ $\text{CaCl}_2$). " "\n"
                    r"- **Phương pháp 2**: Toàn bộ nguyên tử của các chất tham gia phản ứng ($\text{C}_2\text{H}_4$ và $0{,}5\text{O}_2$, tổng khối lượng mol $28 + 16 = 44\text{ g/mol}$) đều đi vào sản phẩm mong muốn $\text{C}_2\text{H}_4\text{O}$, nên $AE_2 = \dfrac{44}{44} \cdot 100\% = 100\%$. " "\n"
                    r"- Vậy phương pháp 2 tuân thủ nguyên tắc Hóa học xanh ưu việt hơn hẳn vì có $AE = 100\%$ và không tạo chất thải phụ."
                ),
            },
        ],
        key_takeaways=[
            r"Tam giác cháy gồm $3$ yếu tố: **Chất cháy + Chất oxi hóa ($\text{O}_2$) + Nguồn nhiệt**; muốn dập tắt đám cháy cần loại bỏ ít nhất một trong ba yếu tố này.",
            r"Tuyệt đối không dùng nước dập đám cháy xăng dầu, thiết bị điện đang có điện và kim loại mạnh ($\text{Na}, \text{K}, \text{Mg}$); không dùng bình $\text{CO}_2$ dập đám cháy kim loại $\text{Mg}, \text{Na}, \text{K}$.",
            r"Mưa acid ($\text{pH} < 5{,}6$) do khí $\text{SO}_2$ và $\text{NO}_x$; hiệu ứng nhà kính chủ yếu do $\text{CO}_2, \text{CH}_4$; suy giảm tầng ozone do $\text{CFC}$; hiện tượng phú dưỡng nguồn nước do dư thừa dinh dưỡng $\text{N}, \text{P}$ ($\text{NO}_3^-, \text{NH}_4^+, \text{PO}_4^{3-}$).",
            r"Nguyên tắc $3\text{R}$ trong quản lý chất thải: **Reduce (Tiết giảm) – Reuse (Tái sử dụng) – Recycle (Tái chế)**; độ tiết kiệm nguyên tử trong Hóa học xanh: $AE = \dfrac{M_{\text{sản phẩm mong muốn}}}{\sum M_{\text{chất phản ứng}}} \cdot 100\%$.",
        ],
        questions=[
            mcq(
                question=r"Ba yếu tố cần thiết tạo thành 'Tam giác cháy' để một đám cháy có thể phát sinh và duy trì là:",
                options=[
                    r"Chất cháy, chất oxi hóa và nguồn nhiệt.",
                    r"Chất cháy, chất xúc tác và khí nitrogen ($\text{N}_2$).",
                    r"Nguồn nhiệt, khí carbon dioxide ($\text{CO}_2$) và hơi nước.",
                    r"Chất oxi hóa, ánh sáng mặt trời và áp suất cao.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Tam giác cháy gồm $3$ yếu tố không thể thiếu: **Chất cháy** (nhiên liệu), **Chất oxi hóa** (thường là oxygen không khí) và **Nguồn nhiệt** (đạt tới nhiệt độ bắt cháy)."
                ),
            ),
            mcq(
                question=r"Hai tác nhân khí thải ô nhiễm chính gây ra hiện tượng mưa acid ($\text{pH} < 5{,}6$) trong khí quyển là:",
                options=[
                    r"$\text{CO}_2$ và $\text{CH}_4$.",
                    r"$\text{SO}_2$ và $\text{NO}_x$ ($\text{NO}, \text{NO}_2$).",
                    r"$\text{CO}$ và $\text{NH}_3$.",
                    r"$\text{CFC}$ và $\text{H}_2\text{S}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Khí $\text{SO}_2$ và các oxide của nitrogen $\text{NO}_x$ ($\text{NO}, \text{NO}_2$) sinh ra từ việc đốt nhiên liệu hóa thạch bị oxi hóa trong khí quyển tạo $\text{H}_2\text{SO}_4$ và $\text{HNO}_3$ hòa tan vào nước mưa gây mưa acid."
                ),
            ),
            mcq(
                question=r"Hợp chất nào sau đây khi phát thải vào khí quyển là nguyên nhân chính gây suy giảm tầng ozone ($\text{O}_3$) ở tầng bình lưu?",
                options=[
                    r"Hợp chất $\text{CFC}$ (chlorofluorocarbon).",
                    r"Khí methane ($\text{CH}_4$).",
                    r"Khí sulfur dioxide ($\text{SO}_2$).",
                    r"Khí carbon monoxide ($\text{CO}$).",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Các hợp chất $\text{CFC}$ (như $\text{CF}_2\text{Cl}_2, \text{CFCl}_3$) khi lên tầng bình lưu bị tia cực tím ($\text{UV}$) phân cắt tạo gốc tự do $\text{Cl}^\bullet$ phá hủy dây chuyền hàng trăm nghìn phân tử $\text{O}_3$."
                ),
            ),
            mcq(
                question=r"Trong nguyên tắc $3\text{R}$ để giảm thiểu ô nhiễm rác thải nhựa và bảo vệ môi trường, ba chữ $\text{R}$ viết tắt của các từ tiếng Anh nào sau đây?",
                options=[
                    r"$\text{Reduce}$ (Tiết giảm) – $\text{Reuse}$ (Tái sử dụng) – $\text{Recycle}$ (Tái chế).",
                    r"$\text{Remove}$ (Loại bỏ) – $\text{React}$ (Phản ứng) – $\text{Restore}$ (Khôi phục).",
                    r"$\text{Reduce}$ (Tiết giảm) – $\text{Replace}$ (Thay thế) – $\text{Recover}$ (Thu hồi).",
                    r"$\text{Reuse}$ (Tái sử dụng) – $\text{Refill}$ (Làm đầy) – $\text{Repair}$ (Sửa chữa).",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Nguyên tắc $3\text{R}$ gồm: **Reduce** (Tiết giảm sử dụng), **Reuse** (Tái sử dụng nhiều lần) và **Recycle** (Tái chế thành nguyên liệu/sản phẩm mới)."
                ),
            ),
            mcq(
                question=r"Khi xảy ra đám cháy do xăng, dầu bị tràn ra sàn, biện pháp xử lý nào sau đây là SAI và gây nguy hiểm?",
                options=[
                    r"Dùng bình bột chữa cháy ($\text{NaHCO}_3$) phun trực tiếp vào đám cháy.",
                    r"Dùng bọt chữa cháy hoặc cát khô phủ kín lên bề mặt xăng, dầu đang cháy.",
                    r"Dùng chăn chiên thấm đẫm nước chụp kín lên đám cháy nhỏ.",
                    r"Dùng vòi nước phun trực tiếp vào đám cháy xăng, dầu.",
                ],
                answer="D",
                level="hieu",
                solution=(
                    r"Xăng, dầu nhẹ hơn nước và không tan trong nước nên khi phun nước vào, xăng dầu nổi lên trên mặt nước và chảy tràn ra diện rộng làm đám cháy lan nhanh hơn."
                ),
            ),
            mcq(
                question=r"Hiện tượng phú dưỡng hóa ở các ao, hồ tù đọng (làm tảo nở hoa, nước chuyển màu xanh đen, cá tôm chết ngạt vì thiếu $\text{O}_2$) xảy ra do nước thải chứa dư thừa các ion dinh dưỡng của hai nguyên tố nào?",
                options=[
                    r"Nitrogen ($\text{N}$) và Phosphorus ($\text{P}$).",
                    r"Calcium ($\text{Ca}$) và Magnesium ($\text{Mg}$).",
                    r"Iron ($\text{Fe}$) và Copper ($\text{Cu}$).",
                    r"Sodium ($\text{Na}$) và Chlorine ($\text{Cl}$).",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Hiện tượng phú dưỡng xảy ra do dư thừa chất dinh dưỡng chứa nguyên tố $\text{N}$ ($\text{NO}_3^-, \text{NH}_4^+$) và $\text{P}$ ($\text{PO}_4^{3-}$) từ phân bón hóa học dư thừa, chất giặt rửa và nước thải sinh hoạt chưa qua xử lý."
                ),
            ),
            tf4(
                stem=(
                    r"Xét nguyên tắc hoạt động và quy tắc an toàn khi sử dụng các phương tiện chữa cháy phổ biến trong phòng thí nghiệm và gia đình."
                ),
                statements=[
                    r"Bột chữa cháy chứa $\text{NaHCO}_3$ khi gặp nhiệt độ cao sẽ bị nhiệt phân theo phản ứng thu nhiệt $2\text{NaHCO}_3 \xrightarrow{t^\circ} \text{Na}_2\text{CO}_3 + \text{CO}_2 + \text{H}_2\text{O}$, vừa làm giảm nhiệt độ vùng cháy vừa tạo khí $\text{CO}_2$ bao phủ đám cháy.",
                    r"Có thể dùng bình chữa cháy khí $\text{CO}_2$ để dập tắt đám cháy của kim loại magnesium ($\text{Mg}$) hoặc sodium ($\text{Na}$) trong phòng thí nghiệm.",
                    r"Khi sử dụng bình chữa cháy khí $\text{CO}_2$ nén lỏng, tuyệt đối không được cầm tay trần trực tiếp vào loa phun vì $\text{CO}_2$ lỏng bay hơi thu nhiệt mạnh làm nhiệt độ hạ xuống khoảng $-79^\circ\text{C}$ gây bỏng lạnh.",
                    r"Khi phát hiện đám cháy ở các thiết bị điện đang hoạt động, việc đầu tiên cần làm là phun ngay nước sinh hoạt vào thiết bị điện để làm nguội.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: Phản ứng nhiệt phân $\text{NaHCO}_3$ thu nhiệt làm mát vùng cháy và sinh ra $\text{CO}_2, \text{H}_2\text{O}$ làm loãng nồng độ $\text{O}_2$." "\n"
                    r"- **b) Sai**: Kim loại hoạt động mạnh như $\text{Mg}, \text{Na}$ khử mạnh khí $\text{CO}_2$ ở nhiệt độ cao ($2\text{Mg} + \text{CO}_2 \xrightarrow{t^\circ} 2\text{MgO} + \text{C}$) làm đám cháy bùng nổ mạnh hơn." "\n"
                    r"- **c) Đúng**: Sự giãn nở và hóa hơi đoạn nhiệt của $\text{CO}_2$ lỏng ở đầu loa phun làm nhiệt độ giảm sâu tới $-79^\circ\text{C}$ (tạo tuyết $\text{CO}_2$ rắn), dễ gây bỏng lạnh nếu chạm tay trần vào loa phun." "\n"
                    r"- **d) Sai**: Khi cháy thiết bị điện, phải **ngắt ngay cầu dao / nguồn điện** trước rồi dùng bình chữa cháy khí $\text{CO}_2$ hoặc bình bột; tuyệt đối không phun nước khi chưa cắt điện vì nước sinh hoạt dẫn điện gây điện giật nguy hiểm."
                ),
            ),
            tf4(
                stem=(
                    r"Cho các nhận định về nguyên nhân hóa học của ô nhiễm môi trường và giải pháp theo định hướng Hóa học xanh."
                ),
                statements=[
                    r"Để xử lý khí thải $\text{SO}_2$ từ các nhà máy nhiệt điện đốt than trước khi thải ra môi trường, người ta thường dẫn khí thải qua hệ thống phun dung dịch sữa vôi $\text{Ca(OH)}_2$ hoặc huyền phù đá vôi $\text{CaCO}_3$.",
                    r"Nước mưa tự nhiên ở những vùng không khí hoàn toàn trong sạch, không bị ô nhiễm luôn có giá trị $\text{pH} = 7{,}0$.",
                    r"Trong Hóa học xanh, các phản ứng hóa học có độ tiết kiệm nguyên tử ($AE$) càng gần $100\%$ thì lượng chất thải phụ sinh ra càng ít và hiệu quả sử dụng nguyên liệu càng cao.",
                    r"Việc thay thế xăng khoáng thông thường bằng xăng sinh học $\text{E5}$ (chứa $5\%$ thể tích $\text{ethanol}$ sản xuất từ tinh bột sắn, ngô) làm tăng lượng phát thải khí $\text{SO}_2$ gây mưa acid.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"- **a) Đúng**: $\text{SO}_2$ là acidic oxide tác dụng với $\text{Ca(OH)}_2$ hoặc $\text{CaCO}_3 + \text{O}_2$ tạo thạch cao ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$), giúp loại bỏ trên $90\%$ lượng $\text{SO}_2$ trong khí thải." "\n"
                    r"- **b) Sai**: Ngay cả ở nơi không khí sạch, nước mưa vẫn hòa tan một lượng khí $\text{CO}_2$ có sẵn trong khí quyển tạo $\text{H}_2\text{CO}_3$ yếu nên có $\text{pH} \approx 5{,}6$ (chỉ khi $\text{pH} < 5{,}6$ mới gọi là mưa acid)." "\n"
                    r"- **c) Đúng**: Độ tiết kiệm nguyên tử $AE$ cho biết tỉ lệ phần trăm khối lượng nguyên tử của các chất phản ứng chuyển vào sản phẩm mong muốn; $AE = 100\%$ nghĩa là không có sản phẩm phụ." "\n"
                    r"- **d) Sai**: $\text{Ethanol}$ ($\text{C}_2\text{H}_5\text{OH}$) sinh học không chứa lưu huỳnh ($\text{S}$) và có nguồn gốc từ sinh khối tái tạo nên việc dùng xăng $\text{E5}$ giúp giảm phát thải khí độc và giảm phụ thuộc nhiên liệu hóa thạch."
                ),
            ),
            mcq(
                question=(
                    r"Một nhà máy nhiệt điện đốt $100\text{ tấn}$ than đá mỗi ngày, biết trong than đá chứa $1{,}6\%$ lưu huỳnh ($\text{S}$, $M = 32\text{ g/mol}$) về khối lượng "
                    r"và toàn bộ lưu huỳnh khi cháy đều chuyển hết thành khí $\text{SO}_2$. Để hấp thụ hết $90\%$ lượng khí $\text{SO}_2$ sinh ra trong một ngày "
                    r"theo phản ứng $\text{SO}_2 + \text{Ca(OH)}_2 \rightarrow \text{CaSO}_3 + \text{H}_2\text{O}$, khối lượng $\text{Ca(OH)}_2$ ($M = 74\text{ g/mol}$) tối thiểu cần dùng mỗi ngày là:"
                ),
                options=[
                    r"$3{,}33\text{ tấn}$.",
                    r"$3{,}70\text{ tấn}$.",
                    r"$1{,}665\text{ tấn}$.",
                    r"$2{,}88\text{ tấn}$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Khối lượng lưu huỳnh ($\text{S}$) có trong $100\text{ tấn}$ than là: $m_{\text{S}} = 100 \cdot 1{,}6\% = 1{,}6\text{ tấn}$. "
                    r"Số mol $\text{S}$ (tính theo $\text{Mmol}$ hay $10^6\text{ mol}$): $n_{\text{SO}_2} = n_{\text{S}} = \dfrac{1{,}6}{32} = 0{,}05\text{ Mmol}$. "
                    r"Lượng $\text{SO}_2$ cần hấp thụ ($90\%$) là: $n_{\text{SO}_2\text{ hấp thụ}} = 0{,}05 \cdot 0{,}90 = 0{,}045\text{ Mmol}$. "
                    r"Theo phương trình: $n_{\text{Ca(OH)}_2} = n_{\text{SO}_2\text{ hấp thụ}} = 0{,}045\text{ Mmol} \Rightarrow m_{\text{Ca(OH)}_2} = 0{,}045 \cdot 74 = 3{,}33\text{ tấn}$."
                ),
            ),
            short(
                question=(
                    r"Trong công nghiệp, $\text{ethanol}$ ($\text{C}_2\text{H}_5\text{OH}$, $M = 46\text{ g/mol}$) có thể được sản xuất bằng phương pháp lên men $\text{glucose}$ "
                    r"($\text{C}_6\text{H}_{12}\text{O}_6$, $M = 180\text{ g/mol}$) theo phương trình hóa học: $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$. "
                    r"Tính độ tiết kiệm nguyên tử ($AE$, theo đơn vị $\%$, làm tròn kết quả đến hàng phần mười) của quá trình điều chế $\text{ethanol}$ theo phản ứng trên."
                ),
                answer=["51,1", "51.1"],
                level="vandung",
                solution=(
                    r"- Trong phương trình $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2$, sản phẩm mong muốn là $2\text{C}_2\text{H}_5\text{OH}$ có tổng khối lượng mol là $2 \cdot 46 = 92\text{ g/mol}$." "\n"
                    r"- Tổng khối lượng mol chất phản ứng ($\text{C}_6\text{H}_{12}\text{O}_6$) là $180\text{ g/mol}$." "\n"
                    r"- Độ tiết kiệm nguyên tử của phản ứng là: $AE = \dfrac{92}{180} \cdot 100\% \approx 51{,}1\%$."
                ),
            ),
        ],
    ),
]

GRADE = 12
LESSONS = LESSONS_GRADE_12
