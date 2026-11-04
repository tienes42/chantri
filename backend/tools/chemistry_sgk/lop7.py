from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_7: list[dict[str, Any]] = [
    lesson(
        grade=7,
        order=1,
        code="H7-C01",
        title="Chương 1: Nguyên tử và cấu tạo nguyên tử",
        topic="nguyen-tu",
        summary=(
            r"Nguyên tử là hạt vô cùng nhỏ và trung hòa về điện, cấu tạo nên mọi chất. "
            r"Theo mô hình nguyên tử Rutherford – Bohr, nguyên tử gồm hạt nhân ở tâm (chứa hạt proton $p$ mang điện tích $+1$ và hạt neutron $n$ không mang điện) "
            r"và vỏ nguyên tử gồm các hạt electron ($e$ mang điện tích $-1$) chuyển động trên các lớp xác định xung quanh hạt nhân. "
            r"Vì nguyên tử trung hòa điện nên luôn có $Z = p = e$; khối lượng nguyên tử tập trung hầu hết ở hạt nhân và được tính theo đơn vị $\text{amu}$ với $A \approx p + n$."
        ),
        objectives=[
            r"Trình bày được mô hình nguyên tử của Rutherford – Bohr (hạt nhân ở tâm và các electron chuyển động trên các lớp vỏ đồng tâm quanh hạt nhân).",
            r"Nêu được thành phần cấu tạo nguyên tử gồm 3 loại hạt cơ bản: proton ($p$, điện tích $+1$, khối lượng $\approx 1\text{ amu}$), neutron ($n$, điện tích $0$, khối lượng $\approx 1\text{ amu}$) và electron ($e$, điện tích $-1$, khối lượng $\approx 0{,}00055\text{ amu}$).",
            r"Giải thích được vì sao nguyên tử trung hòa về điện ($p = e = Z$) và vì sao khối lượng nguyên tử tập trung hầu hết ở hạt nhân ($A \approx p + n\text{ amu}$).",
            r"Xác định được sự phân bố electron trên các lớp vỏ (lớp 1 tối đa $2e$, lớp 2 tối đa $8e$) và giải được bài toán tìm số hạt $p, n, e$ của nguyên tử.",
        ],
        formulas=[
            {
                "name": "Điều kiện trung hòa điện của nguyên tử",
                "formula": r"$Z = p = e$",
                "note": r"$Z$ là số đơn vị điện tích hạt nhân, $p$ là số hạt proton (điện tích $+1$), $e$ là số hạt electron (điện tích $-1$).",
            },
            {
                "name": "Khối lượng nguyên tử theo đơn vị amu và tổng số hạt",
                "formula": r"$A \approx p + n \text{ (amu)}; \quad S = p + n + e = 2p + n$",
                "note": r"Do khối lượng $1\text{ hạt }e \approx 0{,}00055\text{ amu} \ll 1\text{ amu}$ nên khối lượng nguyên tử xấp xỉ bằng tổng khối lượng proton và neutron trong hạt nhân.",
            },
            {
                "name": "Ký hiệu nguyên tử và quy tắc xếp electron vào lớp vỏ",
                "formula": r"${}_Z^A\text{X}; \quad \text{Lớp 1 tối đa } 2e, \text{ Lớp 2 tối đa } 8e$",
                "note": r"Ví dụ nguyên tử sodium ${}_{11}^{23}\text{Na}$ có $p = e = 11$, $n = 23 - 11 = 12$, phân bố electron theo $3$ lớp là $2, 8, 1$.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Mô hình nguyên tử Rutherford – Bohr và các hạt cấu tạo",
                "content": (
                    r"- **Nguyên tử** là hạt vô cùng nhỏ, trung hòa về điện, cấu tạo nên các chất." "\n"
                    r"- Theo **mô hình Rutherford – Bohr**, nguyên tử gồm hai phần chính:" "\n"
                    r"  1. **Hạt nhân nguyên tử** nằm ở tâm, mang điện tích dương, được tạo bởi hai loại hạt là **proton** (ký hiệu $p$, mang điện tích $+1$, khối lượng xấp xỉ $1\text{ amu}$) và **neutron** (ký hiệu $n$, không mang điện, khối lượng xấp xỉ $1\text{ amu}$). Lưu ý: nguyên tử nhẹ nhất là hydrogen (${}_1^1\text{H}$) hạt nhân chỉ có $1$ hạt proton và không có neutron ($n = 0$)." "\n"
                    r"  2. **Vỏ nguyên tử** gồm một hay nhiều **electron** (ký hiệu $e$, mang điện tích $-1$, khối lượng rất nhỏ chỉ khoảng $0{,}00055\text{ amu}$) chuyển động rất nhanh xung quanh hạt nhân và sắp xếp thành từng lớp."
                ),
            },
            {
                "title": "2. Điện tích hạt nhân và lớp vỏ electron",
                "content": (
                    r"- **Điện tích hạt nhân**: Nếu hạt nhân có $Z$ hạt proton thì điện tích của hạt nhân là $+Z$, và số đơn vị điện tích hạt nhân bằng $Z$." "\n"
                    r"- Vì nguyên tử luôn **trung hòa về điện**, tổng điện tích dương của proton bằng độ lớn tổng điện tích âm của electron, nghĩa là trong mọi nguyên tử:" "\n"
                    r"$$\text{Số đơn vị điện tích hạt nhân } (Z) = \text{Số hạt proton } (p) = \text{Số hạt electron } (e)$$" "\n"
                    r"- **Sự sắp xếp electron trên các lớp vỏ**: Các electron sắp xếp vào các lớp theo thứ tự từ gần hạt nhân ra ngoài:" "\n"
                    r"  + **Lớp thứ nhất** (trong cùng, sát hạt nhân nhất) chứa tối đa **$2\text{ electron}$**." "\n"
                    r"  + **Lớp thứ hai** chứa tối đa **$8\text{ electron}$**." "\n"
                    r"  + **Lớp thứ ba** (đối với $20$ nguyên tố đầu tiên có $Z \le 20$) chứa tối đa **$8\text{ electron}$** ở lớp ngoài cùng."
                ),
            },
            {
                "title": "3. Khối lượng nguyên tử",
                "content": (
                    r"- Vì khối lượng của nguyên tử vô cùng nhỏ nếu tính bằng gam ($\text{g}$) hay kilôgam ($\text{kg}$), khoa học sử dụng **đơn vị khối lượng nguyên tử**, ký hiệu là **$\text{amu}$** ($1\text{ amu}$ bằng $\dfrac{1}{12}$ khối lượng của một nguyên tử carbon ${}_6^{12}\text{C}$, xấp xỉ $1{,}6605 \cdot 10^{-24}\text{ g}$)." "\n"
                    r"- Do khối lượng của electron rất nhỏ ($m_e \approx 0{,}00055\text{ amu}$) không đáng kể so với khối lượng của proton ($m_p \approx 1\text{ amu}$) và neutron ($m_n \approx 1\text{ amu}$), nên **khối lượng nguyên tử tập trung hầu hết ở hạt nhân** và được tính gần đúng bằng tổng số hạt proton và số hạt neutron theo đơn vị $\text{amu}$:" "\n"
                    r"$$m_{\text{nguyên tử}} \approx p + n \text{ (amu)}$$"
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Xác định cấu tạo nguyên tử và phân bố lớp electron",
                "problem": (
                    r"Nguyên tử aluminium ($\text{Al}$) có số đơn vị điện tích hạt nhân là $Z = 13$ và số hạt neutron trong hạt nhân là $n = 14$. "
                    r"Hãy xác định số hạt proton ($p$), số hạt electron ($e$), khối lượng nguyên tử theo $\text{amu}$, số lớp electron và số electron ở lớp ngoài cùng của nguyên tử $\text{Al}$."
                ),
                "solution": (
                    r"- Trong nguyên tử trung hòa điện: $p = e = Z = 13$ (có $13$ proton và $13$ electron)." "\n"
                    r"- Khối lượng nguyên tử aluminium theo đơn vị $\text{amu}$ là: $A \approx p + n = 13 + 14 = 27\text{ amu}$." "\n"
                    r"- Phân bố $13\text{ electron}$ vào các lớp từ trong ra ngoài: lớp 1 có $2e$, lớp 2 có $8e$, còn lại lớp 3 (lớp ngoài cùng) có $13 - 2 - 8 = 3e$. "
                    r"Vậy nguyên tử $\text{Al}$ có **$3$ lớp electron** và có **$3\text{ electron}$ ở lớp ngoài cùng**."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán tổng số hạt cơ bản trong nguyên tử",
                "problem": (
                    r"Tổng số hạt cơ bản (proton, neutron, electron) trong một nguyên tử nguyên tố $\text{X}$ là $34$, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là $10$ hạt. "
                    r"Tìm số hạt $p, n, e$ và khối lượng nguyên tử của $\text{X}$ theo đơn vị $\text{amu}$."
                ),
                "solution": (
                    r"- Trong nguyên tử $\text{X}$, các hạt mang điện là proton ($p$) và electron ($e$) với $p = e \Rightarrow$ tổng số hạt mang điện là $p + e = 2p$; hạt không mang điện là neutron ($n$)." "\n"
                    r"- Theo đề bài ta có hệ thức:" "\n"
                    r"$$\begin{cases} 2p + n = 34 \\ 2p - n = 10 \end{cases} \Rightarrow 4p = 44 \Rightarrow p = e = 11; \quad n = 34 - 22 = 12$$" "\n"
                    r"- Khối lượng nguyên tử của $\text{X}$ là $A \approx p + n = 11 + 12 = 23\text{ amu}$ ($\text{X}$ là nguyên tử sodium ${}_{11}^{23}\text{Na}$)."
                ),
            },
        ],
        key_takeaways=[
            r"Hạt nhân nguyên tử gồm proton ($p$, điện tích $+1$) và neutron ($n$, không mang điện); vỏ nguyên tử gồm các electron ($e$, điện tích $-1$).",
            r"Nguyên tử trung hòa về điện nên luôn có $Z = p = e$; khối lượng nguyên tử tập trung ở hạt nhân với $A \approx p + n\text{ (amu)}$.",
            r"Các electron xếp vào các lớp từ gần hạt nhân ra ngoài: lớp 1 tối đa $2e$, lớp 2 tối đa $8e$.",
        ],
        questions=[
            mcq(
                r"Trong nguyên tử, loại hạt cơ bản nào mang điện tích âm ($-1$) và chuyển động xung quanh hạt nhân?",
                [
                    r"Hạt electron ($e$).",
                    r"Hạt proton ($p$).",
                    r"Hạt neutron ($n$).",
                    r"Hạt nhân nguyên tử.",
                ],
                "A",
                "biet",
                r"Hạt electron ($e$) mang điện tích âm ($-1$) tạo nên lớp vỏ nguyên tử và chuyển động xung quanh hạt nhân. Hạt proton ($p$) mang điện tích $+1$, còn hạt neutron ($n$) không mang điện.",
            ),
            mcq(
                r"Thành phần cấu tạo của hạt nhân ở hầu hết các nguyên tử (trừ đồng vị ${}_1^1\text{H}$) gồm có:",
                [
                    r"Chỉ có duy nhất các hạt electron ($e$).",
                    r"Hạt proton ($p$) và hạt neutron ($n$).",
                    r"Hạt proton ($p$) và hạt electron ($e$).",
                    r"Hạt neutron ($n$) và hạt electron ($e$).",
                ],
                "B",
                "biet",
                r"Hạt nhân nguyên tử nằm ở tâm nguyên tử, được cấu tạo bởi các hạt proton ($p$, mang điện $+1$) và các hạt neutron ($n$, không mang điện).",
            ),
            mcq(
                r"Vì sao nói khối lượng của hạt nhân được coi là khối lượng của cả nguyên tử?",
                [
                    r"Vì hạt electron ($e$) có khối lượng lớn gấp $1836$ lần hạt proton ($p$).",
                    r"Vì hạt neutron ($n$) nằm ở lớp vỏ ngoài cùng của nguyên tử.",
                    r"Vì khối lượng của các hạt electron ($e$) ở lớp vỏ vô cùng nhỏ (chỉ khoảng $0{,}00055\text{ amu}$), không đáng kể so với khối lượng của proton và neutron.",
                    r"Vì trong nguyên tử không có hạt electron ($e$) nào ở lớp vỏ.",
                ],
                "C",
                "biet",
                r"Mỗi hạt proton ($p$) hoặc neutron ($n$) trong hạt nhân có khối lượng xấp xỉ $1\text{ amu}$, trong khi mỗi hạt electron ($e$) chỉ nặng khoảng $0{,}00055\text{ amu}$ (nhỏ hơn gần $2000$ lần), nên khối lượng nguyên tử tập trung hầu hết ở hạt nhân.",
            ),
            mcq(
                r"Theo mô hình nguyên tử Rutherford – Bohr, lớp electron thứ nhất (lớp trong cùng sát hạt nhân nhất) và lớp electron thứ hai chứa tối đa lần lượt bao nhiêu electron?",
                [
                    r"Lớp thứ nhất tối đa $8\text{ electron}$, lớp thứ hai tối đa $2\text{ electron}$.",
                    r"Lớp thứ nhất tối đa $4\text{ electron}$, lớp thứ hai tối đa $4\text{ electron}$.",
                    r"Lớp thứ nhất tối đa $2\text{ electron}$, lớp thứ hai tối đa $18\text{ electron}$.",
                    r"Lớp thứ nhất tối đa $2\text{ electron}$, lớp thứ hai tối đa $8\text{ electron}$.",
                ],
                "D",
                "biet",
                r"Theo quy tắc phân bố electron trong mô hình Rutherford – Bohr: lớp thứ nhất (lớp $K$) chứa tối đa $2\text{ electron}$, lớp thứ hai (lớp $L$) chứa tối đa $8\text{ electron}$.",
            ),
            mcq(
                r"Nguyên tử oxygen ($\text{O}$) có điện tích hạt nhân là $+8$. Khi xếp các electron vào lớp vỏ theo mô hình Rutherford – Bohr, số lớp electron và số electron ở lớp ngoài cùng của nguyên tử oxygen lần lượt là:",
                [
                    r"$2$ lớp electron và $6\text{ electron}$ ở lớp ngoài cùng.",
                    r"$2$ lớp electron và $8\text{ electron}$ ở lớp ngoài cùng.",
                    r"$3$ lớp electron và $2\text{ electron}$ ở lớp ngoài cùng.",
                    r"$1$ lớp electron và $8\text{ electron}$ ở lớp ngoài cùng.",
                ],
                "A",
                "hieu",
                r"Nguyên tử oxygen ($\text{O}$) có $Z = p = e = 8\text{ electron}$. Lớp thứ nhất chứa tối đa $2\text{ electron}$, còn lại $8 - 2 = 6\text{ electron}$ xếp vào lớp thứ hai (lớp ngoài cùng). Vậy nguyên tử $\text{O}$ có $2$ lớp electron và $6\text{ electron}$ lớp ngoài cùng.",
            ),
            mcq(
                r"Nguyên tử calcium ($\text{Ca}$) có $20$ proton và $20$ neutron trong hạt nhân. Khối lượng nguyên tử $\text{Ca}$ (theo $\text{amu}$) và tổng số hạt cơ bản ($p + n + e$) trong một nguyên tử $\text{Ca}$ lần lượt là:",
                [
                    r"$60\text{ amu}$ và $40$ hạt.",
                    r"$40\text{ amu}$ và $60$ hạt.",
                    r"$40\text{ amu}$ và $40$ hạt.",
                    r"$20\text{ amu}$ và $60$ hạt.",
                ],
                "B",
                "hieu",
                r"Ta có $p = e = 20$ và $n = 20$. Khối lượng nguyên tử $\text{Ca}$ là $A \approx p + n = 20 + 20 = 40\text{ amu}$. Tổng số hạt cơ bản ($p + n + e$) trong nguyên tử $\text{Ca}$ là $20 + 20 + 20 = 60$ hạt.",
            ),
            tf4(
                r"Cho nguyên tử phosphorus ($\text{P}$) có số đơn vị điện tích hạt nhân là $Z = 15$ và số hạt neutron trong hạt nhân là $n = 16$. Xét tính đúng/sai của các phát biểu sau về nguyên tử phosphorus:",
                [
                    r"Trong một nguyên tử phosphorus ($\text{P}$) có đúng $15$ hạt proton và $15$ hạt electron.",
                    r"Tổng số hạt mang điện trong một nguyên tử phosphorus ($\text{P}$) là $15$ hạt.",
                    r"Khối lượng nguyên tử của phosphorus ($\text{P}$) tính theo đơn vị khối lượng nguyên tử là $31\text{ amu}$.",
                    r"Các electron của nguyên tử phosphorus ($\text{P}$) được phân bố trên $3$ lớp electron (với số electron từng lớp từ trong ra ngoài là $2, 8, 5$).",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Nguyên tử trung hòa điện nên $p = e = Z = 15$." "\n"
                    r"- **Ý b) Sai**: Các hạt mang điện trong nguyên tử gồm cả proton ($+1$) và electron ($-1$), nên tổng số hạt mang điện là $p + e = 15 + 15 = 30$ hạt (không phải $15$ hạt)." "\n"
                    r"- **Ý c) Đúng**: Khối lượng nguyên tử $A \approx p + n = 15 + 16 = 31\text{ amu}$." "\n"
                    r"- **Ý d) Đúng**: Với $15\text{ electron}$, lớp 1 có $2e$, lớp 2 có $8e$, lớp 3 có $15 - 2 - 8 = 5e$ $\rightarrow$ có $3$ lớp electron ($2, 8, 5$)."
                ),
            ),
            tf4(
                r"Xét cấu tạo của ba nguyên tử: Hydrogen (${}_1^1\text{H}$), Carbon (${}_6^{12}\text{C}$) và Magnesium (${}_{12}^{24}\text{Mg}$). Các nhận định sau đây là đúng hay sai?",
                [
                    r"Hạt nhân của nguyên tử hydrogen (${}_1^1\text{H}$) chỉ có $1$ hạt proton và không có hạt neutron nào ($n = 0$).",
                    r"Trong nguyên tử carbon (${}_6^{12}\text{C}$), số hạt proton bằng số hạt neutron và bằng số hạt electron (đều bằng $6$).",
                    r"Nguyên tử magnesium (${}_{12}^{24}\text{Mg}$) có khối lượng nguyên tử gấp đôi khối lượng nguyên tử carbon (${}_6^{12}\text{C}$).",
                    r"Ở lớp electron ngoài cùng, nguyên tử carbon (${}_6^{12}\text{C}$) có $6\text{ electron}$ và nguyên tử magnesium (${}_{12}^{24}\text{Mg}$) có $4\text{ electron}$.",
                ],
                "Đ/Đ/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Với ${}_1^1\text{H}$, ta có $p = 1$, $A = p + n = 1 \Rightarrow n = 1 - 1 = 0$." "\n"
                    r"- **Ý b) Đúng**: Với ${}_6^{12}\text{C}$, ta có $p = e = 6$ và $n = 12 - 6 = 6$." "\n"
                    r"- **Ý c) Đúng**: Khối lượng nguyên tử của ${}_{12}^{24}\text{Mg}$ là $24\text{ amu}$, gấp $2$ lần khối lượng nguyên tử của ${}_6^{12}\text{C}$ ($12\text{ amu}$)." "\n"
                    r"- **Ý d) Sai**: Nguyên tử ${}_6^{12}\text{C}$ ($6e$: phân bố $2, 4$) có **$4\text{ electron}$** lớp ngoài cùng; nguyên tử ${}_{12}^{24}\text{Mg}$ ($12e$: phân bố $2, 8, 2$) có **$2\text{ electron}$** lớp ngoài cùng."
                ),
            ),
            mcq(
                r"Một nguyên tử của nguyên tố $\text{X}$ có tổng số hạt cơ bản ($p, n, e$) là $40$ hạt, trong đó tổng số hạt mang điện nhiều hơn số hạt không mang điện là $12$ hạt. Điện tích hạt nhân và khối lượng nguyên tử của $\text{X}$ lần lượt là:",
                [
                    r"$+14$ và $28\text{ amu}$ (nguyên tử silicon $\text{Si}$).",
                    r"$+11$ và $23\text{ amu}$ (nguyên tử sodium $\text{Na}$).",
                    r"$+13$ và $27\text{ amu}$ (nguyên tử aluminium $\text{Al}$).",
                    r"$+12$ và $24\text{ amu}$ (nguyên tử magnesium $\text{Mg}$).",
                ],
                "C",
                "vandung",
                r"Gọi số hạt proton, neutron, electron của $\text{X}$ là $p, n, e$ (với $p = e$). Tổng số hạt là $2p + n = 40$; số hạt mang điện nhiều hơn không mang điện là $2p - n = 12$. Cộng hai phương trình được $4p = 52 \Rightarrow p = e = 13$ và $n = 40 - 26 = 14$. Vậy điện tích hạt nhân là $+13$ và khối lượng nguyên tử là $A \approx p + n = 13 + 14 = 27\text{ amu}$.",
            ),
            short(
                r"Tổng số hạt cơ bản (proton, neutron và electron) trong một nguyên tử nguyên tố $\text{R}$ là $52$ hạt, trong đó số hạt không mang điện (neutron) là $18$ hạt. Hãy tính khối lượng nguyên tử của $\text{R}$ theo đơn vị $\text{amu}$ (làm tròn đến hàng đơn vị).",
                ["35", "35,0", "35.0"],
                "vandung",
                (
                    r"Ta có tổng số hạt cơ bản trong nguyên tử $\text{R}$ là $S = p + n + e = 2p + n = 52$." "\n"
                    r"Vì số hạt không mang điện là $n = 18$, ta tìm được số hạt proton:" "\n"
                    r"$$2p = 52 - 18 = 34 \Rightarrow p = e = 17$$" "\n"
                    r"Khối lượng nguyên tử của $\text{R}$ (chlorine ${}_{17}^{35}\text{Cl}$) theo đơn vị $\text{amu}$ là:" "\n"
                    r"$$A \approx p + n = 17 + 18 = 35\text{ amu}$$"
                ),
            ),
        ],
        description="Mô hình nguyên tử Rutherford - Bohr, hạt nhân gồm proton và neutron, vỏ electron, điện tích hạt nhân và khối lượng nguyên tử.",
    ),
    lesson(
        grade=7,
        order=2,
        code="H7-C02",
        title="Chương 2: Nguyên tố hóa học và sơ lược bảng tuần hoàn",
        topic="nguyen-to-hoa-hoc",
        summary=(
            r"Nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có cùng số hạt proton ($Z$) trong hạt nhân. "
            r"Mỗi nguyên tố hóa học được biểu diễn bằng một ký hiệu hóa học quốc tế và tên gọi theo chuẩn IUPAC (như hydrogen $\text{H}$, oxygen $\text{O}$, sodium $\text{Na}$, iron $\text{Fe}$, copper $\text{Cu}$). "
            r"Trong bảng tuần hoàn các nguyên tố hóa học, các nguyên tố được sắp xếp theo chiều tăng dần của điện tích hạt nhân nguyên tử vào các ô nguyên tố, các chu kỳ (hàng ngang) và các nhóm (cột dọc), giúp phân loại rõ nguyên tố kim loại, phi kim và khí hiếm."
        ),
        objectives=[
            r"Nêu được khái niệm nguyên tố hóa học và giải thích vì sao số hạt proton ($Z$) là đặc trưng quyết định một nguyên tố hóa học.",
            r"Viết đúng ký hiệu hóa học và đọc tên quốc tế IUPAC của 20 nguyên tố đầu tiên ($Z = 1 \rightarrow 20$) và các kim loại thông dụng ($\text{Fe}$, $\text{Cu}$, $\text{Zn}$, $\text{Ag}$, $\text{Au}$).",
            r"Trình bày được nguyên tắc sắp xếp bảng tuần hoàn và cấu tạo bảng tuần hoàn gồm ô nguyên tố, chu kỳ ($7$ chu kỳ) và nhóm ($8$ nhóm A, $8$ nhóm B).",
            r"Xác định được mối liên hệ giữa vị trí nguyên tố (số thứ tự ô, chu kỳ, nhóm A) với cấu tạo nguyên tử và phân biệt được nguyên tố kim loại, phi kim, khí hiếm.",
        ],
        formulas=[
            {
                "name": "Quan hệ giữa vị trí trong bảng tuần hoàn và cấu tạo nguyên tử (Nhóm A)",
                "formula": r"$\text{Số thứ tự ô} = Z = p = e; \quad \text{Số thứ tự chu kỳ} = \text{Số lớp } e; \quad \text{Số thứ tự nhóm A} = \text{Số } e \text{ lớp ngoài cùng}$",
                "note": r"Ví dụ: $\text{Mg}$ ($Z = 12$, phân bố $2, 8, 2$) nằm ở ô số $12$, chu kỳ $3$ ($3$ lớp $e$), nhóm $\text{IIA}$ ($2e$ lớp ngoài cùng).",
            },
            {
                "name": "20 nguyên tố hóa học đầu tiên theo chiều tăng dần điện tích hạt nhân Z",
                "formula": r"$Z=1\text{..}10: \text{H, He, Li, Be, B, C, N, O, F, Ne} \quad \mid \quad Z=11\text{..}20: \text{Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca}$",
                "note": r"Ký hiệu hóa học gồm 1 hoặc 2 chữ cái, trong đó chữ cái đầu luôn viết IN HOA, chữ cái thứ hai (nếu có) viết thường.",
            },
            {
                "name": "Phân loại nguyên tố theo số electron lớp ngoài cùng (chu kỳ nhỏ)",
                "formula": r"$\text{Kim loại: } 1, 2, 3e \text{ (trừ H, He, B)} \quad \mid \quad \text{Phi kim: } 5, 6, 7e \text{ (và H, B, C, Si)} \quad \mid \quad \text{Khí hiếm: } 8e \text{ (He có } 2e\text{)}$",
                "note": r"Các nguyên tố khí hiếm nhóm $\text{VIIIA}$ ($\text{He}, \text{Ne}, \text{Ar}...$) có lớp vỏ ngoài cùng bền vững nên rất trơ về mặt hóa học.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Nguyên tố hóa học và ký hiệu hóa học chuẩn IUPAC",
                "content": (
                    r"- **Nguyên tố hóa học** là tập hợp những nguyên tử cùng loại, có **cùng số proton ($p$)** trong hạt nhân. Do đó, số proton (số đơn vị điện tích hạt nhân $Z$) là số hiệu nguyên tử đặc trưng cho một nguyên tố hóa học (mọi nguyên tử thuộc cùng một nguyên tố hóa học đều có tính chất hóa học giống nhau)." "\n"
                    r"- **Ký hiệu hóa học**: Biểu diễn bằng 1 hoặc 2 chữ cái (chữ cái đầu viết in hoa, chữ cái sau viết thường). Mỗi ký hiệu vừa chỉ nguyên tố đó, vừa chỉ **một nguyên tử** của nguyên tố đó." "\n"
                    r"- **Tên gọi chuẩn IUPAC của các nguyên tố quan trọng**:" "\n"
                    r"  + $Z = 1 \rightarrow 10$: $\text{H}$ (Hydrogen), $\text{He}$ (Helium), $\text{Li}$ (Lithium), $\text{Be}$ (Beryllium), $\text{B}$ (Boron), $\text{C}$ (Carbon), $\text{N}$ (Nitrogen), $\text{O}$ (Oxygen), $\text{F}$ (Fluorine), $\text{Ne}$ (Neon)." "\n"
                    r"  + $Z = 11 \rightarrow 20$: $\text{Na}$ (Sodium - natri), $\text{Mg}$ (Magnesium), $\text{Al}$ (Aluminium - nhôm), $\text{Si}$ (Silicon), $\text{P}$ (Phosphorus), $\text{S}$ (Sulfur - lưu huỳnh), $\text{Cl}$ (Chlorine), $\text{Ar}$ (Argon), $\text{K}$ (Potassium - kali), $\text{Ca}$ (Calcium)." "\n"
                    r"  + Một số kim loại thông dụng khác: $\text{Fe}$ (Iron - sắt, $Z = 26$), $\text{Cu}$ (Copper - đồng, $Z = 29$), $\text{Zn}$ (Zinc - kẽm, $Z = 30$), $\text{Ag}$ (Silver - bạc, $Z = 47$)."
                ),
            },
            {
                "title": "2. Nguyên tắc sắp xếp và cấu tạo bảng tuần hoàn",
                "content": (
                    r"- **Nguyên tắc sắp xếp**: Các nguyên tố trong bảng tuần hoàn được sắp xếp theo chiều **tăng dần của điện tích hạt nhân nguyên tử ($Z$)**; các nguyên tố có cùng số lớp electron trong nguyên tử được xếp thành một hàng ngang (chu kỳ); các nguyên tố có tính chất hóa học tương tự nhau (cùng số electron hóa trị/lớp ngoài cùng đối với nhóm A) được xếp thành một cột dọc (nhóm)." "\n"
                    r"- **Ô nguyên tố**: Mỗi nguyên tố chiếm 1 ô. Số thứ tự của ô nguyên tố bằng đúng **số hiệu nguyên tử $Z = p = e$**. Trong ô nguyên tố cho biết: số hiệu nguyên tử $Z$, ký hiệu hóa học, tên nguyên tố và khối lượng nguyên tử." "\n"
                    r"- **Chu kỳ**: Là dãy các nguyên tố mà nguyên tử của chúng có **cùng số lớp electron**, được xếp theo chiều điện tích hạt nhân tăng dần từ trái sang phải. Bảng tuần hoàn có $7$ chu kỳ (chu kỳ $1, 2, 3$ là chu kỳ nhỏ; chu kỳ $4, 5, 6, 7$ là chu kỳ lớn). **Số thứ tự của chu kỳ bằng số lớp electron**." "\n"
                    r"- **Nhóm**: Là cột dọc gồm các nguyên tố có cấu hình electron ngoài cùng tương tự nhau nên có tính chất hóa học gần giống nhau. Đối với các nguyên tố **nhóm A** (từ $\text{IA}$ đến $\text{VIIIA}$): **Số thứ tự của nhóm A bằng số electron ở lớp ngoài cùng** (riêng $\text{He}$ có $2e$ lớp ngoài cùng nhưng xếp vào nhóm khí hiếm $\text{VIIIA}$)."
                ),
            },
            {
                "title": "3. Phân loại nguyên tố: Kim loại, phi kim và khí hiếm",
                "content": (
                    r"- **Các nguyên tố kim loại** (chiếm hơn $80\%$ tổng số nguyên tố trong bảng tuần hoàn, như $\text{Na}$, $\text{K}$, $\text{Mg}$, $\text{Ca}$, $\text{Al}$, $\text{Fe}$, $\text{Cu}$): Nằm ở phía bên trái (nhóm $\text{IA}$ trừ $\text{H}$, nhóm $\text{IIA}$, $\text{IIIA}$ trừ $\text{B}$) và khu vực giữa/dưới bảng tuần hoàn (các nhóm B); thường có $1, 2, 3\text{ electron}$ ở lớp ngoài cùng, dẫn điện và dẫn nhiệt tốt." "\n"
                    r"- **Các nguyên tố phi kim** (như $\text{H}$, $\text{C}$, $\text{N}$, $\text{O}$, $\text{F}$, $\text{P}$, $\text{S}$, $\text{Cl}$): Nằm ở phía trên bên phải bảng tuần hoàn (nhóm $\text{IVA}, \text{VA}, \text{VIA}, \text{VIIA}$, riêng $\text{H}$ nằm ở nhóm $\text{IA}$); thường có $5, 6, 7\text{ electron}$ lớp ngoài cùng (hoặc $4e$ với $\text{C}, \text{Si}$)." "\n"
                    r"- **Các nguyên tố khí hiếm** ($\text{He}$, $\text{Ne}$, $\text{Ar}$, $\text{Kr}$, $\text{Xe}$, $\text{Rn}$): Nằm ở cột cuối cùng bên phải (nhóm $\text{VIIIA}$), có lớp vỏ ngoài cùng bền vững ($8\text{ electron}$, riêng $\text{He}$ có $2\text{ electron}$), tồn tại trong tự nhiên dưới dạng các nguyên tử độc lập và rất khó tham gia phản ứng hóa học."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Từ vị trí trong bảng tuần hoàn suy ra cấu tạo nguyên tử",
                "problem": (
                    r"Nguyên tố chlorine ($\text{Cl}$) nằm ở ô số $17$, chu kỳ $3$, nhóm $\text{VIIA}$ trong bảng tuần hoàn. "
                    r"Hãy xác định số hạt proton, số hạt electron, số lớp electron, số electron lớp ngoài cùng và cho biết $\text{Cl}$ là kim loại, phi kim hay khí hiếm."
                ),
                "solution": (
                    r"- Vì $\text{Cl}$ ở ô số $17 \Rightarrow Z = p = e = 17$ (nguyên tử có $17$ proton và $17$ electron)." "\n"
                    r"- Vì $\text{Cl}$ ở chu kỳ $3 \Rightarrow$ nguyên tử có **$3$ lớp electron**." "\n"
                    r"- Vì $\text{Cl}$ ở nhóm $\text{VIIA} \Rightarrow$ nguyên tử có **$7\text{ electron}$ ở lớp ngoài cùng** (sự phân bố electron trên $3$ lớp là $2, 8, 7$)." "\n"
                    r"- Có $7\text{ electron}$ lớp ngoài cùng và nằm ở nhóm $\text{VIIA}$ (góc trên bên phải bảng tuần hoàn) nên chlorine ($\text{Cl}$) là một **nguyên tố phi kim** điển hình."
                ),
            },
            {
                "title": "Ví dụ 2: Từ cấu tạo nguyên tử xác định vị trí trong bảng tuần hoàn",
                "problem": (
                    r"Nguyên tử của nguyên tố $\text{X}$ có $3$ lớp electron và có $2\text{ electron}$ ở lớp ngoài cùng. "
                    r"Hãy xác định vị trí (ô, chu kỳ, nhóm) của $\text{X}$ trong bảng tuần hoàn và gọi tên nguyên tố $\text{X}$ theo danh pháp IUPAC."
                ),
                "solution": (
                    r"- Nguyên tử $\text{X}$ có $3$ lớp electron nên lớp 1 và lớp 2 đã bão hòa với lần lượt $2e$ và $8e$; lớp 3 (ngoài cùng) có $2e$." "\n"
                    r"- Tổng số electron của nguyên tử $\text{X}$ là: $e = p = Z = 2 + 8 + 2 = 12$." "\n"
                    r"- Vậy $\text{X}$ nằm ở **ô số $12$, chu kỳ $3$, nhóm $\text{IIA}$**, chính là nguyên tố kim loại **magnesium** ($\text{Mg}$)."
                ),
            },
        ],
        key_takeaways=[
            r"Các nguyên tử thuộc cùng một nguyên tố hóa học đều có cùng số hạt proton ($p = Z$) trong hạt nhân.",
            r"Trong bảng tuần hoàn: Số thứ tự ô $= Z = p = e$; Số thứ tự chu kỳ $=$ số lớp electron; Số thứ tự nhóm A $=$ số electron lớp ngoài cùng (trừ $\text{He}$).",
            r"Kim loại nằm ở bên trái và giữa bảng (nhóm $\text{IA}, \text{IIA}, \text{IIIA}, \text{B}$); phi kim ở góc trên bên phải (nhóm $\text{VA}, \text{VIA}, \text{VIIA}$ và $\text{H}, \text{C}, \text{Si}$); khí hiếm ở cột cuối cùng nhóm $\text{VIIIA}$.",
        ],
        questions=[
            mcq(
                r"Tập hợp những nguyên tử cùng loại, có cùng số hạt nào sau đây trong hạt nhân thì thuộc cùng một **nguyên tố hóa học**?",
                [
                    r"Cùng số hạt neutron ($n$).",
                    r"Cùng tổng số hạt proton và neutron ($p + n$).",
                    r"Cùng số lớp electron ở vỏ nguyên tử.",
                    r"Cùng số hạt proton ($p$).",
                ],
                "D",
                "biet",
                r"Nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có cùng số hạt proton ($p$) trong hạt nhân.",
            ),
            mcq(
                r"Theo danh pháp quốc tế IUPAC, các nguyên tố có ký hiệu hóa học $\text{Na}$, $\text{K}$, $\text{Cu}$, $\text{Fe}$ có tên gọi lần lượt là:",
                [
                    r"Sodium, potassium, copper, iron.",
                    r"Sulfur, phosphorus, calcium, fluorine.",
                    r"Nitrogen, potassium, carbon, iron.",
                    r"Sodium, calcium, copper, silver.",
                ],
                "A",
                "biet",
                r"Theo chuẩn IUPAC: $\text{Na}$ là sodium (natri), $\text{K}$ là potassium (kali), $\text{Cu}$ là copper (đồng) và $\text{Fe}$ là iron (sắt).",
            ),
            mcq(
                r"Trong bảng tuần hoàn các nguyên tố hóa học, các nguyên tố được sắp xếp theo nguyên tắc cơ bản nào sau đây?",
                [
                    r"Theo chiều tăng dần của số hạt neutron ($n$) trong hạt nhân.",
                    r"Theo chiều tăng dần của điện tích hạt nhân nguyên tử ($Z$).",
                    r"Theo chiều giảm dần của số lớp electron.",
                    r"Theo thứ tự bảng chữ cái tên gọi quốc tế IUPAC.",
                ],
                "B",
                "biet",
                r"Nguyên tắc cơ bản đầu tiên để sắp xếp các nguyên tố trong bảng tuần hoàn là theo chiều tăng dần của điện tích hạt nhân nguyên tử ($Z$).",
            ),
            mcq(
                r"Dãy nào sau đây chỉ gồm các nguyên tố thuộc nhóm **khí hiếm** (nhóm $\text{VIIIA}$)?",
                [
                    r"Sodium ($\text{Na}$), magnesium ($\text{Mg}$), aluminium ($\text{Al}$).",
                    r"Fluorine ($\text{F}$), chlorine ($\text{Cl}$), sulfur ($\text{S}$).",
                    r"Helium ($\text{He}$), neon ($\text{Ne}$), argon ($\text{Ar}$).",
                    r"Hydrogen ($\text{H}$), oxygen ($\text{O}$), nitrogen ($\text{N}$).",
                ],
                "C",
                "biet",
                r"Helium ($\text{He}$), neon ($\text{Ne}$) và argon ($\text{Ar}$) là các nguyên tố khí hiếm nằm ở cột cuối cùng bên phải bảng tuần hoàn (nhóm $\text{VIIIA}$).",
            ),
            mcq(
                r"Nguyên tố sulfur ($\text{S}$) có số hiệu nguyên tử $Z = 16$. Vị trí của sulfur trong bảng tuần hoàn các nguyên tố hóa học là:",
                [
                    r"Ô số $16$, chu kỳ $2$, nhóm $\text{VIA}$.",
                    r"Ô số $16$, chu kỳ $3$, nhóm $\text{IIA}$.",
                    r"Ô số $32$, chu kỳ $3$, nhóm $\text{VIA}$.",
                    r"Ô số $16$, chu kỳ $3$, nhóm $\text{VIA}$.",
                ],
                "D",
                "hieu",
                r"Với $Z = 16$, nguyên tử sulfur ($\text{S}$) có $16\text{ electron}$ phân bố trên $3$ lớp theo thứ tự $2, 8, 6$. Do đó $\text{S}$ ở ô số $16$ ($Z = 16$), chu kỳ $3$ ($3$ lớp electron) và nhóm $\text{VIA}$ ($6\text{ electron}$ lớp ngoài cùng).",
            ),
            mcq(
                r"Cho các ký hiệu hóa học được một học sinh viết như sau: $\text{NA}$ (sodium), $\text{mg}$ (magnesium), $\text{Al}$ (aluminium), $\text{cO}$ (cobalt), $\text{Ca}$ (calcium), $\text{Cl}$ (chlorine). Số ký hiệu hóa học đã được viết **đúng quy tắc** là:",
                [
                    r"$3$ ký hiệu: $\text{Al}$, $\text{Ca}$, $\text{Cl}$.",
                    r"$4$ ký hiệu: $\text{NA}$, $\text{Al}$, $\text{Ca}$, $\text{Cl}$.",
                    r"$2$ ký hiệu: $\text{Al}$, $\text{Ca}$.",
                    r"$6$ ký hiệu đều đúng.",
                ],
                "A",
                "hieu",
                r"Quy tắc viết ký hiệu hóa học: chữ cái đầu tiên phải viết IN HOA, chữ cái thứ hai (nếu có) phải viết thường. Do đó chỉ có $\text{Al}$, $\text{Ca}$, $\text{Cl}$ viết đúng; còn $\text{NA}$ (đúng là $\text{Na}$), $\text{mg}$ (đúng là $\text{Mg}$), $\text{cO}$ (đúng là $\text{Co}$) đều viết sai.",
            ),
            tf4(
                r"Cho thông tin ô nguyên tố của potassium ($\text{K}$) trong bảng tuần hoàn: Số hiệu nguyên tử là $19$, khối lượng nguyên tử là $39\text{ amu}$, nằm ở chu kỳ $4$, nhóm $\text{IA}$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Trong hạt nhân nguyên tử potassium ($\text{K}$) có $19$ hạt proton và lớp vỏ có $19$ hạt electron.",
                    r"Nguyên tử potassium ($\text{K}$) có $4$ lớp electron và có $1\text{ electron}$ ở lớp ngoài cùng.",
                    r"Số hạt neutron ($n$) trong hạt nhân nguyên tử potassium ($\text{K}$) này là $19$ hạt.",
                    r"Potassium ($\text{K}$) là một nguyên tố kim loại hoạt động hóa học mạnh nằm ở nhóm $\text{IA}$ (nhóm kim loại kiềm).",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Số hiệu nguyên tử $Z = 19 \Rightarrow p = e = 19$." "\n"
                    r"- **Ý b) Đúng**: Chu kỳ $4 \Rightarrow$ có $4$ lớp electron; nhóm $\text{IA} \Rightarrow$ có $1\text{ electron}$ lớp ngoài cùng (phân bố $2, 8, 8, 1$)." "\n"
                    r"- **Ý c) Sai**: Số hạt neutron là $n \approx A - p = 39 - 19 = 20$ hạt (không phải $19$ hạt)." "\n"
                    r"- **Ý d) Đúng**: Các nguyên tố nhóm $\text{IA}$ (trừ $\text{H}$) như $\text{Li}, \text{Na}, \text{K}$ đều là các nguyên tố kim loại kiềm điển hình."
                ),
            ),
            tf4(
                r"Khi khảo sát vị trí và tính chất của các nguyên tố thuộc chu kỳ $2$ và chu kỳ $3$ trong bảng tuần hoàn (như $\text{H}, \text{He}, \text{C}, \text{N}, \text{O}, \text{Ne}, \text{Na}, \text{Mg}, \text{Al}$), xét tính đúng/sai của các nhận định sau:",
                [
                    r"Nguyên tố hydrogen ($\text{H}$, $Z = 1$) tuy được xếp ở cột nhóm $\text{IA}$ nhưng là một nguyên tố phi kim chứ không phải kim loại.",
                    r"Nguyên tố helium ($\text{He}$, $Z = 2$) có $2\text{ electron}$ lớp ngoài cùng nên được xếp vào nhóm $\text{IIA}$ cùng với magnesium ($\text{Mg}$).",
                    r"Ba nguyên tố carbon ($\text{C}$, $Z = 6$), nitrogen ($\text{N}$, $Z = 7$) và oxygen ($\text{O}$, $Z = 8$) cùng thuộc chu kỳ $2$ vì nguyên tử của chúng đều có đúng $2$ lớp electron.",
                    r"Hai nguyên tố sodium ($\text{Na}$, ô $11$) và magnesium ($\text{Mg}$, ô $12$) đứng kế tiếp nhau ở đầu chu kỳ $3$ đều là các nguyên tố kim loại.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Hydrogen ($\text{H}$) có $1e$ lớp ngoài cùng nên xếp ở nhóm $\text{IA}$, nhưng là nguyên tố phi kim." "\n"
                    r"- **Ý b) Sai**: Tuy $\text{He}$ chỉ có $2\text{ electron}$ ở lớp thứ nhất (lớp duy nhất đã bão hòa tối đa $2e$), nhưng $\text{He}$ là nguyên tố **khí hiếm** nên được xếp vào **nhóm $\text{VIIIA}$**, không phải nhóm $\text{IIA}$." "\n"
                    r"- **Ý c) Đúng**: $\text{C}$ ($2, 4$), $\text{N}$ ($2, 5$) và $\text{O}$ ($2, 6$) đều có $2$ lớp electron nên cùng thuộc chu kỳ $2$." "\n"
                    r"- **Ý d) Đúng**: $\text{Na}$ (nhóm $\text{IA}$) và $\text{Mg}$ (nhóm $\text{IIA}$) đều là các nguyên tố kim loại điển hình của chu kỳ $3$."
                ),
            ),
            mcq(
                r"Hai nguyên tố $\text{X}$ và $\text{Y}$ đứng kế tiếp nhau trong cùng một chu kỳ của bảng tuần hoàn và có tổng số đơn vị điện tích hạt nhân ($Z_{\text{X}} + Z_{\text{Y}}$) bằng $25$. Biết $Z_{\text{X}} < Z_{\text{Y}}$, hai nguyên tố $\text{X}$ và $\text{Y}$ lần lượt là:",
                [
                    r"Nitrogen ($\text{N}$, $Z = 7$) và argon ($\text{Ar}$, $Z = 18$).",
                    r"Magnesium ($\text{Mg}$, $Z = 12$) và aluminium ($\text{Al}$, $Z = 13$).",
                    r"Sodium ($\text{Na}$, $Z = 11$) và silicon ($\text{Si}$, $Z = 14$).",
                    r"Carbon ($\text{C}$, $Z = 6$) và potassium ($\text{K}$, $Z = 19$).",
                ],
                "B",
                "vandung",
                r"Hai nguyên tố đứng kế tiếp nhau trong một chu kỳ thì hơn kém nhau $1$ đơn vị điện tích hạt nhân: $Z_{\text{Y}} - Z_{\text{X}} = 1$. Kết hợp với $Z_{\text{X}} + Z_{\text{Y}} = 25$, ta giải được $Z_{\text{X}} = \dfrac{25 - 1}{2} = 12$ (magnesium, $\text{Mg}$) và $Z_{\text{Y}} = 13$ (aluminium, $\text{Al}$).",
            ),
            short(
                r"Nguyên tố silicon ($\text{Si}$ — nguyên tố chính trong cát thạch anh và vi mạch bán dẫn) nằm ở chu kỳ $3$, nhóm $\text{IVA}$ trong bảng tuần hoàn các nguyên tố hóa học. Hãy xác định số thứ tự của ô nguyên tố (cũng chính là số hạt proton $Z$) của silicon ($\text{Si}$).",
                ["14"],
                "vandung",
                (
                    r"Vì silicon ($\text{Si}$) nằm ở chu kỳ $3$ nên nguyên tử có $3$ lớp electron (lớp thứ nhất đã chứa tối đa $2e$, lớp thứ hai đã chứa tối đa $8e$)." "\n"
                    r"Vì $\text{Si}$ thuộc nhóm $\text{IVA}$ nên lớp ngoài cùng (lớp thứ ba) có $4\text{ electron}$." "\n"
                    r"Vậy số thứ tự ô nguyên tố (số hạt proton $Z$) của $\text{Si}$ là:" "\n"
                    r"$$Z = p = e = 2 + 8 + 4 = 14$$"
                ),
            ),
        ],
        description="Khái niệm nguyên tố hóa học, ký hiệu hóa học và tên gọi quốc tế IUPAC, cấu tạo bảng tuần hoàn và phân loại kim loại, phi kim, khí hiếm.",
    ),
    lesson(
        grade=7,
        order=3,
        code="H7-C03",
        title="Chương 3: Phân tử và khối lượng phân tử",
        topic="phan-tu",
        summary=(
            r"Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất. "
            r"Phân tử có thể được tạo bởi các nguyên tử của cùng một nguyên tố hóa học (như $\text{H}_2$, $\text{O}_2$, $\text{N}_2$, $\text{Cl}_2$, $\text{O}_3$) hoặc từ các nguyên tử của nhiều nguyên tố khác nhau (như $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NH}_3$, $\text{CH}_4$). "
            r"Khối lượng phân tử (tính theo đơn vị $\text{amu}$) của một chất bằng tổng khối lượng của tất cả các nguyên tử có trong một phân tử chất đó."
        ),
        objectives=[
            r"Nêu được khái niệm phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.",
            r"Phân biệt được hạt hợp thành của các chất phân tử ($\text{H}_2\text{O}$, $\text{O}_2$, $\text{CO}_2$, $\text{NH}_3$) với hạt hợp thành của các khí hiếm ($\text{He}$, $\text{Ne}$, $\text{Ar}$ tồn tại dưới dạng nguyên tử riêng rẽ).",
            r"Xác định được số nguyên tử của mỗi nguyên tố và tổng số nguyên tử có trong một phân tử dựa vào công thức hóa học.",
            r"Tính được khối lượng phân tử ($M$) theo đơn vị $\text{amu}$ của các phân tử đơn chất và hợp chất phổ biến.",
        ],
        formulas=[
            {
                "name": "Công thức tính khối lượng phân tử tổng quát",
                "formula": r"$M_{\text{A}_x\text{B}_y\text{C}_z} = x \cdot M_{\text{A}} + y \cdot M_{\text{B}} + z \cdot M_{\text{C}} \text{ (amu)}$",
                "note": r"Trong đó $M_{\text{A}}, M_{\text{B}}, M_{\text{C}}$ là khối lượng nguyên tử ($\text{amu}$) và $x, y, z$ là chỉ số nguyên tử tương ứng trong phân tử.",
            },
            {
                "name": "Khối lượng nguyên tử (amu) của các nguyên tố thường gặp",
                "formula": r"$\text{H} = 1; \text{ C} = 12; \text{ N} = 14; \text{ O} = 16; \text{ Na} = 23; \text{ Mg} = 24; \text{ Al} = 27; \text{ S} = 32; \text{ Cl} = 35{,}5; \text{ Ca} = 40; \text{ Fe} = 56; \text{ Cu} = 64$",
                "note": r"Khi có nhóm nguyên tử trong ngoặc đơn như $\text{Ca(OH)}_2$ hoặc $\text{Al}_2(\text{SO}_4)_3$, chỉ số ngoài ngoặc nhân cho toàn bộ các nguyên tử trong ngoặc.",
            },
            {
                "name": "Tổng số nguyên tử trong một phân tử",
                "formula": r"$N_{\text{nguyên tử}}(\text{A}_x\text{B}_y\text{C}_z) = x + y + z$",
                "note": r"Ví dụ phân tử sulfuric acid ($\text{H}_2\text{SO}_4$) có $2 + 1 + 4 = 7$ nguyên tử.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Hạt hợp thành của chất và khái niệm phân tử",
                "content": (
                    r"- Mỗi chất đều được tạo nên từ vô số các hạt đại diện vô cùng nhỏ bé giống hệt nhau. Đối với hầu hết các chất (như nước $\text{H}_2\text{O}$, khí oxygen $\text{O}_2$, khí carbon dioxide $\text{CO}_2$, đường saccharose $\text{C}_{12}\text{H}_{22}\text{O}_{11}$), hạt đại diện đó là **phân tử**." "\n"
                    r"- **Định nghĩa**: **Phân tử** là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất." "\n"
                    r"- **Các dạng phân tử thường gặp**:" "\n"
                    r"  + Phân tử tạo bởi các nguyên tử của **cùng một nguyên tố hóa học**: phân tử khí hydrogen ($\text{H}_2$ gồm $2$ nguyên tử $\text{H}$), khí oxygen ($\text{O}_2$ gồm $2$ nguyên tử $\text{O}$), khí ozone ($\text{O}_3$ gồm $3$ nguyên tử $\text{O}$), khí nitrogen ($\text{N}_2$ gồm $2$ nguyên tử $\text{N}$), khí chlorine ($\text{Cl}_2$ gồm $2$ nguyên tử $\text{Cl}$)." "\n"
                    r"  + Phân tử tạo bởi các nguyên tử của **nhiều nguyên tố hóa học khác nhau**: phân tử nước ($\text{H}_2\text{O}$ gồm $2$ nguyên tử $\text{H}$ và $1$ nguyên tử $\text{O}$), phân tử ammonia ($\text{NH}_3$ gồm $1$ nguyên tử $\text{N}$ và $3$ nguyên tử $\text{H}$), phân tử methane ($\text{CH}_4$ gồm $1$ nguyên tử $\text{C}$ và $4$ nguyên tử $\text{H}$), phân tử carbon dioxide ($\text{CO}_2$ gồm $1$ nguyên tử $\text{C}$ và $2$ nguyên tử $\text{O}$)." "\n"
                    r"- **Trường hợp đặc biệt**: Đối với các **khí hiếm** (như helium $\text{He}$, neon $\text{Ne}$, argon $\text{Ar}$), hạt đại diện cho chất chỉ là các **nguyên tử riêng rẽ** (không liên kết thành phân tử nhiều nguyên tử)."
                ),
            },
            {
                "title": "2. Khối lượng phân tử và cách tính",
                "content": (
                    r"- **Khối lượng phân tử** của một chất bằng tổng khối lượng của các nguyên tử có trong phân tử chất đó. Đơn vị của khối lượng phân tử là **$\text{amu}$**." "\n"
                    r"- **Quy tắc tính khối lượng phân tử** của chất có công thức $\text{A}_x\text{B}_y$:" "\n"
                    r"$$M_{\text{A}_x\text{B}_y} = x \cdot M_{\text{A}} + y \cdot M_{\text{B}} \text{ (amu)}$$" "\n"
                    r"- **Ví dụ minh họa nhanh** (với $\text{H} = 1, \text{C} = 12, \text{N} = 14, \text{O} = 16, \text{S} = 32, \text{Ca} = 40$):" "\n"
                    r"  + Phân tử khí oxygen ($\text{O}_2$): $M_{\text{O}_2} = 2 \cdot 16 = 32\text{ amu}$." "\n"
                    r"  + Phân tử nước ($\text{H}_2\text{O}$): $M_{\text{H}_2\text{O}} = 2 \cdot 1 + 1 \cdot 16 = 18\text{ amu}$." "\n"
                    r"  + Phân tử ammonia ($\text{NH}_3$): $M_{\text{NH}_3} = 1 \cdot 14 + 3 \cdot 1 = 17\text{ amu}$." "\n"
                    r"  + Phân tử carbon dioxide ($\text{CO}_2$): $M_{\text{CO}_2} = 1 \cdot 12 + 2 \cdot 16 = 44\text{ amu}$." "\n"
                    r"  + Phân tử calcium carbonate ($\text{CaCO}_3$): $M_{\text{CaCO}_3} = 40 + 12 + 3 \cdot 16 = 100\text{ amu}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Tính khối lượng phân tử của hợp chất có nhóm nguyên tử",
                "problem": (
                    r"Biết khối lượng nguyên tử: $\text{H} = 1\text{ amu}$, $\text{O} = 16\text{ amu}$, $\text{S} = 32\text{ amu}$, $\text{Ca} = 40\text{ amu}$, $\text{Cu} = 64\text{ amu}$. "
                    r"Hãy tính khối lượng phân tử của: a) Sulfuric acid ($\text{H}_2\text{SO}_4$); b) Calcium hydroxide ($\text{Ca(OH)}_2$); c) Copper(II) sulfate ($\text{CuSO}_4$)."
                ),
                "solution": (
                    r"- **a)** Khối lượng phân tử của $\text{H}_2\text{SO}_4$ là:" "\n"
                    r"$$M_{\text{H}_2\text{SO}_4} = 2 \cdot 1 + 1 \cdot 32 + 4 \cdot 16 = 98\text{ amu}$$" "\n"
                    r"- **b)** Khối lượng phân tử của $\text{Ca(OH)}_2$ là:" "\n"
                    r"$$M_{\text{Ca(OH)}_2} = 40 + 2 \cdot (16 + 1) = 40 + 34 = 74\text{ amu}$$" "\n"
                    r"- **c)** Khối lượng phân tử của $\text{CuSO}_4$ là:" "\n"
                    r"$$M_{\text{CuSO}_4} = 64 + 32 + 4 \cdot 16 = 160\text{ amu}$$"
                ),
            },
            {
                "title": "Ví dụ 2: Xác định nguyên tố chưa biết dựa vào khối lượng phân tử",
                "problem": (
                    r"Một phân tử oxide có công thức dạng $\text{XO}_2$ (gồm $1$ nguyên tử nguyên tố $\text{X}$ liên kết với $2$ nguyên tử oxygen $\text{O}$). "
                    r"Biết khối lượng phân tử của $\text{XO}_2$ nặng gấp $2$ lần khối lượng phân tử của khí oxygen ($\text{O}_2$). Tìm khối lượng nguyên tử và tên nguyên tố $\text{X}$."
                ),
                "solution": (
                    r"- Khối lượng phân tử của khí oxygen ($\text{O}_2$) là: $M_{\text{O}_2} = 2 \cdot 16 = 32\text{ amu}$." "\n"
                    r"- Khối lượng phân tử của $\text{XO}_2$ là: $M_{\text{XO}_2} = 2 \cdot 32 = 64\text{ amu}$." "\n"
                    r"- Mặt khác: $M_{\text{XO}_2} = M_{\text{X}} + 2 \cdot 16 = 64 \Rightarrow M_{\text{X}} = 64 - 32 = 32\text{ amu}$." "\n"
                    r"- Vậy $\text{X}$ là nguyên tố **sulfur** ($\text{S} = 32\text{ amu}$) và phân tử đó là sulfur dioxide ($\text{SO}_2$)."
                ),
            },
        ],
        key_takeaways=[
            r"Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và mang đầy đủ tính chất hóa học của chất.",
            r"Khối lượng phân tử ($M$) tính theo đơn vị $\text{amu}$ bằng tổng khối lượng các nguyên tử tạo nên một phân tử đó.",
            r"Khi công thức có dấu ngoặc như $\text{M}(\text{AB})_n$, khối lượng của nhóm $(\text{AB})$ được nhân với chỉ số $n$.",
        ],
        questions=[
            mcq(
                r"Phát biểu nào sau đây định nghĩa đúng nhất về **phân tử**?",
                [
                    r"Phân tử chỉ gồm các hạt electron chuyển động quanh hạt nhân.",
                    r"Phân tử của mọi chất đều chỉ chứa đúng $2$ nguyên tử liên kết với nhau.",
                    r"Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.",
                    r"Phân tử là hạt mang điện tích dương nằm ở tâm của nguyên tử.",
                ],
                "C",
                "biet",
                r"Theo định nghĩa SGK KHTN 7 (Kết nối tri thức): Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.",
            ),
            mcq(
                r"Cho biết khối lượng nguyên tử: $\text{C} = 12\text{ amu}$, $\text{O} = 16\text{ amu}$. Khối lượng phân tử của khí carbon dioxide ($\text{CO}_2$) là:",
                [
                    r"$28\text{ amu}$.",
                    r"$32\text{ amu}$.",
                    r"$40\text{ amu}$.",
                    r"$44\text{ amu}$.",
                ],
                "D",
                "biet",
                r"Một phân tử $\text{CO}_2$ gồm $1$ nguyên tử $\text{C}$ và $2$ nguyên tử $\text{O}$ nên có khối lượng phân tử là: $M_{\text{CO}_2} = 1 \cdot 12 + 2 \cdot 16 = 44\text{ amu}$.",
            ),
            mcq(
                r"Trong một phân tử methane ($\text{CH}_4$ — thành phần chính của khí thiên nhiên và biogas), tổng số nguyên tử tạo nên phân tử là:",
                [
                    r"$5$ nguyên tử (gồm $1$ nguyên tử $\text{C}$ và $4$ nguyên tử $\text{H}$).",
                    r"$4$ nguyên tử (chỉ gồm $4$ nguyên tử $\text{H}$).",
                    r"$2$ nguyên tử (gồm $1$ nguyên tử $\text{C}$ và $1$ nguyên tử $\text{H}$).",
                    r"$8$ nguyên tử (gồm $4$ nguyên tử $\text{C}$ và $4$ nguyên tử $\text{H}$).",
                ],
                "A",
                "biet",
                r"Phân tử $\text{CH}_4$ gồm $1$ nguyên tử carbon ($\text{C}$) liên kết với $4$ nguyên tử hydrogen ($\text{H}$), tổng cộng có $1 + 4 = 5$ nguyên tử.",
            ),
            mcq(
                r"Chất nào sau đây có các hạt đại diện tồn tại dưới dạng **các nguyên tử riêng rẽ** (không liên kết thành phân tử hai hay nhiều nguyên tử ở điều kiện thường)?",
                [
                    r"Nước tinh khiết ($\text{H}_2\text{O}$).",
                    r"Khí hiếm neon ($\text{Ne}$) dùng trong đèn quảng cáo.",
                    r"Khí oxygen ($\text{O}_2$) trong không khí.",
                    r"Khí nitrogen ($\text{N}_2$) trong không khí.",
                ],
                "B",
                "biet",
                r"Các nguyên tố khí hiếm như helium ($\text{He}$), neon ($\text{Ne}$), argon ($\text{Ar}$) có lớp vỏ electron bền vững nên hạt đại diện là các nguyên tử độc lập riêng rẽ.",
            ),
            mcq(
                r"Biết khối lượng nguyên tử: $\text{H} = 1\text{ amu}$, $\text{C} = 12\text{ amu}$, $\text{N} = 14\text{ amu}$, $\text{O} = 16\text{ amu}$, $\text{S} = 32\text{ amu}$. Cặp phân tử nào sau đây có **cùng khối lượng phân tử**?",
                [
                    r"Khí oxygen ($\text{O}_2$) và khí carbon dioxide ($\text{CO}_2$).",
                    r"Nước ($\text{H}_2\text{O}$) và hydrogen sulfide ($\text{H}_2\text{S}$).",
                    r"Khí nitrogen ($\text{N}_2$) và khí carbon monoxide ($\text{CO}$).",
                    r"Khí methane ($\text{CH}_4$) và khí ammonia ($\text{NH}_3$).",
                ],
                "C",
                "hieu",
                r"Ta tính khối lượng phân tử: $M_{\text{N}_2} = 2 \cdot 14 = 28\text{ amu}$ và $M_{\text{CO}} = 12 + 16 = 28\text{ amu}$. Vậy hai phân tử $\text{N}_2$ và $\text{CO}$ có cùng khối lượng phân tử là $28\text{ amu}$. (Ở các phương án khác: $\text{CH}_4 = 16 \neq \text{NH}_3 = 17$; $\text{O}_2 = 32 \neq \text{CO}_2 = 44$; $\text{H}_2\text{O} = 18 \neq \text{H}_2\text{S} = 34$).",
            ),
            mcq(
                r"Cho biết khối lượng nguyên tử: $\text{N} = 14\text{ amu}$, $\text{H} = 1\text{ amu}$, $\text{S} = 32\text{ amu}$, $\text{O} = 16\text{ amu}$. Khối lượng phân tử của muối ammonium sulfate (phân đạm một lá, có công thức $\text{(NH}_4)_2\text{SO}_4$) là:",
                [
                    r"$114\text{ amu}$.",
                    r"$98\text{ amu}$.",
                    r"$150\text{ amu}$.",
                    r"$132\text{ amu}$.",
                ],
                "D",
                "hieu",
                r"Trong $\text{(NH}_4)_2\text{SO}_4$, nhóm $(\text{NH}_4)$ có khối lượng là $14 + 4 \cdot 1 = 18\text{ amu}$ và được lấy $2$ lần. Vậy khối lượng phân tử là: $M = 2 \cdot 18 + 32 + 4 \cdot 16 = 36 + 32 + 64 = 132\text{ amu}$.",
            ),
            tf4(
                r"Cho bốn chất phổ biến sau: khí hydrogen ($\text{H}_2$), khí ozone ($\text{O}_3$), nước ($\text{H}_2\text{O}$) và đá vôi calcium carbonate ($\text{CaCO}_3$). Biết khối lượng nguyên tử: $\text{H} = 1\text{ amu}$, $\text{C} = 12\text{ amu}$, $\text{O} = 16\text{ amu}$, $\text{Ca} = 40\text{ amu}$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Phân tử khí hydrogen ($\text{H}_2$) và phân tử khí ozone ($\text{O}_3$) đều được tạo nên từ các nguyên tử của cùng một nguyên tố hóa học.",
                    r"Khối lượng phân tử của khí ozone ($\text{O}_3$) là $32\text{ amu}$.",
                    r"Một phân tử nước ($\text{H}_2\text{O}$) có khối lượng phân tử bằng $18\text{ amu}$, nặng gấp $9$ lần một phân tử khí hydrogen ($\text{H}_2$).",
                    r"Trong một phân tử calcium carbonate ($\text{CaCO}_3$) có tất cả $5$ nguyên tử và khối lượng phân tử bằng $100\text{ amu}$.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: $\text{H}_2$ chỉ tạo bởi nguyên tố $\text{H}$; $\text{O}_3$ chỉ tạo bởi nguyên tố $\text{O}$." "\n"
                    r"- **Ý b) Sai**: Phân tử ozone ($\text{O}_3$) gồm $3$ nguyên tử oxygen nên có khối lượng phân tử là $3 \cdot 16 = 48\text{ amu}$ (không phải $32\text{ amu}$)." "\n"
                    r"- **Ý c) Đúng**: $M_{\text{H}_2\text{O}} = 18\text{ amu}$ và $M_{\text{H}_2} = 2 \cdot 1 = 2\text{ amu}$, ta có $\dfrac{18}{2} = 9$ lần." "\n"
                    r"- **Ý d) Đúng**: $\text{CaCO}_3$ gồm $1\text{ Ca} + 1\text{ C} + 3\text{ O} = 5$ nguyên tử, và $M_{\text{CaCO}_3} = 40 + 12 + 3 \cdot 16 = 100\text{ amu}$."
                ),
            ),
            tf4(
                r"Glucose là loại đường cung cấp năng lượng trực tiếp cho cơ thể người (có nhiều trong quả nho chín), một phân tử glucose có công thức hóa học là $\text{C}_6\text{H}_{12}\text{O}_6$. Biết khối lượng nguyên tử: $\text{H} = 1\text{ amu}$, $\text{C} = 12\text{ amu}$, $\text{O} = 16\text{ amu}$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Phân tử glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) được cấu tạo từ $3$ nguyên tố hóa học là carbon ($\text{C}$), hydrogen ($\text{H}$) và oxygen ($\text{O}$).",
                    r"Tổng số nguyên tử có trong một phân tử glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) là $24$ nguyên tử.",
                    r"Trong một phân tử glucose, số nguyên tử hydrogen ($\text{H}$) bằng tổng số nguyên tử carbon ($\text{C}$) và nguyên tử oxygen ($\text{O}$).",
                    r"Khối lượng phân tử của glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) bằng $160\text{ amu}$.",
                ],
                "Đ/Đ/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Phân tử $\text{C}_6\text{H}_{12}\text{O}_6$ gồm $3$ nguyên tố hóa học là $\text{C}$, $\text{H}$ và $\text{O}$." "\n"
                    r"- **Ý b) Đúng**: Tổng số nguyên tử trong $1$ phân tử glucose là $6 + 12 + 6 = 24$ nguyên tử." "\n"
                    r"- **Ý c) Đúng**: Số nguyên tử $\text{H}$ là $12$, bằng tổng số nguyên tử $\text{C}$ ($6$) và $\text{O}$ ($6$): $6 + 6 = 12$." "\n"
                    r"- **Ý d) Sai**: Khối lượng phân tử của glucose là $M = 6 \cdot 12 + 12 \cdot 1 + 6 \cdot 16 = 72 + 12 + 96 = 180\text{ amu}$ (không phải $160\text{ amu}$)."
                ),
            ),
            mcq(
                r"Một hợp chất có công thức hóa học dạng $\text{M}_2(\text{SO}_4)_3$ có khối lượng phân tử bằng $342\text{ amu}$. Biết khối lượng nguyên tử của sulfur là $\text{S} = 32\text{ amu}$ và của oxygen là $\text{O} = 16\text{ amu}$. Khối lượng nguyên tử và tên nguyên tố kim loại $\text{M}$ là:",
                [
                    r"$27\text{ amu}$ — Aluminium ($\text{Al}$).",
                    r"$56\text{ amu}$ — Iron ($\text{Fe}$).",
                    r"$24\text{ amu}$ — Magnesium ($\text{Mg}$).",
                    r"$64\text{ amu}$ — Copper ($\text{Cu}$).",
                ],
                "A",
                "vandung",
                r"Khối lượng của một nhóm sulfate $(\text{SO}_4)$ là $32 + 4 \cdot 16 = 96\text{ amu}$. Trong phân tử $\text{M}_2(\text{SO}_4)_3$, ta có: $2 \cdot M_{\text{M}} + 3 \cdot 96 = 342 \Rightarrow 2 \cdot M_{\text{M}} = 342 - 288 = 54 \Rightarrow M_{\text{M}} = 27\text{ amu}$. Vậy $\text{M}$ là nguyên tố aluminium ($\text{Al}$).",
            ),
            short(
                r"Đường mía (saccharose) có công thức phân tử là $\text{C}_{12}\text{H}_{22}\text{O}_{11}$. Biết khối lượng nguyên tử của các nguyên tố lần lượt là $\text{C} = 12\text{ amu}$, $\text{H} = 1\text{ amu}$ và $\text{O} = 16\text{ amu}$. Hãy tính khối lượng phân tử của đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) theo đơn vị $\text{amu}$.",
                ["342", "342,0", "342.0"],
                "vandung",
                (
                    r"Khối lượng phân tử của đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) là:" "\n"
                    r"$$M_{\text{C}_{12}\text{H}_{22}\text{O}_{11}} = 12 \cdot 12 + 22 \cdot 1 + 11 \cdot 16 = 144 + 22 + 176 = 342\text{ amu}$$"
                ),
            ),
        ],
        description="Khái niệm phân tử là hạt đại diện cho chất gồm một số nguyên tử liên kết với nhau và cách tính khối lượng phân tử theo đơn vị amu.",
    ),
    lesson(
        grade=7,
        order=4,
        code="H7-C04",
        title="Chương 4: Đơn chất và hợp chất",
        topic="don-chat-hop-chat",
        summary=(
            r"Mọi chất tinh khiết trong tự nhiên đều được phân loại thành đơn chất hoặc hợp chất dựa trên số nguyên tố hóa học tạo nên chất đó. "
            r"Đơn chất được tạo nên từ một nguyên tố hóa học (bao gồm đơn chất kim loại như $\text{Fe}$, $\text{Cu}$, $\text{Al}$, đơn chất phi kim như $\text{H}_2$, $\text{O}_2$, $\text{N}_2$, $\text{C}$, $\text{S}$ và khí hiếm như $\text{He}$, $\text{Ne}$, $\text{Ar}$). "
            r"Hợp chất được tạo nên từ hai nguyên tố hóa học trở lên (bao gồm hợp chất vô cơ như $\text{H}_2\text{O}$, $\text{NaCl}$, $\text{CaCO}_3$ và hợp chất hữu cơ như $\text{CH}_4$, $\text{C}_6\text{H}_{12}\text{O}_6$), trong đó thành phần phần trăm khối lượng của mỗi nguyên tố luôn xác định."
        ),
        objectives=[
            r"Phân biệt được đơn chất (tạo nên từ $1$ nguyên tố hóa học) và hợp chất (tạo nên từ $2$ nguyên tố hóa học trở lên) dựa vào thành phần nguyên tố.",
            r"Phân loại được các đơn chất thành đơn chất kim loại, đơn chất phi kim, khí hiếm và nêu được đặc điểm cấu tạo, tính chất vật lý đặc trưng của chúng.",
            r"Phân biệt được hợp chất vô cơ ($\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NaCl}$, $\text{CaCO}_3$) và hợp chất hữu cơ ($\text{CH}_4$, $\text{C}_2\text{H}_5\text{OH}$, $\text{C}_6\text{H}_{12}\text{O}_6$) trong đời sống.",
            r"Tính được thành phần phần trăm về khối lượng của từng nguyên tố hóa học trong hợp chất khi biết công thức hóa học.",
        ],
        formulas=[
            {
                "name": "Thành phần phần trăm khối lượng nguyên tố trong hợp chất",
                "formula": r"$\%m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{A}_x\text{B}_y}} \cdot 100\%; \quad \%m_{\text{B}} = 100\% - \%m_{\text{A}}$",
                "note": r"Trong hợp chất $\text{A}_x\text{B}_y$, tổng phần trăm khối lượng của tất cả các nguyên tố luôn bằng $100\%$.",
            },
            {
                "name": "Tìm chỉ số nguyên tử khi biết khối lượng phân tử và phần trăm nguyên tố",
                "formula": r"$x = \dfrac{\%m_{\text{A}} \cdot M_{\text{hợp chất}}}{100\% \cdot M_{\text{A}}}$",
                "note": r"Áp dụng để xác định công thức hóa học của hợp chất từ số liệu phân tích nguyên tố.",
            },
            {
                "name": "Phân biệt nhanh đơn chất và hợp chất",
                "formula": r"$\text{Đơn chất: } 1\text{ nguyên tố } (\text{O}_2, \text{O}_3, \text{Fe}, \text{S}) \quad \mid \quad \text{Hợp chất: } \ge 2\text{ nguyên tố } (\text{H}_2\text{O}, \text{CO}_2, \text{NaCl})$",
                "note": r"Lưu ý: Hỗn hợp (như không khí, nước biển) gồm nhiều chất trộn lẫn, không phải là một hợp chất.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Đơn chất",
                "content": (
                    r"- **Khái niệm**: **Đơn chất** là những chất được tạo nên từ **một nguyên tố hóa học**." "\n"
                    r"- **Phân loại đơn chất**:" "\n"
                    r"  1. **Đơn chất kim loại**: Như iron ($\text{Fe}$), copper ($\text{Cu}$), aluminium ($\text{Al}$), sodium ($\text{Na}$), magnesium ($\text{Mg}$), silver ($\text{Ag}$), mercury ($\text{Hg}$ - kim loại duy nhất ở thể lỏng ở nhiệt độ thường). Các nguyên tử sắp xếp khít nhau, có tính dẫn điện, dẫn nhiệt tốt, có ánh kim và tính dẻo. Công thức hóa học của đơn chất kim loại trùng với ký hiệu nguyên tố ($\text{Fe}, \text{Cu}, \text{Al}$)." "\n"
                    r"  2. **Đơn chất phi kim**: Như khí hydrogen ($\text{H}_2$), khí oxygen ($\text{O}_2$), khí ozone ($\text{O}_3$), khí nitrogen ($\text{N}_2$), khí chlorine ($\text{Cl}_2$), bromine lỏng ($\text{Br}_2$), hoặc chất rắn như carbon ($\text{C}$ - than chì, kim cương), sulfur ($\text{S}$), phosphorus ($\text{P}$). Thường không dẫn điện, không dẫn nhiệt (trừ than chì $\text{C}$ dẫn điện tốt)." "\n"
                    r"  3. **Đơn chất khí hiếm**: Như helium ($\text{He}$), neon ($\text{Ne}$), argon ($\text{Ar}$), tồn tại ở thể khí dưới dạng nguyên tử đơn lẻ rất bền vững."
                ),
            },
            {
                "title": "2. Hợp chất",
                "content": (
                    r"- **Khái niệm**: **Hợp chất** là những chất được tạo nên từ **hai hay nhiều nguyên tố hóa học** liên kết với nhau theo tỉ lệ xác định." "\n"
                    r"- **Phân loại hợp chất**:" "\n"
                    r"  1. **Hợp chất vô cơ**: Nước ($\text{H}_2\text{O}$), muối ăn sodium chloride ($\text{NaCl}$), khí carbon dioxide ($\text{CO}_2$), đá vôi calcium carbonate ($\text{CaCO}_3$), sulfuric acid ($\text{H}_2\text{SO}_4$), sodium hydroxide ($\text{NaOH}$)." "\n"
                    r"  2. **Hợp chất hữu cơ** (hợp chất của carbon, trừ $\text{CO}, \text{CO}_2$, muối carbonate...): Khí methane ($\text{CH}_4$), cồn ethanol ($\text{C}_2\text{H}_5\text{OH}$), đường glucose ($\text{C}_6\text{H}_{12}\text{O}_6$), đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), acetic acid ($\text{CH}_3\text{COOH}$)."
                ),
            },
            {
                "title": "3. Tính thành phần phần trăm khối lượng của nguyên tố trong hợp chất",
                "content": (
                    r"- Với hợp chất có công thức hóa học $\text{A}_x\text{B}_y\text{C}_z$, các bước tính thành phần phần trăm khối lượng của từng nguyên tố:" "\n"
                    r"  + **Bước 1**: Tính khối lượng phân tử của hợp chất: $M = x \cdot M_{\text{A}} + y \cdot M_{\text{B}} + z \cdot M_{\text{C}}\text{ (amu)}$." "\n"
                    r"  + **Bước 2**: Tính phần trăm khối lượng mỗi nguyên tố:" "\n"
                    r"$$\%m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M} \cdot 100\%; \quad \%m_{\text{B}} = \dfrac{y \cdot M_{\text{B}}}{M} \cdot 100\%; \quad \%m_{\text{C}} = 100\% - (\%m_{\text{A}} + \%m_{\text{B}})$$"
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân biệt đơn chất, hợp chất và hỗn hợp",
                "problem": (
                    r"Cho các chất và vật liệu sau: (1) khí ozone ($\text{O}_3$), (2) khí ammonia ($\text{NH}_3$), (3) dây kim loại copper ($\text{Cu}$) nguyên chất, "
                    r"(4) nước muối sinh lý, (5) muối ăn sodium chloride ($\text{NaCl}$) tinh khiết. Hãy chỉ ra đâu là đơn chất, đâu là hợp chất và đâu là hỗn hợp."
                ),
                "solution": (
                    r"- **Đơn chất** (chỉ tạo nên từ $1$ nguyên tố hóa học): (1) khí ozone ($\text{O}_3$ — tạo từ $1$ nguyên tố oxygen $\text{O}$), (3) kim loại copper ($\text{Cu}$ — tạo từ $1$ nguyên tố $\text{Cu}$)." "\n"
                    r"- **Hợp chất** (chất tinh khiết tạo nên từ $2$ nguyên tố trở lên): (2) khí ammonia ($\text{NH}_3$ — tạo từ $\text{N}$ và $\text{H}$), (5) sodium chloride ($\text{NaCl}$ — tạo từ $\text{Na}$ và $\text{Cl}$)." "\n"
                    r"- **Hỗn hợp** (gồm hai chất trộn lẫn là $\text{NaCl}$ và $\text{H}_2\text{O}$): (4) nước muối sinh lý."
                ),
            },
            {
                "title": "Ví dụ 2: Tính phần trăm khối lượng nguyên tố nitrogen trong phân đạm urea",
                "problem": (
                    r"Phân đạm urea có công thức hóa học là $\text{(NH}_2)_2\text{CO}$. Biết khối lượng nguyên tử: $\text{H} = 1\text{ amu}$, $\text{C} = 12\text{ amu}$, $\text{N} = 14\text{ amu}$, $\text{O} = 16\text{ amu}$. "
                    r"Hãy tính khối lượng phân tử của urea và thành phần phần trăm theo khối lượng của nguyên tố nitrogen ($\text{N}$) trong urea (làm tròn đến chữ số thập phân thứ hai)."
                ),
                "solution": (
                    r"- Một phân tử $\text{(NH}_2)_2\text{CO}$ có $2$ nguyên tử $\text{N}$, $4$ nguyên tử $\text{H}$, $1$ nguyên tử $\text{C}$ và $1$ nguyên tử $\text{O}$." "\n"
                    r"- Khối lượng phân tử của urea là:" "\n"
                    r"$$M_{\text{(NH}_2)_2\text{CO}} = 2 \cdot 14 + 4 \cdot 1 + 12 + 16 = 60\text{ amu}$$" "\n"
                    r"- Phần trăm khối lượng của nguyên tố nitrogen ($\text{N}$) trong phân đạm urea là:" "\n"
                    r"$$\%m_{\text{N}} = \dfrac{2 \cdot 14}{60} \cdot 100\% = \dfrac{28}{60} \cdot 100\% \approx 46{,}67\%$$"
                ),
            },
        ],
        key_takeaways=[
            r"Đơn chất được tạo nên từ $1$ nguyên tố hóa học (dù phân tử có $1, 2$ hay $3$ nguyên tử như $\text{Fe}$, $\text{O}_2$, $\text{O}_3$).",
            r"Hợp chất được tạo nên từ $2$ nguyên tố hóa học trở lên liên kết với nhau ($\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NaCl}$, $\text{CH}_4$).",
            r"Thành phần phần trăm khối lượng của nguyên tố $\text{A}$ trong hợp chất $\text{A}_x\text{B}_y$ được tính bằng $\%m_{\text{A}} = \dfrac{x \cdot M_{\text{A}}}{M_{\text{A}_x\text{B}_y}} \cdot 100\%$.",
        ],
        questions=[
            mcq(
                r"Dãy chất nào dưới đây chỉ gồm toàn các **đơn chất**?",
                [
                    r"Muối ăn ($\text{NaCl}$), khí methane ($\text{CH}_4$), đá vôi ($\text{CaCO}_3$).",
                    r"Khí oxygen ($\text{O}_2$), kim loại iron ($\text{Fe}$), khí nitrogen ($\text{N}_2$), sulfur ($\text{S}$).",
                    r"Khí hydrogen ($\text{H}_2$), nước ($\text{H}_2\text{O}$), kim loại copper ($\text{Cu}$), carbon ($\text{C}$).",
                    r"Khí ozone ($\text{O}_3$), khí carbon dioxide ($\text{CO}_2$), khí chlorine ($\text{Cl}_2$).",
                ],
                "B",
                "biet",
                r"Các chất $\text{O}_2$, $\text{Fe}$, $\text{N}_2$, $\text{S}$ đều được tạo nên từ duy nhất $1$ nguyên tố hóa học tương ứng nên đều là đơn chất. Các chất $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NaCl}$, $\text{CH}_4$, $\text{CaCO}_3$ được tạo từ $2$ hay $3$ nguyên tố nên là hợp chất.",
            ),
            mcq(
                r"Dãy chất nào dưới đây chỉ gồm toàn các **hợp chất**?",
                [
                    r"Đường glucose ($\text{C}_6\text{H}_{12}\text{O}_6$), kim loại aluminium ($\text{Al}$), khí methane ($\text{CH}_4$).",
                    r"Khí helium ($\text{He}$), khí neon ($\text{Ne}$), khí argon ($\text{Ar}$).",
                    r"Nước ($\text{H}_2\text{O}$), khí ammonia ($\text{NH}_3$), muối ăn ($\text{NaCl}$), đá vôi ($\text{CaCO}_3$).",
                    r"Khí carbon dioxide ($\text{CO}_2$), khí chlorine ($\text{Cl}_2$), sulfuric acid ($\text{H}_2\text{SO}_4$).",
                ],
                "C",
                "biet",
                r"Các chất $\text{H}_2\text{O}$, $\text{NH}_3$, $\text{NaCl}$ và $\text{CaCO}_3$ đều được tạo nên từ $2$ hoặc $3$ nguyên tố hóa học khác nhau nên đều là hợp chất.",
            ),
            mcq(
                r"Kim cương và than chì (graphite dùng làm ruột bút chì và điện cực) là hai dạng thù hình khác nhau được tạo nên từ duy nhất nguyên tố carbon ($\text{C}$). Vậy kim cương và than chì thuộc loại:",
                [
                    r"Hợp chất hữu cơ.",
                    r"Đơn chất kim loại.",
                    r"Hợp chất vô cơ.",
                    r"Đơn chất phi kim.",
                ],
                "D",
                "biet",
                r"Kim cương và than chì đều chỉ được tạo nên từ một nguyên tố hóa học duy nhất là carbon ($\text{C}$ — nguyên tố phi kim), nên cả hai đều là đơn chất phi kim.",
            ),
            mcq(
                r"Cho biết khối lượng nguyên tử: $\text{C} = 12\text{ amu}$, $\text{H} = 1\text{ amu}$. Thành phần phần trăm theo khối lượng của nguyên tố carbon ($\text{C}$) trong hợp chất methane ($\text{CH}_4$) là:",
                [
                    r"$75\%$.",
                    r"$25\%$.",
                    r"$80\%$.",
                    r"$20\%$.",
                ],
                "A",
                "biet",
                r"Khối lượng phân tử của $\text{CH}_4$ là $M_{\text{CH}_4} = 12 + 4 \cdot 1 = 16\text{ amu}$. Phần trăm khối lượng của $\text{C}$ trong $\text{CH}_4$ là: $\%m_{\text{C}} = \dfrac{12}{16} \cdot 100\% = 75\%$.",
            ),
            mcq(
                r"Một bạn học sinh cho rằng: 'Khí ozone ($\text{O}_3$) là một hợp chất vì phân tử của nó có tới $3$ nguyên tử liên kết với nhau, còn khí carbon monoxide ($\text{CO}$) là đơn chất vì chỉ có $2$ nguyên tử'. Nhận xét nào sau đây sửa lại đúng hoàn toàn?",
                [
                    r"Khí ozone ($\text{O}_3$) là hỗn hợp, còn khí carbon monoxide ($\text{CO}$) là đơn chất.",
                    r"Khí ozone ($\text{O}_3$) là đơn chất vì chỉ tạo từ $1$ nguyên tố oxygen ($\text{O}$); còn $\text{CO}$ là hợp chất vì tạo từ $2$ nguyên tố là carbon ($\text{C}$) và oxygen ($\text{O}$).",
                    r"Cả khí ozone ($\text{O}_3$) và khí carbon monoxide ($\text{CO}$) đều là đơn chất.",
                    r"Cả khí ozone ($\text{O}_3$) và khí carbon monoxide ($\text{CO}$) đều là hợp chất.",
                ],
                "B",
                "hieu",
                r"Việc phân loại đơn chất hay hợp chất dựa vào **số nguyên tố hóa học** tạo nên chất, không phụ thuộc tổng số nguyên tử trong phân tử. $\text{O}_3$ chỉ gồm $1$ nguyên tố $\text{O}$ nên là đơn chất; $\text{CO}$ gồm $2$ nguyên tố $\text{C}$ và $\text{O}$ nên là hợp chất.",
            ),
            mcq(
                r"Biết khối lượng nguyên tử: $\text{Fe} = 56\text{ amu}$, $\text{O} = 16\text{ amu}$. Trong hai loại quặng sắt chứa hợp chất iron(III) oxide ($\text{Fe}_2\text{O}_3$, $M = 160\text{ amu}$) và iron(II,III) oxide ($\text{Fe}_3\text{O}_4$, $M = 232\text{ amu}$), hợp chất nào có hàm lượng phần trăm khối lượng iron ($\text{Fe}$) cao hơn?",
                [
                    r"Hai hợp chất $\text{Fe}_2\text{O}_3$ và $\text{Fe}_3\text{O}_4$ có phần trăm khối lượng $\text{Fe}$ bằng nhau.",
                    r"$\text{Fe}_2\text{O}_3$ có hàm lượng $\text{Fe}$ bằng $50\%$, lớn hơn $\text{Fe}_3\text{O}_4$ ($42{,}86\%$).",
                    r"$\text{Fe}_3\text{O}_4$ có hàm lượng $\text{Fe}$ cao hơn ($\%m_{\text{Fe}} \approx 72{,}41\% > 70{,}00\%$).",
                    r"$\text{Fe}_2\text{O}_3$ có hàm lượng $\text{Fe}$ cao hơn ($\%m_{\text{Fe}} = 75{,}00\% > 72{,}41\%$).",
                ],
                "C",
                "hieu",
                r"Trong $\text{Fe}_2\text{O}_3$: $\%m_{\text{Fe}} = \dfrac{2 \cdot 56}{160} \cdot 100\% = 70{,}00\%$. Trong $\text{Fe}_3\text{O}_4$: $\%m_{\text{Fe}} = \dfrac{3 \cdot 56}{232} \cdot 100\% \approx 72{,}41\%$. Vậy $\text{Fe}_3\text{O}_4$ giàu sắt hơn $\text{Fe}_2\text{O}_3$.",
            ),
            tf4(
                r"Xét tính chất, cấu tạo và phân loại của các chất tinh khiết sau: kim loại aluminium ($\text{Al}$), khí chlorine ($\text{Cl}_2$), nước ($\text{H}_2\text{O}$) và đường glucose ($\text{C}_6\text{H}_{12}\text{O}_6$). Các nhận định dưới đây là đúng hay sai?",
                [
                    r"Kim loại aluminium ($\text{Al}$) là đơn chất kim loại có tính dẻo, dẫn điện và dẫn nhiệt tốt; còn khí chlorine ($\text{Cl}_2$) là đơn chất phi kim ở thể khí màu vàng lục, mùi hắc và độc.",
                    r"Nước ($\text{H}_2\text{O}$) là hợp chất vô cơ, còn đường glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) là hợp chất hữu cơ.",
                    r"Vì nước ($\text{H}_2\text{O}$) được tạo nên từ hai nguyên tố hydrogen ($\text{H}$) và oxygen ($\text{O}$), nên nước giữ nguyên tính chất dễ cháy của khí $\text{H}_2$ và tính duy trì sự cháy của khí $\text{O}_2$.",
                    r"Trong hợp chất nước ($\text{H}_2\text{O}$, với $\text{H} = 1\text{ amu}$, $\text{O} = 16\text{ amu}$), khối lượng của nguyên tố oxygen ($\text{O}$) gấp $8$ lần khối lượng của nguyên tố hydrogen ($\text{H}$).",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: $\text{Al}$ là đơn chất kim loại, $\text{Cl}_2$ là đơn chất phi kim." "\n"
                    r"- **Ý b) Đúng**: $\text{H}_2\text{O}$ là hợp chất vô cơ phổ biến nhất; $\text{C}_6\text{H}_{12}\text{O}_6$ là hợp chất hữu cơ (carbohydrate)." "\n"
                    r"- **Ý c) Sai**: Khi các nguyên tố liên kết tạo thành hợp chất $\text{H}_2\text{O}$, phân tử hợp chất có tính chất hoàn toàn mới khác hẳn các đơn chất thành phần (nước là chất lỏng dùng để dập tắt đám cháy chứ không cháy như $\text{H}_2$)." "\n"
                    r"- **Ý d) Đúng**: Trong $1$ phân tử $\text{H}_2\text{O}$, tỉ lệ khối lượng $\dfrac{m_{\text{O}}}{m_{\text{H}}} = \dfrac{1 \cdot 16}{2 \cdot 1} = \dfrac{16}{2} = 8$ lần."
                ),
            ),
            tf4(
                r"Đá vôi tự nhiên có thành phần chính là hợp chất calcium carbonate ($\text{CaCO}_3$). Biết khối lượng nguyên tử: $\text{Ca} = 40\text{ amu}$, $\text{C} = 12\text{ amu}$, $\text{O} = 16\text{ amu}$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Hợp chất calcium carbonate ($\text{CaCO}_3$) được tạo nên từ $3$ nguyên tố hóa học là calcium ($\text{Ca}$), carbon ($\text{C}$) và oxygen ($\text{O}$).",
                    r"Khối lượng phân tử của $\text{CaCO}_3$ là $100\text{ amu}$, trong đó phần trăm khối lượng của nguyên tố calcium ($\text{Ca}$) là $40\%$.",
                    r"Phần trăm khối lượng của nguyên tố oxygen ($\text{O}$) trong $\text{CaCO}_3$ bằng $16\%$.",
                    r"Trong $250\text{ g}$ calcium carbonate ($\text{CaCO}_3$) tinh khiết có chứa đúng $100\text{ g}$ nguyên tố calcium ($\text{Ca}$) và $30\text{ g}$ nguyên tố carbon ($\text{C}$).",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: $\text{CaCO}_3$ được tạo từ $3$ nguyên tố: $\text{Ca}$, $\text{C}$ và $\text{O}$." "\n"
                    r"- **Ý b) Đúng**: $M_{\text{CaCO}_3} = 40 + 12 + 3 \cdot 16 = 100\text{ amu}$, suy ra $\%m_{\text{Ca}} = \dfrac{40}{100} \cdot 100\% = 40\%$." "\n"
                    r"- **Ý c) Sai**: Trong $\text{CaCO}_3$ có $3$ nguyên tử $\text{O}$ nên $\%m_{\text{O}} = \dfrac{3 \cdot 16}{100} \cdot 100\% = 48\%$ (không phải $16\%$)." "\n"
                    r"- **Ý d) Đúng**: Vì $\%m_{\text{Ca}} = 40\%$ và $\%m_{\text{C}} = 12\%$, nên trong $250\text{ g}$ $\text{CaCO}_3$ có $m_{\text{Ca}} = 250 \cdot 0{,}40 = 100\text{ g}$ và $m_{\text{C}} = 250 \cdot 0{,}12 = 30\text{ g}$."
                ),
            ),
            mcq(
                r"Một hợp chất khí $\text{A}$ được tạo bởi hai nguyên tố là sulfur ($\text{S} = 32\text{ amu}$) và oxygen ($\text{O} = 16\text{ amu}$), có khối lượng phân tử bằng $80\text{ amu}$, trong đó nguyên tố sulfur chiếm $40\%$ về khối lượng. Công thức hóa học của phân tử hợp chất $\text{A}$ là:",
                [
                    r"$\text{SO}_2$.",
                    r"$\text{S}_2\text{O}_3$.",
                    r"$\text{SO}_4$.",
                    r"$\text{SO}_3$.",
                ],
                "D",
                "vandung",
                r"Gọi công thức của $\text{A}$ là $\text{S}_x\text{O}_y$. Khối lượng nguyên tố $\text{S}$ trong $1$ phân tử $\text{A}$ là: $32x = \dfrac{40 \cdot 80}{100} = 32\text{ amu} \Rightarrow x = 1$. Khối lượng nguyên tố $\text{O}$ trong $1$ phân tử $\text{A}$ là: $16y = 80 - 32 = 48\text{ amu} \Rightarrow y = \dfrac{48}{16} = 3$. Vậy công thức phân tử của $\text{A}$ là $\text{SO}_3$ (sulfur trioxide).",
            ),
            short(
                r"Copper(II) sulfate khan có công thức hóa học là $\text{CuSO}_4$ (được dùng làm chất sát khuẩn, diệt nấm trong nông nghiệp và xử lý nước bể bơi). Biết khối lượng nguyên tử của các nguyên tố là $\text{Cu} = 64\text{ amu}$, $\text{S} = 32\text{ amu}$ và $\text{O} = 16\text{ amu}$. Hãy tính thành phần phần trăm về khối lượng của nguyên tố copper ($\text{Cu}$) trong hợp chất $\text{CuSO}_4$ theo đơn vị phần trăm ($\%$).",
                ["40", "40,0", "40.0"],
                "vandung",
                (
                    r"Khối lượng phân tử của hợp chất copper(II) sulfate ($\text{CuSO}_4$) là:" "\n"
                    r"$$M_{\text{CuSO}_4} = 64 + 32 + 4 \cdot 16 = 160\text{ amu}$$" "\n"
                    r"Thành phần phần trăm về khối lượng của nguyên tố copper ($\text{Cu}$) trong $\text{CuSO}_4$ là:" "\n"
                    r"$$\%m_{\text{Cu}} = \dfrac{64}{160} \cdot 100\% = 40\%$$"
                ),
            ),
        ],
        description="Phân biệt đơn chất kim loại, phi kim, khí hiếm với hợp chất vô cơ, hữu cơ và tính thành phần phần trăm khối lượng nguyên tố trong hợp chất.",
    ),
    lesson(
        grade=7,
        order=5,
        code="H7-C05",
        title="Chương 5: Giới thiệu về liên kết hóa học, hóa trị và công thức hóa học",
        topic="hoa-tri-lien-ket",
        summary=(
            r"Khi tham gia liên kết hóa học, nguyên tử của các nguyên tố có xu hướng đạt tới lớp vỏ electron bền vững của khí hiếm ($8\text{ electron}$ lớp ngoài cùng, hoặc $2\text{ electron}$ như helium $\text{He}$) bằng cách nhường - nhận electron tạo liên kết ion (như trong $\text{NaCl}$, $\text{MgO}$, $\text{CaCl}_2$) "
            r"hoặc dùng chung các cặp electron tạo liên kết cộng hóa trị (như trong $\text{H}_2$, $\text{O}_2$, $\text{N}_2$, $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NH}_3$). "
            r"Khả năng liên kết của nguyên tử được biểu thị bằng hóa trị (số La Mã $\text{I}, \text{II}, \text{III}...$), tuân theo quy tắc hóa trị $a \cdot x = b \cdot y$ giúp lập đúng công thức hóa học của mọi hợp chất."
        ),
        objectives=[
            r"Giải thích được xu hướng tạo lớp vỏ bền vững giống khí hiếm của các nguyên tử khi hình thành liên kết hóa học.",
            r"Trình bày được sự tạo thành liên kết ion (lực hút tĩnh điện giữa ion dương như $\text{Na}^+$, $\text{Mg}^{2+}$ và ion âm như $\text{Cl}^-$, $\text{O}^{2-}$) và sự tạo thành liên kết cộng hóa trị (dùng chung electron trong $\text{H}_2$, $\text{O}_2$, $\text{N}_2$, $\text{H}_2\text{O}$, $\text{CO}_2$, $\text{NH}_3$).",
            r"Phân biệt được tính chất vật lý cơ bản của hợp chất ion (rắn, nhiệt độ nóng chảy/sôi cao, dẫn điện khi tan trong nước) và chất cộng hóa trị.",
            r"Vận dụng được quy tắc hóa trị ($a \cdot x = b \cdot y$) để xác định hóa trị của nguyên tố hoặc lập công thức hóa học của hợp chất.",
        ],
        formulas=[
            {
                "name": "Sự tạo thành ion và liên kết ion",
                "formula": r"$\text{Na} \rightarrow \text{Na}^+ + 1e, \quad \text{Cl} + 1e \rightarrow \text{Cl}^- \implies \text{Na}^+ + \text{Cl}^- \rightarrow \text{NaCl}$",
                "note": r"Tương tự với magnesium oxide: $\text{Mg} \rightarrow \text{Mg}^{2+} + 2e$, $\text{O} + 2e \rightarrow \text{O}^{2-} \implies \text{MgO}$.",
            },
            {
                "name": "Quy tắc hóa trị trong hợp chất hai thành phần",
                "formula": r"$\text{Với hợp chất } \overset{a}{\text{A}}_x\overset{b}{\text{B}}_y: \quad a \cdot x = b \cdot y \iff \dfrac{x}{y} = \dfrac{b}{a} = \dfrac{b'}{a'}$",
                "note": r"$a, b$ là hóa trị (biểu diễn bằng chữ số La Mã $\text{I}, \text{II}, \text{III}, \text{IV}, \text{V}, \text{VI}, \text{VII}$); $x, y$ là chỉ số nguyên tử tối giản.",
            },
            {
                "name": "Hóa trị của một số nguyên tố và nhóm nguyên tử thông dụng",
                "formula": r"$\text{I}: \text{H, Na, K, Ag, Cl (trong muối), -OH, -NO}_3 \mid \text{II}: \text{O, Mg, Ca, Zn, Cu, Ba, =SO}_4, \text{=CO}_3 \mid \text{III}: \text{Al,}\equiv\text{PO}_4$",
                "note": r"Trong các hợp chất cộng hóa trị, hóa trị của một nguyên tố bằng số cặp electron dùng chung mà nguyên tử đó tạo ra với các nguyên tử khác.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Vỏ nguyên tử khí hiếm và sự tạo thành liên kết ion",
                "content": (
                    r"- **Đặc điểm vỏ khí hiếm**: Nguyên tử của các nguyên tố khí hiếm có lớp electron ngoài cùng đã bão hòa bền vững: $\text{He}$ có $2e$; $\text{Ne}$ ($2, 8$) và $\text{Ar}$ ($2, 8, 8$) đều có **$8\text{ electron}$ lớp ngoài cùng**. Để đạt được lớp vỏ bền vững giống khí hiếm gần nhất, nguyên tử của các nguyên tố khác có xu hướng **nhường, nhận** hoặc **góp chung electron**." "\n"
                    r"- **Sự tạo thành liên kết ion**:" "\n"
                    r"  + Nguyên tử **kim loại** (có $1, 2, 3e$ lớp ngoài cùng) dễ **nhường electron** lớp ngoài cùng để tạo thành **ion dương** (cation): ví dụ $\text{Na}$ ($2, 8, 1$) nhường $1e$ tạo ion $\text{Na}^+$ ($2, 8$ giống $\text{Ne}$); $\text{Mg}$ ($2, 8, 2$) nhường $2e$ tạo ion $\text{Mg}^{2+}$ ($2, 8$)." "\n"
                    r"  + Nguyên tử **phi kim** (có $5, 6, 7e$ lớp ngoài cùng) dễ **nhận thêm electron** để tạo thành **ion âm** (anion): ví dụ $\text{Cl}$ ($2, 8, 7$) nhận $1e$ tạo ion $\text{Cl}^-$ ($2, 8, 8$ giống $\text{Ar}$); $\text{O}$ ($2, 6$) nhận $2e$ tạo ion $\text{O}^{2-}$ ($2, 8$)." "\n"
                    r"  + Các ion mang điện tích trái dấu hút nhau bằng lực hút tĩnh điện tạo nên **liên kết ion** (ví dụ: $\text{NaCl}$, $\text{MgO}$, $\text{CaCl}_2$, $\text{K}_2\text{O}$). Hợp chất ion thường là chất rắn tinh thể ở điều kiện thường, khó bay hơi, có nhiệt độ nóng chảy và nhiệt độ sôi cao, khi tan trong nước tạo dung dịch dẫn được điện."
                ),
            },
            {
                "title": "2. Sự tạo thành liên kết cộng hóa trị",
                "content": (
                    r"- **Liên kết cộng hóa trị** là liên kết được tạo nên giữa hai nguyên tử bằng **một hay nhiều cặp electron dùng chung** (thường xảy ra giữa các nguyên tử phi kim với nhau)." "\n"
                    r"- **Ví dụ trong các phân tử điển hình**:" "\n"
                    r"  + Phân tử hydrogen ($\text{H}_2$): Mỗi nguyên tử $\text{H}$ (có $1e$) góp chung $1e$ tạo thành **$1$ cặp electron dùng chung** để cả hai đều đạt vỏ bền vững $2e$ giống khí hiếm $\text{He}$." "\n"
                    r"  + Phân tử oxygen ($\text{O}_2$): Mỗi nguyên tử $\text{O}$ ($6e$ lớp ngoài cùng) góp $2e$ tạo thành **$2$ cặp electron dùng chung** để mỗi nguyên tử đạt $8e$ giống $\text{Ne}$." "\n"
                    r"  + Phân tử nitrogen ($\text{N}_2$): Mỗi nguyên tử $\text{N}$ ($5e$ lớp ngoài cùng) góp $3e$ tạo thành **$3$ cặp electron dùng chung**." "\n"
                    r"  + Phân tử nước ($\text{H}_2\text{O}$): Nguyên tử $\text{O}$ góp chung với mỗi nguyên tử $\text{H}$ một cặp electron (có $2$ cặp electron dùng chung trong phân tử $\text{H}_2\text{O}$)." "\n"
                    r"  + Phân tử ammonia ($\text{NH}_3$): Nguyên tử $\text{N}$ có $3$ cặp electron dùng chung với $3$ nguyên tử $\text{H}$. Phân tử carbon dioxide ($\text{CO}_2$): Nguyên tử $\text{C}$ có $2$ cặp electron dùng chung với mỗi nguyên tử $\text{O}$ (tổng cộng $4$ cặp electron dùng chung)." "\n"
                    r"- Các chất cộng hóa trị có thể ở thể khí ($\text{H}_2, \text{O}_2, \text{CO}_2, \text{NH}_3$), thể lỏng ($\text{H}_2\text{O}, \text{C}_2\text{H}_5\text{OH}$) hoặc thể rắn (đường saccharose, lưu huỳnh $\text{S}$), thường có nhiệt độ nóng chảy và nhiệt độ sôi thấp hơn hợp chất ion."
                ),
            },
            {
                "title": "3. Hóa trị và quy tắc hóa trị – Lập công thức hóa học",
                "content": (
                    r"- **Hóa trị** là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác, được ghi bằng số La Mã ($\text{I}, \text{II}, \text{III}, \text{IV}, \text{V}, \text{VI}, \text{VII}$). Quy ước trong hợp chất cộng hóa trị, nguyên tố $\text{H}$ luôn có hóa trị $\text{I}$ và nguyên tố $\text{O}$ thường có hóa trị $\text{II}$." "\n"
                    r"- **Quy tắc hóa trị**: Trong công thức hóa học của hợp chất hai nguyên tố $\overset{a}{\text{A}}_x\overset{b}{\text{B}}_y$ (hoặc có nhóm nguyên tử), tích của chỉ số và hóa trị của nguyên tố này bằng tích của chỉ số và hóa trị của nguyên tố kia:" "\n"
                    r"$$a \cdot x = b \cdot y \implies \dfrac{x}{y} = \dfrac{b}{a}$$" "\n"
                    r"- **Cách lập công thức hóa học khi biết hóa trị**: Chọn $x, y$ là tỉ lệ tối giản của $\dfrac{b}{a}$. Ví dụ: Lập công thức hợp chất của aluminium ($\text{Al}$ hóa trị $\text{III}$) và nhóm sulfate ($(\text{SO}_4)$ hóa trị $\text{II}$): $\dfrac{x}{y} = \dfrac{\text{II}}{\text{III}} = \dfrac{2}{3} \Rightarrow$ công thức là $\text{Al}_2(\text{SO}_4)_3$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Giải thích sự tạo thành liên kết ion trong magnesium oxide (MgO)",
                "problem": (
                    r"Cho biết số hiệu nguyên tử của magnesium là $Z_{\text{Mg}} = 12$ và của oxygen là $Z_{\text{O}} = 8$. "
                    r"Hãy mô tả quá trình nhường - nhận electron để hình thành liên kết ion trong phân tử magnesium oxide ($\text{MgO}$)."
                ),
                "solution": (
                    r"- Nguyên tử $\text{Mg}$ ($Z = 12$, phân bố electron $2, 8, 2$) có $2e$ ở lớp ngoài cùng, dễ **nhường $2\text{ electron}$** cho nguyên tử $\text{O}$ để trở thành ion dương $\text{Mg}^{2+}$ có vỏ bền vững $(2, 8)$ giống khí hiếm neon ($\text{Ne}$)." "\n"
                    r"- Nguyên tử $\text{O}$ ($Z = 8$, phân bố electron $2, 6$) có $6e$ ở lớp ngoài cùng, **nhận $2\text{ electron}$** từ $\text{Mg}$ để trở thành ion âm $\text{O}^{2-}$ có vỏ bền vững $(2, 8)$ giống khí hiếm neon ($\text{Ne}$)." "\n"
                    r"- Hai ion mang điện tích trái dấu $\text{Mg}^{2+}$ và $\text{O}^{2-}$ hút nhau bằng lực hút tĩnh điện tạo thành hợp chất ion $\text{MgO}$."
                ),
            },
            {
                "title": "Ví dụ 2: Vận dụng quy tắc hóa trị xác định hóa trị và lập công thức hóa học",
                "problem": (
                    r"a) Tính hóa trị của nguyên tố iron ($\text{Fe}$) trong hợp chất $\text{Fe}_2\text{O}_3$ và của nguyên tố sulfur ($\text{S}$) trong hợp chất $\text{SO}_3$ (biết $\text{O}$ có hóa trị $\text{II}$)." "\n"
                    r"b) Lập công thức hóa học của hợp chất tạo bởi calcium ($\text{Ca}$ hóa trị $\text{II}$) và nhóm phosphate ($\text{PO}_4$ hóa trị $\text{III}$)."
                ),
                "solution": (
                    r"- **a)** Trong $\overset{a}{\text{Fe}}_2\overset{\text{II}}{\text{O}}_3$: Áp dụng quy tắc hóa trị $a \cdot 2 = \text{II} \cdot 3 = 6 \Rightarrow a = \text{III}$ (iron có hóa trị $\text{III}$). "
                    r"Trong $\overset{b}{\text{S}}\overset{\text{II}}{\text{O}}_3$: $b \cdot 1 = \text{II} \cdot 3 = 6 \Rightarrow b = \text{VI}$ (sulfur có hóa trị $\text{VI}$)." "\n"
                    r"- **b)** Gọi công thức là $\overset{\text{II}}{\text{Ca}}_x(\overset{\text{III}}{\text{PO}_4})_y$. Theo quy tắc hóa trị: $\text{II} \cdot x = \text{III} \cdot y \Rightarrow \dfrac{x}{y} = \dfrac{3}{2} \Rightarrow x = 3, y = 2$. Vậy công thức hóa học là $\text{Ca}_3(\text{PO}_4)_2$."
                ),
            },
        ],
        key_takeaways=[
            r"Liên kết ion hình thành do lực hút tĩnh điện giữa các ion trái dấu (thường giữa kim loại điển hình và phi kim điển hình như $\text{NaCl}, \text{MgO}, \text{CaCl}_2$).",
            r"Liên kết cộng hóa trị hình thành do sự dùng chung một hay nhiều cặp electron giữa hai nguyên tử (thường giữa các phi kim như $\text{H}_2, \text{O}_2, \text{N}_2, \text{H}_2\text{O}, \text{CO}_2, \text{NH}_3$).",
            r"Quy tắc hóa trị trong hợp chất $\overset{a}{\text{A}}_x\overset{b}{\text{B}}_y$: $a \cdot x = b \cdot y \iff \dfrac{x}{y} = \dfrac{b}{a}$.",
        ],
        questions=[
            mcq(
                r"Trong các chất dưới đây, chất nào được tạo thành bởi **liên kết ion**?",
                [
                    r"Sodium chloride ($\text{NaCl}$).",
                    r"Nước tinh khiết ($\text{H}_2\text{O}$).",
                    r"Khí carbon dioxide ($\text{CO}_2$).",
                    r"Khí nitrogen ($\text{N}_2$).",
                ],
                "A",
                "biet",
                r"Sodium chloride ($\text{NaCl}$) được hình thành từ lực hút tĩnh điện giữa ion dương kim loại $\text{Na}^+$ và ion âm phi kim $\text{Cl}^-$ nên có liên kết ion. Các chất $\text{H}_2\text{O}$, $\text{CO}_2$ và $\text{N}_2$ được tạo bởi liên kết cộng hóa trị.",
            ),
            mcq(
                r"Khi nguyên tử kim loại magnesium ($\text{Mg}$, có $2\text{ electron}$ lớp ngoài cùng) nhường đi $2\text{ electron}$ để đạt vỏ bền vững của khí hiếm neon ($\text{Ne}$), nó trở thành phần tử mang điện nào sau đây?",
                [
                    r"Nguyên tử neon ($\text{Ne}$) trung hòa điện.",
                    r"Ion dương $\text{Mg}^{2+}$.",
                    r"Ion âm $\text{Mg}^{2-}$.",
                    r"Ion dương $\text{Mg}^+$.",
                ],
                "B",
                "biet",
                r"Nguyên tử trung hòa điện khi nhường đi $2\text{ electron}$ (mang điện tích $-2$) sẽ dư $2$ điện tích dương của proton và trở thành ion dương $\text{Mg}^{2+}$.",
            ),
            mcq(
                r"Liên kết hóa học giữa các nguyên tử trong phân tử nước ($\text{H}_2\text{O}$), khí ammonia ($\text{NH}_3$) và khí oxygen ($\text{O}_2$) thuộc loại liên kết nào?",
                [
                    r"Liên kết kim loại.",
                    r"Không có liên kết hóa học nào giữa các nguyên tử.",
                    r"Liên kết cộng hóa trị (do dùng chung các cặp electron).",
                    r"Liên kết ion (do sự nhường và nhận hoàn toàn electron).",
                ],
                "C",
                "biet",
                r"Trong các phân tử $\text{H}_2\text{O}$, $\text{NH}_3$ và $\text{O}_2$, các nguyên tử phi kim ($\text{H}, \text{O}, \text{N}$) liên kết với nhau bằng cách góp chung các cặp electron nên đều là liên kết cộng hóa trị.",
            ),
            mcq(
                r"Biết nguyên tố oxygen ($\text{O}$) có hóa trị $\text{II}$. Hóa trị của nguyên tố nitrogen ($\text{N}$) trong hợp chất dinitrogen pentoxide ($\text{N}_2\text{O}_5$) là:",
                [
                    r"Hóa trị $\text{II}$.",
                    r"Hóa trị $\text{III}$.",
                    r"Hóa trị $\text{IV}$.",
                    r"Hóa trị $\text{V}$.",
                ],
                "D",
                "biet",
                r"Gọi hóa trị của $\text{N}$ trong $\overset{a}{\text{N}}_2\overset{\text{II}}{\text{O}}_5$ là $a$. Theo quy tắc hóa trị: $a \cdot 2 = \text{II} \cdot 5 = 10 \Rightarrow a = \text{V}$.",
            ),
            mcq(
                r"Trong một phân tử khí carbon dioxide ($\text{CO}_2$), biết nguyên tử carbon ($\text{C}$ có $4e$ lớp ngoài cùng) liên kết với $2$ nguyên tử oxygen (mỗi nguyên tử $\text{O}$ có $6e$ lớp ngoài cùng) để mọi nguyên tử đều đạt $8e$ lớp ngoài cùng. Tổng số cặp electron dùng chung trong toàn bộ một phân tử $\text{CO}_2$ là:",
                [
                    r"$4$ cặp electron dùng chung ($2$ cặp giữa $\text{C}$ với mỗi nguyên tử $\text{O}$).",
                    r"$2$ cặp electron dùng chung ($1$ cặp giữa $\text{C}$ với mỗi nguyên tử $\text{O}$).",
                    r"$1$ cặp electron dùng chung.",
                    r"$6$ cặp electron dùng chung.",
                ],
                "A",
                "hieu",
                r"Mỗi nguyên tử $\text{O}$ ($6e$ lớp ngoài cùng) cần thêm $2e$ nên góp chung $2e$ với nguyên tử $\text{C}$ tạo thành $2$ cặp electron dùng chung. Có $2$ nguyên tử $\text{O}$ liên kết với $1$ nguyên tử $\text{C}$ ($\text{O}=\text{C}=\text{O}$), nên tổng số cặp electron dùng chung trong phân tử $\text{CO}_2$ là $2 + 2 = 4$ cặp.",
            ),
            mcq(
                r"Công thức hóa học đúng của hợp chất tạo bởi kim loại aluminium ($\text{Al}$ có hóa trị $\text{III}$) và nhóm sulfate ($(\text{SO}_4)$ có hóa trị $\text{II}$) là:",
                [
                    r"$\text{Al}(\text{SO}_4)_3$.",
                    r"$\text{Al}_2(\text{SO}_4)_3$.",
                    r"$\text{Al}_3(\text{SO}_4)_2$.",
                    r"$\text{AlSO}_4$.",
                ],
                "B",
                "hieu",
                r"Gọi công thức hóa học là $\overset{\text{III}}{\text{Al}}_x(\overset{\text{II}}{\text{SO}_4})_y$. Theo quy tắc hóa trị: $\text{III} \cdot x = \text{II} \cdot y \Rightarrow \dfrac{x}{y} = \dfrac{2}{3} \Rightarrow x = 2, y = 3$. Vậy công thức đúng là $\text{Al}_2(\text{SO}_4)_3$.",
            ),
            tf4(
                r"Khi so sánh sự hình thành liên kết và tính chất của muối ăn sodium chloride ($\text{NaCl}$) với đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) và khí carbon dioxide ($\text{CO}_2$), xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Khi hình thành phân tử $\text{NaCl}$ từ nguyên tử $\text{Na}$ ($Z = 11$) và nguyên tử $\text{Cl}$ ($Z = 17$), nguyên tử $\text{Na}$ đã nhường $1\text{ electron}$ cho nguyên tử $\text{Cl}$ để tạo thành hai ion $\text{Na}^+$ và $\text{Cl}^-$.",
                    r"Hợp chất ion $\text{NaCl}$ có nhiệt độ nóng chảy rất cao ($801^\circ\text{C}$), còn hợp chất cộng hóa trị đường saccharose nóng chảy và phân hủy ở nhiệt độ thấp hơn nhiều (khoảng $185^\circ\text{C}$).",
                    r"Cả dung dịch muối ăn ($\text{NaCl}$) trong nước và dung dịch đường saccharose trong nước đều dẫn điện rất tốt.",
                    r"Trong phân tử khí ammonia ($\text{NH}_3$), hóa trị của nguyên tố nitrogen ($\text{N}$) là $\text{III}$ và bằng đúng số cặp electron dùng chung của nguyên tử $\text{N}$ với $3$ nguyên tử $\text{H}$.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: $\text{Na}$ ($2, 8, 1$) nhường $1e$ tạo $\text{Na}^+$ ($2, 8$); $\text{Cl}$ ($2, 8, 7$) nhận $1e$ tạo $\text{Cl}^-$ ($2, 8, 8$)." "\n"
                    r"- **Ý b) Đúng**: Hợp chất ion bền nhiệt và có nhiệt độ nóng chảy cao hơn hẳn hợp chất cộng hóa trị." "\n"
                    r"- **Ý c) Sai**: Dung dịch muối ăn ($\text{NaCl}$) chứa các ion tự do $\text{Na}^+$ và $\text{Cl}^-$ nên dẫn điện tốt; còn đường saccharose là hợp chất cộng hóa trị không phân li thành ion nên dung dịch nước đường **không dẫn điện**." "\n"
                    r"- **Ý d) Đúng**: Trong $\text{NH}_3$, nguyên tử $\text{N}$ có $3$ cặp electron dùng chung với $3$ nguyên tử $\text{H}$ (hóa trị $\text{I}$) nên $\text{N}$ có hóa trị $\text{III}$."
                ),
            ),
            tf4(
                r"Xét việc áp dụng quy tắc hóa trị ($a \cdot x = b \cdot y$) để kiểm tra và lập công thức hóa học của các hợp chất vô cơ. Biết hóa trị: $\text{Na}(\text{I})$, $\text{Ca}(\text{II})$, $\text{Al}(\text{III})$, $\text{C}(\text{IV})$, $\text{P}(\text{V})$, $\text{O}(\text{II})$, nhóm $-\text{OH}(\text{I})$, nhóm $-\text{NO}_3(\text{I})$, nhóm $=\text{CO}_3(\text{II})$. Các nhận định sau là đúng hay sai?",
                [
                    r"Công thức hóa học của hợp chất tạo bởi phosphorus ($\text{P}$ hóa trị $\text{V}$) và oxygen ($\text{O}$ hóa trị $\text{II}$) là $\text{P}_2\text{O}_5$.",
                    r"Công thức hóa học của calcium hydroxide (tạo bởi $\text{Ca}$ hóa trị $\text{II}$ và nhóm $-\text{OH}$ hóa trị $\text{I}$) được viết đúng là $\text{CaOH}_2$.",
                    r"Trong hai hợp chất $\text{FeCl}_2$ và $\text{FeCl}_3$ (với $\text{Cl}$ có hóa trị $\text{I}$), nguyên tố iron ($\text{Fe}$) thể hiện hai hóa trị khác nhau lần lượt là $\text{II}$ và $\text{III}$.",
                    r"Hợp chất tạo bởi sodium ($\text{Na}$ hóa trị $\text{I}$) và nhóm carbonate ($=\text{CO}_3$ hóa trị $\text{II}$) có công thức hóa học là $\text{Na}_2\text{CO}_3$.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Với $\overset{\text{V}}{\text{P}}_x\overset{\text{II}}{\text{O}}_y$, ta có $\dfrac{x}{y} = \dfrac{2}{5} \Rightarrow \text{P}_2\text{O}_5$." "\n"
                    r"- **Ý b) Sai**: Khi có từ $2$ nhóm nguyên tử trở lên phải đặt nhóm nguyên tử trong dấu ngoặc đơn, nên công thức đúng phải là **$\text{Ca(OH)}_2$** (viết $\text{CaOH}_2$ là sai)." "\n"
                    r"- **Ý c) Đúng**: Với $\text{Cl}(\text{I})$, trong $\text{FeCl}_2$ thì $\text{Fe}$ có hóa trị $\text{II}$; trong $\text{FeCl}_3$ thì $\text{Fe}$ có hóa trị $\text{III}$." "\n"
                    r"- **Ý d) Đúng**: Với $\overset{\text{I}}{\text{Na}}_x(\overset{\text{II}}{\text{CO}_3})_y$, ta có $\text{I} \cdot x = \text{II} \cdot y \Rightarrow x = 2, y = 1 \Rightarrow \text{Na}_2\text{CO}_3$."
                ),
            ),
            mcq(
                r"Nguyên tố kim loại $\text{M}$ tạo với oxygen ($\text{O}$ hóa trị $\text{II}$) hợp chất oxide có công thức $\text{M}_2\text{O}_3$. Khi nguyên tố $\text{M}$ (giữ nguyên hóa trị đó) liên kết với nhóm nitrate ($-\text{NO}_3$ có hóa trị $\text{I}$) thì tạo thành hợp chất muối có công thức hóa học và khối lượng phân tử (biết $\text{M}$ là aluminium $\text{Al} = 27\text{ amu}$, $\text{N} = 14\text{ amu}$, $\text{O} = 16\text{ amu}$) là:",
                [
                    r"$\text{Al(NO}_3)_2$ và $151\text{ amu}$.",
                    r"$\text{Al}_3\text{NO}_3$ và $143\text{ amu}$.",
                    r"$\text{Al(NO}_3)_3$ và $213\text{ amu}$.",
                    r"$\text{Al}_2(\text{NO}_3)_3$ và $240\text{ amu}$.",
                ],
                "C",
                "vandung",
                r"Từ công thức oxide $\overset{a}{\text{M}}_2\overset{\text{II}}{\text{O}}_3$, theo quy tắc hóa trị ta có $a \cdot 2 = \text{II} \cdot 3 \Rightarrow a = \text{III}$. Khi $\text{Al}(\text{III})$ liên kết với nhóm $-\text{NO}_3(\text{I})$, công thức muối là $\text{Al(NO}_3)_3$. Khối lượng phân tử là: $M = 27 + 3 \cdot (14 + 3 \cdot 16) = 27 + 3 \cdot 62 = 213\text{ amu}$.",
            ),
            short(
                r"Hợp chất tạo bởi nguyên tố iron ($\text{Fe}$ có hóa trị $\text{III}$) và nhóm sulfate ($=\text{SO}_4$ có hóa trị $\text{II}$) là muối iron(III) sulfate. Biết khối lượng nguyên tử của các nguyên tố là $\text{Fe} = 56\text{ amu}$, $\text{S} = 32\text{ amu}$ và $\text{O} = 16\text{ amu}$. Hãy lập công thức hóa học của muối iron(III) sulfate và tính khối lượng phân tử của hợp chất này theo đơn vị $\text{amu}$.",
                ["400", "400,0", "400.0"],
                "vandung",
                (
                    r"Gọi công thức của iron(III) sulfate là $\overset{\text{III}}{\text{Fe}}_x(\overset{\text{II}}{\text{SO}_4})_y$." "\n"
                    r"Theo quy tắc hóa trị: $\text{III} \cdot x = \text{II} \cdot y \Rightarrow \dfrac{x}{y} = \dfrac{2}{3} \Rightarrow x = 2, y = 3$. Công thức hóa học là $\text{Fe}_2(\text{SO}_4)_3$." "\n"
                    r"Khối lượng phân tử của $\text{Fe}_2(\text{SO}_4)_3$ là:" "\n"
                    r"$$M_{\text{Fe}_2(\text{SO}_4)_3} = 2 \cdot 56 + 3 \cdot (32 + 4 \cdot 16) = 112 + 3 \cdot 96 = 400\text{ amu}$$"
                ),
            ),
        ],
        description="Vỏ nguyên tử khí hiếm bền vững, sự tạo thành liên kết ion và liên kết cộng hóa trị, hóa trị, quy tắc hóa trị và lập công thức hóa học.",
    ),
    lesson(
        grade=7,
        order=6,
        code="H7-C06",
        title="Chương 6: Phản ứng hóa học và năng lượng trong phản ứng",
        topic="phan-ung-hoa-hoc",
        summary=(
            r"Phản ứng hóa học là quá trình biến đổi từ chất này (chất phản ứng) thành chất khác (sản phẩm). "
            r"Về mặt bản chất vi mô, trong một phản ứng hóa học chỉ có liên kết giữa các nguyên tử thay đổi làm cho phân tử này biến đổi thành phân tử khác, còn số nguyên tử của mỗi nguyên tố hóa học trước và sau phản ứng luôn giữ nguyên. "
            r"Mọi phản ứng hóa học đều kèm theo sự biến đổi năng lượng dưới dạng phản ứng tỏa nhiệt (giải phóng nhiệt ra môi trường) hoặc phản ứng thu nhiệt (hấp thụ nhiệt từ môi trường)."
        ),
        objectives=[
            r"Nêu được khái niệm phản ứng hóa học, phân biệt được chất phản ứng (chất tham gia) và chất sản phẩm (chất tạo thành).",
            r"Trình bày được diễn biến vi mô của phản ứng hóa học: liên kết giữa các nguyên tử thay đổi làm phân tử biến đổi, còn số lượng nguyên tử của mỗi nguyên tố được bảo toàn.",
            r"Nhận biết được phản ứng hóa học xảy ra dựa vào các dấu hiệu: xuất hiện chất khí ($\uparrow$), xuất hiện kết tủa ($\downarrow$), đổi màu sắc, tỏa nhiệt hoặc thu nhiệt.",
            r"Phân biệt được phản ứng tỏa nhiệt và phản ứng thu nhiệt, đồng thời lấy được ví dụ ứng dụng thực tiễn của các phản ứng tỏa nhiệt/thu nhiệt trong đời sống.",
        ],
        formulas=[
            {
                "name": "Sơ đồ tổng quát của một phản ứng hóa học",
                "formula": r"$\text{Các chất phản ứng (Chất tham gia)} \xrightarrow{\text{điều kiện}} \text{Các sản phẩm (Chất tạo thành)}$",
                "note": r"Trong quá trình phản ứng, lượng chất phản ứng giảm dần, còn lượng chất sản phẩm tăng dần.",
            },
            {
                "name": "Bản chất vi mô của phản ứng tổng hợp nước",
                "formula": r"$2\text{H}_2 + \text{O}_2 \xrightarrow{t^\circ} 2\text{H}_2\text{O}$",
                "note": r"Trước phản ứng: $\text{H}$ liên kết với $\text{H}$, $\text{O}$ liên kết với $\text{O}$ ($4\text{ nguyên tử H} + 2\text{ nguyên tử O}$). Sau phản ứng: $1\text{ O}$ liên kết với $2\text{ H}$ tạo $2\text{ phân tử H}_2\text{O}$ (vẫn là $4\text{ nguyên tử H} + 2\text{ nguyên tử O}$).",
            },
            {
                "name": "Phân biệt phản ứng tỏa nhiệt và phản ứng thu nhiệt",
                "formula": r"$\text{Tỏa nhiệt: Giải phóng nhiệt } (T_{\text{môi trường}} \uparrow) \quad \mid \quad \text{Thu nhiệt: Hấp thụ nhiệt } (T_{\text{môi trường}} \downarrow)$",
                "note": r"Ví dụ tỏa nhiệt: đốt nhiên liệu ($\text{C}, \text{CH}_4, \text{C}_2\text{H}_5\text{OH}$), tôi vôi ($\text{CaO} + \text{H}_2\text{O}$). Ví dụ thu nhiệt: nung đá vôi ($\text{CaCO}_3$), hòa tan viên C sủi.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Khái niệm và diễn biến của phản ứng hóa học",
                "content": (
                    r"- **Khái niệm**: **Phản ứng hóa học** là quá trình biến đổi từ chất này thành chất khác." "\n"
                    r"  + Chất ban đầu bị biến đổi trong phản ứng gọi là **chất phản ứng** (hay **chất tham gia**)." "\n"
                    r"  + Chất mới sinh ra gọi là **sản phẩm** (hay **chất tạo thành**)." "\n"
                    r"- **Diễn biến vi mô của phản ứng hóa học**:" "\n"
                    r"  + Trước phản ứng: Các nguyên tử liên kết với nhau trong các phân tử chất phản ứng." "\n"
                    r"  + Trong quá trình phản ứng: Các liên kết cũ bị phá vỡ và hình thành các liên kết mới theo trật tự khác." "\n"
                    r"  + **Kết luận cốt lõi**: Trong phản ứng hóa học, **chỉ có liên kết giữa các nguyên tử thay đổi** làm cho phân tử này biến đổi thành phân tử khác; còn **số nguyên tử của mỗi nguyên tố trước và sau phản ứng luôn giữ nguyên**." "\n"
                    r"  + *Lưu ý*: Nếu có đơn chất kim loại (như $\text{Zn}, \text{Fe}, \text{Mg}$) tham gia phản ứng thì sau phản ứng nguyên tử kim loại liên kết với hạt khác (như ion âm $\text{Cl}^-, \text{SO}_4^{2-}$)."
                ),
            },
            {
                "title": "2. Điều kiện và dấu hiệu nhận biết có phản ứng hóa học xảy ra",
                "content": (
                    r"- **Điều kiện để phản ứng xảy ra**: Các chất phản ứng phải **tiếp xúc** với nhau (diện tích tiếp xúc càng lớn phản ứng càng nhanh); nhiều phản ứng cần **đun nóng** đến nhiệt độ nhất định ($t^\circ$), và một số phản ứng cần có mặt **chất xúc tác** (ví dụ: phân hủy hydrogen peroxide $2\text{H}_2\text{O}_2 \xrightarrow{\text{MnO}_2} 2\text{H}_2\text{O} + \text{O}_2\uparrow$ có mặt xúc tác $\text{MnO}_2$)." "\n"
                    r"- **Dấu hiệu nhận biết có chất mới tạo thành**:" "\n"
                    r"  + Xuất hiện **chất khí** (sủi bọt khí $\uparrow$): Cho kẽm ($\text{Zn}$) vào dung dịch hydrochloric acid ($\text{HCl}$) thấy sủi bọt khí hydrogen ($\text{H}_2\uparrow$)." "\n"
                    r"  + Xuất hiện **chất kết tủa** ($\downarrow$): Cho dung dịch barium chloride ($\text{BaCl}_2$) vào dung dịch sodium sulfate ($\text{Na}_2\text{SO}_4$) tạo kết tủa trắng barium sulfate ($\text{BaSO}_4\downarrow$)." "\n"
                    r"  + Có sự **thay đổi màu sắc**, mùi hoặc sự **tỏa nhiệt, phát sáng**."
                ),
            },
            {
                "title": "3. Phản ứng tỏa nhiệt và phản ứng thu nhiệt",
                "content": (
                    r"- **Phản ứng tỏa nhiệt**: Là phản ứng hóa học **giải phóng năng lượng (dạng nhiệt)** ra môi trường xung quanh, làm nhiệt độ của hỗn hợp phản ứng và môi trường xung quanh **tăng lên**." "\n"
                    r"  + *Ví dụ*: Phản ứng đốt cháy nhiên liệu (than $\text{C}$, khí methane $\text{CH}_4$, cồn ethanol $\text{C}_2\text{H}_5\text{OH}$, xăng dầu); phản ứng tôi vôi sống ($\text{CaO} + \text{H}_2\text{O} \rightarrow \text{Ca(OH)}_2$ làm nước sôi bốc hơi); phản ứng hô hấp oxy hóa glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) trong cơ thể giúp giữ ấm thân nhiệt ở $37^\circ\text{C}$." "\n"
                    r"- **Phản ứng thu nhiệt**: Là phản ứng hóa học **hấp thụ năng lượng (dạng nhiệt)** từ môi trường xung quanh trong suốt quá trình phản ứng (làm nhiệt độ xung quanh **giảm xuống** hoặc cần phải cung cấp nhiệt liên tục, nếu ngừng đun thì phản ứng dừng lại)." "\n"
                    r"  + *Ví dụ*: Phản ứng nung đá vôi ($\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$); phản ứng quang hợp của cây xanh; phản ứng giữa baking soda ($\text{NaHCO}_3$) và citric acid trong viên sủi vitamin C khi thả vào cốc nước làm cốc nước mát lạnh đi."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân tích diễn biến vi mô của phản ứng đốt cháy khí methane",
                "problem": (
                    r"Xét phản ứng đốt cháy khí methane ($\text{CH}_4$) trong khí oxygen ($\text{O}_2$) theo sơ đồ: $\text{CH}_4 + 2\text{O}_2 \xrightarrow{t^\circ} \text{CO}_2 + 2\text{H}_2\text{O}$. "
                    r"Hãy so sánh sự liên kết giữa các nguyên tử và số lượng nguyên tử mỗi nguyên tố ($\text{C}, \text{H}, \text{O}$) trước và sau khi phản ứng xảy ra."
                ),
                "solution": (
                    r"- **Trước phản ứng**: $1$ nguyên tử $\text{C}$ liên kết với $4$ nguyên tử $\text{H}$ (trong $1$ phân tử $\text{CH}_4$); các nguyên tử $\text{O}$ liên kết từng đôi một (trong $2$ phân tử $\text{O}_2$). Tổng số nguyên tử là: $1\text{ C}, 4\text{ H}, 4\text{ O}$." "\n"
                    r"- **Sau phản ứng**: Liên kết thay đổi, $1$ nguyên tử $\text{C}$ liên kết với $2$ nguyên tử $\text{O}$ tạo $1$ phân tử $\text{CO}_2$; $2$ nguyên tử $\text{O}$ còn lại mỗi nguyên tử liên kết với $2$ nguyên tử $\text{H}$ tạo $2$ phân tử $\text{H}_2\text{O}$. Tổng số nguyên tử vẫn là: $1\text{ C}, 4\text{ H}, 4\text{ O}$ (được bảo toàn hoàn toàn)."
                ),
            },
            {
                "title": "Ví dụ 2: Phân biệt phản ứng tỏa nhiệt và phản ứng thu nhiệt qua nhiệt kế",
                "problem": (
                    r"Trong phòng thí nghiệm ở $25^\circ\text{C}$, học sinh thực hiện hai thí nghiệm trong hai cốc thủy tinh có cắm sẵn nhiệt kế:" "\n"
                    r"- Cốc 1: Cho vôi sống ($\text{CaO}$) tác dụng với nước ($\text{H}_2\text{O}$), nhiệt kế chỉ giá trị tăng từ $25^\circ\text{C}$ lên $75^\circ\text{C}$." "\n"
                    r"- Cốc 2: Cho viên sủi vitamin C (chứa $\text{NaHCO}_3$ và citric acid) vào nước, nhiệt kế chỉ giá trị giảm từ $25^\circ\text{C}$ xuống $21^\circ\text{C}$." "\n"
                    r"Hãy cho biết phản ứng trong mỗi cốc là phản ứng tỏa nhiệt hay thu nhiệt."
                ),
                "solution": (
                    r"- **Cốc 1**: Nhiệt độ của hệ tăng mạnh từ $25^\circ\text{C}$ lên $75^\circ\text{C}$ chứng tỏ phản ứng giải phóng nhiệt năng ra môi trường $\rightarrow$ đây là **phản ứng tỏa nhiệt**." "\n"
                    r"- **Cốc 2**: Nhiệt độ của hệ giảm từ $25^\circ\text{C}$ xuống $21^\circ\text{C}$ chứng tỏ phản ứng đã hấp thụ nhiệt năng từ nước trong cốc $\rightarrow$ đây là **phản ứng thu nhiệt**."
                ),
            },
        ],
        key_takeaways=[
            r"Trong một phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi làm phân tử này biến đổi thành phân tử khác, còn số lượng nguyên tử mỗi nguyên tố giữ nguyên.",
            r"Trong quá trình phản ứng, lượng chất phản ứng giảm dần, còn lượng chất sản phẩm tăng dần.",
            r"Phản ứng tỏa nhiệt giải phóng nhiệt làm tăng nhiệt độ môi trường; phản ứng thu nhiệt hấp thụ nhiệt làm giảm nhiệt độ môi trường (hoặc cần đun nóng liên tục).",
        ],
        questions=[
            mcq(
                r"Trong một phản ứng hóa học, đại lượng hay yếu tố nào sau đây **luôn thay đổi** để làm cho phân tử này biến đổi thành phân tử khác?",
                [
                    r"Số lượng nguyên tử của mỗi nguyên tố hóa học.",
                    r"Điện tích hạt nhân ($Z$) của mỗi nguyên tử.",
                    r"Tổng số hạt proton ($p$) của các nguyên tử.",
                    r"Liên kết giữa các nguyên tử.",
                ],
                "D",
                "biet",
                r"Bản chất của phản ứng hóa học là sự thay đổi liên kết giữa các nguyên tử, làm phân tử này biến đổi thành phân tử khác; còn số nguyên tử của mỗi nguyên tố và cấu tạo hạt nhân nguyên tử hoàn toàn giữ nguyên.",
            ),
            mcq(
                r"Xét phản ứng hóa học: $\text{Iron } (\text{Fe}) + \text{Sulfur } (\text{S}) \xrightarrow{t^\circ} \text{Iron(II) sulfide } (\text{FeS})$. Trong phản ứng trên, đâu là các chất phản ứng và đâu là sản phẩm?",
                [
                    r"Chất phản ứng là $\text{Fe}$ và $\text{S}$; sản phẩm là $\text{FeS}$.",
                    r"Chất phản ứng là $\text{FeS}$; sản phẩm là $\text{Fe}$ và $\text{S}$.",
                    r"Chất phản ứng là $\text{Fe}$; sản phẩm là $\text{S}$ và $\text{FeS}$.",
                    r"Cả $\text{Fe}$, $\text{S}$ và $\text{FeS}$ đều là sản phẩm.",
                ],
                "A",
                "biet",
                r"Các chất ban đầu bị biến đổi (đứng trước mũi tên) là $\text{Fe}$ và $\text{S}$ gọi là chất phản ứng; chất mới tạo thành (đứng sau mũi tên) là $\text{FeS}$ gọi là sản phẩm.",
            ),
            mcq(
                r"Phản ứng hóa học nào sau đây là một **phản ứng tỏa nhiệt**?",
                [
                    r"Phản ứng hòa tan viên sủi vitamin C vào cốc nước làm cốc nước lạnh đi.",
                    r"Phản ứng đốt cháy cồn ethanol ($\text{C}_2\text{H}_5\text{OH}$) hoặc khí gas ($\text{CH}_4$, $\text{C}_3\text{H}_8$) trong không khí.",
                    r"Phản ứng nung đá vôi ($\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$) cần cung cấp nhiệt liên tục.",
                    r"Phản ứng nhiệt phân thuốc tím ($\text{KMnO}_4$) trong phòng thí nghiệm.",
                ],
                "B",
                "biet",
                r"Phản ứng đốt cháy nhiên liệu (cồn ethanol, khí gas, than, củi) giải phóng một lượng lớn nhiệt năng ra môi trường xung quanh nên là phản ứng tỏa nhiệt. Ba phản ứng còn lại đều là phản ứng thu nhiệt.",
            ),
            mcq(
                r"Khi cho một viên kẽm ($\text{Zn}$) vào ống nghiệm đựng dung dịch hydrochloric acid ($\text{HCl}$), dấu hiệu dễ quan sát nhất cho thấy đã có phản ứng hóa học xảy ra là:",
                [
                    r"Dung dịch trong ống nghiệm chuyển sang màu tím sẫm.",
                    r"Viên kẽm nở to gấp đôi và phát ra tia sáng màu đỏ.",
                    r"Viên kẽm tan dần và có các bọt khí hydrogen ($\text{H}_2\uparrow$) không màu sủi lên mạnh từ bề mặt viên kẽm.",
                    r"Xuất hiện chất kết tủa màu xanh lam lắng xuống đáy ống nghiệm.",
                ],
                "C",
                "biet",
                r"Kẽm ($\text{Zn}$) tác dụng với dung dịch $\text{HCl}$ theo phản ứng $\text{Zn} + 2\text{HCl} \rightarrow \text{ZnCl}_2 + \text{H}_2\uparrow$, dấu hiệu đặc trưng là viên kẽm tan dần và sủi bọt khí không màu ($\text{H}_2\uparrow$).",
            ),
            mcq(
                r"Trong phản ứng tổng hợp khí ammonia từ khí nitrogen và khí hydrogen theo sơ đồ: $\text{N}_2 + 3\text{H}_2 \xrightarrow{t^\circ, p, \text{xt}} 2\text{NH}_3$. Khi có $1$ phân tử $\text{N}_2$ phản ứng vừa đủ với $3$ phân tử $\text{H}_2$, nhận xét nào sau đây về số nguyên tử trước và sau phản ứng là **đúng**?",
                [
                    r"Sau phản ứng số nguyên tử $\text{N}$ tăng lên gấp đôi và số nguyên tử $\text{H}$ giảm đi một nửa.",
                    r"Trước phản ứng có $4$ nguyên tử, sau phản ứng chỉ còn $2$ nguyên tử.",
                    r"Trong phản ứng, các nguyên tử $\text{H}$ đã biến đổi thành nguyên tử $\text{N}$.",
                    r"Trước và sau phản ứng đều có đúng $2$ nguyên tử $\text{N}$ và $6$ nguyên tử $\text{H}$, chỉ có liên kết thay đổi tạo thành $2$ phân tử $\text{NH}_3$.",
                ],
                "D",
                "hieu",
                r"Trước phản ứng: $1$ phân tử $\text{N}_2$ ($2$ nguyên tử $\text{N}$) và $3$ phân tử $\text{H}_2$ ($3 \cdot 2 = 6$ nguyên tử $\text{H}$). Sau phản ứng: tạo $2$ phân tử $\text{NH}_3$ gồm $2 \cdot 1 = 2$ nguyên tử $\text{N}$ và $2 \cdot 3 = 6$ nguyên tử $\text{H}$. Số nguyên tử mỗi nguyên tố được bảo toàn tuyệt đối.",
            ),
            mcq(
                r"Tại sao khi nung đá vôi ($\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$) người ta phải đốt lò cung cấp nhiệt liên tục từ đầu đến cuối, còn khi đốt cháy than đá ($\text{C} + \text{O}_2 \xrightarrow{t^\circ} \text{CO}_2$) thì chỉ cần khơi mào lửa lúc đầu rồi than tự cháy tiếp?",
                [
                    r"Vì phản ứng nung đá vôi là phản ứng thu nhiệt (ngừng cung cấp nhiệt thì phản ứng dừng lại), còn phản ứng đốt than là phản ứng tỏa nhiệt (nhiệt tỏa ra tự duy trì phản ứng).",
                    r"Vì đá vôi ($\text{CaCO}_3$) là chất khí, còn than đá ($\text{C}$) là chất lỏng.",
                    r"Vì phản ứng nung đá vôi là phản ứng tỏa nhiệt quá mạnh nên cần làm nguội.",
                    r"Vì phản ứng đốt than đá là phản ứng thu nhiệt từ không khí.",
                ],
                "A",
                "hieu",
                r"Phản ứng phân hủy $\text{CaCO}_3$ là phản ứng thu nhiệt nên cần cung cấp nhiệt liên tục ở khoảng $1000^\circ\text{C}$. Ngược lại, phản ứng cháy của than $\text{C}$ với $\text{O}_2$ chỉ cần đun nóng ban đầu để đạt nhiệt độ bắt cháy, sau đó phản ứng tỏa ra lượng nhiệt lớn tự duy trì sự cháy.",
            ),
            tf4(
                r"Xét thí nghiệm cho dung dịch barium chloride ($\text{BaCl}_2$) không màu vào ống nghiệm đựng dung dịch sodium sulfate ($\text{Na}_2\text{SO}_4$) không màu ở nhiệt độ phòng: ngay lập tức xuất hiện chất rắn màu trắng không tan là barium sulfate ($\text{BaSO}_4\downarrow$) làm đục ống nghiệm, đồng thời tạo ra muối sodium chloride ($\text{NaCl}$) tan trong nước. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Trong phản ứng trên, các chất phản ứng là $\text{BaCl}_2$ và $\text{Na}_2\text{SO}_4$; các chất sản phẩm là $\text{BaSO}_4$ và $\text{NaCl}$.",
                    r"Dấu hiệu giúp nhận biết phản ứng hóa học đã xảy ra là sự xuất hiện chất kết tủa màu trắng ($\text{BaSO}_4\downarrow$).",
                    r"Theo thời gian diễn ra phản ứng, lượng $\text{BaCl}_2$ và $\text{Na}_2\text{SO}_4$ tăng dần, còn lượng $\text{BaSO}_4$ giảm dần.",
                    r"Tổng số nguyên tử của mỗi nguyên tố ($\text{Ba}, \text{Cl}, \text{Na}, \text{S}, \text{O}$) trước và sau phản ứng hoàn toàn bằng nhau.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Hai chất ban đầu là $\text{BaCl}_2$ và $\text{Na}_2\text{SO}_4$; hai chất mới tạo thành là $\text{BaSO}_4\downarrow$ và $\text{NaCl}$." "\n"
                    r"- **Ý b) Đúng**: Sự tạo thành chất rắn không tan màu trắng ($\text{BaSO}_4\downarrow$) từ hai dung dịch trong suốt là dấu hiệu rõ nét của phản ứng." "\n"
                    r"- **Ý c) Sai**: Trong quá trình phản ứng, lượng các chất phản ứng ($\text{BaCl}_2, \text{Na}_2\text{SO}_4$) **giảm dần**, còn lượng sản phẩm ($\text{BaSO}_4, \text{NaCl}$) **tăng dần**." "\n"
                    r"- **Ý d) Đúng**: Mọi phản ứng hóa học đều bảo toàn số lượng nguyên tử của mỗi nguyên tố."
                ),
            ),
            tf4(
                r"Xét sự biến đổi năng lượng (tỏa nhiệt và thu nhiệt) trong các quá trình hóa học thực tiễn sau. Các nhận định dưới đây là đúng hay sai?",
                [
                    r"Trong các túi chườm nóng tự sôi dùng trong y tế hoặc khẩu phần ăn tự sôi, người ta ứng dụng các phản ứng tỏa nhiệt mạnh (như phản ứng của $\text{CaO}$ hoặc hỗn hợp bột $\text{Mg} - \text{Fe}$ với nước).",
                    r"Quá trình hô hấp tế bào trong cơ thể người (oxy hóa glucose $\text{C}_6\text{H}_{12}\text{O}_6$ bằng khí $\text{O}_2$ tạo $\text{CO}_2$ và $\text{H}_2\text{O}$) là một phản ứng thu nhiệt làm cơ thể lạnh đi.",
                    r"Trong các túi chườm lạnh tức thời dùng sơ cứu chấn thương thể thao, việc hòa tan ammonium nitrate ($\text{NH}_4\text{NO}_3$) với nước hấp thụ nhiệt mạnh làm nhiệt độ túi giảm nhanh xuống gần $0^\circ\text{C}$.",
                    r"Khi đốt cháy $1\text{ kg}$ khí hóa lỏng LPG tỏa ra nhiệt lượng khoảng $46\text{ MJ}$, nhiệt lượng này được chuyển hóa một phần thành nhiệt năng làm chín thức ăn.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Túi chườm nóng và hộp cơm tự sôi dựa trên phản ứng hóa học tỏa nhiệt mạnh để làm nóng mà không cần lửa." "\n"
                    r"- **Ý b) Sai**: Phản ứng oxy hóa glucose ($\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \rightarrow 6\text{CO}_2 + 6\text{H}_2\text{O}$) trong cơ thể là **phản ứng tỏa nhiệt**, cung cấp năng lượng cho cơ bắp hoạt động và duy trì thân nhiệt $37^\circ\text{C}$." "\n"
                    r"- **Ý c) Đúng**: Quá trình này thu nhiệt mạnh từ môi trường làm túi chườm lạnh đi nhanh chóng để giảm sưng đau." "\n"
                    r"- **Ý d) Đúng**: Sự cháy của khí LPG là phản ứng tỏa nhiệt cung cấp năng lượng nhiệt cho việc đun nấu."
                ),
            ),
            mcq(
                r"Khi đốt cháy hoàn toàn một số phân tử khí ethane ($\text{C}_2\text{H}_6$) trong khí oxygen ($\text{O}_2$), sau phản ứng thu được đúng $4$ phân tử khí carbon dioxide ($\text{CO}_2$) và $6$ phân tử nước ($\text{H}_2\text{O}$). Dựa vào sự bảo toàn số nguyên tử của mỗi nguyên tố trong phản ứng hóa học, số phân tử $\text{C}_2\text{H}_6$ và số phân tử $\text{O}_2$ đã tham gia phản ứng lần lượt là:",
                [
                    r"$1$ phân tử $\text{C}_2\text{H}_6$ và $4$ phân tử $\text{O}_2$.",
                    r"$2$ phân tử $\text{C}_2\text{H}_6$ và $7$ phân tử $\text{O}_2$.",
                    r"$2$ phân tử $\text{C}_2\text{H}_6$ và $5$ phân tử $\text{O}_2$.",
                    r"$4$ phân tử $\text{C}_2\text{H}_6$ và $7$ phân tử $\text{O}_2$.",
                ],
                "B",
                "vandung",
                r"Sau phản ứng, trong $4\text{ phân tử CO}_2$ và $6\text{ phân tử H}_2\text{O}$ có: $4\text{ nguyên tử C}$, $6 \cdot 2 = 12\text{ nguyên tử H}$, và $4 \cdot 2 + 6 \cdot 1 = 14\text{ nguyên tử O}$. Vì số nguyên tử mỗi nguyên tố giữ nguyên: số phân tử $\text{C}_2\text{H}_6$ cần là $\dfrac{4}{2} = 2$ phân tử (chứa đúng $4\text{ C}$ và $12\text{ H}$); số phân tử $\text{O}_2$ cần là $\dfrac{14}{2} = 7$ phân tử.",
            ),
            short(
                r"Để đun sôi một ấm nước cần cung cấp một nhiệt lượng hữu ích là $660\text{ kJ}$. Biết khi đốt cháy hoàn toàn $1\text{ g}$ khí methane ($\text{CH}_4$) tỏa ra nhiệt lượng là $55\text{ kJ}$, nhưng hiệu suất hấp thụ nhiệt của ấm nước chỉ đạt $60\%$ (phần nhiệt còn lại tỏa ra môi trường không khí). Hãy tính khối lượng khí methane ($\text{CH}_4$) cần đốt cháy theo đơn vị gam ($\text{g}$).",
                ["20", "20,0", "20.0"],
                "vandung",
                (
                    r"Vì hiệu suất hấp thụ nhiệt của ấm nước là $60\%$, nên tổng nhiệt lượng toàn phần mà phản ứng đốt cháy $\text{CH}_4$ cần tỏa ra là:" "\n"
                    r"$$Q_{\text{tỏa}} = \dfrac{660}{60\%} = \dfrac{660 \cdot 100}{60} = 1100\text{ kJ}$$" "\n"
                    r"Khối lượng khí methane ($\text{CH}_4$) cần đốt cháy là:" "\n"
                    r"$$m_{\text{CH}_4} = \dfrac{1100}{55} = 20\text{ g}$$"
                ),
            ),
        ],
        description="Khái niệm phản ứng hóa học, chất phản ứng, sản phẩm, diễn biến vi mô của phản ứng và phân biệt phản ứng tỏa nhiệt với phản ứng thu nhiệt.",
    ),
    lesson(
        grade=7,
        order=7,
        code="H7-C07",
        title="Chương 7: Định luật bảo toàn khối lượng và phương trình chữ",
        topic="bao-toan-khoi-luong",
        summary=(
            r"Phương trình chữ biểu diễn ngắn gọn tên các chất tham gia và sản phẩm của một phản ứng hóa học. "
            r"Theo Định luật bảo toàn khối lượng do hai nhà bác học Lomonosov và Lavoisier độc lập tìm ra: 'Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng'. "
            r"Định luật này có cơ sở từ sự bảo toàn số lượng nguyên tử của mỗi nguyên tố trước và sau phản ứng, giúp ta dễ dàng tính được khối lượng của một chất bất kỳ khi biết khối lượng của các chất còn lại."
        ),
        objectives=[
            r"Viết được phương trình chữ của các phản ứng hóa học thông dụng ($\text{Tên các chất phản ứng} \xrightarrow{\text{điều kiện}} \text{Tên các sản phẩm}$).",
            r"Phát biểu được nội dung Định luật bảo toàn khối lượng của Lomonosov – Lavoisier và giải thích được định luật dựa trên sự bảo toàn số lượng nguyên tử trong phản ứng hóa học.",
            r"Viết được biểu thức bảo toàn khối lượng cho một phản ứng cụ thể ($m_{\text{A}} + m_{\text{B}} = m_{\text{C}} + m_{\text{D}}$) và giải thích được sự thay đổi khối lượng chất rắn khi nung hoặc đốt trong bình hở.",
            r"Vận dụng thành thạo Định luật bảo toàn khối lượng để tính khối lượng chất tham gia hoặc sản phẩm trong các bài toán thực tế.",
        ],
        formulas=[
            {
                "name": "Biểu thức Định luật bảo toàn khối lượng",
                "formula": r"$\sum m_{\text{chất tham gia}} = \sum m_{\text{sản phẩm}} \iff m_{\text{A}} + m_{\text{B}} = m_{\text{C}} + m_{\text{D}}$",
                "note": r"Đối với phản ứng $\text{A} + \text{B} \rightarrow \text{C} + \text{D}$, chỉ tính khối lượng phần chất thực sự đã tham gia phản ứng.",
            },
            {
                "name": "Quy tắc viết phương trình chữ của phản ứng hóa học",
                "formula": r"$\text{Tên chất phản ứng 1} + \text{Tên chất phản ứng 2} \xrightarrow{\text{điều kiện}} \text{Tên sản phẩm 1} + \text{Tên sản phẩm 2}$",
                "note": r"Dấu $+$ ở vế trái đọc là 'tác dụng với'; mũi tên $\rightarrow$ đọc là 'tạo thành'; dấu $+$ ở vế phải đọc là 'và'.",
            },
            {
                "name": "Bảo toàn khối lượng khi chất rắn tham gia phản ứng có chất khí",
                "formula": r"$m_{\text{kim loại}} + m_{\text{O}_2\text{ phản ứng}} = m_{\text{oxide}}; \quad m_{\text{CaCO}_3\text{ phân hủy}} = m_{\text{CaO}} + m_{\text{CO}_2\uparrow}$",
                "note": r"Đốt kim loại trong không khí thì khối lượng chất rắn tăng thêm bằng $m_{\text{O}_2}$; nung đá vôi thì khối lượng chất rắn giảm đi bằng $m_{\text{CO}_2\uparrow}$ thoát ra.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Phương trình chữ của phản ứng hóa học",
                "content": (
                    r"- Để biểu diễn một phản ứng hóa học một cách trực quan bằng tên các chất, ta viết **phương trình chữ**:" "\n"
                    r"$$\text{Tên các chất phản ứng} \xrightarrow{\text{điều kiện}} \text{Tên các chất sản phẩm}$$" "\n"
                    r"- **Ví dụ 1**: Đốt cháy than (carbon, $\text{C}$) trong khí oxygen ($\text{O}_2$) tạo thành khí carbon dioxide ($\text{CO}_2$):" "\n"
                    r"$$\text{Carbon} + \text{Oxygen} \xrightarrow{t^\circ} \text{Carbon dioxide}$$" "\n"
                    r"  *(Đọc là: Carbon tác dụng với oxygen ở nhiệt độ cao tạo thành carbon dioxide)*." "\n"
                    r"- **Ví dụ 2**: Cho kẽm (zinc, $\text{Zn}$) tác dụng với dung dịch hydrochloric acid ($\text{HCl}$) tạo thành muối zinc chloride ($\text{ZnCl}_2$) và khí hydrogen ($\text{H}_2$):" "\n"
                    r"$$\text{Zinc} + \text{Hydrochloric acid} \rightarrow \text{Zinc chloride} + \text{Hydrogen}$$"
                ),
            },
            {
                "title": "2. Nội dung và giải thích Định luật bảo toàn khối lượng",
                "content": (
                    r"- **Thí nghiệm kiểm chứng**: Cho dung dịch barium chloride ($\text{BaCl}_2$) tác dụng với dung dịch sodium sulfate ($\text{Na}_2\text{SO}_4$) trên cân điện tử tạo kết tủa trắng barium sulfate ($\text{BaSO}_4\downarrow$) và dung dịch sodium chloride ($\text{NaCl}$). Số chỉ của cân trước và sau phản ứng giữ nguyên không đổi." "\n"
                    r"- **Nội dung định luật (Lomonosov – Lavoisier)**: *'Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng'*." "\n"
                    r"- **Giải thích bản chất vi mô**: Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi, còn **số lượng nguyên tử của mỗi nguyên tố trước và sau phản ứng giữ nguyên**, mà khối lượng của mỗi nguyên tử là không đổi nên tổng khối lượng các chất được bảo toàn tuyệt đối." "\n"
                    r"- **Biểu thức toán học**: Giả sử có phản ứng $\text{A} + \text{B} \rightarrow \text{C} + \text{D}$, ta luôn có:" "\n"
                    r"$$m_{\text{A}} + m_{\text{B}} = m_{\text{C}} + m_{\text{D}}$$" "\n"
                    r"  Nếu biết khối lượng của $3$ trong $4$ chất, ta tính ngay được khối lượng chất còn lại (ví dụ: $m_{\text{D}} = m_{\text{A}} + m_{\text{B}} - m_{\text{C}}$)."
                ),
            },
            {
                "title": "3. Giải thích các hiện tượng tăng - giảm khối lượng chất rắn trong bình hở",
                "content": (
                    r"- **Trường hợp 1 (Khối lượng chất rắn tăng lên khi nung trong không khí)**: Khi đốt dây magnesium ($\text{Mg}$) hoặc đinh iron ($\text{Fe}$) trên đĩa cân ngoài không khí, chất rắn thu được là oxide ($\text{MgO}$, $\text{Fe}_3\text{O}_4$) có khối lượng lớn hơn kim loại ban đầu vì kim loại đã kết hợp thêm với một lượng **khí oxygen ($\text{O}_2$)** từ không khí: $m_{\text{MgO}} = m_{\text{Mg}} + m_{\text{O}_2}$." "\n"
                    r"- **Trường hợp 2 (Khối lượng chất rắn giảm đi khi nung trong bình hở)**: Khi nung đá vôi ($\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$) trên đĩa cân hở, chất rắn còn lại là vôi sống ($\text{CaO}$) nhẹ hơn đá vôi ban đầu vì **khí carbon dioxide ($\text{CO}_2\uparrow$)** sinh ra đã bay vào không khí: $m_{\text{CaO}} = m_{\text{CaCO}_3} - m_{\text{CO}_2\uparrow}$."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Tính khối lượng khí oxygen tham gia đốt cháy magnesium",
                "problem": (
                    r"Đốt cháy hoàn toàn $4{,}8\text{ g}$ kim loại magnesium ($\text{Mg}$) trong không khí thu được $8{,}0\text{ g}$ chất rắn màu trắng là hợp chất magnesium oxide ($\text{MgO}$)." "\n"
                    r"a) Viết phương trình chữ của phản ứng." "\n"
                    r"b) Viết công thức về khối lượng và tính khối lượng khí oxygen ($\text{O}_2$) đã phản ứng."
                ),
                "solution": (
                    r"- **a) Phương trình chữ**:" "\n"
                    r"$$\text{Magnesium} + \text{Oxygen} \xrightarrow{t^\circ} \text{Magnesium oxide}$$" "\n"
                    r"- **b) Áp dụng Định luật bảo toàn khối lượng**:" "\n"
                    r"$$m_{\text{Mg}} + m_{\text{O}_2} = m_{\text{MgO}} \implies m_{\text{O}_2} = m_{\text{MgO}} - m_{\text{Mg}} = 8{,}0 - 4{,}8 = 3{,}2\text{ g}$$"
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán nung đá vôi có lẫn tạp chất trơ",
                "problem": (
                    r"Nung nóng một mẫu đá vôi chứa $100\text{ kg}$ calcium carbonate ($\text{CaCO}_3$) nguyên chất. Sau khi $\text{CaCO}_3$ phân hủy hoàn toàn thu được $56\text{ kg}$ vôi sống (calcium oxide, $\text{CaO}$) và một lượng khí carbon dioxide ($\text{CO}_2\uparrow$) thoát ra. "
                    r"Tính khối lượng khí $\text{CO}_2$ đã thoát ra."
                ),
                "solution": (
                    r"- Phương trình chữ của phản ứng:" "\n"
                    r"$$\text{Calcium carbonate} \xrightarrow{t^\circ} \text{Calcium oxide} + \text{Carbon dioxide}$$" "\n"
                    r"- Theo Định luật bảo toàn khối lượng:" "\n"
                    r"$$m_{\text{CaCO}_3} = m_{\text{CaO}} + m_{\text{CO}_2} \implies m_{\text{CO}_2} = 100 - 56 = 44\text{ kg}$$"
                ),
            },
        ],
        key_takeaways=[
            r"Định luật bảo toàn khối lượng: Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng.",
            r"Cơ sở của định luật là trong phản ứng hóa học, số lượng nguyên tử của mỗi nguyên tố trước và sau phản ứng không đổi.",
            r"Khi áp dụng công thức bảo toàn khối lượng, phải tính đầy đủ cả khối lượng các chất khí tham gia (như $\text{O}_2$) hoặc thoát ra khỏi hệ (như $\text{CO}_2\uparrow$, $\text{H}_2\uparrow$) và chỉ tính phần chất thực sự phản ứng.",
        ],
        questions=[
            mcq(
                r"Nội dung của **Định luật bảo toàn khối lượng** do hai nhà khoa học Lomonosov và Lavoisier phát biểu là:",
                [
                    r"Trong một phản ứng hóa học, tổng số phân tử của các chất sản phẩm luôn bằng tổng số phân tử của các chất tham gia.",
                    r"Khi đun nóng một chất rắn ngoài không khí, khối lượng chất rắn sau phản ứng luôn bằng khối lượng chất rắn ban đầu.",
                    r"Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng.",
                    r"Trong một phản ứng hóa học, tổng thể tích của các chất sản phẩm luôn bằng tổng thể tích của các chất tham gia.",
                ],
                "C",
                "biet",
                r"Theo Định luật bảo toàn khối lượng: Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng.",
            ),
            mcq(
                r"Vì sao trong một phản ứng hóa học, tổng khối lượng của các chất được bảo toàn?",
                [
                    r"Vì số lượng phân tử trước và sau mọi phản ứng hóa học luôn bằng nhau.",
                    r"Vì thể tích bình chứa không thay đổi trong suốt quá trình phản ứng.",
                    r"Vì các nguyên tử mới được sinh ra có khối lượng bằng đúng các nguyên tử cũ bị mất đi.",
                    r"Vì trong phản ứng hóa học chỉ có liên kết giữa các nguyên tử thay đổi, còn số lượng nguyên tử của mỗi nguyên tố giữ nguyên.",
                ],
                "D",
                "biet",
                r"Trong phản ứng hóa học, số lượng nguyên tử của mỗi nguyên tố trước và sau phản ứng giữ nguyên và khối lượng mỗi nguyên tử không đổi, vì vậy tổng khối lượng các chất trước và sau phản ứng bằng nhau.",
            ),
            mcq(
                r"Cho phản ứng hóa học: $\text{Barium chloride } (\text{BaCl}_2) + \text{Sodium sulfate } (\text{Na}_2\text{SO}_4) \rightarrow \text{Barium sulfate } (\text{BaSO}_4\downarrow) + \text{Sodium chloride } (\text{NaCl})$. Biểu thức đúng theo Định luật bảo toàn khối lượng là:",
                [
                    r"$m_{\text{BaCl}_2} + m_{\text{Na}_2\text{SO}_4} = m_{\text{BaSO}_4} + m_{\text{NaCl}}$.",
                    r"$m_{\text{BaCl}_2} + m_{\text{BaSO}_4} = m_{\text{Na}_2\text{SO}_4} + m_{\text{NaCl}}$.",
                    r"$m_{\text{BaCl}_2} - m_{\text{Na}_2\text{SO}_4} = m_{\text{BaSO}_4} - m_{\text{NaCl}}$.",
                    r"$m_{\text{BaCl}_2} = m_{\text{Na}_2\text{SO}_4} + m_{\text{BaSO}_4} + m_{\text{NaCl}}$.",
                ],
                "A",
                "biet",
                r"Tổng khối lượng hai chất tham gia ($\text{BaCl}_2$ và $\text{Na}_2\text{SO}_4$) bằng tổng khối lượng hai chất sản phẩm ($\text{BaSO}_4$ và $\text{NaCl}$): $m_{\text{BaCl}_2} + m_{\text{Na}_2\text{SO}_4} = m_{\text{BaSO}_4} + m_{\text{NaCl}}$.",
            ),
            mcq(
                r"Khi cho kim loại iron ($\text{Fe}$) tác dụng với dung dịch hydrochloric acid ($\text{HCl}$) tạo ra muối iron(II) chloride ($\text{FeCl}_2$) và khí hydrogen ($\text{H}_2\uparrow$), phương trình chữ đúng của phản ứng là:",
                [
                    r"$\text{Iron} + \text{Chlorine} \rightarrow \text{Iron(II) chloride}$.",
                    r"$\text{Iron} + \text{Hydrochloric acid} \rightarrow \text{Iron(II) chloride} + \text{Hydrogen}$.",
                    r"$\text{Iron} + \text{Hydrogen} \rightarrow \text{Iron(II) chloride} + \text{Hydrochloric acid}$.",
                    r"$\text{Iron(II) chloride} + \text{Hydrogen} \rightarrow \text{Iron} + \text{Hydrochloric acid}$.",
                ],
                "B",
                "biet",
                r"Các chất tham gia phản ứng ghi ở bên trái mũi tên ($\text{Iron} + \text{Hydrochloric acid}$), các chất sản phẩm ghi ở bên phải mũi tên ($\text{Iron(II) chloride} + \text{Hydrogen}$).",
            ),
            mcq(
                r"Đốt cháy hoàn toàn $9\text{ g}$ kim loại aluminium ($\text{Al}$) trong khí oxygen ($\text{O}_2$) thu được $17\text{ g}$ hợp chất aluminium oxide ($\text{Al}_2\text{O}_3$). Khối lượng khí oxygen ($\text{O}_2$) đã tham gia phản ứng là:",
                [
                    r"$9\text{ g}$.",
                    r"$17\text{ g}$.",
                    r"$8\text{ g}$.",
                    r"$26\text{ g}$.",
                ],
                "C",
                "hieu",
                r"Theo Định luật bảo toàn khối lượng cho phản ứng $\text{Aluminium} + \text{Oxygen} \xrightarrow{t^\circ} \text{Aluminium oxide}$: $m_{\text{Al}} + m_{\text{O}_2} = m_{\text{Al}_2\text{O}_3} \Rightarrow m_{\text{O}_2} = 17 - 9 = 8\text{ g}$.",
            ),
            mcq(
                r"Đặt một chén sứ chứa bột kim loại copper ($\text{Cu}$) màu đỏ lên đĩa cân điện tử ở trạng thái mở ngoài không khí rồi nung nóng mạnh để $\text{Cu}$ tác dụng với khí oxygen ($\text{O}_2$) tạo thành chất rắn màu đen là copper(II) oxide ($\text{CuO}$). Sau khi để nguội, số chỉ của cân điện tử thay đổi như thế nào so với trước khi nung?",
                [
                    r"Số chỉ của cân giảm đi vì khi đun nóng kim loại copper ($\text{Cu}$) nhẹ hơn.",
                    r"Số chỉ của cân giữ nguyên không đổi vì Định luật bảo toàn khối lượng.",
                    r"Số chỉ của cân giảm về $0$ vì $\text{CuO}$ là chất khí bay đi mất.",
                    r"Số chỉ của cân tăng lên vì chất rắn trong chén đã kết hợp thêm với khối lượng khí oxygen ($\text{O}_2$) từ không khí.",
                ],
                "D",
                "hieu",
                r"Theo Định luật bảo toàn khối lượng: $m_{\text{CuO}} = m_{\text{Cu}} + m_{\text{O}_2\text{ phản ứng}}$. Vì ban đầu cân chỉ đo khối lượng của $\text{Cu}$ trong chén sứ (chưa tính khí $\text{O}_2$ ngoài không khí), còn sau khi nung khí $\text{O}_2$ đã hóa hợp tạo thành chất rắn $\text{CuO}$ nằm trong chén, nên khối lượng chất rắn trên cân tăng thêm đúng bằng $m_{\text{O}_2\text{ phản ứng}}$.",
            ),
            tf4(
                r"Một học sinh cho $6{,}5\text{ g}$ hạt kim loại zinc ($\text{Zn}$) vào một cốc thủy tinh chứa sẵn $100\text{ g}$ dung dịch hydrochloric acid ($\text{HCl}$) loãng đặt trên đĩa cân (cốc không đậy nắp). Phản ứng xảy ra hoàn toàn theo phương trình chữ: $\text{Zinc} + \text{Hydrochloric acid} \rightarrow \text{Zinc chloride} + \text{Hydrogen}\uparrow$, biết toàn bộ lượng khí hydrogen ($\text{H}_2\uparrow$) thoát ra khỏi cốc có khối lượng là $0{,}2\text{ g}$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Tổng khối lượng của hạt zinc ($\text{Zn}$) và dung dịch acid ($\text{HCl}$) trong cốc ngay lúc vừa cho vào (trước khi khí thoát ra) là $106{,}5\text{ g}$.",
                    r"Sau khi phản ứng kết thúc và khí hydrogen ($\text{H}_2\uparrow$) đã bay hết ra ngoài không khí, khối lượng dung dịch còn lại trong cốc trên đĩa cân vẫn là $106{,}5\text{ g}$.",
                    r"Khối lượng dung dịch còn lại trong cốc sau khi phản ứng kết thúc bằng $106{,}3\text{ g}$.",
                    r"Nếu thực hiện thí nghiệm trên trong một bình kín hoàn toàn (khí $\text{H}_2$ không thoát ra ngoài) thì tổng khối lượng của cả bình trước và sau phản ứng đều bằng nhau.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Tổng khối lượng ban đầu trong cốc là $6{,}5 + 100 = 106{,}5\text{ g}$." "\n"
                    r"- **Ý b) Sai**: Vì cốc mở nắp nên $0{,}2\text{ g}$ khí $\text{H}_2\uparrow$ đã thoát ra khỏi cốc vào không khí, làm số chỉ trên cân giảm đi $0{,}2\text{ g}$." "\n"
                    r"- **Ý c) Đúng**: Theo bảo toàn khối lượng: $m_{\text{dd sau}} = 6{,}5 + 100 - m_{\text{H}_2\uparrow} = 106{,}5 - 0{,}2 = 106{,}3\text{ g}$." "\n"
                    r"- **Ý d) Đúng**: Trong bình kín, khí $\text{H}_2$ vẫn nằm trong bình nên tổng khối lượng của hệ trước và sau phản ứng bằng nhau tuyệt đối ($106{,}5\text{ g}$)."
                ),
            ),
            tf4(
                r"Xét phản ứng đốt cháy hoàn toàn khí methane ($\text{CH}_4$) trong khí oxygen ($\text{O}_2$) tạo thành khí carbon dioxide ($\text{CO}_2$) và hơi nước ($\text{H}_2\text{O}$). Biết rằng cứ đốt cháy hết $16\text{ g}$ $\text{CH}_4$ thì cần dùng vừa đủ $64\text{ g}$ $\text{O}_2$ và thu được $44\text{ g}$ $\text{CO}_2$ cùng một lượng hơi nước ($\text{H}_2\text{O}$). Xét tính đúng/sai của các nhận định sau:",
                [
                    r"Phương trình chữ của phản ứng là: $\text{Methane} + \text{Oxygen} \xrightarrow{t^\circ} \text{Carbon dioxide} + \text{Water}$.",
                    r"Tổng khối lượng của hai chất sản phẩm ($\text{CO}_2$ và $\text{H}_2\text{O}$) thu được khi đốt hết $16\text{ g}$ $\text{CH}_4$ là $80\text{ g}$.",
                    r"Khối lượng hơi nước ($\text{H}_2\text{O}$) tạo thành trong phản ứng trên là $36\text{ g}$.",
                    r"Nếu đem đốt $8\text{ g}$ khí $\text{CH}_4$ trong một bình kín chỉ chứa $20\text{ g}$ khí $\text{O}_2$ thì cả hai chất $\text{CH}_4$ và $\text{O}_2$ đều phản ứng hết không còn dư.",
                ],
                "Đ/Đ/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Chất tham gia là methane và oxygen; sản phẩm là carbon dioxide và water (hơi nước)." "\n"
                    r"- **Ý b) Đúng**: Theo Định luật bảo toàn khối lượng: $m_{\text{CO}_2} + m_{\text{H}_2\text{O}} = m_{\text{CH}_4} + m_{\text{O}_2} = 16 + 64 = 80\text{ g}$." "\n"
                    r"- **Ý c) Đúng**: Ta có $m_{\text{H}_2\text{O}} = 80 - m_{\text{CO}_2} = 80 - 44 = 36\text{ g}$." "\n"
                    r"- **Ý d) Sai**: Theo tỉ lệ phản ứng, cứ $16\text{ g}$ $\text{CH}_4$ cần $64\text{ g}$ $\text{O}_2$ (tức $1\text{ g}$ $\text{CH}_4$ cần $4\text{ g}$ $\text{O}_2$). Vậy $8\text{ g}$ $\text{CH}_4$ cần tới $32\text{ g}$ $\text{O}_2$; do bình chỉ có $20\text{ g}$ $\text{O}_2$ nên $\text{O}_2$ hết trước và $\text{CH}_4$ còn dư $8 - \dfrac{20}{4} = 3\text{ g}$."
                ),
            ),
            mcq(
                r"Một viên than tổ ong nặng $1200\text{ g}$ chứa $90\%$ khối lượng là carbon ($\text{C}$) nguyên chất, phần còn lại ($10\%$) là tạp chất đất sét trơ không cháy. Khi đốt cháy hoàn toàn viên than này trong không khí, phần carbon ($\text{C}$) tác dụng hết với $2880\text{ g}$ khí oxygen ($\text{O}_2$) tạo thành khí carbon dioxide ($\text{CO}_2\uparrow$) thoát ra ngoài, còn toàn bộ tạp chất đất sét ở lại trong bã xỉ than. Khối lượng khí $\text{CO}_2$ đã thoát vào không khí là:",
                [
                    r"$3960\text{ g}$.",
                    r"$4080\text{ g}$.",
                    r"$1080\text{ g}$.",
                    r"$3840\text{ g}$.",
                ],
                "A",
                "vandung",
                r"Khối lượng carbon ($\text{C}$) nguyên chất thực sự tham gia phản ứng cháy là: $m_{\text{C}} = 1200 \cdot \dfrac{90}{100} = 1080\text{ g}$ (phần tạp chất $120\text{ g}$ không tham gia phản ứng). Theo Định luật bảo toàn khối lượng cho phản ứng $\text{C} + \text{O}_2 \xrightarrow{t^\circ} \text{CO}_2$: $m_{\text{CO}_2} = m_{\text{C}} + m_{\text{O}_2} = 1080 + 2880 = 3960\text{ g}$.",
            ),
            short(
                r"Trong một lò nung vôi công nghiệp, người ta đem nung một lượng đá vôi thì có $150\text{ kg}$ calcium carbonate ($\text{CaCO}_3$) bị phân hủy hoàn toàn tạo thành $84\text{ kg}$ vôi sống (calcium oxide, $\text{CaO}$) và khí carbon dioxide ($\text{CO}_2\uparrow$) thoát ra theo phương trình chữ: $\text{Calcium carbonate} \xrightarrow{t^\circ} \text{Calcium oxide} + \text{Carbon dioxide}$. Hãy áp dụng Định luật bảo toàn khối lượng để tính khối lượng khí carbon dioxide ($\text{CO}_2$) đã thoát ra theo đơn vị kilôgam ($\text{kg}$).",
                ["66", "66,0", "66.0"],
                "vandung",
                (
                    r"Áp dụng Định luật bảo toàn khối lượng cho phản ứng phân hủy $\text{CaCO}_3$:" "\n"
                    r"$$m_{\text{CaCO}_3} = m_{\text{CaO}} + m_{\text{CO}_2}$$" "\n"
                    r"Khối lượng khí carbon dioxide ($\text{CO}_2$) đã thoát ra là:" "\n"
                    r"$$m_{\text{CO}_2} = m_{\text{CaCO}_3} - m_{\text{CaO}} = 150 - 84 = 66\text{ kg}$$"
                ),
            ),
        ],
        description="Phương trình chữ của phản ứng hóa học, nội dung và giải thích Định luật bảo toàn khối lượng của Lomonosov - Lavoisier và bài toán tính khối lượng trong phản ứng.",
    ),
]


LESSONS = LESSONS_GRADE_7
