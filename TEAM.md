# Team

## Thông tin nhóm

- Tên nhóm: G2026
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-G2026-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/mKhaiTruong/K5-L3B-DAY13-G2026-LaunchEconomics · nhánh `main` · commit chốt: (điền khi nộp)

## Thành viên

| STT | Họ tên                | MSSV        | Email                       | GitHub            | Vai trò                             |
| --: | --------------------- | ----------- | --------------------------- | ----------------- | ----------------------------------- |
|   1 | Trương Đặng Minh Khuê | 2A202603785 | 26ai.khuetdm@vinuni.edu.vn  | mKhaiTruong       | A · Người viết code (trước giải lao), kiểm số ở CP4; tạo repo nhóm |
|   2 | Triệu Quốc Khánh      | 2A202603749 | 26ai.khanhtq4@vinuni.edu.vn | qockhah253        | C · Người gắn nhãn 2 kiêm giữ hồ sơ |
|   3 | Trịnh Tuấn Phong      | 2A202603781 | 26ai.phongtt2@vinuni.edu.vn | trinhtuanphong123 | B · Người gắn nhãn 1 kiêm người kiểm số; viết code sau giải lao |

Nhóm chỉ có 3 người nên một người kiêm hai vai (phân vai theo issue #1 của nhóm trưởng). Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-

## TruongDangMinhKhue-2A202603785

### Phần việc phụ trách

- Vai A · người viết code trước giải lao (CP1, CP2), người kiểm số ở CP4; tạo repo nhóm, phân vai trong issue #1, review và merge PR.
- CP1 · A1–A4 và CP2 · B1–B4 trong `src/lab13.py`; điền A1–A4 trong `report/team/bang_chi_phi.md`.
- CP3: công cụ `so_nhan()` tính tỉ lệ đồng thuận (không gắn nhãn).
- CP4: kiểm số D1 độc lập, soạn nháp D2 và phần đánh đổi.
- CP5 · E1: 3 chỉ số tính thử, 2 chỉ số đề xuất, 12 event có `trace_id` trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu; `quoc_te` 1,88× nên loại khỏi phạm vi.
- Bảng độ nhạy: làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]; giới hạn 2 lần chạy rẻ nhất cho cả hệ thống.
- Kiểm số D1 khớp 100% với code của B (1.251 · 3.103 · 1.000 · 300 · m ≥ 299 · power 0,64); đề xuất MDE 6 điểm.
- E1: 82,83% · 27,12% · 4,25% (cả mẫu) và 92,26% · 21,09% · 3,97% (phạm vi pilot).
- Review các PR #4–#10, #13–#15: phát hiện số chưa tính và nội dung trùng bài mẫu để nhóm viết lại trước khi merge.

### Bằng chứng

- PR #2 (CP1), #3 (CP2), #8 (CP3), #11 (CP5 · E1); issue #1 (phân vai, cập nhật tiến độ, nháp D2).
- Báo cáo cá nhân: `report/team/2A202603785_TruongDangMinhKhue.md`.
