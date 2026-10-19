"""Verifier's measurement of the SPEC D14 centre relations on a field export (verifier). Only the sampled rho is read.
With a = 1 + delta x^2 + gamma y^2 + O(r^4) and psi = c xy + alpha x y^3 + beta x^3 y + O(r^6) (code/taylor5_ver.py):
alpha + beta = -1/3, E = beta - 2 A delta, D2 = (4A + 2) gamma - 5 alpha must vanish.
delta, gamma from the odd sine modes of rho at small r:
  f_1 = a0 r^3/4 + (delta + gamma) r^5/8 + ...,  f_3 = a0 r^3/4 + (3 delta + gamma) r^5/16 + ...,
  f_5 = (delta - gamma) r^5/16 + ...  (cos^4 t sin t = sin t/8 + 3 sin 3t/16 + sin 5t/16, cos^2 t sin^3 t = sin t/8 +
  sin 3t/16 - sin 5t/16); least squares in r^2 of f_m/r^3 on [r_lo, r_hi] (polynomial degree K);
alpha, beta from the verifier's inverse (vpolar.psi_modes on modes m <= 9, exact for p_2, p_4 since d_x couples m to m +- 1):
  p_4/r^4 -> (beta - alpha)/8, (p_2 - c r^2/2)/r^4 -> (alpha + beta)/4 = -1/12 (checked); c by vpolar.center_c, c_l = (1 + c)/3.
Usage: python3 vd14.py field.npz
"""
import sys, json
import numpy as np
from vcand import load_modes
from vpolar import psi_modes, center_c
from vresid import fit_power_tail


def jets(r, F, ms, r_lo, r_hi, K):
    sel = (r >= r_lo) & (r <= r_hi)
    s = r[sel] ** 2
    V = np.vander(s, K + 1, increasing=True)
    out = {}
    for m in (1, 3, 5):
        q = F[sel, list(ms).index(m)] / r[sel] ** 3
        co, *_ = np.linalg.lstsq(V, q, rcond=None)
        out[m] = (float(co[0]), float(co[1]), float(np.abs(V @ co - q).max() / np.abs(q).max()))
    c1, c3, c5 = out[1][1], out[3][1], out[5][1]
    de, ga = 4 * (c3 + c5), 4 * c3 - 12 * c5
    return dict(r_lo=r_lo, r_hi=r_hi, K=K, a0_from_f1=4 * out[1][0], a0_from_f3=4 * out[3][0], f5_r3=out[5][0],
                delta=de, gamma=ga, f1_check=(de + ga) / 8 - c1, fit=max(v[2] for v in out.values()))


def main(path):
    d, g, ms, F = load_modes(path, 9)
    r = g.r
    fm = {int(m): F[:, i] for i, m in enumerate(ms)}
    c0 = float(d['c_l']) if 'c_l' in d else 5.5763
    k = 1 / c0
    for _ in range(3):
        th_hi = {m: fit_power_tail(r, f, k=k) for m, f in fm.items()}
        th_lo = {m: (f[0] / r[0] ** max(m, 3), max(m, 3)) for m, f in fm.items()}
        c = center_c(g, fm[3], th_hi[3], th_lo[3])
        cl = (1 + c) / 3
        k = 1 / cl
    A = 2 * cl - 1
    pm = psi_modes(g, fm, 8, th_hi, th_lo)
    p2, p4 = pm[2][0], pm[4][0]
    res = dict(file=path, c=c, c_l=cl, A=A, rows=[])
    ab = []
    for rr in (2e-3, 5e-3, 1e-2, 2e-2):
        j = int(np.argmin(np.abs(r - rr)))
        ab.append(dict(r=float(r[j]), bma=float(8 * p4[j] / r[j] ** 4), sum_check=float(4 * (p2[j] - c * r[j] ** 2 / 2) / r[j] ** 4)))
    res['psi_jet'] = ab
    # beta - alpha: Richardson in r^2 between the two smallest radii (next term O(r^2))
    r1, r2 = ab[0]['r'], ab[1]['r']
    bma = (ab[0]['bma'] * r2 ** 2 - ab[1]['bma'] * r1 ** 2) / (r2 ** 2 - r1 ** 2)
    al, be = (-1 / 3 - bma) / 2, (-1 / 3 + bma) / 2
    res.update(beta_minus_alpha=bma, alpha=al, beta=be)
    for (lo, hi, K) in ((1e-3, 0.02, 3), (1e-3, 0.05, 4), (2e-3, 0.05, 3), (1e-3, 0.1, 5), (5e-3, 0.1, 4)):
        jt = jets(r, F, ms, lo, hi, K)
        jt['E'] = be - 2 * A * jt['delta']
        jt['D2'] = (4 * A + 2) * jt['gamma'] - 5 * al
        jt['E_rel'] = jt['E'] / abs(be)
        jt['D2_rel'] = jt['D2'] / abs(5 * al)
        res['rows'].append(jt)
    return res


if __name__ == '__main__':
    o = main(sys.argv[1])
    print('c %.10f c_l %.10f A %.9f  beta-alpha %.10f alpha %.10f beta %.10f' % (o['c'], o['c_l'], o['A'],
          o['beta_minus_alpha'], o['alpha'], o['beta']))
    for a in o['psi_jet']:
        print('  r %.3e  8 p4/r^4 %.10f  4(p2 - c r^2/2)/r^4 %.10f (-1/3)' % (a['r'], a['bma'], a['sum_check']))
    for rw in o['rows']:
        print('  [%.0e, %.2g] K%d a0 %.10f %.10f f5/r^3 %.1e delta %.10f gamma %.10f f1chk %.1e fit %.1e  E %+.3e D2 %+.3e'
              ' (rel %+.2e %+.2e)' % (rw['r_lo'], rw['r_hi'], rw['K'], rw['a0_from_f1'], rw['a0_from_f3'], rw['f5_r3'],
                                     rw['delta'], rw['gamma'], rw['f1_check'], rw['fit'], rw['E'], rw['D2'], rw['E_rel'],
                                     rw['D2_rel']))
    if len(sys.argv) > 2:
        json.dump(o, open(sys.argv[2], 'w'), indent=1, default=float)
