"""Label-free axis part of the characteristic defect (VERIFY_REPORT G69 (e)), verifier.
On the x-axis rho = 0 and W_2 = 0; R/rho has the even limit q0(x) = lim_{y -> 0} (R/rho)(x, y), obtained from the
half-shifted angles pi/Nt and 3 pi/Nt by Richardson in y^2. Backward characteristics on the separatrix run along the
x-axis from the origin to P with dx/dtau = -W_1(x, 0) > 0, so their J gains I(a, b) = int_a^b q0(x)/|W_1(x, 0)| dx there.
Reports I on (0.01, x* - eps) and on bands, the same with |q0| (abs_left), max |q0| left and right of P, and from the right I on (x* + eps, 20) (labels next to the x-axis, family C).
Evaluation as in vchar.py (vcand.main on the sampled rho only).
Usage: python3 vaxis.py field.npz Mmax out.json
"""
import sys, os, json
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift


def main(path, Mmax, outp):
    out, ev, ax = vcand_main(path, dict({'Mmax': Mmax, 'b3': False}, **json.loads(os.environ.get('VCHAR_CFG', '{}'))))  # VCHAR_CFG: extra vcand cfg
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r; Nt = out['Nt']; th = 2 * np.pi * np.arange(Nt) / Nt; cl = ev.c_l
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    a = np.pi / Nt
    q0 = (9 * q[:, 0] - q[:, 1]) / 8                  # angles a and 3a
    W1 = cl * r + ev.Ur[:, 0]                          # theta = 0: W_1 = c_l x + U_r
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))
    sel = (r > 5e-3) & (r < 25)
    lr = np.log(r[sel]); f = q0[sel] / np.abs(W1[sel]) * r[sel]   # integrand in log r
    S = CubicSpline(lr, f)
    I = lambda lo, hi: float(S.integrate(np.log(lo), np.log(hi)))
    res = dict(file=path, Mmax=Mmax, c_l=cl, x_star=xs, y_first=float(xs * np.sin(a)),
               q0_minus_qa_max=float(np.max(np.abs(q0 - q[:, 0])[sel])),
               W1_sign_change=[float(v) for v in r[sel][np.where(np.diff(np.sign(W1[sel])))[0]]],
               left={}, right={}, bands={})
    for e in (4.0, 2.0, 1.0, 0.5, 0.3, 0.1, 0.03, 0.01):
        res['left']['%g' % e] = I(0.01, xs - e)
        res['right']['%g' % e] = I(xs + e, 20.0)
    Sa = CubicSpline(lr, np.abs(f))
    res['abs_left'] = {('%g' % e): float(Sa.integrate(np.log(0.01), np.log(xs - e))) for e in (0.5, 0.03, 0.01)}
    # partial integrals F(a) = int_a^{x* - 0.03} q0/|W_1| dx (the axis part of labels that join the axis near x = a)
    av = r[(r > 0.01) & (r < xs - 0.5)]
    Fa = np.array([I(a_, xs - 0.03) for a_ in av[::8]])
    res['F_range'] = [float(Fa.min()), float(av[::8][np.argmin(Fa)]), float(Fa.max()), float(av[::8][np.argmax(Fa)])]
    m = (r > 0.01) & (r < xs - 0.03); j = np.argmax(np.abs(q0[m]))
    res['q0_absmax_left'] = [float(q0[m][j]), float(r[m][j])]
    m = (r > xs + 0.03) & (r < 20); j = np.argmax(np.abs(q0[m]))
    res['q0_absmax_right'] = [float(q0[m][j]), float(r[m][j])]
    for lo, hi in ((0.01, 0.5), (0.5, 2), (2, 4), (4, 6), (6, 7.6), (7.6, xs - 0.5), (xs - 0.5, xs - 0.03)):
        res['bands']['%.3g-%.3g' % (lo, hi)] = I(lo, hi)
    # q0 profile on the axis at a few points
    res['q0_at'] = {('%.2f' % x): float(np.interp(np.log(x), np.log(r), q0)) for x in (0.1, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 8.4, 8.8, 10, 15)}
    print(json.dumps(res, indent=1))
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
