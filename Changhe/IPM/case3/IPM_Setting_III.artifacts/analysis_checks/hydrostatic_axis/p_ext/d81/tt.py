# Two classes of three nodes (pattern (1; 2, 2, 2, 1, 1, 1) for d = 19), lead 2026-10-21T19:1xZ.  Scaled variables as in
# gen19.py: x = eta, U = v^3 + a1 v^2 + a2 v + a3 (value al), V = v^3 + c1 v^2 + c2 v + c3 (value be), e = 5.
# (A9) gives a3 and c3, M_1, M_2 give c1, c2; M_3 is linear in a2: a2 = -N0/N1 if N1 != 0; then M_4, M_5 in (a1, x).
import sys, time, sympy as s
x, a1, a2, a3, c1, c2, c3, v = s.symbols('x a1 a2 a3 c1 c2 c3 v')
def psums(cf, kmax):
    # Newton: p_l + c_1 p_(l-1) + ... + l c_l = 0 for monic v^r + c_1 v^(r-1) + ... + c_r
    r = len(cf); P = []
    for l in range(1, kmax + 1):
        t = -sum(cf[i-1]*P[l-i-1] for i in range(1, min(l-1, r) + 1))
        if l <= r: t -= l*cf[l-1]
        P.append(s.expand(t))
    return P
d, A0, al, be = [int(t) for t in sys.argv[1:5]]
T, dl = A0*x - d, al - be
U = v**3 + a1*v**2 + a2*v + a3; V = v**3 + c1*v**2 + c2*v + c3
sol = {}
sol[a3] = s.solve(dl*x*s.diff(U, v).subs(v, x) + T*U.subs(v, x), a3)[0]
pU = [s.expand(q.subs(sol)) for q in psums([a1, a2, a3], 5)]
pU = [s.cancel(q.subs(sol)) for q in psums([a1, a2, sol[a3]], 5)]
M = lambda l, pV: A0*(x-1)**l + al*pU[l-1] + be*pV[l-1]
pV = psums([c1, c2, c3], 5)
sol[c1] = s.solve(M(1, pV), c1)[0]
pV = [s.cancel(q.subs(c1, sol[c1])) for q in pV]
sol[c2] = s.solve(M(2, pV), c2)[0]
pV = [s.cancel(q.subs(c2, sol[c2])) for q in pV]
Vx = V.subs(v, x); Vpx = s.diff(V, v).subs(v, x)
e3 = (dl*x*Vpx - T*Vx).subs({c1: sol[c1]}).subs({c2: sol[c2]})
sol[c3] = s.solve(e3, c3)[0]
pV = [s.cancel(q.subs(c3, sol[c3])) for q in pV]
M3 = s.cancel(s.together(M(3, pV))); n3, d3 = s.fraction(M3)
P3 = s.Poly(n3, a2)
print('deg_a2 M3 numerator', P3.degree(), 'denominator', s.factor(d3), flush=True)
N1, N0 = P3.coeff_monomial(a2), P3.coeff_monomial(1)
print('N1 =', s.factor(N1), flush=True)
def numer(e):
    nm = s.fraction(s.cancel(s.together(e)))[0]
    return s.Poly(nm, a1, x).primitive()[1]
t0 = time.time()
F = numer(M(4, pV).subs(a2, -N0/N1)); G = numer(M(5, pV).subs(a2, -N0/N1))
print('degrees in a1:', F.degree(a1), G.degree(a1), '%.0f s' % (time.time() - t0), flush=True)
def report(R, tag):
    R = s.Poly(R, x).primitive()[1]
    if R.LC() < 0: R = -R
    co = s.Poly(R.as_expr().subs(x, x + d + 2), x).all_coeffs()
    pos = all(c > 0 for c in co)
    nr = None if pos else R.count_roots(d + 2, None)
    print(tag, 'degree', R.degree(), 'least', min(co), 'all positive', pos, 'roots >= d+2', nr, s.factor_list(R)[1][:0], flush=True)
    return R
R = report(s.resultant(F.as_expr(), G.as_expr(), a1), 'Res_a1(M4, M5)')
R0 = report(s.resultant(s.Poly(N1, a1).as_expr(), s.Poly(N0, a1).as_expr(), a1), 'Res_a1(N1, N0)')
