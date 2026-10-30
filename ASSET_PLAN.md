# Kế hoạch hình ảnh — cần hoàn thành trước visual QA

Ảnh gốc là raster phẳng; không có layer/asset riêng. ZIP giữ nguyên ảnh để tham chiếu, không coi đó là bộ asset đã sẵn sàng.

| Asset cần tạo | Đường dẫn đề xuất trong app/public | Cách dùng |
|---|---|---|
| Logo bích cyan | assets/logo-spade.svg | SVG riêng, chữ logo là HTML |
| Bộ bài hero, bích neon xanh/tím | assets/hero-cards.webp | object-fit:contain; neo phải, mask fade trái |
| Minh họa bích lớn, bài, núi/công trình về đêm | assets/sidebar-art.webp | cover phần dưới sidebar, gradient fade trên |
| 4 background phòng | assets/rooms/room-01..04.webp | artwork tối phía sau, overlay navy đảm bảo chữ rõ |
| Avatar cố định theo ID | assets/avatars/*.webp | ảnh local nhất quán, không random mỗi lần render |
| Font + license | assets/fonts/ | Vietnamese + Latin, weight cần dùng |

## Quy tắc
1. Giữ artwork lớn ở hero/sidebar; đây là đặc trưng của mẫu. Lucide chỉ dùng cho icon điều khiển như Home, Users, Trophy, Bell, LogOut, Plus, Search, MessageSquare, MoreHorizontal, ArrowRight, Zap, Crown.
2. Không chụp/cắt nguyên thẻ phòng chứa chữ và avatar rồi dùng thay component. Không dùng nguyên ảnh làm giao diện tương tác giả.
3. Có thể tạo artwork mới bám mẫu bằng image generation nếu có công cụ, nhưng phải kiểm tra các ảnh thực tế trước khi tích hợp. Chỉ cắt từ ảnh gốc nếu vùng đó không chứa UI/chữ; không coi việc cắt là đã tách lớp đầy đủ.
4. Nếu tạo mới artwork, yêu cầu **không chữ, không nút, không avatar, không watermark**. Có alpha hoặc mask chuyển nền mềm. Asset tĩnh dễ cache, không URL hết hạn, không hotlink ảnh người thật không rõ giấy phép.
5. Avatar có thể là chân dung nhân vật tổng hợp được tạo riêng; giữ phong cách portrait thực như ảnh, tránh thay toàn bộ bằng vòng tròn chữ cái trong bản nghiệm thu.
6. Ghi nguồn/quyền sử dụng từng asset trong ASSET_CREDITS.md; các artwork thay thế phải được ghi rõ trong QA_REPORT.

## Prompt gợi ý artwork
Hero: “Wide decorative illustration for dark navy Vietnamese card game dashboard, realistic fan of white playing cards 10 J Q K A with black spades, cyan and violet edge lighting, luminous large spade, dark blue night atmosphere, composition concentrated on right with empty transparent or dark navy fade on left, no typography, no UI, no people.”
Sidebar: “Tall narrow decorative gaming illustration, large ornate metallic spade with restrained gold edges in lower foreground, blue playing cards, dark mountainous night skyline and subtle Vietnamese architectural silhouettes, navy cyan violet palette, dramatic but dark, upper third fading into plain navy, no text, no buttons, no portraits.”
Room backgrounds: bốn cảnh tối riêng: hội quán đèn ấm, phố đêm xanh tím, phòng bài sang vàng đồng, sân vườn đèn lồng; tương phản thấp để không cạnh tranh chữ.

Không hứa tái tạo chính xác từng pixel của artwork sinh ảnh. Yêu cầu độ giống cao ở cấu trúc, tỷ lệ, typography, màu và vị trí artwork; báo khác biệt asset trung thực.
