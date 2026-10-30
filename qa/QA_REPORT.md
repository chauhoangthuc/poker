# QA_REPORT — prototype Tiến Lên Miền Nam

## Môi trường

- Ngày: 29/10/2026, múi giờ Asia/Bangkok.
- Node.js v24.18.0, npm 11.16.0, Windows; Chromium Playwright revision `1228` (đường dẫn cục bộ được truyền qua `PLAYWRIGHT_CHROMIUM_PATH`).
- Viewport: 1586×992, 1440×900, 1024×768, 768×1024, 390×844; DPR 1, locale `vi-VN`, reduced motion, zoom mặc định 100%.
- Font: local WOFF2 Be Vietnam Pro; script chờ `document.fonts.ready`, kiểm `document.fonts.check('400 16px "Be Vietnam Pro"')` = true trên mọi screenshot, gồm login. Chờ mọi thẻ `img.decode()` trước khi chụp.

## Lệnh đã chạy và kết quả cuối

| Lệnh | Kết quả thực |
|---|---|
| `npm install --no-audit --no-fund` | Pass; 282 packages, tạo `app/package-lock.json`. Lần thử trong sandbox bị chặn socket; chạy lại với quyền mạng thành công. |
| `npm run typecheck` | Pass. |
| `npm run lint` | Pass. |
| `npm run test` | Pass, 1 kiểm tra fixture. |
| `npm run test:e2e` | Pass, 6/6 Playwright tests trên Chromium. Dùng `PLAYWRIGHT_CHROMIUM_PATH` cục bộ. |
| `npm run build` | Pass; Vite 6.4.5, 1591 modules. Lần đầu Vite không ghi được `.vite-temp` trong sandbox; chạy lại với quyền ghi thành công. |
| `node tests/capture.mjs` | Pass; 11 screenshot chính + modal. Không có `pageerror`, response HTTP >=400 hay tràn ngang tại các viewport được chụp. |
| `python qa/compare_reference.py ...` | Pass bằng Python runtime đi kèm Codex; tạo overlay, diff và side-by-side. Script ghi mean absolute diff 22.510/255; **không dùng số này làm % giống**. |

## Visual

- [Ảnh sảnh 1586×992](screenshots/lobby-1586.png), [overlay](comparison/overlay.png), [side-by-side](comparison/side-by-side.png), [diff](comparison/diff-x3.png).
- Screenshot responsive: `screenshots/lobby-1440.png`, `lobby-1024.png`, `lobby-768.png`, `lobby-390.png`; thêm `room.png`, `leaderboard.png`, `login.png`, `create-modal.png`, `empty.png`, `loading.png`, `error.png`.
- Đã mở ảnh gốc, actual và overlay bằng công cụ xem ảnh. Sau vòng chụp đầu, sửa lời chào chỉ dùng “Thúc” cho khớp ảnh, giảm độ lấn sáng của hero artwork, giữ chiều cao ô tìm bạn và sửa topbar tràn ngang ở 768px; chụp lại và xem overlay cuối.
- Mốc shell desktop quan sát đạt: sidebar 246px, topbar 74px, friends rail 312px; grid 2×2 bắt đầu khoảng x=276/y=473, card cao 235px, gap 16px. Chữ, avatar, nút, thẻ phòng đều là DOM riêng.
- Đánh giá thủ công theo checklist: layout **34/35**, typography **18/20**, palette/controls **14/15**, artwork/composition **16/20**, chi tiết **8/10**; tổng **90/100**. Đây là ước lượng sau khi xem screenshot, không phải chỉ số đo tự động.
- Sai khác còn lại: bộ bài hero sáng và kiểu minh họa khác mẫu; bích sidebar nằm thấp hơn, cảnh núi khác; bốn nền phòng và chân dung tổng hợp khác ảnh gốc. Chữ và nút không được bake vào các asset này. Chủ ý đổi nút phòng đang chơi thành disabled để tránh hiểu nhầm, và phòng đầy disabled theo dữ liệu thực.

## Chức năng và accessibility

- E2E đã đi qua lọc phòng/count, tạo phòng 2 người, validation tên, đặt mật khẩu sai/đúng, mời mock, sẵn sàng, chat phòng và chat bạn bè local, rời phòng, tham gia nhanh, chặn phòng đầy/đang chơi qua URL, xếp hạng, logout/login, tìm bạn, Esc, empty/error retry.
- Modal có focus đầu, trap Tab, Esc, khôi phục focus; form có label, toast có `role=status`, nút icon có accessible name. `prefers-reduced-motion` được tôn trọng.
- `loading` được chụp bằng query demo; không kiểm animation sau 400ms vì trạng thái query được cố định để QA tái lập.
- Giới hạn chức năng: local state khôi phục seed khi reload; không có luật bài, backend hoặc đồng bộ người chơi. Password chỉ là demo state.

## Kết luận

Đạt mục tiêu prototype và mức tham chiếu hình ảnh theo rubric thủ công. Không tuyên bố pixel-perfect vì artwork và avatar phải tạo lại từ ảnh phẳng.
