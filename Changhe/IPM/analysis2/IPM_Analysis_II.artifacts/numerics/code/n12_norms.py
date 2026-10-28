"""S14 residual norms (FLOAT) of a potential given by a generator list with coefficients (exact JSON from n12_exact.py or float result JSON),
on a fine log-polar grid r in [r_min, R], plus the exact far-field contribution beyond R from the residual sectors (q <= Q) for the
weighted L2 norms: for F ~ sum_sectors r^alpha E(theta): int_R^inf |omega F|^2 dX with omega = <r>^e ~ r^e: sum over sector pairs with
cross terms... we use the exact angular L2 inner products: int_R^inf r^(2e) [sum_s r^alpha_s E_s]^2 r dr dtheta = sum_{s,s'} <E_s,E_s'> R^(2e+alpha_s+alpha_s'+2)/(-(2e+alpha_s+alpha_s'+2))
(valid when all 2e + alpha_s + alpha_s' + 2 < 0, i.e. the norm converges). Derivative norms beyond R are bounded crudely by |D^k F| <= (|alpha|+n+...)/r^k ...:
for the far part of the derivative norms we use the exact sectors' derivatives via the polar rules (farfield_bounds.dx, dy) on the sine series.
Also prints the dyadic profile (contribution of r in [2^j, 2^(j+1)) to each squared norm) over the grid.
"""
import sys, os, json, math
sys.set_int_max_str_digits(0)
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_fit import F_jets, ORDER
from n12_exact import sectors_general, T_coeffs
import farfield_bounds as FB

def load_gens(path):
    d = json.load(open(path))
    if 'generators' in d:
        gens = [{'m': g['m'], 'j': g['j'], 'spec': tuple(g['spec'])} for g in d['generators']]; coefs = [Fr(g['coef']) for g in d['generators']]; cl = Fr(d['cl'])
    else:
        gens = [{'m': g['m'], 'j': g['j'], 'spec': tuple(g['spec'])} for g in d['gens']]; coefs = [Fr(c) for c in d['coefs']]; cl = Fr(d['cl'])
    g = Fr(1)/cl; lam = 1-g; p = [(3+g-j*lam)/2 for j in range(8)]
    for gen in gens: gen['beta'] = float(p[gen['j']] - gen['m'])
    return gens, coefs, cl, p

