"""Frequency split of the axis quantity q0 (VERIFY_REPORT G70 (b)), verifier.
On the axis q0(x) = lim_{y -> 0} R/rho = d_theta R(r, 0) / d_theta rho(r, 0). With the sine series R = sum_k R_k sin k theta
(R_k from the FFT of R on the evaluation circle) and rho = sum_k rho_k sin k theta (the modes of the field file),
d_theta R(r, 0) = sum_k k R_k; the sum over a band of k gives the part of q0 carried by that band.
Bands relative to Ktop = twice the largest angular index of the shape basis (cos 2m theta, m <= Ktop/2):
  low [1, Ktop/2), mid [Ktop/2, Ktop - 40), top [Ktop - 40, Ktop + 40), high [Ktop + 40, Nt/2].
Checks the spectral q0 against the Richardson value of vaxis.py, then reports q0 by band at a few x and the axis integral
I(0.01, x* - eps) = int q0 / |W_1| dx of each band part (eps 0.03, 0.01) and of the low-pass part (low + mid).
Evaluation as in vchar.py (vcand.main on the sampled rho only).
Usage: python3 vq0band.py field.npz Mmax Ktop out.json
"""
import sys, os, json
import numpy as np
from scipy.interpolate import CubicSpline
from vcand import main as vcand_main, load_modes
from vb3 import find_xstar
from vchar import half_shift


def main(path, Mmax, Ktop, outp):
    out, ev, ax = vcand_main(path, dict({'Mmax': Mmax, 'b3': False}, **json.loads(os.environ.get('VCHAR_CFG', '{}'))))
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r; Nt = out['Nt']; th = 2 * np.pi * np.arange(Nt) / Nt; cl = ev.c_l
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    q0 = (9 * q[:, 0] - q[:, 1]) / 8
    rho_t = F @ ms                                       # d_theta rho at theta = 0
    Rs = -2 * np.fft.rfft(ev.R, axis=1).imag / Nt        # sine coefficients of R, k = 0 .. Nt/2
    kk = np.arange(Rs.shape[1])
    bands = dict(low=(1, Ktop // 2), mid=(Ktop // 2, Ktop - 40), top=(Ktop - 40, Ktop + 40), high=(Ktop + 40, Nt // 2 + 1))
    part = {b: (Rs[:, (kk >= lo) & (kk < hi)] @ kk[(kk >= lo) & (kk < hi)]) / rho_t for b, (lo, hi) in bands.items()}
    qs = sum(part.values())
    part['lowpass'] = part['low'] + part['mid']
    W1 = cl * r + ev.Ur[:, 0]
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))
    sel = (r > 5e-3) & (r < 25)
    lr = np.log(r[sel])

    def I(f, lo, hi):
        return float(CubicSpline(lr, f[sel] / np.abs(W1[sel]) * r[sel]).integrate(np.log(lo), np.log(hi)))

    m = (r > 0.01) & (r < xs - 0.03)
    res = dict(file=path, Mmax=Mmax, Ktop=Ktop, Nt=int(Nt), c_l=cl, x_star=xs, bands={b: list(v) for b, v in bands.items()},
               spec_vs_richardson_max=float(np.max(np.abs(qs - q0)[m])), q0_absmax=float(np.max(np.abs(q0[m]))),
               I={}, absmax={}, q0_at={})
    for b, f in list(part.items()) + [('spectral', qs), ('richardson', q0)]:
        res['I'][b] = {('%g' % e): I(f, 0.01, xs - e) for e in (0.03, 0.01)}
        j = np.argmax(np.abs(f[m])); res['absmax'][b] = [float(f[m][j]), float(r[m][j])]
    for x in (0.5, 1, 2, 3, 4, 5, 6, 7, 8, 8.4):
        i = int(np.argmin(np.abs(r - x)))
        res['q0_at']['%.2f' % r[i]] = dict(richardson=float(q0[i]), spectral=float(qs[i]), **{b: float(f[i]) for b, f in part.items()})
    print(json.dumps(res, indent=1))
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
