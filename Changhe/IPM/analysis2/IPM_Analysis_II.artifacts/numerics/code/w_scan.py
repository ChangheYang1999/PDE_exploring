"""FLOAT scan of the verifier's reference hypotheses W1 (decay constants and the low matrix), W2 (weighted principal matrices) and W3 (derivative bounds)
of 16_weighted_fractional/REFERENCE_AUDIT.md for an n12 potential file, on a log-polar grid (nth quarter-angles, nper radii per octave on [RMIN, RMAX]).
Potential jets to order 7 (D^4 rho, D^3 u). Frobenius norms of the ordered derivative tensors (multinomial multiplicities).
  W1: M = (2c+1) I + sym DU + A >= 19/5 (A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]); sup r^0.4 (|D rho| + r |D2 rho|) <= 152; sup r^-0.6 |u| <= 18; sup r^0.4 |Du| <= 18; sup r^1.4 |D2u| <= 45.
  W2: M_k = (1 + c + V.D log omega_k) I - k (c I + sym DU) + A >= I/2, k = 1 (omega1 = <r>^-1/5), k = 2 (omega2 = (1+4r^2)^2/5); V = cX + u.
  W3: |Du| <= 14/5, |D rho| <= 16, <r>|D2u| <= 3, <r>|D3u| <= 16, |D2rho| <= 3, <r>|D2rho| <= 8, <r>^2|D3rho| <= 32, <r>^2|D4rho| <= 512.
Usage: w_scan.py file.json out.json nth RMIN RMAX nper"""
import sys, os, json, math, time
sys.set_int_max_str_digits(0)
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_norms import load_gens

def frob(parts, d):
    return np.sqrt(sum(math.comb(d, i)*p**2 for i, p in enumerate(parts)))

def main(path, out, nth, RMIN, RMAX, nper):
    t0 = time.time(); gens, coefs, cl, p = load_gens(path); c = float(cl)
    jlo, jhi = int(math.floor(math.log2(RMIN))), int(math.ceil(math.log2(RMAX)))
    s = np.linspace(jlo*math.log(2), jhi*math.log(2), (jhi-jlo)*nper + 1); th = (np.arange(nth)+0.5)/nth*math.pi/2
    S, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S).ravel(); x = (np.exp(S)*np.cos(TH)).ravel(); y = (np.exp(S)*np.sin(TH)).ravel()
    ORD = 7; cache = make_cache(x, y, ORD); J = {}
    for gen, cc in zip(gens, coefs):
        cc = float(cc)
        if cc == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORD, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + cc*v
    print('jets to order %d at %d points: %.0f s' % (ORD, len(x), time.time()-t0), flush=True)
    def rho_d(i, j): return -(J[(2+i, 1+j)] + J[(i, 3+j)])          # d_x^i d_y^j rho
    def u1_d(i, j): return -J[(1+i, 2+j)]
    def u2_d(i, j): return J[(2+i, 1+j)]
    rho = rho_d(0, 0); rho_x = rho_d(1, 0); rho_y = rho_d(0, 1); u1 = u1_d(0, 0); u2 = u2_d(0, 0)
    Drho = {d: frob([rho_d(i, d-i) for i in range(d+1)], d) for d in (1, 2, 3, 4)}
    Du = {d: np.sqrt(frob([u1_d(i, d-i) for i in range(d+1)], d)**2 + frob([u2_d(i, d-i) for i in range(d+1)], d)**2) for d in (1, 2, 3)}
    absu = np.sqrt(u1**2 + u2**2); br = np.sqrt(1 + r*r)
    DU11, DU12, DU21, DU22 = u1_d(1, 0), u1_d(0, 1), u2_d(1, 0), u2_d(0, 1); symoff = 0.5*(DU12 + DU21)
    def lam_min(a11, a12, a22): return 0.5*(a11 + a22) - np.sqrt(0.25*(a11 - a22)**2 + a12**2)
    M = lam_min((2*c+1) + DU11 + rho_y, symoff - 0.5*rho_x, (2*c+1) + DU22)
    VX = (c*x + u1)*x + (c*y + u2)*y
    res = {}
    def rec(name, vals, bound, sense='<='):
        i = int(np.argmax(vals)) if sense == '<=' else int(np.argmin(vals)); v = float(vals[i]); ok = (v <= bound) if sense == '<=' else (v >= bound)
        res[name] = {'extreme': v, 'bound': bound, 'ok': bool(ok), 'at_r': float(r[i]), 'at_theta': float(math.atan2(y[i], x[i]))}
        print('  %-34s %s %-8g : extreme %12.6g at (r, theta) = (%.4g, %.3f)  %s' % (name, sense, bound, v, r[i], math.atan2(y[i], x[i]), 'OK' if ok else 'VIOLATED'), flush=True)
    print('W1:'); rec('lambda_min(M) (S9)', M, 19/5, '>=')
    rec('r^0.4 (|D rho| + r |D2 rho|)', r**0.4*(Drho[1] + r*Drho[2]), 152); rec('r^-0.6 |u|', r**(-0.6)*absu, 18); rec('r^0.4 |Du|', r**0.4*Du[1], 18); rec('r^1.4 |D2u|', r**1.4*Du[2], 45)
    print('W2:')
    for k, dlog in ((1, -(1/5)*VX/(1 + r*r)), (2, (16/5)*VX/(1 + 4*r*r))):
        a11 = (1 + c + dlog) - k*(c + DU11) + rho_y; a22 = (1 + c + dlog) - k*(c + DU22); a12 = -k*symoff - 0.5*rho_x
        rec('lambda_min(M_%d) (omega%d)' % (k, k), lam_min(a11, a12, a22), 0.5, '>=')
    print('W3:')
    rec('|Du|', Du[1], 14/5); rec('|D rho|', Drho[1], 16); rec('<r> |D2u|', br*Du[2], 3); rec('<r> |D3u|', br*Du[3], 16)
    rec('|D2rho|', Drho[2], 3); rec('<r> |D2rho|', br*Drho[2], 8); rec('<r>^2 |D3rho|', br**2*Drho[3], 32); rec('<r>^2 |D4rho|', br**2*Drho[4], 512)
    res['_grid'] = {'nth': nth, 'RMIN': RMIN, 'RMAX': RMAX, 'per_octave': nper, 'points': int(len(x))}; res['_file'] = path
    json.dump(res, open(out, 'w'), indent=1); print('all W1-W3 grid checks OK: %s ; written %s (%.0f s)' % (all(v['ok'] for k, v in res.items() if not k.startswith('_')), out, time.time()-t0))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]))
