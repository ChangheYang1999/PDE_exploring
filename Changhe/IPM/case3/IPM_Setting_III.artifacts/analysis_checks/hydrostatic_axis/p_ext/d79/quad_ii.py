# lead (2026-10-21T18:35Z): the quadratic in b_1 for d = 15, A_0 = 3, values (4, 4, 2, 2), in the normalization of the
# d = 13 text of A.3.80 (b_2, b_4 from (A9) with alpha - beta = 2; b_3 from M_1)
import sympy as sp
n,b1,b2,b3,b4=sp.symbols('n b_1 b_2 b_3 b_4')
for A0,d in [(1,13),(3,15)]:
    z=sp.Rational(1)*(2*n+d)/(2*n+d-1); T=A0*(2*n+d)-d
    s2=sp.solve(2*z*(2*z-b1)+T*(z**2-b1*z+b2),b2)[0]
    s4=sp.solve(2*z*(2*z-b3)-T*(z**2-b3*z+b4),b4)[0]
    s3=sp.solve(A0+4*b1+2*b3,b3)[0]
    M2=(A0+4*(b1**2-2*b2)+2*(b3**2-2*b4)).subs({b2:s2,b4:s4}).subs(b3,s3)
    M2=sp.factor(sp.together(M2)); nu,de=sp.fraction(M2)
    print(d,'T =',sp.factor(T),' b_2 =',sp.factor(s2),' b_4 =',sp.factor(s4))
    print('   denominator',sp.factor(de)); P=sp.Poly(sp.expand(nu),b1)
    print('   numerator',[sp.factor(c) for c in P.all_coeffs()])
    print('   disc',sp.factor(P.discriminant()))
