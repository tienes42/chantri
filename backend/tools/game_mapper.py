# -*- coding: utf-8 -*-
"""Bảng ánh xạ bài học Toán - Lý - Hóa sang các file Game trong public/games/.

Chỉ ánh xạ những bài học có game thực tế tương ứng. Bài học chưa có game trả về None
để giao diện hiển thị trạng thái "Đang xây dựng".
"""

GAME_META = {'game_do_luong': {'file': 'games/game_do_luong.html',
                   'title': 'Bé Đo Giỏi – Đo độ dài và Thời gian',
                   'desc': 'Thực hành đo độ dài, xem đồng hồ, tính thời gian và quy đổi đơn vị đo qua các thử thách '
                           'trực quan.'},
 'store_management': {'file': 'games/store_management.html',
                      'title': 'Ông Chủ Tập Sự – Toán Kinh Tế, Hàm Số & Thống Kê',
                      'desc': 'Vận dụng phép tính, tỉ số phần trăm, phương trình, hệ phương trình, hàm số và thống kê '
                              'để điều hành cửa hàng tối ưu lợi nhuận.'},
 'function-challenge': {'file': 'games/function-challenge.html',
                        'title': 'Trạm Điều Hành Đạo Hàm – Toán 11 (CT GDPT 2018)',
                        'desc': 'Khám phá ý nghĩa hình học và vật lí của đạo hàm, tiếp tuyến, vận tốc tức thời và quy '
                                'tắc tính đạo hàm.'},
 'game_ung_dung_dao_ham': {'file': 'games/game_ung_dung_dao_ham.html',
                           'title': 'Biệt Đội Cực Trị – Ứng dụng Đạo hàm Khảo sát & Vẽ Đồ thị Hàm số',
                           'desc': 'Xét tính đơn điệu, tìm cực trị, giá trị lớn nhất – nhỏ nhất, đường tiệm cận và '
                                   'khảo sát đồ thị hàm số thực tế.'},
 'game_toa_do_oxyz': {'file': 'games/game_toa_do_oxyz.html',
                      'title': 'Đội Định Vị Hình Học – Vectơ & Phương pháp Tọa độ',
                      'desc': 'Vận dụng vectơ, tích vô hướng, hệ trục tọa độ và phương trình đường thẳng, mặt phẳng, '
                              'mặt cầu trong định vị không gian.'},
 'game_nguyen_ham': {'file': 'games/game_nguyen_ham.html',
                     'title': 'Trạm Tích Lũy – Nguyên Hàm & Tích Phân Ứng Dụng',
                     'desc': 'Tính nguyên hàm, tích phân xác định, bài toán quãng đường s = ∫v(t)dt, diện tích hình '
                             'phẳng và thể tích vật thể.'},
 'game_on_tap_thpt': {'file': 'games/game_on_tap_thpt.html',
                      'title': 'Mô Hình Hóa Toán THPT – Mũ Lôgarit, Thống Kê & Xác Suất Bayes',
                      'desc': 'Giải quyết các bài toán tối ưu thực tiễn, lãi kép mũ – lôgarit, khoảng biến thiên – '
                              'phương sai và xác suất có điều kiện.'},
 'game_dodai': {'file': 'games/game_dodai.html',
                'title': 'Thợ Mộc Học Việc – Đo Chiều Dài & Sai Số Phép Đo',
                'desc': 'Chọn thước đo có GHĐ và ĐCNN phù hợp, đọc kết quả chính xác và đổi đơn vị đo chiều dài để gia '
                        'công gỗ.'},
 'game_khoiluong': {'file': 'games/game_khoiluong.html',
                    'title': 'Tạp Hóa Cô Tám – Đo Khối Lượng & Quy Đổi Đơn Vị',
                    'desc': 'Sử dụng các loại cân, ước lượng khối lượng, đổi đơn vị g – kg – tạ – tấn và tính tải '
                            'trọng xe chở hàng.'},
 'game_nhietdo': {'file': 'games/game_nhietdo.html',
                  'title': 'Ca Đêm Kho Lạnh – Đo Nhiệt Độ & Thang Nhiệt Độ Celsius – Kelvin',
                  'desc': 'Đọc nhiệt kế, quy đổi giữa thang nhiệt độ Celsius (°C), Fahrenheit (°F), Kelvin (K) và điều '
                          'chỉnh kho bảo quản lạnh.'},
 'game_luc': {'file': 'games/game_luc.html',
              'title': 'Cứu Hộ Đêm Mưa – Lực, Biểu Diễn Lực & Biến Dạng Lò Xo',
              'desc': 'Xác định phương, chiều, độ lớn của lực kéo cứu hộ và độ giãn lò xo theo định luật Hooke.'},
 'game_trong_luong_nang_luong': {'file': 'games/game_trong_luong_nang_luong.html',
                                 'title': 'Trọng Lực & Năng Lượng – Trọng lượng P = 10m & Bảo toàn năng lượng',
                                 'desc': 'Tính trọng lượng P = 10m, phân tích sự truyền năng lượng, định luật bảo toàn '
                                         'năng lượng và chuyển động thiên thể.'},
 'game_lucmasat': {'file': 'games/game_lucmasat.html',
                   'title': 'Kiểm Định Lốp Xe – Lực Ma Sát & Lực Cản Môi Trường',
                   'desc': 'Khảo sát lực ma sát trượt, ma sát nghỉ, lực cản của nước/không khí và kiểm định độ bám '
                           'đường an toàn.'},
 'game_speed': {'file': 'games/game_speed.html',
                'title': 'Giao Hàng Đúng Giờ – Tốc Độ Chuyển Động v = s / t',
                'desc': 'Tính tốc độ v = s/t, đọc đồ thị quãng đường – thời gian, đổi đơn vị km/h ↔ m/s và giữ khoảng '
                        'cách an toàn giao thông.'},
 'game_amthanh': {'file': 'games/game_amthanh.html',
                  'title': 'Cảng Container Cảnh Báo – Sóng Âm, Độ To, Độ Cao & Phản Xạ Âm',
                  'desc': 'Điều chỉnh biên độ (độ to dB), tần số (độ cao Hz), tính khoảng cách bằng tiếng vang và '
                          'chống ô nhiễm tiếng ồn.'},
 'game_anhsang': {'file': 'games/game_anhsang.html',
                  'title': 'Điện Mặt Trời – Ánh Sáng, Tia Sáng & Sự Phản Xạ Ánh Sáng',
                  'desc': "Căn chỉnh góc tới i và góc phản xạ i' = i để điều hướng chùm tia sáng hội tụ về tấm pin mặt "
                          'trời.'},
 'game_guongphang': {'file': 'games/game_guongphang.html',
                     'title': 'Gương An Ninh – Ảnh Của Vật Qua Gương Phẳng',
                     'desc': 'Dựng ảnh ảo qua gương phẳng, xác định vùng quan sát và bố trí gương cầu/gương phẳng tại '
                             'khúc cua hầm xe.'},
 'game_anhsangmau': {'file': 'games/game_anhsangmau.html',
                     'title': 'Chiếu Sáng Đô Thị – Tán Sắc Ánh Sáng & Màu Sắc Các Vật',
                     'desc': 'Phân tích ánh sáng trắng qua lăng kính, phối hợp các ánh sáng màu cơ bản và khảo sát màu '
                             'sắc vật dưới ánh sáng màu.'},
 'game_namcham': {'file': 'games/game_namcham.html',
                  'title': 'Nam Châm & Từ Trường – Cực Từ & Đường Sức Từ',
                  'desc': 'Xác định cực Bắc (N) – Nam (S) của nam châm, tương tác giữa các cực từ và hình dạng đường '
                          'sức từ.'},
 'game_nam_cham_dien': {'file': 'games/game_nam_cham_dien.html',
                        'title': 'Nam Châm Điện & Từ Trường Trái Đất – La Bàn & Lực Từ F ∝ N·I',
                        'desc': 'Sử dụng la bàn định hướng theo từ trường Trái Đất và điều chỉnh số vòng dây N, dòng '
                                'điện I của nam châm điện.'},
 'simulation_classic:khoi-luong-rieng': {'file': 'games/simulation_classic.html?topic=khoi-luong-rieng',
                                         'title': 'Xưởng Đúc & Kiểm Định Vật Liệu – Khối Lượng Riêng D = m / V',
                                         'desc': 'Đo khối lượng m và thể tích V bằng cân và bình chia độ để xác định '
                                                 'khối lượng riêng D = m/V và trọng lượng riêng d = 10D.'},
 'simulation:luc-day-archimedes': {'file': 'games/simulation.html?topic=luc-day-archimedes',
                                   'title': 'Bến Sông: Thuyền Chở Hàng – Lực Đẩy Archimedes FA = d · V',
                                   'desc': 'Tính toán lực đẩy Archimedes FA = d·V và mớn nước của thuyền khi chở hàng '
                                           'qua sông nước ngọt và ra biển nước mặn.'},
 'game_chat_luu': {'file': 'games/game_chat_luu.html',
                   'title': 'Trung Tâm Thủy Lực – Áp Suất p = F / S, Áp Suất Chất Lỏng & Khí Quyển',
                   'desc': 'Khảo sát áp suất trên một bề mặt p = F/S, áp suất chất lỏng p = d·h, máy nén thủy lực và '
                           'lực cản chất lưu.'},
 'game_moment_luc_don_bay': {'file': 'games/game_moment_luc_don_bay.html',
                             'title': 'Xưởng Đòn Bẩy – Moment Lực M = F · d & Quy Tắc Đòn Bẩy',
                             'desc': 'Vận dụng tác dụng làm quay của lực, tính moment lực M = F·d và điều kiện cân '
                                     'bằng đòn bẩy F₁·d₁ = F₂·d₂.'},
 'game_dien': {'file': 'games/game_dien.html',
               'title': 'Thợ Điện Khu Phố – Sự Nhiễm Điện, Dòng Điện, Mạch Điện & Đo I, U',
               'desc': 'Lắp mạch điện đơn giản, khảo sát các tác dụng của dòng điện và dùng ampe kế, vôn kế đo cường '
                       'độ dòng điện I, hiệu điện thế U.'},
 'game_nhietnang': {'file': 'games/game_nhietnang.html',
                    'title': 'Chuyến Giao Nóng Mùa Đông – Năng Lượng Nhiệt, Truyền Nhiệt & Nở Vì Nhiệt',
                    'desc': 'Phân tích nội năng, 3 hình thức truyền nhiệt (dẫn nhiệt, đối lưu, bức xạ nhiệt) và sự nở '
                            'vì nhiệt của chất rắn, lỏng, khí.'},
 'game_congsuat': {'file': 'games/game_congsuat.html',
                   'title': 'Tời Điện Nhà Phố – Công Cơ Học A = F · s & Công Suất P = A / t',
                   'desc': 'Tính công cơ học A = F·s và công suất P = A/t để vận hành hệ thống tời nâng vật liệu xây '
                           'dựng an toàn, hiệu quả.'},
 'game_co_nang_khuc_xa': {'file': 'games/game_co_nang_khuc_xa.html',
                          'title': 'Năng Lượng & Ánh Sáng – Cơ Năng, Khúc Xạ Ánh Sáng & Phản Xạ Toàn Phần',
                          'desc': 'Khảo sát sự chuyển hóa động năng – thế năng, định luật khúc xạ ánh sáng n₁sin i = '
                                  'n₂sin r và góc giới hạn phản xạ toàn phần.'},
 'game_quanghoc': {'file': 'games/game_quanghoc.html',
                   'title': 'Góc Máy Nét Căng – Thấu Kính Hội Tụ, Thấu Kính Phân Kì & Kính Lúp',
                   'desc': 'Điều chỉnh tiêu cự f và khoảng cách vật d để tạo ảnh rõ nét qua thấu kính hội tụ, thấu '
                           'kính phân kì và kính lúp.'},
 'game_ohm': {'file': 'games/game_ohm.html',
              'title': 'Cứu Bảng Hiệu LED – Điện Trở & Định Luật Ohm I = U / R',
              'desc': 'Tính toán điện trở dây dẫn R = ρℓ/S và chọn điện trở hạn dòng theo định luật Ohm I = U/R để bảo '
                      'vệ mạch đèn LED.'},
 'game_doanmachnoitiep': {'file': 'games/game_doanmachnoitiep.html',
                          'title': 'Thợ Đèn Nối Tiếp – Đoạn Mạch Nối Tiếp (I = I₁ = I₂, Rtd = R₁ + R₂)',
                          'desc': 'Thiết kế và tính toán cường độ dòng điện, hiệu điện thế và điện trở tương đương '
                                  'trong đoạn mạch mắc nối tiếp.'},
 'game_doanmachsongsong': {'file': 'games/game_doanmachsongsong.html',
                           'title': 'Mạng Điện Nhà Mình – Đoạn Mạch Song Song (U = U₁ = U₂, 1/Rtd = 1/R₁ + 1/R₂)',
                           'desc': 'Lắp đặt và cân bằng tải cho mạng điện sinh hoạt mắc song song đảm bảo các thiết bị '
                                   'hoạt động đúng hiệu điện thế định mức.'},
 'game_congsuatdien': {'file': 'games/game_congsuatdien.html',
                       'title': 'Săn Watt – Năng Lượng Điện W = UIt, Công Suất P = UI & Định Luật Joule – Lenz',
                       'desc': 'Tính công suất tiêu thụ điện P = U·I = I²R, nhiệt lượng tỏa ra Q = I²Rt và số tiền '
                               'điện tiêu thụ (kWh).'},
 'game_dientu': {'file': 'games/game_dientu.html',
                 'title': 'Điện Về Bản – Cảm Ứng Điện Từ, Dòng Điện Xoay Chiều & Máy Biến Áp',
                 'desc': 'Khảo sát điều kiện xuất hiện dòng điện cảm ứng, nguyên tắc máy phát điện xoay chiều và '
                         'truyền tải điện năng bằng máy biến áp.'},
 'game_robot': {'file': 'games/game_robot.html',
                'title': 'Robot Giao Hàng – Độ Dịch Chuyển, Vận Tốc & Chuyển Động Thẳng Đều',
                'desc': 'Lập trình lộ trình cho robot giao hàng bằng độ dịch chuyển d, vận tốc v và đồ thị độ dịch '
                        'chuyển – thời gian (d – t).'},
 'game_giatoc': {'file': 'games/game_giatoc.html',
                 'title': 'Đường Đua Neon – Gia Tốc, Chuyển Động Biến Đổi Đều, Rơi Tự Do & Chuyển Động Ném',
                 'desc': 'Tính gia tốc a = Δv/Δt, quãng đường s = v₀t + ½at², vận tốc v² - v₀² = 2as, sự rơi tự do và '
                         'tầm bay xa của chuyển động ném.'},
 'force_real_life_game': {'file': 'games/force_real_life_game.html',
                          'title': 'Đêm Nhạc Hội Trường – Tổng Hợp Lực, Cân Bằng Lực & Lực Ma Sát Trên Mặt Nghiêng',
                          'desc': 'Phân tích lực kéo trên mặt phẳng nghiêng, tổng hợp hai lực đồng quy, cân bằng lực '
                                  'căng dây cáp và nguyên lý phanh ABS.'},
 'game_newton': {'file': 'games/game_newton.html',
                 'title': 'Trạm Hỏa Tinh – Ba Định Luật Newton, Trọng Lực & Lực Căng Dây',
                 'desc': 'Vận dụng quán tính (Định luật 1), gia tốc a = F/m (Định luật 2) và cặp lực – phản lực (Định '
                         'luật 3 Newton) trong trạm vũ trụ.'},
 'game_nang_luong': {'file': 'games/game_nang_luong.html',
                     'title': 'Trạm Điều Phối Năng Lượng – Công A = F·s·cosα, Cơ Năng & Hiệu Suất',
                     'desc': 'Tính công cơ học, công suất, động năng Wđ = ½mv², thế năng Wt = mgh, định luật bảo toàn '
                             'cơ năng và hiệu suất H.'},
 'game_dong_luong': {'file': 'games/game_dong_luong.html',
                     'title': 'Phòng Thí Nghiệm Va Chạm – Động Lượng p = mv & Định Luật Bảo Toàn Động Lượng',
                     'desc': 'Khảo sát xung lượng của lực F·Δt = Δp, định luật bảo toàn động lượng trong va chạm đàn '
                             'hồi, va chạm mềm và chuyển động bằng phản lực.'},
 'game_chuyen_dong_tron_lo_xo': {'file': 'games/game_chuyen_dong_tron_lo_xo.html',
                                 'title': 'Xưởng Cơ Học Lưu Động – Chuyển Động Tròn Đều, Lực Hướng Tâm, Moment Lực & '
                                          'Định Luật Hooke',
                                 'desc': 'Tính tốc độ góc ω, gia tốc hướng tâm aht = v²/r, lực hướng tâm, quy tắc '
                                         'moment lực cân bằng vật rắn và lực đàn hồi F = k|Δℓ|.'},
 'game_dao_dong': {'file': 'games/game_dao_dong.html',
                   'title': 'Viện Nhịp Điệu – Dao Động Điều Hòa, Con Lắc, Năng Lượng & Cộng Hưởng',
                   'desc': 'Điều chỉnh biên độ A, tần số góc ω, pha ban đầu φ, chu kì con lắc lò xo – con lắc đơn và '
                           'khảo sát hiện tượng cộng hưởng.'},
 'game_song_co': {'file': 'games/game_song_co.html',
                  'title': 'Viện Âm Vang – Sóng Cơ Học, Bước Sóng λ = v/f, Sóng Ngang & Sóng Dọc',
                  'desc': 'Đo bước sóng λ = v·T = v/f, tốc độ truyền sóng, độ lệch pha và sự truyền năng lượng của '
                          'sóng cơ học.'},
 'game_song_dien_tu_giao_thoa_tu_dien': {'file': 'games/game_song_dien_tu_giao_thoa_tu_dien.html',
                                         'title': 'Đội Săn Sóng – Sóng Điện Từ, Giao Thoa Sóng Cơ, Giao Thoa Ánh Sáng '
                                                  'Young & Sóng Dừng',
                                         'desc': 'Xác định cực đại – cực tiểu giao thoa sóng cơ, khoảng vân giao thoa '
                                                 'ánh sáng i = λD/a, điều kiện sóng dừng và phổ sóng điện từ.'},
 'game_dien_truong': {'file': 'games/game_dien_truong.html',
                      'title': 'Xưởng Tia Lửa – Định Luật Coulomb & Cường Độ Điện Trường E = k|Q|/r²',
                      'desc': 'Tính lực tương tác tĩnh điện Coulomb F = k|q₁q₂|/r², vectơ cường độ điện trường và '
                              'nguyên lý chồng chất điện trường.'},
 'game_dien_truong_deu': {'file': 'games/game_dien_truong_deu.html',
                          'title': 'Phòng Lái Tia – Điện Trường Đều E = U/d & Quỹ Đạo Hạt Mang Điện',
                          'desc': 'Điều khiển hiệu điện thế U giữa hai bản phẳng song song để lái chùm hạt mang điện '
                                  'chuyển động theo quỹ đạo parabol trúng đích.'},
 'game_dien_the': {'file': 'games/game_dien_the.html',
                   'title': 'Biệt Đội Electron-Volt – Thế Năng Điện, Điện Thế, Hiệu Điện Thế & Tụ Điện W = ½CU²',
                   'desc': 'Tính công của lực điện A = qEd = qU, điện thế V, điện dung của tụ điện C = Q/U và năng '
                           'lượng điện trường trong tụ điện.'},
 'game_dong_dien': {'file': 'games/game_dong_dien.html',
                    'title': 'Xưởng Mạch Đồng – Cường Độ Dòng Điện I = Snve, Định Luật Ohm Toàn Mạch I = E/(R+r)',
                    'desc': 'Khảo sát dòng điện không đổi, sự phụ thuộc điện trở vào nhiệt độ, suất điện động E, định '
                            'luật Ohm toàn mạch và đo E, r của nguồn điện.'},
 'game_vat_ly_nhiet_khi_ly_tuong': {'file': 'games/game_vat_ly_nhiet_khi_ly_tuong.html',
                                    'title': 'Biệt Đội Nhiệt Động – Vật Lí Nhiệt (ΔU = A+Q, c, λ, L) & Khí Lí Tưởng '
                                             '(pV = nRT)',
                                    'desc': 'Thực hành đo nhiệt dung riêng c, nhiệt nóng chảy riêng λ, nhiệt hóa hơi '
                                            'riêng L và kiểm nghiệm định luật Boyle, Charles, phương trình pV = nRT.'},
 'game_tu_truong': {'file': 'games/game_tu_truong.html',
                    'title': 'Viện Nam Châm – Từ Trường, Cảm Ứng Từ B & Lực Từ F = BILsinθ',
                    'desc': 'Xác định quy tắc bàn tay trái, độ lớn lực từ F = BILsinθ tác dụng lên đoạn dây dẫn mang '
                            'dòng điện và cân từ trường.'},
 'game_cam_ung_dien_tu': {'file': 'games/game_cam_ung_dien_tu.html',
                          'title': 'Trạm Cảm Ứng – Từ Thông Φ = NBScosα, Định Luật Faraday & Định Luật Lenz',
                          'desc': 'Tính từ thông Φ và suất điện động cảm ứng e_c = -ΔΦ/Δt khi cho khung dây quay hoặc '
                                  'dịch chuyển trong từ trường.'},
 'game_mach_xoay_chieu': {'file': 'games/game_mach_xoay_chieu.html',
                          'title': 'Đội Điều Độ Xoay Chiều – Dòng Điện Xoay Chiều, Giá Trị Hiệu Dụng & Hệ Số Công Suất '
                                   'cosφ',
                          'desc': 'Tính giá trị hiệu dụng I = I₀/√2, U = U₀/√2, chu kì, tần số và công suất tiêu thụ P '
                                  '= UIcosφ của mạch điện xoay chiều.'},
 'game_mach_rlc': {'file': 'games/game_mach_rlc.html',
                   'title': 'Trạm Dò Sóng – Mạch RLC Nối Tiếp, Cộng Hưởng Điện, Máy Biến Áp & Sóng Điện Từ',
                   'desc': 'Điều chỉnh tổng trở Z, tần số cộng hưởng điện ZL = ZC, tỉ số máy biến áp U₁/U₂ = N₁/N₂ và '
                           'giảm hao phí truyền tải điện năng.'},
 'game_hat_nhan': {'file': 'games/game_hat_nhan.html',
                   'title': 'Trạm Đồng Vị – Cấu Trúc Hạt Nhân, Phản Ứng Phân Hạch – Nhiệt Hạch & Định Luật Phóng Xạ',
                   'desc': 'Cân bằng phương trình phản ứng hạt nhân, tính chu kì bán rã T, độ phóng xạ H = λN và ứng '
                           'dụng đồng vị phóng xạ an toàn.'},
 'game_thuyet_tuong_doi': {'file': 'games/game_thuyet_tuong_doi.html',
                           'title': 'Trạm Ánh Sáng – Hệ Thức Einstein E = mc², Độ Hụt Khối Δm & Năng Lượng Liên Kết',
                           'desc': 'Tính độ hụt khối Δm, năng lượng liên kết Wlk = Δm·c², năng lượng liên kết riêng và '
                                   'hệ thức tương đối tính Einstein.'},
 'game_quang_dien': {'file': 'games/game_quang_dien.html',
                     'title': 'Xưởng Photon – Lượng Tử Ánh Sáng ε = hf, Hiện Tượng Quang Điện & Mẫu Nguyên Tử Bohr',
                     'desc': 'Khảo sát năng lượng photon ε = hc/λ, giới hạn quang điện λ₀ và sự chuyển mức năng lượng '
                             'electron trong nguyên tử.'}}


