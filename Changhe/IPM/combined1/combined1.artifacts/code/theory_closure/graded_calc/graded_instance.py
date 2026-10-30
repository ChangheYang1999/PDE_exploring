"""Fixed-parameter instance of FW-T-TB-graded-v1 (theory_v01, c1-t1). CONDITIONAL model.

s = 5*2^-18 fixed. For the forcing direction proportional to the FW-A2-Db component
bounds, find a box r by Nelder-Mead, round it to 4 significant digits, choose a rounded
scale lambda, and verify the closure Gamma(r, phi) <= r in interval arithmetic (mpmath iv,
40 digits). Also reports d = c_s n_g(r) and the low contraction ratio d/(19/5 - d).

Usage: python3 -B graded_instance.py > graded_instance.out
"""
import math
from fractions import Fraction as Fr
from scipy.optimize import minimize
import mpmath as mp
from graded_calc import gamma_map, closes, verify_iv

S = 5 / 2**18
Db = [6.358653e-7, 4.967698e-9, 1.241925e-9, 1.272594e-9]


def lam_for(r):
    if not closes(S, r, [0, 0, 0, 0]):
        return 0.0
    lo, hi = 0.0, 1.0
    while closes(S, r, [hi * d for d in Db]):
        hi *= 2
    for _ in range(60):
        mid = (lo + hi) / 2
        if closes(S, r, [mid * d for d in Db]):
            lo = mid
        else:
            hi = mid
    return lo


best = (0, None)
for x0 in ([-8.5, -15, -17.8, -17.3], [-8.3, -14.9, -17.7, -17.2], [-9, -15.5, -18, -17.5]):
    res = minimize(lambda x: -lam_for([math.exp(t) for t in x]), x0, method='Nelder-Mead',
                   options=dict(maxiter=6000, xatol=1e-7, fatol=1e-12))
    if -res.fun > best[0]:
        best = (-res.fun, res.x)
lam_opt, x = best
r = [float(f"{math.exp(t):.4g}") for t in x]
lam_r = lam_for(r)
lam_cert = math.floor(lam_r * 0.995 * 10) / 10
phi = [lam_cert * d for d in Db]
ok, info = verify_iv(S, r, phi)
G, mg = info
print("FW-T-TB-graded-v1 instance (CONDITIONAL on FW-T-TB-graded-v1:H1-H4)")
print(f"s = 5*2^-18 = {S:.6e}")
print(f"optimal lambda (float) = {lam_opt:.4f}; with rounded box lambda = {lam_r:.4f}; certified lambda = {lam_cert}")
print("box r = (r2, r1, r0, rH) =", r)
print("forcing bounds phi = lambda * D(b) component bounds =", [f"{t:.4e}" for t in phi])
print("interval check Gamma(r, phi) <= r:", "PASS" if ok else "FAIL")
print("Gamma upper ends:", [mp.nstr(g.b, 8) for g in G])
print("margins (lower ends): m2 = %s, m1 = %s, m0 = %s, mH = %s" % tuple(mp.nstr(mg[k].a, 6) for k in ('m2', 'm1', 'm0', 'mH')))
ng = math.sqrt(r[0]**2 + 2 * r[1]**2 + r[2]**2)
cs = 1 / (2 * math.sqrt(math.pi * S * (1 + S)))
d = cs * ng
print(f"n_g(r) = {ng:.6e}; d = c_s n_g = {d:.6e}; low contraction d/(19/5-d) = {d/(3.8-d):.3e}")
# necessary pointwise radius comparison (T4-007 / NORM-T-PTNEC-v1) with the d2 point (0,1)
F, Vn, gn = 0.0117458591346551, 1.13414558978361, 8.39318259059732
C0 = 1 / (2 * math.sqrt(math.pi * (1 + S))); C1 = 1 / math.sqrt(8 * math.pi * S * (1 + S))
A = C1 * Vn + C0 * (1 + gn); B = C0 * C1
print(f"d2 point (0,1) necessary H^(2+s) radius at this s: {2*F/(A+math.sqrt(A*A+4*B*F)):.4e} vs n_g(r) = {ng:.4e}")
