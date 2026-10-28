"""SPEC v1.7 7.13(d)-(e) localized strength and quantitative non-axisymmetry (lead note 2026-10-24T19:27Z; no thresholds):
  R_trap: smallest sampled radius R such that c_l |y| + (y/|y|).U > 0 at every sampled point beyond R (trapping radius);
  max|U|/c_l (an upper bound for R_trap of an exact profile); max of lambda_max(S) over |y| <= R_trap (exact >= 1);
  whether the located maximum of |Omega| lies inside R_trap;
  with A = max|U| and R = 2/c_l + 4 on the ball B_{AR}: B(u) = max|DU| + A max|D^2 U| (D^2 U by central differences of
  the exact DU, step 1e-4 (1+r)), max|K U| / max|U| and int|K Omega|^2 / int|Omega|^2 with K V = J V - (J y . grad) V."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations import residuals as res

DT = torch.float64

def eigvalsh_chunked(A, chunk=8192):
    """Batched symmetric eigenvalues in chunks (cuSOLVER batched syev fails for very large batches)."""
    shp = A.shape[:-2]
    flat = A.reshape(-1, A.shape[-2], A.shape[-1])
    out = torch.cat([torch.linalg.eigvalsh(flat[i:i + chunk]) for i in range(0, flat.shape[0], chunk)], 0)
    return out.reshape(*shp, A.shape[-1])



def strength_diagnostics(model, z, c_l, omega, located_max_r=None, n_ball=4000, seed=0):
    dev = model.r.device
    F = model.fields_grid(z, need_vort=True)
    U, GU, Om = F['U'], F['GU'], F['Om']
    yv = res.yvec(F['y']); r = model.r
    n = model.grid.n.T                                                      # (3, Na)
    radial_W = c_l * r[:, None] + torch.einsum('ija,ia->ja', U, n)          # c_l |y| + n.U at (Nr, Na)
    pos = (radial_W > 0).all(dim=1)                                          # per radius: all angles outgoing
    # smallest radius beyond which all sampled radii are outgoing
    R_trap = None
    for j in range(model.Nr):
        if pos[j:].all():
            R_trap = float(r[j]); break
    A = U.norm(dim=0).max().item()
    S = 0.5 * (GU + GU.transpose(0, 1))
    lam = eigvalsh_chunked(S.permute(2, 3, 0, 1))[..., -1]             # (Nr, Na)
    inside = (r <= (R_trap if R_trap is not None else float('inf')))
    lam_in = lam[inside].max().item() if inside.any() else None
    # ball B_{AR}
    Rb = A * (2.0 / c_l + 4.0)
    rng = np.random.default_rng(seed)
    pts = torch.tensor(rng.normal(size=(n_ball, 3)), dtype=DT, device=dev)
    pts = pts / pts.norm(dim=1, keepdim=True) * torch.tensor(rng.uniform(0, 1, n_ball) ** (1 / 3) * Rb, dtype=DT, device=dev)[:, None]
    Fp = model.fields_points(z, pts, need_vort=True)
    Up, GUp, Omp = Fp['U'].T, Fp['GU'].permute(2, 0, 1), Fp['Om'].T
    maxDU = GUp.reshape(n_ball, -1).norm(dim=1).max().item()
    # D^2 U by central differences of DU
    h = 1e-4 * (1 + pts.norm(dim=1, keepdim=True))
    d2 = 0.0
    for k in range(3):
        e = torch.zeros_like(pts); e[:, k] = h[:, 0]
        Gp = model.fields_points(z, pts + e, need_vort=False)['GU'].permute(2, 0, 1); Gm = model.fields_points(z, pts - e, need_vort=False)['GU'].permute(2, 0, 1)
        d2 = d2 + (((Gp - Gm) / (2 * h[:, :, None])) ** 2).reshape(n_ball, -1).sum(1)
    maxD2U = d2.sqrt().max().item()
    maxU_ball = Up.norm(dim=1).max().item()
    # rotation generator K on U and Omega in the ball
    Jy = res.Jvec(pts.T).T
    KU = res.Jvec(Up.T).T - torch.einsum('pm,pmi->pi', Jy, GUp)
    KOm = res.Jvec(Omp.T).T - torch.einsum('pm,pmi->pi', Jy, Fp['GOm'].permute(2, 0, 1))
    return dict(R_trap=R_trap, maxU_over_cl=A / c_l, lambda_max_S_inside_Rtrap=lam_in,
                located_max_inside_Rtrap=(None if (located_max_r is None or R_trap is None) else bool(located_max_r <= R_trap)),
                ball_radius=Rb, B_u=maxDU + A * maxD2U, max_DU_ball=maxDU, max_D2U_ball=maxD2U, max_U_ball=maxU_ball,
                KU_ratio=KU.norm(dim=1).max().item() / max(maxU_ball, 1e-300),
                KOmega_L2_ratio=((KOm ** 2).sum().item() / max((Omp ** 2).sum().item(), 1e-300)),
                note="ball quantities Monte Carlo on 4000 points; D^2 U by central differences of the exact DU")
