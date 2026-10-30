# Tiến Lên Miền Nam — bộ bàn giao thiết kế cho Codex

Đã chốt: **02 — Đấu trường đêm**, theo `reference/selected-ui.png`.
Ứng dụng prototype đã được triển khai trong [`app/`](app/). Xem [`app/README.md`](app/README.md) để chạy và [`qa/QA_REPORT.md`](qa/QA_REPORT.md) để xem kết quả nghiệm thu.

## Cách dùng
1. Giải nén toàn bộ, mở thư mục này trong workspace của Codex.
2. Gửi nội dung `PROMPT_FOR_CODEX.md` cho Codex.
3. `cd app`, chạy `npm ci`, rồi `npm run dev`.
4. Mở `http://localhost:5173/lobby`.

## Các tài liệu
- `PROMPT_FOR_CODEX.md`: yêu cầu thực thi có thể dán trực tiếp.
- `DESIGN_SPEC.md`: font, màu, kích thước, bố cục và responsive.
- `BUILD_PLAN.md`: kiến trúc, các bước build và điểm kiểm tra.
- `INTERACTIONS.md`: hành vi và quy tắc mock data.
- `ASSET_PLAN.md`: các hình cần chuẩn bị; tránh dùng icon thay artwork.
- `qa/ACCEPTANCE.md`: checklist chức năng và độ giống ảnh.
- `qa/compare_reference.py`: tạo ảnh overlay và ảnh khác biệt để kiểm tra.
- `qa/REPORT_TEMPLATE.md`: mẫu báo cáo kết quả thực tế.
- `design/tokens.css`: CSS variables khởi đầu, dùng được với Tailwind.
- `data/rooms.json`: dữ liệu phòng mẫu nhất quán với ảnh.
- `reference/selected-ui.png`: ảnh tham chiếu gốc, không chỉnh sửa.

Font được chọn theo độ phù hợp, không khẳng định đã nhận diện chính xác font trong ảnh AI. Màu và kích thước là thông số triển khai đề xuất sau khi quan sát ảnh, không phải file thiết kế gốc. Các trang phòng chơi, đăng nhập, xếp hạng chưa có ảnh tham chiếu; triển khai nhất quán theo hệ thống này.

Artwork và font đã được thêm cục bộ trong `app/public/assets/`. Screenshot và overlay đối chiếu ở `qa/screenshots/` và `qa/comparison/`. Không coi bản build là pixel-perfect; chi tiết artwork và chân dung tổng hợp khác ảnh tham chiếu.
