# Type (VI), stage 2a (lead): R_34 = Res_u1(N_3, N_4), R_35 = Res_u1(N_3, N_5) by sympy, factored; powers of the
# known nonzero factors (x, x - 21, x - a, numerators of be and om) are removed.
import sys, pickle, time, sympy as s
x, a, u1 = s.symbols('x a u1')
N = pickle.load(open('t6_21.pkl', 'rb'))['N']
known = [x, x - 21, x - a, s.expand((x - 21)*a - (x - 21 + 4)*x), s.expand((x - 21 + 2)*x - (x - 21)*a)]
t0 = time.time(); out = {}
for i, j in [(0, 1), (0, 2)]:
    r = s.resultant(N[i], N[j], u1)
    print('Res_u1(N_%d, N_%d) computed %.0f s' % (i + 3, j + 3, time.time() - t0), flush=True)
    c, fl = s.factor_list(r)
    keep = []
    for f, m in fl:
        P = s.Poly(f, a, x)
        isk = any(s.simplify(f/k).is_number for k in known)
        print('   factor deg a %d deg x %d mult %d known %s' % (P.degree(a), P.degree(x), m, isk), flush=True)
        if not isk: keep.append(f**m)
    out[(i, j)] = s.expand(s.prod(keep))
    print('   kept: deg a %d deg x %d, %.0f s' % (s.Poly(out[(i, j)], a, x).degree(a), s.Poly(out[(i, j)], a, x).degree(x), time.time() - t0), flush=True)
pickle.dump(out, open('t6b_21.pkl', 'wb'))
