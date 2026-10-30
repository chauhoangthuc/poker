# Nguồn asset

Bổ sung 30/10/2026: `room-background.png`, `table-felt.png`, `table-ornament.png` được tạo riêng bằng OpenAI ImageGen, đã xem trước khi tích hợp. Phong cảnh không có bàn/UI; nỉ và họa tiết được áp lên hình học CSS. Giữ PNG gốc thay vì đổi đuôi thành WebP. Avatar dùng lại contact sheet có sẵn. Mặt bài là SVG tự dựng, hạng/chất xác định bằng dữ liệu, không sinh bằng ImageGen; J/Q/K dùng ký hiệu hạng/chất đơn giản thay chân dung quân bài.

| Asset | Nguồn / quyền sử dụng |
|---|---|
| `public/assets/hero-cards.png` | Tạo bằng OpenAI image generation cho prototype này, 29/10/2026. |
| `public/assets/sidebar-art.png` | Tạo bằng OpenAI image generation cho prototype này, 29/10/2026. |
| `public/assets/rooms/room-01.png` đến `room-04.png` | Bốn artwork riêng tạo bằng OpenAI image generation cho prototype này, 29/10/2026. |
| `public/assets/avatars-grid.png` | Contact sheet gồm 20 chân dung nhân vật tổng hợp tạo bằng OpenAI image generation cho prototype này, 29/10/2026. Không dùng ảnh người thật hotlink. |
| `public/assets/logo-spade.svg` | SVG tự dựng cho prototype này. |
| `public/assets/fonts/*.woff2` | Be Vietnam Pro từ gói `@fontsource/be-vietnam-pro`; giấy phép SIL Open Font License 1.1 tại `public/assets/fonts/OFL.txt`. |
| Lucide icons | `lucide-react`, giấy phép ISC theo package trong lockfile. |

Ảnh `../reference/selected-ui.png` chỉ là mẫu đối chiếu, không được dùng làm background hoặc asset của ứng dụng.

Lượt đối chiếu bổ sung 30/10/2026: room-background-v2.png tạo riêng bằng ImageGen để giảm ánh sáng và bỏ trăng; mặt bài court J/Q/K trong PlayingCard.tsx là SVG nguyên bản tự dựng.

Mặt J/Q/K mới dùng SVG public domain từ hayeah/playing-cards-assets, gốc vector-playing-cards của Byron Knoll. Nguồn và tuyên bố public domain được lưu ở public/assets/cards/SOURCE.md; https://github.com/hayeah/playing-cards-assets.

## PNG button skins — 30/10/2026
- `public/assets/buttons/play.png`, `violet.png`, `navy.png`: generated with OpenAI ImageGen from the user-provided room reference. Local transparent decorative artwork; labels remain HTML. No third-party stock license required. Generated artwork differs from the reference and is not claimed to be an exact reproduction.

### Table and card back, 2026-10-30
`table-render.png` and `cards/back-render.png` were generated with OpenAI ImageGen using the supplied room reference. `cards/back-render-small.png` is a resized delivery variant. These are decorative sprites only. Original generated files are retained; card face SVG credits above still apply.

public/assets/lobby-icons.png: generated with OpenAI ImageGen on 2026-10-30 for this prototype; six decorative lobby icons.

leaderboard-stage.png: OpenAI ImageGen generated decorative podium scene, 2026-10-30. Player portraits, names, scores and ranking remain independent HTML.
