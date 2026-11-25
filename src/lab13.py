"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
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


# ---------- Nhiệm vụ C · So hai bộ nhãn độc lập ----------
LOAI_LOI = ['Do người dùng', 'Hệ thống', 'Ngữ cảnh', 'Giới hạn hệ thống', 'Ngầm']


def so_nhan(duong_dan='../report/team/bang_loi.md'):
    """Đọc hai cột nhãn trong bảng lỗi rồi tính tỉ lệ đồng thuận.

    Chỉ đọc file, không ghi gì: hai người gắn nhãn tự điền cột của mình.
    Nhãn so sánh không phân biệt hoa/thường và khoảng trắng thừa.

    Args:
        duong_dan: Đường dẫn tới report/team/bang_loi.md (tính từ thư mục src/).

    Returns:
        Dict gồm: so_ca (số ca đã có đủ 2 nhãn), trung (số ca trùng), ti_le (trung / 20),
        lech (list số ca không trùng), sai_ten (list (ca, nhãn) không thuộc 5 loại PAIR).
        Ví dụ: {'so_ca': 20, 'trung': 17, 'ti_le': 0.85, 'lech': [4, 9, 15], 'sai_ten': []}.
    """
    hop_le = {loai.lower() for loai in LOAI_LOI}
    trung, lech, sai_ten, so_ca = 0, [], [], 0
    trong_muc = False
    with open(duong_dan, encoding='utf-8') as f:
        for dong in f:
            if dong.startswith('## '):
                # Chỉ đọc mục "Hai bộ nhãn độc lập"; bảng khắc phục phía sau cũng có cột số ca.
                trong_muc = 'Hai bộ nhãn' in dong
                continue
            if not trong_muc:
                continue
            o = [x.strip() for x in dong.strip().strip('|').split('|')]
            if len(o) != 5 or not o[0].isdigit():
                continue   # chỉ lấy dòng của bảng "Hai bộ nhãn độc lập"
            ca, n1, n2 = int(o[0]), o[1].lower(), o[2].lower()
            if '...' in (n1, n2) or not n1 or not n2:
                continue   # ca chưa gắn đủ hai nhãn
            so_ca += 1
            sai_ten += [(ca, n) for n in (o[1], o[2]) if n.lower() not in hop_le]
            if n1 == n2:
                trung += 1
            else:
                lech.append(ca)
    return dict(so_ca=so_ca, trung=trung, ti_le=trung / 20, lech=lech, sai_ten=sai_ten)


# ---------- Nhiệm vụ D1 · Cỡ mẫu cho pilot ----------
ICC = 0.02   # đề cho: mức giống nhau giữa các yêu cầu trong cùng một cụm (nhân viên / depot)


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.8):
    """Tính cỡ mẫu mỗi nhóm để phân biệt hai tỉ lệ p1 và p2.

    Công thức trong docs/du_lieu_va_cong_thuc.md (z chính xác, làm tròn lên):
    n = (z_{1-α/2}·√(2·p̄·(1-p̄)) + z_{1-β}·√(p1(1-p1) + p2(1-p2)))² / (p2 - p1)²

    Args:
        p1: Tỉ lệ hiện tại (nhóm đối chứng), ví dụ 0.70.
        p2: Tỉ lệ mục tiêu (nhóm dùng trợ lý), ví dụ 0.75.
        alpha: Mức ý nghĩa hai phía.
        power: Xác suất phát hiện được mức chênh khi nó có thật.

    Returns:
        Số yêu cầu mỗi nhóm (int), ví dụ 0.70 → 0.75 cho 1.251.
    """
    z_a = NormalDist().inv_cdf(1 - alpha / 2)    # 1,95996 với alpha 0,05
    z_b = NormalDist().inv_cdf(power)            # 0,84162 với power 0,8
    p_tb = (p1 + p2) / 2
    tu = (z_a * math.sqrt(2 * p_tb * (1 - p_tb))
          + z_b * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """Tính hệ số thiết kế (design effect) 1 + (m - 1)·ICC.

    Args:
        m: Số yêu cầu mỗi cụm.
        icc: Hệ số tương quan trong cụm.

    Returns:
        Hệ số thiết kế, ví dụ m = 75 → 2,48.
    """
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc=ICC):
    """Tính cỡ mẫu hiệu dụng c·m / hệ số thiết kế; luôn nhỏ hơn trần c / ICC.

    Args:
        c: Số cụm mỗi nhóm.
        m: Số yêu cầu mỗi cụm.
        icc: Hệ số tương quan trong cụm.

    Returns:
        Cỡ mẫu hiệu dụng mỗi nhóm (float).
    """
    return c * m / he_so_thiet_ke(m, icc)


