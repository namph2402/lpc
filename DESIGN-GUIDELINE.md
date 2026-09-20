# LPC — Website Design Guideline 2027

> **Responsive to change** · Modern · Professional · Trusted · Human-centered · Project-driven

Tài liệu mô tả quy tắc màu sắc, typography, khoảng cách, thành phần giao diện và SEO cho website LPC.

| Thành phần | File |
|---|---|
| Theme CSS (trên Bootstrap 5.3) | [`css/lpc-design-system.css`](css/lpc-design-system.css) |
| Header / footer dùng chung | [`js/layout.js`](js/layout.js) |
| Sáng / tối (chạy trong `<head>`) | [`js/theme.js`](js/theme.js) |
| Dữ liệu SEO từng trang | [`scripts/pages.json`](scripts/pages.json) |
| Sinh ảnh OG + sitemap + robots | [`scripts/build_seo_assets.py`](scripts/build_seo_assets.py) |
| Sinh bộ logo + favicon từ file gốc | [`scripts/make_logo.py`](scripts/make_logo.py) |
| Trang mẫu chuẩn | [`index.html`](index.html) |
| CSS riêng từng trang (chỉ khi thật cần) | [`css/pages/`](css/pages/) — `engineering`, `digital-data`, `industries`, `contact` |

---

## 1. Công nghệ

- **Bootstrap 5.3.3** + **Bootstrap Icons 1.11.3** (CDN jsDelivr, có SRI).
- Font **Inter** (Google Fonts), weight 400–800.
- HTML tĩnh, chạy trực tiếp bằng `file://` hoặc bất kỳ web server nào.

Thứ tự nạp trong `<head>`: `js/theme.js` → Google Fonts → `bootstrap.min.css` → `bootstrap-icons.min.css` → `css/lpc-design-system.css` (→ `css/pages/{slug}.css` nếu có).
Cuối `<body>`: `js/layout.js` → `bootstrap.bundle.min.js`.

---

## 2. Bảng màu

### 2.1 Màu thương hiệu (tỷ lệ 60 / 20 / 10 / 10)

| Vai trò | Token | Mã màu | Tỷ lệ | Dùng cho |
|---|---|---|---|---|
| **Primary – Navy** | `--lpc-navy` | `#0B1F44` | 60% | Tiêu đề, nút chính, hero overlay, CTA band, footer |
| **Neutral** | `--lpc-neutral` | `#F4F6F9` | 20% | Section xen kẽ, card, khối trích dẫn |
| **Accent – Đỏ LPC** | `--lpc-red` | `#E31E24` | 10% | CTA "Liên hệ / RFP", nút chính trong hero, gạch nhấn |
| **Supporting – Xám xanh** | `--lpc-slate` | `#647488` | 10% | Chữ phụ, mô tả, meta |

### 2.2 Màu bổ trợ

| Token | Mã màu | Dùng cho |
|---|---|---|
| `--lpc-bluegray` | `#2E4677` | Technology, Modern |
| `--lpc-navy-700` | `#13295A` | Card ở dark mode |
| `--lpc-navy-600` | `#1A3470` | Hover nút navy, icon |
| `--lpc-red-600` | `#C4161C` | Hover nút đỏ |
| `--lpc-blue` | `#1E5BD8` | Link, thanh tiêu đề section, tab active, nút công cụ |
| `--lpc-blue-soft` | `#E8EFFC` | Nền tag, nền progress |

### 2.3 Quy tắc sử dụng

- ✅ Navy là màu chủ đạo, chiếm phần lớn diện tích có màu.
- ✅ Đỏ **chỉ để nhấn**: nút CTA, gạch dưới tiêu đề, gạch eyebrow, divider.
- ❌ Không dùng đỏ làm nền mảng lớn hoặc màu chữ đoạn văn.
- ✅ Mỗi màn hình chỉ có **1 CTA đỏ nổi bật** (ngoài nút "Liên hệ / RFP" trên header).
- ❌ Không hard-code màu trong HTML — dùng token, utility Bootstrap hoặc class design system để tự đổi theo sáng/tối.

---

## 3. Giao diện sáng / tối

Dùng cơ chế **color mode của Bootstrap 5.3**: thuộc tính `data-bs-theme` trên `<html>`.

- `js/theme.js` đặt theme **trước khi render** (không nháy màu): lựa chọn đã lưu (`localStorage: lpc-theme`) → nếu chưa có thì theo hệ điều hành.
- Nút mặt trăng / mặt trời trên header chuyển đổi và lưu lựa chọn.
- Khối **luôn tối** ở cả hai chế độ đặt `data-bs-theme="dark"`: `.hero`, `.cta-band`, `.section-dark`, footer.

