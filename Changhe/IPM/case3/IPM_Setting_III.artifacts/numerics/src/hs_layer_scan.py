"""
hs_layer_scan.py -- does the centre layer of the hydrostatic trial states follow the first-node scale?  (external referee cauchy1, item 4.)  For each saved state the
pointwise logarithmic slope s(y) = (y G'(y) - G(y))/(G(y) - y) of G - y (G = g(0, .); s = 2 for a clean cubic jet) is scanned on 400 log-spaced y in [1e-4, 1];
reported: the y where |s - 2| is largest in [1e-4, 0.1], its value, and y/r_1 (r_1 = first positive Radau node radius); also the largest |s - 2| on [0.05, 0.3]
(resolved scales).  Diagnostic of trial states only.
usage: python3 src/hs_layer_scan.py state.pt ...
"""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import hs, hs_solve
torch.set_default_dtype(torch.float64)
y = np.logspace(-4, 0, 400); z = np.zeros_like(y)
print("state                        N    r_1       y* (max |s-2| in [1e-4, .1])   s(y*)    y*/r_1    second extremum y**, s(y**)   max|s-2| on [.05,.3]")
for f in sys.argv[1:]:
    st = torch.load(f, weights_only=False); N, M, c = st['N'], st['M'], st['c']; P = st.get('map_exponent_P', st.get('p')); c_map = P / (P - 1)
    hsm = hs_solve.HSModel(N, M, c_map, n_in=4, n_tail=4); m = hsm.m; u = st['u'].to(m.dev); ge = hs.GEval(m, m.beta_full(u)); r1 = float(m.rad.rR[1])
    G, _, Gy = ge(z, y); s = (y * Gy - G) / (G - y); d = np.abs(s - 2); w = y <= 0.1; i = np.argmax(np.where(w, d, -1))
    # second extremum: largest |s-2| of opposite sign to the first within [1e-4, 0.1]
    sgn = np.sign(s[i] - 2); w2 = w & (np.sign(s - 2) == -sgn); j = np.argmax(np.where(w2, d, -1)) if w2.any() else i
    w3 = (y >= 0.05) & (y <= 0.3)
    print(f"{f.split('/')[-1][:-3]:28s} {N:3d}  {r1:.2e}  {y[i]:.3e}                      {s[i]:+.3f}   {y[i]/r1:6.2f}    {y[j]:.3e}, {s[j]:+.3f}            {d[w3].max():.3f}")
