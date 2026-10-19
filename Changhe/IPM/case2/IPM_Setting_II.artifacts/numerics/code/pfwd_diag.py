"""Diagnostics for forward x-even states (numerical researcher, 2026-10-18).

core_term(S, rho):  the r < r_min part of the strain moment c = psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX, with rho/r^2 frozen at the
    first ring: (r_min/pi) int (rho/r^2)(r_min, th) sin 3th dth  (specification M25(f); verifier V54(i) confirmed formula and size, 1.8e-3 at
    r_min = e^-12 on the N = 6 state).  m1 = 1/p - (c_moment + core).
axis_D(S, g, Wr, p, m1):  the y-axis quantities of specification M25(h) (referee result 17, audited by a referee and in V54(iii)) computed from the state alone,
    no orbit tracing:  h = rho_xx(0, +-r) = r^(p-2) d^2 g/dth^2 at 90/270 deg (spectral), B_+- = outward axis speed l r + W_r,
    a = d_x V_1 = 2l - dB/dr, k from B k' = (m1 - a) k with k(0) = 1 (inner tail C e^t fitted on the first two log-decades, V59),
    law = int (1 - 2 m1)/B dr, q = log h - 2 log k - law (constant on each half-axis for an exact stationary state).
        D_ax_k      = q_down(r_max) - q_up(r_max)                      (lead dsum.py definition)
        D_ax_res17  = F(-pi/2) - F(pi/2) + 4 n int_0^inf w_e/(b_o^2 - w_e^2) dr,  n = m2 = 2l - m1, w_e = (B_+ - B_-)/2, b_o = (B_+ + B_-)/2,
                      inner tail C e^t fitted, outer tail 4 n e_p R^(p-1)/(l^2 (1-p)) with e_p from the datum's y-even part (referee result 17 formula).
    drift_up/down = max - min of q over lr in [-6, 9.5]: the axis-law constancy check (lead: 1e-3 on good states; 0.5-0.8 when the
    upper axis is unresolved, notes 04:28Z item 3).  Quote D_ax only when both drifts are small.
"""
import math
import numpy as np
import torch
from pfwd import fd_dlr


def core_term(S, rho):
    r0 = float(S.r[0])
    row = rho[0] / r0 ** 2
    return r0 / math.pi * float((row * torch.sin(3 * S.th)).sum()) * S.dth


def _cum_trapz(y, x):
    return np.concatenate([[0.0], np.cumsum(0.5 * (y[1:] + y[:-1]) * np.diff(x))])


def _inner_tail(integrand_lr, lr, width=2.0, skip=0.2):
    """integrand (per unit lr) ~ C e^lr near r = 0; returns C e^{lr_min} = int_{-inf}^{lr_min}."""
    msk = (lr >= lr[0] + skip) & (lr <= lr[0] + skip + width)
    if msk.sum() < 3:
        return 0.0, 0.0
    C = float(np.mean(integrand_lr[msk] * np.exp(-lr[msk])))
    return C * math.exp(lr[0]), C


def e_p_formula(S, A, p):
    """referee result 17: e_p = -((p+1)/sin(pi p/2)) int_0^{pi/2} A_e(th) cos((p+2) th) dth, A_e the y-even part of the datum (grid trapezoid)."""
    th = S.th.cpu().numpy(); An = A.cpu().numpy() if torch.is_tensor(A) else np.asarray(A)
    Nth = len(th)
    Ae = 0.5 * (An + np.roll(An[::-1], 1))                 # A(-th) on the uniform grid: index -j mod Nth
    q = Nth // 4
    thq = th[:q + 1]; f = Ae[:q + 1] * np.cos((p + 2) * thq)
    I = float(np.trapezoid(f, thq))
    return -((p + 1) / math.sin(math.pi * p / 2)) * I


