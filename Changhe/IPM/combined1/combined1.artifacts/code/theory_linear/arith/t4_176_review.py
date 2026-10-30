"""Checks for the c1-t2 review of T4-176 (c1-t4 research/annular_symmetric_coupling/PROOF.md, sha256
f1ad59b6...80e5): annular localized symmetric coupling bound (reviews/REVIEW_T4_176.md).

Run from artifacts/:  python3 -B -u arith/t4_176_review.py   (a few minutes)
Parts:
  (1) sympy: the kernel identity (6) from the exponential form; the radial integrals of the far part; the constants
      N, T and D_delta of (2) from the stated intermediate bounds; the scaling (4); the kappa-family generalization
      (cut at |x - y| = kappa R) of Remark R1, which reduces to (2) at kappa = 1/2.
  (2) FLOAT: ||E||_HS by direct 4D quadrature of the kernel (6) for explicit v and psi, against the bound (3), the
      T4-163 global bound and the coarse bound ||v||_inf (exp(osc psi) - 1).
      v_A = grad <X>^gamma (G = H = gamma, proved in the review), v_B = <X>^(-delta) e1 (G = 1, H = delta),
      gamma = 1/c, delta = 1 - gamma; psi = eps phi(|X|/R) with the tent phi = (r - 1) on [1, 2], (3 - r) on [2, 3]
      (Lambda = 3, ||phi||_inf = 1, Lip phi = 1, ||grad phi||_2 = sqrt(8 pi), ||phi||_2 = sqrt(8 pi/3)), and one
      signed case psi = eps phi(|X|/R) cos(2 theta).
Output: logs/t4_176_review.log (stdout), data/t4_176_review_results.json.
"""
import json
import time
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import optimize

HERE = Path(__file__).resolve().parents[1]
T0 = time.monotonic()
OUT = {}

# =============================== (1) sympy ===============================
d, a, b = sp.symbols("d a b", real=True)
assert sp.simplify((((sp.exp(d) - 1) * a + (sp.exp(-d) - 1) * b) - ((sp.cosh(d) - 1) * (a + b) + sp.sinh(d) * (a - b))).rewrite(sp.exp)) == 0
print("(1) (exp d - 1) a + (exp(-d) - 1) b = (cosh d - 1)(a + b) + sinh d (a - b): the two forms of (6) agree")
pa, pb = sp.symbols("p q", nonnegative=True)
assert sp.expand(pa**2 + pb**2 - (pa - pb) ** 2) == 2 * pa * pb                 # >= 0 for p, q >= 0
assert sp.expand(2 * (pa**2 + pb**2) - (pa - pb) ** 2 - (pa + pb) ** 2) == 0          # signed case
print("    d^2 <= psi(x)^2 + psi(y)^2 for psi >= 0 (difference 2 psi(x) psi(y)); d^2 <= 2(psi(x)^2 + psi(y)^2) in general")
r, R, G, H, A, B, L, Ps, dl, kap = sp.symbols("r R G H A B L Psi delta kappa", positive=True)
I_far = sp.integrate(2 * sp.pi * r * r**-4, (r, R / 2, sp.oo))
assert sp.simplify(I_far - 4 * sp.pi / R**2) == 0
I_small = sp.integrate(2 * sp.pi * r * r ** (-2 * dl), (r, 0, R / 2), conds="none")
assert sp.simplify(I_small - sp.pi * (R / 2) ** (2 - 2 * dl) / (1 - dl)) == 0
small = 16 * G**2 * R**-4 * I_small
assert sp.simplify(sp.powsimp(small / (4 * sp.pi * 2 ** (2 * dl) * G**2 * R ** (-2 * dl - 2) / (1 - dl)), force=True)) == 1
print("    int_(|z| >= R/2) |z|^-4 dz = 4 pi/R^2;  int_(|y| < R/2) |y|^(-2 delta) dy = pi (R/2)^(2 - 2 delta)/(1 - delta)"
      " (delta < 1);  16 G^2 R^-4 times it = 4 pi 2^(2 delta) G^2 R^(-2 delta - 2)/(1 - delta)")
second = 4 * sp.pi * 2 ** (2 * dl) * G**2 * R ** (-2 * dl - 2) * (1 + 1 / (1 - dl))
Dd = 1 + 2**dl * sp.sqrt((2 - dl) / (1 - dl))
inner = G * R**-dl * sp.sqrt(I_far) + sp.sqrt(second)
assert sp.simplify(sp.powsimp((inner / (2 * sp.sqrt(sp.pi) * G * R ** (-dl - 1) * Dd)).rewrite(sp.exp), force=True)) == 1
far = sp.exp(Ps) * B / (2 * sp.sqrt(2) * sp.pi) * 2 * sp.sqrt(sp.pi) * G * R ** (-dl - 1) * Dd
T = sp.exp(Ps) * G * (B / R) * Dd / sp.sqrt(2 * sp.pi)
assert sp.simplify(far - R**-dl * T) == 0
print("    square root in (8) <= 2 sqrt(pi) G R^(-delta-1) D_delta, D_delta = 1 + 2^delta sqrt((2 - delta)/(1 - delta));"
      " far part = R^(-delta) T with T = exp(Psi) G (B/R) D_delta/sqrt(2 pi)")
