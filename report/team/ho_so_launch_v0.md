# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: G2026 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token+tool/yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%. Cộng cố định 40 triệu đ/tháng (phạm vi noi_dia + hang_nang): 4.599 đ ở 45.000 yêu cầu/tháng | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi: +51,8% · 2. Tỉ lệ xem lại gấp đôi: +40,7% · 3. Lương +25%: +23,1% (giá token gấp đôi chỉ +5,6%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Cả hệ thống 5.865 đ/yêu cầu = 0,49× (đã cộng 222 ca nhân viên làm thay). Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te 1,88× [simulated]. Xem lại 100%: 0,98× (1,03× nếu làm lại 15,3 phút) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Phạm vi pilot (noi_dia + hang_nang, 982 yêu cầu), chỉ số trong đợt chạy thử: chính 92,26% (906/982) · dùng: bỏ qua gợi ý 21,09% (27/128) · an toàn: mở lại 7 ngày 3,97% (39/982). Cả mẫu 1.200: 82,83% · 27,12% · 4,25%. Không có nhóm đối chứng nên chưa kết luận tác động của trợ lý | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; hai người gắn nhãn độc lập trùng 18/20 = 90% (lệch ca 11 và 20); bỏ 3 ca đã nhắc trước với AI (7, 17, 20) còn 16/17 = 94%. Bảng khắc phục 5 ca (1, 20, 3, 11, 5), mỗi ca có event, ngưỡng đề xuất và một vai trò phụ trách (xem `bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên, 20 + 20 cụm, ngẫu nhiên, đối chứng cùng thời gian, phạm vi noi_dia + hang_nang; 859 yêu cầu/nhóm, hệ số thiết kế 6,96, chỉ đo được mức chênh 6 điểm (power khoảng 0,64 nếu tác động thật chỉ 5 điểm); 3 luật dừng đủ bốn vế (an toàn, chi phí, sử dụng), rollback 15 phút, ngày quyết định 2027-01-15 (xem `pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%) · Xem lại 100%: 11.743 đ (0,98×) · Khối lượng còn một nửa: 5.784 đ (0,48×) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ `noi_dia` + `hang_nang` (0,22× và 0,69× so với 12.000 đ [simulated]); loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×). Con số bất lợi nhóm đã biết: xem lại 100% chỉ còn 0,98× đến 1,03× [simulated], tức không tiết kiệm; cách chia theo 40 nhân viên chỉ đo được mức chênh 6 điểm, power khoảng 0,64 nếu thật là 5 điểm; chỉ số trong đợt chạy thử chưa có đối chứng. Điều kiện:

- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm và power 0,64 trước khi bắt đầu. Phụ trách: Giám đốc vận hành LogiX-VN. Kiểm tra: 2026-12-18.
- Chặn hoàn trùng bằng khoá `idempotency_key` theo `order_id` và đối soát sổ cái mỗi giờ (ca 20 trong `bang_loi.md`). Phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-12-18.
- Bật đủ event có `trace_id`; thay phút xem lại và làm lại giả lập bằng phút đo thật sau tuần 1, rồi tính lại chi phí mỗi việc thành công. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2027-01-08.
- Có kế hoạch giảm tỉ lệ xem lại theo bậc và rút ngắn mỗi lần xem lại dưới 5 phút, vì xem lại 100% không tiết kiệm. Phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2027-01-08.
