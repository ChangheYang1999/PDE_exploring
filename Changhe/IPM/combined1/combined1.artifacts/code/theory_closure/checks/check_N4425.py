#!/usr/bin/env python3
# Review R1-053 (c1-t1): independent check of the single-mode residual identity of N4-425, from
# c1-n4 research/candidate017_dual_residual_replay/PROOF.md (sha256 0ce420a0...), on manufactured fixtures.
#   Rn^2 = Qn + 2 n^2 (b - p) + n^2 (a + d),  Rn = ||r (F_n + Delta psi_n)||_2,
# with psi_n = u(r) sin(n theta), F_n = f(r) sin(n theta), A = -r f cos(n theta) e_theta / n,
# Z = -u' sin(n theta) e_r - (r u'' + u') cos(n theta) e_theta / n, d = ||grad psi||^2, p = int F_n psi,
# a = ||Z||^2, b = <A, Z>, Qn = ||r F_n||^2.
# Part A (symbolic, sympy): div A = F_n in polar form; r^2 Delta psi = (u_yy - n^2 u) sin(n theta) with y = log r;
#   the pointwise integrands of a, b, d, p, Qn after the theta integration.
# Part B (mpmath quadrature on (0, inf), 50 digits, FLOAT): every quantity from its definition in r, the identity,
#   ||A||_2 = sqrt(Qn)/n, and agreement with the exact rational t-formulas of the PROOF, computed here in Part C.
# Part C (exact Fractions): the PROOF's t-formulas for d/pi, a/pi, p/pi, b/pi and Qn/pi (t = r^2/(1+r^2), v = 1-t,
#   u = r sum_b v^b P_b, D_b P = (1-2bt)P + 2t(1-t)P', f = r sum_l v^(l delta/2) A_l(t)), by expansion in v.
# Part D (exact Fractions): the N4-425 whole-field H(017) lower bound and the n = 1, 3 mode enclosures recomposed
#   from the saved strict endpoints in data/N4425_extract.json (fields copied verbatim from c1-n4's result.json,
#   mode_001.json and mode_003.json; if those read-only files are present, the extract and their sha256 are rechecked).
#   No mode integral is recomputed.
# Parts A to C use no c1-n4 or c1-t4 code or data. Fixtures: rational beta > 3/2, k >= -1 with 3+2k-n even and >= 0,
# rational delta, A_l with the factor v^3 so that every integral converges absolutely.
import sys
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
IV = [0, mp.mpf(1) / 2, 1, 2, 10, 100, 10 ** 4, 10 ** 8, mp.inf]
NCHK = [0]
FAIL = [0]


def ok(c, msg):
    NCHK[0] += 1
    if not c:
        FAIL[0] += 1
    print(('PASS ' if c else 'FAIL ') + msg)


r, th = sp.symbols('r theta', positive=True)

# ---------- Part C helpers: exact polynomials in t as dicts {power: Fraction} ----------


def padd(p, q, s=1):
    o = dict(p)
    for k, v in q.items():
        o[k] = o.get(k, 0) + s * v
    return {k: v for k, v in o.items() if v != 0}


def pmul(p, q):
    o = {}
    for i, a in p.items():
        for j, b in q.items():
            o[i + j] = o.get(i + j, 0) + a * b
    return {k: v for k, v in o.items() if v != 0}


def pder(p):
    return {i - 1: i * a for i, a in p.items() if i > 0}


def Dop(bb, P):
    # D_b P = (1 - 2 b t) P + 2 t (1 - t) P'
    return padd(pmul({0: Fr(1), 1: -2 * bb}, P), pmul({1: Fr(2), 2: Fr(-2)}, pder(P)))


def int_v(e, P):
    # int_0^1 v^e P(t) dt with t = 1 - v; expand P in v; every resulting exponent must exceed -1
    from math import comb
    cv = {}
    for i, a in P.items():
        for j in range(i + 1):
            cv[j] = cv.get(j, 0) + a * comb(i, j) * (-1) ** j
    tot = Fr(0)
    for j, c in cv.items():
        if c != 0:
            assert e + j > -1, ('divergent monomial', e, j)
            tot += c / (e + j + 1)
    return tot


