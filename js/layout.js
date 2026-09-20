/* LPC — header & footer DÙNG CHUNG cho mọi trang (Bootstrap 5.3 + Bootstrap Icons).
   Mỗi trang: <body data-page="home"> + <div data-include="header"></div> ... <div data-include="footer"></div>
   Nạp ở cuối <body>, TRƯỚC bootstrap.bundle.min.js không bắt buộc (dropdown/offcanvas dùng data-API).
   Chạy được qua file:// (không dùng fetch). */

(function () {
  "use strict";

  /* Logo thật (PNG nền trong suốt). Bản trắng tự hiện trên nền tối. */
  var LOGO =
    '<img class="logo-img logo-on-light" src="assets/img/logo-lpc-h.png" width="681" height="220" alt="LPC — Responsive to change">' +
    '<img class="logo-img logo-on-dark" src="assets/img/logo-lpc-h-white.png" width="681" height="220" alt="" aria-hidden="true">';

  /* Menu: [key, href, nhãn, (menu con)] */
  var NAV = [
    ["home", "index.html", "Trang chủ"],
    ["capabilities", "capabilities.html", "Năng lực", [
      ["capabilities", "capabilities.html", "Tổng quan năng lực"],
      ["engineering", "engineering.html", "Engineering"],
      ["digital-engineering", "digital-engineering.html", "Digital Engineering"],
      ["pm-cm", "pm-cm.html", "PM/CM"],
      ["digital-data", "digital-data.html", "Digital & Data"],
    ]],
    ["projects", "projects.html", "Dự án"],
    ["tech-hub", "tech-hub.html", "Tech Hub"],
    ["engineering-tools", "engineering-tools.html", "Engineering Tools"],
    ["industries", "industries.html", "Lĩnh vực"],
    ["sustainability", "sustainability.html", "Sustainability"],
    ["insights", "insights.html", "Insights"],
    ["about", "about.html", "Giới thiệu", [
      ["about", "about.html", "Giới thiệu LPC"],
      ["partners", "partners.html", "Đối tác"],
      ["trust-center", "trust-center.html", "Trust Center"],
    ]],
  ];

  var page = document.body.getAttribute("data-page") || "";

  function navItem(item) {
    var key = item[0], href = item[1], label = item[2], children = item[3];
    var isActive = key === page || (children && children.some(function (c) { return c[0] === page; }));
    if (!children) {
      return '<li class="nav-item"><a class="nav-link' + (isActive ? " active" : "") + '" href="' + href + '"' +
        (isActive ? ' aria-current="page"' : "") + ">" + label + "</a></li>";
    }
    var sub = children.map(function (c) {
      var on = c[0] === page;
      return '<li><a class="dropdown-item' + (on ? " active" : "") + '" href="' + c[1] + '"' +
        (on ? ' aria-current="page"' : "") + ">" + c[2] + "</a></li>";
    }).join("");
    return '<li class="nav-item dropdown">' +
      '<a class="nav-link dropdown-toggle' + (isActive ? " active" : "") + '" href="' + href + '" role="button" data-bs-toggle="dropdown" aria-expanded="false">' + label + "</a>" +
      '<ul class="dropdown-menu">' + sub + "</ul></li>";
  }

  var HEADER =
    '<a class="visually-hidden-focusable position-absolute top-0 start-0 m-2 btn btn-lpc btn-sm" href="#main">Bỏ qua đến nội dung</a>' +
    '<header class="site-header navbar navbar-expand-xl sticky-top">' +
    '<div class="container">' +
    '<a class="navbar-brand me-3 me-xl-4" href="index.html" aria-label="LPC — Trang chủ">' + LOGO + "</a>" +
    '<div class="d-flex align-items-center gap-2 ms-auto order-xl-last">' +
    '<button class="header-tool" type="button" data-bs-toggle="modal" data-bs-target="#searchModal" aria-label="Tìm kiếm"><i class="bi bi-search"></i></button>' +
    '<span class="lang-switch d-none d-sm-inline mx-1"><strong>VI</strong> | <a href="#" hreflang="en" lang="en">EN</a></span>' +
    '<button class="header-tool" type="button" data-theme-toggle aria-label="Chuyển giao diện sáng/tối"><i class="bi bi-moon-stars"></i></button>' +
    '<a class="btn btn-accent btn-arrow d-none d-md-inline-flex ms-1 ms-xxl-2" href="contact.html">Liên hệ<span class="d-none d-xxl-inline">&nbsp;/ RFP</span></a>' +
    '<button class="header-tool d-xl-none ms-1" type="button" data-bs-toggle="offcanvas" data-bs-target="#mainNav" aria-controls="mainNav" aria-label="Mở menu"><i class="bi bi-list fs-3"></i></button>' +
    "</div>" +
    '<div class="offcanvas offcanvas-end" tabindex="-1" id="mainNav" aria-labelledby="mainNavLabel">' +
    '<div class="offcanvas-header border-bottom">' +
    '<span class="offcanvas-title fw-bold" id="mainNavLabel">Menu</span>' +
    '<button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Đóng"></button>' +
    "</div>" +
    '<div class="offcanvas-body">' +
    '<ul class="navbar-nav mx-xl-auto gap-xl-1">' + NAV.map(navItem).join("") + "</ul>" +
    '<div class="d-xl-none mt-4 d-grid gap-3">' +
    '<a class="btn btn-accent btn-arrow" href="contact.html">Liên hệ / RFP</a>' +
    '<span class="lang-switch text-center"><strong>VI</strong> | <a href="#" hreflang="en" lang="en">EN</a></span>' +
    "</div></div></div>" +
    "</div></header>" +
    /* Modal tìm kiếm */
    '<div class="modal fade" id="searchModal" tabindex="-1" aria-labelledby="searchModalLabel" aria-hidden="true">' +
    '<div class="modal-dialog modal-dialog-centered modal-lg"><div class="modal-content">' +
    '<div class="modal-header"><h2 class="modal-title fs-6" id="searchModalLabel">Tìm kiếm</h2>' +
    '<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Đóng"></button></div>' +
    '<div class="modal-body"><form role="search" action="insights.html"><div class="search-field">' +
    '<i class="bi bi-search"></i><input class="form-control form-control-lg" type="search" name="q" placeholder="Tìm dự án, bài viết, công cụ..." aria-label="Từ khóa tìm kiếm">' +
    "</div></form></div></div></div></div>";

  var FOOTER =
    '<footer class="site-footer" data-bs-theme="dark">' +
    '<div class="container py-5">' +
    '<div class="row g-4 py-lg-3">' +
    '<div class="col-12 col-lg-3">' +
    '<a class="navbar-brand footer-brand" href="index.html" aria-label="LPC — Trang chủ">' + LOGO + "</a>" +
    '<p class="footer-tagline">Engineering<br>Technology<br>People<br>A better tomorrow</p>' +
    "</div>" +
    '<div class="col-6 col-md-4 col-lg-2"><h2>Năng lực</h2><ul>' +
    '<li><a href="engineering.html">Engineering</a></li>' +
    '<li><a href="digital-engineering.html">Digital Engineering</a></li>' +
    '<li><a href="pm-cm.html">PM/CM</a></li>' +
    '<li><a href="tech-hub.html">Tech Hub</a></li>' +
    '<li><a href="digital-data.html">Digital &amp; Data</a></li></ul></div>' +
    '<div class="col-6 col-md-4 col-lg-2"><h2>Tài nguyên</h2><ul>' +
    '<li><a href="engineering-tools.html">Engineering Tools</a></li>' +
    '<li><a href="projects.html">Dự án</a></li>' +
    '<li><a href="industries.html">Lĩnh vực</a></li>' +
    '<li><a href="insights.html">Insights</a></li>' +
    '<li><a href="trust-center.html">Trust Center</a></li></ul></div>' +
    '<div class="col-6 col-md-4 col-lg-2"><h2>Về LPC</h2><ul>' +
    '<li><a href="about.html">Giới thiệu</a></li>' +
    '<li><a href="partners.html">Đối tác</a></li>' +
    '<li><a href="sustainability.html">Phát triển bền vững</a></li>' +
    '<li><a href="about.html#tuyen-dung">Tuyển dụng</a></li>' +
    '<li><a href="contact.html">Liên hệ</a></li></ul></div>' +
    '<div class="col-12 col-lg-3">' +
    "<h2>Đăng ký nhận cập nhật</h2>" +
    "<p>Nhận thông tin công cụ mới, tài liệu kỹ thuật và case study.</p>" +
    '<form class="d-flex gap-2" onsubmit="event.preventDefault()">' +
    '<label class="visually-hidden" for="footerEmail">Email</label>' +
    '<input class="form-control" id="footerEmail" type="email" placeholder="Nhập email của bạn..." required>' +
    '<button class="btn btn-accent" type="submit">Đăng ký</button></form>' +
    '<div class="socials d-flex gap-3 mt-4">' +
    '<a href="#" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a>' +
    '<a href="#" aria-label="YouTube"><i class="bi bi-youtube"></i></a>' +
    '<a href="#" aria-label="Facebook"><i class="bi bi-facebook"></i></a></div>' +
    "</div></div></div>" +
    '<div class="footer-bottom"><div class="container d-flex flex-column flex-md-row justify-content-between gap-2 py-3">' +
    "<span>© 2026 LPC. All rights reserved.</span>" +
    '<span class="d-flex gap-3"><a href="#">Điều khoản</a><a href="#">Bảo mật</a><a href="sitemap.xml">Sitemap</a></span>' +
    "</div></div></footer>" +
    '<a href="#top" class="btn btn-lpc back-to-top" aria-label="Lên đầu trang"><i class="bi bi-arrow-up"></i></a>';

  function mount(name, html) {
    var el = document.querySelector('[data-include="' + name + '"]');
    if (el) el.outerHTML = html;
  }
  mount("header", HEADER);
  mount("footer", FOOTER);
  document.body.id = document.body.id || "top";

  /* ---- Sáng / tối ---- */
  var root = document.documentElement;
  function syncThemeIcon() {
    var dark = root.getAttribute("data-bs-theme") === "dark";
    document.querySelectorAll("[data-theme-toggle] .bi").forEach(function (i) {
      i.className = "bi " + (dark ? "bi-sun" : "bi-moon-stars");
    });
  }
  syncThemeIcon();
  document.addEventListener("click", function (e) {
    if (!e.target.closest("[data-theme-toggle]")) return;
    var next = root.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-bs-theme", next);
    try { localStorage.setItem("lpc-theme", next); } catch (err) {}
    syncThemeIcon();
  });

  /* ---- Chip / tab lọc: <div class="chips" data-filter-target="#grid"> <button class="chip" data-cat="bim">
          phần tử trong #grid có data-cat="bim hạ-tầng" ---- */
  document.addEventListener("click", function (e) {
    var chip = e.target.closest(".chip");
    if (!chip) return;
    var group = chip.closest(".chips");
    group.querySelectorAll(".chip").forEach(function (c) {
      c.classList.toggle("active", c === chip);
      c.setAttribute("aria-pressed", String(c === chip));
    });
    var target = group.getAttribute("data-filter-target");
    target = target && document.querySelector(target);
    if (!target) return;
    var cat = chip.getAttribute("data-cat") || "all";
    target.querySelectorAll("[data-cat]").forEach(function (item) {
      item.classList.toggle("d-none", cat !== "all" && item.getAttribute("data-cat").split(" ").indexOf(cat) < 0);
    });
  });

  /* ---- Nút lên đầu trang ---- */
  var toTop = document.querySelector(".back-to-top");
  if (toTop) {
    window.addEventListener("scroll", function () {
      toTop.classList.toggle("show", window.scrollY > 600);
    }, { passive: true });
  }
})();