def choose_game_key(subject: str, grade: int, topic: str, title: str) -> str | None:
    tp = str(topic or "").strip().lower()
    ti = str(title or "").strip().lower()
    g = int(grade or 0)

    # 1. VẬT LÝ (LỚP 6 – 12): Ánh xạ theo từng bài học cụ thể; bài chưa có game trả về None
    if subject == "physics":
        if g == 6:
            if "chiều dài" in ti: return "game_dodai"
            if "khối lượng" in ti: return "game_khoiluong"
            if "thời gian" in ti: return "game_do_luong"
            if "nhiệt độ" in ti: return "game_nhietdo"
            if "trọng lực" in ti: return "game_trong_luong_nang_luong"
            if "ma sát" in ti or "lực cản" in ti: return "game_lucmasat"
            if "lực" in ti or "lò xo" in ti: return "game_luc"
            if "năng lượng" in ti: return "game_trong_luong_nang_luong"
            if "mặt trời" in ti: return "game_anhsang"
            return None
        if g == 7:
            if "tốc độ" in ti or "quãng đường" in ti: return "game_speed"
            if "âm" in ti: return "game_amthanh"
            if "gương phẳng" in ti: return "game_guongphang"
            if "ánh sáng" in ti or "phản xạ" in ti: return "game_anhsang"
            if "trái đất" in ti or "la bàn" in ti or "nam châm điện" in ti: return "game_nam_cham_dien"
            if "nam châm" in ti or "từ trường" in ti: return "game_namcham"
            return None
        if g == 8:
            if "khối lượng riêng" in ti: return "simulation_classic:khoi-luong-rieng"
            if "archimedes" in ti: return "simulation:luc-day-archimedes"
            if "áp suất" in ti: return "game_chat_luu"
            if "moment" in ti or "đòn bẩy" in ti: return "game_moment_luc_don_bay"
            if "điện" in ti or "mạch" in ti: return "game_dien"
            if "nhiệt" in ti: return "game_nhietnang"
            return None
        if g == 9:
            if ("công" in ti and "công suất" in ti and "điện" not in ti): return "game_congsuat"
            if "động năng" in ti or "thế năng" in ti or "cơ năng" in ti or "khúc xạ" in ti or "phản xạ toàn phần" in ti:
                return "game_co_nang_khuc_xa"
            if "tán sắc" in ti or "màu sắc" in ti: return "game_anhsangmau"
            if "thấu kính" in ti or "kính lúp" in ti: return "game_quanghoc"
            if "ohm" in ti or "điện trở" in ti: return "game_ohm"
            if "nối tiếp" in ti: return "game_doanmachnoitiep"
            if "song song" in ti: return "game_doanmachsongsong"
            if "công suất điện" in ti or "năng lượng điện" in ti: return "game_congsuatdien"
            if "cảm ứng điện từ" in ti or "xoay chiều" in ti or "máy biến áp" in ti: return "game_dientu"
            if "năng lượng tái tạo" in ti or "hóa thạch" in ti: return "game_nang_luong"
            return None
        if g == 10:
            if "sai số" in ti or "phép đo" in ti: return "game_dodai"
            if "độ dịch chuyển" in ti or "tốc độ và vận tốc" in ti: return "game_robot"
            if "gia tốc" in ti or "biến đổi đều" in ti or "rơi tự do" in ti or "chuyển động ném" in ti: return "game_giatoc"
            if "tổng hợp" in ti or "ma sát" in ti: return "force_real_life_game"
            if "lực cản" in ti or "áp suất chất lỏng" in ti: return "game_chat_luu"
            if "newton" in ti or "trọng lực" in ti: return "game_newton"
            if "công" in ti or "động năng" in ti or "cơ năng" in ti: return "game_nang_luong"
            if "động lượng" in ti: return "game_dong_luong"
            if "tròn đều" in ti or "hướng tâm" in ti or "moment" in ti or "lò xo" in ti or "hooke" in ti:
                return "game_chuyen_dong_tron_lo_xo"
            return None
        if g == 11:
            if "dao động" in ti or "cộng hưởng" in ti: return "game_dao_dong"
            if "mô tả sóng" in ti or "sóng ngang" in ti: return "game_song_co"
            if "sóng điện từ" in ti or "giao thoa" in ti or "sóng dừng" in ti: return "game_song_dien_tu_giao_thoa_tu_dien"
            if "coulomb" in ti or "cường độ điện trường" in ti: return "game_dien_truong"
            if "điện trường đều" in ti: return "game_dien_truong_deu"
            if "thế năng điện" in ti or "điện thế" in ti or "tụ điện" in ti: return "game_dien_the"
            if "dòng điện" in ti or "điện trở" in ti or "nguồn điện" in ti or "suất điện động" in ti or "toàn mạch" in ti or "công suất điện" in ti:
                return "game_dong_dien"
            return None
        if g == 12:
            if tp in ("l12-ch01-vat-li-nhiet", "l12-ch02-khi-li-tuong"): return "game_vat_ly_nhiet_khi_ly_tuong"
            if "từ trường" in ti or "cảm ứng từ" in ti: return "game_tu_truong"
            if "cảm ứng điện từ" in ti or "từ thông" in ti: return "game_cam_ung_dien_tu"
            if "xoay chiều" in ti: return "game_mach_xoay_chieu"
            if "máy biến áp" in ti or "rlc" in ti: return "game_mach_rlc"
            if "einstein" in ti: return "game_thuyet_tuong_doi"
            if "hạt nhân" in ti or "phóng xạ" in ti or "phân hạch" in ti or "nhiệt hạch" in ti: return "game_hat_nhan"
            return None
        return None

    # 2. HÓA HỌC (LỚP 6 – 12): Hiện chưa có mini-game Hóa học riêng → "Đang xây dựng"
    if subject == "chemistry":
        return None

    # 3. TOÁN HỌC (LỚP 1 – 12): Chỉ gắn cho bài học khớp nội dung game; bài chưa có game trả về None
    if g == 12:
        if any(k in ti for k in ("đơn điệu", "cực trị", "giá trị lớn nhất", "tiệm cận", "khảo sát")):
            return "game_ung_dung_dao_ham"
        if any(k in ti for k in ("vectơ", "tọa độ", "đường thẳng", "mặt phẳng", "mặt cầu")):
            return "game_toa_do_oxyz"
        if any(k in ti for k in ("nguyên hàm", "tích phân")):
            return "game_nguyen_ham"
        if any(k in ti for k in ("khoảng biến thiên", "phương sai", "độ lệch chuẩn", "xác suất có điều kiện", "bayes")):
            return "game_on_tap_thpt"
        return None
    if g == 11:
        if any(k in ti for k in ("giới hạn", "liên tục", "đạo hàm", "tiếp tuyến")):
            return "function-challenge"
        if any(k in ti for k in ("mũ", "lôgarit", "xác suất", "mẫu số liệu ghép nhóm")):
            return "game_on_tap_thpt"
        return None
    if g == 10:
        if any(k in ti for k in ("vectơ", "tọa độ", "tích vô hướng")):
            return "game_toa_do_oxyz"
        if any(k in ti for k in ("tổ hợp", "chỉnh hợp", "hoán vị", "xác suất")):
            return "game_on_tap_thpt"
        if any(k in ti for k in ("hàm số", "thống kê", "số gần đúng", "trung vị", "phương sai")):
            return "store_management"
        return None
    if g in (6, 7, 8, 9):
        if any(k in ti for k in ("tiền", "lãi", "phần trăm", "hệ phương trình", "hàm số bậc nhất", "hàm số y = ax", "thống kê", "biểu đồ", "tần số")):
            return "store_management"
        return None
    if g == 5:
        if any(k in ti for k in ("vận tốc", "quãng đường", "chuyển động đều")):
            return "game_speed"
    if any(k in ti for k in ("tiền việt nam", "tỉ số phần trăm")):
        return "store_management"
    if any(k in ti for k in ("khối lượng", "ki-lô-gam", "gam", "tấn, tạ, yến")):
        return "game_khoiluong"
    if any(k in ti for k in ("độ dài", "xăng-ti-mét", "mét", "đồng hồ", "xem giờ", "thời gian", "ngày, giờ", "chu vi", "diện tích", "thể tích", "đo góc")):
        return "game_do_luong"
    return None


def resolve_backend_game(subject: str, grade: int, lesson: dict) -> tuple[str | None, str | None, str | None]:
    key = choose_game_key(subject, grade, lesson.get("topic", ""), lesson.get("title", ""))
    if not key or key not in GAME_META:
        return None, None, None
    meta = GAME_META[key]
    return key, meta["title"], meta["desc"]
