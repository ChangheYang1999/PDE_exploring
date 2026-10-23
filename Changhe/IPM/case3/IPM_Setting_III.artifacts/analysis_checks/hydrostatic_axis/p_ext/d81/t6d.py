# Type (VI), stage 2c (lead): Lambda_2 = Res_a(R_34, R_45) as in t6c.py; gcd with Lambda_1; factors and positivity
import sys, pickle, time, json, sympy as s, flint
x, a = s.symbols('x a')
F1 = s.Poly(pickle.load(open('t6b_21.pkl', 'rb'))[(0, 1)], a, x)
F2 = s.Poly(pickle.load(open('t6b45_21.pkl', 'rb'))[(1, 2)], a, x)
def cols(F):
    m = F.degree(a); E = F.as_expr()
    return [[int(c) for c in s.Poly(E.coeff(a, m - k), x).all_coeffs()[::-1]] for k in range(m + 1)]
C1, C2 = cols(F1), cols(F2); m1, m2 = len(C1) - 1, len(C2) - 1
fC1 = [flint.fmpz_poly(c) for c in C1]; fC2 = [flint.fmpz_poly(c) for c in C2]
def syl(x0):
    p = [int(c(x0)) for c in fC1]; q = [int(c(x0)) for c in fC2]; Nn = m1 + m2; rows = []
    for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
    for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
    return int(flint.fmpz_mat(rows).det())
B = m2*F1.degree(x) + m1*F2.degree(x); t0 = time.time()
vals = [syl(x0) for x0 in range(B + 3)]
print('Sylvester size', m1 + m2, 'evaluations', len(vals), 'degree bound', B, '%.0f s' % (time.time() - t0), flush=True)
D = []; row = vals[:]
while row:
    D.append(row[0]); row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
assert all(t == 0 for t in D[B + 1:]), 'degree bound violated'
deg = max(k for k in range(B + 1) if D[k] != 0)
f = flint.fmpq_poly([0]); bk = flint.fmpq_poly([1])
for k in range(deg + 1):
    if k: bk = bk*flint.fmpq_poly([-(k - 1), 1])/k
    if D[k]: f += D[k]*bk
assert f.denom() == 1
L2 = flint.fmpz_poly([int(c) for c in f.numer().coeffs()])
assert all(L2(x0) == vals[x0] for x0 in range(0, B + 3, 97))
print('Lambda_2 degree', L2.degree(), '%.0f s' % (time.time() - t0), flush=True)
c, fl = L2.factor()
print('factors of Lambda_2 (degree, multiplicity):', sorted([(g.degree(), m) for g, m in fl]), flush=True)
L1 = flint.fmpz_poly(pickle.load(open('t6c_21.pkl', 'rb'))['L1'])
g = L1.gcd(L2)
cg, flg = g.factor()
print('gcd(Lambda_1, Lambda_2) degree', g.degree(), 'factors:', sorted([(h.degree(), m) for h, m in flg]), [str(h) for h, m in flg if h.degree() <= 1], flush=True)
for h, m in flg:
    if h.degree() > 1:
        G = s.Poly([int(t) for t in h.coeffs()[::-1]], x)
        sh = s.Poly(G.as_expr().subs(x, x + 23), x).all_coeffs()
        print('  factor degree', h.degree(), 'shifted coefficients one sign', all(t > 0 for t in sh) or all(t < 0 for t in sh), 'least |c|', min(abs(t) for t in sh), flush=True)
pickle.dump({'L2': [int(t) for t in L2.coeffs()]}, open('t6d_21.pkl', 'wb'))