def vpoly_to_t(q, m):
    # (1 - t)^m as a t-polynomial
    from math import comb
    return {i: Fr(comb(m, i) * (-1) ** i) for i in range(m + 1)}


def fixture(n, trial, delta, Al):
    # trial: list of (x, beta, k); Al: dict l -> t-polynomial (already containing v^3)
    # ----- symbolic u and f in r -----
    t = r ** 2 / (1 + r ** 2)
    v = 1 / (1 + r ** 2)
    u = sum(sp.Rational(x.numerator, x.denominator) * r ** 3 * (1 + r ** 2) ** (-sp.Rational(be.numerator, be.denominator))
            * t ** k for (x, be, k) in trial)
    f = r * sum(v ** (sp.Rational(l) * sp.Rational(delta.numerator, delta.denominator) / 2 + 3)
                * sum(sp.Rational(c.numerator, c.denominator) * t ** i for i, c in A.items()) for l, A in Al.items())
    return u, f


def run(n, trial, delta, Al, tag):
    u, f = fixture(n, trial, delta, Al)
    up = sp.diff(u, r)
    upp = sp.diff(u, r, 2)
    # radial integrands (theta integral gives pi for sin^2 and cos^2)
    I = {}
    I['d'] = sp.pi * (up ** 2 + n ** 2 * u ** 2 / r ** 2) * r
    I['p'] = sp.pi * f * u * r
    I['a'] = sp.pi * (up ** 2 + (r * upp + up) ** 2 / n ** 2) * r
    I['b'] = sp.pi * (r * f) * (r * upp + up) / n ** 2 * r
    I['Q'] = sp.pi * r ** 2 * f ** 2 * r
    lapr = sp.diff(r * sp.diff(u, r), r) / r - n ** 2 * u / r ** 2
    I['R2'] = sp.pi * r ** 2 * (f + lapr) ** 2 * r
    I['A2'] = sp.pi * (r * f / n) ** 2 * r
    # Part B: quadrature
    val = {}
    for k, e in I.items():
        fn = sp.lambdify(r, e, modules='mpmath')
        val[k] = mp.quad(fn, IV)
    rhs = val['Q'] + 2 * n ** 2 * (val['b'] - val['p']) + n ** 2 * (val['a'] + val['d'])
    rel = abs(val['R2'] - rhs) / max(abs(val['R2']), mp.mpf(1))
    ok(rel < mp.mpf(10) ** -25, '%s: FLOAT Rn^2 = Qn + 2n^2(b-p) + n^2(a+d): %s vs %s (rel diff %s)'
       % (tag, mp.nstr(val['R2'], 20), mp.nstr(rhs, 20), mp.nstr(rel, 3)))
    ok(abs(val['A2'] - val['Q'] / n ** 2) < mp.mpf(10) ** -25 * max(1, abs(val['Q'])),
       '%s: FLOAT ||A_Fn||^2 = Qn/n^2' % tag)
    # cross term and Laplacian square separately
    lapsq = mp.quad(sp.lambdify(r, sp.pi * r ** 2 * lapr ** 2 * r, modules='mpmath'), IV)
    cross = mp.quad(sp.lambdify(r, sp.pi * r ** 2 * f * lapr * r, modules='mpmath'), IV)
    ok(abs(lapsq - n ** 2 * (val['a'] + val['d'])) < mp.mpf(10) ** -25 * max(1, abs(lapsq)),
       '%s: FLOAT ||r Delta psi||^2 = n^2 (a + d) (integration by parts in y)' % tag)
    ok(abs(cross - n ** 2 * (val['b'] - val['p'])) < mp.mpf(10) ** -25 * max(1, abs(cross)),
       '%s: FLOAT int r^2 F_n Delta psi = n^2 (b - p) (no integration by parts)' % tag)
    # Part C: exact t-formulas
    Pb = {}
    for (x, be, k) in trial:
        bb = be - 1
        Pb[bb] = padd(Pb.get(bb, {}), {k + 1: x})
    Dm = {bb: Dop(bb, P) for bb, P in Pb.items()}
    D2 = {bb: Dop(bb, Dm[bb]) for bb in Pb}
    dt = Fr(0)
    at = Fr(0)
    for b1 in Pb:
        for c1 in Pb:
            e = b1 + c1 - 2
            dt += Fr(1, 2) * int_v(e, padd(pmul(Dm[b1], Dm[c1]), pmul({0: Fr(n * n)}, pmul(Pb[b1], Pb[c1]))))
            at += Fr(1, 2) * int_v(e, padd(pmul(Dm[b1], Dm[c1]), pmul({0: Fr(1, n * n)}, pmul(D2[b1], D2[c1]))))
    pt = Fr(0)
    bt = Fr(0)
    Al = {l: pmul(v3, A) for l, A in Al.items()}
    for l, A in Al.items():
        for b1 in Pb:
            e = l * delta / 2 + b1 - 3
            pt += Fr(1, 2) * int_v(e, pmul({1: Fr(1)}, pmul(A, Pb[b1])))
            bt += Fr(1, 2 * n * n) * int_v(e, pmul({1: Fr(1)}, pmul(A, D2[b1])))
    Qt = Fr(0)
    for l, A in Al.items():
        for j, B in Al.items():
            Qt += Fr(1, 2) * int_v((l + j) * delta / 2 - 4, pmul({2: Fr(1)}, pmul(A, B)))
    for k, ex in (('d', dt), ('a', at), ('p', pt), ('b', bt), ('Q', Qt)):
        q = mp.pi * mp.mpf(ex.numerator) / ex.denominator
        ok(abs(val[k] - q) < mp.mpf(10) ** -25 * max(1, abs(q)),
           '%s: FLOAT quadrature %s = pi * exact t-formula %s (%s)' % (tag, k, mp.nstr(q, 20), 'rational' if True else ''))
    R2t = Qt + 2 * n * n * (bt - pt) + n * n * (at + dt)
    ok(R2t >= 0 and abs(val['R2'] - mp.pi * mp.mpf(R2t.numerator) / R2t.denominator) < mp.mpf(10) ** -25 * max(1, abs(val['R2'])),
       '%s: exact Rn^2/pi from the t-formulas is >= 0 and equals the quadrature of ||r(F_n + Delta psi)||^2' % tag)


