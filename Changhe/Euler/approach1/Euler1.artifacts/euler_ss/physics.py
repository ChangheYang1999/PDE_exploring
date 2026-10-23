"""Derivatives (forward-mode AD via torch.func) and Euler profile residuals.

Conventions (PROMPT.md section 3): y physical similarity coordinates, c_l > 0,
    R_m   = (1-c_l) U + (c_l y + C e_z + U).grad U + grad P
    R_div = div U
    R_om  = Omega + V.grad Omega - (Omega.grad) U,   Omega = curl U, V = c_l y + C e_z + U
    R_P   = -Lap P - sum_ij (d_i U_j)(d_j U_i)
Index conventions: J[n,i,j] = d_j F_i ; H[n,i,j,k] = d_k d_j F_i ; T[n,i,j,k,l] = d_l d_k d_j F_i.
"""
import torch
from torch.func import jacfwd, vmap


def derivs(fields_fn, y, order=2, chunk=None):
    """fields_fn: (3,) -> (4,) single-point function (A_1,A_2,A_3,P). y: (N,3).
    Returns F (N,4), J (N,4,3), H (N,4,3,3) [, T (N,4,3,3,3) if order==3]."""

    def f0(p):
        return fields_fn(p)

    def f1(p):  # J with aux F
        J, F = jacfwd(lambda q: (lambda o: (o, o))(f0(q)), has_aux=True)(p)
        return J, F

    def f2(p):  # H with aux (J,F)
        H, (J, F) = jacfwd(lambda q: (lambda r: (r[0], r))(f1(q)), has_aux=True)(p)
        return H, J, F

    def f3(p):
        T, (H, J, F) = jacfwd(lambda q: (lambda r: (r[0], r))(f2(q)), has_aux=True)(p)
        return T, H, J, F

    fn = {1: f1, 2: f2, 3: f3}[order]
    if chunk is None or y.shape[0] <= chunk:
        outs = vmap(fn)(y)
    else:
        parts = [vmap(fn)(y[i:i + chunk]) for i in range(0, y.shape[0], chunk)]
        outs = tuple(torch.cat([p[k] for p in parts], 0) for k in range(len(parts[0])))
    if order == 1:
        J, F = outs
        return F, J
    if order == 2:
        H, J, F = outs
        return F, J, H
    T, H, J, F = outs
    return F, J, H, T


def curl_from_jac(JA):
    """JA[n,i,j] = d_j A_i  ->  curl A (n,3)."""
    return torch.stack([JA[..., 2, 1] - JA[..., 1, 2],
                        JA[..., 0, 2] - JA[..., 2, 0],
                        JA[..., 1, 0] - JA[..., 0, 1]], dim=-1)


def curl_grad_from_hess(HA):
    """HA[n,i,j,k] = d_k d_j A_i  ->  gU[n,i,k] = d_k (curl A)_i."""
    return torch.stack([HA[..., 2, 1, :] - HA[..., 1, 2, :],
                        HA[..., 0, 2, :] - HA[..., 2, 0, :],
                        HA[..., 1, 0, :] - HA[..., 0, 1, :]], dim=-2)


def velocity_and_grad(F, J, H):
    """From potential/pressure derivatives: U (N,3), gU (N,3,3) [gU[n,i,k]=d_k U_i], P (N,), gP (N,3), HP (N,3,3)."""
    JA = J[:, :3, :]
    HA = H[:, :3, :, :]
    U = curl_from_jac(JA)
    gU = curl_grad_from_hess(HA)
    P = F[:, 3]
    gP = J[:, 3, :]
    HP = H[:, 3, :, :]
    return U, gU, P, gP, HP


def momentum_residual(y, U, gU, gP, cl, C=0.0):
    V = cl * y + U
    if C != 0.0:
        V = V + torch.tensor([0.0, 0.0, C], dtype=y.dtype, device=y.device)
    conv = torch.einsum("nik,nk->ni", gU, V)
    Rm = (1.0 - cl) * U + conv + gP
    return Rm, V, conv


def momentum_terms(y, U, gU, gP, cl, C=0.0):
    """Individual terms for relative residual denominators (PROMPT.md section 11)."""
    lin = (1.0 - cl) * U
    ygU = torch.einsum("nik,nk->ni", gU, y)
    zgU = gU[..., 2]
    UgU = torch.einsum("nik,nk->ni", gU, U)
    return {"lin": lin, "cl_ygradU": cl * ygU, "C_dzU": C * zgU, "UgradU": UgU, "gradP": gP}


def divergence(gU):
    return gU[..., 0, 0] + gU[..., 1, 1] + gU[..., 2, 2]


def vorticity(gU):
    """Omega_i = eps_ijk d_j U_k with gU[n,i,k] = d_k U_i: Omega_1 = d_2 U_3 - d_3 U_2 = gU[2,1]-gU[1,2]."""
    return torch.stack([gU[..., 2, 1] - gU[..., 1, 2],
                        gU[..., 0, 2] - gU[..., 2, 0],
                        gU[..., 1, 0] - gU[..., 0, 1]], dim=-1)


