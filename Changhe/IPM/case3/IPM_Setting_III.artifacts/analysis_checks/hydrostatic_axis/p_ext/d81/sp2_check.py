# Numerical consistency check of sp2.py/sp2b.py (lead): at roots eta0 of each factor of Lambda, find a common root a of
# F1, F2 and u1 from r1 u1 + r0 = 0, rebuild all nodes and evaluate M_1..M_4, pi'(eta0) and (A8) directly.
import pickle, sympy as s, mpmath as mp
mp.mp.dps = 60
x, a, u1 = s.symbols('x a u1')
D = pickle.load(open('sp2_19_1_6_4_2.pkl', 'rb')); L = pickle.load(open('sp2b_19_1_6_4_2.pkl', 'rb'))['Lambda']
def core(E): return [f for f, k in s.factor_list(E)[1] if s.Poly(f, a, x).degree(a) > 1][0]
F1, F2 = core(D['H1']), core(D['R3'])
d, A0, wa, wu, wv = 19, 1, 6, 4, 2
for f, k in s.factor_list(L)[1]:
    f = s.Poly(f, x)
    if f.degree() < 2: continue
    rts = f.nroots(n=50, maxsteps=500)
    best = None
    for r0 in rts[:6]:
        p1 = s.Poly(F1.subs(x, r0), a); p2 = s.Poly(F2.subs(x, r0), a)
        ra = p1.nroots(n=50, maxsteps=500)
        vals = sorted(((abs(complex(p2.eval(q)))/max(1, abs(complex(q)))**12, q) for q in ra), key=lambda t: t[0])
        q = vals[0][1]
        rr1 = complex(D['r1'].subs({x: r0, a: q})); rr0 = complex(D['r0'].subs({x: r0, a: q}))
        U1 = -rr0/rr1 if abs(rr1) > 1e-30 else None
        if U1 is None: continue
        X = complex(r0); A = complex(q); T = A0*X - d
        al = 1/(X - A); be = (-T/X - (wa - wv)*al)/(wu - wv); om = -al - be
        U2 = (2*X + U1)/be - X**2 - U1*X
        W1 = (A0*(X - 1) + wa*A - wu*(-U1))/wv * 1  # M1 = A0 (X-1) + wa A + wu(-U1) + wv(-W1) = 0
        W1 = (A0*(X - 1) + wa*A - wu*U1)/wv
        W2 = (2*X + W1)/om - X**2 - W1*X
        import numpy as np
        nodes = [A] + list(np.roots([1, U1, U2])) + list(np.roots([1, W1, W2])); vals_ = [wa, wu, wu, wv, wv]
        M = [abs(A0*(X - 1)**l + sum(w*y**l for w, y in zip(vals_, nodes))) / abs(X)**l for l in (1, 2, 3, 4)]
        pip = sum(1/(X - y) for y in nodes); A8 = sum(w/(X - y) for w, y in zip(vals_, nodes)) + T/X
        mind = min(abs(y1 - y2) for i, y1 in enumerate(nodes) for y2 in nodes[i+1:])
        res = max(M + [abs(pip)*abs(X), abs(A8)*abs(X)])
        if best is None or res < best[0]: best = (res, X, mind, min(abs(X - y) for y in nodes), min(abs(X - 1 - y) for y in nodes))
    print('factor degree', f.degree(), 'mult', k, '| best residual %.2e at eta0 = %s, min node gap %.2e, min |eta0 - node| %.2e, min |eta0-1-node| %.2e' % best, flush=True)
