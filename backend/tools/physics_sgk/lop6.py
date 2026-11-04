"""KHOA HỌC TỰ NHIÊN 6 (PHẦN VẬT LÍ) — Kết nối tri thức với cuộc sống.

Bao phủ đầy đủ các bài học Vật lí trong SGK KHTN 6 KNTT (Chương I: Mở đầu về KHTN; Chương VIII: Lực trong đời sống; Chương IX: Năng lượng) và mở rộng khái niệm tốc độ cơ bản, chia thành 7 chủ đề tương thích hệ thống game thực nghiệm.
Mỗi chủ đề: Yêu cầu cần đạt (CT GDPT 2018), lý thuyết theo từng bài, công thức,
ví dụ, ứng dụng và 10 câu hỏi: Biết 4 TN | Hiểu 2 TN + 2 Đúng/Sai (4 ý a–d) | Vận dụng 1 TN + 1 trả lời ngắn.
"""
from ._helpers import F, G, mcq, short, tf4

GRADE = 6

LESSONS = [
    {
        "topic": "do-dai",
        "title": "Mở đầu về Khoa học tự nhiên và Đo chiều dài",
        "icon": "📏",
        "description": "Chương I · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 6–21): Bài 1 – Bài 5. Giới thiệu về Khoa học tự nhiên, quy tắc an toàn trong phòng thực hành, sử dụng kính lúp và kính hiển vi quang học; đơn vị và dụng cụ đo chiều dài, giới hạn đo (GHĐ), độ chia nhỏ nhất (ĐCNN) và quy tắc đo chiều dài.",
        "requirements": [
            r"Nêu được khái niệm Khoa học tự nhiên và trình bày được vai trò của Khoa học tự nhiên trong cuộc sống.",
            r"Phân biệt được các lĩnh vực chủ yếu của Khoa học tự nhiên (Vật lí học, Hoá học, Sinh học, Khoa học Trái Đất, Thiên văn học) dựa vào đối tượng nghiên cứu.",
            r"Nêu được các quy định an toàn trong phòng thực hành và phân biệt được các kí hiệu cảnh báo nguy hiểm thường gặp.",
            r"Trình bày được cách sử dụng kính lúp và kính hiển vi quang học để quan sát các vật nhỏ.",
            r"Lấy được ví dụ chứng tỏ giác quan của chúng ta có thể cảm nhận sai một số hiện tượng và nêu được cách đo, đơn vị đo và dụng cụ thường dùng để đo chiều dài của một vật.",
            r"Xác định được giới hạn đo (GHĐ) và độ chia nhỏ nhất (ĐCNN) của thước đo; thực hiện đúng quy tắc ước lượng, chọn thước, đặt thước, đặt mắt và đọc kết quả đo chiều dài.",
        ],
        "definition": (
            r"- **Khoa học tự nhiên** là ngành khoa học nghiên cứu về các sự vật, hiện tượng, quy luật tự nhiên và những ảnh hưởng của chúng đến cuộc sống con người và môi trường." "\n"
            r"- **Đo chiều dài** của một vật là so sánh chiều dài của vật đó với một chiều dài được chọn làm **đơn vị đo**." "\n"
            r"- Đơn vị đo chiều dài trong hệ thống đo lường hợp pháp của nước ta (và hệ SI) là **mét**, kí hiệu là $\text{m}$." "\n"
            r"- **Giới hạn đo (GHĐ)** của thước là chiều dài lớn nhất ghi trên thước. **Độ chia nhỏ nhất (ĐCNN)** của thước là chiều dài giữa hai vạch chia liên tiếp trên thước."
        ),
        "theory": (
            r"### Bài 1. Giới thiệu về Khoa học tự nhiên" "\n"
            r"- Khoa học tự nhiên bao gồm 5 lĩnh vực chính: **Vật lí học** (nghiên cứu vật chất, quy luật vận động, lực, năng lượng), **Hoá học** (nghiên cứu chất và sự biến đổi của chúng), **Sinh học** (nghiên cứu các vật sống), **Khoa học Trái Đất** (nghiên cứu Trái Đất và bầu khí quyển) và **Thiên văn học** (nghiên cứu các thiên thể và vũ trụ)." "\n"
            r"- Phân biệt **vật sống** (có khả năng trao đổi chất, lớn lên, sinh sản, cảm ứng) và **vật không sống** (không có các đặc điểm trên)." "\n"
            r"### Bài 2. An toàn trong phòng thực hành" "\n"
            r"- Tuân thủ nghiêm ngặt nội quy phòng thực hành: mặc trang phục gọn gàng, đeo kính bảo hộ, khẩu trang, găng tay khi làm thí nghiệm với hoá chất hoặc nhiệt; không ăn uống, đùa nghịch trong phòng thực hành." "\n"
            r"- Nhận biết các biển báo: chất dễ cháy, chất ăn mòn, chất độc sinh học, nguy hiểm về điện, dụng cụ sắc nhọn, thuỷ tinh dễ vỡ." "\n"
            r"### Bài 3. Sử dụng kính lúp" "\n"
            r"- **Kính lúp** dùng để quan sát các vật nhỏ mà mắt thường khó nhìn rõ chi tiết (có độ bội giác từ $3\times$ đến $20\times$). Cấu tạo gồm mặt kính hội tụ, khung kính và tay cầm." "\n"
            r"- Cách dùng: đặt kính lúp gần sát vật mẫu, mắt nhìn vào mặt kính rồi từ từ dịch chuyển kính ra xa vật cho đến khi nhìn thấy ảnh của vật rõ nét nhất." "\n"
            r"### Bài 4. Sử dụng kính hiển vi quang học" "\n"
            r"- **Kính hiển vi quang học** có độ phóng đại lớn (từ $40\times$ đến $1000\times$ hoặc hơn), dùng quan sát các vật rất nhỏ như tế bào, vi khuẩn. Độ phóng đại của kính hiển vi bằng tích độ phóng đại của thị kính và vật kính: $G = G_{\text{thị kính}} \cdot G_{\text{vật kính}}$." "\n"
            r"### Bài 5. Đo chiều dài" "\n"
            r"- **Ước lượng và chọn thước**: Trước khi đo cần ước lượng chiều dài vật để chọn thước (thước kẻ, thước cuộn, thước dây, thước kẹp) có GHĐ lớn hơn hoặc bằng chiều dài vật và có ĐCNN phù hợp để đo một lần chính xác." "\n"
            r"- **Quy tắc 5 bước đo chiều dài**: (1) Ước lượng chiều dài cần đo; (2) Chọn thước có GHĐ và ĐCNN phù hợp; (3) Đặt thước dọc theo chiều dài cần đo, vạch số $0$ ngang với một đầu của vật; (4) Đặt mắt nhìn theo hướng **vuông góc** với cạnh thước tại đầu kia của vật; (5) Đọc và ghi kết quả đo theo vạch chia **gần nhất** với đầu kia của vật (kết quả ghi phải là bội số của ĐCNN)."
        ),
        "formulas": [
            G(
                "I. Quy đổi đơn vị đo chiều dài",
                F("Bội số của mét", r"$1\text{ km} = 1000\text{ m} = 10^3\text{ m}$", r"Ki-lô-mét dùng đo quãng đường dài."),
                F("Ước số thông dụng của mét", r"$1\text{ m} = 10\text{ dm} = 100\text{ cm} = 1000\text{ mm}$", r"Mỗi đơn vị liền kề hơn kém nhau $10$ lần."),
                F("Đơn vị hiển vi và hàng hải", r"$1\text{ }\mu\text{m} = 10^{-6}\text{ m}; \quad 1\text{ nm} = 10^{-9}\text{ m}; \quad 1\text{ inch} \approx 2{,}54\text{ cm}$", r"Dùng trong kính hiển vi và kích thước màn hình."),
            ),
            G(
                "II. Độ chia nhỏ nhất & Kính hiển vi",
                F("Công thức tính ĐCNN", r"$\text{ĐCNN} = \dfrac{L_2 - L_1}{n}$", r"$L_1, L_2$ là hai số ghi liên tiếp trên thước; $n$ là số khoảng chia giữa chúng."),
                F("Giá trị thực khi vạch đầu khác 0", r"$l = x_2 - x_1$", r"Khi đầu vật đặt tại vạch $x_1$ và đầu kia trùng vạch $x_2$."),
                F("Độ phóng đại kính hiển vi", r"$G = G_{\text{thị kính}} \cdot G_{\text{vật kính}}$", r"Ví dụ thị kính $10\times$ và vật kính $40\times$ cho $G = 400\times$."),
            ),
        ],
        "example": (
            r"Trên một chiếc thước kẻ học sinh có vạch lớn nhất ghi số $20$ (đơn vị $\text{cm}$). Giữa vạch số $0$ và vạch số $1\text{ cm}$ được chia làm $10$ khoảng đều nhau. Hãy xác định giới hạn đo (GHĐ), độ chia nhỏ nhất (ĐCNN) của thước và tính chiều dài chiếc bút chì nếu một đầu bút đặt ở vạch $1\text{ cm}$ còn đầu kia ngang với vạch $15{,}4\text{ cm}$."
        ),
        "example_answer": (
            r"- **Giới hạn đo (GHĐ)** của thước là chiều dài lớn nhất ghi trên thước: $\text{GHĐ} = 20\text{ cm}$." "\n"
            r"- **Độ chia nhỏ nhất (ĐCNN)** của thước là: $\text{ĐCNN} = \dfrac{1 - 0}{10} = 0{,}1\text{ cm} = 1\text{ mm}$." "\n"
            r"- **Chiều dài chiếc bút chì** là: $l = x_2 - x_1 = 15{,}4 - 1 = 14{,}4\text{ cm}$."
        ),
        "real_life": (
            r"- Thợ may sử dụng **thước dây** mềm để đo số đo cơ thể; thợ mộc và thợ xây dùng **thước cuộn** kim loại để đo kích thước bàn ghế, phòng ốc; thợ cơ khí dùng **thước kẹp** để đo đường kính trục máy với độ chính xác đến $0{,}02\text{ mm}$." "\n"
            r"- Kính hiển vi quang học giúp bác sĩ xét nghiệm máu, quan sát vi khuẩn và tế bào trong y học."
        ),
        "game_title": "Thử thách Đo chiều dài chính xác",
        "game_description": "Lựa chọn thước đo có giới hạn đo và độ chia nhỏ nhất phù hợp, đặt thước và mắt nhìn đúng quy tắc để đọc chính xác chiều dài các vật thể trong phòng thực hành.",
        "game_type": "game_dodai",
        "quiz": [
            mcq(
                "biet",
                r"Đơn vị đo chiều dài hợp pháp trong hệ thống đo lường chính thức của nước ta (hệ SI) là:",
                [r"Mét ($\text{m}$).", r"Xăng-ti-mét ($\text{cm}$).", r"Ki-lô-mét ($\text{km}$).", r"Mi-li-mét ($\text{mm}$)."],
                0,
                r"Đơn vị đo chiều dài cơ bản trong hệ SI và hệ thống đo lường hợp pháp của Việt Nam là **mét** ($\text{m}$).",
            ),
            mcq(
                "biet",
                r"Độ chia nhỏ nhất (ĐCNN) của thước là:",
                [
                    r"Chiều dài giữa hai vạch chia liên tiếp trên thước.",
                    r"Chiều dài lớn nhất được ghi trên thước.",
                    r"Con số nhỏ nhất được in trên mặt thước.",
                    r"Tổng số vạch chia có trên toàn bộ chiếc thước.",
                ],
                0,
                r"Theo định nghĩa, **độ chia nhỏ nhất (ĐCNN)** của thước là chiều dài giữa hai vạch chia liên tiếp trên thước.",
            ),
            mcq(
                "biet",
                r"Đối tượng nào sau đây thuộc lĩnh vực nghiên cứu của **Vật lí học** trong môn Khoa học tự nhiên?",
                [
                    r"Quy luật chuyển động của các vật, tác dụng của lực và sự chuyển hoá năng lượng.",
                    r"Quá trình quang hợp và hô hấp của tế bào thực vật.",
                    r"Sự sinh sản và phát triển của vi khuẩn trong sữa chua.",
                    r"Cấu tạo của tế bào biểu bì vảy hành dưới kính hiển vi.",
                ],
                0,
                r"Vật lí học nghiên cứu về vật chất, quy luật vận động, lực, năng lượng và sự biến đổi năng lượng.",
            ),
            mcq(
                "biet",
                r"Khi sử dụng thước để đo chiều dài của một vật, ta cần đặt mắt nhìn như thế nào để đọc kết quả chính xác?",
                [
                    r"Nhìn theo hướng vuông góc với cạnh thước tại đầu của vật.",
                    r"Nhìn xiên từ bên trái sang đầu của vật.",
                    r"Nhìn xiên từ bên phải sang đầu của vật.",
                    r"Nhìn dọc theo chiều dài của chiếc thước từ vạch số $0$.",
                ],
                0,
                r"Để tránh sai số thị sai khi đọc kết quả, mắt phải đặt nhìn theo hướng **vuông góc** với cạnh thước tại đầu kia của vật.",
            ),
            mcq(
                "hieu",
                r"Trên một thước thẳng có ghi vạch lớn nhất là $30\text{ cm}$. Giữa hai vạch ghi số $2\text{ cm}$ và $3\text{ cm}$ có $5$ khoảng chia bằng nhau. Giới hạn đo (GHĐ) và độ chia nhỏ nhất (ĐCNN) của thước này lần lượt là:",
                [
                    r"$\text{GHĐ} = 30\text{ cm}$ và $\text{ĐCNN} = 0{,}2\text{ cm}$.",
                    r"$\text{GHĐ} = 30\text{ cm}$ và $\text{ĐCNN} = 0{,}5\text{ cm}$.",
                    r"$\text{GHĐ} = 30\text{ cm}$ và $\text{ĐCNN} = 0{,}1\text{ cm}$.",
                    r"$\text{GHĐ} = 1\text{ cm}$ và $\text{ĐCNN} = 0{,}2\text{ cm}$.",
                ],
                0,
                r"Chiều dài lớn nhất ghi trên thước là $\text{GHĐ} = 30\text{ cm}$. Giữa vạch $2\text{ cm}$ và $3\text{ cm}$ có $5$ khoảng chia nên $\text{ĐCNN} = \dfrac{3 - 2}{5} = 0{,}2\text{ cm} = 2\text{ mm}$.",
            ),
            mcq(
                "hieu",
                r"Một học sinh dùng thước có $\text{ĐCNN} = 0{,}5\text{ cm}$ để đo chiều dài bàn học. Cách ghi kết quả đo nào sau đây là **đúng quy tắc**?",
                [
                    r"$115{,}5\text{ cm}$.",
                    r"$115{,}2\text{ cm}$.",
                    r"$115{,}3\text{ cm}$.",
                    r"$115{,}75\text{ cm}$.",
                ],
                0,
                r"Kết quả đọc và ghi từ thước phải là bội số nguyên của ĐCNN ($0{,}5\text{ cm}$), nên phần thập phân chỉ có thể là ${,0}$ hoặc ${,5}$. Vậy $115{,}5\text{ cm}$ là kết quả đúng quy tắc.",
            ),
            tf4(
                "hieu",
                r"Một bạn học sinh chuẩn bị thực hành đo chiều dài quyển sách Khoa học tự nhiên $6$ (dài khoảng $26{,}5\text{ cm}$) và quan sát mẫu vật trong phòng thực hành. Xét tính đúng sai của các phát biểu sau:",
                [
                    r"a) Để đo chiều dài quyển sách chỉ bằng một lần đo, bạn nên chọn thước kẻ có $\text{GHĐ} = 30\text{ cm}$ và $\text{ĐCNN} = 1\text{ mm}$ thay vì thước có $\text{GHĐ} = 20\text{ cm}$.",
                    r"b) Khi đặt thước đo, bắt buộc phải đặt thước lệch một góc $30^\circ$ so với mép quyển sách để dễ nhìn vạch chia hơn.",
                    r"c) Nếu sử dụng kính hiển vi quang học có thị kính ghi $10\times$ và vật kính ghi $40\times$ thì độ phóng đại của ảnh quan sát được là $400$ lần.",
                    r"d) Khi không may làm vỡ ống nghiệm thuỷ tinh trong phòng thực hành, học sinh nên dùng tay trần nhặt ngay các mảnh vỡ bỏ vào túi áo.",
                ],
                [True, False, True, False],
                r"a) Đúng vì quyển sách dài khoảng $26{,}5\text{ cm} > 20\text{ cm}$ nên cần chọn thước có $\text{GHĐ} = 30\text{ cm}$ để đo một lần chính xác." "\n"
                r"b) Sai vì thước phải được đặt **dọc theo** chiều dài cần đo chứ không được đặt lệch góc." "\n"
                r"c) Đúng vì độ phóng đại $G = 10 \cdot 40 = 400$ lần." "\n"
                r"d) Sai vì không được dùng tay trần nhặt mảnh thuỷ tinh vỡ mà phải báo ngay cho giáo viên và dùng chổi, hốt rác chuyên dụng để thu gom an toàn.",
            ),
            tf4(
                "hieu",
                r"Xét các phép đổi đơn vị đo chiều dài và cách đọc kết quả đo. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) $2{,}5\text{ m} = 250\text{ cm} = 2500\text{ mm}$.",
                    r"b) $45\text{ mm} = 0{,}45\text{ m}$.",
                    r"c) Nếu một đầu chiếc đinh vít đặt ngang vạch $2{,}0\text{ cm}$ và đầu kia ngang vạch $6{,}8\text{ cm}$ thì chiều dài chiếc đinh vít là $4{,}8\text{ cm}$.",
                    r"d) Giác quan của con người luôn luôn cảm nhận chính xác tuyệt đối kích thước của mọi vật nên không cần dùng dụng cụ đo.",
                ],
                [True, False, True, False],
                r"a) Đúng vì $2{,}5\text{ m} = 2{,}5 \cdot 100\text{ cm} = 250\text{ cm} = 2500\text{ mm}$." "\n"
                r"b) Sai vì $45\text{ mm} = \dfrac{45}{1000}\text{ m} = 0{,}045\text{ m}$." "\n"
                r"c) Đúng vì chiều dài chiếc đinh vít là $l = 6{,}8 - 2{,}0 = 4{,}8\text{ cm}$." "\n"
                r"d) Sai vì giác quan có thể bị đánh lừa bởi ảo giác thị giác, nên muốn biết chính xác phải dùng dụng cụ đo.",
            ),
            mcq(
                "vandung",
                r"Để đo độ dày của một trang giấy trong sách giáo khoa Khoa học tự nhiên $6$ bằng thước kẻ có $\text{ĐCNN} = 1\text{ mm}$, một học sinh ép chặt $200$ trang giấy (tức $100$ tờ giấy, không tính bìa) và đo được bề dày tổng cộng là $1{,}0\text{ cm}$. Bề dày trung bình của **một tờ giấy** là:",
                [
                    r"$0{,}1\text{ mm}$.",
                    r"$0{,}05\text{ mm}$.",
                    r"$1{,}0\text{ mm}$.",
                    r"$0{,}2\text{ mm}$.",
                ],
                0,
                r"Đổi $1{,}0\text{ cm} = 10\text{ mm}$. Vì $200$ trang giấy ứng với $100$ tờ giấy nên bề dày trung bình của một tờ giấy là $d = \dfrac{10\text{ mm}}{100} = 0{,}1\text{ mm}$.",
            ),
            short(
                "vandung",
                r"Một bạn dùng đoạn dây không dãn quấn sát nhau $25$ vòng quanh một chiếc bút bi hình trụ tròn. Khi trải thẳng phần dây quấn đó ra và đo bằng thước thì được chiều dài $50\text{ cm}$. Chu vi tiết diện ngang của chiếc bút bi đó bằng bao nhiêu xăng-ti-mét?",
                ["2", "2,0", "2.0"],
                r"Chiều dài của $25$ vòng dây quấn sát nhau bằng $25$ lần chu vi $C$ của chiếc bút bi. Do đó chu vi của bút bi là $C = \dfrac{50}{25} = 2\text{ cm}$.",
            ),
        ],
    },
    {
        "topic": "khoi-luong",
        "title": "Đo khối lượng và Đo thời gian",
        "icon": "⚖️",
        "description": "Chương I · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 22–28): Bài 6 – Bài 7. Đơn vị và dụng cụ đo khối lượng, cách hiệu chỉnh và sử dụng cân Roberval, cân đồng hồ; đơn vị và dụng cụ đo thời gian, cách sử dụng đồng hồ bấm giây để đo thời gian một sự kiện.",
        "requirements": [
            r"Nêu được khối lượng là số đo lượng chất của một vật; nêu được đơn vị đo khối lượng trong hệ thống đo lường chính thức của nước ta là ki-lô-gam ($\text{kg}$) và các ước số, bội số thường dùng.",
            r"Nhận biết được một số loại cân thông dụng (cân Roberval, cân đồng hồ, cân điện tử, cân y tế, cân đòn) và xác định được GHĐ, ĐCNN của cân.",
            r"Thực hiện được các bước đo khối lượng của một vật bằng cân đồng hồ và cân Roberval đúng quy tắc.",
            r"Nêu được đơn vị đo thời gian trong hệ SI là giây ($\text{s}$) và các đơn vị thường dùng khác (phút, giờ, ngày).",
            r"Lựa chọn được đồng hồ phù hợp và thực hiện đúng quy tắc đo thời gian của một hoạt động bằng đồng hồ bấm giây.",
        ],
        "definition": (
            r"- **Khối lượng** của một vật chỉ lượng chất tạo nên vật đó (kí hiệu là $m$). Đơn vị đo khối lượng cơ bản trong hệ SI là **ki-lô-gam** ($\text{kg}$)." "\n"
            r"- **Thời gian** là đại lượng dùng để xác định trình tự xảy ra các sự kiện và khoảng kéo dài của một hiện tượng (kí hiệu là $t$). Đơn vị đo thời gian cơ bản trong hệ SI là **giây** ($\text{s}$)." "\n"
            r"- Trước khi đo khối lượng bằng cân hoặc đo thời gian bằng đồng hồ bấm giây, luôn phải **hiệu chỉnh dụng cụ về vạch số $0$**."
        ),
        "theory": (
            r"### Bài 6. Đo khối lượng" "\n"
            r"- **Đơn vị đo khối lượng**: Ngoài $\text{kg}$, ta thường dùng tấn ($\text{t}$), tạ, yến, héc-tô-gam ($\text{hg}$, còn gọi là lạng), gam ($\text{g}$), mi-li-gam ($\text{mg}$)." "\n"
            r"- **Quy tắc 5 bước đo khối lượng bằng cân đồng hồ**: (1) Ước lượng khối lượng vật cần đo; (2) Chọn cân có GHĐ và ĐCNN phù hợp; (3) Hiệu chỉnh cân trước khi đo sao cho kim cân chỉ đúng vạch số $0$ (vặn ốc điều chỉnh); (4) Đặt vật lên đĩa cân và đặt mắt nhìn theo hướng **vuông góc** với mặt cân tại đầu kim cân; (5) Đọc và ghi kết quả đo theo vạch chia gần nhất với đầu kim cân." "\n"
            r"- **Cách dùng cân Roberval**: Hiệu chỉnh đòn cân nằm thăng bằng (kim cân chỉ đúng vạch giữa), đặt vật đem cân lên một đĩa cân, dùng kẹp gắp các quả cân đặt lên đĩa cân bên kia (và dịch chuyển con mã nếu có) cho đến khi đòn cân nằm ngang thăng bằng trở lại. Khối lượng vật bằng tổng khối lượng các quả cân trên đĩa cộng với số chỉ của con mã." "\n"
            r"### Bài 7. Đo thời gian" "\n"
            r"- **Dụng cụ đo thời gian**: Đồng hồ treo tường, đồng hồ đeo tay, đồng hồ quả lắc, đồng hồ cát, đồng hồ bấm giây cơ học hoặc điện tử." "\n"
            r"- **Quy tắc 5 bước đo thời gian bằng đồng hồ bấm giây**: (1) Ước lượng khoảng thời gian cần đo; (2) Chọn đồng hồ có GHĐ và ĐCNN phù hợp; (3) Hiệu chỉnh đồng hồ về vạch số $0$ trước khi đo (nhấn nút `RESET`); (4) Nhấn nút `START` khi sự kiện bắt đầu và nhấn nút `STOP` đúng lúc sự kiện kết thúc; (5) Đặt mắt vuông góc với mặt đồng hồ (nếu là đồng hồ kim) để đọc và ghi kết quả theo vạch chia gần nhất."
        ),
        "formulas": [
            G(
                "I. Quy đổi đơn vị khối lượng",
                F("Các đơn vị lớn hơn ki-lô-gam", r"$1\text{ tấn} = 10\text{ tạ} = 100\text{ yến} = 1000\text{ kg}$"),
                F("Các đơn vị nhỏ hơn ki-lô-gam", r"$1\text{ kg} = 10\text{ hg (lạng)} = 1000\text{ g}; \quad 1\text{ g} = 1000\text{ mg}$"),
                F("Khối lượng trên cân Roberval", r"$m_{\text{vật}} = \sum m_{\text{quả cân}} + m_{\text{con mã}}$", r"Khi đòn cân nằm ngang thăng bằng."),
            ),
            G(
                "II. Quy đổi đơn vị thời gian",
                F("Giờ, phút, giây", r"$1\text{ h} = 60\text{ phút} = 3600\text{ s}; \quad 1\text{ phút} = 60\text{ s}$"),
                F("Ngày và mi-li-giây", r"$1\text{ ngày đêm} = 24\text{ h} = 86\,400\text{ s}; \quad 1\text{ s} = 1000\text{ ms}$"),
                F("Khoảng thời gian diễn ra sự kiện", r"$\Delta t = t_2 - t_1$", r"$t_1$ là thời điểm bắt đầu, $t_2$ là thời điểm kết thúc."),
            ),
        ],
        "example": (
            r"a) Khi dùng cân Roberval để cân một túi đường, người ta đặt túi đường lên đĩa cân bên trái, còn đĩa cân bên phải đặt một quả cân $500\text{ g}$, hai quả cân $100\text{ g}$ và một quả cân $50\text{ g}$ thì đòn cân thăng bằng (con mã ở vạch $0$). Tính khối lượng túi đường ra đơn vị gam ($\text{g}$) và ki-lô-gam ($\text{kg}$)." "\n"
            r"b) Một vận động viên chạy cự li ngắn hết $1\text{ phút } 15\text{ giây}$. Hãy đổi khoảng thời gian này ra đơn vị giây ($\text{s}$)."
        ),
        "example_answer": (
            r"a) Tổng khối lượng các quả cân trên đĩa phải là: $m = 500 + 2 \cdot 100 + 50 = 750\text{ g} = 0{,}75\text{ kg}$." "\n"
            r"b) Đổi sang đơn vị giây: $t = 1 \cdot 60 + 15 = 75\text{ s}$."
        ),
        "real_life": (
            r"- Trên vỏ gói mì ghi “Khối lượng tịnh $75\text{ g}$” chỉ khối lượng thực của vắt mì và gia vị bên trong, không tính khối lượng bao bì." "\n"
            r"- Trong thi đấu điền kinh và bơi lội, người ta dùng đồng hồ bấm giây điện tử kết hợp cảm biến chạm có $\text{ĐCNN} = 0{,}01\text{ s}$ hoặc $0{,}001\text{ s}$ để phân định thứ hạng các vận động viên."
        ),
        "game_title": "Phòng thí nghiệm Đo khối lượng và Thời gian",
        "game_description": "Thực hành cân khối lượng vật bằng cân Roberval, cân đồng hồ và bấm giây đo thời gian chuyển động với độ chính xác cao.",
        "game_type": "game_khoiluong",
        "quiz": [
            mcq(
                "biet",
                r"Đơn vị đo khối lượng và đơn vị đo thời gian cơ bản trong hệ thống đo lường quốc tế SI lần lượt là:",
                [
                    r"Ki-lô-gam ($\text{kg}$) và giây ($\text{s}$).",
                    r"Gam ($\text{g}$) và phút ($\text{min}$).",
                    r"Ki-lô-gam ($\text{kg}$) và giờ ($\text{h}$).",
                    r"Tấn ($\text{t}$) và giây ($\text{s}$).",
                ],
                0,
                r"Trong hệ SI, đơn vị cơ bản đo khối lượng là **ki-lô-gam** ($\text{kg}$) và đơn vị cơ bản đo thời gian là **giây** ($\text{s}$).",
            ),
            mcq(
                "biet",
                r"Trên vỏ một hộp sữa bột có ghi “Khối lượng tịnh $850\text{ g}$”. Con số này cho biết điều gì?",
                [
                    r"Khối lượng của riêng phần sữa bột chứa bên trong hộp.",
                    r"Tổng khối lượng của cả vỏ hộp thiết và sữa bột bên trong.",
                    r"Thể tích của chiếc hộp đựng sữa bột.",
                    r"Giới hạn đo của chiếc cân dùng để cân hộp sữa.",
                ],
                0,
                r"“Khối lượng tịnh” (Net weight) là khối lượng thực của hàng hoá bên trong, **không tính khối lượng vỏ bao bì**.",
            ),
            mcq(
                "biet",
                r"Để đo thời gian một bạn học sinh chạy cự li $100\text{ m}$ trong giờ Thể dục, dụng cụ đo nào sau đây là phù hợp nhất?",
                [
                    r"Đồng hồ bấm giây.",
                    r"Đồng hồ treo tường.",
                    r"Đồng hồ cát.",
                    r"Lịch treo tường.",
                ],
                0,
                r"Thời gian chạy $100\text{ m}$ chỉ khoảng hơn $10\text{ s}$ và đòi hỏi độ chính xác đến phần mười hoặc phần trăm giây nên cần dùng **đồng hồ bấm giây**.",
            ),
            mcq(
                "biet",
                r"Theo quy ước dân gian ở Việt Nam, $1\text{ lạng}$ (tức $1\text{ hg}$) bằng bao nhiêu gam ($\text{g}$)?",
                [
                    r"$100\text{ g}$.",
                    r"$10\text{ g}$.",
                    r"$500\text{ g}$.",
                    r"$1000\text{ g}$.",
                ],
                0,
                r"Ta có $1\text{ kg} = 10\text{ hg (lạng)} = 1000\text{ g}$, suy ra $1\text{ lạng} = 100\text{ g}$.",
            ),
            mcq(
                "hieu",
                r"Một chiếc cân đồng hồ có $\text{GHĐ} = 5\text{ kg}$. Trên mặt cân, khoảng cách giữa vạch $0\text{ kg}$ và vạch $1\text{ kg}$ được chia thành $50$ khoảng nhỏ bằng nhau. Độ chia nhỏ nhất (ĐCNN) của chiếc cân này là:",
                [
                    r"$20\text{ g}$.",
                    r"$50\text{ g}$.",
                    r"$10\text{ g}$.",
                    r"$100\text{ g}$.",
                ],
                0,
                r"Đổi $1\text{ kg} = 1000\text{ g}$. Giữa vạch $0$ và $1000\text{ g}$ có $50$ khoảng chia đều nhau nên $\text{ĐCNN} = \dfrac{1000\text{ g}}{50} = 20\text{ g}$.",
            ),
            mcq(
                "hieu",
                r"Một bộ phim khoa học bắt đầu chiếu lúc $19\text{ giờ } 45\text{ phút}$ và kết thúc lúc $21\text{ giờ } 10\text{ phút}$ cùng ngày. Thời lượng của bộ phim đó tính theo đơn vị giây ($\text{s}$) là:",
                [
                    r"$5100\text{ s}$.",
                    r"$4500\text{ s}$.",
                    r"$5400\text{ s}$.",
                    r"$3900\text{ s}$.",
                ],
                0,
                r"Khoảng thời gian chiếu phim là $\Delta t = 21\text{ h } 10\text{ phút} - 19\text{ h } 45\text{ phút} = 1\text{ h } 25\text{ phút} = 85\text{ phút}$. Đổi ra giây: $85 \cdot 60 = 5100\text{ s}$.",
            ),
            tf4(
                "hieu",
                r"Khi thực hành đo khối lượng bằng cân đồng hồ và đo thời gian bằng đồng hồ bấm giây trong phòng thực hành, mỗi nhận định sau đây đúng hay sai?",
                [
                    r"a) Trước khi đặt vật lên đĩa cân đồng hồ, phải kiểm tra và vặn ốc điều chỉnh để kim cân chỉ đúng vạch số $0$.",
                    r"b) Để cân một chiếc nhẫn vàng nặng khoảng $3{,}75\text{ g}$, dùng cân tạ có $\text{GHĐ} = 100\text{ kg}$ và $\text{ĐCNN} = 100\text{ g}$ sẽ cho kết quả chính xác nhất.",
                    r"c) Trên đồng hồ bấm giây điện tử, nút `RESET` dùng để đưa số chỉ của đồng hồ về $00{:}00{,}00$ trước khi thực hiện phép đo mới.",
                    r"d) Khi đọc số chỉ trên mặt cân đồng hồ, hai bạn đứng nhìn xiên từ hai phía trái và phải sẽ luôn đọc được cùng một giá trị chính xác như nhau.",
                ],
                [True, False, True, False],
                r"a) Đúng vì hiệu chỉnh cân về vạch số $0$ giúp loại bỏ sai số điểm không." "\n"
                r"b) Sai vì nhẫn vàng nặng $3{,}75\text{ g}$ nhỏ hơn rất nhiều so với $\text{ĐCNN} = 100\text{ g}$ của cân tạ; phải dùng cân tiểu li hoặc cân điện tử có $\text{ĐCNN} \le 0{,}01\text{ g}$." "\n"
                r"c) Đúng vì nút `RESET` dùng để hiệu chỉnh đồng hồ bấm giây về số $0$." "\n"
                r"d) Sai vì nhìn xiên từ hai phía sẽ gây ra sai số thị sai làm kết quả đọc bị lệch; phải đặt mắt nhìn vuông góc với mặt cân tại đầu kim.",
            ),
            tf4(
                "hieu",
                r"Xét các phép quy đổi đơn vị khối lượng và thời gian. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) $0{,}45\text{ tấn} = 450\text{ kg}$.",
                    r"b) $250\text{ mg} = 2{,}5\text{ g}$.",
                    r"c) $1{,}5\text{ giờ} = 90\text{ phút} = 5400\text{ s}$.",
                    r"d) $3\text{ lạng rưỡi} = 350\text{ g} = 0{,}35\text{ kg}$.",
                ],
                [True, False, True, True],
                r"a) Đúng vì $0{,}45 \cdot 1000\text{ kg} = 450\text{ kg}$." "\n"
                r"b) Sai vì $1\text{ g} = 1000\text{ mg}$ nên $250\text{ mg} = \dfrac{250}{1000}\text{ g} = 0{,}25\text{ g}$." "\n"
                r"c) Đúng vì $1{,}5 \cdot 60 = 90\text{ phút}$ và $90 \cdot 60 = 5400\text{ s}$." "\n"
                r"d) Đúng vì $1\text{ lạng} = 100\text{ g}$ nên $3{,}5\text{ lạng} = 350\text{ g} = 0{,}35\text{ kg}$.",
            ),
            mcq(
                "vandung",
                r"Trước khi đặt vật lên một chiếc cân đồng hồ, học sinh quên hiệu chỉnh cân nên kim cân đã chỉ sẵn ở vạch $50\text{ g}$. Khi đặt một quả bưởi lên đĩa cân thì kim cân chỉ ở vạch $1\text{ kg } 250\text{ g}$. Khối lượng thực tế của quả bưởi là:",
                [
                    r"$1200\text{ g}$.",
                    r"$1300\text{ g}$.",
                    r"$1250\text{ g}$.",
                    r"$1150\text{ g}$.",
                ],
                0,
                r"Đổi $1\text{ kg } 250\text{ g} = 1250\text{ g}$. Vì khi chưa đặt vật kim đã lệch dương $50\text{ g}$ nên khối lượng thực tế của quả bưởi là $m = 1250 - 50 = 1200\text{ g} = 1{,}2\text{ kg}$.",
            ),
            short(
                "vandung",
                r"Một cốc thuỷ tinh rỗng khi đặt lên cân điện tử có số chỉ $120\text{ g}$. Sau khi rót thêm $50\text{ viên bi sắt}$ giống hệt nhau vào cốc thì số chỉ của cân là $470\text{ g}$. Tính khối lượng của một viên bi sắt theo đơn vị gam ($\text{g}$).",
                ["7", "7,0", "7.0"],
                r"Khối lượng của $50$ viên bi sắt là $m_{50} = 470 - 120 = 350\text{ g}$. Khối lượng của một viên bi sắt là $m_1 = \dfrac{350}{50} = 7\text{ g}$.",
            ),
        ],
    },
    {
        "topic": "nhiet-do",
        "title": "Đo nhiệt độ và Các thang nhiệt độ",
        "icon": "🌡️",
        "description": "Chương I · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 29–34): Bài 8. Khái niệm nhiệt độ, nguyên tắc chế tạo nhiệt kế dựa trên sự nở vì nhiệt của chất lỏng, các thang nhiệt độ Celsius, Fahrenheit, Kelvin và quy tắc sử dụng nhiệt kế y tế, nhiệt kế phòng thí nghiệm.",
        "requirements": [
            r"Lấy được ví dụ chứng tỏ giác quan của chúng ta có thể cảm nhận sai về nhiệt độ của các vật.",
            r"Phát biểu được nhiệt độ là số đo độ “nóng”, “lạnh” của vật; vật nóng hơn có nhiệt độ cao hơn, vật lạnh hơn có nhiệt độ thấp hơn.",
            r"Nêu được nguyên tắc cấu tạo và hoạt động của nhiệt kế chất lỏng dựa trên hiện tượng dãn nở vì nhiệt của chất lỏng.",
            r"Xác định được đơn vị đo nhiệt độ trong hệ SI là Kelvin ($\text{K}$), đơn vị thông dụng ở Việt Nam là độ Celsius ($^\circ\text{C}$) và ở các nước nói tiếng Anh là độ Fahrenheit ($^\circ\text{F}$); chuyển đổi được giữa các thang nhiệt độ.",
            r"Thực hiện được phép đo nhiệt độ của cơ thể và của nước bằng nhiệt kế đúng quy tắc và an toàn.",
        ],
        "definition": (
            r"- **Nhiệt độ** là số đo mức độ “nóng”, “lạnh” của một vật. Vật nóng hơn có nhiệt độ cao hơn; vật lạnh hơn có nhiệt độ thấp hơn." "\n"
            r"- Đơn vị đo nhiệt độ trong hệ SI là **Kelvin** (kí hiệu $\text{K}$); đơn vị đo nhiệt độ thông dụng ở Việt Nam là **độ Celsius** (kí hiệu $^\circ\text{C}$); một số nước sử dụng **độ Fahrenheit** (kí hiệu $^\circ\text{F}$)." "\n"
            r"- **Nhiệt kế chất lỏng** (rượu, thuỷ ngân, dầu màu) hoạt động dựa trên hiện tượng **dãn nở vì nhiệt của chất lỏng**."
        ),
        "theory": (
            r"### Bài 8. Đo nhiệt độ" "\n"
            r"- **Thí nghiệm cảm giác tay với 3 cốc nước** (lạnh, nguội, ấm): Ngón tay nhúng từ nước lạnh sang nước nguội thấy ấm, còn ngón tay nhúng từ nước ấm sang nước nguội lại thấy lạnh. Điều đó chứng tỏ giác quan không thể xác định chính xác nhiệt độ mà phải dùng **nhiệt kế**." "\n"
            r"- **Ba thang nhiệt độ phổ biến**:" "\n"
            r"  + **Thang nhiệt độ Celsius ($^\circ\text{C}$)**: Chọn nhiệt độ của nước đá đang tan ở áp suất tiêu chuẩn là $0^\circ\text{C}$ và nhiệt độ của hơi nước đang sôi là $100^\circ\text{C}$." "\n"
            r"  + **Thang nhiệt độ Fahrenheit ($^\circ\text{F}$)**: Nhiệt độ của nước đá đang tan là $32^\circ\text{F}$ và nhiệt độ của hơi nước đang sôi là $212^\circ\text{F}$ (chia thành $180$ khoảng đều nhau, nên độ biến thiên $1^\circ\text{C}$ tương ứng với $1{,}8^\circ\text{F}$)." "\n"
            r"  + **Thang nhiệt độ tuyệt đối Kelvin ($\text{K}$)**: Nhiệt độ nước đá đang tan là $273{,}15\text{ K}$ (thường lấy tròn là $273\text{ K}$) và hơi nước đang sôi là $373\text{ K}$. Độ biến thiên $1^\circ\text{C}$ bằng đúng độ biến thiên $1\text{ K}$." "\n"
            r"- **Cấu tạo đặc biệt của nhiệt kế y tế chất lỏng**: Có $\text{GHĐ}$ từ $35^\circ\text{C}$ đến $42^\circ\text{C}$, $\text{ĐCNN} = 0{,}1^\circ\text{C}$. Phần ống quản gần bầu chứa có một **chỗ thắt** ngăn không cho chất lỏng tự tụt xuống khi lấy nhiệt kế ra khỏi cơ thể để người dùng đọc kết quả chính xác; vì vậy trước khi đo phải **vảy mạnh** cho cột chất lỏng tụt xuống dưới vạch $35^\circ\text{C}$."
        ),
        "formulas": [
            G(
                "I. Chuyển đổi giữa các thang nhiệt độ",
                F("Từ độ Celsius sang độ Fahrenheit", r"$t(^\circ\text{F}) = t(^\circ\text{C}) \cdot 1{,}8 + 32$", r"Ví dụ: $0^\circ\text{C} = 32^\circ\text{F}$; $100^\circ\text{C} = 212^\circ\text{F}$."),
                F("Từ độ Fahrenheit sang độ Celsius", r"$t(^\circ\text{C}) = \dfrac{t(^\circ\text{F}) - 32}{1{,}8} = \dfrac{5}{9}\cdot \left[t(^\circ\text{F}) - 32\right]$"),
                F("Giữa độ Celsius và Kelvin", r"$T(\text{K}) = t(^\circ\text{C}) + 273 \iff t(^\circ\text{C}) = T(\text{K}) - 273$", r"Chính xác hơn là cộng $273{,}15$."),
            ),
            G(
                "II. Độ biến thiên nhiệt độ",
                F("Liên hệ độ tăng giảm nhiệt độ", r"$\Delta T(\text{K}) = \Delta t(^\circ\text{C}); \quad \Delta t(^\circ\text{F}) = 1{,}8 \cdot \Delta t(^\circ\text{C})$", r"Khi nhiệt độ tăng thêm $10^\circ\text{C}$ thì trong thang $\text{K}$ tăng $10\text{ K}$ và trong thang $^\circ\text{F}$ tăng $18^\circ\text{F}$."),
            ),
        ],
        "example": (
            r"Nhiệt độ cơ thể người bình thường là $37^\circ\text{C}$. Hãy tính nhiệt độ này theo thang nhiệt độ Fahrenheit ($^\circ\text{F}$) và thang nhiệt độ Kelvin ($\text{K}$)."
        ),
        "example_answer": (
            r"- Theo thang nhiệt độ Fahrenheit: $t(^\circ\text{F}) = 37 \cdot 1{,}8 + 32 = 66{,}6 + 32 = 98{,}6^\circ\text{F}$." "\n"
            r"- Theo thang nhiệt độ Kelvin: $T(\text{K}) = 37 + 273 = 310\text{ K}$."
        ),
        "real_life": (
            r"- Nhiệt kế y tế điện tử và nhiệt kế hồng ngoại đo trán giúp kiểm tra thân nhiệt nhanh chóng và an toàn hơn nhiệt kế thuỷ ngân (vì thuỷ ngân rất độc nếu nhiệt kế bị vỡ)." "\n"
            r"- Nhiệt kế rượu có màu đỏ thường dùng để đo nhiệt độ khí quyển và phòng thí nghiệm; rơ-le nhiệt trong bàn là, nồi cơm điện hoạt động dựa trên sự dãn nở vì nhiệt của băng kép."
        ),
        "game_title": "Thí nghiệm Đo nhiệt độ và Chuyển đổi thang đo",
        "game_description": "Đo nhiệt độ của nước ở các trạng thái khác nhau bằng nhiệt kế và thực hành quy đổi giữa thang nhiệt độ Celsius, Fahrenheit và Kelvin.",
        "game_type": "game_nhietdo",
        "quiz": [
            mcq(
                "biet",
                r"Trong thang nhiệt độ Celsius ($^\circ\text{C}$), nhiệt độ của nước đá đang tan và nhiệt độ của hơi nước đang sôi ở áp suất tiêu chuẩn lần lượt là:",
                [
                    r"$0^\circ\text{C}$ và $100^\circ\text{C}$.",
                    r"$32^\circ\text{C}$ và $212^\circ\text{C}$.",
                    r"$273^\circ\text{C}$ và $373^\circ\text{C}$.",
                    r"$0^\circ\text{C}$ và $37^\circ\text{C}$.",
                ],
                0,
                r"Trong thang nhiệt độ Celsius, nước đá đang tan có nhiệt độ $0^\circ\text{C}$ và hơi nước đang sôi có nhiệt độ $100^\circ\text{C}$.",
            ),
            mcq(
                "biet",
                r"Nhiệt kế chất lỏng (như nhiệt kế rượu, nhiệt kế thuỷ ngân) hoạt động dựa trên hiện tượng vật lí nào?",
                [
                    r"Sự dãn nở vì nhiệt của chất lỏng.",
                    r"Sự dãn nở vì nhiệt của chất khí.",
                    r"Sự truyền ánh sáng qua ống thuỷ tinh.",
                    r"Sự biến dạng đàn hồi của lò xo.",
                ],
                0,
                r"Khi nhiệt độ tăng, chất lỏng trong bầu nhiệt kế nở ra và dâng lên trong ống quản; khi nhiệt độ giảm, chất lỏng co lại. Đó là **sự dãn nở vì nhiệt của chất lỏng**.",
            ),
            mcq(
                "biet",
                r"Giới hạn đo của nhiệt kế y tế chất lỏng thông thường nằm trong khoảng nào sau đây?",
                [
                    r"Từ $35^\circ\text{C}$ đến $42^\circ\text{C}$.",
                    r"Từ $0^\circ\text{C}$ đến $100^\circ\text{C}$.",
                    r"Từ $-20^\circ\text{C}$ đến $50^\circ\text{C}$.",
                    r"Từ $20^\circ\text{C}$ đến $120^\circ\text{C}$.",
                ],
                0,
                r"Nhiệt độ cơ thể người sống chỉ dao động quanh $37^\circ\text{C}$ nên nhiệt kế y tế được thiết kế có thang đo từ $35^\circ\text{C}$ đến $42^\circ\text{C}$ với $\text{ĐCNN} = 0{,}1^\circ\text{C}$.",
            ),
            mcq(
                "biet",
                r"Đơn vị đo nhiệt độ cơ bản trong hệ thống đo lường quốc tế SI là:",
                [
                    r"Kelvin ($\text{K}$).",
                    r"Độ Celsius ($^\circ\text{C}$).",
                    r"Độ Fahrenheit ($^\circ\text{F}$).",
                    r"Jun ($\text{J}$).",
                ],
                0,
                r"Trong hệ đo lường quốc tế SI, đơn vị cơ bản của nhiệt độ nhiệt động lực học là **Kelvin** ($\text{K}$).",
            ),
            mcq(
                "hieu",
                r"Bản tin dự báo thời tiết tại Hà Nội cho biết nhiệt độ ban trưa là $25^\circ\text{C}$. Giá trị nhiệt độ này tương ứng với bao nhiêu độ Fahrenheit ($^\circ\text{F}$)?",
                [
                    r"$77^\circ\text{F}$.",
                    r"$57^\circ\text{F}$.",
                    r"$45^\circ\text{F}$.",
                    r"$298^\circ\text{F}$.",
                ],
                0,
                r"Áp dụng công thức chuyển đổi: $t(^\circ\text{F}) = t(^\circ\text{C}) \cdot 1{,}8 + 32 = 25 \cdot 1{,}8 + 32 = 45 + 32 = 77^\circ\text{F}$.",
            ),
            mcq(
                "hieu",
                r"Tại sao không thể dùng nhiệt kế y tế (có giới hạn đo từ $35^\circ\text{C}$ đến $42^\circ\text{C}$) để đo nhiệt độ của nước đang sôi ($100^\circ\text{C}$)?",
                [
                    r"Vì chất lỏng trong bầu sẽ dãn nở quá mức giới hạn của ống quản và làm nổ vỡ nhiệt kế.",
                    r"Vì chất lỏng trong nhiệt kế y tế sẽ đông đặc lại ở $100^\circ\text{C}$.",
                    r"Vì chỗ thắt của nhiệt kế y tế ngăn không cho chất lỏng dâng lên khi gặp nóng.",
                    r"Vì vỏ thuỷ tinh của nhiệt kế y tế tan chảy ngay ở $50^\circ\text{C}$.",
                ],
                0,
                r"Nhiệt độ nước đang sôi ($100^\circ\text{C}$) vượt quá xa giới hạn đo $42^\circ\text{C}$ của nhiệt kế y tế, làm chất lỏng nở mạnh tràn hết ống quản và **gây vỡ bầu nhiệt kế**.",
            ),
            tf4(
                "hieu",
                r"Xét đặc điểm cấu tạo và cách sử dụng các loại nhiệt kế. Mỗi phát biểu sau đây đúng hay sai?",
                [
                    r"a) Ống quản của nhiệt kế y tế chất lỏng có một chỗ thắt ở gần bầu để ngăn chất lỏng tự tụt xuống khi lấy nhiệt kế ra khỏi cơ thể.",
                    r"b) Khi đo nhiệt độ của một cốc nước nóng bằng nhiệt kế phòng thí nghiệm, ta phải nhấc bầu nhiệt kế ra khỏi cốc nước rồi mới đọc kết quả.",
                    r"c) Nếu nhiệt kế thuỷ ngân chẳng may bị vỡ, tuyệt đối không dùng tay trần gom các giọt thuỷ ngân vì hơi thuỷ ngân rất độc.",
                    r"d) Khi nhiệt độ của một vật tăng thêm $10^\circ\text{C}$ thì trong thang nhiệt độ Kelvin, nhiệt độ của vật đó tăng thêm $283\text{ K}$.",
                ],
                [True, False, True, False],
                r"a) Đúng vì chỗ thắt giữ cột chất lỏng đứng yên để người đo đọc kết quả sau khi lấy ra khỏi cơ thể." "\n"
                r"b) Sai vì nhiệt kế phòng thí nghiệm không có chỗ thắt; khi đọc kết quả phải giữ nguyên bầu nhiệt kế ngập trong nước (không chạm đáy và thành cốc)." "\n"
                r"c) Đúng vì thuỷ ngân dễ bay hơi và rất độc đối với hệ thần kinh, hô hấp." "\n"
                r"d) Sai vì độ biến thiên $\Delta T(\text{K}) = \Delta t(^\circ\text{C}) = 10\text{ K}$ chứ không phải cộng thêm $273$.",
            ),
            tf4(
                "hieu",
                r"Xét sự quy đổi giữa ba thang nhiệt độ Celsius ($^\circ\text{C}$), Fahrenheit ($^\circ\text{F}$) và Kelvin ($\text{K}$). Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) $0^\circ\text{C}$ tương ứng với $32^\circ\text{F}$ và $273\text{ K}$.",
                    r"b) $100^\circ\text{C}$ tương ứng với $212^\circ\text{F}$ và $373\text{ K}$.",
                    r"c) Nhiệt độ $50^\circ\text{F}$ tương ứng với $10^\circ\text{C}$.",
                    r"d) Nhiệt độ $300\text{ K}$ cao hơn nhiệt độ $40^\circ\text{C}$.",
                ],
                [True, True, True, False],
                r"a) Đúng theo mốc nhiệt độ nước đá đang tan." "\n"
                r"b) Đúng theo mốc nhiệt độ hơi nước đang sôi." "\n"
                r"c) Đúng vì $t(^\circ\text{C}) = \dfrac{50 - 32}{1{,}8} = \dfrac{18}{1{,}8} = 10^\circ\text{C}$." "\n"
                r"d) Sai vì $300\text{ K} = 300 - 273 = 27^\circ\text{C} < 40^\circ\text{C}$.",
            ),
            mcq(
                "vandung",
                r"Một nhiệt kế thuỷ ngân bị mờ hết các vạch số nhưng ống chia vẫn đều. Khi nhúng bầu nhiệt kế vào nước đá đang tan ($0^\circ\text{C}$) thì cột thuỷ ngân dài $2\text{ cm}$; khi nhúng vào hơi nước đang sôi ($100^\circ\text{C}$) thì cột thuỷ ngân dài $22\text{ cm}$. Khi nhúng nhiệt kế này vào một cốc nước ấm thì cột thuỷ ngân dài $9\text{ cm}$. Nhiệt độ của cốc nước ấm là:",
                [
                    r"$35^\circ\text{C}$.",
                    r"$45^\circ\text{C}$.",
                    r"$40^\circ\text{C}$.",
                    r"$30^\circ\text{C}$.",
                ],
                0,
                r"Khi nhiệt độ tăng từ $0^\circ\text{C}$ lên $100^\circ\text{C}$ (tăng $100^\circ\text{C}$), cột thuỷ ngân dài thêm $22 - 2 = 20\text{ cm}$, tức mỗi $1^\circ\text{C}$ ứng với $0{,}2\text{ cm}$. Ở cốc nước ấm, cột thuỷ ngân dài hơn vạch $0^\circ\text{C}$ một đoạn $9 - 2 = 7\text{ cm}$, nên nhiệt độ cốc nước là $t = \dfrac{7}{0{,}2} = 35^\circ\text{C}$.",
            ),
            short(
                "vandung",
                r"Một du khách tại New York thấy bảng điện tử ngoài trời hiển thị nhiệt độ là $68^\circ\text{F}$. Hãy tính nhiệt độ đó theo đơn vị độ Celsius ($^\circ\text{C}$).",
                ["20", "20,0", "20.0"],
                r"Áp dụng công thức đổi từ $^\circ\text{F}$ sang $^\circ\text{C}$: $t(^\circ\text{C}) = \dfrac{68 - 32}{1{,}8} = \dfrac{36}{1{,}8} = 20^\circ\text{C}$.",
            ),
        ],
    },
    {
        "topic": "luc",
        "title": "Lực và tác dụng của lực, Biểu diễn lực và Biến dạng của lò xo",
        "icon": "🏹",
        "description": "Chương VIII · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 144–152): Bài 40 – Bài 42. Khái niệm lực, tác dụng làm biến đổi chuyển động và làm biến dạng vật, lực tiếp xúc và lực không tiếp xúc; cách biểu diễn lực bằng mũi tên vectơ; biến dạng đàn hồi của lò xo và nguyên tắc hoạt động của lực kế.",
        "requirements": [
            r"Lấy được ví dụ để chứng tỏ lực là sự đẩy hoặc sự kéo.",
            r"Nhận biết được tác dụng của lực làm thay đổi tốc độ, thay đổi hướng chuyển động của vật hoặc làm biến dạng vật.",
            r"Phân biệt được lực tiếp xúc (xuất hiện khi hai vật chạm vào nhau) và lực không tiếp xúc (xuất hiện khi hai vật không chạm vào nhau).",
            r"Nêu được đơn vị đo lực là niutơn ($\text{N}$), dụng cụ đo lực là lực kế và biểu diễn được một lực bằng một mũi tên có điểm đặt, phương, chiều và độ lớn theo tỉ xích cho trước.",
            r"Thực hiện được thí nghiệm chứng minh độ dãn của lò xo treo thẳng đứng tỉ lệ thuận với khối lượng (hoặc trọng lượng) của vật treo.",
        ],
        "definition": (
            r"- Tác dụng **đẩy** hoặc **kéo** của vật này lên vật khác được gọi là **lực** (kí hiệu là $F$, vectơ lực kí hiệu là $\overrightarrow{F}$). Đơn vị đo lực trong hệ SI là **niutơn**, kí hiệu là $\text{N}$." "\n"
            r"- **Tác dụng của lực**: Lực tác dụng lên một vật có thể làm **biến đổi chuyển động** của vật (làm vật bắt đầu chuyển động, dừng lại, chuyển động nhanh lên, chậm đi hoặc đổi hướng) hoặc làm **biến dạng** vật, hoặc đồng thời gây ra cả hai tác dụng đó." "\n"
            r"- **Độ dãn của lò xo** treo thẳng đứng bằng hiệu giữa chiều dài lò xo khi bị biến dạng ($l$) và chiều dài tự nhiên ban đầu ($l_0$): $\Delta l = l - l_0$."
        ),
        "theory": (
            r"### Bài 40. Lực là gì?" "\n"
            r"- **Sự đẩy và sự kéo**: Khi ta đẩy xe hàng, kéo gầu nước, đá quả bóng hay nam châm hút đinh sắt thì đều có lực tác dụng." "\n"
            r"- **Lực tiếp xúc và lực không tiếp xúc**:" "\n"
            r"  + **Lực tiếp xúc** là lực xuất hiện khi vật gây ra lực có sự tiếp xúc với vật chịu tác dụng của lực (ví dụ: lực chân cầu thủ đá vào quả bóng, lực tay đẩy cánh cửa, lực ma sát)." "\n"
            r"  + **Lực không tiếp xúc** là lực xuất hiện khi vật gây ra lực không tiếp xúc với vật chịu tác dụng của lực (ví dụ: lực hút của nam châm lên ghim sắt đặt cách xa, lực hút của Trái Đất lên quả táo đang rơi)." "\n"
            r"### Bài 41. Biểu diễn lực" "\n"
            r"- **Các đặc trưng của lực**: Mỗi lực được xác định bởi $4$ yếu tố: **điểm đặt**, **phương** (nằm ngang, thẳng đứng hay xiên), **chiều** (từ trái sang phải, từ trên xuống dưới, ...) và **độ lớn** (cường độ lực tính bằng $\text{N}$)." "\n"
            r"- **Cách biểu diễn lực bằng mũi tên**: Ta dùng một mũi tên $\overrightarrow{F}$ có:" "\n"
            r"  + **Gốc** của mũi tên đặt tại điểm mà lực tác dụng lên vật (điểm đặt);" "\n"
            r"  + **Hướng** (phương và chiều) của mũi tên trùng với phương và chiều của lực;" "\n"
            r"  + **Chiều dài** của mũi tên biểu diễn độ lớn của lực theo một tỉ xích cho trước (ví dụ $1\text{ cm}$ ứng với $10\text{ N}$)." "\n"
            r"- **Dụng cụ đo lực**: Dùng **lực kế** (thường là lực kế lò xo). Trước khi đo cần hiệu chỉnh kim lực kế về đúng vạch số $0$ và kéo lực kế dọc theo phương của lực cần đo." "\n"
            r"### Bài 42. Biến dạng của lò xo" "\n"
            r"- **Tính chất đàn hồi**: Khi kéo hoặc nén lò xo trong giới hạn đàn hồi, lò xo bị biến dạng; khi thôi tác dụng lực, lò xo tự trở về chiều dài tự nhiên ban đầu $l_0$." "\n"
            r"- **Quy luật độ dãn của lò xo**: Độ dãn $\Delta l = l - l_0$ của lò xo treo thẳng đứng **tỉ lệ thuận** với khối lượng $m$ (và trọng lượng $P$) của vật treo: nếu khối lượng vật treo tăng gấp $n$ lần thì độ dãn của lò xo cũng tăng gấp $n$ lần. Đây là nguyên tắc chế tạo **lực kế lò xo** và **cân lò xo**."
        ),
        "formulas": [
            G(
                "I. Biểu diễn lực theo tỉ xích",
                F("Chiều dài mũi tên biểu diễn lực", r"$n_{\text{đoạn}} = \dfrac{F}{\Delta F_0}$", r"$F$ là độ lớn lực ($\text{N}$), $\Delta F_0$ là độ lớn lực ứng với $1\text{ cm}$ tỉ xích."),
                F("Độ lớn lực từ hình vẽ", r"$F = n_{\text{đoạn}} \cdot \Delta F_0$", r"Ví dụ mũi tên dài $4\text{ đoạn}$, mỗi đoạn ứng với $5\text{ N}$ thì $F = 20\text{ N}$."),
            ),
            G(
                "II. Độ dãn của lò xo treo thẳng đứng",
                F("Độ dãn của lò xo", r"$\Delta l = l - l_0 \iff l = l_0 + \Delta l$", r"$l_0$ là chiều dài tự nhiên ban đầu, $l$ là chiều dài khi treo vật."),
                F("Tỉ lệ thuận giữa độ dãn và khối lượng vật treo", r"$\dfrac{\Delta l_2}{\Delta l_1} = \dfrac{m_2}{m_1} = \dfrac{P_2}{P_1}$", r"Áp dụng trong giới hạn đàn hồi của lò xo."),
            ),
        ],
        "example": (
            r"Một lò xo có chiều dài tự nhiên ban đầu $l_0 = 12\text{ cm}$ được treo thẳng đứng. Khi treo một quả nặng có khối lượng $m_1 = 100\text{ g}$ vào đầu dưới của lò xo thì chiều dài của lò xo là $l_1 = 15\text{ cm}$. Hỏi nếu treo quả nặng $m_2 = 300\text{ g}$ vào lò xo đó thì độ dãn $\Delta l_2$ và chiều dài $l_2$ của lò xo là bao nhiêu?"
        ),
        "example_answer": (
            r"- Khi treo vật $m_1 = 100\text{ g}$, độ dãn của lò xo là: $\Delta l_1 = l_1 - l_0 = 15 - 12 = 3\text{ cm}$." "\n"
            r"- Vì độ dãn của lò xo tỉ lệ thuận với khối lượng vật treo nên khi treo vật $m_2 = 300\text{ g}$ (gấp $3$ lần $m_1$), độ dãn của lò xo là: $\Delta l_2 = \Delta l_1 \cdot \dfrac{m_2}{m_1} = 3 \cdot \dfrac{300}{100} = 9\text{ cm}$." "\n"
            r"- Chiều dài của lò xo khi đó là: $l_2 = l_0 + \Delta l_2 = 12 + 9 = 21\text{ cm}$."
        ),
        "real_life": (
            r"- Lò xo được ứng dụng trong **lực kế**, **cân đồng hồ**, **giảm xóc (phuộc nhún)** của xe máy và ô tô, đệm lò xo, bút bi bấm." "\n"
            r"- Trong thể thao (bắn cung, nhảy sào, quần vợt), lực của tay vận động viên vừa làm biến dạng dây cung, mặt vợt vừa làm biến đổi chuyển động của mũi tên, quả bóng."
        ),
        "game_title": "Mô phỏng Lực và Độ dãn lò xo",
        "game_description": "Biểu diễn vectơ lực tác dụng lên vật và treo các quả nặng vào lò xo để khảo sát mối liên hệ tỉ lệ thuận giữa độ dãn lò xo và khối lượng vật treo.",
        "game_type": "game_luc",
        "quiz": [
            mcq(
                "biet",
                r"Đơn vị đo lực trong hệ thống đo lường quốc tế SI và dụng cụ dùng để đo lực lần lượt là:",
                [
                    r"Niutơn ($\text{N}$) và lực kế.",
                    r"Ki-lô-gam ($\text{kg}$) và cân Roberval.",
                    r"Jun ($\text{J}$) và lực kế.",
                    r"Niutơn ($\text{N}$) và thước kẹp.",
                ],
                0,
                r"Đơn vị đo lực là **niutơn** ($\text{N}$) và dụng cụ dùng để đo lực là **lực kế**.",
            ),
            mcq(
                "biet",
                r"Trường hợp nào sau đây là **lực không tiếp xúc**?",
                [
                    r"Lực của thanh nam châm hút chiếc đinh sắt đặt cách nó $2\text{ cm}$.",
                    r"Lực của chân cầu thủ sút vào quả bóng đang nằm trên sân.",
                    r"Lực của tay học sinh kéo ngăn bàn mở ra.",
                    r"Lực của gió thổi căng buồm làm thuyền chạy trên mặt nước.",
                ],
                0,
                r"Thanh nam châm hút chiếc đinh sắt từ khoảng cách $2\text{ cm}$ mà không cần chạm vào đinh sắt nên đó là **lực không tiếp xúc**.",
            ),
            mcq(
                "biet",
                r"Khi một vận động viên dùng vợt đập mạnh vào quả bóng bàn đang bay tới làm quả bóng bị bẹp một chút và bật ngược trở lại, lực của vợt tác dụng lên quả bóng đã gây ra kết quả gì?",
                [
                    r"Vừa làm biến dạng quả bóng, vừa làm biến đổi chuyển động của quả bóng.",
                    r"Chỉ làm biến dạng quả bóng mà không làm biến đổi chuyển động.",
                    r"Chỉ làm biến đổi chuyển động của quả bóng mà không làm biến dạng.",
                    r"Làm tăng khối lượng của quả bóng bàn.",
                ],
                0,
                r"Quả bóng bị bẹp là bị **biến dạng**, đồng thời bật ngược trở lại là bị **biến đổi chuyển động**.",
            ),
            mcq(
                "biet",
                r"Để biểu diễn một lực trên hình vẽ bằng một mũi tên, gốc của mũi tên cho biết yếu tố nào của lực?",
                [
                    r"Điểm đặt của lực tác dụng lên vật.",
                    r"Độ lớn của lực.",
                    r"Phương của lực.",
                    r"Chiều của lực.",
                ],
                0,
                r"Gốc của mũi tên được vẽ tại đúng vị trí mà lực bắt đầu tác dụng lên vật, gọi là **điểm đặt của lực**.",
            ),
            mcq(
                "hieu",
                r"Một học sinh biểu diễn lực kéo $F = 45\text{ N}$ bằng một mũi tên dài $3\text{ cm}$. Tỉ xích mà học sinh đó đã chọn là $1\text{ cm}$ ứng với bao nhiêu niutơn ($\text{N}$)?",
                [
                    r"$15\text{ N}$.",
                    r"$45\text{ N}$.",
                    r"$3\text{ N}$.",
                    r"$135\text{ N}$.",
                ],
                0,
                r"Mũi tên dài $3\text{ cm}$ biểu diễn lực $45\text{ N}$ nên mỗi $1\text{ cm}$ ứng với $\Delta F_0 = \dfrac{45\text{ N}}{3} = 15\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Một lò xo treo thẳng đứng có chiều dài tự nhiên $l_0 = 10\text{ cm}$. Khi treo một quả nặng $50\text{ g}$ vào lò xo thì lò xo có chiều dài $12\text{ cm}$. Nếu treo đồng thời $3$ quả nặng như thế (tổng khối lượng $150\text{ g}$) vào lò xo thì chiều dài của lò xo là:",
                [
                    r"$16\text{ cm}$.",
                    r"$36\text{ cm}$.",
                    r"$14\text{ cm}$.",
                    r"$6\text{ cm}$.",
                ],
                0,
                r"Khi treo $1$ quả nặng $50\text{ g}$, độ dãn của lò xo là $\Delta l_1 = 12 - 10 = 2\text{ cm}$. Khi treo $3$ quả nặng, độ dãn tăng gấp $3$ lần: $\Delta l_3 = 3 \cdot 2 = 6\text{ cm}$. Vậy chiều dài của lò xo là $l_3 = l_0 + \Delta l_3 = 10 + 6 = 16\text{ cm}$.",
            ),
            tf4(
                "hieu",
                r"Xét các đặc điểm của lực và cách biểu diễn lực. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Khi xe đạp đang xuống dốc mà người lái bóp phanh làm xe chạy chậm dần thì lực hãm phanh đã làm biến đổi chuyển động của xe.",
                    r"b) Lực hút của Trái Đất tác dụng lên chiếc máy bay đang bay trên bầu trời là lực tiếp xúc.",
                    r"c) Với tỉ xích $1\text{ cm}$ ứng với $20\text{ N}$, để biểu diễn lực kéo có độ lớn $80\text{ N}$ thì cần vẽ mũi tên có chiều dài $4\text{ cm}$.",
                    r"d) Khi kéo lò xo bằng một lực quá lớn vượt quá giới hạn đàn hồi, lò xo vẫn luôn tự trở về đúng chiều dài tự nhiên ban đầu khi thôi kéo.",
                ],
                [True, False, True, False],
                r"a) Đúng vì tốc độ của xe giảm đi nên chuyển động của xe bị biến đổi." "\n"
                r"b) Sai vì Trái Đất hút máy bay đang bay trên không mà không cần chạm vào máy bay nên đó là lực không tiếp xúc." "\n"
                r"c) Đúng vì số đoạn $1\text{ cm}$ cần vẽ là $\dfrac{80}{20} = 4\text{ cm}$." "\n"
                r"d) Sai vì khi vượt quá giới hạn đàn hồi, lò xo bị biến dạng dẻo (hỏng tính đàn hồi) và không thể tự trở về chiều dài tự nhiên ban đầu.",
            ),
            tf4(
                "hieu",
                r"Một lò xo treo thẳng đứng có chiều dài tự nhiên $l_0 = 15\text{ cm}$. Khi treo quả nặng $m_1 = 200\text{ g}$ thì lò xo dài $19\text{ cm}$. Giả sử lò xo luôn ở trong giới hạn đàn hồi. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Độ dãn của lò xo khi treo quả nặng $200\text{ g}$ là $\Delta l_1 = 4\text{ cm}$.",
                    r"b) Khi treo quả nặng $m_2 = 100\text{ g}$ thì độ dãn của lò xo là $2\text{ cm}$.",
                    r"c) Khi treo quả nặng $m_3 = 400\text{ g}$ thì chiều dài của lò xo là $38\text{ cm}$.",
                    r"d) Để lò xo có chiều dài $21\text{ cm}$ thì cần treo vào lò xo quả nặng có khối lượng $300\text{ g}$.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $\Delta l_1 = l_1 - l_0 = 19 - 15 = 4\text{ cm}$." "\n"
                r"b) Đúng vì $m_2 = 100\text{ g} = \dfrac{1}{2} m_1$ nên $\Delta l_2 = \dfrac{1}{2} \cdot 4 = 2\text{ cm}$." "\n"
                r"c) Sai vì khi treo $m_3 = 400\text{ g} = 2 m_1$, độ dãn tăng gấp đôi ($\Delta l_3 = 2 \cdot 4 = 8\text{ cm}$) nên chiều dài là $l_3 = 15 + 8 = 23\text{ cm}$ (không nhân đôi cả chiều dài $19\text{ cm}$)." "\n"
                r"d) Đúng vì khi $l = 21\text{ cm}$ thì độ dãn $\Delta l = 21 - 15 = 6\text{ cm}$; mà cứ $100\text{ g}$ làm lò xo dãn $2\text{ cm}$ nên $6\text{ cm}$ ứng với $300\text{ g}$.",
            ),
            mcq(
                "vandung",
                r"Treo thẳng đứng một lò xo, khi móc quả nặng $m_1 = 100\text{ g}$ thì lò xo dài $l_1 = 18\text{ cm}$; khi móc quả nặng $m_2 = 250\text{ g}$ thì lò xo dài $l_2 = 21\text{ cm}$. Chiều dài tự nhiên ban đầu $l_0$ của lò xo khi chưa treo vật là:",
                [
                    r"$16\text{ cm}$.",
                    r"$15\text{ cm}$.",
                    r"$14\text{ cm}$.",
                    r"$17\text{ cm}$.",
                ],
                0,
                r"Khi khối lượng vật treo tăng thêm $\Delta m = 250 - 100 = 150\text{ g}$ thì lò xo dãn thêm $21 - 18 = 3\text{ cm}$. Vậy cứ $50\text{ g}$ làm lò xo dãn $1\text{ cm}$, suy ra quả nặng $m_1 = 100\text{ g}$ đã làm lò xo dãn $\Delta l_1 = 2\text{ cm}$. Chiều dài tự nhiên của lò xo là $l_0 = l_1 - \Delta l_1 = 18 - 2 = 16\text{ cm}$.",
            ),
            short(
                "vandung",
                r"Một lò xo có chiều dài tự nhiên $l_0 = 20\text{ cm}$. Khi treo vật có trọng lượng $P_1 = 2\text{ N}$ thì lò xo dài $24\text{ cm}$. Nếu treo một vật khác làm lò xo có chiều dài $l_2 = 30\text{ cm}$ thì vật đó có trọng lượng bằng bao nhiêu niutơn ($\text{N}$)?",
                ["5", "5,0", "5.0"],
                r"Khi treo $P_1 = 2\text{ N}$, độ dãn là $\Delta l_1 = 24 - 20 = 4\text{ cm}$ (mỗi $1\text{ N}$ làm lò xo dãn $2\text{ cm}$). Khi $l_2 = 30\text{ cm}$, độ dãn là $\Delta l_2 = 30 - 20 = 10\text{ cm}$. Vậy trọng lượng của vật là $P_2 = \dfrac{10}{2} = 5\text{ N}$.",
            ),
        ],
    },
    {
        "topic": "trong-luong-va-nang-luong",
        "title": "Trọng lực, Trọng lượng và Năng lượng trong cuộc sống",
        "icon": "🌍",
        "description": "Chương VIII và Chương IX · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 153–155 và tr. 162–179): Bài 43 và Bài 46 – Bài 51. Lực hấp dẫn, trọng lực và công thức tính trọng lượng theo khối lượng; năng lượng và sự truyền năng lượng, các dạng năng lượng, định luật bảo toàn và chuyển hóa năng lượng, năng lượng hao phí, năng lượng tái tạo và tiết kiệm năng lượng.",
        "requirements": [
            r"Nêu được khái niệm khối lượng (số đo lượng chất của một vật) và lực hấp dẫn (lực hút giữa các vật có khối lượng); nêu được trọng lực là lực hút của Trái Đất tác dụng lên vật và trọng lượng là độ lớn của trọng lực.",
            r"Xác định được phương thẳng đứng, chiều từ trên xuống dưới của trọng lực và vận dụng được hệ thức $P = 10m$ để tính trọng lượng từ khối lượng (và ngược lại).",
            r"Lấy được ví dụ chứng tỏ năng lượng đặc trưng cho khả năng tác dụng lực và nhận biết được các dạng năng lượng thông dụng (động năng, thế năng hấp dẫn, thế năng đàn hồi, quang năng, nhiệt năng, điện năng, hoá năng, năng lượng âm).",
            r"Phát biểu và vận dụng được Định luật bảo toàn và chuyển hoá năng lượng; nhận biết được năng lượng có ích và năng lượng hao phí (thường dưới dạng nhiệt năng).",
            r"Phân biệt được nguồn năng lượng tái tạo và không tái tạo; đề xuất được các biện pháp tiết kiệm năng lượng trong gia đình và nhà trường.",
        ],
        "definition": (
            r"- **Lực hấp dẫn** là lực hút giữa mọi vật có khối lượng trong vũ trụ. **Trọng lực** là lực hấp dẫn của Trái Đất tác dụng lên một vật (có phương **thẳng đứng**, chiều **từ trên xuống dưới** hướng về tâm Trái Đất). **Trọng lượng** (kí hiệu $P$, đơn vị $\text{N}$) là độ lớn của trọng lực tác dụng lên vật: $P \approx 10m$ (với $m$ tính bằng $\text{kg}$)." "\n"
            r"- **Năng lượng** đặc trưng cho khả năng tác dụng lực (đơn vị trong hệ SI là **jun**, kí hiệu $\text{J}$). Năng lượng có thể truyền từ vật này sang vật khác hoặc chuyển hoá từ dạng này sang dạng khác." "\n"
            r"- **Định luật bảo toàn năng lượng**: Năng lượng không tự nhiên sinh ra cũng không tự nhiên mất đi; nó chỉ truyền từ vật này sang vật khác hoặc chuyển hoá từ dạng này sang dạng khác."
        ),
        "theory": (
            r"### Bài 43. Trọng lượng, lực hấp dẫn" "\n"
            r"- **Sự khác nhau giữa khối lượng và trọng lượng**: Khối lượng $m$ ($\text{kg}$) là lượng chất tạo nên vật, không thay đổi khi đưa vật tới vị trí khác (như lên Mặt Trăng hay ngoài vũ trụ). Trọng lượng $P$ ($\text{N}$) là độ lớn lực hút của thiên thể lên vật nên thay đổi theo vị trí (trên Mặt Trăng trọng lượng của vật chỉ bằng khoảng $\dfrac{1}{6}$ trọng lượng trên Trái Đất)." "\n"
            r"- Ở gần mặt đất, vật có khối lượng $100\text{ g} = 0{,}1\text{ kg}$ chịu trọng lực có độ lớn khoảng $1\text{ N}$, vật có khối lượng $1\text{ kg}$ có trọng lượng $P \approx 10\text{ N}$." "\n"
            r"### Bài 46. Năng lượng và sự truyền năng lượng" "\n"
            r"- Mọi hoạt động sống và vận hành máy móc đều cần năng lượng. Khi vật $A$ tác dụng lực lên vật $B$ làm vật $B$ chuyển động hoặc biến dạng, năng lượng đã truyền từ vật $A$ sang vật $B$; lực càng lớn và thời gian tác dụng càng dài thì năng lượng truyền càng nhiều." "\n"
            r"### Bài 47. Một số dạng năng lượng" "\n"
            r"- **Theo nguồn phát và tính chất**: Động năng (do vật chuyển động mà có), thế năng hấp dẫn (do vật ở độ cao so với mặt đất), thế năng đàn hồi (do vật bị biến dạng đàn hồi như lò xo, dây cao su), cơ năng (tổng động năng và thế năng), nhiệt năng, quang năng (năng lượng ánh sáng), năng lượng âm, điện năng, hoá năng (dự trữ trong lương thực, thực phẩm, pin, ắc quy, nhiên liệu), năng lượng hạt nhân." "\n"
            r"### Bài 48. Sự chuyển hoá năng lượng" "\n"
            r"- Trong các quá trình tự nhiên và kỹ thuật, các dạng năng lượng luôn chuyển hoá lẫn nhau (ví dụ: bóng đèn điện chuyển hoá **điện năng** thành **quang năng** và **nhiệt năng**; quả bóng rơi từ trên cao chuyển hoá **thế năng hấp dẫn** thành **động năng**) nhưng tổng năng lượng toàn phần luôn được bảo toàn." "\n"
            r"### Bài 49. Năng lượng hao phí" "\n"
            r"- Khi sử dụng năng lượng vào một mục đích nhất định, luôn có một phần biến thành **năng lượng có ích** và một phần biến thành **năng lượng hao phí** (thường toả ra môi trường dưới dạng **nhiệt năng** và năng lượng âm do ma sát, điện trở)." "\n"
            r"### Bài 50. Năng lượng tái tạo" "\n"
            r"- **Năng lượng tái tạo** là nguồn năng lượng có sẵn trong tự nhiên, liên tục được bổ sung và coi như vô tận: năng lượng Mặt Trời, năng lượng gió, năng lượng nước (thuỷ điện), năng lượng địa nhiệt, năng lượng sinh khối, năng lượng thuỷ triều." "\n"
            r"- **Năng lượng không tái tạo** (nhiên liệu hoá thạch như than đá, dầu mỏ, khí đốt tự nhiên và nhiên liệu hạt nhân) mất hàng triệu năm mới hình thành, sẽ cạn kiệt và gây phát thải khí nhà kính khi đốt cháy." "\n"
            r"### Bài 51. Tiết kiệm năng lượng" "\n"
            r"- Tiết kiệm năng lượng giúp giảm chi phí kinh tế, bảo tồn tài nguyên thiên nhiên và giảm ô nhiễm môi trường (ví dụ: tắt thiết bị điện khi không sử dụng, dùng bóng đèn LED thay đèn sợi đốt, tận dụng ánh sáng và gió tự nhiên)."
        ),
        "formulas": [
            G(
                "I. Trọng lượng và Khối lượng (trên Trái Đất)",
                F("Công thức tính trọng lượng", r"$P = 10m$", r"$m$ là khối lượng ($\text{kg}$), $P$ là trọng lượng ($\text{N}$)."),
                F("Tính khối lượng từ trọng lượng", r"$m = \dfrac{P}{10}$", r"Ví dụ vật có $P = 45\text{ N}$ thì có khối lượng $m = 4{,}5\text{ kg}$."),
                F("Trọng lượng trên Mặt Trăng", r"$P_{\text{Mặt Trăng}} \approx \dfrac{1}{6} P_{\text{Trái Đất}}$", r"Khối lượng $m$ không đổi nhưng trọng lượng giảm $6$ lần."),
            ),
            G(
                "II. Bảo toàn năng lượng & Hiệu suất",
                F("Định luật bảo toàn năng lượng", r"$W_{\text{toàn phần}} = W_{\text{có ích}} + W_{\text{hao phí}}$", r"Đơn vị năng lượng là jun ($\text{J}$) hoặc ki-lô-jun ($1\text{ kJ} = 1000\text{ J}$)."),
                F("Phần trăm năng lượng có ích (Hiệu suất)", r"$H = \dfrac{W_{\text{có ích}}}{W_{\text{toàn phần}}} \cdot 100\%$"),
            ),
        ],
        "example": (
            r"a) Một bao gạo có khối lượng $m = 25\text{ kg}$. Tính trọng lượng $P$ của bao gạo đó trên Trái Đất." "\n"
            r"b) Một bóng đèn sợi đốt tiêu thụ $100\text{ J}$ điện năng mỗi giây, trong đó có $90\text{ J}$ chuyển hoá thành nhiệt năng toả ra môi trường và phần còn lại chuyển hoá thành quang năng (ánh sáng). Tính phần năng lượng có ích (quang năng) và tỉ lệ phần trăm điện năng chuyển hoá thành quang năng."
        ),
        "example_answer": (
            r"a) Trọng lượng của bao gạo trên Trái Đất là: $P = 10m = 10 \cdot 25 = 250\text{ N}$." "\n"
            r"b) Theo định luật bảo toàn năng lượng, năng lượng ánh sáng có ích mỗi giây là: $W_{\text{có ích}} = W_{\text{toàn phần}} - W_{\text{hao phí}} = 100 - 90 = 10\text{ J}$." "\n"
            r"Tỉ lệ phần trăm điện năng biến thành quang năng là: $H = \dfrac{10}{100} \cdot 100\% = 10\%$."
        ),
        "real_life": (
            r"- Dây dọi của thợ xây gồm một quả nặng treo vào sợi dây mềm: dưới tác dụng của trọng lực có phương thẳng đứng, dây dọi giúp thợ xây kiểm tra xem bức tường xây có thẳng đứng hay không." "\n"
            r"- Việc thay thế bóng đèn sợi đốt (hao phí tới $90\%$ nhiệt năng) bằng bóng đèn LED (chuyển hoá trên $80\%$ điện năng thành quang năng) giúp tiết kiệm điện năng rõ rệt."
        ),
        "game_title": "Khám phá Trọng lực và Chuyển hóa Năng lượng",
        "game_description": "Đo trọng lượng vật ở các hành tinh khác nhau và lắp ghép các sơ đồ chuyển hóa năng lượng, tính hiệu suất và năng lượng có ích trong thực tiễn.",
        "game_type": "game_trong_luong_nang_luong",
        "quiz": [
            mcq(
                "biet",
                r"Trọng lực tác dụng lên một vật ở gần mặt đất có phương và chiều như thế nào?",
                [
                    r"Phương thẳng đứng, chiều từ trên xuống dưới.",
                    r"Phương thẳng đứng, chiều từ dưới lên trên.",
                    r"Phương nằm ngang, chiều từ trái sang phải.",
                    r"Phương xiên góc $45^\circ$ so với mặt đất.",
                ],
                0,
                r"Trọng lực là lực hút của Trái Đất tác dụng lên vật, có **phương thẳng đứng** và **chiều từ trên xuống dưới** (hướng về tâm Trái Đất).",
            ),
            mcq(
                "biet",
                r"Dạng năng lượng được dự trữ trong lương thực, thực phẩm, pin, ắc quy và xăng dầu được gọi là:",
                [
                    r"Hoá năng.",
                    r"Động năng.",
                    r"Quang năng.",
                    r"Thế năng đàn hồi.",
                ],
                0,
                r"Năng lượng dự trữ trong các liên kết hoá học của lương thực, thực phẩm, nhiên liệu và pin được gọi là **hoá năng**.",
            ),
            mcq(
                "biet",
                r"Nguồn năng lượng nào sau đây thuộc nhóm **năng lượng tái tạo**?",
                [
                    r"Năng lượng gió và năng lượng Mặt Trời.",
                    r"Than đá và dầu mỏ.",
                    r"Khí đốt tự nhiên.",
                    r"Xăng và dầu diesel.",
                ],
                0,
                r"Năng lượng gió và năng lượng Mặt Trời có sẵn trong tự nhiên, liên tục được bổ sung nên thuộc nhóm **năng lượng tái tạo**; than đá, dầu mỏ, khí đốt là nhiên liệu hoá thạch không tái tạo.",
            ),
            mcq(
                "biet",
                r"Khi quạt điện đang hoạt động, phần năng lượng hao phí chủ yếu xuất hiện dưới dạng nào?",
                [
                    r"Nhiệt năng làm nóng động cơ quạt.",
                    r"Động năng làm quay cánh quạt.",
                    r"Hoá năng dự trữ trong cánh quạt.",
                    r"Thế năng hấp dẫn của chiếc quạt.",
                ],
                0,
                r"Mục đích dùng quạt là tạo gió (động năng là năng lượng có ích), còn phần điện năng làm nóng động cơ quạt là **nhiệt năng hao phí**.",
            ),
            mcq(
                "hieu",
                r"Một kiện hàng có khối lượng $m = 3{,}5\text{ kg}$ đặt trên mặt đất. Trọng lượng $P$ của kiện hàng đó bằng bao nhiêu niutơn ($\text{N}$)?",
                [
                    r"$35\text{ N}$.",
                    r"$3{,}5\text{ N}$.",
                    r"$350\text{ N}$.",
                    r"$0{,}35\text{ N}$.",
                ],
                0,
                r"Áp dụng hệ thức liên hệ giữa trọng lượng và khối lượng: $P = 10m = 10 \cdot 3{,}5 = 35\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Một chiếc ô tô sử dụng động cơ xăng tiêu thụ một phần hoá năng của nhiên liệu là $100\text{ kJ}$, nhưng chỉ có $30\text{ kJ}$ biến thành cơ năng có ích giúp xe chuyển động. Phần năng lượng hao phí toả ra môi trường là:",
                [
                    r"$70\text{ kJ}$.",
                    r"$130\text{ kJ}$.",
                    r"$30\text{ kJ}$.",
                    r"$100\text{ kJ}$.",
                ],
                0,
                r"Theo định luật bảo toàn năng lượng: $W_{\text{hao phí}} = W_{\text{toàn phần}} - W_{\text{có ích}} = 100 - 30 = 70\text{ kJ}$.",
            ),
            tf4(
                "hieu",
                r"Xét một nhà du hành vũ trụ có khối lượng cơ thể cùng bộ đồ bảo hộ là $90\text{ kg}$ khi ở trên Trái Đất và khi đặt chân lên Mặt Trăng (biết lực hút của Mặt Trăng bằng $\dfrac{1}{6}$ lực hút của Trái Đất). Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Trên Trái Đất, trọng lượng của nhà du hành cùng bộ đồ bảo hộ là $900\text{ N}$.",
                    r"b) Khi lên tới Mặt Trăng, khối lượng của nhà du hành cùng bộ đồ giảm đi $6$ lần, chỉ còn $15\text{ kg}$.",
                    r"c) Trên Mặt Trăng, trọng lượng của nhà du hành cùng bộ đồ bảo hộ là khoảng $150\text{ N}$.",
                    r"d) Lực hút giữa Trái Đất và Mặt Trăng là lực hấp dẫn và thuộc loại lực không tiếp xúc.",
                ],
                [True, False, True, True],
                r"a) Đúng vì trên Trái Đất $P = 10m = 10 \cdot 90 = 900\text{ N}$." "\n"
                r"b) Sai vì khối lượng chỉ lượng chất tạo nên vật nên **không thay đổi** theo vị trí, trên Mặt Trăng vẫn là $90\text{ kg}$." "\n"
                r"c) Đúng vì trên Mặt Trăng trọng lượng bằng $\dfrac{1}{6}$ trên Trái Đất: $P_{\text{Mặt Trăng}} = \dfrac{900}{6} = 150\text{ N}$." "\n"
                r"d) Đúng vì lực hấp dẫn tác dụng qua không gian vũ trụ mà không cần tiếp xúc.",
            ),
            tf4(
                "hieu",
                r"Xét các quá trình chuyển hoá và bảo toàn năng lượng trong đời sống. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) Khi dùng bàn là (bàn ủi) điện để là quần áo, điện năng chuyển hoá chủ yếu thành nhiệt năng là năng lượng có ích.",
                    r"b) Khi quả bóng cao su rơi từ trên cao xuống đất, thế năng hấp dẫn giảm dần và chuyển hoá thành động năng tăng dần.",
                    r"c) Pin mặt trời (quang điện) chuyển hoá trực tiếp quang năng của ánh sáng Mặt Trời thành điện năng.",
                    r"d) Năng lượng hao phí bị biến mất hoàn toàn nên định luật bảo toàn năng lượng không còn đúng khi có ma sát.",
                ],
                [True, True, True, False],
                r"a) Đúng vì mục đích của bàn là điện là tạo nhiệt để làm phẳng quần áo nên nhiệt năng ở đây là năng lượng có ích." "\n"
                r"b) Đúng vì độ cao giảm làm thế năng hấp dẫn giảm, tốc độ tăng làm động năng tăng." "\n"
                r"c) Đúng vì pin mặt trời biến đổi trực tiếp quang năng thành điện năng." "\n"
                r"d) Sai vì năng lượng hao phí không biến mất mà chỉ chuyển thành nhiệt năng truyền cho các vật xung quanh và môi trường; tổng năng lượng toàn phần luôn bảo toàn.",
            ),
            mcq(
                "vandung",
                r"Treo một túi hoa quả vào móc của một lực kế lò xo được giữ thẳng đứng thì khi túi hoa quả đứng yên, kim lực kế chỉ vạch $24\text{ N}$. Biết vỏ túi nilon có khối lượng không đáng kể. Khối lượng của số hoa quả trong túi tính theo đơn vị gam ($\text{g}$) là:",
                [
                    r"$2400\text{ g}$.",
                    r"$240\text{ g}$.",
                    r"$2{,}4\text{ g}$.",
                    r"$24\,000\text{ g}$.",
                ],
                0,
                r"Số chỉ của lực kế bằng trọng lượng của túi hoa quả: $P = 24\text{ N}$. Suy ra khối lượng hoa quả là $m = \dfrac{P}{10} = \dfrac{24}{10} = 2{,}4\text{ kg} = 2400\text{ g}$.",
            ),
            short(
                "vandung",
                r"Một bóng đèn LED tiêu thụ $200\text{ J}$ điện năng, trong đó phần năng lượng hao phí toả nhiệt ra môi trường là $30\text{ J}$, phần còn lại chuyển hoá thành quang năng có ích. Tính hiệu suất chuyển hoá điện năng thành quang năng của bóng đèn LED theo đơn vị phần trăm ($\%$).",
                ["85", "85,0", "85.0"],
                r"Quang năng có ích là $W_{\text{có ích}} = 200 - 30 = 170\text{ J}$. Hiệu suất chuyển hoá là $H = \dfrac{170}{200} \cdot 100\% = 85\%$.",
            ),
        ],
    },
    {
        "topic": "luc-ma-sat",
        "title": "Lực ma sát và Lực cản của môi trường",
        "icon": "🛞",
        "description": "Chương VIII · SGK Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (tr. 156–161): Bài 44 – Bài 45. Khái niệm lực ma sát nghỉ và lực ma sát trượt, nguyên nhân xuất hiện lực ma sát, tác dụng cản trở hoặc thúc đẩy chuyển động của lực ma sát và ứng dụng trong an toàn giao thông; lực cản của nước và không khí phụ thuộc vào diện tích mặt cản.",
        "requirements": [
            r"Nêu được lực ma sát là lực tiếp xúc xuất hiện ở bề mặt tiếp xúc giữa hai vật; sự tương tác giữa bề mặt của hai vật tạo ra lực ma sát giữa chúng.",
            r"Phân biệt được lực ma sát trượt (xuất hiện khi một vật trượt trên bề mặt vật khác) và lực ma sát nghỉ (giữ cho vật đứng yên khi vật bị tác dụng của lực khác).",
            r"Trình bày được tác dụng cản trở và tác dụng thúc đẩy chuyển động của lực ma sát; lấy được ví dụ về một số ảnh hưởng của lực ma sát trong an toàn giao thông đường bộ.",
            r"Thực hiện được thí nghiệm chứng tỏ vật chuyển động trong nước (hoặc không khí) chịu tác dụng của lực cản; nêu được lực cản phụ thuộc vào diện tích mặt cản và hình dạng của vật.",
        ],
        "definition": (
            r"- **Lực ma sát** là lực tiếp xúc xuất hiện ở bề mặt tiếp xúc giữa hai vật, có chiều **ngược với chiều chuyển động** (hoặc ngược với chiều của ngoại lực có xu hướng làm vật chuyển động)." "\n"
            r"- **Lực ma sát nghỉ** giữ cho vật đứng yên khi vật chịu tác dụng của một lực khác có xu hướng làm vật trượt trên bề mặt. **Lực ma sát trượt** xuất hiện khi một vật trượt trên bề mặt của một vật khác." "\n"
            r"- **Lực cản của nước (hoặc không khí)** là lực tác dụng lên mọi vật chuyển động trong nước (hoặc không khí), luôn ngược hướng chuyển động và cản trở chuyển động của vật."
        ),
        "theory": (
            r"### Bài 44. Lực ma sát" "\n"
            r"- **Nguyên nhân xuất hiện lực ma sát**: Do bề mặt của các vật dù có vẻ nhẵn nhưng khi phóng đại lên vẫn có những chỗ lồi lõm, gồ ghề; sự tương tác giữa hai bề mặt tiếp xúc tạo ra lực ma sát. Bề mặt càng gồ ghề (nhám) và áp lực ép vuông góc lên mặt tiếp xúc càng lớn thì lực ma sát càng lớn." "\n"
            r"- **Thí nghiệm đo lực ma sát bằng lực kế**:" "\n"
            r"  + Khi kéo lực kế với lực nhỏ $F_{\text{kéo}}$ mà khối gỗ vẫn đứng yên thì lực ma sát nghỉ cân bằng với lực kéo: $F_{\text{msn}} = F_{\text{kéo}}$." "\n"
            r"  + Khi khối gỗ trượt đều trên mặt bàn nằm ngang thì độ lớn lực ma sát trượt bằng số chỉ của lực kế: $F_{\text{mst}} = F_{\text{kéo}}$." "\n"
            r"- **Hai mặt lợi và hại của lực ma sát**:" "\n"
            r"  + *Tác dụng có hại (cản trở chuyển động)*: Làm mòn chi tiết máy, ổ trục, đế giày, lốp xe và gây hao phí năng lượng. Cách giảm ma sát: tra dầu mỡ bôi trơn, mài nhẵn bề mặt, thay ma sát trượt bằng ma sát lăn (dùng ổ bi, con lăn, bánh xe)." "\n"
            r"  + *Tác dụng có ích (giữ vật và thúc đẩy chuyển động)*: Lực ma sát nghỉ giúp tay cầm nắm được đồ vật, giúp đinh giữ chặt trong tường, giúp bàn chân và bánh xe bám vào mặt đường để đẩy người và xe tiến về phía trước. Cách tăng ma sát: xẻ rãnh sâu trên lốp xe và đế giày, rải cát lên đường trơn trượt." "\n"
            r"### Bài 45. Lực cản của nước" "\n"
            r"- Nước và không khí đều tác dụng **lực cản** lên các vật chuyển động trong chúng. Lực cản của nước lớn hơn rất nhiều so với lực cản của không khí (vì thế đi bộ dưới nước khó và chậm hơn đi bộ trên cạn)." "\n"
            r"- **Các yếu tố ảnh hưởng đến lực cản**: Lực cản của nước (và không khí) phụ thuộc vào **diện tích mặt cản** (hình dạng của vật) và tốc độ chuyển động. Diện tích mặt cản càng lớn thì lực cản càng mạnh." "\n"
            r"- **Ứng dụng hình dạng khí động học (thuôn nhọn)**: Cá heo, cá ngừ, tàu ngầm, tàu cao tốc, máy bay, mũ bảo hiểm đua xe đạp đều có phần đầu thuôn nhọn để giảm tối đa lực cản của nước và không khí; ngược lại, dù nhảy có vòm vải diện tích rất lớn để tăng lực cản không khí giúp người nhảy dù hạ cánh an toàn."
        ),
        "formulas": [
            G(
                "I. Cân bằng lực khi có ma sát trên mặt ngang",
                F("Khi vật còn đứng yên (Ma sát nghỉ)", r"$F_{\text{msn}} = F_{\text{kéo}} \le F_{\text{msn cực đại}}$", r"Lực ma sát nghỉ tự điều chỉnh bằng lực kéo cho đến khi vật bắt đầu trượt."),
                F("Khi vật trượt đều (Ma sát trượt)", r"$F_{\text{mst}} = F_{\text{kéo}}$", r"Số chỉ của lực kế khi kéo vật trượt đều chính là độ lớn lực ma sát trượt."),
            ),
            G(
                "II. Quy luật phụ thuộc của lực ma sát và lực cản",
                F("So sánh các loại ma sát cùng điều kiện", r"$F_{\text{ms lăn}} \ll F_{\text{ms trượt}}$", r"Sử dụng ổ bi, bánh xe giúp giảm lực ma sát đi rất nhiều lần."),
                F("Sự phụ thuộc vào diện tích mặt cản", r"$S_{\text{mặt cản}} \text{ càng lớn} \Rightarrow F_{\text{cản}} \text{ càng lớn}$", r"Đầu thuôn nhọn giúp giảm diện tích mặt cản hiệu dụng."),
            ),
        ],
        "example": (
            r"Đặt một khúc gỗ lên mặt bàn nằm ngang rồi móc vào một lực kế. Khi kéo lực kế theo phương ngang với lực $F_1 = 1{,}5\text{ N}$ thì khúc gỗ vẫn đứng yên. Khi tăng lực kéo và giữ cho khúc gỗ trượt thẳng đều trên mặt bàn thì lực kế chỉ $F_2 = 3{,}2\text{ N}$. Hãy xác định loại lực ma sát và độ lớn của lực ma sát tác dụng lên khúc gỗ trong hai trường hợp trên."
        ),
        "example_answer": (
            r"- **Trường hợp 1 ($F_1 = 1{,}5\text{ N}$)**: Vì khúc gỗ vẫn đứng yên nên lực ma sát xuất hiện là **lực ma sát nghỉ**, cân bằng với lực kéo: $F_{\text{msn}} = F_1 = 1{,}5\text{ N}$." "\n"
            r"- **Trường hợp 2 ($F_2 = 3{,}2\text{ N}$)**: Vì khúc gỗ trượt thẳng đều trên mặt bàn nên lực ma sát xuất hiện là **lực ma sát trượt**, có độ lớn bằng lực kéo: $F_{\text{mst}} = F_2 = 3{,}2\text{ N}$."
        ),
        "real_life": (
            r"- Lốp xe máy, ô tô luôn có các rãnh khía sâu để thoát nước và tăng lực ma sát bám đường; khi lốp xe bị mòn nhẵn mà đi dưới trời mưa rất dễ bị trượt ngã hoặc mất lái khi phanh gấp." "\n"
            r"- Vận động viên bơi lội luôn khép sát hai tay vươn thẳng về phía trước khi lướt nước và đội mũ bơi bó sát đầu để giảm lực cản của nước."
        ),
        "game_title": "Thử nghiệm Lực ma sát và Lực cản của nước",
        "game_description": "Kéo khúc gỗ trên các bề mặt có độ nhám khác nhau bằng lực kế và khảo sát lực cản của nước, không khí lên các vật có hình dạng khí động học khác nhau.",
        "game_type": "game_lucmasat",
        "quiz": [
            mcq(
                "biet",
                r"Khi một vận động viên trượt ván đang trượt trên mặt sàn bê tông thì giữa bánh ván trượt bị kẹt cứng (trượt lê) và mặt sàn xuất hiện loại lực ma sát nào?",
                [
                    r"Lực ma sát trượt.",
                    r"Lực ma sát nghỉ.",
                    r"Lực hấp dẫn.",
                    r"Lực đàn hồi.",
                ],
                0,
                r"Khi một vật trượt trên bề mặt của vật khác thì ở mặt tiếp xúc xuất hiện **lực ma sát trượt**.",
            ),
            mcq(
                "biet",
                r"Nhờ có lực nào mà ta có thể cầm nắm chắc chiếc bút trong tay hoặc đặt một thùng hàng đứng yên trên mặt dốc nghiêng mà không bị trượt xuống?",
                [
                    r"Lực ma sát nghỉ.",
                    r"Lực ma sát trượt.",
                    r"Lực cản của không khí.",
                    r"Lực cản của nước.",
                ],
                0,
                r"**Lực ma sát nghỉ** giữ cho vật không bị trượt khi vật chịu tác dụng của lực khác (như trọng lực kéo xuống dốc hoặc trọng lực kéo chiếc bút tuột khỏi tay).",
            ),
            mcq(
                "biet",
                r"Tại sao thân cá, tàu ngầm và tàu cao tốc đều được cấu tạo hoặc thiết kế có phần đầu thuôn nhọn?",
                [
                    r"Để giảm lực cản của nước và không khí khi chuyển động.",
                    r"Để làm tăng lực ma sát trượt với môi trường.",
                    r"Để làm tăng khối lượng của tàu ngầm và tàu cao tốc.",
                    r"Để loại bỏ hoàn toàn lực hút của Trái Đất.",
                ],
                0,
                r"Hình dạng thuôn nhọn (khí động học) giúp thu nhỏ diện tích mặt cản trực diện, từ đó **giảm tối đa lực cản của nước và không khí**.",
            ),
            mcq(
                "biet",
                r"Biện pháp nào sau đây giúp **giảm lực ma sát** có hại trong các ổ trục máy móc và xe đạp?",
                [
                    r"Lắp ổ bi (vòng bi) và tra dầu mỡ bôi trơn định kì.",
                    r"Rải thêm cát mịn vào bên trong ổ trục.",
                    r"Khía thật nhiều rãnh nhám lên bề mặt trục quay.",
                    r"Tăng khối lượng đè lên trục quay.",
                ],
                0,
                r"Lắp ổ bi giúp thay ma sát trượt bằng ma sát lăn nhỏ hơn rất nhiều, kết hợp tra dầu mỡ làm trơn bề mặt tiếp xúc.",
            ),
            mcq(
                "hieu",
                r"Một học sinh dùng tay đẩy ngang một chiếc tủ gỗ nặng với lực $F = 60\text{ N}$ nhưng chiếc tủ vẫn đứng yên trên sàn nhà. Độ lớn của lực ma sát nghỉ do sàn nhà tác dụng lên chân tủ khi đó bằng:",
                [
                    r"$60\text{ N}$.",
                    r"$0\text{ N}$.",
                    r"Lớn hơn $60\text{ N}$.",
                    r"Nhỏ hơn $60\text{ N}$.",
                ],
                0,
                r"Khi chiếc tủ vẫn đứng yên dưới tác dụng của lực đẩy ngang $60\text{ N}$ thì lực ma sát nghỉ cân bằng với lực đẩy, nên $F_{\text{msn}} = 60\text{ N}$.",
            ),
            mcq(
                "hieu",
                r"Thả hai tờ giấy giống hệt nhau từ cùng một độ cao trong không khí: tờ thứ nhất để phẳng nguyên vẹn, tờ thứ hai vo tròn chặt lại. Hiện tượng nào xảy ra?",
                [
                    r"Tờ giấy vo tròn rơi chạm đất nhanh hơn vì có diện tích mặt cản nhỏ hơn nên chịu lực cản không khí nhỏ hơn.",
                    r"Hai tờ giấy chạm đất cùng một lúc vì có khối lượng bằng nhau.",
                    r"Tờ giấy để phẳng chạm đất nhanh hơn vì diện tích lớn hơn.",
                    r"Tờ giấy vo tròn nặng gấp đôi tờ giấy để phẳng nên rơi nhanh hơn.",
                ],
                0,
                r"Hai tờ giấy có cùng khối lượng và cùng trọng lượng, nhưng tờ giấy vo tròn có diện tích mặt cản nhỏ hơn nhiều nên chịu **lực cản không khí nhỏ hơn** và rơi chạm đất nhanh hơn.",
            ),
            tf4(
                "hieu",
                r"Xét vai trò của lực ma sát trong đời sống và giao thông. Mỗi phát biểu sau đây đúng hay sai?",
                [
                    r"a) Các rãnh gai trên mặt lốp ô tô và đế giày thể thao có tác dụng làm tăng lực ma sát với mặt đường để chống trơn trượt.",
                    r"b) Khi bóp phanh xe đạp, má phanh ép sát vào vành bánh xe tạo ra lực ma sát trượt giúp bánh xe quay nhanh hơn.",
                    r"c) Khi quẹt diêm vào vỏ bao diêm, lực ma sát trượt giữa đầu que diêm và mặt nhám của vỏ bao làm tăng nhiệt độ giúp diêm bén lửa.",
                    r"d) Lực ma sát luôn luôn có hại trong mọi trường hợp nên cần loại bỏ hoàn toàn ma sát trên mặt đường giao thông.",
                ],
                [True, False, True, False],
                r"a) Đúng vì rãnh gai tăng độ bám, chống trượt ngã." "\n"
                r"b) Sai vì lực ma sát trượt giữa má phanh và vành bánh xe cản trở chuyển động quay, làm xe **chậm lại và dừng hẳn**." "\n"
                r"c) Đúng vì ma sát trượt chuyển hoá cơ năng thành nhiệt năng làm cháy thuốc diêm." "\n"
                r"d) Sai vì nếu không có ma sát trên mặt đường thì người và phương tiện không thể khởi hành, không thể đi lại và cũng không thể phanh dừng lại được.",
            ),
            tf4(
                "hieu",
                r"Một học sinh dùng lực kế kéo một khối gỗ có gắn móc trượt thẳng đều trên ba bề mặt nằm ngang khác nhau: mặt kính nhẵn (số chỉ $F_1$), mặt gỗ thông thường (số chỉ $F_2$) và mặt giấy nhám (số chỉ $F_3$). Mỗi nhận định sau đúng hay sai?",
                [
                    r"a) Độ lớn lực ma sát trượt trên mặt giấy nhám là lớn nhất ($F_3 > F_2 > F_1$).",
                    r"b) Nếu đặt thêm một quả cân $500\text{ g}$ lên trên khối gỗ rồi kéo trượt đều trên mặt bàn gỗ thì lực ma sát trượt sẽ lớn hơn $F_2$.",
                    r"c) Nếu lót các con lăn (bút chì tròn) dưới đáy khối gỗ rồi kéo đều trên mặt bàn gỗ thì số chỉ lực kế sẽ lớn hơn $F_2$.",
                    r"d) Chiều của lực ma sát trượt tác dụng lên khối gỗ luôn cùng chiều với chiều kéo của lực kế.",
                ],
                [True, True, False, False],
                r"a) Đúng vì bề mặt càng gồ ghề (nhám) thì lực ma sát trượt càng lớn." "\n"
                r"b) Đúng vì đặt thêm quả cân làm tăng áp lực ép lên mặt bàn nên lực ma sát trượt tăng lên." "\n"
                r"c) Sai vì lót con lăn thay ma sát trượt bằng ma sát lăn nên số chỉ lực kế sẽ **nhỏ hơn** $F_2$ rất nhiều." "\n"
                r"d) Sai vì lực ma sát trượt luôn **ngược chiều** với chiều chuyển động trượt của khối gỗ.",
            ),
            mcq(
                "vandung",
                r"Một khối gỗ có khối lượng $m = 800\text{ g}$ được kéo trượt thẳng đều trên mặt sàn nằm ngang bằng một lực kế có phương nằm ngang. Biết độ lớn của lực ma sát trượt bằng $0{,}25$ lần trọng lượng của khối gỗ. Số chỉ của lực kế khi đó là:",
                [
                    r"$2\text{ N}$.",
                    r"$200\text{ N}$.",
                    r"$8\text{ N}$.",
                    r"$0{,}2\text{ N}$.",
                ],
                0,
                r"Đổi $m = 800\text{ g} = 0{,}8\text{ kg}$. Trọng lượng của khối gỗ là $P = 10m = 10 \cdot 0{,}8 = 8\text{ N}$. Khi khối gỗ trượt thẳng đều, số chỉ lực kế bằng lực ma sát trượt: $F_{\text{kéo}} = F_{\text{mst}} = 0{,}25 \cdot 8 = 2\text{ N}$.",
            ),
            short(
                "vandung",
                r"Để kéo một thùng hàng trượt thẳng đều trên sàn phẳng cần lực kéo ngang $F_1 = 45\text{ N}$. Khi người công nhân đặt thùng hàng lên một xe đẩy có bánh xe ổ bi thì lực kéo ngang để xe chuyển động đều giảm đi $9$ lần. Tính độ lớn lực ma sát lăn khi dùng xe đẩy theo đơn vị niutơn ($\text{N}$).",
                ["5", "5,0", "5.0"],
                r"Khi chuyển sang dùng xe đẩy bánh xe ổ bi, lực kéo cân bằng với lực ma sát lăn và giảm đi $9$ lần: $F_{\text{ms lăn}} = \dfrac{45}{9} = 5\text{ N}$.",
            ),
        ],
    },
    {
        "topic": "toc-do",
        "title": "Khái niệm tốc độ cơ bản và Chuyển động cơ học",
        "icon": "🏎️",
        "description": "Chủ đề tích hợp thực nghiệm Khoa học tự nhiên 6 Kết nối tri thức với cuộc sống (vận dụng Bài 5 Đo chiều dài và Bài 7 Đo thời gian, mở đầu cho chủ đề Tốc độ). Cách so sánh sự nhanh chậm của chuyển động qua quãng đường đi được và thời gian chuyển động, công thức tính tốc độ và quy đổi đơn vị tốc độ cơ bản.",
        "requirements": [
            r"Vận dụng được kĩ năng đo chiều dài (Bài 5) và đo thời gian (Bài 7) để xác định độ nhanh chậm của một vật chuyển động trong thực nghiệm.",
            r"Nêu được hai cách so sánh sự nhanh chậm của hai chuyển động: so sánh thời gian đi cùng một quãng đường hoặc so sánh quãng đường đi được trong cùng một đơn vị thời gian.",
            r"Phát biểu được khái niệm tốc độ là đại lượng cho biết quãng đường vật đi được trong một đơn vị thời gian và viết được công thức $v = \dfrac{s}{t}$.",
            r"Nêu được đơn vị đo tốc độ cơ bản trong hệ SI là mét trên giây ($\text{m/s}$), đơn vị thông dụng là ki-lô-mét trên giờ ($\text{km/h}$) và chuyển đổi được giữa hai đơn vị này.",
            r"Vận dụng được công thức $v = \dfrac{s}{t}$, $s = v \cdot t$ và $t = \dfrac{s}{v}$ để giải các bài toán thực tiễn cơ bản.",
        ],
        "definition": (
            r"- **Tốc độ** (kí hiệu là $v$) là đại lượng đặc trưng cho sự nhanh, chậm của chuyển động, được xác định bằng thương số giữa quãng đường đi được $s$ và thời gian $t$ để đi hết quãng đường đó: $v = \dfrac{s}{t}$." "\n"
            r"- Đơn vị đo tốc độ phụ thuộc vào đơn vị đo chiều dài và đơn vị đo thời gian: trong hệ SI là **mét trên giây** ($\text{m/s}$), trong giao thông thường dùng **ki-lô-mét trên giờ** ($\text{km/h}$)." "\n"
            r"- Quy tắc đổi đơn vị tốc độ: $1\text{ m/s} = 3{,}6\text{ km/h}$ và $1\text{ km/h} = \dfrac{1}{3{,}6}\text{ m/s}$."
        ),
        "theory": (
            r"### Bài 5 & Bài 7 (Tích hợp). Đo quãng đường và thời gian chuyển động" "\n"
            r"- Trong thực nghiệm Khoa học tự nhiên, muốn khảo sát chuyển động của một vật (như xe lăn trên máng nghiêng, học sinh chạy trên sân trường), ta kết hợp dùng **thước dây hoặc thước cuộn** (Bài 5) để đo quãng đường $s$ và dùng **đồng hồ bấm giây** (Bài 7) để đo khoảng thời gian chuyển động $t$." "\n"
            r"- **Hai cách so sánh ai chuyển động nhanh hơn**:" "\n"
            r"  + *Cách 1*: Trên cùng một quãng đường $s$, vật nào đi hết thời gian $t$ **ngắn hơn** thì vật đó chuyển động **nhanh hơn**." "\n"
            r"  + *Cách 2*: Trong cùng một khoảng thời gian $t$ (đặc biệt là trong $1\text{ đơn vị thời gian}$ như $1\text{ s}$ hoặc $1\text{ h}$), vật nào đi được quãng đường $s$ **dài hơn** thì vật đó chuyển động **nhanh hơn**." "\n"
            r"### Mở rộng thực nghiệm. Khái niệm tốc độ và đơn vị đo tốc độ cơ bản" "\n"
            r"- Từ công thức gốc $v = \dfrac{s}{t}$, khi biết hai trong ba đại lượng ($s, t, v$), ta luôn suy ra được đại lượng còn lại:" "\n"
            r"  + Tính quãng đường đi được: $s = v \cdot t$." "\n"
            r"  + Tính thời gian chuyển động: $t = \dfrac{s}{v}$." "\n"
            r"- Lưu ý đồng bộ đơn vị trước khi tính: nếu $v$ tính bằng $\text{km/h}$ thì $s$ phải đổi ra $\text{km}$ và $t$ phải đổi ra $\text{h}$; nếu $v$ tính bằng $\text{m/s}$ thì $s$ đổi ra $\text{m}$ và $t$ đổi ra $\text{s}$."
        ),
        "formulas": [
            G(
                "I. Công thức tính tốc độ, quãng đường và thời gian",
                F("Công thức tính tốc độ", r"$v = \dfrac{s}{t}$", r"$s$ là quãng đường đi được, $t$ là thời gian đi hết quãng đường đó."),
                F("Công thức tính quãng đường", r"$s = v \cdot t$"),
                F("Công thức tính thời gian", r"$t = \dfrac{s}{v}$"),
            ),
            G(
                "II. Quy đổi đơn vị tốc độ",
                F(r"Từ $\text{m/s}$ sang $\text{km/h}$", r"$1\text{ m/s} = \dfrac{0{,}001\text{ km}}{\dfrac{1}{3600}\text{ h}} = 3{,}6\text{ km/h}$", r"Nhân số đo $\text{m/s}$ với $3{,}6$."),
                F(r"Từ $\text{km/h}$ sang $\text{m/s}$", r"$1\text{ km/h} = \dfrac{1000\text{ m}}{3600\text{ s}} = \dfrac{1}{3{,}6}\text{ m/s}$", r"Chia số đo $\text{km/h}$ cho $3{,}6$."),
            ),
        ],
        "example": (
            r"Trong giờ thực hành trên sân trường, bạn An dùng thước dây đo được đường chạy dài $s = 60\text{ m}$ và dùng đồng hồ bấm giây đo được thời gian bạn Bình chạy hết quãng đường đó là $t = 12\text{ s}$. Tính tốc độ chạy của bạn Bình ra đơn vị $\text{m/s}$ và $\text{km/h}$."
        ),
        "example_answer": (
            r"- Tốc độ chạy của bạn Bình tính theo đơn vị $\text{m/s}$ là: $v = \dfrac{s}{t} = \dfrac{60}{12} = 5\text{ m/s}$." "\n"
            r"- Đổi sang đơn vị $\text{km/h}$: $v = 5 \cdot 3{,}6 = 18\text{ km/h}$."
        ),
        "real_life": (
            r"- Đồng hồ tốc độ (tốc kế) gắn trên đầu xe máy và bảng điều khiển ô tô cho người lái biết tốc độ tức thời của xe theo đơn vị $\text{km/h}$ để chấp hành biển báo giới hạn tốc độ." "\n"
            r"- Trong thể thao điền kinh, việc đo quãng đường và thời gian giúp huấn luyện viên tính tốc độ của vận động viên ở từng chặng đua."
        ),
        "game_title": "Đường đua Tốc độ cơ bản",
        "game_description": "Sử dụng thước đo quãng đường và đồng hồ bấm giây để xác định tốc độ chuyển động của xe thực nghiệm và so sánh sự nhanh chậm của các vật.",
        "game_type": "game_speed",
        "quiz": [
            mcq(
                "biet",
                r"Công thức tính tốc độ $v$ của một vật đi được quãng đường $s$ trong khoảng thời gian $t$ là:",
                [
                    r"$v = \dfrac{s}{t}$.",
                    r"$v = s \cdot t$.",
                    r"$v = \dfrac{t}{s}$.",
                    r"$v = s + t$.",
                ],
                0,
                r"Tốc độ bằng quãng đường đi được chia cho thời gian đi hết quãng đường đó: $v = \dfrac{s}{t}$.",
            ),
            mcq(
                "biet",
                r"Đơn vị đo tốc độ cơ bản trong hệ thống đo lường quốc tế SI là:",
                [
                    r"Mét trên giây ($\text{m/s}$).",
                    r"Ki-lô-mét trên giờ ($\text{km/h}$).",
                    r"Mét nhân giây ($\text{m}\cdot\text{s}$).",
                    r"Ki-lô-gam trên mét khối ($\text{kg/m}^3$).",
                ],
                0,
                r"Vì đơn vị chiều dài trong hệ SI là $\text{m}$ và đơn vị thời gian là $\text{s}$ nên đơn vị tốc độ trong hệ SI là **mét trên giây** ($\text{m/s}$).",
            ),
            mcq(
                "biet",
                r"Một xe máy chuyển động với tốc độ $10\text{ m/s}$. Giá trị này tương ứng với bao nhiêu $\text{km/h}$?",
                [
                    r"$36\text{ km/h}$.",
                    r"$100\text{ km/h}$.",
                    r"$3{,}6\text{ km/h}$.",
                    r"$60\text{ km/h}$.",
                ],
                0,
                r"Ta có $1\text{ m/s} = 3{,}6\text{ km/h}$, suy ra $10\text{ m/s} = 10 \cdot 3{,}6 = 36\text{ km/h}$.",
            ),
            mcq(
                "biet",
                r"Nói tốc độ của một người đi xe đạp là $15\text{ km/h}$ có nghĩa là:",
                [
                    r"Trung bình trong mỗi giờ ($1\text{ h}$), người đó đi được quãng đường $15\text{ km}$.",
                    r"Người đó bắt buộc phải đi liên tục đúng $15\text{ h}$ mới dừng lại.",
                    r"Trong $15\text{ giờ}$, người đó chỉ đi được quãng đường $1\text{ km}$.",
                    r"Khối lượng của chiếc xe đạp bằng $15\text{ kg}$.",
                ],
                0,
                r"Tốc độ $15\text{ km/h}$ cho biết quãng đường người đó đi được trong một đơn vị thời gian ($1\text{ h}$) là $15\text{ km}$.",
            ),
            mcq(
                "hieu",
                r"Một vận động viên bơi lội bơi hết chiều dài bể bơi $s = 50\text{ m}$ trong khoảng thời gian $t = 25\text{ s}$. Tốc độ bơi của vận động viên đó là:",
                [
                    r"$2\text{ m/s}$.",
                    r"$0{,}5\text{ m/s}$.",
                    r"$1250\text{ m/s}$.",
                    r"$25\text{ m/s}$.",
                ],
                0,
                r"Áp dụng công thức $v = \dfrac{s}{t} = \dfrac{50}{25} = 2\text{ m/s}$.",
            ),
            mcq(
                "hieu",
                r"Một đoàn tàu hoả chuyển động đều với tốc độ $v = 60\text{ km/h}$ trong thời gian $t = 1{,}5\text{ h}$. Quãng đường đoàn tàu đi được là:",
                [
                    r"$90\text{ km}$.",
                    r"$40\text{ km}$.",
                    r"$75\text{ km}$.",
                    r"$61{,}5\text{ km}$.",
                ],
                0,
                r"Quãng đường đoàn tàu đi được là $s = v \cdot t = 60 \cdot 1{,}5 = 90\text{ km}$.",
            ),
            tf4(
                "hieu",
                r"Ba bạn Nam, Minh và Kiên cùng tham gia kiểm tra chạy và đạp xe: bạn Nam chạy $100\text{ m}$ hết $20\text{ s}$, bạn Minh chạy $100\text{ m}$ hết $25\text{ s}$, bạn Kiên đi xe đạp với tốc độ $27\text{ km/h}$. Xét tính đúng sai của các khẳng định sau:",
                [
                    r"a) Bạn Nam chạy nhanh hơn bạn Minh vì trên cùng quãng đường $100\text{ m}$, thời gian chạy của Nam ngắn hơn.",
                    r"b) Tốc độ chạy của bạn Nam là $5\text{ m/s}$ (tức $18\text{ km/h}$).",
                    r"c) Tốc độ chạy của bạn Minh là $4\text{ m/s}$ (tức $14{,}4\text{ km/h}$).",
                    r"d) Tốc độ đi xe đạp của bạn Kiên nhỏ hơn tốc độ chạy của bạn Nam.",
                ],
                [True, True, True, False],
                r"a) Đúng vì cùng quãng đường $100\text{ m}$ mà $20\text{ s} < 25\text{ s}$." "\n"
                r"b) Đúng vì $v_{\text{Nam}} = \dfrac{100}{20} = 5\text{ m/s} = 5 \cdot 3{,}6 = 18\text{ km/h}$." "\n"
                r"c) Đúng vì $v_{\text{Minh}} = \dfrac{100}{25} = 4\text{ m/s} = 4 \cdot 3{,}6 = 14{,}4\text{ km/h}$." "\n"
                r"d) Sai vì $v_{\text{Kiên}} = 27\text{ km/h} = 7{,}5\text{ m/s} > v_{\text{Nam}} = 18\text{ km/h}$.",
            ),
            tf4(
                "hieu",
                r"Xét các phép đổi đơn vị tốc độ và tính toán chuyển động. Mỗi khẳng định sau đúng hay sai?",
                [
                    r"a) $54\text{ km/h} = 15\text{ m/s}$.",
                    r"b) $20\text{ m/s} = 72\text{ km/h}$.",
                    r"c) Một người đi bộ với tốc độ $1{,}5\text{ m/s}$ thì trong $10\text{ phút}$ đi được quãng đường $15\text{ m}$.",
                    r"d) Để đi hết quãng đường $120\text{ km}$ với tốc độ $40\text{ km/h}$ thì cần thời gian $3\text{ h}$.",
                ],
                [True, True, False, True],
                r"a) Đúng vì $\dfrac{54}{3{,}6} = 15\text{ m/s}$." "\n"
                r"b) Đúng vì $20 \cdot 3{,}6 = 72\text{ km/h}$." "\n"
                r"c) Sai vì phải đổi $10\text{ phút} = 600\text{ s}$, quãng đường đi được là $s = 1{,}5 \cdot 600 = 900\text{ m}$." "\n"
                r"d) Đúng vì $t = \dfrac{s}{v} = \dfrac{120}{40} = 3\text{ h}$.",
            ),
            mcq(
                "vandung",
                r"Nhà bạn Lan cách trường học $2{,}7\text{ km}$. Mỗi buổi sáng Lan đạp xe từ nhà đến trường với tốc độ không đổi $v = 3\text{ m/s}$. Biết trường vào học lúc $7\text{ giờ } 00\text{ phút}$, để đến trường vừa đúng giờ vào học thì Lan phải xuất phát từ nhà lúc mấy giờ?",
                [
                    r"$6\text{ giờ } 45\text{ phút}$.",
                    r"$6\text{ giờ } 30\text{ phút}$.",
                    r"$6\text{ giờ } 50\text{ phút}$.",
                    r"$6\text{ giờ } 40\text{ phút}$.",
                ],
                0,
                r"Đổi $s = 2{,}7\text{ km} = 2700\text{ m}$. Thời gian Lan đạp xe đến trường là $t = \dfrac{s}{v} = \dfrac{2700}{3} = 900\text{ s} = 15\text{ phút}$. Vậy Lan phải xuất phát lúc $7\text{ giờ } 00\text{ phút} - 15\text{ phút} = 6\text{ giờ } 45\text{ phút}$.",
            ),
            short(
                "vandung",
                r"Một con báo săn chạy đuổi theo con mồi trên quãng đường thẳng dài $300\text{ m}$ chỉ mất thời gian $12\text{ s}$. Tính tốc độ của con báo săn đó theo đơn vị ki-lô-mét trên giờ ($\text{km/h}$).",
                ["90", "90,0", "90.0"],
                r"Tốc độ của con báo tính theo $\text{m/s}$ là $v = \dfrac{s}{t} = \dfrac{300}{12} = 25\text{ m/s}$. Đổi sang $\text{km/h}$: $v = 25 \cdot 3{,}6 = 90\text{ km/h}$.",
            ),
        ],
    },
]
