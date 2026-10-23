# Stage 2 of sp2.py: Lambda(x) = Res_a(F1, F2) with F1, F2 the irreducible factors of H1, R3 (pivots removed), by exact
# Sylvester determinants at integer points and exact interpolation (lead, 2026-10-21T19:1xZ).
import sys, pickle, time, sympy as s, flint
from fractions import Fraction
x, a = s.symbols('x a')
tag = sys.argv[1]; d = int(tag.split('_')[0])
D = pickle.load(open('sp2_%s.pkl' % tag, 'rb'))
def core(E):
    fl = s.factor_list(E)[1]
    big = [f for f, k in fl if s.Poly(f, a, x).degree(a) > 1]
    assert len(big) == 1, [(s.Poly(f, a, x).degree(a), k) for f, k in fl]
    return s.Poly(big[0], a, x)
F1, F2 = core(D['H1']), core(D['R3'])
print('F1', F1.degree(a), F1.degree(x), 'F2', F2.degree(a), F2.degree(x), 'equal?', F1 == F2 or F1 == -F2, flush=True)
def cols(F):
    m = F.degree(a)
    return [[int(c) for c in s.Poly(F.as_expr().coeff(a, m - i), x).all_coeffs()[::-1]] for i in range(m + 1)]  # lc first, each low-to-high in x
C1, C2 = cols(F1), cols(F2)
m1, m2 = len(C1) - 1, len(C2) - 1
def ev(cl, x0): return sum(c*x0**i for i, c in enumerate(cl))
def syl(x0):
    p = [ev(c, x0) for c in C1]; q = [ev(c, x0) for c in C2]
    N = m1 + m2; rows = []
    for i in range(m2): rows.append([0]*i + p + [0]*(N - i - m1 - 1))
    for i in range(m1): rows.append([0]*i + q + [0]*(N - i - m2 - 1))
    return int(flint.fmpz_mat(rows).det())
B = m2*F1.degree(x) + m1*F2.degree(x)
pts = list(range(0, B + 3)); t0 = time.time()
vals = [syl(x0) for x0 in pts]
print('evaluations', len(pts), 'degree bound', B, '%.0f s' % (time.time() - t0), flush=True)
# Newton divided differences, exact
n = len(pts); c = [Fraction(v) for v in vals]
for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        c[i] = (c[i] - c[i - 1]) / (pts[i] - pts[i - j])
assert all(ci == 0 for ci in c[B + 1:]), 'degree bound violated'
P = s.Poly(0, x); basis = s.Poly(1, x)
for j in range(B + 1):
    P += basis*s.Rational(c[j].numerator, c[j].denominator); basis *= s.Poly(x - pts[j], x)
P = s.Poly(P, x); assert all(q.is_integer for q in P.all_coeffs())
R = P.primitive()[1]
if R.LC() < 0: R = -R
print('Lambda degree', R.degree(), '%.0f s' % (time.time() - t0), flush=True)
fl = s.factor_list(R.as_expr())[1]
print('factors (degree, multiplicity):', [(s.Poly(f, x).degree(), k) for f, k in fl], flush=True)
for f, k in fl:
    f = s.Poly(f, x)
    co = s.Poly(f.as_expr().subs(x, x + d + 2), x).all_coeffs()
    pos = all(q > 0 for q in co) or all(q < 0 for q in co)
    print(' factor deg', f.degree(), 'mult', k, 'coefficients of f(d + 2 + m) one sign:', pos,
          '' if pos else 'real roots >= d+2: %d' % f.count_roots(d + 2, None), flush=True)
pickle.dump({'Lambda': R.as_expr()}, open('sp2b_%s.pkl' % tag, 'wb'))
