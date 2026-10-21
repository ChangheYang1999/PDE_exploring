# Taylor coefficients of order 1, 3, 5, 7, 9 at u = 0 of w0 = -A u (1-u^2)/(1+u^2) + u^3 (1-u^2)^2 q(u^2), exact
# rationals from the JSON decimal strings, for the lead's K = 4..18 references and the fred22 fitted reference.
import json
from fractions import Fraction as Fr
L = 'lead'
refs = {}
for K in range(4, 20, 2):
    d = json.load(open(L + '/b3_functional/xref/ref_c6g_K%d.json' % K))
    refs['K%d' % K] = (Fr(repr(d['A'])), [Fr(s) for s in d['q_monomial']])
d = json.load(open(L + '/exclusion_certificates/reference_fit/data/fitted_reference.json'))
refs['fit'] = (Fr(d['A0_exact']), [Fr(s) for s in d['q_power_coefficients_exact_decimal']])
for name, (A, q) in refs.items():
    c = {}
    for n in (1, 3, 5, 7, 9):
        k = (n - 1) // 2          # -A u (1-u^2)/(1+u^2) = -A u (1 + 2 sum_{k>=1} (-1)^k u^(2k))
        a = -A if k == 0 else -A * 2 * (-1) ** k
        # u^3 (1 - 2t + t^2) q(t), t = u^2: coefficient of u^n is that of t^((n-3)/2)
        if n >= 3:
            m = (n - 3) // 2
            qq = lambda i: q[i] if 0 <= i < len(q) else Fr(0)
            a += qq(m) - 2 * qq(m - 1) + qq(m - 2)
        c[n] = a
    print('%-4s' % name, '  '.join('c%d %.6f' % (n, float(v)) for n, v in c.items()))
