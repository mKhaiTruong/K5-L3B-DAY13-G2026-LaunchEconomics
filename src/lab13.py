"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Tính số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.

    Công thức: (1 - (1 - p)^k) / p; khi k=None (chạy đến khi đúng) giới hạn là 1 / p.

    Args:
        p: Xác suất một lần chạy đúng, trong (0, 1].
        k: Số lần chạy tối đa; None nghĩa là chạy lại đến khi đúng.

    Returns:
        Kỳ vọng số lần chạy, ví dụ p=0.8, k=2 → 1.20.
    """
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Tính xác suất yêu cầu thành công sau tối đa k lần chạy.

    Args:
        p: Xác suất một lần chạy đúng, trong (0, 1].
        k: Số lần chạy tối đa; None nghĩa là chạy lại đến khi đúng (luôn thành công).

    Returns:
        Xác suất thành công 1 - (1 - p)^k.
    """
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Tính chi phí mỗi việc thành công theo bội số giá một lần chạy.

    Bằng số lần chạy kỳ vọng chia xác suất thành công; với mọi k kết quả là 1 / p.

    Args:
        p: Xác suất một lần chạy đúng, trong (0, 1].
        k: Số lần chạy tối đa; None nghĩa là chạy lại đến khi đúng.

    Returns:
        Hệ số chi phí, ví dụ p=0.8, k=3 → 1.25.
    """
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.

    Args:
        runs: Bảng lần chạy (logix_runs.csv); tự lọc theo request_id có trong reqs.
        reqs: Bảng yêu cầu (logix_requests.csv), có thể là một tập con (vd 1 loai).
        gia_vao: Giá 1.000 token đầu vào (đ).
        gia_ra: Giá 1.000 token đầu ra (đ).
        gia_tool: Giá 1 lần gọi tool (đ).
        luong_phut: Chi phí 1 phút nhân viên (đ).
        he_so_xem_lai: Hệ số nhân tiền xem lại.
        he_so_lam_lai: Hệ số nhân tiền làm lại.
        max_lan_chay: Giới hạn số lần chạy; yêu cầu vượt giới hạn coi là chuyen_nhan_vien.

    Returns:
        Dict các khoản (đ): token, tool, chay_lai (phần của attempt > 1), xem_lai, lam_lai,
        tong, thanh_cong (số việc), cps, hoa_don_moi_yc (token + tool chia số yêu cầu).
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"{'gấp hoá đơn':12s} {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14.1f} lần")
    for khoan in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f"  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:>8.1%}")
    chuyen_nv = int((reqs['ket_qua'] != 'thanh_cong').sum())
    he_thong = (ket_qua['tong'] + chuyen_nv * BASELINE) / len(reqs)
    print(f'Cả hệ thống mỗi yêu cầu (+{chuyen_nv} ca không thành công × 12.000 đ): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · loai | số yc | tỉ lệ thành công | lần chạy/yc | cps [simulated] | so với 12.000')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, con)
        print(f"{loai:10s} {len(con):>5d} {kq['thanh_cong'] / len(con):>8.1%} "
              f"{con['so_lan_chay'].mean():>8.2f} {kq['cps']:>10,.0f} {kq['cps'] / BASELINE:>7.2f}×")

    # Tỉ lệ ok theo từng lần thử: chạy lại có giúp không?
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']], on='request_id')
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('\nTỉ lệ ok theo attempt:\n' + ok_theo_lan.round(3).to_string())

    # ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    CHI_PHI_CO_DINH = 40_000_000   # đ / tháng
    YC_THANG = 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    print(f"\nA4 · phạm vi noi_dia + hang_nang: cps {kq_pv['cps']:,.0f} đ, "
          f"{kq_pv['thanh_cong']} thành công / {len(reqs)} yc mẫu")
    for nhan, khoi_luong in [('45.000 yc/tháng', YC_THANG), ('một nửa', YC_THANG // 2)]:
        tc_thang = khoi_luong * kq_pv['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong_viec = kq_pv['cps'] + co_dinh
        print(f'{nhan:16s} thành công/tháng {tc_thang:>8,.0f} | cố định/việc {co_dinh:>6,.0f} đ | '
              f'cps + cố định {tong_viec:>6,.0f} đ = {tong_viec / BASELINE:.2f}× [simulated]')

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
