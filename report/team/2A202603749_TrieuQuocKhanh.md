# Báo cáo cá nhân — Triệu Quốc Khánh-2A202603749

## 1. Thông tin thành viên

- Họ tên: Triệu Quốc Khánh
- MSSV: 2A202603749
- Email: 26ai.khanhtq4@vinuni.edu.vn
- Vai trong nhóm (theo issue #1): C · người gắn nhãn 2 kiêm giữ hồ sơ (nhóm 3 người nên gộp vai)

## 2. Phần việc phụ trách

- CP1: điền `TEAM.md` và dựng khung `ho_so_launch_v0.md`; nắm các câu "cần hiểu" của CP1.
- CP2: trả lời B3 (giới hạn chạy lại) và B4 (xem lại 100%) trong `bang_chi_phi.md`.
- CP3: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2), viết quy tắc cho các ca dễ lẫn và bảng khắc phục 5 ca trong `bang_loi.md`.
- CP4: điền `pilot_plan.yaml` (phạm vi, luật dừng, rollback, chú thích D1 và D2).
- CP5: hoàn thiện `ho_so_launch_v0.md` (mục 4, 5, 6 và đề xuất cuối); bảo vệ trước hội đồng; `group_report.md`.

## 3. Đóng góp cụ thể

- **CP1:** điền thông tin thành viên và vai theo issue #1 trong `TEAM.md`; sửa hồ sơ theo nhận xét của nhóm trưởng trên PR #5 (bỏ các số của CP4 và CP5 khi nhóm chưa tự tính, đổi trạng thái về "Chưa" cho tới khi có bằng chứng).
- **CP2:** viết B3: giới hạn tối đa 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]) nhưng giới hạn 1 lần có chi phí mỗi việc thấp nhất (4.111 đ), vì đẩy thêm 85 việc (319 − 234) sang nhân viên. Viết B4: xem lại 100% cho 11.743 đ = 0,98× và 12.415 đ = 1,03× của 12.000 đ [simulated], hoà vốn khi mỗi lần xem lại ≤ 5,1 hoặc ≤ 4,8 phút.
- **CP3:** tự gắn nhãn 20 ca trên giấy trước khi so với Phong; đồng thuận 18/20 = 90% (lệch ca 11 và 20). Tự viết lại các quy tắc "ca dễ lẫn" (ca 13, 12, 18, 6, 9, 8, 15) và bảng khắc phục 5 ca (1, 20, 3, 11, 5) bằng cách hiểu của mình, sau khi nhóm trưởng nhận xét bản đầu trùng bài mẫu. Khai báo trong `bang_loi.md` rằng trong lúc trao đổi với AI, ca 7, 17, 20 đã được nhắc trước khi gắn xong nhãn; bỏ 3 ca này, đồng thuận là 16/17 = 94%.
- **CP4:** điền `pilot_plan.yaml` bằng số D1 của Phong (859/nhóm, hệ số thiết kế 6,96, 20 cụm); chọn phạm vi `noi_dia` + `hang_nang` dựa trên A3; viết 3 luật dừng có lý do cho từng ngưỡng; chuyển luật sử dụng sang số của phạm vi pilot (21,09% = 27/128).
- **CP5:** điền mục 4, 5, 6 và đề xuất Go có điều kiện cùng 4 điều kiện có người phụ trách và ngày kiểm tra trong `ho_so_launch_v0.md`.

## 4. Bằng chứng

- Pull request của mình trên repo nhóm: #5 (CP1), #6 (CP2, B3 và B4), #7 (CP3, bảng lỗi), #10 (CP4, `pilot_plan.yaml`), và #14 (CP5, hồ sơ launch v0).
- File: `TEAM.md`, `report/team/bang_chi_phi.md` (mục B3, B4), `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`.
- Con số mình đối chiếu với output `python lab13.py` của nhóm: 4.472 đ, 16,3 lần, B3 (k = 1, 2, 3), B4 (11.743 đ và 12.415 đ), D1 (1.251, 3.103, 1.000, 300, m ≥ 299), 4,25% và 3,97%.
- Nhãn độc lập: nhãn của mình ghi trong cột "Nhãn người 2" của `bang_loi.md`; ảnh nhãn viết tay của Phong được đưa lên PR #7.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code
- **Dùng vào việc gì:**
  - Giải thích khái niệm (tử số và mẫu số của chi phí mỗi việc thành công, cỡ mẫu hiệu dụng khi chia theo cụm, 5 loại lỗi, luật dừng).
  - Soạn bản nháp `lab13.py`, các file hồ sơ và bảng khắc phục để nhóm đối chiếu; chạy `lab13.py` và đọc output giúp mình.
  - Review bài của mình (B3, B4, quy tắc ca dễ lẫn) và chỉ chỗ cần sửa.
  - Soạn lệnh `git` và hướng dẫn mở pull request.
- **Chỗ AI làm sai hoặc làm vượt:**
  - Bản nháp ban đầu điền sẵn nhiều số của CP4 và CP5 và điều kiện giống bài mẫu trong `docs/`, trước khi nhóm tự tính. Nhóm trưởng phát hiện trên PR #5 và nhóm đã bỏ.
  - Bảng khắc phục và quy tắc ca dễ lẫn của bản đầu trùng gần nguyên văn bài mẫu; mình đã tự viết lại.
  - Các ngưỡng luật dừng ban đầu lấy theo bài mẫu; sau đó AI đề xuất số khác kèm lý do bằng số của nhóm. Các ngưỡng này vẫn là đề xuất, chưa được kiểm bằng dữ liệu của pilot.
  - Trong lúc trao đổi, AI nhắc tới ca 7, 17, 20 trước khi mình gắn xong nhãn; mình đã khai báo trong `bang_loi.md` theo yêu cầu của nhóm trưởng.
- **Cách mình tự kiểm tra:**
  - Chạy `python lab13.py` và đối chiếu từng số với bản trong hồ sơ (ba phép thử A1 ĐẠT, số khớp bài mẫu trong sai số 2%).
  - Gắn nhãn 20 ca trên giấy, không xem bảng nhãn tham khảo trước khi so với Phong.
  - Tự nói lại bằng lời của mình các câu "cần hiểu" (B3, B4, cỡ mẫu theo cụm) và chỉnh các chỗ AI nhận xét chưa đủ.
  - Nhờ nhóm trưởng và Phong review mọi PR trước khi merge.

## 6. Tự đánh giá

- Làm được: hiểu cách tính chi phí mỗi việc thành công và vì sao xem lại 100% không tiết kiệm; phân biệt được các loại lỗi (ngầm, hệ thống, giới hạn, ngữ cảnh, do người dùng); biết đọc và chọn ngưỡng luật dừng dựa vào số hiện tại của nhóm.
- Chưa tốt: ở bản đầu mình phụ thuộc nhiều vào bản nháp của AI, nên nhóm phải sửa lại nhiều chỗ trùng bài mẫu; các ngưỡng luật dừng mình chưa tự kiểm bằng dữ liệu pilot.
- Sẽ làm khác: tự gắn nhãn và tự viết bản đầu trước khi hỏi AI, rồi mới dùng AI để review.
