"""Checks for the c1-t2 review of T4-194 (S1 velocity estimate in a weighted gradient norm, -1 < p < 3).

Source (read only):
  c1-t4/research/weighted_gradient_velocity/PROOF.md  sha256 831cb25f0216615457c13166a4cf3b80737f244c35e3dcc0a5d837c1b5372fad

The proof is analytic. Part A (sympy) checks its algebra. Part B (numpy/scipy) is FLOAT illustration on explicit
functions. Nothing here is a proof.
  A1 symbols: (symbol of dbar) m_B = (symbol of d); U2 + i U1 = -(1 + m_B)/2.
  A2 Cartesian check of d(f e^(i m theta)) = e^(i(m-1)theta)(f' + m f/r)/2 and
     dbar(g e^(i(m-2)theta)) = e^(i(m-1)theta)(g' - (m-2)g/r)/2 for m = -3, -1, 1, 3; hence (5).
  A3 the Section 1 mode solutions solve (5); the m = 1 homogeneous solution; for m = -M and f = e^(M t)(a0 + a1 e^(2t))
     the r^M terms cancel, so g = a1 r^(M+2)/(M+2) = O(r^|m-2|).
  A4 the pointwise identities behind (7), (8), (9): each integrand difference is an exact t-derivative.
  A5 the ratio bounds (10), (11): the elementary inequality, monotonicity, A(p), B(p), C_0, C_1, C_(3/2); FLOAT grid
     check of the suprema over M <= 60, 0 <= q <= p, 0 <= dot q <= 50.
  A6 Section 3: the Young factors and their maxima; the weight ratio bound.
  A7 Sections 4 and 5: |grad(sin(3 theta)/r^3)|^2 = 9/r^8, the exponent 2p - 7, -d_y K2 = sin(3 theta)/(pi r^3),
     a = int chi r^-2 dr, the exponent in (15), sum 4^-j = 1/3.
  A8 pure power weight (Mellin) symbol of the m = -M energy ratio: decreasing in tau^2, value A_M B_M at tau = 0 with
     q = p (review remark R2); constants (3), (4), 1/(1 - |p|) (review remark R1) and the lower bounds of remark R2,
     with the maximum of (3)/LB on a fine p grid.
  B1 FLOAT 2D FFT: the canonical multiplier m_B applied to h = r^|m| exp(-r^2) e^(i m theta), m = 1, 3, 5, -1, -3,
     against g(r) e^(i(m-2)theta) from the Section 1 formulas (radial quadrature); a = d_y U2[h_*](0) by FFT.
  B2 FLOAT radial: weighted energies of compactly supported smooth profiles (one touching the origin, one annular),
     m = 1, 3, 5, -1, -3, -5, p from -0.9 to 2.9, R = 1: residuals of (5), (7), (8), and E_g/E_f against the bounds.
  B3 FLOAT: profiles f = w^-1 times a slow bump far out (frozen coefficients) for m = -1, -3: E_g/E_f approaches A_M B_M
     at q = p.
Runtime: about 15 s on one core; peak resident memory about 0.76 GB (B1).
"""
import sys
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.signal import lfilter

