from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_9: list[dict[str, Any]] = [
    lesson(
        grade=9,
        order=1,
        code="H9-C01",
        title="Chương 1: Tính chất chung của kim loại và hợp kim",
        topic="kim-loai",
        summary=(
            r"Nắm vững 4 tính chất vật lý chung của kim loại (tính dẻo, dẫn điện, dẫn nhiệt, ánh kim), "
            r"tính chất hóa học của kim loại (tác dụng với phi kim $\text{O}_2, \text{Cl}_2, \text{S}$, dung dịch acid $\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$, "
            r"nước và dung dịch muối) cùng thành phần, tính chất của các hợp kim phổ biến (gang, thép, duralumin)."
        ),
        objectives=[
            r"Trình bày được các tính chất vật lý chung của kim loại (tính dẻo, dẫn điện, dẫn nhiệt, ánh kim) và các ứng dụng tương ứng trong thực tiễn.",
            r"Viết được các phương trình hóa học minh họa tính chất hóa học cơ bản của kim loại: tác dụng với oxygen ($\text{O}_2$), phi kim khác ($\text{Cl}_2, \text{S}$), nước, dung dịch acid loãng ($\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$) và dung dịch muối.",
            r"Nêu được khái niệm hợp kim, ưu điểm vượt trội của hợp kim so với kim loại nguyên chất về độ cứng, độ bền và khả năng chống ăn mòn.",
            r"Phân biệt được thành phần, tính chất và ứng dụng của hai hợp kim quan trọng của iron là gang ($2\text{\%} - 5\text{\% }\text{C}$) và thép ($< 2\text{\% }\text{C}$) cũng như hợp kim duralumin của aluminium.",
        ],
        formulas=[
            {
                "name": r"Phản ứng của kim loại với phi kim ($\text{O}_2, \text{Cl}_2, \text{S}$)",
                "formula": r"$3\text{Fe} + 2\text{O}_2 \xrightarrow{t^\circ} \text{Fe}_3\text{O}_4; \quad 2\text{Fe} + 3\text{Cl}_2 \xrightarrow{t^\circ} 2\text{FeCl}_3; \quad \text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$",
                "note": r"$\text{Fe}$ tác dụng với $\text{Cl}_2$ tạo muối iron(III) chloride ($\text{FeCl}_3$), với $\text{S}$ tạo iron(II) sulfide ($\text{FeS}$)",
            },
            {
                "name": r"Phản ứng của kim loại hoạt động trước $\text{H}$ với dung dịch acid loãng",
                "formula": r"$\text{M} + n\text{HCl} \longrightarrow \text{MCl}_n + \dfrac{n}{2}\text{H}_2\uparrow \quad (\text{M đứng trước }\text{H}: \text{Mg}, \text{Al}, \text{Zn}, \text{Fe}\dots)$",
                "note": r"Với $\text{Fe}$ tác dụng $\text{HCl}$ hoặc $\text{H}_2\text{SO}_4\text{ loãng}$ chỉ tạo muối iron(II) ($\text{FeCl}_2, \text{FeSO}_4$)",
            },
            {
                "name": "Phản ứng của kim loại kiềm với nước và kim loại với dung dịch muối",
                "formula": r"$2\text{Na} + 2\text{H}_2\text{O} \longrightarrow 2\text{NaOH} + \text{H}_2\uparrow; \quad \text{Fe} + \text{CuSO}_4 \longrightarrow \text{FeSO}_4 + \text{Cu}\downarrow$",
                "note": r"Kim loại từ $\text{Mg}$ trở đi (không tan trong nước ở nhiệt độ thường) đẩy được kim loại yếu hơn ra khỏi dung dịch muối",
            },
            {
                "name": "Độ tăng - giảm khối lượng thanh kim loại khi nhúng vào dung dịch muối",
                "formula": r"$\Delta m_{\text{thanh kim loại}} = m_{\text{kim loại bám vào}} - m_{\text{kim loại tan ra}}$",
                "note": r"Ví dụ nhúng $\text{Fe}$ vào $\text{CuSO}_4$: cứ $1\text{ mol }\text{Fe}$ ($56\text{ g}$) phản ứng tạo $1\text{ mol }\text{Cu}$ ($64\text{ g}$) thì khối lượng tăng $8\text{ g}$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Tính chất vật lý của kim loại",
                "content": (
                    r"Kim loại có bốn tính chất vật lý chung: (1) Tính dẻo: dễ rèn, kéo sợi, dát mỏng ($\text{Au}$ là kim loại dẻo nhất; $\text{Al}$ được cán mỏng làm màng bọc thực phẩm). "
                    r"(2) Tính dẫn điện: các kim loại dẫn điện tốt theo thứ tự giảm dần $\text{Ag} > \text{Cu} > \text{Au} > \text{Al} > \text{Fe}$ (thực tế thường dùng $\text{Cu}$ và $\text{Al}$ làm lõi dây dẫn điện). "
                    r"(3) Tính dẫn nhiệt: kim loại dẫn nhiệt tốt thường cũng dẫn điện tốt ($\text{Al}$, thép không gỉ dùng làm dụng cụ nấu ăn). "
                    r"(4) Ánh kim: bề mặt kim loại phản xạ tốt ánh sáng nhìn thấy nên dùng làm đồ trang sức ($\text{Au}, \text{Ag}$), tráng gương ($\text{Ag}$). "
                    r"Ngoài ra, các kim loại khác nhau về khối lượng riêng, nhiệt độ nóng chảy ($\text{Hg}$ lỏng ở nhiệt độ thường, $\text{W}$ nóng chảy ở $3410^\circ\text{C}$) và độ cứng ($\text{Cr}$ cứng nhất)."
                ),
            },
            {
                "title": "2. Tính chất hóa học của kim loại",
                "content": (
                    r"(1) Tác dụng với phi kim: Hầu hết kim loại (trừ $\text{Au}, \text{Pt}, \text{Ag}$) tác dụng với oxygen tạo oxide kim loại "
                    r"(như $4\text{Al} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{Al}_2\text{O}_3$, $3\text{Fe} + 2\text{O}_2 \xrightarrow{t^\circ} \text{Fe}_3\text{O}_4$). "
                    r"Ở nhiệt độ cao, kim loại tác dụng với $\text{Cl}_2$ tạo muối chloride hóa trị cao ($2\text{Fe} + 3\text{Cl}_2 \xrightarrow{t^\circ} 2\text{FeCl}_3$) và với $\text{S}$ tạo muối sulfide ($\text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$, riêng $\text{Hg}$ phản ứng với $\text{S}$ ngay ở nhiệt độ thường). "
                    r"(2) Tác dụng với nước: Kim loại hoạt động mạnh ($\text{K}, \text{Na}, \text{Ca}, \text{Ba}$) tác dụng với nước ở nhiệt độ thường tạo dung dịch kiềm và khí $\text{H}_2$; $\text{Mg}, \text{Zn}, \text{Fe}$ tác dụng với hơi nước ở nhiệt độ cao tạo oxide và $\text{H}_2$; $\text{Cu}, \text{Ag}, \text{Au}$ không phản ứng. "
                    r"(3) Tác dụng với dung dịch acid loãng ($\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$): Kim loại đứng trước $\text{H}$ phản ứng tạo muối và khí $\text{H}_2$. "
                    r"(4) Tác dụng với dung dịch muối: Kim loại hoạt động mạnh hơn (không tan trong nước) đẩy kim loại yếu hơn ra khỏi dung dịch muối của nó."
                ),
            },
            {
                "title": "3. Hợp kim và ứng dụng",
                "content": (
                    r"Hợp kim là vật liệu kim loại có chứa một kim loại cơ bản và một số kim loại khác hoặc phi kim. Hợp kim thường có độ cứng, độ bền cơ học, "
                    r"khả năng chống ăn mòn và chống gỉ vượt trội so với các kim loại nguyên chất tạo nên nó. "
                    r"Các hợp kim phổ biến gồm: Gang (hợp kim $\text{Fe} - \text{C}$ chứa $2\text{\%} - 5\text{\%}$ khối lượng $\text{C}$, cứng và giòn, dùng đúc bệ máy, ống dẫn); "
                    r"Thép (hợp kim $\text{Fe} - \text{C}$ chứa dưới $2\text{\%}$ khối lượng $\text{C}$, dẻo, đàn hồi, bền; thép không gỉ inox chứa thêm $\text{Cr}, \text{Ni}$); "
                    r"Duralumin (hợp kim của $\text{Al}$ với $\text{Cu}, \text{Mg}, \text{Mn}$, nhẹ và bền chắc, dùng chế tạo vỏ máy bay, tàu vũ trụ)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Cho $11{,}2\text{ g}$ bột iron ($\text{Fe}$, $M = 56\text{ g/mol}$) tác dụng hoàn toàn với dung dịch hydrochloric acid ($\text{HCl}$) dư. "
                    r"Tính thể tích khí $\text{H}_2$ thoát ra ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) và khối lượng muối thu được ($M_{\text{Cl}} = 35{,}5\text{ g/mol}$)."
                ),
                "solution": (
                    r"Số mol $\text{Fe}$ là $n_{\text{Fe}} = \dfrac{11{,}2}{56} = 0{,}2\text{ mol}$. Phương trình hóa học: "
                    r"$\text{Fe} + 2\text{HCl} \longrightarrow \text{FeCl}_2 + \text{H}_2\uparrow$. Theo phương trình, "
                    r"$n_{\text{H}_2} = n_{\text{FeCl}_2} = n_{\text{Fe}} = 0{,}2\text{ mol}$. Thể tích khí $\text{H}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}2 = 4{,}958\text{ L}$. "
                    r"Khối lượng muối $\text{FeCl}_2$ ($M = 127\text{ g/mol}$) là $m = 0{,}2 \cdot 127 = 25{,}4\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Nhúng một đinh sắt ($\text{Fe}$, $M = 56\text{ g/mol}$) sạch vào $200\text{ mL}$ dung dịch $\text{CuSO}_4$ $0{,}5\text{ M}$. "
                    r"Sau khi phản ứng kết thúc hoàn toàn, lấy đinh sắt ra rửa nhẹ, làm khô và cân lại (giả sử toàn bộ $\text{Cu}$ sinh ra bám hết vào đinh sắt, "
                    r"biết $M_{\text{Cu}} = 64\text{ g/mol}$). Tính độ tăng khối lượng của đinh sắt."
                ),
                "solution": (
                    r"Số mol $\text{CuSO}_4$ phản ứng là $n_{\text{CuSO}_4} = 0{,}2 \cdot 0{,}5 = 0{,}1\text{ mol}$. Theo phương trình "
                    r"$\text{Fe} + \text{CuSO}_4 \longrightarrow \text{FeSO}_4 + \text{Cu}\downarrow$, có $0{,}1\text{ mol }\text{Fe}$ tan ra và $0{,}1\text{ mol }\text{Cu}$ bám vào. "
                    r"Độ tăng khối lượng của đinh sắt là $\Delta m = m_{\text{Cu}} - m_{\text{Fe}} = 0{,}1 \cdot (64 - 56) = 0{,}8\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Thứ tự độ dẫn điện và dẫn nhiệt giảm dần của các kim loại phổ biến là $\text{Ag} > \text{Cu} > \text{Au} > \text{Al} > \text{Fe}$.",
            r"Kim loại $\text{Fe}$ tác dụng với $\text{Cl}_2$ cho muối $\text{FeCl}_3$ (hóa trị $\text{III}$), nhưng tác dụng với dung dịch $\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$ hoặc dung dịch $\text{CuSO}_4$ chỉ cho muối iron(II) ($\text{FeCl}_2, \text{FeSO}_4$).",
            r"Gang và thép đều là hợp kim của $\text{Fe}$ với $\text{C}$: gang chứa $2\text{\%} - 5\text{\% }\text{C}$ còn thép chứa dưới $2\text{\% }\text{C}$.",
        ],
        questions=[
            mcq(
                question=r"Kim loại có khả năng dẫn điện tốt nhất trong tất cả các kim loại ở điều kiện thường là:",
                options=[r"$\text{Cu}$ (copper)", r"$\text{Al}$ (aluminium)", r"$\text{Ag}$ (silver)", r"$\text{Au}$ (gold)"],
                answer="C",
                level="biet",
                solution=r"Độ dẫn điện của kim loại giảm dần theo dãy $\text{Ag} > \text{Cu} > \text{Au} > \text{Al} > \text{Fe}$, do đó $\text{Ag}$ dẫn điện tốt nhất.",
            ),
            mcq(
                question=r"Khi đốt nóng dây iron ($\text{Fe}$) trong bình chứa khí chlorine ($\text{Cl}_2$) dư, sản phẩm tạo thành có công thức hóa học là:",
                options=[r"$\text{FeCl}_2$", r"$\text{FeCl}_3$", r"$\text{Fe}_3\text{O}_4$", r"$\text{FeCl}$"],
                answer="B",
                level="biet",
                solution=r"Khí $\text{Cl}_2$ là phi kim hoạt động mạnh nên oxi hóa $\text{Fe}$ lên số oxi hóa/hóa trị $\text{III}$: $2\text{Fe} + 3\text{Cl}_2 \xrightarrow{t^\circ} 2\text{FeCl}_3$.",
            ),
            mcq(
                question=r"Kim loại nào sau đây tồn tại ở trạng thái lỏng ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) và phản ứng được với bột sulfur ($\text{S}$) ngay ở nhiệt độ thường?",
                options=[r"$\text{Na}$ (sodium)", r"$\text{Al}$ (aluminium)", r"$\text{Hg}$ (mercury)", r"$\text{Fe}$ (iron)"],
                answer="C",
                level="biet",
                solution=r"Thủy ngân ($\text{Hg}$, mercury) là kim loại duy nhất ở thể lỏng ở điều kiện thường và tác dụng trực tiếp với bột $\text{S}$ ở nhiệt độ thường tạo $\text{HgS}$ rắn.",
            ),
            mcq(
                question=r"Hợp kim thép là hợp kim của iron ($\text{Fe}$) với carbon ($\text{C}$) và một số nguyên tố khác, trong đó hàm lượng carbon chiếm:",
                options=[
                    r"Dưới $2\text{\%}$ về khối lượng",
                    r"Từ $2\text{\%}$ đến $5\text{\%}$ về khối lượng",
                    r"Từ $5\text{\%}$ đến $10\text{\%}$ về khối lượng",
                    r"Trên $10\text{\%}$ về khối lượng",
                ],
                answer="A",
                level="biet",
                solution=r"Trong hợp kim $\text{Fe} - \text{C}$, thép chứa dưới $2\text{\%}$ khối lượng carbon, còn gang chứa từ $2\text{\%}$ đến $5\text{\%}$ khối lượng carbon.",
            ),
            mcq(
                question=r"Cho mẩu nhỏ kim loại sodium ($\text{Na}$) vào cốc nước cất có nhỏ vài giọt dung dịch phenolphthalein. Hiện tượng quan sát được là:",
                options=[
                    r"Mẩu $\text{Na}$ chìm xuống đáy cốc, không có khí thoát ra, dung dịch không đổi màu",
                    r"Mẩu $\text{Na}$ nóng chảy thành giọt tròn chạy trên mặt nước, sủi bọt khí $\text{H}_2$ và dung dịch hóa hồng",
                    r"Mẩu $\text{Na}$ tan dần, sủi bọt khí màu vàng lục và xuất hiện kết tủa trắng",
                    r"Mẩu $\text{Na}$ tan dần, không có khí thoát ra và dung dịch chuyển sang màu xanh lam",
                ],
                answer="B",
                level="hieu",
                solution=r"Kim loại $\text{Na}$ nhẹ hơn nước và phản ứng mạnh tỏa nhiệt với nước: $2\text{Na} + 2\text{H}_2\text{O} \longrightarrow 2\text{NaOH} + \text{H}_2\uparrow$. Dung dịch $\text{NaOH}$ tạo thành làm phenolphthalein hóa hồng.",
            ),
            mcq(
                question=r"Để làm sạch một mẫu bột kim loại copper ($\text{Cu}$) có lẫn tạp chất là bột zinc ($\text{Zn}$) và bột iron ($\text{Fe}$), ta có thể ngâm hỗn hợp vào lượng dư dung dịch nào sau đây rồi lọc lấy chất rắn?",
                options=[
                    r"Dung dịch $\text{NaOH}$",
                    r"Dung dịch $\text{HCl}$ (hoặc dung dịch $\text{CuSO}_4$)",
                    r"Dung dịch $\text{NaCl}$",
                    r"Dung dịch $\text{MgSO}_4$",
                ],
                answer="B",
                level="hieu",
                solution=r"Khi ngâm vào dung dịch $\text{HCl}$ dư (hoặc $\text{CuSO}_4$ dư), tạp chất $\text{Zn}$ và $\text{Fe}$ phản ứng tan hết, còn $\text{Cu}$ không tác dụng với $\text{HCl}$ (hoặc được tạo thêm từ $\text{CuSO}_4$) nên thu được $\text{Cu}$ tinh khiết.",
            ),
            tf4(
                stem=r"Tiến hành các thí nghiệm khảo sát tính chất của kim loại iron ($\text{Fe}$) và aluminium ($\text{Al}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Dây dẫn điện cao thế thường làm bằng $\text{Al}$ vì $\text{Al}$ dẫn điện tốt và nhẹ hơn $\text{Cu}$.",
                    r"b) Khi cho bột $\text{Fe}$ tác dụng với dung dịch $\text{HCl}$ dư, thu được dung dịch muối $\text{FeCl}_3$ và khí $\text{H}_2$.",
                    r"c) Đốt cháy dây $\text{Fe}$ trong bình khí oxygen ($\text{O}_2$) tạo ra các hạt rắn màu nâu đen là iron(II,III) oxide ($\text{Fe}_3\text{O}_4$).",
                    r"d) Nhúng lá $\text{Al}$ vào dung dịch $\text{MgSO}_4$ thấy có kim loại $\text{Mg}$ bám ngoài lá $\text{Al}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{Al}$ có khối lượng riêng nhỏ ($2{,}7\text{ g/cm}^3$) và dẫn điện tốt nên giảm tải trọng cho cột điện cao thế. "
                    r"b) Sai vì $\text{Fe}$ tác dụng với dung dịch $\text{HCl}$ chỉ tạo muối iron(II) chloride ($\text{FeCl}_2$) và khí $\text{H}_2$. "
                    r"c) Đúng vì $3\text{Fe} + 2\text{O}_2 \xrightarrow{t^\circ} \text{Fe}_3\text{O}_4$. "
                    r"d) Sai vì $\text{Al}$ hoạt động hóa học yếu hơn $\text{Mg}$ nên không đẩy được $\text{Mg}$ ra khỏi dung dịch muối $\text{MgSO}_4$."
                ),
            ),
            tf4(
                stem=r"Trong công nghiệp luyện kim và chế tạo cơ khí, các hợp kim như gang, thép, inox và duralumin được sử dụng rộng rãi hơn nhiều so với kim loại tinh khiết. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Hợp kim thường có độ cứng và độ bền cơ học cao hơn so với các kim loại thành phần nguyên chất.",
                    r"b) Gang là hợp kim của $\text{Fe}$ và $\text{C}$ có hàm lượng carbon nhỏ hơn $2\text{\%}$, rất dẻo và dễ uốn.",
                    r"c) Duralumin là hợp kim của aluminium ($\text{Al}$) có đặc tính nhẹ và bền nên được dùng trong chế tạo máy bay.",
                    r"d) Thép không gỉ (inox) dễ bị ăn mòn trong không khí ẩm hơn so với sắt nguyên chất.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì cấu trúc mạng tinh thể của hợp kim có các nguyên tử khác kích thước làm tăng độ cứng và độ bền. "
                    r"b) Sai vì gang chứa $2\text{\%} - 5\text{\% }\text{C}$, có tính cứng và giòn, không dẻo như thép. "
                    r"c) Đúng vì duralumin là hợp kim $\text{Al} - \text{Cu} - \text{Mg} - \text{Mn}$ vừa nhẹ vừa bền chắc. "
                    r"d) Sai vì inox có chứa $\text{Cr}$ và $\text{Ni}$ tạo màng bảo vệ giúp chống gỉ sét vượt trội so với sắt."
                ),
            ),
            mcq(
                question=r"Hòa tan hoàn toàn $5{,}4\text{ g}$ kim loại aluminium ($\text{Al}$, $M = 27\text{ g/mol}$) vào dung dịch $\text{H}_2\text{SO}_4\text{ loãng}$ dư theo phương trình $2\text{Al} + 3\text{H}_2\text{SO}_4 \longrightarrow \text{Al}_2(\text{SO}_4)_3 + 3\text{H}_2\uparrow$. Thể tích khí $\text{H}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là:",
                options=[r"$4{,}958\text{ L}$", r"$6{,}720\text{ L}$", r"$7{,}437\text{ L}$", r"$9{,}916\text{ L}$"],
                answer="C",
                level="vandung",
                solution=r"Số mol $\text{Al}$ là $n_{\text{Al}} = \dfrac{5{,}4}{27} = 0{,}2\text{ mol}$. Theo phương trình hóa học, $n_{\text{H}_2} = \dfrac{3}{2} \cdot n_{\text{Al}} = 0{,}3\text{ mol}$. Thể tích khí $\text{H}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}3 = 7{,}437\text{ L}$.",
            ),
            short(
                question=r"Cho $10\text{ g}$ hỗn hợp bột gồm kim loại zinc ($\text{Zn}$, $M = 65\text{ g/mol}$) và kim loại copper ($\text{Cu}$, $M = 64\text{ g/mol}$) vào dung dịch $\text{HCl}$ dư. Sau khi phản ứng xảy ra hoàn toàn, thu được $2{,}479\text{ L}$ khí $\text{H}_2$ ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$). Tính khối lượng kim loại $\text{Cu}$ (theo đơn vị $\text{g}$) có trong hỗn hợp ban đầu.",
                answer=["3,5", "3.5"],
                level="vandung",
                solution=r"Chỉ có $\text{Zn}$ phản ứng với dung dịch $\text{HCl}$: $\text{Zn} + 2\text{HCl} \longrightarrow \text{ZnCl}_2 + \text{H}_2\uparrow$. Số mol $\text{H}_2$ là $n_{\text{H}_2} = \dfrac{2{,}479}{24{,}79} = 0{,}1\text{ mol}$, suy ra $n_{\text{Zn}} = 0{,}1\text{ mol}$ và $m_{\text{Zn}} = 0{,}1 \cdot 65 = 6{,}5\text{ g}$. Vậy khối lượng $\text{Cu}$ trong hỗn hợp là $m_{\text{Cu}} = 10 - 6{,}5 = 3{,}5\text{ g}$.",
            ),
        ],
        description="Tính chất vật lý và tính chất hóa học chung của kim loại, khái niệm và ứng dụng của hợp kim gang, thép, duralumin theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=2,
        code="H9-C02",
        title="Chương 2: Dãy hoạt động hóa học của kim loại và tách kim loại",
        topic="day-hoat-dong-kim-loai",
        summary=(
            r"Nắm vững dãy hoạt động hóa học của kim loại $\text{K}, \text{Na}, \text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Pb}, \text{H}, \text{Cu}, \text{Ag}, \text{Au}$ "
            r"và 4 ý nghĩa của dãy; trình bày được các phương pháp tách kim loại từ quặng: điện phân nóng chảy đối với kim loại hoạt động mạnh "
            r"($\text{Na}, \text{Mg}, \text{Al}$) và nhiệt luyện (dùng $\text{C}, \text{CO}, \text{H}_2, \text{Al}$) đối với kim loại hoạt động trung bình và yếu ($\text{Zn}, \text{Fe}, \text{Cu}$)."
        ),
        objectives=[
            r"Trình bày được dãy hoạt động hóa học của một số kim loại phổ biến: $\text{K}, \text{Na}, \text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Pb}, \text{H}, \text{Cu}, \text{Ag}, \text{Au}$.",
            r"Nêu được 4 ý nghĩa của dãy hoạt động hóa học và vận dụng để dự đoán chiều phản ứng của kim loại với nước, dung dịch acid và dung dịch muối.",
            r"Trình bày được nguyên tắc tách kim loại ra khỏi hợp chất (khử ion kim loại thành nguyên tử) từ các loại quặng tự nhiên như bauxite ($\text{Al}_2\text{O}_3$), hematite ($\text{Fe}_2\text{O}_3$), sphalerite ($\text{ZnS}$).",
            r"Phân biệt được phạm vi áp dụng của phương pháp điện phân nóng chảy (với $\text{K}, \text{Na}, \text{Ca}, \text{Mg}, \text{Al}$) và phương pháp nhiệt luyện (với $\text{Zn}, \text{Fe}, \text{Cu}$).",
        ],
        formulas=[
            {
                "name": "Dãy hoạt động hóa học của kim loại",
                "formula": r"$\underbrace{\text{K}, \text{Na}}_{\text{tác dụng }\text{H}_2\text{O}\text{ thường}} \quad \underbrace{\text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Pb}}_{\text{đứng trước }\text{H}} \quad [\text{H}] \quad \underbrace{\text{Cu}, \text{Ag}, \text{Au}}_{\text{đứng sau }\text{H}}$",
                "note": r"Từ trái sang phải, mức độ hoạt động hóa học của kim loại giảm dần",
            },
            {
                "name": r"Phương pháp điện phân nóng chảy tách kim loại hoạt động mạnh ($\text{Na}, \text{Mg}, \text{Al}$)",
                "formula": r"$2\text{Al}_2\text{O}_3 \xrightarrow[\text{cryolite}]{\text{đpnc}} 4\text{Al} + 3\text{O}_2\uparrow; \quad 2\text{NaCl} \xrightarrow{\text{đpnc}} 2\text{Na} + \text{Cl}_2\uparrow$",
                "note": r"Cryolite ($\text{Na}_3\text{AlF}_6$) giúp hạ nhiệt độ nóng chảy của $\text{Al}_2\text{O}_3$ và tăng độ dẫn điện",
            },
            {
                "name": r"Phương pháp nhiệt luyện tách kim loại trung bình và yếu ($\text{Zn}, \text{Fe}, \text{Cu}$)",
                "formula": r"$\text{Fe}_2\text{O}_3 + 3\text{CO} \xrightarrow{t^\circ} 2\text{Fe} + 3\text{CO}_2\uparrow; \quad \text{ZnO} + \text{C} \xrightarrow{t^\circ} \text{Zn} + \text{CO}\uparrow$",
                "note": r"Chất khử $\text{C}, \text{CO}, \text{H}_2, \text{Al}$ chỉ khử được oxide của các kim loại đứng sau $\text{Al}$",
            },
            {
                "name": r"Tách zinc từ quặng sphalerite ($\text{ZnS}$)",
                "formula": r"$2\text{ZnS} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{ZnO} + 2\text{SO}_2\uparrow; \quad \text{ZnO} + \text{C} \xrightarrow{t^\circ} \text{Zn} + \text{CO}\uparrow$",
                "note": r"Đốt quặng sulfide thành oxide rồi khử bằng than cốc ở nhiệt độ cao",
            },
        ],
        theory_sections=[
            {
                "title": "1. Dãy hoạt động hóa học của kim loại và ý nghĩa",
                "content": (
                    r"Bằng nhiều thí nghiệm thực nghiệm, các kim loại được sắp xếp theo chiều giảm dần mức độ hoạt động hóa học: "
                    r"$\text{K}, \text{Na}, \text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Pb}, \text{H}, \text{Cu}, \text{Ag}, \text{Au}$. "
                    r"Bốn ý nghĩa của dãy: (1) Mức độ hoạt động hóa học giảm dần từ trái sang phải. "
                    r"(2) Kim loại đứng đầu dãy ($\text{K}, \text{Na}, \text{Ca}$) tác dụng với nước ở điều kiện thường tạo dung dịch kiềm và giải phóng khí $\text{H}_2$. "
                    r"(3) Kim loại đứng trước $\text{H}$ tác dụng với dung dịch acid ($\text{HCl}, \text{H}_2\text{SO}_4\text{ loãng}$) giải phóng khí $\text{H}_2$. "
                    r"(4) Kim loại đứng trước (từ $\text{Mg}$ trở đi) đẩy được kim loại đứng sau ra khỏi dung dịch muối của nó."
                ),
            },
            {
                "title": "2. Nguồn quặng kim loại trong tự nhiên",
                "content": (
                    r"Trong tự nhiên, trừ một số kim loại rất yếu như $\text{Au}, \text{Pt}$ tồn tại ở dạng đơn chất tự do, hầu hết các kim loại "
                    r"tồn tại ở dạng hợp chất (oxide, muối sulfide, muối chloride...) trong các loại quặng và khoáng vật. "
                    r"Các quặng quan trọng gồm: quặng bauxite (chứa $\text{Al}_2\text{O}_3 \cdot 2\text{H}_2\text{O}$) dùng sản xuất nhôm; "
                    r"quặng hematite (chứa $\text{Fe}_2\text{O}_3$) và magnetite (chứa $\text{Fe}_3\text{O}_4$) dùng sản xuất gang, thép; "
                    r"quặng sphalerite (chứa $\text{ZnS}$) dùng sản xuất kẽm; muối mỏ và nước biển (chứa $\text{NaCl}, \text{MgCl}_2$) dùng tách $\text{Na}, \text{Mg}$."
                ),
            },
            {
                "title": "3. Các phương pháp tách kim loại",
                "content": (
                    r"Tùy theo mức độ hoạt động hóa học của kim loại, người ta chọn phương pháp tách thích hợp: "
                    r"(1) Phương pháp điện phân nóng chảy: Dùng dòng điện một chiều để tách các kim loại hoạt động hóa học mạnh ($\text{K}, \text{Na}, \text{Ca}, \text{Mg}, \text{Al}$) "
                    r"từ hợp chất nóng chảy của chúng (ví dụ: điện phân $\text{Al}_2\text{O}_3$ nóng chảy có mặt cryolite để điều chế $\text{Al}$). "
                    r"(2) Phương pháp nhiệt luyện: Dùng các chất khử như $\text{C}, \text{CO}, \text{H}_2$ hoặc kim loại $\text{Al}$ ở nhiệt độ cao để tách các kim loại "
                    r"hoạt động trung bình và yếu (đứng sau $\text{Al}$, như $\text{Zn}, \text{Fe}, \text{Cu}$) ra khỏi oxide của chúng. "
                    r"Ngoài ra còn có phương pháp thủy luyện (dùng kim loại mạnh hơn đẩy kim loại yếu như $\text{Cu}, \text{Ag}$ khỏi dung dịch muối). Tái chế kim loại giúp tiết kiệm quặng, năng lượng và bảo vệ môi trường."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Cho một lá zinc ($\text{Zn}$, $M = 65\text{ g/mol}$) vào dung dịch chứa $0{,}1\text{ mol}$ $\text{AgNO}_3$ ($M_{\text{Ag}} = 108\text{ g/mol}$). "
                    r"Sau khi phản ứng xảy ra hoàn toàn, toàn bộ bạc ($\text{Ag}$) tạo thành bám hết vào lá kẽm. Hỏi khối lượng lá kẽm tăng hay giảm bao nhiêu gam?"
                ),
                "solution": (
                    r"Phương trình hóa học: $\text{Zn} + 2\text{AgNO}_3 \longrightarrow \text{Zn(NO}_3)_2 + 2\text{Ag}\downarrow$. "
                    r"Số mol $\text{AgNO}_3$ là $0{,}1\text{ mol}$ nên số mol $\text{Zn}$ phản ứng là $0{,}05\text{ mol}$ và số mol $\text{Ag}$ tạo thành là $0{,}1\text{ mol}$. "
                    r"Khối lượng lá kẽm thay đổi là $\Delta m = m_{\text{Ag}} - m_{\text{Zn}} = 0{,}1 \cdot 108 - 0{,}05 \cdot 65 = 10{,}8 - 3{,}25 = 7{,}55\text{ g}$ (tăng $7{,}55\text{ g}$)."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Trong lò cao luyện gang, khí $\text{CO}$ khử iron(III) oxide theo phương trình $\text{Fe}_2\text{O}_3 + 3\text{CO} \xrightarrow{t^\circ} 2\text{Fe} + 3\text{CO}_2\uparrow$. "
                    r"Tính khối lượng $\text{Fe}$ ($M = 56\text{ g/mol}$) thu được khi khử hoàn toàn $32\text{ kg}$ $\text{Fe}_2\text{O}_3$ ($M = 160\text{ g/mol}$) với hiệu suất $90\text{\%}$."
                ),
                "solution": (
                    r"Theo phương trình, cứ $160\text{ kg}$ $\text{Fe}_2\text{O}_3$ tạo ra $2 \cdot 56 = 112\text{ kg}$ $\text{Fe}$. "
                    r"Với $32\text{ kg}$ $\text{Fe}_2\text{O}_3$, khối lượng $\text{Fe}$ lý thuyết là $m_{\text{Fe (lt)}} = \dfrac{32 \cdot 112}{160} = 22{,}4\text{ kg}$. "
                    r"Do hiệu suất đạt $90\text{\%}$, khối lượng $\text{Fe}$ thực tế thu được là $m_{\text{Fe (tt)}} = 22{,}4 \cdot 90\text{\%} = 20{,}16\text{ kg}$."
                ),
            },
        ],
        key_takeaways=[
            r"Dãy hoạt động hóa học $\text{K}, \text{Na}, \text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Pb}, \text{H}, \text{Cu}, \text{Ag}, \text{Au}$ là chìa khóa để xét phản ứng của kim loại với nước, acid và dung dịch muối.",
            r"Các kim loại mạnh từ $\text{K}$ đến $\text{Al}$ bắt buộc phải điều chế bằng phương pháp điện phân nóng chảy; các kim loại đứng sau $\text{Al}$ ($\text{Zn}, \text{Fe}, \text{Cu}$) điều chế được bằng phương pháp nhiệt luyện.",
            r"Khí $\text{CO}$ và $\text{H}_2$ ở nhiệt độ cao chỉ khử được oxide của kim loại đứng sau $\text{Al}$ (như $\text{ZnO}, \text{Fe}_2\text{O}_3, \text{CuO}$), không khử được $\text{MgO}, \text{Al}_2\text{O}_3$.",
        ],
        questions=[
            mcq(
                question=r"Dãy các kim loại nào sau đây được sắp xếp theo chiều mức độ hoạt động hóa học giảm dần?",
                options=[
                    r"$\text{Mg}, \text{Al}, \text{Zn}, \text{Fe}, \text{Cu}, \text{Ag}$",
                    r"$\text{Al}, \text{Mg}, \text{Fe}, \text{Zn}, \text{Cu}, \text{Ag}$",
                    r"$\text{Cu}, \text{Fe}, \text{Zn}, \text{Al}, \text{Mg}, \text{Na}$",
                    r"$\text{Na}, \text{Fe}, \text{Mg}, \text{Al}, \text{Ag}, \text{Cu}$",
                ],
                answer="A",
                level="biet",
                solution=r"Theo dãy hoạt động hóa học chuẩn, chiều giảm dần độ hoạt động hóa học là $\text{Mg} > \text{Al} > \text{Zn} > \text{Fe} > \text{Cu} > \text{Ag}$.",
            ),
            mcq(
                question=r"Trong công nghiệp, kim loại aluminium ($\text{Al}$) được tách ra khỏi quặng bauxite (thành phần chính là $\text{Al}_2\text{O}_3$) bằng phương pháp nào sau đây?",
                options=[
                    r"Dùng khí $\text{CO}$ khử $\text{Al}_2\text{O}_3$ ở nhiệt độ cao",
                    r"Điện phân nóng chảy $\text{Al}_2\text{O}_3$ có mặt cryolite",
                    r"Dùng kim loại $\text{Fe}$ đẩy $\text{Al}$ ra khỏi dung dịch $\text{AlCl}_3$",
                    r"Nhiệt phân trực tiếp $\text{Al}_2\text{O}_3$ ở $1000^\circ\text{C}$",
                ],
                answer="B",
                level="biet",
                solution=r"$\text{Al}$ là kim loại hoạt động hóa học mạnh nên được sản xuất bằng phương pháp điện phân nóng chảy $\text{Al}_2\text{O}_3$ có hòa tan trong cryolite.",
            ),
            mcq(
                question=r"Quặng hematite dùng để sản xuất gang và thép trong công nghiệp có thành phần hóa học chính là:",
                options=[r"$\text{Al}_2\text{O}_3$", r"$\text{Fe}_2\text{O}_3$", r"$\text{ZnS}$", r"$\text{CaCO}_3$"],
                answer="B",
                level="biet",
                solution=r"Quặng hematite chứa thành phần chính là iron(III) oxide ($\text{Fe}_2\text{O}_3$).",
            ),
            mcq(
                question=r"Cặp chất nào sau đây xảy ra phản ứng hóa học ở điều kiện thường?",
                options=[
                    r"$\text{Cu} + \text{HCl\text{ (dd)}}$",
                    r"$\text{Ag} + \text{CuSO}_4\text{ (dd)}$",
                    r"$\text{Fe} + \text{CuSO}_4\text{ (dd)}$",
                    r"$\text{Cu} + \text{FeSO}_4\text{ (dd)}$",
                ],
                answer="C",
                level="biet",
                solution=r"$\text{Fe}$ hoạt động mạnh hơn $\text{Cu}$ nên đẩy được $\text{Cu}$ ra khỏi dung dịch $\text{CuSO}_4$: $\text{Fe} + \text{CuSO}_4 \longrightarrow \text{FeSO}_4 + \text{Cu}\downarrow$.",
            ),
            mcq(
                question=r"Dẫn luồng khí $\text{CO}$ dư đi qua ống sứ nung nóng đựng hỗn hợp bột gồm $\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}_2\text{O}_3$ và $\text{CuO}$. Sau khi các phản ứng xảy ra hoàn toàn, chất rắn thu được trong ống sứ gồm:",
                options=[
                    r"$\text{Mg}, \text{Al}, \text{Fe}, \text{Cu}$",
                    r"$\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}, \text{Cu}$",
                    r"$\text{MgO}, \text{Al}, \text{Fe}, \text{Cu}$",
                    r"$\text{MgO}, \text{Al}_2\text{O}_3, \text{Fe}_2\text{O}_3, \text{Cu}$",
                ],
                answer="B",
                level="hieu",
                solution=r"Khí $\text{CO}$ ở nhiệt độ cao chỉ khử được các oxide của kim loại đứng sau $\text{Al}$ là $\text{Fe}_2\text{O}_3$ và $\text{CuO}$ thành $\text{Fe}$ và $\text{Cu}$, còn $\text{MgO}$ và $\text{Al}_2\text{O}_3$ không bị khử nên giữ nguyên.",
            ),
            mcq(
                question=r"Cho ba kim loại $\text{X}, \text{Y}, \text{Z}$ thỏa mãn: $\text{X}$ và $\text{Y}$ đều tác dụng được với dung dịch $\text{HCl}$ giải phóng khí $\text{H}_2$, $\text{Z}$ không tác dụng với dung dịch $\text{HCl}$; khi cho $\text{X}$ vào dung dịch muối của $\text{Y}$ thì $\text{X}$ đẩy được $\text{Y}$ ra khỏi muối. Thứ tự mức độ hoạt động hóa học giảm dần của ba kim loại là:",
                options=[
                    r"$\text{X} > \text{Y} > \text{Z}$",
                    r"$\text{Y} > \text{X} > \text{Z}$",
                    r"$\text{Z} > \text{X} > \text{Y}$",
                    r"$\text{X} > \text{Z} > \text{Y}$",
                ],
                answer="A",
                level="hieu",
                solution=r"$\text{X}$ và $\text{Y}$ tác dụng với $\text{HCl}$ nên đứng trước $\text{H}$, còn $\text{Z}$ đứng sau $\text{H}$. Vì $\text{X}$ đẩy được $\text{Y}$ khỏi dung dịch muối nên $\text{X}$ mạnh hơn $\text{Y}$. Vậy thứ tự giảm dần là $\text{X} > \text{Y} > \text{Z}$.",
            ),
            tf4(
                stem=r"Thực hiện thí nghiệm nhúng một đinh sắt ($\text{Fe}$) đã đánh sạch gỉ vào ống nghiệm chứa dung dịch $\text{CuSO}_4$ màu xanh lam. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Trên bề mặt đinh sắt xuất hiện một lớp kim loại màu đỏ gạch của copper ($\text{Cu}$) bám vào.",
                    r"b) Màu xanh lam của dung dịch $\text{CuSO}_4$ đậm dần lên theo thời gian phản ứng.",
                    r"c) Phản ứng trên chứng tỏ trong dãy hoạt động hóa học, kim loại $\text{Fe}$ hoạt động mạnh hơn kim loại $\text{Cu}$.",
                    r"d) Nếu thay đinh sắt ($\text{Fe}$) bằng một dây bạc ($\text{Ag}$) thì phản ứng đẩy $\text{Cu}$ vẫn xảy ra tương tự.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì xảy ra phản ứng $\text{Fe} + \text{CuSO}_4 \longrightarrow \text{FeSO}_4 + \text{Cu}\downarrow$, $\text{Cu}$ màu đỏ bám lên đinh sắt. "
                    r"b) Sai vì nồng độ $\text{CuSO}_4$ giảm dần nên màu xanh lam của dung dịch nhạt dần. "
                    r"c) Đúng vì kim loại mạnh hơn ($\text{Fe}$) đẩy kim loại yếu hơn ($\text{Cu}$) ra khỏi dung dịch muối. "
                    r"d) Sai vì $\text{Ag}$ đứng sau $\text{Cu}$ trong dãy hoạt động hóa học nên không phản ứng với dung dịch $\text{CuSO}_4$."
                ),
            ),
            tf4(
                stem=r"Xét các quy trình tách kim loại trong công nghiệp từ nguồn quặng tự nhiên. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Kim loại sodium ($\text{Na}$) và magnesium ($\text{Mg}$) được điều chế bằng phương pháp điện phân nóng chảy muối chloride của chúng.",
                    r"b) Trong quá trình điện phân nóng chảy $\text{Al}_2\text{O}_3$, cryolite được thêm vào nhằm mục đích làm tăng nhiệt độ nóng chảy của hỗn hợp lên trên $2050^\circ\text{C}$.",
                    r"c) Để tách zinc ($\text{Zn}$) từ quặng sphalerite ($\text{ZnS}$), người ta đốt $\text{ZnS}$ trong oxi tạo $\text{ZnO}$ rồi dùng than cốc ($\text{C}$) khử $\text{ZnO}$ ở nhiệt độ cao.",
                    r"d) Có thể dùng khí $\text{H}_2$ hoặc khí $\text{CO}$ ở nhiệt độ cao để khử $\text{Al}_2\text{O}_3$ thành kim loại $\text{Al}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{Na}$ và $\text{Mg}$ là các kim loại hoạt động mạnh nên phải dùng phương pháp điện phân nóng chảy $\text{NaCl}, \text{MgCl}_2$. "
                    r"b) Sai vì cryolite giúp hạ nhiệt độ nóng chảy của hỗn hợp từ khoảng $2050^\circ\text{C}$ xuống khoảng $900^\circ\text{C}$ để tiết kiệm năng lượng. "
                    r"c) Đúng vì phản ứng là $2\text{ZnS} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{ZnO} + 2\text{SO}_2\uparrow$ và $\text{ZnO} + \text{C} \xrightarrow{t^\circ} \text{Zn} + \text{CO}\uparrow$. "
                    r"d) Sai vì $\text{Al}$ là kim loại hoạt động mạnh, $\text{H}_2$ và $\text{CO}$ không khử được $\text{Al}_2\text{O}_3$."
                ),
            ),
            mcq(
                question=r"Khử hoàn toàn $24\text{ g}$ hỗn hợp gồm $\text{CuO}$ ($M = 80\text{ g/mol}$) và $\text{Fe}_2\text{O}_3$ ($M = 160\text{ g/mol}$) bằng khí $\text{CO}$ dư ở nhiệt độ cao, thu được $17{,}6\text{ g}$ hỗn hợp hai kim loại $\text{Cu}$ và $\text{Fe}$. Thể tích khí $\text{CO}$ (ở điều kiện chuẩn $25^\circ\text{C}$, $1\text{ bar}$) đã tham gia phản ứng là:",
                options=[r"$4{,}958\text{ L}$", r"$7{,}437\text{ L}$", r"$9{,}916\text{ L}$", r"$12{,}395\text{ L}$"],
                answer="C",
                level="vandung",
                solution=r"Trong phản ứng khử oxide bằng $\text{CO}$, mỗi phân tử $\text{CO}$ lấy $1$ nguyên tử $\text{O}$ trong oxide tạo $\text{CO}_2$. Khối lượng nguyên tố $\text{O}$ trong oxide là $m_{\text{O}} = m_{\text{oxide}} - m_{\text{kim loại}} = 24 - 17{,}6 = 6{,}4\text{ g}$. Suy ra $n_{\text{CO}} = n_{\text{O}} = \dfrac{6{,}4}{16} = 0{,}4\text{ mol}$. Thể tích khí $\text{CO}$ ở đkc là $V = 24{,}79 \cdot 0{,}4 = 9{,}916\text{ L}$.",
            ),
            short(
                question=r"Điện phân nóng chảy hoàn toàn $20{,}4\text{ tấn}$ aluminium oxide ($\text{Al}_2\text{O}_3$, $M = 102\text{ g/mol}$) theo phương trình $2\text{Al}_2\text{O}_3 \xrightarrow[\text{cryolite}]{\text{đpnc}} 4\text{Al} + 3\text{O}_2\uparrow$. Tính khối lượng kim loại $\text{Al}$ ($M = 27\text{ g/mol}$, theo đơn vị $\text{tấn}$) thu được biết hiệu suất quá trình đạt $100\text{\%}$.",
                answer=["10,8", "10.8"],
                level="vandung",
                solution=r"Theo phương trình, cứ $2 \cdot 102 = 204\text{ tấn}$ $\text{Al}_2\text{O}_3$ tạo ra $4 \cdot 27 = 108\text{ tấn}$ $\text{Al}$. Vậy từ $20{,}4\text{ tấn}$ $\text{Al}_2\text{O}_3$ thu được khối lượng $\text{Al}$ là $m_{\text{Al}} = \dfrac{20{,}4 \cdot 108}{204} = 10{,}8\text{ tấn}$.",
            ),
        ],
        description="Dãy hoạt động hóa học của kim loại, ý nghĩa của dãy và các phương pháp tách kim loại từ quặng theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=3,
        code="H9-C03",
        title="Chương 3: Giới thiệu về phi kim và sự khác nhau giữa kim loại và phi kim",
        topic="phi-kim",
        summary=(
            r"Nắm vững tính chất vật lý, tính chất hóa học và ứng dụng của các phi kim quan trọng gồm carbon ($\text{C}$), sulfur ($\text{S}$), "
            r"chlorine ($\text{Cl}_2$), đồng thời so sánh được sự khác biệt về tính chất vật lý và tính chất hóa học giữa đơn chất kim loại và phi kim."
        ),
        objectives=[
            r"Trình bày được các dạng thù hình và ứng dụng thực tế của carbon ($\text{C}$: kim cương, than chì, than hoạt tính), sulfur ($\text{S}$) và khí chlorine ($\text{Cl}_2$).",
            r"Viết được các phương trình hóa học minh họa tính chất hóa học của phi kim: tác dụng với kim loại tạo muối hoặc oxide, tác dụng với hydrogen tạo hợp chất khí và tác dụng với oxygen tạo oxide acid.",
            r"So sánh được sự khác nhau về tính chất vật lý (trạng thái, tính dẫn điện, dẫn nhiệt, nhiệt độ nóng chảy, khối lượng riêng) giữa đơn chất kim loại và phi kim.",
            r"So sánh được sự khác nhau về tính chất hóa học (xu hướng nhường/nhận electron, bản chất oxide tạo thành) giữa kim loại và phi kim.",
        ],
        formulas=[
            {
                "name": "Phản ứng của phi kim với kim loại",
                "formula": r"$2\text{Na} + \text{Cl}_2 \xrightarrow{t^\circ} 2\text{NaCl}; \quad \text{Cu} + \text{Cl}_2 \xrightarrow{t^\circ} \text{CuCl}_2; \quad \text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$",
                "note": r"Phi kim oxi hóa kim loại tạo thành muối (hoặc oxide nếu phi kim là $\text{O}_2$)",
            },
            {
                "name": r"Phản ứng của phi kim với khí hydrogen ($\text{H}_2$)",
                "formula": r"$\text{H}_2 + \text{Cl}_2 \xrightarrow{\text{ánh sáng / }t^\circ} 2\text{HCl}; \quad \text{C} + 2\text{H}_2 \xrightarrow{t^\circ, xt} \text{CH}_4; \quad \text{H}_2 + \text{S} \xrightarrow{t^\circ} \text{H}_2\text{S}$",
                "note": r"Khí $\text{HCl}$ tan vào nước tạo dung dịch hydrochloric acid",
            },
            {
                "name": r"Phản ứng của phi kim ($\text{C}, \text{S}, \text{P}$) với khí oxygen ($\text{O}_2$)",
                "formula": r"$\text{C} + \text{O}_2 \xrightarrow{t^\circ} \text{CO}_2; \quad \text{S} + \text{O}_2 \xrightarrow{t^\circ} \text{SO}_2; \quad 4\text{P} + 5\text{O}_2 \xrightarrow{t^\circ} 2\text{P}_2\text{O}_5$",
                "note": r"Phi kim tác dụng với $\text{O}_2$ thường tạo ra oxide acid",
            },
            {
                "name": "Phản ứng của khí chlorine với nước và dung dịch kiềm",
                "formula": r"$\text{Cl}_2 + \text{H}_2\text{O} \xrightleftharpoons{} \text{HCl} + \text{HClO}; \quad \text{Cl}_2 + 2\text{NaOH} \longrightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$",
                "note": r"Dung dịch hỗn hợp $\text{NaCl}$ và $\text{NaClO}$ được gọi là nước Javel dùng để tẩy trắng, sát trùng",
            },
        ],
        theory_sections=[
            {
                "title": "1. Một số phi kim quan trọng và ứng dụng",
                "content": (
                    r"(1) Carbon ($\text{C}$): Tồn tại ở nhiều dạng thù hình như kim cương (cứng nhất, dùng làm đồ trang sức, mũi khoan), "
                    r"than chì/graphite (mềm, dẫn điện tốt, dùng làm điện cực, ruột bút chì) và carbon vô định hình (than hoạt tính có khả năng hấp phụ mạnh "
                    r"các chất khí, chất màu nên dùng trong mặt nạ phòng độc, máy lọc nước; than đá, than gỗ dùng làm nhiên liệu và chất khử). "
                    r"(2) Sulfur ($\text{S}$): Chất rắn màu vàng, không tan trong nước, dùng để sản xuất sulfuric acid ($\text{H}_2\text{SO}_4$), lưu hóa cao su, chế tạo diêm, thuốc trừ nấm. "
                    r"(3) Chlorine ($\text{Cl}_2$): Chất khí màu vàng lục, mùi hắc, rất độc, dùng để khử trùng nước sinh hoạt, sản xuất nước Javel, nhựa $\text{PVC}$ và hydrochloric acid."
                ),
            },
            {
                "title": "2. Tính chất hóa học của phi kim",
                "content": (
                    r"Các phi kim có ba tính chất hóa học điển hình: "
                    r"(1) Tác dụng với kim loại tạo thành muối (như $2\text{Fe} + 3\text{Cl}_2 \xrightarrow{t^\circ} 2\text{FeCl}_3$, $\text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$) "
                    r"hoặc tạo thành oxide base khi phi kim là oxygen ($2\text{Cu} + \text{O}_2 \xrightarrow{t^\circ} 2\text{CuO}$). "
                    r"(2) Tác dụng với hydrogen ($\text{H}_2$) tạo thành hợp chất khí như $\text{HCl}, \text{H}_2\text{S}, \text{NH}_3, \text{CH}_4, \text{H}_2\text{O}$. "
                    r"(3) Tác dụng với oxygen ($\text{O}_2$) thường tạo thành các oxide acid như $\text{CO}_2, \text{SO}_2, \text{P}_2\text{O}_5$ "
                    r"(khi cháy trong điều kiện thiếu oxygen, carbon tạo ra khí độc $\text{CO}$: $2\text{C} + \text{O}_2 \xrightarrow{t^\circ} 2\text{CO}$)."
                ),
            },
            {
                "title": "3. Sự khác nhau cơ bản giữa kim loại và phi kim",
                "content": (
                    r"Về tính chất vật lý: Ở điều kiện chuẩn ($25^\circ\text{C}, 1\text{ bar}$), kim loại (trừ $\text{Hg}$) đều ở thể rắn, có ánh kim, dẻo, "
                    r"dẫn điện và dẫn nhiệt tốt; ngược lại, phi kim có thể tồn tại ở cả 3 trạng thái: khí ($\text{H}_2, \text{O}_2, \text{N}_2, \text{F}_2, \text{Cl}_2$), "
                    r"lỏng ($\text{Br}_2$) và rắn ($\text{C}, \text{S}, \text{P}, \text{I}_2, \text{Si}$), phần lớn không dẫn điện (trừ than chì), không dẫn nhiệt, giòn và không có ánh kim. "
                    r"Về tính chất hóa học: Trong các phản ứng, nguyên tử kim loại có xu hướng nhường electron để tạo ion dương (cation $\text{M}^{n+}$) và tạo ra oxide base; "
                    r"ngược lại, nguyên tử phi kim có xu hướng nhận electron để tạo ion âm (anion $\text{X}^{m-}$) khi tác dụng với kim loại và tạo ra oxide acid khi tác dụng với oxygen."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Đốt cháy hoàn toàn $6{,}4\text{ g}$ bột sulfur ($\text{S}$, $M = 32\text{ g/mol}$) trong bình chứa khí oxygen ($\text{O}_2$) dư. "
                    r"Tính thể tích khí $\text{O}_2$ đã phản ứng và thể tích khí $\text{SO}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$)."
                ),
                "solution": (
                    r"Số mol $\text{S}$ là $n_{\text{S}} = \dfrac{6{,}4}{32} = 0{,}2\text{ mol}$. Phương trình hóa học: $\text{S} + \text{O}_2 \xrightarrow{t^\circ} \text{SO}_2\uparrow$. "
                    r"Theo phương trình, $n_{\text{O}_2} = n_{\text{SO}_2} = n_{\text{S}} = 0{,}2\text{ mol}$. Vậy thể tích khí $\text{O}_2$ phản ứng bằng thể tích khí $\text{SO}_2$ "
                    r"thu được ở đkc và bằng $V = 24{,}79 \cdot 0{,}2 = 4{,}958\text{ L}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Dẫn $2{,}479\text{ L}$ khí chlorine ($\text{Cl}_2$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) vào dung dịch $\text{NaOH}$ dư ở nhiệt độ thường "
                    r"để điều chế nước Javel theo phương trình $\text{Cl}_2 + 2\text{NaOH} \longrightarrow \text{NaCl} + \text{NaClO} + \text{H}_2\text{O}$. "
                    r"Tính tổng khối lượng hai muối $\text{NaCl}$ ($M = 58{,}5\text{ g/mol}$) và $\text{NaClO}$ ($M = 74{,}5\text{ g/mol}$) tạo thành."
                ),
                "solution": (
                    r"Số mol $\text{Cl}_2$ ở đkc là $n_{\text{Cl}_2} = \dfrac{2{,}479}{24{,}79} = 0{,}1\text{ mol}$. Theo phương trình hóa học, "
                    r"$n_{\text{NaCl}} = n_{\text{NaClO}} = n_{\text{Cl}_2} = 0{,}1\text{ mol}$. Tổng khối lượng hai muối tạo thành là "
                    r"$m = 0{,}1 \cdot (58{,}5 + 74{,}5) = 0{,}1 \cdot 133 = 13{,}3\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Ở điều kiện thường, phi kim tồn tại ở cả 3 thể: khí ($\text{H}_2, \text{O}_2, \text{N}_2, \text{Cl}_2$), lỏng ($\text{Br}_2$) và rắn ($\text{C}, \text{S}, \text{P}, \text{I}_2$); chỉ có than chì (dạng thù hình của $\text{C}$) dẫn điện tốt.",
            r"Khi tham gia phản ứng với nhau, nguyên tử kim loại nhường electron tạo ion dương ($\text{M}^{n+}$), còn nguyên tử phi kim nhận electron tạo ion âm ($\text{X}^{m-}$).",
            r"Oxide của kim loại thường là oxide base (như $\text{CaO}, \text{CuO}$), trong khi oxide của phi kim thường là oxide acid (như $\text{CO}_2, \text{SO}_2, \text{P}_2\text{O}_5$).",
        ],
        questions=[
            mcq(
                question=r"Ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$), đơn chất phi kim duy nhất tồn tại ở trạng thái lỏng là:",
                options=[
                    r"Chlorine ($\text{Cl}_2$)",
                    r"Bromine ($\text{Br}_2$)",
                    r"Sulfur ($\text{S}$)",
                    r"Iodine ($\text{I}_2$)",
                ],
                answer="B",
                level="biet",
                solution=r"Ở điều kiện thường, $\text{Br}_2$ là chất lỏng màu nâu đỏ, $\text{Cl}_2$ là chất khí màu vàng lục, còn $\text{S}$ và $\text{I}_2$ là chất rắn.",
            ),
            mcq(
                question=r"Vật liệu nào sau đây là một dạng của carbon vô định hình có tính hấp phụ cao, được dùng trong mặt nạ phòng độc và lõi lọc nước?",
                options=[r"Kim cương", r"Than hoạt tính", r"Đá vôi", r"Thạch anh"],
                answer="B",
                level="biet",
                solution=r"Than hoạt tính có cấu trúc xốp rỗng với diện tích bề mặt rất lớn nên hấp phụ mạnh các chất khí độc và chất màu hòa tan.",
            ),
            mcq(
                question=r"Trong phản ứng giữa kim loại sodium ($\text{Na}$) và khí chlorine ($\text{Cl}_2$) tạo thành muối ăn ($\text{NaCl}$), nguyên tử $\text{Cl}$ thể hiện xu hướng nào?",
                options=[
                    r"Nhường $1$ electron để tạo thành ion dương $\text{Cl}^+$",
                    r"Nhận $1$ electron để tạo thành ion âm $\text{Cl}^-$",
                    r"Nhường $2$ electron để tạo thành ion dương $\text{Cl}^{2+}$",
                    r"Không nhường và không nhận electron",
                ],
                answer="B",
                level="biet",
                solution=r"Trong phản ứng giữa kim loại và phi kim, nguyên tử $\text{Na}$ nhường $1\text{ e}$ tạo $\text{Na}^+$, còn nguyên tử $\text{Cl}$ nhận $1\text{ e}$ tạo ion $\text{Cl}^-$.",
            ),
            mcq(
                question=r"Ứng dụng quan trọng của bột lưu huỳnh (sulfur, $\text{S}$) trong công nghiệp chế biến cao su là:",
                options=[
                    r"Làm chất tẩy trắng cao su",
                    r"Lưu hóa cao su để tăng tính đàn hồi và độ bền nhiệt",
                    r"Làm chất dẫn điện cho cao su",
                    r"Hòa tan cao su thành dung dịch",
                ],
                answer="B",
                level="biet",
                solution=r"Sulfur ($\text{S}$) được dùng để lưu hóa cao su, tạo cầu nối disulfide giữa các mạch polymer giúp cao su bền và đàn hồi tốt.",
            ),
            mcq(
                question=r"Mặc dù đều là đơn chất phi kim, nhưng dạng thù hình nào sau đây của nguyên tố carbon ($\text{C}$) lại có khả năng dẫn điện tốt và được dùng làm điện cực?",
                options=[
                    r"Kim cương",
                    r"Than chì (graphite)",
                    r"Than gỗ",
                    r"Than muội",
                ],
                answer="B",
                level="hieu",
                solution=r"Than chì (graphite) có cấu trúc lớp với các electron tự do di chuyển giữa các lớp nên dẫn điện tốt, khác với hầu hết các phi kim khác.",
            ),
            mcq(
                question=r"Nhận xét nào sau đây đúng khi so sánh tính chất hóa học của đơn chất kim loại và đơn chất phi kim?",
                options=[
                    r"Kim loại tác dụng với oxygen thường tạo oxide acid, còn phi kim tạo oxide base",
                    r"Kim loại tác dụng với oxygen thường tạo oxide base, còn phi kim tác dụng với oxygen thường tạo oxide acid",
                    r"Cả kim loại và phi kim đều dễ dàng tác dụng với dung dịch $\text{HCl}$ giải phóng khí $\text{H}_2$",
                    r"Trong phản ứng với kim loại, nguyên tử phi kim luôn nhường electron tạo ion dương",
                ],
                answer="B",
                level="hieu",
                solution=r"Đa số kim loại tác dụng với $\text{O}_2$ tạo oxide base ($\text{CaO}, \text{CuO}, \text{Fe}_2\text{O}_3$), còn phi kim tác dụng với $\text{O}_2$ thường tạo oxide acid ($\text{CO}_2, \text{SO}_2, \text{P}_2\text{O}_5$).",
            ),
            tf4(
                stem=r"Khảo sát tính chất và ứng dụng của đơn chất khí chlorine ($\text{Cl}_2$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$), khí $\text{Cl}_2$ có màu vàng lục, mùi hắc, độc và nặng hơn không khí.",
                    r"b) Khí $\text{Cl}_2$ chỉ tác dụng được với các kim loại hoạt động mạnh như $\text{Na}, \text{Mg}$ mà không tác dụng được với $\text{Fe}$ hay $\text{Cu}$.",
                    r"c) Khi dẫn khí $\text{Cl}_2$ vào nước, một phần $\text{Cl}_2$ tác dụng với nước tạo hỗn hợp $\text{HCl}$ và $\text{HClO}$ có tính tẩy màu và diệt khuẩn.",
                    r"d) Khi thu khí $\text{Cl}_2$ trong phòng thí nghiệm bằng phương pháp đẩy không khí, người ta phải đặt úp bình thu.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $M_{\text{Cl}_2} = 71\text{ g/mol} > 29\text{ g/mol}$ nên khí $\text{Cl}_2$ nặng hơn không khí khoảng $2{,}45$ lần. "
                    r"b) Sai vì $\text{Cl}_2$ phản ứng với hầu hết kim loại kể cả $\text{Fe}$ (tạo $\text{FeCl}_3$) và $\text{Cu}$ (tạo $\text{CuCl}_2$) khi đun nóng. "
                    r"c) Đúng vì $\text{Cl}_2 + \text{H}_2\text{O} \xrightleftharpoons{} \text{HCl} + \text{HClO}$, trong đó $\text{HClO}$ có tính oxi hóa mạnh nên tẩy màu và sát trùng. "
                    r"d) Sai vì khí $\text{Cl}_2$ nặng hơn không khí nên phải đặt đứng (ngửa) bình thu."
                ),
            ),
            tf4(
                stem=r"So sánh các tính chất đặc trưng giữa hai nhóm nguyên tố kim loại và phi kim. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Hầu hết các kim loại có nhiệt độ nóng chảy và khối lượng riêng lớn hơn so với các phi kim ở cùng điều kiện.",
                    r"b) Tất cả các đơn chất phi kim đều tồn tại ở trạng thái khí ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$).",
                    r"c) Đốt cháy carbon ($\text{C}$) hoặc sulfur ($\text{S}$) trong khí $\text{O}_2$ dư đều thu được các oxide acid ($\text{CO}_2, \text{SO}_2$).",
                    r"d) Khi cho bột sulfur ($\text{S}$) vào dung dịch $\text{HCl}$ loãng ở nhiệt độ thường thấy thoát ra khí $\text{H}_2$ rất mạnh.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì đa số kim loại có cấu trúc tinh thể đặc khít, nhiệt độ nóng chảy và khối lượng riêng cao hơn phi kim. "
                    r"b) Sai vì phi kim có cả chất khí ($\text{O}_2, \text{Cl}_2$), chất lỏng ($\text{Br}_2$) và chất rắn ($\text{C}, \text{S}, \text{P}$). "
                    r"c) Đúng vì $\text{CO}_2$ và $\text{SO}_2$ đều thuộc loại oxide acid. "
                    r"d) Sai vì phi kim không tác dụng với dung dịch $\text{HCl}$ để giải phóng khí $\text{H}_2$."
                ),
            ),
            mcq(
                question=r"Đốt nóng một hỗn hợp gồm $5{,}6\text{ g}$ bột iron ($\text{Fe}$, $M = 56\text{ g/mol}$) và $4{,}0\text{ g}$ bột sulfur ($\text{S}$, $M = 32\text{ g/mol}$) trong bình kín không có không khí theo phản ứng $\text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$ (giả sử hiệu suất đạt $100\text{\%}$). Khối lượng muối $\text{FeS}$ ($M = 88\text{ g/mol}$) tạo thành là:",
                options=[r"$8{,}8\text{ g}$", r"$9{,}6\text{ g}$", r"$11{,}0\text{ g}$", r"$14{,}4\text{ g}$"],
                answer="A",
                level="vandung",
                solution=r"Ta có $n_{\text{Fe}} = \dfrac{5{,}6}{56} = 0{,}1\text{ mol}$ và $n_{\text{S}} = \dfrac{4{,}0}{32} = 0{,}125\text{ mol}$. Vì tỉ lệ phản ứng là $1 : 1$ và $0{,}1 < 0{,}125$, nên $\text{Fe}$ phản ứng hết, $\text{S}$ còn dư. Số mol $\text{FeS}$ tạo thành là $n_{\text{FeS}} = n_{\text{Fe}} = 0{,}1\text{ mol}$, suy ra $m_{\text{FeS}} = 0{,}1 \cdot 88 = 8{,}8\text{ g}$.",
            ),
            short(
                question=r"Đốt cháy hoàn toàn $3{,}6\text{ g}$ carbon ($\text{C}$, $M = 12\text{ g/mol}$) trong bình chứa khí oxygen ($\text{O}_2$) dư theo phản ứng $\text{C} + \text{O}_2 \xrightarrow{t^\circ} \text{CO}_2\uparrow$. Tính thể tích khí $\text{CO}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$, theo đơn vị $\text{L}$).",
                answer=["7,437", "7.437"],
                level="vandung",
                solution=r"Số mol carbon là $n_{\text{C}} = \dfrac{3{,}6}{12} = 0{,}3\text{ mol}$. Theo phương trình hóa học, $n_{\text{CO}_2} = n_{\text{C}} = 0{,}3\text{ mol}$. Thể tích khí $\text{CO}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}3 = 7{,}437\text{ L}$.",
            ),
        ],
        description="Tính chất vật lý, tính chất hóa học và ứng dụng của phi kim C, S, Cl2 và so sánh sự khác nhau giữa kim loại với phi kim theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=4,
        code="H9-C04",
        title="Chương 4: Đại cương về hợp chất hữu cơ và cấu tạo phân tử",
        topic="acid-bazo-muoi",
        summary=(
            r"Nắm vững khái niệm hợp chất hữu cơ, cách phân loại thành hydrocarbon và dẫn xuất của hydrocarbon, "
            r"công thức phân tử và công thức cấu tạo (đầy đủ, thu gọn), cùng đặc điểm liên kết cộng hóa trị và hóa trị "
            r"của các nguyên tố ($\text{C}$ hóa trị $\text{IV}$, $\text{H}$ hóa trị $\text{I}$, $\text{O}$ hóa trị $\text{II}$) trong ba loại mạch carbon (mạch hở thẳng, mạch nhánh, mạch vòng)."
        ),
        objectives=[
            r"Nêu được khái niệm hợp chất hữu cơ (hợp chất của carbon, trừ $\text{CO}, \text{CO}_2$, muối carbonate, cyanide, carbide...) và phân loại được hydrocarbon với dẫn xuất của hydrocarbon.",
            r"Phân biệt được công thức phân tử và công thức cấu tạo (dạng đầy đủ và dạng thu gọn), giải thích được ý nghĩa của công thức cấu tạo.",
            r"Vận dụng được quy tắc hóa trị trong hợp chất hữu cơ ($\text{C}$ luôn có hóa trị $\text{IV}$, $\text{H}$ hóa trị $\text{I}$, $\text{O}$ hóa trị $\text{II}$, $\text{Cl}$ hóa trị $\text{I}$) để viết công thức cấu tạo.",
            r"Nhận biết được ba dạng mạch carbon: mạch hở không phân nhánh (mạch thẳng), mạch hở phân nhánh và mạch vòng.",
        ],
        formulas=[
            {
                "name": "Phân loại hợp chất hữu cơ theo thành phần nguyên tố",
                "formula": r"$\text{Hydrocarbon: }\text{C}_x\text{H}_y \quad (\text{chỉ gồm }\text{C}, \text{H}); \quad \text{Dẫn xuất: }\text{C}_x\text{H}_y\text{O}_z\text{N}_t\text{X}_u\dots$",
                "note": r"Ví dụ hydrocarbon: $\text{CH}_4, \text{C}_2\text{H}_4, \text{C}_6\text{H}_6$; dẫn xuất: $\text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{COOH}, \text{CH}_3\text{Cl}$",
            },
            {
                "name": "Hóa trị không đổi của các nguyên tố trong hợp chất hữu cơ",
                "formula": r"$\text{C}\text{ (hóa trị }\text{IV}\text{, 4 gạch liên kết)}; \quad \text{O}\text{ (hóa trị }\text{II}\text{, 2 gạch)}; \quad \text{H}, \text{Cl}, \text{Br}\text{ (hóa trị }\text{I}\text{, 1 gạch)}$",
                "note": r"Mỗi gạch nối biểu diễn một liên kết cộng hóa trị giữa hai nguyên tử",
            },
            {
                "name": r"Công thức cấu tạo thu gọn của hai chất đồng phân ứng với $\text{C}_2\text{H}_6\text{O}$",
                "formula": r"$\text{CH}_3-\text{CH}_2-\text{OH}\text{ (ethylic alcohol)} \quad \text{và} \quad \text{CH}_3-\text{O}-\text{CH}_3\text{ (dimethyl ether)}$",
                "note": r"Cùng công thức phân tử $\text{C}_2\text{H}_6\text{O}$ nhưng thứ tự liên kết khác nhau nên tính chất khác nhau",
            },
            {
                "name": r"Tính số mol $\text{CO}_2$ và $\text{H}_2\text{O}$ khi đốt cháy hoàn toàn hợp chất hữu cơ",
                "formula": r"$n_{\text{C}} = n_{\text{CO}_2}; \quad n_{\text{H}} = 2 \cdot n_{\text{H}_2\text{O}}; \quad m_{\text{O (trong hợp chất)}} = m_{\text{hợp chất}} - (m_{\text{C}} + m_{\text{H}})$",
                "note": r"$m_{\text{C}} = 12 \cdot n_{\text{CO}_2}$ và $m_{\text{H}} = 2 \cdot n_{\text{H}_2\text{O}}$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Khái niệm và phân loại hợp chất hữu cơ",
                "content": (
                    r"Hợp chất hữu cơ là hợp chất của carbon (trừ một số hợp chất vô cơ của carbon như các oxide $\text{CO}, \text{CO}_2$, "
                    r"acid $\text{H}_2\text{CO}_3$, các muối carbonate $\text{CaCO}_3, \text{Na}_2\text{CO}_3$, muối hydrogencarbonate $\text{NaHCO}_3$, "
                    r"các carbide như $\text{CaC}_2$). Dựa vào thành phần nguyên tố, hợp chất hữu cơ được chia thành hai loại chính: "
                    r"(1) Hydrocarbon: phân tử chỉ chứa hai nguyên tố là carbon ($\text{C}$) và hydrogen ($\text{H}$), ví dụ $\text{CH}_4, \text{C}_2\text{H}_4, \text{C}_2\text{H}_2, \text{C}_3\text{H}_8$. "
                    r"(2) Dẫn xuất của hydrocarbon: ngoài $\text{C}$ và $\text{H}$, trong phân tử còn có nguyên tử của các nguyên tố khác như $\text{O}, \text{N}, \text{Cl}, \text{S}$..., "
                    r"ví dụ $\text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{COOH}, \text{CH}_3\text{Cl}, \text{C}_6\text{H}_{12}\text{O}_6$."
                ),
            },
            {
                "title": "2. Đặc điểm cấu tạo phân tử hợp chất hữu cơ",
                "content": (
                    r"Trong các hợp chất hữu cơ, liên kết hóa học chủ yếu là liên kết cộng hóa trị. Nguyên tử carbon ($\text{C}$) luôn có hóa trị $\text{IV}$ "
                    r"(xung quanh nguyên tử $\text{C}$ luôn có đủ $4$ gạch liên kết), nguyên tử hydrogen ($\text{H}$) và halogen ($\text{Cl}, \text{Br}$) có hóa trị $\text{I}$, "
                    r"nguyên tử oxygen ($\text{O}$) có hóa trị $\text{II}$. Các nguyên tử carbon không những liên kết với nguyên tử của nguyên tố khác mà còn "
                    r"liên kết trực tiếp với nhau tạo thành mạch carbon (liên kết đơn $\text{C}-\text{C}$, liên kết đôi $\text{C}=\text{C}$, liên kết ba $\text{C}\equiv\text{C}$). "
                    r"Có ba dạng mạch carbon: mạch hở không phân nhánh (mạch thẳng), mạch hở phân nhánh (mạch nhánh) và mạch vòng."
                ),
            },
            {
                "title": "3. Công thức phân tử và công thức cấu tạo",
                "content": (
                    r"Công thức phân tử cho biết thành phần nguyên tố và số lượng nguyên tử của mỗi nguyên tố trong phân tử (ví dụ $\text{C}_2\text{H}_6\text{O}$). "
                    r"Công thức cấu tạo biểu diễn đầy đủ thứ tự và cách thức liên kết (liên kết đơn, liên kết bội) giữa các nguyên tử trong phân tử. "
                    r"Công thức cấu tạo thu gọn viết gộp nguyên tử $\text{C}$ và các nguyên tử $\text{H}$ liên kết trực tiếp với nó thành từng nhóm (như $\text{CH}_3-\text{CH}_2-\text{OH}$). "
                    r"Mỗi hợp chất hữu cơ có một trật tự liên kết xác định giữa các nguyên tử; nếu thay đổi trật tự đó sẽ tạo ra chất mới có tính chất khác."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Trong các chất sau: $\text{CH}_4, \text{CO}_2, \text{C}_2\text{H}_5\text{OH}, \text{CaCO}_3, \text{C}_2\text{H}_4, \text{CH}_3\text{Cl}, \text{NaHCO}_3, \text{C}_3\text{H}_8$, "
                    r"hãy phân loại chất nào là hợp chất vô cơ, chất nào là hydrocarbon và chất nào là dẫn xuất của hydrocarbon."
                ),
                "solution": (
                    r"- Hợp chất vô cơ: $\text{CO}_2, \text{CaCO}_3, \text{NaHCO}_3$. "
                    r"- Hợp chất hữu cơ thuộc nhóm hydrocarbon (chỉ chứa $\text{C}$ và $\text{H}$): $\text{CH}_4, \text{C}_2\text{H}_4, \text{C}_3\text{H}_8$. "
                    r"- Hợp chất hữu cơ thuộc nhóm dẫn xuất của hydrocarbon (có thêm $\text{O}, \text{Cl}$): $\text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{Cl}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Đốt cháy hoàn toàn $4{,}6\text{ g}$ một hợp chất hữu cơ $\text{A}$ (chứa $\text{C}, \text{H}, \text{O}$, có khối lượng phân tử $M_{\text{A}} = 46\text{ g/mol}$) "
                    r"thu được $4{,}958\text{ L}$ khí $\text{CO}_2$ (ở đkc $25^\circ\text{C}$, $1\text{ bar}$) và $5{,}4\text{ g}$ $\text{H}_2\text{O}$. "
                    r"Xác định công thức phân tử của $\text{A}$."
                ),
                "solution": (
                    r"Ta có $n_{\text{CO}_2} = \dfrac{4{,}958}{24{,}79} = 0{,}2\text{ mol} \Rightarrow n_{\text{C}} = 0{,}2\text{ mol}, m_{\text{C}} = 0{,}2 \cdot 12 = 2{,}4\text{ g}$. "
                    r"Số mol $\text{H}_2\text{O}$ là $n_{\text{H}_2\text{O}} = \dfrac{5{,}4}{18} = 0{,}3\text{ mol} \Rightarrow n_{\text{H}} = 2 \cdot 0{,}3 = 0{,}6\text{ mol}, m_{\text{H}} = 0{,}6\text{ g}$. "
                    r"Khối lượng $\text{O}$ trong $\text{A}$ là $m_{\text{O}} = 4{,}6 - (2{,}4 + 0{,}6) = 1{,}6\text{ g} \Rightarrow n_{\text{O}} = \dfrac{1{,}6}{16} = 0{,}1\text{ mol}$. "
                    r"Số mol của $\text{A}$ là $n_{\text{A}} = \dfrac{4{,}6}{46} = 0{,}1\text{ mol}$. Tỉ lệ $x : y : z = \dfrac{0{,}2}{0{,}1} : \dfrac{0{,}6}{0{,}1} : \dfrac{0{,}1}{0{,}1} = 2 : 6 : 1$. "
                    r"Vậy công thức phân tử của $\text{A}$ là $\text{C}_2\text{H}_6\text{O}$."
                ),
            },
        ],
        key_takeaways=[
            r"Hợp chất hữu cơ là hợp chất của carbon (trừ $\text{CO}, \text{CO}_2, \text{H}_2\text{CO}_3$, muối carbonate...), chia thành hai nhóm: hydrocarbon (chỉ chứa $\text{C}, \text{H}$) và dẫn xuất của hydrocarbon.",
            r"Trong hợp chất hữu cơ, $\text{C}$ luôn có hóa trị $\text{IV}$, $\text{O}$ có hóa trị $\text{II}$, $\text{H}$ và $\text{Cl}$ có hóa trị $\text{I}$.",
            r"Công thức cấu tạo cho biết trật tự và cách thức liên kết giữa các nguyên tử, quyết định tính chất hóa học của chất hữu cơ.",
        ],
        questions=[
            mcq(
                question=r"Chất nào sau đây là một hợp chất hữu cơ?",
                options=[r"$\text{CaCO}_3$", r"$\text{CO}_2$", r"$\text{CH}_4$", r"$\text{NaHCO}_3$"],
                answer="C",
                level="biet",
                solution=r"$\text{CH}_4$ (methane) là hợp chất hữu cơ (hydrocarbon), còn $\text{CaCO}_3, \text{CO}_2, \text{NaHCO}_3$ là các hợp chất vô cơ của carbon.",
            ),
            mcq(
                question=r"Dãy gồm các chất đều thuộc loại dẫn xuất của hydrocarbon là:",
                options=[
                    r"$\text{CH}_4, \text{C}_2\text{H}_4, \text{C}_2\text{H}_6$",
                    r"$\text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{COOH}, \text{CH}_3\text{Cl}$",
                    r"$\text{C}_2\text{H}_4, \text{C}_2\text{H}_5\text{OH}, \text{C}_3\text{H}_8$",
                    r"$\text{CO}, \text{CO}_2, \text{H}_2\text{CO}_3$",
                ],
                answer="B",
                level="biet",
                solution=r"Các chất $\text{C}_2\text{H}_5\text{OH}, \text{CH}_3\text{COOH}, \text{CH}_3\text{Cl}$ ngoài $\text{C}$ và $\text{H}$ còn chứa nguyên tố $\text{O}$ hoặc $\text{Cl}$ nên đều là dẫn xuất của hydrocarbon.",
            ),
            mcq(
                question=r"Trong các hợp chất hữu cơ, nguyên tử carbon ($\text{C}$), oxygen ($\text{O}$) và hydrogen ($\text{H}$) lần lượt có hóa trị bằng:",
                options=[
                    r"$\text{IV}, \text{II}, \text{I}$",
                    r"$\text{II}, \text{IV}, \text{I}$",
                    r"$\text{IV}, \text{I}, \text{II}$",
                    r"$\text{III}, \text{II}, \text{I}$",
                ],
                answer="A",
                level="biet",
                solution=r"Trong hợp chất hữu cơ, nguyên tử $\text{C}$ luôn có hóa trị $\text{IV}$, $\text{O}$ có hóa trị $\text{II}$ và $\text{H}$ có hóa trị $\text{I}$.",
            ),
            mcq(
                question=r"Công thức cấu tạo thu gọn $\text{CH}_3-\text{CH}(\text{CH}_3)-\text{CH}_3$ biểu diễn mạch carbon thuộc loại nào sau đây?",
                options=[
                    r"Mạch hở không phân nhánh (mạch thẳng)",
                    r"Mạch hở phân nhánh (mạch nhánh)",
                    r"Mạch vòng $4$ cạnh",
                    r"Mạch vòng $3$ cạnh",
                ],
                answer="B",
                level="biet",
                solution=r"Trong $\text{CH}_3-\text{CH}(\text{CH}_3)-\text{CH}_3$, nguyên tử $\text{C}$ ở giữa liên kết với $3$ nguyên tử $\text{C}$ khác tạo thành mạch hở phân nhánh.",
            ),
            mcq(
                question=r"Ứng với công thức phân tử $\text{C}_4\text{H}_{10}$ có bao nhiêu công thức cấu tạo mạch hở khác nhau?",
                options=[r"$1$", r"$2$", r"$3$", r"$4$"],
                answer="B",
                level="hieu",
                solution=r"Ứng với công thức phân tử $\text{C}_4\text{H}_{10}$ có $2$ công thức cấu tạo: mạch thẳng $\text{CH}_3-\text{CH}_2-\text{CH}_2-\text{CH}_3$ (butane) và mạch nhánh $\text{CH}_3-\text{CH}(\text{CH}_3)-\text{CH}_3$ (isobutane).",
            ),
            mcq(
                question=r"Công thức cấu tạo thu gọn nào sau đây viết đúng quy tắc hóa trị của các nguyên tố $\text{C}, \text{H}, \text{O}$?",
                options=[
                    r"$\text{CH}_3-\text{CH}_3-\text{OH}$",
                    r"$\text{CH}_3-\text{CH}_2-\text{OH}$",
                    r"$\text{CH}_2-\text{CH}_2-\text{OH}$",
                    r"$\text{CH}_3-\text{O}-\text{CH}_2$",
                ],
                answer="B",
                level="hieu",
                solution=r"Trong $\text{CH}_3-\text{CH}_2-\text{OH}$, mỗi nguyên tử $\text{C}$ đều có đủ $4$ liên kết (hóa trị $\text{IV}$), nguyên tử $\text{O}$ có $2$ liên kết (hóa trị $\text{II}$) và mỗi nguyên tử $\text{H}$ có $1$ liên kết (hóa trị $\text{I}$).",
            ),
            tf4(
                stem=r"Cho hai hợp chất hữu cơ có công thức cấu tạo thu gọn là chất $\text{X}$: $\text{CH}_3-\text{CH}_2-\text{OH}$ (ethylic alcohol) và chất $\text{Y}$: $\text{CH}_3-\text{O}-\text{CH}_3$ (dimethyl ether). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Cả hai chất $\text{X}$ và $\text{Y}$ đều có cùng công thức phân tử là $\text{C}_2\text{H}_6\text{O}$ và thuộc loại dẫn xuất của hydrocarbon.",
                    r"b) Trong phân tử chất $\text{Y}$ có chứa nhóm $-\text{OH}$ liên kết trực tiếp với nguyên tử hydrogen.",
                    r"c) Do có trật tự liên kết giữa các nguyên tử khác nhau nên ở điều kiện thường $\text{X}$ là chất lỏng (tan vô hạn trong nước, tác dụng với $\text{Na}$), còn $\text{Y}$ là chất khí (không tác dụng với $\text{Na}$).",
                    r"d) Trong phân tử chất $\text{X}$, nguyên tử oxygen ($\text{O}$) có hóa trị $\text{I}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì đếm số nguyên tử trong cả $\text{X}$ và $\text{Y}$ đều có $2$ nguyên tử $\text{C}$, $6$ nguyên tử $\text{H}$ và $1$ nguyên tử $\text{O}$ ($\text{C}_2\text{H}_6\text{O}$). "
                    r"b) Sai vì trong $\text{Y}$ ($\text{CH}_3-\text{O}-\text{CH}_3$), nguyên tử $\text{O}$ liên kết với hai nguyên tử $\text{C}$, không liên kết với $\text{H}$. "
                    r"c) Đúng vì sự khác nhau về công thức cấu tạo (trật tự liên kết) làm cho tính chất vật lý và hóa học của $\text{X}$ và $\text{Y}$ khác nhau. "
                    r"d) Sai vì trong cả $\text{X}$ và $\text{Y}$, nguyên tử $\text{O}$ luôn có hóa trị $\text{II}$ ($2$ liên kết đơn)."
                ),
            ),
            tf4(
                stem=r"Xét các hợp chất chứa nguyên tố carbon gồm: (1) $\text{CH}_4$, (2) $\text{C}_2\text{H}_4$, (3) $\text{C}_6\text{H}_{12}\text{O}_6$ (glucose), (4) $\text{Na}_2\text{CO}_3$, (5) $\text{CH}_3\text{COOH}$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Trong $5$ chất trên, có $4$ chất là hợp chất hữu cơ và $1$ chất là hợp chất vô cơ ($\text{Na}_2\text{CO}_3$).",
                    r"b) Cả ba chất $\text{CH}_4, \text{C}_2\text{H}_4$ và $\text{C}_6\text{H}_{12}\text{O}_6$ đều thuộc loại hydrocarbon.",
                    r"c) Hai chất $\text{C}_6\text{H}_{12}\text{O}_6$ và $\text{CH}_3\text{COOH}$ thuộc loại dẫn xuất của hydrocarbon vì phân tử có chứa thêm nguyên tố oxygen ($\text{O}$).",
                    r"d) Liên kết hóa học chủ yếu trong phân tử $\text{CH}_4$ và $\text{C}_2\text{H}_4$ là liên kết ion.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{Na}_2\text{CO}_3$ là muối carbonate vô cơ, $4$ chất còn lại là hợp chất hữu cơ. "
                    r"b) Sai vì $\text{C}_6\text{H}_{12}\text{O}_6$ có chứa nguyên tố $\text{O}$ nên là dẫn xuất của hydrocarbon, chỉ có $\text{CH}_4, \text{C}_2\text{H}_4$ là hydrocarbon. "
                    r"c) Đúng vì phân tử của chúng có nguyên tố $\text{O}$ ngoài $\text{C}$ và $\text{H}$. "
                    r"d) Sai vì liên kết trong phân tử hợp chất hữu cơ $\text{CH}_4, \text{C}_2\text{H}_4$ là liên kết cộng hóa trị."
                ),
            ),
            mcq(
                question=r"Đốt cháy hoàn toàn $3{,}0\text{ g}$ một hợp chất hữu cơ $\text{X}$ thu được $4{,}958\text{ L}$ khí $\text{CO}_2$ (ở đkc $25^\circ\text{C}$, $1\text{ bar}$) và $5{,}4\text{ g}$ $\text{H}_2\text{O}$ (biết $M_{\text{C}} = 12\text{ g/mol}$, $M_{\text{H}} = 1\text{ g/mol}$, $M_{\text{O}} = 16\text{ g/mol}$). Thành phần nguyên tố của hợp chất $\text{X}$ và tỉ lệ số mol $n_{\text{C}} : n_{\text{H}}$ trong $\text{X}$ là:",
                options=[
                    r"Chỉ gồm $\text{C}, \text{H}$ với tỉ lệ $n_{\text{C}} : n_{\text{H}} = 1 : 3$",
                    r"Chỉ gồm $\text{C}, \text{H}$ với tỉ lệ $n_{\text{C}} : n_{\text{H}} = 1 : 2$",
                    r"Gồm $\text{C}, \text{H}, \text{O}$ với tỉ lệ $n_{\text{C}} : n_{\text{H}} = 1 : 3$",
                    r"Chỉ gồm $\text{C}, \text{H}$ với tỉ lệ $n_{\text{C}} : n_{\text{H}} = 2 : 3$",
                ],
                answer="A",
                level="vandung",
                solution=r"Ta có $n_{\text{CO}_2} = \dfrac{4{,}958}{24{,}79} = 0{,}2\text{ mol} \Rightarrow n_{\text{C}} = 0{,}2\text{ mol}, m_{\text{C}} = 2{,}4\text{ g}$. Số mol $\text{H}_2\text{O}$ là $n_{\text{H}_2\text{O}} = \dfrac{5{,}4}{18} = 0{,}3\text{ mol} \Rightarrow n_{\text{H}} = 0{,}6\text{ mol}, m_{\text{H}} = 0{,}6\text{ g}$. Vì $m_{\text{C}} + m_{\text{H}} = 2{,}4 + 0{,}6 = 3{,}0\text{ g} = m_{\text{X}}$ nên $\text{X}$ chỉ gồm hai nguyên tố $\text{C}, \text{H}$ (là hydrocarbon) với tỉ lệ $n_{\text{C}} : n_{\text{H}} = 0{,}2 : 0{,}6 = 1 : 3$ ($\text{C}_2\text{H}_6$).",
            ),
            short(
                question=r"Một hydrocarbon $\text{A}$ có thành phần phần trăm khối lượng của nguyên tố carbon là $80\text{\%}$ và có khối lượng phân tử bằng $30\text{ amu}$ (biết $M_{\text{C}} = 12\text{ amu}$, $M_{\text{H}} = 1\text{ amu}$). Tính tổng số nguyên tử ($\text{C}$ và $\text{H}$) có trong một phân tử $\text{A}$.",
                answer=["8"],
                level="vandung",
                solution=r"Đặt công thức phân tử của $\text{A}$ là $\text{C}_x\text{H}_y$. Ta có $x = \dfrac{80 \cdot 30}{100 \cdot 12} = 2$ và $y = \dfrac{20 \cdot 30}{100 \cdot 1} = 6$. Công thức phân tử của $\text{A}$ là $\text{C}_2\text{H}_6$ (ethane), nên tổng số nguyên tử trong một phân tử là $2 + 6 = 8$.",
            ),
        ],
        description="Khái niệm hợp chất hữu cơ, phân loại hydrocarbon và dẫn xuất, công thức phân tử, công thức cấu tạo và quy tắc hóa trị theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=5,
        code="H9-C05",
        title="Chương 5: Hydrocarbon (Alkane, Alkene) và nguồn nhiên liệu",
        topic="hydrocarbon",
        summary=(
            r"Nắm vững khái niệm, công thức chung và tính chất của alkane ($\text{C}_n\text{H}_{2n+2}$, tiêu biểu là methane $\text{CH}_4$, ethane $\text{C}_2\text{H}_6$), "
            r"alkene ($\text{C}_n\text{H}_{2n}$, tiêu biểu là ethylene $\text{C}_2\text{H}_4$ có liên kết đôi $\text{C}=\text{C}$ làm mất màu dung dịch $\text{Br}_2$ và tham gia phản ứng trùng hợp), "
            r"cùng nguồn nhiên liệu hóa thạch (dầu mỏ, khí thiên nhiên, khí mỏ dầu và phương pháp chưng cất phân đoạn)."
        ),
        objectives=[
            r"Nêu được khái niệm alkane (hydrocarbon mạch hở chỉ chứa liên kết đơn, công thức chung $\text{C}_n\text{H}_{2n+2}$ với $n \ge 1$), viết được công thức cấu tạo và phương trình phản ứng cháy tỏa nhiệt của methane ($\text{CH}_4$), ethane ($\text{C}_2\text{H}_6$).",
            r"Nêu được khái niệm alkene (hydrocarbon mạch hở có một liên kết đôi $\text{C}=\text{C}$, công thức chung $\text{C}_n\text{H}_{2n}$ với $n \ge 2$), trình bày được cấu tạo và tính chất hóa học của ethylene ($\text{C}_2\text{H}_4$: phản ứng cháy, cộng $\text{Br}_2$, trùng hợp tạo $\text{PE}$).",
            r"Trình bày được thành phần chính của dầu mỏ, khí thiên nhiên, khí mỏ dầu (hàm lượng $\text{CH}_4$ cao) và nguyên tắc chưng cất phân đoạn dầu mỏ.",
            r"Giải thích được cách sử dụng nhiên liệu an toàn, tiết kiệm, hiệu quả và giảm phát thải khí nhà kính bảo vệ môi trường.",
        ],
        formulas=[
            {
                "name": r"Phản ứng đốt cháy hoàn toàn alkane ($\text{C}_n\text{H}_{2n+2}$, $n \ge 1$)",
                "formula": r"$\text{C}_n\text{H}_{2n+2} + \dfrac{3n+1}{2}\text{O}_2 \xrightarrow{t^\circ} n\text{CO}_2 + (n+1)\text{H}_2\text{O} \quad (\text{ví dụ: }\text{CH}_4 + 2\text{O}_2 \xrightarrow{t^\circ} \text{CO}_2 + 2\text{H}_2\text{O})$",
                "note": r"Khi đốt cháy hoàn toàn alkane luôn có $n_{\text{H}_2\text{O}} > n_{\text{CO}_2}$ và $n_{\text{alkane}} = n_{\text{H}_2\text{O}} - n_{\text{CO}_2}$",
            },
            {
                "name": r"Phản ứng đốt cháy hoàn toàn alkene ($\text{C}_n\text{H}_{2n}$, $n \ge 2$)",
                "formula": r"$\text{C}_n\text{H}_{2n} + \dfrac{3n}{2}\text{O}_2 \xrightarrow{t^\circ} n\text{CO}_2 + n\text{H}_2\text{O} \quad (\text{ví dụ: }\text{C}_2\text{H}_4 + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{CO}_2 + 2\text{H}_2\text{O})$",
                "note": r"Khi đốt cháy hoàn toàn alkene luôn có $n_{\text{CO}_2} = n_{\text{H}_2\text{O}}$",
            },
            {
                "name": r"Phản ứng cộng bromine ($\text{Br}_2$) của ethylene",
                "formula": r"$\text{CH}_2=\text{CH}_2 + \text{Br}_2\text{ (da cam)} \longrightarrow \text{Br}-\text{CH}_2-\text{CH}_2-\text{Br}\text{ (không màu)}$",
                "note": r"Dùng dung dịch $\text{Br}_2$ để nhận biết và phân biệt ethylene ($\text{C}_2\text{H}_4$) với methane ($\text{CH}_4$)",
            },
            {
                "name": r"Phản ứng trùng hợp ethylene tạo nhựa polyethylene ($\text{PE}$)",
                "formula": r"$n\text{CH}_2=\text{CH}_2 \xrightarrow{t^\circ, p, xt} \left(-\text{CH}_2-\text{CH}_2-\right)_n$",
                "note": r"Liên kết kém bền trong nối đôi $\text{C}=\text{C}$ đứt ra để các phân tử $\text{C}_2\text{H}_4$ kết hợp với nhau",
            },
        ],
        theory_sections=[
            {
                "title": "1. Alkane — Methane và Ethane",
                "content": (
                    r"Alkane là những hydrocarbon mạch hở mà trong phân tử chỉ chứa các liên kết đơn ($\text{C}-\text{C}$ và $\text{C}-\text{H}$), "
                    r"có công thức phân tử chung là $\text{C}_n\text{H}_{2n+2}$ ($n \ge 1$). Bốn alkane đầu dãy là methane ($\text{CH}_4$), "
                    r"ethane ($\text{C}_2\text{H}_6$, $\text{CH}_3-\text{CH}_3$), propane ($\text{C}_3\text{H}_8$) và butane ($\text{C}_4\text{H}_{10}$) đều là các chất khí không màu, "
                    r"không mùi, hầu như không tan trong nước. Khi đốt cháy hoàn toàn trong khí oxygen, alkane tạo thành khí $\text{CO}_2$ và hơi nước $\text{H}_2\text{O}$, "
                    r"đồng thời tỏa ra rất nhiều nhiệt nên được dùng làm nhiên liệu (khí thiên nhiên chứa chủ yếu $\text{CH}_4$, khí hóa lỏng $\text{LPG}$ chứa propane và butane)."
                ),
            },
            {
                "title": "2. Alkene — Ethylene",
                "content": (
                    r"Alkene là những hydrocarbon mạch hở trong phân tử có một liên kết đôi $\text{C}=\text{C}$, công thức phân tử chung là $\text{C}_n\text{H}_{2n}$ ($n \ge 2$). "
                    r"Chất tiêu biểu nhất là ethylene ($\text{C}_2\text{H}_4$, công thức cấu tạo thu gọn $\text{CH}_2=\text{CH}_2$) — chất khí không màu, không mùi, ít tan trong nước, "
                    r"nhẹ hơn không khí ($d = \dfrac{28}{29}$) và có tác dụng kích thích quả xanh mau chín. Trong liên kết đôi $\text{C}=\text{C}$ của ethylene có một liên kết kém bền "
                    r"dễ bị đứt ra trong các phản ứng hóa học, vì vậy ethylene có phản ứng cộng làm mất màu da cam của dung dịch nước bromine ($\text{C}_2\text{H}_4 + \text{Br}_2 \longrightarrow \text{C}_2\text{H}_4\text{Br}_2$), "
                    r"phản ứng trùng hợp tạo nhựa polyethylene ($\text{PE}$) và phản ứng cháy tỏa nhiều nhiệt."
                ),
            },
            {
                "title": "3. Nguồn nhiên liệu hóa thạch (Dầu mỏ và khí thiên nhiên)",
                "content": (
                    r"Dầu mỏ là hỗn hợp lỏng sánh, màu nâu đen, nhẹ hơn nước và không tan trong nước, chứa hàng trăm hydrocarbon khác nhau. "
                    r"Người ta chế biến dầu mỏ bằng phương pháp chưng cất phân đoạn (dựa vào nhiệt độ sôi khác nhau của các cấu tử) để thu được khí đốt, xăng, "
                    r"dầu hỏa, dầu diesel, dầu nhờn và nhựa đường; ngoài ra còn dùng phương pháp cracking (bẻ gãy mạch carbon dài thành mạch ngắn) để tăng sản lượng xăng. "
                    r"Khí thiên nhiên (chứa khoảng $95\text{\%}$ thể tích là $\text{CH}_4$) và khí mỏ dầu (chứa khoảng $75\text{\%}$ là $\text{CH}_4$) là các nguồn nhiên liệu sạch hơn than đá."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Dẫn $3{,}7185\text{ L}$ hỗn hợp khí gồm methane ($\text{CH}_4$) và ethylene ($\text{C}_2\text{H}_4$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) "
                    r"đi chậm qua bình đựng dung dịch bromine ($\text{Br}_2$) dư thì thấy khối lượng bình tăng thêm $2{,}8\text{ g}$ (biết $M_{\text{C}_2\text{H}_4} = 28\text{ g/mol}$). "
                    r"Tính thành phần phần trăm theo thể tích của mỗi khí trong hỗn hợp ban đầu."
                ),
                "solution": (
                    r"Tổng số mol hỗn hợp khí ở đkc là $n_{\text{hh}} = \dfrac{3{,}7185}{24{,}79} = 0{,}15\text{ mol}$. Khi dẫn qua bình dung dịch $\text{Br}_2$ dư, "
                    r"chỉ có $\text{C}_2\text{H}_4$ phản ứng và bị giữ lại làm khối lượng bình tăng $2{,}8\text{ g}$, nên $m_{\text{C}_2\text{H}_4} = 2{,}8\text{ g}$ "
                    r"$\Rightarrow n_{\text{C}_2\text{H}_4} = \dfrac{2{,}8}{28} = 0{,}1\text{ mol}$. Phần trăm thể tích bằng phần trăm số mol: "
                    r"$\text{\%}V_{\text{C}_2\text{H}_4} = \dfrac{0{,}1}{0{,}15} \cdot 100\text{\%} \approx 66{,}67\text{\%}$ và $\text{\%}V_{\text{CH}_4} \approx 33{,}33\text{\%}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Đốt cháy hoàn toàn $0{,}1\text{ mol}$ khí propane ($\text{C}_3\text{H}_8$) trong khí oxygen dư. Tính thể tích khí $\text{O}_2$ cần dùng "
                    r"ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) và khối lượng nước thu được."
                ),
                "solution": (
                    r"Phương trình hóa học: $\text{C}_3\text{H}_8 + 5\text{O}_2 \xrightarrow{t^\circ} 3\text{CO}_2 + 4\text{H}_2\text{O}$. "
                    r"Theo phương trình, $n_{\text{O}_2} = 5 \cdot n_{\text{C}_3\text{H}_8} = 0{,}5\text{ mol}$ và $n_{\text{H}_2\text{O}} = 4 \cdot 0{,}1 = 0{,}4\text{ mol}$. "
                    r"Thể tích khí $\text{O}_2$ ở đkc là $V_{\text{O}_2} = 24{,}79 \cdot 0{,}5 = 12{,}395\text{ L}$. Khối lượng nước thu được là $m_{\text{H}_2\text{O}} = 0{,}4 \cdot 18 = 7{,}2\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Alkane ($\text{C}_n\text{H}_{2n+2}$, như $\text{CH}_4, \text{C}_2\text{H}_6$) chỉ có liên kết đơn bền vững, phản ứng đặc trưng là phản ứng cháy tỏa nhiệt lớn.",
            r"Alkene ($\text{C}_n\text{H}_{2n}$, như $\text{C}_2\text{H}_4$) có một liên kết đôi $\text{C}=\text{C}$ chứa một liên kết kém bền nên dễ tham gia phản ứng cộng làm mất màu dung dịch $\text{Br}_2$ và phản ứng trùng hợp.",
            r"Khí thiên nhiên và khí mỏ dầu có thành phần chính là methane ($\text{CH}_4$); chưng cất phân đoạn dầu mỏ dựa trên sự khác nhau về nhiệt độ sôi của các phân đoạn hydrocarbon.",
        ],
        questions=[
            mcq(
                question=r"Công thức phân tử chung của dãy đồng đẳng alkane (hydrocarbon mạch hở chỉ có liên kết đơn) là:",
                options=[
                    r"$\text{C}_n\text{H}_{2n+2}$ ($n \ge 1$)",
                    r"$\text{C}_n\text{H}_{2n}$ ($n \ge 2$)",
                    r"$\text{C}_n\text{H}_{2n-2}$ ($n \ge 2$)",
                    r"$\text{C}_n\text{H}_{2n-6}$ ($n \ge 6$)",
                ],
                answer="A",
                level="biet",
                solution=r"Alkane là hydrocarbon mạch hở chỉ chứa liên kết đơn, có công thức chung là $\text{C}_n\text{H}_{2n+2}$ với $n \ge 1$.",
            ),
            mcq(
                question=r"Trong phân tử ethylene ($\text{C}_2\text{H}_4$, công thức cấu tạo thu gọn $\text{CH}_2=\text{CH}_2$) có đặc điểm liên kết là:",
                options=[
                    r"Chỉ có các liên kết đơn",
                    r"Có một liên kết đôi $\text{C}=\text{C}$ và bốn liên kết đơn $\text{C}-\text{H}$",
                    r"Có một liên kết ba $\text{C}\equiv\text{C}$ và hai liên kết đơn $\text{C}-\text{H}$",
                    r"Có hai liên kết đôi $\text{C}=\text{C}$",
                ],
                answer="B",
                level="biet",
                solution=r"Phân tử ethylene ($\text{CH}_2=\text{CH}_2$) có một liên kết đôi $\text{C}=\text{C}$ giữa hai nguyên tử carbon và bốn liên kết đơn $\text{C}-\text{H}$.",
            ),
            mcq(
                question=r"Thành phần hydrocarbon chiếm tỉ lệ thể tích lớn nhất trong khí thiên nhiên và khí mỏ dầu là:",
                options=[
                    r"Ethylene ($\text{C}_2\text{H}_4$)",
                    r"Methane ($\text{CH}_4$)",
                    r"Butane ($\text{C}_4\text{H}_{10}$)",
                    r"Acetylene ($\text{C}_2\text{H}_2$)",
                ],
                answer="B",
                level="biet",
                solution=r"Methane ($\text{CH}_4$) chiếm khoảng $95\text{\%}$ trong khí thiên nhiên và khoảng $75\text{\%}$ trong khí mỏ dầu.",
            ),
            mcq(
                question=r"Thuốc thử dùng để nhận biết và phân biệt hai chất khí không màu là methane ($\text{CH}_4$) và ethylene ($\text{C}_2\text{H}_4$) là:",
                options=[
                    r"Dung dịch nước vôi trong $\text{Ca(OH)}_2$",
                    r"Dung dịch nước bromine ($\text{Br}_2$)",
                    r"Dung dịch $\text{NaOH}$",
                    r"Quỳ tím ẩm",
                ],
                answer="B",
                level="biet",
                solution=r"Khí $\text{C}_2\text{H}_4$ có liên kết đôi $\text{C}=\text{C}$ nên tham gia phản ứng cộng làm mất màu da cam của dung dịch $\text{Br}_2$, còn $\text{CH}_4$ không phản ứng.",
            ),
            mcq(
                question=r"Để loại bỏ tạp chất khí ethylene ($\text{C}_2\text{H}_4$) có lẫn trong khí methane ($\text{CH}_4$) nhằm thu được khí $\text{CH}_4$ tinh khiết, người ta dẫn hỗn hợp khí đi qua lượng dư dung dịch nào sau đây?",
                options=[
                    r"Dung dịch $\text{NaCl}$ bão hòa",
                    r"Dung dịch nước bromine ($\text{Br}_2$)",
                    r"Dung dịch $\text{HCl}$",
                    r"Dung dịch $\text{Ca(OH)}_2$",
                ],
                answer="B",
                level="hieu",
                solution=r"Khi dẫn hỗn hợp qua dung dịch $\text{Br}_2$ dư, $\text{C}_2\text{H}_4$ tác dụng tạo $\text{C}_2\text{H}_4\text{Br}_2$ lỏng giữ lại trong bình, còn $\text{CH}_4$ không phản ứng thoát ra tinh khiết.",
            ),
            mcq(
                question=r"Khi đốt cháy hoàn toàn $1\text{ mol}$ hydrocarbon $\text{X}$ mạch hở thu được $2\text{ mol}$ khí $\text{CO}_2$ và $3\text{ mol}$ $\text{H}_2\text{O}$. Công thức phân tử và tên gọi IUPAC của $\text{X}$ là:",
                options=[
                    r"$\text{C}_2\text{H}_4$ (ethylene)",
                    r"$\text{C}_2\text{H}_6$ (ethane)",
                    r"$\text{C}_3\text{H}_6$ (propylene)",
                    r"$\text{C}_3\text{H}_8$ (propane)",
                ],
                answer="B",
                level="hieu",
                solution=r"Bảo toàn nguyên tố $\text{C}$ và $\text{H}$: trong $1\text{ mol}$ $\text{X}$ có $n_{\text{C}} = n_{\text{CO}_2} = 2\text{ mol}$ và $n_{\text{H}} = 2 \cdot n_{\text{H}_2\text{O}} = 6\text{ mol}$. Vậy công thức phân tử của $\text{X}$ là $\text{C}_2\text{H}_6$ (ethane).",
            ),
            tf4(
                stem=r"So sánh cấu tạo, tính chất và ứng dụng của hai hydrocarbon là methane ($\text{CH}_4$) và ethylene ($\text{C}_2\text{H}_4$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$), cả $\text{CH}_4$ và $\text{C}_2\text{H}_4$ đều là các chất khí không màu, ít tan trong nước và nhẹ hơn không khí.",
                    r"b) Cả hai khí $\text{CH}_4$ và $\text{C}_2\text{H}_4$ đều làm mất màu dung dịch nước bromine ($\text{Br}_2$) ở điều kiện thường.",
                    r"c) Trùng hợp khí ethylene ($\text{C}_2\text{H}_4$) ở điều kiện nhiệt độ, áp suất và xúc tác thích hợp thu được nhựa polyethylene ($\text{PE}$).",
                    r"d) Khi đốt cháy hoàn toàn $1\text{ mol}$ $\text{C}_2\text{H}_4$, số mol $\text{H}_2\text{O}$ thu được lớn hơn số mol $\text{CO}_2$ thu được.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $M_{\text{CH}_4} = 16\text{ g/mol} < 29\text{ g/mol}$ và $M_{\text{C}_2\text{H}_4} = 28\text{ g/mol} < 29\text{ g/mol}$, cả hai đều là khí không màu, ít tan trong nước. "
                    r"b) Sai vì chỉ có $\text{C}_2\text{H}_4$ (có liên kết đôi $\text{C}=\text{C}$) làm mất màu dung dịch $\text{Br}_2$, còn $\text{CH}_4$ không phản ứng. "
                    r"c) Đúng vì $n\text{CH}_2=\text{CH}_2 \xrightarrow{t^\circ, p, xt} \left(-\text{CH}_2-\text{CH}_2-\right)_n$ ($\text{PE}$). "
                    r"d) Sai vì đốt cháy alkene $\text{C}_2\text{H}_4$ luôn cho $n_{\text{CO}_2} = n_{\text{H}_2\text{O}} = 2\text{ mol}$."
                ),
            ),
            tf4(
                stem=r"Tìm hiểu về nguồn nhiên liệu dầu mỏ, khí thiên nhiên và cách sử dụng nhiên liệu an toàn, hiệu quả. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Chưng cất phân đoạn dầu mỏ là quá trình vật lý tách dầu mỏ thành các phân đoạn có nhiệt độ sôi khác nhau như xăng, dầu hỏa, dầu diesel.",
                    r"b) Dầu mỏ là một đơn chất tinh khiết có nhiệt độ sôi cố định và nặng hơn nước.",
                    r"c) Phương pháp cracking dầu mỏ giúp bẻ gãy các phân tử hydrocarbon mạch dài (dầu nặng) thành các hydrocarbon mạch ngắn hơn để làm tăng sản lượng xăng và thu thêm alkene.",
                    r"d) Khi xảy ra đám cháy xăng hoặc dầu hỏa, cách dập lửa hiệu quả nhất là phun thật nhiều nước trực tiếp vào đám cháy.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì chưng cất phân đoạn dựa trên sự khác nhau về nhiệt độ sôi của các hydrocarbon trong dầu mỏ. "
                    r"b) Sai vì dầu mỏ là hỗn hợp phức tạp của nhiều hydrocarbon, nhẹ hơn nước và không có nhiệt độ sôi xác định. "
                    r"c) Đúng vì cracking là quá trình hóa học bẻ gãy mạch carbon tăng hiệu quả chế biến xăng và nguyên liệu hóa dầu. "
                    r"d) Sai vì xăng, dầu nhẹ hơn nước và không tan trong nước nên phun nước sẽ làm xăng dầu nổi lên và lan rộng đám cháy; phải dùng bình bột/bọt chữa cháy hoặc cát."
                ),
            ),
            mcq(
                question=r"Đốt cháy hoàn toàn $4{,}958\text{ L}$ khí methane ($\text{CH}_4$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) theo phản ứng $\text{CH}_4 + 2\text{O}_2 \xrightarrow{t^\circ} \text{CO}_2 + 2\text{H}_2\text{O}$. Thể tích không khí ở điều kiện chuẩn (biết khí $\text{O}_2$ chiếm $20\text{\%}$ thể tích không khí) cần dùng vừa đủ cho phản ứng trên là:",
                options=[r"$9{,}916\text{ L}$", r"$24{,}790\text{ L}$", r"$49{,}580\text{ L}$", r"$99{,}160\text{ L}$"],
                answer="C",
                level="vandung",
                solution=r"Theo phương trình, $V_{\text{O}_2} = 2 \cdot V_{\text{CH}_4} = 2 \cdot 4{,}958 = 9{,}916\text{ L}$. Vì $\text{O}_2$ chiếm $20\text{\%}$ thể tích không khí nên thể tích không khí cần dùng là $V_{\text{kk}} = \dfrac{9{,}916}{20\text{\%}} = 9{,}916 \cdot 5 = 49{,}580\text{ L}$.",
            ),
            short(
                question=r"Dẫn $4{,}958\text{ L}$ khí ethylene ($\text{C}_2\text{H}_4$) ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) vào bình đựng dung dịch bromine ($\text{Br}_2$, $M_{\text{Br}} = 80\text{ g/mol}$) dư. Phản ứng xảy ra hoàn toàn theo phương trình $\text{C}_2\text{H}_4 + \text{Br}_2 \longrightarrow \text{C}_2\text{H}_4\text{Br}_2$. Tính khối lượng $\text{Br}_2$ (theo đơn vị $\text{g}$) đã tham gia phản ứng.",
                answer=["32", "32,0", "32.0"],
                level="vandung",
                solution=r"Số mol $\text{C}_2\text{H}_4$ ở đkc là $n_{\text{C}_2\text{H}_4} = \dfrac{4{,}958}{24{,}79} = 0{,}2\text{ mol}$. Theo phương trình hóa học, $n_{\text{Br}_2} = n_{\text{C}_2\text{H}_4} = 0{,}2\text{ mol}$. Khối lượng mol của $\text{Br}_2$ là $M_{\text{Br}_2} = 160\text{ g/mol}$, nên khối lượng $\text{Br}_2$ đã phản ứng là $m = 0{,}2 \cdot 160 = 32\text{ g}$.",
            ),
        ],
        description="Cấu tạo, tính chất của alkane (methane, ethane), alkene (ethylene) và nguồn nhiên liệu dầu mỏ, khí thiên nhiên theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=6,
        code="H9-C06",
        title="Chương 6: Ethylic alcohol và Acetic acid",
        topic="dan-xuat-hydrocarbon-lop-9",
        summary=(
            r"Nắm vững công thức cấu tạo, khái niệm độ cồn, tính chất hóa học và điều chế ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$ có nhóm $-\text{OH}$), "
            r"cùng công thức cấu tạo, tính chất acid đầy đủ, phản ứng ester hóa tạo ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$) và điều chế acetic acid ($\text{CH}_3\text{COOH}$ có nhóm $-\text{COOH}$)."
        ),
        objectives=[
            r"Viết được công thức phân tử ($\text{C}_2\text{H}_6\text{O}$), công thức cấu tạo thu gọn ($\text{CH}_3-\text{CH}_2-\text{OH}$), nêu được khái niệm độ cồn và tính được thể tích $\text{C}_2\text{H}_5\text{OH}$ nguyên chất trong dung dịch rượu.",
            r"Trình bày được tính chất hóa học của ethylic alcohol (phản ứng cháy tỏa nhiệt, phản ứng thế $\text{H}$ của nhóm $-\text{OH}$ với $\text{Na}$) và phương pháp điều chế từ tinh bột hoặc từ ethylene.",
            r"Viết được công thức phân tử ($\text{C}_2\text{H}_4\text{O}_2$), công thức cấu tạo thu gọn ($\text{CH}_3-\text{COOH}$) và trình bày được đầy đủ tính chất acid của acetic acid (tác dụng với quỳ tím, kim loại trước $\text{H}$, base, oxide base, muối carbonate).",
            r"Viết được phương trình hóa học của phản ứng ester hóa giữa $\text{CH}_3\text{COOH}$ và $\text{C}_2\text{H}_5\text{OH}$ (xúc tác $\text{H}_2\text{SO}_4$ đặc, $t^\circ$) và phản ứng lên men giấm.",
        ],
        formulas=[
            {
                "name": "Công thức tính độ cồn của dung dịch ethylic alcohol",
                "formula": r"$\text{Độ cồn } ({}^\circ\text{ hoặc \% vol}) = \dfrac{V_{\text{C}_2\text{H}_5\text{OH}\text{ nguyên chất}}}{V_{\text{dung dịch rượu}}} \cdot 100$",
                "note": r"Khối lượng ethylic alcohol nguyên chất: $m_{\text{C}_2\text{H}_5\text{OH}} = V_{\text{C}_2\text{H}_5\text{OH}} \cdot D \quad (D \approx 0{,}8\text{ g/mL})$",
            },
            {
                "name": r"Phản ứng cháy và phản ứng với $\text{Na}$ của ethylic alcohol",
                "formula": r"$\text{C}_2\text{H}_5\text{OH} + 3\text{O}_2 \xrightarrow{t^\circ} 2\text{CO}_2 + 3\text{H}_2\text{O}; \quad 2\text{C}_2\text{H}_5\text{OH} + 2\text{Na} \longrightarrow 2\text{C}_2\text{H}_5\text{ONa} + \text{H}_2\uparrow$",
                "note": r"Cứ $1\text{ mol }\text{C}_2\text{H}_5\text{OH}$ tác dụng với $\text{Na}$ dư giải phóng $0{,}5\text{ mol }\text{H}_2$",
            },
            {
                "name": "Phản ứng ester hóa giữa acetic acid và ethylic alcohol",
                "formula": r"$\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \xrightleftharpoons[\text{H}_2\text{SO}_4\text{ đặc}]{t^\circ} \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$",
                "note": r"Sản phẩm ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$, $M = 88\text{ g/mol}$) là chất lỏng không màu, mùi thơm, ít tan và nhẹ hơn nước",
            },
            {
                "name": "Điều chế ethylic alcohol và lên men giấm tạo acetic acid",
                "formula": r"$\text{CH}_2=\text{CH}_2 + \text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} \text{C}_2\text{H}_5\text{OH}; \quad \text{C}_2\text{H}_5\text{OH} + \text{O}_2 \xrightarrow{\text{men giấm}} \text{CH}_3\text{COOH} + \text{H}_2\text{O}$",
                "note": r"Lên men glucose điều chế cồn: $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2\uparrow$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Ethylic alcohol — Cấu tạo, độ cồn và tính chất",
                "content": (
                    r"Ethylic alcohol (ethanol) có công thức phân tử $\text{C}_2\text{H}_6\text{O}$ và công thức cấu tạo thu gọn $\text{CH}_3-\text{CH}_2-\text{OH}$ (hay $\text{C}_2\text{H}_5\text{OH}$), "
                    r"trong đó nhóm hydroxy ($-\text{OH}$) quyết định tính chất hóa học đặc trưng. Ở điều kiện thường, $\text{C}_2\text{H}_5\text{OH}$ là chất lỏng không màu, "
                    r"sôi ở $78{,}3^\circ\text{C}$, nhẹ hơn nước ($D \approx 0{,}8\text{ g/mL}$), tan vô hạn trong nước và hòa tan được nhiều chất như iodine, benzen. "
                    r"Độ cồn là số mi-li-lít ($\text{mL}$) ethylic alcohol nguyên chất có trong $100\text{ mL}$ dung dịch ở $20^\circ\text{C}$. "
                    r"Về hóa học: $\text{C}_2\text{H}_5\text{OH}$ cháy với ngọn lửa xanh mờ tỏa nhiều nhiệt; tác dụng với kim loại mạnh ($\text{Na}, \text{K}$) giải phóng khí $\text{H}_2$ "
                    r"(nhưng không tác dụng với dung dịch $\text{NaOH}$). Ethylic alcohol được điều chế bằng cách lên men tinh bột/đường hoặc cộng nước vào ethylene."
                ),
            },
            {
                "title": "2. Acetic acid — Cấu tạo, tính chất acid và phản ứng ester hóa",
                "content": (
                    r"Acetic acid (ethanoic acid) có công thức phân tử $\text{C}_2\text{H}_4\text{O}_2$ và công thức cấu tạo thu gọn $\text{CH}_3-\text{COOH}$, "
                    r"trong đó nhóm carboxyl ($-\text{COOH}$) gây nên tính acid. Ở điều kiện thường, $\text{CH}_3\text{COOH}$ là chất lỏng không màu, vị chua, "
                    r"tan vô hạn trong nước; dung dịch $\text{CH}_3\text{COOH}$ nồng độ $2\text{\%} - 5\text{\%}$ được dùng làm giấm ăn. "
                    r"Acetic acid là một acid hữu cơ yếu nhưng có đầy đủ tính chất của một acid: làm quỳ tím hóa đỏ, tác dụng với kim loại đứng trước $\text{H}$ "
                    r"($2\text{CH}_3\text{COOH} + \text{Zn} \longrightarrow (\text{CH}_3\text{COO})_2\text{Zn} + \text{H}_2\uparrow$), tác dụng với oxide base, base và muối carbonate "
                    r"($2\text{CH}_3\text{COOH} + \text{CaCO}_3 \longrightarrow (\text{CH}_3\text{COO})_2\text{Ca} + \text{CO}_2\uparrow + \text{H}_2\text{O}$). "
                    r"Khi đun nóng với $\text{C}_2\text{H}_5\text{OH}$ có $\text{H}_2\text{SO}_4$ đặc làm xúc tác, xảy ra phản ứng ester hóa thuận nghịch tạo thành ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$)."
                ),
            },
            {
                "title": "3. Ứng dụng và tác hại của việc lạm dụng rượu, bia",
                "content": (
                    r"Ethylic alcohol được dùng làm nhiên liệu sinh học (xăng sinh học $\text{E5}$ chứa $5\text{\%}$ thể tích cồn), dung môi pha sơn, dược phẩm, "
                    r"cồn sát khuẩn y tế ($70^\circ$) và sản xuất acetic acid. Tuy nhiên, lạm dụng rượu bia gây tổn hại nghiêm trọng đến hệ thần kinh, gan, dạ dày "
                    r"và là nguyên nhân hàng đầu gây tai nạn giao thông. Acetic acid được dùng sản xuất giấm ăn, tơ nhân tạo, chất dẻo, dược phẩm và phẩm nhuộm."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Trên nhãn một chai cồn y tế ghi $70^\circ$. Hãy tính thể tích và khối lượng ethylic alcohol nguyên chất "
                    r"(biết $D_{\text{C}_2\text{H}_5\text{OH}} = 0{,}8\text{ g/mL}$) có trong $500\text{ mL}$ cồn y tế $70^\circ$ đó."
                ),
                "solution": (
                    r"Thể tích $\text{C}_2\text{H}_5\text{OH}$ nguyên chất trong $500\text{ mL}$ cồn $70^\circ$ là: "
                    r"$V_{\text{C}_2\text{H}_5\text{OH}} = \dfrac{500 \cdot 70}{100} = 350\text{ mL}$. "
                    r"Khối lượng $\text{C}_2\text{H}_5\text{OH}$ nguyên chất là $m = V \cdot D = 350 \cdot 0{,}8 = 280\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Đun nóng $12\text{ g}$ acetic acid ($\text{CH}_3\text{COOH}$, $M = 60\text{ g/mol}$) với lượng dư ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$) "
                    r"có mặt $\text{H}_2\text{SO}_4$ đặc làm xúc tác. Tính khối lượng ester ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$, $M = 88\text{ g/mol}$) "
                    r"thu được biết hiệu suất phản ứng ester hóa đạt $60\text{\%}$."
                ),
                "solution": (
                    r"Số mol $\text{CH}_3\text{COOH}$ ban đầu là $n_{\text{CH}_3\text{COOH}} = \dfrac{12}{60} = 0{,}2\text{ mol}$. "
                    r"Theo phương trình $\text{CH}_3\text{COOH} + \text{C}_2\text{H}_5\text{OH} \xrightleftharpoons[\text{H}_2\text{SO}_4\text{ đặc}]{t^\circ} \text{CH}_3\text{COOC}_2\text{H}_5 + \text{H}_2\text{O}$, "
                    r"số mol ester thu được theo lý thuyết là $0{,}2\text{ mol}$. Với hiệu suất $H = 60\text{\%}$, khối lượng ethyl acetate thực tế thu được là "
                    r"$m_{\text{ester}} = 0{,}2 \cdot 60\text{\%} \cdot 88 = 10{,}56\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$) có nhóm $-\text{OH}$ tác dụng với $\text{Na}$ giải phóng $\text{H}_2$, nhưng không làm đổi màu quỳ tím và không tác dụng với $\text{NaOH}$ hay $\text{CaCO}_3$.",
            r"Acetic acid ($\text{CH}_3\text{COOH}$) có nhóm $-\text{COOH}$ làm quỳ tím hóa đỏ, tác dụng được với cả $\text{Na}$, $\text{NaOH}$, $\text{CuO}$ và $\text{CaCO}_3$.",
            r"Phản ứng ester hóa giữa $\text{CH}_3\text{COOH}$ và $\text{C}_2\text{H}_5\text{OH}$ là phản ứng thuận nghịch, cần xúc tác $\text{H}_2\text{SO}_4$ đặc và đun nóng để tạo ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$).",
        ],
        questions=[
            mcq(
                question=r"Nhóm nguyên tử gây nên tính chất hóa học đặc trưng của ethylic alcohol ($\text{CH}_3-\text{CH}_2-\text{OH}$) là:",
                options=[
                    r"Nhóm $-\text{CH}_3$",
                    r"Nhóm $-\text{OH}$ (hydroxy)",
                    r"Nhóm $-\text{COOH}$ (carboxyl)",
                    r"Nhóm $-\text{CH}_2-$",
                ],
                answer="B",
                level="biet",
                solution=r"Nhóm $-\text{OH}$ (hydroxy) trong phân tử $\text{C}_2\text{H}_5\text{OH}$ là nhóm chức quyết định các tính chất hóa học đặc trưng của ethylic alcohol.",
            ),
            mcq(
                question=r"Dung dịch acetic acid ($\text{CH}_3\text{COOH}$) có nồng độ từ $2\text{\%}$ đến $5\text{\%}$ có vị chua, thường được dùng trong chế biến thực phẩm với tên gọi là:",
                options=[r"Nước vôi trong", r"Giấm ăn", r"Cồn y tế", r"Nước Javel"],
                answer="B",
                level="biet",
                solution=r"Giấm ăn là dung dịch acetic acid ($\text{CH}_3\text{COOH}$) có nồng độ khoảng $2\text{\%} - 5\text{\%}$.",
            ),
            mcq(
                question=r"Trong $200\text{ mL}$ rượu $40^\circ$ có chứa bao nhiêu mi-li-lít ($\text{mL}$) ethylic alcohol nguyên chất?",
                options=[r"$40\text{ mL}$", r"$60\text{ mL}$", r"$80\text{ mL}$", r"$160\text{ mL}$"],
                answer="C",
                level="biet",
                solution=r"Áp dụng công thức độ cồn: $V_{\text{C}_2\text{H}_5\text{OH}} = \dfrac{200 \cdot 40}{100} = 80\text{ mL}$.",
            ),
            mcq(
                question=r"Sản phẩm hữu cơ có mùi thơm dễ chịu thu được khi đun nóng hỗn hợp gồm acetic acid ($\text{CH}_3\text{COOH}$) và ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$) có mặt $\text{H}_2\text{SO}_4$ đặc là:",
                options=[
                    r"Sodium acetate ($\text{CH}_3\text{COONa}$)",
                    r"Sodium ethoxide ($\text{C}_2\text{H}_5\text{ONa}$)",
                    r"Ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$)",
                    r"Diethyl ether ($\text{C}_2\text{H}_5\text{OC}_2\text{H}_5$)",
                ],
                answer="C",
                level="biet",
                solution=r"Phản ứng ester hóa tạo ra ester ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$) và nước.",
            ),
            mcq(
                question=r"Để làm sạch cặn trắng (thành phần chính là $\text{CaCO}_3$) bám ở đáy ấm đun nước lâu ngày, người ta có thể dùng dung dịch nào sau đây có sẵn trong gian bếp?",
                options=[
                    r"Rượu trắng ($\text{C}_2\text{H}_5\text{OH}$)",
                    r"Giấm ăn ($\text{CH}_3\text{COOH}$)",
                    r"Nước muối ăn ($\text{NaCl}$)",
                    r"Dầu ăn",
                ],
                answer="B",
                level="hieu",
                solution=r"Giấm ăn chứa $\text{CH}_3\text{COOH}$ tác dụng được với $\text{CaCO}_3$ tạo muối tan $(\text{CH}_3\text{COO})_2\text{Ca}$, khí $\text{CO}_2$ và nước: $2\text{CH}_3\text{COOH} + \text{CaCO}_3 \longrightarrow (\text{CH}_3\text{COO})_2\text{Ca} + \text{CO}_2\uparrow + \text{H}_2\text{O}$.",
            ),
            mcq(
                question=r"Chất nào sau đây vừa tác dụng được với ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$), vừa tác dụng được với acetic acid ($\text{CH}_3\text{COOH}$)?",
                options=[
                    r"Kim loại sodium ($\text{Na}$)",
                    r"Dung dịch $\text{NaOH}$",
                    r"Đá vôi ($\text{CaCO}_3$)",
                    r"Bột copper(II) oxide ($\text{CuO}$)",
                ],
                answer="A",
                level="hieu",
                solution=r"Kim loại $\text{Na}$ tác dụng được với cả nhóm $-\text{OH}$ của $\text{C}_2\text{H}_5\text{OH}$ và nhóm $-\text{COOH}$ của $\text{CH}_3\text{COOH}$ để giải phóng khí $\text{H}_2$; còn $\text{NaOH}, \text{CaCO}_3, \text{CuO}$ chỉ tác dụng với $\text{CH}_3\text{COOH}$.",
            ),
            tf4(
                stem=r"Có hai lọ mất nhãn đựng riêng biệt hai chất lỏng không màu là ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$) và dung dịch acetic acid ($\text{CH}_3\text{COOH}$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Có thể dùng giấy quỳ tím để phân biệt hai lọ chất lỏng trên vì $\text{CH}_3\text{COOH}$ làm quỳ tím hóa đỏ còn $\text{C}_2\text{H}_5\text{OH}$ không làm đổi màu quỳ tím.",
                    r"b) Khi cho mẩu kim loại $\text{Na}$ vào từng chất lỏng, chỉ có ống nghiệm chứa $\text{CH}_3\text{COOH}$ mới sủi bọt khí $\text{H}_2$.",
                    r"c) Có thể dùng bột đá vôi ($\text{CaCO}_3$) để nhận biết vì $\text{CH}_3\text{COOH}$ hòa tan $\text{CaCO}_3$ tạo bọt khí $\text{CO}_2$, còn $\text{C}_2\text{H}_5\text{OH}$ không phản ứng.",
                    r"d) Trong công nghiệp thực phẩm, giấm ăn được điều chế bằng cách cho $\text{C}_2\text{H}_5\text{OH}$ loãng tác dụng với kim loại $\text{Cu}$.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{CH}_3\text{COOH}$ có tính acid làm quỳ tím hóa đỏ, còn $\text{C}_2\text{H}_5\text{OH}$ trung tính. "
                    r"b) Sai vì cả $\text{C}_2\text{H}_5\text{OH}$ và $\text{CH}_3\text{COOH}$ đều tác dụng với $\text{Na}$ giải phóng khí $\text{H}_2$. "
                    r"c) Đúng vì chỉ có $\text{CH}_3\text{COOH}$ phản ứng với $\text{CaCO}_3$ giải phóng khí $\text{CO}_2\uparrow$. "
                    r"d) Sai vì giấm ăn được điều chế bằng cách lên men dung dịch $\text{C}_2\text{H}_5\text{OH}$ loãng nhờ men giấm với $\text{O}_2$ không khí: $\text{C}_2\text{H}_5\text{OH} + \text{O}_2 \xrightarrow{\text{men giấm}} \text{CH}_3\text{COOH} + \text{H}_2\text{O}$."
                ),
            ),
            tf4(
                stem=r"Trong phòng thí nghiệm, học sinh tiến hành đun nóng hỗn hợp gồm ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$), acetic acid ($\text{CH}_3\text{COOH}$) và vài giọt dung dịch $\text{H}_2\text{SO}_4$ đặc để điều chế ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$). Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Dung dịch $\text{H}_2\text{SO}_4$ đặc vừa đóng vai trò là chất xúc tác, vừa có tác dụng hút nước làm tăng hiệu suất tạo thành ester.",
                    r"b) Phản ứng ester hóa trên là phản ứng một chiều và luôn đạt hiệu suất $100\text{\%}$.",
                    r"c) Sản phẩm ethyl acetate ($\text{CH}_3\text{COOC}_2\text{H}_5$) tạo thành là chất lỏng có mùi thơm, rất ít tan trong nước và nổi lên trên mặt nước.",
                    r"d) Có thể thay dung dịch $\text{H}_2\text{SO}_4$ đặc bằng dung dịch $\text{NaOH}$ đặc để làm xúc tác cho phản ứng tổng hợp ester này.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì $\text{H}_2\text{SO}_4$ đặc xúc tác cho phản ứng và hút nước giúp cân bằng chuyển dịch theo chiều tạo ester. "
                    r"b) Sai vì phản ứng ester hóa là phản ứng thuận nghịch ($\xrightleftharpoons{}$), hiệu suất luôn nhỏ hơn $100\text{\%}$. "
                    r"c) Đúng vì ethyl acetate có mùi thơm, nhẹ hơn nước và ít tan trong nước nên tách thành lớp nổi lên trên. "
                    r"d) Sai vì $\text{NaOH}$ sẽ trung hòa mất $\text{CH}_3\text{COOH}$ và thủy phân ester, không thể làm xúc tác ester hóa."
                ),
            ),
            mcq(
                question=r"Cho $9{,}2\text{ g}$ ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$, $M = 46\text{ g/mol}$) nguyên chất tác dụng hết với kim loại sodium ($\text{Na}$) dư theo phương trình $2\text{C}_2\text{H}_5\text{OH} + 2\text{Na} \longrightarrow 2\text{C}_2\text{H}_5\text{ONa} + \text{H}_2\uparrow$. Thể tích khí $\text{H}_2$ thu được ở điều kiện chuẩn ($25^\circ\text{C}$, $1\text{ bar}$) là:",
                options=[r"$1{,}2395\text{ L}$", r"$2{,}479\text{ L}$", r"$3{,}7185\text{ L}$", r"$4{,}958\text{ L}$"],
                answer="B",
                level="vandung",
                solution=r"Ta có $n_{\text{C}_2\text{H}_5\text{OH}} = \dfrac{9{,}2}{46} = 0{,}2\text{ mol}$. Theo phương trình hóa học, $n_{\text{H}_2} = \dfrac{1}{2} \cdot n_{\text{C}_2\text{H}_5\text{OH}} = 0{,}1\text{ mol}$. Thể tích khí $\text{H}_2$ ở đkc là $V = 24{,}79 \cdot 0{,}1 = 2{,}479\text{ L}$.",
            ),
            short(
                question=r"Để trung hòa hoàn toàn $150\text{ g}$ dung dịch acetic acid ($\text{CH}_3\text{COOH}$, $M = 60\text{ g/mol}$) cần dùng vừa đủ $100\text{ mL}$ dung dịch $\text{NaOH}$ $1{,}5\text{ M}$ theo phản ứng $\text{CH}_3\text{COOH} + \text{NaOH} \longrightarrow \text{CH}_3\text{COONa} + \text{H}_2\text{O}$. Tính nồng độ phần trăm (theo đơn vị $\text{\%}$) của dung dịch $\text{CH}_3\text{COOH}$ đã dùng.",
                answer=["6", "6%", "6,0", "6.0"],
                level="vandung",
                solution=r"Số mol $\text{NaOH}$ là $n_{\text{NaOH}} = 0{,}1 \cdot 1{,}5 = 0{,}15\text{ mol}$. Theo phương trình, $n_{\text{CH}_3\text{COOH}} = n_{\text{NaOH}} = 0{,}15\text{ mol}$, suy ra khối lượng $\text{CH}_3\text{COOH}$ là $m_{\text{ct}} = 0{,}15 \cdot 60 = 9\text{ g}$. Nồng độ phần trăm của dung dịch là $C\text{\%} = \dfrac{9}{150} \cdot 100\text{\%} = 6\text{\%}$.",
            ),
        ],
        description="Cấu tạo, tính chất hóa học và ứng dụng của ethylic alcohol và acetic acid, độ cồn và phản ứng ester hóa theo chương trình KHTN 9 Kết nối tri thức.",
    ),
    lesson(
        grade=9,
        order=7,
        code="H9-C07",
        title="Chương 7: Lipid, Carbohydrate, Protein và Polymer",
        topic="polime-vat-lieu",
        summary=(
            r"Nắm vững cấu tạo, tính chất thủy phân và xà phòng hóa của chất béo/lipid; tính chất hóa học đặc trưng của các carbohydrate "
            r"(glucose $\text{C}_6\text{H}_{12}\text{O}_6$, saccharose $\text{C}_{12}\text{H}_{22}\text{O}_{11}$, tinh bột và cellulose $(\text{C}_6\text{H}_{10}\text{O}_5)_n$); "
            r"sự đông tụ và thủy phân của protein; cùng khái niệm monomer, mắt xích, hệ số trùng hợp của polymer ($\text{PE}, \text{PP}, \text{PVC}$) và vật liệu composite."
        ),
        objectives=[
            r"Nêu được khái niệm lipid, cấu tạo của chất béo (triester của glycerol $\text{C}_3\text{H}_5(\text{OH})_3$ với acid béo $(\text{RCOO})_3\text{C}_3\text{H}_5$) và viết được phương trình phản ứng xà phòng hóa.",
            r"Trình bày được công thức phân tử, trạng thái tự nhiên và tính chất hóa học đặc trưng của glucose (tráng bạc, lên men rượu), saccharose (thủy phân), tinh bột (hồ tinh bột làm xanh dung dịch $\text{I}_2$, thủy phân) và cellulose.",
            r"Nêu được khái niệm, cấu tạo từ các đơn vị amino acid và tính chất hóa học của protein (thủy phân, đông tụ bởi nhiệt/acid/kiềm, mùi khét khi đốt).",
            r"Nêu được khái niệm polymer, monomer, mắt xích, hệ số trùng hợp $n$, phân loại polymer thiên nhiên - tổng hợp (nhất là nhựa $\text{PE}, \text{PP}, \text{PVC}$, cao su, tơ, vật liệu composite) và biện pháp giảm ô nhiễm rác thải nhựa.",
        ],
        formulas=[
            {
                "name": "Phản ứng xà phòng hóa chất béo trong môi trường kiềm",
                "formula": r"$(\text{RCOO})_3\text{C}_3\text{H}_5 + 3\text{NaOH} \xrightarrow{t^\circ} 3\text{RCOONa}\text{ (xà phòng)} + \text{C}_3\text{H}_5(\text{OH})_3\text{ (glycerol)}$",
                "note": r"Tỉ lệ số mol: $n_{\text{NaOH}} = 3 \cdot n_{\text{chất béo}}$ và $n_{\text{C}_3\text{H}_5(\text{OH})_3} = n_{\text{chất béo}}$",
            },
            {
                "name": r"Phản ứng tráng bạc và phản ứng lên men rượu của glucose ($\text{C}_6\text{H}_{12}\text{O}_6$)",
                "formula": r"$\text{C}_6\text{H}_{12}\text{O}_6 + \text{Ag}_2\text{O} \xrightarrow{\text{dd }\text{NH}_3, t^\circ} \text{C}_6\text{H}_{12}\text{O}_7 + 2\text{Ag}\downarrow; \quad \text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2\uparrow$",
                "note": r"Cứ $1\text{ mol}$ glucose tráng bạc hoàn toàn tạo ra $2\text{ mol }\text{Ag}$ ($M_{\text{Ag}} = 108\text{ g/mol}$)",
            },
            {
                "name": "Phản ứng thủy phân saccharose, tinh bột và cellulose",
                "formula": r"$\text{C}_{12}\text{H}_{22}\text{O}_{11} + \text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} \text{C}_6\text{H}_{12}\text{O}_6\text{ (glucose)} + \text{C}_6\text{H}_{12}\text{O}_6\text{ (fructose)}; \quad (\text{C}_6\text{H}_{10}\text{O}_5)_n + n\text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} n\text{C}_6\text{H}_{12}\text{O}_6$",
                "note": r"Khối lượng mol mắt xích tinh bột/cellulose là $162\text{ g/mol}$; khối lượng mol glucose là $180\text{ g/mol}$",
            },
            {
                "name": "Khối lượng phân tử của polymer và hệ số trùng hợp $n$",
                "formula": r"$M_{\text{polymer}} = n \cdot M_{\text{mắt xích}} \Rightarrow n = \dfrac{M_{\text{polymer}}}{M_{\text{mắt xích}}}$",
                "note": r"Với polyethylene $\left(-\text{CH}_2-\text{CH}_2-\right)_n$, khối lượng một mắt xích là $M_{\text{mắt xích}} = 28\text{ amu}$",
            },
        ],
        theory_sections=[
            {
                "title": "1. Lipid và chất béo",
                "content": (
                    r"Lipid là những hợp chất hữu cơ có trong tế bào sống, không tan trong nước nhưng tan trong các dung môi hữu cơ không phân cực (như xăng, dầu hỏa, benzene), "
                    r"bao gồm chất béo, sáp, steroid, phospholipid... Chất béo là triester của glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$) với các acid béo ($\text{RCOOH}$ là acid đơn chức có mạch carbon dài không phân nhánh), "
                    r"công thức chung là $(\text{RCOO})_3\text{C}_3\text{H}_5$. Ở điều kiện thường, dầu thực vật chứa chủ yếu gốc acid béo không no nên ở thể lỏng, "
                    r"còn mỡ động vật chứa chủ yếu gốc acid béo no nên ở thể rắn. Khi đun nóng chất béo với dung dịch kiềm ($\text{NaOH}, \text{KOH}$), xảy ra phản ứng xà phòng hóa tạo glycerol và muối của acid béo (xà phòng)."
                ),
            },
            {
                "title": "2. Carbohydrate — Glucose, Saccharose, Tinh bột và Cellulose",
                "content": (
                    r"Carbohydrate có công thức chung là $\text{C}_n(\text{H}_2\text{O})_m$: "
                    r"(1) Glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, $M = 180\text{ g/mol}$): chất rắn kết tinh, vị ngọt, có nhiều trong quả nho chín và trong máu người (khoảng $0{,}1\text{\%}$); "
                    r"có phản ứng tráng bạc (tác dụng với $\text{AgNO}_3$ trong dung dịch $\text{NH}_3$ đun nóng tạo lớp bạc $\text{Ag}$ sáng bóng) và phản ứng lên men rượu. "
                    r"(2) Saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$, $M = 342\text{ g/mol}$): đường mía, không có phản ứng tráng bạc, khi thủy phân tạo glucose và fructose. "
                    r"(3) Tinh bột và Cellulose đều có công thức chung $(\text{C}_6\text{H}_{10}\text{O}_5)_n$ nhưng hệ số $n$ của cellulose lớn hơn nhiều. "
                    r"Hồ tinh bột làm dung dịch iodine ($\text{I}_2$) chuyển sang màu xanh tím đặc trưng; cả tinh bột và cellulose khi thủy phân hoàn toàn đều tạo ra glucose."
                ),
            },
            {
                "title": "3. Protein và Polymer",
                "content": (
                    r"Protein là hợp chất hữu cơ có khối lượng phân tử rất lớn, cấu tạo từ hàng trăm đến hàng nghìn đơn vị amino acid liên kết với nhau bằng liên kết peptide. "
                    r"Protein bị đông tụ khi đun nóng hoặc khi thêm acid, base, muối kim loại nặng (như lòng trắng trứng đông lại khi luộc, sữa đậu nành kết tủa khi vắt chanh); "
                    r"protein bị thủy phân nhờ acid/base/enzyme tạo thành các amino acid; khi đốt cháy protein (tóc, sừng, len lông cừu, tơ tằm) có mùi khét đặc trưng. "
                    r"Polymer là những hợp chất có khối lượng phân tử rất lớn do nhiều đơn vị nhỏ gọi là mắt xích liên kết với nhau (số mắt xích $n$ gọi là hệ số trùng hợp; "
                    r"phân tử ban đầu tạo nên polymer gọi là monomer). Vật liệu polymer gồm chất dẻo ($\text{PE}, \text{PP}, \text{PVC}$), tơ, cao su và vật liệu composite (kết hợp vật liệu nền và vật liệu cốt)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1",
                "problem": (
                    r"Thực hiện phản ứng tráng bạc hoàn toàn đối với $18\text{ g}$ glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, $M = 180\text{ g/mol}$) "
                    r"bằng lượng dư dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ đun nóng. Tính khối lượng bạc ($\text{Ag}$, $M = 108\text{ g/mol}$) kết tủa thu được."
                ),
                "solution": (
                    r"Số mol glucose là $n_{\text{C}_6\text{H}_{12}\text{O}_6} = \dfrac{18}{180} = 0{,}1\text{ mol}$. Theo phương trình phản ứng tráng bạc "
                    r"$\text{C}_6\text{H}_{12}\text{O}_6 + \text{Ag}_2\text{O} \xrightarrow{\text{dd }\text{NH}_3, t^\circ} \text{C}_6\text{H}_{12}\text{O}_7 + 2\text{Ag}\downarrow$, "
                    r"ta có $n_{\text{Ag}} = 2 \cdot n_{\text{glucose}} = 0{,}2\text{ mol}$. Khối lượng bạc thu được là $m_{\text{Ag}} = 0{,}2 \cdot 108 = 21{,}6\text{ g}$."
                ),
            },
            {
                "title": "Ví dụ 2",
                "problem": (
                    r"Một phân tử polyethylene ($\text{PE}$) có công thức $\left(-\text{CH}_2-\text{CH}_2-\right)_n$ và có khối lượng phân tử trung bình là $56000\text{ amu}$ "
                    r"(biết $M_{\text{C}} = 12\text{ amu}$, $M_{\text{H}} = 1\text{ amu}$). Hãy tính hệ số trùng hợp $n$ của phân tử $\text{PE}$ đó."
                ),
                "solution": (
                    r"Khối lượng của một mắt xích $-\text{CH}_2-\text{CH}_2-$ là $M_{\text{mắt xích}} = 2 \cdot 12 + 4 \cdot 1 = 28\text{ amu}$. "
                    r"Hệ số trùng hợp của phân tử $\text{PE}$ là $n = \dfrac{56000}{28} = 2000$."
                ),
            },
        ],
        key_takeaways=[
            r"Chất béo $(\text{RCOO})_3\text{C}_3\text{H}_5$ thủy phân trong dung dịch kiềm ($\text{NaOH}, \text{KOH}$) tạo xà phòng và glycerol (phản ứng xà phòng hóa).",
            r"Glucose có phản ứng tráng bạc tạo $2\text{Ag}$; hồ tinh bột gặp dung dịch $\text{I}_2$ hóa xanh tím; protein bị đông tụ bởi nhiệt/acid và cháy có mùi khét.",
            r"Polymer gồm các polymer thiên nhiên (tinh bột, cellulose, tơ tằm, cao su thiên nhiên) và polymer tổng hợp ($\text{PE}, \text{PP}, \text{PVC}$, tơ nylon); cần áp dụng nguyên tắc 3R (Reduce - Reuse - Recycle) để giảm rác thải nhựa.",
        ],
        questions=[
            mcq(
                question=r"Khi đun nóng chất béo với dung dịch kiềm $\text{NaOH}$ (phản ứng xà phòng hóa), sản phẩm thu được gồm muối sodium của acid béo (xà phòng) và hợp chất nào sau đây?",
                options=[
                    r"Ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$)",
                    r"Glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$)",
                    r"Acetic acid ($\text{CH}_3\text{COOH}$)",
                    r"Glucose ($\text{C}_6\text{H}_{12}\text{O}_6$)",
                ],
                answer="B",
                level="biet",
                solution=r"Chất béo là triester của glycerol và acid béo, khi xà phòng hóa tạo ra muối của acid béo và glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$).",
            ),
            mcq(
                question=r"Nhỏ vài giọt dung dịch iodine ($\text{I}_2$) vào ống nghiệm đựng dung dịch hồ tinh bột để nguội (hoặc mặt cắt củ khoai lang), hiện tượng quan sát được là:",
                options=[
                    r"Xuất hiện màu xanh tím đặc trưng",
                    r"Xuất hiện kết tủa bạc sáng bóng",
                    r"Sủi bọt khí không màu",
                    r"Dung dịch chuyển sang màu hồng",
                ],
                answer="A",
                level="biet",
                solution=r"Hồ tinh bột hấp phụ các phân tử $\text{I}_2$ vào cấu trúc xoắn tạo hợp chất có màu xanh tím đặc trưng.",
            ),
            mcq(
                question=r"Khi thủy phân hoàn toàn protein trong môi trường acid hoặc base (hoặc nhờ xúc tác enzyme), sản phẩm cuối cùng thu được là:",
                options=[
                    r"Các phân tử glucose",
                    r"Các phân tử amino acid",
                    r"Glycerol và các acid béo",
                    r"Ethylic alcohol và khí $\text{CO}_2$",
                ],
                answer="B",
                level="biet",
                solution=r"Protein được cấu tạo từ các đơn vị amino acid nên khi thủy phân hoàn toàn sẽ thu được hỗn hợp các amino acid.",
            ),
            mcq(
                question=r"Polymer nào sau đây thuộc loại polymer tổng hợp?",
                options=[
                    r"Tinh bột",
                    r"Cellulose (sợi bông)",
                    r"Polyethylene ($\text{PE}$)",
                    r"Tơ tằm",
                ],
                answer="C",
                level="biet",
                solution=r"Polyethylene ($\text{PE}$) được tổng hợp nhân tạo bằng phản ứng trùng hợp ethylene, còn tinh bột, cellulose và tơ tằm là các polymer thiên nhiên.",
            ),
            mcq(
                question=r"Để phân biệt hai dung dịch không màu là dung dịch glucose ($\text{C}_6\text{H}_{12}\text{O}_6$) và dung dịch saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), người ta đun nhẹ từng mẫu thử với thuốc thử nào sau đây?",
                options=[
                    r"Dung dịch $\text{NaCl}$",
                    r"Dung dịch $\text{AgNO}_3$ trong $\text{NH}_3$ (phản ứng tráng bạc)",
                    r"Dung dịch $\text{HCl}$ loãng ở nhiệt độ thường",
                    r"Giấy quỳ tím",
                ],
                answer="B",
                level="hieu",
                solution=r"Chỉ có dung dịch glucose tham gia phản ứng tráng bạc với $\text{AgNO}_3/\text{NH}_3$ tạo lớp $\text{Ag}$ sáng bóng, còn saccharose không có phản ứng tráng bạc.",
            ),
            mcq(
                question=r"Để phân biệt một sợi vải dệt bằng tơ tằm tự nhiên (bản chất là protein) và một sợi vải dệt bằng sợi bông (bản chất là cellulose), cách đơn giản nhất là:",
                options=[
                    r"Nhúng vào nước lạnh xem sợi nào tan",
                    r"Đốt từng sợi vải: sợi tơ tằm cháy có mùi khét như tóc cháy và vón cục, còn sợi bông cháy nhanh không có mùi khét",
                    r"Nhỏ dung dịch phenolphthalein lên hai sợi vải",
                    r"Nhúng vào dầu ăn",
                ],
                answer="B",
                level="hieu",
                solution=r"Tơ tằm có bản chất là protein nên khi đốt cháy tạo mùi khét đặc trưng như mùi tóc cháy, còn sợi bông là cellulose cháy có mùi giấy cháy.",
            ),
            tf4(
                stem=r"Khảo sát tính chất của các hợp chất carbohydrate gồm glucose ($\text{C}_6\text{H}_{12}\text{O}_6$), saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), tinh bột và cellulose $(\text{C}_6\text{H}_{10}\text{O}_5)_n$. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Glucose và saccharose đều là các chất rắn kết tinh, không màu, có vị ngọt và tan tốt trong nước.",
                    r"b) Tinh bột và cellulose có cùng công thức viết gọn $(\text{C}_6\text{H}_{10}\text{O}_5)_n$ nên chúng là hai chất hoàn toàn giống nhau và có cùng khối lượng phân tử.",
                    r"c) Khi thủy phân hoàn toàn tinh bột hoặc cellulose trong môi trường acid đun nóng đều thu được sản phẩm cuối cùng là glucose.",
                    r"d) Cellulose tan rất tốt trong nước lạnh và làm dung dịch iodine ($\text{I}_2$) chuyển sang màu xanh tím.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì cả glucose (đường nho) và saccharose (đường mía) đều là chất rắn vị ngọt, dễ tan trong nước. "
                    r"b) Sai vì giá trị hệ số $n$ và cấu trúc liên kết mắt xích trong tinh bột và cellulose khác nhau nên chúng không phải cùng một chất. "
                    r"c) Đúng vì $(\text{C}_6\text{H}_{10}\text{O}_5)_n + n\text{H}_2\text{O} \xrightarrow{\text{H}^+, t^\circ} n\text{C}_6\text{H}_{12}\text{O}_6$ (glucose). "
                    r"d) Sai vì cellulose không tan trong nước và không làm xanh dung dịch $\text{I}_2$ (chỉ có hồ tinh bột mới làm xanh $\text{I}_2$)."
                ),
            ),
            tf4(
                stem=r"Xét tính chất, ứng dụng của protein, polymer và các vật liệu mới trong đời sống. Xét tính đúng sai của các phát biểu sau:",
                statements=[
                    r"a) Hiện tượng riêu cua nổi lên khi nấu canh cua hoặc sữa đậu nành đông lại khi thêm giấm chanh là do sự đông tụ protein.",
                    r"b) Monomer dùng để trùng hợp điều chế nhựa poly(vinyl chloride) ($\text{PVC}$) là khí ethylene ($\text{CH}_2=\text{CH}_2$).",
                    r"c) Vật liệu composite là vật liệu tổ hợp gồm hai thành phần chính là vật liệu nền (thường là nhựa polymer) và vật liệu cốt (như sợi thủy tinh, sợi carbon).",
                    r"d) Các loại túi nhựa $\text{PE}, \text{PP}$ rất dễ bị vi sinh vật phân hủy hoàn toàn trong đất chỉ sau vài ngày.",
                ],
                answer="Đ/S/Đ/S",
                level="hieu",
                solution=(
                    r"a) Đúng vì protein tan trong nước bị đông tụ dưới tác dụng của nhiệt độ hoặc môi trường acid. "
                    r"b) Sai vì monomer của $\text{PVC}$ là vinyl chloride ($\text{CH}_2=\text{CHCl}$), còn $\text{CH}_2=\text{CH}_2$ là monomer của $\text{PE}$. "
                    r"c) Đúng vì vật liệu composite kết hợp vật liệu nền và vật liệu cốt để đạt độ bền cơ học và độ nhẹ vượt trội. "
                    r"d) Sai vì nhựa $\text{PE}, \text{PP}$ rất bền vững trong tự nhiên, phải mất hàng trăm năm mới phân hủy nên gây ô nhiễm trắng."
                ),
            ),
            mcq(
                question=r"Lên men $90\text{ g}$ glucose ($\text{C}_6\text{H}_{12}\text{O}_6$, $M = 180\text{ g/mol}$) với hiệu suất quá trình lên men đạt $80\text{\%}$ theo phương trình $\text{C}_6\text{H}_{12}\text{O}_6 \xrightarrow{\text{enzyme}} 2\text{C}_2\text{H}_5\text{OH} + 2\text{CO}_2\uparrow$. Khối lượng ethylic alcohol ($\text{C}_2\text{H}_5\text{OH}$, $M = 46\text{ g/mol}$) thu được là:",
                options=[r"$18{,}4\text{ g}$", r"$23{,}0\text{ g}$", r"$36{,}8\text{ g}$", r"$46{,}0\text{ g}$"],
                answer="C",
                level="vandung",
                solution=r"Số mol glucose là $n_{\text{glucose}} = \dfrac{90}{180} = 0{,}5\text{ mol}$. Theo phương trình, số mol $\text{C}_2\text{H}_5\text{OH}$ lý thuyết là $2 \cdot 0{,}5 = 1{,}0\text{ mol}$. Với hiệu suất $H = 80\text{\%}$, khối lượng $\text{C}_2\text{H}_5\text{OH}$ thu được là $m = 1{,}0 \cdot 80\text{\%} \cdot 46 = 36{,}8\text{ g}$.",
            ),
            short(
                question=r"Đun nóng hoàn toàn $0{,}1\text{ mol}$ một chất béo $(\text{RCOO})_3\text{C}_3\text{H}_5$ với dung dịch $\text{NaOH}$ dư theo phản ứng xà phòng hóa $(\text{RCOO})_3\text{C}_3\text{H}_5 + 3\text{NaOH} \xrightarrow{t^\circ} 3\text{RCOONa} + \text{C}_3\text{H}_5(\text{OH})_3$. Tính khối lượng glycerol ($\text{C}_3\text{H}_5(\text{OH})_3$, $M = 92\text{ g/mol}$, theo đơn vị $\text{g}$) thu được sau phản ứng.",
                answer=["9,2", "9.2"],
                level="vandung",
                solution=r"Theo phương trình phản ứng xà phòng hóa, số mol glycerol bằng số mol chất béo phản ứng: $n_{\text{C}_3\text{H}_5(\text{OH})_3} = 0{,}1\text{ mol}$. Vậy khối lượng glycerol thu được là $m = 0{,}1 \cdot 92 = 9{,}2\text{ g}$.",
            ),
        ],
        description="Cấu tạo và tính chất hóa học của lipid, chất béo, carbohydrate (glucose, saccharose, tinh bột, cellulose), protein và polymer theo chương trình KHTN 9 Kết nối tri thức.",
    ),
]


LESSONS = LESSONS_GRADE_9
