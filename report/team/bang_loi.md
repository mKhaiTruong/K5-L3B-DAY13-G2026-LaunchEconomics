# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phong · Người gắn nhãn 2: Khánh (gắn độc lập, không trao đổi, trước khi so).

| Ca | Nhãn người 1 (Phong) | Nhãn người 2 (Khánh) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Ngầm | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Ngầm | Hệ thống | Không | Hệ thống |

**Tỉ lệ đồng thuận:** 18 / 20 = 90% (đạt ngưỡng 16/20 = 80%)

Ghi chú: người gắn nhãn 2 đã trao đổi với AI về ca 7, 17, 20 trước khi gắn xong. Bỏ 3 ca này, đồng thuận là 16/17 = 94% (chỉ lệch ca 11).

## Quy tắc phân biệt cho các ca không trùng và ca dễ lẫn

Hai ca không trùng là 11 và 20; các ca còn lại là quy tắc cho các ca dễ lẫn.


- **Ca 11 (Phong: Ngầm · Khánh: Giới hạn hệ thống):** gắn Giới hạn hệ thống vì trợ lý không thể xử lý tin nhắn thoại và đã nói rõ với khách; Ngầm chỉ dùng khi không ai biết.
- **Ca 20 (Phong: Ngầm · Khánh: Hệ thống):** gắn Hệ thống vì hoàn trùng là vi phạm thiết kế (thiếu khoá chống trùng) và lộ ra qua hai lệnh hoàn; Ngầm chỉ dùng khi lỗi không có tín hiệu nào cho tới khi kiểm tra mẫu.
- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** gốc lỗi là khách chọn sai mục / nhập sai mã; việc trợ lý không gợi ý là việc cần cải thiện, nằm ở cột khắc phục.
- **Ca 13 là Giới hạn hệ thống:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- **Ca 18 là Ngữ cảnh:** số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" không khớp hoàn cảnh.
- **Ca 12 là Ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí.
- **Ca 2 vs 17:** cả hai tính sai tiền, nhưng ca 2 có khách mở lại (đã lộ) → Hệ thống; ca 17 không ai mở lại trong 9 ngày → Ngầm.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" mà không có bản ghi `refund_ledger_write` kết quả ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do số tiền mà kiểm tra thấy đúng, theo tuần; ngưỡng > 1% yêu cầu/tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, theo loại yêu cầu, báo cáo hằng tuần | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot (thành công 27,3% [simulated]) | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần (`audit_sample_checked`) so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
