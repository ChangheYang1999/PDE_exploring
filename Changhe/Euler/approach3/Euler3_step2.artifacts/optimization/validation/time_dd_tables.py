"""timing of eval_solid_dd at the production grid for the field tables (degree 15, nderiv 2) and the pressure tables (degree 36, nderiv 1), and with the cache."""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from src.bases.solid_harmonics import eval_solid, eval_solid_fp64, mode_list, AngularGrid
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
g = AngularGrid(38, 74, device=dev)
for L, nd, par, lmin in ((15, 2, "even", 1), (36, 1, "even", 0), (36, 0, "even", 0)):
    modes = mode_list(L, par, l_min=lmin)
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); t0 = time.time(); eval_solid_fp64(g.n, modes, L, nd); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t1 = time.time() - t0
    t0 = time.time(); eval_solid(g.n, modes, L, nd); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t2 = time.time() - t0
    t0 = time.time(); eval_solid(g.n, modes, L, nd); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t3 = time.time() - t0
    print(f"degree {L} nderiv {nd} modes {len(modes)}: float64 {t1:.2f}s, double-double {t2:.2f}s, cached {t3:.4f}s")
