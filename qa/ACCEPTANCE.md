# Checklist nghiệm thu

## Cách chụp
1. Chromium desktop, viewport 1586×992 CSS px, deviceScaleFactor=1, zoom 100%, locale vi-VN. Dùng fixture seed nguyên bản, user Hoàng Thúc; đóng toast/modal; không hover card.
2. Chờ document.fonts.ready và tất cả img decode/load, chờ skeleton kết thúc. Tắt motion bằng prefers-reduced-motion hoặc stylesheet screenshot. Screenshot viewport, không fullPage cho ảnh đối chiếu gốc.
3. Chụp /lobby; dùng Python 3 + Pillow: `python qa/compare_reference.py reference/selected-ui.png qa/screenshots/lobby-1586.png --out qa/comparison` từ gốc bộ bàn giao. Script không resize để giấu sai lệch.
4. Mở reference, actual, overlay, diff để so trực quan. Đầu tiên kiểm tra sidebar/topbar/rail/grid; sau đó font, avatar/artwork, màu/glow. Sau mỗi sửa đáng kể chụp lại.
5. Chụp responsive riêng, không so pixel với ảnh desktop. Chụp modal tạo phòng, room, leaderboard, login, empty/loading/error.

## Visual gates
- [ ] Sidebar 246px, topbar 74px, right rail 312px ở viewport gốc; mốc khối lớn lệch không quá khoảng 8px.
- [ ] Đúng 2×2 room grid, khoảng cách ~16px, 4 seat/card; hình không méo.
- [ ] Hero, 3 stats, 3 actions có thứ bậc đúng; heading không wrap ngoài dự kiến.
- [ ] Be Vietnam Pro đã load, tiếng Việt không rơi dấu, weight đúng; kiểm computed style + font loading.
- [ ] Có hero card artwork + sidebar spade artwork + room backgrounds; không thay bằng icon hoặc gradient trống.
- [ ] Không có chữ/nút bị bake vào ảnh. UI là DOM thật.
- [ ] Cyan CTA nổi nhất, violet đang chơi/BXH, full đỏ, xu vàng; không glow dày khắp nền.
- [ ] Không tràn ngang ở tất cả viewport, không che CTA bởi rail/drawer.
- [ ] Modal, bàn chờ, BXH cùng palette/font/radius; không tự đổi style.

## Functional gates (manual hoặc E2E)
- [ ] Create blank/2 chars fail; 3–40 chars pass; chọn 2/3/4, password optional; cancel không mutate.
- [ ] Create -> đúng room, host=current user, 1 seat; reload chính sách local state được README giải thích.
- [ ] Join available -> tăng count đúng một lần; đầy/đang chơi bị chặn; password đúng/sai hoạt động.
- [ ] Quick join bỏ qua locked/full/playing; không có match hiện thông báo.
- [ ] Filters và count đổi theo data; empty filter có reset.
- [ ] Room ready toggle, mời mock, chat local, leave và room invalid hoạt động.
- [ ] Leaderboard route và back; logout -> login; login -> lobby.
- [ ] Friend search/menu/chat, notification có phản hồi nếu hiển thị.
- [ ] Loading, empty, error và retry có thể tái lập.
- [ ] Escape/focus trap/restore focus; tab order; accessible names và focus visible.
- [ ] Console không lỗi, ảnh/font không 404, typecheck/lint/build pass.

## Đánh giá độ giống
Không dùng MAE/pixel diff toàn ảnh làm tỷ lệ “% giống”: ảnh chân dung, artwork và anti-aliasing có thể khác. Chấm có giải thích theo nhóm: layout 35, typography 20, palette/controls 15, artwork/composition 20, chi tiết 10. Mục tiêu nội bộ >=90/100 và không có lỗi lớn ở visual gates; đây là đánh giá thủ công, không phải phép đo khách quan. Ghi điểm sau khi xem screenshot thật, không chấm trước.

Không pass nếu thiếu artwork chính hoặc font, dù chức năng chạy. Khác biệt có chủ đích: nút phòng đang chơi disabled, dữ liệu counts nhất quán, responsive chưa có ảnh gốc. Ghi rõ trong báo cáo.
