"""Manufactured check: Omega from the mixed jets vs physical -Lap Psi by root inversion and finite differences;
U vs (-Psi_y, Psi_x); W.grad Theta - b Theta = 0 physically."""
import torch, numpy as np, math
from jets import *
from model import *
torch.manual_seed(1)
mod = Model(4, 3)
c = torch.randn(mod.nb, dtype=DT) * 0.003
K1 = mod.Kw + 1
c[0] += 0.775; c[K1] += 0.2; c[2 * K1] += 0.025
c0 = torch.tensor(mod.h00_row()); c = c + (1 - float(c0 @ c)) * c0 / float(c0 @ c0)
a0 = 7.0
def Gval(x, e):   # G only (order 0 jets)
    Bm = mod.basis_matrix(x, e, p=1)
    return (Bm @ c)
pts_x = torch.tensor([0.3, 0.8, 1.7], dtype=DT); pts_e = torch.tensor([0.4, 0.9, 0.5], dtype=DT)
Bm = mod.basis_matrix(pts_x, pts_e)
Gc = Bm @ c
F = fields(Gc, pts_x, pts_e, a0, mod.beta)
print('A', F['A'])
# physical: for given (x, y) find eta with G_x(x, eta) = y by Newton
def eta_of(x, y, e_guess):
    e = e_guess.clone()
    for _ in range(60):
        B1 = mod.basis_matrix(x, e, p=2) @ c
        L, ix = monos(2)
        Gx = B1[ix[(1, 0)]]; Gxe = B1[ix[(1, 1)]]
        e = e - (Gx - y) / Gxe
    return e
def Psi_phys(x, y, eg):
    e = eta_of(x, y, eg)
    B1 = mod.basis_matrix(x, e, p=1) @ c
    L, ix = monos(1)
    G = B1[0]; Gx = B1[ix[(1, 0)]]; Ge = B1[ix[(0, 1)]]
    return mod.beta * x * Gx + mod.b * e * Ge - 2 * mod.beta * G, e
for h in [1e-2, 5e-3, 2.5e-3]:
    y0 = F['y']
    P0, e0 = Psi_phys(pts_x, y0, pts_e)
    Pxp, _ = Psi_phys(pts_x + h, y0, pts_e); Pxm, _ = Psi_phys(pts_x - h, y0, pts_e)
    Pyp, _ = Psi_phys(pts_x, y0 + h, pts_e); Pym, _ = Psi_phys(pts_x, y0 - h, pts_e)
    lap = (Pxp + Pxm + Pyp + Pym - 4 * P0) / h**2
    U1 = -(Pyp - Pym) / (2 * h); U2 = (Pxp - Pxm) / (2 * h)
    # Theta transport: Theta = a0 eta(x,y)
    _, exp_ = Psi_phys(pts_x + h, y0, pts_e); _, exm = Psi_phys(pts_x - h, y0, pts_e)
    _, eyp = Psi_phys(pts_x, y0 + h, pts_e); _, eym = Psi_phys(pts_x, y0 - h, pts_e)
    Thx = a0 * (exp_ - exm) / (2 * h); Thy = a0 * (eyp - eym) / (2 * h)
    W1 = mod.beta * pts_x + U1; W2 = mod.beta * y0 + U2
    RT = W1 * Thx + W2 * Thy - mod.b * a0 * e0
    print('h %.4f  |Om_jet + lap| %.2e  |U1| %.2e |U2| %.2e  |Thx| %.2e  RT %.2e' % (h, float((F['Om'] + lap).abs().max()),
          float((F['U1'] - U1).abs().max()), float((F['U2'] - U2).abs().max()), float((F['Thx'] - Thx).abs().max()), float(RT.abs().max())))
