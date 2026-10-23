# hand-check of the external answer x3o (lead): full coefficient lists of all 15 main Lambda and the extra type (III)
# polynomial compared with the answer's audit_certificates.json (ascending coefficients, primitive, positive leading).
import sys, json, pickle, time, sympy as s
J = json.load(open('../../../referee/x3o/audit_certificates.json'))
main = J['main']
def asc(R, var):
    R = s.Poly(R, var).primitive()[1]
    if R.LC() < 0: R = -R
    return [int(c) for c in reversed(R.all_coeffs())]
def match(co, tag):
    hits = [r['name'] for r in main if [int(c) for c in r['coefficients']] == co]
    print(tag, 'degree', len(co) - 1, 'identical to', hits, flush=True)
    return hits
sys.argv = ['gen19.py']
import gen19
found = []
for kind, args in gen19.CASES[19]:
    t0 = time.time()
    F, G = (gen19.three if kind == 'three' else gen19.two)(19, *args)
    R = s.resultant(F.as_expr(), G.as_expr(), gen19.p)
    found += match(asc(R, gen19.x), '%s %s (%.0f s)' % (kind, args, time.time() - t0))
# type (III): run tt.py in a namespace and take R and R0
ns = {}; sys.argv = ['tt.py', '19', '1', '4', '2']
exec(open('tt.py').read(), ns)
found += match(asc(ns['R'].as_expr(), ns['x']), 'III Res(M4, M5)')
R0 = asc(ns['R0'].as_expr(), ns['x'])
ex = J['extra_type_III']
print('III Res(C1, C0) keys', list(ex) if isinstance(ex, dict) else type(ex), flush=True)
cand = [ex] if isinstance(ex, dict) else ex
for c in cand:
    for k, vv in c.items():
        if isinstance(vv, list) and vv and all(isinstance(q, (int, str)) for q in vv):
            L = [int(q) for q in vv]
            print('  extra', k, 'equal' if L == R0 else ('equal up to sign' if L == [-q for q in R0] else 'different'), flush=True)
# type (IV)
L = pickle.load(open('sp2b_19_1_6_4_2.pkl', 'rb'))['Lambda']
found += match(asc(L, s.Symbol('x')), 'IV Lambda')
print('all 15 matched once:', sorted(found) == sorted(r['name'] for r in main), flush=True)
