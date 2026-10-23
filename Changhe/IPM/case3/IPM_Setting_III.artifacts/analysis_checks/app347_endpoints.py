"""Symbolic checks for the appendix entries A.3.47(iv) and A.3.49.

Exact sympy checks of the rational arithmetic in 3.49(a), the explicit solutions and identities used in
3.49(b)-(d), the mode formulas used in A.3.49(d) and the affine core of A.3.47(iv).  A finite truncation
of the Jacobi matrix is evaluated numerically only as a consistency check (it gives a lower bound for the
top of the spectrum, not an upper bound).  Run with OMP_NUM_THREADS=1.  Exit status is nonzero on failure.
"""
import sys

import sympy as sp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


x, y = sp.symbols("x y", real=True)
r, th, t = sp.symbols("r theta t", positive=True)
m = sp.symbols("m", positive=True)
j = sp.symbols("j", positive=True)


def bj(jj, mm):
    return (mm**2 + 4 * jj**2) / (4 * sp.Abs(4 * jj**2 - mm**2))


# ---------------------------------------------------------------- 3.49(a): exact arithmetic
m0 = sp.Rational(11, 3)
b1, b2, b3 = bj(1, m0), bj(2, m0), bj(3, m0)
report("E1 b_1, b_2, b_3 at m = 11/3 are 157/340, 265/92, 445/812",
       b1 == sp.Rational(157, 340) and b2 == sp.Rational(265, 92) and b3 == sp.Rational(445, 812))
report("E1b b_3 > b_1 at m = 11/3", b3 > b1)
Bm = sp.Rational(1, 2) + b2 + sp.Max(b1, b3)
report("E2 B_m = 1/2 + b_2 + max(b_1, b_3) = 18342/4669 at m = 11/3", Bm == sp.Rational(18342, 4669),
       str(Bm) + " = " + str(sp.N(Bm, 12)))
# monotonicity: for 4 j^2 > m^2, b_j = (1/4)(1 + 2 m^2/(4 j^2 - m^2)), decreasing in j
bj_large = (m**2 + 4 * j**2) / (4 * (4 * j**2 - m**2))
report("E3 b_j = (1/4)(1 + 2m^2/(4j^2 - m^2)) for 4j^2 > m^2",
       zero(bj_large - sp.Rational(1, 4) * (1 + 2 * m**2 / (4 * j**2 - m**2))))
dbj = sp.factor(sp.diff(bj_large, j))
report("E3b d b_j/dj = -4 j m^2/(4j^2 - m^2)^2 < 0", zero(dbj + 4 * j * m**2 / (4 * j**2 - m**2)**2), str(dbj))
# Gershgorin rows at m = 11/3: row1 < row2, rows j >= 4 <= 1/2 + 2 b_3 <= row3, max = B_m
row1 = sp.Rational(1, 4) + b1
row2 = sp.Rational(1, 2) + b1 + b2
row3 = sp.Rational(1, 2) + b2 + b3
row4 = sp.Rational(1, 2) + b3 + bj(4, m0)
report("E4 rows: 1/4 + b_1 < 1/2 + b_1 + b_2 < 1/2 + b_2 + b_3 = B_m, row 4 < row 3",
       row1 < row2 and row2 < row3 and row3 == Bm and row4 < row3 and sp.Rational(1, 2) + 2 * b3 <= row3)
# general m in (2, 4): b_1 is defined with 4 < m^2 < 16, and j >= 2 has 4 j^2 > m^2
report("E4b for 2 < m < 4: 4 - m^2 < 0 < 16 - m^2", all((4 - mm**2 < 0) and (16 - mm**2 > 0)
                                                     for mm in [sp.Rational(201, 100), 3, m0, sp.Rational(399, 100)]))
s0, K0 = sp.Rational(2, 5), 1
beta = m0 - 2 - m0 * s0
coef = K0 * Bm - (m0 - 1)
eps = beta / coef
report("E5 beta = m - 2 - m s = 1/5, K B_m - (m - 1) = 17674/14007, eps = 14007/88370 at m = 11/3, s = 2/5, K = 1",
       beta == sp.Rational(1, 5) and coef == sp.Rational(17674, 14007) and eps == sp.Rational(14007, 88370),
       "eps = %s = %s" % (eps, sp.N(eps, 12)))
