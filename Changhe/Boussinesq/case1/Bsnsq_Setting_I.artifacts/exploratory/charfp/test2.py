import sys, time, math, numpy as np, torch
from charlib import *
from evalfields import fields_at
f = sys.argv[1]
P, cT, cO, NT, NO, K = load_coefs(f)
tab = VelTable(P, cO, NO, K)
rs = np.array([0.3, 0.6, 1.0, 2.0, 10.0]); ths = np.deg2rad([5.0, 20, 45, 85])
R, TH = np.meshgrid(rs, ths, indexing='ij')
X = torch.tensor(np.stack([(R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel()], 1), dtype=DT)
prof = radial_profiles(P, cT, cO, torch.tensor([1e-6], dtype=DT), NT, NO, K)
a0 = float(sum(prof['f'][n][0] * (2 * n + 1) * (-1) ** n for n in range(NT)) / 1e-6)
o = fields_at(radial_profiles(P, cT, cO, torch.tensor(rs, dtype=DT), NT, NO, K), torch.tensor(rs, dtype=DT), torch.tensor(ths, dtype=DT), P.beta, NT, NO)
res = {}
for (h, rst, jets) in [(0.02, 1e-3, True), (0.01, 1e-3, True), (0.01, 3e-4, True), (0.01, 1e-3, False)]:
    out = reconstruct(tab, X, a0, h=h, r_stop=rst, scale=-2.0 / tab.c, jets=jets)
    res[(h, rst, jets)] = out
    XY = (X[:, 0] * X[:, 1])
    print('h %.3f r_stop %.0e jets %s' % (h, rst, jets))
    print('   Om/(xy) char :', ' '.join('%+.6e' % v for v in (out['Om'] / XY).numpy()))
st = (o['Om'].reshape(-1) / (X[:, 0] * X[:, 1]))
print('   Om/(xy) stored:', ' '.join('%+.6e' % v for v in st.numpy()))
print('   NO_xy  stored:', ' '.join('%+.3e' % v for v in o['NO_xy'].reshape(-1).numpy()))
