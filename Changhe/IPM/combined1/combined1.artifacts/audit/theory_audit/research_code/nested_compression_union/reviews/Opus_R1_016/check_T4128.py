# c1-t1 R1-016: exact checks of the identities in T4-128, T4-130/T4-132, T4-133 (with BALL_LDL) and T4-138.
# Part 1 is exact (sympy). Part 2 tests the abstract inequalities on random matrices (FLOAT, illustration only).
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4128.py > check_T4128.out
import sympy as sp
import numpy as np

x, y, z, t, s, r, th = sp.symbols('x y z t s r theta', positive=True)
ok = []


def rep(name, cond):
    ok.append(bool(cond))
    print('%-72s %s' % (name, 'OK' if cond else 'FAIL'))


# 1. Poisson family. g = (z^2 + x^2 + y^2)^(-1/2) is harmonic in (x, y, z), so -d_z g is (-Lap)^(1/2) g.
g = (z**2 + x**2 + y**2) ** sp.Rational(-1, 2)
rep('g_z harmonic in (x,y,z)', sp.simplify(sp.diff(g, x, 2) + sp.diff(g, y, 2) + sp.diff(g, z, 2)) == 0)
rep('-d_z g_z = z (z^2 + r^2)^(-3/2)', sp.simplify(-sp.diff(g, z) - z * (z**2 + x**2 + y**2) ** sp.Rational(-3, 2)) == 0)


def fn(n):  # f_n as a function of (x, y), and of t = r^2
    e = sp.diff(g, z, n).subs(z, 1)
    return sp.simplify(e)


def ft(n):
    return sp.simplify(fn(n).subs({x: sp.sqrt(t), y: 0}))


lap = lambda e: sp.diff(e, x, 2) + sp.diff(e, y, 2)
for n in range(3):
    f, F = ft(n), ft(n + 1)
    fp, fpp = sp.diff(f, t), sp.diff(f, t, 2)
    H = -4 * (fp + t * fpp)
    X = {t: x**2 + y**2}
    rep('n=%d: h_n = -Lap f_n = -4(f_n\' + t f_n\'\')' % n, sp.simplify(-lap(fn(n)) - H.subs(X)) == 0)
    rep('n=%d: d_xy f_n = 4xy f_n\'\', d_xx f_n = 2 f_n\' + 4x^2 f_n\'\'' % n,
        sp.simplify(sp.diff(fn(n), x, y) - 4 * x * y * fpp.subs(X)) == 0
        and sp.simplify(sp.diff(fn(n), x, 2) - (2 * fp + 4 * x**2 * fpp).subs(X)) == 0)
    rep('n=%d: R1 h_n = -d_x f_(n+1) = -2x f_(n+1)\'' % n,
        sp.simplify(-sp.diff(fn(n + 1), x) + 2 * x * sp.diff(F, t).subs(X)) == 0)
f0 = ft(0)
H0 = sp.simplify(-4 * (sp.diff(f0, t) + t * sp.diff(f0, t, 2)))
rep('H_0 = (2 - t)(1 + t)^(-5/2)', sp.simplify(H0 - (2 - t) * (1 + t) ** sp.Rational(-5, 2)) == 0)
rep('G_00 = pi int_0^oo H_0^2 dt = 3 pi/4', sp.simplify(sp.pi * sp.integrate(H0**2, (t, 0, sp.oo)) - 3 * sp.pi / 4) == 0)


def AD(i, j):
    fi, fj, Fi, Fj = ft(i), ft(j), ft(i + 1), ft(j + 1)
    Hi = -4 * (sp.diff(fi, t) + t * sp.diff(fi, t, 2))
    Hj = -4 * (sp.diff(fj, t) + t * sp.diff(fj, t, 2))
    A = -2 * (Hi * sp.diff(fj, t, 2) + Hj * sp.diff(fi, t, 2)) - 4 * sp.diff(Fi, t) * sp.diff(Fj, t)
    D = Hi * sp.diff(fj, t) + Hj * sp.diff(fi, t)
    return sp.simplify(A), sp.simplify(D)


A00, D00 = AD(0, 0)
rep('C_00 = A_00 + 2 D_00\' = 3(1 - t)(1 + t)^(-5)', sp.simplify(A00 + 2 * sp.diff(D00, t) - 3 * (1 - t) * (1 + t) ** -5) == 0)

