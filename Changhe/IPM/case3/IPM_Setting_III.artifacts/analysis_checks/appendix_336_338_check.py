"""Checks for the proofs A.3.36, A.3.37, A.3.38.

Exact (sympy) checks of algebraic identities and numerical (mpmath / numpy) checks of
integrals.  These checks support, but do not replace, the written proofs.
Run with OMP_NUM_THREADS=1.
"""
import itertools
import math

import mpmath as mp
import numpy as np
import sympy as sp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


# ---------------------------------------------------------------- 3.36
# Lambda = largest eigenvalue of [[1, 9/2], [9/2, 3/sqrt 2]]
M = sp.Matrix([[1, sp.Rational(9, 2)], [sp.Rational(9, 2), 3 / sp.sqrt(2)]])
lam = max(M.eigenvals().keys(), key=lambda e: float(e))
report("3.36 Lambda", abs(float(lam) - 6.0954523) < 1e-7, "Lambda = %.10f" % float(lam))
# quadratic form bound: x^2 + 9 x y + (3/sqrt2) y^2 <= Lambda (x^2 + y^2)
x, y = sp.symbols("x y", real=True)
Q = sp.Matrix([[lam, 0], [0, lam]]) - M
report("3.36 Lambda I - M psd", all(float(e) >= -1e-12 for e in Q.eigenvals().keys()))

# worst case of 1 - D <= a + 9 sqrt(a sqrt(2 D^2 + a^2/2)) on 0 < D <= 1/2, 0 < a <= 1/400
def rhs(D, a):
    return a + 9 * mp.sqrt(a * mp.sqrt(2 * D**2 + a**2 / 2))

worst = rhs(mp.mpf(1) / 2, mp.mpf(1) / 400)
report("3.36 worst-case RHS", worst < 0.381, "RHS(1/2, 1/400) = %s" % mp.nstr(worst, 10))
R = sp.Rational
ok = (2 * R(1, 4) + R(1, 400) ** 2 / 2 < R(71, 100) ** 2) and (R(1, 400) * R(71, 100) < R(17, 400) ** 2)
report("3.36 rational chain 71/100, 17/400", ok and R(1, 400) + 9 * R(17, 400) == R(154, 400))
grid_ok = True
for D in np.linspace(1e-6, 0.5, 201):
    for a in np.linspace(1e-9, 1 / 400, 101):
        if not (1 - D > float(rhs(D, a))):
            grid_ok = False
report("3.36 grid 1 - D > RHS", grid_ok)

# trace-free 2x2: |M|_F^2 = |S|_F^2 + curl^2/2 and |S|_op = |S|_F/sqrt 2
p_, q_, w_ = sp.symbols("p q w", real=True)
DU = sp.Matrix([[p_, q_ - w_ / 2], [q_ + w_ / 2, -p_]])  # rows: components, d_y U1 = q - w/2, d_x U2 = q + w/2
S = (DU + DU.T) / 2
curl = DU[1, 0] - DU[0, 1]
fro = lambda A: sum(e**2 for e in A)
report("3.36 Frobenius split", sp.simplify(fro(DU) - fro(S) - curl**2 / 2) == 0)
ev = list(S.eigenvals().keys())
report("3.36 |S|_op^2 = |S|_F^2/2", all(sp.simplify(e**2 - fro(S) / 2) == 0 for e in ev))

# slot contraction: first-order commutator group equals sum_l w^T S w
rng = np.random.default_rng(1)
k = 3
ok = True
for trial in range(50):
    g = rng.normal(size=(2,) * k)
    f = sum(np.transpose(g, perm) for perm in itertools.permutations(range(k))) / math.factorial(k)
    A = rng.normal(size=(2, 2))
    A[1, 1] = -A[0, 0]  # trace free; A[m, i] = d_i U_m
    Ssym = (A + A.T) / 2
    tot = 0.0
    for I in itertools.product(range(2), repeat=k):
        for l in range(k):
            for m in range(2):
                J = list(I)
                J[l] = m
                tot += f[I] * A[m, I[l]] * f[tuple(J)]
    tot_S = 0.0
    for I in itertools.product(range(2), repeat=k):
        for l in range(k):
            for m in range(2):
                J = list(I)
                J[l] = m
                tot_S += f[I] * Ssym[m, I[l]] * f[tuple(J)]
    bound = k * np.max(np.abs(np.linalg.eigvalsh(Ssym))) * np.sum(f**2)
    ok = ok and abs(tot - tot_S) < 1e-10 and abs(tot) <= bound + 1e-12
