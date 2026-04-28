<sub>🌐 <a href="README.en.md">English</a> · <b>Tiếng Việt</b></sub>

<div align="center">

# Huashu Design (Dành cho Antigravity)

> *「Gõ yêu cầu. Nhấn Enter. Nhận về một bản thiết kế hoàn chỉnh.」*

[![License](https://img.shields.io/badge/License-Personal%20Use%20Only-orange.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](https://skills.sh)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Chỉ cần trò chuyện với Antigravity, bạn sẽ nhận được một thiết kế sẵn sàng để bàn giao.**

<br>

Chỉ từ 3 đến 30 phút, bạn có thể hoàn thành một **đoạn video ra mắt sản phẩm**, một bản mẫu (prototype) App có thể bấm tương tác được, một bộ slide PowerPoint có thể chỉnh sửa, hoặc một đồ họa thông tin (infographic) chuẩn in ấn.

Chất lượng không dừng ở mức "AI làm tàm tạm" — nó trông giống như tác phẩm của một đội ngũ thiết kế chuyên nghiệp. Nếu bạn cung cấp các tài sản thương hiệu (logo, bảng màu, ảnh chụp UI), kỹ năng (skill) này sẽ hiểu và thấm nhuần phong cách thương hiệu của bạn. Nếu không cung cấp gì, hệ thống cũng có sẵn 20 ngôn ngữ thiết kế tích hợp để đảm bảo kết quả luôn đạt mức thẩm mỹ cao, không bị lỗi thiết kế AI (AI slop).

**Mọi hiệu ứng animation bạn thấy trong README này đều do chính huashu-design tự tạo ra.** Không dùng Figma, không dùng After Effects. Chỉ cần một câu lệnh prompt + chạy skill. Lần tới bạn cần làm video ra mắt sản phẩm? Giờ đây chính bạn cũng có thể tự làm được.

```bash
Sao chép thư mục vào ~/.gemini/antigravity/skills/huashu-design-Antigravity
```

Dành riêng và tương thích hoàn toàn với **Antigravity**.

[Xem thư viện Demo](#thư-viện-demo) · [Cài đặt & Sử dụng](#cài-đặt--sử-dụng-ngay) · [Tính năng](#các-tính-năng-chính) · [Cơ chế cốt lõi](#cơ-chế-cốt-lõi)

</div>

---

<p align="center">
  <img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.gif" alt="huashu-design Hero · Typing → Choosing directions → Gallery expansion → Focus → Brand reveal" width="100%">
</p>

<p align="center"><sub>
  ▲ 25 Giây · Terminal → 4 Hướng phong cách → Gallery ripple → 4 Lần Focus → Hiển thị thương hiệu<br>
  👉 <a href="https://www.huasheng.ai/huashu-design-hero/">Truy cập bản tương tác HTML có âm thanh</a> ·
  <a href="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4">Tải MP4 (Bao gồm BGM+SFX · 10MB)</a>
</sub></p>

---

## Cài đặt & Sử dụng ngay

Skill này đã được tải về trực tiếp. Để sử dụng trong **Antigravity**, chỉ cần mở chat và đưa ra yêu cầu:

```text
"Hãy làm một slide thuyết trình về AI Tâm lý học, đề xuất cho tôi 3 hướng phong cách để chọn."
"Tạo một bản mẫu (prototype) iOS cho app đếm ngược (Pomodoro), thiết kế 4 màn hình có thể bấm qua lại được."
"Biến đoạn văn bản logic này thành một video animation dài 60 giây, xuất ra dạng MP4 và GIF."
"Hãy đóng vai chuyên gia và đánh giá bản thiết kế này theo 5 tiêu chí."
```

Không cần nút bấm, không cần bảng điều khiển phức tạp, không cần cài đặt thêm plugin cho Figma.

---

## Các Tính Năng Chính

| Khả năng | Sản phẩm đầu ra | Thời gian (ước tính) |
|------|--------|----------|
| **Prototype Tương tác (App/Web)** | Một file HTML duy nhất · Hiển thị giao diện iPhone chân thực · Clickable (Bấm được) · Hỗ trợ Playwright test | 10–15 phút |
| **Slide Thuyết Trình** | HTML deck (Chiếu trên trình duyệt) + Có thể xuất ra file PowerPoint (PPTX) hỗ trợ chỉnh sửa chữ | 15–25 phút |
| **Motion Design (Animation)** | File MP4 (25fps / 60fps) + GIF (tối ưu bảng màu) + Nhạc nền (BGM) | 8–12 phút |
| **Gợi ý Biến thể Thiết kế** | Xem so sánh 3+ phong cách cạnh nhau · Tweak trực tiếp qua bảng điều khiển · Thử nghiệm đa chiều | 10 phút |
| **Infographic / Biểu đồ Dữ liệu** | Dàn trang chuẩn in ấn (Magazine-level) · Xuất ra file PDF/PNG/SVG | 10 phút |
| **Cố Vấn Hướng Thiết Kế** | Tổng hợp 5 trường phái × 20 triết lý thiết kế · Đề xuất 3 định hướng · Chạy song song tạo Demo | 5 phút |
| **Chuyên gia Đánh giá (5 Tiêu chí)** | Đánh giá qua biểu đồ Radar + Checklist (Keep/Fix/Quick Wins) hành động ngay | 3 phút |

---

## Thư viện Demo

### Cố vấn Định hướng (Fallback Advisor)

Khi yêu cầu của bạn quá chung chung: Skill sẽ không "làm bừa", mà sẽ tự động gọi chế độ Fallback, gợi ý 3 định hướng thiết kế khác nhau (từ bộ 20 triết lý), sau đó làm ra 3 bản demo riêng biệt để bạn chọn phong cách ưng ý nhất.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w3-fallback-advisor.gif" width="100%"></p>

### Bản mẫu App iOS (iOS App Prototype)

Hiển thị kích thước iPhone 15 Pro chuẩn (kèm Dynamic Island, thanh trạng thái). Hỗ trợ chuyển qua lại nhiều màn hình và lấy hình ảnh thực tế từ Wikimedia/Unsplash.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c1-ios-prototype.gif" width="100%"></p>

### Động cơ Thiết kế Chuyển động (Motion Design Engine)

Hỗ trợ các API như `useTime`, `useSprite`, `interpolate` để bao quát mọi nhu cầu Animation. Có script đi kèm cho phép xuất ra MP4 hoặc GIF 60fps có kèm nhạc nền.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c3-motion-design.gif" width="100%"></p>

### Từ HTML Slides sang PowerPoint (Chỉnh sửa được)

Tạo Slide trình chiếu dưới định dạng HTML, sau đó dùng `html2pptx.js` để đọc toàn bộ giao diện và dịch nó sang đối tượng PowerPoint, **giữ nguyên khung văn bản (Textboxes)** để bạn có thể bấm vào chữ và sửa được trên PowerPoint.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c2-slides-pptx.gif" width="100%"></p>

### Bảng Điều khiển (Tweaks)

Có thể cài đặt các thông số (Màu sắc, Font, Độ đậm nhạt...) và chỉnh qua bảng điều khiển hiển thị ở cạnh màn hình. Cấu hình được lưu lại tại `localStorage`.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c4-tweaks.gif" width="100%"></p>

### Trình bày Dữ liệu & Infographic

Dàn trang dạng tạp chí dùng CSS Grid, tự động ngắt dòng thông minh (`text-wrap: pretty`), chạy bằng dữ liệu thực. Có thể xuất thẳng ra PDF vector.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c5-infographic.gif" width="100%"></p>

### Workflow Thiết Kế Thương Hiệu (Brand Asset Protocol)

Gồm 5 bước bắt buộc khi cần làm thiết kế cho một thương hiệu có thật: Hỏi ý kiến -> Lên trang chủ tìm -> Tải logo (SVG/HTML) -> Phân tích mã màu (Hex/RGB) -> Viết tệp `brand-spec.md` để áp dụng màu đó một cách chuẩn xác. Không bao giờ đoán bừa màu thương hiệu.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w1-brand-protocol.gif" width="100%"></p>

---

## Cơ Chế Cốt Lõi

### Giao thức Nhận diện Thương hiệu (Brand Asset Protocol)

Một quy tắc cực kì "cứng" của skill. Khi yêu cầu liên quan đến các thương hiệu cụ thể (Stripe, Apple, hoặc công ty của bạn), 5 bước sau sẽ được kích hoạt:

| Bước | Hành động | Mục đích |
|------|------|------|
| 1 · Hỏi | Hỏi người dùng xem họ có bộ hướng dẫn nhận diện thương hiệu không? | Tôn trọng nguồn tài nguyên có sẵn |
| 2 · Truy cập web | Tìm trên `<brand>.com/brand` hoặc `<brand>.com/press` | Lấy bảng màu từ nguồn chính thống |
| 3 · Tải tài nguyên | Tải SVG → HTML trang chủ → Chụp màn hình để trích xuất màu | Các biện pháp dự phòng liên tiếp |
| 4 · Phân tích mã màu | Tìm tất cả mã hex `#xxxxxx`, lọc bỏ trắng đen, lấy màu chủ đạo | **Tuyệt đối không đoán bừa màu thương hiệu từ bộ nhớ của AI** |
| 5 · Lưu cấu hình | Lưu tệp `brand-spec.md` + biến CSS `var(--brand-*)` | Giúp nhất quán thiết kế sau này |

### Chống lại giao diện kiểu "AI Slop"

Skill này được thiết lập để tránh các thiết kế nhìn "sặc mùi AI" (như gradient màu tím sến, icon emoji, mặt người nhợt nhạt vẽ bằng SVG...). Thay vào đó nó dùng Typography tiêu chuẩn in ấn, CSS Grid và hệ thống phối màu chuyên nghiệp oklch.

---

## Sự khác biệt so với các sản phẩm GUI 

Ý tưởng về giao thức Thương hiệu bắt nguồn từ các bài học tạo Design System tiên tiến: **Một bản thiết kế tuyệt vời không bắt đầu từ trang giấy trắng, mà nó phát triển từ bối cảnh và định dạng phong cách đã có**. Đó là lằn ranh giữa một bản phác thảo 65 điểm và một tác phẩm 90 điểm.

Nếu như các phần mềm giao diện đồ họa (GUI) hay Figma là **những công cụ đồ họa tốt hơn**, thì mục tiêu của Antigravity huashu-design là **làm cho lớp giao diện công cụ đó biến mất**. Bạn không cần thao tác chuột, chỉ cần ra lệnh. 

---

## Hạn chế (Limitations)

- **Không hỗ trợ chuyển PPTX sang Figma**. Bạn có thể xuất HTML, quay video, xuất PDF, xuất PowerPoint, nhưng không thể ném tệp đó vào thiết kế Keynote để thay thế vector chi tiết.
- **Không hỗ trợ Animation phức tạp dạng Framer Motion**. Không xử lý thiết kế vật lý, 3D thật, hệ thống hạt (particle systems).
- **Với thương hiệu không có bất kỳ nguồn dữ liệu nào (Trang trắng hoàn toàn), chất lượng thiết kế có thể chỉ đạt 60-65 điểm.** Thiết kế đẹp luôn cần điểm tựa phong cách.

---

## Cấu Trúc Thư Mục

```
huashu-design-Antigravity/
├── SKILL.md                 # Tài liệu hướng dẫn chính (Dành cho AI Agent)
├── README.md                # Tệp này (Dành cho người dùng đọc)
├── assets/                  # Các thành phần cốt lõi
│   ├── animations.jsx       # Bộ Engine: Stage + Sprite + Easing + interpolate
│   ├── ios_frame.jsx        # Khung iPhone 15 Pro bezel
│   ├── deck_stage.js        # Engine xử lý HTML Slide
│   └── ...                  # (Các showcase demo & nhạc nền)
├── references/              # Tài liệu tham khảo sâu cho từng tác vụ
├── scripts/                 # Chuỗi công cụ xuất ra file Video, PDF, PPTX
│   ├── render-video.js      # Trình render HTML → MP4
│   ├── convert-formats.sh   # Chuyển đổi MP4 → 60fps / GIF
│   ├── export_deck_pptx.mjs # Xuất HTML sang tệp PPTX
│   └── html2pptx.js         # Engine quy đổi HTML sang PowerPoint Object
└── demos/                   # Demo GIF/MP4 giới thiệu các năng lực
```

---

## Giấy Phép Sử Dụng (License)

**Miễn phí và Tự do cho Cá nhân** — Bạn có thể học tập, nghiên cứu, sáng tạo, làm dự án cá nhân, viết bài, chạy project ngoài giờ thoải mái.

**Nghiêm cấm Thương mại hóa cho Doanh nghiệp** — Các tổ chức, công ty, đội nhóm muốn dùng công cụ này để kiếm lợi nhuận, tích hợp vào sản phẩm thương mại hoặc dùng làm công cụ bàn giao cho khách hàng bắt buộc phải liên hệ cấp phép bản quyền.

*(Dự án huashu-design ban đầu được phát triển bởi tác giả Alchain/Huasheng)*
