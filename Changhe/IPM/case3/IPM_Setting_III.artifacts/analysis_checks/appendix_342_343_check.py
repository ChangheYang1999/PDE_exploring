"""Checks for the proofs A.3.42 and A.3.43.

Exact (sympy) checks of the algebraic identities and numerical (mpmath / numpy) checks of
integrals and of one Fourier multiplier value.  These checks support, but do not replace,
the written proofs.  Run with OMP_NUM_THREADS=1.  Exit status is nonzero if any check fails.
"""
import math
import sys

import mpmath as mp
import numpy as np
import sympy as sp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


x, y = sp.symbols("x y", real=True)
r, th, s = sp.symbols("r theta s", real=True)
cl, a0, m = sp.symbols("c_l a0 m", positive=True)
R = sp.Rational
polar = {x: r * sp.cos(th), y: r * sp.sin(th)}

# ======================================================================= 3.42
# (1) 3.42(i): W . grad h - h + a0 v_2 = W . grad rho - rho on a manufactured example
b3, e3, f5, k5, q1, q2, q3 = sp.symbols("b3 e3 f5 k5 q1 q2 q3", real=True)
csym = sp.symbols("c", real=True)
rho = a0 * y + b3 * x**2 * y + e3 * y**3 + f5 * x**4 * y + k5 * y * sp.exp(-x**2 - y**2) * x**2
psi_c = csym * x * y + q1 * x**3 * y + q2 * x * y**3 + q3 * x * y * sp.cos(x * y) * x**2 * y**2


def check_identity(cval):
    psi = psi_c.subs(csym, cval)
    U = (-sp.diff(psi, y), sp.diff(psi, x))
    W = (cl * x + U[0], cl * y + U[1])
    h = rho - a0 * y
    phi = psi - cval * x * y
    v2 = sp.diff(phi, x)
    lhs = W[0] * sp.diff(h, x) + W[1] * sp.diff(h, y) - h + a0 * v2
    rhs = W[0] * sp.diff(rho, x) + W[1] * sp.diff(rho, y) - rho
    return sp.simplify(lhs - rhs), psi, phi, h


d1, psi1, phi1, h1 = check_identity(1 - cl)
report("3.42(i) W.grad h - h + a0 v2 = W.grad rho - rho (c = 1 - c_l)", d1 == 0)
d2, _, _, _ = check_identity(csym)
report("3.42(i) defect for general c is a0 y (1 - c_l - c)", sp.simplify(d2 - a0 * y * (1 - cl - csym)) == 0)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
report("3.42(i) -Lap phi - d_x h = -Lap psi - d_x rho",
       sp.simplify((-lap(phi1) - sp.diff(h1, x)) - (-lap(psi1) - sp.diff(rho, x))) == 0)
# parities of the manufactured pair and orders at 0
report("3.42 manufactured parities",
       sp.simplify(rho.subs(x, -x) - rho) == 0 and sp.simplify(rho.subs(y, -y) + rho) == 0
       and sp.simplify(psi1.subs(x, -x) + psi1) == 0 and sp.simplify(psi1.subs(y, -y) + psi1) == 0)

# (2) div(W r^{-2m}) and the pointwise form of the weighted identity, generic h, psi
H = sp.Function("H")(x, y)
P = sp.Function("P")(x, y)
U = (-sp.diff(P, y), sp.diff(P, x))
W = (cl * x + U[0], cl * y + U[1])
w = (x**2 + y**2) ** (-m)
divwW = sp.diff(w * W[0], x) + sp.diff(w * W[1], y)
XU = x * U[0] + y * U[1]
target = 2 * (1 - m) * cl * w - 2 * m * XU / (x**2 + y**2) * w
report("3.42(ii) div(w W) = 2(1-m) c_l w - 2m (X.U/r^2) w", sp.simplify(divwW - target) == 0)
lhs = H * w * (W[0] * sp.diff(H, x) + W[1] * sp.diff(H, y) - H)
flux = (sp.diff(H**2 * w * W[0], x) + sp.diff(H**2 * w * W[1], y)) / 2
rhs = flux + ((m - 1) * cl - 1) * H**2 * w + m * XU / (x**2 + y**2) * H**2 * w
report("3.42(ii) h w (W.grad h - h) = div(h^2 w W)/2 + ((m-1)c_l-1) h^2 w + m (X.U/r^2) h^2 w",
       sp.simplify(sp.expand(lhs - rhs)) == 0)

# (2b) integrated identity on a manufactured non-profile (adds int R h w), m = 3 and m = 2.6
mp.mp.dps = 20
cl_n, a0_n = mp.mpf("1.4"), mp.mpf("0.7")
c_n = 1 - cl_n
xs, ys = sp.symbols("xs ys", real=True)
rho_m = a0_n * ys * sp.exp(-(xs**2 + ys**2))
psi_m = c_n * xs * ys / sp.sqrt(1 + xs**2 + ys**2)
Um = (-sp.diff(psi_m, ys), sp.diff(psi_m, xs))
Wm = (cl_n * xs + Um[0], cl_n * ys + Um[1])
hm = rho_m - a0_n * ys
v2m = sp.diff(psi_m - c_n * xs * ys, xs)
Rm = Wm[0] * sp.diff(rho_m, xs) + Wm[1] * sp.diff(rho_m, ys) - rho_m
XUm = xs * Um[0] + ys * Um[1]
fh2 = sp.lambdify((xs, ys), hm**2, "mpmath")
fxu = sp.lambdify((xs, ys), XUm / (xs**2 + ys**2) * hm**2, "mpmath")
fvh = sp.lambdify((xs, ys), v2m * hm, "mpmath")
fRh = sp.lambdify((xs, ys), Rm * hm, "mpmath")


