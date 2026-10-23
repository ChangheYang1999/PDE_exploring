"""Symbolic checks for the appendix entries A.3.47 and A.3.48.

Exact sympy checks of the differential identities, the angular integrals and the elementary
inequalities used in the written proofs, plus two numerical tests of the moment identities on
manufactured functions (flat at 0, decaying at infinity).  The checks support, but do not
replace, the written proofs.  Run with OMP_NUM_THREADS=1.  Exit status is nonzero on failure.
"""
import sys

import mpmath as mp
import sympy as sp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


x, y = sp.symbols("x y", real=True)
r, th, t = sp.symbols("r theta t", positive=True)
m, cl, b = sp.symbols("m c_l b", positive=True)
a = sp.symbols("a", real=True, nonzero=True)
D = cl - 1
A = 2 * cl - 1
rr = sp.sqrt(x**2 + y**2)
polar = {x: r * sp.cos(th), y: r * sp.sin(th)}


def lap(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


# ---------------------------------------------------------------- weights
w0 = y * rr**(2 - 2 * m)
e1 = lap(w0) - 4 * (m - 1) * (m - 2) * y * rr**(-2 * m)
report("S1 Lap(y r^{2-2m}) = 4(m-1)(m-2) y r^{-2m}", zero(e1.subs(polar)))
e2 = sp.diff(w0, x, 2) - 2 * (m - 1) * y * rr**(-2 * m) * (2 * m * x**2 / rr**2 - 1)
report("S2 d_xx(y r^{2-2m}) = 2(m-1) y r^{-2m}(2m x^2/r^2 - 1)", zero(e2.subs(polar)))
g0 = [sp.diff(w0, x), sp.diff(w0, y)]
g0e = [(2 - 2 * m) * y * rr**(-2 * m) * x, rr**(2 - 2 * m) + (2 - 2 * m) * y * rr**(-2 * m) * y]
report("S3 grad(y r^{2-2m}) = r^{2-2m} e_2 + (2-2m) y r^{-2m} X",
       all(zero((g0[i] - g0e[i]).subs(polar)) for i in range(2)))
# |grad w0|^2 r^{4m-4} = 1 + 4(m-1)(m-2) sin^2 th <= (2m-3)^2 <= (2m-1)^2 for m > 2
gn = sp.simplify(((g0[0]**2 + g0[1]**2) * rr**(4 * m - 4)).subs(polar))
report("S3b |grad w0|^2 r^{4m-4} = 1 + 4(m-1)(m-2) sin^2 th",
       zero(gn - 1 - 4 * (m - 1) * (m - 2) * sp.sin(th)**2))

# ---------------------------------------------------------------- generic identities
rho = sp.Function("rho")(x, y)
psi = sp.Function("psi")(x, y)
Hf = sp.Function("H")(x, y)
U1, U2 = -sp.diff(psi, y), sp.diff(psi, x)
W1, W2 = cl * x + U1, cl * y + U2
divU = sp.diff(U1, x) + sp.diff(U2, y)
report("S4 div U = 0 for U = (-psi_y, psi_x)", zero(divU))
Wgrad = lambda f: W1 * sp.diff(f, x) + W2 * sp.diff(f, y)
Hh = y - rho / a
V = U2 + D * y
e5 = Wgrad(Hh) - Hh - V + (Wgrad(rho) - rho) / a
report("S5 W.grad H - H - V = -(W.grad rho - rho)/a", zero(e5))
e6 = lap(V) - a * sp.diff(Hh, x, 2) + sp.diff(-lap(psi) - sp.diff(rho, x), x)
report("S6 Lap V - a H_xx = -d_x(-Lap psi - rho_x)", zero(e6))
# transport test with w = y r^{-2m}
w = y * rr**(-2 * m)
Bq = (x * W1 + y * W2) / rr**2
div_HwW = sp.diff(Hf * w * W1, x) + sp.diff(Hf * w * W2, y)
lhs = w * (Wgrad(Hf) - Hf) - div_HwW
rhs = Hf * y * rr**(-2 * m) * (2 * m * Bq - 2 * cl - 1) - Hf * W2 * rr**(-2 * m)
report("S7 w(W.grad H - H) - div(H w W) = H y r^{-2m}(2mB - 2c_l - 1) - H W_2 r^{-2m}",
       zero(sp.simplify(lhs - rhs)))
# differentiated transport and the energy identity
g = [sp.diff(rho, x), sp.diff(rho, y)]
DU = sp.Matrix([[sp.diff(U1, x), sp.diff(U1, y)], [sp.diff(U2, x), sp.diff(U2, y)]])
DW = cl * sp.eye(2) + DU
Rt = Wgrad(rho) - rho
gv = sp.Matrix(g)
lhs8 = sp.Matrix([sp.diff(Rt, x), sp.diff(Rt, y)])
rhs8 = sp.Matrix([Wgrad(g[0]), Wgrad(g[1])]) - gv + DW.T * gv
report("S8 grad(W.grad rho - rho) = W.grad g - g + DW^T g",
       all(zero(lhs8[i] - rhs8[i]) for i in range(2)))
S = (DU + DU.T) / 2
e9 = (gv.T * (gv - DW.T * gv))[0] - (-D * (gv.T * gv)[0] - (gv.T * S * gv)[0])
report("S9 g.(g - DW^T g) = -D|g|^2 - g^T S g", zero(e9))
curl = sp.diff(U2, x) - sp.diff(U1, y)
Jm = sp.Matrix([[0, -1], [1, 0]])
e10 = DU - S - curl / 2 * Jm
report("S10 DU = S + (curl U/2) [[0,-1],[1,0]], curl U = Lap psi",
       all(zero(e10[i, j]) for i in range(2) for j in range(2)) and zero(curl - lap(psi)))
report("S10b tr S = 0", zero(S[0, 0] + S[1, 1]))

# ---------------------------------------------------------------- radial and axis formulas (example)
q = sp.symbols("q0:6", real=True)
psi_ex = (-D * x * y + q[0] * x**3 * y + q[1] * x * y**3 + q[2] * x**5 * y + q[3] * x**3 * y**3
          + q[4] * x * y**5 + q[5] * x * y * (x**2 + y**2)**3)
U1e, U2e = -sp.diff(psi_ex, y), sp.diff(psi_ex, x)
DUe = sp.Matrix([[sp.diff(U1e, x), sp.diff(U1e, y)], [sp.diff(U2e, x), sp.diff(U2e, y)]])
Se = (DUe + DUe.T) / 2
tX = {x: t * x, y: t * y}
XSX = (sp.Matrix([[x, y]]) * Se.subs(tX, simultaneous=True) * sp.Matrix([x, y]))[0]
e11 = x * U1e + y * U2e - sp.integrate(sp.expand(XSX), (t, 0, 1))
report("S11 X.U = int_0^1 X^T S(tX) X dt (polynomial example)", zero(e11))
e12 = U1e - x * sp.integrate(sp.expand(sp.diff(U1e, x).subs(x, t * x)), (t, 0, 1))
e13 = U2e - y * sp.integrate(sp.expand(sp.diff(U2e, y).subs(y, t * y)), (t, 0, 1))
report("S12 U_1 = x int_0^1 S_11(tx, y) dt, U_2 = y int_0^1 S_22(x, ty) dt (example)",
       zero(e12) and zero(e13))
report("S12b U_1(0, y) = 0, U_2(x, 0) = 0 (example)",
       zero(U1e.subs(x, 0)) and zero(U2e.subs(y, 0)))

# ---------------------------------------------------------------- explicit choice of m
ap = b  # |a| = b > 0
mm = 3 + 2 * cl + 2 * ap
low = sp.simplify(2 * mm - 4 * cl)
report("S13 lower bound 2m - 4c_l = 6 + 4|a| at m = 3 + 2c_l + 2|a|", zero(low - 6 - 4 * ap))
up_pos = ap * (2 * mm - 1) / (2 * (mm - 2))
d1 = sp.factor(sp.together(sp.Rational(3, 2) * ap - up_pos))
d2 = sp.factor(sp.together(sp.Rational(5, 2) * ap - up_pos))
up_neg = ap / (2 * (mm - 2))
d3 = sp.factor(sp.together(sp.Rational(1, 4) - up_neg))
print("   3|a|/2 - upper(a>0) =", d1)
print("   5|a|/2 - upper(a>0) =", d2)
print("   1/4 - upper(a<0)    =", d3)
sub = {cl: 1 + sp.Symbol("d", positive=True)}
pos = lambda e: sp.simplify(e.subs(sub)).is_positive
report("S14 at m = 3 + 2c_l + 2|a|: upper(a>0) < 3|a|/2 < 5|a|/2 and upper(a<0) < 1/4",
       pos(d1) and pos(d2) and pos(d3))
report("S14b 6 + 4|a| > 5|a|/2 and 6 + 4|a| > 1/4", pos(6 + 4 * ap - sp.Rational(5, 2) * ap) and pos(6 + 4 * ap - sp.Rational(1, 4)))
# (2m - 1)/(2(m - 2)) = 1 + 3/(2(m - 2))
report("S15 (2m-1)/(2(m-2)) = 1 + 3/(2(m-2))", zero((2 * m - 1) / (2 * (m - 2)) - 1 - 3 / (2 * (m - 2))))

# ---------------------------------------------------------------- angular integrals (3.48)
I13 = sp.integrate(sp.sin(th) * sp.sin(3 * th), (th, 0, 2 * sp.pi))
I33 = sp.integrate(sp.sin(3 * th)**2, (th, 0, 2 * sp.pi))
report("S16 int_0^{2pi} sin th sin 3th = 0, int sin^2 3th = pi", I13 == 0 and sp.simplify(I33 - sp.pi) == 0)
a0s, bs = sp.symbols("a0 bb", real=True)
rho_ex = (a0s * y + bs * (3 * x**2 * y - y**3)) * sp.exp(-(x**2 + y**2))
rho3 = sp.simplify(sp.integrate(sp.expand_trig(sp.simplify(rho_ex.subs(polar)) * sp.sin(3 * th)),
                                (th, 0, 2 * sp.pi)) / sp.pi)
ok17 = zero(rho3 - bs * r**3 * sp.exp(-r**2))
J = sp.integrate(rho3 / r**2, (r, 0, sp.oo))
report("S17 example: rho_3 = b r^3 e^{-r^2}, int rho_3 r^{-2} dr = b/2", ok17 and zero(J - bs / 2))
abs13 = mp.quad(lambda s: abs(mp.sin(s) * mp.sin(3 * s)), [0, mp.pi / 3, 2 * mp.pi / 3, mp.pi,
                                                              4 * mp.pi / 3, 5 * mp.pi / 3, 2 * mp.pi])
report("S18 int_0^{2pi} |sin th sin 3th| dth = 3 sqrt 3/2 > 0 (numerical)",
       abs(abs13 - 3 * mp.sqrt(3) / 2) < 1e-20, mp.nstr(abs13, 15))

# ---------------------------------------------------------------- 3.48 rearrangements
k, e0, a0p = sp.symbols("kappa eps0 a0p", positive=True)
Dp = sp.Symbol("Dp", positive=True)
Jv = lambda aa: aa / 4 - Dp
report("S19 (a) a0 = 2D gives J = -D/2; (A-1)/4 = D/2", zero(Jv(2 * Dp) + Dp / 2) and zero((A - 1) / 4 - D / 2))
report("S20 (b) J = -eps0 a0/4 exactly at a0 = 4D/(1+eps0) = 2(A-1)/(1+eps0)",
       zero(Jv(4 * Dp / (1 + e0)) + e0 * (4 * Dp / (1 + e0)) / 4) and zero(4 * D - 2 * (A - 1)))
report("S21 (c) J = -kappa a0 at a0 = 4D/(1+4kappa), J = kappa a0 at a0 = 4D/(1-4kappa)",
       zero(Jv(4 * Dp / (1 + 4 * k)) + k * 4 * Dp / (1 + 4 * k))
       and zero(Jv(4 * Dp / (1 - 4 * k)) - k * 4 * Dp / (1 - 4 * k)))
report("S22 (c) a0 < 0: |J| - kappa|a0| = D + |a0|(1/4 - kappa)",
       zero(sp.Abs(Jv(-a0p)) - k * a0p - (Dp + a0p * (sp.Rational(1, 4) - k))))

# ---------------------------------------------------------------- numerical tests of the moments
import numpy as np

_gl_x, _gl_w = np.polynomial.legendre.leggauss(60)
_edges = [0.02, 0.1, 0.2, 0.35, 0.5, 0.75, 1, 1.5, 2, 3, 4, 5.5, 7, 9]
_rn = np.concatenate([(b1 - a1) / 2 * _gl_x + (b1 + a1) / 2 for a1, b1 in zip(_edges[:-1], _edges[1:])])
_rw = np.concatenate([(b1 - a1) / 2 * _gl_w for a1, b1 in zip(_edges[:-1], _edges[1:])])
_nt = 512
_tn = 2 * np.pi * (np.arange(_nt) + 0.5) / _nt
_RR, _TT = np.meshgrid(_rn, _tn, indexing="ij")
_XX, _YY = _RR * np.cos(_TT), _RR * np.sin(_TT)


def polar_int(f, mval=None):
    """int_{R^2} f dX in polar coordinates (Gauss-Legendre in r on [0.02, 9], periodic rule in th).
    The test integrands are flat at 0 (factor exp(-1/r^2)) and decay like exp(-r^2), so the
    truncation errors are far below the tolerance."""
    vals = f(_XX, _YY) * _RR
    return float(np.sum(vals.sum(axis=1) * (2 * np.pi / _nt) * _rw))


# elliptic: P odd in x and y, V = P_xxx, H = (1/a) d_x Lap P, so Lap V = a H_xx
aval = sp.Rational(-3, 2)
mval = sp.Rational(7, 2)
P = x * y * sp.exp(-(x**2 + y**2) - 1 / (x**2 + y**2))
Vm = sp.diff(P, x, 3)
Hm = sp.diff(lap(P), x) / aval
report("N0 manufactured pair: Lap V - a H_xx = 0", zero(sp.simplify(lap(Vm) - aval * sp.diff(Hm, x, 2))))
w0m = w0.subs(m, mval)
fL = sp.lambdify((x, y), Vm * lap(w0m), "numpy")
fR = sp.lambdify((x, y), aval * Hm * sp.diff(w0m, x, 2), "numpy")
fJ = sp.lambdify((x, y), Vm * y * rr**(-2 * mval), "numpy")
fK = sp.lambdify((x, y), Hm * y * rr**(-2 * mval) * (2 * mval * x**2 / rr**2 - 1), "numpy")
vL, vR = polar_int(fL, mval), polar_int(fR, mval)
vJ, vK = polar_int(fJ, mval), polar_int(fK, mval)
pred = float(aval) / (2 * (float(mval) - 2)) * vK
report("N1 int V Lap w0 = a int H (w0)_xx and J_m = a/(2(m-2)) int H y r^{-2m}(2m x^2/r^2 - 1) (m = 7/2)",
       abs(vL - vR) < 1e-9 * (1 + abs(vL)) and abs(vJ - pred) < 1e-9 * (1 + abs(vJ)),
       "J = %.12g, prediction = %.12g, Green sides %.12g, %.12g" % (vJ, pred, vL, vR))

# transport: W = c_l X + U from a stream function, H flat, V := W.grad H - H
clv = sp.Rational(5, 3)
psi_m = -(clv - 1) * x * y + sp.Rational(1, 5) * x**3 * y * sp.exp(-(x**2 + y**2)) \
    - sp.Rational(2, 7) * x * y**3 / (1 + x**2 + y**2)
U1m, U2m = -sp.diff(psi_m, y), sp.diff(psi_m, x)
W1m, W2m = clv * x + U1m, clv * y + U2m
Hm2 = y * (1 + x**2) * sp.exp(-(x**2 + y**2) - 1 / (x**2 + y**2))
Vm2 = W1m * sp.diff(Hm2, x) + W2m * sp.diff(Hm2, y) - Hm2
Bm = (x * W1m + y * W2m) / rr**2
fJ2 = sp.lambdify((x, y), Vm2 * y * rr**(-2 * mval), "numpy")
fT2 = sp.lambdify((x, y), Hm2 * y * rr**(-2 * mval) * (2 * mval * Bm - 2 * clv - 1) - Hm2 * W2m * rr**(-2 * mval),
                  "numpy")
vJ2, vT2 = polar_int(fJ2, mval), polar_int(fT2, mval)
report("N2 J_m = int H y r^{-2m}(2mB - 2c_l - 1 - W_2/y) (manufactured, m = 7/2)",
       abs(vJ2 - vT2) < 1e-9 * (1 + abs(vJ2)), "J = %.12g, rhs = %.12g" % (vJ2, vT2))

nf = sum(1 for _, ok in results if not ok)
print("%d checks, %d failed" % (len(results), nf))
sys.exit(1 if nf else 0)
