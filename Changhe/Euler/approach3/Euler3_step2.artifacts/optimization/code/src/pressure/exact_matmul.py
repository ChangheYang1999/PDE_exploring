"""D6FP (lead 23:08Z D1 variant v1): error-free matrix products in float64 on the GPU by the Ozaki splitting scheme, returning a double-double
(hi, lo) result. A (m x k) and B (k x n) are split row-wise / column-wise into slices of beta bits each (beta chosen so that every slice-product
accumulated over k is exact in float64: 2 beta + ceil(log2 k) <= 52); the slice products are exact float64 matmuls (cuBLAS, no FMA ordering
dependence since every partial sum is exactly representable) and are summed in double-double arithmetic. The result equals the exact product
rounded to double-double for the slices kept (all slices here: the matrices are reconstructed exactly, so the result is the exact product to
about 2^-106 relative, limited only by the final double-double accumulation of the slice products)."""
from __future__ import annotations
import math
import torch

DT = torch.float64


def _two_sum(a, b):
    s = a + b; bb = s - a
    return s, (a - (s - bb)) + (b - bb)


def _dd_add(h1, l1, h2, l2):
    s, e = _two_sum(h1, h2); e = e + (l1 + l2)
    s2 = s + e
    return s2, e - (s2 - s)


def split_ozaki(A, k_inner, dim, beta=None, max_slices=4):
    """Split A along  (the contraction dimension of A: dim=-1 for the left factor, dim=-2 for the right factor) into slices A_1 + ... + A_s + R
    (exact decomposition) such that every slice has at most beta significant bits relative to the maximum over the contraction dimension, so
    that any slice-slice product summed over k_inner terms is exact in float64 (2 beta + ceil(log2 k) <= 52). The last element is the
    remainder (exact), which is already far below the double-double level after four slices of 18 or more bits. No Python-side data-dependent
    branching (the function is used under torch.func.jvp and vmap). Batched leading dimensions allowed. Returns (slices, beta)."""
    if beta is None:
        beta = (52 - math.ceil(math.log2(max(k_inner, 2)))) // 2
    slices = []
    R = A
    for s in range(max_slices):
        mx = R.detach().abs().amax(dim=dim, keepdim=True)
        e = torch.where(mx > 0, torch.ceil(torch.log2(torch.where(mx > 0, mx, torch.ones_like(mx)))), torch.zeros_like(mx))
        sigma = torch.pow(2.0, e + 1.0 + (53 - beta))                            # fl((R + sigma) - sigma) keeps about beta bits of R relative to 2^e
        hi = (R + sigma) - sigma
        slices.append(hi)
        R = R - hi                                                               # exact
    slices.append(R)
    return slices, beta


def matmul_dd(A, B, beta=None, max_slices=4):
    """Double-double (hi, lo) of A @ B (torch.matmul semantics, batched leading dimensions allowed) for float64 A (..., m, k), B (..., k, n):
    Ozaki slices, exact float64 slice products, double-double summation (largest slice pairs first)."""
    if A.dtype != torch.float64 or B.dtype != torch.float64:
        raise TypeError("matmul_dd needs float64 operands")
    k = A.shape[-1]
    As, bA = split_ozaki(A, k, -1, beta, max_slices)
    Bs, bB = split_ozaki(B, k, -2, beta, max_slices)
    terms = []
    for i, a in enumerate(As):
        for j, b in enumerate(Bs):
            terms.append((i + j, torch.matmul(a, b)))
    terms.sort(key=lambda t: t[0])
    hi = torch.zeros_like(terms[0][1]); lo = torch.zeros_like(hi)
    for _, P in terms:
        hi, lo = _dd_add(hi, lo, P, torch.zeros_like(P))
    return hi, lo


def matmul_dd_x(Ah, Al, B, beta=None, max_slices=4):
    """(Ah + Al) @ B in double-double for a double-double A and float64 B."""
    h1, l1 = matmul_dd(Ah, B, beta, max_slices); h2, l2 = matmul_dd(Al, B, beta, max_slices)
    return _dd_add(h1, l1, h2, l2)


# ----- double-double elementwise helpers for the pressure chain (hi, lo) tensors -----
def dd_mul_f(h, l, f):
    """(h + l) * f for float64 f (exact product by two_prod plus the low part)."""
    p = h * f; e = torch.fma(h, f, -p) if hasattr(torch, "fma") else _two_prod_err(h, f, p)
    e = e + l * f
    s = p + e
    return s, e - (s - p)


def _two_prod_err(a, b, p):
    """Error of the float64 product p = fl(a b) by Veltkamp splitting (no fma)."""
    c = 134217729.0 * a; ah = c - (c - a); al = a - ah
    c = 134217729.0 * b; bh = c - (c - b); bl = b - bh
    return ((ah * bh - p) + ah * bl + al * bh) + al * bl


def dd_add(h1, l1, h2, l2):
    return _dd_add(h1, l1, h2, l2)


def dd_div_f(h, l, f):
    """(h + l) / f for float64 f."""
    q1 = h / f
    p = q1 * f; e = _two_prod_err(q1, f, p)
    r = (h - p) - e + l                                                            # remainder (h + l) - q1 f, to float64 accuracy
    q2 = r / f
    s = q1 + q2
    return s, q2 - (s - q1)


def dd_scale(h, l, c):
    """(h + l) * c for a float64 scalar or broadcastable tensor c (same as dd_mul_f)."""
    return dd_mul_f(h, l, c)


def matmul_x_dd(A, Bh, Bl, beta=None, max_slices=4):
    """A @ (Bh + Bl) in double-double for float64 A and a double-double right factor."""
    h1, l1 = matmul_dd(A, Bh, beta, max_slices); h2, l2 = matmul_dd(A, Bl, beta, max_slices)
    return _dd_add(h1, l1, h2, l2)
