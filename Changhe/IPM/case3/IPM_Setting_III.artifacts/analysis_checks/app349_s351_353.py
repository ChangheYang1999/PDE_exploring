#!/usr/bin/env python3
# Symbolic checks for the appendix entries 3.51(c),(d), 3.53 and the 3.50(d) bump constants.
import sympy as sp
from fractions import Fraction as Fr

x, y, a, A, t, s, lam, th, chi, eta, j = sp.symbols('x y a A t s lam th chi eta j', real=True)
res = []


def chk(name, cond):
    res.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)


def Lop(f):
    return sp.expand(A * x * sp.diff(f, x) + y * sp.diff(f, y) - f)


def lap(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2)


# 3.51(c): leading equations <-> recurrence, for n = 3, 5, 7, 9
for n in (3, 5, 7, 9):
    K = (n - 1) // 2
    c = sp.symbols('c0:%d' % (K + 1))
    Hn = sum(c[i] * x**(2 * i) * y**(n - 2 * i) for i in range(K + 1))
    expr = sp.expand(lap(Lop(Hn)) - a * sp.diff(Hn, x, 2))
    e = [n - 1 + 2 * i * (A - 1) for i in range(K + 1)]
    ok = True
    for i in range(K):
        coeff = sp.Poly(expr, x, y).coeff_monomial(x**(2 * i) * y**(n - 2 - 2 * i))
        rec = (n - 2 * i) * (n - 2 * i - 1) * e[i] * c[i] + (2 * i + 2) * (2 * i + 1) * (e[i + 1] - a) * c[i + 1]
        ok = ok and sp.expand(coeff - rec) == 0
    # no other monomials
    tot = sum(sp.Poly(expr, x, y).coeff_monomial(x**(2 * i) * y**(n - 2 - 2 * i)) * x**(2 * i) * y**(n - 2 - 2 * i)
              for i in range(K))
    ok = ok and sp.expand(expr - tot) == 0
    chk('3.51c recurrence equals Lap L H - a H_xx, n=%d' % n, ok)
    # commutator form
    comm = sp.expand(lap(Lop(Hn)) - a * sp.diff(Hn, x, 2)
                     - ((Lop(lap(Hn)) + 2 * lap(Hn)) + (2 * (A - 1) - a) * sp.diff(Hn, x, 2)))
    chk('3.51c commutator (L+2)Lap H + (2(A-1)-a)H_xx, n=%d' % n, comm == 0)
    # c0 formula from solving downward with cK = 1
    sol = {c[K]: 1}
    for i in range(K - 1, -1, -1):
        sol[c[i]] = sp.simplify(-(2 * i + 2) * (2 * i + 1) * (e[i + 1] - a) * sol[c[i + 1]]
                                / ((n - 2 * i) * (n - 2 * i - 1) * e[i]))
    c0f = sp.prod([a - e[i] for i in range(1, K + 1)]) / ((2 * K + 1) * sp.prod([e[i] for i in range(K)]))
    chk('3.51c c0 formula n=%d' % n, sp.simplify(sol[c[0]] - c0f) == 0)
    # F_j solves the recurrence in eta/chi form
    etav = sp.Rational(K) / (A - 1)
    chiv = 1 + (2 * K - a) / (2 * (A - 1))
    F = [(-1)**i * sp.binomial(n, 2 * i) * sp.rf(etav, i) * sp.rf(chiv + i, K - i) for i in range(K + 1)]
    ok = all(sp.simplify((n - 2 * i) * (n - 2 * i - 1) * e[i] * F[i]
                         + (2 * i + 2) * (2 * i + 1) * (e[i + 1] - a) * F[i + 1]) == 0 for i in range(K))
    chk('3.51c F_j solves recurrence n=%d' % n, ok)
    chk('3.51c e_K = (n-1)A, n=%d' % n, sp.expand(e[K] - (n - 1) * A) == 0)
    chk('3.51c e_j = 2(A-1)(eta+j), e_{j+1}-a = 2(A-1)(chi+j), n=%d' % n,
        all(sp.simplify(e[i] - 2 * (A - 1) * (etav + i)) == 0 for i in range(K + 1)) and
        all(sp.simplify(e[i + 1] - a - 2 * (A - 1) * (chiv + i)) == 0 for i in range(K)))
    u = chiv + K - 1
    chk('3.51c u = ((n-1)A - a)/(2(A-1)), n=%d' % n, sp.simplify(u - ((n - 1) * A - a) / (2 * (A - 1))) == 0)

