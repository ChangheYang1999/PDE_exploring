"""Radial basis for the scalar potentials, single global map.

  rho = r^2,  u = rho + R0^2,  s = sqrt(u),  x = (s - R0)/(s + R0) in [0, 1).
  Mode (l, m, t) radial function of potential T:   T_q(r) = r^l g_q(rho),
      g_q(rho) = (s/R0)^(-(alpha + l)) * sum_k a_kq Phi_k(x),      Phi_k(x) = T_k(2x - 1).
  Potential S uses the envelope (s/R0)^(-(alpha + l - 1)).
  Twist (applied to cos/sin pairs of the same (l, m)): angle beta(rho) = omega/(2 c_l) log(1 + rho/R0^2).
Regular at the origin (every factor is smooth in rho; x ~ rho/(4 R0^2)); at infinity T ~ r^-alpha (1 + series in 1/r),
S ~ r^(1-alpha) (...), and beta = (omega/c_l) log r - (omega/c_l) log R0 + O(1/r^2).
Jets give the rho-derivatives up to order K exactly."""
from __future__ import annotations
import math
import numpy as np
import torch
from . import jets

DT = torch.float64


def cheb_gauss_nodes_x(N):
    """Chebyshev-Gauss nodes on (0,1), ascending (no endpoints)."""
    j = np.arange(N)
    x = 0.5 * (1 - np.cos(np.pi * (j + 0.5) / N))
    return x


def r_from_x(x, R0):
    s = R0 * (1 + x) / (1 - x)
    return np.sqrt(np.maximum(s * s - R0 * R0, 0.0))


def x_from_r(r, R0):
    s = np.sqrt(r * r + R0 * R0)
    return (s - R0) / (s + R0)


class RadialBasis:
    """Precomputes nothing parameter-dependent; call `matrices(rho, alpha, R0, Lmax, K, shift)`."""

    def __init__(self, Nk):
        self.Nk = Nk

    def matrices(self, rho, alpha, R0, Lmax, K, shift=0.0, power=None, core_damp=0, R1=None, Nk=None, lmask=None):
        """Return B of shape (Lmax+1, K+1, Nr, Nk): B[l, n, j, k] = d^n/drho^n [ (s/R0)^-(p_l) damp(rho) Phi_k(x) ] at rho_j,
        p_l = alpha + l - shift by default, or power(l) (callable returning a tensor) when given;
        damp = (rho/(rho + R1^2))^core_damp (1 if core_damp = 0); lmask: list of l for which the channel is zero.
        alpha, R0 may be 0-dim tensors (differentiable)."""
        rho = torch.as_tensor(rho, dtype=DT)
        R0 = torch.as_tensor(R0, dtype=DT)
        alpha = torch.as_tensor(alpha, dtype=DT)
        Nk = Nk or self.Nk
        u = rho + R0 * R0
        s = jets.affine_pow(u, 0.5, K)                      # jet of s
        sp = s + jets.const(R0, s)                          # s + R0
        x = jets.const(1.0, s) - 2 * R0 * jets.recip(sp)    # x = 1 - 2 R0/(s+R0)
        Phi = jets.chebyshev_shifted(x, Nk)                 # list of jets
        Phi = torch.stack(Phi, dim=-1)                      # (K+1, Nr, Nk)
        damp = None
        if core_damp and core_damp > 0:
            R1 = R0 if R1 is None else torch.as_tensor(R1, dtype=DT)
            u1 = rho + R1 * R1
            frac = jets.const(1.0, s) - (R1 * R1) * jets.affine_pow(u1, -1.0, K)     # rho/(rho+R1^2)
            damp = frac
            for _ in range(int(core_damp) - 1):
                damp = jets.mul(damp, frac)
        out = []
        for l in range(Lmax + 1):
            p = -(alpha + l - shift) / 2.0 if power is None else -power(l) / 2.0
            env = jets.affine_pow(u, p, K) * (R0 ** (-(2 * p)))   # (s/R0)^(2p) = u^p R0^(-2p)
            if damp is not None:
                env = jets.mul(env, damp)
            if lmask is not None and l in lmask:
                env = env * 0.0
            prod = []
            for n in range(K + 1):
                acc = 0
                for k in range(n + 1):
                    acc = acc + env[k][..., None] * Phi[n - k]
                prod.append(acc)
            out.append(jets.to_derivs(torch.stack(prod, 0)))
        return torch.stack(out, dim=0)

    @staticmethod
    def twist_tables(rho, omega, c_l, R0, Mmax, K):
        """C[m, n, j] = d^n/drho^n cos(m beta(rho_j)), S likewise, beta = omega/(2 c_l) log(1 + rho/R0^2)."""
        rho = torch.as_tensor(rho, dtype=DT)
        R0 = torch.as_tensor(R0, dtype=DT)
        u = rho + R0 * R0
        lg = jets.affine_log(u, K)
        # D6FP 2026-10-28 (verifier V004/V005): the value log(1 + rho/R0^2) by log1p (no cancellation for rho << R0^2); the
        # rho-derivatives (jet coefficients n >= 1 of log u) are unchanged. Same function, roundoff-level change at the core.
        lg = torch.cat([torch.log1p(rho / (R0 * R0))[None], lg[1:]], 0)
        beta = (omega / (2.0 * c_l)) * lg
        Cs, Ss = [], []
        for m in range(Mmax + 1):
            c, s_ = jets.cos_sin(m * beta)
            Cs.append(jets.to_derivs(c)); Ss.append(jets.to_derivs(s_))
        return torch.stack(Cs, 0), torch.stack(Ss, 0)
