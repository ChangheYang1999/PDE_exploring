import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch, mpmath as mp
torch.set_default_dtype(torch.float64)
from src.pressure.exact_matmul import matmul_dd, split_ozaki
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
mp.mp.dps = 40
torch.manual_seed(0)
for (m, k, n) in ((7, 60576, 5), (12, 2812, 9), (40, 48, 30)):
    A = torch.randn(m, k, device=dev) * torch.logspace(-8, 8, k, device=dev)[None, :] * torch.where(torch.rand(m, k, device=dev) > 0.5, 1.0, -1.0)
    B = torch.randn(k, n, device=dev) * torch.logspace(3, -5, k, device=dev)[:, None]
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); hi, lo = matmul_dd(A, B); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_dd = time.time() - t0
    t0 = time.time(); C64 = A @ B; (torch.cuda.synchronize() if torch.cuda.is_available() else None); t64 = time.time() - t0
    An = A.cpu().numpy(); Bn = B.cpu().numpy()
    # exact reference for a few entries with mpmath
    errs_dd = []; errs_64 = []
    for (i, j) in [(0, 0), (m // 2, n // 2), (m - 1, n - 1), (1, 2)]:
        ref = mp.fsum(mp.mpf(float(An[i, t])) * mp.mpf(float(Bn[t, j])) for t in range(k))
        v = mp.mpf(float(hi[i, j])) + mp.mpf(float(lo[i, j])); v64 = mp.mpf(float(C64[i, j]))
        scale = mp.fsum(abs(mp.mpf(float(An[i, t])) * mp.mpf(float(Bn[t, j]))) for t in range(k))
        errs_dd.append(float(abs(v - ref) / scale)); errs_64.append(float(abs(v64 - ref) / scale))
    sl = split_ozaki(A, k, 1)[0]
    print(f"({m}x{k})@({k}x{n}): slices A {len(sl)} (beta {split_ozaki(A, k, 1)[1]}), time dd {t_dd:.3f}s vs fp64 {t64:.4f}s; error relative to the absolute sum: dd max {max(errs_dd):.1e}, float64 max {max(errs_64):.1e}")