def wint(f, mm):
    g = lambda rr, tt: f(rr * mp.cos(tt), rr * mp.sin(tt)) * rr ** (1 - 2 * mm)
    # integrand is even under th -> -th and th -> pi - th: integrate over the quadrant
    return 4 * mp.quad(g, [0, 1, 3, 8, mp.inf], [0, mp.pi / 2])


for mm in (mp.mpf(3), mp.mpf("2.6")):
    L = ((mm - 1) * cl_n - 1) * wint(fh2, mm) + mm * wint(fxu, mm) + a0_n * wint(fvh, mm)
    Rr = wint(fRh, mm)
    report("3.42(ii) integrated identity (non-profile, + int R h w), m = %s" % mp.nstr(mm, 3),
           abs(L - Rr) < 1e-10 * (1 + abs(Rr)), "lhs %s rhs %s" % (mp.nstr(L, 14), mp.nstr(Rr, 14)))

# (3) Mellin form of the Poisson equation and the norm identity (explicit test functions)
Gt = sp.exp(-s**2) * (sp.sin(2 * th) + s * sp.sin(4 * th) + s**2 * sp.sin(6 * th))
Ft = sp.exp(-(s - 1) ** 2) * (sp.sin(th) + s**2 * sp.sin(3 * th) + s * sp.sin(5 * th))
phit = (r**m * Gt).subs(s, sp.log(r))
ht = (r ** (m - 1) * Ft).subs(s, sp.log(r))
lap_p = sp.diff(phit, r, 2) + sp.diff(phit, r) / r + sp.diff(phit, th, 2) / r**2
dxh = sp.cos(th) * sp.diff(ht, r) - sp.sin(th) / r * sp.diff(ht, th)
Ds = lambda f: sp.diff(f, s) + m * f
lhsG = (-(Ds(Ds(Gt)) + sp.diff(Gt, th, 2))).subs(s, sp.log(r))
rhsF = (Ds(sp.cos(th) * Ft) + sp.diff(-sp.sin(th) * Ft, th)).subs(s, sp.log(r))
ok1 = sp.simplify(sp.expand(r ** (2 - m) * (-lap_p) - lhsG)) == 0
ok2 = sp.simplify(sp.expand(r ** (2 - m) * dxh - rhsF)) == 0
report("3.42(iii) r^{2-m}(-Lap phi) = -((d_s+m)^2 + d_th^2) G", ok1)
report("3.42(iii) r^{2-m} d_x h = (d_s+m)(cos th F) + d_th(-sin th F)", ok2)
gradsq = sp.diff(phit, r) ** 2 + (sp.diff(phit, th) / r) ** 2
normG = (Ds(Gt) ** 2 + sp.diff(Gt, th) ** 2).subs(s, sp.log(r))
report("3.42(iii) |grad phi|^2 r^{2-2m} = |(d_s+m)G|^2 + |G_th|^2",
       sp.simplify(sp.expand(gradsq * r ** (2 - 2 * m) - normG)) == 0)
# pi-periodicity of H = (cos th F, -sin th F) for odd sine modes, and even modes of phi
okper = True
for j in range(1, 7):
    f = sp.sin((2 * j - 1) * th)
    for comp in (sp.cos(th) * f, sp.sin(th) * f):
        okper &= sp.simplify(sp.expand_trig(comp.subs(th, th + sp.pi) - comp)) == 0
    g = sp.sin(2 * j * th)
    okper &= sp.simplify(g.subs(th, sp.pi - th) + g) == 0 and sp.simplify(g.subs(th, -th) + g) == 0
report("3.42(iii) H pi-periodic; sin(2j th) odd in x and y", okper)

# symbol: rank-one norm, identity for M^2, monotonicity, maximization, N_3, N_sqrt8
xi, t, n = sp.symbols("xi t n", real=True)
Msq = (t + m**2 + n**2) ** 2 / ((t + (n - m) ** 2) * (t + (n + m) ** 2))
report("3.42(iii) M^2 = 1 + 4 m^2 n^2/((t+(n-m)^2)(t+(n+m)^2))",
       sp.simplify(Msq - 1 - 4 * m**2 * n**2 / ((t + (n - m) ** 2) * (t + (n + m) ** 2))) == 0)
dM = sp.simplify(sp.diff(1 + 4 * m**2 * n**2 / ((t + (n - m) ** 2) * (t + (n + m) ** 2)), t))
dM_expected = -4 * m**2 * n**2 * (2 * t + (n - m) ** 2 + (n + m) ** 2) / (
    (t + (n - m) ** 2) ** 2 * (t + (n + m) ** 2) ** 2)
report("3.42(iii) d(M^2)/dt = -4m^2n^2(2t+(n-m)^2+(n+m)^2)/(...)^2 <= 0", sp.simplify(dM - dM_expected) == 0)
zz = m + sp.I * xi
report("3.42(iii) |n^2 - z^2|^2 = (xi^2+(n-m)^2)(xi^2+(n+m)^2)",
       sp.simplify(sp.expand((n**2 - zz**2) * sp.conjugate(n**2 - zz**2)) -
                   sp.expand((xi**2 + (n - m) ** 2) * (xi**2 + (n + m) ** 2))) == 0)
