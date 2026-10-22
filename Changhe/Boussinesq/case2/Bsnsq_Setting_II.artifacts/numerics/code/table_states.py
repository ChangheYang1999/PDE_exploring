import sys, json, numpy as np
from glob import glob
print(f"{'state':34s} {'map':3s} {'N':>3s} {'M':>3s} {'L':>5s} {'beta':>7s} {'its':>4s} {'RMS':>9s} {'Fmax':>8s} {'Ra_max':>8s} {'RG_max':>8s} {'a_rt':>7s} {'a_at':>7s} {'G_rt':>7s} {'G_at':>7s} {'nunk':>5s}")
for p in sorted(sys.argv[1:]):
    d = np.load(p, allow_pickle=True); h = json.loads(str(d['hist']))
    if not h: continue
    e = h[-1]; mp = str(d['mapname']) if 'mapname' in d else 'xi'
    print(f"{p.split('/')[-1][:-4]:34s} {mp:3s} {int(d['N']):3d} {int(d['M']):3d} {float(d['L']):5.1f} {float(d['beta']):7.4f} {len(h):4d} {e['Fnorm']:9.3e} {e['Fmax']:8.2e} {e['Ra_max']:8.2e} {e['RG_max']:8.2e} {e['a_rtail']:7.1e} {e['a_atail']:7.1e} {e['G_rtail']:7.1e} {e['G_atail']:7.1e} {e['n_unknown']:5d}")