T0 = time.time()
print("t4_194_review.py start", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
I = sp.I

# ---------------------------------------------------------------- A1
k1, k2 = sp.symbols("xi1 xi2", real=True)
mB = (k1 - I * k2) ** 2 / (k1 ** 2 + k2 ** 2)
sym_d = I * (k1 - I * k2) / 2          # d = (d_x - i d_y)/2, d_x -> i xi1
sym_db = I * (k1 + I * k2) / 2         # dbar = (d_x + i d_y)/2
print("A1 sym(dbar) m_B - sym(d) =", sp.simplify(sym_db * mB - sym_d))
U1s = k1 * k2 / (k1 ** 2 + k2 ** 2)    # -R1 R2, R_j -> -i xi_j/|xi|
U2s = -k1 ** 2 / (k1 ** 2 + k2 ** 2)   # R1^2
print("A1 U2 + i U1 + (1 + m_B)/2 =", sp.simplify(U2s + I * U1s + (1 + mB) / 2))

# ---------------------------------------------------------------- A2
x, y = sp.symbols("x y", real=True)
rr = sp.sqrt(x ** 2 + y ** 2)
fF = sp.Function("f")
gF = sp.Function("g")
rs = sp.symbols("r", positive=True)


def mode(fun, k):
    """fun(r) e^(i k theta) in Cartesian form, with e^(i theta) = (x + i y)/r."""
    e = (x + I * y) / rr if k >= 0 else (x - I * y) / rr
    return fun(rr) * e ** abs(k)


def radial_d(fun):
    return sp.diff(fun(rs), rs).subs(rs, rr)


for m in (-3, -1, 1, 3):
    h = mode(fF, m)
    lhs = (sp.diff(h, x) - I * sp.diff(h, y)) / 2
    rhs = mode(lambda r_: (radial_d(fF) + m * fF(rr) / rr) / 2, m - 1)
    g = mode(gF, m - 2)
    lhs2 = (sp.diff(g, x) + I * sp.diff(g, y)) / 2
    rhs2 = mode(lambda r_: (radial_d(gF) - (m - 2) * gF(rr) / rr) / 2, m - 1)
    z1 = sp.simplify(sp.expand(lhs - rhs))
    z2 = sp.simplify(sp.expand(lhs2 - rhs2))
    print(f"A2 m = {m}: d(f e^(i m th)) - e^(i(m-1)th)(f' + m f/r)/2 = {z1};  dbar(g e^(i(m-2)th)) - e^(i(m-1)th)(g' - (m-2)g/r)/2 = {z2}")
print("A2 so dbar B h_m = d h_m reads (g_r - (m-2)g/r) = (f_r + m f/r); with t = log r this is (5).")

# ---------------------------------------------------------------- A3
t, s_ = sp.symbols("t s", real=True)
mm = sp.symbols("m", integer=True)
ff = sp.Function("f")
gpos = ff(t) - 2 * (mm - 1) * sp.Integral(sp.exp((mm - 2) * (t - s_)) * ff(s_), (s_, t, sp.oo))
gneg = ff(t) + 2 * (mm - 1) * sp.Integral(sp.exp((mm - 2) * (t - s_)) * ff(s_), (s_, -sp.oo, t))
for name, gg in (("m >= 3", gpos), ("m <= -1", gneg)):
    res = sp.diff(gg, t) - (mm - 2) * gg - sp.diff(ff(t), t) - mm * ff(t)
    print(f"A3 {name}: dot g - (m-2) g - dot f - m f =", sp.simplify(res))
Cc = sp.symbols("C")
print("A3 m = 1: homogeneous solution of dot k + k = 0 is C e^(-t) = C/r, check:", sp.simplify(sp.diff(Cc * sp.exp(-t), t) + Cc * sp.exp(-t)))
Mp = sp.symbols("M", positive=True)
a0, a1 = sp.symbols("a0 a1")
fpoly = sp.exp(Mp * s_) * (a0 + a1 * sp.exp(2 * s_))
mval = -Mp
gint = sp.integrate(sp.exp((mval - 2) * (t - s_)) * fpoly, (s_, -sp.oo, t), conds="none")
gcan = sp.simplify(fpoly.subs(s_, t) + 2 * (mval - 1) * gint)
print("A3 m = -M, f = e^(M t)(a0 + a1 e^(2t)): g =", sp.simplify(sp.expand(gcan)), " (expected a1 e^((M+2)t)/(M+2); difference",
      sp.simplify(gcan - a1 * sp.exp((Mp + 2) * t) / (Mp + 2)), ")")

# ---------------------------------------------------------------- A4
w = sp.Function("w")(t)
f_ = sp.Function("f")(t)
g_ = sp.Function("g")(t)
q = sp.diff(w, t) / w
D = lambda e: sp.diff(e, t)
m = sp.symbols("m")
I7 = (w ** 2 * (D(g_) ** 2 + (m - 2) ** 2 * g_ ** 2) - w ** 2 * (D(f_) ** 2 + m ** 2 * f_ ** 2)
      + 2 * q * w ** 2 * (m * f_ ** 2 + (m - 2) * g_ ** 2) - D(w ** 2 * ((m - 2) * g_ ** 2 + m * f_ ** 2))
      - w ** 2 * ((D(g_) - (m - 2) * g_) ** 2 - (D(f_) + m * f_) ** 2))
print("A4 (7) pointwise: integrand difference minus exact derivative minus w^2[(5)_L^2 - (5)_R^2] =", sp.simplify(sp.expand(I7)))
M = sp.symbols("M", positive=True)
F = w * f_
G = w * g_
lhs8 = D(G) ** 2 + ((M + 2 - q) ** 2 + D(q)) * G ** 2
rhs8 = D(F) ** 2 + ((M + q) ** 2 + D(q)) * F ** 2
I8 = (lhs8 - rhs8 + D((M + 2 - q) * G ** 2 + (M + q) * F ** 2)
      - w ** 2 * ((D(g_) - (-M - 2) * g_) ** 2 - (D(f_) - M * f_) ** 2))
print("A4 (8) pointwise (m = -M): =", sp.simplify(sp.expand(I8)))
I9g = w ** 2 * (D(g_) ** 2 + (M + 2) ** 2 * g_ ** 2) - (D(G) ** 2 + ((M + 2) ** 2 + q ** 2 + D(q)) * G ** 2) + D(q * G ** 2)
I9f = w ** 2 * (D(f_) ** 2 + M ** 2 * f_ ** 2) - (D(F) ** 2 + (M ** 2 + q ** 2 + D(q)) * F ** 2) + D(q * F ** 2)
print("A4 (9) pointwise: E_g form", sp.simplify(sp.expand(I9g)), "; E_f form", sp.simplify(sp.expand(I9f)))
Rr, pp = sp.symbols("R p", positive=True)
wexp = (1 + sp.exp(2 * t) / Rr ** 2) ** (pp / 2)
qq = sp.simplify(sp.diff(wexp, t) / wexp)
print("A4 q for w = (1 + e^(2t)/R^2)^(p/2):", qq, "; minus p e^(2t)/(R^2 + e^(2t)):", sp.simplify(qq - pp * sp.exp(2 * t) / (Rr ** 2 + sp.exp(2 * t))),
      "; dot q - 2 p R^2 e^(2t)/(R^2+e^(2t))^2:", sp.simplify(sp.diff(qq, t) - 2 * pp * Rr ** 2 * sp.exp(2 * t) / (Rr ** 2 + sp.exp(2 * t)) ** 2))

# ---------------------------------------------------------------- A5
aa, bb, dd = sp.symbols("a b d", positive=True)
print("A5 a/b - (a+d)/(b+d) =", sp.factor(aa / bb - (aa + dd) / (bb + dd)), " (>= 0 when a >= b)")
qs = sp.symbols("q", nonnegative=True)
print("A5 (M+2)^2 + q^2 - (M+2-q)^2 =", sp.expand((M + 2) ** 2 + qs ** 2 - (M + 2 - qs) ** 2),
      "; (M+q)^2 - (M^2+q^2) =", sp.expand((M + qs) ** 2 - M ** 2 - qs ** 2))
xx = sp.symbols("x", real=True)
print("A5 d/dx log((1+x^2)/(1-x)^2) =", sp.factor(sp.diff(sp.log((1 + xx ** 2) / (1 - xx) ** 2), xx)), " (> 0 on 0 <= x < 1)")
print("A5 d/dx (1+x)^2/(1+x^2) =", sp.factor(sp.diff((1 + xx) ** 2 / (1 + xx ** 2), xx)), "; value at x = 1:", ((1 + xx) ** 2 / (1 + xx ** 2)).subs(xx, 1))
pa = sp.symbols("p", nonnegative=True)
Aexpr = sp.simplify(((1 + xx ** 2) / (1 - xx) ** 2).subs(xx, pa / 3))
print("A5 (1+x^2)/(1-x)^2 at x = p/3:", sp.factor(Aexpr), "; minus (9+p^2)/(3-p)^2:", sp.simplify(Aexpr - (9 + pa ** 2) / (3 - pa) ** 2))
Af = lambda p_: (9 + p_ ** 2) / (3 - p_) ** 2
Bf = lambda p_: (1 + p_) ** 2 / (1 + p_ ** 2) if p_ <= 1 else sp.Integer(2)
Cf = lambda p_: (1 + sp.sqrt((1 + Af(p_) * Bf(p_)) / 2)) / 2
for p_, exp_ in ((sp.Integer(0), sp.Integer(1)), (sp.Integer(1), (1 + sp.sqrt(3)) / 2), (sp.Rational(3, 2), (1 + sp.sqrt(sp.Rational(11, 2))) / 2)):
    print(f"A5 C_{p_} = {sp.nsimplify(Cf(p_))} ; printed {exp_}; difference {sp.simplify(Cf(p_) - exp_)}")
worst10 = worst11 = 0.0
for p_ in np.linspace(0.0, 2.99, 300):
    A_ = (9 + p_ ** 2) / (3 - p_) ** 2
    B_ = (1 + p_) ** 2 / (1 + p_ ** 2) if p_ <= 1 else 2.0
    for M_ in range(1, 61):
        qv = np.linspace(0.0, p_, 201)[:, None]
        qd = np.array([0.0, 0.1, 1.0, 10.0, 50.0])[None, :]
        r10 = ((M_ + 2) ** 2 + qv ** 2 + qd) / ((M_ + 2 - qv) ** 2 + qd)
        r11 = ((M_ + qv) ** 2 + qd) / (M_ ** 2 + qv ** 2 + qd)
        worst10 = max(worst10, float(np.max(r10)) / A_)
        worst11 = max(worst11, float(np.max(r11)) / B_)
print(f"A5 FLOAT grid (p in [0, 2.99], M <= 60): max ratio(10)/A(p) = {worst10:.12f}, max ratio(11)/B(p) = {worst11:.12f} (both must be <= 1)")

# ---------------------------------------------------------------- A6
pn = sp.symbols("p", real=True)
mm_ = sp.symbols("m", positive=True)
Lp = 1 + 2 * (mm_ - 1) / (mm_ - 2 + pn)
print("A6 d/dm [1 + 2(m-1)/(m-2+p)] =", sp.factor(sp.diff(Lp, mm_)), " (< 0 for p < 1); value at m = 3:", sp.simplify(Lp.subs(mm_, 3)))
Lm = (M + 2) / M * (1 + 2 * (M + 1) / (M + 2))
print("A6 [(M+2)/M][1 + 2(M+1)/(M+2)] - (3 + 4/M) =", sp.simplify(Lm - 3 - 4 / M), "; at M = 1:", Lm.subs(M, 1))
print("A6 weight ratio: for p < 0, p <= q <= 0, so w(t)/w(s) = exp(-int_t^s q) <= exp(-p (s - t)) for s >= t and <= 1 for s <= t;"
      " kernel exp(-(m-2)(s-t)) exp(-p(s-t)) has L1 norm 1/(m-2+p) > 0 since m >= 3, p > -1.")

# ---------------------------------------------------------------- A7
th = sp.symbols("theta", real=True)
r_ = sp.symbols("r", positive=True)
V = sp.sin(3 * th) / r_ ** 3
grad2 = sp.diff(V, r_) ** 2 + (sp.diff(V, th) / r_) ** 2
print("A7 |grad(sin(3 theta)/r^3)|^2 =", sp.simplify(grad2))
print("A7 weighted integrand r^(2p) * 9 r^-8 * r = 9 r^(2p-7); diverges iff 2p - 7 >= -1 iff p >= 3")
K2 = (x ** 2 - y ** 2) / (2 * sp.pi * (x ** 2 + y ** 2) ** 2)
dyK2 = sp.diff(K2, y)
pol = sp.simplify(sp.trigsimp((-dyK2).subs({x: r_ * sp.cos(th), y: r_ * sp.sin(th)})))
print("A7 -d_y K2 in polar:", pol, "; minus sin(3 theta)/(pi r^3):", sp.simplify(sp.expand_trig(pol - sp.sin(3 * th) / (sp.pi * r_ ** 3))))
print("A7 d/dX2 K2(X - Y) at X = 0 equals (d_2 K2)(-Y) = -(d_2 K2)(Y) = sin(3 phi)/(pi |Y|^3) (d_2 K2 is odd)")
print("A7 int_0^(2 pi) sin(3 phi)^2 d phi =", sp.integrate(sp.sin(3 * th) ** 2, (th, 0, 2 * sp.pi)),
      "; so a = (1/pi) * pi * int chi(r) r^-3 r dr = int_1^2 chi r^-2 dr")
Ls = sp.symbols("L", positive=True)
print("A7 (15): D_p(h_L)^2 = L^2 int (1 + L^2|Y|^2/R^2)^p |grad h_*|^2 dY <= L^(2+2p) R^(-2p) ||grad h_*||^2 for p < 0, |Y| >= 1;"
      " so D_p(h_L) <= C L^(p+1)")
jj = sp.symbols("j", integer=True, positive=True)
print("A7 sum_(j>=1) 4^-j =", sp.summation(sp.Rational(1, 4) ** jj, (jj, 1, sp.oo)))

# ---------------------------------------------------------------- A8
tau = sp.symbols("tau", real=True)
pq = sp.symbols("p", positive=True)
# pure power weight: q = p, dot q = 0. Then dot G + (M+2-p) G = dot F - (M+p) F, so |G^|^2 = (tau^2+(M+p)^2)/(tau^2+(M+2-p)^2) |F^|^2,
# E_g = int (tau^2 + p^2 + (M+2)^2)|G^|^2, E_f = int (tau^2 + p^2 + M^2)|F^|^2 (Plancherel in t).
Ssym = (tau ** 2 + pq ** 2 + (M + 2) ** 2) * (tau ** 2 + (M + pq) ** 2) / ((tau ** 2 + (M + 2 - pq) ** 2) * (tau ** 2 + pq ** 2 + M ** 2))
AM = ((M + 2) ** 2 + pq ** 2) / (M + 2 - pq) ** 2
BM = (M + pq) ** 2 / (M ** 2 + pq ** 2)
print("A8 Mellin symbol at tau = 0 minus A_M(p) B_M(p) (q = p):", sp.simplify(Ssym.subs(tau, 0) - AM * BM))
u = sp.symbols("u", nonnegative=True)
fac1 = (u + pq ** 2 + (M + 2) ** 2) / (u + (M + 2 - pq) ** 2)
fac2 = (u + (M + pq) ** 2) / (u + pq ** 2 + M ** 2)
print("A8 d/du of the two factors (u = tau^2):", sp.factor(sp.diff(fac1, u)), ";", sp.factor(sp.diff(fac2, u)), " (both <= 0)")
Pf = lambda p_: (9 + p_ ** 2) * (1 + p_) ** 2 / ((3 - p_) ** 2 * (1 + p_ ** 2))
pg = np.linspace(0, 2.999, 3000)
print("A8 FLOAT: P(p) = A_1 B_1 at q = p is increasing on [0, 3):", bool(np.all(np.diff(Pf(pg)) > 0)),
      "; P(p)/(A(p)B(p)) at p = 1.5, 2, 2.5, 2.9:", [round(Pf(p_) / ((9 + p_ ** 2) / (3 - p_) ** 2 * 2), 6) for p_ in (1.5, 2.0, 2.5, 2.9)])
print("A8 constants. C3 = (3), C4 = (4), FS = 1/(1-|p|) (T4-177 full space applied to d_x h, d_y h; |p| < 1),"
      " LB = max(1, sqrt((1 + P(p))/8)) for p >= 0 and 1 for p < 0 (remark R2 lower bounds)")
for p_ in (-0.9, -0.5, -0.25, 0.0, 0.25, 0.5, 0.8, 1.0, 1.5, 2.0, 2.5, 2.9):
    if p_ >= 0:
        A_ = (9 + p_ ** 2) / (3 - p_) ** 2
        B_ = (1 + p_) ** 2 / (1 + p_ ** 2) if p_ <= 1 else 2.0
        c3 = (1 + np.sqrt((1 + A_ * B_) / 2)) / 2
        lb = max(1.0, np.sqrt((1 + Pf(p_)) / 8))
        c4 = float("nan")
    else:
        c3 = float("nan")
        lb = 1.0
        c4 = (1 + max(7.0, 1 + 4 / (1 + p_))) / 2
    fs = 1 / (1 - abs(p_)) if abs(p_) < 1 else float("inf")
    best = np.nanmin([c3, c4, fs])
    fmt = lambda v: f"{v:.6f}" if v == v else "  n/a   "
    print(f"A8 p = {p_:5.2f}: C3 = {fmt(c3)}  C4 = {fmt(c4)}  FS = {fs:.6f}  best upper = {best:.6f}  LB = {lb:.6f}  ratio = {best / lb:.4f}")
pfine = np.linspace(0.0, 2.99, 299001)
Af = (9 + pfine ** 2) / (3 - pfine) ** 2
Bf = np.where(pfine <= 1, (1 + pfine) ** 2 / (1 + pfine ** 2), 2.0)
C3f = (1 + np.sqrt((1 + Af * Bf) / 2)) / 2
LBf = np.maximum(1.0, np.sqrt((1 + Pf(pfine)) / 8))
ia = int(np.argmax(C3f / LBf))
print(f"A8 FLOAT grid p in [0, 2.99], step 1e-5: max C3/LB = {C3f[ia] / LBf[ia]:.6f} at p = {pfine[ia]:.5f}"
      f" (there P(p) = {Pf(pfine[ia]):.5f}, so the two lower bounds cross); C3/LB at p = 2.99: {C3f[-1] / LBf[-1]:.6f}")

# ---------------------------------------------------------------- B1
N, Lb = 2048, 40.0
dx = 2 * Lb / N
xs = (np.arange(N) - N // 2) * dx
X, Y = np.meshgrid(xs, xs, indexing="ij")
Rg = np.hypot(X, Y)
kk = 2 * np.pi * np.fft.fftfreq(N, dx)
K1, K2g = np.meshgrid(kk, kk, indexing="ij")
kq = K1 ** 2 + K2g ** 2
kq[0, 0] = 1.0
mBg = (K1 - 1j * K2g) ** 2 / kq
mBg[0, 0] = 0.0
del K1, K2g
sel = Rg <= 6.0
rtab = np.linspace(0, 6.0, 3001)


def g_radial(mval, r):
    M_ = abs(mval)
    fr = lambda s: s ** M_ * np.exp(-s * s)
    if r == 0:
        return 0.0
    if mval == 1:
        return fr(r)
    if mval >= 3:
        val, _ = quad(lambda s: s ** (1 - mval) * fr(s), r, np.inf, epsabs=0, epsrel=1e-12, limit=200)
        return fr(r) - 2 * (mval - 1) * r ** (mval - 2) * val
    val, _ = quad(lambda s: s ** (1 - mval) * fr(s), 0, r, epsabs=0, epsrel=1e-12, limit=200)
    return fr(r) + 2 * (mval - 1) * r ** (mval - 2) * val


for mval in (1, 3, 5, -1, -3):
    M_ = abs(mval)
    zz = (X + 1j * Y) if mval > 0 else (X - 1j * Y)
    h = zz ** M_ * np.exp(-Rg ** 2)
    Bh = np.fft.fftshift(np.fft.ifft2(mBg * np.fft.fft2(np.fft.ifftshift(h))))
    gt = np.array([g_radial(mval, r) for r in rtab])
    k_ = mval - 2
    ph = ((X + 1j * Y) / np.where(Rg > 0, Rg, 1.0)) if k_ >= 0 else ((X - 1j * Y) / np.where(Rg > 0, Rg, 1.0))
    pred = np.interp(Rg[sel], rtab, gt) * ph[sel] ** abs(k_)
    err = np.max(np.abs(Bh[sel] - pred))
    print(f"B1 m = {mval:2d}: max |FFT B h - g(r) e^(i(m-2)theta)| on r <= 6: {err:.3e}  (max |g| = {np.max(np.abs(gt)):.4f})")
    del h, Bh, ph, zz
bump = lambda r: np.where((r > 1) & (r < 2), np.exp(-1 / np.clip((r - 1) * (2 - r), 1e-300, None)), 0.0)
th_g = np.arctan2(Y, X)
hstar = bump(Rg) * np.sin(3 * th_g)
kk1, kk2 = np.meshgrid(kk, kk, indexing="ij")
symb = 1j * kk2 * (-kk1 ** 2 / kq)
symb[0, 0] = 0.0
dyU2 = np.fft.fftshift(np.fft.ifft2(symb * np.fft.fft2(np.fft.ifftshift(hstar))))
a_fft = dyU2[N // 2, N // 2].real
a_int, _ = quad(lambda r: float(bump(np.array(r))) / r ** 2, 1, 2, epsabs=0, epsrel=1e-12)
print(f"B1 a = d_y U2[h_*](0) for h_* = chi(r) sin(3 theta), chi = exp(-1/((r-1)(2-r))): FFT {a_fft:.10f}, int chi r^-2 dr = {a_int:.10f}")
del X, Y, Rg, mBg, kq, kk1, kk2, symb, dyU2, hstar, th_g

# ---------------------------------------------------------------- B2
dt = 0.001
tg = np.arange(-25.0, 160.0 + dt / 2, dt)


def bump1(z):
    out = np.zeros_like(z)
    inside = (z > -1) & (z < 1)
    out[inside] = np.exp(-1 / (1 - z[inside] ** 2))
    return out


def dbump1(z):
    out = np.zeros_like(z)
    inside = (z > -1) & (z < 1)
    zi = z[inside]
    out[inside] = np.exp(-1 / (1 - zi ** 2)) * (-2 * zi / (1 - zi ** 2) ** 2)
    return out


def profile(kind, mval):
    """Return f(t), dot f(t) on tg for a compact smooth h."""
    M_ = abs(mval)
    if kind == "origin":           # f(r) = r^M chi(r/2), chi(s) = bump1(s) (support r < 2): smooth h with 0 in its support
        r = np.exp(np.minimum(tg, 1.0))          # support is r < 2 (t < log 2); avoids overflow of r^M far out
        c = bump1(r / 2) * (tg < 1.0)
        dc = dbump1(r / 2) / 2 * (tg < 1.0)
        f = r ** M_ * c
        fd = M_ * f + r ** (M_ + 1) * dc
        return f, fd
    z = (tg - 0.3) / 0.8          # annular: bump in t on (-0.5, 1.1)
    return bump1(z), dbump1(z) / 0.8


def g_of(f, mval):
    if mval == 1:
        return f.copy()
    k_ = mval - 2
    if mval >= 3:                  # J(t) = int_t^inf e^{k(t-s)} f ds, backward recursion
        b = np.exp(-k_ * dt)
        fr = f[::-1]
        xin = np.empty_like(fr)
        xin[0] = 0.0
        xin[1:] = dt / 2 * (fr[1:] + b * fr[:-1])
        J = lfilter([1.0], [1.0, -b], xin)[::-1]
        return f - 2 * (mval - 1) * J
    a = np.exp(k_ * dt)            # I(t) = int_-inf^t e^{k(t-s)} f ds, forward recursion
    xin = np.empty_like(f)
    xin[0] = 0.0
    xin[1:] = dt / 2 * (a * f[:-1] + f[1:])
    Iv = lfilter([1.0], [1.0, -a], xin)
    return f + 2 * (mval - 1) * Iv


trap = lambda v: float(np.sum((v[1:] + v[:-1]) * dt / 2))
worst = {}
for p_ in (-0.9, -0.5, -0.1, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 2.9):
    logw = (p_ / 2) * np.logaddexp(0.0, 2 * tg)
    wv = np.exp(logw - p_ * 40.0)           # constant normalization; cancels in every ratio
    ex = 1 / (1 + np.exp(-2 * tg))
    qv = p_ * ex
    qd = 2 * p_ * ex * (1 - ex)
    if p_ >= 0:
        A_ = (9 + p_ ** 2) / (3 - p_) ** 2
        B_ = (1 + p_) ** 2 / (1 + p_ ** 2) if p_ <= 1 else 2.0
    for kind in ("origin", "annular"):
        for mval in (1, 3, 5, -1, -3, -5):
            f, fd = profile(kind, mval)
            g = g_of(f, mval)
            gd_ode = (mval - 2) * g + fd + mval * f          # from (5)
            gd_num = np.gradient(g, dt)
            res5 = np.max(np.abs(gd_num[2:-2] - gd_ode[2:-2])) / np.max(np.abs(gd_ode))
            Ef = trap((wv * fd) ** 2 + mval ** 2 * (wv * f) ** 2)
            Eg = trap((wv * gd_ode) ** 2 + (mval - 2) ** 2 * (wv * g) ** 2)
            rat = Eg / Ef
            if p_ >= 0:
                if mval >= 1:
                    res = (Eg - Ef + 2 * trap(qv * wv ** 2 * (mval * f ** 2 + (mval - 2) * g ** 2))) / Ef
                    bound = 1.0
                else:
                    Mm = -mval
                    Fv, Gv = wv * f, wv * g
                    Fd, Gd = qv * Fv + wv * fd, qv * Gv + wv * gd_ode
                    l8 = trap(Gd ** 2 + ((Mm + 2 - qv) ** 2 + qd) * Gv ** 2)
                    r8 = trap(Fd ** 2 + ((Mm + qv) ** 2 + qd) * Fv ** 2)
                    res = (l8 - r8) / r8
                    bound = A_ * B_
                lab = "(7)" if mval >= 1 else "(8)"
            else:
                res = float("nan")
                lab = "   "
                if mval == 1:
                    bound = 1.0
                elif mval >= 3:
                    bound = (1 + 4 / (1 + p_)) ** 2
                else:
                    bound = (3 + 4 / (-mval)) ** 2
            worst[(p_, kind, mval)] = rat / bound
            rs_ = f"{res: .1e}" if p_ >= 0 else "  n/a  "
            print(f"B2 p = {p_:4.1f} {kind:7s} m = {mval:2d}: (5) residual {res5:.1e}, identity {lab} rel. residual {rs_},"
                  f" E_g/E_f = {rat:.6f}, bound {bound:.6f}, ratio/bound = {rat / bound:.6f}")
print(f"B2 max over all rows of (E_g/E_f)/bound = {max(worst.values()):.8f} (must be <= 1 up to discretization; at p = 0 the bound E_g = E_f is attained)")

# ---------------------------------------------------------------- B3
for mval in (-1, -3):
    Mm = -mval
    for p_ in (0.5, 1.0, 1.5, 2.0, 2.5):
        target = ((Mm + 2) ** 2 + p_ ** 2) / (Mm + 2 - p_) ** 2 * (Mm + p_) ** 2 / (Mm ** 2 + p_ ** 2)
        out = []
        for K_ in (2.0, 8.0, 32.0):
            Tc = 30.0 + K_
            tail = 40.0 / (2 * Mm + 4 - 2 * p_) + 5.0
            dtl = 0.0025
            tl = np.arange(Tc - K_ - 1.0, Tc + K_ + tail, dtl)
            z = (tl - Tc) / K_
            inside = np.abs(z) < 1
            f = np.zeros_like(tl)
            fd = np.zeros_like(tl)
            bz = np.exp(-1 / (1 - z[inside] ** 2))
            dbz = bz * (-2 * z[inside] / (1 - z[inside] ** 2) ** 2) / K_
            ew = np.exp(-p_ * (tl[inside] - Tc))  # f = w^-1 times a slow bump, so that F = w f varies slowly
            f[inside] = ew * bz
            fd[inside] = ew * (dbz - p_ * bz)
            k_ = mval - 2
            a = np.exp(k_ * dtl)
            xin = np.empty_like(f)
            xin[0] = 0.0
            xin[1:] = dtl / 2 * (a * f[:-1] + f[1:])
            g = f + 2 * (mval - 1) * lfilter([1.0], [1.0, -a], xin)
            gd = (mval - 2) * g + fd + mval * f
            logw = (p_ / 2) * np.logaddexp(0.0, 2 * tl)
            wv = np.exp(logw - p_ * Tc)
            tr = lambda v: float(np.sum((v[1:] + v[:-1]) * dtl / 2))
            Ef = tr((wv * fd) ** 2 + Mm ** 2 * (wv * f) ** 2)
            Eg = tr((wv * gd) ** 2 + (Mm + 2) ** 2 * (wv * g) ** 2)
            out.append(Eg / Ef)
        AB = (9 + p_ ** 2) / (3 - p_) ** 2 * ((1 + p_) ** 2 / (1 + p_ ** 2) if p_ <= 1 else 2.0)
        print(f"B3 m = {mval}, p = {p_}: E_g/E_f for widths K = 2, 8, 32: {[round(v, 6) for v in out]};"
              f" frozen limit A_M B_M at q = p: {target:.6f}; proved bound A(p)B(p): {AB:.6f}")

print(f"EXIT 0 elapsed {time.time() - T0:.1f} s")
sys.exit(0)
