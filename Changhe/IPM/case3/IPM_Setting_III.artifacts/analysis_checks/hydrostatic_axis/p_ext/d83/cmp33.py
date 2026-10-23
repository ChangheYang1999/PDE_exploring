# d = 23, gen23 case 33 (type II e = 7, (1;3,2,1,1,1,1,1,1)): my resultant R = Res_p(F, G) recomputed by exact
# Sylvester determinants at 0..B+1 (B the maximum-weight assignment bound of the x-degrees) and the Newton form, then
# compared with the external Lambda as in cmp12.py and with the gen23 values (degree 294, least coefficient in powers
# of x - 25). (lead, 2026-10-22T00:1xZ)
import sys, time, json, numpy as np, flint
from scipy.optimize import linear_sum_assignment
src = open('gen23.py').read().split('sel = ')[0]
exec(src)
t0 = time.time(); i = 33; kind, args = C23[i]
F, G = three(23, *args)
def cols(P):
    P = s.Poly(P.as_expr(), p); return [flint.fmpz_poly([int(c) for c in s.Poly(cc, x).all_coeffs()[::-1]]) for cc in P.all_coeffs()]
C1, C2 = cols(F), cols(G); m1, m2 = len(C1) - 1, len(C2) - 1; Nn = m1 + m2
def rows(P, Q, z):
    out = []
    for r in range(m2): out.append([z]*r + P + [z]*(Nn - r - m1 - 1))
    for r in range(m1): out.append([z]*r + Q + [z]*(Nn - r - m2 - 1))
    return out
W = np.full((Nn, Nn), -10**7, dtype=np.int64)
for r, row in enumerate(rows(C1, C2, None)):
    for j, e in enumerate(row):
        if e is not None and e.degree() >= 0: W[r, j] = e.degree()
ri, ci = linear_sum_assignment(W, maximize=True); B = int(W[ri, ci].sum())
print('Sylvester size', Nn, 'degree bound', B, flush=True)
vals = [int(flint.fmpz_mat(rows([int(c(x0)) for c in C1], [int(c(x0)) for c in C2], 0)).det()) for x0 in range(B + 2)]
D = []; row = vals[:]
while row:
    D.append(row[0]); row = [row[j + 1] - row[j] for j in range(len(row) - 1)]
assert D[B + 1] == 0
n = max(k for k in range(B + 1) if D[k] != 0); g = flint.fmpq_poly([D[n]])
for k in range(n - 1, -1, -1): g = g*flint.fmpq_poly([-k, 1])/(k + 1) + D[k]
assert all(int(c.q) == 1 for c in g.coeffs())
R = flint.fmpz_poly([int(c.p) for c in g.coeffs()]); assert all(int(R(x0)) == vals[x0] for x0 in range(B + 2))
print('R: degree', R.degree(), '%.0f s' % (time.time() - t0), flush=True)
Rp = s.Poly(s.Poly([int(c) for c in R.coeffs()[::-1]], x).as_expr().subs(x, x + 25), x).all_coeffs()
cont = 0
for c in Rp: cont = __import__('math').gcd(cont, int(c))
print('R in powers of x - 25: number of coefficients', len(Rp), 'all of one sign', all(c > 0 for c in Rp) or all(c < 0 for c in Rp), flush=True)
C = '../../../referee/x3q/d23/certificates/'
A0, wa, wb, wq = args[:4]; k = args[4]; mu = [wa//2, wb//2] + [wq//2]*k
pid = '%d_%s' % (A0, '_'.join(map(str, sorted(mu, reverse=True))))
c = json.load(open(C + pid + '.json'))
E = flint.fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']])
q, r = divmod(R, E); out = [i, kind, args, pid, 'deg R', R.degree(), 'deg ext', E.degree(), 'divides', r == 0]
if r == 0:
    T = flint.fmpz_poly([-23, A0]); X = flint.fmpz_poly([0, 1]); a_ = b_ = 0
    while q.degree() > 0 and divmod(q, X)[1] == 0: q = divmod(q, X)[0]; a_ += 1
    while q.degree() > 0 and divmod(q, T)[1] == 0: q = divmod(q, T)[0]; b_ += 1
    out += ['x^%d T^%d' % (a_, b_), 'rest deg', q.degree()]
print(*out, '%.0f s' % (time.time() - t0), flush=True)
