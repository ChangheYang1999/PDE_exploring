"""Candidate diagnostics (EQUATIONS.md 7.3): stagnation set of V, parity defects, 3D dependence, ring Fourier content."""
import math
import torch
from . import physics as ph
from .model import apply_Q


def velocity(model, y):
    F, J = ph.derivs(lambda p: model.fields(p), y, order=1)
    return ph.curl_from_jac(J[:, :3, :])


def velocity_grad(model, y):
    F, J, H = ph.derivs(lambda p: model.fields(p), y, order=2)
    U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
    return U, gU


def find_stagnation_points(model, starts, cl, C=0.0, iters=40, tol=1e-9, R_max=None, dedupe=1e-5):
    """Batched Newton iteration for zeros of V = c_l y + C e_z + U from the given starts (N,3).
    Returns list of dicts: position, |V| residual, |Omega|, eigenvalues of grad V and of S, min |eig(grad V)|,
    number of starts that converged to it (basin count), and nearest-other-zero distance (isolation)."""
    y = starts.clone()
    ez = torch.tensor([0.0, 0.0, C], dtype=y.dtype, device=y.device)
    alive = torch.ones(y.shape[0], dtype=torch.bool, device=y.device)
    with torch.no_grad():
        pass
    for it in range(iters):
        U, gU = velocity_grad(model, y)
        U, gU = U.detach(), gU.detach()
        V = cl * y + ez + U
        A = cl * torch.eye(3, dtype=y.dtype, device=y.device) + gU
        try:
            step = torch.linalg.solve(A, V.unsqueeze(-1)).squeeze(-1)
        except Exception:
            step = torch.linalg.lstsq(A, V.unsqueeze(-1)).solution.squeeze(-1)
        # damped step, bounded length
        sn = step.norm(dim=-1, keepdim=True)
        step = step * torch.clamp(1.0 / sn.clamp_min(1e-300), max=1.0)  # full Newton step, length capped at 1
        y = y - step
        if R_max is not None:
            far = y.norm(dim=-1) > R_max
            alive = alive & ~far
    U, gU = velocity_grad(model, y)
    U, gU = U.detach(), gU.detach()
    V = cl * y + ez + U
    Vn = V.norm(dim=-1)
    conv = alive & (Vn < tol) & torch.isfinite(Vn)
    pts = y[conv]; G = gU[conv]
    zeros = []
    used = torch.zeros(pts.shape[0], dtype=torch.bool, device=y.device)
    for i in range(pts.shape[0]):
        if used[i]:
            continue
        dist = (pts - pts[i]).norm(dim=-1)
        grp = (dist < dedupe * (1.0 + pts[i].norm())) & ~used
        used = used | grp
        p = pts[grp].mean(0)
        Gi = G[grp][0]
        A = cl * torch.eye(3, dtype=y.dtype, device=y.device) + Gi
        S = 0.5 * (Gi + Gi.T)
        om = torch.stack([Gi[2, 1] - Gi[1, 2], Gi[0, 2] - Gi[2, 0], Gi[1, 0] - Gi[0, 1]])
        eA = torch.linalg.eigvals(A)
        eS = torch.linalg.eigvalsh(S)
        zeros.append({"y": p.cpu().tolist(), "R": p.norm().item(), "r": math.hypot(p[0].item(), p[1].item()), "z": p[2].item(),
                      "basin_starts": int(grp.sum().item()), "abs_Omega": om.norm().item(),
                      "eig_gradV_re": eA.real.cpu().tolist(), "eig_gradV_im": eA.imag.cpu().tolist(),
                      "min_abs_eig_gradV": eA.abs().min().item(), "eig_S": eS.cpu().tolist(), "lambda_max_S": eS.max().item(),
                      "n_negative_re_eig_gradV": int((eA.real < -1e-10).sum().item())})
    for i, zi in enumerate(zeros):
        others = [math.dist(zi["y"], zj["y"]) for j, zj in enumerate(zeros) if j != i]
        zi["nearest_other_zero"] = min(others) if others else float("inf")
    return zeros, int(conv.sum().item()), int((~conv).sum().item())


