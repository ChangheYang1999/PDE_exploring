# d = 23, (1; 3, 3, 1, 1, 1, 1, 1) type (I) (pair of value 6, five nodes of value 2): Lambda has a real root >= 25 (lead)
import sys, pickle
src = open('../d81/gen21.py').read().split('CASES = ')[0]
exec(src)
F, G = two(23, 1, 6, 2, 5)
R = s.Poly(s.resultant(F.as_expr(), G.as_expr(), p), x).primitive()[1]
if R.LC() < 0: R = -R
pickle.dump({'F': F.as_expr(), 'G': G.as_expr(), 'R': R.as_expr()}, open('case25.pkl', 'wb'))
print('degree', R.degree())
fl = s.factor_list(R.as_expr())[1]
print('factors (degree, mult):', [(s.Poly(f, x).degree(), m) for f, m in fl])
for f, m in fl:
    P = s.Poly(f, x)
    rr = P.intervals(inf=25, sup=None) if False else None
    nr = P.count_roots(25, None)
    if nr:
        roots = [r for r in P.real_roots() if r >= 25]
        print('factor degree', P.degree(), 'mult', m, 'roots >= 25:', [s.N(r, 30) for r in roots])
        for r in roots:
            z = s.N(r, 40); n = (z - 23)/2
            print('   eta =', z, ' n =', n)