rng = np.random.default_rng(7)
okrank = True
for _ in range(2000):
    mm = rng.uniform(2.01, 3.99)
    xv = rng.normal() * 3
    nv = 2 * rng.integers(-6, 7)
    z = mm + 1j * xv
    a = np.array([z, 1j * nv])
    Mat = np.outer(a, a) / (nv**2 - z**2)
    sv = np.linalg.svd(Mat, compute_uv=False)[0]
    Mf = (xv**2 + mm**2 + nv**2) / math.sqrt((xv**2 + (nv - mm) ** 2) * (xv**2 + (nv + mm) ** 2))
    okrank &= abs(sv - Mf) < 1e-10 * Mf
report("3.42(iii) operator norm of a a^T/(n^2 - z^2) equals M_{m,n}(xi) (2000 random cases)", okrank)


def Mfun(mm, xv, nv):
    return (xv**2 + mm**2 + nv**2) / np.sqrt((xv**2 + (nv - mm) ** 2) * (xv**2 + (nv + mm) ** 2))


def Nm(mm):
    return max((mm**2 + 4) / (mm**2 - 4), (mm**2 + 16) / (16 - mm**2))


okmax = True
ns = np.arange(-400, 401, 2)
xis = np.concatenate([np.linspace(0, 5, 501), np.linspace(5, 200, 400)])
for mm in np.linspace(2.02, 3.98, 99):
    best = max(Mfun(mm, 0.0, nv) for nv in ns)
    okmax &= abs(best - Nm(mm)) < 1e-12 * Nm(mm)
    for nv in (0, 2, 4, 6, 8, 20):
        vals = Mfun(mm, xis, nv)
        okmax &= bool(np.all(np.diff(vals) <= 1e-13)) and vals.max() <= Nm(mm) * (1 + 1e-13)
report("3.42(iii) sup over xi and even n equals N_m, decreasing in xi (grid)", okmax)
N = lambda mm: sp.Max((mm**2 + 4) / (mm**2 - 4), (mm**2 + 16) / (16 - mm**2))
report("3.42(iii) N_3 = 25/7 and N_sqrt8 = 3", N(sp.Integer(3)) == R(25, 7) and sp.simplify(N(sp.sqrt(8)) - 3) == 0,
       "candidates at 3: 13/5, 25/7")

# (iv), (v)
s1, s2, w1 = sp.symbols("s1 s2 w1", real=True)
DU = sp.Matrix([[s1, s2 - w1], [s2 + w1, -s1]])
S = (DU + DU.T) / 2
ev = list(S.eigenvals().keys())
froS = sum(e**2 for e in S)
froDU = sum(e**2 for e in DU)
report("3.42(iv) trace-free S: |S|_op^2 = |S|_F^2/2 and |DU|_F^2 = |S|_F^2 + 2 w1^2",
       all(sp.simplify(e**2 - froS / 2) == 0 for e in ev) and sp.simplify(froDU - froS - 2 * w1**2) == 0)
report("3.42(iv) 3/sqrt 2 < 25/7", 3 / sp.sqrt(2) < R(25, 7))
Ds_ = sp.symbols("D", positive=True)
ineq = sp.simplify((2 * (1 + Ds_) - 1) - 3 * Ds_ - (2 - (1 + Ds_)))
report("3.42(v) 2c_l - 1 - 3(c_l - 1) = 2 - c_l", ineq == 0)

# ======================================================================= 3.43
k = sp.sin(th) ** 2 * (4 * sp.sin(th) ** 2 - 3)
# (5) kernel facts
okk = sp.simplify(sp.integrate(k, (th, 0, sp.pi / 2))) == 0
pos = sp.simplify(sp.integrate(k, (th, sp.pi / 3, sp.pi / 2)))
absk = sp.simplify(sp.integrate(-k, (th, 0, sp.pi / 3)) + pos)
report("3.43 kernel: int_0^{pi/2} k = 0", okk)
report("3.43 kernel: positive mass 3 sqrt3/16, |k| mass 3 sqrt3/8",
       sp.simplify(pos - 3 * sp.sqrt(3) / 16) == 0 and sp.simplify(absk - 3 * sp.sqrt(3) / 8) == 0)
report("3.43 kernel: k(pi/3) = 0, k < 0 on (0, pi/3), k > 0 on (pi/3, pi/2)",
       sp.simplify(k.subs(th, sp.pi / 3)) == 0
       and all(float(k.subs(th, v)) < 0 for v in np.linspace(0.01, math.pi / 3 - 0.01, 50))
       and all(float(k.subs(th, v)) > 0 for v in np.linspace(math.pi / 3 + 0.01, math.pi / 2, 50)))
report("3.43 kernel: k = -(cos sin^3)' = (cos 4th - cos 2th)/2 = -sin th sin 3th",
       sp.simplify(k + sp.diff(sp.cos(th) * sp.sin(th) ** 3, th)) == 0
       and sp.simplify(sp.expand_trig(k - (sp.cos(4 * th) - sp.cos(2 * th)) / 2)) == 0
       and sp.simplify(sp.expand_trig(k + sp.sin(th) * sp.sin(3 * th))) == 0)
report("3.43 int_0^{pi/2} cos^2 sin^2 = pi/16",
       sp.simplify(sp.integrate(sp.cos(th) ** 2 * sp.sin(th) ** 2, (th, 0, sp.pi / 2)) - sp.pi / 16) == 0)
