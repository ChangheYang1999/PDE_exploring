"""R1-031 (REVIEWS_v28): independent checks of c1-t4 T4-251 (affine lift of the five Taylor constraints).

Part A (general real c, symbolic). Ordinary Cartesian jets in sympy, with c and a = rho_y(0) symbolic and a general
even-even potential jet of degree <= 8 subject to chi_xxyy(0) = 1 - c:
  A1 the y-coefficient of F vanishes (strain normalization), so C collects all of F/y of degree <= 4 except 0;
  A2 C(chi + h) = C(chi) + J s + Q(s) exactly for h = sum s_k e_k, with Q = (0, 0, -192 s1^2, -8640 s1 s2, 0);
  A3 J is block lower triangular with diagonal 24(a - 4c + 2), -240, K, -480c, -1344, K = 60(a - 8c + 4), and the
     degree-eight block is matrix (4) and depends on (c, a) only;
  A4 J[3:5, 3:5] (u0, v0, w0) = (-192 alpha^2, -8640 alpha beta, 0) for symbolic alpha, beta;
  A5 the nonlinear system C(chi + eta) = 0 has exactly one solution eta in the span (triangular solve), and with
     tau, z = eta + tau: C(chi) + J z = 0 and C(chi + z) = (0, 0, -192 alpha^2, -8640 alpha beta, 0);
  A6 the tail identity r^(2(l-m)) (1 + r^2)^(p-l-2) = t^(l-m) (1 - t)^2 (1 + r^2)^(p-m), t = r^2/(1 + r^2).
Part B (c = c_007, exact rationals from data/T4251_inputs.json):
  B1 u0, v0, w0 from the T4-211 alpha, beta and a0 equal the T4-251 tau parameters exactly; z = eta + tau;
  B2 the 15 canonical tau coordinates rebuilt from the harmonic expansion equal the T4-251 values exactly, lie in
     the frozen 007 order, and have zero leading and first-descendant tail rows;
  B3 the five whole-plane norms B_ij^2/pi recomputed by the Beta integral equal the T4-211 rationals exactly;
  B4 the tau and z density bounds (5), in 512-bit arb.
Writes no file.
"""
import json
import sys
from fractions import Fraction as Q
from math import comb
from pathlib import Path

import sympy as sp
from flint import arb, ctx

ctx.prec = 512
sys.set_int_max_str_digits(0)
x, y, c, a = sp.symbols('x y c a')
PAIRS = [(2, 1), (0, 3), (3, 1), (1, 3), (0, 4)]
ROWS = [(2, 1), (0, 3), (4, 1), (2, 3), (0, 5)]   # monomials x^i y^j of F for x^2, y^2, x^4, x^2 y^2, y^4 in F/y


def trunc(e, d):
    P = sp.Poly(sp.expand(e), x, y)
    return sum((coef * x**i * y**j for (i, j), coef in P.terms() if i + j <= d), sp.Integer(0))


def fields(chi):
    rho = -sp.diff(sp.diff(chi, x, 2) + sp.diff(chi, y, 2), y)
    return rho, -sp.diff(chi, x, y, y), sp.diff(chi, x, x, y)


def F(chi, cc):
    rho, u1, u2 = fields(chi)
    return trunc((cc * x + u1) * sp.diff(rho, x) + (cc * y + u2) * sp.diff(rho, y) - rho, 5)


def coeff(e, i, j):
    return sp.Poly(sp.expand(e), x, y).coeff_monomial(x**i * y**j)


def C(chi, cc):
    f = F(chi, cc)
    return [coeff(f, i, j) for i, j in ROWS], f


