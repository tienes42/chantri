"""Hóa học Lớp 7 (KHTN 7 - Kết nối tri thức với cuộc sống): 3 Chương - 10 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 7

CH1 = ("l7-ch01-nguyen-tu-bang-tuan-hoan", "Chương I: Nguyên tử và Sơ lược về bảng tuần hoàn các nguyên tố hóa học", "Chương I · Hóa học 7 (KHTN 7): Cấu tạo nguyên tử, nguyên tố hóa học và cấu trúc bảng tuần hoàn.")
CH2 = ("l7-ch02-phan-tu-don-chat-hop-chat", "Chương II: Phân tử – Đơn chất và Hợp chất", "Chương II · Hóa học 7 (KHTN 7): Phân tử, đơn chất, hợp chất và cách tính khối lượng phân tử theo amu.")
CH3 = ("l7-ch03-lien-ket-hoa-tri-cthh", "Chương III: Liên kết hóa học, Hóa trị và Công thức hóa học", "Chương III · Hóa học 7 (KHTN 7): Liên kết ion, liên kết cộng hóa trị, quy tắc hóa trị và lập công thức hóa học.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Nguyên tử",
        icon="⚛️",
        description="Mô hình nguyên tử Rutherford – Bohr, thành phần hạt nhân (proton, neutron) và vỏ electron, sự trung hòa điện và khối lượng nguyên tử (amu).",
        requirements=[
            "Trình bày được mô hình nguyên tử của Rutherford – Bohr: nguyên tử gồm hạt nhân mang điện tích dương ở tâm và các electron mang điện tích âm chuyển động xung quanh theo từng lớp.",
            "Nêu được điện tích và khối lượng (theo đơn vị $\\text{amu}$) của $3$ loại hạt cơ bản: proton ($p: +1, \\approx 1\\text{ amu}$), neutron ($n: 0, \\approx 1\\text{ amu}$), electron ($e: -1, \\approx 0{,}00055\\text{ amu} \\ll 1\\text{ amu}$).",
            "Vận dụng được tính trung hòa về điện của nguyên tử (số hạt $p = \\text{số hạt } e = Z$) và tính khối lượng nguyên tử xấp xỉ bằng khối lượng hạt nhân ($m_{\\text{nt}} \\approx p + n$ theo $\\text{amu}$).",
        ],
        definition="Nguyên tử là hạt vô cùng nhỏ và trung hòa về điện, cấu tạo nên các chất. Nguyên tử gồm hạt nhân mang điện tích dương ở tâm (chứa các hạt proton và neutron) và lớp vỏ tạo bởi một hay nhiều electron mang điện tích âm chuyển động xung quanh hạt nhân.",
        theory=(
            "### 1. Cấu tạo nguyên tử và Mô hình Rutherford – Bohr\n"
            "- **Thành phần nguyên tử**:\n"
            "  1. **Hạt nhân (ở tâm)**: gồm hạt **proton ($p$)** mang điện tích dương ($+1$ đơn vị điện tích nguyên tố) và hạt **neutron ($n$)** không mang điện ($0$). *(Riêng nguyên tử hydrogen thông thường $^1_1\\text{H}$ hạt nhân chỉ có $1$ proton, không có neutron)*.\n"
            "  2. **Lớp vỏ nguyên tử**: gồm các hạt **electron ($e$)** mang điện tích âm ($-1$).\n"
            "- **Sự trung hòa điện của nguyên tử**: Trong mọi nguyên tử, **số hạt proton luôn bằng số hạt electron** ($p = e = Z$): nếu hạt nhân có điện tích $+Z$ thì có đúng $Z$ proton và $Z$ electron.\n"
            "- **Mô hình Rutherford – Bohr**: Các electron chuyển động xung quanh hạt nhân theo những quỹ đạo tròn (các lớp electron) từ trong ra ngoài: **lớp thứ nhất (trong cùng)** chứa tối đa **$2$ electron**; **lớp thứ hai** chứa tối đa **$8$ electron**.\n\n"
            "### 2. Khối lượng của nguyên tử (Đơn vị amu)\n"
            "- Khối lượng của $1$ proton $\\approx 1\\text{ amu}$, của $1$ neutron $\\approx 1\\text{ amu}$; còn khối lượng của $1$ electron cực kì nhỏ ($\\approx 0{,}00055\\text{ amu}$, chỉ bằng $\\dfrac{1}{1840}$ khối lượng proton).\n"
            "- Do đó **khối lượng của nguyên tử tập trung hầu hết ở hạt nhân**: $m_{\\text{nguyên tử}} \\approx m_{\\text{hạt nhân}} \\approx (p + n)\\text{ amu}$."
        ),
        formulas=[
            G(
                "Các hệ thức cấu tạo và khối lượng nguyên tử",
                F("Điều kiện trung hòa điện và Tổng số hạt của nguyên tử", "$p = e = Z; \\qquad \\text{Tổng số hạt } S = p + n + e = 2p + n$", "Số đơn vị điện tích hạt nhân $Z$ bằng số hạt proton $p$ và bằng số hạt electron $e$."),
                F("Khối lượng nguyên tử theo đơn vị amu và Tối đa electron mỗi lớp", "$m_{\\text{nt}} \\approx (p + n)\\text{ amu}; \\qquad \\text{Lớp 1 tối đa } 2e,\\ \\text{Lớp 2 tối đa } 8e$", "Ví dụ: Nguyên tử oxygen ($Z = 8$) có $8e$ phân bố vào 2 lớp: lớp 1 có $2e$, lớp 2 (ngoài cùng) có $6e$."),
            )
        ],
        example="Nguyên tử nhôm (Aluminium – $\\text{Al}$) có điện tích hạt nhân là $+13$ và trong hạt nhân có $14$ hạt neutron. Hãy xác định số hạt proton, số hạt electron, số electron ở lớp ngoài cùng (theo mô hình Bohr) và khối lượng nguyên tử nhôm theo đơn vị $\\text{amu}$.",
        example_answer="Vì điện tích hạt nhân là $+13$ và nguyên tử trung hòa về điện nên số hạt proton bằng số hạt electron: $p = e = 13$ hạt. Phân bố $13$ electron vào các lớp từ trong ra ngoài: lớp 1 có $2e$, lớp 2 có $8e$, còn lại lớp 3 (ngoài cùng) có $13 - 2 - 8 = 3$ electron. Khối lượng nguyên tử nhôm là $m_{\\text{Al}} \\approx p + n = 13 + 14 = 27\\text{ amu}$.",
        real_life="Nhờ hiểu rõ cấu tạo nguyên tử và sự chuyển dịch của các electron lớp ngoài cùng, các nhà khoa học giải thích được vì sao kim loại dẫn điện tốt và vì sao các nguyên tử liên kết với nhau tạo ra hàng triệu chất.",
        quiz=[
            mcq("biet", "Trong nguyên tử, loại hạt nào mang **điện tích âm** và chuyển động xung quanh hạt nhân?", ["Hạt electron ($e$)", "Hạt proton ($p$)", "Hạt neutron ($n$)", "Hạt nhân nguyên tử"], 0, "Electron ($e$) mang điện tích âm ($-1$) tạo nên lớp vỏ nguyên tử; còn proton ($+1$) và neutron ($0$) nằm trong hạt nhân."),
            mcq("biet", "Vì sao nguyên tử luôn **trung hòa về điện**?", ["Vì trong nguyên tử, số hạt proton (mang điện $+1$) luôn bằng số hạt electron (mang điện $-1$)", "Vì trong nguyên tử chỉ toàn các hạt neutron không mang điện", "Vì số hạt proton luôn bằng số hạt neutron", "Vì các electron đứng yên trong hạt nhân"], 0, "Mỗi proton mang điện $+1$, mỗi electron mang điện $-1$; vì số proton bằng số electron ($p = e$) nên tổng điện tích của nguyên tử bằng $0$."),
            mcq("hieu", "Vì sao khối lượng của nguyên tử được coi là gần bằng khối lượng của hạt nhân nguyên tử ($m_{\\text{nt}} \\approx p + n$ theo $\\text{amu}$)?", ["Vì khối lượng của các electron ở lớp vỏ quá nhỏ ($\\approx 0{,}00055\\text{ amu}$), không đáng kể so với khối lượng của proton và neutron ($\\approx 1\\text{ amu}$)", "Vì nguyên tử không có lớp vỏ electron", "Vì hạt neutron không có khối lượng", "Vì khối lượng electron lớn gấp $1000$ lần proton"], 0, "Khối lượng 1 electron chỉ bằng khoảng $0{,}00055\\text{ amu}$, rất nhỏ so với $1\\text{ amu}$ của proton và neutron nên khối lượng nguyên tử tập trung ở hạt nhân."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cấu tạo nguyên tử:", [
                "Hạt nhân nguyên tử được cấu tạo bởi các hạt proton và neutron (trừ nguyên tử $^1_1\\text{H}$ không có neutron).",
                "Theo mô hình Rutherford – Bohr, lớp electron thứ nhất (sát hạt nhân nhất) chứa tối đa $2$ electron và lớp thứ hai chứa tối đa $8$ electron.",
                "Một nguyên tử carbon có $6$ proton và $6$ neutron thì có $12$ electron ở lớp vỏ.",
                "Một nguyên tử sodium ($\\text{Na}$) có $11$ proton và $12$ neutron thì có khối lượng nguyên tử xấp xỉ bằng $23\\text{ amu}$.",
            ], [True, True, False, True], "Ý c) sai vì nguyên tử carbon có $6$ proton nên chỉ có $e = p = 6$ electron ở lớp vỏ (còn $6 + 6 = 12\\text{ amu}$ là khối lượng nguyên tử)."),
            short("vandung", "Một nguyên tử nitrogen ($\\text{N}$) có $7$ hạt proton và $7$ hạt neutron trong hạt nhân. Tổng số hạt cơ bản ($p + n + e$) trong nguyên tử nitrogen này bằng bao nhiêu hạt?", ["21"], "Vì nguyên tử trung hòa điện nên $e = p = 7$. Tổng số hạt trong nguyên tử là $S = p + n + e = 7 + 7 + 7 = 21$ hạt.", unit="hạt"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Nguyên tố hóa học",
        icon="🏷️",
        description="Định nghĩa nguyên tố hóa học (tập hợp các nguyên tử có cùng số proton), kí hiệu hóa học và tên gọi chuẩn IUPAC của 20 nguyên tố đầu tiên.",
        requirements=[
            "Định nghĩa được nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có **cùng số proton trong hạt nhân**.",
            "Nêu được các nguyên tử của cùng một nguyên tố hóa học đều có tính chất hóa học giống nhau.",
            "Viết đúng kí hiệu hóa học (gồm 1 hoặc 2 chữ cái, chữ cái đầu viết in hoa) và đọc tên chuẩn IUPAC của 20 nguyên tố đầu tiên ($\\text{H}, \\text{He}, \\text{Li}, \\text{Be}, \\text{B}, \\text{C}, \\text{N}, \\text{O}, \\text{F}, \\text{Ne}, \\text{Na}, \\text{Mg}, \\text{Al}, \\text{Si}, \\text{P}, \\text{S}, \\text{Cl}, \\text{Ar}, \\text{K}, \\text{Ca}$) cùng một số nguyên tố phổ biến ($\\text{Fe}, \\text{Cu}, \\text{Zn}, \\text{Ag}$).",
        ],
        definition="Nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có cùng số hạt proton trong hạt nhân. Số proton trong hạt nhân chính là số hiệu nguyên tử ($Z$), là đặc trưng cơ bản quyết định một nguyên tử thuộc nguyên tố hóa học nào.",
        theory=(
            "### 1. Khái niệm Nguyên tố hóa học\n"
            "- Các nguyên tử có **cùng số hạt proton ($p = Z$)** trong hạt nhân đều thuộc về **cùng một nguyên tố hóa học** (dù số hạt neutron của chúng có thể khác nhau).\n"
            "- Các nguyên tử thuộc cùng một nguyên tố hóa học có cùng số electron nên có **tính chất hóa học giống nhau**.\n"
            "- Hiện nay các nhà khoa học đã biết $118$ nguyên tố hóa học ($98$ nguyên tố có trong tự nhiên và các nguyên tố nhân tạo). Trong vỏ Trái Đất, nguyên tố phổ biến nhất theo khối lượng là **Oxygen ($\\text{O}, \\approx 46{,}6\\%$)**, tiếp theo là Silicon ($\\text{Si}$), Aluminium ($\\text{Al}$), Iron ($\\text{Fe}$)...\n\n"
            "### 2. Kí hiệu hóa học và Tên gọi theo danh pháp IUPAC\n"
            "- **Quy tắc viết kí hiệu hóa học**: biểu diễn bằng $1$ hoặc $2$ chữ cái lấy từ tên Latinh của nguyên tố; **chữ cái đầu tiên luôn viết IN HOA**, chữ cái thứ hai (nếu có) luôn viết **chữ thường**.\n"
            "- **Các nguyên tố tiêu biểu cần nhớ (Tên IUPAC – Kí hiệu – Khối lượng nguyên tử amu)**:\n"
            "  - $\\text{H}$ (Hydrogen: $1$), $\\text{He}$ (Helium: $4$), $\\text{C}$ (Carbon: $12$), $\\text{N}$ (Nitrogen: $14$), $\\text{O}$ (Oxygen: $16$).\n"
            "  - $\\text{Na}$ (Sodium: $23$), $\\text{Mg}$ (Magnesium: $24$), $\\text{Al}$ (Aluminium: $27$), $\\text{Si}$ (Silicon: $28$), $\\text{P}$ (Phosphorus: $31$), $\\text{S}$ (Sulfur: $32$), $\\text{Cl}$ (Chlorine: $35{,}5$).\n"
            "  - $\\text{K}$ (Potassium: $39$), $\\text{Ca}$ (Calcium: $40$), $\\text{Fe}$ (Iron: $56$), $\\text{Cu}$ (Copper: $64$), $\\text{Zn}$ (Zinc: $65$), $\\text{Ag}$ (Silver: $108$), $\\text{Ba}$ (Barium: $137$)."
        ),
        formulas=[
            G(
                "Quy tắc xác định Nguyên tố hóa học và Kí hiệu hóa học",
                F("Tiêu chuẩn duy nhất xác định cùng một nguyên tố hóa học", "$\\text{Cùng nguyên tố hóa học} \\iff \\text{Cùng số hạt proton } p \\text{ trong hạt nhân } (p_1 = p_2 = Z)$", "Ví dụ: Ba nguyên tử có cùng $p = 8$ (nhưng có $n = 8, 9, 10$) đều thuộc cùng 1 nguyên tố là Oxygen ($\\text{O}$)."),
                F("Ý nghĩa của kí hiệu hóa học (ví dụ Na, Ca, Fe)", "$1\\text{ kí hiệu } X \\implies \\text{Biểu diễn nguyên tố } X \\text{ và } 1 \\text{ nguyên tử của nguyên tố đó}$", "Muốn biểu diễn $k$ nguyên tử riêng rẽ, ta viết hệ số $k$ phía trước kí hiệu: ví dụ $3\\text{Fe}$ là $3$ nguyên tử iron (sắt)."),
            )
        ],
        example="Cho 4 nguyên tử có thành phần hạt nhân như sau: Nguyên tử $A$ ($6p, 6n$), nguyên tử $B$ ($7p, 7n$), nguyên tử $C$ ($6p, 8n$) và nguyên tử $D$ ($8p, 8n$). Hỏi những nguyên tử nào thuộc cùng một nguyên tố hóa học? Đó là nguyên tố nào?",
        example_answer="Hai nguyên tử **$A$ và $C$** có **cùng số hạt proton trong hạt nhân ($p = 6$)** nên thuộc **cùng một nguyên tố hóa học** (đó là nguyên tố Carbon, kí hiệu $\\text{C}$). Như vậy 4 nguyên tử trên thuộc về $3$ nguyên tố hóa học khác nhau ($Z = 6, 7, 8$).",
        real_life="Trên nhãn hộp sữa và thực phẩm bổ sung luôn in kí hiệu các nguyên tố khoáng thiết yếu như $\\text{Ca}$ (Calcium giúp xương và răng chắc khỏe), $\\text{Fe}$ (Iron tạo máu), $\\text{Zn}$ (Zinc tăng miễn dịch) và $\\text{I}$ (Iodine phòng bướu cổ).",
        quiz=[
            mcq("biet", "Các nguyên tử thuộc **cùng một nguyên tố hóa học** là những nguyên tử có cùng đại lượng nào sau đây?", ["Có cùng số hạt proton trong hạt nhân", "Có cùng số hạt neutron trong hạt nhân", "Có cùng tổng số hạt $p + n$", "Có cùng kích thước bình chứa"], 0, "Nguyên tố hóa học là tập hợp những nguyên tử cùng loại có cùng số hạt proton trong hạt nhân."),
            mcq("biet", "Theo danh pháp quốc tế IUPAC trong SGK Kết nối tri thức, các nguyên tố có tên gọi **Sodium, Potassium, Copper, Iron** lần lượt có kí hiệu hóa học là gì?", ["$\\text{Na}, \\text{K}, \\text{Cu}, \\text{Fe}$", "$\\text{S}, \\text{P}, \\text{Co}, \\text{I}$", "$\\text{Na}, \\text{Ca}, \\text{Cu}, \\text{Zn}$", "$\\text{Mg}, \\text{K}, \\text{C}, \\text{Fe}$"], 0, "Sodium là $\\text{Na}$ (Natri), Potassium là $\\text{K}$ (Kali), Copper là $\\text{Cu}$ (Đồng) và Iron là $\\text{Fe}$ (Sắt)."),
            mcq("hieu", "Cách viết kí hiệu hóa học của nguyên tố Aluminium (Nhôm) và Chlorine (Clo) nào sau đây là **đúng** quy ước quốc tế?", ["$\\text{Al}$ và $\\text{Cl}$ (chữ cái đầu viết in hoa, chữ cái thứ hai viết thường)", "$\\text{AL}$ và $\\text{CL}$", "$\\text{al}$ và $\\text{cl}$", "$\\text{aL}$ và $\\text{cL}$"], 0, "Trong kí hiệu hóa học gồm 2 chữ cái, chữ cái đầu tiên bắt buộc viết in hoa và chữ cái thứ hai bắt buộc viết thường: $\\text{Al}, \\text{Cl}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nguyên tố hóa học:", [
                "Các nguyên tử thuộc cùng một nguyên tố hóa học đều có tính chất hóa học giống nhau.",
                "Cách viết $5\\text{Ca}$ dùng để chỉ $5$ nguyên tử calcium riêng rẽ.",
                "Hai nguyên tử có cùng số hạt neutron là $7$ (ví dụ nguyên tử $X$ có $6p, 7n$ và nguyên tử $Y$ có $7p, 7n$) thì thuộc cùng một nguyên tố hóa học.",
                "Nguyên tố chiếm tỉ lệ khối lượng lớn nhất trong vỏ Trái Đất là Oxygen ($\\text{O}$).",
            ], [True, True, False, True], "Ý c) sai vì $X$ có $6$ proton (là $\\text{C}$) còn $Y$ có $7$ proton (là $\\text{N}$); khác số proton nên chúng thuộc hai nguyên tố hóa học khác nhau."),
            short("vandung", "Cho 4 nguyên tử có cấu tạo hạt nhân lần lượt là: $X_1(8p, 8n)$, $X_2(8p, 9n)$, $X_3(8p, 10n)$ và $X_4(9p, 10n)$. Trong 4 nguyên tử trên, có bao nhiêu nguyên tử thuộc về nguyên tố Oxygen ($Z = 8$)?", ["3"], "Các nguyên tử $X_1, X_2, X_3$ đều có cùng số proton $p = 8$ nên có $3$ nguyên tử thuộc nguyên tố Oxygen."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 3: Cấu trúc bảng tuần hoàn các nguyên tố hóa học",
        icon="📅",
        description="Nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn (theo chiều tăng điện tích hạt nhân Z) và cấu tạo bảng tuần hoàn (ô nguyên tố, chu kì, nhóm).",
        requirements=[
            "Nêu được nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn: theo chiều tăng dần của điện tích hạt nhân nguyên tử (số hiệu nguyên tử $Z$).",
            "Đọc được các thông tin trong một **ô nguyên tố** (số hiệu nguyên tử $Z$, kí hiệu hóa học, tên nguyên tố, khối lượng nguyên tử).",
            "Vận dụng được mối liên hệ giữa cấu tạo nguyên tử và vị trí trong bảng tuần hoàn (đối với 20 nguyên tố đầu): $\\text{Số thứ tự ô} = Z = p = e$; $\\text{Số thứ tự chu kì} = \\text{Số lớp electron}$; $\\text{Số thứ tự nhóm A} = \\text{Số electron lớp ngoài cùng}$.",
        ],
        definition="Bảng tuần hoàn các nguyên tố hóa học (do Dmitri Mendeleev phát minh năm 1869) sắp xếp các nguyên tố theo chiều tăng dần của điện tích hạt nhân nguyên tử. Cấu trúc bảng tuần hoàn gồm các ô nguyên tố, các hàng ngang gọi là chu kì ($7$ chu kì) và các cột dọc gọi là nhóm ($8$ nhóm A và $8$ nhóm B).",
        theory=(
            "### 1. Nguyên tắc sắp xếp của Bảng tuần hoàn\n"
            "1. Các nguyên tố được sắp xếp theo **chiều tăng dần của điện tích hạt nhân nguyên tử ($Z$)**.\n"
            "2. Các nguyên tố có **cùng số lớp electron** trong nguyên tử được xếp vào cùng một hàng ngang gọi là **chu kì**.\n"
            "3. Các nguyên tố có **số electron lớp ngoài cùng giống nhau** (nên có tính chất hóa học tương tự nhau) được xếp vào cùng một cột dọc gọi là **nhóm**.\n\n"
            "### 2. Ô nguyên tố – Chu kì – Nhóm\n"
            "- **Ô nguyên tố**: Số thứ tự của ô nguyên tố bằng **số hiệu nguyên tử $Z$** ($= \\text{số } p = \\text{số } e$). Ngoài ra trong ô còn ghi kí hiệu hóa học, tên nguyên tố và khối lượng nguyên tử trung bình.\n"
            "- **Chu kì (hàng ngang)**: Bảng tuần hoàn hiện có **$7$ chu kì** (chu kì $1, 2, 3$ là các *chu kì nhỏ*; chu kì $4, 5, 6, 7$ là các *chu kì lớn*).\n"
            "  $$\\text{Số thứ tự của chu kì} = \\text{Số lớp electron của nguyên tử}$$\n"
            "- **Nhóm (cột dọc)**: Gồm $8$ nhóm A (từ $\\text{IA}$ đến $\\text{VIIIA}$) và $8$ nhóm B (từ $\\text{IB}$ đến $\\text{VIIIB}$). Đối với các nguyên tố nhóm A:\n"
            "  $$\\text{Số thứ tự của nhóm A (chữ số La Mã)} = \\text{Số electron ở lớp ngoài cùng}$$"
        ),
        formulas=[
            G(
                "Liên hệ giữa Cấu tạo nguyên tử và Vị trí trong Bảng tuần hoàn",
                F("Quy tắc 3 dấu bằng vàng cho nguyên tố nhóm A", "$\\begin{cases} \\text{Số thứ tự ô nguyên tố} = Z = p = e \\\\ \\text{Số thứ tự Chu kì (hàng ngang)} = \\text{Số lớp electron} \\\\ \\text{Số thứ tự Nhóm A (cột dọc)} = \\text{Số electron lớp ngoài cùng} \\end{cases}$", "Ngoại lệ duy nhất: Nguyên tử Helium ($\\text{He}, Z = 2$) chỉ có $1$ lớp chứa $2e$ đã bão hòa nên được xếp vào nhóm khí hiếm $\\text{VIIIA}$."),
                F("Số nguyên tố trong các chu kì nhỏ", "$\\text{Chu kì 1}: 2\\text{ nguyên tố } (\\text{H}, \\text{He}); \\quad \\text{Chu kì 2}: 8\\text{ nguyên tố } (Z = 3..10); \\quad \\text{Chu kì 3}: 8\\text{ nguyên tố } (Z = 11..18)$", "Bảng tuần hoàn có tổng cộng $7$ chu kì."),
            )
        ],
        example="Nguyên tử của nguyên tố Magnesium ($\\text{Mg}$) có điện tích hạt nhân là $+12$, có $12$ electron được phân bố trên $3$ lớp electron (lớp thứ nhất có $2e$, lớp thứ hai có $8e$, lớp thứ ba ngoài cùng có $2e$). Hãy xác định vị trí (ô thứ mấy, chu kì mấy, nhóm nào) của nguyên tố $\\text{Mg}$ trong bảng tuần hoàn.",
        example_answer="- Vì $Z = p = e = 12$ nên $\\text{Mg}$ nằm ở **ô nguyên tố số $12$**.\n- Vì nguyên tử có $3$ lớp electron nên $\\text{Mg}$ thuộc **chu kì $3$**.\n- Vì lớp ngoài cùng có $2$ electron nên $\\text{Mg}$ thuộc **nhóm $\\text{IIA}$**.",
        real_life="Bảng tuần hoàn được ví như 'tấm bản đồ vĩ đại của Hóa học': chỉ cần nhìn vị trí ô, chu kì và nhóm của một nguyên tố bất kì, ta biết ngay cấu tạo nguyên tử và dự đoán được tính chất của nó.",
        quiz=[
            mcq("biet", "Trong bảng tuần hoàn hiện đại, các nguyên tố hóa học được sắp xếp theo nguyên tắc cơ bản nào?", ["Theo chiều tăng dần của điện tích hạt nhân nguyên tử (số hiệu nguyên tử $Z$)", "Theo thứ tự bảng chữ cái A, B, C của tên nguyên tố", "Theo thời gian nguyên tố được tìm ra sớm hay muộn", "Theo độ cứng của đơn chất tăng dần"], 0, "Các nguyên tố trong bảng tuần hoàn được sắp xếp theo chiều tăng dần của điện tích hạt nhân nguyên tử."),
            mcq("biet", "Các nguyên tố hóa học nằm trong cùng một **chu kì** (cùng một hàng ngang) trong bảng tuần hoàn có đặc điểm chung nào về cấu tạo nguyên tử?", ["Có cùng số lớp electron trong nguyên tử", "Có cùng số electron ở lớp ngoài cùng", "Có cùng số hạt proton trong hạt nhân", "Có cùng số hạt neutron trong hạt nhân"], 0, "Chu kì là dãy các nguyên tố mà nguyên tử của chúng có cùng số lớp electron (số thứ tự chu kì bằng số lớp electron)."),
            mcq("hieu", "Nguyên tố Sulfur ($\\text{S}$) nằm ở **ô số $16$, chu kì $3$, nhóm $\\text{VIA}$** trong bảng tuần hoàn. Phát biểu nào sau đây về cấu tạo nguyên tử $\\text{S}$ là **đúng**?", ["Nguyên tử $\\text{S}$ có $16$ proton, $3$ lớp electron và có $6$ electron ở lớp ngoài cùng", "Nguyên tử $\\text{S}$ có $16$ proton, $6$ lớp electron và $3$ electron ở lớp ngoài cùng", "Nguyên tử $\\text{S}$ có $3$ proton và $6$ electron", "Nguyên tử $\\text{S}$ có $6$ proton và $16$ lớp electron"], 0, "Ô số $16 \\implies p = e = 16$; chu kì $3 \\implies 3$ lớp electron; nhóm $\\text{VIA} \\implies 6$ electron ở lớp ngoài cùng ($2, 8, 6$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cấu trúc bảng tuần hoàn:", [
                "Bảng tuần hoàn hiện nay gồm có $7$ chu kì (trong đó chu kì $1, 2, 3$ là các chu kì nhỏ).",
                "Số thứ tự của ô nguyên tố luôn bằng số hiệu nguyên tử $Z$ (bằng số proton và bằng số electron trong nguyên tử).",
                "Các nguyên tố trong cùng một nhóm A (cột dọc) có số electron lớp ngoài cùng bằng nhau nên có tính chất hóa học tương tự nhau.",
                "Chu kì $1$ của bảng tuần hoàn chứa tới $8$ nguyên tố hóa học.",
            ], [True, True, True, False], "Ý d) sai vì chu kì $1$ chỉ gồm đúng $2$ nguyên tố là Hydrogen ($\\text{H}, Z = 1$) và Helium ($\\text{He}, Z = 2$)."),
            short("vandung", "Nguyên tử của nguyên tố Chlorine ($\\text{Cl}$) có $17$ electron phân bố trên $3$ lớp (lớp 1 có $2e$, lớp 2 có $8e$, lớp 3 ngoài cùng có $7e$). Nguyên tố Chlorine nằm ở chu kì thứ mấy trong bảng tuần hoàn?", ["3"], "Vì nguyên tử $\\text{Cl}$ có $3$ lớp electron nên thuộc chu kì $3$."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 4: Nguyên tố kim loại, phi kim và khí hiếm trong bảng tuần hoàn",
        icon="💎",
        description="Vị trí và đặc điểm của các nhóm nguyên tố kim loại (IA, IIA, IIIA, nhóm B), nguyên tố phi kim (VA, VIA, VIIA) và nguyên tố khí hiếm (VIIIA).",
        requirements=[
            "Xác định được vị trí của các nguyên tố kim loại (chiếm hơn $80\\%$ số nguyên tố, nằm ở phía bên trái và phía dưới bảng tuần hoàn: nhóm $\\text{IA}, \\text{IIA}, \\text{IIIA}$ và các nhóm $\\text{B}$).",
            "Xác định được vị trí của các nguyên tố phi kim (nằm ở phía trên bên phải bảng tuần hoàn: phần lớn nhóm $\\text{VA}, \\text{VIA}, \\text{VIIA}$ và $\\text{H}$ ở nhóm $\\text{IA}$).",
            "Nêu được đặc điểm của các nguyên tố khí hiếm ở cột cuối cùng (nhóm $\\text{VIIIA}$: $\\text{He}, \\text{Ne}, \\text{Ar}$... có lớp vỏ ngoài cùng bền vững $8e$, riêng $\\text{He}$ có $2e$, hầu như không tham gia phản ứng hóa học).",
        ],
        definition="Trong bảng tuần hoàn, hơn $80\\%$ các nguyên tố là kim loại (nằm ở bên trái và phía dưới bảng); các nguyên tố phi kim nằm ở phía trên bên phải bảng (và $\\text{H}$ ở ô số 1); cột cuối cùng bên phải (nhóm $\\text{VIIIA}$) là các nguyên tố khí hiếm có lớp electron ngoài cùng đã bão hòa bền vững.",
        theory=(
            "### 1. Các nguyên tố Kim loại\n"
            "- Chiếm hơn $80\\%$ tổng số nguyên tố (hơn $90$ nguyên tố), nguyên tử thường có $1, 2$ hoặc $3$ electron ở lớp ngoài cùng.\n"
            "- **Vị trí**:\n"
            "  - **Nhóm $\\text{IA}$ (Kim loại kiềm, trừ $\\text{H}$)**: $\\text{Li}$ (Lithium), $\\text{Na}$ (Sodium), $\\text{K}$ (Potassium)... ($1e$ lớp ngoài cùng).\n"
            "  - **Nhóm $\\text{IIA}$ (Kim loại kiềm thổ)**: $\\text{Be}, \\text{Mg}$ (Magnesium), $\\text{Ca}$ (Calcium), $\\text{Ba}$ (Barium)... ($2e$ lớp ngoài cùng).\n"
            "  - **Nhóm $\\text{IIIA}$** (trừ $\\text{B}$): $\\text{Al}$ (Aluminium – $3e$ lớp ngoài cùng)...\n"
            "  - **Toàn bộ các nhóm $\\text{B}$ (Kim loại chuyển tiếp)**: $\\text{Fe}$ (Iron), $\\text{Cu}$ (Copper), $\\text{Zn}$ (Zinc), $\\text{Ag}$ (Silver), $\\text{Au}$ (Gold), $\\text{Hg}$ (Mercury – kim loại duy nhất ở thể lỏng ở điều kiện thường).\n\n"
            "### 2. Các nguyên tố Phi kim và Nguyên tố Khí hiếm\n"
            "- **Nguyên tố phi kim** (khoảng gần $20$ nguyên tố, nguyên tử thường có $5, 6, 7$ electron ở lớp ngoài cùng):\n"
            "  - Nằm ở góc phía trên bên phải bảng tuần hoàn: thuộc một phần nhóm $\\text{IIIA}$ ($\\text{B}$), $\\text{IVA}$ ($\\text{C}, \\text{Si}$), $\\text{VA}$ ($\\text{N}, \\text{P}$), $\\text{VIA}$ ($\\text{O}, \\text{S}$) và **nhóm $\\text{VIIA}$ (nhóm Halogen: $\\text{F}, \\text{Cl}, \\text{Br}, \\text{I}$)**, cùng với nguyên tố **Hydrogen ($\\text{H}$)** ở ô số 1 nhóm $\\text{IA}$.\n"
            "- **Nguyên tố khí hiếm (Nhóm $\\text{VIIIA}$ – cột 18 cuối cùng bên phải)**:\n"
            "  - Gồm $\\text{He}$ (Helium), $\\text{Ne}$ (Neon), $\\text{Ar}$ (Argon), $\\text{Kr}$ (Krypton), $\\text{Xe}$ (Xenon), $\\text{Rn}$ (Radon).\n"
            "  - Có lớp electron ngoài cùng bền vững tối đa (**$8$ electron**, riêng $\\text{He}$ có **$2$ electron**), nên ở điều kiện thường tồn tại dưới dạng nguyên tử đơn độc và **rất trơ về mặt hóa học**."
        ),
        formulas=[
            G(
                "Phân vùng Kim loại – Phi kim – Khí hiếm trong Bảng tuần hoàn",
                F("Dấu hiệu nhận biết theo số electron lớp ngoài cùng", "$1, 2, 3e \\text{ ngoài cùng} \\implies \\text{Kim loại (trừ H, He, B)}; \\quad 5, 6, 7e \\implies \\text{Phi kim}; \\quad 8e \\ (\\text{He: } 2e) \\implies \\text{Khí hiếm (VIIIA)}$", "Kim loại chiếm trên $80\\%$ tổng số nguyên tố trong bảng tuần hoàn."),
                F("Các nhóm nguyên tố tiêu biểu", "$\\text{Nhóm IA (trừ H)}: \\text{KL kiềm } (\\text{Li, Na, K}); \\quad \\text{Nhóm IIA}: \\text{KL kiềm thổ } (\\text{Mg, Ca}); \\quad \\text{Nhóm VIIA}: \\text{Halogen } (\\text{F, Cl, Br, I}); \\quad \\text{Nhóm VIIIA}: \\text{Khí hiếm } (\\text{He, Ne, Ar})$", "Thủy ngân (Mercury – $\\text{Hg}$) là kim loại duy nhất ở thể lỏng ở nhiệt độ phòng; Bromine ($\\text{Br}_2$) là phi kim duy nhất ở thể lỏng."),
            )
        ],
        example="Dựa vào cấu tạo vỏ nguyên tử và vị trí trong bảng tuần hoàn, hãy phân loại các nguyên tố sau thành 3 nhóm (Kim loại, Phi kim, Khí hiếm): Sodium ($\\text{Na}$, nhóm $\\text{IA}$), Oxygen ($\\text{O}$, nhóm $\\text{VIA}$), Neon ($\\text{Ne}$, nhóm $\\text{VIIIA}$), Iron ($\\text{Fe}$, nhóm $\\text{VIIIB}$), Chlorine ($\\text{Cl}$, nhóm $\\text{VIIA}$) và Argon ($\\text{Ar}$, nhóm $\\text{VIIIA}$).",
        example_answer="- **Nguyên tố kim loại**: Sodium ($\\text{Na}$) và Iron ($\\text{Fe}$).\n- **Nguyên tố phi kim**: Oxygen ($\\text{O}$) và Chlorine ($\\text{Cl}$).\n- **Nguyên tố khí hiếm**: Neon ($\\text{Ne}$) và Argon ($\\text{Ar}$).",
        real_life="Khí hiếm Helium ($\\text{He}$) rất nhẹ và không cháy nổ nên được bơm vào khinh khí cầu, bóng bay an toàn (thay cho khí $\\text{H}_2$ dễ nổ); khí hiếm Argon ($\\text{Ar}$) và Neon ($\\text{Ne}$) được bơm vào bóng đèn sợi đốt và đèn quảng cáo.",
        quiz=[
            mcq("biet", "Trong bảng tuần hoàn các nguyên tố hóa học, các nguyên tố **khí hiếm** (như $\\text{He}, \\text{Ne}, \\text{Ar}$) nằm ở nhóm nào?", ["Nhóm $\\text{VIIIA}$ (cột cuối cùng bên phải bảng tuần hoàn)", "Nhóm $\\text{IA}$ (cột đầu tiên bên trái)", "Nhóm $\\text{VIIA}$", "Các nhóm $\\text{B}$ ở giữa bảng"], 0, "Các nguyên tố khí hiếm nằm ở cột cuối cùng bên phải của bảng tuần hoàn, tức nhóm $\\text{VIIIA}$ (nhóm 18)."),
            mcq("biet", "Loại nguyên tố nào chiếm tỉ lệ lớn nhất (trên $80\\%$ tổng số nguyên tố) trong bảng tuần hoàn các nguyên tố hóa học?", ["Các nguyên tố kim loại", "Các nguyên tố phi kim", "Các nguyên tố khí hiếm", "Các nguyên tố phóng xạ nhân tạo"], 0, "Hơn $80\\%$ các nguyên tố trong bảng tuần hoàn là nguyên tố kim loại (gồm hầu hết nhóm $\\text{IA}, \\text{IIA}, \\text{IIIA}$ và toàn bộ các nhóm $\\text{B}$)."),
            mcq("hieu", "Vì sao ở điều kiện thường, các nguyên tố khí hiếm (như Helium $\\text{He}$, Neon $\\text{Ne}$, Argon $\\text{Ar}$) lại tồn tại dưới dạng nguyên tử độc lập và hầu như không tham gia phản ứng hóa học?", ["Vì lớp electron ngoài cùng của nguyên tử khí hiếm đã đạt số lượng tối đa bền vững ($8$ electron, riêng $\\text{He}$ là $2$ electron)", "Vì hạt nhân của khí hiếm không có hạt proton", "Vì nguyên tử khí hiếm không có lớp vỏ electron", "Vì khí hiếm là các kim loại rất nặng"], 0, "Lớp electron ngoài cùng của khí hiếm đã bão hòa bền vững ($8e$, riêng $\\text{He}$ là $2e$) nên chúng rất trơ về mặt hóa học."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về kim loại, phi kim và khí hiếm trong bảng tuần hoàn:", [
                "Nguyên tố Hydrogen ($\\text{H}$, ô số 1) tuy xếp ở đầu nhóm $\\text{IA}$ nhưng là một nguyên tố phi kim.",
                "Tất cả các nguyên tố thuộc nhóm $\\text{B}$ (như $\\text{Fe}, \\text{Cu}, \\text{Zn}, \\text{Ag}, \\text{Au}$) đều là các nguyên tố kim loại.",
                "Các nguyên tố Oxygen ($\\text{O}$), Nitrogen ($\\text{N}$) và Chlorine ($\\text{Cl}$) là các nguyên tố kim loại điển hình.",
                "Kim loại Thủy ngân (Mercury – $\\text{Hg}$) là kim loại duy nhất tồn tại ở thể lỏng ở nhiệt độ phòng.",
            ], [True, True, False, True], "Ý c) sai vì Oxygen ($\\text{O}$), Nitrogen ($\\text{N}$) và Chlorine ($\\text{Cl}$) là các nguyên tố phi kim điển hình nằm ở góc trên bên phải bảng tuần hoàn."),
            short("vandung", "Trừ nguyên tử Helium ($\\text{He}$) có $2$ electron ở lớp ngoài cùng, nguyên tử của tất cả các nguyên tố khí hiếm còn lại ($\\text{Ne}, \\text{Ar}, \\text{Kr}, \\text{Xe}, \\text{Rn}$) trong nhóm $\\text{VIIIA}$ đều có bao nhiêu electron ở lớp ngoài cùng?", ["8"], "Các nguyên tử khí hiếm thuộc nhóm $\\text{VIIIA}$ (trừ $\\text{He}$) đều có $8$ electron ở lớp ngoài cùng."),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 5: Phân tử – Đơn chất – Hợp chất",
        icon="🧬",
        description="Khái niệm hạt phân tử, phân biệt đơn chất (tạo nên từ 1 nguyên tố hóa học) và hợp chất (tạo nên từ 2 nguyên tố hóa học trở lên).",
        requirements=[
            "Định nghĩa được phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.",
            "Phân biệt được **đơn chất** (chất được tạo nên từ **một** nguyên tố hóa học, như $\\text{O}_2, \\text{H}_2, \\text{N}_2, \\text{Cl}_2, \\text{Cu}, \\text{Fe}, \\text{C}$) và **hợp chất** (chất được tạo nên từ **hai hay nhiều** nguyên tố hóa học trở lên, như $\\text{H}_2\\text{O}, \\text{CO}_2, \\text{NaCl}, \\text{CH}_4$).",
            "Nhận biết được mô hình phân tử của một số đơn chất và hợp chất thông dụng.",
        ],
        definition="Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất. Đơn chất là những chất được tạo nên từ một nguyên tố hóa học. Hợp chất là những chất được tạo nên từ hai hay nhiều nguyên tố hóa học.",
        theory=(
            "### 1. Phân tử – Hạt đại diện cho chất\n"
            "- **Phân tử** là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và mang đầy đủ tính chất hóa học của chất đó:\n"
            "  - Phân tử gồm các nguyên tử của **cùng một nguyên tố** liên kết với nhau: $\\text{H}_2, \\text{O}_2, \\text{N}_2, \\text{Cl}_2, \\text{O}_3$ (ozone).\n"
            "  - Phân tử gồm các nguyên tử của **nhiều nguyên tố khác nhau** liên kết với nhau: nước ($\\text{H}_2\\text{O}$ gồm $2\\text{H} + 1\\text{O}$), carbon dioxide ($\\text{CO}_2$), ammonia ($\\text{NH}_3$), methane ($\\text{CH}_4$).\n"
            "  - *(Đối với khí hiếm như $\\text{He}, \\text{Ne}, \\text{Ar}$ hoặc kim loại như $\\text{Cu}, \\text{Fe}$, hạt đại diện cho chất là các nguyên tử)*.\n\n"
            "### 2. Phân biệt Đơn chất và Hợp chất\n"
            "- **Đơn chất**: chất được tạo nên từ **một nguyên tố hóa học** duy nhất:\n"
            "  - *Đơn chất kim loại*: $\\text{Fe}, \\text{Cu}, \\text{Al}, \\text{Na}, \\text{Mg}$ (dẫn điện, dẫn nhiệt, có ánh kim).\n"
            "  - *Đơn chất phi kim*: $\\text{H}_2, \\text{O}_2, \\text{N}_2, \\text{Cl}_2, \\text{C}$ (than chì, kim cương), $\\text{S}, \\text{P}$.\n"
            "  - *Đơn chất khí hiếm*: $\\text{He}, \\text{Ne}, \\text{Ar}$.\n"
            "- **Hợp chất**: chất được tạo nên từ **hai nguyên tố hóa học trở lên**:\n"
            "  - *Hợp chất vô cơ*: $\\text{H}_2\\text{O}, \\text{CO}_2, \\text{NaCl}, \\text{CaCO}_3, \\text{HCl}, \\text{H}_2\\text{SO}_4$.\n"
            "  - *Hợp chất hữu cơ*: methane ($\\text{CH}_4$), glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$), ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$)."
        ),
        formulas=[
            G(
                "Tiêu chuẩn phân biệt Đơn chất và Hợp chất",
                F("Quy tắc phân loại Đơn chất và Hợp chất", "$\\text{Chất tinh khiết} = \\begin{cases} \\text{ĐƠN CHẤT (chỉ tạo từ } 1 \\text{ nguyên tố: } \\text{O}_2, \\text{H}_2, \\text{N}_2, \\text{Cl}_2, \\text{O}_3, \\text{Fe}, \\text{Cu}, \\text{C}) \\\\ \\text{HỢP CHẤT (tạo từ } \\ge 2 \\text{ nguyên tố: } \\text{H}_2\\text{O}, \\text{CO}_2, \\text{NH}_3, \\text{NaCl}, \\text{CaCO}_3) \\end{cases}$", "Mẹo nhận biết nhanh từ công thức hóa học: chỉ có **1 kí hiệu nguyên tố** là Đơn chất; có **từ 2 kí hiệu nguyên tố trở lên** là Hợp chất!"),
                F("Lưu ý tránh nhầm lẫn giữa CO (Carbon monoxide) và Co (Cobalt)", "$\\text{CO (chữ O in hoa)}: \\text{Hợp chất của C và O}; \\qquad \\text{Co (chữ o thường)}: \\text{Đơn chất kim loại Cobalt}$", "Khí ozone ($\\text{O}_3$) dù có $3$ nguyên tử trong phân tử nhưng đều thuộc nguyên tố $\\text{O}$ nên vẫn là **đơn chất**!"),
            )
        ],
        example="Cho các chất có công thức hóa học sau: khí hydrogen ($\\text{H}_2$), nước ($\\text{H}_2\\text{O}$), kim loại đồng ($\\text{Cu}$), khí ozone ($\\text{O}_3$), muối ăn ($\\text{NaCl}$) và đá vôi ($\\text{CaCO}_3$). Hãy phân loại các chất trên thành hai nhóm: Đơn chất và Hợp chất.",
        example_answer="- **Đơn chất** (tạo nên từ $1$ nguyên tố hóa học): khí hydrogen ($\\text{H}_2$), kim loại đồng ($\\text{Cu}$) và khí ozone ($\\text{O}_3$).\n- **Hợp chất** (tạo nên từ $2$ nguyên tố hóa học trở lên): nước ($\\text{H}_2\\text{O}$ gồm $\\text{H}, \\text{O}$), muối ăn ($\\text{NaCl}$ gồm $\\text{Na}, \\text{Cl}$) và đá vôi ($\\text{CaCO}_3$ gồm $\\text{Ca}, \\text{C}, \\text{O}$).",
        real_life="Than chì làm ruột bút chì và kim cương làm đồ trang sức tuy có vẻ ngoài và độ cứng khác hẳn nhau nhưng đều là các **đơn chất** được tạo nên từ một nguyên tố duy nhất là Carbon ($\\text{C}$).",
        quiz=[
            mcq("biet", "Đơn chất là những chất được tạo nên từ bao nhiêu nguyên tố hóa học?", ["Từ $1$ nguyên tố hóa học duy nhất", "Từ $2$ nguyên tố hóa học trở lên", "Từ ít nhất $3$ nguyên tố hóa học", "Từ hỗn hợp nhiều chất trộn lẫn"], 0, "Đơn chất là những chất được tạo nên từ một nguyên tố hóa học."),
            mcq("biet", "Dãy các chất nào sau đây đều là **hợp chất**?", ["$\\text{H}_2\\text{O}, \\text{CO}_2, \\text{NaCl}, \\text{NH}_3$", "$\\text{O}_2, \\text{H}_2, \\text{N}_2, \\text{Cl}_2$", "$\\text{Fe}, \\text{Cu}, \\text{Al}, \\text{Zn}$", "$\\text{O}_3, \\text{H}_2\\text{O}, \\text{He}$"], 0, "Các chất $\\text{H}_2\\text{O}, \\text{CO}_2, \\text{NaCl}, \\text{NH}_3$ đều được tạo nên từ $2$ nguyên tố hóa học khác nhau nên đều là hợp chất."),
            mcq("hieu", "Khí ozone có công thức phân tử là $\\text{O}_3$ (mỗi phân tử gồm $3$ nguyên tử oxygen liên kết với nhau). Khí ozone thuộc loại chất nào?", ["Đơn chất phi kim (vì chỉ được tạo nên từ một nguyên tố duy nhất là Oxygen)", "Hợp chất vì có tới $3$ nguyên tử", "Đơn chất kim loại", "Hỗn hợp khí"], 0, "Dù phân tử $\\text{O}_3$ có $3$ nguyên tử nhưng cả $3$ nguyên tử đều thuộc cùng một nguyên tố Oxygen ($\\text{O}$), nên ozone là đơn chất."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phân tử, đơn chất và hợp chất:", [
                "Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.",
                "Phân tử khí nitrogen ($\\text{N}_2$), khí oxygen ($\\text{O}_2$) và khí chlorine ($\\text{Cl}_2$) đều là các phân tử đơn chất gồm $2$ nguyên tử.",
                "Kim cương và than chì đều được tạo nên từ nguyên tố Carbon ($\\text{C}$) nên chúng là các hợp chất.",
                "Mỗi phân tử methane ($\\text{CH}_4$) gồm $1$ nguyên tử carbon liên kết với $4$ nguyên tử hydrogen (tổng cộng $5$ nguyên tử).",
            ], [True, True, False, True], "Ý c) sai vì kim cương và than chì chỉ tạo nên từ một nguyên tố duy nhất là Carbon ($\\text{C}$) nên cả hai đều là **đơn chất**."),
            short("vandung", "Cho 6 chất có công thức hóa học sau: (1) $\\text{Cl}_2$, (2) $\\text{HCl}$, (3) $\\text{Al}$, (4) $\\text{H}_2\\text{SO}_4$, (5) $\\text{O}_2$, (6) $\\text{CaCO}_3$. Có bao nhiêu chất trong danh sách trên là **hợp chất**?", ["3"], "Các chất (2) $\\text{HCl}$, (4) $\\text{H}_2\\text{SO}_4$ và (6) $\\text{CaCO}_3$ được tạo từ $2$ nguyên tố trở lên nên có $3$ hợp chất (còn $\\text{Cl}_2, \\text{Al}, \\text{O}_2$ là đơn chất)."),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 6: Khối lượng phân tử",
        icon="⚖️",
        description="Cách tính khối lượng phân tử (amu) của đơn chất và hợp chất bằng tổng khối lượng của các nguyên tử có trong phân tử.",
        requirements=[
            "Định nghĩa được khối lượng phân tử của một chất bằng tổng khối lượng của các nguyên tử có trong phân tử chất đó (đơn vị là $\\text{amu}$).",
            "Nhớ được khối lượng nguyên tử thông dụng ($\\text{H}=1, \\text{C}=12, \\text{N}=14, \\text{O}=16, \\text{Na}=23, \\text{Mg}=24, \\text{Al}=27, \\text{S}=32, \\text{Cl}=35{,}5, \\text{K}=39, \\text{Ca}=40, \\text{Fe}=56, \\text{Cu}=64$).",
            "Tính thành thạo khối lượng phân tử của các đơn chất ($\\text{H}_2, \\text{O}_2, \\text{N}_2, \\text{Cl}_2$) và các hợp chất có hoặc không có dấu ngoặc đơn (như $\\text{H}_2\\text{O}, \\text{CaCO}_3, \\text{Ca(OH)}_2, \\text{Al}_2(\\text{SO}_4)_3$).",
        ],
        definition="Khối lượng phân tử của một chất bằng tổng khối lượng của các nguyên tử có trong một phân tử chất đó. Đơn vị của khối lượng phân tử là đơn vị khối lượng nguyên tử ($\\text{amu}$).",
        theory=(
            "### 1. Công thức tính Khối lượng phân tử\n"
            "- Xét phân tử (hoặc đơn vị công thức) có dạng $A_x B_y C_z$:\n"
            "  $$\\text{KLPT}(A_x B_y C_z) = x \\cdot M_A + y \\cdot M_B + z \\cdot M_C \\quad (\\text{đơn vị: amu})$$\n"
            "- Đối với hợp chất chứa nhóm nguyên tử đặt trong dấu ngoặc đơn $A_x(BC_y)_z$: chỉ số $z$ ở ngoài dấu ngoặc nhân với toàn bộ khối lượng của nhóm $(BC_y)$:\n"
            "  $$\\text{KLPT}[A_x(BC_y)_z] = x \\cdot M_A + z \\cdot (M_B + y \\cdot M_C)$$\n\n"
            "### 2. Bảng khối lượng nguyên tử ($\\text{amu}$) của các nguyên tố thường gặp\n"
            "- $\\text{H} = 1; \\quad \\text{C} = 12; \\quad \\text{N} = 14; \\quad \\text{O} = 16; \\quad \\text{F} = 19; \\quad \\text{Na} = 23; \\quad \\text{Mg} = 24; \\quad \\text{Al} = 27$.\n"
            "- $\\text{Si} = 28; \\quad \\text{P} = 31; \\quad \\text{S} = 32; \\quad \\text{Cl} = 35{,}5; \\quad \\text{K} = 39; \\quad \\text{Ca} = 40; \\quad \\text{Fe} = 56; \\quad \\text{Cu} = 64; \\quad \\text{Zn} = 65; \\quad \\text{Ag} = 108; \\quad \\text{Ba} = 137$.\n"
            "- **Một số nhóm nguyên tử quen thuộc**: nhóm $-\\text{OH}$ ($17\\text{ amu}$), nhóm $-\\text{NO}_3$ ($62\\text{ amu}$), nhóm $=\\text{CO}_3$ ($60\\text{ amu}$), nhóm $=\\text{SO}_4$ ($96\\text{ amu}$), nhóm $-\\text{NH}_4$ ($18\\text{ amu}$), nhóm $\\equiv\\text{PO}_4$ ($95\\text{ amu}$)."
        ),
        formulas=[
            G(
                "Công thức tính Khối lượng phân tử (amu)",
                F("Khối lượng phân tử của chất A_x B_y", "$\\text{KLPT}(A_x B_y) = x \\cdot M_A + y \\cdot M_B\\text{ (amu)}$", "Ví dụ: $\\text{KLPT}(\\text{H}_2\\text{O}) = 2 \\cdot 1 + 16 = 18\\text{ amu}$; $\\text{KLPT}(\\text{CO}_2) = 12 + 2 \\cdot 16 = 44\\text{ amu}$."),
                F("Khối lượng phân tử khi có dấu ngoặc A_x(BC_y)_z", "$\\text{KLPT}[A_x(BC_y)_z] = x \\cdot M_A + z \\cdot (M_B + y \\cdot M_C)\\text{ (amu)}$", "Ví dụ: $\\text{KLPT}[\\text{Ca(OH)}_2] = 40 + 2 \\cdot (16 + 1) = 74\\text{ amu}$."),
            )
        ],
        example="Cho biết khối lượng nguyên tử: $\\text{H} = 1, \\text{C} = 12, \\text{O} = 16, \\text{S} = 32, \\text{Ca} = 40$. Hãy tính khối lượng phân tử của: (a) Sulfuric acid ($\\text{H}_2\\text{SO}_4$); (b) Calcium carbonate ($\\text{CaCO}_3$).",
        example_answer="- (a) Khối lượng phân tử của $\\text{H}_2\\text{SO}_4$ là: $2 \\cdot 1 + 1 \\cdot 32 + 4 \\cdot 16 = 2 + 32 + 64 = 98\\text{ amu}$.\n- (b) Khối lượng phân tử của $\\text{CaCO}_3$ là: $1 \\cdot 40 + 1 \\cdot 12 + 3 \\cdot 16 = 40 + 12 + 48 = 100\\text{ amu}$.",
        real_life="Tính đúng khối lượng phân tử là bước nền tảng bắt buộc để pha chế hóa chất, tính toán phần trăm dinh dưỡng trong phân bón và tính lượng chất trong mọi phản ứng hóa học.",
        quiz=[
            mcq("biet", "Đơn vị dùng để đo **khối lượng phân tử** của một chất là gì?", ["$\\text{amu}$ (đơn vị khối lượng nguyên tử)", "Mét ($\\text{m}$)", "Lít ($\\text{L}$)", "Newton ($\\text{N}$)"], 0, "Khối lượng phân tử bằng tổng khối lượng các nguyên tử trong phân tử nên có đơn vị là $\\text{amu}$."),
            mcq("biet", "Biết khối lượng nguyên tử của $\\text{H} = 1\\text{ amu}$ và $\\text{O} = 16\\text{ amu}$. Khối lượng phân tử của nước ($\\text{H}_2\\text{O}$) và của khí oxygen ($\\text{O}_2$) lần lượt là bao nhiêu?", ["$18\\text{ amu}$ và $32\\text{ amu}$", "$17\\text{ amu}$ và $16\\text{ amu}$", "$32\\text{ amu}$ và $18\\text{ amu}$", "$34\\text{ amu}$ và $32\\text{ amu}$"], 0, "Ta có $\\text{KLPT}(\\text{H}_2\\text{O}) = 2 \\cdot 1 + 16 = 18\\text{ amu}$ và $\\text{KLPT}(\\text{O}_2) = 2 \\cdot 16 = 32\\text{ amu}$."),
            mcq("hieu", "Biết $\\text{Ca} = 40, \\text{O} = 16, \\text{H} = 1$. Khối lượng phân tử của calcium hydroxide có công thức $\\text{Ca(OH)}_2$ bằng bao nhiêu $\\text{amu}$?", ["$74\\text{ amu}$", "$57\\text{ amu}$", "$58\\text{ amu}$", "$114\\text{ amu}$"], 0, "Ta có $\\text{KLPT}[\\text{Ca(OH)}_2] = 40 + 2 \\cdot (16 + 1) = 40 + 34 = 74\\text{ amu}$."),
            tf4("hieu", "Cho $\\text{H} = 1, \\text{C} = 12, \\text{N} = 14, \\text{O} = 16, \\text{Na} = 23, \\text{Cl} = 35{,}5$. Xét tính đúng/sai của các phát biểu sau:", [
                "Khối lượng phân tử của khí ammonia ($\\text{NH}_3$) là $14 + 3 \\cdot 1 = 17\\text{ amu}$.",
                "Khối lượng phân tử của khí carbon dioxide ($\\text{CO}_2$) là $12 + 2 \\cdot 16 = 44\\text{ amu}$.",
                "Khối lượng phân tử của khí nitrogen ($\\text{N}_2$) là $14\\text{ amu}$.",
                "Khối lượng phân tử của muối ăn sodium chloride ($\\text{NaCl}$) là $23 + 35{,}5 = 58{,}5\\text{ amu}$.",
            ], [True, True, False, True], "Ý c) sai vì phân tử khí nitrogen là $\\text{N}_2$ gồm $2$ nguyên tử $\\text{N}$, nên khối lượng phân tử là $2 \\cdot 14 = 28\\text{ amu}$."),
            short("vandung", "Biết $\\text{C} = 12, \\text{H} = 1, \\text{O} = 16$. Khối lượng phân tử của đường glucose có công thức phân tử $\\text{C}_6\\text{H}_{12}\\text{O}_6$ bằng bao nhiêu $\\text{amu}$?", ["180"], "Ta có $\\text{KLPT}(\\text{C}_6\\text{H}_{12}\\text{O}_6) = 6 \\cdot 12 + 12 \\cdot 1 + 6 \\cdot 16 = 72 + 12 + 96 = 180\\text{ amu}$.", unit="amu"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 7: Sự tạo thành ion và liên kết ion",
        icon="🧲",
        description="Quy tắc lớp vỏ bền vững của khí hiếm, sự nhường electron của nguyên tử kim loại tạo ion dương, sự nhận electron của phi kim tạo ion âm và bản chất liên kết ion.",
        requirements=[
            "Giải thích được xu hướng của các nguyên tử kim loại (nhường $1, 2, 3$ electron lớp ngoài cùng để tạo thành **ion dương / cation** $M^{n+}$) và nguyên tử phi kim (nhận $1, 2, 3$ electron để tạo thành **ion âm / anion** $X^{m-}$) nhằm đạt lớp vỏ bền vững của khí hiếm ($8e$ hoặc $2e$).",
            "Định nghĩa được liên kết ion là liên kết được hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu (thường giữa kim loại điển hình và phi kim điển hình).",
            "Nêu được các đặc điểm tính chất chung của hợp chất ion (như $\\text{NaCl}, \\text{MgO}, \\text{CaCl}_2$): ở điều kiện thường là chất rắn kết tinh, có nhiệt độ nóng chảy và nhiệt độ sôi cao, khi tan trong nước tạo dung dịch dẫn điện.",
        ],
        definition="Khi nguyên tử kim loại nhường electron sẽ trở thành ion dương (cation), còn nguyên tử phi kim nhận electron sẽ trở thành ion âm (anion) để đạt lớp vỏ electron bền vững như khí hiếm. Liên kết ion là liên kết được hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu.",
        theory=(
            "### 1. Sự tạo thành Ion dương và Ion âm\n"
            "- Để đạt lớp vỏ ngoài cùng bền vững ($8e$ như $\\text{Ne}, \\text{Ar}$ hoặc $2e$ như $\\text{He}$):\n"
            "  - **Nguyên tử Kim loại** (có $1, 2, 3e$ lớp ngoài cùng) dễ **nhường electron** tạo thành **ion dương**:\n"
            "    - $\\text{Na}$ ($Z=11: 2, 8, 1$) nhường $1e \\longrightarrow \\text{Na}^+$ ($10e: 2, 8$ giống $\\text{Ne}$).\n"
            "    - $\\text{Mg}$ ($Z=12: 2, 8, 2$) nhường $2e \\longrightarrow \\text{Mg}^{2+}$ ($10e: 2, 8$ giống $\\text{Ne}$).\n"
            "    - $\\text{Al}$ ($Z=13: 2, 8, 3$) nhường $3e \\longrightarrow \\text{Al}^{3+}$.\n"
            "  - **Nguyên tử Phi kim** (có $5, 6, 7e$ lớp ngoài cùng) dễ **nhận thêm electron** tạo thành **ion âm**:\n"
            "    - $\\text{Cl}$ ($Z=17: 2, 8, 7$) nhận $1e \\longrightarrow \\text{Cl}^-$ ($18e: 2, 8, 8$ giống $\\text{Ar}$).\n"
            "    - $\\text{O}$ ($Z=8: 2, 6$) nhận $2e \\longrightarrow \\text{O}^{2-}$ ($10e: 2, 8$ giống $\\text{Ne}$).\n\n"
            "### 2. Sự tạo thành Liên kết ion và Tính chất hợp chất ion\n"
            "- Hai ion mang điện tích trái dấu (như $\\text{Na}^+$ và $\\text{Cl}^-$, hoặc $\\text{Mg}^{2+}$ và $\\text{O}^{2-}$) hút nhau bằng lực hút tĩnh điện tạo thành **liên kết ion** (phân tử $\\text{NaCl}, \\text{MgO}, \\text{CaCl}_2$).\n"
            "- **Tính chất của hợp chất ion**: là chất rắn ở nhiệt độ thường, khá cứng nhưng giòn, có **nhiệt độ nóng chảy và nhiệt độ sôi rất cao** (ví dụ $\\text{NaCl}$ nóng chảy ở $801^\\circ\\text{C}$, $\\text{MgO}$ nóng chảy ở $2852^\\circ\\text{C}$), nhiều chất tan tốt trong nước tạo thành dung dịch dẫn được điện."
        ),
        formulas=[
            G(
                "Quá trình tạo thành Ion và Liên kết ion",
                F("Sự tạo thành ion dương (Kim loại) và ion âm (Phi kim)", "$\\text{Kim loại } M \\xrightarrow{-ne} M^{n+} \\text{ (ion dương)}; \\qquad \\text{Phi kim } X \\xrightarrow{+me} X^{m-} \\text{ (ion âm)}$", "Số electron trong ion dương $M^{n+}$ là $e_{\\text{ion}} = Z - n$; số electron trong ion âm $X^{m-}$ là $e_{\\text{ion}} = Z + m$."),
                F("Sơ đồ hình thành liên kết ion trong NaCl và MgO", "$\\text{Na}^+ + \\text{Cl}^- \\longrightarrow \\text{NaCl}; \\qquad \\text{Mg}^{2+} + \\text{O}^{2-} \\longrightarrow \\text{MgO}; \\qquad \\text{Ca}^{2+} + 2\\text{Cl}^- \\longrightarrow \\text{CaCl}_2$", "Dấu hiệu nhận biết nhanh: Hợp chất tạo bởi **Kim loại điển hình + Phi kim điển hình** có liên kết ion."),
            )
        ],
        example="Trong phản ứng giữa kim loại Magnesium ($\\text{Mg}, Z = 12$, lớp ngoài cùng có $2e$) và phi kim Oxygen ($\\text{O}, Z = 8$, lớp ngoài cùng có $6e$) tạo thành hợp chất magnesium oxide ($\\text{MgO}$): hãy cho biết nguyên tử nào nhường electron, nguyên tử nào nhận electron, mỗi nguyên tử nhường/nhận bao nhiêu electron và tạo ra các ion nào?",
        example_answer="Nguyên tử kim loại $\\text{Mg}$ **nhường đi $2$ electron** lớp ngoài cùng để trở thành **ion dương $\\text{Mg}^{2+}$** (có $12 - 2 = 10$ electron giống khí hiếm $\\text{Ne}$). Nguyên tử phi kim $\\text{O}$ **nhận thêm $2$ electron** từ $\\text{Mg}$ để trở thành **ion âm $\\text{O}^{2-}$** (có $8 + 2 = 10$ electron giống $\\text{Ne}$). Sau đó hai ion $\\text{Mg}^{2+}$ và $\\text{O}^{2-}$ hút nhau tạo thành liên kết ion trong $\\text{MgO}$.",
        real_life="Muối ăn ($\\text{NaCl}$) là hợp chất ion tiêu biểu; khi hòa tan trong nước hoặc trong dịch cơ thể, $\\text{NaCl}$ phân li thành các ion $\\text{Na}^+$ và $\\text{Cl}^-$ đóng vai trò chất điện giải dẫn truyền xung thần kinh và cân bằng nước trong cơ thể.",
        quiz=[
            mcq("biet", "Khi tham gia hình thành liên kết ion, nguyên tử **kim loại** có xu hướng nhường hay nhận electron và tạo thành loại ion nào?", ["Nhường electron lớp ngoài cùng để tạo thành ion dương", "Nhận thêm electron để tạo thành ion âm", "Nhường hạt proton trong hạt nhân", "Không nhường cũng không nhận electron"], 0, "Nguyên tử kim loại có $1, 2, 3$ electron lớp ngoài cùng nên có xu hướng nhường electron để tạo thành ion dương."),
            mcq("biet", "Liên kết ion được hình thành bởi bản chất lực nào và thường xảy ra giữa những loại nguyên tố nào?", ["Hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu (thường giữa kim loại điển hình và phi kim điển hình)", "Hình thành bởi sự dùng chung electron giữa hai nguyên tử phi kim giống hệt nhau", "Hình thành giữa hai nguyên tử khí hiếm", "Hình thành bởi lực đẩy giữa hai hạt nhân"], 0, "Liên kết ion là liên kết được tạo thành bởi lực hút tĩnh điện giữa ion dương (kim loại) và ion âm (phi kim)."),
            mcq("hieu", "Nguyên tử Sodium ($\\text{Na}$) có $11$ proton và $11$ electron ($2, 8, 1$). Khi nguyên tử $\\text{Na}$ nhường đi $1$ electron ở lớp ngoài cùng để tạo thành ion dương $\\text{Na}^+$ thì trong ion $\\text{Na}^+$ có bao nhiêu hạt proton và bao nhiêu hạt electron?", ["Có $11$ proton và $10$ electron", "Có $10$ proton và $10$ electron", "Có $11$ proton và $12$ electron", "Có $12$ proton và $11$ electron"], 0, "Khi tạo thành ion, hạt nhân nguyên tử không thay đổi nên vẫn có $11$ proton; lớp vỏ mất đi $1$ electron nên còn $11 - 1 = 10$ electron."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về ion và liên kết ion:", [
                "Nguyên tử Oxygen ($Z = 8$, có $6e$ lớp ngoài cùng) có xu hướng nhận thêm $2$ electron để tạo thành ion âm $\\text{O}^{2-}$ có lớp vỏ bền vững giống khí hiếm Neon.",
                "Phân tử sodium chloride ($\\text{NaCl}$), magnesium oxide ($\\text{MgO}$) và calcium chloride ($\\text{CaCl}_2$) đều là các hợp chất ion.",
                "Ở điều kiện thường, các hợp chất ion đều là chất khí có nhiệt độ sôi rất thấp.",
                "Dung dịch muối ăn ($\\text{NaCl}$) trong nước dẫn được điện là do có chứa các ion $\\text{Na}^+$ và $\\text{Cl}^-$ chuyển động tự do.",
            ], [True, True, False, True], "Ý c) sai vì ở điều kiện thường, tất cả các hợp chất ion đều là chất rắn tinh thể có nhiệt độ nóng chảy và nhiệt độ sôi rất cao."),
            short("vandung", "Nguyên tử Chlorine ($\\text{Cl}$) có $17$ hạt electron ở lớp vỏ ($2, 8, 7$). Khi nguyên tử $\\text{Cl}$ nhận thêm $1$ electron để tạo thành ion âm $\\text{Cl}^-$ thì tổng số hạt electron của ion $\\text{Cl}^-$ bằng bao nhiêu hạt?", ["18"], "Số hạt electron của ion $\\text{Cl}^-$ là $17 + 1 = 18$ hạt (bằng số electron của khí hiếm Argon).", unit="hạt"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 8: Liên kết cộng hóa trị",
        icon="🤝",
        description="Bản chất liên kết cộng hóa trị bằng sự dùng chung các cặp electron giữa các nguyên tử phi kim (H₂, O₂, N₂, Cl₂, H₂O, CO₂, NH₃, HCl) và tính chất chất cộng hóa trị.",
        requirements=[
            "Định nghĩa được liên kết cộng hóa trị là liên kết được tạo nên giữa hai nguyên tử bằng **một hay nhiều cặp electron dùng chung** (thường xảy ra giữa các nguyên tử phi kim với nhau).",
            "Mô tả được số cặp electron dùng chung trong các phân tử tiêu biểu: $1$ cặp dùng chung ($\\text{H}_2, \\text{Cl}_2, \\text{HCl}$), $2$ cặp dùng chung ($\\text{O}_2$), $3$ cặp dùng chung ($\\text{N}_2$), và trong $\\text{H}_2\\text{O}, \\text{NH}_3, \\text{CO}_2, \\text{CH}_4$.",
            "So sánh được tính chất của chất cộng hóa trị (có ở cả 3 thể rắn, lỏng, khí; nhiệt độ nóng chảy và nhiệt độ sôi thường thấp hơn chất ion; phần lớn không dẫn điện).",
        ],
        definition="Liên kết cộng hóa trị là liên kết được hình thành giữa hai nguyên tử bằng một hay nhiều cặp electron dùng chung (thường là liên kết giữa các nguyên tử phi kim với nhau). Mỗi cặp electron dùng chung được tính cho cả hai nguyên tử để mỗi nguyên tử đều đạt lớp vỏ bền vững của khí hiếm.",
        theory=(
            "### 1. Sự hình thành Liên kết cộng hóa trị trong Đơn chất và Hợp chất\n"
            "- Khi hai nguyên tử **phi kim** kết hợp với nhau, không nguyên tử nào nhường hẳn electron mà chúng **góp chung electron** tạo thành các **cặp electron dùng chung**:\n"
            "  - **Phân tử Hydrogen ($\\text{H}_2$)**: mỗi nguyên tử $\\text{H}$ (có $1e$) góp $1e$ tạo thành **$1$ cặp electron dùng chung** ($\\text{H}-\\text{H}$) để mỗi $\\text{H}$ có $2e$ giống khí hiếm $\\text{He}$.\n"
            "  - **Phân tử Oxygen ($\\text{O}_2$)**: mỗi nguyên tử $\\text{O}$ (có $6e$ lớp ngoài cùng, thiếu $2e$) góp $2e$ tạo thành **$2$ cặp electron dùng chung** ($\\text{O}=\\text{O}$) để mỗi $\\text{O}$ có đủ $8e$ giống $\\text{Ne}$.\n"
            "  - **Phân tử Nitrogen ($\\text{N}_2$)**: mỗi nguyên tử $\\text{N}$ (có $5e$ ngoài cùng, thiếu $3e$) góp $3e$ tạo thành **$3$ cặp electron dùng chung** ($\\text{N}\\equiv\\text{N}$).\n"
            "  - **Phân tử Nước ($\\text{H}_2\\text{O}$)**: nguyên tử $\\text{O}$ góp chung với mỗi nguyên tử $\\text{H}$ $1$ cặp electron (tổng cộng có $2$ cặp electron dùng chung trong phân tử $\\text{H}_2\\text{O}$).\n"
            "  - **Phân tử Carbon dioxide ($\\text{CO}_2$)**: nguyên tử $\\text{C}$ ($4e$ ngoài cùng) góp chung $2$ cặp electron với mỗi nguyên tử $\\text{O}$ ($\\text{O}=\\text{C}=\\text{O}$, tổng cộng $4$ cặp dùng chung).\n\n"
            "### 2. Tính chất của các chất có liên kết cộng hóa trị\n"
            "- Ở điều kiện thường có thể ở cả **3 thể**: thể khí ($\\text{H}_2, \\text{O}_2, \\text{CO}_2, \\text{NH}_3, \\text{CH}_4$), thể lỏng ($\\text{H}_2\\text{O}$, cồn $\\text{C}_2\\text{H}_5\\text{OH}$) và thể rắn (đường saccharose, glucose, sulfur, iodine).\n"
            "- Thường có **nhiệt độ nóng chảy và nhiệt độ sôi thấp** hơn nhiều so với hợp chất ion, và các chất cộng hóa trị nguyên chất (như nước cất, dung dịch đường, cồn) **không dẫn điện**."
        ),
        formulas=[
            G(
                "Số cặp electron dùng chung và Phân biệt Liên kết cộng hóa trị – Liên kết ion",
                F("Số cặp electron dùng chung giữa 2 nguyên tử trong đơn chất phi kim", "$\\text{H}-\\text{H},\\ \\text{Cl}-\\text{Cl}: 1\\text{ cặp } (2e); \\qquad \\text{O}=\\text{O}: 2\\text{ cặp } (4e); \\qquad \\text{N}\\equiv\\text{N}: 3\\text{ cặp } (6e)$", "Số electron một nguyên tử phi kim góp chung bằng số electron mà nó còn thiếu để đạt $8e$ (hoặc $2e$ đối với $\\text{H}$): $8 - e_{\\text{ngoài cùng}}$."),
                F("Quy tắc phân biệt nhanh Chất cộng hóa trị và Chất ion", "$\\text{Phi kim} + \\text{Phi kim (vd: } \\text{H}_2, \\text{O}_2, \\text{H}_2\\text{O}, \\text{CO}_2, \\text{NH}_3, \\text{CH}_4) \\implies \\text{Liên kết CỘNG HÓA TRỊ}$", "Còn $\\text{Kim loại điển hình} + \\text{Phi kim điển hình (vd: } \\text{NaCl}, \\text{KCl}, \\text{MgO}, \\text{CaO}) \\implies \\text{Liên kết ION}$."),
            )
        ],
        example="Nguyên tử Nitrogen ($\\text{N}$) có $7$ electron ($2$ ở lớp trong và $5$ ở lớp ngoài cùng). Khi hai nguyên tử $\\text{N}$ liên kết với nhau tạo thành phân tử khí nitrogen ($\\text{N}_2$), mỗi nguyên tử $\\text{N}$ cần thêm bao nhiêu electron để đạt $8e$ bền vững và giữa hai nguyên tử $\\text{N}$ có bao nhiêu cặp electron dùng chung?",
        example_answer="Mỗi nguyên tử $\\text{N}$ có $5$ electron lớp ngoài cùng nên cần thêm $8 - 5 = 3$ electron để đạt lớp vỏ $8e$ bền vững như khí hiếm $\\text{Ne}$. Do đó mỗi nguyên tử $\\text{N}$ góp ra $3$ electron để tạo thành **$3$ cặp electron dùng chung** (tức $6$ electron dùng chung, kí hiệu $\\text{N}\\equiv\\text{N}$).",
        real_life="Đường kính trắng (saccharose – chất cộng hóa trị) và muối ăn ($\\text{NaCl}$ – chất ion) đều là các hạt tinh thể màu trắng tan trong nước, nhưng khi đun trên chảo nóng đường nhanh chóng nóng chảy ở $186^\\circ\\text{C}$ trong khi muối ăn không hề nóng chảy (vì nóng chảy ở tận $801^\\circ\\text{C}$); ngoài ra dung dịch nước đường không dẫn điện còn dung dịch nước muối dẫn điện tốt.",
        quiz=[
            mcq("biet", "Bản chất của **liên kết cộng hóa trị** giữa hai nguyên tử là gì?", ["Được tạo nên giữa hai nguyên tử bằng một hay nhiều cặp electron dùng chung", "Được tạo nên bởi lực hút tĩnh điện giữa ion dương kim loại và ion âm phi kim", "Do một nguyên tử lấy mất hoàn toàn hạt nhân của nguyên tử kia", "Do các hạt neutron bay từ nguyên tử này sang nguyên tử khác"], 0, "Liên kết cộng hóa trị được hình thành bằng một hay nhiều cặp electron dùng chung giữa hai nguyên tử."),
            mcq("biet", "Dãy các chất nào sau đây chỉ gồm các chất có **liên kết cộng hóa trị**?", ["$\\text{H}_2, \\text{O}_2, \\text{H}_2\\text{O}, \\text{CO}_2, \\text{NH}_3, \\text{CH}_4$", "$\\text{NaCl}, \\text{MgO}, \\text{CaCl}_2, \\text{K}_2\\text{O}$", "$\\text{NaCl}, \\text{H}_2\\text{O}, \\text{MgO}$", "$\\text{CaO}, \\text{Na}_2\\text{O}, \\text{KCl}$"], 0, "Các phân tử $\\text{H}_2, \\text{O}_2, \\text{H}_2\\text{O}, \\text{CO}_2, \\text{NH}_3, \\text{CH}_4$ đều được tạo bởi các nguyên tử phi kim liên kết với nhau bằng cặp electron dùng chung."),
            mcq("hieu", "Trong phân tử khí oxygen ($\\text{O}_2$), biết mỗi nguyên tử $\\text{O}$ có $6$ electron ở lớp ngoài cùng. Số cặp electron dùng chung giữa hai nguyên tử oxygen trong phân tử $\\text{O}_2$ là bao nhiêu?", ["$2$ cặp electron dùng chung (gồm $4$ electron)", "$1$ cặp electron dùng chung (gồm $2$ electron)", "$3$ cặp electron dùng chung (gồm $6$ electron)", "$6$ cặp electron dùng chung"], 0, "Mỗi nguyên tử $\\text{O}$ thiếu $8 - 6 = 2$ electron nên mỗi nguyên tử góp $2$ electron tạo thành $2$ cặp electron dùng chung ($\\text{O}=\\text{O}$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về liên kết cộng hóa trị:", [
                "Trong phân tử nước ($\\text{H}_2\\text{O}$), nguyên tử $\\text{O}$ có $2$ cặp electron dùng chung với $2$ nguyên tử $\\text{H}$.",
                "Trong phân tử khí hydrogen ($\\text{H}_2$) và phân tử hydrogen chloride ($\\text{HCl}$) đều có $1$ cặp electron dùng chung.",
                "Ở điều kiện thường, các chất có liên kết cộng hóa trị có thể tồn tại ở cả ba thể rắn, lỏng và khí.",
                "Dung dịch đường glucose tinh khiết pha trong nước cất dẫn điện mạnh hơn dung dịch muối ăn $\\text{NaCl}$.",
            ], [True, True, True, False], "Ý d) sai vì đường glucose là hợp chất cộng hóa trị không phân li ra ion trong nước nên dung dịch đường không dẫn điện."),
            short("vandung", "Trong phân tử ammonia ($\\text{NH}_3$), một nguyên tử nitrogen ($\\text{N}$) liên kết với $3$ nguyên tử hydrogen ($\\text{H}$), trong đó mỗi nguyên tử $\\text{H}$ góp chung $1$ electron với nguyên tử $\\text{N}$. Tổng số **cặp electron dùng chung** trong một phân tử $\\text{NH}_3$ bằng bao nhiêu cặp?", ["3"], "Mỗi liên kết $\\text{N}-\\text{H}$ có $1$ cặp electron dùng chung, có $3$ nguyên tử $\\text{H}$ liên kết với $\\text{N}$ nên tổng cộng có $3$ cặp electron dùng chung.", unit="cặp"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 9: Hóa trị và công thức hóa học",
        icon="📝",
        description="Khái niệm hóa trị (biểu thị bằng số La Mã I, II, III...), quy tắc hóa trị x.a = y.b và cách lập công thức hóa học khi biết hóa trị.",
        requirements=[
            "Nêu được hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác (ghi bằng chữ số La Mã $\\text{I, II, III, IV}$...), lấy hóa trị của $\\text{H}$ làm $1$ đơn vị ($\\text{I}$) và hóa trị của $\\text{O}$ là $2$ đơn vị ($\\text{II}$).",
            "Phát biểu và vận dụng được **quy tắc hóa trị** cho hợp chất hai nguyên tố $A^a_x B^b_y$: tích của chỉ số và hóa trị của nguyên tố này bằng tích của chỉ số và hóa trị của nguyên tố kia ($x \\cdot a = y \\cdot b \\iff \\dfrac{x}{y} = \\dfrac{b}{a}$).",
            "Tính được hóa trị của một nguyên tố trong công thức cho trước và lập được công thức hóa học của hợp chất khi biết hóa trị của hai nguyên tố hoặc nhóm nguyên tử.",
        ],
        definition="Hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác (trong hợp chất cộng hóa trị, hóa trị bằng số cặp electron dùng chung; trong hợp chất ion, hóa trị bằng điện tích của ion). Quy tắc hóa trị đối với hợp chất $A^a_x B^b_y$: $x \\cdot a = y \\cdot b$.",
        theory=(
            "### 1. Hóa trị của nguyên tố và nhóm nguyên tử\n"
            "- Quy ước: Trong các hợp chất, **Hydrogen ($\\text{H}$) luôn có hóa trị $\\text{I}$** và **Oxygen ($\\text{O}$) thường có hóa trị $\\text{II}$**.\n"
            "- **Bảng hóa trị thường gặp cần thuộc lòng**:\n"
            "  - **Hóa trị $\\text{I}$**: $\\text{H}, \\text{Na}, \\text{K}, \\text{Ag}, \\text{Cl}$ (trong muối chloride); nhóm $-\\text{OH}$ (hydroxide), nhóm $-\\text{NO}_3$ (nitrate), nhóm $-\\text{NH}_4$ (ammonium).\n"
            "  - **Hóa trị $\\text{II}$**: $\\text{O}, \\text{Mg}, \\text{Ca}, \\text{Ba}, \\text{Zn}, \\text{Cu}$ ($\\text{I, II}$); nhóm $=\\text{SO}_4$ (sulfate), nhóm $=\\text{CO}_3$ (carbonate), nhóm $=\\text{SO}_3$ (sulfite).\n"
            "  - **Hóa trị $\\text{III}$**: $\\text{Al}$; nhóm $\\equiv\\text{PO}_4$ (phosphate).\n"
            "  - **Nguyên tố có nhiều hóa trị**: $\\text{Fe}$ ($\\text{II, III}$); $\\text{C}$ ($\\text{II, IV}$); $\\text{S}$ ($\\text{II, IV, VI}$); $\\text{N}$ ($\\text{I, II, III, IV, V}$); $\\text{P}$ ($\\text{III, V}$).\n\n"
            "### 2. Quy tắc hóa trị và Hai dạng bài toán cơ bản\n"
            "- Với công thức hóa học chung $A^a_x B^b_y$ (trong đó $x, y$ là các chỉ số nguyên dương tối giản; $a, b$ là hóa trị của $A, B$):\n"
            "  $$x \\cdot a = y \\cdot b \\iff \\dfrac{x}{y} = \\dfrac{b}{a} = \\dfrac{b'}{a'} \\quad (\\text{với } \\dfrac{b'}{a'} \\text{ là phân số tối giản})$$\n"
            "- **Dạng 1 (Tìm hóa trị $a$ khi biết công thức $A_x B_y$ và hóa trị $b$)**: $a = \\dfrac{y \\cdot b}{x}$.\n"
            "- **Dạng 2 (Lập công thức hóa học khi biết hóa trị $a$ và $b$)**: lấy chéo tỉ lệ tối giản $x = b'$ và $y = a'$ (nếu chỉ số bằng $1$ thì không ghi số $1$; nếu chỉ số của nhóm nguyên tử $\\ge 2$ thì phải đặt nhóm nguyên tử trong dấu ngoặc đơn, ví dụ $\\text{Al}_2(\\text{SO}_4)_3$)."
        ),
        formulas=[
            G(
                "Quy tắc hóa trị và Lập công thức hóa học",
                F("Biểu thức Quy tắc hóa trị cho hợp chất A^a_x B^b_y", "$x \\cdot a = y \\cdot b \\implies a = \\dfrac{y \\cdot b}{x}; \\qquad \\dfrac{x}{y} = \\dfrac{b}{a} = \\dfrac{b'}{a'}$", "Quy tắc chéo nhanh: Hóa trị tối giản của nguyên tố này là chỉ số của nguyên tố kia ($A^a_x B^b_y \\implies x = b',\\ y = a'$)."),
                F("Hóa trị chuẩn của các nhóm nguyên tử thông dụng", "$\\text{Hóa trị I}: (-\\text{OH}),\\ (-\\text{NO}_3),\\ (-\\text{NH}_4); \\qquad \\text{Hóa trị II}: (=\\text{SO}_4),\\ (=\\text{CO}_3); \\qquad \\text{Hóa trị III}: (\\equiv\\text{PO}_4)$", "Ví dụ: $\\text{Al}(\\text{III})$ kết hợp với nhóm $(\\text{SO}_4)(\\text{II})$ tạo ra công thức $\\text{Al}_2(\\text{SO}_4)_3$."),
            )
        ],
        example="Áp dụng quy tắc hóa trị, hãy: (a) Xác định hóa trị của nguyên tố Iron ($\\text{Fe}$) trong hợp chất $\\text{Fe}_2\\text{O}_3$ (biết $\\text{O}$ có hóa trị $\\text{II}$); (b) Lập công thức hóa học của hợp chất tạo bởi Calcium ($\\text{Ca}$ có hóa trị $\\text{II}$) và nhóm phosphate ($\\text{PO}_4$ có hóa trị $\\text{III}$).",
        example_answer="- (a) Gọi $a$ là hóa trị của $\\text{Fe}$ trong $\\text{Fe}_2\\text{O}_3$. Theo quy tắc hóa trị: $2 \\cdot a = 3 \\cdot \\text{II} \\implies a = \\dfrac{6}{2} = \\text{III}$. Vậy $\\text{Fe}$ có hóa trị $\\text{III}$.\n- (b) Đặt công thức là $\\text{Ca}_x(\\text{PO}_4)_y$. Theo quy tắc hóa trị: $x \\cdot \\text{II} = y \\cdot \\text{III} \\implies \\dfrac{x}{y} = \\dfrac{3}{2} \\implies x = 3, y = 2$. Vậy công thức hóa học là **$\\text{Ca}_3(\\text{PO}_4)_2$**.",
        real_life="Quy tắc hóa trị giúp ta viết đúng công thức hóa học của mọi hợp chất vô cơ quen thuộc như vôi tôi $\\text{Ca(OH)}_2$, phèn chua, thạch cao, thuốc muối dạ dày mà không cần học vẹt từng chất.",
        quiz=[
            mcq("biet", "Đối với hợp chất có công thức hóa học chung là $A^a_x B^b_y$ (với $a, b$ lần lượt là hóa trị của $A, B$ và $x, y$ là chỉ số nguyên tử), biểu thức của **quy tắc hóa trị** là gì?", ["$x \\cdot a = y \\cdot b$", "$x \\cdot b = y \\cdot a$", "$x + a = y + b$", "$\\dfrac{x}{a} = \\dfrac{y}{b}$"], 0, "Theo quy tắc hóa trị, tích chỉ số và hóa trị của nguyên tố này bằng tích chỉ số và hóa trị của nguyên tố kia: $x \\cdot a = y \\cdot b$."),
            mcq("biet", "Trong hợp chất sulfur trioxide có công thức $\\text{SO}_3$ (biết $\\text{O}$ có hóa trị $\\text{II}$), nguyên tố Sulfur ($\\text{S}$) có hóa trị bằng bao nhiêu?", ["Hóa trị $\\text{VI}$ ($6$)", "Hóa trị $\\text{IV}$ ($4$)", "Hóa trị $\\text{II}$ ($2$)", "Hóa trị $\\text{III}$ ($3$)"], 0, "Trong $\\text{SO}_3$, gọi $a$ là hóa trị của $\\text{S}$: $1 \\cdot a = 3 \\cdot \\text{II} \\implies a = \\text{VI}$."),
            mcq("hieu", "Công thức hóa học của hợp chất tạo bởi nguyên tố Aluminium ($\\text{Al}$, hóa trị $\\text{III}$) và nhóm sulfate ($=\\text{SO}_4$, hóa trị $\\text{II}$) là công thức nào sau đây?", ["$\\text{Al}_2(\\text{SO}_4)_3$", "$\\text{Al}_3(\\text{SO}_4)_2$", "$\\text{AlSO}_4$", "$\\text{Al}_2\\text{SO}_4$"], 0, "Đặt công thức là $\\text{Al}_x(\\text{SO}_4)_y$: $\\dfrac{x}{y} = \\dfrac{\\text{II}}{\\text{III}} = \\dfrac{2}{3} \\implies x = 2, y = 3 \\implies \\text{Al}_2(\\text{SO}_4)_3$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về hóa trị và công thức hóa học:", [
                "Trong các hợp chất cộng hóa trị, nguyên tố Hydrogen ($\\text{H}$) được chọn làm đơn vị có hóa trị $\\text{I}$ và nguyên tố Oxygen ($\\text{O}$) có hóa trị $\\text{II}$.",
                "Trong hợp chất $\\text{FeO}$ nguyên tố $\\text{Fe}$ có hóa trị $\\text{II}$, còn trong hợp chất $\\text{Fe}_2\\text{O}_3$ nguyên tố $\\text{Fe}$ có hóa trị $\\text{III}$.",
                "Công thức hóa học của hợp chất tạo bởi $\\text{Mg}$ (hóa trị $\\text{II}$) và nhóm $-\\text{OH}$ (hóa trị $\\text{I}$) được viết là $\\text{MgOH}_2$ (không cần dấu ngoặc).",
                "Công thức hóa học của hợp chất tạo bởi $\\text{C}$ (hóa trị $\\text{IV}$) và $\\text{O}$ (hóa trị $\\text{II}$) là $\\text{CO}_2$.",
            ], [True, True, False, True], "Ý c) sai vì khi có từ $2$ nhóm nguyên tử $(-\\text{OH})$ trở lên thì bắt buộc phải đặt nhóm nguyên tử trong dấu ngoặc đơn: $\\text{Mg(OH)}_2$."),
            short("vandung", "Cho hợp chất diphosphorus pentoxide có công thức hóa học là $\\text{P}_2\\text{O}_5$ (biết $\\text{O}$ có hóa trị $\\text{II}$). Hóa trị của nguyên tố Phosphorus ($\\text{P}$) trong hợp chất này bằng bao nhiêu (nhập bằng chữ số tự nhiên từ 1 đến 7)?", ["5"], "Áp dụng quy tắc hóa trị cho $\\text{P}_2\\text{O}_5$: $2 \\cdot a = 5 \\cdot 2 = 10 \\implies a = 5$ (hóa trị $\\text{V}$)."),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 10: Tính phần trăm khối lượng các nguyên tố và lập công thức hóa học",
        icon="📊",
        description="Ý nghĩa của công thức hóa học, công thức tính phần trăm khối lượng nguyên tố trong hợp chất và cách lập công thức hóa học khi biết phần trăm khối lượng và khối lượng phân tử.",
        requirements=[
            "Nêu được ý nghĩa của công thức hóa học (cho biết nguyên tố nào tạo ra chất, số nguyên tử của mỗi nguyên tố trong 1 phân tử và khối lượng phân tử của chất).",
            "Tính được phần trăm khối lượng của mỗi nguyên tố trong hợp chất $A_x B_y$: $\\%m_A = \\dfrac{x \\cdot M_A}{\\text{KLPT}(A_x B_y)} \\cdot 100\\%$.",
            "Xác định được công thức hóa học của hợp chất khi biết phần trăm khối lượng các nguyên tố và khối lượng phân tử: $x = \\dfrac{\\%m_A \\cdot \\text{KLPT}}{100\\% \\cdot M_A}$.",
        ],
        definition="Trong hợp chất có công thức hóa học $A_x B_y$, phần trăm khối lượng của nguyên tố $A$ bằng tỉ số phần trăm giữa khối lượng của nguyên tố $A$ trong một phân tử và khối lượng phân tử của hợp chất: $\\%m_A = \\dfrac{x \\cdot M_A}{x \\cdot M_A + y \\cdot M_B} \\cdot 100\\%$.",
        theory=(
            "### 1. Ý nghĩa của Công thức hóa học\n"
            "Mỗi công thức hóa học $A_x B_y$ cho ta biết 3 thông tin:\n"
            "1. **Các nguyên tố** tạo nên chất đó.\n"
            "2. **Số nguyên tử của mỗi nguyên tố** có trong một phân tử của chất (và tỉ lệ số nguyên tử $x : y$).\n"
            "3. **Khối lượng phân tử** của chất.\n\n"
            "### 2. Hai bài toán trọng tâm về Công thức hóa học\n"
            "- **Bài toán 1 — Tính $\\%$ khối lượng mỗi nguyên tố từ công thức $A_x B_y C_z$**:\n"
            "  $$\\text{KLPT} = x M_A + y M_B + z M_C$$\n"
            "  $$\\%m_A = \\dfrac{x \\cdot M_A}{\\text{KLPT}} \\cdot 100\\%; \\qquad \\%m_B = \\dfrac{y \\cdot M_B}{\\text{KLPT}} \\cdot 100\\%; \\qquad \\%m_C = 100\\% - (\\%m_A + \\%m_B)$$\n"
            "- **Bài toán 2 — Lập công thức hóa học $A_x B_y$ khi biết $\\%m_A, \\%m_B$ và $\\text{KLPT}$**:\n"
            "  - **Cách 1 (Khi đã biết $\\text{KLPT} = M$)**:\n"
            "    $$x = \\dfrac{\\%m_A \\cdot M}{100\\% \\cdot M_A}; \\qquad y = \\dfrac{\\%m_B \\cdot M}{100\\% \\cdot M_B}$$\n"
            "  - **Cách 2 (Tỉ lệ thức chung mọi trường hợp)**:\n"
            "    $$x : y = \\dfrac{\\%m_A}{M_A} : \\dfrac{\\%m_B}{M_B}$$"
        ),
        formulas=[
            G(
                "Công thức tính % khối lượng nguyên tố và Lập công thức hóa học",
                F("Phần trăm khối lượng nguyên tố trong hợp chất A_x B_y", "$\\%m_A = \\dfrac{x \\cdot M_A}{\\text{KLPT}(A_x B_y)} \\cdot 100\\%; \\qquad \\%m_A + \\%m_B = 100\\%$", "Tổng phần trăm khối lượng của tất cả các nguyên tố trong một hợp chất luôn bằng $100\\%$."),
                F("Tìm chỉ số nguyên tử (x, y) khi biết % khối lượng và KLPT", "$x = \\dfrac{\\%m_A \\cdot \\text{KLPT}}{100 \\cdot M_A}; \\qquad x : y = \\dfrac{\\%m_A}{M_A} : \\dfrac{\\%m_B}{M_B}$", "Các chỉ số $x, y$ trong công thức hóa học phải là những số nguyên dương."),
            )
        ],
        example="Phân bón đạm ammonium nitrate có công thức hóa học là $\\text{NH}_4\\text{NO}_3$ (gồm $2$ nguyên tử $\\text{N}$, $4$ nguyên tử $\\text{H}$ và $3$ nguyên tử $\\text{O}$). Biết $\\text{N} = 14, \\text{H} = 1, \\text{O} = 16$. Hãy tính khối lượng phân tử của $\\text{NH}_4\\text{NO}_3$ và phần trăm khối lượng của nguyên tố dinh dưỡng Nitrogen ($\\text{N}$) trong loại phân đạm này.",
        example_answer="Trong $1$ phân tử $\\text{NH}_4\\text{NO}_3$ có tổng cộng $2$ nguyên tử $\\text{N}$, $4$ nguyên tử $\\text{H}$ và $3$ nguyên tử $\\text{O}$. Khối lượng phân tử là $\\text{KLPT} = 2 \\cdot 14 + 4 \\cdot 1 + 3 \\cdot 16 = 28 + 4 + 48 = 80\\text{ amu}$. Phần trăm khối lượng của nguyên tố $\\text{N}$ trong $\\text{NH}_4\\text{NO}_3$ là $\\%m_{\\text{N}} = \\dfrac{2 \\cdot 14}{80} \\cdot 100\\% = \\dfrac{28}{80} \\cdot 100\\% = 35\\%$.",
        real_life="Khi mua phân đạm bón cho cây trồng, người nông dân so sánh phần trăm khối lượng nguyên tố $\\text{N}$ trong đạm urea ($(\\text{NH}_2)_2\\text{CO}$ có $\\%m_{\\text{N}} = 46{,}67\\%$) và đạm hai lá ($\\text{NH}_4\\text{NO}_3$ có $\\%m_{\\text{N}} = 35\\%$) để tính đúng lượng phân cần bón.",
        quiz=[
            mcq("biet", "Trong hợp chất có công thức hóa học $A_x B_y$ (với khối lượng nguyên tử là $M_A, M_B$ và khối lượng phân tử là $M = x M_A + y M_B$), công thức tính phần trăm khối lượng của nguyên tố $A$ là gì?", ["$\\%m_A = \\dfrac{x \\cdot M_A}{M} \\cdot 100\\%$", "$\\%m_A = \\dfrac{M_A}{M} \\cdot 100\\%$", "$\\%m_A = \\dfrac{x}{x + y} \\cdot 100\\%$", "$\\%m_A = \\dfrac{M}{x \\cdot M_A} \\cdot 100\\%$"], 0, "Phần trăm khối lượng của nguyên tố $A$ bằng khối lượng của $x$ nguyên tử $A$ chia cho khối lượng phân tử $M$ nhân với $100\\%$."),
            mcq("biet", "Biết $\\text{Cu} = 64\\text{ amu}$ và $\\text{O} = 16\\text{ amu}$. Trong hợp chất copper(II) oxide có công thức $\\text{CuO}$ ($\\text{KLPT} = 80\\text{ amu}$), phần trăm khối lượng của nguyên tố Copper ($\\text{Cu}$) và Oxygen ($\\text{O}$) lần lượt là:", ["$\\%m_{\\text{Cu}} = 80\\%$ và $\\%m_{\\text{O}} = 20\\%$", "$\\%m_{\\text{Cu}} = 50\\%$ và $\\%m_{\\text{O}} = 50\\%$", "$\\%m_{\\text{Cu}} = 64\\%$ và $\\%m_{\\text{O}} = 16\\%$", "$\\%m_{\\text{Cu}} = 20\\%$ và $\\%m_{\\text{O}} = 80\\%$"], 0, "Ta có $\\%m_{\\text{Cu}} = \\dfrac{64}{64 + 16} \\cdot 100\\% = \\dfrac{64}{80} \\cdot 100\\% = 80\\%$ và $\\%m_{\\text{O}} = 100\\% - 80\\% = 20\\%$."),
            mcq("hieu", "Một hợp chất khí tạo bởi nguyên tố Sulfur ($\\text{S} = 32$) và Oxygen ($\\text{O} = 16$) có khối lượng phân tử là $64\\text{ amu}$, trong đó nguyên tố $\\text{S}$ chiếm $50\\%$ về khối lượng. Công thức hóa học của hợp chất khí này là gì?", ["$\\text{SO}_2$", "$\\text{SO}_3$", "$\\text{SO}$", "$\\text{S}_2\\text{O}_3$"], 0, "Số nguyên tử $\\text{S}$ là $x = \\dfrac{50 \\cdot 64}{100 \\cdot 32} = 1$; số nguyên tử $\\text{O}$ là $y = \\dfrac{50 \\cdot 64}{100 \\cdot 16} = 2$. Vậy công thức là $\\text{SO}_2$."),
            tf4("hieu", "Cho $\\text{H} = 1, \\text{C} = 12, \\text{O} = 16, \\text{Ca} = 40, \\text{Fe} = 56$. Xét tính đúng/sai của các phát biểu sau:", [
                "Trong hợp chất đá vôi $\\text{CaCO}_3$ ($\\text{KLPT} = 100\\text{ amu}$), phần trăm khối lượng của $\\text{Ca}$ là $40\\%$, của $\\text{C}$ là $12\\%$ và của $\\text{O}$ là $48\\%$.",
                "Trong phân tử methane $\\text{CH}_4$ ($\\text{KLPT} = 16\\text{ amu}$), nguyên tố Carbon chiếm $75\\%$ về khối lượng và Hydrogen chiếm $25\\%$ về khối lượng.",
                "Trong phân tử nước $\\text{H}_2\\text{O}$, vì có $2$ nguyên tử $\\text{H}$ và $1$ nguyên tử $\\text{O}$ nên phần trăm khối lượng của $\\text{H}$ lớn gấp đôi phần trăm khối lượng của $\\text{O}$.",
                "Trong quặng hematite chứa $\\text{Fe}_2\\text{O}_3$ ($\\text{KLPT} = 160\\text{ amu}$), phần trăm khối lượng của sắt ($\\text{Fe}$) là $\\dfrac{2 \\cdot 56}{160} \\cdot 100\\% = 70\\%$.",
            ], [True, True, False, True], "Ý c) sai vì trong $\\text{H}_2\\text{O}$ ($18\\text{ amu}$), khối lượng $2\\text{H}$ là $2\\text{ amu}$ ($\\approx 11{,}1\\%$) nhỏ hơn nhiều so với khối lượng $1\\text{O}$ là $16\\text{ amu}$ ($\\approx 88{,}9\\%$)."),
            short("vandung", "Biết $\\text{C} = 12\\text{ amu}$ và $\\text{H} = 1\\text{ amu}$. Trong hợp chất khí methane có công thức $\\text{CH}_4$ ($\\text{KLPT} = 16\\text{ amu}$), phần trăm khối lượng của nguyên tố Carbon ($\\text{C}$) bằng bao nhiêu phần trăm ($\\%$)?", ["75"], "Áp dụng công thức $\\%m_{\\text{C}} = \\dfrac{12}{12 + 4 \\cdot 1} \\cdot 100\\% = \\dfrac{12}{16} \\cdot 100\\% = 75\\%$.", unit="%"),
        ],
    ),
]


from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("chemistry", 7, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