# lemma |int k g| <= (3 sqrt3/16) osc g on random trigonometric g
tg = np.linspace(0, math.pi / 2, 20001)
kk = np.sin(tg) ** 2 * (4 * np.sin(tg) ** 2 - 3)
wts = np.full(tg.size, tg[1] - tg[0])
wts[0] = wts[-1] = (tg[1] - tg[0]) / 2
oklem = True
worst = 0.0
for _ in range(500):
    coef = rng.normal(size=6)
    gv = sum(coef[j] * np.cos(2 * j * tg) for j in range(6))
    val = abs(np.sum(wts * kk * gv))
    bound = 3 * math.sqrt(3) / 16 * (gv.max() - gv.min())
    worst = max(worst, val / bound)
    oklem &= val < bound
# near-extremal step function shows the constant is approached
step = 0.5 * (1 + np.tanh((tg - math.pi / 3) * 1000))
ratio_step = np.sum(wts * kk * step) / (3 * math.sqrt(3) / 16)
report("3.43(ii) lemma |int k g| < (3 sqrt3/16) osc g (500 random g), smooth step ratio -> 1",
       oklem and abs(ratio_step - 1) < 2e-3, "max ratio random %.4f, step %.6f" % (worst, ratio_step))

# (4) 3.43(i) on a manufactured q: q_x form of the strain identity versus the angular-contrast form
mp.mp.dps = 15
e1, e2 = R(3, 10), R(1, 2)
qexpr = (1 + x**2 + y**2) ** R(-1, 4) + e1 * (x**2 - y**2) / (1 + x**2 + y**2) ** 2 \
    + e2 * (x**4 - 6 * x**2 * y**2 + y**4) / (1 + x**2 + y**2) ** 3
qf = sp.lambdify((x, y), qexpr, "mpmath")
qxf = sp.lambdify((x, y), sp.diff(qexpr, x), "mpmath")
qyf = sp.lambdify((x, y), sp.diff(qexpr, y), "mpmath")
pts = [0, mp.mpf(1) / 4, mp.mpf(1) / 2, 1, 2, 4, 8, 16, 40, 100, 1000, mp.inf]
lhs_qx = -4 / mp.pi * mp.quad(lambda rr, tt: mp.cos(tt) * mp.sin(tt) ** 2 * qxf(rr * mp.cos(tt), rr * mp.sin(tt)),
                              pts, [0, mp.pi / 2])
Tq = -4 / mp.pi * mp.quad(lambda rr, tt: mp.sin(tt) ** 3 * qyf(rr * mp.cos(tt), rr * mp.sin(tt)), pts, [0, mp.pi / 2])
kf = lambda tt: mp.sin(tt) ** 2 * (4 * mp.sin(tt) ** 2 - 3)


def inner(rr):
    return mp.quad(lambda tt: kf(tt) * qf(rr * mp.cos(tt), rr * mp.sin(tt)), [0, mp.pi / 3, mp.pi / 2])


rhs_k = mp.mpf(1) / 4 + 4 / mp.pi * mp.quad(lambda rr: inner(rr) / rr, pts)
closed = mp.mpf(1) / 4 + mp.mpf(e2) / 8 - mp.mpf(e1) / 4
report("3.43(i) -(4/pi) int_Q x y^2 r^-4 q_x = 1/4 + (4/pi) int [int k q dth] dr/r",
       abs(lhs_qx - rhs_k) < 1e-10 and abs(rhs_k - closed) < 1e-10,
       "q_x form %s, contrast form %s, closed %s" % (mp.nstr(lhs_qx, 13), mp.nstr(rhs_k, 13), mp.nstr(closed, 13)))
report("3.43 (3.24(ii)) S + T = 1 on the manufactured q", abs(lhs_qx + Tq - 1) < 1e-9,
       "S + T - 1 = %s" % mp.nstr(lhs_qx + Tq - 1, 3))
# inner integral O(r^2) at 0
i_small = [abs(inner(mp.mpf(10) ** (-j))) * mp.mpf(10) ** (2 * j) for j in (2, 3, 4)]
report("3.43(i) inner integral O(r^2) at 0", max(i_small) < 1, "r^-2 |I(r)| at r = 1e-2..1e-4: %s"
       % ", ".join(mp.nstr(v, 5) for v in i_small))
# rho_3 route: c = -a0/4 + int rho_3 s^-2 (a0 = 1 normalisation), D = -c
rho3 = lambda rr: 4 / mp.pi * mp.quad(lambda tt: rr * mp.sin(tt) * qf(rr * mp.cos(tt), rr * mp.sin(tt))
                                       * mp.sin(3 * tt), [0, mp.pi / 2])
cval = -mp.mpf(1) / 4 + mp.quad(lambda rr: rho3(rr) / rr**2, pts)
report("3.43(i) agrees with 3.2: D/a0 = -c/a0", abs(-cval - rhs_k) < 1e-10, "-c = %s" % mp.nstr(-cval, 13))
# A(q) and the bound of (ii)
tq = np.linspace(0, math.pi / 2, 1001)
qnp = sp.lambdify((x, y), qexpr, "numpy")


def A_of(lam):
    # A(q(./lam)) = int osc_th q(r/lam, th) dr/r, computed in u = log r on a uniform grid
    u = np.linspace(-20, 20, 4001)
    rr_ = np.exp(u)[:, None] / lam
    vals = qnp(rr_ * np.cos(tq)[None, :], rr_ * np.sin(tq)[None, :])
    oscv = vals.max(axis=1) - vals.min(axis=1)
    return float(np.sum((oscv[1:] + oscv[:-1]) / 2) * (u[1] - u[0]))


