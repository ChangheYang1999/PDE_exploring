"""Residuals of the rotating self-similar profile equations (Cartesian components).

  W = (c_l I - omega J) y + U,   J y = (-y_2, y_1, 0),   J U = (-U_2, U_1, 0)
  R_u     = (1-c_l) U + (W . grad) U + omega J U + grad P          (R_u0: without grad P)
  R_Omega = Omega + (W . grad) Omega + omega J Omega - (Omega . grad) U
  R_div   = div U,   R_P = -Lap P - sum_ij d_i U_j d_j U_i
Fields come as tensors with leading component axes: U (3,...), GU (m,i,...) = d_m U_i, y (...,3)."""
from __future__ import annotations
import torch


def Jvec(V):
    return torch.stack([-V[1], V[0], torch.zeros_like(V[0])], dim=0)


def yvec(y):
    # y (..., 3) -> (3, ...)
    return y.movedim(-1, 0)


def momentum_terms(F, gradP=None):
    """Return dict of the individual terms of R_u (each (3,...)) and their sum."""
    U, GU, c_l, omega = F['U'], F['GU'], F['c_l'], F['omega']
    yv = yvec(F['y'])
    W = c_l * yv - omega * Jvec(yv) + U
    lin = (1.0 - c_l) * U
    adv = torch.einsum('m...,mi...->i...', W, GU)
    rot = omega * Jvec(U)
    terms = dict(lin=lin, adv=adv, rot=rot)
    R = lin + adv + rot
    if gradP is not None:
        terms['gradP'] = gradP
        R = R + gradP
    terms['sum'] = R
    terms['W'] = W
    return terms


def vorticity_terms(F):
    U, GU, Om, GOm, c_l, omega = F['U'], F['GU'], F['Om'], F['GOm'], F['c_l'], F['omega']
    yv = yvec(F['y'])
    W = c_l * yv - omega * Jvec(yv) + U
    lin = Om
    adv = torch.einsum('m...,mi...->i...', W, GOm)
    rot = omega * Jvec(Om)
    stretch = -torch.einsum('m...,mi...->i...', Om, GU)
    R = lin + adv + rot + stretch
    return dict(lin=lin, adv=adv, rot=rot, stretch=stretch, sum=R)


def divergence(GU):
    return GU[0, 0] + GU[1, 1] + GU[2, 2]


def pressure_source(GU):
    """sum_ij d_i U_j d_j U_i = trace(GU GU)."""
    return torch.einsum('mi...,im...->...', GU, GU)


def div_W(F):
    """div W = 3 c_l exactly for divergence-free U (test quantity)."""
    return 3.0 * F['c_l'] + divergence(F['GU'])


def rotation_content(F):
    """J U - (J y . grad) U : vanishes identically iff U is axisymmetric (as a vector field)."""
    U, GU = F['U'], F['GU']
    yv = yvec(F['y'])
    Jy = Jvec(yv)
    return Jvec(U) - torch.einsum('m...,mi...->i...', Jy, GU)
