from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_8: list[dict[str, Any]] = [
    lesson(
        grade=8,
        order=1,
        code="H8-C01",
        title="Chương 1: Công thức hóa học và tính theo công thức hóa học",
        topic="cong-thuc-hoa-hoc",
        summary=(
            r"Nắm vững ý nghĩa công thức hóa học của đơn chất và hợp chất, quy tắc hóa trị "
            r"$a \cdot x = b \cdot y$, cách tính phần trăm khối lượng nguyên tố trong hợp chất "
            r"$\text{\%}m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{hợp chất}}} \cdot 100\text{\%}$ "
            r"và xác định công thức hóa học khi biết thành phần phần trăm khối lượng và khối lượng phân tử."
        ),
        objectives=[
            r"Trình bày được ý nghĩa công thức hóa học của đơn chất và hợp chất: nguyên tố tạo nên chất, số nguyên tử của mỗi nguyên tố và khối lượng phân tử ($\text{amu}$).",
            r"Vận dụng được quy tắc hóa trị $a \cdot x = b \cdot y$ cho hợp chất $\text{A}_x\text{B}_y$ để lập công thức hóa học của hợp chất.",
            r"Tính được thành phần phần trăm theo khối lượng của từng nguyên tố trong một hợp chất khi biết công thức hóa học của hợp chất đó.",
            r"Xác định được công thức hóa học của hợp chất khi biết thành phần phần trăm khối lượng các nguyên tố và khối lượng phân tử.",
        ],
        formulas=[
            {
                "name": "Quy tắc hóa trị đối với hợp chất hai nguyên tố",
                "formula": r"$a \cdot x = b \cdot y \quad (\text{trong hợp chất }\overset{a}{\text{A}}_x\overset{b}{\text{B}}_y)$",
                "note": r"$x, y$ là chỉ số nguyên tử (tối giản); $a, b$ là hóa trị tương ứng của $\text{A}, \text{B}$",
            },
            {
                "name": "Khối lượng phân tử của hợp chất",
                "formula": r"$M_{\text{A}_x\text{B}_y\text{C}_z} = x \cdot M_{\text{A}} + y \cdot M_{\text{B}} + z \cdot M_{\text{C}}\text{ (amu hoặc g/mol)}$",
                "note": r"$M_{\text{A}}, M_{\text{B}}, M_{\text{C}}$ là khối lượng nguyên tử của các nguyên tố",
            },
            {
                "name": "Phần trăm khối lượng nguyên tố trong hợp chất",
                "formula": r"$\text{\%}m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{A}_x\text{B}_y}} \cdot 100\text{\%}; \quad \text{\%}m_{\text{B}} = 100\text{\%} - \text{\%}m_{\text{A}}$",
                "note": r"Tổng phần trăm khối lượng tất cả các nguyên tố trong hợp chất bằng $100\text{\%}$",
            },
            {
                "name": "Xác định chỉ số nguyên tử từ phần trăm khối lượng và khối lượng phân tử",
                "formula": r"$x = \dfrac{\text{\%}m_{\text{A}} \cdot M_{\text{hợp chất}}}{100\text{\%} \cdot M_{\text{A}}}; \quad x : y = \dfrac{\text{\%}m_{\text{A}}}{M_{\text{A}}} : \dfrac{\text{\%}m_{\text{B}}}{M_{\text{B}}}$",
                "note": r"Áp dụng để tìm công thức hóa học $\text{A}_x\text{B}_y$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Công thức hóa học của đơn chất và hợp chất",
                "content": (
                    r"Công thức hóa học dùng để biểu diễn chất, gồm một kí hiệu hóa học (đơn chất) hoặc hai, ba kí hiệu "
                    r"hóa học trở lên (hợp chất) kèm theo chỉ số ở chân mỗi kí hiệu. Đối với đơn chất kim loại ($\text{Fe}, \text{Cu}, \text{Al}$), "
                    r"khí hiếm ($\text{He}, \text{Ne}, \text{Ar}$) và một số phi kim rắn ($\text{C}, \text{S}, \text{P}$), công thức chung là $\text{A}$; "
                    r"đối với nhiều phi kim khí ở điều kiện chuẩn ($\text{H}_2, \text{O}_2, \text{N}_2, \text{Cl}_2$), công thức là $\text{A}_2$ "
                    r"(hoặc $\text{O}_3$ với ozone). Đối với hợp chất, công thức chung có dạng $\text{A}_x\text{B}_y$ hoặc $\text{A}_x\text{B}_y\text{C}_z$, "
                    r"cho biết nguyên tố tạo nên chất, số nguyên tử của mỗi nguyên tố trong một phân tử và khối lượng phân tử của chất."
                ),
            },
            {
                "title": "2. Hóa trị và quy tắc hóa trị",
                "content": (
                    r"Hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác, "
                    r"được xác định bằng cách chọn hóa trị của $\text{H}$ làm đơn vị ($\text{I}$) và hóa trị của $\text{O}$ là hai đơn vị ($\text{II}$). "
                    r"Trong công thức hóa học của hợp chất hai nguyên tố $\overset{a}{\text{A}}_x\overset{b}{\text{B}}_y$, tích của chỉ số và hóa trị "
                    r"của nguyên tố này bằng tích của chỉ số và hóa trị của nguyên tố kia: $a \cdot x = b \cdot y$, suy ra tỉ lệ $\dfrac{x}{y} = \dfrac{b}{a}$ "
                    r"(tối giản). Quy tắc này cũng áp dụng cho nhóm nguyên tử như $\text{OH}$ (hóa trị $\text{I}$), $\text{NO}_3$ (hóa trị $\text{I}$), "
                    r"$\text{SO}_4$ (hóa trị $\text{II}$), $\text{CO}_3$ (hóa trị $\text{II}$), $\text{PO}_4$ (hóa trị $\text{III}$)."
                ),
            },
            {
                "title": "3. Tính theo công thức hóa học",
                "content": (
                    r"Bài toán 1 — Tính phần trăm khối lượng các nguyên tố khi biết công thức hóa học $\text{A}_x\text{B}_y$: "
                    r"Bước 1: Tính khối lượng phân tử $M_{\text{A}_x\text{B}_y} = x \cdot M_{\text{A}} + y \cdot M_{\text{B}}$. "
                    r"Bước 2: Tính $\text{\%}m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{A}_x\text{B}_y}} \cdot 100\text{\%}$ và $\text{\%}m_{\text{B}} = 100\text{\%} - \text{\%}m_{\text{A}}$. "
                    r"Bài toán 2 — Xác định công thức hóa học khi biết thành phần phần trăm khối lượng và khối lượng phân tử $M$: "
                    r"Đặt công thức tổng quát $\text{A}_x\text{B}_y$, tính khối lượng mỗi nguyên tố trong $1\text{ mol}$ phân tử "
                    r"$m_{\text{A}} = \dfrac{\text{\%}m_{\text{A}} \cdot M}{100\text{\%}}$, từ đó suy ra chỉ số $x = \dfrac{m_{\text{A}}}{M_{\text{A}}}$ và $y = \dfrac{m_{\text{B}}}{M_{\text{B}}}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Copper(II) sulfate có công thức hóa học là $\text{CuSO}_4$. Biết $M_{\text{Cu}} = 64\text{ g/mol}$, "
                    r"$M_{\text{S}} = 32\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$. Hãy tính khối lượng phân tử và thành phần "
                    r"phần trăm theo khối lượng của từng nguyên tố trong $\text{CuSO}_4$."
                ),
                "solution": (
                    r"Khối lượng phân tử của $\text{CuSO}_4$ là $M_{\text{CuSO}_4} = 64 + 32 + 4 \cdot 16 = 160\text{ g/mol}$. "
                    r"Thành phần phần trăm theo khối lượng của các nguyên tố là: "
                    r"$\text{\%}m_{\text{Cu}} = \dfrac{64}{160} \cdot 100\text{\%} = 40\text{\%}$; "
                    r"$\text{\%}m_{\text{S}} = \dfrac{32}{160} \cdot 100\text{\%} = 20\text{\%}$; "
                    r"$\text{\%}m_{\text{O}} = 100\text{\%} - 40\text{\%} - 20\text{\%} = 40\text{\%}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Một oxide của iron có thành phần phần trăm theo khối lượng của iron là $70\text{\%}$, còn lại là oxygen. "
                    r"Biết khối lượng phân tử của oxide đó là $160\text{ amu}$ ($M_{\text{Fe}} = 56\text{ amu}$, $M_{\text{O}} = 16\text{ amu}$). "
                    r"Hãy xác định công thức hóa học của oxide."
                ),
                "solution": (
                    r"Đặt công thức hóa học của oxide là $\text{Fe}_x\text{O}_y$. Ta có $\text{\%}m_{\text{O}} = 100\text{\%} - 70\text{\%} = 30\text{\%}$. "
                    r"Số nguyên tử $\text{Fe}$ là $x = \dfrac{70 \cdot 160}{100 \cdot 56} = 2$; số nguyên tử $\text{O}$ là "
                    r"$y = \dfrac{30 \cdot 160}{100 \cdot 16} = 3$. Vậy công thức hóa học của oxide là $\text{Fe}_2\text{O}_3$ (iron(III) oxide)."
                ),
            },
        ],
        key_takeaways=[
            r"Công thức hóa học cho biết thành phần nguyên tố, số nguyên tử của mỗi nguyên tố trong một phân tử và khối lượng phân tử của chất.",
            r"Quy tắc hóa trị $a \cdot x = b \cdot y$ là cơ sở để tính hóa trị chưa biết hoặc lập nhanh công thức hóa học với tỉ lệ tối giản $\dfrac{x}{y} = \dfrac{b}{a}$.",
            r"Phần trăm khối lượng của nguyên tố $\text{A}$ trong $\text{A}_x\text{B}_y$ luôn tính bằng $\text{\%}m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{A}_x\text{B}_y}} \cdot 100\text{\%}$.",
        ],
        questions=[
            mcq(
                question=r"Công thức hóa học của đơn chất khí oxygen ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là:",
                options=[r"$\text{O}$", r"$\text{O}_2$", r"$\text{O}_3$", r"$\text{2O}$"],
                answer="B",
                level="biet",
                solution=r"Ở điều kiện chuẩn, đơn chất khí oxygen tồn tại dưới dạng phân tử gồm hai nguyên tử liên kết với nhau nên có công thức hóa học là $\text{O}_2$.",
            ),
            mcq(
                question=r"Trong hợp chất sulfur trioxide có công thức hóa học $\text{SO}_3$, biết $\text{O}$ có hóa trị $\text{II}$ thì hóa trị của nguyên tố sulfur ($\text{S}$) là:",
                options=[r"$\text{II}$", r"$\text{III}$", r"$\text{IV}$", r"$\text{VI}$"],
                answer="D",
                level="biet",
                solution=r"Theo quy tắc hóa trị đối với $\overset{a}{\text{S}}_1\overset{\text{II}}{\text{O}}_3$, ta có $a \cdot 1 = \text{II} \cdot 3 \Rightarrow a = \text{VI}$.",
            ),
            mcq(
                question=r"Công thức hóa học của aluminium sulfate (biết $\text{Al}$ hóa trị $\text{III}$ và nhóm $\text{SO}_4$ hóa trị $\text{II}$) là:",
                options=[
                    r"$\text{AlSO}_4$",
                    r"$\text{Al}_2\text{SO}_4$",
                    r"$\text{Al}_2(\text{SO}_4)_3$",
                    r"$\text{Al}_3(\text{SO}_4)_2$",
                ],
                answer="C",
                level="biet",
                solution=r"Áp dụng quy tắc hóa trị cho $\overset{\text{III}}{\text{Al}}_x(\overset{\text{II}}{\text{SO}_4})_y$, ta có $\dfrac{x}{y} = \dfrac{2}{3}$, vậy công thức hóa học là $\text{Al}_2(\text{SO}_4)_3$.",
            ),
            mcq(
                question=r"Khối lượng phân tử của calcium carbonate ($\text{CaCO}_3$, biết $M_{\text{Ca}} = 40\text{ amu}$, $M_{\text{C}} = 12\text{ amu}$, $M_{\text{O}} = 16\text{ amu}$) bằng:",
                options=[
                    r"$68\text{ amu}$",
                    r"$84\text{ amu}$",
                    r"$100\text{ amu}$",
                    r"$116\text{ amu}$",
                ],
                answer="C",
                level="biet",
                solution=r"Ta có $M_{\text{CaCO}_3} = 40 + 12 + 3 \cdot 16 = 100\text{ amu}$.",
            ),
            mcq(
                question=r"Thành phần phần trăm theo khối lượng của nguyên tố nitrogen ($\text{N}$) trong phân đạm ammonium nitrate ($\text{NH}_4\text{NO}_3$, biết $M_{\text{N}} = 14\text{ g/mol}$, $M_{\text{H}} = 1\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$) là:",
                options=[r"$17{,}5\text{\%}$", r"$28{,}0\text{\%}$", r"$35{,}0\text{\%}$", r"$46{,}67\text{\%}$"],
                answer="C",
                level="hieu",
                solution=r"Khối lượng phân tử $M_{\text{NH}_4\text{NO}_3} = 2 \cdot 14 + 4 \cdot 1 + 3 \cdot 16 = 80\text{ g/mol}$. Phần trăm khối lượng của $\text{N}$ là $\text{\%}m_{\text{N}} = \dfrac{2 \cdot 14}{80} \cdot 100\text{\%} = 35{,}0\text{\%}$.",
            ),
            mcq(
                question=r"Một hợp chất khí $\text{X}$ gồm hai nguyên tố carbon và hydrogen có $\text{\%}m_{\text{C}} = 75\text{\%}$, khối lượng phân tử bằng $16\text{ amu}$ ($M_{\text{C}} = 12\text{ amu}$, $M_{\text{H}} = 1\text{ amu}$). Công thức hóa học của $\text{X}$ là:",
                options=[r"$\text{CH}_4$", r"$\text{C}_2\text{H}_4$", r"$\text{C}_2\text{H}_6$", r"$\text{C}_2\text{H}_2$"],
                answer="A",
                level="hieu",
                solution=r"Đặt công thức là $\text{C}_x\text{H}_y$. Ta có $\text{\%}m_{\text{H}} = 100\text{\%} - 75\text{\%} = 25\text{\%}$. Suy ra $x = \dfrac{75 \cdot 16}{100 \cdot 12} = 1$ và $y = \dfrac{25 \cdot 16}{100 \cdot 1} = 4$. Vậy công thức là $\text{CH}_4$ (methane).",
            ),
            tf4(
                stem=r"Cho hợp chất iron(III) sulfate có công thức hóa học là $\text{Fe}_2(\text{SO}_4)_3$ (biết $M_{\text{Fe}} = 56\text{ amu}$, $M_{\text{S}} = 32\text{ amu}$, $M_{\text{O}} = 16\text{ amu}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Hợp chất $\text{Fe}_2(\text{SO}_4)_3$ được tạo nên từ $3$ nguyên tố hóa học là $\text{Fe}$, $\text{S}$ và $\text{O}$.",
                    r"b) Trong một phân tử $\text{Fe}_2(\text{SO}_4)_3$ có tất cả $12$ nguyên tử các nguyên tố.",
                    r"c) Khối lượng phân tử của $\text{Fe}_2(\text{SO}_4)_3$ bằng $400\text{ amu}$.",
                    r"d) Phần trăm khối lượng của nguyên tố $\text{Fe}$ trong $\text{Fe}_2(\text{SO}_4)_3$ bằng $42\text{\%}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì hợp chất tạo bởi ba nguyên tố iron ($\text{Fe}$), sulfur ($\text{S}$) và oxygen ($\text{O}$). "
                    r"b) Sai vì tổng số nguyên tử trong một phân tử là $2 + 3 \cdot (1 + 4) = 17$ nguyên tử. "
                    r"c) Đúng vì $M_{\text{Fe}_2(\text{SO}_4)_3} = 2 \cdot 56 + 3 \cdot (32 + 4 \cdot 16) = 112 + 288 = 400\text{ amu}$. "
                    r"d) Sai vì $\text{\%}m_{\text{Fe}} = \dfrac{112}{400} \cdot 100\text{\%} = 28\text{\%}$."
                ),
            ),
            tf4(
                stem=r"Một hợp chất hữu cơ $\text{Y}$ là thành phần chính của giấm ăn, có công thức phân tử $\text{C}_2\text{H}_4\text{O}_2$ (biết $M_{\text{C}} = 12\text{ g/mol}$, $M_{\text{H}} = 1\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Khối lượng phân tử của hợp chất $\text{Y}$ là $60\text{ amu}$.",
                    r"b) Tỉ lệ số nguyên tử $\text{C} : \text{H} : \text{O}$ tối giản trong phân tử $\text{Y}$ là $1 : 4 : 1$.",
                    r"c) Phần trăm khối lượng của nguyên tố carbon trong $\text{Y}$ là $40\text{\%}$.",
                    r"d) Phần trăm khối lượng của nguyên tố oxygen trong $\text{Y}$ nhỏ hơn phần trăm khối lượng của nguyên tố carbon.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $M_{\text{C}_2\text{H}_4\text{O}_2} = 2 \cdot 12 + 4 \cdot 1 + 2 \cdot 16 = 60\text{ amu}$. "
                    r"b) Sai vì tỉ lệ số nguyên tử $\text{C} : \text{H} : \text{O} = 2 : 4 : 2 = 1 : 2 : 1$. "
                    r"c) Đúng vì $\text{\%}m_{\text{C}} = \dfrac{24}{60} \cdot 100\text{\%} = 40\text{\%}$. "
                    r"d) Sai vì $\text{\%}m_{\text{O}} = \dfrac{32}{60} \cdot 100\text{\%} \approx 53{,}33\text{\%} > 40\text{\%}$."
                ),
            ),
            mcq(
                question=r"Một loại quặng hematite chứa $80\text{\%}$ khối lượng là iron(III) oxide ($\text{Fe}_2\text{O}_3$), phần còn lại là tạp chất trơ không chứa iron. Khối lượng nguyên tố iron ($\text{Fe}$) có trong $1{,}5\text{ tấn}$ quặng trên (biết $M_{\text{Fe}} = 56\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$) là:",
                options=[
                    r"$0{,}56\text{ tấn}$",
                    r"$0{,}84\text{ tấn}$",
                    r"$1{,}05\text{ tấn}$",
                    r"$1{,}20\text{ tấn}$",
                ],
                answer="B",
                level="vandung",
                solution=r"Khối lượng $\text{Fe}_2\text{O}_3$ trong quặng là $m_{\text{Fe}_2\text{O}_3} = 1{,}5 \cdot 80\text{\%} = 1{,}2\text{ tấn}$. Phần trăm khối lượng $\text{Fe}$ trong $\text{Fe}_2\text{O}_3$ là $\text{\%}m_{\text{Fe}} = \dfrac{2 \cdot 56}{160} \cdot 100\text{\%} = 70\text{\%}$. Vậy khối lượng $\text{Fe}$ là $m_{\text{Fe}} = 1{,}2 \cdot 70\text{\%} = 0{,}84\text{ tấn}$.",
            ),
            short(
                question=r"Tính thành phần phần trăm theo khối lượng (theo đơn vị $\text{\%}$, làm tròn đến chữ số hàng phần mười) của nguyên tố nitrogen ($\text{N}$) trong phân đạm urea có công thức hóa học $(\text{NH}_2)_2\text{CO}$ (biết $M_{\text{C}} = 12\text{ g/mol}$, $M_{\text{N}} = 14\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$, $M_{\text{H}} = 1\text{ g/mol}$).",
                answer=["46,7", "46.7", "46,67", "46.67"],
                level="vandung",
                solution=r"Khối lượng phân tử của urea $(\text{NH}_2)_2\text{CO}$ là $M = 2 \cdot (14 + 2 \cdot 1) + 12 + 16 = 60\text{ g/mol}$. Phần trăm khối lượng của $\text{N}$ là $\text{\%}m_{\text{N}} = \dfrac{2 \cdot 14}{60} \cdot 100\text{\%} = \dfrac{28}{60} \cdot 100\text{\%} \approx 46{,}7\text{\%}$.",
            ),
        ],
        description="Ý nghĩa công thức hóa học của đơn chất và hợp chất, quy tắc hóa trị, tính phần trăm khối lượng nguyên tố và xác định công thức hóa học theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=2,
        code="H8-C02",
        title="Chương 2: Mol, khối lượng mol, thể tích mol chất khí và tỉ khối",
        topic="mol-va-khoi-luong-mol",
        summary=(
            r"Nắm vững khái niệm mol và hằng số Avogadro $N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$, "
            r"khối lượng mol $M = \dfrac{m}{n}$, thể tích mol chất khí ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) "
            r"$V = 24{,}79 \cdot n\text{ (L)}$ và tỉ khối của chất khí $d_{\text{A/B}} = \dfrac{M_{\text{A}}}{M_{\text{B}}}$, $d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$."
        ),
        objectives=[
            r"Nêu được khái niệm mol, hằng số Avogadro $N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$ và tính được số hạt vi mô $N = n \cdot N_{\text{A}}$.",
            r"Nêu được khái niệm khối lượng mol ($M$) và vận dụng công thức $n = \dfrac{m}{M}$ để chuyển đổi giữa số mol và khối lượng chất.",
            r"Trình bày được khái niệm thể tích mol chất khí ở điều kiện chuẩn ($25^\circ\text{C}$ và $1\text{ bar}$) và vận dụng được công thức $V = 24{,}79 \cdot n\text{ (L)}$.",
            r"Vận dụng được công thức tỉ khối chất khí $d_{\text{A/B}} = \dfrac{M_{\text{A}}}{M_{\text{B}}}$ và $d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$ để so sánh khí nặng hay nhẹ hơn khí khác và hơn không khí.",
        ],
        formulas=[
            {
                "name": "Quan hệ giữa số mol và số hạt vi mô (nguyên tử, phân tử)",
                "formula": r"$N = n \cdot N_{\text{A}} \Rightarrow n = \dfrac{N}{N_{\text{A}}} \quad (N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1})$",
                "note": r"$n$: lượng chất ($\text{mol}$); $N$: số nguyên tử hoặc phân tử",
            },
            {
                "name": "Quan hệ giữa khối lượng chất, số mol và khối lượng mol",
                "formula": r"$M = \dfrac{m}{n} \Rightarrow m = n \cdot M; \quad n = \dfrac{m}{M}$",
                "note": r"$m$: khối lượng chất ($\text{g}$); $M$: khối lượng mol ($\text{g/mol}$)",
            },
            {
                "name": r"Thể tích mol chất khí ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$)",
                "formula": r"$V = 24{,}79 \cdot n \Rightarrow n = \dfrac{V}{24{,}79}$",
                "note": r"$V$: thể tích chất khí ở đkc ($\text{L}$); $1\text{ mol}$ khí bất kì ở đkc chiếm $24{,}79\text{ L}$",
            },
            {
                "name": "Tỉ khối của chất khí",
                "formula": r"$d_{\text{A/B}} = \dfrac{M_{\text{A}}}{M_{\text{B}}}; \quad d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$",
                "note": r"Khối lượng mol trung bình của không khí lấy bằng $29\text{ g/mol}$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Mol và khối lượng mol",
                "content": (
                    r"Mol là lượng chất có chứa $N_{\text{A}} = 6{,}022 \cdot 10^{23}$ hạt vi mô (nguyên tử, phân tử, hoặc ion) của chất đó; "
                    r"con số $6{,}022 \cdot 10^{23}\text{ mol}^{-1}$ được gọi là hằng số Avogadro ($N_{\text{A}}$). "
                    r"Khối lượng mol (kí hiệu là $M$, đơn vị thường dùng là $\text{g/mol}$) của một chất là khối lượng tính bằng gam của $N_{\text{A}}$ "
                    r"nguyên tử hoặc phân tử chất đó. Khối lượng mol nguyên tử hay phân tử của một chất (theo $\text{g/mol}$) có cùng trị số với "
                    r"khối lượng nguyên tử hay phân tử của chất đó tính theo đơn vị $\text{amu}$."
                ),
            },
            {
                "title": "2. Thể tích mol chất khí ở điều kiện chuẩn",
                "content": (
                    r"Thể tích mol của chất khí là thể tích chiếm bởi $N_{\text{A}}$ phân tử ($1\text{ mol}$) của chất khí đó. "
                    r"Ở cùng điều kiện về nhiệt độ và áp suất, $1\text{ mol}$ của bất kì chất khí nào đều chiếm những thể tích bằng nhau. "
                    r"Ở điều kiện chuẩn (nhiệt độ $25^\circ\text{C}$ và áp suất $1\text{ bar}$), $1\text{ mol}$ chất khí bất kì đều chiếm thể tích "
                    r"bằng $24{,}79\text{ L}$. Do đó thể tích của $n\text{ mol}$ khí ở điều kiện chuẩn được tính bằng $V = 24{,}79 \cdot n\text{ (L)}$."
                ),
            },
            {
                "title": "3. Tỉ khối của chất khí và ứng dụng thu khí",
                "content": (
                    r"Để biết khí $\text{A}$ nặng hay nhẹ hơn khí $\text{B}$ bao nhiêu lần, ta dựa vào tỉ khối $d_{\text{A/B}} = \dfrac{M_{\text{A}}}{M_{\text{B}}}$. "
                    r"Để biết khí $\text{A}$ nặng hay nhẹ hơn không khí bao nhiêu lần, ta tính $d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$ (vì $1\text{ mol}$ không khí "
                    r"có khoảng $0{,}8\text{ mol }\text{N}_2$ và $0{,}2\text{ mol }\text{O}_2$ nên $M_{\text{kk}} \approx 28 \cdot 0{,}8 + 32 \cdot 0{,}2 \approx 29\text{ g/mol}$). "
                    r"Khi thu khí bằng phương pháp đẩy không khí: nếu $d_{\text{A/kk}} > 1$ (như $\text{CO}_2, \text{SO}_2, \text{Cl}_2, \text{O}_2$) thì đặt đứng bình (ngửa bình); "
                    r"nếu $d_{\text{A/kk}} < 1$ (như $\text{H}_2, \text{CH}_4, \text{NH}_3$) thì đặt úp bình."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Tính số phân tử, khối lượng và thể tích ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) của $0{,}2\text{ mol}$ "
                    r"khí carbon dioxide ($\text{CO}_2$, biết $M_{\text{C}} = 12\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$)."
                ),
                "solution": (
                    r"Số phân tử $\text{CO}_2$ là $N = n \cdot N_{\text{A}} = 0{,}2 \cdot 6{,}022 \cdot 10^{23} = 1{,}2044 \cdot 10^{23}\text{ phân tử}$. "
                    r"Khối lượng mol của $\text{CO}_2$ là $M_{\text{CO}_2} = 12 + 2 \cdot 16 = 44\text{ g/mol}$, nên khối lượng là "
                    r"$m = n \cdot M = 0{,}2 \cdot 44 = 8{,}8\text{ g}$. Thể tích khí $\text{CO}_2$ ở đkc là $V = 24{,}79 \cdot n = 24{,}79 \cdot 0{,}2 = 4{,}958\text{ L}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Một chất khí $\text{X}$ có tỉ khối đối với khí hydrogen ($\text{H}_2$) bằng $22$. Hãy tính khối lượng mol của khí $\text{X}$ "
                    r"và cho biết khí $\text{X}$ nặng hay nhẹ hơn không khí bao nhiêu lần."
                ),
                "solution": (
                    r"Từ công thức $d_{\text{X/H}_2} = \dfrac{M_{\text{X}}}{M_{\text{H}_2}} = \dfrac{M_{\text{X}}}{2} = 22$, suy ra "
                    r"$M_{\text{X}} = 22 \cdot 2 = 44\text{ g/mol}$. Tỉ khối của $\text{X}$ đối với không khí là $d_{\text{X/kk}} = \dfrac{44}{29} \approx 1{,}52$, "
                    r"vậy khí $\text{X}$ nặng hơn không khí khoảng $1{,}52$ lần."
                ),
            },
        ],
        key_takeaways=[
            r"Hằng số Avogadro $N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$ biểu thị số hạt vi mô trong đúng $1\text{ mol}$ chất.",
            r"Ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$), $1\text{ mol}$ chất khí bất kì luôn chiếm thể tích $24{,}79\text{ L}$ ($V = 24{,}79 \cdot n$).",
            r"Tỉ khối chất khí $d_{\text{A/B}} = \dfrac{M_{\text{A}}}{M_{\text{B}}}$ và $d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$ giúp xác định khối lượng mol chất khí và cách đặt bình khi thu khí.",
        ],
        questions=[
            mcq(
                question=r"Ở điều kiện chuẩn (nhiệt độ $25^\circ\text{C}$ và áp suất $1\text{ bar}$), $1\text{ mol}$ của bất kì chất khí nào đều chiếm thể tích bằng:",
                options=[r"$22{,}4\text{ L}$", r"$24{,}0\text{ L}$", r"$24{,}79\text{ L}$", r"$25{,}0\text{ L}$"],
                answer="C",
                level="biet",
                solution=r"Theo chuẩn Chương trình GDPT 2018, ở điều kiện chuẩn ($25^\circ\text{C}$ và $1\text{ bar}$), $1\text{ mol}$ khí bất kì chiếm thể tích là $24{,}79\text{ L}$.",
            ),
            mcq(
                question=r"Giá trị của hằng số Avogadro ($N_{\text{A}}$) là:",
                options=[
                    r"$6{,}022 \cdot 10^{22}\text{ mol}^{-1}$",
                    r"$6{,}022 \cdot 10^{23}\text{ mol}^{-1}$",
                    r"$24{,}79 \cdot 10^{23}\text{ mol}^{-1}$",
                    r"$1{,}602 \cdot 10^{-19}\text{ mol}^{-1}$",
                ],
                answer="B",
                level="biet",
                solution=r"Hằng số Avogadro có giá trị $N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$.",
            ),
            mcq(
                question=r"Công thức tính tỉ khối của chất khí $\text{A}$ đối với không khí là:",
                options=[
                    r"$d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$",
                    r"$d_{\text{A/kk}} = \dfrac{29}{M_{\text{A}}}$",
                    r"$d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{24{,}79}$",
                    r"$d_{\text{A/kk}} = 29 \cdot M_{\text{A}}$",
                ],
                answer="A",
                level="biet",
                solution=r"Tỉ khối của khí $\text{A}$ so với không khí được tính theo công thức $d_{\text{A/kk}} = \dfrac{M_{\text{A}}}{29}$.",
            ),
            mcq(
                question=r"Số mol của $18\text{ g}$ nước ($\text{H}_2\text{O}$, biết $M_{\text{H}} = 1\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$) là:",
                options=[r"$0{,}5\text{ mol}$", r"$1{,}0\text{ mol}$", r"$1{,}5\text{ mol}$", r"$2{,}0\text{ mol}$"],
                answer="B",
                level="biet",
                solution=r"Ta có $M_{\text{H}_2\text{O}} = 2 \cdot 1 + 16 = 18\text{ g/mol}$. Số mol nước là $n = \dfrac{m}{M} = \dfrac{18}{18} = 1{,}0\text{ mol}$.",
            ),
            mcq(
                question=r"Thể tích ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) của $16\text{ g}$ khí oxygen ($\text{O}_2$, biết $M_{\text{O}} = 16\text{ g/mol}$) là:",
                options=[
                    r"$11{,}20\text{ L}$",
                    r"$12{,}395\text{ L}$",
                    r"$24{,}79\text{ L}$",
                    r"$49{,}58\text{ L}$",
                ],
                answer="B",
                level="hieu",
                solution=r"Khối lượng mol của khí oxygen là $M_{\text{O}_2} = 32\text{ g/mol}$. Số mol $\text{O}_2$ là $n = \dfrac{16}{32} = 0{,}5\text{ mol}$. Thể tích ở đkc là $V = 24{,}79 \cdot 0{,}5 = 12{,}395\text{ L}$.",
            ),
            mcq(
                question=r"Trong số các chất khí sau: $\text{H}_2$ ($M = 2\text{ g/mol}$), $\text{CH}_4$ ($M = 16\text{ g/mol}$), $\text{NH}_3$ ($M = 17\text{ g/mol}$) và $\text{SO}_2$ ($M = 64\text{ g/mol}$), chất khí nặng hơn không khí là:",
                options=[r"$\text{H}_2$", r"$\text{CH}_4$", r"$\text{NH}_3$", r"$\text{SO}_2$"],
                answer="D",
                level="hieu",
                solution=r"Khí nặng hơn không khí phải có $M > 29\text{ g/mol}$. Trong các khí đã cho, chỉ có $\text{SO}_2$ có $M = 64\text{ g/mol} > 29\text{ g/mol}$.",
            ),
            tf4(
                stem=r"Một bình kín chứa $7{,}437\text{ L}$ khí nitrogen ($\text{N}_2$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$). Biết $M_{\text{N}} = 14\text{ g/mol}$ và $N_{\text{A}} = 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Số mol khí $\text{N}_2$ trong bình là $0{,}3\text{ mol}$.",
                    r"b) Khối lượng mol phân tử của khí $\text{N}_2$ bằng $14\text{ g/mol}$.",
                    r"c) Khối lượng khí $\text{N}_2$ chứa trong bình bằng $8{,}4\text{ g}$.",
                    r"d) Số nguyên tử nitrogen có trong bình là $1{,}8066 \cdot 10^{23}\text{ nguyên tử}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $n_{\text{N}_2} = \dfrac{V}{24{,}79} = \dfrac{7{,}437}{24{,}79} = 0{,}3\text{ mol}$. "
                    r"b) Sai vì phân tử khí nitrogen gồm $2$ nguyên tử $\text{N}$ nên $M_{\text{N}_2} = 2 \cdot 14 = 28\text{ g/mol}$. "
                    r"c) Đúng vì $m_{\text{N}_2} = n \cdot M = 0{,}3 \cdot 28 = 8{,}4\text{ g}$. "
                    r"d) Sai vì số phân tử $\text{N}_2$ là $0{,}3 \cdot 6{,}022 \cdot 10^{23} = 1{,}8066 \cdot 10^{23}$, còn số nguyên tử $\text{N}$ phải gấp đôi là $3{,}6132 \cdot 10^{23}\text{ nguyên tử}$."
                ),
            ),
            tf4(
                stem=r"Cho hai chất khí ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là khí methane ($\text{CH}_4$, $M = 16\text{ g/mol}$) và khí carbon dioxide ($\text{CO}_2$, $M = 44\text{ g/mol}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Khí $\text{CH}_4$ nhẹ hơn không khí nên khi thu khí $\text{CH}_4$ bằng phương pháp đẩy không khí phải đặt úp bình thu.",
                    r"b) Tỉ khối của khí $\text{CO}_2$ so với khí $\text{CH}_4$ bằng $2{,}5$.",
                    r"c) Ở cùng điều kiện chuẩn, $1\text{ mol}$ khí $\text{CH}_4$ và $1\text{ mol}$ khí $\text{CO}_2$ có cùng thể tích là $24{,}79\text{ L}$.",
                    r"d) Cùng một khối lượng $16\text{ g}$, khí $\text{CO}_2$ có số phân tử nhiều hơn số phân tử của khí $\text{CH}_4$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $d_{\text{CH}_4\text{/kk}} = \dfrac{16}{29} < 1$ nên khí $\text{CH}_4$ nhẹ hơn không khí, phải đặt úp bình thu. "
                    r"b) Sai vì $d_{\text{CO}_2\text{/CH}_4} = \dfrac{44}{16} = 2{,}75$. "
                    r"c) Đúng vì ở đkc ($25^\circ\text{C}$, $1\text{ bar}$), $1\text{ mol}$ của mọi chất khí đều có thể tích $24{,}79\text{ L}$. "
                    r"d) Sai vì với cùng khối lượng $16\text{ g}$, $n_{\text{CO}_2} = \dfrac{16}{44}\text{ mol} < n_{\text{CH}_4} = \dfrac{16}{16} = 1\text{ mol}$ nên số phân tử $\text{CO}_2$ ít hơn."
                ),
            ),
            mcq(
                question=r"Một hỗn hợp khí $\text{X}$ ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) gồm $0{,}2\text{ mol}$ khí $\text{O}_2$ ($M = 32\text{ g/mol}$) và $0{,}3\text{ mol}$ khí $\text{CO}_2$ ($M = 44\text{ g/mol}$). Tỉ khối của hỗn hợp khí $\text{X}$ đối với khí $\text{H}_2$ ($M = 2\text{ g/mol}$) là:",
                options=[r"$18{,}0$", r"$19{,}6$", r"$20{,}4$", r"$39{,}2$"],
                answer="B",
                level="vandung",
                solution=r"Tổng số mol hỗn hợp là $n_{\text{X}} = 0{,}2 + 0{,}3 = 0{,}5\text{ mol}$. Tổng khối lượng hỗn hợp là $m_{\text{X}} = 0{,}2 \cdot 32 + 0{,}3 \cdot 44 = 6{,}4 + 13{,}2 = 19{,}6\text{ g}$. Khối lượng mol trung bình của hỗn hợp là $\overline{M}_{\text{X}} = \dfrac{19{,}6}{0{,}5} = 39{,}2\text{ g/mol}$. Vậy tỉ khối đối với $\text{H}_2$ là $d_{\text{X/H}_2} = \dfrac{39{,}2}{2} = 19{,}6$.",
            ),
            short(
                question=r"Tính thể tích (theo đơn vị $\text{L}$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) của $6{,}4\text{ g}$ khí sulfur dioxide ($\text{SO}_2$, biết $M_{\text{S}} = 32\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$).",
                answer=["2,479", "2.479"],
                level="vandung",
                solution=r"Khối lượng mol của $\text{SO}_2$ là $M_{\text{SO}_2} = 32 + 2 \cdot 16 = 64\text{ g/mol}$. Số mol $\text{SO}_2$ là $n = \dfrac{6{,}4}{64} = 0{,}1\text{ mol}$. Thể tích khí $\text{SO}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}1 = 2{,}479\text{ L}$.",
            ),
        ],
        description="Khái niệm mol, hằng số Avogadro, khối lượng mol, thể tích mol chất khí ở điều kiện chuẩn và tỉ khối của chất khí theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=3,
        code="H8-C03",
        title="Chương 3: Phương trình hóa học, tính theo phương trình và hiệu suất phản ứng",
        topic="phuong-trinh-hoa-hoc",
        summary=(
            r"Nắm vững định luật bảo toàn khối lượng $m_{\text{tham gia}} = m_{\text{sản phẩm}}$, các bước lập và cân bằng phương trình hóa học, "
            r"bài toán tính lượng chất theo phương trình hóa học (kể cả bài toán lượng dư) và công thức hiệu suất phản ứng "
            r"$H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$."
        ),
        objectives=[
            r"Phát biểu và vận dụng được Định luật bảo toàn khối lượng để tính khối lượng chất chưa biết trong phản ứng hóa học.",
            r"Thực hiện được các bước lập phương trình hóa học và xác định được tỉ lệ số nguyên tử, số phân tử hay tỉ lệ số mol giữa các chất trong phương trình.",
            r"Tính được lượng chất tham gia hoặc lượng sản phẩm (theo số mol, khối lượng hoặc thể tích khí ở đkc) dựa vào phương trình hóa học.",
            r"Nêu được khái niệm hiệu suất phản ứng và vận dụng được công thức $H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$ để giải bài toán thực tế.",
        ],
        formulas=[
            {
                "name": "Định luật bảo toàn khối lượng",
                "formula": r"$\text{A} + \text{B} \longrightarrow \text{C} + \text{D} \implies m_{\text{A}} + m_{\text{B}} = m_{\text{C}} + m_{\text{D}}$",
                "note": r"Tổng khối lượng các chất phản ứng bằng tổng khối lượng các chất sản phẩm",
            },
            {
                "name": "Tỉ lệ số mol theo phương trình hóa học",
                "formula": r"$a\text{A} + b\text{B} \longrightarrow c\text{C} + d\text{D} \implies \dfrac{n_{\text{A}}}{a} = \dfrac{n_{\text{B}}}{b} = \dfrac{n_{\text{C}}}{c} = \dfrac{n_{\text{D}}}{d}$",
                "note": r"Nếu cho số mol cả $\text{A}$ và $\text{B}$, so sánh $\dfrac{n_{\text{A}}}{a}$ và $\dfrac{n_{\text{B}}}{b}$ để tìm chất hết, chất dư",
            },
            {
                "name": "Hiệu suất phản ứng tính theo sản phẩm hoặc chất tham gia",
                "formula": r"$H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%} = \dfrac{m_{\text{thực tế}}}{m_{\text{lý thuyết}}} \cdot 100\text{\%}$",
                "note": r"Thực tế luôn có $0\text{\%} < H \le 100\text{\%}$",
            },
            {
                "name": "Quy tắc tính lượng sản phẩm và chất tham gia khi có hiệu suất $H$",
                "formula": r"$m_{\text{sp thực tế}} = m_{\text{sp lý thuyết}} \cdot \dfrac{H}{100\text{\%}}; \quad m_{\text{tg cần dùng}} = m_{\text{tg lý thuyết}} \cdot \dfrac{100\text{\%}}{H}$",
                "note": r"Nhân $\dfrac{H}{100\text{\%}}$ khi tìm sản phẩm; chia $\dfrac{H}{100\text{\%}}$ khi tìm lượng nguyên liệu ban đầu",
            },
        ],
        theory_sections=[
            {
                "title": "1. Định luật bảo toàn khối lượng và phương trình hóa học",
                "content": (
                    r"Trong một phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi làm phân tử này biến đổi thành phân tử khác, "
                    r"còn số nguyên tử của mỗi nguyên tố trước và sau phản ứng giữ nguyên, vì vậy tổng khối lượng các chất tham gia phản ứng "
                    r"luôn bằng tổng khối lượng các sản phẩm tạo thành. Để lập phương trình hóa học: (1) Viết sơ đồ phản ứng gồm công thức "
                    r"hóa học của các chất tham gia và sản phẩm; (2) Cân bằng số nguyên tử của mỗi nguyên tố ở hai vế bằng cách đặt hệ số "
                    r"nguyên dương tối giản trước công thức hóa học (không thay đổi chỉ số trong công thức); (3) Viết thành phương trình hóa học."
                ),
            },
            {
                "title": "2. Tính theo phương trình hóa học và bài toán lượng dư",
                "content": (
                    r"Các bước tính theo phương trình hóa học: Bước 1: Đổi dữ kiện đề bài ra số mol ($n = \dfrac{m}{M}$ hoặc $n = \dfrac{V}{24{,}79}$ ở đkc). "
                    r"Bước 2: Viết và cân bằng phương trình hóa học. Bước 3: Dựa vào tỉ lệ hệ số trong phương trình để tìm số mol chất cần tính "
                    r"(nếu đề bài cho số mol của hai chất tham gia trong phản ứng $a\text{A} + b\text{B} \longrightarrow c\text{C}$, ta lập tỉ số "
                    r"$\dfrac{n_{\text{A}}}{a}$ và $\dfrac{n_{\text{B}}}{b}$; tỉ số nào nhỏ hơn thì chất đó phản ứng hết và mọi tính toán phải tính theo chất hết). "
                    r"Bước 4: Chuyển đổi số mol tìm được sang khối lượng ($m = n \cdot M$) hoặc thể tích khí ở đkc ($V = 24{,}79 \cdot n$)."
                ),
            },
            {
                "title": "3. Hiệu suất phản ứng hóa học",
                "content": (
                    r"Trong thực tế sản xuất và thí nghiệm, do phản ứng không xảy ra hoàn toàn hoặc bị hao hụt trong quá trình thu hồi, lượng sản phẩm "
                    r"thu được thực tế ($n_{\text{thực tế}}$ hoặc $m_{\text{thực tế}}$) thường nhỏ hơn lượng tính theo phương trình hóa học ($n_{\text{lý thuyết}}$ "
                    r"hoặc $m_{\text{lý thuyết}}$). Hiệu suất phản ứng $H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$ cho biết mức độ "
                    r"hiệu quả của quá trình chuyển hóa các chất."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Cho $5{,}6\text{ g}$ iron ($\text{Fe}$, $M = 56\text{ g/mol}$) tác dụng vừa đủ với dung dịch hydrochloric acid ($\text{HCl}$) "
                    r"theo phản ứng: $\text{Fe} + 2\text{HCl} \longrightarrow \text{FeCl}_2 + \text{H}_2\uparrow$. Tính thể tích khí $\text{H}_2$ "
                    r"thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) và khối lượng muối $\text{FeCl}_2$ ($M_{\text{Cl}} = 35{,}5\text{ g/mol}$) tạo thành."
                ),
                "solution": (
                    r"Số mol $\text{Fe}$ phản ứng là $n_{\text{Fe}} = \dfrac{5{,}6}{56} = 0{,}1\text{ mol}$. Theo phương trình hóa học "
                    r"$\text{Fe} + 2\text{HCl} \longrightarrow \text{FeCl}_2 + \text{H}_2\uparrow$, ta có $n_{\text{H}_2} = n_{\text{FeCl}_2} = n_{\text{Fe}} = 0{,}1\text{ mol}$. "
                    r"Thể tích khí $\text{H}_2$ ở đkc là $V_{\text{H}_2} = 24{,}79 \cdot 0{,}1 = 2{,}479\text{ L}$. Khối lượng muối $\text{FeCl}_2$ ($M = 56 + 71 = 127\text{ g/mol}$) "
                    r"là $m_{\text{FeCl}_2} = 0{,}1 \cdot 127 = 12{,}7\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Nung nóng $20\text{ g}$ đá vôi chứa $\text{CaCO}_3$ nguyên chất ($M = 100\text{ g/mol}$) thu được $8{,}96\text{ g}$ calcium oxide ($\text{CaO}$, "
                    r"$M = 56\text{ g/mol}$) theo phương trình $\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$. Tính hiệu suất của phản ứng nung vôi."
                ),
                "solution": (
                    r"Số mol $\text{CaCO}_3$ ban đầu là $n_{\text{CaCO}_3} = \dfrac{20}{100} = 0{,}2\text{ mol}$. Theo phương trình hóa học, số mol $\text{CaO}$ "
                    r"thu được theo lý thuyết là $n_{\text{CaO (lý thuyết)}} = 0{,}2\text{ mol}$, tương ứng khối lượng $m_{\text{CaO (lý thuyết)}} = 0{,}2 \cdot 56 = 11{,}2\text{ g}$. "
                    r"Vậy hiệu suất phản ứng là $H = \dfrac{8{,}96}{11{,}2} \cdot 100\text{\%} = 80\text{\%}$."
                ),
            },
        ],
        key_takeaways=[
            r"Trong mọi phản ứng hóa học, số nguyên tử của mỗi nguyên tố được bảo toàn nên tổng khối lượng các chất tham gia bằng tổng khối lượng sản phẩm.",
            r"Hệ số các chất trong phương trình hóa học đã cân bằng chính là tỉ lệ số mol phản ứng của các chất đó.",
            r"Hiệu suất phản ứng được tính theo công thức $H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$ (tính theo lượng chất thiếu nếu có chất dư).",
        ],
        questions=[
            mcq(
                question=r"Sau khi cân bằng phương trình hóa học $x\text{Al} + y\text{O}_2 \xrightarrow{t^\circ} z\text{Al}_2\text{O}_3$ với các hệ số nguyên tối giản, bộ hệ số $(x, y, z)$ lần lượt là:",
                options=[
                    r"$(2, 3, 1)$",
                    r"$(4, 3, 2)$",
                    r"$(2, 1, 2)$",
                    r"$(3, 4, 2)$",
                ],
                answer="B",
                level="biet",
                solution=r"Để cân bằng số nguyên tử $\text{O}$ (BCNN của $2$ và $3$ là $6$), ta đặt hệ số $3$ trước $\text{O}_2$ và $2$ trước $\text{Al}_2\text{O}_3$, từ đó đặt $4$ trước $\text{Al}$: $4\text{Al} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{Al}_2\text{O}_3$.",
            ),
            mcq(
                question=r"Trong một phản ứng hóa học, đại lượng luôn được bảo toàn trước và sau phản ứng là:",
                options=[
                    r"Tổng số phân tử của các chất",
                    r"Tổng thể tích của các chất khí",
                    r"Số nguyên tử của mỗi nguyên tố và tổng khối lượng các chất",
                    r"Số liên kết hóa học trong phân tử",
                ],
                answer="C",
                level="biet",
                solution=r"Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi, còn số nguyên tử của mỗi nguyên tố giữ nguyên nên tổng khối lượng các chất được bảo toàn.",
            ),
            mcq(
                question=r"Cho phương trình hóa học: $\text{N}_2 + 3\text{H}_2 \xrightleftharpoons{t^\circ, p, xt} 2\text{NH}_3$. Tỉ lệ số mol $n_{\text{N}_2} : n_{\text{H}_2} : n_{\text{NH}_3}$ tham gia và tạo thành trong phản ứng là:",
                options=[
                    r"$1 : 2 : 3$",
                    r"$1 : 3 : 2$",
                    r"$2 : 3 : 1$",
                    r"$3 : 1 : 2$",
                ],
                answer="B",
                level="biet",
                solution=r"Tỉ lệ số mol phản ứng của các chất đúng bằng tỉ lệ hệ số cân bằng trong phương trình: $1 : 3 : 2$.",
            ),
            mcq(
                question=r"Công thức tính hiệu suất phản ứng ($H$) theo số mol sản phẩm thực tế thu được ($n_{\text{thực tế}}$) và số mol sản phẩm tính theo phương trình ($n_{\text{lý thuyết}}$) là:",
                options=[
                    r"$H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$",
                    r"$H = \dfrac{n_{\text{lý thuyết}}}{n_{\text{thực tế}}} \cdot 100\text{\%}$",
                    r"$H = (n_{\text{lý thuyết}} - n_{\text{thực tế}}) \cdot 100\text{\%}$",
                    r"$H = \dfrac{n_{\text{thực tế}}}{n_{\text{thực tế}} + n_{\text{lý thuyết}}} \cdot 100\text{\%}$",
                ],
                answer="A",
                level="biet",
                solution=r"Theo định nghĩa, hiệu suất phản ứng là $H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%}$.",
            ),
            mcq(
                question=r"Đốt cháy hoàn toàn $2{,}4\text{ g}$ kim loại magnesium ($\text{Mg}$) trong khí oxygen ($\text{O}_2$) thu được $4{,}0\text{ g}$ magnesium oxide ($\text{MgO}$). Theo định luật bảo toàn khối lượng, khối lượng khí $\text{O}_2$ đã phản ứng là:",
                options=[r"$0{,}8\text{ g}$", r"$1{,}6\text{ g}$", r"$2{,}4\text{ g}$", r"$6{,}4\text{ g}$"],
                answer="B",
                level="hieu",
                solution=r"Áp dụng định luật bảo toàn khối lượng cho phản ứng $2\text{Mg} + \text{O}_2 \xrightarrow{t^\circ} 2\text{MgO}$: $m_{\text{Mg}} + m_{\text{O}_2} = m_{\text{MgO}} \Rightarrow m_{\text{O}_2} = 4{,}0 - 2{,}4 = 1{,}6\text{ g}$.",
            ),
            mcq(
                question=r"Đốt cháy hoàn toàn $6{,}5\text{ g}$ zinc ($\text{Zn}$, $M = 65\text{ g/mol}$) trong bình chứa khí oxygen ($\text{O}_2$) dư theo phản ứng $2\text{Zn} + \text{O}_2 \xrightarrow{t^\circ} 2\text{ZnO}$. Khối lượng $\text{ZnO}$ ($M = 81\text{ g/mol}$) thu được là:",
                options=[r"$4{,}05\text{ g}$", r"$8{,}10\text{ g}$", r"$12{,}15\text{ g}$", r"$16{,}20\text{ g}$"],
                answer="B",
                level="hieu",
                solution=r"Ta có $n_{\text{Zn}} = \dfrac{6{,}5}{65} = 0{,}1\text{ mol}$. Theo phương trình hóa học, $n_{\text{ZnO}} = n_{\text{Zn}} = 0{,}1\text{ mol}$, suy ra $m_{\text{ZnO}} = 0{,}1 \cdot 81 = 8{,}10\text{ g}$.",
            ),
            tf4(
                stem=r"Cho $0{,}3\text{ mol}$ khí hydrogen ($\text{H}_2$) tác dụng với $0{,}2\text{ mol}$ khí oxygen ($\text{O}_2$) trong bình kín có tia lửa điện theo phản ứng $2\text{H}_2 + \text{O}_2 \xrightarrow{t^\circ} 2\text{H}_2\text{O}$ (giả sử phản ứng xảy ra hoàn toàn, biết $M_{\text{H}} = 1\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Tỉ lệ số mol phản ứng theo phương trình hóa học là $n_{\text{H}_2} : n_{\text{O}_2} = 2 : 1$.",
                    r"b) Sau khi phản ứng kết thúc, khí $\text{O}_2$ phản ứng hết và khí $\text{H}_2$ còn dư.",
                    r"c) Số mol nước ($\text{H}_2\text{O}$) tạo thành sau phản ứng là $0{,}3\text{ mol}$.",
                    r"d) Khối lượng nước thu được sau phản ứng bằng $7{,}2\text{ g}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì theo hệ số cân bằng phương trình $2\text{H}_2 + \text{O}_2 \xrightarrow{t^\circ} 2\text{H}_2\text{O}$, tỉ lệ $n_{\text{H}_2} : n_{\text{O}_2} = 2 : 1$. "
                    r"b) Sai vì lập tỉ số $\dfrac{n_{\text{H}_2}}{2} = \dfrac{0{,}3}{2} = 0{,}15 < \dfrac{n_{\text{O}_2}}{1} = 0{,}2$, nên $\text{H}_2$ phản ứng hết và $\text{O}_2$ còn dư $0{,}2 - 0{,}15 = 0{,}05\text{ mol}$. "
                    r"c) Đúng vì tính theo chất hết $\text{H}_2$, ta có $n_{\text{H}_2\text{O}} = n_{\text{H}_2} = 0{,}3\text{ mol}$. "
                    r"d) Sai vì $m_{\text{H}_2\text{O}} = 0{,}3 \cdot 18 = 5{,}4\text{ g}$."
                ),
            ),
            tf4(
                stem=r"Trong công nghiệp, ammonia ($\text{NH}_3$) được tổng hợp theo phương trình $\text{N}_2 + 3\text{H}_2 \xrightleftharpoons{t^\circ, p, xt} 2\text{NH}_3$. Khi cho $1\text{ mol}$ $\text{N}_2$ tác dụng với $3\text{ mol}$ $\text{H}_2$, thực tế thu được $1{,}5\text{ mol}$ $\text{NH}_3$ (biết ở đkc $25^\circ\text{C}$, $1\text{ bar}$, $1\text{ mol}$ khí chiếm $24{,}79\text{ L}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Nếu hiệu suất phản ứng đạt $100\text{\%}$ thì số mol $\text{NH}_3$ thu được theo lý thuyết là $2\text{ mol}$.",
                    r"b) Số mol khí $\text{N}_2$ đã thực tế tham gia phản ứng là $1{,}5\text{ mol}$.",
                    r"c) Hiệu suất của phản ứng tổng hợp $\text{NH}_3$ trên bằng $75\text{\%}$.",
                    r"d) Thể tích khí $\text{NH}_3$ thực tế thu được ở điều kiện chuẩn là $49{,}58\text{ L}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\dfrac{1}{1} = \dfrac{3}{3} = 1$, nên số mol $\text{NH}_3$ lý thuyết là $2 \cdot 1 = 2\text{ mol}$. "
                    r"b) Sai vì thực tế thu được $1{,}5\text{ mol}$ $\text{NH}_3$ nên số mol $\text{N}_2$ thực tế đã phản ứng là $\dfrac{1{,}5}{2} = 0{,}75\text{ mol}$. "
                    r"c) Đúng vì hiệu suất $H = \dfrac{n_{\text{thực tế}}}{n_{\text{lý thuyết}}} \cdot 100\text{\%} = \dfrac{1{,}5}{2} \cdot 100\text{\%} = 75\text{\%}$. "
                    r"d) Sai vì thể tích $\text{NH}_3$ thực tế ở đkc là $V = 1{,}5 \cdot 24{,}79 = 37{,}185\text{ L}$."
                ),
            ),
            mcq(
                question=r"Nung $50\text{ g}$ calcium carbonate ($\text{CaCO}_3$, $M = 100\text{ g/mol}$) với hiệu suất phản ứng đạt $80\text{\%}$ theo phương trình $\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$. Thể tích khí $\text{CO}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là:",
                options=[
                    r"$8{,}960\text{ L}$",
                    r"$9{,}916\text{ L}$",
                    r"$12{,}395\text{ L}$",
                    r"$15{,}494\text{ L}$",
                ],
                answer="B",
                level="vandung",
                solution=r"Ta có $n_{\text{CaCO}_3} = \dfrac{50}{100} = 0{,}5\text{ mol}$. Theo phương trình, $n_{\text{CO}_2\text{ (lý thuyết)}} = 0{,}5\text{ mol}$. Do hiệu suất $H = 80\text{\%}$ nên $n_{\text{CO}_2\text{ (thực tế)}} = 0{,}5 \cdot 80\text{\%} = 0{,}4\text{ mol}$. Thể tích khí $\text{CO}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}4 = 9{,}916\text{ L}$.",
            ),
            short(
                question=r"Khử hoàn toàn $16\text{ g}$ copper(II) oxide ($\text{CuO}$, $M = 80\text{ g/mol}$) bằng khí hydrogen ($\text{H}_2$) dư ở nhiệt độ cao theo phản ứng $\text{CuO} + \text{H}_2 \xrightarrow{t^\circ} \text{Cu} + \text{H}_2\text{O}$, thực tế thu được $10{,}88\text{ g}$ kim loại copper ($\text{Cu}$, $M = 64\text{ g/mol}$). Tính hiệu suất của phản ứng (theo đơn vị $\text{\%}$).",
                answer=["85", "85%", "85,0", "85.0"],
                level="vandung",
                solution=r"Số mol $\text{CuO}$ ban đầu là $n_{\text{CuO}} = \dfrac{16}{80} = 0{,}2\text{ mol}$. Theo phương trình hóa học, khối lượng $\text{Cu}$ thu được theo lý thuyết là $m_{\text{Cu (lý thuyết)}} = 0{,}2 \cdot 64 = 12{,}8\text{ g}$. Hiệu suất phản ứng là $H = \dfrac{10{,}88}{12{,}8} \cdot 100\text{\%} = 85\text{\%}$.",
            ),
        ],
        description="Định luật bảo toàn khối lượng, các bước lập phương trình hóa học, tính theo phương trình hóa học và hiệu suất phản ứng theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=4,
        code="H8-C04",
        title="Chương 4: Độ tan, nồng độ phần trăm và nồng độ mol của dung dịch",
        topic="dung-dich-nong-do",
        summary=(
            r"Nắm vững khái niệm dung môi, chất tan, dung dịch bão hòa, độ tan $S = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100$, "
            r"nồng độ phần trăm $C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\text{\%}$, nồng độ mol $C_{\text{M}} = \dfrac{n}{V_{\text{dd}}}$, "
            r"công thức liên hệ $C_{\text{M}} = \dfrac{10 \cdot D \cdot C\text{\%}}{M}$ và cách tính toán pha chế dung dịch."
        ),
        objectives=[
            r"Phân biệt được dung môi, chất tan, dung dịch chưa bão hòa và dung dịch bão hòa; tính được độ tan của một chất trong nước theo công thức $S = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100$.",
            r"Tính được nồng độ phần trăm ($C\text{\%}$) và nồng độ mol ($C_{\text{M}}$) của dung dịch theo công thức.",
            r"Vận dụng được công thức liên hệ $C_{\text{M}} = \dfrac{10 \cdot D \cdot C\text{\%}}{M}$ và bảo toàn lượng chất tan khi pha loãng hoặc trộn dung dịch.",
            r"Trình bày được các bước tính toán và thực hành pha chế một dung dịch theo nồng độ cho trước.",
        ],
        formulas=[
            {
                "name": "Độ tan của một chất trong nước (ở nhiệt độ xác định)",
                "formula": r"$S = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100 \quad (\text{g/100 g }\text{H}_2\text{O})$",
                "note": r"$m_{\text{ct}}$: khối lượng chất tan tối đa ($\text{g}$) tạo dung dịch bão hòa trong $m_{\text{H}_2\text{O}}\text{ (g)}$ nước",
            },
            {
                "name": "Nồng độ phần trăm của dung dịch",
                "formula": r"$C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\text{\%}; \quad m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}} = V_{\text{dd (mL)}} \cdot D$",
                "note": r"$m_{\text{ct}}$: khối lượng chất tan ($\text{g}$); $m_{\text{dd}}$: khối lượng dung dịch ($\text{g}$)",
            },
            {
                "name": "Nồng độ mol của dung dịch",
                "formula": r"$C_{\text{M}} = \dfrac{n}{V_{\text{dd}}} \Rightarrow n = C_{\text{M}} \cdot V_{\text{dd}}$",
                "note": r"$n$: số mol chất tan ($\text{mol}$); $V_{\text{dd}}$: thể tích dung dịch ($\text{L}$); đơn vị của $C_{\text{M}}$ là $\text{mol/L}$ hay $\text{M}$",
            },
            {
                "name": r"Hệ thức liên hệ giữa $C_{\text{M}}$ và $C\text{\%}$",
                "formula": r"$C_{\text{M}} = \dfrac{10 \cdot D \cdot C\text{\%}}{M}$",
                "note": r"$D$: khối lượng riêng của dung dịch ($\text{g/mL}$); $M$: khối lượng mol chất tan ($\text{g/mol}$)",
            },
        ],
        theory_sections=[
            {
                "title": "1. Dung dịch và độ tan của một chất trong nước",
                "content": (
                    r"Dung dịch là hỗn hợp đồng nhất của chất tan và dung môi. Ở một nhiệt độ xác định, dung dịch chưa bão hòa là dung dịch "
                    r"có thể hòa tan thêm chất tan, còn dung dịch bão hòa là dung dịch không thể hòa tan thêm chất tan đó nữa. "
                    r"Độ tan ($S$) của một chất trong nước là số gam chất đó hòa tan trong $100\text{ g}$ nước để tạo thành dung dịch bão hòa ở một nhiệt độ "
                    r"xác định. Phần lớn các chất rắn có độ tan tăng khi nhiệt độ tăng; ngược lại, các chất khí có độ tan giảm khi nhiệt độ tăng và áp suất giảm."
                ),
            },
            {
                "title": "2. Nồng độ phần trăm và nồng độ mol",
                "content": (
                    r"Nồng độ phần trăm ($C\text{\%}$) cho biết số gam chất tan có trong $100\text{ g}$ dung dịch: $C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\text{\%}$. "
                    r"Trong dung dịch bão hòa có độ tan $S$, nồng độ phần trăm được tính bằng $C\text{\%}_{\text{bh}} = \dfrac{S}{100 + S} \cdot 100\text{\%}$. "
                    r"Nồng độ mol ($C_{\text{M}}$) cho biết số mol chất tan có trong $1\text{ L}$ ($1000\text{ mL}$) dung dịch: $C_{\text{M}} = \dfrac{n}{V_{\text{dd}}}$ "
                    r"(lưu ý phải đổi thể tích dung dịch sang đơn vị $\text{L}$ trước khi tính)."
                ),
            },
            {
                "title": "3. Pha chế và pha loãng dung dịch",
                "content": (
                    r"Khi pha chế dung dịch từ chất rắn tinh khiết và nước: Bước 1: Tính lượng chất tan ($m_{\text{ct}}$ hoặc $n$) và lượng nước cần dùng. "
                    r"Bước 2: Cân chính xác khối lượng chất tan cho vào cốc thủy tinh, đong nước (hoặc thêm nước đến vạch định mức thể tích $V_{\text{dd}}$) và khuấy đều. "
                    r"Khi pha loãng dung dịch bằng nước, lượng chất tan trước và sau khi pha loãng không đổi: $m_{\text{ct (1)}} = m_{\text{ct (2)}}$ và "
                    r"$n_1 = n_2 \Leftrightarrow C_{\text{M1}} \cdot V_1 = C_{\text{M2}} \cdot V_2$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Ở $25^\circ\text{C}$, hòa tan tối đa $72\text{ g}$ muối ăn ($\text{NaCl}$) vào $200\text{ g}$ nước thì thu được dung dịch bão hòa. "
                    r"Hãy tính độ tan $S$ của $\text{NaCl}$ ở $25^\circ\text{C}$ và nồng độ phần trăm của dung dịch bão hòa này."
                ),
                "solution": (
                    r"Độ tan của $\text{NaCl}$ ở $25^\circ\text{C}$ là $S = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100 = \dfrac{72}{200} \cdot 100 = 36\text{ g/100 g }\text{H}_2\text{O}$. "
                    r"Khối lượng dung dịch bão hòa là $m_{\text{dd}} = 72 + 200 = 272\text{ g}$. Nồng độ phần trăm của dung dịch bão hòa là "
                    r"$C\text{\%} = \dfrac{72}{272} \cdot 100\text{\%} \approx 26{,}47\text{\%}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Hòa tan $16\text{ g}$ sodium hydroxide ($\text{NaOH}$, $M = 40\text{ g/mol}$) vào nước để thu được $250\text{ mL}$ dung dịch. "
                    r"Tính nồng độ mol ($C_{\text{M}}$) của dung dịch $\text{NaOH}$ thu được."
                ),
                "solution": (
                    r"Số mol $\text{NaOH}$ là $n = \dfrac{16}{40} = 0{,}4\text{ mol}$. Đổi thể tích dung dịch $V_{\text{dd}} = 250\text{ mL} = 0{,}25\text{ L}$. "
                    r"Nồng độ mol của dung dịch là $C_{\text{M}} = \dfrac{n}{V_{\text{dd}}} = \dfrac{0{,}4}{0{,}25} = 1{,}6\text{ M}$."
                ),
            },
        ],
        key_takeaways=[
            r"Độ tan $S$ tính trên $100\text{ g}$ nước ($S = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100$), còn nồng độ phần trăm $C\text{\%}$ tính trên $100\text{ g}$ dung dịch ($m_{\text{dd}} = m_{\text{ct}} + m_{\text{H}_2\text{O}}$).",
            r"Khi tính nồng độ mol $C_{\text{M}} = \dfrac{n}{V_{\text{dd}}}$, thể tích dung dịch $V_{\text{dd}}$ bắt buộc phải tính theo đơn vị lít ($\text{L}$).",
            r"Khi pha loãng dung dịch bằng nước, số mol và khối lượng chất tan luôn bảo toàn ($C_{\text{M1}} \cdot V_1 = C_{\text{M2}} \cdot V_2$).",
        ],
        questions=[
            mcq(
                question=r"Công thức tính nồng độ phần trăm ($C\text{\%}$) của một dung dịch là:",
                options=[
                    r"$C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{H}_2\text{O}}} \cdot 100\text{\%}$",
                    r"$C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\text{\%}$",
                    r"$C\text{\%} = \dfrac{m_{\text{dd}}}{m_{\text{ct}}} \cdot 100\text{\%}$",
                    r"$C\text{\%} = \dfrac{n}{V_{\text{dd}}} \cdot 100\text{\%}$",
                ],
                answer="B",
                level="biet",
                solution=r"Nồng độ phần trăm được tính bằng tỉ số khối lượng chất tan trên khối lượng dung dịch nhân với $100\text{\%}$: $C\text{\%} = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\text{\%}$.",
            ),
            mcq(
                question=r"Đơn vị thường dùng của nồng độ mol ($C_{\text{M}}$) là:",
                options=[r"$\text{g/L}$", r"$\text{mol/L}$ (hoặc $\text{M}$)", r"$\text{g/mL}$", r"$\text{\%}$"],
                answer="B",
                level="biet",
                solution=r"Nồng độ mol $C_{\text{M}} = \dfrac{n}{V_{\text{dd}}}$ có đơn vị là $\text{mol/L}$, thường kí hiệu là $\text{M}$.",
            ),
            mcq(
                question=r"Khi hòa tan đường saccharose vào cốc nước lọc, chất đóng vai trò là dung môi là:",
                options=[
                    r"Đường saccharose",
                    r"Nước",
                    r"Nước đường thu được",
                    r"Cả đường và nước",
                ],
                answer="B",
                level="biet",
                solution=r"Trong dung dịch nước đường, nước là dung môi (chất có lượng lớn hơn và làm môi trường hòa tan), còn đường là chất tan.",
            ),
            mcq(
                question=r"Trong $500\text{ mL}$ dung dịch $\text{HCl}$ $2\text{ M}$ có chứa số mol $\text{HCl}$ là:",
                options=[r"$0{,}25\text{ mol}$", r"$0{,}50\text{ mol}$", r"$1{,}00\text{ mol}$", r"$2{,}50\text{ mol}$"],
                answer="C",
                level="biet",
                solution=r"Đổi $V_{\text{dd}} = 500\text{ mL} = 0{,}5\text{ L}$. Số mol $\text{HCl}$ là $n = C_{\text{M}} \cdot V_{\text{dd}} = 2 \cdot 0{,}5 = 1{,}00\text{ mol}$.",
            ),
            mcq(
                question=r"Hòa tan $20\text{ g}$ muối $\text{KNO}_3$ vào $180\text{ g}$ nước thì thu được dung dịch có nồng độ phần trăm ($C\text{\%}$) bằng:",
                options=[r"$10{,}0\text{\%}$", r"$11{,}1\text{\%}$", r"$12{,}5\text{\%}$", r"$20{,}0\text{\%}$"],
                answer="A",
                level="hieu",
                solution=r"Khối lượng dung dịch là $m_{\text{dd}} = m_{\text{ct}} + m_{\text{H}_2\text{O}} = 20 + 180 = 200\text{ g}$. Nồng độ phần trăm là $C\text{\%} = \dfrac{20}{200} \cdot 100\text{\%} = 10{,}0\text{\%}$.",
            ),
            mcq(
                question=r"Để pha chế $300\text{ g}$ dung dịch $\text{CuSO}_4$ $15\text{\%}$, khối lượng $\text{CuSO}_4$ khan và khối lượng nước cần lấy lần lượt là:",
                options=[
                    r"$15\text{ g}$ $\text{CuSO}_4$ và $285\text{ g}$ nước",
                    r"$45\text{ g}$ $\text{CuSO}_4$ và $255\text{ g}$ nước",
                    r"$45\text{ g}$ $\text{CuSO}_4$ và $300\text{ g}$ nước",
                    r"$30\text{ g}$ $\text{CuSO}_4$ và $270\text{ g}$ nước",
                ],
                answer="B",
                level="hieu",
                solution=r"Khối lượng chất tan cần lấy là $m_{\text{CuSO}_4} = \dfrac{300 \cdot 15\text{\%}}{100\text{\%}} = 45\text{ g}$. Khối lượng nước cần lấy là $m_{\text{H}_2\text{O}} = 300 - 45 = 255\text{ g}$.",
            ),
            tf4(
                stem=r"Ở $20^\circ\text{C}$, khi hòa tan tối đa $63{,}2\text{ g}$ muối potassium nitrate ($\text{KNO}_3$) vào $200\text{ g}$ nước thì thu được dung dịch bão hòa $\text{X}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Độ tan của muối $\text{KNO}_3$ trong nước ở $20^\circ\text{C}$ là $31{,}6\text{ g/100 g }\text{H}_2\text{O}$.",
                    r"b) Khối lượng của dung dịch bão hòa $\text{X}$ thu được bằng $200\text{ g}$.",
                    r"c) Nồng độ phần trăm của dung dịch bão hòa $\text{X}$ ở $20^\circ\text{C}$ xấp xỉ bằng $24{,}01\text{\%}$.",
                    r"d) Nếu giữ nguyên nhiệt độ ở $20^\circ\text{C}$ và cho thêm $10\text{ g}$ $\text{KNO}_3$ vào dung dịch $\text{X}$ thì toàn bộ lượng muối thêm vào vẫn tan hết.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $S = \dfrac{63{,}2}{200} \cdot 100 = 31{,}6\text{ g/100 g }\text{H}_2\text{O}$. "
                    r"b) Sai vì khối lượng dung dịch là $m_{\text{dd}} = 63{,}2 + 200 = 263{,}2\text{ g}$. "
                    r"c) Đúng vì $C\text{\%} = \dfrac{63{,}2}{263{,}2} \cdot 100\text{\%} \approx 24{,}01\text{\%}$. "
                    r"d) Sai vì dung dịch $\text{X}$ đã bão hòa ở $20^\circ\text{C}$ nên không thể hòa tan thêm $\text{KNO}_3$ ở cùng nhiệt độ đó."
                ),
            ),
            tf4(
                stem=r"Một học sinh lấy $200\text{ mL}$ dung dịch $\text{NaOH}$ $2\text{ M}$ (biết $M_{\text{NaOH}} = 40\text{ g/mol}$) rồi thêm nước cất vào và khuấy đều cho đến khi thu được $500\text{ mL}$ dung dịch mới $\text{Y}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Số mol $\text{NaOH}$ có trong $200\text{ mL}$ dung dịch ban đầu là $0{,}4\text{ mol}$.",
                    r"b) Khối lượng chất tan $\text{NaOH}$ có trong dung dịch $\text{Y}$ sau khi pha loãng bằng $8\text{ g}$.",
                    r"c) Nồng độ mol của dung dịch $\text{Y}$ sau khi pha loãng là $0{,}8\text{ M}$.",
                    r"d) Khi pha loãng bằng nước cất, số mol $\text{NaOH}$ trong dung dịch tăng lên gấp $2{,}5$ lần.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $n_{\text{NaOH}} = C_{\text{M}} \cdot V = 2 \cdot 0{,}2 = 0{,}4\text{ mol}$. "
                    r"b) Sai vì lượng chất tan không đổi và bằng $m_{\text{NaOH}} = 0{,}4 \cdot 40 = 16\text{ g}$. "
                    r"c) Đúng vì nồng độ mol mới là $C_{\text{M (Y)}} = \dfrac{0{,}4}{0{,}5} = 0{,}8\text{ M}$. "
                    r"d) Sai vì khi chỉ thêm nước cất, số mol chất tan giữ nguyên là $0{,}4\text{ mol}$."
                ),
            ),
            mcq(
                question=r"Một dung dịch sulfuric acid ($\text{H}_2\text{SO}_4$, $M = 98\text{ g/mol}$) có nồng độ phần trăm $C\text{\%} = 19{,}6\text{\%}$ và khối lượng riêng $D = 1{,}14\text{ g/mL}$. Nồng độ mol ($C_{\text{M}}$) của dung dịch $\text{H}_2\text{SO}_4$ này là:",
                options=[r"$1{,}14\text{ M}$", r"$2{,}00\text{ M}$", r"$2{,}28\text{ M}$", r"$4{,}56\text{ M}$"],
                answer="C",
                level="vandung",
                solution=r"Áp dụng công thức liên hệ $C_{\text{M}} = \dfrac{10 \cdot D \cdot C\text{\%}}{M} = \dfrac{10 \cdot 1{,}14 \cdot 19{,}6}{98} = 2{,}28\text{ M}$.",
            ),
            short(
                question=r"Trộn $200\text{ g}$ dung dịch $\text{NaCl}$ $10\text{\%}$ với $300\text{ g}$ dung dịch $\text{NaCl}$ $25\text{\%}$. Tính nồng độ phần trăm (theo đơn vị $\text{\%}$) của dung dịch $\text{NaCl}$ thu được sau khi trộn.",
                answer=["19", "19%", "19,0", "19.0"],
                level="vandung",
                solution=r"Tổng khối lượng chất tan $\text{NaCl}$ là $m_{\text{ct}} = 200 \cdot 10\text{\%} + 300 \cdot 25\text{\%} = 20 + 75 = 95\text{ g}$. Tổng khối lượng dung dịch sau khi trộn là $m_{\text{dd}} = 200 + 300 = 500\text{ g}$. Nồng độ phần trăm của dung dịch mới là $C\text{\%} = \dfrac{95}{500} \cdot 100\text{\%} = 19\text{\%}$.",
            ),
        ],
        description="Khái niệm dung dịch, độ tan, nồng độ phần trăm, nồng độ mol và phương pháp pha chế dung dịch theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=5,
        code="H8-C05",
        title="Chương 5: Acid, Base, thang pH và Muối",
        topic="axit-bazo-muoi",
        summary=(
            r"Nắm vững khái niệm, phân loại, danh pháp IUPAC và tính chất hóa học của acid ($\text{HCl}, \text{H}_2\text{SO}_4$), "
            r"base ($\text{NaOH}, \text{Ca(OH)}_2$), thang $\text{pH}$ từ $1$ đến $14$, cùng tính chất hóa học và điều kiện phản ứng trao đổi của muối."
        ),
        objectives=[
            r"Nêu được khái niệm acid (tạo ra ion $\text{H}^+$ trong nước) và base (tạo ra ion $\text{OH}^-$ trong nước); trình bày được tính chất hóa học của $\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$ và $\text{NaOH}, \text{Ca(OH)}_2$.",
            r"Sử dụng được thang $\text{pH}$ để đánh giá độ acid - base của dung dịch ($\text{pH} < 7$: môi trường acid, $\text{pH} = 7$: trung tính, $\text{pH} > 7$: môi trường base) và liên hệ với đất trồng, dịch vị dạ dày.",
            r"Nêu được khái niệm, cách gọi tên IUPAC của muối và tính tan của một số muối phổ biến.",
            r"Trình bày được tính chất hóa học của muối và điều kiện xảy ra phản ứng trao đổi trong dung dịch (tạo kết tủa, chất khí hoặc nước).",
        ],
        formulas=[
            {
                "name": "Sự phân li của acid và base trong nước",
                "formula": r"$\text{H}_n\text{A} \longrightarrow n\text{H}^+ + \text{A}^{n-}; \quad \text{M(OH)}_m \longrightarrow \text{M}^{m+} + m\text{OH}^-$",
                "note": r"Acid tạo ra ion $\text{H}^+$; base tan (kiềm) tạo ra ion $\text{OH}^-$",
            },
            {
                "name": "Phản ứng trung hòa giữa acid và base",
                "formula": r"$\text{Acid} + \text{Base} \longrightarrow \text{Muối} + \text{H}_2\text{O} \quad (\text{bản chất: }\text{H}^+ + \text{OH}^- \longrightarrow \text{H}_2\text{O})$",
                "note": r"Ví dụ: $\text{HCl} + \text{NaOH} \longrightarrow \text{NaCl} + \text{H}_2\text{O}$",
            },
            {
                "name": "Thang đo độ pH của dung dịch",
                "formula": r"$\text{pH} < 7\text{ (môi trường acid)}; \quad \text{pH} = 7\text{ (trung tính)}; \quad \text{pH} > 7\text{ (môi trường base)}$",
                "note": r"$\text{pH}$ càng nhỏ thì độ acid càng mạnh; $\text{pH}$ càng lớn thì độ base càng mạnh",
            },
            {
                "name": "Điều kiện phản ứng trao đổi của muối trong dung dịch",
                "formula": r"$\text{AB} + \text{CD} \longrightarrow \text{AD}\downarrow + \text{CB} \quad \text{hoặc tạo chất khí }\uparrow \text{ / }\text{H}_2\text{O}$",
                "note": r"Các kết tủa quan trọng: $\text{AgCl}\downarrow, \text{BaSO}_4\downarrow, \text{CaCO}_3\downarrow, \text{Cu(OH)}_2\downarrow, \text{Fe(OH)}_3\downarrow$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Acid và tính chất hóa học của acid",
                "content": (
                    r"Acid là những hợp chất trong phân tử có nguyên tử hydrogen ($\text{H}$) liên kết với gốc acid, khi tan trong nước tạo ra ion $\text{H}^+$ "
                    r"(ví dụ: hydrochloric acid $\text{HCl}$, sulfuric acid $\text{H}_2\text{SO}_4$, nitric acid $\text{HNO}_3$, acetic acid $\text{CH}_3\text{COOH}$). "
                    r"Dung dịch acid làm quỳ tím chuyển sang màu đỏ (không làm đổi màu phenolphthalein), tác dụng với kim loại đứng trước $\text{H}$ "
                    r"($\text{Mg}, \text{Al}, \text{Zn}, \text{Fe}$...) tạo muối và giải phóng khí $\text{H}_2$, tác dụng với base và oxide base tạo muối và nước, "
                    r"tác dụng với nhiều muối (như $\text{CaCO}_3$) giải phóng khí $\text{CO}_2$."
                ),
            },
            {
                "title": "2. Base và thang pH",
                "content": (
                    r"Base là những hợp chất trong phân tử có nguyên tử kim loại liên kết với một hay nhiều nhóm hydroxide ($-\text{OH}$), khi tan trong nước "
                    r"tạo ra ion $\text{OH}^-$. Base được chia thành base kiềm (tan trong nước như $\text{NaOH}, \text{KOH}, \text{Ca(OH)}_2, \text{Ba(OH)}_2$) "
                    r"và base không tan (như $\text{Cu(OH)}_2$ màu xanh lam, $\text{Fe(OH)}_3$ màu nâu đỏ, $\text{Mg(OH)}_2$ màu trắng). Dung dịch kiềm làm quỳ tím "
                    r"hóa xanh và làm dung dịch phenolphthalein không màu chuyển sang màu hồng; tác dụng với acid, oxide acid và dung dịch muối. "
                    r"Thang $\text{pH}$ thường có giá trị từ $1$ đến $14$: môi trường acid có $\text{pH} < 7$, trung tính có $\text{pH} = 7$, môi trường kiềm có $\text{pH} > 7$."
                ),
            },
            {
                "title": "3. Muối và phản ứng trao đổi trong dung dịch",
                "content": (
                    r"Muối là hợp chất được hình thành khi thay thế ion $\text{H}^+$ của acid bằng ion kim loại hoặc ion ammonium ($\text{NH}_4^+$). "
                    r"Tên gọi IUPAC của muối: Tên kim loại (kèm hóa trị nếu kim loại có nhiều hóa trị) + tên gốc acid ($\text{-Cl}$: chloride, "
                    r"$\text{=SO}_4$: sulfate, $\text{-NO}_3$: nitrate, $\text{=CO}_3$: carbonate, $\equiv\text{PO}_4$: phosphate). "
                    r"Dung dịch muối có thể tác dụng với kim loại, acid, dung dịch base hoặc dung dịch muối khác. Phản ứng trao đổi trong dung dịch "
                    r"chỉ xảy ra khi sản phẩm tạo thành có chất kết tủa ($\downarrow$), chất khí ($\uparrow$) hoặc nước ($\text{H}_2\text{O}$)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Cho $100\text{ mL}$ dung dịch $\text{BaCl}_2$ $0{,}2\text{ M}$ tác dụng hoàn toàn với dung dịch $\text{Na}_2\text{SO}_4$ dư. "
                    r"Viết phương trình hóa học, nêu hiện tượng và tính khối lượng kết tủa thu được (biết $M_{\text{Ba}} = 137\text{ g/mol}$, "
                    r"$M_{\text{S}} = 32\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$)."
                ),
                "solution": (
                    r"Phương trình hóa học: $\text{BaCl}_2 + \text{Na}_2\text{SO}_4 \longrightarrow \text{BaSO}_4\downarrow + 2\text{NaCl}$. "
                    r"Hiện tượng: xuất hiện kết tủa trắng barium sulfate ($\text{BaSO}_4$) không tan trong nước và các acid. "
                    r"Ta có $n_{\text{BaCl}_2} = 0{,}1 \cdot 0{,}2 = 0{,}02\text{ mol}$, suy ra $n_{\text{BaSO}_4} = 0{,}02\text{ mol}$. "
                    r"Khối lượng kết tủa thu được là $m_{\text{BaSO}_4} = 0{,}02 \cdot (137 + 32 + 64) = 0{,}02 \cdot 233 = 4{,}66\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Để trung hòa hết $200\text{ mL}$ dung dịch $\text{H}_2\text{SO}_4$ $0{,}5\text{ M}$ cần dùng vừa đủ $V\text{ (mL)}$ dung dịch "
                    r"$\text{NaOH}$ $1\text{ M}$. Hãy tính giá trị của $V$."
                ),
                "solution": (
                    r"Số mol $\text{H}_2\text{SO}_4$ là $n_{\text{H}_2\text{SO}_4} = 0{,}2 \cdot 0{,}5 = 0{,}1\text{ mol}$. Phương trình phản ứng trung hòa: "
                    r"$2\text{NaOH} + \text{H}_2\text{SO}_4 \longrightarrow \text{Na}_2\text{SO}_4 + 2\text{H}_2\text{O}$. Theo phương trình, "
                    r"$n_{\text{NaOH}} = 2 \cdot n_{\text{H}_2\text{SO}_4} = 0{,}2\text{ mol}$. Thể tích dung dịch $\text{NaOH}$ cần dùng là "
                    r"$V_{\text{dd NaOH}} = \dfrac{0{,}2}{1} = 0{,}2\text{ L} = 200\text{ mL}$."
                ),
            },
        ],
        key_takeaways=[
            r"Acid phân li ra ion $\text{H}^+$ làm quỳ tím hóa đỏ ($\text{pH} < 7$); dung dịch base (kiềm) phân li ra ion $\text{OH}^-$ làm quỳ tím hóa xanh và phenolphthalein hóa hồng ($\text{pH} > 7$).",
            r"Kim loại hoạt động đứng trước $\text{H}$ ($\text{Mg}, \text{Al}, \text{Zn}, \text{Fe}$) tác dụng với dung dịch $\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$ giải phóng khí $\text{H}_2$, còn $\text{Cu}, \text{Ag}$ không phản ứng.",
            r"Phản ứng trao đổi giữa các dung dịch muối, acid, base chỉ xảy ra khi có tạo thành chất kết tủa ($\downarrow$), chất khí ($\uparrow$) hoặc nước ($\text{H}_2\text{O}$).",
        ],
        questions=[
            mcq(
                question=r"Khi hòa tan vào nước, các hợp chất acid đều phân li tạo ra cation nào sau đây?",
                options=[r"$\text{OH}^-$", r"$\text{H}^+$", r"$\text{Na}^+$", r"$\text{Cl}^-$"],
                answer="B",
                level="biet",
                solution=r"Theo định nghĩa, acid là hợp chất khi tan trong nước tạo ra ion $\text{H}^+$.",
            ),
            mcq(
                question=r"Nhỏ vài giọt dung dịch phenolphthalein không màu vào ống nghiệm đựng dung dịch sodium hydroxide ($\text{NaOH}$) thì dung dịch chuyển sang màu:",
                options=[r"Đỏ", r"Xanh lam", r"Hồng", r"Vàng"],
                answer="C",
                level="biet",
                solution=r"Dung dịch kiềm ($\text{NaOH}$) có môi trường base nên làm phenolphthalein không màu chuyển sang màu hồng.",
            ),
            mcq(
                question=r"Một mẫu đất trồng bị chua do nhiễm phèn có giá trị $\text{pH}$ thuộc khoảng nào sau đây?",
                options=[r"$\text{pH} < 7$", r"$\text{pH} = 7$", r"$\text{pH} > 7$", r"$\text{pH} = 14$"],
                answer="A",
                level="biet",
                solution=r"Đất chua có môi trường acid nên có giá trị $\text{pH} < 7$. Người ta thường bón vôi bột ($\text{CaO}$ hoặc $\text{Ca(OH)}_2$) để khử chua.",
            ),
            mcq(
                question=r"Theo danh pháp IUPAC, muối có công thức hóa học $\text{CuSO}_4$ được gọi tên là:",
                options=[
                    r"Copper sulfate",
                    r"Copper(I) sulfate",
                    r"Copper(II) sulfate",
                    r"Copper(II) sulfite",
                ],
                answer="C",
                level="biet",
                solution=r"Nguyên tố $\text{Cu}$ trong $\text{CuSO}_4$ có hóa trị $\text{II}$ và gốc $=\text{SO}_4$ là sulfate, nên tên gọi chuẩn IUPAC là copper(II) sulfate.",
            ),
            mcq(
                question=r"Kim loại nào sau đây không tác dụng với dung dịch sulfuric acid loãng ($\text{H}_2\text{SO}_4\text{ loãng}$)?",
                options=[r"$\text{Zn}$", r"$\text{Fe}$", r"$\text{Mg}$", r"$\text{Cu}$"],
                answer="D",
                level="hieu",
                solution=r"Kim loại $\text{Cu}$ đứng sau $\text{H}$ trong dãy hoạt động hóa học nên không phản ứng với dung dịch $\text{HCl}$ và $\text{H}_2\text{SO}_4\text{ loãng}$.",
            ),
            mcq(
                question=r"Cặp chất nào sau đây xảy ra phản ứng trao đổi khi trộn lẫn hai dung dịch với nhau?",
                options=[
                    r"$\text{NaCl}$ và $\text{KNO}_3$",
                    r"$\text{BaCl}_2$ và $\text{H}_2\text{SO}_4$",
                    r"$\text{CuSO}_4$ và $\text{HCl}$",
                    r"$\text{Na}_2\text{SO}_4$ và $\text{KOH}$",
                ],
                answer="B",
                level="hieu",
                solution=r"Dung dịch $\text{BaCl}_2$ tác dụng với dung dịch $\text{H}_2\text{SO}_4$ tạo kết tủa trắng $\text{BaSO}_4\downarrow$: $\text{BaCl}_2 + \text{H}_2\text{SO}_4 \longrightarrow \text{BaSO}_4\downarrow + 2\text{HCl}$.",
            ),
            tf4(
                stem=r"Cho bốn dung dịch không màu đựng trong bốn ống nghiệm riêng biệt: dung dịch $\text{HCl}$ ($\text{pH} = 1$), nước cất ($\text{pH} = 7$), dung dịch $\text{NaCl}$ ($\text{pH} = 7$) và dung dịch $\text{NaOH}$ ($\text{pH} = 13$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Dung dịch $\text{HCl}$ làm giấy quỳ tím chuyển sang màu đỏ.",
                    r"b) Cả nước cất và dung dịch $\text{NaCl}$ đều làm dung dịch phenolphthalein chuyển sang màu hồng.",
                    r"c) Dung dịch $\text{NaOH}$ có môi trường kiềm và làm giấy quỳ tím chuyển sang màu xanh.",
                    r"d) Khi trộn lẫn $10\text{ mL}$ dung dịch $\text{HCl}$ $0{,}1\text{ M}$ với $10\text{ mL}$ dung dịch $\text{NaOH}$ $0{,}1\text{ M}$ thì dung dịch thu được có $\text{pH} < 7$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì dung dịch $\text{HCl}$ là môi trường acid ($\text{pH} = 1 < 7$) làm quỳ tím hóa đỏ. "
                    r"b) Sai vì nước cất và dung dịch $\text{NaCl}$ có môi trường trung tính ($\text{pH} = 7$), không làm đổi màu phenolphthalein. "
                    r"c) Đúng vì dung dịch $\text{NaOH}$ là kiềm mạnh ($\text{pH} = 13 > 7$) làm quỳ tím hóa xanh. "
                    r"d) Sai vì $n_{\text{HCl}} = n_{\text{NaOH}} = 0{,}001\text{ mol}$, phản ứng trung hòa vừa đủ tạo dung dịch $\text{NaCl}$ trung tính có $\text{pH} = 7$."
                ),
            ),
            tf4(
                stem=r"Thực hiện các thí nghiệm hóa học với dung dịch muối trong phòng thí nghiệm. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Nhỏ dung dịch $\text{NaOH}$ vào ống nghiệm chứa dung dịch $\text{CuSO}_4$ thấy xuất hiện kết tủa màu xanh lam $\text{Cu(OH)}_2$.",
                    r"b) Nhỏ dung dịch $\text{AgNO}_3$ vào dung dịch $\text{NaCl}$ không thấy xảy ra hiện tượng gì.",
                    r"c) Nhỏ dung dịch $\text{HCl}$ vào ống nghiệm đựng đá vôi ($\text{CaCO}_3$) thấy sủi bọt khí không màu $\text{CO}_2$.",
                    r"d) Muối $\text{BaSO}_4$ và muối $\text{CaCO}_3$ đều tan rất tốt trong nước ở điều kiện chuẩn.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{CuSO}_4 + 2\text{NaOH} \longrightarrow \text{Cu(OH)}_2\downarrow\text{ (xanh lam)} + \text{Na}_2\text{SO}_4$. "
                    r"b) Sai vì $\text{AgNO}_3 + \text{NaCl} \longrightarrow \text{AgCl}\downarrow\text{ (trắng)} + \text{NaNO}_3$, xuất hiện kết tủa trắng. "
                    r"c) Đúng vì $\text{CaCO}_3 + 2\text{HCl} \longrightarrow \text{CaCl}_2 + \text{CO}_2\uparrow + \text{H}_2\text{O}$. "
                    r"d) Sai vì cả $\text{BaSO}_4$ và $\text{CaCO}_3$ đều là các muối không tan (kết tủa trắng) trong nước."
                ),
            ),
            mcq(
                question=r"Cho $10\text{ g}$ calcium carbonate ($\text{CaCO}_3$, $M = 100\text{ g/mol}$) tác dụng hết với dung dịch hydrochloric acid ($\text{HCl}$) dư theo phương trình $\text{CaCO}_3 + 2\text{HCl} \longrightarrow \text{CaCl}_2 + \text{CO}_2\uparrow + \text{H}_2\text{O}$. Thể tích khí $\text{CO}_2$ thoát ra ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là:",
                options=[r"$1{,}2395\text{ L}$", r"$2{,}240\text{ L}$", r"$2{,}479\text{ L}$", r"$4{,}958\text{ L}$"],
                answer="C",
                level="vandung",
                solution=r"Số mol $\text{CaCO}_3$ là $n_{\text{CaCO}_3} = \dfrac{10}{100} = 0{,}1\text{ mol}$. Theo phương trình hóa học, $n_{\text{CO}_2} = n_{\text{CaCO}_3} = 0{,}1\text{ mol}$. Thể tích khí $\text{CO}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}1 = 2{,}479\text{ L}$.",
            ),
            short(
                question=r"Cho $200\text{ mL}$ dung dịch $\text{CuSO}_4$ $0{,}5\text{ M}$ tác dụng hoàn toàn với dung dịch $\text{NaOH}$ dư theo phương trình $\text{CuSO}_4 + 2\text{NaOH} \longrightarrow \text{Cu(OH)}_2\downarrow + \text{Na}_2\text{SO}_4$. Tính khối lượng kết tủa $\text{Cu(OH)}_2$ (theo đơn vị $\text{g}$, biết $M_{\text{Cu}} = 64\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$, $M_{\text{H}} = 1\text{ g/mol}$) thu được.",
                answer=["9,8", "9.8"],
                level="vandung",
                solution=r"Số mol $\text{CuSO}_4$ là $n_{\text{CuSO}_4} = 0{,}2 \cdot 0{,}5 = 0{,}1\text{ mol}$. Theo phương trình hóa học, $n_{\text{Cu(OH)}_2} = n_{\text{CuSO}_4} = 0{,}1\text{ mol}$. Khối lượng mol của $\text{Cu(OH)}_2$ là $M = 64 + 2 \cdot 17 = 98\text{ g/mol}$. Vậy khối lượng kết tủa là $m = 0{,}1 \cdot 98 = 9{,}8\text{ g}$.",
            ),
        ],
        description="Khái niệm, danh pháp IUPAC và tính chất hóa học của acid, base, muối và thang pH theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=6,
        code="H8-C06",
        title="Chương 6: Oxide và Phân bón hóa học",
        topic="oxide-phan-bon",
        summary=(
            r"Phân loại 4 nhóm oxide gồm oxide acid ($\text{CO}_2, \text{SO}_2, \text{P}_2\text{O}_5$), oxide base ($\text{CaO}, \text{Fe}_2\text{O}_3, \text{CuO}$), "
            r"oxide lưỡng tính ($\text{Al}_2\text{O}_3, \text{ZnO}$) và oxide trung tính ($\text{CO}, \text{NO}$); nắm vững tính chất hóa học của oxide "
            r"và các loại phân bón hóa học chủ yếu (phân đạm cung cấp $\text{N}$, phân lân cung cấp $\text{P}$, phân kali cung cấp $\text{K}$, phân $\text{NPK}$)."
        ),
        objectives=[
            r"Nêu được khái niệm oxide và phân loại được 4 loại oxide theo tính chất hóa học: oxide acid, oxide base, oxide lưỡng tính và oxide trung tính.",
            r"Viết được phương trình hóa học minh họa tính chất của oxide base (tác dụng với acid) và oxide acid (tác dụng với dung dịch base).",
            r"Phân biệt được vai trò của các nguyên tố dinh dưỡng đa lượng $\text{N}, \text{P}, \text{K}$ trong phân đạm, phân lân, phân kali, phân hỗn hợp $\text{NPK}$ và phân hữu cơ.",
            r"Trình bày được nguyên tắc sử dụng phân bón an toàn, hiệu quả và bảo vệ môi trường đất, nước.",
        ],
        formulas=[
            {
                "name": "Phản ứng của oxide base với dung dịch acid",
                "formula": r"$\text{Oxide base} + \text{Acid} \longrightarrow \text{Muối} + \text{H}_2\text{O}$",
                "note": r"Ví dụ: $\text{CuO} + 2\text{HCl} \longrightarrow \text{CuCl}_2 + \text{H}_2\text{O}$",
            },
            {
                "name": "Phản ứng của oxide acid với dung dịch kiềm",
                "formula": r"$\text{Oxide acid} + \text{Base (kiềm)} \longrightarrow \text{Muối} + \text{H}_2\text{O}$",
                "note": r"Ví dụ: $\text{CO}_2 + \text{Ca(OH)}_2 \longrightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O}$",
            },
            {
                "name": r"Tính chất của oxide lưỡng tính ($\text{Al}_2\text{O}_3, \text{ZnO}$)",
                "formula": r"$\text{Al}_2\text{O}_3 + 6\text{HCl} \longrightarrow 2\text{AlCl}_3 + 3\text{H}_2\text{O}; \quad \text{Al}_2\text{O}_3 + 2\text{NaOH} \longrightarrow 2\text{NaAlO}_2 + \text{H}_2\text{O}$",
                "note": r"Oxide lưỡng tính tác dụng được với cả dung dịch acid mạnh và dung dịch kiềm mạnh",
            },
            {
                "name": "Các thành phần dinh dưỡng chính trong phân bón hóa học",
                "formula": r"$\text{Đạm (N)}: (\text{NH}_2)_2\text{CO}, \text{NH}_4\text{NO}_3; \quad \text{Lân (P)}: \text{Ca(H}_2\text{PO}_4)_2; \quad \text{Kali (K)}: \text{KCl}, \text{K}_2\text{SO}_4$",
                "note": r"Phân $\text{NPK}$ chứa đồng thời cả ba nguyên tố dinh dưỡng $\text{N}, \text{P}, \text{K}$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Khái niệm và phân loại oxide",
                "content": (
                    r"Oxide là hợp chất của hai nguyên tố, trong đó có một nguyên tố là oxygen ($\text{O}$). Dựa vào tính chất hóa học, oxide được chia thành 4 loại: "
                    r"(1) Oxide base là những oxide tác dụng với dung dịch acid tạo thành muối và nước, thường là oxide của kim loại như $\text{CaO}, \text{Na}_2\text{O}, \text{CuO}, \text{Fe}_2\text{O}_3, \text{MgO}$. "
                    r"(2) Oxide acid là những oxide tác dụng với dung dịch base tạo thành muối và nước, thường là oxide của phi kim như $\text{CO}_2, \text{SO}_2, \text{SO}_3, \text{P}_2\text{O}_5, \text{N}_2\text{O}_5$. "
                    r"(3) Oxide lưỡng tính là những oxide tác dụng được với cả dung dịch acid và dung dịch base tạo thành muối và nước như $\text{Al}_2\text{O}_3, \text{ZnO}$. "
                    r"(4) Oxide trung tính (oxide không tạo muối) là những oxide không tác dụng với acid, base hay nước như $\text{CO}, \text{NO}$."
                ),
            },
            {
                "title": "2. Tính chất hóa học của oxide",
                "content": (
                    r"Một số oxide base của kim loại kiềm và kiềm thổ ($\text{Na}_2\text{O}, \text{K}_2\text{O}, \text{CaO}, \text{BaO}$) tác dụng trực tiếp với nước tạo dung dịch kiềm: "
                    r"$\text{CaO} + \text{H}_2\text{O} \longrightarrow \text{Ca(OH)}_2$. Hầu hết oxide base tác dụng với dung dịch acid tạo muối và nước "
                    r"(ví dụ $\text{Fe}_2\text{O}_3 + 6\text{HCl} \longrightarrow 2\text{FeCl}_3 + 3\text{H}_2\text{O}$). "
                    r"Nhiều oxide acid ($\text{CO}_2, \text{SO}_2, \text{SO}_3, \text{P}_2\text{O}_5$) tác dụng với nước tạo dung dịch acid tương ứng "
                    r"($\text{SO}_3 + \text{H}_2\text{O} \longrightarrow \text{H}_2\text{SO}_4$) và tác dụng với dung dịch kiềm tạo muối và nước."
                ),
            },
            {
                "title": "3. Phân bón hóa học và vai trò đối với cây trồng",
                "content": (
                    r"Phân bón hóa học cung cấp các nguyên tố dinh dưỡng thiết yếu cho cây trồng: "
                    r"(1) Phân đạm cung cấp nguyên tố nitrogen ($\text{N}$) dưới dạng ion $\text{NH}_4^+$ hoặc $\text{NO}_3^-$, kích thích cây sinh trưởng mạnh, ra nhiều lá "
                    r"(gồm urea $(\text{NH}_2)_2\text{CO}$, đạm hai lá $\text{NH}_4\text{NO}_3$, đạm một lá $(\text{NH}_4)_2\text{SO}_4$). "
                    r"(2) Phân lân cung cấp nguyên tố phosphorus ($\text{P}$), kích thích sự phát triển của bộ rễ, quá trình đẻ nhánh và nảy chồi "
                    r"(gồm superphosphate $\text{Ca(H}_2\text{PO}_4)_2$, phân lân nung chảy). "
                    r"(3) Phân kali cung cấp nguyên tố potassium ($\text{K}$), giúp cây tổng hợp chất đường, bột, chất xơ và tăng khả năng chống chịu rét, hạn, sâu bệnh ($\text{KCl}, \text{K}_2\text{SO}_4$). "
                    r"(4) Phân hỗn hợp $\text{NPK}$ chứa cả ba nguyên tố $\text{N}, \text{P}, \text{K}$. Khi bón phân cần tuân thủ quy tắc '4 đúng' (đúng loại, đúng liều, đúng lúc, đúng cách)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Hòa tan hoàn toàn $8\text{ g}$ copper(II) oxide ($\text{CuO}$, $M = 80\text{ g/mol}$) vào $200\text{ mL}$ dung dịch hydrochloric acid ($\text{HCl}$) "
                    r"vừa đủ. Tính nồng độ mol của dung dịch $\text{HCl}$ đã dùng và khối lượng muối $\text{CuCl}_2$ ($M = 135\text{ g/mol}$) thu được."
                ),
                "solution": (
                    r"Số mol $\text{CuO}$ là $n_{\text{CuO}} = \dfrac{8}{80} = 0{,}1\text{ mol}$. Phương trình hóa học: "
                    r"$\text{CuO} + 2\text{HCl} \longrightarrow \text{CuCl}_2 + \text{H}_2\text{O}$. Theo phương trình, "
                    r"$n_{\text{HCl}} = 2 \cdot n_{\text{CuO}} = 0{,}2\text{ mol}$ và $n_{\text{CuCl}_2} = 0{,}1\text{ mol}$. "
                    r"Nồng độ mol của dung dịch $\text{HCl}$ là $C_{\text{M}} = \dfrac{0{,}2}{0{,}2} = 1{,}0\text{ M}$. Khối lượng muối $\text{CuCl}_2$ là $m = 0{,}1 \cdot 135 = 13{,}5\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Dẫn $2{,}479\text{ L}$ khí carbon dioxide ($\text{CO}_2$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) vào dung dịch nước vôi trong "
                    r"$\text{Ca(OH)}_2$ dư. Tính khối lượng kết tủa $\text{CaCO}_3$ ($M = 100\text{ g/mol}$) tạo thành."
                ),
                "solution": (
                    r"Số mol $\text{CO}_2$ ở đkc là $n_{\text{CO}_2} = \dfrac{2{,}479}{24{,}79} = 0{,}1\text{ mol}$. Phương trình hóa học khi $\text{Ca(OH)}_2$ dư: "
                    r"$\text{CO}_2 + \text{Ca(OH)}_2 \longrightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O}$. Suy ra $n_{\text{CaCO}_3} = n_{\text{CO}_2} = 0{,}1\text{ mol}$, "
                    r"khối lượng kết tủa là $m_{\text{CaCO}_3} = 0{,}1 \cdot 100 = 10\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"4 loại oxide cần phân biệt rõ: oxide base ($\text{CaO}, \text{CuO}, \text{Fe}_2\text{O}_3$), oxide acid ($\text{CO}_2, \text{SO}_2, \text{P}_2\text{O}_5$), oxide lưỡng tính ($\text{Al}_2\text{O}_3, \text{ZnO}$) và oxide trung tính ($\text{CO}, \text{NO}$).",
            r"Phân đạm cung cấp $\text{N}$ (phát triển thân, lá), phân lân cung cấp $\text{P}$ (phát triển rễ, chồi), phân kali cung cấp $\text{K}$ (tăng sức chống chịu và tạo đường/bột).",
            r"Lạm dụng phân bón hóa học gây thoái hóa đất và phú dưỡng nguồn nước, do đó cần kết hợp phân hữu cơ và bón theo quy tắc '4 đúng'.",
        ],
        questions=[
            mcq(
                question=r"Chất nào sau đây thuộc loại oxide lưỡng tính?",
                options=[r"$\text{CuO}$", r"$\text{Al}_2\text{O}_3$", r"$\text{CO}_2$", r"$\text{CO}$"],
                answer="B",
                level="biet",
                solution=r"$\text{Al}_2\text{O}_3$ (cùng với $\text{ZnO}$) là oxide lưỡng tính vì tác dụng được với cả dung dịch acid mạnh và dung dịch kiềm mạnh.",
            ),
            mcq(
                question=r"Dãy gồm các chất đều thuộc loại oxide trung tính (oxide không tạo muối) là:",
                options=[
                    r"$\text{CO}, \text{NO}$",
                    r"$\text{CO}_2, \text{SO}_2$",
                    r"$\text{CaO}, \text{MgO}$",
                    r"$\text{Al}_2\text{O}_3, \text{ZnO}$",
                ],
                answer="A",
                level="biet",
                solution=r"$\text{CO}$ (carbon monoxide) và $\text{NO}$ (nitrogen monoxide) là hai oxide trung tính điển hình, không tác dụng với acid hay base.",
            ),
            mcq(
                question=r"Phân bón hóa học nào sau đây thuộc nhóm phân đạm (cung cấp nguyên tố dinh dưỡng nitrogen $\text{N}$ cho cây trồng)?",
                options=[
                    r"$\text{KCl}$",
                    r"$\text{Ca(H}_2\text{PO}_4)_2$",
                    r"$(\text{NH}_2)_2\text{CO}$",
                    r"$\text{K}_2\text{SO}_4$",
                ],
                answer="C",
                level="biet",
                solution=r"Urea có công thức $(\text{NH}_2)_2\text{CO}$ chứa nguyên tố dinh dưỡng $\text{N}$ nên thuộc nhóm phân đạm.",
            ),
            mcq(
                question=r"Loại phân bón hóa học cung cấp nguyên tố phosphorus ($\text{P}$) giúp kích thích sự phát triển bộ rễ của cây trồng là:",
                options=[r"Phân đạm", r"Phân lân", r"Phân kali", r"Phân vi lượng"],
                answer="B",
                level="biet",
                solution=r"Phân lân cung cấp nguyên tố phosphorus ($\text{P}$) cho cây, thúc đẩy bộ rễ phát triển khỏe và quá trình đẻ nhánh, nảy chồi.",
            ),
            mcq(
                question=r"Để làm khô khí carbon monoxide ($\text{CO}$) có lẫn hơi nước và tạp chất khí sulfur dioxide ($\text{SO}_2$), người ta có thể dẫn hỗn hợp khí qua bình đựng lượng dư chất nào sau đây?",
                options=[
                    r"Dung dịch $\text{HCl}$ đặc",
                    r"Vôi sống $\text{CaO}$ (hoặc $\text{NaOH}$ rắn)",
                    r"Dung dịch $\text{H}_2\text{SO}_4$ loãng",
                    r"Bột $\text{CuO}$ ở nhiệt độ thường",
                ],
                answer="B",
                level="hieu",
                solution=r"$\text{CaO}$ (hoặc $\text{NaOH}$ rắn) hấp thụ cả hơi nước và oxide acid $\text{SO}_2$, trong khi $\text{CO}$ là oxide trung tính không phản ứng nên thoát ra tinh khiết.",
            ),
            mcq(
                question=r"Khi hòa tan bột iron(III) oxide ($\text{Fe}_2\text{O}_3$) màu nâu đỏ vào dung dịch sulfuric acid loãng ($\text{H}_2\text{SO}_4$) dư, muối tạo thành trong dung dịch có công thức hóa học là:",
                options=[
                    r"$\text{FeSO}_4$",
                    r"$\text{Fe}_2(\text{SO}_4)_3$",
                    r"$\text{FeSO}_3$",
                    r"$\text{Fe}_3(\text{SO}_4)_2$",
                ],
                answer="B",
                level="hieu",
                solution=r"Trong $\text{Fe}_2\text{O}_3$, nguyên tố $\text{Fe}$ có hóa trị $\text{III}$ nên khi tác dụng với $\text{H}_2\text{SO}_4\text{ loãng}$ tạo muối iron(III) sulfate: $\text{Fe}_2\text{O}_3 + 3\text{H}_2\text{SO}_4 \longrightarrow \text{Fe}_2(\text{SO}_4)_3 + 3\text{H}_2\text{O}$.",
            ),
            tf4(
                stem=r"Cho bốn oxide sau: $\text{CaO}$, $\text{SO}_2$, $\text{Al}_2\text{O}_3$ và $\text{CO}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) $\text{CaO}$ là một oxide base, tác dụng được với nước tạo thành dung dịch calcium hydroxide $\text{Ca(OH)}_2$.",
                    r"b) Khí $\text{SO}_2$ là một oxide base nên không tác dụng được với dung dịch $\text{NaOH}$.",
                    r"c) $\text{Al}_2\text{O}_3$ là oxide lưỡng tính nên vừa tác dụng được với dung dịch $\text{HCl}$, vừa tác dụng được với dung dịch $\text{NaOH}$.",
                    r"d) Khí $\text{CO}$ tác dụng mạnh với dung dịch $\text{Ca(OH)}_2$ ở nhiệt độ thường tạo kết tủa trắng $\text{CaCO}_3$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{CaO} + \text{H}_2\text{O} \longrightarrow \text{Ca(OH)}_2$. "
                    r"b) Sai vì $\text{SO}_2$ là một oxide acid, tác dụng với dung dịch $\text{NaOH}$ tạo muối $\text{Na}_2\text{SO}_3$ (hoặc $\text{NaHSO}_3$). "
                    r"c) Đúng vì $\text{Al}_2\text{O}_3$ là oxide lưỡng tính điển hình. "
                    r"d) Sai vì $\text{CO}$ là oxide trung tính, không tác dụng với dung dịch $\text{Ca(OH)}_2$ (chỉ có $\text{CO}_2$ mới tạo kết tủa $\text{CaCO}_3$)."
                ),
            ),
            tf4(
                stem=r"Trong sản xuất nông nghiệp, người nông dân sử dụng các loại phân bón hóa học như ammonium sulfate $(\text{NH}_4)_2\text{SO}_4$, calcium dihydrogenphosphate $\text{Ca(H}_2\text{PO}_4)_2$, potassium chloride $\text{KCl}$ và vôi bột $\text{CaO}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Phân bón $(\text{NH}_4)_2\text{SO}_4$ thuộc nhóm phân đạm, cung cấp nguyên tố nitrogen ($\text{N}$) cho cây trồng.",
                    r"b) Phân bón $\text{KCl}$ thuộc nhóm phân lân, cung cấp nguyên tố phosphorus ($\text{P}$) cho cây.",
                    r"c) Không nên trộn chung phân đạm ammonium như $(\text{NH}_4)_2\text{SO}_4$ với vôi bột $\text{CaO}$ vì sẽ làm thất thoát đạm dưới dạng khí $\text{NH}_3$.",
                    r"d) Bón càng nhiều phân hóa học vượt quá nhu cầu của cây thì đất càng tơi xốp và nguồn nước càng sạch.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $(\text{NH}_4)_2\text{SO}_4$ chứa nguyên tố $\text{N}$ dưới dạng ion $\text{NH}_4^+$. "
                    r"b) Sai vì $\text{KCl}$ thuộc nhóm phân kali, cung cấp nguyên tố potassium ($\text{K}$). "
                    r"c) Đúng vì $\text{CaO}$ gặp nước tạo $\text{Ca(OH)}_2$ có tính kiềm, phản ứng với $\text{NH}_4^+$ giải phóng khí $\text{NH}_3\uparrow$ gây mất đạm. "
                    r"d) Sai vì bón thừa phân hóa học làm đất chai cứng, chua hóa và gây ô nhiễm, phú dưỡng nguồn nước."
                ),
            ),
            mcq(
                question=r"Hòa tan hoàn toàn $16\text{ g}$ iron(III) oxide ($\text{Fe}_2\text{O}_3$, $M = 160\text{ g/mol}$) cần dùng vừa đủ $V\text{ (mL)}$ dung dịch $\text{H}_2\text{SO}_4$ $1{,}5\text{ M}$. Giá trị của $V$ là:",
                options=[r"$100\text{ mL}$", r"$150\text{ mL}$", r"$200\text{ mL}$", r"$300\text{ mL}$"],
                answer="C",
                level="vandung",
                solution=r"Ta có $n_{\text{Fe}_2\text{O}_3} = \dfrac{16}{160} = 0{,}1\text{ mol}$. Theo phương trình $\text{Fe}_2\text{O}_3 + 3\text{H}_2\text{SO}_4 \longrightarrow \text{Fe}_2(\text{SO}_4)_3 + 3\text{H}_2\text{O}$, số mol acid cần dùng là $n_{\text{H}_2\text{SO}_4} = 3 \cdot 0{,}1 = 0{,}3\text{ mol}$. Thể tích dung dịch là $V = \dfrac{0{,}3}{1{,}5} = 0{,}2\text{ L} = 200\text{ mL}$.",
            ),
            short(
                question=r"Hấp thụ hoàn toàn $4{,}958\text{ L}$ khí carbon dioxide ($\text{CO}_2$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) vào dung dịch $\text{Ca(OH)}_2$ dư theo phản ứng $\text{CO}_2 + \text{Ca(OH)}_2 \longrightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O}$. Tính khối lượng kết tủa $\text{CaCO}_3$ (theo đơn vị $\text{g}$, biết $M_{\text{CaCO}_3} = 100\text{ g/mol}$) thu được.",
                answer=["20", "20,0", "20.0"],
                level="vandung",
                solution=r"Số mol $\text{CO}_2$ ở đkc là $n_{\text{CO}_2} = \dfrac{4{,}958}{24{,}79} = 0{,}2\text{ mol}$. Theo phương trình hóa học, $n_{\text{CaCO}_3} = n_{\text{CO}_2} = 0{,}2\text{ mol}$. Khối lượng kết tủa $\text{CaCO}_3$ thu được là $m = 0{,}2 \cdot 100 = 20\text{ g}$.",
            ),
        ],
        description="Phân loại và tính chất hóa học của 4 nhóm oxide, vai trò và cách sử dụng các loại phân bón hóa học N, P, K theo chương trình KHTN 8 Kết nối tri thức.",
    ),
    lesson(
        grade=8,
        order=7,
        code="H8-C07",
        title="Chương 7: Tốc độ phản ứng, chất xúc tác và phản ứng tỏa nhiệt - thu nhiệt",
        topic="oxi-hoa-khu",
        summary=(
            r"Nắm vững khái niệm tốc độ phản ứng, 5 yếu tố ảnh hưởng đến tốc độ phản ứng (nồng độ, nhiệt độ, áp suất đối với chất khí, "
            r"diện tích bề mặt tiếp xúc đối với chất rắn, chất xúc tác), phân biệt phản ứng tỏa nhiệt - thu nhiệt và ứng dụng thực tiễn."
        ),
        objectives=[
            r"Nêu được khái niệm tốc độ phản ứng hóa học (đại lượng đặc trưng cho sự nhanh hay chậm của một phản ứng hóa học).",
            r"Trình bày được ảnh hưởng của 5 yếu tố: nồng độ, nhiệt độ, áp suất, diện tích bề mặt tiếp xúc và chất xúc tác đến tốc độ phản ứng.",
            r"Nêu được khái niệm chất xúc tác và chất ức chế; giải thích được một số biện pháp điều chỉnh tốc độ phản ứng trong đời sống và sản xuất.",
            r"Phân biệt được phản ứng tỏa nhiệt (giải phóng năng lượng nhiệt ra môi trường) và phản ứng thu nhiệt (hấp thụ năng lượng nhiệt từ môi trường).",
        ],
        formulas=[
            {
                "name": "Quan hệ giữa 4 yếu tố vật lý - hóa học và tốc độ phản ứng $v$",
                "formula": r"$C \uparrow \implies v \uparrow; \quad T \uparrow \implies v \uparrow; \quad p_{\text{khí}} \uparrow \implies v \uparrow; \quad S_{\text{bề mặt}} \uparrow \implies v \uparrow$",
                "note": r"Khi tăng nồng độ, nhiệt độ, áp suất khí hoặc diện tích bề mặt tiếp xúc, tần số va chạm hiệu quả tăng nên tốc độ phản ứng tăng",
            },
            {
                "name": "Vai trò của chất xúc tác trong phản ứng hóa học",
                "formula": r"$2\text{H}_2\text{O}_2 \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O} + \text{O}_2\uparrow$",
                "note": r"Chất xúc tác ($\text{MnO}_2$, enzyme) làm tăng tốc độ phản ứng nhưng giữ nguyên khối lượng và bản chất hóa học sau phản ứng",
            },
            {
                "name": "Phản ứng tỏa nhiệt và phản ứng thu nhiệt",
                "formula": r"$\text{Phản ứng tỏa nhiệt: }T_{\text{môi trường}} \uparrow; \quad \text{Phản ứng thu nhiệt: }T_{\text{môi trường}} \downarrow$",
                "note": r"Đốt cháy nhiên liệu ($\text{C}, \text{CH}_4, \text{C}_2\text{H}_5\text{OH}$) là phản ứng tỏa nhiệt; nung đá vôi $\text{CaCO}_3$ là phản ứng thu nhiệt",
            },
            {
                "name": "Tốc độ trung bình của phản ứng (biểu thức định lượng bổ trợ)",
                "formula": r"$\overline{v} = \dfrac{\Delta n}{V \cdot \Delta t} = \dfrac{\Delta C}{\Delta t}$",
                "note": r"$\Delta C$: độ biến thiên nồng độ mol của một chất trong khoảng thời gian $\Delta t$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Khái niệm tốc độ phản ứng",
                "content": (
                    r"Các phản ứng hóa học xảy ra nhanh chậm rất khác nhau: phản ứng đốt cháy khí gas hay kết tủa $\text{BaSO}_4$ xảy ra tức thời, "
                    r"trong khi sự gỉ sắt trong không khí ẩm hay quá trình lên men rượu xảy ra chậm trong nhiều ngày, nhiều tháng. "
                    r"Để đánh giá mức độ xảy ra nhanh hay chậm của một phản ứng hóa học, người ta dùng đại lượng tốc độ phản ứng, "
                    r"được xác định bằng độ biến thiên lượng chất (nồng độ, số mol, khối lượng hoặc thể tích khí) của một chất phản ứng hoặc sản phẩm "
                    r"trong một đơn vị thời gian."
                ),
            },
            {
                "title": "2. Năm yếu tố ảnh hưởng đến tốc độ phản ứng",
                "content": (
                    r"Có 5 yếu tố chính làm thay đổi tốc độ phản ứng: "
                    r"(1) Nồng độ: Tăng nồng độ chất phản ứng làm tăng số va chạm giữa các hạt, nên tốc độ phản ứng tăng (ví dụ: than cháy trong bình $\text{O}_2$ nguyên chất nhanh hơn trong không khí). "
                    r"(2) Nhiệt độ: Tăng nhiệt độ làm các hạt chuyển động nhanh hơn và va chạm mạnh hơn, nên tốc độ phản ứng tăng (ngược lại, bảo quản thực phẩm trong tủ lạnh để giảm tốc độ phân hủy). "
                    r"(3) Áp suất (với phản ứng có chất khí): Tăng áp suất làm nồng độ chất khí tăng nên tốc độ phản ứng tăng. "
                    r"(4) Diện tích bề mặt tiếp xúc (với chất rắn): Đập nhỏ, nghiền mịn hoặc chẻ nhỏ chất rắn làm tăng diện tích bề mặt tiếp xúc nên tốc độ phản ứng tăng. "
                    r"(5) Chất xúc tác: Chất làm tăng tốc độ phản ứng nhưng không bị tiêu hao sau khi phản ứng kết thúc (ví dụ $\text{MnO}_2$ xúc tác phân hủy $\text{H}_2\text{O}_2$)."
                ),
            },
            {
                "title": "3. Phản ứng tỏa nhiệt và phản ứng thu nhiệt",
                "content": (
                    r"Phản ứng tỏa nhiệt là phản ứng hóa học có giải phóng năng lượng dưới dạng nhiệt ra môi trường xung quanh làm nhiệt độ môi trường tăng lên "
                    r"(ví dụ: phản ứng đốt cháy than, xăng dầu, khí methane $\text{CH}_4$, phản ứng tôi vôi $\text{CaO} + \text{H}_2\text{O} \longrightarrow \text{Ca(OH)}_2$). "
                    r"Phản ứng thu nhiệt là phản ứng hóa học cần hấp thụ năng lượng dưới dạng nhiệt từ môi trường xung quanh trong suốt quá trình phản ứng "
                    r"(ví dụ: phản ứng nung đá vôi $\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$, hòa tan viên C sủi vào nước)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Cho hai mẫu đá vôi ($\text{CaCO}_3$) có cùng khối lượng $5\text{ g}$: mẫu 1 ở dạng viên lớn, mẫu 2 được đập nhỏ thành dạng bột mịn. "
                    r"Cùng cho hai mẫu vào hai cốc chứa $100\text{ mL}$ dung dịch $\text{HCl}$ $1\text{ M}$ ở $25^\circ\text{C}$. Hãy cho biết ở cốc nào khí $\text{CO}_2$ "
                    r"thoát ra nhanh hơn và giải thích."
                ),
                "solution": (
                    r"Ở cốc chứa mẫu 2 ($\text{CaCO}_3$ dạng bột mịn), bọt khí $\text{CO}_2$ thoát ra nhanh và mạnh hơn hẳn so với mẫu 1. "
                    r"Nguyên nhân là với cùng khối lượng $5\text{ g}$, $\text{CaCO}_3$ dạng bột mịn có diện tích bề mặt tiếp xúc với dung dịch $\text{HCl}$ "
                    r"lớn hơn nhiều so với dạng viên lớn, làm tăng số va chạm hiệu quả nên tốc độ phản ứng lớn hơn."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Trong thí nghiệm phân hủy $100\text{ mL}$ dung dịch $\text{H}_2\text{O}_2$ có mặt xúc tác $\text{MnO}_2$, sau $20\text{ giây}$ thu được "
                    r"$0{,}4958\text{ L}$ khí $\text{O}_2$ ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$). Tính số mol $\text{H}_2\text{O}_2$ đã bị phân hủy "
                    r"và tốc độ trung bình tính theo số mol $\text{H}_2\text{O}_2$ phản ứng trong mỗi giây."
                ),
                "solution": (
                    r"Số mol khí $\text{O}_2$ thu được ở đkc là $n_{\text{O}_2} = \dfrac{0{,}4958}{24{,}79} = 0{,}02\text{ mol}$. Theo phương trình "
                    r"$2\text{H}_2\text{O}_2 \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O} + \text{O}_2\uparrow$, số mol $\text{H}_2\text{O}_2$ đã phân hủy là "
                    r"$n_{\text{H}_2\text{O}_2} = 2 \cdot 0{,}02 = 0{,}04\text{ mol}$. Tốc độ phân hủy trung bình là $\dfrac{0{,}04}{20} = 0{,}002\text{ mol/s}$."
                ),
            },
        ],
        key_takeaways=[
            r"5 yếu tố làm tăng tốc độ phản ứng: tăng nồng độ, tăng nhiệt độ, tăng áp suất (đối với chất khí), tăng diện tích bề mặt tiếp xúc (đối với chất rắn) và dùng chất xúc tác thích hợp.",
            r"Chất xúc tác chỉ làm tăng tốc độ phản ứng mà vẫn giữ nguyên khối lượng cũng như tính chất hóa học sau khi phản ứng kết thúc.",
            r"Phản ứng tỏa nhiệt giải phóng nhiệt làm nóng môi trường xung quanh; phản ứng thu nhiệt hấp thụ nhiệt từ môi trường.",
        ],
        questions=[
            mcq(
                question=r"Yếu tố nào sau đây không làm thay đổi tốc độ của phản ứng chỉ có chất rắn và dung dịch lỏng tham gia (không có chất khí)?",
                options=[
                    r"Nhiệt độ của hỗn hợp phản ứng",
                    r"Nồng độ của dung dịch chất phản ứng",
                    r"Áp suất bên ngoài tác dụng lên bình phản ứng",
                    r"Diện tích bề mặt tiếp xúc của chất rắn",
                ],
                answer="C",
                level="biet",
                solution=r"Áp suất chỉ ảnh hưởng đến tốc độ của các phản ứng có chất khí tham gia; với phản ứng không có chất khí, áp suất hầu như không ảnh hưởng.",
            ),
            mcq(
                question=r"Việc chẻ nhỏ củi trước khi đưa vào bếp đun nấu nhằm làm tăng tốc độ phản ứng cháy thông qua yếu tố nào?",
                options=[
                    r"Tăng diện tích bề mặt tiếp xúc",
                    r"Tăng áp suất khí quyển",
                    r"Bổ sung chất xúc tác",
                    r"Giảm nhiệt độ phản ứng",
                ],
                answer="A",
                level="biet",
                solution=r"Chẻ nhỏ củi giúp làm tăng diện tích bề mặt tiếp xúc giữa củi (chất rắn) với khí oxygen trong không khí, giúp củi cháy nhanh hơn.",
            ),
            mcq(
                question=r"Trong phản ứng phân hủy hydrogen peroxide $2\text{H}_2\text{O}_2 \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O} + \text{O}_2\uparrow$, bột $\text{MnO}_2$ đóng vai trò là:",
                options=[
                    r"Chất tham gia phản ứng bị tiêu hao hết",
                    r"Chất sản phẩm của phản ứng",
                    r"Chất xúc tác làm tăng tốc độ phản ứng",
                    r"Chất ức chế làm chậm phản ứng",
                ],
                answer="C",
                level="biet",
                solution=r"$\text{MnO}_2$ làm tăng mạnh tốc độ phân hủy $\text{H}_2\text{O}_2$ nhưng khối lượng và bản chất hóa học của $\text{MnO}_2$ không đổi sau phản ứng, nên $\text{MnO}_2$ là chất xúc tác.",
            ),
            mcq(
                question=r"Phản ứng hóa học nào sau đây là phản ứng thu nhiệt?",
                options=[
                    r"Đốt cháy khí methane ($\text{CH}_4$) trong bếp gas",
                    r"Đốt cháy cồn ($\text{C}_2\text{H}_5\text{OH}$) trong đèn cồn",
                    r"Nung đá vôi ($\text{CaCO}_3$) ở nhiệt độ cao tạo vôi sống ($\text{CaO}$) và $\text{CO}_2$",
                    r"Cho vôi sống ($\text{CaO}$) tác dụng với nước (tôi vôi)",
                ],
                answer="C",
                level="biet",
                solution=r"Phản ứng nhiệt phân đá vôi $\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$ cần cung cấp nhiệt liên tục nên là phản ứng thu nhiệt.",
            ),
            mcq(
                question=r"Cho cùng một lượng kẽm ($\text{Zn}$) dạng hạt vào bốn ống nghiệm chứa dung dịch $\text{HCl}$ ở cùng điều kiện. Khí $\text{H}_2$ thoát ra nhanh nhất ở ống nghiệm chứa:",
                options=[
                    r"Dung dịch $\text{HCl}$ $0{,}5\text{ M}$ ở $25^\circ\text{C}$",
                    r"Dung dịch $\text{HCl}$ $2{,}0\text{ M}$ ở $25^\circ\text{C}$",
                    r"Dung dịch $\text{HCl}$ $0{,}5\text{ M}$ ở $50^\circ\text{C}$",
                    r"Dung dịch $\text{HCl}$ $2{,}0\text{ M}$ ở $50^\circ\text{C}$",
                ],
                answer="D",
                level="hieu",
                solution=r"Ống nghiệm chứa dung dịch $\text{HCl}$ có cả nồng độ lớn nhất ($2{,}0\text{ M}$) và nhiệt độ cao nhất ($50^\circ\text{C}$) sẽ cho tốc độ phản ứng lớn nhất.",
            ),
            mcq(
                question=r"Vì sao người ta bảo quản thực phẩm tươi sống (thịt, cá, rau quả) trong tủ lạnh?",
                options=[
                    r"Để làm tăng tốc độ các phản ứng sinh hóa trong thực phẩm",
                    r"Để hạ thấp nhiệt độ, làm giảm tốc độ phân hủy thực phẩm của vi sinh vật và enzyme",
                    r"Để làm tăng diện tích tiếp xúc của thực phẩm với không khí",
                    r"Để biến các phản ứng tỏa nhiệt thành phản ứng thu nhiệt",
                ],
                answer="B",
                level="hieu",
                solution=r"Trong tủ lạnh nhiệt độ thấp làm giảm mạnh tốc độ các phản ứng oxi hóa và phân hủy do enzyme của vi sinh vật, giúp thực phẩm lâu hỏng.",
            ),
            tf4(
                stem=r"Trong phòng thí nghiệm, một học sinh thêm $0{,}5\text{ g}$ bột đen $\text{MnO}_2$ vào ống nghiệm chứa dung dịch $\text{H}_2\text{O}_2$ thấy bọt khí $\text{O}_2$ thoát ra rất mạnh theo phản ứng $2\text{H}_2\text{O}_2 \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O} + \text{O}_2\uparrow$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Bột $\text{MnO}_2$ là chất xúc tác giúp làm tăng tốc độ phân hủy của $\text{H}_2\text{O}_2$.",
                    r"b) Sau khi $\text{H}_2\text{O}_2$ phân hủy hết, khối lượng bột $\text{MnO}_2$ giảm đi một nửa.",
                    r"c) Nếu thay dung dịch $\text{H}_2\text{O}_2$ $3\text{\%}$ bằng dung dịch $\text{H}_2\text{O}_2$ $10\text{\%}$ ở cùng nhiệt độ thì tốc độ thoát khí $\text{O}_2$ ban đầu sẽ nhanh hơn.",
                    r"d) Nếu không có $\text{MnO}_2$, dung dịch $\text{H}_2\text{O}_2$ hoàn toàn không thể bị phân hủy ở bất kì nhiệt độ nào.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{MnO}_2$ đóng vai trò chất xúc tác làm tăng tốc độ phân hủy $\text{H}_2\text{O}_2$. "
                    r"b) Sai vì chất xúc tác không bị tiêu hao sau phản ứng nên khối lượng $\text{MnO}_2$ thu hồi được vẫn là $0{,}5\text{ g}$. "
                    r"c) Đúng vì tăng nồng độ chất phản ứng $\text{H}_2\text{O}_2$ từ $3\text{\%}$ lên $10\text{\%}$ làm tăng tốc độ phản ứng. "
                    r"d) Sai vì khi không có xúc tác, $\text{H}_2\text{O}_2$ vẫn tự phân hủy chậm (và phân hủy nhanh hơn khi đun nóng hoặc chiếu sáng)."
                ),
            ),
            tf4(
                stem=r"Xét các biện pháp điều khiển tốc độ phản ứng và sự biến thiên nhiệt trong thực tiễn đời sống và sản xuất. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Khi nướng bánh hoặc ủ rượu, men vi sinh chứa các enzyme đóng vai trò là chất xúc tác sinh học.",
                    r"b) Đập nhỏ quặng pyrite ($\text{FeS}_2$) trước khi đưa vào lò đốt để sản xuất $\text{SO}_2$ nhằm mục đích làm giảm tốc độ phản ứng.",
                    r"c) Phản ứng đốt cháy nhiên liệu xăng, dầu, khí hóa lỏng ($\text{LPG}$) trong động cơ và bếp đun là các phản ứng tỏa nhiệt.",
                    r"d) Nấu thức ăn trong nồi áp suất lâu chín hơn so với nồi thường vì áp suất và nhiệt độ nước sôi trong nồi áp suất thấp hơn.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì enzyme trong men là chất xúc tác sinh học thúc đẩy nhanh quá trình lên men ở nhiệt độ thường. "
                    r"b) Sai vì đập nhỏ quặng làm tăng diện tích bề mặt tiếp xúc nhằm tăng tốc độ phản ứng đốt quặng. "
                    r"c) Đúng vì quá trình đốt cháy nhiên liệu luôn giải phóng lượng nhiệt lớn ra môi trường. "
                    r"d) Sai vì trong nồi áp suất, áp suất và nhiệt độ sôi của nước cao hơn ($> 100^\circ\text{C}$) nên tốc độ phản ứng làm chín thức ăn nhanh hơn."
                ),
            ),
            mcq(
                question=r"Thực hiện phản ứng $\text{Mg} + 2\text{HCl} \longrightarrow \text{MgCl}_2 + \text{H}_2\uparrow$ trong bình chứa $200\text{ mL}$ dung dịch $\text{HCl}$ (coi thể tích dung dịch không đổi). Sau $50\text{ giây}$, nồng độ của dung dịch $\text{HCl}$ giảm từ $1{,}2\text{ M}$ xuống còn $0{,}4\text{ M}$. Tốc độ trung bình của phản ứng tính theo độ giảm nồng độ $\text{HCl}$ trong khoảng thời gian trên là:",
                options=[
                    r"$0{,}008\text{ M/s}$",
                    r"$0{,}016\text{ M/s}$",
                    r"$0{,}024\text{ M/s}$",
                    r"$0{,}032\text{ M/s}$",
                ],
                answer="B",
                level="vandung",
                solution=r"Độ giảm nồng độ $\text{HCl}$ là $\Delta C = 1{,}2 - 0{,}4 = 0{,}8\text{ M}$. Tốc độ trung bình tính theo $\text{HCl}$ là $\overline{v} = \dfrac{\Delta C}{\Delta t} = \dfrac{0{,}8}{50} = 0{,}016\text{ M/s}$.",
            ),
            short(
                question=r"Cho lượng dư bột kẽm ($\text{Zn}$) tác dụng với dung dịch $\text{H}_2\text{SO}_4\text{ loãng}$. Sau $10\text{ giây}$ đầu tiên, thu được $0{,}7437\text{ L}$ khí $\text{H}_2$ ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$). Tính tốc độ trung bình của phản ứng tính theo số mol khí $\text{H}_2$ tạo thành trong mỗi giây (đơn vị $\text{mol/s}$).",
                answer=["0,003", "0.003"],
                level="vandung",
                solution=r"Số mol khí $\text{H}_2$ thu được ở đkc sau $10\text{ giây}$ là $n_{\text{H}_2} = \dfrac{0{,}7437}{24{,}79} = 0{,}03\text{ mol}$. Tốc độ trung bình tính theo số mol $\text{H}_2$ mỗi giây là $\dfrac{0{,}03}{10} = 0{,}003\text{ mol/s}$.",
            ),
        ],
        description="Khái niệm tốc độ phản ứng, 5 yếu tố ảnh hưởng đến tốc độ phản ứng, chất xúc tác và phản ứng tỏa nhiệt - thu nhiệt theo chương trình KHTN 8 Kết nối tri thức.",
    ),
]


LESSONS = LESSONS_GRADE_8
