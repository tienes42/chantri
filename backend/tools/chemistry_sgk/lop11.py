from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_11: list[dict[str, Any]] = [
    # =========================================================================
    # CHƯƠNG 1: TỐC ĐỘ PHẢN ỨNG HÓA HỌC VÀ HỆ SỐ NHIỆT ĐỘ VAN'T HOFF
    # =========================================================================
    lesson(
        grade=11,
        order=1,
        code="H11-C01",
        title="Chương 1: Tốc độ phản ứng hóa học và hệ số nhiệt độ Van't Hoff",
        topic="toc-do-phan-ung",
        description="Khái niệm tốc độ phản ứng hóa học, tốc độ trung bình, định luật tác dụng khối lượng, các yếu tố ảnh hưởng đến tốc độ phản ứng, năng lượng hoạt hóa và quy tắc nhiệt độ Van't Hoff.",
        summary=(
            r"Chương học trình bày khái niệm tốc độ phản ứng hóa học, cách tính tốc độ trung bình của phản ứng "
            r"$\overline{v} = \pm \dfrac{\Delta C}{\Delta t}$, biểu thức định luật tác dụng khối lượng "
            r"$v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$ cho phản ứng đơn giản, vai trò của năng lượng hoạt hóa $E_{\text{a}}$ "
            r"và định lượng ảnh hưởng của nhiệt độ qua quy tắc Van't Hoff $v_2 = v_1 \cdot \gamma^{\frac{T_2 - T_1}{10}}$ "
            r"cùng các yếu tố nồng độ, áp suất, diện tích bề mặt tiếp xúc và chất xúc tác."
        ),
        objectives=[
            r"Trình bày được khái niệm tốc độ phản ứng hóa học và viết được công thức tính tốc độ trung bình $\overline{v}$ của phản ứng theo sự biến thiên nồng độ $\Delta C$ trong khoảng thời gian $\Delta t$.",
            r"Phát biểu và vận dụng được định luật tác dụng khối lượng $v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$ cho các phản ứng đơn giản và giải thích được ý nghĩa của hằng số tốc độ phản ứng $k$.",
            r"Giải thích được ảnh hưởng của 5 yếu tố: nồng độ, áp suất, diện tích bề mặt tiếp xúc, nhiệt độ và chất xúc tác đến tốc độ phản ứng dựa trên tần số va chạm hiệu quả và năng lượng hoạt hóa $E_{\text{a}}$.",
            r"Vận dụng thành thạo công thức hệ số nhiệt độ Van't Hoff $v_2 = v_1 \cdot \gamma^{\frac{T_2 - T_1}{10}}$ để tính độ thay đổi tốc độ và thời gian thực hiện phản ứng.",
        ],
        formulas=[
            {
                "name": "Tốc độ trung bình của phản ứng tổng quát",
                "formula": r"$\text{aA} + \text{bB} \rightarrow \text{cC} + \text{dD}: \quad \overline{v} = -\dfrac{1}{a}\dfrac{\Delta C_{\text{A}}}{\Delta t} = -\dfrac{1}{b}\dfrac{\Delta C_{\text{B}}}{\Delta t} = +\dfrac{1}{c}\dfrac{\Delta C_{\text{C}}}{\Delta t} = +\dfrac{1}{d}\dfrac{\Delta C_{\text{D}}}{\Delta t}$",
                "note": r"Đơn vị thường dùng là $\text{mol/(L}\cdot\text{s)}$ hay $\text{M/s}$, $\text{M/min}$; dấu $-$ đặt trước biến thiên nồng độ chất tham gia để $\overline{v} > 0$.",
            },
            {
                "name": "Định luật tác dụng khối lượng (Guldberg – Waage)",
                "formula": r"$v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$",
                "note": r"Áp dụng cho phản ứng đơn giản; $k$ là hằng số tốc độ phản ứng (chỉ phụ thuộc vào bản chất chất phản ứng và nhiệt độ); không đưa nồng độ chất rắn nguyên chất vào biểu thức $v$.",
            },
            {
                "name": "Quy tắc nhiệt độ Van't Hoff",
                "formula": r"$\dfrac{v_2}{v_1} = \dfrac{k_2}{k_1} = \gamma^{\frac{T_2 - T_1}{10}}$",
                "note": r"$\gamma$ là hệ số nhiệt độ Van't Hoff (thường $\gamma \in [2; 4]$ khi nhiệt độ tăng thêm $10^\circ\text{C}$).",
            },
            {
                "name": "Liên hệ giữa thời gian phản ứng và tốc độ theo quy tắc Van't Hoff",
                "formula": r"$\dfrac{t_1}{t_2} = \dfrac{v_2}{v_1} = \gamma^{\frac{T_2 - T_1}{10}}$",
                "note": r"Thời gian thực hiện phản ứng tỉ lệ nghịch với tốc độ phản ứng ở cùng lượng chất phản ứng.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Khái niệm tốc độ phản ứng và tốc độ trung bình",
                "content": (
                    r"Tốc độ phản ứng hóa học là đại lượng đặc trưng cho sự biến thiên nồng độ của một trong các chất phản ứng "
                    r"hoặc sản phẩm trong một đơn vị thời gian. Xét phản ứng tổng quát $\text{aA} + \text{bB} \rightarrow \text{cC} + \text{dD}$, "
                    r"nếu trong khoảng thời gian $\Delta t = t_2 - t_1$, nồng độ chất tham gia $\text{A}$ giảm từ $C_1$ xuống $C_2$ "
                    r"($\Delta C_{\text{A}} = C_2 - C_1 < 0$) và nồng độ sản phẩm $\text{C}$ tăng từ $C'_1$ lên $C'_2$ "
                    r"($\Delta C_{\text{C}} = C'_2 - C'_1 > 0$), thì tốc độ trung bình của phản ứng được tính bằng công thức "
                    r"$\overline{v} = -\dfrac{1}{a}\dfrac{\Delta C_{\text{A}}}{\Delta t} = +\dfrac{1}{c}\dfrac{\Delta C_{\text{C}}}{\Delta t}$."
                ),
            },
            {
                "title": "2. Định luật tác dụng khối lượng và hằng số tốc độ",
                "content": (
                    r"Đối với một phản ứng đơn giản (diễn ra qua một giai đoạn duy nhất) có dạng $\text{aA} + \text{bB} \rightarrow \text{sản phẩm}$, "
                    r"tốc độ tức thời của phản ứng tỉ lệ thuận với tích nồng độ các chất tham gia với số mũ thích hợp: "
                    r"$v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$. Hệ số $k$ được gọi là hằng số tốc độ phản ứng; khi $C_{\text{A}} = C_{\text{B}} = 1\text{ M}$ "
                    r"thì $v = k$, nên $k$ còn gọi là tốc độ riêng của phản ứng. Lưu ý rằng chất rắn nguyên chất $\text{(s)}$ không xuất hiện trong biểu thức tốc độ."
                ),
            },
            {
                "title": "3. Các yếu tố ảnh hưởng đến tốc độ phản ứng và năng lượng hoạt hóa",
                "content": (
                    r"Để phản ứng hóa học xảy ra, các hạt chất phản ứng phải va chạm hiệu quả với nhau và phải có năng lượng tối thiểu "
                    r"vượt qua rào cản năng lượng hoạt hóa $E_{\text{a}}$. Khi tăng nồng độ chất tan, tăng áp suất chất khí (nén giảm thể tích) "
                    r"hoặc tăng diện tích bề mặt tiếp xúc của chất rắn (nghiền nhỏ, đập vụn), tần số va chạm hiệu quả tăng lên nên tốc độ phản ứng tăng. "
                    r"Khi tăng nhiệt độ, cả tốc độ chuyển động của các hạt và tỉ lệ số hạt có năng lượng lớn hơn hoặc bằng $E_{\text{a}}$ đều tăng mạnh. "
                    r"Chất xúc tác làm tăng tốc độ phản ứng bằng cách hướng phản ứng đi theo con đường mới có năng lượng hoạt hóa $E_{\text{a}}$ thấp hơn, "
                    r"nhưng bản thân chất xúc tác không bị tiêu hao sau khi phản ứng kết thúc."
                ),
            },
            {
                "title": "4. Quy tắc nhiệt độ Van't Hoff",
                "content": (
                    r"Theo nhà bác học Van't Hoff, khi nhiệt độ tăng thêm $10^\circ\text{C}$ thì tốc độ của phần lớn các phản ứng hóa học "
                    r"tăng từ $2$ đến $4$ lần. Giá trị $\gamma = 2 \div 4$ được gọi là hệ số nhiệt độ Van't Hoff: "
                    r"$v_2 = v_1 \cdot \gamma^{\frac{T_2 - T_1}{10}}$. Ngược lại, việc bảo quản thực phẩm trong tủ lạnh là ứng dụng "
                    r"hạ thấp nhiệt độ để làm chậm tốc độ các phản ứng oxi hóa và phân hủy sinh hóa."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Tính tốc độ trung bình của phản ứng phân hủy $\text{N}_2\text{O}_5$",
                "problem": (
                    r"Cho phản ứng phân hủy $\text{N}_2\text{O}_5$ trong dung môi $\text{CCl}_4$ ở $45^\circ\text{C}$: "
                    r"$2\text{N}_2\text{O}_5\text{(g)} \rightarrow 4\text{NO}_2\text{(g)} + \text{O}_2\text{(g)}$. "
                    r"Ban đầu nồng độ của $\text{N}_2\text{O}_5$ là $2,33\text{ M}$, sau $184\text{ s}$ nồng độ của $\text{N}_2\text{O}_5$ còn lại là $2,08\text{ M}$. "
                    r"Tính tốc độ trung bình của phản ứng theo $\text{N}_2\text{O}_5$ trong khoảng thời gian trên."
                ),
                "solution": (
                    r"Độ biến thiên nồng độ của $\text{N}_2\text{O}_5$ là $\Delta C_{\text{N}_2\text{O}_5} = 2,08 - 2,33 = -0,25\text{ M}$. "
                    r"Áp dụng công thức tính tốc độ trung bình của phản ứng: "
                    r"$\overline{v} = -\dfrac{1}{2} \cdot \dfrac{\Delta C_{\text{N}_2\text{O}_5}}{\Delta t} = -\dfrac{1}{2} \cdot \dfrac{-0,25}{184} \approx 6,79 \cdot 10^{-4}\text{ M/s}$."
                ),
            },
            {
                "title": r"Ví dụ 2: Vận dụng định luật tác dụng khối lượng khi nén khí",
                "problem": (
                    r"Xét phản ứng đơn giản xảy ra trong bình kín: $2\text{NO(g)} + \text{O}_2\text{(g)} \rightarrow 2\text{NO}_2\text{(g)}$. "
                    r"a) Viết biểu thức tốc độ tức thời của phản ứng. "
                    r"b) Nếu giữ nguyên nhiệt độ và nén bình để áp suất chung của hệ tăng lên gấp $3$ lần thì tốc độ phản ứng thay đổi như thế nào?"
                ),
                "solution": (
                    r"a) Biểu thức tốc độ tức thời theo định luật tác dụng khối lượng là $v = k \cdot C_{\text{NO}}^2 \cdot C_{\text{O}_2}$. "
                    r"b) Khi nén bình ở nhiệt độ không đổi để áp suất tăng gấp $3$ lần (thể tích bình giảm $3$ lần), nồng độ mol của cả $\text{NO}$ và $\text{O}_2$ "
                    r"đều tăng gấp $3$ lần: $C'_{\text{NO}} = 3C_{\text{NO}}$ và $C'_{\text{O}_2} = 3C_{\text{O}_2}$. "
                    r"Tốc độ phản ứng mới là $v' = k \cdot (3C_{\text{NO}})^2 \cdot (3C_{\text{O}_2}) = 27 \cdot k \cdot C_{\text{NO}}^2 \cdot C_{\text{O}_2} = 27v$. "
                    r"Vậy tốc độ phản ứng tăng lên $27$ lần."
                ),
            },
        ],
        key_takeaways=[
            r"Tốc độ trung bình của phản ứng $\text{aA} + \text{bB} \rightarrow \text{cC} + \text{dD}$ luôn dương và phải chia cho hệ số tỉ lượng tương ứng của từng chất.",
            r"Trong biểu thức định luật tác dụng khối lượng $v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$, hằng số tốc độ $k$ chỉ phụ thuộc vào nhiệt độ và bản chất chất phản ứng, không phụ thuộc nồng độ.",
            r"Chất xúc tác làm giảm năng lượng hoạt hóa $E_{\text{a}}$ của phản ứng nên làm tăng tốc độ phản ứng nhưng giữ nguyên khối lượng và bản chất hóa học sau phản ứng.",
            r"Theo quy tắc Van't Hoff, khi nhiệt độ tăng từ $T_1$ lên $T_2$ thì tốc độ tăng $\gamma^{\frac{T_2 - T_1}{10}}$ lần và thời gian phản ứng giảm đi bấy nhiêu lần.",
        ],
        questions=[
            mcq(
                question=r"Đối với phản ứng hóa học tổng quát $\text{aA} + \text{bB} \rightarrow \text{cC} + \text{dD}$, công thức tính tốc độ trung bình $\overline{v}$ của phản ứng theo chất tham gia $\text{A}$ là:",
                options=[
                    r"$\overline{v} = -\dfrac{1}{a}\dfrac{\Delta C_{\text{A}}}{\Delta t}$",
                    r"$\overline{v} = +\dfrac{1}{a}\dfrac{\Delta C_{\text{A}}}{\Delta t}$",
                    r"$\overline{v} = -a\dfrac{\Delta C_{\text{A}}}{\Delta t}$",
                    r"$\overline{v} = +a\dfrac{\Delta C_{\text{A}}}{\Delta t}$",
                ],
                answer="A",
                level="biet",
                solution=r"Vì nồng độ chất tham gia $\text{A}$ giảm dần theo thời gian ($\Delta C_{\text{A}} < 0$) và hệ số tỉ lượng là $a$, nên công thức đúng là $\overline{v} = -\dfrac{1}{a}\dfrac{\Delta C_{\text{A}}}{\Delta t}$.",
            ),
            mcq(
                question=r"Cho phản ứng đơn giản xảy ra trong pha khí: $\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightarrow 2\text{NH}_3\text{(g)}$. Biểu thức tốc độ tức thời $v$ của phản ứng theo định luật tác dụng khối lượng là:",
                options=[
                    r"$v = k \cdot C_{\text{N}_2} \cdot C_{\text{H}_2}$",
                    r"$v = k \cdot C_{\text{N}_2} \cdot C_{\text{H}_2}^3$",
                    r"$v = k \cdot C_{\text{N}_2} \cdot 3C_{\text{H}_2}$",
                    r"$v = k \cdot C_{\text{NH}_3}^2$",
                ],
                answer="B",
                level="biet",
                solution=r"Theo định luật tác dụng khối lượng cho phản ứng đơn giản $\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightarrow 2\text{NH}_3\text{(g)}$, biểu thức tốc độ tức thời là $v = k \cdot C_{\text{N}_2}^1 \cdot C_{\text{H}_2}^3 = k \cdot C_{\text{N}_2} \cdot C_{\text{H}_2}^3$.",
            ),
            mcq(
                question=r"Hằng số tốc độ phản ứng $k$ trong biểu thức $v = k \cdot C_{\text{A}}^a \cdot C_{\text{B}}^b$ phụ thuộc vào yếu tố nào sau đây?",
                options=[
                    r"Nồng độ mol ban đầu của chất $\text{A}$ và chất $\text{B}$",
                    r"Thể tích của bình phản ứng",
                    r"Bản chất của chất phản ứng và nhiệt độ (cùng sự có mặt của chất xúc tác)",
                    r"Thời gian tiến hành phản ứng $\Delta t$",
                ],
                answer="C",
                level="biet",
                solution=r"Hằng số tốc độ $k$ (tốc độ riêng khi $C_{\text{A}} = C_{\text{B}} = 1\text{ M}$) chỉ phụ thuộc vào bản chất của các chất phản ứng và nhiệt độ (cũng như chất xúc tác), không phụ thuộc vào nồng độ chất phản ứng.",
            ),
            mcq(
                question=r"Yếu tố nào dưới đây KHÔNG làm thay đổi tốc độ của phản ứng chỉ có các chất rắn và dung dịch lỏng tham gia: $\text{Zn(s)} + 2\text{HCl(aq)} \rightarrow \text{ZnCl}_2\text{(aq)} + \text{H}_2\text{(g)}$?",
                options=[
                    r"Thay kẽm viên bằng bột kẽm có cùng khối lượng",
                    r"Tăng nồng độ dung dịch $\text{HCl}$ từ $1\text{ M}$ lên $2\text{ M}$",
                    r"Tăng áp suất chung của hệ phản ứng",
                    r"Đun nóng nhẹ dung dịch phản ứng",
                ],
                answer="C",
                level="biet",
                solution=r"Áp suất chỉ ảnh hưởng đến tốc độ của phản ứng có chất khí tham gia. Trong phản ứng $\text{Zn(s)} + 2\text{HCl(aq)} \rightarrow \text{ZnCl}_2\text{(aq)} + \text{H}_2\text{(g)}$, các chất tham gia là chất rắn $\text{Zn(s)}$ và chất tan $\text{HCl(aq)}$, không có chất khí tham gia nên thay đổi áp suất không làm đổi tốc độ phản ứng.",
            ),
            mcq(
                question=r"Một phản ứng hóa học có hệ số nhiệt độ Van't Hoff là $\gamma = 3$. Khi tăng nhiệt độ của phản ứng từ $20^\circ\text{C}$ lên $50^\circ\text{C}$ thì tốc độ của phản ứng này tăng lên bao nhiêu lần?",
                options=[
                    r"$9\text{ lần}$",
                    r"$12\text{ lần}$",
                    r"$27\text{ lần}$",
                    r"$81\text{ lần}$",
                ],
                answer="C",
                level="hieu",
                solution=r"Áp dụng công thức Van't Hoff: $\dfrac{v_2}{v_1} = \gamma^{\frac{T_2 - T_1}{10}} = 3^{\frac{50 - 20}{10}} = 3^3 = 27\text{ lần}$.",
            ),
            mcq(
                question=r"Cho phản ứng dị thể đơn giản: $\text{C(s)} + \text{O}_2\text{(g)} \rightarrow \text{CO}_2\text{(g)}$. Nếu giữ nguyên nhiệt độ và tăng nồng độ khí $\text{O}_2$ lên gấp $4$ lần thì tốc độ phản ứng thay đổi như thế nào?",
                options=[
                    r"Tăng lên $4\text{ lần}$",
                    r"Tăng lên $8\text{ lần}$",
                    r"Tăng lên $16\text{ lần}$",
                    r"Không thay đổi",
                ],
                answer="A",
                level="hieu",
                solution=r"Vì $\text{C(s)}$ là chất rắn nguyên chất nên không có mặt trong biểu thức tốc độ: $v = k \cdot C_{\text{O}_2}$. Khi tăng nồng độ $\text{O}_2$ lên gấp $4$ lần thì tốc độ phản ứng tăng $4\text{ lần}$.",
            ),
            tf4(
                stem=r"Xét phản ứng phân hủy hydrogen peroxide trong dung dịch nước: $2\text{H}_2\text{O}_2\text{(aq)} \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O(l)} + \text{O}_2\text{(g)}$. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Tốc độ trung bình của phản ứng được tính theo biểu thức $\overline{v} = -\dfrac{1}{2}\dfrac{\Delta C_{\text{H}_2\text{O}_2}}{\Delta t} = \dfrac{\Delta C_{\text{O}_2}}{\Delta t}$.",
                    r"b) Bột $\text{MnO}_2$ đóng vai trò là chất phản ứng nên khối lượng $\text{MnO}_2$ giảm dần trong quá trình phản ứng.",
                    r"c) Sự có mặt của $\text{MnO}_2$ làm giảm năng lượng hoạt hóa $E_{\text{a}}$ của phản ứng phân hủy $\text{H}_2\text{O}_2$, giúp khí $\text{O}_2$ thoát ra nhanh và mạnh hơn.",
                    r"d) Nếu pha loãng dung dịch $\text{H}_2\text{O}_2$ bằng nước cất ở cùng nhiệt độ thì tốc độ thoát khí $\text{O}_2$ sẽ tăng lên.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Theo hệ số tỉ lượng của phương trình $2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2$, ta có $\overline{v} = -\dfrac{1}{2}\dfrac{\Delta C_{\text{H}_2\text{O}_2}}{\Delta t} = \dfrac{\Delta C_{\text{O}_2}}{\Delta t}$. "
                    r"b) Sai: $\text{MnO}_2$ là chất xúc tác nên không bị tiêu hao sau phản ứng, khối lượng $\text{MnO}_2$ giữ nguyên. "
                    r"c) Đúng: Chất xúc tác $\text{MnO}_2$ làm giảm năng lượng hoạt hóa $E_{\text{a}}$ nên làm tăng tốc độ phân hủy $\text{H}_2\text{O}_2$. "
                    r"d) Sai: Pha loãng làm giảm nồng độ $C_{\text{H}_2\text{O}_2}$ nên tần số va chạm hiệu quả giảm, tốc độ thoát khí $\text{O}_2$ giảm."
                ),
            ),
            tf4(
                stem=r"Một học sinh khảo sát tốc độ phản ứng giữa đá vôi và dung dịch hydrochloric acid: $\text{CaCO}_3\text{(s)} + 2\text{HCl(aq)} \rightarrow \text{CaCl}_2\text{(aq)} + \text{CO}_2\text{(g)} + \text{H}_2\text{O(l)}$. Xét tính đúng/sai của các nhận định sau:",
                statements=[
                    r"a) Đập nhỏ viên đá vôi $\text{CaCO}_3$ thành dạng hạt nhỏ làm tăng diện tích bề mặt tiếp xúc nên tốc độ thoát khí $\text{CO}_2$ tăng.",
                    r"b) Theo định luật tác dụng khối lượng, biểu thức tốc độ của phản ứng có dạng $v = k \cdot C_{\text{CaCO}_3} \cdot C_{\text{HCl}}^2$.",
                    r"c) Khi đun nhẹ ống nghiệm chứa hỗn hợp phản ứng, các ion $\text{H}^+$ chuyển động nhanh hơn và va chạm hiệu quả hơn với bề mặt $\text{CaCO}_3$ nên tốc độ phản ứng tăng.",
                    r"d) Tốc độ phản ứng giữ không đổi trong suốt quá trình từ lúc bắt đầu cho đến khi viên đá vôi tan hết.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Đập nhỏ $\text{CaCO}_3\text{(s)}$ làm tăng tổng diện tích bề mặt tiếp xúc với dung dịch $\text{HCl}$ nên tốc độ phản ứng tăng. "
                    r"b) Sai: $\text{CaCO}_3\text{(s)}$ là chất rắn nguyên chất nên không đưa nồng độ vào biểu thức tốc độ. "
                    r"c) Đúng: Tăng nhiệt độ làm tăng động năng và tần số va chạm có năng lượng vượt năng lượng hoạt hóa $E_{\text{a}}$, giúp tốc độ phản ứng tăng. "
                    r"d) Sai: Theo thời gian, nồng độ $\text{HCl}$ và diện tích bề mặt viên đá vôi giảm dần nên tốc độ phản ứng giảm dần."
                ),
            ),
            mcq(
                question=r"Trong bình kín ở nhiệt độ không đổi, xét phản ứng tổng hợp $\text{SO}_3$: $2\text{SO}_2\text{(g)} + \text{O}_2\text{(g)} \rightarrow 2\text{SO}_3\text{(g)}$ (giả sử là phản ứng đơn giản). Khi thể tích của bình phản ứng giảm đi một nửa so với ban đầu thì tốc độ phản ứng thuận tại thời điểm đó thay đổi như thế nào?",
                options=[
                    r"Tăng lên $2\text{ lần}$",
                    r"Tăng lên $4\text{ lần}$",
                    r"Tăng lên $8\text{ lần}$",
                    r"Giảm đi $8\text{ lần}$",
                ],
                answer="C",
                level="vandung",
                solution=r"Biểu thức tốc độ của phản ứng là $v = k \cdot C_{\text{SO}_2}^2 \cdot C_{\text{O}_2}$. Khi thể tích bình giảm đi một nửa ($V' = \dfrac{V}{2}$), nồng độ mol của cả $\text{SO}_2$ và $\text{O}_2$ đều tăng lên gấp $2$ lần: $C'_{\text{SO}_2} = 2C_{\text{SO}_2}$ và $C'_{\text{O}_2} = 2C_{\text{O}_2}$. Do đó $v' = k \cdot (2C_{\text{SO}_2})^2 \cdot (2C_{\text{O}_2}) = 8v$, tức tốc độ tăng lên $8\text{ lần}$.",
            ),
            short(
                question=r"Ở $25^\circ\text{C}$, một phản ứng hóa học cần $32\text{ phút}$ để hoàn thành. Biết hệ số nhiệt độ Van't Hoff của phản ứng trong khoảng nhiệt độ xét là $\gamma = 2$. Nếu thực hiện phản ứng đó ở nhiệt độ $65^\circ\text{C}$ thì phản ứng sẽ hoàn thành sau bao nhiêu phút?",
                answer=["2", "2,0", "2.0"],
                level="vandung",
                solution=r"Độ tăng nhiệt độ là $\Delta T = 65^\circ\text{C} - 25^\circ\text{C} = 40^\circ\text{C}$. Theo quy tắc Van't Hoff, tốc độ phản ứng tăng lên $\dfrac{v_2}{v_1} = \gamma^{\frac{40}{10}} = 2^4 = 16\text{ lần}$. Vì thời gian hoàn thành phản ứng tỉ lệ nghịch với tốc độ nên $t_2 = \dfrac{t_1}{16} = \dfrac{32}{16} = 2\text{ phút}$.",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 2: CÂN BẰNG HÓA HỌC VÀ NGUYÊN LÝ CHUYỂN DỊCH LE CHATELIER
    # =========================================================================
    lesson(
        grade=11,
        order=2,
        code="H11-C02",
        title="Chương 2: Cân bằng hóa học và nguyên lý chuyển dịch Le Chatelier",
        topic="can-bang-hoa-hoc",
        description="Phản ứng một chiều và phản ứng thuận nghịch, trạng thái cân bằng động, hằng số cân bằng KC và nguyên lý chuyển dịch cân bằng Le Chatelier.",
        summary=(
            r"Chương học làm rõ sự khác biệt giữa phản ứng một chiều ($\rightarrow$) và phản ứng thuận nghịch ($\rightleftharpoons$), "
            r"bản chất của trạng thái cân bằng động ($v_{\text{thuận}} = v_{\text{nghịch}} > 0$), cách lập biểu thức hằng số cân bằng "
            r"$K_{\text{C}} = \dfrac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}$ (không biểu diễn chất rắn nguyên chất) "
            r"và vận dụng nguyên lý chuyển dịch cân bằng Le Chatelier khi thay đổi nồng độ, áp suất, nhiệt độ."
        ),
        objectives=[
            r"Phân biệt được phản ứng một chiều và phản ứng thuận nghịch $\text{aA} + \text{bB} \rightleftharpoons \text{cC} + \text{dD}$; giải thích được vì sao cân bằng hóa học là một cân bằng động ($v_{\text{thuận}} = v_{\text{nghịch}} > 0$).",
            r"Viết được biểu thức hằng số cân bằng $K_{\text{C}}$ cho phản ứng đồng thể và dị thể (lưu ý chất rắn nguyên chất không có mặt trong biểu thức $K_{\text{C}}$) và nêu được ý nghĩa của độ lớn $K_{\text{C}}$.",
            r"Phát biểu và vận dụng được nguyên lý chuyển dịch cân bằng Le Chatelier để dự đoán chiều chuyển dịch cân bằng khi thay đổi nồng độ, áp suất (hệ khí có $\Delta n_{\text{khí}} \neq 0$) và nhiệt độ ($\Delta_{\text{r}} H_{298}^\circ$).",
            r"Giải thích được các điều kiện tối ưu trong sản xuất công nghiệp như tổng hợp $\text{NH}_3$ (quy trình Haber – Bosch) và oxi hóa $\text{SO}_2$ thành $\text{SO}_3$.",
        ],
        formulas=[
            {
                "name": "Điều kiện tại trạng thái cân bằng hóa học",
                "formula": r"$v_{\text{thuận}} = v_{\text{nghịch}} > 0 \implies [\text{A}], [\text{B}], [\text{C}], [\text{D}] = \text{const}$",
                "note": r"Phản ứng thuận và phản ứng nghịch vẫn tiếp diễn với tốc độ bằng nhau nên gọi là cân bằng động.",
            },
            {
                "name": "Biểu thức hằng số cân bằng nồng độ",
                "formula": r"$\text{aA(g)} + \text{bB(g)} \rightleftharpoons \text{cC(g)} + \text{dD(g)}: \quad K_{\text{C}} = \dfrac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}$",
                "note": r"$[\text{A}], [\text{B}], [\text{C}], [\text{D}]$ là nồng độ mol ở trạng thái cân bằng; $K_{\text{C}}$ chỉ phụ thuộc vào nhiệt độ và bản chất phản ứng.",
            },
            {
                "name": "Hằng số cân bằng đối với hệ dị thể có chất rắn nguyên chất",
                "formula": r"$\text{CaCO}_3\text{(s)} \rightleftharpoons \text{CaO(s)} + \text{CO}_2\text{(g)}: \quad K_{\text{C}} = [\text{CO}_2]$",
                "note": r"Chất rắn nguyên chất $\text{(s)}$ và chất lỏng nguyên chất làm dung môi $\text{(l)}$ không có mặt trong biểu thức $K_{\text{C}}$.",
            },
            {
                "name": "Quy tắc nhiệt độ trong nguyên lý Le Chatelier",
                "formula": r"$T \uparrow \implies \text{dịch theo chiều thu nhiệt } (\Delta_{\text{r}} H_{298}^\circ > 0); \quad T \downarrow \implies \text{dịch theo chiều tỏa nhiệt } (\Delta_{\text{r}} H_{298}^\circ < 0)$",
                "note": r"Ghi nhớ nhanh: Tăng thu – Giảm tỏa; chất xúc tác không làm chuyển dịch cân bằng.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Phản ứng một chiều, phản ứng thuận nghịch và cân bằng động",
                "content": (
                    r"Phản ứng một chiều là phản ứng chỉ xảy ra theo chiều từ chất tham gia tạo thành sản phẩm trong điều kiện xác định "
                    r"(biểu diễn bằng mũi tên một chiều $\rightarrow$). Phản ứng thuận nghịch là phản ứng xảy ra đồng thời theo hai chiều "
                    r"trái ngược nhau trong cùng một điều kiện (biểu diễn bằng mũi tên hai chiều $\rightleftharpoons$). "
                    r"Khi tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_{\text{thuận}} = v_{\text{nghịch}} > 0$), hệ đạt trạng thái "
                    r"cân bằng hóa học. Vì ở trạng thái cân bằng, cả hai phản ứng thuận và nghịch không dừng lại mà vẫn tiếp tục diễn ra "
                    r"với tốc độ bằng nhau nên cân bằng hóa học là một cân bằng động, tại đó nồng độ các chất trong hệ giữ không đổi."
                ),
            },
            {
                "title": "2. Hằng số cân bằng KC và ý nghĩa",
                "content": (
                    r"Xét phản ứng thuận nghịch tổng quát $\text{aA} + \text{bB} \rightleftharpoons \text{cC} + \text{dD}$, hằng số cân bằng "
                    r"được xác định bởi biểu thức $K_{\text{C}} = \dfrac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}$, trong đó "
                    r"$[\text{A}], [\text{B}], [\text{C}], [\text{D}]$ là nồng độ mol/L của các chất ở trạng thái cân bằng. "
                    r"Lưu ý quan trọng: (1) Không đưa nồng độ chất rắn nguyên chất $\text{(s)}$ và chất lỏng nguyên chất làm dung môi $\text{(l)}$ "
                    r"vào biểu thức $K_{\text{C}}$; (2) Giá trị của $K_{\text{C}}$ chỉ phụ thuộc vào bản chất của phản ứng và nhiệt độ $T$, "
                    r"không phụ thuộc vào nồng độ ban đầu của các chất; (3) $K_{\text{C}}$ càng lớn thì phản ứng thuận càng chiếm ưu thế "
                    r"và hiệu suất chuyển hóa tạo sản phẩm càng cao."
                ),
            },
            {
                "title": "3. Nguyên lý chuyển dịch cân bằng Le Chatelier",
                "content": (
                    r"Nguyên lý Le Chatelier phát biểu: Một phản ứng thuận nghịch đang ở trạng thái cân bằng, khi chịu một tác động từ bên ngoài "
                    r"như biến đổi nồng độ, áp suất hoặc nhiệt độ thì cân bằng sẽ chuyển dịch theo chiều làm giảm tác động bên ngoài đó:\n"
                    r"- Ảnh hưởng của nồng độ: Khi tăng nồng độ một chất, cân bằng chuyển dịch theo chiều làm giảm nồng độ chất đó (chiều tiêu thụ chất đó) và ngược lại.\n"
                    r"- Ảnh hưởng của áp suất (đối với hệ có chất khí): Khi tăng áp suất chung của hệ (nén giảm thể tích), cân bằng chuyển dịch theo chiều làm giảm số mol khí; khi giảm áp suất chung, cân bằng chuyển dịch theo chiều làm tăng số mol khí. Nếu tổng hệ số tỉ lượng của các chất khí ở hai vế bằng nhau ($\Delta n_{\text{khí}} = 0$), việc thay đổi áp suất không làm chuyển dịch cân bằng.\n"
                    r"- Ảnh hưởng của nhiệt độ: Khi tăng nhiệt độ, cân bằng chuyển dịch theo chiều phản ứng thu nhiệt ($\Delta_{\text{r}} H_{298}^\circ > 0$); khi giảm nhiệt độ, cân bằng chuyển dịch theo chiều phản ứng tỏa nhiệt ($\Delta_{\text{r}} H_{298}^\circ < 0$).\n"
                    r"- Vai trò của chất xúc tác: Chất xúc tác làm tăng tốc độ phản ứng thuận và phản ứng nghịch với số lần bằng nhau nên KHÔNG làm chuyển dịch cân bằng, mà chỉ giúp hệ đạt tới trạng thái cân bằng nhanh hơn."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Tối ưu hóa tổng hợp $\text{NH}_3$ theo nguyên lý Le Chatelier",
                "problem": (
                    r"Xét cân bằng tổng hợp ammonia trong công nghiệp (quy trình Haber – Bosch): "
                    r"$\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightleftharpoons 2\text{NH}_3\text{(g)}$ có $\Delta_{\text{r}} H_{298}^\circ = -91,8\text{ kJ} < 0$. "
                    r"Hãy viết biểu thức $K_{\text{C}}$ và cho biết cần tác động vào nồng độ, áp suất, nhiệt độ như thế nào để cân bằng chuyển dịch theo chiều thuận."
                ),
                "solution": (
                    r"Biểu thức hằng số cân bằng là $K_{\text{C}} = \dfrac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3}$. "
                    r"Để cân bằng chuyển dịch theo chiều thuận (tạo thêm $\text{NH}_3$): "
                    r"(1) Về nồng độ: Tăng nồng độ $\text{N}_2$ hoặc $\text{H}_2$, đồng thời hóa lỏng để tách $\text{NH}_3$ ra khỏi hỗn hợp phản ứng; "
                    r"(2) Về áp suất: Tăng áp suất chung của hệ vì chiều thuận làm giảm số mol khí từ $4\text{ mol}$ xuống $2\text{ mol}$; "
                    r"(3) Về nhiệt độ: Hạ nhiệt độ thích hợp vì chiều thuận là phản ứng tỏa nhiệt ($\Delta_{\text{r}} H_{298}^\circ < 0$). Trong thực tế công nghiệp, người ta duy trì nhiệt độ khoảng $400^\circ\text{C} \div 450^\circ\text{C}$ kết hợp xúc tác bột $\text{Fe}$ để đảm bảo tốc độ phản ứng đủ lớn."
                ),
            },
            {
                "title": r"Ví dụ 2: Tính hằng số cân bằng $K_{\text{C}}$ từ số mol ban đầu và tại cân bằng",
                "problem": (
                    r"Cho $1,0\text{ mol}$ khí $\text{CO}$ và $1,0\text{ mol}$ hơi nước $\text{H}_2\text{O}$ vào bình kín dung tích $1,0\text{ L}$ ở nhiệt độ $T$ không đổi. "
                    r"Khi phản ứng $\text{CO(g)} + \text{H}_2\text{O(g)} \rightleftharpoons \text{CO}_2\text{(g)} + \text{H}_2\text{(g)}$ đạt trạng thái cân bằng thì thu được $0,6\text{ mol}$ $\text{CO}_2$. "
                    r"Tính hằng số cân bằng $K_{\text{C}}$ của phản ứng ở nhiệt độ $T$."
                ),
                "solution": (
                    r"Vì thể tích bình là $V = 1,0\text{ L}$ nên nồng độ mol bằng số mol. Tại trạng thái cân bằng, $[\text{CO}_2] = [\text{H}_2] = 0,6\text{ M}$. "
                    r"Nồng độ còn lại ở trạng thái cân bằng của các chất tham gia là $[\text{CO}] = 1,0 - 0,6 = 0,4\text{ M}$ và $[\text{H}_2\text{O}] = 1,0 - 0,6 = 0,4\text{ M}$. "
                    r"Hằng số cân bằng của phản ứng ở nhiệt độ $T$ là: "
                    r"$K_{\text{C}} = \dfrac{[\text{CO}_2][\text{H}_2]}{[\text{CO}][\text{H}_2\text{O}]} = \dfrac{0,6 \cdot 0,6}{0,4 \cdot 0,4} = \dfrac{0,36}{0,16} = 2,25$."
                ),
            },
        ],
        key_takeaways=[
            r"Tại trạng thái cân bằng động, $v_{\text{thuận}} = v_{\text{nghịch}} > 0$ và nồng độ mọi chất trong hệ giữ không đổi theo thời gian.",
            r"Chất rắn nguyên chất $\text{(s)}$ không xuất hiện trong biểu thức hằng số cân bằng $K_{\text{C}}$; giá trị $K_{\text{C}}$ chỉ thay đổi khi nhiệt độ $T$ thay đổi.",
            r"Khi $\Delta n_{\text{khí}} = 0$, việc thay đổi áp suất chung của hệ không làm chuyển dịch cân bằng.",
            r"Chất xúc tác không làm chuyển dịch cân bằng hóa học và không làm thay đổi hằng số cân bằng $K_{\text{C}}$.",
        ],
        questions=[
            mcq(
                question=r"Tại trạng thái cân bằng của một phản ứng thuận nghịch, phát biểu nào sau đây là ĐÚNG?",
                options=[
                    r"Phản ứng thuận và phản ứng nghịch đều đã dừng lại hoàn toàn ($v_{\text{thuận}} = v_{\text{nghịch}} = 0$)",
                    r"Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch ($v_{\text{thuận}} = v_{\text{nghịch}} > 0$) và nồng độ các chất không đổi",
                    r"Nồng độ của các chất sản phẩm luôn bằng nồng độ của các chất tham gia",
                    r"Tốc độ phản ứng thuận luôn lớn hơn tốc độ phản ứng nghịch",
                ],
                answer="B",
                level="biet",
                solution=r"Cân bằng hóa học là cân bằng động: tại đó phản ứng thuận và phản ứng nghịch vẫn tiếp diễn với tốc độ bằng nhau ($v_{\text{thuận}} = v_{\text{nghịch}} > 0$), làm cho nồng độ các chất trong hệ giữ không đổi.",
            ),
            mcq(
                question=r"Cho cân bằng dị thể nung vôi: $\text{CaCO}_3\text{(s)} \rightleftharpoons \text{CaO(s)} + \text{CO}_2\text{(g)}$. Biểu thức hằng số cân bằng $K_{\text{C}}$ của phản ứng trên là:",
                options=[
                    r"$K_{\text{C}} = \dfrac{[\text{CaO}][\text{CO}_2]}{[\text{CaCO}_3]}$",
                    r"$K_{\text{C}} = [\text{CO}_2]$",
                    r"$K_{\text{C}} = \dfrac{1}{[\text{CO}_2]}$",
                    r"$K_{\text{C}} = [\text{CaO}][\text{CO}_2]$",
                ],
                answer="B",
                level="biet",
                solution=r"Vì $\text{CaCO}_3\text{(s)}$ và $\text{CaO(s)}$ là các chất rắn nguyên chất nên không có mặt trong biểu thức hằng số cân bằng $K_{\text{C}}$. Do đó $K_{\text{C}} = [\text{CO}_2]$.",
            ),
            mcq(
                question=r"Hằng số cân bằng $K_{\text{C}}$ của một phản ứng thuận nghịch xác định chỉ phụ thuộc vào yếu tố nào sau đây?",
                options=[
                    r"Nồng độ ban đầu của các chất phản ứng",
                    r"Áp suất chung của hệ phản ứng",
                    r"Nhiệt độ của hệ phản ứng",
                    r"Chất xúc tác được thêm vào hệ",
                ],
                answer="C",
                level="biet",
                solution=r"Đối với một phản ứng thuận nghịch xác định, hằng số cân bằng $K_{\text{C}}$ chỉ phụ thuộc vào nhiệt độ $T$, không phụ thuộc vào nồng độ ban đầu, áp suất hay chất xúc tác.",
            ),
            mcq(
                question=r"Đối với một phản ứng thuận nghịch đang ở trạng thái cân bằng, khi thêm chất xúc tác vào hệ thì:",
                options=[
                    r"Cân bằng chuyển dịch theo chiều thuận",
                    r"Cân bằng chuyển dịch theo chiều nghịch",
                    r"Hằng số cân bằng $K_{\text{C}}$ tăng lên",
                    r"Cân bằng không bị chuyển dịch vì chất xúc tác làm tăng tốc độ phản ứng thuận và nghịch như nhau",
                ],
                answer="D",
                level="biet",
                solution=r"Chất xúc tác làm tăng tốc độ của cả phản ứng thuận và phản ứng nghịch với cùng một tỉ lệ nên không làm chuyển dịch cân bằng hóa học.",
            ),
            mcq(
                question=r"Cho cân bằng hóa học: $\text{H}_2\text{(g)} + \text{I}_2\text{(g)} \rightleftharpoons 2\text{HI(g)}$ có $\Delta_{\text{r}} H_{298}^\circ < 0$. Tác động nào dưới đây KHÔNG làm chuyển dịch cân bằng của hệ?",
                options=[
                    r"Tăng nhiệt độ của bình phản ứng",
                    r"Thêm một lượng khí $\text{H}_2$ vào bình phản ứng",
                    r"Tăng áp suất chung của hệ bằng cách nén giảm thể tích bình ở nhiệt độ không đổi",
                    r"Lấy bớt một lượng khí $\text{HI}$ ra khỏi bình phản ứng",
                ],
                answer="C",
                level="hieu",
                solution=r"Trong phản ứng $\text{H}_2\text{(g)} + \text{I}_2\text{(g)} \rightleftharpoons 2\text{HI(g)}$, tổng số mol khí ở vế trái ($1 + 1 = 2$) bằng tổng số mol khí ở vế phải ($2$), tức $\Delta n_{\text{khí}} = 0$. Do đó thay đổi áp suất chung không làm chuyển dịch cân bằng.",
            ),
            mcq(
                question=r"Cho cân bằng giữa hai khí $\text{NO}_2$ (màu nâu đỏ) và $\text{N}_2\text{O}_4$ (không màu): $2\text{NO}_2\text{(g)} \rightleftharpoons \text{N}_2\text{O}_4\text{(g)}$ có $\Delta_{\text{r}} H_{298}^\circ = -58\text{ kJ} < 0$. Khi ngâm bình thủy tinh kín chứa hỗn hợp khí trên vào chậu nước đá thì hiện tượng quan sát được là:",
                options=[
                    r"Màu nâu đỏ của hỗn hợp khí nhạt dần vì cân bằng chuyển dịch theo chiều thuận",
                    r"Màu nâu đỏ của hỗn hợp khí đậm lên vì cân bằng chuyển dịch theo chiều nghịch",
                    r"Màu sắc của hỗn hợp khí hoàn toàn không thay đổi",
                    r"Áp suất trong bình tăng vọt lên",
                ],
                answer="A",
                level="hieu",
                solution=r"Chiều thuận tạo $\text{N}_2\text{O}_4$ (không màu) là chiều tỏa nhiệt ($\Delta_{\text{r}} H_{298}^\circ = -58\text{ kJ} < 0$). Khi ngâm bình vào nước đá (giảm nhiệt độ), theo nguyên lý Le Chatelier cân bằng chuyển dịch theo chiều tỏa nhiệt (chiều thuận), làm giảm nồng độ $\text{NO}_2$ nên màu nâu đỏ nhạt dần.",
            ),
            tf4(
                stem=r"Trong công nghiệp sản xuất sulfuric acid, giai đoạn oxi hóa sulfur dioxide thành sulfur trioxide diễn ra theo cân bằng: $2\text{SO}_2\text{(g)} + \text{O}_2\text{(g)} \rightleftharpoons 2\text{SO}_3\text{(g)}$ với $\Delta_{\text{r}} H_{298}^\circ = -197\text{ kJ}$. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Biểu thức hằng số cân bằng của phản ứng trên là $K_{\text{C}} = \dfrac{[\text{SO}_3]^2}{[\text{SO}_2]^2[\text{O}_2]}$.",
                    r"b) Khi tăng nhiệt độ của buồng phản ứng, cân bằng chuyển dịch theo chiều thuận làm tăng hiệu suất tạo $\text{SO}_3$.",
                    r"c) Khi tăng áp suất chung của hệ hoặc thổi dư không khí (tăng nồng độ $\text{O}_2$), cân bằng chuyển dịch theo chiều thuận.",
                    r"d) Việc sử dụng chất xúc tác $\text{V}_2\text{O}_5$ làm tăng giá trị hằng số cân bằng $K_{\text{C}}$ của phản ứng.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Theo định nghĩa hằng số cân bằng cho hệ đồng thể khí, $K_{\text{C}} = \dfrac{[\text{SO}_3]^2}{[\text{SO}_2]^2[\text{O}_2]}$. "
                    r"b) Sai: Vì chiều thuận tỏa nhiệt ($\Delta_{\text{r}} H_{298}^\circ = -197\text{ kJ} < 0$), nên khi tăng nhiệt độ cân bằng chuyển dịch theo chiều thu nhiệt (chiều nghịch), làm giảm hiệu suất tạo $\text{SO}_3$. "
                    r"c) Đúng: Tăng áp suất làm cân bằng dịch về phía ít mol khí hơn (chiều thuận, từ $3\text{ mol}$ khí xuống $2\text{ mol}$ khí); tăng nồng độ $\text{O}_2$ cũng làm cân bằng dịch theo chiều thuận. "
                    r"d) Sai: Chất xúc tác $\text{V}_2\text{O}_5$ chỉ giúp hệ nhanh đạt cân bằng hơn chứ không làm thay đổi hằng số cân bằng $K_{\text{C}}$."
                ),
            ),
            tf4(
                stem=r"Xét cân bằng este hóa giữa acetic acid và ethanol: $\text{CH}_3\text{COOH(l)} + \text{C}_2\text{H}_5\text{OH(l)} \rightleftharpoons \text{CH}_3\text{COOC}_2\text{H}_5\text{(l)} + \text{H}_2\text{O(l)}$. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Để tăng hiệu suất thu hồi ester $\text{CH}_3\text{COOC}_2\text{H}_5$, người ta có thể dùng dư một trong hai chất đầu hoặc chưng cất tách ester ra khỏi hỗn hợp phản ứng.",
                    r"b) Tại trạng thái cân bằng, số mol của $\text{CH}_3\text{COOH}$ và $\text{C}_2\text{H}_5\text{OH}$ trong bình bằng $0$.",
                    r"c) Dung dịch $\text{H}_2\text{SO}_4$ đặc vừa đóng vai trò chất xúc tác vừa có tác dụng hút nước giúp cân bằng chuyển dịch theo chiều thuận.",
                    r"d) Nếu pha thêm nhiều nước cất vào hỗn hợp phản ứng thì cân bằng sẽ chuyển dịch theo chiều thuận tạo thêm ester.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Tăng nồng độ chất tham gia hoặc giảm nồng độ sản phẩm ($\text{CH}_3\text{COOC}_2\text{H}_5$) đều làm cân bằng chuyển dịch theo chiều thuận. "
                    r"b) Sai: Đây là phản ứng thuận nghịch nên tại trạng thái cân bằng luôn tồn tại đồng thời cả chất tham gia và sản phẩm, số mol chất tham gia luôn khác $0$. "
                    r"c) Đúng: $\text{H}_2\text{SO}_4$ đặc vừa cung cấp $\text{H}^+$ làm xúc tác, vừa có tính háo nước làm giảm lượng $\text{H}_2\text{O}$, thúc đẩy cân bằng dịch theo chiều thuận. "
                    r"d) Sai: Thêm nước làm tăng nồng độ $\text{H}_2\text{O}$ ở vế phải nên cân bằng chuyển dịch theo chiều nghịch (thủy phân ester)."
                ),
            ),
            mcq(
                question=r"Nạp $0,4\text{ mol}$ khí $\text{N}_2$ và $1,6\text{ mol}$ khí $\text{H}_2$ vào một bình kín dung tích $1,0\text{ L}$ ở nhiệt độ $T$ không đổi. Khi phản ứng $\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightleftharpoons 2\text{NH}_3\text{(g)}$ đạt tới trạng thái cân bằng thì thu được $0,4\text{ mol}$ khí $\text{NH}_3$. Hằng số cân bằng $K_{\text{C}}$ của phản ứng ở nhiệt độ $T$ là:",
                options=[
                    r"$K_{\text{C}} = 0,20$",
                    r"$K_{\text{C}} = 0,80$",
                    r"$K_{\text{C}} = 1,25$",
                    r"$K_{\text{C}} = 2,00$",
                ],
                answer="B",
                level="vandung",
                solution=r"Vì $V = 1,0\text{ L}$ nên nồng độ mol bằng số mol. Tại cân bằng $[\text{NH}_3] = 0,4\text{ M}$, suy ra lượng $\text{N}_2$ đã phản ứng là $0,2\text{ M}$ và lượng $\text{H}_2$ đã phản ứng là $0,6\text{ M}$. Nồng độ còn lại tại cân bằng: $[\text{N}_2] = 0,4 - 0,2 = 0,2\text{ M}$ và $[\text{H}_2] = 1,6 - 0,6 = 1,0\text{ M}$. Vậy $K_{\text{C}} = \dfrac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3} = \dfrac{0,4^2}{0,2 \cdot 1,0^3} = \dfrac{0,16}{0,20} = 0,80$.",
            ),
            short(
                question=r"Trong một bình kín dung tích $1,0\text{ L}$ ở nhiệt độ $T$ không đổi, người ta cho vào $1,0\text{ mol}$ khí $\text{CO}$ và $1,0\text{ mol}$ hơi nước $\text{H}_2\text{O}$ để thực hiện phản ứng thuận nghịch: $\text{CO(g)} + \text{H}_2\text{O(g)} \rightleftharpoons \text{CO}_2\text{(g)} + \text{H}_2\text{(g)}$. Khi hệ đạt trạng thái cân bằng thì thu được $0,6\text{ mol}$ khí $\text{CO}_2$. Tính hằng số cân bằng $K_{\text{C}}$ của phản ứng ở nhiệt độ $T$.",
                answer=["2,25", "2.25"],
                level="vandung",
                solution=r"Vì bình có dung tích $V = 1,0\text{ L}$ nên nồng độ mol bằng số mol. Tại trạng thái cân bằng: $[\text{CO}_2] = [\text{H}_2] = 0,6\text{ M}$; $[\text{CO}] = 1,0 - 0,6 = 0,4\text{ M}$ và $[\text{H}_2\text{O}] = 1,0 - 0,6 = 0,4\text{ M}$. Vậy $K_{\text{C}} = \dfrac{[\text{CO}_2][\text{H}_2]}{[\text{CO}][\text{H}_2\text{O}]} = \dfrac{0,6 \cdot 0,6}{0,4 \cdot 0,4} = 2,25$.",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 3: SỰ ĐIỆN LI, THUYẾT BRØNSTED – LOWRY VÀ pH CỦA DUNG DỊCH
    # =========================================================================
    lesson(
        grade=11,
        order=3,
        code="H11-C03",
        title="Chương 3: Sự điện li, thuyết Brønsted – Lowry và pH của dung dịch",
        topic="su-dien-li",
        description="Chất điện li mạnh, chất điện li yếu, thuyết acid – base của Brønsted – Lowry, tích số ion của nước, độ pH, sự thủy phân của muối và chuẩn độ acid – base.",
        summary=(
            r"Chương học nghiên cứu quá trình điện li của các chất trong nước, phân loại chất điện li mạnh ($\rightarrow$), "
            r"chất điện li yếu ($\rightleftharpoons$) và chất không điện li; định nghĩa acid (chất cho proton $\text{H}^+$), "
            r"base (chất nhận proton $\text{H}^+$) và chất lưỡng tính theo thuyết Brønsted – Lowry; tích số ion của nước "
            r"$K_{\text{w}} = [\text{H}^+][\text{OH}^-] = 10^{-14}$ ở $25^\circ\text{C}$, thang $\text{pH} = -\log[\text{H}^+]$, "
            r"sự thủy phân của các ion trong dung dịch muối và phương pháp chuẩn độ acid – base."
        ),
        objectives=[
            r"Phân biệt được chất điện li mạnh, chất điện li yếu và chất không điện li; viết đúng phương trình điện li bằng mũi tên $\rightarrow$ hoặc $\rightleftharpoons$.",
            r"Phát biểu được thuyết Brønsted – Lowry về acid – base và xác định được vai trò acid, base hoặc lưỡng tính của các phân tử và ion ($\text{NH}_3, \text{NH}_4^+, \text{CO}_3^{2-}, \text{HCO}_3^-, \text{Al(OH)}_3, \text{H}_2\text{O}$).",
            r"Vận dụng được tích số ion của nước $K_{\text{w}} = [\text{H}^+][\text{OH}^-] = 10^{-14}$ ở $25^\circ\text{C}$ và công thức $\text{pH} = -\log[\text{H}^+]$, $\text{pH} + \text{pOH} = 14$ để tính $\text{pH}$ của dung dịch acid, base.",
            r"Giải thích được môi trường của dung dịch muối qua sự thủy phân của các ion và tính toán được nồng độ chất chưa biết trong chuẩn độ acid – base.",
        ],
        formulas=[
            {
                "name": "Tích số ion của nước ở 25 độ C",
                "formula": r"$K_{\text{w}} = [\text{H}^+][\text{OH}^-] = 10^{-14} \quad (\text{ở } 25^\circ\text{C})$",
                "note": r"Trong môi trường trung tính ở $25^\circ\text{C}$: $[\text{H}^+] = [\text{OH}^-] = 10^{-7}\text{ M}$.",
            },
            {
                "name": "Công thức tính pH và pOH của dung dịch",
                "formula": r"$\text{pH} = -\log[\text{H}^+] \iff [\text{H}^+] = 10^{-\text{pH}}; \quad \text{pOH} = -\log[\text{OH}^-]; \quad \text{pH} + \text{pOH} = 14$",
                "note": r"Môi trường acid: $\text{pH} < 7$; môi trường trung tính: $\text{pH} = 7$; môi trường kiềm (base): $\text{pH} > 7$.",
            },
            {
                "name": "Thuyết acid – base của Brønsted – Lowry",
                "formula": r"$\text{Acid (cho H}^+\text{)}: \text{HA} + \text{H}_2\text{O} \rightleftharpoons \text{A}^- + \text{H}_3\text{O}^+; \quad \text{Base (nhận H}^+\text{)}: \text{B} + \text{H}_2\text{O} \rightleftharpoons \text{BH}^+ + \text{OH}^-$",
                "note": r"Các hạt vừa có khả năng cho $\text{H}^+$ vừa có khả năng nhận $\text{H}^+$ như $\text{HCO}_3^-, \text{HS}^-, \text{H}_2\text{PO}_4^-, \text{Al(OH)}_3, \text{H}_2\text{O}$ là chất lưỡng tính.",
            },
            {
                "name": "Điều kiện tương đương trong chuẩn độ đơn acid mạnh bằng đơn base mạnh",
                "formula": r"$n_{\text{H}^+} = n_{\text{OH}^-} \iff C_{\text{A}} \cdot V_{\text{A}} = C_{\text{B}} \cdot V_{\text{B}}$",
                "note": r"Áp dụng cho chuẩn độ dung dịch $\text{HCl}$ bằng dung dịch $\text{NaOH}$ chuẩn với chỉ thị phenolphthalein.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Sự điện li, chất điện li mạnh và chất điện li yếu",
                "content": (
                    r"Sự điện li là quá trình phân li các chất trong nước tạo thành các ion, giúp dung dịch dẫn được điện. "
                    r"Các hợp chất cộng hóa trị không phân cực hoặc ít phân cực như saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), "
                    r"ethanol ($\text{C}_2\text{H}_5\text{OH}$) khi tan trong nước không phân li ra ion nên là chất không điện li. "
                    r"Chất điện li mạnh là chất khi tan trong nước, các phân tử hòa tan đều phân li hoàn toàn ra ion (biểu diễn bằng mũi tên $\rightarrow$), "
                    r"bao gồm các acid mạnh ($\text{HCl}, \text{HBr}, \text{HI}, \text{HNO}_3, \text{H}_2\text{SO}_4, \text{HClO}_4$), "
                    r"các base mạnh ($\text{NaOH}, \text{KOH}, \text{Ca(OH)}_2, \text{Ba(OH)}_2$) và hầu hết các muối tan. "
                    r"Chất điện li yếu là chất khi tan trong nước chỉ có một phần số phân tử hòa tan phân li ra ion, phần còn lại tồn tại ở dạng phân tử "
                    r"(biểu diễn bằng mũi tên thuận nghịch $\rightleftharpoons$), bao gồm các acid yếu ($\text{CH}_3\text{COOH}, \text{HF}, \text{H}_2\text{CO}_3, \text{H}_2\text{S}, \text{HClO}$) "
                    r"và base yếu ($\text{NH}_3$, các hydroxide không tan)."
                ),
            },
            {
                "title": "2. Thuyết acid – base của Brønsted – Lowry",
                "content": (
                    r"Theo thuyết Brønsted – Lowry: Acid là chất cho proton ($\text{H}^+$) và base là chất nhận proton ($\text{H}^+$). "
                    r"Định nghĩa này mở rộng cho cả các phân tử và các ion:\n"
                    r"- Các acid Brønsted: $\text{HCl}, \text{CH}_3\text{COOH}, \text{NH}_4^+, \text{Al(H}_2\text{O)}_6^{3+}, \text{Fe(H}_2\text{O)}_6^{3+}, \text{HSO}_4^-$.\n"
                    r"- Các base Brønsted: $\text{OH}^-, \text{NH}_3, \text{CO}_3^{2-}, \text{S}^{2-}, \text{CH}_3\text{COO}^-, \text{PO}_4^{3-}$.\n"
                    r"- Các chất/ion lưỡng tính (vừa cho $\text{H}^+$ vừa nhận $\text{H}^+$): $\text{HCO}_3^-, \text{HSO}_3^-, \text{HS}^-, \text{H}_2\text{PO}_4^-, \text{HPO}_4^{2-}, \text{Al(OH)}_3, \text{Zn(OH)}_2, \text{H}_2\text{O}$."
                ),
            },
            {
                "title": "3. Tích số ion của nước, pH và sự thủy phân của các ion trong dung dịch muối",
                "content": (
                    r"Nước là chất điện li rất yếu: $\text{H}_2\text{O} \rightleftharpoons \text{H}^+ + \text{OH}^-$. Ở $25^\circ\text{C}$, tích số ion của nước là "
                    r"$K_{\text{w}} = [\text{H}^+][\text{OH}^-] = 10^{-14}$. Độ acid hay kiềm của dung dịch được đánh giá qua đại lượng "
                    r"$\text{pH} = -\log[\text{H}^+]$ và $\text{pOH} = -\log[\text{OH}^-]$ với $\text{pH} + \text{pOH} = 14$. "
                    r"Trong dung dịch muối: (1) Muối tạo bởi cation của base mạnh và anion gốc acid mạnh (như $\text{NaCl}, \text{K}_2\text{SO}_4$) không bị thủy phân, có $\text{pH} = 7$; "
                    r"(2) Muối tạo bởi cation của base yếu và anion gốc acid mạnh (như $\text{NH}_4\text{Cl}, \text{AlCl}_3, \text{Fe}_2(\text{SO}_4)_3$) có cation bị thủy phân cho $\text{H}^+$ nên $\text{pH} < 7$ (đất chua chứa nhiều $\text{Al}^{3+}, \text{Fe}^{3+}$ được khử chua bằng vôi $\text{CaO}$ hoặc $\text{Ca(OH)}_2$); "
                    r"(3) Muối tạo bởi cation của base mạnh và anion gốc acid yếu (như $\text{Na}_2\text{CO}_3, \text{CH}_3\text{COONa}$) có anion nhận $\text{H}^+$ từ nước giải phóng $\text{OH}^-$ nên $\text{pH} > 7$."
                ),
            },
            {
                "title": "4. Chuẩn độ acid – base",
                "content": (
                    r"Chuẩn độ là phương pháp xác định nồng độ của một chất bằng một dung dịch chuẩn đã biết chính xác nồng độ. "
                    r"Khi chuẩn độ dung dịch $\text{HCl}$ chưa biết nồng độ bằng dung dịch chuẩn $\text{NaOH}$ với chất chỉ thị phenolphthalein, "
                    r"điểm tương đương đạt được khi $n_{\text{H}^+} = n_{\text{OH}^-}$, nhận biết tại thời điểm dung dịch trong bình tam giác "
                    r"vừa chuyển từ không màu sang màu hồng nhạt bền trong khoảng $20\text{ s}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Tính $\text{pH}$ của dung dịch acid mạnh và base mạnh",
                "problem": (
                    r"Tính $\text{pH}$ của các dung dịch sau ở $25^\circ\text{C}$: "
                    r"a) Dung dịch $\text{H}_2\text{SO}_4\text{ } 0,005\text{ M}$ (coi phân li hoàn toàn cả 2 nấc); "
                    r"b) Dung dịch $\text{Ba(OH)}_2\text{ } 0,005\text{ M}$."
                ),
                "solution": (
                    r"a) Phương trình điện li: $\text{H}_2\text{SO}_4 \rightarrow 2\text{H}^+ + \text{SO}_4^{2-}$. "
                    r"Suy ra $[\text{H}^+] = 2 \cdot 0,005 = 0,01\text{ M} = 10^{-2}\text{ M} \implies \text{pH} = -\log(10^{-2}) = 2,0$. "
                    r"b) Phương trình điện li: $\text{Ba(OH)}_2 \rightarrow \text{Ba}^{2+} + 2\text{OH}^-$. "
                    r"Suy ra $[\text{OH}^-] = 2 \cdot 0,005 = 0,01\text{ M} = 10^{-2}\text{ M} \implies \text{pOH} = -\log(10^{-2}) = 2,0 \implies \text{pH} = 14 - 2,0 = 12,0$."
                ),
            },
            {
                "title": r"Ví dụ 2: Bài toán trộn dung dịch acid mạnh với base mạnh",
                "problem": (
                    r"Trộn $200\text{ mL}$ dung dịch $\text{HCl}\text{ } 0,15\text{ M}$ với $300\text{ mL}$ dung dịch $\text{NaOH}\text{ } 0,10\text{ M}$ ở $25^\circ\text{C}$. "
                    r"Tính $\text{pH}$ của dung dịch thu được sau khi trộn."
                ),
                "solution": (
                    r"Số mol $\text{H}^+$ ban đầu: $n_{\text{H}^+} = 0,2 \cdot 0,15 = 0,03\text{ mol}$. "
                    r"Số mol $\text{OH}^-$ ban đầu: $n_{\text{OH}^-} = 0,3 \cdot 0,10 = 0,03\text{ mol}$. "
                    r"Phản ứng trung hòa: $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$. Vì $n_{\text{H}^+} = n_{\text{OH}^-} = 0,03\text{ mol}$ nên hai chất phản ứng vừa đủ với nhau, môi trường thu được trung tính có $\text{pH} = 7,0$."
                ),
            },
        ],
        key_takeaways=[
            r"Theo thuyết Brønsted – Lowry: Acid là chất cho proton $\text{H}^+$, base là chất nhận proton $\text{H}^+$, chất lưỡng tính vừa cho vừa nhận $\text{H}^+$.",
            r"Ở $25^\circ\text{C}$: $[\text{H}^+][\text{OH}^-] = 10^{-14}$ và $\text{pH} + \text{pOH} = 14$; khi biết $[\text{OH}^-]$ của dung dịch kiềm, ta tính $\text{pOH} = -\log[\text{OH}^-]$ rồi suy ra $\text{pH} = 14 - \text{pOH}$.",
            r"Dung dịch muối $\text{NH}_4^+, \text{Al}^{3+}, \text{Fe}^{3+}$ có môi trường acid ($\text{pH} < 7$); dung dịch muối $\text{CO}_3^{2-}, \text{PO}_4^{3-}, \text{CH}_3\text{COO}^-$ có môi trường kiềm ($\text{pH} > 7$).",
            r"Tại điểm tương đương của phép chuẩn độ acid – base: tổng số mol $\text{H}^+$ phản ứng bằng tổng số mol $\text{OH}^-$.",
        ],
        questions=[
            mcq(
                question=r"Chất nào dưới đây là chất điện li YẾU khi tan trong nước?",
                options=[
                    r"Hydrochloric acid ($\text{HCl}$)",
                    r"Sodium hydroxide ($\text{NaOH}$)",
                    r"Acetic acid ($\text{CH}_3\text{COOH}$)",
                    r"Potassium nitrate ($\text{KNO}_3$)",
                ],
                answer="C",
                level="biet",
                solution=r"$\text{HCl}$ (acid mạnh), $\text{NaOH}$ (base mạnh) và $\text{KNO}_3$ (muối tan) đều là chất điện li mạnh. $\text{CH}_3\text{COOH}$ là acid hữu cơ yếu, chỉ phân li một phần trong nước ($\text{CH}_3\text{COOH} \rightleftharpoons \text{CH}_3\text{COO}^- + \text{H}^+$) nên là chất điện li yếu.",
            ),
            mcq(
                question=r"Theo thuyết acid – base của Brønsted – Lowry, phát biểu nào sau đây là ĐÚNG?",
                options=[
                    r"Acid là chất nhận proton ($\text{H}^+$), base là chất cho proton ($\text{H}^+$)",
                    r"Acid là chất cho proton ($\text{H}^+$), base là chất nhận proton ($\text{H}^+$)",
                    r"Base phải là hợp chất có chứa nhóm $\text{OH}^-$ trong công thức phân tử",
                    r"Chỉ các phân tử trung hòa mới có thể đóng vai trò là acid hoặc base",
                ],
                answer="B",
                level="biet",
                solution=r"Theo thuyết Brønsted – Lowry, acid là chất cho proton ($\text{H}^+$) và base là chất nhận proton ($\text{H}^+$); cả phân tử lẫn ion đều có thể là acid, base hoặc chất lưỡng tính.",
            ),
            mcq(
                question=r"Theo thuyết Brønsted – Lowry, ion nào dưới đây là chất LƯỠNG TÍNH trong dung dịch nước?",
                options=[
                    r"Ion carbonate ($\text{CO}_3^{2-}$)",
                    r"Ion ammonium ($\text{NH}_4^+$)",
                    r"Ion hydrogencarbonate ($\text{HCO}_3^-$)",
                    r"Ion chloride ($\text{Cl}^-$)",
                ],
                answer="C",
                level="biet",
                solution=r"Ion $\text{HCO}_3^-$ vừa có thể cho proton $\text{H}^+$ ($\text{HCO}_3^- + \text{H}_2\text{O} \rightleftharpoons \text{CO}_3^{2-} + \text{H}_3\text{O}^+$), vừa có thể nhận proton $\text{H}^+$ ($\text{HCO}_3^- + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3 + \text{OH}^-$) nên là ion lưỡng tính.",
            ),
            mcq(
                question=r"Ở $25^\circ\text{C}$, một dung dịch có nồng độ $[\text{H}^+] = 1,0 \cdot 10^{-3}\text{ M}$. Giá trị $\text{pH}$ và môi trường của dung dịch này là:",
                options=[
                    r"$\text{pH} = 3$, môi trường acid",
                    r"$\text{pH} = 11$, môi trường kiềm",
                    r"$\text{pH} = 3$, môi trường kiềm",
                    r"$\text{pH} = 7$, môi trường trung tính",
                ],
                answer="A",
                level="biet",
                solution=r"Ta có $\text{pH} = -\log[\text{H}^+] = -\log(1,0 \cdot 10^{-3}) = 3$. Vì $\text{pH} = 3 < 7$ nên dung dịch có môi trường acid.",
            ),
            mcq(
                question=r"Ở $25^\circ\text{C}$, giá trị $\text{pH}$ của dung dịch $\text{Ba(OH)}_2\text{ } 0,005\text{ M}$ là:",
                options=[
                    r"$\text{pH} = 2,0$",
                    r"$\text{pH} = 11,7$",
                    r"$\text{pH} = 12,0$",
                    r"$\text{pH} = 12,3$",
                ],
                answer="C",
                level="hieu",
                solution=r"$\text{Ba(OH)}_2$ là base mạnh có $2$ nhóm $\text{OH}^-$: $\text{Ba(OH)}_2 \rightarrow \text{Ba}^{2+} + 2\text{OH}^-$. Suy ra $[\text{OH}^-] = 2 \cdot 0,005 = 0,01\text{ M} = 10^{-2}\text{ M}$. Vậy $\text{pOH} = -\log(10^{-2}) = 2,0 \implies \text{pH} = 14 - 2,0 = 12,0$.",
            ),
            mcq(
                question=r"Dãy gồm các muối khi hòa tan vào nước đều bị thủy phân tạo môi trường có $\text{pH} < 7$ (làm quỳ tím hóa đỏ) là:",
                options=[
                    r"$\text{Na}_2\text{CO}_3, \text{CH}_3\text{COONa}, \text{K}_2\text{S}$",
                    r"$\text{NH}_4\text{Cl}, \text{AlCl}_3, \text{Fe}_2(\text{SO}_4)_3$",
                    r"$\text{NaCl}, \text{KNO}_3, \text{Na}_2\text{SO}_4$",
                    r"$\text{NaHCO}_3, \text{K}_3\text{PO}_4, \text{BaCl}_2$",
                ],
                answer="B",
                level="hieu",
                solution=r"Các muối $\text{NH}_4\text{Cl}, \text{AlCl}_3, \text{Fe}_2(\text{SO}_4)_3$ tạo bởi cation của base yếu ($\text{NH}_4^+, \text{Al}^{3+}, \text{Fe}^{3+}$) và anion của acid mạnh ($\text{Cl}^-, \text{SO}_4^{2-}$). Trong nước, các cation này thủy phân cho $\text{H}^+$ tạo môi trường acid có $\text{pH} < 7$.",
            ),
            tf4(
                stem=r"Trong dung dịch nước, ammonia phản ứng thuận nghịch với nước theo phương trình: $\text{NH}_3\text{(aq)} + \text{H}_2\text{O(l)} \rightleftharpoons \text{NH}_4^+\text{(aq)} + \text{OH}^-\text{(aq)}$. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Trong phản ứng thuận, phân tử $\text{NH}_3$ nhận proton $\text{H}^+$ từ $\text{H}_2\text{O}$ nên $\text{NH}_3$ đóng vai trò là một base theo thuyết Brønsted – Lowry.",
                    r"b) Trong phản ứng thuận, phân tử $\text{H}_2\text{O}$ đóng vai trò là một base theo thuyết Brønsted – Lowry.",
                    r"c) Dung dịch $\text{NH}_3$ có $[\text{OH}^-] > 10^{-7}\text{ M}$ (ở $25^\circ\text{C}$), có $\text{pH} > 7$ và làm phenolphthalein chuyển sang màu hồng.",
                    r"d) $\text{NH}_3$ là chất điện li mạnh nên nồng độ $[\text{OH}^-]$ tại cân bằng luôn bằng nồng độ mol ban đầu của $\text{NH}_3$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: $\text{NH}_3$ nhận $\text{H}^+$ từ $\text{H}_2\text{O}$ để tạo thành $\text{NH}_4^+$ nên $\text{NH}_3$ là một base Brønsted. "
                    r"b) Sai: Trong phản ứng thuận, $\text{H}_2\text{O}$ nhường proton $\text{H}^+$ cho $\text{NH}_3$ nên $\text{H}_2\text{O}$ đóng vai trò là một acid Brønsted. "
                    r"c) Đúng: Quá trình phân li tạo ra ion $\text{OH}^-$ làm $[\text{OH}^-] > 10^{-7}\text{ M}$, $\text{pH} > 7$ và làm phenolphthalein hóa hồng. "
                    r"d) Sai: $\text{NH}_3$ là một base yếu, chỉ một phần nhỏ phân tử $\text{NH}_3$ tác dụng với nước tạo $\text{OH}^-$ nên $[\text{OH}^-] < C_{\text{NH}_3}$ ban đầu."
                ),
            ),
            tf4(
                stem=r"Một học sinh tiến hành chuẩn độ $20,0\text{ mL}$ dung dịch $\text{HCl}$ chưa biết nồng độ (đặt trong bình tam giác có nhỏ $2$ giọt phenolphthalein) bằng dung dịch chuẩn $\text{NaOH}\text{ } 0,10\text{ M}$ (nạp trên burette). Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Phản ứng bản chất ion thu gọn diễn ra trong quá trình chuẩn độ là $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$.",
                    r"b) Trước khi nhỏ dung dịch $\text{NaOH}$ từ burette xuống, dung dịch $\text{HCl}$ và phenolphthalein trong bình tam giác có màu hồng đậm.",
                    r"c) Điểm kết thúc chuẩn độ được xác định khi dung dịch trong bình tam giác vừa chuyển từ không màu sang màu hồng nhạt bền trong khoảng $20\text{ s}$.",
                    r"d) Nếu thể tích dung dịch $\text{NaOH}\text{ } 0,10\text{ M}$ tiêu tốn trung bình là $15,0\text{ mL}$ thì nồng độ của dung dịch $\text{HCl}$ đem chuẩn độ là $0,15\text{ M}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Phản ứng trung hòa giữa acid mạnh $\text{HCl}$ và base mạnh $\text{NaOH}$ có phương trình ion thu gọn là $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$. "
                    r"b) Sai: Trong môi trường acid ($\text{HCl}$), chất chỉ thị phenolphthalein hoàn toàn không màu. "
                    r"c) Đúng: Khi một giọt $\text{NaOH}$ vừa dư sau điểm tương đương, phenolphthalein chuyển sang màu hồng nhạt bền trong khoảng $20\text{ s}$, báo hiệu dừng chuẩn độ. "
                    r"d) Sai: Áp dụng $C_{\text{HCl}} \cdot V_{\text{HCl}} = C_{\text{NaOH}} \cdot V_{\text{NaOH}} \implies C_{\text{HCl}} = \dfrac{0,10 \cdot 15,0}{20,0} = 0,075\text{ M}$ (chứ không phải $0,15\text{ M}$)."
                ),
            ),
            mcq(
                question=r"Trộn $100\text{ mL}$ dung dịch $\text{HCl}\text{ } 0,10\text{ M}$ với $100\text{ mL}$ dung dịch $\text{NaOH}\text{ } 0,12\text{ M}$ ở $25^\circ\text{C}$. Biết thể tích dung dịch sau khi trộn bằng $200\text{ mL}$. Giá trị $\text{pH}$ của dung dịch thu được là:",
                options=[
                    r"$\text{pH} = 2,0$",
                    r"$\text{pH} = 7,0$",
                    r"$\text{pH} = 11,0$",
                    r"$\text{pH} = 12,0$",
                ],
                answer="D",
                level="vandung",
                solution=r"Ta có $n_{\text{H}^+} = 0,1 \cdot 0,10 = 0,010\text{ mol}$ và $n_{\text{OH}^-} = 0,1 \cdot 0,12 = 0,012\text{ mol}$. Sau phản ứng $\text{H}^+ + \text{OH}^- \rightarrow \text{H}_2\text{O}$, số mol $\text{OH}^-$ còn dư là $n_{\text{OH}^-\text{(dư)}} = 0,012 - 0,010 = 0,002\text{ mol}$. Nồng độ $[\text{OH}^-]$ sau khi trộn là $[\text{OH}^-] = \dfrac{0,002}{0,200} = 0,01\text{ M} = 10^{-2}\text{ M}$. Suy ra $\text{pOH} = 2,0$ và $\text{pH} = 14 - 2,0 = 12,0$.",
            ),
            short(
                question=r"Để trung hòa hoàn toàn $25,0\text{ mL}$ dung dịch $\text{H}_2\text{SO}_4\text{ } 0,10\text{ M}$ cần dùng vừa đủ $V\text{ mL}$ dung dịch $\text{NaOH}\text{ } 0,20\text{ M}$. Hãy tính giá trị của $V$ (theo đơn vị $\text{mL}$).",
                answer=["25", "25,0", "25.0"],
                level="vandung",
                solution=r"Số mol $\text{H}^+$ trong $25,0\text{ mL}$ dung dịch $\text{H}_2\text{SO}_4\text{ } 0,10\text{ M}$ là $n_{\text{H}^+} = 2 \cdot n_{\text{H}_2\text{SO}_4} = 2 \cdot 0,025 \cdot 0,10 = 0,005\text{ mol}$. Để trung hòa vừa đủ cần $n_{\text{OH}^-} = n_{\text{H}^+} = 0,005\text{ mol} \implies V_{\text{NaOH}} = \dfrac{0,005}{0,20} = 0,025\text{ L} = 25\text{ mL}$.",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 4: NITROGEN, AMMONIA, MUỐI AMMONIUM VÀ HỢP CHẤT CHỨA NITROGEN
    # =========================================================================
    lesson(
        grade=11,
        order=4,
        code="H11-C04",
        title="Chương 4: Nitrogen, Ammonia, Muối Ammonium và Hợp chất chứa Nitrogen",
        topic="nitrogen-ammonia",
        description="Cấu tạo và tính chất của đơn chất nitrogen, ammonia, muối ammonium, hiện tượng phú dưỡng, các oxide của nitrogen và nitric acid.",
        summary=(
            r"Chương học khám phá đơn chất nitrogen $\text{N}_2$ với liên kết ba $\text{N}\equiv\text{N}$ siêu bền ($E_{\text{b}} = 945\text{ kJ/mol}$), "
            r"cấu tạo hình chóp tam giác cùng tính base yếu và tính khử của ammonia $\text{NH}_3$, tính chất dễ tan – dễ bị nhiệt phân – phản ứng với kiềm "
            r"của muối ammonium $\text{NH}_4^+$, nguyên nhân và hệ lụy của hiện tượng phú dưỡng, tác hại mưa acid từ $\text{NO}_x$ "
            r"và tính acid mạnh kèm tính oxi hóa rất mạnh của nitric acid $\text{HNO}_3$."
        ),
        objectives=[
            r"Giải thích được tính trơ của đơn chất $\text{N}_2$ ở nhiệt độ thường dựa vào năng lượng liên kết ba $\text{N}\equiv\text{N}$ lớn và chứng minh $\text{N}_2$ vừa có tính oxi hóa vừa có tính khử ở nhiệt độ cao.",
            r"Mô tả được cấu tạo phân tử $\text{NH}_3$, giải thích độ tan lớn của $\text{NH}_3$ trong nước và viết các phương trình chứng minh tính base yếu, tính khử của $\text{NH}_3$ cũng như tính chất của muối $\text{NH}_4^+$.",
            r"Trình bày được nguyên nhân, hậu quả và biện pháp hạn chế hiện tượng phú dưỡng (dư thừa dinh dưỡng chứa $\text{N}, \text{P}$) và mưa acid do khí thải $\text{NO}_x$.",
            r"Vận dụng được tính chất acid mạnh và tính oxi hóa rất mạnh của $\text{HNO}_3$ để giải quyết các bài toán kim loại tác dụng với $\text{HNO}_3$.",
        ],
        formulas=[
            {
                "name": "Chuỗi chuyển hóa từ nitrogen đến nitric acid (Quy trình Haber – Bosch và Ostwald)",
                "formula": r"$\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3; \quad 4\text{NH}_3 + 5\text{O}_2 \xrightarrow{\text{Pt, } 850^\circ\text{C}} 4\text{NO} + 6\text{H}_2\text{O}; \quad 2\text{NO} + \text{O}_2 \rightarrow 2\text{NO}_2; \quad 4\text{NO}_2 + \text{O}_2 + 2\text{H}_2\text{O} \rightarrow 4\text{HNO}_3$",
                "note": r"Khi có tia lửa điện sấm sét ($\approx 3000^\circ\text{C}$), $\text{N}_2 + \text{O}_2 \rightleftharpoons 2\text{NO}$ khởi đầu quá trình tạo đạm nitrate tự nhiên.",
            },
            {
                "name": "Phản ứng nhận biết ion ammonium bằng dung dịch kiềm",
                "formula": r"$\text{NH}_4^+ + \text{OH}^- \xrightarrow{t^\circ} \text{NH}_3\uparrow + \text{H}_2\text{O}$",
                "note": r"Khí $\text{NH}_3\uparrow$ thoát ra có mùi khai đặc trưng và làm giấy quỳ tím ẩm chuyển sang màu xanh.",
            },
            {
                "name": "Phản ứng của đồng với dung dịch nitric acid đặc và loãng",
                "formula": r"$\text{Cu} + 4\text{HNO}_3\text{(đặc)} \rightarrow \text{Cu(NO}_3)_2 + 2\text{NO}_2\uparrow + 2\text{H}_2\text{O}; \quad 3\text{Cu} + 8\text{HNO}_3\text{(loãng)} \rightarrow 3\text{Cu(NO}_3)_2 + 2\text{NO}\uparrow + 4\text{H}_2\text{O}$",
                "note": r"$\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong dung dịch $\text{HNO}_3$ đặc, nguội.",
            },
            {
                "name": "Định luật bảo toàn electron và công thức số mol HNO3 phản ứng với kim loại",
                "formula": r"$\sum n \cdot n_{\text{KL}} = 1 \cdot n_{\text{NO}_2} + 3 \cdot n_{\text{NO}} + 8 \cdot n_{\text{N}_2\text{O}} + 10 \cdot n_{\text{N}_2} + 8 \cdot n_{\text{NH}_4\text{NO}_3}; \quad n_{\text{HNO}_3\text{(pư)}} = 2n_{\text{NO}_2} + 4n_{\text{NO}} + 10n_{\text{N}_2\text{O}} + 12n_{\text{N}_2} + 10n_{\text{NH}_4\text{NO}_3}$",
                "note": r"Áp dụng giải nhanh các bài toán hòa tan hoàn toàn kim loại trong dung dịch $\text{HNO}_3$.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Đơn chất nitrogen (N2)",
                "content": (
                    r"Nguyên tử nitrogen ($Z = 7$, cấu hình electron $1s^22s^22p^3$) thuộc chu kỳ 2, nhóm VA. Phân tử $\text{N}_2$ có liên kết ba "
                    r"$\text{N}\equiv\text{N}$ cộng hóa trị không phân cực rất bền vững với năng lượng liên kết lớn ($E_{\text{b}} = 945\text{ kJ/mol}$), "
                    r"do đó ở nhiệt độ thường $\text{N}_2$ rất trơ về mặt hóa học (dùng làm khí quyển bảo quản thực phẩm, mẫu sinh học). "
                    r"Ở nhiệt độ cao hoặc có xúc tác, tia lửa điện, $\text{N}_2$ trở nên hoạt động hơn và thể hiện cả tính oxi hóa "
                    r"(tác dụng với $\text{H}_2$ tạo $\text{NH}_3$, tác dụng với $\text{Li}$ ngay ở nhiệt độ thường tạo $\text{Li}_3\text{N}$, với $\text{Mg}$ ở nhiệt độ cao tạo $\text{Mg}_3\text{N}_2$) "
                    r"lẫn tính khử (tác dụng với $\text{O}_2$ ở khoảng $3000^\circ\text{C}$ hoặc hồ quang điện tạo $\text{NO}$ không màu, sau đó $\text{NO}$ hóa nâu ngay trong không khí tạo $\text{NO}_2$)."
                ),
            },
            {
                "title": "2. Ammonia (NH3) và muối ammonium (NH4+)",
                "content": (
                    r"Phân tử $\text{NH}_3$ có cấu tạo hình chóp tam giác với cặp electron hóa trị riêng trên nguyên tử $\text{N}$, phân cực mạnh "
                    r"và tạo được liên kết hydrogen liên phân tử với nước nên $\text{NH}_3$ tan rất nhiều trong nước. "
                    r"Về hóa tính, $\text{NH}_3$ có: (1) Tính base yếu ($\text{NH}_3 + \text{H}_2\text{O} \rightleftharpoons \text{NH}_4^+ + \text{OH}^-$, làm quỳ tím ẩm hóa xanh, "
                    r"tác dụng với acid tạo muối ammonium và kết tủa các hydroxide kim loại như $\text{AlCl}_3 + 3\text{NH}_3 + 3\text{H}_2\text{O} \rightarrow \text{Al(OH)}_3\downarrow + 3\text{NH}_4\text{Cl}$); "
                    r"(2) Tính khử (do nguyên tử $\text{N}$ có số oxi hóa $-3$ thấp nhất, khi đốt trong $\text{O}_2$ cháy tạo $\text{N}_2 + \text{H}_2\text{O}$, nếu có xúc tác $\text{Pt}$ ở $850^\circ\text{C}$ tạo $\text{NO} + \text{H}_2\text{O}$). "
                    r"Các muối ammonium ($\text{NH}_4\text{Cl}, \text{NH}_4\text{NO}_3, (\text{NH}_4)_2\text{SO}_4, \text{NH}_4\text{HCO}_3$) đều dễ tan trong nước, là chất điện li mạnh, "
                    r"kém bền nhiệt (dễ bị nhiệt phân như $\text{NH}_4\text{Cl} \xrightarrow{t^\circ} \text{NH}_3\uparrow + \text{HCl}\uparrow$, $\text{NH}_4\text{NO}_2 \xrightarrow{t^\circ} \text{N}_2\uparrow + 2\text{H}_2\text{O}$) "
                    r"và tác dụng với dung dịch kiềm giải phóng khí $\text{NH}_3\uparrow$."
                ),
            },
            {
                "title": "3. Hiện tượng phú dưỡng, các oxide của nitrogen và nitric acid (HNO3)",
                "content": (
                    r"Hiện tượng phú dưỡng xảy ra khi nguồn nước ao, hồ bị dư thừa các chất dinh dưỡng chứa nitrogen ($\text{NO}_3^-, \text{NH}_4^+$) "
                    r"và phosphorus ($\text{PO}_4^{3-}$) từ phân bón nông nghiệp dư thừa và nước thải chưa xử lý, làm rong tảo phát triển bùng nổ "
                    r"che kín mặt nước, ngăn ánh sáng và làm suy giảm nghiêm trọng lượng oxygen hòa tan khiến thủy sinh vật chết hàng loạt. "
                    r"Các oxide $\text{NO}_x$ ($\text{NO}, \text{NO}_2$) sinh ra từ sấm sét và khí thải động cơ đốt trong là tác nhân gây mưa acid và mù quang hóa. "
                    r"Nitric acid ($\text{HNO}_3$, trong đó $\text{N}$ có số oxi hóa $+5$) vừa là một acid mạnh, vừa là một chất oxi hóa rất mạnh: "
                    r"oxi hóa được hầu hết kim loại (kể cả $\text{Cu}, \text{Ag}$, trừ $\text{Au}, \text{Pt}$) lên mức oxi hóa cao nhất và giải phóng các sản phẩm khử "
                    r"($\text{NO}_2, \text{NO}, \text{N}_2\text{O}, \text{N}_2, \text{NH}_4\text{NO}_3$) chứ không giải phóng $\text{H}_2$. Đặc biệt, $\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong $\text{HNO}_3$ đặc, nguội."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Giải thích hiện tượng tạo đạm tự nhiên khi có sấm chớp",
                "problem": (
                    r"Giải thích câu ca dao: Lúa chiêm lấp ló đầu bờ, hễ nghe tiếng sấm phất cờ mà lên bằng các phương trình hóa học."
                ),
                "solution": (
                    r"Khi có sấm sét (tia lửa điện ở khoảng $3000^\circ\text{C}$), $\text{N}_2$ và $\text{O}_2$ trong không khí hóa hợp tạo thành $\text{NO}$: "
                    r"$\text{N}_2\text{(g)} + \text{O}_2\text{(g)} \stackrel{3000^\circ\text{C}}{\rightleftharpoons} 2\text{NO(g)}$. "
                    r"Ngay ở điều kiện thường, $\text{NO}$ kết hợp với $\text{O}_2$ tạo khí $\text{NO}_2$ màu nâu đỏ: $2\text{NO(g)} + \text{O}_2\text{(g)} \rightarrow 2\text{NO}_2\text{(g)}$. "
                    r"Khí $\text{NO}_2$ tan vào nước mưa cùng với $\text{O}_2$ tạo thành nitric acid: $4\text{NO}_2\text{(g)} + \text{O}_2\text{(g)} + 2\text{H}_2\text{O(l)} \rightarrow 4\text{HNO}_3\text{(aq)}$. "
                    r"$\text{HNO}_3$ theo nước mưa rơi xuống đất cung cấp ion dinh dưỡng $\text{NO}_3^-$ giúp lúa phát triển nhanh."
                ),
            },
            {
                "title": r"Ví dụ 2: Bảo toàn electron trong bài toán kim loại tác dụng với $\text{HNO}_3$",
                "problem": (
                    r"Hòa tan hoàn toàn $m\text{ gam}$ bột $\text{Cu}$ ($M = 64\text{ g/mol}$) vào dung dịch $\text{HNO}_3$ loãng dư, thu được $2,479\text{ L}$ khí $\text{NO}$ "
                    r"(sản phẩm khử duy nhất ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$). Tính giá trị của $m$ và số mol $\text{HNO}_3$ đã phản ứng."
                ),
                "solution": (
                    r"Số mol khí $\text{NO}$ ở điều kiện chuẩn là $n_{\text{NO}} = \dfrac{2,479}{24,79} = 0,10\text{ mol}$. "
                    r"Áp dụng bảo toàn electron: $2 \cdot n_{\text{Cu}} = 3 \cdot n_{\text{NO}} = 3 \cdot 0,10 = 0,30\text{ mol} \implies n_{\text{Cu}} = 0,15\text{ mol}$. "
                    r"Khối lượng đồng đã phản ứng là $m = 0,15 \cdot 64 = 9,6\text{ g}$. "
                    r"Tổng số mol $\text{HNO}_3$ đã phản ứng là $n_{\text{HNO}_3} = 4 \cdot n_{\text{NO}} = 4 \cdot 0,10 = 0,40\text{ mol}$."
                ),
            },
        ],
        key_takeaways=[
            r"Phân tử $\text{N}_2$ có liên kết ba $\text{N}\equiv\text{N}$ rất bền nên trơ ở nhiệt độ thường; ở nhiệt độ cao $\text{N}_2$ vừa có tính oxi hóa vừa có tính khử.",
            r"Phân tử $\text{NH}_3$ có cấu tạo hình chóp tam giác, tan rất tốt trong nước, thể hiện tính base yếu và tính khử.",
            r"Muối ammonium $\text{NH}_4^+$ dễ tan, dễ bị nhiệt phân và tác dụng với dung dịch kiềm đun nóng giải phóng khí $\text{NH}_3\uparrow$ làm xanh quỳ tím ẩm.",
            r"$\text{HNO}_3$ là acid mạnh và chất oxi hóa rất mạnh; $\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong $\text{HNO}_3$ đặc, nguội.",
        ],
        questions=[
            mcq(
                question=r"Nguyên nhân chính khiến đơn chất khí nitrogen ($\text{N}_2$) rất trơ về mặt hóa học ở nhiệt độ thường là:",
                options=[
                    r"Nguyên tử nitrogen có bán kính nguyên tử lớn nhất trong nhóm VA",
                    r"Phân tử $\text{N}_2$ có liên kết ba $\text{N}\equiv\text{N}$ không phân cực với năng lượng liên kết rất lớn ($945\text{ kJ/mol}$)",
                    r"Phân tử $\text{N}_2$ tan rất nhiều trong nước và tạo liên kết hydrogen mạnh",
                    r"Nguyên tử nitrogen trong phân tử $\text{N}_2$ đã đạt số oxi hóa tối đa là $+5$",
                ],
                answer="B",
                level="biet",
                solution=r"Phân tử $\text{N}_2$ chứa liên kết ba cộng hóa trị không phân cực $\text{N}\equiv\text{N}$ có năng lượng liên kết rất lớn ($E_{\text{b}} = 945\text{ kJ/mol}$), rất khó bị phá vỡ ở nhiệt độ thường.",
            ),
            mcq(
                question=r"Nhóm các kim loại đều bị THỤ ĐỘNG HÓA trong dung dịch $\text{HNO}_3$ đặc, nguội là:",
                options=[
                    r"$\text{Cu}, \text{Ag}, \text{Zn}$",
                    r"$\text{Al}, \text{Fe}, \text{Cr}$",
                    r"$\text{Mg}, \text{Ca}, \text{Ba}$",
                    r"$\text{Na}, \text{K}, \text{Cu}$",
                ],
                answer="B",
                level="biet",
                solution=r"Ba kim loại $\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong dung dịch $\text{HNO}_3$ đặc, nguội (và $\text{H}_2\text{SO}_4$ đặc, nguội) do tạo lớp màng oxide bền bảo vệ bề mặt.",
            ),
            mcq(
                question=r"Để nhận biết các ion ammonium ($\text{NH}_4^+$) trong dung dịch phân đạm, người ta đun nóng mẫu thử với dung dịch kiềm ($\text{NaOH}$ hoặc $\text{KOH}$) vì phản ứng giải phóng:",
                options=[
                    r"Khí $\text{N}_2$ không màu, không mùi",
                    r"Khí $\text{NO}_2$ màu nâu đỏ, mùi hắc",
                    r"Khí $\text{NH}_3$ có mùi khai và làm giấy quỳ tím ẩm hóa xanh",
                    r"Kết tủa trắng không tan trong acid",
                ],
                answer="C",
                level="biet",
                solution=r"Khi đun nóng muối ammonium với dung dịch kiềm xảy ra phản ứng $\text{NH}_4^+ + \text{OH}^- \xrightarrow{t^\circ} \text{NH}_3\uparrow + \text{H}_2\text{O}$. Khí $\text{NH}_3$ thoát ra có mùi khai đặc trưng và làm quỳ tím ẩm hóa xanh.",
            ),
            mcq(
                question=r"Hiện tượng phú dưỡng ở các ao, hồ chủ yếu do sự dư thừa quá mức của các nguyên tố dinh dưỡng nào trong nước?",
                options=[
                    r"Sodium ($\text{Na}$) và Chlorine ($\text{Cl}$)",
                    r"Nitrogen ($\text{N}$) và Phosphorus ($\text{P}$)",
                    r"Calcium ($\text{Ca}$) và Magnesium ($\text{Mg}$)",
                    r"Iron ($\text{Fe}$) và Copper ($\text{Cu}$)",
                ],
                answer="B",
                level="biet",
                solution=r"Hiện tượng phú dưỡng xảy ra khi nước ao, hồ tích tụ quá nhiều chất dinh dưỡng chứa nitrogen ($\text{NO}_3^-, \text{NH}_4^+$) và phosphorus ($\text{PO}_4^{3-}$), làm tảo phát triển bùng phát và gây thiếu hụt oxygen trong nước.",
            ),
            mcq(
                question=r"Trong phản ứng tổng hợp ammonia $\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightleftharpoons 2\text{NH}_3\text{(g)}$ và phản ứng phóng điện $\text{N}_2\text{(g)} + \text{O}_2\text{(g)} \rightleftharpoons 2\text{NO(g)}$, đơn chất $\text{N}_2$ đóng vai trò lần lượt là:",
                options=[
                    r"Chất oxi hóa và chất khử",
                    r"Chất khử và chất oxi hóa",
                    r"Chất oxi hóa trong cả hai phản ứng",
                    r"Chất khử trong cả hai phản ứng",
                ],
                answer="A",
                level="hieu",
                solution=r"Khi tác dụng với $\text{H}_2$, số oxi hóa của $\text{N}$ giảm từ $0$ xuống $-3$ (trong $\text{NH}_3$) nên $\text{N}_2$ là chất oxi hóa. Khi tác dụng với $\text{O}_2$, số oxi hóa của $\text{N}$ tăng từ $0$ lên $+2$ (trong $\text{NO}$) nên $\text{N}_2$ là chất khử.",
            ),
            mcq(
                question=r"Nhỏ từ từ đến dư dung dịch $\text{NH}_3$ vào ống nghiệm chứa dung dịch $\text{AlCl}_3$. Hiện tượng quan sát được là:",
                options=[
                    r"Không có kết tủa xuất hiện",
                    r"Xuất hiện kết tủa keo trắng $\text{Al(OH)}_3$, sau đó kết tủa tan hoàn toàn trong $\text{NH}_3$ dư",
                    r"Xuất hiện kết tủa keo trắng $\text{Al(OH)}_3$ tăng dần đến cực đại và kết tủa không tan trong dung dịch $\text{NH}_3$ dư",
                    r"Xuất hiện kết tủa màu nâu đỏ và có khí màu nâu thoát ra",
                ],
                answer="C",
                level="hieu",
                solution=r"Dung dịch $\text{NH}_3$ là một base yếu, phản ứng với $\text{AlCl}_3$ theo phương trình $\text{AlCl}_3 + 3\text{NH}_3 + 3\text{H}_2\text{O} \rightarrow \text{Al(OH)}_3\downarrow + 3\text{NH}_4\text{Cl}$. Vì $\text{Al(OH)}_3$ không tan trong dung dịch base yếu $\text{NH}_3$ và không tạo phức với $\text{NH}_3$ nên kết tủa keo trắng không bị hòa tan khi $\text{NH}_3$ dư.",
            ),
            tf4(
                stem=r"Ammonia ($\text{NH}_3$) là một trong những hóa chất cơ bản quan trọng bậc nhất của công nghiệp phân bón và hóa chất. Xét tính đúng/sai của các phát biểu sau về $\text{NH}_3$ và muối ammonium:",
                statements=[
                    r"a) Phân tử $\text{NH}_3$ có cấu tạo hình chóp tam giác, phân cực mạnh và tạo được liên kết hydrogen với nước nên tan rất nhiều trong nước.",
                    r"b) Khi đốt cháy khí $\text{NH}_3$ trong khí $\text{O}_2$ không có chất xúc tác, sản phẩm thu được là khí $\text{NO}$ và $\text{H}_2\text{O}$.",
                    r"c) Muối $\text{NH}_4\text{HCO}_3$ dễ bị nhiệt phân tạo các chất khí $\text{NH}_3, \text{CO}_2, \text{H}_2\text{O}$ nên được ứng dụng làm bột nở trong chế biến thực phẩm.",
                    r"d) Để khử chua đất trồng trọt, người ta nên trộn trực tiếp phân đạm ammonium như $(\text{NH}_4)_2\text{SO}_4$ hoặc $\text{NH}_4\text{NO}_3$ với vôi bột $\text{CaO}$ trước khi bón.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: $\text{NH}_3$ có hình chóp tam giác, nguyên tử $\text{N}$ còn cặp electron chưa liên kết, tạo liên kết hydrogen với $\text{H}_2\text{O}$ nên tan cực tốt trong nước. "
                    r"b) Sai: Khi đốt $\text{NH}_3$ trong $\text{O}_2$ không có xúc tác thì tạo $\text{N}_2$ và $\text{H}_2\text{O}$ ($4\text{NH}_3 + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{N}_2 + 6\text{H}_2\text{O}$); chỉ khi có xúc tác $\text{Pt}$ ở $850^\circ\text{C}$ mới tạo $\text{NO}$. "
                    r"c) Đúng: $\text{NH}_4\text{HCO}_3 \xrightarrow{t^\circ} \text{NH}_3\uparrow + \text{CO}_2\uparrow + \text{H}_2\text{O}\uparrow$ tạo các lỗ xốp giúp bánh phồng xốp. "
                    r"d) Sai: Trộn phân đạm ammonium với vôi ($\text{CaO}$ tạo môi trường kiềm $\text{OH}^-$) sẽ xảy ra phản ứng $2\text{NH}_4^+ + \text{Ca(OH)}_2 \rightarrow \text{Ca}^{2+} + 2\text{NH}_3\uparrow + 2\text{H}_2\text{O}$ làm thất thoát đạm dưới dạng khí $\text{NH}_3$."
                ),
            ),
            tf4(
                stem=r"Một học sinh cho một mảnh kim loại đồng ($\text{Cu}$) vào ống nghiệm chứa dung dịch $\text{HNO}_3$ đặc. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Mảnh đồng tan dần, dung dịch chuyển sang màu xanh lam của $\text{Cu(NO}_3)_2$ và có khí $\text{NO}_2$ màu nâu đỏ thoát ra.",
                    r"b) Trong phản ứng trên, toàn bộ lượng $\text{HNO}_3$ tham gia phản ứng đều đóng vai trò là chất oxi hóa.",
                    r"c) Để hạn chế khí độc $\text{NO}_2$ thoát ra ngoài phòng thí nghiệm, ta cần nút miệng ống nghiệm bằng bông tẩm dung dịch kiềm $\text{NaOH}$.",
                    r"d) Nếu thay mảnh $\text{Cu}$ bằng một lá $\text{Al}$ sạch và dùng dung dịch $\text{HNO}_3$ đặc, nguội thì khí $\text{NO}_2$ sẽ thoát ra mạnh hơn.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Phương trình phản ứng là $\text{Cu} + 4\text{HNO}_3\text{(đặc)} \rightarrow \text{Cu(NO}_3)_2 + 2\text{NO}_2\uparrow + 2\text{H}_2\text{O}$. "
                    r"b) Sai: Trong $4\text{ mol}$ $\text{HNO}_3$ phản ứng chỉ có $2\text{ mol}$ đóng vai trò chất oxi hóa (tạo $2\text{ mol}$ $\text{NO}_2$) và $2\text{ mol}$ đóng vai trò môi trường acid (tạo muối $\text{Cu(NO}_3)_2$). "
                    r"c) Đúng: Khí $\text{NO}_2$ bị hấp thụ bởi dung dịch $\text{NaOH}$ theo phương trình $2\text{NO}_2 + 2\text{NaOH} \rightarrow \text{NaNO}_3 + \text{NaNO}_2 + \text{H}_2\text{O}$. "
                    r"d) Sai: $\text{Al}$ bị thụ động hóa trong dung dịch $\text{HNO}_3$ đặc, nguội nên không xảy ra phản ứng."
                ),
            ),
            mcq(
                question=r"Hòa tan hoàn toàn $19,2\text{ g}$ kim loại $\text{Cu}$ ($M = 64\text{ g/mol}$) vào dung dịch $\text{HNO}_3$ dư, thu được $7,437\text{ L}$ hỗn hợp khí $\text{X}$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$) gồm hai khí $\text{NO}$ và $\text{NO}_2$ (không còn sản phẩm khử nào khác). Số mol khí $\text{NO}$ và $\text{NO}_2$ trong hỗn hợp $\text{X}$ lần lượt là:",
                options=[
                    r"$0,10\text{ mol}$ và $0,20\text{ mol}$",
                    r"$0,15\text{ mol}$ và $0,15\text{ mol}$",
                    r"$0,20\text{ mol}$ và $0,10\text{ mol}$",
                    r"$0,12\text{ mol}$ và $0,18\text{ mol}$",
                ],
                answer="B",
                level="vandung",
                solution=r"Ta có $n_{\text{Cu}} = \dfrac{19,2}{64} = 0,30\text{ mol}$ và tổng số mol khí $n_{\text{X}} = \dfrac{7,437}{24,79} = 0,30\text{ mol}$. Gọi $x, y$ lần lượt là số mol của $\text{NO}$ và $\text{NO}_2$. Theo tổng số mol khí: $x + y = 0,30$. Theo bảo toàn electron: $3x + y = 2 \cdot n_{\text{Cu}} = 2 \cdot 0,30 = 0,60$. Giải hệ phương trình thu được $x = 0,15\text{ mol}$ và $y = 0,15\text{ mol}$.",
            ),
            short(
                question=r"Hòa tan hoàn toàn $m\text{ gam}$ bột $\text{Cu}$ ($M = 64\text{ g/mol}$) vào dung dịch $\text{HNO}_3$ loãng dư thì thu được $4,958\text{ L}$ khí $\text{NO}$ (sản phẩm khử duy nhất ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$). Tính giá trị của $m$ (theo đơn vị $\text{gam}$).",
                answer=["19,2", "19.2"],
                level="vandung",
                solution=r"Số mol khí $\text{NO}$ thoát ra ở điều kiện chuẩn là $n_{\text{NO}} = \dfrac{4,958}{24,79} = 0,20\text{ mol}$. Áp dụng định luật bảo toàn electron: $2 \cdot n_{\text{Cu}} = 3 \cdot n_{\text{NO}} = 3 \cdot 0,20 = 0,60\text{ mol} \implies n_{\text{Cu}} = 0,30\text{ mol}$. Vậy khối lượng đồng đã phản ứng là $m = 0,30 \cdot 64 = 19,2\text{ g}$.",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 5: SULFUR, SULFUR DIOXIDE, SULFURIC ACID VÀ MUỐI SULFATE
    # =========================================================================
    lesson(
        grade=11,
        order=5,
        code="H11-C05",
        title="Chương 5: Sulfur, Sulfur dioxide, Sulfuric acid và Muối Sulfate",
        topic="sulfuric-acid",
        description="Tính chất của đơn chất lưu huỳnh, sulfur dioxide, quy tắc pha loãng và tính chất của sulfuric acid loãng và đặc, quy trình tiếp xúc và nhận biết muối sulfate.",
        summary=(
            r"Chương học trình bày tính chất vật lý và hóa học của đơn chất lưu huỳnh $\text{S}$, khí sulfur dioxide $\text{SO}_2$ "
            r"(oxide acid vừa có tính oxi hóa vừa có tính khử, tác nhân chính gây mưa acid), quy tắc an toàn khi pha loãng $\text{H}_2\text{SO}_4$ đặc "
            r"(rót từ từ acid vào nước), sự khác biệt giữa $\text{H}_2\text{SO}_4$ loãng và $\text{H}_2\text{SO}_4$ đặc (tính oxi hóa mạnh và tính háo nước), "
            r"quy trình tiếp xúc sản xuất $\text{H}_2\text{SO}_4$ qua 3 giai đoạn và cách nhận biết ion $\text{SO}_4^{2-}$ bằng dung dịch muối $\text{Ba}^{2+}$."
        ),
        objectives=[
            r"Trình bày được cấu tạo, tính chất vật lý và chứng minh đơn chất lưu huỳnh $\text{S}$ vừa có tính oxi hóa vừa có tính khử (ứng dụng thu hồi thủy ngân $\text{Hg}$ rơi vãi).",
            r"Giải thích được tính chất vừa oxi hóa vừa khử của $\text{SO}_2$ (số oxi hóa $+4$ trung gian), nguyên nhân gây mưa acid và các biện pháp giảm thiểu phát thải $\text{SO}_2$.",
            r"Nêu được quy tắc an toàn khi pha loãng $\text{H}_2\text{SO}_4$ đặc; so sánh và viết được phương trình minh họa tính acid mạnh của $\text{H}_2\text{SO}_4$ loãng với tính oxi hóa mạnh, tính háo nước của $\text{H}_2\text{SO}_4$ đặc.",
            r"Trình bày được 3 giai đoạn của phương pháp tiếp xúc sản xuất $\text{H}_2\text{SO}_4$ (tạo oleum $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$), ứng dụng của các muối sulfate và nhận biết ion $\text{SO}_4^{2-}$ bằng kết tủa trắng $\text{BaSO}_4\downarrow$.",
        ],
        formulas=[
            {
                "name": "Ba giai đoạn sản xuất sulfuric acid theo phương pháp tiếp xúc",
                "formula": r"$(1)\text{ }\text{S} + \text{O}_2 \xrightarrow{t^\circ} \text{SO}_2\text{ (hoặc } 4\text{FeS}_2 + 11\text{O}_2 \xrightarrow{t^\circ} 2\text{Fe}_2\text{O}_3 + 8\text{SO}_2\text{)}; \quad (2)\text{ } 2\text{SO}_2 + \text{O}_2 \underset{450^\circ\text{C}}{\stackrel{\text{V}_2\text{O}_5}{\rightleftharpoons}} 2\text{SO}_3; \quad (3)\text{ }\text{H}_2\text{SO}_4\text{(đặc)} + n\text{SO}_3 \rightarrow \text{H}_2\text{SO}_4\cdot n\text{SO}_3$",
                "note": r"Pha loãng oleum bằng nước thu được $\text{H}_2\text{SO}_4$: $\text{H}_2\text{SO}_4\cdot n\text{SO}_3 + n\text{H}_2\text{O} \rightarrow (n+1)\text{H}_2\text{SO}_4$.",
            },
            {
                "name": "So sánh phản ứng của sắt với H2SO4 loãng và H2SO4 đặc, nóng dư",
                "formula": r"$\text{Fe} + \text{H}_2\text{SO}_4\text{(loãng)} \rightarrow \text{FeSO}_4 + \text{H}_2\uparrow; \quad 2\text{Fe} + 6\text{H}_2\text{SO}_4\text{(đặc, nóng)} \rightarrow \text{Fe}_2(\text{SO}_4)_3 + 3\text{SO}_2\uparrow + 6\text{H}_2\text{O}$",
                "note": r"$\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong dung dịch $\text{H}_2\text{SO}_4$ đặc, nguội.",
            },
            {
                "name": "Tính háo nước của H2SO4 đặc làm than hóa saccharose",
                "formula": r"$\text{C}_{12}\text{H}_{22}\text{O}_{11} \xrightarrow{\text{H}_2\text{SO}_4\text{ đặc}} 12\text{C} + 11\text{H}_2\text{O}; \quad \text{C} + 2\text{H}_2\text{SO}_4\text{(đặc)} \xrightarrow{t^\circ} \text{CO}_2\uparrow + 2\text{SO}_2\uparrow + 2\text{H}_2\text{O}$",
                "note": r"Khối than đen xốp bị khí $\text{CO}_2$ và $\text{SO}_2$ đẩy phồng trào lên miệng cốc.",
            },
            {
                "name": "Phản ứng nhận biết ion sulfate trong dung dịch",
                "formula": r"$\text{Ba}^{2+} + \text{SO}_4^{2-} \rightarrow \text{BaSO}_4\downarrow\text{ (kết tủa trắng)}$",
                "note": r"Kết tủa $\text{BaSO}_4\downarrow$ màu trắng, bền và không tan trong các dung dịch acid mạnh ($\text{HCl}, \text{HNO}_3$).",
            },
        ],
        theory_sections=[
            {
                "title": "1. Đơn chất lưu huỳnh (S) và sulfur dioxide (SO2)",
                "content": (
                    r"Nguyên tử lưu huỳnh ($Z = 16$, cấu hình electron $[\text{Ne}]3s^23p^4$) thuộc chu kỳ 3, nhóm VIA, có các số oxi hóa phổ biến là "
                    r"$-2, 0, +4, +6$. Đơn chất $\text{S}$ là chất rắn màu vàng, không tan trong nước, vừa có tính oxi hóa (tác dụng với $\text{H}_2$ và nhiều kim loại ở nhiệt độ cao; "
                    r"riêng với thủy ngân $\text{Hg}$ phản ứng xảy ra ngay ở nhiệt độ thường: $\text{Hg} + \text{S} \rightarrow \text{HgS}$, được dùng để thu gom thủy ngân rơi vãi), "
                    r"vừa có tính khử (cháy trong $\text{O}_2$ tạo $\text{SO}_2$). "
                    r"Khí sulfur dioxide ($\text{SO}_2$) là chất khí không màu, mùi hắc, độc, là một acidic oxide. Do $\text{S}$ trong $\text{SO}_2$ có số oxi hóa $+4$ trung gian "
                    r"nên $\text{SO}_2$ vừa có tính khử (làm mất màu dung dịch nước bromine: $\text{SO}_2 + \text{Br}_2 + 2\text{H}_2\text{O} \rightarrow 2\text{HBr} + \text{H}_2\text{SO}_4$ "
                    r"và dung dịch $\text{KMnO}_4$), vừa có tính oxi hóa ($\text{SO}_2 + 2\text{H}_2\text{S} \rightarrow 3\text{S}\downarrow + 2\text{H}_2\text{O}$). "
                    r"$\text{SO}_2$ cùng với $\text{NO}_x$ là nguyên nhân chính gây ra hiện tượng mưa acid ($\text{pH} < 5,6$)."
                ),
            },
            {
                "title": "2. Sulfuric acid (H2SO4): Quy tắc pha loãng và tính chất hóa học",
                "content": (
                    r"Dung dịch $\text{H}_2\text{SO}_4$ đặc là chất lỏng sánh như dầu, không bay hơi, rất háo nước và khi tan trong nước tỏa lượng nhiệt rất lớn. "
                    r"Vì vậy, khi pha loãng $\text{H}_2\text{SO}_4$ đặc, BẮT BUỘC phải rót từ từ acid vào nước và khuấy nhẹ bằng đũa thủy tinh, "
                    r"TUYỆT ĐỐI KHÔNG rót nước vào acid đặc để tránh nước sôi đột ngột làm bắn acid gây bỏng nặng.\n"
                    r"- Dung dịch $\text{H}_2\text{SO}_4$ loãng thể hiện tính chất của một acid mạnh điển hình (do ion $\text{H}^+$): làm quỳ tím hóa đỏ, tác dụng với base, basic oxide, muối và tác dụng với các kim loại đứng trước $\text{H}$ giải phóng khí $\text{H}_2\uparrow$ (với $\text{Fe}$ chỉ lên $\text{Fe}^{2+}$).\n"
                    r"- Dung dịch $\text{H}_2\text{SO}_4$ đặc có tính oxi hóa rất mạnh (do $\text{S}^{+6}$) và tính háo nước: oxi hóa hầu hết kim loại (kể cả $\text{Cu}, \text{Ag}$, trừ $\text{Au}, \text{Pt}$) lên số oxi hóa cao nhất tạo muối sulfate và sản phẩm khử ($\text{SO}_2, \text{S}, \text{H}_2\text{S}$), cũng như oxi hóa nhiều phi kim ($\text{C}, \text{S}, \text{P}$); riêng $\text{Al}, \text{Fe}, \text{Cr}$ bị thụ động hóa trong $\text{H}_2\text{SO}_4$ đặc, nguội."
                ),
            },
            {
                "title": "3. Sản xuất H2SO4 và muối sulfate",
                "content": (
                    r"Trong công nghiệp, $\text{H}_2\text{SO}_4$ được sản xuất bằng phương pháp tiếp xúc qua 3 giai đoạn: "
                    r"(1) Đốt lưu huỳnh hoặc quặng pyrite ($\text{FeS}_2$) tạo $\text{SO}_2$; "
                    r"(2) Oxi hóa $\text{SO}_2$ bằng $\text{O}_2$ với xúc tác $\text{V}_2\text{O}_5$ ở khoảng $450^\circ\text{C}$ tạo $\text{SO}_3$; "
                    r"(3) Dùng $\text{H}_2\text{SO}_4$ đặc $98\%$ hấp thụ $\text{SO}_3$ thu được oleum $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$, sau đó pha loãng oleum bằng lượng nước thích hợp. "
                    r"Các muối sulfate có nhiều ứng dụng quan trọng như $(\text{NH}_4)_2\text{SO}_4$ làm phân đạm, $\text{CaSO}_4 \cdot \text{H}_2\text{O}$ (thạch cao nung) dùng đúc tượng và bó bột y tế, "
                    r"$\text{MgSO}_4$ dùng làm thuốc, $\text{BaSO}_4$ dùng làm chất cản quang. Để nhận biết ion $\text{SO}_4^{2-}$, ta dùng dung dịch chứa ion $\text{Ba}^{2+}$ ($\text{BaCl}_2, \text{Ba(NO}_3)_2, \text{Ba(OH)}_2$) tạo kết tủa trắng $\text{BaSO}_4\downarrow$ không tan trong acid."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Kim loại tác dụng với dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng",
                "problem": (
                    r"Hòa tan hoàn toàn $12,8\text{ g}$ kim loại $\text{Cu}$ ($M = 64\text{ g/mol}$) vào dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng dư. "
                    r"Tính thể tích khí $\text{SO}_2$ (sản phẩm khử duy nhất ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$) và số mol $\text{H}_2\text{SO}_4$ đã phản ứng."
                ),
                "solution": (
                    r"Số mol đồng là $n_{\text{Cu}} = \dfrac{12,8}{64} = 0,20\text{ mol}$. "
                    r"Phương trình hóa học: $\text{Cu} + 2\text{H}_2\text{SO}_4\text{(đặc, nóng)} \rightarrow \text{CuSO}_4 + \text{SO}_2\uparrow + 2\text{H}_2\text{O}$. "
                    r"Theo phương trình: $n_{\text{SO}_2} = n_{\text{Cu}} = 0,20\text{ mol} \implies V_{\text{SO}_2} = 0,20 \cdot 24,79 = 4,958\text{ L}$. "
                    r"Số mol $\text{H}_2\text{SO}_4$ đã tham gia phản ứng là $n_{\text{H}_2\text{SO}_4} = 2 \cdot n_{\text{Cu}} = 0,40\text{ mol}$."
                ),
            },
            {
                "title": r"Ví dụ 2: Xác định công thức của oleum $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$",
                "problem": (
                    r"Hòa tan hoàn toàn $8,45\text{ g}$ một loại oleum $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$ vào nước, thu được dung dịch $\text{X}$. "
                    r"Để trung hòa hết dung dịch $\text{X}$ cần dùng vừa đủ $200\text{ mL}$ dung dịch $\text{NaOH}\text{ } 1,0\text{ M}$. Xác định giá trị của $n$ và công thức oleum."
                ),
                "solution": (
                    r"Khi hòa tan vào nước: $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3 + n\text{H}_2\text{O} \rightarrow (n+1)\text{H}_2\text{SO}_4$. "
                    r"Số mol $\text{NaOH}$ phản ứng là $n_{\text{NaOH}} = 0,2 \cdot 1,0 = 0,20\text{ mol} \implies n_{\text{H}_2\text{SO}_4} = \dfrac{1}{2}n_{\text{NaOH}} = 0,10\text{ mol}$. "
                    r"Suy ra số mol oleum là $\dfrac{0,10}{n+1}\text{ mol}$. Ta có phương trình khối lượng: "
                    r"$\dfrac{0,10}{n+1} \cdot (98 + 80n) = 8,45 \implies 9,8 + 8n = 8,45n + 8,45 \implies 0,45n = 1,35 \implies n = 3$. "
                    r"Vậy công thức của oleum là $\text{H}_2\text{SO}_4 \cdot 3\text{SO}_3$."
                ),
            },
        ],
        key_takeaways=[
            r"Bột lưu huỳnh $\text{S}$ phản ứng với thủy ngân $\text{Hg}$ ngay ở nhiệt độ thường tạo $\text{HgS}$ rắn, dùng để xử lý khi vỡ nhiệt kế thủy ngân.",
            r"Khí $\text{SO}_2$ vừa có tính khử (làm mất màu dung dịch $\text{Br}_2, \text{KMnO}_4$) vừa có tính oxi hóa (tác dụng với $\text{H}_2\text{S}$ tạo kết tủa vàng $\text{S}\downarrow$).",
            r"Khi pha loãng $\text{H}_2\text{SO}_4$ đặc, bắt buộc rót từ từ acid vào nước và khuấy đều, tuyệt đối không rót nước vào acid đặc.",
            r"Nhận biết ion $\text{SO}_4^{2-}$ bằng dung dịch muối $\text{Ba}^{2+}$ tạo kết tủa trắng $\text{BaSO}_4\downarrow$ không tan trong acid mạnh.",
        ],
        questions=[
            mcq(
                question=r"Khi chẳng may làm vỡ nhiệt kế thủy ngân trong phòng thí nghiệm, người ta rắc ngay hóa chất nào sau đây lên các giọt thủy ngân ($\text{Hg}$) rơi vãi để thu gom chúng ở dạng hợp chất bền không bay hơi?",
                options=[
                    r"Muối ăn ($\text{NaCl}$)",
                    r"Cát sạch ($\text{SiO}_2$)",
                    r"Bột lưu huỳnh ($\text{S}$)",
                    r"Bột đá vôi ($\text{CaCO}_3$)",
                ],
                answer="C",
                level="biet",
                solution=r"Đơn chất lưu huỳnh ($\text{S}$) phản ứng trực tiếp với thủy ngân lỏng ($\text{Hg}$) ngay ở nhiệt độ thường tạo thành muối rắn $\text{HgS}$ không bay hơi: $\text{Hg} + \text{S} \rightarrow \text{HgS}$.",
            ),
            mcq(
                question=r"Thao tác nào sau đây là ĐÚNG và an toàn tuyệt đối khi pha loãng dung dịch $\text{H}_2\text{SO}_4$ đặc trong phòng thí nghiệm?",
                options=[
                    r"Rót nhanh nước cất vào cốc đựng sẵn dung dịch $\text{H}_2\text{SO}_4$ đặc",
                    r"Rót từ từ dung dịch $\text{H}_2\text{SO}_4$ đặc dọc theo đũa thủy tinh vào cốc nước và khuấy nhẹ đều",
                    r"Rót từ từ nước cất dọc theo đũa thủy tinh vào bình đựng $\text{H}_2\text{SO}_4$ đặc và đậy kín nút",
                    r"Đun sôi dung dịch $\text{H}_2\text{SO}_4$ đặc rồi đổ nước lạnh vào",
                ],
                answer="B",
                level="biet",
                solution=r"Do $\text{H}_2\text{SO}_4$ đặc có khối lượng riêng lớn và tỏa nhiệt rất mạnh khi hòa tan, ta phải rót từ từ acid đặc vào nước và khuấy đều để nhiệt phân tán an toàn.",
            ),
            mcq(
                question=r"Để nhận biết sự có mặt của ion sulfate ($\text{SO}_4^{2-}$) trong dung dịch $\text{H}_2\text{SO}_4$ hoặc muối sulfate, thuốc thử đặc trưng được sử dụng là:",
                options=[
                    r"Dung dịch $\text{AgNO}_3$",
                    r"Dung dịch $\text{BaCl}_2$ (hoặc $\text{Ba(NO}_3)_2$) trong môi trường acid",
                    r"Dung dịch $\text{NaOH}$",
                    r"Dung dịch $\text{HCl}$",
                ],
                answer="B",
                level="biet",
                solution=r"Ion $\text{Ba}^{2+}$ phản ứng với ion $\text{SO}_4^{2-}$ tạo kết tủa màu trắng $\text{BaSO}_4\downarrow$ không tan trong các dung dịch acid mạnh ($\text{Ba}^{2+} + \text{SO}_4^{2-} \rightarrow \text{BaSO}_4\downarrow$).",
            ),
            mcq(
                question=r"Trong công nghiệp, giai đoạn hấp thụ khí $\text{SO}_3$ của quy trình tiếp xúc sản xuất sulfuric acid được thực hiện bằng cách dùng dung dịch $\text{H}_2\text{SO}_4\text{ } 98\%$ để thu được:",
                options=[
                    r"Dung dịch $\text{H}_2\text{SO}_3$ loãng",
                    r"Oleum có công thức chung $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$",
                    r"Khí $\text{H}_2\text{S}$ tinh khiết",
                    r"Tinh thể muối $\text{FeSO}_4 \cdot 7\text{H}_2\text{O}$",
                ],
                answer="B",
                level="biet",
                solution=r"Nếu dùng nước hấp thụ trực tiếp $\text{SO}_3$ sẽ tạo mù $\text{H}_2\text{SO}_4$ rất khó ngưng tụ, nên người ta dùng $\text{H}_2\text{SO}_4\text{ } 98\%$ hấp thụ $\text{SO}_3$ tạo oleum $\text{H}_2\text{SO}_4 \cdot n\text{SO}_3$.",
            ),
            mcq(
                question=r"Cho hai phản ứng hóa học của khí sulfur dioxide ($\text{SO}_2$): $(1)\text{ }\text{SO}_2 + \text{Br}_2 + 2\text{H}_2\text{O} \rightarrow 2\text{HBr} + \text{H}_2\text{SO}_4$ và $(2)\text{ }\text{SO}_2 + 2\text{H}_2\text{S} \rightarrow 3\text{S}\downarrow + 2\text{H}_2\text{O}$. Vai trò của $\text{SO}_2$ trong phản ứng $(1)$ và $(2)$ lần lượt là:",
                options=[
                    r"Chất oxi hóa và chất khử",
                    r"Chất khử và chất oxi hóa",
                    r"Chất khử trong cả hai phản ứng",
                    r"Chất oxi hóa trong cả hai phản ứng",
                ],
                answer="B",
                level="hieu",
                solution=r"Ở phản ứng $(1)$, số oxi hóa của $\text{S}$ trong $\text{SO}_2$ tăng từ $+4$ lên $+6$ (trong $\text{H}_2\text{SO}_4$) nên $\text{SO}_2$ là chất khử. Ở phản ứng $(2)$, số oxi hóa của $\text{S}$ trong $\text{SO}_2$ giảm từ $+4$ xuống $0$ (trong $\text{S}$) nên $\text{SO}_2$ là chất oxi hóa.",
            ),
            mcq(
                question=r"Cho kim loại sắt ($\text{Fe}$) tác dụng hoàn toàn với: $(1)$ dung dịch $\text{H}_2\text{SO}_4$ loãng dư; $(2)$ dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng dư. Muối sắt thu được trong hai trường hợp $(1)$ và $(2)$ lần lượt là:",
                options=[
                    r"$\text{Fe}_2(\text{SO}_4)_3$ và $\text{FeSO}_4$",
                    r"$\text{FeSO}_4$ và $\text{Fe}_2(\text{SO}_4)_3$",
                    r"$\text{FeSO}_4$ trong cả hai trường hợp",
                    r"$\text{Fe}_2(\text{SO}_4)_3$ trong cả hai trường hợp",
                ],
                answer="B",
                level="hieu",
                solution=r"Với $\text{H}_2\text{SO}_4$ loãng, tính oxi hóa của ion $\text{H}^+$ chỉ đưa $\text{Fe}$ lên số oxi hóa $+2$ tạo $\text{FeSO}_4$ và $\text{H}_2\uparrow$. Với $\text{H}_2\text{SO}_4$ đặc, nóng dư, tính oxi hóa mạnh của $\text{S}^{+6}$ đưa $\text{Fe}$ lên số oxi hóa $+3$ tạo $\text{Fe}_2(\text{SO}_4)_3$ và $\text{SO}_2\uparrow$.",
            ),
            tf4(
                stem=r"Một học sinh thực hiện thí nghiệm nhỏ vài mililit dung dịch $\text{H}_2\text{SO}_4$ đặc ($98\%$) vào cốc thủy tinh chứa khoảng $10\text{ g}$ đường kính trắng saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$). Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Đường trắng chuyển dần sang màu vàng, nâu rồi hóa thành khối than màu đen xốp bị bọt khí đẩy phồng lên miệng cốc.",
                    r"b) Trong thí nghiệm trên, dung dịch $\text{H}_2\text{SO}_4$ đặc chỉ đóng vai trò làm chất xúc tác mà không tham gia phản ứng oxi hóa – khử.",
                    r"c) Khí thoát ra làm đục nước vôi trong và làm mất màu cánh hoa hồng (hoặc dung dịch nước bromine) gồm $\text{CO}_2$ và $\text{SO}_2$.",
                    r"d) Nếu thay dung dịch $\text{H}_2\text{SO}_4$ đặc bằng dung dịch $\text{H}_2\text{SO}_4$ loãng $1\text{ M}$ ở nhiệt độ thường thì hiện tượng than hóa đường vẫn xảy ra tương tự.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: $\text{H}_2\text{SO}_4$ đặc chiếm nước của $\text{C}_{12}\text{H}_{22}\text{O}_{11}$ tạo $\text{C}$ màu đen, đồng thời khí sinh ra đẩy cột than xốp trào lên. "
                    r"b) Sai: Một phần $\text{C}$ sinh ra bị $\text{H}_2\text{SO}_4$ đặc, nóng oxi hóa theo phương trình $\text{C} + 2\text{H}_2\text{SO}_4\text{(đặc)} \rightarrow \text{CO}_2\uparrow + 2\text{SO}_2\uparrow + 2\text{H}_2\text{O}$, nên $\text{H}_2\text{SO}_4$ đặc vừa thể hiện tính háo nước vừa thể hiện tính oxi hóa mạnh. "
                    r"c) Đúng: Hỗn hợp khí gồm $\text{CO}_2$ và $\text{SO}_2$. "
                    r"d) Sai: Dung dịch $\text{H}_2\text{SO}_4$ loãng không có tính háo nước nên không làm than hóa đường saccharose."
                ),
            ),
            tf4(
                stem=r"Xét các tính chất và ứng dụng thực tiễn của hợp chất chứa lưu huỳnh ($\text{SO}_2$, $\text{H}_2\text{SO}_4$ và muối sulfate). Xét tính đúng/sai của các nhận định sau:",
                statements=[
                    r"a) Khí $\text{SO}_2$ sinh ra từ việc đốt nhiên liệu hóa thạch (than đá, dầu mỏ) là một trong những tác nhân chính gây ra hiện tượng mưa acid.",
                    r"b) Trong phòng thí nghiệm, có thể dùng dung dịch $\text{H}_2\text{SO}_4$ đặc để làm khô khí $\text{NH}_3$ ẩm hoặc khí $\text{H}_2\text{S}$ ẩm.",
                    r"c) Người ta có thể dùng bồn chứa bằng thép (hợp kim của $\text{Fe}$) hoặc nhôm ($\text{Al}$) để vận chuyển dung dịch $\text{H}_2\text{SO}_4$ đặc, nguội.",
                    r"d) Muối $\text{BaSO}_4$ tan rất tốt trong dung dịch $\text{HCl}$ trong dạ dày nên được dùng làm thuốc cản quang khi chụp X-quang đường tiêu hóa.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: $\text{SO}_2$ bị oxi hóa trong khí quyển thành $\text{SO}_3$ rồi kết hợp với nước mưa tạo $\text{H}_2\text{SO}_4$ gây mưa acid. "
                    r"b) Sai: $\text{H}_2\text{SO}_4$ đặc phản ứng với $\text{NH}_3$ (tạo muối $(\text{NH}_4)_2\text{SO}_4$) và oxi hóa $\text{H}_2\text{S}$ nên không thể dùng làm khô hai khí này. "
                    r"c) Đúng: $\text{Fe}$ và $\text{Al}$ bị thụ động hóa trong dung dịch $\text{H}_2\text{SO}_4$ đặc, nguội nên không bị ăn mòn. "
                    r"d) Sai: $\text{BaSO}_4$ hoàn toàn không tan trong nước và không tan trong dung dịch $\text{HCl}$ của dịch vị dạ dày nên mới an toàn (không giải phóng ion $\text{Ba}^{2+}$ độc) khi uống làm chất cản quang."
                ),
            ),
            mcq(
                question=r"Hòa tan hoàn toàn $11,9\text{ g}$ hỗn hợp hai kim loại $\text{Al}$ ($M = 27\text{ g/mol}$) và $\text{Zn}$ ($M = 65\text{ g/mol}$) bằng dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng dư thì thu được $8,6765\text{ L}$ khí $\text{SO}_2$ (sản phẩm khử duy nhất ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$). Khối lượng của $\text{Al}$ và $\text{Zn}$ trong hỗn hợp ban đầu lần lượt là:",
                options=[
                    r"$2,7\text{ g}$ và $9,2\text{ g}$",
                    r"$5,4\text{ g}$ và $6,5\text{ g}$",
                    r"$8,1\text{ g}$ và $3,8\text{ g}$",
                    r"$4,05\text{ g}$ và $7,85\text{ g}$",
                ],
                answer="B",
                level="vandung",
                solution=r"Ta có $n_{\text{SO}_2} = \dfrac{8,6765}{24,79} = 0,35\text{ mol}$. Gọi $x, y$ lần lượt là số mol của $\text{Al}$ và $\text{Zn}$. Theo khối lượng hỗn hợp: $27x + 65y = 11,9$. Theo định luật bảo toàn electron: $3x + 2y = 2 \cdot n_{\text{SO}_2} = 2 \cdot 0,35 = 0,70$. Giải hệ thu được $x = 0,20\text{ mol}$ và $y = 0,10\text{ mol}$. Vậy $m_{\text{Al}} = 0,20 \cdot 27 = 5,4\text{ g}$ và $m_{\text{Zn}} = 0,10 \cdot 65 = 6,5\text{ g}$.",
            ),
            short(
                question=r"Hòa tan hoàn toàn $19,2\text{ g}$ kim loại $\text{Cu}$ ($M = 64\text{ g/mol}$) vào dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng dư thì thu được $V\text{ L}$ khí $\text{SO}_2$ (sản phẩm khử duy nhất ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$). Tính giá trị của $V$ (làm tròn đến 2 chữ số thập phân).",
                answer=["7,44", "7.44", "7,437", "7.437"],
                level="vandung",
                solution=r"Số mol $\text{Cu}$ là $n_{\text{Cu}} = \dfrac{19,2}{64} = 0,30\text{ mol}$. Bảo toàn electron: $2 \cdot n_{\text{SO}_2} = 2 \cdot n_{\text{Cu}} \implies n_{\text{SO}_2} = 0,30\text{ mol}$. Thể tích khí $\text{SO}_2$ ở điều kiện chuẩn là $V = 0,30 \cdot 24,79 = 7,437\text{ L} \approx 7,44\text{ L}$.",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 6: ĐẠI CƯƠNG HÓA HỮU CƠ VÀ HYDROCARBON (ALKANE, ALKENE, ALKYNE, ARENE)
    # =========================================================================
    lesson(
        grade=11,
        order=6,
        code="H11-C06",
        title="Chương 6: Đại cương Hóa hữu cơ và Hydrocarbon (Alkane, Alkene, Alkyne, Arene)",
        topic="hydrocarbon-huu-co",
        description="Nhóm chức và phổ hồng ngoại IR, phổ khối lượng MS, đồng đẳng, đồng phân, danh pháp IUPAC và tính chất của alkane, alkene, alkyne, arene.",
        summary=(
            r"Chương học hệ thống hóa kiến thức đại cương hóa học hữu cơ (nhóm chức, phổ hồng ngoại $\text{IR}$, phổ khối lượng $\text{MS}$, "
            r"phương pháp tách và tinh chế, độ bất bão hòa $k$, đồng đẳng, đồng phân cấu tạo và đồng phân hình học *cis–trans*) "
            r"cùng danh pháp thay thế IUPAC và tính chất hóa học trọng tâm của các dãy hydrocarbon: alkane $\text{C}_n\text{H}_{2n+2}$, "
            r"alkene $\text{C}_n\text{H}_{2n}$, alkyne $\text{C}_n\text{H}_{2n-2}$ (quy tắc cộng Markovnikov, phản ứng của alk-1-yne với thuốc thử Tollens) "
            r"và arene $\text{C}_n\text{H}_{2n-6}$ (benzene, toluene, styrene)."
        ),
        objectives=[
            r"Xác định được nhóm chức qua số sóng đặc trưng trên phổ hồng ngoại $\text{IR}$, phân tử khối $M$ qua mảnh ion phân tử $[\text{M}^+]$ trên phổ khối lượng $\text{MS}$ và tính được độ bất bão hòa $k = \dfrac{2x + 2 + t - y}{2}$.",
            r"Viết được các đồng phân cấu tạo, xác định điều kiện có đồng phân hình học *cis–trans* và gọi đúng tên thay thế IUPAC của alkane, alkene, alkyne, arene.",
            r"Trình bày và viết được phương trình hóa học của phản ứng thế halogen, cracking, reforming của alkane; phản ứng cộng theo quy tắc Markovnikov, trùng hợp và oxi hóa bằng $\text{KMnO}_4$ của alkene, alkyne.",
            r"Vận dụng được phản ứng thế ion $\text{Ag}^+$ của alk-1-yne ($\text{R-C}\equiv\text{CH}$) với thuốc thử Tollens $[\text{Ag(NH}_3)_2]\text{OH}$ và tính chất của benzene, toluene để nhận biết và giải bài toán hỗn hợp hydrocarbon.",
        ],
        formulas=[
            {
                "name": "Công thức tính độ bất bão hòa k (tổng số liên kết pi và số vòng)",
                "formula": r"$\text{Hợp chất }\text{C}_x\text{H}_y\text{O}_z\text{N}_t\text{X}_u: \quad k = \pi + v = \dfrac{2x + 2 + t - y - u}{2}$",
                "note": r"Alkane: $\text{C}_n\text{H}_{2n+2}\text{ }(n \ge 1, k = 0)$; Alkene: $\text{C}_n\text{H}_{2n}\text{ }(n \ge 2, k = 1)$; Alkyne: $\text{C}_n\text{H}_{2n-2}\text{ }(n \ge 2, k = 2)$; Alkylbenzene: $\text{C}_n\text{H}_{2n-6}\text{ }(n \ge 6, k = 4)$.",
            },
            {
                "name": "Quy tắc Markovnikov khi cộng HX hoặc HOH vào alkene bất đối xứng",
                "formula": r"$\text{CH}_3\text{-CH=CH}_2 + \text{HBr} \rightarrow \text{CH}_3\text{-CHBr-CH}_3\text{ (sản phẩm chính)} + \text{CH}_3\text{-CH}_2\text{-CH}_2\text{Br}\text{ (sản phẩm phụ)}$",
                "note": r"Nguyên tử $\text{H}$ ưu tiên cộng vào nguyên tử $\text{C}$ mang nối đôi có nhiều $\text{H}$ hơn (bậc thấp hơn), còn $\text{X}$ hoặc $-\text{OH}$ ưu tiên cộng vào $\text{C}$ bậc cao hơn.",
            },
            {
                "name": "Phản ứng đặc trưng của alk-1-yne với thuốc thử Tollens",
                "formula": r"$\text{HC}\equiv\text{CH} + 2[\text{Ag(NH}_3)_2]\text{OH} \rightarrow \text{AgC}\equiv\text{CAg}\downarrow\text{ (vàng nhạt)} + 4\text{NH}_3 + 2\text{H}_2\text{O}; \quad \text{R-C}\equiv\text{CH} + [\text{Ag(NH}_3)_2]\text{OH} \rightarrow \text{R-C}\equiv\text{CAg}\downarrow + 2\text{NH}_3 + \text{H}_2\text{O}$",
                "note": r"Chỉ các alkyne có liên kết ba ở đầu mạch ($\text{R-C}\equiv\text{CH}$) mới có nguyên tử $\text{H}$ linh động bị thế bởi $\text{Ag}^+$.",
            },
            {
                "name": "Phản ứng oxi hóa không hoàn toàn alkene và toluene bằng dung dịch KMnO4",
                "formula": r"$3\text{CH}_2\text{=CH}_2 + 2\text{KMnO}_4 + 4\text{H}_2\text{O} \rightarrow 3\text{HO-CH}_2\text{-CH}_2\text{-OH} + 2\text{MnO}_2\downarrow + 2\text{KOH}; \quad \text{C}_6\text{H}_5\text{CH}_3 + 2\text{KMnO}_4 \xrightarrow{t^\circ} \text{C}_6\text{H}_5\text{COOK} + 2\text{MnO}_2\downarrow + \text{KOH} + \text{H}_2\text{O}$",
                "note": r"Alkene và styrene làm mất màu $\text{KMnO}_4$ ngay ở nhiệt độ thường; toluene làm mất màu $\text{KMnO}_4$ khi đun nóng; benzene không phản ứng.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Đại cương hóa học hữu cơ: Nhóm chức, phổ IR, phổ MS, đồng đẳng và đồng phân",
                "content": (
                    r"Các phương pháp tách biệt và tinh chế hợp chất hữu cơ gồm: chưng cất (dựa vào sự khác nhau về nhiệt độ sôi), "
                    r"chiết (tách các chất lỏng không trộn lẫn hoặc dùng dung môi hòa tan chọn lọc), kết tinh (dựa vào độ tan khác nhau theo nhiệt độ) "
                    r"và sắc ký cột. Trên phổ khối lượng ($\text{MS}$), peak ion phân tử $[\text{M}^+]$ có giá trị $m/z$ lớn nhất cho biết phân tử khối $M$. "
                    r"Trên phổ hồng ngoại ($\text{IR}$), các nhóm chức có vùng số sóng hấp thụ đặc trưng: nhóm $-\text{OH}$ alcohol ở khoảng $3650 \div 3200\text{ cm}^{-1}$ (tù, rộng), "
                    r"nhóm $-\text{NH}_2$ amine ở $3500 \div 3200\text{ cm}^{-1}$, liên kết $\text{C=O}$ của aldehyde/ketone/ester/acid ở khoảng $1750 \div 1680\text{ cm}^{-1}$ (nhọn, mạnh) "
                    r"và nhóm $-\text{OH}$ của carboxylic acid trải rộng ở $3300 \div 2500\text{ cm}^{-1}$. "
                    r"Đồng đẳng là những chất có thành phần phân tử hơn kém nhau một hay nhiều nhóm $-\text{CH}_2-$ và có tính chất hóa học tương tự nhau. "
                    r"Điều kiện để hợp chất chứa liên kết đôi $\text{abC=Ccd}$ có đồng phân hình học *cis–trans* là hai nhóm gắn trên mỗi nguyên tử $\text{C}$ mang nối đôi phải khác nhau: $a \neq b$ và $c \neq d$."
                ),
            },
            {
                "title": "2. Alkane (CnH2n+2, n >= 1)",
                "content": (
                    r"Trong phân tử alkane chỉ chứa các liên kết đơn $\sigma$ ($\text{C-C}$ và $\text{C-H}$) bền vững và hầu như không phân cực. "
                    r"Vì vậy ở nhiệt độ thường alkane không tác dụng với acid, kiềm và dung dịch $\text{KMnO}_4$. "
                    r"Các phản ứng đặc trưng của alkane gồm: (1) Phản ứng thế halogen ($\text{Cl}_2, \text{Br}_2$) khi chiếu sáng hoặc đun nóng, trong đó nguyên tử $\text{H}$ gắn ở nguyên tử $\text{C}$ bậc cao hơn dễ bị thế hơn tạo sản phẩm chính; "
                    r"(2) Phản ứng cracking bẻ gãy mạch carbon dài thành alkane và alkene mạch ngắn hơn; "
                    r"(3) Phản ứng reforming chuyển alkane mạch không phân nhánh thành hydrocarbon mạch nhánh và arene làm tăng chỉ số octane của xăng; "
                    r"(4) Phản ứng cháy tỏa nhiều nhiệt: $\text{C}_n\text{H}_{2n+2} + \dfrac{3n+1}{2}\text{O}_2 \xrightarrow{t^\circ} n\text{CO}_2 + (n+1)\text{H}_2\text{O}$ (với $n_{\text{H}_2\text{O}} > n_{\text{CO}_2}$ và $n_{\text{alkane}} = n_{\text{H}_2\text{O}} - n_{\text{CO}_2}$)."
                ),
            },
            {
                "title": "3. Alkene (CnH2n) và Alkyne (CnH2n-2)",
                "content": (
                    r"Alkene (chứa $1$ liên kết đôi $\text{C=C}$ gồm $1\sigma + 1\pi$) và alkyne (chứa $1$ liên kết ba $\text{C}\equiv\text{C}$ gồm $1\sigma + 2\pi$) "
                    r"có liên kết $\pi$ kém bền nên dễ tham gia phản ứng cộng:\n"
                    r"- Cộng $\text{H}_2$: Xúc tác $\text{Ni}, t^\circ$ chuyển cả alkene và alkyne thành alkane; riêng alkyne khi dùng xúc tác $\text{Pd/PbCO}_3$ (xúc tác Lindlar) chỉ cộng $1$ phân tử $\text{H}_2$ dừng lại ở alkene.\n"
                    r"- Cộng halogen ($\text{Br}_2, \text{Cl}_2$): Cả alkene và alkyne đều làm mất màu nâu đỏ của dung dịch nước bromine.\n"
                    r"- Cộng $\text{HX}$ ($\text{HCl}, \text{HBr}$) và cộng nước $\text{H}_2\text{O}$ (hydrate hóa): Tuân theo quy tắc Markovnikov. Riêng alkyne cộng $\text{H}_2\text{O}$ (xúc tác $\text{HgSO}_4/\text{H}_2\text{SO}_4$ ở $80^\circ\text{C}$) tạo hợp chất trung gian không bền chuyển vị thành aldehyde ($\text{CH}\equiv\text{CH} + \text{H}_2\text{O} \rightarrow \text{CH}_3\text{CHO}$) hoặc ketone.\n"
                    r"- Phản ứng riêng của alk-1-yne ($\text{R-C}\equiv\text{CH}$): Tác dụng với dung dịch $\text{AgNO}_3/\text{NH}_3$ (thuốc thử Tollens) tạo kết tủa màu vàng nhạt ($\text{AgC}\equiv\text{CAg}\downarrow$ hoặc $\text{R-C}\equiv\text{CAg}\downarrow$), dùng để phân biệt alk-1-yne với alkene và các alkyne có nối ba ở giữa mạch."
                ),
            },
            {
                "title": "4. Arene – Hydrocarbon thơm (Benzene, Toluene, Styrene)",
                "content": (
                    r"Benzene ($\text{C}_6\text{H}_6$) có cấu trúc vòng $6$ cạnh đều phẳng với hệ liên hợp $\pi$ bền vững nên thể hiện tính thơm: "
                    r"dễ tham gia phản ứng thế nguyên tử $\text{H}$ của vòng (halogen hóa với $\text{Br}_2/\text{FeBr}_3$, nitro hóa với $\text{HNO}_3\text{ đặc}/\text{H}_2\text{SO}_4\text{ đặc}$), "
                    r"khó tham gia phản ứng cộng (cộng $\text{H}_2$ tạo cyclohexane $\text{C}_6\text{H}_{12}$, cộng $\text{Cl}_2$ khi chiếu sáng tạo $\text{C}_6\text{H}_6\text{Cl}_6$) và bền với chất oxi hóa. "
                    r"Trong phân tử toluene ($\text{C}_6\text{H}_5\text{CH}_3$), nhóm $-\text{CH}_3$ đẩy electron làm vòng benzene hoạt động hơn và ưu tiên thế vào vị trí *ortho* (số $2$) và *para* (số $4$). "
                    r"Đồng thời nhánh $-\text{CH}_3$ của toluene bị oxi hóa bởi dung dịch $\text{KMnO}_4$ khi đun nóng tạo potassium benzoate $\text{C}_6\text{H}_5\text{COOK}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Nhận biết các chất khí Ethane, Ethylene và Acetylene",
                "problem": (
                    r"Trình bày phương pháp hóa học để phân biệt ba chất khí không màu đựng trong ba bình riêng biệt: "
                    r"ethane ($\text{C}_2\text{H}_6$), ethylene ($\text{CH}_2\text{=CH}_2$) và acetylene ($\text{CH}\equiv\text{CH}$)."
                ),
                "solution": (
                    r"Bước 1: Dẫn lần lượt từng khí qua dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ dư (thuốc thử Tollens). "
                    r"Khí nào tạo kết tủa màu vàng nhạt ($\text{AgC}\equiv\text{CAg}\downarrow$) là acetylene ($\text{CH}\equiv\text{CH}$): "
                    r"$\text{HC}\equiv\text{CH} + 2[\text{Ag(NH}_3)_2]\text{OH} \rightarrow \text{AgC}\equiv\text{CAg}\downarrow + 4\text{NH}_3 + 2\text{H}_2\text{O}$. "
                    r"Bước 2: Dẫn hai khí còn lại qua dung dịch nước bromine ($\text{Br}_2$) màu nâu đỏ. Khí nào làm mất màu nâu đỏ của dung dịch $\text{Br}_2$ "
                    r"là ethylene ($\text{CH}_2\text{=CH}_2$): $\text{CH}_2\text{=CH}_2 + \text{Br}_2 \rightarrow \text{BrCH}_2\text{-CH}_2\text{Br}$. "
                    r"Khí còn lại không làm đổi màu dung dịch $\text{Br}_2$ là ethane ($\text{C}_2\text{H}_6$)."
                ),
            },
            {
                "title": r"Ví dụ 2: Bài toán hỗn hợp Propane, Propene và Propyne",
                "problem": (
                    r"Dẫn $6,1975\text{ L}$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$) hỗn hợp khí $\text{X}$ gồm propane ($\text{C}_3\text{H}_8$), "
                    r"propene ($\text{CH}_2\text{=CH-CH}_3$) và propyne ($\text{CH}\equiv\text{C-CH}_3$) lội từ từ qua bình 1 đựng dung dịch $\text{AgNO}_3/\text{NH}_3$ dư "
                    r"thì thu được $14,7\text{ g}$ kết tủa màu vàng. Khí thoát ra khỏi bình 1 được dẫn tiếp qua bình 2 đựng dung dịch $\text{Br}_2$ dư thì thấy có $16,0\text{ g}$ $\text{Br}_2$ phản ứng. "
                    r"Tính số mol mỗi chất trong hỗn hợp $\text{X}$ (cho $\text{C} = 12, \text{H} = 1, \text{Br} = 80, \text{Ag} = 108$)."
                ),
                "solution": (
                    r"Tổng số mol hỗn hợp $\text{X}$ là $n_{\text{X}} = \dfrac{6,1975}{24,79} = 0,25\text{ mol}$. "
                    r"Ở bình 1, chỉ có propyne phản ứng tạo kết tủa vàng $\text{CAg}\equiv\text{C-CH}_3$ ($M = 147\text{ g/mol}$): "
                    r"$n_{\text{propyne}} = n_{\text{kết tủa}} = \dfrac{14,7}{147} = 0,10\text{ mol}$. "
                    r"Ở bình 2, chỉ có propene phản ứng cộng với $\text{Br}_2$ ($M = 160\text{ g/mol}$) theo tỉ lệ $1 : 1$: "
                    r"$n_{\text{propene}} = n_{\text{Br}_2} = \dfrac{16,0}{160} = 0,10\text{ mol}$. "
                    r"Suy ra số mol propane trong hỗn hợp $\text{X}$ là $n_{\text{propane}} = 0,25 - (0,10 + 0,10) = 0,05\text{ mol}$."
                ),
            },
        ],
        key_takeaways=[
            r"Điều kiện có đồng phân hình học *cis–trans* ở liên kết đôi $\text{abC=Ccd}$ là $a \neq b$ và $c \neq d$.",
            r"Quy tắc cộng Markovnikov: nguyên tử $\text{H}$ ưu tiên cộng vào nguyên tử $\text{C}$ mang liên kết bội có nhiều $\text{H}$ hơn (bậc thấp hơn).",
            r"Chỉ các alk-1-yne ($\text{R-C}\equiv\text{CH}$) mới tạo kết tủa màu vàng nhạt với dung dịch $\text{AgNO}_3/\text{NH}_3$.",
            r"Alkene và styrene làm mất màu dung dịch $\text{KMnO}_4$ ở nhiệt độ thường; toluene làm mất màu $\text{KMnO}_4$ khi đun nóng; benzene không làm mất màu $\text{KMnO}_4$.",
        ],
        questions=[
            mcq(
                question=r"Công thức chung của dãy đồng đẳng alkene (hydrocarbon mạch hở có một liên kết đôi $\text{C=C}$) là:",
                options=[
                    r"$\text{C}_n\text{H}_{2n+2}\text{ }(n \ge 1)$",
                    r"$\text{C}_n\text{H}_{2n}\text{ }(n \ge 2)$",
                    r"$\text{C}_n\text{H}_{2n-2}\text{ }(n \ge 2)$",
                    r"$\text{C}_n\text{H}_{2n-6}\text{ }(n \ge 6)$",
                ],
                answer="B",
                level="biet",
                solution=r"Alkene mạch hở có độ bất bão hòa $k = 1$ (chứa $1$ liên kết $\pi$) nên có công thức chung là $\text{C}_n\text{H}_{2n}$ với $n \ge 2$.",
            ),
            mcq(
                question=r"Theo danh pháp thay thế IUPAC, hợp chất có công thức cấu tạo $\text{CH}_3\text{-CH(CH}_3\text{)-CH}_2\text{-CH}_3$ có tên gọi là:",
                options=[
                    r"2-methylbutane",
                    r"3-methylbutane",
                    r"pentane",
                    r"2,2-dimethylpropane",
                ],
                answer="A",
                level="biet",
                solution=r"Mạch chính dài nhất có $4$ nguyên tử $\text{C}$ (butane), đánh số từ đầu gần nhánh $-\text{CH}_3$ hơn nên nhánh methyl ở vị trí số $2$: tên IUPAC là 2-methylbutane.",
            ),
            mcq(
                question=r"Hydrocarbon nào dưới đây tác dụng với dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ (thuốc thử Tollens) tạo ra kết tủa màu vàng nhạt?",
                options=[
                    r"Ethane ($\text{CH}_3\text{-CH}_3$)",
                    r"Ethylene ($\text{CH}_2\text{=CH}_2$)",
                    r"Propyne ($\text{CH}\equiv\text{C-CH}_3$)",
                    r"But-2-yne ($\text{CH}_3\text{-C}\equiv\text{C-CH}_3$)",
                ],
                answer="C",
                level="biet",
                solution=r"Chỉ các alk-1-yne có liên kết ba ở đầu mạch ($\text{R-C}\equiv\text{CH}$) như propyne ($\text{CH}\equiv\text{C-CH}_3$) mới có nguyên tử $\text{H}$ linh động bị thế bởi $\text{Ag}^+$ tạo kết tủa vàng $\text{CAg}\equiv\text{C-CH}_3\downarrow$. But-2-yne có nối ba ở giữa mạch nên không phản ứng.",
            ),
            mcq(
                question=r"Khi cho propene ($\text{CH}_2\text{=CH-CH}_3$) tác dụng với $\text{HBr}$, theo quy tắc Markovnikov sản phẩm chính thu được là:",
                options=[
                    r"1-bromopropane ($\text{CH}_2\text{Br-CH}_2\text{-CH}_3$)",
                    r"2-bromopropane ($\text{CH}_3\text{-CHBr-CH}_3$)",
                    r"1,2-dibromopropane ($\text{CH}_2\text{Br-CHBr-CH}_3$)",
                    r"2-bromopropene ($\text{CH}_2\text{=CBr-CH}_3$)",
                ],
                answer="B",
                level="biet",
                solution=r"Theo quy tắc Markovnikov, nguyên tử $\text{H}$ ưu tiên cộng vào nguyên tử $\text{C}$ nối đôi bậc thấp hơn ($-\text{CH}_2=$), còn nguyên tử $\text{Br}$ ưu tiên cộng vào nguyên tử $\text{C}$ nối đôi bậc cao hơn ($-\text{CH}=$), tạo sản phẩm chính là 2-bromopropane ($\text{CH}_3\text{-CHBr-CH}_3$).",
            ),
            mcq(
                question=r"Hợp chất nào sau đây có đồng phân hình học (*cis–trans*)?",
                options=[
                    r"Propene ($\text{CH}_2\text{=CH-CH}_3$)",
                    r"But-1-ene ($\text{CH}_2\text{=CH-CH}_2\text{-CH}_3$)",
                    r"But-2-ene ($\text{CH}_3\text{-CH=CH-CH}_3$)",
                    r"2-methylpropene ($\text{CH}_2\text{=C(CH}_3)_2$)",
                ],
                answer="C",
                level="hieu",
                solution=r"Điều kiện để alkene $\text{abC=Ccd}$ có đồng phân hình học là $a \neq b$ và $c \neq d$. Ở but-2-ene ($\text{CH}_3\text{-CH=CH-CH}_3$), mỗi nguyên tử $\text{C}$ mang nối đôi đều liên kết với hai nhóm khác nhau là $-\text{H}$ và $-\text{CH}_3$ nên có đồng phân *cis* và *trans*.",
            ),
            mcq(
                question=r"Để phân biệt ba chất lỏng không màu: benzene ($\text{C}_6\text{H}_6$), toluene ($\text{C}_6\text{H}_5\text{CH}_3$) và styrene ($\text{C}_6\text{H}_5\text{-CH=CH}_2$), người ta có thể chỉ dùng một thuốc thử duy nhất là:",
                options=[
                    r"Dung dịch $\text{AgNO}_3/\text{NH}_3$",
                    r"Dung dịch thuốc tím $\text{KMnO}_4$ (khảo sát ở nhiệt độ thường và khi đun nóng)",
                    r"Dung dịch $\text{NaOH}$",
                    r"Giấy quỳ tím ẩm",
                ],
                answer="B",
                level="hieu",
                solution=r"Khi dùng dung dịch $\text{KMnO}_4$: chất làm mất màu tím của $\text{KMnO}_4$ ngay ở nhiệt độ thường là styrene ($\text{C}_6\text{H}_5\text{-CH=CH}_2$); chất chỉ làm mất màu $\text{KMnO}_4$ khi đun nóng là toluene ($\text{C}_6\text{H}_5\text{CH}_3$); chất không làm mất màu $\text{KMnO}_4$ cả khi đun nóng là benzene ($\text{C}_6\text{H}_6$).",
            ),
            tf4(
                stem=r"Một hợp chất hữu cơ $\text{X}$ được phân tích bằng phổ khối lượng ($\text{MS}$) và phổ hồng ngoại ($\text{IR}$) kết hợp với khảo sát cấu tạo của các hydrocarbon. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Trên phổ hồng ngoại ($\text{IR}$), tín hiệu hấp thụ mạnh và nhọn ở vùng số sóng khoảng $1740 \div 1680\text{ cm}^{-1}$ là đặc trưng của liên kết đôi $\text{C=O}$, còn dải hấp thụ tù và rộng ở $3650 \div 3200\text{ cm}^{-1}$ là đặc trưng của nhóm $-\text{OH}$ alcohol.",
                    r"b) Phương pháp chưng cất được dùng để tách hai chất lỏng dựa trên sự khác nhau về khối lượng riêng của chúng.",
                    r"c) Khi cho 2-methylbutane ($\text{CH}_3\text{-CH(CH}_3\text{)-CH}_2\text{-CH}_3$) tác dụng với $\text{Br}_2$ theo tỉ lệ mol $1 : 1$ khi chiếu sáng, sản phẩm monobromo chính thu được là 2-bromo-2-methylbutane.",
                    r"d) Tất cả các alkyne có công thức phân tử $\text{C}_4\text{H}_6$ đều phản ứng được với dung dịch $\text{AgNO}_3/\text{NH}_3$ tạo kết tủa vàng.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Nhóm $\text{C=O}$ hấp thụ đặc trưng ở khoảng $1740 \div 1680\text{ cm}^{-1}$ và nhóm $-\text{OH}$ alcohol hấp thụ ở khoảng $3650 \div 3200\text{ cm}^{-1}$. "
                    r"b) Sai: Phương pháp chưng cất dựa vào sự khác nhau về nhiệt độ sôi của các chất lỏng (tách theo khối lượng riêng và không tan vào nhau là phương pháp chiết lỏng – lỏng). "
                    r"c) Đúng: Phản ứng thế brom vào alkane ưu tiên thế nguyên tử $\text{H}$ ở nguyên tử $\text{C}$ bậc III ($\text{C}$ số $2$) tạo sản phẩm chính là 2-bromo-2-methylbutane. "
                    r"d) Sai: $\text{C}_4\text{H}_6$ có hai đồng phân alkyne là but-1-yne ($\text{CH}\equiv\text{C-CH}_2\text{-CH}_3$, có phản ứng với $\text{AgNO}_3/\text{NH}_3$) và but-2-yne ($\text{CH}_3\text{-C}\equiv\text{C-CH}_3$, không phản ứng với $\text{AgNO}_3/\text{NH}_3$)."
                ),
            ),
            tf4(
                stem=r"Xét các tính chất hóa học và ứng dụng của ethylene ($\text{CH}_2\text{=CH}_2$), acetylene ($\text{CH}\equiv\text{CH}$) và toluene ($\text{C}_6\text{H}_5\text{CH}_3$). Xét tính đúng/sai của các nhận định sau:",
                statements=[
                    r"a) Trùng hợp ethylene ở nhiệt độ, áp suất và xúc tác thích hợp thu được nhựa polyethylene ($\text{PE}$) có công thức mắt xích là $\text{(-CH}_2\text{-CH}_2\text{-)}_n$.",
                    r"b) Khi cộng $\text{H}_2$ vào acetylene ($\text{CH}\equiv\text{CH}$) có xúc tác $\text{Ni}$ đun nóng với $\text{H}_2$ dư, sản phẩm thu được dừng lại ở ethylene ($\text{CH}_2\text{=CH}_2$).",
                    r"c) Khi cho toluene tác dụng với hỗn hợp $\text{HNO}_3$ đặc và $\text{H}_2\text{SO}_4$ đặc theo tỉ lệ $1 : 1$, phản ứng thế xảy ra dễ hơn so với benzene và ưu tiên vào vị trí *ortho* và *para* so với nhóm $-\text{CH}_3$.",
                    r"d) Khi đốt cháy hoàn toàn bất kỳ một alkene $\text{C}_n\text{H}_{2n}$ mạch hở nào cũng luôn thu được số mol $\text{H}_2\text{O}$ lớn hơn số mol $\text{CO}_2$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Phương trình trùng hợp là $n\text{CH}_2\text{=CH}_2 \xrightarrow{t^\circ, p, \text{xt}} \text{(-CH}_2\text{-CH}_2\text{-)}_n$. "
                    r"b) Sai: Với xúc tác $\text{Ni}, t^\circ$ và $\text{H}_2$ dư, acetylene cộng $2$ phân tử $\text{H}_2$ tạo thành ethane ($\text{CH}_3\text{-CH}_3$); muốn dừng ở ethylene phải dùng xúc tác $\text{Pd/PbCO}_3$ (Lindlar). "
                    r"c) Đúng: Nhóm $-\text{CH}_3$ đẩy electron làm giàu mật độ electron ở vòng benzene, đặc biệt tại vị trí *ortho* và *para*. "
                    r"d) Sai: Đốt cháy alkene $\text{C}_n\text{H}_{2n}$ luôn cho $n_{\text{CO}_2} = n_{\text{H}_2\text{O}}$ (chỉ khi đốt alkane $\text{C}_n\text{H}_{2n+2}$ mới có $n_{\text{H}_2\text{O}} > n_{\text{CO}_2}$)."
                ),
            ),
            mcq(
                question=r"Dẫn $4,958\text{ L}$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$) hỗn hợp khí $\text{X}$ gồm ethylene ($\text{C}_2\text{H}_4$) và acetylene ($\text{C}_2\text{H}_2$) vào lượng dư dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ thì thu được $24,0\text{ g}$ kết tủa màu vàng nhạt $\text{Ag}_2\text{C}_2$ ($M = 240\text{ g/mol}$). Phần trăm thể tích của khí ethylene trong hỗn hợp $\text{X}$ là:",
                options=[
                    r"$25\%$",
                    r"$40\%$",
                    r"$50\%$",
                    r"$75\%$",
                ],
                answer="C",
                level="vandung",
                solution=r"Tổng số mol hỗn hợp khí $\text{X}$ là $n_{\text{X}} = \dfrac{4,958}{24,79} = 0,20\text{ mol}$. Chỉ có acetylene ($\text{HC}\equiv\text{CH}$) tác dụng với dung dịch $\text{AgNO}_3/\text{NH}_3$ tạo kết tủa $\text{AgC}\equiv\text{CAg}\downarrow$: $n_{\text{C}_2\text{H}_2} = n_{\text{Ag}_2\text{C}_2} = \dfrac{24,0}{240} = 0,10\text{ mol}$. Suy ra $n_{\text{C}_2\text{H}_4} = 0,20 - 0,10 = 0,10\text{ mol}$, chiếm $\dfrac{0,10}{0,20} \cdot 100\% = 50\%$ thể tích hỗn hợp.",
            ),
            short(
                question=r"Đốt cháy hoàn toàn một lượng hydrocarbon mạch hở $\text{X}$ thuộc dãy đồng đẳng alkane, thu được $0,40\text{ mol}$ khí $\text{CO}_2$ và $0,50\text{ mol}$ $\text{H}_2\text{O}$. Hãy cho biết trong một phân tử alkane $\text{X}$ có bao nhiêu nguyên tử carbon?",
                answer=["4"],
                level="vandung",
                solution=r"Vì $\text{X}$ là alkane ($\text{C}_n\text{H}_{2n+2}$) nên số mol của $\text{X}$ đem đốt là $n_{\text{X}} = n_{\text{H}_2\text{O}} - n_{\text{CO}_2} = 0,50 - 0,40 = 0,10\text{ mol}$. Số nguyên tử carbon trong phân tử $\text{X}$ là $n = \dfrac{n_{\text{CO}_2}}{n_{\text{X}}} = \dfrac{0,40}{0,10} = 4$ ($\text{C}_4\text{H}_{10}$).",
            ),
        ],
    ),

    # =========================================================================
    # CHƯƠNG 7: DẪN XUẤT HALOGEN, ALCOHOL, PHENOL, HỢP CHẤT CARBONYL VÀ CARBOXYLIC ACID
    # =========================================================================
    lesson(
        grade=11,
        order=7,
        code="H11-C07",
        title="Chương 7: Dẫn xuất Halogen, Alcohol, Phenol, Hợp chất Carbonyl và Carboxylic acid",
        topic="dan-xuat-alcohol-carbonyl-acid",
        description="Tính chất hóa học của dẫn xuất halogen, alcohol đơn chức và đa chức, phenol, hợp chất carbonyl (aldehyde và ketone) và carboxylic acid.",
        summary=(
            r"Chương học tổng hợp toàn diện các dẫn xuất của hydrocarbon gồm: dẫn xuất halogen (phản ứng thủy phân tạo alcohol và tách $\text{HX}$ theo quy tắc Zaitsev), "
            r"alcohol (bậc alcohol, tính chất của monoalcohol $\text{C}_n\text{H}_{2n+1}\text{OH}$ và polyalcohol như ethylene glycol, glycerol hòa tan $\text{Cu(OH)}_2$ tạo phức xanh lam thẫm), "
            r"phenol $\text{C}_6\text{H}_5\text{OH}$ (tính acid yếu tác dụng với $\text{NaOH}$ và thế vòng thơm với nước bromine tạo kết tủa trắng $2,4,6\text{-tribromophenol}$), "
            r"hợp chất carbonyl aldehyde/ketone (phản ứng tráng bạc với thuốc thử Tollens $[\text{Ag(NH}_3)_2]\text{OH}$, phản ứng với $\text{Cu(OH)}_2/\text{OH}^-$ tạo kết tủa đỏ gạch $\text{Cu}_2\text{O}\downarrow$, "
            r"phản ứng iodoform tạo kết tủa vàng $\text{CHI}_3\downarrow$) và carboxylic acid $\text{RCOOH}$ (tính acid và phản ứng ester hóa thuận nghịch)."
        ),
        objectives=[
            r"Viết được phương trình phản ứng thế nguyên tử halogen bằng nhóm $-\text{OH}$ và vận dụng được quy tắc tách Zaitsev đối với dẫn xuất halogen.",
            r"Xác định được bậc của alcohol, giải thích được nhiệt độ sôi và độ tan của alcohol qua liên kết hydrogen; trình bày được tính chất của monoalcohol và phản ứng hòa tan $\text{Cu(OH)}_2$ của polyalcohol có các nhóm $-\text{OH}$ kề nhau.",
            r"Giải thích được tính acid yếu của phenol $\text{C}_6\text{H}_5\text{OH}$ (phản ứng với $\text{NaOH}$ nhưng không làm đổi màu quỳ tím) và phản ứng thế vòng thơm tạo kết tủa trắng $2,4,6\text{-tribromophenol}$.",
            r"Vận dụng thành thạo phản ứng tráng bạc với thuốc thử Tollens, phản ứng với $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng, phản ứng iodoform tạo $\text{CHI}_3\downarrow$ của hợp chất carbonyl và phản ứng ester hóa của carboxylic acid.",
        ],
        formulas=[
            {
                "name": "Phản ứng thủy phân và phản ứng tách HX theo quy tắc Zaitsev của dẫn xuất halogen",
                "formula": r"$\text{R-X} + \text{NaOH(aq)} \xrightarrow{t^\circ} \text{R-OH} + \text{NaX}; \quad \text{CH}_3\text{-CHBr-CH}_2\text{-CH}_3 + \text{KOH} \xrightarrow{\text{C}_2\text{H}_5\text{OH}, t^\circ} \text{CH}_3\text{-CH=CH-CH}_3\text{ (chính)} + \text{KBr} + \text{H}_2\text{O}$",
                "note": r"Quy tắc Zaitsev: Nguyên tử halogen $-\text{X}$ ưu tiên tách ra cùng nguyên tử $-\text{H}$ ở nguyên tử $\text{C}$ bên cạnh có bậc cao hơn (ít $\text{H}$ hơn).",
            },
            {
                "name": "Phản ứng nhận biết polyalcohol (glycerol, ethylene glycol) và phenol",
                "formula": r"$2\text{C}_3\text{H}_5(\text{OH})_3 + \text{Cu(OH)}_2 \rightarrow [\text{C}_3\text{H}_5(\text{OH})_2\text{O}]_2\text{Cu (xanh lam thẫm)} + 2\text{H}_2\text{O}; \quad \text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow\text{ (trắng)} + 3\text{HBr}$",
                "note": r"Phenol tác dụng được với cả $\text{Na}$ và dung dịch $\text{NaOH}$ ($\text{C}_6\text{H}_5\text{OH} + \text{NaOH} \rightarrow \text{C}_6\text{H}_5\text{ONa} + \text{H}_2\text{O}$), trong khi alcohol không tác dụng với $\text{NaOH}$.",
            },
            {
                "name": "Phản ứng tráng bạc và phản ứng với Cu(OH)2/OH- của aldehyde",
                "formula": r"$\text{RCHO} + 2[\text{Ag(NH}_3)_2]\text{OH} \xrightarrow{t^\circ} \text{RCOONH}_4 + 2\text{Ag}\downarrow + 3\text{NH}_3 + \text{H}_2\text{O}; \quad \text{RCHO} + 2\text{Cu(OH)}_2 + \text{NaOH} \xrightarrow{t^\circ} \text{RCOONa} + \text{Cu}_2\text{O}\downarrow\text{ (đỏ gạch)} + 3\text{H}_2\text{O}$",
                "note": r"Tỉ lệ tráng bạc: $1\text{ mol RCHO (đơn chức, } \text{R} \neq \text{H)} \rightarrow 2\text{ mol Ag}\downarrow$; riêng $1\text{ mol HCHO} \rightarrow 4\text{ mol Ag}\downarrow$.",
            },
            {
                "name": "Phản ứng tạo iodoform của hợp chất chứa nhóm methyl carbonyl và phản ứng ester hóa",
                "formula": r"$\text{CH}_3\text{COR} + 3\text{I}_2 + 4\text{NaOH} \rightarrow \text{CHI}_3\downarrow\text{ (vàng)} + \text{RCOONa} + 3\text{NaI} + 3\text{H}_2\text{O}; \quad \text{RCOOH} + \text{R'OH} \underset{t^\circ}{\stackrel{\text{H}_2\text{SO}_4\text{ đặc}}{\rightleftharpoons}} \text{RCOOR'} + \text{H}_2\text{O}$",
                "note": r"Phản ứng iodoform dùng nhận biết các hợp chất có cấu trúc $\text{CH}_3\text{-C=O}$ như acetaldehyde ($\text{CH}_3\text{CHO}$) và acetone ($\text{CH}_3\text{COCH}_3$).",
            },
        ],
        theory_sections=[
            {
                "title": "1. Dẫn xuất halogen của hydrocarbon",
                "content": (
                    r"Khi thay thế nguyên tử hydrogen của hydrocarbon bằng nguyên tử halogen ($\text{F}, \text{Cl}, \text{Br}, \text{I}$), ta thu được dẫn xuất halogen. "
                    r"Hai phản ứng hóa học quan trọng nhất của dẫn xuất halogen là:\n"
                    r"- Phản ứng thế nguyên tử halogen bằng nhóm $-\text{OH}$ (thủy phân trong dung dịch kiềm loãng đun nóng): $\text{R-X} + \text{NaOH} \xrightarrow{t^\circ} \text{R-OH} + \text{NaX}$.\n"
                    r"- Phản ứng tách hydrogen halide ($\text{HX}$) khi đun nóng với $\text{KOH}$ hoặc $\text{NaOH}$ trong dung môi $\text{C}_2\text{H}_5\text{OH}$ tạo alkene theo quy tắc Zaitsev: "
                    r"nguyên tử halogen $-\text{X}$ ưu tiên tách ra cùng với nguyên tử $-\text{H}$ ở nguyên tử $\text{C}$ bên cạnh có bậc cao hơn để tạo alkene bền hơn làm sản phẩm chính."
                ),
            },
            {
                "title": "2. Alcohol và Phenol",
                "content": (
                    r"Alcohol là hợp chất hữu cơ có nhóm $-\text{OH}$ liên kết trực tiếp với nguyên tử carbon no; bậc của alcohol bằng bậc của nguyên tử $\text{C}$ liên kết với nhóm $-\text{OH}$. "
                    r"Nhờ tạo được liên kết hydrogen liên phân tử nên alcohol có nhiệt độ sôi cao hơn hẳn hydrocarbon hay dẫn xuất halogen có phân tử khối tương đương và các alcohol đầu dãy ($\text{CH}_3\text{OH}, \text{C}_2\text{H}_5\text{OH}$) tan vô hạn trong nước. "
                    r"Về hóa tính: (1) Tác dụng với kim loại kiềm $\text{Na}, \text{K}$ giải phóng $\text{H}_2\uparrow$ ($\text{R-OH} + \text{Na} \rightarrow \text{R-ONa} + \dfrac{1}{2}\text{H}_2\uparrow$); "
                    r"(2) Phản ứng của polyalcohol có ít nhất $2$ nhóm $-\text{OH}$ gắn vào hai nguyên tử $\text{C}$ kề nhau (như ethylene glycol $\text{HO-CH}_2\text{-CH}_2\text{-OH}$, glycerol $\text{C}_3\text{H}_5(\text{OH})_3$) hòa tan $\text{Cu(OH)}_2$ tạo dung dịch phức chất màu xanh lam thẫm; "
                    r"(3) Tách nước nội phân tử ở $170^\circ\text{C}$ với $\text{H}_2\text{SO}_4$ đặc tạo alkene (hoặc tạo ether ở $140^\circ\text{C}$); "
                    r"(4) Oxi hóa không hoàn toàn bằng $\text{CuO}$ đun nóng: alcohol bậc I tạo aldehyde ($\text{RCH}_2\text{OH} + \text{CuO} \xrightarrow{t^\circ} \text{RCHO} + \text{Cu} + \text{H}_2\text{O}$), alcohol bậc II tạo ketone, alcohol bậc III không bị oxi hóa bởi $\text{CuO}$.\n"
                    r"Phenol ($\text{C}_6\text{H}_5\text{OH}$) có nhóm $-\text{OH}$ gắn trực tiếp vào vòng benzene. Do vòng benzene hút electron làm tăng độ phân cực của liên kết $\text{O-H}$, phenol có tính acid yếu (tác dụng được với cả $\text{Na}$ và dung dịch $\text{NaOH}$ tạo sodium phenolate $\text{C}_6\text{H}_5\text{ONa}$, nhưng lực acid rất yếu nên không làm đổi màu quỳ tím và bị $\text{CO}_2 + \text{H}_2\text{O}$ đẩy ra khỏi muối: $\text{C}_6\text{H}_5\text{ONa} + \text{CO}_2 + \text{H}_2\text{O} \rightarrow \text{C}_6\text{H}_5\text{OH}\downarrow + \text{NaHCO}_3$). "
                    r"Ngược lại, nhóm $-\text{OH}$ làm tăng mật độ electron ở vòng benzene tại các vị trí *ortho* và *para*, giúp phenol dễ dàng tác dụng với dung dịch nước $\text{Br}_2$ ngay ở điều kiện thường tạo kết tủa trắng $2,4,6\text{-tribromophenol}$ ($\text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow$) và tác dụng với $\text{HNO}_3$ đặc tạo picric acid ($2,4,6\text{-trinitrophenol}$ kết tủa vàng)."
                ),
            },
            {
                "title": "3. Hợp chất Carbonyl (Aldehyde và Ketone) và Carboxylic acid",
                "content": (
                    r"Hợp chất carbonyl chứa nhóm chức $\text{C=O}$ gồm aldehyde ($\text{R-CHO}$, nhóm $-\text{CHO}$ gắn với $\text{H}$ hoặc gốc hydrocarbon) và ketone ($\text{R-CO-R'}$, nhóm $\text{C=O}$ gắn với hai gốc hydrocarbon):\n"
                    r"- Phản ứng khử: Bị khử bởi $\text{NaBH}_4$ hoặc $\text{LiAlH}_4$ (hoặc $\text{H}_2/\text{Ni}, t^\circ$): aldehyde tạo alcohol bậc I, ketone tạo alcohol bậc II.\n"
                    r"- Phản ứng oxi hóa (chỉ aldehyde có, ketone không phản ứng): Aldehyde làm mất màu nước bromine ($\text{RCHO} + \text{Br}_2 + \text{H}_2\text{O} \rightarrow \text{RCOOH} + 2\text{HBr}$), "
                    r"tham gia phản ứng tráng bạc với thuốc thử Tollens $[\text{Ag(NH}_3)_2]\text{OH}$ đun nóng tạo lớp bạc sáng $\text{Ag}\downarrow$ (tỉ lệ $1\text{ -CHO} : 2\text{ Ag}$, riêng $\text{HCHO}$ cho $4\text{ Ag}$) "
                    r"và phản ứng với $\text{Cu(OH)}_2/\text{NaOH}$ đun nóng tạo kết tủa đỏ gạch $\text{Cu}_2\text{O}\downarrow$.\n"
                    r"- Phản ứng tạo iodoform: Các hợp chất chứa cụm $\text{CH}_3\text{-CO-}$ (như ethanal $\text{CH}_3\text{CHO}$, propanone $\text{CH}_3\text{COCH}_3$) tác dụng với $\text{I}_2$ trong dung dịch $\text{NaOH}$ tạo kết tủa màu vàng iodoform ($\text{CHI}_3\downarrow$).\n"
                    r"Carboxylic acid ($\text{R-COOH}$) là chất điện li yếu nhưng thể hiện đầy đủ tính chất của một acid: làm quỳ tím hóa đỏ, tác dụng với kim loại đứng trước $\text{H}$, basic oxide, base và muối carbonate ($\text{2CH}_3\text{COOH} + \text{CaCO}_3 \rightarrow (\text{CH}_3\text{COO})_2\text{Ca} + \text{CO}_2\uparrow + \text{H}_2\text{O}$ — dùng giấm ăn tẩy cặn vôi trong ấm đun nước). "
                    r"Khi đun nóng carboxylic acid với alcohol có mặt $\text{H}_2\text{SO}_4$ đặc làm xúc tác, xảy ra phản ứng ester hóa thuận nghịch tạo ester có mùi thơm."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: So sánh lượng bạc thu được khi tráng gương $\text{CH}_3\text{CHO}$ và $\text{HCHO}$",
                "problem": (
                    r"Cho $4,4\text{ g}$ ethanal (acetaldehyde: $\text{CH}_3\text{CHO}$, $M = 44\text{ g/mol}$) tác dụng hoàn toàn với lượng dư thuốc thử Tollens đun nóng. "
                    r"Tính khối lượng $\text{Ag}$ ($M = 108\text{ g/mol}$) thu được. Nếu thay $4,4\text{ g}$ $\text{CH}_3\text{CHO}$ bằng $3,0\text{ g}$ methanal (formaldehyde: $\text{HCHO}$, $M = 30\text{ g/mol}$) "
                    r"thì thu được bao nhiêu gam $\text{Ag}$?"
                ),
                "solution": (
                    r"Với $4,4\text{ g}$ $\text{CH}_3\text{CHO}$: $n_{\text{CH}_3\text{CHO}} = \dfrac{4,4}{44} = 0,10\text{ mol}$. "
                    r"Theo phương trình $\text{CH}_3\text{CHO} + 2[\text{Ag(NH}_3)_2]\text{OH} \xrightarrow{t^\circ} \text{CH}_3\text{COONH}_4 + 2\text{Ag}\downarrow + 3\text{NH}_3 + \text{H}_2\text{O}$, "
                    r"ta có $n_{\text{Ag}} = 2 \cdot 0,10 = 0,20\text{ mol} \implies m_{\text{Ag}} = 0,20 \cdot 108 = 21,6\text{ g}$. "
                    r"Với $3,0\text{ g}$ $\text{HCHO}$: $n_{\text{HCHO}} = \dfrac{3,0}{30} = 0,10\text{ mol}$. Vì $\text{HCHO}$ phản ứng theo tỉ lệ $1\text{ mol HCHO} \rightarrow 4\text{ mol Ag}\downarrow$ "
                    r"nên $n_{\text{Ag}} = 4 \cdot 0,10 = 0,40\text{ mol} \implies m_{\text{Ag}} = 0,40 \cdot 108 = 43,2\text{ g}$."
                ),
            },
            {
                "title": r"Ví dụ 2: Bài toán hỗn hợp Ethanol và Phenol tác dụng với $\text{Br}_2$ và $\text{Na}$",
                "problem": (
                    r"Cho $14,0\text{ g}$ hỗn hợp $\text{X}$ gồm ethanol ($\text{C}_2\text{H}_5\text{OH}$, $M = 46\text{ g/mol}$) và phenol ($\text{C}_6\text{H}_5\text{OH}$, $M = 94\text{ g/mol}$) "
                    r"tác dụng với lượng dư dung dịch nước $\text{Br}_2$ thì thu được $33,1\text{ g}$ kết tủa trắng $2,4,6\text{-tribromophenol}$ ($\text{C}_6\text{H}_2\text{Br}_3\text{OH}$, $M = 331\text{ g/mol}$). "
                    r"Nếu cho $14,0\text{ g}$ hỗn hợp $\text{X}$ trên tác dụng hết với kim loại $\text{Na}$ dư thì thu được bao nhiêu lít khí $\text{H}_2$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$)?"
                ),
                "solution": (
                    r"Chỉ có phenol phản ứng với nước bromine tạo kết tủa trắng: $\text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow + 3\text{HBr}$. "
                    r"Suy ra $n_{\text{phenol}} = n_{\text{kết tủa}} = \dfrac{33,1}{331} = 0,10\text{ mol} \implies m_{\text{phenol}} = 0,10 \cdot 94 = 9,4\text{ g}$. "
                    r"Khối lượng ethanol trong hỗn hợp $\text{X}$ là $m_{\text{ethanol}} = 14,0 - 9,4 = 4,6\text{ g} \implies n_{\text{ethanol}} = \dfrac{4,6}{46} = 0,10\text{ mol}$. "
                    r"Khi tác dụng với $\text{Na}$ dư, cả hai chất đều phản ứng theo tỉ lệ $1\text{ nhóm -OH} \rightarrow \dfrac{1}{2}\text{H}_2\uparrow$: "
                    r"$n_{\text{H}_2} = \dfrac{1}{2}(n_{\text{phenol}} + n_{\text{ethanol}}) = \dfrac{1}{2}(0,10 + 0,10) = 0,10\text{ mol} \implies V_{\text{H}_2} = 0,10 \cdot 24,79 = 2,479\text{ L}$."
                ),
            },
        ],
        key_takeaways=[
            r"Tách $\text{HX}$ khỏi dẫn xuất halogen hoặc tách $\text{H}_2\text{O}$ khỏi alcohol bất đối xứng đều tuân theo quy tắc Zaitsev (tách cùng $\text{H}$ ở $\text{C}$ bậc cao hơn).",
            r"Polyalcohol có ít nhất $2$ nhóm $-\text{OH}$ gắn vào các nguyên tử $\text{C}$ kề nhau (ethylene glycol, glycerol) hòa tan được $\text{Cu(OH)}_2$ tạo phức màu xanh lam thẫm.",
            r"Phenol ($\text{C}_6\text{H}_5\text{OH}$) tác dụng được với dung dịch $\text{NaOH}$ (khác với alcohol) và tạo kết tủa trắng $2,4,6\text{-tribromophenol}$ với nước $\text{Br}_2$.",
            r"Aldehyde tráng bạc với thuốc thử Tollens và tạo kết tủa đỏ gạch $\text{Cu}_2\text{O}\downarrow$ với $\text{Cu(OH)}_2/\text{OH}^-$ đun nóng; hợp chất có nhóm $\text{CH}_3\text{CO}-$ tạo kết tủa vàng $\text{CHI}_3\downarrow$ với $\text{I}_2/\text{NaOH}$.",
        ],
        questions=[
            mcq(
                question=r"Khi đun nóng 2-bromobutane ($\text{CH}_3\text{-CHBr-CH}_2\text{-CH}_3$) với $\text{KOH}$ trong dung môi $\text{C}_2\text{H}_5\text{OH}$, theo quy tắc tách Zaitsev sản phẩm alkene chính thu được là:",
                options=[
                    r"But-1-ene ($\text{CH}_2\text{=CH-CH}_2\text{-CH}_3$)",
                    r"But-2-ene ($\text{CH}_3\text{-CH=CH-CH}_3$)",
                    r"2-methylpropene ($\text{CH}_2\text{=C(CH}_3)_2$)",
                    r"Butan-2-ol ($\text{CH}_3\text{-CH(OH)-CH}_2\text{-CH}_3$)",
                ],
                answer="B",
                level="biet",
                solution=r"Theo quy tắc Zaitsev, nguyên tử $-\text{Br}$ ở $\text{C}_2$ ưu tiên tách ra cùng nguyên tử $-\text{H}$ ở nguyên tử $\text{C}_3$ bậc cao hơn, tạo sản phẩm chính là but-2-ene ($\text{CH}_3\text{-CH=CH-CH}_3$).",
            ),
            mcq(
                question=r"Chất nào dưới đây hòa tan được $\text{Cu(OH)}_2$ ở nhiệt độ thường tạo thành dung dịch phức chất có màu xanh lam thẫm?",
                options=[
                    r"Ethanol ($\text{CH}_3\text{-CH}_2\text{-OH}$)",
                    r"Propan-1,3-diol ($\text{HO-CH}_2\text{-CH}_2\text{-CH}_2\text{-OH}$)",
                    r"Glycerol ($\text{HO-CH}_2\text{-CH(OH)-CH}_2\text{-OH}$)",
                    r"Phenol ($\text{C}_6\text{H}_5\text{OH}$)",
                ],
                answer="C",
                level="biet",
                solution=r"Các polyalcohol có ít nhất $2$ nhóm $-\text{OH}$ đính vào hai nguyên tử carbon kề nhau như glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$) hoặc ethylene glycol ($\text{C}_2\text{H}_4(\text{OH})_2$) hòa tan được $\text{Cu(OH)}_2$ tạo phức màu xanh lam thẫm. Propan-1,3-diol có $2$ nhóm $-\text{OH}$ cách xa nhau nên không có phản ứng này.",
            ),
            mcq(
                question=r"Khi nhỏ nước bromine ($\text{Br}_2$) vào ống nghiệm chứa dung dịch phenol ($\text{C}_6\text{H}_5\text{OH}$), hiện tượng quan sát được là:",
                options=[
                    r"Nước bromine mất màu và xuất hiện kết tủa màu trắng của $2,4,6\text{-tribromophenol}$",
                    r"Xuất hiện kết tủa màu đỏ gạch của $\text{Cu}_2\text{O}$",
                    r"Xuất hiện kết tủa màu vàng của iodoform $\text{CHI}_3$",
                    r"Không có hiện tượng gì xảy ra",
                ],
                answer="A",
                level="biet",
                solution=r"Do ảnh hưởng của nhóm $-\text{OH}$ đẩy electron vào vòng benzene, phenol phản ứng rất dễ với nước $\text{Br}_2$ tạo kết tủa trắng $2,4,6\text{-tribromophenol}$: $\text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow + 3\text{HBr}$.",
            ),
            mcq(
                question=r"Hợp chất carbonyl nào dưới đây khi tác dụng với $\text{I}_2$ trong dung dịch $\text{NaOH}$ đun nóng tạo ra kết tủa màu vàng iodoform ($\text{CHI}_3\downarrow$), nhưng KHÔNG tham gia phản ứng tráng bạc với thuốc thử Tollens?",
                options=[
                    r"Methanal ($\text{HCHO}$)",
                    r"Ethanal ($\text{CH}_3\text{CHO}$)",
                    r"Propanone (acetone: $\text{CH}_3\text{COCH}_3$)",
                    r"Benzaldehyde ($\text{C}_6\text{H}_5\text{CHO}$)",
                ],
                answer="C",
                level="biet",
                solution=r"Propanone (acetone: $\text{CH}_3\text{COCH}_3$) là một ketone có chứa nhóm methyl carbonyl ($\text{CH}_3\text{CO}-$) nên tham gia phản ứng tạo kết tủa vàng $\text{CHI}_3\downarrow$, nhưng không có nhóm $-\text{CHO}$ nên không tham gia phản ứng tráng bạc.",
            ),
            mcq(
                question=r"Để phân biệt ba chất lỏng đựng trong ba lọ mất nhãn: ethanol ($\text{C}_2\text{H}_5\text{OH}$), glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$) và dung dịch ethanal ($\text{CH}_3\text{CHO}$), ta có thể chỉ dùng một thuốc thử duy nhất là:",
                options=[
                    r"Kim loại $\text{Na}$",
                    r"$\text{Cu(OH)}_2$ trong môi trường kiềm $\text{NaOH}$ (khảo sát ở nhiệt độ thường và khi đun nóng)",
                    r"Dung dịch $\text{NaCl}$",
                    r"Quỳ tím",
                ],
                answer="B",
                level="hieu",
                solution=r"Ở nhiệt độ thường, glycerol hòa tan $\text{Cu(OH)}_2$ tạo dung dịch màu xanh lam thẫm; hai chất còn lại không hòa tan $\text{Cu(OH)}_2$. Khi đun nóng, ethanal ($\text{CH}_3\text{CHO}$) khử $\text{Cu(OH)}_2/\text{NaOH}$ tạo kết tủa màu đỏ gạch $\text{Cu}_2\text{O}\downarrow$, còn ethanol không có hiện tượng này.",
            ),
            mcq(
                question=r"Cho dãy các chất: $\text{C}_2\text{H}_5\text{OH}$, $\text{C}_6\text{H}_5\text{OH}$ (phenol) và $\text{CH}_3\text{COOH}$. Thứ tự tăng dần lực acid (độ linh động của nguyên tử $\text{H}$ trong nhóm $-\text{OH}$) của các chất trong dãy là:",
                options=[
                    r"$\text{C}_2\text{H}_5\text{OH} < \text{C}_6\text{H}_5\text{OH} < \text{CH}_3\text{COOH}$",
                    r"$\text{C}_6\text{H}_5\text{OH} < \text{C}_2\text{H}_5\text{OH} < \text{CH}_3\text{COOH}$",
                    r"$\text{CH}_3\text{COOH} < \text{C}_6\text{H}_5\text{OH} < \text{C}_2\text{H}_5\text{OH}$",
                    r"$\text{C}_2\text{H}_5\text{OH} < \text{CH}_3\text{COOH} < \text{C}_6\text{H}_5\text{OH}$",
                ],
                answer="A",
                level="hieu",
                solution=r"Gốc $-\text{C}_2\text{H}_5$ đẩy electron làm giảm độ phân cực liên kết $\text{O-H}$ nên $\text{C}_2\text{H}_5\text{OH}$ hầu như trung tính (chỉ tác dụng $\text{Na}$, không tác dụng $\text{NaOH}$). Vòng $-\text{C}_6\text{H}_5$ hút electron nên $\text{C}_6\text{H}_5\text{OH}$ có tính acid yếu (tác dụng $\text{NaOH}$, không tác dụng $\text{NaHCO}_3$). Nhóm $\text{C=O}$ trong $-\text{COOH}$ hút electron rất mạnh nên $\text{CH}_3\text{COOH}$ có tính acid mạnh nhất (làm đỏ quỳ tím, tác dụng $\text{NaHCO}_3$).",
            ),
            tf4(
                stem=r"Khảo sát tính chất vật lý và hóa học của ethanol ($\text{C}_2\text{H}_5\text{OH}$) và phenol ($\text{C}_6\text{H}_5\text{OH}$). Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Cả ethanol và phenol đều tác dụng được với kim loại $\text{Na}$ giải phóng khí $\text{H}_2\uparrow$, nhưng chỉ có phenol tác dụng được với dung dịch $\text{NaOH}$.",
                    r"b) Dung dịch phenol trong nước làm giấy quỳ tím chuyển sang màu đỏ đậm.",
                    r"c) Khi sục khí $\text{CO}_2$ vào dung dịch sodium phenolate ($\text{C}_6\text{H}_5\text{ONa}$), dung dịch bị vẩn đục do tạo thành phenol ($\text{C}_6\text{H}_5\text{OH}$) ít tan trong nước lạnh.",
                    r"d) Oxi hóa không hoàn toàn alcohol bậc II là propan-2-ol ($\text{CH}_3\text{-CH(OH)-CH}_3$) bằng $\text{CuO}$ đun nóng thu được một aldehyde.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Ethanol và phenol đều có nguyên tử $\text{H}$ linh động trong nhóm $-\text{OH}$ nên đều tác dụng với $\text{Na}$, nhưng chỉ phenol có tính acid đủ để phản ứng với $\text{NaOH}$ ($\text{C}_6\text{H}_5\text{OH} + \text{NaOH} \rightarrow \text{C}_6\text{H}_5\text{ONa} + \text{H}_2\text{O}$). "
                    r"b) Sai: Tính acid của phenol rất yếu ($K_{\text{a}} \approx 10^{-10}$) nên không làm đổi màu quỳ tím. "
                    r"c) Đúng: Vì tính acid của phenol yếu hơn nấc 1 của $\text{H}_2\text{CO}_3$ nên $\text{C}_6\text{H}_5\text{ONa} + \text{CO}_2 + \text{H}_2\text{O} \rightarrow \text{C}_6\text{H}_5\text{OH}\downarrow + \text{NaHCO}_3$. "
                    r"d) Sai: Oxi hóa alcohol bậc II ($\text{CH}_3\text{-CH(OH)-CH}_3$) bằng $\text{CuO}$ đun nóng thu được ketone là propanone ($\text{CH}_3\text{COCH}_3$), không phải aldehyde."
                ),
            ),
            tf4(
                stem=r"Xét các phản ứng hóa học đặc trưng của hợp chất carbonyl (aldehyde, ketone) và carboxylic acid. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Khi cho $1\text{ mol}$ methanal ($\text{HCHO}$) phản ứng hoàn toàn với lượng dư thuốc thử Tollens $[\text{Ag(NH}_3)_2]\text{OH}$ đun nóng thì thu được tối đa $4\text{ mol}$ $\text{Ag}\downarrow$.",
                    r"b) Cả ethanal ($\text{CH}_3\text{CHO}$) và propanone ($\text{CH}_3\text{COCH}_3$) đều làm mất màu dung dịch nước bromine ở điều kiện thường.",
                    r"c) Có thể dùng giấm ăn (dung dịch $\text{CH}_3\text{COOH}$ nồng độ $2\% \div 5\%$) để làm sạch lớp cặn đá vôi ($\text{CaCO}_3$) bám ở đáy ấm đun nước.",
                    r"d) Phản ứng ester hóa giữa acetic acid ($\text{CH}_3\text{COOH}$) và ethanol ($\text{C}_2\text{H}_5\text{OH}$) có xúc tác $\text{H}_2\text{SO}_4$ đặc đun nóng là phản ứng một chiều nên luôn đạt hiệu suất $100\%$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng: Phương trình phản ứng là $\text{HCHO} + 4[\text{Ag(NH}_3)_2]\text{OH} \xrightarrow{t^\circ} (\text{NH}_4)_2\text{CO}_3 + 4\text{Ag}\downarrow + 6\text{NH}_3 + 2\text{H}_2\text{O}$. "
                    r"b) Sai: Chỉ aldehyde ($\text{CH}_3\text{CHO}$) mới bị nước $\text{Br}_2$ oxi hóa làm mất màu nước bromine; ketone ($\text{CH}_3\text{COCH}_3$) không làm mất màu nước bromine. "
                    r"c) Đúng: $\text{CH}_3\text{COOH}$ mạnh hơn $\text{H}_2\text{CO}_3$ nên hòa tan $\text{CaCO}_3$ tạo muối tan: $2\text{CH}_3\text{COOH} + \text{CaCO}_3 \rightarrow (\text{CH}_3\text{COO})_2\text{Ca} + \text{CO}_2\uparrow + \text{H}_2\text{O}$. "
                    r"d) Sai: Phản ứng ester hóa là phản ứng thuận nghịch ($\rightleftharpoons$) nên không bao giờ đạt hiệu suất $100\%$ nếu không tách sản phẩm."
                ),
            ),
            mcq(
                question=r"Đun nóng $12,0\text{ g}$ acetic acid ($\text{CH}_3\text{COOH}$, $M = 60\text{ g/mol}$) với $13,8\text{ g}$ ethanol ($\text{C}_2\text{H}_5\text{OH}$, $M = 46\text{ g/mol}$) có mặt $\text{H}_2\text{SO}_4$ đặc làm xúc tác. Sau khi phản ứng đạt tới trạng thái cân bằng thì thu được $11,0\text{ g}$ ester ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$, $M = 88\text{ g/mol}$). Hiệu suất của phản ứng ester hóa trên là:",
                options=[
                    r"$41,67\%$",
                    r"$62,50\%$",
                    r"$75,00\%$",
                    r"$80,00\%$",
                ],
                answer="B",
                level="vandung",
                solution=r"Ta có $n_{\text{CH}_3\text{COOH}} = \dfrac{12,0}{60} = 0,20\text{ mol}$ và $n_{\text{C}_2\text{H}_5\text{OH}} = \dfrac{13,8}{46} = 0,30\text{ mol}$. Vì phản ứng xảy ra theo tỉ lệ mol $1 : 1$ và $0,20 < 0,30$ nên hiệu suất phải tính theo $\text{CH}_3\text{COOH}$. Số mol ester thu được thực tế là $n_{\text{ester}} = \dfrac{11,0}{88} = 0,125\text{ mol}$. Vậy hiệu suất phản ứng là $H = \dfrac{0,125}{0,20} \cdot 100\% = 62,50\%$.",
            ),
            short(
                question=r"Cho $6,6\text{ g}$ ethanal (acetaldehyde: $\text{CH}_3\text{CHO}$, $M = 44\text{ g/mol}$) phản ứng hoàn toàn với lượng dư thuốc thử Tollens $[\text{Ag(NH}_3)_2]\text{OH}$ đun nóng. Tính khối lượng kết tủa bạc ($\text{Ag}$, $M = 108\text{ g/mol}$) thu được (theo đơn vị $\text{gam}$).",
                answer=["32,4", "32.4"],
                level="vandung",
                solution=r"Số mol $\text{CH}_3\text{CHO}$ là $n_{\text{CH}_3\text{CHO}} = \dfrac{6,6}{44} = 0,15\text{ mol}$. Theo phản ứng tráng bạc, $1\text{ mol }\text{CH}_3\text{CHO}$ tạo ra $2\text{ mol }\text{Ag}\downarrow$, nên $n_{\text{Ag}} = 2 \cdot 0,15 = 0,30\text{ mol}$. Khối lượng bạc thu được là $m_{\text{Ag}} = 0,30 \cdot 108 = 32,4\text{ g}$.",
            ),
        ],
    ),
]


LESSONS = LESSONS_GRADE_11