report("3.36 slot contraction (k = 3)", ok)

# interpolation constant 3 on a sample field v = (1 + r^2)^(-0.3) (scalar), grid quadrature
n = 1601
L = 200.0
xs = np.linspace(-L, L, n)
h = xs[1] - xs[0]
X, Y = np.meshgrid(xs, xs, indexing="ij")
r2 = X**2 + Y**2
th = 0.3
v = (1 + r2) ** (-th)
vx = -2 * th * X * (1 + r2) ** (-th - 1)
vy = -2 * th * Y * (1 + r2) ** (-th - 1)
c2 = 4 * th * (th + 1) * (1 + r2) ** (-th - 2)
vxx = c2 * X**2 - 2 * th * (1 + r2) ** (-th - 1)
vyy = c2 * Y**2 - 2 * th * (1 + r2) ** (-th - 1)
vxy = c2 * X * Y
lhs = np.sqrt(np.sum((vx**2 + vy**2) ** 2) * h * h)
rhs3 = 3 * 1.0 * np.sqrt(np.sum(vxx**2 + 2 * vxy**2 + vyy**2) * h * h)
report("3.36 interpolation sample", lhs <= rhs3, "||Dv||_4^2 = %.4f, 3||v||_inf||D^2v||_2 = %.4f" % (lhs, rhs3))

# Remark 3: base density rho_b = 4 D y F0(r), stream psi_b = 2 z(r) x y, z = -(a/2) r^-4 int_0^r s^3 F0
mp.mp.dps = 30


def smoothstep(t):
    # C^infinity, 0 for t <= 0, 1 for t >= 1
    if t <= 0:
        return mp.mpf(0)
    if t >= 1:
        return mp.mpf(1)
    e1 = mp.e ** (-1 / t)
    e2 = mp.e ** (-1 / (1 - t))
    return e1 / (e1 + e2)


Dv = mp.mpf("0.3")
pexp = 1 / (1 + Dv)
a_b = 4 * Dv


def F0(s):
    lam_ = smoothstep(s - 1)
    return (1 - lam_) * 1 + lam_ * s ** (pexp - 1)


def dF0(s):
    return mp.diff(F0, s)


def psi1_modal(rho1, rho3, r):
    # derivative-free modal form for n = 1 (m = 2)
    t1 = r**2 * mp.quad(lambda s: s ** (-2) * rho3(s), [r, 2, 3, mp.inf])
    t2 = r ** (-2) * mp.quad(lambda s: s**2 * rho1(s), [0, min(r, 1), r] if r > 1 else [0, r])
    return (t1 - t2) / 2


def psi1_fform(rho1, rho3, r, cuts):
    # f_n form: psi_1 = (1/4)[r^-2 int_0^r s^3 f_1 + r^2 int_r^inf s^-1 f_1]
    def f1(s):
        return (mp.diff(rho1, s) - rho1(s) / s + mp.diff(rho3, s) + 3 * rho3(s) / s) / 2

    inner = [c for c in cuts if 0 < c < r]
    outer = [c for c in cuts if c > r]
    I1 = mp.quad(lambda s: s**3 * f1(s), [mp.mpf("1e-30")] + inner + [r])
    I2 = mp.quad(lambda s: f1(s) / s, [r] + outer + [mp.inf])
    return (I1 / r**2 + r**2 * I2) / 4