report("E5b eps > 0.158", eps > sp.Rational(158, 1000))
Dd = sp.symbols("D", positive=True)
lhs = (m0 - 1) * (1 + Dd) - 1
rhs = m0 * s0 + Bm * K0 * Dd
report("E5c (m-1)c_l - 1 - (m s + B_m K D) = beta - (K B_m - (m-1)) D, vanishing at D = eps",
       zero(lhs - rhs - (beta - coef * Dd)) and zero((lhs - rhs).subs(Dd, eps)))
# 3.44(ii) => G_rho + G_U >= (sqrt 2/3)(2c_l - 1): need 3/sqrt 2 >= 1.633 and >= 0.710
report("E6 3/sqrt(2) > 1633/1000 > 710/1000", sp.Rational(9, 2) > sp.Rational(1633, 1000)**2)
# consistency: truncated Jacobi matrix top eigenvalue (a lower bound for Q_m^-) is below B_m
import numpy as np

n_tr = 4000
diag = np.array([0.25] + [0.5] * (n_tr - 1))
off = np.array([float(bj(k, m0)) for k in range(1, n_tr)])
Jmat = np.diag(diag) + np.diag(off, 1) + np.diag(off, -1)
top = float(np.linalg.eigvalsh(Jmat)[-1])
report("E7 truncated Jacobi matrix (4000 rows) at m = 11/3: top eigenvalue < B_m (consistency only)",
       top < float(Bm), "top = %.10f, B_m = %.10f" % (top, float(Bm)))

# ---------------------------------------------------------------- 3.49(b)
f = sp.Function("f")
q = f(y)
u1, u2 = x, -y
eq_tr = (x + u1) * sp.diff(q, x) + (y + u2) * sp.diff(q, y)
report("E8 q = f(y), u = (x, -y): (X + u).grad q = 0, div u = 0, curl u = -q_x",
       zero(eq_tr) and zero(sp.diff(u1, x) + sp.diff(u2, y)) and zero(sp.diff(u2, x) - sp.diff(u1, y) + sp.diff(q, x)))
cl = sp.symbols("c_l", positive=True)
rho = sp.Function("rho")(x, y)
U1 = sp.Function("U1")(x, y)
U2 = sp.Function("U2")(x, y)
Rres = (cl * x + U1) * sp.diff(rho, x) + (cl * y + U2) * sp.diff(rho, y) - rho
qn, un1, un2 = rho / cl, U1 / cl, U2 / cl
norm_res = (x + un1) * sp.diff(qn, x) + (y + un2) * sp.diff(qn, y) - qn / cl
report("E9 R/c_l^2 = (X + u).grad q - q/c_l for q = rho/c_l, u = U/c_l", zero(Rres / cl**2 - norm_res))
divform = sp.diff((x + un1) * qn, x) + sp.diff((y + un2) * qn, y) - ((x + un1) * sp.diff(qn, x)
                                                                      + (y + un2) * sp.diff(qn, y)) - 2 * qn
report("E9b div((X + u) q) = (X + u).grad q + (2 + div u) q",
       zero(divform - qn * (sp.diff(un1, x) + sp.diff(un2, y))))
# radial first mode: psi = -a x y H(r), r H' + 4 H = F gives -Lap psi = d_x(a y F(r))
a = sp.symbols("a", real=True)
Hf = sp.Function("H")
rr = sp.sqrt(x**2 + y**2)
psi_rad = -a * x * y * Hf(rr)
Fexpr = rr * sp.diff(Hf(rr), x) * rr / x + 4 * Hf(rr)  # r H'(r) + 4 H(r), written via d_x H(r) = H'(r) x/r
lap = lambda g: sp.diff(g, x, 2) + sp.diff(g, y, 2)
e_rad = -lap(psi_rad) - sp.diff(a * y * Fexpr, x)
report("E10 psi = -a x y H(r) with F = r H' + 4 H solves -Lap psi = d_x(a y F)", zero(sp.simplify(e_rad)))
Ux_rad = -sp.diff(psi_rad, y)
Uy_rad = sp.diff(psi_rad, x)
Hp = sp.diff(Hf(rr), x) * rr / x  # H'(r)
report("E10b U = (a x (H + y^2 H'/r), -a y (H + x^2 H'/r))",
       zero(sp.simplify(Ux_rad - a * x * (Hf(rr) + y**2 * Hp / rr)))
       and zero(sp.simplify(Uy_rad + a * y * (Hf(rr) + x**2 * Hp / rr))))
