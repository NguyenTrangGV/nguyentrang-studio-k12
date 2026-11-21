# Kiểm định phát hành Prototype 3.5 — Studio K12

Trạng thái: **CHƯA ĐỦ ĐIỀU KIỆN PHÁT HÀNH**. Đây là checklist; việc đánh dấu chỉ dựa trên bằng chứng thực tế.

## Cổng tự động
- [x] Mã nguồn HTML Prototype 3.5 nằm trong `prototypes/` trên nhánh staging.
- [x] Có bộ kiểm thử tĩnh `tests/check_prototype35.py`: 10 cảnh, ID duy nhất, lời thuyết minh, nguồn, đáp án trắc nghiệm cảnh 9, JavaScript và cấu hình 16:9.
- [x] GitHub Actions đã chạy thành công ít nhất một lần trên Pull Request nháp.
- [ ] Kiểm thử trình duyệt thực tế (Chromium): mở 10 cảnh, không lỗi console, không tràn chữ.
- [ ] Kiểm tra hiển thị trên điện thoại và màn hình 16:9.
- [ ] Kiểm thử nhập/xuất JSON với dữ liệu lỗi và dữ liệu lớn.

## Cổng sư phạm Toán 12
- [ ] Đối chiếu từng cảnh với giáo án nguồn và kiểm tra ký hiệu, định nghĩa, giả thiết.
- [ ] Xác minh hình minh họa phép chiếu vuông góc và biến đường tròn thành elip.
- [ ] Kiểm tra công thức `f(x,y)=(x,ky)`, `k>0`, `k≠1`, và các trường hợp co/dãn.
- [ ] Kiểm tra toàn bộ câu hỏi và đáp án độc lập, không chỉ bằng khớp chuỗi.

## Cổng bảo mật và phát hành
- [ ] Kiểm thử an toàn khi nhập SVG/JSON tùy ý (không coi regex là cơ chế khử độc hoàn chỉnh).
- [ ] Xác minh nguồn CDN và phương án dự phòng khi mất mạng.
- [ ] Xuất MP4 thực tế, kiểm tra âm thanh/hình ảnh và tải tệp thành công.
- [ ] Được người phụ trách duyệt trước khi merge `main` hoặc triển khai Cloudflare.

**Quy tắc:** không tự động merge, không tự động triển khai production. CI xanh chỉ chứng nhận những kiểm tra mà CI thật sự thực hiện.
