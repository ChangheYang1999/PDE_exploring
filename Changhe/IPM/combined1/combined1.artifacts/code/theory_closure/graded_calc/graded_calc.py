"""Graded (componentwise) closure model for the S1 correction equation in the
N_s component structure of analysis2 P7.5/P8.4.  Status: CONDITIONAL model.

It evaluates the box-closure conditions of framework FW-T-TB-graded-v1
(theory_v01, c1-t1).  The inequalities used are the per-level base
inequalities of A2 P7.5 (5),(6),(10), the per-component commutator table of
A2 P8.4 section 2 (unscaled), and the per-component rough-transport costs of
A2 P8.4 section 3, with the hypothesis FW-T-TB-graded-v1:H1 that every rough
cost depends on k only through n_g(k) = (P_k^2 + 2 a_k^2 + b_k^2)^(1/2)
(the unweighted H^(2+s) Bessel norm bound) and on P_k.  H1 is NOT verified.

Usage: python3 -B graded_calc.py > graded_calc.out
"""
import math
from scipy.optimize import minimize
import mpmath as mp

# A2 P8.4 (1): coefficient bounds certified for state 131
C, U1, U2, U3, R1, R2, R3, R4 = 2, 6, 24, 160, 22, 32, 80, 2048
k22 = 6*C + 28*U1 + 166*U2 + 17*R2      # top <- P
k21 = 17*U3 + 34*R3                       # top <- a
k20 = 17*R4                               # top <- b
k11 = C + 28*U1 + 149*U2 + 17*R2          # grad <- a
k10 = 17*R3                               # grad <- b
k00 = C + 28*U1 + 132*U2 + 17*R2          # L2 <- b
kHH = C                                   # H <- H
kH0 = 17*(U1 + R1)                        # H <- b
assert (k22, k21, k20, k11, k10, k00, kHH, kH0) == (4708, 5440, 34816, 4290, 1360, 3882, 2, 476)


def gamma_map(s, r, phi, lib=math):
    """Componentwise bound Gamma(r,phi) for e(h), h = A_k^{-1} f, k in box r.
    r = (r2, r1, r0, rH) box radii for (P, a, b, H) of J^s k.
    phi = (F2, F1, F0, FH): components of J^s F (P, grad, L2, Hdot^-1).
    Returns (Gamma tuple, margins dict) or None if a margin is nonpositive."""
    r2, r1, r0, rH = r
    F2, F1, F0, FH = phi
    iv = lib is mp.iv
    sq = mp.iv.sqrt if iv else math.sqrt
    q = (lambda a, b: mp.iv.mpf(a)/b) if iv else (lambda a, b: a/b)
    ng = sq(r2*r2 + 2*r1*r1 + r0*r0)
    nu = ng/sq(s)
    As = q(127, 50) + q(653, 5)*s
    Bs = q(9, 5)*(1 + 44*s)
    mH = q(19, 5) - s*kHH
    m0 = q(11, 4) - s*k00 - q(3, 10)*nu
    m1 = q(9, 10) - s*k11 - q(13, 10)*nu
    m2 = q(1, 2) - s*k22 - (As + Bs)*nu
    kap = (s*kH0 + nu)/mH
    for m in (mH, m0, m1, m2):
        if (m.a if iv else m) <= 0:
            return None
    den = 1 - kap/sq(m0)
    if (den.a if iv else den) <= 0:
        return None
    # H <= FH/mH + kap b,  b <= F0/m0 + H/sqrt(m0)
    b = (F0/m0 + FH/(mH*sq(m0)))/den
    H = FH/mH + kap*b
    a = (F1 + (6 + s*k10)*b)/m1
    alpha = q(347, 5) + s*k21 + Bs*nu
    beta = 10 + s*k20
    P = (F2 + alpha*a + beta*b)/m2 + sq(40/m2)*a
    return (P, a, b, H), dict(m2=m2, m1=m1, m0=m0, mH=mH, nu=nu, ng=ng)


def closes(s, r, phi):
    out = gamma_map(s, r, phi)
    if out is None:
        return False
    G, _ = out
    return all(g <= ri for g, ri in zip(G, r))


