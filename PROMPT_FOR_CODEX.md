# Prompt triển khai

Hãy build prototype web Tiến Lên Miền Nam theo bộ tài liệu này. Thiết kế đã chốt là ảnh `reference/selected-ui.png`; không hỏi lại chọn phong cách. Xem ảnh bằng công cụ xem ảnh trước khi viết UI. Đọc README, DESIGN_SPEC, ASSET_PLAN, INTERACTIONS, BUILD_PLAN và qa/ACCEPTANCE.

Tạo ứng dụng đầy đủ trong `app/`: React + TypeScript + Vite, Tailwind CSS, Lucide React. Component tái sử dụng, toàn bộ nội dung người dùng bằng tiếng Việt. Chỉ mock data và local state, không backend, không thanh toán, không cần đăng nhập thật. Hoàn thiện các route /login, /lobby, /rooms/:roomId, /leaderboard. Trang /friends hoặc drawer bạn bè phải hoạt động nếu hiển thị điều hướng đó.

Ưu tiên độ giống sảnh: ba cột, sidebar 246px, topbar 74px, friends rail 312px tại viewport 1586×992, artwork bộ bài bên phải hero và artwork lớn phía dưới sidebar, hai cột phòng, cyan/tím, avatar tròn và viền sáng tiết chế. Không thay ảnh trang trí bằng icon nhỏ. Không dùng toàn bộ ảnh tham chiếu làm background rồi đặt nút đè lên; mọi nội dung, avatar, thẻ và nút phải là thành phần riêng có semantic HTML.

Thực hiện lần lượt các checkpoint trong BUILD_PLAN. Tạo asset cục bộ theo ASSET_PLAN; nếu không tạo được, ghi rõ giới hạn và không tuyên bố hoàn tất độ giống ảnh. Dùng Be Vietnam Pro thật, đủ tiếng Việt và weight; không để font fallback trong ảnh nghiệm thu. Phiên bản thư viện phải tương thích; pin phiên bản đã cài vào package-lock.json, không trộn cấu hình Tailwind major khác nhau. README ghi phiên bản Node đã dùng và cách chạy thực tế.

Chạy typecheck, lint, production build, kiểm thử các tương tác trọng yếu. Khởi động app, chụp ảnh Chromium ở 1586×992, DPR 1 và các viewport trong checklist, đợi font và ảnh tải xong. So ảnh gốc với ảnh sảnh bằng overlay, kiểm tra bằng mắt, sửa các sai lệch lớn rồi chụp lại. Không dùng số diff toàn ảnh làm bằng chứng duy nhất vì artwork và avatar có thể khác. Không tự đổi ảnh tham chiếu hoặc ngưỡng để cho test qua.

Giao source runnable, package.json, lockfile, README, assets và giấy phép cần thiết, test code, screenshot và QA_REPORT.md nêu rõ lệnh đã chạy, kết quả thật, sai khác còn lại. Không nộp node_modules/dist trong ZIP. Không tự publish hoặc push GitHub; chuẩn bị source GitHub-ready. Nếu môi trường chặn cài dependency hoặc chụp browser, ghi chính xác bước chưa kiểm tra, không giả kết quả.
