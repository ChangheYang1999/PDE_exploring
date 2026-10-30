"""HEURISTIC tail budget: how far out the reference must be accurate before an
n-branch exact far field (first uncancelled residual sector r^q E(theta),
q = p_(n+1) = 1 - (n+1) delta) can take over, for D(b) and for the graded model.

Amplitude model (HEURISTIC): full-circle angular L2 norm A_n of the fixed sector,
A_6 = 3081.27 (six branches, sector p_7, A2 P14) and A_7 = 9679.97 (seven branches,
sector p_8, A2 P32), extrapolated geometrically with ratio A_7/A_6 for n > 7.
Norm model: for F = r^q E(theta) on r > T (sharp onset),
  ||F||_2 = A T^(q+1)/sqrt(-2q-2),  ||D F||_2 ~ A sqrt(q^2+m^2) T^q/sqrt(-2q) (m=1),
  ||F||_Hdot^-1 <= ||r F||_2 = A T^(q+2)/sqrt(-2q-4)  (parity Hardy, rigorous UB form).
Usage: python3 -B tail_budget.py > tail_budget.out
"""
import math
cl = 4076476460239181 / 2**51
delta = 1 - 1/cl
A6, A7 = 3081.27, 9679.97
ratio = A7 / A6
thr = {
    'D(b)':   dict(H=1.272594e-9, G0=1.241925e-9, G1=4.967698e-9),
    'graded': dict(H=4.434172e-7, G0=1.905949e-7, G1=4.424294e-7),  # graded_calc.out, single-component maxima
}

def tails(q, A, T):
    G0 = A * T**(q+1) / math.sqrt(-2*q-2) if q < -1 else math.inf
    G1 = A * math.sqrt(q*q+1) * T**q / math.sqrt(-2*q) if q < 0 else math.inf
    H = A * T**(q+2) / math.sqrt(-2*q-4) if q < -2 else math.inf
    return dict(H=H, G0=G0, G1=G1)

def Tmin(q, A, th):
    # smallest T with every tail component <= its threshold (each separately)
    lo, hi = 1.0, 1.0
    def ok(T):
        t = tails(q, A, T)
        return all(t[k] <= th[k] for k in th)
    if math.isinf(tails(q, A, 2.0)['H']):
        return math.inf
    while not ok(hi):
        hi *= 10
        if hi > 1e300:
            return math.inf
    lo = hi / 10
    for _ in range(200):
        mid = math.sqrt(lo*hi)
        if ok(mid): hi = mid
        else: lo = mid
    return hi

print("HEURISTIC tail budget (see docstring). delta = %.6f, amplitude ratio per branch %.4f" % (delta, ratio))
print("convergence radius of the sector series if amplitudes grow geometrically: r_c = ratio^(1/delta) = %.2f" % ratio**(1/delta))
print("%3s %9s %11s %12s %12s %14s %14s" % ("n", "q=p_(n+1)", "A_n", "T_min D(b)", "T_min graded", "f_max(T) D(b)", "f_max(T) grad"))
for n in range(6, 31):
    q = 1 - (n+1)*delta
    A = A6 * ratio**(n-6)
    Tb = Tmin(q, A, thr['D(b)'])
    Tg = Tmin(q, A, thr['graded'])
    # near-field pointwise tolerance at the onset radius from the H component (annulus T/2<r<T, size f): ~ H_thr / T^2
    fb = thr['D(b)']['H'] / Tb**2 if math.isfinite(Tb) else 0
    fg = thr['graded']['H'] / Tg**2 if math.isfinite(Tg) else 0
    print("%3d %9.4f %11.3e %12.3e %12.3e %14.3e %14.3e" % (n, q, A, Tb, Tg, fb, fg))