| Biến Bootstrap | Light | Dark |
|---|---|---|
| `--bs-body-bg` | `#FFFFFF` | `#0B1F44` |
| `--bs-tertiary-bg` (section-alt, feature-card) | `#F4F6F9` | `#0E2550` |
| `--bs-secondary-bg` (card dark) | `#EDF1F6` | `#13295A` |
| `--bs-border-color` | `#E3E8EF` | `rgba(255,255,255,.12)` |
| `--bs-heading-color` | `#0B1F44` | `#FFFFFF` |
| `--bs-body-color` | `#1F2A3D` | `#E6EBF3` |
| `--bs-secondary-color` | `#647488` | `#A9B4C6` |
| `--bs-link-color` | `#1E5BD8` | `#6FA2FF` |
| `.btn-lpc` | Nền navy | Nền **đỏ** |

---

## 3b. Logo

| File | Dùng ở đâu |
|---|---|
| `assets/img/logo-lpc-h.png` | Header, nền sáng (ngang: biểu tượng + chữ) |
| `assets/img/logo-lpc-h-white.png` | Header nền tối, footer |
| `assets/img/logo-lpc.png` / `-white.png` | Bản xếp dọc (tài liệu, in ấn) |
| `assets/img/logo-mark.png` | Riêng biểu tượng tháp |
| `assets/favicon.svg`, `assets/apple-touch-icon.png` | Favicon, icon app |
| `assets/img/logo-source.png` | File gốc, giữ để sinh lại |

Header tự đổi giữa hai bản qua class `.logo-on-light` / `.logo-on-dark`. Khi có file logo mới:

```bash
python3 scripts/make_logo.py assets/img/logo-source.png   # sinh lại toàn bộ bộ logo + favicon
python3 scripts/build_seo_assets.py                       # ảnh OG dùng logo mới
```

Khoảng trống quanh logo tối thiểu bằng nửa chiều cao logo. Không đặt logo bản màu lên nền tối — dùng bản trắng.

---

## 3c. Ngôn ngữ

Giao diện dùng **tiếng Việt**. Ba nhóm giữ nguyên tiếng Anh:

1. **Slogan thương hiệu:** "Responsive to change", "Engineering today for a better tomorrow.", cột từ khóa trong hero (People · Projects · Technology · Sustainability), dòng "Engineering · Technology · People" ở footer.
2. **Tên mảng dịch vụ:** Engineering, Digital Engineering, PM/CM, Tech Hub, Digital & Data, Engineering Tools, Sustainability, Insights, Trust Center.
3. **Thuật ngữ chuyên ngành:** BIM, CDE, Digital Twin, Scan to BIM, Data Platform, ESG, IoT, ISO 19650, HSE…

Nhãn điều hướng và nhãn giao diện dịch hết: Trang chủ, Năng lực, Dự án, Lĩnh vực, Giới thiệu, Đối tác, các nhãn tab, nút và eyebrow.

---

## 4. Typography

| Cấp | Class | Cỡ chữ | Weight | Kiểu |
|---|---|---|---|---|
| Hero H1 | `.display-lpc` | 32 → 56px (clamp) | 800 | IN HOA, line-height 1.14 |
| Section title (H2) | `.section-title` | 18 → 22px | 700 | IN HOA, thanh xanh trái + gạch đỏ dưới |
| Card title (H3) | `.card-title` / `.feature-card h3` | 15–16px | 700 | — |
| Lead | `.hero-lead` | 18px | 400 | Tagline tiếng Anh |
| Body | — | 16px | 400 | line-height 1.625 |
| Small / meta | `.fs-7` / `.card-meta` | 14 / 12px | 400 | — |
| Eyebrow | `.eyebrow` (+ `.eyebrow-dash`) | 12px | 700 | IN HOA, letter-spacing .08em |
| Số liệu | `.stat-value` | 32px | 700 | 15+ / 100+ / 500+ |

Mỗi trang chỉ có **1 thẻ `<h1>`** (trong hero); khối dùng `h2`, card dùng `h3`.

---

## 5. Khoảng cách & bố cục (đồng bộ toàn site)

| Quy tắc | Giá trị |
|---|---|
| Padding dọc mỗi `.section` | **80px** desktop · **64px** tablet (<992px) · **48px** mobile (<576px) |
| Hai section cùng nền nối tiếp | Tự bỏ `padding-top` → khoảng cách luôn = 1 × section |
| Tiêu đề khối → nội dung | `.section-head` = 32px |
| Khe lưới card nhỏ | `.row.g-3` (16px) |
| Khe lưới khối lớn | `.row.g-4` (24px) |
| Container | Bootstrap `.container` (tối đa 1320px), gutter 2rem |
| Header | Cao 76px, sticky |

Cấu trúc trang chuẩn:

