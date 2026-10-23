import sys, numpy as np, torch
sys.path.insert(0, 'src'); import hs_layer, hs_cauchy
torch.set_default_dtype(torch.float64)
S96 = hs_cauchy.load('runs/hsG_c2.0_N96_log.pt'); S128 = hs_cauchy.load('runs/hsG_c2.0_N128_log_cont.pt')
r = np.logspace(-2, 4, 25); th = np.linspace(0, np.pi / 2, 9); R, T = np.meshgrid(r, th, indexing='ij'); X = (R * np.cos(T)).reshape(-1); Y = (R * np.sin(T)).reshape(-1); R = R.reshape(-1)
m = (R >= 0.01) & (R < 0.1)
for nt in (400, 800, 1600, 3200):
    for q in (3, 2):
        a1, a2 = hs_layer.hydro_V_log(S96['ge'], X[m], Y[m], n0=32, per_decade=10, ngl=16, n_tail=nt, q=q); b1, b2 = hs_layer.hydro_V_log(S128['ge'], X[m], Y[m], n0=32, per_decade=10, ngl=16, n_tail=nt, q=q)
        a1, a2, b1, b2 = map(np.asarray, (a1, a2, b1, b2)); d1 = np.abs(a1 - b1) / (1 + R[m]) ** 0.5; i = np.argmax(d1)
        print(f"n_tail {nt:5d} q {q}: inner max|dV1|/(1+r)^p = {d1.max():.6e} at (x,y)=({X[m][i]:.4f},{Y[m][i]:.4f});  V1_96 there = {a1[i]:+.9f}, V1_128 = {b1[i]:+.9f};  max|dV2| = {(np.abs(a2-b2)/(1+R[m])**0.5).max():.6e}")
