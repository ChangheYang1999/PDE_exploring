# Quartic type (VI) at d = 23, pattern (1; 3, 2, 2, 1, 1, 1, 1) (lead, 2026-10-22T00:1xZ): EXACT version of vi4m.py.
# Lambda_1 = Res_a(r01, r02), Lambda_2 = Res_a(r01, r03) computed exactly: exact Sylvester determinants (fmpz_mat) at
# the integers 0..B+1, where B is a proven degree bound (maximum-weight assignment of the x-degrees of the entries), then
# exact forward differences (asserted zero beyond B) and the Newton form; then the exact gcd, its factors x and x - 23
# removed, the rest compared with the external core and checked for one sign in powers of x - 25.
# usage: python3 vi4x.py [test]     (values are checkpointed in vi4x_<st>.vals.pkl)
import sys, os, json, pickle, time, sympy as s, flint, numpy as np
from scipy.optimize import linear_sum_assignment
x, a = s.symbols('x a'); t0 = time.time(); tag = 't6g_23_1_6_4_2_4'
R = {st: s.Poly(pickle.load(open(tag + '_' + st + '.pkl', 'rb')), a, x) for st in ('r01', 'r02', 'r03')}
def cols(F):
    m = F.degree(a); E = F.as_expr()
    return [flint.fmpz_poly([int(c) for c in s.Poly(E.coeff(a, m - kk), x).all_coeffs()[::-1]]) for kk in range(m + 1)]
Cs = {st: cols(R[st]) for st in R}
def sylrows(P, Q):
    m1, m2 = len(P) - 1, len(Q) - 1; Nn = m1 + m2; rows = []
    for i in range(m2): rows.append([None]*i + P + [None]*(Nn - i - m1 - 1))
    for i in range(m1): rows.append([None]*i + Q + [None]*(Nn - i - m2 - 1))
    return rows
def bound(st1, st2):
    rows = sylrows(Cs[st1], Cs[st2]); Nn = len(rows)
    W = np.full((Nn, Nn), -10**7, dtype=np.int64)
    for i, r in enumerate(rows):
        for j, e in enumerate(r):
            if e is not None and e.degree() >= 0: W[i, j] = e.degree()
    ri, ci = linear_sum_assignment(W, maximize=True); B = int(W[ri, ci].sum()); assert B >= 0
    Bs = (len(Cs[st2]) - 1)*R[st1].degree(x) + (len(Cs[st1]) - 1)*R[st2].degree(x)
    return B, Bs, Nn
def syl(st1, st2, x0):
    rows = sylrows([int(c(x0)) for c in Cs[st1]], [int(c(x0)) for c in Cs[st2]])
    return int(flint.fmpz_mat([[0 if e is None else e for e in r] for r in rows]).det())
def exact_res(st1, st2):
    B, Bs, Nn = bound(st1, st2)
    print('Res_a(%s, %s): Sylvester size %d, assignment degree bound %d (column bound %d)' % (st1, st2, Nn, B, Bs), flush=True)
    fn = 'vi4x_%s_%s.vals.pkl' % (st1, st2)
    vals = pickle.load(open(fn, 'rb')) if os.path.exists(fn) else []
    for x0 in range(len(vals), B + 2):
        vals.append(syl(st1, st2, x0))
        if x0 % 250 == 0:
            pickle.dump(vals, open(fn, 'wb')); print('   %d of %d values, %d bits, %.0f s' % (x0 + 1, B + 2, vals[-1].bit_length(), time.time() - t0), flush=True)
    pickle.dump(vals, open(fn, 'wb'))
    D = []; row = vals[:B + 2]
    while row:
        D.append(row[0]); row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    assert D[B + 1] == 0, 'degree bound violated'
    n = max(kk for kk in range(B + 1) if D[kk] != 0)
    g = flint.fmpq_poly([D[n]])
    for kk in range(n - 1, -1, -1):
        g = g*flint.fmpq_poly([-kk, 1])/(kk + 1) + D[kk]
    assert all(int(c.q) == 1 for c in g.coeffs()), 'not integral'
    f = flint.fmpz_poly([int(c.p) for c in g.coeffs()]); assert f.degree() == n
    assert all(int(f(x0)) == vals[x0] for x0 in range(0, B + 2, 97)), 'values not reproduced'
    print('   exact Res_a(%s, %s): degree %d, max coefficient bits %d, %.0f s' % (st1, st2, n, max(abs(int(c)).bit_length() for c in f.coeffs()), time.time() - t0), flush=True)
    for pr in (2**61 - 1, 2**31 - 1):
        assert int(f.coeffs()[-1]) % pr != 0
    return f
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    for st1, st2 in (('r01', 'r02'), ('r01', 'r03')):
        print(bound(st1, st2), flush=True)
        for x0 in (100, 2400):
            t1 = time.time(); v = syl(st1, st2, x0); print(x0, v.bit_length(), '%.2f s' % (time.time() - t1), flush=True)
    sys.exit()
L1 = exact_res('r01', 'r02'); L2 = exact_res('r01', 'r03')
pickle.dump({'L1': [int(c) for c in L1.coeffs()], 'L2': [int(c) for c in L2.coeffs()]}, open('vi4x_L.pkl', 'wb'))
c = json.load(open('../../../referee/x3q/d23/certificates/1_3_2_2_1_1_1_1.json'))
def P(Fi):
    co = [0]*(max(t[0][2] for t in Fi) + 1)
    for e, v in Fi: co[e[2]] = int(v)
    return flint.fmpz_poly(co)
def prim(f):
    co = [int(t) for t in f.coeffs()]; g = 0
    for t in co: g = __import__('math').gcd(g, t)
    sg = 1 if co[-1] > 0 else -1
    return flint.fmpz_poly([sg*t//g for t in co])
F = [prim(P(Fi)) for Fi in c['final_resultants']]
print('my Lambda_1 equal to the external first final resultant up to a constant:', prim(L1) == F[0], flush=True)
g = L1.gcd(L2); print('exact gcd: degree %d, %.0f s' % (g.degree(), time.time() - t0), flush=True)
X = flint.fmpz_poly([0, 1]); T = flint.fmpz_poly([-23, 1]); mx = mt = 0
while divmod(g, X)[1] == 0 and g.degree() > 0: g = divmod(g, X)[0]; mx += 1
while divmod(g, T)[1] == 0 and g.degree() > 0: g = divmod(g, T)[0]; mt += 1
E = prim(flint.fmpz_poly([int(t) for t in c['Lambda']['coefficients_low_to_high']]))
print('gcd = c x^%d (x - 23)^%d h, deg h %d; h equal to the external core up to a constant:' % (mx, mt, g.degree()), prim(g) == E, flush=True)
sh = [int(t) for t in g(flint.fmpz_poly([25, 1])).coeffs()]
print('h in powers of x - 25: all coefficients of one sign:', all(t > 0 for t in sh) or all(t < 0 for t in sh), '; least |c|', min(abs(t) for t in sh), flush=True)
print('RESULT exact gcd has no root x >= 25:', all(t > 0 for t in sh) or all(t < 0 for t in sh), '%.0f s' % (time.time() - t0), flush=True)