def main(path, smin, smax, ns, nth, sigmas, Q=4):
    gens, coefs, cl, p = load_gens(path); clf = float(cl)
    s = np.linspace(smin, smax, ns); ds = s[1]-s[0]; th = (np.arange(nth)+0.5)/nth*math.pi/2; dth = math.pi/2/nth
    S, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S).ravel(); x = (np.exp(S)*np.cos(TH)).ravel(); y = (np.exp(S)*np.sin(TH)).ravel()
    wq = r*r*ds*dth*4; wq[:nth] *= 0.5; wq[-nth:] *= 0.5
    cache = make_cache(x, y, ORDER)
    J = {}
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORDER, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    FJ = F_jets(J, None, clf, x, y, K=2)
    br = np.sqrt(1 + r*r); D1 = FJ[(1, 0)]**2 + FJ[(0, 1)]**2; D2 = FJ[(2, 0)]**2 + 2*FJ[(1, 1)]**2 + FJ[(0, 2)]**2
    R = math.exp(smax)
    X = sectors_general(gens, coefs, cl, qmax=Q, hmax=8, jmax=7)
    secs = [((h, q), float(X['alpha'](h, q)), {int(k): float(v) for k, v in Sd.items()}) for (h, q), Sd in X['E'].items() if Sd]
    def inner(S1, S2):   # <sum a_k sin k, sum b_k sin k>_{L2(0,2pi)} = pi sum a_k b_k
        return math.pi*sum(S1.get(k, 0)*S2.get(k, 0) for k in set(S1) | set(S2))
    def far_norm2(e, deriv=0):
        # derivative sectors via polar rules: D^k of r^alpha E(theta) -> list of (exponent, trig dict); use farfield_bounds dx/dy on sine dicts
        comps = []  # list of lists of (alpha, dict) for each derivative component
        for (hq, al, Sd) in secs:
            T = {('s', k): v for k, v in Sd.items()}
            if deriv == 0: comps.append([(al, T)])
            elif deriv == 1: comps.append([(al-1, FB.dx(T, al)), (al-1, FB.dy(T, al))])
            else:
                Tx = FB.dx(T, al); Ty = FB.dy(T, al)
                comps.append([(al-2, FB.dx(Tx, al-1)), (al-2, FB.dx(Ty, al-1)), (al-2, FB.dy(Tx, al-1)), (al-2, FB.dy(Ty, al-1))])   # xx, yx, xy, yy (Frobenius)
        ncomp = 1 if deriv == 0 else (2 if deriv == 1 else 4)
        total = 0.0
        for ci in range(ncomp):
            terms = [c[ci] for c in comps]
            for (a1, T1) in terms:
                for (a2, T2) in terms:
                    ex = 2*e + a1 + a2 + 2
                    if ex >= 0: return float('inf')
                    ip = math.pi*sum(v*T2.get(k, 0) for k, v in T1.items())    # both sine or both cosine dicts share keys (kind,k)
                    total += ip*R**ex/(-ex)
        return total
    out = {}
    for sg in sigmas:
        if sg == 'L':
            wL = (1 + 4*r*r)**0.4
            w = {'rF': r*r*FJ[(0, 0)]**2, 'F': FJ[(0, 0)]**2, 'gradF': D1, 'wLD2F': wL*wL*D2}
            efar = {'rF': 1.0, 'F': 0.0, 'gradF': 0.0, 'wLD2F': 0.8}; dfar = {'rF': 0, 'F': 0, 'gradF': 1, 'wLD2F': 2}
            # far part of the lead weight: (1+4r^2)^0.4 <= (4r^2)^0.4 (1 + 1/(4R^2))^0.4 for r >= R: bound by 2^0.8 (1+1/(4R^2))^0.4 r^0.8
            cL = (2**0.8*(1 + 1/(4*R*R))**0.4)**2
        else:
            w = {'rwF': (r*br**(-(2+sg)))**2*FJ[(0, 0)]**2, 'w0F': br**(-2-2*sg)*FJ[(0, 0)]**2, 'w1DF': br**(-2*sg)*D1, 'w2D2F': br**(2-2*sg)*D2}
            efar = {'rwF': -(1+sg), 'w0F': -1-sg, 'w1DF': -sg, 'w2D2F': 1-sg}; dfar = {'rwF': 0, 'w0F': 0, 'w1DF': 1, 'w2D2F': 2}; cL = None
        row = {}
        for name, integrand in w.items():
            inner_part = float(np.sum(wq*integrand))
            e = efar[name]; deriv = dfar[name]
            far = far_norm2(e, deriv)
            if cL is not None and name == 'wLD2F' and far < float('inf'): far = far*cL
            row[name] = {'inner_sq': inner_part, 'far_sq': far, 'norm': math.sqrt(inner_part + far) if far < float('inf') else float('inf')}
            # dyadic profile
            jbins = np.floor(np.log2(r)).astype(int); prof = {}
            for jb in np.unique(jbins): prof[int(jb)] = float(np.sum((wq*integrand)[jbins == jb]))
            row[name]['dyadic_sq'] = prof
        out[str(sg)] = row
        if sg == 'L':
            print('LEAD weights: ||r F||_2 = %.4g (far %s) | ||F||_2 = %.4g (far %s) | ||grad F||_2 = %.4g (far %s) | ||(1+4r^2)^0.4 D^2 F||_2 = %.4g (far %s)' % tuple(sum([[row[k]['norm'], ('%.2e' % math.sqrt(row[k]['far_sq'])) if row[k]['far_sq'] < 1e300 else 'inf'] for k in ('rF', 'F', 'gradF', 'wLD2F')], [])))
        else:
            print('sigma=%.2f: ||r w F|| = %.4g (far %.2e) | ||omega_0 F|| = %.4g (far %.2e) | ||omega_1 DF|| = %.4g (far %.2e) | ||omega_2 D^2F|| = %.4g (far %.2e)' % (sg, row['rwF']['norm'], math.sqrt(row['rwF']['far_sq']), row['w0F']['norm'], math.sqrt(row['w0F']['far_sq']), row['w1DF']['norm'], math.sqrt(row['w1DF']['far_sq']) if row['w1DF']['far_sq'] < 1e300 else float('inf'), row['w2D2F']['norm'], math.sqrt(row['w2D2F']['far_sq']) if row['w2D2F']['far_sq'] < 1e300 else float('inf')))
    sup = float(np.abs(FJ[(0, 0)]).max()); i = int(np.argmax(np.abs(FJ[(0, 0)])))
    print('sup over grid |F| = %.4g at r = %.4g; |F| at r~1: %.3e; near-origin: max |F|/r^3 for r<0.1: %.3e' % (sup, r[i], np.abs(FJ[(0, 0)][np.argmin(abs(r-1))]), (np.abs(FJ[(0, 0)])/r**3)[r < 0.1].max()))
    out['sup_F'] = sup; out['sup_F_r'] = float(r[i]); out['grid'] = [smin, smax, ns, nth]
    out['F_at_r1'] = float(np.abs(FJ[(0, 0)][np.argmin(abs(r-1))])); out['maxF_over_r3_r_lt_0.1'] = float((np.abs(FJ[(0, 0)])/r**3)[r < 0.1].max())
    i1 = np.argmin(abs(r-1)); out['D2F_at_r1'] = float(np.sqrt(D2[i1])); out['max_D2F_near_r1'] = float(np.sqrt(D2[(r > 0.9) & (r < 1.1)]).max())
    out['sectors'] = {'%d,%d' % hq: {'alpha': al, 'norm_L2_quarter': math.sqrt(math.pi*sum(v*v for v in Sd.values())/4)} for (hq, al, Sd) in secs if al > -3}
    print('residual sector norms (exponent > -3):', {k: (round(v['alpha'], 3), '%.4g' % v['norm_L2_quarter']) for k, v in out['sectors'].items()})
    return out

if __name__ == '__main__':
    path = sys.argv[1]; smin, smax, ns, nth = float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    sigmas = [v if v == 'L' else float(v) for v in sys.argv[6].split(',')]
    out = main(path, smin, smax, ns, nth, sigmas)
    json.dump(out, open(sys.argv[7], 'w'), indent=1)
