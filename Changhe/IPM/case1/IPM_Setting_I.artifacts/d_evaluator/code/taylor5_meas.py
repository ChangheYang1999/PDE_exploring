"""Verifier's measurement of the center coefficients alpha, beta (psi) and delta, gamma (a) of the construct1 global
trial formula (SPEC D14), verifier. delta, gamma: from H on rays at small r (gen_shape.shape_rho, own evaluation);
alpha, beta: from the verifier's own canonical inverse (vpolar.psi_modes, own tails): p_4/r^4 -> (beta - alpha)/8,
(p_2 - c r^2/2)/r^4 -> (alpha + beta)/4 = -1/12.
Usage: python3 taylor5_meas.py shape.npz N"""
import sys
import numpy as np
from gen_shape import shape_rho
from vpolar import LogGrid, modes_from_samples, psi_modes, center_c
from vresid import fit_power_tail

d = np.load(sys.argv[1], allow_pickle=True)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 3520
L = float(d['L'])
r0, R = 1e-4 * L, 1e7 * L
g = LogGrid(N, r0, R)
r = g.r
Nt = 2560
th = 2 * np.pi * np.arange(Nt) / Nt
rho, H, info = shape_rho(d, r, th)
cl_nom = info['c_l']
A = 2 * cl_nom - 1
# delta, gamma from H(r, 0) and H(r, pi/2) at small r: H = delta x^2 + gamma y^2 + O(r^4)
for rr in (1e-3, 2e-3, 4e-3):
    hh, HH, _ = shape_rho(d, np.array([rr]), np.array([0.0, np.pi / 2]))
    print('r=%.0e  H(r,0)/r^2 = %.9f   H(r,pi/2)/r^2 = %.9f' % (rr, HH[0, 0] / rr ** 2, HH[0, 1] / rr ** 2))
rs = np.array([1e-3, 2e-3])
_, HH, _ = shape_rho(d, rs, np.array([0.0, np.pi / 2]))
# Richardson in r^2 (next term r^4)
de = (4 * HH[0, 0] / rs[0] ** 2 - HH[1, 0] / rs[1] ** 2) / 3
ga = (4 * HH[0, 1] / rs[0] ** 2 - HH[1, 1] / rs[1] ** 2) / 3
fm, bad, _ = modes_from_samples(rho, 9)
fm = {m: fm[m] for m in (1, 3, 5, 7, 9)}
th_hi = {m: fit_power_tail(r, f, k=info['k']) for m, f in fm.items()}
th_lo = {m: (f[0] / r[0] ** max(m, 3), max(m, 3)) for m, f in fm.items()}
c = center_c(g, fm[3], th_hi[3], th_lo[3])
pm = psi_modes(g, fm, 8, th_hi, th_lo)
p2, p4 = pm[2][0], pm[4][0]
print('own c = %.10f  nominal 3c_l-1 = %.10f  rel %.2e   parity_bad %.1e' % (c, 3 * cl_nom - 1, c / (3 * cl_nom - 1) - 1, bad))
for j in (40, 80, 120, 160, 200):
    print('r=%.3e  p4/r^4 = %.9f   (p2 - c r^2/2)/r^4 = %.9f' % (r[j], p4[j] / r[j] ** 4, (p2[j] - c * r[j] ** 2 / 2) / r[j] ** 4))
j = 80
bma = 8 * p4[j] / r[j] ** 4
al, be = (-1 / 3 - bma) / 2, (-1 / 3 + bma) / 2
print('beta - alpha = %.10f  alpha = %.10f  beta = %.10f   delta = %.8f  gamma = %.8f' % (bma, al, be, de, ga))
E = be - 2 * A * de
D2 = (4 * A + 2) * ga - 5 * al
print('E = beta - 2 A delta = %.5f (terms %.4f, %.4f)   D2 = (4A+2) gamma - 5 alpha = %.5f (terms %.4f, %.4f)'
      % (E, be, 2 * A * de, D2, (4 * A + 2) * ga, 5 * al))
print('required delta = %.6f  gamma = %.6f' % (be / (2 * A), 5 * al / (4 * A + 2)))
