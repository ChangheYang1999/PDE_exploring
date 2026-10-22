import sys, numpy as np, torch
from charlib import *
torch.set_num_threads(1)
f = sys.argv[1]
P, cT, cO, NT, NO, K = load_coefs(f)
crow = c_row(P, P.gamma_O, K)
cO = cO * (-2.0 / float(crow @ cO[0]))
tab = VelTable(P, cO, NO, K, rmin=1e-4, rmax=1e12, per_dec=400)
print('beta', P.beta, 'c', tab.c)
for r in [1e-3,1e-2,0.03,0.1,0.2,0.3,0.5,0.7,1,1.3,1.7,2,3,5,10,30,100,1e3,1e4,1e5,1e6,1e8]:
    Yy = torch.tensor([[1e-12, r]], dtype=DT); Yx = torch.tensor([[r, 1e-12]], dtype=DT)
    Wy, DWy = tab.W_DW(Yy); Wx, DWx = tab.W_DW(Yx)
    print('%9.3g  W2(0,y)/y %9.5f  W1(x,0)/x %9.5f   dxW1(0,y) %9.5f dyW2(x,0) %9.5f' % (r, float(Wy[0,1])/r, float(Wx[0,0])/r, float(DWy[0,0,0]), float(DWx[0,1,1])))
