"""KHTN 9 (phần Hóa học - Chất và sự biến đổi của chất) — Kết nối tri thức.
Cấu trúc: Lớp 9 -> 4 Chương -> 16 Bài học độc lập.
Mỗi bài có đúng công thức của bài đó, 3+ yêu cầu cần đạt, 10 câu hỏi.
"""
from ._helpers import bai, F, G, mcq, tf, short

GRADE = 9

# =========================================================================
# CHƯƠNG 1: KIM LOẠI VÀ SỰ KHÁC NHAU CƠ BẢN GIỮA PHI KIM VÀ KIM LOẠI
# =========================================================================
CH1_ID = "hoa9_ch1"
CH1_TITLE = "Chương 1: Kim loại và phi kim"
CH1_DESC = "Tính chất vật lí, hóa học của kim loại, dãy hoạt động hóa học, tách kim loại, hợp kim và sự khác nhau giữa phi kim với kim loại"

CH1_LESSONS = [
    bai(1, "Tính chất chung của kim loại",
        "Tính dẻo, dẫn điện, dẫn nhiệt, ánh kim và phản ứng của kim loại với phi kim, dung dịch acid, dung dịch muối",
        "Kim loại có các tính chất vật lí chung: tính dẻo, tính dẫn điện, tính dẫn nhiệt và ánh kim (do các electron tự do trong mạng tinh thể kim loại gây ra). Về tính chất hóa học, hầu hết kim loại tác dụng với oxygen tạo oxide ($2\\text{Mg} + \\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{MgO}$), tác dụng với phi kim khác tạo muối ($\\text{Fe} + \\text{S} \\xrightarrow{t^\\circ} \\text{FeS}$), kim loại hoạt động đứng trước $\\text{H}$ tác dụng với dung dịch acid ($\\text{HCl}, \\text{H}_2\\text{SO}_4$ loãng) giải phóng $\\text{H}_2$, và kim loại mạnh đẩy kim loại yếu hơn ra khỏi dung dịch muối.",
        [
            F("Phản ứng với oxygen", "2\\text{Mg} + \\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{MgO};\\quad 3\\text{Fe} + 2\\text{O}_2 \\xrightarrow{t^\\circ} \\text{Fe}_3\\text{O}_4", "Hầu hết kim loại (trừ Au, Ag, Pt) tác dụng với O2"),
            F("Phản ứng với acid loãng", "\\text{M} + n\\text{HCl} \\rightarrow \\text{MCl}_n + \\frac{n}{2}\\text{H}_2\\uparrow", "Điều kiện: Kim loại M đứng trước H trong dãy hoạt động hóa học"),
            F("Phản ứng với dung dịch muối", "\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}\\downarrow", "Kim loại mạnh hơn (trừ K, Na, Ca, Ba) đẩy kim loại yếu hơn ra khỏi muối"),
        ],
        [
            "Nêu được tính chất vật lí chung của kim loại (tính dẻo, dẫn điện, dẫn nhiệt, ánh kim) và ứng dụng tương ứng",
            "Trình bày được tính chất hóa học cơ bản của kim loại: tác dụng với phi kim, dung dịch acid loãng, dung dịch muối",
            "Viết được các phương trình hóa học minh họa tính chất hóa học của kim loại",
        ],
        "Cho $5,6\\text{ g}$ sắt ($\\text{Fe}$) tác dụng hoàn toàn với dung dịch $\\text{HCl}$ dư. Tính thể tích khí $\\text{H}_2$ thu được ở đkc ($25^\\circ\\text{C}, 1\\text{ bar}$).",
        "Số mol $\\text{Fe}$: $n_{\\text{Fe}} = \\frac{5,6}{56} = 0,1\\text{ mol}$.\nPTHH: $\\text{Fe} + 2\\text{HCl} \\rightarrow \\text{FeCl}_2 + \\text{H}_2\\uparrow$.\nTheo PTHH: $n_{\\text{H}_2} = n_{\\text{Fe}} = 0,1\\text{ mol} \\Rightarrow V_{\\text{H}_2} = 0,1 \\cdot 24,79 = 2,479\\text{ L}$.",
        "Đồng ($\\text{Cu}$) và nhôm ($\\text{Al}$) dẫn điện tốt nên làm lõi dây điện; bạc ($\\text{Ag}$) dẫn nhiệt và phản xạ ánh sáng tốt nên dùng tráng gương, làm ruột phích.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Kim loại nào sau đây dẫn điện tốt nhất trong tất cả các kim loại?", "Bạc ($\\text{Ag}$)", ["Bạc ($\\text{Ag}$)", "Đồng ($\\text{Cu}$)", "Vàng ($\\text{Au}$)", "Nhôm ($\\text{Al}$)"], "Thứ tự dẫn điện giảm dần: $\\text{Ag} > \\text{Cu} > \\text{Au} > \\text{Al} > \\text{Fe}$.", "biet"),
            mcq("Đốt cháy dây sắt ($\\text{Fe}$) trong bình chứa khí oxygen ($\\text{O}_2$) dư thu được sản phẩm chính là:", "$\\text{Fe}_3\\text{O}_4$", ["$\\text{FeO}$", "$\\text{Fe}_2\\text{O}_3$", "$\\text{Fe}_3\\text{O}_4$", "$\\text{Fe(OH)}_3$"], "Phương trình: $3\\text{Fe} + 2\\text{O}_2 \\xrightarrow{t^\\circ} \\text{Fe}_3\\text{O}_4$ (oxide sắt từ).", "hieu"),
            short("Cho $6,5\\text{ g}$ kẽm ($\\text{Zn} = 65$) tác dụng hết với dung dịch $\\text{H}_2\\text{SO}_4$ loãng dư. Tính số mol khí $\\text{H}_2$ thu được.", "0,1", ["0,1", "0.1"], "PTHH: $\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2\\uparrow$. Số mol $n_{\\text{H}_2} = n_{\\text{Zn}} = \\frac{6,5}{65} = 0,1\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(2, "Dãy hoạt động hóa học của kim loại",
        "Thứ tự dãy hoạt động hóa học và ý nghĩa trong dự đoán chiều phản ứng của kim loại với nước, acid và dung dịch muối",
        "Dãy hoạt động hóa học của một số kim loại thông dụng sắp xếp theo chiều mức độ hoạt động hóa học giảm dần: $\\text{K}, \\text{Na}, \\text{Ca}, \\text{Mg}, \\text{Al}, \\text{Zn}, \\text{Fe}, \\text{Pb}, (\\text{H}), \\text{Cu}, \\text{Ag}, \\text{Au}$. Ý nghĩa: (1) Kim loại đứng đầu dãy ($\\text{K}, \\text{Na}, \\text{Ca}$) tác dụng mạnh với nước ở nhiệt độ thường tạo dung dịch base (kiềm) và giải phóng $\\text{H}_2$; (2) Kim loại đứng trước $\\text{H}$ phản ứng với dung dịch acid loãng giải phóng $\\text{H}_2$; (3) Kim loại đứng trước (trừ kim loại tan trong nước) đẩy kim loại đứng sau ra khỏi dung dịch muối của chúng.",
        [
            F("Dãy hoạt động hóa học", "\\text{K} > \\text{Na} > \\text{Ca} > \\text{Mg} > \\text{Al} > \\text{Zn} > \\text{Fe} > \\text{Pb} > (\\text{H}) > \\text{Cu} > \\text{Ag} > \\text{Au}", "Mức độ hoạt động hóa học giảm dần từ trái sang phải"),
            F("Kim loại kiềm tác dụng với nước", "2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2\\uparrow", "Xảy ra ngay ở nhiệt độ thường với K, Na, Ca, Ba"),
            F("Điều kiện đẩy muối", "\\text{M}_{\\text{trước}} + \\text{Muối của M}_{\\text{sau}} \\rightarrow \\text{Muối của M}_{\\text{trước}} + \\text{M}_{\\text{sau}}\\downarrow", "M trước không tác dụng trực tiếp với nước (từ Mg trở đi)"),
        ],
        [
            "Trình bày được thứ tự dãy hoạt động hóa học của các kim loại phổ biến",
            "Nêu được ý nghĩa của dãy hoạt động hóa học của kim loại",
            "Vận dụng dãy hoạt động hóa học để dự đoán sản phẩm khi cho kim loại vào nước, dung dịch acid và dung dịch muối",
        ],
        "Nêu hiện tượng và viết phương trình hóa học khi cho một mẩu nhỏ kim loại sodium ($\\text{Na}$) vào cốc đựng dung dịch $\\text{CuSO}_4$.",
        "Mẩu $\\text{Na}$ nóng chảy thành giọt tròn chạy trên mặt nước, sủi bọt khí không màu ($\\text{H}_2$), đồng thời xuất hiện kết tủa màu xanh lam ($\\text{Cu(OH)}_2$):\\n(1) $2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2\\uparrow$.\\n(2) $2\\text{NaOH} + \\text{CuSO}_4 \\rightarrow \\text{Cu(OH)}_2\\downarrow + \\text{Na}_2\\text{SO}_4$.",
        "Giải thích vì sao vàng ($\\text{Au}$), bạc ($\\text{Ag}$) đứng cuối dãy hoạt động hóa học nên tồn tại bền vững trong tự nhiên và giữ được vẻ sáng bóng lâu dài.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Kim loại nào sau đây KHÔNG phản ứng với dung dịch $\\text{HCl}$ loãng?", "Đồng ($\\text{Cu}$)", ["Đồng ($\\text{Cu}$)", "Kẽm ($\\text{Zn}$)", "Sắt ($\\text{Fe}$)", "Magnesium ($\\text{Mg}$)"], "$\\text{Cu}$ đứng sau $\\text{H}$ trong dãy hoạt động hóa học nên không tác dụng với dung dịch $\\text{HCl}$.", "biet"),
            mcq("Nhúng một đinh sắt ($\\text{Fe}$) sạch vào dung dịch $\\text{CuSO}_4$ màu xanh lam. Hiện tượng quan sát được là:", "Có lớp đồng màu đỏ bám ngoài đinh sắt, màu xanh của dung dịch nhạt dần", ["Có lớp đồng màu đỏ bám ngoài đinh sắt, màu xanh của dung dịch nhạt dần", "Sủi bọt khí không màu và không có kết tủa", "Không có hiện tượng gì xảy ra", "Xuất hiện kết tủa màu trắng xanh"], "PTHH: $\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}\\downarrow$ (đỏ).", "hieu"),
            short("Trong các kim loại: $\\text{Mg}, \\text{Cu}, \\text{Ag}, \\text{Zn}, \\text{Fe}$, có bao nhiêu kim loại tác dụng được với dung dịch $\\text{H}_2\\text{SO}_4$ loãng giải phóng khí $\\text{H}_2$?", "3", ["3"], "Có $3$ kim loại đứng trước $\\text{H}$ là $\\text{Mg}, \\text{Zn}, \\text{Fe}$ (còn $\\text{Cu}, \\text{Ag}$ đứng sau $\\text{H}$).", "vandung"),
        ]
    ),
    bai(3, "Tách kim loại và việc sử dụng hợp kim",
        "Phương pháp điện phân nóng chảy, nhiệt luyện, thủy luyện để tách kim loại và khái niệm, ưu điểm của hợp kim (gang, thép, duralumin)",
        "Trong tự nhiên, hầu hết kim loại tồn tại ở dạng hợp chất (oxide, muối) trong quặng, trừ $\\text{Au}, \\text{Pt}$ ở dạng tự do. Tùy mức độ hoạt động hóa học, người ta dùng: (1) Phương pháp điện phân nóng chảy để điều chế kim loại hoạt động mạnh ($\\text{K}, \\text{Na}, \\text{Ca}, \\text{Mg}, \\text{Al}$); (2) Phương pháp nhiệt luyện (dùng $\\text{C}, \\text{CO}, \\text{H}_2, \\text{Al}$ khử oxide kim loại ở nhiệt độ cao) để điều chế kim loại hoạt động trung bình ($\\text{Zn}, \\text{Fe}, \\text{Pb}, \\text{Cu}$). Hợp kim là vật liệu kim loại có chứa một kim loại cơ bản và một số kim loại hoặc phi kim khác (như gang, thép là hợp kim của $\\text{Fe}$ với $\\text{C}$), thường cứng, bền và chống ăn mòn tốt hơn kim loại nguyên chất.",
        [
            F("Điện phân nóng chảy Al2O3", "2\\text{Al}_2\\text{O}_3 \\xrightarrow{\\text{đpnc, cryolite}} 4\\text{Al} + 3\\text{O}_2\\uparrow", "Tách nhôm từ quặng bauxite"),
            F("Nhiệt luyện tách sắt và kẽm", "\\text{Fe}_2\\text{O}_3 + 3\\text{CO} \\xrightarrow{t^\\circ} 2\\text{Fe} + 3\\text{CO}_2;\\quad \\text{ZnO} + \\text{C} \\xrightarrow{t^\\circ} \\text{Zn} + \\text{CO}", "Khử oxide kim loại trung bình bằng CO hoặc C ở nhiệt độ cao"),
            F("Thành phần carbon trong Gang và Thép", "\\%m_{\\text{C (Thép)}} < 2\\% < \\%m_{\\text{C (Gang)}} \\le 5\\%", "Luyện thép là quá trình giảm hàm lượng C và tạp chất (Si, S, P, Mn) trong gang"),
        ],
        [
            "Nêu được nguyên tắc và các phương pháp cơ bản tách kim loại ra khỏi hợp chất (điện phân nóng chảy, nhiệt luyện)",
            "Trình bày được khái niệm hợp kim và giải thích vì sao hợp kim được sử dụng phổ biến hơn kim loại tinh khiết",
            "Phân biệt được thành phần, tính chất và ứng dụng của gang, thép, hợp kim nhôm (duralumin) và thép không gỉ (inox)",
        ],
        "Khử hoàn toàn $16\\text{ g}$ $\\text{Fe}_2\\text{O}_3$ bằng khí $\\text{CO}$ dư ở nhiệt độ cao. Tính khối lượng sắt ($\\text{Fe}$) thu được.",
        "Số mol $\\text{Fe}_2\\text{O}_3$: $n_{\\text{Fe}_2\\text{O}_3} = \\frac{16}{160} = 0,1\\text{ mol}$.\\nPTHH: $\\text{Fe}_2\\text{O}_3 + 3\\text{CO} \\xrightarrow{t^\\circ} 2\\text{Fe} + 3\\text{CO}_2$.\\nTheo PTHH: $n_{\\text{Fe}} = 2n_{\\text{Fe}_2\\text{O}_3} = 0,2\\text{ mol} \\Rightarrow m_{\\text{Fe}} = 0,2 \\cdot 56 = 11,2\\text{ g}$.",
        "Thép không gỉ (inox, chứa $\\text{Fe}, \\text{Cr}, \\text{Ni}, \\text{C}$) không bị gỉ sét dùng làm dụng cụ y tế, xoong nồi; hợp kim duralumin ($\\text{Al}-\\text{Cu}-\\text{Mg}-\\text{Mn}$) nhẹ và siêu bền dùng chế tạo vỏ máy bay.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Phương pháp thích hợp để tách kim loại nhôm ($\\text{Al}$) từ quặng bauxite ($\\text{Al}_2\\text{O}_3$) trong công nghiệp là:", "Điện phân nóng chảy $\\text{Al}_2\\text{O}_3$ có mặt cryolite", ["Điện phân nóng chảy $\\text{Al}_2\\text{O}_3$ có mặt cryolite", "Dùng khí $\\text{CO}$ khử $\\text{Al}_2\\text{O}_3$ ở nhiệt độ cao", "Cho $\\text{Fe}$ đẩy $\\text{Al}$ ra khỏi dung dịch muối", "Nhiệt phân $\\text{Al(OH)}_3$"], "$\\text{Al}$ là kim loại hoạt động mạnh nên chỉ điều chế bằng điện phân nóng chảy $\\text{Al}_2\\text{O}_3$.", "biet"),
            mcq("Hợp kim thép là hợp kim của sắt ($\\text{Fe}$) với carbon ($\\text{C}$) và một số nguyên tố khác, trong đó hàm lượng carbon chiếm:", "Dưới $2\\%$ về khối lượng", ["Dưới $2\\%$ về khối lượng", "Từ $2\\%$ đến $5\\%$ về khối lượng", "Trên $10\\%$ về khối lượng", "Đúng $50\\%$ về khối lượng"], "Thép có hàm lượng $\\text{C} < 2\\%$, còn gang có hàm lượng $\\text{C}$ từ $2\\% - 5\\%$.", "hieu"),
            short("Điện phân nóng chảy hoàn toàn $10,2\\text{ tấn}$ $\\text{Al}_2\\text{O}_3$ ($M = 102$) thu được tối đa bao nhiêu tấn nhôm ($\\text{Al} = 27$)?", "5,4", ["5,4", "5.4"], "Ta có $n_{\\text{Al}_2\\text{O}_3} = 0,1\\text{ Mmol} \\Rightarrow n_{\\text{Al}} = 0,2\\text{ Mmol} \\Rightarrow m_{\\text{Al}} = 0,2 \\cdot 27 = 5,4\\text{ tấn}$.", "vandung"),
        ]
    ),
    bai(4, "Sự khác nhau cơ bản giữa phi kim và kim loại",
        "Tính chất của carbon, lưu huỳnh, chlorine và so sánh sự khác nhau về tính chất vật lí, hóa học giữa phi kim và kim loại",
        "Phi kim ở điều kiện thường tồn tại ở cả $3$ thể: rắn (carbon $\\text{C}$, lưu huỳnh $\\text{S}$, phosphorus $\\text{P}$), lỏng (bromine $\\text{Br}_2$), khí (oxygen $\\text{O}_2$, nitrogen $\\text{N}_2$, chlorine $\\text{Cl}_2$, hydrogen $\\text{H}_2$). Phần lớn phi kim không dẫn điện (trừ than chì), không dẫn nhiệt, không có ánh kim và có nhiệt độ nóng chảy thấp hơn kim loại. Về hóa học, trong phản ứng với kim loại, kim loại dễ nhường electron tạo ion dương (cation), còn phi kim dễ nhận electron tạo ion âm (anion); oxide của kim loại thường là oxide base ($\\text{CaO}, \\text{Na}_2\\text{O}$), còn oxide của phi kim thường là oxide acid ($\\text{CO}_2, \\text{SO}_2, \\text{P}_2\\text{O}_5$).",
        [
            F("Phản ứng giữa kim loại và phi kim", "2\\text{Na} + \\text{Cl}_2 \\xrightarrow{t^\\circ} 2\\text{NaCl};\\quad \\text{Fe} + \\text{S} \\xrightarrow{t^\\circ} \\text{FeS}", "Kim loại nhường electron, phi kim nhận electron"),
            F("Oxide phi kim (oxide acid) + Nước", "\\text{SO}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{SO}_3;\\quad \\text{P}_2\\text{O}_5 + 3\\text{H}_2\\text{O} \\rightarrow 2\\text{H}_3\\text{PO}_4", "Đa số oxide phi kim tác dụng với nước tạo dung dịch acid"),
            F("Khí chlorine tác dụng với dung dịch kiềm", "\\text{Cl}_2 + 2\\text{NaOH} \\rightarrow \\text{NaCl} + \\text{NaClO} + \\text{H}_2\\text{O}", "Điều chế nước Javel dùng tẩy trắng và khử trùng"),
        ],
        [
            "Nêu được ứng dụng của một số đơn chất phi kim quan trọng: carbon (than chì, kim cương, than hoạt tính), lưu huỳnh, chlorine",
            "So sánh được sự khác nhau cơ bản về tính chất vật lí (trạng thái, tính dẫn điện, dẫn nhiệt, nhiệt độ nóng chảy) giữa phi kim và kim loại",
            "Phân biệt được sự khác nhau về tính chất hóa học cơ bản giữa phi kim và kim loại (khả năng tạo ion, bản chất của oxide)",
        ],
        "So sánh bản chất của $\\text{Na}_2\\text{O}$ (oxide của kim loại $\\text{Na}$) và $\\text{SO}_2$ (oxide của phi kim $\\text{S}$) khi cho tác dụng với nước và thử bằng giấy quỳ tím.",
        "$\\text{Na}_2\\text{O}$ là oxide base, tác dụng với nước tạo dung dịch kiềm làm quỳ tím hóa xanh: $\\text{Na}_2\\text{O} + \\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH}$.\\n$\\text{SO}_2$ là oxide acid, tác dụng với nước tạo dung dịch acid làm quỳ tím hóa đỏ: $\\text{SO}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{SO}_3$.",
        "Than hoạt tính có tính hấp phụ cao dùng trong mặt nạ phòng độc và máy lọc nước; lưu huỳnh dùng lưu hóa cao su; chlorine dùng khử trùng nước sinh hoạt và sản xuất nhựa PVC.",
        CH1_ID, CH1_TITLE, CH1_DESC,
        extra_questions=[
            mcq("Ở điều kiện thường, đơn chất phi kim nào sau đây tồn tại ở trạng thái lỏng?", "Bromine ($\\text{Br}_2$)", ["Bromine ($\\text{Br}_2$)", "Chlorine ($\\text{Cl}_2$)", "Lưu huỳnh ($\\text{S}$)", "Iodine ($\\text{I}_2$)"], "Trong các phi kim, chỉ có bromine ($\\text{Br}_2$) tồn tại ở thể lỏng (màu nâu đỏ) ở điều kiện thường.", "biet"),
            mcq("Dạng thù hình nào của nguyên tố carbon ($\\text{C}$) có khả năng dẫn điện tốt?", "Than chì (graphite)", ["Than chì (graphite)", "Kim cương", "Than gỗ", "Than muội"], "Than chì có cấu trúc lớp với các electron tự do di chuyển được nên dẫn điện tốt, dùng làm điện cực.", "hieu"),
            short("Đốt cháy hoàn toàn $3,2\\text{ g}$ lưu huỳnh ($\\text{S} = 32$) trong khí $\\text{O}_2$ dư. Tính số mol khí $\\text{SO}_2$ tạo thành.", "0,1", ["0,1", "0.1"], "PTHH: $\\text{S} + \\text{O}_2 \\xrightarrow{t^\\circ} \\text{SO}_2$. Số mol $n_{\\text{SO}_2} = n_{\\text{S}} = \\frac{3,2}{32} = 0,1\\text{ mol}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 2: GIỚI THIỆU VỀ CHẤT HỮU CƠ. HYDROCARBON VÀ NGUỒN NHIÊN LIỆU
# =========================================================================
CH2_ID = "hoa9_ch2"
CH2_TITLE = "Chương 2: Hydrocarbon và nguồn nhiên liệu"
CH2_DESC = "Hợp chất hữu cơ, công thức cấu tạo, alkane (methane), alkene (ethylene) và nguồn nhiên liệu dầu mỏ, khí thiên nhiên"

CH2_LESSONS = [
    bai(5, "Giới thiệu về chất hữu cơ",
        "Khái niệm hợp chất hữu cơ, phân loại hydrocarbon với dẫn xuất của hydrocarbon và công thức cấu tạo",
        "Hợp chất hữu cơ là hợp chất của carbon (trừ $\\text{CO}, \\text{CO}_2, \\text{H}_2\\text{CO}_3$, các muối carbonate, cyanide, carbide...). Dựa vào thành phần nguyên tố, hợp chất hữu cơ được chia thành $2$ loại chính: (1) Hydrocarbon (phân tử chỉ chứa $2$ nguyên tố $\\text{C}$ và $\\text{H}$ như $\\text{CH}_4, \\text{C}_2\\text{H}_4, \\text{C}_6\\text{H}_6$); (2) Dẫn xuất của hydrocarbon (ngoài $\\text{C}, \\text{H}$ còn có nguyên tố khác như $\\text{O}, \\text{N}, \\text{Cl}$... ví dụ $\\text{C}_2\\text{H}_5\\text{OH}, \\text{CH}_3\\text{COOH}, \\text{CH}_3\\text{Cl}$). Trong hợp chất hữu cơ, carbon luôn có hóa trị $\\text{IV}$, hydrogen có hóa trị $\\text{I}$, oxygen có hóa trị $\\text{II}$. Công thức cấu tạo biểu diễn thứ tự và cách thức liên kết giữa các nguyên tử trong phân tử.",
        [
            F("Phân loại hợp chất hữu cơ", "\\text{HCHC} = \\begin{cases} \\text{Hydrocarbon: } \\text{C}_x\\text{H}_y \\\\ \\text{Dẫn xuất HC: } \\text{C}_x\\text{H}_y\\text{O}_z\\text{N}_t\\text{X}_u \\end{cases}", "Hydrocarbon chỉ gồm C và H; dẫn xuất chứa thêm O, N, halogen..."),
            F("Hóa trị trong hợp chất hữu cơ", "\\text{C (IV)},\\quad \\text{H (I)},\\quad \\text{O (II)},\\quad \\text{Cl (I)}", "Mỗi đơn vị hóa trị được biểu diễn bằng 1 nét gạch liên kết"),
            F("Công thức cấu tạo thu gọn của ethanol", "\\text{CH}_3-\\text{CH}_2-\\text{OH}", "Cùng công thức phân tử C2H6O còn có đồng phân CH3-O-CH3"),
        ],
        [
            "Nêu được khái niệm hợp chất hữu cơ và hóa học hữu cơ",
            "Phân biệt được chất vô cơ với chất hữu cơ, hydrocarbon với dẫn xuất của hydrocarbon dựa vào công thức phân tử",
            "Trình bày được ý nghĩa của công thức cấu tạo và viết được công thức cấu tạo của một số chất hữu cơ đơn giản",
        ],
        "Trong các chất sau: $\\text{CH}_4, \\text{CaCO}_3, \\text{C}_2\\text{H}_6\\text{O}, \\text{CO}_2, \\text{C}_2\\text{H}_4, \\text{CH}_3\\text{Cl}$. Hãy chỉ ra đâu là hydrocarbon và đâu là dẫn xuất của hydrocarbon.",
        "- Các chất vô cơ: $\\text{CaCO}_3, \\text{CO}_2$.\\n- Hydrocarbon (chỉ chứa $\\text{C}$ và $\\text{H}$): $\\text{CH}_4, \\text{C}_2\\text{H}_4$.\\n- Dẫn xuất của hydrocarbon (chứa thêm $\\text{O}, \\text{Cl}$): $\\text{C}_2\\text{H}_6\\text{O}, \\text{CH}_3\\text{Cl}$.",
        "Hợp chất hữu cơ có mặt ở khắp nơi: trong lương thực thực phẩm (tinh bột, đường, chất đạm, chất béo), quần áo (sợi bông, polyester), thuốc chữa bệnh và chất dẻo.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Chất nào sau đây là một hydrocarbon?", "$\\text{C}_2\\text{H}_4$", ["$\\text{C}_2\\text{H}_4$", "$\\text{C}_2\\text{H}_5\\text{OH}$", "$\\text{CH}_3\\text{COOH}$", "$\\text{Na}_2\\text{CO}_3$"], "Hydrocarbon là hợp chất hữu cơ mà phân tử chỉ chứa carbon ($\\text{C}$) và hydrogen ($\\text{H}$).", "biet"),
            mcq("Trong các hợp chất hữu cơ, nguyên tử carbon ($\\text{C}$) luôn có hóa trị bằng:", "$\\text{IV}$", ["$\\text{IV}$", "$\\text{II}$", "$\\text{III}$", "$\\text{I}$"], "Nguyên tử $\\text{C}$ luôn có hóa trị $\\text{IV}$ (ứng với $4$ gạch liên kết xung quanh nguyên tử $\\text{C}$).", "hieu"),
            short("Ứng với công thức phân tử $\\text{C}_2\\text{H}_6\\text{O}$ có bao nhiêu công thức cấu tạo mạch hở khác nhau?", "2", ["2"], "Có $2$ công thức cấu tạo: $\\text{CH}_3-\\text{CH}_2-\\text{OH}$ (ethylic alcohol) và $\\text{CH}_3-\\text{O}-\\text{CH}_3$ (dimethyl ether).", "vandung"),
        ]
    ),
    bai(6, "Alkane",
        "Khái niệm alkane, công thức chung CnH2n+2, cấu tạo và phản ứng cháy của methane (CH4), butane (C4H10)",
        "Alkane là những hydrocarbon mạch hở, trong phân tử chỉ chứa các liên kết đơn ($\\text{C}-\\text{C}$ và $\\text{C}-\\text{H}$), có công thức phân tử chung là $\\text{C}_n\\text{H}_{2n+2}$ ($n \\ge 1$). Bốn alkane đầu dãy là methane ($\\text{CH}_4$), ethane ($\\text{C}_2\\text{H}_6$), propane ($\\text{C}_3\\text{H}_8$), butane ($\\text{C}_4\\text{H}_{10}$) đều là chất khí không màu, nhẹ hơn hoặc nặng hơn không khí, hầu như không tan trong nước. Khi đốt cháy hoàn toàn trong oxygen, alkane tạo thành khí $\\text{CO}_2$, hơi nước $\\text{H}_2\\text{O}$ và tỏa nhiều nhiệt, nên được dùng làm nhiên liệu (khí thiên nhiên, khí biogas, khí bình gas LPG).",
        [
            F("Công thức chung của Alkane", "\\text{C}_n\\text{H}_{2n+2}\\quad (n \\ge 1,\\; n \\in \\mathbb{N}^*)", "Chỉ chứa liên kết đơn trong phân tử"),
            F("Phản ứng đốt cháy Alkane", "\\text{C}_n\\text{H}_{2n+2} + \\frac{3n+1}{2}\\text{O}_2 \\xrightarrow{t^\\circ} n\\text{CO}_2 + (n+1)\\text{H}_2\\text{O}", "Đặc trưng: số mol H2O luôn lớn hơn số mol CO2 và n_alkane = n_H2O - n_CO2"),
            F("Đốt cháy Methane", "\\text{CH}_4 + 2\\text{O}_2 \\xrightarrow{t^\\circ} \\text{CO}_2 + 2\\text{H}_2\\text{O}", "Hỗn hợp V_CH4 : V_O2 = 1 : 2 là hỗn hợp nổ mạnh"),
        ],
        [
            "Nêu được khái niệm alkane, công thức chung $\\text{C}_n\\text{H}_{2n+2}$ ($n \\ge 1$) và gọi tên được $4$ alkane đầu dãy ($\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8, \\text{C}_4\\text{H}_{10}$)",
            "Viết được công thức cấu tạo và trình bày được tính chất vật lí, phản ứng đốt cháy tỏa nhiệt của methane và butane",
            "Trình bày được ứng dụng làm nhiên liệu của alkane trong đời sống và sản xuất",
        ],
        "Đốt cháy hoàn toàn $4,958\\text{ L}$ khí methane ($\\text{CH}_4$) ở đkc. Tính thể tích khí $\\text{O}_2$ cần dùng (đkc) và khối lượng $\\text{H}_2\\text{O}$ tạo thành.",
        "Số mol $\\text{CH}_4$: $n_{\\text{CH}_4} = \\frac{4,958}{24,79} = 0,2\\text{ mol}$.\\nPTHH: $\\text{CH}_4 + 2\\text{O}_2 \\xrightarrow{t^\\circ} \\text{CO}_2 + 2\\text{H}_2\\text{O}$.\\n- $n_{\\text{O}_2} = 2n_{\\text{CH}_4} = 0,4\\text{ mol} \\Rightarrow V_{\\text{O}_2} = 0,4 \\cdot 24,79 = 9,916\\text{ L}$.\\n- $n_{\\text{H}_2\\text{O}} = 2n_{\\text{CH}_4} = 0,4\\text{ mol} \\Rightarrow m_{\\text{H}_2\\text{O}} = 0,4 \\cdot 18 = 7,2\\text{ g}$.",
        "Khí biogas sinh ra từ hầm ủ chất thải chăn nuôi chứa chủ yếu khí methane ($\\text{CH}_4$); bình gas đun bếp gia đình chứa hỗn hợp hóa lỏng của propane ($\\text{C}_3\\text{H}_8$) và butane ($\\text{C}_4\\text{H}_{10}$).",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Công thức phân tử của butane là:", "$\\text{C}_4\\text{H}_{10}$", ["$\\text{C}_4\\text{H}_{10}$", "$\\text{C}_3\\text{H}_8$", "$\\text{C}_2\\text{H}_6$", "$\\text{C}_4\\text{H}_8$"], "Butane là alkane có $n = 4 \\Rightarrow \\text{C}_4\\text{H}_{2\\cdot 4+2} = \\text{C}_4\\text{H}_{10}$.", "biet"),
            mcq("Trong phân tử methane ($\\text{CH}_4$) có chứa:", "$4$ liên kết đơn $\\text{C}-\\text{H}$", ["$4$ liên kết đơn $\\text{C}-\\text{H}$", "$1$ liên kết đôi và $2$ liên kết đơn", "$3$ liên kết đơn và $1$ liên kết đôi", "$2$ liên kết đơn $\\text{C}-\\text{C}$"], "Nguyên tử $\\text{C}$ liên kết với $4$ nguyên tử $\\text{H}$ bằng $4$ liên kết đơn $\\text{C}-\\text{H}$.", "hieu"),
            short("Đốt cháy hoàn toàn $0,15\\text{ mol}$ ethane ($\\text{C}_2\\text{H}_6$) thu được bao nhiêu mol khí $\\text{CO}_2$?", "0,3", ["0,3", "0.3"], "Bảo toàn nguyên tố $\\text{C}$: $n_{\\text{CO}_2} = 2n_{\\text{C}_2\\text{H}_6} = 2 \\cdot 0,15 = 0,3\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(7, "Alkene",
        "Khái niệm alkene, cấu tạo có liên kết đôi C=C của ethylene (C2H4), phản ứng cộng làm mất màu nước bromine và phản ứng trùng hợp",
        "Alkene là những hydrocarbon mạch hở, trong phân tử có một liên kết đôi $\\text{C}=\\text{C}$, có công thức phân tử chung là $\\text{C}_n\\text{H}_{2n}$ ($n \\ge 2$). Chất tiêu biểu là ethylene ($\\text{C}_2\\text{H}_4$, công thức cấu tạo $\\text{CH}_2=\\text{CH}_2$), là chất khí không màu, không mùi, ít tan trong nước, nhẹ hơn không khí. Trong liên kết đôi $\\text{C}=\\text{C}$ có một liên kết kém bền dễ bị đứt ra trong các phản ứng hóa học, nên ngoài phản ứng cháy, ethylene dễ tham gia phản ứng cộng (làm mất màu dung dịch nước bromine $\\text{Br}_2$, cộng $\\text{H}_2$) và phản ứng trùng hợp tạo thành nhựa polyethylene (PE).",
        [
            F("Công thức chung của Alkene", "\\text{C}_n\\text{H}_{2n}\\quad (n \\ge 2,\\; n \\in \\mathbb{N}^*)", "Có 1 liên kết đôi C=C trong phân tử"),
            F("Phản ứng cộng nước bromine", "\\text{CH}_2=\\text{CH}_2 + \\text{Br}_2 \\rightarrow \\text{BrCH}_2-\\text{CH}_2\\text{Br}", "Dung dịch nước bromine màu da cam bị mất màu (dùng nhận biết alkene)"),
            F("Phản ứng trùng hợp tạo nhựa PE", "n\\,\\text{CH}_2=\\text{CH}_2 \\xrightarrow{t^\\circ, p, xt} (-\\text{CH}_2-\\text{CH}_2-)_n", "Tổng hợp polyethylene (PE) từ ethylene"),
        ],
        [
            "Nêu được khái niệm alkene, công thức chung $\\text{C}_n\\text{H}_{2n}$ ($n \\ge 2$) và viết được công thức cấu tạo của ethylene ($\\text{CH}_2=\\text{CH}_2$)",
            "Trình bày được tính chất hóa học đặc trưng của ethylene: phản ứng cháy, phản ứng làm mất màu nước bromine và phản ứng trùng hợp tạo PE",
            "Trình bày được ứng dụng của ethylene: kích thích quả mau chín, sản xuất nhựa PE và ethylic alcohol",
        ],
        "Dẫn $3,7185\\text{ L}$ hỗn hợp khí gồm $\\text{CH}_4$ và $\\text{C}_2\\text{H}_4$ (ở đkc) đi chậm qua bình đựng dung dịch nước $\\text{Br}_2$ dư thì thấy khối lượng bình tăng thêm $1,4\\text{ g}$. Tính phần trăm thể tích mỗi khí trong hỗn hợp đầu.",
        "Tổng số mol hỗn hợp: $n_{\\text{hh}} = \\frac{3,7185}{24,79} = 0,15\\text{ mol}$.\\nChỉ có $\\text{C}_2\\text{H}_4$ phản ứng và bị giữ lại trong bình $\\text{Br}_2$: $m_{\\text{C}_2\\text{H}_4} = 1,4\\text{ g} \\Rightarrow n_{\\text{C}_2\\text{H}_4} = \\frac{1,4}{28} = 0,05\\text{ mol}$.\\nPhần trăm thể tích: $\\%V_{\\text{C}_2\\text{H}_4} = \\frac{0,05}{0,15} \\cdot 100\\% = 33,33\\%$; $\\%V_{\\text{CH}_4} = 66,67\\%$.",
        "Khi xếp quả chín chung với quả xanh, quả chín tiết ra một lượng nhỏ khí ethylene ($\\text{C}_2\\text{H}_4$) có tác dụng kích thích các quả xanh xung quanh mau chín đều.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Thuốc thử dùng để phân biệt khí ethylene ($\\text{C}_2\\text{H}_4$) và khí methane ($\\text{CH}_4$) là:", "Dung dịch nước bromine ($\\text{Br}_2$)", ["Dung dịch nước bromine ($\\text{Br}_2$)", "Dung dịch $\\text{NaCl}$", "Nước vôi trong $\\text{Ca(OH)}_2$", "Quỳ tím ẩm"], "$\\text{C}_2\\text{H}_4$ có liên kết đôi nên làm mất màu dung dịch nước $\\text{Br}_2$, còn $\\text{CH}_4$ không phản ứng.", "biet"),
            mcq("Trùng hợp hoàn toàn các phân tử ethylene ($\\text{CH}_2=\\text{CH}_2$) ở điều kiện nhiệt độ, áp suất và xúc tác thích hợp thu được polymer nào?", "Polyethylene (PE)", ["Polyethylene (PE)", "Polypropylene (PP)", "Poly(vinyl chloride) (PVC)", " Tinh bột"], "Phương trình: $n\\,\\text{CH}_2=\\text{CH}_2 \\xrightarrow{t^\\circ, p, xt} (-\\text{CH}_2-\\text{CH}_2-)_n$ (polyethylene - PE).", "hieu"),
            short("Dẫn khí ethylene ($\\text{C}_2\\text{H}_4$) dư qua bình đựng dung dịch chứa $0,2\\text{ mol}$ $\\text{Br}_2$. Tính số mol $\\text{C}_2\\text{H}_4\\text{Br}_2$ tạo thành.", "0,2", ["0,2", "0.2"], "PTHH: $\\text{C}_2\\text{H}_4 + \\text{Br}_2 \\rightarrow \\text{C}_2\\text{H}_4\\text{Br}_2$. Số mol $n_{\\text{C}_2\\text{H}_4\\text{Br}_2} = n_{\\text{Br}_2} = 0,2\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(8, "Nguồn nhiên liệu",
        "Thành phần, chế biến và sử dụng dầu mỏ, khí thiên nhiên, khí mỏ dầu và nhiên liệu sinh học bảo vệ môi trường",
        "Nhiên liệu hóa thạch gồm than mỏ, dầu mỏ và khí thiên nhiên. Dầu mỏ là hỗn hợp lỏng sánh, màu nâu đen, nhẹ hơn nước, không tan trong nước, gồm hàng trăm hydrocarbon khác nhau. Chưng cất phân đoạn dầu mỏ thu được khí đốt, xăng, dầu hỏa, dầu diesel, dầu nhờn và nhựa đường; để tăng lượng xăng người ta dùng phương pháp cracking (bẻ gãy mạch carbon dài thành mạch ngắn). Khí thiên nhiên và khí mỏ dầu có thành phần chính là methane ($\\text{CH}_4$, chiếm $75\\% - 95\\%$). Sử dụng nhiên liệu hiệu quả và chuyển sang nhiên liệu xanh (xăng sinh học E5, biogas) giúp giảm phát thải khí nhà kính $\\text{CO}_2$.",
        [
            F("Phương pháp chưng cất dầu mỏ", "\\text{Dầu thô} \\xrightarrow{\\text{chưng cất phân đoạn}} \\text{Khí đốt, Xăng, Dầu hỏa, Diesel, Mazut, Nhựa đường}", "Dựa vào sự khác nhau về nhiệt độ sôi của các phân đoạn hydrocarbon"),
            F("Phản ứng Cracking (minh họa)", "\\text{C}_{16}\\text{H}_{34} \\xrightarrow{\\text{cracking (xt, } t^\\circ\\text{)}} \\text{C}_8\\text{H}_{18} + \\text{C}_8\\text{H}_{16}", "Bẻ gãy alkane mạch dài thành alkane và alkene mạch ngắn hơn để làm xăng"),
            F("Thành phần chính của Khí thiên nhiên", "\\%V_{\\text{CH}_4 (\\text{Khí thiên nhiên})} \\approx 95\\% > \\%V_{\\text{CH}_4 (\\text{Khí mỏ dầu})} \\approx 75\\%", "Khí thiên nhiên chứa hàm lượng methane cao hơn khí mỏ dầu"),
        ],
        [
            "Trình bày được trạng thái tự nhiên, tính chất vật lí và thành phần của dầu mỏ, khí thiên nhiên và khí mỏ dầu",
            "Nêu được các sản phẩm chính của quá trình chưng cất dầu mỏ và ý nghĩa của phản ứng cracking",
            "Trình bày được các biện pháp sử dụng nhiên liệu an toàn, hiệu quả và bảo vệ môi trường",
        ],
        "Khi tàu chở dầu gặp sự cố tràn dầu trên biển, dầu mỏ chìm xuống đáy biển hay nổi lên trên mặt nước? Giải thích và nêu cách xử lí cơ bản.",
        "Dầu mỏ nhẹ hơn nước ($D < 1\\text{ g/cm}^3$) và không tan trong nước nên sẽ nổi lên tạo thành lớp váng dầu loang rộng trên mặt biển, ngăn cản sự hòa tan oxygen vào nước biển. Để xử lí, người ta dùng phao quây vùng dầu tràn rồi hút dầu lên hoặc dùng chất hấp phụ chuyên dụng.",
        "Xăng sinh học E5 là hỗn hợp gồm $95\\%$ xăng truyền thống và $5\\%$ ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$) theo thể tích, giúp đốt cháy triệt để hơn và giảm khí thải độc hại.",
        CH2_ID, CH2_TITLE, CH2_DESC,
        extra_questions=[
            mcq("Thành phần chính của khí thiên nhiên và khí mỏ dầu là:", "Methane ($\\text{CH}_4$)", ["Methane ($\\text{CH}_4$)", "Ethylene ($\\text{C}_2\\text{H}_4$)", "Carbon dioxide ($\\text{CO}_2$)", "Hydrogen ($\\text{H}_2$)"], "Methane ($\\text{CH}_4$) là thành phần chủ yếu của khí thiên nhiên (khoảng $95\\%$) và khí mỏ dầu (khoảng $75\\%$).", "biet"),
            mcq("Để làm tăng hàm lượng xăng thu được từ các phân đoạn dầu nặng (như dầu mazut), trong công nghiệp lọc dầu người ta sử dụng phương pháp hóa học nào?", "Phương pháp cracking", ["Phương pháp cracking", "Phương pháp lọc cơ học", "Phương pháp lắng gạn", "Phương pháp kết tinh"], "Cracking là quá trình bẻ gãy phân tử hydrocarbon mạch dài thành các phân tử hydrocarbon mạch ngắn hơn (cỡ xăng).", "hieu"),
            short("Để pha chế $100\\text{ L}$ xăng sinh học E5 (chứa $5\\%$ thể tích ethylic alcohol), cần dùng bao nhiêu lít ethylic alcohol nguyên chất?", "5", ["5"], "Thể tích ethylic alcohol trong $100\\text{ L}$ xăng E5 là $100 \\cdot 5\\% = 5\\text{ L}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 3: ETHYLIC ALCOHOL VÀ ACETIC ACID
# =========================================================================
CH3_ID = "hoa9_ch3"
CH3_TITLE = "Chương 3: Ethylic alcohol và Acetic acid"
CH3_DESC = "Cấu tạo, độ cồn, tính chất hóa học và điều chế ethylic alcohol (C2H5OH), acetic acid (CH3COOH) và phản ứng ester hóa"

CH3_LESSONS = [
    bai(9, "Ethylic alcohol",
        "Công thức cấu tạo CH3-CH2-OH, khái niệm độ cồn, phản ứng cháy, phản ứng với Na và điều chế ethylic alcohol",
        "Ethylic alcohol (ethanol) có công thức phân tử $\\text{C}_2\\text{H}_6\\text{O}$ và công thức cấu tạo thu gọn $\\text{CH}_3-\\text{CH}_2-\\text{OH}$ (hoặc $\\text{C}_2\\text{H}_5\\text{OH}$), trong đó nhóm $-\\text{OH}$ gây ra tính chất hóa học đặc trưng. Đó là chất lỏng không màu, sôi ở $78,3^\\circ\\text{C}$, nhẹ hơn nước ($D \\approx 0,8\\text{ g/mL}$) và tan vô hạn trong nước. Độ cồn là số mililít ethylic alcohol nguyên chất có trong $100\\text{ mL}$ dung dịch ở $20^\\circ\\text{C}$. Ethylic alcohol cháy tỏa nhiều nhiệt với ngọn lửa xanh mờ, tác dụng với kim loại hoạt động mạnh ($\\text{Na}, \\text{K}$) giải phóng khí $\\text{H}_2$, và được điều chế bằng cách lên men tinh bột hoặc cộng nước vào ethylene.",
        [
            F("Công thức tính Độ cồn", "\\text{Độ cồn} = \\frac{V_{\\text{C}_2\\text{H}_5\\text{OH}}}{V_{\\text{dung dịch}}} \\cdot 100^\\circ", "Số mL rượu nguyên chất có trong 100 mL hỗn hợp rượu với nước"),
            F("Phản ứng thế với kim loại Na", "2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{Na} \\rightarrow 2\\text{C}_2\\text{H}_5\\text{ONa} + \\text{H}_2\\uparrow", "Nguyên tử Na thế nguyên tử H linh động trong nhóm -OH"),
            F("Phản ứng đốt cháy và Điều chế", "\\text{C}_2\\text{H}_5\\text{OH} + 3\\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{CO}_2 + 3\\text{H}_2\\text{O};\\quad \\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{enzyme}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2", "Đốt cháy tỏa nhiệt mạnh; điều chế từ lên men glucose hoặc hydrate hóa C2H4"),
        ],
        [
            "Viết được công thức phân tử, công thức cấu tạo của ethylic alcohol và nêu được đặc điểm nhóm chức $-\\text{OH}$",
            "Trình bày được tính chất vật lí, khái niệm độ cồn và tính toán được lượng cồn trong dung dịch",
            "Viết được phương trình hóa học của phản ứng đốt cháy, phản ứng với $\\text{Na}$ và phản ứng điều chế ethylic alcohol",
        ],
        "Cho $9,2\\text{ g}$ ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$) nguyên chất tác dụng với lượng dư kim loại $\\text{Na}$. Tính thể tích khí $\\text{H}_2$ thoát ra ở đkc.",
        "Số mol $\\text{C}_2\\text{H}_5\\text{OH}$: $n = \\frac{9,2}{46} = 0,2\\text{ mol}$.\\nPTHH: $2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{Na} \\rightarrow 2\\text{C}_2\\text{H}_5\\text{ONa} + \\text{H}_2\\uparrow$.\\nTheo PTHH: $n_{\\text{H}_2} = \\frac{1}{2}n_{\\text{C}_2\\text{H}_5\\text{OH}} = 0,1\\text{ mol} \\Rightarrow V_{\\text{H}_2} = 0,1 \\cdot 24,79 = 2,479\\text{ L}$.",
        "Cồn y tế $70^\\circ$ có khả năng thẩm thấu qua màng tế bào vi khuẩn tốt nhất nên được dùng để sát khuẩn vết thương và khử trùng dụng cụ y tế.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Nhóm nguyên tử nào trong phân tử $\\text{CH}_3-\\text{CH}_2-\\text{OH}$ gây nên tính chất hóa học đặc trưng của ethylic alcohol?", "Nhóm $-\\text{OH}$", ["Nhóm $-\\text{OH}$", "Nhóm $-\\text{CH}_3$", "Nhóm $-\\text{CH}_2-$", "Liên kết $\\text{C}-\\text{C}$"], "Nhóm hydroxyl ($-\\text{OH}$) có nguyên tử $\\text{H}$ linh động quyết định tính chất đặc trưng của alcohol.", "biet"),
            mcq("Trên nhãn một chai cồn y tế có ghi $70^\\circ$. Ý nghĩa của con số này là:", "Trong $100\\text{ mL}$ cồn y tế có chứa $70\\text{ mL}$ ethylic alcohol nguyên chất", ["Trong $100\\text{ mL}$ cồn y tế có chứa $70\\text{ mL}$ ethylic alcohol nguyên chất", "Nhiệt độ sôi của cồn là $70^\\circ\\text{C}$", "Trong $100\\text{ g}$ dung dịch có $70\\text{ g}$ rượu nguyên chất", "Pha $70\\text{ mL}$ rượu với $100\\text{ mL}$ nước"], "Độ cồn là số $\\text{mL}$ ethylic alcohol nguyên chất có trong $100\\text{ mL}$ dung dịch.", "hieu"),
            short("Trong $250\\text{ mL}$ dung dịch cồn $40^\\circ$ có chứa bao nhiêu mililít ethylic alcohol nguyên chất?", "100", ["100"], "Thể tích $\\text{C}_2\\text{H}_5\\text{OH}$ nguyên chất: $V = \\frac{250 \\cdot 40}{100} = 100\\text{ mL}$.", "vandung"),
        ]
    ),
    bai(10, "Acetic acid",
        "Công thức cấu tạo CH3-COOH, tính acid yếu, phản ứng ester hóa với ethylic alcohol và điều chế giấm ăn",
        "Acetic acid có công thức phân tử $\\text{C}_2\\text{H}_4\\text{O}_2$ và công thức cấu tạo thu gọn $\\text{CH}_3-\\text{COOH}$, trong đó nhóm carboxyl ($-\\text{COOH}$) quyết định tính chất hóa học đặc trưng. Đó là chất lỏng không màu, vị chua, tan vô hạn trong nước; dung dịch acetic acid $2\\% - 5\\%$ được dùng làm giấm ăn. Acetic acid là một acid hữu cơ có đầy đủ tính chất của một acid: làm quỳ tím hóa đỏ, tác dụng với kim loại đứng trước $\\text{H}$, base, oxide base và muối carbonate. Đặc biệt, acetic acid tác dụng với ethylic alcohol (xúc tác $\\text{H}_2\\text{SO}_4$ đặc, đun nóng) tạo ra ethyl acetate có mùi thơm (phản ứng ester hóa).",
        [
            F("Tính chất của một Acid", "2\\text{CH}_3\\text{COOH} + \\text{CaCO}_3 \\rightarrow (\\text{CH}_3\\text{COO})_2\\text{Ca} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}", "Dùng giấm ăn tẩy cặn vôi CaCO3 trong ấm đun nước"),
            F("Phản ứng Ester hóa", "\\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH} \\underset{t^\\circ}{\\overset{\\text{H}_2\\text{SO}_4\\text{ đặc}}{\\rightleftharpoons}} \\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O}", "Phản ứng thuận nghịch tạo thành ethyl acetate có mùi thơm, ít tan trong nước"),
            F("Lên men giấm từ rượu nhạt", "\\text{C}_2\\text{H}_5\\text{OH} + \\text{O}_2 \\xrightarrow{\\text{men giấm}} \\text{CH}_3\\text{COOH} + \\text{H}_2\\text{O}", "Phương pháp truyền thống sản xuất giấm ăn"),
        ],
        [
            "Viết được công thức phân tử, công thức cấu tạo của acetic acid và nhận diện được nhóm chức $-\\text{COOH}$",
            "Trình bày được tính chất hóa học của acetic acid: tính acid và phản ứng ester hóa với ethylic alcohol",
            "Trình bày được phương pháp điều chế acetic acid bằng cách lên men dung dịch ethylic alcohol loãng và ứng dụng của acetic acid",
        ],
        "Đun nóng $12\\text{ g}$ $\\text{CH}_3\\text{COOH}$ với lượng dư $\\text{C}_2\\text{H}_5\\text{OH}$ có mặt $\\text{H}_2\\text{SO}_4$ đặc làm xúc tác. Tính khối lượng ester $\\text{CH}_3\\text{COOC}_2\\text{H}_5$ thu được biết hiệu suất phản ứng đạt $60\\%$.",
        "Số mol $\\text{CH}_3\\text{COOH}$: $n = \\frac{12}{60} = 0,2\\text{ mol}$.\\nPTHH: $\\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH} \\rightleftharpoons \\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O}$.\\nVới hiệu suất $H = 60\\%$: $n_{\\text{ester}} = 0,2 \\cdot 60\\% = 0,12\\text{ mol}$.\\nKhối lượng ethyl acetate ($M = 88$): $m = 0,12 \\cdot 88 = 10,56\\text{ g}$.",
        "Dùng giấm ăn (dung dịch $\\text{CH}_3\\text{COOH}$ $2\\% - 5\\%$) ngâm vào ấm đun nước bị đóng cặn vôi ($\\text{CaCO}_3$) qua đêm sẽ hòa tan sạch lớp cặn mà không làm hỏng ấm.",
        CH3_ID, CH3_TITLE, CH3_DESC,
        extra_questions=[
            mcq("Nhóm nguyên tử nào gây nên tính acid đặc trưng của phân tử acetic acid ($\\text{CH}_3\\text{COOH}$)?", "Nhóm $-\\text{COOH}$", ["Nhóm $-\\text{COOH}$", "Nhóm $-\\text{CH}_3$", "Nhóm $-\\text{OH}$", "Nhóm $-\\text{CHO}$"], "Nhóm carboxyl ($-\\text{COOH}$) phân li ra ion $\\text{H}^+$ tạo nên tính chất acid của acetic acid.", "biet"),
            mcq("Chất nào sau đây vừa tác dụng được với kim loại $\\text{Na}$, vừa tác dụng được với đá vôi ($\\text{CaCO}_3$) sủi bọt khí?", "$\\text{CH}_3\\text{COOH}$", ["$\\text{CH}_3\\text{COOH}$", "$\\text{C}_2\\text{H}_5\\text{OH}$", "$\\text{CH}_3\\text{COOC}_2\\text{H}_5$", "$\\text{C}_2\\text{H}_4$"], "$\\text{CH}_3\\text{COOH}$ là acid nên tác dụng được với cả $\\text{Na}$ và muối carbonate $\\text{CaCO}_3$ (còn $\\text{C}_2\\text{H}_5\\text{OH}$ chỉ tác dụng với $\\text{Na}$).", "hieu"),
            short("Để trung hòa vừa đủ dung dịch chứa $0,15\\text{ mol}$ $\\text{CH}_3\\text{COOH}$ cần dùng bao nhiêu mol $\\text{NaOH}$?", "0,15", ["0,15", "0.15"], "PTHH: $\\text{CH}_3\\text{COOH} + \\text{NaOH} \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O}$. Số mol $n_{\\text{NaOH}} = n_{\\text{CH}_3\\text{COOH}} = 0,15\\text{ mol}$.", "vandung"),
        ]
    ),
]

# =========================================================================
# CHƯƠNG 4: LIPID. CARBOHYDRATE. PROTEIN. POLYMER
# =========================================================================
CH4_ID = "hoa9_ch4"
CH4_TITLE = "Chương 4: Lipid, Carbohydrate, Protein và Polymer"
CH4_DESC = "Chất béo (lipid), glucose, saccharose, tinh bột, cellulose, protein và vật liệu polymer (chất dẻo, tơ, cao su)"

CH4_LESSONS = [
    bai(11, "Lipid và chất béo",
        "Khái niệm lipid, cấu tạo chất béo là triester của glycerol với acid béo và phản ứng xà phòng hóa",
        "Lipid là những hợp chất hữu cơ có trong tế bào sống, không tan trong nước nhưng tan trong các dung môi hữu cơ không phân cực (xăng, benzene, chloroform), bao gồm chất béo, sáp, steroid, phospholipid. Chất béo là triester của glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$) với các acid béo (như stearic acid $\\text{C}_{17}\\text{H}_{35}\\text{COOH}$, palmitic acid $\\text{C}_{15}\\text{H}_{31}\\text{COOH}$, oleic acid $\\text{C}_{17}\\text{H}_{33}\\text{COOH}$), có công thức chung $(R\\text{COO})_3\\text{C}_3\\text{H}_5$. Đun nóng chất béo với dung dịch kiềm ($\\text{NaOH}$ hoặc $\\text{KOH}$) thu được glycerol và muối của acid béo (xà phòng) — gọi là phản ứng xà phòng hóa.",
        [
            F("Công thức chung của Chất béo", "(R\\text{COO})_3\\text{C}_3\\text{H}_5", "R là gốc hydrocarbon của acid béo (C17H35-, C15H31-, C17H33-...)"),
            F("Phản ứng thủy phân trong môi trường acid", "(R\\text{COO})_3\\text{C}_3\\text{H}_5 + 3\\text{H}_2\\text{O} \\underset{t^\\circ}{\\overset{\\text{H}^+}{\\rightleftharpoons}} 3R\\text{COOH} + \\text{C}_3\\text{H}_5(\\text{OH})_3", "Phản ứng thuận nghịch thu được acid béo và glycerol"),
            F("Phản ứng xà phòng hóa", "(R\\text{COO})_3\\text{C}_3\\text{H}_5 + 3\\text{NaOH} \\xrightarrow{t^\\circ} 3R\\text{COONa} + \\text{C}_3\\text{H}_5(\\text{OH})_3", "Phản ứng một chiều dùng sản xuất xà phòng (RCOONa) và glycerol"),
        ],
        [
            "Nêu được khái niệm lipid, khái niệm chất béo và trạng thái, tính chất vật lí của chất béo (nhẹ hơn nước, không tan trong nước)",
            "Viết được phương trình hóa học của phản ứng thủy phân chất béo trong môi trường acid và phản ứng xà phòng hóa",
            "Trình bày được vai trò của chất béo đối với cơ thể và cách sử dụng chất béo hợp lí để phòng bệnh béo phì, tim mạch",
        ],
        "Xà phòng hóa hoàn toàn $89\\text{ g}$ chất béo tristearin ($(\\text{C}_{17}\\text{H}_{35}\\text{COO})_3\\text{C}_3\\text{H}_5$, $M = 890$) bằng dung dịch $\\text{NaOH}$ vừa đủ. Tính khối lượng glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$, $M = 92$) thu được.",
        "Số mol chất béo: $n_{\\text{chất béo}} = \\frac{89}{890} = 0,1\\text{ mol}$.\\nTheo PTHH xà phòng hóa: $n_{\\text{glycerol}} = n_{\\text{chất béo}} = 0,1\\text{ mol}$.\\nKhối lượng glycerol thu được: $m = 0,1 \\cdot 92 = 9,2\\text{ g}$.",
        "Dầu thực vật chứa nhiều gốc acid béo không no nên ở thể lỏng, tốt cho tim mạch hơn mỡ động vật (chứa nhiều gốc acid béo no ở thể rắn); dầu mỡ rán đi rán lại nhiều lần ở nhiệt độ cao dễ bị oxi hóa sinh ra chất độc hại.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Khi đun nóng chất béo với dung dịch $\\text{NaOH}$ dư (phản ứng xà phòng hóa), sản phẩm thu được gồm muối của các acid béo và chất nào sau đây?", "Glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$)", ["Glycerol ($\\text{C}_3\\text{H}_5(\\text{OH})_3$)", "Ethylic alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$)", "Acetic acid ($\\text{CH}_3\\text{COOH}$)", "Nước ($\\text{H}_2\\text{O}$)"], "Chất béo là triester của glycerol với acid béo nên khi xà phòng hóa luôn giải phóng glycerol.", "biet"),
            mcq("Vì sao khi quần áo bị dính vết dầu mỡ, giặt bằng nước sạch không hết nhưng giặt bằng xăng hoặc xà phòng lại sạch?", "Vì chất béo không tan trong nước nhưng tan tốt trong dung môi hữu cơ (xăng) và bị nhũ tương hóa bởi xà phòng", ["Vì chất béo không tan trong nước nhưng tan tốt trong dung môi hữu cơ (xăng) và bị nhũ tương hóa bởi xà phòng", "Vì chất béo nặng hơn nước nên bám chặt vào vải", "Vì chất béo tác dụng với nước tạo kết tủa", "Vì xăng làm bay hơi sợi vải"], "Chất béo là hợp chất không phân cực, không tan trong nước nhưng tan tốt trong xăng, dầu hỏa.", "hieu"),
            short("Để xà phòng hóa hoàn toàn $0,2\\text{ mol}$ một chất béo $(R\\text{COO})_3\\text{C}_3\\text{H}_5$ cần dùng tối thiểu bao nhiêu mol $\\text{NaOH}$?", "0,6", ["0,6", "0.6"], "Theo PTHH: $n_{\\text{NaOH}} = 3n_{\\text{chất béo}} = 3 \\cdot 0,2 = 0,6\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(12, "Glucose và Saccharose",
        "Công thức phân tử, trạng thái tự nhiên, phản ứng tráng bạc và lên men của glucose (C6H12O6) và thủy phân saccharose (C12H22O11)",
        "Glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$, $M = 180$) và saccharose ($\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$, $M = 342$) là các carbohydrate quan trọng, đều là chất rắn kết tinh, không màu, vị ngọt và dễ tan trong nước. Glucose có nhiều trong quả nho chín và trong máu người (nồng độ khoảng $0,1\\%$); glucose tham gia phản ứng tráng bạc với dung dịch $\\text{AgNO}_3/\\text{NH}_3$ đun nóng tạo kết tủa bạc ($\\text{Ag}$) sáng bóng và tham gia phản ứng lên men rượu tạo $\\text{C}_2\\text{H}_5\\text{OH}$. Saccharose có nhiều trong mía, củ cải đường, hoa thốt nốt; saccharose không có phản ứng tráng bạc nhưng bị thủy phân khi đun nóng với acid (hoặc enzyme) tạo ra glucose và fructose.",
        [
            F("Phản ứng tráng bạc của Glucose", "\\text{C}_6\\text{H}_{12}\\text{O}_6 + \\text{Ag}_2\\text{O} \\xrightarrow{\\text{NH}_3, t^\\circ} \\text{C}_6\\text{H}_{12}\\text{O}_7 + 2\\text{Ag}\\downarrow", "1 mol glucose tạo ra 2 mol bạc kết tủa (dùng tráng gương, tráng ruột phích)"),
            F("Lên men rượu từ Glucose", "\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{enzyme, } 30-35^\\circ\\text{C}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2\\uparrow", "Điều chế ethylic alcohol từ đường glucose"),
            F("Thủy phân Saccharose", "\\text{C}_{12}\\text{H}_{22}\\text{O}_{11} + \\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+, t^\\circ} \\text{C}_6\\text{H}_{12}\\text{O}_6\\text{ (glucose)} + \\text{C}_6\\text{H}_{12}\\text{O}_6\\text{ (fructose)}", "Saccharose thủy phân tạo 2 đồng phân glucose và fructose"),
        ],
        [
            "Nêu được công thức phân tử, trạng thái tự nhiên và tính chất vật lí của glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) và saccharose ($\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$)",
            "Trình bày được tính chất hóa học đặc trưng của glucose (phản ứng tráng bạc, lên men rượu) và của saccharose (phản ứng thủy phân)",
            "Phân biệt được dung dịch glucose và dung dịch saccharose bằng phương pháp hóa học",
        ],
        "Đun nóng dung dịch chứa $18\\text{ g}$ glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) với lượng dư dung dịch $\\text{AgNO}_3$ trong $\\text{NH}_3$. Tính khối lượng bạc ($\\text{Ag} = 108$) kết tủa thu được.",
        "Số mol glucose: $n_{\\text{C}_6\\text{H}_{12}\\text{O}_6} = \\frac{18}{180} = 0,1\\text{ mol}$.\\nTheo PTHH tráng bạc: $n_{\\text{Ag}} = 2n_{\\text{glucose}} = 2 \\cdot 0,1 = 0,2\\text{ mol}$.\\nKhối lượng bạc thu được: $m_{\\text{Ag}} = 0,2 \\cdot 108 = 21,6\\text{ g}$.",
        "Khi cơ thể bị suy nhược hoặc hạ đường huyết, bệnh nhân được truyền dịch đường glucose $5\\%$ để cung cấp năng lượng trực tiếp và nhanh chóng cho các tế bào.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Để phân biệt hai dung dịch không màu là glucose và saccharose, ta có thể đun nhẹ từng mẫu thử với thuốc thử nào sau đây?", "Dung dịch $\\text{AgNO}_3$ trong $\\text{NH}_3$", ["Dung dịch $\\text{AgNO}_3$ trong $\\text{NH}_3$", "Dung dịch $\\text{NaCl}$", "Quỳ tím", "Nước vôi trong"], "Glucose có phản ứng tráng bạc tạo lớp $\\text{Ag}$ sáng bóng, còn saccharose không có phản ứng tráng bạc.", "biet"),
            mcq("Khi thủy phân hoàn toàn saccharose ($\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$) trong môi trường acid đun nóng, sản phẩm thu được là:", "Glucose và fructose", ["Glucose và fructose", "Chỉ có glucose", "Ethylic alcohol và $\\text{CO}_2$", "Tinh bột và nước"], "Phương trình: $\\text{C}_{12}\\text{H}_{22}\\text{O}_{11} + \\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+, t^\\circ} \\text{Glucose} + \\text{Fructose}$.", "hieu"),
            short("Lên men hoàn toàn $90\\text{ g}$ glucose ($M = 180$) thu được tối đa bao nhiêu mol $\\text{C}_2\\text{H}_5\\text{OH}$?", "1", ["1", "1,0", "1.0"], "Ta có $n_{\\text{glucose}} = \\frac{90}{180} = 0,5\\text{ mol}$. Theo PTHH: $n_{\\text{C}_2\\text{H}_5\\text{OH}} = 2n_{\\text{glucose}} = 2 \\cdot 0,5 = 1\\text{ mol}$.", "vandung"),
        ]
    ),
    bai(13, "Tinh bột và Cellulose",
        "Công thức chung (C6H10O5)n, sự tạo thành qua quang hợp, phản ứng thủy phân và nhận biết hồ tinh bột bằng iodine",
        "Tinh bột và cellulose đều là những polymer thiên nhiên có công thức chung là $(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n$, nhưng có cấu trúc phân tử và giá trị $n$ khác nhau (hệ số $n$ của cellulose lớn hơn nhiều so với tinh bột). Tinh bột là chất rắn màu trắng, không tan trong nước lạnh nhưng trương phồng trong nước nóng tạo thành dung dịch keo gọi là hồ tinh bột; hồ tinh bột tác dụng với dung dịch iodine ($\\text{I}_2$) tạo màu xanh tím đặc trưng. Cellulose là chất rắn màu trắng, dạng sợi (có nhiều trong bông, gỗ, tre), không tan trong nước ngay cả khi đun nóng. Cả hai đều bị thủy phân đến cùng trong môi trường acid (hoặc enzyme) tạo thành glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$).",
        [
            F("Quá trình quang hợp tạo Tinh bột / Cellulose", "6n\\text{CO}_2 + 5n\\text{H}_2\\text{O} \\xrightarrow{\\text{ánh sáng, chất diệp lục}} (\\text{C}_6\\text{H}_{10}\\text{O}_5)_n + 6n\\text{O}_2\\uparrow", "Cây xanh tổng hợp tinh bột và cellulose từ CO2 và nước"),
            F("Phản ứng thủy phân hoàn toàn", "(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n + n\\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+\\text{ hoặc enzyme, } t^\\circ} n\\text{C}_6\\text{H}_{12}\\text{O}_6\\text{ (glucose)}", "Mỗi mắt xích C6H10O5 (M = 162) thủy phân tạo 1 phân tử glucose (M = 180)"),
            F("Phản ứng màu đặc trưng của Tinh bột", "\\text{Hồ tinh bột} + \\text{Dung dịch } \\text{I}_2 \\rightarrow \\text{Hợp chất màu xanh tím}", "Đun nóng mất màu, để nguội màu xanh tím xuất hiện trở lại"),
        ],
        [
            "Nêu được trạng thái tự nhiên, tính chất vật lí của tinh bột và cellulose",
            "Trình bày được tính chất hóa học của tinh bột và cellulose: phản ứng thủy phân tạo glucose và phản ứng màu của hồ tinh bột với iodine",
            "Nêu được sự tạo thành tinh bột, cellulose trong cây xanh nhờ quang hợp và ứng dụng của chúng trong đời sống, công nghiệp",
        ],
        "Thủy phân hoàn toàn $32,4\\text{ g}$ tinh bột trong môi trường acid đun nóng. Tính khối lượng glucose thu được biết hiệu suất phản ứng đạt $100\\%$.",
        "Tính theo $1$ mắt xích $\\text{C}_6\\text{H}_{10}\\text{O}_5$ ($M = 162$): $n_{\\text{C}_6\\text{H}_{10}\\text{O}_5} = \\frac{32,4}{162} = 0,2\\text{ mol}$.\\nPTHH: $(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n + n\\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+, t^\\circ} n\\text{C}_6\\text{H}_{12}\\text{O}_6$.\\nSố mol glucose: $n_{\\text{glucose}} = 0,2\\text{ mol} \\Rightarrow m_{\\text{glucose}} = 0,2 \\cdot 180 = 36\\text{ g}$.",
        "Khi nhai kĩ cơm trắng (chứa tinh bột), enzyme amylase trong nước bọt thủy phân một phần tinh bột thành đường maltose và glucose nên ta cảm thấy có vị ngọt.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Nhỏ vài giọt dung dịch cồn iodine ($\\text{I}_2$) lên mặt cắt của củ khoai lang hoặc lát bánh mì thì xuất hiện màu gì?", "Màu xanh tím", ["Màu xanh tím", "Màu đỏ gạch", "Màu vàng tươi", "Màu hồng nhạt"], "Trong khoai lang và bánh mì có chứa nhiều tinh bột, tác dụng với $\\text{I}_2$ tạo hợp chất màu xanh tím.", "biet"),
            mcq("Thành phần chính của sợi bông nõn (chiếm gần $98\\%$) dùng để dệt vải cotton là chất nào sau đây?", "Cellulose", ["Cellulose", "Tinh bột", "Saccharose", "Protein"], "Cellulose có cấu trúc dạng sợi bền chắc, chiếm tới $95\\% - 98\\%$ trong bông nõn và $40\\% - 50\\%$ trong gỗ.", "hieu"),
            short("Thủy phân hoàn toàn $162\\text{ g}$ cellulose (tính theo mắt xích $\\text{C}_6\\text{H}_{10}\\text{O}_5$ có $M = 162$) thu được tối đa bao nhiêu gam glucose ($M = 180$)?", "180", ["180"], "Ta có $n_{\\text{mắt xích}} = \\frac{162}{162} = 1\\text{ mol} \\Rightarrow n_{\\text{glucose}} = 1\\text{ mol} \\Rightarrow m_{\\text{glucose}} = 180\\text{ g}$.", "vandung"),
        ]
    ),
    bai(14, "Protein",
        "Khái niệm protein, cấu tạo từ các amino acid, phản ứng thủy phân, sự đông tụ và phân biệt tơ tằm với sợi bông",
        "Protein là những hợp chất hữu cơ thiên nhiên có khối lượng phân tử rất lớn (từ vài chục nghìn đến hàng triệu $\\text{amu}$), được tạo thành từ nhiều đơn vị amino acid liên kết với nhau bằng liên kết peptide. Protein có trong mọi bộ phận của cơ thể người và động vật (thịt, cá, trứng, sữa, máu, tóc, sừng) và một số thực vật (hạt đậu nành). Về tính chất, một số protein tan trong nước tạo dung dịch keo (như lòng trắng trứng) và bị đông tụ khi đun nóng hoặc khi cho thêm acid, base, cồn; khi thủy phân đến cùng tạo ra hỗn hợp các amino acid; khi đốt cháy protein có mùi khét như mùi tóc cháy.",
        [
            F("Cấu tạo phân tử Protein", "n\\,\\text{Amino acid} \\xrightarrow{- (n-1)\\text{H}_2\\text{O}} \\text{Chuỗi Polypeptide (Protein)}", "Các nguyên tố chính tạo nên protein là C, H, O, N (và một lượng nhỏ S, P, Fe...)"),
            F("Phản ứng thủy phân hoàn toàn Protein", "\\text{Protein} + n\\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+, \\text{OH}^-\\text{ hoặc enzyme, } t^\\circ} \\text{Hỗn hợp các Amino acid}", "Xảy ra trong dạ dày và ruột non khi tiêu hóa thức ăn giàu đạm"),
            F("Sự đông tụ Protein", "\\text{Dung dịch Protein (lòng trắng trứng)} \\xrightarrow{t^\\circ\\text{ hoặc acid, cồn}} \\text{Protein đông tụ}\\downarrow", "Giải thích hiện tượng luộc trứng hoặc vắt chanh vào sữa làm sữa kết tủa"),
        ],
        [
            "Nêu được khái niệm, đặc điểm cấu tạo phân tử (tạo bởi nhiều đơn vị amino acid) và vai trò của protein đối với cơ thể sống",
            "Trình bày được tính chất hóa học của protein: phản ứng thủy phân tạo amino acid, sự đông tụ bởi nhiệt/acid/cồn và sự phân hủy tạo mùi khét khi đốt",
            "Vận dụng dấu hiệu đốt cháy để phân biệt tơ tự nhiên có bản chất protein (tơ tằm, len lông cừu) với sợi bông (cellulose)",
        ],
        "Trình bày cách phân biệt một mảnh vải dệt bằng tơ tằm tự nhiên và một mảnh vải dệt bằng sợi bông (cotton).",
        "Lấy mỗi mảnh vải một sợi nhỏ đem đốt trên ngọn lửa đèn cồn:\\n- Sợi vải cháy có mùi khét như mùi tóc cháy và tạo tàn đen bóp vụn là vải tơ tằm (bản chất là protein).\\n- Sợi vải cháy nhanh, không có mùi khét và để lại tro trắng mịn là vải sợi bông (bản chất là cellulose).",
        "Khi nấu canh cua, protein tan trong nước cua bị đông tụ bởi nhiệt độ cao tạo thành từng mảng gạch cua nổi lên trên mặt nồi nước.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Khi thủy phân hoàn toàn protein trong môi trường acid hoặc nhờ xúc tác enzyme, sản phẩm cuối cùng thu được là:", "Các amino acid", ["Các amino acid", "Glucose", "Glycerol và acid béo", "Ethylic alcohol"], "Protein được cấu tạo từ các mắt xích amino acid nên khi thủy phân đến cùng sẽ thu được hỗn hợp các amino acid.", "biet"),
            mcq("Hiện tượng nào sau đây là ví dụ về sự đông tụ của protein?", "Lòng trắng trứng gà chuyển từ thể lỏng sang thể rắn màu trắng khi luộc chín", ["Lòng trắng trứng gà chuyển từ thể lỏng sang thể rắn màu trắng khi luộc chín", "Đường kính trắng tan hết khi khuấy vào nước ấm", "Mỡ lợn đông đặc lại khi để vào ngăn mát tủ lạnh", "Đá vôi sủi bọt khí khi nhỏ giấm ăn vào"], "Lòng trắng trứng chứa protein albumin bị đông tụ dưới tác dụng của nhiệt độ cao.", "hieu"),
            short("Trong $4$ nguyên tố hóa học bắt buộc phải có mặt trong mọi phân tử protein là $\\text{C}, \\text{H}, \\text{O}$ và nguyên tố $X$. Khối lượng nguyên tử (theo $\\text{amu}$) của nguyên tố $X$ là bao nhiêu?", "14", ["14"], "Mọi protein đều chứa $4$ nguyên tố cơ bản là $\\text{C}, \\text{H}, \\text{O}$ và $\\text{N}$ (nitrogen có khối lượng nguyên tử bằng $14\\text{ amu}$).", "vandung"),
        ]
    ),
    bai(15, "Polymer",
        "Khái niệm polymer, monomer, hệ số polymer hóa và phân loại vật liệu polymer (chất dẻo, tơ, cao su, vật liệu composite)",
        "Polymer là những hợp chất có khối lượng phân tử rất lớn do nhiều đơn vị nhỏ (gọi là mắt xích) liên kết với nhau tạo nên; các phân tử nhỏ ban đầu tạo nên polymer gọi là monomer, và số mắt xích $n$ trong phân tử polymer gọi là hệ số polymer hóa. Polymer được chia thành polymer thiên nhiên (tinh bột, cellulose, tơ tằm, cao su thiên nhiên) và polymer tổng hợp (PE, PP, PVC, nylon-6,6). Các vật liệu polymer gồm: (1) Chất dẻo (có tính dẻo); (2) Tơ (dạng sợi mảnh, bền); (3) Cao su (có tính đàn hồi); (4) Vật liệu composite (tổ hợp từ polymer nền và vật liệu cốt). Vì chất dẻo khó phân hủy sinh học, cần thực hiện nguyên tắc 3R (Tiết giảm - Tái sử dụng - Tái chế).",
        [
            F("Phản ứng trùng hợp tổng quát", "n\\,\\text{CH}_2=\\text{CH}-\\text{R} \\xrightarrow{t^\\circ, p, xt} (-\\text{CH}_2-\\text{CH}(\\text{R})-)_n", "Với R = -H là PE; R = -CH3 là PP; R = -Cl là PVC"),
            F("Hệ số polymer hóa (n)", "n = \\frac{M_{\\text{polymer}}}{M_{\\text{mắt xích}}}", "Cho biết số lượng mắt xích liên kết với nhau trong 1 phân tử polymer"),
            F("Nguyên tắc 3R giảm ô nhiễm rác thải nhựa", "\\text{3R} = \\text{Reduce (Tiết giảm)} + \\text{Reuse (Tái sử dụng)} + \\text{Recycle (Tái chế)}", "Giải pháp bảo vệ môi trường trước rác thải nhựa khó phân hủy"),
        ],
        [
            "Nêu được khái niệm polymer, monomer, mắt xích, hệ số polymer hóa và phân biệt được polymer thiên nhiên với polymer tổng hợp",
            "Trình bày được khái niệm, tính chất cơ bản và ứng dụng của chất dẻo, tơ, cao su và vật liệu composite",
            "Nêu được tác hại của rác thải nhựa đối với môi trường và các biện pháp hạn chế ô nhiễm nhựa",
        ],
        "Một phân tử polyethylene (PE) có công thức $(-\\text{CH}_2-\\text{CH}_2-)_n$ và có khối lượng phân tử là $56\\,000\\text{ amu}$. Tính hệ số polymer hóa $n$ của phân tử PE đó.",
        "Khối lượng của $1$ mắt xích $-\\text{CH}_2-\\text{CH}_2-$ là $M_{\\text{mắt xích}} = 28\\text{ amu}$.\\nHệ số polymer hóa: $n = \\frac{M_{\\text{PE}}}{M_{\\text{mắt xích}}} = \\frac{56\\,000}{28} = 2000$ mắt xích.",
        "Ống dẫn nước trong gia đình thường làm bằng nhựa PVC (poly(vinyl chloride)); hộp đựng thực phẩm dùng trong lò vi sóng thường làm bằng nhựa PP (polypropylene) chịu nhiệt an toàn.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Polymer nào sau đây thuộc loại polymer tổng hợp?", "Polyethylene (PE)", ["Polyethylene (PE)", "Tinh bột", "Cellulose", "Tơ tằm"], "PE được con người tổng hợp từ phản ứng trùng hợp ethylene; tinh bột, cellulose và tơ tằm là polymer thiên nhiên.", "biet"),
            mcq("Tính chất vật lí đặc trưng nhất của vật liệu cao su so với chất dẻo và tơ là:", "Tính đàn hồi", ["Tính đàn hồi", "Tính dẫn điện", "Tính tan tốt trong nước", "Tính giòn dễ vỡ"], "Cao su là vật liệu polymer có tính đàn hồi (biến dạng khi chịu lực tác dụng và trở lại hình dạng ban đầu khi thôi tác dụng lực).", "hieu"),
            short("Một đoạn mạch poly(vinyl chloride) (PVC) có công thức $(-\\text{CH}_2-\\text{CHCl}-)_n$ (với $M_{\\text{mắt xích}} = 62,5\\text{ amu}$) có khối lượng phân tử là $62\\,500\\text{ amu}$. Hệ số polymer hóa $n$ của đoạn mạch này là bao nhiêu?", "1000", ["1000"], "Ta có $n = \\frac{62\\,500}{62,5} = 1000$.", "vandung"),
        ]
    ),
    bai(16, "Vỏ Trái Đất và khai thác tài nguyên từ vỏ Trái Đất",
        "Thành phần nguyên tố trong vỏ Trái Đất, khai thác đá vôi (CaCO3), quặng bauxite, cát thạch anh (SiO2) và phát triển bền vững",
        "Vỏ Trái Đất được cấu tạo từ các khoáng vật và đá, trong đó các nguyên tố phổ biến nhất về khối lượng là oxygen ($\\text{O} \\approx 46,6\\%$), silicon ($\\text{Si} \\approx 27,7\\%$), aluminium ($\\text{Al} \\approx 8,1\\%$), sắt ($\\text{Fe} \\approx 5,0\\%$), calcium ($\\text{Ca} \\approx 3,6\\%$). Các hợp chất trong vỏ Trái Đất tồn tại chủ yếu ở dạng oxide (như cát thạch anh $\\text{SiO}_2$, quặng bauxite $\\text{Al}_2\\text{O}_3$, quặng hematite $\\text{Fe}_2\\text{O}_3$) và muối (đá vôi $\\text{CaCO}_3$, muối mỏ $\\text{NaCl}$). Đá vôi dùng sản xuất vôi sống ($\\text{CaO}$), xi măng; cát thạch anh ($\\text{SiO}_2$) dùng sản xuất thủy tinh và gốm sứ. Khai thác tài nguyên khoáng sản cần gắn liền với bảo vệ môi trường và sử dụng vật liệu tái chế.",
        [
            F("Nhiệt phân đá vôi sản xuất vôi sống", "\\text{CaCO}_3 \\xrightarrow{900-1000^\\circ\\text{C}} \\text{CaO} + \\text{CO}_2\\uparrow", "Phản ứng xảy ra trong lò nung vôi công nghiệp"),
            F("Sản xuất thủy tinh thông thường", "\\text{Na}_2\\text{CO}_3 + \\text{CaCO}_3 + 6\\text{SiO}_2 \\xrightarrow{t^\\circ} \\text{Na}_2\\text{O}\\cdot\\text{CaO}\\cdot 6\\text{SiO}_2 + 2\\text{CO}_2\\uparrow", "Nung chảy cát thạch anh (SiO2) với đá vôi và soda"),
            F("Thứ tự nguyên tố phổ biến trong vỏ Trái Đất", "\\%m_{\\text{O}} (46,6\\%) > \\%m_{\\text{Si}} (27,7\\%) > \\%m_{\\text{Al}} (8,1\\%) > \\%m_{\\text{Fe}} (5,0\\%)", "Oxygen là nguyên tố phổ biến nhất; nhôm là kim loại phổ biến nhất trong vỏ Trái Đất"),
        ],
        [
            "Nêu được hàm lượng các nguyên tố hóa học chủ yếu trong vỏ Trái Đất và các dạng hợp chất tự nhiên của chúng (oxide, muối)",
            "Trình bày được nguồn gốc, thành phần chính và ứng dụng của đá vôi ($\\text{CaCO}_3$), cát thạch anh ($\\text{SiO}_2$) và các loại quặng kim loại",
            "Giải thích được lợi ích kinh tế và yêu cầu bảo vệ môi trường trong việc khai thác, chế biến tài nguyên khoáng sản",
        ],
        "Nung hoàn toàn $200\\text{ kg}$ đá vôi chứa $80\\%$ $\\text{CaCO}_3$ về khối lượng (phần còn lại là tạp chất trơ). Tính khối lượng vôi sống ($\\text{CaO}$) thu được.",
        "Khối lượng $\\text{CaCO}_3$ nguyên chất: $m_{\\text{CaCO}_3} = 200 \\cdot 80\\% = 160\\text{ kg} \\Rightarrow n_{\\text{CaCO}_3} = \\frac{160}{100} = 1,6\\text{ kmol}$.\\nPTHH: $\\text{CaCO}_3 \\xrightarrow{t^\\circ} \\text{CaO} + \\text{CO}_2\\uparrow$.\\nTheo PTHH: $n_{\\text{CaO}} = 1,6\\text{ kmol} \\Rightarrow m_{\\text{CaO}} = 1,6 \\cdot 56 = 89,6\\text{ kg}$.",
        "Tỉnh Quảng Ninh, Ninh Bình, Hà Nam, Kiên Giang ở Việt Nam có trữ lượng đá vôi lớn phục vụ ngành công nghiệp sản xuất xi măng; cát trắng ở Khánh Hòa, Quảng Nam giàu $\\text{SiO}_2$ dùng sản xuất thủy tinh cao cấp.",
        CH4_ID, CH4_TITLE, CH4_DESC,
        extra_questions=[
            mcq("Nguyên tố kim loại phổ biến nhất trong vỏ Trái Đất (chiếm khoảng $8,1\\%$ về khối lượng) là:", "Nhôm ($\\text{Al}$)", ["Nhôm ($\\text{Al}$)", "Sắt ($\\text{Fe}$)", "Calcium ($\\text{Ca}$)", "Đồng ($\\text{Cu}$)"], "Trong vỏ Trái Đất, nguyên tố phổ biến nhất là $\\text{O}$, đứng thứ hai là $\\text{Si}$ (phi kim), và đứng thứ ba (kim loại phổ biến nhất) là $\\text{Al}$.", "biet"),
            mcq("Thành phần hóa học chính của cát trắng (cát thạch anh) dùng làm nguyên liệu sản xuất thủy tinh là:", "$\\text{SiO}_2$", ["$\\text{SiO}_2$", "$\\text{CaCO}_3$", "$\\text{Al}_2\\text{O}_3$", "$\\text{Fe}_2\\text{O}_3$"], "Cát thạch anh có thành phần chính là silicon dioxide ($\\text{SiO}_2$).", "hieu"),
            short("Nung hoàn toàn $10\\text{ tấn}$ $\\text{CaCO}_3$ ($M = 100$) nguyên chất thu được tối đa bao nhiêu tấn vôi sống $\\text{CaO}$ ($M = 56$)?", "5,6", ["5,6", "5.6"], "Theo PTHH $\\text{CaCO}_3 \\xrightarrow{t^\\circ} \\text{CaO} + \\text{CO}_2$, từ $100\\text{ tấn}$ $\\text{CaCO}_3$ thu được $56\\text{ tấn}$ $\\text{CaO}$, vậy từ $10\\text{ tấn}$ thu được $5,6\\text{ tấn}$ $\\text{CaO}$.", "vandung"),
        ]
    ),
]

LESSONS = CH1_LESSONS + CH2_LESSONS + CH3_LESSONS + CH4_LESSONS
