"""R/N and R/N2 of a genfn state on rays close to the vertical axis (diagnostic for the y-axis band).
Usage: python3 yband.py state.npz   (gphys reads the state from argv[1])"""
import sys, numpy as np, torch
torch.set_num_threads(1)
sys.argv = [sys.argv[0], sys.argv[1], 'unused.npz']
from gphys import phys_fields, a0, mod
from jets import DT
rr = np.logspace(-1, 6, 29)
phs = np.array([70, 80, 85, 88, 89, 89.7, 89.97])
R_, P_ = np.meshgrid(rr, phs * np.pi / 180, indexing='ij')
x = torch.tensor((R_ * np.cos(P_)).ravel(), dtype=DT); y = torch.tensor((R_ * np.sin(P_)).ravel(), dtype=DT)
F = phys_fields(x, y)
b = mod.beta
N2 = (F['U1'] * F['Ox']).abs() + (F['U2'] * F['Oy']).abs() + (b * (x * F['Ox'] + y * F['Oy']) + F['Om']).abs() + F['Thx'].abs()
q = (F['R'].abs() / F['N']).numpy().reshape(R_.shape); q2 = (F['R'].abs() / N2).numpy().reshape(R_.shape)
print('a0 %.4f   R/N [R/N2]; rows r, columns phi = %s deg' % (a0, ' '.join('%g' % p for p in phs)))
for i, r in enumerate(rr):
    print('  r %-9.3g ' % r + ' '.join('%.1e[%.1e]' % (q[i, j], q2[i, j]) for j in range(len(phs))))
