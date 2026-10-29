"""First nonlinear far-field correction in the reduced variables (phi, q), slaved algebraically to the leading tail (A, B).

Expansion: phi = R^-alpha A(mu) + R^-(2 alpha + 1) A1(mu) + ...,  q = R^-(alpha + 1) B(mu) + R^-(2 alpha + 2) B1(mu) + ...,
eta = -Delta_5 phi = R^-(alpha + 2) E(mu) + R^-(2 alpha + 3) E1(mu) + ... .
With W = c y + U and 1/c = alpha + 1 the orders work out as follows (derivation in NUMERICAL_METHODS.md, checked numerically by
tests/test_farfield.py):
  q equation at order R^-(2 alpha + 2):   (1 - c(2 alpha + 2)) q1 = -(U0 . grad q0 + 2 (U0^r/r) q0)  and 1 - c(2 alpha + 2) = -1,
      so   B1 = R^(2 alpha + 2) [U0 . grad q0 + 2 (U0^r/r) q0]   (an angular function of A, A', B, B');
  eta equation at order R^-(2 alpha + 3): (1 + c - c(2 alpha + 3)) eta1 = -(U0 . grad eta0) + d_z(q0^2) and 1 + c - c(2 alpha + 3) = -1,
      so   E1 = R^(2 alpha + 3) [U0 . grad eta0 - d_z(q0^2)];
  then -Delta_5 (R^-(2 alpha + 1) A1) = R^-(2 alpha + 3) E1 gives, in Gegenbauer modes C_l^{3/2} (L5 C_l = -l(l+3) C_l),
      a1_l = e1_l / (l(l + 3) - (2 alpha + 1)(2 alpha - 2)),   no resonance for 1/2 < c_l < 3/4 (denominator > 0).
The pressure does not enter the reduced variables; it enters only the primitive momentum reconstruction.
Everything is evaluated by quadrature in mu on a Gauss grid and projected onto Legendre (B1) and Gegenbauer->Legendre (A1) coefficients
up to a chosen degree; the truncation to the representable degree is reported.
"""
from __future__ import annotations

import numpy as np
import torch

from . import basis, ops
from .pressure import gegenbauer32


def _legendre_matrix(mu, nmax):
    return basis.legendre_derivs(mu, nmax, 0)[0]          # (n_mu, nmax+1)


def first_correction(a, b, alpha, nmax_out, n_mu=None, R0=1.0):
    """a, b: Legendre coefficients of A(mu), B(mu) (length nmax_in + 1 each).  Returns (a1, b1, info): Legendre coefficients of
    A1, B1 up to degree nmax_out and the relative truncation errors of the projections.  Evaluation at R = R0 then rescaled
    (the correction is homogeneous, so any R0 works; R0 = 1 by default)."""
    a = np.asarray(a, float); b = np.asarray(b, float)
    nin = max(len(a), len(b)) - 1
    n_mu = n_mu or (2 * nin + 2 * nmax_out + 16)
    mu, w = basis.gauss_legendre(n_mu)
    R = np.full_like(mu, R0)
    # leading fields phi0, q0 and their (R, mu) derivatives to third order at R0 (torch dicts, via the exterior basis structure)
    Pm = basis.legendre_derivs(mu, nin, 3)                 # P, P', P'', P'''
    def field_derivs(coef, e):                             # f = R^-e sum_n coef_n P_n(mu): derivative dict keyed (i, j)
        pw = basis.power_derivs(R, -e)
        out = {}
        for i in range(4):
            for j in range(4 - i):
                out[(i, j)] = torch.tensor(pw[i] * (Pm[j] @ coef))
        return out
    phi0 = field_derivs(a, alpha); q0 = field_derivs(b, alpha + 1)
    g = ops.geom(torch.tensor(R), torch.tensor(mu))
    Ur, Uz, Ur_over_r = ops.velocities(phi0, g)
    qr, qz = ops.grad_rz(q0, g)
    Nq = (Ur * qr + Uz * qz + 2 * Ur_over_r * q0[(0, 0)]).numpy()                 # = -(1 - c(2a+2)) q1 -> q1 = +Nq
    eta0 = ops.eta_and_grad(phi0, g)
    er, ez = ops.grad_rz(eta0, g)
    Neta = (Ur * er + Uz * ez - 2 * q0[(0, 0)] * qz).numpy()                      # eta1 = +Neta
    B1 = Nq * R0 ** (2 * alpha + 2); E1 = Neta * R0 ** (2 * alpha + 3)
    # project B1 onto Legendre up to nmax_out
    P_out = _legendre_matrix(mu, nmax_out)
    norm = 2.0 / (2 * np.arange(nmax_out + 1) + 1)
    b1 = (P_out * w[:, None]).T @ B1 / norm
    B1_fit = P_out @ b1
    trunc_b = float(np.sqrt(np.sum(w * (B1 - B1_fit) ** 2) / max(np.sum(w * B1 ** 2), 1e-300)))
    # A1: solve L5 A1 + (2a+1)(2a-2) A1 = -E1 in Gegenbauer modes, then convert to Legendre
    C = gegenbauer32(mu, nmax_out)                                               # (L+1, n_mu)
    wz = w * (1 - mu * mu)
    h = (C * C * wz[None, :]).sum(axis=1)
    e1 = (C * wz[None, :]) @ E1 / h
    ls = np.arange(nmax_out + 1)
    denom = ls * (ls + 3) - (2 * alpha + 1) * (2 * alpha - 2)
    a1_geg = -(-e1) / denom * (-1.0)        # L5 A1 + k A1 = -E1 with L5 C_l = -l(l+3) C_l: (-l(l+3) + k) a_l = -e_l -> a_l = e_l/(l(l+3) - k)
    a1_geg = e1 / denom
    A1_vals = C.T @ a1_geg
    a1 = (P_out * w[:, None]).T @ A1_vals / norm
    A1_fit = P_out @ a1
    trunc_a = float(np.sqrt(np.sum(w * (A1_vals - A1_fit) ** 2) / max(np.sum(w * A1_vals ** 2), 1e-300)))
    E1_fit = C.T @ (e1)
    trunc_e = float(np.sqrt(np.sum(wz * (E1 - E1_fit) ** 2) / max(np.sum(wz * E1 ** 2), 1e-300)))
    return a1, b1, dict(trunc_B1=trunc_b, trunc_A1=trunc_a, trunc_E1=trunc_e, min_denominator=float(np.min(np.abs(denom))))


