import sys, time, math, numpy as np, torch
from charlib import *
from evalfields import fields_at
f = sys.argv[1]; h = float(sys.argv[2]) if len(sys.argv) > 2 else 0.02
P, cT, cO, NT, NO, K = load_coefs(f)
t0 = time.time(); tab = VelTable(P, cO, NO, K); print('table %.1fs c=%.10f' % (time.time() - t0, tab.c))
A, C4, A2 = local_jets(tab); print('jets A %.6e (check %.6e) C4 %.6e' % (A, A2, C4))
rs = np.array([0.1, 0.3, 0.6, 1.0, 2.0, 10.0, 100.0]); ths = np.deg2rad([5.0, 10, 20, 45, 70, 85])
R, TH = np.meshgrid(rs, ths, indexing='ij')
X = torch.tensor(np.stack([(R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel()], 1), dtype=DT)
# a0 of the stored state: Theta_y(0)
from polarlib import Params
prof = radial_profiles(P, cT, cO, torch.tensor([1e-6], dtype=DT), NT, NO, K)
a0 = float(sum(prof['f'][n][0] * (2 * n + 1) * (-1) ** n for n in range(NT)) / 1e-6)
print('a0 %.6f' % a0)
t0 = time.time(); out = reconstruct(tab, X, a0, h=h, scale=-2.0 / tab.c); print('reconstruct %d pts %.1fs, S range %.2f-%.2f, all done %s' % (X.shape[0], time.time() - t0, out['S'].min(), out['S'].max(), bool(out['done'].all())))
o = fields_at(radial_profiles(P, cT, cO, torch.tensor(rs, dtype=DT), NT, NO, K), torch.tensor(rs, dtype=DT), torch.tensor(ths, dtype=DT), P.beta, NT, NO)
for k in ['Th', 'Thx', 'Om']:
    st = o[k].reshape(-1); ch = out[k]
    print(k)
    for i in range(len(rs)):
        row = ' '.join('%+.2e' % float((ch[i * len(ths) + j] - st[i * len(ths) + j]) / (abs(st[i * len(ths) + j]) + 1e-30)) for j in range(len(ths)))
        print('  r %7.2f rel diff (phi 5,10,20,45,70,85): %s   stored %+.4e' % (rs[i], row, float(st[i * len(ths) + 2])))
np.savez('test1_out_h%g.npz' % h, **{k: v.numpy() for k, v in out.items() if torch.is_tensor(v)})
