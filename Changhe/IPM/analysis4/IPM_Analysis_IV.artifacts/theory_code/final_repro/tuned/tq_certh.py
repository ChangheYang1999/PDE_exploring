"""Certificate for explicit profiles at delta = 2h/Q (gcd(h,Q) = 1, 2h < Q, c = Q/(Q-2h)):
f_1 = sin(theta) + b sin(3 theta).  usage: tq_certh.py Q h   (h = 1 is the case of tq_cert.py).

k1 = 1 if h >= 2 else 2 (first resonance index), N1 = k1 Q (order of the first obstruction), B = 4,
K0 = ceil((QB+2)/(2h)) (then q_k = 2hk-2 >= QB for k >= K0, so the symbolic-k formula has no folding).
Checks (exact arithmetic unless stated):
 1. O_N1(b) = P(b) * const with P primitive; P irreducible over QQ (sympy factorization and an independent certificate
    from factor degree patterns modulo good primes); real roots isolated in rational intervals of width <= 1e-30.
 2. sigma_k for k >= K0: generic formula N(k,b)/D(k) from tq_symh (symbolic k), equal to the direct computation at
    k = K0..K0+5; D has no integer zero k >= K0.  Let r_j(k) be the coefficients (in b) of the remainder of N(k,b) on
    division by the monic multiple of P; the gcd of the r_j in QQ[k] has no integer root k >= K0.  Since P is
    irreducible, sigma_k(b_i) = 0 at a root b_i of P iff P divides sigma_k(.) iff all r_j(k) = 0.  Hence sigma_k(b_i) != 0
    for every k >= K0 and every root (real or complex).
 3. sigma_k for k1 <= k < K0: direct computation, nonzero polynomials of degree <= Q in b, not divisible by P.
 4. sigma_inf = lim sigma_k: polynomial of degree <= Q, not divisible by P.
 For h = 1 the degree bound Q < 2Q = deg P already excludes divisibility; for h >= 2, deg P = Q and divisibility is
 excluded by the remainder test.  Hence sigma_k(b_i) != 0 for all k >= k1 and sigma_inf(b_i) != 0, so
 inf_k |sigma_k(b_i)| > 0 at every real root b_i.
 5. (information, floating point) values of sigma_k at the real roots, and the minimum over k1 <= k <= 2000.
"""
import sys, time
QQ_ = int(sys.argv[1]) if len(sys.argv) > 1 else 9
HH_ = int(sys.argv[2]) if len(sys.argv) > 2 else 2
BB = 4
K0 = -(-(QQ_ * BB + 2) // (2 * HH_))
sys.argv = [sys.argv[0], str(QQ_), str(HH_), '3', str(K0 + 5)]
import tq_symh as T
from sympy import (Poly, symbols, factor_list, sympify, gcd, nextprime, together, fraction, Rational, N as Nn, rem,
                   discriminant)

t0 = time.time()
b, k = symbols('b k')
out = []
tag = 'Q%dh%d' % (QQ_, HH_)


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


k1, N1 = T.KFIRST, T.NFIRST
F, G = T.low_orders(N1)
O = sympify(F[N1].get(2 * HH_ * k1 - 3, T.R.zero).as_expr())
Op = Poly(O, b)
cont, P = Op.primitive()
P = Poly(P.as_expr() * (1 if P.LC() > 0 else -1), b)
deg = P.degree()
log('Q = %d, h = %d, delta = %s, c = %s, first obstruction at order %d (density mode %d); K0 = %d'
    % (QQ_, HH_, Rational(2 * HH_, QQ_), Rational(QQ_, QQ_ - 2 * HH_), N1, 2 * HH_ * k1 - 3, K0))
log('P =', P.as_expr())
log('O = P *', Rational(Op.LC()) / P.LC())
fl = factor_list(P.as_expr())
log('factor_list over QQ:', [(Poly(f, b).degree(), e) for f, e in fl[1]])
assert len(fl[1]) == 1 and fl[1][0][1] == 1 and Poly(fl[1][0][0], b).degree() == deg
possible = set(range(deg + 1))
p = 2
used = []
disc = discriminant(P.as_expr(), b)
while p < 3000 and possible != {0, deg}:
    p = nextprime(p)
    if P.LC() % p == 0 or disc % p == 0:
        continue
    Pp = Poly(P.as_expr(), b, modulus=p)
    degs = [Poly(f, b, modulus=p).degree() for f, e in Pp.factor_list()[1] for _ in range(e)]
    sums = {0}
    for d_ in degs:
        sums = sums | {x + d_ for x in sums}
    possible &= sums
    used.append((p, sorted(degs)))
found = used[-1][0] if possible == {0, deg} else None
log('factor degree patterns modulo good primes (unit leading coefficient, squarefree):', used)
log('possible degrees of a rational factor after intersection:', sorted(possible), '-> irreducible over QQ' if found else '')
assert found is not None
iv = P.intervals(eps=Rational(1, 10 ** 30))
roots = []
for (lo, hi), m in iv:
    assert m == 1
    roots.append((lo, hi))
    log('  [%s, %s]  ~ %s' % (Nn(lo, 25), Nn(hi, 25), Nn((lo + hi) / 2, 25)))
log('number of real roots:', len(roots))
Pm = Poly(P.as_expr() / P.LC(), b)  # monic over QQ


def not_divisible(poly_b):
    """poly_b: Poly in b over QQ, nonzero; True if P does not divide it"""
    return not rem(poly_b, Pm).is_zero


# generic response
sg, _ = T.sigma(None, F, G)
ge = together(sympify(sg.as_expr()))
num, den = fraction(ge)
Nk = Poly(num, b)
Dk = Poly(den, k)
log('generic sigma: numerator degree in b', Nk.degree(), ', in k', Poly(num, k).degree(), '; denominator degree in k',
    Dk.degree())
assert Nk.degree() <= QQ_
Nkb = Poly(num, b, k)
Rem = Poly(rem(Poly(num, b), Pm).as_expr(), b)  # coefficients in QQ[k]
rcoef = [Poly(c, k) for c in Rem.all_coeffs()]
assert any(not c.is_zero for c in rcoef)
g = None
for c in rcoef:
    if c.is_zero:
        continue
    g = c if g is None else gcd(g, c)
log('remainder of N(k,.) modulo P: %d coefficients; gcd in QQ[k] of degree %d' % (len(rcoef), g.degree()))
gfac = factor_list(g.as_expr()) if g.degree() > 0 else (1, [])
rts = []
for f, e in gfac[1]:
    pf = Poly(f, k)
    if pf.degree() == 1:
        rts.append(-pf.all_coeffs()[1] / pf.all_coeffs()[0])
log('rational roots of the gcd (factors of degree >= 2 have none):', rts, '; factor degrees',
    sorted(Poly(f, k).degree() for f, e in gfac[1]))
for r in rts:
    assert not (r.is_integer and r >= K0), r
dfac = factor_list(den)
log('denominator factors:', [(f, e) for f, e in dfac[1]])
for f, e in dfac[1]:
    pf = Poly(f, k)
    assert pf.degree() <= 1
    if pf.degree() == 1:
        r = -pf.all_coeffs()[1] / pf.all_coeffs()[0]
        assert not (r.is_integer and r >= K0), r
for kv in range(K0, K0 + 6):
    s, _ = T.sigma(kv, F, G)
    d = sympify(s.as_expr()) - ge.subs(k, kv)
    assert together(d) == 0, kv
log('generic formula equals the direct computation at k = %d..%d' % (K0, K0 + 5))
dn = Poly(num, k).degree()
dd = Dk.degree()
assert dn <= dd
lead = Poly(num, k).coeff_monomial(k ** dd) if dn == dd else 0
sinf = sympify(lead) / Dk.LC()
sinf_p = Poly(sinf, b)
log('sigma_inf =', sinf_p.as_expr())
assert not sinf_p.is_zero and sinf_p.degree() <= QQ_ and not_divisible(sinf_p)
log('sigma_inf: nonzero, degree %d, not divisible by P' % sinf_p.degree())

small = {}
for kv in range(k1, K0):
    s, _ = T.sigma(kv, F, G)
    ps = Poly(sympify(s.as_expr()), b)
    assert not ps.is_zero and ps.degree() <= QQ_ and not_divisible(ps)
    small[kv] = ps
log('sigma_k for k = %d..%d: nonzero polynomials of degree <= Q, none divisible by P (degrees %s)'
    % (k1, K0 - 1, [small[kv].degree() for kv in small]))
log('CERTIFIED: for every root b_i of P, sigma_k(b_i) != 0 for all k >= %d and sigma_inf(b_i) != 0.' % k1)
open('tq_certh_%s.out' % tag, 'w').write('\n'.join(out) + '\n')

# information: floating values (interval midpoints, width <= 1e-30)
import mpmath as mp
from sympy import lambdify
mp.mp.dps = 120
fN = lambdify((k, b), num, 'mpmath')
fD = lambdify(k, den, 'mpmath')
fI = lambdify(b, sinf, 'mpmath')
for i, (lo, hi) in enumerate(roots):
    mid = (lo + hi) / 2
    bv = mp.mpf(int(mid.p)) / int(mid.q)
    sv = [(kv, float(small[kv].eval(mid))) for kv in sorted(small)]
    big = [(kv, float(fN(kv, bv) / fD(kv))) for kv in (K0, K0 + 1, 20, 50, 100, 1000)]
    mins = min([(abs(v), kv) for kv, v in sv] + [(abs(float(fN(kv, bv) / fD(kv))), kv) for kv in range(K0, 2001)])
    log('root %d: b = %s' % (i + 1, mp.nstr(bv, 20)))
    log('   sigma_%d..%d =' % (k1, K0 - 1), ['%.4e' % v for _, v in sv])
    log('   sigma_k (k=K0,K0+1,20,50,100,1000) =', ['%.4e' % v for _, v in big], ' sigma_inf = %.6e' % float(fI(bv)))
    log('   min_{%d<=k<=2000} |sigma_k| = %.6e at k = %d' % (k1, mins[0], mins[1]))
log('time %.1fs' % (time.time() - t0))
open('tq_certh_%s.out' % tag, 'w').write('\n'.join(out) + '\n')
