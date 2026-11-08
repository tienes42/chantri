"""Vật lý Lớp 12 (SGK Vật lí 12 - Kết nối tri thức với cuộc sống): 4 Chương - 22 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 12

CH1 = ("l12-ch01-vat-li-nhiet", "Chương I: Vật lí nhiệt", "Chương I · SGK Vật lí 12: Cấu trúc chất, sự chuyển thể, nội năng, định luật 1 NĐLH, thang nhiệt độ, nhiệt dung riêng, nhiệt nóng chảy riêng và nhiệt hóa hơi riêng.")
CH2 = ("l12-ch02-khi-li-tuong", "Chương II: Khí lí tưởng", "Chương II · SGK Vật lí 12: Mô hình động học phân tử chất khí, định luật Boyle, định luật Charles, phương trình trạng thái khí lí tưởng và áp suất phân tử.")
CH3 = ("l12-ch03-tu-truong", "Chương III: Từ trường", "Chương III · SGK Vật lí 12: Từ trường, cảm ứng từ, lực từ F = B.I.ℓ.sinα, từ thông, cảm ứng điện từ, dòng điện xoay chiều và máy biến áp.")
CH4 = ("l12-ch04-vat-li-hat-nhan", "Chương IV: Vật lí hạt nhân", "Chương IV · SGK Vật lí 12: Cấu trúc hạt nhân, độ hụt khối, năng lượng liên kết, phản ứng phân hạch – nhiệt hạch, phóng xạ và an toàn phóng xạ.")

LESSONS = [
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 1: Cấu trúc của chất. Sự chuyển thể",
        icon="🧊",
        description="Mô hình động học phân tử về cấu tạo chất, đặc điểm cấu trúc của thể rắn – lỏng – khí, sự nóng chảy và sự hóa hơi (bay hơi, sôi).",
        requirements=[
            "Trình bày được 3 nội dung cơ bản của mô hình động học phân tử về cấu tạo chất và so sánh khoảng cách, lực tương tác, chuyển động phân tử ở 3 thể rắn, lỏng, khí.",
            "Phân biệt được chất rắn kết tinh (có cấu trúc tinh thể và nhiệt độ nóng chảy xác định) với chất rắn vô định hình (không có nhiệt độ nóng chảy xác định).",
            "Giải thích được quá trình nóng chảy, đông đặc, bay hơi và sôi bằng mô hình động học phân tử (trong suốt quá trình nóng chảy của chất rắn kết tinh và quá trình sôi, nhiệt độ của chất không đổi).",
        ],
        definition="Theo mô hình động học phân tử: các chất được cấu tạo từ các hạt riêng biệt gọi là phân tử; các phân tử chuyển động không ngừng (nhiệt độ càng cao thì chuyển động càng nhanh); giữa các phân tử có lực hút và lực đẩy gọi chung là lực tương tác phân tử.",
        theory=(
            "### 1. Cấu trúc của chất ở thể Rắn – Lỏng – Khí\n"
            "- **Thể rắn**: các phân tử ở rất gần nhau, lực tương tác rất mạnh giữ các phân tử chỉ dao động quanh vị trí cân bằng xác định $\\implies$ có **hình dạng và thể tích riêng xác định**.\n"
            "  - *Chất rắn kết tinh* (muối ăn, thạch anh, kim cương, nước đá, kim loại): có cấu trúc tinh thể và có **nhiệt độ nóng chảy xác định**.\n"
            "  - *Chất rắn vô định hình* (thủy tinh, nhựa đường, sáp nến): không có cấu trúc tinh thể và **không có nhiệt độ nóng chảy xác định**.\n"
            "- **Thể lỏng**: khoảng cách phân tử lớn hơn thể rắn, lực tương tác trung bình, phân tử dao động quanh vị trí cân bằng có thể di chuyển $\\implies$ có **thể tích riêng xác định** nhưng hình dạng phụ thuộc bình chứa.\n"
            "- **Thể khí**: khoảng cách phân tử rất lớn so với kích thước phân tử, lực tương tác rất yếu, phân tử chuyển động hỗn loạn về mọi phía $\\implies$ **không có hình dạng và thể tích riêng** (dễ nén).\n\n"
            "### 2. Sự chuyển thể (Nóng chảy – Đông đặc & Hóa hơi – Ngưng tụ)\n"
            "- **Sự nóng chảy**: chuyển từ thể rắn sang thể lỏng (thu nhiệt). Trong suốt thời gian chất rắn kết tinh đang nóng chảy, **nhiệt độ của nó giữ nguyên không đổi** dù vẫn tiếp tục cấp nhiệt.\n"
            "- **Sự hóa hơi**: chuyển từ thể lỏng sang thể khí, gồm 2 hình thức:\n"
            "  - **Bay hơi**: xảy ra ở **mặt thoáng** của chất lỏng ở **mọi nhiệt độ** (tốc độ bay hơi tăng khi nhiệt độ cao, diện tích mặt thoáng lớn, có gió và độ ẩm không khí thấp).\n"
            "  - **Sôi**: xảy ra đồng thời ở **cả trong lòng và trên mặt thoáng** chất lỏng ở một **nhiệt độ sôi xác định** (tại áp suất chuẩn $1\\text{ atm}$, nước sôi ở $100^\\circ\\text{C}$ và trong suốt khi đang sôi nhiệt độ nước không đổi)."
        ),
        formulas=[
            G(
                "So sánh 3 thể của chất và Đặc điểm chuyển thể",
                F("So sánh lực tương tác và khoảng cách phân tử", "$F_{\\text{rắn}} > F_{\\text{lỏng}} \\gg F_{\\text{khí}}; \\qquad d_{\\text{rắn}} < d_{\\text{lỏng}} \\ll d_{\\text{khí}}$", "Ở thể khí, khoảng cách giữa các phân tử rất lớn nên chất khí rất dễ bị nén."),
                F("Quy luật nhiệt độ trong khi nóng chảy (kết tinh) và khi sôi", "$\\text{Đang nóng chảy (chất kết tinh): } t = t_{\\text{nc}} = \\text{const}; \\qquad \\text{Đang sôi: } t = t_{\\text{sôi}} = \\text{const}$", "Nhiệt lượng cung cấp trong giai đoạn này dùng để phá vỡ liên kết giữa các phân tử (tăng thế năng phân tử)."),
            )
        ],
        example="Khi đun nóng một cục nước đá từ $-10^\\circ\\text{C}$ ở áp suất chuẩn: tại $0^\\circ\\text{C}$ nước đá bắt đầu tan (nóng chảy) thành nước lỏng. Trong suốt thời gian cục nước đá đang tan (vừa có đá vừa có nước), nhiệt độ của hỗn hợp nước đá là bao nhiêu và năng lượng nhiệt cung cấp lúc này dùng để làm gì?",
        example_answer="Trong suốt quá trình nước đá (chất rắn kết tinh) đang nóng chảy, nhiệt độ của hệ **giữ nguyên không đổi ở $0^\\circ\\text{C}$**. Nhiệt lượng cung cấp trong giai đoạn này không làm tăng động năng phân tử mà dùng để **phá vỡ mạng tinh thể nước đá** (làm tăng thế năng tương tác phân tử).",
        real_life="Khi cơ thể ra mồ hôi vào ngày nóng hoặc khi lau người bằng khăn ấm lúc sốt, nước bay hơi từ bề mặt da sẽ thu nhiệt từ cơ thể làm da mát đi và giúp hạ sốt.",
        quiz=[
            mcq("biet", "Ở thể nào thì các phân tử chỉ dao động xung quanh các vị trí cân bằng cố định làm cho vật có cả hình dạng và thể tích riêng xác định?", ["Thể rắn", "Thể lỏng", "Thể khí", "Chân không"], 0, "Ở thể rắn, lực tương tác phân tử rất mạnh giữ các phân tử dao động quanh vị trí cân bằng xác định nên vật rắn có hình dạng và thể tích riêng."),
            mcq("biet", "Trong suốt thời gian một chất rắn **kết tinh** đang nóng chảy (hoặc một chất lỏng đang sôi ở áp suất không đổi), nhiệt độ của chất đó thay đổi như thế nào?", ["Nhiệt độ giữ nguyên không đổi", "Nhiệt độ tăng vọt lên gấp đôi", "Nhiệt độ giảm liên tục", "Nhiệt độ lúc tăng lúc giảm ngẫu nhiên"], 0, "Chất rắn kết tinh có nhiệt độ nóng chảy xác định và chất lỏng có nhiệt độ sôi xác định; trong suốt quá trình chuyển thể đó nhiệt độ không đổi."),
            mcq("hieu", "Điểm khác biệt cơ bản giữa **sự sôi** và **sự bay hơi** của chất lỏng là gì?", ["Sự bay hơi chỉ xảy ra trên mặt thoáng ở mọi nhiệt độ, còn sự sôi xảy ra cả trên mặt thoáng và trong lòng chất lỏng ở nhiệt độ sôi xác định", "Sự bay hơi chỉ xảy ra ở $100^\\circ\\text{C}$, còn sự sôi xảy ra ở mọi nhiệt độ", "Sự sôi làm giảm nhiệt độ chất lỏng xuống dưới $0^\\circ\\text{C}$", "Sự bay hơi là sự chuyển từ thể khí sang thể rắn"], 0, "Bay hơi xảy ra ở mặt thoáng tại bất kì nhiệt độ nào, còn sôi xảy ra cả trong lòng chất lỏng (tạo các bọt khí nổi lên vỡ ở mặt thoáng) tại nhiệt độ sôi xác định."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cấu trúc chất và sự chuyển thể:", [
                "Chất rắn vô định hình (như thủy tinh, nhựa đường, sáp nến) không có cấu trúc tinh thể và không có nhiệt độ nóng chảy xác định.",
                "Tốc độ bay hơi của nước tăng lên khi nhiệt độ tăng, diện tích mặt thoáng lớn và có gió thổi.",
                "Khoảng cách giữa các phân tử ở thể khí rất nhỏ so với kích thước mỗi phân tử nên chất khí không thể nén được.",
                "Ở áp suất tiêu chuẩn $1\\text{ atm}$, nước tinh khiết nóng chảy ở $0^\\circ\\text{C}$ và sôi ở $100^\\circ\\text{C}$.",
            ], [True, True, False, True], "Ý c) sai vì ở thể khí khoảng cách giữa các phân tử rất lớn so với kích thước phân tử nên chất khí rất dễ bị nén."),
            short("vandung", "Ở áp suất tiêu chuẩn $1\\text{ atm}$, trong suốt quá trình nước tinh khiết đang sôi thì nhiệt độ của nước giữ không đổi ở bao nhiêu độ Celsius ($^\\circ\\text{C}$)?", ["100"], "Ở áp suất chuẩn $1\\text{ atm}$, nước tinh khiết sôi ở nhiệt độ không đổi là $100^\\circ\\text{C}$.", unit="°C"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 2: Nội năng. Định luật 1 của nhiệt động lực học",
        icon="🔥",
        description="Nội năng U phụ thuộc nhiệt độ và thể tích, hai cách làm biến đổi nội năng (thực hiện công và truyền nhiệt), công thức ΔU = A + Q và quy ước dấu.",
        requirements=[
            "Nêu được nội năng $U$ của một vật là tổng động năng và thế năng tương tác của các phân tử cấu tạo nên vật; nội năng phụ thuộc vào nhiệt độ $T$ và thể tích $V$ của vật.",
            "Phân biệt được hai cách làm biến đổi nội năng: thực hiện công ($A$) và truyền nhiệt ($Q$).",
            "Viết và vận dụng được biểu thức Định luật 1 của nhiệt động lực học $\\Delta U = A + Q$ kèm quy ước dấu của $A, Q, \\Delta U$.",
        ],
        definition="Định luật 1 của nhiệt động lực học: Độ biến thiên nội năng $\\Delta U$ của một hệ bằng tổng công $A$ và nhiệt lượng $Q$ mà hệ nhận được trong quá trình đó: $\\Delta U = A + Q$.",
        theory=(
            "### 1. Nội năng và hai cách làm biến đổi nội năng\n"
            "- **Nội năng ($U$)**: tổng động năng (do chuyển động nhiệt) và thế năng (do tương tác phân tử) của các phân tử cấu tạo nên vật, đơn vị là Joule ($\\text{J}$). Nội năng của vật phụ thuộc vào **nhiệt độ $T$** và **thể tích $V$**.\n"
            "- **Hai cách làm biến đổi nội năng**:\n"
            "  1. **Thực hiện công ($A$)**: có sự chuyển hóa từ dạng năng lượng khác (như cơ năng) sang nội năng (ví dụ: cọ xát hai bàn tay, nén khí trong xi-lanh).\n"
            "  2. **Truyền nhiệt ($Q$)**: không có sự thực hiện công mà chỉ có sự truyền nội năng từ vật nóng hơn sang vật lạnh hơn.\n\n"
            "### 2. Định luật 1 của nhiệt động lực học và Quy ước dấu\n"
            "- Công thức:\n"
            "  $$\\Delta U = A + Q$$\n"
            "- **Quy ước dấu chuẩn SGK**:\n"
            "  - $Q > 0$: Hệ **nhận nhiệt lượng** từ bên ngoài; $Q < 0$: Hệ **truyền (tỏa) nhiệt lượng** ra bên ngoài.\n"
            "  - $A > 0$: Hệ **nhận công** từ bên ngoài (ví dụ khối khí bị nén); $A < 0$: Hệ **thực hiện công** lên bên ngoài (ví dụ khối khí dãn nở đẩy pít-tông).\n"
            "  - $\\Delta U > 0$: Nội năng của hệ tăng; $\\Delta U < 0$: Nội năng của hệ giảm."
        ),
        formulas=[
            G(
                "Định luật 1 Nhiệt động lực học và Quy ước dấu",
                F("Biểu thức Định luật 1 của nhiệt động lực học", "$\\Delta U = A + Q$", "Trong đó $\\Delta U = U_2 - U_1$ là độ biến thiên nội năng ($\\text{J}$), $A$ là công ($\\text{J}$), $Q$ là nhiệt lượng ($\\text{J}$)."),
                F("Quy ước dấu của Q và A", "$\\text{Hệ nhận: } Q > 0,\\ A > 0; \\qquad \\text{Hệ truyền/thực hiện ra ngoài: } Q < 0,\\ A < 0$", "Mẹo nhớ nhanh: Cái gì đi VÀO hệ thì mang dấu DƯƠNG ($+$), cái gì đi RA khỏi hệ thì mang dấu ÂM ($-$)."),
            )
        ],
        example="Người ta truyền cho một khối khí trong xi-lanh một nhiệt lượng $150\\text{ J}$. Khối khí nở ra và thực hiện một công $90\\text{ J}$ đẩy pít-tông dịch chuyển. Hãy xác định dấu của $Q, A$ và tính độ biến thiên nội năng $\\Delta U$ của khối khí.",
        example_answer="Vì khối khí nhận nhiệt lượng nên $Q = +150\\text{ J}$; khối khí nở ra thực hiện công lên pít-tông nên $A = -90\\text{ J}$. Theo định luật 1 của nhiệt động lực học, độ biến thiên nội năng của khối khí là $\\Delta U = A + Q = -90 + 150 = +60\\text{ J}$ (nội năng của khối khí tăng thêm $60\\text{ J}$).",
        real_life="Động cơ đốt trong của ô tô, xe máy và động cơ nhiệt trong nhà máy nhiệt điện hoạt động dựa trên nguyên lí cung cấp nhiệt lượng $Q$ cho khí nóng dãn nở sinh công cơ học $A$ làm quay trục máy.",
        quiz=[
            mcq("biet", "Biểu thức của Định luật 1 nhiệt động lực học liên hệ giữa độ biến thiên nội năng $\\Delta U$, công $A$ và nhiệt lượng $Q$ mà hệ nhận được là gì?", ["$\\Delta U = A + Q$", "$\\Delta U = A \\cdot Q$", "$\\Delta U = \\dfrac{Q}{A}$", "$A + Q + \\Delta U = 0$"], 0, "Theo định luật 1 của nhiệt động lực học: $\\Delta U = A + Q$."),
            mcq("biet", "Trong biểu thức $\\Delta U = A + Q$, quy ước dấu nào sau đây tương ứng với quá trình hệ **nhận nhiệt lượng** nhưng **thực hiện công** ra bên ngoài?", ["$Q > 0$ và $A < 0$", "$Q > 0$ và $A > 0$", "$Q < 0$ và $A > 0$", "$Q < 0$ và $A < 0$"], 0, "Theo quy ước dấu: hệ nhận nhiệt thì $Q > 0$, hệ thực hiện công ra ngoài thì $A < 0$."),
            mcq("hieu", "Khi dùng tay nén nhanh pít-tông để ép khối khí trong một xi-lanh cách nhiệt hoàn toàn ($Q = 0$) thì nội năng của khối khí thay đổi như thế nào?", ["Nội năng tăng lên ($\\Delta U = A > 0$) vì khối khí nhận công", "Nội năng giảm đi ($\\Delta U < 0$)", "Nội năng không thay đổi ($\\Delta U = 0$)", "Nội năng giảm về bằng $0$"], 0, "Xi-lanh cách nhiệt nên $Q = 0$; nén khí nghĩa là khí nhận công ($A > 0$), do đó $\\Delta U = A + 0 > 0$ (nội năng và nhiệt độ khí tăng lên)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nội năng và định luật 1 nhiệt động lực học:", [
                "Nội năng của một vật phụ thuộc vào nhiệt độ và thể tích của vật đó.",
                "Có thể làm thay đổi nội năng của vật bằng hai cách: thực hiện công và truyền nhiệt.",
                "Nếu hệ truyền nhiệt lượng $50\\text{ J}$ ra môi trường thì trong công thức $\\Delta U = A + Q$ ta thay $Q = +50\\text{ J}$.",
                "Nếu thực hiện công $100\\text{ J}$ để nén khí mà khí tỏa ra ngoài nhiệt lượng $30\\text{ J}$ thì nội năng của khí tăng thêm $70\\text{ J}$.",
            ], [True, True, False, True], "Ý c) sai vì khi hệ tỏa (truyền) nhiệt lượng ra môi trường ngoài thì $Q$ mang dấu âm ($Q = -50\\text{ J}$)."),
            short("vandung", "Một lượng khí trong xi-lanh nhận được nhiệt lượng $200\\text{ J}$ và dãn nở thực hiện một công $80\\text{ J}$ đẩy pít-tông đi lên. Độ biến thiên nội năng $\\Delta U$ của lượng khí bằng bao nhiêu Joule ($\\text{J}$)?", ["120"], "Khí nhận nhiệt ($Q = +200\\text{ J}$) và thực hiện công ($A = -80\\text{ J}$), nên $\\Delta U = A + Q = -80 + 200 = 120\\text{ J}$.", unit="J"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 3: Nhiệt độ. Thang nhiệt độ – nhiệt kế",
        icon="🌡️",
        description="Sự cân bằng nhiệt, độ không tuyệt đối (0 K = -273,15 °C), điểm ba của nước và công thức chuyển đổi thang Kelvin T(K) = t(°C) + 273.",
        requirements=[
            "Nêu được chiều truyền nhiệt tự nhiên từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn và điều kiện dừng truyền nhiệt khi đạt trạng thái cân bằng nhiệt (hai vật có cùng nhiệt độ).",
            "Nêu được ý nghĩa của độ không tuyệt đối ($0\\text{ K} = -273{,}15^\\circ\\text{C}$) và điểm ba của nước ($273{,}16\\text{ K} = 0{,}01^\\circ\\text{C}$) trong thang nhiệt độ tuyệt đối Kelvin.",
            "Vận dụng được hệ thức $T(\\text{K}) = t(^\\circ\\text{C}) + 273$ (hoặc $273{,}15$) và nhận xét $\\Delta T(\\text{K}) = \\Delta t(^\\circ\\text{C})$.",
        ],
        definition="Khi hai vật có nhiệt độ chênh lệch tiếp xúc nhau thì năng lượng nhiệt tự truyền từ vật có nhiệt độ cao hơn sang vật có nhiệt độ thấp hơn cho đến khi nhiệt độ hai vật bằng nhau (trạng thái cân bằng nhiệt). Trong hệ SI, đơn vị nhiệt độ là Kelvin ($\\text{K}$), liên hệ với độ Celsius bởi: $T(\\text{K}) = t(^\\circ\\text{C}) + 273$ (chính xác là $273{,}15$).",
        theory=(
            "### 1. Sự truyền nhiệt và Cân bằng nhiệt (Định luật 0 Nhiệt động lực học)\n"
            "- Nhiệt năng luôn tự truyền từ vật có **nhiệt độ cao hơn** sang vật có **nhiệt độ thấp hơn**.\n"
            "- Khi hai vật đạt **trạng thái cân bằng nhiệt**, nhiệt độ của hai vật bằng nhau ($t_1 = t_2 = t_{\\text{cb}}$) và quá trình truyền nhiệt dừng lại.\n\n"
            "### 2. Thang nhiệt độ Kelvin (Thang nhiệt độ tuyệt đối) và Thang Celsius\n"
            "- **Độ không tuyệt đối ($0\\text{ K} = -273{,}15^\\circ\\text{C}$)**: nhiệt độ thấp nhất mà tại đó động năng chuyển động nhiệt của các phân tử tiến tới bằng không và thế năng của chúng đạt tối thiểu (không có vật nào có nhiệt độ thấp hơn $0\\text{ K}$).\n"
            "- **Điểm ba của nước ($273{,}16\\text{ K} = 0{,}01^\\circ\\text{C}$ ở $611{,}7\\text{ Pa}$)**: trạng thái mà nước tinh khiết tồn tại đồng thời ở cả 3 thể rắn (nước đá), lỏng (nước) và khí (hơi nước) ở cân bằng nhiệt.\n"
            "- **Công thức chuyển đổi**:\n"
            "  $$T(\\text{K}) = t(^\\circ\\text{C}) + 273{,}15 \\approx t(^\\circ\\text{C}) + 273$$\n"
            "- **Độ biến thiên nhiệt độ**: Mỗi độ chia $1\\text{ K}$ bằng đúng $1^\\circ\\text{C}$ nên độ chênh lệch (độ tăng/giảm) nhiệt độ trên hai thang luôn bằng nhau:\n"
            "  $$\\Delta T(\\text{K}) = T_2 - T_1 = t_2 - t_1 = \\Delta t(^\\circ\\text{C})$$"
        ),
        formulas=[
            G(
                "Chuyển đổi giữa thang Kelvin (K), Celsius (°C) và Fahrenheit (°F)",
                F("Liên hệ giữa nhiệt độ Kelvin và nhiệt độ Celsius", "$T(\\text{K}) = t(^\\circ\\text{C}) + 273; \\qquad \\Delta T(\\text{K}) = \\Delta t(^\\circ\\text{C})$", "Chú ý: Nhiệt độ tuyệt đối $T = t + 273$, nhưng **độ tăng nhiệt độ** $\\Delta T = \\Delta t$ (không cộng $273$ vào $\\Delta t$!)."),
                F("Liên hệ giữa thang Fahrenheit và Celsius", "$t(^\\circ\\text{F}) = 1{,}8 \\cdot t(^\\circ\\text{C}) + 32; \\qquad \\Delta t(^\\circ\\text{F}) = 1{,}8 \\cdot \\Delta t(^\\circ\\text{C})$", "Độ không tuyệt đối: $0\\text{ K} = -273{,}15^\\circ\\text{C}$."),
            )
        ],
        example="Đun nóng một lượng nước từ nhiệt độ $t_1 = 27^\\circ\\text{C}$ lên đến nhiệt độ $t_2 = 87^\\circ\\text{C}$. Hãy tính các nhiệt độ $T_1, T_2$ theo thang Kelvin và độ tăng nhiệt độ $\\Delta T$ theo đơn vị Kelvin ($\\text{K}$).",
        example_answer="Theo thang Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$ và $T_2 = 87 + 273 = 360\\text{ K}$. Độ tăng nhiệt độ theo thang Kelvin bằng đúng độ tăng nhiệt độ theo thang Celsius: $\\Delta T = T_2 - T_1 = 360 - 300 = 60\\text{ K}$ (bằng $\\Delta t = 87 - 27 = 60^\\circ\\text{C}$).",
        real_life="Trong mọi công thức của định luật chất khí lí tưởng và bức xạ nhiệt trong Vật lí và Hóa học, nhiệt độ bắt buộc phải được tính theo thang nhiệt độ tuyệt đối Kelvin ($\\text{K}$).",
        quiz=[
            mcq("biet", "Đơn vị đo nhiệt độ cơ bản trong hệ thống đo lường quốc tế SI là gì?", ["Kelvin ($\\text{K}$)", "Độ Celsius ($^\\circ\\text{C}$)", "Độ Fahrenheit ($^\\circ\\text{F}$)", "Joule ($\\text{J}$)"], 0, "Trong hệ SI, đơn vị cơ bản của nhiệt độ nhiệt động lực học là Kelvin ($\\text{K}$)."),
            mcq("biet", "Khi cho hai vật có nhiệt độ khác nhau tiếp xúc nhau, quá trình truyền nhiệt giữa chúng sẽ dừng lại khi nào?", ["Khi hai vật có cùng nhiệt độ (đạt trạng thái cân bằng nhiệt)", "Khi hai vật có cùng khối lượng", "Khi hai vật có cùng thể tích", "Khi một trong hai vật có nhiệt độ bằng $0\\text{ K}$"], 0, "Sự truyền nhiệt tự phát chỉ xảy ra khi có sự chênh lệch nhiệt độ và dừng lại khi hai vật đạt cùng một nhiệt độ (cân bằng nhiệt)."),
            mcq("hieu", "Khi nhiệt độ của một thanh sắt tăng thêm $\\Delta t = 40^\\circ\\text{C}$ thì trong thang nhiệt độ Kelvin, nhiệt độ của thanh sắt đó đã tăng thêm bao nhiêu Kelvin ($\\text{K}$)?", ["$40\\text{ K}$", "$313\\text{ K}$", "$233\\text{ K}$", "$273\\text{ K}$"], 0, "Vì khoảng cách $1\\text{ K}$ bằng đúng khoảng cách $1^\\circ\\text{C}$ nên độ biến thiên nhiệt độ trên hai thang bằng nhau: $\\Delta T(\\text{K}) = \\Delta t(^\\circ\\text{C}) = 40\\text{ K}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về thang nhiệt độ:", [
                "Độ không tuyệt đối ($0\\text{ K}$) tương ứng với nhiệt độ $-273{,}15^\\circ\\text{C}$ trong thang Celsius.",
                "Không thể có bất kì vật chất nào đạt nhiệt độ thấp hơn độ không tuyệt đối $0\\text{ K}$.",
                "Điểm ba của nước là trạng thái mà nước tinh khiết vừa đóng băng, vừa ở thể lỏng và vừa hóa hơi cân bằng nhau ở $0{,}01^\\circ\\text{C}$ ($273{,}16\\text{ K}$).",
                "Ở nhiệt độ $100^\\circ\\text{C}$ tương ứng với $173\\text{ K}$ trong thang Kelvin.",
            ], [True, True, True, False], "Ý d) sai vì $100^\\circ\\text{C}$ tương ứng với $T = 100 + 273 = 373\\text{ K}$."),
            short("vandung", "Một bình khí ở nhiệt độ $t = 47^\\circ\\text{C}$. Lấy $T(\\text{K}) = t(^\\circ\\text{C}) + 273$, nhiệt độ tuyệt đối $T$ của bình khí này bằng bao nhiêu Kelvin ($\\text{K}$)?", ["320"], "Áp dụng công thức $T = 47 + 273 = 320\\text{ K}$.", unit="K"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 4: Nhiệt dung riêng",
        icon="🫖",
        description="Định nghĩa và đơn vị nhiệt dung riêng c [J/(kg.K)], công thức nhiệt lượng Q = m.c.Δt và phương trình cân bằng nhiệt Q_tỏa = Q_thu.",
        requirements=[
            "Định nghĩa được nhiệt dung riêng $c$ của một chất là nhiệt lượng cần truyền cho $1\\text{ kg}$ chất đó để làm cho nhiệt độ của nó tăng thêm $1\\text{ K}$ (hoặc $1^\\circ\\text{C}$), có đơn vị $\\text{J/(kg}\\cdot\\text{K)}$.",
            "Viết và vận dụng được công thức tính nhiệt lượng vật thu vào hay tỏa ra khi thay đổi nhiệt độ (không chuyển thể): $Q = m \\cdot c \\cdot \\Delta t = m \\cdot c \\cdot |t_2 - t_1|$.",
            "Vận dụng được phương trình cân bằng nhiệt $Q_{\\text{tỏa}} = Q_{\\text{thu}}$ và giải thích bố trí thí nghiệm đo nhiệt dung riêng của nước ($c = \\dfrac{\\mathcal{P} \\cdot \\tau}{m \\cdot \\Delta T}$).",
        ],
        definition="Nhiệt dung riêng ($c$) của một chất là nhiệt lượng cần truyền cho $1\\text{ kg}$ chất đó để làm cho nhiệt độ của nó tăng thêm $1\\text{ K}$ (hay $1^\\circ\\text{C}$). Nhiệt lượng mà một lượng chất có khối lượng $m$ thu vào hoặc tỏa ra khi độ biến thiên nhiệt độ là $\\Delta t$ được tính bằng công thức: $Q = m \\cdot c \\cdot \\Delta t$.",
        theory=(
            "### 1. Nhiệt dung riêng và Công thức tính nhiệt lượng\n"
            "- Kí hiệu nhiệt dung riêng: $c$, đơn vị trong hệ SI là $\\text{J/(kg}\\cdot\\text{K)}$ hoặc $\\text{J/(kg}\\cdot\\text{độ)}$ (ví dụ: nước có nhiệt dung riêng rất lớn $c_{\\text{nước}} \\approx 4200\\text{ J/(kg}\\cdot\\text{K)}$, nhôm $c_{\\text{Al}} = 880\\text{ J/(kg}\\cdot\\text{K)}$, đồng $c_{\\text{Cu}} = 380\\text{ J/(kg}\\cdot\\text{K)}$).\n"
            "- **Công thức tính nhiệt lượng**:\n"
            "  $$Q = m \\cdot c \\cdot \\Delta T = m \\cdot c \\cdot (t_2 - t_1) \\implies c = \\dfrac{Q}{m \\cdot \\Delta T}$$\n\n"
            "### 2. Phương trình cân bằng nhiệt và Thực hành đo nhiệt dung riêng\n"
            "- Khi các vật trao đổi nhiệt trong một hệ cô lập (nhiệt lượng kế cách nhiệt), tổng nhiệt lượng do các vật nóng hơn tỏa ra bằng tổng nhiệt lượng do các vật lạnh hơn thu vào:\n"
            "  $$Q_{\\text{tỏa}} = Q_{\\text{thu}} \\iff m_1 c_1 (t_1 - t_{\\text{cb}}) = m_2 c_2 (t_{\\text{cb}} - t_2)$$\n"
            "- **Thực hành đo $c$ của nước**: Dùng dây điện trở công suất $\\mathcal{P}$ đun khối lượng $m$ nước trong bình nhiệt lượng kế trong thời gian $\\tau$ làm nhiệt độ tăng $\\Delta T$: $Q = \\mathcal{P} \\cdot \\tau = m \\cdot c \\cdot \\Delta T \\implies c = \\dfrac{\\mathcal{P} \\cdot \\tau}{m \\cdot \\Delta T}$."
        ),
        formulas=[
            G(
                "Công thức Nhiệt dung riêng và Phương trình cân bằng nhiệt",
                F("Nhiệt lượng thu vào hay tỏa ra khi biến thiên nhiệt độ", "$Q = m \\cdot c \\cdot \\Delta t = m \\cdot c \\cdot |t_2 - t_1| \\implies c = \\dfrac{Q}{m \\cdot \\Delta t}$", "Trong đó $m$ tính bằng $\\text{kg}$ ($1\\text{ L nước} \\approx 1\\text{ kg}$), $c$ tính bằng $\\text{J/(kg}\\cdot\\text{K)}$, $\\Delta t$ tính bằng $\\text{K}$ hoặc $^\\circ\\text{C}$, $Q$ tính bằng $\\text{J}$."),
                F("Phương trình cân bằng nhiệt và Công thức thực hành", "$Q_{\\text{tỏa}} = Q_{\\text{thu}}; \\qquad c = \\dfrac{\\mathcal{P} \\cdot \\tau}{m \\cdot \\Delta T} = \\dfrac{U \\cdot I \\cdot \\tau}{m \\cdot \\Delta T}$", "Trong đó $\\mathcal{P}$ là công suất dây đun ($\\text{W}$), $\\tau$ là thời gian đun ($\\text{s}$)."),
            )
        ],
        example="Một ấm nhôm có khối lượng $m_1 = 0{,}5\\text{ kg}$ chứa $2\\text{ lít}$ nước ($m_2 = 2\\text{ kg}$) ở nhiệt độ ban đầu $t_1 = 20^\\circ\\text{C}$. Biết nhiệt dung riêng của nhôm là $c_1 = 880\\text{ J/(kg}\\cdot\\text{K)}$ và của nước là $c_2 = 4200\\text{ J/(kg}\\cdot\\text{K)}$. Hãy tính nhiệt lượng $Q$ cần cung cấp để đun sôi ấm nước đó ở $t_2 = 100^\\circ\\text{C}$.",
        example_answer="Độ tăng nhiệt độ của cả ấm nhôm và nước là $\\Delta t = 100 - 20 = 80^\\circ\\text{C}$. Nhiệt lượng cần cung cấp là $Q = Q_1 + Q_2 = (m_1 c_1 + m_2 c_2)\\Delta t = (0{,}5 \\cdot 880 + 2 \\cdot 4200) \\cdot 80 = (440 + 8400) \\cdot 80 = 8840 \\cdot 80 = 707\\,200\\text{ J} = 707{,}2\\text{ kJ}$.",
        real_life="Vì nước có nhiệt dung riêng rất lớn ($4200\\text{ J/(kg}\\cdot\\text{K)}$, gấp $5$ lần đất cát) nên nước được dùng làm chất tải nhiệt làm mát trong két nước động cơ ô tô, và các vùng ven biển có khí hậu ôn hòa hơn vùng sâu trong lục địa.",
        quiz=[
            mcq("biet", "Đơn vị đo của nhiệt dung riêng $c$ trong hệ thống đo lường quốc tế SI là gì?", ["$\\text{J/(kg}\\cdot\\text{K)}$", "$\\text{J/kg}$", "$\\text{J/K}$", "$\\text{W/m}^2$"], 0, "Vì $c = \\dfrac{Q}{m \\cdot \\Delta T}$ nên đơn vị của nhiệt dung riêng là $\\text{J/(kg}\\cdot\\text{K)}$."),
            mcq("biet", "Biết nhiệt dung riêng của đồng là $380\\text{ J/(kg}\\cdot\\text{K)}$. Con số này có ý nghĩa vật lí là gì?", ["Cần truyền nhiệt lượng $380\\text{ J}$ cho $1\\text{ kg}$ đồng để làm nhiệt độ của nó tăng thêm $1\\text{ K}$ (hoặc $1^\\circ\\text{C}$)", "Cần truyền $380\\text{ J}$ để làm nóng chảy hoàn toàn $1\\text{ kg}$ đồng", "Cần truyền $380\\text{ J}$ để làm hóa hơi $1\\text{ kg}$ đồng", "$1\\text{ kg}$ đồng luôn có nội năng bằng $380\\text{ J}$"], 0, "Nhiệt dung riêng cho biết nhiệt lượng cần thiết để $1\\text{ kg}$ chất đó tăng thêm $1\\text{ K}$ ($1^\\circ\\text{C}$)."),
            mcq("hieu", "Cùng cung cấp một nhiệt lượng $Q$ như nhau cho $1\\text{ kg}$ nước ($c_1 = 4200\\text{ J/(kg}\\cdot\\text{K)}$) và $1\\text{ kg}$ nhôm ($c_2 = 880\\text{ J/(kg}\\cdot\\text{K)}$) thì độ tăng nhiệt độ của chất nào lớn hơn?", ["Độ tăng nhiệt độ của nhôm lớn hơn của nước (vì nhôm có nhiệt dung riêng nhỏ hơn)", "Độ tăng nhiệt độ của nước lớn hơn của nhôm", "Hai chất tăng nhiệt độ bằng nhau", "Cả hai chất đều không tăng nhiệt độ"], 0, "Từ $\\Delta t = \\dfrac{Q}{m c}$, với cùng $Q$ và $m$, chất nào có nhiệt dung riêng $c$ nhỏ hơn (nhôm) sẽ có độ tăng nhiệt độ $\\Delta t$ lớn hơn."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nhiệt dung riêng và cân bằng nhiệt:", [
                "Nhiệt dung riêng là đại lượng đặc trưng cho bản chất của từng chất.",
                "Nước có nhiệt dung riêng rất lớn nên thường được dùng làm chất làm mát trong động cơ nhiệt.",
                "Khi thả một miếng sắt ở $90^\\circ\\text{C}$ vào một cốc nước ở $25^\\circ\\text{C}$, nhiệt độ cân bằng của hệ có thể bằng $100^\\circ\\text{C}$.",
                "Trong thí nghiệm đo nhiệt dung riêng bằng bình nhiệt lượng kế, que khuấy giúp nhiệt độ của nước trong bình đồng đều hơn.",
            ], [True, True, False, True], "Ý c) sai vì nhiệt độ cân bằng $t_{\\text{cb}}$ luôn phải nằm trong khoảng giữa nhiệt độ thấp và nhiệt độ cao ban đầu ($25^\\circ\\text{C} < t_{\\text{cb}} < 90^\\circ\\text{C}$)."),
            short("vandung", "Tính nhiệt lượng $Q$ (theo đơn vị $\\text{kJ}$) cần cung cấp để đun nóng $m = 2\\text{ kg}$ nước từ $25^\\circ\\text{C}$ lên $75^\\circ\\text{C}$, biết nhiệt dung riêng của nước là $c = 4200\\text{ J/(kg}\\cdot\\text{K)}$.", ["420"], "Ta có $\\Delta t = 75 - 25 = 50\\text{ K}$. Nhiệt lượng cần truyền là $Q = m c \\Delta t = 2 \\cdot 4200 \\cdot 50 = 420\\,000\\text{ J} = 420\\text{ kJ}$.", unit="kJ"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 5: Nhiệt nóng chảy riêng",
        icon="❄️",
        description="Khái niệm và đơn vị nhiệt nóng chảy riêng λ (J/kg), công thức tính nhiệt lượng nóng chảy Q = λ.m và bài toán kết hợp tăng nhiệt độ – nóng chảy.",
        requirements=[
            "Định nghĩa được nhiệt nóng chảy riêng $\\lambda$ của một chất rắn kết tinh là nhiệt lượng cần truyền cho $1\\text{ kg}$ chất đó để nó chuyển hoàn toàn từ thể rắn sang thể lỏng ở nhiệt độ nóng chảy (đơn vị $\\text{J/kg}$).",
            "Viết và vận dụng được công thức tính nhiệt lượng cần truyền cho vật rắn kết tinh khối lượng $m$ đang ở nhiệt độ nóng chảy: $Q = \\lambda \\cdot m$.",
            "Giải được bài toán tổng hợp tính nhiệt lượng làm vật rắn tăng nhiệt độ đến điểm nóng chảy rồi nóng chảy hoàn toàn: $Q = m c_{\\text{rắn}}(t_{\\text{nc}} - t_1) + \\lambda m$.",
        ],
        definition="Nhiệt nóng chảy riêng ($\\lambda$) của một chất rắn kết tinh là nhiệt lượng cần truyền cho một đơn vị khối lượng ($1\\text{ kg}$) chất đó ở nhiệt độ nóng chảy để nó chuyển hoàn toàn từ thể rắn sang thể lỏng mà không thay đổi nhiệt độ: $\\lambda = \\dfrac{Q}{m} \\iff Q = \\lambda \\cdot m$ (đơn vị $\\text{J/kg}$).",
        theory=(
            "### 1. Nhiệt nóng chảy riêng và Công thức tính nhiệt lượng nóng chảy\n"
            "- Kí hiệu: $\\lambda$, đơn vị trong hệ SI là **Joule trên kilôgam** ($\\text{J/kg}$). Ví dụ của nước đá ở $0^\\circ\\text{C}$: $\\lambda \\approx 3{,}34 \\cdot 10^5\\text{ J/kg}$.\n"
            "- Khi vật rắn kết tinh có khối lượng $m$ đã ở đúng nhiệt độ nóng chảy $t_{\\text{nc}}$, nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn vật là:\n"
            "  $$Q = \\lambda \\cdot m$$\n"
            "- Ngược lại, trong quá trình **đông đặc** ở nhiệt độ đông đặc $t_{\\text{nc}}$, một khối chất lỏng khối lượng $m$ cũng **tỏa ra** nhiệt lượng đúng bằng $Q = \\lambda \\cdot m$.\n\n"
            "### 2. Bài toán đun nóng chảy từ nhiệt độ ban đầu $t_1 < t_{\\text{nc}}$\n"
            "- Gồm 2 giai đoạn:\n"
            "  1. Tăng nhiệt độ của vật rắn từ $t_1$ lên nhiệt độ nóng chảy $t_{\\text{nc}}$: $Q_1 = m \\cdot c_{\\text{rắn}} \\cdot (t_{\\text{nc}} - t_1)$.\n"
            "  2. Làm vật rắn nóng chảy hoàn toàn ở nhiệt độ không đổi $t_{\\text{nc}}$: $Q_2 = \\lambda \\cdot m$.\n"
            "  - Tổng nhiệt lượng: $Q = Q_1 + Q_2 = m c_{\\text{rắn}}(t_{\\text{nc}} - t_1) + \\lambda m$."
        ),
        formulas=[
            G(
                "Công thức Nhiệt nóng chảy riêng",
                F("Nhiệt lượng nóng chảy ở nhiệt độ nóng chảy", "$Q = \\lambda \\cdot m \\iff \\lambda = \\dfrac{Q}{m}$", "Trong đó $m$ là khối lượng phần chất rắn đã nóng chảy ($\\text{kg}$), $\\lambda$ là nhiệt nóng chảy riêng ($\\text{J/kg}$), $Q$ tính bằng $\\text{J}$."),
                F("Tổng nhiệt lượng đun vật rắn từ t₁ < t_nc đến khi nóng chảy hết", "$Q = m \\cdot c_{\\text{rắn}} \\cdot (t_{\\text{nc}} - t_1) + \\lambda \\cdot m$", "Nếu tiếp tục đun phần chất lỏng sau khi tan hết lên nhiệt độ $t_2 > t_{\\text{nc}}$ thì cộng thêm $Q_3 = m \\cdot c_{\\text{lỏng}} \\cdot (t_2 - t_{\\text{nc}})$."),
            )
        ],
        example="Tính nhiệt lượng $Q$ cần cung cấp để làm nóng chảy hoàn toàn một tảng nước đá có khối lượng $m = 2\\text{ kg}$ đang ở nhiệt độ $0^\\circ\\text{C}$. Biết nhiệt nóng chảy riêng của nước đá ở $0^\\circ\\text{C}$ là $\\lambda = 3{,}34 \\cdot 10^5\\text{ J/kg}$.",
        example_answer="Vì tảng nước đá đã ở sẵn nhiệt độ nóng chảy $0^\\circ\\text{C}$ nên nhiệt lượng cần cung cấp để nó tan hoàn toàn thành nước ở $0^\\circ\\text{C}$ là $Q = \\lambda \\cdot m = 3{,}34 \\cdot 10^5 \\cdot 2 = 6{,}68 \\cdot 10^5\\text{ J} = 668\\text{ kJ}$.",
        real_life="Trong công nghiệp luyện kim và đúc đồng, đúc gang, kĩ sư phải dựa vào nhiệt độ nóng chảy và nhiệt nóng chảy riêng $\\lambda$ của từng kim loại để tính lượng nhiên liệu hoặc điện năng cần thiết cho lò nung.",
        quiz=[
            mcq("biet", "Công thức tính nhiệt lượng $Q$ cần cung cấp để làm nóng chảy hoàn toàn một khối chất rắn kết tinh có khối lượng $m$ và nhiệt nóng chảy riêng $\\lambda$ ngay tại nhiệt độ nóng chảy của nó là gì?", ["$Q = \\lambda \\cdot m$", "$Q = \\dfrac{\\lambda}{m}$", "$Q = \\dfrac{m}{\\lambda}$", "$Q = \\lambda \\cdot m \\cdot \\Delta t$"], 0, "Tại nhiệt độ nóng chảy, nhiệt lượng làm nóng chảy hoàn toàn khối lượng $m$ là $Q = \\lambda \\cdot m$."),
            mcq("biet", "Đơn vị đo của nhiệt nóng chảy riêng $\\lambda$ trong hệ SI là gì?", ["$\\text{J/kg}$", "$\\text{J/(kg}\\cdot\\text{K)}$", "$\\text{J}\\cdot\\text{kg}$", "$\\text{W/kg}$"], 0, "Vì $\\lambda = \\dfrac{Q}{m}$ nên đơn vị của nhiệt nóng chảy riêng là Joule trên kilôgam ($\\text{J/kg}$)."),
            mcq("hieu", "Vì sao để giữ cho thực phẩm tươi lâu trong thùng bảo quản, người ta dùng các tảng nước đá ở $0^\\circ\\text{C}$ hiệu quả hơn nhiều so với dùng cùng một khối lượng nước lạnh ở $0^\\circ\\text{C}$?", ["Vì khi $1\\text{ kg}$ nước đá ở $0^\\circ\\text{C}$ nóng chảy thành nước ở $0^\\circ\\text{C}$, nó thu thêm một nhiệt lượng rất lớn $\\lambda = 3{,}34 \\cdot 10^5\\text{ J}$ từ thực phẩm", "Vì nước đá ở $0^\\circ\\text{C}$ có nhiệt độ thấp hơn nước lỏng ở $0^\\circ\\text{C}$", "Vì nước đá không bao giờ tan", "Vì nước đá tỏa nhiệt lượng ra thùng"], 0, "Quá trình nóng chảy của nước đá ở $0^\\circ\\text{C}$ thu một nhiệt lượng ẩn rất lớn ($334\\text{ kJ}$ cho mỗi $\\text{kg}$ đá) giúp giữ nhiệt độ thùng ở $0^\\circ\\text{C}$ trong thời gian dài."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nhiệt nóng chảy riêng:", [
                "Nhiệt nóng chảy riêng của một chất phụ thuộc vào bản chất của chất rắn kết tinh đó.",
                "Trong suốt quá trình nước đá đang nóng chảy ở $0^\\circ\\text{C}$, nhiệt lượng cung cấp làm tăng thế năng tương tác giữa các phân tử còn động năng trung bình của phân tử không đổi.",
                "Khi $1\\text{ kg}$ nước ở $0^\\circ\\text{C}$ đông đặc hoàn toàn thành nước đá ở $0^\\circ\\text{C}$, nó cũng thu vào nhiệt lượng $\\lambda = 3{,}34 \\cdot 10^5\\text{ J}$.",
                "Để làm nóng chảy một thỏi kim loại đang ở nhiệt độ phòng $25^\\circ\\text{C}$, ta phải cung cấp nhiệt lượng gồm cả phần làm tăng nhiệt độ lên điểm nóng chảy và phần nhiệt nóng chảy $\\lambda m$.",
            ], [True, True, False, True], "Ý c) sai vì quá trình nóng chảy thu nhiệt còn quá trình ngược lại (đông đặc) là quá trình **tỏa nhiệt** ra môi trường."),
            short("vandung", "Biết nhiệt nóng chảy riêng của nước đá là $\\lambda = 330\\text{ kJ/kg}$. Nhiệt lượng $Q$ cần cung cấp để làm nóng chảy hoàn toàn $m = 0{,}5\\text{ kg}$ nước đá đang ở $0^\\circ\\text{C}$ bằng bao nhiêu $\\text{kJ}$?", ["165"], "Áp dụng công thức $Q = \\lambda \\cdot m = 330 \\cdot 0{,}5 = 165\\text{ kJ}$.", unit="kJ"),
        ],
    ),
    bai(
        topic=CH1[0], chapter_title=CH1[1], chapter_desc=CH1[2],
        title="Bài 6: Nhiệt hóa hơi riêng",
        icon="♨️",
        description="Khái niệm và đơn vị nhiệt hóa hơi riêng L (J/kg), công thức tính nhiệt lượng hóa hơi Q = L.m và bài toán đun sôi hóa hơi nước.",
        requirements=[
            "Định nghĩa được nhiệt hóa hơi riêng $L$ của một chất lỏng là nhiệt lượng cần truyền cho $1\\text{ kg}$ chất lỏng đó để nó hóa hơi hoàn toàn ở một nhiệt độ xác định (đơn vị $\\text{J/kg}$).",
            "Viết và vận dụng được công thức tính nhiệt lượng hóa hơi $Q = L \\cdot m$ (với $m$ là khối lượng phần chất lỏng đã chuyển thành hơi).",
            "Giải được bài toán tổng hợp đun nước từ nhiệt độ $t_1$ lên $100^\\circ\\text{C}$ rồi hóa hơi: $Q = m_{\\text{nước}} c (100 - t_1) + L \\cdot m_{\\text{hơi}}$.",
        ],
        definition="Nhiệt hóa hơi riêng ($L$) của một chất lỏng là nhiệt lượng cần truyền cho một đơn vị khối lượng ($1\\text{ kg}$) chất lỏng đó để nó chuyển hoàn toàn sang thể khí (hơi) ở một nhiệt độ xác định: $L = \\dfrac{Q}{m} \\iff Q = L \\cdot m$ (đơn vị $\\text{J/kg}$).",
        theory=(
            "### 1. Nhiệt hóa hơi riêng và Công thức tính nhiệt lượng hóa hơi\n"
            "- Kí hiệu: $L$, đơn vị trong hệ SI là **Joule trên kilôgam** ($\\text{J/kg}$). Ví dụ của nước ở $100^\\circ\\text{C}$: $L \\approx 2{,}26 \\cdot 10^6\\text{ J/kg}$ (rất lớn, gấp gần $7$ lần nhiệt nóng chảy riêng của nước đá!).\n"
            "- Nhiệt lượng cần truyền để một lượng chất lỏng có khối lượng $m$ hóa hơi hoàn toàn ở nhiệt độ không đổi:\n"
            "  $$Q = L \\cdot m$$\n"
            "- Ngược lại, khi một lượng hơi có khối lượng $m$ **ngưng tụ** thành chất lỏng ở cùng nhiệt độ đó, nó cũng **tỏa ra** nhiệt lượng cực lớn đúng bằng $Q = L \\cdot m$ (đó là lí do bỏng hơi nước ở $100^\\circ\\text{C}$ nguy hiểm hơn bỏng nước sôi ở $100^\\circ\\text{C}$).\n\n"
            "### 2. Bài toán đun nước từ $t_1 < 100^\\circ\\text{C}$ đến khi hóa hơi\n"
            "- Đun khối lượng $m$ nước từ $t_1$ đến sôi ở $100^\\circ\\text{C}$ rồi làm hóa hơi một phần khối lượng $m_h \\le m$:\n"
            "  $$Q = m \\cdot c \\cdot (100 - t_1) + L \\cdot m_h$$\n"
            "- **Thực hành đo $L$ của nước**: Đun nước đang sôi bằng ấm điện công suất $\\mathcal{P}$ đặt trên cân điện tử; trong thời gian $\\Delta t$, khối lượng nước giảm đi $\\Delta m$ (đã bay hơi): $L = \\dfrac{\\mathcal{P} \\cdot \\Delta t}{\\Delta m}$."
        ),
        formulas=[
            G(
                "Công thức Nhiệt hóa hơi riêng",
                F("Nhiệt lượng hóa hơi ở nhiệt độ sôi", "$Q = L \\cdot m \\iff L = \\dfrac{Q}{m}$", "Trong đó $m$ là khối lượng phần chất lỏng đã biến thành hơi ($\\text{kg}$), $L$ là nhiệt hóa hơi riêng ($\\text{J/kg}$), $Q$ tính bằng $\\text{J}$."),
                F("Tổng nhiệt lượng đun sôi và hóa hơi + Công thức thực hành", "$Q = m c (100 - t_1) + L \\cdot m_{\\text{hơi}}; \\qquad L = \\dfrac{\\mathcal{P} \\cdot \\Delta t}{\\Delta m}$", "Trong bài thực hành, phải mở nắp bình đun khi nước sôi để hơi nước thoát ra ngoài giúp cân điện tử đo đúng khối lượng hơi thoát đi $\\Delta m$."),
            )
        ],
        example="Tính nhiệt lượng $Q$ cần cung cấp để đun $m = 1\\text{ kg}$ nước từ nhiệt độ $t_1 = 20^\\circ\\text{C}$ đến khi sôi ở $100^\\circ\\text{C}$ và làm cho $0{,}2\\text{ kg}$ nước trong số đó hóa hơi hoàn toàn ở $100^\\circ\\text{C}$. Biết nhiệt dung riêng của nước là $c = 4200\\text{ J/(kg}\\cdot\\text{K)}$ và nhiệt hóa hơi riêng của nước ở $100^\\circ\\text{C}$ là $L = 2{,}26 \\cdot 10^6\\text{ J/kg}$.",
        example_answer="Nhiệt lượng cần để đun $1\\text{ kg}$ nước từ $20^\\circ\\text{C}$ lên $100^\\circ\\text{C}$ là $Q_1 = m c (100 - 20) = 1 \\cdot 4200 \\cdot 80 = 336\\,000\\text{ J} = 336\\text{ kJ}$. Nhiệt lượng cần để làm hóa hơi $m_h = 0{,}2\\text{ kg}$ nước ở $100^\\circ\\text{C}$ là $Q_2 = L \\cdot m_h = 2{,}26 \\cdot 10^6 \\cdot 0{,}2 = 452\\,000\\text{ J} = 452\\text{ kJ}$. Tổng nhiệt lượng cần cung cấp là $Q = Q_1 + Q_2 = 336 + 452 = 788\\text{ kJ}$.",
        real_life="Các máy điều hòa nhiệt độ và tủ lạnh hoạt động dựa trên chu trình cho môi chất lạnh (gas lạnh) bay hơi thu nhiệt ở dàn lạnh trong phòng rồi nén ngưng tụ tỏa nhiệt ra dàn nóng bên ngoài.",
        quiz=[
            mcq("biet", "Nhiệt lượng $Q$ cần cung cấp để làm hóa hơi hoàn toàn một lượng chất lỏng có khối lượng $m$ ở nhiệt độ sôi (với $L$ là nhiệt hóa hơi riêng ở nhiệt độ đó) được tính bằng công thức nào?", ["$Q = L \\cdot m$", "$Q = \\dfrac{L}{m}$", "$Q = \\dfrac{m}{L}$", "$Q = L \\cdot m \\cdot \\Delta t$"], 0, "Nhiệt lượng làm hóa hơi hoàn toàn khối lượng $m$ ở nhiệt độ xác định là $Q = L \\cdot m$."),
            mcq("biet", "Đơn vị của nhiệt hóa hơi riêng $L$ trong hệ SI là gì?", ["$\\text{J/kg}$", "$\\text{J/(kg}\\cdot\\text{K)}$", "$\\text{J/K}$", "$\\text{W}\\cdot\\text{kg}$"], 0, "Vì $L = \\dfrac{Q}{m}$ nên đơn vị của nhiệt hóa hơi riêng là $\\text{J/kg}$."),
            mcq("hieu", "Vì sao bị bỏng do hơi nước đang sôi ở $100^\\circ\\text{C}$ lại gây tổn thương nặng hơn rất nhiều so với bị bỏng do cùng một khối lượng nước lỏng ở $100^\\circ\\text{C}$?", ["Vì khi hơi nước ở $100^\\circ\\text{C}$ ngưng tụ trên da thành nước ở $100^\\circ\\text{C}$, nó tỏa thêm một nhiệt lượng cực lớn $Q = L \\cdot m$ (với $L \\approx 2{,}26 \\cdot 10^6\\text{ J/kg}$)", "Vì hơi nước ở $100^\\circ\\text{C}$ có nhiệt độ cao hơn nước sôi ở $100^\\circ\\text{C}$", "Vì hơi nước có khối lượng riêng lớn hơn nước lỏng", "Vì hơi nước không truyền nhiệt cho da"], 0, "Mỗi kilôgam hơi nước ở $100^\\circ\\text{C}$ khi ngưng tụ thành nước ở $100^\\circ\\text{C}$ tỏa ra thêm $2{,}26 \\cdot 10^6\\text{ J}$ nhiệt lượng trước khi nguội xuống nhiệt độ của da."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nhiệt hóa hơi riêng:", [
                "Nhiệt hóa hơi riêng của một chất lỏng phụ thuộc vào bản chất của chất lỏng và nhiệt độ mà tại đó chất lỏng bay hơi.",
                "Trong thí nghiệm đo nhiệt hóa hơi riêng của nước đang sôi bằng cân điện tử, ta phải mở nắp bình đun để hơi nước bay thoát ra ngoài.",
                "Trong suốt thời gian nước đang sôi và hóa hơi ở áp suất chuẩn, nhiệt độ của nước tăng đều từ $100^\\circ\\text{C}$ lên $200^\\circ\\text{C}$.",
                "Nếu ấm đun công suất $\\mathcal{P} = 1000\\text{ W}$ làm bay hơi $\\Delta m = 0{,}05\\text{ kg}$ nước đang sôi trong $\\Delta t = 113\\text{ s}$ thì nhiệt hóa hơi riêng đo được là $L = \\dfrac{1000 \\cdot 113}{0{,}05} = 2{,}26 \\cdot 10^6\\text{ J/kg}$.",
            ], [True, True, False, True], "Ý c) sai vì trong suốt quá trình nước đang sôi ở áp suất không đổi, nhiệt độ của nước giữ nguyên ở $100^\\circ\\text{C}$."),
            short("vandung", "Biết nhiệt hóa hơi riêng của nước ở $100^\\circ\\text{C}$ là $L = 2260\\text{ kJ/kg}$. Nhiệt lượng $Q$ cần cung cấp để làm hóa hơi hoàn toàn $m = 0{,}5\\text{ kg}$ nước đang sôi ở $100^\\circ\\text{C}$ bằng bao nhiêu $\\text{kJ}$?", ["1130"], "Áp dụng công thức $Q = L \\cdot m = 2260 \\cdot 0{,}5 = 1130\\text{ kJ}$.", unit="kJ"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 7: Mô hình động học phân tử chất khí",
        icon="💨",
        description="Chuyển động Brown, 3 nội dung của mô hình động học phân tử chất khí, khí lí tưởng và công thức số mol n = m/M = N/N_A.",
        requirements=[
            "Mô tả được chuyển động Brown (chuyển động hỗn loạn, không ngừng theo quỹ đạo gấp khúc của các hạt nhỏ lơ lửng trong chất lỏng hay chất khí) là bằng chứng thực nghiệm của chuyển động phân tử.",
            "Trình bày được 3 giả thuyết của mô hình khí lí tưởng (coi phân tử khí là các chất điểm, chỉ tương tác khi va chạm đàn hồi với nhau và với thành bình) và giải thích cơ chế gây ra áp suất chất khí lên thành bình.",
            "Vận dụng được công thức tính lượng chất (số mol) $n = \\dfrac{m}{M} = \\dfrac{N}{N_A}$ với hằng số Avogadro $N_A \\approx 6{,}02 \\cdot 10^{23}\\text{ mol}^{-1}$.",
        ],
        definition="Trong mô hình khí lí tưởng, các phân tử khí được coi là các chất điểm chuyển động hỗn loạn không ngừng, chỉ tương tác với nhau khi va chạm trực tiếp và va chạm đàn hồi với thành bình tạo nên áp suất chất khí. Số mol chất khí được tính bởi: $n = \\dfrac{m}{M} = \\dfrac{N}{N_A}$ (với $N_A = 6{,}02 \\cdot 10^{23}\\text{ mol}^{-1}$).",
        theory=(
            "### 1. Chuyển động Brown và Mô hình động học phân tử chất khí\n"
            "- **Chuyển động Brown (1827)**: các hạt phấn hoa (hoặc hạt khói) chuyển động hỗn loạn không ngừng theo quỹ đạo những đường gấp khúc bất kì do sự va chạm không cân bằng từ mọi phía của các phân tử nước (hoặc không khí).\n"
            "- **Ba nội dung của mô hình động học phân tử chất khí**:\n"
            "  1. Chất khí được cấu tạo từ các phân tử có kích thước rất nhỏ so với khoảng cách giữa chúng.\n"
            "  2. Các phân tử khí chuyển động hỗn loạn, không ngừng; nhiệt độ càng cao thì tốc độ chuyển động nhiệt càng lớn.\n"
            "  3. Khi chuyển động hỗn loạn, các phân tử khí va chạm vào nhau và **va chạm vào thành bình** gây ra **áp suất chất khí lên thành bình**.\n\n"
            "### 2. Khí lí tưởng và Lượng chất (Số mol)\n"
            "- **Khí lí tưởng**: chất khí mà các phân tử được coi là các **chất điểm** (bỏ qua thể tích riêng của phân tử) và **chỉ tương tác với nhau khi va chạm** (bỏ qua lực tương tác phân tử khi không va chạm).\n"
            "- **Số mol ($n$)** và **Số phân tử ($N$)**:\n"
            "  $$n = \\dfrac{m}{M} = \\dfrac{N}{N_A} \\implies N = n \\cdot N_A = \\dfrac{m}{M} N_A$$\n"
            "  với $M$ là khối lượng mol ($\\text{g/mol}$ hoặc $\\text{kg/mol}$) và $N_A \\approx 6{,}02 \\cdot 10^{23}\\text{ mol}^{-1}$ là hằng số Avogadro."
        ),
        formulas=[
            G(
                "Công thức Số mol và Số phân tử khí",
                F("Số mol chất khí theo khối lượng m và số phân tử N", "$n = \\dfrac{m}{M} = \\dfrac{N}{N_A} \\implies N = n \\cdot N_A = \\dfrac{m}{M} N_A$", "Trong đó $N_A \\approx 6{,}02 \\cdot 10^{23}\\text{ mol}^{-1}$ là số Avogadro; $m$ và $M$ phải để cùng đơn vị (cùng là $\\text{g}$ và $\\text{g/mol}$, hoặc cùng là $\\text{kg}$ và $\\text{kg/mol}$)."),
                F("Khối lượng của 1 phân tử khí và Mật độ phân tử", "$m_0 = \\dfrac{M}{N_A}; \\qquad \\mu = \\dfrac{N}{V} = \\dfrac{n \\cdot N_A}{V}$", "Trong đó $m_0$ là khối lượng của $1$ phân tử khí, $\\mu$ là mật độ phân tử (số phân tử trong $1\\text{ m}^3$)."),
            )
        ],
        example="Một bình kín chứa $m = 64\\text{ g}$ khí ôxi ($\\text{O}_2$, có khối lượng mol $M = 32\\text{ g/mol}$). Lấy số Avogadro $N_A = 6{,}02 \\cdot 10^{23}\\text{ mol}^{-1}$. Hãy tính số mol $n$ và tổng số phân tử khí ôxi $N$ có trong bình.",
        example_answer="Số mol khí ôxi trong bình là $n = \\dfrac{m}{M} = \\dfrac{64}{32} = 2\\text{ mol}$. Tổng số phân tử khí ôxi trong bình là $N = n \\cdot N_A = 2 \\cdot 6{,}02 \\cdot 10^{23} = 1{,}204 \\cdot 10^{24}$ phân tử.",
        real_life="Ở áp suất khí quyển thông thường và nhiệt độ phòng, không khí, khí ôxi, khí nitơ, khí heli đều tuân theo rất sát các định luật của mô hình khí lí tưởng.",
        quiz=[
            mcq("biet", "Trong mô hình **khí lí tưởng**, các phân tử khí được coi như thế nào?", ["Được coi là các chất điểm chuyển động hỗn loạn không ngừng và chỉ tương tác với nhau khi va chạm", "Là những quả cầu lớn xếp khít sát vào nhau", "Luôn đứng yên tại các nút mạng tinh thể", "Luôn hút nhau rất mạnh ngay cả khi ở rất xa nhau"], 0, "Trong mô hình khí lí tưởng, kích thước phân tử rất nhỏ được coi là chất điểm và bỏ qua lực tương tác khi chưa va chạm."),
            mcq("biet", "Nguyên nhân gây ra áp suất của chất khí lên thành bình chứa là gì?", ["Do hàng tỉ phân tử khí chuyển động nhiệt hỗn loạn va chạm liên tục vào thành bình từ mọi phía", "Do các phân tử khí đứng yên đè lên đáy bình", "Do lực hút của thành bình lên các hạt nhân", "Do chất khí tự nở thành chất rắn"], 0, "Khi chuyển động hỗn loạn, mỗi phân tử khí va chạm với thành bình tác dụng một lực nhỏ; tổng hợp vô số va chạm tạo nên áp suất liên tục lên thành bình."),
            mcq("hieu", "Công thức tính số phân tử $N$ có trong một khối lượng $m$ của chất khí có khối lượng mol $M$ (với $N_A$ là hằng số Avogadro) là gì?", ["$N = \\dfrac{m}{M} \\cdot N_A$", "$N = \\dfrac{M}{m} \\cdot N_A$", "$N = \\dfrac{m \\cdot M}{N_A}$", "$N = \\dfrac{N_A}{m \\cdot M}$"], 0, "Vì số mol $n = \\dfrac{m}{M} = \\dfrac{N}{N_A}$, nên $N = n \\cdot N_A = \\dfrac{m}{M} N_A$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về mô hình động học phân tử chất khí:", [
                "Quỹ đạo chuyển động Brown của các hạt khói lơ lửng trong không khí là những đường gấp khúc không theo một quy luật nào.",
                "Khi nhiệt độ của chất khí càng cao thì chuyển động Brown diễn ra càng nhanh và mạnh.",
                "Một mol của bất kì chất khí nào ở cùng điều kiện cũng chứa một số phân tử khác nhau tùy theo khối lượng mol.",
                "Một bình chứa $14\\text{ g}$ khí nitơ ($\\text{N}_2, M = 28\\text{ g/mol}$) tương ứng với số mol là $n = 0{,}5\\text{ mol}$.",
            ], [True, True, False, True], "Ý c) sai vì $1\\text{ mol}$ của mọi chất đều chứa cùng một số phân tử bằng hằng số Avogadro $N_A \\approx 6{,}02 \\cdot 10^{23}$ hạt."),
            short("vandung", "Một bình chứa $m = 12\\text{ g}$ khí heli ($\\text{He}$, có khối lượng mol $M = 4\\text{ g/mol}$). Số mol $n$ khí heli trong bình bằng bao nhiêu $\\text{mol}$?", ["3"], "Áp dụng công thức $n = \\dfrac{m}{M} = \\dfrac{12}{4} = 3\\text{ mol}$.", unit="mol"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 8: Định luật Boyle",
        icon="💉",
        description="Quá trình đẳng nhiệt (T = const), phát biểu và biểu thức Định luật Boyle p.V = const hay p₁V₁ = p₂V₂, đường đẳng nhiệt trong các hệ tọa độ.",
        requirements=[
            "Nêu được quá trình đẳng nhiệt là quá trình biến đổi trạng thái của một lượng khí xác định khi nhiệt độ được giữ không đổi ($T = \\text{const}$).",
            "Phát biểu và vận dụng được biểu thức của Định luật Boyle: ở nhiệt độ không đổi, áp suất của một khối lượng khí xác định tỉ lệ nghịch với thể tích của nó ($p V = \\text{const} \\iff p_1 V_1 = p_2 V_2$).",
            "Nhận biết được đường đẳng nhiệt trong hệ tọa độ $(p, V)$ là một nhánh hypebol (đường ở trên ứng với nhiệt độ cao hơn: $T_2 > T_1$) và trong hệ $(p, T)$ hoặc $(V, T)$ là đoạn thẳng vuông góc với trục $OT$.",
        ],
        definition="Định luật Boyle: Với một khối lượng khí xác định khi giữ nhiệt độ không đổi (quá trình đẳng nhiệt), áp suất $p$ tỉ lệ nghịch với thể tích $V$ của nó: $p \\cdot V = \\text{const} \\iff p_1 V_1 = p_2 V_2$.",
        theory=(
            "### 1. Quá trình đẳng nhiệt và Định luật Boyle\n"
            "- **Ba thông số trạng thái** của một lượng khí xác định: áp suất $p$, thể tích $V$ và nhiệt độ tuyệt đối $T$.\n"
            "- **Quá trình đẳng nhiệt**: quá trình biến đổi trạng thái trong đó nhiệt độ được giữ không đổi ($T = \\text{const}$).\n"
            "- **Định luật Boyle (Robert Boyle)**:\n"
            "  $$p \\sim \\dfrac{1}{V} \\iff p \\cdot V = \\text{hằng số} \\iff p_1 V_1 = p_2 V_2$$\n"
            "- *Giải thích bằng thuyết động học phân tử*: Khi $T$ không đổi, tốc độ trung bình của phân tử không đổi; nếu nén thể tích $V$ giảm đi $k$ lần thì mật độ phân tử $\\mu = \\dfrac{N}{V}$ tăng lên $k$ lần, số va chạm lên thành bình tăng $k$ lần nên áp suất $p$ tăng $k$ lần.\n\n"
            "### 2. Đường đẳng nhiệt\n"
            "- Trong hệ tọa độ $(p, V)$: đường đẳng nhiệt là một **nhánh đường hypebol**. Cùng một lượng khí, đường đẳng nhiệt nằm ở phía trên (xa gốc tọa độ hơn) ứng với nhiệt độ cao hơn ($T_2 > T_1$).\n"
            "- Trong hệ tọa độ $(p, T)$ hoặc $(V, T)$: đường đẳng nhiệt là một **đoạn thẳng vuông góc với trục nhiệt độ tuyệt đối $OT$**."
        ),
        formulas=[
            G(
                "Biểu thức Định luật Boyle (Quá trình đẳng nhiệt T = const)",
                F("Hệ thức Định luật Boyle cho hai trạng thái (1) và (2)", "$p_1 \\cdot V_1 = p_2 \\cdot V_2 = \\text{const} \\implies p_2 = p_1 \\cdot \\dfrac{V_1}{V_2}$", "Hai đại lượng $p_1, p_2$ chỉ cần cùng đơn vị ($\\text{Pa}, \\text{kPa}, \\text{atm}, \\text{bar}$) và $V_1, V_2$ cùng đơn vị ($\\text{L}, \\text{cm}^3, \\text{m}^3$)."),
                F("Bài toán bơm khí đẳng nhiệt (n lần bơm ống thể tích V₀ vào bình V)", "$p_0 (V + n V_0) = p_2 V \\quad (\\text{nếu ban đầu trong bình đã có khí ở } p_0)$", "Nếu ban đầu bình rỗng hoàn toàn thì $p_0 \\cdot (n V_0) = p_2 \\cdot V$."),
            )
        ],
        example="Một xi-lanh kín chứa $V_1 = 6\\text{ lít}$ khí ở áp suất $p_1 = 1{,}5\\text{ atm}$. Người ta đẩy pít-tông nén chậm khối khí để nhiệt độ không đổi cho đến khi thể tích khí giảm xuống còn $V_2 = 2\\text{ lít}$. Hãy tính áp suất $p_2$ của khối khí lúc này.",
        example_answer="Vì quá trình nén chậm giữ nhiệt độ không đổi (đẳng nhiệt), áp dụng định luật Boyle: $p_1 V_1 = p_2 V_2 \\implies p_2 = \\dfrac{p_1 V_1}{V_2} = \\dfrac{1{,}5 \\cdot 6}{2} = 4{,}5\\text{ atm}$.",
        real_life="Hoạt động hít vào – thở ra của phổi người tuân theo định luật Boyle: khi cơ hoành hạ xuống làm thể tích lồng ngực $V$ tăng lên, áp suất khí trong phổi $p$ giảm nhỏ hơn áp suất khí quyển nên không khí tự tràn từ mũi vào phổi.",
        quiz=[
            mcq("biet", "Hệ thức nào sau đây biểu diễn đúng **Định luật Boyle** cho quá trình đẳng nhiệt của một lượng khí xác định từ trạng thái $(p_1, V_1)$ sang trạng thái $(p_2, V_2)$?", ["$p_1 V_1 = p_2 V_2$", "$\\dfrac{p_1}{V_1} = \\dfrac{p_2}{V_2}$", "$p_1 + V_1 = p_2 + V_2$", "$\\dfrac{p_1}{p_2} = \\dfrac{V_1}{V_2}$"], 0, "Trong quá trình đẳng nhiệt, tích của áp suất và thể tích là hằng số: $p_1 V_1 = p_2 V_2$."),
            mcq("biet", "Trong hệ tọa độ $(p, V)$ (trục hoành là thể tích $V$, trục tung là áp suất $p$), đường đẳng nhiệt của một lượng khí lí tưởng có dạng đường gì?", ["Một nhánh đường hypebol", "Một đường thẳng đi qua gốc tọa độ", "Một đường tròn", "Một đường thẳng song song với trục hoành"], 0, "Vì $p = \\dfrac{\\text{const}}{V}$ là hàm phân thức bậc nhất nên đồ thị trong hệ $(p, V)$ là một nhánh hypebol."),
            mcq("hieu", "Nén đẳng nhiệt một khối lượng khí xác định sao cho thể tích của nó giảm đi $4$ lần thì áp suất của khối khí đó thay đổi như thế nào?", ["Áp suất tăng lên $4$ lần", "Áp suất giảm đi $4$ lần", "Áp suất tăng lên $16$ lần", "Áp suất không thay đổi"], 0, "Theo định luật Boyle ($p V = \\text{const}$), khi thể tích $V$ giảm $4$ lần thì áp suất $p$ tăng lên $4$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về quá trình đẳng nhiệt và định luật Boyle:", [
                "Định luật Boyle chỉ áp dụng cho một khối lượng khí xác định (không rò rỉ hoặc bơm thêm khí) khi nhiệt độ không đổi.",
                "Trong hệ tọa độ $(p, T)$, đường đẳng nhiệt là một đoạn thẳng vuông góc với trục nhiệt độ tuyệt đối $OT$.",
                "Khi dãn nở đẳng nhiệt một khối khí, mật độ phân tử khí trong bình tăng lên.",
                "Một bọt khí nổi từ đáy hồ (nơi áp suất bằng $3\\text{ atm}$) lên sát mặt nước (áp suất $1\\text{ atm}$, coi nhiệt độ nước không đổi theo độ sâu) thì thể tích bọt khí tăng gấp $3$ lần.",
            ], [True, True, False, True], "Ý c) sai vì khi dãn nở đẳng nhiệt thì thể tích $V$ tăng nên mật độ phân tử $\\mu = \\dfrac{N}{V}$ giảm đi."),
            short("vandung", "Một lượng khí có thể tích $V_1 = 8\\text{ lít}$ ở áp suất $p_1 = 2\\text{ bar}$. Khi dãn đẳng nhiệt đến áp suất $p_2 = 1\\text{ bar}$ thì thể tích $V_2$ của lượng khí đó bằng bao nhiêu lít?", ["16"], "Áp dụng định luật Boyle: $p_1 V_1 = p_2 V_2 \\implies V_2 = \\dfrac{p_1 V_1}{p_2} = \\dfrac{2 \\cdot 8}{1} = 16\\text{ lít}$.", unit="lít"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 9: Định luật Charles",
        icon="🎈",
        description="Quá trình đẳng áp (p = const), phát biểu và biểu thức Định luật Charles V/T = const hay V₁/T₁ = V₂/T₂, đường đẳng áp trong hệ tọa độ (V, T).",
        requirements=[
            "Nêu được quá trình đẳng áp là quá trình biến đổi trạng thái của một lượng khí xác định khi áp suất được giữ không đổi ($p = \\text{const}$).",
            "Phát biểu và vận dụng được biểu thức của Định luật Charles: khi áp suất của một khối lượng khí xác định được giữ không đổi thì thể tích của khí tỉ lệ thuận với nhiệt độ tuyệt đối của nó ($\\dfrac{V}{T} = \\text{const} \\iff \\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$).",
            "Nhận biết được đường đẳng áp trong hệ tọa độ $(V, T)$ là đường thẳng có đường kéo dài đi qua gốc tọa độ tuyệt đối $0\\text{ K}$ (độ dốc nhỏ hơn ứng với áp suất lớn hơn).",
        ],
        definition="Định luật Charles: Khi áp suất của một khối lượng khí xác định được giữ không đổi (quá trình đẳng áp), thì thể tích $V$ của khí tỉ lệ thuận với nhiệt độ tuyệt đối $T$ của nó: $\\dfrac{V}{T} = \\text{const} \\iff \\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$.",
        theory=(
            "### 1. Quá trình đẳng áp và Định luật Charles\n"
            "- **Quá trình đẳng áp**: quá trình biến đổi trạng thái của một lượng khí xác định khi áp suất được giữ không đổi ($p = \\text{const}$, ví dụ khối khí trong xi-lanh có pít-tông chuyển động tự do không ma sát).\n"
            "- **Định luật Charles (Jacques Charles)**:\n"
            "  $$\\dfrac{V}{T} = \\text{hằng số} \\iff \\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$$\n"
            "  *(Lưu ý bắt buộc: Nhiệt độ $T_1, T_2$ trong công thức phải đổi sang thang Kelvin: $T(\\text{K}) = t(^\\circ\\text{C}) + 273$!)*\n"
            "- Liên hệ với thể tích $V_0$ ở $0^\\circ\\text{C}$ ($T_0 = 273\\text{ K}$): $V = V_0\\left(1 + \\dfrac{t}{273}\\right)$.\n\n"
            "### 2. Đường đẳng áp\n"
            "- Trong hệ tọa độ $(V, T)$: đường đẳng áp là **đường thẳng mà đường kéo dài đi qua gốc tọa độ tuyệt đối $O(0\\text{ K}; 0)$**. Với hai đường đẳng áp của cùng một lượng khí, đường nằm dưới (gần trục $OT$ hơn) có áp suất lớn hơn ($p_2 > p_1$).\n"
            "- Trong hệ tọa độ $(p, V)$ hoặc $(p, T)$: đường đẳng áp là **đoạn thẳng vuông góc với trục áp suất $Op$**."
        ),
        formulas=[
            G(
                "Biểu thức Định luật Charles (Quá trình đẳng áp p = const)",
                F("Hệ thức Định luật Charles", "$\\dfrac{V}{T} = \\text{const} \\iff \\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2} \\implies V_2 = V_1 \\cdot \\dfrac{T_2}{T_1}$", "Bắt buộc phải đổi nhiệt độ ra Kelvin ($T = t + 273$) trước khi thay vào tỉ lệ thức!"),
                F("Công thức nở đẳng áp theo độ Celsius", "$V = V_0 (1 + \\alpha_V t) \\quad \\text{với } \\alpha_V = \\dfrac{1}{273}\\text{ K}^{-1}$", "Trong đó $V_0$ là thể tích của khối khí ở $0^\\circ\\text{C}$ ($273\\text{ K}$)."),
            )
        ],
        example="Một khối khí xác định có thể tích $V_1 = 3\\text{ lít}$ ở nhiệt độ $t_1 = 27^\\circ\\text{C}$. Khi đun nóng đẳng áp khối khí đó lên đến nhiệt độ $t_2 = 127^\\circ\\text{C}$ thì thể tích $V_2$ của khối khí bằng bao nhiêu lít?",
        example_answer="Đổi nhiệt độ ra thang Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$ và $T_2 = 127 + 273 = 400\\text{ K}$. Áp dụng định luật Charles cho quá trình đẳng áp: $\\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2} \\implies V_2 = V_1 \\cdot \\dfrac{T_2}{T_1} = 3 \\cdot \\dfrac{400}{300} = 4\\text{ lít}$.",
        real_life="Đèn trời hoặc khinh khí cầu đốt nóng không khí bên trong vòm cầu ở áp suất khí quyển không đổi ($p = p_0$), làm không khí dãn nở theo định luật Charles khiến khối lượng riêng của khí nóng giảm nhỏ hơn không khí lạnh xung quanh và bay lên.",
        quiz=[
            mcq("biet", "Biểu thức nào sau đây biểu diễn đúng **Định luật Charles** cho quá trình đẳng áp của một khối lượng khí xác định?", ["$\\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$ (với $T$ là nhiệt độ tuyệt đối Kelvin)", "$V_1 T_1 = V_2 T_2$", "$\\dfrac{V_1}{t_1} = \\dfrac{V_2}{t_2}$ (với $t$ tính bằng $^\\circ\\text{C}$)", "$p_1 V_1 = p_2 V_2$"], 0, "Trong quá trình đẳng áp, thể tích tỉ lệ thuận với nhiệt độ tuyệt đối $T(\\text{K})$: $\\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$."),
            mcq("biet", "Trong hệ tọa độ $(V, T)$ (trục hoành là nhiệt độ tuyệt đối $T$, trục tung là thể tích $V$), đường đẳng áp của một lượng khí xác định có dạng gì?", ["Một đường thẳng mà đường kéo dài đi qua gốc tọa độ $O(0\\text{ K}; 0)$", "Một nhánh đường hypebol", "Một đường thẳng vuông góc với trục $OT$", "Một đường parabol"], 0, "Vì $V = \\text{const} \\cdot T$ nên đường đẳng áp trong hệ $(V, T)$ là đường thẳng có đường kéo dài đi qua gốc tọa độ $0\\text{ K}$."),
            mcq("hieu", "Khi nung nóng đẳng áp một khối lượng khí xác định sao cho nhiệt độ tuyệt đối $T(\\text{K})$ của nó tăng lên gấp $2$ lần thì thể tích $V$ của khối khí thay đổi như thế nào?", ["Thể tích tăng lên gấp $2$ lần", "Thể tích giảm đi $2$ lần", "Thể tích tăng lên gấp $4$ lần", "Thể tích không đổi"], 0, "Theo định luật Charles ($\\dfrac{V}{T} = \\text{const}$), khi nhiệt độ tuyệt đối $T$ tăng gấp $2$ lần thì thể tích $V$ cũng tăng gấp $2$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về quá trình đẳng áp và định luật Charles:", [
                "Khi đun nóng đẳng áp một lượng khí từ $20^\\circ\\text{C}$ lên $40^\\circ\\text{C}$ thì thể tích của nó tăng lên gấp đôi.",
                "Mọi chất khí lí tưởng đều có cùng hệ số nở đẳng áp $\\alpha = \\dfrac{1}{273}\\text{ K}^{-1}$.",
                "Trong quá trình dãn nở đẳng áp ($V$ tăng, $T$ tăng), khối khí vừa nhận nhiệt lượng vừa thực hiện công đẩy pít-tông.",
                "Ở $27^\\circ\\text{C}$ ($300\\text{ K}$) một lượng khí có thể tích $6\\text{ lít}$; khi làm lạnh đẳng áp xuống $-23^\\circ\\text{C}$ ($250\\text{ K}$) thì thể tích khí còn $5\\text{ lít}$.",
            ], [False, True, True, True], "Ý a) sai vì thể tích tỉ lệ thuận với nhiệt độ tuyệt đối $T(\\text{K})$ chứ không tỉ lệ thuận với $t(^\\circ\\text{C})$: $\\dfrac{V_2}{V_1} = \\dfrac{40+273}{20+273} = \\dfrac{313}{293} \\ne 2$."),
            short("vandung", "Một lượng khí xác định ở nhiệt độ $t_1 = 27^\\circ\\text{C}$ ($T_1 = 300\\text{ K}$) có thể tích $V_1 = 6\\text{ lít}$. Khi đun nóng đẳng áp lên nhiệt độ $t_2 = 177^\\circ\\text{C}$ ($T_2 = 450\\text{ K}$) thì thể tích $V_2$ của lượng khí bằng bao nhiêu lít?", ["9"], "Áp dụng định luật Charles: $V_2 = V_1 \\cdot \\dfrac{T_2}{T_1} = 6 \\cdot \\dfrac{450}{300} = 9\\text{ lít}$.", unit="lít"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 10: Phương trình trạng thái của khí lí tưởng",
        icon="⚗️",
        description="Phương trình trạng thái khí lí tưởng pV/T = const, quá trình đẳng tích p/T = const và phương trình Clapeyron pV = nRT.",
        requirements=[
            "Kết hợp định luật Boyle và định luật Charles để thiết lập và vận dụng phương trình trạng thái của một lượng khí lí tưởng xác định: $\\dfrac{pV}{T} = \\text{const} \\iff \\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2}$.",
            "Suy ra được hệ thức cho quá trình đẳng tích ($V = \\text{const}$): $\\dfrac{p}{T} = \\text{const} \\iff \\dfrac{p_1}{T_1} = \\dfrac{p_2}{T_2}$.",
            "Viết và vận dụng được phương trình Clapeyron (Clapeyron–Mendeleev): $pV = nRT = \\dfrac{m}{M}RT$ với hằng số khí lí tưởng $R \\approx 8{,}31\\text{ J/(mol}\\cdot\\text{K)}$ hoặc $R \\approx 0{,}082\\text{ atm}\\cdot\\text{L/(mol}\\cdot\\text{K)}$.",
        ],
        definition="Đối với một khối lượng khí lí tưởng xác định, tỉ số giữa tích của áp suất $p$ và thể tích $V$ với nhiệt độ tuyệt đối $T$ là một hằng số: $\\dfrac{pV}{T} = \\text{const} \\iff \\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2}$. Với $n$ mol khí lí tưởng, ta có phương trình Clapeyron: $pV = nRT$.",
        theory=(
            "### 1. Phương trình trạng thái của một lượng khí xác định và Quá trình đẳng tích\n"
            "- **Phương trình trạng thái**:\n"
            "  $$\\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2} \\iff \\dfrac{pV}{T} = \\text{const}$$\n"
            "  - Khi $T_1 = T_2$ (đẳng nhiệt): trở về định luật Boyle $p_1 V_1 = p_2 V_2$.\n"
            "  - Khi $p_1 = p_2$ (đẳng áp): trở về định luật Charles $\\dfrac{V_1}{T_1} = \\dfrac{V_2}{T_2}$.\n"
            "  - Khi **$V_1 = V_2$ (quá trình đẳng tích – bình kín có thể tích không đổi)**: áp suất tỉ lệ thuận với nhiệt độ tuyệt đối:\n"
            "    $$\\dfrac{p_1}{T_1} = \\dfrac{p_2}{T_2} \\iff \\dfrac{p}{T} = \\text{const}$$\n"
            "    *(Trong quá trình đẳng tích, vì $\\Delta V = 0$ nên khối khí không sinh công $A = 0 \\implies \\Delta U = Q$).* \n\n"
            "### 2. Phương trình Clapeyron (Clapeyron – Mendeleev)\n"
            "- Xét $n$ mol khí lí tưởng:\n"
            "  $$p \\cdot V = n \\cdot R \\cdot T = \\dfrac{m}{M} R T$$\n"
            "- **Hai hệ đơn vị thường dùng của hằng số khí $R$**:\n"
            "  1. **Hệ chuẩn SI**: $p$ ($\\text{Pa} = \\text{N/m}^2$), $V$ ($\\text{m}^3$), $T$ ($\\text{K}$) $\\implies R \\approx 8{,}31\\text{ J/(mol}\\cdot\\text{K)}$.\n"
            "  2. **Hệ atm – lít**: $p$ ($\\text{atm}$), $V$ ($\\text{lít}$), $T$ ($\\text{K}$) $\\implies R \\approx 0{,}082\\text{ atm}\\cdot\\text{L/(mol}\\cdot\\text{K)}$ (ở ĐKTC $0^\\circ\\text{C} = 273\\text{ K}, 1\\text{ atm}$, $1\\text{ mol}$ khí có thể tích $22{,}4\\text{ lít}$)."
        ),
        formulas=[
            G(
                "Phương trình trạng thái khí lí tưởng, Đẳng tích và Phương trình Clapeyron",
                F("Phương trình trạng thái và Quá trình đẳng tích (V = const)", "$\\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2}; \\qquad \\text{Đẳng tích } (V_1 = V_2): \\dfrac{p_1}{T_1} = \\dfrac{p_2}{T_2}$", "Nhiệt độ $T_1, T_2$ luôn phải tính bằng Kelvin ($T = t + 273$)."),
                F("Phương trình Clapeyron và Khối lượng riêng của khí", "$p V = n R T = \\dfrac{m}{M} R T \\implies D = \\dfrac{m}{V} = \\dfrac{p M}{R T}$", "Trong hệ SI: $p(\\text{Pa}), V(\\text{m}^3), R = 8{,}31\\text{ J/(mol}\\cdot\\text{K)}$. Trong hệ atm-lít: $p(\\text{atm}), V(\\text{L}), R = 0{,}082$."),
            )
        ],
        example="Trong xi-lanh của một động cơ có chứa một lượng khí ở nhiệt độ $t_1 = 27^\\circ\\text{C}$, thể tích $V_1 = 10\\text{ lít}$ và áp suất $p_1 = 1\\text{ atm}$. Sau khi pít-tông nén, thể tích của khí giảm còn $V_2 = 2\\text{ lít}$ và nhiệt độ tăng lên đến $t_2 = 327^\\circ\\text{C}$. Hãy tính áp suất $p_2$ của khí trong xi-lanh lúc đó.",
        example_answer="Đổi nhiệt độ sang Kelvin: $T_1 = 27 + 273 = 300\\text{ K}$ và $T_2 = 327 + 273 = 600\\text{ K}$. Áp dụng phương trình trạng thái của khí lí tưởng: $\\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2} \\implies p_2 = p_1 \\cdot \\dfrac{V_1}{V_2} \\cdot \\dfrac{T_2}{T_1} = 1 \\cdot \\dfrac{10}{2} \\cdot \\dfrac{600}{300} = 10\\text{ atm}$.",
        real_life="Nồi áp suất nấu thức ăn chín nhừ rất nhanh và các bình xịt (bình gas mini, bình cứu hỏa) không được để ngoài nắng gắt vì trong bình kín thể tích không đổi ($V = \\text{const}$), khi nhiệt độ $T$ tăng thì áp suất $p$ tăng tỉ lệ thuận có thể gây nổ nếu không có van an toàn.",
        quiz=[
            mcq("biet", "Phương trình nào sau đây là **phương trình trạng thái của một lượng khí lí tưởng xác định** chuyển từ trạng thái $(p_1, V_1, T_1)$ sang trạng thái $(p_2, V_2, T_2)$?", ["$\\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2}$", "$p_1 V_1 T_1 = p_2 V_2 T_2$", "$\\dfrac{p_1 T_1}{V_1} = \\dfrac{p_2 T_2}{V_2}$", "$\\dfrac{V_1 T_1}{p_1} = \\dfrac{V_2 T_2}{p_2}$"], 0, "Phương trình trạng thái của một lượng khí lí tưởng xác định là $\\dfrac{p_1 V_1}{T_1} = \\dfrac{p_2 V_2}{T_2}$."),
            mcq("biet", "Phương trình Clapeyron liên hệ giữa áp suất $p$, thể tích $V$, nhiệt độ tuyệt đối $T$ và số mol $n$ của một khối khí lí tưởng là gì?", ["$p V = n R T$", "$\\dfrac{p V}{n} = \\dfrac{R}{T}$", "$p T = n R V$", "$p R = n V T$"], 0, "Phương trình Clapeyron đối với $n$ mol khí lí tưởng là $p V = n R T$."),
            mcq("hieu", "Đun nóng một lượng khí chứa trong một bình thép kín có thể tích hoàn toàn không đổi ($V = \\text{const}$). Nếu nhiệt độ tuyệt đối $T$ của khí tăng từ $300\\text{ K}$ lên $450\\text{ K}$ thì áp suất $p$ của khí trong bình thay đổi như thế nào?", ["Áp suất tăng gấp $1{,}5$ lần", "Áp suất giảm đi $1{,}5$ lần", "Áp suất không thay đổi", "Áp suất tăng gấp $3$ lần"], 0, "Trong quá trình đẳng tích ($V_1 = V_2$), ta có $\\dfrac{p_2}{p_1} = \\dfrac{T_2}{T_1} = \\dfrac{450}{300} = 1{,}5$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phương trình trạng thái khí lí tưởng:", [
                "Trong hệ tọa độ $(p, T)$, đường biểu diễn quá trình đẳng tích là một đường thẳng có đường kéo dài đi qua gốc tọa độ $0\\text{ K}$.",
                "Trong quá trình biến đổi đẳng tích ($V = \\text{const}$), khối khí không thực hiện công ($A = 0$) nên toàn bộ nhiệt lượng truyền cho khí làm thay đổi nội năng của nó ($\\Delta U = Q$).",
                "Trong công thức $p V = n R T$ với $R = 8{,}31\\text{ J/(mol}\\cdot\\text{K)}$, thể tích $V$ phải tính theo đơn vị lít ($\\text{L}$).",
                "Nếu vừa nén cho thể tích khí giảm đi $2$ lần vừa làm tăng nhiệt độ tuyệt đối lên $2$ lần thì áp suất của khí tăng lên $4$ lần.",
            ], [True, True, False, True], "Ý c) sai vì khi dùng $R = 8{,}31\\text{ J/(mol}\\cdot\\text{K)}$ trong hệ SI thì áp suất $p$ phải tính bằng $\\text{Pa}$ và thể tích $V$ phải đổi ra mét khối ($\\text{m}^3$, với $1\\text{ L} = 10^{-3}\\text{ m}^3$)."),
            short("vandung", "Một bóng đèn dây tóc chứa khí trơ ở nhiệt độ $t_1 = 27^\\circ\\text{C}$ ($T_1 = 300\\text{ K}$) dưới áp suất $p_1 = 0{,}6\\text{ atm}$. Khi đèn cháy sáng, thể tích bóng đèn coi như không đổi và nhiệt độ khí trong đèn tăng lên đến $t_2 = 227^\\circ\\text{C}$ ($T_2 = 500\\text{ K}$). Áp suất $p_2$ của khí trong đèn lúc đó bằng bao nhiêu $\\text{atm}$?", ["1"], "Quá trình đẳng tích ($V = \\text{const}$): $p_2 = p_1 \\cdot \\dfrac{T_2}{T_1} = 0{,}6 \\cdot \\dfrac{500}{300} = 1\\text{ atm}$.", unit="atm"),
        ],
    ),
    bai(
        topic=CH2[0], chapter_title=CH2[1], chapter_desc=CH2[2],
        title="Bài 11: Áp suất khí theo mô hình động học phân tử. Quan hệ giữa động năng phân tử và nhiệt độ",
        icon="⚛️",
        description="Công thức áp suất chất khí theo mô hình động học phân tử p = (1/3)μm.v² = (2/3)μ.E_đ, hằng số Boltzmann k = R/N_A và động năng tịnh tiến trung bình E_đ = (3/2)kT.",
        requirements=[
            "Viết và giải thích được công thức áp suất chất khí theo mô hình động học phân tử: $p = \\dfrac{1}{3}\\mu m \\overline{v^2} = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}}$ (với $\\mu = \\dfrac{N}{V}$ là mật độ phân tử).",
            "Viết và vận dụng được công thức động năng tịnh tiến trung bình của một phân tử khí lí tưởng: $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}k T$, với hằng số Boltzmann $k = \\dfrac{R}{N_A} \\approx 1{,}38 \\cdot 10^{-23}\\text{ J/K}$.",
            "Nêu được động năng tịnh tiến trung bình của phân tử khí tỉ lệ thuận với nhiệt độ tuyệt đối $T$ (nhiệt độ tuyệt đối là thước đo động năng trung bình của phân tử) và tính căn bậc hai của trung bình bình phương tốc độ $v_{\\text{rms}} = \\sqrt{\\overline{v^2}} = \\sqrt{\\dfrac{3kT}{m_0}} = \\sqrt{\\dfrac{3RT}{M}}$.",
        ],
        definition="Theo mô hình động học phân tử chất khí, áp suất khí tác dụng lên thành bình là $p = \\dfrac{1}{3}\\mu m \\overline{v^2} = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}}$. Động năng tịnh tiến trung bình của một phân tử khí tỉ lệ thuận với nhiệt độ tuyệt đối $T$ của khí: $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$, trong đó $k = \\dfrac{R}{N_A} \\approx 1{,}38 \\cdot 10^{-23}\\text{ J/K}$ là hằng số Boltzmann.",
        theory=(
            "### 1. Áp suất chất khí theo mô hình động học phân tử\n"
            "- Gọi $\\mu = \\dfrac{N}{V}$ là mật độ phân tử (số phân tử trong một đơn vị thể tích, đơn vị $\\text{m}^{-3}$), $m$ là khối lượng của $1$ phân tử khí, $\\overline{v^2}$ là trung bình của bình phương tốc độ các phân tử.\n"
            "- Công thức cơ bản của thuyết động học phân tử chất khí:\n"
            "  $$p = \\dfrac{1}{3}\\mu m \\overline{v^2} = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}}$$\n"
            "  trong đó $\\overline{E_{\\text{đ}}} = \\dfrac{1}{2}m\\overline{v^2}$ là **động năng tịnh tiến trung bình** của một phân tử khí.\n\n"
            "### 2. Quan hệ giữa động năng phân tử và nhiệt độ tuyệt đối $T$\n"
            "- Kết hợp với phương trình Clapeyron $pV = nRT = \\dfrac{N}{N_A}RT \\implies p = \\mu \\dfrac{R}{N_A}T = \\mu k T$, đặt **hằng số Boltzmann**:\n"
            "  $$k = \\dfrac{R}{N_A} = \\dfrac{8{,}31}{6{,}02 \\cdot 10^{23}} \\approx 1{,}38 \\cdot 10^{-23}\\text{ J/K}$$\n"
            "- Ta thu được hệ thức liên hệ giữa động năng tịnh tiến trung bình của phân tử và nhiệt độ tuyệt đối $T$:\n"
            "  $$\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$$\n"
            "- **Hệ quả quan trọng**:\n"
            "  1. Động năng tịnh tiến trung bình của phân tử khí **chỉ phụ thuộc vào nhiệt độ tuyệt đối $T$** (không phụ thuộc vào bản chất khí là $\\text{H}_2, \\text{He}$ hay $\\text{O}_2$!).\n"
            "  2. Căn bậc hai của trung bình bình phương tốc độ phân tử (tốc độ căn quân phương): $v_{\\text{rms}} = \\sqrt{\\overline{v^2}} = \\sqrt{\\dfrac{3kT}{m}} = \\sqrt{\\dfrac{3RT}{M}}$.\n"
            "  3. Nội năng của $n$ mol khí lí tưởng đơn nguyên tử (như $\\text{He}, \\text{Ne}, \\text{Ar}$): $U = N \\cdot \\overline{E_{\\text{đ}}} = \\dfrac{3}{2}nRT$ (chỉ phụ thuộc vào nhiệt độ $T$)."
        ),
        formulas=[
            G(
                "Công thức Áp suất phân tử và Động năng trung bình phân tử",
                F("Áp suất khí theo mật độ phân tử μ và động năng trung bình", "$p = \\dfrac{1}{3}\\mu m \\overline{v^2} = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}} = \\mu k T \\quad \\left(\\mu = \\dfrac{N}{V}\\right)$", "Áp suất khí tỉ lệ thuận với mật độ phân tử $\\mu$ và động năng trung bình của phân tử $\\overline{E_{\\text{đ}}}$."),
                F("Động năng tịnh tiến trung bình của phân tử và Hằng số Boltzmann", "$\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT; \\qquad k = \\dfrac{R}{N_A} \\approx 1{,}38 \\cdot 10^{-23}\\text{ J/K}; \\qquad \\sqrt{\\overline{v^2}} = \\sqrt{\\dfrac{3RT}{M}}$", "Ở cùng một nhiệt độ $T$, mọi loại phân tử khí đều có cùng động năng tịnh tiến trung bình $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$."),
            )
        ],
        example="Tính động năng tịnh tiến trung bình $\\overline{E_{\\text{đ}}}$ của một phân tử khí lí tưởng ở nhiệt độ $t = 27^\\circ\\text{C}$. Biết hằng số Boltzmann là $k = 1{,}38 \\cdot 10^{-23}\\text{ J/K}$. Nếu tăng nhiệt độ của khối khí lên đến $t' = 327^\\circ\\text{C}$ thì động năng trung bình của phân tử tăng lên gấp mấy lần?",
        example_answer="Ở $t = 27^\\circ\\text{C}$, nhiệt độ tuyệt đối là $T = 27 + 273 = 300\\text{ K}$. Động năng tịnh tiến trung bình của một phân tử là $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT = 1{,}5 \\cdot 1{,}38 \\cdot 10^{-23} \\cdot 300 = 6{,}21 \\cdot 10^{-21}\\text{ J}$. Ở $t' = 327^\\circ\\text{C}$ thì $T' = 600\\text{ K} = 2T$, nên động năng trung bình của phân tử tăng lên gấp $2$ lần.",
        real_life="Tại tầng cao của khí quyển Trái Đất, ở cùng một nhiệt độ $T$, các phân tử hiđrô ($\\text{H}_2$) và heli ($\\text{He}$) có khối lượng mol $M$ rất nhỏ nên có tốc độ $\\sqrt{\\overline{v^2}} = \\sqrt{\\dfrac{3RT}{M}}$ rất lớn, dễ dàng thoát khỏi lực hấp dẫn của Trái Đất bay vào vũ trụ.",
        quiz=[
            mcq("biet", "Công thức tính động năng tịnh tiến trung bình $\\overline{E_{\\text{đ}}}$ của một phân tử khí lí tưởng theo hằng số Boltzmann $k$ và nhiệt độ tuyệt đối $T$ là gì?", ["$\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$", "$\\overline{E_{\\text{đ}}} = \\dfrac{1}{2}kT$", "$\\overline{E_{\\text{đ}}} = \\dfrac{2}{3}kT$", "$\\overline{E_{\\text{đ}}} = 3kT^2$"], 0, "Động năng tịnh tiến trung bình của phân tử khí lí tưởng tỉ lệ thuận với nhiệt độ tuyệt đối $T$: $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$."),
            mcq("biet", "Công thức tính áp suất chất khí $p$ theo mật độ phân tử $\\mu = \\dfrac{N}{V}$ và động năng tịnh tiến trung bình $\\overline{E_{\\text{đ}}}$ của phân tử là gì?", ["$p = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}}$ (hay $p = \\dfrac{1}{3}\\mu m \\overline{v^2}$)", "$p = \\dfrac{3}{2}\\mu \\overline{E_{\\text{đ}}}$", "$p = \\mu \\overline{E_{\\text{đ}}}$", "$p = \\dfrac{1}{2}\\mu \\overline{E_{\\text{đ}}}$"], 0, "Theo mô hình động học phân tử chất khí: $p = \\dfrac{1}{3}\\mu m \\overline{v^2} = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}}$."),
            mcq("hieu", "Hai bình kín chứa hai chất khí khác nhau là khí hiđrô ($\\text{H}_2, M_1 = 2\\text{ g/mol}$) và khí ôxi ($\\text{O}_2, M_2 = 32\\text{ g/mol}$) ở **cùng một nhiệt độ** $T$. Khi so sánh động năng tịnh tiến trung bình của phân tử hiđrô ($\\overline{E_{\\text{đ}1}}$) và phân tử ôxi ($\\overline{E_{\\text{đ}2}}$), kết luận nào sau đây là đúng?", ["$\\overline{E_{\\text{đ}1}} = \\overline{E_{\\text{đ}2}}$ (vì cùng nhiệt độ $T$ nên $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$ như nhau)", "$\\overline{E_{\\text{đ}1}} = 16 \\overline{E_{\\text{đ}2}}$", "$\\overline{E_{\\text{đ}2}} = 16 \\overline{E_{\\text{đ}1}}$", "$\\overline{E_{\\text{đ}1}} = 4 \\overline{E_{\\text{đ}2}}$"], 0, "Động năng tịnh tiến trung bình của phân tử $\\overline{E_{\\text{đ}}} = \\dfrac{3}{2}kT$ chỉ phụ thuộc vào nhiệt độ tuyệt đối $T$, không phụ thuộc khối lượng phân tử."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về áp suất và động năng phân tử chất khí:", [
                "Hằng số Boltzmann $k$ liên hệ với hằng số khí lí tưởng $R$ và số Avogadro $N_A$ qua hệ thức $k = \\dfrac{R}{N_A} \\approx 1{,}38 \\cdot 10^{-23}\\text{ J/K}$.",
                "Khi nhiệt độ tuyệt đối $T$ của một khối khí lí tưởng tăng lên $4$ lần thì căn bậc hai của trung bình bình phương tốc độ phân tử ($\\sqrt{\\overline{v^2}}$) tăng lên $2$ lần.",
                "Nội năng của một lượng khí lí tưởng xác định phụ thuộc vào cả thể tích $V$ và nhiệt độ $T$.",
                "Áp suất của chất khí trong bình tỉ lệ thuận với mật độ phân tử $\\mu$ và nhiệt độ tuyệt đối $T$ ($p = \\mu k T$).",
            ], [True, True, False, True], "Ý c) sai vì đối với khí lí tưởng, ta bỏ qua thế năng tương tác phân tử nên nội năng chỉ bằng tổng động năng phân tử và **chỉ phụ thuộc vào nhiệt độ $T$** (không phụ thuộc thể tích $V$)."),
            short("vandung", "Một bình kín chứa khí có mật độ phân tử $\\mu = 3 \\cdot 10^{25}\\text{ m}^{-3}$. Biết động năng tịnh tiến trung bình của mỗi phân tử khí là $\\overline{E_{\\text{đ}}} = 5 \\cdot 10^{-21}\\text{ J}$. Áp suất $p$ của khí trong bình bằng bao nhiêu $\\text{kPa}$ (biết $1\\text{ kPa} = 1000\\text{ Pa}$)?", ["100"], "Áp dụng công thức $p = \\dfrac{2}{3}\\mu \\overline{E_{\\text{đ}}} = \\dfrac{2}{3} \\cdot 3 \\cdot 10^{25} \\cdot 5 \\cdot 10^{-21} = 10^5\\text{ Pa} = 100\\text{ kPa}$.", unit="kPa"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 12: Từ trường và đường sức từ",
        icon="🧲",
        description="Tương tác từ, tính chất của đường sức từ, từ trường đều và quy tắc nắm tay phải xác định chiều đường sức từ của dòng điện thẳng, dòng điện tròn và ống dây.",
        requirements=[
            "Nêu được tương tác từ là tương tác giữa nam châm với nam châm, giữa dòng điện với nam châm và giữa dòng điện với dòng điện thông qua từ trường.",
            "Trình bày được các tính chất của đường sức từ (là những đường cong khép kín, không cắt nhau, nơi từ trường mạnh thì đường sức dày, ngoài nam châm đi ra từ cực Bắc $\\text{N}$ vào cực Nam $\\text{S}$).",
            "Vận dụng được quy tắc nắm bàn tay phải để xác định chiều đường sức từ của dòng điện trong dây dẫn thẳng dài, khung dây tròn và ống dây hình trụ.",
        ],
        definition="Từ trường là trường vật chất tồn tại xung quanh nam châm và xung quanh dòng điện (hay điện tích chuyển động), biểu hiện cụ thể là tác dụng lực từ lên một nam châm hay một dòng điện khác đặt trong nó. Đường sức từ là những đường vẽ ở trong không gian có từ trường sao cho tiếp tuyến tại mỗi điểm trùng với phương của vectơ cảm ứng từ $\\vec{B}$ tại điểm đó.",
        theory=(
            "### 1. Tính chất của đường sức từ và Từ trường đều\n"
            "- Qua mỗi điểm trong không gian chỉ vẽ được **duy nhất một đường sức từ** (các đường sức từ **không bao giờ cắt nhau**).\n"
            "- Khác với đường sức điện tĩnh (hở), các đường sức từ là **những đường cong khép kín** (bên ngoài nam châm đi ra từ cực Bắc $\\text{N}$ và đi vào cực Nam $\\text{S}$; bên trong nam châm đi từ $\\text{S}$ sang $\\text{N}$).\n"
            "- Nơi nào từ trường mạnh thì các đường sức từ **mau (dày)**, nơi nào từ trường yếu thì đường sức từ **thưa**.\n"
            "- **Từ trường đều**: từ trường mà đặc tính tại mọi điểm đều như nhau; các đường sức từ là những **đường thẳng song song, cùng chiều và cách đều nhau** (ví dụ: trong lòng ống dây hình trụ dài có dòng điện và giữa hai cực của nam châm hình chữ U).\n\n"
            "### 2. Quy tắc nắm bàn tay phải cho dòng điện\n"
            "- **Dây dẫn thẳng dài**: Giơ ngón cái của bàn tay phải hướng theo chiều dòng điện $I$, khum bốn ngón kia xung quanh dây dẫn thì chiều từ cổ tay đến bốn ngón tay chỉ chiều của các đường sức từ (là các đường tròn đồng tâm nằm trong mặt phẳng vuông góc với dây).\n"
            "- **Khung dây tròn và Ống dây hình trụ**: Khum bàn tay phải theo các vòng dây của ống dây sao cho chiều từ cổ tay đến các ngón tay trùng với chiều dòng điện trong các vòng dây; khi đó ngón cái choãi ra chỉ **chiều của đường sức từ ở trong lòng ống dây** (đi ra từ cực Bắc $\\text{N}$ của ống dây)."
        ),
        formulas=[
            G(
                "Quy tắc xác định chiều đường sức từ",
                F("Quy tắc đối với nam châm và mặt dòng điện tròn", "$\\text{Ngoài nam châm: Ra Bắc (N) – Vào Nam (S)}; \\qquad \\text{Mặt dòng điện: Vào Nam (cùng chiều KĐH) – Ra Bắc (ngược chiều KĐH)}$", "Trong lòng ống dây dẫn có dòng điện, các đường sức từ là những đường thẳng song song đi từ cực Nam sang cực Bắc rồi đi ra ngoài tại cực Bắc."),
                F("Tương tác giữa hai dây dẫn thẳng song song mang dòng điện", "$I_1 \\uparrow\\uparrow I_2 \\implies \\text{Hút nhau}; \\qquad I_1 \\uparrow\\downarrow I_2 \\implies \\text{Đẩy nhau}$", "Hai dòng điện thẳng song song cùng chiều thì hút nhau, ngược chiều thì đẩy nhau."),
            )
        ],
        example="Một ống dây hình trụ dài đặt nằm ngang có dòng điện một chiều chạy qua các vòng dây. Khi nhìn vào đầu bên trái $A$ của ống dây, ta thấy dòng điện chạy theo chiều kim đồng hồ. Hãy xác định tên cực từ ở đầu $A$, đầu $B$ (bên phải) và chiều của đường sức từ bên trong lòng ống dây.",
        example_answer="Áp dụng quy tắc nắm bàn tay phải (hoặc quy tắc 'Vào Nam ra Bắc': nhìn vào mặt đầu ống dây thấy dòng điện chạy cùng chiều kim đồng hồ thì mặt đó là cực Nam $\\text{S}$): Đầu $A$ là **cực Nam ($\\text{S}$)**, đầu $B$ là **cực Bắc ($\\text{N}$)**. Ở bên trong lòng ống dây, các đường sức từ hướng từ đầu $A$ ($\\text{S}$) sang đầu $B$ ($\\text{N}$) và đi ra ngoài từ đầu $B$.",
        real_life="Máy chụp cộng hưởng từ (MRI) trong các bệnh viện sử dụng một ống dây siêu dẫn khổng lồ tạo ra từ trường đều cực mạnh và ổn định ở trong lòng ống để ghi ảnh chi tiết các cơ quan nội tạng của cơ thể.",
        quiz=[
            mcq("biet", "Các đường sức từ của một dòng điện chạy trong dây dẫn thẳng rất dài có hình dạng gì?", ["Là những đường tròn đồng tâm nằm trong mặt phẳng vuông góc với dây dẫn và có tâm nằm trên dây dẫn", "Là những đường thẳng song song với dây dẫn", "Là những đường thẳng xuất phát từ dây dẫn tỏa ra mọi phía", "Là những đường parabol"], 0, "Đường sức từ của dòng điện thẳng dài là các đường tròn đồng tâm nằm trong mặt phẳng vuông góc với dây dẫn, chiều xác định theo quy tắc nắm tay phải."),
            mcq("biet", "Đặc điểm nào sau đây là **đúng** đối với mọi đường sức từ?", ["Các đường sức từ là những đường cong khép kín (hoặc vô hạn ở hai đầu) và không bao giờ cắt nhau", "Các đường sức từ bắt đầu từ điện tích dương và kết thúc ở điện tích âm", "Qua một điểm trong từ trường có thể vẽ được hai đường sức từ cắt nhau", "Nơi nào từ trường mạnh thì các đường sức từ được vẽ rất thưa"], 0, "Qua mỗi điểm chỉ có một đường sức từ và mọi đường sức từ đều là đường cong khép kín."),
            mcq("hieu", "Hai dây dẫn thẳng dài đặt song song gần nhau trong không khí. Khi cho hai dòng điện không đổi $I_1$ và $I_2$ chạy qua hai dây theo **cùng một chiều** thì hai dây dẫn sẽ tương tác với nhau như thế nào?", ["Hai dây dẫn hút nhau", "Hai dây dẫn đẩy nhau", "Hai dây dẫn không tương tác với nhau", "Hai dây dẫn quay vuông góc với nhau"], 0, "Hai dòng điện thẳng song song cùng chiều thì hút nhau, ngược chiều thì đẩy nhau."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về từ trường và đường sức từ:", [
                "Từ trường trong lòng một ống dây hình trụ dài có dòng điện không đổi chạy qua là từ trường đều.",
                "Chiều của đường sức từ tại một điểm trùng với chiều mà cực Bắc của kim nam châm nhỏ tự do chỉ khi nằm cân bằng tại điểm đó.",
                "Xung quanh một điện tích đứng yên luôn tồn tại đồng thời cả điện trường và từ trường.",
                "Quy tắc nắm bàn tay phải dùng để xác định chiều đường sức từ của dòng điện thẳng và ống dây có dòng điện.",
            ], [True, True, False, True], "Ý c) sai vì xung quanh một điện tích **đứng yên** chỉ có điện trường tĩnh, không có từ trường (chỉ khi điện tích chuyển động mới sinh ra từ trường)."),
            short("vandung", "Qua mỗi điểm bất kì trong không gian có từ trường, ta có thể vẽ được tối đa bao nhiêu đường sức từ đi qua điểm đó?", ["1"], "Tại mỗi điểm trong từ trường chỉ có một hướng duy nhất của $\\vec{B}$ nên chỉ vẽ được duy nhất $1$ đường sức từ đi qua điểm đó."),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 13: Cảm ứng từ và lực từ tác dụng lên đoạn dây dẫn mang dòng điện",
        icon="✋",
        description="Vectơ cảm ứng từ B (đơn vị Tesla - T), quy tắc bàn tay trái xác định hướng của lực từ và công thức độ lớn lực từ F = B.I.ℓ.sinα.",
        requirements=[
            "Định nghĩa được cảm ứng từ $B = \\dfrac{F}{I\\ell}$ (khi dây vuông góc đường sức) đặc trưng cho từ trường về mặt tác dụng lực, có đơn vị là Tesla ($\\text{T}$).",
            "Vận dụng được **quy tắc bàn tay trái** để xác định chiều của lực từ $\\vec{F}$ tác dụng lên đoạn dây dẫn thẳng mang dòng điện đặt trong từ trường.",
            "Viết và vận dụng được công thức tổng quát tính độ lớn lực từ: $F = B \\cdot I \\cdot \\ell \\cdot \\sin\\alpha$ (với $\\alpha = (\\widehat{\\vec{B}, \\vec{I}})$).",
        ],
        definition="Vectơ cảm ứng từ $\\vec{B}$ tại một điểm đặc trưng cho từ trường về phương diện tác dụng lực từ tại điểm đó (đơn vị trong hệ SI là Tesla – $\\text{T}$). Lực từ $\\vec{F}$ tác dụng lên đoạn dây dẫn thẳng dài $\\ell$ mang dòng điện $I$ đặt trong từ trường đều $\\vec{B}$ có phương vuông góc với mặt phẳng chứa dây dẫn và $\\vec{B}$, có chiều tuân theo quy tắc bàn tay trái và có độ lớn: $F = B \\cdot I \\cdot \\ell \\cdot \\sin\\alpha$.",
        theory=(
            "### 1. Lực từ tác dụng lên đoạn dây dẫn mang dòng điện\n"
            "- **Điểm đặt**: tại trung điểm của đoạn dây dẫn nằm trong từ trường.\n"
            "- **Phương**: vuông góc với mặt phẳng tạo bởi đoạn dây dẫn mang dòng điện và vectơ cảm ứng từ $\\vec{B}$ ($\\vec{F} \\perp \\vec{I}$ và $\\vec{F} \\perp \\vec{B}$).\n"
            "- **Chiều — Quy tắc bàn tay trái**: Đặt bàn tay trái duỗi thẳng sao cho các đường sức từ ($\\vec{B}$) hướng vào lòng bàn tay, chiều từ cổ tay đến bốn ngón tay trùng với chiều dòng điện $I$; khi đó ngón tay cái choãi ra $90^\\circ$ chỉ chiều của lực từ $\\vec{F}$.\n\n"
            "### 2. Công thức độ lớn lực từ và Cảm ứng từ $B$\n"
            "- **Công thức tổng quát (Định luật Ampere)**:\n"
            "  $$F = B \\cdot I \\cdot \\ell \\cdot \\sin\\alpha$$\n"
            "  trong đó $\\alpha$ là góc hợp bởi hướng dòng điện $\\vec{I}$ và hướng của vectơ cảm ứng từ $\\vec{B}$:\n"
            "  - Khi dây dẫn **vuông góc** với đường sức từ ($\\alpha = 90^\\circ, \\sin 90^\\circ = 1$): lực từ đạt cực đại $F_{\\max} = B \\cdot I \\cdot \\ell \\implies B = \\dfrac{F_{\\max}}{I \\cdot \\ell}$.\n"
            "  - Khi dây dẫn **song song** với đường sức từ ($\\alpha = 0^\\circ$ hoặc $180^\\circ$): lực từ bằng không ($F = 0$).\n"
            "- **Đơn vị cảm ứng từ**: **Tesla** (kí hiệu $\\text{T}$), với $1\\text{ T} = 1\\text{ N/(A}\\cdot\\text{m)}$."
        ),
        formulas=[
            G(
                "Công thức Lực từ và Cảm ứng từ",
                F("Độ lớn lực từ tác dụng lên đoạn dây dẫn thẳng", "$F = B \\cdot I \\cdot \\ell \\cdot \\sin\\alpha$", "Trong đó $B$ tính bằng Tesla ($\\text{T}$), $I$ tính bằng Ampe ($\\text{A}$), $\\ell$ là chiều dài phần dây nằm trong từ trường ($\\text{m}$), $\\alpha = (\\widehat{\\vec{B}, \\vec{I}})$."),
                F("Cảm ứng từ B từ thí nghiệm cân từ (khi α = 90°)", "$B = \\dfrac{F}{I \\cdot \\ell} \\quad (1\\text{ T} = 1\\text{ N}\\cdot\\text{A}^{-1}\\cdot\\text{m}^{-1};\\ 1\\text{ mT} = 10^{-3}\\text{ T})$", "Khi dòng điện song song với các đường sức từ ($\\alpha = 0^\\circ$ hoặc $180^\\circ$) thì $F = 0$."),
            )
        ],
        example="Một đoạn dây dẫn thẳng dài $\\ell = 20\\text{ cm} = 0{,}2\\text{ m}$ có dòng điện cường độ $I = 5\\text{ A}$ chạy qua được đặt trong một từ trường đều có độ lớn cảm ứng từ $B = 0{,}4\\text{ T}$. Hãy tính độ lớn lực từ $F$ tác dụng lên đoạn dây trong hai trường hợp: (a) Dây dẫn đặt vuông góc với các đường sức từ ($\\alpha = 90^\\circ$); (b) Dây dẫn hợp với các đường sức từ một góc $\\alpha = 30^\\circ$.",
        example_answer="Đổi $\\ell = 0{,}2\\text{ m}$. (a) Khi $\\alpha = 90^\\circ$: $F = B I \\ell \\sin 90^\\circ = 0{,}4 \\cdot 5 \\cdot 0{,}2 \\cdot 1 = 0{,}4\\text{ N}$. (b) Khi $\\alpha = 30^\\circ$: $F = B I \\ell \\sin 30^\\circ = 0{,}4 \\cdot 5 \\cdot 0{,}2 \\cdot 0{,}5 = 0{,}2\\text{ N}$.",
        real_life="Động cơ điện một chiều (trong quạt tích điện, xe điện, đồ chơi) và màng loa điện động phát ra âm thanh đều hoạt động dựa trên lực từ $\\vec{F}$ tác dụng lên cuộn dây dẫn mang dòng điện đặt trong từ trường của nam châm.",
        quiz=[
            mcq("biet", "Công thức tính độ lớn lực từ $F$ tác dụng lên một đoạn dây dẫn thẳng dài $\\ell$ mang dòng điện $I$ đặt trong từ trường đều $\\vec{B}$ hợp với dây một góc $\\alpha$ là gì?", ["$F = B \\cdot I \\cdot \\ell \\cdot \\sin\\alpha$", "$F = B \\cdot I \\cdot \\ell \\cdot \\cos\\alpha$", "$F = \\dfrac{B \\cdot I}{\\ell \\cdot \\sin\\alpha}$", "$F = B^2 I \\ell \\sin\\alpha$"], 0, "Độ lớn lực từ tác dụng lên đoạn dây dẫn thẳng mang dòng điện là $F = B I \\ell \\sin\\alpha$."),
            mcq("biet", "Đơn vị của cảm ứng từ $B$ trong hệ thống đo lường quốc tế SI là gì?", ["Tesla ($\\text{T}$)", "Weber ($\\text{Wb}$)", "Henry ($\\text{H}$)", "Vôn trên mét ($\\text{V/m}$)"], 0, "Đơn vị của cảm ứng từ $B$ trong hệ SI là Tesla (kí hiệu $\\text{T}$)."),
            mcq("hieu", "Khi đặt một đoạn dây dẫn thẳng có dòng điện $I$ chạy qua **song song** với các đường sức từ của một từ trường đều ($\\alpha = 0^\\circ$ hoặc $\\alpha = 180^\\circ$) thì độ lớn lực từ tác dụng lên đoạn dây đó bằng bao nhiêu?", ["$F = 0$", "$F = B I \\ell$", "$F = \\dfrac{1}{2} B I \\ell$", "$F = 2 B I \\ell$"], 0, "Khi dây dẫn song song với đường sức từ thì $\\alpha = 0^\\circ$ (hoặc $180^\\circ$), $\\sin\\alpha = 0$ nên $F = B I \\ell \\sin\\alpha = 0$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cảm ứng từ và lực từ:", [
                "Vectơ lực từ $\\vec{F}$ luôn vuông góc với cả đoạn dây dẫn mang dòng điện và vectơ cảm ứng từ $\\vec{B}$.",
                "Quy tắc bàn tay trái dùng để xác định chiều của lực từ tác dụng lên đoạn dây dẫn mang dòng điện trong từ trường.",
                "Nếu đồng thời đổi chiều dòng điện và đổi chiều đường sức từ (đảo hai cực nam châm) thì chiều của lực từ $\\vec{F}$ bị đổi ngược lại.",
                "Đơn vị $1\\text{ T}$ tương đương với $1\\text{ N/(A}\\cdot\\text{m)}$.",
            ], [True, True, False, True], "Ý c) sai vì đổi chiều dòng điện làm $\\vec{F}$ đổi chiều 1 lần, đổi chiều từ trường $\\vec{B}$ làm $\\vec{F}$ đổi chiều thêm lần nữa, nên kết quả là chiều của lực từ $\\vec{F}$ **giữ nguyên như cũ**."),
            short("vandung", "Một đoạn dây dẫn thẳng dài $\\ell = 0{,}5\\text{ m}$ mang dòng điện $I = 4\\text{ A}$ đặt vuông góc với các đường sức từ ($\\alpha = 90^\\circ$) của một từ trường đều có cảm ứng từ $B = 0{,}5\\text{ T}$. Độ lớn lực từ $F$ tác dụng lên đoạn dây bằng bao nhiêu Newton ($\\text{N}$)?", ["1"], "Áp dụng công thức $F = B I \\ell \\sin 90^\\circ = 0{,}5 \\cdot 4 \\cdot 0{,}5 \\cdot 1 = 1\\text{ N}$.", unit="N"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 14: Từ thông. Hiện tượng cảm ứng điện từ",
        icon="🔄",
        description="Khái niệm và công thức từ thông Φ = N.B.S.cosα (đơn vị Weber - Wb), định luật Lenz về chiều dòng điện cảm ứng và định luật Faraday e_c = -ΔΦ/Δt.",
        requirements=[
            "Viết và vận dụng được công thức tính từ thông qua khung dây có $N$ vòng dây, diện tích $S$ đặt trong từ trường đều $\\vec{B}$: $\\Phi = N B S \\cos\\alpha$ (đơn vị Weber – $\\text{Wb}$), với $\\alpha = (\\widehat{\\vec{n}, \\vec{B}})$.",
            "Phát biểu và vận dụng được Định luật Lenz về chiều dòng điện cảm ứng (tạo ra từ trường cảm ứng $\\vec{B}_c$ chống lại nguyên nhân sinh ra nó: từ thông tăng thì $\\vec{B}_c \\uparrow\\downarrow \\vec{B}$, từ thông giảm thì $\\vec{B}_c \\uparrow\\uparrow \\vec{B}$).",
            "Viết và vận dụng được công thức Định luật Faraday về suất điện động cảm ứng: $e_c = -\\dfrac{\\Delta\\Phi}{\\Delta t}$ và $|e_c| = \\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right|$, cường độ dòng cảm ứng $i_c = \\dfrac{|e_c|}{R}$.",
        ],
        definition="Từ thông qua một khung dây phẳng có $N$ vòng dây, diện tích mỗi vòng là $S$ đặt trong từ trường đều $\\vec{B}$ được xác định bởi công thức $\\Phi = N B S \\cos\\alpha$ (đơn vị Weber – $\\text{Wb}$), với $\\alpha$ là góc hợp bởi vectơ pháp tuyến $\\vec{n}$ của mặt phẳng khung dây và $\\vec{B}$. Khi từ thông qua mạch kín biến thiên thì xuất hiện suất điện động cảm ứng theo định luật Faraday: $e_c = -\\dfrac{\\Delta\\Phi}{\\Delta t}$.",
        theory=(
            "### 1. Từ thông ($\\Phi$)\n"
            "- Biểu thức:\n"
            "  $$\\Phi = N \\cdot B \\cdot S \\cdot \\cos\\alpha$$\n"
            "  trong đó $\\alpha = (\\widehat{\\vec{n}, \\vec{B}})$ là góc hợp bởi **vectơ pháp tuyến $\\vec{n}$** (vuông góc với mặt khung) và vectơ cảm ứng từ $\\vec{B}$.\n"
            "  *(Lưu ý cực kì quan trọng: nếu đề bài cho mặt phẳng khung dây hợp với $\\vec{B}$ một góc $\\beta$ thì góc trong công thức là $\\alpha = 90^\\circ - \\beta \\implies \\cos\\alpha = \\sin\\beta$!)*. \n"
            "- Đơn vị từ thông trong hệ SI là **Weber** (kí hiệu $\\text{Wb}$), với $1\\text{ Wb} = 1\\text{ T}\\cdot\\text{m}^2$.\n\n"
            "### 2. Định luật Lenz và Định luật Faraday về cảm ứng điện từ\n"
            "- **Định luật Lenz (chiều dòng điện cảm ứng)**: Dòng điện cảm ứng xuất hiện trong mạch kín có chiều sao cho từ trường cảm ứng ($\\vec{B}_c$) mà nó sinh ra có tác dụng **chống lại sự biến thiên của từ thông ban đầu** qua mạch kín:\n"
            "  - Nếu từ thông $\\Phi$ đang **tăng**: $\\vec{B}_c$ **ngược chiều** với $\\vec{B}$ ban đầu ($\\vec{B}_c \\uparrow\\downarrow \\vec{B}$).\n"
            "  - Nếu từ thông $\\Phi$ đang **giảm**: $\\vec{B}_c$ **cùng chiều** với $\\vec{B}$ ban đầu ($\\vec{B}_c \\uparrow\\uparrow \\vec{B}$).\n"
            "- **Định luật Faraday (độ lớn suất điện động cảm ứng)**:\n"
            "  $$e_c = -\\dfrac{\\Delta\\Phi}{\\Delta t} \\implies |e_c| = \\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right| = \\left|\\dfrac{\\Phi_2 - \\Phi_1}{\\Delta t}\\right|; \\qquad i_c = \\dfrac{|e_c|}{R}$$\n"
            "- **Dòng điện Foucault (dòng điện xoáy)**: dòng điện cảm ứng sinh ra trong khối vật dẫn kim loại khi chuyển động trong từ trường hoặc đặt trong từ trường biến thiên (ứng dụng trong bếp từ, phanh điện từ, lò tôi kim loại; gây hao phí tỏa nhiệt trong lõi máy biến áp nên phải ghép lõi từ các lá thép kĩ thuật điện mỏng sơn cách điện)."
        ),
        formulas=[
            G(
                "Từ thông, Định luật Lenz và Định luật Faraday",
                F("Công thức tính từ thông qua khung dây N vòng", "$\\Phi = N \\cdot B \\cdot S \\cdot \\cos\\alpha \\quad (\\text{với } \\alpha = (\\widehat{\\vec{n}, \\vec{B}});\\ 1\\text{ Wb} = 1\\text{ T}\\cdot\\text{m}^2)$", "Khi mặt khung vuông góc với đường sức từ thì $\\vec{n} \\parallel \\vec{B} \\ (\\alpha = 0^\\circ) \\implies \\Phi_{\\max} = NBS$."),
                F("Suất điện động cảm ứng (Định luật Faraday)", "$e_c = -\\dfrac{\\Delta\\Phi}{\\Delta t}; \\qquad |e_c| = \\left|\\dfrac{\\Phi_2 - \\Phi_1}{\\Delta t}\\right|; \\qquad i_c = \\dfrac{|e_c|}{R}$", "Tốc độ biến thiên từ thông $\\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right|$ càng lớn thì độ lớn suất điện động cảm ứng $|e_c|$ càng lớn."),
            )
        ],
        example="Một cuộn dây phẳng gồm $N = 100$ vòng dây, diện tích mỗi vòng là $S = 20\\text{ cm}^2 = 2 \\cdot 10^{-3}\\text{ m}^2$ đặt trong từ trường đều có vectơ cảm ứng từ $\\vec{B}$ vuông góc với mặt phẳng khung dây ($\\alpha = 0^\\circ$). Trong khoảng thời gian $\\Delta t = 0{,}05\\text{ s}$, độ lớn cảm ứng từ tăng đều từ $B_1 = 0{,}1\\text{ T}$ lên $B_2 = 0{,}6\\text{ T}$. Hãy tính độ biến thiên từ thông $\\Delta\\Phi$ và độ lớn suất điện động cảm ứng $|e_c|$ xuất hiện trong cuộn dây.",
        example_answer="Vì mặt khung vuông góc với $\\vec{B}$ nên $\\alpha = 0^\\circ, \\cos 0^\\circ = 1$. Độ biến thiên từ thông qua cuộn dây là $\\Delta\\Phi = N S (B_2 - B_1)\\cos 0^\\circ = 100 \\cdot 2 \\cdot 10^{-3} \\cdot (0{,}6 - 0{,}1) = 0{,}1\\text{ Wb}$. Theo định luật Faraday, độ lớn suất điện động cảm ứng là $|e_c| = \\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right| = \\dfrac{0{,}1}{0{,}05} = 2\\text{ V}$.",
        real_life="Bếp từ đun nấu hiện đại tạo ra từ trường biến thiên tần số cao xuyên qua đáy nồi bằng kim loại nhiễm từ, sinh ra dòng điện cảm ứng Foucault cực mạnh làm đáy nồi tự nóng lên trực tiếp mà mặt bếp vẫn mát.",
        quiz=[
            mcq("biet", "Đơn vị của từ thông $\\Phi$ trong hệ thống đo lường quốc tế SI là gì?", ["Weber ($\\text{Wb}$)", "Tesla ($\\text{T}$)", "Vôn ($\\text{V}$)", "Ampe ($\\text{A}$)"], 0, "Đơn vị đo từ thông trong hệ SI là Weber (kí hiệu $\\text{Wb}$, với $1\\text{ Wb} = 1\\text{ T}\\cdot\\text{m}^2$)."),
            mcq("biet", "Theo Định luật Faraday về cảm ứng điện từ, độ lớn của suất điện động cảm ứng $|e_c|$ xuất hiện trong mạch kín tỉ lệ thuận với đại lượng nào?", ["Tốc độ biến thiên của từ thông qua mạch kín $\\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right|$", "Giá trị tức thời của từ thông $\\Phi$", "Điện trở $R$ của mạch kín", "Thời gian $\\Delta t$ mà từ thông không đổi"], 0, "Theo định luật Faraday, $|e_c| = \\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right|$ tỉ lệ thuận với tốc độ biến thiên của từ thông."),
            mcq("hieu", "Theo Định luật Lenz, khi từ thông $\\Phi$ gửi qua một khung dây dẫn kín đang **tăng lên** thì từ trường cảm ứng $\\vec{B}_c$ do dòng điện cảm ứng sinh ra có chiều như thế nào so với từ trường ban đầu $\\vec{B}$?", ["Ngược chiều với từ trường ban đầu ($\\vec{B}_c \\uparrow\\downarrow \\vec{B}$) để chống lại sự tăng của từ thông", "Cùng chiều với từ trường ban đầu ($\\vec{B}_c \\uparrow\\uparrow \\vec{B}$)", "Vuông góc với từ trường ban đầu", "Bằng không"], 0, "Theo định luật Lenz, khi từ thông tăng thì từ trường cảm ứng $\\vec{B}_c$ ngược chiều với $\\vec{B}$ để chống lại sự tăng; khi từ thông giảm thì $\\vec{B}_c$ cùng chiều với $\\vec{B}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về từ thông và cảm ứng điện từ:", [
                "Khi mặt phẳng khung dây vuông góc với các đường sức từ thì vectơ pháp tuyến $\\vec{n}$ song song với $\\vec{B}$ ($\\alpha = 0^\\circ$) và từ thông đạt giá trị cực đại $\\Phi = NBS$.",
                "Khi mặt phẳng khung dây song song với các đường sức từ thì $\\alpha = 90^\\circ$ và từ thông qua khung dây bằng $0$.",
                "Để giảm hao phí do dòng điện Foucault trong lõi sắt máy biến áp, người ta đúc lõi sắt thành một khối sắt đặc nguyên khối.",
                "Dấu trừ ($-$) trong biểu thức $e_c = -\\dfrac{\\Delta\\Phi}{\\Delta t}$ thể hiện định luật Lenz và sự bảo toàn năng lượng.",
            ], [True, True, False, True], "Ý c) sai vì để giảm dòng Foucault trong lõi máy biến áp, người ta phải ghép lõi từ nhiều lá thép kĩ thuật điện mỏng có phủ sơn cách điện với nhau chứ không đúc khối đặc."),
            short("vandung", "Từ thông qua một khung dây dẫn kín biến thiên một lượng $\\Delta\\Phi = 0{,}6\\text{ Wb}$ trong khoảng thời gian $\\Delta t = 0{,}2\\text{ s}$. Độ lớn suất điện động cảm ứng $|e_c|$ xuất hiện trong khung dây bằng bao nhiêu Vôn ($\\text{V}$)?", ["3"], "Áp dụng định luật Faraday: $|e_c| = \\left|\\dfrac{\\Delta\\Phi}{\\Delta t}\\right| = \\dfrac{0{,}6}{0{,}2} = 3\\text{ V}$.", unit="V"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 15: Đại cương về dòng điện xoay chiều",
        icon="〰️",
        description="Từ thông và suất điện động xoay chiều E₀ = N.B.S.ω, biểu thức u và i xoay chiều, giá trị hiệu dụng I = I₀/√2, U = U₀/√2 và công suất P = U.I.cosφ.",
        requirements=[
            "Thiết lập được biểu thức từ thông $\\Phi = NBS\\cos(\\omega t + \\varphi_0)$ và suất điện động cảm ứng xoay chiều $e = E_0\\sin(\\omega t + \\varphi_0)$ với giá trị cực đại $E_0 = N B S \\omega$.",
            "Phân biệt được giá trị tức thời ($i, u, e$), giá trị cực đại ($I_0, U_0, E_0$) và tính được **giá trị hiệu dụng**: $I = \\dfrac{I_0}{\\sqrt{2}}, U = \\dfrac{U_0}{\\sqrt{2}}, E = \\dfrac{E_0}{\\sqrt{2}}$.",
            "Viết và vận dụng được công thức tính công suất tiêu thụ của mạch điện xoay chiều $\\mathcal{P} = U I \\cos\\varphi$ (với $\\varphi = \\varphi_u - \\varphi_i$ là độ lệch pha giữa $u$ và $i$).",
        ],
        definition="Dòng điện xoay chiều là dòng điện có cường độ và chiều biến thiên điều hòa theo thời gian theo quy luật hàm côsin (hay sin): $i = I_0\\cos(\\omega t + \\varphi_i)$. Giá trị hiệu dụng của dòng điện xoay chiều bằng giá trị cực đại chia cho $\\sqrt{2}$: $I = \\dfrac{I_0}{\\sqrt{2}}, U = \\dfrac{U_0}{\\sqrt{2}}, E = \\dfrac{E_0}{\\sqrt{2}}$.",
        theory=(
            "### 1. Suất điện động xoay chiều và Biểu thức $u, i$\n"
            "- Khi khung dây phẳng gồm $N$ vòng, diện tích $S$ quay đều với tốc độ góc $\\omega = 2\\pi f$ trong từ trường đều $\\vec{B}$:\n"
            "  - Từ thông qua khung: $\\Phi = N B S \\cos(\\omega t + \\varphi_0) = \\Phi_0 \\cos(\\omega t + \\varphi_0)$ (với $\\Phi_0 = NBS$).\n"
            "  - Suất điện động cảm ứng trong khung: $e = -\\Phi'(t) = \\omega N B S \\sin(\\omega t + \\varphi_0) = E_0 \\cos\\left(\\omega t + \\varphi_0 - \\dfrac{\\pi}{2}\\right)$, trong đó **suất điện động cực đại** là:\n"
            "    $$E_0 = \\omega \\Phi_0 = N \\cdot B \\cdot S \\cdot \\omega$$\n"
            "  *(Lưu ý: Suất điện động $e$ luôn trễ pha $\\dfrac{\\pi}{2}$ so với từ thông $\\Phi$ — hai đại lượng vuông pha nhau)*.\n\n"
            "### 2. Giá trị hiệu dụng và Công suất điện xoay chiều\n"
            "- **Giá trị hiệu dụng ($I$)**: được xây dựng dựa trên **tác dụng nhiệt** của dòng điện (dòng xoay chiều có cường độ cực đại $I_0$ tỏa nhiệt lượng trên điện trở $R$ trong 1 chu kì bằng với dòng điện không đổi có cường độ $I = \\dfrac{I_0}{\\sqrt{2}}$):\n"
            "  $$I = \\dfrac{I_0}{\\sqrt{2}}; \\qquad U = \\dfrac{U_0}{\\sqrt{2}}; \\qquad E = \\dfrac{E_0}{\\sqrt{2}}$$\n"
            "- Số chỉ của các ampe kế, vôn kế xoay chiều và các số ghi định mức trên thiết bị điện (như $220\\text{ V}$) đều là **giá trị hiệu dụng** (vậy mạng điện $220\\text{ V}$ có điện áp cực đại $U_0 = 220\\sqrt{2} \\approx 311\\text{ V}$).\n"
            "- **Công suất tiêu thụ điện xoay chiều**: $\\mathcal{P} = U \\cdot I \\cdot \\cos\\varphi$, với $\\varphi = \\varphi_u - \\varphi_i$ và $\\cos\\varphi$ là hệ số công suất."
        ),
        formulas=[
            G(
                "Suất điện động cực đại, Giá trị hiệu dụng và Công suất xoay chiều",
                F("Suất điện động cực đại của khung dây quay trong từ trường", "$E_0 = \\omega \\Phi_0 = N \\cdot B \\cdot S \\cdot \\omega = 2\\pi f N B S$", "Suất điện động $e$ luôn vuông pha (trễ pha $\\dfrac{\\pi}{2}$) so với từ thông $\\Phi$: $\\left(\\dfrac{\\Phi}{\\Phi_0}\\right)^2 + \\left(\\dfrac{e}{E_0}\\right)^2 = 1$."),
                F("Các giá trị hiệu dụng và Công suất tiêu thụ", "$I = \\dfrac{I_0}{\\sqrt{2}}; \\quad U = \\dfrac{U_0}{\\sqrt{2}}; \\quad E = \\dfrac{E_0}{\\sqrt{2}}; \\qquad \\mathcal{P} = U I \\cos\\varphi \\ (\\varphi = \\varphi_u - \\varphi_i)$", "Nếu mạch chỉ có điện trở thuần $R$ thì $u$ và $i$ cùng pha ($\\varphi = 0, \\cos\\varphi = 1 \\implies \\mathcal{P} = UI = I^2 R$)."),
            )
        ],
        example="Dòng điện xoay chiều chạy qua một đoạn mạch có biểu thức $i = 4\\sqrt{2}\\cos(100\\pi t)\\text{ (A)}$ (với $t$ tính bằng $\\text{s}$), đặt dưới điện áp xoay chiều $u = 220\\sqrt{2}\\cos(100\\pi t)\\text{ (V)}$. Hãy xác định tần số $f$, cường độ dòng điện hiệu dụng $I$, điện áp hiệu dụng $U$ và công suất tiêu thụ $\\mathcal{P}$ của đoạn mạch.",
        example_answer="Từ biểu thức ta có $\\omega = 100\\pi\\text{ rad/s} \\implies f = \\dfrac{\\omega}{2\\pi} = 50\\text{ Hz}$. Cường độ dòng điện hiệu dụng là $I = \\dfrac{I_0}{\\sqrt{2}} = \\dfrac{4\\sqrt{2}}{\\sqrt{2}} = 4\\text{ A}$. Điện áp hiệu dụng là $U = \\dfrac{U_0}{\\sqrt{2}} = \\dfrac{220\\sqrt{2}}{\\sqrt{2}} = 220\\text{ V}$. Vì $u$ và $i$ cùng pha ($\\varphi = 0 \\implies \\cos\\varphi = 1$) nên công suất tiêu thụ là $\\mathcal{P} = U I \\cos 0 = 220 \\cdot 4 \\cdot 1 = 880\\text{ W}$.",
        real_life="Lưới điện dân dụng tại Việt Nam cung cấp điện áp xoay chiều có giá trị hiệu dụng $U = 220\\text{ V}$ (giá trị cực đại $U_0 = 220\\sqrt{2} \\approx 311\\text{ V}$) và tần số $f = 50\\text{ Hz}$.",
        quiz=[
            mcq("biet", "Cho dòng điện xoay chiều có cường độ cực đại là $I_0$. Cường độ dòng điện **hiệu dụng** $I$ được tính bằng công thức nào?", ["$I = \\dfrac{I_0}{\\sqrt{2}}$", "$I = I_0 \\sqrt{2}$", "$I = \\dfrac{I_0}{2}$", "$I = 2I_0$"], 0, "Giá trị hiệu dụng của dòng điện hình sin bằng giá trị cực đại chia cho $\\sqrt{2}$: $I = \\dfrac{I_0}{\\sqrt{2}}$."),
            mcq("biet", "Một khung dây phẳng gồm $N$ vòng dây, mỗi vòng có diện tích $S$, quay đều với tốc độ góc $\\omega$ quanh trục vuông góc với các đường sức của một từ trường đều có cảm ứng từ $B$. Suất điện động cực đại $E_0$ xuất hiện trong khung dây là:", ["$E_0 = N \\cdot B \\cdot S \\cdot \\omega$", "$E_0 = \\dfrac{N B S}{\\omega}$", "$E_0 = N B S \\omega^2$", "$E_0 = \\dfrac{N B \\omega}{S}$"], 0, "Suất điện động cực đại trong khung dây quay đều là $E_0 = \\omega \\Phi_0 = N B S \\omega$."),
            mcq("hieu", "Giá trị hiệu dụng của dòng điện xoay chiều được định nghĩa dựa trên tác dụng nào của dòng điện?", ["Tác dụng nhiệt (nhiệt lượng tỏa ra trên điện trở $R$ trong một chu kì)", "Tác dụng hóa học (mạ điện)", "Tác dụng từ lên la bàn", "Tác dụng quang học"], 0, "Cường độ hiệu dụng của dòng điện xoay chiều bằng cường độ của một dòng điện không đổi mà khi chạy qua cùng một điện trở $R$ thì tỏa ra nhiệt lượng bằng nhau trong cùng thời gian."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về dòng điện xoay chiều:", [
                "Số chỉ của vôn kế và ampe kế xoay chiều cho biết giá trị hiệu dụng của điện áp và cường độ dòng điện.",
                "Mạng điện sinh hoạt $220\\text{ V} - 50\\text{ Hz}$ có điện áp hiệu dụng là $220\\text{ V}$ và điện áp cực đại là $220\\sqrt{2}\\text{ V} \\approx 311\\text{ V}$.",
                "Trong một khung dây quay đều trong từ trường, suất điện động cảm ứng $e$ luôn biến thiên cùng pha với từ thông $\\Phi$.",
                "Đối với dòng điện $i = 2\\sqrt{2}\\cos(100\\pi t)\\text{ (A)}$, mỗi giây dòng điện đổi chiều $100$ lần.",
            ], [True, True, False, True], "Ý c) sai vì $e = -\\Phi'(t)$ nên suất điện động cảm ứng $e$ luôn vuông pha (trễ pha $\\dfrac{\\pi}{2}$) so với từ thông $\\Phi$."),
            short("vandung", "Một điện áp xoay chiều có biểu thức $u = 120\\sqrt{2}\\cos(100\\pi t)\\text{ (V)}$. Giá trị điện áp hiệu dụng $U$ của điện áp này bằng bao nhiêu Vôn ($\\text{V}$)?", ["120"], "Ta có $U_0 = 120\\sqrt{2}\\text{ V}$, suy ra giá trị hiệu dụng là $U = \\dfrac{U_0}{\\sqrt{2}} = 120\\text{ V}$.", unit="V"),
        ],
    ),
    bai(
        topic=CH3[0], chapter_title=CH3[1], chapter_desc=CH3[2],
        title="Bài 16: Máy biến áp và truyền tải điện năng. Sóng điện từ",
        icon="🗼",
        description="Hệ thức máy biến áp lí tưởng U₁/U₂ = N₁/N₂ = I₂/I₁, bài toán hao phí truyền tải điện năng ΔP = P²R/(U²cos²φ) và tính chất sóng điện từ (E ⊥ B ⊥ v cùng pha).",
        requirements=[
            "Vận dụng được hệ thức của máy biến áp lí tưởng: $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$ (tăng áp bao nhiêu lần thì giảm cường độ dòng điện bấy nhiêu lần).",
            "Tính được công suất hao phí trên đường dây truyền tải điện năng $\\Delta\\mathcal{P} = I^2 R = \\dfrac{\\mathcal{P}^2 R}{U^2 \\cos^2\\varphi}$.",
            "Trình bày được sự hình thành sóng điện từ từ điện từ trường biến thiên và quy tắc tam diện thuận ($\\vec{E}, \\vec{B}, \\vec{v}$ đôi một vuông góc và $\\vec{E}, \\vec{B}$ dao động cùng pha).",
        ],
        definition="Đối với một máy biến áp lí tưởng ($\\mathcal{P}_1 = \\mathcal{P}_2$), tỉ số hiệu điện thế hiệu dụng ở hai đầu cuộn sơ cấp và thứ cấp bằng tỉ số vòng dây và bằng nghịch đảo tỉ số cường độ dòng điện: $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$. Trong sóng điện từ, tại mỗi điểm hai vectơ $\\vec{E}$ và $\\vec{B}$ luôn vuông góc với nhau, vuông góc với phương truyền sóng $\\vec{v}$ và dao động cùng pha.",
        theory=(
            "### 1. Máy biến áp lí tưởng và Truyền tải điện năng đi xa\n"
            "- **Máy biến áp**: hoạt động dựa trên **hiện tượng cảm ứng điện từ**:\n"
            "  $$\\dfrac{U_1}{U_2} = \\dfrac{E_1}{E_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$$\n"
            "  *(Lưu ý: Máy biến áp làm thay đổi $U$ và $I$ nhưng **giữ nguyên tần số $f$** của dòng điện xoay chiều!)*\n"
            "- **Công suất hao phí trên đường dây truyền tải có điện trở $R$**:\n"
            "  $$\\Delta\\mathcal{P} = I^2 R = \\dfrac{\\mathcal{P}^2 \\cdot R}{U^2 \\cos^2\\varphi}$$\n"
            "  Nếu nâng điện áp truyền tải $U$ lên $k$ lần thì công suất hao phí $\\Delta\\mathcal{P}$ giảm đi $k^2$ lần.\n\n"
            "### 2. Điện từ trường và Sóng điện từ (Thuyết Maxwell)\n"
            "- Từ trường biến thiên theo thời gian sinh ra **điện trường xoáy** (có đường sức là đường cong kín); ngược lại điện trường biến thiên theo thời gian sinh ra **từ trường**.\n"
            "- Trong quá trình truyền sóng điện từ, tại mọi điểm:\n"
            "  1. Ba vectơ $(\\vec{E}, \\vec{B}, \\vec{v})$ đôi một vuông góc với nhau tạo thành một **tam diện thuận** (theo quy tắc đinh ốc hoặc bàn tay phải: quay từ $\\vec{E}$ sang $\\vec{B}$ thì chiều tiến là $\\vec{v}$).\n"
            "  2. Hai thành phần **điện trường $\\vec{E}$ và từ trường $\\vec{B}$ tại cùng một điểm luôn dao động CÙNG PHA** với nhau ($\\dfrac{E}{E_0} = \\dfrac{B}{B_0}$)."
        ),
        formulas=[
            G(
                "Công thức Máy biến áp, Truyền tải điện và Sóng điện từ",
                F("Hệ thức Máy biến áp lí tưởng và Công suất hao phí", "$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}; \\qquad \\Delta\\mathcal{P} = \\dfrac{\\mathcal{P}^2 \\cdot R}{U^2 \\cos^2\\varphi}$", "Máy tăng áp ($N_2 > N_1$) làm tăng hiệu điện thế ($U_2 > U_1$) nhưng làm giảm cường độ dòng điện ($I_2 < I_1$)."),
                F("Tương quan phương và pha của E và B trong sóng điện từ", "$\\vec{E} \\perp \\vec{B} \\perp \\vec{v} \\text{ (tam diện thuận)}; \\qquad \\vec{E} \\text{ và } \\vec{B} \\text{ dao động CÙNG PHA } \\left(\\dfrac{E}{E_0} = \\dfrac{B}{B_0}\\right)$", "Khi tại 1 điểm $E$ đạt cực đại $E_0$ thì cảm ứng từ $B$ tại điểm đó cũng đồng thời đạt cực đại $B_0$."),
            )
        ],
        example="Một máy biến áp lí tưởng có số vòng dây cuộn sơ cấp là $N_1 = 500$ vòng và cuộn thứ cấp là $N_2 = 2500$ vòng. Đặt vào cuộn sơ cấp điện áp hiệu dụng $U_1 = 200\\text{ V}$, cường độ dòng điện hiệu dụng chạy trong cuộn sơ cấp là $I_1 = 10\\text{ A}$. Hãy tính điện áp hiệu dụng $U_2$ và cường độ dòng điện hiệu dụng $I_2$ ở mạch thứ cấp.",
        example_answer="Áp dụng hệ thức máy biến áp lí tưởng $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$: Điện áp hiệu dụng ở cuộn thứ cấp là $U_2 = U_1 \\cdot \\dfrac{N_2}{N_1} = 200 \\cdot \\dfrac{2500}{500} = 1000\\text{ V}$. Cường độ dòng điện hiệu dụng ở cuộn thứ cấp là $I_2 = I_1 \\cdot \\dfrac{N_1}{N_2} = 10 \\cdot \\dfrac{500}{2500} = 2\\text{ A}$.",
        real_life="Các bộ sạc điện thoại và máy tính xách tay dùng mạch biến áp hạ áp từ $220\\text{ V}$ xuống $5\\text{ V} - 20\\text{ V}$; còn các trạm phát sóng viễn thông 5G và vệ tinh phát đi sóng điện từ gồm $\\vec{E} \\perp \\vec{B}$ truyền với tốc độ ánh sáng.",
        quiz=[
            mcq("biet", "Đối với một máy biến áp lí tưởng (bỏ qua mọi hao phí), hệ thức liên hệ giữa hiệu điện thế hiệu dụng ($U_1, U_2$), số vòng dây ($N_1, N_2$) và cường độ dòng điện hiệu dụng ($I_1, I_2$) của cuộn sơ cấp và thứ cấp là gì?", ["$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$", "$\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_1}{I_2}$", "$\\dfrac{U_1}{U_2} = \\dfrac{N_2}{N_1} = \\dfrac{I_2}{I_1}$", "$U_1 N_1 = U_2 N_2$"], 0, "Trong máy biến áp lí tưởng, $\\mathcal{P}_1 = \\mathcal{P}_2 \\iff U_1 I_1 = U_2 I_2$, nên $\\dfrac{U_1}{U_2} = \\dfrac{N_1}{N_2} = \\dfrac{I_2}{I_1}$."),
            mcq("biet", "Tại mỗi điểm trong không gian có sóng điện từ truyền qua, dao động của điện trường $\\vec{E}$ và dao động của từ trường $\\vec{B}$ có mối quan hệ về phương và về pha như thế nào?", ["Vuông góc với nhau về phương ($\\vec{E} \\perp \\vec{B}$) nhưng luôn **cùng pha** với nhau về thời gian", "Cùng phương với nhau và ngược pha nhau", "Vuông góc với nhau về phương và lệch pha nhau một góc $\\dfrac{\\pi}{2}$", "Cùng phương và cùng pha với phương truyền sóng $\\vec{v}$"], 0, "Trong sóng điện từ, $\\vec{E}$ và $\\vec{B}$ có phương vuông góc với nhau và vuông góc với $\\vec{v}$, nhưng biến thiên điều hòa **cùng pha** với nhau."),
            mcq("hieu", "Trong truyền tải điện năng đi xa với công suất truyền đi $\\mathcal{P}$ và đường dây không đổi, nếu dùng máy biến áp nâng điện áp hiệu dụng ở đầu đường dây lên gấp $5$ lần thì công suất hao phí do tỏa nhiệt trên đường dây thay đổi như thế nào?", ["Giảm đi $25$ lần", "Giảm đi $5$ lần", "Tăng lên $5$ lần", "Tăng lên $25$ lần"], 0, "Vì $\\Delta\\mathcal{P} = \\dfrac{\\mathcal{P}^2 R}{U^2 \\cos^2\\varphi}$ tỉ lệ nghịch với $U^2$, nên khi tăng $U$ lên $5$ lần thì $\\Delta\\mathcal{P}$ giảm đi $5^2 = 25$ lần."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về máy biến áp và sóng điện từ:", [
                "Máy biến áp làm thay đổi điện áp hiệu dụng và cường độ dòng điện hiệu dụng nhưng giữ nguyên tần số của dòng điện xoay chiều.",
                "Một từ trường biến thiên theo thời gian sinh ra trong không gian xung quanh một điện trường xoáy có các đường sức là đường cong khép kín.",
                "Tại một điểm có sóng điện từ truyền qua, khi cường độ điện trường đạt cực đại ($E = E_0$) thì cảm ứng từ tại điểm đó bằng không ($B = 0$).",
                "Ba vectơ $\\vec{E}, \\vec{B}$ và $\\vec{v}$ tại mỗi điểm của sóng điện từ lập thành một tam diện thuận.",
            ], [True, True, False, True], "Ý c) sai vì $\\vec{E}$ và $\\vec{B}$ trong sóng điện từ dao động **cùng pha** nên khi $E = E_0$ thì $B$ cũng đồng thời đạt cực đại $B = B_0$."),
            short("vandung", "Một máy biến áp lí tưởng có số vòng cuộn sơ cấp $N_1 = 400$ vòng, số vòng cuộn thứ cấp $N_2 = 1200$ vòng. Khi đặt vào cuộn sơ cấp điện áp xoay chiều hiệu dụng $U_1 = 100\\text{ V}$ thì điện áp hiệu dụng ở hai đầu cuộn thứ cấp để hở $U_2$ bằng bao nhiêu Vôn ($\\text{V}$)?", ["300"], "Áp dụng công thức $U_2 = U_1 \\cdot \\dfrac{N_2}{N_1} = 100 \\cdot \\dfrac{1200}{400} = 300\\text{ V}$.", unit="V"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 17: Cấu trúc hạt nhân",
        icon="⚛️",
        description="Thí nghiệm tán xạ hạt alpha của Rutherford, cấu tạo hạt nhân (^A_Z X gồm Z proton và N = A - Z neutron), đồng vị, đơn vị khối lượng nguyên tử amu và bán kính hạt nhân.",
        requirements=[
            "Mô tả được thí nghiệm tán xạ hạt alpha ($\\alpha$) của Ernest Rutherford chứng tỏ nguyên tử có cấu tạo rỗng và tâm nguyên tử là hạt nhân mang điện dương kích thước rất nhỏ ($10^{-15} - 10^{-14}\\text{ m}$).",
            "Biểu diễn được kí hiệu hạt nhân $^A_Z X$, xác định số proton ($Z$), số khối (số nucleon $A$) và số neutron ($N = A - Z$), khái niệm đồng vị.",
            "Vận dụng được đơn vị khối lượng nguyên tử ($1\\text{ amu} \\approx 1{,}66055 \\cdot 10^{-27}\\text{ kg} \\approx 931{,}5\\text{ MeV}/c^2$) và công thức bán kính hạt nhân $R = 1{,}2 \\cdot 10^{-15} A^{1/3}\\text{ (m)}$.",
        ],
        definition="Hạt nhân nguyên tử được cấu tạo từ hai loại hạt nucleon là proton (mang điện tích $+e$) và neutron (không mang điện). Hạt nhân của nguyên tố $X$ được kí hiệu là $^A_Z X$, trong đó $Z$ là số proton (nguyên tử số), $A$ là tổng số nucleon (số khối) và $N = A - Z$ là số hạt neutron.",
        theory=(
            "### 1. Thí nghiệm tán xạ hạt alpha và Cấu tạo hạt nhân\n"
            "- **Thí nghiệm Rutherford (1911)**: Chiếu chùm hạt $\\alpha$ ($^4_2\\text{He}^{2+}$) vào lá vàng rất mỏng: hầu hết các hạt $\\alpha$ truyền thẳng xuyên qua lá vàng, chỉ một tỉ lệ rất nhỏ bị lệch góc lớn hoặc bật ngược trở lại $\\implies$ **Nguyên tử có cấu trúc rỗng**, toàn bộ điện tích dương và gần như toàn bộ khối lượng nguyên tử tập trung ở **hạt nhân** có kích thước cực nhỏ ở tâm.\n"
            "- **Thành phần hạt nhân $^A_Z X$**:\n"
            "  - **Số proton**: $Z$ hạt (mỗi hạt có $q_p = +e = +1{,}6 \\cdot 10^{-19}\\text{ C}$, $m_p \\approx 1{,}00728\\text{ amu}$).\n"
            "  - **Số neutron**: $N = A - Z$ hạt (không mang điện $q_n = 0$, $m_n \\approx 1{,}00866\\text{ amu}$).\n"
            "  - **Số khối (số nucleon)**: $A = Z + N$.\n\n"
            "### 2. Đồng vị, Đơn vị amu và Bán kính hạt nhân\n"
            "- **Đồng vị**: các hạt nhân có **cùng số proton $Z$** nhưng **khác nhau số neutron $N$** (nên khác số khối $A$). Ví dụ 3 đồng vị của hiđrô: $^1_1\\text{H}$ (proti), $^2_1\\text{H}$ hay $^2_1\\text{D}$ (đơteri), $^3_1\\text{H}$ hay $^3_1\\text{T}$ (triti).\n"
            "- **Đơn vị khối lượng nguyên tử ($\\text{amu}$ hay $\\text{u}$)**: bằng $\\dfrac{1}{12}$ khối lượng của một nguyên tử đồng vị carbon $^{12}_6\\text{C}$:\n"
            "  $$1\\text{ amu} \\approx 1{,}66055 \\cdot 10^{-27}\\text{ kg} \\approx 931{,}5\\text{ MeV}/c^2$$\n"
            "- **Bán kính hạt nhân**: $R = r_0 \\cdot A^{1/3}$ với $r_0 = 1{,}2 \\cdot 10^{-15}\\text{ m} = 1{,}2\\text{ fm}$ (thể tích hạt nhân tỉ lệ thuận với số khối $A$, mật độ khối lượng của mọi hạt nhân đều xấp xỉ như nhau và cực lớn $\\approx 2{,}3 \\cdot 10^{17}\\text{ kg/m}^3$)."
        ),
        formulas=[
            G(
                "Cấu trúc hạt nhân ^A_Z X, Đơn vị amu và Bán kính hạt nhân",
                F("Số hạt proton, neutron và nucleon trong hạt nhân ^A_Z X", "$N_{\\text{proton}} = Z; \\qquad N_{\\text{nucleon}} = A; \\qquad N_{\\text{neutron}} = N = A - Z$", "Điện tích của hạt nhân $^A_Z X$ là $q = +Z e$."),
                F("Đơn vị khối lượng amu và Công thức bán kính hạt nhân", "$1\\text{ amu} \\approx 1{,}66055 \\cdot 10^{-27}\\text{ kg} \\approx 931{,}5\\text{ MeV}/c^2; \\qquad R = 1{,}2 \\cdot 10^{-15} \\cdot A^{1/3}\\text{ (m)}$", "Nếu xét $n = \\dfrac{m}{A}$ mol hạt nhân thì số proton trong khối lượng $m$ là $N_p = n N_A Z$ và số neutron là $N_n = n N_A (A - Z)$."),
            )
        ],
        example="Cho hạt nhân uranium $^{235}_{92}\\text{U}$ và hạt nhân nhôm $^{27}_{13}\\text{Al}$. Hãy xác định số proton, số neutron và tổng số nucleon của hạt nhân $^{235}_{92}\\text{U}$, đồng thời tính bán kính $R$ của hạt nhân nhôm $^{27}_{13}\\text{Al}$ theo đơn vị femtômét ($1\\text{ fm} = 10^{-15}\\text{ m}$).",
        example_answer="Trong hạt nhân $^{235}_{92}\\text{U}$ có: số proton là $Z = 92$, tổng số nucleon là $A = 235$, và số neutron là $N = A - Z = 235 - 92 = 143$ hạt. Đối với hạt nhân $^{27}_{13}\\text{Al}$ có $A = 27$, bán kính hạt nhân là $R = 1{,}2 \\cdot A^{1/3} = 1{,}2 \\cdot 27^{1/3} = 1{,}2 \\cdot 3 = 3{,}6\\text{ fm} = 3{,}6 \\cdot 10^{-15}\\text{ m}$.",
        real_life="Nước nặng ($\\text{D}_2\\text{O}$) chứa đồng vị đơteri ($^2_1\\text{D}$) được sử dụng làm chất làm chậm neutron trong các lò phản ứng hạt nhân điện nguyên tử.",
        quiz=[
            mcq("biet", "Trong một hạt nhân nguyên tử được kí hiệu là $^A_Z X$, số hạt **neutron** ($N$) được tính bằng công thức nào?", ["$N = A - Z$", "$N = A + Z$", "$N = Z$", "$N = A$"], 0, "Trong kí hiệu $^A_Z X$, $A$ là tổng số nucleon ($Z$ proton và $N$ neutron) nên số neutron là $N = A - Z$."),
            mcq("biet", "Các **đồng vị** của cùng một nguyên tố hóa học là những hạt nhân có đặc điểm gì?", ["Có cùng số proton $Z$ nhưng khác nhau số neutron $N$ (nên khác số khối $A$)", "Có cùng số khối $A$ nhưng khác số proton $Z$", "Có cùng số neutron $N$ nhưng khác số proton $Z$", "Có số electron lớn hơn số proton"], 0, "Đồng vị (cùng vị trí trong bảng tuần hoàn) là các hạt nhân có cùng số proton $Z$ nhưng khác số neutron $N$."),
            mcq("hieu", "Hạt nhân carbon $^{14}_6\\text{C}$ có bao nhiêu hạt proton, bao nhiêu hạt neutron và bao nhiêu nucleon?", ["$6$ proton, $8$ neutron và $14$ nucleon", "$6$ proton, $14$ neutron và $20$ nucleon", "$8$ proton, $6$ neutron và $14$ nucleon", "$14$ proton, $6$ neutron và $8$ nucleon"], 0, "Với $^{14}_6\\text{C}$, ta có $Z = 6$ proton, $A = 14$ nucleon và $N = 14 - 6 = 8$ neutron."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về cấu trúc hạt nhân:", [
                "Thí nghiệm tán xạ hạt alpha của Rutherford chứng tỏ nguyên tử có cấu tạo rỗng, phần lớn khối lượng và toàn bộ điện tích dương tập trung ở hạt nhân.",
                "Hạt proton và hạt neutron được gọi chung là các nucleon.",
                "Hạt nhân đồng vị triti ($^3_1\\text{T}$) có $3$ hạt proton và $1$ hạt neutron.",
                "Bán kính hạt nhân tỉ lệ thuận với căn bậc ba của số khối $A$ theo công thức $R = 1{,}2 \\cdot 10^{-15} A^{1/3}\\text{ (m)}$.",
            ], [True, True, False, True], "Ý c) sai vì hạt nhân triti $^3_1\\text{T}$ có $Z = 1$ proton và $N = 3 - 1 = 2$ neutron."),
            short("vandung", "Hạt nhân sắt $^{56}_{26}\\text{Fe}$ có bao nhiêu hạt neutron?", ["30"], "Số hạt neutron trong hạt nhân $^{56}_{26}\\text{Fe}$ là $N = A - Z = 56 - 26 = 30$ hạt.", unit="hạt"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 18: Hệ thức Einstein và năng lượng liên kết của hạt nhân",
        icon="💥",
        description="Lực hạt nhân, hệ thức năng lượng – khối lượng Einstein E = m.c², độ hụt khối Δm, năng lượng liên kết W_lk = Δm.c² và năng lượng liên kết riêng W_lkr = W_lk/A.",
        requirements=[
            "Nêu được bản chất và đặc điểm của lực hạt nhân (lực tương tác mạnh giữ các nucleon liên kết chặt trong hạt nhân, có bán kính tác dụng cực ngắn cỡ $10^{-15}\\text{ m}$ và không phụ thuộc điện tích).",
            "Viết và vận dụng được hệ thức Einstein $E = m c^2$, công thức độ hụt khối $\\Delta m = Z m_p + (A - Z)m_n - m_X$ và năng lượng liên kết $W_{\\text{lk}} = \\Delta m \\cdot c^2$ (với $1\\text{ amu}\\cdot c^2 \\approx 931{,}5\\text{ MeV}$).",
            "Nêu được năng lượng liên kết riêng $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A}$ đặc trưng cho **mức độ bền vững của hạt nhân** (các hạt nhân có số khối trung bình $50 < A < 80$ như $^{56}\\text{Fe}$ bền vững nhất).",
        ],
        definition="Khối lượng của một hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tạo thành nó một lượng gọi là độ hụt khối: $\\Delta m = Z m_p + (A - Z)m_n - m_X$. Năng lượng liên kết của hạt nhân là năng lượng tối thiểu dùng để tách toàn bộ hạt nhân thành các nucleon riêng lẻ: $W_{\\text{lk}} = \\Delta m \\cdot c^2$. Năng lượng liên kết riêng $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A}$ đặc trưng cho mức độ bền vững của hạt nhân.",
        theory=(
            "### 1. Lực hạt nhân và Hệ thức Einstein $E = m c^2$\n"
            "- **Lực hạt nhân**: lực hút cực mạnh giữa các nucleon ($p-p, p-n, n-n$) thắng lực đẩy tĩnh điện Coulomb giữa các proton; thuộc loại **tương tác mạnh**, không có bản chất điện hay hấp dẫn, và chỉ phát huy tác dụng trong phạm vi kích thước hạt nhân ($\\approx 10^{-15}\\text{ m}$).\n"
            "- **Hệ thức năng lượng – khối lượng Einstein**: Một vật có khối lượng $m$ thì có năng lượng toàn phần:\n"
            "  $$E = m \\cdot c^2$$\n\n"
            "### 2. Độ hụt khối, Năng lượng liên kết và Năng lượng liên kết riêng\n"
            "- **Độ hụt khối ($\\Delta m$)**: Khối lượng hạt nhân $m_X$ luôn nhỏ hơn tổng khối lượng các nucleon riêng rẽ:\n"
            "  $$\\Delta m = [Z \\cdot m_p + (A - Z) \\cdot m_n] - m_X > 0$$\n"
            "- **Năng lượng liên kết ($W_{\\text{lk}}$)**:\n"
            "  $$W_{\\text{lk}} = \\Delta m \\cdot c^2$$\n"
            "  *(Nếu $\\Delta m$ tính bằng $\\text{amu}$ thì $W_{\\text{lk}}(\\text{MeV}) = \\Delta m(\\text{amu}) \\cdot 931{,}5$)*.\n"
            "- **Năng lượng liên kết riêng ($W_{\\text{lkr}}$ hoặc $\\varepsilon$)**: năng lượng liên kết tính bình quân cho 1 nucleon:\n"
            "  $$W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A} = \\dfrac{\\Delta m \\cdot c^2}{A} \\quad (\\text{đơn vị: } \\text{MeV/nucleon})$$\n"
            "  - **Ý nghĩa**: Hạt nhân có **năng lượng liên kết riêng $W_{\\text{lkr}}$ càng lớn thì càng bền vững** (chứ không phải so sánh $W_{\\text{lk}}$!). Các hạt nhân trung bình ($50 < A < 80$, tiêu biểu là sắt $^{56}_{26}\\text{Fe}$ với $W_{\\text{lkr}} \\approx 8{,}8\\text{ MeV/nucleon}$) là bền vững nhất."
        ),
        formulas=[
            G(
                "Độ hụt khối, Năng lượng liên kết và Năng lượng liên kết riêng",
                F("Độ hụt khối và Năng lượng liên kết của hạt nhân ^A_Z X", "$\\Delta m = Z m_p + (A - Z)m_n - m_X; \\qquad W_{\\text{lk}} = \\Delta m \\cdot c^2 = \\Delta m(\\text{amu}) \\cdot 931{,}5\\text{ (MeV)}$", "Trong đó $1\\text{ amu}\\cdot c^2 \\approx 931{,}5\\text{ MeV}$."),
                F("Năng lượng liên kết riêng (thước đo độ bền vững của hạt nhân)", "$W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A} = \\dfrac{\\Delta m \\cdot c^2}{A}\\text{ (MeV/nucleon)}$", "Hạt nhân nào có $W_{\\text{lkr}}$ lớn hơn thì bền vững hơn."),
            )
        ],
        example="Cho hạt nhân heli $^4_2\\text{He}$ có khối lượng $m_{\\text{He}} = 4{,}0015\\text{ amu}$. Biết khối lượng của proton là $m_p = 1{,}0073\\text{ amu}$, của neutron là $m_n = 1{,}0087\\text{ amu}$ và $1\\text{ amu}\\cdot c^2 = 931{,}5\\text{ MeV}$. Hãy tính độ hụt khối $\\Delta m$, năng lượng liên kết $W_{\\text{lk}}$ và năng lượng liên kết riêng $W_{\\text{lkr}}$ của hạt nhân $^4_2\\text{He}$.",
        example_answer="Hạt nhân $^4_2\\text{He}$ có $Z = 2$ proton và $N = 4 - 2 = 2$ neutron. Độ hụt khối là $\\Delta m = 2m_p + 2m_n - m_{\\text{He}} = 2 \\cdot 1{,}0073 + 2 \\cdot 1{,}0087 - 4{,}0015 = 4{,}0320 - 4{,}0015 = 0{,}0305\\text{ amu}$. Năng lượng liên kết là $W_{\\text{lk}} = \\Delta m \\cdot 931{,}5 = 0{,}0305 \\cdot 931{,}5 \\approx 28{,}41\\text{ MeV}$. Năng lượng liên kết riêng là $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A} = \\dfrac{28{,}41}{4} \\approx 7{,}1\\text{ MeV/nucleon}$.",
        real_life="Hệ thức nổi tiếng $E = mc^2$ của Albert Einstein cho thấy chỉ cần một độ hụt khối rất nhỏ trong phản ứng hạt nhân cũng giải phóng ra nguồn năng lượng khổng lồ gấp hàng triệu lần phản ứng đốt cháy hóa học.",
        quiz=[
            mcq("biet", "Công thức tính **độ hụt khối** $\\Delta m$ của hạt nhân $^A_Z X$ (có khối lượng $m_X$, khối lượng proton là $m_p$ và khối lượng neutron là $m_n$) là gì?", ["$\\Delta m = Z m_p + (A - Z)m_n - m_X$", "$\\Delta m = m_X - [Z m_p + (A - Z)m_n]$", "$\\Delta m = Z m_p + A m_n - m_X$", "$\\Delta m = A m_p + Z m_n + m_X$"], 0, "Tổng khối lượng các nucleon riêng rẽ là $Z m_p + (A - Z)m_n$ luôn lớn hơn khối lượng hạt nhân $m_X$, nên $\\Delta m = Z m_p + (A - Z)m_n - m_X$."),
            mcq("biet", "Đại lượng vật lí nào đặc trưng trực tiếp cho **mức độ bền vững** của một hạt nhân?", ["Năng lượng liên kết riêng $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A}$", "Năng lượng liên kết toàn phần $W_{\\text{lk}}$", "Số khối $A$ của hạt nhân", "Số hạt proton $Z$ của hạt nhân"], 0, "Mức độ bền vững của hạt nhân được quyết định bởi năng lượng liên kết riêng $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A}$ (tính cho 1 nucleon)."),
            mcq("hieu", "Cho ba hạt nhân $X, Y, Z$ có năng lượng liên kết riêng lần lượt là $W_{\\text{lkr}(X)} = 7{,}1\\text{ MeV/nucleon}$, $W_{\\text{lkr}(Y)} = 8{,}8\\text{ MeV/nucleon}$ và $W_{\\text{lkr}(Z)} = 7{,}6\\text{ MeV/nucleon}$. Thứ tự sắp xếp các hạt nhân theo mức độ **bền vững giảm dần** là:", ["$Y, Z, X$", "$X, Z, Y$", "$Z, Y, X$", "$Y, X, Z$"], 0, "Hạt nhân có năng lượng liên kết riêng càng lớn thì càng bền vững; vì $8{,}8 > 7{,}6 > 7{,}1$ nên thứ tự bền vững giảm dần là $Y, Z, X$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về lực hạt nhân và năng lượng liên kết:", [
                "Lực hạt nhân là lực tương tác mạnh giữa các nucleon, chỉ có tác dụng trong phạm vi kích thước hạt nhân ($\\approx 10^{-15}\\text{ m}$).",
                "Khối lượng của một hạt nhân sau khi tạo thành luôn nhỏ hơn tổng khối lượng của các nucleon riêng rẽ tạo nên nó.",
                "Lực hạt nhân có bản chất là lực tĩnh điện Coulomb nên chỉ tác dụng giữa các hạt mang điện.",
                "Các hạt nhân có số khối trung bình (cỡ từ $50$ đến $80$ như $^{56}_{26}\\text{Fe}$) có năng lượng liên kết riêng lớn nhất nên bền vững nhất.",
            ], [True, True, False, True], "Ý c) sai vì lực hạt nhân không phụ thuộc vào điện tích (tác dụng như nhau giữa $p-p, p-n$ và $n-n$) và không có bản chất tĩnh điện."),
            short("vandung", "Một hạt nhân có số khối $A = 16$ và có năng lượng liên kết toàn phần là $W_{\\text{lk}} = 128\\text{ MeV}$. Năng lượng liên kết riêng $W_{\\text{lkr}}$ của hạt nhân này bằng bao nhiêu $\\text{MeV/nucleon}$?", ["8"], "Áp dụng công thức $W_{\\text{lkr}} = \\dfrac{W_{\\text{lk}}}{A} = \\dfrac{128}{16} = 8\\text{ MeV/nucleon}$.", unit="MeV/nucleon"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 19: Phản ứng hạt nhân và năng lượng phản ứng hạt nhân",
        icon="⚗️",
        description="Khái niệm phản ứng hạt nhân (tự phát và kích thích), 4 định luật bảo toàn trong phản ứng hạt nhân và công thức năng lượng phản ứng ΔE = (m_trước - m_sau)c².",
        requirements=[
            "Nêu được khái niệm phản ứng hạt nhân và áp dụng được 4 định luật bảo toàn trong phản ứng hạt nhân: bảo toàn số nucleon (số khối $A$), bảo toàn điện tích ($Z$), bảo toàn động lượng và bảo toàn năng lượng toàn phần.",
            "Nhận biết được trong phản ứng hạt nhân **không có** định luật bảo toàn khối lượng nghỉ.",
            "Tính được năng lượng của phản ứng hạt nhân $\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2 = (W_{\\text{lk sau}} - W_{\\text{lk trước}})$ và phân biệt phản ứng tỏa năng lượng ($\\Delta E > 0$) với phản ứng thu năng lượng ($\\Delta E < 0$).",
        ],
        definition="Phản ứng hạt nhân là mọi quá trình dẫn đến sự biến đổi của các hạt nhân. Trong phản ứng hạt nhân $A + B \\to C + D$, số khối và điện tích luôn được bảo toàn ($A_1 + A_2 = A_3 + A_4$ và $Z_1 + Z_2 = Z_3 + Z_4$). Năng lượng của phản ứng hạt nhân được xác định bởi: $\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2$.",
        theory=(
            "### 1. Bốn định luật bảo toàn trong phản ứng hạt nhân\n"
            "Xét phản ứng hạt nhân: $^{A_1}_{Z_1}X_1 + {}^{A_2}_{Z_2}X_2 \\longrightarrow {}^{A_3}_{Z_3}X_3 + {}^{A_4}_{Z_4}X_4$.\n"
            "1. **Bảo toàn số nucleon (số khối $A$)**: $A_1 + A_2 = A_3 + A_4$.\n"
            "2. **Bảo toàn điện tích (nguyên tử số $Z$)**: $Z_1 + Z_2 = Z_3 + Z_4$.\n"
            "3. **Bảo toàn động lượng**: $\\vec{p}_1 + \\vec{p}_2 = \\vec{p}_3 + \\vec{p}_4$.\n"
            "4. **Bảo toàn năng lượng toàn phần** (gồm năng lượng nghỉ $mc^2$ và động năng $W_{\\text{đ}}$).\n"
            "- *Chú ý*: Trong phản ứng hạt nhân **KHÔNG CÓ** định luật bảo toàn khối lượng nghỉ ($m_{\\text{trước}} \\ne m_{\\text{sau}}$) và không bảo toàn số proton hay số neutron riêng rẽ (vì $p$ có thể biến đổi thành $n$ hoặc ngược lại).\n\n"
            "### 2. Năng lượng của phản ứng hạt nhân ($\\Delta E$)\n"
            "- Gọi $m_{\\text{trước}} = m_1 + m_2$ và $m_{\\text{sau}} = m_3 + m_4$:\n"
            "  $$\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2 = (\\Delta m_{\\text{sau}} - \\Delta m_{\\text{trước}})c^2 = W_{\\text{lk sau}} - W_{\\text{lk trước}} = W_{\\text{đ sau}} - W_{\\text{đ trước}}$$\n"
            "  - Nếu **$m_{\\text{trước}} > m_{\\text{sau}}$ ($\\Delta E > 0$)**: phản ứng **tỏa năng lượng** (các hạt nhân sinh ra bền vững hơn các hạt nhân ban đầu).\n"
            "  - Nếu **$m_{\\text{trước}} < m_{\\text{sau}}$ ($\\Delta E < 0$)**: phản ứng **thu năng lượng** (không tự xảy ra, phải cung cấp động năng ban đầu)."
        ),
        formulas=[
            G(
                "Các định luật bảo toàn và Năng lượng phản ứng hạt nhân",
                F("Bảo toàn số khối A và bảo toàn điện tích Z", "$A_1 + A_2 = A_3 + A_4; \\qquad Z_1 + Z_2 = Z_3 + Z_4$", "Một số hạt sơ cấp thường gặp: proton $^1_1 p$ (hay $^1_1\\text{H}$), neutron $^1_0 n$, hạt $\\alpha$ ($^4_2\\text{He}$), electron $\\beta^-$ ($^0_{-1}e$), positron $\\beta^+$ ($^0_{+1}e$)."),
                F("Năng lượng của phản ứng hạt nhân", "$\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2 = W_{\\text{lk sau}} - W_{\\text{lk trước}} = W_{\\text{đ sau}} - W_{\\text{đ trước}}$", "Nếu $\\Delta E > 0$ ($m_{\\text{trước}} > m_{\\text{sau}}$): phản ứng tỏa năng lượng; nếu $\\Delta E < 0$: phản ứng thu năng lượng."),
            )
        ],
        example="Cho phản ứng hạt nhân: $^2_1\\text{D} + {}^3_1\\text{T} \\longrightarrow {}^4_2\\text{He} + {}^A_Z X$. Hãy xác định $A, Z$ và tên hạt $X$. Biết tổng khối lượng các hạt trước phản ứng lớn hơn tổng khối lượng các hạt sau phản ứng một lượng $m_{\\text{trước}} - m_{\\text{sau}} = 0{,}0189\\text{ amu}$ và $1\\text{ amu}\\cdot c^2 = 931{,}5\\text{ MeV}$, hãy tính năng lượng tỏa ra của một phản ứng này.",
        example_answer="Áp dụng bảo toàn số khối: $2 + 3 = 4 + A \\implies A = 1$; bảo toàn điện tích: $1 + 1 = 2 + Z \\implies Z = 0$. Vậy hạt $X$ là hạt **neutron ($^1_0 n$)**. Năng lượng tỏa ra của một phản ứng là $\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2 = 0{,}0189 \\cdot 931{,}5 \\approx 17{,}6\\text{ MeV}$.",
        real_life="Bắn phá hạt nhân bằng các chùm hạt trong máy gia tốc giúp các nhà vật lí tạo ra các đồng vị nhân tạo dùng trong chẩn đoán và điều trị ung thư.",
        quiz=[
            mcq("biet", "Trong mọi phản ứng hạt nhân, đại lượng nào sau đây **không** được bảo toàn?", ["Khối lượng nghỉ của hệ ($m_{\\text{trước}} \\ne m_{\\text{sau}}$)", "Tổng số nucleon (số khối $A$)", "Điện tích ($Z$)", "Động lượng và năng lượng toàn phần"], 0, "Trong phản ứng hạt nhân, có sự chuyển hóa giữa năng lượng nghỉ và động năng nên tổng khối lượng nghỉ không bảo toàn."),
            mcq("biet", "Một phản ứng hạt nhân là phản ứng **tỏa năng lượng** ($\\Delta E > 0$) khi tổng khối lượng nghỉ của các hạt trước phản ứng ($m_{\\text{trước}}$) và sau phản ứng ($m_{\\text{sau}}$) thỏa mãn điều kiện nào?", ["$m_{\\text{trước}} > m_{\\text{sau}}$ (và tổng năng lượng liên kết sau phản ứng lớn hơn trước phản ứng)", "$m_{\\text{trước}} < m_{\\text{sau}}$", "$m_{\\text{trước}} = m_{\\text{sau}}$", "$m_{\\text{trước}} = 0$"], 0, "Vì $\\Delta E = (m_{\\text{trước}} - m_{\\text{sau}})c^2$, nên phản ứng tỏa năng lượng khi $m_{\\text{trước}} > m_{\\text{sau}}$."),
            mcq("hieu", "Cho phản ứng hạt nhân: $^{27}_{13}\\text{Al} + {}^4_2\\text{He} \\longrightarrow {}^{30}_{15}\\text{P} + {}^A_Z X$. Hạt $X$ trong phản ứng trên là hạt nào?", ["Hạt neutron ($^1_0 n$)", "Hạt proton ($^1_1 p$)", "Hạt electron ($^0_{-1}e$)", "Hạt alpha ($^4_2\\text{He}$)"], 0, "Bảo toàn số khối: $A = 27 + 4 - 30 = 1$; bảo toàn điện tích: $Z = 13 + 2 - 15 = 0$. Vậy $X$ là neutron ($^1_0 n$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản ứng hạt nhân:", [
                "Trong mọi phản ứng hạt nhân, tổng số khối $A$ và tổng điện tích $Z$ luôn được bảo toàn.",
                "Trong phản ứng hạt nhân tỏa năng lượng, các hạt nhân sản phẩm sinh ra bền vững hơn các hạt nhân ban đầu.",
                "Phản ứng hạt nhân chỉ biến đổi lớp vỏ electron bên ngoài nguyên tử chứ không làm biến đổi hạt nhân.",
                "Nếu $m_{\\text{trước}} - m_{\\text{sau}} = 0{,}02\\text{ amu}$ thì phản ứng tỏa ra năng lượng $\\Delta E = 0{,}02 \\cdot 931{,}5 = 18{,}63\\text{ MeV}$.",
            ], [True, True, False, True], "Ý c) sai vì phản ứng hóa học mới biến đổi lớp vỏ electron, còn phản ứng hạt nhân làm biến đổi chính các hạt nhân nguyên tử."),
            short("vandung", "Cho phản ứng hạt nhân: $^9_4\\text{Be} + {}^4_2\\text{He} \\longrightarrow {}^A_6\\text{C} + {}^1_0 n$. Giá trị số khối $A$ của hạt nhân carbon tạo thành bằng bao nhiêu?", ["12"], "Theo định luật bảo toàn số khối: $9 + 4 = A + 1 \\implies A = 12$ ($^{12}_6\\text{C}$)."),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 20: Phản ứng phân hạch và phản ứng nhiệt hạch",
        icon="☀️",
        description="Cơ chế phản ứng phân hạch của U-235, phản ứng phân hạch dây chuyền và hệ số nhân neutron k, phản ứng nhiệt hạch (tổng hợp hạt nhân nhẹ) trên Mặt Trời.",
        requirements=[
            "Nêu được phản ứng phân hạch là phản ứng trong đó một hạt nhân nặng (như $^{235}_{92}\\text{U}, {}^{239}_{94}\\text{Pu}$) hấp thụ một neutron chậm rồi vỡ thành hai hạt nhân trung bình, kèm theo giải phóng $2 - 3$ neutron mới và tỏa năng lượng lớn ($\\approx 200\\text{ MeV}$).",
            "Biện luận được điều kiện phản ứng phân hạch dây chuyền theo hệ số nhân neutron $k$ ($k < 1$: tắt nhanh; $k = 1$: tự duy trì có điều khiển trong nhà máy điện hạt nhân; $k > 1$: bùng nổ không điều khiển).",
            "Nêu được phản ứng nhiệt hạch là phản ứng tổng hợp hai hạt nhân rất nhẹ (như $^1_1\\text{H}, {}^2_1\\text{D}, {}^3_1\\text{T}$) thành hạt nhân nặng hơn ở nhiệt độ cực cao (hàng chục đến hàng trăm triệu độ) và là nguồn năng lượng của Mặt Trời, các ngôi sao.",
        ],
        definition="Phản ứng phân hạch là phản ứng trong đó một hạt nhân nặng vỡ thành hai mảnh hạt nhân nhẹ hơn (số khối trung bình). Phản ứng nhiệt hạch là phản ứng tổng hợp hai hạt nhân rất nhẹ thành một hạt nhân nặng hơn ở điều kiện nhiệt độ hàng chục triệu độ. Cả hai loại phản ứng đều là phản ứng hạt nhân tỏa năng lượng lớn.",
        theory=(
            "### 1. Phản ứng phân hạch và Phản ứng dây chuyền\n"
            "- **Cơ chế phân hạch kích thích của $^{235}_{92}\\text{U}$**: Hạt nhân $^{235}_{92}\\text{U}$ hấp thụ một **neutron chậm (neutron nhiệt)** chuyển thành trạng thái kích thích không bền $^{236}_{92}\\text{U}^*$, rồi vỡ thành hai hạt nhân có số khối trung bình kèm theo $k$ neutron mới ($k = 2$ hoặc $3$) và tỏa khoảng $\\Delta E \\approx 200\\text{ MeV}$ mỗi phân hạch:\n"
            "  $$^1_0 n + {}^{235}_{92}\\text{U} \\longrightarrow {}^{236}_{92}\\text{U}^* \\longrightarrow {}^{A_1}_{Z_1}X + {}^{A_2}_{Z_2}Y + k \\cdot {}^1_0 n$$\n"
            "- **Hệ số nhân neutron ($k$)** và điều kiện khối lượng tới hạn:\n"
            "  - $k < 1$: phản ứng dây chuyền tắt nhanh.\n"
            "  - **$k = 1$**: phản ứng dây chuyền tự duy trì với công suất không đổi (**trong lò phản ứng của nhà máy điện hạt nhân**, điều khiển bằng các thanh điều khiển chứa Bo hoặc Cadimi hấp thụ neutron thừa).\n"
            "  - $k > 1$ (khi khối lượng nhiên liệu vượt quá khối lượng tới hạn): phản ứng dây chuyền bùng nổ mãnh liệt (bom nguyên tử).\n\n"
            "### 2. Phản ứng nhiệt hạch (Tổng hợp hạt nhân)\n"
            "- Là sự kết hợp hai hạt nhân rất nhẹ ($A \\le 4$, như $^2_1\\text{D} + {}^3_1\\text{T} \\to {}^4_2\\text{He} + {}^1_0 n + 17{,}6\\text{ MeV}$) thành hạt nhân nặng hơn.\n"
            "- **Điều kiện thực hiện**: Để thắng lực đẩy tĩnh điện Coulomb giữa hai hạt nhân mang điện dương, hỗn hợp nhiên liệu phải ở trạng thái plasma có **mật độ hạt lớn** và **nhiệt độ cực cao** (từ $50\\text{ triệu}$ đến $100\\text{ triệu độ K}$).\n"
            "- **Ưu điểm của năng lượng nhiệt hạch**: tính trên cùng một đơn vị khối lượng nhiên liệu, phản ứng nhiệt hạch tỏa năng lượng lớn hơn phân hạch, nguồn nhiên liệu đơteri trong nước biển gần như vô tận và sản phẩm ($^4_2\\text{He}$) sạch, không gây ô nhiễm phóng xạ như chất thải phân hạch.\n"
            "- Nguồn năng lượng của **Mặt Trời và các ngôi sao** chính là các phản ứng nhiệt hạch tổng hợp hiđrô thành heli."
        ),
        formulas=[
            G(
                "Phản ứng Phân hạch và Phản ứng Nhiệt hạch",
                F("Phương trình tổng quát phân hạch U-235 và Hệ số nhân neutron k", "$^1_0 n + {}^{235}_{92}\\text{U} \\to {}^{A_1}_{Z_1}X + {}^{A_2}_{Z_2}Y + k\\,{}^1_0 n \\ (\\Delta E \\approx 200\\text{ MeV}); \\qquad \\text{Lò điện hạt nhân: } k = 1$", "Trong lò phản ứng hạt nhân, dùng thanh điều khiển chứa Bo ($\\text{B}$) hoặc Cadimi ($\\text{Cd}$) để hấp thụ neutron thừa giữ đúng $k = 1$."),
                F("Phương trình phản ứng nhiệt hạch D - T", "$^2_1\\text{D} + {}^3_1\\text{T} \\longrightarrow {}^4_2\\text{He} + {}^1_0 n + 17{,}6\\text{ MeV}$", "Cả phản ứng phân hạch và phản ứng nhiệt hạch đều là phản ứng hạt nhân **tỏa năng lượng**."),
            )
        ],
        example="Trong một phản ứng phân hạch của hạt nhân $^{235}_{92}\\text{U}$ khi hấp thụ một neutron chậm: $^1_0 n + {}^{235}_{92}\\text{U} \\longrightarrow {}^{95}_{42}\\text{Mo} + {}^{139}_{57}\\text{La} + k\\,{}^1_0 n + 7\\,{}^0_{-1}e$. Hãy áp dụng định luật bảo toàn số khối để tìm số hạt neutron $k$ sinh ra sau phản ứng này.",
        example_answer="Tổng số khối trước phản ứng là $A_{\\text{trước}} = 1 + 235 = 236$. Tổng số khối sau phản ứng là $A_{\\text{sau}} = 95 + 139 + k \\cdot 1 + 7 \\cdot 0 = 234 + k$. Từ $A_{\\text{trước}} = A_{\\text{sau}} \\implies 236 = 234 + k \\implies k = 2$ neutron.",
        real_life="Năng lượng ánh sáng và nhiệt từ Mặt Trời sưởi ấm Trái Đất suốt hàng tỉ năm qua được tạo ra từ phản ứng nhiệt hạch tổng hợp các hạt nhân hiđrô thành hạt nhân heli ở lõi Mặt Trời.",
        quiz=[
            mcq("biet", "Để lò phản ứng của một **nhà máy điện hạt nhân** hoạt động ổn định với công suất không đổi và an toàn, hệ số nhân neutron $k$ trong phản ứng phân hạch dây chuyền phải được điều khiển bằng bao nhiêu?", ["$k = 1$", "$k > 1$", "$k = 0$", "$k = 10$"], 0, "Trong lò phản ứng hạt nhân, các thanh điều khiển hấp thụ bớt neutron thừa để duy trì hệ số nhân neutron đúng bằng $k = 1$."),
            mcq("biet", "Nguồn năng lượng khổng lồ tỏa ra liên tục từ Mặt Trời và các ngôi sao trong vũ trụ có bản chất là loại phản ứng nào?", ["Phản ứng nhiệt hạch (tổng hợp các hạt nhân hiđrô nhẹ thành hạt nhân heli)", "Phản ứng phân hạch hạt nhân uranium", "Phản ứng đốt cháy than đá và khí ôxi", "Hiện tượng phóng xạ tự nhiên của chì"], 0, "Trong lòng Mặt Trời và các ngôi sao diễn ra phản ứng nhiệt hạch tổng hợp hiđrô thành heli."),
            mcq("hieu", "Vì sao phản ứng tổng hợp hạt nhân nhẹ lại được gọi là **phản ứng nhiệt hạch** (cần nhiệt độ lên tới hàng chục triệu độ)?", ["Vì cần nhiệt độ cực cao để các hạt nhân nhẹ có động năng nhiệt đủ lớn thắng được lực đẩy tĩnh điện Coulomb và tiến lại gần nhau trong phạm vi tác dụng của lực hạt nhân", "Vì phản ứng này thu nhiệt làm lạnh môi trường xuống $0\\text{ K}$", "Vì phản ứng này chỉ xảy ra với các hạt nhân rất nặng như $^{235}\\text{U}$", "Vì các hạt neutron mang điện tích dương đẩy nhau"], 0, "Hai hạt nhân nhẹ đều mang điện tích dương nên đẩy nhau bằng lực Coulomb; cần nhiệt độ hàng chục triệu độ để chúng chuyển động cực nhanh vượt qua rào thế Coulomb tiến tới khoảng cách $\\approx 10^{-15}\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản ứng phân hạch và phản ứng nhiệt hạch:", [
                "Cả phản ứng phân hạch và phản ứng nhiệt hạch đều là các phản ứng hạt nhân tỏa năng lượng.",
                "Trong phản ứng phân hạch của $^{235}_{92}\\text{U}$, một hạt nhân nặng hấp thụ một neutron chậm rồi vỡ thành hai hạt nhân trung bình và giải phóng thêm $2$ đến $3$ neutron.",
                "Tính theo cùng một khối lượng nhiên liệu (ví dụ $1\\text{ gam}$), phản ứng nhiệt hạch tỏa ra năng lượng nhỏ hơn rất nhiều so với phản ứng phân hạch.",
                "Trong lò phản ứng hạt nhân, các thanh điều khiển có chứa Bo hoặc Cadimi dùng để hấp thụ các neutron thừa nhằm khống chế hệ số nhân neutron $k = 1$.",
            ], [True, True, False, True], "Ý c) sai vì tính trên cùng một đơn vị khối lượng nhiên liệu (ví dụ $1\\text{ g}$), phản ứng nhiệt hạch tỏa ra năng lượng lớn gấp khoảng $3$ đến $4$ lần phản ứng phân hạch."),
            short("vandung", "Biết mỗi phân hạch của một hạt nhân $^{235}_{92}\\text{U}$ tỏa ra năng lượng trung bình là $200\\text{ MeV}$. Khi $10$ hạt nhân $^{235}_{92}\\text{U}$ phân hạch hoàn toàn thì tổng năng lượng tỏa ra bằng bao nhiêu $\\text{MeV}$?", ["2000"], "Tổng năng lượng tỏa ra là $E = 10 \\cdot 200 = 2000\\text{ MeV}$.", unit="MeV"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 21: Hiện tượng phóng xạ",
        icon="☢️",
        description="Bản chất tự phát của hiện tượng phóng xạ, các tia phóng xạ α, β⁻, β⁺, γ, chu kì bán rã T, hằng số phóng xạ λ = ln2/T và định luật phóng xạ N(t) = N₀.2^(-t/T).",
        requirements=[
            "Nêu được hiện tượng phóng xạ là quá trình phân rã tự phát của một hạt nhân không bền vững, hoàn toàn ngẫu nhiên và không phụ thuộc vào các tác động lí – hóa bên ngoài (nhiệt độ, áp suất).",
            "Nêu được bản chất, phương trình phân rã và khả năng ion hóa, đâm xuyên của các tia phóng xạ $\\alpha$ ($^4_2\\text{He}$), $\\beta^-$ ($^0_{-1}e$), $\\beta^+$ ($^0_{+1}e$) và $\\gamma$ (photon năng lượng cao).",
            "Viết và vận dụng được công thức hằng số phóng xạ $\\lambda = \\dfrac{\\ln 2}{T}$ và định luật phóng xạ: $N(t) = N_0 \\cdot 2^{-\\frac{t}{T}} = N_0 e^{-\\lambda t}$, $m(t) = m_0 \\cdot 2^{-\\frac{t}{T}}$.",
        ],
        definition="Hiện tượng phóng xạ là hiện tượng một hạt nhân không bền vững tự phát phân rã, phát ra các tia phóng xạ và biến đổi thành hạt nhân khác. Chu kì bán rã ($T$) là khoảng thời gian để một nửa số hạt nhân của một mẫu chất phóng xạ phân rã. Số hạt nhân và khối lượng chất phóng xạ còn lại sau thời gian $t$ giảm theo hàm mũ: $N(t) = N_0 \\cdot 2^{-t/T} = N_0 e^{-\\lambda t}$ và $m(t) = m_0 \\cdot 2^{-t/T}$.",
        theory=(
            "### 1. Bản chất của hiện tượng phóng xạ và các tia phóng xạ\n"
            "- **Đặc điểm**: Hoàn toàn do nguyên nhân bên trong hạt nhân, mang tính tự phát, ngẫu nhiên và **không chịu ảnh hưởng bởi nhiệt độ, áp suất hay trạng thái hợp chất hóa học**.\n"
            "- **Các loại tia phóng xạ**:\n"
            "  1. **Phóng xạ $\\alpha$**: dòng hạt nhân $^4_2\\text{He}$ ($^A_Z X \\to {}^{A-4}_{Z-2}Y + {}^4_2\\text{He}$). Khả năng **ion hóa mạnh nhất**, nhưng khả năng **đâm xuyên yếu nhất** (chỉ đi được vài $\\text{cm}$ trong không khí, bị tờ giấy mỏng chặn lại).\n"
            "  2. **Phóng xạ $\\beta^-$**: dòng electron $^0_{-1}e$ ($^A_Z X \\to {}^A_{Z+1}Y + {}^0_{-1}e + \\tilde{\\nu}$); và **phóng xạ $\\beta^+$**: dòng positron $^0_{+1}e$ ($^A_Z X \\to {}^A_{Z-1}Y + {}^0_{+1}e + \\nu$). Đâm xuyên mạnh hơn tia $\\alpha$ (bị tấm nhôm dày vài $\\text{mm}$ chặn lại).\n"
            "  3. **Phóng xạ $\\gamma$ (tia gamma)**: sóng điện từ (chùm photon) có bước sóng cực ngắn ($\\lambda < 10^{-11}\\text{ m}$), đi kèm theo phân rã $\\alpha, \\beta$, **không mang điện** (không bị lệch trong điện trường và từ trường), không làm thay đổi $A$ và $Z$, có **khả năng đâm xuyên mạnh nhất** (phải dùng khối chì dày hoặc bê tông dày để chắn).\n\n"
            "### 2. Chu kì bán rã, Hằng số phóng xạ và Định luật phóng xạ\n"
            "- **Hằng số phóng xạ ($\\lambda$)**: đặc trưng cho từng chất phóng xạ, liên hệ với chu kì bán rã $T$ (theo giây $\\text{s}$):\n"
            "  $$\\lambda = \\dfrac{\\ln 2}{T} \\approx \\dfrac{0{,}693}{T} \\quad (\\text{đơn vị: } \\text{s}^{-1})$$\n"
            "- **Định luật phóng xạ**:\n"
            "  - Số hạt nhân (hoặc khối lượng) **còn lại** sau thời gian $t$: $N(t) = N_0 \\cdot 2^{-\\frac{t}{T}} = N_0 e^{-\\lambda t}$; $m(t) = m_0 \\cdot 2^{-\\frac{t}{T}}$.\n"
            "  - Số hạt nhân (hoặc khối lượng) **đã bị phân rã** sau thời gian $t$: $\\Delta N = N_0 - N(t) = N_0\\left(1 - 2^{-\\frac{t}{T}}\\right)$; $\\Delta m = m_0\\left(1 - 2^{-\\frac{t}{T}}\\right)$."
        ),
        formulas=[
            G(
                "Hằng số phóng xạ và Định luật phóng xạ",
                F("Hằng số phóng xạ và Số hạt / Khối lượng còn lại", "$\\lambda = \\dfrac{\\ln 2}{T}; \\qquad N(t) = N_0 \\cdot 2^{-\\frac{t}{T}} = N_0 e^{-\\lambda t}; \\qquad m(t) = m_0 \\cdot 2^{-\\frac{t}{T}}$", "Khi tính $2^{-t/T}$, chỉ cần $t$ và $T$ để cùng một đơn vị thời gian (cùng là ngày, năm, giờ hoặc giây)."),
                F("Số hạt nhân và Khối lượng đã bị phân rã", "$\\Delta N = N_0 - N(t) = N_0\\left(1 - 2^{-\\frac{t}{T}}\\right); \\qquad \\Delta m = m_0\\left(1 - 2^{-\\frac{t}{T}}\\right)$", "Tỉ số giữa số hạt nhân con tạo thành và số hạt nhân mẹ còn lại tại thời điểm $t$: $\\dfrac{N_{\\text{con}}}{N_{\\text{mẹ}}} = \\dfrac{\\Delta N}{N(t)} = 2^{\\frac{t}{T}} - 1$."),
            )
        ],
        example="Đồng vị phóng xạ iốt $^{131}_{53}\\text{I}$ dùng trong y học có chu kì bán rã là $T = 8\\text{ ngày}$. Ban đầu một mẫu chất có khối lượng $m_0 = 64\\text{ g}$ chất phóng xạ $^{131}_{53}\\text{I}$ nguyên chất. Hãy tính khối lượng $m$ của $^{131}_{53}\\text{I}$ còn lại và khối lượng $\\Delta m$ đã bị phân rã sau thời gian $t = 24\\text{ ngày}$.",
        example_answer="Ta có $\\dfrac{t}{T} = \\dfrac{24}{8} = 3$ chu kì bán rã. Khối lượng $^{131}_{53}\\text{I}$ còn lại sau $24\\text{ ngày}$ là $m(t) = m_0 \\cdot 2^{-t/T} = 64 \\cdot 2^{-3} = \\dfrac{64}{8} = 8\\text{ g}$. Khối lượng $^{131}_{53}\\text{I}$ đã bị phân rã là $\\Delta m = m_0 - m(t) = 64 - 8 = 56\\text{ g}$.",
        real_life="Phương pháp xác định niên đại cổ vật bằng đồng vị phóng xạ carbon $^{14}_6\\text{C}$ (có chu kì bán rã $T \\approx 5730\\text{ năm}$) cho phép các nhà khảo cổ tính chính xác tuổi của các mẫu gỗ, xương hóa thạch cổ đại.",
        quiz=[
            mcq("biet", "Tia phóng xạ nào sau đây là bản chất sóng điện từ có bước sóng cực ngắn, **không mang điện** (không bị lệch trong điện trường và từ trường) và có khả năng đâm xuyên mạnh nhất?", ["Tia gamma ($\\gamma$)", "Tia alpha ($\\alpha$)", "Tia bêta trừ ($\\beta^-$)", "Tia bêta cộng ($\\beta^+$)"], 0, "Tia gamma ($\\gamma$) là chùm photon năng lượng rất cao, không mang điện nên không bị lệch trong điện trường và từ trường."),
            mcq("biet", "Gọi $N_0$ là số hạt nhân ban đầu của một mẫu chất phóng xạ có chu kì bán rã $T$. Số hạt nhân còn lại $N(t)$ của mẫu chất đó sau khoảng thời gian $t$ được xác định bởi công thức nào?", ["$N(t) = N_0 \\cdot 2^{-\\frac{t}{T}}$", "$N(t) = N_0 \\cdot 2^{\\frac{t}{T}}$", "$N(t) = \\dfrac{N_0 \\cdot T}{t}$", "$N(t) = N_0\\left(1 - \\dfrac{t}{T}\\right)$"], 0, "Theo định luật phóng xạ, số hạt nhân còn lại sau thời gian $t$ là $N(t) = N_0 \\cdot 2^{-\\frac{t}{T}} = N_0 e^{-\\lambda t}$."),
            mcq("hieu", "Khi hạt nhân $^{238}_{92}\\text{U}$ phóng xạ phát ra một hạt $\\alpha$ ($^4_2\\text{He}$) để biến đổi thành hạt nhân con $^A_Z\\text{Th}$ thì giá trị của số khối $A$ và nguyên tử số $Z$ của hạt nhân con lần lượt là:", ["$A = 234$ và $Z = 90$", "$A = 238$ và $Z = 91$", "$A = 234$ và $Z = 92$", "$A = 242$ và $Z = 94$"], 0, "Trong phóng xạ $\\alpha$ ($^4_2\\text{He}$), số khối giảm $4$ đơn vị ($A = 238 - 4 = 234$) và điện tích giảm $2$ đơn vị ($Z = 92 - 2 = 90$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về hiện tượng phóng xạ:", [
                "Tia alpha ($\\alpha$) thực chất là dòng các hạt nhân heli ($^4_2\\text{He}$).",
                "Nếu nung nóng một mẫu chất phóng xạ lên $2000^\\circ\\text{C}$ thì chu kì bán rã $T$ của nó giảm đi một nửa.",
                "Hằng số phóng xạ $\\lambda$ liên hệ với chu kì bán rã $T$ theo công thức $\\lambda = \\dfrac{\\ln 2}{T}$.",
                "Sau thời gian $t = 2T$ (hai chu kì bán rã), số hạt nhân phóng xạ còn lại bằng $25\\%$ số hạt nhân ban đầu (và đã phân rã $75\\%$).",
            ], [True, False, True, True], "Ý b) sai vì quá trình phóng xạ xảy ra bên trong hạt nhân, hoàn toàn không phụ thuộc vào nhiệt độ, áp suất hay tác động bên ngoài."),
            short("vandung", "Một mẫu chất phóng xạ có khối lượng ban đầu $m_0 = 40\\text{ g}$ và chu kì bán rã $T = 5\\text{ giờ}$. Sau thời gian $t = 10\\text{ giờ}$, khối lượng chất phóng xạ đó **còn lại** bằng bao nhiêu gam ($\\text{g}$)?", ["10"], "Ta có $\\dfrac{t}{T} = \\dfrac{10}{5} = 2$. Khối lượng còn lại là $m = m_0 \\cdot 2^{-2} = \\dfrac{40}{4} = 10\\text{ g}$.", unit="g"),
        ],
    ),
    bai(
        topic=CH4[0], chapter_title=CH4[1], chapter_desc=CH4[2],
        title="Bài 22: Độ phóng xạ và an toàn phóng xạ. Công nghiệp hạt nhân",
        icon="🛡️",
        description="Định nghĩa và công thức độ phóng xạ H = λ.N = H₀.2^(-t/T) (đơn vị Becquerel - Bq), ứng dụng đồng vị phóng xạ và 3 nguyên tắc vàng về an toàn phóng xạ.",
        requirements=[
            "Định nghĩa được độ phóng xạ $H$ là đại lượng đặc trưng cho tính phóng xạ mạnh hay yếu của một lượng chất phóng xạ, đo bằng số phân rã trong $1\\text{ giây}$: $H = -\\dfrac{\\Delta N}{\\Delta t} = \\lambda \\cdot N$ (đơn vị Becquerel – $\\text{Bq}$).",
            "Vận dụng được công thức giảm độ phóng xạ theo thời gian $H(t) = H_0 \\cdot 2^{-\\frac{t}{T}} = H_0 e^{-\\lambda t} = \\lambda \\cdot N(t)$.",
            "Nêu được các ứng dụng của công nghiệp hạt nhân (điện hạt nhân, xạ trị y học, chiếu xạ bảo quản thực phẩm, tạo giống đột biến, định tuổi cổ vật) và **3 nguyên tắc cơ bản về an toàn phóng xạ**: giảm thời gian tiếp xúc, tăng khoảng cách tới nguồn và che chắn thích hợp.",
        ],
        definition="Độ phóng xạ ($H$) là đại lượng đặc trưng cho tính phóng xạ mạnh hay yếu của một lượng chất phóng xạ, được xác định bằng số hạt nhân phân rã trong một giây: $H = \\lambda \\cdot N = H_0 \\cdot 2^{-t/T} = H_0 e^{-\\lambda t}$ (đơn vị trong hệ SI là Becquerel – $\\text{Bq}$, với $1\\text{ Bq} = 1\\text{ phân rã/giây}$).",
        theory=(
            "### 1. Độ phóng xạ ($H$)\n"
            "- Biểu thức liên hệ giữa độ phóng xạ $H$, hằng số phóng xạ $\\lambda$ và số hạt nhân $N$ tại thời điểm $t$:\n"
            "  $$H(t) = \\lambda \\cdot N(t) = \\dfrac{\\ln 2}{T} \\cdot N(t) = H_0 \\cdot 2^{-\\frac{t}{T}} = H_0 e^{-\\lambda t}$$\n"
            "  trong đó $H_0 = \\lambda \\cdot N_0$ là độ phóng xạ ban đầu lúc $t = 0$.\n"
            "  *(Lưu ý: Khi dùng công thức $H = \\lambda N = \\dfrac{\\ln 2}{T}N$ để tính $H$ ra đơn vị $\\text{Bq}$, bắt buộc phải đổi chu kì bán rã $T$ ra đơn vị **giây ($\\text{s}$)**!)*\n"
            "- **Đơn vị**:\n"
            "  - Trong hệ SI: **Becquerel** (kí hiệu $\\text{Bq}$): $1\\text{ Bq} = 1\\text{ phân rã/s} = 1\\text{ s}^{-1}$.\n"
            "  - Đơn vị thực hành truyền thống: **Curie** (kí hiệu $\\text{Ci}$): $1\\text{ Ci} = 3{,}7 \\cdot 10^{10}\\text{ Bq}$.\n\n"
            "### 2. Ứng dụng công nghiệp hạt nhân và 3 nguyên tắc vàng về An toàn phóng xạ\n"
            "- **Ứng dụng**: Nhà máy điện hạt nhân (không phát thải khí nhà kính $\\text{CO}_2$); Y học hạt nhân (dùng $^{131}\\text{I}$ chẩn đoán/điều trị bướu tuyến giáp, tia $\\gamma$ của $^{60}\\text{Co}$ xạ trị ung thư); Nông nghiệp & Thực phẩm (tạo giống cây trồng đột biến năng suất cao, chiếu xạ thanh trùng bảo quản nông sản xuất khẩu); Khảo cổ học ($^{14}\\text{C}$).\n"
            "- **Ba nguyên tắc cơ bản đảm bảo an toàn phóng xạ**:\n"
            "  1. **Giảm thời gian tiếp xúc**: ở gần nguồn phóng xạ trong thời gian càng ngắn càng tốt.\n"
            "  2. **Tăng khoảng cách**: giữ khoảng cách càng xa nguồn phóng xạ càng an toàn (cường độ bức xạ giảm nhanh theo bình phương khoảng cách).\n"
            "  3. **Che chắn thích hợp**: sử dụng màn chắn chuyên dụng (áo giáp chì, tường bê tông dày, kính pha chì) giữa cơ thể và nguồn phóng xạ."
        ),
        formulas=[
            G(
                "Công thức Độ phóng xạ và Định tuổi cổ vật",
                F("Độ phóng xạ tại thời điểm t", "$H(t) = \\lambda \\cdot N(t) = \\dfrac{\\ln 2}{T(\\text{s})} \\cdot N(t); \\qquad H(t) = H_0 \\cdot 2^{-\\frac{t}{T}} = H_0 e^{-\\lambda t}$", "Đơn vị: $1\\text{ Bq} = 1\\text{ s}^{-1}$; $1\\text{ kBq} = 10^3\\text{ Bq}$; $1\\text{ MBq} = 10^6\\text{ Bq}$; $1\\text{ Ci} = 3{,}7 \\cdot 10^{10}\\text{ Bq}$."),
                F("Tính tuổi cổ vật theo độ phóng xạ C-14", "$\\dfrac{H}{H_0} = 2^{-\\frac{t}{T}} \\implies t = T \\cdot \\log_2\\left(\\dfrac{H_0}{H}\\right) = \\dfrac{T}{\\ln 2} \\cdot \\ln\\left(\\dfrac{H_0}{H}\\right)$", "Ba quy tắc vàng an toàn phóng xạ: **Thời gian (ngắn nhất) – Khoảng cách (xa nhất) – Che chắn (chì/bê tông)**."),
            )
        ],
        example="Một dược chất phóng xạ dùng trong y học có độ phóng xạ ban đầu là $H_0 = 800\\text{ MBq}$ và chu kì bán rã là $T = 6\\text{ giờ}$. Hãy tính độ phóng xạ $H$ của mẫu dược chất này sau khoảng thời gian $t = 18\\text{ giờ}$.",
        example_answer="Số chu kì bán rã đã trôi qua là $\\dfrac{t}{T} = \\dfrac{18}{6} = 3$. Độ phóng xạ của mẫu dược chất còn lại sau $18\\text{ giờ}$ là $H = H_0 \\cdot 2^{-t/T} = 800 \\cdot 2^{-3} = \\dfrac{800}{8} = 100\\text{ MBq}$.",
        real_life="Tại các khoa Y học hạt nhân và X-quang của bệnh viện, bên ngoài cửa phòng máy luôn gắn biển cảnh báo phóng xạ hình cánh quạt ba lá màu đen trên nền tam giác vàng và nhân viên y tế luôn mặc tạp dề chì bảo hộ để chắn bức xạ.",
        quiz=[
            mcq("biet", "Đơn vị đo của **độ phóng xạ** $H$ trong hệ thống đo lường quốc tế SI là gì?", ["Becquerel ($\\text{Bq}$, với $1\\text{ Bq} = 1\\text{ phân rã/giây}$)", "Tesla ($\\text{T}$)", "Sievert ($\\text{Sv}$)", "amu"], 0, "Trong hệ SI, đơn vị của độ phóng xạ $H$ là Becquerel ($\\text{Bq}$)."),
            mcq("biet", "Ba nguyên tắc cơ bản nhất để đảm bảo **an toàn phóng xạ** khi làm việc với nguồn phóng xạ là gì?", ["Giảm thời gian tiếp xúc, giữ khoảng cách xa nguồn và sử dụng màn chắn (chì, bê tông) thích hợp", "Tăng thời gian tiếp xúc, đứng thật gần nguồn và không dùng đồ bảo hộ", "Đun nóng nguồn phóng xạ để khử tính phóng xạ", "Ngâm nguồn phóng xạ vào nước muối loãng"], 0, "Ba nguyên tắc vàng về an toàn phóng xạ là: Thời gian tiếp xúc ngắn nhất – Khoảng cách xa nhất – Che chắn thích hợp."),
            mcq("hieu", "Một mẫu gỗ cổ đại tìm thấy trong di chỉ khảo cổ có độ phóng xạ của đồng vị $^{14}_6\\text{C}$ bằng $\\dfrac{1}{2}$ độ phóng xạ của một mẫu gỗ tươi cùng loại vừa mới đốn hạ ($H = 0{,}5 H_0$). Biết chu kì bán rã của $^{14}_6\\text{C}$ là $T = 5730\\text{ năm}$, tuổi của mẫu gỗ cổ đó là bao nhiêu?", ["$5730\\text{ năm}$", "$11\\,460\\text{ năm}$", "$2865\\text{ năm}$", "$17\\,190\\text{ năm}$"], 0, "Vì $H = \\dfrac{1}{2}H_0 = H_0 \\cdot 2^{-1}$ nên thời gian đã trôi qua đúng bằng $1$ chu kì bán rã: $t = T = 5730\\text{ năm}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về độ phóng xạ và công nghiệp hạt nhân:", [
                "Độ phóng xạ $H$ của một mẫu chất phóng xạ tỉ lệ thuận với số hạt nhân phóng xạ $N$ hiện có trong mẫu ($H = \\lambda N$).",
                "Theo thời gian, độ phóng xạ của một mẫu chất giảm dần theo cùng quy luật hàm mũ với số hạt nhân: $H(t) = H_0 \\cdot 2^{-t/T}$.",
                "Thực phẩm, trái cây sau khi được chiếu xạ bằng tia gamma để diệt vi khuẩn và nấm mốc sẽ biến thành chất phóng xạ nguy hiểm.",
                "Nhà máy điện hạt nhân sản xuất điện năng ổn định quy mô lớn mà hầu như không phát thải khí nhà kính $\\text{CO}_2$ trong quá trình vận hành.",
            ], [True, True, False, True], "Ý c) sai vì chiếu xạ thực phẩm bằng tia $\\gamma$ với liều lượng kiểm soát chỉ tiêu diệt vi sinh vật gây thối hỏng chứ hoàn toàn không làm thực phẩm bị nhiễm phóng xạ."),
            short("vandung", "Một nguồn phóng xạ có độ phóng xạ ban đầu $H_0 = 600\\text{ kBq}$ và chu kì bán rã là $T = 10\\text{ ngày}$. Sau thời gian $t = 20\\text{ ngày}$, độ phóng xạ $H$ của nguồn đó bằng bao nhiêu $\\text{kBq}$?", ["150"], "Ta có $\\dfrac{t}{T} = \\dfrac{20}{10} = 2$. Độ phóng xạ còn lại là $H = H_0 \\cdot 2^{-2} = \\dfrac{600}{4} = 150\\text{ kBq}$.", unit="kBq"),
        ],
    ),
]


from game_mapper import resolve_backend_game as _resolve_bg
for _l in LESSONS:
    _gt, _gtitle, _gdesc = _resolve_bg("physics", 12, _l)
    _l["game_type"] = _gt
    _l["game_title"] = _gtitle
    _l["game_description"] = _gdesc
