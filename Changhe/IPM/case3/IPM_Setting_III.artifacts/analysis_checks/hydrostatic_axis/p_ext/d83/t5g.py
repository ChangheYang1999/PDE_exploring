# Type (V) generalized (lead, 2026-10-21T22:0xZ; from ../d81/t5.py, t5b.py): a class of three nodes of value al
# (U = v^3 + a1 v^2 + a2 v + a3) and a class of k nodes of value be (V = v^k + c1 v^(k-1) + ... + ck), e = k + 2.
# pi'(x) = 0 and the weighted sum give U'(x)/U(x) = bU = -T/((al - be) x) = -V'(x)/V(x). a3 from U, c1..c_{k-1}
# from M_1..M_{k-1}, ck from V; M_k, M_{k+1}, M_{k+2} remain in (a1, a2). R_ij = Res_a2(N_i, N_j); Lambda_1 =
# Res_a1(R_01, R_02), Lambda_2 = Res_a1(R_01, R_12) by exact Sylvester determinants at integer x (fixed formal size)
# and exact interpolation; gcd; sign of every factor in powers of x - (d + 2).
# usage: python3 t5g.py d A0 al be k
import sys, pickle, time, sympy as s, flint
d, A0, al, be, k = [int(t) for t in sys.argv[1:6]]
tag = 't5g_%d_%d_%d_%d_%d' % (d, A0, al, be, k)
x, a1, a2, a3, v = s.symbols('x a1 a2 a3 v'); cs = s.symbols('c1:%d' % (k + 1))
T = A0*x - d
def psums(cf, kmax):
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
U = v**3 + a1*v**2 + a2*v + a3; V = v**k + sum(c*v**(k - 1 - i) for i, c in enumerate(cs))
bU = -T/((al - be)*x)
assert s.simplify(al*bU + be*(-bU) + T/x) == 0
t0 = time.time()
sa3 = s.solve(s.diff(U, v).subs(v, x) - bU*U.subs(v, x), a3); assert len(sa3) == 1; sa3 = s.cancel(sa3[0])
pU = [s.cancel(q.subs(a3, sa3)) for q in psums([a1, a2, a3], k + 2)]
pV = psums(list(cs), k + 2)
M = lambda l: A0*(x - 1)**l + al*pU[l-1] + be*pV[l-1]
sub = {}
def full(e):
    for _ in range(k + 2): e = e.subs(sub)
    return e
for l in range(1, k):
    sl = s.solve(s.cancel(full(M(l))), cs[l-1]); assert len(sl) == 1; sub[cs[l-1]] = s.cancel(sl[0])
Vs = full(V)
sl = s.solve(s.diff(Vs, v).subs(v, x) + bU*Vs.subs(v, x), cs[k-1]); assert len(sl) == 1; sub[cs[k-1]] = s.cancel(sl[0])
def num(e):
    n_ = s.fraction(s.cancel(s.together(e)))[0]
    return s.Poly(n_, a2, a1, x).primitive()[1]
N = [num(full(M(l))) for l in (k, k + 1, k + 2)]
for l, P in zip((k, k + 1, k + 2), N):
    print('M_%d numerator: deg a2 %d, deg a1 %d, deg x %d, terms %d, %.0f s' % (l, P.degree(a2), P.degree(a1), P.degree(x), len(P.terms()), time.time() - t0), flush=True)
R = {}
for i, j in [(0, 1), (0, 2), (1, 2)]:
    r = s.Poly(s.resultant(N[i].as_expr(), N[j].as_expr(), a2), a1, x)
    R[(i, j)] = r
    print('Res_a2(N_%d, N_%d): deg a1 %d, deg x %d, %.0f s' % (i + k, j + k, r.degree(a1), r.degree(x), time.time() - t0), flush=True)
def cols(F):
    m = F.degree(a1); E = F.as_expr()
    return [[int(c) for c in s.Poly(E.coeff(a1, m - kk), x).all_coeffs()[::-1]] for kk in range(m + 1)]
def elim(F1, F2):
    C1, C2 = cols(F1), cols(F2); m1, m2 = len(C1) - 1, len(C2) - 1
    fC1 = [flint.fmpz_poly(c) for c in C1]; fC2 = [flint.fmpz_poly(c) for c in C2]
    def syl(x0):
        p = [int(c(x0)) for c in fC1]; q = [int(c(x0)) for c in fC2]; Nn = m1 + m2; rows = []
        for i in range(m2): rows.append([0]*i + p + [0]*(Nn - i - m1 - 1))
        for i in range(m1): rows.append([0]*i + q + [0]*(Nn - i - m2 - 1))
        return int(flint.fmpz_mat(rows).det())
    B = m2*F1.degree(x) + m1*F2.degree(x)
    vals = [syl(x0) for x0 in range(B + 3)]
    D = []; row = vals[:]
    while row:
        D.append(row[0]); row = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    assert all(t == 0 for t in D[B + 1:]), 'degree bound violated'
    deg = max(kk for kk in range(B + 1) if D[kk] != 0)
    f = flint.fmpq_poly([0]); bk = flint.fmpq_poly([1])
    for kk in range(deg + 1):
        if kk: bk = bk*flint.fmpq_poly([-(kk - 1), 1])/kk
        if D[kk]: f += D[kk]*bk
    assert f.denom() == 1
    L = flint.fmpz_poly([int(c) for c in f.numer().coeffs()])
    assert all(L(x0) == vals[x0] for x0 in range(0, B + 3, 7))
    print('Sylvester size', m1 + m2, 'degree bound', B, 'degree', L.degree(), '%.0f s' % (time.time() - t0), flush=True)
    return L
L1 = elim(R[(0, 1)], R[(0, 2)]); L2 = elim(R[(0, 1)], R[(1, 2)])
g = L1.gcd(L2); flg = g.factor()[1]
print('gcd degree', g.degree(), 'factors (degree, mult):', sorted([(h.degree(), m) for h, m in flg]), [(str(h), m) for h, m in flg if h.degree() <= 1], flush=True)
ok = True; core = flint.fmpz_poly([1])
for h, m in flg:
    G = s.Poly([int(t) for t in h.coeffs()[::-1]], x)
    sh = s.Poly(G.as_expr().subs(x, x + d + 2), x).all_coeffs()
    one = all(t > 0 for t in sh) or all(t < 0 for t in sh); ok = ok and one
    if h.degree() > 1: core *= h**m
    print('  factor degree', h.degree(), 'mult', m, 'one sign in powers of x - %d:' % (d + 2), one, 'least |c|', min(abs(t) for t in sh), flush=True)
print('RESULT gcd has no root x >= %d:' % (d + 2), ok, '| core degree', core.degree(), flush=True)
pickle.dump({'L1': [int(t) for t in L1.coeffs()], 'L2': [int(t) for t in L2.coeffs()], 'g': [int(t) for t in g.coeffs()], 'core': [int(t) for t in core.coeffs()]}, open(tag + '.pkl', 'wb'))
