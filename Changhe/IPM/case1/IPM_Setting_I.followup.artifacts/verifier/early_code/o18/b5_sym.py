# (o18)(a): beta recurrence (26) -> (21), P(1+z), and the gamma signs on (1, 2) and (2, 4); own sympy check.
import sympy as sp
A, z = sp.symbols('A z', positive=True)
q = 4/A; a = -4 - 2/A
c0 = 2076*A**2 + 741*A - 36; c1 = -3060*A**2 + 305*A - 70; c2 = 1400*A**2 - 950*A + 50
br = c0 + c1*a/(a + q) + c2*a*(a + 1)/((a + q)*(a + q + 1))
P = 1248*A**4 - 548*A**3 + 297*A**2 - 178*A + 84
print('bracket - 2P/((2A-1)(3A-2)) =', sp.simplify(br - 2*P/((2*A - 1)*(3*A - 2))))
print('(26) prefactor / (21) prefactor:', sp.simplify((2*P/((2*A-1)*(3*A-2)))/(30*A*(4*A-3)*(8*A-1)) /
      (P/(15*A*(2*A-1)*(3*A-2)*(4*A-3)*(8*A-1)))))
print('P(1+z) =', sp.expand(P.subs(A, 1 + z)))
# a and a + q ranges
for lo, hi in [(1, 2), (2, 4)]:
    print('A in (%d,%d): a in (%s, %s), a+q in (%s, %s)' % (lo, hi, a.subs(A, hi), a.subs(A, lo),
          (a + q).subs(A, lo), (a + q).subs(A, hi)))
import mpmath as mp
for x in ['-5.9', '-5.5', '-5.1', '-4.9', '-4.6', '-2.9', '-2.5', '-2.1', '-3.4', '-3.1']:
    print('Gamma(%s) = %s' % (x, mp.nstr(mp.gamma(mp.mpf(x)), 6)))
