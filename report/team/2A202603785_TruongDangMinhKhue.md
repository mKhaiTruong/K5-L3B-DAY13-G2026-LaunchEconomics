# Báo cáo cá nhân — TruongDangMinhKhue-2A202603785

## 1. Thông tin thành viên

- Họ tên: Trương Đặng Minh Khuê
- MSSV: 2A202603785
- Email: 26ai.khuetdm@vinuni.edu.vn
- Vai trong nhóm: **A · Người viết code** (trước giải lao, CP1–CP2) và **người kiểm số** ở CP4. Nhóm có 3 người nên mình kiêm thêm: tạo repo nhóm, phân vai (issue #1), review và merge PR của các bạn.

## 2. Phần việc phụ trách

- CP1 · A1–A4: code mô hình chi phí mỗi việc thành công trong `src/lab13.py`, điền A1–A4 trong `bang_chi_phi.md`.
- CP2 · B1–B4: code 9 kịch bản độ nhạy, cặp kịch bản, giới hạn số lần chạy, xem lại 100%.
- CP3: công cụ `so_nhan()` tính tỉ lệ đồng thuận từ hai cột nhãn (không gắn nhãn, vì nhãn do B và C gắn độc lập).
- CP4: kiểm số D1 độc lập với code của B; soạn nháp 5 câu D2 và phần đánh đổi cho C.
- CP5 · E1: tính thử 3 chỉ số, đề xuất 2 chỉ số mới, danh sách 12 event có `trace_id` trong `chi_so.md`.
- Điều phối: chia việc trong issue #1, review và merge PR, cập nhật tiến độ cho nhóm.

## 3. Đóng góp cụ thể

- **Mô hình chi phí (CP1):** tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong` → **4.472 đ/việc thành công [simulated], gấp 16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ). Chỉ ra `quoc_te` là 1,88× so với 12.000 đ và chạy lại không giúp (tỉ lệ ok theo lần thử 30% → 11,4% → 2,2%).
- **Độ nhạy (CP2):** xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) nhưng giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ).
- **CP3:** `so_nhan()` cho kết quả 18/20 = 90%, lệch ca 11 và 20, khớp số C ghi tay. Đề xuất ghi minh bạch việc người gắn nhãn 2 đã bàn với AI về ca 7, 17, 20 (bỏ 3 ca vẫn đạt 16/17 = 94%) thay vì gắn lại nhãn.
- **CP4:** kiểm số D1 độc lập (scipy + statsmodels) khớp 100% với code của B: 1.251 · DE 2,48 → 3.103 · 1.000 · 300 · m ≥ 299 (DE 6,96) · power 0,64. Đề xuất MDE 6 điểm và tính thêm: m ≥ 299 tương đương khoảng 10 ngày làm việc, nên pilot 2 tuần là khả thi.
- **CP5:** 82,83% · 27,12% · 4,25% trên cả mẫu và 92,26% · 21,09% · 3,97% trong phạm vi pilot; tên event dùng lại đúng tên nhóm đã đặt ở `bang_loi.md` và `pilot_plan.yaml`.
- **Review:** phát hiện số CP4/CP5 và bảng khắc phục, luật dừng chép từ bài mẫu trong các PR #5, #7, #10, soạn comment để các bạn viết lại bằng lời của nhóm trước khi merge.

## 4. Bằng chứng

| Việc | PR | Commit |
| --- | --- | --- |
| CP1 · A1–A4 | #2 | `37dc6b4` |
| CP2 · B1–B4 | #3 | `97f14ef` |
| CP3 · `so_nhan()` (và sửa lỗi đọc nhầm bảng khắc phục) | #8 | `3b6dc2b`, `4feda27` |
| CP5 · E1 + event | #11 | `686e569` |
| Phân vai, cập nhật tiến độ, nháp D2 | issue #1 | comment tiến độ CP1 → CP4 |
| Review, kiểm số độc lập | #4, #5, #6, #7, #9, #10, #13, #14, #15 | comment review trên từng PR |

Chạy lại: `cd src && python lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT" và đủ các bảng A → E1.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Opus):**
  - viết code CP1, CP2, `so_nhan()` (CP3), mục E1 (CP5) trong `src/lab13.py`;
  - điền số vào `bang_chi_phi.md` (A1–A4) và `chi_so.md` (E1, event);
  - đọc diff, gộp thử PR trong worktree tạm, soạn comment review và nháp D2;
  - không dùng AI để gắn nhãn CP3 hay chọn kết luận thay nhóm.
- **Cách tự kiểm tra:**
  - ba phép thử đáp án biết trước của A1 phải ĐẠT trước khi tính tiếp;
  - đối chiếu mọi số A–E với số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch 0%, B4 lệch 1 đ do làm tròn 15,3 phút);
  - kiểm D1 bằng script riêng ngoài repo, dùng thư viện khác với code của B;
  - test `so_nhan()` trên bản copy có nhãn giả (lệch 3 ca, nhãn gõ sai) trước khi dùng;
  - trước mỗi lần merge: gộp thử, chạy `lab13.py`, `yaml.safe_load`, `grep` dấu `?` và từ cấm theo quy tắc 5 trong README.

## 6. Tự đánh giá

- **Làm tốt:** code chạy hết từ A đến E, số khớp đáp án; giữ được nguyên tắc tự kiểm tra trước khi tin số (đặc biệt kiểm số D1 độc lập); review kỹ để hồ sơ không chép số hay câu chữ từ bài mẫu.
- **Chưa tốt:** dựa nhiều vào AI cho phần code nên cần tự giải thích lại được cỡ mẫu hiệu dụng và hệ số thiết kế; hai lần kết luận PR sớm khi chưa fetch bản mới nhất của bạn trong nhóm.
- **Bài học:** tử số tính mọi lần chạy, mẫu số chỉ đếm việc thành công; với 40 nhân viên, số cụm (không phải tổng số yêu cầu) quyết định cỡ mẫu.
