"""Hóa học Lớp 6 (KHTN 6 - Kết nối tri thức với cuộc sống): 4 Chương - 12 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 6

CH1 = ("l6-ch01-cac-the-cua-chat", "Chương I: Các thể của chất", "Chương I · Hóa học 6 (KHTN 6): Sự đa dạng của chất, ba thể rắn – lỏng – khí, tính chất và sự chuyển thể của chất.")
CH2 = ("l6-ch02-oxygen-va-khong-khi", "Chương II: Oxygen và không khí", "Chương II · Hóa học 6 (KHTN 6): Tính chất của oxygen, thành phần không khí, sự cháy và bảo vệ môi trường không khí.")
CH3 = ("l6-ch03-vat-lieu-nhien-lieu-thuc-pham", "Chương III: Một số vật liệu, nhiên liệu, nguyên liệu, lương thực – thực phẩm", "Chương III · Hóa học 6 (KHTN 6): Tính chất và sử dụng an toàn, hiệu quả vật liệu, nhiên liệu, nguyên liệu và thực phẩm.")
CH4 = ("l6-ch04-hon-hop-va-tach-chat", "Chương IV: Hỗn hợp và tách chất ra khỏi hỗn hợp", "Chương IV · Hóa học 6 (KHTN 6): Chất tinh khiết, hỗn hợp, dung dịch, huyền phù, nhũ tương và các phương pháp lọc, cô cạn, chiết.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Sự đa dạng của chất và ba thể cơ bản",
        icon="🧊",
        description="Phân biệt vật thể (tự nhiên, nhân tạo; hữu sinh, vô sinh) với chất, và đặc điểm cơ bản của ba thể rắn, lỏng, khí.",
        requirements=[
            "Phân biệt được vật thể tự nhiên, vật thể nhân tạo, vật hữu sinh (vật sống), vật vô sinh (vật không sống) và chất tạo nên vật thể.",
            "So sánh được đặc điểm về hình dạng, thể tích và khả năng chịu nén của chất ở ba thể: rắn, lỏng, khí (hơi).",
            "Giải thích được ở đâu có vật thể là ở đó có chất, một vật thể có thể được tạo nên từ một chất hoặc nhiều chất.",
        ],
        definition="Vật thể là tất cả những gì tồn tại xung quanh chúng ta; chất là thành phần cấu tạo nên vật thể (ở đâu có vật thể là ở đó có chất). Các chất tồn tại ở ba thể cơ bản: thể rắn, thể lỏng và thể khí (hơi).",
        theory=(
            "### 1. Vật thể và Chất\n"
            "- **Vật thể tự nhiên**: có sẵn trong tự nhiên (núi đá vôi, sông suối, cây cối, không khí).\n"
            "- **Vật thể nhân tạo**: do con người tạo ra (cốc thủy tinh, xe đạp, bàn gỗ, quần áo).\n"
            "- **Vật hữu sinh (vật sống)**: có đặc trưng trao đổi chất, lớn lên và sinh sản (con người, động vật, thực vật, vi khuẩn).\n"
            "- **Vật vô sinh (vật không sống)**: không có các đặc trưng sống (hòn đá, chiếc bàn, dòng nước).\n"
            "- Mỗi vật thể đều được cấu tạo từ một hoặc nhiều **chất** (ví dụ: dây điện gồm chất đồng $\\text{Cu}$ và chất nhựa PVC).\n\n"
            "### 2. Đặc điểm ba thể cơ bản của chất\n"
            "- **Thể rắn** (nước đá, thanh sắt, muối ăn): có **hình dạng và thể tích xác định**, rất khó bị nén.\n"
            "- **Thể lỏng** (nước lỏng, dầu ăn, cồn): **không có hình dạng riêng** (có hình dạng của phần vật chứa nó), có **thể tích xác định**, khó bị nén.\n"
            "- **Thể khí / hơi** (khí oxygen, hơi nước, không khí): **không có hình dạng và thể tích riêng** (chiếm toàn bộ thể tích bình chứa), **rất dễ bị nén**."
        ),
        formulas=[
            G(
                "Phân loại Vật thể – Chất và Ba thể của chất",
                F("Quan hệ giữa Vật thể và Chất", "$\\text{Vật thể} \\xleftarrow{\\text{cấu tạo từ}} \\text{Một chất hoặc nhiều chất}$", "Ví dụ: Ấm đun nước (vật thể nhân tạo) được làm từ chất nhôm ($\\text{Al}$) và nhựa cách nhiệt."),
                F("Đặc trưng hình dạng, thể tích và khả năng nén của 3 thể", "$\\text{Rắn: Hình dạng \\& Thể tích cố định}; \\quad \\text{Lỏng: Thể tích cố định}; \\quad \\text{Khí: Dễ nén, lan tỏa mọi phía}$", "Các hạt cấu tạo nên chất ở thể rắn liên kết rất chặt, ở thể lỏng liên kết vừa phải và ở thể khí ở rất xa nhau."),
            )
        ],
        example="Cho câu sau: 'Cây mía là vật thể tự nhiên (hữu sinh), trong thân cây mía có chứa nước, đường saccharose và chất xơ cellulose'. Hãy chỉ ra đâu là vật thể và đâu là các chất trong câu trên.",
        example_answer="Trong câu trên, **cây mía** (và thân cây mía) là **vật thể** (vật thể tự nhiên, hữu sinh); còn **nước, đường saccharose và cellulose** là các **chất** cấu tạo nên cây mía.",
        real_life="Khí dầu mỏ hóa lỏng (gas đun bếp LPG) ở điều kiện thường là thể khí nhưng vì chất khí rất dễ bị nén nên người ta nén dưới áp suất cao chuyển thành thể lỏng gọn gàng trong bình gas thép.",
        quiz=[
            mcq("biet", "Ở thể nào thì chất có **cả hình dạng và thể tích riêng xác định** và rất khó bị nén?", ["Thể rắn", "Thể lỏng", "Thể khí", "Chân không"], 0, "Ở thể rắn, các hạt liên kết chặt chẽ nên chất rắn có hình dạng và thể tích xác định, rất khó bị nén."),
            mcq("biet", "Trong các từ in nghiêng của câu: 'Chiếc *nồi nhôm* dùng để đun *nước*', từ nào chỉ **vật thể** và từ nào chỉ **chất**?", ["Nồi là vật thể; nhôm và nước là chất", "Nồi và nhôm là vật thể; nước là chất", "Nhôm là vật thể; nồi và nước là chất", "Cả nồi, nhôm và nước đều là vật thể nhân tạo"], 0, "Chiếc nồi là vật thể nhân tạo, được làm từ chất nhôm và dùng để chứa chất nước."),
            mcq("hieu", "Vì sao ta có thể dễ dàng bơm một lượng lớn không khí vào trong quả bóng đá hoặc lốp xe đạp?", ["Vì không khí ở thể khí có khoảng cách giữa các hạt rất lớn nên rất dễ bị nén", "Vì không khí ở thể rắn", "Vì không khí có hình dạng cố định", "Vì không khí không có khối lượng"], 0, "Chất ở thể khí rất dễ bị nén và luôn chiếm toàn bộ thể tích bình chứa."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về vật thể và ba thể của chất:", [
                "Cây xanh, con cá là các vật hữu sinh (vật sống); còn hòn đá, chiếc bàn là các vật vô sinh.",
                "Chất ở thể lỏng có thể tích xác định nhưng không có hình dạng riêng mà lấy hình dạng của phần bình chứa nó.",
                "Chất ở thể khí có hình dạng và thể tích cố định không phụ thuộc bình chứa.",
                "Một vật thể nhân tạo như chiếc xe đạp được cấu tạo từ nhiều chất khác nhau (sắt, nhôm, cao su, nhựa).",
            ], [True, True, False, True], "Ý c) sai vì chất ở thể khí không có hình dạng và thể tích riêng."),
            short("vandung", "Trong chương trình Khoa học tự nhiên 6, các chất quanh ta tồn tại ở mấy thể cơ bản (rắn, lỏng, khí)?", ["3"], "Chất tồn tại ở $3$ thể cơ bản là thể rắn, thể lỏng và thể khí (hơi)."),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Tính chất của chất và sự chuyển thể",
        icon="🌡️",
        description="Phân biệt tính chất vật lí với tính chất hóa học của chất, và 6 quá trình chuyển thể (nóng chảy, đông đặc, bay hơi, sôi, ngưng tụ).",
        requirements=[
            "Phân biệt được tính chất vật lí (không có sự tạo thành chất mới: thể, màu, mùi, vị, tính tan, nhiệt độ nóng chảy, nhiệt độ sôi, tính dẫn điện/nhiệt) và tính chất hóa học (có sự biến đổi tạo ra chất mới).",
            "Nêu và lấy được ví dụ về các quá trình chuyển thể của chất: nóng chảy (rắn $\\to$ lỏng), đông đặc (lỏng $\\to$ rắn), bay hơi và sôi (lỏng $\\to$ khí/hơi), ngưng tụ (khí/hơi $\\to$ lỏng).",
            "Giải thích được vòng tuần hoàn của nước trong tự nhiên dựa trên sự chuyển thể của nước.",
        ],
        definition="Tính chất vật lí của chất là các tính chất không kèm theo sự biến đổi thành chất khác (màu sắc, mùi vị, tính tan, khối lượng riêng, nhiệt độ nóng chảy, nhiệt độ sôi...). Tính chất hóa học là khả năng của một chất biến đổi thành chất mới (như khả năng cháy, khả năng bị phân hủy, khả năng tác dụng với chất khác).",
        theory=(
            "### 1. Tính chất vật lí và Tính chất hóa học của chất\n"
            "- **Tính chất vật lí**: thể (rắn, lỏng, khí), màu sắc, mùi, vị, tính tan trong nước, tính dẫn điện, tính dẫn nhiệt, khối lượng riêng, nhiệt độ nóng chảy ($t_{\\text{nc}}$), nhiệt độ sôi ($t_s$).\n"
            "- **Tính chất hóa học**: khả năng biến đổi tạo thành **chất mới** (ví dụ: than đá cháy trong không khí tạo ra khí carbon dioxide $\\text{CO}_2$; đinh sắt để ngoài không khí ẩm bị gỉ tạo thành gỉ sắt nâu đỏ; đá vôi $\\text{CaCO}_3$ bị nung phân hủy thành vôi sống $\\text{CaO}$ và khí $\\text{CO}_2$).\n\n"
            "### 2. Các quá trình chuyển thể của chất\n"
            "- **Nóng chảy**: chuyển từ thể **rắn sang thể lỏng** (nước đá tan ở $0^\\circ\\text{C}$).\n"
            "- **Đông đặc**: chuyển từ thể **lỏng sang thể rắn** (làm đá trong tủ lạnh ở $0^\\circ\\text{C}$).\n"
            "- **Bay hơi**: chuyển từ thể **lỏng sang thể hơi** xảy ra trên **mặt thoáng** ở **mọi nhiệt độ**.\n"
            "- **Sôi**: chuyển từ thể **lỏng sang thể hơi** xảy ra cả **trong lòng và trên mặt thoáng** chất lỏng ở **nhiệt độ sôi xác định** (nước tinh khiết sôi ở $100^\\circ\\text{C}$).\n"
            "- **Ngưng tụ**: chuyển từ thể **khơi/khí sang thể lỏng** khi gặp lạnh (hơi nước gặp thành cốc nước đá ngưng tụ thành các giọt sương bên ngoài thành cốc)."
        ),
        formulas=[
            G(
                "Sơ đồ chuyển thể và Dấu hiệu tính chất hóa học",
                F("Sơ đồ các quá trình chuyển thể cơ bản", "$\\text{Rắn} \\underset{\\text{Đông đặc (tỏa nhiệt)}}{\\overset{\\text{Nóng chảy (thu nhiệt)}}{\\rightleftarrows}} \\text{Lỏng} \\underset{\\text{Ngưng tụ (tỏa nhiệt)}}{\\overset{\\text{Bay hơi / Sôi (thu nhiệt)}}{\\rightleftarrows}} \\text{Khí (Hơi)}$", "Sự chuyển thể chỉ làm thay đổi trạng thái vật lí của chất chứ không tạo ra chất mới."),
                F("Điểm nóng chảy và điểm sôi chuẩn của nước tinh khiết", "$t_{\\text{nc}}(\\text{H}_2\\text{O}) = 0^\\circ\\text{C}; \\qquad t_{\\text{sôi}}(\\text{H}_2\\text{O}) = 100^\\circ\\text{C} \\ (\\text{ở } 1\\text{ atm})$", "Trong suốt thời gian nước đá đang tan hoặc nước đang sôi, nhiệt độ của nước giữ không đổi."),
            )
        ],
        example="Khi đun nóng đường kính trắng (saccharose) trong ống nghiệm: lúc đầu đường chảy lỏng thành chất lỏng trong suốt không màu (giai đoạn 1); nếu tiếp tục đun mạnh thì đường chuyển thành chất rắn màu đen (than) và có mùi khét kèm hơi nước bốc lên (giai đoạn 2). Hãy cho biết giai đoạn nào thể hiện tính chất vật lí (chuyển thể) và giai đoạn nào thể hiện tính chất hóa học của đường?",
        example_answer="**Giai đoạn 1** (đường rắn chảy lỏng không đổi màu) là sự **nóng chảy**, không tạo ra chất mới nên thể hiện **tính chất vật lí**. **Giai đoạn 2** (đường biến thành than màu đen và nước) có sự tạo thành chất mới nên thể hiện **tính chất hóa học** (bị phân hủy nhiệt).",
        real_life="Hiện tượng mặt ngoài cốc nước đá có các giọt nước đọng lại không phải do nước thấm qua thành thủy tinh, mà do hơi nước trong không khí xung quanh gặp thành cốc lạnh bị ngưng tụ thành nước lỏng.",
        quiz=[
            mcq("biet", "Tính chất nào sau đây là **tính chất hóa học** của chất?", ["Khả năng của chất biến đổi tạo thành chất mới (như đinh sắt bị gỉ trong không khí ẩm, than cháy tạo khí $\\text{CO}_2$)", "Nhiệt độ nóng chảy và nhiệt độ sôi của chất", "Khối lượng riêng và tính dẫn điện của chất", "Màu sắc, mùi vị và tính tan trong nước của chất"], 0, "Tính chất hóa học gắn liền với khả năng biến đổi chất này thành chất khác."),
            mcq("biet", "Quá trình một chất chuyển từ thể **khí (hơi)** sang thể **lỏng** khi gặp lạnh được gọi là sự gì?", ["Sự ngưng tụ", "Sự bay hơi", "Sự nóng chảy", "Sự đông đặc"], 0, "Sự chuyển từ thể hơi/khí sang thể lỏng gọi là sự ngưng tụ (ví dụ hơi nước ngưng tụ thành mây, mưa, giọt sương)."),
            mcq("hieu", "Khi đặt một cốc nước đá lạnh trên bàn một lúc, ta thấy mặt ngoài thành cốc xuất hiện nhiều giọt nước nhỏ. Nguyên nhân của hiện tượng này là gì?", ["Hơi nước có sẵn trong không khí xung quanh cốc gặp thành cốc lạnh nên ngưng tụ thành các giọt nước lỏng", "Nước đá bên trong cốc thấm xuyên qua lớp thủy tinh ra ngoài", "Thủy tinh của cốc bị nóng chảy thành nước", "Không khí biến đổi hóa học thành nước"], 0, "Thủy tinh không thấm nước; các giọt nước bên ngoài là do hơi nước trong không khí gặp lạnh ngưng tụ lại."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tính chất và sự chuyển thể của chất:", [
                "Sự bay hơi của nước xảy ra trên mặt thoáng ở mọi nhiệt độ, còn sự sôi chỉ xảy ra ở nhiệt độ sôi xác định.",
                "Trong suốt thời gian nước tinh khiết đang sôi ở $100^\\circ\\text{C}$, dù tiếp tục đun thì nhiệt độ của nước vẫn giữ ở $100^\\circ\\text{C}$.",
                "Quá trình hòa tan muối ăn vào nước tạo thành nước muối là một tính chất hóa học của muối ăn.",
                "Nghề làm muối từ nước biển ở vùng ven biển ứng dụng quá trình bay hơi của nước dưới ánh nắng Mặt Trời và gió.",
            ], [True, True, False, True], "Ý c) sai vì tính tan của muối ăn trong nước không tạo ra chất mới (cô cạn lại thu được muối ăn) nên đó là tính chất vật lí."),
            short("vandung", "Ở áp suất chuẩn ($1\\text{ atm}$), hiệu số giữa nhiệt độ sôi ($100^\\circ\\text{C}$) và nhiệt độ đông đặc ($0^\\circ\\text{C}$) của nước tinh khiết bằng bao nhiêu độ Celsius ($^\\circ\\text{C}$)?", ["100"], "Hiệu số là $100^\\circ\\text{C} - 0^\\circ\\text{C} = 100^\\circ\\text{C}$.", unit="°C"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 3: Oxygen và tính chất của oxygen",
        icon="🫧",
        description="Tính chất vật lí của khí oxygen (O₂), vai trò duy trì sự hô hấp và sự cháy, cách thử nhận biết khí oxygen bằng tàn đóm đỏ.",
        requirements=[
            "Nêu được tính chất vật lí của khí oxygen ($\\text{O}_2$): ở điều kiện thường là chất khí không màu, không mùi, không vị, ít tan trong nước và nặng hơn không khí.",
            "Trình bày được hai vai trò sống còn của oxygen là duy trì sự hô hấp của sinh vật và duy trì sự cháy của nhiên liệu.",
            "Mô tả được cách nhận biết khí oxygen bằng que đóm còn tàn đỏ (tàn đóm bùng cháy thành ngọn lửa).",
        ],
        definition="Oxygen (kí hiệu hóa học $\\text{O}$, công thức phân tử $\\text{O}_2$) ở điều kiện thường là chất khí không màu, không mùi, không vị, ít tan trong nước, nặng hơn không khí và hóa lỏng ở $-183^\\circ\\text{C}$ (có màu xanh nhạt). Oxygen là chất khí duy trì sự hô hấp và duy trì sự cháy.",
        theory=(
            "### 1. Tính chất vật lí của Oxygen ($\\text{O}_2$)\n"
            "- Trạng thái: chất khí không màu, không mùi, không vị.\n"
            "- **Tính tan**: **ít tan trong nước** ($1\\text{ lít}$ nước ở $20^\\circ\\text{C}, 1\\text{ atm}$ chỉ hòa tan được khoảng $31\\text{ mL}$ khí oxygen). Vì vậy trong các đầm nuôi tôm cá mật độ cao phải lắp quạt sục khí để tăng lượng oxygen hòa tan trong nước.\n"
            "- Nặng hơn không khí (tỉ khối $\\dfrac{32}{29} \\approx 1{,}1$). Hóa lỏng ở $-183^\\circ\\text{C}$ (oxygen lỏng có màu xanh nhạt).\n\n"
            "### 2. Vai trò và Cách nhận biết khí Oxygen\n"
            "- **Duy trì sự hô hấp**: Con người, động vật và thực vật đều cần oxygen để hô hấp. Bình khí oxygen nén được dùng cho bệnh nhân khó thở, thợ lặn sâu, phi công bay cao và nhà du hành vũ trụ.\n"
            "- **Duy trì sự cháy**: Oxygen là chất duy trì sự cháy của gỗ, than, khí gas, xăng dầu (lưu ý: bản thân oxygen là **chất duy trì sự cháy** chứ không phải nhiên liệu cháy).\n"
            "- **Thí nghiệm nhận biết**: Đưa que đóm còn tàn đỏ vào lọ chứa khí oxygen, **tàn đóm bùng cháy mãnh liệt thành ngọn lửa**."
        ),
        formulas=[
            G(
                "Đặc trưng và Nhận biết khí Oxygen (O₂)",
                F("Tính chất vật lí cốt lõi của khí Oxygen", "$\\text{O}_2\\text{ (khí)}: \\text{Không màu, không mùi, không vị, ít tan trong nước, } t_{\\text{hóa lỏng}} = -183^\\circ\\text{C}$", "Khi thu khí $\\text{O}_2$ bằng cách đẩy không khí phải đặt **ngửa bình** (vì $\\text{O}_2$ nặng hơn không khí) hoặc thu bằng cách **đẩy nước** (vì $\\text{O}_2$ ít tan trong nước)."),
                F("Dấu hiệu nhận biết khí Oxygen", "$\\text{Que đóm còn tàn đỏ} + \\text{O}_2 \\longrightarrow \\text{Bùng cháy sáng thành ngọn lửa}$", "Dùng để phân biệt lọ chứa khí oxygen với không khí hoặc khí carbon dioxide."),
            )
        ],
        example="Vì sao trong các bể cá cảnh nhỏ trong nhà người ta thường lắp máy sục khí sủi bọt liên tục, còn ở các đầm nuôi tôm công nghiệp người ta phải lắp hệ thống quạt nước quay suốt ngày đêm?",
        example_answer="Vì khí oxygen trong không khí **ít tan trong nước**; việc sục khí hoặc quay quạt nước làm tăng diện tích tiếp xúc giữa nước và không khí, giúp hòa tan thêm nhiều khí oxygen vào nước để tôm, cá hô hấp không bị ngạt.",
        real_life="Trong y tế cấp cứu, bình khí oxygen tinh khiết giúp duy trì sự sống cho bệnh nhân suy hô hấp; trong công nghiệp luyện thép và hàn cắt kim loại, đèn xì oxygen – acetylene tạo ngọn lửa nóng tới $3000^\\circ\\text{C}$.",
        quiz=[
            mcq("biet", "Ở điều kiện thường, khí oxygen ($\\text{O}_2$) có những tính chất vật lí nào sau đây?", ["Không màu, không mùi, không vị, ít tan trong nước và nặng hơn không khí", "Có màu xanh đậm, mùi hắc và tan rất nhiều trong nước", "Không màu, mùi thơm và nhẹ hơn không khí", "Là chất lỏng màu trắng ở nhiệt độ phòng"], 0, "Ở điều kiện thường, khí oxygen không màu, không mùi, không vị, ít tan trong nước và nặng hơn không khí."),
            mcq("biet", "Để nhận biết một lọ thủy tinh không nhãn đang chứa khí oxygen nguyên chất, ta dùng cách thử nào sau đây?", ["Đưa que đóm còn tàn đỏ vào miệng lọ, nếu tàn đóm bùng cháy thành ngọn lửa thì đó là khí oxygen", "Đổ nước vôi trong vào lọ xem có vẩn đục không", "Ngửi mùi của chất khí trong lọ", "Quan sát màu sắc của khí ở nhiệt độ phòng"], 0, "Oxygen duy trì sự cháy mạnh nên làm que đóm còn tàn đỏ bùng cháy thành ngọn lửa."),
            mcq("hieu", "Khi thu khí oxygen vào ống nghiệm bằng phương pháp đẩy không khí, ta phải đặt ống nghiệm ở tư thế nào? Vì sao?", ["Đặt đứng ống nghiệm có miệng hướng lên trên (ngửa bình) vì khí oxygen nặng hơn không khí nên chìm xuống đáy ống", "Đặt úp ngược ống nghiệm vì khí oxygen nhẹ hơn không khí", "Đặt nằm ngang ống nghiệm", "Đậy kín nút trước khi dẫn khí vào"], 0, "Vì khí oxygen nặng hơn không khí nên khi dẫn vào đáy ống nghiệm đặt ngửa, oxygen sẽ chiếm chỗ từ dưới lên và đẩy không khí ra khỏi miệng ống."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về oxygen:", [
                "Oxygen duy trì sự hô hấp của con người, động vật, thực vật và duy trì sự cháy của nhiên liệu.",
                "Có thể thu khí oxygen bằng phương pháp đẩy nước vì khí oxygen ít tan trong nước.",
                "Ở $-183^\\circ\\text{C}$, oxygen hóa lỏng và có màu xanh nhạt.",
                "Cá và các sinh vật thủy sinh sống được dưới nước là vì khí oxygen tan vô hạn trong nước.",
            ], [True, True, True, False], "Ý d) sai vì khí oxygen **ít tan** trong nước (chỉ khoảng $31\\text{ mL}$ trong $1\\text{ lít}$ nước ở $20^\\circ\\text{C}$)."),
            short("vandung", "Biết ở $20^\\circ\\text{C}$ và $1\\text{ atm}$, $1\\text{ lít}$ nước hòa tan được tối đa $31\\text{ mL}$ khí oxygen. Hỏi một bể chứa $10\\text{ lít}$ nước ở cùng điều kiện đó hòa tan được tối đa bao nhiêu mililít ($\\text{mL}$) khí oxygen?", ["310"], "Lượng khí oxygen hòa tan tối đa trong $10\\text{ lít}$ nước là $10 \\cdot 31 = 310\\text{ mL}$.", unit="mL"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 4: Không khí, sự cháy và bảo vệ môi trường không khí",
        icon="🌍",
        description="Thành phần phần trăm thể tích của không khí (78% N₂, 21% O₂, 1% khí khác), 3 điều kiện của sự cháy, cách dập tắt đám cháy và bảo vệ không khí.",
        requirements=[
            "Nêu được thành phần theo thể tích của không khí khô, sạch: khoảng $78\\%$ khí nitrogen ($\\text{N}_2$), $21\\%$ khí oxygen ($\\text{O}_2$, xấp xỉ $\\dfrac{1}{5}$ thể tích không khí) và $1\\%$ các khí khác ($\\text{CO}_2$, hơi nước, khí hiếm $\\text{Ar}$...).",
            "Trình bày được thí nghiệm đốt nến trong ống thủy tinh úp trên chậu nước chứng minh oxygen chiếm khoảng $\\dfrac{1}{5}$ thể tích không khí.",
            "Nêu được 3 điều kiện cần và đủ để sự cháy xảy ra (chất cháy, oxygen, nhiệt độ bắt cháy), các nguyên tắc dập tắt đám cháy và biện pháp chống ô nhiễm không khí.",
        ],
        definition="Không khí là một hỗn hợp khí gồm khoảng $78\\%$ thể tích khí nitrogen ($\\text{N}_2$), $21\\%$ thể tích khí oxygen ($\\text{O}_2$, xấp xỉ $\\dfrac{1}{5}$ thể tích không khí) và khoảng $1\\%$ các khí khác (carbon dioxide $\\text{CO}_2$, hơi nước, khí hiếm...).",
        theory=(
            "### 1. Thành phần của không khí\n"
            "- Theo thể tích, không khí gồm:\n"
            "  - **$78\\%$ khí Nitrogen ($\\text{N}_2$)** (không duy trì sự cháy và sự hô hấp).\n"
            "  - **$21\\%$ khí Oxygen ($\\text{O}_2$)** (xấp xỉ $\\dfrac{1}{5}$ thể tích không khí).\n"
            "  - **$1\\%$ các chất khí khác**: khí carbon dioxide ($\\text{CO}_2$), hơi nước, khí hiếm (argon $\\text{Ar}$, neon $\\text{Ne}$...), bụi.\n"
            "- **Thí nghiệm chứng minh**: Đốt ngọn nến (hoặc photpho) trong ống trụ chia vạch úp trên chậu nước kiềm loãng; khi nến tắt do hết oxygen, mực nước dâng lên chiếm đúng **$\\dfrac{1}{5}$ thể tích** phần không khí trong ống ($V_{\\text{O}_2} \\approx \\dfrac{1}{5}V_{\\text{kk}}$).\n\n"
            "### 2. Điều kiện phát sinh sự cháy, Dập tắt đám cháy và Bảo vệ không khí\n"
            "- **Tam giác lửa (3 điều kiện để sự cháy xảy ra)**: (1) Phải có chất cháy (nhiên liệu); (2) Phải có đủ khí oxygen; (3) Phải có nguồn nhiệt đạt tới nhiệt độ bắt cháy.\n"
            "- **Nguyên tắc dập tắt đám cháy**: Hạ nhiệt độ chất cháy xuống dưới nhiệt độ bắt cháy và cách li chất cháy với khí oxygen:\n"
            "  - Đám cháy gỗ, giấy, vải thông thường: phun nước hoặc dùng bình chữa cháy.\n"
            "  - **Đám cháy xăng, dầu**: tuyệt đối **KHÔNG dội nước** (vì xăng dầu nhẹ hơn nước và không tan trong nước sẽ nổi lên lan rộng đám cháy); phải phủ chăn ướt, đổ cát hoặc dùng bình bọt/khí $\\text{CO}_2$.\n"
            "  - **Đám cháy thiết bị điện**: phải **ngắt cầu dao điện ngay** rồi dùng bình chữa cháy khí $\\text{CO}_2$ hoặc bột khô (không dội nước khi chưa ngắt điện)."
        ),
        formulas=[
            G(
                "Thành phần phần trăm thể tích không khí",
                F("Tỉ lệ thể tích các khí trong không khí sạch", "$\\%V_{\\text{N}_2} \\approx 78\\%; \\qquad \\%V_{\\text{O}_2} \\approx 21\\% \\approx \\dfrac{1}{5}; \\qquad \\%V_{\\text{khí khác}} \\approx 1\\%$", "Công thức tính nhanh thể tích oxygen trong không khí: $V_{\\text{O}_2} = 0{,}21 \\cdot V_{\\text{kk}} \\approx \\dfrac{1}{5} V_{\\text{kk}}$."),
                F("Hai nguyên tắc dập tắt đám cháy", "$\\text{Dập tắt sự cháy} \\iff \\begin{cases} \\text{Hạ nhiệt độ } t < t_{\\text{bắt cháy}} \\\\ \\text{Cách li chất cháy khỏi khí } \\text{O}_2 \\end{cases}$", "Đám cháy xăng dầu phải phủ cát hoặc chăn chiên ướt, tuyệt đối không dội nước."),
            )
        ],
        example="Một phòng học có thể tích không khí là $V_{\\text{kk}} = 150\\text{ m}^3$. Biết khí oxygen chiếm $21\\%$ thể tích không khí. Hãy tính thể tích khí oxygen $V_{\\text{O}_2}$ có trong phòng học đó.",
        example_answer="Thể tích khí oxygen có trong phòng học là $V_{\\text{O}_2} = 21\\% \\cdot V_{\\text{kk}} = 0{,}21 \\cdot 150 = 31{,}5\\text{ m}^3$.",
        real_life="Các bình chữa cháy bằng khí nén $\\text{CO}_2$ khi phun vào đám cháy vừa làm lạnh đột ngột vùng cháy vừa tạo lớp khí $\\text{CO}_2$ nặng hơn không khí bao phủ đám cháy, ngăn chất cháy tiếp xúc với oxygen.",
        quiz=[
            mcq("biet", "Trong không khí khô và sạch, chất khí nào chiếm tỉ lệ thể tích lớn nhất ($\\approx 78\\%$) và chất khí nào chiếm khoảng $21\\%$?", ["Khí nitrogen ($\\text{N}_2$) chiếm $78\\%$ và khí oxygen ($\\text{O}_2$) chiếm $21\\%$", "Khí oxygen chiếm $78\\%$ và khí nitrogen chiếm $21\\%$", "Khí carbon dioxide chiếm $78\\%$ và khí oxygen chiếm $21\\%$", "Hơi nước chiếm $78\\%$ và khí hydrogen chiếm $21\\%$"], 0, "Trong không khí, nitrogen chiếm khoảng $78\\%$, oxygen chiếm khoảng $21\\%$ và $1\\%$ là các khí khác."),
            mcq("biet", "Vì sao khi xảy ra đám cháy do **xăng hoặc dầu hỏa** tràn ra sàn, ta tuyệt đối **không** được dùng nước để dập lửa?", ["Vì xăng, dầu nhẹ hơn nước và không tan trong nước nên sẽ nổi lên mặt nước làm đám cháy lan rộng hơn", "Vì nước là một chất nhiên liệu tự bốc cháy", "Vì xăng dầu nặng hơn nước nên chìm xuống đáy", "Vì nước phản ứng với xăng tạo ra vàng"], 0, "Xăng dầu không tan trong nước và nhẹ hơn nước ($D \\approx 0{,}8\\text{ g/cm}^3$) nên dội nước chỉ làm xăng dầu nổi lên trôi lan ra diện tích rộng hơn."),
            mcq("hieu", "Khi úp một ống thủy tinh chia thành $5$ phần thể tích bằng nhau lên một ngọn nến đang cháy đặt trong chậu nước, sau khi nến tắt và ống nguội thì mực nước trong ống dâng lên chiếm khoảng mấy phần thể tích ống?", ["Chiếm khoảng $1$ phần (tức $\\dfrac{1}{5}$ thể tích ống) do khí oxygen đã phản ứng hết", "Chiếm toàn bộ $5$ phần của ống", "Chiếm $4$ phần của ống", "Mực nước không hề dâng lên"], 0, "Oxygen chiếm khoảng $21\\% \\approx \\dfrac{1}{5}$ thể tích không khí; khi oxygen cháy hết, nước dâng lên thế chỗ khoảng $\\dfrac{1}{5}$ thể tích ống."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về không khí và bảo vệ môi trường không khí:", [
                "Không khí là một hỗn hợp gồm nhiều chất khí chứ không phải là một chất tinh khiết.",
                "Khí carbon dioxide ($\\text{CO}_2$), hơi nước và khí hiếm argon ($\\text{Ar}$) chiếm tổng cộng khoảng $1\\%$ thể tích không khí.",
                "Đốt rơm rạ ngoài đồng và xả khói bụi từ xe cộ, nhà máy giúp làm sạch bầu không khí.",
                "Trồng nhiều cây xanh và chuyển sang sử dụng phương tiện giao thông điện là biện pháp thiết thực bảo vệ môi trường không khí.",
            ], [True, True, False, True], "Ý c) sai vì đốt rơm rạ và xả khí thải sinh ra nhiều bụi mịn ($\\text{PM}_{2.5}$) và khí độc ($\\text{CO}, \\text{SO}_2, \\text{NO}_2$) gây ô nhiễm không khí nghiêm trọng."),
            short("vandung", "Biết khí oxygen chiếm $21\\%$ thể tích không khí. Trong $200\\text{ lít}$ không khí có chứa bao nhiêu lít khí oxygen?", ["42"], "Thể tích khí oxygen là $V_{\\text{O}_2} = 0{,}21 \\cdot 200 = 42\\text{ lít}$.", unit="lít"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 5: Một số vật liệu thông dụng",
        icon="🧱",
        description="Tính chất, ứng dụng của các vật liệu thông dụng (kim loại, nhựa, gỗ, thủy tinh, cao su, gốm sứ) và mô hình 3R sử dụng vật liệu bền vững.",
        requirements=[
            "Nêu được khái niệm vật liệu và kể tên các vật liệu thông dụng: kim loại, nhựa, gỗ, cao su, thủy tinh, gốm sứ, vật liệu composite.",
            "Liên hệ được tính chất của mỗi loại vật liệu (tính dẫn điện, dẫn nhiệt, tính đàn hồi, trong suốt, chịu nhiệt, ăn mòn) với ứng dụng của chúng.",
            "Trình bày được cách sử dụng vật liệu an toàn, hiệu quả và bảo vệ môi trường theo quy tắc **3R (Reduce – Reuse – Recycle)**.",
        ],
        definition="Vật liệu là chất hoặc hỗn hợp một số chất được con người sử dụng như đầu vào để chế tạo các đồ vật, dụng cụ, máy móc hoặc xây dựng công trình (như kim loại, nhựa, gỗ, cao su, thủy tinh, gốm sứ).",
        theory=(
            "### 1. Tính chất và ứng dụng của một số vật liệu thông dụng\n"
            "- **Kim loại** (sắt, thép, nhôm, đồng): có ánh kim, **dẫn điện và dẫn nhiệt tốt**, có tính dẻo, bền cơ học; nhưng một số kim loại như sắt dễ bị **gỉ (ăn mòn)** trong không khí ẩm $\\implies$ làm dây điện, nồi nấu, khung nhà, cầu cống.\n"
            "- **Nhựa (chất dẻo)**: nhẹ, không dẫn điện, không dẫn nhiệt, không thấm nước, dễ tạo hình nhưng **rất khó phân hủy trong tự nhiên** (gây ô nhiễm trắng) và một số loại nhựa kém chất lượng sinh chất độc ở nhiệt độ cao.\n"
            "- **Cao su**: có **tính đàn hồi cao**, không thấm nước, không dẫn điện, chịu mài mòn $\\implies$ làm lốp xe, găng tay cách điện, gioăng đệm.\n"
            "- **Thủy tinh**: **trong suốt cho ánh sáng truyền qua**, không thấm nước, không tác dụng với nhiều hóa chất nhưng giòn, dễ vỡ $\\implies$ làm cửa kính, dụng cụ thí nghiệm.\n"
            "- **Gốm, sứ, đất nung**: cứng, bền nhiệt, cách điện tốt nhưng giòn $\\implies$ làm gạch ngói, bát đĩa, sứ cách điện cao thế.\n\n"
            "### 2. Sử dụng vật liệu theo mô hình 3R\n"
            "- **Reduce (Giảm thiểu)** – **Reuse (Tái sử dụng)** – **Recycle (Tái chế)** nhằm tiết kiệm tài nguyên và giảm rác thải nhựa ra môi trường."
        ),
        formulas=[
            G(
                "Liên hệ Tính chất – Ứng dụng vật liệu và Quy tắc 3R",
                F("Quy tắc ghép cặp Tính chất đặc trưng ➔ Ứng dụng", "$\\text{Đồng (dẫn điện)} \\to \\text{Lõi dây}; \\quad \\text{Nhựa/Cao su (cách điện)} \\to \\text{Vỏ bọc}; \\quad \\text{Thủy tinh (trong suốt)} \\to \\text{Cửa kính}$", "Mỗi đồ vật thường kết hợp nhiều vật liệu khác nhau để tận dụng ưu điểm của từng vật liệu."),
                F("Mô hình 3R phát triển bền vững", "$\\text{3R} = \\text{Reduce (Giảm thiểu)} + \\text{Reuse (Tái sử dụng)} + \\text{Recycle (Tái chế)}$", "Ưu tiên dùng hộp thủy tinh, inox hoặc túi vải sử dụng nhiều lần thay cho đồ nhựa dùng một lần."),
            )
        ],
        example="Trên một chiếc ấm đun nước siêu tốc dùng trong gia đình, người ta dùng thép không gỉ (inox) làm thân ấm và mâm nhiệt, dùng nhựa cứng làm tay cầm và vỏ công tắc, dùng cao su làm vòng đệm nắp ấm. Hãy giải thích vì sao lại chọn các vật liệu đó cho từng bộ phận.",
        example_answer="- **Thép không gỉ (inox)** bền, dẫn nhiệt tốt và không bị gỉ khi đun nước sôi nên dùng làm thân ấm và mâm nhiệt.\n- **Nhựa cứng** cách điện và cách nhiệt tốt nên dùng làm tay cầm và công tắc để không bị bỏng hay điện giật.\n- **Cao su** có tính đàn hồi và kín khít nên dùng làm vòng đệm nắp ấm.",
        real_life="Để bảo vệ các công trình bằng sắt thép (cửa sắt, khung cầu, vỏ tàu biển) khỏi bị gỉ sét do oxygen và độ ẩm không khí, người ta luôn sơn phủ chống gỉ hoặc tráng kẽm bên ngoài bề mặt sắt.",
        quiz=[
            mcq("biet", "Vật liệu nào sau đây có tính **đàn hồi cao**, không thấm nước, chịu mài mòn tốt và được dùng để sản xuất lốp xe máy, ô tô?", ["Cao su", "Thủy tinh", "Gốm sứ", "Đá vôi"], 0, "Cao su có tính đàn hồi tốt, chịu ma sát và không thấm nước nên dùng làm săm lốp xe."),
            mcq("biet", "Vì sao các dụng cụ thí nghiệm hóa học (như ống nghiệm, cốc đong, bình cầu) thường được làm bằng **thủy tinh chịu nhiệt**?", ["Vì thủy tinh trong suốt giúp dễ quan sát hiện tượng bên trong và bền với hầu hết các hóa chất", "Vì thủy tinh dẫn điện tốt hơn đồng", "Vì thủy tinh có tính đàn hồi dẻo như cao su", "Vì thủy tinh rơi không bao giờ vỡ"], 0, "Thủy tinh trong suốt dễ quan sát và trơ với hầu hết hóa chất thông thường."),
            mcq("hieu", "Để hạn chế rác thải nhựa gây ô nhiễm môi trường ('ô nhiễm trắng') và bảo vệ sức khỏe khi bảo quản thức ăn nóng hoặc quay trong lò vi sóng, ta nên chọn hộp đựng làm bằng vật liệu nào?", ["Hộp thủy tinh chịu nhiệt hoặc hộp sứ", "Hộp xốp nhựa dùng một lần", "Túi nilon mỏng", "Hộp bằng sắt chưa sơn"], 0, "Hộp thủy tinh chịu nhiệt và hộp sứ an toàn ở nhiệt độ cao, không tiết ra chất độc hại như nhựa xốp và dùng lại được nhiều lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về các vật liệu thông dụng:", [
                "Kim loại dẫn điện và dẫn nhiệt tốt, còn nhựa, cao su, gỗ khô và gốm sứ cách điện tốt.",
                "Để chống gỉ cho các đồ vật bằng sắt thép, người ta thường bôi dầu mỡ hoặc sơn phủ bề mặt để ngăn sắt tiếp xúc với oxygen và hơi nước.",
                "Rác thải nhựa và túi nilon có thể tự phân hủy hoàn toàn trong đất chỉ sau $2$ đến $3$ ngày.",
                "Quy tắc 3R trong sử dụng vật liệu bền vững gồm: Giảm thiểu (Reduce), Tái sử dụng (Reuse) và Tái chế (Recycle).",
            ], [True, True, False, True], "Ý c) sai vì rác thải nhựa và túi nilon phải mất hàng trăm năm mới phân hủy trong môi trường tự nhiên."),
            short("vandung", "Mô hình sử dụng vật liệu tiết kiệm, hiệu quả và bảo vệ môi trường gồm mấy chữ R (Reduce – Giảm thiểu, Reuse – Tái sử dụng, Recycle – Tái chế)?", ["3"], "Mô hình gồm $3$ chữ R (3R: Reduce, Reuse, Recycle)."),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 6: Một số nhiên liệu",
        icon="🔥",
        description="Phân loại nhiên liệu theo trạng thái (rắn, lỏng, khí; nhiên liệu hóa thạch và nhiên liệu sinh học), tính chất cháy tỏa nhiệt và cách sử dụng an toàn, tiết kiệm.",
        requirements=[
            "Nêu được nhiên liệu (chất đốt) là những chất khi cháy đều tỏa nhiệt và phát sáng.",
            "Phân loại được các nhiên liệu thông dụng theo trạng thái: nhiên liệu rắn (than đá, củi, nến), nhiên liệu lỏng (xăng, dầu diesel, cồn), nhiên liệu khí (gas, biogas, khí thiên nhiên).",
            "Giải thích được các biện pháp tăng hiệu quả đốt cháy nhiên liệu (cung cấp vừa đủ oxygen, tăng diện tích tiếp xúc như chẻ nhỏ củi, tạo lỗ tổ ong trên viên than) và sử dụng nhiên liệu an toàn, bền vững.",
        ],
        definition="Nhiên liệu (chất đốt) là những chất khi cháy đều tỏa nhiệt và phát sáng, được sử dụng rộng rãi trong đun nấu, sưởi ấm, giao thông vận tải và sản xuất công nghiệp.",
        theory=(
            "### 1. Phân loại nhiên liệu\n"
            "- **Theo trạng thái tồn tại**:\n"
            "  1. **Nhiên liệu rắn**: than đá, than gỗ, củi, tre, sáp nến.\n"
            "  2. **Nhiên liệu lỏng**: xăng, dầu hỏa, dầu diesel (DO), cồn (ethanol).\n"
            "  3. **Nhiên liệu khí**: khí mỏ dầu, khí thiên nhiên, khí gas hóa lỏng (LPG), khí lò cốc, khí sinh học (biogas).\n"
            "- **Theo nguồn gốc và khả năng tái tạo**:\n"
            "  - *Nhiên liệu hóa thạch* (than đá, dầu mỏ, khí thiên nhiên): không tái tạo, mất hàng trăm triệu năm hình thành, khi đốt phát thải nhiều $\\text{CO}_2$.\n"
            "  - *Nhiên liệu sinh học / xanh* (xăng sinh học $\\text{E5}$, khí biogas, viên nén mùn cưa): thân thiện với môi trường, thuộc nguồn năng lượng tái tạo.\n\n"
            "### 2. Sử dụng nhiên liệu an toàn và hiệu quả\n"
            "- **Tăng hiệu suất cháy**:\n"
            "  - Cung cấp **đủ không khí (oxygen)** cho quá trình cháy (nếu thiếu oxygen, nhiên liệu cháy không hoàn toàn sinh ra khói đen muội than và **khí $\\text{CO}$ cực độc**; nếu thừa quá nhiều không khí sẽ tốn nhiệt làm nóng không khí thừa).\n"
            "  - **Tăng diện tích tiếp xúc** của nhiên liệu với không khí: chẻ nhỏ củi, tạo các lỗ thông khí cho viên than tổ ong, phun nhiên liệu lỏng thành dạng sương mù trong buồng đốt động cơ."
        ),
        formulas=[
            G(
                "Tính chất của Nhiên liệu và Nguyên tắc đốt cháy hiệu quả",
                F("Phản ứng cháy tổng quát của nhiên liệu", "$\\text{Nhiên liệu} + \\text{O}_2 \\xrightarrow{t^\\circ} \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{Nhiệt lượng } Q \\quad (\\text{nếu thiếu } \\text{O}_2 \\text{ sinh ra khí độc } \\text{CO})$", "Tuyệt đối không đốt than củi, than tổ ong hoặc chạy máy phát điện xăng dầu trong phòng kín vì sinh ra khí $\\text{CO}$ gây ngạt tử vong!"),
                F("Hai biện pháp tăng hiệu suất đốt cháy nhiên liệu", "$\\text{Đốt cháy hoàn toàn} \\iff \\begin{cases} \\text{Cung cấp vừa đủ khí } \\text{O}_2 \\text{ (quạt gió, thông gió)} \\\\ \\text{Tăng diện tích tiếp xúc (chẻ củi, phun sương xăng dầu)} \\end{cases}$", "Xăng sinh học E5 gồm $95\\%$ thể tích xăng khoáng và $5\\%$ thể tích cồn sinh học ethanol."),
            )
        ],
        example="Vì sao khi đun bếp củi, người ta thường chẻ các khúc củi to thành những thanh củi nhỏ và xếp củi có khe thoáng thay vì chất khít đặc vào nhau?",
        example_answer="Việc chẻ nhỏ củi làm **tăng diện tích bề mặt tiếp xúc** của củi với khí oxygen, còn việc xếp củi có khe thoáng giúp không khí (**oxygen**) lưu thông vào buồng đốt dễ dàng, nhờ đó củi bắt lửa nhanh hơn và cháy hoàn toàn, tỏa nhiều nhiệt hơn.",
        real_life="Xăng sinh học E5 RON 92 (pha $5\\%$ ethanol sản xuất từ sắn, mía) và hầm ủ khí Biogas tại các trang trại chăn nuôi giúp tận dụng phụ phẩm nông nghiệp và giảm phát thải khí nhà kính.",
        quiz=[
            mcq("biet", "Tính chất đặc trưng chung của mọi loại **nhiên liệu (chất đốt)** là gì?", ["Khi cháy đều tỏa nhiệt và phát sáng", "Đều là chất lỏng tan tốt trong nước", "Đều dẫn điện tốt như kim loại", "Đều không tác dụng với khí oxygen"], 0, "Nhiên liệu là những chất khi cháy đều tỏa nhiệt và phát sáng."),
            mcq("biet", "Nhóm các chất nào sau đây đều thuộc loại **nhiên liệu khí**?", ["Khí thiên nhiên, khí gas đun bếp (LPG) và khí sinh học (biogas)", "Xăng, dầu hỏa và cồn", "Than đá, củi khô và sáp nến", "Đá vôi, cát và quặng sắt"], 0, "Khí thiên nhiên, khí gas và khí biogas đều là các nhiên liệu ở thể khí."),
            mcq("hieu", "Vì sao việc đốt than tổ ong, than củi để sưởi ấm hoặc chạy máy phát điện chạy xăng trong **phòng đóng kín cửa** lại cực kì nguy hiểm đến tính mạng?", ["Vì trong phòng kín lượng oxygen giảm dần làm nhiên liệu cháy không hoàn toàn sinh ra khí $\\text{CO}$ (carbon monoxide) và $\\text{CO}_2$ gây ngạt thở tử vong", "Vì than củi làm nhiệt độ phòng giảm xuống dưới $0^\\circ\\text{C}$", "Vì than cháy sinh ra thêm quá nhiều khí oxygen", "Vì máy phát điện hút hết trọng lực trong phòng"], 0, "Trong phòng kín thiếu oxygen, sự cháy sản sinh khí $\\text{CO}$ không màu, không mùi nhưng kết hợp chặt với hemoglobin trong máu gây ngạt thở tử vong nhanh chóng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nhiên liệu và cách sử dụng:", [
                "Tạo nhiều lỗ nhỏ xuyên dọc viên than tổ ong giúp tăng diện tích tiếp xúc của than với oxygen không khí để than cháy đều.",
                "Trong động cơ ô tô, xe máy, xăng được phun thành dạng sương hòa trộn với không khí trước khi đốt cháy để tăng hiệu suất.",
                "Than đá, dầu mỏ và khí thiên nhiên là các nguồn nhiên liệu tái tạo vô tận.",
                "Khi ngửi thấy mùi khí gas bị rò rỉ trong bếp, cần khóa ngay van bình gas, mở toang cửa thông thoáng và tuyệt đối không bật lửa hay bật/tắt công tắc điện.",
            ], [True, True, False, True], "Ý c) sai vì than đá, dầu mỏ và khí thiên nhiên là nhiên liệu hóa thạch không tái tạo, có nguy cơ cạn kiệt."),
            short("vandung", "Xăng sinh học E5 là hỗn hợp gồm $95\\%$ thể tích xăng khoáng truyền thống và bao nhiêu phần trăm ($\\%$) thể tích cồn sinh học (ethanol)?", ["5"], "Kí hiệu E5 nghĩa là chứa $5\\%$ thể tích ethanol sinh học ($100\\% - 95\\% = 5\\%$).", unit="%"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 7: Một số nguyên liệu khoáng",
        icon="⛏️",
        description="Khái niệm nguyên liệu, tính chất và ứng dụng của đá vôi (CaCO₃), quặng khoáng sản, cát thạch anh và khai thác bền vững.",
        requirements=[
            "Nêu được nguyên liệu là vật liệu tự nhiên chưa qua xử lí (hoặc mới sơ chế) cần được chuyển hóa để tạo ra sản phẩm công nghiệp.",
            "Trình bày được tính chất của đá vôi (thành phần chính là $\\text{CaCO}_3$: khá cứng, bị phân hủy khi nung tạo vôi sống, sủi bọt khí khi gặp acid) và ứng dụng sản xuất xi măng, vôi sống.",
            "Kể tên được một số loại quặng quan trọng (quặng bauxite sản xuất nhôm, quặng hematite sản xuất sắt, quặng apatite sản xuất phân lân) và nguyên tắc khai thác tài nguyên khoáng sản bền vững.",
        ],
        definition="Nguyên liệu là vật liệu tự nhiên (thường là các khoáng sản như đá vôi, đất sét, cát, quặng kim loại, dầu mỏ, nước biển, gỗ, tre...) được dùng làm đầu vào cho các quá trình sản xuất công nghiệp để chế biến ra vật liệu và sản phẩm mới.",
        theory=(
            "### 1. Đá vôi và một số loại quặng nguyên liệu\n"
            "- **Đá vôi** (thành phần chính là calcium carbonate $\\text{CaCO}_3$):\n"
            "  - **Tính chất**: chất rắn, khá cứng, không tan trong nước; khi nung ở nhiệt độ cao bị phân hủy thành vôi sống ($\\text{CaO}$) và khí $\\text{CO}_2$; khi nhỏ giấm ăn hoặc dung dịch hydrochloric acid ($\\text{HCl}$) vào đá vôi thì **sủi bọt khí** không màu ($\\text{CO}_2$) làm mòn đá.\n"
            "  - **Ứng dụng**: làm đá xây dựng, sản xuất vôi sống, sản xuất **xi măng** (cùng với đất sét), làm phấn viết, tượng đá.\n"
            "- **Các loại quặng khoáng sản**:\n"
            "  - **Quặng sắt** (hematite, magnetite): nguyên liệu luyện gang, thép.\n"
            "  - **Quặng bauxite** (giàu $\\text{Al}_2\\text{O}_3$): nguyên liệu sản xuất kim loại nhôm ($\\text{Al}$).\n"
            "  - **Quặng apatite, phosphorite**: nguyên liệu sản xuất phân bón lân.\n"
            "  - **Cát trắng (thạch anh $\\text{SiO}_2$)**: nguyên liệu sản xuất thủy tinh.\n\n"
            "### 2. Khai thác và sử dụng nguyên liệu an toàn, hiệu quả, bền vững\n"
            "- Khoáng sản tự nhiên là tài nguyên **không tái tạo** (trữ lượng hữu hạn), việc khai thác bừa bãi gây sạt lở, cạn kiệt và ô nhiễm môi trường.\n"
            "- Cần khai thác theo quy hoạch, áp dụng **chuỗi sản xuất khép kín** (tận dụng chất thải ngành này làm nguyên liệu ngành khác) và tăng cường tái chế kim loại, thủy tinh."
        ),
        formulas=[
            G(
                "Các chuỗi chuyển hóa từ Nguyên liệu khoáng sang Vật liệu",
                F("Tính chất hóa học đặc trưng của đá vôi (CaCO₃)", "$\\text{Đá vôi } (\\text{CaCO}_3) \\xrightarrow{t^\\circ} \\text{Vôi sống } (\\text{CaO}) + \\text{CO}_2\\uparrow; \\qquad \\text{Đá vôi} + \\text{Acid/Giấm} \\longrightarrow \\text{Sủi bọt khí } \\text{CO}_2\\uparrow$", "Do đá vôi tác dụng với acid nên mưa acid làm ăn mòn các bức tượng đá vôi, cẩm thạch ngoài trời."),
                F("Các nguyên liệu sản xuất Vật liệu công nghiệp chính", "$\\text{Đá vôi + Đất sét} \\to \\text{Xi măng}; \\quad \\text{Cát trắng} \\to \\text{Thủy tinh}; \\quad \\text{Quặng Bauxite} \\to \\text{Nhôm}; \\quad \\text{Quặng Sắt} \\to \\text{Gang, Thép}$", "Nước biển là nguyên liệu tự nhiên để sản xuất muối ăn ($\\text{NaCl}$) và xút ($\\text{NaOH}$), khí chlorine ($\\text{Cl}_2$)."),
            )
        ],
        example="Khi nhỏ vài giọt nước cốt chanh hoặc giấm ăn lên bề mặt một mẫu đá vôi (hoặc vỏ trứng, vỏ sò có thành phần chính là $\\text{CaCO}_3$), ta quan sát thấy hiện tượng gì? Từ đó hãy giải thích vì sao các công trình kiến trúc và tượng điêu khắc bằng đá vôi ngoài trời lại bị ăn mòn nhanh ở những vùng có mưa acid?",
        example_answer="Khi nhỏ nước chanh hoặc giấm ăn (chứa acid) lên đá vôi, ta thấy **sủi bọt khí** không màu ($\\text{CO}_2$) và bề mặt đá vôi bị hòa tan dần. Ở những vùng công nghiệp ô nhiễm có mưa acid, lượng acid trong nước mưa tác dụng hóa học với $\\text{CaCO}_3$ trong đá vôi làm các bức tượng và công trình bị ăn mòn, hư hại.",
        real_life="Tại Việt Nam, đá vôi ở Ninh Bình, Hà Nam, Quảng Ninh là nguyên liệu cho các nhà máy xi măng lớn; quặng bauxite ở Tây Nguyên dùng sản xuất alumina/nhôm; quặng apatite ở Lào Cai dùng sản xuất phân lân.",
        quiz=[
            mcq("biet", "Nguyên liệu chính dùng để sản xuất **xi măng** và **vôi sống** trong công nghiệp xây dựng là gì?", ["Đá vôi (cùng với đất sét khi sản xuất xi măng)", "Quặng bauxite", "Gỗ thông", "Mủ cây cao su"], 0, "Đá vôi là nguyên liệu chính để nung vôi sống và nghiền nung cùng đất sét để sản xuất xi măng."),
            mcq("biet", "Khi nhỏ dung dịch hydrochloric acid ($\\text{HCl}$) hoặc giấm ăn vào một mẫu đá vôi thì xuất hiện hiện tượng đặc trưng nào?", ["Sủi bọt khí mạnh trên bề mặt đá vôi và đá vôi tan dần", "Đá vôi phát sáng rực rỡ", "Đá vôi biến thành kim loại sắt", "Không có bất kì hiện tượng gì xảy ra"], 0, "Thành phần chính của đá vôi là $\\text{CaCO}_3$ tác dụng với acid giải phóng bọt khí $\\text{CO}_2$."),
            mcq("hieu", "Quặng **bauxite** (phân bố nhiều ở khu vực Tây Nguyên nước ta) là nguyên liệu chính dùng để sản xuất kim loại nào sau đây?", ["Nhôm ($\\text{Al}$)", "Sắt ($\\text{Fe}$)", "Vàng ($\\text{Au}$)", "Thủy ngân ($\\text{Hg}$)"], 0, "Quặng bauxite giàu aluminium oxide ($\\text{Al}_2\\text{O}_3$) là nguyên liệu chính để sản xuất kim loại nhôm."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nguyên liệu:", [
                "Các loại quặng khoáng sản và đá vôi trong tự nhiên là nguồn tài nguyên không tái tạo nên cần khai thác hợp lí, tiết kiệm.",
                "Nước biển là nguyên liệu tự nhiên dùng để sản xuất muối ăn.",
                "Cát trắng (thạch anh) là nguyên liệu chính để nấu luyện thủy tinh.",
                "Khai thác đá vôi và khoáng sản tự do không quy hoạch hoàn toàn không gây ảnh hưởng gì đến cảnh quan và môi trường.",
            ], [True, True, True, False], "Ý d) sai vì khai thác khoáng sản tự phát không quy hoạch làm hủy hoại cảnh quan, gây bụi, sạt lở và cạn kiệt tài nguyên."),
            short("vandung", "Cho 4 đối tượng sau: (1) Đá vôi tự nhiên, (2) Quặng sắt, (3) Viên gạch xây đã nung thành phẩm, (4) Cát thạch anh. Có bao nhiêu đối tượng trong danh sách trên là **nguyên liệu tự nhiên**?", ["3"], "Đá vôi (1), quặng sắt (2) và cát thạch anh (4) là $3$ nguyên liệu tự nhiên; còn viên gạch xây (3) là vật liệu nhân tạo đã qua chế biến."),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 8: Một số lương thực, thực phẩm",
        icon="🌾",
        description="Phân biệt lương thực và thực phẩm, 4 nhóm chất dinh dưỡng chính (carbohydrate, protein, lipid, vitamin & chất khoáng) và an toàn vệ sinh thực phẩm.",
        requirements=[
            "Phân biệt được lương thực (gạo, ngô, khoai, sắn, lúa mì – giàu tinh bột/carbohydrate) và các thực phẩm cung cấp chất đạm, chất béo, vitamin.",
            "Nêu được vai trò của 4 nhóm chất dinh dưỡng cơ bản đối với cơ thể người: chất bột đường (carbohydrate), chất đạm (protein), chất béo (lipid), vitamin và chất khoáng.",
            "Trình bày được nguyên nhân khiến lương thực – thực phẩm dễ bị ôi thiu, nấm mốc và cách bảo quản, sử dụng an toàn.",
        ],
        definition="Lương thực là thức ăn chứa hàm lượng lớn tinh bột (carbohydrate), cung cấp nguồn năng lượng chính cho cơ thể (như lúa gạo, ngô, khoai, sắn, lúa mì). Thực phẩm (thức ăn) là các sản phẩm chứa chất bột đường, chất đạm (protein), chất béo (lipid), vitamin và khoáng chất mà con người ăn, uống ở dạng tươi sống hoặc đã chế biến.",
        theory=(
            "### 1. Bốn nhóm chất dinh dưỡng trong lương thực – thực phẩm\n"
            "1. **Carbohydrate (Chất bột đường – Tinh bột, đường)**: nguồn cung cấp **năng lượng chính** cho mọi hoạt động của cơ thể; có nhiều trong **lương thực** (gạo, ngô, khoai, sắn, bánh mì).\n"
            "2. **Protein (Chất đạm)**: cấu tạo và tái tạo các tế bào, cơ bắp, kháng thể, enzyme; có nhiều trong thịt, cá, trứng, sữa, tôm, cua và các loại đậu (đậu nành).\n"
            "3. **Lipid (Chất béo)**: dự trữ năng lượng, giúp hòa tan các vitamin tan trong dầu ($\\text{A}, \\text{D}, \\text{E}, \\text{K}$) và giữ ấm cơ thể; có nhiều trong mỡ động vật, dầu thực vật, lạc (đậu phộng), vừng (mè), bơ.\n"
            "4. **Vitamin và Chất khoáng** ($\\text{Ca}, \\text{Fe}, \\text{I}, \\text{Zn}$...): tuy cần lượng nhỏ nhưng không thể thiếu để tăng sức đề kháng và điều hòa trao đổi chất; có nhiều trong rau xanh và trái cây tươi.\n\n"
            "### 2. Tính chất và Bảo quản an toàn lương thực – thực phẩm\n"
            "- Lương thực, thực phẩm để lâu ngoài không khí ẩm rất dễ bị vi khuẩn, nấm mốc xâm nhập gây **biến đổi hóa học (lên men chua, ôi thiu, mốc hỏng)** sinh ra độc tố (như độc tố aflatoxin trong lạc, ngô mốc hoặc solanine trong khoai tây mọc mầm xanh).\n"
            "- **Cách bảo quản**: phơi/sấy khô (với hạt ngũ cốc), bảo quản lạnh trong tủ lạnh, hút chân không, ướp muối và luôn kiểm tra hạn sử dụng."
        ),
        formulas=[
            G(
                "4 nhóm chất dinh dưỡng và Nguồn cung cấp chính",
                F("Bốn nhóm chất dinh dưỡng thiết yếu", "$\\text{Dinh dưỡng} = \\{\\text{Carbohydrate (Tinh bột)},\\ \\text{Protein (Đạm)},\\ \\text{Lipid (Béo)},\\ \\text{Vitamin \\& Khoáng chất}\\}$", "Một khẩu phần ăn khoa học cần phối hợp cân đối cả 4 nhóm chất cùng với nước và chất xơ."),
                F("Nguồn thực phẩm tiêu biểu cho từng nhóm", "$\\text{Gạo, ngô, khoai} \\to \\text{Tinh bột}; \\quad \\text{Thịt, cá, trứng, sữa, đậu} \\to \\text{Đạm}; \\quad \\text{Dầu, mỡ, lạc, vừng} \\to \\text{Béo}; \\quad \\text{Rau quả} \\to \\text{Vitamin}$", "Không ăn thực phẩm đã hết hạn, bị mốc, ôi thiu hoặc khoai tây đã mọc mầm."),
            )
        ],
        example="Một bữa cơm trưa của học sinh gồm có: cơm trắng, cá kho, thịt gà luộc, canh rau cải nấu tôm và tráng miệng bằng quả cam. Hãy phân loại các món ăn trên theo nhóm chất dinh dưỡng chính mà chúng cung cấp cho cơ thể.",
        example_answer="- **Cơm trắng** (từ gạo): cung cấp chủ yếu **Carbohydrate (tinh bột)**.\n- **Cá kho, thịt gà, tôm**: cung cấp chủ yếu **Protein (chất đạm)** và một phần **Lipid (chất béo)**.\n- **Rau cải và quả cam**: cung cấp chủ yếu **Vitamin (như vitamin C), chất khoáng và chất xơ**.",
        real_life="Sau khi thu hoạch lúa, ngô, lạc, người nông dân luôn phải phơi hoặc sấy thật khô trước khi đưa vào kho bảo quản để làm giảm độ ẩm, ngăn không cho nấm mốc và mọt phát triển.",
        quiz=[
            mcq("biet", "Thành phần chất dinh dưỡng chính có hàm lượng cao nhất trong các loại **lương thực** (như gạo, ngô, khoai, sắn, lúa mì) là gì?", ["Tinh bột (Carbohydrate)", "Vitamin C", "Muối ăn", "Nước tinh khiết"], 0, "Các loại lương thực như gạo, ngô, khoai, sắn chứa hàm lượng lớn tinh bột (carbohydrate), cung cấp năng lượng chính cho cơ thể."),
            mcq("biet", "Nhóm thực phẩm nào sau đây là nguồn cung cấp dồi dào **chất đạm (Protein)** giúp xây dựng tế bào và phát triển cơ bắp?", ["Thịt, cá, trứng, sữa, tôm và đậu nành", "Gạo tẻ, khoai lang và sắn", "Dầu ăn và mỡ lợn", "Nước lọc đóng chai"], 0, "Thịt, cá, trứng, sữa, hải sản và các hạt họ đậu chứa rất nhiều protein (chất đạm)."),
            mcq("hieu", "Vì sao chúng ta tuyệt đối **không** được ăn các hạt lạc (đậu phộng), ngô đã bị mốc xanh hoặc củ khoai tây đã mọc mầm dù đã rửa sạch bên ngoài?", ["Vì nấm mốc trên lạc, ngô và mầm khoai tây đã sinh ra các chất độc hóa học bền nhiệt, có thể gây ngộ độc cấp tính và ung thư gan", "Vì lạc mốc và khoai tây mọc mầm quá cứng không nhai được", "Vì chúng làm giảm khối lượng của nồi nấu", "Vì chúng không còn chứa nước"], 0, "Lạc, ngô mốc chứa độc tố aflatoxin và khoai tây mọc mầm chứa độc tố solanine không bị phân hủy hết khi nấu thông thường."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về lương thực – thực phẩm:", [
                "Rau xanh và hoa quả tươi là nguồn cung cấp chính các loại vitamin, chất khoáng và chất xơ cho cơ thể.",
                "Lương thực, thực phẩm để lâu ngoài không khí nóng ẩm bị ôi thiu là một sự biến đổi hóa học do vi sinh vật phân hủy tạo chất mới có mùi khó chịu.",
                "Để cơ thể khỏe mạnh, học sinh chỉ cần ăn thật nhiều thịt và mỡ mà không cần ăn rau xanh hay trái cây.",
                "Bảo quản thực phẩm tươi sống trong ngăn mát hoặc ngăn đá tủ lạnh giúp làm chậm sự phát triển của vi khuẩn gây ôi thiu.",
            ], [True, True, False, True], "Ý c) sai vì khẩu phần ăn thiếu rau xanh và trái cây sẽ dẫn đến thiếu hụt vitamin, khoáng chất và chất xơ, gây rối loạn tiêu hóa và giảm sức đề kháng."),
            short("vandung", "Khẩu phần dinh dưỡng cân đối hằng ngày của con người cần đầy đủ mấy nhóm chất dinh dưỡng chính (Chất bột đường, Chất đạm, Chất béo, Vitamin và chất khoáng)?", ["4"], "Cơ thể cần đủ $4$ nhóm chất dinh dưỡng chính: carbohydrate (bột đường), protein (đạm), lipid (béo), vitamin và chất khoáng."),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 9: Chất tinh khiết và hỗn hợp",
        icon="🧪",
        description="Phân biệt chất tinh khiết (tạo từ 1 chất duy nhất, có tính chất xác định) và hỗn hợp (tạo từ 2 chất trở lên trộn lẫn), hỗn hợp đồng nhất và không đồng nhất.",
        requirements=[
            "Phân biệt được chất tinh khiết (chỉ gồm một chất duy nhất, có nhiệt độ nóng chảy, nhiệt độ sôi và khối lượng riêng xác định) và hỗn hợp (gồm hai hay nhiều chất trộn lẫn vào nhau).",
            "Nêu được tính chất của hỗn hợp thay đổi phụ thuộc vào thành phần các chất trong hỗn hợp.",
            "Phân biệt được hỗn hợp đồng nhất (thành phần giống nhau ở mọi vị trí như nước đường, nước muối lọc trong) và hỗn hợp không đồng nhất (như nước lẫn cát, nước lẫn dầu ăn).",
        ],
        definition="Chất tinh khiết (chất nguyên chất) được tạo ra từ một chất duy nhất và có các tính chất vật lí, hóa học hoàn toàn xác định. Hỗn hợp được tạo ra khi hai hay nhiều chất trộn lẫn vào nhau (mỗi chất trong hỗn hợp vẫn giữ nguyên tính chất ban đầu của nó).",
        theory=(
            "### 1. Chất tinh khiết và Hỗn hợp\n"
            "- **Chất tinh khiết**: chỉ chứa một chất duy nhất, không lẫn chất khác. Ví dụ: **nước cất** (chỉ gồm $\\text{H}_2\\text{O}$), khí oxygen tinh khiết, muối ăn tinh khiết ($\\text{NaCl}$), đường tinh luyện.\n"
            "  - Chất tinh khiết có các hằng số vật lí **xác định không đổi**: ở $1\\text{ atm}$, nước cất nóng chảy đúng ở $0^\\circ\\text{C}$, sôi đúng ở $100^\\circ\\text{C}$ và có khối lượng riêng $D = 1\\text{ g/cm}^3$ ở $4^\\circ\\text{C}$.\n"
            "- **Hỗn hợp**: gồm từ $2$ chất trở lên trộn lẫn với nhau. Ví dụ: không khí, nước tự nhiên (nước sông, nước biển, nước khoáng), sữa, nước cam, bột canh (gồm muối ăn, bột ngọt, tiêu, ớt).\n"
            "  - Tính chất của hỗn hợp (độ mặn/ngọt, khối lượng riêng, nhiệt độ sôi) **thay đổi tùy thuộc vào tỉ lệ các chất thành phần**.\n\n"
            "### 2. Hỗn hợp đồng nhất và Hỗn hợp không đồng nhất\n"
            "- **Hỗn hợp đồng nhất**: hỗn hợp có thành phần giống nhau tại mọi vị trí trong toàn bộ hỗn hợp (ví dụ: nước đường, nước muối trong suốt, không khí sạch, hợp kim đồng thau).\n"
            "- **Hỗn hợp không đồng nhất**: hỗn hợp có thành phần không giống nhau trong toàn bộ hỗn hợp, có sự phân lớp hoặc hạt lơ lửng (ví dụ: cát lẫn trong nước, dầu ăn trong nước, sữa đặc pha nước)."
        ),
        formulas=[
            G(
                "Phân biệt Chất tinh khiết và Hỗn hợp",
                F("Tiêu chuẩn nhận biết Chất tinh khiết và Hỗn hợp", "$\\text{Chất tinh khiết (1 chất)}: t_{\\text{nc}},\\ t_{\\text{sôi}},\\ D = \\text{hằng số xác định}; \\qquad \\text{Hỗn hợp (}\\ge 2\\text{ chất)}: \\text{Tính chất phụ thuộc thành phần}$", "Nước cất dùng pha thuốc tiêm trong y tế là chất tinh khiết; còn nước khoáng, nước biển, nước máy là hỗn hợp."),
                F("Phân loại Hỗn hợp theo sự phân bố", "$\\text{Hỗn hợp} = \\begin{cases} \\text{Đồng nhất (mọi điểm như nhau: dung dịch nước muối, nước đường)} \\\\ \\text{Không đồng nhất (phân lớp/vẩn đục: dầu ăn + nước, bột mì + nước)} \\end{cases}$", "Khi trộn các chất thành hỗn hợp (không phản ứng hóa học), khối lượng hỗn hợp bằng tổng khối lượng các chất thành phần."),
            )
        ],
        example="Có hai cốc chất lỏng trong suốt không màu: một cốc đựng nước cất và một cốc đựng nước muối loãng. Nếu đun sôi cả hai cốc ở áp suất chuẩn $1\\text{ atm}$ và dùng nhiệt kế đo nhiệt độ lúc đang sôi, hoặc lấy vài giọt mỗi cốc đem cô cạn trên mặt kính đồng hồ thì ta phân biệt hai cốc như thế nào?",
        example_answer="- **Cách 1 (Đo nhiệt độ sôi)**: Cốc sôi ở đúng $100^\\circ\\text{C}$ và giữ nguyên nhiệt độ trong suốt khi sôi là **nước cất** (chất tinh khiết); cốc sôi ở nhiệt độ cao hơn $100^\\circ\\text{C}$ (và nhiệt độ tăng dần khi nước bay hơi bớt) là **nước muối** (hỗn hợp).\n- **Cách 2 (Cô cạn)**: Giọt bay hơi hết không để lại vết gì trên mặt kính là **nước cất**; giọt để lại các hạt tinh thể màu trắng là **nước muối**.",
        real_life="Trong y học, bác sĩ bắt buộc phải dùng **nước cất** (chất tinh khiết) để pha thuốc tiêm tĩnh mạch, còn **nước muối sinh lí** ($0{,}9\\%\\text{ NaCl}$ trong nước cất) là một hỗn hợp đồng nhất dùng để rửa vết thương và nhỏ mắt.",
        quiz=[
            mcq("biet", "Trong các vật phẩm sau đây, đâu là một **chất tinh khiết**?", ["Nước cất dùng trong y tế và phòng thí nghiệm", "Nước khoáng đóng chai", "Nước biển", "Không khí tự nhiên"], 0, "Nước cất chỉ gồm một chất duy nhất là $\\text{H}_2\\text{O}$ nên là chất tinh khiết; còn nước khoáng, nước biển và không khí chứa nhiều chất hòa tan nên là hỗn hợp."),
            mcq("biet", "Hỗn hợp nào sau đây là **hỗn hợp đồng nhất**?", ["Nước đường đã khuấy tan hoàn toàn trong suốt", "Nước trộn lẫn với dầu ăn", "Nước sông phù sa đang đục ngầu", "Hỗn hợp bột sắt trộn với cát vàng"], 0, "Đường tan hoàn toàn trong nước tạo ra dung dịch trong suốt có thành phần giống nhau ở mọi vị trí nên là hỗn hợp đồng nhất."),
            mcq("hieu", "Vì sao dựa vào việc đo nhiệt độ nóng chảy hoặc nhiệt độ sôi, các nhà hóa học có thể kiểm tra xem một chất rắn hoặc chất lỏng có tinh khiết hay có lẫn tạp chất?", ["Vì chất tinh khiết luôn có nhiệt độ nóng chảy và nhiệt độ sôi xác định không đổi, còn hỗn hợp (lẫn tạp chất) có nhiệt độ nóng chảy và nhiệt độ sôi thay đổi theo thành phần", "Vì mọi hỗn hợp đều không thể sôi được", "Vì chất tinh khiết luôn sôi ở $0^\\circ\\text{C}$", "Vì tạp chất làm chất mất hết khối lượng"], 0, "Mỗi chất tinh khiết có $t_{\\text{nc}}$ và $t_{\\text{sôi}}$ cố định đặc trưng, khi lẫn tạp chất (trở thành hỗn hợp) các nhiệt độ này sẽ bị lệch đi."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về chất tinh khiết và hỗn hợp:", [
                "Chất tinh khiết chỉ được tạo nên từ một chất duy nhất, còn hỗn hợp gồm từ hai chất trở lên trộn lẫn vào nhau.",
                "Gói bột canh gia vị (gồm muối ăn, bột ngọt, hạt tiêu, bột ớt) là một hỗn hợp.",
                "Nước khoáng thiên nhiên đóng chai là chất tinh khiết vì nhìn bằng mắt thường thấy trong suốt.",
                "Hỗn hợp dầu ăn và nước khi để yên tách thành hai lớp riêng biệt là một hỗn hợp không đồng nhất.",
            ], [True, True, False, True], "Ý c) sai vì nước khoáng chứa nước cùng nhiều khoáng chất hòa tan ($\\text{Ca}^{2+}, \\text{Mg}^{2+}, \\text{Na}^+, \\text{HCO}_3^-$) nên là một hỗn hợp đồng nhất chứ không phải chất tinh khiết."),
            short("vandung", "Cho 5 mẫu sau: (1) Nước cất, (2) Nước cam vắt, (3) Không khí, (4) Khí oxygen tinh khiết $100\\%$, (5) Nước biển. Có bao nhiêu mẫu trong danh sách trên là **hỗn hợp**?", ["3"], "Các mẫu (2) Nước cam, (3) Không khí và (5) Nước biển gồm nhiều chất trộn lẫn nên có $3$ mẫu là hỗn hợp; còn (1) và (4) là chất tinh khiết."),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 10: Dung dịch, huyền phù và nhũ tương",
        icon="🥤",
        description="Khái niệm chất tan – dung môi – dung dịch, các yếu tố làm chất rắn tan nhanh hơn và phân biệt dung dịch, huyền phù, nhũ tương.",
        requirements=[
            "Nêu được dung dịch là hỗn hợp đồng nhất của chất tan và dung môi; xác định được chất tan và dung môi trong các dung dịch quen thuộc ($m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}}$).",
            "Trình bày được 3 biện pháp làm cho chất rắn tan nhanh hơn trong nước: khuấy đều, đun nóng dung dịch và nghiền nhỏ chất rắn.",
            "Phân biệt được dung dịch (hỗn hợp đồng nhất trong suốt), huyền phù (các hạt chất rắn nhỏ lơ lửng trong chất lỏng) và nhũ tương (các giọt chất lỏng nhỏ lơ lửng trong một chất lỏng khác không hòa tan).",
        ],
        definition="Dung dịch là hỗn hợp đồng nhất của dung môi và chất tan. Huyền phù là hỗn hợp không đồng nhất gồm các hạt chất rắn nhỏ lơ lửng trong môi trường chất lỏng. Nhũ tương là hỗn hợp không đồng nhất gồm một hay nhiều chất lỏng phân tán dưới dạng các giọt nhỏ lơ lửng trong một chất lỏng khác.",
        theory=(
            "### 1. Chất tan, Dung môi và Dung dịch\n"
            "- **Dung môi**: chất có khả năng hòa tan chất khác để tạo thành dung dịch (thường là chất lỏng chiếm lượng lớn, phổ biến nhất là **nước**; ngoài ra có cồn, xăng, acetone).\n"
            "- **Chất tan**: chất bị hòa tan trong dung môi (có thể ở thể rắn như đường, muối; thể lỏng như cồn, giấm; hoặc thể khí như khí $\\text{CO}_2$ trong nước ngọt có gas, khí $\\text{O}_2$ trong nước).\n"
            "- **Dung dịch**: hỗn hợp **đồng nhất** của chất tan và dung môi ($m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}}$). Dung dịch để yên không bị lắng cặn hay phân lớp.\n"
            "- **Ba cách làm chất rắn tan nhanh hơn trong nước**: (1) **Khuấy** dung dịch; (2) **Đun nóng** nước; (3) **Nghiền nhỏ** chất rắn (tăng diện tích tiếp xúc).\n\n"
            "### 2. Phân biệt Dung dịch – Huyền phù – Nhũ tương\n"
            "- **Huyền phù (Rắn lơ lửng trong Lỏng)**: nước phù sa sông Hồng, nước bột sắn dây chưa nấu, nước vôi sữa. Nếu để yên một thời gian, các hạt rắn nặng hơn sẽ **lắng xuống đáy**.\n"
            "- **Nhũ tương (Giọt Lỏng lơ lửng trong Lỏng)**: hỗn hợp dầu ăn và nước được lắc mạnh, sữa tươi, sốt mayonnaise (lòng đỏ trứng gà đánh với dầu ăn và giấm)."
        ),
        formulas=[
            G(
                "Cấu tạo Dung dịch và Phân biệt Dung dịch – Huyền phù – Nhũ tương",
                F("Khối lượng dung dịch", "$m_{\\text{dd}} = m_{\\text{chất tan}} + m_{\\text{dung môi}}$", "Lưu ý: Khi chất rắn chưa tan hết lắng ở đáy cốc, phần rắn không tan đó không được tính vào $m_{\\text{chất tan}}$ của dung dịch!"),
                F("Bảng phân biệt nhanh 3 hệ phân tán trong chất lỏng", "$\\text{Dung dịch}: \\text{Chất tan} + \\text{Dung môi (Đồng nhất)}; \\quad \\text{Huyền phù}: \\text{Hạt Rắn lơ lửng}; \\quad \\text{Nhũ tương}: \\text{Giọt Lỏng lơ lửng}$", "Huyền phù và nhũ tương đều là các hỗn hợp **không đồng nhất**."),
            )
        ],
        example="Hòa tan hoàn toàn $15\\text{ g}$ đường kính trắng vào một cốc chứa $185\\text{ g}$ nước ấm. Hãy chỉ ra đâu là chất tan, đâu là dung môi và tính khối lượng dung dịch nước đường thu được.",
        example_answer="Trong quá trình trên: **đường kính** là **chất tan** ($m_{\\text{ct}} = 15\\text{ g}$), **nước** là **dung môi** ($m_{\\text{dm}} = 185\\text{ g}$), và nước đường thu được là **dung dịch**. Khối lượng dung dịch nước đường là $m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}} = 15 + 185 = 200\\text{ g}$.",
        real_life="Trên vỏ các chai thuốc ho thảo dược dạng hỗn dịch (huyền phù) hoặc kem dưỡng da, sữa tắm (nhũ tương) luôn có dòng chữ hướng dẫn 'Lắc đều trước khi dùng' để các hạt hoạt chất phân bố đồng đều trở lại.",
        quiz=[
            mcq("biet", "Hỗn hợp không đồng nhất gồm các **hạt chất rắn nhỏ** lơ lửng trong môi trường chất lỏng (như nước phù sa, nước bột sắn dây sống) được gọi là gì?", ["Huyền phù", "Nhũ tương", "Dung dịch", "Chất tinh khiết"], 0, "Các hạt chất rắn nhỏ lơ lửng trong chất lỏng tạo thành huyền phù."),
            mcq("biet", "Hỗn hợp không đồng nhất gồm các **giọt chất lỏng nhỏ** lơ lửng trong một chất lỏng khác không hòa tan vào nhau (như lắc mạnh dầu ăn với nước, sốt mayonnaise) được gọi là gì?", ["Nhũ tương", "Huyền phù", "Dung dịch bão hòa", "Hợp kim"], 0, "Các giọt chất lỏng phân tán lơ lửng trong một chất lỏng khác gọi là nhũ tương."),
            mcq("hieu", "Để hòa tan một viên đường phèn to vào cốc nước nhanh nhất, ta nên kết hợp những thao tác nào sau đây?", ["Đập nhỏ viên đường phèn, cho vào nước nóng và dùng thìa khuấy đều", "Để nguyên cả viên đường phèn to bỏ vào nước đá lạnh và không khuấy", "Bỏ viên đường phèn vào dầu ăn", "Đậy kín nắp cốc nước lạnh"], 0, "Nghiền nhỏ chất rắn, dùng nước nóng và khuấy đều là 3 biện pháp giúp chất rắn tan nhanh nhất trong nước."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dung dịch, huyền phù và nhũ tương:", [
                "Dung dịch là hỗn hợp đồng nhất của chất tan và dung môi.",
                "Chất tan trong dung dịch chỉ có thể là chất rắn, không thể là chất lỏng hay chất khí.",
                "Khi để yên một cốc nước phù sa (huyền phù) một thời gian, các hạt bùn đất rắn sẽ lắng dần xuống đáy cốc.",
                "Vết sơn dầu hoặc vết nhựa cây dính trên tay không rửa sạch được bằng nước nhưng lau sạch dễ dàng bằng xăng hoặc dầu hỏa vì xăng/dầu hỏa là dung môi hòa tan được sơn dầu.",
            ], [True, False, True, True], "Ý b) sai vì chất tan có thể ở cả 3 thể rắn (muối, đường), lỏng (cồn, acid) và khí (khí $\\text{CO}_2$ trong nước giải khát có gas)."),
            short("vandung", "Hòa tan hoàn toàn $25\\text{ g}$ muối ăn ($\\text{NaCl}$) vào $175\\text{ g}$ nước cất thì thu được dung dịch nước muối có khối lượng bằng bao nhiêu gam ($\\text{g}$)?", ["200"], "Áp dụng công thức $m_{\\text{dd}} = m_{\\text{ct}} + m_{\\text{dm}} = 25 + 175 = 200\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 11: Tách chất bằng phương pháp lọc và cô cạn",
        icon="⏳",
        description="Nguyên tắc lựa chọn phương pháp tách chất, phương pháp lắng – gạn – lọc (tách chất rắn không tan khỏi chất lỏng) và phương pháp cô cạn (tách chất rắn không bay hơi tan trong dung dịch).",
        requirements=[
            "Nêu được nguyên tắc tách chất ra khỏi hỗn hợp dựa trên sự khác nhau về tính chất vật lí (tính tan, kích thước hạt, nhiệt độ sôi, khối lượng riêng).",
            "Trình bày được dụng cụ và quy trình tách chất rắn không tan ra khỏi hỗn hợp lỏng (huyền phù) bằng **phương pháp lọc**.",
            "Trình bày được cách tách chất rắn tan (không bay hơi ở nhiệt độ thường như muối ăn) ra khỏi dung dịch bằng **phương pháp cô cạn**.",
        ],
        definition="Phương pháp lọc dùng để tách chất rắn không tan ra khỏi hỗn hợp lỏng (huyền phù) nhờ phễu lọc và giấy lọc. Phương pháp cô cạn dùng để tách chất rắn tan (nhưng không hóa hơi khi đun nóng) ra khỏi dung dịch bằng cách đun cho dung môi bay hơi hết.",
        theory=(
            "### 1. Phương pháp Lắng, Gạn và Lọc (Tách chất rắn không tan khỏi chất lỏng)\n"
            "- **Phương pháp lắng – gạn**: Với các hạt chất rắn nặng không tan (như cát trong nước), để yên cho cát lắng xuống đáy rồi gạn lớp nước phía trên ra.\n"
            "- **Phương pháp lọc**: Dùng để tách các hạt chất rắn lơ lửng không tan ra khỏi chất lỏng (ví dụ: lọc nước lẫn đất cát, lọc bã trà, lọc bã đậu nành làm sữa đậu nành, khẩu trang lọc bụi trong không khí).\n"
            "  - **Dụng cụ lọc trong phòng thí nghiệm**: Phễu thủy tinh, giấy lọc gấp hình phễu, đũa thủy tinh dẫn dòng, bình tam giác (hoặc cốc hứng dịch lọc).\n"
            "  - Chất rắn giữ lại trên giấy lọc gọi là **bã lọc (cặn)**; chất lỏng trong suốt chảy xuống bình hứng gọi là **dịch lọc**.\n\n"
            "### 2. Phương pháp Cô cạn (Tách chất rắn tan khỏi dung dịch)\n"
            "- Với dung dịch (như nước muối ăn $\\text{NaCl}$), các hạt chất tan có kích thước phân tử/ion cực nhỏ đi lọt hoàn toàn qua lỗ giấy lọc nên **không thể dùng phương pháp lọc để tách muối ra khỏi nước muối**!\n"
            "- **Nguyên tắc cô cạn**: Đun nóng dung dịch trên bát sứ; nước (dung môi) có nhiệt độ sôi thấp ($100^\\circ\\text{C}$) sẽ **bay hơi hết**, còn muối ăn ($\\text{NaCl}$) không bay hơi (nhiệt độ nóng chảy rất cao $> 800^\\circ\\text{C}$) sẽ **kết tinh lại dưới đáy bát sứ**."
        ),
        formulas=[
            G(
                "Quy tắc chọn phương pháp Lọc hay Cô cạn",
                F("Khi chất rắn KHÔNG TAN trong chất lỏng (Huyền phù)", "$\\text{Rắn không tan + Lỏng (vd: Cát + Nước)} \\xrightarrow{\\text{Phương pháp LỌC (qua phễu + giấy lọc)}} \\text{Cát (trên giấy lọc)} + \\text{Nước trong}$", "Dựa vào sự khác nhau về kích thước hạt: hạt chất rắn không tan lớn hơn lỗ nhỏ li ti của giấy lọc."),
                F("Khi chất rắn TAN trong chất lỏng (Dung dịch)", "$\\text{Rắn tan không bay hơi + Lỏng (vd: Muối ăn + Nước)} \\xrightarrow{\\text{Phương pháp CÔ CẠN (đun bay hơi)}} \\text{Muối rắn kết tinh} + \\text{Hơi nước}\\uparrow$", "Dựa vào sự khác nhau về khả năng bay hơi (nhiệt độ sôi): dung môi bay hơi hết, chất rắn tan ở lại đáy bát sứ."),
            )
        ],
        example="Một mẫu muối ăn thu hoạch từ ruộng muối bị lẫn một ít cát bẩn không tan. Hãy trình bày quy trình 3 bước sử dụng nước, dụng cụ lọc và bát sứ cô cạn để thu được muối ăn sạch.",
        example_answer="- **Bước 1 (Hòa tan)**: Cho hỗn hợp muối lẫn cát vào cốc nước và khuấy kỹ; muối ăn tan hết vào nước tạo thành dung dịch, còn cát không tan.\n- **Bước 2 (Lọc)**: Đổ hỗn hợp qua phễu có lót giấy lọc; **cát không tan bị giữ lại trên giấy lọc**, còn dung dịch nước muối trong suốt chảy xuống cốc hứng.\n- **Bước 3 (Cô cạn)**: Đổ dịch lọc nước muối vào bát sứ rồi đun nóng cho nước bay hơi hết, thu được **muối ăn tinh khiết kết tinh trắng** ở đáy bát sứ.",
        real_life="Bình lọc nước gia đình, phin pha cà phê, rây lọc bột và khẩu trang y tế lọc khói bụi đều ứng dụng nguyên tắc của phương pháp lọc; còn nghề làm muối biển và nấu đường mật mía ứng dụng phương pháp cô cạn.",
        quiz=[
            mcq("biet", "Để tách các hạt cát không tan ra khỏi hỗn hợp nước lẫn cát, ta sử dụng phương pháp nào sau đây?", ["Phương pháp lọc (hoặc lắng – gạn – lọc)", "Phương pháp cô cạn toàn bộ", "Dùng nam châm hút cát", "Đun cho cát bay hơi"], 0, "Cát là chất rắn không tan trong nước nên tách ra khỏi nước bằng phương pháp lọc qua giấy lọc."),
            mcq("biet", "Để tách lấy muối ăn ($\\text{NaCl}$) rắn ra khỏi dung dịch nước muối trong suốt, ta phải dùng phương pháp nào?", ["Phương pháp cô cạn (đun nóng cho nước bay hơi hết, muối kết tinh lại)", "Phương pháp lọc qua giấy lọc", "Phương pháp dùng phễu chiết", "Phương pháp lắng gạn"], 0, "Muối ăn đã tan thành dung dịch đồng nhất sẽ đi qua giấy lọc, nên phải dùng phương pháp cô cạn để nước bay hơi hết và thu lại muối rắn."),
            mcq("hieu", "Vì sao **không** thể dùng giấy lọc để tách riêng đường ăn ra khỏi một cốc dung dịch nước đường đã hòa tan hoàn toàn?", ["Vì các phân tử đường đã hòa tan có kích thước vô cùng nhỏ, chui lọt hoàn toàn qua các lỗ nhỏ của giấy lọc cùng với nước", "Vì đường ăn làm cháy thủng giấy lọc", "Vì nước bị giữ lại trên giấy lọc còn đường chảy xuống", "Vì dung dịch nước đường là chất rắn"], 0, "Giấy lọc chỉ giữ lại được các hạt chất rắn không tan (huyền phù), còn chất tan trong dung dịch đi xuyên qua giấy lọc dễ dàng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phương pháp lọc và cô cạn:", [
                "Phương pháp lọc dùng để tách chất rắn không tan ra khỏi hỗn hợp lỏng.",
                "Phương pháp cô cạn dựa trên sự khác nhau về khả năng bay hơi của dung môi và chất tan không bay hơi.",
                "Khi cô cạn dung dịch nước muối trên ngọn lửa đèn cồn, muối ăn bay hơi đi mất còn nước ở lại đáy bát sứ.",
                "Để tinh chế muối ăn có lẫn cát, ta tiến hành theo thứ tự: Hòa tan vào nước $\\to$ Lọc bỏ cát $\\to$ Cô cạn dịch lọc.",
            ], [True, True, False, True], "Ý c) sai vì khi cô cạn, nước là chất dễ bay hơi sẽ hóa hơi bay đi, còn muối ăn không bay hơi kết tinh lại ở đáy bát sứ."),
            short("vandung", "Để làm sạch một mẫu muối ăn bị lẫn cát bẩn không tan, ta cần thực hiện quy trình gồm mấy bước cơ bản theo thứ tự: (1) Hòa tan vào nước, (2) Lọc bỏ cát, (3) Cô cạn dung dịch nước muối?", ["3"], "Quy trình tinh chế muối lẫn cát gồm $3$ bước cơ bản: Hòa tan $\\to$ Lọc $\\to$ Cô cạn."),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 12: Tách chất bằng phương pháp chiết",
        icon="⚗️",
        description="Nguyên tắc và dụng cụ của phương pháp chiết (phễu chiết) để tách hai chất lỏng không hòa tan vào nhau và phân lớp theo khối lượng riêng.",
        requirements=[
            "Nêu được phương pháp chiết dùng để tách các chất lỏng không hòa tan vào nhau (hỗn hợp chất lỏng không đồng nhất bị phân thành hai lớp riêng biệt).",
            "Giải thích được trong phễu chiết, chất lỏng nào có khối lượng riêng nhỏ hơn (nhẹ hơn, như dầu ăn, xăng) sẽ nổi ở lớp trên; chất lỏng nào có khối lượng riêng lớn hơn (nặng hơn, như nước) sẽ nằm ở lớp dưới.",
            "Trình bày được các bước sử dụng phễu chiết để tách riêng hỗn hợp dầu ăn và nước.",
        ],
        definition="Phương pháp chiết là phương pháp dùng để tách các chất lỏng không hòa tan vào nhau (tạo thành hỗn hợp lỏng không đồng nhất phân lớp) ra khỏi nhau bằng dụng cụ chuyên dụng gọi là phễu chiết.",
        theory=(
            "### 1. Nguyên tắc của phương pháp chiết\n"
            "- Khi trộn hai chất lỏng **không tan vào nhau** và có **khối lượng riêng khác nhau** (ví dụ: dầu ăn với nước, xăng với nước, tinh dầu sả/tràm với nước), sau khi để yên hỗn hợp sẽ tự tách thành **hai lớp chất lỏng riêng biệt**:\n"
            "  - **Lớp phía trên**: là chất lỏng có khối lượng riêng **nhỏ hơn** (nhẹ hơn, ví dụ dầu ăn có $D \\approx 0{,}8\\text{ g/cm}^3$).\n"
            "  - **Lớp phía dưới**: là chất lỏng có khối lượng riêng **lớn hơn** (nặng hơn, ví dụ nước có $D = 1{,}0\\text{ g/cm}^3$).\n\n"
            "### 2. Dụng cụ và Các bước tách bằng phễu chiết\n"
            "- **Dụng cụ chính**: **Phễu chiết** (bầu thủy tinh có nắp ở trên và có **khóa vòi** đóng/mở ở cuống phễu phía dưới), giá đỡ sắt và hai cốc hứng.\n"
            "- **Các bước thực hiện tách dầu ăn và nước**:\n"
            "  1. Kiểm tra khóa phễu chiết đã đóng chặt, rót hỗn hợp dầu ăn và nước vào phễu chiết.\n"
            "  2. Để yên trên giá đỡ cho đến khi hỗn hợp phân tách rõ rệt thành 2 lớp (nước ở dưới, dầu ăn ở trên) và **mở nắp trên của phễu chiết** (để áp suất khí quyển đẩy chất lỏng chảy xuống).\n"
            "  3. Mở từ từ khóa phễu chiết cho lớp nước ở phía dưới chảy xuống cốc hứng thứ nhất; ngay khi mặt phân cách giữa dầu và nước chạm tới khóa thì **đóng khóa phễu chiết lại**."
        ),
        formulas=[
            G(
                "Nguyên tắc phân lớp trong Phễu chiết và Tổng kết các phương pháp tách chất",
                F("Quy tắc phân lớp hai chất lỏng không tan vào nhau", "$D_1 < D_2 \\implies \\begin{cases} \\text{Chất lỏng 1 (nhẹ hơn, vd: Dầu ăn, Xăng, Tinh dầu) nổi ở LỚP TRÊN} \\\\ \\text{Chất lỏng 2 (nặng hơn, vd: Nước) nằm ở LỚP DƯỚI (chảy ra trước khi mở khóa)} \\end{cases}$", "Phương pháp chiết chỉ dùng cho hai chất lỏng **không hòa tan vào nhau** (không dùng được cho cồn + nước vì cồn tan vô hạn trong nước!)."),
                F("Bảng tổng kết lựa chọn 3 phương pháp tách chất Lớp 6", "$\\text{Rắn không tan + Lỏng} \\to \\text{LỌC}; \\quad \\text{Rắn tan không bay hơi + Lỏng} \\to \\text{CÔ CẠN}; \\quad \\text{2 Lỏng không tan vào nhau} \\to \\text{CHIẾT}$", "Ngoài ra bột sắt ($\\text{Fe}$) trộn lẫn bột lưu huỳnh hoặc cát có thể tách nhanh bằng **nam châm**."),
            )
        ],
        example="Trong quá trình chưng cất tinh dầu sả (hoặc tinh dầu tràm, tinh dầu bưởi) bằng hơi nước, hỗn hợp ngưng tụ thu được gồm nước và tinh dầu sả không tan vào nhau. Biết khối lượng riêng của tinh dầu sả là $D_1 = 0{,}89\\text{ g/cm}^3$ và của nước là $D_2 = 1{,}00\\text{ g/cm}^3$. Khi cho hỗn hợp này vào phễu chiết và để yên, lớp nào nằm ở trên, lớp nào nằm ở dưới và chất nào chảy ra khỏi vòi phễu chiết trước?",
        example_answer="Vì $D_{\\text{tinh dầu}} = 0{,}89\\text{ g/cm}^3 < D_{\\text{nước}} = 1{,}00\\text{ g/cm}^3$ nên **tinh dầu sả nhẹ hơn nổi ở lớp phía trên**, còn **nước nặng hơn nằm ở lớp phía dưới**. Khi mở khóa vòi ở đáy phễu chiết, **lớp nước ở phía dưới sẽ chảy ra trước**.",
        real_life="Trong sản xuất tinh dầu thiên nhiên (tinh dầu tràm, sả, quế, bạc hà), người ta luôn dùng bình chiết/phễu chiết để tách lớp tinh dầu nguyên chất nổi ở phía trên ra khỏi lớp nước chưng cất ở phía dưới.",
        quiz=[
            mcq("biet", "Dụng cụ chuyên dụng trong phòng thí nghiệm dùng để tách hai chất lỏng không hòa tan vào nhau (như dầu ăn và nước) bằng phương pháp chiết là gì?", ["Phễu chiết (có khóa vòi ở cuống phễu)", "Phễu lọc thường lót giấy lọc", "Bát sứ nung", "Nhiệt kế thủy ngân"], 0, "Phễu chiết có khóa vòi ở dưới đáy giúp xả riêng lớp chất lỏng phía dưới và giữ lại lớp chất lỏng phía trên."),
            mcq("biet", "Hỗn hợp nào sau đây có thể tách riêng các chất thành phần bằng **phương pháp chiết** với phễu chiết?", ["Hỗn hợp dầu ăn và nước (hoặc xăng và nước)", "Dung dịch nước muối ăn trong suốt", "Dung dịch cồn y tế (ethanol hòa tan hoàn toàn trong nước)", "Hỗn hợp cát và sỏi"], 0, "Dầu ăn (hoặc xăng) và nước là hai chất lỏng không hòa tan vào nhau và tách thành hai lớp riêng biệt nên tách được bằng phương pháp chiết."),
            mcq("hieu", "Khi cho hỗn hợp gồm dầu hỏa ($D_1 = 0{,}8\\text{ g/cm}^3$) và nước ($D_2 = 1{,}0\\text{ g/cm}^3$) vào phễu chiết rồi để yên cho phân lớp, khi mở khóa ở đáy phễu chiết thì chất lỏng nào sẽ chảy ra khỏi vòi trước?", ["Nước chảy ra trước vì nước có khối lượng riêng lớn hơn dầu hỏa nên nằm ở lớp phía dưới sát khóa phễu", "Dầu hỏa chảy ra trước vì dầu hỏa nhẹ hơn", "Cả hai chất chảy ra trộn lẫn cùng lúc", "Không chất nào chảy ra được"], 0, "Chất lỏng nặng hơn ($D_{\\text{nước}} = 1{,}0 > D_{\\text{dầu}} = 0{,}8$) nằm ở lớp dưới cùng sát khóa phễu chiết nên chảy ra trước."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phương pháp chiết và tách chất:", [
                "Phương pháp chiết dùng để tách hai chất lỏng không hòa tan vào nhau và phân thành hai lớp.",
                "Khi mở khóa phễu chiết để xả chất lỏng lớp dưới, cần mở nắp ở miệng trên của phễu chiết để không khí đi vào giúp chất lỏng chảy đều.",
                "Có thể dùng phễu chiết để tách riêng rượu etylic (ethanol) ra khỏi nước trong rượu uống.",
                "Khi trộn bột sắt với bột lưu huỳnh, ta có thể dùng nam châm để hút tách riêng bột sắt ra khỏi hỗn hợp.",
            ], [True, True, False, True], "Ý c) sai vì rượu etylic (ethanol) và nước tan vô hạn vào nhau thành một dung dịch đồng nhất (không phân lớp) nên không thể tách bằng phễu chiết (mà phải dùng phương pháp chưng cất dựa vào nhiệt độ sôi khác nhau)."),
            short("vandung", "Cho 4 hỗn hợp lỏng sau: (1) Dầu ăn và nước; (2) Xăng và nước; (3) Nước đường trong suốt; (4) Tinh dầu sả và nước. Có bao nhiêu hỗn hợp trong danh sách trên phân thành 2 lớp và tách được bằng **phễu chiết**?", ["3"], "Các hỗn hợp (1) Dầu ăn + nước, (2) Xăng + nước và (4) Tinh dầu sả + nước là $3$ hỗn hợp gồm hai chất lỏng không tan vào nhau nên tách được bằng phễu chiết; còn (3) nước đường là dung dịch đồng nhất."),
        ],
    ),
]


from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("chemistry", 6, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
