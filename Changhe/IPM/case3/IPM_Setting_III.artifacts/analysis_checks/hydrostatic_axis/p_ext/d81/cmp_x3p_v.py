# compare the type (V) core of t5b.py with the common resultant of the external answer (certificate_13) (lead)
import json, pickle, sympy as s
x = s.symbols('x')
core = s.Poly(pickle.load(open('t5b_21.pkl', 'rb'))['core'], x)
c = json.load(open('../../../referee/x3p/certificate_13.json'))['certificate']['regular']
th = [int(t) for t in c['common_positivity']['coefficients_eta_ascending']]
TH = s.Poly(sum(cc*x**i for i, cc in enumerate(th)), x)
q, r = s.div(TH, core)
print('external degree', TH.degree(), 'core degree', core.degree(), 'remainder zero', r.is_zero, 'quotient', s.factor(q.as_expr()))
for k in ('positivity', 'other_eliminant'):
    P = c[k] if k == 'positivity' else c[k]['positivity']
    E = s.Poly(sum(int(cc)*x**i for i, cc in enumerate(P['coefficients_eta_ascending'])), x)
    q2, r2 = s.div(E, core)
    print(k, 'degree', E.degree(), 'divisible by core', r2.is_zero)
