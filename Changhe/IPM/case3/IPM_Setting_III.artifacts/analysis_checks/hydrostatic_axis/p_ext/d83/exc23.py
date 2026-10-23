# d = 23: exact values for (1; 5, 5, 1), n = 1, 2, 3 (b - A_1 = 8 > 2n) (lead)
from fractions import Fraction as Fr
import sympy as s
v = s.symbols('v')
d = 23; A1, b, r = 2, 10, 2
for n in (1, 2, 3):
    P2 = d + 2*n; z = Fr(P2, P2 - 1); T = P2 - d
    v1 = z*(1 + Fr(A1 - b, T))
    ps = [-(1 + A1*v1**l)/Fr(b) for l in range(1, r + 1)]
    e = [Fr(1)]
    for k in range(1, r + 1):
        e.append(sum((-1)**(i - 1)*e[k - i]*ps[i - 1] for i in range(1, k + 1))/k)
    W = sum((-1)**k*s.Rational(e[k].numerator, e[k].denominator)*v**(r - k) for k in range(r + 1))
    pi = (v - s.Rational(v1.numerator, v1.denominator))*W
    zz = s.Rational(z.numerator, z.denominator)
    val = s.diff(pi, v).subs(v, zz)
    # checks: M_1 = M_2 = 0 and the sum relation sum A_j/(z - v_j) = -T/z
    rts = s.roots(s.Poly(W, v))
    M = [1 + A1*s.Rational(v1.numerator, v1.denominator)**l + b*sum(m*rt**l for rt, m in rts.items()) for l in (1, 2)]
    S = A1/(zz - s.Rational(v1.numerator, v1.denominator)) + b*sum(m/(zz - rt) for rt, m in rts.items()) + s.Rational(T)/zz
    print('n', n, 'z', z, 'T', T, 'v_1', v1, 'e1, e2', [str(t) for t in e[1:]], "pi'(z) =", val,
          'checks', [s.simplify(t) for t in M], s.simplify(S))
