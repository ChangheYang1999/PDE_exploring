"""Certificate for explicit profiles at delta = 2/Q (c = Q/(Q-2)): f_1 = sin(theta) + b sin(3 theta).  usage: tq_cert.py Q
(the original tq5_cert.py is the case Q = 5; the numbers in this docstring are those of Q = 5, B = 4, k0 = 2Q+1).

Checks (exact arithmetic unless stated):
 1. O_10(b) = P10(b)/den with P10 primitive of degree 10, irreducible over QQ (sympy factorization and an independent
    mod-p irreducibility certificate); six real roots, isolated in rational intervals.
 2. sigma_k for k >= 11 (= QB/2+1 with B=4): generic formula N(k,b)/D(k) from tq_sym (symbolic k), agrees with the
    direct computation at k = 11..16; D has no integer zero k >= 11; the coefficients of N in b have gcd 1 in QQ[k].
 3. sigma_k for 2 <= k <= 10: direct computation, nonzero polynomials of degree <= 5 in b.
 4. sigma_inf = lim sigma_k is a nonzero polynomial of degree <= 5.
 Since P10 is irreducible of degree 10, no nonzero rational polynomial of degree <= 5 vanishes at a root; hence
 sigma_k(b_i) != 0 for all k >= 2 and sigma_inf(b_i) != 0, so inf_k |sigma_k(b_i)| > 0.
 5. (information, floating point) values of sigma_k at the six roots, and the minimum over 2 <= k <= 2000.
"""
import sys, time
QQ_ = int(sys.argv[1]) if len(sys.argv) > 1 else 5
K0 = 2 * QQ_ + 1  # = Q*B/2 + 1 with B = 4
sys.argv = [sys.argv[0], str(QQ_), '3', str(K0 + 5)]
import tq_sym as T
from sympy import (Poly, symbols, factor_list, sympify, gcd, nextprime, together, fraction, LT, degree, limit, oo,
                   Rational, N as Nn, nsimplify)

t0 = time.time()
b, k = symbols('b k')
out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


F, G = T.low_orders(2 * QQ_)
O = sympify(F[2 * QQ_].get(1, T.R.zero).as_expr())
Op = Poly(O, b)
cont, P10 = Op.primitive()
P10 = Poly(P10.as_expr() * (1 if P10.LC() > 0 else -1), b)
log('Q =', QQ_, ' P =', P10.as_expr())
log('O_2Q = P *', Rational(Op.LC()) / P10.LC())
fl = factor_list(P10.as_expr())
log('factor_list over QQ:', [(Poly(f, b).degree(), e) for f, e in fl[1]])
assert len(fl[1]) == 1 and fl[1][0][1] == 1 and Poly(fl[1][0][0], b).degree() == 2 * QQ_
# mod-p certificate: factor degree patterns modulo good primes; the possible degrees of a rational factor are subset sums
# of every pattern; if only 0 and deg remain, the polynomial is irreducible over QQ
from itertools import combinations
deg = P10.degree()
possible = set(range(deg + 1))
p = 2
used = []
from sympy import discriminant
disc = discriminant(P10.as_expr(), b)
while p < 3000 and possible != {0, deg}:
    p = nextprime(p)
    if Poly(P10.as_expr(), b).LC() % p == 0 or disc % p == 0:
        continue
    Pp = Poly(P10.as_expr(), b, modulus=p)
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
iv = P10.intervals(eps=Rational(1, 10 ** 30))
log('real roots (isolating intervals of width <= 1e-30):', len(iv))
roots = []
for (lo, hi), m in iv:
    assert m == 1
    roots.append((lo, hi))
    log('  [%s, %s]  ~ %s' % (Nn(lo, 25), Nn(hi, 25), Nn((lo + hi) / 2, 25)))
log('number of real roots:', len(roots))

# generic response
sg, _ = T.sigma(None, F, G)
ge = together(sympify(sg.as_expr()))
num, den = fraction(ge)
Nk = Poly(num, b)
Dk = Poly(den, k)
log('generic sigma: numerator degree in b', Nk.degree(), ', in k', Poly(num, k).degree(), '; denominator degree in k',
    Dk.degree())
assert Nk.degree() <= QQ_
coeffs = [Poly(c, k) for c in Nk.all_coeffs()]
g = coeffs[0]
for c in coeffs[1:]:
    g = gcd(g, c)
log('gcd of the b-coefficients of the numerator in QQ[k]:', g.as_expr())
gc = Poly(g, k)
# remove the explicit factors (k-1)(2k-1)^2 if they are common: report the gcd and its integer roots
from sympy import roots as sroots
rts = sroots(gc.as_expr(), k) if gc.degree() > 0 else {}
log('roots of the gcd:', rts)
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
assert not sinf_p.is_zero and sinf_p.degree() <= QQ_

small = {}
for kv in range(2, K0):
    s, _ = T.sigma(kv, F, G)
    ps = Poly(sympify(s.as_expr()), b)
    assert not ps.is_zero and ps.degree() <= QQ_
    small[kv] = ps
log('sigma_k for k = 2..%d: nonzero polynomials of degree <= Q (degrees %s)' % (K0 - 1, [small[kv].degree() for kv in small]))
assert QQ_ < 2 * QQ_
log('CERTIFIED: for every real root b_i of P, sigma_k(b_i) != 0 for all k >= 2 and sigma_inf(b_i) != 0.')

# information: floating values (interval midpoints, width <= 1e-30)
open('tq_cert_Q%d.out' % QQ_, 'w').write('\n'.join(out) + '\n')
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
    log('   sigma_2..%d =' % (K0 - 1), ['%.4e' % v for _, v in sv])
    log('   sigma_k (k=K0,K0+1,20,50,100,1000) =', ['%.4e' % v for _, v in big], ' sigma_inf = %.6e' % float(fI(bv)))
    log('   min_{2<=k<=2000} |sigma_k| = %.6e at k = %d' % mins)
log('time %.1fs' % (time.time() - t0))
open('tq_cert_Q%d.out' % QQ_, 'w').write('\n'.join(out) + '\n')