# identities and K-th differences, K = 1..6
for K in range(1, 7):
    ok1 = all(sp.binomial(2 * K + 1, 2 * jj) * sp.rf(sp.Rational(1, 2), jj) * sp.rf(sp.Rational(3, 2), K - jj)
              / sp.rf(sp.Rational(3, 2), K) == sp.binomial(K, jj) for jj in range(K + 1))
    chk('binomial-Pochhammer identity K=%d' % K, ok1)
    u = chi + K - 1
    ok2 = all(sp.expand(sp.rf(chi + jj, K - jj) * sp.rf(u, jj) - (chi + K - 1) * sp.rf(chi + jj, K - 1)) == 0
              for jj in range(K + 1))
    chk('Pochhammer product identity K=%d' % K, ok2)
    d = sp.expand(sum((-1)**jj * sp.binomial(K, jj) * sp.rf(chi + jj, K - 1) for jj in range(K + 1)))
    chk('K-th difference vanishes K=%d' % K, d == 0)
    # full expectation with symbolic moments: E F_chi(TS) = 0
    n = 2 * K + 1
    uu = sp.Symbol('u', positive=True)
    et = sp.Symbol('et', positive=True)
    ch = uu - K + 1
    ET = [sp.rf(uu, jj) * sp.rf(sp.Rational(3, 2), K - jj) / sp.rf(sp.Rational(3, 2), K) for jj in range(K + 1)]
    ES = [sp.rf(sp.Rational(1, 2), jj) / sp.rf(et, jj) for jj in range(K + 1)]
    Fj = [(-1)**jj * sp.binomial(n, 2 * jj) * sp.rf(et, jj) * sp.rf(ch + jj, K - jj) for jj in range(K + 1)]
    chk('E F_chi(TS) = 0 symbolically K=%d' % K, sp.simplify(sum(Fj[i] * ET[i] * ES[i] for i in range(K + 1))) == 0)

# moments of BetaPrime and Beta (numeric spot checks with exact integrals)
uu, KK = sp.Rational(7, 3), 2
for jj in range(KK + 1):
    xx = sp.Symbol('xx', positive=True)
    m = sp.integrate(xx**(uu - 1 + jj) * (1 + xx)**(-uu - KK - sp.Rational(3, 2)), (xx, 0, sp.oo)) / \
        sp.beta(uu, KK + sp.Rational(3, 2))
    chk('BetaPrime moment j=%d' % jj, sp.simplify(sp.gammasimp(m - sp.rf(uu, jj) * sp.rf(sp.Rational(3, 2), KK - jj)
                                                               / sp.rf(sp.Rational(3, 2), KK))) == 0)
et0 = sp.Rational(5, 2)
for jj in range(4):
    xx = sp.Symbol('xx', positive=True)
    m = sp.integrate(xx**(jj - sp.Rational(1, 2)) * (1 - xx)**(et0 - sp.Rational(3, 2)), (xx, 0, 1)) / \
        (sp.gamma(sp.Rational(1, 2)) * sp.gamma(et0 - sp.Rational(1, 2)) / sp.gamma(et0))
    chk('Beta moment j=%d' % jj, sp.simplify(sp.gammasimp(sp.expand_func(m)) - sp.rf(sp.Rational(1, 2), jj)
                                             / sp.rf(et0, jj)) == 0)

# quintic
e0, e1, e2 = 4, 2 * A + 2, 4 * A
c2 = sp.Integer(1)
c1 = 2 * (a - e2) / e1
c0 = (a - e1) * (a - e2) / (20 * e1)
H5 = c0 * y**5 + c1 * x**2 * y**3 + c2 * x**4 * y
chk('quintic P solves leading equations', sp.simplify(lap(Lop(H5)) - a * sp.diff(H5, x, 2)) == 0)
disc = c1**2 - 4 * c0
beta_a = (18 - 2 * A) * a + 4 * A**2 - 72 * A + 4
chk('discriminant = -(4(e2-a)/e1^2) beta(a)/20 ...', sp.simplify(disc + 4 * (e2 - a) / e1**2 * beta_a / 20) == 0)
chk('beta = (20-e1)a + e1^2 - 20 e2', sp.expand(beta_a - ((20 - e1) * a + e1**2 - 20 * e2)) == 0)
chk('beta(e1) = 20(e1-e2)', sp.expand(beta_a.subs(a, e1) - 20 * (e1 - e2)) == 0)
chk('beta(e2) = e1(e1-e2)', sp.expand(beta_a.subs(a, e2) - e1 * (e1 - e2)) == 0)
astar = 2 * (A**2 - 18 * A + 1) / (A - 9)
chk('beta(a_*) = 0', sp.simplify(beta_a.subs(a, astar)) == 0)
chk('a_*(11) = -76', astar.subs(A, 11) == -76)
chk("a_* < e1 for A > 9 (e1 - a_* = 20(A-1)/(A-9))", sp.simplify(e1 - astar - 20 * (A - 1) / (A - 9)) == 0)

