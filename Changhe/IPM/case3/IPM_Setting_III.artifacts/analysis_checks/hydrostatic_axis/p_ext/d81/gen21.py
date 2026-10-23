# gen21.py = gen19.py with the d = 21 cases (lead, 2026-10-21T19:5xZ). gen.py extended (lead, 2026-10-21T18:5xZ): three() with a class of any size k; d = 19 cases; real roots >= d + 2.
# Original header: independent generic certificate.  Scaled variables: x = 2P = 2n + d >= d + 2,
# nodes y = (x - 1) v, fixed node x - 1 of value A0, point z -> x.  Conditions:
#   A0 (x-1)^l + sum_j A_j y_j^l = 0 (1 <= l <= e),  pi'(x) = 0,  sum_j A_j/(x - y_j) = -T/x,  T = A0 x - d.
# Power sums are traces of powers of the companion matrix (different route from Newton recursions).
import sys, sympy as s
from math import comb
x, p, v = s.symbols('x p v')

def psums(coeffs, kmax):
    # monic v^m + c1 v^(m-1) + ... + cm ; returns [p_1..p_kmax] as traces of C^k
    m = len(coeffs)
    C = s.zeros(m, m)
    for i in range(1, m):
        C[i, i-1] = 1
    for i in range(m):
        C[i, m-1] = -coeffs[m-1-i]
    out, Ck = [], s.eye(m)
    for k in range(kmax):
        Ck = (Ck*C).applyfunc(s.expand)
        out.append(s.cancel(Ck.trace()))
    return out

def numer(e):
    nm = s.cancel(s.together(e)).as_numer_denom()[0]
    return s.Poly(nm, p, x).primitive()[1]

def two(d, A0, al, be, m):
    # U = v^2 - p v + q (value al), V of degree m (value be); e = m + 1
    T, dl = A0*x - d, al - be
    q = s.cancel((-dl*x*(2*x - p) + T*p*x - T*x**2)/T)          # dl x U'(x) + T U(x) = 0
    hU = psums([-p, q], m + 1)
    cs = []
    for k in range(1, m):
        c = s.Symbol('c%d' % k)
        Mk = A0*(x-1)**k + al*hU[k-1] + be*psums(cs + [c] + [0]*(m-k), k)[k-1]
        sol = s.solve(Mk, c)
        assert len(sol) == 1
        cs.append(s.cancel(sol[0]))
    cm = s.Symbol('cm')
    V = v**m + sum(cc*v**(m-1-i) for i, cc in enumerate(cs)) + cm
    sol = s.solve(dl*x*s.diff(V, v).subs(v, x) - T*V.subs(v, x), cm)
    assert len(sol) == 1
    cs.append(s.cancel(sol[0]))
    hV = psums(cs, m + 1)
    F = numer(A0*(x-1)**m + al*hU[m-1] + be*hV[m-1])
    G = numer(A0*(x-1)**(m+1) + al*hU[m] + be*hV[m])
    return F, G

def three(d, A0, wa, wb, wq, k=2):
    # singletons p (value wa), b (value wb); class V = v^k + c1 v^(k-1) + ... + ck (value wq); e = k + 1
    T, da, db = A0*x - d, wa - wq, wb - wq
    bb = s.Symbol('bb')
    sol = s.solve(x*(da*(x - bb) + db*(x - p)) + T*(x - p)*(x - bb), bb)   # (A10) cleared
    assert len(sol) == 1
    b = s.cancel(sol[0])
    cs = []
    for l in range(1, k + 1):
        c = s.Symbol('c%d' % l)
        Ml = A0*(x-1)**l + wa*p**l + wb*b**l + wq*psums(cs + [c] + [0]*(k-l), l)[l-1]
        sl = s.solve(Ml, c)
        assert len(sl) == 1
        cs.append(s.cancel(sl[0]))
    F = numer(A0*(x-1)**(k+1) + wa*p**(k+1) + wb*b**(k+1) + wq*psums(cs, k+1)[k])
    Pv = (v - p)*(v - b)*(v**k + sum(cc*v**(k-1-i) for i, cc in enumerate(cs)))
    G = numer(s.diff(Pv, v).subs(v, x))
    return F, G

def cert(F, G, d):
    R = s.Poly(s.resultant(F.as_expr(), G.as_expr(), p), x).primitive()[1]
    if R.LC() < 0:
        R = -R
    sh = s.Poly(R.as_expr().subs(x, x + d + 2), x)
    co = sh.all_coeffs()
    nr = R.count_roots(d + 2, None) if not all(c > 0 for c in co) else 0
    ints = [r for r in s.Poly(R, x).ground_roots() if r.is_integer and r >= d + 2 and (r - d) % 2 == 0] if nr else []
    return R.degree(), len(co), min(co), all(c > 0 for c in co), 'roots>=d+2:', nr, 'admissible integer roots:', ints

CASES = {15: [('three', (1, 6, 4, 2)), ('two', (1, 4, 2, 3))],
         17: [('three', (1, 8, 4, 2)), ('three', (1, 6, 2, 4)), ('three', (3, 6, 4, 2)),
              ('two', (1, 2, 4, 3)), ('two', (3, 4, 2, 3)), ('two', (1, 4, 2, 4))],
         19: [('three', (1, 10, 4, 2)), ('three', (1, 8, 6, 2)), ('three', (1, 8, 2, 4)), ('three', (1, 4, 2, 6)),
              ('three', (3, 8, 4, 2)), ('three', (3, 6, 2, 4)), ('three', (5, 6, 4, 2)),
              ('two', (1, 6, 2, 3)), ('two', (3, 2, 4, 3)), ('two', (5, 4, 2, 3)), ('two', (3, 4, 2, 4)),
              ('two', (1, 4, 2, 5)), ('three', (1, 6, 4, 2, 4))],
         21: [('three', (1, 12, 4, 2)), ('three', (1, 10, 6, 2)), ('three', (1, 10, 2, 4)), ('three', (3, 10, 4, 2)),
              ('three', (3, 8, 6, 2)), ('three', (3, 8, 2, 4)), ('three', (3, 4, 2, 6)), ('three', (5, 8, 4, 2)),
              ('three', (5, 6, 2, 4)), ('three', (7, 6, 4, 2)),
              ('two', (3, 6, 2, 3)), ('two', (5, 2, 4, 3)), ('two', (1, 6, 2, 4)), ('two', (1, 2, 4, 4)),
              ('two', (5, 4, 2, 4)), ('two', (3, 4, 2, 5)), ('two', (1, 4, 2, 6)),
              ('three', (1, 8, 4, 2, 4)), ('three', (3, 6, 4, 2, 4))]}
import time
for d in map(int, sys.argv[1:]):
    for kind, args in CASES[d]:
        t0 = time.time()
        F, G = (three if kind == 'three' else two)(d, *args)
        print(d, kind, args, 'degF_p', F.degree(p), 'degG_p', G.degree(p), cert(F, G, d), '%.0f s' % (time.time() - t0), flush=True)
