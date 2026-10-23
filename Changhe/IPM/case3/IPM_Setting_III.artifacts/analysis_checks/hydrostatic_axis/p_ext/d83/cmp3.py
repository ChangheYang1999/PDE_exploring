# d = 23, type (III) (5; 2, 2, 2, 1, 1, 1): my resultant (../d81/tt.py) against the external Lambda (degree 70), and
# the C_1, C_0 resultant (degree 7) against the external branch polynomial if present
import sys, json
sys.argv = ['tt.py', '23', '5', '4', '2']
src = open('../d81/tt.py').read().split("R = report(")[0]
exec(src)
from flint import fmpz_poly
def fz(P): return fmpz_poly([int(c) for c in s.Poly(P, x).all_coeffs()[::-1]])
R = fz(s.resultant(F.as_expr(), G.as_expr(), a1))
c = json.load(open('../../../referee/x3q/d23/certificates/5_2_2_2_1_1_1.json'))
E = fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']])
q, r = divmod(R, E); print('deg R', R.degree(), 'deg ext', E.degree(), 'divides', r == 0)
X = fmpz_poly([0, 1]); Tp = fmpz_poly([-23, 5]); a = b = 0
while divmod(q, X)[1] == 0 and q.degree() > 0: q = divmod(q, X)[0]; a += 1
while divmod(q, Tp)[1] == 0 and q.degree() > 0: q = divmod(q, Tp)[0]; b += 1
print('R = c x^%d T^%d Lambda_ext:' % (a, b), q.degree() == 0, q)
print([k for k in c.keys()])
B = fz(s.resultant(N1, N0, a1)); print('Res(N1, N0) degree', B.degree(), B)
for k, v in c.items():
    if isinstance(v, dict) and 'coefficients_low_to_high' in v and k != 'Lambda':
        Eb = fmpz_poly([int(t) for t in v['coefficients_low_to_high']]); print(k, 'deg', Eb.degree(), 'divides mine:', divmod(B, Eb)[1] == 0)
