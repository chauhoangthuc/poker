# Nâng cấp phòng chơi — 30/10/2026

Đã triển khai phòng chờ/đang chơi mô phỏng cùng một bố cục, chat phải và drawer ở màn nhỏ, bốn ghế, chọn bài SVG, xếp bài, bỏ lượt, đánh bài có kiểm tra lựa chọn cơ bản. Button/IconButton và token tại `app/src/Button.tsx`, `button.tokens.css`; UI kit tại `/ui-kit`. Các button native cũ đã chuyển sang Button; một số class bố cục tương thích của sảnh vẫn giữ trong styles.css.

Kiểm tra thực: typecheck, lint, production build pass. Playwright 8/8 pass gồm 6 luồng cũ và hai test mới cho ván demo/UI kit. Chromium DPR 1 chụp ở 1586×992, 1280×800, 768×1024, 390×844; font check true và không tràn ngang ở cả bốn. Vite đã phải khởi động lại với quyền ghi file tạm sau lỗi sandbox EPERM.

Ảnh: `arena/room-1586.png`, `room-1280.png`, `room-768.png`, `room-390.png`, `ui-kit.png`. Đối chiếu ảnh tham chiếu mới tại `arena/comparison/`. Đã xem screenshot desktop/mobile, sửa chất liệu viền bàn, nâng cụm bài giữa bàn và chỉnh timer sang bên avatar trước lần chụp cuối.

Khác biệt còn lại: phong cảnh sáng hơn mẫu, viền bàn và chân dung khác; mặt J/Q/K dùng SVG ký hiệu đơn giản; bài trên tay không xòe cong như mẫu. Timer 18s tĩnh, âm thanh chỉ toggle, luật chơi chỉ mô phỏng bài lẻ/nhóm cùng hạng. Không chấm phần trăm giống ảnh hoặc tuyên bố pixel-perfect. Các asset mới là PNG gốc, không phải WebP. Avatar hiện có được dùng lại.

Chưa kiểm chứng tự động toàn bộ contrast và mọi tổ hợp focus của UI kit. Focus-visible, disabled/loading và reduced motion đã có trong component; test xác nhận nút disabled/loading không được kích hoạt.

## Lượt sửa sau phản hồi về độ giống
Đã thay phong cảnh bằng room-background-v2.png, bổ sung subset Latin Be Vietnam Pro đủ 400–800, giảm chiều cao bàn, làm nỉ tối/mịn hơn, thêm các lớp mép bàn, căn lại ghế/bài/action dock, xòe bài và thêm hình quân J/Q/K SVG. Đã chụp lại bốn viewport, mở ảnh actual và overlay cuối để kiểm tra. Mặt bài và phong cảnh vẫn khác mẫu; không tuyên bố khớp hoàn toàn.
Typecheck, lint và 8/8 E2E pass. Build mặc định gặp EPERM khi xóa dist/assets cũ; npm run build -- --outDir dist-review pass (1597 modules). Screenshot và overlay trong arena/ được cập nhật. Không tràn ngang cả bốn viewport. Các nhận xét trước đó về mặt bài chỉ có ký hiệu đã được thay thế bởi hình quân SVG mới.

## Lượt sửa bàn/bài/button/chat tiếp theo
Thay 12 mặt J/Q/K bằng SVG public domain truyền thống (thay phần court tự vẽ), làm lại mép bàn liền với chất liệu khắc chìm, loại bỏ sọc chân bàn, nỉ teal mềm hơn; button dùng khung vát kim loại và mặt kính tập trung trong token chung. Chat có nền navy đặc, bubble gradient nhẹ và khoảng cách mới. Desktop co theo chiều cao viewport để giữ bài/action dock; kiểm tra 1586×992,1280×800,768×1024,390×844 không tràn ngang. Đã mở ảnh desktop và desktop nhỏ; sửa dòng phụ CTA bị chật ở cửa sổ thấp rồi chụp lại.
Typecheck/lint/8 E2E pass. Production build bằng npm run build -- --outDir dist-review --emptyOutDir false pass. Mặt bài mới có index nhỏ hơn ảnh tham chiếu; cảnh nền/avatar và chi tiết viền còn khác. Không tuyên bố giống hoàn toàn.

