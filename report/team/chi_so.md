# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) · phạm vi noi_dia + hang_nang: 92,26% (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) · phạm vi: 21,09% (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200) · phạm vi: 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý mà nhân viên có mở gợi ý | Số `request_id` của `arm = tro_ly` có ít nhất 1 `assistant_opened`, chia số `refund_request_created` của `arm = tro_ly`. Cùng công thức cho `arm = doi_chung` để đo tràn tác động (mục tiêu 0, khớp D2 câu 3 trong `pilot_plan.yaml`) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn bị hoàn trùng | Số `order_id` có từ 2 bản ghi `refund_ledger_write` kết quả ok trở lên, chia số `order_id` đã ghi sổ; mục tiêu 0 (bắt lỗi như ca 20 trong `bang_loi.md`) | Không cần tính |

Số tính bằng `src/lab13.py` (mục E1). Đợt chạy thử không có nhóm đối chứng, nên đây là **chỉ số trong đợt chạy thử**, chưa phải tác động của trợ lý.

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, order_id, loai, so_tien_vnd, depot, arm (`tro_ly` / `doi_chung`), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status (`ok` / `loi`), trace_id | Sau **mỗi** lần chạy, kể cả lần lỗi (tử số chi phí) |
| `assistant_opened` | Giao diện nhân viên | staff_id, arm, request_id, trace_id | Khi nhân viên mở gợi ý của trợ lý |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (`giu` / `sua` / `bo`), phut_xem_lai (đo thật), trace_id | Khi bấm gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong một ca trả lời sai |
| `refund_ledger_write` | Dịch vụ sổ cái | order_id, idempotency_key, so_tien, ket_qua, trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `handoff_to_staff` | Agent | reason (`thieu_du_lieu` / `het_lan_chay` / `ngoai_pham_vi`), tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, 100 đơn mẫu |
| `bank_account_validation_failed` | App khách | ngan_hang, ly_do, trace_id | Khi số tài khoản nhập sai định dạng (ca 1) |
| `unsupported_input_type` | Agent | media_type, trace_id | Khi khách gửi đầu vào trợ lý không xử lý được (ca 11) |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính:** `ticket_closed` (closed_at − thời điểm `refund_request_created` ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- **Dùng (bỏ qua gợi ý):** `staff_review_decision` có quyet_dinh `sua` hoặc `bo`, chia tổng số `staff_review_decision`.
- **An toàn (mở lại):** số `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- **Dùng (tự đề xuất):** `assistant_opened` chia `refund_request_created`, tách theo arm.
- **An toàn (tự đề xuất):** `refund_ledger_write` nhóm theo `order_id`, đếm order có từ 2 bản ghi ok.
- **Chi phí mỗi việc thành công** (để thay số simulated sau tuần 1): `agent_run_completed` (token + tool, mọi lần chạy) + `staff_review_decision`.phut_xem_lai + `staff_rework_completed`.phut_lam_lai, chia số việc thành công (đóng, không mở lại, `audit_sample_checked` không lệch tiền).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