GR, HR = 2**dl * G * R**-dl, 2 ** (dl + 1) * H * R ** (-dl - 1)
near = sp.cosh(Ps) / (4 * sp.pi) * (GR * A * (L / R) * sp.sqrt(sp.pi) * R / 2 + A * HR * sp.sqrt(sp.pi) * R / 2)
N = sp.cosh(Ps) * A * (2**dl * G * L + 2 ** (dl + 1) * H) / (8 * sp.sqrt(sp.pi))
assert sp.simplify(near - R**-dl * N) == 0
z = sp.symbols("z", positive=True)
assert sp.integrate(2 * sp.pi * z * z**2 * z**-4 * z**2, (z, 0, R / 2)) == sp.pi * R**2 / 4      # int_(|z|<R/2) dz
print("    near part: cosh(Psi)/(4 pi) [G_R A Lip(psi) + A H_R] sqrt(pi) R/2 = R^(-delta) N with L* = R Lip(psi)")
# kappa family (Remark R1): cut at |x - y| = kappa R, split |y| at (1 - kappa) R
Nk = sp.cosh(Ps) * A * kap * ((1 - kap) ** -dl * G * L + (1 - kap) ** (-dl - 1) * H) / (4 * sp.sqrt(sp.pi))
Tk = sp.exp(Ps) * G * (B / R) / (2 * sp.sqrt(2 * sp.pi)) * (1 / kap + sp.sqrt((1 - kap) ** (-2 * dl) / kap**2
                                                                           + (1 - kap) ** (2 - 2 * dl) / ((1 - dl) * kap**4)))
assert sp.simplify(sp.powsimp((Nk.subs(kap, sp.Rational(1, 2)) - N).rewrite(sp.exp), force=True)) == 0
assert sp.simplify(sp.powsimp((Tk.subs(kap, sp.Rational(1, 2)) - T).rewrite(sp.exp), force=True)) == 0
print("    kappa family N_kappa, T_kappa (Remark R1) equals (2) at kappa = 1/2")
Nk_f = sp.lambdify((kap, Ps, A, G, L, H, dl), Nk, "numpy")
Tk_f = sp.lambdify((kap, Ps, B, R, G, dl), Tk, "numpy")

# =============================== (2) FLOAT quadrature ===============================
c = 4076476460239181 / 2**51
gam = 1 / c
delta = 1 - gam


def K2(z1, z2):
    q = z1 * z1 + z2 * z2
    return -2 * z1 * z2 / (2 * np.pi * q * q), (z1 * z1 - z2 * z2) / (2 * np.pi * q * q)


def vA(x1, x2):                                   # grad <X>^gamma
    f = gam * (1 + x1 * x1 + x2 * x2) ** (gam / 2 - 1)
    return f * x1, f * x2


def vB(x1, x2):                                   # <X>^(-delta) e1
    return (1 + x1 * x1 + x2 * x2) ** (-delta / 2), 0 * x1


def tent(s):
    return np.clip(np.minimum(s - 1, 3 - s), 0, None)


def psi_fun(eps, R, signed):
    if signed:
        return lambda x1, x2: eps * tent(np.hypot(x1, x2) / R) * np.cos(2 * np.arctan2(x2, x1))
    return lambda x1, x2: eps * tent(np.hypot(x1, x2) / R)


def gl(a_, b_, n):
    u, w = np.polynomial.legendre.leggauss(n)
    return (b_ - a_) / 2 * u + (b_ + a_) / 2, (b_ - a_) / 2 * w


