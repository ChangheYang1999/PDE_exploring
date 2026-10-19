"""Local tail slope of the D10 (cubic moment) integrand on decades of r, against 2k - 2 with k = 1/c_l (verifier,
lead NOTES 16:52:51Z item 2 (e)). prof(r) = int_theta 3 rho (-U_r sin 3t + U_t cos 3t) / r^2 dt is the integrand per d log r
(vcand.d10). If rho ~ r^k A(t) (1 + B(t) r^(k-1) + ...), the local slope is 2k - 2 + O(r^(k-1)).
Usage: python3 d10tail.py field.npz Mmax out.json"""
import sys, json, warnings
warnings.simplefilter("ignore")
import numpy as np
from vcand import main as vcand_main, load_modes


def main(path, Mmax, outp):
    out, ev, ax = vcand_main(path, {'Mmax': Mmax, 'b3': False})
    d, g, ms, F = load_modes(path, Mmax)
    Nt = out['Nt']
    th = 2 * np.pi * np.arange(Nt) / Nt
    rho = F @ np.sin(np.outer(ms, th))
    r = g.r
    integ = 3 * rho * (-ev.Ur * np.sin(3 * th)[None, :] + ev.Ut * np.cos(3 * th)[None, :]) / r[:, None] ** 2
    prof = integ.sum(1) * (2 * np.pi / Nt)
    k = 1 / ev.c_l
    rows = []
    wins = [(1e1, 1e2), (1e2, 1e3), (1e3, 1e4), (1e4, 1e5), (1e5, 1e6), (1e6, r[-1]), (r[-1] / 10, r[-1])]
    for a, b in wins:
        sel = (r >= a) & (r <= b)
        s = np.polyfit(np.log(r[sel]), np.log(np.abs(prof[sel]) + 1e-300), 1)[0]
        rm = np.sqrt(a * b)
        rows.append(dict(r_lo=float(a), r_hi=float(b), slope=float(s), dev=float(s - (2 * k - 2)), r_mid_pow=float(rm ** (k - 1)),
                         sign_changes=int(np.sum(np.diff(np.sign(prof[sel])) != 0))))
        print('  r %.3g-%.3g slope %.7f  dev %+.3e  r_mid^(k-1) %.2e' % (a, b, s, s - (2 * k - 2), rm ** (k - 1)), flush=True)
    res = dict(file=path, c_l=float(ev.c_l), k=float(k), two_k_minus_2=float(2 * k - 2), D10=out.get('D10'), rows=rows)
    json.dump(res, open(outp, 'w'), indent=1)
    print(json.dumps(dict(c_l=ev.c_l, two_k_minus_2=2 * k - 2, D10=out.get('D10'))), flush=True)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), sys.argv[3])
