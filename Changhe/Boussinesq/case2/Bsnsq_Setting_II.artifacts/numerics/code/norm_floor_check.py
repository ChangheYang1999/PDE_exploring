"""Normalization facts for the between-node grids (analysis request 11:32Z): on the fine grid of diag_state (300 log-spaced radii in [0.02, 2000]
x 4M-1 interior angles), count the points where N_Theta or N_Omega is below 1e-12 (or is exactly 0 / underflows), and print the minima.
The axes themselves are not on the grid (interior angles only); the divided residuals R_a, R_G are evaluated from the parity-factored fields."""
import sys, numpy as np, torch
sys.path.insert(0, 'code')
from lm_solve import load_state
from diag_state import eval_state
for path in sys.argv[1:]:
    d = load_state(path); M = int(d['M']); beta = float(d['beta'])
    r_mid = np.geomspace(0.02, 2000, 300); th_mid = np.linspace(0, np.pi/2, 4*M+1)[1:-1]
    m, f = eval_state(d, r_mid, th_mid)
    x = f['x']; y = f['y']; W1 = f['W1']; W2 = f['W2']; a = f['a']; G = f['G']
    Tx = x*y*(2*a + x*f['a_x']); Ty = x**2*(a + y*f['a_y']); Ox = y*(G + x*f['G_x']); Oy = x*(G + y*f['G_y']); Th = x**2*y*a; Om = x*y*G
    NO = (W1*Ox).abs() + (W2*Oy).abs() + Om.abs() + Tx.abs(); NT = (W1*Tx).abs() + (W2*Ty).abs() + abs(beta-2)*Th.abs()
    for nm, Nn in (('N_Theta', NT), ('N_Omega', NO)):
        v = Nn.reshape(-1).cpu().numpy()
        print(f"{path}: {nm}: points {v.size}, min {v.min():.3e}, count < 1e-12: {(v < 1e-12).sum()}, count == 0: {(v == 0).sum()}, count < 1e-6: {(v < 1e-6).sum()}, count < 1e-3: {(v < 1e-3).sum()}")