## Kiểm tra PNG nút — 30/10/2026
- Tạo và xem ba PNG ImageGen trước khi tích hợp: play, violet, navy. Nút Đánh bài có khoang bích, mặt kính cyan, viền kim loại; nội dung và tương tác vẫn là button HTML.
- `npm run typecheck`: PASS. `npm run lint`: PASS.
- `npm run test:e2e`: 8/8 PASS (11.1s), bao gồm chọn/đánh/bỏ lượt và disabled/loading.
- `npm run build -- --outDir dist-review --emptyOutDir false`: PASS sau khi chạy với quyền bổ sung; lần chạy sandbox bị EPERM khi Vite ghi node_modules/.vite-temp. Không thay đổi dependency.
- `node tests/arena-capture.mjs`: Chromium DPR1, 1586×992, 1280×800, 768×1024, 390×844; đợi font, ảnh DOM và cả ba skin PNG decode. Không tràn ngang ở cả bốn viewport. Đã xem ảnh desktop và mobile; sửa vị trí nút mở chat để không đè nút đánh bài.
- `qa/compare_reference.py`: tạo lại overlay và side-by-side, đã xem overlay trực tiếp. Không dùng điểm diff làm tỷ lệ giống.
- Còn khác: mặt bàn và chiều sâu thành bàn, artwork nền/avatar, họa tiết lưng bài; mặt quân J/Q/K và font chữ số không trùng mẫu. Dock thấp hơn mẫu khoảng 12px ở 1586×992, khung chat cao hơn mẫu ở mép dưới. PNG nút gần chất liệu mẫu hơn nhưng không trùng từng pixel. Chưa tuyên bố hoàn tất độ giống toàn màn hình.

## Bàn và lưng bài ImageGen — 30/10/2026
- Tạo riêng table-render.png (bàn trống nền trong suốt) và cards/back-render.png từ tham chiếu người dùng bằng OpenAI ImageGen. Giữ bản gốc; back-render-small.png là bản thu nhỏ Lanczos 128×192 để giảm răng cưa khi hiển thị. Các asset này không chứa UI, người chơi, nút hoặc chữ gameplay.
- Tích hợp arena-artwork.css: bàn PNG thay các lớp CSS giả chất liệu; lưng bài PNG thay họa tiết vòng tròn; xòe bài ở ghế trên. Mặt bài ngửa không thay bằng ImageGen trong lần này.
- Typecheck PASS; lint PASS; Playwright 8/8 PASS (11.6s); production build PASS (outDir dist-review, quyền bổ sung để Vite ghi .vite-temp).
- Chụp lại Chromium DPR1 ở 1586×992,1280×800,768×1024,390×844 sau khi font và asset decode. Không tràn ngang. Đã xem ảnh desktop và mobile. Overlay được tạo lại.
- Còn khác tham chiếu: hình dáng và độ sáng thành bàn, biểu tượng bích giữa bàn, mẫu hoa văn lưng bài; mặt bài ngửa, avatar và background vẫn khác. Mobile co giãn bàn theo vùng chơi nên tỷ lệ ellipse khác desktop. Không tuyên bố khớp tuyệt đối.

## Lobby artwork 30/10/2026
ImageGen generated lobby-icons.png (six decorative icons). Existing ImageGen navy/violet button skins reused for lobby actions. Text and behavior remain HTML. Typecheck/lint PASS, E2E 8/8 PASS (11.3s), production build PASS to dist-review. Chromium 1586×992 DPR1 screenshot qa/lobby-artwork.png inspected after fonts and PNG decode. This iteration did not capture mobile lobby. Other navigation icons remain Lucide; no claim all icons replaced.

Room action polish: reused ImageGen navy/violet PNG skins. Join label and arrow inline; disabled labels readable silver. Typecheck/lint and 8 E2E tests passed. Build passed before final text-color CSS correction; final screenshot 1586x992 inspected after correction.

Leaderboard redesign 30/10/2026: generated and inspected ImageGen stage before integration; gold/silver/bronze top-three cards and highlighted own rank. Typecheck, lint, 8/8 E2E (11.3s), production build PASS. Screenshot qa/leaderboard-artwork.png at 1586x992 DPR1 inspected after font and artwork decode. Capture initially failed due to incorrect preload filename; fixed and rerun successfully. Mobile styling implemented but not screenshot-verified this iteration.
