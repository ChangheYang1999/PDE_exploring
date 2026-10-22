"""Print the x half-width x* of Theta_y(x, 0) (where Theta_y(x,0) = a0/2) for an Omega-basis state (solve_gn npz)."""
import sys, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs, radial_profiles
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); device = dev()
r = torch.logspace(-2, 4, 6001, dtype=DT, device=device) * P.L; prof = radial_profiles(P, cT, cO, r, NT, NO, K)
m = torch.tensor([2 * n + 1 for n in range(NT)], dtype=DT, device=device); tau = (m[:, None] * prof['f']).sum(0) / r
a0 = float(tau[0]); idx = torch.nonzero(tau < a0 / 2)
print('%.6f' % (float(r[int(idx[0])]) / P.L) if idx.numel() else 'nan')
