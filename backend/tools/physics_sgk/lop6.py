"""Vật lý Lớp 6 (KHTN 6 - Kết nối tri thức với cuộc sống): 3 Chương - 14 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 6

CH1_TOPIC = "l6-ch01-cac-phep-do"
CH1_TITLE = "Chương I: Mở đầu và các phép đo Vật lý"
CH1_DESC = "Chương I · Vật lý 6 (KHTN 6): Các phép đo độ dài, khối lượng, thời gian và nhiệt độ."

CH2_TOPIC = "l6-ch02-luc-trong-doi-song"
CH2_TITLE = "Chương II: Lực trong đời sống"
CH2_DESC = "Chương II · Vật lý 6 (KHTN 6): Khái niệm lực, biểu diễn lực, biến dạng lò xo, trọng lực và lực ma sát."

CH3_TOPIC = "l6-ch03-nang-luong-va-bau-troi"
CH3_TITLE = "Chương III: Năng lượng và Trái Đất – Bầu trời"
CH3_DESC = "Chương III · Vật lý 6 (KHTN 6): Các dạng năng lượng, bảo toàn năng lượng, Hệ Mặt Trời và Ngân Hà."

LESSONS = [
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 1: Đo chiều dài",
        icon="📏",
        description="Đơn vị đo độ dài trong hệ SI, giới hạn đo (GHĐ), độ chia nhỏ nhất (ĐCNN) và quy tắc 5 bước đo chiều dài.",
        requirements=[
            "Nêu được đơn vị đo độ dài hợp pháp trong hệ SI là mét ($\\text{m}$) và quy đổi được giữa các đơn vị $\\text{km}, \\text{m}, \\text{dm}, \\text{cm}, \\text{mm}$.",
            "Xác định được giới hạn đo (GHĐ) và độ chia nhỏ nhất (ĐCNN) của thước đo chiều dài.",
            "Thực hiện đúng 5 bước đo chiều dài bằng thước và đọc kết quả đo theo vạch chia gần nhất.",
        ],
        definition="Đo chiều dài của một vật là so sánh chiều dài của vật đó với một độ dài được chọn làm đơn vị. Đơn vị đo độ dài chính thức trong hệ SI là mét (kí hiệu $\\text{m}$).",
        theory=(
            "### 1. Đơn vị và dụng cụ đo chiều dài\n"
            "- Đơn vị đo chiều dài trong hệ SI là **mét** ($\\text{m}$). Các đơn vị thường dùng khác: $\\text{km}, \\text{dm}, \\text{cm}, \\text{mm}$.\n"
            "- Quy đổi: $1\\text{ km} = 1000\\text{ m}$; $1\\text{ m} = 10\\text{ dm} = 100\\text{ cm} = 1000\\text{ mm}$.\n"
            "- **Giới hạn đo (GHĐ)** của thước là chiều dài lớn nhất ghi trên thước.\n"
            "- **Độ chia nhỏ nhất (ĐCNN)** của thước là chiều dài giữa hai vạch chia liên tiếp trên thước.\n\n"
            "### 2. Quy tắc 5 bước đo chiều dài\n"
            "1. Ước lượng chiều dài cần đo.\n"
            "2. Chọn thước có GHĐ và ĐCNN phù hợp.\n"
            "3. Đặt thước dọc theo chiều dài cần đo, vạch số $0$ ngang với một đầu của vật.\n"
            "4. Đặt mắt nhìn theo hướng vuông góc với cạnh thước tại đầu kia của vật.\n"
            "5. Đọc và ghi kết quả đo theo vạch chia gần nhất với đầu kia của vật."
        ),
        formulas=[
            G(
                "Đơn vị độ dài và Độ chia nhỏ nhất",
                F("Quy đổi đơn vị độ dài", "$1\\text{ m} = 10\\text{ dm} = 100\\text{ cm} = 1000\\text{ mm}$", "Nhân hoặc chia cho $10$ khi chuyển giữa hai đơn vị liền kề."),
                F("Công thức tính ĐCNN của thước", "$\\text{ĐCNN} = \\dfrac{L_2 - L_1}{n}$", "Trong đó $L_2 - L_1$ là hiệu hai số ghi lớn và nhỏ, $n$ là số khoảng chia giữa chúng."),
            )
        ],
        example="Trên một chiếc thước kẻ học sinh, từ vạch số $0\\text{ cm}$ đến vạch số $1\\text{ cm}$ được chia thành $10$ khoảng đều nhau. Chiều dài lớn nhất ghi trên thước là $20\\text{ cm}$. Hãy xác định GHĐ và ĐCNN của thước này theo đơn vị $\\text{mm}$.",
        example_answer="Giới hạn đo của thước là $\\text{GHĐ} = 20\\text{ cm} = 200\\text{ mm}$. Độ chia nhỏ nhất của thước là $\\text{ĐCNN} = \\dfrac{1 - 0}{10} = 0{,}1\\text{ cm} = 1\\text{ mm}$.",
        real_life="Thợ may dùng thước dây mềm để đo số đo cơ thể, thợ mộc dùng thước cuộn kim loại để đo kích thước bàn ghế, học sinh dùng thước kẻ nhựa có $\\text{ĐCNN} = 1\\text{ mm}$ để vẽ hình.",
        quiz=[
            mcq("biet", "Đơn vị đo chiều dài hợp pháp trong hệ thống đo lường quốc tế SI là gì?", ["Mét ($\\text{m}$)", "Kilôgam ($\\text{kg}$)", "Giây ($\\text{s}$)", "Độ Celsius ($^\\circ\\text{C}$)"], 0, "Trong hệ SI, đơn vị cơ bản đo chiều dài là mét ($\\text{m}$)."),
            mcq("biet", "Độ chia nhỏ nhất (ĐCNN) của thước là gì?", ["Chiều dài giữa hai vạch chia liên tiếp trên thước", "Chiều dài lớn nhất ghi trên thước", "Chiều dài nhỏ nhất ghi bằng số trên thước", "Tổng số vạch chia có trên thước"], 0, "ĐCNN của thước là độ dài giữa hai vạch chia liên tiếp trên thước."),
            mcq("hieu", "Khi dùng thước có $\\text{ĐCNN} = 0{,}1\\text{ cm}$ để đo chiều dài cây bút chì, cách ghi kết quả nào sau đây là đúng chuẩn?", ["$14{,}5\\text{ cm}$", "$14\\text{ cm}$", "$14{,}52\\text{ cm}$", "$14{,}555\\text{ cm}$"], 0, "Kết quả đo phải được ghi theo ĐCNN ($0{,}1\\text{ cm}$ có 1 chữ số thập phân), nên $14{,}5\\text{ cm}$ là đúng."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu về phép đo chiều dài:", [
                "Khi đo chiều dài, cần đặt thước dọc theo chiều dài vật và vạch số $0$ trùng với một đầu của vật.",
                "Mắt phải nhìn xiên góc $45^\\circ$ vào đầu kia của vật để đọc kết quả chính xác nhất.",
                "Đổi đơn vị: $2{,}5\\text{ m} = 250\\text{ cm}$.",
                "Nếu từ vạch $0\\text{ cm}$ đến vạch $5\\text{ cm}$ có $10$ khoảng chia bằng nhau thì $\\text{ĐCNN} = 0{,}5\\text{ cm}$.",
            ], [True, False, True, True], "Ý b) sai vì mắt phải nhìn theo hướng vuông góc với cạnh thước tại đầu kia của vật."),
            short("vandung", "Một thước thẳng có khoảng cách từ vạch $0\\text{ cm}$ đến vạch $2\\text{ cm}$ được chia làm $20$ khoảng bằng nhau. Độ chia nhỏ nhất (ĐCNN) của thước này bằng bao nhiêu $\\text{mm}$?", ["1"], "Ta có $\\text{ĐCNN} = \\dfrac{2 - 0}{20} = 0{,}1\\text{ cm} = 1\\text{ mm}$.", unit="mm"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 2: Đo khối lượng",
        icon="⚖️",
        description="Đơn vị đo khối lượng trong hệ SI, các loại cân thông dụng và quy tắc đo khối lượng bằng cân đồng hồ.",
        requirements=[
            "Nêu được khối lượng là số đo lượng chất của một vật và đơn vị cơ bản trong hệ SI là kilôgam ($\\text{kg}$).",
            "Quy đổi được giữa các đơn vị đo khối lượng: tấn, tạ, yến, $\\text{kg}$, $\\text{g}$, $\\text{mg}$.",
            "Trình bày được 5 bước đo khối lượng của một vật bằng cân đồng hồ hoặc cân điện tử.",
        ],
        definition="Mọi vật đều có khối lượng. Khối lượng của một vật chỉ lượng chất tạo nên vật đó. Đơn vị đo khối lượng cơ bản trong hệ SI là kilôgam (kí hiệu $\\text{kg}$).",
        theory=(
            "### 1. Đơn vị đo khối lượng\n"
            "- Đơn vị cơ bản trong hệ SI là **kilôgam** ($\\text{kg}$).\n"
            "- Các đơn vị thường dùng: $1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1000\\text{ kg}$; $1\\text{ kg} = 1000\\text{ g}$; $1\\text{ g} = 1000\\text{ mg}$.\n"
            "- Trên vỏ bao bì hàng hóa thường ghi **khối lượng tịnh** (khối lượng của thực phẩm không tính bao bì).\n\n"
            "### 2. Dụng cụ và cách đo khối lượng\n"
            "- Các loại cân phổ biến: cân đồng hồ, cân điện tử, cân Roberval, cân y tế, cân đòn.\n"
            "- Trước khi đặt vật lên cân đồng hồ, phải **hiệu chỉnh cân** sao cho kim cân chỉ đúng vạch số $0$."
        ),
        formulas=[
            G(
                "Quy đổi đơn vị khối lượng",
                F("Từ tấn, tạ, yến sang kilôgam", "$1\\text{ tấn} = 10\\text{ tạ} = 100\\text{ yến} = 1000\\text{ kg}$", "Dùng để đo khối lượng hàng hóa, nông sản lớn."),
                F("Từ kilôgam sang gam và miligam", "$1\\text{ kg} = 1000\\text{ g} = 10^6\\text{ mg}$", "Dùng trong phòng thí nghiệm, thực phẩm và dược phẩm."),
            )
        ],
        example="Một túi đường ghi khối lượng tịnh là $1{,}5\\text{ kg}$. Nếu chia đều lượng đường này vào $5$ lọ nhỏ bằng nhau thì mỗi lọ chứa bao nhiêu gam ($\\text{g}$) đường?",
        example_answer="Đổi $1{,}5\\text{ kg} = 1500\\text{ g}$. Khối lượng đường trong mỗi lọ nhỏ là $m_1 = \\dfrac{1500}{5} = 300\\text{ g}$.",
        real_life="Dược sĩ dùng cân điện tử có ĐCNN tới $1\\text{ mg}$ để pha chế thuốc, người bán hàng ngoài chợ dùng cân đồng hồ có GHĐ $5\\text{ kg}$ hoặc $10\\text{ kg}$ để cân rau củ.",
        quiz=[
            mcq("biet", "Đơn vị đo khối lượng chuẩn trong hệ thống đo lường quốc tế SI là gì?", ["Kilôgam ($\\text{kg}$)", "Mét ($\\text{m}$)", "Newton ($\\text{N}$)", "Lít ($\\text{L}$)"], 0, "Đơn vị đo khối lượng trong hệ SI là kilôgam ($\\text{kg}$)."),
            mcq("biet", "Trước khi đặt vật lên đĩa cân đồng hồ để đo khối lượng, thao tác bắt buộc nào cần thực hiện?", ["Điều chỉnh ốc hiệu chỉnh để kim cân chỉ đúng vạch số $0$", "Đặt quả cân chuẩn lên đĩa cân", "Nghiêng mặt cân một góc $30^\\circ$", "Nhấn mạnh đĩa cân xuống đáy"], 0, "Cần hiệu chỉnh kim cân về đúng vạch số $0$ trước khi cân để tránh sai số điểm $0$."),
            mcq("hieu", "Để cân một chiếc nhẫn vàng có khối lượng khoảng $3{,}75\\text{ g}$, ta nên chọn loại cân nào sau đây?", ["Cân điện tử có GHĐ $200\\text{ g}$ và ĐCNN $0{,}01\\text{ g}$", "Cân đồng hồ có GHĐ $10\\text{ kg}$ và ĐCNN $50\\text{ g}$", "Cân y tế có GHĐ $120\\text{ kg}$ và ĐCNN $0{,}5\\text{ kg}$", "Cân tạ có GHĐ $500\\text{ kg}$ và ĐCNN $1\\text{ kg}$"], 0, "Chiếc nhẫn nặng $3{,}75\\text{ g}$ có phần lẻ tới $0{,}01\\text{ g}$, nên cần cân điện tử có ĐCNN $0{,}01\\text{ g}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về đo khối lượng:", [
                "Đổi đơn vị: $0{,}5\\text{ tấn} = 500\\text{ kg}$.",
                "Số ghi $500\\text{ g}$ trên vỏ hộp sữa bột chỉ thể tích của chiếc hộp.",
                "Khi đọc kết quả trên cân đồng hồ, mắt phải nhìn vuông góc với vạch chia nơi đầu kim cân chỉ.",
                "Một vật có khối lượng $250\\text{ g}$ tương ứng với $0{,}25\\text{ kg}$.",
            ], [True, False, True, True], "Ý b) sai vì $500\\text{ g}$ chỉ khối lượng của lượng sữa chứa trong hộp."),
            short("vandung", "Một xe tải chở $2{,}4\\text{ tấn}$ gạo. Hỏi khối lượng gạo trên xe bằng bao nhiêu kilôgam ($\\text{kg}$)?", ["2400"], "Ta có $2{,}4\\text{ tấn} = 2{,}4 \\cdot 1000 = 2400\\text{ kg}$.", unit="kg"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 3: Đo thời gian",
        icon="⏱️",
        description="Đơn vị đo thời gian trong hệ SI, đồng hồ bấm giây và các bước đo thời gian trong thí nghiệm.",
        requirements=[
            "Nêu được đơn vị đo thời gian cơ bản trong hệ SI là giây ($\\text{s}$) và quy đổi được giữa giờ, phút, giây.",
            "Lựa chọn được loại đồng hồ phù hợp để đo khoảng thời gian của một hoạt động.",
            "Sử dụng đúng cách đồng hồ bấm giây để đo thời gian trong các thí nghiệm vật lí.",
        ],
        definition="Thời gian là đại lượng dùng để xác định trình tự xảy ra các sự kiện và khoảng kéo dài của một hiện tượng. Đơn vị đo thời gian trong hệ SI là giây (kí hiệu $\\text{s}$).",
        theory=(
            "### 1. Đơn vị và dụng cụ đo thời gian\n"
            "- Đơn vị cơ bản trong hệ SI là **giây** ($\\text{s}$).\n"
            "- Đổi đơn vị: $1\\text{ ngày} = 24\\text{ giờ (h)}$; $1\\text{ h} = 60\\text{ phút (min)} = 3600\\text{ s}$; $1\\text{ min} = 60\\text{ s}$.\n"
            "- Dụng cụ đo thời gian: đồng hồ treo tường, đồng hồ đeo tay, đồng hồ bấm giây (cơ học hoặc điện tử), cổng quang điện.\n\n"
            "### 2. Quy tắc đo thời gian bằng đồng hồ bấm giây\n"
            "1. Ước lượng khoảng thời gian cần đo để chọn đồng hồ phù hợp.\n"
            "2. Nhấn nút `RESET` để đưa đồng hồ bấm giây về vạch số $0$ (`00:00:00`).\n"
            "3. Nhấn `START/STOP` đúng lúc sự kiện bắt đầu và nhấn lần nữa ngay khi sự kiện kết thúc.\n"
            "4. Đọc và ghi kết quả theo ĐCNN của đồng hồ."
        ),
        formulas=[
            G(
                "Quy đổi đơn vị thời gian",
                F("Đổi giờ, phút ra giây", "$1\\text{ h} = 60\\text{ min} = 3600\\text{ s}$", "Nhân số giờ với $3600$ hoặc nhân số phút với $60$ để đổi ra giây."),
                F("Đổi giây ra phần nghìn giây", "$1\\text{ s} = 1000\\text{ ms}$", "Miligiây ($\\text{ms}$) dùng trong đồng hồ hiện số và cổng quang điện."),
            )
        ],
        example="Một vận động viên chạy cự li $400\\text{ m}$ hết $1\\text{ phút } 15\\text{ giây}$. Hãy đổi khoảng thời gian này ra đơn vị giây ($\\text{s}$).",
        example_answer="Ta có $1\\text{ phút} = 60\\text{ s}$. Vậy tổng thời gian chạy của vận động viên là $t = 60 + 15 = 75\\text{ s}$.",
        real_life="Trọng tài điền kinh dùng đồng hồ bấm giây điện tử có $\\text{ĐCNN} = 0{,}01\\text{ s}$ để bấm thành tích chạy $100\\text{ m}$ của các vận động viên.",
        quiz=[
            mcq("biet", "Đơn vị đo thời gian trong hệ thống đo lường quốc tế SI là gì?", ["Giây ($\\text{s}$)", "Giờ ($\\text{h}$)", "Ngày đêm", "Tháng"], 0, "Đơn vị đo thời gian chuẩn trong hệ SI là giây ($\\text{s}$)."),
            mcq("biet", "Để đo thời gian một học sinh chạy cự li $100\\text{ m}$ trong giờ Thể dục, dụng cụ nào sau đây phù hợp nhất?", ["Đồng hồ bấm giây", "Đồng hồ cát", "Lịch treo tường", "Đồng hồ báo thức để bàn"], 0, "Chạy $100\\text{ m}$ diễn ra khoảng $12\\text{ s} - 20\\text{ s}$, cần đo chính xác tới phần mười hoặc phần trăm giây bằng đồng hồ bấm giây."),
            mcq("hieu", "Khoảng thời gian $0{,}5\\text{ giờ}$ tương ứng với bao nhiêu giây?", ["$1800\\text{ s}$", "$30\\text{ s}$", "$300\\text{ s}$", "$3600\\text{ s}$"], 0, "Ta có $0{,}5\\text{ h} = 0{,}5 \\cdot 3600\\text{ s} = 1800\\text{ s}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phép đo thời gian:", [
                "Trước khi đo bằng đồng hồ bấm giây, cần nhấn nút RESET để đưa chỉ số về số $0$.",
                "Đổi đơn vị: $2\\text{ phút } 30\\text{ giây} = 150\\text{ s}$.",
                "Đồng hồ treo tường có kim giờ và kim phút thích hợp để đo thời gian viên bi rơi từ mặt bàn xuống sàn.",
                "Một phần tư giờ bằng $15\\text{ phút}$ hay $900\\text{ s}$.",
            ], [True, True, False, True], "Ý c) sai vì viên bi rơi xuống sàn chỉ mất khoảng $0{,}4\\text{ s}$, phải dùng đồng hồ bấm giây hoặc cổng quang điện."),
            short("vandung", "Một tiết học kéo dài $45\\text{ phút}$. Hãy tính thời gian của một tiết học theo đơn vị giây ($\\text{s}$).", ["2700"], "Đổi $t = 45 \\cdot 60 = 2700\\text{ s}$.", unit="s"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 4: Thang nhiệt độ Celsius. Đo nhiệt độ",
        icon="🌡️",
        description="Khái niệm nhiệt độ, nguyên lý nở vì nhiệt của chất lỏng trong nhiệt kế và công thức đổi các thang nhiệt độ.",
        requirements=[
            "Nêu được nhiệt độ là số đo độ 'nóng', 'lạnh' của một vật và nguyên lý hoạt động của nhiệt kế chất lỏng dựa trên sự nở vì nhiệt.",
            "Xác định được hai mốc chuẩn trong thang nhiệt độ Celsius ($0^\\circ\\text{C}$ và $100^\\circ\\text{C}$).",
            "Vận dụng được công thức chuyển đổi giữa thang Celsius ($^\\circ\\text{C}$), Kelvin ($\\text{K}$) và Fahrenheit ($^\\circ\\text{F}$).",
        ],
        definition="Nhiệt độ là số đo mức độ 'nóng', 'lạnh' của một vật; vật nóng hơn có nhiệt độ cao hơn. Trong thang nhiệt độ Celsius ($^\\circ\\text{C}$), nhiệt độ nước đá đang tan là $0^\\circ\\text{C}$ và hơi nước đang sôi ở áp suất chuẩn là $100^\\circ\\text{C}$.",
        theory=(
            "### 1. Các thang nhiệt độ\n"
            "- **Thang Celsius ($^\\circ\\text{C}$)**: Chia khoảng từ nhiệt độ nước đá đang tan ($0^\\circ\\text{C}$) đến nhiệt độ nước tinh khiết đang sôi ($100^\\circ\\text{C}$) thành $100$ phần bằng nhau.\n"
            "- **Thang Kelvin ($\\text{K}$)**: Đơn vị đo nhiệt độ trong hệ SI là Kelvin ($\\text{K}$), liên hệ bởi $T(\\text{K}) = t(^\\circ\\text{C}) + 273$.\n"
            "- **Thang Fahrenheit ($^\\circ\\text{F}$)**: Liên hệ bởi $t(^\\circ\\text{F}) = 1{,}8 \\cdot t(^\\circ\\text{C}) + 32$.\n\n"
            "### 2. Nhiệt kế và cách đo nhiệt độ\n"
            "- Nhiệt kế rượu, nhiệt kế thủy ngân hoạt động dựa trên **sự nở vì nhiệt của chất lỏng**.\n"
            "- Nhiệt kế y tế thủy ngân có giới hạn đo từ $35^\\circ\\text{C}$ đến $42^\\circ\\text{C}$ và có **chỗ thắt** ở ống quản giúp cột thủy ngân không tự tụt xuống bầu khi lấy nhiệt kế ra khỏi cơ thể."
        ),
        formulas=[
            G(
                "Chuyển đổi giữa các thang nhiệt độ",
                F("Đổi từ độ Celsius sang độ Fahrenheit", "$t(^\\circ\\text{F}) = 1{,}8 \\cdot t(^\\circ\\text{C}) + 32$", "Ở $0^\\circ\\text{C}$ tương ứng $32^\\circ\\text{F}$; ở $100^\\circ\\text{C}$ tương ứng $212^\\circ\\text{F}$."),
                F("Đổi từ độ Celsius sang độ Kelvin", "$T(\\text{K}) = t(^\\circ\\text{C}) + 273$", "Mỗi độ chia $1\\text{ K}$ có độ lớn đúng bằng $1^\\circ\\text{C}$."),
            )
        ],
        example="Nhiệt độ cơ thể người bình thường là $37^\\circ\\text{C}$. Hãy tính nhiệt độ này theo thang nhiệt độ Fahrenheit ($^\\circ\\text{F}$) và thang Kelvin ($\\text{K}$).",
        example_answer="Theo thang Fahrenheit: $t(^\\circ\\text{F}) = 1{,}8 \\cdot 37 + 32 = 98{,}6^\\circ\\text{F}$. Theo thang Kelvin: $T(\\text{K}) = 37 + 273 = 310\\text{ K}$.",
        real_life="Nhiệt kế hồng ngoại đo thân nhiệt từ xa không tiếp xúc giúp kiểm tra sức khỏe nhanh chóng; nhiệt kế y tế đo thân nhiệt người có thang chia từ $35^\\circ\\text{C}$ đến $42^\\circ\\text{C}$.",
        quiz=[
            mcq("biet", "Nhiệt kế chất lỏng (như nhiệt kế rượu hoặc thủy ngân) hoạt động dựa trên hiện tượng vật lí nào?", ["Sự nở vì nhiệt của chất lỏng", "Sự nở vì nhiệt của chất khí", "Sự bay hơi của chất lỏng", "Sự đông đặc của chất lỏng"], 0, "Khi nhiệt độ tăng, chất lỏng trong bầu nhiệt kế nở ra và dâng lên trong ống mao dẫn."),
            mcq("biet", "Trong thang nhiệt độ Celsius, nhiệt độ của hơi nước tinh khiết đang sôi ở áp suất chuẩn là bao nhiêu?", ["$100^\\circ\\text{C}$", "$0^\\circ\\text{C}$", "$37^\\circ\\text{C}$", "$273^\\circ\\text{C}$"], 0, "Trong thang Celsius, nước đá đang tan là $0^\\circ\\text{C}$ và hơi nước đang sôi là $100^\\circ\\text{C}$."),
            mcq("hieu", "Vì sao không thể dùng nhiệt kế y tế (GHĐ từ $35^\\circ\\text{C}$ đến $42^\\circ\\text{C}$) để đo nhiệt độ của nước đang sôi?", ["Vì nhiệt độ nước sôi ($100^\\circ\\text{C}$) vượt quá giới hạn đo ($42^\\circ\\text{C}$) làm vỡ bầu nhiệt kế", "Vì thủy ngân trong nhiệt kế y tế đông đặc ở $100^\\circ\\text{C}$", "Vì nước sôi làm mất màu vạch chia của nhiệt kế", "Vì nhiệt kế y tế chỉ đo được nhiệt độ âm"], 0, "Nhiệt độ nước sôi là $100^\\circ\\text{C} > 42^\\circ\\text{C}$ nên thủy ngân nở mạnh sẽ làm nứt vỡ ống nhiệt kế."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về thang nhiệt độ và nhiệt kế:", [
                "Ở $0^\\circ\\text{C}$ tương ứng với $32^\\circ\\text{F}$ trong thang Fahrenheit.",
                "Nhiệt độ $27^\\circ\\text{C}$ tương ứng với $300\\text{ K}$ trong thang Kelvin.",
                "Ống quản của nhiệt kế y tế có chỗ thắt để ngăn thủy ngân tự tụt xuống khi lấy nhiệt kế ra khỏi cơ thể để đọc.",
                "Cảm giác của tay người luôn cho phép xác định chính xác tuyệt đối nhiệt độ của mọi vật.",
            ], [True, True, True, False], "Ý d) sai vì cảm giác của tay chỉ mang tính tương đối và dễ sai lệch, cần dùng nhiệt kế để đo chính xác."),
            short("vandung", "Một bản tin thời tiết báo nhiệt độ ngoài trời tại Hà Nội là $25^\\circ\\text{C}$. Nhiệt độ này tương ứng với bao nhiêu độ Fahrenheit ($^\\circ\\text{F}$)?", ["77"], "Áp dụng công thức: $t(^\\circ\\text{F}) = 1{,}8 \\cdot 25 + 32 = 45 + 32 = 77^\\circ\\text{F}$.", unit="°F"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 5: Lực và tác dụng của lực",
        icon="🥊",
        description="Khái niệm lực đẩy, lực kéo, đơn vị lực Newton (N) và hai tác dụng cơ bản của lực lên vật.",
        requirements=[
            "Nêu được tác dụng đẩy hoặc kéo của vật này lên vật khác gọi là lực và đơn vị đo lực là Newton ($\\text{N}$).",
            "Chỉ ra được hai tác dụng cơ bản của lực: làm biến đổi chuyển động của vật hoặc làm vật bị biến dạng.",
            "Lấy được ví dụ thực tế về lực vừa làm biến dạng vật vừa làm thay đổi chuyển động của vật.",
        ],
        definition="Tác dụng đẩy hoặc kéo của vật này lên vật khác được gọi là lực (kí hiệu $F$). Đơn vị đo lực trong hệ SI là Newton (kí hiệu $\\text{N}$).",
        theory=(
            "### 1. Khái niệm lực\n"
            "- Khi vật $A$ đẩy hoặc kéo vật $B$, ta nói vật $A$ tác dụng **lực** lên vật $B$.\n"
            "- Kí hiệu của độ lớn lực là $F$, đơn vị đo trong hệ SI là **Newton** ($\\text{N}$).\n\n"
            "### 2. Hai tác dụng của lực\n"
            "1. **Làm biến đổi chuyển động của vật**: làm vật đang đứng yên bắt đầu chuyển động, đang chuyển động thì dừng lại, chuyển động nhanh lên, chậm đi hoặc đổi hướng chuyển động.\n"
            "2. **Làm biến dạng vật**: làm thay đổi hình dạng hoặc kích thước của vật (như bóp méo quả bóng, kéo dãn lò xo).\n"
            "- Một lực có thể đồng thời gây ra cả hai tác dụng trên (ví dụ: cầu thủ sút quả bóng cao su)."
        ),
        formulas=[
            G(
                "Kí hiệu và tác dụng của lực",
                F("Đơn vị đo lực trong hệ SI", "$[F] = \\text{N (Newton)}$", "Đặt theo tên nhà bác học Isaac Newton."),
                F("Hai dấu hiệu nhận biết có lực tác dụng", "$\\text{Lực } F \\Rightarrow \\begin{cases} \\text{Biến đổi chuyển động (tốc độ, hướng)} \\\\ \\text{Biến dạng vật (hình dạng, kích thước)} \\end{cases}$", "Có thể xảy ra một trong hai hoặc đồng thời cả hai tác dụng."),
            )
        ],
        example="Khi cầu thủ đá mạnh vào quả bóng đang nằm yên trên sân cỏ, lực của chân cầu thủ tác dụng lên quả bóng đã gây ra những kết quả gì?",
        example_answer="Lực đá của chân cầu thủ gây ra đồng thời 2 tác dụng: (1) làm quả bóng bị móp nhẹ tại chỗ tiếp xúc (biến dạng) và (2) làm quả bóng từ đứng yên bay vọt đi (biến đổi chuyển động).",
        real_life="Vợt cầu lông đập vào quả cầu làm mặt lưới vợt lún xuống (biến dạng) và làm quả cầu đổi hướng bay ngược lại (biến đổi chuyển động).",
        quiz=[
            mcq("biet", "Tác dụng đẩy hoặc kéo của vật này lên vật khác được gọi là gì?", ["Lực", "Khối lượng", "Quãng đường", "Thể tích"], 0, "Tác dụng đẩy hoặc kéo của vật này lên vật khác được gọi là lực."),
            mcq("biet", "Đơn vị đo lực trong hệ thống đo lường quốc tế SI là gì?", ["Newton ($\\text{N}$)", "Kilôgam ($\\text{kg}$)", "Mét ($\\text{m}$)", "Joule ($\\text{J}$)"], 0, "Đơn vị đo lực trong hệ SI là Newton ($\\text{N}$)."),
            mcq("hieu", "Trong trường hợp nào sau đây, lực chỉ làm vật bị biến dạng mà không làm vật thay đổi trạng thái đứng yên?", ["Lấy hai tay ép nhẹ hai đầu một chiếc lò xo đang đặt yên trên bàn", "Đá quả bóng lăn trên sân", "Gió thổi làm thuyền buồm chạy nhanh hơn", "Bóp phanh làm xe đạp dừng lại"], 0, "Ép nhẹ lò xo giữ yên trên bàn làm lò xo ngắn lại (biến dạng) nhưng lò xo vẫn đứng yên."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về lực và tác dụng của lực:", [
                "Khi thủ môn bắt dính quả bóng đang bay tới, lực của tay thủ môn đã làm quả bóng biến đổi chuyển động.",
                "Lực tác dụng lên một vật không bao giờ vừa làm vật biến dạng vừa làm vật đổi hướng chuyển động.",
                "Gió thổi làm cành cây uốn cong là ví dụ về tác dụng làm biến dạng của lực.",
                "Viên bi sắt lăn chạm vào thành bàn rồi bật ngược lại chứng tỏ lực của thành bàn đã làm đổi hướng chuyển động của viên bi.",
            ], [True, False, True, True], "Ý b) sai vì lực hoàn toàn có thể gây ra đồng thời cả hai tác dụng biến dạng và biến đổi chuyển động."),
            short("vandung", "Có mấy tác dụng cơ bản của lực lên một vật (biến đổi chuyển động và biến dạng)?", ["2"], "Lực tác dụng lên vật có $2$ tác dụng cơ bản: làm biến đổi chuyển động và làm biến dạng vật."),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 6: Biểu diễn lực",
        icon="🏹",
        description="Các đặc trưng của lực (điểm đặt, phương, chiều, độ lớn) và cách biểu diễn lực bằng mũi tên theo tỉ xích.",
        requirements=[
            "Nêu được 4 yếu tố đặc trưng của một lực: điểm đặt (gốc), phương, chiều và độ lớn.",
            "Biểu diễn được một lực bằng một mũi tên trên hình vẽ theo tỉ xích cho trước.",
            "Xác định được độ lớn của lực từ hình biểu diễn lực khi biết tỉ xích.",
        ],
        definition="Lực là một đại lượng vectơ được biểu diễn bằng một mũi tên có: gốc là điểm mà lực tác dụng lên vật, phương và chiều trùng với phương và chiều của lực, độ dài biểu thị độ lớn của lực theo một tỉ xích cho trước.",
        theory=(
            "### 1. Các đặc trưng của lực\n"
            "- Kết quả tác dụng của lực phụ thuộc vào 4 yếu tố:\n"
            "  1. **Điểm đặt**: vị trí lực tác dụng lên vật.\n"
            "  2. **Phương**: nằm ngang, thẳng đứng hay xiên góc.\n"
            "  3. **Chiều**: từ trái sang phải, từ dưới lên trên, từ trên xuống dưới...\n"
            "  4. **Độ lớn (cường độ)**: mạnh hay yếu, kí hiệu là $F$ (đơn vị $\\text{N}$).\n\n"
            "### 2. Cách biểu diễn lực bằng mũi tên\n"
            "- Dùng một mũi tên để biểu diễn lực $\\vec{F}$:\n"
            "  - **Gốc mũi tên**: đặt tại điểm lực tác dụng lên vật.\n"
            "  - **Hướng mũi tên**: theo đúng phương và chiều của lực.\n"
            "  - **Chiều dài mũi tên**: gồm $n$ đoạn đơn vị ứng với tỉ xích đã chọn ($F = n \\cdot \\Delta F$)."
        ),
        formulas=[
            G(
                "Biểu diễn lực theo tỉ xích",
                F("Độ lớn lực theo tỉ xích", "$F = n \\cdot \\Delta F$", "Trong đó $n$ là số đoạn chia trên mũi tên, $\\Delta F$ là giá trị lực ứng với $1$ đoạn tỉ xích (ví dụ $1\\text{ cm} \\leftrightarrow 5\\text{ N}$)."),
                F("Số đoạn tỉ xích cần vẽ", "$n = \\dfrac{F}{\\Delta F}$", "Dùng để xác định chiều dài mũi tên khi vẽ lực $\\vec{F}$."),
            )
        ],
        example="Cần biểu diễn lực kéo $F = 30\\text{ N}$ theo phương nằm ngang, chiều từ trái sang phải, với tỉ xích $1\\text{ cm}$ ứng với $10\\text{ N}$. Mũi tên biểu diễn lực có chiều dài bao nhiêu $\\text{cm}$?",
        example_answer="Số đoạn tỉ xích cần vẽ là $n = \\dfrac{F}{\\Delta F} = \\dfrac{30}{10} = 3$. Vậy mũi tên biểu diễn lực dài $3\\text{ cm}$, hướng ngang từ trái sang phải.",
        real_life="Trong bản vẽ thiết kế cầu đường và xây dựng, các kĩ sư dùng các mũi tên tỉ xích để biểu diễn lực chịu tải của dầm cầu và trụ cột.",
        quiz=[
            mcq("biet", "Để biểu diễn một lực trên hình vẽ, người ta sử dụng kí hiệu hình học nào?", ["Một mũi tên", "Một hình tròn", "Một hình vuông", "Một đường gấp khúc khép kín"], 0, "Lực có điểm đặt, phương, chiều và độ lớn nên được biểu diễn bằng một mũi tên."),
            mcq("biet", "Gốc của mũi tên biểu diễn lực cho biết yếu tố nào của lực?", ["Điểm đặt mà lực tác dụng lên vật", "Độ lớn của lực", "Đơn vị đo của lực", "Khối lượng của vật chịu lực"], 0, "Gốc của mũi tên đặt tại điểm mà lực tác dụng lên vật."),
            mcq("hieu", "Trên hình vẽ, một lực kéo được biểu diễn bằng mũi tên dài $4$ đoạn tỉ xích, biết mỗi đoạn tỉ xích ứng với $5\\text{ N}$. Độ lớn của lực kéo đó là bao nhiêu?", ["$20\\text{ N}$", "$9\\text{ N}$", "$1{,}25\\text{ N}$", "$45\\text{ N}$"], 0, "Ta có $F = n \\cdot \\Delta F = 4 \\cdot 5 = 20\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về biểu diễn lực:", [
                "Mũi tên biểu diễn lực cho biết đồng thời điểm đặt, phương, chiều và độ lớn của lực.",
                "Nếu chọn tỉ xích $1\\text{ cm}$ ứng với $2\\text{ N}$ thì lực $10\\text{ N}$ được vẽ bằng mũi tên dài $5\\text{ cm}$.",
                "Hai lực có cùng độ lớn $15\\text{ N}$ thì luôn có cùng phương và cùng chiều.",
                "Trọng lực tác dụng lên quả táo luôn được biểu diễn bằng mũi tên có phương thẳng đứng, chiều từ trên xuống dưới.",
            ], [True, True, False, True], "Ý c) sai vì hai lực có cùng độ lớn vẫn có thể khác phương hoặc ngược chiều nhau."),
            short("vandung", "Một lực đẩy có độ lớn $F = 45\\text{ N}$ được biểu diễn theo tỉ xích $1\\text{ cm}$ ứng với $15\\text{ N}$. Chiều dài mũi tên biểu diễn lực này bằng bao nhiêu $\\text{cm}$?", ["3"], "Số xăng-ti-mét cần vẽ là $n = \\dfrac{45}{15} = 3\\text{ cm}$.", unit="cm"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 7: Biến dạng của lò xo. Phép đo lực",
        icon="🌀",
        description="Đặc điểm biến dạng đàn hồi của lò xo, độ giãn của lò xo và cách đo lực bằng lực kế.",
        requirements=[
            "Tính được độ giãn của lò xo thẳng đứng khi treo vật: $\\Delta l = l - l_0$.",
            "Nhận biết được độ giãn của lò xo tỉ lệ thuận với khối lượng (hoặc trọng lượng) vật treo trong giới hạn đàn hồi.",
            "Trình bày được cấu tạo và các bước đo lực bằng lực kế lò xo.",
        ],
        definition="Khi treo vật vào lò xo thẳng đứng, lò xo bị dãn ra một đoạn $\\Delta l = l - l_0$ (với $l_0$ là chiều dài tự nhiên, $l$ là chiều dài khi treo vật). Trong giới hạn đàn hồi, độ giãn $\\Delta l$ tỉ lệ thuận với lực kéo tác dụng lên lò xo.",
        theory=(
            "### 1. Biến dạng của lò xo\n"
            "- Chiều dài ban đầu khi chưa treo vật gọi là **chiều dài tự nhiên** $l_0$.\n"
            "- Khi treo vật, lò xo có chiều dài $l$. **Độ giãn của lò xo** là $\\Delta l = l - l_0$.\n"
            "- Trong giới hạn đàn hồi, khi khối lượng (hoặc lực kéo) tăng gấp $k$ lần thì độ giãn $\\Delta l$ cũng tăng gấp $k$ lần: $\\dfrac{\\Delta l_1}{\\Delta l_2} = \\dfrac{m_1}{m_2} = \\dfrac{F_1}{F_2}$.\n\n"
            "### 2. Lực kế và phép đo lực\n"
            "- **Lực kế** là dụng cụ dùng để đo lực, hoạt động dựa trên tính chất độ giãn của lò xo tỉ lệ với lực tác dụng.\n"
            "- Các bước đo lực: ước lượng lực cần đo $\\rightarrow$ chọn lực kế có GHĐ và ĐCNN phù hợp $\\rightarrow$ hiệu chỉnh kim về vạch số $0$ $\\rightarrow$ cho lực tác dụng vào móc lực kế dọc theo trục lò xo $\\rightarrow$ đọc kết quả."
        ),
        formulas=[
            G(
                "Độ giãn của lò xo",
                F("Độ giãn của lò xo khi kéo giãn", "$\\Delta l = l - l_0$", "Trong đó $l_0$ là chiều dài tự nhiên, $l$ là chiều dài lò xo khi chịu lực kéo."),
                F("Quy tắc tỉ lệ độ giãn lò xo", "$\\dfrac{\\Delta l_1}{\\Delta l_2} = \\dfrac{m_1}{m_2} = \\dfrac{F_1}{F_2}$", "Áp dụng trong giới hạn đàn hồi của lò xo."),
            )
        ],
        example="Một lò xo có chiều dài tự nhiên $l_0 = 12\\text{ cm}$. Khi treo một quả nặng có khối lượng $m_1 = 50\\text{ g}$ thì lò xo dài $l_1 = 14\\text{ cm}$. Hỏi nếu treo quả nặng có khối lượng $m_2 = 150\\text{ g}$ thì lò xo có chiều dài $l_2$ bằng bao nhiêu?",
        example_answer="Khi treo $m_1 = 50\\text{ g}$, độ giãn là $\\Delta l_1 = l_1 - l_0 = 14 - 12 = 2\\text{ cm}$. Khi treo $m_2 = 150\\text{ g} = 3 m_1$, độ giãn tăng $3$ lần: $\\Delta l_2 = 3 \\cdot 2 = 6\\text{ cm}$. Chiều dài lò xo lúc đó là $l_2 = l_0 + \\Delta l_2 = 12 + 6 = 18\\text{ cm}$.",
        real_life="Cân lò xo, lực kế phòng thí nghiệm, giảm xóc xe máy và đệm lò xo đều ứng dụng tính đàn hồi của lò xo.",
        quiz=[
            mcq("biet", "Dụng cụ nào sau đây được dùng để đo độ lớn của lực?", ["Lực kế", "Nhiệt kế", "Đồng hồ bấm giây", "Thước cuộn"], 0, "Lực kế là dụng cụ dùng để đo lực."),
            mcq("biet", "Gọi $l_0$ là chiều dài tự nhiên của lò xo và $l$ là chiều dài của lò xo khi treo vật nặng. Độ giãn $\\Delta l$ của lò xo được tính bằng công thức nào?", ["$\\Delta l = l - l_0$", "$\\Delta l = l + l_0$", "$\\Delta l = l \\cdot l_0$", "$\\Delta l = \\dfrac{l}{l_0}$"], 0, "Độ giãn của lò xo bằng hiệu giữa chiều dài lúc dãn $l$ và chiều dài tự nhiên $l_0$: $\\Delta l = l - l_0$."),
            mcq("hieu", "Một lò xo có chiều dài tự nhiên $10\\text{ cm}$. Khi treo quả cân $100\\text{ g}$ thì lò xo dài $12\\text{ cm}$. Độ giãn của lò xo khi đó là bao nhiêu?", ["$2\\text{ cm}$", "$10\\text{ cm}$", "$12\\text{ cm}$", "$22\\text{ cm}$"], 0, "Độ giãn của lò xo là $\\Delta l = l - l_0 = 12 - 10 = 2\\text{ cm}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về biến dạng lò xo và phép đo lực:", [
                "Trong giới hạn đàn hồi, khi bỏ vật nặng ra thì lò xo trở về chiều dài tự nhiên $l_0$ ban đầu.",
                "Độ giãn của lò xo tỉ lệ thuận với khối lượng vật treo trong giới hạn đàn hồi.",
                "Khi đo lực bằng lực kế, ta có thể kéo móc lực kế lệch góc vuông với trục lò xo.",
                "Nếu treo $1$ quả nặng lò xo giãn thêm $3\\text{ cm}$ thì khi treo $2$ quả nặng giống hệt nhau lò xo giãn thêm $6\\text{ cm}$.",
            ], [True, True, False, True], "Ý c) sai vì khi đo lực phải giữ cho phương của lực trùng với trục của lò xo trong lực kế để không bị kẹt."),
            short("vandung", "Một lò xo có chiều dài tự nhiên $l_0 = 15\\text{ cm}$. Khi treo vật nặng $100\\text{ g}$ thì lò xo giãn thêm $\\Delta l_1 = 3\\text{ cm}$. Hỏi khi treo vật nặng $200\\text{ g}$ thì chiều dài tổng cộng $l_2$ của lò xo bằng bao nhiêu $\\text{cm}$?", ["21"], "Khi treo $200\\text{ g}$, độ giãn là $\\Delta l_2 = 2 \\cdot 3 = 6\\text{ cm}$. Chiều dài lò xo là $l_2 = 15 + 6 = 21\\text{ cm}$.", unit="cm"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 8: Trọng lực và đơn vị lực",
        icon="🍎",
        description="Khái niệm trọng lực, trọng lượng, phương và chiều của trọng lực, hệ thức liên hệ P = 10m.",
        requirements=[
            "Nêu được trọng lực là lực hút của Trái Đất tác dụng lên vật, có phương thẳng đứng và chiều hướng về phía Trái Đất.",
            "Phân biệt được khối lượng $m$ (đơn vị $\\text{kg}$) và trọng lượng $P$ (đơn vị $\\text{N}$).",
            "Vận dụng được công thức $P = 10m$ để tính trọng lượng hoặc khối lượng của vật.",
        ],
        definition="Trọng lực là lực hút của Trái Đất tác dụng lên vật, có phương thẳng đứng và chiều từ trên xuống dưới (hướng về tâm Trái Đất). Độ lớn của trọng lực tác dụng lên vật gọi là trọng lượng (kí hiệu $P$).",
        theory=(
            "### 1. Trọng lực và trọng lượng\n"
            "- Mọi vật ở gần mặt đất đều chịu lực hút của Trái Đất gọi là **trọng lực**.\n"
            "- Trọng lực có **phương thẳng đứng**, **chiều từ trên xuống dưới**.\n"
            "- Độ lớn của trọng lực tác dụng lên vật được gọi là **trọng lượng** của vật, kí hiệu là $P$ (đơn vị $\\text{N}$).\n\n"
            "### 2. Liên hệ giữa trọng lượng và khối lượng\n"
            "- Quả cân có khối lượng $m = 100\\text{ g} = 0{,}1\\text{ kg}$ có trọng lượng $P \\approx 1\\text{ N}$.\n"
            "- Vật có khối lượng $m = 1\\text{ kg}$ có trọng lượng $P \\approx 10\\text{ N}$. Tổng quát: $P = 10m$ (với $m$ tính bằng $\\text{kg}$, $P$ tính bằng $\\text{N}$)."
        ),
        formulas=[
            G(
                "Trọng lượng và Khối lượng",
                F("Công thức tính trọng lượng gần mặt đất", "$P = 10 \\cdot m$", "Trong đó $m$ là khối lượng của vật ($\\text{kg}$), $P$ là trọng lượng của vật ($\\text{N}$)."),
                F("Tính khối lượng khi biết trọng lượng", "$m = \\dfrac{P}{10}$", "Ví dụ: vật có trọng lượng $P = 50\\text{ N}$ thì có khối lượng $m = 5\\text{ kg}$."),
            )
        ],
        example="Một bạn học sinh có khối lượng $m = 42\\text{ kg}$. Hãy tính trọng lượng $P$ của bạn học sinh đó trên mặt đất.",
        example_answer="Áp dụng công thức $P = 10m$, trọng lượng của bạn học sinh là $P = 10 \\cdot 42 = 420\\text{ N}$.",
        real_life="Thợ xây dùng dây dọi (quả nặng treo vào đầu sợi dây mềm) để xác định phương thẳng đứng khi xây tường nhờ phương của trọng lực.",
        quiz=[
            mcq("biet", "Trọng lực tác dụng lên một vật ở gần mặt đất có phương và chiều như thế nào?", ["Phương thẳng đứng, chiều từ trên xuống dưới", "Phương nằm ngang, chiều từ trái sang phải", "Phương thẳng đứng, chiều từ dưới lên trên", "Phương xiên góc $45^\\circ$ so với mặt đất"], 0, "Trọng lực là lực hút của Trái Đất nên luôn có phương thẳng đứng và chiều từ trên xuống dưới."),
            mcq("biet", "Hệ thức liên hệ gần đúng giữa trọng lượng $P$ ($\\text{N}$) và khối lượng $m$ ($\\text{kg}$) của một vật gần mặt đất là gì?", ["$P = 10m$", "$P = \\dfrac{m}{10}$", "$P = 100m$", "$P = m + 10$"], 0, "Một vật có khối lượng $m$ ($\\text{kg}$) chịu trọng lượng $P = 10m$ ($\\text{N}$)."),
            mcq("hieu", "Một quả cân có khối lượng $500\\text{ g}$ thì có trọng lượng bằng bao nhiêu Newton?", ["$5\\text{ N}$", "$50\\text{ N}$", "$500\\text{ N}$", "$5000\\text{ N}$"], 0, "Đổi $m = 500\\text{ g} = 0{,}5\\text{ kg}$. Trọng lượng của quả cân là $P = 10 \\cdot 0{,}5 = 5\\text{ N}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về trọng lực và khối lượng:", [
                "Khối lượng chỉ lượng chất của vật (đơn vị $\\text{kg}$), còn trọng lượng là độ lớn lực hút của Trái Đất tác dụng lên vật (đơn vị $\\text{N}$).",
                "Một vật có trọng lượng $P = 80\\text{ N}$ thì có khối lượng $m = 8\\text{ kg}$.",
                "Khi đưa một vật từ Trái Đất lên Mặt Trăng, khối lượng của vật giảm đi $6$ lần.",
                "Dây dọi giúp thợ xây kiểm tra bức tường có thẳng đứng hay không dựa vào phương của trọng lực.",
            ], [True, True, False, True], "Ý c) sai vì khối lượng là lượng chất chứa trong vật nên không đổi khi lên Mặt Trăng (chỉ có trọng lượng giảm khoảng $6$ lần)."),
            short("vandung", "Một thùng hàng có khối lượng $m = 15\\text{ kg}$. Trọng lượng $P$ của thùng hàng đó bằng bao nhiêu Newton ($\\text{N}$)?", ["150"], "Áp dụng công thức $P = 10m = 10 \\cdot 15 = 150\\text{ N}$.", unit="N"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 9: Lực tiếp xúc và lực không tiếp xúc",
        icon="🧲",
        description="Phân biệt điều kiện xuất hiện lực tiếp xúc và lực không tiếp xúc qua các hiện tượng thực tế.",
        requirements=[
            "Phân biệt được lực tiếp xúc (xuất hiện khi hai vật chạm trực tiếp vào nhau) và lực không tiếp xúc (xuất hiện ngay cả khi hai vật không chạm nhau).",
            "Nêu được các ví dụ về lực tiếp xúc (lực đẩy tay, lực kéo dây, lực ma sát) và lực không tiếp xúc (trọng lực, lực từ, lực tĩnh điện).",
            "Giải thích được hiện tượng tương tác giữa nam châm với sắt hoặc giữa Trái Đất với Mặt Trăng là lực không tiếp xúc.",
        ],
        definition="Lực tiếp xúc xuất hiện khi vật gây ra lực có sự tiếp xúc trực tiếp với vật chịu tác dụng của lực. Lực không tiếp xúc xuất hiện khi vật gây ra lực không tiếp xúc trực tiếp với vật chịu tác dụng của lực.",
        theory=(
            "### 1. Lực tiếp xúc\n"
            "- Xuất hiện khi hai vật **chạm trực tiếp** vào nhau.\n"
            "- Ví dụ: tay đẩy xe hàng, chân cầu thủ sút quả bóng, búa đóng đinh, gió đập vào cánh buồm.\n\n"
            "### 2. Lực không tiếp xúc\n"
            "- Xuất hiện khi vật gây ra lực **không cần chạm** vào vật chịu lực (tác dụng qua trường).\n"
            "- Ví dụ:\n"
            "  - **Lực hấp dẫn (trọng lực)**: Trái Đất hút quả táo rơi xuống, Trái Đất hút Mặt Trăng.\n"
            "  - **Lực từ**: Nam châm hút đinh sắt đặt cách nó một khoảng.\n"
            "  - **Lực tĩnh điện**: Thước nhựa nhiễm điện hút các vụn giấy nhỏ từ xa."
        ),
        formulas=[
            G(
                "Phân loại lực theo sự tiếp xúc",
                F("Điều kiện của lực tiếp xúc", "$d_{\\text{tiếp xúc}} = 0 \\text{ (hai vật chạm trực tiếp nhau)}$", "Ví dụ: lực nâng của tay, lực căng dây, lực ma sát, lực đàn hồi khi ép lò xo."),
                F("Điều kiện của lực không tiếp xúc", "$d > 0 \\text{ (tác dụng từ xa qua không gian)}$", "Bao gồm: lực hấp dẫn (trọng lực), lực từ của nam châm, lực điện giữa các điện tích."),
            )
        ],
        example="Xét hiện tượng: một quả dừa chín rụng từ trên cây rơi xuống mặt đất (bỏ qua sức cản không khí) và khi chạm đất làm mặt đất lún xuống một vết nhỏ. Hãy chỉ ra đâu là lực không tiếp xúc và đâu là lực tiếp xúc.",
        example_answer="Lực hút của Trái Đất (trọng lực) kéo quả dừa rơi từ trên cây xuống là **lực không tiếp xúc**. Khi quả dừa đập trực tiếp vào mặt đất làm đất lún xuống, lực giữa quả dừa và mặt đất là **lực tiếp xúc**.",
        real_life="Cần cẩu từ trong nhà máy thép dùng nam châm điện hút các tấm sắt vụn từ khoảng cách gần; tàu đệm từ (Maglev) nâng thân tàu lơ lửng trên đường ray nhờ lực từ không tiếp xúc.",
        quiz=[
            mcq("biet", "Lực nào sau đây là lực không tiếp xúc?", ["Lực hút của Trái Đất tác dụng lên giọt mưa đang rơi", "Lực của tay người đẩy chiếc xe nôi", "Lực của đầu búa đập vào chiếc đinh", "Lực của mặt vợt đập vào quả bóng bàn"], 0, "Trái Đất hút giọt mưa từ trên cao mà không cần chạm trực tiếp vào giọt mưa nên đó là lực không tiếp xúc."),
            mcq("biet", "Lực tiếp xúc xuất hiện khi nào?", ["Khi vật gây ra lực tiếp xúc trực tiếp với vật chịu tác dụng của lực", "Khi hai vật đặt cách xa nhau trong chân không", "Khi một nam châm đặt gần một cực của nam châm khác", "Khi Trái Đất quay quanh Mặt Trời"], 0, "Lực tiếp xúc chỉ xuất hiện khi hai vật có sự tiếp xúc trực tiếp với nhau."),
            mcq("hieu", "Đưa một thanh nam châm lại gần (nhưng chưa chạm vào) một chiếc ghim sắt nằm trên bàn thì chiếc ghim sắt bị hút dịch chuyển về phía nam châm. Trong quá trình chiếc ghim đang trượt trên mặt bàn, chiếc ghim chịu tác dụng của những lực nào?", ["Vừa chịu lực không tiếp xúc (lực từ, trọng lực) vừa chịu lực tiếp xúc (lực nâng và ma sát của mặt bàn)", "Chỉ chịu duy nhất lực không tiếp xúc", "Chỉ chịu duy nhất lực tiếp xúc", "Không chịu tác dụng của lực nào"], 0, "Ghim sắt chịu lực từ của nam châm và trọng lực của Trái Đất (lực không tiếp xúc), đồng thời chạm mặt bàn nên chịu lực nâng và ma sát của bàn (lực tiếp xúc)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu phân loại lực sau đây:", [
                "Lực của gió thổi căng cánh buồm là lực tiếp xúc vì không khí va đập trực tiếp vào mặt buồm.",
                "Lực đẩy giữa hai cực cùng tên của hai thanh nam châm đặt gần nhau là lực không tiếp xúc.",
                "Trọng lực giữ Mặt Trăng chuyển động quanh Trái Đất là một lực tiếp xúc.",
                "Thước nhựa sau khi cọ xát vào vải khô hút được các mẩu giấy vụn từ xa nhờ lực không tiếp xúc.",
            ], [True, True, False, True], "Ý c) sai vì Trái Đất và Mặt Trăng không chạm vào nhau, lực hấp dẫn giữa chúng là lực không tiếp xúc."),
            short("vandung", "Cho 4 lực sau: (1) Trọng lực của Trái Đất hút quả bóng đang bay; (2) Lực từ của nam châm hút đinh sắt từ xa; (3) Lực tay kéo cánh cửa; (4) Lực chân đạp bàn đạp xe đạp. Có bao nhiêu lực trong danh sách trên là **lực không tiếp xúc**?", ["2"], "Các lực (1) trọng lực và (2) lực từ của nam châm tác dụng từ xa là $2$ lực không tiếp xúc; còn (3) và (4) là lực tiếp xúc."),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 10: Lực ma sát và lực cản của môi trường",
        icon="🛞",
        description="Lực ma sát trượt, ma sát nghỉ, ma sát lăn, lực cản của nước và không khí cùng tác dụng có lợi, có hại.",
        requirements=[
            "Phân biệt được lực ma sát trượt, lực ma sát nghỉ và lực ma sát lăn qua các tình huống thực tế.",
            "Nêu được tác dụng có lợi và có hại của lực ma sát trong đời sống và giao thông.",
            "Nhận biết được lực cản của nước và không khí phụ thuộc vào hình dạng của vật chuyển động.",
        ],
        definition="Lực ma sát là lực tiếp xúc xuất hiện ở bề mặt tiếp xúc giữa hai vật, cản trở chuyển động (hoặc xu hướng chuyển động) của vật này trên bề mặt vật kia. Khi vật chuyển động trong không khí hoặc trong nước, vật còn chịu lực cản của môi trường.",
        theory=(
            "### 1. Các loại lực ma sát\n"
            "- **Lực ma sát trượt**: xuất hiện khi một vật trượt trên bề mặt của vật khác (ví dụ: má phanh ép vào vành bánh xe, đẩy thùng gỗ trượt trên sàn).\n"
            "- **Lực ma sát nghỉ**: giữ cho vật đứng yên khi vật bị tác dụng của một lực khác có xu hướng làm nó trượt (ví dụ: giúp bàn chân không bị trượt khi đi bộ, giữ vật đứng yên trên mặt phẳng nghiêng).\n"
            "- **Lực ma sát lăn**: xuất hiện khi vật lăn trên bề mặt vật khác, có độ lớn nhỏ hơn nhiều so với ma sát trượt.\n\n"
            "### 2. Lực cản của nước và không khí\n"
            "- Vật chuyển động trong không khí hay trong nước luôn chịu **lực cản** ngược chiều chuyển động.\n"
            "- Vật có hình dạng **khí động học (thuôn nhọn)** giúp giảm đáng kể lực cản của nước và không khí."
        ),
        formulas=[
            G(
                "Đặc điểm của lực ma sát và lực cản",
                F("Chiều của lực ma sát trượt và lực cản", "$\\vec{F}_{\\text{ms}} \\uparrow\\downarrow \\vec{v}$", "Lực ma sát trượt và lực cản môi trường luôn ngược chiều với vận tốc chuyển động tương đối."),
                F("So sánh độ lớn ma sát lăn và ma sát trượt", "$F_{\\text{ms lăn}} \\ll F_{\\text{ms trượt}}$", "Thay trượt bằng lăn (dùng ổ bi, con lăn, bánh xe) giúp giảm mạnh lực ma sát có hại."),
            )
        ],
        example="Một người đẩy một chiếc tủ gỗ trên sàn nhà bằng lực nằm ngang $F_{\\text{đẩy}} = 80\\text{ N}$ nhưng chiếc tủ vẫn đứng yên không nhúc nhích. Khi đó lực ma sát nghỉ do sàn nhà tác dụng lên đáy tủ có độ lớn bằng bao nhiêu?",
        example_answer="Vì chiếc tủ vẫn đứng yên nên lực ma sát nghỉ cân bằng với lực đẩy nằm ngang của người đó: $F_{\\text{msn}} = F_{\\text{đẩy}} = 80\\text{ N}$ (hướng ngược chiều lực đẩy).",
        real_life="Lốp xe ô tô, xe máy và đế giày thể thao được xẻ rãnh sâu để tăng ma sát chống trơn trượt; trong khi trục bánh xe được lắp ổ bi và tra dầu mỡ để giảm ma sát.",
        quiz=[
            mcq("biet", "Khi đẩy một thùng hàng trượt trên mặt sàn nằm ngang, lực ma sát xuất hiện giữa đáy thùng và mặt sàn thuộc loại ma sát nào?", ["Ma sát trượt", "Ma sát nghỉ", "Ma sát lăn", "Lực hấp dẫn"], 0, "Đáy thùng trượt trên mặt sàn nên xuất hiện lực ma sát trượt."),
            mcq("biet", "Cách làm nào sau đây giúp **giảm** lực ma sát có hại trong các chi tiết máy?", ["Lắp ổ bi và tra dầu mỡ bôi trơn vào trục quay", "Tăng độ nhám của bề mặt tiếp xúc", "Khía nhiều rãnh sâu trên bề mặt trục", "Rắc cát khô vào giữa các bánh răng"], 0, "Ổ bi biến ma sát trượt thành ma sát lăn và dầu mỡ làm trơn bề mặt tiếp xúc giúp giảm ma sát."),
            mcq("hieu", "Vì sao tàu cao tốc, máy bay và cá heo đều có phần đầu thuôn nhọn?", ["Để giảm lực cản của không khí hoặc của nước khi chuyển động nhanh", "Để tăng lực ma sát trượt với môi trường", "Để làm tăng trọng lượng của vật", "Để không chịu tác dụng của trọng lực"], 0, "Hình dạng thuôn nhọn (khí động học) giúp dòng chất lưu trượt êm qua vật, làm giảm tối đa lực cản của không khí và nước."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về lực ma sát và lực cản:", [
                "Nhờ có lực ma sát nghỉ giữa đế giày và mặt đường mà con người có thể bước đi không bị trượt ngã.",
                "Khi bóp phanh xe đạp, lực ma sát trượt giữa má phanh và vành bánh xe giúp xe chậm lại và dừng hẳn.",
                "Lực cản của nước tác dụng lên người bơi luôn cùng chiều với chiều bơi của người đó.",
                "Vận động viên nhảy dù mở chiếc dù có diện tích lớn để tăng lực cản của không khí, giúp tiếp đất an toàn.",
            ], [True, True, False, True], "Ý c) sai vì lực cản của môi trường luôn ngược chiều với chiều chuyển động của vật."),
            short("vandung", "Kéo một khúc gỗ trên bàn nằm ngang bằng lực kéo $F_k = 12\\text{ N}$ nhưng khúc gỗ vẫn đứng yên. Độ lớn của lực ma sát nghỉ tác dụng lên khúc gỗ lúc này bằng bao nhiêu Newton ($\\text{N}$)?", ["12"], "Vì khúc gỗ vẫn đứng yên nên lực ma sát nghỉ cân bằng với lực kéo: $F_{\\text{msn}} = 12\\text{ N}$.", unit="N"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 11: Năng lượng và sự truyền năng lượng",
        icon="⚡",
        description="Các dạng năng lượng thường gặp (động năng, thế năng, nhiệt năng, điện năng, quang năng, hóa năng) và đơn vị Joule (J).",
        requirements=[
            "Nhận biết được mọi hoạt động và biến đổi trong tự nhiên đều cần năng lượng; đơn vị đo năng lượng trong hệ SI là Joule ($\\text{J}$).",
            "Phân loại được các dạng năng lượng theo nguồn phát hoặc theo tính chất: động năng, thế năng, nhiệt năng, điện năng, quang năng, hóa năng.",
            "Lấy được ví dụ về sự truyền năng lượng từ vật này sang vật khác thông qua tác dụng lực hoặc truyền nhiệt.",
        ],
        definition="Mọi quá trình biến đổi trong tự nhiên đều cần năng lượng. Đơn vị đo năng lượng trong hệ SI là Joule (kí hiệu $\\text{J}$), với $1\\text{ kJ} = 1000\\text{ J}$.",
        theory=(
            "### 1. Các dạng năng lượng\n"
            "- **Động năng**: năng lượng vật có được do đang chuyển động.\n"
            "- **Thế năng**: gồm thế năng hấp dẫn (vật ở độ cao so với mặt đất) và thế năng đàn hồi (lò xo, dây cao su bị biến dạng).\n"
            "- **Nhiệt năng**: năng lượng gắn với nhiệt độ của vật.\n"
            "- **Điện năng**: năng lượng của dòng điện cung cấp cho các thiết bị điện.\n"
            "- **Quang năng**: năng lượng ánh sáng (từ Mặt Trời, bóng đèn).\n"
            "- **Hóa năng**: năng lượng dự trữ trong lương thực, thực phẩm, nhiên liệu (xăng, dầu, than) và pin, ắc quy.\n\n"
            "### 2. Sự truyền năng lượng\n"
            "- Năng lượng có thể truyền từ vật này sang vật khác qua **tác dụng lực** (gió đẩy cánh quạt quay) hoặc qua **truyền nhiệt** (nước nóng truyền nhiệt cho cốc)."
        ),
        formulas=[
            G(
                "Đơn vị đo năng lượng",
                F("Quy đổi đơn vị Joule và kilôjoule", "$1\\text{ kJ} = 1000\\text{ J}; \\quad 1\\text{ MJ} = 1000\\text{ kJ} = 10^6\\text{ J}$", "Đơn vị Joule ($\\text{J}$) dùng chung cho mọi dạng năng lượng trong hệ SI."),
                F("Quy đổi đơn vị Calo trong dinh dưỡng", "$1\\text{ cal} \\approx 4{,}18\\text{ J}; \\quad 1\\text{ kcal} \\approx 4{,}18\\text{ kJ}$", "Thường ghi trên nhãn dinh dưỡng của thực phẩm."),
            )
        ],
        example="Một hộp sữa tươi cung cấp năng lượng dinh dưỡng là $250\\text{ kJ}$. Hãy đổi giá trị năng lượng này ra đơn vị Joule ($\\text{J}$).",
        example_answer="Ta có $1\\text{ kJ} = 1000\\text{ J}$, do đó năng lượng hộp sữa cung cấp là $E = 250 \\cdot 1000 = 250\\,000\\text{ J}$.",
        real_life="Cơ thể người lấy hóa năng từ thức ăn để duy trì thân nhiệt ($37^\\circ\\text{C}$) và thực hiện các hoạt động chạy nhảy, học tập hằng ngày.",
        quiz=[
            mcq("biet", "Đơn vị đo năng lượng trong hệ thống đo lường quốc tế SI là gì?", ["Joule ($\\text{J}$)", "Newton ($\\text{N}$)", "Mét ($\\text{m}$)", "Kilôgam ($\\text{kg}$)"], 0, "Đơn vị đo năng lượng trong hệ SI là Joule ($\\text{J}$)."),
            mcq("biet", "Năng lượng được tích trữ trong xăng dầu, than đá, pin và lương thực thực phẩm thuộc dạng năng lượng nào?", ["Hóa năng", "Động năng", "Thế năng hấp dẫn", "Năng lượng âm"], 0, "Năng lượng dự trữ trong các liên kết hóa học của nhiên liệu, thực phẩm và pin gọi là hóa năng."),
            mcq("hieu", "Một cánh cung đang được kéo căng chuẩn bị bắn mũi tên đi dự trữ dạng năng lượng chủ yếu nào?", ["Thế năng đàn hồi", "Nhiệt năng", "Quang năng", "Điện năng"], 0, "Cánh cung bị uốn cong (biến dạng đàn hồi) nên tích trữ thế năng đàn hồi."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về các dạng năng lượng:", [
                "Một chiếc ô tô đang chạy trên đường có động năng.",
                "Nước chứa trong hồ thủy điện trên núi cao có thế năng hấp dẫn.",
                "Đổi đơn vị: $3{,}5\\text{ kJ} = 350\\text{ J}$.",
                "Khi phơi quần áo dưới ánh nắng Mặt Trời, năng lượng nhiệt từ Mặt Trời đã truyền cho nước trong quần áo làm nước bay hơi nhanh hơn.",
            ], [True, True, False, True], "Ý c) sai vì $3{,}5\\text{ kJ} = 3{,}5 \\cdot 1000 = 3500\\text{ J}$."),
            short("vandung", "Một khẩu phần ăn sáng cung cấp $1{,}2\\text{ MJ}$ năng lượng. Biết $1\\text{ MJ} = 1000\\text{ kJ}$, hỏi khẩu phần ăn đó cung cấp bao nhiêu kilôjoule ($\\text{kJ}$)?", ["1200"], "Đổi $1{,}2\\text{ MJ} = 1{,}2 \\cdot 1000 = 1200\\text{ kJ}$.", unit="kJ"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 12: Bảo toàn năng lượng và sử dụng năng lượng tiết kiệm",
        icon="♻️",
        description="Định luật bảo toàn và chuyển hóa năng lượng, năng lượng có ích, năng lượng hao phí và biện pháp tiết kiệm năng lượng.",
        requirements=[
            "Phát biểu được định luật bảo toàn năng lượng: năng lượng không tự sinh ra hoặc tự mất đi mà chỉ truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác.",
            "Chỉ ra được phần năng lượng có ích và phần năng lượng hao phí (thường dưới dạng nhiệt năng) trong các thiết bị quen thuộc.",
            "Vận dụng được công thức bảo toàn năng lượng $W_{\\text{toàn phần}} = W_{\\text{ích}} + W_{\\text{hao phí}}$ và nêu các biện pháp tiết kiệm năng lượng.",
        ],
        definition="Theo định luật bảo toàn năng lượng, năng lượng không tự nhiên sinh ra cũng không tự nhiên mất đi; nó chỉ truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác.",
        theory=(
            "### 1. Sự chuyển hóa và bảo toàn năng lượng\n"
            "- Trong các dụng cụ tiêu thụ năng lượng, năng lượng ban đầu ($W_{\\text{tp}}$) luôn chuyển hóa thành **năng lượng có ích** ($W_{\\text{ích}}$) và **năng lượng hao phí** ($W_{\\text{hp}}$, thường tỏa ra dưới dạng nhiệt năng).\n"
            "- Ví dụ: Bóng đèn điện chuyển hóa **điện năng** thành **quang năng** (có ích) và **nhiệt năng** làm nóng bóng đèn (hao phí).\n\n"
            "### 2. Hiệu quả sử dụng và tiết kiệm năng lượng\n"
            "- Tổng năng lượng luôn được bảo toàn: $W_{\\text{tp}} = W_{\\text{ích}} + W_{\\text{hp}}$.\n"
            "- Sử dụng đèn LED thay đèn sợi đốt, tắt thiết bị điện khi không sử dụng, ưu tiên năng lượng tái tạo (mặt trời, gió) giúp giảm hao phí và bảo vệ môi trường."
        ),
        formulas=[
            G(
                "Định luật bảo toàn năng lượng",
                F("Phương trình bảo toàn năng lượng", "$W_{\\text{tp}} = W_{\\text{ích}} + W_{\\text{hp}}$", "Tổng năng lượng cung cấp bằng tổng năng lượng có ích và năng lượng hao phí."),
                F("Tỉ lệ phần trăm năng lượng có ích (Hiệu suất)", "$H = \\dfrac{W_{\\text{ích}}}{W_{\\text{tp}}} \\cdot 100\\%$", "Thiết bị tiết kiệm năng lượng là thiết bị có tỉ lệ $W_{\\text{ích}}$ cao và $W_{\\text{hp}}$ thấp."),
            )
        ],
        example="Một bóng đèn sợi đốt khi hoạt động nhận vào $100\\text{ J}$ điện năng, nhưng chỉ chuyển hóa được $10\\text{ J}$ thành quang năng (ánh sáng) có ích, phần còn lại tỏa nhiệt ra môi trường. Hãy tính phần năng lượng nhiệt hao phí $W_{\\text{hp}}$.",
        example_answer="Theo định luật bảo toàn năng lượng: $W_{\\text{hp}} = W_{\\text{tp}} - W_{\\text{ích}} = 100 - 10 = 90\\text{ J}$.",
        real_life="Bóng đèn LED chuyển hóa tới $80\\% - 90\\%$ điện năng thành ánh sáng, tiết kiệm điện gấp nhiều lần so với bóng đèn sợi đốt.",
        quiz=[
            mcq("biet", "Khi quạt điện đang hoạt động, phần năng lượng có ích mà quạt tạo ra là dạng năng lượng nào?", ["Động năng của cánh quạt và luồng gió", "Nhiệt năng làm nóng bầu quạt", "Năng lượng âm thanh phát ra từ trục quay", "Quang năng của đèn báo"], 0, "Mục đích của quạt điện là tạo ra gió mát, nên động năng của cánh quạt và không khí là năng lượng có ích."),
            mcq("biet", "Nội dung nào sau đây phát biểu đúng Định luật bảo toàn năng lượng?", ["Năng lượng không tự sinh ra hoặc tự mất đi mà chỉ truyền từ vật này sang vật khác hoặc chuyển hóa từ dạng này sang dạng khác", "Năng lượng luôn tự sinh ra thêm khi máy móc hoạt động", "Năng lượng có ích luôn lớn hơn năng lượng toàn phần cung cấp cho máy", "Năng lượng hao phí luôn bằng $0$ trong mọi động cơ"], 0, "Theo định luật bảo toàn năng lượng, tổng năng lượng luôn không đổi."),
            mcq("hieu", "Vì sao nên thay thế bóng đèn sợi đốt bằng bóng đèn LED trong gia đình?", ["Vì đèn LED biến đổi phần lớn điện năng thành quang năng và tỏa rất ít nhiệt năng hao phí", "Vì đèn sợi đốt không phát ra ánh sáng", "Vì đèn LED không cần dùng điện năng", "Vì đèn sợi đốt làm giảm nhiệt độ phòng"], 0, "Đèn sợi đốt hao phí tới $90\\%$ điện năng thành nhiệt, trong khi đèn LED có hiệu suất phát sáng rất cao."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về chuyển hóa và bảo toàn năng lượng:", [
                "Trong động cơ ô tô chạy xăng, hóa năng của xăng chuyển hóa thành động năng của xe và nhiệt năng hao phí.",
                "Năng lượng hao phí trong các thiết bị cơ – điện thường xuất hiện dưới dạng nhiệt năng do ma sát và tỏa nhiệt.",
                "Theo định luật bảo toàn năng lượng, ta có $W_{\\text{toàn phần}} = W_{\\text{ích}} + W_{\\text{hao phí}}$.",
                "Để tiết kiệm điện, khi sử dụng điều hòa nhiệt độ vào mùa hè nên mở toang tất cả cửa sổ.",
            ], [True, True, True, False], "Ý d) sai vì mở toang cửa sổ khi bật điều hòa làm thất thoát khí lạnh, gây lãng phí rất nhiều điện năng."),
            short("vandung", "Một động cơ điện nhận $500\\text{ J}$ điện năng, trong đó phần năng lượng cơ học có ích thu được là $420\\text{ J}$. Phần năng lượng hao phí tỏa nhiệt của động cơ bằng bao nhiêu Joule ($\\text{J}$)?", ["80"], "Ta có $W_{\\text{hp}} = W_{\\text{tp}} - W_{\\text{ích}} = 500 - 420 = 80\\text{ J}$.", unit="J"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 13: Chuyển động nhìn thấy của Mặt Trời. Mặt Trăng",
        icon="🌙",
        description="Giải thích hiện tượng Mặt Trời mọc đằng Đông lặn đằng Tây do sự tự quay của Trái Đất và các pha của Mặt Trăng.",
        requirements=[
            "Giải thích được chuyển động nhìn thấy của Mặt Trời hằng ngày từ Đông sang Tây là do Trái Đất tự quay quanh trục từ Tây sang Đông.",
            "Nêu được chu kì tự quay một vòng quanh trục của Trái Đất là khoảng $24\\text{ giờ}$ (1 ngày đêm).",
            "Giải thích được Mặt Trăng phản xạ ánh sáng Mặt Trời và phân biệt các hình dạng nhìn thấy (pha) của Mặt Trăng trong tháng âm lịch.",
        ],
        definition="Hiện tượng Mặt Trời mọc ở hướng Đông và lặn ở hướng Tây mỗi ngày là chuyển động nhìn thấy (biểu kiến), nguyên nhân thực sự là do Trái Đất tự quay quanh trục của nó theo chiều từ Tây sang Đông với chu kì $24\\text{ giờ}$.",
        theory=(
            "### 1. Chuyển động nhìn thấy của Mặt Trời\n"
            "- Trái Đất tự quay quanh trục từ **Tây sang Đông** hết một vòng trong $T \\approx 24\\text{ h}$.\n"
            "- Do đó, người đứng trên Trái Đất nhìn thấy Mặt Trời và các ngôi sao có vẻ như chuyển động ngược lại từ **Đông sang Tây**.\n"
            "- Tại mỗi thời điểm, ánh sáng Mặt Trời chỉ chiếu sáng được một nửa Trái Đất (ban ngày), nửa còn lại nằm trong bóng tối (ban đêm).\n\n"
            "### 2. Ánh sáng của Mặt Trăng và các pha Mặt Trăng\n"
            "- Mặt Trăng không tự phát sáng mà **phản xạ ánh sáng Mặt Trời** chiếu tới nó.\n"
            "- Khi Mặt Trăng quay quanh Trái Đất (chu kì tuần trăng khoảng $29{,}5\\text{ ngày}$), phần bề mặt được chiếu sáng hướng về Trái Đất thay đổi tạo nên các pha: **Không trăng (Sóc)**, **Trăng lưỡi liềm**, **Trăng bán nguyệt**, **Trăng tròn (Vọng – Rằm)**."
        ),
        formulas=[
            G(
                "Chu kì tự quay của Trái Đất và Tuần trăng",
                F("Chu kì tự quay của Trái Đất quanh trục", "$T_{\\text{Trái Đất}} \\approx 24\\text{ h}$", "Góc quay của Trái Đất trong $1\\text{ giờ}$ là $\\dfrac{360^\\circ}{24} = 15^\\circ$."),
                F("Chu kì tuần trăng (tháng âm lịch)", "$T_{\\text{tuần trăng}} \\approx 29{,}5\\text{ ngày}$", "Khoảng thời gian giữa hai lần Trăng tròn (ngày Rằm $15$ âm lịch) liên tiếp."),
            )
        ],
        example="Trái Đất tự quay một vòng ($360^\\circ$) quanh trục của nó hết $24\\text{ giờ}$. Hỏi trong $1\\text{ giờ}$, Trái Đất tự quay được một góc bằng bao nhiêu độ?",
        example_answer="Góc quay của Trái Đất trong $1\\text{ giờ}$ là $\\alpha = \\dfrac{360^\\circ}{24} = 15^\\circ$ (đây cũng là cơ sở chia Trái Đất thành $24$ múi giờ, mỗi múi giờ rộng $15^\\circ$ kinh tuyến).",
        real_life="Lịch âm (Nông lịch) được tính theo chu kì các pha của Mặt Trăng, trong đó ngày $1$ âm lịch là ngày Không trăng và ngày $15, 16$ âm lịch là ngày Trăng tròn.",
        quiz=[
            mcq("biet", "Nguyên nhân nào làm cho trên Trái Đất có hiện tượng ngày và đêm luân phiên nhau?", ["Do Trái Đất có dạng hình cầu và tự quay quanh trục từ Tây sang Đông", "Do Mặt Trời quay quanh Trái Đất một vòng mỗi ngày", "Do Mặt Trăng che khuất Mặt Trời vào mỗi buổi tối", "Do Mặt Trời tắt sáng vào ban đêm"], 0, "Trái Đất hình cầu nên Mặt Trời luôn chỉ chiếu sáng một nửa; nhờ Trái Đất tự quay quanh trục từ Tây sang Đông nên ngày và đêm luân phiên khắp nơi."),
            mcq("biet", "Vì sao vào ban đêm chúng ta nhìn thấy Mặt Trăng sáng?", ["Vì Mặt Trăng phản xạ ánh sáng từ Mặt Trời truyền tới mắt ta", "Vì Mặt Trăng là một ngôi sao tự phát sáng rực rỡ", "Vì Mặt Trăng phản xạ ánh sáng của các bóng đèn trên Trái Đất", "Vì trên Mặt Trăng có các đám cháy khổng lồ"], 0, "Mặt Trăng là vệ tinh tự nhiên không tự phát sáng, ta nhìn thấy nó vì nó phản xạ ánh sáng Mặt Trời."),
            mcq("hieu", "Ta thấy Trăng tròn (Vọng) vào giữa tháng âm lịch khi vị trí tương đối giữa Mặt Trời, Trái Đất và Mặt Trăng như thế nào?", ["Trái Đất nằm ở khoảng giữa Mặt Trời và Mặt Trăng (toàn bộ nửa được chiếu sáng của Mặt Trăng hướng về Trái Đất)", "Mặt Trăng nằm chính giữa Mặt Trời và Trái Đất", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Mặt Trăng tạo với Mặt Trời một góc vuông tại Trái Đất"], 0, "Khi Trái Đất nằm ở khoảng giữa Mặt Trời và Mặt Trăng, toàn bộ nửa bề mặt được chiếu sáng của Mặt Trăng quay về phía Trái Đất nên ta thấy Trăng tròn."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về chuyển động nhìn thấy của Mặt Trời và Mặt Trăng:", [
                "Trái Đất tự quay quanh trục theo chiều từ Tây sang Đông nên ta thấy Mặt Trời mọc ở hướng Đông, lặn ở hướng Tây.",
                "Một chu kì tự quay quanh trục của Trái Đất kéo dài khoảng $24\\text{ giờ}$.",
                "Mặt Trăng tự phát ra ánh sáng trắng giống như Mặt Trời.",
                "Vào ngày mồng $1$ âm lịch (Không trăng), nửa bề mặt không được Mặt Trời chiếu sáng của Mặt Trăng hướng về phía Trái Đất.",
            ], [True, True, False, True], "Ý c) sai vì Mặt Trăng không tự phát sáng mà chỉ phản xạ ánh sáng Mặt Trời."),
            short("vandung", "Biết Trái Đất tự quay một vòng ($360^\\circ$) hết $24\\text{ giờ}$. Hỏi trong $2\\text{ giờ}$, Trái Đất quay quanh trục được một góc bao nhiêu độ?", ["30"], "Trong $1\\text{ giờ}$ Trái Đất quay được $\\dfrac{360^\\circ}{24} = 15^\\circ$, nên trong $2\\text{ giờ}$ quay được $2 \\cdot 15^\\circ = 30^\\circ$.", unit="độ"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 14: Hệ Mặt Trời và Ngân Hà",
        icon="🪐",
        description="Cấu trúc Hệ Mặt Trời với 8 hành tinh theo thứ tự từ trong ra ngoài, phân biệt sao – hành tinh – vệ tinh và Ngân Hà.",
        requirements=[
            "Phân biệt được Sao (thiên thể tự phát sáng như Mặt Trời), Hành tinh (quay quanh sao, phản xạ ánh sáng) và Vệ tinh (quay quanh hành tinh).",
            "Kể tên đúng thứ tự 8 hành tinh trong Hệ Mặt Trời tính từ Mặt Trời ra ngoài: Thủy tinh, Kim tinh, Trái Đất, Hỏa tinh, Mộc tinh, Thổ tinh, Thiên Vương tinh, Hải Vương tinh.",
            "Nêu được Hệ Mặt Trời chỉ là một phần nhỏ nằm ở rìa của Ngân Hà (Milky Way).",
        ],
        definition="Hệ Mặt Trời (Thái Dương hệ) có Mặt Trời ở tâm và 8 hành tinh chuyển động xung quanh theo quỹ đạo gần tròn cùng chiều. Hệ Mặt Trời là một phần nhỏ của Ngân Hà — một tập hợp hàng trăm tỉ ngôi sao.",
        theory=(
            "### 1. Cấu trúc Hệ Mặt Trời\n"
            "- **Mặt Trời** là ngôi sao ở trung tâm, chiếm phần lớn khối lượng của hệ và tự phát ra ánh sáng.\n"
            "- **8 hành tinh** theo thứ tự khoảng cách tăng dần từ Mặt Trời:\n"
            "  1. **Thủy tinh** (gần Mặt Trời nhất) – 2. **Kim tinh** – 3. **Trái Đất** – 4. **Hỏa tinh** ($4$ hành tinh đất đá vòng trong).\n"
            "  5. **Mộc tinh** (lớn nhất) – 6. **Thổ tinh** (có vành đai nổi bật) – 7. **Thiên Vương tinh** – 8. **Hải Vương tinh** ($4$ hành tinh khí khổng lồ vòng ngoài).\n\n"
            "### 2. Ngân Hà\n"
            "- **Ngân Hà** (Milky Way) là một thiên hà xoắn ốc chứa hàng trăm tỉ ngôi sao, trong đó Hệ Mặt Trời nằm ở một nhánh xoắn ốc phía rìa Ngân Hà.\n"
            "- Khoảng cách trong vũ trụ thường đo bằng **đơn vị thiên văn** ($1\\text{ AU} \\approx 150\\text{ triệu km}$, khoảng cách trung bình từ Trái Đất đến Mặt Trời) hoặc **năm ánh sáng**."
        ),
        formulas=[
            G(
                "Các con số đặc trưng của Hệ Mặt Trời",
                F("Số hành tinh trong Hệ Mặt Trời", "$N = 8\\text{ hành tinh}$", "Thủy – Kim – Địa (Trái Đất) – Hỏa – Mộc – Thổ – Thiên Vương – Hải Vương."),
                F("Đơn vị thiên văn (AU) và Chu kì Trái Đất quay quanh Mặt Trời", "$1\\text{ AU} \\approx 1{,}5 \\cdot 10^8\\text{ km}; \\quad T_{\\text{Trái Đất}} \\approx 365{,}25\\text{ ngày}$", "Hành tinh càng ở xa Mặt Trời thì chu kì quay một vòng quanh Mặt Trời càng dài."),
            )
        ],
        example="Trong 8 hành tinh của Hệ Mặt Trời, Trái Đất nằm ở vị trí thứ mấy tính từ Mặt Trời ra ngoài và nằm giữa hai hành tinh nào?",
        example_answer="Tính từ Mặt Trời ra ngoài (Thủy tinh $\\rightarrow$ Kim tinh $\\rightarrow$ Trái Đất $\\rightarrow$ Hỏa tinh...), Trái Đất đứng ở vị trí thứ $3$ và nằm giữa Kim tinh và Hỏa tinh.",
        real_life="Vào những đêm trời quang không trăng ở vùng quê, ta có thể nhìn thấy một dải sáng mờ vắt ngang bầu trời gồm vô số ngôi sao — đó chính là dải Ngân Hà nhìn từ Trái Đất.",
        quiz=[
            mcq("biet", "Hệ Mặt Trời có tất cả bao nhiêu hành tinh chính thức quay xung quanh Mặt Trời?", ["$8$ hành tinh", "$6$ hành tinh", "$9$ hành tinh", "$12$ hành tinh"], 0, "Hệ Mặt Trời gồm $8$ hành tinh: Thủy, Kim, Trái Đất, Hỏa, Mộc, Thổ, Thiên Vương, Hải Vương."),
            mcq("biet", "Tính từ Mặt Trời ra ngoài, Trái Đất là hành tinh đứng ở vị trí thứ mấy?", ["Thứ $3$", "Thứ $1$", "Thứ $4$", "Thứ $5$"], 0, "Thứ tự từ Mặt Trời ra: (1) Thủy tinh, (2) Kim tinh, (3) Trái Đất."),
            mcq("hieu", "Điểm khác biệt cơ bản giữa một ngôi sao (như Mặt Trời) và một hành tinh (như Trái Đất, Mộc tinh) là gì?", ["Ngôi sao tự phát ra ánh sáng, còn hành tinh không tự phát sáng mà phản xạ ánh sáng của sao", "Hành tinh luôn lớn hơn ngôi sao", "Hành tinh tự phát sáng còn ngôi sao không phát sáng", "Ngôi sao quay xung quanh các hành tinh"], 0, "Sao là thiên thể nóng sáng tự phát ra ánh sáng, còn hành tinh quay quanh sao và phản xạ ánh sáng từ sao."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về Hệ Mặt Trời và Ngân Hà:", [
                "Thủy tinh là hành tinh ở gần Mặt Trời nhất và Hải Vương tinh là hành tinh ở xa Mặt Trời nhất.",
                "Mộc tinh là hành tinh có kích thước lớn nhất trong Hệ Mặt Trời.",
                "Hành tinh càng ở xa Mặt Trời thì thời gian quay hết một vòng quanh Mặt Trời càng ngắn.",
                "Hệ Mặt Trời chỉ là một hệ sao nhỏ nằm trong thiên hà Ngân Hà.",
            ], [True, True, False, True], "Ý c) sai vì hành tinh càng ở xa Mặt Trời thì chu kì quay quanh Mặt Trời càng dài (ví dụ Thủy tinh chỉ mất $88$ ngày còn Hải Vương tinh mất tới $165$ năm)."),
            short("vandung", "Trong Hệ Mặt Trời có tất cả bao nhiêu hành tinh?", ["8"], "Hệ Mặt Trời có $8$ hành tinh quay xung quanh Mặt Trời."),
        ],
        chapter_desc=CH3_DESC,
    ),
]
