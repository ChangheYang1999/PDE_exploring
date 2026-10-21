"""Truncated Taylor-series ("jet") arithmetic, verifier verifier code (written for this run).

A jet of order K is a tensor J with leading dimension K+1, J[j] = f^(j)(x0)/j! (Taylor coefficients in the local
variable around each sample point x0; the remaining dimensions index the sample points).  All operations act
elementwise on the trailing dimensions.  Works with torch tensors.
"""
import math
import torch


def const(v, K):
    """Jet of a constant (or of a value with zero derivatives)."""
    v = torch.as_tensor(v)
    J = torch.zeros((K + 1,) + tuple(v.shape), dtype=v.dtype, device=v.device)
    J[0] = v
    return J


def var(x, K):
    """Jet of the independent variable at the points x."""
    J = const(x, K)
    if K >= 1:
        J[1] = 1.0
    return J


def mul(A, B):
    K = A.shape[0] - 1
    C = torch.zeros(torch.broadcast_shapes(A.shape, B.shape), dtype=A.dtype, device=A.device)
    for n in range(K + 1):
        acc = A[0] * B[n]
        for i in range(1, n + 1):
            acc = acc + A[i] * B[n - i]
        C[n] = acc
    return C


def exp(A):
    K = A.shape[0] - 1
    E = torch.zeros_like(A)
    E[0] = torch.exp(A[0])
    for n in range(1, K + 1):
        acc = A[1] * E[n - 1]
        for i in range(2, n + 1):
            acc = acc + i * A[i] * E[n - i]
        E[n] = acc / n
    return E


def log(A):
    K = A.shape[0] - 1
    Lg = torch.zeros_like(A)
    Lg[0] = torch.log(A[0])
    for n in range(1, K + 1):
        acc = A[n].clone()
        for i in range(1, n):
            acc = acc - (i / n) * Lg[i] * A[n - i]
        Lg[n] = acc / A[0]
    return Lg


def pw(A, a):
    """A^a for A[0] > 0."""
    K = A.shape[0] - 1
    P = torch.zeros_like(A)
    P[0] = A[0] ** a
    for n in range(1, K + 1):
        acc = torch.zeros_like(A[0])
        for i in range(1, n + 1):
            acc = acc + ((a + 1) * i - n) * A[i] * P[n - i]
        P[n] = acc / (n * A[0])
    return P


def recip(A):
    K = A.shape[0] - 1
    Rr = torch.zeros_like(A)
    Rr[0] = 1.0 / A[0]
    for n in range(1, K + 1):
        acc = torch.zeros_like(A[0])
        for i in range(1, n + 1):
            acc = acc + A[i] * Rr[n - i]
        Rr[n] = -acc / A[0]
    return Rr


def compose(fders, A):
    """f(A) given fders[j] = f^(j)(A[0]) (j = 0..K), each broadcastable against A[0]."""
    K = A.shape[0] - 1
    d = A.clone()
    d[0] = 0.0
    shape = tuple(torch.broadcast_shapes(A.shape[1:], fders[0].shape))
    out = torch.zeros((K + 1,) + shape, dtype=A.dtype, device=A.device)
    out[0] = fders[0]
    powj = None
    for j in range(1, K + 1):
        powj = d if j == 1 else mul(powj, d)
        out = out + (fders[j] / math.factorial(j)) * powj
    return out


def deriv(A):
    """Jet of the derivative (order K-1)."""
    K = A.shape[0] - 1
    n = torch.arange(1, K + 1, dtype=A.dtype, device=A.device).view((K,) + (1,) * (A.dim() - 1))
    return A[1:] * n


def ders(A):
    """Plain derivatives f^(j)(x0) = j! J[j]."""
    K = A.shape[0] - 1
    f = torch.tensor([math.factorial(j) for j in range(K + 1)], dtype=A.dtype, device=A.device)
    return A * f.view((K + 1,) + (1,) * (A.dim() - 1))


def r_to_t(A, r):
    """Given an r-jet A (coefficients in powers of dr) at points r, return the jet in t = log r (powers of dt):
    r e^{dt} - r = r (dt + dt^2/2 + ...)."""
    K = A.shape[0] - 1
    e = torch.zeros((K + 1,) + tuple(r.shape), dtype=A.dtype, device=A.device)
    for j in range(1, K + 1):
        e[j] = r / math.factorial(j)
    # f(r + e(dt)) = sum_j A[j] e^j
    while e.dim() < A.dim():
        e = e.unsqueeze(-1)
    out = torch.zeros_like(A)
    out[0] = A[0]
    powj = None
    for j in range(1, K + 1):
        powj = e if j == 1 else mul(powj, e)
        out = out + A[j].unsqueeze(0) * powj
    return out


def t_to_r(A, r):
    """Inverse of r_to_t: given a t-jet A (powers of dt, t = log r) at points r, return the r-jet (powers of dr):
    t(r + dr) - t = log(1 + dr/r) = sum_j (-1)^(j+1) (dr/r)^j / j."""
    K = A.shape[0] - 1
    e = torch.zeros((K + 1,) + tuple(r.shape), dtype=A.dtype, device=A.device)
    for j in range(1, K + 1):
        e[j] = (-1.0) ** (j + 1) / (j * r ** j)
    while e.dim() < A.dim():
        e = e.unsqueeze(-1)
    out = torch.zeros_like(A)
    out[0] = A[0]
    powj = None
    for j in range(1, K + 1):
        powj = e if j == 1 else mul(powj, e)
        out = out + A[j].unsqueeze(0) * powj
    return out
