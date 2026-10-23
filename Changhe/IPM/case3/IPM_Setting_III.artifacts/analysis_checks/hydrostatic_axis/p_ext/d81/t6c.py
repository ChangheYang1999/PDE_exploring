# Type (VI), stage 2b (lead): Lambda_1 = Res_a(R_34, R_35) (kept factors of t6b.py) by exact Sylvester determinants
# (formal degrees in a) at x = 0, ..., B + 2 and exact integer forward-difference interpolation; factorization;
# positivity of the coefficients in powers of x - 23; comparison with the external answer (certificate_11).
import sys, pickle, time, json, sympy as s, flint
x, a = s.symbols('x a')
R = pickle.load(open('t6b_21.pkl', 'rb'))
F1, F2 = s.Poly(R[(0, 1)], a, x), s.Poly(R[(0, 2)], a, x)
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
# forward differences: f(x) = sum_k D_k binom(x, k), D_k = Delta^k f(0), integers
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
L1 = flint.fmpz_poly([int(c) for c in f.numer().coeffs()])
assert all(L1(x0) == vals[x0] for x0 in range(0, B + 3, 97))
print('Lambda_1 degree', L1.degree(), '%.0f s' % (time.time() - t0), flush=True)
c, fl = L1.factor()
print('content sign', c, 'factors (degree, multiplicity):', sorted([(g.degree(), m) for g, m in fl]), flush=True)
def shifted_positive(g):
    G = s.Poly([int(t) for t in g.coeffs()[::-1]], x)
    sh = s.Poly(G.as_expr().subs(x, x + 23), x).all_coeffs()
    return all(t > 0 for t in sh) or all(t < 0 for t in sh), min(abs(t) for t in sh)
for g, m in fl:
    if g.degree() <= 2: print('  small factor', g, 'mult', m)
    else: print('  factor degree', g.degree(), 'mult', m, 'shifted one sign, least |coefficient|:', shifted_positive(g), flush=True)
pickle.dump({'L1': [int(t) for t in L1.coeffs()]}, open('t6c_21.pkl', 'wb'))
cc = json.load(open('../../../referee/x3p/certificate_11.json'))['certificate']['regular']
def find(o, key):
    if isinstance(o, dict):
        if key in o: return o[key]
        for v in o.values():
            r = find(v, key)
            if r is not None: return r
th = find(cc, 'common_positivity')
TH = flint.fmpz_poly([int(t) for t in th['coefficients_eta_ascending']])
print('external common resultant degree', TH.degree(), flush=True)
g = L1.gcd(TH)
print('gcd(Lambda_1, external) degree', g.degree(), '| external / gcd factors:', [(h.degree(), m) for h, m in (TH // g).factor()[1]] if (TH // g).degree() > 0 else 'none', flush=True)
