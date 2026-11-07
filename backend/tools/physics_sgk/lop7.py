"""Vật lý Lớp 7 (KHTN 7 - Kết nối tri thức với cuộc sống): 4 Chương - 14 Bài học độc lập."""
from ._helpers import F, G, bai, mcq, short, tf4

GRADE = 7

CH1_TOPIC = "l7-ch01-toc-do"
CH1_TITLE = "Chương I: Tốc độ"
CH1_DESC = "Chương I · Vật lý 7 (KHTN 7): Tốc độ chuyển động, đồ thị quãng đường – thời gian, đo tốc độ và an toàn giao thông."

CH2_TOPIC = "l7-ch02-am-thanh"
CH2_TITLE = "Chương II: Âm thanh"
CH2_DESC = "Chương II · Vật lý 7 (KHTN 7): Mô tả sóng âm, độ to – độ cao của âm, phản xạ âm và chống ô nhiễm tiếng ồn."

CH3_TOPIC = "l7-ch03-anh-sang"
CH3_TITLE = "Chương III: Ánh sáng"
CH3_DESC = "Chương III · Vật lý 7 (KHTN 7): Sự truyền thẳng của ánh sáng, định luật phản xạ ánh sáng và ảnh qua gương phẳng."

CH4_TOPIC = "l7-ch04-tu-truong"
CH4_TITLE = "Chương IV: Từ"
CH4_DESC = "Chương IV · Vật lý 7 (KHTN 7): Nam châm, từ trường, từ trường Trái Đất – la bàn và nam châm điện."