v3 = vpoly_to_t(None, 3)


def partA():
    # generic radial profiles u(r), f(r) and integer n >= 1
    U = sp.Function('u')(r)
    Fr_ = sp.Function('f')(r)
    for n in (1, 3, 5):
        S, C = sp.sin(n * th), sp.cos(n * th)
        psi = U * S
        Fn = Fr_ * S
        A_th = -r * Fr_ * C / n
        ok(sp.simplify(sp.diff(A_th, th) / r - Fn) == 0, 'generic n=%d: div A_Fn = F_n (A_r = 0, no radial flux)' % n)
        lap = sp.diff(r * sp.diff(psi, r), r) / r + sp.diff(psi, th, 2) / r ** 2
        uy = r * sp.diff(U, r)
        uyy = r * sp.diff(uy, r)
        ok(sp.simplify(r ** 2 * lap - (uyy - n ** 2 * U) * S) == 0,
           'generic n=%d: r^2 Delta psi = (u_yy - n^2 u) sin(n theta), u_y = r u_r' % n)
        up, upp = sp.diff(U, r), sp.diff(U, r, 2)
        Z_r = -up * S
        Z_th = -(r * upp + up) * C / n
        full = {'d': ((sp.diff(psi, r) ** 2 + sp.diff(psi, th) ** 2 / r ** 2) * r,
                      sp.pi * (up ** 2 + n ** 2 * U ** 2 / r ** 2) * r),
                'p': (Fn * psi * r, sp.pi * Fr_ * U * r),
                'a': ((Z_r ** 2 + Z_th ** 2) * r, sp.pi * (up ** 2 + (r * upp + up) ** 2 / n ** 2) * r),
                'b': (A_th * Z_th * r, sp.pi * (r * Fr_) * (r * upp + up) / n ** 2 * r),
                'Q': (r ** 2 * Fn ** 2 * r, sp.pi * r ** 2 * Fr_ ** 2 * r),
                'A2': (A_th ** 2 * r, sp.pi * (r * Fr_ / n) ** 2 * r)}
        for k, (e, red) in full.items():
            ok(sp.simplify(sp.integrate(e, (th, 0, 2 * sp.pi)) - red) == 0,
               'generic n=%d: theta integral of the %s integrand' % (n, k))
        # pointwise algebra behind the identity, before the y integration by parts
        lapr = (uyy - n ** 2 * U) / r ** 2
        ok(sp.simplify((r * (Fr_ + lapr)) ** 2 - (r * Fr_) ** 2 - 2 * Fr_ * (uyy - n ** 2 * U)
                       - (uyy - n ** 2 * U) ** 2 / r ** 2) == 0, 'generic n=%d: square expansion of r(F_n + Delta psi)' % n)
        ok(sp.simplify(r * (r * upp + up) - uyy) == 0, 'generic n=%d: r (r u_rr + u_r) = u_yy' % n)


