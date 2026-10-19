# Lead: compare the numerics' velocity (their PFwdB kernels, run on CPU, read-only import) with the lead velocity
# (pforward.velocity_p; run through withpf2.py for the corrected weights) on the same state, band by band in lr; then one
# transport step of each scheme on that state (dg/ds), to separate a velocity difference from a transport/interpolation one.
# Usage: python3 withpf2.py velcmp.py state.npz
import sys, numpy as np, torch
sys.path.insert(0, '../numerics/code')
sys.path.insert(0, 'explore')
torch.set_default_dtype(torch.float64)
from pfwd_batch import PFwdB
import pforward as PF, p0_forward2 as P2
d = np.load(sys.argv[1]); g, lr, th, p = d['g'], d['lr'], d['th'], float(d['p']); Nr, Nth = g.shape; r = np.exp(lr); l = 1 / p
S = PFwdB(Nr, Nth, lr[0], lr[-1], p, dev='cpu')
rho = (r ** p)[:, None] * g
Wr_n, Wt_n = S.velocity(torch.tensor(rho)[None], torch.tensor([p]))
Wr_n, Wt_n = Wr_n[0].numpy(), Wt_n[0].numpy()
Wr_l, Wt_l = PF.velocity_p(rho, lr, th, p)
print('state', sys.argv[1], 'Nth', Nth, 'p %.5f' % p)
print('band            max|d ar|   max|d at|   (ar = l + Wr/r, at = Wt/r; numerics - lead)   at angle of max d at (deg)')
for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2), (2, 10)]:
    i = (lr >= a) & (lr <= b)
    dar = (Wr_n - Wr_l)[i] / r[i, None]; dat = (Wt_n - Wt_l)[i] / r[i, None]
    k = np.unravel_index(np.argmax(np.abs(dat)), dat.shape)
    print('[%5.1f,%5.1f]   %.2e    %.2e    %s' % (a, b, np.abs(dar).max(), np.abs(dat).max(), '%.1f' % np.degrees(th[k[1]])))
print('ar, at at lr ~ -11 (numerics / lead) at selected angles:')
i = np.argmin(np.abs(lr + 11))
for deg in [0, 30, 60, 80, 86, 90, 94, 100, 150, 180, 270]:
    j = np.argmin(np.abs(np.degrees(th) - deg))
    print('  th %5.1f  ar %.5f / %.5f   at %.5f / %.5f' % (np.degrees(th[j]), l + Wr_n[i, j] / r[i], l + Wr_l[i, j] / r[i], Wt_n[i, j] / r[i], Wt_l[i, j] / r[i]))
