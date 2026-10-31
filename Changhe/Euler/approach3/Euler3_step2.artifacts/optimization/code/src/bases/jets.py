"""Truncated Taylor jets in one variable (rho = r^2), order K, stored as tensors J[n] = f^{(n)}(rho)/n!.
All operations are exact to the truncation order and differentiable by torch autograd in every parameter."""
from __future__ import annotations
import math
import torch


def const(c, like):
    K = like.shape[0] - 1
    parts = [torch.zeros_like(like[0]) + c] + [torch.zeros_like(like[0]) for _ in range(K)]
    return torch.stack(parts, 0)


def variable(rho, K):
    parts = [rho] + [torch.ones_like(rho) if n == 1 else torch.zeros_like(rho) for n in range(1, K + 1)]
    return torch.stack(parts, 0)


def mul(a, b):
    K = a.shape[0] - 1
    out = []
    for n in range(K + 1):
        acc = 0
        for k in range(n + 1):
            acc = acc + a[k] * b[n - k]
        out.append(acc)
    return torch.stack(out, 0)


def recip(a):
    K = a.shape[0] - 1
    inv0 = 1.0 / a[0]
    out = [inv0]
    for n in range(1, K + 1):
        acc = 0
        for k in range(1, n + 1):
            acc = acc + a[k] * out[n - k]
        out.append(-inv0 * acc)
    return torch.stack(out, 0)


def affine_pow(u, p, K):
    """Jet of (u)^p where u is an affine function of rho with du/drho = 1 (u = rho + R0^2); p may be a tensor."""
    out = []
    c = 1.0
    for n in range(K + 1):
        if n > 0:
            c = c * (p - (n - 1)) / n      # C(p, n) = p (p-1) ... (p-n+1) / n!
        out.append(c * u ** (p - n))
    return torch.stack(out, 0)


def affine_log(u, K):
    """Jet of log(u), u affine in rho with slope 1."""
    out = [torch.log(u)]
    for n in range(1, K + 1):
        out.append(((-1) ** (n - 1)) / n * u ** (-n))
    return torch.stack(out, 0)


def cos_sin(u):
    """Jets of cos(u) and sin(u) for a jet u."""
    K = u.shape[0] - 1
    c = [torch.cos(u[0])]; s = [torch.sin(u[0])]
    for n in range(1, K + 1):
        accc = 0; accs = 0
        for k in range(1, n + 1):
            accc = accc + k * u[k] * s[n - k]
            accs = accs + k * u[k] * c[n - k]
        c.append(-accc / n)
        s.append(accs / n)
    return torch.stack(c, 0), torch.stack(s, 0)


def chebyshev_shifted(x, Nk):
    """List of jets Phi_k(x) = T_k(2x-1), k = 0..Nk-1, for a jet x (shifted Chebyshev on [0,1])."""
    two_x_m1 = 2 * x - const(1.0, x)
    T = [const(1.0, x), two_x_m1]
    for k in range(2, Nk):
        T.append(2 * mul(two_x_m1, T[-1]) - T[-2])
    return T[:Nk]


def to_derivs(J):
    """Convert Taylor coefficients to derivatives f^{(n)} = n! J[n]."""
    return torch.stack([math.factorial(n) * J[n] for n in range(J.shape[0])], 0)