# third angular mode of the structural densities
ts = sp.symbols("tau", real=True)
I13 = sp.integrate(sp.sin(ts) * sp.sin(3 * ts), (ts, 0, 2 * sp.pi))
I33 = sp.integrate(sp.sin(3 * ts)**2, (ts, 0, 2 * sp.pi))
I53 = sp.integrate(sp.sin(5 * ts) * sp.sin(3 * ts), (ts, 0, 2 * sp.pi))
report("E11 int sin th sin 3th = 0, int sin^2 3th = pi, int sin 5th sin 3th = 0", I13 == 0 and I33 == sp.pi and I53 == 0)
kap, n = sp.symbols("kappa n", positive=True)
aa = kap * n
cstrain = -aa / 4 + (aa / 4 - (n - 1))
report("E11b psi_xy(0) = -a/4 + (a/4 - (c_l - 1)) = 1 - c_l", zero(cstrain - (1 - n)))
# parity of sin(k th), k = 3, 5, as polynomials / r^k
for k in (3, 5):
    pk = sp.im(sp.expand((x + sp.I * y)**k))
    ok = zero(pk.subs(x, -x) - pk) and zero(pk.subs(y, -y) + pk)
    report("E12 r^%d sin(%d th) = Im (x + i y)^%d is even in x and odd in y" % (k, k, k), ok, str(pk))
# Fourier multipliers of v = U[f]: psi_hat = i xi1 f_hat/|xi|^2
xi1, xi2 = sp.symbols("xi1 xi2", real=True)
fh = sp.symbols("fh")
k2 = xi1**2 + xi2**2
psih = sp.I * xi1 * fh / k2
v1h, v2h = -sp.I * xi2 * psih, sp.I * xi1 * psih
report("E13 -Lap psi = f_x in Fourier; v_2 hat = -xi1^2/|xi|^2 f hat; |v hat|^2 = xi1^2/|xi|^2 |f hat|^2",
       zero(k2 * psih - sp.I * xi1 * fh) and zero(v2h + xi1**2 / k2 * fh)
       and zero(sp.expand(v1h * sp.conjugate(v1h) + v2h * sp.conjugate(v2h)).subs(sp.conjugate(fh), sp.Symbol("fc"))
                - xi1**2 / k2 * fh * sp.Symbol("fc")))
vv1, vv2 = sp.Function("v1")(x, y), sp.Function("v2")(x, y)
report("E13b div(y v) = v_2 + y div v", zero(sp.diff(y * vv1, x) + sp.diff(y * vv2, y) - vv2
                                          - y * (sp.diff(vv1, x) + sp.diff(vv2, y))))

# ---------------------------------------------------------------- 3.49(c)
# exact solutions (a y, 0) of the c_l = 1 system
report("E14 (rho, U) = (a y, 0) solves X.grad rho = rho (and div 0 = 0, curl 0 = -d_x(a y))",
       zero(x * sp.diff(a * y, x) + y * sp.diff(a * y, y) - a * y) and zero(sp.diff(a * y, x)))
# Euler: X.grad of a homogeneous polynomial of degree d is d times it
cs = sp.symbols("c0:6")
pj = sum(cs[i] * x**i * y**(5 - i) for i in range(6))
report("E14b X.grad P = 5 P for P homogeneous of degree 5", zero(x * sp.diff(pj, x) + y * sp.diff(pj, y) - 5 * pj))
# U_1 - i U_2 holomorphic iff div U = 0 and curl U = 0
uu1, uu2 = sp.Function("u1")(x, y), sp.Function("u2")(x, y)
cr1 = sp.diff(uu1, x) - sp.diff(-uu2, y)
cr2 = sp.diff(uu1, y) + sp.diff(-uu2, x)
report("E14c Cauchy-Riemann for (U_1, -U_2) is div U = 0 and curl U = 0",
       zero(cr1 - (sp.diff(uu1, x) + sp.diff(uu2, y))) and zero(cr2 + (sp.diff(uu2, x) - sp.diff(uu1, y))))

# ---------------------------------------------------------------- 3.49(d): mode formulas
Dsym, lsym = sp.symbols("D l", positive=True)
A_ = sp.Function("A_")  # density mode coefficient a_j(t), t = log r