ok = True
for rr in [mp.mpf("0.5"), mp.mpf("1.5"), mp.mpf("2.5"), mp.mpf(4)]:
    z_formula = -(a_b / 2) * rr ** (-4) * mp.quad(lambda s: s**3 * F0(s), [0, 1, 2, rr] if rr > 2 else ([0, 1, rr] if rr > 1 else [0, rr]))
    z_modal = psi1_modal(lambda s: a_b * s * F0(s), lambda s: 0 * s, rr) / rr**2
    ok = ok and abs(z_formula - z_modal) < 1e-12 and (-a_b / 8 - 1e-20 <= z_formula <= 0)
report("3.36 remark-3 base stream z = -(a/2)H, -a/8 <= z <= 0", ok)

# ---------------------------------------------------------------- 3.37 (iii)
Dq = mp.mpf("0.3")
aq = mp.mpf("0.7")


def chi(t):
    return 1 - smoothstep(t - 1)


def eta(t):
    if t <= 2 or t >= 3:
        return mp.mpf(0)
    return mp.e ** (-1 / ((t - 2) * (3 - t)))


Jq = mp.quad(lambda t: eta(t) / t, [2, 3])
bq = (aq / 4 - Dq) / Jq
rho1 = lambda s: aq * s * chi(s)
rho3 = lambda s: bq * s * eta(s)
ok = True
for rr in [mp.mpf("0.2"), mp.mpf("0.6"), mp.mpf("0.95")]:
    p1 = psi1_modal(rho1, rho3, rr)
    p1f = psi1_fform(rho1, rho3, rr, [1, 2, 3])
    ok = ok and abs(p1 + Dq * rr**2 / 2) < 1e-15 and abs(p1f + Dq * rr**2 / 2) < 1e-12
report("3.37(iii) psi_1 = -D r^2/2 on B_L (both modal forms)", ok)


def psi2_fform(r):
    def f2(s):
        return (mp.diff(rho3, s) - 3 * rho3(s) / s) / 2

    I1 = 0 if r <= 2 else mp.quad(lambda s: s**5 * f2(s), [2, min(r, 3)])
    I2 = mp.quad(lambda s: f2(s) / s**3, [max(r, 2), 3]) if r < 3 else 0
    return (I1 / r**4 + r**4 * I2) / 8


ok = all(abs(psi2_fform(mp.mpf(rr))) < 1e-15 for rr in ["0.3", "0.9", "1.7"])
report("3.37(iii) psi_2 = 0 on B_L", ok)

# independent real-space check of v_L at points of B_1 (L = 1) via the kernel of 3.1(ii)
Df, af = float(Dq), float(aq)
bf = float(bq)


def smoothstep_np(t):
    t = np.clip(t, 0.0, 1.0)
    out = np.zeros_like(t)
    m = (t > 0) & (t < 1)
    e1 = np.exp(-1 / t[m])
    e2 = np.exp(-1 / (1 - t[m]))
    out[m] = e1 / (e1 + e2)
    out[t >= 1] = 1.0
    return out


def eta_np(t):
    out = np.zeros_like(t)
    m = (t > 2) & (t < 3)
    out[m] = np.exp(-1 / ((t[m] - 2) * (3 - t[m])))
    return out


def q1_np(X1, X2):
    r = np.sqrt(X1**2 + X2**2)
    th = np.arctan2(X2, X1)
    return af * X2 * (1 - smoothstep_np(r - 1)) + bf * r * np.sin(3 * th) * eta_np(r)


def velocity(X0):
    R0 = 4.5
    nt, nphi = 3000, 512
    tg, tw = np.polynomial.legendre.leggauss(nt)
    t = (tg + 1) * R0 / 2
    wt = tw * R0 / 2
    phi = np.arange(nphi) * 2 * np.pi / nphi
    T, P = np.meshgrid(t, phi, indexing="ij")
    Z1, Z2 = T * np.cos(P), T * np.sin(P)
    rho0 = q1_np(np.array([X0[0]]), np.array([X0[1]]))[0]
    diff = q1_np(X0[0] - Z1, X0[1] - Z2) - rho0
    K1 = -np.cos(P) * np.sin(P) / (np.pi * T**2)
    K2 = (np.cos(P) ** 2 - np.sin(P) ** 2) / (2 * np.pi * T**2)
    wgt = (wt[:, None] * T) * (2 * np.pi / nphi)
    U1 = np.sum(K1 * diff * wgt)
    U2 = -rho0 / 2 + np.sum(K2 * diff * wgt)
    return U1, U2


