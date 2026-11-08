"""Hóa học Lớp 8 (KHTN 8 - Kết nối tri thức với cuộc sống): 2 Chương - 13 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 8

CH1 = ("l8-ch01-phan-ung-hoa-hoc", "Chương I: Phản ứng hóa học", "Chương I · Hóa học 8 (KHTN 8): Biến đổi hóa học, phản ứng tỏa nhiệt – thu nhiệt, mol, tỉ khối khí, nồng độ dung dịch, bảo toàn khối lượng, tính theo PTHH và tốc độ phản ứng.")
CH2 = ("l8-ch02-hop-chat-thong-dung", "Chương II: Một số hợp chất thông dụng", "Chương II · Hóa học 8 (KHTN 8): Acid, Base, thang pH, Oxide, Muối và Phân bón hóa học.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Sử dụng một số hóa chất, thiết bị cơ bản trong phòng thí nghiệm",
        icon="🧪",
        description="Quy tắc an toàn khi lấy và sử dụng hóa chất, dụng cụ thí nghiệm hóa học (ống nghiệm, bình cầu, phễu, đèn cồn) và thiết bị điện.",
        requirements=[
            "Nhận biết được các dụng cụ thí nghiệm hóa học cơ bản (ống nghiệm, cốc thủy tinh, bình tam giác, phễu, ống hút nhỏ giọt, đèn cồn) và cách sử dụng đúng quy trình.",
            "Thực hiện đúng quy tắc lấy hóa chất rắn (dùng thìa thủy tinh/kim loại hoặc kẹp) và hóa chất lỏng (dùng ống hút nhỏ giọt hoặc rót qua đũa thủy tinh; nhãn lọ quay vào lòng bàn tay).",
            "Tuân thủ quy tắc an toàn: không dùng tay trực tiếp cầm hóa chất, không nếm hoặc ngửi trực tiếp, không đổ hóa chất thừa ngược lại lọ gốc và tắt đèn cồn bằng nắp đậy.",
        ],
        definition="Khi làm việc trong phòng thí nghiệm Hóa học, việc nắm vững chức năng của từng dụng cụ (ống nghiệm, ống hút nhỏ giọt, đèn cồn...) và tuân thủ nghiêm ngặt quy tắc sử dụng hóa chất giúp thí nghiệm chính xác và an toàn tuyệt đối.",
        theory=(
            "### 1. Một số dụng cụ thí nghiệm Hóa học cơ bản\n"
            "- **Ống nghiệm**: thực hiện các phản ứng hóa học với lượng nhỏ hóa chất (chỉ lấy hóa chất không quá $\\dfrac{1}{3}$ thể tích ống nghiệm; khi đun nóng ống nghiệm phải kẹp ở vị trí cách miệng ống khoảng $\\dfrac{1}{3}$ từ trên xuống và hướng miệng ống về phía không có người).\n"
            "- **Ống hút nhỏ giọt (pipette)**: lấy một lượng nhỏ chất lỏng theo từng giọt (luôn giữ thẳng đứng, không dốc ngược để chất lỏng chảy vào bóp cao su).\n"
            "- **Đèn cồn**: dùng để đun nóng; lượng cồn trong đèn từ $\\dfrac{1}{3}$ đến $\\dfrac{2}{3}$ bầu đèn; **tắt đèn cồn bằng cách chụp nắp đèn cồn** lên ngọn lửa (tuyệt đối **không thổi tắt** bằng miệng và không châm đèn cồn này từ đèn cồn khác đang cháy).\n\n"
            "### 2. Quy tắc sử dụng hóa chất an toàn\n"
            "- **Tuyệt đối không dùng tay trần** tiếp xúc trực tiếp với hóa chất, không ăn uống hay nếm hóa chất.\n"
            "- Khi cần nhận biết mùi chất khí: dùng bàn tay **phẩy nhẹ** từ miệng ống nghiệm về phía mũi, không hít trực tiếp.\n"
            "- Hóa chất dùng xong còn thừa **không được đổ ngược trở lại bình chứa ban đầu** để tránh làm bẩn cả lọ hóa chất gốc.\n"
            "- Khi pha loãng sulfuric acid ($\\text{H}_2\\text{SO}_4$) đặc: bắt buộc **rót từ từ acid đặc vào nước** và khuấy đều, tuyệt đối **không đổ nước vào acid đặc**!"
        ),
        formulas=[
            G(
                "Quy tắc vàng an toàn Hóa chất và Đèn cồn",
                F("Quy tắc đun ống nghiệm và tắt đèn cồn", "$V_{\\text{hóa chất trong ống nghiệm}} \\le \\dfrac{1}{3}V_{\\text{ống}}; \\qquad \\text{Tắt đèn cồn} = \\text{Đậy nắp chụp (cách li } \\text{O}_2)$", "Khi đun ống nghiệm trên đèn cồn, phải hơ đều cả ống nghiệm rồi mới đun tập trung ở đáy ống, miệng ống nghiêng hướng về phía không có người."),
                F("Quy tắc pha loãng Acid đặc an toàn", "$\\text{Rót từ từ ACID ĐẶC vào NƯỚC và khuấy đều (Tuyệt đối KHÔNG đổ nước vào acid đặc)}$", "Nếu đổ nước vào $\\text{H}_2\\text{SO}_4$ đặc, nước nhẹ nổi lên trên và sôi đột ngột làm bắn các giọt acid đặc gây bỏng nặng."),
            )
        ],
        example="Giải thích vì sao khi muốn dập tắt ngọn lửa đèn cồn sau khi làm xong thí nghiệm, ta phải dùng nắp đèn cồn đậy chụp lên ngọn lửa mà tuyệt đối không được dùng miệng thổi tắt?",
        example_answer="Khi chụp nắp đèn cồn lên ngọn lửa, ta **cách li cồn đang cháy với khí oxygen** ngoài không khí nên ngọn lửa tắt ngay và an toàn. Nếu dùng miệng thổi, luồng gió có thể đẩy ngọn lửa tạt ngược vào bầu chứa cồn bên dưới gây bùng cháy hoặc nổ đèn cồn rất nguy hiểm.",
        real_life="Các bình đựng hóa chất trong phòng thí nghiệm và trong gia đình (như nước tẩy rửa bồn cầu, cồn y tế, xút thông cống) luôn phải dán nhãn rõ ràng và để xa tầm tay trẻ em.",
        quiz=[
            mcq("biet", "Cách làm nào sau đây là **đúng và an toàn** để tắt đèn cồn sau khi kết thúc thí nghiệm?", ["Dùng nắp đèn cồn đậy chụp trực tiếp lên ngọn lửa", "Dùng miệng thổi thật mạnh vào ngọn lửa", "Đổ một cốc nước vào bầu đèn cồn đang cháy", "Nghiêng đèn cồn cho cồn chảy ra bàn"], 0, "Đậy nắp đèn cồn giúp ngăn ngọn lửa tiếp xúc với khí oxygen, làm lửa tắt êm và an toàn."),
            mcq("biet", "Khi lấy hóa chất rắn dạng bột hoặc hạt nhỏ từ lọ hóa chất ra ống nghiệm, ta phải sử dụng dụng cụ nào?", ["Dùng thìa lấy hóa chất (thìa thủy tinh, sứ hoặc kim loại sạch) hoặc kẹp gắp", "Dùng hai ngón tay trần bốc trực tiếp", "Dùng ống hút nhỏ giọt", "Dốc ngược cả lọ hóa chất đổ tràn ra tay"], 0, "Tuyệt đối không dùng tay trần tiếp xúc với hóa chất; hóa chất rắn phải lấy bằng thìa chuyên dụng hoặc kẹp gắp."),
            mcq("hieu", "Sau khi làm thí nghiệm xong, nếu còn thừa một ít hóa chất đã lấy ra ngoài, ta nên xử lí như thế nào?", ["Thu gom vào bình chứa chất thải quy định theo hướng dẫn của giáo viên, tuyệt đối không đổ ngược trở lại lọ hóa chất gốc", "Đổ ngược trở lại vào lọ hóa chất ban đầu để tiết kiệm", "Đổ thẳng xuống sàn lớp học", "Mang về nhà cất trong tủ lạnh"], 0, "Đổ hóa chất thừa ngược lại lọ gốc sẽ làm nhiễm bẩn và hỏng toàn bộ lọ hóa chất tinh khiết ban đầu."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về an toàn trong phòng thí nghiệm Hóa học:", [
                "Khi muốn nhận biết mùi của một chất khí trong ống nghiệm, ta dùng bàn tay phẩy nhẹ khí về phía mũi chứ không đưa mũi hít trực tiếp.",
                "Khi đun nóng chất lỏng trong ống nghiệm, chỉ nên lấy lượng chất lỏng không quá $\\dfrac{1}{3}$ thể tích ống nghiệm và hướng miệng ống về phía không có người.",
                "Ta có thể dùng ngọn lửa của một đèn cồn đang cháy để châm trực tiếp sang một đèn cồn khác.",
                "Khi pha loãng $\\text{H}_2\\text{SO}_4$ đặc, ta phải rót từ từ acid đặc vào nước và dùng đũa thủy tinh khuấy đều.",
            ], [True, True, False, True], "Ý c) sai vì nghiêng đèn cồn để mồi lửa từ đèn cồn khác sẽ làm cồn tràn ra ngoài bén lửa gây cháy bỏng."),
            short("vandung", "Khi làm thí nghiệm trong ống nghiệm (đặc biệt là khi cần đun nóng chất lỏng), thể tích chất lỏng lấy vào ống nghiệm tối đa chỉ nên chiếm một phần mấy ($\\dfrac{1}{n}$, nhập mẫu số $n$) thể tích của ống nghiệm để tránh sôi trào bắn ra ngoài?", ["3"], "Thể tích hóa chất trong ống nghiệm chỉ nên lấy tối đa khoảng $\\dfrac{1}{3}$ thể tích ống nghiệm."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Biến đổi vật lí và biến đổi hóa học",
        icon="🔄",
        description="Phân biệt biến đổi vật lí (không tạo ra chất mới) và biến đổi hóa học (có sự tạo thành chất mới) qua các hiện tượng tự nhiên và thí nghiệm.",
        requirements=[
            "Phân biệt được **biến đổi vật lí** (chỉ thay đổi trạng thái, hình dạng, kích thước, hòa tan... mà **không tạo ra chất mới**) và **biến đổi hóa học** (có sự biến đổi chất ban đầu thành **chất mới**).",
            "Chỉ ra được dấu hiệu本質 nhất để khẳng định có biến đổi hóa học xảy ra là có sự xuất hiện của chất mới (khác chất ban đầu về tính chất).",
            "Phân tích được một quá trình thực tế (như đốt nến) gồm những giai đoạn nào là biến đổi vật lí và giai đoạn nào là biến đổi hóa học.",
        ],
        definition="Biến đổi vật lí là hiện tượng chất có sự biến đổi về trạng thái (thể), hình dạng, kích thước... nhưng vẫn giữ nguyên là chất ban đầu (không tạo ra chất mới). Biến đổi hóa học là hiện tượng chất có sự biến đổi tạo ra chất mới.",
        theory=(
            "### 1. Biến đổi vật lí\n"
            "- Bao gồm các quá trình: chuyển thể (nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ), hòa tan (pha nước muối, nước đường), nghiền nhỏ, cắt gọt, uốn cong vật.\n"
            "- **Đặc điểm cốt lõi**: **Không có chất mới nào được sinh ra**, phân tử của chất không bị biến đổi thành phân tử chất khác.\n\n"
            "### 2. Biến đổi hóa học\n"
            "- Là quá trình trong đó từ chất này biến đổi thành **chất khác (chất mới)**.\n"
            "- **Ví dụ điển hình**:\n"
            "  - Đốt bột sắt ($\\text{Fe}$) với bột lưu huỳnh ($\\text{S}$): tạo ra chất rắn mới là iron(II) sulfide ($\\text{FeS}$) màu xám đen, không còn bị nam châm hút.\n"
            "  - Đinh sắt để lâu ngoài không khí ẩm bị gỉ tạo thành gỉ sắt ($\\text{Fe}_2\\text{O}_3\\cdot n\\text{H}_2\\text{O}$) giòn, xốp màu nâu đỏ.\n"
            "  - Cơm để lâu bị thiu, sữa tươi lên men thành sữa chua, đốt cháy khí gas hoặc cồn tạo ra khí $\\text{CO}_2$ và hơi nước $\\text{H}_2\\text{O}$."
        ),
        formulas=[
            G(
                "Tiêu chí phân biệt Biến đổi vật lí và Biến đổi hóa học",
                F("Dấu hiệu phân biệt cốt lõi", "$\\text{Biến đổi VẬT LÍ}: \\text{Không tạo chất mới (chuyển thể, hòa tan, đập nhỏ)}; \\qquad \\text{Biến đổi HÓA HỌC}: \\text{Có tạo thành CHẤT MỚI}$", "Biến đổi hóa học chính là quá trình xảy ra **phản ứng hóa học**."),
                F("Phân tích các giai đoạn khi đốt một cây nến paraffin", "$\\text{Nến rắn} \\xrightarrow[(1)\\text{ Vật lí}]{\\text{nóng chảy}} \\text{Nến lỏng} \\xrightarrow[(2)\\text{ Vật lí}]{\\text{hóa hơi}} \\text{Hơi nến} \\xrightarrow[(3)\\text{ Hóa học (+ }\\text{O}_2\\text{)}]{\\text{cháy}} \\text{CO}_2 + \\text{H}_2\\text{O}$", "Chỉ có giai đoạn (3) hơi nến cháy tạo ra khí $\\text{CO}_2$ và hơi nước $\\text{H}_2\\text{O}$ là biến đổi hóa học!"),
            )
        ],
        example="Trộn đều hỗn hợp bột sắt ($\\text{Fe}$) và bột lưu huỳnh ($\\text{S}$) theo tỉ lệ khối lượng $7 : 4$ rồi chia làm hai phần:\n- Phần 1: Đưa thanh nam châm lại gần thì thấy nam châm hút bột sắt tách ra khỏi bột lưu huỳnh.\n- Phần 2: Cho vào ống nghiệm đun nóng mạnh, hỗn hợp nóng đỏ lên và chuyển thành hợp chất iron(II) sulfide ($\\text{FeS}$) màu xám đen, không còn bị nam châm hút nữa.\nHãy cho biết ở phần nào đã xảy ra biến đổi vật lí và ở phần nào đã xảy ra biến đổi hóa học?",
        example_answer="- Ở **Phần 1**: việc trộn lẫn và dùng nam châm tách sắt chỉ là **biến đổi vật lí** vì sắt và lưu huỳnh vẫn giữ nguyên tính chất, chưa tạo ra chất mới.\n- Ở **Phần 2**: khi đun nóng đã xảy ra **biến đổi hóa học** vì tạo ra chất mới là $\\text{FeS}$ không còn tính từ của sắt.",
        real_life="Quá trình quang hợp của cây xanh (biến $\\text{CO}_2$ và $\\text{H}_2\\text{O}$ thành tinh bột và khí $\\text{O}_2$) và quá trình tiêu hóa thức ăn trong dạ dày con người đều là những biến đổi hóa học quan trọng duy trì sự sống.",
        quiz=[
            mcq("biet", "Dấu hiệu bản chất quan trọng nhất để phân biệt **biến đổi hóa học** với **biến đổi vật lí** là gì?", ["Biến đổi hóa học có sự tạo thành chất mới, còn biến đổi vật lí không tạo thành chất mới", "Biến đổi vật lí luôn cần đun nóng, còn biến đổi hóa học thì không", "Biến đổi hóa học chỉ xảy ra với chất khí", "Biến đổi vật lí làm tăng khối lượng của chất"], 0, "Dấu hiệu quyết định của biến đổi hóa học là có sự xuất hiện chất mới khác với chất ban đầu."),
            mcq("biet", "Hiện tượng nào sau đây là một **biến đổi hóa học**?", ["Đinh sắt để lâu ngoài không khí ẩm bị gỉ tạo thành lớp gỉ sắt màu nâu đỏ", "Nước lỏng trong ngăn đá tủ lạnh đông đặc thành nước đá", "Hòa tan muối ăn vào nước được dung dịch nước muối", "Dây tóc bóng đèn bằng vonfram nóng sáng lên khi có dòng điện chạy qua"], 0, "Sắt tác dụng với oxygen và hơi nước tạo thành chất mới là gỉ sắt nên là biến đổi hóa học; 3 hiện tượng còn lại không tạo ra chất mới nên là biến đổi vật lí."),
            mcq("hieu", "Khi đốt một cây nến bằng sáp paraffin: (1) sáp nến ở gần bấc chảy lỏng ra; (2) sáp lỏng thấm vào bấc rồi hóa hơi; (3) hơi sáp cháy trong không khí tạo thành khí carbon dioxide ($\\text{CO}_2$) và hơi nước ($\\text{H}_2\\text{O}$). Giai đoạn nào là biến đổi hóa học?", ["Chỉ có giai đoạn (3)", "Chỉ có giai đoạn (1)", "Giai đoạn (1) và (2)", "Cả ba giai đoạn (1), (2) và (3)"], 0, "Giai đoạn (1) nóng chảy và (2) hóa hơi chỉ là sự chuyển thể (biến đổi vật lí); chỉ giai đoạn (3) hơi nến cháy tạo ra chất mới ($\\text{CO}_2, \\text{H}_2\\text{O}$) mới là biến đổi hóa học."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về biến đổi vật lí và biến đổi hóa học:", [
                "Quá trình lên men sữa tươi thành sữa chua (chuyển đường lactose thành lactic acid) là một biến đổi hóa học.",
                "Nghiền nhỏ viên đường phèn thành bột đường mịn là một biến đổi hóa học.",
                "Hiện tượng mặt trời mọc làm sương sớm trên lá cây bay hơi tan biến là biến đổi vật lí.",
                "Đốt cháy khí gas (butane $\\text{C}_4\\text{H}_{10}$) trên bếp tạo ra khí $\\text{CO}_2$ và hơi nước là biến đổi hóa học.",
            ], [True, False, True, True], "Ý b) sai vì nghiền nhỏ đường phèn chỉ làm thay đổi kích thước hạt đường, chất vẫn là đường saccharose nên đó là biến đổi vật lí."),
            short("vandung", "Cho 5 hiện tượng sau: (1) Hòa tan đường vào nước; (2) Đốt cháy than đá tạo khí $\\text{CO}_2$; (3) Nước sôi hóa hơi; (4) Sắt bị gỉ trong không khí ẩm; (5) Cơm để lâu ngày bị ôi thiu. Có bao nhiêu hiện tượng trong danh sách trên là **biến đổi hóa học**?", ["3"], "Các hiện tượng (2) Đốt than, (4) Sắt bị gỉ và (5) Cơm bị thiu có tạo ra chất mới nên có $3$ hiện tượng là biến đổi hóa học (còn 1 và 3 là biến đổi vật lí)."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 3: Phản ứng hóa học và năng lượng của phản ứng",
        icon="🔥",
        description="Khái niệm phản ứng hóa học, chất phản ứng – sản phẩm, diễn biến vi mô (liên kết thay đổi, số nguyên tử bảo toàn), dấu hiệu nhận biết và phản ứng tỏa nhiệt – thu nhiệt.",
        requirements=[
            "Nêu được khái niệm phản ứng hóa học, phân biệt chất phản ứng (chất tham gia) và sản phẩm (chất tạo thành).",
            "Giải thích được bản chất vi mô của phản ứng hóa học: chỉ có **liên kết giữa các nguyên tử thay đổi** làm phân tử này biến đổi thành phân tử khác, còn **số nguyên tử mỗi nguyên tố giữ nguyên không đổi**.",
            "Nhận biết được các dấu hiệu có phản ứng xảy ra (đổi màu, tạo khí sủi bọt, tạo kết tủa, tỏa nhiệt/phát sáng) và phân biệt phản ứng tỏa nhiệt với phản ứng thu nhiệt.",
        ],
        definition="Phản ứng hóa học là quá trình biến đổi từ chất này (chất phản ứng) thành chất khác (sản phẩm). Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi làm phân tử này biến đổi thành phân tử khác, còn số nguyên tử của mỗi nguyên tố trước và sau phản ứng luôn giữ nguyên.",
        theory=(
            "### 1. Bản chất vi mô và Dấu hiệu nhận biết phản ứng hóa học\n"
            "- **Phương trình chữ**: $\\text{Chất phản ứng (Chất tham gia)} \\longrightarrow \\text{Sản phẩm}$.\n"
            "  - Trong quá trình phản ứng: lượng chất phản ứng **giảm dần**, lượng chất sản phẩm **tăng dần**.\n"
            "- **Diễn biến vi mô**:\n"
            "  - Trước phản ứng: các nguyên tử liên kết với nhau trong phân tử chất phản ứng.\n"
            "  - Trong phản ứng: các liên kết cũ bị phá vỡ và hình thành các liên kết mới.\n"
            "  - Sau phản ứng: tạo thành các phân tử mới (sản phẩm), nhưng **loại nguyên tử và tổng số nguyên tử của mỗi nguyên tố hoàn toàn không đổi**!\n"
            "- **Dấu hiệu nhận biết có phản ứng xảy ra**: (1) Thay đổi màu sắc; (2) Xuất hiện bọt khí ($\\uparrow$); (3) Xuất hiện chất rắn không tan – kết tủa ($\\downarrow$); (4) Tỏa nhiệt và phát sáng.\n\n"
            "### 2. Phản ứng tỏa nhiệt và Phản ứng thu nhiệt\n"
            "- **Phản ứng tỏa nhiệt**: phản ứng giải phóng năng lượng dưới dạng nhiệt ra môi trường xung quanh (làm nhiệt độ môi trường xung quanh **tăng lên**). Ví dụ: mọi phản ứng đốt cháy nhiên liệu (than, xăng, gas, cồn), phản ứng tôi vôi ($\\text{CaO} + \\text{H}_2\\text{O}$), phản ứng tạo gỉ sắt, hô hấp.\n"
            "- **Phản ứng thu nhiệt**: phản ứng hấp thụ năng lượng dưới dạng nhiệt từ môi trường xung quanh trong suốt quá trình phản ứng (làm nhiệt độ môi trường xung quanh **giảm đi** hoặc phải đun nóng liên tục mới xảy ra). Ví dụ: nung đá vôi ($\\text{CaCO}_3 \\xrightarrow{t^\\circ} \\text{CaO} + \\text{CO}_2$), hòa tan viên C sủi vào nước, quang hợp."
        ),
        formulas=[
            G(
                "Bản chất vi mô của Phản ứng hóa học và Năng lượng phản ứng",
                F("Quy luật bảo toàn nguyên tử và biến đổi phân tử", "$\\text{Trong PƯHH}: \\begin{cases} \\text{Liên kết giữa các nguyên tử: THAY ĐỔI} \\implies \\text{Phân tử thay đổi} \\\\ \\text{Số lượng nguyên tử của mỗi nguyên tố: GIỮ NGUYÊN KHÔNG ĐỔI} \\end{cases}$", "Đây chính là cơ sở vi mô của Định luật bảo toàn khối lượng và cân bằng phương trình hóa học."),
                F("Phân biệt Phản ứng tỏa nhiệt và Phản ứng thu nhiệt", "$\\text{PƯ Tỏa nhiệt}: \\text{Giải phóng nhiệt } (T_{\\text{môi trường}} \\uparrow); \\qquad \\text{PƯ Thu nhiệt}: \\text{Hấp thụ nhiệt } (T_{\\text{môi trường}} \\downarrow \\text{ hoặc cần nung liên tục})$", "Phản ứng đốt cháy nhiên liệu luôn là phản ứng tỏa nhiệt; phản ứng nhiệt phân đá vôi luôn là phản ứng thu nhiệt."),
            )
        ],
        example="Xét phản ứng tổng hợp nước từ khí hydrogen và khí oxygen: $\\text{Hydrogen} + \\text{Oxygen} \\xrightarrow{t^\\circ} \\text{Nước}$ ($2\\text{H}_2 + \\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{H}_2\\text{O}$). Hãy cho biết: (a) Trước phản ứng những nguyên tử nào liên kết với nhau, sau phản ứng những nguyên tử nào liên kết với nhau? (b) Số nguyên tử $\\text{H}$ và số nguyên tử $\\text{O}$ trước và sau phản ứng có thay đổi không?",
        example_answer="- (a) **Trước phản ứng**: $2$ nguyên tử $\\text{H}$ liên kết với nhau trong phân tử $\\text{H}_2$, $2$ nguyên tử $\\text{O}$ liên kết với nhau trong phân tử $\\text{O}_2$. **Sau phản ứng**: mỗi nguyên tử $\\text{O}$ liên kết với $2$ nguyên tử $\\text{H}$ tạo thành phân tử nước $\\text{H}_2\\text{O}$.\n- (b) Số nguyên tử $\\text{H}$ ($4$ nguyên tử) và số nguyên tử $\\text{O}$ ($2$ nguyên tử) trước và sau phản ứng **giữ nguyên không đổi**.",
        real_life="Túi chườm nóng tự sôi dùng trong mùa đông tận dụng phản ứng tỏa nhiệt, trong khi túi chườm lạnh cấp cứu chấn thương thể thao tận dụng quá trình thu nhiệt mạnh khi hòa tan muối ammonium nitrate trong nước.",
        quiz=[
            mcq("biet", "Trong một phản ứng hóa học, yếu tố nào thay đổi làm cho phân tử này biến đổi thành phân tử khác?", ["Liên kết giữa các nguyên tử thay đổi (còn số nguyên tử của mỗi nguyên tố giữ nguyên)", "Số lượng nguyên tử của mỗi nguyên tố tăng gấp đôi", "Hạt nhân nguyên tử của nguyên tố này biến thành hạt nhân nguyên tố khác", "Các nguyên tử bị biến mất hoàn toàn"], 0, "Trong phản ứng hóa học, chỉ có liên kết giữa các nguyên tử thay đổi, còn số nguyên tử mỗi nguyên tố được bảo toàn."),
            mcq("biet", "Phản ứng hóa học giải phóng năng lượng dưới dạng nhiệt ra môi trường xung quanh (làm nóng môi trường xung quanh) được gọi là phản ứng gì?", ["Phản ứng tỏa nhiệt", "Phản ứng thu nhiệt", "Biến đổi vật lí", "Sự ngưng tụ"], 0, "Phản ứng giải phóng nhiệt năng ra môi trường là phản ứng tỏa nhiệt."),
            mcq("hieu", "Trong các quá trình hóa học sau đây, quá trình nào là **phản ứng thu nhiệt**?", ["Nung đá vôi ($\\text{CaCO}_3$) ở nhiệt độ cao để tạo ra vôi sống ($\\text{CaO}$) và khí $\\text{CO}_2$ (ngừng cung cấp nhiệt thì phản ứng dừng lại)", "Đốt cháy khí gas trên bếp để nấu ăn", "Đốt cháy than đá trong lò nhiệt điện", "Đốt cháy cồn trong đèn cồn"], 0, "Phản ứng nung đá vôi cần hấp thụ nhiệt liên tục từ lò nung, nếu ngừng đun thì phản ứng dừng ngay nên là phản ứng thu nhiệt; còn các phản ứng đốt cháy nhiên liệu đều tỏa nhiệt."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản ứng hóa học:", [
                "Trong quá trình phản ứng hóa học diễn ra, lượng chất phản ứng giảm dần và lượng chất sản phẩm tăng dần.",
                "Sự xuất hiện chất kết tủa (chất rắn không tan), sủi bọt khí hoặc đổi màu sắc là những dấu hiệu giúp nhận biết có phản ứng hóa học xảy ra.",
                "Mọi phản ứng đốt cháy nhiên liệu (than, củi, xăng, dầu, khí gas) đều là phản ứng thu nhiệt.",
                "Khi thả viên sủi vitamin C vào cốc nước thấy sủi bọt khí và sờ thành cốc thấy mát lạnh hơn ban đầu, chứng tỏ đã xảy ra phản ứng thu nhiệt.",
            ], [True, True, False, True], "Ý c) sai vì mọi phản ứng đốt cháy nhiên liệu đều giải phóng nhiệt lượng lớn ra môi trường nên là **phản ứng tỏa nhiệt**."),
            short("vandung", "Khi cho $4$ nguyên tử hydrogen ($2$ phân tử $\\text{H}_2$) phản ứng vừa đủ với $2$ nguyên tử oxygen ($1$ phân tử $\\text{O}_2$) để tạo thành các phân tử nước ($\\text{H}_2\\text{O}$), tổng số nguyên tử hydrogen có trong các phân tử nước sau phản ứng bằng bao nhiêu nguyên tử?", ["4"], "Trong phản ứng hóa học, số nguyên tử mỗi nguyên tố được bảo toàn nên sau phản ứng vẫn có đúng $4$ nguyên tử hydrogen (nằm trong $2$ phân tử $\\text{H}_2\\text{O}$).", unit="nguyên tử"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 4: Mol và tỉ khối của chất khí",
        icon="🎈",
        description="Khái niệm mol, hằng số Avogadro N_A = 6,022.10²³, khối lượng mol M = m/n, thể tích mol chất khí ở điều kiện chuẩn (25 °C, 1 bar: V = 24,79.n) và tỉ khối chất khí d_A/B = M_A/M_B.",
        requirements=[
            "Định nghĩa được mol là lượng chất có chứa $N_A = 6{,}022 \\cdot 10^{23}$ hạt vi mô (nguyên tử, phân tử) của chất đó, và khối lượng mol ($M$, đơn vị $\\text{g/mol}$) có trị số bằng khối lượng nguyên tử hoặc phân tử ($\\text{amu}$).",
            "Vận dụng thành thạo bộ công thức chuyển đổi số mol: $n = \\dfrac{N}{6{,}022 \\cdot 10^{23}}$, $n = \\dfrac{m}{M} \\iff m = n \\cdot M$ và thể tích khí ở **điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$)**: $V = 24{,}79 \\cdot n \\iff n = \\dfrac{V}{24{,}79}$.",
            "Tính được tỉ khối của khí $A$ đối với khí $B$ ($d_{A/B} = \\dfrac{M_A}{M_B}$) và đối với không khí ($d_{A/\\text{kk}} = \\dfrac{M_A}{29}$).",
        ],
        definition="Mol là lượng chất có chứa $N_A = 6{,}022 \\cdot 10^{23}$ hạt vi mô (nguyên tử hoặc phân tử) của chất đó. Ở điều kiện chuẩn ($25^\\circ\\text{C}$ và $1\\text{ bar}$), $1\\text{ mol}$ của bất kì chất khí nào cũng chiếm thể tích bằng $24{,}79\\text{ lít}$ ($V = 24{,}79 \\cdot n$).",
        theory=(
            "### 1. Mol, Khối lượng mol ($M$) và Thể tích mol của chất khí ở điều kiện chuẩn\n"
            "- **Số Avogadro**: $N_A \\approx 6{,}022 \\cdot 10^{23}\\text{ mol}^{-1}$. Số mol chất từ số hạt $N$: $n = \\dfrac{N}{N_A}$.\n"
            "- **Khối lượng mol ($M$, đơn vị $\\text{g/mol}$)**: khối lượng tính bằng gam của $1\\text{ mol}$ chất (có số trị bằng đúng khối lượng nguyên tử/phân tử tính theo $\\text{amu}$, ví dụ $M_{\\text{H}_2\\text{O}} = 18\\text{ g/mol}$):\n"
            "  $$n = \\dfrac{m}{M} \\iff m = n \\cdot M \\iff M = \\dfrac{m}{n}$$\n"
            "- **Thể tích mol của chất khí ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$)**:\n"
            "  $$V = 24{,}79 \\cdot n \\iff n = \\dfrac{V}{24{,}79} \\quad (\\text{với } V \\text{ tính bằng lít})$$\n\n"
            "### 2. Tỉ khối của chất khí\n"
            "- Để biết khí $A$ nặng hay nhẹ hơn khí $B$ bao nhiêu lần (ở cùng nhiệt độ và áp suất), ta tính **tỉ khối của khí $A$ đối với khí $B$**:\n"
            "  $$d_{A/B} = \\dfrac{M_A}{M_B}$$\n"
            "- **Tỉ khối của khí $A$ đối với không khí** (coi khối lượng mol trung bình của không khí là $M_{\\text{kk}} \\approx 29\\text{ g/mol}$):\n"
            "  $$d_{A/\\text{kk}} = \\dfrac{M_A}{29}$$\n"
            "  - Nếu $M_A > 29$ ($d_{A/\\text{kk}} > 1$, như $\\text{O}_2, \\text{CO}_2, \\text{Cl}_2, \\text{SO}_2$): khí $A$ **nặng hơn không khí** (thu bằng cách **đặt đứng/ngửa bình**).\n"
            "  - Nếu $M_A < 29$ ($d_{A/\\text{kk}} < 1$, như $\\text{H}_2, \\text{He}, \\text{CH}_4, \\text{NH}_3$): khí $A$ **nhẹ hơn không khí** (thu bằng cách **úp ngược bình**)."
        ),
        formulas=[
            G(
                "Bộ công thức tính Số mol (n), Thể tích đkc (24,79 L) và Tỉ khối chất khí",
                F("Chuyển đổi giữa Số mol (n), Khối lượng (m) và Thể tích khí ở đkc (25 °C, 1 bar)", "$n = \\dfrac{m}{M} \\iff m = n \\cdot M; \\qquad V_{\\text{đkc}} = 24{,}79 \\cdot n \\iff n = \\dfrac{V_{\\text{đkc}}}{24{,}79}$", "Lưu ý chuẩn GDPT 2018: ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$), $1\\text{ mol}$ khí có thể tích là **$24{,}79\\text{ lít}$**."),
                F("Công thức tính tỉ khối của chất khí", "$d_{A/B} = \\dfrac{M_A}{M_B} \\implies M_A = d_{A/B} \\cdot M_B; \\qquad d_{A/\\text{kk}} = \\dfrac{M_A}{29}$", "Khí có $M > 29$ nặng hơn không khí; khí có $M < 29$ nhẹ hơn không khí."),
            )
        ],
        example="Ở điều kiện chuẩn ($25^\\circ\\text{C}$ và $1\\text{ bar}$), một bình chứa $V = 4{,}958\\text{ lít}$ khí carbon dioxide ($\\text{CO}_2$, biết $\\text{C}=12, \\text{O}=16$). Hãy tính số mol $n$, khối lượng $m$ của lượng khí $\\text{CO}_2$ trên và cho biết khí $\\text{CO}_2$ nặng hơn không khí bao nhiêu lần.",
        example_answer="Số mol khí $\\text{CO}_2$ ở điều kiện chuẩn là $n = \\dfrac{V}{24{,}79} = \\dfrac{4{,}958}{24{,}79} = 0{,}2\\text{ mol}$. Khối lượng mol của $\\text{CO}_2$ là $M_{\\text{CO}_2} = 12 + 2 \\cdot 16 = 44\\text{ g/mol}$. Khối lượng của $0{,}2\\text{ mol}\\text{ CO}_2$ là $m = n \\cdot M = 0{,}2 \\cdot 44 = 8{,}8\\text{ g}$. Tỉ khối của $\\text{CO}_2$ so với không khí là $d_{\\text{CO}_2/\\text{kk}} = \\dfrac{44}{29} \\approx 1{,}52$ (nặng hơn không khí khoảng $1{,}52$ lần).",
        real_life="Vì khí $\\text{CO}_2$ nặng hơn không khí ($d = \\dfrac{44}{29} \\approx 1{,}52$) nên trong các hang sâu hoặc giếng sâu không thông thoáng thường tích tụ nhiều khí $\\text{CO}_2$ ở dưới đáy gây nguy cơ ngạt thở; ngược lại khí $\\text{He}$ ($M = 4$) và $\\text{H}_2$ ($M = 2$) rất nhẹ so với không khí nên bơm vào bóng bay giúp bóng bay lên cao.",
        quiz=[
            mcq("biet", "Ở điều kiện chuẩn ($25^\\circ\\text{C}$ và $1\\text{ bar}$), $1\\text{ mol}$ của bất kì chất khí nào cũng chiếm một thể tích bằng bao nhiêu lít?", ["$24{,}79\\text{ lít}$", "$100\\text{ lít}$", "$1{,}00\\text{ lít}$", "$29{,}00\\text{ lít}$"], 0, "Theo chuẩn chương trình GDPT 2018, ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$), thể tích mol của chất khí là $24{,}79\\text{ L/mol}$."),
            mcq("biet", "Công thức tính tỉ khối của khí $A$ đối với không khí ($d_{A/\\text{kk}}$) là gì?", ["$d_{A/\\text{kk}} = \\dfrac{M_A}{29}$", "$d_{A/\\text{kk}} = \\dfrac{29}{M_A}$", "$d_{A/\\text{kk}} = \\dfrac{M_A}{24{,}79}$", "$d_{A/\\text{kk}} = 29 \\cdot M_A$"], 0, "Khối lượng mol trung bình của không khí là $29\\text{ g/mol}$, nên tỉ khối của khí $A$ đối với không khí là $d_{A/\\text{kk}} = \\dfrac{M_A}{29}$."),
            mcq("hieu", "Cho các chất khí sau: $\\text{H}_2$ ($M = 2$), $\\text{CH}_4$ ($M = 16$), $\\text{NH}_3$ ($M = 17$) và $\\text{CO}_2$ ($M = 44$). Chất khí nào **nặng hơn không khí** ($M_{\\text{kk}} = 29$)?", ["Khí $\\text{CO}_2$", "Khí $\\text{H}_2$", "Khí $\\text{CH}_4$", "Khí $\\text{NH}_3$"], 0, "Vì $M_{\\text{CO}_2} = 44 > 29$ nên khí $\\text{CO}_2$ nặng hơn không khí; các khí $\\text{H}_2, \\text{CH}_4, \\text{NH}_3$ đều có $M < 29$ nên nhẹ hơn không khí."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về mol và tỉ khối chất khí:", [
                "Một mol của bất kì chất nào cũng chứa $N_A = 6{,}022 \\cdot 10^{23}$ hạt vi mô (nguyên tử hoặc phân tử) của chất đó.",
                "Công thức tính khối lượng chất $m$ từ số mol $n$ và khối lượng mol $M$ là $m = n \\cdot M$.",
                "Ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$), $1\\text{ mol}$ khí $\\text{H}_2$ có thể tích nhỏ hơn $1\\text{ mol}$ khí $\\text{O}_2$.",
                "Khí sulfur dioxide ($\\text{SO}_2, M = 64\\text{ g/mol}$) nặng gấp $2$ lần khí oxygen ($\\text{O}_2, M = 32\\text{ g/mol}$).",
            ], [True, True, False, True], "Ý c) sai vì ở cùng điều kiện nhiệt độ và áp suất, $1\\text{ mol}$ của mọi chất khí đều chiếm thể tích bằng nhau ($24{,}79\\text{ lít}$ ở đkc)."),
            short("vandung", "Ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$), thể tích của $n = 0{,}5\\text{ mol}$ khí oxygen ($\\text{O}_2$) bằng bao nhiêu lít (lấy $1\\text{ mol}$ khí ở đkc bằng $24{,}79\\text{ lít}$)?", ["12,395", "12.395"], "Áp dụng công thức $V = 24{,}79 \\cdot n = 24{,}79 \\cdot 0{,}5 = 12{,}395\\text{ lít}$.", unit="lít"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 5: Dung dịch và nồng độ dung dịch",
        icon="🧪",
        description="Dung dịch bão hòa và chưa bão hòa, độ tan S, công thức nồng độ phần trăm C% = (m_ct/m_dd).100% và nồng độ mol C_M = n/V.",
        requirements=[
            "Phân biệt được dung dịch chưa bão hòa (vẫn có thể hòa tan thêm chất tan) và dung dịch bão hòa (không thể hòa tan thêm chất tan ở nhiệt độ đó); tính được độ tan $S = \\dfrac{m_{\\text{ct}}}{m_{\\text{nước}}} \\cdot 100$ ($\\text{g/100 g nước}$).",
            "Viết và vận dụng được công thức tính **nồng độ phần trăm**: $C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\%$ (với $m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}}$).",
            "Viết và vận dụng được công thức tính **nồng độ mol**: $C_M = \\dfrac{n}{V}$ (đơn vị $\\text{mol/L}$ hoặc $\\text{M}$, với $V$ đổi ra đơn vị **lít**).",
        ],
        definition="Nồng độ phần trăm ($C\\%$) cho biết số gam chất tan có trong $100\\text{ gam}$ dung dịch: $C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\%$. Nồng độ mol ($C_M$) cho biết số mol chất tan có trong $1\\text{ lít}$ dung dịch: $C_M = \\dfrac{n}{V}$ (đơn vị $\\text{mol/L}$ hay $\\text{M}$).",
        theory=(
            "### 1. Độ tan ($S$) của một chất trong nước\n"
            "- **Độ tan ($S$)**: số gam chất đó hòa tan tối đa trong $100\\text{ gam}$ nước để tạo thành dung dịch bão hòa ở một nhiệt độ xác định:\n"
            "  $$S = \\dfrac{m_{\\text{ct}}}{m_{\\text{H}_2\\text{O}}} \\cdot 100 \\quad (\\text{g/100 g H}_2\\text{O})$$\n"
            "- Độ tan của hầu hết chất rắn **tăng khi nhiệt độ tăng**; ngược lại độ tan của các chất khí **tăng khi nhiệt độ giảm và áp suất tăng**.\n\n"
            "### 2. Nồng độ phần trăm ($C\\%$) và Nồng độ mol ($C_M$)\n"
            "1. **Nồng độ phần trăm ($C\\%$)**:\n"
            "   $$C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\% \\iff m_{\\text{ct}} = \\dfrac{C\\% \\cdot m_{\\text{dd}}}{100\\%}; \\qquad m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}} = V_{\\text{dd}}(\\text{mL}) \\cdot D(\\text{g/mL})$$\n"
            "2. **Nồng độ mol ($C_M$)**:\n"
            "   $$C_M = \\dfrac{n}{V} \\iff n = C_M \\cdot V$$\n"
            "   *(Lưu ý bắt buộc: Thể tích dung dịch $V$ trong công thức $C_M = \\dfrac{n}{V}$ phải đổi ra đơn vị **lít ($\\text{L}$)**, với $1\\text{ L} = 1000\\text{ mL}$!)*\n"
            "3. **Pha loãng dung dịch bằng nước**: số mol và khối lượng chất tan không đổi ($n_1 = n_2 \\iff C_{M1}V_1 = C_{M2}V_2$; $m_{\\text{ct}1} = m_{\\text{ct}2} \\iff m_{\\text{dd}1}C_1\\% = m_{\\text{dd}2}C_2\\%$)."
        ),
        formulas=[
            G(
                "Độ tan (S), Nồng độ phần trăm (C%) và Nồng độ mol (C_M)",
                F("Độ tan và Nồng độ phần trăm", "$S = \\dfrac{m_{\\text{ct}}}{m_{\\text{nước}}} \\cdot 100; \\qquad C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\% \\implies m_{\\text{ct}} = \\dfrac{C\\% \\cdot m_{\\text{dd}}}{100\\%}$", "Liên hệ giữa độ tan $S$ và nồng độ phần trăm của dung dịch bão hòa: $C\\%_{\\text{bão hòa}} = \\dfrac{S}{100 + S} \\cdot 100\\%$."),
                F("Nồng độ mol của dung dịch", "$C_M = \\dfrac{n}{V(\\text{L})} \\implies n = C_M \\cdot V(\\text{L}); \\qquad 1\\text{ mL} = 10^{-3}\\text{ L}$", "Đơn vị của $C_M$ là $\\text{mol/L}$ hoặc viết tắt là $\\text{M}$ (ví dụ dung dịch $\\text{HCl } 2\\text{ M}$)."),
            )
        ],
        example="Hòa tan hoàn toàn $20\\text{ g}$ muối copper(II) sulfate ($\\text{CuSO}_4$, có $M = 160\\text{ g/mol}$) vào $180\\text{ g}$ nước thu được dung dịch có thể tích $V = 200\\text{ mL} = 0{,}2\\text{ L}$. Hãy tính nồng độ phần trăm ($C\\%$) và nồng độ mol ($C_M$) của dung dịch $\\text{CuSO}_4$ thu được.",
        example_answer="- Khối lượng dung dịch là $m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}} = 20 + 180 = 200\\text{ g}$. **Nồng độ phần trăm** là $C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\% = \\dfrac{20}{200} \\cdot 100\\% = 10\\%$.\n- Số mol $\\text{CuSO}_4$ là $n = \\dfrac{m_{\\text{ct}}}{M} = \\dfrac{20}{160} = 0{,}125\\text{ mol}$. Đổi $V = 200\\text{ mL} = 0{,}2\\text{ L}$. **Nồng độ mol** là $C_M = \\dfrac{n}{V} = \\dfrac{0{,}125}{0{,}2} = 0{,}625\\text{ M}$.",
        real_life="Nước muối sinh lí dùng nhỏ mắt và tiêm truyền có nồng độ phần trăm chính xác $C\\% = 0{,}9\\%$ (tức trong $100\\text{ g}$ dung dịch có đúng $0{,}9\\text{ g}$ $\\text{NaCl}$ và $99{,}1\\text{ g}$ nước cất); giấm ăn trong bếp là dung dịch acetic acid có nồng độ khoảng $2\\% - 5\\%$.",
        quiz=[
            mcq("biet", "Công thức tính **nồng độ phần trăm** ($C\\%$) của một dung dịch theo khối lượng chất tan ($m_{\\text{ct}}$) và khối lượng dung dịch ($m_{\\text{dd}}$) là gì?", ["$C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\%$", "$C\\% = \\dfrac{m_{\\text{dd}}}{m_{\\text{ct}}} \\cdot 100\\%$", "$C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{nước}}} \\cdot 100\\%$", "$C\\% = \\dfrac{n}{V}$"], 0, "Nồng độ phần trăm bằng tỉ số phần trăm giữa khối lượng chất tan và khối lượng dung dịch: $C\\% = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\%$."),
            mcq("biet", "Công thức tính **nồng độ mol** ($C_M$, đơn vị $\\text{mol/L}$ hoặc $\\text{M}$) của một dung dịch có $n$ mol chất tan trong $V$ lít dung dịch là gì?", ["$C_M = \\dfrac{n}{V}$", "$C_M = n \\cdot V$", "$C_M = \\dfrac{V}{n}$", "$C_M = \\dfrac{m_{\\text{ct}}}{m_{\\text{dd}}} \\cdot 100\\%$"], 0, "Nồng độ mol bằng số mol chất tan chia cho thể tích dung dịch (tính bằng lít): $C_M = \\dfrac{n}{V}$."),
            mcq("hieu", "Trong $400\\text{ mL}$ ($0{,}4\\text{ lít}$) dung dịch sodium hydroxide ($\\text{NaOH}$) có hòa tan $0{,}2\\text{ mol}$ $\\text{NaOH}$. Nồng độ mol ($C_M$) của dung dịch này bằng bao nhiêu?", ["$0{,}5\\text{ M}$", "$2{,}0\\text{ M}$", "$0{,}08\\text{ M}$", "$0{,}0005\\text{ M}$"], 0, "Đổi $V = 400\\text{ mL} = 0{,}4\\text{ L}$. Ta có $C_M = \\dfrac{n}{V} = \\dfrac{0{,}2}{0{,}4} = 0{,}5\\text{ M}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về độ tan và nồng độ dung dịch:", [
                "Dung dịch bão hòa là dung dịch không thể hòa tan thêm chất tan ở nhiệt độ đang xét.",
                "Độ tan của hầu hết các chất rắn trong nước tăng khi nhiệt độ tăng, còn độ tan của chất khí tăng khi nhiệt độ giảm và áp suất tăng.",
                "Khi hòa tan $10\\text{ g}$ đường vào $100\\text{ g}$ nước thì nồng độ phần trăm của dung dịch thu được là $10\\%$.",
                "Muốn pha chế $500\\text{ g}$ dung dịch nước muối $\\text{NaCl } 0{,}9\\%$, ta cần cân $4{,}5\\text{ g}$ $\\text{NaCl}$ và $495{,}5\\text{ g}$ nước cất.",
            ], [True, True, False, True], "Ý c) sai vì khối lượng dung dịch là $m_{\\text{dd}} = 10 + 100 = 110\\text{ g}$, nên $C\\% = \\dfrac{10}{110} \\cdot 100\\% \\approx 9{,}09\\% \ne 10\\%$."),
            short("vandung", "Hòa tan hoàn toàn $15\\text{ g}$ đường vào $85\\text{ g}$ nước. Nồng độ phần trăm ($C\\%$) của dung dịch nước đường thu được bằng bao nhiêu phần trăm ($\\%$)?", ["15"], "Khối lượng dung dịch là $m_{\\text{dd}} = 15 + 85 = 100\\text{ g}$. Nồng độ phần trăm là $C\\% = \\dfrac{15}{100} \\cdot 100\\% = 15\\%$.", unit="%"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 6: Định luật bảo toàn khối lượng và phương trình hóa học",
        icon="⚖️",
        description="Phát biểu và công thức Định luật bảo toàn khối lượng (Lomonosov – Lavoisier), nguyên tắc và các bước lập phương trình hóa học.",
        requirements=[
            "Phát biểu và viết được công thức của **Định luật bảo toàn khối lượng**: trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng.",
            "Giải thích được cơ sở của định luật bảo toàn khối lượng dựa vào sự bảo toàn số lượng nguyên tử mỗi nguyên tố.",
            "Thực hiện thành thạo 3 bước lập và cân bằng phương trình hóa học, xác định tỉ lệ số nguyên tử/số phân tử (cũng là tỉ lệ số mol) giữa các chất trong phương trình.",
        ],
        definition="Định luật bảo toàn khối lượng: Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng ($\\sum m_{\\text{tham gia}} = \\sum m_{\\text{sản phẩm}}$). Phương trình hóa học biểu diễn ngắn gọn phản ứng hóa học bằng công thức hóa học của các chất phản ứng và sản phẩm với các hệ số cân bằng thích hợp.",
        theory=(
            "### 1. Định luật bảo toàn khối lượng (Lomonosov – Lavoisier)\n"
            "- **Giải thích**: Trong phản ứng hóa học, số nguyên tử của mỗi nguyên tố trước và sau phản ứng không đổi và khối lượng mỗi nguyên tử không đổi, nên tổng khối lượng các chất được bảo toàn.\n"
            "- **Biểu thức** cho phản ứng $A + B \\longrightarrow C + D$:\n"
            "  $$m_A + m_B = m_C + m_D$$\n"
            "  *(Lưu ý: chỉ tính khối lượng phần chất **thực sự đã tham gia phản ứng**, không tính phần chất còn dư; nếu có chất khí thoát ra hoặc kết tủa thì vẫn phải cộng cả khối lượng khí/kết tủa vào vế sản phẩm!)*\n\n"
            "### 2. Lập Phương trình hóa học (PTHH) và Ý nghĩa\n"
            "- **Ba bước lập PTHH**:\n"
            "  1. Viết sơ đồ phản ứng bằng công thức hóa học đúng của các chất phản ứng và sản phẩm.\n"
            "  2. **Cân bằng số nguyên tử** của mỗi nguyên tố ở hai vế bằng cách điền các **hệ số nguyên dương tối giản** trước công thức hóa học (*tuyệt đối không được tự ý sửa các chỉ số nhỏ ở chân công thức!*).\n"
            "  3. Viết thành phương trình hóa học hoàn chỉnh (thay nét đứt bằng mũi tên liền $\\longrightarrow$).\n"
            "- **Ý nghĩa của PTHH**: Cho biết **tỉ lệ số nguyên tử, số phân tử** (và cũng chính là **tỉ lệ số mol**) giữa các chất trong phản ứng."
        ),
        formulas=[
            G(
                "Định luật bảo toàn khối lượng và Quy tắc cân bằng PTHH",
                F("Biểu thức Định luật bảo toàn khối lượng cho A + B ➔ C + D", "$m_A + m_B = m_C + m_D \\implies m_A = (m_C + m_D) - m_B$", "Biết khối lượng của $(n - 1)$ chất trong phản ứng gồm $n$ chất, ta luôn tính được khối lượng chất còn lại."),
                F("Ý nghĩa hệ số cân bằng của PTHH aA + bB ➔ cC + dD", "$\\text{Tỉ lệ số hạt (hoặc số mol)}: \\quad n_A : n_B : n_C : n_D = a : b : c : d$", "Ví dụ: $4\\text{Al} + 3\\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{Al}_2\\text{O}_3 \\implies n_{\\text{Al}} : n_{\\text{O}_2} : n_{\\text{Al}_2\\text{O}_3} = 4 : 3 : 2$."),
            )
        ],
        example="Nung nóng hoàn toàn $m\\text{ gam}$ đá vôi ($\\text{CaCO}_3$) thu được $11{,}2\\text{ g}$ vôi sống ($\\text{CaO}$) và $8{,}8\\text{ g}$ khí carbon dioxide ($\\text{CO}_2$) thoát ra. Hãy: (a) Viết phương trình hóa học của phản ứng; (b) Áp dụng định luật bảo toàn khối lượng để tính khối lượng $m$ của đá vôi đã đem nung.",
        example_answer="- (a) Phương trình hóa học (đã tự cân bằng $1:1:1$): $\\text{CaCO}_3 \\xrightarrow{t^\\circ} \\text{CaO} + \\text{CO}_2\\uparrow$.\n- (b) Theo định luật bảo toàn khối lượng: $m_{\\text{CaCO}_3} = m_{\\text{CaO}} + m_{\\text{CO}_2} = 11{,}2 + 8{,}8 = 20\\text{ g}$.",
        real_life="Trong lò nung vôi công nghiệp, khi nung đá vôi thấy khối lượng chất rắn thu được (vôi sống $\\text{CaO}$) nhẹ hơn đá vôi ban đầu không phải vì định luật bảo toàn khối lượng sai, mà vì một phần khối lượng đã chuyển thành khí $\\text{CO}_2$ bay ra không khí.",
        quiz=[
            mcq("biet", "Cho phản ứng hóa học có dạng: $A + B \\longrightarrow C + D$. Biểu thức nào sau đây thể hiện đúng **Định luật bảo toàn khối lượng**?", ["$m_A + m_B = m_C + m_D$", "$m_A - m_B = m_C - m_D$", "$m_A \\cdot m_B = m_C \\cdot m_D$", "$m_A + m_C = m_B + m_D$"], 0, "Tổng khối lượng các chất tham gia phản ứng bằng tổng khối lượng các chất sản phẩm: $m_A + m_B = m_C + m_D$."),
            mcq("biet", "Sau khi cân bằng phương trình hóa học: $x\\text{Fe} + y\\text{O}_2 \\xrightarrow{t^\\circ} z\\text{Fe}_3\\text{O}_4$ với bộ hệ số nguyên dương tối giản, các hệ số $(x, y, z)$ lần lượt là:", ["$3, 2, 1$", "$1, 1, 1$", "$2, 3, 1$", "$3, 4, 1$"], 0, "Trong $\\text{Fe}_3\\text{O}_4$ có $3\\text{Fe}$ và $4\\text{O}$, nên đặt $x = 3$ trước $\\text{Fe}$, $y = 2$ trước $\\text{O}_2$ và $z = 1$ trước $\\text{Fe}_3\\text{O}_4$: $3\\text{Fe} + 2\\text{O}_2 \\xrightarrow{t^\\circ} \\text{Fe}_3\\text{O}_4$."),
            mcq("hieu", "Khi đốt cháy một mẩu dây kim loại magnesium ($\\text{Mg}$) trong không khí, người ta đem cân sản phẩm rắn thu được là bột trắng magnesium oxide ($\\text{MgO}$) thì thấy nặng hơn mẩu dây $\\text{Mg}$ ban đầu. Giải thích nào sau đây là đúng?", ["Vì theo định luật bảo toàn khối lượng, $m_{\\text{MgO}} = m_{\\text{Mg}} + m_{\\text{O}_2}$, khối lượng tăng thêm chính là khối lượng khí oxygen đã tham gia phản ứng", "Vì định luật bảo toàn khối lượng không đúng khi đốt kim loại", "Vì các nguyên tử $\\text{Mg}$ tự sinh thêm ra từ hư không", "Vì ánh sáng của ngọn lửa biến thành khối lượng"], 0, "Phản ứng $2\\text{Mg} + \\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{MgO}$ có khí $\\text{O}_2$ từ không khí kết hợp vào $\\text{Mg}$, nên $m_{\\text{MgO}} = m_{\\text{Mg}} + m_{\\text{O}_2} > m_{\\text{Mg}}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về định luật bảo toàn khối lượng và phương trình hóa học:", [
                "Khi cân bằng phương trình hóa học, ta chỉ được phép điền hệ số ở phía trước công thức hóa học chứ tuyệt đối không được thay đổi các chỉ số ở chân công thức.",
                "Trong phương trình $2\\text{H}_2 + \\text{O}_2 \\xrightarrow{t^\\circ} 2\\text{H}_2\\text{O}$, tỉ lệ số phân tử $\\text{H}_2 : \\text{O}_2 : \\text{H}_2\\text{O}$ là $2 : 1 : 2$.",
                "Nếu tổng số phân tử ở hai vế thay đổi thì tổng khối lượng các chất cũng thay đổi.",
                "Cho $5{,}6\\text{ g}$ sắt ($\\text{Fe}$) tác dụng vừa đủ với $3{,}2\\text{ g}$ lưu huỳnh ($\\text{S}$) khi đun nóng thì thu được $8{,}8\\text{ g}$ $\\text{FeS}$.",
            ], [True, True, False, True], "Ý c) sai vì số phân tử có thể thay đổi nhưng số nguyên tử mỗi nguyên tố luôn bảo toàn, nên tổng khối lượng luôn bảo toàn."),
            short("vandung", "Đốt cháy hoàn toàn $4{,}8\\text{ g}$ kim loại magnesium ($\\text{Mg}$) trong khí oxygen ($\\text{O}_2$) thu được $8{,}0\\text{ g}$ magnesium oxide ($\\text{MgO}$). Khối lượng khí oxygen đã tham gia phản ứng bằng bao nhiêu gam ($\\text{g}$)?", ["3,2", "3.2"], "Theo định luật bảo toàn khối lượng: $m_{\\text{O}_2} = m_{\\text{MgO}} - m_{\\text{Mg}} = 8{,}0 - 4{,}8 = 3{,}2\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 7: Tính theo phương trình hóa học và hiệu suất phản ứng",
        icon="🧮",
        description="Quy trình 4 bước giải bài toán tính theo phương trình hóa học (số mol, khối lượng, thể tích khí đkc) và công thức tính hiệu suất phản ứng H%.",
        requirements=[
            "Thực hiện thành thạo 4 bước tính theo phương trình hóa học: (1) Viết và cân bằng PTHH; (2) Đổi dữ kiện đề bài ra số mol ($n$); (3) Dựa vào tỉ lệ hệ số PTHH để tìm số mol các chất cần tính; (4) Tính khối lượng ($m = nM$), thể tích khí ở đkc ($V = 24{,}79n$) hoặc nồng độ.",
            "Định nghĩa được hiệu suất phản ứng ($H\\%$) và giải thích vì sao trong thực tế hầu hết các phản ứng có hiệu suất nhỏ hơn $100\\%$.",
            "Vận dụng được công thức tính hiệu suất: $H\\% = \\dfrac{n_{\\text{thực tế}}}{n_{\\text{lí thuyết}}} \\cdot 100\\% = \\dfrac{m_{\\text{thực tế}}}{m_{\\text{lí thuyết}}} \\cdot 100\\%$.",
        ],
        definition="Dựa vào phương trình hóa học đã cân bằng, khi biết số mol của một chất bất kì tham gia hoặc tạo thành, ta tính được số mol, khối lượng và thể tích của tất cả các chất còn lại. Hiệu suất phản ứng ($H\\%$) là tỉ số phần trăm giữa lượng sản phẩm thu được theo thực tế và lượng sản phẩm thu được theo lí thuyết: $H\\% = \\dfrac{m_{\\text{tt}}}{m_{\\text{lt}}} \\cdot 100\\% = \\dfrac{n_{\\text{tt}}}{n_{\\text{lt}}} \\cdot 100\\%$.",
        theory=(
            "### 1. Quy trình 4 bước giải bài toán tính theo Phương trình hóa học\n"
            "1. **Bước 1**: Viết và cân bằng đúng phương trình hóa học: $aA + bB \\longrightarrow cC + dD$.\n"
            "2. **Bước 2**: Đổi lượng chất đã biết từ đề bài ra **số mol ($n$)**: $n = \\dfrac{m}{M} = \\dfrac{V_{\\text{đkc}}}{24{,}79} = C_M \\cdot V_{\\text{dd}}$.\n"
            "3. **Bước 3**: Dựa vào tỉ lệ hệ số trên PTHH để suy ra số mol các chất cần tìm:\n"
            "   $$\\dfrac{n_A}{a} = \\dfrac{n_B}{b} = \\dfrac{n_C}{c} = \\dfrac{n_D}{d}$$\n"
            "   *(Nếu đề bài cho biết số mol của cả 2 chất tham gia $n_A, n_B$, ta so sánh $\\dfrac{n_A}{a}$ và $\\dfrac{n_B}{b}$: tỉ số nào nhỏ hơn thì chất đó phản ứng hết và tính theo chất phản ứng hết)*.\n"
            "4. **Bước 4**: Chuyển đổi số mol vừa tìm được sang khối lượng ($m = nM$) hoặc thể tích khí ở đkc ($V = 24{,}79n$) theo yêu cầu đề bài.\n\n"
            "### 2. Hiệu suất của phản ứng hóa học ($H\\%$)\n"
            "- Trong thực tế, do phản ứng xảy ra không hoàn toàn hoặc thất thoát trong quá trình thu hồi nên lượng sản phẩm thực tế ($m_{\\text{tt}}, n_{\\text{tt}}$) thường nhỏ hơn lượng tính theo lí thuyết PTHH ($m_{\\text{lt}}, n_{\\text{lt}}$):\n"
            "  $$H\\% = \\dfrac{m_{\\text{sp thực tế}}}{m_{\\text{sp lí thuyết}}} \\cdot 100\\% = \\dfrac{n_{\\text{sp thực tế}}}{n_{\\text{sp lí thuyết}}} \\cdot 100\\% = \\dfrac{m_{\\text{tham gia đã phản ứng}}}{m_{\\text{tham gia ban đầu}}} \\cdot 100\\%$$"
        ),
        formulas=[
            G(
                "Tỉ lệ số mol trên PTHH và Công thức Hiệu suất phản ứng (H%)",
                F("Quy tắc nhân chéo chia ngang trên PTHH aA + bB ➔ cC + dD", "$\\dfrac{n_A}{a} = \\dfrac{n_B}{b} = \\dfrac{n_C}{c} = \\dfrac{n_D}{d} \\implies n_C = n_A \\cdot \\dfrac{c}{a}$", "Sau khi có số mol $n_C$, tính khối lượng $m_C = n_C \\cdot M_C$ hoặc thể tích khí đkc $V_C = 24{,}79 \\cdot n_C$."),
                F("Công thức tính Hiệu suất phản ứng (H%)", "$H\\% = \\dfrac{m_{\\text{tt}}}{m_{\\text{lt}}} \\cdot 100\\% = \\dfrac{n_{\\text{tt}}}{n_{\\text{lt}}} \\cdot 100\\% \\implies m_{\\text{sp thực tế}} = m_{\\text{sp lí thuyết}} \\cdot \\dfrac{H\\%}{100\\%}$", "Mẹo nhớ nhanh: **Phải nhân – Trái chia** (tính lượng sản phẩm bên phải mũi tên thì nhân với $H\\%$; tính lượng nguyên liệu ban đầu bên trái mũi tên cần dùng thì chia cho $H\\%$)."),
            )
        ],
        example="Cho $6{,}5\\text{ g}$ kim loại kẽm ($\\text{Zn} = 65$) tác dụng hết với dung dịch hydrochloric acid ($\\text{HCl}$) dư theo phương trình: $\\text{Zn} + 2\\text{HCl} \\longrightarrow \\text{ZnCl}_2 + \\text{H}_2\\uparrow$. Hãy tính số mol $\\text{HCl}$ đã phản ứng và thể tích khí $\\text{H}_2$ thu được ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$).",
        example_answer="Số mol $\\text{Zn}$ là $n_{\\text{Zn}} = \\dfrac{6{,}5}{65} = 0{,}1\\text{ mol}$. Theo tỉ lệ hệ số phương trình hóa học ($1 : 2 : 1 : 1$), ta có: số mol $\\text{HCl}$ phản ứng là $n_{\\text{HCl}} = 2 \\cdot n_{\\text{Zn}} = 0{,}2\\text{ mol}$; số mol khí $\\text{H}_2$ sinh ra là $n_{\\text{H}_2} = n_{\\text{Zn}} = 0{,}1\\text{ mol}$. Thể tích khí $\\text{H}_2$ ở đkc là $V_{\\text{H}_2} = 24{,}79 \\cdot 0{,}1 = 2{,}479\\text{ lít}$.",
        real_life="Trong các nhà máy sản xuất ammonia ($\\text{NH}_3$), sulfuric acid ($\\text{H}_2\\text{SO}_4$) và xi măng, các kĩ sư hóa học luôn phải tính toán hiệu suất phản ứng $H\\%$ ở từng công đoạn để xác định chính xác khối lượng quặng nguyên liệu cần nhập vào.",
        quiz=[
            mcq("biet", "Cho phương trình hóa học đã cân bằng: $\\text{N}_2 + 3\\text{H}_2 \\xrightarrow{t^\\circ, p, xt} 2\\text{NH}_3$. Nếu có $1\\text{ mol}$ khí $\\text{N}_2$ phản ứng hoàn toàn thì số mol khí $\\text{H}_2$ đã phản ứng và số mol khí $\\text{NH}_3$ tạo thành theo lí thuyết lần lượt là:", ["$3\\text{ mol } \\text{H}_2$ và $2\\text{ mol } \\text{NH}_3$", "$1\\text{ mol } \\text{H}_2$ và $1\\text{ mol } \\text{NH}_3$", "$2\\text{ mol } \\text{H}_2$ và $3\\text{ mol } \\text{NH}_3$", "$3\\text{ mol } \\text{H}_2$ và $1\\text{ mol } \\text{NH}_3$"], 0, "Theo hệ số cân bằng của PTHH, tỉ lệ số mol là $n_{\\text{N}_2} : n_{\\text{H}_2} : n_{\\text{NH}_3} = 1 : 3 : 2$."),
            mcq("biet", "Gọi $m_{\\text{lt}}$ là khối lượng sản phẩm tính theo phương trình hóa học (lí thuyết) và $m_{\\text{tt}}$ là khối lượng sản phẩm thực tế thu được. Công thức tính **hiệu suất phản ứng** ($H\\%$) là gì?", ["$H\\% = \\dfrac{m_{\\text{tt}}}{m_{\\text{lt}}} \\cdot 100\\%$", "$H\\% = \\dfrac{m_{\\text{lt}}}{m_{\\text{tt}}} \\cdot 100\\%$", "$H\\% = (m_{\\text{lt}} - m_{\\text{tt}}) \\cdot 100\\%$", "$H\\% = (m_{\\text{lt}} + m_{\\text{tt}}) \\cdot 100\\%$"], 0, "Hiệu suất phản ứng bằng tỉ số phần trăm giữa lượng sản phẩm thực tế thu được và lượng sản phẩm tính theo lí thuyết: $H\\% = \\dfrac{m_{\\text{tt}}}{m_{\\text{lt}}} \\cdot 100\\%$."),
            mcq("hieu", "Đốt cháy hoàn toàn $0{,}2\\text{ mol}$ carbon ($\\text{C}$) trong khí oxygen dư theo phương trình $\\text{C} + \\text{O}_2 \\xrightarrow{t^\\circ} \\text{CO}_2$. Khối lượng khí $\\text{CO}_2$ ($M = 44\\text{ g/mol}$) thu được là bao nhiêu?", ["$8{,}8\\text{ g}$", "$4{,}4\\text{ g}$", "$44\\text{ g}$", "$2{,}2\\text{ g}$"], 0, "Theo PTHH: $n_{\\text{CO}_2} = n_{\\text{C}} = 0{,}2\\text{ mol} \\implies m_{\\text{CO}_2} = 0{,}2 \\cdot 44 = 8{,}8\\text{ g}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tính theo phương trình hóa học và hiệu suất:", [
                "Tỉ lệ các hệ số cân bằng trong phương trình hóa học chính là tỉ lệ số mol giữa các chất tham gia và tạo thành trong phản ứng.",
                "Trong thực tế, do phản ứng không hoàn toàn hoặc hao hụt khi thu hồi nên hiệu suất phản ứng thường nhỏ hơn $100\\%$.",
                "Nếu hiệu suất phản ứng đạt $100\\%$ thì phản ứng được coi là xảy ra hoàn toàn.",
                "Theo lí thuyết nung $100\\text{ g}$ $\\text{CaCO}_3$ thu được $56\\text{ g}$ $\\text{CaO}$, nhưng nếu hiệu suất phản ứng là $80\\%$ thì thực tế thu được $70\\text{ g}$ $\\text{CaO}$.",
            ], [True, True, True, False], "Ý d) sai vì với hiệu suất $H = 80\\%$, khối lượng $\\text{CaO}$ thực tế thu được là $m_{\\text{tt}} = 56 \\cdot 80\\% = 44{,}8\\text{ g}$."),
            short("vandung", "Theo lí thuyết tính từ phương trình hóa học, khi nung một lượng đá vôi sẽ thu được $m_{\\text{lt}} = 50\\text{ kg}$ vôi sống ($\\text{CaO}$). Nhưng trên thực tế do đá vôi chưa phân hủy hết nên chỉ thu được $m_{\\text{tt}} = 40\\text{ kg}$ vôi sống. Hiệu suất $H$ của phản ứng nung vôi bằng bao nhiêu phần trăm ($\\%$)?", ["80"], "Áp dụng công thức $H\\% = \\dfrac{m_{\\text{tt}}}{m_{\\text{lt}}} \\cdot 100\\% = \\dfrac{40}{50} \\cdot 100\\% = 80\\%$.", unit="%"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 8: Tốc độ phản ứng và chất xúc tác",
        icon="⏱️",
        description="Khái niệm tốc độ phản ứng hóa học và 5 yếu tố ảnh hưởng đến tốc độ phản ứng (nồng độ, nhiệt độ, áp suất, diện tích bề mặt tiếp xúc và chất xúc tác).",
        requirements=[
            "Nêu được khái niệm tốc độ phản ứng là đại lượng chỉ mức độ nhanh hay chậm của một phản ứng hóa học.",
            "Trình bày và giải thích được ảnh hưởng của các yếu tố đến tốc độ phản ứng: nồng độ chất phản ứng, nhiệt độ, diện tích bề mặt tiếp xúc của chất rắn (và áp suất đối với chất khí).",
            "Nêu được vai trò của **chất xúc tác** (làm tăng tốc độ phản ứng nhưng vẫn giữ nguyên về lượng và bản chất hóa học sau khi phản ứng kết thúc; các xúc tác sinh học gọi là enzyme).",
        ],
        definition="Tốc độ phản ứng là đại lượng đặc trưng cho sự diễn ra nhanh hay chậm của một phản ứng hóa học. Các yếu tố làm tăng tốc độ phản ứng gồm: tăng nồng độ chất phản ứng, tăng nhiệt độ, tăng áp suất (với chất khí), tăng diện tích bề mặt tiếp xúc (với chất rắn) và sử dụng chất xúc tác.",
        theory=(
            "### 1. Khái niệm Tốc độ phản ứng\n"
            "- Trong thực tế, có những phản ứng xảy ra **rất nhanh** (đốt thuốc nổ, pháo hoa, phản ứng tạo kết tủa trong dung dịch) và có những phản ứng xảy ra **rất chậm** (sắt bị gỉ trong không khí, quá trình lên men rượu, phong hóa đá).\n"
            "- Để đánh giá mức độ nhanh hay chậm của phản ứng, người ta dùng khái niệm **tốc độ phản ứng** (đo bằng độ biến thiên nồng độ của một chất trong một đơn vị thời gian).\n\n"
            "### 2. Năm yếu tố ảnh hưởng đến tốc độ phản ứng\n"
            "1. **Nồng độ**: Khi **tăng nồng độ** chất phản ứng (trong dung dịch hoặc khí), mật độ hạt tăng làm tần số va chạm hiệu quả tăng $\\implies$ **tốc độ phản ứng tăng** (ví dụ: than cháy trong bình khí oxygen nguyên chất sáng mãnh liệt hơn hẳn trong không khí).\n"
            "2. **Nhiệt độ**: Khi **tăng nhiệt độ**, các hạt chuyển động nhanh hơn và va chạm mạnh hơn $\\implies$ **tốc độ phản ứng tăng** (ngược lại bảo quản thực phẩm trong tủ lạnh làm giảm nhiệt độ để làm chậm phản ứng phân hủy).\n"
            "3. **Diện tích bề mặt tiếp xúc (với chất rắn)**: Đập nhỏ, nghiền mịn chất rắn làm **tăng diện tích bề mặt tiếp xúc** $\\implies$ **tốc độ phản ứng tăng** (đá vôi dạng bột tan trong dung dịch $\\text{HCl}$ nhanh hơn nhiều so với đá vôi dạng viên to).\n"
            "4. **Áp suất (với phản ứng có chất khí)**: Tăng áp suất chất khí tương đương với tăng nồng độ khí $\\implies$ tốc độ phản ứng tăng.\n"
            "5. **Chất xúc tác**: Chất làm **tăng tốc độ phản ứng** nhưng **không bị tiêu hao** (còn nguyên khối lượng và tính chất hóa học) sau khi phản ứng kết thúc (ví dụ: bột $\\text{MnO}_2$ xúc tác phân hủy $\\text{H}_2\\text{O}_2$ thành $\\text{H}_2\\text{O}$ và $\\text{O}_2$; **enzyme** là chất xúc tác sinh học)."
        ),
        formulas=[
            G(
                "Các quy luật làm thay đổi Tốc độ phản ứng và Chất xúc tác",
                F("Quy tắc làm TĂNG tốc độ phản ứng hóa học", "$\\text{Tăng } (C_{\\text{nồng độ}},\\ T_{\\text{nhiệt độ}},\\ p_{\\text{áp suất khí}},\\ S_{\\text{diện tích bề mặt rắn}}) + \\text{Thêm Chất xúc tác} \\implies v_{\\text{phản ứng}} \\text{ TĂNG}$", "Ngược lại, muốn kìm hãm phản ứng có hại (như ôi thiu thức ăn) thì phải **hạ nhiệt độ** (để tủ lạnh) hoặc dùng chất ức chế."),
                F("Đặc trưng của Chất xúc tác (ví dụ MnO₂ trong phân hủy H₂O₂)", "$2\\text{H}_2\\text{O}_2 \\xrightarrow{\\text{xt } \\text{MnO}_2} 2\\text{H}_2\\text{O} + \\text{O}_2\\uparrow; \\qquad m_{\\text{xúc tác sau PƯ}} = m_{\\text{xúc tác ban đầu}}$", "Chất xúc tác tham gia vào các giai đoạn trung gian làm tăng tốc độ phản ứng nhưng được hoàn trả nguyên vẹn sau phản ứng."),
            )
        ],
        example="Cho cùng $2\\text{ g}$ đá vôi ($\\text{CaCO}_3$) vào hai ống nghiệm chứa cùng một thể tích dung dịch hydrochloric acid ($\\text{HCl}$): ở ống nghiệm (1) dùng đá vôi dạng bột mịn và dung dịch $\\text{HCl } 2\\text{ M}$; ở ống nghiệm (2) dùng đá vôi dạng một viên nguyên khối và dung dịch $\\text{HCl } 0{,}5\\text{ M}$. Hãy cho biết ở ống nghiệm nào bọt khí $\\text{CO}_2$ thoát ra nhanh và mạnh hơn? Giải thích dựa trên các yếu tố ảnh hưởng đến tốc độ phản ứng.",
        example_answer="Ở **ống nghiệm (1)** bọt khí $\\text{CO}_2$ thoát ra nhanh và mạnh hơn hẳn vì cả hai yếu tố đều thuận lợi hơn: (1) Đá vôi dạng bột mịn có **diện tích bề mặt tiếp xúc lớn hơn** viên đá khối; (2) Dung dịch $\\text{HCl } 2\\text{ M}$ có **nồng độ lớn hơn** dung dịch $\\text{HCl } 0{,}5\\text{ M}$.",
        real_life="Nồi áp suất giúp hầm xương nhanh nhừ nhờ tăng áp suất và tăng nhiệt độ sôi của nước lên trên $100^\\circ\\text{C}$; men rượu (chứa enzyme sinh học) đóng vai trò chất xúc tác giúp chuyển hóa nhanh tinh bột và đường thành rượu etylic.",
        quiz=[
            mcq("biet", "Chất làm tăng tốc độ của một phản ứng hóa học nhưng vẫn giữ nguyên về khối lượng và bản chất hóa học sau khi phản ứng kết thúc được gọi là gì?", ["Chất xúc tác", "Chất phản ứng chính", "Chất sản phẩm", "Dung môi hòa tan"], 0, "Chất xúc tác làm tăng tốc độ phản ứng nhưng không bị tiêu hao sau khi phản ứng kết thúc."),
            mcq("biet", "Khi cho cùng một lượng kẽm hạt ($\\text{Zn}$) vào hai cốc đựng dung dịch hydrochloric acid ($\\text{HCl}$) có nồng độ lần lượt là $0{,}5\\text{ M}$ (cốc 1) và $2{,}0\\text{ M}$ (cốc 2) ở cùng nhiệt độ, hiện tượng nào xảy ra?", ["Tốc độ thoát khí $\\text{H}_2$ ở cốc 2 nhanh hơn ở cốc 1 do nồng độ acid lớn hơn", "Tốc độ thoát khí ở cốc 1 nhanh hơn ở cốc 2", "Tốc độ thoát khí ở hai cốc hoàn toàn như nhau", "Cả hai cốc đều không có phản ứng"], 0, "Khi nồng độ chất phản ứng tăng ($2{,}0\\text{ M} > 0{,}5\\text{ M}$) thì tốc độ phản ứng tăng."),
            mcq("hieu", "Vì sao khi muối dưa cải hoặc làm sữa chua vào mùa hè (trời ấm) thì dưa cải và sữa chua nhanh chua hơn vào mùa đông (trời lạnh)?", ["Vì nhiệt độ mùa hè cao hơn làm tăng tốc độ phản ứng lên men lactic của vi khuẩn", "Vì mùa hè nồng độ muối bằng không", "Vì mùa đông không có khí oxygen", "Vì nhiệt độ tăng làm giảm tốc độ phản ứng"], 0, "Nhiệt độ tăng làm tăng tốc độ của các phản ứng hóa học và sinh hóa (lên men chua)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tốc độ phản ứng và chất xúc tác:", [
                "Đập nhỏ đá vôi trước khi đưa vào lò nung vôi giúp làm tăng diện tích bề mặt tiếp xúc, từ đó tăng tốc độ phản ứng phân hủy.",
                "Bảo quản thực phẩm trong ngăn mát hoặc ngăn đông tủ lạnh là ứng dụng yếu tố giảm nhiệt độ để làm chậm tốc độ phản ứng phân hủy thức ăn.",
                "Sau khi phản ứng phân hủy $\\text{H}_2\\text{O}_2$ có xúc tác $\\text{MnO}_2$ kết thúc hoàn toàn, lượng bột $\\text{MnO}_2$ bị mất đi một nửa khối lượng.",
                "Các enzyme (như amylase trong nước bọt, pepsin trong dạ dày) là các chất xúc tác sinh học giúp tiêu hóa nhanh thức ăn ở nhiệt độ cơ thể $37^\\circ\\text{C}$.",
            ], [True, True, False, True], "Ý c) sai vì $\\text{MnO}_2$ là chất xúc tác nên khối lượng của nó sau phản ứng vẫn giữ nguyên không đổi."),
            short("vandung", "Người ta thêm $0{,}5\\text{ g}$ bột $\\text{MnO}_2$ làm chất xúc tác vào ống nghiệm chứa dung dịch $\\text{H}_2\\text{O}_2$ để phân hủy tạo khí $\\text{O}_2$. Sau khi phản ứng kết thúc hoàn toàn, nếu lọc tách và làm khô phần bột $\\text{MnO}_2$ thì thu lại được bao nhiêu gam ($\\text{g}$) $\\text{MnO}_2$?", ["0,5", "0.5"], "Vì chất xúc tác không bị tiêu hao trong phản ứng nên khối lượng $\\text{MnO}_2$ thu lại sau phản ứng vẫn đúng bằng $0{,}5\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 9: Acid",
        icon="🍋",
        description="Khái niệm Acid (phân li ra ion H⁺ trong nước), công thức các acid thông dụng (HCl, H₂SO₄, HNO₃, CH₃COOH) và tính chất hóa học của acid (đổi màu quỳ tím thành đỏ, tác dụng với kim loại).",
        requirements=[
            "Định nghĩa được **Acid** là những hợp chất trong phân tử có nguyên tử hydrogen ($\\text{H}$) liên kết với gốc acid; khi tan trong nước, acid tạo ra **ion $\\text{H}^+$**.",
            "Viết đúng công thức hóa học và đọc tên chuẩn IUPAC của các acid quan trọng: hydrochloric acid ($\\text{HCl}$), sulfuric acid ($\\text{H}_2\\text{SO}_4$), nitric acid ($\\text{HNO}_3$), carbonic acid ($\\text{H}_2\\text{CO}_3$), phosphoric acid ($\\text{H}_3\\text{PO}_4$), acetic acid ($\\text{CH}_3\\text{COOH}$).",
            "Trình bày và viết được phương trình hóa học minh họa tính chất của dung dịch acid: làm đổi màu **giấy quỳ tím thành đỏ** và tác dụng với các kim loại hoạt động đứng trước $\\text{H}$ ($\\text{Mg}, \\text{Al}, \\text{Zn}, \\text{Fe}$) giải phóng khí $\\text{H}_2$.",
        ],
        definition="Acid là những hợp chất trong phân tử có nguyên tử hydrogen ($\\text{H}$) liên kết với gốc acid. Khi tan trong nước, các acid phân li tạo ra các ion dương $\\text{H}^+$ (chính ion $\\text{H}^+$ quyết định các tính chất hóa học đặc trưng của dung dịch acid).",
        theory=(
            "### 1. Khái niệm, Công thức và Tên gọi của một số Acid\n"
            "- Công thức chung của acid vô cơ: $\\text{H}_n A$ (trong đó $n$ là số nguyên tử $\\text{H}$ có khả năng phân li ra $\\text{H}^+$, cũng bằng hóa trị của gốc acid $A$):\n"
            "  - $\\text{HCl} \\longrightarrow \\text{H}^+ + \\text{Cl}^-$: **Hydrochloric acid** (gốc $-\\text{Cl}$: chloride, hóa trị $\\text{I}$).\n"
            "  - $\\text{H}_2\\text{SO}_4 \\longrightarrow 2\\text{H}^+ + \\text{SO}_4^{2-}$: **Sulfuric acid** (gốc $=\\text{SO}_4$: sulfate, hóa trị $\\text{II}$).\n"
            "  - $\\text{HNO}_3 \\longrightarrow \\text{H}^+ + \\text{NO}_3^-$: **Nitric acid** (gốc $-\\text{NO}_3$: nitrate, hóa trị $\\text{I}$).\n"
            "  - $\\text{H}_3\\text{PO}_4$: **Phosphoric acid** (gốc $\\equiv\\text{PO}_4$: phosphate, hóa trị $\\text{III}$).\n"
            "  - $\\text{CH}_3\\text{COOH} \\rightleftharpoons \\text{H}^+ + \\text{CH}_3\\text{COO}^-$: **Acetic acid** (có trong giấm ăn, gốc $\\text{CH}_3\\text{COO}-$: acetate, hóa trị $\\text{I}$).\n\n"
            "### 2. Tính chất hóa học cơ bản của Dung dịch Acid\n"
            "1. **Tác dụng với chất chỉ thị màu**: Dung dịch acid làm **đổi màu giấy quỳ tím thành màu đỏ (hoặc hồng)**; không làm đổi màu dung dịch phenolphthalein.\n"
            "2. **Tác dụng với kim loại hoạt động** (đứng trước $\\text{H}$ như $\\text{Mg}, \\text{Al}, \\text{Zn}, \\text{Fe}$; **không** tác dụng với $\\text{Cu}, \\text{Ag}, \\text{Au}$ đối với $\\text{HCl}$ và $\\text{H}_2\\text{SO}_4$ loãng):\n"
            "   $$\\text{Kim loại (Mg, Al, Zn, Fe)} + \\text{Acid (HCl, H}_2\\text{SO}_4\\text{ loãng)} \\longrightarrow \\text{Muối} + \\text{H}_2\\uparrow$$\n"
            "   *(Lưu ý cực kì quan trọng: Khi sắt $\\text{Fe}$ tác dụng với dung dịch $\\text{HCl}$ hoặc $\\text{H}_2\\text{SO}_4$ loãng chỉ tạo ra muối **iron(II)** là $\\text{FeCl}_2$ hoặc $\\text{FeSO}_4$, không tạo muối $\\text{Fe(III)}$!)*"
        ),
        formulas=[
            G(
                "Sự phân li ion H⁺ và Phương trình phản ứng của Acid với Kim loại",
                F("Sự phân li tạo ion H⁺ và Chỉ thị màu", "$\\text{H}_n A \\xrightarrow{\\text{H}_2\\text{O}} n\\text{H}^+ + A^{n-}; \\qquad \\text{Dung dịch Acid} + \\text{Quỳ tím} \\longrightarrow \\text{Màu ĐỎ}$", "Dung dịch acid không làm đổi màu phenolphthalein."),
                F("Các phương trình kim loại tác dụng với HCl và H₂SO₄ loãng", "$\\text{Mg} + 2\\text{HCl} \\to \\text{MgCl}_2 + \\text{H}_2\\uparrow; \\quad \\text{Fe} + \\text{H}_2\\text{SO}_4\\text{(loãng)} \\to \\text{FeSO}_4 + \\text{H}_2\\uparrow; \\quad 2\\text{Al} + 6\\text{HCl} \\to 2\\text{AlCl}_3 + 3\\text{H}_2\\uparrow$", "Kim loại Copper ($\\text{Cu}$) và Silver ($\\text{Ag}$) **không** phản ứng với dung dịch $\\text{HCl}$ và $\\text{H}_2\\text{SO}_4$ loãng."),
            )
        ],
        example="Cho $5{,}6\\text{ g}$ bột sắt ($\\text{Fe} = 56$) vào dung dịch hydrochloric acid ($\\text{HCl}$) lấy dư. Hãy nêu hiện tượng quan sát được, viết phương trình hóa học và tính thể tích khí hydrogen ($\\text{H}_2$) thoát ra ở điều kiện chuẩn ($25^\\circ\\text{C}, 1\\text{ bar}$).",
        example_answer="- **Hiện tượng**: Bột sắt tan dần, có bọt khí không màu ($\\text{H}_2$) sủi lên và tạo thành dung dịch muối iron(II) chloride ($\\text{FeCl}_2$) màu lục nhạt.\n- **Phương trình hóa học**: $\\text{Fe} + 2\\text{HCl} \\longrightarrow \\text{FeCl}_2 + \\text{H}_2\\uparrow$.\n- **Tính toán**: Ta có $n_{\\text{Fe}} = \\dfrac{5{,}6}{56} = 0{,}1\\text{ mol}$. Theo PTHH: $n_{\\text{H}_2} = n_{\\text{Fe}} = 0{,}1\\text{ mol} \\implies V_{\\text{H}_2(\\text{đkc})} = 24{,}79 \\cdot 0{,}1 = 2{,}479\\text{ lít}$.",
        real_life="Dịch vị dạ dày con người có chứa hydrochloric acid ($\\text{HCl}$) loãng giúp tiêu hóa thức ăn và diệt khuẩn; giấm ăn chứa acetic acid ($\\text{CH}_3\\text{COOH}$); bình ắc quy chì chứa dung dịch sulfuric acid ($\\text{H}_2\\text{SO}_4$).",
        quiz=[
            mcq("biet", "Khi tan trong nước, mọi hợp chất **Acid** đều phân li tạo ra loại ion dương đặc trưng nào?", ["Ion $\\text{H}^+$", "Ion $\\text{OH}^-$", "Ion $\\text{Na}^+$", "Ion $\\text{Cl}^-$"], 0, "Acid là những hợp chất khi tan trong nước tạo ra ion $\\text{H}^+$."),
            mcq("biet", "Nhỏ vài giọt dung dịch hydrochloric acid ($\\text{HCl}$) hoặc nước cốt chanh lên mẩu **giấy quỳ tím** thì giấy quỳ tím chuyển sang màu gì?", ["Chuyển sang màu đỏ (hoặc hồng)", "Chuyển sang màu xanh", "Chuyển sang màu đen", "Giữ nguyên màu tím"], 0, "Dung dịch acid làm đổi màu giấy quỳ tím thành màu đỏ (acid yếu như nước chanh làm hóa đỏ nhạt/hồng)."),
            mcq("hieu", "Kim loại nào sau đây **không** phản ứng với dung dịch hydrochloric acid ($\\text{HCl}$) và dung dịch sulfuric acid ($\\text{H}_2\\text{SO}_4$) loãng?", ["Copper ($\\text{Cu}$ – đồng)", "Magnesium ($\\text{Mg}$)", "Zinc ($\\text{Zn}$ – kẽm)", "Iron ($\\text{Fe}$ – sắt)"], 0, "Kim loại đồng ($\\text{Cu}$) đứng sau $\\text{H}$ trong dãy hoạt động hóa học nên không tác dụng với dung dịch $\\text{HCl}$ và $\\text{H}_2\\text{SO}_4$ loãng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Acid:", [
                "Khi cho sắt ($\\text{Fe}$) tác dụng với dung dịch $\\text{HCl}$, sản phẩm tạo thành là muối $\\text{FeCl}_2$ và khí $\\text{H}_2$.",
                "Dung dịch sulfuric acid có công thức hóa học là $\\text{H}_2\\text{SO}_4$, trong đó gốc sulfate ($=\\text{SO}_4$) có hóa trị $\\text{II}$.",
                "Khi nhỏ dung dịch acid vào dung dịch phenolphthalein không màu thì dung dịch chuyển sang màu hồng đậm.",
                "Mưa acid hình thành chủ yếu do các khí thải công nghiệp $\\text{SO}_2$ và $\\text{NO}_x$ hòa tan vào nước mưa tạo thành $\\text{H}_2\\text{SO}_4$ và $\\text{HNO}_3$.",
            ], [True, True, False, True], "Ý c) sai vì dung dịch acid không làm đổi màu phenolphthalein (chỉ có dung dịch base/kiềm mới làm phenolphthalein hóa hồng)."),
            short("vandung", "Cho $0{,}2\\text{ mol}$ kim loại magnesium ($\\text{Mg}$) tác dụng hoàn toàn với dung dịch $\\text{H}_2\\text{SO}_4$ loãng dư theo phương trình: $\\text{Mg} + \\text{H}_2\\text{SO}_4 \\longrightarrow \\text{MgSO}_4 + \\text{H}_2\\uparrow$. Số mol khí $\\text{H}_2$ thu được bằng bao nhiêu $\\text{mol}$?", ["0,2", "0.2"], "Theo phương trình hóa học (tỉ lệ $1 : 1$), số mol khí $\\text{H}_2$ thu được là $n_{\\text{H}_2} = n_{\\text{Mg}} = 0{,}2\\text{ mol}$.", unit="mol"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 10: Base và thang pH",
        icon="🧼",
        description="Khái niệm Base (M(OH)_n phân li ra ion OH⁻), phân biệt base kiềm (tan) và base không tan, tính chất hóa học của base (quỳ tím hóa xanh, phenolphthalein hóa hồng, phản ứng trung hòa) và thang pH (1–14).",
        requirements=[
            "Định nghĩa được **Base** là những hợp chất trong phân tử có nguyên tử kim loại liên kết với nhóm hydroxide ($-\\text{OH}$); khi tan trong nước, base tạo ra **ion $\\text{OH}^-$**.",
            "Phân biệt được **base tan (kiềm)**: $\\text{NaOH}, \\text{KOH}, \\text{Ca(OH)}_2, \\text{Ba(OH)}_2$ với **base không tan** trong nước: $\\text{Mg(OH)}_2, \\text{Cu(OH)}_2$ (xanh lam), $\\text{Fe(OH)}_3$ (nâu đỏ), $\\text{Al(OH)}_3$ (trắng keo); viết được phương trình phản ứng trung hòa $\\text{Acid} + \\text{Base} \\to \\text{Muối} + \\text{H}_2\\text{O}$.",
            "Sử dụng được **thang $\\text{pH}$** để đánh giá độ acid – base của dung dịch: $\\text{pH} < 7$ (môi trường acid), $\\text{pH} = 7$ (môi trường trung tính), $\\text{pH} > 7$ (môi trường base/kiềm).",
        ],
        definition="Base là những hợp chất trong phân tử có nguyên tử kim loại liên kết với một hay nhiều nhóm hydroxide ($-\\text{OH}$); khi tan trong nước, base tạo ra ion $\\text{OH}^-$. Thang pH (thường từ $1$ đến $14$) dùng để biểu thị độ acid hoặc độ base của dung dịch: $\\text{pH} < 7$ là môi trường acid, $\\text{pH} = 7$ là môi trường trung tính, $\\text{pH} > 7$ là môi trường base.",
        theory=(
            "### 1. Khái niệm, Phân loại và Tính chất hóa học của Base\n"
            "- **Công thức chung**: $M(\\text{OH})_n$ (với $n$ là hóa trị của kim loại $M$, vì nhóm $-\\text{OH}$ có hóa trị $\\text{I}$). Tên gọi: $\\text{Tên kim loại (kèm hóa trị nếu nhiều hóa trị)} + \\text{hydroxide}$.\n"
            "- **Phân loại Base theo tính tan trong nước**:\n"
            "  1. **Base tan trong nước (gọi là Kiềm)**: $\\text{NaOH}$ (sodium hydroxide – xút ăn da), $\\text{KOH}$ (potassium hydroxide), $\\text{Ba(OH)}_2$ (barium hydroxide) và $\\text{Ca(OH)}_2$ (calcium hydroxide – vôi tôi, ít tan tạo dung dịch nước vôi trong).\n"
            "  2. **Base không tan trong nước (chất kết tủa)**: $\\text{Cu(OH)}_2\\downarrow$ (màu xanh lam), $\\text{Fe(OH)}_3\\downarrow$ (màu nâu đỏ), $\\text{Fe(OH)}_2\\downarrow$ (trắng xanh), $\\text{Mg(OH)}_2\\downarrow$ (trắng), $\\text{Al(OH)}_3\\downarrow$ (keo trắng).\n"
            "- **Tính chất hóa học**:\n"
            "  - **Đổi màu chất chỉ thị**: Dung dịch base (kiềm) làm **giấy quỳ tím chuyển sang màu xanh** và làm **dung dịch phenolphthalein không màu chuyển sang màu hồng**.\n"
            "  - **Tác dụng với dung dịch Acid (Phản ứng trung hòa)**: $\\text{Base} + \\text{Acid} \\longrightarrow \\text{Muối} + \\text{H}_2\\text{O}$ (cả base tan và base không tan đều phản ứng với acid!).\n\n"
            "### 2. Thang pH\n"
            "- Giá trị $\\text{pH}$ thường nhận từ $1$ đến $14$:\n"
            "  - **$\\text{pH} = 7$**: môi trường **trung tính** (nước cất, dung dịch $\\text{NaCl}$).\n"
            "  - **$\\text{pH} < 7$**: môi trường **acid** ($\\text{pH}$ càng nhỏ thì độ acid càng mạnh).\n"
            "  - **$\\text{pH} > 7$**: môi trường **base / kiềm** ($\\text{pH}$ càng lớn thì độ kiềm càng mạnh)."
        ),
        formulas=[
            G(
                "Phản ứng của Base, Chất chỉ thị màu và Thang pH",
                F("Đổi màu chất chỉ thị của Dung dịch Kiềm và Phản ứng trung hòa", "$\\text{Dung dịch Kiềm} \\implies \\begin{cases} \\text{Quỳ tím} \\to \\text{XANH} \\\\ \\text{Phenolphthalein} \\to \\text{HỒNG} \\end{cases}; \\qquad \\text{Base} + \\text{Acid} \\longrightarrow \\text{Muối} + \\text{H}_2\\text{O}$", "Ví dụ: $\\text{NaOH} + \\text{HCl} \\to \\text{NaCl} + \\text{H}_2\\text{O}$; $\\text{Cu(OH)}_2 + 2\\text{HCl} \\to \\text{CuCl}_2 + 2\\text{H}_2\\text{O}$."),
                F("Quy ước Thang pH (1 ➔ 14)", "$\\text{pH} < 7: \\text{Môi trường ACID } (\\text{pH} \\downarrow \\Rightarrow \\text{acid tăng}); \\quad \\text{pH} = 7: \\text{TRUNG TÍNH}; \\quad \\text{pH} > 7: \\text{Môi trường BASE } (\\text{pH} \\uparrow \\Rightarrow \\text{kiềm tăng})$", "Khi đất trồng bị chua ($\\text{pH} < 5$), người nông dân bón vôi bột ($\\text{CaO}$ hoặc $\\text{Ca(OH)}_2$) để khử chua (tăng $\\text{pH}$ của đất)."),
            )
        ],
        example="Cho hai dung dịch không màu đựng trong hai lọ mất nhãn là dung dịch hydrochloric acid ($\\text{HCl}$) và dung dịch sodium hydroxide ($\\text{NaOH}$). Hãy trình bày cách nhận biết hai lọ bằng giấy quỳ tím hoặc dung dịch phenolphthalein, và viết phương trình hóa học khi trộn hai dung dịch này với nhau.",
        example_answer="- **Dùng giấy quỳ tím**: Nhỏ mẫu thử lên giấy quỳ tím; mẫu làm quỳ tím hóa **đỏ** là dung dịch $\\text{HCl}$ (acid), mẫu làm quỳ tím hóa **xanh** là dung dịch $\\text{NaOH}$ (base kiềm). *(Nếu dùng phenolphthalein thì mẫu hóa hồng là $\\text{NaOH}$, mẫu không đổi màu là $\\text{HCl}$)*. \n- **Phương trình phản ứng trung hòa**: $\\text{NaOH} + \\text{HCl} \\longrightarrow \\text{NaCl} + \\text{H}_2\\text{O}$.",
        real_life="Thuốc kháng acid dạ dày (Antacid) chứa base không tan $\\text{Mg(OH)}_2$ và $\\text{Al(OH)}_3$ giúp trung hòa lượng acid $\\text{HCl}$ dư thừa trong dạ dày (đưa $\\text{pH}$ dạ dày về mức ổn định) để giảm đau rát thượng vị.",
        quiz=[
            mcq("biet", "Khi tan trong nước, các hợp chất **Base (Kiềm)** phân li tạo ra loại ion âm đặc trưng nào?", ["Ion hydroxide ($\\text{OH}^-$)", "Ion $\\text{H}^+$", "Ion $\\text{Cl}^-$", "Ion $\\text{SO}_4^{2-}$"], 0, "Base là những hợp chất khi tan trong nước tạo ra ion $\\text{OH}^-$."),
            mcq("biet", "Nhỏ vài giọt dung dịch sodium hydroxide ($\\text{NaOH}$) vào ống nghiệm đựng dung dịch **phenolphthalein** không màu thì dung dịch chuyển sang màu gì?", ["Chuyển sang màu hồng", "Chuyển sang màu xanh lam", "Giữ nguyên không màu", "Chuyển sang màu vàng"], 0, "Dung dịch kiềm ($\\text{NaOH}, \\text{KOH}, \\text{Ca(OH)}_2, \\text{Ba(OH)}_2$) làm dung dịch phenolphthalein không màu chuyển sang màu hồng (và làm quỳ tím hóa xanh)."),
            mcq("hieu", "Một mẫu nước mưa đo được $\\text{pH} = 5{,}2$ và một mẫu nước xà phòng đo được $\\text{pH} = 9{,}5$. Nhận xét nào sau đây về môi trường của hai mẫu này là **đúng**?", ["Mẫu nước mưa có môi trường acid ($\\text{pH} < 7$), còn mẫu nước xà phòng có môi trường base/kiềm ($\\text{pH} > 7$)", "Mẫu nước mưa có môi trường base, còn nước xà phòng có môi trường acid", "Cả hai mẫu đều có môi trường trung tính", "Cả hai mẫu đều có môi trường acid mạnh"], 0, "Theo thang pH: $\\text{pH} = 5{,}2 < 7$ là môi trường acid; $\\text{pH} = 9{,}5 > 7$ là môi trường base (kiềm)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Base và thang pH:", [
                "Các base tan tốt trong nước như $\\text{NaOH}, \\text{KOH}, \\text{Ba(OH)}_2$ được gọi là các kiềm.",
                "Copper(II) hydroxide $\\text{Cu(OH)}_2$ là một base không tan trong nước có màu xanh lam, nhưng tan được trong dung dịch acid $\\text{HCl}$ tạo muối và nước.",
                "Trong vùng $\\text{pH} < 7$, giá trị $\\text{pH}$ càng lớn thì độ acid của dung dịch càng mạnh.",
                "Người nông dân rắc vôi bột ($\\text{CaO}$ hoặc $\\text{Ca(OH)}_2$) lên ruộng bị chua là ứng dụng phản ứng trung hòa giữa base và acid trong đất.",
            ], [True, True, False, True], "Ý c) sai vì trong vùng $\\text{pH} < 7$, giá trị $\\text{pH}$ **càng nhỏ** (càng gần $1$) thì độ acid của dung dịch càng mạnh."),
            short("vandung", "Ở nhiệt độ thường ($25^\\circ\\text{C}$), nước cất tinh khiết (môi trường trung tính) có giá trị $\\text{pH}$ bằng bao nhiêu?", ["7"], "Môi trường trung tính (nước tinh khiết ở $25^\\circ\\text{C}$) có giá trị $\\text{pH} = 7$."),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 11: Oxide",
        icon="🪨",
        description="Khái niệm Oxide, phân loại 4 nhóm oxide (oxide base, oxide acid, oxide lưỡng tính, oxide trung tính) và tính chất hóa học của oxide base, oxide acid.",
        requirements=[
            "Định nghĩa được **Oxide** là hợp chất của hai nguyên tố, trong đó có một nguyên tố là oxygen ($\\text{O}$).",
            "Phân loại được các oxide thành 4 nhóm theo tính chất hóa học: **oxide base** ($\\text{CuO}, \\text{Fe}_2\\text{O}_3, \\text{CaO}, \\text{Na}_2\\text{O}$), **oxide acid** ($\\text{CO}_2, \\text{SO}_2, \\text{SO}_3, \\text{P}_2\\text{O}_5$), **oxide lưỡng tính** ($\\text{Al}_2\\text{O}_3, \\text{ZnO}$) và **oxide trung tính** ($\\text{CO}, \\text{NO}$).",
            "Viết được phương trình hóa học của oxide base tác dụng với dung dịch acid ($\\text{Oxide base} + \\text{Acid} \\to \\text{Muối} + \\text{H}_2\\text{O}$) và oxide acid tác dụng với dung dịch kiềm ($\\text{Oxide acid} + \\text{Dung dịch Base} \\to \\text{Muối} + \\text{H}_2\\text{O}$).",
        ],
        definition="Oxide là hợp chất của hai nguyên tố, trong đó có một nguyên tố là oxygen ($\\text{O}$). Dựa vào tính chất hóa học, oxide được chia thành 4 loại: oxide base, oxide acid, oxide lưỡng tính và oxide trung tính.",
        theory=(
            "### 1. Khái niệm và Phân loại 4 nhóm Oxide\n"
            "1. **Oxide base**: là những oxide tác dụng được với dung dịch acid tạo thành muối và nước (thường là oxide của kim loại như $\\text{Na}_2\\text{O}, \\text{K}_2\\text{O}, \\text{CaO}, \\text{BaO}, \\text{MgO}, \\text{CuO}, \\text{FeO}, \\text{Fe}_2\\text{O}_3$).\n"
            "2. **Oxide acid**: là những oxide tác dụng được với dung dịch base (kiềm) tạo thành muối và nước (thường là oxide của phi kim như $\\text{CO}_2, \\text{SO}_2, \\text{SO}_3, \\text{P}_2\\text{O}_5, \\text{N}_2\\text{O}_5, \\text{SiO}_2$).\n"
            "3. **Oxide lưỡng tính**: là những oxide vừa tác dụng được với dung dịch acid vừa tác dụng được với dung dịch base (kiềm) đều tạo thành muối và nước: tiêu biểu nhất là **$\\text{Al}_2\\text{O}_3$** (aluminium oxide) và **$\\text{ZnO}$** (zinc oxide).\n"
            "4. **Oxide trung tính (oxide không tạo muối)**: không tác dụng với acid, không tác dụng với base và không tác dụng với nước: tiêu biểu là **$\\text{CO}$** (carbon monoxide) và **$\\text{NO}$** (nitrogen monoxide).\n\n"
            "### 2. Tính chất hóa học trọng tâm của Oxide base và Oxide acid\n"
            "- **Oxide base $+$ Dung dịch Acid $\\longrightarrow$ Muối $+$ Nước**:\n"
            "  $$\\text{CuO} + 2\\text{HCl} \\longrightarrow \\text{CuCl}_2 + \\text{H}_2\\text{O}; \\qquad \\text{Fe}_2\\text{O}_3 + 3\\text{H}_2\\text{SO}_4 \\longrightarrow \\text{Fe}_2(\\text{SO}_4)_3 + 3\\text{H}_2\\text{O}$$\n"
            "- **Oxide acid $+$ Dung dịch Base (kiềm) $\\longrightarrow$ Muối $+$ Nước**:\n"
            "  $$\\text{CO}_2 + \\text{Ca(OH)}_2 \\longrightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}; \\qquad \\text{SO}_2 + 2\\text{NaOH} \\longrightarrow \\text{Na}_2\\text{SO}_3 + \\text{H}_2\\text{O}$$"
        ),
        formulas=[
            G(
                "Phân loại 4 nhóm Oxide và Phương trình hóa học đặc trưng",
                F("Bốn nhóm Oxide theo tính chất hóa học", "$\\begin{cases} \\text{Oxide base}: \\text{CaO, CuO, Fe}_2\\text{O}_3, \\text{Na}_2\\text{O} \\\\ \\text{Oxide acid}: \\text{CO}_2, \\text{SO}_2, \\text{SO}_3, \\text{P}_2\\text{O}_5 \\\\ \\text{Oxide lưỡng tính}: \\text{Al}_2\\text{O}_3, \\text{ZnO} \\\\ \\text{Oxide trung tính}: \\text{CO, NO} \\end{cases}$", "Chú ý $\\text{CO}$ và $\\text{NO}$ là oxide trung tính (không phản ứng với dung dịch acid hay kiềm)!"),
                F("Hai phương trình phản ứng tạo muối và nước của Oxide", "$\\text{Oxide base} + \\text{Acid} \\to \\text{Muối} + \\text{H}_2\\text{O}; \\qquad \\text{Oxide acid} + \\text{Kiềm} \\to \\text{Muối} + \\text{H}_2\\text{O}$", "Phản ứng nhận biết khí $\\text{CO}_2$ bằng nước vôi trong: $\\text{CO}_2 + \\text{Ca(OH)}_2 \\to \\text{CaCO}_3\\downarrow_{\\text{(trắng)}} + \\text{H}_2\\text{O}$."),
            )
        ],
        example="Cho bột copper(II) oxide ($\\text{CuO}$, màu đen) vào ống nghiệm chứa dung dịch hydrochloric acid ($\\text{HCl}$) rồi lắc nhẹ. Hãy nêu hiện tượng quan sát được, cho biết $\\text{CuO}$ thuộc loại oxide nào và viết phương trình hóa học của phản ứng.",
        example_answer="- **Hiện tượng**: Bột $\\text{CuO}$ màu đen tan dần hết, dung dịch từ không màu chuyển sang màu xanh lam đặc trưng của muối copper(II) chloride ($\\text{CuCl}_2$).\n- **Phân loại**: $\\text{CuO}$ tác dụng với acid tạo muối và nước nên là một **oxide base**.\n- **Phương trình hóa học**: $\\text{CuO} + 2\\text{HCl} \\longrightarrow \\text{CuCl}_2 + \\text{H}_2\\text{O}$.",
        real_life="Trước khi hàn hoặc sơn các chi tiết bằng sắt thép bị gỉ, người thợ cơ khí thường ngâm tẩy bề mặt kim loại bằng dung dịch acid loãng để hòa tan lớp gỉ sắt ($\\text{Fe}_2\\text{O}_3$ – một oxide base); còn vôi sống ($\\text{CaO}$) được dùng làm gói hút ẩm trong túi bánh gạo.",
        quiz=[
            mcq("biet", "Hợp chất nào sau đây là một **oxide**?", ["$\\text{CaO}$ (calcium oxide)", "$\\text{Ca(OH)}_2$", "$\\text{CaCO}_3$", "$\\text{H}_2\\text{SO}_4$"], 0, "Oxide là hợp chất chỉ gồm $2$ nguyên tố, trong đó có $1$ nguyên tố là oxygen ($\\text{O}$). $\\text{CaO}$ gồm $2$ nguyên tố $\\text{Ca}$ và $\\text{O}$ nên là oxide."),
            mcq("biet", "Cặp chất nào sau đây thuộc loại **oxide lưỡng tính** (vừa tác dụng được với dung dịch acid vừa tác dụng được với dung dịch kiềm)?", ["$\\text{Al}_2\\text{O}_3$ và $\\text{ZnO}$", "$\\text{CO}$ và $\\text{NO}$", "$\\text{CO}_2$ và $\\text{SO}_2$", "$\\text{CuO}$ và $\\text{Fe}_2\\text{O}_3$"], 0, "$\\text{Al}_2\\text{O}_3$ và $\\text{ZnO}$ là hai oxide lưỡng tính tiêu biểu; còn $\\text{CO}, \\text{NO}$ là oxide trung tính."),
            mcq("hieu", "Khi dẫn từ từ khí carbon dioxide ($\\text{CO}_2$ – một oxide acid) vào cốc đựng dung dịch nước vôi trong ($\\text{Ca(OH)}_2$) dư thì xuất hiện hiện tượng gì?", ["Nước vôi trong bị vẩn đục màu trắng do tạo thành kết tủa $\\text{CaCO}_3$", "Dung dịch chuyển sang màu xanh lam", "Có khí màu vàng lục bay ra", "Không có hiện tượng gì"], 0, "Khí $\\text{CO}_2$ phản ứng với $\\text{Ca(OH)}_2$ theo phương trình $\\text{CO}_2 + \\text{Ca(OH)}_2 \\longrightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}$ tạo kết tủa trắng làm đục nước vôi trong."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Oxide:", [
                "Các chất $\\text{CuO}, \\text{Fe}_2\\text{O}_3, \\text{CaO}, \\text{MgO}$ đều là các oxide base.",
                "Các chất $\\text{CO}_2, \\text{SO}_2, \\text{SO}_3, \\text{P}_2\\text{O}_5$ đều là các oxide acid.",
                "Khí carbon monoxide ($\\text{CO}$) là một oxide acid nên tác dụng mạnh với dung dịch $\\text{NaOH}$ ở điều kiện thường.",
                "Khi hòa tan iron(III) oxide ($\\text{Fe}_2\\text{O}_3$) vào dung dịch $\\text{HCl}$ vừa đủ thì thu được muối $\\text{FeCl}_3$ và nước.",
            ], [True, True, False, True], "Ý c) sai vì $\\text{CO}$ (carbon monoxide) là một **oxide trung tính** (oxide không tạo muối) nên không phản ứng với dung dịch $\\text{NaOH}$ hay dung dịch acid."),
            short("vandung", "Dẫn $0{,}15\\text{ mol}$ khí $\\text{CO}_2$ vào bình đựng dung dịch nước vôi trong ($\\text{Ca(OH)}_2$) lấy dư theo phương trình: $\\text{CO}_2 + \\text{Ca(OH)}_2 \\longrightarrow \\text{CaCO}_3\\downarrow + \\text{H}_2\\text{O}$. Khối lượng kết tủa $\\text{CaCO}_3$ ($M = 100\\text{ g/mol}$) thu được bằng bao nhiêu gam ($\\text{g}$)?", ["15"], "Theo PTHH: $n_{\\text{CaCO}_3} = n_{\\text{CO}_2} = 0{,}15\\text{ mol} \\implies m_{\\text{CaCO}_3} = 0{,}15 \\cdot 100 = 15\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 12: Muối",
        icon="🧂",
        description="Khái niệm, danh pháp và tính tan của Muối, tính chất hóa học của muối và điều kiện xảy ra phản ứng trao đổi trong dung dịch (tạo kết tủa, chất khí hoặc nước).",
        requirements=[
            "Định nghĩa được **Muối** là những hợp chất được tạo ra khi thay thế ion $\\text{H}^+$ của acid bằng ion kim loại hoặc ion ammonium ($\\text{NH}_4^+$); gọi đúng tên muối theo danh pháp IUPAC.",
            "Nắm được quy tắc tính tan cơ bản của các muối (mọi muối $\\text{Na}^+, \\text{K}^+, \\text{NH}_4^+, \\text{NO}_3^-$ đều tan; $\\text{AgCl}\\downarrow$ trắng, $\\text{BaSO}_4\\downarrow$ trắng, $\\text{CaCO}_3\\downarrow$ trắng, $\\text{BaCO}_3\\downarrow$ trắng không tan).",
            "Trình bày được 4 tính chất hóa học của dung dịch muối (tác dụng với kim loại, với acid, với dung dịch base, với dung dịch muối khác) và **điều kiện để phản ứng trao đổi xảy ra** là sản phẩm phải có **chất kết tủa ($\\downarrow$), chất khí ($\\uparrow$) hoặc nước ($\\text{H}_2\\text{O}$)**.",
        ],
        definition="Muối là những hợp chất được hình thành từ sự thay thế ion $\\text{H}^+$ của acid bằng ion kim loại (hoặc ion ammonium $\\text{NH}_4^+$). Phản ứng trao đổi giữa các dung dịch acid, base, muối chỉ xảy ra khi các chất tạo thành có chất kết tủa ($\\downarrow$), chất khí dễ bay hơi ($\\uparrow$) hoặc chất điện li rất yếu như nước ($\\text{H}_2\\text{O}$).",
        theory=(
            "### 1. Khái niệm, Tên gọi và Tính tan của một số Muối\n"
            "- **Cấu tạo phân tử muối**: gồm một hay nhiều **cation kim loại** (hoặc $\\text{NH}_4^+$) liên kết với một hay nhiều **anion gốc acid** ($\\text{Cl}^-\\text{: chloride}$, $\\text{NO}_3^-\\text{: nitrate}$, $\\text{SO}_4^{2-}\\text{: sulfate}$, $\\text{CO}_3^{2-}\\text{: carbonate}$, $\\text{PO}_4^{3-}\\text{: phosphate}$).\n"
            "- **Quy tắc tính tan cần nhớ**:\n"
            "  - Tất cả các muối của **$\\text{Na}^+, \\text{K}^+, \\text{NH}_4^+$** và tất cả các muối **nitrate ($-\\text{NO}_3$)** đều **TAN TỐT** trong nước.\n"
            "  - Hầu hết muối chloride ($-\\text{Cl}$) đều tan, **trừ $\\text{AgCl}\\downarrow$ (kết tủa trắng)**.\n"
            "  - Hầu hết muối sulfate ($=\\text{SO}_4$) đều tan, **trừ $\\text{BaSO}_4\\downarrow$ (kết tủa trắng)**, $\\text{PbSO}_4\\downarrow$ (và $\\text{CaSO}_4, \\text{Ag}_2\\text{SO}_4$ ít tan).\n"
            "  - Hầu hết muối carbonate ($=\\text{CO}_3$) và phosphate ($\\equiv\\text{PO}_4$) đều **KHÔNG TAN** ($\\text{CaCO}_3\\downarrow, \\text{BaCO}_3\\downarrow, \\text{MgCO}_3\\downarrow$), trừ muối của $\\text{Na}^+, \\text{K}^+, \\text{NH}_4^+$.\n\n"
            "### 2. Bốn tính chất hóa học của Dung dịch Muối & Điều kiện phản ứng trao đổi\n"
            "1. **Muối $+$ Kim loại mạnh hơn $\\longrightarrow$ Muối mới $+$ Kim loại mới**: $\\text{Fe} + \\text{CuSO}_4 \\longrightarrow \\text{FeSO}_4 + \\text{Cu}\\downarrow$.\n"
            "2. **Muối $+$ Acid $\\longrightarrow$ Muối mới $+$ Acid mới**: $\\text{CaCO}_3 + 2\\text{HCl} \\longrightarrow \\text{CaCl}_2 + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}$; $\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\longrightarrow \\text{BaSO}_4\\downarrow + 2\\text{HCl}$.\n"
            "3. **Dung dịch Muối $+$ Dung dịch Base (kiềm) $\\longrightarrow$ Muối mới $+$ Base mới**: $\\text{CuSO}_4 + 2\\text{NaOH} \\longrightarrow \\text{Cu(OH)}_2\\downarrow_{\\text{(xanh)}} + \\text{Na}_2\\text{SO}_4$.\n"
            "4. **Dung dịch Muối $+$ Dung dịch Muối $\\longrightarrow$ 2 Muối mới**: $\\text{AgNO}_3 + \\text{NaCl} \\longrightarrow \\text{AgCl}\\downarrow_{\\text{(trắng)}} + \\text{NaNO}_3$.\n"
            "- **Điều kiện xảy ra phản ứng trao đổi trong dung dịch**: Sản phẩm sinh ra phải có ít nhất một chất là **chất kết tủa ($\\downarrow$)**, **chất khí ($\\uparrow$)** hoặc **nước ($\\text{H}_2\\text{O}$)**."
        ),
        formulas=[
            G(
                "Tính chất hóa học của Muối và Điều kiện phản ứng trao đổi",
                F("Điều kiện cần và đủ để phản ứng trao đổi trong dung dịch xảy ra", "$AB + CD \\longrightarrow AD + CB \\quad \\text{xảy ra khi sản phẩm có: } \\text{Kết tủa } (\\downarrow) \\text{ hoặc Khí } (\\uparrow) \\text{ hoặc } \\text{H}_2\\text{O}$", "Các kết tủa trắng kinh điển không tan trong acid mạnh: $\\text{AgCl}\\downarrow$ và $\\text{BaSO}_4\\downarrow$."),
                F("Các phương trình phản ứng đặc trưng của Muối", "$\\text{Fe} + \\text{CuSO}_4 \\to \\text{FeSO}_4 + \\text{Cu}\\downarrow; \\quad \\text{BaCl}_2 + \\text{Na}_2\\text{SO}_4 \\to \\text{BaSO}_4\\downarrow + 2\\text{NaCl}; \\quad \\text{Na}_2\\text{CO}_3 + 2\\text{HCl} \\to 2\\text{NaCl} + \\text{CO}_2\\uparrow + \\text{H}_2\\text{O}$", "Hai chất tham gia phản ứng giữa Muối + Kiềm hoặc Muối + Muối đều phải là dung dịch tan."),
            )
        ],
        example="Nhỏ dung dịch barium chloride ($\\text{BaCl}_2$) vào ống nghiệm đựng dung dịch sodium sulfate ($\\text{Na}_2\\text{SO}_4$). Hãy nêu hiện tượng xảy ra, giải thích vì sao phản ứng trao đổi này xảy ra được và viết phương trình hóa học.",
        example_answer="- **Hiện tượng**: Xuất hiện ngay **kết tủa màu trắng** không tan trong nước và các acid.\n- **Giải thích**: Phản ứng trao đổi xảy ra được vì tạo thành chất kết tủa là barium sulfate ($\\text{BaSO}_4\\downarrow$).\n- **Phương trình hóa học**: $\\text{BaCl}_2 + \\text{Na}_2\\text{SO}_4 \\longrightarrow \\text{BaSO}_4\\downarrow + 2\\text{NaCl}$.",
        real_life="Thuốc muối dạ dày (baking soda – $\\text{NaHCO}_3$) phản ứng với lượng acid $\\text{HCl}$ dư thừa trong dạ dày; thạch cao ($\\text{CaSO}_4$) dùng bó bột chấn thương và đúc tượng; nước muối $\\text{NaCl}$ dùng bảo quản thực phẩm.",
        quiz=[
            mcq("biet", "Điều kiện để một **phản ứng trao đổi** giữa các dung dịch muối, acid, base xảy ra được là gì?", ["Các chất sản phẩm tạo thành phải có chất kết tủa ($\\downarrow$), chất khí ($\\uparrow$) hoặc nước ($\\text{H}_2\\text{O}$)", "Tất cả các chất sản phẩm đều phải tan hoàn toàn và phân li mạnh", "Phải nung ở nhiệt độ trên $2000^\\circ\\text{C}$", "Không cần bất kì điều kiện nào"], 0, "Phản ứng trao đổi trong dung dịch chỉ xảy ra khi tạo thành chất kết tủa, chất khí bay hơi hoặc chất điện li yếu như $\\text{H}_2\\text{O}$."),
            mcq("biet", "Khi nhỏ dung dịch silver nitrate ($\\text{AgNO}_3$) vào ống nghiệm đựng dung dịch muối ăn sodium chloride ($\\text{NaCl}$), hiện tượng quan sát được là gì?", ["Xuất hiện kết tủa màu trắng của silver chloride ($\\text{AgCl}\\downarrow$)", "Sủi bọt khí không màu", "Dung dịch chuyển sang màu xanh lam", "Không có hiện tượng gì xảy ra"], 0, "Phản ứng $\\text{AgNO}_3 + \\text{NaCl} \\longrightarrow \\text{AgCl}\\downarrow + \\text{NaNO}_3$ tạo kết tủa trắng $\\text{AgCl}$."),
            mcq("hieu", "Cặp dung dịch nào sau đây **không** xảy ra phản ứng hóa học khi trộn lẫn vào nhau?", ["Dung dịch $\\text{NaCl}$ và dung dịch $\\text{KNO}_3$", "Dung dịch $\\text{BaCl}_2$ và dung dịch $\\text{H}_2\\text{SO}_4$", "Dung dịch $\\text{CuSO}_4$ và dung dịch $\\text{NaOH}$", "Dung dịch $\\text{Na}_2\\text{CO}_3$ và dung dịch $\\text{HCl}$"], 0, "Khi trộn $\\text{NaCl}$ và $\\text{KNO}_3$, các sản phẩm giả định ($\\text{NaNO}_3$ và $\\text{KCl}$) đều là muối tan mạnh, không có kết tủa hay chất khí nên phản ứng không xảy ra."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Muối:", [
                "Tất cả các muối của sodium ($\\text{Na}^+$), potassium ($\\text{K}^+$), ammonium ($\\text{NH}_4^+$) và các muối nitrate ($-\\text{NO}_3$) đều tan tốt trong nước.",
                "Ngâm một đinh sắt sạch ($\\text{Fe}$) vào dung dịch $\\text{CuSO}_4$ màu xanh lam thì thấy có lớp kim loại đồng ($\\text{Cu}$) màu đỏ bám ngoài đinh sắt.",
                "Khi nhỏ dung dịch $\\text{NaOH}$ vào dung dịch $\\text{FeCl}_3$ thì thu được kết tủa $\\text{Fe(OH)}_3$ có màu nâu đỏ.",
                "Muối barium sulfate ($\\text{BaSO}_4$) và calcium carbonate ($\\text{CaCO}_3$) đều tan rất nhiều trong nước lạnh.",
            ], [True, True, True, False], "Ý d) sai vì $\\text{BaSO}_4$ và $\\text{CaCO}_3$ đều là các muối kết tủa trắng không tan trong nước."),
            short("vandung", "Cho dung dịch chứa $0{,}1\\text{ mol}$ $\\text{BaCl}_2$ tác dụng với dung dịch $\\text{Na}_2\\text{SO}_4$ lấy dư theo phương trình: $\\text{BaCl}_2 + \\text{Na}_2\\text{SO}_4 \\longrightarrow \\text{BaSO}_4\\downarrow + 2\\text{NaCl}$. Khối lượng kết tủa $\\text{BaSO}_4$ ($M = 233\\text{ g/mol}$) thu được bằng bao nhiêu gam ($\\text{g}$)?", ["23,3", "23.3"], "Theo PTHH: $n_{\\text{BaSO}_4} = n_{\\text{BaCl}_2} = 0{,}1\\text{ mol} \\implies m_{\\text{BaSO}_4} = 0{,}1 \\cdot 233 = 23{,}3\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 13: Phân bón hóa học",
        icon="🌱",
        description="Các nguyên tố dinh dưỡng đa lượng (N, P, K), phân loại và vai trò của phân đạm, phân lân, phân kali, phân NPK và nguyên tắc bón phân '4 đúng' bảo vệ môi trường.",
        requirements=[
            "Nêu được vai trò của 3 nguyên tố dinh dưỡng đa lượng thiết yếu đối với cây trồng: **Đạm (Nitrogen – $\\text{N}$)**, **Lân (Phosphorus – $\\text{P}$)** và **Kali (Potassium – $\\text{K}$)**.",
            "Nhận biết được công thức hóa học của các loại phân bón thông dụng: phân đạm (urea $(\\text{NH}_2)_2\\text{CO}$, $\\text{NH}_4\\text{NO}_3$, $(\\text{NH}_4)_2\\text{SO}_4$), phân lân ($\\text{Ca(H}_2\\text{PO}_4)_2$), phân kali ($\\text{KCl}, \\text{K}_2\\text{SO}_4$) và phân hỗn hợp NPK.",
            "Trình bày được tác động của việc lạm dụng phân bón hóa học đối với đất, nước và nguyên tắc sử dụng phân bón an toàn, hiệu quả.",
        ],
        definition="Phân bón hóa học là những hóa chất có chứa các nguyên tố dinh dưỡng dùng để bón cho cây trồng nhằm nâng cao năng suất nông sản. Ba nhóm phân bón đa lượng quan trọng nhất là phân đạm (cung cấp $\\text{N}$), phân lân (cung cấp $\\text{P}$) và phân kali (cung cấp $\\text{K}$).",
        theory=(
            "### 1. Phân loại và Vai trò của Phân đạm – Phân lân – Phân kali – Phân NPK\n"
            "1. **Phân đạm (cung cấp nguyên tố Nitrogen – $\\text{N}$)**:\n"
            "   - **Vai trò**: kích thích cây trồng phát triển mạnh thân, cành, lá xanh tốt, ra nhiều hạt, củ, quả (tăng hàm lượng protein thực vật).\n"
            "   - **Các loại phổ biến**: Đạm urea ($(\\text{NH}_2)_2\\text{CO}$, giàu đạm nhất với $\\approx 46\\%\\text{ N}$), đạm ammonium nitrate ($\\text{NH}_4\\text{NO}_3$), đạm ammonium sulfate ($(\\text{NH}_4)_2\\text{SO}_4$).\n"
            "2. **Phân lân (cung cấp nguyên tố Phosphorus – $\\text{P}$)**:\n"
            "   - **Vai trò**: kích thích sự phát triển của **bộ rễ**, quá trình đẻ nhánh, nảy chồi, thúc đẩy cây ra hoa, đậu quả sớm và tăng khả năng chống chịu hạn, rét.\n"
            "   - **Các loại phổ biến**: Superphosphate (chứa $\\text{Ca(H}_2\\text{PO}_4)_2$ tan trong nước), phân lân nung chảy (dùng cho đất chua).\n"
            "3. **Phân kali (cung cấp nguyên tố Potassium – $\\text{K}$)**:\n"
            "   - **Vai trò**: thúc đẩy quá trình tạo đường, tinh bột, chất xơ và dầu, giúp cây cứng cáp **chống đổ ngã**, chịu rét, chịu hạn và kháng sâu bệnh.\n"
            "   - **Các loại phổ biến**: Potassium chloride ($\\text{KCl}$), potassium sulfate ($\\text{K}_2\\text{SO}_4$); tro bếp chứa $\\text{K}_2\\text{CO}_3$ cũng là một loại phân kali.\n"
            "4. **Phân hỗn hợp NPK**: chứa đồng thời cả 3 nguyên tố dinh dưỡng $\\text{N}, \\text{P}, \\text{K}$ theo tỉ lệ ghi trên bao bì.\n\n"
            "### 2. Sử dụng phân bón theo nguyên tắc '4 đúng' và Bảo vệ môi trường\n"
            "- Bón thừa phân hóa học làm đất bị chai cứng, chua hóa, tồn dư nitrate ($\\text{NO}_3^-$) trong rau quả gây hại sức khỏe và rửa trôi xuống ao hồ gây **hiện tượng phú dưỡng** (tảo nở hoa làm cá chết ngạt).\n"
            "- Cần áp dụng quy tắc **4 đúng**: *Đúng loại – Đúng liều – Đúng lúc – Đúng cách*, kết hợp với **phân bón hữu cơ, vi sinh**."
        ),
        formulas=[
            G(
                "Công thức các loại Phân bón hóa học và Vai trò N – P – K",
                F("Công thức hóa học của 3 nhóm phân bón đơn", "$\\text{Phân Đạm (N)}: (\\text{NH}_2)_2\\text{CO},\\ \\text{NH}_4\\text{NO}_3,\\ (\\text{NH}_4)_2\\text{SO}_4; \\quad \\text{Phân Lân (P)}: \\text{Ca(H}_2\\text{PO}_4)_2; \\quad \\text{Phân Kali (K)}: \\text{KCl},\\ \\text{K}_2\\text{SO}_4$", "Đạm urea $(\\text{NH}_2)_2\\text{CO}$ có $M = 60\\text{ g/mol}$, hàm lượng $\\%m_{\\text{N}} = \\dfrac{28}{60} \\cdot 100\\% \\approx 46{,}67\\%$."),
                F("Vai trò cốt lõi của 3 nguyên tố đa lượng N – P – K", "$\\text{N (Đạm)}: \\text{Phát triển thân, lá xanh tốt}; \\quad \\text{P (Lân)}: \\text{Phát triển bộ rễ, ra hoa}; \\quad \\text{K (Kali)}: \\text{Tạo đường/bột, cứng cây chống đổ ngã}$", "Không trộn phân đạm ammonium ($\\text{NH}_4^+$) với vôi hoặc tro bếp (có tính kiềm) vì sẽ giải phóng mất khí $\\text{NH}_3\\uparrow$ làm mất đạm!"),
            )
        ],
        example="Một bao phân bón đạm urea nguyên chất có công thức hóa học là $(\\text{NH}_2)_2\\text{CO}$ và có khối lượng tịnh $50\\text{ kg}$. Biết $\\text{N} = 14, \\text{H} = 1, \\text{C} = 12, \\text{O} = 16$. Hãy tính khối lượng mol của phân urea và tính khối lượng nguyên tố dinh dưỡng Nitrogen ($\\text{N}$) có trong bao phân $50\\text{ kg}$ đó.",
        example_answer="Trong $1$ phân tử $(\\text{NH}_2)_2\\text{CO}$ có $2\\text{N}, 4\\text{H}, 1\\text{C}, 1\\text{O}$. Khối lượng mol của urea là $M = 2 \\cdot 14 + 4 \\cdot 1 + 12 + 16 = 60\\text{ g/mol}$. Phần trăm khối lượng của $\\text{N}$ trong urea là $\\%m_{\\text{N}} = \\dfrac{28}{60} \\cdot 100\\% \\approx 46{,}67\\%$. Khối lượng nguyên tố $\\text{N}$ có trong bao phân $50\\text{ kg}$ là $m_{\\text{N}} = 50 \\cdot \\dfrac{28}{60} \\approx 23{,}33\\text{ kg}$.",
        real_life="Trên các bao phân bón NPK (ví dụ NPK 16-16-8 hoặc NPK 20-20-15) luôn in rõ 3 con số cho người nông dân biết tỉ lệ dinh dưỡng của Đạm – Lân – Kali để chọn loại phân phù hợp với từng giai đoạn sinh trưởng của lúa và cây ăn quả.",
        quiz=[
            mcq("biet", "Phân bón **đạm** (như urea $(\\text{NH}_2)_2\\text{CO}$, $\\text{NH}_4\\text{NO}_3$) cung cấp nguyên tố dinh dưỡng chính nào cho cây trồng?", ["Nguyên tố Nitrogen ($\\text{N}$)", "Nguyên tố Phosphorus ($\\text{P}$)", "Nguyên tố Potassium ($\\text{K}$)", "Nguyên tố Calcium ($\\text{Ca}$)"], 0, "Phân đạm cung cấp nguyên tố dinh dưỡng Nitrogen ($\\text{N}$) giúp cây phát triển mạnh thân, cành, lá."),
            mcq("biet", "Loại phân bón nào sau đây có vai trò kích thích sự phát triển của **bộ rễ** cây trồng, giúp cây đẻ nhánh, nảy chồi và ra hoa quả sớm?", ["Phân lân (cung cấp nguyên tố $\\text{P}$, như $\\text{Ca(H}_2\\text{PO}_4)_2$)", "Phân đạm", "Phân kali", "Muối ăn $\\text{NaCl}$"], 0, "Phân lân (cung cấp $\\text{P}$) rất cần cho thời kì sinh trưởng ban đầu để bộ rễ phát triển khỏe và thúc đẩy ra hoa, đậu quả."),
            mcq("hieu", "Cho các công thức hóa học sau: $\\text{KCl}, \\text{NH}_4\\text{NO}_3, \\text{Ca(H}_2\\text{PO}_4)_2$. Các chất này lần lượt thuộc loại phân bón nào?", ["Phân kali, phân đạm và phân lân", "Phân đạm, phân lân và phân kali", "Phân lân, phân kali và phân đạm", "Cả ba đều là phân đạm"], 0, "$\\text{KCl}$ chứa $\\text{K}$ là phân kali; $\\text{NH}_4\\text{NO}_3$ chứa $\\text{N}$ là phân đạm; $\\text{Ca(H}_2\\text{PO}_4)_2$ chứa $\\text{P}$ là phân lân."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phân bón hóa học:", [
                "Ba nguyên tố dinh dưỡng đa lượng quan trọng nhất đối với cây trồng là $\\text{N}$ (đạm), $\\text{P}$ (lân) và $\\text{K}$ (kali).",
                "Phân hỗn hợp NPK là loại phân bón chứa đồng thời cả ba nguyên tố dinh dưỡng $\\text{N}, \\text{P}$ và $\\text{K}$.",
                "Càng bón nhiều phân đạm hóa học vượt mức khuyến cáo càng giúp rau củ sạch hơn và đất đai tơi xốp màu mỡ hơn.",
                "Tro thực vật (tro bếp) có chứa muối potassium carbonate ($\\text{K}_2\\text{CO}_3$) nên cũng được dùng làm phân bón cung cấp nguyên tố kali ($\\text{K}$).",
            ], [True, True, False, True], "Ý c) sai vì lạm dụng phân đạm hóa học làm đất chai cứng, ô nhiễm nguồn nước (hiện tượng phú dưỡng) và làm tồn dư nitrate trong rau gây hại sức khỏe."),
            short("vandung", "Phân bón NPK là loại phân hỗn hợp cung cấp đồng thời bao nhiêu nguyên tố dinh dưỡng đa lượng thiết yếu ($\\text{N}, \\text{P}, \\text{K}$) cho cây trồng?", ["3"], "Phân NPK cung cấp đồng thời $3$ nguyên tố dinh dưỡng đa lượng là Nitrogen ($\\text{N}$), Phosphorus ($\\text{P}$) và Potassium ($\\text{K}$)."),
        ],
    ),
]


from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("chemistry", 8, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
