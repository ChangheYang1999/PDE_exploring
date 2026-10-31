"""SPEC 7.11 X5-style off-grid maximization of the pressure-free vorticity residual |R_Omega| per dyadic shell:
random points per shell plus gradient ascent (finite-difference gradient of |R_Omega|^2, step 1e-4 (1+r)) started from
the worst points; returns per shell the sampled and the ascended maximum of r^(1/c_l) |R_Omega| (fixed-gauge scaling)
and the ratio to the grid maximum. The momentum residual needs grad P at arbitrary points and is covered on the
holdout grid only (reported separately)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations import residuals as res

DT = torch.float64


def _ROm(model, z, pts, c_l, omega):
    F = model.fields_points(z, pts, need_vort=True)
    U, GU, Om, GOm = F['U'].T, F['GU'].permute(2, 0, 1), F['Om'].T, F['GOm'].permute(2, 0, 1)
    W = c_l * pts - omega * res.Jvec(pts.T).T + U
    R = Om + torch.einsum('pm,pmi->pi', W, GOm) + omega * res.Jvec(Om.T).T - torch.einsum('pm,pmi->pi', Om, GU)
    return R


def max_vorticity_residual(model, z, c_l, omega, edges, n_random=2048, n_ascend=20, iters=30, seed=0, grid_max=None):
    dev = model.r.device
    rng = np.random.default_rng(seed)
    out = []
    for k, (a, b) in enumerate(edges):
        lo = max(a, 1e-3 * b)
        r = np.exp(rng.uniform(np.log(lo), np.log(b), n_random)); n = rng.normal(size=(n_random, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
        pts = torch.tensor(r[:, None] * n, dtype=DT, device=dev)
        sc = lambda p: (1 + (p ** 2).sum(1) / model.R0 ** 2) ** (1 / (2 * c_l))
        f = (_ROm(model, z, pts, c_l, omega).norm(dim=1) * sc(pts))
        sampled = f.max().item()
        idx = torch.argsort(f, descending=True)[:n_ascend]
        y = pts[idx].clone(); fy = f[idx].clone()
        step = 0.05 * (b - a) * torch.ones(len(y), 1, dtype=DT, device=dev)
        for it in range(iters):
            h = 1e-4 * (1 + y.norm(dim=1, keepdim=True))
            g = torch.zeros_like(y)
            for d in range(3):
                e = torch.zeros_like(y); e[:, d] = h[:, 0]
                g[:, d] = ((_ROm(model, z, y + e, c_l, omega).norm(dim=1) * sc(y + e)) - (_ROm(model, z, y - e, c_l, omega).norm(dim=1) * sc(y - e))) / (2 * h[:, 0])
            gn = g.norm(dim=1, keepdim=True).clamp_min(1e-300)
            ynew = y + step * g / gn
            # keep inside the shell [a, b]
            rn = ynew.norm(dim=1, keepdim=True); ynew = torch.where(rn > b, ynew * (b / rn), ynew); ynew = torch.where(rn < lo, ynew * (lo / rn.clamp_min(1e-300)), ynew)
            fnew = _ROm(model, z, ynew, c_l, omega).norm(dim=1) * sc(ynew)
            better = fnew > fy
            y = torch.where(better[:, None], ynew, y); fy = torch.where(better, fnew, fy)
            step = torch.where(better[:, None], step * 1.2, step * 0.5)
        ascended = fy.max().item()
        out.append(dict(shell=[a, b], sampled_max=sampled, ascended_max=ascended, grid_max=(grid_max[k] if grid_max is not None else None),
                        ratio_to_grid=(ascended / grid_max[k] if grid_max is not None and grid_max[k] else None)))
    return out
