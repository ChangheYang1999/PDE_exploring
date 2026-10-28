"""Critical-point diagnostics requested by the lead (SPEC 2.1, 7.5 N2; lead note 2026-10-24T18:54Z):
 (a) continuous local maxima of |Omega|^2: Newton/gradient ascent on the smooth representation from many starts; at each
     located maximum report |Omega|, Omega.S Omega/|Omega|^2 (exact value 1 at a critical point of a solution) and the
     measured transport term W.grad(|Omega|^2/2)/|Omega|^2 (exact 0 at a critical point);
 (b) zeros of W = (c_l I - omega J) y + U: Newton from many starts; at each zero q report the spectrum of DW(q) and the
     eigenvector defect |DW(q) Omega(q) - (1+c_l) Omega(q)| / |Omega(q)| (exact 0: Omega is an eigenvector with 1+c_l,
     the other two eigenvalues sum to 2 c_l - 1).
All derivatives are the representation's own (fields_points gives DU, Omega, DOmega exactly)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations import residuals as res

DT = torch.float64


def _fields(model, z, pts):
    F = model.fields_points(z, pts, need_vort=True)
    U, GU, Om, GOm = F['U'].T, F['GU'].permute(2, 0, 1), F['Om'].T, F['GOm'].permute(2, 0, 1)   # (Np,3), (Np,3(m),3(i))
    return U, GU, Om, GOm


def local_maxima_omega(model, z, c_l, omega, n_starts=200, r_range=(0.02, 30.0), iters=40, seed=0, top=8, dedup=1e-2):
    """Ascent on f = |Omega|^2: Newton step using the exact gradient 2 (DOmega) Omega and a finite-difference Hessian
    of the gradient (step 1e-5 relative), with backtracking; converged if |grad f| < 1e-10 |f|/r_scale."""
    rng = np.random.default_rng(seed)
    r = np.exp(rng.uniform(np.log(r_range[0]), np.log(r_range[1]), n_starts)); n = rng.normal(size=(n_starts, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
    y = torch.tensor(r[:, None] * n, dtype=DT, device=model.r.device)
    def f_and_grad(pts):
        U, GU, Om, GOm = _fields(model, z, pts)
        f = (Om ** 2).sum(1)
        g = 2 * torch.einsum('pmi,pi->pm', GOm, Om)          # d_m |Om|^2 = 2 Om_i d_m Om_i
        return f, g
    f, g = f_and_grad(y)
    for it in range(iters):
        # Hessian by central differences of the gradient (per point, 3 directions)
        h = 1e-5 * (1 + y.norm(dim=1, keepdim=True))
        H = torch.zeros(y.shape[0], 3, 3, dtype=DT, device=y.device)
        for k in range(3):
            e = torch.zeros_like(y); e[:, k] = h[:, 0]
            _, gp = f_and_grad(y + e); _, gm = f_and_grad(y - e)
            H[:, :, k] = (gp - gm) / (2 * h)
        H = 0.5 * (H + H.transpose(1, 2))
        # ascent direction: Newton if H negative definite, else gradient ascent scaled
        evals = torch.linalg.eigvalsh(H)
        step = torch.zeros_like(y)
        nd = evals[:, -1] < 0
        if nd.any():
            step[nd] = -torch.linalg.solve(H[nd], g[nd].unsqueeze(-1)).squeeze(-1)
        gn = g.norm(dim=1, keepdim=True).clamp_min(1e-300)
        step[~nd] = g[~nd] / gn[~nd] * 0.1 * (1 + y[~nd].norm(dim=1, keepdim=True))
        # backtracking on f increase
        alpha = torch.ones(y.shape[0], 1, dtype=DT, device=y.device)
        for _ in range(12):
            ynew = y + alpha * step
            fnew, gnew = f_and_grad(ynew)
            ok = fnew > f
            if ok.all():
                break
            alpha[~ok] *= 0.5
        y = torch.where(ok[:, None], ynew, y); f = torch.where(ok, fnew, f); g = torch.where(ok[:, None], gnew, g)
    # evaluate at the final points
    U, GU, Om, GOm = _fields(model, z, y)
    f = (Om ** 2).sum(1); g = 2 * torch.einsum('pmi,pi->pm', GOm, Om)
    yv = y
    W = c_l * yv - omega * res.Jvec(yv.T).T + U
    transport = torch.einsum('pm,pm->p', W, g) / 2 / f.clamp_min(1e-300)             # W.grad(|Om|^2/2)/|Om|^2
    S = 0.5 * (GU + GU.transpose(1, 2))
    strain = torch.einsum('pi,pij,pj->p', Om, S, Om) / f.clamp_min(1e-300)
    lamS = torch.linalg.eigvalsh(S)[:, -1]
    conv = g.norm(dim=1) / (f / (1 + y.norm(dim=1))).clamp_min(1e-300)
    # classify by the Hessian of |Omega|^2 at the final point (negative definite = strict local maximum)
    hfd = 1e-5 * (1 + y.norm(dim=1, keepdim=True)); Hf = torch.zeros(y.shape[0], 3, 3, dtype=DT, device=y.device)
    for k in range(3):
        e = torch.zeros_like(y); e[:, k] = hfd[:, 0]
        _, gp = f_and_grad(y + e); _, gm = f_and_grad(y - e); Hf[:, :, k] = (gp - gm) / (2 * hfd)
    Hf = 0.5 * (Hf + Hf.transpose(1, 2)); hess_max_eig = torch.linalg.eigvalsh(Hf)[:, -1]
    order = torch.argsort(f, descending=True)
    out = []
    for i in order.tolist():
        yi = y[i]
        if conv[i] > 1e-6:          # keep located (converged) maxima only
            continue
        if any((yi - torch.tensor(o['y'], dtype=DT, device=y.device)).norm().item() < dedup * (1 + yi.norm().item()) for o in out):
            continue
        out.append(dict(y=[float(v) for v in yi], r=float(yi.norm()), abs_Omega=float(f[i].sqrt()), strain_ratio=float(strain[i]), transport_ratio=float(transport[i]),
                        lambda_max_S=float(lamS[i]), grad_rel=float(conv[i]), converged=bool(conv[i] < 1e-8),
                        hessian_max_eig=float(hess_max_eig[i]), is_local_max=bool(hess_max_eig[i] < 0)))
        if len(out) >= top:
            break
    return out


def zeros_of_W(model, z, c_l, omega, n_starts=200, r_range=(0.02, 30.0), iters=50, seed=1, top=10, dedup=1e-3):
    rng = np.random.default_rng(seed)
    r = np.exp(rng.uniform(np.log(r_range[0]), np.log(r_range[1]), n_starts)); n = rng.normal(size=(n_starts, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
    y = torch.tensor(r[:, None] * n, dtype=DT, device=model.r.device)
    J = torch.tensor([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=DT, device=y.device)
    A = c_l * torch.eye(3, dtype=DT, device=y.device) - omega * J
    def W_and_DW(pts):
        U, GU, Om, GOm = _fields(model, z, pts)
        W = pts @ A.T + U                                   # (Np,3): (c_l I - omega J) y + U
        DW = A.T[None] + GU                                 # DW[p, m, i] = d_m W_i = A_im + d_m U_i
        return W, DW, Om
    for it in range(iters):
        W, DW, Om = W_and_DW(y)
        # Newton: y_new = y - (DW^T)^-1 W  with DW[m,i] = d_m W_i -> Jacobian matrix Jac[i,m] = DW[m,i]
        Jac = DW.transpose(1, 2)
        try:
            step = -torch.linalg.solve(Jac, W.unsqueeze(-1)).squeeze(-1)
        except RuntimeError:
            step = -W
        sn = step.norm(dim=1, keepdim=True); maxstep = 0.5 * (1 + y.norm(dim=1, keepdim=True))
        step = step * torch.clamp(maxstep / sn.clamp_min(1e-300), max=1.0)
        y = y + step
    W, DW, Om = W_and_DW(y)
    resid = W.norm(dim=1) / (1 + y.norm(dim=1))
    order = torch.argsort(resid)
    out = []
    for i in order.tolist():
        if resid[i] > 1e-9:
            break
        yi = y[i]
        if any((yi - torch.tensor(o['y'], dtype=DT, device=y.device)).norm().item() < dedup * (1 + yi.norm().item()) for o in out):
            continue
        Jm = DW[i].T                                        # matrix (DW)_{im} = d_m W_i acting on vectors: (DW v)_i = sum_m d_m W_i v_m ... use Jm = Jac
        ev = torch.linalg.eigvals(Jm)
        om = Om[i]; omn = om.norm().item()
        defect = ((Jm @ om - (1 + c_l) * om).norm() / max(omn, 1e-300)).item() if omn > 0 else None
        out.append(dict(y=[float(v) for v in yi], r=float(yi.norm()), W_resid=float(resid[i]), abs_Omega=omn,
                        DW_eigs=[[float(e.real), float(e.imag)] for e in ev], eigvec_defect=defect, trace_DW=float(Jm.trace()),
                        expected=dict(eig_along_Omega=1 + c_l, other_two_sum=2 * c_l - 1)))
        if len(out) >= top:
            break
    return out
