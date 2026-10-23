# Two pairs: values al (pair pi_1 = v^2 - p v + q) and be (pair pi_2 = v^2 - h v + j), fixed node 1 of value A.
# (A9): (al-be) z pi_1'(z) + T pi_1(z) = 0, (al-be) z pi_2'(z) - T pi_2(z) = 0; M_1 = M_2 = 0.
import sympy as s
A, al, be, z, T, p, x = s.symbols('A alpha beta z T p x', positive=True)
dl = al - be
q = s.solve(dl*z*(2*z - p) + T*(z**2 - p*z + s.Symbol('q')), s.Symbol('q'))[0]
h = -(A + al*p)/be                      # M_1 = A + al p + be h = 0
jj = s.Symbol('jj')
j = s.solve(dl*z*(2*z - h) - T*(z**2 - h*z + jj), jj)[0]
M2 = A + al*(p**2 - 2*q) + be*(h**2 - 2*j)
num = s.factor(s.together(M2)).as_numer_denom()
print('denominator', num[1])
P = s.Poly(s.expand(num[0]), p)
a2, a1, a0 = P.all_coeffs()
Disc = s.factor(a1**2 - 4*a2*a0)
print('a2 =', s.factor(a2)); print('Disc =', Disc)
# substitute z = x/(x-1), T = A x - d with d = A + 2 al + 2 be
d = A + 2*al + 2*be
D2 = s.factor(Disc.subs({z: x/(x-1), T: A*x - d}))
print('Disc(x) =', D2)
K = (A**2*T**2 + A*T**2*(al+be)*(1+2*z) + 2*A*T*z*(al-be)**2 + 2*T**2*z**2*(al+be)**2
     + 4*z**2*(al-be)**2*(T*(al+be) - al*be))
print('Disc == -4 al be K:', s.expand(Disc + 4*al*be*K) == 0)
# compare with the specific d=13, 15, 17 normalizations
n = s.Symbol('n', positive=True)
for (AA, aa, bb) in [(1,4,2), (3,4,2), (1,6,2), (5,4,2)]:
    dd = AA + 2*aa + 2*bb
    xx = 2*n + dd
    sub = {A: AA, al: aa, be: bb, z: xx/(xx-1), T: AA*xx - dd}
    print((AA, aa, bb), 'd =', dd, 'Disc =', s.factor(Disc.subs(sub)))
