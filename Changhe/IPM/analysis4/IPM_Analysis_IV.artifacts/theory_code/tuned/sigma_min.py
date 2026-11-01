"""min_k |sigma_k| at the two real roots of P6 (k=2..6 exact cubics, k>=7 the generic formula), k up to 10^5."""
import json, sympy as sp, numpy as np
d = json.load(open('sigma_check.json'))
b, k = sp.symbols('b k')
gen = sp.sympify(d['generic_sigma_numerator']) / sp.sympify(d['generic_sigma_denominator'])
small = {int(kv): sp.sympify(v) for kv, v in d['sigma_small_k'].items()}
out = {}
for bv in ('0.28066166273196640400', '0.64635228988093464431'):
    f = sp.lambdify(k, gen.subs(b, sp.Float(bv, 30)), 'numpy')
    ks = np.arange(7, 100001, dtype=float)
    v = f(ks)
    allv = {kv: float(s.subs(b, sp.Float(bv, 30))) for kv, s in small.items()}
    i = int(np.argmin(np.abs(v)))
    kmin = min(allv, key=lambda kv: abs(allv[kv]))
    m = min(abs(allv[kmin]), abs(v[i]))
    arg = kmin if abs(allv[kmin]) <= abs(v[i]) else int(ks[i])
    print(bv, 'min |sigma_k| over 2..1e5 =', m, 'at k =', arg, '; sign changes for k>=7:', int(np.sum(np.diff(np.sign(v)) != 0)),
          '; sigma_7..:', v[:3], 'sigma_1e5 =', v[-1])
    out[bv] = {'min_abs_sigma': m, 'argmin_k': arg}
json.dump(out, open('sigma_min.json', 'w'), indent=1)
