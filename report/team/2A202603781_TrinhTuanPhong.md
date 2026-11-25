# Báo cáo cá nhân — TrinhTuanPhong-2A202603781

## 1. Thông tin thành viên

- Họ tên: Trịnh Tuấn Phong
- MSSV: 2A202603781
- Email: 26ai.phongtt2@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người kiểm số + người gắn nhãn 1 (vai B); người viết code sau giải lao (CP4). Nhóm 3 người gộp 4 vai, xem `TEAM.md`.

## 2. Phần việc phụ trách

- CP1: kiểm số độc lập bảng A1–A4 trong `report/team/bang_chi_phi.md`.
- CP2: điền bảng B1 (9 kịch bản) và B2 (đổi một cặp, xếp hạng), kiểm luật "giảm một nửa".
- CP3: gắn nhãn độc lập 20 ca lỗi với vai người gắn nhãn 1.
- CP4: viết code D1 (5 câu cỡ mẫu) và tỉ lệ `mo_lai_trong_7_ngay` trong `src/lab13.py`.
- CP5: 2 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`; chấm nhóm cùng bàn trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- CP1: tính tay đối chiếu với code của A. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); A3 4/4 dòng và A4 2/2 dòng khớp code, lệch 0%. Ghi kết quả kiểm vào comment ở PR #2.
- CP2: B1 9 dòng, ví dụ số ca làm lại gấp đôi → 6.787 đ (+51,8%), tỉ lệ xem lại gấp đôi → 6.292 đ (+40,7%) [simulated]. Luật "nửa" đúng cả 3 cặp (5,6 → 2,8 · 40,7 → 20,3 · 51,8 → 25,9). B2: token ×2 cùng xem lại ×2 = 6.543 đ (+46,3%), đúng bằng tổng hai tác động riêng. Xếp hạng: làm lại · xem lại · lương nhân viên.
- CP3: bộ nhãn người 1; đồng thuận với người 2 là 18/20 = 90% (lệch ca 11 và 20).
- CP4: 5 hàm `co_mau_hai_ti_le`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `m_toi_thieu`, `power_hai_ti_le`. Kết quả: cần 1.251 yêu cầu mỗi nhóm; hệ số thiết kế 2,48 → cần 42 nhân viên mỗi nhóm (84 > 40, không đủ); muốn 20 + 20 nhân viên thì mỗi người cần ≥ 299 yêu cầu; nếu chọn mde 6 điểm mà tác động thật 5 điểm thì power chỉ 0,64. Tỉ lệ mở lại trong 7 ngày: 51/1.200 = 4,25%, phạm vi noi_dia + hang_nang 39/982 = 3,97%.
- CP5: E2 hai dòng rủi ro. (1) Số ca làm lại gấp đôi: +51,8%, lên 6.787 đ [simulated], vượt ngưỡng dừng 6.000 đ; theo dõi tỉ lệ làm lại theo tuần > 7% (hiện 4,9%). (2) Phải xem lại 100%: 0,98× đến 1,03× của 12.000 đ [simulated]; theo dõi phút xem lại đo thật > 5,1 phút (hiện 5,0 phút [simulated]).
- CP5: chấm nhóm Pilot (chấm trong bàn): 20/30, chi tiết từng tiêu chí trong `report/team/phieu_cham.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit 19358c5 "CP2: điền B1, B2 trong bang_chi_phi.md (B kiểm số)", PR #4: bảng B1, B2 trong `report/team/bang_chi_phi.md`.
- Commit e700f79 "CP4: code D1 cỡ mẫu và tỉ lệ mở lại (B viết code sau giải lao)", PR #9: `src/lab13.py`, các hàm D1 và phần in D1.
- Commit 9ea7596 "CP5: viết 2 dòng rủi ro kinh tế E2 trong chi_so.md (B)", PR #12: bảng E2 trong `report/team/chi_so.md`.
- Cột "Nhãn người 1 (Phong)" trong `report/team/bang_loi.md`.
- Comment kiểm số ở PR #2; merge PR #2 và PR #3.
- `report/team/phieu_cham.md`: phiếu chấm nhóm cùng bàn.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Công cụ: Claude Code chạy trong terminal.
- Dùng vào: tóm tắt tài liệu lab và các khái niệm (chi phí mỗi việc thành công, độ nhạy, cỡ mẫu hai tỉ lệ, hệ số thiết kế); kiểm số A1–A4 bằng script pandas chỉ đọc CSV; điền bảng B1, B2 theo số đã kiểm; viết code D1 theo 4 quyết định em chốt (công thức tay, công thức đóng cho câu e, tách hàm, in thêm power); nháp 2 dòng rủi ro E2; soạn tin nhắn nhóm và mô tả PR.
- Không dùng AI cho: bộ nhãn CP3 (em tự gắn, không trao đổi với ai); điểm và nhận xét trong phiếu chấm.
- Cách tự kiểm: mỗi con số so 3 nguồn (output `python src/lab13.py`, tính tay, số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`), lệch phải ≤ 2%; power ở CP4 đối chiếu với `statsmodels` (0,6417 so với 0,64); sau khi sửa `lab13.py` chạy lại và so phần output cũ không đổi; quét từ cấm trong `report/team` bằng `grep` trước mỗi lần push.
- Các số AI hỗ trợ tính (bảng B1, B2 và D1 a–e), em đã tự tính lại bằng tay theo công thức, kết quả trùng với bảng và output của `lab13.py`.

## 6. Tự đánh giá

**Làm tốt**

- Kiểm số độc lập bằng 3 nguồn (code, tính tay, docs). A1–A4 và B1 lệch 0%, nên nhóm tin được bảng chi phí trước khi viết hồ sơ.
- Code D1 cho thấy 40 nhân viên là không đủ: cần 84 người, hệ số thiết kế 2,48. Nhờ vậy pilot phải đổi thiết kế (≥ 299 yêu cầu mỗi nhân viên) thay vì chạy rồi mới phát hiện không ra được kết luận.
- Gắn nhãn độc lập, đồng thuận 18/20 = 90% với người gắn nhãn 2.
- Làm theo nhánh ngắn và PR có ghi CP và file. Không gây conflict trên src/lab13.py khi đổi người viết code.

**Học được**

- Chi phí mỗi việc thành công gấp 16,3 lần hoá đơn token chia số yêu cầu, vì giờ nhân viên xem lại và làm lại chiếm 92,5%. Theo dõi tỉ lệ làm lại quan trọng hơn theo dõi giá token.
- Chạy lại không cứu được lỗi lặp: quoc_te thành công theo từng lần chạy chỉ còn 30% → 11,4% → 2,2%.
- Với dữ liệu theo cụm, số nhân viên quyết định cỡ mẫu chứ không phải số yêu cầu. Cỡ mẫu hiệu dụng không vượt quá c ÷ ICC.