errs = []
for X0 in [(0.3, 0.2), (-0.5, 0.4), (0.1, -0.7)]:
    U1, U2 = velocity(X0)
    errs.append(max(abs(U1 - Df * X0[0]), abs(U2 + Df * X0[1])))
report("3.37(iii) real-space v_L = (Dx, -Dy) on B_1", max(errs) < 2e-6, "max error %.2e" % max(errs))

# ---------------------------------------------------------------- 3.38
A, a, d = sp.symbols("A a d", positive=True)
B = A - 1
u = (d - A) / B
vv = (a + 2 - A * (d + 1)) / B
py = (a - d + 1) / B
kx = (A * d - 1) / B
report("3.38 u + v - a/B = -d - 2", sp.simplify(u + vv - a / B + d + 2) == 0)
report("3.38 p_y = d + v + 1", sp.simplify(py - d - vv - 1) == 0)
report("3.38 kappa_x - d = (d - 1)/B", sp.simplify(kx - d - (d - 1) / B) == 0)
report("3.38 crossing d = (a+1)/A", sp.simplify(py.subs(d, (a + 1) / A) - (a + 1) / A) == 0)
report("3.38 a/B - (a+1)/A = (a - B)/(A B)", sp.simplify(a / B - (a + 1) / A - (a - B) / (A * B)) == 0)

# Fourier quadrant solution of [A xi d_xi + eta d_eta + A + 2 + a xi^2/|xi|^2] F = 0
xi, et = sp.symbols("xi eta", positive=True)
qv = et / xi
F = xi ** (-d - 2) * (1 + qv**2) ** (-a / (2 * B)) * qv**vv
op = A * xi * sp.diff(F, xi) + et * sp.diff(F, et) + (A + 2) * F + a * xi**2 / (xi**2 + et**2) * F
report("3.38 Fourier quadrant solution", sp.simplify(op / F) == 0)

# Fourier transform of the frozen equation (convention hat f = int f e^{-i X.xi}):
# check on a Gaussian test pair that hat[(A x d_x + y d_y - 1) h] = -(A xi1 d1 + xi2 d2 + A + 2) hat h
X1, X2, k1, k2 = sp.symbols("x1 x2 k1 k2", real=True)
hg = X2 * sp.exp(-(X1**2 + 2 * X2**2) / 2)
lhs_phys = A * X1 * sp.diff(hg, X1) + X2 * sp.diff(hg, X2) - hg


def ft(fun):
    return sp.simplify(
        sp.integrate(sp.integrate(fun * sp.exp(-sp.I * (X1 * k1 + X2 * k2)), (X1, -sp.oo, sp.oo)), (X2, -sp.oo, sp.oo))
    )


Hg = ft(hg)
lhs_four = ft(lhs_phys)
rhs_four = -(A * k1 * sp.diff(Hg, k1) + k2 * sp.diff(Hg, k2) + (A + 2) * Hg)
report("3.38 Fourier transform of transport operator", sp.simplify(lhs_four - rhs_four) == 0)

# angular system: h = r^d Theta, psi = r^(d+1) Phi
r, t = sp.symbols("r t", positive=True)
Th = sp.Function("Theta")
Ph = sp.Function("Phi")
xx, yy = r * sp.cos(t), r * sp.sin(t)
hh = r**d * Th(t)
pp = r ** (d + 1) * Ph(t)


def dx(fn):
    return sp.cos(t) * sp.diff(fn, r) - sp.sin(t) / r * sp.diff(fn, t)


def dy(fn):
    return sp.sin(t) * sp.diff(fn, r) + sp.cos(t) / r * sp.diff(fn, t)