def stagnation_starts(n, R, g, device):
    """Starts: uniform in ball radius R plus axis points (n_axis = n//4)."""
    u = torch.rand(n, 1, generator=g, dtype=torch.float64)
    v = torch.randn(n, 3, generator=g, dtype=torch.float64); v = v / v.norm(dim=-1, keepdim=True)
    y = R * u ** (1 / 3) * v
    na = max(4, n // 4)
    z = (torch.rand(na, generator=g, dtype=torch.float64) * 2 - 1) * R
    ya = torch.stack([torch.zeros_like(z), torch.zeros_like(z), z], -1)
    return torch.cat([y, ya], 0).to(device)


def parity_defects(model, y):
    """Inversion defect ||U(-y) + U(y)|| / ||U|| and z-reflection defect ||U(Sz y) - Sz U(y)|| / ||U|| (Sz = diag(1,1,-1)),
    both as RMS ratios on the given points. For the unreleased seed both are ~0; the m=2 class does not require them."""
    U = velocity(model, y)
    Um = velocity(model, -y)
    Sz = torch.tensor([1.0, 1.0, -1.0], dtype=y.dtype, device=y.device)
    Us = velocity(model, y * Sz)
    n = (U ** 2).sum().clamp_min(1e-300)
    inv = ((Um + U) ** 2).sum() / n
    zr = ((Us - Sz * U) ** 2).sum() / n
    return inv.sqrt().item(), zr.sqrt().item()


def symmetry_defect(model, y):
    """Hard Q symmetry check: ||U(Qy) - Q U(y)|| / ||U|| (should be round-off)."""
    U = velocity(model, y); Uq = velocity(model, apply_Q(y))
    return (((Uq - apply_Q(U)) ** 2).sum() / (U ** 2).sum().clamp_min(1e-300)).sqrt().item()


def ring_fourier_energy(model, radii, zs, K=32):
    """Cylindrical Fourier content on rings (r, z): for each ring sample K angles, compute U^r, U^theta, U^z and their
    discrete Fourier coefficients; return energy fractions in |n| = 0, 2, 4, >=6 (both signs, sine and cosine) summed
    over components and rings, plus the max relative aliasing proxy (energy at n = K/2)."""
    dev = next(model.parameters()).device
    th = torch.arange(K, dtype=torch.float64, device=dev) * (2 * math.pi / K)
    tot = {0: 0.0, 2: 0.0, 4: 0.0, 6: 0.0, "odd": 0.0, "all": 0.0}
    for r in radii:
        for z in zs:
            y = torch.stack([r * torch.cos(th), r * torch.sin(th), torch.full_like(th, z)], -1)
            U = velocity(model, y)
            er = torch.stack([torch.cos(th), torch.sin(th), torch.zeros_like(th)], -1)
            et = torch.stack([-torch.sin(th), torch.cos(th), torch.zeros_like(th)], -1)
            comps = torch.stack([(U * er).sum(-1), (U * et).sum(-1), U[:, 2]], 0)  # (3,K)
            c = torch.fft.rfft(comps, dim=-1) / K  # n = 0..K/2
            e = (c.abs() ** 2)
            e[:, 1:] *= 2.0  # both signs
            e = e.sum(0)  # over components
            tot["all"] += e.sum().item(); tot[0] += e[0].item(); tot[2] += e[2].item() if K > 2 else 0.0
            tot[4] += e[4].item() if K > 4 else 0.0
            tot[6] += e[6:].sum().item()
            tot["odd"] += e[1::2].sum().item()
    a = max(tot["all"], 1e-300)
    return {"n0": tot[0] / a, "n2": tot[2] / a, "n4": tot[4] / a, "n6plus": tot[6] / a, "odd_frac": tot["odd"] / a}


def three_d_dependence(gU, w):
    """||d_3 U|| / ||grad U|| (weighted RMS) : an effectively 2D field has this ~0."""
    num = (w * (gU[..., :, 2] ** 2).sum(-1)).sum()
    den = (w * (gU ** 2).sum((-1, -2))).sum().clamp_min(1e-300)
    return (num / den).sqrt().item()