def axis_D(S, g, Wr, p, m1, A=None, Wt=None, hmode='sp', qj=2.0):
    """qj != 2 (problem P_q, notes of the lead analyst 09:59Z): h_q = rho(th_j +- dth) / (r sin dth)^q (the |x|^q coefficient on the axis, two-neighbour mean),
    law = int (1 - q m1)/B dr, q_law = log h_q - q log k - law; the paired integral 4 n -> 2 q n; F(-pi/2) - F(pi/2) from log(A / |cos|^q) at the neighbours."""
    assert abs(S.thshift) < 1e-12, 'axis columns need thshift = 0'
    Nth = S.Nth; ju, jd = Nth // 4, 3 * Nth // 4
    l = 1.0 / p; n = 2 * l - m1
    lr = S.lr.cpu().numpy(); r = np.exp(lr)
    gn = g.cpu().numpy()
    kk = np.fft.rfftfreq(Nth, 1.0 / Nth)
    qj = float(qj)
    if abs(qj - 2.0) > 1e-12:
        dth = 2 * np.pi / Nth
        gtt = (np.roll(gn, -1, axis=1) + np.roll(gn, 1, axis=1)) / (2 * math.sin(dth) ** qj) * r[:, None] ** (2 - qj)     # so that r^(p-2) gtt = rho / |x|^q
    elif hmode == 'fd1':
        # local angular second difference over +-1 grid angle (verifier V95: the spectral h suffers Gibbs sign changes on exit-map states)
        dth = 2 * np.pi / Nth
        gtt = (np.roll(gn, -1, axis=1) - 2 * gn + np.roll(gn, 1, axis=1)) / dth ** 2
    else:
        gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(gn, axis=1), Nth, axis=1)
    Wrn = Wr.cpu().numpy()
    dWr_dlr = fd_dlr(Wr, S.d).cpu().numpy()
    # a_dir = d_x V_1 on the axis = (V_r + d_th V_th)/r (notes of the lead analyst 05:21Z: independent of div V = 2l); a_div = 2l - dB/dr assumes div W = 0
    Wt_th = None
    if Wt is not None:
        Wt_th = np.fft.irfft(1j * kk * np.fft.rfft(Wt.cpu().numpy(), axis=1), Nth, axis=1)
    out = {}
    res = {}
    for name, j in (('up', ju), ('down', jd)):
        h = r ** (p - 2) * gtt[:, j]
        B = l * r + Wrn[:, j]                                  # outward speed on the half-axis
        dB = l + dWr_dlr[:, j] / r                             # dB/dr
        a_div = 2 * l - dB
        if Wt_th is not None:
            sgn = 1.0 if name == 'up' else -1.0                # V_r on the lower axis points in -y; both give d_x V_1 = (V_r + d_th V_th)/r
            a_dir = (B + Wt_th[:, j]) / r
            out['a_gap_%s' % name] = float(np.abs(a_dir - a_div)[(lr >= -8) & (lr <= 0)].max())
            a = a_dir
        else:
            a = a_div
        f_lr = (m1 - a) / B * r                                # d log k / d lr
        tail, C = _inner_tail(f_lr, lr)
        logk = tail + _cum_trapz(f_lr, lr)
        law = _cum_trapz((1 - qj * m1) / B * r, lr)
        q = np.log(np.abs(h)) - qj * logk - law
        win = (lr >= -6) & (lr <= 9.5)
        res[name] = dict(h=h, B=B, logk=logk, law=law, q=q, C=C, tail=tail,
                         logF_out=float(np.log(abs(h[-1]) * r[-1] ** (2 - p) / 2)),
                         drift=float(q[win].max() - q[win].min()),
                         q_sel={'%g' % L: round(float(q[int(np.argmin(np.abs(lr - L)))]), 4) for L in (-12, -11, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 9.5)},
                         Bmin=float(B.min()))
    up, dn = res['up'], res['down']
    out['Fp_minus_Fm_ring'] = up['logF_out'] - dn['logF_out']
    if A is not None:
        An = A.cpu().numpy() if torch.is_tensor(A) else np.asarray(A)
        if abs(qj - 2.0) > 1e-12:
            thg = S.th.cpu().numpy(); lA = np.log(np.clip(An, 1e-300, None)) - qj * np.log(np.abs(np.cos(thg)) + 1e-300)
            out['Fp_minus_Fm_datum'] = float(0.5 * (lA[ju - 1] + lA[ju + 1]) - 0.5 * (lA[jd - 1] + lA[jd + 1]))
        else:
            Att = np.fft.irfft(-(kk ** 2) * np.fft.rfft(An), Nth)
            out['Fp_minus_Fm_datum'] = float(np.log(abs(Att[ju]) / 2) - np.log(abs(Att[jd]) / 2))
    out['twoL_k'] = float(qj * (up['logk'][-1] - dn['logk'][-1]))
    out['D_ax_k'] = float(dn['q'][-1] - up['q'][-1])
    out['a_mode'] = 'dir' if Wt_th is not None else 'div'
    out['h_mode'] = hmode; out['qj'] = qj
    out['drift_up'] = up['drift']; out['drift_down'] = dn['drift']
    out['q_up'] = up['q_sel']; out['q_down'] = dn['q_sel']
    out['logk_tail_up'] = up['tail']; out['logk_tail_down'] = dn['tail']; out['C_up'] = up['C']; out['C_down'] = dn['C']
    out['Bmin_up'] = up['Bmin']; out['Bmin_down'] = dn['Bmin']
    # referee result 17 paired integral
    we = 0.5 * (up['B'] - dn['B']); bo = 0.5 * (up['B'] + dn['B'])
    dens = 2 * qj * n * we / (bo ** 2 - we ** 2) * r           # per unit lr (4 n at q = 2)
    tail_in, Cw = _inner_tail(dens, lr)
    grid = float(np.trapezoid(dens, lr))
    ep_meas = float(we[-1] / r[-1] ** p)
    ep = e_p_formula(S, A if A is not None else g[-1], p)
    R = r[-1]
    tail_out = 2 * qj * n * ep * R ** (p - 1) / (l ** 2 * (1 - p))
    out['twoL_res17_grid'] = grid; out['twoL_res17_tail_in'] = tail_in; out['twoL_res17_tail_out'] = tail_out
    out['twoL_res17'] = grid + tail_in + tail_out
    out['e_p_formula'] = ep; out['e_p_measured'] = ep_meas
    Fdiff = out.get('Fp_minus_Fm_datum', out['Fp_minus_Fm_ring'])
    out['D_ax_res17'] = -Fdiff + out['twoL_res17']
    sh = lambda lo, hi: float(np.trapezoid(dens[(lr >= lo) & (lr < hi)], lr[(lr >= lo) & (lr < hi)]))
    out['share_lt_m4'] = sh(-99, -4); out['share_m4_2'] = sh(-4, 2); out['share_gt_2'] = sh(2, 99)
    out['we_over_r_m6'] = float(we[np.argmin(np.abs(lr + 6))] / math.exp(-6))
    return out


