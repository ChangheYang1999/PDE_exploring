import sys, numpy as np, torch
from charlib import *
f = sys.argv[1]; pd = int(sys.argv[2]); h = float(sys.argv[3]); rst = float(sys.argv[4])
P, cT, cO, NT, NO, K = load_coefs(f)
tab = VelTable(P, cO, NO, K, per_dec=pd)
a0 = 52.82895; sc = -2.0 / tab.c
rs = np.array([3e-3, 1e-2, 3e-2, 0.1]); ths = np.deg2rad([30.0, 66.8, 85.0])
R, TH = np.meshgrid(rs, ths, indexing='ij')
X = torch.tensor(np.stack([(R * np.cos(TH)).ravel(), (R * np.sin(TH)).ravel()], 1), dtype=DT)
out = reconstruct(tab, X, a0, h=h, r_stop=rst, scale=sc)
xy = (X[:, 0] * X[:, 1]).numpy()
for k in ['Thx', 'Om']:
    ch = out[k].numpy()
    print(k, 'pd %d h %g rstop %g' % (pd, h, rst), ' | '.join('r %.0e: ' % rs[i] + ' '.join('%+.6f' % (ch[i*3+j]/xy[i*3+j]) for j in range(3)) for i in range(len(rs))))