Aq = A_of(1.0)
report("3.43(ii) |D/a0 - 1/4| < (3 sqrt3/(4 pi)) A(q) on the manufactured q",
       abs(rhs_k - mp.mpf(1) / 4) < 3 * mp.sqrt(3) / (4 * mp.pi) * Aq,
       "|D/a0 - 1/4| = %s, bound %s" % (mp.nstr(abs(rhs_k - 0.25), 6), mp.nstr(3 * mp.sqrt(3) / (4 * mp.pi) * Aq, 6)))
Aq_l = A_of(3.7)
report("3.43(ii) A(q(./l)) = A(q) (l = 3.7)", abs(Aq_l - Aq) < 1e-6 * Aq, "A = %.10f, A_l = %.10f" % (Aq, Aq_l))
# algebra of the consequences
zs, Dd, aa = sp.symbols("z D a", positive=True)
okc = sp.simplify(3 * sp.sqrt(3) / (4 * sp.pi) * (sp.pi * zs / (3 * sp.sqrt(3))) - zs / 4) == 0
okc &= sp.simplify((sp.Rational(1, 4) - Dd / (-aa)) - (1 + 4 * Dd / aa) / 4) == 0  # a0 = -a < 0
okc &= sp.simplify((Dd / aa - sp.Rational(1, 4)) - (4 * Dd / aa - 1) / 4) == 0
report("3.43(ii) rearrangements (z/4 form, a0 < 0, 0 < a0 <= 2D)", okc)

# (6) 3.43(iii): Tg(2,1)
E = sp.exp(-(x**2 + y**2))
Fr = -(1 - sp.exp(-r**2)) / (2 * r)
report("3.43(iii) F' = -(1 - e^{-r^2})/(2r) solves -(r F')'/r = e^{-r^2}",
       sp.simplify(-sp.diff(r * Fr, r) / r - sp.exp(-r**2)) == 0)
Fpp = sp.diff(Fr, r)
TG_from_F = -(Fpp * x**2 / (x**2 + y**2) + Fr * y**2 / (x**2 + y**2) ** sp.Rational(3, 2))
TG_from_F = TG_from_F.subs(r, sp.sqrt(x**2 + y**2))
TG = E * x**2 / (x**2 + y**2) + (1 - E) * (y**2 - x**2) / (2 * (x**2 + y**2) ** 2)
report("3.43(iii) TG = -d_x^2 F = e^{-r^2} x^2/r^2 + (1 - e^{-r^2})(y^2 - x^2)/(2 r^4)",
       sp.simplify(TG_from_F - TG) == 0)
report("3.43(iii) g = y e^{-r^2} = -(1/2) d_y e^{-r^2}", sp.simplify(-sp.diff(E, y) / 2 - y * E) == 0)
Tg = -sp.diff(TG, y) / 2
Tg21 = sp.simplify(Tg.subs({x: 2, y: 1}))
exact = -R(11, 250) + R(133, 125) * sp.exp(-5)
report("3.43(iii) Tg(2,1) = -11/250 + (133/125) e^{-5}", sp.simplify(Tg21 - exact) == 0, "value %.12f" % float(exact))
taylor = 1 + 5 + R(25, 2) + R(125, 6)
report("3.43(iii) e^5 > 1 + 5 + 25/2 + 125/6 = 118/3 > 266/11 (37/2 alone is not enough), so Tg(2,1) < 0",
       taylor == R(118, 3) and taylor > R(266, 11) and sp.simplify(R(133, 125) / R(11, 250) - R(266, 11)) == 0
       and R(37, 2) < R(266, 11))
# direct numerical Fourier evaluation: hat g = -(i pi/2) xi_2 e^{-|xi|^2/4}
nr, na = 400, 720
gl_x, gl_w = np.polynomial.legendre.leggauss(nr)
L = 30.0
rr_ = (gl_x + 1) * L / 2
wr_ = gl_w * L / 2
aa_ = np.arange(na) * 2 * math.pi / na
RR, AA = np.meshgrid(rr_, aa_, indexing="ij")
WW = np.outer(wr_, np.full(na, 2 * math.pi / na))


def fourier_T(X0, Y0, which):
    b = RR * (X0 * np.cos(AA) + Y0 * np.sin(AA))
    if which == "g":
        integrand = np.cos(AA) ** 2 * np.sin(AA) * RR**2 * np.exp(-RR**2 / 4) * np.sin(b)
        return np.sum(WW * integrand) / (8 * math.pi)
    integrand = np.cos(AA) ** 2 * np.exp(-RR**2 / 4) * np.cos(b) * RR
    return np.sum(WW * integrand) / (4 * math.pi)


num_g = fourier_T(2.0, 1.0, "g")
num_G = fourier_T(2.0, 1.0, "G")
TG21 = float(TG.subs({x: 2, y: 1}))
report("3.43(iii) Fourier quadrature of the multiplier reproduces Tg(2,1) and TG(2,1)",
       abs(num_g - float(exact)) < 1e-11 and abs(num_G - TG21) < 1e-11,
       "Tg: quad %.14f exact %.14f; TG: quad %.14f exact %.14f" % (num_g, float(exact), num_G, TG21))
num_g2 = fourier_T(0.3, -1.7, "g")
report("3.43(iii) same at (0.3, -1.7)", abs(num_g2 - float(Tg.subs({x: 0.3, y: -1.7}))) < 1e-11)
# radial-bump identity int G TG = (1/2)||G||^2 = pi/4 (used in (iv)), from the closed form
TGp = sp.lambdify((r, th), sp.simplify(TG.subs(polar)), "mpmath")
mp.mp.dps = 15
iGTG = mp.quad(lambda rr, tt: mp.exp(-rr**2) * TGp(rr, tt) * rr, [0, 1, 3, 8], [0, 2 * mp.pi])
report("3.43(iv) radial identity int G T G = ||G||^2/2 = pi/4", abs(iGTG - mp.pi / 4) < 1e-10, mp.nstr(iGTG, 14))
# explicit positive even-even weight with int w g Tg < 0
Tgn = sp.lambdify((x, y), Tg, "numpy")


