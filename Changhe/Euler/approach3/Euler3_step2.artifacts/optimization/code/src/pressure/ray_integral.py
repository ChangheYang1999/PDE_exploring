"""Independent full-space pressure gradient by the ray integral (SPEC 5.4):
    grad P(x) = (1/4 pi) int_{S^2} n int_0^inf f(x + rho n) d rho dS,   f = sum_ij d_i U_j d_j U_i,
valid for the decaying solution of -Lap P = f. Angular Gauss-Legendre x uniform directions, radial variable
rho = R_s t/(1-t) on t in (0,1) with Gauss-Legendre nodes (compactified), f evaluated with Model.fields_points.
This shares no code path with the spherical-harmonic Green solver except the field evaluator itself."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..bases.solid_harmonics import AngularGrid
from ..equations import residuals as res


def gradP_ray(model, z, points, ntheta=24, nphi=48, nrad=160, Rs=None, chunk=200000):
    pts = torch.as_tensor(points, dtype=torch.float64, device=model.r.device)
    g = AngularGrid(ntheta, nphi, device=model.r.device)
    t, wt = np.polynomial.legendre.leggauss(nrad)
    t = 0.5 * (t + 1); wt = 0.5 * wt
    t = torch.tensor(t, dtype=torch.float64, device=pts.device); wt = torch.tensor(wt, dtype=torch.float64, device=pts.device)
    out = []
    for p in pts:
        Rs_p = Rs if Rs is not None else max(1.0, float(p.norm()))
        rho = Rs_p * t / (1 - t); drho = Rs_p / (1 - t) ** 2 * wt            # (nrad,)
        Y = p[None, None, :] + rho[:, None, None] * g.n[None, :, :]           # (nrad, Na, 3)
        Yf = Y.reshape(-1, 3)
        fvals = []
        for s in range(0, Yf.shape[0], chunk):
            F = model.fields_points(z, Yf[s:s + chunk], need_vort=False, table_path="fp64")   # diagnostic cross-check on 5e5 scattered points: frozen float64 tables by name (lead 22:35Z)
            fvals.append(res.pressure_source(F['GU']))
        f = torch.cat(fvals).reshape(len(rho), g.Na)
        radial = (f * drho[:, None]).sum(0)                                   # (Na,) int f d rho along each ray
        out.append((g.n * (radial * g.w)[:, None]).sum(0) / (4 * math.pi))
    return torch.stack(out, 0)                                                # (Np, 3)