def max_scale(direction, verbose=False):
    """Max lambda such that phi = lambda*direction closes for some s, box."""
    best = (0, None)
    def neg(x):
        s = math.exp(x[0]); r = [math.exp(t) for t in x[1:5]]
        if s > 1/1024:
            return 0
        # largest lambda for this (s,r): Gamma is affine-increasing in lambda
        lo, hi = 0.0, 1.0
        if not closes(s, r, [0, 0, 0, 0]):
            return 0
        while closes(s, r, [hi*d for d in direction]):
            hi *= 2
            if hi > 1e12:
                break
        for _ in range(60):
            mid = (lo + hi)/2
            if closes(s, r, [mid*d for d in direction]):
                lo = mid
            else:
                hi = mid
        return -lo
    starts = []
    for ls in (-8, -10, -11, -12, -14):
        for lr in (-9, -10, -12):
            starts.append([ls, lr, lr - 6, lr - 8, lr - 8])
    for x0 in starts:
        res = minimize(neg, x0, method='Nelder-Mead',
                       options=dict(maxiter=4000, xatol=1e-6, fatol=1e-14))
        if -res.fun > best[0]:
            best = (-res.fun, res.x)
    lam, x = best
    s = math.exp(x[0]); r = [math.exp(t) for t in x[1:5]]
    return lam, s, r


def verify_iv(s, r, phi):
    """Interval re-check of the closure at rational-rounded data."""
    mp.iv.dps = 40
    S = mp.iv.mpf(s)
    R = [mp.iv.mpf(t) for t in r]
    PHI = [mp.iv.mpf(t) for t in phi]
    out = gamma_map(S, R, PHI, lib=mp.iv)
    if out is None:
        return False, None
    G, mg = out
    ok = all(g.b <= ri.a for g, ri in zip(G, R))
    return ok, (G, mg)


if __name__ == '__main__':
    print("Graded closure model FW-T-TB-graded-v1 (CONDITIONAL on H1-H3; see theory_v01)")
    # D(b) component thresholds (closure_calc.out) for comparison
    Db = dict(F2=6.358653e-7, F1=4.967698e-9, F0=1.241925e-9, FH=1.272594e-9)
    names = ['F2', 'F1', 'F0', 'FH']
    dirs = {
        'top only (F2)': [1, 0, 0, 0],
        'gradient only (F1)': [0, 1, 0, 0],
        'L2 only (F0)': [0, 0, 1, 0],
        'Hdot^-1 only (FH)': [0, 0, 0, 1],
        'D(b) proportional': [Db[n] for n in names],
        'far-field shape p7,T=10 (H:G0:G1 = 4510:150.6:25.9, P2=0)': [0, 25.9, 150.6, 4510],
    }
    for label, d in dirs.items():
        lam, s, r = max_scale(d)
        phi = [lam*0.999*t for t in d]
        ok, info = verify_iv(s, r, phi)
        line = f"{label}: lambda={lam:.6e} at s={s:.4e}, box r=(" + ", ".join(f"{t:.3e}" for t in r) + ")"
        print(line)
        print(f"   interval re-check at 0.999*lambda: {'PASS' if ok else 'FAIL'}")
        if label.endswith('only (F2)'):
            print(f"   compare D(b) P2 bound {Db['F2']:.4e}: gain {lam/Db['F2']:.2f}")
        for n, t in zip(names, d):
            if t and 'only' in label:
                print(f"   compare D(b) {n} bound {Db[n]:.4e}: gain {lam*t/Db[n]:.2f}")
        if label == 'D(b) proportional':
            print(f"   uniform gain over D(b) component bounds: {lam:.2f}")
        if label.startswith('far-field'):
            sc = lam
            print(f"   admissible scale {sc:.3e} vs actual 1 (tail model p7, T=10): gap {1/sc:.3e}")
            # D(b) scalar: N_s >= 512*sqrt(20/21)*H etc.; scalar requirement for this direction
            import math as m
            Ns = m.sqrt((128*25.9)**2 + (512*150.6)**2 + (512*m.sqrt(20/21)*4510)**2)
            print(f"   D(b) scalar gap for the same direction: N_s/eta = {Ns/(1/1572864):.3e}")