def bump(Z2):
    out = np.zeros_like(Z2)
    msk = Z2 < 1
    out[msk] = np.exp(-1 / (1 - Z2[msk]))
    return out


gx, gw = np.polynomial.legendre.leggauss(200)
rad = 0.4
U1 = 2 + rad * gx
V1 = 1 + rad * gx
UU, VV = np.meshgrid(U1, V1, indexing="ij")
Wb = np.outer(gw * rad, gw * rad)
Z2 = ((UU - 2) ** 2 + (VV - 1) ** 2) / rad**2
I0 = 4 * np.sum(Wb * bump(Z2) * VV * np.exp(-(UU**2 + VV**2)) * Tgn(UU, VV))
X1 = 6 * gx
XX, YY = np.meshgrid(X1, X1, indexing="ij")
Wf = np.outer(gw * 6, gw * 6)
I1 = np.sum(Wf * np.exp(-(XX**2 + YY**2)) * YY * np.exp(-(XX**2 + YY**2)) * Tgn(XX, YY))
eta_w = 0.5 * abs(I0) / max(abs(I1), 1e-300)
report("3.43(iii) w = w0 + eta e^{-r^2}: int w g Tg < 0 with int g Tg e^{-r^2} finite",
       I0 < 0 and I0 + min(eta_w, 1.0) * I1 < 0,
       "int w0 g Tg = %.6e, int e^{-r^2} g Tg = %.6e, eta = %.3g" % (I0, I1, min(eta_w, 1.0)))
# unweighted positivity int g Tg >= 0
I2 = np.sum(Wf * YY * np.exp(-(XX**2 + YY**2)) * Tgn(XX, YY))
report("3.43(iii) unweighted int g Tg > 0 (equals (2pi)^-2 int xi1^2/|xi|^2 |hat g|^2 = pi/32)",
       I2 > 0 and abs(I2 - math.pi / 32) < 1e-8, "%.12f vs pi/32 = %.12f" % (I2, math.pi / 32))

# (7) 3.43(iv): second far-field coefficient
p = sp.symbols("p", positive=True)
Th0 = a0 * sp.sin(th)
Cc = sp.symbols("Cc")
Phi = Cc * sp.sin(2 * th)
eq = sp.simplify(-sp.diff(Phi, th, 2) - (p + 1) ** 2 * Phi - (p * sp.cos(th) * Th0 - sp.sin(th) * sp.diff(Th0, th)))
Csol = sp.solve(sp.expand_trig(eq).subs(th, sp.pi / 4), Cc)[0]
Phi0 = Phi.subs(Cc, Csol)
okPhi = sp.simplify(-sp.diff(Phi0, th, 2) - (p + 1) ** 2 * Phi0 - (p * sp.cos(th) * Th0 - sp.sin(th) * sp.diff(Th0, th))) == 0
okPhi &= sp.simplify(Csol + a0 / (2 * (p + 3))) == 0
u0r = -sp.diff(Phi0, th)
u0t = (p + 1) * Phi0
Dp = 1 / p - 1
Th1 = (p * u0r * Th0 + u0t * sp.diff(Th0, th)) / Dp
Th1_claim = -a0**2 * sp.sin(th) * (sp.cos(th) ** 2 + p * sp.sin(th) ** 2) / (Dp * (p + 3))
report("3.43(iv) Phi0 = -a0 sin 2th/(2(p+3)) solves the 3.32 equation", okPhi)
report("3.43(iv) u0r = a0 cos 2th/(p+3), u0th = -a0 (p+1) sin th cos th/(p+3)",
       sp.simplify(u0r - a0 * sp.cos(2 * th) / (p + 3)) == 0
       and sp.simplify(u0t + a0 * (p + 1) * sp.sin(th) * sp.cos(th) / (p + 3)) == 0)
report("3.43(iv) Theta1 = -a0^2 sin th (cos^2 + p sin^2)/(D(p+3))", sp.simplify(sp.expand_trig(Th1 - Th1_claim)) == 0)
report("3.43(iv) required Theta1(pi/2) = -a0^2 p/(D(p+3)) != 0 (0 < p < 1)",
       sp.simplify(Th1.subs(th, sp.pi / 2) + a0**2 * p / (Dp * (p + 3))) == 0)
# the stream r^{p+1} Phi0 inverts d_x(r^p Theta0) (Cartesian check at p = 7/10)
pv = R(7, 10)
rr = sp.sqrt(x**2 + y**2)
psi0 = (rr ** (pv + 1) * 2 * x * y / rr**2) * Csol.subs(p, pv)  # r^{p+1} sin 2th times coefficient
rho0 = a0 * rr ** pv * y / rr
chk = sp.simplify(-lap(psi0) - sp.diff(rho0, x))
report("3.43(iv) -Lap(r^{p+1} Phi0) = d_x(r^p Theta0) (p = 7/10)", chk == 0)
# a0 y F_p has no r^{2p-1} term: r F_p - r^p = ((p-1)/2) r^{p-2} + ..., and b_p ~ r^{p-1}/(p+3)
mp.mp.dps = 30
okt = True
for pv_ in (mp.mpf("0.55"), mp.mpf("0.8"), mp.mpf("0.95")):
    for R0 in (mp.mpf(10) ** 4, mp.mpf(10) ** 6):
        Fp = (1 + R0**2) ** ((pv_ - 1) / 2)
        okt &= abs((R0 * Fp - R0**pv_) / R0 ** (pv_ - 2) - (pv_ - 1) / 2) < 10 / R0**2
    R0 = mp.mpf(10) ** 8
    bpR = mp.quad(lambda tt: tt**3 * (1 + (R0 * tt) ** 2) ** ((pv_ - 1) / 2), [0, 1 / R0, 1])
    okt &= abs(bpR * R0 ** (1 - pv_) * (pv_ + 3) - 1) < 1e-6
