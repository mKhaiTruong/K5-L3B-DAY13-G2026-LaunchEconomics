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
- **Ca 13 là Giới hạn hệ thống, không phải Hệ thống:** vì hoàn phí bảo hiểm hàng hoá thuộc công ty đối tác, nằm ngoài phạm vi trợ lý có thể xử lý; Hệ thống chỉ dùng khi tác vụ nằm trong khả năng của trợ lý nhưng trợ lý làm sai so với thiết kế hoặc chính sách và lỗi đã lộ ra.
- **Ca 12 là Ngầm, không phải Hệ thống:** vì lỗi tool của depot D05 trả thiếu trường làm trợ lý phải gọi tool nhiều lần, kết quả vẫn đúng nhưng tốn gấp 3 tiền token suốt 3 tuần mà không ai biết; Hệ thống chỉ dùng khi sai sót so với thiết kế hoặc chính sách đã có người nhìn thấy (như khách mở lại, nhân viên bắt được hoặc lỗi hiện ra).
- **Ca 18 là Ngữ cảnh, không phải Hệ thống:** vì trợ lý đã tính đúng mức hoàn 50% (15.000 đ) theo chính sách và thiết kế, chỉ do tin nhắn thiếu giải thích cách tính khiến khách hiểu nhầm là hoàn thiếu; Hệ thống chỉ dùng khi bản thân trợ lý tính toán hoặc xử lý sai so với chính sách hoặc thiết kế.
- **Ca 6 là Do người dùng, không phải Hệ thống:** vì khách đã chọn nhầm mục "Hoàn phí giao trễ" ngay từ đầu trong khi vấn đề thực tế là hàng bị vỡ; Hệ thống chỉ dùng khi người dùng thao tác đúng nhưng trợ lý xử lý sai so với thiết kế hoặc chính sách.
- **Ca 9 là Do người dùng, không phải Hệ thống:** vì khách nhập sai loại mã (dùng mã đơn sàn thương mại điện tử thay vì mã vận đơn); Hệ thống chỉ dùng khi người dùng cung cấp đúng đầu vào theo yêu cầu nhưng trợ lý xử lý sai thiết kế hoặc chính sách.
- **Ca 8 là Hệ thống, không phải Ngầm:** vì trợ lý tự bịa căn cứ "Điều 7.2" không tồn tại trong chính sách hiện hành dù số tiền hoàn vẫn đúng, và lỗi này hiện trực tiếp ra nội dung tin nhắn; Ngầm chỉ dùng khi sai sót âm thầm diễn ra suốt thời gian dài mà không ai phát hiện cho tới khi kiểm tra.
- **Ca 15 là Hệ thống, không phải Ngầm:** vì trợ lý tính mức hoàn 100% thay vì 50% theo chính sách và đã bị nhân viên xem lại bắt được; Ngầm chỉ dùng khi lỗi không bị ai phát hiện trong thời gian dài và chỉ lộ ra khi kiểm tra định kỳ.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_account_validation_failed`; cảnh báo khi quá 3% số yêu cầu/ngày | Kiểm tra độ dài số tài khoản theo từng ngân hàng ngay lúc nhập; hiển thị tên chủ tài khoản để khách xác nhận | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: nhiều bản ghi `refund_ledger_write` có cùng `idempotency_key` hoặc cùng `order_id`; ngưỡng 0 ca | Gắn khoá chống trùng (`idempotency_key` theo `order_id`) vào lệnh hoàn; chặn lệnh hoàn thứ hai nếu đã có cùng khoá | Kỹ sư trưởng agent |
| 3 | Ngữ cảnh | Tỉ lệ `ticket_reopened` báo "chưa nhận tiền" dù `refund_ledger_write` ghi hoàn về ví đã ok, theo tuần; ngưỡng > 2% yêu cầu/tuần | Sửa mẫu tin nhắn ghi rõ "Đã hoàn về ví LogiX (không chuyển thẳng về ngân hàng)" kèm hướng dẫn rút tiền | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Event `unsupported_input_type` với `media_type = audio`, báo cáo hằng tuần; ngưỡng > 5% lượt chat/tuần | Ẩn nút ghi âm trên khung chat trợ lý hoàn phí và hiện gợi ý nhập chữ | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần (`audit_sample_checked`) so với tiền khách thực trả; ngưỡng 1% đơn hoàn thừa | Tính tiền hoàn theo số tiền khách thực trả (`actual_paid_amount`) thay vì giá gốc; chặn tự động nếu tiền hoàn lớn hơn tiền khách trả | Kế toán trưởng |

Ghi chú: các ngưỡng (3%, 2%, 5%, 1%) là đề xuất của nhóm, điều chỉnh sau tuần 1 của pilot. Hai event mới `bank_account_validation_failed` và `unsupported_input_type` cần thêm vào danh sách event trong `chi_so.md`.