transport = A * xx * dx(hh) + yy * dy(hh) - hh + a * dx(pp)
c_, z_ = sp.cos(t), sp.sin(t)
qq = A * c_**2 + z_**2
eq13a = (d * qq - 1) * Th(t) - B * z_ * c_ * sp.diff(Th(t), t) + a * ((d + 1) * c_ * Ph(t) - z_ * sp.diff(Ph(t), t))
report("3.38 angular transport equation", sp.simplify(transport / r**d - eq13a) == 0)
lap = sp.diff(pp, r, 2) + sp.diff(pp, r) / r + sp.diff(pp, t, 2) / r**2
poisson = -lap - dx(hh)
eq13b = sp.diff(Ph(t), t, 2) - (z_ * sp.diff(Th(t), t) - d * c_ * Th(t) - (d + 1) ** 2 * Ph(t))
report("3.38 angular Poisson equation", sp.simplify(poisson / r ** (d - 1) + eq13b) == 0)

# residues: first-order system Y = (Theta, Phi, Phi'), t Y' = R(t) Y
T0, P0, P1 = sp.symbols("T0 P0 P1")
Thp = ((d * qq - 1) * T0 + a * ((d + 1) * c_ * P0 - z_ * P1)) / (B * z_ * c_)
Ppp = z_ * Thp - d * c_ * T0 - (d + 1) ** 2 * P0
rows = [sp.expand(t * Thp), t * P1, sp.expand(t * Ppp)]
Rx = sp.Matrix([[sp.limit(sp.diff(rw, var), t, 0) for var in (T0, P0, P1)] for rw in rows])
report(
    "3.38 residue at x-axis",
    sp.simplify(Rx - sp.Matrix([[kx, a * (d + 1) / B, 0], [0, 0, 0], [0, 0, 0]])) == sp.zeros(3, 3),
)
# vertical axis: s = pi/2 - theta, Y = (Theta, Phi, dPhi/ds); d/dtheta = -d/ds
s_ = sp.symbols("s", positive=True)
sub = {t: sp.pi / 2 - s_}
Thp_s = -(Thp.subs(sub)).subs(P1, -P1)  # dTheta/ds with Phi_theta = -Phi_s
Pss = (Ppp.subs(sub)).subs(P1, -P1)  # Phi_ss = Phi_thth
rows_s = [sp.expand(s_ * Thp_s), s_ * P1, sp.expand(s_ * Pss)]
Ry = sp.Matrix([[sp.limit(sp.simplify(sp.diff(rw, var)), s_, 0) for var in (T0, P0, P1)] for rw in rows_s])
Ry_exp = sp.Matrix([[-(d - 1) / B, 0, -a / B], [0, 0, 0], [(d - 1) / B, 0, a / B]])
report("3.38 residue at y-axis", sp.simplify(Ry - Ry_exp) == sp.zeros(3, 3))
report("3.38 eigenvalues", sp.simplify(Ry.trace() - py) == 0 and sp.simplify(Rx.trace() - kx) == 0
       and Rx.rank() == 1 and Ry.rank() == 1)
report("3.38 y-axis eigenvector (1,0,-1)", sp.simplify(Ry * sp.Matrix([1, 0, -1]) - py * sp.Matrix([1, 0, -1])) == sp.zeros(3, 1))

# frequency-axis example h = y |x|^p, psi = -y x |x|^p/(p+1), a = A p, d = p + 1 (x > 0 branch)
pp_ = sp.symbols("p", positive=True)
xp, yv = sp.symbols("x y", positive=True)
he = yv * xp**pp_
pse = -yv * xp * xp**pp_ / (pp_ + 1)
tr = A * xp * sp.diff(he, xp) + yv * sp.diff(he, yv) - he + A * pp_ * sp.diff(pse, xp)
po = -(sp.diff(pse, xp, 2) + sp.diff(pse, yv, 2)) - sp.diff(he, xp)
pyex = (A * pp_ - (pp_ + 1) + 1) / (A - 1)
report("3.38 example y|x|^p", sp.simplify(tr) == 0 and sp.simplify(po) == 0 and sp.simplify(pyex - pp_) == 0)

print()
print("%d checks, %d failed" % (len(results), sum(1 for _, ok in results if not ok)))
