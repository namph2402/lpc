/* Đặt giao diện sáng/tối trước khi trang render (nạp đồng bộ trong <head>).
   Thứ tự ưu tiên: lựa chọn đã lưu → cài đặt hệ điều hành. */
(function () {
  var saved = null;
  try { saved = localStorage.getItem("lpc-theme"); } catch (e) {}
  var theme = saved || (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  document.documentElement.setAttribute("data-bs-theme", theme);
})();