partA()
fixtures = [
    (1, [(Fr(3, 2), Fr(7, 4), -1), (Fr(-2, 5), Fr(2), 0), (Fr(1, 3), Fr(5, 2), 1)], Fr(4, 9),
     {1: pmul(v3, {0: Fr(1), 1: Fr(-1, 2)}), 2: pmul(v3, {0: Fr(2, 3)}), 5: pmul(v3, {1: Fr(1, 4)})}, 'n=1'),
    (3, [(Fr(1), Fr(13, 8), 0), (Fr(5, 7), Fr(9, 4), 1)], Fr(4, 9),
     {1: pmul(v3, {1: Fr(1), 2: Fr(-1, 3)}), 3: pmul(v3, {1: Fr(-1, 2)})}, 'n=3'),
    (5, [(Fr(-1, 2), Fr(7, 4), 1), (Fr(2), Fr(3), 2)], Fr(1, 3),
     {2: pmul(v3, {2: Fr(3, 2)}), 4: pmul(v3, {2: Fr(1), 3: Fr(1)})}, 'n=5'),
]
for (n, trial, delta, Al, tag) in fixtures:
    for (x, be, k) in trial:
        assert be > Fr(3, 2) and k >= -1 and (3 + 2 * k - n) % 2 == 0 and 3 + 2 * k - n >= 0
    run(n, trial, delta, Al, tag)


