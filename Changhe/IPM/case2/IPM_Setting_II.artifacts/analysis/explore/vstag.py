# Lead: look for stagnation points of V away from 0: min of |V|/r per radial band, and V_th/r where V_r changes sign.
# Usage: python3 withpf2.py vstag.py state.npz
import sys, json, numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); g, lr, th, p = d['g'], d['lr'], d['th'], float(d['p']); l = 1 / p; r = np.exp(lr)
wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p); ar = l + wr / r[:, None]; at = wt / r[:, None]; sp = np.hypot(ar, at)
out = dict(state=sys.argv[1].split('/')[-1])
for a, b in ((-11, -6), (-6, -2), (-2, 2), (2, 9)):
    w = np.where((lr >= a) & (lr < b))[0]; s = sp[w]; i, j = np.unravel_index(np.argmin(s), s.shape)
    out['minspeed_%g_%g' % (a, b)] = [round(float(s[i, j]), 4), round(float(lr[w][i]), 2), round(float(np.degrees(th[j])), 1),
                                      round(float(ar[w][i, j]), 4), round(float(at[w][i, j]), 4)]
neg = ar < 0
if neg.any():
    out['Vr_neg_cells'] = int(neg.sum()); out['Vth_over_r_on_neg'] = [round(float(at[neg].min()), 4), round(float(at[neg].max()), 4)]
    jj = np.where(neg.any(axis=0))[0]; ii = np.where(neg.any(axis=1))[0]
    out['neg_deg_range'] = [round(float(np.degrees(th[jj].min())), 1), round(float(np.degrees(th[jj].max())), 1)]
    out['neg_lr_range'] = [round(float(lr[ii].min()), 2), round(float(lr[ii].max()), 2)]
print(json.dumps(out))
