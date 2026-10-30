# Đặc tả thiết kế đã chốt

## 1. Ngôn ngữ thị giác
Đấu trường đêm: navy gần đen, cyan là hành động chính, tím cho xếp hạng và trạng thái đang chơi; vàng chỉ dành cho xu/vương miện. Giữ cảm giác gaming nhưng chữ rõ, viền mảnh, glow cục bộ. Không đổi sang xanh lá chủ đạo hoặc dashboard trắng.

## 2. Font
Chọn **Be Vietnam Pro**, sans-serif, có dấu tiếng Việt. Dùng weight 400/500/600/700/800; tránh faux-bold và font chữ trang trí cho nội dung. Cài qua gói font phù hợp hoặc tự host WOFF2 chính thức có subset Vietnamese + Latin. Đưa giấy phép font vào source khi phân phối. Tải local để screenshot ổn định; font-display: swap; QA phải đợi document.fonts.ready. Fallback chỉ khi tải lỗi: Arial, sans-serif. Nếu chưa tải được font, báo blocker visual QA.

| Thành phần | Cỡ / line-height desktop | Weight |
|---|---|---|
| Logo TIẾN LÊN | 26 / 30px | 800 |
| Dòng MIỀN NAM | 12 / 16px, tracking 3px | 700 |
| Tiêu đề hero | 46 / 56px, tracking -1px | 800 |
| Mô tả hero | 18 / 28px | 400 |
| Số thống kê | 28 / 34px | 700 |
| Heading section / tên phòng | 20 / 28px | 700 |
| Nhãn nút hành động | 18 / 26px | 700 |
| Nội dung / tên bạn | 14 / 21px | 400–600 |
| Meta / trạng thái | 12 / 18px | 400–500 |

Ở mobile hero 28/36px, heading 18/26px. Không ép một dòng gây tràn; desktop dùng line break phù hợp ảnh. Số xu và thống kê dùng tabular-nums.

## 3. Bảng màu
| Token | Giá trị | Vai trò |
|---|---|---|
| bg | #060F1C | Nền trang |
| panel | #0B1727 | Thẻ và sidebar |
| panel-raised | #102238 | Hover / vùng nổi |
| border | #18344D | Viền nền |
| text | #F3F7FF | Chữ chính |
| muted | #A5B8D5 | Mô tả |
| dim | #8198B9 | Chữ phụ, offline |
| primary | #16D5F3 | CTA / active |
| primary-hover | #56E5FF | Hover |
| on-primary | #03131D | Chữ trên nút cyan |
| violet | #9D8AFF | BXH / đang chơi |
| success | #20E6A1 | Online / còn chỗ |
| danger | #FF6474 | Đã đầy / lỗi |
| gold | #FFD165 | Xu / chủ phòng |

Màu gradient/artwork không cần bị giới hạn vào bảng này. Không dùng chữ trắng trên nền cyan sáng; dùng on-primary. Kiểm tra contrast WCAG AA cho chữ nhỏ khi triển khai (4.5:1), không mặc định các token đã được chứng nhận.

## 4. Bố cục desktop theo ảnh 1586×992
Các mốc sau là tọa độ gần đúng để căn chỉnh, sai số mục tiêu 8px cho khối lớn.
- Sidebar x=0..246, cao toàn viewport. Logo vùng y=0..74. Menu bắt đầu y≈102, item cao 60px; artwork phía dưới từ khoảng y=320 tới đáy.
- Topbar x=246..1586, y=0..74. Cụm user/xu/logout bên phải. Dòng “02 — ĐẤU TRƯỜNG ĐÊM” là nhãn concept trong ảnh: giữ ở prototype để so ảnh, có thể đổi thành “SẢNH CHƠI” ở bản sản phẩm sau khi được yêu cầu.
- Friends rail x≈1274..1586, y=74..992, padding 24px; viền trái. Tiêu đề, tìm kiếm, 7 bạn online, divider, 4 bạn offline đang hiển thị; nhãn “Bạn bè khác (12)” phải có đủ 12 mẫu nếu dùng số đó, phần còn lại cho scroll.
- Main x=246..1274, padding trái/phải 30–32px; content width≈966px.
- Hero top≈105, title x≈276; artwork nằm nửa phải, dưới chữ/không che chữ. Ba ô thống kê x≈278, y≈213, cao≈82, rộng≈202, gap≈16.
- Ba nút action y≈315, cao≈77, gap 12px, chia đều. “Tham gia nhanh” cyan đặc; “Tạo phòng” nền tối cyan viền; “Bảng xếp hạng” nền tím tối viền tím.
- Hàng danh sách/bộ lọc y≈419..455. Tiêu đề trái, 4 tab phải.
- Grid phòng x≈277..1242, y≈472..956; 2 cột bằng nhau, gap 16px; mỗi thẻ cao≈234px, radius 10px.
- Mỗi thẻ: header tên/chủ phòng/status; hàng 4 vị trí avatar trên panel tối; footer số người và nút join. Avatar người chơi 52px; avatar bạn bè 44px; avatar topbar 42px. Chủ phòng có vương miện nhỏ, online có chấm xanh với vòng nền.

Dùng CSS grid cho page shell và room grid, flex trong header/footer. Không absolute-position toàn bộ UI. Absolute chỉ dành cho artwork, glow, crown và presence dot. Main min-width:0; text dài truncate có title hoặc wrap có kiểm soát.

## 5. Hiệu ứng
Viền thẻ 1px, glow cyan 0 0 16px rgba(22,213,243,.15); đang chơi dùng tím, đầy dùng đỏ nhẹ. Radius input/button 8px, panel 10–12px, avatar 50%. Hover 150–200ms, translateY tối đa -2px. Focus-visible outline 2px cyan offset 3px. Tôn trọng prefers-reduced-motion; không pulse liên tục toàn trang.

## 6. Responsive
- >=1440px: sidebar 246px, friends 312px, main flexible.
- 1200–1439px: sidebar 210px, friends 260px, main padding 24px; thẻ 2 cột, giảm khoảng cách và heading vừa phải.
- 1024–1199px: sidebar 80px icon-only có accessible label; friends chuyển drawer; main vẫn 2 cột.
- 768–1023px: sidebar 72px, friends drawer, room grid 2 cột nếu mỗi card >=320px, nếu không thì 1 cột.
- <768px: bỏ sidebar cố định, dùng header gọn + navigation drawer; rooms 1 cột, stats 3 cột gọn, actions xếp 1 cột, filters wrap, friends drawer. Không làm biến mất đường vào BXH/bạn bè/logout. Touch target >=44px.
- QA tại 1586×992, 1440×900, 1024×768, 768×1024, 390×844. Không cuộn ngang toàn trang.