# 3.51(d)
H5d = y**5 - sp.Rational(2, 5) * x**2 * y**3 + sp.Rational(1, 25) * x**4 * y
chk('H5 = y(y^2 - x^2/5)^2', sp.expand(H5d - y * (y**2 - x**2 / 5)**2) == 0)
V5 = sp.expand(Lop(H5d).subs(A, 11))
chk('V5', sp.expand(V5 - (4 * y**5 - sp.Rational(48, 5) * x**2 * y**3 + sp.Rational(44, 25) * x**4 * y)) == 0)
phi6 = sp.integrate(V5, (x, 0, x))
chk('phi6', sp.expand(phi6 - (4 * x * y**5 - sp.Rational(16, 5) * x**3 * y**3 + sp.Rational(44, 125) * x**5 * y)) == 0)
chk('Lap V5 = -76 H5_xx', sp.expand(lap(V5) + 76 * sp.diff(H5d, x, 2)) == 0)
chk('Lap phi6 = -76 H5_x', sp.expand(lap(phi6) + 76 * sp.diff(H5d, x)) == 0)
chk('Lap phi6 value', sp.expand(lap(phi6) - (sp.Rational(304, 5) * x * y**3 - sp.Rational(304, 25) * x**3 * y)) == 0)
cc = [sp.simplify(v.subs({A: 11, a: -76})) for v in (c0, c1, c2)]
chk('quintic coefficients at A=11, a=-76 are (25,-10,1)', cc == [25, -10, 1])
cc = [sp.nsimplify(v.subs({A: 11, a: -100})) for v in (c0, c1, c2)]
cn = [v / cc[0] for v in cc]
chk('a=-100 coefficients (1, -10/31, 5/186)', cn == [1, sp.Rational(-10, 31), sp.Rational(5, 186)])
chk('a=-100 discriminant -10/2883', sp.nsimplify(cn[1]**2 - 4 * cn[0] * cn[2]) == sp.Rational(-10, 2883))
chk('a_* < 0 iff A < 9 + sqrt80 (root)', sp.simplify((A**2 - 18 * A + 1).subs(A, 9 + sp.sqrt(80))) == 0)

# 3.53: recursion from A.3.9 relations, k = 1..4
for k in range(1, 5):
    n = 2 * k + 1
    a0 = sp.Symbol('a0')
    tt = sp.symbols('t0:%d' % (k + 1))
    gg = sp.symbols('g0:%d' % (k + 1))
    # rho^(n) = a0 y Q_{2k}, psi^(n+1) = sum g_j x^{2j+1} y^{n-2j}; leading transport and Poisson
    rho = a0 * y * sum(tt[i] * x**(2 * i) * y**(2 * k - 2 * i) for i in range(k + 1))
    psi = sum(gg[i] * x**(2 * i + 1) * y**(n - 2 * i) for i in range(k + 1))
    cl = (A + 1) / 2
    Dd = cl - 1
    U = (-sp.diff(psi, y), sp.diff(psi, x))
    # transport at degree n: (c_l X + U_lin).grad rho^(n) - rho^(n) + U^(n).grad(a0 y) = 0, U_lin = (D x, -D y)
    tr = sp.expand(cl * (x * sp.diff(rho, x) + y * sp.diff(rho, y)) + Dd * x * sp.diff(rho, x)
                   - Dd * y * sp.diff(rho, y) - rho + a0 * U[1])
    po = sp.expand(-lap(psi) - sp.diff(rho, x))
    eqs = [c for c in sp.Poly(tr, x, y).coeffs()] + [c for c in sp.Poly(po, x, y).coeffs()]
    gsol = sp.solve(sp.Poly(tr, x, y).coeffs(), gg, dict=True)
    ok = len(gsol) == 1
    if ok:
        pol = [sp.simplify(c.subs(gsol[0])) for c in sp.Poly(po, x, y).coeffs()]
        d = [2 * i * (A - 1) + 2 * k for i in range(k + 1)]
        rec = [2 * i * (a0 - d[i]) * tt[i] - sp.Rational((2 * k - 2 * i + 3) * (2 * k - 2 * i + 2), 2 * i - 1)
               * d[i - 1] * tt[i - 1] for i in range(1, k + 1)]
        # the Poisson equations must be equivalent to the recursion: same solution set (linear in t)
        M1 = sp.Matrix([[sp.diff(p, ti) for ti in tt] for p in pol])
        M2 = sp.Matrix([[sp.diff(r, ti) for ti in tt] for r in rec])
        ok = (M1.rank() == M2.rank() == sp.Matrix.vstack(M1, M2).rank())
        ok = ok and all(sp.expand(2 * i * A + 2 * (k - i) - d[i]) == 0 for i in range(k + 1))
    chk('3.53 recursion from leading equations k=%d' % k, ok)