report("3.43(iv) r F_p - r^p = ((p-1)/2) r^{p-2} + o (no r^{2p-1} term) and b_p r^{1-p} -> 1/(p+3)", okt)

# (8) further identities used in 3.43(iv)
S_, B_, J_ = sp.symbols("S B J", real=True)
Dv, av = sp.symbols("Dv av", real=True)
lhs34 = -Dv * sp.pi * av * J_ + av**2 * B_
rhs34 = -av * sp.pi * Dv / 2
sol = sp.solve(sp.Eq(lhs34.subs({J_: R(1, 4) - S_, Dv: av * S_}), rhs34.subs(Dv, av * S_)), B_)
report("3.43(iv) 3.4 with c = -D, D = a0 S, J = 1/4 - S  <=>  B = -pi S (S + 1/4)",
       len(sol) == 1 and sp.simplify(sol[0] + sp.pi * S_ * (S_ + R(1, 4))) == 0)
phi3 = sp.sin(3 * th) / r**3
phi3c = (3 * x**2 * y - y**3) / (x**2 + y**2) ** 3
report("3.43(iv) phi = (3x^2y - y^3)/r^6 harmonic, d_y phi = 3 r^-4 cos 4th",
       sp.simplify(lap(phi3c)) == 0
       and sp.simplify(sp.expand_trig(sp.simplify(sp.diff(phi3c, y).subs(polar)) - 3 * sp.cos(4 * th) / r**4)) == 0)
hx = sp.symbols("h_g", real=True)
e312 = (y * (hx * x * sp.diff(phi3c, x) - hx * y * sp.diff(phi3c, y))).subs(polar)
report("3.43(iv) y (h x, -h y) . grad phi = -3 h r^-2 sin th sin 5th",
       sp.simplify(sp.expand_trig(sp.simplify(e312) + 3 * hx * sp.sin(th) * sp.sin(5 * th) / r**2)) == 0)
report("3.43(iv) angular integrals int sin th sin 5th = 0, int sin th sin 2th cos 3th = -pi/2",
       sp.integrate(sp.sin(th) * sp.sin(5 * th), (th, 0, 2 * sp.pi)) == 0
       and sp.simplify(sp.integrate(sp.sin(th) * sp.sin(2 * th) * sp.cos(3 * th), (th, 0, 2 * sp.pi)) + sp.pi / 2) == 0)
angs = {"pi/12": math.pi / 12, "pi/4": math.pi / 4, "5pi/12": 5 * math.pi / 12, "17pi/48": 17 * math.pi / 48}
sg = {kk_: (math.sin(3 * v), math.cos(4 * v)) for kk_, v in angs.items()}
oktab = sg["pi/12"][0] > 0 and sg["pi/12"][1] > 0 and sg["pi/4"][0] > 0 and sg["pi/4"][1] < 0
oktab &= sg["5pi/12"][0] < 0 and sg["5pi/12"][1] > 0 and sg["17pi/48"][0] < 0 and sg["17pi/48"][1] < 0
report("3.43(iv) bump angles: signs of sin 3th (for J) and cos 4th (for B)", oktab,
       "; ".join("%s: %.4f, %.4f" % (kk_, a_, b_) for kk_, (a_, b_) in sg.items()))
rho_ = sp.symbols("rho_", positive=True)
c32 = sp.simplify(2 * sp.pi * sp.integrate(rho_**2 / (1 + rho_**2) ** 3, (rho_, 0, sp.oo)) / (4 * sp.pi**2))
report("3.43(iv) (2pi)^-2 int |xi| (1+|xi|^2)^-3 dxi = 1/32", c32 == R(1, 32))
# radial reference: with F = r b' + 4 b (equivalently r^4 b = int_0^r s^3 F), -Lap(-x y b) = d_x(y F)
bF = sp.Function("b")
Fdef = r * sp.diff(bF(r), r) + 4 * bF(r)
psi_pol = -r**2 * sp.sin(th) * sp.cos(th) * bF(r)
lap_pol = lambda f: sp.diff(f, r, 2) + sp.diff(f, r) / r + sp.diff(f, th, 2) / r**2
rho_pol = r * sp.sin(th) * Fdef
dx_pol = sp.cos(th) * sp.diff(rho_pol, r) - sp.sin(th) / r * sp.diff(rho_pol, th)
ok_ell = sp.simplify(sp.expand(-lap_pol(psi_pol) - dx_pol)) == 0
report("3.43(iv) radial reference: -Lap(-x y b) = d_x(y (r b' + 4 b)) (polar, generic b)", ok_ell)
mp.mp.dps = 20
okb = True
for pv_ in (mp.mpf("0.6"), mp.mpf("0.9")):
    Fn = lambda q, pv_=pv_: (1 + q * q) ** ((pv_ - 1) / 2)
    bn = lambda q, pv_=pv_: mp.quad(lambda tt: tt**3 * Fn(q * tt), [0, 1])
    for q0 in (mp.mpf("0.3"), mp.mpf("2.5"), mp.mpf(40)):
        okb &= abs(q0 * mp.diff(bn, q0) - (Fn(q0) - 4 * bn(q0))) < 1e-12
    okb &= abs(bn(0) - mp.mpf(1) / 4) < 1e-15