```html
<section class="hero" data-bs-theme="dark">…</section>
<div class="hero-stats">…</div>                     <!-- tuỳ chọn, đè lên đáy hero -->
<section class="section">…</section>
<section class="section section-alt">…</section>    <!-- nền xám xen kẽ -->
<section class="section">…cta-band…</section>
```

❌ Không thêm `mt-* / mb-* / py-*` lên `section`.

### Breakpoint (Bootstrap)

| Mốc | Header | Lưới card |
|---|---|---|
| < 576px | Logo + icon + menu offcanvas | 1–2 cột |
| ≥ 768px | + nút "Liên hệ / RFP" | 2–3 cột |
| ≥ 992px | Vẫn dùng menu offcanvas | 3–5 cột |
| ≥ 1200px | Menu ngang đầy đủ | |

---

## 6. Bo góc, đổ bóng

- Bo góc: 4px (nút, tag) · 6px (card, `--bs-border-radius`) · 10px (khối lớn).
- Đổ bóng (chỉ light mode): card `0 2px 10px rgba(11,31,68,.06)` · hover `0 12px 28px rgba(11,31,68,.12)`.
- Hover card: nhấc lên 3px, transition 200ms. Tắt chuyển động khi `prefers-reduced-motion`.

---

## 7. Thành phần

| Nhóm | Class |
|---|---|
| Nút | `.btn` + `.btn-lpc` (navy/đỏ theo theme) · `.btn-accent` (đỏ) · `.btn-blue` · `.btn-outline-lpc` · `.btn-ghost` (viền trắng trên nền tối) · `.btn-arrow` (thêm mũi tên) · `.arrow-btn` (nút tròn) |
| Hero | `.hero` `.hero-sm` · `.hero-content` · `.hero-lead` · `.hero-text` · `.hero-actions` · `.hero-keywords` |
| Số liệu | `.hero-stats` · `.row.g-0.stats` · `.stat-value` · `.stat-label` · `.stats-plain` |
| Card | `.card.card-hover` · `.feature-card` · `.project-card` · `.tag` · `.check-list` |
| Điều hướng | `.nav-underline` (tabs) · `.chips` / `.chip` (lọc — `data-filter-target` + `data-cat`) |
| Khối | `.feature-block` (+ `.blueprint`) · `.cta-band` · `.quote-card` · `.process` |
| Đối tác / chứng chỉ | `.logo-tile` · `.cert-badge` |
| Form | `.form-control` · `.form-select` · `.form-check` · `.upload-box` · `.search-field` · `.req` |
| Dashboard | `.kpi` · `.kpi-trend.up/.down` · `.progress` · `.bars` · `.donut` (`--v`) · `.legend` (`--c`) |
| Ảnh | `.media` + `.ph-city/-night/-sunset/-green/-site/-tech/-people` · `.media-4x3/-1x1/-21x9/-fill` |

### Ảnh

Hiện dùng placeholder (gradient + skyline). Thay ảnh thật bằng cách đặt `<img>` vào trong `.media`:

```html
<div class="media ph-city"><img src="assets/img/thanh-cong-tower.jpg" alt="Thành Công Tower" loading="lazy"></div>
```

Icon: Bootstrap Icons dạng line, cùng màu tiêu đề (`.icon-lg` 32px, `.icon-md` 24px).

---

## 8. SEO

Mỗi trang có:

- `<title>`, `meta description`, `robots`, `canonical`, `hreflang` (vi / en / x-default).
- Open Graph (`og:type`, `og:site_name`, `og:locale`, `og:title`, `og:description`, `og:url`, `og:image` 1200×630 + alt) và Twitter Card `summary_large_image`.
- JSON-LD: trang chủ có `Organization` + `WebSite` (SearchAction); các trang con có `WebPage` + `BreadcrumbList` (và `ContactPage`, `AboutPage`, `CollectionPage`, `Service` khi phù hợp).
- `theme-color`, `color-scheme`, favicon SVG + apple-touch-icon.
- `sitemap.xml`, `robots.txt`.

Ảnh OG nằm trong `assets/og/{slug}.jpg`, sinh tự động từ `scripts/pages.json`:

```bash
python3 scripts/build_seo_assets.py   # tạo lại ảnh OG, sitemap.xml, robots.txt
```

> Domain đang dùng là `https://lpc.vn` (giả định). Nếu khác, đổi `site` trong `pages.json`, chạy lại script và thay trong các thẻ `<head>`.

---

## 9. Thêm trang mới

1. Thêm mục vào `scripts/pages.json` → chạy `python3 scripts/build_seo_assets.py`.
2. Sao chép `index.html`, đổi `<head>` theo dữ liệu mới, đặt `<body data-page="{slug}">`.
3. Thêm vào menu trong `js/layout.js` (mảng `NAV`) nếu cần.
4. Kiểm tra ở 390px / 768px / 1440px, cả sáng và tối.