def dec_dn(x, k):
    # x rounded down to k decimals
    return _fmt(Fr((x.numerator * 10 ** k) // x.denominator, 10 ** k), k)


def dec_up(x, k):
    # x rounded up to k decimals
    return _fmt(Fr(-((-x.numerator * 10 ** k) // x.denominator), 10 ** k), k)


def _fmt(q, k):
    n = q.numerator * (10 ** k // q.denominator)
    sgn = '-' if n < 0 else ''
    n = abs(n)
    return '%s%d.%0*d' % (sgn, n // 10 ** k, k, n % 10 ** k)


def partD():
    import json, os, hashlib
    here = os.path.dirname(os.path.abspath(__file__))
    X = json.load(open(os.path.join(here, 'data', 'N4425_extract.json')))
    src = 'RUN_ROOT/numerics_audit_N4/research/candidate017_dual_residual_replay/verification/'
    if os.path.exists(src + 'result.json'):
        sh = lambda f: hashlib.sha256(open(src + f, 'rb').read()).hexdigest()
        ok(sh('result.json') == X['result_sha256'] == '7e093982e733237262819ca3ad0486f85bdc4d31c69d73a99e382dbad5c3ab06',
           'D: source result.json present, sha256 7e093982... equals the extract')
        R = json.load(open(src + 'result.json'))
        ok(R['H_lower_square_exact'] == X['H_lower_square_exact'] and R['H_strict_lower_exact'] == X['H_strict_lower_exact']
           and [m['quotient_strict_lower_exact'] for m in R['modes']] == [m['quotient_strict_lower_exact'] for m in X['modes']],
           'D: extract fields equal the source result.json')
        for n in ('1', '3'):
            f = 'mode_%03d.json' % int(n)
            M = json.load(open(src + f))
            ok(sh(f) == X['residual'][n]['record_sha256']
               and M['residual_trial']['H_mode_strict_lower_exact'] == X['residual'][n]['H_mode_strict_lower_exact']
               and M['residual_trial']['H_mode_strict_upper_exact'] == X['residual'][n]['H_mode_strict_upper_exact'],
               'D: %s sha256 and residual endpoints equal the extract' % f)
    else:
        print('NOTE source files absent; Part D uses the extract only')
    ok(X['raw_sha256'] == '7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114', 'D: raw 017 identity 7dc30181...')
    ns = [m['n'] for m in X['modes']]
    ok(ns == list(range(1, 32, 2)), 'D: sixteen distinct odd frequencies 1, 3, ..., 31 (one dual trial each)')
    q = [Fr(m['quotient_strict_lower_exact']) for m in X['modes']]
    ok(all(x > 0 for x in q), 'D: every strict quotient floor |p_n|/sqrt(d_n) is positive')
    S = sum(x * x for x in q)
    ok(S == Fr(X['H_lower_square_exact']), 'D: sum of the sixteen squared floors equals H_lower_square_exact (formula (1))')
    HL = Fr(X['H_strict_lower_exact'])
    ok(HL == Fr(307209799380023711068567013529, 5 * 10 ** 29), 'D: H_strict_lower_exact = 307209799380023711068567013529/(5 10^29)')
    ok(0 < HL and HL * HL < S, 'D: HL^2 < sum, so H(017) > HL by (1)')
    ok(Fr(614419598760, 10 ** 12) < HL < Fr(614419598761, 10 ** 12), 'D: 0.614419598760 < HL < 0.614419598761')
    print('  H(017) > %s (rounded down); sum of squared floors in [%s, %s]' % (dec_dn(HL, 15), dec_dn(S, 15), dec_up(S, 15)))
    for n in ('1', '3'):
        Rn = X['residual'][n]
        L, U = Fr(Rn['H_mode_strict_lower_exact']), Fr(Rn['H_mode_strict_upper_exact'])
        qd = Fr(Rn['dual_quotient_strict_lower_exact'])
        qm = q[ns.index(int(n))]
        ok(qd == qm, 'D n=%s: the mode record dual floor equals the result floor' % n)
        ok(0 < L < U, 'D n=%s: residual-trial enclosure %s < H(F_%s) < %s is nonempty' % (n, dec_dn(L, 13), n, dec_up(U, 13)))
        ok(qd < U, 'D n=%s: the separate dual-trial floor %s is below the residual upper (consistency of two valid bounds)'
           % (n, dec_dn(qd, 13)))
        print('  n=%s: width U - L = %s (rounded up), relative %s; dual floor minus residual lower %s' %
              (n, dec_up(U - L, 15), dec_up((U - L) / L, 8), dec_dn(qd - L, 18) if qd >= L else '-' + dec_up(L - qd, 18)))
    T4484 = (Fr(6144195987, 10 ** 10), Fr(6165956396, 10 ** 10))
    ok(T4484[0] < HL < T4484[1], 'D: HL lies inside the T4-484 conditional interval (0.6144195987, 0.6165956396) (consistency)')
    ok(X['complete_H_upper'].startswith('OPEN') and X['complete_E2_and_017_less_than007'].startswith('OPEN'),
       'D: the source records complete H upper and E2 / 017<007 as OPEN')


partD()
print('checks %d failures %d' % (NCHK[0], FAIL[0]))
print('RESULT ' + ('PASS' if FAIL[0] == 0 else 'FAIL'))
sys.exit(1 if FAIL[0] else 0)
