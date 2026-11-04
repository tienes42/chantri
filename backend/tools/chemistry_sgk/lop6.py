from __future__ import annotations
from typing import Any
from ._helpers import lesson, mcq, tf4, short

LESSONS_GRADE_6: list[dict[str, Any]] = [
    lesson(
        grade=6,
        order=1,
        code="H6-C01",
        title="Chương 1: Chất quanh ta và tính chất của chất",
        topic="chat-va-vat-lieu",
        summary=(
            r"Mọi vật thể xung quanh chúng ta (vật thể tự nhiên hay nhân tạo, vật hữu sinh hay vô sinh) đều được tạo nên từ một hoặc nhiều chất. "
            r"Mỗi chất tinh khiết có những tính chất vật lý nhất định (trạng thái, màu sắc, mùi vị, tính tan, tính dẫn điện, nhiệt độ nóng chảy $t_{\text{nc}}$, nhiệt độ sôi $t_{\text{s}}$, khối lượng riêng $D = \dfrac{m}{V}$) "
            r"và tính chất hóa học đặc trưng (khả năng biến đổi thành chất khác như sự cháy trong khí oxygen $\text{O}_2$, sự phân hủy bởi nhiệt của calcium carbonate $\text{CaCO}_3$ hay sự gỉ sét của kim loại iron $\text{Fe}$)."
        ),
        objectives=[
            r"Nêu được sự đa dạng của chất và phân biệt được vật thể tự nhiên, vật thể nhân tạo, vật hữu sinh (vật sống) và vật vô sinh (vật không sống).",
            r"Trình bày được khái niệm chất tạo nên vật thể; lấy được ví dụ về vật thể được tạo nên từ một chất hoặc nhiều chất như water ($\text{H}_2\text{O}$), sodium chloride ($\text{NaCl}$), iron ($\text{Fe}$), aluminium ($\text{Al}$).",
            r"Phân biệt được tính chất vật lý (trạng thái, màu, mùi, vị, tính tan, khối lượng riêng $D$, nhiệt độ nóng chảy $t_{\text{nc}}$, nhiệt độ sôi $t_{\text{s}}$, tính dẫn điện, dẫn nhiệt) và tính chất hóa học của chất.",
            r"Vận dụng được các tính chất của chất (khối lượng riêng $D = \dfrac{m}{V}$, nhiệt độ sôi, tính tan, khả năng phản ứng hóa học) để nhận biết chất và giải thích ứng dụng trong đời sống.",
        ],
        formulas=[
            {
                "name": "Khối lượng riêng của chất",
                "formula": r"$D = \dfrac{m}{V}$",
                "note": r"$D$ là khối lượng riêng ($\text{g/cm}^3$ hoặc $\text{kg/m}^3$), $m$ là khối lượng ($\text{g}$ hoặc $\text{kg}$), $V$ là thể tích ($\text{cm}^3$ hoặc $\text{m}^3$).",
            },
            {
                "name": "Quy đổi đơn vị khối lượng riêng và thể tích",
                "formula": r"$1\text{ g/cm}^3 = 1\text{ g/mL} = 1000\text{ kg/m}^3; \quad 1\text{ L} = 1000\text{ mL} = 1000\text{ cm}^3$",
                "note": r"Ở điều kiện chuẩn, nước tinh khiết ($\text{H}_2\text{O}$) có $D = 1\text{ g/cm}^3$, $t_{\text{nc}} = 0^\circ\text{C}$, $t_{\text{s}} = 100^\circ\text{C}$.",
            },
            {
                "name": "Phản ứng nhiệt phân đá vôi (tính chất hóa học)",
                "formula": r"$\text{CaCO}_3 \xrightarrow{t^\circ} \text{CaO} + \text{CO}_2\uparrow$",
                "note": r"Calcium carbonate ($\text{CaCO}_3$) bị phân hủy ở nhiệt độ cao tạo calcium oxide ($\text{CaO}$) và khí carbon dioxide ($\text{CO}_2$).",
            },
        ],
        theory_sections=[
            {
                "title": "1. Vật thể và chất quanh ta",
                "content": (
                    r"- **Vật thể tự nhiên** là những vật thể có sẵn trong tự nhiên (núi đá vôi, sông suối, cây xanh, con cá, bầu khí quyển). **Vật thể nhân tạo** do con người tạo ra để phục vụ đời sống (chiếc ấm bằng aluminium $\text{Al}$, cốc thủy tinh, bàn gỗ, xe đạp)." "\n"
                    r"- **Vật hữu sinh (vật sống)** có các đặc trưng sống như trao đổi chất, lớn lên và sinh sản (cây lúa, con người, vi khuẩn). **Vật vô sinh (vật không sống)** không có các đặc trưng sống trên (hòn đá, chiếc cầu bằng iron $\text{Fe}$, cốc nước)." "\n"
                    r"- **Chất** cấu tạo nên mọi vật thể: ở đâu có vật thể là ở đó có chất. Một vật thể có thể được tạo nên từ một chất (dây dẫn điện lõi copper $\text{Cu}$, nước cất $\text{H}_2\text{O}$) hoặc từ nhiều chất (quả chanh chứa water $\text{H}_2\text{O}$, citric acid, đường saccharose và vitamin C)."
                ),
            },
            {
                "title": "2. Tính chất vật lý của chất",
                "content": (
                    r"- **Tính chất vật lý** là những tính chất của chất không kèm theo sự biến đổi thành chất khác, có thể quan sát trực tiếp bằng giác quan hoặc đo bằng dụng cụ đo:" "\n"
                    r"  + Thể (rắn, lỏng, khí), màu sắc, mùi, vị (ví dụ: muối ăn sodium chloride $\text{NaCl}$ ở thể rắn, màu trắng, vị mặn; khí oxygen $\text{O}_2$ không màu, không mùi, không vị)." "\n"
                    r"  + Tính tan trong water ($\text{H}_2\text{O}$) hoặc trong chất lỏng khác (ví dụ: đường saccharose và muối $\text{NaCl}$ tan tốt trong nước; bột calcium carbonate $\text{CaCO}_3$ và dầu ăn không tan trong nước)." "\n"
                    r"  + Tính dẻo, tính cứng, tính dẫn điện, tính dẫn nhiệt (ví dụ: kim loại silver $\text{Ag}$, copper $\text{Cu}$, aluminium $\text{Al}$ dẫn điện và dẫn nhiệt tốt)." "\n"
                    r"  + **Nhiệt độ nóng chảy** ($t_{\text{nc}}$), **nhiệt độ sôi** ($t_{\text{s}}$) và **khối lượng riêng** ($D = \dfrac{m}{V}$): Mỗi chất tinh khiết có các hằng số vật lý xác định (ví dụ: ở áp suất $1\text{ atm}$, water $\text{H}_2\text{O}$ tinh khiết có $t_{\text{nc}} = 0^\circ\text{C}$, $t_{\text{s}} = 100^\circ\text{C}$, $D = 1{,}0\text{ g/cm}^3$; iron $\text{Fe}$ có $D = 7{,}87\text{ g/cm}^3$; aluminium $\text{Al}$ có $D = 2{,}70\text{ g/cm}^3$)."
                ),
            },
            {
                "title": "3. Tính chất hóa học của chất",
                "content": (
                    r"- **Tính chất hóa học** là khả năng của một chất biến đổi thành chất mới thông qua các phản ứng hóa học:" "\n"
                    r"  + Khả năng cháy trong khí oxygen ($\text{O}_2$): than đá (chứa carbon $\text{C}$) cháy tạo thành khí carbon dioxide ($\text{CO}_2$) theo sơ đồ $\text{C} + \text{O}_2 \xrightarrow{t^\circ} \text{CO}_2$." "\n"
                    r"  + Khả năng bị phân hủy bởi nhiệt: đường mía ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) đun nóng quá mức bị phân hủy thành than đen ($\text{C}$) và hơi nước ($\text{H}_2\text{O}$); đá vôi ($\text{CaCO}_3$) nung nóng tạo vôi sống ($\text{CaO}$) và khí $\text{CO}_2$." "\n"
                    r"  + Khả năng bị ăn mòn, gỉ sét: đinh iron ($\text{Fe}$) để lâu trong không khí ẩm tác dụng với oxygen ($\text{O}_2$) và nước ($\text{H}_2\text{O}$) tạo thành lớp gỉ sắt màu nâu đỏ giòn, xốp."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân biệt vật thể và chất",
                "problem": (
                    r"Cho danh sách các từ sau: (1) chiếc nồi, (2) aluminium ($\text{Al}$), (3) cây mía, (4) đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), "
                    r"(5) nước ($\text{H}_2\text{O}$), (6) lọ hoa thủy tinh. Hãy phân loại thành vật thể tự nhiên, vật thể nhân tạo và chất."
                ),
                "solution": (
                    r"- **Vật thể tự nhiên** (và là vật hữu sinh): (3) cây mía." "\n"
                    r"- **Vật thể nhân tạo** (và là vật vô sinh): (1) chiếc nồi, (6) lọ hoa thủy tinh." "\n"
                    r"- **Chất** tạo nên vật thể: (2) aluminium ($\text{Al}$), (4) đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$), (5) nước ($\text{H}_2\text{O}$)."
                ),
            },
            {
                "title": "Ví dụ 2: Nhận biết kim loại qua khối lượng riêng",
                "problem": (
                    r"Một thỏi kim loại tinh khiết hình hộp chữ nhật có thể tích $V = 20\text{ cm}^3$ và cân nặng $m = 54\text{ g}$. "
                    r"Biết khối lượng riêng của aluminium ($\text{Al}$) là $2{,}7\text{ g/cm}^3$, của zinc ($\text{Zn}$) là $7{,}1\text{ g/cm}^3$ và của iron ($\text{Fe}$) là $7{,}87\text{ g/cm}^3$. "
                    r"Xác định tên kim loại tạo nên thỏi trên."
                ),
                "solution": (
                    r"Áp dụng công thức tính khối lượng riêng của chất:" "\n"
                    r"$$D = \dfrac{m}{V} = \dfrac{54}{20} = 2{,}7\text{ g/cm}^3$$" "\n"
                    r"Đối chiếu với bảng khối lượng riêng, ta kết luận thỏi kim loại đó làm bằng **aluminium** ($\text{Al}$)."
                ),
            },
        ],
        key_takeaways=[
            r"Vật thể được chia thành vật thể tự nhiên và vật thể nhân tạo (hoặc vật hữu sinh và vật vô sinh); mọi vật thể đều do một hay nhiều chất cấu tạo nên.",
            r"Tính chất vật lý không làm xuất hiện chất mới (thể, màu, mùi, vị, tính tan, tính dẫn điện, $t_{\text{nc}}$, $t_{\text{s}}$, $D = \dfrac{m}{V}$).",
            r"Tính chất hóa học là khả năng chất biến đổi thành chất mới (tính cháy, tính bị nhiệt phân hủy, tính tác dụng với acid hay oxygen $\text{O}_2$).",
        ],
        questions=[
            mcq(
                r"Trong các từ chỉ đối tượng dưới đây, từ nào chỉ một **chất** hóa học (không phải tên vật thể)?",
                [
                    r"Sodium chloride ($\text{NaCl}$).",
                    r"Chiếc bàn học bằng gỗ.",
                    r"Quả bóng đá bằng cao su.",
                    r"Cây cầu bắc qua sông.",
                ],
                "A",
                "biet",
                r"Sodium chloride ($\text{NaCl}$ - muối ăn) là tên của một chất hóa học. Chiếc bàn học, quả bóng đá và cây cầu là các vật thể nhân tạo.",
            ),
            mcq(
                r"Dãy nào sau đây chỉ gồm các **vật hữu sinh** (vật sống)?",
                [
                    r"Chiếc cốc thủy tinh, dây đồng ($\text{Cu}$), muối ăn ($\text{NaCl}$).",
                    r"Cây lúa, con cá chép, vi khuẩn đường ruột.",
                    r"Con mèo, chiếc xe đạp, hòn đá cuội.",
                    r"Cây bàng, đám mây, dòng nước suối.",
                ],
                "B",
                "biet",
                r"Vật hữu sinh (vật sống) có khả năng trao đổi chất, lớn lên và sinh sản, bao gồm cây lúa, con cá chép và vi khuẩn đường ruột.",
            ),
            mcq(
                r"Ở áp suất tiêu chuẩn $1\text{ atm}$, nước tinh khiết ($\text{H}_2\text{O}$) có nhiệt độ nóng chảy và nhiệt độ sôi lần lượt là:",
                [
                    r"$10^\circ\text{C}$ và $100^\circ\text{C}$.",
                    r"$-10^\circ\text{C}$ và $90^\circ\text{C}$.",
                    r"$0^\circ\text{C}$ và $100^\circ\text{C}$.",
                    r"$0^\circ\text{C}$ và $78{,}3^\circ\text{C}$.",
                ],
                "C",
                "biet",
                r"Ở áp suất chuẩn $1\text{ atm}$, nước tinh khiết ($\text{H}_2\text{O}$) nóng chảy ở $0^\circ\text{C}$ và sôi ở $100^\circ\text{C}$.",
            ),
            mcq(
                r"Tính chất nào sau đây của kim loại iron ($\text{Fe}$) là **tính chất hóa học**?",
                [
                    r"Có màu trắng hơi xám, dẻo và có ánh kim.",
                    r"Dẫn điện, dẫn nhiệt tốt và bị nam châm hút mạnh.",
                    r"Có khối lượng riêng $D = 7{,}87\text{ g/cm}^3$ và nóng chảy ở $1538^\circ\text{C}$.",
                    r"Bị gỉ thành lớp chất rắn màu nâu đỏ khi để lâu trong không khí ẩm.",
                ],
                "D",
                "biet",
                r"Iron ($\text{Fe}$) bị gỉ trong không khí ẩm là quá trình $\text{Fe}$ tác dụng với oxygen ($\text{O}_2$) và nước ($\text{H}_2\text{O}$) tạo thành chất mới (iron(III) oxide ngậm nước), nên đây là tính chất hóa học. Các tính chất còn lại đều là tính chất vật lý.",
            ),
            mcq(
                r"Vì sao người ta thường dùng kim loại copper ($\text{Cu}$) hoặc aluminium ($\text{Al}$) để làm lõi dây dẫn điện mà dùng nhựa PVC để làm vỏ bọc bên ngoài?",
                [
                    r"Vì $\text{Cu}$ và $\text{Al}$ dẫn điện tốt, còn nhựa PVC cách điện giúp đảm bảo an toàn.",
                    r"Vì $\text{Cu}$ và $\text{Al}$ có tính chất hóa học dễ cháy, còn nhựa PVC dẫn điện tốt.",
                    r"Vì nhựa PVC có khối lượng riêng lớn hơn $\text{Cu}$ và $\text{Al}$.",
                    r"Vì $\text{Cu}$ và $\text{Al}$ không có nhiệt độ nóng chảy xác định.",
                ],
                "A",
                "hieu",
                r"Dựa vào tính chất vật lý của chất: kim loại copper ($\text{Cu}$) và aluminium ($\text{Al}$) dẫn điện rất tốt nên dùng làm lõi truyền tải điện, còn nhựa PVC không dẫn điện (cách điện) nên dùng làm lớp vỏ bọc bảo vệ an toàn.",
            ),
            mcq(
                r"Cho ba chất lỏng không màu đựng trong ba lọ mất nhãn gồm: nước cất ($\text{H}_2\text{O}$), cồn ethanol ($\text{C}_2\text{H}_5\text{OH}$) và dầu ăn. Chỉ dựa vào tính chất vật lý, cách đơn giản và an toàn nhất để phân biệt cả ba chất là:",
                [
                    r"Dùng nam châm đưa lại gần miệng từng lọ chất lỏng.",
                    r"Dựa vào mùi đặc trưng để nhận ra ethanol, sau đó hòa tan một ít muối ăn ($\text{NaCl}$) hoặc trộn với nước để phân biệt nước cất và dầu ăn.",
                    r"Đem nếm trực tiếp cả ba chất lỏng trong phòng thí nghiệm.",
                    r"Quan sát màu sắc bằng mắt thường dưới ánh sáng mặt trời.",
                ],
                "B",
                "hieu",
                r"Trong phòng thí nghiệm tuyệt đối không được nếm hóa chất. Ethanol ($\text{C}_2\text{H}_5\text{OH}$) có mùi thơm cồn đặc trưng; nước cất ($\text{H}_2\text{O}$) không mùi và hòa tan tốt muối ăn ($\text{NaCl}$); dầu ăn không tan trong nước và nhẹ hơn nước ($D \approx 0{,}8\text{ g/cm}^3$) nên nổi lên trên mặt nước.",
            ),
            tf4(
                r"Trong giờ thực hành tìm hiểu về vật thể và tính chất của các chất quanh ta, một nhóm học sinh thảo luận về muối ăn (sodium chloride, $\text{NaCl}$), đá vôi (thành phần chính là calcium carbonate, $\text{CaCO}_3$) và dây kim loại copper ($\text{Cu}$). Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Dây điện có lõi bằng copper ($\text{Cu}$) và vỏ bằng nhựa là một vật thể nhân tạo được cấu tạo từ nhiều chất.",
                    r"Sodium chloride ($\text{NaCl}$) ở thể rắn, màu trắng và tan tốt trong nước ($\text{H}_2\text{O}$) là những tính chất hóa học của muối ăn.",
                    r"Khi nhỏ dung dịch hydrochloric acid ($\text{HCl}$) vào mẫu đá vôi ($\text{CaCO}_3$) thấy sủi bọt khí carbon dioxide ($\text{CO}_2$), điều này thể hiện tính chất hóa học của $\text{CaCO}_3$.",
                    r"Mọi chất tinh khiết ở cùng điều kiện nhiệt độ và áp suất đều có khối lượng riêng $D$, nhiệt độ nóng chảy $t_{\text{nc}}$ và nhiệt độ sôi $t_{\text{s}}$ hoàn toàn giống nhau.",
                ],
                "Đ/S/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Dây điện do con người chế tạo nên là vật thể nhân tạo, gồm ít nhất hai chất là kim loại copper ($\text{Cu}$) và nhựa cách điện." "\n"
                    r"- **Ý b) Sai**: Trạng thái rắn, màu trắng và tính tan trong nước ($\text{H}_2\text{O}$) không làm biến đổi $\text{NaCl}$ thành chất mới nên đều là **tính chất vật lý**." "\n"
                    r"- **Ý c) Đúng**: $\text{CaCO}_3$ tác dụng với $\text{HCl}$ tạo ra chất mới là $\text{CaCl}_2$, $\text{H}_2\text{O}$ và khí $\text{CO}_2\uparrow$, thể hiện tính chất hóa học của $\text{CaCO}_3$." "\n"
                    r"- **Ý d) Sai**: Mỗi chất tinh khiết khác nhau có khối lượng riêng $D$, nhiệt độ nóng chảy $t_{\text{nc}}$ và nhiệt độ sôi $t_{\text{s}}$ đặc trưng riêng biệt (ví dụ ở $1\text{ atm}$, nước sôi ở $100^\circ\text{C}$ còn ethanol sôi ở $78{,}3^\circ\text{C}$)."
                ),
            ),
            tf4(
                r"Cho bảng số liệu về một số tính chất của ba chất tinh khiết ở áp suất $1\text{ atm}$: Nước ($\text{H}_2\text{O}$: $t_{\text{nc}} = 0^\circ\text{C}$, $t_{\text{s}} = 100^\circ\text{C}$, $D = 1{,}00\text{ g/cm}^3$); Ethanol ($\text{C}_2\text{H}_5\text{OH}$: $t_{\text{nc}} = -114^\circ\text{C}$, $t_{\text{s}} = 78{,}3^\circ\text{C}$, $D = 0{,}79\text{ g/cm}^3$); Kim loại Iron ($\text{Fe}$: $t_{\text{nc}} = 1538^\circ\text{C}$, $t_{\text{s}} = 2862^\circ\text{C}$, $D = 7{,}87\text{ g/cm}^3$). Xét tính đúng/sai của các nhận định sau:",
                [
                    r"Ở nhiệt độ phòng $25^\circ\text{C}$, cả nước ($\text{H}_2\text{O}$) và ethanol ($\text{C}_2\text{H}_5\text{OH}$) đều tồn tại ở thể lỏng, còn iron ($\text{Fe}$) tồn tại ở thể rắn.",
                    r"Nếu lấy cùng một thể tích $V = 100\text{ cm}^3$ thì khối lượng của ethanol ($\text{C}_2\text{H}_5\text{OH}$) lớn hơn khối lượng của nước ($\text{H}_2\text{O}$).",
                    r"Khi đun nóng hỗn hợp gồm nước và ethanol, ethanol sẽ sôi và bay hơi mạnh trước nước vì có nhiệt độ sôi thấp hơn ($78{,}3^\circ\text{C} < 100^\circ\text{C}$).",
                    r"Ở nhiệt độ $-50^\circ\text{C}$, cả nước ($\text{H}_2\text{O}$) và ethanol ($\text{C}_2\text{H}_5\text{OH}$) đều đã đông đặc hoàn toàn thành thể rắn.",
                ],
                "Đ/S/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Vì $25^\circ\text{C}$ nằm trong khoảng giữa $t_{\text{nc}}$ và $t_{\text{s}}$ của nước ($0^\circ\text{C} < 25^\circ\text{C} < 100^\circ\text{C}$) và của ethanol ($-114^\circ\text{C} < 25^\circ\text{C} < 78{,}3^\circ\text{C}$) nên hai chất này ở thể lỏng; còn $25^\circ\text{C} < 1538^\circ\text{C}$ nên iron ($\text{Fe}$) ở thể rắn." "\n"
                    r"- **Ý b) Sai**: Ta có $m = D \cdot V$. Với $V = 100\text{ cm}^3$, $m_{\text{ethanol}} = 0{,}79 \cdot 100 = 79\text{ g}$, nhỏ hơn $m_{\text{H}_2\text{O}} = 1{,}00 \cdot 100 = 100\text{ g}$." "\n"
                    r"- **Ý c) Đúng**: Chất có nhiệt độ sôi thấp hơn ($78{,}3^\circ\text{C} < 100^\circ\text{C}$) sẽ sôi và hóa hơi trước khi đun nóng." "\n"
                    r"- **Ý d) Sai**: Ở $-50^\circ\text{C}$, nước đã đông đặc thành băng rắn (do $-50^\circ\text{C} < 0^\circ\text{C}$), nhưng ethanol vẫn ở thể lỏng vì $-50^\circ\text{C} > -114^\circ\text{C}$."
                ),
            ),
            mcq(
                r"Để kiểm tra một chiếc nhẫn màu vàng có phải làm bằng vàng nguyên chất ($\text{Au}$, có khối lượng riêng $D_{\text{Au}} = 19{,}3\text{ g/cm}^3$) hay bị pha trộn với đồng ($\text{Cu}$, có $D_{\text{Cu}} = 8{,}96\text{ g/cm}^3$), người thợ kim hoàn cân chiếc nhẫn được khối lượng $m = 15{,}44\text{ g}$ và đo thể tích bằng bình chia độ được $V = 0{,}8\text{ cm}^3$. Kết luận nào sau đây đúng?",
                [
                    r"Chiếc nhẫn có khối lượng riêng $D = 8{,}96\text{ g/cm}^3$ nên làm hoàn toàn bằng copper ($\text{Cu}$).",
                    r"Chiếc nhẫn có khối lượng riêng $D = 14{,}64\text{ g/cm}^3$ nên là hợp kim vàng - đồng.",
                    r"Chiếc nhẫn có khối lượng riêng $D = 19{,}3\text{ g/cm}^3$ nên phù hợp với vàng nguyên chất ($\text{Au}$).",
                    r"Chiếc nhẫn có khối lượng riêng $D = 12{,}35\text{ g/cm}^3$ nên đã bị pha nhiều copper ($\text{Cu}$).",
                ],
                "C",
                "vandung",
                r"Khối lượng riêng của chiếc nhẫn là: $D = \dfrac{m}{V} = \dfrac{15{,}44}{0{,}8} = 19{,}3\text{ g/cm}^3$. Giá trị này trùng khớp với khối lượng riêng của vàng nguyên chất ($D_{\text{Au}} = 19{,}3\text{ g/cm}^3$).",
            ),
            short(
                r"Khi thả chìm hoàn toàn một khối kim loại copper ($\text{Cu}$) đặc nguyên chất vào bình chia độ chứa sẵn $50\text{ mL}$ nước ($\text{H}_2\text{O}$), mực nước trong bình dâng lên đến vạch $80\text{ mL}$. Biết khối lượng riêng của copper là $D = 8{,}9\text{ g/cm}^3$ và $1\text{ mL} = 1\text{ cm}^3$. Hãy tính khối lượng của khối kim loại copper đó theo đơn vị gam ($\text{g}$).",
                ["267", "267,0", "267.0"],
                "vandung",
                (
                    r"Thể tích của khối kim loại copper ($\text{Cu}$) bằng phần thể tích nước dâng lên trong bình chia độ:" "\n"
                    r"$$V = 80 - 50 = 30\text{ mL} = 30\text{ cm}^3$$" "\n"
                    r"Khối lượng của khối kim loại copper là:" "\n"
                    r"$$m = D \cdot V = 8{,}9 \cdot 30 = 267\text{ g}$$"
                ),
            ),
        ],
        description="Khái niệm vật thể tự nhiên, vật thể nhân tạo, vật hữu sinh, vật vô sinh, chất tinh khiết, tính chất vật lý và tính chất hóa học của chất.",
    ),
    lesson(
        grade=6,
        order=2,
        code="H6-C02",
        title="Chương 2: Ba thể của chất và sự chuyển thể",
        topic="trang-thai-chat",
        summary=(
            r"Các chất xung quanh ta tồn tại ở ba thể cơ bản: rắn, lỏng, khí (hơi). Theo mô hình hạt, chất được tạo nên từ các hạt vô cùng nhỏ luôn chuyển động; "
            r"khoảng cách và lực liên kết giữa các hạt quyết định hình dạng, thể tích và khả năng chịu nén của mỗi thể. "
            r"Khi thay đổi nhiệt độ hoặc áp suất, chất có thể chuyển từ thể này sang thể khác qua các quá trình: nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ và thăng hoa (như đá khô $\text{CO}_2$ rắn chuyển thẳng thành khí $\text{CO}_2$)."
        ),
        objectives=[
            r"Trình bày được đặc điểm cơ bản về khoảng cách hạt, lực liên kết hạt, chuyển động hạt, hình dạng, thể tích và khả năng chịu nén của ba thể rắn, lỏng, khí theo mô hình hạt.",
            r"Định nghĩa và lấy được ví dụ thực tế về các quá trình chuyển thể: nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ và thăng hoa (ví dụ nước đá khô $\text{CO}_2$).",
            r"Phân biệt được sự bay hơi (xảy ra trên mặt thoáng ở mọi nhiệt độ) và sự sôi (xảy ra cả trên mặt thoáng và trong lòng chất lỏng ở nhiệt độ sôi xác định).",
            r"Giải thích được vòng tuần hoàn của nước ($\text{H}_2\text{O}$) trong tự nhiên và tính toán các bài toán liên quan đến nhiệt độ chuyển thể, lượng chất bay hơi hoặc đông đặc.",
        ],
        formulas=[
            {
                "name": "Sơ đồ chuyển thể thuận nghịch giữa 3 thể",
                "formula": r"$\text{Thể rắn} \underset{\text{Đông đặc (tỏa nhiệt)}}{\overset{\text{Nóng chảy (thu nhiệt)}}{\rightleftharpoons}} \text{Thể lỏng} \underset{\text{Ngưng tụ (tỏa nhiệt)}}{\overset{\text{Bay hơi / Sôi (thu nhiệt)}}{\rightleftharpoons}} \text{Thể khí (hơi)}$",
                "note": r"Với cùng một chất tinh khiết, nhiệt độ đông đặc bằng đúng nhiệt độ nóng chảy ($t_{\text{đđ}} = t_{\text{nc}}$).",
            },
            {
                "name": "Sự thăng hoa của nước đá khô (carbon dioxide rắn)",
                "formula": r"$\text{CO}_2\text{ (rắn)} \xrightarrow{-78{,}5^\circ\text{C}} \text{CO}_2\text{ (khí)}$",
                "note": r"Đá khô ($\text{CO}_2$ rắn) chuyển trực tiếp từ thể rắn sang thể khí mà không qua thể lỏng ở áp suất thường ($1\text{ atm}$).",
            },
            {
                "name": "Tốc độ bay hơi trung bình",
                "formula": r"$v_{\text{bh}} = \dfrac{\Delta m_{\text{hơi}}}{t}$",
                "note": r"$\Delta m_{\text{hơi}}$ là khối lượng chất lỏng bay hơi ($\text{g}$), $t$ là thời gian bay hơi ($\text{h}$ hoặc $\text{phút}$).",
            },
        ],
        theory_sections=[
            {
                "title": "1. Đặc điểm ba thể của chất theo mô hình hạt",
                "content": (
                    r"Mọi chất đều được cấu tạo từ những hạt vô cùng nhỏ bé (phân tử, nguyên tử hoặc ion). Sự khác biệt giữa ba thể rắn, lỏng, khí phụ thuộc vào sự sắp xếp và liên kết của các hạt:" "\n"
                    r"- **Thể rắn** (ví dụ: thanh iron $\text{Fe}$, viên muối $\text{NaCl}$, nước đá $\text{H}_2\text{O}$ ở dưới $0^\circ\text{C}$): Các hạt xếp rất sát nhau theo trật tự xác định, lực liên kết rất chặt chẽ, các hạt chỉ dao động quanh vị trí cân bằng cố định $\rightarrow$ có **hình dạng và thể tích xác định**, rất khó bị nén." "\n"
                    r"- **Thể lỏng** (ví dụ: nước uống $\text{H}_2\text{O}$, ethanol $\text{C}_2\text{H}_5\text{OH}$, dầu ăn): Khoảng cách giữa các hạt xa hơn thể rắn, lực liên kết ở mức trung bình, các hạt trượt lên nhau dễ dàng $\rightarrow$ **không có hình dạng riêng** (có hình dạng của phần vật chứa nó), nhưng có **thể tích xác định** và khó bị nén." "\n"
                    r"- **Thể khí / hơi** (ví dụ: khí oxygen $\text{O}_2$, khí nitrogen $\text{N}_2$, hơi nước $\text{H}_2\text{O}$): Khoảng cách giữa các hạt rất xa nhau, lực liên kết rất yếu (không đáng kể), các hạt chuyển động hỗn loạn về mọi phía $\rightarrow$ **không có hình dạng và thể tích riêng** (chiếm toàn bộ thể tích bình chứa) và **rất dễ bị nén**."
                ),
            },
            {
                "title": "2. Các quá trình chuyển thể của chất",
                "content": (
                    r"- **Sự nóng chảy**: Quá trình chuyển từ thể rắn sang thể lỏng khi được cung cấp nhiệt (ví dụ: nung chảy đồng $\text{Cu}$ để đúc tượng, băng tan ở $0^\circ\text{C}$). Trong suốt thời gian chất tinh khiết đang nóng chảy, nhiệt độ của chất giữ không đổi." "\n"
                    r"- **Sự đông đặc**: Quá trình chuyển từ thể lỏng sang thể rắn khi làm lạnh (ví dụ: làm nước đá trong tủ lạnh ở $0^\circ\text{C}$, sáp nến lỏng nguội đi đông cứng lại)." "\n"
                    r"- **Sự bay hơi**: Quá trình chuyển từ thể lỏng sang thể khí (hơi) diễn ra trên **bề mặt thoáng** của chất lỏng ở **bất kỳ nhiệt độ nào**. Tốc độ bay hơi tăng khi: nhiệt độ cao hơn, gió mạnh hơn, diện tích mặt thoáng lớn hơn và độ ẩm không khí thấp hơn." "\n"
                    r"- **Sự sôi**: Là trường hợp đặc biệt của sự bay hơi, trong đó chất lỏng chuyển sang thể hơi cả ở **trên mặt thoáng lẫn trong lòng chất lỏng** (tạo các bọt khí nổi lên và vỡ ra). Sự sôi chỉ xảy ra ở một nhiệt độ xác định gọi là **nhiệt độ sôi** ($t_{\text{s}}$) và nhiệt độ giữ không đổi trong suốt quá trình sôi." "\n"
                    r"- **Sự ngưng tụ**: Quá trình chuyển từ thể khí (hơi) sang thể lỏng khi gặp lạnh (ví dụ: hơi nước trong không khí gặp thành ngoài cốc nước đá ngưng tụ thành các giọt nước đọng bên ngoài cốc; sự tạo thành sương mù, mây, mưa)." "\n"
                    r"- **Sự thăng hoa**: Quá trình một số chất chuyển trực tiếp từ **thể rắn sang thể khí** mà không qua thể lỏng (ví dụ: nước đá khô là carbon dioxide rắn $\text{CO}_2$ thăng hoa ở $-78{,}5^\circ\text{C}$ tạo làn sương lạnh bảo quản thực phẩm; viên long não hoặc tinh thể iodine $\text{I}_2$ thăng hoa)."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Giải thích hiện tượng đọng nước ngoài cốc đá và đá khô",
                "problem": (
                    r"a) Vì sao khi đặt một cốc nước đá lạnh trên bàn, một lát sau ta thấy mặt ngoài thành cốc có nhiều giọt nước bám vào?" "\n"
                    r"b) Vì sao nước đá khô ($\text{CO}_2$ rắn) được gọi là 'đá khô' và thường dùng để tạo khói trắng trên sân khấu?"
                ),
                "solution": (
                    r"- **a)** Không phải nước từ trong cốc thấm qua thủy tinh, mà do trong không khí xung quanh luôn có **hơi nước** ($\text{H}_2\text{O}$ ở thể khí). Khi gặp thành cốc nước đá có nhiệt độ thấp, hơi nước bị lạnh đi và **ngưng tụ** thành các giọt nước lỏng bám bên ngoài cốc." "\n"
                    r"- **b)** Nước đá khô là carbon dioxide rắn ($\text{CO}_2$). Ở áp suất thường, nó không nóng chảy thành chất lỏng mà **thăng hoa** trực tiếp từ thể rắn sang khí $\text{CO}_2$ ở $-78{,}5^\circ\text{C}$ nên luôn khô ráo. Quá trình thăng hoa thu nhiệt rất mạnh làm hơi nước trong không khí xung quanh ngưng tụ thành những hạt sương nhỏ li ti tạo làn khói trắng đẹp mắt."
                ),
            },
            {
                "title": "Ví dụ 2: Bài toán làm muối từ nước biển nhờ sự bay hơi",
                "problem": (
                    r"Một ô ruộng muối chứa $2000\text{ kg}$ nước biển có hàm lượng muối sodium chloride ($\text{NaCl}$) là $3{,}5\%$ về khối lượng. "
                    r"Sau một số ngày phơi nắng gió cho nước bay hơi, người diêm dân thu được dung dịch nước ót và muối kết tinh có tổng khối lượng còn lại là $250\text{ kg}$ (giả sử chỉ có nước $\text{H}_2\text{O}$ bay hơi). Tính khối lượng nước đã bay hơi."
                ),
                "solution": (
                    r"Vì muối ăn ($\text{NaCl}$) không bị bay hơi dưới ánh nắng mặt trời, toàn bộ độ giảm khối lượng của ô ruộng chính là khối lượng nước ($\text{H}_2\text{O}$) đã chuyển từ thể lỏng sang thể hơi:" "\n"
                    r"$$m_{\text{H}_2\text{O bay hơi}} = 2000 - 250 = 1750\text{ kg}$$"
                ),
            },
        ],
        key_takeaways=[
            r"Thể rắn có hình dạng và thể tích xác định, hạt xếp khít; thể lỏng có thể tích xác định nhưng không có hình dạng riêng; thể khí không có hình dạng và thể tích riêng, rất dễ nén.",
            r"Sự bay hơi diễn ra trên mặt thoáng ở mọi nhiệt độ; sự sôi diễn ra cả trong lòng và trên mặt thoáng ở nhiệt độ sôi $t_{\text{s}}$ xác định.",
            r"Nước đá khô ($\text{CO}_2$ rắn) thăng hoa trực tiếp từ thể rắn sang thể khí ở $-78{,}5^\circ\text{C}$ mà không qua thể lỏng.",
        ],
        questions=[
            mcq(
                r"Theo mô hình hạt của chất, ở trạng thái nào các hạt liên kết với nhau chặt chẽ nhất và chỉ dao động quanh vị trí cân bằng cố định?",
                [
                    r"Thể lỏng.",
                    r"Thể khí.",
                    r"Thể hơi.",
                    r"Thể rắn.",
                ],
                "D",
                "biet",
                r"Ở thể rắn, các hạt xếp rất sát nhau, lực liên kết giữa các hạt rất mạnh nên các hạt chỉ dao động quanh vị trí cân bằng cố định, giúp chất rắn có hình dạng và thể tích xác định.",
            ),
            mcq(
                r"Quá trình chất chuyển từ thể khí (hoặc hơi) sang thể lỏng khi làm lạnh được gọi là:",
                [
                    r"Sự ngưng tụ.",
                    r"Sự bay hơi.",
                    r"Sự đông đặc.",
                    r"Sự nóng chảy.",
                ],
                "A",
                "biet",
                r"Quá trình chuyển từ thể khí (hơi) sang thể lỏng được gọi là sự ngưng tụ (ngược lại với sự bay hơi).",
            ),
            mcq(
                r"Khi để một viên nước đá khô (carbon dioxide rắn, $\text{CO}_2$) ngoài không khí ở nhiệt độ phòng, viên đá khô nhỏ dần rồi biến mất mà không để lại chất lỏng nào. Hiện tượng chuyển thể của $\text{CO}_2$ rắn là:",
                [
                    r"Sự ngưng tụ (chuyển từ thể khí sang thể lỏng).",
                    r"Sự thăng hoa (chuyển trực tiếp từ thể rắn sang thể khí).",
                    r"Sự nóng chảy (chuyển từ thể rắn sang thể lỏng).",
                    r"Sự đông đặc (chuyển từ thể lỏng sang thể rắn).",
                ],
                "B",
                "biet",
                r"Ở áp suất thường, đá khô ($\text{CO}_2$ rắn) chuyển trực tiếp từ thể rắn sang thể khí ở $-78{,}5^\circ\text{C}$ mà không qua thể lỏng; hiện tượng này gọi là sự thăng hoa.",
            ),
            mcq(
                r"Đặc điểm nào sau đây là của chất ở **thể khí** (ví dụ khí oxygen $\text{O}_2$, khí nitrogen $\text{N}_2$)?",
                [
                    r"Không có hình dạng riêng nhưng có thể tích xác định, khó bị nén.",
                    r"Các hạt xếp sát nhau và không thể di chuyển tự do.",
                    r"Không có hình dạng và thể tích riêng, rất dễ bị nén.",
                    r"Có hình dạng và thể tích xác định, rất khó bị nén.",
                ],
                "C",
                "biet",
                r"Ở thể khí, khoảng cách giữa các hạt rất lớn so với kích thước hạt nên các hạt chuyển động tự do về mọi hướng, chất khí không có hình dạng và thể tích riêng (chiếm toàn bộ bình chứa) và rất dễ bị nén.",
            ),
            mcq(
                r"Điểm khác biệt cơ bản giữa **sự sôi** và **sự bay hơi** của nước ($\text{H}_2\text{O}$) là:",
                [
                    r"Sự bay hơi chỉ xảy ra ở $100^\circ\text{C}$, còn sự sôi xảy ra ở mọi nhiệt độ.",
                    r"Sự bay hơi là chuyển từ thể lỏng sang thể rắn, còn sự sôi là chuyển từ thể lỏng sang thể khí.",
                    r"Khi nước đang sôi, nhiệt độ của nước tăng liên tục theo thời gian đun.",
                    r"Sự bay hơi xảy ra ở mọi nhiệt độ chỉ trên mặt thoáng, còn sự sôi xảy ra ở nhiệt độ sôi xác định cả trên mặt thoáng và trong lòng chất lỏng.",
                ],
                "D",
                "hieu",
                r"Sự bay hơi xảy ra trên bề mặt thoáng ở bất kỳ nhiệt độ nào; còn sự sôi xảy ra ở nhiệt độ sôi xác định ($100^\circ\text{C}$ với nước ở $1\text{ atm}$), có sự tạo bọt khí cả trong lòng chất lỏng lẫn bay hơi trên mặt thoáng, và nhiệt độ giữ không đổi trong suốt khi sôi.",
            ),
            mcq(
                r"Để quần áo ướt sau khi giặt nhanh khô nhất, biện pháp nào sau đây vận dụng đầy đủ các yếu tố làm tăng tốc độ bay hơi của nước ($\text{H}_2\text{O}$)?",
                [
                    r"Căng phẳng quần áo và phơi ở nơi có nắng ấm, thoáng gió.",
                    r"Cuộn tròn quần áo lại và để trong phòng kín, ẩm thấp.",
                    r"Gấp gọn quần áo và cất ngay vào tủ gỗ đóng kín.",
                    r"Phơi quần áo vào ban đêm khi độ ẩm không khí đạt gần $100\%$.",
                ],
                "A",
                "hieu",
                r"Căng phẳng quần áo làm tăng diện tích mặt thoáng; phơi nơi nắng ấm làm tăng nhiệt độ; nơi thoáng gió giúp đưa hơi nước ra xa nhanh chóng. Cả 3 yếu tố này đều làm tăng tốc độ bay hơi của nước ($\text{H}_2\text{O}$).",
            ),
            tf4(
                r"Một học sinh tiến hành thí nghiệm đun nóng một cốc chứa các viên nước đá tinh khiết ($\text{H}_2\text{O}$) từ nhiệt độ $-10^\circ\text{C}$ ở áp suất tiêu chuẩn $1\text{ atm}$ cho đến khi nước sôi mạnh và dùng nhiệt kế theo dõi nhiệt độ theo thời gian. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Khi nhiệt độ tăng từ $-10^\circ\text{C}$ lên đến $0^\circ\text{C}$, nước đá bắt đầu chuyển từ thể rắn sang thể lỏng (sự nóng chảy).",
                    r"Trong suốt khoảng thời gian nước đá đang tan (trong cốc vừa có nước đá vừa có nước lỏng), nhiệt độ của hỗn hợp tăng dần từ $0^\circ\text{C}$ lên $20^\circ\text{C}$.",
                    r"Khi nước lỏng được đun từ $20^\circ\text{C}$ lên $80^\circ\text{C}$, trên mặt thoáng của cốc nước vẫn diễn ra sự bay hơi.",
                    r"Khi nước đã đạt $100^\circ\text{C}$ và đang sôi mạnh, nếu tiếp tục đun to lửa hơn thì nhiệt độ của nước trong cốc vẫn giữ ở $100^\circ\text{C}$.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Nhiệt độ nóng chảy của nước đá tinh khiết ở $1\text{ atm}$ là $0^\circ\text{C}$." "\n"
                    r"- **Ý b) Sai**: Trong suốt quá trình nóng chảy của chất tinh khiết, nhiệt độ của hệ giữ không đổi ở $0^\circ\text{C}$ cho đến khi toàn bộ nước đá tan hết thành nước lỏng." "\n"
                    r"- **Ý c) Đúng**: Sự bay hơi trên mặt thoáng của chất lỏng xảy ra ở mọi nhiệt độ, và nhiệt độ càng tăng thì tốc độ bay hơi càng nhanh." "\n"
                    r"- **Ý d) Đúng**: Trong suốt thời gian nước đang sôi ở áp suất $1\text{ atm}$, nhiệt độ của nước không tăng thêm mà giữ nguyên ở $100^\circ\text{C}$ (đun to lửa hơn chỉ làm nước hóa hơi nhanh hơn)."
                ),
            ),
            tf4(
                r"Khi so sánh đặc điểm hạt và ứng dụng thực tiễn của chất ở ba thể rắn, lỏng, khí như khí oxygen ($\text{O}_2$), nước ($\text{H}_2\text{O}$) và thanh kim loại iron ($\text{Fe}$), xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Người ta có thể nén một thể tích lớn khí oxygen ($\text{O}_2$) vào bình thép nhỏ cho thợ lặn và bệnh viện vì khoảng cách giữa các phân tử khí $\text{O}_2$ rất lớn.",
                    r"Khi rót $250\text{ mL}$ nước ($\text{H}_2\text{O}$) từ bình đong hình trụ sang chiếc bát rộng miệng, cả hình dạng và thể tích của lượng nước đó đều thay đổi.",
                    r"Vòng tuần hoàn của nước trong tự nhiên (nước biển bay hơi $\rightarrow$ tạo mây $\rightarrow$ mưa rơi xuống) là sự kết hợp của hai quá trình chuyển thể chính là sự bay hơi và sự ngưng tụ.",
                    r"Khi nước chuyển từ thể lỏng sang thể hơi, cấu tạo phân tử $\text{H}_2\text{O}$ bị phá vỡ thành khí hydrogen ($\text{H}_2$) và khí oxygen ($\text{O}_2$).",
                ],
                "Đ/S/Đ/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Ở thể khí, khoảng cách giữa các hạt $\text{O}_2$ rất xa nhau nên chất khí rất dễ bị nén dưới áp suất cao vào bình chứa nhỏ." "\n"
                    r"- **Ý b) Sai**: Khi rót nước sang bát, chỉ có **hình dạng** của khối chất lỏng thay đổi theo vật chứa, còn **thể tích** vẫn giữ nguyên là $250\text{ mL}$." "\n"
                    r"- **Ý c) Đúng**: Nước mặt bay hơi tạo hơi nước bay lên cao, gặp lạnh ngưng tụ thành mây và giọt nước mưa rơi xuống." "\n"
                    r"- **Ý d) Sai**: Sự chuyển thể chỉ làm thay đổi khoảng cách và sự sắp xếp giữa các phân tử $\text{H}_2\text{O}$, bản chất phân tử $\text{H}_2\text{O}$ hoàn toàn giữ nguyên (không tạo thành $\text{H}_2$ và $\text{O}_2$)."
                ),
            ),
            mcq(
                r"Một bác sĩ dùng bông tẩm cồn y tế (chứa ethanol $\text{C}_2\text{H}_5\text{OH}$) thoa lên vùng da của bệnh nhân trước khi tiêm thì bệnh nhân cảm thấy vùng da đó mát lạnh. Nguyên nhân chính xác của hiện tượng này là:",
                [
                    r"Ethanol phản ứng hóa học với khí nitrogen ($\text{N}_2$) trong không khí tạo ra nước đá.",
                    r"Ethanol ($\text{C}_2\text{H}_5\text{OH}$) bay hơi rất nhanh và quá trình bay hơi thu nhiệt từ vùng da làm da hạ nhiệt độ.",
                    r"Ethanol ($\text{C}_2\text{H}_5\text{OH}$) đông đặc ngay trên bề mặt da ở nhiệt độ $37^\circ\text{C}$.",
                    r"Hơi nước trong không khí ngưng tụ tỏa nhiệt vào vùng da.",
                ],
                "B",
                "vandung",
                r"Ethanol ($\text{C}_2\text{H}_5\text{OH}$) là chất lỏng rất dễ bay hơi. Khi thoa lên da ($37^\circ\text{C}$), ethanol bay hơi nhanh và lấy nhiệt (thu nhiệt) trực tiếp từ vùng da tiếp xúc, làm vùng da đó giảm nhiệt độ nên có cảm giác mát lạnh.",
            ),
            short(
                r"Để khảo sát tốc độ bay hơi của nước ($\text{H}_2\text{O}$), một học sinh rót $250\text{ g}$ nước vào một đĩa thủy tinh rộng miệng đặt ngoài trời nắng. Sau $4$ giờ, học sinh cân lại lượng nước còn trong đĩa thấy còn $190\text{ g}$. Giả sử tốc độ bay hơi của nước không đổi, hãy tính khối lượng nước bay hơi trung bình trong mỗi giờ theo đơn vị gam trên giờ ($\text{g/h}$).",
                ["15", "15,0", "15.0"],
                "vandung",
                (
                    r"Khối lượng nước ($\text{H}_2\text{O}$) đã bay hơi sau $4$ giờ là:" "\n"
                    r"$$\Delta m = 250 - 190 = 60\text{ g}$$" "\n"
                    r"Khối lượng nước bay hơi trung bình trong mỗi giờ là:" "\n"
                    r"$$v_{\text{bh}} = \dfrac{\Delta m}{t} = \dfrac{60}{4} = 15\text{ g/h}$$"
                ),
            ),
        ],
        description="Đặc điểm thể rắn, lỏng, khí theo mô hình hạt; các quá trình nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ và thăng hoa.",
    ),
    lesson(
        grade=6,
        order=3,
        code="H6-C03",
        title="Chương 3: Oxygen và không khí",
        topic="oxygen-khong-khi",
        summary=(
            r"Oxygen ($\text{O}_2$) là chất khí không màu, không mùi, không vị, ít tan trong nước và nặng hơn không khí, đóng vai trò thiết yếu giúp duy trì sự hô hấp của sinh vật và sự cháy của nhiên liệu. "
            r"Không khí khô và sạch là một hỗn hợp khí có thành phần phần trăm theo thể tích gồm khoảng $78\%$ khí nitrogen ($\text{N}_2$), $21\%$ khí oxygen ($\text{O}_2$) và $1\%$ các khí khác (argon $\text{Ar}$, carbon dioxide $\text{CO}_2$, hơi nước $\text{H}_2\text{O}$...). "
            r"Hiểu rõ 3 điều kiện phát sinh sự cháy giúp ta chủ động phòng cháy chữa cháy và bảo vệ môi trường không khí trong lành."
        ),
        objectives=[
            r"Trình bày được tính chất vật lý của khí oxygen ($\text{O}_2$): trạng thái, màu sắc, mùi vị, tính tan trong nước, nhiệt độ hóa lỏng ($-183^\circ\text{C}$) và tỉ khối nặng hơn không khí.",
            r"Nêu được tầm quan trọng của oxygen ($\text{O}_2$) đối với sự sống (hô hấp) và sự cháy; trình bày được 3 điều kiện phát sinh sự cháy và các biện pháp dập tắt đám cháy an toàn.",
            r"Nêu được thành phần phần trăm thể tích của không khí ($78\%$ nitrogen $\text{N}_2$, $21\%$ oxygen $\text{O}_2$, $1\%$ khí khác) và giải thích được thí nghiệm xác định thành phần phần trăm thể tích của $\text{O}_2$ trong không khí.",
            r"Trình bày được nguồn gây ô nhiễm không khí (khí thải $\text{CO}$, $\text{SO}_2$, $\text{NO}_2$, bụi mịn) và các biện pháp bảo vệ môi trường không khí.",
        ],
        formulas=[
            {
                "name": "Thành phần phần trăm thể tích không khí khô",
                "formula": r"$\%V_{\text{N}_2} \approx 78\%; \quad \%V_{\text{O}_2} \approx 21\%; \quad \%V_{\text{khí khác}} \approx 1\%$",
                "note": r"Tỉ lệ thể tích gần đúng trong thực hành: $V_{\text{O}_2} \approx \dfrac{1}{5} V_{\text{không khí}}$ (hay $20\% - 21\%$).",
            },
            {
                "name": "Công thức tính thể tích khí oxygen trong không khí",
                "formula": r"$V_{\text{O}_2} = V_{\text{không khí}} \cdot \dfrac{21}{100}$",
                "note": r"Với $V_{\text{không khí}} = a \cdot b \cdot h$ là thể tích phòng học hoặc bình chứa ($\text{m}^3$ hoặc $\text{L}$).",
            },
            {
                "name": "Phản ứng đốt cháy phosphorus đỏ xác định thành phần không khí",
                "formula": r"$4\text{P} + 5\text{O}_2 \xrightarrow{t^\circ} 2\text{P}_2\text{O}_5$",
                "note": r"Khi đốt phosphorus ($\text{P}$) dư trong ống đong úp trên chậu nước, lượng $\text{O}_2$ phản ứng hết làm nước dâng lên chiếm khoảng $\dfrac{1}{5}$ thể tích không khí ban đầu.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Tính chất và vai trò của khí oxygen",
                "content": (
                    r"- **Tính chất vật lý của oxygen ($\text{O}_2$)**: Ở điều kiện thường, oxygen là chất khí không màu, không mùi, không vị, nặng hơn không khí và **ít tan trong nước** ($1\text{ L}$ nước ở $20^\circ\text{C}$, $1\text{ atm}$ chỉ hòa tan được khoảng $31\text{ mL}$ khí $\text{O}_2$). Oxygen hóa lỏng ở $-183^\circ\text{C}$, oxygen lỏng có màu xanh nhạt." "\n"
                    r"- **Vai trò duy trì sự sống (hô hấp)**: Mọi sinh vật hiếu khí và con người đều cần khí $\text{O}_2$ để oxy hóa chất dinh dưỡng trong cơ thể, giải phóng năng lượng cho các hoạt động sống (thợ lặn, phi công, bệnh nhân suy hô hấp cần bình thở $\text{O}_2$ nén; đầm nuôi tôm cá cần quạt nước để tăng lượng $\text{O}_2$ hòa tan)." "\n"
                    r"- **Vai trò duy trì sự cháy**: Khí $\text{O}_2$ duy trì sự cháy của các nhiên liệu (củi, than $\text{C}$, khí methane $\text{CH}_4$, xăng dầu). Que đóm còn tàn đỏ khi đưa vào bình chứa khí $\text{O}_2$ tinh khiết sẽ bùng cháy thành ngọn lửa sáng chói (dấu hiệu nhận biết khí $\text{O}_2$)."
                ),
            },
            {
                "title": "2. Điều kiện phát sinh sự cháy và biện pháp dập tắt sự cháy",
                "content": (
                    r"- **Tam giác lửa (3 điều kiện cần và đủ để phát sinh sự cháy)**:" "\n"
                    r"  1. Phải có **chất cháy** (nhiên liệu: gỗ, giấy, xăng dầu, khí gas)." "\n"
                    r"  2. Phải có đủ **khí oxygen ($\text{O}_2$)** cho sự cháy." "\n"
                    r"  3. Phải có nguồn nhiệt làm chất cháy nóng đến **nhiệt độ bắt cháy**." "\n"
                    r"- **Nguyên tắc dập tắt sự cháy** (loại bỏ ít nhất 1 trong 3 điều kiện trên):" "\n"
                    r"  + Hạ nhiệt độ của chất cháy xuống thấp hơn nhiệt độ bắt cháy và ngăn cách với $\text{O}_2$ (ví dụ: phun nước vào đám cháy gỗ, giấy, vải)." "\n"
                    r"  + Cách ly chất cháy với khí $\text{O}_2$ bằng chăn chiên ướt, cát khô, bọt chữa cháy hoặc bình khí $\text{CO}_2$ nén." "\n"
                    r"  + **Lưu ý an toàn**: TUYỆT ĐỐI KHÔNG dùng nước để dập đám cháy xăng, dầu hỏa vì xăng dầu không tan trong nước và nhẹ hơn nước ($D_{\text{xăng}} \approx 0{,}7\text{ g/cm}^3 < D_{\text{H}_2\text{O}} = 1{,}0\text{ g/cm}^3$) nên sẽ nổi lên mặt nước làm đám cháy lan rộng hơn; cũng không phun nước trực tiếp vào thiết bị điện đang có điện."
                ),
            },
            {
                "title": "3. Thành phần không khí và bảo vệ môi trường không khí",
                "content": (
                    r"- **Thành phần phần trăm thể tích không khí khô**:" "\n"
                    r"  + $78\%$ khí **nitrogen** ($\text{N}_2$ - không duy trì sự cháy và sự hô hấp)." "\n"
                    r"  + $21\%$ khí **oxygen** ($\text{O}_2$ - duy trì sự sống và sự cháy)." "\n"
                    r"  + $1\%$ các khí khác: khí hiếm argon ($\text{Ar}$), khí carbon dioxide ($\text{CO}_2$), hơi nước ($\text{H}_2\text{O}$), bụi..." "\n"
                    r"- **Bảo vệ môi trường không khí**: Khói bụi từ nhà máy, phương tiện giao thông, cháy rừng, đốt rơm rạ thải ra các khí độc hại như $\text{CO}$, $\text{SO}_2$, $\text{NO}_2$ và bụi mịn gây mưa acid, hiệu ứng nhà kính và bệnh hô hấp. Cần trồng nhiều cây xanh (cây xanh quang hợp hấp thụ $\text{CO}_2$ và nhả ra $\text{O}_2$), sử dụng năng lượng sạch (điện mặt trời, điện gió), xử lý khí thải công nghiệp và không đốt rác bừa bãi."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Thí nghiệm xác định phần trăm thể tích oxygen trong không khí",
                "problem": (
                    r"Đốt cháy một lượng phosphorus đỏ ($\text{P}$) lấy dư trong muôi sắt rồi đưa nhanh vào một ống đong hình trụ có chia $5$ vạch thể tích bằng nhau đang úp trên chậu nước (ban đầu mực nước ở vạch số $0$). "
                    r"Đậy kín nút, sau khi ngọn lửa tắt hoàn toàn và ống đong nguội về nhiệt độ ban đầu, mực nước trong ống đong thay đổi như thế nào? Giải thích."
                ),
                "solution": (
                    r"- Khi phosphorus ($\text{P}$) cháy trong ống đong, nó tác dụng hết với khí oxygen ($\text{O}_2$) có trong không khí tạo thành khói trắng diphosphorus pentoxide ($\text{P}_2\text{O}_5$) tan vào nước." "\n"
                    r"- Áp suất khí trong ống giảm xuống làm nước từ chậu dâng vào ống đong để bù vào đúng thể tích khí $\text{O}_2$ đã phản ứng." "\n"
                    r"- Vì khí $\text{O}_2$ chiếm khoảng $21\%$ (xấp xỉ $\dfrac{1}{5}$) thể tích không khí nên mực nước dâng lên đến **vạch số $1$** (chiếm $\dfrac{1}{5}$ thể tích ống đong). Phần khí còn lại chiếm $\dfrac{4}{5}$ thể tích chủ yếu là khí nitrogen ($\text{N}_2$)."
                ),
            },
            {
                "title": "Ví dụ 2: Tính thể tích khí oxygen trong phòng học",
                "problem": (
                    r"Một phòng học có chiều dài $8\text{ m}$, chiều rộng $6\text{ m}$ và chiều cao $3{,}5\text{ m}$. "
                    r"Biết khí oxygen ($\text{O}_2$) chiếm $21\%$ thể tích không khí. Tính thể tích khí $\text{O}_2$ có trong phòng học theo đơn vị mét khối ($\text{m}^3$)."
                ),
                "solution": (
                    r"Thể tích không khí trong phòng học là:" "\n"
                    r"$$V_{\text{không khí}} = 8 \cdot 6 \cdot 3{,}5 = 168\text{ m}^3$$" "\n"
                    r"Thể tích khí oxygen ($\text{O}_2$) có trong phòng học là:" "\n"
                    r"$$V_{\text{O}_2} = 168 \cdot \dfrac{21}{100} = 35{,}28\text{ m}^3$$"
                ),
            },
        ],
        key_takeaways=[
            r"Khí oxygen ($\text{O}_2$) không màu, không mùi, không vị, ít tan trong nước, nặng hơn không khí, duy trì sự hô hấp và sự cháy (làm bùng cháy que đóm còn tàn đỏ).",
            r"Không khí khô gồm $78\%$ nitrogen ($\text{N}_2$), $21\%$ oxygen ($\text{O}_2$) và $1\%$ các khí khác ($\text{CO}_2$, $\text{Ar}$, hơi nước...).",
            r"Muốn dập tắt đám cháy cần hạ nhiệt độ dưới nhiệt độ bắt cháy và cách ly chất cháy với $\text{O}_2$; tuyệt đối không dùng nước dập đám cháy xăng dầu.",
        ],
        questions=[
            mcq(
                r"Trong không khí khô và sạch, thành phần phần trăm theo thể tích của khí nitrogen ($\text{N}_2$) và khí oxygen ($\text{O}_2$) lần lượt là:",
                [
                    r"$50\%$ khí nitrogen ($\text{N}_2$) và $49\%$ khí oxygen ($\text{O}_2$).",
                    r"$78\%$ khí carbon dioxide ($\text{CO}_2$) và $21\%$ khí oxygen ($\text{O}_2$).",
                    r"$78\%$ khí nitrogen ($\text{N}_2$) và $21\%$ khí oxygen ($\text{O}_2$).",
                    r"$21\%$ khí nitrogen ($\text{N}_2$) và $78\%$ khí oxygen ($\text{O}_2$).",
                ],
                "C",
                "biet",
                r"Theo thể tích, không khí khô gồm khoảng $78\%$ khí nitrogen ($\text{N}_2$), $21\%$ khí oxygen ($\text{O}_2$) và $1\%$ các khí khác.",
            ),
            mcq(
                r"Để nhận biết một lọ chứa khí oxygen ($\text{O}_2$) tinh khiết không màu, người ta dùng cách nào sau đây?",
                [
                    r"Dẫn khí đi qua dung dịch nước vôi trong $\text{Ca(OH)}_2$ xem có vẩn đục hay không.",
                    r"Quan sát màu sắc của chất khí trong lọ ở nhiệt độ phòng $25^\circ\text{C}$.",
                    r"Ngửi mùi đặc trưng của chất khí thoát ra từ miệng lọ.",
                    r"Đưa que đóm còn tàn đỏ vào miệng lọ, nếu tàn đóm bùng cháy thành ngọn lửa sáng thì đó là khí $\text{O}_2$.",
                ],
                "D",
                "biet",
                r"Khí oxygen ($\text{O}_2$) không màu, không mùi nhưng duy trì sự cháy rất mãnh liệt, làm que đóm còn tàn đỏ bùng cháy ngay thành ngọn lửa.",
            ),
            mcq(
                r"Tính chất vật lý nào sau đây của khí oxygen ($\text{O}_2$) là **đúng**?",
                [
                    r"Chất khí không màu, không mùi, không vị, ít tan trong nước và nặng hơn không khí.",
                    r"Chất khí màu xanh nhạt ở điều kiện thường, tan rất nhiều trong nước.",
                    r"Chất khí có mùi hắc, nhẹ hơn không khí và hóa lỏng ở $0^\circ\text{C}$.",
                    r"Chất khí không màu, không duy trì sự cháy và sự hô hấp.",
                ],
                "A",
                "biet",
                r"Ở điều kiện thường, oxygen ($\text{O}_2$) là chất khí không màu, không mùi, không vị, ít tan trong nước ($1\text{ L}$ nước ở $20^\circ\text{C}$ hòa tan khoảng $31\text{ mL}$ $\text{O}_2$), nặng hơn không khí và chỉ hóa lỏng ở $-183^\circ\text{C}$.",
            ),
            mcq(
                r"Quá trình tự nhiên nào sau đây giúp hấp thụ khí carbon dioxide ($\text{CO}_2$) và giải phóng khí oxygen ($\text{O}_2$) để giữ cân bằng thành phần không khí trên Trái Đất?",
                [
                    r"Quá trình phun trào núi lửa và cháy rừng.",
                    r"Quá trình quang hợp của cây xanh dưới ánh sáng mặt trời.",
                    r"Quá trình hô hấp của động vật và con người.",
                    r"Quá trình đốt cháy nhiên liệu hóa thạch trong các nhà máy nhiệt điện.",
                ],
                "B",
                "biet",
                r"Quá trình quang hợp của cây xanh sử dụng năng lượng ánh sáng mặt trời để tổng hợp chất hữu cơ từ khí $\text{CO}_2$ và nước ($\text{H}_2\text{O}$), đồng thời giải phóng khí $\text{O}_2$ vào bầu khí quyển.",
            ),
            mcq(
                r"Tại sao trong các đầm nuôi tôm, cá công nghiệp với mật độ dày, người nuôi phải lắp đặt hệ thống cánh quạt đảo nước hoạt động liên tục trên mặt đầm?",
                [
                    r"Vì khí nitrogen ($\text{N}_2$) trong không khí cần được hòa tan để làm ấm nước.",
                    r"Vì phân tử nước ($\text{H}_2\text{O}$) khi bị cánh quạt đập mạnh sẽ tự phân hủy thành khí $\text{O}_2$.",
                    r"Vì khí oxygen ($\text{O}_2$) ít tan trong nước nên quạt nước giúp tăng diện tích tiếp xúc giữa nước và không khí, hòa tan thêm $\text{O}_2$ cho tôm cá hô hấp.",
                    r"Vì quạt nước giúp làm nước bay hơi nhanh để tăng nồng độ muối trong đầm.",
                ],
                "C",
                "hieu",
                r"Do khí oxygen ($\text{O}_2$) ít tan trong nước, khi nuôi mật độ cao lượng $\text{O}_2$ hòa tan dễ bị cạn kiệt. Quạt đảo nước làm xáo trộn bề mặt, tăng diện tích tiếp xúc giữa nước và không khí giúp $\text{O}_2$ hòa tan vào nước nhanh hơn.",
            ),
            mcq(
                r"Vì sao tuyệt đối **không** được dùng nước ($\text{H}_2\text{O}$) để dập tắt đám cháy do xăng hoặc dầu hỏa gây ra?",
                [
                    r"Vì nước tác dụng hóa học với xăng dầu tạo ra thêm khí oxygen ($\text{O}_2$).",
                    r"Vì xăng dầu nặng hơn nước nên chìm xuống đáy làm nước sôi bắn tung tóe.",
                    r"Vì nhiệt độ sôi của nước cao hơn nhiệt độ bắt cháy của kim loại iron ($\text{Fe}$).",
                    r"Vì xăng dầu không tan trong nước và nhẹ hơn nước nên sẽ nổi lên trên mặt nước, làm đám cháy lan rộng hơn.",
                ],
                "D",
                "hieu",
                r"Xăng dầu không tan trong nước và có khối lượng riêng nhỏ hơn nước ($D \approx 0{,}7 - 0{,}8\text{ g/cm}^3 < 1{,}0\text{ g/cm}^3$). Nếu phun nước, xăng dầu đang cháy sẽ nổi lên trên mặt nước và chảy tràn ra xung quanh làm đám cháy bùng phát rộng hơn. Để dập cháy xăng dầu phải dùng cát, chăn ướt hoặc bình bọt/khí $\text{CO}_2$.",
            ),
            tf4(
                r"Một nhóm học sinh thực hiện thí nghiệm: gắn một cây nến nhỏ vào đế đặt trong chậu nước có pha màu, đốt nến cháy rồi úp chụp một ống đong thủy tinh hình trụ lên cây nến. Xét tính đúng/sai của các nhận định sau về thí nghiệm:",
                [
                    r"Cây nến cháy sáng một lúc rồi yếu dần và tự tắt dù phần sáp nến vẫn còn nhiều.",
                    r"Nguyên nhân cây nến tắt là do khí nitrogen ($\text{N}_2$) trong ống đong đã phản ứng hết với sáp nến.",
                    r"Sau khi nến tắt và ống đong nguội về nhiệt độ phòng, mực nước trong ống đong dâng lên chiếm khoảng $\dfrac{1}{5}$ thể tích không khí ban đầu trong ống.",
                    r"Thí nghiệm này chứng minh khí oxygen ($\text{O}_2$) duy trì sự cháy và chiếm khoảng $\dfrac{1}{5}$ (tức khoảng $20\% - 21\%$) thể tích không khí.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Khi lượng khí oxygen ($\text{O}_2$) trong ống đong bị tiêu thụ cạn dần bởi sự cháy của nến, ngọn lửa yếu đi rồi tắt hẳn." "\n"
                    r"- **Ý b) Sai**: Khí nitrogen ($\text{N}_2$) không duy trì sự cháy; nến tắt là do hết khí **oxygen** ($\text{O}_2$)." "\n"
                    r"- **Ý c) Đúng**: Lượng khí $\text{O}_2$ mất đi làm áp suất trong ống giảm, nước dâng lên chiếm khoảng $\dfrac{1}{5}$ thể tích ống đong." "\n"
                    r"- **Ý d) Đúng**: Kết quả thí nghiệm khẳng định vai trò duy trì sự cháy của $\text{O}_2$ và tỉ lệ thể tích $V_{\text{O}_2} \approx \dfrac{1}{5} V_{\text{không khí}}$."
                ),
            ),
            tf4(
                r"Xét các tình huống ứng phó với sự cháy, hô hấp và bảo vệ môi trường không khí trong đời sống thực tiễn. Các phát biểu sau đây là đúng hay sai?",
                [
                    r"Khi dùng bình chữa cháy chứa khí carbon dioxide ($\text{CO}_2$) nén phun vào đám cháy, khí $\text{CO}_2$ vừa làm lạnh vùng cháy vừa bao phủ ngăn cách chất cháy với khí oxygen ($\text{O}_2$).",
                    r"Việc đun bếp than tổ ong trong phòng ngủ đóng kín cửa vào mùa đông là an toàn vì than cháy chỉ tạo ra khí oxygen ($\text{O}_2$).",
                    r"Trồng nhiều cây xanh quanh khu đô thị và khu công nghiệp giúp giảm lượng bụi và giảm nồng độ khí carbon dioxide ($\text{CO}_2$) trong không khí.",
                    r"Khi đi vào các hang sâu, giếng sâu lâu ngày không thông khí, người ta cần kiểm tra hàm lượng khí oxygen ($\text{O}_2$) trước vì nơi đó có thể thiếu $\text{O}_2$ và tích tụ nhiều khí $\text{CO}_2$, $\text{CH}_4$ gây ngạt.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Khí $\text{CO}_2$ nén khi thoát ra khỏi bình thu nhiệt mạnh làm hạ nhiệt độ vùng cháy, đồng thời $\text{CO}_2$ nặng hơn không khí và không duy trì sự cháy nên bao phủ cách ly chất cháy với $\text{O}_2$." "\n"
                    r"- **Ý b) Sai**: Đốt than trong phòng kín tiêu thụ hết khí $\text{O}_2$ và sinh ra nhiều khí $\text{CO}_2$ cùng khí carbon monoxide ($\text{CO}$) cực độc, gây ngạt thở nguy hiểm đến tính mạng." "\n"
                    r"- **Ý c) Đúng**: Tán lá cây cản bụi và quá trình quang hợp hấp thụ $\text{CO}_2$, giải phóng $\text{O}_2$." "\n"
                    r"- **Ý d) Đúng**: Hang sâu, giếng sâu kín gió dễ tích tụ khí $\text{CO}_2$ (nặng hơn không khí) hoặc khí độc và thiếu hụt $\text{O}_2$, dễ gây ngạt thở."
                ),
            ),
            mcq(
                r"Trung bình mỗi giờ một người trưởng thành cần hít vào khoảng $20\text{ L}$ khí oxygen ($\text{O}_2$) nguyên chất để duy trì hô hấp. Biết khí $\text{O}_2$ chiếm $21\%$ thể tích không khí. Thể tích không khí tối thiểu mà một người cần hít thở trong $1$ ngày đêm ($24$ giờ), làm tròn đến hàng đơn vị theo đơn vị lít ($\text{L}$), là:",
                [
                    r"$2286\text{ L}$.",
                    r"$480\text{ L}$.",
                    r"$1008\text{ L}$.",
                    r"$2400\text{ L}$.",
                ],
                "A",
                "vandung",
                r"Trong $24$ giờ, thể tích khí oxygen ($\text{O}_2$) một người cần là: $V_{\text{O}_2} = 20 \cdot 24 = 480\text{ L}$. Vì $\text{O}_2$ chiếm $21\%$ thể tích không khí nên thể tích không khí cần thiết là: $V_{\text{không khí}} = \dfrac{480 \cdot 100}{21} \approx 2285{,}71\text{ L} \approx 2286\text{ L}$.",
            ),
            short(
                r"Một phòng học tiêu chuẩn có chiều dài $10\text{ m}$, chiều rộng $6\text{ m}$ và chiều cao $3{,}5\text{ m}$. Biết khí oxygen ($\text{O}_2$) chiếm $21\%$ thể tích không khí. Hãy tính thể tích khí oxygen ($\text{O}_2$) có trong phòng học đó theo đơn vị mét khối ($\text{m}^3$, ghi kết quả số thập phân chính xác đến hàng phần mười).",
                ["44,1", "44.1"],
                "vandung",
                (
                    r"Thể tích không khí trong phòng học hình hộp chữ nhật là:" "\n"
                    r"$$V_{\text{không khí}} = 10 \cdot 6 \cdot 3{,}5 = 210\text{ m}^3$$" "\n"
                    r"Thể tích khí oxygen ($\text{O}_2$) có trong phòng học là:" "\n"
                    r"$$V_{\text{O}_2} = 210 \cdot \dfrac{21}{100} = 44{,}1\text{ m}^3$$"
                ),
            ),
        ],
        description="Tính chất, vai trò của oxygen đối với sự sống và sự cháy, điều kiện phát sinh và dập tắt sự cháy, thành phần không khí và bảo vệ môi trường không khí.",
    ),
    lesson(
        grade=6,
        order=4,
        code="H6-C04",
        title="Chương 4: Hỗn hợp, huyền phù, nhũ tương và tách chất",
        topic="hon-hop",
        summary=(
            r"Chất tinh khiết chỉ gồm một chất duy nhất và có các tính chất vật lý, hóa học xác định, còn hỗn hợp gồm hai hay nhiều chất trộn lẫn vào nhau. "
            r"Hỗn hợp được chia thành hỗn hợp đồng nhất (như dung dịch nước muối $\text{NaCl}$, nước đường) và hỗn hợp không đồng nhất — bao gồm huyền phù (hạt chất rắn lơ lửng trong chất lỏng) và nhũ tương (giọt chất lỏng lơ lửng trong chất lỏng khác). "
            r"Dựa vào sự khác nhau về tính chất vật lý (tính tan, kích thước hạt, nhiệt độ sôi, khối lượng riêng, từ tính), ta tách các chất ra khỏi hỗn hợp bằng phương pháp lọc, cô cạn, chiết, chưng cất hoặc dùng nam châm."
        ),
        objectives=[
            r"Phân biệt được chất tinh khiết (như nước cất $\text{H}_2\text{O}$, sodium chloride $\text{NaCl}$ tinh khiết) và hỗn hợp (nước tự nhiên, nước khoáng, không khí).",
            r"Phân biệt được hỗn hợp đồng nhất (dung dịch) và hỗn hợp không đồng nhất; nêu được khái niệm và ví dụ thực tế về huyền phù (nước phù sa) và nhũ tương (sữa, hỗn hợp dầu ăn và nước).",
            r"Trình bày được nguyên tắc và dụng cụ của các phương pháp tách chất: lắng - gạn - lọc, cô cạn, chiết, chưng cất và dùng nam châm.",
            r"Thiết kế được quy trình tách các chất từ hỗn hợp thực tế (ví dụ tách muối ăn $\text{NaCl}$ từ hỗn hợp muối lẫn cát, tách dầu ăn khỏi nước) và tính toán hiệu suất/khối lượng chất thu được.",
        ],
        formulas=[
            {
                "name": "Tổng khối lượng hỗn hợp",
                "formula": r"$m_{\text{hh}} = m_1 + m_2 + \dots + m_n$",
                "note": r"Khối lượng hỗn hợp bằng tổng khối lượng các chất thành phần tạo nên hỗn hợp.",
            },
            {
                "name": "Thành phần phần trăm khối lượng của một chất trong hỗn hợp",
                "formula": r"$\%m_A = \dfrac{m_A}{m_{\text{hh}}} \cdot 100\%$",
                "note": r"$m_A$ là khối lượng chất $A$ ($\text{g}$), $m_{\text{hh}}$ là khối lượng toàn bộ hỗn hợp ($\text{g}$).",
            },
            {
                "name": "Bảng chọn phương pháp tách chất theo tính chất vật lý",
                "formula": r"$\text{Lọc (rắn không tan/lỏng)} \mid \text{Cô cạn (rắn tan không bay hơi/lỏng)} \mid \text{Chiết (2 chất lỏng không tan)}$",
                "note": r"Chưng cất dùng tách các chất lỏng tan vào nhau có nhiệt độ sôi khác nhau (như ethanol $78{,}3^\circ\text{C}$ và nước $100^\circ\text{C}$).",
            },
        ],
        theory_sections=[
            {
                "title": "1. Chất tinh khiết và hỗn hợp",
                "content": (
                    r"- **Chất tinh khiết (chất nguyên chất)**: Được tạo nên từ một chất duy nhất, không lẫn chất nào khác. Mỗi chất tinh khiết có thành phần và tính chất vật lý (nhiệt độ nóng chảy $t_{\text{nc}}$, nhiệt độ sôi $t_{\text{s}}$, khối lượng riêng $D$) hoàn toàn xác định (ví dụ: nước cất $\text{H}_2\text{O}$ sôi đúng ở $100^\circ\text{C}$ và có $D = 1{,}00\text{ g/cm}^3$ ở $1\text{ atm}$)." "\n"
                    r"- **Hỗn hợp**: Được tạo nên khi hai hay nhiều chất trộn lẫn vào nhau. Tính chất của hỗn hợp phụ thuộc vào thành phần các chất trong đó (ví dụ: nước muối có nhiệt độ sôi cao hơn $100^\circ\text{C}$ và khối lượng riêng lớn hơn $1\text{ g/cm}^3$)." "\n"
                    r"- **Hỗn hợp đồng nhất**: Có thành phần giống nhau tại mọi vị trí trong toàn bộ hỗn hợp (ví dụ: dung dịch nước muối $\text{NaCl}$, nước đường, không khí sạch, cồn y tế)." "\n"
                    r"- **Hỗn hợp không đồng nhất**: Thành phần không giống nhau trong toàn bộ hỗn hợp, các chất vẫn phân bố tách biệt (ví dụ: hỗn hợp cát và nước, hỗn hợp dầu ăn và nước)."
                ),
            },
            {
                "title": "2. Huyền phù và nhũ tương",
                "content": (
                    r"- **Huyền phù**: Là hỗn hợp không đồng nhất gồm các **hạt chất rắn nhỏ** lơ lửng trong môi trường chất lỏng. Nếu để yên một thời gian, các hạt chất rắn sẽ lắng xuống đáy (ví dụ: nước sông phù sa, nước bột sắn dây chưa nấu chín, nước vôi sữa)." "\n"
                    r"- **Nhũ tương**: Là hỗn hợp không đồng nhất gồm một hay nhiều **chất lỏng phân tán dưới dạng các giọt nhỏ** lơ lửng trong một chất lỏng khác không hòa tan vào nhau (ví dụ: hỗn hợp dầu ăn và nước khi lắc mạnh, sữa tươi, sốt mayonnaise làm từ dầu ăn, lòng đỏ trứng và giấm)."
                ),
            },
            {
                "title": "3. Các phương pháp tách chất ra khỏi hỗn hợp",
                "content": (
                    r"Dựa vào sự khác nhau về tính chất vật lý của các chất, ta chọn phương pháp tách phù hợp:" "\n"
                    r"- **Phương pháp lọc (kết hợp lắng, gạn)**: Dùng để tách **chất rắn không tan** ra khỏi hỗn hợp với chất lỏng (sử dụng phễu lọc và giấy lọc). Ví dụ: lọc tách cát hoặc bã trà ra khỏi nước; lọc nước đục." "\n"
                    r"- **Phương pháp cô cạn**: Dùng để tách **chất rắn tan** (không bị bay hơi hoặc phân hủy bởi nhiệt) ra khỏi dung dịch bằng cách đun nóng cho dung môi bay hơi hết. Ví dụ: cô cạn dung dịch nước muối thu muối ăn $\text{NaCl}$ rắn." "\n"
                    r"- **Phương pháp chiết**: Dùng để tách **các chất lỏng không hòa tan vào nhau** và tách thành các lớp riêng biệt (do khác khối lượng riêng $D$) bằng dụng cụ là **phễu chiết**. Ví dụ: tách dầu ăn ($D \approx 0{,}8\text{ g/cm}^3$ nổi ở lớp trên) ra khỏi nước ($D = 1{,}0\text{ g/cm}^3$ nằm ở lớp dưới)." "\n"
                    r"- **Phương pháp chưng cất**: Dùng để tách các chất lỏng hòa tan vào nhau nhưng có **nhiệt độ sôi khác nhau** (ví dụ: chưng cất hỗn hợp ethanol $\text{C}_2\text{H}_5\text{OH}$ sôi ở $78{,}3^\circ\text{C}$ và nước $\text{H}_2\text{O}$ sôi ở $100^\circ\text{C}$)." "\n"
                    r"- **Phương pháp dùng nam châm**: Dùng tách chất có tính nhiễm từ như mạt iron ($\text{Fe}$) ra khỏi hỗn hợp với chất không bị nam châm hút như bột sulfur ($\text{S}$), bột aluminium ($\text{Al}$) hoặc cát."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân loại dung dịch, huyền phù và nhũ tương",
                "problem": (
                    r"Cho ba cốc nước sau khi khuấy đều với: (1) $1$ thìa muối ăn ($\text{NaCl}$), (2) $1$ thìa bột đất sét mịn, (3) $1$ thìa dầu ăn. "
                    r"Hãy xác định cốc nào chứa dung dịch (hỗn hợp đồng nhất), cốc nào chứa huyền phù và cốc nào chứa nhũ tương."
                ),
                "solution": (
                    r"- **Cốc (1)** là **dung dịch (hỗn hợp đồng nhất)** vì muối ăn ($\text{NaCl}$) tan hoàn toàn vào nước tạo hỗn hợp trong suốt đồng nhất." "\n"
                    r"- **Cốc (2)** là **huyền phù** vì các hạt bột đất sét rắn không tan lơ lửng làm đục nước và sẽ lắng dần xuống đáy khi để yên." "\n"
                    r"- **Cốc (3)** là **nhũ tương** vì các giọt dầu ăn lỏng không tan phân tán lơ lửng trong nước lỏng."
                ),
            },
            {
                "title": "Ví dụ 2: Tinh chế muối ăn lẫn cát",
                "problem": (
                    r"Một mẫu muối thô nặng $25\text{ g}$ gồm sodium chloride ($\text{NaCl}$) bị lẫn cát ($\text{SiO}_2$). Hòa tan hoàn toàn mẫu muối này vào nước dư, sau đó đem lọc qua giấy lọc thu được phần bã cát trên giấy lọc (sau khi sấy khô nặng $3\text{ g}$) và phần nước lọc trong suốt. "
                    r"Cô cạn hoàn toàn phần nước lọc thì thu được bao nhiêu gam muối $\text{NaCl}$ tinh khiết? Tính phần trăm khối lượng $\text{NaCl}$ trong mẫu muối thô."
                ),
                "solution": (
                    r"- Cát ($\text{SiO}_2$) không tan trong nước nên giữ lại trên giấy lọc với khối lượng $m_{\text{cát}} = 3\text{ g}$." "\n"
                    r"- Muối sodium chloride ($\text{NaCl}$) tan hết vào nước lọc và không bị bay hơi khi cô cạn, nên khối lượng $\text{NaCl}$ tinh khiết thu được là:" "\n"
                    r"$$m_{\text{NaCl}} = m_{\text{hh}} - m_{\text{cát}} = 25 - 3 = 22\text{ g}$$" "\n"
                    r"- Thành phần phần trăm khối lượng của $\text{NaCl}$ trong mẫu muối thô là:" "\n"
                    r"$$\%m_{\text{NaCl}} = \dfrac{22}{25} \cdot 100\% = 88\%$$"
                ),
            },
        ],
        key_takeaways=[
            r"Chất tinh khiết gồm 1 chất duy nhất có $t_{\text{nc}}$, $t_{\text{s}}$, $D$ xác định; hỗn hợp gồm từ 2 chất trở lên trộn lẫn.",
            r"Huyền phù là hạt rắn lơ lửng trong chất lỏng; nhũ tương là giọt chất lỏng lơ lửng trong chất lỏng khác không tan vào nhau.",
            r"Lọc tách chất rắn không tan khỏi chất lỏng; cô cạn tách chất rắn tan không bay hơi khỏi dung dịch; chiết tách hai chất lỏng không tan vào nhau.",
        ],
        questions=[
            mcq(
                r"Mẫu chất nào dưới đây được coi là một **chất tinh khiết**?",
                [
                    r"Nước giải khát có gas.",
                    r"Nước cất ($\text{H}_2\text{O}$) dùng pha thuốc tiêm trong y tế.",
                    r"Nước khoáng thiên nhiên đóng chai.",
                    r"Nước biển tự nhiên.",
                ],
                "B",
                "biet",
                r"Nước cất ($\text{H}_2\text{O}$) chỉ gồm một chất duy nhất là nước tinh khiết. Nước khoáng, nước biển và nước giải khát có gas đều chứa nước cùng nhiều muối khoáng hoặc chất khí hòa tan nên là hỗn hợp.",
            ),
            mcq(
                r"Hỗn hợp không đồng nhất gồm các hạt chất rắn nhỏ lơ lửng trong chất lỏng (như nước phù sa sông Cửu Long) được gọi là:",
                [
                    r"Dung dịch.",
                    r"Hợp kim.",
                    r"Huyền phù.",
                    r"Nhũ tương.",
                ],
                "C",
                "biet",
                r"Huyền phù là hỗn hợp không đồng nhất gồm các hạt chất rắn nhỏ lơ lửng trong môi trường chất lỏng.",
            ),
            mcq(
                r"Để tách dầu ăn và nước ($\text{H}_2\text{O}$) ra khỏi hỗn hợp của chúng trong phòng thí nghiệm, người ta sử dụng dụng cụ và phương pháp nào sau đây?",
                [
                    r"Dùng giấy lọc theo phương pháp lọc.",
                    r"Dùng bát sứ và đèn cồn theo phương pháp cô cạn.",
                    r"Dùng thanh nam châm vĩnh cửu.",
                    r"Dùng phễu chiết theo phương pháp chiết.",
                ],
                "D",
                "biet",
                r"Dầu ăn và nước ($\text{H}_2\text{O}$) là hai chất lỏng không hòa tan vào nhau và phân thành hai lớp rõ rệt (dầu ăn nhẹ hơn nổi lên trên, nước nặng hơn ở dưới), nên dùng phễu chiết theo phương pháp chiết để tách riêng.",
            ),
            mcq(
                r"Khi cho một thìa dầu ăn vào cốc nước ($\text{H}_2\text{O}$) rồi khuấy hoặc lắc mạnh, ta thu được các giọt dầu nhỏ li ti lơ lửng trong nước. Hỗn hợp lúc đó thuộc loại:",
                [
                    r"Nhũ tương.",
                    r"Huyền phù.",
                    r"Dung dịch bão hòa.",
                    r"Chất tinh khiết.",
                ],
                "A",
                "biet",
                r"Nhũ tương là hỗn hợp không đồng nhất gồm các giọt nhỏ của một chất lỏng (dầu ăn) phân tán lơ lửng trong một chất lỏng khác không hòa tan (nước).",
            ),
            mcq(
                r"Một học sinh có hỗn hợp bột gồm mạt kim loại iron ($\text{Fe}$), muối ăn sodium chloride ($\text{NaCl}$) và cát ($\text{SiO}_2$). Thứ tự các bước hợp lý nhất để tách riêng từng chất ra khỏi hỗn hợp là:",
                [
                    r"Đun nóng chảy toàn bộ hỗn hợp ở $1538^\circ\text{C}$ rồi lọc qua giấy lọc.",
                    r"Dùng nam châm hút tách $\text{Fe}$ $\rightarrow$ hòa tan phần còn lại vào nước rồi lọc tách cát $\rightarrow$ cô cạn nước lọc để thu muối $\text{NaCl}$.",
                    r"Cô cạn hỗn hợp trước $\rightarrow$ dùng phễu chiết tách cát $\rightarrow$ dùng giấy lọc tách $\text{Fe}$.",
                    r"Hòa tan tất cả vào dầu ăn $\rightarrow$ lọc lấy muối $\text{NaCl}$ $\rightarrow$ cô cạn thu cát.",
                ],
                "B",
                "hieu",
                r"Bước 1: Dùng nam châm hút mạt iron ($\text{Fe}$) vì chỉ có $\text{Fe}$ có từ tính. Bước 2: Cho nước vào hỗn hợp ($\text{NaCl} + \text{cát}$), khuấy cho $\text{NaCl}$ tan hết rồi lọc qua giấy lọc để giữ lại cát ($\text{SiO}_2$ không tan). Bước 3: Đun cô cạn nước lọc cho nước ($\text{H}_2\text{O}$) bay hơi hết, thu được muối $\text{NaCl}$ rắn.",
            ),
            mcq(
                r"Vì sao không thể dùng phương pháp lọc qua giấy lọc để tách muối ăn sodium chloride ($\text{NaCl}$) ra khỏi dung dịch nước muối?",
                [
                    r"Vì giấy lọc phản ứng hóa học với muối ăn $\text{NaCl}$ tạo ra chất khí.",
                    r"Vì muối ăn $\text{NaCl}$ nhẹ hơn nước nên luôn nổi lên trên mặt giấy lọc.",
                    r"Vì trong dung dịch nước muối, các hạt của $\text{NaCl}$ đã phân bố đồng nhất và có kích thước vô cùng nhỏ nên đi xuyên qua hết các lỗ nhỏ của giấy lọc.",
                    r"Vì muối ăn $\text{NaCl}$ là chất lỏng không tan trong nước.",
                ],
                "C",
                "hieu",
                r"Trong dung dịch nước muối đồng nhất, chất tan $\text{NaCl}$ phân tán thành các hạt ion ($\text{Na}^+$, $\text{Cl}^-$) kích thước siêu hiển vi, nhỏ hơn rất nhiều so với lỗ trống của giấy lọc nên chảy qua giấy lọc cùng với nước.",
            ),
            tf4(
                r"Trong thực tế đời sống và phòng thí nghiệm, người ta thường làm việc với các hỗn hợp khác nhau như sữa tươi, nước phù sa, nước muối sinh lý ($0{,}9\%$ $\text{NaCl}$) và hỗn hợp cồn - nước. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Nước muối sinh lý ($0{,}9\%$ $\text{NaCl}$) là một hỗn hợp đồng nhất (dung dịch), trong đó nước ($\text{H}_2\text{O}$) là dung môi và $\text{NaCl}$ là chất tan.",
                    r"Sữa tươi và sốt mayonnaise là các ví dụ điển hình về hệ huyền phù trong thực phẩm.",
                    r"Khi để yên một cốc nước phù sa sau một thời gian, các hạt bùn đất rắn lơ lửng sẽ lắng dần xuống đáy cốc dưới tác dụng của trọng lực.",
                    r"Để tách rượu ethanol ($\text{C}_2\text{H}_5\text{OH}$, sôi ở $78{,}3^\circ\text{C}$) ra khỏi hỗn hợp đồng nhất với nước ($\text{H}_2\text{O}$, sôi ở $100^\circ\text{C}$), người ta dùng phương pháp chưng cất.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Muối $\text{NaCl}$ tan hoàn toàn trong nước tạo hỗn hợp đồng nhất gọi là dung dịch." "\n"
                    r"- **Ý b) Sai**: Sữa tươi (các giọt chất béo lỏng phân tán trong nước) và sốt mayonnaise là **nhũ tương**, không phải huyền phù." "\n"
                    r"- **Ý c) Đúng**: Nước phù sa là huyền phù chứa các hạt bùn đất rắn không tan; khi để yên các hạt rắn nặng hơn nước sẽ lắng xuống đáy." "\n"
                    r"- **Ý d) Đúng**: Ethanol và nước tan vô hạn vào nhau tạo hỗn hợp đồng nhất nhưng có nhiệt độ sôi chênh lệch đáng kể ($78{,}3^\circ\text{C}$ và $100^\circ\text{C}$), nên tách bằng phương pháp chưng cất."
                ),
            ),
            tf4(
                r"Một học sinh dùng phễu chiết để tách hỗn hợp gồm $100\text{ mL}$ nước cất ($\text{H}_2\text{O}$, khối lượng riêng $D_1 = 1{,}00\text{ g/cm}^3$) và $100\text{ mL}$ dầu hỏa (khối lượng riêng $D_2 = 0{,}80\text{ g/cm}^3$, không tan trong nước). Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Sau khi đổ hỗn hợp vào phễu chiết và để yên, hỗn hợp tách thành hai lớp: lớp trên là dầu hỏa, lớp dưới là nước ($\text{H}_2\text{O}$).",
                    r"Tổng khối lượng của hai chất lỏng trong phễu chiết là $200\text{ g}$.",
                    r"Khi mở khóa phễu chiết từ từ ở đáy phễu, chất lỏng chảy ra khỏi vòi phễu chiết trước là dầu hỏa.",
                    r"Phương pháp chiết này dựa trên sự khác nhau về nhiệt độ sôi của dầu hỏa và nước.",
                ],
                "Đ/S/S/S",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Dầu hỏa không tan trong nước và có khối lượng riêng nhỏ hơn ($0{,}80\text{ g/cm}^3 < 1{,}00\text{ g/cm}^3$) nên nổi lên lớp trên, còn nước nằm ở lớp dưới." "\n"
                    r"- **Ý b) Sai**: Ta có $m_{\text{H}_2\text{O}} = 100 \cdot 1{,}00 = 100\text{ g}$ và $m_{\text{dầu}} = 100 \cdot 0{,}80 = 80\text{ g}$, nên tổng khối lượng là $100 + 80 = 180\text{ g}$ (không phải $200\text{ g}$)." "\n"
                    r"- **Ý c) Sai**: Vì nước ($\text{H}_2\text{O}$) nặng hơn nằm ở lớp dưới sát khóa phễu nên khi mở khóa, **nước** sẽ chảy ra trước." "\n"
                    r"- **Ý d) Sai**: Phương pháp chiết bằng phễu chiết dựa trên tính chất hai chất lỏng **không hòa tan vào nhau** và có **khối lượng riêng khác nhau** (không phải dựa vào nhiệt độ sôi)."
                ),
            ),
            mcq(
                r"Một hỗn hợp rắn nặng $40\text{ g}$ gồm bột kim loại iron ($\text{Fe}$), bột đá vôi ($\text{CaCO}_3$ không tan trong nước) và muối ăn ($\text{NaCl}$ tan tốt trong nước). Đầu tiên dùng nam châm hút hết $\text{Fe}$ thu được $8\text{ g}$ $\text{Fe}$. Phần còn lại hòa tan vào nước dư rồi lọc lấy chất rắn không tan đem sấy khô cân nặng $12\text{ g}$. Cô cạn phần nước lọc thu được bao nhiêu gam muối $\text{NaCl}$ (giả sử hao hụt không đáng kể)?",
                [
                    r"$32\text{ g}$.",
                    r"$28\text{ g}$.",
                    r"$12\text{ g}$.",
                    r"$20\text{ g}$.",
                ],
                "D",
                "vandung",
                r"Theo bảo toàn khối lượng các thành phần trong hỗn hợp: $m_{\text{hh}} = m_{\text{Fe}} + m_{\text{CaCO}_3} + m_{\text{NaCl}}$. Chất rắn không tan giữ lại trên giấy lọc là $\text{CaCO}_3$ nặng $12\text{ g}$. Do đó khối lượng muối ăn $\text{NaCl}$ thu được khi cô cạn nước lọc là: $m_{\text{NaCl}} = 40 - 8 - 12 = 20\text{ g}$.",
            ),
            short(
                r"Để tinh chế một mẫu muối mỏ nặng $50\text{ g}$ có chứa sodium chloride ($\text{NaCl}$) lẫn tạp chất đất cát không tan, một học sinh hòa tan mẫu muối vào nước dư, lọc bỏ phần đất cát không tan (sau khi sấy khô phần bã đất cát này cân nặng $6\text{ g}$), rồi cô cạn hoàn toàn nước lọc thu được muối $\text{NaCl}$ tinh khiết. Hãy tính thành phần phần trăm khối lượng của $\text{NaCl}$ trong mẫu muối mỏ ban đầu theo đơn vị phần trăm ($\%$).",
                ["88", "88,0", "88.0"],
                "vandung",
                (
                    r"Khối lượng muối sodium chloride ($\text{NaCl}$) tinh khiết có trong $50\text{ g}$ muối mỏ là:" "\n"
                    r"$$m_{\text{NaCl}} = 50 - 6 = 44\text{ g}$$" "\n"
                    r"Thành phần phần trăm khối lượng của $\text{NaCl}$ trong mẫu muối mỏ là:" "\n"
                    r"$$\%m_{\text{NaCl}} = \dfrac{44}{50} \cdot 100\% = 88\%$$"
                ),
            ),
        ],
        description="Chất tinh khiết và hỗn hợp đồng nhất, hỗn hợp không đồng nhất, huyền phù, nhũ tương và các phương pháp tách chất: cô cạn, lọc, chiết, chưng cất, dùng nam châm.",
    ),
    lesson(
        grade=6,
        order=5,
        code="H6-C05",
        title="Chương 5: Dung dịch, chất tan, dung môi và độ tan",
        topic="dung-dich",
        summary=(
            r"Dung dịch là hỗn hợp đồng nhất của chất tan và dung môi (thường gặp nhất là dung môi nước $\text{H}_2\text{O}$). "
            r"Ở một nhiệt độ xác định, dung dịch chưa bão hòa vẫn có thể hòa tan thêm chất tan, còn dung dịch bão hòa không thể hòa tan thêm chất tan đó nữa. "
            r"Tốc độ hòa tan của chất rắn trong nước tăng lên khi khuấy trộn, đun nóng hoặc nghiền nhỏ chất rắn; trong khi độ tan ($S$) và nồng độ phần trăm ($C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\%$) cho biết định lượng khả năng hòa tan và hàm lượng chất tan trong dung dịch."
        ),
        objectives=[
            r"Nêu được khái niệm dung dịch, chất tan, dung môi và xác định đúng chất tan, dung môi trong các dung dịch thực tế (như nước muối $\text{NaCl}$, nước đường, nước khoáng có gas).",
            r"Phân biệt được dung dịch bão hòa và dung dịch chưa bão hòa ở một nhiệt độ xác định.",
            r"Trình bày và giải thích được 3 biện pháp làm tăng tốc độ hòa tan của chất rắn trong nước: khuấy trộn, đun nóng dung dịch và nghiền nhỏ chất rắn.",
            r"Vận dụng được công thức tính khối lượng dung dịch ($m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}}$), nồng độ phần trăm ($C\%$) và độ tan ($S$) để giải bài toán pha chế dung dịch.",
        ],
        formulas=[
            {
                "name": "Khối lượng dung dịch",
                "formula": r"$m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}}$",
                "note": r"$m_{\text{dd}}$ là khối lượng dung dịch ($\text{g}$), $m_{\text{ct}}$ là khối lượng chất tan ($\text{g}$), $m_{\text{dm}}$ là khối lượng dung môi ($\text{g}$).",
            },
            {
                "name": "Phần trăm khối lượng chất tan trong dung dịch (Nồng độ phần trăm)",
                "formula": r"$C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\% = \dfrac{m_{\text{ct}}}{m_{\text{ct}} + m_{\text{dm}}} \cdot 100\%$",
                "note": r"Cho biết số gam chất tan có trong $100\text{ g}$ dung dịch.",
            },
            {
                "name": "Độ tan của một chất trong nước",
                "formula": r"$S = \dfrac{m_{\text{ct (max)}}}{m_{\text{H}_2\text{O}}} \cdot 100$",
                "note": r"$S$ là số gam chất tan hòa tan tối đa trong $100\text{ g}$ nước ($\text{H}_2\text{O}$) để tạo thành dung dịch bão hòa ở nhiệt độ xác định.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Dung dịch, chất tan và dung môi",
                "content": (
                    r"- **Dung dịch** là hỗn hợp đồng nhất của **dung môi** và **chất tan**." "\n"
                    r"- **Dung môi** là chất có khả năng hòa tan chất khác để tạo thành dung dịch (thường là chất lỏng có lượng nhiều hơn, phổ biến nhất là nước $\text{H}_2\text{O}$; ngoài ra còn có dung môi hữu cơ như ethanol $\text{C}_2\text{H}_5\text{OH}$, acetone để hòa tan sơn móng tay, xăng để hòa tan dầu mỡ)." "\n"
                    r"- **Chất tan** là chất bị hòa tan trong dung môi. Chất tan có thể ở thể rắn (muối sodium chloride $\text{NaCl}$, đường saccharose $\text{C}_{12}\text{H}_{22}\text{O}_{11}$, copper(II) sulfate $\text{CuSO}_4$), thể lỏng (ethanol $\text{C}_2\text{H}_5\text{OH}$, acetic acid $\text{CH}_3\text{COOH}$ trong giấm ăn) hoặc thể khí (khí carbon dioxide $\text{CO}_2$ trong nước ngọt có gas, khí oxygen $\text{O}_2$ hòa tan trong nước)." "\n"
                    r"- Ở một nhiệt độ và lượng dung môi xác định:" "\n"
                    r"  + **Dung dịch chưa bão hòa**: Là dung dịch vẫn có thể hòa tan thêm chất tan." "\n"
                    r"  + **Dung dịch bão hòa**: Là dung dịch đã chứa lượng chất tan tối đa, không thể hòa tan thêm chất tan đó nữa (nếu cho thêm chất tan vào thì phần thêm vào sẽ không tan và lắng xuống đáy)."
                ),
            },
            {
                "title": "2. Các yếu tố ảnh hưởng đến tốc độ hòa tan và độ tan",
                "content": (
                    r"- **3 biện pháp làm chất rắn tan nhanh hơn trong nước (tăng tốc độ hòa tan)**:" "\n"
                    r"  1. **Nghiền nhỏ chất rắn**: Làm tăng diện tích bề mặt tiếp xúc giữa các hạt chất rắn với các phân tử nước ($\text{H}_2\text{O}$)." "\n"
                    r"  2. **Khuấy trộn dung dịch**: Tạo sự tiếp xúc liên tục giữa chất rắn và các phân tử dung môi chưa bão hòa." "\n"
                    r"  3. **Đun nóng dung dịch**: Ở nhiệt độ cao, các phân tử nước và hạt chất tan chuyển động nhiệt nhanh hơn, va chạm mạnh hơn nên quá trình hòa tan diễn ra nhanh hơn." "\n"
                    r"- **Độ tan ($S$) và sự phụ thuộc vào nhiệt độ, áp suất**:" "\n"
                    r"  + Với hầu hết các **chất rắn** (như đường saccharose, potassium nitrate $\text{KNO}_3$, copper(II) sulfate $\text{CuSO}_4$): độ tan **tăng** khi nhiệt độ **tăng**." "\n"
                    r"  + Với các **chất khí** (như $\text{O}_2$, $\text{CO}_2$): độ tan **tăng** khi nhiệt độ **giảm** và áp suất **tăng** (ví dụ: khi mở nắp lon nước ngọt có gas ở nhiệt độ cao, áp suất giảm và nhiệt độ cao làm độ tan của khí $\text{CO}_2$ giảm mạnh nên bọt khí $\text{CO}_2\uparrow$ thoát ra sủi bọt)."
                ),
            },
            {
                "title": "3. Tính toán khối lượng dung dịch và phần trăm khối lượng chất tan",
                "content": (
                    r"- Khi hòa tan hoàn toàn $m_{\text{ct}}$ ($\text{g}$) chất tan vào $m_{\text{dm}}$ ($\text{g}$) dung môi nước ($\text{H}_2\text{O}$, với $D_{\text{H}_2\text{O}} = 1\text{ g/mL}$ nên $V\text{ mL}$ nước có khối lượng đúng bằng $V\text{ g}$), khối lượng dung dịch thu được là:" "\n"
                    r"$$m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}}$$" "\n"
                    r"- Tỉ số phần trăm khối lượng của chất tan so với khối lượng dung dịch gọi là **nồng độ phần trăm** ($C\%$):" "\n"
                    r"$$C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\%$$"
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Tính phần trăm khối lượng chất tan trong dung dịch",
                "problem": (
                    r"Hòa tan hoàn toàn $30\text{ g}$ đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) vào $170\text{ g}$ nước ($\text{H}_2\text{O}$). "
                    r"Xác định chất tan, dung môi, khối lượng dung dịch và tính nồng độ phần trăm ($C\%$) của dung dịch nước đường thu được."
                ),
                "solution": (
                    r"- **Chất tan**: đường saccharose ($m_{\text{ct}} = 30\text{ g}$); **Dung môi**: nước $\text{H}_2\text{O}$ ($m_{\text{dm}} = 170\text{ g}$)." "\n"
                    r"- **Khối lượng dung dịch** nước đường là:" "\n"
                    r"$$m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}} = 30 + 170 = 200\text{ g}$$" "\n"
                    r"- **Phần trăm khối lượng chất tan (nồng độ phần trăm)** là:" "\n"
                    r"$$C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\% = \dfrac{30}{200} \cdot 100\% = 15\%$$"
                ),
            },
            {
                "title": "Ví dụ 2: Kiểm tra dung dịch bão hòa hay chưa bão hòa qua độ tan",
                "problem": (
                    r"Ở $25^\circ\text{C}$, độ tan của muối sodium chloride ($\text{NaCl}$) trong nước là $S = 36\text{ g}/100\text{ g }\text{H}_2\text{O}$. "
                    r"Nếu cho $20\text{ g}$ muối $\text{NaCl}$ vào $50\text{ g}$ nước ở $25^\circ\text{C}$ và khuấy kỹ thì muối có tan hết không? Khối lượng dung dịch thu được là bao nhiêu?"
                ),
                "solution": (
                    r"- Theo định nghĩa độ tan $S = 36\text{ g}/100\text{ g }\text{H}_2\text{O}$: ở $25^\circ\text{C}$, cứ $100\text{ g}$ nước hòa tan tối đa được $36\text{ g}$ $\text{NaCl}$." "\n"
                    r"- Vậy $50\text{ g}$ nước chỉ hòa tan tối đa được:" "\n"
                    r"$$m_{\text{NaCl (tan tối đa)}} = \dfrac{50 \cdot 36}{100} = 18\text{ g}$$" "\n"
                    r"- Vì cho vào $20\text{ g} > 18\text{ g}$ nên muối **không tan hết**: thu được dung dịch $\text{NaCl}$ bão hòa và còn $20 - 18 = 2\text{ g}$ muối $\text{NaCl}$ rắn không tan lắng ở đáy cốc." "\n"
                    r"- Khối lượng dung dịch bão hòa thu được (chỉ tính phần đã tan) là: $m_{\text{dd}} = 50 + 18 = 68\text{ g}$."
                ),
            },
        ],
        key_takeaways=[
            r"Dung dịch là hỗn hợp đồng nhất của dung môi và chất tan; dung dịch bão hòa không thể hòa tan thêm chất tan ở nhiệt độ đang xét.",
            r"Muốn chất rắn tan nhanh hơn trong nước cần nghiền nhỏ, khuấy đều và đun nóng dung dịch.",
            r"Khối lượng dung dịch $m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}}$ (chỉ tính lượng chất tan thực tế đã tan) và nồng độ phần trăm $C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\%$.",
        ],
        questions=[
            mcq(
                r"Khi hòa tan một thìa muối ăn sodium chloride ($\text{NaCl}$) vào một cốc nước ($\text{H}_2\text{O}$) được hỗn hợp trong suốt, đâu là chất tan và đâu là dung môi?",
                [
                    r"Sodium chloride ($\text{NaCl}$) là chất tan, nước ($\text{H}_2\text{O}$) là dung môi.",
                    r"Nước ($\text{H}_2\text{O}$) là chất tan, sodium chloride ($\text{NaCl}$) là dung môi.",
                    r"Cả sodium chloride ($\text{NaCl}$) và nước ($\text{H}_2\text{O}$) đều là dung môi.",
                    r"Dung dịch nước muối là chất tan, nước ($\text{H}_2\text{O}$) là dung môi.",
                ],
                "A",
                "biet",
                r"Trong dung dịch nước muối, muối ăn sodium chloride ($\text{NaCl}$) bị hòa tan nên là chất tan, còn nước ($\text{H}_2\text{O}$) là môi trường hòa tan nên là dung môi.",
            ),
            mcq(
                r"Ở một nhiệt độ xác định, dung dịch **không thể** hòa tan thêm chất tan được nữa gọi là:",
                [
                    r"Nhũ tương.",
                    r"Dung dịch bão hòa.",
                    r"Dung dịch chưa bão hòa.",
                    r"Huyền phù.",
                ],
                "B",
                "biet",
                r"Dung dịch bão hòa là dung dịch không thể hòa tan thêm chất tan ở một nhiệt độ xác định.",
            ),
            mcq(
                r"Biện pháp nào sau đây **không** làm tăng tốc độ hòa tan của đường phèn (rắn) vào trong nước ($\text{H}_2\text{O}$)?",
                [
                    r"Dùng thìa khuấy đều liên tục sau khi cho đường vào nước.",
                    r"Dùng nước nóng ở $70^\circ\text{C}$ để pha đường.",
                    r"Dùng nước đá lạnh ở $0^\circ\text{C}$ thay cho nước ấm và để yên cốc nước.",
                    r"Đập nhỏ viên đường phèn thành dạng hạt mịn trước khi cho vào nước.",
                ],
                "C",
                "biet",
                r"Dùng nước đá lạnh và để yên làm các hạt chuyển động chậm và giảm tiếp xúc mới giữa đường với nước, khiến tốc độ hòa tan giảm đi. Đập nhỏ, khuấy đều và dùng nước nóng đều làm tăng tốc độ hòa tan.",
            ),
            mcq(
                r"Khi tăng nhiệt độ của nước ($\text{H}_2\text{O}$), độ tan của hầu hết các chất rắn (như đường saccharose) và độ tan của các chất khí (như $\text{O}_2$, $\text{CO}_2$) thay đổi như thế nào?",
                [
                    r"Độ tan của cả chất rắn và chất khí đều tăng.",
                    r"Độ tan của hầu hết chất rắn giảm, còn độ tan của chất khí tăng.",
                    r"Độ tan của cả chất rắn và chất khí đều không thay đổi theo nhiệt độ.",
                    r"Độ tan của hầu hết chất rắn tăng, còn độ tan của chất khí giảm.",
                ],
                "D",
                "biet",
                r"Khi tăng nhiệt độ, hầu hết các chất rắn tan được nhiều hơn (độ tan tăng), ngược lại các chất khí ($\text{O}_2$, $\text{CO}_2$) thoát ra khỏi nước dễ hơn nên độ tan giảm.",
            ),
            mcq(
                r"Vì sao vào những ngày mùa hè nắng nóng, cá trong các ao hồ cạn thường phải ngoi lên mặt nước để đớp không khí nhiều hơn so với mùa mát?",
                [
                    r"Vì khi nhiệt độ nước tăng cao, độ tan của khí oxygen ($\text{O}_2$) trong nước giảm xuống làm nước ao bị thiếu $\text{O}_2$.",
                    r"Vì mùa hè áp suất khí quyển tăng gấp đôi làm khí nitrogen ($\text{N}_2$) tan quá nhiều.",
                    r"Vì ở nhiệt độ cao, nước ($\text{H}_2\text{O}$) biến đổi thành nhũ tương không có $\text{O}_2$.",
                    r"Vì độ tan của khí oxygen ($\text{O}_2$) trong nước chỉ phụ thuộc vào việc khuấy trộn chứ không phụ thuộc nhiệt độ.",
                ],
                "A",
                "hieu",
                r"Độ tan của chất khí ($\text{O}_2$) trong nước giảm khi nhiệt độ tăng. Vào mùa hè nắng nóng, nhiệt độ nước ao tăng cao khiến lượng $\text{O}_2$ hòa tan trong nước giảm mạnh, cá bị thiếu dưỡng khí nên phải ngoi lên mặt nước để hô hấp.",
            ),
            mcq(
                r"Một học sinh hòa tan hoàn toàn $15\text{ g}$ muối sodium chloride ($\text{NaCl}$) vào $135\text{ g}$ nước ($\text{H}_2\text{O}$). Nồng độ phần trăm ($C\%$) của dung dịch muối thu được là:",
                [
                    r"$9\%$.",
                    r"$10\%$.",
                    r"$11{,}11\%$.",
                    r"$15\%$.",
                ],
                "B",
                "hieu",
                r"Khối lượng dung dịch là: $m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}} = 15 + 135 = 150\text{ g}$. Nồng độ phần trăm của dung dịch là: $C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\% = \dfrac{15}{150} \cdot 100\% = 10\%$.",
            ),
            tf4(
                r"Trong phòng thí nghiệm, một học sinh tiến hành khảo sát sự hòa tan của muối copper(II) sulfate ($\text{CuSO}_4$, tinh thể màu xanh) trong nước ($\text{H}_2\text{O}$) ở $20^\circ\text{C}$. Biết ở $20^\circ\text{C}$, cứ $100\text{ g}$ nước hòa tan tối đa được $20{,}7\text{ g}$ $\text{CuSO}_4$. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Nếu hòa tan $10\text{ g}$ $\text{CuSO}_4$ vào $100\text{ g}$ nước ở $20^\circ\text{C}$ thì thu được một dung dịch chưa bão hòa có màu xanh đồng nhất.",
                    r"Để $10\text{ g}$ tinh thể $\text{CuSO}_4$ tan nhanh hơn trong $100\text{ g}$ nước, học sinh nên nghiền mịn tinh thể và dùng đũa thủy tinh khuấy đều.",
                    r"Nếu cho $25\text{ g}$ $\text{CuSO}_4$ vào $100\text{ g}$ nước ở $20^\circ\text{C}$ và khuấy kỹ thì toàn bộ $25\text{ g}$ $\text{CuSO}_4$ đều tan hết tạo thành $125\text{ g}$ dung dịch.",
                    r"Khi đun nóng cốc chứa $25\text{ g}$ $\text{CuSO}_4$ và $100\text{ g}$ nước từ $20^\circ\text{C}$ lên $60^\circ\text{C}$, phần $\text{CuSO}_4$ rắn chưa tan ở đáy cốc sẽ tan thêm vào nước.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Vì $10\text{ g} < 20{,}7\text{ g}$ nên $\text{CuSO}_4$ tan hết và dung dịch vẫn có thể hòa tan thêm $10{,}7\text{ g}$ $\text{CuSO}_4$ nữa, tức là dung dịch chưa bão hòa." "\n"
                    r"- **Ý b) Đúng**: Nghiền mịn chất rắn và khuấy đều là hai biện pháp trực tiếp làm tăng tốc độ hòa tan của chất rắn trong nước." "\n"
                    r"- **Ý c) Sai**: Ở $20^\circ\text{C}$, $100\text{ g}$ nước chỉ hòa tan tối đa $20{,}7\text{ g}$ $\text{CuSO}_4$ tạo ra $100 + 20{,}7 = 120{,}7\text{ g}$ dung dịch bão hòa, còn lại $25 - 20{,}7 = 4{,}3\text{ g}$ $\text{CuSO}_4$ rắn không tan lắng ở đáy cốc." "\n"
                    r"- **Ý d) Đúng**: Khi tăng nhiệt độ từ $20^\circ\text{C}$ lên $60^\circ\text{C}$, độ tan của $\text{CuSO}_4$ trong nước tăng mạnh nên phần $\text{CuSO}_4$ rắn ở đáy sẽ tan thêm vào dung dịch."
                ),
            ),
            tf4(
                r"Xét các ứng dụng thực tế về dung môi, chất tan và sự hòa tan trong đời sống hằng ngày. Các nhận định dưới đây là đúng hay sai?",
                [
                    r"Khi quần áo bị dính vết dầu mỡ hoặc nhựa sơn (không tan trong nước), người ta có thể dùng xăng hoặc acetone làm dung môi để tẩy sạch vết bẩn.",
                    r"Trong chai nước ngọt có gas đóng kín ở áp suất cao, khí carbon dioxide ($\text{CO}_2$) đóng vai trò là dung môi, còn nước ($\text{H}_2\text{O}$) là chất tan.",
                    r"Khi mở nắp chai nước ngọt có gas đã ướp lạnh so với chai nước ngọt để ngoài trời nắng nóng, chai để ngoài nắng nóng sẽ sủi bọt khí $\text{CO}_2\uparrow$ mạnh hơn nhiều.",
                    r"Để pha chế $500\text{ g}$ dung dịch nước muối sinh lý có nồng độ $C\% = 0{,}9\%$, ta cần cân đúng $4{,}5\text{ g}$ muối $\text{NaCl}$ tinh khiết hòa tan vào $495{,}5\text{ g}$ nước cất.",
                ],
                "Đ/S/Đ/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Dầu mỡ và sơn không tan trong nước nhưng tan tốt trong các dung môi hữu cơ như xăng hoặc acetone." "\n"
                    r"- **Ý b) Sai**: Trong nước ngọt có gas, nước ($\text{H}_2\text{O}$) là **dung môi**, còn đường và khí carbon dioxide ($\text{CO}_2$) là các **chất tan**." "\n"
                    r"- **Ý c) Đúng**: Ở nhiệt độ cao (ngoài trời nắng), độ tan của khí $\text{CO}_2$ trong nước giảm mạnh nên khi mở nắp (giảm áp suất), khí $\text{CO}_2$ thoát ra mãnh liệt hơn." "\n"
                    r"- **Ý d) Đúng**: Ta có $m_{\text{NaCl}} = \dfrac{500 \cdot 0{,}9}{100} = 4{,}5\text{ g}$ và $m_{\text{H}_2\text{O}} = 500 - 4{,}5 = 495{,}5\text{ g}$."
                ),
            ),
            mcq(
                r"Để pha chế $300\text{ g}$ dung dịch nước đường có nồng độ $C\% = 20\%$ dùng làm siro thực phẩm, khối lượng đường saccharose ($m_{\text{ct}}$) và khối lượng nước cất ($m_{\text{H}_2\text{O}}$) cần lấy lần lượt là:",
                [
                    r"$60\text{ g}$ đường và $300\text{ g}$ nước.",
                    r"$50\text{ g}$ đường và $250\text{ g}$ nước.",
                    r"$60\text{ g}$ đường và $240\text{ g}$ nước.",
                    r"$20\text{ g}$ đường và $280\text{ g}$ nước.",
                ],
                "C",
                "vandung",
                r"Khối lượng đường chất tan cần lấy là: $m_{\text{ct}} = \dfrac{m_{\text{dd}} \cdot C\%}{100\%} = \dfrac{300 \cdot 20}{100} = 60\text{ g}$. Khối lượng nước dung môi cần lấy là: $m_{\text{H}_2\text{O}} = m_{\text{dd}} - m_{\text{ct}} = 300 - 60 = 240\text{ g}$.",
            ),
            short(
                r"Hòa tan hoàn toàn $40\text{ g}$ muối sodium chloride ($\text{NaCl}$) vào $160\text{ g}$ nước ($\text{H}_2\text{O}$) ở nhiệt độ phòng để thu được một dung dịch đồng nhất. Hãy tính phần trăm khối lượng chất tan (nồng độ phần trăm $C\%$) của dung dịch muối thu được theo đơn vị phần trăm ($\%$).",
                ["20", "20,0", "20.0"],
                "vandung",
                (
                    r"Khối lượng dung dịch nước muối thu được là:" "\n"
                    r"$$m_{\text{dd}} = m_{\text{ct}} + m_{\text{dm}} = 40 + 160 = 200\text{ g}$$" "\n"
                    r"Nồng độ phần trăm ($C\%$) của dung dịch là:" "\n"
                    r"$$C\% = \dfrac{m_{\text{ct}}}{m_{\text{dd}}} \cdot 100\% = \dfrac{40}{200} \cdot 100\% = 20\%$$"
                ),
            ),
        ],
        description="Khái niệm dung dịch, dung môi, chất tan, dung dịch bão hòa và chưa bão hòa, các yếu tố ảnh hưởng đến tốc độ hòa tan, độ tan và phần trăm khối lượng chất tan.",
    ),
    lesson(
        grade=6,
        order=6,
        code="H6-C06",
        title="Chương 6: Biến đổi vật lý và biến đổi hóa học",
        topic="bien-doi-vat-ly",
        summary=(
            r"Trong tự nhiên và đời sống, các chất luôn trải qua những sự biến đổi đa dạng. "
            r"Biến đổi vật lý (hiện tượng vật lý) là sự biến đổi mà chất chỉ thay đổi về trạng thái, hình dạng, kích thước hoặc hòa tan/cô cạn mà không tạo thành chất mới. "
            r"Biến đổi hóa học (hiện tượng hóa học) là sự biến đổi có tạo thành chất mới với những tính chất hoàn toàn khác chất ban đầu, thường nhận biết qua dấu hiệu đổi màu, sủi bọt khí ($\uparrow$), tạo kết tủa ($\downarrow$) hoặc tỏa nhiệt, phát sáng."
        ),
        objectives=[
            r"Nêu được khái niệm và lấy được ví dụ thực tế về sự biến đổi vật lý (chuyển thể, nghiền nhỏ, hòa tan, kéo sợi, uốn cong kim loại).",
            r"Nêu được khái niệm và lấy được ví dụ thực tế về sự biến đổi hóa học (đốt cháy nhiên liệu, đun đường hóa than, sắt bị gỉ, nung hỗn hợp iron $\text{Fe}$ và sulfur $\text{S}$).",
            r"Nhận biết được 4 dấu hiệu đặc trưng cho biết đã có biến đổi hóa học xảy ra: thay đổi màu sắc, xuất hiện bọt khí ($\uparrow$), xuất hiện kết tủa ($\downarrow$), tỏa nhiệt và phát sáng.",
            r"Phân tích được các quá trình nhiều giai đoạn trong đời sống (như thắp nến, nung vôi, nấu ăn) để chỉ rõ giai đoạn nào là biến đổi vật lý, giai đoạn nào là biến đổi hóa học.",
        ],
        formulas=[
            {
                "name": "Phản ứng hóa học giữa iron và sulfur khi đun nóng",
                "formula": r"$\text{Fe} + \text{S} \xrightarrow{t^\circ} \text{FeS}$",
                "note": r"Trộn bột $\text{Fe}$ và $\text{S}$ ở nhiệt độ thường là biến đổi vật lý (còn từ tính); đun nóng tạo chất mới iron(II) sulfide ($\text{FeS}$ màu xám đen, không bị nam châm hút) là biến đổi hóa học.",
            },
            {
                "name": "Phản ứng nhiệt phân đường saccharose (thắng đường hóa than)",
                "formula": r"$\text{C}_{12}\text{H}_{22}\text{O}_{11} \xrightarrow{t^\circ} 12\text{C} + 11\text{H}_2\text{O}\uparrow$",
                "note": r"Đường trắng vị ngọt chuyển thành than đen ($\text{C}$) vị đắng và hơi nước ($\text{H}_2\text{O}$) — có sự tạo thành chất mới.",
            },
            {
                "name": "Tiêu chí phân biệt cốt lõi",
                "formula": r"$\text{Biến đổi vật lý: Không tạo chất mới} \quad \neq \quad \text{Biến đổi hóa học: Có tạo thành chất mới}$",
                "note": r"Dấu hiệu nhận biết chất mới: đổi màu sắc, sủi bọt khí ($\uparrow$), xuất hiện kết tủa ($\downarrow$), tỏa nhiệt và phát sáng.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Sự biến đổi vật lý (Hiện tượng vật lý)",
                "content": (
                    r"- **Khái niệm**: Biến đổi vật lý là hiện tượng chất có sự biến đổi về **trạng thái (thể), hình dạng, kích thước** hoặc sự hòa tan, cô cạn... nhưng **không có sự tạo thành chất mới** (bản chất phân tử của chất được giữ nguyên)." "\n"
                    r"- **Các dạng biến đổi vật lý thường gặp**:" "\n"
                    r"  + Sự chuyển thể của chất: Nước đá ($\text{H}_2\text{O}$ rắn) nóng chảy thành nước lỏng, nước lỏng sôi thành hơi nước ($\text{H}_2\text{O}$ khí); đúc đồng, làm kem." "\n"
                    r"  + Sự thay đổi hình dạng, kích thước: Xé tờ giấy thành nhiều mảnh nhỏ, đập nhỏ viên đá vôi ($\text{CaCO}_3$), kéo kim loại copper ($\text{Cu}$) thành sợi dây mảnh, vo gạo, thái rau." "\n"
                    r"  + Sự hòa tan và kết tinh: Hòa tan muối ăn ($\text{NaCl}$) hoặc đường vào nước; cô cạn nước biển để thu muối kết tinh."
                ),
            },
            {
                "title": "2. Sự biến đổi hóa học (Hiện tượng hóa học)",
                "content": (
                    r"- **Khái niệm**: Biến đổi hóa học là hiện tượng chất bị biến đổi và **có sự tạo thành chất mới** (chất mới có tính chất vật lý và hóa học khác hẳn chất ban đầu)." "\n"
                    r"- **Các dấu hiệu nhận biết có biến đổi hóa học xảy ra**:" "\n"
                    r"  1. **Sự thay đổi màu sắc** và mùi vị: Đun nóng đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) màu trắng, vị ngọt quá nhiệt độ nóng chảy sẽ biến thành chất rắn màu đen là than ($\text{C}$), vị đắng và có mùi khét; đinh iron ($\text{Fe}$) màu xám trắng để lâu trong không khí ẩm chuyển thành gỉ sắt màu nâu đỏ." "\n"
                    r"  2. **Sự xuất hiện chất khí (sủi bọt khí $\uparrow$)**: Cho viên sủi vitamin C vào nước hoặc nhỏ giấm ăn (acetic acid $\text{CH}_3\text{COOH}$) vào vỏ trứng / đá vôi ($\text{CaCO}_3$) thấy sủi bọt khí carbon dioxide ($\text{CO}_2\uparrow$)." "\n"
                    r"  3. **Sự xuất hiện chất kết tủa ($\downarrow$ - chất rắn không tan)**: Thổi hơi thở chứa khí $\text{CO}_2$ vào cốc nước vôi trong ($\text{Ca(OH)}_2$) thấy dung dịch bị vẩn đục do tạo thành kết tủa trắng calcium carbonate ($\text{CaCO}_3\downarrow$)." "\n"
                    r"  4. **Sự tỏa nhiệt và phát sáng**: Đốt cháy dải kim loại magnesium ($\text{Mg}$) trong không khí tạo ngọn lửa sáng chói mắt và bột màu trắng magnesium oxide ($\text{MgO}$); đốt cháy khí gas ($\text{CH}_4$, $\text{C}_3\text{H}_8$) hoặc củi."
                ),
            },
            {
                "title": "3. Phân tích thí nghiệm trộn và nung bột iron với bột sulfur",
                "content": (
                    r"- **Giai đoạn 1 (Trộn đều ở nhiệt độ thường)**: Trộn bột iron ($\text{Fe}$ màu xám, bị nam châm hút) với bột sulfur ($\text{S}$ màu vàng, không bị nam châm hút). Đưa nam châm lại gần, nam châm vẫn hút tách được bột $\text{Fe}$ ra khỏi hỗn hợp $\rightarrow$ không có chất mới tạo thành $\rightarrow$ đây là **biến đổi vật lý**." "\n"
                    r"- **Giai đoạn 2 (Đun nóng mạnh hỗn hợp)**: Hỗn hợp nóng đỏ rực và chuyển thành khối chất rắn màu xám đen là hợp chất **iron(II) sulfide** ($\text{FeS}$). Khi để nguội và đưa nam châm lại gần, chất rắn $\text{FeS}$ **không còn bị nam châm hút** nữa $\rightarrow$ đã có chất mới tạo thành $\rightarrow$ đây là **biến đổi hóa học**."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Phân tích các giai đoạn khi đốt một cây nến",
                "problem": (
                    r"Khi thắp sáng một cây nến paraffin, có 3 quá trình diễn ra nối tiếp nhau: "
                    r"(1) Sáp nến rắn quanh chân bấc nóng chảy thành sáp lỏng; "
                    r"(2) Sáp lỏng thấm theo sợi bấc lên trên rồi hóa hơi thành hơi paraffin; "
                    r"(3) Hơi paraffin tác dụng với khí oxygen ($\text{O}_2$) trong không khí cháy tạo thành khí carbon dioxide ($\text{CO}_2$), hơi nước ($\text{H}_2\text{O}$), tỏa nhiệt và phát sáng. "
                    r"Hãy xác định quá trình nào là biến đổi vật lý, quá trình nào là biến đổi hóa học."
                ),
                "solution": (
                    r"- **Quá trình (1) và (2)** là **biến đổi vật lý** vì paraffin chỉ chuyển từ thể rắn sang thể lỏng rồi sang thể hơi, chưa tạo ra chất mới." "\n"
                    r"- **Quá trình (3)** là **biến đổi hóa học** vì hơi paraffin đã phản ứng với $\text{O}_2$ tạo thành các chất hoàn toàn mới là khí $\text{CO}_2$ và hơi nước $\text{H}_2\text{O}$, kèm theo tỏa nhiệt và phát sáng."
                ),
            },
            {
                "title": "Ví dụ 2: Tính khối lượng chất tham gia biến đổi hóa học",
                "problem": (
                    r"Một học sinh trộn đều $10\text{ g}$ bột iron ($\text{Fe}$) với $4\text{ g}$ bột sulfur ($\text{S}$) rồi đun nóng trong ống nghiệm kín. "
                    r"Sau khi phản ứng dừng lại và để nguội, học sinh nghiền nhỏ hỗn hợp rồi dùng thanh nam châm hút kỹ toàn bộ phần bột $\text{Fe}$ còn dư chưa phản ứng thì thu được $3\text{ g}$ $\text{Fe}$ bị nam châm hút. "
                    r"Tính khối lượng iron ($\text{Fe}$) đã thực sự tham gia vào sự biến đổi hóa học tạo thành $\text{FeS}$."
                ),
                "solution": (
                    r"- Phần bột iron ($\text{Fe}$) còn dư không biến đổi hóa học vẫn giữ nguyên tính chất vật lý bị nam châm hút với khối lượng $m_{\text{Fe dư}} = 3\text{ g}$." "\n"
                    r"- Khối lượng iron ($\text{Fe}$) đã tham gia biến đổi hóa học tạo thành hợp chất mới $\text{FeS}$ (không bị nam châm hút) là:" "\n"
                    r"$$m_{\text{Fe phản ứng}} = 10 - 3 = 7\text{ g}$$"
                ),
            },
        ],
        key_takeaways=[
            r"Dấu hiệu cốt lõi để phân biệt biến đổi hóa học với biến đổi vật lý là có sự tạo thành chất mới hay không.",
            r"Mọi quá trình chuyển thể (nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ, thăng hoa) và hòa tan vật lý đều là biến đổi vật lý.",
            r"Sự cháy, sự gỉ sét của kim loại, sự lên men, sự quang hợp, sự phân hủy bởi nhiệt tạo chất mới đều là biến đổi hóa học.",
        ],
        questions=[
            mcq(
                r"Hiện tượng nào sau đây là một **biến đổi vật lý**?",
                [
                    r"Đốt cháy khí methane ($\text{CH}_4$) trong bếp gas tạo ra khí $\text{CO}_2$ và hơi nước $\text{H}_2\text{O}$.",
                    r"Đinh iron ($\text{Fe}$) để ngoài mưa nắng lâu ngày bị phủ một lớp gỉ màu nâu đỏ.",
                    r"Cơm để lâu ngày ngoài không khí nóng ẩm bị ôi thiu và có vị chua.",
                    r"Hòa tan muối ăn sodium chloride ($\text{NaCl}$) vào nước được dung dịch nước muối.",
                ],
                "D",
                "biet",
                r"Hòa tan muối ăn ($\text{NaCl}$) vào nước chỉ tạo hỗn hợp đồng nhất, khi cô cạn nước bay hơi ta thu lại được đúng muối $\text{NaCl}$ ban đầu, không có chất mới tạo thành nên là biến đổi vật lý. Ba hiện tượng còn lại đều tạo ra chất mới nên là biến đổi hóa học.",
            ),
            mcq(
                r"Hiện tượng nào sau đây là một **biến đổi hóa học**?",
                [
                    r"Đun nóng đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) đến khi chuyển thành chất rắn màu đen là than ($\text{C}$) và có mùi khét.",
                    r"Dây tóc bóng đèn bằng kim loại tungsten ($\text{W}$) nóng sáng lên khi có dòng điện chạy qua rồi trở lại như cũ khi ngắt điện.",
                    r"Nước lỏng ($\text{H}_2\text{O}$) trong khay tủ lạnh đông đặc thành các viên nước đá ở $0^\circ\text{C}$.",
                    r"Nghiền nhỏ viên phấn viết bảng thành bụi phấn mịn.",
                ],
                "A",
                "biet",
                r"Đun đường hóa than đen ($\text{C}$) và hơi nước ($\text{H}_2\text{O}$) có sự tạo thành chất mới (màu đen, vị đắng, không tan trong nước), nên là biến đổi hóa học.",
            ),
            mcq(
                r"Dấu hiệu chính giúp nhận biết đã có sự biến đổi hóa học xảy ra khi thổi hơi thở (chứa khí $\text{CO}_2$) vào cốc nước vôi trong ($\text{Ca(OH)}_2$) là:",
                [
                    r"Thể tích nước trong cốc tăng lên gấp đôi.",
                    r"Dung dịch nước vôi trong bị vẩn đục do xuất hiện chất kết tủa trắng calcium carbonate ($\text{CaCO}_3\downarrow$).",
                    r"Dung dịch nước vôi trong đông đặc thành băng ở $0^\circ\text{C}$.",
                    r"Cốc nước phát ra ánh sáng chói lòa như pháo hoa.",
                ],
                "B",
                "biet",
                r"Khí carbon dioxide ($\text{CO}_2$) tác dụng với dung dịch calcium hydroxide ($\text{Ca(OH)}_2$) tạo thành chất rắn không tan màu trắng là calcium carbonate ($\text{CaCO}_3\downarrow$) làm nước vôi trong bị vẩn đục.",
            ),
            mcq(
                r"Tiêu chí quan trọng nhất để phân biệt biến đổi hóa học với biến đổi vật lý là:",
                [
                    r"Có cần đun nóng bằng đèn cồn hay không.",
                    r"Có sự chuyển từ thể rắn sang thể lỏng hay không.",
                    r"Có sự tạo thành chất mới hay không.",
                    r"Có sự thay đổi thể tích của vật thể hay không.",
                ],
                "C",
                "biet",
                r"Bản chất của biến đổi hóa học là có sự tạo thành chất mới, còn biến đổi vật lý không tạo ra chất mới.",
            ),
            mcq(
                r"Cho quy trình sản xuất vôi sống thủ công gồm 2 công đoạn: Công đoạn 1: Đập nhỏ các tảng đá vôi lớn ($\text{CaCO}_3$) thành các viên đá nhỏ đều nhau; Công đoạn 2: Xếp đá vôi vào lò và nung ở khoảng $1000^\circ\text{C}$ thu được vôi sống ($\text{CaO}$) và khí carbon dioxide ($\text{CO}_2\uparrow$). Nhận xét nào sau đây đúng?",
                [
                    r"Công đoạn 1 là biến đổi hóa học, công đoạn 2 là biến đổi vật lý.",
                    r"Cả hai công đoạn 1 và 2 đều là biến đổi vật lý.",
                    r"Cả hai công đoạn 1 và 2 đều là biến đổi hóa học.",
                    r"Công đoạn 1 là biến đổi vật lý, công đoạn 2 là biến đổi hóa học.",
                ],
                "D",
                "hieu",
                r"Ở công đoạn 1, đá vôi ($\text{CaCO}_3$) chỉ thay đổi kích thước chứ không tạo chất mới $\rightarrow$ biến đổi vật lý. Ở công đoạn 2, $\text{CaCO}_3$ bị phân hủy thành chất mới là $\text{CaO}$ và khí $\text{CO}_2\uparrow$ $\rightarrow$ biến đổi hóa học.",
            ),
            mcq(
                r"Trong thí nghiệm đun nóng hỗn hợp bột iron ($\text{Fe}$) và bột sulfur ($\text{S}$), dấu hiệu thực nghiệm nào chứng minh phản ứng đã tạo ra chất mới là iron(II) sulfide ($\text{FeS}$)?",
                [
                    r"Sản phẩm thu được có màu xám đen và không còn bị thanh nam châm hút như bột iron ($\text{Fe}$) ban đầu.",
                    r"Sản phẩm thu được vẫn có màu vàng tươi của bột sulfur ($\text{S}$).",
                    r"Sản phẩm thu được bay hơi hoàn toàn thành chất khí không màu.",
                    r"Sản phẩm thu được bị nam châm hút mạnh gấp đôi bột iron ($\text{Fe}$) ban đầu.",
                ],
                "A",
                "hieu",
                r"Bột iron ($\text{Fe}$) ban đầu bị nam châm hút mạnh, nhưng sau khi đun nóng với sulfur ($\text{S}$) tạo thành hợp chất mới iron(II) sulfide ($\text{FeS}$) có màu xám đen và hoàn toàn không bị nam châm hút.",
            ),
            tf4(
                r"Một học sinh quan sát các hiện tượng xảy ra trong nhà bếp và tự nhiên hằng ngày. Xét tính đúng/sai của các phát biểu phân loại dưới đây:",
                [
                    r"Khi bật bếp từ để đun sôi một ấm nước tinh khiết ($\text{H}_2\text{O}$), quá trình nước chuyển thành hơi nước là một biến đổi vật lý.",
                    r"Khi vắt nước cốt chanh (chứa citric acid) vào cốc sữa bò tươi làm sữa kết tủa vón cục, hoặc nhỏ giấm ăn vào bột baking soda ($\text{NaHCO}_3$) thấy sủi bọt khí $\text{CO}_2\uparrow$, đó là các biến đổi hóa học.",
                    r"Quá trình lên men sữa tươi thành sữa chua (nhờ vi khuẩn chuyển hóa đường lactose thành lactic acid có vị chua) là một biến đổi vật lý.",
                    r"Khi đốt củi trong bếp lửa, củi cháy tỏa nhiều nhiệt, phát sáng và biến thành tro cùng khí $\text{CO}_2$, hơi nước $\text{H}_2\text{O}$ là một biến đổi hóa học.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Nước ($\text{H}_2\text{O}$) sôi chuyển từ thể lỏng sang thể hơi không tạo thành chất mới nên là biến đổi vật lý." "\n"
                    r"- **Ý b) Đúng**: Có dấu hiệu tạo kết tủa và sủi bọt khí ($\text{CO}_2\uparrow$) do tạo ra chất mới nên là biến đổi hóa học." "\n"
                    r"- **Ý c) Sai**: Lên men sữa chua tạo ra chất mới là lactic acid làm thay đổi vị và trạng thái của sữa nên là **biến đổi hóa học**." "\n"
                    r"- **Ý d) Đúng**: Sự cháy của củi tạo ra chất mới ($\text{CO}_2$, $\text{H}_2\text{O}$, tro), tỏa nhiệt và phát sáng nên là biến đổi hóa học."
                ),
            ),
            tf4(
                r"Trong một buổi thực hành, học sinh cho $10\text{ g}$ đường saccharose ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) màu trắng vào ống nghiệm khô rồi đun nóng trên ngọn lửa đèn cồn: lúc đầu đường nóng chảy thành chất lỏng không màu, tiếp tục đun thì chuyển sang màu vàng nâu (caramel) rồi cuối cùng biến thành khối xốp màu đen ($\text{C}$) và có những giọt nước ($\text{H}_2\text{O}$) đọng trên thành ống nghiệm. Xét tính đúng/sai của các nhận định sau:",
                [
                    r"Giai đoạn đầu khi đường rắn nóng chảy thành đường lỏng không màu là sự biến đổi vật lý.",
                    r"Giai đoạn đường chuyển thành khối than đen ($\text{C}$) và hơi nước ($\text{H}_2\text{O}$) là sự biến đổi hóa học vì có tạo thành các chất mới.",
                    r"Nếu lấy khối chất rắn màu đen ($\text{C}$) thu được ở cuối thí nghiệm hòa tan vào nước, ta sẽ thu lại được dung dịch nước đường có vị ngọt như ban đầu.",
                    r"Các dấu hiệu giúp nhận biết biến đổi hóa học trong thí nghiệm trên là sự thay đổi màu sắc (trắng $\rightarrow$ đen), mùi vị và xuất hiện hơi nước ngưng tụ.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Đường chỉ mới chuyển từ thể rắn sang thể lỏng, chưa phân hủy thành chất mới nên là biến đổi vật lý." "\n"
                    r"- **Ý b) Đúng**: Đường ($\text{C}_{12}\text{H}_{22}\text{O}_{11}$) đã bị phân hủy bởi nhiệt tạo thành hai chất mới là carbon ($\text{C}$) và nước ($\text{H}_2\text{O}$)." "\n"
                    r"- **Ý c) Sai**: Chất rắn màu đen là than ($\text{C}$) không tan trong nước và không còn vị ngọt, không thể hòa tan để thu lại đường ban đầu." "\n"
                    r"- **Ý d) Đúng**: Sự đổi màu từ trắng sang đen, xuất hiện mùi khét và giọt nước đọng trên thành ống là dấu hiệu trực quan của biến đổi hóa học."
                ),
            ),
            mcq(
                r"Cho các quá trình sau: (1) Hòa tan muối ăn ($\text{NaCl}$) vào nước; (2) Đốt cháy dây magnesium ($\text{Mg}$) trong không khí tạo bột trắng $\text{MgO}$; (3) Nước đá khô ($\text{CO}_2$ rắn) thăng hoa thành khí $\text{CO}_2$; (4) Nung đá vôi ($\text{CaCO}_3$) tạo vôi sống ($\text{CaO}$) và khí $\text{CO}_2$; (5) Uốn thanh iron ($\text{Fe}$) thành khung cửa; (6) Quả táo gọt vỏ để ngoài không khí bị thâm nâu do enzyme oxy hóa. Số quá trình thuộc loại **biến đổi hóa học** là:",
                [
                    r"$3$ quá trình: (1), (3), (5).",
                    r"$3$ quá trình: (2), (4), (6).",
                    r"$2$ quá trình: (2), (4).",
                    r"$4$ quá trình: (1), (2), (4), (6).",
                ],
                "B",
                "vandung",
                r"Các quá trình (1) hòa tan muối, (3) thăng hoa đá khô $\text{CO}_2$ và (5) uốn thanh $\text{Fe}$ không tạo chất mới nên là biến đổi vật lý. Các quá trình (2) đốt $\text{Mg}$ tạo $\text{MgO}$, (4) nung $\text{CaCO}_3$ tạo $\text{CaO} + \text{CO}_2$ và (6) táo bị oxy hóa đổi màu nâu đều tạo chất mới nên có $3$ quá trình là biến đổi hóa học.",
            ),
            short(
                r"Một học sinh trộn đều $14\text{ g}$ bột kim loại iron ($\text{Fe}$) với $8\text{ g}$ bột sulfur ($\text{S}$) rồi đun nóng mạnh để thực hiện phản ứng hóa học tạo thành iron(II) sulfide ($\text{FeS}$). Sau khi để nguội, học sinh dùng nam châm tách lấy toàn bộ lượng bột $\text{Fe}$ còn dư chưa bị biến đổi hóa học thì thu được $2{,}8\text{ g}$ $\text{Fe}$ (biết sulfur $\text{S}$ đã phản ứng vừa hết với phần $\text{Fe}$ biến đổi). Hãy tính phần trăm khối lượng của bột iron ($\text{Fe}$) đã tham gia vào sự biến đổi hóa học so với lượng $\text{Fe}$ ban đầu theo đơn vị phần trăm ($\%$).",
                ["80", "80,0", "80.0"],
                "vandung",
                (
                    r"Khối lượng bột iron ($\text{Fe}$) đã tham gia vào sự biến đổi hóa học tạo thành chất mới $\text{FeS}$ là:" "\n"
                    r"$$m_{\text{Fe phản ứng}} = 14 - 2{,}8 = 11{,}2\text{ g}$$" "\n"
                    r"Phần trăm khối lượng bột iron ($\text{Fe}$) đã tham gia biến đổi hóa học so với ban đầu là:" "\n"
                    r"$$\%m_{\text{Fe phản ứng}} = \dfrac{11{,}2}{14} \cdot 100\% = 80\%$$"
                ),
            ),
        ],
        description="Phân biệt biến đổi vật lý (không tạo chất mới) và biến đổi hóa học (có tạo thành chất mới) cùng các dấu hiệu nhận biết.",
    ),
    lesson(
        grade=6,
        order=7,
        code="H6-C07",
        title="Chương 7: Một số vật liệu, nhiên liệu, nguyên liệu và an toàn phòng thí nghiệm",
        topic="an-toan-hoa-hoc",
        summary=(
            r"Con người khai thác và sử dụng các vật liệu (kim loại, nhựa, thủy tinh, gốm, cao su), nhiên liệu (than đá, xăng dầu, khí biogas/LPG) và nguyên liệu tự nhiên (đá vôi $\text{CaCO}_3$, quặng bauxite, quặng sắt, cát thạch anh $\text{SiO}_2$) để phục vụ sản xuất và đời sống. "
            r"Việc sử dụng an toàn, tiết kiệm theo mô hình $3\text{R}$ (Reduce – Reuse – Recycle) gắn liền với phát triển bền vững, đồng thời khi làm việc trong phòng thí nghiệm hóa học phải tuân thủ nghiêm ngặt quy tắc an toàn và nhận biết đúng các biển báo nguy hiểm."
        ),
        objectives=[
            r"Trình bày được tính chất, ứng dụng và cách sử dụng an toàn, hiệu quả theo mô hình $3\text{R}$ đối với các vật liệu thông dụng: kim loại ($\text{Fe}$, $\text{Al}$, $\text{Cu}$), nhựa, thủy tinh, gốm sứ, cao su.",
            r"Phân loại được nhiên liệu rắn (than đá, củi), lỏng (xăng, dầu, ethanol $\text{C}_2\text{H}_5\text{OH}$), khí (biogas chứa $\text{CH}_4$, khí gas LPG) và nêu được cách sử dụng nhiên liệu an toàn, tiết kiệm.",
            r"Nêu được thành phần chính, tính chất và ứng dụng của nguyên liệu đá vôi (chứa calcium carbonate $\text{CaCO}_3$) và các loại quặng tự nhiên.",
            r"Nhận biết được dụng cụ thí nghiệm hóa học cơ bản, ý nghĩa các biển báo nguy hiểm (chất dễ cháy, chất ăn mòn, chất độc, dụng cụ sắc nhọn/dễ vỡ) và thực hiện đúng quy tắc an toàn phòng thí nghiệm.",
        ],
        formulas=[
            {
                "name": "Phản ứng nhận biết đá vôi (calcium carbonate) bằng acid",
                "formula": r"$\text{CaCO}_3 + 2\text{HCl} \rightarrow \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2\uparrow$",
                "note": r"Nhỏ hydrochloric acid ($\text{HCl}$) hoặc giấm ăn vào đá vôi ($\text{CaCO}_3$) thấy sủi bọt khí carbon dioxide ($\text{CO}_2\uparrow$).",
            },
            {
                "name": "Tính khối lượng hợp chất nguyên chất trong nguyên liệu/quặng",
                "formula": r"$m_{\text{CaCO}_3} = m_{\text{đá vôi}} \cdot \dfrac{100\% - \%m_{\text{tạp chất}}}{100\%}$",
                "note": r"Đá vôi và quặng tự nhiên luôn là hỗn hợp chứa hợp chất chính và một phần tạp chất.",
            },
            {
                "name": "Nguyên tắc 3R trong sử dụng vật liệu bền vững",
                "formula": r"$3\text{R} = \text{Reduce (Giảm thiểu)} + \text{Reuse (Tái sử dụng)} + \text{Recycle (Tái chế)}$",
                "note": r"Áp dụng đặc biệt cho vật liệu nhựa, kim loại ($\text{Al}$, $\text{Fe}$), thủy tinh và giấy để bảo vệ môi trường.",
            },
        ],
        theory_sections=[
            {
                "title": "1. Một số vật liệu thông dụng và mô hình 3R",
                "content": (
                    r"- **Vật liệu kim loại** (iron $\text{Fe}$, aluminium $\text{Al}$, copper $\text{Cu}$, thép): Dẫn điện, dẫn nhiệt tốt, có ánh kim, dẻo và bền cơ học nhưng dễ bị ăn mòn/gỉ sét trong không khí ẩm hoặc môi trường acid, muối. Để bảo vệ đồ vật bằng kim loại cần sơn phủ, mạ kẽm ($\text{Zn}$), bôi dầu mỡ và giữ khô ráo." "\n"
                    r"- **Vật liệu nhựa (chất dẻo)**: Nhẹ, bền, cách điện, dễ tạo hình nhưng dễ biến dạng ở nhiệt độ cao và rất khó phân hủy sinh học (gây ô nhiễm trắng). Khi đựng thực phẩm nóng chỉ dùng nhựa an toàn (như nhựa PP ký hiệu số $5$) hoặc hộp thủy tinh/sứ." "\n"
                    r"- **Thủy tinh và gốm sứ**: Thủy tinh trong suốt, không thấm nước, trơ với nhiều hóa chất (dùng làm ống nghiệm, bình cầu, cốc đong trong phòng thí nghiệm) nhưng giòn, dễ vỡ. Gốm sứ bền nhiệt, cách điện tốt." "\n"
                    r"- **Cao su**: Có tính đàn hồi cao, không thấm nước và khí, cách điện, không tan trong nước nhưng bị hòa tan bởi xăng dầu (dùng làm lốp xe, găng tay bảo hộ, nút cao su phòng thí nghiệm)." "\n"
                    r"- **Mô hình $3\text{R}$**: **Reduce** (Giảm thiểu lượng rác thải nhựa dùng một lần), **Reuse** (Tái sử dụng chai lọ thủy tinh, túi vải), **Recycle** (Tái chế phế liệu kim loại $\text{Al}$, $\text{Fe}$, giấy, nhựa)."
                ),
            },
            {
                "title": "2. Nhiên liệu và nguyên liệu tự nhiên",
                "content": (
                    r"- **Nhiên liệu (chất đốt)**: Là những chất khi cháy tỏa nhiệt và phát sáng, chia làm 3 loại theo trạng thái:" "\n"
                    r"  + Nhiên liệu rắn: Than đá, củi, gỗ, nến sáp." "\n"
                    r"  + Nhiên liệu lỏng: Xăng, dầu diesel, dầu hỏa, cồn ethanol ($\text{C}_2\text{H}_5\text{OH}$)." "\n"
                    r"  + Nhiên liệu khí: Khí thiên nhiên, khí mỏ dầu, khí biogas (thành phần chính là methane $\text{CH}_4$), khí hóa lỏng LPG (propane $\text{C}_3\text{H}_8$ và butane $\text{C}_4\text{H}_{10}$)." "\n"
                    r"  + Để sử dụng nhiên liệu hiệu quả cần cung cấp vừa đủ khí oxygen ($\text{O}_2$) và tăng diện tích tiếp xúc của nhiên liệu với không khí (chẻ nhỏ củi, tạo lỗ cho viên than tổ ong, phun nhiên liệu lỏng thành tia sương)." "\n"
                    r"- **Nguyên liệu tự nhiên**: Là vật liệu thô khai thác từ tự nhiên chưa qua chế biến hóa học:" "\n"
                    r"  + **Đá vôi**: Thành phần chính là **calcium carbonate** ($\text{CaCO}_3$), cứng, màu trắng hoặc xám, không tan trong nước nhưng tác dụng với acid ($\text{HCl}$, giấm ăn) sủi bọt khí $\text{CO}_2\uparrow$; dùng sản xuất vôi sống ($\text{CaO}$), xi măng, vật liệu xây dựng." "\n"
                    r"  + **Quặng**: Quặng bauxite (giàu $\text{Al}_2\text{O}_3$) dùng sản xuất aluminium ($\text{Al}$); quặng hematite ($\text{Fe}_2\text{O}_3$) và magnetite ($\text{Fe}_3\text{O}_4$) dùng luyện gang thép ($\text{Fe}$); quặng apatite dùng sản xuất phân lân; cát thạch anh ($\text{SiO}_2$) dùng sản xuất thủy tinh."
                ),
            },
            {
                "title": "3. Quy tắc an toàn và biển báo trong phòng thí nghiệm hóa học",
                "content": (
                    r"- **Quy tắc an toàn bắt buộc**:" "\n"
                    r"  + Mặc áo choàng blouse, buộc gọn tóc, đeo kính bảo hộ, găng tay và khẩu trang khi làm thí nghiệm với hóa chất hoặc nhiệt." "\n"
                    r"  + Tuyệt đối **không ăn uống, đùa nghịch**, không tự ý nếm hóa chất hoặc hít trực tiếp hơi hóa chất (khi cần nhận biết mùi phải dùng bàn tay phẩy nhẹ từ miệng lọ về phía mũi)." "\n"
                    r"  + Khi tắt đèn cồn phải dùng **nắp đậy đèn cồn** chụp lên bấc để cách ly với $\text{O}_2$, tuyệt đối **không dùng miệng thổi tắt đèn cồn** vì lửa có thể bén vào bầu cồn gây nổ." "\n"
                    r"- **Các biển báo nguy hiểm thường gặp**:" "\n"
                    r"  + **Chất dễ cháy** (hình ngọn lửa): cồn ethanol $\text{C}_2\text{H}_5\text{OH}$, xăng, acetone." "\n"
                    r"  + **Chất ăn mòn** (hình giọt chất lỏng làm mòn bề mặt kim loại và bàn tay): hydrochloric acid ($\text{HCl}$) đặc, sulfuric acid ($\text{H}_2\text{SO}_4$) đặc, dung dịch sodium hydroxide ($\text{NaOH}$) đặc." "\n"
                    r"  + **Chất độc** (hình đầu lâu xương chéo): hóa chất độc hại."
                ),
            },
        ],
        worked_examples=[
            {
                "title": "Ví dụ 1: Xử lý tình huống an toàn với đèn cồn và đá vôi",
                "problem": (
                    r"a) Vì sao khi kết thúc thí nghiệm đun nóng bằng đèn cồn, ta phải dùng nắp nhựa/thủy tinh đậy kín miệng đèn cồn mà tuyệt đối không được dùng miệng thổi?" "\n"
                    r"b) Làm thế nào để nhận biết một mẫu đá lấy từ tự nhiên có phải là đá vôi (chứa $\text{CaCO}_3$) hay không?"
                ),
                "solution": (
                    r"- **a)** Khi đậy nắp đèn cồn, ngọn lửa bị cách ly hoàn toàn với khí oxygen ($\text{O}_2$) bên ngoài nên tự tắt an toàn. Nếu dùng miệng thổi, luồng gió đẩy ngọn lửa tạt ngược vào trong bầu chứa hơi ethanol ($\text{C}_2\text{H}_5\text{OH}$) đang nóng làm bùng cháy hoặc nổ đèn cồn." "\n"
                    r"- **b)** Nhỏ vài giọt dung dịch hydrochloric acid ($\text{HCl}$) hoặc giấm ăn ($\text{CH}_3\text{COOH}$) lên bề mặt mẫu đá: nếu thấy hiện tượng **sủi bọt khí** không màu ($\text{CO}_2\uparrow$) thì mẫu đá đó chứa calcium carbonate ($\text{CaCO}_3$ - đá vôi)."
                ),
            },
            {
                "title": "Ví dụ 2: Tính khối lượng calcium carbonate trong đá vôi",
                "problem": (
                    r"Một mẫu đá vôi khai thác từ núi đá có khối lượng $200\text{ kg}$, trong đó chứa $85\%$ khối lượng là calcium carbonate ($\text{CaCO}_3$) nguyên chất, phần còn lại là tạp chất trơ. "
                    r"Tính khối lượng $\text{CaCO}_3$ nguyên chất và khối lượng tạp chất có trong mẫu đá vôi trên."
                ),
                "solution": (
                    r"- Khối lượng calcium carbonate ($\text{CaCO}_3$) nguyên chất là:" "\n"
                    r"$$m_{\text{CaCO}_3} = 200 \cdot \dfrac{85}{100} = 170\text{ kg}$$" "\n"
                    r"- Khối lượng tạp chất trơ trong mẫu đá vôi là:" "\n"
                    r"$$m_{\text{tạp chất}} = 200 - 170 = 30\text{ kg}$$"
                ),
            },
        ],
        key_takeaways=[
            r"Vật liệu (kim loại, nhựa, thủy tinh, gốm, cao su) dùng trực tiếp chế tạo đồ vật; nhiên liệu (than, xăng, khí gas $\text{CH}_4$) dùng đốt tỏa nhiệt; nguyên liệu (đá vôi $\text{CaCO}_3$, quặng) dùng làm đầu vào sản xuất công nghiệp.",
            r"Đá vôi chứa thành phần chính là calcium carbonate ($\text{CaCO}_3$), sủi bọt khí $\text{CO}_2\uparrow$ khi tác dụng với acid.",
            r"Trong phòng thí nghiệm: không nếm/ngửi trực tiếp hóa chất, dùng nắp đậy tắt đèn cồn (không thổi), và nhận diện đúng biển báo chất ăn mòn, chất dễ cháy, chất độc.",
        ],
        questions=[
            mcq(
                r"Thành phần hóa học chính của nguyên liệu đá vôi tự nhiên là hợp chất nào sau đây?",
                [
                    r"Copper(II) sulfate ($\text{CuSO}_4$).",
                    r"Carbon dioxide ($\text{CO}_2$).",
                    r"Calcium carbonate ($\text{CaCO}_3$).",
                    r"Sodium chloride ($\text{NaCl}$).",
                ],
                "C",
                "biet",
                r"Đá vôi tự nhiên có thành phần chính là hợp chất calcium carbonate ($\text{CaCO}_3$).",
            ),
            mcq(
                r"Loại quặng tự nhiên nào sau đây là nguyên liệu chính dùng để sản xuất kim loại aluminium ($\text{Al}$)?",
                [
                    r"Quặng apatite (sản xuất phân lân).",
                    r"Quặng hematite (sản xuất gang, thép $\text{Fe}$).",
                    r"Cát thạch anh (chứa $\text{SiO}_2$).",
                    r"Quặng bauxite (giàu $\text{Al}_2\text{O}_3$).",
                ],
                "D",
                "biet",
                r"Quặng bauxite (chứa thành phần chính là aluminium oxide $\text{Al}_2\text{O}_3$) là nguyên liệu để sản xuất kim loại aluminium ($\text{Al}$).",
            ),
            mcq(
                r"Biển báo an toàn có hình giọt chất lỏng nhỏ xuống làm ăn mòn thanh kim loại và bàn tay trên các lọ đựng dung dịch hydrochloric acid ($\text{HCl}$) đặc hoặc sodium hydroxide ($\text{NaOH}$) đặc mang ý nghĩa:",
                [
                    r"Cảnh báo hóa chất ăn mòn.",
                    r"Cảnh báo chất dễ cháy nổ.",
                    r"Cảnh báo khu vực có điện áp cao.",
                    r"Cảnh báo dụng cụ thủy tinh dễ vỡ.",
                ],
                "A",
                "biet",
                r"Hình ảnh chất lỏng nhỏ xuống làm hỏng bề mặt kim loại và tổn thương da tay là biển báo chuẩn quốc tế về **hóa chất ăn mòn** (Corrosive).",
            ),
            mcq(
                r"Trong phòng thí nghiệm hóa học, thao tác nào sau đây là **đúng quy tắc an toàn** khi muốn tắt ngọn lửa đèn cồn?",
                [
                    r"Cầm đèn cồn đang cháy dốc ngược xuống mặt bàn.",
                    r"Dùng nắp đèn cồn đậy kín lên phần bấc đang cháy.",
                    r"Dùng miệng thổi thật mạnh trực tiếp vào ngọn lửa đèn cồn.",
                    r"Đổ trực tiếp một cốc nước lạnh lên bầu đèn cồn đang cháy.",
                ],
                "B",
                "biet",
                r"Để tắt đèn cồn an toàn, bắt buộc phải dùng nắp đèn cồn chụp kín lên bấc đèn nhằm ngăn cách ngọn lửa với khí oxygen ($\text{O}_2$). Tuyệt đối không thổi bằng miệng hoặc đổ nước vì dễ gây cháy lan hoặc nổ đèn cồn.",
            ),
            mcq(
                r"Vì sao người ta khoan nhiều lỗ thông dọc theo viên than tổ ong hoặc chẻ nhỏ củi trước khi đưa vào bếp đun?",
                [
                    r"Để viên than tổ ong biến đổi thành nhiên liệu khí trước khi cháy.",
                    r"Để ngăn không cho khí oxygen ($\text{O}_2$) tiếp xúc với phần bên trong viên than.",
                    r"Để làm tăng diện tích tiếp xúc của nhiên liệu rắn với khí oxygen ($\text{O}_2$) trong không khí, giúp nhiên liệu cháy hoàn toàn và hiệu quả hơn.",
                    r"Để làm giảm nhiệt độ bắt cháy của than đá xuống dưới $0^\circ\text{C}$.",
                ],
                "C",
                "hieu",
                r"Việc tạo các lỗ thông khí trên viên than tổ ong hoặc chẻ nhỏ củi giúp tăng diện tích bề mặt tiếp xúc giữa nhiên liệu rắn với khí oxygen ($\text{O}_2$) trong không khí, nhờ đó sự cháy diễn ra đều, triệt để và giảm lượng khí độc $\text{CO}$ sinh ra.",
            ),
            mcq(
                r"Lý do chính khiến các dụng cụ đun nóng và chứa hóa chất trong phòng thí nghiệm (như ống nghiệm, bình cầu, cốc đong) thường được làm bằng thủy tinh chịu nhiệt thay vì bằng nhựa hoặc kim loại iron ($\text{Fe}$) là:",
                [
                    r"Vì thủy tinh dẫn điện tốt hơn kim loại iron ($\text{Fe}$) và không bao giờ bị vỡ khi rơi.",
                    r"Vì thủy tinh có tính đàn hồi cao như cao su và nhẹ hơn nhựa.",
                    r"Vì thủy tinh là nhiên liệu tỏa nhiều nhiệt khi tiếp xúc với nước.",
                    r"Vì thủy tinh trong suốt giúp dễ quan sát hiện tượng, chịu nhiệt tốt và không bị ăn mòn bởi hầu hết các acid hay muối.",
                ],
                "D",
                "hieu",
                r"Thủy tinh phòng thí nghiệm (như thủy tinh borosilicate) có độ trong suốt cao để quan sát màu sắc/kết tủa/bọt khí, chịu nhiệt độ cao (không bị chảy như nhựa) và trơ về mặt hóa học (không tác dụng với acid $\text{HCl}$, $\text{H}_2\text{SO}_4$ loãng như kim loại $\text{Fe}$).",
            ),
            tf4(
                r"Xét các nhận định về tính chất, ứng dụng và sử dụng bền vững các loại vật liệu, nhiên liệu, nguyên liệu trong đời sống:",
                [
                    r"Kim loại copper ($\text{Cu}$) và aluminium ($\text{Al}$) là các vật liệu dẫn điện, dẫn nhiệt tốt; để hạn chế sự ăn mòn kim loại iron ($\text{Fe}$), người ta thường sơn phủ bề mặt để ngăn $\text{Fe}$ tiếp xúc với oxygen ($\text{O}_2$) và hơi nước ($\text{H}_2\text{O}$).",
                    r"Khí biogas được sản xuất từ quá trình ủ kín chất thải chăn nuôi có thành phần chính là khí methane ($\text{CH}_4$), thuộc nhóm nhiên liệu tái tạo thân thiện với môi trường.",
                    r"Khi nhỏ giấm ăn hoặc dung dịch hydrochloric acid ($\text{HCl}$) lên bề mặt bàn đá vôi ($\text{CaCO}_3$), mặt đá không hề bị ảnh hưởng gì vì đá vôi trơ với mọi loại acid.",
                    r"Việc thu gom vỏ lon nước giải khát bằng aluminium ($\text{Al}$) để nấu chảy và sản xuất lại thành các vật dụng mới tương ứng với chữ Recycle (Tái chế) trong mô hình $3\text{R}$.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Sơn phủ bề mặt kim loại $\text{Fe}$ giúp cách ly kim loại với $\text{O}_2$ và độ ẩm không khí, chống gỉ sét hiệu quả." "\n"
                    r"- **Ý b) Đúng**: Khí biogas chứa chủ yếu methane ($\text{CH}_4$), vừa tận dụng chất thải hữu cơ giảm ô nhiễm vừa cung cấp nhiên liệu khí sạch." "\n"
                    r"- **Ý c) Sai**: Đá vôi chứa $\text{CaCO}_3$ phản ứng hóa học với acid tạo muối tan và sủi bọt khí $\text{CO}_2\uparrow$, làm bề mặt bàn đá bị ăn mòn và rỗ." "\n"
                    r"- **Ý d) Đúng**: Nấu chảy phế liệu $\text{Al}$ để chế tạo sản phẩm mới là hoạt động tái chế (Recycle) giúp tiết kiệm quặng bauxite và điện năng."
                ),
            ),
            tf4(
                r"Trong giờ thực hành tại phòng thí nghiệm hóa học, giáo viên hướng dẫn học sinh các quy tắc an toàn khi tiếp xúc với hóa chất và dụng cụ. Xét tính đúng/sai của các phát biểu sau:",
                [
                    r"Khi muốn nhận biết mùi của một hóa chất trong lọ, học sinh chỉ được mở nắp, để lọ cách xa mặt và dùng bàn tay phẩy nhẹ luồng hơi từ miệng lọ về phía mũi.",
                    r"Nếu chẳng may bị hóa chất (như dung dịch acid loãng hoặc base) bắn vào da tay, việc đầu tiên cần làm ngay lập tức là xả rửa kỹ vùng da đó dưới vòi nước sạch chảy nhẹ trong nhiều phút và báo cho giáo viên.",
                    r"Sau khi lấy một lượng hóa chất lỏng ra khỏi lọ để làm thí nghiệm, nếu dùng không hết thì học sinh nên đổ ngay phần hóa chất thừa ngược trở lại vào lọ gốc để tiết kiệm.",
                    r"Trên nhãn chai đựng cồn ethanol ($\text{C}_2\text{H}_5\text{OH}$) $90^\circ$ có in biển báo hình ngọn lửa; vì vậy không được đặt chai cồn gần ngọn lửa đèn cồn đang cháy.",
                ],
                "Đ/Đ/S/Đ",
                "hieu",
                (
                    r"- **Ý a) Đúng**: Phẩy nhẹ tay giúp một lượng rất nhỏ hơi hóa chất bay tới mũi, tránh hít trực tiếp nồng độ cao gây ngộ độc đường hô hấp." "\n"
                    r"- **Ý b) Đúng**: Rửa ngay dưới vòi nước sạch nhiều phút giúp làm loãng và cuốn trôi hóa chất ăn mòn trên da trước khi xử lý y tế tiếp theo." "\n"
                    r"- **Ý c) Sai**: Tuyệt đối **không** đổ hóa chất thừa trở lại lọ gốc vì có thể làm nhiễm bẩn hoặc gây phản ứng hỏng toàn bộ lọ hóa chất chuẩn." "\n"
                    r"- **Ý d) Đúng**: Ethanol ($\text{C}_2\text{H}_5\text{OH}$) rất dễ bay hơi và dễ bắt lửa (biển báo hình ngọn lửa), để gần đèn cồn đang cháy dễ gây hỏa hoạn."
                ),
            ),
            mcq(
                r"Một hộ gia đình chăn nuôi lắp đặt hầm ủ khí biogas. Trung bình mỗi ngày gia đình đun nấu hết $1{,}5\text{ m}^3$ khí biogas. Biết mỗi $1\text{ m}^3$ khí biogas khi đốt cháy hoàn toàn tỏa ra nhiệt lượng $22\text{ MJ}$ (tương đương nhiệt lượng tỏa ra khi đốt $0{,}6\text{ kg}$ khí hóa lỏng LPG). Trong $30$ ngày, việc sử dụng hầm biogas đã giúp gia đình tiết kiệm được bao nhiêu kilôgam ($\text{kg}$) khí LPG?",
                [
                    r"$27\text{ kg}$.",
                    r"$18\text{ kg}$.",
                    r"$45\text{ kg}$.",
                    r"$33\text{ kg}$.",
                ],
                "A",
                "vandung",
                r"Trong $30$ ngày, tổng thể tích khí biogas gia đình sử dụng là: $V = 1{,}5 \cdot 30 = 45\text{ m}^3$. Vì $1\text{ m}^3$ biogas thay thế được $0{,}6\text{ kg}$ khí LPG nên khối lượng LPG tiết kiệm được là: $m_{\text{LPG}} = 45 \cdot 0{,}6 = 27\text{ kg}$.",
            ),
            short(
                r"Một nhà máy xi măng nhập về một lô nguyên liệu đá vôi tự nhiên có khối lượng $250\text{ tấn}$, trong đó hàm lượng tạp chất đất sét và cát là $8\%$ về khối lượng, phần còn lại là calcium carbonate ($\text{CaCO}_3$) nguyên chất. Hãy tính khối lượng calcium carbonate ($\text{CaCO}_3$) nguyên chất có trong lô đá vôi đó theo đơn vị tấn.",
                ["230", "230,0", "230.0"],
                "vandung",
                (
                    r"Phần trăm khối lượng của calcium carbonate ($\text{CaCO}_3$) nguyên chất trong lô đá vôi là:" "\n"
                    r"$$\%m_{\text{CaCO}_3} = 100\% - 8\% = 92\%$$" "\n"
                    r"Khối lượng $\text{CaCO}_3$ nguyên chất có trong $250\text{ tấn}$ đá vôi là:" "\n"
                    r"$$m_{\text{CaCO}_3} = 250 \cdot \dfrac{92}{100} = 230\text{ tấn}$$"
                ),
            ),
        ],
        description="Tính chất và sử dụng bền vững vật liệu kim loại, nhựa, thủy tinh, gốm, nhiên liệu rắn, lỏng, khí, nguyên liệu đá vôi, quặng và quy tắc an toàn phòng thí nghiệm hóa học.",
    ),
]


LESSONS = LESSONS_GRADE_6
