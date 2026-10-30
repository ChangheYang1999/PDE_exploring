"""Graded closure with an L2 bottom level (FW-T-TB-gradedL2-v1, theory_v01, c1-t1). CONDITIONAL model.

Combines the componentwise box of FW-T-TB-graded-v1 with the signed L2 low estimate of
c1-t4 T4-019 (c1-t4/research/l2_closure/PROOF.md, sha256 e15173a4...; CLAIMED by c1-t4).
Components of J^s h: e = (P, a, b) = (||omega D^2 J^s h||, ||D J^s h||, ||J^s h||); no Hdot^-1.
Per-level inequalities for A_k h = f with phi = (F2, F1, F0) the components of J^s f,
nu = n_g(k)/sqrt(s), n_g = (P_k^2 + 2 a_k^2 + b_k^2)^(1/2), beta = certified c+1-theta-kappa:

  (L0) (beta - 3882 s - (3/10) nu) b <= F0
  (G1) (9/10 - 4290 s - (13/10) nu) a <= F1 + (6 + 1360 s) b
  (G2) (1/2 - 4708 s - (A_s + B_s) nu) P^2 <= [F2 + (347/5 + 5440 s + B_s nu) a + (10 + 34816 s) b] P + 40 a^2

(L0) is T4-019 (7) at the J^s level with the third row of K3 and the L2 rough cost (3/10) nu b^2
(T4-019 section 4); (G1), (G2) are unchanged from FW-T-TB-graded-v1 (T4-013).
Low contraction in L2: ratio <= c_s n_g / beta (T4-019 section 1 argument).

Outputs: optimal admissible scale in several forcing directions, a certified (mpmath iv) instance,
and the HEURISTIC far-field tail table with the L2 component.

Usage (from artifacts/graded_calc):
  OMP_NUM_THREADS=1 python3 -B graded_l2.py > graded_l2.out
"""
import math
from fractions import Fraction as Fr

import mpmath as mp
from scipy.optimize import minimize

BETA = 2


def gamma_l2(s, r, phi, lib=math, beta=BETA):
    r2, r1, r0 = r
    F2, F1, F0 = phi
    iv = lib is mp.iv
    sq = mp.iv.sqrt if iv else math.sqrt
    q = (lambda a, b: mp.iv.mpf(a) / b) if iv else (lambda a, b: a / b)
    ng = sq(r2 * r2 + 2 * r1 * r1 + r0 * r0)
    nu = ng / sq(s)
    As = q(127, 50) + q(653, 5) * s
    Bs = q(9, 5) * (1 + 44 * s)
    m0 = beta - 3882 * s - q(3, 10) * nu
    m1 = q(9, 10) - 4290 * s - q(13, 10) * nu
    m2 = q(1, 2) - 4708 * s - (As + Bs) * nu
    for m in (m0, m1, m2):
        if (m.a if iv else m) <= 0:
            return None
    b = F0 / m0
    a = (F1 + (6 + 1360 * s) * b) / m1
    alpha = q(347, 5) + 5440 * s + Bs * nu
    bet = 10 + 34816 * s
    P = (F2 + alpha * a + bet * b) / m2 + sq(40 / m2) * a
    return (P, a, b), dict(m0=m0, m1=m1, m2=m2, nu=nu, ng=ng)


def closes(s, r, phi):
    out = gamma_l2(s, r, phi)
    if out is None:
        return False
    return all(g <= ri for g, ri in zip(out[0], r))


def lam_for(s, r, d):
    if not closes(s, r, [0, 0, 0]):
        return 0.0
    lo, hi = 0.0, 1.0
    while closes(s, r, [hi * t for t in d]):
        hi *= 2
        if hi > 1e14:
            break
    for _ in range(60):
        mid = (lo + hi) / 2
        if closes(s, r, [mid * t for t in d]):
            lo = mid
        else:
            hi = mid
    return lo


