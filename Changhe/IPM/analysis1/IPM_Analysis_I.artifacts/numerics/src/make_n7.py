"""N7 (centre-regular trial, lead 21:17Z / 22:03Z / 22:30Z): remove the non-polynomial inner terms r^{2j} cos(2m theta) with m > j, j <= JMAX
(set D[m, j-1] = 0 for 1 <= j <= min(m-1, JMAX)), then re-solve the 7 inner correction coefficients Ei[m] of every affected mode from the
C^6 join conditions at tmin (the spline and the remaining inner powers are unchanged). The inner density is then a polynomial in (x, y)
through degree 3 + 2 JMAX = 11 plus the j >= JMAX+1 powers (degree >= 13) and the corrections e^{bi tau'} tau'^i = O((r/rmin)^{bi} log^i)
(bi = 50). X3's own modes vanish like r^{2m} (factor chi^{m-1} b_m(q)), so the removed coefficients are fit noise (|D_mj| ~ 1e-9).
Usage: python3 make_n7.py trial.npz out.npz [JMAX=4]
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial, NIN, NCOR

path, out = sys.argv[1], sys.argv[2]; JMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 4
d = dict(np.load(path)); T = Trial(d); M = T.M; bi = T.bi; tmin = T.tmin
D = d["D"].copy(); Ei = d["Ei"].copy()
removed = []
for m in range(2, M):
    for j in range(1, min(m - 1, JMAX) + 1):
        if D[m, j - 1] != 0.0: removed.append((m, j, D[m, j - 1])); D[m, j - 1] = 0.0
print("removed %d coefficients (m > j, j <= %d); largest |D_mj| removed: %.3e; degree-5 resonance h7 = (D[2,0]+D[3,0]-D[4,0]-D[5,0])/8 before: %.3e, after: %.3e" % (
    len(removed), JMAX, max(abs(x[2]) for x in removed), (d["D"][2, 0] + d["D"][3, 0] - d["D"][4, 0] - d["D"][5, 0]) / 8, (D[2, 0] + D[3, 0] - D[4, 0] - D[5, 0]) / 8))
# re-solve Ei for every mode m >= 2: join conditions  spline^{(i)}(tmin) = inner^{(i)}(tmin), i = 0..6, where inner = delta_{m0} + sum_j D e^{2j tau'} + e^{bi tau'} sum_i Ei tau'^i
# derivative of order nu at tau' = 0 of e^{bi tau'} tau'^i: sum over l: C(nu, l) bi^{nu-l} * (i! if l == i else 0)  -> nu!/(nu-i)! bi^{nu-i} for i <= nu
from math import factorial, comb
Mat = np.zeros((NCOR, NCOR))
for nu in range(NCOR):
    for i in range(NCOR):
        if i <= nu: Mat[nu, i] = factorial(nu) / factorial(nu - i) * bi ** (nu - i)
spl_jet = np.stack([T.spl(np.array([tmin]), nu=nu)[0] for nu in range(NCOR)])     # (7, M): spline jet at tmin (extrapolate=False: tmin is the first knot -> fine)
jj = np.arange(1, NIN + 1)
for m in range(M):                                                                 # all modes (the stored float Ei of modes 0, 1 miss the joins at orders >= 4)
    pow_jet = np.array([np.sum(D[m] * (2.0 * jj) ** nu) for nu in range(NCOR)])    # jet of sum_j D e^{2j tau'}
    if m == 0: pow_jet[0] += 1.0                                                   # the constant a_0 = 1 on the inner region
    rhs = spl_jet[:, m] - pow_jet
    Ei[m] = np.linalg.solve(Mat, rhs)
d["D"] = D; d["Ei"] = Ei
np.savez_compressed(out, **d)
T2 = Trial(dict(np.load(out)))
# checks: joins (jets at tmin from both sides), change of the density on r < rmin and at rmin
tt = np.linspace(tmin - 6, tmin, 2001)
chg = np.abs(T2.eval(tt, 0) - T.eval(tt, 0)); print("inner density change: max over modes and r < rmin: %.3e (at r = %.3g); relative to a_0: %.3e" % (chg.max(), np.exp(tt[np.unravel_index(chg.argmax(), chg.shape)[0]]), chg.max() / np.abs(T.eval(tt, 0)[:, 0]).max()))
for nu in range(NCOR):
    jl = T2.eval(np.array([tmin - 1e-12]), nu); jr = T2.eval(np.array([tmin + 1e-12]), nu)
    print("join order %d: max |inner - spline| = %.2e (scale %.2e)" % (nu, np.abs(jl - jr).max(), np.abs(jr).max()))
print("remaining lowest non-polynomial inner terms: j = %d (degree %d): max |D[m, %d]| over m > %d = %.3e" % (JMAX + 1, 3 + 2 * (JMAX + 1), JMAX, JMAX + 1, np.abs(D[JMAX + 2:, JMAX]).max() if M > JMAX + 2 else 0.0))
print("saved", out)
