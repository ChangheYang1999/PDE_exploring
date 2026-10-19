# Lead: min of V_r / r over the grid (V58: does the radial velocity stay positive off the axis?).
# Usage: python3 withpf2.py vrmin.py state.npz
import sys, json, numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); g, lr, th, p = d['g'], d['lr'], d['th'], float(d['p']); l = 1 / p; r = np.exp(lr)
wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p); ar = l + wr / r[:, None]
i, j = np.unravel_index(np.argmin(ar), ar.shape)
out = dict(state=sys.argv[1].split('/')[-1], min_Vr_over_r=round(float(ar[i, j]), 4), at_lr=round(float(lr[i]), 3), at_deg=round(float(np.degrees(th[j])), 2))
for a, b in ((-12, -6), (-6, -2), (-2, 2), (2, 10)):
    w = (lr >= a) & (lr < b); k = np.argmin(ar[w].min(axis=1)); jj = np.argmin(ar[w][k])
    out['min_%g_%g' % (a, b)] = [round(float(ar[w][k, jj]), 4), round(float(lr[w][k]), 2), round(float(np.degrees(th[jj])), 1)]
print(json.dumps(out))