def ejet(i, j, pp, deg=8):
    q = pp - i - j - 2
    r2 = x**2 + y**2
    ser = sum((sp.binomial(q, k) * r2**k for k in range(0, (deg - 2 * (i + j)) // 2 + 1)), sp.Integer(0))
    return trunc(x**(2 * i) * y**(2 * j) * ser, deg)


def part_a():
    p = (3 + 1 / c) / 2
    ks = {(i, j): sp.Symbol(f'k{2*i}{2*j}') for i in range(5) for j in range(5) if 2 <= i + j <= 4}
    ks[1, 1] = (1 - c) / 4                 # chi_xxyy(0) = 4 k22 = 1 - c
    ks[0, 2] = (c - 1 - a) / 24            # a = rho_y(0) = -(4 k22 + 24 k04)
    chi = sum((v * x**(2 * i) * y**(2 * j) for (i, j), v in ks.items()), sp.Integer(0))
    rho, u1, u2 = fields(chi)
    assert sp.simplify(sp.diff(rho, y).subs({x: 0, y: 0}) - a) == 0
    assert sp.simplify(sp.diff(chi, x, x, y, y).subs({x: 0, y: 0}) - (1 - c)) == 0
    f0 = F(chi, c)
    assert sp.simplify(coeff(f0, 0, 1)) == 0, 'A1'
    P = sp.Poly(f0, x, y)
    assert all(j % 2 == 1 and i % 2 == 0 for (i, j), v in P.terms() if sp.simplify(v) != 0), 'F/y is even-even'
    print('A1 strain: y-coefficient of F is 0; F/y is even in x and y up to degree 4')
    s = sp.symbols('s1:6')
    E = [ejet(i, j, p) for i, j in PAIRS]
    h = sum((sk * ek for sk, ek in zip(s, E)), sp.Integer(0))
    C0, _ = C(chi, c)
    Ch, _ = C(chi + h, c)
    Jm = sp.Matrix([[sp.diff(Ch[r], s[k]).subs({sv: 0 for sv in s}) for k in range(5)] for r in range(5)])
    Qexp = [sp.Integer(0), sp.Integer(0), -192 * s[0]**2, -8640 * s[0] * s[1], sp.Integer(0)]
    for r in range(5):
        lin = sum((Jm[r, k] * s[k] for k in range(5)), sp.Integer(0))
        assert sp.simplify(sp.expand(Ch[r] - C0[r] - lin - Qexp[r])) == 0, ('A2', r)
    print('A2 exact expansion C(chi+h) = C(chi) + J s + Q(s), Q = (0, 0, -192 s1^2, -8640 s1 s2, 0)')
    K = 60 * (a - 8 * c + 4)
    D4 = sp.Matrix([[K, 0, 0], [0, -480 * c, 0], [0, 12 * (a - 4), -1344]])
    assert all(sp.simplify(Jm[r, k]) == 0 for r in range(2) for k in range(2, 5)), 'A3 zero block'
    assert sp.simplify(Jm[0, 1]) == 0 and sp.simplify(Jm[1, 0]) == 0
    assert sp.simplify(Jm[0, 0] - 24 * (a - 4 * c + 2)) == 0 and sp.simplify(Jm[1, 1] + 240) == 0
    assert sp.simplify(Jm[2:5, 2:5] - D4) == sp.zeros(3, 3)
    free = set().union(*(sp.sympify(Jm[r, k]).free_symbols for r in range(2, 5) for k in range(2, 5)))
    assert free <= {a, c}, free
    blockB = set().union(*(sp.sympify(Jm[r, k]).free_symbols for r in range(2, 5) for k in range(2)))
    print('A3 J = [[diag(24(a-4c+2), -240), 0], [B, (4)]]; (4) depends on', sorted(map(str, free)),
          '; B depends on', sorted(map(str, blockB)))
    al, be = sp.symbols('alpha beta')
    u0 = -192 * al**2 / K
    v0 = 18 * al * be / c
    w0 = (a - 4) * v0 / 112
    lhs = D4 * sp.Matrix([u0, v0, w0])
    assert sp.simplify(lhs - sp.Matrix([-192 * al**2, -8640 * al * be, 0])) == sp.zeros(3, 1), 'A4'
    print('A4 (4) (u0, v0, w0) = (-192 alpha^2, -8640 alpha beta, 0)')
    # A5: unique nonlinear repair (triangular), then the affine statements.
    e1 = -C0[0] / Jm[0, 0]
    e2 = -C0[1] / Jm[1, 1]
    rhs = sp.Matrix([-(C0[r] + Jm[r, 0] * e1 + Jm[r, 1] * e2 + Qexp[r].subs({s[0]: e1, s[1]: e2}))
                     for r in range(2, 5)])
    e345 = D4.LUsolve(rhs)
    eta = [e1, e2] + list(e345)
    sub_eta = dict(zip(s, eta))
    assert all(sp.simplify(Ch[r].subs(sub_eta)) == 0 for r in range(5)), 'A5 C(chi+eta) = 0'
    sub_ab = {al: e1, be: e2}
    tau = [sp.Integer(0), sp.Integer(0), u0.subs(sub_ab), v0.subs(sub_ab), w0.subs(sub_ab)]
    zz = [eta[k] + tau[k] for k in range(5)]
    sub_z = dict(zip(s, zz))
    for r in range(5):
        aff = C0[r] + sum((Jm[r, k] * zz[k] for k in range(5)), sp.Integer(0))
        assert sp.simplify(aff) == 0, ('A5 affine', r)
        assert sp.simplify(Ch[r].subs(sub_z) - Qexp[r].subs({s[0]: e1, s[1]: e2})) == 0, ('A5 nonlinear', r)
    print('A5 det J != 0 under the hypotheses; eta unique; C(chi) + J z = 0; C(chi + z) = (0, 0, -192 alpha^2, '
          '-8640 alpha beta, 0); z - eta = tau has degree >= 8, so a and chi_xxyy(0) are unchanged')
    rr, pp, l, m = sp.symbols('r p l m', positive=True)
    t = rr**2 / (1 + rr**2)
    lhs = rr**(2 * (l - m)) * (1 + rr**2)**(pp - l - 2)
    rhs = t**(l - m) * (1 - t)**2 * (1 + rr**2)**(pp - m)
    assert sp.simplify(sp.powsimp(sp.expand_power_base(lhs / rhs, force=True), force=True)) == 1, 'A6'
    print('A6 r^(2(l-m)) (1+r^2)^(p-l-2) = t^(l-m) (1-t)^2 (1+r^2)^(p-m)')


def harmonic_identity(i, j, d):
    """Check x^(2i) y^(2j) = sum_m d_m Re(x + i y)^(2m) (x^2 + y^2)^(l - m) as a polynomial identity."""
    l = i + j
    def H(m):
        return sum((sp.Integer((-1)**jj * comb(2 * m, 2 * jj)) * x**(2 * (m - jj)) * y**(2 * jj)
                    for jj in range(m + 1)), sp.Integer(0))
    tot = sum((sp.Rational(v.numerator, v.denominator) * H(m) * (x**2 + y**2)**(l - m) for m, v in d.items()),
              sp.Integer(0))
    return sp.expand(tot - x**(2 * i) * y**(2 * j)) == 0


def harmonic_split_exact(i, j):
    """x^(2i) y^(2j) = sum_m d_m Re(x + i y)^(2m) r^(2(l-m)): exact d_m by a triangular Chebyshev solve."""
    l = i + j
    X = sp.symbols('X')
    # In the variables x^2 = X, y^2 = 1 - X on the unit circle: Re(x + i y)^(2m) = T_m(cos 2 th), cos 2 th = 2X - 1.
    target = sp.Poly(X**i * (1 - X)**j, X)
    basis = [sp.Poly(sp.chebyshevt(m, 2 * X - 1), X) for m in range(l + 1)]
    d = {}
    rem = target
    for m in range(l, -1, -1):
        lc = basis[m].coeff_monomial(X**m) if m else basis[0].as_expr()
        dm = rem.coeff_monomial(X**m) / lc
        d[m] = Q(str(sp.Rational(dm)))
        rem = rem - basis[m] * dm
    assert rem.is_zero
    return d


def part_b():
    D = json.loads((Path(__file__).resolve().parent / 'data/T4251_inputs.json').read_text())
    cq = Q(D['c'])
    assert D['a0_canonical007'] == D['a0_lift']
    aq = Q(D['a0_canonical007'])
    pq = (3 + 1 / cq) / 2
    ts = {tuple(z['pair']): Q(z['coefficient']) for z in D['eta_parameters']}
    al, be = ts[2, 1], ts[0, 3]
    assert al != 0 and aq - 4 * cq + 2 != 0 and aq - 8 * cq + 4 != 0
    K = 60 * (aq - 8 * cq + 4)
    corr = {(3, 1): -192 * al**2 / K, (1, 3): 18 * al * be / cq}
    corr[0, 4] = (aq - 4) * corr[1, 3] / 112
    given = {tuple(z['pair']): Q(z['coefficient']) for z in D['tau_parameters']}
    assert given == corr, 'B1 tau'
    aff = {tuple(z['pair']): Q(z['coefficient']) for z in D['affine_parameters']}
    assert aff == {ij: ts[ij] + corr.get(ij, Q(0)) for ij in ts}, 'B1 z'
    print('B1 tau = (u0, v0, w0) and z = eta + tau equal the T4-251 parameters exactly;',
          'a0 - 4c + 2 =', float(aq - 4 * cq + 2), ', a0 - 8c + 4 =', float(aq - 8 * cq + 4))
    print('   alpha =', f'{float(al):.6e}', ', beta =', f'{float(be):.6e}', '; nonlinear defect of z (2):',
          f'(0, 0, {float(-192 * al**2):.6e}, {float(-8640 * al * be):.6e}, 0)')
    can = {}
    for (i, j), tval in corr.items():
        d2 = harmonic_split_exact(i, j)
        assert harmonic_identity(i, j, d2)
        l = i + j
        for m, dm in d2.items():
            for k, w in ((l, 1), (l + 1, -2), (l + 2, 1)):
                can[0, m, k] = can.get((0, m, k), Q(0)) + w * dm * tval
    can = {k: v for k, v in can.items() if v}
    given = {tuple(z['index']): Q(z['coefficient']) for z in D['canonical_tau_changes']}
    assert can == given, 'B2'
    order = {tuple(t) for t in D['canonical007_order_block0']}
    assert set(can) <= order
    for m in {k[1] for k in can}:
        vals = [(k[2], v) for k, v in can.items() if k[1] == m]
        assert sum((v for _, v in vals), Q(0)) == 0 and sum(((pq - k) * v for k, v in vals), Q(0)) == 0
    print('B2', len(can), 'canonical tau coordinates rebuilt from the harmonic expansion equal T4-251;',
          'all in the frozen 007 order; leading and first-descendant tail rows vanish in each block m')
    # B3: whole-plane norms by the Beta integral.
    norms = {}
    for i, j in PAIRS:
        l = i + j
        qv = pq - l - 2
        # f = sum_k P_k (1 + r^2)^(q - k), stored as {k: P_k}; d(P w^(q-k)) = dP w^(q-k) + (q-k) P dw w^(q-k-1).
        qv_s = sp.Rational(qv.numerator, qv.denominator)

        def d(fd, var):
            out = {}
            for k, Pk in fd.items():
                out[k] = out.get(k, 0) + sp.diff(Pk, var)
                out[k + 1] = out.get(k + 1, 0) + (qv_s - k) * Pk * 2 * var
            return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}

        def addd(f1, f2, s2=1):
            out = dict(f1)
            for k, v in f2.items():
                out[k] = sp.expand(out.get(k, 0) + s2 * v)
            return {k: v for k, v in out.items() if v != 0}
        f = {0: x**(2 * i) * y**(2 * j)}
        lap = addd(d(d(f, x), x), d(d(f, y), y))
        rd = d(lap, y)
        assert max(rd) <= 3
        Ptot = sp.expand(-sum((Pk * (1 + x**2 + y**2)**(3 - k) for k, Pk in rd.items()), sp.Integer(0)))
        Pp = sp.Poly(Ptot, x, y)
        coeffs = {mon: Q(str(sp.Rational(cf))) for mon, cf in Pp.terms()}
        sq = {}
        for (i1, j1), c1 in coeffs.items():
            for (i2, j2), c2 in coeffs.items():
                sq[i1 + i2, j1 + j2] = sq.get((i1 + i2, j1 + j2), Q(0)) + c1 * c2
        s_exp = 2 * qv - 6
        tot = Q(0)
        for (A, B), v in sq.items():
            if v == 0:
                continue
            assert A % 2 == 0 and B % 2 == 0
            A2, B2 = A // 2, B // 2
            n = A2 + B2
            ang = Q(1)                      # (2A2-1)!!(2B2-1)!!/2^n  (times 2 pi / n! ... combined below)
            for kk in range(1, 2 * A2, 2):
                ang *= kk
            for kk in range(1, 2 * B2, 2):
                ang *= kk
            ang /= 2**n
            den = Q(1)
            for kk in range(1, n + 2):
                den *= (-s_exp - kk)
            assert -s_exp - n - 1 > 0
            tot += v * ang / den
        norms[i, j] = tot
    given = {tuple(z['pair']): Q(z['squared_L2_over_pi']) for z in D['eta_direction_norms_squared_over_pi']}
    assert norms == given, 'B3'
    print('B3 B_ij^2/pi recomputed exactly and equal to the T4-211 rationals; B_ij =',
          ', '.join(f'{ij}: {float((arb.pi() * arb(v.numerator) / v.denominator).sqrt().mid()):.6e}'
                    for ij, v in norms.items()))

    def ar(v):
        return arb(v.numerator) / arb(v.denominator)
    bn = {ij: (arb.pi() * ar(v)).sqrt() for ij, v in norms.items()}
    tb = sum((ar(abs(v)) * bn[ij] for ij, v in corr.items()), arb(0))
    zb = sum((ar(abs(aff[ij])) * bn[ij] for ij in aff), arb(0))
    eb = sum((ar(abs(ts[ij])) * bn[ij] for ij in ts), arb(0))
    assert tb < arb('1e-24') and zb < arb('3.424e-12')
    print('B4 ||rho[tau]||_2 <=', tb.str(12), '; ||rho[z]||_2 <=', zb.str(12), '; ||rho[eta]||_2 <=', eb.str(12))
    lb = D['lift_result_bounds']
    print('   T4-251 stored balls: tau', lb['tau'][:40], '; z', lb['affine'][:40])


if __name__ == '__main__':
    part_a()
    part_b()
    print('all checks passed')