def polar_dx(F):
    return sp.cos(th) * sp.diff(F, r) - sp.sin(th) / r * sp.diff(F, th)


def polar_dy(F):
    return sp.sin(th) * sp.diff(F, r) + sp.cos(th) / r * sp.diff(F, th)


ok15 = True
for jj in (1, 3, 5, 7):
    Fj = r * A_(sp.log(r)) * sp.sin(jj * th)
    ap = sp.Subs(sp.Derivative(A_(t), t), t, sp.log(r)).doit()
    target = (sp.Rational(1, 2) * ((1 - jj) * A_(sp.log(r)) + ap) * sp.sin((jj + 1) * th)
              + sp.Rational(1, 2) * ((1 + jj) * A_(sp.log(r)) + ap) * sp.sin((jj - 1) * th))
    ok15 = ok15 and zero(sp.expand_trig(sp.expand(polar_dx(Fj) - target)))
report("E15 d_x(r a(log r) sin j th) = (1/2)((1-j)a + a') sin((j+1)th) + (1/2)((1+j)a + a') sin((j-1)th), j = 1,3,5,7",
       ok15)
# gradient of r a sin(j th): radial (a + a') sin, angular j a cos
ok15b = True
for jj in (1, 3, 5):
    Fj = r * A_(sp.log(r)) * sp.sin(jj * th)
    ap = sp.Subs(sp.Derivative(A_(t), t), t, sp.log(r)).doit()
    gx, gy = polar_dx(Fj), polar_dy(Fj)
    grad_r = sp.cos(th) * gx + sp.sin(th) * gy
    grad_t = -sp.sin(th) * gx + sp.cos(th) * gy
    ok15b = ok15b and zero(sp.simplify(grad_r - (A_(sp.log(r)) + ap) * sp.sin(jj * th))) \
        and zero(sp.simplify(grad_t - jj * A_(sp.log(r)) * sp.cos(jj * th)))
report("E15b grad(r a sin j th) = (a + a') sin(j th) e_r + j a cos(j th) e_th", ok15b)
# -Lap(r^2 p(log r) sin N th) = -[(d_t + 2)^2 - N^2] p sin N th, and polar Hessian entries
P_ = sp.Function("P_")
ok16 = True
ok16b = True
for N in (2, 4, 6):
    Fn = r**2 * P_(sp.log(r)) * sp.sin(N * th)
    p0 = P_(sp.log(r))
    p1 = sp.Subs(sp.Derivative(P_(t), t), t, sp.log(r)).doit()
    p2 = sp.Subs(sp.Derivative(P_(t), (t, 2)), t, sp.log(r)).doit()
    lapF = sp.diff(Fn, r, 2) + sp.diff(Fn, r) / r + sp.diff(Fn, th, 2) / r**2
    ok16 = ok16 and zero(sp.simplify(lapF - (4 * p0 + 4 * p1 + p2 - N**2 * p0) * sp.sin(N * th)))
    Frr = sp.diff(Fn, r, 2)
    Fmix = sp.diff(Fn, r, th) / r - sp.diff(Fn, th) / r**2
    Ftt = sp.diff(Fn, r) / r + sp.diff(Fn, th, 2) / r**2
    ok16b = ok16b and zero(sp.simplify(Frr - (2 * p0 + 3 * p1 + p2) * sp.sin(N * th))) \
        and zero(sp.simplify(Fmix - N * (p0 + p1) * sp.cos(N * th))) \
        and zero(sp.simplify(Ftt - (2 * p0 + p1 - N**2 * p0) * sp.sin(N * th)))
report("E16 Lap(r^2 p(t) sin N th) = ((d_t + 2)^2 - N^2) p sin N th, N = 2, 4, 6", ok16)
report("E16b polar-frame Hessian of r^2 p sin N th: (2p+3p'+p'') sin, N(p+p') cos, (2p+p'-N^2 p) sin", ok16b)
# the Cartesian Hessian of a generic G(r, th) is R M R^T, M = polar-frame Hessian, R = rotation by th;
# hence the Frobenius norms agree
G_ = sp.Function("G")(r, th)
Mrr = sp.diff(G_, r, 2)
Mrt = sp.diff(G_, r, th) / r - sp.diff(G_, th) / r**2
Mtt = sp.diff(G_, r) / r + sp.diff(G_, th, 2) / r**2
Mp = sp.Matrix([[Mrr, Mrt], [Mrt, Mtt]])
Rot = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
Hc = Rot * Mp * Rot.T
Hcart = sp.Matrix([[polar_dx(polar_dx(G_)), polar_dx(polar_dy(G_))], [polar_dy(polar_dx(G_)), polar_dy(polar_dy(G_))]])
report("E16c Cartesian Hessian = R(th) M R(th)^T for generic G(r, th) (so |D^2 G|_F = |M|_F)",
       all(zero(sp.simplify(sp.expand(Hc[i, k] - Hcart[i, k]))) for i in range(2) for k in range(2)))