def m_toi_thieu(n_can, c, icc=ICC):
    """Tính số yêu cầu mỗi cụm tối thiểu để c cụm đạt cỡ mẫu hiệu dụng n_can.

    Giải c·m / (1 + (m - 1)·icc) ≥ n_can  →  m ≥ n_can·(1 - icc) / (c - n_can·icc).

    Args:
        n_can: Cỡ mẫu hiệu dụng cần đạt mỗi nhóm.
        c: Số cụm mỗi nhóm.
        icc: Hệ số tương quan trong cụm.

    Returns:
        m nhỏ nhất (int), hoặc None nếu không có nghiệm (trần c / icc nhỏ hơn n_can).
    """
    if c <= n_can * icc:
        return None
    return math.ceil(n_can * (1 - icc) / (c - n_can * icc))


def power_hai_ti_le(p1, p2, n, alpha=0.05):
    """Tính power khi mỗi nhóm có n mẫu (đảo ngược công thức cỡ mẫu ở trên).

    Args:
        p1: Tỉ lệ nhóm đối chứng.
        p2: Tỉ lệ thật của nhóm dùng trợ lý.
        n: Cỡ mẫu (hiệu dụng) mỗi nhóm.
        alpha: Mức ý nghĩa hai phía.

    Returns:
        Xác suất pilot phát hiện được mức chênh p2 - p1, ví dụ n = 859, 0.70 → 0.75 cho ≈ 0,64.
    """
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    p_tb = (p1 + p2) / 2
    z_b = ((abs(p2 - p1) * math.sqrt(n) - z_a * math.sqrt(2 * p_tb * (1 - p_tb)))
           / math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))
    return NormalDist().cdf(z_b)


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

    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    print(f'\nB1 · kịch bản | cps [simulated] | thay đổi  (gốc {goc:,.0f} đ)')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = cps / goc - 1
        print(f'{ten:24s} {cps:>8,.0f} {thay_doi[ten]:>+8.1%}')
    # Tự kiểm tra: "giảm một nửa" = -½ mức tăng của "gấp đôi" (mô hình tuyến tính).
    for yeu_to in ('Giá token', 'Xem lại', 'Làm lại'):
        assert abs(thay_doi[f'{yeu_to} giảm một nửa'] + thay_doi[f'{yeu_to} gấp đôi'] / 2) < 1e-9

    # ---------- Nhiệm vụ B2 · Đổi một cặp ----------
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'\nB2 · token ×2 + xem lại ×2: {cps_cap:,.0f} đ ({cps_cap / goc - 1:+.1%}); '
          f'tổng hai tác động riêng {tong_rieng:+.1%} [simulated]')
    xep_hang = sorted(['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%'],
                      key=lambda t: abs(thay_doi[t]), reverse=True)
    print('Xếp hạng:', ' > '.join(f'{t} ({thay_doi[t]:+.1%})' for t in xep_hang[:3]))

    # ---------- Nhiệm vụ B3 · Giới hạn chạy lại: chi phí cả hệ thống ----------
    print('\nB3 · giới hạn | tổng trợ lý | không thành công | cả hệ thống | cps  [simulated]')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE   # nhân viên làm thay ca không thành công
        print(f'{k} lần {kq["tong"]:>14,.0f} {khong_tc:>6d} {he_thong:>14,.0f} {kq["cps"]:>8,.0f}')

    # ---------- Nhiệm vụ B4 · Xem lại 100% (noi_dia + hang_nang) ----------
    PHUT_XEM_LAI_MOI_YC = 5   # đề cho: mỗi yêu cầu xem lại 5 phút
    PHUT_LAM_LAI_DE = 9       # đề cho: mỗi ca làm lại 9 phút
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tien_ai = ((runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA).sum()
               + (runs_pv['tool_calls'] * GIA_TOOL).sum())
    tien_xem = co_ok * PHUT_XEM_LAI_MOI_YC * LUONG_PHUT
    tc_pv = kq_pv['thanh_cong']
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · {len(pham_vi)} yc, {co_ok} có lần chạy ok, {ca_lam_lai} ca lam_lai, token+tool {tien_ai:,.0f} đ')
    for nhan, phut_lam_lai in [('9 phút (đề)', PHUT_LAM_LAI_DE),
                               (f'{phut_lam_lai_tb:.1f} phút (TB cột simulated)', phut_lam_lai_tb)]:
        tien_lam = ca_lam_lai * phut_lam_lai * LUONG_PHUT
        tong_b4 = tien_ai + tien_xem + tien_lam
        cps_b4 = tong_b4 / tc_pv
        # Hoà vốn: số phút xem lại tối đa để cps = 12.000 đ.
        phut_hoa_von = (BASELINE * tc_pv - tien_ai - tien_lam) / (co_ok * LUONG_PHUT)
        print(f'làm lại {nhan:28s} tổng {tong_b4:>12,.0f} đ → {cps_b4:,.0f} đ = {cps_b4 / BASELINE:.2f}× '
              f'| hoà vốn khi xem lại ≤ {phut_hoa_von:.1f} phút [simulated]')
    # ---------- Nhiệm vụ C · Tỉ lệ đồng thuận ----------
    kq_nhan = so_nhan()
    if kq_nhan['so_ca'] < 20:
        print(f"\nC · mới có {kq_nhan['so_ca']}/20 ca đủ hai nhãn, chưa tính đồng thuận")
    else:
        dat = 'ĐẠT' if kq_nhan['trung'] >= 16 else 'CHƯA ĐẠT, viết lại định nghĩa trước khi đi tiếp'
        print(f"\nC · đồng thuận {kq_nhan['trung']}/20 = {kq_nhan['ti_le']:.0%} ({dat}); "
              f"ca lệch: {kq_nhan['lech'] or 'không có'}")
    if kq_nhan['sai_ten']:
        print(f"  nhãn không thuộc 5 loại PAIR: {kq_nhan['sai_ten']} (dùng đúng: {', '.join(LOAI_LOI)})")

    # ---------- Nhiệm vụ D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ----------
    # Dùng công thức tay của docs (ra 1.251) thay cho statsmodels (proportion_effectsize dùng arcsine, ra 1.250).
    P0, MDE = 0.70, 0.05
    SO_NHAN_VIEN = 40
    n_a = co_mau_hai_ti_le(P0, P0 + MDE)
    print(f'\nD1 · a) chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')

    m_b = 75
    de_b = he_so_thiet_ke(m_b)
    n_b = math.ceil(n_a * de_b)                 # cỡ mẫu cần khi chia cụm = n × hệ số thiết kế
    nv_b = math.ceil(n_b / m_b)
    du_nguoi = 'đủ người' if 2 * nv_b <= SO_NHAN_VIEN else 'KHÔNG đủ người'
    print(f'     b) theo nhân viên, m = {m_b}: hệ số thiết kế {de_b:.2f} → {n_b:,} yêu cầu mỗi nhóm '
          f'→ {nv_b} nhân viên mỗi nhóm, tổng {2 * nv_b} so với {SO_NHAN_VIEN} người: {du_nguoi}')

    for cau, c, don_vi in [('c', 20, 'nhân viên'), ('d', 6, 'depot')]:
        tran = c / ICC                           # cỡ mẫu hiệu dụng tối đa, kể cả khi m rất lớn
        dat = 'đạt' if tran >= n_a else 'KHÔNG đạt'
        print(f'     {cau}) {c} {don_vi} mỗi nhóm: cỡ mẫu hiệu dụng tối đa {c} / {ICC} = {tran:,.0f} '
              f'so với cần {n_a:,} → {dat}')

    n_e = co_mau_hai_ti_le(P0, P0 + 0.06)       # mức chênh 6 điểm
    m_e = m_toi_thieu(n_e, 20)
    print(f'     e) mức chênh 6 điểm ({n_e:,} mỗi nhóm), 20 nhân viên mỗi nhóm: m ≥ {m_e} yêu cầu mỗi người '
          f'(hệ số thiết kế {he_so_thiet_ke(m_e):.2f}, hiệu dụng {co_mau_hieu_dung(20, m_e):,.0f})')
    pw = power_hai_ti_le(P0, P0 + MDE, n_e)
    print(f'     Con số bất lợi: chọn mức chênh 6 điểm mà tác động thật chỉ 5 điểm thì power còn {pw:.2f}')

    # ---------- Nhiệm vụ D3 · Tỉ lệ mở lại hiện tại, trước khi đặt luật an toàn ----------
    for nhan, bang in [('cả mẫu', reqs), ('noi_dia + hang_nang', pham_vi)]:
        so_mo_lai = int(bang['mo_lai_trong_7_ngay'].sum())
        print(f'mo_lai_trong_7_ngay {nhan:20s}: {so_mo_lai}/{len(bang):,} = {so_mo_lai / len(bang):.2%}')
