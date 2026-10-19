"""Axis law on saved states with the LOCAL second-difference h (verifier V95) next to the spectral h: D_ax and drifts in the a_div and a_dir forms.
Usage: python3 tests/pfwd_axfd1.py state1.npz [state2.npz ...]   (bnewton iterate / exit-map _fp.npz / bscan single-state files)"""
import sys, json; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)
print("%-34s %-8s | %-8s %-8s %-8s %-8s | %-8s %-8s %-8s %-8s" % ('state', 'm1', 'Ddiv_sp', 'drU_sp', 'Ddiv_fd1', 'drU_fd1', 'Ddir_fd1', 'drUdir', 'drD_fd1', 'drDdir'))
for fn in sys.argv[1:]:
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']
    a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
    info = json.loads(str(d['info'])) if 'info' in d.files else None
    Nr, Nth = g0.shape
    SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p); S = SB.S
    g = torch.tensor(g0, device='cuda'); pB = torch.tensor([p], device='cuda')
    def Afun(t):
        F = torch.zeros_like(t)
        for j in range(len(coef)):
            n = j + 1; F = F + float(coef[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
        return torch.cos(t) ** 2 * torch.exp(F)
    A = Afun(S.th[None, :])
    rho = S.r[None, :, None] ** p * g[None]; Wr, Wt = SB.velocity(rho, pB); cm, core = SB.c_moment(rho, pB, A); m1 = 1 / p - float(cm[0])
    sp = axis_D(S, g, Wr[0], p, m1, A=A[0])
    f1 = axis_D(S, g, Wr[0], p, m1, A=A[0], hmode='fd1')
    f1d = axis_D(S, g, Wr[0], p, m1, A=A[0], Wt=Wt[0], hmode='fd1')
    print("%-34s %-8.5f | %-8.4f %-8.4f %-8.4f %-8.4f | %-8.4f %-8.4f %-8.4f %-8.4f" % (fn.split('/')[-1][:34], m1, sp['D_ax_k'], sp['drift_up'], f1['D_ax_k'], f1['drift_up'], f1d['D_ax_k'], f1d['drift_up'], f1['drift_down'], f1d['drift_down']))