def best_scale(d, starts):
    best = (0.0, None)
    for x0 in starts:
        def neg(x):
            s = math.exp(x[0])
            if s > 1 / 1024:
                return 0.0
            return -lam_for(s, [math.exp(t) for t in x[1:]], d)
        res = minimize(neg, x0, method='Nelder-Mead', options=dict(maxiter=8000, xatol=1e-8, fatol=1e-14))
        if -res.fun > best[0]:
            best = (-res.fun, res.x)
    return best


Db3 = [6.358653e-7, 4.967698e-9, 1.241925e-9]              # FW-A2-Db (P2, G1, G0) requirements
eta19 = 1 / 163840
T19 = [eta19, eta19 / 128, eta19 / 512]                      # T4-019 implied component requirements
starts = [[math.log(2e-5), math.log(2e-4), math.log(3e-7), math.log(3e-8)],
          [math.log(1e-5), math.log(1.5e-4), math.log(2e-7), math.log(1e-8)],
          [math.log(4e-5), math.log(2.5e-4), math.log(5e-7), math.log(1e-7)]]

print("FW-T-TB-gradedL2-v1 model (CONDITIONAL; beta = 2 from T4-019 condition (B))")
print()
print("single-direction and proportional maxima (float, Nelder-Mead; comparison-system sensitivities):")
for name, d in (("F2 only", [1, 0, 0]), ("F1 only", [0, 1, 0]), ("F0 only", [0, 0, 1]),
                ("prop. FW-A2-Db (P2,G1,G0)", Db3), ("prop. T4-019 components", T19)):
    lam, x = best_scale(d, starts)
    print(f"  {name:>28}: lambda = {lam:.4e} at s = {math.exp(x[0]):.3e}, box = {[f'{math.exp(t):.3e}' for t in x[1:]]}")

# certified instance: s = 5*2^-18, direction proportional to FW-A2-Db components
S = 5 / 2 ** 18
lam, x = best_scale(Db3, [[math.log(S)] + st[1:] for st in starts])
# re-optimize the box at fixed s
def neg_fixed(y):
    return -lam_for(S, [math.exp(t) for t in y], Db3)
res = minimize(neg_fixed, x[1:], method='Nelder-Mead', options=dict(maxiter=8000, xatol=1e-9, fatol=1e-14))
r = [float(f"{math.exp(t):.4g}") for t in res.x]
lam_r = lam_for(S, r, Db3)
lam_cert = math.floor(lam_r * 0.995)
mp.iv.dps = 50


def fs(x, n=8):
    """lower..upper of an mpmath iv interval as short strings"""
    lo, hi = (mp.mpf(str(e).strip("[]").split(",")[0]) for e in (x.a, x.b))
    return f"[{mp.nstr(lo, n)}, {mp.nstr(hi, n)}]"


sI = mp.iv.mpf(5) / 2 ** 18
rI = [mp.iv.mpf(str(t)) for t in r]
phiI = [mp.iv.mpf(lam_cert) * mp.iv.mpf(str(t)) for t in Db3]
G, mg = gamma_l2(sI, rI, phiI, lib=mp.iv)
ok = all(g.b < ri.a for g, ri in zip(G, rI))
print()
print("certified instance (mpmath iv, 50 digits):")
print(f"  s = 5*2^-18; box r = (r2, r1, r0) = {r}")
print(f"  forcing condition: (gamma_2, gamma_1, gamma_0)(F) <= {lam_cert} x FW-A2-Db (P2, G1, G0) bounds = "
      f"{[f'{lam_cert * t:.5e}' for t in Db3]}")