# 2. Formula (3): the a and b coefficients of <K h_j, h_i> from the commutator expansion
#    (R1* = -R1, R1^2 = U2, R1 R2 = -U1), written as the T4-130 kernels, equal the radial kernels xy A and D - x^2 A.
for (i, j) in [(0, 0), (0, 1), (1, 2)]:
    X = {t: x**2 + y**2}
    hs, U1, U2, v1, v2 = [], [], [], [], []
    for n in (i, j):
        f, F = ft(n), ft(n + 1)
        hs.append((-4 * (sp.diff(f, t) + t * sp.diff(f, t, 2))).subs(X))
        U1.append((-4 * x * y * sp.diff(f, t, 2)).subs(X))
        U2.append((2 * sp.diff(f, t) + 4 * x**2 * sp.diff(f, t, 2)).subs(X))
        v1.append((-2 * x * sp.diff(F, t)).subs(X))
        v2.append((-2 * y * sp.diff(F, t)).subs(X))
    Aang = (hs[0] * U1[1] + hs[1] * U1[0] - v1[0] * v2[1] - v2[0] * v1[1]) / 2
    Bang = (hs[0] * U2[1] + hs[1] * U2[0]) / 2 + v1[0] * v1[1]
    A, D = AD(i, j)
    rep('(i,j)=(%d,%d): T4-130 kernels = T4-128 kernels xyA, D - x^2 A' % (i, j),
        sp.simplify(Aang - x * y * A.subs(X)) == 0 and sp.simplify(Bang - (D - x**2 * A).subs(X)) == 0)

# 3. Divergence identity d_x(xy A) + d_y(D - x^2 A) = y (A + 2 D'), generic A, D of t = r^2.
Af, Df = sp.Function('A'), sp.Function('D')
w = x**2 + y**2
lhs = sp.diff(x * y * Af(w), x) + sp.diff(Df(w) - x**2 * Af(w), y)
rhs = y * (Af(w) + 2 * sp.diff(Df(t), t).subs(t, w))
rep('d_x(xyA) + d_y(D - x^2 A) = y(A + 2D\')', sp.simplify(sp.expand(lhs - rhs)) == 0)

# 4. Beta moments. int_0^oo t^(l+1)(1+t)^(-a-l-k) dt = B(l+2, k+a-2) (radial, T4-128 (4));
#    (1/2) int_0^oo s^(q+l)(1+s)^(-a-p-l) ds = B(q+l+1, p+a-q-1)/2 (angular, T4-130 (4)).
for (a, l, k) in [(sp.Rational(7, 5), 0, 3), (sp.Rational(9, 10), 2, 4), (sp.Rational(1, 3), 1, 3)]:
    I1 = sp.integrate(t ** (l + 1) * (1 + t) ** (-a - l - k), (t, 0, sp.oo))
    rep('radial moment a=%s l=%d k=%d' % (a, l, k), sp.gammasimp(I1 - sp.beta(l + 2, k + a - 2)) == 0)
for (a, l, p, q) in [(sp.Rational(7, 5), 1, 5, 1), (sp.Rational(1, 2), 0, 4, 2)]:
    I2 = sp.integrate(s ** (q + l) * (1 + s) ** (-a - p - l), (s, 0, sp.oo)) / 2
    rep('angular moment a=%s l=%d p=%d q=%d' % (a, l, p, q), sp.gammasimp(I2 - sp.beta(q + l + 1, p + a - q - 1) / 2) == 0)
# 5. Angular integral formula.
for (a, b) in [(0, 0), (1, 0), (1, 1), (2, 1), (3, 2)]:
    I = sp.integrate(sp.cos(th) ** (2 * a) * sp.sin(th) ** (2 * b), (th, 0, 2 * sp.pi)) / sp.pi
    fo = 2 * sp.factorial(2 * a) * sp.factorial(2 * b) / (4 ** (a + b) * sp.factorial(a) * sp.factorial(b) * sp.factorial(a + b))
    rep('pi^-1 int cos^%d sin^%d = formula' % (2 * a, 2 * b), sp.simplify(I - fo) == 0)
