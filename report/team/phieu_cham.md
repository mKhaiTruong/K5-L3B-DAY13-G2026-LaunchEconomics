# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): G2026 (`K5-L3B-DAY13-G2026-LaunchEconomics`)
- Nhóm được chấm: Pilot (`QuangNEU/K5-L3B-DAY13-Pilot-LaunchEconomics`, hồ sơ đọc tại commit `0b1006c`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 0 | Hồ sơ chưa có đề xuất (dòng cuối ghi "Chưa chốt"), nên không có kết luận để đối chiếu với số. Con số bất lợi có xuất hiện (xem lại 100% là 11.743–12.415 đ, simulated) nhưng chưa được dùng để ra quyết định |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ cột simulated đều có nhãn (hồ sơ mục 1–3, 7 và `simulated_inputs`). Phạm vi thu hẹp về noi_dia + hang_nang có lý do bằng số: 0,22× và 0,69× so với quoc_te 1,88× (thành công 27,3%) và doi_tac 0,85× |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo nhân viên 20 + 20, phân tầng theo depot, đối chứng cùng thời gian; 859 yêu cầu/nhóm, m ≥ 299, DE 6,96, ghi rõ đánh đổi power 0,64. 3 luật dừng có ngưỡng (+2 điểm / trần 6%, 8.000 đ, 40%), thời hạn (3 ngày, 2 tuần, 1 tuần) và người có quyền dừng (Giám đốc vận hành) |
| **Tổng** | | | | **20 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Số liệu ủng hộ pilot: trong phạm vi noi_dia + hang_nang, chi phí mỗi việc thành công đã cộng cố định là 4.599 đ, bằng 0,38 lần nhân viên tự làm (simulated). Kế hoạch pilot chia 20 + 20 nhân viên ngẫu nhiên, đủ cỡ mẫu (859 mỗi nhóm) và có luật dừng rõ ràng. Tuy nhiên hồ sơ chưa có đề xuất cuối, `chi_so.md` chưa có chỉ số và event nên chưa đo được chỉ số chính và chỉ số an toàn, người phụ trách vẫn ghi "chờ nhóm chốt". Điều kiện trước ngày bắt đầu: hoàn thiện ít nhất 6 event có `trace_id`, ghi vai trò phụ trách cho 7 mục, và chốt cách xử lý khi phải xem lại 100% (chi phí lên 0,98 đến 1,03 lần).

**Một câu hỏi cho đội trình:** Luật dừng an toàn của nhóm dựa vào tỉ lệ mở lại trong 7 ngày, nhưng `chi_so.md` chưa có event nào. Nhóm sẽ đo chỉ số này bằng event gì và nối với trace của agent như thế nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa kịp trao đổi trực tiếp tại buổi vì không đủ thời gian. Hội đồng gợi ý nhóm bổ sung danh sách event có `trace_id` trong `chi_so.md` để đo được chỉ số mở lại 7 ngày.
