# (o6): exact check that om = -w0/(u(1-u)) >= A on (0,1) for each K (so inf om = A, the limit at both ends):
# om - A = u [A - u (1+u)^2 (1+u^2) q(u^2)] / (1+u^2) ... sign decided by the bracket; Sturm counts of its roots in (0,1)
# and of the roots of q in [0,1]
import json, sympy as sp
u, t = sp.symbols('u t')
for K in range(4, 20, 2):
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    A = sp.Rational(repr(d['A']))
    q = sum(sp.Rational(c)*t**k for k, c in enumerate(d['q_monomial']))
    om = sp.cancel(((1 + u)*(A - u**2*(1 - u**4)*q.subs(t, u**2)))/(1 + u**2))
    br = sp.Poly(sp.expand(A - u*(1 + u)**2*(1 + u**2)*q.subs(t, u**2)), u)
    chk = sp.simplify(om - A - u*(1 - u)*br.as_expr()/(1 + u**2))
    nq = sp.Poly(q, t).count_roots(0, 1)
    nb = br.count_roots(0, 1)
    print('K=%2d: roots of q in [0,1]: %d, q(0) = %.6f, q(1) = %.6f; roots of the bracket in [0,1]: %d; identity residual %s; om(1/2) - A = %.6f'
          % (K, nq, float(q.subs(t, 0)), float(q.subs(t, 1)), nb, chk, float((om - A).subs(u, sp.Rational(1, 2)))), flush=True)