# Green kernel of 3.1(iv) in t = log r for frequency N = 2n >= 4
nn = sp.symbols("nn", positive=True)
uu = sp.symbols("u", real=True)
Kp = sp.exp(-(2 * nn + 2) * uu) / (4 * nn)   # u > 0
Km = sp.exp((2 * nn - 2) * uu) / (4 * nn)    # u < 0
Lop = lambda K: (2 * nn)**2 * K - (sp.diff(K, uu, 2) + 4 * sp.diff(K, uu) + 4 * K)
jump = -(sp.diff(Kp, uu).subs(uu, 0) - sp.diff(Km, uu).subs(uu, 0))
L1 = sp.integrate(Kp, (uu, 0, sp.oo), conds="none") + sp.integrate(Km, (uu, -sp.oo, 0), conds="none")
report("E17 kernel of [N^2 - (d_t+2)^2], N = 2n: homogeneous on both sides, continuous, unit jump, L^1 norm 1/(N^2-4)",
       zero(Lop(Kp)) and zero(Lop(Km)) and zero(Kp.subs(uu, 0) - Km.subs(uu, 0)) and zero(jump - 1)
       and zero(L1 - 1 / ((2 * nn)**2 - 4)))
# check the change of variables in 3.1(iv): r^{-2n} int_0^r s^{2n+1} f ds / r^2 = int_{-inf}^t e^{-(2n+2)(t - tau)} f dtau
# on the test function f = e^{b tau} (b > 0)
bb = sp.symbols("bb", positive=True)
lhs_g = (sp.exp(-2 * nn * t) * sp.integrate(sp.exp((2 * nn + 2) * ts) * sp.exp(bb * ts), (ts, -sp.oo, t), conds="none")
         / sp.exp(2 * t))
rhs_g = sp.integrate(sp.exp(-(2 * nn + 2) * (t - ts)) * sp.exp(bb * ts), (ts, -sp.oo, t), conds="none")
sv = sp.symbols("sv", positive=True)
lhs_r = r**(-2 * nn) * sp.integrate(sv**(2 * nn + 1) * sv**bb, (sv, 0, r), conds="none") / r**2
report("E17b 3.1(iv) inner term in t = log r (test f = e^{b t})",
       zero(sp.simplify(lhs_g - rhs_g)) and zero(sp.simplify(lhs_r.subs(r, sp.exp(t)) - rhs_g)))
# mode 2: f_1 = (1/2) a_1' + 2 a_3 + (1/2) a_3'; Q = int_t^inf f_1 = D B(s);
# p_1 = (1/4)[int_{-inf}^t e^{-4(t-tau)} f_1 + Q] = int_0^inf e^{-4u} Q(t - u) du
# check (d_t + 4) of both sides equals Q for a test Q(t) = e^{-t^2} (f_1 = -Q')
Qt = sp.exp(-t**2)
f1 = -sp.diff(Qt, t)
inner = sp.Integral(sp.exp(-4 * (t - ts)) * f1.subs(t, ts), (ts, -sp.oo, t))
p1a = (inner + Qt) / 4
p1b = sp.Integral(sp.exp(-4 * (t - ts)) * Qt.subs(t, ts), (ts, -sp.oo, t))
d4 = lambda e: sp.diff(e, t) + 4 * e
ok18 = zero(sp.simplify(d4(p1a).doit() - Qt)) and zero(sp.simplify(d4(p1b).doit() - Qt))
p1a_n = sp.N(p1a.subs(t, sp.Rational(3, 10)).doit(), 30)
p1b_n = sp.N(p1b.subs(t, sp.Rational(3, 10)).doit(), 30)
report("E18 mode 2: (1/4)[int e^{-4(t-tau)} f_1 + Q] = int e^{-4(t-tau)} Q (test Q = e^{-t^2})",
       ok18 and abs(p1a_n - p1b_n) < 1e-20, "values at t = 0.3: %s, %s" % (sp.N(p1a_n, 15), sp.N(p1b_n, 15)))
