# compare the type IV resultants Lambda(eta) of sp2b.py (d = 21) with the resultants of the external answer x3p, up to
# a rational factor (lead)
import json, pickle, sys, sympy as s
from fractions import Fraction
x = s.symbols('x')
for tag, idx in [('21_1_8_4_2', 5), ('21_1_4_6_2', 9), ('21_3_6_4_2', 20)]:
    L = s.Poly(pickle.load(open('research/p_ext/d81/sp2b_%s.pkl' % tag, 'rb'))['Lambda'], x)
    mine = [int(c) for c in L.all_coeffs()[::-1]]
    c = json.load(open('referee/x3p/certificate_%02d.json' % idx))['certificate']['regular']['positivity']
    th = [int(t) for t in c['coefficients_eta_ascending']]
    assert len(th) == len(mine), (len(th), len(mine))
    k = next(i for i in range(len(th)) if th[i] != 0)
    r = Fraction(mine[k], th[k])
    prop = all(Fraction(mine[i]) == r*th[i] for i in range(len(th)))
    sh = s.Poly(L.as_expr().subs(x, x + 23), x).all_coeffs()[::-1]
    print(tag, idx, 'degree', L.degree(), 'proportional', prop, 'ratio', r, 'shift coeffs one sign',
          all(q > 0 for q in sh) or all(q < 0 for q in sh), 'their all positive', c['all_strictly_positive'])
