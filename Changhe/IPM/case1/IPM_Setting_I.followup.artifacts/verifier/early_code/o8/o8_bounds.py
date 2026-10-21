# (o8) item 4: sampled checks of the analytic reference bounds of fred22 03 section 3 (q = 0 reference,
# w0 = -A u (1 - u^2)/(1 + u^2), g0 = u^2/(1 + u^2)) against rational_bounds.json; origin majorants as absolute
# power-series sums at u = r; the C^2 failure coefficient (30) and condition (30a) at both references.
import json
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
J = json.load(open('lead/exclusion_certificates/raw_bounds/03-norm-and-radius/verification/rational_bounds.json'))
u, t = sp.symbols('u t', positive=True)
for case in ('computed_parameters_r12', 'earlier_reference_same_parameter_widths'):
    x = {k: sp.Rational(*map(int, v.split('/'))) for k, v in J[case]['exact'].items()}
    A0, e0, r = x['A0'], x['e0'], x['r']
    w0 = -A0*u*(1 - u**2)/(1 + u**2)
    g0 = sp.exp(sp.integrate(sp.cancel((sp.diff(w0, u) - A0)/w0), u))
    g0 = sp.simplify(g0/sp.limit(g0/u**2, u, 0))
    assert sp.simplify(g0 - u**2/(1 + u**2)) == 0
    a0 = sp.cancel(-w0/(1 - u)); k0 = sp.cancel((sp.diff(w0, u) - A0)/w0)
    funcs = dict(w2S=sp.diff(w0, u, 2), w2H=sp.diff(w0, u, 3), g2S=g0**-2, g2H=sp.diff(g0**-2, u), g3S=g0**-3, g3H=sp.diff(g0**-3, u),
                 H_a=sp.diff(a0, u), K0=k0, H_k=sp.diff(k0, u))
    grid = [r + (1 - r)*sp.Rational(i, 4000) for i in range(4001)]
    print(case, 'A0', A0, 'e0', e0)
    for name, f in funcs.items():
        fl = sp.lambdify(u, f, 'mpmath')
        smax = max(abs(fl(mp.mpf(g.p)/g.q)) for g in grid)
        print('  %-4s sampled sup on [r,1] %-22s bound %-22s ok %s' % (name, mp.nstr(smax, 15), sp.N(x[name], 15), smax <= x[name]))
    al = sp.lambdify(u, a0, 'mpmath')
    amin = min(al(mp.mpf(g.p)/g.q) for g in grid)
    print('  a_*  sampled min of a0 = -w0/(1-u) on [r,1] %s, json %s, equal at r: %s' % (mp.nstr(amin, 15), sp.N(x['a_star'], 15), sp.simplify(a0.subs(u, r) - x['a_star']) == 0))
    print('  gstar g0(1) = %s (json %s), w2star w0\'\'(1) = %s (json %s)' % (g0.subs(u, 1), x['gstar'], sp.simplify(sp.diff(w0, u, 2).subs(u, 1)), x['w2star']))
    # Q(1) on the reference and the json bound Qstar for the ball
    Q1 = sp.simplify(((sp.diff(g0, u) - e0*sp.diff(w0, u, 2))/(2*g0**3)).subs(u, 1))
    print('  |Q(1)| reference %s, json Qstar %s' % (sp.N(abs(Q1), 12), sp.N(x['Qstar'], 12)))
    # origin majorants: absolute power-series sums in t = u^2 at t = R = r^2
    Rr = r**2
    for name, f in dict(Z=(1 - t)/(1 + t), n=(1 + t)/(1 - t), D=-4*t/(1 + t)**2, J=-4*(3 - t)/(1 + t)**3, Eo=-sp.log(1 - t)).items():
        s = sp.series(f, t, 0, 120).removeO()
        abssum = sum(abs(c)*Rr**k for (k,), c in sp.Poly(s, t).terms())
        print('  %-3s abs series sum at R (120 terms) %-20s bound %-20s ok %s' % (name, sp.N(abssum, 12), sp.N(x[name], 12), abssum <= x[name]))
    # (30) coefficient and (30a)
    b = 2/A0; gs = sp.Rational(1, 2); gam = sp.Symbol('gamma')
    c30 = 1/(2*A0*(gam + 1)*gs**2) - e0/(2*gs**3)
    print('  (30): coefficient', sp.simplify(c30), '; zero at gamma =', sp.N(sp.solve(c30, gam)[0], 10), ', 1 - beta =', sp.N(1 - b, 10),
          '; (30a) e0 =', sp.N(e0, 8), 'vs g*/(A(2-beta)) =', sp.N(gs/(A0*(2 - b)), 8))