# 6. Parities of C_m f and S_m f (f radial): C_m f is ((-1)^m, +), S_m f is ((-1)^(m+1), -).
f = fn(0)
for m in range(1, 5):
    P_, Q_ = sp.symbols('P_ Q_', real=True)
    e = sp.expand((P_ + sp.I * Q_) ** m)
    def Dm(part):
        out = 0
        for term in sp.Add.make_args(sp.expand(part)):
            c, mono = term.as_coeff_Mul()
            pp, qq = sp.degree(mono, P_), sp.degree(mono, Q_)
            out += c * sp.diff(f, x, pp, y, qq) if pp + qq else c * f
        return out
    Cm, Sm = Dm(sp.re(e).expand()), Dm(sp.im(e).expand())
    def par(e2):
        px = sp.simplify(e2.subs(x, -x) - e2) == 0 and 1 or (sp.simplify(e2.subs(x, -x) + e2) == 0 and -1)
        py = sp.simplify(e2.subs(y, -y) - e2) == 0 and 1 or (sp.simplify(e2.subs(y, -y) + e2) == 0 and -1)
        return px, py
    rep('m=%d: parity C_m f = ((-1)^m, +), S_m f = ((-1)^(m+1), -)' % m,
        par(Cm) == ((-1) ** m, 1) and par(Sm) == ((-1) ** (m + 1), -1))

# 7. BALL_LDL congruence: qG - B = (L D^(1/2)) (qI - C) (L D^(1/2))^T with C = D^(-1/2) L^-1 B L^-T D^(-1/2).
Gm = sp.Matrix([[3, 1, 0], [1, 4, 1], [0, 1, 5]]) / 7
Bm = sp.Matrix([[1, 2, -1], [2, 0, 3], [-1, 3, 2]]) / 11
L, Dd = Gm.LDLdecomposition()
Dh = sp.diag(*[sp.sqrt(Dd[i, i]) for i in range(3)])
Cm = Dh.inv() * L.inv() * Bm * L.inv().T * Dh.inv()
qq = sp.Rational(3, 2)
rep('BALL_LDL congruence identity (exact 3x3 example)',
    sp.simplify((L * Dh) * (qq * sp.eye(3) - Cm) * (L * Dh).T - (qq * Gm - Bm)) == sp.zeros(3, 3))

# Part 2 (FLOAT): random self-adjoint matrices as stand-ins for K on a finite-dimensional space.
rng = np.random.default_rng(20261029)
worst = {'T4-128': -1e9, 'T4-133': -1e9, 'T4-138': -1e9}
for trial in range(2000):
    n = 14
    M = rng.standard_normal((n, n)); K = (M + M.T) / 2
    if trial % 2:
        K += 3 * np.outer(v := rng.standard_normal(n), v) / n   # some trials with a large positive eigenvalue
    hs2 = np.sum(K * K)
    H = list(range(6)); O = list(range(6, n))                # "target" block and complement (block-diagonal K)
    K[np.ix_(H, O)] = 0; K[np.ix_(O, H)] = 0
    hs2 = np.sum(K * K); AH = K[np.ix_(H, H)]
    S = rng.standard_normal((len(O), 3)); G = S.T @ S; B = S.T @ K[np.ix_(O, O)] @ S   # nonorthogonal family
    T = np.trace(np.linalg.solve(G, B) @ np.linalg.solve(G, B))
    worst['T4-128'] = max(worst['T4-128'], np.linalg.norm(AH, 2) ** 2 - (hs2 - T))
    Sh = rng.standard_normal((len(H), 2)); Gh = Sh.T @ Sh; Bh = Sh.T @ AH @ Sh
    Th = np.trace(np.linalg.solve(Gh, Bh) @ np.linalg.solve(Gh, Bh))
    qv = max(0.0, np.max(np.linalg.eigvals(np.linalg.solve(Gh, Bh)).real))
    lam1 = max(0.0, np.max(np.linalg.eigvalsh(AH)))
    worst['T4-133'] = max(worst['T4-133'], lam1 ** 2 - (hs2 - T - Th + qv ** 2))
    # T4-138: commuting projections P = span(e0..e3), Q = span(e2..e6) on R^n; R = span(e2, e3). K need not be symmetric.
    Kn = rng.standard_normal((n, n))
    P = np.diag([1.0 if i < 4 else 0 for i in range(n)]); Q = np.diag([1.0 if 2 <= i < 7 else 0 for i in range(n)])
    U = np.linalg.qr(rng.standard_normal((n, n)))[0]; P, Q = U @ P @ U.T, U @ Q @ U.T; Rr = P @ Q
    hs = lambda X: np.sum(X * X)
    worst['T4-138'] = max(worst['T4-138'], hs(P @ Kn @ P) + hs(Q @ Kn @ Q) - hs(Rr @ Kn @ Rr) - hs(Kn))
for k, v in worst.items():
    rep('%s: max over 2000 random trials of (left side - bound) = %.3e <= 1e-9' % (k, v), v <= 1e-9)
print('all checks', 'PASS' if all(ok) else 'FAIL', '(%d of %d)' % (sum(ok), len(ok)))
