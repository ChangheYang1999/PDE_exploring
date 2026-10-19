"""Angular structure of q = R/rho next to the x-axis (VERIFY_REPORT G70), verifier.
At fixed r the half-shifted samples q(r, theta_j), theta_j < 0.12, are fitted by an even polynomial in theta (degree 6 in
theta, i.e. 4 terms in theta^2); the remainder is the ripple that labels joining the axis at different heights sample.
Reports for each r: q on the axis (Richardson, as vaxis.py), the fitted smooth part at theta 0.02 and 0.1, the ripple
amplitude max |q - fit|, the mean spacing of its sign changes (half period in theta) and the equivalent angular frequency
pi / spacing; and the sine spectrum of R(r, .) over the whole circle in bands of the frequency k (R = sum_k R_k sin k theta).
Evaluation as in vchar.py (vcand.main on the sampled rho only).
Usage: python3 vstrip.py field.npz Mmax out.json
"""
import sys, json
import numpy as np
from vcand import main as vcand_main, load_modes
from vchar import half_shift


def main(path, Mmax, outp):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    d, g, ms, F = load_modes(path, Mmax)
    r = g.r; Nt = out['Nt']; th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    q = half_shift(ev.R, Nt) / half_shift(rho, Nt)
    thm = th + np.pi / Nt
    res = dict(file=path, Mmax=Mmax, Nt=int(Nt), c_l=float(ev.c_l), rows=[])
    sel = thm < 0.12
    t = thm[sel]
    V = np.vstack([t ** (2 * j) for j in range(4)]).T
    Rhat = np.fft.rfft(ev.R, axis=1)                     # R real; sine coefficients from the imaginary part
    kk = np.arange(Rhat.shape[1])
    bands = ((1, 50), (50, 150), (150, 250), (250, 290), (290, 310), (310, 400), (400, 600), (600, Nt // 2))
    for x in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.6, 8.0, 8.3):
        i = int(np.argmin(np.abs(r - x)))
        qq = q[i, sel]
        c, *_ = np.linalg.lstsq(V, qq, rcond=None)
        rem = qq - V @ c
        sc = np.nonzero(np.diff(np.sign(rem)))[0]
        sp = float(np.mean(np.diff(t[sc]))) if len(sc) > 2 else float('nan')
        q0 = float((9 * q[i, 0] - q[i, 1]) / 8)
        Rs = -2 * Rhat[i].imag / Nt
        spec = {('%d-%d' % b): float(np.sqrt(np.sum(Rs[(kk >= b[0]) & (kk < b[1])] ** 2))) for b in bands}
        row = dict(r=float(r[i]), q0=q0, fit_002=float(np.polyval(c[::-1], 0.02 ** 2)), fit_01=float(np.polyval(c[::-1], 0.1 ** 2)),
                   ripple_max=float(np.max(np.abs(rem))), ripple_at=float(t[np.argmax(np.abs(rem))]),
                   ripple_max_t_lt_005=float(np.max(np.abs(rem[t < 0.05]))), half_period=sp,
                   freq=float(np.pi / sp) if sp == sp else float('nan'), n_sign=int(len(sc)), R_spec=spec,
                   rho_scale=float(np.max(np.abs(rho[i]))),
                   profile=[[float(a), float(b)] for a, b in zip(t[t < 0.08], qq[t < 0.08])])
        res['rows'].append(row)
        print('r %.3f q0 %+.3e fit(.02) %+.3e fit(.1) %+.3e | ripple max %.2e at th %.4f (th<.05: %.2e) half period %.4f (k %.0f, %d sign changes)'
              % (row['r'], q0, row['fit_002'], row['fit_01'], row['ripple_max'], row['ripple_at'], row['ripple_max_t_lt_005'], sp,
                 row['freq'], row['n_sign']))
        print('    q(theta): ' + ' '.join('%.4f:%+.2e' % (a, b) for a, b in row['profile'][::2]))
        print('    |R_k| by band ' + ' '.join('%s %.2e' % (k, v) for k, v in spec.items()))
        sys.stdout.flush()
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