def vorticity_residual(y, U, gU, T, cl, C=0.0):
    """Needs third derivatives of A: T[n,i,j,k,l] = d_l d_k d_j A_i.
    gradU second derivatives: HU[n,i,k,l] = d_l d_k U_i from curl of T (over the A index)."""
    TA = T[:, :3]
    HU = torch.stack([TA[..., 2, 1, :, :] - TA[..., 1, 2, :, :],
                      TA[..., 0, 2, :, :] - TA[..., 2, 0, :, :],
                      TA[..., 1, 0, :, :] - TA[..., 0, 1, :, :]], dim=-3)  # (N,3,3,3) i,k,l
    Om = vorticity(gU)
    # gOm[n,i,l] = d_l Omega_i : Omega_1 = d_2 U_3 - d_3 U_2 -> d_l: HU[2,1,l]-HU[1,2,l]
    gOm = torch.stack([HU[..., 2, 1, :] - HU[..., 1, 2, :],
                       HU[..., 0, 2, :] - HU[..., 2, 0, :],
                       HU[..., 1, 0, :] - HU[..., 0, 1, :]], dim=-2)
    V = cl * y + U
    if C != 0.0:
        V = V + torch.tensor([0.0, 0.0, C], dtype=y.dtype, device=y.device)
    Rom = Om + torch.einsum("nil,nl->ni", gOm, V) - torch.einsum("nik,nk->ni", gU, Om)
    return Rom, Om, gOm


def pressure_residual(gU, HP):
    lapP = HP[..., 0, 0] + HP[..., 1, 1] + HP[..., 2, 2]
    src = torch.einsum("nij,nji->n", gU, gU)
    return -lapP - src, lapP, src


def cylindrical_residual(y, U, gU, gP, cl, C=0.0, rmin=1e-8):
    """Independent cylindrical formulation (PROMPT.md section 3) evaluated from Cartesian derivatives
    via the chain rule; valid away from the axis. Points with r < rmin get NaN (use the Cartesian residual there).
    Returns the 4 residual components (N,4)."""
    x1, x2, z = y[..., 0], y[..., 1], y[..., 2]
    r_true = torch.sqrt(x1 * x1 + x2 * x2)
    r = r_true.clamp_min(rmin)
    ct, st = x1 / r, x2 / r
    er = torch.stack([ct, st, torch.zeros_like(ct)], -1)
    et = torch.stack([-st, ct, torch.zeros_like(ct)], -1)
    ez = torch.stack([torch.zeros_like(ct), torch.zeros_like(ct), torch.ones_like(ct)], -1)
    Ur = (U * er).sum(-1)
    Ut = (U * et).sum(-1)
    Uz = U[..., 2]
    # directional derivatives: d_r f = er.grad f ; d_theta f = r et.grad f ; d_z f = ez.grad f
    def dirderiv(gF, e):  # gF (N,3,3) [i,k]=d_k F_i -> (N,3)
        return torch.einsum("nik,nk->ni", gF, e)
    dU_r, dU_t, dU_z = dirderiv(gU, er), dirderiv(gU, et) * r.unsqueeze(-1), dirderiv(gU, ez)
    # components of derivative vectors, remembering basis vector rotation: d_theta er = et, d_theta et = -er
    def comps(dU):
        return (dU * er).sum(-1), (dU * et).sum(-1), dU[..., 2]
    dUr_r, dUt_r, dUz_r = comps(dU_r)
    dUr_tC, dUt_tC, dUz_t = comps(dU_t)  # Cartesian-vector theta derivative projected
    # d_theta er = et, d_theta et = -er  =>  d_theta Ur = (d_theta U).er + Ut ;  d_theta Ut = (d_theta U).et - Ur
    dUr_t = dUr_tC + Ut
    dUt_t = dUt_tC - Ur
    dUr_z, dUt_z, dUz_z = comps(dU_z)
    Pr = (gP * er).sum(-1)
    Pt = (gP * et).sum(-1) * r
    Pz = gP[..., 2]
    Br = cl * r + Ur
    Bz = cl * z + C + Uz
    def D(fr, ft, fz):
        return Br * fr + (Ut / r) * ft + Bz * fz
    e_r = (1 - cl) * Ur + D(dUr_r, dUr_t, dUr_z) - Ut * Ut / r + Pr
    e_t = (1 - cl) * Ut + D(dUt_r, dUt_t, dUt_z) + Ur * Ut / r + Pt / r
    e_z = (1 - cl) * Uz + D(dUz_r, dUz_t, dUz_z) + Pz
    e_div = dUr_r + Ur / r + dUt_t / r + dUz_z
    out = torch.stack([e_r, e_t, e_z, e_div], -1)
    return torch.where((r_true < rmin).unsqueeze(-1), torch.full_like(out, float("nan")), out)


def term_scale(y, cl, mode="nonlinear", l_env=1.0, lam=None):
    """Fixed normalization scale T(y) for residuals, T = (1+R^2/l^2)^(q/2), q = d + lam (d-1):
    lam=0 ('linear', q=d, the scale of the individual linear terms) ... lam=1 ('nonlinear', q=2d-1, the
    scale of the convective and pressure terms in the far field). T ~ 1 in the core."""
    d = 1.0 - 1.0 / cl
    base = 1.0 + (y * y).sum(-1) / (l_env ** 2)
    if lam is None:
        lam = {"nonlinear": 1.0, "linear": 0.0, "none": None}[mode]
    if lam is None:
        return torch.ones_like(base)
    q = d + lam * (d - 1.0)
    return base ** (0.5 * q)
