"""Axisymmetric self-similar Euler operators in reduced variables (phi, q), torch float64.

Conventions (PROMPT.md sections 1, 2):
  U^r = -r d_z phi,  U^z = 2 phi + r d_r phi,  U^theta = r q,
  eta = Omega^theta / r = -Delta_5 phi,  Delta_5 = d_rr + (3/r) d_r + d_zz,
  W_m = (c_l r + U^r, c_l z + U^z),
  R_q   = q + W_m . grad q + 2 (U^r/r) q           with U^r/r = -d_z phi  (regular),
  R_eta = (1+c_l) eta + W_m . grad eta - d_z(q^2).

All fields are given through their (R, mu) partial derivatives, keyed (i, j) = d^i_R d^j_mu.
In spherical coordinates R = sqrt(r^2+z^2), mu = z/R, s = sqrt(1-mu^2) = r/R:
  f_r = s f_R - (mu s / R) f_mu,     f_z = mu f_R + (s^2 / R) f_mu,
  f_rr = s^2 f_RR - (2 mu s^2/R) f_Rmu + (mu^2 s^2/R^2) f_mumu + (mu^2/R) f_R + (mu(2-3mu^2)/R^2) f_mu,
  f_rz = mu s f_RR + (s(1-2mu^2)/R) f_Rmu - (mu s^3/R^2) f_mumu - (mu s/R) f_R + (s(3mu^2-1)/R^2) f_mu,
  f_zz = mu^2 f_RR + (2 mu s^2/R) f_Rmu + (s^4/R^2) f_mumu + (s^2/R) f_R - (3 mu s^2/R^2) f_mu.
  Delta_5 f = f_RR + (4/R) f_R + (1/R^2) [(1-mu^2) f_mumu - 4 mu f_mu].
These formulas are regular at the poles (no 1/s) and are checked against sympy in tests/test_ops.py.
"""
from __future__ import annotations

import torch

DT = torch.float64


def geom(R, mu):
    s2 = 1.0 - mu * mu
    s = torch.sqrt(torch.clamp(s2, min=0.0))
    return dict(R=R, mu=mu, s=s, s2=s2, r=R * s, z=R * mu)


def grad_rz(f, g):
    """First derivatives (f_r, f_z) from dict f with keys (1,0), (0,1)."""
    R, mu, s, s2 = g["R"], g["mu"], g["s"], g["s2"]
    fR, fm = f[(1, 0)], f[(0, 1)]
    fr = s * fR - (mu * s / R) * fm
    fz = mu * fR + (s2 / R) * fm
    return fr, fz


def hess_rz(f, g):
    """Second derivatives (f_rr, f_rz, f_zz) from dict f with keys up to order 2."""
    R, mu, s, s2 = g["R"], g["mu"], g["s"], g["s2"]
    fR, fm = f[(1, 0)], f[(0, 1)]
    fRR, fRm, fmm = f[(2, 0)], f[(1, 1)], f[(0, 2)]
    R2 = R * R
    frr = s2 * fRR - (2 * mu * s2 / R) * fRm + (mu * mu * s2 / R2) * fmm + (mu * mu / R) * fR + (mu * (2 - 3 * mu * mu) / R2) * fm
    frz = mu * s * fRR + (s * (1 - 2 * mu * mu) / R) * fRm - (mu * s * s2 / R2) * fmm - (mu * s / R) * fR + (s * (3 * mu * mu - 1) / R2) * fm
    fzz = mu * mu * fRR + (2 * mu * s2 / R) * fRm + (s2 * s2 / R2) * fmm + (s2 / R) * fR - (3 * mu * s2 / R2) * fm
    return frr, frz, fzz


def delta5(f, g):
    R, mu, s2 = g["R"], g["mu"], g["s2"]
    return f[(2, 0)] + 4 * f[(1, 0)] / R + (s2 * f[(0, 2)] - 4 * mu * f[(0, 1)]) / (R * R)


def eta_and_grad(phi, g):
    """eta = -Delta_5 phi and its (R, mu) derivatives from phi derivatives up to third order.

    eta_R  = -( phi_RRR + 4 phi_RR/R - 4 phi_R/R^2 - 2 L5(phi)/R^3 + L5(phi_R)/R^2 )
    eta_mu = -( phi_RRmu + 4 phi_Rmu/R + [ (1-mu^2) phi_mumumu - 6 mu phi_mumu - 4 phi_mu ]/R^2 )
    where L5(f) = (1-mu^2) f_mumu - 4 mu f_mu.
    Returns dict with keys (0,0), (1,0), (0,1).
    """
    R, mu, s2 = g["R"], g["mu"], g["s2"]
    R2 = R * R
    L5 = s2 * phi[(0, 2)] - 4 * mu * phi[(0, 1)]
    L5R = s2 * phi[(1, 2)] - 4 * mu * phi[(1, 1)]
    eta = -(phi[(2, 0)] + 4 * phi[(1, 0)] / R + L5 / R2)
    etaR = -(phi[(3, 0)] + 4 * phi[(2, 0)] / R - 4 * phi[(1, 0)] / R2 - 2 * L5 / (R2 * R) + L5R / R2)
    etam = -(phi[(2, 1)] + 4 * phi[(1, 1)] / R + (s2 * phi[(0, 3)] - 6 * mu * phi[(0, 2)] - 4 * phi[(0, 1)]) / R2)
    return {(0, 0): eta, (1, 0): etaR, (0, 1): etam}