LESSONS = [
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 1: Tốc độ chuyển động",
        icon="🏃",
        description="Ý nghĩa vật lí của tốc độ, công thức tính tốc độ v = s/t và quy đổi đơn vị m/s sang km/h.",
        requirements=[
            "Nêu được ý nghĩa vật lí của tốc độ là đại lượng cho biết mức độ nhanh hay chậm của chuyển động.",
            "Viết và vận dụng được công thức tính tốc độ $v = \\dfrac{s}{t}$, tính quãng đường $s = v \\cdot t$ và thời gian $t = \\dfrac{s}{v}$.",
            "Đổi được đơn vị tốc độ giữa $\\text{m/s}$ và $\\text{km/h}$ theo hệ thức $1\\text{ m/s} = 3{,}6\\text{ km/h}$.",
        ],
        definition="Tốc độ chuyển động cho biết mức độ nhanh hay chậm của chuyển động, được xác định bằng độ dài quãng đường đi được trong một đơn vị thời gian: $v = \\dfrac{s}{t}$.",
        theory=(
            "### 1. Công thức tính tốc độ\n"
            "- Gọi $s$ là quãng đường đi được, $t$ là thời gian đi hết quãng đường đó, thì tốc độ chuyển động là:\n"
            "  $$v = \\dfrac{s}{t}$$\n"
            "- Từ đó suy ra: quãng đường $s = v \\cdot t$ và thời gian $t = \\dfrac{s}{v}$.\n\n"
            "### 2. Đơn vị đo tốc độ\n"
            "- Trong hệ SI, đơn vị của quãng đường là mét ($\\text{m}$), thời gian là giây ($\\text{s}$), nên đơn vị hợp pháp của tốc độ là **mét trên giây** ($\\text{m/s}$).\n"
            "- Trong giao thông thường dùng **kilômét trên giờ** ($\\text{km/h}$): $1\\text{ m/s} = 3{,}6\\text{ km/h}$ và $1\\text{ km/h} = \\dfrac{1}{3{,}6}\\text{ m/s}$."
        ),
        formulas=[
            G(
                "Công thức tính tốc độ và đổi đơn vị",
                F("Công thức tính tốc độ", "$v = \\dfrac{s}{t} \\implies s = v \\cdot t; \\quad t = \\dfrac{s}{v}$", "Trong đó $s$ là quãng đường ($\\text{m}$ hoặc $\\text{km}$), $t$ là thời gian ($\\text{s}$ hoặc $\\text{h}$)."),
                F("Quy đổi đơn vị tốc độ", "$1\\text{ m/s} = 3{,}6\\text{ km/h}$", "Đổi từ $\\text{m/s}$ sang $\\text{km/h}$ ta nhân với $3{,}6$; đổi từ $\\text{km/h}$ sang $\\text{m/s}$ ta chia cho $3{,}6$."),
            )
        ],
        example="Một vận động viên chạy bộ vượt qua quãng đường $s = 100\\text{ m}$ trong thời gian $t = 10\\text{ s}$. Hãy tính tốc độ của vận động viên theo đơn vị $\\text{m/s}$ và $\\text{km/h}$.",
        example_answer="Tốc độ của vận động viên là $v = \\dfrac{s}{t} = \\dfrac{100}{10} = 10\\text{ m/s}$. Đổi sang $\\text{km/h}$: $v = 10 \\cdot 3{,}6 = 36\\text{ km/h}$.",
        real_life="Đồng hồ tốc độ (tốc kế) trên xe máy và ô tô hiển thị tốc độ tức thời của xe theo đơn vị $\\text{km/h}$ giúp người lái kiểm soát tốc độ an toàn.",
        quiz=[
            mcq("biet", "Công thức tính tốc độ chuyển động $v$ theo quãng đường đi được $s$ và thời gian $t$ là gì?", ["$v = \\dfrac{s}{t}$", "$v = s \\cdot t$", "$v = \\dfrac{t}{s}$", "$v = s + t$"], 0, "Tốc độ bằng quãng đường đi được chia cho thời gian đi hết quãng đường đó: $v = \\dfrac{s}{t}$."),
            mcq("biet", "Đơn vị đo tốc độ trong hệ SI là gì?", ["$\\text{m/s}$", "$\\text{m}\\cdot\\text{s}$", "$\\text{s/m}$", "$\\text{kg/m}^3$"], 0, "Trong hệ SI, quãng đường tính bằng $\\text{m}$, thời gian tính bằng $\\text{s}$ nên tốc độ có đơn vị $\\text{m/s}$."),
            mcq("hieu", "Một ô tô chuyển động với tốc độ $54\\text{ km/h}$. Tốc độ này bằng bao nhiêu $\\text{m/s}$?", ["$15\\text{ m/s}$", "$20\\text{ m/s}$", "$5{,}4\\text{ m/s}$", "$194{,}4\\text{ m/s}$"], 0, "Đổi từ $\\text{km/h}$ sang $\\text{m/s}$ ta chia cho $3{,}6$: $v = \\dfrac{54}{3{,}6} = 15\\text{ m/s}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tốc độ chuyển động:", [
                "Trong cùng một thời gian, vật nào đi được quãng đường dài hơn thì có tốc độ lớn hơn.",
                "Đổi đơn vị: $10\\text{ m/s} = 36\\text{ km/h}$.",
                "Một người đi xe đạp với tốc độ $12\\text{ km/h}$ trong $0{,}5\\text{ h}$ sẽ đi được quãng đường $24\\text{ km}$.",
                "Khi đi trên cùng một quãng đường, vật chuyển động với tốc độ lớn hơn sẽ mất ít thời gian hơn.",
            ], [True, True, False, True], "Ý c) sai vì quãng đường đi được là $s = v \\cdot t = 12 \\cdot 0{,}5 = 6\\text{ km}$."),
            short("vandung", "Một người đi xe máy đi hết quãng đường $45\\text{ km}$ trong thời gian $1{,}5\\text{ giờ}$. Tốc độ của xe máy bằng bao nhiêu $\\text{km/h}$?", ["30"], "Áp dụng công thức $v = \\dfrac{s}{t} = \\dfrac{45}{1{,}5} = 30\\text{ km/h}$.", unit="km/h"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 2: Đồ thị quãng đường – thời gian",
        icon="📈",
        description="Cách lập bảng ghi dữ liệu, vẽ đồ thị quãng đường – thời gian (s – t) và tìm tốc độ từ đồ thị.",
        requirements=[
            "Vẽ được đồ thị quãng đường – thời gian ($s - t$) cho chuyển động thẳng có tốc độ không đổi từ bảng số liệu.",
            "Nhận biết được đường biểu diễn $s - t$ khi vật chuyển động với tốc độ không đổi là đường thẳng xiên góc, còn khi vật đứng yên là đường thẳng song song với trục thời gian $Ot$.",
            "Tính được tốc độ chuyển động của vật từ đồ thị quãng đường – thời gian.",
        ],
        definition="Đồ thị quãng đường – thời gian ($s - t$) mô tả mối liên hệ giữa quãng đường đi được $s$ (trục tung) và thời gian chuyển động $t$ (trục hoành) của một vật.",
        theory=(
            "### 1. Hình dạng đồ thị quãng đường – thời gian\n"
            "- Hệ trục tọa độ vuông góc gồm trục hoành $Ot$ biểu diễn thời gian $t$ và trục tung $Os$ biểu diễn quãng đường $s$.\n"
            "- Khi vật **chuyển động với tốc độ không đổi**, đồ thị $s - t$ là một **đoạn thẳng nằm nghiêng (xiên góc)**.\n"
            "- Khi vật **đứng yên** (quãng đường $s$ không tăng thêm khi thời gian $t$ trôi đi), đồ thị $s - t$ là một **đoạn thẳng nằm ngang song song với trục thời gian $Ot$**.\n\n"
            "### 2. Tìm tốc độ từ đồ thị\n"
            "- Trên đoạn thẳng biểu diễn giai đoạn chuyển động từ điểm $(t_1, s_1)$ đến $(t_2, s_2)$, tốc độ của vật là: $v = \\dfrac{s_2 - s_1}{t_2 - t_1}$."
        ),
        formulas=[
            G(
                "Xác định tốc độ trên đồ thị s - t",
                F("Tốc độ khi đồ thị đi qua gốc tọa độ O(0, 0)", "$v = \\dfrac{s}{t}$", "Đường biểu diễn càng dốc (hợp với trục $Ot$ góc càng lớn) thì tốc độ $v$ càng lớn."),
                F("Tốc độ trên một giai đoạn từ t₁ đến t₂", "$v = \\dfrac{\\Delta s}{\\Delta t} = \\dfrac{s_2 - s_1}{t_2 - t_1}$", "Nếu $s_2 = s_1$ (đoạn nằm ngang song song $Ot$) thì $v = 0$ (vật đứng yên)."),
            )
        ],
        example="Trên đồ thị quãng đường – thời gian của một ca nô xuất phát từ gốc tọa độ $O(0; 0)$, tại thời điểm $t = 2\\text{ h}$ ca nô đi được quãng đường $s = 50\\text{ km}$. Hãy xác định tốc độ của ca nô.",
        example_answer="Từ đồ thị $s - t$, tốc độ của ca nô là $v = \\dfrac{s}{t} = \\dfrac{50}{2} = 25\\text{ km/h}$.",
        real_life="Trong ngành điều hành đường sắt và hàng hải, biểu đồ hành trình $s - t$ được dùng để theo dõi vị trí các đoàn tàu và tránh xung đột trên cùng tuyến đường ray.",
        quiz=[
            mcq("biet", "Trên đồ thị quãng đường – thời gian ($s - t$), nếu đoạn thẳng biểu diễn nằm ngang song song với trục thời gian $Ot$ thì vật đang ở trạng thái nào?", ["Vật đang đứng yên", "Vật đang chuyển động nhanh dần", "Vật đang chuyển động với tốc độ rất lớn", "Vật đang quay tròn"], 0, "Đoạn thẳng song song với trục $Ot$ nghĩa là thời gian tăng nhưng quãng đường $s$ không đổi, tức vật đang đứng yên ($v = 0$)."),
            mcq("biet", "Khi vật chuyển động thẳng với tốc độ không đổi xuất phát từ gốc tọa độ, đồ thị quãng đường – thời gian ($s - t$) có dạng gì?", ["Một đường thẳng đi qua gốc tọa độ $O$", "Một đường tròn tâm $O$", "Một đường thẳng vuông góc với trục thời gian", "Một đường gấp khúc lên xuống ngẫu nhiên"], 0, "Vì $s = v \\cdot t$ với $v$ không đổi nên đồ thị $s - t$ là đường thẳng đi qua gốc tọa độ $O$."),
            mcq("hieu", "Trên cùng một hệ trục tọa độ $s - t$, đường biểu diễn của xe $A$ dốc hơn (tạo với trục $Ot$ góc lớn hơn) so với đường biểu diễn của xe $B$. Nhận xét nào sau đây là đúng?", ["Tốc độ của xe $A$ lớn hơn tốc độ của xe $B$", "Tốc độ của xe $A$ nhỏ hơn tốc độ của xe $B$", "Hai xe có cùng tốc độ", "Xe $A$ đang đứng yên còn xe $B$ chuyển động"], 0, "Trong cùng một khoảng thời gian $t$, đường nào dốc hơn thì ứng với quãng đường $s$ lớn hơn nên có tốc độ lớn hơn."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về đồ thị quãng đường – thời gian:", [
                "Trục hoành $Ot$ dùng để biểu diễn thời gian và trục tung $Os$ dùng để biểu diễn quãng đường.",
                "Từ đồ thị $s - t$, ta có thể tìm được cả quãng đường đi được, thời gian đi và tốc độ của vật.",
                "Nếu từ $t_1 = 1\\text{ h}$ đến $t_2 = 2\\text{ h}$ quãng đường giữ nguyên ở $s = 30\\text{ km}$ thì trong khoảng thời gian đó vật chuyển động với tốc độ $30\\text{ km/h}$.",
                "Nếu đồ thị đi qua điểm $(t = 3\\text{ s}; s = 12\\text{ m})$ kể từ gốc $O(0;0)$ thì tốc độ của vật là $4\\text{ m/s}$.",
            ], [True, True, False, True], "Ý c) sai vì từ $t_1 = 1\\text{ h}$ đến $t_2 = 2\\text{ h}$ quãng đường không đổi ($s_2 - s_1 = 0$) nên vật đang đứng yên ($v = 0$)."),
            short("vandung", "Đồ thị quãng đường – thời gian của một người đi xe đạp là một đường thẳng đi qua gốc tọa độ $O(0; 0)$ và điểm $M(t = 2\\text{ h}; s = 28\\text{ km})$. Tốc độ của người đi xe đạp bằng bao nhiêu $\\text{km/h}$?", ["14"], "Từ tọa độ điểm $M$ trên đồ thị, tốc độ là $v = \\dfrac{s}{t} = \\dfrac{28}{2} = 14\\text{ km/h}$.", unit="km/h"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 3: Đo tốc độ",
        icon="⏱️",
        description="Hai phương pháp đo tốc độ trong phòng thí nghiệm: dùng đồng hồ bấm giây và dùng cổng quang điện.",
        requirements=[
            "Trình bày được cách đo tốc độ bằng thước và đồng hồ bấm giây trong phòng thực hành.",
            "Trình bày được cách đo tốc độ bằng cổng quang điện kết nối với đồng hồ đo thời gian hiện số.",
            "Tính được tốc độ chuyển động từ số liệu thực nghiệm và so sánh ưu nhược điểm của hai phương pháp đo.",
        ],
        definition="Để đo tốc độ của một vật chuyển động trong phòng thí nghiệm, ta đo độ dài quãng đường $s$ (hoặc đường kính tấm chắn sáng $d$) và khoảng thời gian $t$ vật đi hết quãng đường đó, rồi tính $v = \\dfrac{s}{t}$.",
        theory=(
            "### 1. Đo tốc độ bằng đồng hồ bấm giây\n"
            "- Dùng thước đo khoảng cách $s$ giữa vạch xuất phát $A$ và vạch đích $B$.\n"
            "- Dùng đồng hồ bấm giây đo thời gian $t$ từ lúc vật qua vạch $A$ đến lúc qua vạch $B$, lấy trung bình $t = \\dfrac{t_1 + t_2 + t_3}{3}$, rồi tính $v = \\dfrac{s}{t}$.\n\n"
            "### 2. Đo tốc độ bằng cổng quang điện\n"
            "- **Cổng quang điện** phát ra một tia hồng ngoại chiếu sang bộ thu; khi vật (hoặc tấm cản quang có chiều rộng $d$) đi qua làm chắn tia sáng, đồng hồ đo thời gian hiện số tự động ghi lại thời gian chắn sáng $t$.\n"
            "- Ưu điểm của cổng quang điện là không phụ thuộc phản xạ bấm tay của người đo nên có độ chính xác rất cao."
        ),
        formulas=[
            G(
                "Công thức thực hành đo tốc độ",
                F("Đo tốc độ trên quãng đường giữa 2 cổng quang A và B", "$v = \\dfrac{s_{AB}}{t_{AB}}$", "Chế độ $A \\leftrightarrow B$ trên đồng hồ hiện số đo thời gian vật đi từ cổng quang $A$ đến cổng quang $B$."),
                F("Đo tốc độ tức thời qua 1 cổng quang điện", "$v = \\dfrac{d}{\\Delta t}$", "Trong đó $d$ là độ rộng tấm chắn sáng gắn trên xe lăn, $\\Delta t$ là thời gian tấm chắn đi qua cổng quang."),
            )
        ],
        example="Trong thí nghiệm đo tốc độ bằng hai cổng quang điện đặt cách nhau một khoảng $s = 0{,}6\\text{ m}$, đồng hồ đo thời gian hiện số chỉ thời gian viên bi lăn từ cổng quang thứ nhất đến cổng quang thứ hai là $t = 0{,}4\\text{ s}$. Tính tốc độ của viên bi.",
        example_answer="Tốc độ của viên bi trên đoạn đường giữa hai cổng quang điện là $v = \\dfrac{s}{t} = \\dfrac{0{,}6}{0{,}4} = 1{,}5\\text{ m/s}$.",
        real_life="Súng bắn tốc độ của cảnh sát giao thông và camera giám sát tốc độ trên đường cao tốc xác định chính xác tốc độ các phương tiện trong thời gian cực ngắn.",
        quiz=[
            mcq("biet", "Để đo tốc độ của một vật chuyển động trong phòng thí nghiệm, hai đại lượng cơ bản cần đo trực tiếp là gì?", ["Quãng đường đi được $s$ và thời gian chuyển động $t$", "Khối lượng $m$ và nhiệt độ $T$", "Trọng lượng $P$ và thể tích $V$", "Chiều dài $l$ và khối lượng $m$"], 0, "Vì $v = \\dfrac{s}{t}$ nên cần đo quãng đường $s$ bằng thước và thời gian $t$ bằng đồng hồ."),
            mcq("biet", "Ưu điểm nổi bật của việc dùng cổng quang điện kết nối với đồng hồ đo thời gian hiện số so với đồng hồ bấm giây cầm tay là gì?", ["Đo thời gian tự động bằng tia hồng ngoại nên giảm sai số do phản xạ của người bấm", "Không cần dùng nguồn điện", "Có thể đo được khối lượng của xe lăn", "Không cần đo khoảng cách"], 0, "Cổng quang điện tự động bật/tắt bộ đếm khi vật chắn tia sáng nên loại bỏ được độ trễ phản xạ tay của người đo."),
            mcq("hieu", "Một tấm chắn sáng có chiều rộng $d = 2\\text{ cm} = 0{,}02\\text{ m}$ gắn trên xe lăn đi qua một cổng quang điện mất thời gian $\\Delta t = 0{,}05\\text{ s}$. Tốc độ của xe lăn khi qua cổng quang là bao nhiêu?", ["$0{,}4\\text{ m/s}$", "$2{,}5\\text{ m/s}$", "$0{,}1\\text{ m/s}$", "$4\\text{ m/s}$"], 0, "Ta có $v = \\dfrac{d}{\\Delta t} = \\dfrac{0{,}02}{0{,}05} = 0{,}4\\text{ m/s}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu về thực hành đo tốc độ:", [
                "Khi đo bằng đồng hồ bấm giây, người ta thường đo $3$ lần rồi lấy giá trị trung bình để giảm sai số ngẫu nhiên.",
                "Trong thí nghiệm với hai cổng quang điện $A$ và $B$, đồng hồ hiện số ở chế độ $A \\leftrightarrow B$ cho biết thời gian vật đi từ cổng $A$ đến cổng $B$.",
                "Súng bắn tốc độ của cảnh sát giao thông đo thời gian bằng thước dây cơ học.",
                "Nếu khoảng cách giữa hai cổng quang là $0{,}8\\text{ m}$ và thời gian đo được là $0{,}5\\text{ s}$ thì tốc độ vật là $1{,}6\\text{ m/s}$.",
            ], [True, True, False, True], "Ý c) sai vì súng bắn tốc độ sử dụng sóng điện từ hoặc tia laser phản xạ để tính tốc độ tức thời."),
            short("vandung", "Hai cổng quang điện đặt cách nhau $s = 0{,}9\\text{ m}$. Thời gian xe lăn đi từ cổng quang thứ nhất đến cổng quang thứ hai hiển thị trên đồng hồ hiện số là $t = 0{,}6\\text{ s}$. Tốc độ của xe lăn bằng bao nhiêu $\\text{m/s}$?", ["1,5", "1.5"], "Ta có $v = \\dfrac{s}{t} = \\dfrac{0{,}9}{0{,}6} = 1{,}5\\text{ m/s}$.", unit="m/s"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH1_TOPIC,
        chapter_title=CH1_TITLE,
        title="Bài 4: Tốc độ và an toàn giao thông",
        icon="🚦",
        description="Ảnh hưởng của tốc độ đến an toàn giao thông, biển báo tốc độ tối đa và quy tắc 3 giây tính khoảng cách an toàn.",
        requirements=[
            "Giải thích được vì sao phải quy định tốc độ giới hạn đối với các phương tiện khác nhau và trên các cung đường khác nhau.",
            "Hiểu và vận dụng được quy tắc '3 giây' để ước tính khoảng cách an toàn tối thiểu: $d = v(\\text{m/s}) \\cdot 3\\text{ s}$.",
            "Đọc được các biển báo tốc độ tối đa, biển báo khoảng cách tối thiểu và điều chỉnh khoảng cách khi trời mưa, đường trơn.",
        ],
        definition="Khoảng cách an toàn tối thiểu giữa hai xe chạy liên tiếp trên cùng một làn đường giúp người lái xe phía sau kịp thời xử lí và phanh xe không va chạm khi xe phía trước dừng đột ngột. Theo quy tắc '3 giây', khoảng cách an toàn tối thiểu là $d = v \\cdot 3$ (với $v$ tính bằng $\\text{m/s}$).",
        theory=(
            "### 1. Tốc độ giới hạn và va chạm giao thông\n"
            "- Khi tốc độ càng lớn, quãng đường xe đi thêm trong thời gian phản ứng của người lái và quãng đường trượt khi phanh càng dài, đồng thời năng lượng va chạm càng lớn.\n"
            "- Khi trời mưa, sương mù hoặc mặt đường trơn trượt, lực ma sát giảm nên người lái xe phải **giảm tốc độ** và **tăng khoảng cách an toàn**.\n\n"
            "### 2. Quy tắc '3 giây' trên đường cao tốc\n"
            "- Khoảng thời gian an toàn tối thiểu từ lúc xe trước đi qua một mốc cố định đến lúc xe sau đi tới mốc đó là $t = 3\\text{ s}$.\n"
            "- Công thức tính khoảng cách an toàn theo quy tắc '3 giây': $d(\\text{m}) = v(\\text{m/s}) \\cdot 3(\\text{s})$."
        ),
        formulas=[
            G(
                "Khoảng cách an toàn theo quy tắc 3 giây",
                F("Công thức quy tắc 3 giây", "$d_{\\min} = v \\cdot 3$", "Trong đó $v$ là tốc độ của xe đổi ra đơn vị $\\text{m/s}$, $d_{\\min}$ là khoảng cách an toàn tối thiểu ($\\text{m}$)."),
                F("Tính nhanh từ tốc độ km/h", "$d_{\\min} = \\dfrac{v(\\text{km/h})}{3{,}6} \\cdot 3 = \\dfrac{5}{6} v(\\text{km/h})$", "Ví dụ: khi chạy ở tốc độ $72\\text{ km/h} = 20\\text{ m/s}$, khoảng cách an toàn theo quy tắc 3 giây là $d = 20 \\cdot 3 = 60\\text{ m}$."),
            )
        ],
        example="Một ô tô đang chạy trên đường cao tốc với tốc độ $v = 90\\text{ km/h}$. Áp dụng quy tắc '3 giây', hãy tính khoảng cách an toàn tối thiểu mà người lái xe phải giữ đối với xe chạy liền trước.",
        example_answer="Đổi tốc độ ra $\\text{m/s}$: $v = \\dfrac{90}{3{,}6} = 25\\text{ m/s}$. Theo quy tắc '3 giây', khoảng cách an toàn tối thiểu là $d = 25 \\cdot 3 = 75\\text{ m}$.",
        real_life="Trên các tuyến cao tốc ở Việt Nam đều cắm các biển báo cự li $0\\text{ m} - 50\\text{ m} - 100\\text{ m}$ bên lề đường để tài xế tự căn khoảng cách an toàn với xe phía trước.",
        quiz=[
            mcq("biet", "Theo quy tắc '3 giây' trên đường cao tốc, công thức tính khoảng cách an toàn tối thiểu $d(\\text{m})$ theo tốc độ $v(\\text{m/s})$ của xe là gì?", ["$d = 3v$", "$d = \\dfrac{v}{3}$", "$d = v + 3$", "$d = 3{,}6v$"], 0, "Theo quy tắc '3 giây', khoảng cách an toàn tối thiểu bằng tốc độ ($\\text{m/s}$) nhân với $3\\text{ s}$: $d = 3v$."),
            mcq("biet", "Khi trời mưa to làm mặt đường ướt và trơn trượt, người điều khiển phương tiện giao thông cần làm gì để đảm bảo an toàn?", ["Giảm tốc độ và tăng khoảng cách an toàn với xe phía trước", "Tăng tốc độ để đi qua vùng mưa thật nhanh", "Giữ nguyên tốc độ tối đa và bám sát đuôi xe phía trước", "Tắt toàn bộ đèn chiếu sáng của xe"], 0, "Khi đường trơn, ma sát giảm làm quãng đường phanh dài hơn, nên phải giảm tốc độ và giữ khoảng cách xa hơn."),
            mcq("hieu", "Một ô tô đang chạy với tốc độ $v = 72\\text{ km/h}$. Theo quy tắc '3 giây', khoảng cách an toàn tối thiểu với xe phía trước là bao nhiêu mét?", ["$60\\text{ m}$", "$216\\text{ m}$", "$20\\text{ m}$", "$72\\text{ m}$"], 0, "Đổi $v = 72\\text{ km/h} = 20\\text{ m/s}$. Khoảng cách an toàn là $d = 20 \\cdot 3 = 60\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về tốc độ và an toàn giao thông:", [
                "Tốc độ lưu thông càng lớn thì khoảng cách an toàn tối thiểu giữa hai xe càng phải lớn.",
                "Biển báo hình tròn viền đỏ ghi số '60' trên nền trắng quy định tốc độ tối đa cho phép là $60\\text{ km/h}$.",
                "Khoảng cách an toàn tối thiểu không phụ thuộc vào tốc độ của xe.",
                "Khi xe chạy với tốc độ $15\\text{ m/s}$ ($54\\text{ km/h}$), khoảng cách an toàn theo quy tắc '3 giây' là $45\\text{ m}$.",
            ], [True, True, False, True], "Ý c) sai vì tốc độ càng cao thì khoảng cách an toàn tối thiểu càng lớn."),
            short("vandung", "Một xe khách chạy trên cao tốc với tốc độ $108\\text{ km/h}$ (tương ứng $30\\text{ m/s}$). Theo quy tắc '3 giây', khoảng cách an toàn tối thiểu giữa xe khách và xe chạy liền trước bằng bao nhiêu mét ($\\text{m}$)?", ["90"], "Áp dụng quy tắc '3 giây': $d = v \\cdot 3 = 30 \\cdot 3 = 90\\text{ m}$.", unit="m"),
        ],
        chapter_desc=CH1_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 5: Mô tả sóng âm",
        icon="🔊",
        description="Nguồn âm, dao động âm, sự truyền sóng âm trong các môi trường rắn, lỏng, khí và so sánh tốc độ truyền âm.",
        requirements=[
            "Nêu được nguồn âm là các vật phát ra âm thanh và các nguồn âm đều dao động.",
            "Giải thích được sóng âm là sự lan truyền dao động của nguồn âm trong môi trường đàn hồi (rắn, lỏng, khí).",
            "So sánh được tốc độ truyền âm trong các môi trường ($v_{\\text{rắn}} > v_{\\text{lỏng}} > v_{\\text{khí}}$) và khẳng định sóng âm không truyền được trong chân không.",
        ],
        definition="Vật phát ra âm được gọi là nguồn âm; khi phát ra âm, các nguồn âm đều dao động. Sóng âm là sự lan truyền dao động âm trong các môi trường chất rắn, chất lỏng và chất khí (sóng âm không truyền được trong chân không).",
        theory=(
            "### 1. Nguồn âm và sóng âm\n"
            "- **Dao động** là sự chuyển động qua lại quanh một vị trí cân bằng (như dây đàn rung, mặt trống rung, nhánh âm thoa rung).\n"
            "- Dao động từ nguồn âm làm lớp môi trường tiếp xúc bị nén – dãn luân phiên và lan truyền ra xa tạo thành **sóng âm**.\n\n"
            "### 2. Môi trường truyền âm và tốc độ truyền âm\n"
            "- Sóng âm truyền được trong các môi trường **rắn, lỏng, khí**, nhưng **không truyền được trong chân không**.\n"
            "- Tốc độ truyền âm trong chất rắn lớn hơn trong chất lỏng, và trong chất lỏng lớn hơn trong chất khí:\n"
            "  $$v_{\\text{rắn}} > v_{\\text{lỏng}} > v_{\\text{khí}}$$\n"
            "- Ví dụ ở $20^\\circ\\text{C}$: trong không khí $v \\approx 340\\text{ m/s}$, trong nước $v \\approx 1500\\text{ m/s}$, trong thép $v \\approx 6100\\text{ m/s}$."
        ),
        formulas=[
            G(
                "Sự truyền sóng âm trong các môi trường",
                F("So sánh tốc độ truyền âm", "$v_{\\text{rắn}} > v_{\\text{lỏng}} > v_{\\text{khí}} \\quad (v_{\\text{chân không}} = 0)$", "Sóng âm không truyền được trong chân không vì chân không không có các hạt vật chất để truyền dao động."),
                F("Quãng đường truyền âm trong thời gian t", "$s = v_{\\text{âm}} \\cdot t$", "Trong không khí ở điều kiện thường, tốc độ truyền âm khoảng $v_{\\text{khí}} \\approx 340\\text{ m/s}$."),
            )
        ],
        example="Trong một cơn giông, một người nhìn thấy tia chớp lóe sáng và sau đó $t = 3\\text{ s}$ mới nghe thấy tiếng sấm nổ. Biết tốc độ truyền âm trong không khí là $v = 340\\text{ m/s}$ (coi ánh sáng truyền đi tức thời). Hỏi nơi sét đánh cách người đó bao nhiêu mét?",
        example_answer="Khoảng cách từ nơi sét đánh đến người quan sát bằng quãng đường âm thanh truyền đi trong $3\\text{ s}$: $s = v \\cdot t = 340 \\cdot 3 = 1020\\text{ m}$.",
        real_life="Ngày xưa, để phát hiện tiếng vó ngựa từ rất xa, các kị binh thường áp tai xuống mặt đất vì mặt đất (chất rắn) truyền âm nhanh và tốt hơn không khí.",
        quiz=[
            mcq("biet", "Đặc điểm chung của mọi nguồn âm khi đang phát ra âm thanh là gì?", ["Các bộ phận của nguồn âm đều đang dao động", "Các nguồn âm đều đang nóng chảy", "Các nguồn âm đều nhiễm điện dương", "Các nguồn âm đều chuyển động thẳng đều"], 0, "Mọi nguồn âm khi phát ra âm thanh đều dao động quanh vị trí cân bằng."),
            mcq("biet", "Sóng âm **không** thể truyền được trong môi trường nào sau đây?", ["Chân không", "Không khí", "Nước biển", "Thanh sắt"], 0, "Sóng âm cần môi trường vật chất đàn hồi (rắn, lỏng, khí) để truyền dao động, nên không truyền được trong chân không."),
            mcq("hieu", "Khi so sánh tốc độ truyền âm trong không khí ($v_1$), trong nước ($v_2$) và trong thanh thép ($v_3$), thứ tự nào sau đây là đúng?", ["$v_3 > v_2 > v_1$", "$v_1 > v_2 > v_3$", "$v_2 > v_3 > v_1$", "$v_1 = v_2 = v_3$"], 0, "Tốc độ truyền âm trong chất rắn (thép $v_3$) lớn hơn chất lỏng (nước $v_2$) và lớn hơn chất khí (không khí $v_1$)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sóng âm:", [
                "Khi gảy dây đàn ghi-ta, dây đàn dao động phát ra âm thanh.",
                "Trên Mặt Trăng không có khí quyển (coi như chân không) nên hai nhà du hành vũ trụ đứng gần nhau không thể nói chuyện trực tiếp qua không gian mà phải dùng bộ đàm sóng vô tuyến.",
                "Khi thổi sáo, bộ phận dao động chính phát ra âm thanh là cột không khí bên trong ống sáo.",
                "Tốc độ truyền âm trong không khí lớn hơn tốc độ truyền âm trong đường ray bằng thép.",
            ], [True, True, True, False], "Ý d) sai vì thép là chất rắn nên truyền âm nhanh gấp khoảng $18$ lần so với không khí."),
            short("vandung", "Biết tốc độ truyền âm trong không khí là $340\\text{ m/s}$. Trong khoảng thời gian $t = 2\\text{ s}$, sóng âm truyền đi được quãng đường bao nhiêu mét ($\\text{m}$) trong không khí?", ["680"], "Quãng đường âm truyền đi được là $s = v \\cdot t = 340 \\cdot 2 = 680\\text{ m}$.", unit="m"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 6: Độ to và độ cao của âm",
        icon="🎵",
        description="Liên hệ giữa biên độ dao động với độ to của âm (dB) và giữa tần số dao động f = N/t (Hz) với độ cao của âm.",
        requirements=[
            "Nêu được biên độ dao động là độ lệch lớn nhất của vật dao động so với vị trí cân bằng; biên độ càng lớn thì âm nghe càng to.",
            "Định nghĩa được tần số là số dao động trong $1\\text{ giây}$ ($f = \\dfrac{N}{t}$, đơn vị Hertz – $\\text{Hz}$); tần số càng lớn thì âm nghe càng cao (càng bổng).",
            "Vận dụng được công thức $f = \\dfrac{N}{t}$ để tính tần số và so sánh độ cao của các âm.",
        ],
        definition="Biên độ dao động là độ lệch lớn nhất của vật dao động so với vị trí cân bằng (biên độ càng lớn thì âm càng to). Tần số là số dao động thực hiện được trong một giây: $f = \\dfrac{N}{t}$ (đơn vị $\\text{Hz}$); tần số càng lớn thì âm càng cao (bổng).",
        theory=(
            "### 1. Biên độ dao động và độ to của âm\n"
            "- **Biên độ dao động** là khoảng cách lớn nhất từ vị trí cân bằng đến vị trí biên khi vật dao động.\n"
            "- Âm phát ra càng **to** khi **biên độ dao động** của nguồn âm càng **lớn**.\n"
            "- Độ to của âm được đo bằng đơn vị **đêxiben** (kí hiệu $\\text{dB}$).\n\n"
            "### 2. Tần số dao động và độ cao của âm\n"
            "- **Tần số** ($f$) là số dao động trong $1\\text{ giây}$: $f = \\dfrac{N}{t}$, đơn vị là **Hertz** ($\\text{Hz}$).\n"
            "- Âm phát ra càng **cao (bổng)** khi **tần số dao động** càng **lớn**; âm càng **thấp (trầm)** khi **tần số dao động** càng **nhỏ**.\n"
            "- Tai người bình thường nghe được âm có tần số từ $20\\text{ Hz}$ đến $20\\,000\\text{ Hz}$."
        ),
        formulas=[
            G(
                "Tần số dao động và đặc trưng của âm",
                F("Công thức tính tần số dao động", "$f = \\dfrac{N}{t}$", "Trong đó $N$ là số dao động thực hiện được trong thời gian $t$ ($\\text{s}$), $f$ có đơn vị là Hertz ($\\text{Hz}$)."),
                F("Quan hệ đặc trưng vật lí và sinh lí của âm", "$\\text{Biên độ lớn} \\iff \\text{Âm to (dB)}; \\qquad \\text{Tần số } f \\text{ lớn} \\iff \\text{Âm cao/bổng (Hz)}$", "Ngưỡng nghe của tai người: $20\\text{ Hz} \\le f \\le 20\\,000\\text{ Hz}$."),
            )
        ],
        example="Trong thời gian $t = 2\\text{ s}$, cánh của một con ong mật thực hiện được $N_1 = 600$ dao động, còn cánh của một con muỗi thực hiện được $N_2 = 1200$ dao động. Hãy tính tần số dao động cánh của mỗi con vật và cho biết âm do con nào phát ra cao hơn.",
        example_answer="Tần số vỗ cánh của con ong là $f_1 = \\dfrac{600}{2} = 300\\text{ Hz}$. Tần số vỗ cánh của con muỗi là $f_2 = \\dfrac{1200}{2} = 600\\text{ Hz}$. Vì $f_2 > f_1$ nên âm do cánh muỗi phát ra cao (bổng) hơn âm của cánh ong.",
        real_life="Khi lên dây đàn ghi-ta, người nghệ sĩ vặn khóa đàn để làm căng dây hơn giúp dây dao động nhanh hơn (tần số $f$ lớn hơn) để phát ra nốt nhạc cao hơn.",
        quiz=[
            mcq("biet", "Độ to của âm phụ thuộc vào yếu tố nào của nguồn âm?", ["Biên độ dao động của nguồn âm", "Tần số dao động của nguồn âm", "Thời gian nguồn âm dao động", "Khối lượng riêng của không khí"], 0, "Biên độ dao động của nguồn âm càng lớn thì sóng âm có biên độ càng lớn và âm nghe được càng to."),
            mcq("biet", "Đơn vị của tần số dao động là gì?", ["Hertz ($\\text{Hz}$)", "Đêxiben ($\\text{dB}$)", "Mét trên giây ($\\text{m/s}$)", "Newton ($\\text{N}$)"], 0, "Tần số là số dao động trong $1\\text{ giây}$, có đơn vị là Hertz ($\\text{Hz}$)."),
            mcq("hieu", "Dây đàn thứ nhất dao động với tần số $f_1 = 220\\text{ Hz}$, dây đàn thứ hai dao động với tần số $f_2 = 440\\text{ Hz}$. So sánh độ cao của hai âm phát ra:", ["Âm do dây thứ hai phát ra cao (bổng) hơn âm do dây thứ nhất phát ra", "Âm do dây thứ nhất phát ra cao hơn âm do dây thứ hai phát ra", "Hai dây đàn phát ra âm có cùng độ cao", "Không so sánh được vì chưa biết biên độ"], 0, "Vì $f_2 = 440\\text{ Hz} > f_1 = 220\\text{ Hz}$ nên dây thứ hai phát ra âm cao hơn."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về độ to và độ cao của âm:", [
                "Khi gõ mạnh vào mặt trống, mặt trống dao động với biên độ lớn nên phát ra âm to.",
                "Tần số dao động càng nhỏ thì âm phát ra càng trầm (thấp).",
                "Đơn vị đo độ to của âm là Hertz ($\\text{Hz}$).",
                "Một vật thực hiện $100$ dao động trong $5\\text{ s}$ thì có tần số dao động là $20\\text{ Hz}$.",
            ], [True, True, False, True], "Ý c) sai vì đơn vị đo độ to của âm là đêxiben ($\\text{dB}$), còn Hertz ($\\text{Hz}$) là đơn vị đo tần số."),
            short("vandung", "Một lá thép mỏng thực hiện được $N = 450$ dao động trong thời gian $t = 3\\text{ giây}$. Tần số dao động $f$ của lá thép bằng bao nhiêu $\\text{Hz}$?", ["150"], "Áp dụng công thức $f = \\dfrac{N}{t} = \\dfrac{450}{3} = 150\\text{ Hz}$.", unit="Hz"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH2_TOPIC,
        chapter_title=CH2_TITLE,
        title="Bài 7: Phản xạ âm, chống ô nhiễm tiếng ồn",
        icon="🦇",
        description="Vật phản xạ âm tốt và kém, hiện tượng tiếng vang, công thức Sonar d = v.t/2 và các biện pháp chống ô nhiễm tiếng ồn.",
        requirements=[
            "Phân biệt được vật phản xạ âm tốt (cứng, nhẵn như tường gạch, mặt kính, tấm kim loại) và vật phản xạ âm kém (mềm, xốp, gồ ghề như nhung, dạ, cao su xốp).",
            "Giải thích được sự hình thành tiếng vang và vận dụng công thức $d = \\dfrac{v \\cdot t}{2}$ để tính khoảng cách từ nguồn âm đến vật cản hoặc độ sâu đáy biển.",
            "Đề xuất được các biện pháp chống ô nhiễm tiếng ồn trong trường học, bệnh viện và khu dân cư.",
        ],
        definition="Sóng âm khi gặp mặt chắn đều bị phản xạ nhiều hay ít. Tiếng vang là âm phản xạ nghe được cách biệt với âm trực tiếp (khi âm phản xạ truyền đến tai chậm hơn âm trực tiếp ít nhất $\\dfrac{1}{15}\\text{ s}$).",
        theory=(
            "### 1. Phản xạ âm và tiếng vang\n"
            "- **Vật phản xạ âm tốt**: các vật cứng, có bề mặt nhẵn (đá hoa cương, tường gạch phẳng, tấm sắt, mặt gương).\n"
            "- **Vật phản xạ âm kém (hấp thụ âm tốt)**: các vật mềm, xốp, có bề mặt gồ ghề (rèm nhung, thảm len, tấm xốp tiêu âm).\n"
            "- Khi sóng âm truyền từ nguồn đến vật cản ở khoảng cách $d$ rồi phản xạ trở lại nguồn mất tổng thời gian $t$, quãng đường âm đi được là $s = 2d = v \\cdot t \\implies d = \\dfrac{v \\cdot t}{2}$.\n\n"
            "### 2. Chống ô nhiễm tiếng ồn\n"
            "- **Tiếng ồn** là những âm thanh to, kéo dài gây ảnh hưởng xấu đến sức khỏe và hoạt động của con người.\n"
            "- Ba nhóm biện pháp giảm tiếng ồn: (1) tác động vào nguồn âm, (2) phân tán âm trên đường truyền (trồng cây xanh), (3) ngăn chặn đường truyền âm (lắp kính hai lớp, tường xốp cách âm)."
        ),
        formulas=[
            G(
                "Bài toán phản xạ âm và Sonar đo độ sâu",
                F("Khoảng cách từ nguồn âm đến bức tường hoặc đáy biển", "$d = \\dfrac{v \\cdot t}{2}$", "Vì sóng âm đi từ nguồn đến vật phản xạ rồi quay trở lại nguồn nên tổng quãng đường âm đi là $s = 2d$."),
                F("Khoảng cách tối thiểu để nghe được tiếng vang trong không khí", "$d_{\\min} = \\dfrac{340 \\cdot (1/15)}{2} \\approx 11{,}3\\text{ m}$", "Nếu đứng gần bức tường hơn $11{,}3\\text{ m}$, âm phản xạ hòa lẫn với âm trực tiếp làm âm nghe to hơn."),
            )
        ],
        example="Một tàu khảo sát dùng thiết bị Sonar phát một xung siêu âm thẳng đứng xuống đáy biển và thu được âm phản xạ sau thời gian $t = 1{,}2\\text{ s}$. Biết tốc độ truyền siêu âm trong nước biển là $v = 1500\\text{ m/s}$. Hãy tính độ sâu $d$ của đáy biển tại vị trí đó.",
        example_answer="Trong thời gian $t = 1{,}2\\text{ s}$, xung siêu âm truyền từ tàu xuống đáy biển rồi phản xạ ngược lên tàu nên đi được quãng đường $2d$. Độ sâu của đáy biển là $d = \\dfrac{v \\cdot t}{2} = \\dfrac{1500 \\cdot 1{,}2}{2} = 900\\text{ m}$.",
        real_life="Các rạp chiếu phim và phòng thu âm thường ốp tường bằng mút xốp hình gai nhọn và treo rèm nhung dày để hấp thụ âm, tránh tiếng vang dội lại.",
        quiz=[
            mcq("biet", "Vật nào sau đây phản xạ âm **kém** nhất (hấp thụ âm tốt nhất)?", ["Tấm xốp mềm và rèm nhung", "Mặt gương phẳng", "Tường gạch trát phẳng", "Tấm thép dày"], 0, "Các vật mềm, xốp, có bề mặt gồ ghề như mút xốp, rèm nhung phản xạ âm kém (hấp thụ âm tốt)."),
            mcq("biet", "Biện pháp nào sau đây giúp giảm tiếng ồn bằng cách **phân tán âm trên đường truyền**?", ["Trồng nhiều cây xanh xung quanh trường học và bệnh viện", "Cấm bóp còi gần bệnh viện", "Đeo nút bịt tai chống ồn", "Tắt loa phóng thanh"], 0, "Lá cây xanh phản xạ âm theo nhiều hướng khác nhau, giúp phân tán sóng âm trên đường truyền."),
            mcq("hieu", "Một người đứng trước một vách núi cao và hét to một tiếng, sau $2\\text{ s}$ người đó nghe thấy tiếng vang của mình. Biết tốc độ truyền âm trong không khí là $340\\text{ m/s}$, khoảng cách từ người đó đến vách núi là bao nhiêu?", ["$340\\text{ m}$", "$680\\text{ m}$", "$170\\text{ m}$", "$1020\\text{ m}$"], 0, "Âm đi từ người đến vách núi rồi dội lại nên $d = \\dfrac{v \\cdot t}{2} = \\dfrac{340 \\cdot 2}{2} = 340\\text{ m}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về phản xạ âm và chống ô nhiễm tiếng ồn:", [
                "Các vật cứng, có bề mặt nhẵn như mặt đá hoa cương phản xạ âm rất tốt.",
                "Tàu thủy dùng sóng siêu âm (Sonar) để đo độ sâu đáy biển dựa trên hiện tượng phản xạ âm.",
                "Treo biển báo 'Đi nhẹ, nói khẽ' trong bệnh viện là biện pháp tác động trực tiếp vào nguồn âm để giảm tiếng ồn.",
                "Khi sóng âm truyền đi gặp mặt chắn rồi phản xạ lại chỗ cũ sau thời gian $t$, khoảng cách đến mặt chắn là $d = v \\cdot t$.",
            ], [True, True, True, False], "Ý d) sai vì sóng âm phải đi cả lượt đi lẫn lượt về ($s = 2d$) nên khoảng cách đến mặt chắn là $d = \\dfrac{v \\cdot t}{2}$."),
            short("vandung", "Một tàu biển phát ra siêu âm xuống đáy biển và nhận lại tín hiệu phản xạ sau $t = 0{,}8\\text{ s}$. Biết tốc độ truyền siêu âm trong nước biển là $v = 1500\\text{ m/s}$. Độ sâu của đáy biển tại đó bằng bao nhiêu mét ($\\text{m}$)?", ["600"], "Áp dụng công thức $d = \\dfrac{v \\cdot t}{2} = \\dfrac{1500 \\cdot 0{,}8}{2} = 600\\text{ m}$.", unit="m"),
        ],
        chapter_desc=CH2_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 8: Ánh sáng, tia sáng",
        icon="🔦",
        description="Định luật truyền thẳng của ánh sáng, 3 loại chùm sáng, vùng tối – vùng nửa tối và hiện tượng nhật thực, nguyệt thực.",
        requirements=[
            "Phát biểu được định luật truyền thẳng của ánh sáng: trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường thẳng.",
            "Nhận biết và vẽ được tia sáng (đường thẳng có mũi tên chỉ hướng) và 3 loại chùm sáng: song song, hội tụ, phân kì.",
            "Giải thích được sự tạo thành vùng tối (bóng tối), vùng nửa tối (bóng nửa tối) và nguyên nhân hiện tượng nhật thực, nguyệt thực.",
        ],
        definition="Trong một môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường thẳng. Đường truyền của ánh sáng được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng gọi là tia sáng.",
        theory=(
            "### 1. Tia sáng và chùm sáng\n"
            "- **Tia sáng**: biểu diễn bằng một đường thẳng có mũi tên chỉ hướng truyền của ánh sáng.\n"
            "- **Ba loại chùm sáng**:\n"
            "  1. **Chùm sáng song song**: các tia sáng không giao nhau trên đường truyền.\n"
            "  2. **Chùm sáng hội tụ**: các tia sáng giao nhau tại một điểm trên đường truyền.\n"
            "  3. **Chùm sáng phân kì**: các tia sáng loe rộng ra từ một điểm nguồn.\n\n"
            "### 2. Vùng tối và vùng nửa tối\n"
            "- **Vùng tối**: nằm phía sau vật cản, hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới.\n"
            "- **Vùng nửa tối**: nằm phía sau vật cản, chỉ nhận được một phần ánh sáng từ nguồn sáng rộng truyền tới.\n"
            "- **Nhật thực** xảy ra ban ngày khi Mặt Trăng nằm giữa Mặt Trời và Trái Đất; **Nguyệt thực** xảy ra đêm rằm khi Trái Đất nằm giữa Mặt Trời và Mặt Trăng."
        ),
        formulas=[
            G(
                "Quy luật truyền thẳng ánh sáng và che khuất",
                F("Định luật truyền thẳng của ánh sáng", "$\\text{Môi trường trong suốt + đồng tính} \\implies \\text{Ánh sáng truyền theo đường thẳng}$", "Là cơ sở để ngắm thẳng khi xếp hàng, trồng cây thẳng hàng và tạo bóng của vật."),
                F("Thứ tự thiên thể khi xảy ra Nhật thực và Nguyệt thực", "$\\text{Nhật thực: Mặt Trời} - \\text{Mặt Trăng} - \\text{Trái Đất}; \\quad \\text{Nguyệt thực: Mặt Trời} - \\text{Trái Đất} - \\text{Mặt Trăng}$", "Ứng dụng trực tiếp sự tạo thành vùng tối và vùng nửa tối trong vũ trụ."),
            )
        ],
        example="Khi xếp hàng chào cờ trên sân trường, bạn đứng cuối hàng chỉ nhìn thấy gáy của bạn đứng ngay trước mình mà không nhìn thấy các bạn đứng đầu hàng. Hiện tượng đó chứng tỏ hàng đã thẳng chưa và dựa trên định luật vật lí nào?",
        example_answer="Hàng đã thẳng vì trong không khí trong suốt và đồng tính, ánh sáng truyền đi theo đường thẳng; bạn đứng ngay trước đã chắn các tia sáng đi thẳng từ các bạn phía trên truyền tới mắt bạn cuối hàng.",
        real_life="Đèn pha ô tô hoặc đèn pin chiếu xa tạo chùm sáng gần song song, trong khi kính lúp hứng ánh nắng Mặt Trời tạo ra chùm sáng hội tụ tại một điểm.",
        quiz=[
            mcq("biet", "Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường nào?", ["Theo đường thẳng", "Theo đường gấp khúc", "Theo đường tròn", "Theo đường xoắn ốc"], 0, "Theo định luật truyền thẳng của ánh sáng, trong môi trường trong suốt và đồng tính ánh sáng truyền đi theo đường thẳng."),
            mcq("biet", "Chùm sáng gồm các tia sáng không giao nhau trên đường truyền của chúng được gọi là chùm sáng gì?", ["Chùm sáng song song", "Chùm sáng hội tụ", "Chùm sáng phân kì", "Chùm sáng khúc xạ"], 0, "Các tia sáng không giao nhau trên đường truyền tạo thành chùm sáng song song."),
            mcq("hieu", "Vì sao trong phòng học và phòng mổ bệnh viện, người ta thường lắp nhiều bóng đèn dài hoặc hệ thống nhiều đèn thay vì chỉ lắp một bóng đèn nhỏ duy nhất?", ["Để xóa bỏ vùng tối (bóng đen) do đầu hoặc tay người che khuất khi viết bài hay phẫu thuật", "Để ánh sáng truyền đi theo đường cong", "Để làm giảm tốc độ truyền ánh sáng", "Để tạo ra vùng tối lớn hơn trên mặt bàn"], 0, "Nguồn sáng rộng hoặc nhiều đèn chiếu từ nhiều phía giúp ánh sáng vẫn rọi tới chỗ bị tay che khuất, tránh tạo vùng tối đậm trên trang vở."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự truyền ánh sáng:", [
                "Tia sáng được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng truyền của ánh sáng.",
                "Vùng tối phía sau vật cản là vùng hoàn toàn không nhận được ánh sáng từ nguồn sáng truyền tới.",
                "Hiện tượng nhật thực xảy ra khi Trái Đất đi vào vùng bóng tối của Mặt Trăng vào ban ngày.",
                "Chùm sáng phát ra từ một bóng đèn dây tóc nhỏ tỏa ra mọi phía là chùm sáng hội tụ.",
            ], [True, True, True, False], "Ý d) sai vì chùm sáng phát ra từ một nguồn điểm tỏa rộng ra xung quanh là chùm sáng phân kì."),
            short("vandung", "Có mấy loại chùm sáng cơ bản thường gặp (song song, hội tụ, phân kì)?", ["3"], "Có $3$ loại chùm sáng cơ bản: chùm sáng song song, chùm sáng hội tụ và chùm sáng phân kì."),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 9: Sự phản xạ ánh sáng",
        icon="🪞",
        description="Hiện tượng phản xạ ánh sáng, định luật phản xạ ánh sáng (i' = i) và phân biệt phản xạ gương với phản xạ khuếch tán.",
        requirements=[
            "Xác định được tia tới $SI$, tia phản xạ $IR$, pháp tuyến $IN$, góc tới $i$ và góc phản xạ $i'$ trên hình vẽ.",
            "Phát biểu và vận dụng được định luật phản xạ ánh sáng: tia phản xạ nằm trong mặt phẳng tới và góc phản xạ bằng góc tới ($i' = i$).",
            "Phân biệt được phản xạ gương (trên bề mặt nhẵn bóng) và phản xạ khuếch tán (trên bề mặt gồ ghề).",
        ],
        definition="Theo định luật phản xạ ánh sáng: Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến của gương tại điểm tới; góc phản xạ luôn bằng góc tới ($i' = i$).",
        theory=(
            "### 1. Các khái niệm cơ bản\n"
            "- **Điểm tới $I$**: giao điểm của tia sáng tới $SI$ với mặt gương.\n"
            "- **Pháp tuyến $IN$**: đường thẳng vuông góc với mặt gương tại điểm tới $I$.\n"
            "- **Góc tới $i$**: góc hợp bởi tia tới $SI$ và pháp tuyến $IN$ ($i = \\widehat{SIN}$). Nếu tia tới hợp với mặt gương một góc $\\alpha$ thì $i = 90^\\circ - \\alpha$.\n"
            "- **Góc phản xạ $i'$**: góc hợp bởi tia phản xạ $IR$ và pháp tuyến $IN$ ($i' = \\widehat{NIR}$).\n\n"
            "### 2. Định luật phản xạ ánh sáng & Hai loại phản xạ\n"
            "- Hệ thức định luật phản xạ ánh sáng: $i' = i$. Góc hợp bởi tia tới và tia phản xạ là $\\widehat{SIR} = i + i' = 2i$.\n"
            "- **Phản xạ gương**: chùm tia tới song song chiếu lên bề mặt nhẵn bóng cho chùm tia phản xạ song song (nhìn thấy ảnh rõ nét).\n"
            "- **Phản xạ khuếch tán (tán xạ)**: chùm tia tới song song chiếu lên bề mặt nhám, gồ ghề cho các tia phản xạ truyền theo nhiều hướng khác nhau."
        ),
        formulas=[
            G(
                "Định luật phản xạ ánh sáng",
                F("Hệ thức góc phản xạ và góc tới", "$i' = i$", "Trong đó $i = \\widehat{SIN}$ là góc tới và $i' = \\widehat{NIR}$ là góc phản xạ (đều tính so với pháp tuyến $IN$)."),
                F("Tính góc tới khi biết góc hợp bởi tia tới và mặt gương α", "$i = 90^\\circ - \\alpha; \\quad \\widehat{SIR} = i + i' = 2i$", "Lưu ý: khi tia sáng chiếu vuông góc với mặt gương ($\\alpha = 90^\\circ$) thì góc tới $i = 0^\\circ$ và góc phản xạ $i' = 0^\\circ$."),
            )
        ],
        example="Chiếu một tia sáng $SI$ tới mặt gương phẳng sao cho tia sáng hợp với mặt gương một góc $\\alpha = 30^\\circ$. Hãy tính góc tới $i$, góc phản xạ $i'$ và góc hợp bởi tia tới với tia phản xạ.",
        example_answer="Vì pháp tuyến $IN$ vuông góc với mặt gương nên góc tới là $i = 90^\\circ - \\alpha = 90^\\circ - 30^\\circ = 60^\\circ$. Theo định luật phản xạ ánh sáng, góc phản xạ là $i' = i = 60^\\circ$. Góc hợp bởi tia tới và tia phản xạ là $\\widehat{SIR} = i + i' = 120^\\circ$.",
        real_life="Khi mặt hồ nước phẳng lặng không gợn sóng, ta nhìn thấy bóng hàng cây soi rõ dưới mặt hồ nhờ phản xạ gương; khi có gió thổi làm mặt nước gợn sóng lăn tăn, xảy ra phản xạ khuếch tán nên ảnh bị nhòe.",
        quiz=[
            mcq("biet", "Theo định luật phản xạ ánh sáng, mối quan hệ giữa góc phản xạ $i'$ và góc tới $i$ là gì?", ["$i' = i$", "$i' = 2i$", "$i' = 90^\\circ - i$", "$i' + i = 90^\\circ$"], 0, "Theo định luật phản xạ ánh sáng, góc phản xạ luôn bằng góc tới ($i' = i$)."),
            mcq("biet", "Góc tới $i$ trong hiện tượng phản xạ ánh sáng là góc hợp bởi hai đường nào?", ["Tia tới $SI$ và pháp tuyến $IN$ của gương tại điểm tới", "Tia tới $SI$ và mặt gương", "Tia tới $SI$ và tia phản xạ $IR$", "Tia phản xạ $IR$ và mặt gương"], 0, "Góc tới $i = \\widehat{SIN}$ là góc hợp bởi tia tới $SI$ và pháp tuyến $IN$ tại điểm tới."),
            mcq("hieu", "Chiếu một tia sáng vuông góc với mặt một gương phẳng. Khi đó góc tới $i$ và góc phản xạ $i'$ có giá trị bằng bao nhiêu?", ["$i = 0^\\circ$ và $i' = 0^\\circ$", "$i = 90^\\circ$ và $i' = 90^\\circ$", "$i = 45^\\circ$ và $i' = 45^\\circ$", "$i = 90^\\circ$ và $i' = 0^\\circ$"], 0, "Khi tia sáng vuông góc với mặt gương thì tia tới trùng với pháp tuyến $IN$, nên góc tới $i = 0^\\circ$ và góc phản xạ $i' = 0^\\circ$ (tia phản xạ truyền ngược lại đường cũ)."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về sự phản xạ ánh sáng:", [
                "Nếu góc tới bằng $40^\\circ$ thì góc phản xạ cũng bằng $40^\\circ$ và góc hợp bởi tia tới với tia phản xạ bằng $80^\\circ$.",
                "Nếu tia tới hợp với mặt gương phẳng một góc $35^\\circ$ thì góc tới bằng $35^\\circ$.",
                "Phản xạ gương xảy ra trên các bề mặt nhẵn bóng như mặt gương phẳng hay mặt tấm kim loại đánh bóng.",
                "Nhờ có phản xạ khuếch tán từ trang sách giấy trắng mà ta có thể đọc được chữ từ nhiều hướng khác nhau mà không bị chói mắt.",
            ], [True, False, True, True], "Ý b) sai vì khi tia tới hợp với mặt gương góc $35^\\circ$ thì góc tới hợp với pháp tuyến là $i = 90^\\circ - 35^\\circ = 55^\\circ$."),
            short("vandung", "Chiếu một tia sáng tới mặt gương phẳng sao cho góc hợp bởi tia tới và mặt gương là $\\alpha = 25^\\circ$. Góc phản xạ $i'$ có giá trị bằng bao nhiêu độ?", ["65"], "Góc tới là $i = 90^\\circ - 25^\\circ = 65^\\circ$. Theo định luật phản xạ ánh sáng, góc phản xạ là $i' = i = 65^\\circ$.", unit="độ"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH3_TOPIC,
        chapter_title=CH3_TITLE,
        title="Bài 10: Ảnh của vật qua gương phẳng",
        icon="🖼️",
        description="Tính chất ảnh tạo bởi gương phẳng (ảnh ảo, bằng vật, đối xứng qua gương d' = d) và cách dựng ảnh.",
        requirements=[
            "Nêu được 3 tính chất của ảnh tạo bởi gương phẳng: là ảnh ảo không hứng được trên màn chắn, có độ lớn bằng vật và khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương ($d' = d$).",
            "Dựng được ảnh $S'$ của điểm sáng $S$ và ảnh $A'B'$ của vật sáng $AB$ đặt trước gương phẳng dựa vào tính chất đối xứng.",
            "Vận dụng tính chất ảnh qua gương phẳng để tính khoảng cách từ vật đến ảnh và giải thích ứng dụng kính tiềm vọng.",
        ],
        definition="Ảnh của một vật tạo bởi gương phẳng là ảnh ảo (không hứng được trên màn chắn), có kích thước bằng vật ($h' = h$) và đối xứng với vật qua mặt gương (khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương: $d' = d$).",
        theory=(
            "### 1. Tính chất của ảnh tạo bởi gương phẳng\n"
            "- **Tính chất 1**: Ảnh của vật tạo bởi gương phẳng là **ảnh ảo** (không hứng được trên màn chắn, vì chỉ là giao điểm đường kéo dài của các tia phản xạ).\n"
            "- **Tính chất 2**: Độ lớn của ảnh luôn **bằng độ lớn của vật** ($A'B' = AB$).\n"
            "- **Tính chất 3**: Điểm sáng và ảnh của nó **đối xứng nhau qua gương phẳng**, nghĩa là $SH \\perp \\text{gương}$ và khoảng cách từ ảnh đến gương bằng khoảng cách từ vật đến gương ($d' = d$).\n\n"
            "### 2. Khoảng cách giữa vật và ảnh\n"
            "- Nếu một điểm sáng $S$ cách gương phẳng một khoảng $d$, thì ảnh $S'$ nằm sau gương một khoảng $d' = d$, do đó khoảng cách giữa điểm sáng $S$ và ảnh $S'$ của nó là $SS' = d + d' = 2d$."
        ),
        formulas=[
            G(
                "Công thức khoảng cách và kích thước ảnh qua gương phẳng",
                F("Quan hệ kích thước và khoảng cách tới gương", "$h' = h; \\qquad d' = d$", "Trong đó $h, h'$ là chiều cao vật và ảnh; $d, d'$ là khoảng cách từ vật và từ ảnh tới mặt gương phẳng."),
                F("Khoảng cách giữa vật và ảnh qua gương phẳng", "$L = d + d' = 2d$", "Khi vật tiến lại gần gương một đoạn $\\Delta d$ thì khoảng cách giữa vật và ảnh giảm đi $2\\Delta d$."),
            )
        ],
        example="Một bạn học sinh cao $1{,}6\\text{ m}$ đứng soi gương trước một gương phẳng treo thẳng đứng và cách gương một khoảng $d = 1{,}2\\text{ m}$. Hãy cho biết chiều cao ảnh của bạn đó trong gương và khoảng cách từ bạn đó đến ảnh của mình.",
        example_answer="Vì ảnh qua gương phẳng có độ lớn bằng vật nên ảnh của bạn học sinh cao $h' = h = 1{,}6\\text{ m}$. Ảnh cách gương một khoảng $d' = d = 1{,}2\\text{ m}$, nên khoảng cách từ bạn học sinh đến ảnh là $L = d + d' = 1{,}2 + 1{,}2 = 2{,}4\\text{ m}$.",
        real_life="Kính tiềm vọng trên tàu ngầm sử dụng hai gương phẳng đặt song song nghiêng góc $45^\\circ$ giúp thủy thủ ở dưới mặt nước quan sát được các tàu thuyền trên mặt biển.",
        quiz=[
            mcq("biet", "Ảnh của một vật tạo bởi gương phẳng có tính chất nào sau đây?", ["Là ảnh ảo, không hứng được trên màn chắn và lớn bằng vật", "Là ảnh thật, hứng được trên màn chắn và lớn bằng vật", "Là ảnh ảo và luôn nhỏ hơn vật", "Là ảnh ảo và luôn lớn gấp đôi vật"], 0, "Ảnh tạo bởi gương phẳng luôn là ảnh ảo, không hứng được trên màn chắn và có kích thước bằng vật."),
            mcq("biet", "Để dựng ảnh $S'$ của một điểm sáng $S$ đặt trước gương phẳng nhanh và chính xác nhất, ta lấy điểm $S'$ như thế nào?", ["Lấy $S'$ đối xứng với $S$ qua mặt phẳng gương", "Lấy $S'$ trùng với điểm $S$", "Lấy $S'$ nằm ngay trên mặt gương", "Lấy $S'$ cách gương gấp đôi khoảng cách từ $S$ đến gương"], 0, "Ảnh $S'$ của điểm sáng $S$ qua gương phẳng luôn đối xứng với $S$ qua mặt gương."),
            mcq("hieu", "Một vật sáng đặt cách gương phẳng $40\\text{ cm}$. Nếu dịch chuyển vật lại gần gương thêm $10\\text{ cm}$ theo phương vuông góc với mặt gương thì khoảng cách từ vật đến ảnh của nó lúc này là bao nhiêu?", ["$60\\text{ cm}$", "$30\\text{ cm}$", "$80\\text{ cm}$", "$50\\text{ cm}$"], 0, "Khoảng cách mới từ vật đến gương là $d = 40 - 10 = 30\\text{ cm}$. Khi đó khoảng cách giữa vật và ảnh là $L = 2d = 2 \\cdot 30 = 60\\text{ cm}$."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về ảnh của vật qua gương phẳng:", [
                "Khi một người tiến lại gần gương phẳng, kích thước ảnh của người đó trong gương tăng lên.",
                "Một mũi tên $AB$ dài $8\\text{ cm}$ đặt trước gương phẳng luôn cho ảnh ảo $A'B'$ dài đúng $8\\text{ cm}$.",
                "Đoạn thẳng nối điểm sáng $S$ và ảnh $S'$ của nó luôn vuông góc với mặt gương phẳng tại trung điểm của $SS'$.",
                "Các tia phản xạ từ gương phẳng đi tới mắt có đường kéo dài đi qua ảnh ảo $S'$ phía sau gương.",
            ], [False, True, True, True], "Ý a) sai vì độ lớn của ảnh tạo bởi gương phẳng luôn bằng độ lớn của vật, không phụ thuộc khoảng cách từ vật tới gương."),
            short("vandung", "Một điểm sáng $S$ đặt trước một gương phẳng và cách mặt gương một khoảng $d = 25\\text{ cm}$. Khoảng cách từ điểm sáng $S$ đến ảnh $S'$ của nó bằng bao nhiêu $\\text{cm}$?", ["50"], "Ảnh $S'$ đối xứng với $S$ qua gương nên khoảng cách giữa $S$ và $S'$ là $SS' = 2d = 2 \\cdot 25 = 50\\text{ cm}$.", unit="cm"),
        ],
        chapter_desc=CH3_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 11: Nam châm",
        icon="🧲",
        description="Tính chất từ của nam châm vĩnh cửu, hai cực từ Bắc (N) – Nam (S), tương tác giữa hai nam châm và vật liệu từ.",
        requirements=[
            "Nêu được nam châm là vật có từ tính, có khả năng hút các vật bằng sắt, thép, niken, côban (vật liệu từ).",
            "Chỉ ra được mọi nam châm luôn có hai cực từ: cực Bắc (kí hiệu $\\text{N}$) và cực Nam (kí hiệu $\\text{S}$).",
            "Trình bày được quy luật tương tác giữa hai nam châm: hai cực cùng tên thì đẩy nhau, hai cực khác tên thì hút nhau.",
        ],
        definition="Nam châm là những vật có tính chất từ (hút được các vật bằng sắt, thép, niken, côban...). Mỗi nam châm đều có hai cực từ là cực Bắc (kí hiệu $\\text{N}$ – North) và cực Nam (kí hiệu $\\text{S}$ – South). Khi đưa hai cực từ lại gần nhau: cùng tên thì đẩy nhau, khác tên thì hút nhau.",
        theory=(
            "### 1. Tính chất từ và hai cực của nam châm\n"
            "- Nam châm hút được các **vật liệu từ** như sắt ($\\text{Fe}$), thép, niken ($\\text{Ni}$), côban ($\\text{Co}$), nhưng **không hút** đồng ($\\text{Cu}$), nhôm ($\\text{Al}$), vàng, bạc, nhựa, gỗ.\n"
            "- Lực hút từ mạnh nhất ở **hai đầu cực** của thanh nam châm và rất yếu ở chính giữa thanh.\n"
            "- Khi để kim nam châm tự do quay quanh trục thẳng đứng, một đầu luôn chỉ hướng Bắc (gọi là **cực Bắc $\\text{N}$**, thường sơn màu đỏ) và đầu kia chỉ hướng Nam (gọi là **cực Nam $\\text{S}$**, thường sơn màu xanh hoặc trắng).\n\n"
            "### 2. Tương tác giữa hai nam châm\n"
            "- Hai cực **cùng tên** ($\\text{N} - \\text{N}$ hoặc $\\text{S} - \\text{S}$) đặt gần nhau thì **đẩy nhau**.\n"
            "- Hai cực **khác tên** ($\\text{N} - \\text{S}$) đặt gần nhau thì **hút nhau**."
        ),
        formulas=[
            G(
                "Quy tắc cực từ và tương tác nam châm",
                F("Tương tác giữa hai cực từ", "$\\text{N} \\leftrightarrow \\text{N} \\text{ hoặc } \\text{S} \\leftrightarrow \\text{S}: \\text{Đẩy nhau}; \\qquad \\text{N} \\leftrightarrow \\text{S}: \\text{Hút nhau}$", "Dùng lực đẩy giữa hai cực cùng tên để phân biệt một thanh nam châm với một thanh sắt chưa nhiễm từ."),
                F("Tính không tách rời của hai cực từ", "$1 \\text{ nam châm bị cắt đôi} \\implies 2 \\text{ nam châm mới đều đủ cả 2 cực N và S}$", "Không bao giờ thu được một nam châm chỉ có một cực từ đơn độc."),
            )
        ],
        example="Nếu một thanh nam châm thẳng không may bị gãy làm hai nửa ở chính giữa, thì mỗi nửa thanh nam châm đó sẽ chỉ còn một cực từ duy nhất hay vẫn có đủ cả hai cực Bắc ($\\text{N}$) và Nam ($\\text{S}$)?",
        example_answer="Mỗi nửa thanh nam châm sau khi gãy sẽ trở thành một thanh nam châm mới hoàn chỉnh và đều có đủ cả hai cực từ Bắc ($\\text{N}$) và Nam ($\\text{S}$).",
        real_life="Cánh cửa tủ lạnh có viền đệm cao su gắn dải nam châm giúp cửa tự động hút chặt vào vỏ thép của tủ lạnh; các bác sĩ dùng nam châm y tế để lấy mạt sắt nhỏ chẳng may bay vào mắt bệnh nhân.",
        quiz=[
            mcq("biet", "Thanh nam châm vĩnh cửu có thể hút mạnh các vật được làm bằng chất liệu nào sau đây?", ["Sắt và thép", "Đồng và nhôm", "Nhựa và cao su", "Gỗ khô và thủy tinh"], 0, "Sắt, thép, niken, côban là các vật liệu có tính chất từ nên bị nam châm hút mạnh."),
            mcq("biet", "Khi đưa cực Bắc ($\\text{N}$) của thanh nam châm thứ nhất lại gần cực Bắc ($\\text{N}$) của thanh nam châm thứ hai thì xảy ra hiện tượng gì?", ["Hai cực đẩy nhau", "Hai cực hút nhau", "Hai cực không tương tác với nhau", "Hai thanh nam châm mất hết từ tính"], 0, "Hai cực từ cùng tên ($\\text{N}$ và $\\text{N}$) khi đặt gần nhau luôn đẩy nhau."),
            mcq("hieu", "Trên một thanh nam châm thẳng, vị trí nào hút các mạt sắt mạnh nhất?", ["Ở cả hai đầu cực từ ($\\text{N}$ và $\\text{S}$) của thanh nam châm", "Ở điểm chính giữa của thanh nam châm", "Chỉ ở riêng cực Bắc ($\\text{N}$)", "Chỉ ở riêng cực Nam ($\\text{S}$)"], 0, "Từ tính của thanh nam châm tập trung mạnh nhất ở hai đầu cực từ ($\\text{N}$ và $\\text{S}$) và yếu nhất ở phần chính giữa."),
            tf4("hieu", "Xét tính đúng/sai của các nhận định sau về nam châm:", [
                "Mọi nam châm luôn có hai cực: cực Bắc (kí hiệu $\\text{N}$) và cực Nam (kí hiệu $\\text{S}$).",
                "Hai cực khác tên ($\\text{N}$ và $\\text{S}$) của hai nam châm đặt gần nhau thì hút nhau.",
                "Nam châm hút được mọi kim loại như đồng, nhôm, vàng và bạc.",
                "Khi cưa đôi một thanh nam châm thẳng, ta thu được một nửa chỉ mang cực Bắc $\\text{N}$ và một nửa chỉ mang cực Nam $\\text{S}$.",
            ], [True, True, False, False], "Ý c) sai vì nam châm không hút đồng, nhôm, vàng, bạc; ý d) sai vì mỗi nửa sau khi cắt đều có đủ cả hai cực $\\text{N}$ và $\\text{S}$."),
            short("vandung", "Mỗi thanh nam châm vĩnh cửu luôn có bao nhiêu cực từ?", ["2"], "Mỗi nam châm luôn có $2$ cực từ là cực Bắc ($\\text{N}$) và cực Nam ($\\text{S}$)."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 12: Từ trường",
        icon="🧭",
        description="Khái niệm từ trường quanh nam châm và dòng điện, từ phổ và quy ước chiều đường sức từ (ra Bắc vào Nam).",
        requirements=[
            "Nêu được không gian bao quanh nam châm và bao quanh dây dẫn có dòng điện chạy qua tồn tại từ trường.",
            "Nhận biết được dụng cụ dùng để phát hiện sự tồn tại của từ trường là kim nam châm thử.",
            "Mô tả được hình ảnh từ phổ (bằng mạt sắt) và nêu đúng quy ước chiều của đường sức từ ở bên ngoài nam châm: đi ra từ cực Bắc ($\\text{N}$) và đi vào cực Nam ($\\text{S}$).",
        ],
        definition="Không gian bao quanh nam châm hoặc bao quanh dây dẫn mang dòng điện có khả năng tác dụng lực từ lên kim nam châm đặt trong nó; ta nói trong không gian đó có từ trường. Ở bên ngoài nam châm, các đường sức từ có chiều đi ra từ cực Bắc ($\\text{N}$) và đi vào cực Nam ($\\text{S}$).",
        theory=(
            "### 1. Từ trường và cách nhận biết\n"
            "- **Từ trường** tồn tại trong không gian xung quanh **nam châm** và xung quanh **dòng điện**.\n"
            "- Để nhận biết tại một điểm trong không gian có từ trường hay không, người ta đặt tại đó một **kim nam châm thử** (nếu kim nam châm bị lệch khỏi hướng Bắc – Nam ban đầu thì tại đó có từ trường).\n\n"
            "### 2. Từ phổ và đường sức từ\n"
            "- **Từ phổ**: hình ảnh các đường tạo bởi mạt sắt rắc trên tấm nhựa đặt trong từ trường khi gõ nhẹ.\n"
            "- **Đường sức từ**: các đường cong vẽ trong không gian có từ trường sao cho độ mau/thưa thể hiện độ mạnh/yếu của từ trường.\n"
            "- **Quy ước chiều đường sức từ**: ở bên ngoài thanh nam châm, đường sức từ là những đường cong có chiều **đi ra từ cực Bắc ($\\text{N}$) và đi vào cực Nam ($\\text{S}$)**."
        ),
        formulas=[
            G(
                "Quy ước đường sức từ và độ mạnh từ trường",
                F("Chiều đường sức từ bên ngoài nam châm", "$\\text{Cực Bắc (N)} \\longrightarrow \\text{Đường sức từ} \\longrightarrow \\text{Cực Nam (S)}$", "Quy tắc nhớ nhanh: 'Ra Bắc ($\\text{N}$) – Vào Nam ($\\text{S}$)'."),
                F("Mật độ đường sức từ và độ mạnh từ trường", "$\\text{Đường sức từ càng dày (mau)} \\iff \\text{Từ trường càng mạnh}$", "Ở gần hai cực của nam châm, các đường sức từ rất dày nên từ trường mạnh; càng xa nam châm đường sức từ càng thưa."),
            )
        ],
        example="Đặt một kim nam châm nhỏ tự do trên đường sức từ nối giữa hai cực của một nam châm chữ U. Biết cực Bắc của kim nam châm hướng về đầu $A$ và cực Nam của kim nam châm hướng về đầu $B$ của nam châm chữ U. Hãy xác định tên các cực từ $A$ và $B$ của nam châm chữ U.",
        example_answer="Vì hai cực khác tên hút nhau (hoặc theo chiều đường sức từ ra $\\text{N}$ vào $\\text{S}$), cực Bắc của kim nam châm bị hút về phía cực Nam của nam châm chữ U. Vậy đầu $A$ là cực Nam ($\\text{S}$) và đầu $B$ là cực Bắc ($\\text{N}$).",
        real_life="Thí nghiệm Oersted đưa dây dẫn có dòng điện chạy qua song song phía trên một kim nam châm làm kim nam châm quay lệch đi đã mở ra ngành Điện từ học hiện đại.",
        quiz=[
            mcq("biet", "Để nhận biết tại một vị trí trong không gian có từ trường hay không, người ta sử dụng dụng cụ nào sau đây?", ["Kim nam châm thử có thể quay tự do", "Nhiệt kế thủy ngân", "Thước kẻ nhựa", "Cân đồng hồ"], 0, "Kim nam châm thử chịu tác dụng của lực từ nên là dụng cụ dùng để phát hiện từ trường."),
            mcq("biet", "Ở bên ngoài một thanh nam châm, chiều của các đường sức từ được quy ước như thế nào?", ["Đi ra từ cực Bắc ($\\text{N}$) và đi vào cực Nam ($\\text{S}$)", "Đi ra từ cực Nam ($\\text{S}$) và đi vào cực Bắc ($\\text{N}$)", "Đi ra từ cả hai cực $\\text{N}$ và $\\text{S}$", "Đi vào cả hai cực $\\text{N}$ và $\\text{S}$"], 0, "Theo quy ước, bên ngoài nam châm đường sức từ có chiều đi ra từ cực Bắc ($\\text{N}$) và đi vào cực Nam ($\\text{S}$)."),
            mcq("hieu", "Quan sát hình ảnh từ phổ của một thanh nam châm, nơi nào có các đường mạt sắt sắp xếp dày (mau) nhất?", ["Ở gần hai đầu cực từ của thanh nam châm", "Ở khoảng chính giữa thanh nam châm", "Ở rất xa thanh nam châm", "Mạt sắt phân bố đều như nhau ở mọi chỗ"], 0, "Nơi từ trường mạnh (ở gần hai cực từ) có các đường mạt sắt và đường sức từ sắp xếp dày nhất."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về từ trường và đường sức từ:", [
                "Không gian xung quanh nam châm và xung quanh dòng điện đều tồn tại từ trường.",
                "Chiều của đường sức từ bên ngoài nam châm tuân theo quy tắc 'ra Bắc ($\\text{N}$) vào Nam ($\\text{S}$)'.",
                "Chỗ nào các đường sức từ càng thưa thì từ trường tại chỗ đó càng mạnh.",
                "Rắc mạt sắt lên tấm nhựa trong đặt trên thanh nam châm rồi gõ nhẹ giúp ta quan sát được hình ảnh từ phổ.",
            ], [True, True, False, True], "Ý c) sai vì chỗ nào đường sức từ càng dày (mau) thì từ trường càng mạnh, càng thưa thì từ trường càng yếu."),
            short("vandung", "Xung quanh (1) thanh nam châm vĩnh cửu, (2) dây dẫn đang có dòng điện chạy qua, (3) thanh gỗ khô không mang điện. Có bao nhiêu vật trong 3 vật trên có **từ trường** bao quanh?", ["2"], "Từ trường tồn tại xung quanh (1) nam châm và (2) dây dẫn có dòng điện chạy qua, tức có $2$ vật."),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 13: Từ trường Trái Đất. Sử dụng la bàn",
        icon="🌍",
        description="Trái Đất là một nam châm khổng lồ, vị trí cực từ so với cực địa lí, cấu tạo và quy tắc sử dụng la bàn định hướng.",
        requirements=[
            "Giải thích được vì sao kim nam châm tự do luôn chỉ hướng Bắc – Nam địa lí là do tác dụng của từ trường Trái Đất.",
            "Nhận biết được cực từ Bắc của Trái Đất nằm gần cực Nam địa lí và cực từ Nam của Trái Đất nằm gần cực Bắc địa lí.",
            "Mô tả được cấu tạo của la bàn và thực hiện đúng các bước sử dụng la bàn để xác định phương hướng.",
        ],
        definition="Trái Đất là một thanh nam châm khổng lồ có từ trường bao quanh. Nhờ từ trường Trái Đất, kim nam châm trong la bàn khi nằm cân bằng luôn định hướng theo phương Bắc – Nam địa lí.",
        theory=(
            "### 1. Từ trường của Trái Đất\n"
            "- Trái Đất giống như một thanh nam châm khổng lồ. Đường sức từ của Trái Đất đi từ vùng bán cầu Nam lên vùng bán cầu Bắc.\n"
            "- Vì cực Bắc ($\\text{N}$) của kim la bàn luôn hướng về phía cực Bắc địa lí nên gần **cực Bắc địa lí** là **cực từ Nam** của nam châm Trái Đất, và gần **cực Nam địa lí** là **cực từ Bắc** của nam châm Trái Đất.\n"
            "- Trục từ và trục quay địa lí của Trái Đất không hoàn toàn trùng nhau mà lệch nhau một góc nhỏ.\n\n"
            "### 2. Cấu tạo và cách sử dụng la bàn\n"
            "- **La bàn** gồm: kim nam châm quay tự do trên trục nhọn, mặt chia độ từ $0^\\circ$ đến $360^\\circ$ có ghi các hướng Bắc ($\\text{N}$), Đông ($\\text{E}$), Nam ($\\text{S}$), Tây ($\\text{W}$) và vỏ hộp bảo vệ (bằng nhựa, đồng hoặc nhôm — không làm bằng sắt thép).\n"
            "- **Cách dùng**: Đặt la bàn trên mặt phẳng nằm ngang, **cách xa các nam châm khác và các vật bằng sắt thép, dòng điện**, đợi kim đứng yên rồi xoay vỏ la bàn sao cho vạch chữ $\\text{N}$ trùng với đầu cực Bắc của kim."
        ),
        formulas=[
            G(
                "Các hướng chính trên mặt chia độ của la bàn",
                F("Các góc phương vị trên mặt la bàn", "$\\text{Bắc (N)} = 0^\\circ; \\quad \\text{Đông (E)} = 90^\\circ; \\quad \\text{Nam (S)} = 180^\\circ; \\quad \\text{Tây (W)} = 270^\\circ$", "Các hướng phụ: Đông Bắc ($\\text{NE} = 45^\\circ$), Đông Nam ($\\text{SE} = 135^\\circ$), Tây Nam ($\\text{SW} = 225^\\circ$), Tây Bắc ($\\text{NW} = 315^\\circ$)."),
                F("Nguyên lý định hướng của kim la bàn", "$\\text{Cực Bắc (N) của kim la bàn} \\longrightarrow \\text{Hướng về Cực Bắc địa lí}$", "Do lực từ của từ trường Trái Đất tác dụng lên kim nam châm."),
            )
        ],
        example="Vì sao vỏ hộp và mặt đế của la bàn thường được chế tạo bằng nhôm, đồng hoặc nhựa mà tuyệt đối không làm bằng sắt hoặc thép?",
        example_answer="Vì sắt và thép là các vật liệu từ; nếu làm vỏ la bàn bằng sắt hoặc thép thì vỏ hộp sẽ hút kim nam châm của la bàn, làm kim bị kẹt hoặc không còn chỉ đúng hướng Bắc – Nam của từ trường Trái Đất.",
        real_life="Thủy thủ đi biển, phi công, người đi rừng và các loài chim di cư đều định hướng đường đi dựa vào từ trường của Trái Đất.",
        quiz=[
            mcq("biet", "Bộ phận chính quan trọng nhất bên trong một chiếc la bàn dùng để định hướng là gì?", ["Một kim nam châm có thể quay tự do trên trục thẳng đứng", "Một lò xo xoắn bằng thép", "Một nhiệt kế rượu nhỏ", "Một bóng đèn phát sáng"], 0, "Bộ phận cốt lõi của la bàn là kim nam châm nhỏ quay tự do dưới tác dụng của từ trường Trái Đất."),
            mcq("biet", "Trên mặt chia độ của la bàn, kí hiệu chữ $\\text{N}$ và chữ $\\text{S}$ lần lượt chỉ hướng địa lí nào?", ["$\\text{N}$ chỉ hướng Bắc, $\\text{S}$ chỉ hướng Nam", "$\\text{N}$ chỉ hướng Đông, $\\text{S}$ chỉ hướng Tây", "$\\text{N}$ chỉ hướng Nam, $\\text{S}$ chỉ hướng Bắc", "$\\text{N}$ chỉ hướng Tây, $\\text{S}$ chỉ hướng Đông"], 0, "$\\text{N}$ (North) chỉ hướng Bắc và $\\text{S}$ (South) chỉ hướng Nam."),
            mcq("hieu", "Khi sử dụng la bàn để xác định phương hướng, tại sao phải đặt la bàn cách xa các thanh nam châm khác và các vật lớn bằng sắt, thép?", ["Để tránh từ trường của nam châm hoặc vật bằng sắt làm lệch hướng của kim la bàn", "Để tránh làm mặt kính của la bàn bị vỡ", "Để tránh làm la bàn bị tăng nhiệt độ", "Để làm tăng khối lượng của kim la bàn"], 0, "Nam châm hoặc vật bằng sắt ở gần sẽ tác dụng lực từ mạnh lên kim la bàn, làm kim không còn chỉ đúng hướng Bắc – Nam của Trái Đất."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về từ trường Trái Đất và la bàn:", [
                "Trái Đất là một nam châm khổng lồ nên xung quanh Trái Đất có từ trường.",
                "Từ trường của Trái Đất giúp cản lại các bức xạ hạt mang điện nguy hiểm từ Mặt Trời (gió Mặt Trời), bảo vệ sự sống trên Trái Đất.",
                "Khi sử dụng la bàn, ta nên đặt sát cạnh một chiếc loa nam châm lớn để kim la bàn quay nhanh hơn.",
                "Trên mặt la bàn, các kí hiệu $\\text{E}$ (East) và $\\text{W}$ (West) lần lượt chỉ hướng Đông và hướng Tây.",
            ], [True, True, False, True], "Ý c) sai vì đặt la bàn sát nam châm của loa sẽ làm kim la bàn chỉ sai lệch hoàn toàn."),
            short("vandung", "Trên mặt chia độ $360^\\circ$ của la bàn, nếu hướng Bắc ($\\text{N}$) ứng với vạch $0^\\circ$ và hướng Đông ($\\text{E}$) ứng với vạch $90^\\circ$, thì hướng Nam ($\\text{S}$) đối diện với hướng Bắc ứng với vạch bao nhiêu độ?", ["180"], "Hướng Nam ($\\text{S}$) ngược chiều với hướng Bắc ($\\text{N} = 0^\\circ$) nên ứng với góc $180^\\circ$.", unit="độ"),
        ],
        chapter_desc=CH4_DESC,
    ),
    bai(
        topic=CH4_TOPIC,
        chapter_title=CH4_TITLE,
        title="Bài 14: Nam châm điện",
        icon="🔋",
        description="Cấu tạo của nam châm điện (ống dây có dòng điện và lõi sắt non), cách làm tăng lực từ và đổi cực nam châm điện.",
        requirements=[
            "Mô tả được cấu tạo của một nam châm điện gồm một ống dây dẫn có dòng điện một chiều chạy qua và một lõi sắt non đặt bên trong.",
            "Giải thích được vì sao lõi nam châm điện dùng sắt non mà không dùng thép (sắt non mất từ tính ngay khi ngắt điện).",
            "Nêu được các cách làm tăng lực từ của nam châm điện (tăng cường độ dòng điện $I$, tăng số vòng dây $N$) và cách đổi cực từ (đổi chiều dòng điện).",
        ],
        definition="Nam châm điện gồm một ống dây dẫn có dòng điện chạy qua và bên trong ống dây có đặt một lõi sắt non. Nam châm điện chỉ có tính chất từ khi có dòng điện chạy qua và mất hết từ tính ngay khi ngắt dòng điện.",
        theory=(
            "### 1. Cấu tạo và hoạt động của nam châm điện\n"
            "- Gồm **ống dây dẫn** nối với nguồn điện một chiều (pin, ắc quy) và một **lõi sắt non** lồng trong lòng ống dây.\n"
            "- **Lõi sắt non** làm tăng mạnh tác dụng từ của ống dây khi có dòng điện chạy qua, và khi **ngắt dòng điện** thì sắt non **mất sạch từ tính ngay lập tức** (nếu dùng lõi thép thì khi ngắt điện thép vẫn giữ từ tính trở thành nam châm vĩnh cửu, không nhả được vật sắt ra).\n\n"
            "### 2. Thay đổi lực từ và cực từ của nam châm điện\n"
            "- **Làm tăng lực từ**: (1) Tăng cường độ dòng điện $I$ chạy qua ống dây (tăng số pin nối tiếp); (2) Tăng số vòng dây $N$ của ống dây.\n"
            "- **Đổi tên hai cực từ ($\\text{N} \\leftrightarrow \\text{S}$)**: Đổi chiều dòng điện chạy vào hai đầu ống dây (đảo hai cực của nguồn pin)."
        ),
        formulas=[
            G(
                "Các yếu tố điều khiển nam châm điện",
                F("Cách tăng lực từ của nam châm điện", "$\\text{Tăng dòng điện } I \\text{ hoặc tăng số vòng dây } N \\implies \\text{Lực từ } F_{\\text{từ}} \\text{ tăng}$", "Ngoài ra thêm lõi sắt non vào lòng ống dây làm lực từ mạnh hơn rất nhiều so với ống dây rỗng."),
                F("Cách đổi cực từ và tắt từ tính", "$\\text{Đảo chiều dòng điện } I \\implies \\text{Đổi cực } \\text{N} \\leftrightarrow \\text{S}; \\qquad I = 0 \\implies F_{\\text{từ}} = 0$", "Đây là ưu điểm vượt trội của nam châm điện so với nam châm vĩnh cửu."),
            )
        ],
        example="Một học sinh chế tạo một nam châm điện bằng cách quấn $50$ vòng dây đồng quanh một chiếc đinh sắt non và nối với $1$ viên pin $1{,}5\\text{ V}$, hút được $8$ chiếc ghim giấy. Học sinh đó muốn nam châm điện hút được nhiều ghim giấy hơn thì cần thay đổi như thế nào?",
        example_answer="Học sinh đó có thể thực hiện một trong hai cách (hoặc kết hợp cả hai): (1) quấn tăng số vòng dây đồng trên đinh sắt (ví dụ từ $50$ vòng lên $100$ vòng); (2) ghép nối tiếp $2$ viên pin ($3\\text{ V}$) để tăng dòng điện chạy qua ống dây.",
        real_life="Cần cẩu điện từ ở cảng và nhà máy luyện kim dùng nam châm điện cực mạnh: đóng điện để hút hàng tấn sắt thép vụn nhấc lên xe tải, rồi ngắt điện để sắt thép tự động rơi xuống thùng xe.",
        quiz=[
            mcq("biet", "Cấu tạo cơ bản của một nam châm điện trong phòng thí nghiệm gồm những bộ phận nào?", ["Một ống dây dẫn có dòng điện chạy qua và một lõi sắt non bên trong", "Một ống nhựa rỗng và một thanh đồng bên trong", "Một thanh gỗ khô quấn chỉ mảnh", "Một thanh thủy tinh đặt cạnh một viên pin"], 0, "Nam châm điện gồm ống dây dẫn có dòng điện chạy qua và lõi sắt non đặt trong lòng ống dây."),
            mcq("biet", "Vì sao lõi của nam châm điện được làm bằng **sắt non** mà không làm bằng thép?", ["Vì khi ngắt dòng điện, sắt non mất ngay từ tính giúp nam châm điện nhả vật ra, còn thép vẫn giữ từ tính lâu dài", "Vì sắt non không bị nam châm hút", "Vì thép không dẫn điện", "Vì sắt non nhẹ hơn nhôm"], 0, "Sắt non nhiễm từ mạnh khi có dòng điện nhưng mất từ tính ngay khi ngắt điện, giúp điều khiển đóng/nhả của nam châm điện."),
            mcq("hieu", "Muốn đổi tên hai cực từ Bắc ($\\text{N}$) và Nam ($\\text{S}$) của một nam châm điện, ta phải làm cách nào sau đây?", ["Đổi chiều dòng điện chạy qua các vòng dây (đảo hai đầu dây nối với hai cực của pin)", "Tăng thêm số vòng dây của ống dây", "Rút lõi sắt non ra khỏi ống dây", "Thay lõi sắt non bằng lõi nhôm"], 0, "Chiều của đường sức từ và tên các cực từ của nam châm điện phụ thuộc vào chiều dòng điện chạy trong ống dây."),
            tf4("hieu", "Xét tính đúng/sai của các phát biểu sau về nam châm điện:", [
                "Khi ngắt công tắc điện, nam châm điện mất từ tính và các đinh sắt bị hút sẽ rơi ra.",
                "Tăng số vòng dây hoặc tăng cường độ dòng điện chạy qua ống dây sẽ làm tăng lực từ của nam châm điện.",
                "Nam châm vĩnh cửu có thể dễ dàng điều chỉnh tăng giảm lực từ và đảo cực bằng một công tắc điện.",
                "Chuông điện, rơ-le điện từ và cần cẩu từ đều là các thiết bị ứng dụng nam châm điện.",
            ], [True, True, False, True], "Ý c) sai vì chỉ có nam châm điện mới điều chỉnh được lực từ và đảo cực bằng dòng điện, còn nam châm vĩnh cửu có từ tính cố định."),
            short("vandung", "Có hai ống dây có lõi sắt non giống hệt nhau và cùng nối vào nguồn điện có cùng cường độ dòng điện: ống dây thứ nhất có $N_1 = 100$ vòng dây, ống dây thứ hai có $N_2 = 250$ vòng dây. Hỏi ống dây thứ mấy (nhập 1 hoặc 2) là nam châm điện mạnh hơn?", ["2"], "Vì cùng cường độ dòng điện nhưng số vòng dây $N_2 = 250 > N_1 = 100$ nên nam châm điện số $2$ có lực từ mạnh hơn."),
        ],
        chapter_desc=CH4_DESC,
    ),
]
