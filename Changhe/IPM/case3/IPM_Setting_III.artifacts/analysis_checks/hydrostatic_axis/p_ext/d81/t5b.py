# Type (V), stage 2 (lead): R_ij = Res_a2(N_i, N_j) by sympy, then Lambda_ij = Res_a1(R_45, R_ij) by exact Sylvester
# determinants at integer x and exact interpolation (as in sp2b.py); gcd of the eliminants; positivity of the
# coefficients in powers of x - 23.
import sys, pickle, time, json, sympy as s, flint
from fractions import Fraction
x, a1, a2 = s.symbols('x a1 a2')
N = [s.Poly(e, a2, a1, x) for e in pickle.load(open('t5_21.pkl', 'rb'))['N']]
t0 = time.time()
R = {}
for i, j in [(0, 1), (0, 2), (1, 2)]:
    r = s.Poly(s.resultant(N[i].as_expr(), N[j].as_expr(), a2), a1, x)
    R[(i, j)] = r
    print('Res_a2(N_%d, N_%d): deg a1 %d, deg x %d, %.0f s' % (i + 4, j + 4, r.degree(a1), r.degree(x), time.time() - t0), flush=True)
def cols(F, var):
    m = F.degree(var); E = F.as_expr()
    return [[int(c) for c in s.Poly(E.coeff(var, m - k), x).all_coeffs()[::-1]] for k in range(m + 1)]
def elim(F1, F2):
    C1, C2 = cols(F1, a1), cols(F2, a1); m1, m2 = len(C1) - 1, len(C2) - 1
    ev = lambda cl, x0: sum(c*x0**i for i, c in enumerate(cl))
    def syl(x0):
        p = [ev(c, x0) for c in C1]; q = [ev(c, x0) for c in C2]; Nn = m1 + m2; rows = []
        for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
        for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
        return int(flint.fmpz_mat(rows).det())
    B = m2*F1.degree(x) + m1*F2.degree(x); pts = list(range(0, B + 3)); vals = [syl(x0) for x0 in pts]
    n = len(pts); c = [Fraction(v) for v in vals]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            c[i] = (c[i] - c[i - 1])/(pts[i] - pts[i - j])
    assert all(ci == 0 for ci in c[B + 1:]), 'degree bound violated'
    P = s.Poly(0, x); basis = s.Poly(1, x)
    for j in range(B + 1):
        P += basis*s.Rational(c[j].numerator, c[j].denominator); basis *= s.Poly(x - pts[j], x)
    return s.Poly(P, x), B
L = []
for key in [(0, 2), (1, 2)]:
    P, B = elim(R[(0, 1)], R[key])
    print('Res_a1(R_45, R_%d%d): degree bound %d, degree %d, zero %s, %.0f s' % (key[0] + 4, key[1] + 4, B, P.degree(), P.is_zero, time.time() - t0), flush=True)
    L.append(P)
G = s.gcd(L[0], L[1]); G = s.Poly(G, x)
fl = s.factor_list(G.as_expr())[1]
print('gcd degree', G.degree(), 'factors (degree, multiplicity):', [(s.Poly(f, x).degree(), k) for f, k in fl], flush=True)
big = s.Poly(s.prod([f**k for f, k in fl if s.Poly(f, x).degree() > 1]), x)
big = big.primitive()[1]; big = -big if big.LC() < 0 else big
sh = s.Poly(big.as_expr().subs(x, x + 23), x).all_coeffs()
print('core degree', big.degree(), 'shifted coefficients all positive', all(c > 0 for c in sh), 'least', min(sh), flush=True)
for f, k in fl:
    if s.Poly(f, x).degree() == 1: print('  linear factor', f, 'multiplicity', k)
c = json.load(open('../../../referee/x3p/certificate_13.json'))
def find(o):
    if isinstance(o, dict):
        if 'coefficients_eta_ascending' in o: return o
        for v in o.values():
            r = find(v)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = find(v)
            if r: return r
th = [int(t) for t in find(c)['coefficients_eta_ascending']]
TH = s.Poly(sum(cc*x**i for i, cc in enumerate(th)), x)
q, r = s.div(big, TH)
print('external Lambda degree', TH.degree(), '| core / external: quotient', q, 'remainder zero', r.is_zero, flush=True)
pickle.dump({'L': [P.as_expr() for P in L], 'core': big.as_expr()}, open('t5b_21.pkl', 'wb'))
