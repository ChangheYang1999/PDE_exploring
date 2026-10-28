import json, glob, sys, os
d = sys.argv[1] if len(sys.argv) > 1 else '../numerics_data/lp1'
rows = []
for f in sorted(glob.glob(os.path.join(d, '*.json'))):
    r = json.load(open(f)); p = r['params']
    rows.append((os.path.basename(f)[:-5], r['alpha'], r['beta'], p['ntheta'], p['q'], p['rho_min'], p['rho_max'], p['ntheta_f'], p['h'], len(r['nodes']), r['V_h'], r['corr_inner'], r['hist'][-1]['t']))
print(f"{'tag':14s} {'alpha':>5} {'beta':>6} {'nth':>3} {'q':>5} {'rmin':>7} {'rmax':>7} {'nthf':>4} {'h':>5} {'N':>6} {'V_h':>9} {'corr':>8} {'t[s]':>6}")
for r in rows:
    print(f"{r[0]:14s} {r[1]:5.2f} {r[2]:6.3f} {r[3]:3d} {r[4]:5.3f} {r[5]:7.0e} {r[6]:7.0e} {r[7]:4d} {r[8]:5.3f} {r[9]:6d} {r[10]:9.5f} {r[11]:8.1e} {r[12]:6.0f}")
