# Kế hoạch triển khai

## Stack và tổ chức
React + TypeScript + Vite; Tailwind CSS; Lucide React; React Router cho route; state dùng Context + useReducer hoặc hooks có chủ đích. Chọn bộ phiên bản tương thích khi build, commit lockfile. Không cần Redux, websocket, DB hoặc model AI. Import design/tokens.css và ánh xạ utility vào CSS variables, tránh màu rải rác.

Cấu trúc app/ đề xuất:
```text
src/
  app/                 # router, providers, global styles
  components/ui/       # Button, Modal, Avatar, Badge, Input, Toast, Skeleton
  components/layout/   # AppShell, Sidebar, Topbar, FriendsPanel
  features/lobby/      # LobbyPage, HeroStats, LobbyActions, RoomFilters, RoomCard
  features/rooms/      # RoomPage, PlayerSeat, ReadyControls
  features/leaderboard/# LeaderboardPage, RankRow
  features/auth/       # LoginPage, session mock
  features/friends/    # FriendList, FriendSearch
  data/                # seeded fixture data
  types/               # Room, Player, RoomStatus
  state/               # reducer và selectors
public/assets/
tests/
```

## Checkpoint 1 — nền móng
Tạo Vite app, cấu hình TS strict, Tailwind, router. Scripts bắt buộc: dev, build, preview, typecheck, lint, test; bổ sung test:e2e khi có browser runner. Cài Be Vietnam Pro, đưa tokens vào CSS. Hoàn thành asset inventory và license. Chỉ coi font đạt khi browser đã load đúng weight.

## Checkpoint 2 — dựng hình sảnh
Dựng shell desktop đúng ba cột trước, rồi hero/stats/actions, room cards, friends panel. Dùng data fixture cố định, route /lobby mở trực tiếp được trong chế độ demo. Chụp 1586×992 trước khi thêm responsive. Chỉnh hình học trước, font sau, artwork/màu/glow sau cùng. Không dừng ở các hộp trống hoặc UI template generic.

## Checkpoint 3 — tương tác
Triển khai đầy đủ INTERACTIONS. Model state tập trung; phân biệt waiting/playing/full; kiểm tra lại room ngay trong handler join. Sau tạo/join rời sảnh sang room. Các nút hiện ra phải có phản hồi thực, không nút chết. Demo room có sẵn sàng/mời bạn/rời phòng, không giả rằng đã có gameplay Tiến Lên đầy đủ.

## Checkpoint 4 — trang liên quan
Phòng chơi dùng bàn oval xanh navy/teal, viền cyan, 4 seat và avatar chung, chat mô phỏng local; chỉ demo trạng thái bàn chờ. BXH dùng cùng shell/palette/avatar, top 3 và bảng thứ hạng, highlight người dùng. Login dùng cùng nền, artwork và font, tên hiển thị + “Vào sảnh”; nói rõ là demo, không yêu cầu mật khẩu thật.

## Checkpoint 5 — responsive và accessibility
Theo breakpoint trong DESIGN_SPEC. Modal trap focus, Esc đóng, restore focus, label input, aria-live toast, keyboard navigation, không chỉ dùng màu phân biệt trạng thái. Kiểm tra touch target, contrast và reduced motion.

## Checkpoint 6 — QA và bàn giao
Chạy các lệnh kiểm tra thực, E2E trọng yếu, screenshot các viewport. Dùng qa/compare_reference.py tạo overlay rồi mở xem, lặp sửa tối thiểu cho đến khi không còn sai lệch lớn; không ghi số vòng giả nếu chưa chạy. Ghi QA_REPORT từ mẫu. README mô tả npm install; npm run dev, Node thực tế, route, demo controls và giới hạn. Đóng ZIP source không node_modules/dist; không deploy/push nếu chưa được yêu cầu.

## Tiêu chí kết thúc
App chạy được; chức năng checklist đạt; không overflow; không thiếu font/artwork lớn; có ảnh so thực tế và báo cáo trung thực. Nếu một bước bị môi trường chặn, phân loại blocked và nêu cách chạy lại thay vì đánh dấu pass.
