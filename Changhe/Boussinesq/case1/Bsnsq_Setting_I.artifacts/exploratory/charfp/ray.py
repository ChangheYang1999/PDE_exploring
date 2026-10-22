import sys, numpy as np, torch
from charlib import *
from evalfields import fields_at
f = sys.argv[1]
P, cT, cO, NT, NO, K = load_coefs(f)
tab = VelTable(P, cO, NO, K)
prof = radial_profiles(P, cT, cO, torch.tensor([1e-6], dtype=DT), NT, NO, K)
a0 = float(sum(prof['f'][n][0] * (2 * n + 1) * (-1) ** n for n in range(NT)) / 1e-6)
A, C4, _ = local_jets(tab); sc = -2.0 / tab.c
h10 = (2 * A + 4 * C4) * sc; h01 = (2 * A - 4 * C4) * sc
beta = P.beta
print('a0 %.6f h10 %.6e h01 %.6e  jet a10 %.6e a01 %.6e g00 %.6e  (h01/h10 %.5f vs a0/70-1 %.5f)' % (a0, h10, h01, -3*a0*h10/(2*beta+4), -a0*h01/(2*beta-4), 2*(-3*a0*h10/(2*beta+4))/(2*beta+1), h01/h10, a0/((2*beta+4)*(2*beta+1))-1))
rs = np.array([3e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0]); ths = np.deg2rad([30.0, 66.8, 85.0])
R, TH = np.meshgrid(rs, ths, indexing='ij')
X = torch.tensor(np.stack([(R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel()], 1), dtype=DT)
out = reconstruct(tab, X, a0, h=0.01, r_stop=3e-4, scale=sc)
o = fields_at(radial_profiles(P, cT, cO, torch.tensor(rs, dtype=DT), NT, NO, K), torch.tensor(rs, dtype=DT), torch.tensor(ths, dtype=DT), P.beta, NT, NO)
xy = (X[:, 0] * X[:, 1]).numpy()
for k in ['Thx', 'Om']:
    st = o[k].reshape(-1).numpy(); ch = out[k].numpy()
    print(k, '/(xy): stored | char  at phi 30, 66.8, 85')
    for i in range(len(rs)):
        print('  r %.0e  ' % rs[i] + '   '.join('%+.5e | %+.5e' % (st[i*3+j]/xy[i*3+j], ch[i*3+j]/xy[i*3+j]) for j in range(3)))