# 3.53: leading part of q_th and the angular weight
for k in range(1, 5):
    tt = sp.symbols('t0:%d' % (k + 1))
    Q = sum(tt[i] * x**(2 * i) * y**(2 * k - 2 * i) for i in range(k + 1))
    qth = sp.expand(x * sp.diff(Q, y) - y * sp.diff(Q, x))
    lead = sp.Poly(qth, x, y).coeff_monomial(x * y**(2 * k - 1))
    chk('3.53 x y^{2k-1} coefficient 2(k t0 - t1), k=%d' % k, sp.expand(lead - 2 * (k * tt[0] - tt[1])) == 0)
    rest = sp.expand(qth - lead * x * y**(2 * k - 1))
    chk('3.53 other terms have x^3, k=%d' % k, all(mon[0] >= 3 for mon in sp.Poly(rest, x, y).monoms()) or rest == 0)
w = sp.cos(th) * sp.sin(th)**3
kk = sp.sin(th)**2 * (4 * sp.sin(th)**2 - 3)
chk('3.53 k = -(cos sin^3)\'', sp.simplify(kk + sp.diff(w, th)) == 0)
chk('3.53 w(0) = w(pi/2) = 0', w.subs(th, 0) == 0 and sp.simplify(w.subs(th, sp.pi / 2)) == 0)
chk('3.53 d_1 = 4D + 2k with A - 1 = 2D', sp.expand((2 * (A - 1)) - 4 * ((A + 1) / 2 - 1)) == 0)

# 3.50(d) bump constants in exact arithmetic
v = sp.Symbol('v', positive=True)
sv = sp.Symbol('s')
vv = 1 / (sv * (1 - sv))
e1d = sp.diff(sp.exp(-vv), sv)
e2d = sp.diff(sp.exp(-vv), sv, 2)
chk('eta\' form', sp.simplify(e1d - sp.exp(-vv) * (1 - 2 * sv) * vv**2) == 0)
chk('eta\'\' form', sp.simplify(e2d - sp.exp(-vv) * ((1 - 2 * sv)**2 * vv**4 - 2 * vv**2
                                                     - 2 * (1 - 2 * sv)**2 * vv**3)) == 0)
chk('3 e^{9/2} < 729', 3 * sp.exp(sp.Rational(9, 2)) < 729)
chk('constants 1458, 29160', 2 * 729 == 1458 and (24 + 12 + 4) * 729 == 29160)
gq = Fr(4, 3)
g1 = 2 + Fr(4, 3) * 729
g2 = 2 + 4 * 729 + Fr(4, 3) * 1458
chk('g bounds 974, 4862', g1 == 974 and g2 == 4862)
Sr = 1458 * 974 + Fr(1, 2) * (29160 * Fr(4, 3) + 729 * 4862)
chk('remote strain constant 3211731', Sr == 3211731 and Sr < 4 * 10**6)
yv = sp.Symbol('yv')
chiv = sp.Function('chi')(yv)
gfun = yv**3 * chiv / 6
chk('g\' and g\'\' expansions', sp.expand(sp.diff(gfun, yv, 2) - (yv * chiv + yv**2 * sp.diff(chiv, yv)
                                                                 + yv**3 * sp.diff(chiv, yv, 2) / 6)) == 0)

npass = sum(1 for _, ok in res if ok)
print('%d/%d PASS' % (npass, len(res)))
