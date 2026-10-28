"""Tabulate D_alpha vs C_alpha LP estimates (runs/lp4): D_h = LP with --ident 0.5, C_h without; both heuristic, same discretisation."""
import json, glob, os, numpy as np
rows = {}
for f in sorted(glob.glob('../numerics_data/lp4/*.json') + glob.glob('../numerics_data/lp2/*.json') + glob.glob('../numerics_data/lp1/*.json')):
    r = json.load(open(f)); p = r['params']; ident = p.get('ident', 0.0)
    key = (round(r['alpha'], 3), round(r['beta'], 3), p['ntheta'], p['rho_min'], p['rho_max'], p['ntheta_f'])
    rows.setdefault(key, {})['D' if ident else 'C'] = r['V_h'] + r['corr_inner']
print(f"{'alpha':>6} {'beta':>6} {'C_h':>9} {'D_h':>9} {'D_h-C_h':>9}  {'C_h-2/(pi a)':>12} {'D_h-2/(pi a)':>12}   (the verification work: liminf(D-C) >= 0.1735; C_0 = 0.4023)")
for key in sorted(rows):
    v = rows[key]
    if 'D' in v or 'C' in v:
        a, b = key[0], key[1]
        C = v.get('C', float('nan')); D = v.get('D', float('nan'))
        print(f"{a:6.2f} {b:6.3f} {C:9.4f} {D:9.4f} {D-C:9.4f}  {C-2/(np.pi*a):12.4f} {D-2/(np.pi*a):12.4f}")
