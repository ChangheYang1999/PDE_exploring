"""Lead request (notes 06:08Z item 4): min V_r/r and min |V|/r over the grid for saved batched states (bscan *_states.npz or bn iterate npz).
Also recomputes D_ax with a_dir (lead 05:21Z) next to a_div.  Usage: python3 tests/pfwd_vrmin.py file.npz [p=..] [Nth from file]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]; d = np.load(fn, allow_pickle=True)
g = d['g']; lr = d['lr']; th = d['th']
if g.ndim == 2: g = g[None]
B, Nr, Nth = g.shape
if 'X' in d.files:
    X = d['X']; ps = X[:, -1]; labels = json.loads(str(d['labels'])) if 'labels' in d.files else [None] * B
elif 'par' in d.files:
    X = None; ps = np.full(B, float(d['p'])); labels = [tuple(np.round(r, 3)) for r in d['par']]
else:
    a = json.loads(str(d['args'])); ps = np.array([a['p']]); labels = [a.get('par')]; X = None
pk = float(np.median(ps))
SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), pk); S = SB.S
gt = torch.tensor(g, device='cuda'); pt = torch.tensor(ps, device='cuda')
rho = S.r[None, :, None] ** pt[:, None, None] * gt
Wr, Wt = SB.velocity(rho, pt)
cm, core = SB.c_moment(rho, pt, gt[:, -1, :]); m1 = (1 / pt - cm).cpu().numpy()
Vr_r = (1 / pt)[:, None, None] + Wr / S.r[None, :, None]; Vt_r = Wt / S.r[None, :, None]
Vabs_r = torch.sqrt(Vr_r ** 2 + Vt_r ** 2)
lrn = lr; thd = np.degrees(th)
print("%-28s %-8s | %-9s %-7s %-7s | %-9s %-7s %-7s | %-7s %-7s %-7s %-7s %-7s" % ('label', 'm1', 'minVr/r', 'at lr', 'at th', 'min|V|/r', 'at lr', 'at th', 'Dax_div', 'Dax_dir', 'agap_up', 'agap_dn', 'drU_dir'))
for b in range(B):
    v = Vr_r[b].cpu().numpy(); w = Vabs_r[b].cpu().numpy()
    i, j = np.unravel_index(np.argmin(v), v.shape); i2, j2 = np.unravel_index(np.argmin(w), w.shape)
    A = gt[b, -1, :]
    ax0 = axis_D(S, gt[b], Wr[b], float(ps[b]), float(m1[b]), A=A)
    ax1 = axis_D(S, gt[b], Wr[b], float(ps[b]), float(m1[b]), A=A, Wt=Wt[b])
    neg = float((v < 0).mean())
    print("%-28s %-8.5f | %-9.4f %-7.2f %-7.1f | %-9.4f %-7.2f %-7.1f | %-7.3f %-7.3f %-7.3f %-7.3f %-7.3f   negfrac %.4f" % (str(labels[b])[:28], m1[b], v[i, j], lrn[i], thd[j], w[i2, j2], lrn[i2], thd[j2], ax0['D_ax_k'], ax1['D_ax_k'], ax1.get('a_gap_up', float('nan')), ax1.get('a_gap_down', float('nan')), ax1['drift_up'], neg))
