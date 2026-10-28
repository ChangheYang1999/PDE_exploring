# Independent cross-read check of V232 geometry (exact) and a float estimate of the supplemental savings.
from fractions import Fraction as Fr
import sympy as sp
from mpmath import mp, quad, sqrt, binomial, pi
t = sp.symbols('t')
cm = Fr(18575812884078966825547550257, 25 * 10 ** 27); am = 1 - cm
D = [(cm, am), (Fr(41, 100), Fr(3, 40)), (Fr(29, 100), Fr(1, 25)), (Fr(9, 40), Fr(3, 125)), (Fr(7, 40), Fr(7, 500))]
for i, (c, a) in enumerate(D):
    c_, a_ = sp.Rational(c.numerator, c.denominator), sp.Rational(a.numerator, a.denominator)
    P = sp.Poly(c_**2 - a_**2 - 4*c_*t + 4*t**2 + 4*c_*t**3 - 4*t**4, t)
    nroots = P.count_roots(0, sp.Rational(3, 4))
    # minimum on [0, 1/sqrt2] numerically, for the margin
    crit = [r for r in sp.Poly(P.diff(t), t).nroots() if abs(sp.im(r)) < 1e-30 and 0 <= sp.re(r) <= 0.7072]
    mn = min([float(P.eval(sp.re(r))) for r in crit] + [float(P.eval(0)), float(P.eval(sp.sqrt(2) / 2))])
    print(i, float(c), float(a), 'a<c/2', a < c / 2, 'c+a<=1', c + a <= 1, 'roots in [0,3/4]:', nroots, 'min P on [0,1/sqrt2] ~ %.3e' % mn)
for i in range(len(D)):
    for j in range(i):
        (ci, ai), (cj, aj) = D[i], D[j]; m = abs(ci - cj) - ai - aj
        print('sep', i, j, float(m), m >= 0)
mp.dps = 30
def I(c, a, n): c, a = mp.mpf(c.numerator) / c.denominator, mp.mpf(a.numerator) / a.denominator; return quad(lambda u: u ** (2 * n) * sqrt(a * a - u * u) / (c * c + 2 * c * u + a * a), [0, a])
for al in [Fr(1, 20), Fr(1, 2), Fr(3, 4), Fr(99, 100)]:
    s = mp.mpf(1) / 2; alf = mp.mpf(al.numerator) / al.denominator
    sav = [sum(4 ** (n + 1) / pi * (-binomial(alf, 2 * n)) * I(c, a, n) * s ** (2 * n) for n in range(1, 9)) for c, a in D]
    print('alpha', al, 'main %.6e' % sav[0], 'supp', ['%.3e' % x for x in sav[1:]], 'total extra %.4e (%.2f%%)' % (sum(sav[1:]), 100 * sum(sav[1:]) / sav[0]))
