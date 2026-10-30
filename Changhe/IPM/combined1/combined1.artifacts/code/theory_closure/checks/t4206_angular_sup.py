"""c1-t1 R1-026 remark R2: FLOAT value of the angular constant Lambda_k that would make T4-206 (10) sharp.

Run from artifacts/checks:
  OMP_NUM_THREADS=1 python3 -B t4206_angular_sup.py > t4206_angular_sup.out

Lambda_k = sup over real b(theta) with only odd angular modes of
  int cos^2(theta) (|b'|^2 + (k+2) |b|^2) dtheta / int (|b'|^2 + k |b|^2) dtheta,
computed as the largest generalized eigenvalue on the span of cos(n theta), sin(n theta), n odd <= nmax, with the
integrals evaluated exactly by an equispaced quadrature (exact for these trigonometric polynomials). Truncation is
monitored by nmax = 21, 41, 81, 161. FLOAT (LAPACK eigh); not certified.
"""
import numpy as np
from scipy.linalg import eigh

print("k  nmax  Lambda_k            T4-206 constant 1 + 2/(k+1)   mode-1 value (3k+7)/(4k+4)")
for k in range(5):
    for nmax in (21, 41, 81, 161):
        ns = np.arange(1, nmax + 1, 2)
        M = 4 * nmax + 8
        th = 2 * np.pi * np.arange(M) / M
        Bc, Bs = np.cos(np.outer(th, ns)), np.sin(np.outer(th, ns))
        B = np.hstack([Bc, Bs])
        Bp = np.hstack([-Bs * ns, Bc * ns])
        w = np.cos(th) ** 2
        num = Bp.T @ (w[:, None] * Bp) + (k + 2) * B.T @ (w[:, None] * B)
        den = Bp.T @ Bp + k * B.T @ B
        lam = eigh(num, den, eigvals_only=True)[-1]
        print(f"{k}  {nmax:4d}  {lam:.15f}   {1 + 2 / (k + 1):.6f}                     {(3 * k + 7) / (4 * k + 4):.6f}")
