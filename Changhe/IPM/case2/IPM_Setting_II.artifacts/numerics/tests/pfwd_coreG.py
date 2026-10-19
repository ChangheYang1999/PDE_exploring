"""Notes of the lead analyst 09:35Z item 2(c): per state, c_core = band integral of the strain moment over lr < -6 (with the core term) and the axis values
log(G_-/G_+) at lr -11 and -8 (q_down - q_up of the axis law, local h), plus the drift convention: drift = max - min of q over lr in [-6, 9.5] (a range).
Usage: python3 tests/pfwd_coreG.py state1.npz [state2.npz ...]"""
import sys, json, math; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)
print("%-28s %-8s %-8s %-9s %-9s | %-9s %-9s %-9s" % ('state', 'p', 'm1', 'c_total', 'c_lr<-6', 'logG-/G+ -11', '-8', 'D_div(9.5)'))
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p'])
    coef = np.array(a['par']) if 'par' in a else d['x'][:-1]
    K = len(coef); Nr, Nth = g0.shape
    SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p); S = SB.S
    g = torch.tensor(g0, device='cuda'); pB = torch.tensor([p], device='cuda')
    def Afun(t):
        F = torch.zeros_like(t)
        for j in range(K):
            n = j + 1; F = F + float(coef[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
        return torch.cos(t) ** 2 * torch.exp(F)
    A = Afun(S.th[None, :]); rho = S.r[None, :, None] ** p * g[None]; Wr, Wt = SB.velocity(rho, pB)
    cm, core = SB.c_moment(rho, pB, A); m1 = 1 / p - float(cm[0])
    # band integral of c over lr < -6 (trapezoid in lr, with the core term)
    wl = torch.full((Nr,), S.d, device='cuda'); wl[0] = 0.5 * S.d; wl[-1] = 0.5 * S.d
    band = (S.lr < -6).double()
    c_band = float((rho[0] * torch.sin(3 * S.th)[None, :] * ((S.r ** (-1) * wl * band)[:, None]) * S.dth / math.pi).sum()) + float(core[0])
    ax = axis_D(S, g, Wr[0], p, m1, A=A[0], hmode='fd1')
    q_up, q_dn = ax['q_up'], ax['q_down']
    print("%-28s %-8.4f %-8.5f %-9.4f %-9.4f | %-9.4f %-9.4f %-9.4f" % (fn.split('/')[-1][:28], p, m1, float(cm[0]), c_band, q_dn['-10'] - q_up['-10'] if '-11' not in q_dn else q_dn['-11'] - q_up['-11'], q_dn['-8'] - q_up['-8'], ax['D_ax_k']))
