"""Certificate for explicit profiles at delta = 2/5 (Q = 5, c = 5/3): f_1 = sin(theta) + b sin(3 theta).

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
sys.argv = [sys.argv[0], '5', '3', '16']
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


F, G = T.low_orders(10)
O = sympify(F[10].get(1, T.R.zero).as_expr())
Op = Poly(O, b)
cont, P10 = Op.primitive()
P10 = Poly(P10.as_expr() * (1 if P10.LC() > 0 else -1), b)
log('P10 =', P10.as_expr())
log('O10 = P10 *', Rational(Op.LC()) / P10.LC())
fl = factor_list(P10.as_expr())
log('factor_list over QQ:', [(Poly(f, b).degree(), e) for f, e in fl[1]])
assert len(fl[1]) == 1 and fl[1][0][1] == 1 and Poly(fl[1][0][0], b).degree() == 10
# mod-p certificate
p = 2
found = None
while p < 2000:
    p = nextprime(p)
    if Poly(P10.as_expr(), b).LC() % p == 0:
        continue
    Pp = Poly(P10.as_expr(), b, modulus=p)
    if Pp.degree() == 10 and Pp.is_irreducible:
        found = p
        break
log('irreducible modulo p =', found, '(leading coefficient a unit mod p): hence irreducible over QQ')
assert found is not None
iv = P10.intervals(eps=Rational(1, 10 ** 30))
log('real roots (isolating intervals of width <= 1e-30):', len(iv))
roots = []
for (lo, hi), m in iv:
    assert m == 1
    roots.append((lo, hi))
    log('  [%s, %s]  ~ %s' % (Nn(lo, 25), Nn(hi, 25), Nn((lo + hi) / 2, 25)))
assert len(roots) == 6

# generic response
sg, _ = T.sigma(None, F, G)
ge = together(sympify(sg.as_expr()))
num, den = fraction(ge)
Nk = Poly(num, b)
Dk = Poly(den, k)
log('generic sigma: numerator degree in b', Nk.degree(), ', in k', Poly(num, k).degree(), '; denominator degree in k',
    Dk.degree())
assert Nk.degree() <= 5
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
    assert not (r.is_integer and r >= 11), r
dfac = factor_list(den)
log('denominator factors:', [(f, e) for f, e in dfac[1]])
for f, e in dfac[1]:
    pf = Poly(f, k)
    assert pf.degree() <= 1
    if pf.degree() == 1:
        r = -pf.all_coeffs()[1] / pf.all_coeffs()[0]
        assert not (r.is_integer and r >= 11), r
for kv in range(11, 17):
    s, _ = T.sigma(kv, F, G)
    d = sympify(s.as_expr()) - ge.subs(k, kv)
    assert together(d) == 0, kv
log('generic formula equals the direct computation at k = 11..16')
dn = Poly(num, k).degree()
dd = Dk.degree()
assert dn <= dd
lead = Poly(num, k).coeff_monomial(k ** dd) if dn == dd else 0
sinf = sympify(lead) / Dk.LC()
sinf_p = Poly(sinf, b)
log('sigma_inf =', sinf_p.as_expr())
assert not sinf_p.is_zero and sinf_p.degree() <= 5

small = {}
for kv in range(2, 11):
    s, _ = T.sigma(kv, F, G)
    ps = Poly(sympify(s.as_expr()), b)
    assert not ps.is_zero and ps.degree() <= 5
    small[kv] = ps
log('sigma_k for k = 2..10: nonzero polynomials of degree <= 5 (degrees %s)' % [small[kv].degree() for kv in small])
log('CERTIFIED: for every real root b_i of P10, sigma_k(b_i) != 0 for all k >= 2 and sigma_inf(b_i) != 0.')

# information: floating values (interval midpoints, width <= 1e-30)
open('tq5_cert.out', 'w').write('\n'.join(out) + '\n')
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
    big = [(kv, float(fN(kv, bv) / fD(kv))) for kv in (11, 12, 20, 50, 100, 1000)]
    mins = min([(abs(v), kv) for kv, v in sv] + [(abs(float(fN(kv, bv) / fD(kv))), kv) for kv in range(11, 2001)])
    log('root %d: b = %s' % (i + 1, mp.nstr(bv, 20)))
    log('   sigma_2..10 =', ['%.4e' % v for _, v in sv])
    log('   sigma_k (k=11,12,20,50,100,1000) =', ['%.4e' % v for _, v in big], ' sigma_inf = %.6e' % float(fI(bv)))
    log('   min_{2<=k<=2000} |sigma_k| = %.6e at k = %d' % mins)
log('time %.1fs' % (time.time() - t0))
open('tq5_cert.out', 'w').write('\n'.join(out) + '\n')
