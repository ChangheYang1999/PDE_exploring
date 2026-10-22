"""Off-grid closure check of a Psi-only characteristic state (diagnostic).
Omega_basis (stored coefficients, normalized to c = -2) versus a0 * Omega_char (Theta, Omega reconstructed along
backward characteristics of the state's own velocity, a0 = stored a0) at points offset from the Newton grid:
log-spaced radii and angles (k + 0.3) pi / (2 M2). Reports by radial region the max of
|Omega_b - a0 Omega_char| / max_phi |Omega_b(r, .)| and, near the y-axis (phi > 80 deg), the relative defect of Omega/(xy).
Usage: python3 offgrid_eval.py state.npz [rmax] [nrad] [M2] [a0 (default: stored)]"""
import sys, numpy as np, torch
from charlib import *
from picard import omega_char_grid, omega_on_grid
torch.set_num_threads(1)

f = sys.argv[1]
rmax = float(sys.argv[2]) if len(sys.argv) > 2 else 1e6
nrad = int(sys.argv[3]) if len(sys.argv) > 3 else 64
M2 = int(sys.argv[4]) if len(sys.argv) > 4 else 40
d = np.load(f)
P, cT, cO_t, NT, NO, K = load_coefs(f)
cO = cO_t.numpy().copy()
crow = c_row(P, P.gamma_O, K).numpy()
cO *= -2.0 / float(crow @ cO[0])
a0 = float(sys.argv[5]) if len(sys.argv) > 5 else (float(d['a0']) if 'a0' in d.files else None)
rr = np.logspace(-2.0, np.log10(rmax), nrad) * 1.0137
ph = (np.arange(M2) + 0.3) * np.pi / (2 * M2)
Ob = omega_on_grid(P, cO, NO, K, rr, ph)
Om1, tab, out = omega_char_grid(P, torch.tensor(cO, dtype=DT), NO, K, rr, ph, h=0.02, r_stop=1e-3)
if a0 is None:
    raise SystemExit('no a0 stored')
D = Ob - a0 * Om1
scale = np.abs(Ob).max(1, keepdims=True) + 1e-300
rel = np.abs(D) / scale
edges = [0, 0.1, 1, 10, 1e2, 1e4, 1e6, 1e12]
print('state %s beta %.6f a0 %.4f c_tab %.8f' % (f, P.beta, a0, tab.c))
print('region            max |Ob - a0 Oc| / max_phi |Ob|')
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (rr >= lo) & (rr < hi)
    if m.any():
        print('  %8.0e-%8.0e  %.3e   (%d radii)' % (lo, hi, rel[m].max(), m.sum()))
X = rr[:, None] * np.cos(ph)[None, :]; Y = rr[:, None] * np.sin(ph)[None, :]
ya = ph > np.deg2rad(80)
q = np.abs(D[:, ya]) / (np.abs(Ob[:, ya]) + 1e-300)
for lo, hi in [(0.01, 0.1), (0.1, 1), (1, 10), (10, 1e3)]:
    m = (rr >= lo) & (rr < hi)
    if m.any():
        print('  y-axis sector phi>80deg, r in [%g,%g): max |dOmega|/|Omega_b| = %.3e' % (lo, hi, q[m].max()))
print('overall max rel (r <= 10): %.3e' % rel[rr <= 10].max())