report("3.43(iv) b_p = int_0^1 t^3 F_p(rt) dt satisfies r b_p' = F_p - 4 b_p, b_p(0) = 1/4", okb)

# B(v_p) = (3pi/4) int F_p b_p' dr (circular truncation) and |DV_p|_F <= 2, p in [1/2, 1)
mp.mp.dps = 15


def bp_funcs(pv_):
    Fn = lambda q: (1 + q * q) ** ((pv_ - 1) / 2)
    dF = lambda q: (pv_ - 1) * q * (1 + q * q) ** ((pv_ - 3) / 2)
    b = lambda q: mp.quad(lambda tt: tt**3 * Fn(q * tt), [0, 1])
    db = lambda q: mp.quad(lambda tt: tt**4 * dF(q * tt), [0, 1])
    return Fn, dF, b, db


pv_ = mp.mpf("0.7")
Fn, dF, bfun, dbfun = bp_funcs(pv_)
tt_ = [2 * mp.pi * j / 64 for j in range(64)]


def circ(rr):
    b0, b1 = bfun(rr), dbfun(rr)
    tot = 0
    for tq_ in tt_:
        X0, Y0 = rr * mp.cos(tq_), rr * mp.sin(tq_)
        V1 = X0 * b0 + X0 * Y0**2 * b1 / rr
        V2 = -Y0 * b0 - X0**2 * Y0 * b1 / rr
        r6 = rr**6
        px = (6 * X0 * Y0) / r6 - 6 * (3 * X0**2 * Y0 - Y0**3) * X0 / rr**8
        py = (3 * X0**2 - 3 * Y0**2) / r6 - 6 * (3 * X0**2 * Y0 - Y0**3) * Y0 / rr**8
        tot += Y0 * Fn(rr) * (V1 * px + V2 * py)
    return tot * 2 * mp.pi / 64 * rr


Bdirect = mp.quad(circ, [0, 1, 5, 50, mp.inf])
Bformula = 3 * mp.pi / 4 * mp.quad(lambda rr: Fn(rr) * dbfun(rr), [0, 1, 5, 50, mp.inf])
report("3.43(iv) B(v_p) = (3pi/4) int F_p b_p' dr in [-3pi/16, 0] (p = 0.7)",
       abs(Bdirect - Bformula) < 1e-8 and -3 * mp.pi / 16 <= Bformula <= 0,
       "direct %s, formula %s" % (mp.nstr(Bdirect, 12), mp.nstr(Bformula, 12)))
# |DV_p|_F on a polar grid via finite differences of the explicit field
okDV = True
maxDV = 0.0
for pv_ in (0.5, 0.75, 0.99):
    gl2, gw2 = np.polynomial.legendre.leggauss(60)
    tnodes = (gl2 + 1) / 2
    twts = gw2 / 2

    def bnum(q):
        q = np.atleast_1d(q)[:, None]
        return np.sum(twts * tnodes**3 * (1 + (q * tnodes) ** 2) ** ((pv_ - 1) / 2), axis=1)

    def Vp(X0, Y0):
        q = np.sqrt(X0**2 + Y0**2)
        hh = 1e-6
        b0 = bnum(q)
        b1 = (bnum(q + hh) - bnum(q - hh)) / (2 * hh)
        return float(X0 * b0[0] + X0 * Y0**2 * b1[0] / q), float(-Y0 * b0[0] - X0**2 * Y0 * b1[0] / q)

    for rr_v in np.geomspace(1e-2, 1e3, 40):
        for tv in np.linspace(0.05, math.pi / 2 - 0.05, 12):
            X0, Y0 = rr_v * math.cos(tv), rr_v * math.sin(tv)
            hh = 1e-4 * max(rr_v, 1e-2)
            a_ = [(np.array(Vp(X0 + hh, Y0)) - np.array(Vp(X0 - hh, Y0))) / (2 * hh),
                  (np.array(Vp(X0, Y0 + hh)) - np.array(Vp(X0, Y0 - hh))) / (2 * hh)]
            fro = math.sqrt(sum(float(v) ** 2 for col in a_ for v in col))
            maxDV = max(maxDV, fro)
okDV = maxDV <= 2
Hm = sp.Matrix([[y**2, 2 * x * y], [-2 * x * y, -x**2]])
okH = sp.simplify(sum(e**2 for e in Hm) - ((x**2 + y**2) ** 2 + 6 * x**2 * y**2)) == 0
okH &= sp.sqrt(2) / 4 + R(1, 4) + sp.sqrt(10) / 8 + R(1, 2) < 2
report("3.43(iv) |DH|_F^2 = r^4 + 6x^2y^2 <= 5r^4/2 for H = (xy^2, -x^2y); sqrt2/4 + 1/4 + sqrt10/8 + 1/2 < 2", okH)
report("3.43(iv) |DV_p|_F <= 2 on a grid, p in {0.5, 0.75, 0.99}", okDV, "max %.4f" % maxDV)

# ----------------------------------------------------------------------- summary
nfail = sum(1 for _, ok in results if not ok)
print("%d checks, %d failed" % (len(results), nfail))
sys.exit(1 if nfail else 0)
