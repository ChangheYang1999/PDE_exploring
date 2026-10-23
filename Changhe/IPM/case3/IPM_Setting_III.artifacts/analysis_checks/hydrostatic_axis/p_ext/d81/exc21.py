# d = 21: the patterns (1; 4, 4, 2) and (1; 3, 3, 3, 1) (one lower multiplicity) and (1; 3, 3, 2, 2) (two pairs),
# symbolically in real n >= 1 (lead, cross-check of the external answer x3p)
import sympy as s
n, v, p, h = s.symbols('n v p h')
d = 21; D = d + 2*n; z = D/(D - 1)
def newton(ps):  # power sums p_1..p_r -> elementary e_1..e_r
    e = [1]
    for k in range(1, len(ps) + 1):
        e.append(s.together(sum((-1)**(i - 1)*e[k - i]*ps[i - 1] for i in range(1, k + 1))/k))
    return e
def lower(A0, mu, nu, r):  # r nodes of weight 2 mu (group W), one node of weight 2 nu, e = r
    a = z*(1 - s.Rational(mu - nu)/n)
    ps = [-(A0 + 2*nu*a**l)/(2*mu) for l in range(1, r + 1)]
    e = newton(ps)
    W = sum((-1)**k*e[k]*v**(r - k) for k in range(r + 1))
    pp = s.diff((v - a)*W, v).subs(v, z)
    N, Dn = s.fraction(s.factor(s.together(pp)))
    return s.factor(N), s.factor(Dn)
for A0, mu, nu, r in [(1, 4, 2, 2), (1, 3, 1, 3)]:
    N, Dn = lower(A0, mu, nu, r)
    Pn = s.Poly(N, n); sh = s.Poly(Pn.as_expr().subs(n, n + 1), n).all_coeffs()
    print((A0, mu, nu, r), 'pi\'(z) numerator', N, '| denominator', Dn, '| N(n+1) coefficients', sh,
          'one sign', all(c > 0 for c in sh) or all(c < 0 for c in sh), '| value n=1', s.nsimplify(N.subs(n, 1)/Dn.subs(n, 1)))
# two pairs (1; 3, 3, 2, 2): U (weight 6) and W (weight 4); U'(z)/U(z) = be, W'(z)/W(z) = -be (pi'(z) = 0), and
# 1/(z - 1) + 6 be - 4 be = d/z (A0 = 1)
be = s.together((d/z - (D - 1))/2)
q = s.solve(s.Eq(2*z - p, be*(z**2 - p*z + s.Symbol('q'))), s.Symbol('q'))[0]
hh = -(1 + 12*p/2)/4*1  # M_1: 1 + 6 p + 4 h = 0
hh = -(1 + 6*p)/4
j = s.solve(s.Eq(2*z - hh, -be*(z**2 - hh*z + s.Symbol('j'))), s.Symbol('j'))[0]
M2 = 1 + 6*(p**2 - 2*q) + 4*(hh**2 - 2*j)
num = s.factor(s.fraction(s.together(M2))[0])
P2 = s.Poly(num, p); print('two pairs: M_2 numerator degree in p', P2.degree())
disc = s.factor(P2.discriminant())
print('discriminant', disc)
Pd = s.Poly(s.fraction(s.together(disc))[0], n)
sh = s.Poly(Pd.as_expr().subs(n, n + 1), n).all_coeffs()
print('discriminant numerator at n + 1:', sh, 'one sign', all(c > 0 for c in sh) or all(c < 0 for c in sh))
