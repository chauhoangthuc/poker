# Tiến Lên Miền Nam — prototype Đấu trường đêm

Bản nâng cấp phòng chơi: mở `/rooms/room-01?demo=playing` để xem ván mô phỏng theo ảnh mới; `/ui-kit` để xem bộ Button/IconButton. Trong bàn chờ, nút “Xem ván demo” mở cùng giao diện. Timer 18s là số minh họa; validation chỉ hỗ trợ bài lẻ hoặc nhóm cùng hạng, chưa xét chặt/chặn và luật Tiến Lên đầy đủ. Nút âm thanh chỉ đổi trạng thái bật/tắt, chưa phát audio.

Prototype React + TypeScript + Vite, Tailwind CSS 3 và Lucide React. Giao diện dựa trên `../reference/selected-ui.png`. Mọi dữ liệu và tương tác chỉ chạy trong trình duyệt; không có backend, thanh toán hay đăng nhập thật.

## Môi trường và chạy

Đã build bằng **Node.js v24.18.0** và npm **11.16.0** trên Windows. Dùng Node 20.19+ hoặc 22.12+ để chạy Vite 6. Cài và khởi động:

```sh
cd app
npm ci
npm run dev
```

Mở `http://localhost:5173/lobby`. Các lệnh kiểm tra: `npm run typecheck`, `npm run lint`, `npm run test`, `npm run build`, `npm run test:e2e`. Cài Chromium cho Playwright bằng `npx playwright install chromium` nếu máy chưa có. Nếu dùng bản Chromium có sẵn ở đường dẫn khác, đặt biến môi trường `PLAYWRIGHT_CHROMIUM_PATH` tới `chrome.exe` trước khi chạy E2E hoặc `node tests/capture.mjs`.

## Route và demo

- `/lobby`: sảnh, lọc phòng, tạo phòng, tham gia nhanh, bạn bè và thông báo.
- `/rooms/:roomId`: bàn chờ, sẵn sàng, mời bạn mock, chat local và rời phòng.
- `/leaderboard`: bảng xếp hạng cố định.
- `/login`: nhập tên hiển thị demo và vào sảnh. Đăng xuất đưa về đây.
- `/friends`: mở danh sách bạn bè ở rail trên desktop; điều hướng Bạn bè mở drawer ở màn hình nhỏ.

Mở `/lobby` trực tiếp trong phiên mới sẽ tự dùng người chơi demo **Hoàng Thúc** để chụp ảnh. Sau khi đăng xuất, route sảnh chuyển về `/login` đến khi người dùng nhập tên và vào lại. Tên hiển thị lưu trong `sessionStorage`; phòng, ghế, chat và trạng thái sẵn sàng chỉ ở React local state, nên **tải lại trang sẽ khôi phục bốn phòng seed**. Mật khẩu phòng chỉ kiểm tra trên state demo, không bảo mật. Các URL `/lobby?state=loading`, `?state=empty` và `?state=error` mô phỏng trạng thái QA; nút Thử lại đưa về sảnh mặc định. Phòng đang chơi và phòng đầy bị chặn khi vào trực tiếp.

## Asset và bản quyền

Artwork và chân dung tổng hợp đã tạo bằng OpenAI image generation; xem `ASSET_CREDITS.md`. Bộ chân dung cố định là một contact sheet và được định vị theo ID bằng CSS. Font Be Vietnam Pro 400/500/600/700/800 được self-host trong `public/assets/fonts`; giấy phép ở `public/assets/fonts/OFL.txt`. Không dùng hotlink.

## Giới hạn

Đây là prototype bàn chờ, không có luật chơi Tiến Lên, đồng bộ nhiều người, tài khoản thật hoặc backend. Artwork sinh ảnh khác ảnh tham chiếu về chi tiết; xem `../qa/QA_REPORT.md` và screenshot/overlay ở `../qa/`.
