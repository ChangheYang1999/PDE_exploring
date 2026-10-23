# d = 21, n = 1: exact values for the text of A.3.80 (lead)
from fractions import Fraction as Fr
import sympy as s
v = s.symbols('v')
d = 21; n = 1; P2 = d + 2*n; z = Fr(P2, P2 - 1); T = P2*1 - d
for A1, b, r in [(4, 8, 2), (2, 6, 3)]:
    v1 = z*(1 + Fr(A1 - b, T))
    ps = [-(1 + A1*v1**l)/Fr(b) for l in range(1, r + 1)]
    e = [Fr(1)]
    for k in range(1, r + 1):
        e.append(sum((-1)**(i - 1)*e[k - i]*ps[i - 1] for i in range(1, k + 1))/k)
    W = sum((-1)**k*s.Rational(e[k].numerator, e[k].denominator)*v**(r - k) for k in range(r + 1))
    pi = (v - s.Rational(v1.numerator, v1.denominator))*W
    val = s.diff(pi, v).subs(v, s.Rational(z.numerator, z.denominator))
    print('A_1 =', A1, 'b =', b, 'v_1 =', v1, 'elementary symmetric functions of the others:', [str(t) for t in e[1:]], "pi'(z) =", val)
# two pairs (1; 3, 3, 2, 2): A_1 = 6, A_3 = 4, the lemma's K at n = 1
A0, A1, A3 = 1, 6, 4
K = (A0**2*T**2 + A0*(A1 + A3)*(1 + 2*z)*T**2 + 2*A0*(A1 - A3)**2*z*T + 2*(A1 + A3)**2*z**2*T**2
     + 4*(A1 - A3)**2*z**2*(T*(A1 + A3) - A1*A3))
print('two pairs n = 1: T =', T, 'T (A_1 + A_3) - A_1 A_3 =', T*(A1 + A3) - A1*A3, 'K =', K, float(K))
for nn in range(1, 6):
    P2 = d + 2*nn; zz = Fr(P2, P2 - 1); TT = P2 - d
    KK = (A0**2*TT**2 + A0*(A1 + A3)*(1 + 2*zz)*TT**2 + 2*A0*(A1 - A3)**2*zz*TT + 2*(A1 + A3)**2*zz**2*TT**2
          + 4*(A1 - A3)**2*zz**2*(TT*(A1 + A3) - A1*A3))
    print('  n', nn, 'K', KK)