hh = sp.Function("h")
H3 = sp.Function("H3")
sv2 = sp.symbols("s", real=True)
# int_t^T f_1 dtau with a_1 = D h(s), a_3 = D^2 H3(s), s = D (tau - log l), d_tau = D d_s
f1s = sp.Rational(1, 2) * Dsym**2 * sp.Derivative(hh(sv2), sv2) + 2 * Dsym**2 * H3(sv2) \
    + sp.Rational(1, 2) * Dsym**3 * sp.Derivative(H3(sv2), sv2)
# dtau = ds/D; antiderivative in s of f1s/D, apart from the integral term
anti = sp.Rational(1, 2) * Dsym * hh(sv2) + sp.Rational(1, 2) * Dsym**2 * H3(sv2)
report("E18b f_1/D = d_s[(D/2) h + (D^2/2) H_3] + 2 D H_3, so Q = D(-h/2 - (D/2) H_3 + 2 int_s^inf H_3) = D B",
       zero(sp.simplify(f1s / Dsym - sp.diff(anti, sv2) - 2 * Dsym * H3(sv2))))

# ---------------------------------------------------------------- A.3.47(iv): affine core
Dc = sp.symbols("Dc", positive=True)
clc = 1 + Dc
Ac = 2 * clc - 1
psi_core = -Dc * x * y
Uc1, Uc2 = -sp.diff(psi_core, y), sp.diff(psi_core, x)
Wc1, Wc2 = clc * x + Uc1, clc * y + Uc2
Bc = (x * Wc1 + y * Wc2) / (x**2 + y**2)
report("E19 phi = 0: psi = -D x y gives U = (D x, -D y), W = (A x, y), B - 1 = 2D x^2/r^2 >= 0, W_2/y = 1",
       zero(Uc1 - Dc * x) and zero(Uc2 + Dc * y) and zero(Wc1 - Ac * x) and zero(Wc2 - y)
       and zero(Bc - 1 - 2 * Dc * x**2 / (x**2 + y**2)) and zero(Wc2 / y - 1))
# parity: no quadratic terms in U for psi odd in x and in y (psi has only monomials x^odd y^odd)
cq = sp.symbols("cq0:10")
psi_odd = (cq[0] * x * y + cq[1] * x**3 * y + cq[2] * x * y**3 + cq[3] * x**5 * y + cq[4] * x**3 * y**3
           + cq[5] * x * y**5)
Ue1, Ue2 = -sp.diff(psi_odd, y), sp.diff(psi_odd, x)
quad = [sp.Poly(Ue1, x, y).coeff_monomial(mo) for mo in (x**2, x * y, y**2)] + \
       [sp.Poly(Ue2, x, y).coeff_monomial(mo) for mo in (x**2, x * y, y**2)]
report("E19b psi odd in x and y: U has no quadratic Taylor terms", all(zero(cq_) for cq_ in quad))
# concentration: ratio bound (r0/R)^{2m}/(2m - 4) times m tends to 0 (r0 < R)
lim = sp.limit(m * (sp.Rational(1, 2))**(2 * m) / (2 * m - 4), m, sp.oo)
report("E20 m (r0/R)^{2m}/(2m - 4) -> 0 (r0/R = 1/2)", lim == 0)
mm_ = sp.symbols("mm_", positive=True)
Rb = sp.symbols("R", positive=True)
s_ = sp.symbols("s_", positive=True)
ext_int = sp.integrate(2 * sp.pi * s_**(2 - 2 * mm_) * s_, (s_, Rb, sp.oo), conds="none")
report("E20b int_{r >= R} r^{2-2m} dX = 2 pi R^{4-2m}/(2m - 4) for m > 2",
       zero(sp.simplify(ext_int.subs(mm_, 3 + mm_) - 2 * sp.pi * Rb**(4 - 2 * (3 + mm_)) / (2 * (3 + mm_) - 4))))

nf = sum(1 for _, ok in results if not ok)
print("%d checks, %d failed" % (len(results), nf))
sys.exit(1 if nf else 0)
