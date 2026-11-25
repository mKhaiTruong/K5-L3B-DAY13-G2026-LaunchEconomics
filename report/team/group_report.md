# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: G2026
- Lớp: L3B
- Thành viên: xem `TEAM.md` (3 người: Khuê là nhóm trưởng, Phong, Khánh; gộp 4 vai của lab thành 3 theo issue #1)

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí của LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi con số tính bằng `src/lab13.py` trên 1.200 yêu cầu và 1.624 lần chạy giả lập; số tính từ cột `_simulated` ghi nhãn simulated. Nhóm làm theo issue #1 (phân công CP1–CP5), mỗi file có một chủ, mỗi thay đổi qua pull request có người review.

## 3. Giải pháp

- **A, B (chi phí, độ nhạy):** `src/lab13.py` và `report/team/bang_chi_phi.md`. Tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công; tách theo loại yêu cầu; cộng chi phí cố định 40 triệu đ/tháng; 9 kịch bản độ nhạy; so giới hạn 1, 2, 3 lần chạy; xem lại 100%.
- **C (lỗi):** `report/team/bang_loi.md`. Hai người gắn nhãn độc lập 20 ca, đồng thuận 18/20; quy tắc cho ca dễ lẫn và bảng khắc phục 5 ca (1, 20, 3, 11, 5), mỗi ca có event, ngưỡng đề xuất và một vai trò phụ trách.
- **D (pilot):** `report/team/pilot_plan.yaml`. Chia theo nhân viên 20 + 20 cụm, ngẫu nhiên, đối chứng cùng thời gian; phạm vi `noi_dia` + `hang_nang`; 3 luật dừng (an toàn, chi phí, sử dụng) đủ bốn vế.
- **E (chỉ số, hồ sơ):** `report/team/chi_so.md` (3 chỉ số, 12 event có `trace_id`, rủi ro kinh tế) và `report/team/ho_so_launch_v0.md` (bảy mục và đề xuất).

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%.
- Theo loại (so với 12.000 đ nhân viên tự làm) [simulated]: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88×. Cả hệ thống 5.865 đ/yêu cầu = 0,49×.
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại +51,8%, tỉ lệ xem lại +40,7%, lương +23,1%. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% chỉ còn 0,98× đến 1,03×.
- Chỉ số trong đợt chạy thử (chưa có đối chứng), phạm vi pilot: chính 92,26% · bỏ qua gợi ý 21,09% · mở lại 7 ngày 3,97%.
- Pilot: 859 yêu cầu/nhóm, hệ số thiết kế 6,96, 20 cụm mỗi nhóm; chỉ đo được mức chênh 6 điểm, power khoảng 0,64 nếu tác động thật chỉ 5 điểm.
- **Đề xuất của hồ sơ: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với 4 điều kiện có người phụ trách và ngày kiểm tra.
- Duyệt chéo: nhóm chấm nhóm Pilot (`report/team/phieu_cham.md`). Kết quả hội đồng chấm hồ sơ của nhóm mình: **30/30**.

## 5. Khó khăn và cách xử lý

- Nhóm chỉ có 3 người trong khi lab có 4 vai: gộp vai theo issue #1, đổi người viết code sau giải lao.
- Bản nháp ban đầu của hồ sơ có số và nội dung trùng bài mẫu, trước khi nhóm tự tính (nhóm trưởng phát hiện trên PR #5, #7): nhóm bỏ các số chưa tính, viết lại quy tắc và bảng khắc phục theo cách hiểu của mình.
- Nhãn độc lập: một thành viên đã trao đổi với AI về ca 7, 17, 20 trước khi gắn xong; nhóm không gắn lại mà khai báo và báo thêm đồng thuận khi bỏ ba ca này (16/17 = 94%).
- Ngưỡng luật dừng cần dựa vào mức hiện tại của chỉ số (mở lại 4,25%; 3,97% trong phạm vi): đặt trần tuyệt đối 3% sẽ dừng pilot ngay tuần đầu, nên dùng chênh so với đối chứng cộng một trần cao hơn mức hiện tại.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; cần thay bằng phút đo thật sau tuần 1 của pilot rồi tính lại chi phí.
- Đợt chạy thử không có nhóm đối chứng nên chưa kết luận được tác động của trợ lý lên chỉ số chính.
- Với 40 nhân viên, chia theo nhân viên chỉ đo được mức chênh 6 điểm; nếu tác động thật là 5 điểm thì power chỉ khoảng 0,64.
- Các ngưỡng luật dừng và ngưỡng phát hiện trong bảng khắc phục là đề xuất của nhóm, cần điều chỉnh bằng dữ liệu của pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, lớp `NormalIndPower`
- Đề bài, hướng dẫn và dữ liệu của lab trong `docs/` và `src/`