def hs2(v, psi, R, nx=12, nxt=24, nz=16, nzt=96, M=30.0):
    """int_(|x| < M R) int_(R^2) |e(x, x + z)|^2 dz dx. Both v and psi are even in x1 and in x2, and |K.w|^2 is
    invariant under the corresponding reflections of (z, w), so x runs over the first quadrant with weight 4."""
    xr, xw = [], []
    for a_, b_ in ((0, 1), (1, 2), (2, 3), (3, 6), (6, 12), (12, M)):
        n_, w_ = gl(a_ * R, b_ * R, nx)
        xr.append(n_), xw.append(w_ * n_)
    xr, xw = np.concatenate(xr), np.concatenate(xw)
    th = (np.arange(nxt) + 0.5) * (np.pi / 2) / nxt
    zr, zw = [], []
    for a_, b_ in ((1e-4, 1e-2), (1e-2, 0.1), (0.1, 0.5), (0.5, 1), (1, 2), (2, 4), (4, 8), (8, 64), (64, 2e3)):
        n_, w_ = gl(np.log(a_ * R), np.log(b_ * R), nz)
        zr.append(np.exp(n_)), zw.append(w_ * np.exp(2 * n_))        # dz = r^2 d(log r) dtheta
    zr, zw = np.concatenate(zr), np.concatenate(zw)
    zt = 2 * np.pi * np.arange(nzt) / nzt
    Z1 = (zr[:, None] * np.cos(zt)[None, :]).ravel()
    Z2 = (zr[:, None] * np.sin(zt)[None, :]).ravel()
    ZW = (zw[:, None] * np.full(nzt, 2 * np.pi / nzt)[None, :]).ravel()
    k1, k2 = K2(Z1, Z2)
    tot = 0.0
    for rx, wx in zip(xr, xw):
        for t in th:
            x1, x2 = rx * np.cos(t), rx * np.sin(t)
            px = psi(np.array([x1]), np.array([x2]))[0]
            y1, y2 = x1 + Z1, x2 + Z2
            dd = px - psi(y1, y2)
            if px == 0 and not np.any(dd):
                continue
            vx1, vx2 = v(x1, x2)
            vy1, vy2 = v(y1, y2)
            em, ep = np.expm1(dd), np.expm1(-dd)
            e = (k1 * (em * vx1 + ep * vy1) + k2 * (em * vx2 + ep * vy2)) / 2
            tot += 4 * wx * (np.pi / 2 / nxt) * np.sum(e * e * ZW)
    return tot


def far_tail(R, M, Gglob, Psi_osc, B2):
    """upper bound for int_(|x| > M R) int |e|^2: there d = -psi(y), y in supp psi (|y| <= 3R), |x - y| >= |x| - 3R,
    |e| <= exp(osc) |d| 2 Gglob/(4 pi |x - y|^2); int_(|x| > MR) (|x| - 3R)^-4 dx = 2 pi int_(MR)^inf r (r - 3R)^-4 dr"""
    s = M * R - 3 * R
    I = 2 * np.pi * (1 / (2 * s**2) + 3 * R / (3 * s**3))
    return np.exp(2 * Psi_osc) * (2 * Gglob) ** 2 / (16 * np.pi**2) * B2 * I


def J(A_, B_, H0, D):
    Rr, S = 2 * B_ / A_, D / H0
    lo, hi = min(Rr, S), max(Rr, S)
    return np.sqrt(2 * np.pi) * A_ * H0 * lo * np.sqrt(1 + np.log(hi / lo))


# exact data of the tent: ||grad phi||_2^2 = 2 pi int_1^3 r dr = 8 pi; ||phi||_2^2 = 2 pi (7/12 + 3/4) = 8 pi/3
assert sp.integrate(2 * sp.pi * r, (r, 1, 3)) == 8 * sp.pi
assert sp.integrate(2 * sp.pi * r * (r - 1) ** 2, (r, 1, 2)) + sp.integrate(2 * sp.pi * r * (3 - r) ** 2, (r, 2, 3)) == 8 * sp.pi / 3
# sup |v_A| = gamma max_s sqrt(s) (1 + s)^(gamma/2 - 1), at s = 1/(1 - gamma)
sA = 1 / (1 - gam)
GA_glob = gam * np.sqrt(sA) * (1 + sA) ** (gam / 2 - 1)
VCASES = {"v_A = grad <X>^gamma": (vA, gam, gam, GA_glob, gam), "v_B = <X>^-delta e1": (vB, 1.0, delta, 1.0, delta)}
print(f"(2) gamma = 1/c = {gam:.12f}, delta = {delta:.12f}; ||v_A||_inf = {GA_glob:.6f}, Lip v_A = gamma;"
      " ||v_B||_inf = 1, Lip v_B <= delta")


