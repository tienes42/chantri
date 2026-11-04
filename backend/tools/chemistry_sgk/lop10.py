from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_10: list[dict[str, Any]] = [
    # =========================================================================
    # CHƯƠNG 1: THÀNH PHẦN NGUYÊN TỬ, NGUYÊN TỐ HÓA HỌC VÀ ĐỒNG VỊ
    # =========================================================================
    lesson(
        grade=10,
        order=1,
        code="H10-C01",
        title="Chương 1: Thành phần nguyên tử, nguyên tố hóa học và đồng vị",
        topic="cau-tao-nguyen-tu",
        summary=(
            r"Nguyên tử là hạt vô cùng nhỏ, trung hòa về điện, cấu tạo gồm hạt nhân mang điện tích dương "
            r"(chứa hạt proton $p$ và neutron $n$) và vỏ nguyên tử mang điện tích âm (chứa các hạt electron $e$). "
            r"Mỗi nguyên tố hóa học được đặc trưng bởi số hiệu nguyên tử $Z$ (bằng số đơn vị điện tích hạt nhân $Z = p = e$). "
            r"Tổng số proton và neutron trong hạt nhân gọi là số khối $A = Z + N$, biểu diễn qua ký hiệu nguyên tử ${}_Z^A\text{X}$. "
            r"Các đồng vị của cùng một nguyên tố có cùng số proton $Z$ nhưng khác số neutron $N$, và nguyên tử khối trung bình "
            r"được tính theo công thức $\overline{A} = \dfrac{A_1 x_1 + A_2 x_2 + \dots}{100}$."
        ),
        objectives=[
            r"Trình bày được thành phần cấu tạo nguyên tử gồm hạt nhân (proton $p$, neutron $n$) và lớp vỏ (electron $e$); so sánh khối lượng và điện tích của các hạt cơ bản.",
            r"So sánh được kích thước của nguyên tử (cỡ $10^{-10}\text{ m} = 100\text{ pm}$) và hạt nhân nguyên tử (cỡ $10^{-14}\text{ m} = 0,01\text{ pm}$); giải thích vì sao khối lượng nguyên tử tập trung hầu hết ở hạt nhân.",
            r"Nêu được khái niệm nguyên tố hóa học, số hiệu nguyên tử $Z$, số khối $A = Z + N$ và viết đúng ký hiệu nguyên tử ${}_Z^A\text{X}$.",
            r"Trình bày được khái niệm đồng vị và vận dụng thành thạo công thức tính nguyên tử khối trung bình $\overline{A} = \dfrac{A_1 x_1 + A_2 x_2 + \dots}{100}$ từ phổ khối lượng hoặc thành phần phần trăm số nguyên tử.",
        ],
        formulas=[
            {
                "name": r"Điều kiện trung hòa điện của nguyên tử",
                "formula": r"$Z = p = e$",
                "note": r"Số đơn vị điện tích hạt nhân $Z$ bằng số proton $p$ và bằng số electron $e$ trong nguyên tử trung hòa.",
            },
            {
                "name": r"Số khối của hạt nhân nguyên tử",
                "formula": r"$A = Z + N = p + n \Rightarrow N = A - Z$",
                "note": r"$A$: số khối; $Z$: số hiệu nguyên tử (số hạt proton $p$); $N$: số hạt neutron $n$.",
            },
            {
                "name": r"Ký hiệu nguyên tử chuẩn IUPAC",
                "formula": r"${}_Z^A\text{X}$",
                "note": r"Ví dụ: ${}_{11}^{23}\text{Na}$ có $Z = p = e = 11$, $A = 23$ và $N = 23 - 11 = 12$.",
            },
            {
                "name": r"Tổng số hạt cơ bản trong nguyên tử",
                "formula": r"$S = p + n + e = 2Z + N$",
                "note": r"Với các nguyên tố bền có $2 \le Z \le 82$: $1 \le \dfrac{N}{Z} \le 1,52 \Leftrightarrow \dfrac{S}{3,52} \le Z \le \dfrac{S}{3}$.",
            },
            {
                "name": r"Số hạt electron trong ion đơn nguyên tử",
                "formula": r"$e(\text{M}^{k+}) = Z - k \quad ; \quad e(\text{X}^{m-}) = Z + m$",
                "note": r"Khi nguyên tử nhường hoặc nhận electron tạo ion, số proton $p$ và số neutron $n$ giữ nguyên.",
            },
            {
                "name": r"Nguyên tử khối trung bình của nguyên tố có nhiều đồng vị",
                "formula": r"$\overline{A} = \dfrac{A_1 x_1 + A_2 x_2 + \dots + A_k x_k}{100}$",
                "note": r"$A_i$: số khối (hoặc nguyên tử khối) của đồng vị thứ $i$; $x_i$: phần trăm số nguyên tử của đồng vị thứ $i$ ($x_1 + x_2 + \dots + x_k = 100$).",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Thành phần cấu tạo nguyên tử",
                "content": (
                    r"Nguyên tử gồm hai phần: hạt nhân nằm ở tâm nguyên tử và lớp vỏ gồm các electron chuyển động xung quanh hạt nhân. "
                    r"Hạt nhân được cấu tạo bởi hai loại hạt là proton (ký hiệu $p$, mang điện tích $+1e_0 \approx +1,602 \times 10^{-19}\text{ C}$, "
                    r"khối lượng $m_p \approx 1\text{ amu}$) và neutron (ký hiệu $n$, không mang điện, điện tích bằng $0$, khối lượng $m_n \approx 1\text{ amu}$). "
                    r"Riêng nguyên tử đồng vị phổ biến nhất của hydrogen là protium (${}_1^1\text{H}$) chỉ có $1$ proton trong hạt nhân mà không có neutron ($N = 0$). "
                    r"Lớp vỏ nguyên tử chứa các hạt electron (ký hiệu $e$, mang điện tích $-1e_0 \approx -1,602 \times 10^{-19}\text{ C}$, "
                    r"khối lượng $m_e \approx 0,00055\text{ amu} \approx 9,11 \times 10^{-28}\text{ g}$). Vì nguyên tử trung hòa về điện nên số proton luôn bằng số electron ($p = e$)."
                ),
            },
            {
                "title": r"2. Kích thước và khối lượng của nguyên tử",
                "content": (
                    r"Kích thước của nguyên tử là khoảng không gian tạo bởi sự chuyển động của các electron quanh hạt nhân. "
                    r"Đường kính của nguyên tử cỡ $10^{-10}\text{ m}$ ($100\text{ pm}$ hay $1\text{ \AA}$), trong khi đường kính của hạt nhân chỉ khoảng $10^{-14}\text{ m}$ ($0,01\text{ pm}$), "
                    r"tức là đường kính nguyên tử lớn gấp khoảng $10\,000$ lần đường kính hạt nhân. Do đó, nguyên tử có cấu tạo rỗng. "
                    r"Đơn vị khối lượng nguyên tử ký hiệu là $\text{amu}$ ($1\text{ amu} = \dfrac{1}{12}$ khối lượng của một nguyên tử carbon-${}_{6}^{12}\text{C} \approx 1,6605 \times 10^{-24}\text{ g}$). "
                    r"Vì khối lượng của electron rất nhỏ ($m_e \approx 0,00055\text{ amu}$) so với khối lượng của proton và neutron ($m_p \approx m_n \approx 1\text{ amu}$), "
                    r"nên khối lượng của nguyên tử tập trung hầu hết ở hạt nhân và có giá trị xấp xỉ bằng số khối $A$ (tính theo $\text{amu}$)."
                ),
            },
            {
                "title": r"3. Nguyên tố hóa học, số hiệu nguyên tử và ký hiệu nguyên tử",
                "content": (
                    r"Nguyên tố hóa học là tập hợp những nguyên tử có cùng điện tích hạt nhân (cùng số proton $p$). "
                    r"Số đơn vị điện tích hạt nhân nguyên tử của một nguyên tố được gọi là số hiệu nguyên tử (ký hiệu $Z$). "
                    r"Tổng số hạt proton ($Z$) và tổng số hạt neutron ($N$) trong hạt nhân được gọi là số khối (ký hiệu $A$), với $A = Z + N$. "
                    r"Ký hiệu nguyên tử ${}_Z^A\text{X}$ cho biết đầy đủ các đặc trưng cơ bản của một nguyên tử: ký hiệu hóa học $\text{X}$, "
                    r"số hiệu nguyên tử $Z$ (viết ở chỉ số dưới bên trái) và số khối $A$ (viết ở chỉ số trên bên trái). "
                    r"Ví dụ, ký hiệu ${}_{26}^{56}\text{Fe}$ cho biết nguyên tử iron (sắt) có $Z = p = e = 26$, số khối $A = 56$ và số neutron $N = 56 - 26 = 30$."
                ),
            },
            {
                "title": r"4. Đồng vị và nguyên tử khối trung bình",
                "content": (
                    r"Các đồng vị của cùng một nguyên tố hóa học là những nguyên tử có cùng số hạt proton ($Z$) nhưng khác nhau về số hạt neutron ($N$), "
                    r"do đó số khối ($A$) của chúng khác nhau. Vì có cùng số proton và cùng cấu trúc lớp vỏ electron nên các đồng vị của cùng một nguyên tố "
                    r"có tính chất hóa học giống nhau. Ví dụ, nguyên tố hydrogen có ba đồng vị tự nhiên là ${}_1^1\text{H}$ (protium), ${}_1^2\text{H}$ (deuterium) và ${}_1^3\text{H}$ (tritium); "
                    r"nguyên tố chlorine có hai đồng vị bền là ${}_{17}^{35}\text{Cl}$ (chiếm $75,77\%$) và ${}_{17}^{37}\text{Cl}$ (chiếm $24,23\%$). "
                    r"Nguyên tử khối của một nguyên tố là khối lượng trung bình của một nguyên tử nguyên tố đó (tính theo đơn vị $\text{amu}$), "
                    r"được xác định bằng công thức $\overline{A} = \dfrac{A_1 x_1 + A_2 x_2 + \dots + A_k x_k}{100}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Xác định thành phần hạt từ ký hiệu nguyên tử và ion",
                "problem": (
                    r"Cho nguyên tử sodium ${}_{11}^{23}\text{Na}$ và nguyên tử iron ${}_{26}^{56}\text{Fe}$. "
                    r"Hãy xác định số hạt proton $p$, neutron $n$, electron $e$ trong các nguyên tử ${}_{11}^{23}\text{Na}$, ${}_{26}^{56}\text{Fe}$ "
                    r"và trong các ion tương ứng ${}_{11}^{23}\text{Na}^+$, ${}_{26}^{56}\text{Fe}^{3+}$."
                ),
                "solution": (
                    r"• Đối với nguyên tử ${}_{11}^{23}\text{Na}$: Ta có $Z = 11$ và $A = 23$, suy ra số hạt proton $p = 11$, số hạt electron $e = 11$ "
                    r"và số hạt neutron $n = A - Z = 23 - 11 = 12$. Khi nguyên tử $\text{Na}$ nhường $1$ electron để tạo thành cation ${}_{11}^{23}\text{Na}^+$, "
                    r"số hạt trong hạt nhân không đổi ($p = 11$, $n = 12$) còn số electron là $e = 11 - 1 = 10$. "
                    r"• Đối với nguyên tử ${}_{26}^{56}\text{Fe}$: Ta có $Z = 26$ và $A = 56$, suy ra $p = e = 26$ và $n = 56 - 26 = 30$. "
                    r"Khi tạo thành cation ${}_{26}^{56}\text{Fe}^{3+}$ (nhường $3$ electron), hạt nhân vẫn có $p = 26$, $n = 30$, còn lớp vỏ có $e = 26 - 3 = 23$."
                ),
            },
            {
                "title": r"Ví dụ 2: Tính nguyên tử khối trung bình và phần trăm đồng vị",
                "problem": (
                    r"Trong tự nhiên, nguyên tố copper (đồng, $\text{Cu}$) có hai đồng vị bền là ${}_{29}^{63}\text{Cu}$ và ${}_{29}^{65}\text{Cu}$. "
                    r"Biết nguyên tử khối trung bình của copper là $\overline{A}_{\text{Cu}} = 63,54$. "
                    r"Tính thành phần phần trăm số nguyên tử của mỗi đồng vị và phần trăm khối lượng của ${}_{29}^{63}\text{Cu}$ trong hợp chất $\text{CuSO}_4$ "
                    r"(cho nguyên tử khối của $\text{S} = 32$, $\text{O} = 16$)."
                ),
                "solution": (
                    r"Gọi thành phần phần trăm số nguyên tử của đồng vị ${}_{29}^{63}\text{Cu}$ là $x\%$ ($0 < x < 100$), suy ra phần trăm số nguyên tử của đồng vị ${}_{29}^{65}\text{Cu}$ là $(100 - x)\%$. "
                    r"Áp dụng công thức tính nguyên tử khối trung bình: $\overline{A}_{\text{Cu}} = \dfrac{63x + 65(100 - x)}{100} = 63,54 \Leftrightarrow 6500 - 2x = 6354 \Rightarrow x = 73\%$. "
                    r"Vậy trong tự nhiên, đồng vị ${}_{29}^{63}\text{Cu}$ chiếm $73\%$ và đồng vị ${}_{29}^{65}\text{Cu}$ chiếm $27\%$ về số nguyên tử. "
                    r"Phân tử khối trung bình của $\text{CuSO}_4$ là $M_{\text{CuSO}_4} = 63,54 + 32 + 4 \times 16 = 159,54\text{ g/mol}$. "
                    r"Trong $1\text{ mol}$ $\text{CuSO}_4$ có $1\text{ mol}$ nguyên tử $\text{Cu}$, trong đó có $0,73\text{ mol}$ đồng vị ${}_{29}^{63}\text{Cu}$ (khối lượng $0,73 \times 63 = 45,99\text{ g}$). "
                    r"Phần trăm khối lượng của ${}_{29}^{63}\text{Cu}$ trong $\text{CuSO}_4$ là $\%m_{{}_{29}^{63}\text{Cu}} = \dfrac{45,99}{159,54} \times 100\% \approx 28,83\%$."
                ),
            },
        ],
        key_takeaways=[
            r"Nguyên tử trung hòa về điện có $Z = p = e$; hạt nhân mang điện dương (gồm $p$ và $n$), lớp vỏ mang điện âm (gồm $e$).",
            r"Khối lượng nguyên tử tập trung hầu hết ở hạt nhân vì $m_p \approx m_n \approx 1\text{ amu} \gg m_e \approx 0,00055\text{ amu}$; số khối $A = Z + N$.",
            r"Nguyên tố hóa học gồm các nguyên tử có cùng số proton $Z$; các đồng vị có cùng $Z$ nhưng khác số neutron $N$ (khác $A$).",
            r"Công thức nguyên tử khối trung bình: $\overline{A} = \dfrac{A_1 x_1 + A_2 x_2 + \dots + A_k x_k}{100}$ với $\sum x_i = 100\%$.",
        ],
        questions=[
            mcq(
                question=r"Các hạt cấu tạo nên hạt nhân của hầu hết các nguyên tử (trừ đồng vị ${}_1^1\text{H}$) là:",
                options=[
                    r"Electron và neutron.",
                    r"Proton và neutron.",
                    r"Proton và electron.",
                    r"Proton, neutron và electron.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Hạt nhân của hầu hết các nguyên tử được cấu tạo bởi hai loại hạt là proton ($p$, mang điện dương) "
                    r"và neutron ($n$, không mang điện). Riêng hạt nhân nguyên tử đồng vị ${}_1^1\text{H}$ chỉ có $1$ proton và không có neutron."
                ),
            ),
            mcq(
                question=r"Cho ký hiệu nguyên tử của nguyên tố chlorine là ${}_{17}^{35}\text{Cl}$. Số hạt proton, neutron và electron của nguyên tử này lần lượt là:",
                options=[
                    r"$17$, $35$, $17$.",
                    r"$17$, $18$, $17$.",
                    r"$18$, $17$, $18$.",
                    r"$35$, $17$, $18$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Từ ký hiệu nguyên tử ${}_{17}^{35}\text{Cl}$, ta có số hiệu nguyên tử $Z = 17$ và số khối $A = 35$. "
                    r"Do đó: số proton $p = Z = 17$, số electron $e = Z = 17$, và số neutron $n = A - Z = 35 - 17 = 18$."
                ),
            ),
            mcq(
                question=r"Phát biểu nào sau đây là đúng khi nói về các đồng vị của cùng một nguyên tố hóa học?",
                options=[
                    r"Các đồng vị là những nguyên tử có cùng số khối $A$ nhưng khác số hiệu nguyên tử $Z$.",
                    r"Các đồng vị là những nguyên tử có cùng số neutron $N$ nhưng khác số proton $Z$.",
                    r"Các đồng vị là những nguyên tử có cùng số proton $Z$ nhưng khác nhau về số neutron $N$.",
                    r"Các đồng vị của cùng một nguyên tố có số electron lớp vỏ khác nhau.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Đồng vị của cùng một nguyên tố hóa học là những nguyên tử có cùng số hạt proton $Z$ (cùng điện tích hạt nhân) "
                    r"nhưng khác nhau về số hạt neutron $N$, dẫn đến số khối $A = Z + N$ khác nhau."
                ),
            ),
            mcq(
                question=r"Trong các hạt cơ bản cấu tạo nên nguyên tử, hạt không mang điện là:",
                options=[
                    r"Proton ($p$).",
                    r"Electron ($e$).",
                    r"Neutron ($n$).",
                    r"Hạt nhân nguyên tử.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Trong nguyên tử, hạt proton ($p$) mang điện tích $+1$, hạt electron ($e$) mang điện tích $-1$, "
                    r"còn hạt neutron ($n$) không mang điện (điện tích bằng $0$)."
                ),
            ),
            mcq(
                question=r"Cation iron(III) có ký hiệu ${}_{26}^{56}\text{Fe}^{3+}$. Số hạt proton, neutron và electron trong một ion ${}_{26}^{56}\text{Fe}^{3+}$ lần lượt là:",
                options=[
                    r"$26$, $30$, $26$.",
                    r"$26$, $30$, $23$.",
                    r"$26$, $30$, $29$.",
                    r"$23$, $30$, $26$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Nguyên tử ${}_{26}^{56}\text{Fe}$ có $Z = 26$, $A = 56 \Rightarrow p = 26$, $n = 56 - 26 = 30$, $e = 26$. "
                    r"Khi nguyên tử ${}_{26}^{56}\text{Fe}$ nhường $3$ electron để tạo thành cation ${}_{26}^{56}\text{Fe}^{3+}$, "
                    r"số hạt trong hạt nhân giữ nguyên ($p = 26$, $n = 30$) và số hạt electron còn lại là $e = 26 - 3 = 23$."
                ),
            ),
            mcq(
                question=(
                    r"Trong tự nhiên, nguyên tố chlorine có hai đồng vị bền là ${}_{17}^{35}\text{Cl}$ (chiếm $75,77\%$ tổng số nguyên tử) "
                    r"và ${}_{17}^{37}\text{Cl}$ (chiếm $24,23\%$ tổng số nguyên tử). Nguyên tử khối trung bình của chlorine là:"
                ),
                options=[
                    r"$35,48$.",
                    r"$36,00$.",
                    r"$35,24$.",
                    r"$36,52$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Áp dụng công thức tính nguyên tử khối trung bình của hỗn hợp đồng vị: "
                    r"$\overline{A}_{\text{Cl}} = \dfrac{35 \times 75,77 + 37 \times 24,23}{100} = \dfrac{2651,95 + 896,51}{100} = 35,4846 \approx 35,48$."
                ),
            ),
            tf4(
                stem=r"Cho nguyên tử của nguyên tố sodium có ký hiệu là ${}_{11}^{23}\text{Na}$. Xét tính đúng/sai của các phát biểu sau:",
                statements=[
                    r"a) Hạt nhân nguyên tử ${}_{11}^{23}\text{Na}$ có chứa $11$ hạt proton và $12$ hạt neutron.",
                    r"b) Tổng số hạt mang điện trong một nguyên tử ${}_{11}^{23}\text{Na}$ là $23$ hạt.",
                    r"c) Khi nguyên tử ${}_{11}^{23}\text{Na}$ nhường $1$ electron để tạo thành ion $\text{Na}^+$, ion tạo thành có $10$ electron và $12$ neutron.",
                    r"d) Khối lượng của nguyên tử ${}_{11}^{23}\text{Na}$ tập trung chủ yếu ở lớp vỏ electron.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Từ ký hiệu ${}_{11}^{23}\text{Na}$, ta có $Z = 11$ và $A = 23 \Rightarrow$ số hạt proton là $p = 11$ và số hạt neutron là $n = A - Z = 23 - 11 = 12$. "
                    r"• b) Sai: Các hạt mang điện trong nguyên tử là proton ($p$) và electron ($e$). Tổng số hạt mang điện là $p + e = 2Z = 2 \times 11 = 22$ hạt (không phải $23$ hạt). "
                    r"• c) Đúng: Khi nguyên tử ${}_{11}^{23}\text{Na}$ nhường $1$ electron tạo ion $\text{Na}^+$, số electron còn lại là $11 - 1 = 10$ hạt và số neutron trong hạt nhân giữ nguyên là $12$ hạt. "
                    r"• d) Sai: Vì $m_e \approx 0,00055\text{ amu}$ rất nhỏ so với $m_p \approx m_n \approx 1\text{ amu}$, nên khối lượng nguyên tử tập trung hầu hết ở hạt nhân chứ không phải ở lớp vỏ electron."
                ),
            ),
            tf4(
                stem=(
                    r"Trong tự nhiên, nguyên tố boron ($\text{B}$, $Z = 5$) có hai đồng vị bền là ${}_5^{10}\text{B}$ và ${}_5^{11}\text{B}$. "
                    r"Biết nguyên tử khối trung bình của boron là $\overline{A}_{\text{B}} = 10,81$. Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Hai đồng vị ${}_5^{10}\text{B}$ và ${}_5^{11}\text{B}$ có cùng số hạt proton là $5$ nhưng số hạt neutron lần lượt là $5$ và $6$.",
                    r"b) Trong tự nhiên, đồng vị ${}_5^{10}\text{B}$ chiếm $81\%$ và đồng vị ${}_5^{11}\text{B}$ chiếm $19\%$ tổng số nguyên tử boron.",
                    r"c) Trong hợp chất boric acid ($\text{H}_3\text{BO}_3$, cho $M_{\text{H}} = 1$, $M_{\text{O}} = 16$), phần trăm khối lượng của đồng vị ${}_5^{11}\text{B}$ là khoảng $14,41\%$.",
                    r"d) Hạt nhân đồng vị ${}_5^{11}\text{B}$ có điện tích lớn hơn hạt nhân đồng vị ${}_5^{10}\text{B}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Cả hai đồng vị đều có $Z = p = 5$; số neutron của ${}_5^{10}\text{B}$ là $N_1 = 10 - 5 = 5$ và của ${}_5^{11}\text{B}$ là $N_2 = 11 - 5 = 6$. "
                    r"• b) Sai: Gọi $x\%$ là phần trăm số nguyên tử của ${}_5^{10}\text{B}$, ta có $\dfrac{10x + 11(100 - x)}{100} = 10,81 \Rightarrow x = 19\%$. Vậy ${}_5^{10}\text{B}$ chiếm $19\%$ và ${}_5^{11}\text{B}$ chiếm $81\%$. "
                    r"• c) Đúng: Phân tử khối trung bình của $\text{H}_3\text{BO}_3$ là $M = 3 \times 1 + 10,81 + 3 \times 16 = 61,81\text{ g/mol}$. Phần trăm khối lượng của ${}_5^{11}\text{B}$ trong $\text{H}_3\text{BO}_3$ là $\%m_{{}_5^{11}\text{B}} = \dfrac{11 \times 0,81}{61,81} \times 100\% \approx 14,415\% \approx 14,41\%$. "
                    r"• d) Sai: Hai đồng vị của cùng một nguyên tố có cùng số proton ($Z = 5$) nên có cùng điện tích hạt nhân ($+5e_0$)."
                ),
            ),
            mcq(
                question=(
                    r"Tổng số hạt proton, neutron và electron trong nguyên tử của một nguyên tố $\text{X}$ là $40$, "
                    r"trong đó tổng số hạt mang điện nhiều hơn số hạt không mang điện là $12$. Ký hiệu nguyên tử của $\text{X}$ là:"
                ),
                options=[
                    r"${}_{12}^{24}\text{Mg}$.",
                    r"${}_{13}^{27}\text{Al}$.",
                    r"${}_{14}^{28}\text{Si}$.",
                    r"${}_{11}^{23}\text{Na}$.",
                ],
                answer="B",
                level="vandung",
                solution=(
                    r"Gọi số proton, electron và neutron của nguyên tử $\text{X}$ lần lượt là $Z$, $Z$ và $N$. "
                    r"Theo đề bài, tổng số hạt là $2Z + N = 40$ (1) và số hạt mang điện nhiều hơn số hạt không mang điện là $2Z - N = 12$ (2). "
                    r"Giải hệ phương trình (1) và (2) ta được $4Z = 52 \Rightarrow Z = 13$ và $N = 40 - 2 \times 13 = 14$. "
                    r"Số khối của $\text{X}$ là $A = Z + N = 13 + 14 = 27$. Vậy ký hiệu nguyên tử của $\text{X}$ là ${}_{13}^{27}\text{Al}$."
                ),
            ),
            short(
                question=(
                    r"Trong tự nhiên, nguyên tố hydrogen có $3$ đồng vị (${}_1^1\text{H}$, ${}_1^2\text{H}$, ${}_1^3\text{H}$) "
                    r"và nguyên tố oxygen có $3$ đồng vị (${}_8^{16}\text{O}$, ${}_8^{17}\text{O}$, ${}_8^{18}\text{O}$). "
                    r"Hỏi có thể tạo thành tối đa bao nhiêu loại phân tử nước ($\text{H}_2\text{O}$) khác nhau từ các đồng vị trên?"
                ),
                answer=["18"],
                level="vandung",
                solution=(
                    r"Mỗi phân tử $\text{H}_2\text{O}$ gồm $2$ nguyên tử $\text{H}$ liên kết với $1$ nguyên tử $\text{O}$. "
                    r"Số cách chọn bộ $2$ nguyên tử $\text{H}$ từ $3$ đồng vị ${}_1^1\text{H}$, ${}_1^2\text{H}$, ${}_1^3\text{H}$ gồm: "
                    r"$3$ cặp hai nguyên tử giống nhau (${}_1^1\text{H}-{}_1^1\text{H}$, ${}_1^2\text{H}-{}_1^2\text{H}$, ${}_1^3\text{H}-{}_1^3\text{H}$) "
                    r"và $3$ cặp hai nguyên tử khác nhau (${}_1^1\text{H}-{}_1^2\text{H}$, ${}_1^1\text{H}-{}_1^3\text{H}$, ${}_1^2\text{H}-{}_1^3\text{H}$), "
                    r"tổng cộng có $6$ cách chọn bộ $\text{H}_2$. Kết hợp với $3$ cách chọn đồng vị của oxygen (${}_8^{16}\text{O}$, ${}_8^{17}\text{O}$, ${}_8^{18}\text{O}$), "
                    r"số loại phân tử $\text{H}_2\text{O}$ tối đa tạo thành là $6 \times 3 = 18$."
                ),
            ),
        ],
        description="Tìm hiểu thành phần cấu tạo nguyên tử gồm hạt nhân (proton, neutron) và lớp vỏ electron, kích thước và khối lượng nguyên tử, ký hiệu nguyên tử, đồng vị và cách tính nguyên tử khối trung bình.",
    ),

    # =========================================================================
    # CHƯƠNG 2: CẤU TRÚC LỚP VỎ ELECTRON CỦA NGUYÊN TỬ
    # =========================================================================
    lesson(
        grade=10,
        order=2,
        code="H10-C02",
        title="Chương 2: Cấu trúc lớp vỏ electron của nguyên tử",
        topic="cau-hinh-electron",
        summary=(
            r"Theo mô hình hiện đại, trong nguyên tử các electron chuyển động rất nhanh xung quanh hạt nhân không theo những quỹ đạo xác định "
            r"mà tạo thành đám mây electron. Khu vực không gian xung quanh hạt nhân mà tại đó xác suất tìm thấy electron khoảng $90\%$ được gọi là "
            r"orbital nguyên tử ($\text{AO}$), gồm $\text{AO } s$ hình cầu và $\text{AO } p$ hình số tám nổi. Các electron được phân bố vào các lớp ($K, L, M, N...$) "
            r"và các phân lớp ($s, p, d, f$) tuân theo nguyên lý vững bền, nguyên lý Pauli và quy tắc Hund. Cấu hình electron nguyên tử cho biết sự phân bố electron "
            r"trên các phân lớp thuộc các lớp khác nhau (chú ý ngoại lệ bán bão hòa $\text{Cr}$ có $Z=24: [\text{Ar}]3d^5 4s^1$ và bão hòa $\text{Cu}$ có $Z=29: [\text{Ar}]3d^{10} 4s^1$), "
            r"từ đó xác định được tính chất kim loại ($1, 2, 3$ electron lớp ngoài cùng), phi kim ($5, 6, 7$ electron) hay khí hiếm ($8$ electron, hoặc $2$ với $\text{He}$)."
        ),
        objectives=[
            r"So sánh được mô hình nguyên tử của Rutherford – Bohr với mô hình hiện đại về sự chuyển động của electron trong nguyên tử; nêu được khái niệm orbital nguyên tử ($\text{AO}$) và mô tả hình dạng của $\text{AO } s$ (hình cầu), $\text{AO } p$ (hình số tám nổi).",
            r"Trình bày được khái niệm lớp electron ($K, L, M, N...$), phân lớp electron ($s, p, d, f$) và số lượng $\text{AO}$, số electron tối đa trong một $\text{AO}$ ($2$ electron), trong từng phân lớp ($s^2, p^6, d^{10}, f^{14}$) và trong lớp thứ $n$ ($2n^2$ electron).",
            r"Vận dụng được nguyên lý vững bền, nguyên lý Pauli và quy tắc Hund để viết cấu hình electron đầy đủ, cấu hình thu gọn và biểu diễn theo ô orbital của các nguyên tố có $Z = 1 \to 30$ (kể cả $\text{Cr}$ và $\text{Cu}$).",
            r"Dựa vào số electron ở lớp ngoài cùng của nguyên tử ở trạng thái cơ bản để dự đoán tính chất cơ bản của nguyên tố là kim loại, phi kim hay khí hiếm.",
        ],
        formulas=[
            {
                "name": r"Số lượng orbital ($\text{AO}$) và số electron tối đa trên mỗi phân lớp",
                "formula": r"$s: 1\text{ AO } (2e) \quad ; \quad p: 3\text{ AO } (6e) \quad ; \quad d: 5\text{ AO } (10e) \quad ; \quad f: 7\text{ AO } (14e)$",
                "note": r"Mỗi orbital nguyên tử ($\text{AO}$) chứa tối đa $2$ electron có chiều tự quay ngược nhau ($\uparrow\downarrow$).",
            },
            {
                "name": r"Số orbital ($\text{AO}$) và số electron tối đa trong lớp thứ $n$ ($n \le 4$)",
                "formula": r"$\text{Số AO} = n^2 \quad ; \quad \text{Số electron tối đa} = 2n^2$",
                "note": r"Lớp $K$ ($n=1$): tối đa $2e$; lớp $L$ ($n=2$): tối đa $8e$; lớp $M$ ($n=3$): tối đa $18e$; lớp $N$ ($n=4$): tối đa $32e$.",
            },
            {
                "name": r"Thứ tự mức năng lượng các phân lớp (Nguyên lý vững bền)",
                "formula": r"$1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s\dots$",
                "note": r"Khi viết cấu hình electron, sau khi điền theo mức năng lượng ($4s$ trước $3d$), phải sắp xếp lại theo thứ tự lớp: $\dots 3s^2 3p^6 3d^k 4s^m$.",
            },
            {
                "name": r"Cấu hình electron đặc biệt của Chromium ($\text{Cr}$) và Copper ($\text{Cu}$)",
                "formula": r"$\text{Cr } (Z=24): [\text{Ar}]3d^5 4s^1 \quad ; \quad \text{Cu } (Z=29): [\text{Ar}]3d^{10} 4s^1$",
                "note": r"Do sự chuyển $1$ electron từ $4s$ sang $3d$ để đạt cấu hình bán bão hòa ($3d^5$) hoặc bão hòa ($3d^{10}$) bền vững.",
            },
            {
                "name": r"Xác định tính chất nguyên tố theo số electron lớp ngoài cùng",
                "formula": r"$1, 2, 3e \rightarrow \text{Kim loại} \quad ; \quad 5, 6, 7e \rightarrow \text{Phi kim} \quad ; \quad 8e\text{ (He: }2e\text{)} \rightarrow \text{Khí hiếm}$",
                "note": r"Ngoại lệ: $\text{H}$ ($Z=1$), $\text{He}$ ($Z=2$, khí hiếm) và $\text{B}$ ($Z=5$, phi kim) tuy có $1, 2, 3$ electron lớp ngoài cùng nhưng không phải kim loại.",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Mô hình hiện đại về sự chuyển động của electron và orbital nguyên tử ($\text{AO}$)",
                "content": (
                    r"Trong mô hình hành tinh nguyên tử của Rutherford – Bohr, các electron chuyển động trên những quỹ đạo tròn hay bầu dục xác định xung quanh hạt nhân. "
                    r"Tuy nhiên, theo mô hình hiện đại của cơ học lượng tử, các electron chuyển động rất nhanh trong khu vực không gian xung quanh hạt nhân không theo những quỹ đạo xác định, "
                    r"tạo nên đám mây electron. Orbital nguyên tử (ký hiệu $\text{AO}$) là khu vực không gian xung quanh hạt nhân nguyên tử mà tại đó xác suất tìm thấy electron là lớn nhất (khoảng $90\%$). "
                    r"Dựa vào sự khác nhau về hình dạng và sự định hướng trong không gian, người ta phân loại thành các $\text{AO } s, p, d, f$: "
                    r"$\text{AO } s$ có dạng hình cầu; các $\text{AO } p$ (gồm $3$ orbital $p_x, p_y, p_z$) có dạng hình số tám nổi định hướng dọc theo ba trục tọa độ vuông góc $Ox, Oy, Oz$."
                ),
            },
            {
                "title": r"2. Lớp và phân lớp electron",
                "content": (
                    r"Các electron ở vỏ nguyên tử được sắp xếp thành từng lớp từ gần đến xa hạt nhân theo thứ tự năng lượng tăng dần: "
                    r"lớp thứ nhất ($n = 1$, lớp $K$), lớp thứ hai ($n = 2$, lớp $L$), lớp thứ ba ($n = 3$, lớp $M$), lớp thứ tư ($n = 4$, lớp $N$)... "
                    r"Các electron trên cùng một lớp có năng lượng gần bằng nhau. Mỗi lớp thứ $n$ lại được chia thành $n$ phân lớp, ký hiệu bằng các chữ cái thường $s, p, d, f$. "
                    r"Các electron trên cùng một phân lớp có mức năng lượng bằng nhau. Cụ thể: phân lớp $s$ có $1\text{ AO}$ (chứa tối đa $2$ electron), "
                    r"phân lớp $p$ có $3\text{ AO}$ (chứa tối đa $6$ electron), phân lớp $d$ có $5\text{ AO}$ (chứa tối đa $10$ electron), "
                    r"và phân lớp $f$ có $7\text{ AO}$ (chứa tối đa $14$ electron). Tổng số $\text{AO}$ trong lớp thứ $n$ ($n \le 4$) là $n^2$ và số electron tối đa trong lớp thứ $n$ là $2n^2$."
                ),
            },
            {
                "title": r"3. Nguyên lý vững bền, nguyên lý Pauli và quy tắc Hund",
                "content": (
                    r"Sự phân bố các electron trong nguyên tử ở trạng thái cơ bản tuân theo ba nguyên lý và quy tắc: "
                    r"• Nguyên lý vững bền: Ở trạng thái cơ bản, các electron trong nguyên tử lần lượt chiếm các orbital có mức năng lượng từ thấp đến cao ($1s \to 2s \to 2p \to 3s \to 3p \to 4s \to 3d \to 4p\dots$). "
                    r"• Nguyên lý Pauli: Mỗi orbital nguyên tử ($\text{AO}$) chỉ chứa tối đa $2$ electron và hai electron này phải có chiều tự quay ngược nhau alrededor trục riêng (biểu diễn bằng hai mũi tên ngược chiều $\uparrow\downarrow$, gọi là cặp electron ghép đôi; nếu $\text{AO}$ chỉ có $1$ electron $\uparrow$ thì gọi là electron độc thân). "
                    r"• Quy tắc Hund: Trong cùng một phân lớp chưa bão hòa, các electron sẽ phân bố vào các orbital sao cho số electron độc thân là tối đa và các electron này phải có chiều tự quay giống nhau."
                ),
            },
            {
                "title": r"4. Cấu hình electron nguyên tử và dự đoán tính chất nguyên tố",
                "content": (
                    r"Cấu hình electron nguyên tử biểu diễn sự phân bố electron trên các phân lớp thuộc các lớp khác nhau. "
                    r"Với các nguyên tố có $Z \le 20$, thứ tự mức năng lượng trùng với thứ tự lớp cho đến $4s$ ($\text{K}$ có $Z=19: 1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$; $\text{Ca}$ có $Z=20: [\text{Ar}]4s^2$). "
                    r"Khi $Z > 20$, electron bắt đầu điền vào phân lớp $3d$ sau khi đã điền đầy $4s^2$, rồi viết lại theo thứ tự lớp (ví dụ $\text{Fe}$ có $Z=26: 1s^2 2s^2 2p^6 3s^2 3p^6 3d^6 4s^2$ hay $[\text{Ar}]3d^6 4s^2$). "
                    r"Đặc biệt, ở nguyên tử chromium ($\text{Cr}$, $Z = 24$) và copper ($\text{Cu}$, $Z = 29$), có $1$ electron chuyển từ phân lớp $4s$ sang $3d$ để đạt cấu hình bán bão hòa $3d^5$ và bão hòa $3d^{10}$ bền vững: "
                    r"$\text{Cr}: [\text{Ar}]3d^5 4s^1$ (có $6$ electron độc thân) và $\text{Cu}: [\text{Ar}]3d^{10} 4s^1$ (có $1$ electron độc thân). "
                    r"Dựa vào số electron lớp ngoài cùng: nguyên tử có $1, 2, 3$ electron lớp ngoài cùng thường là kim loại (trừ $\text{H}, \text{He}, \text{B}$); "
                    r"có $5, 6, 7$ electron lớp ngoài cùng thường là phi kim; có $4$ electron lớp ngoài cùng có thể là kim loại hoặc phi kim; có $8$ electron lớp ngoài cùng ($2$ với $\text{He}$) là khí hiếm."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Viết cấu hình electron và xác định số electron độc thân của Fe và Cr",
                "problem": (
                    r"Viết cấu hình electron đầy đủ và thu gọn của nguyên tử iron ($\text{Fe}$, $Z = 26$) và nguyên tử chromium ($\text{Cr}$, $Z = 24$) ở trạng thái cơ bản. "
                    r"Xác định số electron lớp ngoài cùng, số electron độc thân và cho biết các nguyên tố này là kim loại hay phi kim."
                ),
                "solution": (
                    r"• Đối với $\text{Fe}$ ($Z = 26$): Điền theo thứ tự mức năng lượng được $1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^6$, sắp xếp lại theo thứ tự lớp ta có cấu hình đầy đủ là "
                    r"$1s^2 2s^2 2p^6 3s^2 3p^6 3d^6 4s^2$ (thu gọn: $[\text{Ar}]3d^6 4s^2$). Lớp ngoài cùng ($n=4$, phân lớp $4s^2$) có $2$ electron $\Rightarrow \text{Fe}$ là kim loại. "
                    r"Phân lớp $3d^6$ có $5\text{ AO}$, theo quy tắc Hund điền $5$ electron vào $5\text{ AO}$ rồi ghép đôi $1\text{ AO}$, nên nguyên tử $\text{Fe}$ có $4$ electron độc thân. "
                    r"• Đối với $\text{Cr}$ ($Z = 24$): Do hiệu ứng bán bão hòa bền của phân lớp $3d^5$, cấu hình electron đầy đủ của $\text{Cr}$ là "
                    r"$1s^2 2s^2 2p^6 3s^2 3p^6 3d^5 4s^1$ (thu gọn: $[\text{Ar}]3d^5 4s^1$). Lớp ngoài cùng ($4s^1$) có $1$ electron $\Rightarrow \text{Cr}$ là kim loại. "
                    r"Tổng số electron độc thân của $\text{Cr}$ ở trạng thái cơ bản là $5 + 1 = 6$ electron độc thân."
                ),
            },
            {
                "title": r"Ví dụ 2: Xác định nguyên tố từ tổng số electron trên các phân lớp",
                "problem": (
                    r"Nguyên tử của nguyên tố $\text{X}$ ở trạng thái cơ bản có tổng số electron trên các phân lớp $p$ là $11$. "
                    r"Hãy viết cấu hình electron của $\text{X}$, xác định số hiệu nguyên tử $Z$, số electron độc thân và tính chất cơ bản của $\text{X}$."
                ),
                "solution": (
                    r"Theo nguyên lý vững bền, các phân lớp $p$ lần lượt được điền electron là $2p$ và $3p$. "
                    r"Để tổng số electron trên các phân lớp $p$ bằng $11$, phân lớp $2p$ phải đạt bão hòa ($2p^6$) và phân lớp $3p$ có $11 - 6 = 5$ electron ($3p^5$). "
                    r"Do đó cấu hình electron đầy đủ của $\text{X}$ ở trạng thái cơ bản là $1s^2 2s^2 2p^6 3s^2 3p^5$. "
                    r"Tổng số electron của $\text{X}$ là $Z = 2 + 2 + 6 + 2 + 5 = 17$ (nguyên tố chlorine, $\text{Cl}$). "
                    r"Phân lớp $3p^5$ có $3\text{ AO}$ chứa $2$ cặp ghép đôi và $1$ electron độc thân. Vì lớp ngoài cùng ($n=3$) có $2 + 5 = 7$ electron nên $\text{X}$ là phi kim."
                ),
            },
        ],
        key_takeaways=[
            r"Orbital nguyên tử ($\text{AO}$) là vùng không gian quanh hạt nhân có xác suất tìm thấy electron khoảng $90\%$: $\text{AO } s$ hình cầu, $\text{AO } p$ hình số tám nổi.",
            r"Sức chứa tối đa: $1\text{ AO}$ chứa $2e$; phân lớp $s^2, p^6, d^{10}, f^{14}$; lớp thứ $n$ chứa tối đa $2n^2$ electron ($n \le 4$).",
            r"Hai cấu hình ngoại lệ bắt buộc nhớ: $\text{Cr}$ ($Z=24$): $[\text{Ar}]3d^5 4s^1$ ($6e$ độc thân) và $\text{Cu}$ ($Z=29$): $[\text{Ar}]3d^{10} 4s^1$ ($1e$ độc thân).",
            r"Số electron lớp ngoài cùng quyết định tính chất cơ bản: $1, 2, 3e$ là kim loại (trừ $\text{H}, \text{He}, \text{B}$); $5, 6, 7e$ là phi kim; $8e$ ($\text{He}: 2e$) là khí hiếm.",
        ],
        questions=[
            mcq(
                question=r"Theo mô hình hiện đại về nguyên tử, orbital nguyên tử $\text{AO } s$ và $\text{AO } p$ có hình dạng lần lượt là:",
                options=[
                    r"Hình cầu và hình số tám nổi.",
                    r"Hình số tám nổi và hình cầu.",
                    r"Cùng có dạng hình cầu nhưng bán kính khác nhau.",
                    r"Hình bầu dục và hình số tám nổi.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Orbital nguyên tử $\text{AO } s$ có dạng hình cầu, còn các orbital $\text{AO } p$ ($p_x, p_y, p_z$) "
                    r"có dạng hình số tám nổi định hướng theo ba trục tọa độ $Ox, Oy, Oz$."
                ),
            ),
            mcq(
                question=r"Số electron tối đa có thể phân bố trên một orbital nguyên tử ($\text{AO}$) và trên phân lớp $d$ lần lượt là:",
                options=[
                    r"$2$ và $6$.",
                    r"$2$ và $10$.",
                    r"$6$ và $10$.",
                    r"$2$ và $14$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Theo nguyên lý Pauli, mỗi orbital nguyên tử ($\text{AO}$) chứa tối đa $2$ electron có chiều tự quay ngược nhau. "
                    r"Phân lớp $d$ có $5\text{ AO}$ nên chứa tối đa $5 \times 2 = 10$ electron ($d^{10}$)."
                ),
            ),
            mcq(
                question=r"Lớp electron thứ $3$ (lớp $M$, ứng với $n = 3$) có tổng số orbital nguyên tử ($\text{AO}$) và số electron tối đa lần lượt là:",
                options=[
                    r"$3\text{ AO}$ và $6$ electron.",
                    r"$4\text{ AO}$ và $8$ electron.",
                    r"$9\text{ AO}$ và $18$ electron.",
                    r"$16\text{ AO}$ và $32$ electron.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Lớp electron thứ $n = 3$ (lớp $M$) gồm $3$ phân lớp $3s, 3p, 3d$ có tổng số orbital là $n^2 = 3^2 = 9\text{ AO}$ "
                    r"($1 + 3 + 5 = 9\text{ AO}$) và chứa tối đa $2n^2 = 2 \times 3^2 = 18$ electron."
                ),
            ),
            mcq(
                question=r"Nguyên tử của nguyên tố potassium ($\text{K}$, $Z = 19$) ở trạng thái cơ bản có cấu hình electron là:",
                options=[
                    r"$1s^2 2s^2 2p^6 3s^2 3p^6 3d^1$.",
                    r"$1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$.",
                    r"$1s^2 2s^2 2p^6 3s^2 3p^5 4s^2$.",
                    r"$1s^2 2s^2 2p^6 3s^2 3p^7$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Vì phân lớp $4s$ có mức năng lượng thấp hơn phân lớp $3d$, nên sau khi điền đầy phân lớp $3p^6$ ($18$ electron), "
                    r"electron thứ $19$ của $\text{K}$ được điền vào phân lớp $4s$, tạo cấu hình $1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$."
                ),
            ),
            mcq(
                question=r"Ở trạng thái cơ bản, cấu hình electron thu gọn đúng của nguyên tử chromium ($\text{Cr}$, $Z = 24$) và số electron độc thân của nó lần lượt là:",
                options=[
                    r"$[\text{Ar}]3d^4 4s^2$ và $4$ electron độc thân.",
                    r"$[\text{Ar}]3d^5 4s^1$ và $6$ electron độc thân.",
                    r"$[\text{Ar}]3d^5 4s^1$ và $1$ electron độc thân.",
                    r"$[\text{Ar}]3d^6$ và $4$ electron độc thân.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Do cấu hình bán bão hòa $3d^5$ bền vững, ở nguyên tử $\text{Cr}$ ($Z = 24$) có $1$ electron chuyển từ $4s$ sang $3d$, "
                    r"tạo cấu hình $[\text{Ar}]3d^5 4s^1$. Theo quy tắc Hund, $5$ electron trên $3d^5$ và $1$ electron trên $4s^1$ đều là electron độc thân, "
                    r"nên tổng cộng có $5 + 1 = 6$ electron độc thân."
                ),
            ),
            mcq(
                question=(
                    r"Cho cấu hình electron của $4$ nguyên tử ở trạng thái cơ bản: "
                    r"$\text{X}: 1s^2$; $\text{Y}: 1s^2 2s^2 2p^1$; $\text{Z}: 1s^2 2s^2 2p^6 3s^2 3p^1$; $\text{T}: 1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^1$. "
                    r"Các nguyên tử của nguyên tố kim loại là:"
                ),
                options=[
                    r"$\text{X}$, $\text{Y}$ và $\text{Z}$.",
                    r"$\text{Y}$, $\text{Z}$ và $\text{T}$.",
                    r"$\text{Z}$ và $\text{T}$.",
                    r"$\text{X}$, $\text{Z}$ và $\text{T}$.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"• $\text{X}$ ($Z = 2$, $1s^2$) là nguyên tố khí hiếm helium ($\text{He}$). "
                    r"• $\text{Y}$ ($Z = 5$, $1s^2 2s^2 2p^1$) là nguyên tố phi kim boron ($\text{B}$). "
                    r"• $\text{Z}$ ($Z = 13$, $[\text{Ne}]3s^2 3p^1$) là kim loại aluminium ($\text{Al}$, có $3$ electron lớp ngoài cùng). "
                    r"• $\text{T}$ ($Z = 29$, $[\text{Ar}]3d^{10} 4s^1$) là kim loại copper ($\text{Cu}$, có $1$ electron lớp ngoài cùng). "
                    r"Vậy chỉ có $\text{Z}$ và $\text{T}$ là kim loại."
                ),
            ),
            tf4(
                stem=(
                    r"Cho hai nguyên tố phosphorus ($\text{P}$, $Z = 15$) và iron ($\text{Fe}$, $Z = 26$) ở trạng thái cơ bản. "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Cấu hình electron của nguyên tử $\text{P}$ là $1s^2 2s^2 2p^6 3s^2 3p^3$, lớp ngoài cùng có $5$ electron nên $\text{P}$ là phi kim.",
                    r"b) Ở trạng thái cơ bản, nguyên tử $\text{P}$ có $1$ electron độc thân ở phân lớp $3p$.",
                    r"c) Cấu hình electron thu gọn của nguyên tử $\text{Fe}$ là $[\text{Ar}]3d^6 4s^2$, có $4$ electron độc thân ở phân lớp $3d$.",
                    r"d) Khi nguyên tử $\text{Fe}$ nhường $2$ electron để tạo thành ion $\text{Fe}^{2+}$, cấu hình electron của $\text{Fe}^{2+}$ là $[\text{Ar}]3d^4 4s^2$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: $\text{P}$ ($Z = 15$) có cấu hình $1s^2 2s^2 2p^6 3s^2 3p^3$, lớp thứ $3$ (ngoài cùng) có $2 + 3 = 5$ electron nên $\text{P}$ là phi kim. "
                    r"• b) Sai: Theo quy tắc Hund, $3$ electron trên phân lớp $3p^3$ phân bố đều vào $3\text{ AO } p$, nên nguyên tử $\text{P}$ có $3$ electron độc thân (không phải $1$). "
                    r"• c) Đúng: $\text{Fe}$ ($Z = 26$) có cấu hình $[\text{Ar}]3d^6 4s^2$; phân lớp $3d^6$ có $5\text{ AO}$ chứa $1$ cặp ghép đôi và $4$ electron độc thân. "
                    r"• d) Sai: Khi tạo thành cation, nguyên tử nhường electron ở lớp ngoài cùng ($4s$) trước, nên cấu hình electron của $\text{Fe}^{2+}$ là $[\text{Ar}]3d^6$ (không phải $[\text{Ar}]3d^4 4s^2$)."
                ),
            ),
            tf4(
                stem=(
                    r"Xét nguyên tử của nguyên tố copper ($\text{Cu}$, $Z = 29$) và nguyên tử của nguyên tố sulfur ($\text{S}$, $Z = 16$) ở trạng thái cơ bản. "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Cấu hình electron của nguyên tử $\text{Cu}$ ở trạng thái cơ bản là $1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^1$.",
                    r"b) Nguyên tử $\text{Cu}$ ở trạng thái cơ bản có $9$ electron ở phân lớp $3d$ và $2$ electron ở phân lớp $4s$.",
                    r"c) Nguyên tử $\text{S}$ ($Z = 16$) có cấu hình electron là $1s^2 2s^2 2p^6 3s^2 3p^4$ và có $2$ electron độc thân.",
                    r"d) Cả hai nguyên tố $\text{Cu}$ và $\text{S}$ đều là kim loại vì có số electron lớp ngoài cùng nhỏ hơn $4$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Do phân lớp $3d^{10}$ bão hòa bền vững nên $1$ electron từ $4s$ chuyển sang $3d$, tạo cấu hình $1s^2 2s^2 2p^6 3s^2 3p^6 3d^{10} 4s^1$. "
                    r"• b) Sai: Ở trạng thái cơ bản, nguyên tử $\text{Cu}$ có $10$ electron ở phân lớp $3d$ và $1$ electron ở phân lớp $4s$. "
                    r"• c) Đúng: Nguyên tử $\text{S}$ ($Z = 16$) có cấu hình $1s^2 2s^2 2p^6 3s^2 3p^4$; phân lớp $3p^4$ ($3\text{ AO}$) có $1$ cặp electron ghép đôi và $2$ electron độc thân. "
                    r"• d) Sai: $\text{Cu}$ có $1$ electron lớp ngoài cùng ($4s^1$) nên là kim loại, còn $\text{S}$ có $6$ electron lớp ngoài cùng ($3s^2 3p^4$) nên là phi kim."
                ),
            ),
            mcq(
                question=(
                    r"Nguyên tử của nguyên tố $\text{X}$ ở trạng thái cơ bản có tổng số electron trong các phân lớp $s$ bằng $7$. "
                    r"Biết số hiệu nguyên tử của $\text{X}$ thỏa mãn $20 < Z_{\text{X}} < 28$. Số hiệu nguyên tử $Z_{\text{X}}$ và số electron độc thân của $\text{X}$ lần lượt là:"
                ),
                options=[
                    r"$Z_{\text{X}} = 24$ và $6$ electron độc thân.",
                    r"$Z_{\text{X}} = 24$ và $4$ electron độc thân.",
                    r"$Z_{\text{X}} = 19$ và $1$ electron độc thân.",
                    r"$Z_{\text{X}} = 25$ và $5$ electron độc thân.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Tổng số electron trên các phân lớp $s$ bằng $7 \Rightarrow$ các phân lớp $s$ đã điền là $1s^2, 2s^2, 3s^2$ và $4s^1$ ($2 + 2 + 2 + 1 = 7$). "
                    r"Vì $20 < Z_{\text{X}} < 28$ mà phân lớp $4s$ chỉ có $1$ electron ($4s^1$), đây chính là trường hợp bán bão hòa đặc biệt của chromium ($\text{Cr}$): "
                    r"$1s^2 2s^2 2p^6 3s^2 3p^6 3d^5 4s^1$ với $Z_{\text{X}} = 24$ và có $5 + 1 = 6$ electron độc thân."
                ),
            ),
            short(
                question=(
                    r"Ở trạng thái cơ bản, nguyên tử của nguyên tố manganese ($\text{Mn}$, có số hiệu nguyên tử $Z = 25$) "
                    r"có bao nhiêu electron độc thân?"
                ),
                answer=["5"],
                level="vandung",
                solution=(
                    r"Nguyên tử $\text{Mn}$ ($Z = 25$) ở trạng thái cơ bản có cấu hình electron là $1s^2 2s^2 2p^6 3s^2 3p^6 3d^5 4s^2$ (hay $[\text{Ar}]3d^5 4s^2$). "
                    r"Các phân lớp $1s^2, 2s^2, 2p^6, 3s^2, 3p^6, 4s^2$ đều đã bão hòa (toàn bộ electron đã ghép đôi). "
                    r"Riêng phân lớp $3d^5$ có $5$ orbital nguyên tử ($\text{AO } d$); theo quy tắc Hund, $5$ electron phân bố đều vào $5\text{ AO}$, "
                    r"mỗi $\text{AO}$ chứa $1$ electron độc thân. Vậy nguyên tử $\text{Mn}$ có $5$ electron độc thân."
                ),
            ),
        ],
        description="Khám phá mô hình hiện đại về lớp vỏ nguyên tử, khái niệm và hình dạng orbital nguyên tử (AO), cấu trúc lớp và phân lớp electron, ba nguyên lý và quy tắc phân bố electron cùng cách viết cấu hình electron nguyên tử.",
    ),

    # =========================================================================
    # CHƯƠNG 3: BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC VÀ ĐỊNH LUẬT TUẦN HOÀN
    # =========================================================================
    lesson(
        grade=10,
        order=3,
        code="H10-C03",
        title="Chương 3: Bảng tuần hoàn các nguyên tố hóa học và định luật tuần hoàn",
        topic="bang-tuan-hoan",
        summary=(
            r"Bảng tuần hoàn sắp xếp các nguyên tố theo chiều tăng dần của điện tích hạt nhân nguyên tử $Z$, các nguyên tố có cùng số lớp electron "
            r"được xếp vào một hàng (chu kỳ), các nguyên tố có số electron hóa trị như nhau được xếp vào một cột (nhóm $\text{A}$ gồm nguyên tố $s, p$ và nhóm $\text{B}$ gồm nguyên tố $d, f$). "
            r"Trong một chu kỳ từ trái sang phải (theo chiều $Z$ tăng): bán kính nguyên tử $R$ giảm dần, độ âm điện $\chi$ tăng dần, tính kim loại giảm dần, tính phi kim tăng dần, "
            r"tính base của oxide và hydroxide giảm dần còn tính acid của chúng tăng dần. Trong một nhóm $\text{A}$ từ trên xuống dưới, các đại lượng trên biến đổi theo chiều ngược lại. "
            r"Nguyên tố nhóm $n\text{A}$ ($4 \le n \le 7$) có oxide cao nhất dạng $\text{R}_2\text{O}_n$ và hợp chất khí với hydrogen dạng $\text{RH}_{8-n}$."
        ),
        objectives=[
            r"Nêu được nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn và mô tả được cấu tạo bảng tuần hoàn (ô nguyên tố, chu kỳ nhỏ, chu kỳ lớn, nhóm $\text{A}$ và nhóm $\text{B}$).",
            r"Từ cấu hình electron nguyên tử suy ra được vị trí của nguyên tố trong bảng tuần hoàn (số thứ tự ô $= Z$, số thứ tự chu kỳ $=$ số lớp electron, số thứ tự nhóm $=$ số electron hóa trị) và ngược lại.",
            r"Giải thích và vận dụng được quy luật biến đổi tuần hoàn trong một chu kỳ và trong một nhóm $\text{A}$ đối với: bán kính nguyên tử $R$, độ âm điện $\chi$, tính kim loại – tính phi kim, tính acid – base của oxide và hydroxide cao nhất.",
            r"Lập được công thức oxide cao nhất ($\text{R}_2\text{O}_n$) và hợp chất khí với hydrogen ($\text{RH}_{8-n}$), phát biểu được định luật tuần hoàn và giải các bài toán xác định nguyên tố.",
        ],
        formulas=[
            {
                "name": r"Mối liên hệ giữa cấu hình electron và vị trí trong bảng tuần hoàn",
                "formula": r"$\text{Số thứ tự ô} = Z \quad ; \quad \text{Số thứ tự chu kỳ} = \text{Số lớp } e \quad ; \quad \text{Số thứ tự nhóm A} = \text{Số } e\text{ lớp ngoài cùng}$",
                "note": r"Nguyên tố $s, p$ thuộc nhóm $\text{A}$; nguyên tố $d$ (cấu hình $(n-1)d^a ns^b$) thuộc nhóm $\text{B}$ với tổng số electron hóa trị là $a + b$.",
            },
            {
                "name": r"Quy luật biến đổi trong một chu kỳ (theo chiều $Z$ tăng từ trái sang phải)",
                "formula": r"$R \downarrow \quad ; \quad \chi \uparrow \quad ; \quad \text{Tính kim loại} \downarrow \quad ; \quad \text{Tính phi kim} \uparrow \quad ; \quad \text{Tính acid của oxide/hydroxide} \uparrow$",
                "note": r"Do số lớp electron không đổi nhưng điện tích hạt nhân $Z$ tăng, lực hút của hạt nhân với lớp vỏ ngoài cùng mạnh lên.",
            },
            {
                "name": r"Quy luật biến đổi trong một nhóm $\text{A}$ (theo chiều $Z$ tăng từ trên xuống dưới)",
                "formula": r"$R \uparrow \quad ; \quad \chi \downarrow \quad ; \quad \text{Tính kim loại} \uparrow \quad ; \quad \text{Tính phi kim} \downarrow \quad ; \quad \text{Tính base của hydroxide} \uparrow$",
                "note": r"Do số lớp electron tăng lên làm bán kính nguyên tử $R$ tăng nhanh, lực hút của hạt nhân với electron lớp ngoài cùng giảm.",
            },
            {
                "name": r"Công thức oxide cao nhất và hợp chất khí với hydrogen của nguyên tố nhóm $n\text{A}$ ($4 \le n \le 7$)",
                "formula": r"$\text{Oxide cao nhất: }\text{R}_2\text{O}_n \text{ (tối giản nếu } n\text{ chẵn)} \quad ; \quad \text{Hợp chất khí với H: }\text{RH}_{8-n}$",
                "note": r"Tổng hóa trị cao nhất với oxygen ($n$) và hóa trị với hydrogen ($8 - n$) của phi kim nhóm $n\text{A}$ luôn bằng $8$.",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Nguyên tắc sắp xếp và cấu tạo bảng tuần hoàn",
                "content": (
                    r"Các nguyên tố hóa học trong bảng tuần hoàn được sắp xếp theo ba nguyên tắc: "
                    r"(1) Theo chiều tăng dần của điện tích hạt nhân nguyên tử ($Z$); "
                    r"(2) Các nguyên tố có cùng số lớp electron trong nguyên tử được xếp thành một hàng ngang (gọi là chu kỳ); "
                    r"(3) Các nguyên tố có cùng số electron hóa trị trong nguyên tử và có tính chất hóa học tương tự nhau được xếp thành một cột dọc (gọi là nhóm). "
                    r"Bảng tuần hoàn hiện nay gồm $7$ chu kỳ ($3$ chu kỳ nhỏ $1, 2, 3$ và $4$ chu kỳ lớn $4, 5, 6, 7$) và $18$ cột chia thành $8$ nhóm $\text{A}$ (từ $\text{IA}$ đến $\text{VIIIA}$, gồm các nguyên tố $s$ và $p$) "
                    r"cùng $8$ nhóm $\text{B}$ (từ $\text{IB}$ đến $\text{VIIIB}$, gồm các nguyên tố chuyển tiếp $d$ và $f$, trong đó nhóm $\text{VIIIB}$ chiếm $3$ cột $8, 9, 10$)."
                ),
            },
            {
                "title": r"2. Quy luật biến đổi bán kính nguyên tử $R$, độ âm điện $\chi$, tính kim loại và tính phi kim",
                "content": (
                    r"• Bán kính nguyên tử ($R$): Trong một chu kỳ từ trái sang phải ($Z$ tăng), số lớp electron không đổi nhưng điện tích hạt nhân tăng làm lực hút giữa hạt nhân và các electron lớp ngoài cùng tăng, khiến bán kính nguyên tử $R$ giảm dần. "
                    r"Trong một nhóm $\text{A}$ từ trên xuống dưới ($Z$ tăng), số lớp electron tăng lên nên bán kính nguyên tử $R$ tăng dần. "
                    r"• Độ âm điện ($\chi$) đặc trưng cho khả năng hút cặp electron dùng chung của nguyên tử khi tạo thành liên kết hóa học (theo thang Pauling, fluorine $\text{F}$ có độ âm điện lớn nhất $\chi = 3,98$). "
                    r"Tính kim loại đặc trưng bởi khả năng nhường electron, còn tính phi kim đặc trưng bởi khả năng nhận electron. "
                    r"Trong một chu kỳ theo chiều $Z$ tăng: độ âm điện $\chi$ và tính phi kim tăng dần, tính kim loại giảm dần. "
                    r"Trong một nhóm $\text{A}$ theo chiều $Z$ tăng: độ âm điện $\chi$ và tính phi kim giảm dần, tính kim loại tăng dần."
                ),
            },
            {
                "title": r"3. Hóa trị và tính chất của oxide, hydroxide cao nhất (Chu kỳ 3)",
                "content": (
                    r"Khi đi từ trái sang phải trong một chu kỳ, hóa trị cao nhất của các nguyên tố nhóm $\text{A}$ với oxygen tăng lần lượt từ $1$ đến $7$ (trừ $\text{F}$ và khí hiếm), "
                    r"còn hóa trị của các phi kim (từ nhóm $\text{IVA}$ đến $\text{VIIA}$) trong hợp chất khí với hydrogen giảm từ $4$ xuống $1$ theo công thức $\text{RH}_{8-n}$. "
                    r"Xét dãy oxide và hydroxide cao nhất của các nguyên tố chu kỳ 3: "
                    r"$\text{Na}_2\text{O} / \text{NaOH}$ (basic oxide / kiềm mạnh) $\to \text{MgO} / \text{Mg(OH)}_2$ (base yếu hơn) $\to \text{Al}_2\text{O}_3 / \text{Al(OH)}_3$ (chất lưỡng tính) "
                    r"$\to \text{SiO}_2 / \text{H}_2\text{SiO}_3$ (acid yếu) $\to \text{P}_2\text{O}_5 / \text{H}_3\text{PO}_4$ (acid trung bình) $\to \text{SO}_3 / \text{H}_2\text{SO}_4$ (acid mạnh) "
                    r"$\to \text{Cl}_2\text{O}_7 / \text{HClO}_4$ (perchloric acid, acid rất mạnh). Như vậy, trong một chu kỳ theo chiều $Z$ tăng, tính base của oxide và hydroxide giảm dần, đồng thời tính acid của chúng tăng dần."
                ),
            },
            {
                "title": r"4. Định luật tuần hoàn",
                "content": (
                    r"Nguyên nhân của sự biến đổi tuần hoàn tính chất của các nguyên tố là sự biến đổi tuần hoàn cấu hình electron lớp ngoài cùng của nguyên tử khi điện tích hạt nhân tăng dần. "
                    r"Định luật tuần hoàn phát biểu: Tính chất của các nguyên tố và đơn chất, cũng như thành phần và tính chất của các hợp chất tạo nên từ các nguyên tố đó "
                    r"biến đổi tuần hoàn theo chiều tăng của điện tích hạt nhân nguyên tử."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: So sánh bán kính nguyên tử, độ âm điện và tính base của các hydroxide",
                "problem": (
                    r"Cho bốn nguyên tố: sodium (${}_{11}\text{Na}$), magnesium (${}_{12}\text{Mg}$), aluminium (${}_{13}\text{Al}$) và potassium (${}_{19}\text{K}$). "
                    r"Hãy sắp xếp các nguyên tố theo chiều tăng dần bán kính nguyên tử và sắp xếp các hydroxide tương ứng ($\text{NaOH}, \text{Mg(OH)}_2, \text{Al(OH)}_3, \text{KOH}$) theo chiều tăng dần tính base."
                ),
                "solution": (
                    r"Viết cấu hình electron thu gọn để xác định vị trí: "
                    r"${}_{11}\text{Na}$ ($[\text{Ne}]3s^1$, chu kỳ $3$, nhóm $\text{IA}$); ${}_{12}\text{Mg}$ ($[\text{Ne}]3s^2$, chu kỳ $3$, nhóm $\text{IIA}$); "
                    r"${}_{13}\text{Al}$ ($[\text{Ne}]3s^2 3p^1$, chu kỳ $3$, nhóm $\text{IIIA}$); ${}_{19}\text{K}$ ($[\text{Ar}]4s^1$, chu kỳ $4$, nhóm $\text{IA}$). "
                    r"• Trong chu kỳ $3$ theo chiều $Z$ tăng từ $11 \to 13$, bán kính nguyên tử và tính kim loại giảm dần: $R_{\text{Na}} > R_{\text{Mg}} > R_{\text{Al}}$. "
                    r"• Trong nhóm $\text{IA}$ từ trên xuống dưới, $\text{K}$ đứng dưới $\text{Na}$ nên có bán kính và tính kim loại lớn hơn: $R_{\text{K}} > R_{\text{Na}}$. "
                    r"Vậy thứ tự tăng dần bán kính nguyên tử là: $\text{Al} < \text{Mg} < \text{Na} < \text{K}$; "
                    r"và thứ tự tăng dần tính base của các hydroxide tương ứng là: $\text{Al(OH)}_3 < \text{Mg(OH)}_2 < \text{NaOH} < \text{KOH}$."
                ),
            },
            {
                "title": r"Ví dụ 2: Xác định nguyên tố dựa vào công thức oxide cao nhất và hợp chất khí với hydrogen",
                "problem": (
                    r"Nguyên tố $\text{R}$ thuộc nhóm $\text{VIA}$ trong bảng tuần hoàn. Trong hợp chất oxide cao nhất của $\text{R}$, "
                    r"nguyên tố oxygen chiếm $60\%$ về khối lượng. Xác định nguyên tố $\text{R}$, công thức oxide cao nhất, công thức hợp chất khí với hydrogen "
                    r"và tính phần trăm khối lượng của $\text{R}$ trong hợp chất khí với hydrogen (cho $M_{\text{O}} = 16$, $M_{\text{H}} = 1$)."
                ),
                "solution": (
                    r"Vì $\text{R}$ thuộc nhóm $\text{VIA}$ ($n = 6$) nên hóa trị cao nhất của $\text{R}$ với oxygen là $6$, công thức oxide cao nhất là $\text{RO}_3$; "
                    r"hóa trị của $\text{R}$ với hydrogen là $8 - 6 = 2$, công thức hợp chất khí với hydrogen là $\text{RH}_2$ (hay $\text{H}_2\text{R}$). "
                    r"Trong $\text{RO}_3$, oxygen chiếm $60\%$ về khối lượng nên $\text{R}$ chiếm $40\%$: "
                    r"$\dfrac{M_{\text{R}}}{3 \times 16} = \dfrac{40}{60} \Rightarrow M_{\text{R}} = 48 \times \dfrac{2}{3} = 32\text{ g/mol}$. "
                    r"Vậy $\text{R}$ là nguyên tố sulfur ($\text{S}$), oxide cao nhất là $\text{SO}_3$ và hợp chất khí với hydrogen là $\text{H}_2\text{S}$ ($M = 34\text{ g/mol}$). "
                    r"Phần trăm khối lượng của $\text{S}$ trong $\text{H}_2\text{S}$ là $\%m_{\text{S}} = \dfrac{32}{34} \times 100\% \approx 94,12\%$."
                ),
            },
        ],
        key_takeaways=[
            r"Vị trí nguyên tố nhóm $\text{A}$: Số thứ tự ô $= Z$; Chu kỳ $=$ số lớp electron; Nhóm $\text{A}$ $=$ số electron lớp ngoài cùng.",
            r"Trong một chu kỳ ($Z$ tăng): $R$ giảm, $\chi$ tăng, tính kim loại giảm, tính phi kim tăng, tính acid của oxide và hydroxide cao nhất tăng.",
            r"Trong một nhóm $\text{A}$ ($Z$ tăng): $R$ tăng, $\chi$ giảm, tính kim loại tăng, tính phi kim giảm, tính base của hydroxide tăng.",
            r"Nguyên tố nhóm $n\text{A}$ ($4 \le n \le 7$) có oxide cao nhất $\text{R}_2\text{O}_n$ và hợp chất khí với hydrogen $\text{RH}_{8-n}$ (tổng hai hóa trị bằng $8$).",
        ],
        questions=[
            mcq(
                question=r"Trong bảng tuần hoàn các nguyên tố hóa học, các nguyên tố được sắp xếp theo nguyên tắc nào sau đây?",
                options=[
                    r"Theo chiều tăng dần của khối lượng nguyên tử.",
                    r"Theo chiều tăng dần của điện tích hạt nhân nguyên tử.",
                    r"Theo chiều tăng dần của bán kính nguyên tử.",
                    r"Theo chiều tăng dần của số hạt neutron trong hạt nhân.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Nguyên tắc cơ bản đầu tiên để sắp xếp các nguyên tố trong bảng tuần hoàn hiện đại là theo chiều tăng dần "
                    r"của điện tích hạt nhân nguyên tử ($Z$)."
                ),
            ),
            mcq(
                question=r"Nguyên tử của nguyên tố magnesium ($\text{Mg}$) có số hiệu nguyên tử $Z = 12$ ($1s^2 2s^2 2p^6 3s^2$). Vị trí của $\text{Mg}$ trong bảng tuần hoàn là:",
                options=[
                    r"Ô số $12$, chu kỳ $2$, nhóm $\text{IIIA}$.",
                    r"Ô số $12$, chu kỳ $3$, nhóm $\text{IIA}$.",
                    r"Ô số $12$, chu kỳ $3$, nhóm $\text{IIB}$.",
                    r"Ô số $12$, chu kỳ $2$, nhóm $\text{IIA}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Nguyên tử $\text{Mg}$ có $Z = 12 \Rightarrow$ thuộc ô số $12$; có $3$ lớp electron $\Rightarrow$ thuộc chu kỳ $3$; "
                    r"là nguyên tố $s$ có $2$ electron lớp ngoài cùng ($3s^2$) $\Rightarrow$ thuộc nhóm $\text{IIA}$."
                ),
            ),
            mcq(
                question=r"Trong một chu kỳ của bảng tuần hoàn, khi đi từ trái sang phải theo chiều điện tích hạt nhân tăng dần, nhận xét nào sau đây là đúng?",
                options=[
                    r"Bán kính nguyên tử tăng dần, độ âm điện giảm dần.",
                    r"Tính kim loại tăng dần, tính phi kim giảm dần.",
                    r"Bán kính nguyên tử giảm dần, độ âm điện và tính phi kim tăng dần.",
                    r"Tính acid của các oxide và hydroxide cao nhất giảm dần.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Trong một chu kỳ theo chiều $Z$ tăng từ trái sang phải, số lớp electron giữ nguyên nhưng điện tích hạt nhân tăng "
                    r"nên bán kính nguyên tử $R$ giảm dần, độ âm điện $\chi$ tăng dần, tính kim loại giảm dần và tính phi kim tăng dần."
                ),
            ),
            mcq(
                question=r"Nguyên tố $\text{R}$ thuộc nhóm $\text{VA}$ của bảng tuần hoàn. Công thức hợp chất khí với hydrogen và công thức oxide cao nhất của $\text{R}$ lần lượt là:",
                options=[
                    r"$\text{RH}_3$ và $\text{R}_2\text{O}_5$.",
                    r"$\text{RH}_5$ và $\text{R}_2\text{O}_3$.",
                    r"$\text{RH}_2$ và $\text{RO}_3$.",
                    r"$\text{RH}_4$ và $\text{RO}_2$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Nguyên tố $\text{R}$ thuộc nhóm $\text{VA}$ ($n = 5$) có hóa trị cao nhất với oxygen bằng $5$ nên công thức oxide cao nhất là $\text{R}_2\text{O}_5$; "
                    r"hóa trị với hydrogen là $8 - 5 = 3$ nên công thức hợp chất khí với hydrogen là $\text{RH}_3$."
                ),
            ),
            mcq(
                question=(
                    r"Cho các nguyên tố: fluorine (${}_9\text{F}$), oxygen (${}_8\text{O}$), nitrogen (${}_7\text{N}$) và phosphorus (${}_{15}\text{P}$). "
                    r"Thứ tự tăng dần độ âm điện của các nguyên tố trên là:"
                ),
                options=[
                    r"$\text{P} < \text{N} < \text{O} < \text{F}$.",
                    r"$\text{F} < \text{O} < \text{N} < \text{P}$.",
                    r"$\text{N} < \text{P} < \text{O} < \text{F}$.",
                    r"$\text{P} < \text{O} < \text{N} < \text{F}$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"• $\text{N}$ ($Z=7$), $\text{O}$ ($Z=8$), $\text{F}$ ($Z=9$) cùng thuộc chu kỳ $2$; từ trái sang phải độ âm điện tăng dần: $\chi_{\text{N}} < \chi_{\text{O}} < \chi_{\text{F}}$. "
                    r"• $\text{N}$ ($Z=7$, chu kỳ $2$) và $\text{P}$ ($Z=15$, chu kỳ $3$) cùng thuộc nhóm $\text{VA}$; từ trên xuống dưới độ âm điện giảm dần: $\chi_{\text{P}} < \chi_{\text{N}}$. "
                    r"Vậy chiều tăng dần độ âm điện là: $\text{P} < \text{N} < \text{O} < \text{F}$."
                ),
            ),
            mcq(
                question=r"Cho dãy các acid ứng với mức oxi hóa cao nhất của các nguyên tố chu kỳ $3$: $\text{H}_2\text{SiO}_3$, $\text{H}_3\text{PO}_4$, $\text{H}_2\text{SO}_4$, $\text{HClO}_4$. Dãy sắp xếp theo chiều tính acid tăng dần là:",
                options=[
                    r"$\text{HClO}_4 < \text{H}_2\text{SO}_4 < \text{H}_3\text{PO}_4 < \text{H}_2\text{SiO}_3$.",
                    r"$\text{H}_2\text{SiO}_3 < \text{H}_3\text{PO}_4 < \text{H}_2\text{SO}_4 < \text{HClO}_4$.",
                    r"$\text{H}_3\text{PO}_4 < \text{H}_2\text{SiO}_3 < \text{H}_2\text{SO}_4 < \text{HClO}_4$.",
                    r"$\text{H}_2\text{SiO}_3 < \text{H}_3\text{PO}_4 < \text{HClO}_4 < \text{H}_2\text{SO}_4$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Trong chu kỳ $3$, khi đi từ trái sang phải theo thứ tự $\text{Si}$ ($Z=14$) $\to \text{P}$ ($Z=15$) $\to \text{S}$ ($Z=16$) $\to \text{Cl}$ ($Z=17$), "
                    r"tính phi kim của nguyên tố tăng dần nên tính acid của các hydroxide (acid có oxygen) ứng với hóa trị cao nhất tăng dần: "
                    r"$\text{H}_2\text{SiO}_3 < \text{H}_3\text{PO}_4 < \text{H}_2\text{SO}_4 < \text{HClO}_4$."
                ),
            ),
            tf4(
                stem=(
                    r"Cho bốn nguyên tố thuộc chu kỳ $3$ và chu kỳ $4$ của bảng tuần hoàn: "
                    r"${}_{11}\text{Na}$, ${}_{12}\text{Mg}$, ${}_{13}\text{Al}$ và ${}_{19}\text{K}$. Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Ba nguyên tố ${}_{11}\text{Na}$, ${}_{12}\text{Mg}$ và ${}_{13}\text{Al}$ cùng thuộc chu kỳ $3$ vì nguyên tử của chúng đều có $3$ lớp electron.",
                    r"b) Bán kính nguyên tử của các nguyên tố biến đổi theo thứ tự: $R_{\text{Na}} < R_{\text{Mg}} < R_{\text{Al}}$.",
                    r"c) Trong bốn nguyên tố trên, potassium (${}_{19}\text{K}$) là nguyên tố có tính kim loại mạnh nhất và $\text{KOH}$ có tính base mạnh nhất.",
                    r"d) Oxide và hydroxide của aluminium ($\text{Al}_2\text{O}_3$ và $\text{Al(OH)}_3$) chỉ có tính base, không tác dụng được với dung dịch kiềm mạnh.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: ${}_{11}\text{Na}$ ($[\text{Ne}]3s^1$), ${}_{12}\text{Mg}$ ($[\text{Ne}]3s^2$), ${}_{13}\text{Al}$ ($[\text{Ne}]3s^2 3p^1$) đều có $3$ lớp electron nên cùng thuộc chu kỳ $3$. "
                    r"• b) Sai: Trong cùng chu kỳ $3$ theo chiều $Z$ tăng từ $11 \to 13$, bán kính nguyên tử giảm dần nên $R_{\text{Na}} > R_{\text{Mg}} > R_{\text{Al}}$. "
                    r"• c) Đúng: Tính kim loại tăng theo thứ tự $\text{Al} < \text{Mg} < \text{Na} < \text{K}$, nên $\text{K}$ có tính kim loại mạnh nhất và $\text{KOH}$ là base mạnh nhất. "
                    r"• d) Sai: $\text{Al}_2\text{O}_3$ và $\text{Al(OH)}_3$ là các hợp chất lưỡng tính, vừa tác dụng với dung dịch acid mạnh vừa tác dụng với dung dịch kiềm mạnh như $\text{NaOH}$."
                ),
            ),
            tf4(
                stem=(
                    r"Cho các hạt vi mô (nguyên tử và ion) có cùng cấu hình electron $1s^2 2s^2 2p^6$ ($10$ electron): "
                    r"$\text{O}^{2-}$ ($Z = 8$), $\text{F}^-$ ($Z = 9$), $\text{Ne}$ ($Z = 10$), $\text{Na}^+$ ($Z = 11$) và $\text{Mg}^{2+}$ ($Z = 12$). "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Cả $5$ hạt vi mô trên đều có $2$ lớp electron với tổng cộng $10$ electron ở lớp vỏ.",
                    r"b) Ion $\text{Mg}^{2+}$ có bán kính lớn hơn ion $\text{O}^{2-}$ vì hạt nhân của $\text{Mg}^{2+}$ có điện tích lớn hơn.",
                    r"c) Thứ tự giảm dần bán kính của các hạt là: $R_{\text{O}^{2-}} > R_{\text{F}^-} > R_{\text{Ne}} > R_{\text{Na}^+} > R_{\text{Mg}^{2+}}$.",
                    r"d) Hai nguyên tố $\text{Na}$ ($Z = 11$) và $\text{F}$ ($Z = 9$) thuộc cùng một chu kỳ trong bảng tuần hoàn.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: $\text{O}^{2-}$ ($8+2=10e$), $\text{F}^-$ ($9+1=10e$), $\text{Ne}$ ($10e$), $\text{Na}^+$ ($11-1=10e$), $\text{Mg}^{2+}$ ($12-2=10e$) đều có cấu hình $1s^2 2s^2 2p^6$ ($2$ lớp, $10$ electron). "
                    r"• b) Sai: Với các hạt có cùng số electron ($10e$), điện tích hạt nhân $Z$ càng lớn thì lực hút của hạt nhân với lớp vỏ càng mạnh làm bán kính càng nhỏ, nên $R_{\text{Mg}^{2+}} < R_{\text{O}^{2-}}$. "
                    r"• c) Đúng: Theo chiều tăng điện tích hạt nhân $Z$ từ $8 \to 12$, bán kính các hạt đẳng electron giảm dần: $R_{\text{O}^{2-}} > R_{\text{F}^-} > R_{\text{Ne}} > R_{\text{Na}^+} > R_{\text{Mg}^{2+}}$. "
                    r"• d) Sai: Nguyên tử $\text{F}$ ($Z=9$, $1s^2 2s^2 2p^5$) thuộc chu kỳ $2$, còn nguyên tử $\text{Na}$ ($Z=11$, $[\text{Ne}]3s^1$) thuộc chu kỳ $3$."
                ),
            ),
            mcq(
                question=(
                    r"Hợp chất khí với hydrogen của một nguyên tố $\text{R}$ có công thức là $\text{RH}_4$. "
                    r"Trong công thức oxide cao nhất của $\text{R}$, nguyên tố oxygen chiếm $53,33\%$ về khối lượng (cho $M_{\text{O}} = 16$). "
                    r"Nguyên tử khối của nguyên tố $\text{R}$ và tên nguyên tố $\text{R}$ là:"
                ),
                options=[
                    r"$12$ (Carbon, $\text{C}$).",
                    r"$28$ (Silicon, $\text{Si}$).",
                    r"$32$ (Sulfur, $\text{S}$).",
                    r"$14$ (Nitrogen, $\text{N}$).",
                ],
                answer="B",
                level="vandung",
                solution=(
                    r"Hợp chất khí với hydrogen có dạng $\text{RH}_4 \Rightarrow 8 - n = 4 \Rightarrow n = 4$ ($\text{R}$ thuộc nhóm $\text{IVA}$). "
                    r"Do đó công thức oxide cao nhất của $\text{R}$ là $\text{RO}_2$ (chứa $2$ nguyên tử $\text{O}$, có khối lượng $2 \times 16 = 32\text{ g/mol}$). "
                    r"Theo đề bài, oxygen chiếm $53,33\%$ về khối lượng trong $\text{RO}_2$: "
                    r"$\dfrac{32}{M_{\text{R}} + 32} \times 100\% = 53,33\% \Rightarrow M_{\text{R}} + 32 \approx 60 \Rightarrow M_{\text{R}} = 28\text{ g/mol}$ (Silicon, $\text{Si}$)."
                ),
            ),
            short(
                question=(
                    r"Hai nguyên tố $\text{A}$ và $\text{B}$ đứng kế tiếp nhau trong cùng một chu kỳ của bảng tuần hoàn và có tổng số hiệu nguyên tử là $25$. "
                    r"Hãy xác định số hiệu nguyên tử $Z$ của nguyên tố có tính kim loại yếu hơn trong hai nguyên tố đó."
                ),
                answer=["13"],
                level="vandung",
                solution=(
                    r"Gọi số hiệu nguyên tử của hai nguyên tố kế tiếp nhau trong cùng một chu kỳ là $Z_{\text{A}}$ và $Z_{\text{B}}$ (giả sử $Z_{\text{A}} < Z_{\text{B}}$, suy ra $Z_{\text{B}} - Z_{\text{A}} = 1$). "
                    r"Ta có hệ phương trình: $Z_{\text{A}} + Z_{\text{B}} = 25$ và $Z_{\text{B}} - Z_{\text{A}} = 1 \Rightarrow Z_{\text{A}} = 12$ ($\text{Mg}$) và $Z_{\text{B}} = 13$ ($\text{Al}$). "
                    r"Cả hai nguyên tố đều thuộc chu kỳ $3$; theo chiều tăng điện tích hạt nhân từ $\text{Mg}$ ($Z=12$) sang $\text{Al}$ ($Z=13$), tính kim loại giảm dần. "
                    r"Vậy nguyên tố có tính kim loại yếu hơn có số hiệu nguyên tử là $13$."
                ),
            ),
        ],
        description="Nghiên cứu nguyên tắc sắp xếp và cấu tạo bảng tuần hoàn các nguyên tố hóa học, quy luật biến đổi tuần hoàn bán kính nguyên tử, độ âm điện, tính kim loại - phi kim, tính acid - base của oxide và hydroxide cùng định luật tuần hoàn.",
    ),

    # =========================================================================
    # CHƯƠNG 4: LIÊN KẾT HÓA HỌC (QUY TẮC OCTET, LIÊN KẾT ION, CỘNG HÓA TRỊ, HYDROGEN)
    # =========================================================================
    lesson(
        grade=10,
        order=4,
        code="H10-C04",
        title="Chương 4: Liên kết hóa học (Quy tắc Octet, Liên kết ion, Cộng hóa trị, Hydrogen)",
        topic="lien-ket-hoa-hoc",
        summary=(
            r"Theo quy tắc octet, khi hình thành liên kết hóa học, các nguyên tử của các nguyên tố nhóm $\text{A}$ có xu hướng nhường, nhận hoặc góp chung electron "
            r"để đạt tới cấu hình bền vững có $8$ electron ở lớp ngoài cùng của khí hiếm (hoặc $2$ electron như $\text{He}$). Liên kết ion được hình thành bởi lực hút tĩnh điện "
            r"giữa các cation và anion (thường có hiệu độ âm điện $\Delta\chi \ge 1,7$). Liên kết cộng hóa trị được hình thành bằng một hay nhiều cặp electron dùng chung, "
            r"gồm liên kết cộng hóa trị không phân cực ($0 \le \Delta\chi < 0,4$), phân cực ($0,4 \le \Delta\chi < 1,7$) và liên kết cho – nhận; về kiểu xen phủ orbital có liên kết $\sigma$ "
            r"(xen phủ trục, bền) và liên kết $\pi$ (xen phủ bên, kém bền hơn). Ngoài ra, giữa các phân tử còn có liên kết hydrogen ($\dots\text{X}-\text{H}\cdots\text{Y}$ với $\text{X}, \text{Y} \in \{\text{F}, \text{O}, \text{N}\}$) "
            r"và tương tác van der Waals quyết định nhiệt độ nóng chảy, nhiệt độ sôi và độ tan."
        ),
        objectives=[
            r"Trình bày và vận dụng được quy tắc octet để giải thích sự hình thành liên kết trong các phân tử đơn chất và hợp chất của các nguyên tố nhóm $\text{A}$.",
            r"Trình bày được sự hình thành cation, anion, bản chất của liên kết ion, cấu tạo mạng tinh thể ion (như tinh thể $\text{NaCl}$) và giải thích vì sao hợp chất ion thường là chất rắn có nhiệt độ nóng chảy cao, dẫn điện khi nóng chảy hoặc tan trong nước.",
            r"Trình bày được sự hình thành liên kết cộng hóa trị (không phân cực, phân cực, liên kết cho – nhận), viết được công thức electron, công thức Lewis và công thức cấu tạo của các phân tử phổ biến.",
            r"Phân biệt được liên kết $\sigma$ và liên kết $\pi$, nêu được ý nghĩa của năng lượng liên kết $E_{\text{b}}$, phân loại liên kết dựa vào hiệu độ âm điện $\Delta\chi$, và giải thích được ảnh hưởng của liên kết hydrogen cùng tương tác van der Waals đến nhiệt độ sôi và độ tan.",
        ],
        formulas=[
            {
                "name": r"Hiệu độ âm điện và phân loại tương đối các loại liên kết hóa học",
                "formula": r"$\Delta\chi = |\chi_{\text{A}} - \chi_{\text{B}}| \quad : \quad [0; 0,4)\text{ CHT không cực} \;;\; [0,4; 1,7)\text{ CHT phân cực} \;;\; \ge 1,7\text{ Liên kết ion}$",
                "note": r"Quy tắc hiệu độ âm điện mang tính tương đối (ví dụ $\text{HF}$ có $\Delta\chi = 1,78$ nhưng vẫn là hợp chất cộng hóa trị phân cực mạnh).",
            },
            {
                "name": r"Số liên kết sigma ($\sigma$) và liên kết pi ($\pi$) trong các loại liên kết cộng hóa trị",
                "formula": r"$\text{Liên kết đơn } (-): 1\sigma \quad ; \quad \text{Liên kết đôi } (=): 1\sigma + 1\pi \quad ; \quad \text{Liên kết ba } (\equiv): 1\sigma + 2\pi$",
                "note": r"Liên kết $\sigma$ hình thành do sự xen phủ trục của các $\text{AO}$ nên bền vững hơn liên kết $\pi$ (xen phủ bên).",
            },
            {
                "name": r"Quá trình hình thành ion và liên kết ion giữa kim loại và phi kim",
                "formula": r"$\text{M} \rightarrow \text{M}^{n+} + ne \quad ; \quad \text{X} + me \rightarrow \text{X}^{m-} \quad ; \quad m\text{M}^{n+} + n\text{X}^{m-} \rightarrow \text{M}_m\text{X}_n$",
                "note": r"Ví dụ: $2\text{Na} + \text{Cl}_2 \rightarrow 2\text{NaCl}$ (hình thành từ lực hút tĩnh điện giữa $\text{Na}^+$ và $\text{Cl}^-$).",
            },
            {
                "name": r"Điều kiện tạo thành liên kết hydrogen liên phân tử",
                "formula": r"$\dots\text{X}-\text{H}\cdots\text{Y}-\quad (\text{với } \text{X}, \text{Y} \in \{\text{F}, \text{O}, \text{N}\})$",
                "note": r"Nguyên tử $\text{H}$ liên kết cộng hóa trị phân cực mạnh với $\text{X}$ ($\text{F}, \text{O}, \text{N}$) hút cặp electron chưa liên kết trên $\text{Y}$ ($\text{F}, \text{O}, \text{N}$).",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Quy tắc Octet (Quy tắc bát tử)",
                "content": (
                    r"Trong quá trình hình thành liên kết hóa học, nguyên tử của các nguyên tố nhóm $\text{A}$ có xu hướng nhường, nhận hoặc góp chung electron "
                    r"để đạt tới cấu hình electron bền vững của nguyên tử khí hiếm gần nhất với $8$ electron ở lớp ngoài cùng (hoặc $2$ electron ở lớp ngoài cùng như khí hiếm $\text{He}$). "
                    r"Cụ thể: nguyên tử kim loại ($1, 2, 3$ electron lớp ngoài cùng) có xu hướng nhường electron; nguyên tử phi kim ($5, 6, 7$ electron lớp ngoài cùng) "
                    r"có xu hướng nhận thêm electron khi gặp kim loại hoặc góp chung electron khi kết hợp với nhau. Một số phân tử có thể không tuân theo quy tắc octet như $\text{NO}$, $\text{BH}_3$, $\text{PCl}_5$, $\text{SF}_6$."
                ),
            },
            {
                "title": r"2. Liên kết ion và tinh thể ion",
                "content": (
                    r"Khi nguyên tử kim loại nhường electron sẽ trở thành ion dương (cation), còn nguyên tử phi kim nhận electron sẽ trở thành ion âm (anion). "
                    r"Liên kết ion là liên kết được hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu (thường hình thành giữa kim loại điển hình và phi kim điển hình, có hiệu độ âm điện $\Delta\chi \ge 1,7$). "
                    r"Ở điều kiện thường, các hợp chất ion (như $\text{NaCl}, \text{MgO}, \text{CaCl}_2$) tồn tại ở dạng tinh thể ion bền vững, trong đó các cation và anion sắp xếp luân phiên đều đặn tại các nút mạng. "
                    r"Do lực hút tĩnh điện giữa các ion rất lớn nên hợp chất ion là chất rắn, khó nóng chảy, khó bay hơi, tan nhiều trong nước; ở trạng thái rắn không dẫn điện nhưng khi nóng chảy hoặc hòa tan trong nước thì phân li thành các ion tự do nên dẫn điện tốt."
                ),
            },
            {
                "title": r"3. Liên kết cộng hóa trị, liên kết $\sigma$, liên kết $\pi$ và năng lượng liên kết $E_{\text{b}}$",
                "content": (
                    r"Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng một hay nhiều cặp electron dùng chung. "
                    r"Nếu cặp electron chung không bị hút lệch về phía nguyên tử nào ($0 \le \Delta\chi < 0,4$, như trong $\text{H}_2, \text{Cl}_2, \text{O}_2, \text{N}_2, \text{CH}_4$) thì gọi là liên kết cộng hóa trị không phân cực; "
                    r"nếu cặp electron chung bị hút lệch về phía nguyên tử có độ âm điện lớn hơn ($0,4 \le \Delta\chi < 1,7$, như trong $\text{HCl}, \text{H}_2\text{O}, \text{NH}_3, \text{CO}_2$) thì gọi là liên kết cộng hóa trị phân cực. "
                    r"Trường hợp cặp electron dùng chung chỉ do một nguyên tử đóng góp thì gọi là liên kết cho – nhận (biểu diễn bằng mũi tên $\rightarrow$, ví dụ trong $\text{NH}_4^+$, $\text{SO}_2$, $\text{HNO}_3$, $\text{CO}$). "
                    r"Xét về sự xen phủ orbital: liên kết $\sigma$ hình thành do sự xen phủ trục của hai $\text{AO}$ (vùng xen phủ nằm trên đường nối tâm hai hạt nhân, rất bền); "
                    r"liên kết $\pi$ hình thành do sự xen phủ bên của hai $\text{AO } p$ song song (kém bền hơn liên kết $\sigma$). Liên kết đơn gồm $1\sigma$, liên kết đôi gồm $1\sigma + 1\pi$, liên kết ba gồm $1\sigma + 2\pi$. "
                    r"Năng lượng liên kết ($E_{\text{b}}$, đơn vị $\text{kJ/mol}$) là năng lượng cần thiết để phá vỡ $1\text{ mol}$ liên kết xác định ở thể khí tại điều kiện chuẩn; $E_{\text{b}}$ càng lớn thì liên kết càng bền."
                ),
            },
            {
                "title": r"4. Liên kết hydrogen và tương tác van der Waals",
                "content": (
                    r"• Liên kết hydrogen là một loại liên kết yếu được hình thành giữa nguyên tử $\text{H}$ (đã liên kết với một nguyên tử có độ âm điện lớn như $\text{F}, \text{O}, \text{N}$) "
                    r"với một nguyên tử khác cũng có độ âm điện lớn ($\text{F}, \text{O}, \text{N}$) còn cặp electron hóa trị chưa tham gia liên kết, ký hiệu bằng dấu ba chấm ($\dots\text{O}-\text{H}\cdots\text{O}$). "
                    r"Các hợp chất tạo được liên kết hydrogen liên phân tử (như $\text{H}_2\text{O}, \text{HF}, \text{NH}_3, \text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{COOH}$) có nhiệt độ sôi cao hơn hẳn so với các chất có phân tử khối tương đương nhưng không có liên kết hydrogen, đồng thời tạo liên kết hydrogen với nước nên tan tốt trong nước. "
                    r"• Tương tác van der Waals là lực tương tác tĩnh điện rất yếu giữa các phân tử (do sự xuất hiện các lưỡng cực tạm thời và lưỡng cực cảm ứng). "
                    r"Khi kích thước và khối lượng phân tử (tổng số electron) tăng lên thì tương tác van der Waals tăng, làm nhiệt độ nóng chảy và nhiệt độ sôi tăng dần (ví dụ dãy $\text{F}_2 < \text{Cl}_2 < \text{Br}_2 < \text{I}_2$ hoặc $\text{He} < \text{Ne} < \text{Ar} < \text{Kr} < \text{Xe}$)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Xác định loại liên kết và đếm số liên kết sigma ($\sigma$), liên kết pi ($\pi$)",
                "problem": (
                    r"Xét các phân tử: nitrogen ($\text{N}_2$), carbon dioxide ($\text{CO}_2$) và ethylene ($\text{C}_2\text{H}_4$, công thức cấu tạo $\text{CH}_2=\text{CH}_2$). "
                    r"Hãy viết công thức cấu tạo của $\text{N}_2$, $\text{CO}_2$ và xác định số liên kết $\sigma$, số liên kết $\pi$ trong mỗi phân tử $\text{N}_2$, $\text{CO}_2$, $\text{C}_2\text{H}_4$."
                ),
                "solution": (
                    r"• Phân tử $\text{N}_2$: Mỗi nguyên tử $\text{N}$ ($Z=7$, nhóm $\text{VA}$) có $5$ electron hóa trị, cần góp chung $3$ electron để đạt octet $\Rightarrow$ công thức cấu tạo là $\text{N}\equiv\text{N}$ (liên kết ba), gồm $1$ liên kết $\sigma$ và $2$ liên kết $\pi$. "
                    r"• Phân tử $\text{CO}_2$: Nguyên tử $\text{C}$ (nhóm $\text{IVA}$) góp chung $2$ electron với mỗi nguyên tử $\text{O}$ (nhóm $\text{VIA}$) $\Rightarrow$ công thức cấu tạo là $\text{O}=\text{C}=\text{O}$ ($2$ liên kết đôi), gồm $2$ liên kết $\sigma$ và $2$ liên kết $\pi$. "
                    r"• Phân tử $\text{C}_2\text{H}_4$ ($\text{H}_2\text{C}=\text{CH}_2$): Có $4$ liên kết đơn $\text{C}-\text{H}$ ($4\sigma$) và $1$ liên kết đôi $\text{C}=\text{C}$ ($1\sigma + 1\pi$) $\Rightarrow$ tổng cộng có $5$ liên kết $\sigma$ và $1$ liên kết $\pi$."
                ),
            },
            {
                "title": r"Ví dụ 2: Giải thích sự khác biệt về nhiệt độ sôi dựa vào liên kết hydrogen",
                "problem": (
                    r"Cho ba chất: nước ($\text{H}_2\text{O}$, $M = 18\text{ g/mol}$), hydrogen sulfide ($\text{H}_2\text{S}$, $M = 34\text{ g/mol}$) và methane ($\text{CH}_4$, $M = 16\text{ g/mol}$). "
                    r"Hãy sắp xếp ba chất trên theo chiều tăng dần nhiệt độ sôi và giải thích."
                ),
                "solution": (
                    r"• Giữa các phân tử $\text{H}_2\text{O}$ có liên kết hydrogen liên phân tử bền vững ($\dots\text{O}-\text{H}\cdots\text{O}$) vì nguyên tử $\text{O}$ có độ âm điện rất lớn ($\chi = 3,44$) và còn cặp electron hóa trị chưa liên kết, nên $\text{H}_2\text{O}$ có nhiệt độ sôi cao nhất ($100^\circ\text{C}$). "
                    r"• Hai chất $\text{CH}_4$ và $\text{H}_2\text{S}$ không tạo được liên kết hydrogen liên phân tử mà chỉ có tương tác van der Waals. Vì $\text{H}_2\text{S}$ phân cực hơn và có phân tử khối lớn hơn $\text{CH}_4$ ($34 > 16$) nên tương tác van der Waals giữa các phân tử $\text{H}_2\text{S}$ mạnh hơn $\text{CH}_4$. "
                    r"Vậy chiều tăng dần nhiệt độ sôi là: $\text{CH}_4 < \text{H}_2\text{S} < \text{H}_2\text{O}$."
                ),
            },
        ],
        key_takeaways=[
            r"Quy tắc octet: Nguyên tử các nguyên tố nhóm $\text{A}$ nhường, nhận hoặc góp chung electron để đạt $8$ electron lớp ngoài cùng ($2$ với $\text{He}$).",
            r"Liên kết ion hình thành do lực hút tĩnh điện giữa cation và anion ($\Delta\chi \ge 1,7$); liên kết cộng hóa trị hình thành bằng cặp electron dùng chung.",
            r"Liên kết đơn ($-$) gồm $1\sigma$; liên kết đôi ($=$) gồm $1\sigma + 1\pi$; liên kết ba ($\equiv$) gồm $1\sigma + 2\pi$.",
            r"Liên kết hydrogen ($\dots\text{X}-\text{H}\cdots\text{Y}$ với $\text{X}, \text{Y} \in \{\text{F}, \text{O}, \text{N}\}$) làm tăng nhiệt độ sôi và độ tan trong nước; tương tác van der Waals tăng theo khối lượng và kích thước phân tử.",
        ],
        questions=[
            mcq(
                question=r"Theo quy tắc octet, khi tham gia hình thành liên kết hóa học, nguyên tử sodium ($\text{Na}$, $Z = 11$) có xu hướng:",
                options=[
                    r"Nhận thêm $1$ electron để đạt cấu hình electron của khí hiếm $\text{Ar}$.",
                    r"Nhường đi $1$ electron để đạt cấu hình electron bền vững của khí hiếm $\text{Ne}$.",
                    r"Nhường đi $2$ electron để đạt cấu hình electron của khí hiếm $\text{Ne}$.",
                    r"Nhận thêm $7$ electron để đạt $8$ electron ở lớp ngoài cùng.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Nguyên tử $\text{Na}$ ($Z = 11$) có cấu hình electron là $1s^2 2s^2 2p^6 3s^1$ ($1$ electron ở lớp ngoài cùng). "
                    r"Khi hình thành liên kết, $\text{Na}$ dễ dàng nhường $1$ electron để tạo cation $\text{Na}^+$ có cấu hình bền vững $1s^2 2s^2 2p^6$ của khí hiếm $\text{Ne}$."
                ),
            ),
            mcq(
                question=r"Hợp chất nào sau đây có liên kết ion trong phân tử?",
                options=[
                    r"$\text{HCl}$.",
                    r"$\text{NH}_3$.",
                    r"$\text{KCl}$.",
                    r"$\text{H}_2\text{O}$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Potassium chloride ($\text{KCl}$) được tạo thành từ kim loại kiềm điển hình $\text{K}$ và phi kim điển hình $\text{Cl}$ "
                    r"bằng lực hút tĩnh điện giữa ion $\text{K}^+$ và ion $\text{Cl}^-$, nên có liên kết ion. Các chất $\text{HCl}, \text{NH}_3, \text{H}_2\text{O}$ chứa liên kết cộng hóa trị phân cực."
                ),
            ),
            mcq(
                question=r"Trong phân tử nitrogen ($\text{N}_2$, có công thức cấu tạo $\text{N}\equiv\text{N}$), liên kết giữa hai nguyên tử nitrogen gồm:",
                options=[
                    r"$3$ liên kết $\sigma$.",
                    r"$2$ liên kết $\sigma$ và $1$ liên kết $\pi$.",
                    r"$1$ liên kết $\sigma$ và $2$ liên kết $\pi$.",
                    r"$3$ liên kết $\pi$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Liên kết ba ($\text{N}\equiv\text{N}$) trong phân tử $\text{N}_2$ được tạo bởi $3$ cặp electron dùng chung, "
                    r"bao gồm $1$ liên kết $\sigma$ bền vững (xen phủ trục) và $2$ liên kết $\pi$ (xen phủ bên)."
                ),
            ),
            mcq(
                question=r"Chất nào sau đây có khả năng tạo liên kết hydrogen liên phân tử giữa các phân tử cùng loại?",
                options=[
                    r"$\text{CH}_4$.",
                    r"$\text{H}_2\text{S}$.",
                    r"$\text{C}_2\text{H}_5\text{OH}$.",
                    r"$\text{CH}_3\text{OCH}_3$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Phân tử ethanol ($\text{C}_2\text{H}_5\text{OH}$) có chứa nhóm $-\text{O}-\text{H}$ (nguyên tử $\text{H}$ liên kết trực tiếp với nguyên tử $\text{O}$ có độ âm điện lớn), "
                    r"nên tạo được liên kết hydrogen liên phân tử giữa các phân tử $\text{C}_2\text{H}_5\text{OH}$."
                ),
            ),
            mcq(
                question=(
                    r"Cho độ âm điện của một số nguyên tố theo thang Pauling: $\chi_{\text{H}} = 2,20$; $\chi_{\text{C}} = 2,55$; "
                    r"$\chi_{\text{Cl}} = 3,16$; $\chi_{\text{Na}} = 0,93$. Dựa vào hiệu độ âm điện $\Delta\chi$, loại liên kết trong các phân tử "
                    r"$\text{CH}_4$, $\text{HCl}$ và $\text{NaCl}$ lần lượt là:"
                ),
                options=[
                    r"Cộng hóa trị không phân cực, cộng hóa trị phân cực và liên kết ion.",
                    r"Cộng hóa trị phân cực, cộng hóa trị không phân cực và liên kết ion.",
                    r"Cộng hóa trị không phân cực, liên kết ion và cộng hóa trị phân cực.",
                    r"Đều là liên kết cộng hóa trị phân cực.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Tính hiệu độ âm điện $\Delta\chi$: "
                    r"• Trong $\text{CH}_4$: $\Delta\chi = |2,55 - 2,20| = 0,35 < 0,4 \Rightarrow$ liên kết cộng hóa trị không phân cực. "
                    r"• Trong $\text{HCl}$: $\Delta\chi = |3,16 - 2,20| = 0,96 \in [0,4; 1,7) \Rightarrow$ liên kết cộng hóa trị phân cực. "
                    r"• Trong $\text{NaCl}$: $\Delta\chi = |3,16 - 0,93| = 2,23 \ge 1,7 \Rightarrow$ liên kết ion."
                ),
            ),
            mcq(
                question=r"Vì sao ở điều kiện thường, đơn chất $\text{F}_2$ và $\text{Cl}_2$ là chất khí, $\text{Br}_2$ là chất lỏng, còn $\text{I}_2$ là chất rắn (nhiệt độ sôi tăng dần từ $\text{F}_2$ đến $\text{I}_2$)?",
                options=[
                    r"Do độ bền liên kết cộng hóa trị trong phân tử tăng dần từ $\text{F}_2$ đến $\text{I}_2$.",
                    r"Do giữa các phân tử $\text{I}_2$ có liên kết hydrogen mạnh hơn các phân tử còn lại.",
                    r"Do khối lượng phân tử và kích thước nguyên tử tăng dần từ $\text{F}_2$ đến $\text{I}_2$ làm tương tác van der Waals giữa các phân tử tăng dần.",
                    r"Do độ âm điện của các nguyên tố tăng dần từ $\text{F}$ đến $\text{I}$.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"Các phân tử $\text{F}_2, \text{Cl}_2, \text{Br}_2, \text{I}_2$ đều là các phân tử hai nguyên tử không phân cực và không có liên kết hydrogen. "
                    r"Đi từ $\text{F}_2$ đến $\text{I}_2$, khối lượng phân tử và kích thước vỏ electron tăng nhanh làm tương tác van der Waals giữa các phân tử tăng mạnh, "
                    r"dẫn đến nhiệt độ nóng chảy và nhiệt độ sôi tăng dần."
                ),
            ),
            tf4(
                stem=(
                    r"Xét ba hợp chất: sodium chloride ($\text{NaCl}$), hydrogen chloride ($\text{HCl}$) và nước ($\text{H}_2\text{O}$). "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Ở điều kiện thường, $\text{NaCl}$ tồn tại ở dạng tinh thể ion rắn, có nhiệt độ nóng chảy cao ($801^\circ\text{C}$).",
                    r"b) Tinh thể $\text{NaCl}$ ở trạng thái rắn khan dẫn điện rất tốt vì chứa sẵn các ion $\text{Na}^+$ và $\text{Cl}^-$.",
                    r"c) Trong phân tử $\text{HCl}$ và $\text{H}_2\text{O}$, các cặp electron dùng chung đều bị lệch về phía nguyên tử có độ âm điện lớn hơn ($\text{Cl}$ và $\text{O}$).",
                    r"d) Trong phân tử $\text{H}_2\text{O}$, nguyên tử oxygen ở trung tâm có $4$ cặp electron dùng chung với hai nguyên tử hydrogen và không còn cặp electron hóa trị chưa liên kết nào.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: $\text{NaCl}$ là hợp chất ion điển hình, lực hút tĩnh điện giữa các ion $\text{Na}^+$ và $\text{Cl}^-$ rất mạnh nên ở điều kiện thường là chất rắn có nhiệt độ nóng chảy cao. "
                    r"• b) Sai: Ở trạng thái rắn khan, các ion $\text{Na}^+$ và $\text{Cl}^-$ bị giữ chặt tại các nút mạng tinh thể, không di chuyển tự do được nên $\text{NaCl}$ rắn không dẫn điện (chỉ dẫn điện khi nóng chảy hoặc tan trong nước). "
                    r"• c) Đúng: Liên kết $\text{H}-\text{Cl}$ và $\text{O}-\text{H}$ là các liên kết cộng hóa trị phân cực, cặp electron chung lệch về phía $\text{Cl}$ và $\text{O}$. "
                    r"• d) Sai: Nguyên tử $\text{O}$ ($Z=8$, có $6$ electron hóa trị) góp chung $2$ electron với $2$ nguyên tử $\text{H}$ tạo $2$ cặp electron dùng chung và vẫn còn $2$ cặp electron hóa trị chưa liên kết."
                ),
            ),
            tf4(
                stem=(
                    r"Cho hai hợp chất hữu cơ có cùng công thức phân tử $\text{C}_2\text{H}_6\text{O}$ ($M = 46\text{ g/mol}$) là "
                    r"ethanol ($\text{CH}_3\text{CH}_2\text{OH}$) và dimethyl ether ($\text{CH}_3\text{OCH}_3$). Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Các phân tử ethanol ($\text{CH}_3\text{CH}_2\text{OH}$) tạo được liên kết hydrogen liên phân tử với nhau do có nguyên tử $\text{H}$ liên kết trực tiếp với nguyên tử $\text{O}$.",
                    r"b) Ở cùng điều kiện áp suất, dimethyl ether ($\text{CH}_3\text{OCH}_3$) có nhiệt độ sôi cao hơn ethanol ($\text{CH}_3\text{CH}_2\text{OH}$).",
                    r"c) Ethanol tan vô hạn trong nước vì các phân tử $\text{CH}_3\text{CH}_2\text{OH}$ tạo được liên kết hydrogen bền vững với các phân tử $\text{H}_2\text{O}$.",
                    r"d) Trong một phân tử ethanol ($\text{C}_2\text{H}_6\text{O}$) chỉ có các liên kết đơn nên tổng số liên kết $\sigma$ bằng $7$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Ethanol có nhóm $-\text{OH}$ nên tạo được liên kết hydrogen liên phân tử ($\dots\text{O}-\text{H}\cdots\text{O}$). "
                    r"• b) Sai: Vì $\text{CH}_3\text{OCH}_3$ không có nguyên tử $\text{H}$ gắn trực tiếp với $\text{O}$ nên không tạo được liên kết hydrogen giữa các phân tử của nó; do đó nhiệt độ sôi của $\text{CH}_3\text{OCH}_3$ ($-24^\circ\text{C}$) thấp hơn nhiều so với $\text{CH}_3\text{CH}_2\text{OH}$ ($78,3^\circ\text{C}$). "
                    r"• c) Đúng: Nhóm $-\text{OH}$ của ethanol tạo liên kết hydrogen với nước giúp ethanol tan vô hạn trong nước. "
                    r"• d) Sai: Trong phân tử $\text{CH}_3-\text{CH}_2-\text{O}-\text{H}$ có: $5$ liên kết $\text{C}-\text{H}$, $1$ liên kết $\text{C}-\text{C}$, $1$ liên kết $\text{C}-\text{O}$ và $1$ liên kết $\text{O}-\text{H}$, tổng cộng là $5 + 1 + 1 + 1 = 8$ liên kết $\sigma$ (không phải $7$)."
                ),
            ),
            mcq(
                question=(
                    r"Xét phân tử vinylacetylene có công thức cấu tạo thu gọn là $\text{CH}_2=\text{CH}-\text{C}\equiv\text{CH}$ (công thức phân tử $\text{C}_4\text{H}_4$). "
                    r"Tổng số liên kết sigma ($\sigma$) và tổng số liên kết pi ($\pi$) trong một phân tử vinylacetylene lần lượt là:"
                ),
                options=[
                    r"$7$ liên kết $\sigma$ và $3$ liên kết $\pi$.",
                    r"$7$ liên kết $\sigma$ và $2$ liên kết $\pi$.",
                    r"$6$ liên kết $\sigma$ và $3$ liên kết $\pi$.",
                    r"$8$ liên kết $\sigma$ và $3$ liên kết $\pi$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Phân tích các liên kết trong phân tử $\text{CH}_2=\text{CH}-\text{C}\equiv\text{CH}$: "
                    r"• Có $4$ liên kết đơn $\text{C}-\text{H}$ $\Rightarrow 4$ liên kết $\sigma$. "
                    r"• Có $1$ liên kết đơn $\text{C}-\text{C}$ $\Rightarrow 1$ liên kết $\sigma$. "
                    r"• Có $1$ liên kết đôi $\text{C}=\text{C}$ $\Rightarrow 1$ liên kết $\sigma$ và $1$ liên kết $\pi$. "
                    r"• Có $1$ liên kết ba $\text{C}\equiv\text{C}$ $\Rightarrow 1$ liên kết $\sigma$ và $2$ liên kết $\pi$. "
                    r"Vậy tổng số liên kết $\sigma$ là $4 + 1 + 1 + 1 = 7$ và tổng số liên kết $\pi$ là $1 + 2 = 3$."
                ),
            ),
            short(
                question=(
                    r"Trong phân tử nitric acid ($\text{HNO}_3$), nguyên tử nitrogen ở trung tâm liên kết với các nguyên tử oxygen "
                    r"sao cho mọi nguyên tử đều thỏa mãn quy tắc octet. Hỏi tổng số electron hóa trị đã tham gia tạo thành các liên kết "
                    r"(tức tổng số electron thuộc các cặp electron dùng chung) trong một phân tử $\text{HNO}_3$ là bao nhiêu?"
                ),
                answer=["10"],
                level="vandung",
                solution=(
                    r"Công thức cấu tạo thỏa mãn quy tắc octet của phân tử $\text{HNO}_3$ là $\text{H}-\text{O}-\text{N}(=\text{O})\rightarrow\text{O}$. "
                    r"Các cặp electron dùng chung trong phân tử gồm: $1$ cặp của liên kết đơn $\text{H}-\text{O}$ ($2$ electron), "
                    r"$1$ cặp của liên kết đơn $\text{O}-\text{N}$ ($2$ electron), $2$ cặp của liên kết đôi $\text{N}=\text{O}$ ($4$ electron) "
                    r"và $1$ cặp của liên kết cho – nhận $\text{N}\rightarrow\text{O}$ ($2$ electron). "
                    r"Tổng cộng có $1 + 1 + 2 + 1 = 5$ cặp electron dùng chung, ứng với $5 \times 2 = 10$ electron tham gia liên kết."
                ),
            ),
        ],
        description="Tìm hiểu quy tắc octet, sự hình thành và bản chất của liên kết ion, liên kết cộng hóa trị (không phân cực, phân cực, cho - nhận), liên kết sigma và pi, năng lượng liên kết, liên kết hydrogen và tương tác van der Waals.",
    ),

    # =========================================================================
    # CHƯƠNG 5: PHẢN ỨNG OXI HÓA – KHỬ
    # =========================================================================
    lesson(
        grade=10,
        order=5,
        code="H10-C05",
        title="Chương 5: Phản ứng oxi hóa – khử",
        topic="phan-ung-oxy-hoa-khu",
        summary=(
            r"Số oxi hóa là điện tích quy ước của nguyên tử trong phân tử khi giả định tất cả các liên kết đều là liên kết ion. "
            r"Phản ứng oxi hóa – khử là phản ứng hóa học trong đó có sự chuyển dịch electron giữa các chất phản ứng, hay có sự thay đổi "
            r"số oxi hóa của ít nhất một nguyên tố hóa học. Chất khử (chất bị oxi hóa) là chất nhường electron (số oxi hóa tăng), "
            r"chất oxi hóa (chất bị khử) là chất nhận electron (số oxi hóa giảm). Quá trình chất khử nhường electron gọi là quá trình oxi hóa, "
            r"quá trình chất oxi hóa nhận electron gọi là quá trình khử. Việc lập phương trình hóa học của phản ứng oxi hóa – khử và giải toán "
            r"đều dựa trên định luật bảo toàn electron: $\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$."
        ),
        objectives=[
            r"Nêu được khái niệm và vận dụng được $4$ quy tắc xác định số oxi hóa của nguyên tử các nguyên tố trong đơn chất, phân tử hợp chất và ion.",
            r"Phân biệt được khái niệm phản ứng oxi hóa – khử, chất khử, chất oxi hóa, quá trình oxi hóa (sự oxi hóa) và quá trình khử (sự khử).",
            r"Lập được phương trình hóa học của các phản ứng oxi hóa – khử (kể cả phản ứng tự oxi hóa – khử và phản ứng có môi trường acid/kiềm) bằng phương pháp thăng bằng electron.",
            r"Vận dụng được định luật bảo toàn electron ($\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$) để giải các bài toán kim loại hoặc hợp chất tác dụng với dung dịch $\text{HNO}_3$, $\text{H}_2\text{SO}_4$ đặc và nêu được ý nghĩa của phản ứng oxi hóa – khử trong thực tiễn.",
        ],
        formulas=[
            {
                "name": r"Quy tắc tổng đại số số oxi hóa trong phân tử và trong ion",
                "formula": r"$\sum (\text{Số oxi hóa trong phân tử}) = 0 \quad ; \quad \sum (\text{Số oxi hóa trong ion}) = q_{\text{ion}}$",
                "note": r"Trong đơn chất số oxi hóa bằng $0$; trong hợp chất thường gặp: $\text{H}$ là $+1$, $\text{O}$ là $-2$, kim loại nhóm $\text{IA}, \text{IIA}, \text{Al}$ là $+1, +2, +3$, $\text{F}$ luôn là $-1$.",
            },
            {
                "name": r"Bản chất của chất khử, chất oxi hóa và các quá trình chuyển dịch electron",
                "formula": r"$\text{Chất khử} \rightarrow \text{Nhường } e \text{ (Số oxi hóa tăng: Quá trình oxi hóa)} \quad ; \quad \text{Chất oxi hóa} \rightarrow \text{Nhận } e \text{ (Số oxi hóa giảm: Quá trình khử)}$",
                "note": r"Quy tắc ghi nhớ nhanh: Khử cho – O nhận; Khử tăng – O giảm.",
            },
            {
                "name": r"Định luật bảo toàn electron trong phản ứng oxi hóa – khử",
                "formula": r"$\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$",
                "note": r"Áp dụng cho cả một phản ứng đơn lẻ lẫn một chuỗi nhiều phản ứng oxi hóa – khử nối tiếp hoặc song song.",
            },
            {
                "name": r"Hệ thức bảo toàn electron khi kim loại $\text{M}$ (hóa trị $n$) tác dụng với $\text{HNO}_3$ hoặc $\text{H}_2\text{SO}_4$ đặc",
                "formula": r"$n \cdot n_{\text{M}} = 1 \cdot n_{\text{NO}_2} + 3 \cdot n_{\text{NO}} + 8 \cdot n_{\text{N}_2\text{O}} + 10 \cdot n_{\text{N}_2} + 8 \cdot n_{\text{NH}_4\text{NO}_3} \quad ; \quad n \cdot n_{\text{M}} = 2 \cdot n_{\text{SO}_2} + 6 \cdot n_{\text{S}} + 8 \cdot n_{\text{H}_2\text{S}}$",
                "note": r"Do $\overset{+5}{\text{N}} + 1e \to \overset{+4}{\text{N}}$ ($\text{NO}_2$), $+3e \to \overset{+2}{\text{N}}$ ($\text{NO}$), $2\overset{+5}{\text{N}} + 8e \to 2\overset{+1}{\text{N}}$ ($\text{N}_2\text{O}$), $2\overset{+5}{\text{N}} + 10e \to \overset{0}{\text{N}}_2$, $\overset{+5}{\text{N}} + 8e \to \overset{-3}{\text{N}}$ ($\text{NH}_4^+$); và $\overset{+6}{\text{S}} + 2e \to \overset{+4}{\text{S}}$ ($\text{SO}_2$).",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Số oxi hóa và quy tắc xác định số oxi hóa",
                "content": (
                    r"Số oxi hóa của một nguyên tử trong phân tử là điện tích của nguyên tử nguyên tố đó nếu giả định cặp electron chung thuộc hẳn về nguyên tử của nguyên tố có độ âm điện lớn hơn. "
                    r"Bốn quy tắc xác định số oxi hóa: "
                    r"• Quy tắc 1: Trong đơn chất, số oxi hóa của nguyên tố bằng $0$ (ví dụ $\overset{0}{\text{Cu}}, \overset{0}{\text{Fe}}, \overset{0}{\text{O}}_2, \overset{0}{\text{Cl}}_2$). "
                    r"• Quy tắc 2: Trong một phân tử, tổng số oxi hóa của các nguyên tử bằng $0$. "
                    r"• Quy tắc 3: Trong ion đơn nguyên tử, số oxi hóa của nguyên tố bằng điện tích của ion đó (ví dụ $\text{Fe}^{3+}$ có số oxi hóa $+3$, $\text{S}^{2-}$ có số oxi hóa $-2$); trong ion đa nguyên tử, tổng số oxi hóa của các nguyên tử bằng điện tích của ion. "
                    r"• Quy tắc 4: Trong hầu hết các hợp chất, số oxi hóa của hydrogen ($\text{H}$) bằng $+1$ (trừ hydride kim loại như $\text{NaH}, \text{CaH}_2$ bằng $-1$); "
                    r"số oxi hóa của oxygen ($\text{O}$) bằng $-2$ (trừ peroxide như $\text{H}_2\text{O}_2, \text{Na}_2\text{O}_2$ bằng $-1$ và $\text{OF}_2$ bằng $+2$); "
                    r"kim loại nhóm $\text{IA}, \text{IIA}, \text{Al}$ luôn có số oxi hóa $+1, +2, +3$; nguyên tố fluorine ($\text{F}$) trong hợp chất luôn có số oxi hóa $-1$."
                ),
            },
            {
                "title": r"2. Chất khử, chất oxi hóa, quá trình oxi hóa, quá trình khử và phản ứng oxi hóa – khử",
                "content": (
                    r"• Chất khử (còn gọi là chất bị oxi hóa) là chất nhường electron, có số oxi hóa tăng lên sau phản ứng. "
                    r"• Chất oxi hóa (còn gọi là chất bị khử) là chất nhận electron, có số oxi hóa giảm xuống sau phản ứng. "
                    r"• Quá trình chất khử nhường electron được gọi là quá trình oxi hóa (sự oxi hóa); quá trình chất oxi hóa nhận electron được gọi là quá trình khử (sự khử). "
                    r"• Phản ứng oxi hóa – khử là phản ứng hóa học trong đó có sự chuyển dịch electron giữa các chất phản ứng, hay là phản ứng có sự thay đổi số oxi hóa của ít nhất một nguyên tố hóa học. "
                    r"Quá trình oxi hóa và quá trình khử luôn diễn ra đồng thời trong một phản ứng oxi hóa – khử."
                ),
            },
            {
                "title": r"3. Lập phương trình hóa học của phản ứng oxi hóa – khử bằng phương pháp thăng bằng electron",
                "content": (
                    r"Nguyên tắc của phương pháp thăng bằng electron là tổng số electron do chất khử nhường phải bằng tổng số electron mà chất oxi hóa nhận ($\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$). "
                    r"Các bước thực hiện: "
                    r"• Bước 1: Xác định số oxi hóa của các nguyên tố có sự thay đổi số oxi hóa trước và sau phản ứng để tìm chất khử và chất oxi hóa. "
                    r"• Bước 2: Viết quá trình oxi hóa (nhường electron) và quá trình khử (nhận electron). "
                    r"• Bước 3: Tìm hệ số thích hợp cho chất khử và chất oxi hóa (thường là bội chung nhỏ nhất của số electron trao đổi) sao cho tổng số electron nhường bằng tổng số electron nhận. "
                    r"• Bước 4: Đặt hệ số của chất oxi hóa và chất khử vào sơ đồ phản ứng, sau đó cân bằng số lượng nguyên tử của các nguyên tố còn lại (ưu tiên kim loại $\to$ gốc acid môi trường $\to$ $\text{H}$ và kiểm tra lại bằng $\text{O}$)."
                ),
            },
            {
                "title": r"4. Ý nghĩa của phản ứng oxi hóa – khử và ứng dụng bảo toàn electron",
                "content": (
                    r"Phản ứng oxi hóa – khử đóng vai trò vô cùng quan trọng trong tự nhiên và sản xuất: quá trình đốt cháy nhiên liệu (than, xăng, dầu, khí thiên nhiên) cung cấp năng lượng; "
                    r"quá trình quang hợp ở cây xanh và hô hấp ở sinh vật; các quá trình luyện kim (sản xuất gang, thép, nhôm), sản xuất hóa chất ($\text{H}_2\text{SO}_4, \text{HNO}_3$), hoạt động của pin và ắc quy điện hóa, cũng như sự ăn mòn kim loại. "
                    r"Khi giải bài toán hóa học có phản ứng oxi hóa – khử, việc áp dụng định luật bảo toàn electron ($\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$) giúp thiết lập nhanh phương trình toán học dựa vào trạng thái số oxi hóa đầu và cuối mà không cần viết từng phương trình phản ứng trung gian."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Lập phương trình hóa học bằng phương pháp thăng bằng electron",
                "problem": (
                    r"Xác định chất khử, chất oxi hóa, quá trình oxi hóa, quá trình khử và cân bằng phản ứng sau bằng phương pháp thăng bằng electron: "
                    r"$\text{Cu} + \text{HNO}_3\text{ (loãng)} \rightarrow \text{Cu(NO}_3\text{)}_2 + \text{NO} + \text{H}_2\text{O}$."
                ),
                "solution": (
                    r"• Bước 1: Xác định sự thay đổi số oxi hóa: $\overset{0}{\text{Cu}} \rightarrow \overset{+2}{\text{Cu}}$ (tăng, nên $\text{Cu}$ là chất khử) "
                    r"và $\overset{+5}{\text{N}}$ (trong $\text{HNO}_3$) $\rightarrow \overset{+2}{\text{N}}$ (trong $\text{NO}$, giảm, nên $\text{HNO}_3$ là chất oxi hóa kiêm môi trường). "
                    r"• Bước 2 & 3: Viết các quá trình và nhân hệ số: "
                    r"Quá trình oxi hóa: $\overset{0}{\text{Cu}} \rightarrow \overset{+2}{\text{Cu}} + 2e$ (nhân hệ số $3$); "
                    r"Quá trình khử: $\overset{+5}{\text{N}} + 3e \rightarrow \overset{+2}{\text{N}}$ (nhân hệ số $2$). "
                    r"• Bước 4: Điền hệ số $3$ vào $\text{Cu}$, $\text{Cu(NO}_3\text{)}_2$ và hệ số $2$ vào $\text{NO}$. Tổng số nguyên tử $\text{N}$ ở vế phải là $3 \times 2 + 2 = 8 \Rightarrow$ đặt hệ số $8$ trước $\text{HNO}_3$ và hệ số $4$ trước $\text{H}_2\text{O}$. "
                    r"Phương trình hóa học hoàn chỉnh: $3\text{Cu} + 8\text{HNO}_3 \rightarrow 3\text{Cu(NO}_3\text{)}_2 + 2\text{NO} + 4\text{H}_2\text{O}$."
                ),
            },
            {
                "title": r"Ví dụ 2: Giải bài toán hỗn hợp kim loại tác dụng với acid bằng bảo toàn electron",
                "problem": (
                    r"Hòa tan hoàn toàn $11,6\text{ g}$ hỗn hợp gồm hai kim loại iron ($\text{Fe}$, $M = 56\text{ g/mol}$) và copper ($\text{Cu}$, $M = 64\text{ g/mol}$) "
                    r"vào dung dịch $\text{HNO}_3$ loãng dư, thu được $4,958\text{ L}$ khí $\text{NO}$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$; biết $1\text{ mol}$ khí chiếm $24,79\text{ L}$ "
                    r"và $\text{NO}$ là sản phẩm khử duy nhất). Tính khối lượng mỗi kim loại trong hỗn hợp ban đầu."
                ),
                "solution": (
                    r"Số mol khí $\text{NO}$ thu được ở điều kiện chuẩn là $n_{\text{NO}} = \dfrac{4,958}{24,79} = 0,2\text{ mol}$. "
                    r"Gọi số mol của $\text{Fe}$ và $\text{Cu}$ trong hỗn hợp lần lượt là $x$ và $y$ ($\text{mol}$). "
                    r"Theo khối lượng hỗn hợp: $56x + 64y = 11,6$ (1). "
                    r"Khi tác dụng với $\text{HNO}_3$ dư: $\overset{0}{\text{Fe}} \rightarrow \overset{+3}{\text{Fe}} + 3e$ (nhường $3x\text{ mol } e$), "
                    r"$\overset{0}{\text{Cu}} \rightarrow \overset{+2}{\text{Cu}} + 2e$ (nhường $2y\text{ mol } e$), "
                    r"và $\overset{+5}{\text{N}} + 3e \rightarrow \overset{+2}{\text{N}}$ (nhận $3 \times 0,2 = 0,6\text{ mol } e$). "
                    r"Áp dụng định luật bảo toàn electron ($\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$): $3x + 2y = 0,6$ (2). "
                    r"Giải hệ phương trình (1) và (2) ta được $x = 0,1\text{ mol}$ và $y = 0,15\text{ mol}$. "
                    r"Vậy khối lượng mỗi kim loại là $m_{\text{Fe}} = 0,1 \times 56 = 5,6\text{ g}$ và $m_{\text{Cu}} = 0,15 \times 64 = 9,6\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Tổng số oxi hóa của các nguyên tử trong phân tử bằng $0$, trong ion bằng điện tích của ion; đơn chất luôn có số oxi hóa bằng $0$.",
            r"Chất khử nhường electron (số oxi hóa tăng, bị oxi hóa); chất oxi hóa nhận electron (số oxi hóa giảm, bị khử).",
            r"Cân bằng phản ứng oxi hóa – khử và giải toán đều dựa trên định luật bảo toàn electron: $\sum n_{e\text{ nhường}} = \sum n_{e\text{ nhận}}$.",
            r"Chú ý số electron nhận khi tạo thành sản phẩm khử phân tử có $2$ nguyên tử: $2\overset{+5}{\text{N}} + 8e \to \overset{+1}{\text{N}}_2\text{O}$ ($8e$) và $2\overset{+5}{\text{N}} + 10e \to \overset{0}{\text{N}}_2$ ($10e$).",
        ],
        questions=[
            mcq(
                question=r"Số oxi hóa của nguyên tố manganese ($\text{Mn}$) trong hợp chất potassium permanganate ($\text{KMnO}_4$) là:",
                options=[
                    r"$+6$.",
                    r"$+7$.",
                    r"$+4$.",
                    r"$+2$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Trong hợp chất $\text{KMnO}_4$, số oxi hóa của $\text{K}$ là $+1$, của $\text{O}$ là $-2$. "
                    r"Gọi $x$ là số oxi hóa của $\text{Mn}$, ta có: $(+1) + x + 4 \times (-2) = 0 \Rightarrow x = +7$."
                ),
            ),
            mcq(
                question=r"Trong một phản ứng oxi hóa – khử, chất khử là chất:",
                options=[
                    r"Nhận electron, có số oxi hóa giảm sau phản ứng.",
                    r"Nhường electron, có số oxi hóa tăng sau phản ứng.",
                    r"Nhường electron, có số oxi hóa giảm sau phản ứng.",
                    r"Không thay đổi số oxi hóa trong suốt phản ứng.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Theo định nghĩa, chất khử (chất bị oxi hóa) là chất nhường electron, do đó số oxi hóa của nguyên tố đóng vai trò khử tăng lên sau phản ứng."
                ),
            ),
            mcq(
                question=r"Phản ứng hóa học nào sau đây là phản ứng oxi hóa – khử?",
                options=[
                    r"$\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2$.",
                    r"$\text{NaOH} + \text{HCl} \rightarrow \text{NaCl} + \text{H}_2\text{O}$.",
                    r"$\text{Fe} + \text{CuSO}_4 \rightarrow \text{FeSO}_4 + \text{Cu}$.",
                    r"$\text{BaCl}_2 + \text{Na}_2\text{SO}_4 \rightarrow \text{BaSO}_4\downarrow + 2\text{NaCl}$.",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Trong phản ứng $\overset{0}{\text{Fe}} + \overset{+2}{\text{Cu}}\text{SO}_4 \rightarrow \overset{+2}{\text{Fe}}\text{SO}_4 + \overset{0}{\text{Cu}}$, "
                    r"có sự thay đổi số oxi hóa của $\text{Fe}$ (từ $0$ lên $+2$) và $\text{Cu}$ (từ $+2$ xuống $0$), nên đây là phản ứng oxi hóa – khử. "
                    r"Ba phản ứng còn lại không có sự thay đổi số oxi hóa của bất kỳ nguyên tố nào."
                ),
            ),
            mcq(
                question=r"Trong hợp chất ammonium nitrate ($\text{NH}_4\text{NO}_3$), số oxi hóa của nguyên tố nitrogen ($\text{N}$) trong ion $\text{NH}_4^+$ và trong ion $\text{NO}_3^-$ lần lượt là:",
                options=[
                    r"$-3$ và $+5$.",
                    r"$+3$ và $+5$.",
                    r"$-3$ và $+3$.",
                    r"$-4$ và $+6$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"• Trong ion $\text{NH}_4^+$: gọi $x$ là số oxi hóa của $\text{N}$, ta có $x + 4 \times (+1) = +1 \Rightarrow x = -3$. "
                    r"• Trong ion $\text{NO}_3^-$: gọi $y$ là số oxi hóa của $\text{N}$, ta có $y + 3 \times (-2) = -1 \Rightarrow y = +5$."
                ),
            ),
            mcq(
                question=r"Cho phản ứng oxi hóa – khử: $\text{Fe}_2\text{O}_3 + 3\text{CO} \xrightarrow{t^\circ} 2\text{Fe} + 3\text{CO}_2$. Trong phản ứng trên, chất khử và chất oxi hóa lần lượt là:",
                options=[
                    r"$\text{Fe}_2\text{O}_3$ và $\text{CO}$.",
                    r"$\text{CO}$ và $\text{Fe}_2\text{O}_3$.",
                    r"$\text{Fe}$ và $\text{CO}_2$.",
                    r"$\text{CO}_2$ và $\text{Fe}$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Xác định số oxi hóa: trong $\text{CO}$, nguyên tử $\overset{+2}{\text{C}}$ tăng số oxi hóa lên $\overset{+4}{\text{C}}$ trong $\text{CO}_2$ nên $\text{CO}$ là chất khử; "
                    r"trong $\text{Fe}_2\text{O}_3$, nguyên tử $\overset{+3}{\text{Fe}}$ giảm số oxi hóa xuống $\overset{0}{\text{Fe}}$ nên $\text{Fe}_2\text{O}_3$ là chất oxi hóa."
                ),
            ),
            mcq(
                question=(
                    r"Cho sơ đồ phản ứng: $a\text{Al} + b\text{HNO}_3 \rightarrow c\text{Al(NO}_3\text{)}_3 + d\text{N}_2\text{O} + e\text{H}_2\text{O}$ "
                    r"(với $a, b, c, d, e$ là các hệ số nguyên dương tối giản). Tổng hệ số $(a + b)$ của các chất tham gia phản ứng là:"
                ),
                options=[
                    r"$38$.",
                    r"$46$.",
                    r"$20$.",
                    r"$30$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Thăng bằng electron: "
                    r"• Quá trình oxi hóa: $\overset{0}{\text{Al}} \rightarrow \overset{+3}{\text{Al}} + 3e$ (nhân hệ số $8$). "
                    r"• Quá trình khử: $2\overset{+5}{\text{N}} + 8e \rightarrow \overset{+1}{\text{N}}_2\text{O}$ (nhân hệ số $3$). "
                    r"Phương trình cân bằng tối giản là: $8\text{Al} + 30\text{HNO}_3 \rightarrow 8\text{Al(NO}_3\text{)}_3 + 3\text{N}_2\text{O} + 15\text{H}_2\text{O}$. "
                    r"Vậy $a = 8$, $b = 30 \Rightarrow a + b = 8 + 30 = 38$."
                ),
            ),
            tf4(
                stem=(
                    r"Trong phòng thí nghiệm, khí chlorine ($\text{Cl}_2$) được điều chế bằng phản ứng đun nóng manganese dioxide ($\text{MnO}_2$) với dung dịch $\text{HCl}$ đặc theo phương trình: "
                    r"$\text{MnO}_2 + 4\text{HCl} \xrightarrow{t^\circ} \text{MnCl}_2 + \text{Cl}_2\uparrow + 2\text{H}_2\text{O}$. "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Trong phản ứng trên, $\text{MnO}_2$ đóng vai trò là chất oxi hóa còn $\text{HCl}$ đóng vai trò là chất khử kiêm môi trường.",
                    r"b) Số oxi hóa của nguyên tố manganese ($\text{Mn}$) đã tăng từ $+2$ lên $+4$ sau phản ứng.",
                    r"c) Trong số $4$ phân tử $\text{HCl}$ tham gia vào phương trình phản ứng, chỉ có $2$ phân tử $\text{HCl}$ bị oxi hóa thành $\text{Cl}_2$ và $2$ phân tử $\text{HCl}$ đóng vai trò tạo muối $\text{MnCl}_2$.",
                    r"d) Nếu dùng $0,1\text{ mol}$ $\text{MnO}_2$ tác dụng hết với dung dịch $\text{HCl}$ đặc dư thì thu được $0,2\text{ mol}$ khí $\text{Cl}_2$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: $\overset{+4}{\text{Mn}}$ trong $\text{MnO}_2$ giảm số oxi hóa xuống $\overset{+2}{\text{Mn}}$ nên $\text{MnO}_2$ là chất oxi hóa; $\overset{-1}{\text{Cl}}$ trong $\text{HCl}$ vừa tăng số oxi hóa lên $\overset{0}{\text{Cl}}_2$ (chất khử) vừa giữ nguyên $-1$ trong $\text{MnCl}_2$ (môi trường). "
                    r"• b) Sai: Số oxi hóa của $\text{Mn}$ giảm từ $+4$ (trong $\text{MnO}_2$) xuống $+2$ (trong $\text{MnCl}_2$). "
                    r"• c) Đúng: Trong $4\text{HCl}$, có $2$ ion $\text{Cl}^-$ nhường $2$ electron tạo $1$ phân tử $\text{Cl}_2$ và $2$ ion $\text{Cl}^-$ kết hợp với $\text{Mn}^{2+}$ tạo $\text{MnCl}_2$. "
                    r"• d) Sai: Theo tỉ lệ phương trình phản ứng, $n_{\text{Cl}_2} = n_{\text{MnO}_2} = 0,1\text{ mol}$ (không phải $0,2\text{ mol}$)."
                ),
            ),
            tf4(
                stem=(
                    r"Xét phản ứng của kim loại copper ($\text{Cu}$) với dung dịch sulfuric acid ($\text{H}_2\text{SO}_4$) đặc, nóng: "
                    r"$\text{Cu} + 2\text{H}_2\text{SO}_4\text{ (đặc)} \xrightarrow{t^\circ} \text{CuSO}_4 + \text{SO}_2\uparrow + 2\text{H}_2\text{O}$. "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Trong phản ứng trên, mỗi nguyên tử $\text{Cu}$ đã nhường đi $2$ electron để trở thành ion $\text{Cu}^{2+}$ (quá trình oxi hóa).",
                    r"b) Nguyên tố sulfur ($\text{S}$) trong $\text{H}_2\text{SO}_4$ bị khử từ mức số oxi hóa $+6$ về mức số oxi hóa $+2$ trong phân tử $\text{SO}_2$.",
                    r"c) Tỉ lệ số phân tử $\text{H}_2\text{SO}_4$ đóng vai trò chất oxi hóa và số phân tử $\text{H}_2\text{SO}_4$ đóng vai trò môi trường tạo muối là $1 : 1$.",
                    r"d) Ở điều kiện thường hoặc khi đun nóng, kim loại $\text{Cu}$ cũng phản ứng tương tự với dung dịch $\text{H}_2\text{SO}_4$ loãng giải phóng khí $\text{H}_2$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Quá trình oxi hóa là $\overset{0}{\text{Cu}} \rightarrow \overset{+2}{\text{Cu}} + 2e$. "
                    r"• b) Sai: Trong phân tử $\text{SO}_2$, số oxi hóa của $\text{S}$ là $+4$ (giảm từ $+6$ về $+4$, không phải $+2$). "
                    r"• c) Đúng: Trong $2$ phân tử $\text{H}_2\text{SO}_4$ tham gia phản ứng, có $1$ phân tử bị khử thành $\text{SO}_2$ và $1$ phân tử tạo muối $\text{CuSO}_4$ (tỉ lệ $1 : 1$). "
                    r"• d) Sai: Kim loại $\text{Cu}$ đứng sau $\text{H}$ trong dãy hoạt động hóa học nên không tác dụng được với dung dịch $\text{H}_2\text{SO}_4$ loãng."
                ),
            ),
            mcq(
                question=(
                    r"Hòa tan hoàn toàn $12,0\text{ g}$ hỗn hợp gồm $\text{Fe}$ ($M = 56\text{ g/mol}$) và $\text{Cu}$ ($M = 64\text{ g/mol}$) "
                    r"vào dung dịch $\text{HNO}_3$ đặc, nóng, dư thì thu được $12,395\text{ L}$ khí $\text{NO}_2$ (sản phẩm khử duy nhất, đo ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$ với $V_{\text{mol}} = 24,79\text{ L/mol}$). "
                    r"Phần trăm khối lượng của $\text{Fe}$ trong hỗn hợp ban đầu là:"
                ),
                options=[
                    r"$46,67\%$.",
                    r"$53,33\%$.",
                    r"$35,00\%$.",
                    r"$65,00\%$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Số mol khí $\text{NO}_2$ (ở đkc) là $n_{\text{NO}_2} = \dfrac{12,395}{24,79} = 0,5\text{ mol}$. "
                    r"Gọi số mol của $\text{Fe}$ và $\text{Cu}$ trong hỗn hợp lần lượt là $x$ và $y$ ($\text{mol}$). "
                    r"Ta có phương trình khối lượng: $56x + 64y = 12,0$ (1). "
                    r"Áp dụng bảo toàn electron ($\overset{0}{\text{Fe}} \to \overset{+3}{\text{Fe}} + 3e$; $\overset{0}{\text{Cu}} \to \overset{+2}{\text{Cu}} + 2e$; $\overset{+5}{\text{N}} + 1e \to \overset{+4}{\text{N}}$): "
                    r"$3x + 2y = 1 \times 0,5 = 0,5$ (2). "
                    r"Giải hệ (1) và (2) được $x = 0,1\text{ mol}$ và $y = 0,1\text{ mol}$. "
                    r"Khối lượng $\text{Fe}$ là $m_{\text{Fe}} = 0,1 \times 56 = 5,6\text{ g} \Rightarrow \%m_{\text{Fe}} = \dfrac{5,6}{12,0} \times 100\% \approx 46,67\%$."
                ),
            ),
            short(
                question=(
                    r"Hòa tan hoàn toàn $m\text{ g}$ kim loại aluminium ($\text{Al}$, $M = 27\text{ g/mol}$) vào dung dịch $\text{HNO}_3$ loãng dư, "
                    r"thu được $0,15\text{ mol}$ khí $\text{NO}$ và $0,05\text{ mol}$ khí $\text{N}_2\text{O}$ (không còn sản phẩm khử nào khác). "
                    r"Hãy tính giá trị của $m$ (theo đơn vị gam)."
                ),
                answer=["7,65", "7.65"],
                level="vandung",
                solution=(
                    r"Các quá trình trao đổi electron: "
                    r"• Quá trình oxi hóa: $\overset{0}{\text{Al}} \rightarrow \overset{+3}{\text{Al}} + 3e \Rightarrow n_{e\text{ nhường}} = 3n_{\text{Al}}$. "
                    r"• Quá trình khử: $\overset{+5}{\text{N}} + 3e \rightarrow \overset{+2}{\text{N}}$ ($\text{NO}$) và $2\overset{+5}{\text{N}} + 8e \rightarrow \overset{+1}{\text{N}}_2\text{O}$ "
                    r"$\Rightarrow n_{e\text{ nhận}} = 3n_{\text{NO}} + 8n_{\text{N}_2\text{O}} = 3 \times 0,15 + 8 \times 0,05 = 0,45 + 0,40 = 0,85\text{ mol}$. "
                    r"Áp dụng bảo toàn electron: $3n_{\text{Al}} = 0,85 \Rightarrow n_{\text{Al}} = \dfrac{0,85}{3}\text{ mol}$. "
                    r"Vậy khối lượng aluminium đã phản ứng là $m = \dfrac{0,85}{3} \times 27 = 0,85 \times 9 = 7,65\text{ g}$."
                ),
            ),
        ],
        description="Nắm vững quy tắc xác định số oxi hóa, khái niệm chất khử, chất oxi hóa, quá trình oxi hóa, quá trình khử, phương pháp thăng bằng electron và ứng dụng định luật bảo toàn electron trong giải toán hóa học.",
    ),

    # =========================================================================
    # CHƯƠNG 6: NĂNG LƯỢNG HÓA HỌC (ENTHALPY TẠO THÀNH VÀ BIẾN THIÊN ENTHALPY)
    # =========================================================================
    lesson(
        grade=10,
        order=6,
        code="H10-C06",
        title="Chương 6: Năng lượng hóa học (Enthalpy tạo thành và biến thiên enthalpy)",
        topic="nang-luong-hoa-hoc",
        summary=(
            r"Các phản ứng hóa học luôn kèm theo sự giải phóng hoặc hấp thụ năng lượng dưới dạng nhiệt. "
            r"Biến thiên enthalpy chuẩn của phản ứng ($\Delta_{\text{r}} H^\circ_{298}$, đơn vị $\text{kJ}$) là lượng nhiệt tỏa ra hay thu vào của phản ứng "
            r"ở điều kiện chuẩn ($25^\circ\text{C}$ hay $298\text{ K}$, áp suất $1\text{ bar}$ đối với chất khí, nồng độ $1\text{ mol/L}$ đối với chất tan). "
            r"Phản ứng tỏa nhiệt có $\Delta_{\text{r}} H^\circ_{298} < 0$; phản ứng thu nhiệt có $\Delta_{\text{r}} H^\circ_{298} > 0$. "
            r"Enthalpy tạo thành chuẩn ($\Delta_{\text{f}} H^\circ_{298}$, đơn vị $\text{kJ/mol}$) của một chất là biến thiên enthalpy của phản ứng tạo thành $1\text{ mol}$ chất đó "
            r"từ các đơn chất ở dạng bền vững nhất (với đơn chất bền: $\Delta_{\text{f}} H^\circ_{298} = 0$). Ta có hai công thức tính $\Delta_{\text{r}} H^\circ_{298}$: "
            r"theo nhiệt tạo thành $\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$ "
            r"và theo năng lượng liên kết $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$."
        ),
        objectives=[
            r"Phân biệt được phản ứng tỏa nhiệt ($\Delta_{\text{r}} H^\circ_{298} < 0$, làm nóng môi trường xung quanh) và phản ứng thu nhiệt ($\Delta_{\text{r}} H^\circ_{298} > 0$, làm lạnh môi trường xung quanh) qua các ví dụ thực tiễn.",
            r"Nêu được các thông số của điều kiện chuẩn ($25^\circ\text{C}$ hay $298\text{ K}$, áp suất $1\text{ bar}$, nồng độ $1\text{ mol/L}$), khái niệm enthalpy tạo thành chuẩn $\Delta_{\text{f}} H^\circ_{298}$ và phương trình nhiệt hóa học.",
            r"Vận dụng thành thạo công thức tính biến thiên enthalpy chuẩn của phản ứng dựa vào enthalpy tạo thành chuẩn: $\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$.",
            r"Vận dụng thành thạo công thức tính biến thiên enthalpy chuẩn của phản ứng (khi các chất đều ở thể khí) dựa vào năng lượng liên kết: $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$.",
        ],
        formulas=[
            {
                "name": r"Quy ước dấu của biến thiên enthalpy chuẩn $\Delta_{\text{r}} H^\circ_{298}$",
                "formula": r"$\Delta_{\text{r}} H^\circ_{298} < 0 \Rightarrow \text{Phản ứng tỏa nhiệt} \quad ; \quad \Delta_{\text{r}} H^\circ_{298} > 0 \Rightarrow \text{Phản ứng thu nhiệt}$",
                "note": r"Phản ứng tỏa nhiệt có tổng năng lượng chất đầu lớn hơn sản phẩm; phản ứng thu nhiệt có tổng năng lượng chất đầu nhỏ hơn sản phẩm.",
            },
            {
                "name": r"Enthalpy tạo thành chuẩn của đơn chất bền vững nhất",
                "formula": r"$\Delta_{\text{f}} H^\circ_{298}(\text{đơn chất bền}) = 0\text{ kJ/mol}$",
                "note": r"Ví dụ: $\Delta_{\text{f}} H^\circ_{298}$ của $\text{O}_2(g), \text{H}_2(g), \text{N}_2(g), \text{Cl}_2(g), \text{C}(\text{graphite}), \text{Fe}(s)$ đều bằng $0$.",
            },
            {
                "name": r"Công thức 1: Tính $\Delta_{\text{r}} H^\circ_{298}$ theo enthalpy tạo thành chuẩn (Sản phẩm trừ Chất đầu)",
                "formula": r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$",
                "note": r"Phải nhân giá trị $\Delta_{\text{f}} H^\circ_{298}$ của mỗi chất với hệ số cân bằng tương ứng trong phương trình hóa học.",
            },
            {
                "name": r"Công thức 2: Tính $\Delta_{\text{r}} H^\circ_{298}$ theo năng lượng liên kết $E_{\text{b}}$ (Chất đầu trừ Sản phẩm)",
                "formula": r"$\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$",
                "note": r"Chỉ áp dụng cho phản ứng trong đó tất cả các chất tham gia và sản phẩm đều ở thể khí ($g$).",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Phản ứng tỏa nhiệt, phản ứng thu nhiệt và điều kiện chuẩn",
                "content": (
                    r"• Phản ứng tỏa nhiệt là phản ứng hóa học giải phóng năng lượng dưới dạng nhiệt ra môi trường xung quanh (làm nhiệt độ môi trường tăng lên), "
                    r"ví dụ: phản ứng đốt cháy nhiên liệu (than, gas, cồn, xăng), phản ứng tôi vôi ($\text{CaO} + \text{H}_2\text{O} \to \text{Ca(OH)}_2$), phản ứng trung hòa acid – base, phản ứng oxi hóa glucose trong cơ thể. "
                    r"• Phản ứng thu nhiệt là phản ứng hóa học hấp thụ năng lượng dưới dạng nhiệt từ môi trường xung quanh (làm nhiệt độ môi trường giảm xuống), "
                    r"ví dụ: phản ứng nung đá vôi ($\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2$), phản ứng hòa tan viên sủi hoặc muối $\text{NH}_4\text{NO}_3$ vào nước, phản ứng nhiệt phân $\text{KClO}_3$. "
                    r"• Điều kiện chuẩn trong nhiệt hóa học được quy định là: áp suất $1\text{ bar}$ (đối với chất khí), nồng độ $1\text{ mol/L}$ (đối với chất tan trong dung dịch) và nhiệt độ thường được chọn là $298\text{ K}$ ($25^\circ\text{C}$)."
                ),
            },
            {
                "title": r"2. Biến thiên enthalpy chuẩn của phản ứng ($\Delta_{\text{r}} H^\circ_{298}$) và phương trình nhiệt hóa học",
                "content": (
                    r"Biến thiên enthalpy của phản ứng (nhiệt phản ứng, ký hiệu $\Delta_{\text{r}} H$) là lượng nhiệt tỏa ra hoặc thu vào của một phản ứng hóa học ở áp suất không đổi. "
                    r"Ở điều kiện chuẩn, đại lượng này được ký hiệu là $\Delta_{\text{r}} H^\circ_{298}$ (đơn vị thường dùng là $\text{kJ}$). "
                    r"• Nếu $\Delta_{\text{r}} H^\circ_{298} < 0$: phản ứng tỏa nhiệt (càng âm thì tỏa càng nhiều nhiệt và càng thuận lợi về mặt năng lượng). "
                    r"• Nếu $\Delta_{\text{r}} H^\circ_{298} > 0$: phản ứng thu nhiệt (cần cung cấp nhiệt lượng để phản ứng diễn ra). "
                    r"Phương trình nhiệt hóa học là phương trình phản ứng hóa học có kèm theo trạng thái tập hợp của các chất ($s$: rắn, $l$: lỏng, $g$: khí, $aq$: dung dịch) và giá trị $\Delta_{\text{r}} H^\circ_{298}$. "
                    r"Lưu ý: Khi nhân hệ số của phương trình nhiệt hóa học với $k$ thì giá trị $\Delta_{\text{r}} H^\circ_{298}$ cũng nhân với $k$; khi đảo ngược chiều phản ứng thì $\Delta_{\text{r}} H^\circ_{298}$ đổi dấu."
                ),
            },
            {
                "title": r"3. Enthalpy tạo thành chuẩn ($\Delta_{\text{f}} H^\circ_{298}$) và cách tính $\Delta_{\text{r}} H^\circ_{298}$ theo nhiệt tạo thành",
                "content": (
                    r"Enthalpy tạo thành chuẩn (hay nhiệt tạo thành chuẩn, ký hiệu $\Delta_{\text{f}} H^\circ_{298}$, đơn vị $\text{kJ/mol}$) của một chất là biến thiên enthalpy của phản ứng "
                    r"tạo thành $1\text{ mol}$ chất đó từ các đơn chất ở dạng bền vững nhất ở điều kiện chuẩn. "
                    r"Theo định nghĩa, enthalpy tạo thành chuẩn của mọi đơn chất ở dạng bền nhất ở điều kiện chuẩn (như $\text{O}_2(g)$, $\text{H}_2(g)$, $\text{N}_2(g)$, $\text{C}(\text{graphite})$...) đều bằng $0$. "
                    r"Chất có $\Delta_{\text{f}} H^\circ_{298} < 0$ thì bền hơn về mặt năng lượng so với các đơn chất tạo nên nó. "
                    r"Từ giá trị $\Delta_{\text{f}} H^\circ_{298}$ của các chất, biến thiên enthalpy chuẩn của phản ứng được tính theo quy tắc lấy tổng nhiệt tạo thành của sản phẩm trừ đi tổng nhiệt tạo thành của chất đầu: "
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$."
                ),
            },
            {
                "title": r"4. Tính biến thiên enthalpy chuẩn của phản ứng theo năng lượng liên kết ($E_{\text{b}}$)",
                "content": (
                    r"Phản ứng hóa học về bản chất là quá trình phá vỡ các liên kết hóa học trong chất đầu (cần thu năng lượng, mang dấu $+$) "
                    r"và hình thành các liên kết hóa học mới trong sản phẩm (tỏa năng lượng, mang dấu $-$). "
                    r"Đối với phản ứng có tất cả các chất tham gia và sản phẩm đều ở thể khí ($g$), biến thiên enthalpy chuẩn của phản ứng được tính bằng hiệu giữa tổng năng lượng liên kết của các chất đầu "
                    r"và tổng năng lượng liên kết của các sản phẩm: $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$. "
                    r"Cần đặc biệt lưu ý không nhầm lẫn thứ tự trừ giữa hai công thức: tính theo $\Delta_{\text{f}} H^\circ_{298}$ là $(\text{sp}) - (\text{cđ})$, còn tính theo $E_{\text{b}}$ là $(\text{cđ}) - (\text{sp})$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Tính biến thiên enthalpy chuẩn của phản ứng dựa vào nhiệt tạo thành chuẩn",
                "problem": (
                    r"Cho phản ứng đốt cháy hoàn toàn khí methane: $\text{CH}_4(g) + 2\text{O}_2(g) \xrightarrow{t^\circ} \text{CO}_2(g) + 2\text{H}_2\text{O}(l)$. "
                    r"Biết enthalpy tạo thành chuẩn $\Delta_{\text{f}} H^\circ_{298}$ của $\text{CH}_4(g)$, $\text{CO}_2(g)$ và $\text{H}_2\text{O}(l)$ lần lượt là "
                    r"$-74,6\text{ kJ/mol}$, $-393,5\text{ kJ/mol}$ và $-285,8\text{ kJ/mol}$. Tính $\Delta_{\text{r}} H^\circ_{298}$ của phản ứng và cho biết phản ứng tỏa nhiệt hay thu nhiệt."
                ),
                "solution": (
                    r"Vì $\text{O}_2(g)$ là đơn chất ở dạng bền nhất tại điều kiện chuẩn nên $\Delta_{\text{f}} H^\circ_{298}(\text{O}_2(g)) = 0\text{ kJ/mol}$. "
                    r"Áp dụng công thức tính biến thiên enthalpy chuẩn theo nhiệt tạo thành: "
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$ "
                    r"$= \left[1 \times \Delta_{\text{f}} H^\circ_{298}(\text{CO}_2(g)) + 2 \times \Delta_{\text{f}} H^\circ_{298}(\text{H}_2\text{O}(l))\right] - \left[1 \times \Delta_{\text{f}} H^\circ_{298}(\text{CH}_4(g)) + 2 \times \Delta_{\text{f}} H^\circ_{298}(\text{O}_2(g))\right]$ "
                    r"$= \left[(-393,5) + 2 \times (-285,8)\right] - \left[(-74,6) + 0\right] = -965,1 + 74,6 = -890,5\text{ kJ}$. "
                    r"Vì $\Delta_{\text{r}} H^\circ_{298} = -890,5\text{ kJ} < 0$ nên phản ứng đốt cháy methane là phản ứng tỏa nhiệt mạnh."
                ),
            },
            {
                "title": r"Ví dụ 2: Tính biến thiên enthalpy chuẩn của phản ứng dựa vào năng lượng liên kết",
                "problem": (
                    r"Tính biến thiên enthalpy chuẩn $\Delta_{\text{r}} H^\circ_{298}$ của phản ứng tổng hợp ammonia: "
                    r"$\text{N}_2(g) + 3\text{H}_2(g) \xrightarrow{t^\circ, p, xt} 2\text{NH}_3(g)$. "
                    r"Biết năng lượng liên kết ở điều kiện chuẩn: $E_{\text{b}}(\text{N}\equiv\text{N}) = 945\text{ kJ/mol}$, "
                    r"$E_{\text{b}}(\text{H}-\text{H}) = 436\text{ kJ/mol}$ và $E_{\text{b}}(\text{N}-\text{H}) = 391\text{ kJ/mol}$."
                ),
                "solution": (
                    r"Trong $1$ phân tử $\text{N}_2$ có $1$ liên kết ba $\text{N}\equiv\text{N}$; trong $1$ phân tử $\text{H}_2$ có $1$ liên kết đơn $\text{H}-\text{H}$; "
                    r"trong $1$ phân tử $\text{NH}_3$ có $3$ liên kết đơn $\text{N}-\text{H}$ (nên $2\text{ mol}$ $\text{NH}_3$ có $2 \times 3 = 6\text{ mol}$ liên kết $\text{N}-\text{H}$). "
                    r"Áp dụng công thức tính theo năng lượng liên kết: "
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp}) = \left[1 \times E_{\text{b}}(\text{N}\equiv\text{N}) + 3 \times E_{\text{b}}(\text{H}-\text{H})\right] - \left[2 \times 3 \times E_{\text{b}}(\text{N}-\text{H})\right]$ "
                    r"$= (945 + 3 \times 436) - (6 \times 391) = 2253 - 2346 = -93\text{ kJ}$."
                ),
            },
        ],
        key_takeaways=[
            r"Điều kiện chuẩn: áp suất $1\text{ bar}$ (chất khí), nồng độ $1\text{ mol/L}$ (chất tan), nhiệt độ $25^\circ\text{C}$ ($298\text{ K}$).",
            r"Phản ứng tỏa nhiệt có $\Delta_{\text{r}} H^\circ_{298} < 0$; phản ứng thu nhiệt có $\Delta_{\text{r}} H^\circ_{298} > 0$; với đơn chất bền thì $\Delta_{\text{f}} H^\circ_{298} = 0$.",
            r"Tính theo nhiệt tạo thành chuẩn: $\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$.",
            r"Tính theo năng lượng liên kết (các chất ở thể khí): $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$.",
        ],
        questions=[
            mcq(
                question=r"Một phản ứng hóa học có biến thiên enthalpy chuẩn $\Delta_{\text{r}} H^\circ_{298} < 0$. Phát biểu nào sau đây là đúng?",
                options=[
                    r"Phản ứng đó là phản ứng thu nhiệt.",
                    r"Phản ứng đó là phản ứng tỏa nhiệt.",
                    r"Phản ứng đó không có sự trao đổi năng lượng với môi trường.",
                    r"Tổng năng lượng của các sản phẩm lớn hơn tổng năng lượng của các chất phản ứng.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Theo quy ước dấu của nhiệt hóa học, phản ứng có $\Delta_{\text{r}} H^\circ_{298} < 0$ (mang dấu âm) là phản ứng tỏa nhiệt "
                    r"(giải phóng năng lượng dưới dạng nhiệt ra môi trường xung quanh)."
                ),
            ),
            mcq(
                question=r"Enthalpy tạo thành chuẩn ($\Delta_{\text{f}} H^\circ_{298}$) của các đơn chất ở dạng bền vững nhất (như $\text{O}_2(g)$, $\text{H}_2(g)$, $\text{N}_2(g)$) ở điều kiện chuẩn có giá trị bằng:",
                options=[
                    r"$0\text{ kJ/mol}$.",
                    r"$+100\text{ kJ/mol}$.",
                    r"$-100\text{ kJ/mol}$.",
                    r"$+298\text{ kJ/mol}$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Theo định nghĩa, enthalpy tạo thành chuẩn của một đơn chất ở dạng bền vững nhất ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) luôn bằng $0\text{ kJ/mol}$."
                ),
            ),
            mcq(
                question=r"Công thức tính biến thiên enthalpy chuẩn của phản ứng ($\Delta_{\text{r}} H^\circ_{298}$) dựa vào enthalpy tạo thành chuẩn ($\Delta_{\text{f}} H^\circ_{298}$) là:",
                options=[
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp})$.",
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$.",
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) + \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$.",
                    r"$\Delta_{\text{r}} H^\circ_{298} = \dfrac{\sum \Delta_{\text{f}} H^\circ_{298}(\text{sp})}{\sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})}$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Khi tính biến thiên enthalpy chuẩn của phản ứng theo enthalpy tạo thành chuẩn, ta lấy tổng nhiệt tạo thành chuẩn của các chất sản phẩm ($\text{sp}$) "
                    r"trừ đi tổng nhiệt tạo thành chuẩn của các chất đầu ($\text{cđ}$): $\Delta_{\text{r}} H^\circ_{298} = \sum \Delta_{\text{f}} H^\circ_{298}(\text{sp}) - \sum \Delta_{\text{f}} H^\circ_{298}(\text{cđ})$."
                ),
            ),
            mcq(
                question=r"Quá trình nào sau đây trong thực tiễn là phản ứng thu nhiệt ($\Delta_{\text{r}} H^\circ_{298} > 0$)?",
                options=[
                    r"Đốt cháy khí thiên nhiên (chứa thành phần chính là $\text{CH}_4$) để đun nấu.",
                    r"Nung đá vôi ($\text{CaCO}_3$) ở nhiệt độ cao để sản xuất vôi sống ($\text{CaO}$).",
                    r"Đốt cháy than củi trong không khí.",
                    r"Phản ứng tỏa nhiệt khi tôi vôi sống ($\text{CaO}$) trong nước.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Phản ứng nung đá vôi: $\text{CaCO}_3(s) \xrightarrow{t^\circ} \text{CaO}(s) + \text{CO}_2(g)$ có $\Delta_{\text{r}} H^\circ_{298} = +178,5\text{ kJ} > 0$, "
                    r"cần phải cung cấp nhiệt liên tục trong suốt quá trình nung nên là phản ứng thu nhiệt."
                ),
            ),
            mcq(
                question=(
                    r"Cho phản ứng tổng hợp khí hydrogen chloride: $\text{H}_2(g) + \text{Cl}_2(g) \rightarrow 2\text{HCl}(g)$. "
                    r"Biết năng lượng liên kết $E_{\text{b}}$ ở điều kiện chuẩn của các liên kết: $E_{\text{b}}(\text{H}-\text{H}) = 436\text{ kJ/mol}$, "
                    r"$E_{\text{b}}(\text{Cl}-\text{Cl}) = 243\text{ kJ/mol}$ và $E_{\text{b}}(\text{H}-\text{Cl}) = 432\text{ kJ/mol}$. "
                    r"Biến thiên enthalpy chuẩn $\Delta_{\text{r}} H^\circ_{298}$ của phản ứng trên bằng:"
                ),
                options=[
                    r"$+185\text{ kJ}$.",
                    r"$-185\text{ kJ}$.",
                    r"$-247\text{ kJ}$.",
                    r"$+247\text{ kJ}$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Áp dụng công thức tính biến thiên enthalpy chuẩn theo năng lượng liên kết: "
                    r"$\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp}) = \left[E_{\text{b}}(\text{H}-\text{H}) + E_{\text{b}}(\text{Cl}-\text{Cl})\right] - 2 \times E_{\text{b}}(\text{H}-\text{Cl})$ "
                    r"$= (436 + 243) - 2 \times 432 = 679 - 864 = -185\text{ kJ}$."
                ),
            ),
            mcq(
                question=(
                    r"Cho phương trình nhiệt hóa học của phản ứng nhiệt phân đá vôi: "
                    r"$\text{CaCO}_3(s) \xrightarrow{t^\circ} \text{CaO}(s) + \text{CO}_2(g)$ có $\Delta_{\text{r}} H^\circ_{298} = +178,5\text{ kJ}$. "
                    r"Biết $\Delta_{\text{f}} H^\circ_{298}(\text{CaCO}_3(s)) = -1206,9\text{ kJ/mol}$ và $\Delta_{\text{f}} H^\circ_{298}(\text{CO}_2(g)) = -393,5\text{ kJ/mol}$. "
                    r"Enthalpy tạo thành chuẩn $\Delta_{\text{f}} H^\circ_{298}$ của $\text{CaO}(s)$ là:"
                ),
                options=[
                    r"$-634,9\text{ kJ/mol}$.",
                    r"$+634,9\text{ kJ/mol}$.",
                    r"$-991,9\text{ kJ/mol}$.",
                    r"$-1421,9\text{ kJ/mol}$.",
                ],
                answer="A",
                level="hieu",
                solution=(
                    r"Ta có: $\Delta_{\text{r}} H^\circ_{298} = \left[\Delta_{\text{f}} H^\circ_{298}(\text{CaO}(s)) + \Delta_{\text{f}} H^\circ_{298}(\text{CO}_2(g))\right] - \Delta_{\text{f}} H^\circ_{298}(\text{CaCO}_3(s))$ "
                    r"$\Rightarrow +178,5 = \Delta_{\text{f}} H^\circ_{298}(\text{CaO}(s)) + (-393,5) - (-1206,9)$ "
                    r"$\Rightarrow \Delta_{\text{f}} H^\circ_{298}(\text{CaO}(s)) = 178,5 + 393,5 - 1206,9 = -634,9\text{ kJ/mol}$."
                ),
            ),
            tf4(
                stem=(
                    r"Cho phương trình nhiệt hóa học của phản ứng đốt cháy lưu huỳnh tạo khí sulfur dioxide: "
                    r"$\text{S}(s) + \text{O}_2(g) \xrightarrow{t^\circ} \text{SO}_2(g)$ với $\Delta_{\text{r}} H^\circ_{298} = -296,8\text{ kJ}$. "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Phản ứng đốt cháy $\text{S}(s)$ trong khí $\text{O}_2(g)$ là một phản ứng tỏa nhiệt vì có $\Delta_{\text{r}} H^\circ_{298} < 0$.",
                    r"b) Ở điều kiện chuẩn, enthalpy tạo thành chuẩn của $\text{S}(s)$ và $\text{O}_2(g)$ đều khác $0$.",
                    r"c) Giá trị enthalpy tạo thành chuẩn của khí $\text{SO}_2(g)$ ở điều kiện chuẩn là $\Delta_{\text{f}} H^\circ_{298}(\text{SO}_2(g)) = -296,8\text{ kJ/mol}$.",
                    r"d) Khi đốt cháy hoàn toàn $0,5\text{ mol}$ $\text{S}(s)$ ở điều kiện chuẩn, phản ứng cần thu vào một lượng nhiệt là $148,4\text{ kJ}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Vì $\Delta_{\text{r}} H^\circ_{298} = -296,8\text{ kJ} < 0$ nên đây là phản ứng tỏa nhiệt. "
                    r"• b) Sai: $\text{S}(s)$ (dạng tà phương bền nhất) và $\text{O}_2(g)$ là các đơn chất bền nhất ở điều kiện chuẩn nên có $\Delta_{\text{f}} H^\circ_{298} = 0\text{ kJ/mol}$. "
                    r"• c) Đúng: Phản ứng tạo thành đúng $1\text{ mol}$ $\text{SO}_2(g)$ từ các đơn chất bền $\text{S}(s)$ và $\text{O}_2(g)$ nên $\Delta_{\text{f}} H^\circ_{298}(\text{SO}_2(g)) = \Delta_{\text{r}} H^\circ_{298} = -296,8\text{ kJ/mol}$. "
                    r"• d) Sai: Khi đốt cháy $0,5\text{ mol}$ $\text{S}(s)$, phản ứng tỏa ra (giải phóng) lượng nhiệt là $0,5 \times 296,8 = 148,4\text{ kJ}$ chứ không phải thu nhiệt."
                ),
            ),
            tf4(
                stem=(
                    r"Xét phản ứng cộng hydrogen vào ethylene ở thể khí: $\text{C}_2\text{H}_4(g) + \text{H}_2(g) \xrightarrow{xt, t^\circ} \text{C}_2\text{H}_6(g)$ "
                    r"(công thức cấu tạo: $\text{CH}_2=\text{CH}_2 + \text{H}-\text{H} \rightarrow \text{CH}_3-\text{CH}_3$). "
                    r"Cho năng lượng liên kết ở điều kiện chuẩn: $E_{\text{b}}(\text{C}=\text{C}) = 614\text{ kJ/mol}$, $E_{\text{b}}(\text{C}-\text{C}) = 347\text{ kJ/mol}$, "
                    r"$E_{\text{b}}(\text{C}-\text{H}) = 413\text{ kJ/mol}$ và $E_{\text{b}}(\text{H}-\text{H}) = 436\text{ kJ/mol}$. Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Trong một phân tử $\text{C}_2\text{H}_4$ có $1$ liên kết đôi $\text{C}=\text{C}$ và $4$ liên kết đơn $\text{C}-\text{H}$; trong một phân tử $\text{C}_2\text{H}_6$ có $1$ liên kết đơn $\text{C}-\text{C}$ và $6$ liên kết đơn $\text{C}-\text{H}$.",
                    r"b) Khi tính biến thiên enthalpy chuẩn của phản ứng theo năng lượng liên kết, ta áp dụng công thức $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{sp}) - \sum E_{\text{b}}(\text{cđ})$.",
                    r"c) Biến thiên enthalpy chuẩn của phản ứng trên có giá trị bằng $\Delta_{\text{r}} H^\circ_{298} = -123\text{ kJ}$.",
                    r"d) Phản ứng cộng hydrogen vào ethylene trên là một phản ứng thu nhiệt.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Dựa vào công thức cấu tạo $\text{H}_2\text{C}=\text{CH}_2$ ($1\text{ C}=\text{C}, 4\text{ C}-\text{H}$) và $\text{H}_3\text{C}-\text{CH}_3$ ($1\text{ C}-\text{C}, 6\text{ C}-\text{H}$). "
                    r"• b) Sai: Khi tính theo năng lượng liên kết $E_{\text{b}}$, công thức đúng là lấy tổng năng lượng liên kết chất đầu trừ đi tổng năng lượng liên kết sản phẩm: $\Delta_{\text{r}} H^\circ_{298} = \sum E_{\text{b}}(\text{cđ}) - \sum E_{\text{b}}(\text{sp})$. "
                    r"• c) Đúng: $\Delta_{\text{r}} H^\circ_{298} = \left[E_{\text{b}}(\text{C}=\text{C}) + 4E_{\text{b}}(\text{C}-\text{H}) + E_{\text{b}}(\text{H}-\text{H})\right] - \left[E_{\text{b}}(\text{C}-\text{C}) + 6E_{\text{b}}(\text{C}-\text{H})\right] = (614 + 4 \times 413 + 436) - (347 + 6 \times 413) = 2702 - 2825 = -123\text{ kJ}$. "
                    r"• d) Sai: Vì $\Delta_{\text{r}} H^\circ_{298} = -123\text{ kJ} < 0$ nên đây là phản ứng tỏa nhiệt."
                ),
            ),
            mcq(
                question=(
                    r"Phản ứng nhiệt nhôm dùng để hàn đường ray tàu hỏa có phương trình hóa học: "
                    r"$2\text{Al}(s) + \text{Fe}_2\text{O}_3(s) \xrightarrow{t^\circ} \text{Al}_2\text{O}_3(s) + 2\text{Fe}(s)$. "
                    r"Biết enthalpy tạo thành chuẩn của $\text{Fe}_2\text{O}_3(s)$ là $-824,2\text{ kJ/mol}$ và của $\text{Al}_2\text{O}_3(s)$ là $-1675,7\text{ kJ/mol}$. "
                    r"Nhiệt lượng tỏa ra khi có $54\text{ g}$ $\text{Al}$ ($M = 27\text{ g/mol}$) phản ứng hoàn toàn với lượng dư $\text{Fe}_2\text{O}_3(s)$ ở điều kiện chuẩn là:"
                ),
                options=[
                    r"$851,5\text{ kJ}$.",
                    r"$1703,0\text{ kJ}$.",
                    r"$425,75\text{ kJ}$.",
                    r"$2499,9\text{ kJ}$.",
                ],
                answer="A",
                level="vandung",
                solution=(
                    r"Vì $\text{Al}(s)$ và $\text{Fe}(s)$ là các đơn chất bền nên $\Delta_{\text{f}} H^\circ_{298} = 0\text{ kJ/mol}$. "
                    r"Biến thiên enthalpy chuẩn của phản ứng ứng với $2\text{ mol}$ $\text{Al}$ là: "
                    r"$\Delta_{\text{r}} H^\circ_{298} = \Delta_{\text{f}} H^\circ_{298}(\text{Al}_2\text{O}_3(s)) - \Delta_{\text{f}} H^\circ_{298}(\text{Fe}_2\text{O}_3(s)) = (-1675,7) - (-824,2) = -851,5\text{ kJ}$. "
                    r"Số mol của $54\text{ g}$ $\text{Al}$ là $n_{\text{Al}} = \dfrac{54}{27} = 2\text{ mol}$, đúng bằng hệ số của $\text{Al}$ trong phương trình. "
                    r"Vậy nhiệt lượng tỏa ra là $851,5\text{ kJ}$."
                ),
            ),
            short(
                question=(
                    r"Quá trình oxi hóa hoàn toàn $1\text{ mol}$ glucose ($\text{C}_6\text{H}_{12}\text{O}_6(s)$, $M = 180\text{ g/mol}$) ở điều kiện chuẩn diễn ra theo phương trình nhiệt hóa học: "
                    r"$\text{C}_6\text{H}_{12}\text{O}_6(s) + 6\text{O}_2(g) \rightarrow 6\text{CO}_2(g) + 6\text{H}_2\text{O}(l)$ với $\Delta_{\text{r}} H^\circ_{298} = -2803\text{ kJ}$. "
                    r"Tính nhiệt lượng (theo đơn vị $\text{kJ}$) giải phóng ra khi cơ thể oxi hóa hoàn toàn $18\text{ g}$ glucose ở điều kiện chuẩn."
                ),
                answer=["280,3", "280.3"],
                level="vandung",
                solution=(
                    r"Số mol glucose trong $18\text{ g}$ là $n_{\text{C}_6\text{H}_{12}\text{O}_6} = \dfrac{18}{180} = 0,1\text{ mol}$. "
                    r"Theo phương trình nhiệt hóa học, khi oxi hóa hoàn toàn $1\text{ mol}$ glucose thì giải phóng ra $2803\text{ kJ}$ nhiệt lượng. "
                    r"Vậy khi oxi hóa hoàn toàn $0,1\text{ mol}$ glucose, nhiệt lượng giải phóng ra là $Q = 0,1 \times 2803 = 280,3\text{ kJ}$."
                ),
            ),
        ],
        description="Tìm hiểu phản ứng tỏa nhiệt và phản ứng thu nhiệt, điều kiện chuẩn, khái niệm enthalpy tạo thành chuẩn, biến thiên enthalpy chuẩn của phản ứng và hai công thức tính biến thiên enthalpy chuẩn theo nhiệt tạo thành và theo năng lượng liên kết.",
    ),

    # =========================================================================
    # CHƯƠNG 7: NHÓM HALOGEN (NHÓM VIIA)
    # =========================================================================
    lesson(
        grade=10,
        order=7,
        code="H10-C07",
        title="Chương 7: Nhóm Halogen (Nhóm VIIA)",
        topic="nhom-halogen",
        summary=(
            r"Nhóm halogen (nhóm $\text{VIIA}$) gồm các nguyên tố fluorine ($\text{F}$), chlorine ($\text{Cl}$), bromine ($\text{Br}$), iodine ($\text{I}$)... "
            r"Nguyên tử của chúng đều có cấu hình electron lớp ngoài cùng là $ns^2 np^5$ ($7$ electron hóa trị) nên là những phi kim điển hình. "
            r"Ở dạng đơn chất, halogen tồn tại dưới dạng phân tử $\text{X}_2$; đi từ $\text{F}_2$ đến $\text{I}_2$, trạng thái chuyển từ khí ($\text{F}_2, \text{Cl}_2$) sang lỏng ($\text{Br}_2$) và rắn ($\text{I}_2$), "
            r"nhiệt độ nóng chảy và nhiệt độ sôi tăng dần (do tương tác van der Waals tăng), còn tính oxi hóa giảm dần ($\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$). "
            r"Các hydrogen halide ($\text{HF}, \text{HCl}, \text{HBr}, \text{HI}$) tan trong nước tạo dung dịch hydrohalic acid có tính acid tăng dần từ $\text{HF}$ (yếu, ăn mòn thủy tinh) đến $\text{HI}$ (rất mạnh); "
            r"tính khử của các ion halide tăng dần theo chiều $\text{F}^- < \text{Cl}^- < \text{Br}^- < \text{I}^-$, và được nhận biết bằng dung dịch $\text{AgNO}_3$."
        ),
        objectives=[
            r"Nêu được vị trí của nhóm halogen trong bảng tuần hoàn, cấu hình electron lớp ngoài cùng ($ns^2 np^5$), sự biến đổi trạng thái, màu sắc, nhiệt độ nóng chảy, nhiệt độ sôi của các đơn chất từ $\text{F}_2$ đến $\text{I}_2$.",
            r"Trình bày được xu hướng giảm dần tính oxi hóa của các đơn chất ($\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$) và viết được các phương trình hóa học chứng minh tính chất của halogen tác dụng với kim loại, hydrogen, nước, dung dịch kiềm và dung dịch muối halide.",
            r"Trình bày được nguyên tắc điều chế khí $\text{Cl}_2$ trong phòng thí nghiệm (từ $\text{HCl}$ đặc và chất oxi hóa mạnh như $\text{MnO}_2, \text{KMnO}_4$) và trong công nghiệp (điện phân dung dịch $\text{NaCl}$ bão hòa có màng ngăn).",
            r"Giải thích được quy luật biến đổi nhiệt độ sôi (cao bất thường ở $\text{HF}$ do liên kết hydrogen), tính acid tăng dần từ $\text{HF}$ đến $\text{HI}$, tính khử tăng dần của các ion halide ($\text{Cl}^- < \text{Br}^- < \text{I}^-$) và cách phân biệt các ion $\text{F}^-, \text{Cl}^-, \text{Br}^-, \text{I}^-$ bằng dung dịch $\text{AgNO}_3$.",
        ],
        formulas=[
            {
                "name": r"Cấu hình electron lớp ngoài cùng và quy luật tính oxi hóa của đơn chất nhóm $\text{VIIA}$",
                "formula": r"$\text{Cấu hình lớp ngoài cùng: } ns^2 np^5 \quad ; \quad \text{Tính oxi hóa: } \text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$",
                "note": r"Từ $\text{Cl}_2$ trở đi, halogen mạnh hơn đẩy được halogen yếu hơn ra khỏi dung dịch muối halide: $\text{Cl}_2 + 2\text{NaBr} \to 2\text{NaCl} + \text{Br}_2$; $\text{Br}_2 + 2\text{NaI} \to 2\text{NaBr} + \text{I}_2$.",
            },
            {
                "name": r"Phản ứng của $\text{Cl}_2$ với nước và với dung dịch kiềm ($\text{NaOH}$)",
                "formula": r"$\text{Cl}_2 + \text{H}_2\text{O} \rightleftharpoons \text{HCl} + \text{HClO} \quad ; \quad \text{Cl}_2 + 2\text{NaOH} \rightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$",
                "note": r"Đều là phản ứng tự oxi hóa – khử của $\text{Cl}_2$; hỗn hợp $\text{NaCl}$ và $\text{NaClO}$ là thành phần chính của nước Javel tẩy trắng, sát trùng.",
            },
            {
                "name": r"Điều chế khí $\text{Cl}_2$ trong phòng thí nghiệm và trong công nghiệp",
                "formula": r"$\text{MnO}_2 + 4\text{HCl}_{\text{đặc}} \xrightarrow{t^\circ} \text{MnCl}_2 + \text{Cl}_2\uparrow + 2\text{H}_2\text{O} \quad ; \quad 2\text{NaCl} + 2\text{H}_2\text{O} \xrightarrow{\text{đpdd, mn}} 2\text{NaOH} + \text{H}_2\uparrow + \text{Cl}_2\uparrow$",
                "note": r"Trong phòng thí nghiệm có thể thay $\text{MnO}_2$ bằng $\text{KMnO}_4$ hoặc $\text{KClO}_3$.",
            },
            {
                "name": r"Quy luật tính acid của dãy $\text{HX}$ và tính khử của các ion $\text{X}^-$",
                "formula": r"$\text{Tính acid: } \text{HF (yếu)} < \text{HCl} < \text{HBr} < \text{HI (mạnh nhất)} \quad ; \quad \text{Tính khử: } \text{F}^- < \text{Cl}^- < \text{Br}^- < \text{I}^-$",
                "note": r"Riêng dung dịch $\text{HF}$ ăn mòn thủy tinh do phản ứng: $\text{SiO}_2 + 4\text{HF} \rightarrow \text{SiF}_4\uparrow + 2\text{H}_2\text{O}$.",
            },
            {
                "name": r"Nhận biết các ion halide ($\text{F}^-, \text{Cl}^-, \text{Br}^-, \text{I}^-$) bằng dung dịch $\text{AgNO}_3$",
                "formula": r"$\text{AgF (tan, không kết tủa)} \;;\; \text{AgCl}\downarrow\text{ (trắng)} \;;\; \text{AgBr}\downarrow\text{ (vàng nhạt)} \;;\; \text{AgI}\downarrow\text{ (vàng đậm)}$",
                "note": r"Phương trình ion rút gọn: $\text{Ag}^+ + \text{X}^- \rightarrow \text{AgX}\downarrow$ (với $\text{X} = \text{Cl}, \text{Br}, \text{I}$).",
            },
        ],
        theory_sections=[
            {
                "title": r"1. Vị trí, cấu tạo và tính chất vật lý của các đơn chất nhóm Halogen",
                "content": (
                    r"Nhóm halogen (nhóm $\text{VIIA}$) gồm các nguyên tố: fluorine (${}_9\text{F}$), chlorine (${}_{17}\text{Cl}$), bromine (${}_{35}\text{Br}$), iodine (${}_{53}\text{I}$), astatine (${}_{85}\text{At}$) và tennessine (${}_{117}\text{Ts}$). "
                    r"Lớp electron ngoài cùng của nguyên tử halogen có dạng $ns^2 np^5$ ($7$ electron hóa trị), chỉ thiếu $1$ electron để đạt cấu hình octet bền vững nên dễ nhận thêm $1$ electron hoặc góp chung $1$ electron. "
                    r"Trong hợp chất, fluorine luôn có số oxi hóa duy nhất là $-1$ (vì có độ âm điện lớn nhất $\chi = 3,98$ và không có phân lớp $d$), trong khi $\text{Cl}, \text{Br}, \text{I}$ ngoài số oxi hóa $-1$ còn có các số oxi hóa dương $+1, +3, +5, +7$. "
                    r"Ở điều kiện thường, đi từ $\text{F}_2$ đến $\text{I}_2$: $\text{F}_2$ là chất khí màu lục nhạt, $\text{Cl}_2$ là chất khí màu vàng lục, $\text{Br}_2$ là chất lỏng màu nâu đỏ dễ bay hơi, còn $\text{I}_2$ là chất rắn màu đen tím (khi đun nóng bị thăng hoa chuyển thẳng từ thể rắn sang hơi màu tím mà không qua thể lỏng). "
                    r"Do kích thước và khối lượng phân tử tăng dần làm tương tác van der Waals tăng, nhiệt độ nóng chảy và nhiệt độ sôi tăng dần từ $\text{F}_2$ đến $\text{I}_2$."
                ),
            },
            {
                "title": r"2. Tính chất hóa học và điều chế đơn chất Halogen",
                "content": (
                    r"Các đơn chất halogen là những chất oxi hóa mạnh, và tính oxi hóa giảm dần từ $\text{F}_2 \to \text{Cl}_2 \to \text{Br}_2 \to \text{I}_2$: "
                    r"• Tác dụng với kim loại: $\text{F}_2$ oxi hóa được tất cả các kim loại; $\text{Cl}_2$ oxi hóa hầu hết kim loại lên mức số oxi hóa cao (như $2\text{Fe} + 3\text{Cl}_2 \xrightarrow{t^\circ} 2\text{FeCl}_3$). "
                    r"• Tác dụng với hydrogen ($\text{H}_2(g) + \text{X}_2(g) \to 2\text{HX}(g)$): mức độ phản ứng giảm dần từ $\text{F}_2$ (nổ mạnh ngay trong bóng tối ở nhiệt độ rất thấp) $\to \text{Cl}_2$ (cần ánh sáng hoặc đun nóng, gây nổ) $\to \text{Br}_2$ (đun nóng cao, không nổ) $\to \text{I}_2$ (đun nóng có xúc tác, phản ứng thuận nghịch $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$). "
                    r"• Tác dụng với nước và dung dịch kiềm: Riêng $\text{F}_2$ bốc cháy mãnh liệt với nước giải phóng oxygen ($2\text{F}_2 + 2\text{H}_2\text{O} \to 4\text{HF} + \text{O}_2\uparrow$). "
                    r"Khí $\text{Cl}_2$ tác dụng thuận nghịch với nước tạo $\text{HCl}$ và $\text{HClO}$ (hypochlorous acid có tính oxi hóa mạnh dùng khử trùng nước); tác dụng với dung dịch $\text{NaOH}$ ở nhiệt độ thường tạo nước Javel ($\text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$). "
                    r"• Tác dụng với dung dịch muối halide: $\text{Cl}_2$ đẩy được $\text{Br}_2, \text{I}_2$ ra khỏi dung dịch muối $\text{NaBr}, \text{NaI}$; $\text{Br}_2$ đẩy được $\text{I}_2$ ra khỏi dung dịch $\text{NaI}$."
                ),
            },
            {
                "title": r"3. Hydrogen halide ($\text{HX}$) và Hydrohalic acid",
                "content": (
                    r"• Nhiệt độ sôi của các hydrogen halide: Nhiệt độ sôi tăng dần từ $\text{HCl} < \text{HBr} < \text{HI}$ do khối lượng phân tử tăng làm tương tác van der Waals tăng. "
                    r"Tuy nhiên, $\text{HF}$ ($M = 20$) có nhiệt độ sôi cao bất thường ($19,5^\circ\text{C}$, cao hơn cả $\text{HCl}, \text{HBr}, \text{HI}$) vì giữa các phân tử $\text{HF}$ tạo được liên kết hydrogen liên phân tử rất bền ($\dots\text{F}-\text{H}\cdots\text{F}$). "
                    r"• Tính acid của dung dịch hydrohalic acid: Khi đi từ $\text{HF}$ đến $\text{HI}$, độ dài liên kết $\text{H}-\text{X}$ tăng và năng lượng liên kết giảm dần nên khả năng phân li ra ion $\text{H}^+$ trong nước tăng dần. "
                    r"Do đó tính acid tăng dần theo thứ tự: $\text{HF}$ (acid yếu) $< \text{HCl} < \text{HBr} < \text{HI}$ (acid mạnh nhất trong dãy). "
                    r"Đặc biệt, dung dịch $\text{HF}$ có tính chất riêng là hòa tan được silicon dioxide ($\text{SiO}_2$) trong thủy tinh theo phản ứng $\text{SiO}_2 + 4\text{HF} \to \text{SiF}_4\uparrow + 2\text{H}_2\text{O}$, nên không được đựng dung dịch $\text{HF}$ trong lọ thủy tinh mà phải đựng trong bình nhựa."
                ),
            },
            {
                "title": r"4. Tính khử của các ion Halide ($\text{X}^-$) và nhận biết ion Halide",
                "content": (
                    r"• Tính khử của các ion halide tăng dần theo chiều $\text{F}^- < \text{Cl}^- < \text{Br}^- < \text{I}^-$. Khi cho các muối halide rắn tác dụng với dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng: "
                    r"$\text{NaF}$ và $\text{NaCl}$ chỉ xảy ra phản ứng trao đổi tạo khí $\text{HF}, \text{HCl}$ (không có phản ứng oxi hóa – khử); "
                    r"$\text{NaBr}$ khử được $\text{H}_2\text{SO}_4$ đặc thành khí $\text{SO}_2$ đồng thời tạo $\text{Br}_2$ ($2\text{NaBr} + 2\text{H}_2\text{SO}_4 \to \text{Na}_2\text{SO}_4 + \text{Br}_2 + \text{SO}_2\uparrow + 2\text{H}_2\text{O}$); "
                    r"$\text{NaI}$ có tính khử mạnh hơn nữa nên khử được $\text{H}_2\text{SO}_4$ đặc xuống tận $\text{H}_2\text{S}$ ($8\text{NaI} + 5\text{H}_2\text{SO}_4 \to 4\text{Na}_2\text{SO}_4 + 4\text{I}_2 + \text{H}_2\text{S}\uparrow + 4\text{H}_2\text{O}$). "
                    r"• Để nhận biết các ion halide trong dung dịch, ta dùng thuốc thử là dung dịch silver nitrate ($\text{AgNO}_3$): "
                    r"ion $\text{F}^-$ không tạo kết tủa (vì $\text{AgF}$ tan trong nước); ion $\text{Cl}^-$ tạo kết tủa $\text{AgCl}$ màu trắng; ion $\text{Br}^-$ tạo kết tủa $\text{AgBr}$ màu vàng nhạt; ion $\text{I}^-$ tạo kết tủa $\text{AgI}$ màu vàng đậm."
                ),
            },
        ],
        worked_examples=[
            {
                "title": r"Ví dụ 1: Phân biệt các dung dịch muối halide bằng một thuốc thử",
                "problem": (
                    r"Trình bày phương pháp hóa học để phân biệt $4$ dung dịch không màu đựng trong $4$ lọ mất nhãn: "
                    r"$\text{NaF}$, $\text{NaCl}$, $\text{NaBr}$ và $\text{NaI}$ chỉ bằng một thuốc thử duy nhất. Viết các phương trình hóa học minh họa."
                ),
                "solution": (
                    r"Trích mẫu thử của $4$ dung dịch vào $4$ ống nghiệm riêng biệt có đánh số thứ tự. Nhỏ vài giọt dung dịch silver nitrate ($\text{AgNO}_3$) vào mỗi ống nghiệm: "
                    r"• Ống nghiệm không có hiện tượng kết tủa là dung dịch $\text{NaF}$ (vì muối $\text{AgF}$ tan tốt trong nước). "
                    r"• Ống nghiệm xuất hiện kết tủa màu trắng là dung dịch $\text{NaCl}$: $\text{NaCl} + \text{AgNO}_3 \rightarrow \text{AgCl}\downarrow\text{ (trắng)} + \text{NaNO}_3$. "
                    r"• Ống nghiệm xuất hiện kết tủa màu vàng nhạt là dung dịch $\text{NaBr}$: $\text{NaBr} + \text{AgNO}_3 \rightarrow \text{AgBr}\downarrow\text{ (vàng nhạt)} + \text{NaNO}_3$. "
                    r"• Ống nghiệm xuất hiện kết tủa màu vàng đậm là dung dịch $\text{NaI}$: $\text{NaI} + \text{AgNO}_3 \rightarrow \text{AgI}\downarrow\text{ (vàng đậm)} + \text{NaNO}_3$."
                ),
            },
            {
                "title": r"Ví dụ 2: Bài toán điều chế khí Chlorine và phản ứng thế với muối Halide",
                "problem": (
                    r"Cho $15,8\text{ g}$ potassium permanganate ($\text{KMnO}_4$, $M = 158\text{ g/mol}$) tác dụng hoàn toàn với dung dịch $\text{HCl}$ đặc, dư theo phương trình: "
                    r"$2\text{KMnO}_4 + 16\text{HCl} \rightarrow 2\text{KCl} + 2\text{MnCl}_2 + 5\text{Cl}_2\uparrow + 8\text{H}_2\text{O}$. "
                    r"Toàn bộ lượng khí $\text{Cl}_2$ sinh ra được dẫn vào dung dịch chứa lượng dư sodium bromide ($\text{NaBr}$). "
                    r"Tính thể tích khí $\text{Cl}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) và khối lượng bromine ($\text{Br}_2$, $M = 160\text{ g/mol}$) tạo thành."
                ),
                "solution": (
                    r"Số mol $\text{KMnO}_4$ phản ứng là $n_{\text{KMnO}_4} = \dfrac{15,8}{158} = 0,1\text{ mol}$. "
                    r"Theo phương trình phản ứng: $n_{\text{Cl}_2} = \dfrac{5}{2} n_{\text{KMnO}_4} = \dfrac{5}{2} \times 0,1 = 0,25\text{ mol}$. "
                    r"Thể tích khí $\text{Cl}_2$ thu được ở điều kiện chuẩn là $V_{\text{Cl}_2} = 0,25 \times 24,79 = 6,1975\text{ L}$. "
                    r"Khi dẫn khí $\text{Cl}_2$ vào dung dịch $\text{NaBr}$ dư, xảy ra phản ứng thế: $\text{Cl}_2 + 2\text{NaBr} \rightarrow 2\text{NaCl} + \text{Br}_2$. "
                    r"Ta có $n_{\text{Br}_2} = n_{\text{Cl}_2} = 0,25\text{ mol} \Rightarrow$ khối lượng $\text{Br}_2$ tạo thành là $m_{\text{Br}_2} = 0,25 \times 160 = 40\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Nguyên tử nhóm halogen ($\text{VIIA}$) có cấu hình electron lớp ngoài cùng $ns^2 np^5$; tính oxi hóa đơn chất giảm dần: $\text{F}_2 > \text{Cl}_2 > \text{Br}_2 > \text{I}_2$.",
            r"Nhiệt độ sôi của các hydrogen halide: $\text{HCl} < \text{HBr} < \text{HI} < \text{HF}$ (do $\text{HF}$ có liên kết hydrogen liên phân tử bền vững).",
            r"Tính acid của dung dịch hydrohalic acid tăng dần: $\text{HF} < \text{HCl} < \text{HBr} < \text{HI}$; dung dịch $\text{HF}$ ăn mòn thủy tinh ($\text{SiO}_2$).",
            r"Nhận biết ion halide bằng dung dịch $\text{AgNO}_3$: $\text{F}^-$ không kết tủa, $\text{Cl}^-$ tạo $\text{AgCl}\downarrow$ trắng, $\text{Br}^-$ tạo $\text{AgBr}\downarrow$ vàng nhạt, $\text{I}^-$ tạo $\text{AgI}\downarrow$ vàng đậm.",
        ],
        questions=[
            mcq(
                question=r"Cấu hình electron lớp ngoài cùng chung của nguyên tử các nguyên tố nhóm halogen (nhóm $\text{VIIA}$) ở trạng thái cơ bản là:",
                options=[
                    r"$ns^2 np^4$.",
                    r"$ns^2 np^5$.",
                    r"$ns^2 np^6$.",
                    r"$ns^2 np^3$.",
                ],
                answer="B",
                level="biet",
                solution=(
                    r"Các nguyên tố nhóm halogen thuộc nhóm $\text{VIIA}$ của bảng tuần hoàn, có $7$ electron ở lớp ngoài cùng với cấu hình chung là $ns^2 np^5$."
                ),
            ),
            mcq(
                question=r"Ở điều kiện thường, đơn chất halogen tồn tại ở trạng thái lỏng, có màu nâu đỏ là:",
                options=[
                    r"Fluorine ($\text{F}_2$).",
                    r"Chlorine ($\text{Cl}_2$).",
                    r"Bromine ($\text{Br}_2$).",
                    r"Iodine ($\text{I}_2$).",
                ],
                answer="C",
                level="biet",
                solution=(
                    r"Ở điều kiện thường, $\text{F}_2$ (lục nhạt) và $\text{Cl}_2$ (vàng lục) là chất khí, $\text{Br}_2$ là chất lỏng màu nâu đỏ, còn $\text{I}_2$ là chất rắn màu đen tím."
                ),
            ),
            mcq(
                question=r"Trong dãy các dung dịch hydrohalic acid gồm $\text{HF}, \text{HCl}, \text{HBr}, \text{HI}$ có cùng nồng độ mol, dung dịch có tính acid yếu nhất và có khả năng ăn mòn thủy tinh là:",
                options=[
                    r"Dung dịch $\text{HI}$.",
                    r"Dung dịch $\text{HBr}$.",
                    r"Dung dịch $\text{HCl}$.",
                    r"Dung dịch $\text{HF}$.",
                ],
                answer="D",
                level="biet",
                solution=(
                    r"Trong dãy $\text{HF} < \text{HCl} < \text{HBr} < \text{HI}$, dung dịch hydrofluoric acid ($\text{HF}$) là một acid yếu nhưng có tính chất đặc biệt là phản ứng với $\text{SiO}_2$ trong thủy tinh: $\text{SiO}_2 + 4\text{HF} \rightarrow \text{SiF}_4\uparrow + 2\text{H}_2\text{O}$."
                ),
            ),
            mcq(
                question=r"Nhỏ dung dịch silver nitrate ($\text{AgNO}_3$) dư vào dung dịch nào sau đây thì không thu được kết tủa?",
                options=[
                    r"Dung dịch $\text{NaF}$.",
                    r"Dung dịch $\text{NaCl}$.",
                    r"Dung dịch $\text{NaBr}$.",
                    r"Dung dịch $\text{NaI}$.",
                ],
                answer="A",
                level="biet",
                solution=(
                    r"Khi cho dung dịch $\text{AgNO}_3$ vào dung dịch $\text{NaF}$ thì không tạo kết tủa vì muối silver fluoride ($\text{AgF}$) tan tốt trong nước. "
                    r"Các dung dịch $\text{NaCl}, \text{NaBr}, \text{NaI}$ lần lượt tạo kết tủa $\text{AgCl}$ (trắng), $\text{AgBr}$ (vàng nhạt), $\text{AgI}$ (vàng đậm)."
                ),
            ),
            mcq(
                question=r"Vì sao hợp chất hydrogen fluoride ($\text{HF}$, $M = 20\text{ g/mol}$) lại có nhiệt độ sôi ($19,5^\circ\text{C}$) cao hơn hẳn so với $\text{HCl}$ ($-84,9^\circ\text{C}$), $\text{HBr}$ ($-66,7^\circ\text{C}$) và $\text{HI}$ ($-35,4^\circ\text{C}$)?",
                options=[
                    r"Vì phân tử khối của $\text{HF}$ lớn hơn của $\text{HCl}, \text{HBr}, \text{HI}$.",
                    r"Vì liên kết trong phân tử $\text{HF}$ là liên kết ion điển hình.",
                    r"Vì giữa các phân tử $\text{HF}$ tạo được liên kết hydrogen liên phân tử bền vững ($\dots\text{F}-\text{H}\cdots\text{F}$).",
                    r"Vì tương tác van der Waals giữa các phân tử $\text{HF}$ mạnh hơn so với $\text{HI}$.",
                ],
                answer="C",
                level="hieu",
                solution=(
                    r"Nguyên tử fluorine ($\text{F}$) có bán kính rất nhỏ và độ âm điện lớn nhất ($\chi = 3,98$), nên giữa các phân tử $\text{HF}$ hình thành được liên kết hydrogen liên phân tử rất bền ($\dots\text{F}-\text{H}\cdots\text{F}$), "
                    r"làm nhiệt độ sôi của $\text{HF}$ cao bất thường so với $\text{HCl}, \text{HBr}, \text{HI}$."
                ),
            ),
            mcq(
                question=r"Phản ứng hóa học nào sau đây chứng minh tính oxi hóa của chlorine ($\text{Cl}_2$) mạnh hơn tính oxi hóa của bromine ($\text{Br}_2$)?",
                options=[
                    r"$\text{Cl}_2 + 2\text{NaOH} \rightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$.",
                    r"$\text{Cl}_2 + 2\text{NaBr} \rightarrow 2\text{NaCl} + \text{Br}_2$.",
                    r"$\text{Br}_2 + 2\text{NaI} \rightarrow 2\text{NaBr} + \text{I}_2$.",
                    r"$\text{Cl}_2 + \text{H}_2\text{O} \rightleftharpoons \text{HCl} + \text{HClO}$.",
                ],
                answer="B",
                level="hieu",
                solution=(
                    r"Trong phản ứng $\text{Cl}_2 + 2\text{NaBr} \rightarrow 2\text{NaCl} + \text{Br}_2$, đơn chất $\text{Cl}_2$ đã oxi hóa ion $\text{Br}^-$ thành $\text{Br}_2$ "
                    r"(đẩy được bromine ra khỏi dung dịch muối bromide), chứng tỏ tính oxi hóa của $\text{Cl}_2$ mạnh hơn $\text{Br}_2$."
                ),
            ),
            tf4(
                stem=(
                    r"Xét tính chất vật lý và tính chất hóa học của các đơn chất nhóm halogen ($\text{F}_2, \text{Cl}_2, \text{Br}_2, \text{I}_2$). "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Đi từ $\text{F}_2$ đến $\text{I}_2$, nhiệt độ nóng chảy và nhiệt độ sôi của các đơn chất halogen tăng dần do tương tác van der Waals giữa các phân tử tăng dần.",
                    r"b) Khi dẫn khí fluorine ($\text{F}_2$) vào dung dịch $\text{NaCl}$, xảy ra phản ứng thế tạo ra $\text{NaF}$ và giải phóng khí $\text{Cl}_2$.",
                    r"c) Khi dẫn khí $\text{Cl}_2$ vào dung dịch $\text{NaOH}$ loãng ở nhiệt độ thường, thu được dung dịch nước Javel chứa $\text{NaCl}$ và $\text{NaClO}$ có tính tẩy màu và sát trùng.",
                    r"d) Ở điều kiện thường, đơn chất iodine ($\text{I}_2$) là chất khí màu tím và tác dụng mãnh liệt với khí $\text{H}_2$ gây nổ ngay trong bóng tối.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Từ $\text{F}_2$ đến $\text{I}_2$, khối lượng phân tử và kích thước vỏ electron tăng làm tương tác van der Waals tăng, nên nhiệt độ nóng chảy và nhiệt độ sôi tăng dần. "
                    r"• b) Sai: Khí $\text{F}_2$ có tính oxi hóa quá mạnh nên khi dẫn vào dung dịch $\text{NaCl}$ sẽ phản ứng mãnh liệt ngay với nước: $2\text{F}_2 + 2\text{H}_2\text{O} \rightarrow 4\text{HF} + \text{O}_2\uparrow$, không đẩy được $\text{Cl}_2$ ra khỏi dung dịch muối. "
                    r"• c) Đúng: Phản ứng $\text{Cl}_2 + 2\text{NaOH} \rightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$ tạo ra nước Javel có tính oxi hóa mạnh dùng tẩy trắng và sát trùng. "
                    r"• d) Sai: Ở điều kiện thường $\text{I}_2$ là chất rắn màu đen tím, chỉ phản ứng thuận nghịch với $\text{H}_2$ khi đun nóng ở nhiệt độ cao và có chất xúc tác ($\text{F}_2$ mới là chất nổ mạnh với $\text{H}_2$ ngay trong bóng tối)."
                ),
            ),
            tf4(
                stem=(
                    r"Xét các hợp chất hydrogen halide ($\text{HF}, \text{HCl}, \text{HBr}, \text{HI}$) và các muối halide ($\text{NaF}, \text{NaCl}, \text{NaBr}, \text{NaI}$). "
                    r"Xét tính đúng/sai của các phát biểu sau:"
                ),
                statements=[
                    r"a) Trong dãy dung dịch hydrohalic acid, tính acid tăng dần theo thứ tự $\text{HF} < \text{HCl} < \text{HBr} < \text{HI}$ do độ bền liên kết $\text{H}-\text{X}$ giảm dần.",
                    r"b) Khi cho tinh thể $\text{NaCl}$ rắn tác dụng với dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng, ion $\text{Cl}^-$ khử được $\text{H}_2\text{SO}_4$ đặc tạo thành khí $\text{Cl}_2$ và khí $\text{SO}_2$.",
                    r"c) Khi cho tinh thể $\text{NaBr}$ tác dụng với dung dịch $\text{H}_2\text{SO}_4$ đặc, nóng thì xảy ra phản ứng oxi hóa – khử tạo ra $\text{Br}_2$ và khí $\text{SO}_2$, chứng tỏ tính khử của $\text{Br}^-$ mạnh hơn $\text{Cl}^-$.",
                    r"d) Nhỏ dung dịch $\text{AgNO}_3$ vào dung dịch $\text{NaI}$ thấy xuất hiện kết tủa màu trắng của $\text{AgI}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"• a) Đúng: Từ $\text{HF}$ đến $\text{HI}$, bán kính nguyên tử halogen tăng làm độ dài liên kết $\text{H}-\text{X}$ tăng, năng lượng liên kết giảm nên khả năng phân li ra $\text{H}^+$ trong nước tăng, tính acid tăng dần. "
                    r"• b) Sai: Ion $\text{Cl}^-$ có tính khử yếu nên không khử được $\text{H}_2\text{SO}_4$ đặc; khi đun $\text{NaCl}$ rắn với $\text{H}_2\text{SO}_4$ đặc chỉ xảy ra phản ứng trao đổi tạo khí $\text{HCl}$ ($\text{NaCl} + \text{H}_2\text{SO}_4 \xrightarrow{t^\circ} \text{NaHSO}_4 + \text{HCl}\uparrow$). "
                    r"• c) Đúng: Ion $\text{Br}^-$ có tính khử đủ mạnh để khử $\text{H}_2\text{SO}_4$ đặc thành $\text{SO}_2$ ($2\text{NaBr} + 2\text{H}_2\text{SO}_4 \rightarrow \text{Na}_2\text{SO}_4 + \text{Br}_2 + \text{SO}_2\uparrow + 2\text{H}_2\text{O}$). "
                    r"• d) Sai: Kết tủa $\text{AgI}$ có màu vàng đậm (kết tủa màu trắng là $\text{AgCl}$)."
                ),
            ),
            mcq(
                question=(
                    r"Cho dung dịch chứa $21,3\text{ g}$ hỗn hợp hai muối sodium chloride ($\text{NaCl}$, $M = 58,5\text{ g/mol}$) và sodium bromide ($\text{NaBr}$, $M = 103\text{ g/mol}$) "
                    r"tác dụng vừa đủ với dung dịch silver nitrate ($\text{AgNO}_3$), sau phản ứng thu được $42,55\text{ g}$ hỗn hợp hai kết tủa $\text{AgCl}$ ($M = 143,5\text{ g/mol}$) "
                    r"và $\text{AgBr}$ ($M = 188\text{ g/mol}$). Khối lượng của muối $\text{NaBr}$ trong hỗn hợp ban đầu là:"
                ),
                options=[
                    r"$10,30\text{ g}$.",
                    r"$15,45\text{ g}$.",
                    r"$5,85\text{ g}$.",
                    r"$12,36\text{ g}$.",
                ],
                answer="B",
                level="vandung",
                solution=(
                    r"Gọi số mol của $\text{NaCl}$ và $\text{NaBr}$ trong hỗn hợp lần lượt là $x$ và $y$ ($\text{mol}$). "
                    r"Theo khối lượng hỗn hợp muối ban đầu: $58,5x + 103y = 21,3$ (1). "
                    r"Khi tác dụng với dung dịch $\text{AgNO}_3$ dư, tạo ra $x\text{ mol}$ kết tủa $\text{AgCl}\downarrow$ (trắng) và $y\text{ mol}$ kết tủa $\text{AgBr}\downarrow$ (vàng nhạt): "
                    r"$143,5x + 188y = 42,55$ (2). "
                    r"Giải hệ phương trình (1) và (2) ta được $x = 0,1\text{ mol}$ và $y = 0,15\text{ mol}$. "
                    r"Vậy khối lượng muối $\text{NaBr}$ trong hỗn hợp ban đầu là $m_{\text{NaBr}} = 0,15 \times 103 = 15,45\text{ g}$."
                ),
            ),
            short(
                question=(
                    r"Cho $17,4\text{ g}$ manganese dioxide ($\text{MnO}_2$, $M = 87\text{ g/mol}$) tác dụng hoàn toàn với dung dịch $\text{HCl}$ đặc, dư đun nóng "
                    r"theo phương trình: $\text{MnO}_2 + 4\text{HCl} \xrightarrow{t^\circ} \text{MnCl}_2 + \text{Cl}_2\uparrow + 2\text{H}_2\text{O}$. "
                    r"Dẫn toàn bộ lượng khí $\text{Cl}_2$ sinh ra vào $500\text{ mL}$ dung dịch $\text{NaOH}$ $1\text{ M}$ ở nhiệt độ thường. "
                    r"Tính tổng khối lượng (theo đơn vị gam) của hai muối $\text{NaCl}$ ($M = 58,5\text{ g/mol}$) và $\text{NaClO}$ ($M = 74,5\text{ g/mol}$) tạo thành trong dung dịch sau phản ứng."
                ),
                answer=["26,6", "26.6"],
                level="vandung",
                solution=(
                    r"Số mol $\text{MnO}_2$ phản ứng là $n_{\text{MnO}_2} = \dfrac{17,4}{87} = 0,2\text{ mol} \Rightarrow n_{\text{Cl}_2} = n_{\text{MnO}_2} = 0,2\text{ mol}$. "
                    r"Số mol $\text{NaOH}$ trong dung dịch là $n_{\text{NaOH}} = 0,5 \times 1 = 0,5\text{ mol}$. "
                    r"Phương trình phản ứng tạo nước Javel: $\text{Cl}_2 + 2\text{NaOH} \rightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$. "
                    r"Vì $\dfrac{n_{\text{Cl}_2}}{1} = 0,2 < \dfrac{n_{\text{NaOH}}}{2} = 0,25$ nên $\text{Cl}_2$ phản ứng hết, $\text{NaOH}$ còn dư: "
                    r"$n_{\text{NaCl}} = n_{\text{NaClO}} = n_{\text{Cl}_2} = 0,2\text{ mol}$. "
                    r"Vậy tổng khối lượng hai muối tạo thành là $m = 0,2 \times 58,5 + 0,2 \times 74,5 = 11,7 + 14,9 = 26,6\text{ g}$."
                ),
            ),
        ],
        description="Tìm hiểu vị trí, cấu hình electron, tính chất vật lý, tính chất hóa học và điều chế các đơn chất nhóm halogen (nhóm VIIA), cùng tính chất của các hydrogen halide, hydrohalic acid và cách nhận biết các ion halide.",
    ),
]


LESSONS = LESSONS_GRADE_10
