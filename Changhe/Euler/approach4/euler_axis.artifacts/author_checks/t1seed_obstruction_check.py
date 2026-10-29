"""Lead cross-review of the verifier's finite-family obstruction for phi_a = z(1 + 3z^2)/(2(1 + a s + z^2)^(p + 1)), p = 1/(2c).
Checks: source jet p_s = -a(p + 1)/2, p_z = (2 - p)/2; -Delta_5 phi = (-8 p_s - 6 p_z) z + O(R^3); upper-axis tail of -Delta_5 phi
equals (3/2)[8a(p + 1) - (2p - 1)2p] z^(-1 - 2p); transported axis tail sign (h'/h -> -2p/z); disjointness of
a > 3(2 - p)/(4(p + 1)) and a < p(2p - 1)/(4(p + 1)) for 2/3 < p < 1.
"""
import json, time
import sympy as sp
t0 = time.time()
a, p, s, z, x, K = sp.symbols('a p s z x K', positive=True)
c = 1/(2*p); delta = 1 + c
phi = z*(1 + 3*z**2)/(2*(1 + a*s + z**2)**(p + 1))
res = {}
ps = sp.simplify(sp.diff(phi, s, 1).subs(s, 0).diff(z).subs(z, 0))
pz = sp.simplify(sp.diff(phi.subs(s, 0), z, 3).subs(z, 0)/6)
res['p_s'] = sp.simplify(ps + a*(p + 1)/2) == 0
res['p_z'] = sp.simplify(pz - (2 - p)/2) == 0
lap = 8*sp.diff(phi, s) + 4*s*sp.diff(phi, s, 2) + sp.diff(phi, z, 2)
lin = sp.simplify(sp.diff(-lap, z).subs({s: 0, z: 0}))
res['lap_jet'] = sp.simplify(lin - (-8*ps - 6*pz)) == 0
# jet relation solved for a at K^2 = k2 > 0
k2 = sp.symbols('k2', positive=True)
asol = sp.solve(sp.Eq(-a*(p + 1)/2, -sp.Rational(3, 4)*pz*(1 + k2/delta**2)), a)[0]
res['a_jet_minus_bound'] = str(sp.simplify(asol - 3*(2 - p)/(4*(p + 1))))
# axis tail: substitute z = 1/x, leading coefficient of z^(-1-2p)
lap_axis = (-lap).subs(s, 0)
tail = sp.simplify(lap_axis*z**(1 + 2*p))
lim = sp.limit(tail.subs(z, 1/x), x, 0, '+')
res['axis_tail'] = sp.simplify(lim - sp.Rational(3, 2)*(8*a*(p + 1) - (2*p - 1)*2*p)) == 0
# transported tail rate (w' - delta)/w * z -> -2p
w = c*z + 2*phi.subs(s, 0)
rate = sp.limit(((sp.diff(w, z) - delta)/w*z).subs(z, 1/x), x, 0, '+')
res['h_rate'] = sp.simplify(rate + 2*p) == 0
gap = sp.expand(3*(2 - p) - p*(2*p - 1))
res['gap'] = str(gap)
res['gap_min_on_[2/3,1]'] = float(min(gap.subs(p, sp.Rational(2, 3)), gap.subs(p, 1)))
res['seconds'] = round(time.time() - t0, 1)
print(json.dumps(res, indent=1))
json.dump(res, open('checks/t1seed_obstruction_check_output.json', 'w'), indent=1)
