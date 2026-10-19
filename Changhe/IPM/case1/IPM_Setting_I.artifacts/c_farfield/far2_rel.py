"""Relative inconsistency of the trial's far field at orders 1, 2, 3 next to the y-axis (lead): |R_j| / max(|pure_j|, |vel_j|),
pure_j = j (1 - c_l) a_j (the pure-power part of R_j / Theta_0), vel_j = U.grad rho part T_j / Theta_0, and the series terms at
4858 L. usage: python3 far2_rel.py <shape.npz> [<shape.npz> ...]"""
import sys
import numpy as np
import far2
for path in sys.argv[1:]:
    o = far2.coefficients(path, 1 << 15)
    th, k, L, cl = o['th'], o['k'], o['L'], o['cl']
    i = int(np.argmin(np.abs(th - 1.56811)))
    rel = []
    for j in (1, 2, 3):
        pure = j*(1-cl)*o['a'][j][i]; vel = o['Tn'][j][i]
        rel.append(abs(o['R'][j][i])/max(abs(pure), abs(vel)))
    r = 4858*L; d = r**(k-1)
    q = [o[n][i] for n in ('q1', 'q2', 'qh', 'q3')]
    terms = [q[0]*d, q[1]*d*d, q[2]/r**2, q[3]*d**3]
    print('%s theta %.5f  rel %.4e %.4e %.4e  q %s  terms4858 %s sum %.4e'
          % (path, th[i], *rel, ' '.join('%+.4e' % x for x in q), ' '.join('%+.3e' % x for x in terms), sum(terms)))