def case(vname, eps, R, signed=False, **kw):
    v, G_, H_, Gglob, Hglob = VCASES[vname]
    psi = psi_fun(eps, R, signed)
    if signed:
        # |grad psi|^2 = eps^2 [phi'(s)^2 cos^2(2t)/R^2 + 4 phi(s)^2 sin^2(2t)/r^2], s = r/R
        # sup over angles of a cos^2 + b sin^2 is max(a, b); 2 phi(s)/s <= 1 on [1, 3] (equality at s = 2)
        ss = np.linspace(1, 3, 200001)
        Lip = eps / R * max(1.0, np.max(2 * tent(ss) / ss))
        Iphi = float(sp.integrate((r - 1) ** 2 / r, (r, 1, 2)) + sp.integrate((3 - r) ** 2 / r, (r, 2, 3)))
        A_ = eps * np.sqrt(4 * np.pi * (1 + Iphi))       # int phi'^2 cos^2/R^2 = 4 pi, int 4 phi^2 sin^2/r^2 = 4 pi Iphi
        B_ = eps * R * np.sqrt(4 * np.pi / 3)
        osc = 2 * eps
        fac = np.sqrt(2)
    else:
        Lip, A_, B_, osc, fac = eps / R, eps * np.sqrt(8 * np.pi), eps * R * np.sqrt(8 * np.pi / 3), eps, 1.0
    Nn = np.cosh(osc) * A_ * (2**delta * G_ * R * Lip + 2 ** (delta + 1) * H_) / (8 * np.sqrt(np.pi))
    Tt = fac * np.exp(osc) * G_ * (B_ / R) * (1 + 2**delta * np.sqrt((2 - delta) / (1 - delta))) / np.sqrt(2 * np.pi)
    bound = R**-delta * np.hypot(Nn, Tt)
    kbest = optimize.minimize_scalar(lambda k: np.hypot(Nk_f(k, osc, A_, G_, R * Lip, H_, delta),
                                                        fac * Tk_f(k, osc, B_, R, G_, delta)),
                                     bounds=(0.02, 0.98), method="bounded")
    bound_k = R**-delta * kbest.fun
    q = hs2(v, psi, R, **kw)
    # x-tail |x| > M R, plus the z-tail |z| > 2e3 R for x in supp psi (there d = psi(x), int_(|z|>Z) |z|^-4 = pi/Z^2)
    tail = far_tail(R, kw.get("M", 30.0), Gglob, osc, B_**2) \
        + np.exp(2 * osc) * (2 * Gglob) ** 2 / (16 * np.pi**2) * B_**2 * np.pi / (2e3 * R) ** 2
    hs_lo, hs_hi = np.sqrt(q), np.sqrt(q + tail)
    t163 = np.cosh(osc) / (4 * np.pi) * (Gglob * J(A_, B_, Lip, osc) + J(A_, B_, Hglob, 2 * Gglob))
    coarse = Gglob * np.expm1(osc)
    row = dict(v=vname, eps=eps, R=R, signed=signed, HS_quad=hs_lo, HS_upper=hs_hi, bound3=bound, N=Nn, T=Tt,
               bound_kappa=bound_k, kappa_opt=kbest.x, T4_163=t163, coarse=coarse, ratio=hs_hi / bound, res=kw)
    print(f"    {vname:22s} eps = {eps:<8.4g} R = {R:<5g} {'signed' if signed else '      '} ||E||_HS = {hs_lo:.5e}"
          f" (<= {hs_hi:.5e} with tail)  bound (3) = {bound:.5e}  ratio {hs_hi / bound:.4f};  kappa-opt {bound_k:.5e}"
          f" at kappa {kbest.x:.3f};  T4-163 {t163:.4e};  coarse {coarse:.4e}  [{time.monotonic() - T0:.0f} s]")
    assert hs_hi <= bound
    return row


rows = []
print("    resolution check (v_A, eps = 1/2, R = 4): default and refined grids")
rows.append(case("v_A = grad <X>^gamma", 0.5, 4.0))
rows.append(case("v_A = grad <X>^gamma", 0.5, 4.0, nx=18, nxt=36, nz=24, nzt=144))
for vname in VCASES:
    for R_ in (1.0, 4.0, 16.0, 64.0):
        for eps in (0.5, R_**-delta):
            if R_ == 4.0 and eps == 0.5 and vname.startswith("v_A"):
                continue
            rows.append(case(vname, eps, R_))
rows.append(case("v_A = grad <X>^gamma", 0.5, 4.0, signed=True))
rows.append(case("v_A = grad <X>^gamma", 0.5, 16.0, signed=True))
OUT["cases"] = rows
print("    R^delta ||E||_HS at eps = 1/2 (v_A): " + ", ".join(f"R = {e['R']:g}: {e['R'] ** delta * e['HS_quad']:.5f}"
                                                       for e in rows[2:] if e["v"].startswith("v_A") and e["eps"] == 0.5
                                                       and not e["signed"]))
OUT["elapsed_seconds"] = time.monotonic() - T0
(HERE / "data/t4_176_review_results.json").write_text(json.dumps(OUT, indent=1, default=float))
print(f"done in {time.monotonic() - T0:.1f} s; wrote data/t4_176_review_results.json")
