"""Hóa học 10 — Kết nối tri thức với cuộc sống.
Cấu trúc: Lớp 10 -> 7 Chương -> 21 Bài học độc lập.
Mỗi bài có đúng công thức của bài đó, 3+ yêu cầu cần đạt, 10 câu hỏi.
"""
from ._helpers import bai, F, G, mcq, tf, short

GRADE = 10

# =========================================================================
# CHƯƠNG 1: CẤU TẠO NGUYÊN TỬ
# =========================================================================
CH1_ID = "hoa10_ch1"
CH1_TITLE = "Chương 1: Cấu tạo nguyên tử"
CH1_DESC = "Thành phần nguyên tử, nguyên tố hóa học, đồng vị, nguyên tử khối trung bình và cấu hình electron nguyên tử"

CH1_LESSONS = [
    bai(1, "Thành phần của nguyên tử",
        "Cấu tạo nguyên tử gồm hạt nhân (proton, neutron) và vỏ electron; khối lượng, điện tích các hạt cơ bản",
        "Nguyên tử vô cùng nhỏ nhưng cấu tạo gồm hai phần: hạt nhân ở tâm (chứa các hạt proton $p$ mang điện tích $+1$ và các hạt neutron $n$ không mang điện) và lớp vỏ gồm các hạt electron $e$ mang điện tích $-1$ chuyển động rất nhanh xung quanh hạt nhân. Nguyên tử trung hòa về điện nên số proton luôn bằng số electron ($Z = N_p = N_e$). Khối lượng của electron rất nhỏ ($m_e \\approx 0,00055\\text{ amu}$) so với khối lượng của proton và neutron ($m_p \\approx m_n \\approx 1\\text{ amu}$), do đó khối lượng của nguyên tử tập trung hầu hết ở hạt nhân.",
        [
            F("Điều kiện trung hòa điện của nguyên tử", "Z = N_p = N_e", "Số đơn vị điện tích hạt nhân (Z) = số proton = số electron"),
            F("Tổng số hạt cơ bản trong nguyên tử", "S = N_p + N_n + N_e = 2Z + N", "Với nguyên tử bền (2 <= Z <= 82) ta luôn có 1 <= N/Z <= 1,52"),
            F("Khối lượng và điện tích các hạt cơ bản", "m_p \\approx m_n \\approx 1\\text{ amu},\\quad m_e \\approx 0,00055\\text{ amu};\\quad q_p = +1,\\; q_e = -1,\\; q_n = 0", "1 amu = 1,6605 * 10^-27 kg; điện tích nguyên tố e0 = 1,602 * 10^-19 C"),
        ],
        [
            "Trình bày được thành phần cấu tạo của nguyên tử gồm hạt nhân (proton, neutron) và lớp vỏ electron",
            "So sánh được khối lượng và điện tích của electron với proton và neutron",
            "Giải được bài toán xác định số hạt $p, n, e$ dựa vào tổng số hạt $S = 2Z + N$",
        ],
        "Tổng số hạt cơ bản ($p, n, e$) trong một nguyên tử nguyên tố $X$ là $40$, trong đó tổng số hạt mang điện nhiều hơn số hạt không mang điện là $12$. Tìm số proton $Z$ và số neutron $N$ của $X$.",
        "Ta có hệ phương trình:\\n$\\begin{cases} 2Z + N = 40 \\\\ 2Z - N = 12 \\end{cases} \\Rightarrow \\begin{cases} 4Z = 52 \\\\ N = 2Z - 12 \\end{cases} \\Rightarrow \\begin{cases} Z = 13 \\\\ N = 14 \\end{cases}$.\\nVậy nguyên tử $X$ có $13$ proton ($13$ electron) và $14$ neutron (Aluminium - $\\text{Al}$).",
        "Thí nghiệm bắn phá lá vàng mỏng bằng chùm hạt alpha của Rutherford chứng minh nguyên tử có cấu tạo rỗng, phần lớn khối lượng tập trung ở hạt nhân có kích thước rất nhỏ ở tâm.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Hạt cơ bản nào trong nguyên tử KHÔNG mang điện tích?", "Neutron ($n$)", ["Neutron ($n$)", "Proton ($p$)", "Electron ($e$)", "Hạt nhân"], "Trong nguyên tử, proton mang điện $+1$, electron mang điện $-1$, còn neutron không mang điện ($q_n = 0$).", "biet"),
            mcq("Nguyên tử hầu như toàn bộ khối lượng tập trung ở hạt nhân vì:", "Khối lượng của electron ở lớp vỏ rất nhỏ so với khối lượng của proton và neutron", ["Khối lượng của electron ở lớp vỏ rất nhỏ so với khối lượng của proton và neutron", "Hạt nhân có kích thước lớn hơn rất nhiều so với lớp vỏ", "Nguyên tử không có electron", "Neutron nằm ở lớp vỏ nguyên tử"], "$m_e \\approx 0,00055\\text{ amu} \\ll m_p \\approx m_n \\approx 1\\text{ amu}$.", "hieu"),
            short("Một nguyên tử có tổng số hạt ($p, n, e$) là $28$, trong đó số hạt không mang điện là $10$. Số hiệu nguyên tử $Z$ (số proton) của nguyên tử đó bằng bao nhiêu?", "9", ["9"], "Ta có $2Z + N = 28$ và $N = 10 \\Rightarrow 2Z = 18 \\Rightarrow Z = 9$.", "vandung"),
        ]
    ),
    bai(2, "Nguyên tố hóa học",
        "Số hiệu nguyên tử Z, số khối A, kí hiệu nguyên tử, đồng vị và công thức tính nguyên tử khối trung bình",
        "Nguyên tố hóa học là tập hợp các nguyên tử có cùng số đơn vị điện tích hạt nhân ($Z$). Số khối ($A$) của hạt nhân bằng tổng số proton ($Z$) và tổng số neutron ($N$): $A = Z + N$. Kí hiệu nguyên tử được viết là $^A_Z\\text{X}$. Các đồng vị của cùng một nguyên tố hóa học là những nguyên tử có cùng số proton ($Z$) nhưng khác nhau về số neutron ($N$), do đó số khối ($A$) của chúng khác nhau. Nguyên tử khối trung bình ($\\overline{A}$) của nguyên tố có nhiều đồng vị được tính theo phần trăm số nguyên tử của các đồng vị trong tự nhiên.",
        [
            F("Số khối và Kí hiệu nguyên tử", "A = Z + N;\\quad \\text{Kí hiệu: } ^A_Z\\text{X}", "Z là số hiệu nguyên tử (số proton), A là số khối"),
            F("Công thức tính Nguyên tử khối trung bình", "\\overline{A} = \\frac{A_1 x_1 + A_2 x_2 + \\dots + A_k x_k}{100}", "Ai là số khối và xi (%) là phần trăm số nguyên tử của đồng vị thứ i (x1 + x2 + ... = 100)"),
            F("Ba đồng vị tự nhiên của Hydrogen", "^1_1\\text{H}\\text{ (Protium)},\\quad ^2_1\\text{H}\\text{ (Deuterium)},\\quad ^3_1\\text{H}\\text{ (Tritium)}", "Cùng Z = 1 nhưng có số neutron lần lượt là 0, 1, 2"),
        ],
        [
            "Trình bày được khái niệm về nguyên tố hóa học, số hiệu nguyên tử ($Z$), số khối ($A$) và kí hiệu nguyên tử $^A_Z\\text{X}$",
            "Phát biểu được khái niệm đồng vị và giải thích vì sao nguyên tử khối của nhiều nguyên tố là số thập phân",
            "Tính được nguyên tử khối trung bình của nguyên tố có nhiều đồng vị dựa trên phổ khối lượng (MS)",
        ],
        "Trong tự nhiên, chlorine có $2$ đồng vị bền là $^{35}_{17}\\text{Cl}$ chiếm $75,76\\%$ và $^{37}_{17}\\text{Cl}$ chiếm $24,24\\%$ tổng số nguyên tử. Tính nguyên tử khối trung bình của chlorine.",
        "Áp dụng công thức tính nguyên tử khối trung bình:\\n$\\overline{A}_{\\text{Cl}} = \\frac{35 \\cdot 75,76 + 37 \\cdot 24,24}{100} = 35,4848 \\approx 35,5$.",
        "Đồng vị phóng xạ $^{14}_6\\text{C}$ được dùng trong khảo cổ học để xác định niên đại của các cổ vật có nguồn gốc sinh vật; đồng vị $^{60}_{27}\\text{Co}$ và $^{131}_{53}\\text{I}$ được dùng trong y học để xạ trị ung thư.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Trong nguyên tử $^{27}_{13}\\text{Al}$, số hạt proton ($p$) và số hạt neutron ($n$) lần lượt là:", "$13$ và $14$", ["$13$ và $14$", "$13$ và $27$", "$14$ và $13$", "$27$ và $13$"], "Ta có $Z = 13$ (số proton) và $N = A - Z = 27 - 13 = 14$ (số neutron).", "biet"),
            mcq("Các nguyên tử thuộc cùng một nguyên tố hóa học nhưng là các đồng vị khác nhau thì có cùng đại lượng nào?", "Số proton ($Z$)", ["Số proton ($Z$)", "Số neutron ($N$)", "Số khối ($A$)", "Tổng số hạt trong hạt nhân"], "Đồng vị là những nguyên tử có cùng số proton ($Z$) nhưng khác nhau về số neutron ($N$).", "hieu"),
            short("Trong tự nhiên, đồng ($\\text{Cu}$) có hai đồng vị bền là $^{63}\\text{Cu}$ (chiếm $73\\%$) và $^{65}\\text{Cu}$ (chiếm $27\\%$). Tính nguyên tử khối trung bình của $\\text{Cu}$ (làm tròn đến chữ số thập phân thứ hai).", "63,54", ["63,54", "63.54"], "Ta có $\\overline{A}_{\\text{Cu}} = \\frac{63 \\cdot 73 + 65 \\cdot 27}{100} = 63,54$.", "vandung"),
        ]
    ),
    bai(3, "Cấu trúc lớp vỏ electron nguyên tử",
        "Orbital nguyên tử (AO), lớp và phân lớp electron, nguyên lí Pauli, nguyên lí vững bền, quy tắc Hund và cấu hình electron",
        "Trong mô hình hiện đại, electron chuyển động rất nhanh trong khu vực không gian xung quanh hạt nhân gọi là orbital nguyên tử (AO: AO $s$ hình cầu, AO $p$ hình số tám nổi). Các electron được sắp xếp thành từng lớp ($n = 1, 2, 3, 4...$ ứng với $K, L, M, N...$) và phân lớp ($s, p, d, f$ chứa tối đa lần lượt $2, 6, 10, 14$ electron). Cấu hình electron tuân theo nguyên lí vững bền (thứ tự mức năng lượng: $1s\\,2s\\,2p\\,3s\\,3p\\,4s\\,3d\\,4p...$), nguyên lí Pauli (mỗi AO chứa tối đa $2$ electron có chiều tự quay ngược nhau) và quy tắc Hund. Dựa vào số electron lớp ngoài cùng: $1, 2, 3\\text{ e}$ thường là kim loại; $5, 6, 7\\text{ e}$ thường là phi kim; $8\\text{ e}$ ($2\\text{ e}$ với $\\text{He}$) là khí hiếm.",
        [
            F("Số AO và số electron tối đa trong mỗi phân lớp", "\\text{Phân lớp } s\\text{ (1 AO, tối đa 2e)};\\; p\\text{ (3 AO, tối đa 6e)};\\; d\\text{ (5 AO, tối đa 10e)};\\; f\\text{ (7 AO, tối đa 14e)}", "Lớp thứ n (n <= 4) có n^2 AO và chứa tối đa 2n^2 electron"),
            F("Thứ tự mức năng lượng các phân lớp", "1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s", "Khi viết cấu hình electron của Z > 20, sắp xếp lại theo thứ tự lớp: 1s2 2s2 2p6 3s2 3p6 3d^x 4s^y"),
            F("Số electron lớp ngoài cùng và tính chất", "\\begin{cases} 1, 2, 3\\text{ e ngoài cùng} \\rightarrow \\text{Kim loại (trừ H, He, B)} \\\\ 5, 6, 7\\text{ e ngoài cùng} \\rightarrow \\text{Phi kim} \\\\ 8\\text{ e ngoài cùng (He có 2e)} \\rightarrow \\text{Khí hiếm} \\end{cases}", "Quyết định tính chất hóa học cơ bản của nguyên tố"),
        ],
        [
            "Mô tả được hình dạng orbital nguyên tử ($s, p$) và số lượng electron tối đa trong một AO, một phân lớp, một lớp",
            "Viết được cấu hình electron nguyên tử theo lớp, phân lớp và theo ô orbital cho các nguyên tố có $Z \\le 30$",
            "Dự đoán được tính chất cơ bản (kim loại, phi kim, khí hiếm) dựa vào số electron lớp ngoài cùng",
        ],
        "Viết cấu hình electron đầy đủ của nguyên tử sắt ($\\text{Fe}, Z = 26$) và cho biết số electron lớp ngoài cùng của $\\text{Fe}$.",
        "Thứ tự điền mức năng lượng của $\\text{Fe}$ ($Z = 26$): $1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^6$.\\nSắp xếp lại theo thứ tự lớp, cấu hình electron của $\\text{Fe}$ là: $1s^2 2s^2 2p^6 3s^2 3p^6 3d^6 4s^2$ (hoặc $[\\text{Ar}]3d^6 4s^2$).\\nNguyên tử $\\text{Fe}$ có $2$ electron ở lớp ngoài cùng (lớp thứ $4$), là kim loại.",
        "Các nguyên tố khí hiếm ($\\text{He}, \\text{Ne}, \\text{Ar}$) có lớp vỏ ngoài cùng bão hòa ($2$ hoặc $8$ electron) rất bền vững nên hầu như không tham gia phản ứng hóa học ở điều kiện thường, được bơm vào bóng đèn sợi đốt và đèn quảng cáo.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Phân lớp $p$ chứa tối đa bao nhiêu electron?", "$6$ electron", ["$6$ electron", "$2$ electron", "$10$ electron", "$14$ electron"], "Phân lớp $p$ có $3$ orbital ($p_x, p_y, p_z$), mỗi AO chứa tối đa $2$ electron nên chứa tối đa $6$ electron.", "biet"),
            mcq("Cấu hình electron của nguyên tử nguyên tố $X$ ($Z = 17$) ở trạng thái cơ bản là:", "$1s^2 2s^2 2p^6 3s^2 3p^5$", ["$1s^2 2s^2 2p^6 3s^2 3p^5$", "$1s^2 2s^2 2p^6 3s^2 3p^3$", "$1s^2 2s^2 2p^6 3s^1 3p^6$", "$1s^2 2s^2 2p^6 3s^2 3d^5$"], "Tổng số electron bằng $17$: $2 + 2 + 6 + 2 + 5 = 17$, có $7$ electron lớp ngoài cùng nên $X$ là phi kim (Chlorine).", "hieu"),
            short("Nguyên tử nguyên tố potassium ($\\text{K}$) có số hiệu nguyên tử $Z = 19$ (cấu hình $1s^2 2s^2 2p^6 3s^2 3p^6 4s^1$). Số electron ở lớp ngoài cùng của nguyên tử $\\text{K}$ là bao nhiêu?", "1", ["1"], "Lớp ngoài cùng của $\\text{K}$ là lớp thứ $4$ ($4s^1$) có $1$ electron.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 2: BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC VÀ ĐỊNH LUẬT TUẦN HOÀN
# =========================================================================
CH2_ID = "hoa10_ch2"
CH2_TITLE = "Chương 2: Bảng tuần hoàn các nguyên tố hóa học"
CH2_DESC = "Cấu tạo bảng tuần hoàn, xu hướng biến đổi bán kính nguyên tử, độ âm điện, tính kim loại - phi kim và định luật tuần hoàn"

CH2_LESSONS = [
    bai(4, "Cấu tạo của bảng tuần hoàn các nguyên tố hóa học",
        "Nguyên tắc sắp xếp và mối liên hệ giữa cấu hình electron với vị trí nguyên tố (ô, chu kì, nhóm A, nhóm B)",
        "Bảng tuần hoàn được sắp xếp theo3 nguyên tắc: (1) Theo chiều tăng dần của điện tích hạt nhân nguyên tử; (2) Các nguyên tố có cùng số lớp electron trong nguyên tử được xếp vào một hàng (chu kì); (3) Các nguyên tố có cùng số electron hóa trị trong nguyên tử được xếp vào một cột (nhóm). Bảng tuần hoàn hiện nay có $7$ chu kì ($3$ chu kì nhỏ $1, 2, 3$ và $4$ chu kì lớn $4, 5, 6, 7$) và $18$ cột chia thành $8$ nhóm A (nguyên tố $s, p$) và $8$ nhóm B (nguyên tố $d, f$). Từ cấu hình electron ta xác định ngay được vị trí và ngược lại.",
        [
            F("Mối liên hệ giữa Cấu hình electron và Vị trí (Nhóm A)", "\\begin{cases} \\text{Số thứ tự ô} = Z = N_p = N_e \\\\ \\text{Số thứ tự chu kì} = \\text{Số lớp electron } (n) \\\\ \\text{Số thứ tự nhóm A} = \\text{Số electron lớp ngoài cùng} \\end{cases}", "Áp dụng cho các nguyên tố thuộc khối s và khối p (nhóm IA đến VIIIA)"),
            F("Xác định nhóm B (nguyên tố d: (n-1)d^x ns^y)", "\\text{Tổng } (x + y) = \\begin{cases} 3 \\rightarrow 7: \\text{Nhóm IIIB} \\rightarrow \\text{VIIB} \\\\ 8, 9, 10: \\text{Nhóm VIIIB} \\\\ 11 \\rightarrow \\text{IB};\\quad 12 \\rightarrow \\text{IIB} \\end{cases}", "Chu kì vẫn bằng số thứ tự lớp ngoài cùng n"),
        ],
        [
            "Nêu được $3$ nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn",
            "Mô tả được cấu tạo của bảng tuần hoàn gồm ô nguyên tố, chu kì (nhỏ, lớn) và nhóm (nhóm A, nhóm B)",
            "Từ cấu hình electron suy ra được vị trí của nguyên tố trong bảng tuần hoàn và ngược lại",
        ],
        "Nguyên tử nguyên tố $X$ có số hiệu nguyên tử $Z = 15$. Hãy viết cấu hình electron và xác định vị trí (ô, chu kì, nhóm) của $X$ trong bảng tuần hoàn.",
        "Cấu hình electron của $X$ ($Z = 15$): $1s^2 2s^2 2p^6 3s^2 3p^3$.\\n- $X$ có $Z = 15 \\Rightarrow$ thuộc ô số $15$.\\n- $X$ có $3$ lớp electron $\\Rightarrow$ thuộc chu kì $3$.\\n- $X$ là nguyên tố $p$ có $5$ electron lớp ngoài cùng $\\Rightarrow$ thuộc nhóm $\\text{VA}$ (Phosphorus).",
        "Năm 1869, nhà bác học người Nga D. I. Mendeleev đã công bố bảng tuần hoàn đầu tiên và dự đoán chính xác tính chất của nhiều nguyên tố chưa tìm ra thời đó (như $\\text{Ga}, \\text{Ge}, \\text{Sc}$).",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Trong bảng tuần hoàn, số thứ tự của chu kì luôn bằng:", "Số lớp electron trong nguyên tử", ["Số lớp electron trong nguyên tử", "Số electron lớp ngoài cùng", "Số proton trong hạt nhân", "Số neutron trong hạt nhân"], "Các nguyên tố có cùng số lớp electron được xếp vào cùng một chu kì, số thứ tự chu kì bằng số lớp electron.", "biet"),
            mcq("Nguyên tố magnesium ($\\text{Mg}, Z = 12$) có cấu hình electron $1s^2 2s^2 2p^6 3s^2$. Vị trí của $\\text{Mg}$ trong bảng tuần hoàn là:", "Ô $12$, chu kì $3$, nhóm $\\text{IIA}$", ["Ô $12$, chu kì $3$, nhóm $\\text{IIA}$", "Ô $12$, chu kì $2$, nhóm $\\text{IIIA}$", "Ô $12$, chu kì $3$, nhóm $\\text{IIB}$", "Ô $6$, chu kì $3$, nhóm $\\text{IIA}$"], "$Z = 12$ (ô $12$), $3$ lớp electron (chu kì $3$), nguyên tố $s$ có $2\\text{ e}$ ngoài cùng (nhóm $\\text{IIA}$).", "hieu"),
            short("Nguyên tố $Y$ thuộc chu kì $3$, nhóm $\\text{VIA}$ trong bảng tuần hoàn. Số hiệu nguyên tử $Z$ của nguyên tố $Y$ bằng bao nhiêu?", "16", ["16"], "Chu kì $3$, nhóm $\\text{VIA}$ có cấu hình $1s^2 2s^2 2p^6 3s^2 3p^4 \\Rightarrow Z = 2+2+6+2+4 = 16$ (Lưu huỳnh).", "vandung"),
        ]
    ),
    bai(5, "Xu hướng biến đổi một số tính chất của nguyên tử các nguyên tố trong một chu kì và trong một nhóm",
        "Quy luật biến đổi bán kính nguyên tử (R), độ âm điện (chi), tính kim loại và tính phi kim theo chu kì và nhóm A",
        "Đối với các nguyên tố nhóm A: (1) Trong một chu kì, theo chiều tăng dần của điện tích hạt nhân (từ trái sang phải), số lớp electron không đổi nhưng lực hút của hạt nhân với electron lớp ngoài cùng tăng lên, do đó: bán kính nguyên tử ($R$) giảm dần, độ âm điện ($\\chi$) tăng dần, tính kim loại giảm dần và tính phi kim tăng dần. (2) Trong một nhóm A, theo chiều tăng dần của điện tích hạt nhân (từ trên xuống dưới), số lớp electron tăng lên nhanh làm: bán kính nguyên tử ($R$) tăng dần, độ âm điện ($\\chi$) giảm dần, tính kim loại tăng dần và tính phi kim giảm dần.",
        [
            F("Xu hướng biến đổi trong một Chu kì (Z tăng từ trái sang phải)", "R \\text{ giảm},\\quad \\chi \\text{ tăng},\\quad \\text{Tính kim loại giảm},\\quad \\text{Tính phi kim tăng}", "Kim loại mạnh nhất đầu chu kì (nhóm IA), phi kim mạnh nhất cuối chu kì (nhóm VIIA)"),
            F("Xu hướng biến đổi trong một Nhóm A (Z tăng từ trên xuống dưới)", "R \\text{ tăng},\\quad \\chi \\text{ giảm},\\quad \\text{Tính kim loại tăng},\\quad \\text{Tính phi kim giảm}", "Fluorine (F) ở đầu nhóm VIIA có độ âm điện lớn nhất (chi = 3,98) và tính phi kim mạnh nhất"),
        ],
        [
            "Giải thích được xu hướng biến đổi bán kính nguyên tử trong một chu kì và trong một nhóm A",
            "Trình bày được khái niệm độ âm điện và quy luật biến đổi độ âm điện, tính kim loại, tính phi kim theo chu kì và nhóm A",
            "Vận dụng quy luật biến đổi để sắp xếp thứ tự bán kính nguyên tử, độ âm điện hoặc tính kim loại/phi kim của dãy nguyên tố",
        ],
        "Sắp xếp các nguyên tố sau theo chiều tính kim loại tăng dần: $_{11}\\text{Na}, _{12}\\text{Mg}, _{13}\\text{Al}, _{19}\\text{K}$.",
        "- Ba nguyên tố $_{11}\\text{Na}, _{12}\\text{Mg}, _{13}\\text{Al}$ cùng thuộc chu kì $3$: theo chiều $Z$ tăng, tính kim loại giảm dần nên $\\text{Al} < \\text{Mg} < \\text{Na}$.\\n- Hai nguyên tố $_{11}\\text{Na}$ và $_{19}\\text{K}$ cùng thuộc nhóm $\\text{IA}$: đi từ trên xuống dưới tính kim loại tăng dần nên $\\text{Na} < \\text{K}$.\\nVậy thứ tự tính kim loại tăng dần là: $\\text{Al} < \\text{Mg} < \\text{Na} < \\text{K}$.",
        "Độ âm điện của Fluorine ($\\chi_{\\text{F}} = 3,98$) là lớn nhất trong bảng tuần hoàn nên trong mọi hợp chất, nguyên tử $\\text{F}$ luôn hút electron về phía mình và chỉ có số oxi hóa $-1$.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Trong một chu kì, theo chiều tăng dần của điện tích hạt nhân nguyên tử (trừ khí hiếm), đại lượng nào sau đây GIẢM dần?", "Bán kính nguyên tử", ["Bán kính nguyên tử", "Độ âm điện", "Tính phi kim", "Số electron lớp ngoài cùng"], "Trong một chu kì từ trái sang phải, bán kính nguyên tử và tính kim loại giảm dần, còn độ âm điện và tính phi kim tăng dần.", "biet"),
            mcq("Cho các nguyên tố nhóm $\\text{VIIA}$ (halogen): $_9\\text{F}, _{17}\\text{Cl}, _{35}\\text{Br}, _{53}\\text{I}$. Nguyên tố có tính phi kim mạnh nhất là:", "$_9\\text{F}$", ["$_9\\text{F}$", "$_{17}\\text{Cl}$", "$_{35}\\text{Br}$", "$_{53}\\text{I}$"], "Trong một nhóm A từ trên xuống dưới, tính phi kim giảm dần nên $_9\\text{F}$ đứng đầu nhóm có tính phi kim mạnh nhất.", "hieu"),
            short("Cho $3$ nguyên tố thuộc chu kì $3$: $_{11}\\text{Na}$ (số thứ tự 1), $_{13}\\text{Al}$ (số thứ tự 2), $_{17}\\text{Cl}$ (số thứ tự 3). Nguyên tố có bán kính nguyên tử lớn nhất ứng với số thứ tự nào?", "1", ["1"], "Trong cùng chu kì $3$, bán kính nguyên tử giảm dần theo chiều tăng $Z$, nên $_{11}\\text{Na}$ (số 1) có bán kính lớn nhất.", "vandung"),
        ]
    ),
    bai(6, "Xu hướng biến đổi thành phần và một số tính chất của hợp chất trong một chu kì. Định luật tuần hoàn",
        "Hóa trị cao nhất với oxygen, hóa trị với hydrogen, tính acid - base của oxide và hydroxide cao nhất và Định luật tuần hoàn",
        "Trong một chu kì, từ nhóm $\\text{IA}$ đến $\\text{VIIA}$: hóa trị cao nhất của nguyên tố trong hợp chất với oxygen tăng lần lượt từ $1$ đến $7$ (bằng số thứ tự nhóm $n$), còn hóa trị với hydrogen của các phi kim (từ nhóm $\\text{IVA}$ đến $\\text{VIIA}$) giảm từ $4$ xuống $1$. Theo chiều tăng điện tích hạt nhân trong một chu kì, tính base của các oxide và hydroxide cao nhất giảm dần, đồng thời tính acid của chúng tăng dần (ví dụ ở chu kì $3$: $\\text{NaOH}$ là kiềm mạnh $\\rightarrow \\text{Al(OH)}_3$ lưỡng tính $\\rightarrow \\text{HClO}_4$ là acid rất mạnh). Định luật tuần hoàn: Tính chất của các nguyên tố và đơn chất, cũng như thành phần và tính chất của các hợp chất tạo nên từ các nguyên tố đó biến đổi tuần hoàn theo chiều tăng của điện tích hạt nhân nguyên tử.",
        [
            F("Quan hệ hóa trị của nguyên tố nhóm nA (IVA -> VIIA)", "\\begin{cases} \\text{Công thức oxide cao nhất: } \\text{R}_2\\text{O}_n \\text{ (n chẵn rút gọn)} \\\\ \\text{Công thức hợp chất khí với H: } \\text{RH}_{8-n} \\\\ \\text{Tổng hóa trị: } n + (8 - n) = 8 \\end{cases}", "n là số thứ tự nhóm A (bằng số electron lớp ngoài cùng)"),
            F("Biến đổi tính acid - base trong Chu kì 3", "\\underbrace{\\text{NaOH}}_{\\text{kiềm mạnh}} > \\underbrace{\\text{Mg(OH)}_2}_{\\text{base yếu}} > \\underbrace{\\text{Al(OH)}_3}_{\\text{lưỡng tính}} \\longrightarrow \\underbrace{\\text{H}_2\\text{SiO}_3 < \\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SO}_4 < \\text{HClO}_4}_{\\text{tính acid tăng dần}}", "Trong một chu kì: tính base giảm dần, tính acid tăng dần"),
        ],
        [
            "Xác định được công thức oxide cao nhất, hydroxide tương ứng và hợp chất khí với hydrogen của nguyên tố dựa vào số thứ tự nhóm A",
            "Trình bày được xu hướng biến đổi tính acid, tính base của oxide và hydroxide cao nhất trong một chu kì và một nhóm A",
            "Phát biểu được nội dung và ý nghĩa của Định luật tuần hoàn các nguyên tố hóa học",
        ],
        "Nguyên tố $R$ thuộc nhóm $\\text{VIA}$. Trong hợp chất khí với hydrogen, $R$ chiếm $94,12\\%$ về khối lượng. Tìm nguyên tố $R$ và viết công thức oxide cao nhất của $R$.",
        "$R$ thuộc nhóm $\\text{VIA}$ ($n = 6$) nên công thức hợp chất khí với hydrogen là $\\text{RH}_{8-6} = \\text{RH}_2$.\\nTa có: $\\%m_R = \\frac{M_R}{M_R + 2} \\cdot 100\\% = 94,12\\% \\Rightarrow M_R = 32$ ($\\text{g/mol}$).\\nVậy $R$ là Lưu huỳnh ($\\text{S}$). Công thức oxide cao nhất của $\\text{S}$ là $\\text{SO}_3$.",
        "Nhờ định luật tuần hoàn, các nhà hóa học có thể thiết kế các chất bán dẫn mới từ các nguyên tố nhóm $\\text{IVA}$ ($\\text{Si}, \\text{Ge}$) và các vật liệu xúc tác từ kim loại chuyển tiếp.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Nguyên tố $X$ thuộc nhóm $\\text{VA}$ trong bảng tuần hoàn. Công thức hợp chất khí với hydrogen của $X$ là:", "$\\text{XH}_3$", ["$\\text{XH}_3$", "$\\text{XH}_5$", "$\\text{XH}_2$", "$\\text{XH}_4$"], "Thuộc nhóm $\\text{VA}$ ($n = 5$) nên hóa trị với $\\text{H}$ là $8 - 5 = 3 \\Rightarrow$ công thức là $\\text{XH}_3$.", "biet"),
            mcq("Trong chu kì $3$, dãy các hydroxide được sắp xếp theo chiều tính acid tăng dần là:", "$\\text{H}_2\\text{SiO}_3 < \\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SO}_4 < \\text{HClO}_4$", ["$\\text{H}_2\\text{SiO}_3 < \\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SO}_4 < \\text{HClO}_4$", "$\\text{HClO}_4 < \\text{H}_2\\text{SO}_4 < \\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SiO}_3$", "$\\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SiO}_3 < \\text{H}_2\\text{SO}_4 < \\text{HClO}_4$", "$\\text{H}_2\\text{SO}_4 < \\text{HClO}_4 < \\text{H}_3\\text{PO}_4 < \\text{H}_2\\text{SiO}_3$"], "Theo chiều $Z$ tăng từ $_{14}\\text{Si} \\rightarrow _{15}\\text{P} \\rightarrow _{16}\\text{S} \\rightarrow _{17}\\text{Cl}$, tính acid của hydroxide cao nhất tăng dần.", "hieu"),
            short("Nguyên tố $R$ có công thức hợp chất khí với hydrogen là $\\text{RH}_4$. Trong oxide cao nhất với oxygen, nguyên tố $R$ có hóa trị bằng bao nhiêu?", "4", ["4"], "Vì tổng hóa trị cao nhất với $\\text{O}$ và hóa trị với $\\text{H}$ bằng $8$, nên hóa trị với $\\text{O}$ của $R$ bằng $8 - 4 = 4$ (nhóm $\\text{IVA}$).", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 3: LIÊN KẾT HÓA HỌC
# =========================================================================
CH3_ID = "hoa10_ch3"
CH3_TITLE = "Chương 3: Liên kết hóa học"
CH3_DESC = "Quy tắc octet, liên kết ion, liên kết cộng hóa trị, liên kết hydrogen và tương tác van der Waals"

CH3_LESSONS = [
    bai(7, "Quy tắc octet",
        "Nội dung quy tắc octet (bát tử) và sự hình thành xu hướng nhường, nhận hoặc góp chung electron của nguyên tử",
        "Quy tắc octet (quy tắc bát tử): Trong quá trình hình thành liên kết hóa học, nguyên tử của các nguyên tố nhóm A có xu hướng tạo thành lớp vỏ ngoài cùng có $8$ electron tương ứng với khí hiếm gần nhất (hoặc $2$ electron như khí hiếm helium). Để đạt quy tắc octet: nguyên tử kim loại (có $1, 2, 3\\text{ e}$ ngoài cùng) có xu hướng nhường electron; nguyên tử phi kim (có $5, 6, 7\\text{ e}$ ngoài cùng) có xu hướng nhận thêm electron (khi gặp kim loại) hoặc góp chung electron (khi gặp phi kim khác). Một số phân tử có ngoại lệ không tuân theo quy tắc octet như $\\text{NO}, \\text{BF}_3, \\text{PCl}_5, \\text{SF}_6$.",
        [
            F("Xu hướng của Kim loại (1, 2, 3e ngoài cùng)", "\\text{M} \\rightarrow \\text{M}^{n+} + n\\text{e}\\quad (n = 1, 2, 3)", "Nhường electron lớp ngoài cùng để đạt cấu hình bền của khí hiếm chu kì trước"),
            F("Xu hướng của Phi kim (5, 6, 7e ngoài cùng)", "\\text{X} + m\\text{e} \\rightarrow \\text{X}^{m-}\\quad (m = 8 - \\text{số e ngoài cùng})", "Nhận thêm electron hoặc góp chung m electron để đủ 8e lớp ngoài cùng"),
        ],
        [
            "Trình bày được nội dung quy tắc octet trong sự hình thành liên kết hóa học",
            "Vận dụng được quy tắc octet để giải thích xu hướng nhường, nhận hoặc góp chung electron của các nguyên tử nguyên tố nhóm A",
            "Nhận biết được một số trường hợp phân tử không tuân theo quy tắc octet",
        ],
        "Vận dụng quy tắc octet, hãy giải thích xu hướng của nguyên tử oxygen ($\\text{O}, Z = 8$) và nguyên tử sodium ($\\text{Na}, Z = 11$) khi tham gia liên kết hóa học.",
        "- $\\text{Na}$ ($Z = 11$): cấu hình $1s^2 2s^2 2p^6 3s^1$, có $1\\text{ e}$ lớp ngoài cùng nên có xu hướng nhường $1\\text{ e}$ để đạt cấu hình bền $2s^2 2p^6$ ($8\\text{ e}$) của khí hiếm $\\text{Ne}$.\\n- $\\text{O}$ ($Z = 8$): cấu hình $1s^2 2s^2 2p^4$, có $6\\text{ e}$ lớp ngoài cùng nên có xu hướng nhận $2\\text{ e}$ (hoặc góp chung $2\\text{ e}$) để đạt cấu hình bền $8\\text{ e}$ của $\\text{Ne}$.",
        "Quy tắc octet giải thích vì sao muối ăn có công thức là $\\text{NaCl}$, nước là $\\text{H}_2\\text{O}$ và khí nitrogen là $\\text{N}_2$ chứ không phải một tỉ lệ bất kì nào khác.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Theo quy tắc octet, khi hình thành liên kết hóa học, các nguyên tử có xu hướng đạt tới cấu hình electron bền vững của:", "Nguyên tử khí hiếm ($8$ electron lớp ngoài cùng, hoặc $2$ với $\\text{He}$)", ["Nguyên tử khí hiếm ($8$ electron lớp ngoài cùng, hoặc $2$ với $\\text{He}$)", "Kim loại kiềm ($1$ electron lớp ngoài cùng)", "Halogen ($7$ electron lớp ngoài cùng)", "Nguyên tử carbon ($4$ electron lớp ngoài cùng)"], "Cấu hình $8$ electron lớp ngoài cùng ($ns^2 np^6$) của khí hiếm là cấu hình rất bền vững.", "biet"),
            mcq("Nguyên tử nhôm ($\\text{Al}, Z = 13$) có cấu hình electron $1s^2 2s^2 2p^6 3s^2 3p^1$. Để đạt quy tắc octet, nguyên tử $\\text{Al}$ có xu hướng:", "Nhường đi $3$ electron lớp ngoài cùng", ["Nhường đi $3$ electron lớp ngoài cùng", "Nhận thêm $5$ electron", "Nhường đi $1$ electron", "Nhận thêm $3$ electron"], "$\\text{Al}$ có $3$ electron lớp ngoài cùng nên nhường $3$ electron để đạt cấu hình bền $1s^2 2s^2 2p^6$ của $\\text{Ne}$.", "hieu"),
            short("Nguyên tử nitrogen ($\\text{N}, Z = 7$) có $5$ electron lớp ngoài cùng. Khi hình thành phân tử $\\text{N}_2$, mỗi nguyên tử $\\text{N}$ cần góp chung bao nhiêu electron để đạt quy tắc octet?", "3", ["3"], "Vì có $5$ electron ngoài cùng nên mỗi nguyên tử $\\text{N}$ cần góp chung $8 - 5 = 3$ electron.", "vandung"),
        ]
    ),
    bai(8, "Liên kết ion",
        "Sự tạo thành cation, anion, bản chất lực hút tĩnh điện của liên kết ion và tính chất của hợp chất ion",
        "Khi nguyên tử nhường hay nhận electron sẽ trở thành phần tử mang điện gọi là ion: nguyên tử kim loại nhường electron tạo ion dương (cation $\\text{M}^{n+}$), nguyên tử phi kim nhận electron tạo ion âm (anion $\\text{X}^{m-}$). Liên kết ion là liên kết được hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu, thường được tạo thành giữa kim loại điển hình và phi kim điển hình (hiệu độ âm điện $\\Delta \\chi \\ge 1,7$). Các hợp chất ion (như $\\text{NaCl}, \\text{MgO}, \\text{CaCl}_2$) tồn tại ở dạng tinh thể ion, là chất rắn ở điều kiện thường, có nhiệt độ nóng chảy và nhiệt độ sôi cao, thường tan tốt trong nước và dẫn điện khi tan trong nước hoặc khi nóng chảy.",
        [
            F("Sự tạo thành Cation và Anion", "\\text{M} \\rightarrow \\text{M}^{n+} + n\\text{e};\\quad \\text{X} + m\\text{e} \\rightarrow \\text{X}^{m-}", "Số electron trong cation M^(n+) = Z - n; số electron trong anion X^(m-) = Z + m"),
            F("Sự tạo thành phân tử NaCl", "\\text{Na} + \\text{Cl} \\rightarrow \\text{Na}^+ + \\text{Cl}^- \\rightarrow \\text{NaCl}", "Lực hút tĩnh điện giữa Na+ và Cl- tạo nên liên kết ion"),
            F("Điều kiện dự đoán Liên kết ion theo hiệu độ âm điện", "\\Delta \\chi = |\\chi_A - \\chi_B| \\ge 1,7 \\implies \\text{Liên kết ion}", "Quy tắc tương đối (trừ một số trường hợp như HF có Delta chi = 1,78 nhưng là cộng hóa trị)"),
        ],
        [
            "Trình bày được sự hình thành ion dương (cation), ion âm (anion) và viết được cấu hình electron của các ion đơn nguyên tử",
            "Nêu được bản chất của liên kết ion và viết được sơ đồ hình thành liên kết ion trong các hợp chất như $\\text{NaCl}, \\text{MgO}, \\text{CaF}_2$",
            "Giải thích được vì sao hợp chất ion thường là chất rắn, có nhiệt độ nóng chảy cao và dẫn điện khi nóng chảy hoặc hòa tan trong nước",
        ],
        "Nguyên tử calcium ($\\text{Ca}, Z = 20$) tác dụng với nguyên tử chlorine ($\\text{Cl}, Z = 17$) tạo thành hợp chất $\\text{CaCl}_2$. Viết quá trình tạo thành các ion và phương trình hình thành $\\text{CaCl}_2$.",
        "- $\\text{Ca}$ ($Z = 20$) nhường $2\\text{ e}$: $\\text{Ca} \\rightarrow \\text{Ca}^{2+} + 2\\text{e}$.\\n- Mỗi nguyên tử $\\text{Cl}$ ($Z = 17$) nhận $1\\text{ e}$: $2\\text{Cl} + 2\\text{e} \\rightarrow 2\\text{Cl}^-$.\\n- Các ion trái dấu hút nhau bằng lực hút tĩnh điện: $\\text{Ca}^{2+} + 2\\text{Cl}^- \\rightarrow \\text{CaCl}_2$.",
        "Muối ăn ($\\text{NaCl}$) ở trạng thái rắn các ion $\\text{Na}^+$ và $\\text{Cl}^-$ bị giữ chặt ở các nút mạng tinh thể nên không dẫn điện, nhưng khi hòa tan vào nước các ion di chuyển tự do nên dung dịch nước muối dẫn điện tốt.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Bản chất của liên kết ion là:", "Lực hút tĩnh điện giữa các ion mang điện tích trái dấu", ["Lực hút tĩnh điện giữa các ion mang điện tích trái dấu", "Sự dùng chung các cặp electron giữa hai nguyên tử", "Lực hút giữa các electron tự do với ion dương kim loại", "Lực tương tác yếu giữa các phân tử trung hòa"], "Liên kết ion được hình thành bởi lực hút tĩnh điện giữa cation và anion.", "biet"),
            mcq("Ion $\\text{Mg}^{2+}$ được tạo thành từ nguyên tử $\\text{Mg}$ ($Z = 12$) có cấu hình electron là:", "$1s^2 2s^2 2p^6$", ["$1s^2 2s^2 2p^6$", "$1s^2 2s^2 2p^6 3s^2$", "$1s^2 2s^2 2p^6 3s^2 3p^2$", "$1s^2 2s^2 2p^4$"], "Nguyên tử $\\text{Mg}$ ($1s^2 2s^2 2p^6 3s^2$) nhường đi $2$ electron ở phân lớp $3s^2$ tạo ion $\\text{Mg}^{2+}$ có cấu hình $1s^2 2s^2 2p^6$.", "hieu"),
            short("Trong ion oxide $\\text{O}^{2-}$ (cho nguyên tử $\\text{O}$ có $Z = 8$) có tổng cộng bao nhiêu hạt electron?", "10", ["10"], "Nguyên tử $\\text{O}$ có $8$ electron nhận thêm $2$ electron tạo ion $\\text{O}^{2-}$ có $8 + 2 = 10$ electron.", "vandung"),
        ]
    ),
    bai(9, "Liên kết cộng hóa trị",
        "Sự hình thành liên kết cộng hóa trị không phân cực, phân cực, liên kết cho - nhận và liên kết sigma, pi",
        "Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng một hay nhiều cặp electron dùng chung (thường giữa các nguyên tử phi kim với nhau). Nếu cặp electron dùng chung không lệch về phía nguyên tử nào ($0 \\le \\Delta \\chi < 0,4$) thì đó là liên kết cộng hóa trị không phân cực (như $\\text{H}_2, \\text{Cl}_2, \\text{N}_2$); nếu cặp electron dùng chung bị lệch về phía nguyên tử có độ âm điện lớn hơn ($0,4 \\le \\Delta \\chi < 1,7$) thì đó là liên kết cộng hóa trị phân cực (như $\\text{HCl}, \\text{H}_2\\text{O}, \\text{NH}_3$). Nếu cặp electron dùng chung chỉ do một nguyên tử đóng góp thì gọi là liên kết cho - nhận. Theo sự xen phủ orbital: xen phủ trục tạo liên kết $\\sigma$ bền vững, xen phủ bên tạo liên kết $\\pi$ kém bền hơn.",
        [
            F("Phân loại liên kết theo hiệu độ âm điện (Delta chi)", "\\begin{cases} 0 \\le \\Delta \\chi < 0,4 \\rightarrow \\text{Cộng hóa trị không phân cực} \\\\ 0,4 \\le \\Delta \\chi < 1,7 \\rightarrow \\text{Cộng hóa trị phân cực} \\\\ \\Delta \\chi \\ge 1,7 \\rightarrow \\text{Liên kết ion} \\end{cases}", "Quy ước tương đối dựa vào thang độ âm điện Pauling"),
            F("Số liên kết sigma và pi trong liên kết đơn, đôi, ba", "\\begin{cases} \\text{Liên kết đơn } (-): 1\\sigma \\\\ \\text{Liên kết đôi } (=): 1\\sigma + 1\\pi \\\\ \\text{Liên kết ba } (\\equiv): 1\\sigma + 2\\pi \\end{cases}", "Liên kết sigma (xen phủ trục) bền hơn liên kết pi (xen phủ bên)"),
        ],
        [
            "Trình bày được khái niệm liên kết cộng hóa trị (không phân cực, phân cực, cho - nhận) và viết được công thức Lewis của các phân tử đơn giản",
            "Vận dụng được hiệu độ âm điện $\\Delta \\chi$ để dự đoán loại liên kết hóa học trong phân tử",
            "Phân biệt được liên kết $\\sigma$ (xen phủ trục) và liên kết $\\pi$ (xen phủ bên), xác định được số liên kết $\\sigma, \\pi$ trong phân tử",
        ],
        "Cho độ âm điện của $\\text{H} = 2,20$; $\\text{Cl} = 3,16$; $\\text{Na} = 0,93$. Hãy xác định loại liên kết hóa học trong các phân tử $\\text{Cl}_2, \\text{HCl}, \\text{NaCl}$.",
        "- Trong $\\text{Cl}_2$: $\\Delta \\chi = 3,16 - 3,16 = 0 < 0,4 \\Rightarrow$ Liên kết cộng hóa trị không phân cực.\\n- Trong $\\text{HCl}$: $\\Delta \\chi = 3,16 - 2,20 = 0,96$ ($0,4 \\le 0,96 < 1,7$) $\\Rightarrow$ Liên kết cộng hóa trị phân cực.\\n- Trong $\\text{NaCl}$: $\\Delta \\chi = 3,16 - 0,93 = 2,23 \\ge 1,7 \\Rightarrow$ Liên kết ion.",
        "Phân tử nitrogen ($\\text{N}\\equiv\\text{N}$) có liên kết ba rất bền vững ($E_b = 945\\text{ kJ/mol}$ gồm $1\\sigma + 2\\pi$) nên khí $\\text{N}_2$ rất trơ ở nhiệt độ thường, được dùng bơm vào túi thực phẩm để bảo quản chống oxi hóa.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Trong phân tử nào sau đây chứa liên kết cộng hóa trị KHÔNG phân cực?", "$\\text{N}_2$", ["$\\text{N}_2$", "$\\text{HCl}$", "$\\text{H}_2\\text{O}$", "$\\text{NaCl}$"], "Trong $\\text{N}_2$ hai nguyên tử giống hệt nhau nên $\\Delta \\chi = 0$, cặp electron dùng chung không bị lệch về phía nào.", "biet"),
            mcq("Một liên kết đôi (ví dụ $\\text{C}=\\text{C}$ hoặc $\\text{C}=\\text{O}$) được tạo thành từ:", "$1$ liên kết $\\sigma$ và $1$ liên kết $\\pi$", ["$1$ liên kết $\\sigma$ và $1$ liên kết $\\pi$", "$2$ liên kết $\\sigma$", "$2$ liên kết $\\pi$", "$1$ liên kết $\\sigma$ và $2$ liên kết $\\pi$"], "Mọi liên kết bội luôn có $1$ liên kết $\\sigma$ bền và các liên kết còn lại là liên kết $\\pi$.", "hieu"),
            short("Trong phân tử ethylene ($\\text{CH}_2=\\text{CH}_2$) có tổng cộng bao nhiêu liên kết $\\sigma$ (sigma)?", "5", ["5"], "Trong $\\text{CH}_2=\\text{CH}_2$ có $4$ liên kết đơn $\\text{C}-\\text{H}$ ($4\\sigma$) và $1$ liên kết đôi $\\text{C}=\\text{C}$ ($1\\sigma + 1\\pi$), tổng cộng có $4 + 1 = 5$ liên kết $\\sigma$.", "vandung"),
        ]
    ),
    bai(10, "Liên kết hydrogen và tương tác van der Waals",
        "Bản chất, điều kiện hình thành liên kết hydrogen, tương tác van der Waals và ảnh hưởng đến nhiệt độ sôi, độ tan",
        "Liên kết hydrogen là một loại liên kết yếu được hình thành giữa nguyên tử $\\text{H}$ (đã liên kết với một nguyên tử có độ âm điện lớn như $\\text{F}, \\text{O}, \\text{N}$) với một nguyên tử khác có độ âm điện lớn ($\\text{F}, \\text{O}, \\text{N}$) còn cặp electron hóa trị chưa tham gia liên kết, kí hiệu bằng dấu ba chấm ($\\cdots$). Liên kết hydrogen làm tăng nhiệt độ nóng chảy, nhiệt độ sôi và làm tăng độ tan trong nước của chất (ví dụ $\\text{H}_2\\text{O}$ sôi ở $100^\\circ\\text{C}$ cao hơn hẳn $\\text{H}_2\\text{S}$, $\\text{C}_2\\text{H}_5\\text{OH}$ sôi cao hơn $\\text{CH}_3\\text{OCH}_3$). Tương tác van der Waals là lực tương tác tĩnh điện rất yếu giữa các phân tử do sự xuất hiện các lưỡng cực tạm thời và lưỡng cực cảm ứng; khối lượng phân tử và kích thước phân tử càng lớn thì tương tác van der Waals càng mạnh, làm nhiệt độ sôi tăng.",
        [
            F("Biểu diễn Liên kết hydrogen giữa các phân tử nước", "\\cdots\\text{O}^{\\delta-}-\\text{H}^{\\delta+} \\cdots \\text{O}^{\\delta-}-\\text{H}^{\\delta+}\\cdots", "Nguyên tử H linh động liên kết với F, O hoặc N còn cặp electron tự do"),
            F("Ảnh hưởng của Liên kết hydrogen đến nhiệt độ sôi", "t_s(\\text{C}_2\\text{H}_5\\text{OH}) = 78,3^\\circ\\text{C} > t_s(\\text{CH}_3\\text{OCH}_3) = -24^\\circ\\text{C}", "Rượu có liên kết hydrogen liên phân tử nên nhiệt độ sôi cao hơn hẳn ether có cùng M"),
            F("Ảnh hưởng của Tương tác van der Waals (dãy Halogen / Khí hiếm)", "t_s(\\text{F}_2) < t_s(\\text{Cl}_2) < t_s(\\text{Br}_2) < t_s(\\text{I}_2)", "Phân tử khối và số electron càng tăng -> tương tác van der Waals càng mạnh -> nhiệt độ sôi càng tăng"),
        ],
        [
            "Trình bày được khái niệm, điều kiện hình thành liên kết hydrogen và biểu diễn được liên kết hydrogen giữa các phân tử $\\text{H}_2\\text{O}, \\text{NH}_3, \\text{C}_2\\text{H}_5\\text{OH}$",
            "Trình bày được khái niệm tương tác van der Waals và sự phụ thuộc của nó vào kích thước, số electron trong phân tử",
            "Giải thích được sự khác biệt về nhiệt độ sôi và độ tan trong nước của các chất dựa vào liên kết hydrogen và tương tác van der Waals",
        ],
        "Giải thích vì sao ở điều kiện thường, $\\text{H}_2\\text{O}$ ($M = 18$) là chất lỏng sôi ở $100^\\circ\\text{C}$, trong khi $\\text{H}_2\\text{S}$ ($M = 34$, phân tử khối lớn hơn) lại là chất khí sôi ở $-60,7^\\circ\\text{C}$.",
        "Nguyên tử $\\text{O}$ có độ âm điện lớn ($3,44$) và bán kính nhỏ nên giữa các phân tử $\\text{H}_2\\text{O}$ tạo được liên kết hydrogen liên phân tử bền vững, cần nhiều năng lượng để phá vỡ nên $\\text{H}_2\\text{O}$ có nhiệt độ sôi cao ($100^\\circ\\text{C}$). Còn $\\text{S}$ có độ âm điện nhỏ hơn ($2,58$) và bán kính lớn nên giữa các phân tử $\\text{H}_2\\text{S}$ không có liên kết hydrogen.",
        "Nhờ cấu trúc mạng tinh thể nước đá có nhiều khoảng trống do các liên kết hydrogen định hướng tạo nên, nước đá có khối lượng riêng nhỏ hơn nước lỏng nên nổi trên mặt nước, giúp sinh vật dưới đáy hồ sống sót qua mùa đông giá lạnh.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Chất nào sau đây có khả năng tạo liên kết hydrogen giữa các phân tử cùng loại?", "$\\text{C}_2\\text{H}_5\\text{OH}$", ["$\\text{C}_2\\text{H}_5\\text{OH}$", "$\\text{CH}_4$", "$\\text{CH}_3-\\text{O}-\\text{CH}_3$", "$\\text{CO}_2$"], "$\\text{C}_2\\text{H}_5\\text{OH}$ có nguyên tử $\\text{H}$ liên kết trực tiếp với nguyên tử $\\text{O}$ (nhóm $-\\text{OH}$) nên tạo được liên kết hydrogen liên phân tử.", "biet"),
            mcq("Theo chiều từ $\\text{He} \\rightarrow \\text{Ne} \\rightarrow \\text{Ar} \\rightarrow \\text{Kr} \\rightarrow \\text{Xe}$, nhiệt độ sôi của các khí hiếm tăng dần là do:", "Tương tác van der Waals giữa các phân tử tăng dần khi kích thước và số electron tăng", ["Tương tác van der Waals giữa các phân tử tăng dần khi kích thước và số electron tăng", "Độ bền liên kết hydrogen tăng dần", "Độ bền liên kết ion tăng dần", "Liên kết cộng hóa trị giữa các nguyên tử mạnh dần"], "Các nguyên tử khí hiếm chỉ tương tác với nhau bằng lực van der Waals, tăng dần theo kích thước và số electron.", "hieu"),
            short("Mỗi phân tử nước ($\\text{H}_2\\text{O}$) ở trạng thái tinh thể nước đá có thể tạo tối đa bao nhiêu liên kết hydrogen với các phân tử $\\text{H}_2\\text{O}$ lân cận?", "4", ["4"], "Mỗi phân tử $\\text{H}_2\\text{O}$ có $2$ nguyên tử $\\text{H}^{\\delta+}$ và $2$ cặp electron tự do trên nguyên tử $\\text{O}^{\\delta-}$, nên tạo tối đa $4$ liên kết hydrogen theo hình tứ diện.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 4: PHẢN ỨNG OXI HÓA - KHỬ
# =========================================================================
CH4_ID = "hoa10_ch4"
CH4_TITLE = "Chương 4: Phản ứng oxi hóa - khử"
CH4_DESC = "Số oxi hóa, chất khử, chất oxi hóa, lập phương trình hóa học của phản ứng oxi hóa - khử và ý nghĩa thực tiễn"

CH4_LESSONS = [
    bai(11, "Số oxi hóa và khái niệm phản ứng oxi hóa - khử",
        "Quy tắc xác định số oxi hóa của nguyên tố, định nghĩa chất khử, chất oxi hóa, quá trình oxi hóa và quá trình khử",
        "Số oxi hóa là điện tích quy ước của nguyên tử trong phân tử khi giả định tất cả các liên kết đều là liên kết ion. Quy tắc xác định số oxi hóa: (1) Trong đơn chất, số oxi hóa của nguyên tử bằng $0$; (2) Trong phân tử, tổng số oxi hóa của các nguyên tử bằng $0$ (trong ion bằng điện tích của ion); (3) Trong hầu hết hợp chất: $\\text{H}$ có số oxi hóa $+1$, $\\text{O}$ có số oxi hóa $-2$, kim loại nhóm $\\text{IA}, \\text{IIA}, \\text{Al}$ có số oxi hóa $+1, +2, +3$, $\\text{F}$ luôn bằng $-1$. Phản ứng oxi hóa - khử là phản ứng hóa học có sự chuyển dịch electron giữa các chất phản ứng (có sự thay đổi số oxi hóa): Chất khử là chất nhường electron (số oxi hóa tăng), chất oxi hóa là chất nhận electron (số oxi hóa giảm).",
        [
            F("Quy tắc tổng số oxi hóa", "\\sum n_i \\cdot (\\text{Số oxi hóa})_i = \\begin{cases} 0 & \\text{(trong phân tử trung hòa)} \\\\ q & \\text{(trong ion mang điện tích } q\\text{)} \\end{cases}", "Với H = +1, O = -2, Kim loại kiềm = +1, Kiềm thổ = +2, Al = +3"),
            F("Khái niệm Chất khử và Chất oxi hóa", "\\begin{cases} \\text{Chất khử (bị oxi hóa): nhường e (số oxi hóa tăng)} \\\\ \\text{Chất oxi hóa (bị khử): nhận e (số oxi hóa giảm)} \\end{cases}", "Mẹo nhớ: Khử cho (nhường e) - O nhận (nhận e); Quá trình oxi hóa là quá trình nhường e"),
        ],
        [
            "Nêu được khái niệm và vận dụng được $4$ quy tắc xác định số oxi hóa của nguyên tử các nguyên tố trong đơn chất, hợp chất và ion",
            "Phát biểu được định nghĩa phản ứng oxi hóa - khử, chất khử, chất oxi hóa, quá trình oxi hóa (sự oxi hóa) và quá trình khử (sự khử)",
            "Nhận diện được phản ứng oxi hóa - khử dựa vào dấu hiệu thay đổi số oxi hóa của nguyên tố",
        ],
        "Xác định số oxi hóa của nguyên tố nitrogen ($\\text{N}$) trong các phân tử và ion sau: $\\text{NH}_3, \\text{N}_2, \\text{NO}_2, \\text{HNO}_3, \\text{NH}_4^+$.",
        "Đặt số oxi hóa của $\\text{N}$ là $x$ (biết $\\text{H}$ là $+1$, $\\text{O}$ là $-2$):\\n- $\\text{NH}_3$: $x + 3(+1) = 0 \\Rightarrow x = -3$.\\n- $\\text{N}_2$ (đơn chất): $x = 0$.\\n- $\\text{NO}_2$: $x + 2(-2) = 0 \\Rightarrow x = +4$.\\n- $\\text{HNO}_3$: $(+1) + x + 3(-2) = 0 \\Rightarrow x = +5$.\\n- $\\text{NH}_4^+$: $x + 4(+1) = +1 \\Rightarrow x = -3$.",
        "Quá trình hô hấp tế bào, sự cháy của nhiên liệu, sự gỉ sét của kim loại và sự phóng điện của pin/ắc quy đều là các phản ứng oxi hóa - khử diễn ra hàng ngày.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Số oxi hóa của nguyên tố manganese ($\\text{Mn}$) trong hợp chất $\\text{KMnO}_4$ là:", "$+7$", ["$+7$", "$+6$", "$+4$", "$+2$"], "Biết $\\text{K}$ là $+1$, $\\text{O}$ là $-2$, ta có $(+1) + x + 4(-2) = 0 \\Rightarrow x = +7$.", "biet"),
            mcq("Trong phản ứng: $\\text{Zn} + \\text{CuSO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{Cu}$, vai trò của $\\text{Zn}$ là:", "Chất khử (bị oxi hóa)", ["Chất khử (bị oxi hóa)", "Chất oxi hóa (bị khử)", "Vừa là chất oxi hóa vừa là chất khử", "Môi trường phản ứng"], "Số oxi hóa của $\\text{Zn}$ tăng từ $0$ lên $+2$ ($\\text{Zn} \\rightarrow \\text{Zn}^{2+} + 2\\text{e}$), nên $\\text{Zn}$ là chất khử.", "hieu"),
            short("Số oxi hóa của nguyên tố lưu huỳnh ($\\text{S}$) trong phân tử $\\text{H}_2\\text{SO}_4$ là dương mấy?", "6", ["6", "+6"], "Ta có $2(+1) + x + 4(-2) = 0 \\Rightarrow x = +6$.", "vandung"),
        ]
    ),
    bai(12, "Lập phương trình hóa học của phản ứng oxi hóa - khử và ý nghĩa thực tiễn",
        "Phương pháp thăng bằng electron (4 bước) để cân bằng phương trình oxi hóa - khử và tính toán theo bảo toàn electron",
        "Nguyên tắc lập phương trình hóa học của phản ứng oxi hóa - khử theo phương pháp thăng bằng electron là: Tổng số electron do chất khử nhường phải bằng tổng số electron mà chất oxi hóa nhận ($\\sum n_{\\text{e nhường}} = \\sum n_{\\text{e nhận}}$). Quy trình gồm $4$ bước: Bước 1: Xác định các nguyên tử có sự thay đổi số oxi hóa, chỉ rõ chất khử, chất oxi hóa; Bước 2: Viết các quá trình oxi hóa và quá trình khử; Bước 3: Tìm hệ số thích hợp cho chất khử và chất oxi hóa sao cho tổng số electron nhường bằng tổng số electron nhận; Bước 4: Đặt hệ số của các chất oxi hóa và chất khử vào sơ đồ phản ứng, từ đó kiểm tra và hoàn thành hệ số các chất còn lại.",
        [
            F("Định luật Bảo toàn electron", "\\sum n_{\\text{e nhường (Chất khử)}} = \\sum n_{\\text{e nhận (Chất oxi hóa)}}", "Cơ sở để cân bằng phương trình oxi hóa - khử và giải nhanh bài tập hóa học"),
            F("Ví dụ cân bằng Cu tác dụng với HNO3 loãng", "3\\text{Cu} + 8\\text{HNO}_3 \\rightarrow 3\\text{Cu(NO}_3)_2 + 2\\text{NO}\\uparrow + 4\\text{H}_2\\text{O}", "Cu nhường 2e (nhân 3); N(+5) nhận 3e thành N(+2) (nhân 2)"),
        ],
        [
            "Trình bày được nguyên tắc và $4$ bước lập phương trình hóa học của phản ứng oxi hóa - khử theo phương pháp thăng bằng electron",
            "Cân bằng được các phương trình phản ứng oxi hóa - khử thông dụng và xác định được tỉ lệ mol giữa chất khử với chất oxi hóa",
            "Vận dụng định luật bảo toàn electron để giải bài toán tính khối lượng kim loại hoặc thể tích khí sản phẩm khử",
        ],
        "Hòa tan hoàn toàn $9,6\\text{ g}$ đồng ($\\text{Cu} = 64$) trong dung dịch $\\text{HNO}_3$ loãng dư, thu được khí $\\text{NO}$ là sản phẩm khử duy nhất. Tính thể tích khí $\\text{NO}$ thu được ở đkc.",
        "Số mol $\\text{Cu}$: $n_{\\text{Cu}} = \\frac{9,6}{64} = 0,15\\text{ mol}$.\\nQuá trình nhường - nhận electron:\\n- $\\text{Cu}^0 \\rightarrow \\text{Cu}^{+2} + 2\\text{e}$\\n- $\\text{N}^{+5} + 3\\text{e} \\rightarrow \\text{N}^{+2}$ (trong $\\text{NO}$)\\nBảo toàn electron: $2n_{\\text{Cu}} = 3n_{\\text{NO}} \\Rightarrow n_{\\text{NO}} = \\frac{2 \\cdot 0,15}{3} = 0,1\\text{ mol}$.\\nThể tích khí $\\text{NO}$ (đkc): $V_{\\text{NO}} = 0,1 \\cdot 24,79 = 2,479\\text{ L}$.",
        "Máy đo nồng độ cồn của cảnh sát giao thông dựa trên phản ứng oxi hóa - khử giữa hơi ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$) trong hơi thở với $\\text{K}_2\\text{Cr}_2\\text{O}_7$ (màu da cam chuyển sang $\\text{Cr}^{3+}$ màu xanh lục).",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Nguyên tắc của phương pháp thăng bằng electron khi cân bằng phản ứng oxi hóa - khử là:", "Tổng số electron do chất khử nhường bằng tổng số electron mà chất oxi hóa nhận", ["Tổng số electron do chất khử nhường bằng tổng số electron mà chất oxi hóa nhận", "Tổng số nguyên tử trước phản ứng lớn hơn sau phản ứng", "Tổng số phân tử các chất tham gia bằng tổng số phân tử sản phẩm", "Số oxi hóa của mọi nguyên tố phải bằng $0$"], "Định luật bảo toàn electron: $\\sum n_{\\text{e nhường}} = \\sum n_{\\text{e nhận}}$.", "biet"),
            mcq("Cho phương trình hóa học (đã cân bằng hệ số tối giản): $a\\text{Al} + b\\text{HNO}_3 \\rightarrow c\\text{Al(NO}_3)_3 + d\\text{NO} + e\\text{H}_2\\text{O}$. Tỉ lệ hệ số $a : c$ và $a : d$ lần lượt là:", "$a : c = 1 : 1$ và $a : d = 1 : 1$", ["$a : c = 1 : 1$ và $a : d = 1 : 1$", "$a : c = 1 : 3$ và $a : d = 3 : 1$", "$a : c = 2 : 1$ và $a : d = 1 : 2$", "$a : c = 3 : 2$ và $a : d = 3 : 2$"], "Vì $\\text{Al}$ nhường $3\\text{e}$ và $\\text{N}^{+5}$ nhận $3\\text{e}$ tạo $\\text{N}^{+2}$ ($\\text{NO}$), nên hệ số cân bằng là $\\text{Al} + 4\\text{HNO}_3 \\rightarrow \\text{Al(NO}_3)_3 + \\text{NO} + 2\\text{H}_2\\text{O}$ ($a=1, d=1$).", "hieu"),
            short("Hòa tan hoàn toàn $0,1\\text{ mol}$ sắt ($\\text{Fe}$) vào dung dịch $\\text{H}_2\\text{SO}_4$ đặc, nóng dư thu được muối $\\text{Fe}_2(\\text{SO}_4)_3$, nước và bao nhiêu mol khí $\\text{SO}_2$ (sản phẩm khử duy nhất)?", "0,15", ["0,15", "0.15"], "Bảo toàn electron: $\\text{Fe}$ nhường $3\\text{e}$, $\\text{S}^{+6}$ nhận $2\\text{e}$ tạo $\\text{SO}_2 \\Rightarrow 3n_{\\text{Fe}} = 2n_{\\text{SO}_2} \\Rightarrow n_{\\text{SO}_2} = \\frac{3 \\cdot 0,1}{2} = 0,15\\text{ mol}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 5: NĂNG LƯỢNG HÓA HỌC
# =========================================================================
CH5_ID = "hoa10_ch5"
CH5_TITLE = "Chương 5: Năng lượng hóa học"
CH5_DESC = "Phản ứng tỏa nhiệt, phản ứng thu nhiệt, enthalpy tạo thành chuẩn và tính biến thiên enthalpy chuẩn của phản ứng"

CH5_LESSONS = [
    bai(13, "Enthalpy tạo thành và biến thiên enthalpy của phản ứng hóa học",
        "Phản ứng tỏa nhiệt (Delta_r H < 0), phản ứng thu nhiệt (Delta_r H > 0), điều kiện chuẩn và enthalpy tạo thành chuẩn (Delta_f H298)",
        "Biến thiên enthalpy của phản ứng ($\\Delta_r H$) là nhiệt lượng tỏa ra hay thu vào của một phản ứng hóa học ở áp suất không đổi. Điều kiện chuẩn đối với phản ứng nhiệt hóa học là áp suất $1\\text{ bar}$ (với chất khí), nồng độ $1\\text{ mol/L}$ (với chất tan trong dung dịch) và nhiệt độ thường chọn là $25^\\circ\\text{C}$ ($298\\text{ K}$), kí hiệu là $\\Delta_r H^\\circ_{298}$. Nếu $\\Delta_r H^\\circ_{298} < 0$: phản ứng tỏa nhiệt (năng lượng của hệ chất phản ứng lớn hơn hệ sản phẩm, làm nóng môi trường xung quanh); nếu $\\Delta_r H^\\circ_{298} > 0$: phản ứng thu nhiệt (làm lạnh môi trường xung quanh). Enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$) là biến thiên enthalpy của phản ứng tạo thành $1\\text{ mol}$ chất đó từ các đơn chất ở dạng bền vững nhất ở điều kiện chuẩn; với đơn chất bền nhất thì $\\Delta_f H^\\circ_{298} = 0$.",
        [
            F("Dấu của Biến thiên Enthalpy chuẩn", "\\begin{cases} \\Delta_r H^\\circ_{298} < 0 \\implies \\text{Phản ứng tỏa nhiệt} \\\\ \\Delta_r H^\\circ_{298} > 0 \\implies \\text{Phản ứng thu nhiệt} \\end{cases}", "Đơn vị thường dùng là kJ hoặc kJ/mol"),
            F("Enthalpy tạo thành chuẩn của đơn chất bền", "\\Delta_f H^\\circ_{298}(\\text{Đơn chất bền nhất ở } 25^\\circ\\text{C}, 1\\text{ bar}) = 0\\text{ kJ/mol}", "Ví dụ: O2(g), H2(g), N2(g), C(graphite), Fe(s) có Delta_f H298 = 0"),
        ],
        [
            "Phân biệt được phản ứng tỏa nhiệt ($\\Delta_r H < 0$) và phản ứng thu nhiệt ($\\Delta_r H > 0$) qua dấu của biến thiên enthalpy và hiện tượng thực tế",
            "Nêu được các thông số của điều kiện chuẩn trong nhiệt hóa học ($1\\text{ bar}, 1\\text{ M}, 298\\text{ K}$) và khái niệm enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$)",
            "Đọc và giải thích được ý nghĩa của phương trình nhiệt hóa học",
        ],
        "Cho phương trình nhiệt hóa học: $\\text{CH}_4(g) + 2\\text{O}_2(g) \\xrightarrow{t^\\circ} \\text{CO}_2(g) + 2\\text{H}_2\\text{O}(l)$ có $\\Delta_r H^\\circ_{298} = -890,3\\text{ kJ}$. Cho biết đây là phản ứng tỏa nhiệt hay thu nhiệt, và tính nhiệt lượng tỏa ra khi đốt cháy hoàn toàn $3,2\\text{ g}$ $\\text{CH}_4$ ở điều kiện chuẩn.",
        "- Vì $\\Delta_r H^\\circ_{298} = -890,3\\text{ kJ} < 0$ nên đây là phản ứng tỏa nhiệt.\\n- Số mol $\\text{CH}_4$: $n_{\\text{CH}_4} = \\frac{3,2}{16} = 0,2\\text{ mol}$.\\n- Đốt cháy $1\\text{ mol}$ $\\text{CH}_4$ tỏa ra $890,3\\text{ kJ}$, vậy đốt cháy $0,2\\text{ mol}$ $\\text{CH}_4$ tỏa ra nhiệt lượng: $Q = 0,2 \\cdot 890,3 = 178,06\\text{ kJ}$.",
        "Phản ứng tôi vôi ($\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2$) làm nước sôi lên là phản ứng tỏa nhiệt ($\Delta_r H < 0$); còn hòa tan viên sủi vitamin C vào cốc nước thấy cốc nước mát lạnh là quá trình thu nhiệt ($\Delta_r H > 0$).",
        CH5_ID, CH5_TITLE, CH5_DESC,
        extra_questions=[
            mcq("Một phản ứng hóa học có biến thiên enthalpy chuẩn $\\Delta_r H^\\circ_{298} = +178,3\\text{ kJ}$. Phát biểu nào sau đây đúng?", "Đó là phản ứng thu nhiệt", ["Đó là phản ứng thu nhiệt", "Đó là phản ứng tỏa nhiệt", "Phản ứng giải phóng năng lượng ra môi trường", "Phản ứng không có sự trao đổi nhiệt"], "Khi $\\Delta_r H^\\circ_{298} > 0$, phản ứng thu nhiệt từ môi trường xung quanh (như phản ứng nung đá vôi).", "biet"),
            mcq("Ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$), chất nào sau đây có enthalpy tạo thành chuẩn $\\Delta_f H^\\circ_{298}$ bằng $0\\text{ kJ/mol}$?", "$\\text{O}_2(g)$", ["$\\text{O}_2(g)$", "$\\text{CO}_2(g)$", "$\\text{H}_2\\text{O}(l)$", "$\\text{O}_3(g)$"], "$\\text{O}_2(g)$ là đơn chất bền vững nhất của oxygen ở điều kiện chuẩn nên có $\\Delta_f H^\\circ_{298} = 0$ (còn $\\text{O}_3$ kém bền hơn).", "hieu"),
            short("Biết phản ứng nhiệt phân $1\\text{ mol}$ $\\text{CaCO}_3(s) \\rightarrow \\text{CaO}(s) + \\text{CO}_2(g)$ cần thu vào $178,3\\text{ kJ}$ nhiệt lượng. Để phân hủy hoàn toàn $2\\text{ mol}$ $\\text{CaCO}_3$ cần cung cấp tối thiểu bao nhiêu $\\text{kJ}$ nhiệt lượng?", "356,6", ["356,6", "356.6"], "Nhiệt lượng cần cung cấp cho $2\\text{ mol}$ $\\text{CaCO}_3$ là $Q = 2 \\cdot 178,3 = 356,6\\text{ kJ}$.", "vandung"),
        ]
    ),
    bai(14, "Tính biến thiên enthalpy của phản ứng hóa học",
        "Hai công thức tính biến thiên enthalpy chuẩn: theo enthalpy tạo thành chuẩn (Sản phẩm trừ Chất đầu) và theo năng lượng liên kết (Chất đầu trừ Sản phẩm)",
        "Có hai cách tính biến thiên enthalpy chuẩn ($\\Delta_r H^\\circ_{298}$) của một phản ứng hóa học: (1) Tính theo enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$): lấy tổng enthalpy tạo thành chuẩn của các chất sản phẩm trừ đi tổng enthalpy tạo thành chuẩn của các chất đầu (có nhân với hệ số tỉ lượng trong phương trình). (2) Tính theo năng lượng liên kết ($E_b$, áp dụng cho phản ứng mà tất cả các chất đều ở thể khí): lấy tổng năng lượng liên kết trong các phân tử chất đầu trừ đi tổng năng lượng liên kết trong các phân tử sản phẩm.",
        [
            F("Công thức 1: Tính theo Enthalpy tạo thành chuẩn (Delta_f H)", "\\Delta_r H^\\circ_{298} = \\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm}) - \\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu})", "Nhớ quy tắc: theo nhiệt tạo thành = Sản phẩm trừ Chất đầu (nhớ nhân hệ số cân bằng)"),
            F("Công thức 2: Tính theo Năng lượng liên kết (Eb, các chất ở thể khí)", "\\Delta_r H^\\circ_{298} = \\sum E_b(\\text{chất đầu}) - \\sum E_b(\\text{sản phẩm})", "Nhớ quy tắc: theo năng lượng liên kết = Chất đầu trừ Sản phẩm"),
        ],
        [
            "Vận dụng được công thức tính $\\Delta_r H^\\circ_{298}$ dựa vào enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$) của các chất",
            "Vận dụng được công thức tính $\\Delta_r H^\\circ_{298}$ dựa vào năng lượng liên kết ($E_b$) của các chất khí",
            "So sánh được hiệu quả tỏa nhiệt của các loại nhiên liệu dựa trên giá trị $\\Delta_r H^\\circ_{298}$ tính được",
        ],
        "Cho phản ứng: $\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)$. Biết năng lượng liên kết ở điều kiện chuẩn: $E_b(\\text{H}-\\text{H}) = 436\\text{ kJ/mol}$, $E_b(\\text{Cl}-\\text{Cl}) = 243\\text{ kJ/mol}$, $E_b(\\text{H}-\\text{Cl}) = 432\\text{ kJ/mol}$. Tính $\\Delta_r H^\\circ_{298}$ của phản ứng.",
        "Áp dụng công thức tính theo năng lượng liên kết (Chất đầu trừ Sản phẩm):\\n$\\Delta_r H^\\circ_{298} = E_b(\\text{H}-\\text{H}) + E_b(\\text{Cl}-\\text{Cl}) - 2 \\cdot E_b(\\text{H}-\\text{Cl})$\\n$\\Delta_r H^\\circ_{298} = 436 + 243 - 2 \\cdot 432 = 679 - 864 = -185\\text{ kJ}$.",
        "Tính toán biến thiên enthalpy giúp các kĩ sư hóa học thiết kế hệ thống làm mát cho các lò phản ứng tỏa nhiệt mạnh (như tổng hợp $\\text{NH}_3$, sản xuất $\\text{H}_2\\text{SO}_4$) để tránh nguy cơ nổ nhiệt.",
        CH5_ID, CH5_TITLE, CH5_DESC,
        extra_questions=[
            mcq("Khi tính biến thiên enthalpy chuẩn của phản ứng ($\\Delta_r H^\\circ_{298}$) dựa vào enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$), công thức đúng là:", "$\\Delta_r H^\\circ_{298} = \\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm}) - \\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu})$", ["$\\Delta_r H^\\circ_{298} = \\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm}) - \\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu})$", "$\\Delta_r H^\\circ_{298} = \\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu}) - \\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm})$", "$\\Delta_r H^\\circ_{298} = \\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm}) + \\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu})$", "$\\Delta_r H^\\circ_{298} = \\frac{\\sum \\Delta_f H^\\circ_{298}(\\text{sản phẩm})}{\\sum \\Delta_f H^\\circ_{298}(\\text{chất đầu})}$"], "Theo enthalpy tạo thành chuẩn ($\\Delta_f H^\\circ_{298}$): lấy tổng của sản phẩm trừ đi tổng của chất đầu.", "biet"),
            mcq("Khi tính $\\Delta_r H^\\circ_{298}$ của phản ứng giữa các chất khí dựa vào năng lượng liên kết ($E_b$), công thức đúng là:", "$\\Delta_r H^\\circ_{298} = \\sum E_b(\\text{chất đầu}) - \\sum E_b(\\text{sản phẩm})$", ["$\\Delta_r H^\\circ_{298} = \\sum E_b(\\text{chất đầu}) - \\sum E_b(\\text{sản phẩm})$", "$\\Delta_r H^\\circ_{298} = \\sum E_b(\\text{sản phẩm}) - \\sum E_b(\\text{chất đầu})$", "$\\Delta_r H^\\circ_{298} = \\sum E_b(\\text{chất đầu}) + \\sum E_b(\\text{sản phẩm})$", "$\\Delta_r H^\\circ_{298} = 2\\sum E_b(\\text{chất đầu})$"], "Phá vỡ liên kết chất đầu cần thu năng lượng ($+$), hình thành liên kết sản phẩm tỏa năng lượng ($-$), nên lấy chất đầu trừ sản phẩm.", "hieu"),
            short("Cho phản ứng: $\\text{C}(s) + \\text{O}_2(g) \\rightarrow \\text{CO}_2(g)$. Biết $\\Delta_f H^\\circ_{298}(\\text{CO}_2, g) = -393,5\\text{ kJ/mol}$ và đơn chất bền có $\\Delta_f H^\\circ_{298} = 0$. Giá trị $\\Delta_r H^\\circ_{298}$ của phản ứng bằng bao nhiêu $\\text{kJ}$?", "-393,5", ["-393,5", "-393.5"], "Ta có $\\Delta_r H^\\circ_{298} = \\Delta_f H^\\circ_{298}(\\text{CO}_2) - [\\Delta_f H^\\circ_{298}(\\text{C}) + \\Delta_f H^\\circ_{298}(\\text{O}_2)] = -393,5 - 0 = -393,5\\text{ kJ}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 6: TỐC ĐỘ PHẢN ỨNG HÓA HỌC
# =========================================================================
CH6_ID = "hoa10_ch6"
CH6_TITLE = "Chương 6: Tốc độ phản ứng hóa học"
CH6_DESC = "Phương trình tốc độ phản ứng, tốc độ trung bình và 5 yếu tố ảnh hưởng đến tốc độ phản ứng (nồng độ, áp suất, nhiệt độ, diện tích bề mặt, chất xúc tác)"

CH6_LESSONS = [
    bai(15, "Phương trình tốc độ phản ứng và hằng số tốc độ của phản ứng",
        "Khái niệm tốc độ phản ứng, công thức tính tốc độ trung bình và định luật tác dụng khối lượng (v = k.C_A^a.C_B^b)",
        "Tốc độ phản ứng ($v$) của một phản ứng hóa học là đại lượng đặc trưng cho sự biến thiên nồng độ của một trong các chất phản ứng hoặc sản phẩm phản ứng trong một đơn vị thời gian. Đối với phản ứng tổng quát $a\\text{A} + b\\text{B} \\rightarrow m\\text{M} + n\\text{N}$, tốc độ trung bình ($\\overline{v}$) trong khoảng thời gian $\\Delta t = t_2 - t_1$ được tính bằng độ biến thiên nồng độ chia cho $\\Delta t$ và chia cho hệ số tỉ lượng. Đối với phản ứng đơn giản, định luật tác dụng khối lượng biểu diễn tốc độ tức thời: $v = k \\cdot C_{\\text{A}}^a \\cdot C_{\\text{B}}^b$, trong đó $k$ là hằng số tốc độ phản ứng (chỉ phụ thuộc vào bản chất chất phản ứng và nhiệt độ).",
        [
            F("Tốc độ trung bình của phản ứng (aA + bB -> mM + nN)", "\\overline{v} = -\\frac{1}{a}\\frac{\\Delta C_{\\text{A}}}{\\Delta t} = -\\frac{1}{b}\\frac{\\Delta C_{\\text{B}}}{\\Delta t} = +\\frac{1}{m}\\frac{\\Delta C_{\\text{M}}}{\\Delta t} = +\\frac{1}{n}\\frac{\\Delta C_{\\text{N}}}{\\Delta t}", "Dấu trừ (-) trước chất tham gia vì nồng độ chất tham gia giảm theo thời gian (Delta C < 0)"),
            F("Định luật tác dụng khối lượng (cho phản ứng đơn giản)", "v = k \\cdot C_{\\text{A}}^a \\cdot C_{\\text{B}}^b", "k là hằng số tốc độ phản ứng; không đưa nồng độ chất rắn nguyên chất vào biểu thức tốc độ"),
        ],
        [
            "Trình bày được khái niệm tốc độ phản ứng hóa học và đơn vị của tốc độ phản ứng (thường là $\\text{mol/(L}\\cdot\\text{s)}$ hoặc $\\text{M/s}$)",
            "Vận dụng được công thức tính tốc độ trung bình của phản ứng từ độ biến thiên nồng độ theo thời gian",
            "Viết được biểu thức tốc độ phản ứng theo định luật tác dụng khối lượng cho phản ứng đơn giản và nêu được ý nghĩa của hằng số tốc độ $k$",
        ],
        "Cho phản ứng: $\\text{Br}_2 + \\text{HCOOH} \\rightarrow 2\\text{HBr} + \\text{CO}_2$. Ở thời điểm đầu ($t_1 = 0$), nồng độ $\\text{Br}_2$ là $0,012\\text{ M}$. Sau $50\\text{ s}$, nồng độ $\\text{Br}_2$ còn lại là $0,010\\text{ M}$. Tính tốc độ trung bình của phản ứng trong $50\\text{ s}$ đó.",
        "Áp dụng công thức tính tốc độ trung bình theo $\\text{Br}_2$ (hệ số $a = 1$):\\n$\\overline{v} = -\\frac{C_2 - C_1}{t_2 - t_1} = -\\frac{0,010 - 0,012}{50 - 0} = \\frac{0,002}{50} = 4 \\cdot 10^{-5}\\text{ mol/(L}\\cdot\\text{s)}$.",
        "Phản ứng nổ thuốc súng xảy ra với tốc độ cực nhanh (trong phần nghìn giây), trong khi phản ứng tạo gỉ sắt hay sự phong hóa đá vôi trong tự nhiên diễn ra rất chậm qua nhiều tháng, nhiều năm.",
        CH6_ID, CH6_TITLE, CH6_DESC,
        extra_questions=[
            mcq("Đơn vị thường dùng của tốc độ phản ứng hóa học trong dung dịch là:", "$\\text{mol/(L}\\cdot\\text{s)}$ (hoặc $\\text{M}\\cdot\\text{s}^{-1}$)", ["$\\text{mol/(L}\\cdot\\text{s)}$ (hoặc $\\text{M}\\cdot\\text{s}^{-1}$)", "$\\text{kJ/mol}$", "$\\text{g/mol}$", "$\\text{m/s}$"], "Tốc độ phản ứng bằng biến thiên nồng độ ($\\text{mol/L}$ hay $\\text{M}$) chia cho thời gian ($\\text{s}, \\text{min}$).", "biet"),
            mcq("Cho phản ứng đơn giản ở thể khí: $2\\text{NO}(g) + \\text{O}_2(g) \\rightarrow 2\\text{NO}_2(g)$. Biểu thức tốc độ tức thời của phản ứng theo định luật tác dụng khối lượng là:", "$v = k \\cdot C_{\\text{NO}}^2 \\cdot C_{\\text{O}_2}$", ["$v = k \\cdot C_{\\text{NO}}^2 \\cdot C_{\\text{O}_2}$", "$v = k \\cdot C_{\\text{NO}} \\cdot C_{\\text{O}_2}$", "$v = k \\cdot (2C_{\\text{NO}}) \\cdot C_{\\text{O}_2}$", "$v = k \\cdot C_{\\text{NO}_2}^2$"], "Theo định luật tác dụng khối lượng, số mũ nồng độ các chất tham gia bằng hệ số cân bằng của chúng: $v = k \\cdot C_{\\text{NO}}^2 \\cdot C_{\\text{O}_2}^1$.", "hieu"),
            short("Với phản ứng đơn giản $2\\text{NO}(g) + \\text{O}_2(g) \\rightarrow 2\\text{NO}_2(g)$ có $v = k \\cdot C_{\\text{NO}}^2 \\cdot C_{\\text{O}_2}$. Nếu giữ nguyên nhiệt độ và nồng độ $\\text{O}_2$, nhưng tăng nồng độ $\\text{NO}$ lên gấp $3$ lần thì tốc độ phản ứng tăng lên bao nhiêu lần?", "9", ["9"], "Vì $v$ tỉ lệ thuận với $C_{\\text{NO}}^2$, khi $C_{\\text{NO}}$ tăng $3$ lần thì $v$ tăng $3^2 = 9$ lần.", "vandung"),
        ]
    ),
    bai(16, "Các yếu tố ảnh hưởng đến tốc độ phản ứng",
        "Ảnh hưởng của nồng độ, áp suất, nhiệt độ (hệ số nhiệt độ Van't Hoff), diện tích bề mặt tiếp xúc và chất xúc tác",
        "Có $5$ yếu tố chính làm tăng tốc độ phản ứng hóa học: (1) Tăng nồng độ chất phản ứng (làm tăng tần số va chạm hiệu quả); (2) Tăng áp suất đối với phản ứng có chất khí tham gia; (3) Tăng nhiệt độ: theo quy tắc thực nghiệm Van't Hoff, khi nhiệt độ tăng thêm $10^\\circ\\text{C}$ thì tốc độ phản ứng thường tăng từ $2$ đến $4$ lần (gọi là hệ số nhiệt độ $\\gamma$); (4) Tăng diện tích bề mặt tiếp xúc của chất rắn (bằng cách đập nhỏ, nghiền mịn); (5) Sử dụng chất xúc tác (chất làm tăng tốc độ phản ứng nhưng vẫn giữ nguyên về lượng và chất sau khi phản ứng kết thúc).",
        [
            F("Công thức hệ số nhiệt độ Van't Hoff", "\\frac{v_2}{v_1} = \\gamma^{\\frac{t_2 - t_1}{10}}", "v1, v2 là tốc độ ở nhiệt độ t1, t2; gamma (thường từ 2 đến 4) là hệ số nhiệt độ Van't Hoff"),
            F("Tổng kết 5 yếu tố làm tăng tốc độ phản ứng", "\\begin{cases} C \\uparrow,\\; P_{\\text{khí}} \\uparrow,\\; T \\uparrow,\\; S_{\\text{bề mặt}} \\uparrow \\implies v \\uparrow \\\\ \\text{Có chất xúc tác} \\implies \\text{Giảm năng lượng hoạt hóa } \\implies v \\uparrow \\end{cases}", "Ngược lại, chất ức chế và việc bảo quản lạnh làm giảm tốc độ phản ứng phân hủy"),
        ],
        [
            "Giải thích được ảnh hưởng của nồng độ, áp suất, nhiệt độ, diện tích bề mặt và chất xúc tác đến tốc độ phản ứng",
            "Vận dụng được công thức hệ số nhiệt độ Van't Hoff $\\frac{v_2}{v_1} = \\gamma^{\\frac{t_2 - t_1}{10}}$ để tính độ thay đổi tốc độ phản ứng khi thay đổi nhiệt độ",
            "Giải thích được các ứng dụng điều khiển tốc độ phản ứng trong đời sống và sản xuất (nồi áp suất, tủ lạnh, chẻ nhỏ củi, quạt than)",
        ],
        "Một phản ứng có hệ số nhiệt độ Van't Hoff $\\gamma = 3$. Hỏi khi tăng nhiệt độ của phản ứng từ $20^\\circ\\text{C}$ lên $50^\\circ\\text{C}$ thì tốc độ phản ứng tăng lên bao nhiêu lần?",
        "Độ tăng nhiệt độ: $\\Delta t = t_2 - t_1 = 50 - 20 = 30^\\circ\\text{C}$.\\nÁp dụng công thức Van't Hoff:\\n$\\frac{v_2}{v_1} = \\gamma^{\\frac{t_2 - t_1}{10}} = 3^{\\frac{30}{10}} = 3^3 = 27$ lần.",
        "Bảo quản thực phẩm trong tủ lạnh là giảm nhiệt độ để làm chậm tốc độ phản ứng oxi hóa và phân hủy thức ăn; hầm xương bằng nồi áp suất giúp tăng áp suất và nhiệt độ sôi của nước nên thực phẩm nhanh chín mềm.",
        CH6_ID, CH6_TITLE, CH6_DESC,
        extra_questions=[
            mcq("Yếu tố nào sau đây KHÔNG làm thay đổi tốc độ của phản ứng chỉ có các chất rắn và dung dịch tham gia (không có chất khí)?", "Áp suất", ["Áp suất", "Nhiệt độ", "Nồng độ dung dịch", "Diện tích bề mặt chất rắn"], "Áp suất chỉ ảnh hưởng đến tốc độ của các phản ứng có chất khí tham gia.", "biet"),
            mcq("Khi đốt than tổ ong, người ta tạo các lỗ thông khí xuyên dọc viên than nhằm mục đích chính là:", "Tăng diện tích bề mặt tiếp xúc giữa than với khí oxygen để than cháy nhanh và đều hơn", ["Tăng diện tích bề mặt tiếp xúc giữa than với khí oxygen để than cháy nhanh và đều hơn", "Làm giảm nhiệt độ cháy của than", "Đóng vai trò chất xúc tác cho phản ứng", "Làm tăng khối lượng riêng của viên than"], "Các lỗ tổ ong giúp tăng diện tích tiếp xúc giữa chất rắn (than $\\text{C}$) và chất khí ($\\text{O}_2$), làm tăng tốc độ phản ứng cháy.", "hieu"),
            short("Một phản ứng có hệ số nhiệt độ Van't Hoff $\\gamma = 2$. Khi tăng nhiệt độ từ $30^\\circ\\text{C}$ lên $60^\\circ\\text{C}$ thì tốc độ phản ứng tăng lên bao nhiêu lần?", "8", ["8"], "Ta có $\\frac{v_2}{v_1} = 2^{\\frac{60-30}{10}} = 2^3 = 8$ lần.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 7: NGUYÊN TỐ NHÓM HALOGEN
# =========================================================================
CH7_ID = "hoa10_ch7"
CH7_TITLE = "Chương 7: Nguyên tố nhóm Halogen"
CH7_DESC = "Đơn chất nhóm VIIA (F2, Cl2, Br2, I2), hydrogen halide (HF, HCl, HBr, HI), hydrohalic acid và nhận biết ion halide"

CH7_LESSONS = [
    bai(17, "Vị trí, cấu hình electron và tính chất vật lí của các đơn chất nhóm VIIA",
        "Cấu hình electron lớp ngoài cùng ns2 np5, sự biến đổi trạng thái, màu sắc và nhiệt độ sôi từ F2 đến I2",
        "Nhóm $\\text{VIIA}$ (nhóm halogen) gồm các nguyên tố: fluorine ($\\text{F}, Z=9$), chlorine ($\\text{Cl}, Z=17$), bromine ($\\text{Br}, Z=35$), iodine ($\\text{I}, Z=53$) và các nguyên tố phóng xạ ($\\text{At}, \\text{Ts}$). Nguyên tử các nguyên tố halogen đều có $7$ electron lớp ngoài cùng với cấu hình $ns^2 np^5$, nên ở trạng thái tự do hai nguyên tử góp chung $1$ cặp electron tạo phân tử hai nguyên tử $\\text{X}_2$ ($\\text{F}_2, \\text{Cl}_2, \\text{Br}_2, \\text{I}_2$). Đi từ $\\text{F}_2$ đến $\\text{I}_2$: trạng thái chuyển từ khí ($\\text{F}_2$ lục nhạt, $\\text{Cl}_2$ vàng lục) sang lỏng ($\\text{Br}_2$ nâu đỏ) rồi rắn ($\\text{I}_2$ đen tím, có tính thăng hoa); màu sắc đậm dần và nhiệt độ nóng chảy, nhiệt độ sôi tăng dần do tương tác van der Waals tăng.",
        [
            F("Cấu hình electron lớp ngoài cùng nhóm VIIA", "ns^2 np^5\\quad (7\\text{ electron lớp ngoài cùng})", "Phân tử đơn chất có công thức X2 với 1 liên kết đơn X-X"),
            F("Biến đổi tính chất vật lí từ F2 -> Cl2 -> Br2 -> I2", "\\begin{cases} \\text{Trạng thái: Khí } (\\text{F}_2, \\text{Cl}_2) \\rightarrow \\text{Lỏng } (\\text{Br}_2) \\rightarrow \\text{Rắn } (\\text{I}_2) \\\\ \\text{Màu sắc: Đậm dần (Lục nhạt } \\rightarrow \\text{Vàng lục } \\rightarrow \\text{Nâu đỏ } \\rightarrow \\text{Đen tím)} \\\\ \\text{Nhiệt độ sôi } (t_s): \\text{F}_2 < \\text{Cl}_2 < \\text{Br}_2 < \\text{I}_2 \\end{cases}", "Nhiệt độ sôi tăng dần do phân tử khối và tương tác van der Waals tăng dần"),
        ],
        [
            "Phát biểu được vị trí, cấu hình electron lớp ngoài cùng $ns^2 np^5$ và đặc điểm liên kết trong phân tử $\\text{X}_2$ của các nguyên tố halogen",
            "Trình bày được trạng thái, màu sắc và giải thích được xu hướng biến đổi nhiệt độ nóng chảy, nhiệt độ sôi của các đơn chất từ $\\text{F}_2$ đến $\\text{I}_2$",
            "Nêu được hiện tượng thăng hoa của tinh thể iodine ($\\text{I}_2$) khi đun nóng",
        ],
        "Giải thích vì sao nhiệt độ sôi của các đơn chất halogen tăng dần theo thứ tự $\\text{F}_2 (-188^\\circ\\text{C}) < \\text{Cl}_2 (-34^\\circ\\text{C}) < \\text{Br}_2 (59^\\circ\\text{C}) < \\text{I}_2 (184^\\circ\\text{C})$.",
        "Các phân tử $\\text{F}_2, \\text{Cl}_2, \\text{Br}_2, \\text{I}_2$ đều là các phân tử không phân cực. Đi từ $\\text{F}_2$ đến $\\text{I}_2$, khối lượng phân tử và kích thước phân tử (số electron) tăng dần, làm cho tương tác van der Waals giữa các phân tử tăng dần, dẫn đến nhiệt độ sôi tăng dần.",
        "Khi đun nóng tinh thể iodine ($\\text{I}_2$) màu đen tím trong ống nghiệm, iodine chuyển trực tiếp từ thể rắn sang hơi màu tím mà không qua trạng thái lỏng — hiện tượng này gọi là sự thăng hoa, dùng để tinh chế iodine.",
        CH7_ID, CH7_TITLE, CH7_DESC,
        extra_questions=[
            mcq("Cấu hình electron lớp ngoài cùng chung của nguyên tử các nguyên tố nhóm halogen (nhóm $\\text{VIIA}$) là:", "$ns^2 np^5$", ["$ns^2 np^5$", "$ns^2 np^6$", "$ns^2 np^4$", "$ns^1$"], "Các nguyên tố nhóm $\\text{VIIA}$ có $7$ electron lớp ngoài cùng với cấu hình chung $ns^2 np^5$.", "biet"),
            mcq("Đơn chất halogen nào sau đây ở điều kiện thường là chất rắn màu đen tím và có hiện tượng thăng hoa khi đun nóng?", "Iodine ($\\text{I}_2$)", ["Iodine ($\\text{I}_2$)", "Fluorine ($\\text{F}_2$)", "Chlorine ($\\text{Cl}_2$)", "Bromine ($\\text{Br}_2$)"], "$\\text{I}_2$ là chất rắn màu đen tím ở điều kiện thường và dễ thăng hoa thành hơi màu tím khi đun nóng.", "hieu"),
            short("Trong một nguyên tử của bất kì nguyên tố nhóm halogen nào ở trạng thái cơ bản có bao nhiêu electron độc thân?", "1", ["1"], "Cấu hình lớp ngoài cùng $ns^2 np^5$ có $1$ orbital $p$ chỉ chứa $1$ electron độc thân.", "vandung"),
        ]
    ),
    bai(18, "Tính chất hóa học và điều chế các đơn chất nhóm VIIA",
        "Tính oxi hóa mạnh giảm dần từ F2 đến I2, phản ứng với kim loại, hydrogen, nước, dung dịch kiềm, dung dịch muối halide và điều chế Cl2",
        "Do có $7$ electron lớp ngoài cùng và độ âm điện lớn, các đơn chất halogen thể hiện tính oxi hóa mạnh ($\\text{X}_2 + 2\\text{e} \\rightarrow 2\\text{X}^-$) và tính oxi hóa giảm dần từ $\\text{F}_2 > \\text{Cl}_2 > \\text{Br}_2 > \\text{I}_2$. Các halogen oxi hóa hầu hết kim loại tạo muối halide ($2\\text{Fe} + 3\\text{Cl}_2 \\xrightarrow{t^\\circ} 2\\text{FeCl}_3$), tác dụng với $\\text{H}_2$ với mức độ giảm dần ($\\text{F}_2$ nổ ngay trong bóng tối, $\\text{I}_2$ thuận nghịch cần đun nóng và xúc tác). $\\text{Cl}_2$ tác dụng với nước và dung dịch $\\text{NaOH}$ (nước Javel) vừa đóng vai trò chất oxi hóa vừa đóng vai trò chất khử. Halogen mạnh hơn (từ $\\text{Cl}_2$) đẩy được halogen yếu hơn ra khỏi dung dịch muối. Trong công nghiệp, $\\text{Cl}_2$ được điều chế bằng điện phân dung dịch $\\text{NaCl}$ bão hòa có màng ngăn.",
        [
            F("Qui luật tính oxi hóa và Phản ứng thế Halide", "\\text{Tính oxi hóa: } \\text{F}_2 > \\text{Cl}_2 > \\text{Br}_2 > \\text{I}_2;\\quad \\text{Cl}_2 + 2\\text{NaBr} \\rightarrow 2\\text{NaCl} + \\text{Br}_2", "Cl2 đẩy được Br2 và I2; Br2 đẩy được I2 ra khỏi dung dịch muối"),
            F("Phản ứng tự oxi hóa - tự khử của Cl2", "\\text{Cl}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCl} + \\text{HClO};\\quad \\text{Cl}_2 + 2\\text{NaOH} \\rightarrow \\text{NaCl} + \\text{NaClO} + \\text{H}_2\\text{O}", "HClO và NaClO có tính oxi hóa rất mạnh, dùng tẩy trắng và sát trùng"),
            F("Điều chế Cl2 trong phòng thí nghiệm và công nghiệp", "\\begin{cases} \\text{PTN: } \\text{MnO}_2 + 4\\text{HCl}_{\\text{đặc}} \\xrightarrow{t^\\circ} \\text{MnCl}_2 + \\text{Cl}_2\\uparrow + 2\\text{H}_2\\text{O} \\\\ \\text{CN: } 2\\text{NaCl} + 2\\text{H}_2\\text{O} \\xrightarrow{\\text{đpdd, màng ngăn}} 2\\text{NaOH} + \\text{Cl}_2\\uparrow + \\text{H}_2\\uparrow \\end{cases}", "Không có màng ngăn thì Cl2 tác dụng với NaOH tạo nước Javel"),
        ],
        [
            "Giải thích được tính chất hóa học đặc trưng của các đơn chất halogen là tính oxi hóa mạnh và giảm dần từ $\\text{F}_2$ đến $\\text{I}_2$",
            "Viết được phương trình hóa học của halogen với kim loại, $\\text{H}_2$, nước, dung dịch $\\text{NaOH}$ và dung dịch muối halide",
            "Trình bày được phương pháp điều chế khí $\\text{Cl}_2$ trong phòng thí nghiệm và trong công nghiệp",
        ],
        "Đốt cháy hoàn toàn $5,6\\text{ g}$ bột sắt ($\\text{Fe} = 56$) trong bình chứa khí $\\text{Cl}_2$ dư. Tính khối lượng muối sắt thu được.",
        "Số mol $\\text{Fe}$: $n_{\\text{Fe}} = \\frac{5,6}{56} = 0,1\\text{ mol}$.\\nVì $\\text{Cl}_2$ có tính oxi hóa mạnh nên oxi hóa $\\text{Fe}$ lên số oxi hóa $+3$:\\n$2\\text{Fe} + 3\\text{Cl}_2 \\xrightarrow{t^\\circ} 2\\text{FeCl}_3$.\\nSố mol $\\text{FeCl}_3$ ($M = 162,5$): $n_{\\text{FeCl}_3} = n_{\\text{Fe}} = 0,1\\text{ mol} \\Rightarrow m_{\\text{FeCl}_3} = 0,1 \\cdot 162,5 = 16,25\\text{ g}$.",
        "Nước biển chứa một lượng đáng kể muối $\\text{NaBr}$; người ta sục khí $\\text{Cl}_2$ vào nước biển đã cô đặc để oxi hóa $\\text{Br}^-$ thành đơn chất $\\text{Br}_2$ phục vụ công nghiệp hóa chất và dược phẩm.",
        CH7_ID, CH7_TITLE, CH7_DESC,
        extra_questions=[
            mcq("Cho phản ứng của các đơn chất halogen với khí $\\text{H}_2$. Đơn chất nào phản ứng mãnh liệt nhất (gây nổ ngay trong bóng tối ở nhiệt độ rất thấp)?", "$\\text{F}_2$", ["$\\text{F}_2$", "$\\text{Cl}_2$", "$\\text{Br}_2$", "$\\text{I}_2$"], "$\\text{F}_2$ có tính oxi hóa mạnh nhất nên phản ứng nổ với $\\text{H}_2$ ngay trong bóng tối ở $-252^\\circ\\text{C}$.", "biet"),
            mcq("Trong phản ứng của khí $\\text{Cl}_2$ với dung dịch $\\text{NaOH}$ ở nhiệt độ thường tạo nước Javel ($\\text{Cl}_2 + 2\\text{NaOH} \\rightarrow \\text{NaCl} + \\text{NaClO} + \\text{H}_2\\text{O}$), vai trò của $\\text{Cl}_2$ là:", "Vừa là chất oxi hóa, vừa là chất khử", ["Vừa là chất oxi hóa, vừa là chất khử", "Chỉ là chất oxi hóa", "Chỉ là chất khử", "Không phải chất oxi hóa cũng không phải chất khử"], "Số oxi hóa của $\\text{Cl}$ từ $0$ vừa giảm xuống $-1$ (trong $\\text{NaCl}$) vừa tăng lên $+1$ (trong $\\text{NaClO}$).", "hieu"),
            short("Cho $8,7\\text{ g}$ $\\text{MnO}_2$ ($M = 87$) tác dụng hết với dung dịch $\\text{HCl}$ đặc, đun nóng dư. Tính số mol khí $\\text{Cl}_2$ thu được.", "0,1", ["0,1", "0.1"], "PTHH: $\\text{MnO}_2 + 4\\text{HCl} \\xrightarrow{t^\\circ} \\text{MnCl}_2 + \\text{Cl}_2\\uparrow + 2\\text{H}_2\\text{O}$. Số mol $n_{\\text{Cl}_2} = n_{\\text{MnO}_2} = \\frac{8,7}{87} = 0,1\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(19, "Hydrogen halide và một số phản ứng của ion halide",
        "Xu hướng biến đổi nhiệt độ sôi, tính acid của dãy HF -> HI, tính khử của ion halide và nhận biết ion X- bằng AgNO3",
        "Các hydrogen halide ($\\text{HF}, \\text{HCl}, \\text{HBr}, \\text{HI}$) là các hợp chất cộng hóa trị phân cực. Nhiệt độ sôi tăng từ $\\text{HCl} < \\text{HBr} < \\text{HI}$ do khối lượng phân tử và tương tác van der Waals tăng, riêng $\\text{HF}$ có nhiệt độ sôi cao bất thường ($19,5^\\circ\\text{C}$) do tạo được liên kết hydrogen bền giữa các phân tử. Khi tan vào nước, chúng tạo thành dung dịch hydrohalic acid có tính acid tăng dần từ $\\text{HF}$ (acid yếu, nhưng ăn mòn được thủy tinh $\\text{SiO}_2$) đến $\\text{HCl} < \\text{HBr} < \\text{HI}$ (các acid mạnh) do độ bền liên kết $\\text{H}-\\text{X}$ giảm dần. Tính khử của các ion $X^-$ tăng dần: $\\text{F}^-$ (không có tính khử) $< \\text{Cl}^- < \\text{Br}^- < \\text{I}^-$. Thuốc thử nhận biết các ion halide là dung dịch $\\text{AgNO}_3$.",
        [
            F("Qui luật biến đổi từ HF -> HCl -> HBr -> HI", "\\begin{cases} \\text{Nhiệt độ sôi: } \\text{HCl} < \\text{HBr} < \\text{HI} < \\text{HF (có liên kết hydrogen)} \\\\ \\text{Độ bền liên kết H-X giảm dần } \\implies \\text{Tính acid tăng dần: } \\text{HF} \\ll \\text{HCl} < \\text{HBr} < \\text{HI} \\\\ \\text{Tính khử của ion } X^- \\text{ tăng dần: } \\text{Cl}^- < \\text{Br}^- < \\text{I}^- \\end{cases}", "HF ăn mòn thủy tinh: SiO2 + 4HF -> SiF4 + 2H2O"),
            F("Nhận biết ion Halide (X-) bằng dung dịch AgNO3", "\\begin{cases} \\text{F}^- + \\text{Ag}^+ \\rightarrow \\text{Không hiện tượng (AgF tan)} \\\\ \\text{Cl}^- + \\text{Ag}^+ \\rightarrow \\text{AgCl}\\downarrow\\text{ (kết tủa trắng)} \\\\ \\text{Br}^- + \\text{Ag}^+ \\rightarrow \\text{AgBr}\\downarrow\\text{ (kết tủa vàng nhạt)} \\\\ \\text{I}^- + \\text{Ag}^+ \\rightarrow \\text{AgI}\\downarrow\\text{ (kết tủa vàng đậm)} \\end{cases}", "Dùng dung dịch AgNO3 để phân biệt các muối F-, Cl-, Br-, I-"),
        ],
        [
            "Giải thích được sự biến đổi nhiệt độ sôi của $\\text{HF}, \\text{HCl}, \\text{HBr}, \\text{HI}$ (đặc biệt là nhiệt độ sôi cao bất thường của $\\text{HF}$)",
            "Trình bày được xu hướng biến đổi tính acid của dãy hydrohalic acid và tính khử của các ion halide ($\\text{Cl}^-, \\text{Br}^-, \\text{I}^-$ tác dụng với $\\text{H}_2\\text{SO}_4$ đặc)",
            "Trình bày được cách nhận biết các ion $\\text{F}^-, \\text{Cl}^-, \\text{Br}^-, \\text{I}^-$ trong dung dịch bằng thuốc thử $\\text{AgNO}_3$",
        ],
        "Cho $100\\text{ mL}$ dung dịch $\\text{NaCl}$ $0,2\\text{ M}$ tác dụng với lượng dư dung dịch $\\text{AgNO}_3$. Nêu hiện tượng và tính khối lượng kết tủa thu được.",
        "- Hiện tượng: Xuất hiện kết tủa màu trắng của $\\text{AgCl}$.\\n- Số mol $\\text{NaCl}$: $n_{\\text{NaCl}} = 0,1 \\cdot 0,2 = 0,02\\text{ mol}$.\\n- PTHH: $\\text{NaCl} + \\text{AgNO}_3 \\rightarrow \\text{AgCl}\\downarrow + \\text{NaNO}_3$.\\n- Khối lượng kết tủa $\\text{AgCl}$ ($M = 143,5$): $m_{\\text{AgCl}} = 0,02 \\cdot 143,5 = 2,87\\text{ g}$.",
        "Dung dịch $\\text{HF}$ hòa tan được $\\text{SiO}_2$ nên không thể đựng trong bình thủy tinh mà phải đựng trong bình nhựa, và được ứng dụng để khắc chữ, hoa văn lên bề mặt kính thủy tinh; muối ăn được trộn thêm một lượng nhỏ $\\text{KI}$ hoặc $\\text{KIO}_3$ (muối i-ốt) để phòng bệnh bướu cổ.",
        CH7_ID, CH7_TITLE, CH7_DESC,
        extra_questions=[
            mcq("Dung dịch acid nào sau đây không thể chứa trong bình thủy tinh vì có phản ứng ăn mòn thủy tinh ($\\text{SiO}_2$)?", "Dung dịch $\\text{HF}$", ["Dung dịch $\\text{HF}$", "Dung dịch $\\text{HCl}$", "Dung dịch $\\text{HBr}$", "Dung dịch $\\text{HI}$"], "Phương trình ăn mòn thủy tinh: $\\text{SiO}_2 + 4\\text{HF} \\rightarrow \\text{SiF}_4\\uparrow + 2\\text{H}_2\\text{O}$.", "biet"),
            mcq("Nhỏ dung dịch $\\text{AgNO}_3$ vào ống nghiệm đựng dung dịch $\\text{NaI}$ thấy xuất hiện kết tủa có màu gì?", "Màu vàng đậm", ["Màu vàng đậm", "Màu trắng", "Màu xanh lam", "Không có kết tủa"], "$\\text{AgCl}$ kết tủa trắng, $\\text{AgBr}$ kết tủa vàng nhạt, còn $\\text{AgI}$ kết tủa màu vàng đậm.", "hieu"),
            short("Trong $4$ dung dịch acid có cùng nồng độ mol: (1) $\\text{HF}$, (2) $\\text{HCl}$, (3) $\\text{HBr}$, (4) $\\text{HI}$, dung dịch có tính acid mạnh nhất ứng với số thứ tự nào?", "4", ["4"], "Tính acid tăng dần theo thứ tự $\\text{HF} < \\text{HCl} < \\text{HBr} < \\text{HI}$, nên $\\text{HI}$ (số 4) là acid mạnh nhất.", "vandung"),
        ]
    ),
    bai(20, "Muối halide và ứng dụng trong y tế, công nghiệp",
        "Tính chất muối halide, điều chế HCl bằng phương pháp sunfat, nước muối sinh lí NaCl 0,9% và phòng bệnh bướu cổ bằng muối i-ốt",
        "Hầu hết các muối halide đều dễ tan trong nước, trừ một số muối không tan như $\\text{AgCl}, \\text{AgBr}, \\text{AgI}$ và ít tan như $\\text{PbCl}_2, \\text{CaF}_2$. Khi tác dụng với $\\text{H}_2\\text{SO}_4$ đặc: muối $\\text{NaCl}$ tinh thể chỉ xảy ra phản ứng trao đổi tạo khí $\\text{HCl}$ (phương pháp sunfat điều chế $\\text{HCl}$ trong phòng thí nghiệm vì $\\text{Cl}^-$ có tính khử yếu không khử được $\\text{H}_2\\text{SO}_4$ đặc), trong khi $\\text{NaBr}$ và $\\text{NaI}$ có tính khử mạnh nên khử $\\text{H}_2\\text{SO}_4$ đặc tạo thành $\\text{Br}_2$ (kèm $\\text{SO}_2$) và $\\text{I}_2$ (kèm $\\text{H}_2\\text{S}$). Muối ăn ($\\text{NaCl}$) là nguyên liệu sống còn của công nghiệp hóa chất (điều chế $\\text{NaOH}, \\text{Cl}_2, \\text{HCl}$, nước Javel, soda) và y tế (nước muối sinh lí $\\text{NaCl}$ $0,9\\%$).",
        [
            F("Phương pháp Sunfat điều chế khí HCl", "\\text{NaCl}_{\\text{rắn}} + \\text{H}_2\\text{SO}_{4\\text{ đặc}} \\xrightarrow{< 250^\\circ\\text{C}} \\text{NaHSO}_4 + \\text{HCl}\\uparrow", "Không dùng phương pháp này để điều chế HBr và HI vì Br- và I- bị H2SO4 đặc oxi hóa thành Br2, I2"),
            F("Phản ứng oxi hóa - khử của Br-, I- với H2SO4 đặc", "\\begin{cases} 2\\text{NaBr} + 2\\text{H}_2\\text{SO}_{4\\text{ đặc}} \\rightarrow \\text{Na}_2\\text{SO}_4 + \\text{Br}_2 + \\text{SO}_2\\uparrow + 2\\text{H}_2\\text{O} \\\\ 8\\text{NaI} + 5\\text{H}_2\\text{SO}_{4\\text{ đặc}} \\rightarrow 4\\text{Na}_2\\text{SO}_4 + 4\\text{I}_2 + \\text{H}_2\\text{S}\\uparrow + 4\\text{H}_2\\text{O} \\end{cases}", "Chứng minh tính khử tăng dần: Cl- < Br- < I-"),
        ],
        [
            "Giải thích được vì sao có thể điều chế khí $\\text{HCl}$ bằng phản ứng của $\\text{NaCl}$ rắn với $\\text{H}_2\\text{SO}_4$ đặc nhưng không áp dụng được để điều chế $\\text{HBr}$ và $\\text{HI}$",
            "Trình bày được vai trò và ứng dụng của $\\text{NaCl}$ trong công nghiệp hóa chất, bảo quản thực phẩm và pha chế nước muối sinh lí $0,9\\%$",
            "Nêu được vai trò của nguyên tố iodine đối với tuyến giáp và cách sử dụng, bảo quản muối i-ốt đúng cách",
        ],
        "Cần dùng bao nhiêu gam $\\text{NaCl}$ tinh khiết để pha chế được $500\\text{ g}$ dung dịch nước muối sinh lí có nồng độ $0,9\\%$?",
        "Áp dụng công thức nồng độ phần trăm:\\n$m_{\\text{NaCl}} = \\frac{m_{\\text{dd}} \\cdot C\\%}{100\\%} = \\frac{500 \\cdot 0,9\\%}{100\\%} = 4,5\\text{ g}$.",
        "Muối i-ốt là muối ăn có trộn thêm một lượng nhỏ $\\text{KI}$ hoặc $\\text{KIO}_3$; khi nấu ăn chỉ nên nêm muối i-ốt sau khi đã tắt bếp vì ở nhiệt độ cao hợp chất chứa iodine dễ bị phân hủy và bay hơi.",
        CH7_ID, CH7_TITLE, CH7_DESC,
        extra_questions=[
            mcq("Trong phòng thí nghiệm, khí $\\text{HCl}$ thường được điều chế bằng cách cho tinh thể $\\text{NaCl}$ tác dụng với chất nào đun nóng?", "Dung dịch $\\text{H}_2\\text{SO}_4$ đặc", ["Dung dịch $\\text{H}_2\\text{SO}_4$ đặc", "Dung dịch $\\text{HNO}_3$ loãng", "Dung dịch $\\text{NaOH}$", "Nước cất"], "Phương pháp sunfat: $\\text{NaCl}_{\\text{rắn}} + \\text{H}_2\\text{SO}_{4\\text{ đặc}} \\xrightarrow{t^\\circ} \\text{NaHSO}_4 + \\text{HCl}\\uparrow$ (dựa vào tính dễ bay hơi của $\\text{HCl}$).", "biet"),
            mcq("Vì sao không dùng phản ứng giữa $\\text{NaBr}$ (hoặc $\\text{NaI}$) rắn với $\\text{H}_2\\text{SO}_4$ đặc nóng để điều chế khí $\\text{HBr}$ (hoặc $\\text{HI}$)?", "Vì $\\text{HBr}$ và $\\text{HI}$ có tính khử mạnh nên bị $\\text{H}_2\\text{SO}_4$ đặc oxi hóa thành $\\text{Br}_2$ và $\\text{I}_2$", ["Vì $\\text{HBr}$ và $\\text{HI}$ có tính khử mạnh nên bị $\\text{H}_2\\text{SO}_4$ đặc oxi hóa thành $\\text{Br}_2$ và $\\text{I}_2$", "Vì $\\text{NaBr}$ và $\\text{NaI}$ không phản ứng với $\\text{H}_2\\text{SO}_4$ đặc", "Vì $\\text{HBr}$ và $\\text{HI}$ là chất rắn không bay hơi", "Vì phản ứng tạo kết tủa bền"], "Ion $\\text{Br}^-$ và $\\text{I}^-$ có tính khử mạnh sẽ khử $\\text{H}_2\\text{SO}_4$ đặc tạo thành $\\text{Br}_2, \\text{I}_2$ chứ không thu được $\\text{HBr}, \\text{HI}$ tinh khiết.", "hieu"),
            short("Hòa tan hoàn toàn một hỗn hợp gồm $\\text{NaF}$ và $\\text{NaCl}$ vào nước dư rồi thêm dung dịch $\\text{AgNO}_3$ dư vào thì thu được $14,35\\text{ g}$ kết tủa. Tính số mol $\\text{NaCl}$ trong hỗn hợp đầu (biết $\\text{AgF}$ tan tốt trong nước, $M_{\\text{AgCl}} = 143,5$).", "0,1", ["0,1", "0.1"], "Vì $\\text{AgF}$ tan nên kết tủa chỉ có $\\text{AgCl}$: $n_{\\text{NaCl}} = n_{\\text{AgCl}} = \\frac{14,35}{143,5} = 0,1\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(21, "Ôn tập và bài toán tổng hợp nhóm Halogen",
        "Hệ thống hóa tính chất đơn chất và hợp chất nhóm VIIA, phương pháp bảo toàn khối lượng và bảo toàn electron trong bài toán halogen",
        "Tổng kết toàn bộ nhóm Halogen (nhóm $\\text{VIIA}$): Đi từ $\\text{F}$ đến $\\text{I}$, bán kính nguyên tử tăng, độ âm điện giảm, dẫn đến tính oxi hóa của đơn chất $\\text{X}_2$ giảm dần ($\\text{F}_2 > \\text{Cl}_2 > \\text{Br}_2 > \\text{I}_2$), trong khi tính acid của các dung dịch $\\text{HX}$ tăng dần ($\\text{HF} < \\text{HCl} < \\text{HBr} < \\text{HI}$) và tính khử của các ion $\\text{X}^-$ tăng dần ($\\text{F}^- < \\text{Cl}^- < \\text{Br}^- < \\text{I}^-$). Trong các bài toán kim loại tác dụng với dung dịch $\\text{HCl}$ tạo muối chloride và khí $\\text{H}_2$, ta áp dụng công thức tính nhanh khối lượng muối: $m_{\\text{muối chloride}} = m_{\\text{kim loại}} + 71 \\cdot n_{\\text{H}_2}$.",
        [
            F("Công thức tính nhanh khối lượng muối Chloride (Kim loại + HCl)", "m_{\\text{muối chloride}} = m_{\\text{kim loại phản ứng}} + m_{\\text{Cl}^-} = m_{\\text{KL}} + 35,5 \\cdot 2n_{\\text{H}_2} = m_{\\text{KL}} + 71 \\cdot n_{\\text{H}_2}", "Do bảo toàn H: n_HCl = 2 * n_H2 => n_Cl- = 2 * n_H2"),
            F("Công thức tăng giảm khối lượng khi Cl2 đẩy Br2 khỏi muối", "\\Delta m_{\\text{muối giảm}} = m_{\\text{Br}} - m_{\\text{Cl}} = (80 - 35,5) \\cdot n_{\\text{Br}^-\\text{ phản ứng}} = 44,5 \\cdot 2n_{\\text{Cl}_2} = 89 \\cdot n_{\\text{Cl}_2}", "1 mol Cl2 phản ứng với 2 mol NaBr làm khối lượng muối giảm 89 g"),
        ],
        [
            "Hệ thống hóa được mối liên hệ giữa cấu tạo nguyên tử và quy luật biến đổi tính chất của đơn chất $\\text{X}_2$ và hợp chất $\\text{HX}$ nhóm $\\text{VIIA}$",
            "Lập được sơ đồ chuyển hóa giữa đơn chất halogen, hydrogen halide và muối halide",
            "Vận dụng định luật bảo toàn khối lượng, bảo toàn nguyên tố và tăng giảm khối lượng để giải bài toán hỗn hợp kim loại hoặc muối halide",
        ],
        "Hòa tan hoàn toàn $11,9\\text{ g}$ hỗn hợp hai kim loại $\\text{Al}$ và $\\text{Zn}$ bằng dung dịch $\\text{HCl}$ dư, sau phản ứng thu được $9,916\\text{ L}$ khí $\\text{H}_2$ (ở đkc) và dung dịch chứa $m$ gam muối khan. Tính giá trị của $m$.",
        "Số mol khí $\\text{H}_2$: $n_{\\text{H}_2} = \\frac{9,916}{24,79} = 0,4\\text{ mol}$.\\nBảo toàn nguyên tố $\\text{H}$: $n_{\\text{HCl}} = 2n_{\\text{H}_2} = 0,8\\text{ mol} \\Rightarrow n_{\\text{Cl}^-\\text{ (trong muối)}} = 0,8\\text{ mol}$.\\nKhối lượng muối khan thu được:\\n$m_{\\text{muối}} = m_{\\text{KL}} + m_{\\text{Cl}^-} = 11,9 + 0,8 \\cdot 35,5 = 11,9 + 28,4 = 40,3\\text{ g}$.",
        "Các hợp chất của nhóm halogen đóng vai trò thiết yếu từ xử lí nước sạch đô thị ($\\text{Cl}_2$), sản xuất chất dẻo chống dính Teflon ($\\text{F}$), phim ảnh ($\\text{AgBr}$) đến cồn sát trùng povidone-iodine ($\\text{I}_2$).",
        CH7_ID, CH7_TITLE, CH7_DESC,
        extra_questions=[
            mcq("Nhận xét nào sau đây ĐÚNG về quy luật biến đổi tính chất trong nhóm halogen theo chiều từ $\\text{F}$ đến $\\text{I}$?", "Tính oxi hóa của đơn chất $\\text{X}_2$ giảm dần, tính acid của dung dịch $\\text{HX}$ tăng dần", ["Tính oxi hóa của đơn chất $\\text{X}_2$ giảm dần, tính acid của dung dịch $\\text{HX}$ tăng dần", "Tính oxi hóa của đơn chất $\\text{X}_2$ tăng dần, tính acid của dung dịch $\\text{HX}$ giảm dần", "Cả tính oxi hóa của $\\text{X}_2$ và tính acid của $\\text{HX}$ đều tăng dần", "Cả tính oxi hóa của $\\text{X}_2$ và tính acid của $\\text{HX}$ đều giảm dần"], "Đi từ $\\text{F}$ đến $\\text{I}$: tính oxi hóa của $\\text{X}_2$ giảm dần, còn tính acid của $\\text{HX}$ và tính khử của $\\text{X}^-$ tăng dần.", "biet"),
            mcq("Sục khí $\\text{Cl}_2$ dư vào dung dịch chứa hỗn hợp $\\text{NaBr}$ và $\\text{NaI}$, sau đó cô cạn dung dịch và nung đến khối lượng không đổi thì chất rắn duy nhất còn lại là:", "$\\text{NaCl}$", ["$\\text{NaCl}$", "$\\text{NaBr}$", "$\\text{NaI}$", "Hỗn hợp $\\text{NaCl}, \\text{NaBr}, \\text{NaI}$"], "$\\text{Cl}_2$ đẩy hết $\\text{Br}_2$ và $\\text{I}_2$ ra khỏi muối tạo $\\text{NaCl}$; khi cô cạn và nung thì $\\text{Br}_2$, $\\text{I}_2$ bay hơi hết chỉ còn lại $\\text{NaCl}$.", "hieu"),
            short("Cho $10\\text{ g}$ hỗn hợp bột gồm $\\text{Mg}$ và $\\text{Fe}$ tác dụng hết với dung dịch $\\text{HCl}$ dư thu được $0,3\\text{ mol}$ khí $\\text{H}_2$. Tính khối lượng muối chloride khan thu được sau khi cô cạn dung dịch (theo đơn vị gam).", "31,3", ["31,3", "31.3"], "Áp dụng công thức: $m_{\\text{muối}} = m_{\\text{KL}} + 71 \\cdot n_{\\text{H}_2} = 10 + 71 \\cdot 0,3 = 31,3\\text{ g}$.", "vandung"),
        ]
    ),
]

LESSONS = (
    CH1_LESSONS + CH2_LESSONS + CH3_LESSONS + CH4_LESSONS
    + CH5_LESSONS + CH6_LESSONS + CH7_LESSONS
)
