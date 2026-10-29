# Lead check of the referee's far-axis pole-sign exclusion of the lowest-defect T1 fields (t1newton):
# on the upper axis -Delta_5 phi = -8 phi_s - phi_zz at s = 0; its z^(-1-2p) coefficient must be negative for a T1 fixed point.
import json, time, sympy as sp, mpmath as mp
t0 = time.time()
s, z = sp.symbols('s z', nonnegative=True)
base = 'referee/R15/results/best/'
out = {}
for tag, ref in (('c060', 275.2122), ('c068', 28.4584), ('c074', 33.4002)):
    m = json.load(open(base + tag + '/metadata.json'))
    c = sp.nsimplify(m['c']); p = 1/(2*c)
    phi = 0
    for coef, j, k, d, a, b in m['terms']:
        n = round(d - float(p) - j - k)
        phi += sp.Float(coef, 30)*s**j*z**(2*k)/(1 + sp.Float(a, 30)*s + sp.Float(b, 30)*z**2)**(p + j + k + n)
    phi = z*phi
    lap = (-8*sp.diff(phi, s) - sp.diff(phi, z, 2)).subs(s, 0)
    f = sp.lambdify(z, lap*z**(1 + 2*p), 'mpmath')
    mp.mp.dps = 30
    v1, v2 = f(mp.mpf(10)**4), f(mp.mpf(10)**5)
    rich = v2 + (v2 - v1)/99      # O(z^-2) correction removed
    out[tag] = dict(c=float(c), T_phi=float(rich), referee=ref, rel_diff=float(abs(rich - ref)/abs(ref)),
                    positive=bool(rich > 0))
out['all_positive_and_match'] = all(out[t]['positive'] and out[t]['rel_diff'] < 1e-4 for t in ('c060', 'c068', 'c074'))
out['seconds'] = round(time.time() - t0, 1)
json.dump(out, open('checks/t1newton_tail_check_output.json', 'w'), indent=1)
print(json.dumps(out))
