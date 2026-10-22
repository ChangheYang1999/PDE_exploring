"""R/N of a genfn state along physical rays near the origin and through the core (diagnostic).
Usage: python3 rays.py state.npz"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from gphys import phys_fields, a0
from jets import DT
rr = np.array([1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3, 1, 3, 10, 30, 100])
phs = np.array([5, 20, 45, 70, 85, 89]) * np.pi / 180
R_, P_ = np.meshgrid(rr, phs, indexing='ij')
x = torch.tensor((R_ * np.cos(P_)).ravel(), dtype=DT); y = torch.tensor((R_ * np.sin(P_)).ravel(), dtype=DT)
F = phys_fields(x, y)
q = (F['R'].abs() / F['N']).numpy().reshape(R_.shape)
print('a0 %.4f   rows r, columns phi = %s deg' % (a0, ' '.join('%d' % round(p * 180 / np.pi) for p in phs)))
for i, r in enumerate(rr):
    print('  r %-7g ' % r + ' '.join('%.2e' % v for v in q[i]))
