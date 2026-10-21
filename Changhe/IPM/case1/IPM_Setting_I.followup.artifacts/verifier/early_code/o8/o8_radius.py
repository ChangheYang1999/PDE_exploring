# (o8) item 1: the final inequality (32) of fred22 03 PROOF, recomputed with sympy rationals from the exact constants of
# rational_bounds.json (the lead-lane copy), assembled here independently of the referee's script; also (33), the
# rational lower bound b0 from its formula, and checks that b0 < B0 and the strict budget at the claimed radii.
import json
import sympy as sp
import mpmath as mp
mp.mp.dps = 40
J = json.load(open('lead/exclusion_certificates/raw_bounds/03-norm-and-radius/verification/rational_bounds.json'))
R = sp.Rational
claimed = {'computed_parameters_r12': R(1, 10**6), 'earlier_reference_same_parameter_widths': R(1, 10**8),
           'earlier_reference_fixed_parameters': R(1, 10**7)}
for case, val in J.items():
    x = {k: R(*map(int, v.split('/'))) for k, v in val['exact'].items()}
    h, hp = R(val['inputs']['h']), R(val['inputs']['hp'])
    A0, e0 = R(val['inputs']['A0']), R(val['inputs']['e0'])
    assert x['A0'] == A0 and x['e0'] == e0 and x['h'] == h and x['hp'] == hp
    P = x['DA']*h + x['De']*hp + x['KAA']*h**2/2 + x['KAe']*h*hp
    m = x['B_lower']/2 - P
    D = x['DN'] + x['KAv']*h + x['Kev']*hp
    eps32 = min(x['delta0'], m/(2*(D + x['Rvv']*x['delta0'])))
    eps33 = min(x['delta0'], 2*m/(D + sp.sqrt(D**2 + 4*x['Rvv']*m)))
    # b0 from its formula: (16 - beta)/(3 A (4 + beta)) * 1/(beta (1 + beta)) * (1 - S_A e)
    b = 2/A0; SA = 6*A0*(4*A0 - 3)/(8*A0 - 1)
    b0 = (16 - b)/(3*A0*(4 + b))/(b*(1 + b))*(1 - SA*e0)
    bm, Am = mp.mpf(2)/mp.mpf(A0.p)*mp.mpf(A0.q), None
    B0 = (16 - mp.mpf(b.p)/b.q)/(3*mp.mpf(A0.p)/A0.q*(4 + mp.mpf(b.p)/b.q))*mp.beta(2 - mp.mpf(b.p)/b.q/2, mp.mpf(b.p)/b.q)*(1 - mp.mpf(SA.p)/SA.q*mp.mpf(e0.p)/e0.q)
    c = claimed[case]
    budget = P + D*c + x['Rvv']*c**2
    print(case)
    print('  P %s (json %s) m %s (json %s) D %s (json linear %s)' % (sp.N(P, 12), sp.N(x['parameter_budget'], 12), sp.N(m, 12),
          sp.N(x['margin'], 12), sp.N(D, 12), sp.N(x['linear'], 12)))
    print('  eps (32) = %s (json %s, equal: %s); eps (33) = %s' % (sp.N(eps32, 12), sp.N(x['epsilon_formula'], 12), eps32 == x['epsilon_formula'], sp.N(eps33, 12)))
    print('  b0 formula %s, equal to json B_lower: %s; B0 (Beta function, mpmath) %s; b0 < B0: %s' % (sp.N(b0, 15), b0 == x['B_lower'], mp.nstr(B0, 15), mp.mpf(b0.p)/b0.q < B0))
    print('  claimed radius %s: eps32 >= claimed %s; strict budget P + D c + Rvv c^2 = %s < b0/2 = %s: %s; c <= delta0: %s'
          % (c, eps32 >= c, sp.N(budget, 12), sp.N(x['B_lower']/2, 12), budget < x['B_lower']/2, c <= x['delta0']))
