"""FLOAT octave profiles for an n12 potential file (exact 'generators' JSON or float 'gens/coefs' JSON): on a log-polar grid (nth quarter-angles,
radii from RMIN to RMAX), the smallest eigenvalue of the energy matrix M = (2c_l+1) I + sym(DU) + [[rho_y, -rho_x/2], [-rho_x/2, 0]] (SPEC S9),
min over each octave r in [2^j, 2^(j+1)), with the location of the global minimum; sup |F| per octave; sup |F| r^-p2 for the far field.
Potential jets to order 4 (DU and grad rho). Usage: n12_Mscan.py file.json out.json nth RMIN RMAX nper_octave"""
import sys, os, json, math
sys.set_int_max_str_digits(0)
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n12_eval import make_cache, generator_jet
from n12_norms import load_gens

def main(path, out, nth, RMIN, RMAX, nper):
    gens, coefs, cl, p = load_gens(path); clf = float(cl)
    jlo, jhi = int(math.floor(math.log2(RMIN))), int(math.ceil(math.log2(RMAX)))
    s = np.linspace(jlo*math.log(2), jhi*math.log(2), (jhi-jlo)*nper + 1)
    th = (np.arange(nth)+0.5)/nth*math.pi/2
    S, TH = np.meshgrid(s, th, indexing='ij'); r = np.exp(S).ravel(); x = (np.exp(S)*np.cos(TH)).ravel(); y = (np.exp(S)*np.sin(TH)).ravel()
    ORD = 4; cache = make_cache(x, y, ORD); J = {}
    for gen, c in zip(gens, coefs):
        c = float(c)
        if c == 0: continue
        gj = generator_jet(x, y, gen['m'], gen['beta'], gen['spec'], ORD, cache)
        for k, v in gj.items(): J[k] = J.get(k, 0) + c*v
    rho = -(J[(2, 1)] + J[(0, 3)]); rho_x = -(J[(3, 1)] + J[(1, 3)]); rho_y = -(J[(2, 2)] + J[(0, 4)])
    U1 = -J[(1, 2)]; U2 = J[(2, 1)]
    DU11 = -J[(2, 2)]; DU12 = -J[(1, 3)]; DU21 = J[(3, 1)]; DU22 = J[(2, 2)]
    F = (clf*x + U1)*rho_x + (clf*y + U2)*rho_y - rho
    M11 = (2*clf+1) + DU11 + rho_y; M22 = (2*clf+1) + DU22; M12 = 0.5*(DU12 + DU21) - 0.5*rho_x
    lam_min = 0.5*(M11 + M22) - np.sqrt(0.25*(M11 - M22)**2 + M12**2)
    g = 1/clf; p2 = 2*g - 1
    prof = {}
    for j in range(jlo, jhi):
        sel = (r >= 2.0**j) & (r < 2.0**(j+1))
        if not sel.any(): continue
        i = np.argmin(np.where(sel, lam_min, np.inf)); k = np.argmax(np.where(sel, np.abs(F), -np.inf))
        prof[j] = {'min_eig_M': float(lam_min[i]), 'at': [float(r[i]), float(math.atan2(y[i], x[i]))], 'sup_F': float(abs(F[k])), 'sup_F_at': [float(r[k]), float(math.atan2(y[k], x[k]))],
                   'sup_F_rp2': float(np.max(np.abs(F[sel])*r[sel]**(-p2)))}
    i = int(np.argmin(lam_min))
    res = {'file': path, 'grid': {'nth': nth, 'RMIN': RMIN, 'RMAX': RMAX, 'per_octave': nper}, 'global_min_eig_M': float(lam_min[i]), 'at': [float(r[i]), float(math.atan2(y[i], x[i]))],
           'sup_F': float(np.abs(F).max()), 'octaves': {str(j): v for j, v in prof.items()}}
    json.dump(res, open(out, 'w'), indent=1)
    print('%s: grid %d angles x %d radii on [%g, %g]; global min eig M = %.4f at r = %.4g theta = %.3f; sup|F| = %.4g' % (os.path.basename(path), nth, len(s), RMIN, RMAX, res['global_min_eig_M'], res['at'][0], res['at'][1], res['sup_F']))
    print('  j   min eig M     at r      sup|F|      at r    sup|F| r^-p2')
    for j, v in prof.items(): print(' %3d  %9.4f  %9.3g  %10.3e  %8.3g  %10.3e' % (j, v['min_eig_M'], v['at'][0], v['sup_F'], v['sup_F_at'][0], v['sup_F_rp2']))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]))