print("  Gamma(r, phi) <= r componentwise:", "PASS" if ok else "FAIL")
print("  Gamma:", [fs(g) for g in G])
print("  margins: m0 = %s, m1 = %s, m2 = %s" % tuple(fs(mg[k], 6) for k in ('m0', 'm1', 'm2')))
cs = 1 / (2 * mp.iv.sqrt(mp.iv.pi * sI * (1 + sI)))
d = cs * mg["ng"]
print("  n_g(r) =", fs(mg["ng"]), "; d = c_s n_g =", fs(d), "; L2 contraction c_s n_g/beta =", fs(d / BETA))
print(f"  (float scale with rounded box: {lam_r:.3f}; scalar T4-019 G0 requirement eta/512 = {eta19 / 512:.4e},"
      f" this box admits gamma_0 <= {lam_cert * Db3[2]:.4e})")

# HEURISTIC far-field tail table with the L2 component (same model as tail_budget.py)
print()
print("HEURISTIC tail table, L2 component only: sector A r^p E(theta) on r > T, G0 tail = A T^(p+1)/sqrt(-2p-2)")
delta = 0.447611
ratio = 3.1416
A6 = 3081.27
tol = {"T4-019 scalar (eta/512)": eta19 / 512, "gradedL2 instance": lam_cert * Db3[2]}
print("  n  p=p_(n+1)   A_n(model)   " + "   ".join(f"T_min[{k}]" for k in tol))
for n in (4, 5, 6, 7, 8, 10, 12, 16):
    p = 1 - (n + 1) * delta
    An = A6 * ratio ** (n - 6)
    if p >= -1:
        print(f" {n:2d}  {p:8.4f}  {An:10.3e}   not in L2 (needs p < -1)")
        continue
    c = An / math.sqrt(-2 * p - 2)
    Ts = [(c / t) ** (1 / (-(p + 1))) for t in tol.values()]
    print(f" {n:2d}  {p:8.4f}  {An:10.3e}   " + "   ".join(f"{T:10.3e}" for T in Ts))

# point tests (NORM-T-PTSYM-v1, T4-017 constant; NORM-T-PTNEC-v1, T4-007 constant) for the T4-019 ball and this box,
# applied to the N4-017 CONFIRMED Cartesian point intervals (copied in ../checks/data)
import json
from pathlib import Path
from flint import arb, ctx
ctx.prec = 256
data = json.loads((Path(__file__).resolve().parent.parent / "checks" / "data" / "N4_cartesian_witnesses.json").read_text())
PI = arb.pi()


def A_(q):
    q = Fr(q)
    return arb(q.numerator) / q.denominator


print()
print("point-test gaps (|F| minus necessary bound; positive = excluded); X_s(h) >= ||h||_(H^(2+s)) by Bessel")
for label, s, rb in (("T4-019 ball (s=2^-17, X_s(h) <= 2^-14)", Fr(1, 2 ** 17), A_(Fr(1, 2 ** 14))),
                     ("gradedL2 instance box (s=5*2^-18)", Fr(5, 2 ** 18),
                      (A_(Fr(str(r[0]))) ** 2 + 2 * A_(Fr(str(r[1]))) ** 2 + A_(Fr(str(r[2]))) ** 2).sqrt())):
    sa = A_(s)
    C0 = 1 / (4 * PI * (1 + sa)).sqrt()
    C1 = 1 / (8 * PI * sa * (1 + sa)).sqrt()
    C1s = C1 / arb(2).sqrt()
    print(" ", label, "radius", rb.mid().str(8))
    for row in data["rows"]:
        fl = row["fields"]
        F, V, Gd = arb(fl["residual"]), arb(fl["velocity_norm"]), arb(fl["gradient_norm"])
        g7 = abs(F) - ((C1 * V + C0 * (1 + Gd)) * rb + C0 * C1 * rb * rb)
        g17 = abs(F) - ((C1s * V + C0 * (1 + Gd)) * rb + C0 * C1s * rb * rb)
        print(f"    {row['candidate']:>12} {row['point']}: gap T4-007 const {g7.str(6)} ({g7 > 0}); gap T4-017 const {g17.str(6)} ({g17 > 0})")
