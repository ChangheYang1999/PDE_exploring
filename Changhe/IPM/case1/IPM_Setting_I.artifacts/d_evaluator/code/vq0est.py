"""Estimator check for the axis quantity q0 = lim_{y -> 0} R/rho next to P (G74, verifier). On the nodes lo <= r <= hi:
q(theta) = R/rho at the half-shifted angles h/2, 3h/2, 5h/2 (h = 2 pi / Nt, spectral half shift as in vchar.py); the
two-point Richardson of vq0prof.py (eliminates theta^2), the three-point Richardson (eliminates theta^2 and theta^4), and
the spectral value sum_k k R_k / sum_m m F_m with partial sums k <= K. The Richardson values converge to the spectral one
only when k h is small for the modes that carry R near the axis; the partial sums show which k carry the axis value.
Usage: python3 vq0est.py field.npz Mmax lo hi out.json
"""
import sys, os, json
import numpy as np
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift


def main(path, Mmax, lo, hi, outp):
    out, ev, ax = vcand_main(path, dict({'Mmax': Mmax, 'b3': False}, **json.loads(os.environ.get('VCHAR_CFG', '{}'))))
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r; Nt = out['Nt']; th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    r2 = (9 * q[:, 0] - q[:, 1]) / 8
    r3 = (225 / 192) * q[:, 0] - (25 / 128) * q[:, 1] + (9 / 384) * q[:, 2]
    Rs = -2 * np.fft.rfft(ev.R, axis=1).imag / Nt
    kk = np.arange(Rs.shape[1]); den = F @ ms
    Ks = [50, 100, 150, 200, 300, 400, 600, int(kk[-1])]
    part = {K: (Rs[:, :K + 1] @ kk[:K + 1]) / den for K in Ks}
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))
    sel = (r >= lo) & (r <= hi)
    res = dict(file=path, Mmax=Mmax, Nt=int(Nt), c_l=float(ev.c_l), x_star=xs, h=float(2 * np.pi / Nt), max={},
               cols=['r', 'q(h/2)', 'rich2', 'rich3'] + ['spec_K%d' % K for K in Ks],
               profile=[[float(v) for v in row] for row in
                        np.column_stack([r, q[:, 0], r2, r3] + [part[K] for K in Ks])[sel]])
    for a in (7.5, 8.0, 8.4):
        m = (r >= a) & (r <= xs - 0.003)
        if not m.any(): continue
        e = {}
        for name, v in [('q(h/2)', q[:, 0]), ('rich2', r2), ('rich3', r3)] + [('spec_K%d' % K, part[K]) for K in Ks]:
            j = np.argmax(np.abs(v[m])); e[name] = [float(v[m][j]), float(r[m][j])]
        res['max']['%g' % a] = e
    print(json.dumps({k: v for k, v in res.items() if k != 'profile'}, indent=1))
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    a = sys.argv
    main(a[1], int(a[2]), float(a[3]), float(a[4]), a[5])