def velocities(phi, g):
    """U^r, U^z, and the regular ratio U^r/r = -phi_z, from phi derivatives (order <= 1)."""
    pr, pz = grad_rz(phi, g)
    Ur = -g["r"] * pz
    Uz = 2 * phi[(0, 0)] + g["r"] * pr
    return Ur, Uz, -pz


def reduced_residuals(phi, q, g, cl):
    """R_q and R_eta at the nodes. phi: derivatives to order 3, q: to order 1."""
    Ur, Uz, Ur_over_r = velocities(phi, g)
    Wr = cl * g["r"] + Ur
    Wz = cl * g["z"] + Uz
    qr, qz = grad_rz(q, g)
    q0 = q[(0, 0)]
    Rq = q0 + Wr * qr + Wz * qz + 2 * Ur_over_r * q0
    eta = eta_and_grad(phi, g)
    er, ez = grad_rz(eta, g)
    Reta = (1 + cl) * eta[(0, 0)] + Wr * er + Wz * ez - 2 * q0 * qz
    return Rq, Reta, dict(Ur=Ur, Uz=Uz, eta=eta[(0, 0)], Wr=Wr, Wz=Wz, qr=qr, qz=qz)


def gamma_residual(phi, q, g, cl):
    """(1-2c_l) Gamma + W_m . grad Gamma with Gamma = r^2 q (used only as a cross-check)."""
    Ur, Uz, _ = velocities(phi, g)
    Wr = cl * g["r"] + Ur
    Wz = cl * g["z"] + Uz
    qr, qz = grad_rz(q, g)
    r = g["r"]
    G = r * r * q[(0, 0)]
    Gr = 2 * r * q[(0, 0)] + r * r * qr
    Gz = r * r * qz
    return (1 - 2 * cl) * G + Wr * Gr + Wz * Gz, G


def primitive_terms(phi, q, g, cl):
    """Pieces for the primitive momentum residuals without pressure (validation support).

    Returns dict with Ur, Uz, Ut (=U^theta), their r,z derivatives, the swirl terms, the divergence,
    Omega^theta, and the pressure Poisson source S = sum_ij d_i U_j d_j U_i in axisymmetric form:
      S = (Ur_r)^2 + (Uz_z)^2 + (Ur/r)^2 + 2 Ur_z Uz_r - 2 (Ut/r) Ut_r
    (checked against the Cartesian expression in tests/test_ops.py).
    """
    r = g["r"]
    pr, pz = grad_rz(phi, g)
    prr, prz, pzz = hess_rz(phi, g)
    Ur = -r * pz
    Uz = 2 * phi[(0, 0)] + r * pr
    Ur_r = -pz - r * prz
    Ur_z = -r * pzz
    Uz_r = 3 * pr + r * prr
    Uz_z = 2 * pz + r * prz
    Ur_over_r = -pz
    q0 = q[(0, 0)]
    qr, qz = grad_rz(q, g)
    Ut = r * q0
    Ut_r = q0 + r * qr
    Ut_z = r * qz
    Ut_over_r = q0
    div = Ur_r + Ur_over_r + Uz_z
    Om_theta = Ur_z - Uz_r
    S = Ur_r**2 + Uz_z**2 + Ur_over_r**2 + 2 * Ur_z * Uz_r - 2 * Ut_over_r * Ut_r
    # momentum pieces without pressure gradient
    Wr = cl * r + Ur
    Wz = cl * g["z"] + Uz
    Mr = (1 - cl) * Ur + Wr * Ur_r + Wz * Ur_z - Ut * Ut_over_r
    Mt = (1 - cl) * Ut + Wr * Ut_r + Wz * Ut_z + Ur * Ut_over_r
    Mz = (1 - cl) * Uz + Wr * Uz_r + Wz * Uz_z
    return dict(Ur=Ur, Uz=Uz, Ut=Ut, Ur_r=Ur_r, Ur_z=Ur_z, Uz_r=Uz_r, Uz_z=Uz_z, Ut_r=Ut_r, Ut_z=Ut_z,
                div=div, Om_theta=Om_theta, S=S, Mr=Mr, Mt=Mt, Mz=Mz, Ur_over_r=Ur_over_r)
