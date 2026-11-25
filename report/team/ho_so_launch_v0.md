# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Gate 2a chỉ duyệt kế hoạch pilot, không duyệt chạy chính thức. Mọi số dựa trên cột `_simulated` ghi [simulated].

Nhóm: G2026 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hoá đơn token+tool/yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%. Cộng cố định 40 triệu đ/tháng (phạm vi noi_dia + hang_nang): 4.599 đ ở 45.000 yêu cầu/tháng | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi: +51,8% · 2. Tỉ lệ xem lại gấp đôi: +40,7% · 3. Lương +25%: +23,1% (giá token gấp đôi chỉ +5,6%) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm (12.000 đ) | Cả hệ thống 5.865 đ/yêu cầu = 0,49× (đã cộng 222 ca nhân viên làm thay). Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te 1,88× [simulated]. Xem lại 100%: 0,98× (1,03× nếu làm lại 15,3 phút) | Giả lập | Giám đốc tài chính |
| 4 · Chỉ số chính, dùng, an toàn | Chính 82,83% (994/1.200) · Dùng: bỏ qua gợi ý 27,12% (48/177) · An toàn: mở lại 7 ngày 4,25% (51/1.200). Đây là chỉ số trong đợt chạy thử, không có đối chứng | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; 5 ca có cách phát hiện đo được và người phụ trách (xem `bang_loi.md`). Đồng thuận hai người gắn nhãn: (điền)/20 | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20 cụm, ngẫu nhiên, đối chứng cùng thời gian; 859 yêu cầu/nhóm, DE 6,96, chênh 6 điểm (power ~0,64 nếu thật là 5 điểm); 3 luật dừng đủ bốn vế; quyết định 2027-01-05 | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%) · Xem lại 100%: 11.743 đ (0,98×) · Khối lượng còn một nửa: 5.784 đ (0,48×) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×). Con số bất lợi cần nêu rõ: xem lại 100% gần như không tiết kiệm (0,98×–1,03×); cách chia chưa đủ mẫu cho mức chênh 5 điểm (power ~0,64); tỉ lệ mở lại 4,25% [simulated] chưa có đối chứng. Điều kiện:

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu. Phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-12-20.
- Ký chấp nhận mức chênh 6 điểm (power ~0,64 ở mức 5 điểm). Phụ trách: Giám đốc vận hành LogiX-VN. Kiểm tra: 2026-12-20.
- Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật sau tuần 1. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2027-01-05.
- Kế hoạch giảm xem lại theo bậc (xem lại 100% không tiết kiệm, B4). Phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2027-01-05.
