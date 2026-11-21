# NguyenTrang Studio K12

> WEB TẠO VIDEO BÀI GIẢNG K12 — **nhánh thử nghiệm, chưa phát hành**.
> Không phải dự án APP HỌC TOÁN BẰNG TIẾNG ANH.

## Mã nguồn

- `index.html`: bản Studio Web 2.2 độc lập hiện có. **Giữ nguyên** trong đợt QA này.
- `prototypes/NguyenTrang_Studio_K12_Prototype_3_5_QA_Layout.html`: bản nguyên mẫu **3.5 QA**, 10 cảnh của bài **Toán 12 — Bài 1. Phép biến hình**; 6 giao diện, khung 16:9, dữ liệu bài giảng trong HTML.
- `tests/check_studio.py`: smoke check mã nguồn Web 2.2.
- `tests/check_prototype35.py`: kiểm tra 10 cảnh, dữ liệu, câu trắc nghiệm minh họa, 16:9, tham chiếu MathJax, và cú pháp JS.
- `.github/workflows/studio-staging-qa.yml`: chạy hai bài kiểm tra trên nhánh `ai/studio-qa-staging` và khi mở pull request vào `main`.

## Chạy kiểm thử mã nguồn

Yêu cầu Python 3 và Node.js trên PATH:

```bash
python3 tests/check_studio.py index.html
python3 tests/check_prototype35.py
```

**Giới hạn:** Các kiểm tra trên không chứng minh độ chính xác toàn bộ nội dung Toán học, không mô phỏng phát video, không kiểm chứng trình chiếu trên mọi thiết bị và không thay thế nghiệm thu của giáo viên.

## Danh mục cần nghiệm thu trước khi phát hành

- [ ] Đối chiếu đầy đủ 10 cảnh và lời thuyết minh với KHBD CD1-B1.
- [ ] Kiểm tra hình học/SVG, câu hỏi, đáp án, phép biến hình (f(x,y)=(x,ky)) và LaTeX khi **có kết nối MathJax**.
- [ ] Kiểm tra giao diện 16:9, chữ và hình không tràn ở chế độ toàn màn hình.
- [ ] Kiểm tra thao tác chỉnh sửa, nhập/xuất JSON, chuyển cảnh trên trình duyệt mục tiêu.
- [ ] Nếu bổ sung xuất video: xuất tệp thật, kiểm chứng tiếng/hình/định dạng, không đánh dấu MP4 đã làm khi chưa có.
- [ ] Xác minh build/Actions và trạng thái deployment độc lập.

## Chính sách phát hành

Các thay đổi QA chỉ nằm trên `ai/studio-qa-staging`. **Không tự động merge vào `main`, không triển khai Cloudflare production**. Bản Prototype 3.5 QA hiện là tài liệu/ứng dụng thử nghiệm trong kho, không phải phiên bản website chính thức. Chức năng xuất MP4 và nhập trực tiếp DOCX/PDF/PPTX chưa được xác nhận hoàn thành.
