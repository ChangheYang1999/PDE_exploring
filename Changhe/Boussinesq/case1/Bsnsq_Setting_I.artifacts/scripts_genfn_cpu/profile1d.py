"""1D cuts of a genfn state: A(x, 0) (= a0/Theta_y on the x-axis), Omega/(x y) near the x-axis, and along the y-axis
Theta(0, y)/(a0 y), Omega/(x y); radial scales of the profile (diagnostic). Usage: python3 profile1d.py state.npz"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from gphys import phys_fields, a0, mod, c
from jets import DT, monos
from model import fields
xs = np.logspace(-3, 4, 29)
# x-axis: eta -> 0 limit; use eta = 1e-7
x = torch.tensor(xs, dtype=DT); e = torch.full_like(x, 1e-7)
F = fields(mod.basis_matrix(x, e) @ c, x, e, a0, mod.beta)
print('a0 %.4f' % a0)
print('x-axis:   x        A=a0/Th_y   Om/(x eta)   U1/x      Th_x/(x eta)')
for i in range(len(xs)):
    print('  %9.3g  %10.5f  %11.4e  %9.5f  %11.4e' % (xs[i], F['A'][i], F['Om'][i] / (xs[i] * 1e-7), F['U1'][i] / xs[i], F['Thx'][i] / (xs[i] * 1e-7)))
ys = np.logspace(-3, 4, 29)
y = torch.tensor(ys, dtype=DT); xx = torch.full_like(y, 1e-7)
Fp = phys_fields(xx, y)
print('y-axis:   y        Theta/(a0 y)  Om/(x y)   U2/y')
for i in range(len(ys)):
    print('  %9.3g  %11.5e  %11.4e  %9.5f' % (ys[i], a0 * Fp['eta'][i] / (a0 * ys[i]), Fp['Om'][i] / (1e-7 * ys[i]), Fp['U2'][i] / ys[i]))