class SlaveMap:
    """Differentiable (torch) version of first_correction for a fixed Legendre degree set: maps the leading exterior coefficient
    vectors (a over n in n_phi, b over n in n_q, both as functions of mu with the full Legendre numbering) to the Legendre coefficients
    (a1, b1) of the first correction on the same degree sets.  Used by Problem (slave rows) and rebuilt when alpha changes."""
    def __init__(self, n_phi, n_q, nmax, alpha, device="cpu", n_mu=None):
        self.n_phi = list(n_phi); self.n_q = list(n_q); self.nmax = nmax; self.alpha = float(alpha); self.device = device
        n_mu = n_mu or (4 * nmax + 16)
        mu, w = basis.gauss_legendre(n_mu)
        Pm = basis.legendre_derivs(mu, nmax, 3)
        self.mu = torch.tensor(mu, device=device); self.w = torch.tensor(w, device=device)
        self.Pm = [torch.tensor(P, device=device) for P in Pm]                         # (n_mu, nmax+1) for j = 0..3
        self.norm = torch.tensor(2.0 / (2 * np.arange(nmax + 1) + 1), device=device)
        C = gegenbauer32(mu, nmax)
        wz = w * (1 - mu * mu)
        self.C = torch.tensor(C, device=device); self.wz = torch.tensor(wz, device=device)
        self.h = torch.tensor((C * C * wz[None, :]).sum(axis=1), device=device)
        ls = np.arange(nmax + 1)
        self.denom = torch.tensor(ls * (ls + 3) - (2 * alpha + 1) * (2 * alpha - 2), device=device)
        self.g = ops.geom(torch.ones_like(self.mu), self.mu)
        self.iphi = torch.tensor(self.n_phi, device=device); self.iq = torch.tensor(self.n_q, device=device)

    def _pw(self, e):
        # d^i/dR^i R^-e at R = 1, i = 0..3
        return [1.0, -e, e * (e + 1), -e * (e + 1) * (e + 2)]

    def __call__(self, a_sub, b_sub):
        """a_sub, b_sub: coefficients on the degree subsets n_phi, n_q (torch).  Returns (a1_sub, b1_sub) on the same subsets."""
        alpha = self.alpha
        a = torch.zeros(self.nmax + 1, dtype=a_sub.dtype, device=self.device).index_put((self.iphi,), a_sub)
        b = torch.zeros(self.nmax + 1, dtype=b_sub.dtype, device=self.device).index_put((self.iq,), b_sub)
        pwa = self._pw(alpha); pwb = self._pw(alpha + 1)
        phi0 = {(i, j): pwa[i] * (self.Pm[j] @ a) for i in range(4) for j in range(4 - i)}
        q0 = {(i, j): pwb[i] * (self.Pm[j] @ b) for i in range(4) for j in range(4 - i)}
        Ur, Uz, Uror = ops.velocities(phi0, self.g)
        qr, qz = ops.grad_rz(q0, self.g)
        B1 = Ur * qr + Uz * qz + 2 * Uror * q0[(0, 0)]
        eta0 = ops.eta_and_grad(phi0, self.g)
        er, ez = ops.grad_rz(eta0, self.g)
        E1 = Ur * er + Uz * ez - 2 * q0[(0, 0)] * qz
        b1 = (self.Pm[0] * self.w[:, None]).T @ B1 / self.norm
        e1 = (self.C * self.wz[None, :]) @ E1 / self.h
        A1 = self.C.T @ (e1 / self.denom)
        a1 = (self.Pm[0] * self.w[:, None]).T @ A1 / self.norm
        return a1[self.iphi], b1[self.iq]
