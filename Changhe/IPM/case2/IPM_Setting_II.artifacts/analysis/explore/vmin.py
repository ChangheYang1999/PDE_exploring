# Lead: min |V|/r and min V_r/r of a lead-format state by sector and lr band (lead velocity, pforward2 via withpf2).
# Usage: python3 withpf2.py vmin.py state.npz
import sys, json, numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); g, lr, th = d['g'], d['lr'], d['th']; p = float(d['p']); l = 1 / p; r = np.exp(lr)
wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]; sp = np.hypot(ar, at)
deg = np.degrees(th); out = dict(state=sys.argv[1].split('/')[-1], p=p)
for name, lo, hi in (('up', 80, 100), ('low', 260, 280), ('all', -1, 361)):
    m = (deg >= lo) & (deg <= hi)
    for blo, bhi in ((-14, -8), (-8, -2), (-2, 4), (-14, 10)):
        b = (lr >= blo) & (lr <= bhi); S = sp[np.ix_(b, m)]; k = np.unravel_index(np.argmin(S), S.shape)
        out['%s_%g..%g' % (name, blo, bhi)] = dict(minV=round(float(S.min()), 4), at=[round(float(lr[b][k[0]]), 2), round(float(deg[m][k[1]]), 1)],
                                                  minVr=round(float(ar[np.ix_(b, m)].min()), 4))
print(json.dumps(out))