def deep_trace_stats(FP, Wr, Wt, A_fine, m1, e1=(1.0, 0.0), lr0=None, picks=(89, 269), bulk_cos=0.3):
    """Tracer statistics with a deep inner stop (V59).  Returns centred log Gt picks, D_samp, bulk std, and the tracer stop used."""
    old = FP.lr0
    if lr0 is not None:
        FP.lr0 = lr0
    T, u0, w0, th0, it = FP.trace(Wr, Wt, e1)
    FP.lr0 = old
    lg = (torch.log(torch.clamp(A_fine, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T).cpu().numpy()
    thA = np.degrees(FP.thA.cpu().numpy()); nA = len(thA)
    w = np.abs(np.cos(np.radians(thA))) > 0.05
    lg = lg - lg[w].mean()
    at = lambda deg: float(lg[int(round(deg / 360 * nA)) % nA])
    out = dict(D_samp=at(picks[1]) - at(picks[0]), up=at(picks[0]), low=at(picks[1]),
               bulk_std=float(lg[np.abs(np.cos(np.radians(thA))) > bulk_cos].std()),
               range_005=float(lg[w].max() - lg[w].min()), lr0=float(lr0 if lr0 is not None else old), steps=it)
    for d in (85, 87, 88, 89, 265, 268, 269, 270, 271):
        out['lg%d' % d] = round(at(d), 4)
    return out, lg
