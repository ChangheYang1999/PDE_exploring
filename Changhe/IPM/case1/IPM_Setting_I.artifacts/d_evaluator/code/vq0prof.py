"""Node-level profile of the axis quantity q0 = lim_{y -> 0} R/rho near the source point (VERIFY_REPORT G70 (d)), verifier.
q0 at every radial node with lo <= r <= hi, two ways as in code/vq0band.py: Richardson from the two half-shifted angles
next to theta = 0, and spectral, sum_k k R_k / d_theta rho(r, 0). Reports max |q0| over [a, x* - eps] for a = 7.5, 8, 8.4
and eps = 0.1, 0.03, 0.01, 0.003, the node spacing there, and the profile. Evaluation as in vchar.py (vcand.main on the
sampled rho only).
Usage: python3 vq0prof.py field.npz Mmax lo hi out.json
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
    q0 = (9 * q[:, 0] - q[:, 1]) / 8
    Rs = -2 * np.fft.rfft(ev.R, axis=1).imag / Nt
    kk = np.arange(Rs.shape[1])
    qs = (Rs @ kk) / (F @ ms)
    xs = find_xstar(np.asarray(ax['x']), np.asarray(ax['w']))
    sel = (r >= lo) & (r <= hi)
    res = dict(file=path, Mmax=Mmax, Nt=int(Nt), c_l=float(ev.c_l), x_star=xs, max={}, spacing={},
               profile=[[float(a), float(b), float(c)] for a, b, c in zip(r[sel], q0[sel], qs[sel])])
    for a in (7.5, 8.0, 8.4):
        for e in (0.1, 0.03, 0.01, 0.003):
            m = (r >= a) & (r <= xs - e)
            if m.any():
                j = np.argmax(np.abs(q0[m])); js = np.argmax(np.abs(qs[m]))
                res['max']['%g_%g' % (a, e)] = dict(richardson=[float(q0[m][j]), float(r[m][j])],
                                                    spectral=[float(qs[m][js]), float(r[m][js])], n=int(m.sum()))
        m = (r >= a) & (r <= xs)
        res['spacing']['%g' % a] = float(np.max(np.diff(r[m]))) if m.sum() > 1 else float('nan')
    print(json.dumps({k: v for k, v in res.items() if k != 'profile'}, indent=1))
    for a, b, c in res['profile'][::4]:
        print('r %.4f q0 %+.3e spectral %+.3e' % (a, b, c))
    json.dump(res, open(outp, 'w'), indent=1)


if __name__ == '__main__':
    a = sys.argv
    main(a[1], int(a[2]), float(a[3]), float(a[4]), a[5])
