# (1;4,4,1), d = 19: exceptional node a = z(1 - 3/n) (gap 3 > n), pair of value 8 with W = v^2 - h v + j.
import sympy as s
n, v = s.symbols('n v', positive=True)
d = 19; eta = 2*n + d; z = eta/(eta - 1)
a = z*(1 - s.Rational(3)/n)
h = -(1 + 2*a)/8
j = (1 + 2*a**2 + 8*h**2)/16
W = v**2 - h*v + j
M1 = 1 + 2*a + 8*h
M2 = 1 + 2*a**2 + 8*(h**2 - 2*j)
assert s.simplify(M1) == 0 and s.simplify(M2) == 0
dp = s.factor(s.together(s.diff((v - a)*W, v).subs(v, z)))
print('pi\'(z) =', dp)
for nn in (1, 2):
    print(nn, dp.subs(n, nn))
num, den = s.fraction(dp)
print('numerator real roots:', s.Poly(num, n).count_roots(1, 3), [r.evalf(6) for r in s.real_roots(s.Poly(num, n))])
