# Hành vi prototype

## Dữ liệu và trạng thái
Room: id, name, hostId, maxPlayers (2|3|4), playerIds, status (waiting|playing), password tùy chọn, theme. “Đã đầy” là nhãn suy ra khi waiting và count>=maxPlayers; playing ưu tiên nhãn “Đang chơi”. available = waiting && count<maxPlayers. Seed 4 phòng: 2 còn chỗ, 1 đang chơi, 1 đầy, khớp các tab trong ảnh. Online friends 7; offline 12, cho scroll. Stats cố định 128 trận/68%/5 trận thắng liên tiếp, không giả là số liệu server.

## Tạo phòng
Modal có tên 3–40 ký tự sau trim, lựa chọn 2/3/4 (mặc định 4), mật khẩu tùy chọn tối đa 32 ký tự, nút hiện/ẩn. Không đặt quy tắc mật khẩu phức tạp cho demo. Enter submit khi hợp lệ, nút tạo disabled khi không hợp lệ, lỗi dưới field. Người tạo là host và seat đầu tiên, count=1, status waiting. Sau tạo chuyển /rooms/:id. Hủy/Esc không đổi dữ liệu. Mật khẩu chỉ là state demo, không phải cơ chế bảo mật.

## Tham gia / tham gia nhanh
- Waiting còn chỗ: join người dùng một lần rồi chuyển room.
- Room có password: mở modal nhập và check local; sai hiện lỗi, đúng mới join.
- Full: hiển thị “Phòng đã đủ người. Hãy chọn phòng khác.” Không tăng số người. Card có nút disabled “Đã đầy”, handler vẫn chặn nếu dữ liệu thay đổi hoặc truy cập trực tiếp.
- Playing: giữ sắc tím và bố cục ảnh, đổi nhãn nút thành “Đang chơi” disabled; không để nút Tham gia gây hiểu nhầm. Đây là điều chỉnh có chủ đích so với ảnh AI.
- Quick join: chọn phòng waiting còn chỗ, không mật khẩu, theo thứ tự fixture; không có thì toast “Chưa có phòng phù hợp. Bạn có thể tạo phòng mới.”
- Nếu đã ở room đó, không cộng seat lặp. Rời room cập nhật số người; host rời thì chuyển host cho người còn lại hoặc xóa room rỗng.

## Bộ lọc / bạn bè
Tabs tính count từ data, không hardcode sau mutation; “Còn chỗ” bao gồm phòng khóa còn chỗ, có Lock icon. Friend search lọc không phân biệt hoa thường/dấu. Mời bạn trong room thêm một bạn mock còn chưa có mặt nếu còn chỗ, toast rõ; trong sảnh nút chat mở drawer chat local, không gửi người thật. Dấu ba chấm mở menu xem hồ sơ demo/mời; Bell mở danh sách thông báo demo.

## Route
- /leaderboard: danh sách seed, sort theo điểm giảm dần, có nút trở lại sảnh; không đổi ranking ngẫu nhiên.
- /login: nhập tên và vào sảnh; logout clear mock session và đưa về login. Không dùng auth thật. Guest /lobby có thể seed user để phục vụ demo screenshot; chế độ demo được README ghi rõ. Sau logout giữ login cho tới khi người dùng vào lại.
- /rooms/:id: bàn chờ có seat, toggle sẵn sàng, mời bot/bạn mock, chat local và rời phòng. Room ID không tồn tại hiện thông báo + về sảnh. Không triển khai luật bài đầy đủ ngoài scope.

## Loading / empty / error
Có demo switch qua query `?state=loading|empty|error` ở /lobby để QA tái lập; mặc định success. Loading: skeleton đúng kích thước 4 card, vùng list aria-busy. Empty: “Chưa có phòng nào”, nút Tạo phòng. Filter rỗng: “Không có phòng phù hợp”, nút Xóa bộ lọc. Error: “Không thể tải danh sách phòng”, nút Thử lại chuyển về success. Không trình bày lỗi mạng giả như backend thật; README giải thích đây là mô phỏng. Transition loading bình thường có thể 400ms cố định, screenshot chỉ sau success.
