"""Vertical-axis far coefficient of a stored generating-function state (float64 implementation of the verifier's
closed formula, result 69): from P and its t, w derivatives at (t, w) = (0, 1) compute Q1..Q4, the desingularized vertical
grouped limit |Q1+Q2+Q3+Q4|/(|Q1|+|Q2|+|Q3|+|Q4|) and the unique amplitude a_vertical = -(Q1+Q2+Q3)/(2 j h).
Also the horizontal-axis amplitude a_horizontal from F_axis = 0 (formula (H) of the verifier's far compatibility proof, P at
(0, 0)) and the centre amplitude a_center = 70 h_c + 14 q_c/(h_c p_c) (outer P only; not valid for states with core patches).
Core patches do not enter the two far amplitudes. Diagnostic only (binary64, not an enclosure).
Usage: python3 vamp.py state.npz [state2.npz ...]"""
import sys, math, numpy as np
for f in sys.argv[1:]:
    d = np.load(f); J, K = int(d['J']), int(d['Kw']); c = d['c'].reshape(J + 1, K + 1); a = float(d['a0'])
    al = float(d['alpha']); s = float(d['se']) if 'se' in d.files else 1.0
    if 'gam' in d.files and float(d['gam']) != 0: print(f, 'gam != 0: not covered'); continue
    n = np.arange(J + 1.0); k = np.arange(K + 1.0)
    Tn = (-1.0) ** n; dTn = 2 * (-1.0) ** (n + 1) * n ** 2; ddTn = 4 * (-1.0) ** n * n ** 2 * (n ** 2 - 1) / 3   # d/dt of T_n(2t-1) at t = 0
    Tk = np.ones(K + 1); dTk = 2 * k ** 2                                                                       # d/dw of T_k(2w-1) at w = 1
    p0, p0w = Tn @ c @ Tk, Tn @ c @ dTk
    p1, p1w = dTn @ c @ Tk, dTn @ c @ dTk
    p2, p2w = ddTn @ c @ Tk, ddTn @ c @ dTk
    c1 = (1 - math.exp(-al)) / al; c2 = (al / 2) * c1 ** 2
    h = p0 / s ** 2; j = (s ** 4 / 3) * (p0 - p0w)
    b = c1 * p1 / s; cc = (c1 * s ** 5 / 6) * (p1 - 2 * p1w)
    k0 = c2 * p1 + (c1 ** 2 / 2) * p2; k1 = c2 * p1w + (c1 ** 2 / 2) * p2w
    L = -2 * k0 + 2 * b ** 2 / (3 * h); M = (2 * s ** 6 / 3) * k1 + 2 * b * cc / (3 * h) + 2 * b ** 2 * j / h ** 2
    d0 = 2 * b * j / h - cc
    Q1 = -2 * L / 9 + 6 * h ** 2 * M - 6 * h * L * j; Q2 = -4 * b ** 2 / (27 * h) - 4 * b * d0 * h; Q3 = 2 * Q2; Q4 = 2 * a * j * h
    Q = np.array([Q1, Q2, Q3, Q4])
    Tk0 = (-1.0) ** k; dTk0 = 2 * (-1.0) ** (k + 1) * k ** 2                                                  # T_k(2w-1) and d/dw at w = 0
    q00, q01, q10, q11, q20, q21 = Tn @ c @ Tk0, Tn @ c @ dTk0, dTn @ c @ Tk0, dTn @ c @ dTk0, ddTn @ c @ Tk0, ddTn @ c @ dTk0
    hh = (5 / 3) * q00; A_ = -c1 * q10 / hh; B_ = (c1 / s ** 2) * (q10 * q01 / hh ** 4 - q11 / hh ** 3); g_ = (2 / 9) * A_ - 6 * B_
    kh0 = c2 * q10 + (c1 ** 2 / 2) * q20; kh1 = c2 * q11 + (c1 ** 2 / 2) * q21
    Lh = -2 * kh0 + (4 / 3) * c1 ** 2 * q10 ** 2 / hh
    Mh = s ** -2 * (-2 * kh1 + c1 ** 2 * ((14 / 3) * q10 * q11 / hh - 4 * q10 ** 2 * q01 / hh ** 2))
    C1h = Lh / hh; D1h = -Lh * q01 / (s ** 2 * hh ** 4) + Mh / hh ** 3
    Fk = -(2 / 9) * C1h + 6 * D1h + 2 * A_ * g_; a_h = -(3 * hh / 2) * Fk
    hc = Tk0 @ c.T @ np.ones(J + 1); Pt1 = (2 * n ** 2) @ c @ Tk0; Pw1 = np.ones(J + 1) @ c @ dTk0
    ell = -(math.exp(al) - 1) / (6 * al); pc = hc / 3 + ell * Pt1; qc = Pw1 / s ** 2; a_c = 70 * hc + 14 * qc / (hc * pc)
    print('   a_center %s  a_horizontal %.6f  a_vertical %.6f  (stored a0 %.6f)' % ('%.6f' % a_c if 'core' not in d.files else 'n/a(core)', a_h, -(Q1 + Q2 + Q3) / (2 * j * h), a))
    print('%s  a0 %.6f  p0 %.6e  j %.4e  C_div %+.6e  vertical grouped limit %.6e  a_vertical %.6f  terms %s' % (
        f, a, p0, j, Q.sum() / (s ** 2 * p0 ** 3), abs(Q.sum()) / np.abs(Q).sum(), -(Q1 + Q2 + Q3) / (2 * j * h), ' '.join('%+.3e' % v for v in Q)))
