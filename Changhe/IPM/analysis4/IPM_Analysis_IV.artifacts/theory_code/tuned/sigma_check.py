"""Exact checks for the tuned series at delta=2/3, f_1 = sin + b sin3: sigma_k nonvanishing for all k >= 2."""
import json, sympy as sp
import sigma_sym as ss
b, k = ss.b, ss.kk
F, G = ss.low_orders(3)
gen, _ = ss.sigma(k, F, G)
num, den = sp.fraction(sp.factor(gen))
O6 = sp.Poly(176703765525000*b**6-222533688701250*b**5+96180432855375*b**4-20675598499400*b**3+2783057141280*b**2-243275209320*b+10532171936, b)
out = {'generic_sigma_numerator': str(sp.factor(num)), 'generic_sigma_denominator': str(sp.factor(den))}
# the b-cubic part N(k,b) of the numerator
fl = sp.factor_list(num)
print(fl)
Nkb = [f for f, e in fl[1] if sp.Poly(f, b).degree() == 3][0]
cf = sp.Poly(Nkb, b).all_coeffs()
g = cf[0]
for c_ in cf[1:]:
    g = sp.gcd(g, c_)
print('gcd of the b-coefficients (polynomials in k):', g)
out['gcd_b_coeffs'] = str(g)
lead = sp.Poly(Nkb, k).LC()
print('leading k^8 coefficient N_8(b) =', lead)
out['N8'] = str(lead)
lim = sp.limit(gen, k, sp.oo)
print('sigma_infinity =', sp.factor(lim))
out['sigma_inf'] = str(sp.factor(lim))
# small k exact
small = {}
for kv in range(2, 7):
    s, _ = ss.sigma(kv, F, G)
    small[kv] = str(s)
    print(kv, s, ' generic:', sp.factor(gen.subs(k, kv)))
out['sigma_small_k'] = small
# numeric values at both real roots
roots = [r for r in O6.real_roots()]
vals = {}
for r in roots:
    rv = sp.N(r, 40)
    row = {kv: float(sp.N(sp.sympify(small[kv]).subs(b, rv), 20)) for kv in range(2, 7)}
    for kv in (7, 8, 10, 20, 50, 100, 1000, 10**6):
        row[kv] = float(sp.N(gen.subs({k: kv, b: rv}), 20))
    row['inf'] = float(sp.N(lim.subs(b, rv), 20))
    vals[str(sp.N(r, 20))] = row
    print(sp.N(r, 20), row)
out['values'] = vals
print('O6 irreducible:', O6.is_irreducible)
json.dump(out, open('sigma_check.json', 'w'), indent=1)
