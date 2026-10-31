"""First nonlinear far-field correction G[F] (SPEC 3, prompt section 3 'First nonlinear correction') and its distance to the angular
span carried by the rate-(2alpha+1) channels B, D (SPEC 4.4 angular closure; lead 2026-10-24T22:40Z request (a)).

Method (independent of the SPEC spherical-component formulas, which it reproduces numerically):
  the exact homogeneous leading tail is U_0 = curl(T_0 y) + curl curl(S_0 y) with
      T_0(y) = r^-alpha     sum_q t_q P_q(R_{chi0(r)} n),   S_0(y) = r^(1-alpha) sum_q s_q P_q(R_{chi0(r)} n),
  P_q real orthonormal spherical harmonics (regular solid harmonics at |n| = 1), R_{chi0} the rotation about the z axis by
  chi0(r) = (omega/c_l) log(r/R0) (the twist: field = c cos(m(phi+chi0)) + s sin(m(phi+chi0)), the convention of
  spec_diagnostics.leading_tail_field), t_q, s_q the tail amplitudes of Problem.tail_amplitudes. U_0, DU_0 are obtained by torch
  autograd of these closed forms (exact derivatives). (U_0.grad)U_0 = r^-(2alpha+1) N(theta, chi).
  Pressure: -Delta P_0 = tr(DU_0 DU_0) = r^-(2alpha+2) Sigma(theta, chi); mode by mode in the twisted frame the particular solution is
  P_0 = r^-2alpha Q with q_lm = sigma_lm / (-lambda_lm), lambda_lm = (-2alpha + i m kappa)(1 - 2alpha + i m kappa) - l(l+1), kappa = omega/c_l,
  complex pairs sigma = sigma_c - i sigma_s (Re[sigma e^{i m chi}] = sigma_c cos + sigma_s sin). The harmonic (global) pressure parts enter
  the velocity at rate 4, not 2alpha+1 (SPEC 3.5), so they do not contribute to G.
  G(n) = R0^(2alpha+1) [ (U_0.grad)U_0 + grad P_0 ](R0 n)   (at r = R0 the twist angle is zero, chi = phi).
Carried span: the asymptotic velocity patterns of the B columns (T = r^-(2alpha+1) P_q(R n)) and D columns (S = r^-2alpha P_q(R n)) of
the model's channel modes, evaluated at r = R0 (all Chebyshev columns of one mode share the pattern since Phi_k(1) = 1). dist(G, span)
is the L2(S^2) least-squares residual; the rank of the pattern matrix and the coefficients are reported.
Norms: ||.|| = L2(S^2, dS) (the F-gauge has ||F|| = 1).
D6FP 2026-10-28: first_correction, carried_patterns and closure_distance evaluate the homogeneous potentials through homogeneous_velocity_exact /
twisted_scalar_gradient_exact (production jets + double-double tables, end of this file); the autograd path (eval_Y, homogeneous_velocity) is kept
for the complete-gradient graph (first_correction_graph) and as the reference it was compared with (agreement 1e-15, validation/test_closure_exact_path.json)."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import alpha_of
from ..bases.solid_harmonics import eval_solid, AngularGrid, mode_list

DT = torch.float64


def _rotate_z(n, ang):
    c, s = torch.cos(ang), torch.sin(ang)
    return torch.stack([n[..., 0] * c - n[..., 1] * s, n[..., 0] * s + n[..., 1] * c, n[..., 2]], -1)


EVAL_Y_CALLS = [0]


def eval_Y(y, modes, L):
    """Real solid harmonics P_q(y) (the convention of bases.solid_harmonics.eval_solid: orthonormal real spherical harmonics at |y| = 1)
    by a functional recursion (no in-place writes), so that torch autograd can differentiate through the points to any order."""
    EVAL_Y_CALLS[0] += 1                                                   # D6FP: call counter (G5 (c) scope record; must be 0 on the production routes)
    x, yy, z = y[..., 0], y[..., 1], y[..., 2]
    rho = x * x + yy * yy + z * z
    Re = {(0, 0): torch.ones_like(x)}; Im = {(0, 0): torch.zeros_like(x)}
    for m in range(1, L + 1):
        pr, pi_ = Re[(m - 1, m - 1)], Im[(m - 1, m - 1)]
        Re[(m, m)] = (x * pr - yy * pi_) / (2 * m); Im[(m, m)] = (x * pi_ + yy * pr) / (2 * m)
    for m in range(0, L):
        Re[(m + 1, m)] = z * Re[(m, m)]; Im[(m + 1, m)] = z * Im[(m, m)]
    for m in range(0, L + 1):
        for l in range(m + 2, L + 1):
            c = 1.0 / ((l - m) * (l + m))
            Re[(l, m)] = ((2 * l - 1) * z * Re[(l - 1, m)] - rho * Re[(l - 2, m)]) * c
            Im[(l, m)] = ((2 * l - 1) * z * Im[(l - 1, m)] - rho * Im[(l - 2, m)]) * c
    out = []
    for (l, m, t) in modes:
        N = math.sqrt((2 * l + 1) / (4 * math.pi) * math.factorial(l - m) / math.factorial(l + m))
        if m == 0:
            out.append(N * math.factorial(l) * Re[(l, 0)])
        else:
            f = math.sqrt(2.0) * N * math.factorial(l + m)
            out.append(f * (Re[(l, m)] if t == 0 else Im[(l, m)]))
    return torch.stack(out, dim=-1)


def _potential(y, coef, p, modes, Lmax, kappa, R0):
    """r^-p sum_q coef[q, j] P_q(R_{chi0(r)} n) at points y (..., 3); coef (Nq, J) -> (..., J) (or (Nq,) -> (...))."""
    r = y.norm(dim=-1)
    n = y / r[..., None]
    chi0 = kappa * torch.log(r / R0)
    P = eval_Y(_rotate_z(n, chi0), modes, Lmax)
    return (r ** (-p))[..., None] * (P @ coef) if coef.dim() == 2 else (r ** (-p)) * (P @ coef)


def homogeneous_velocity(y, tcoef, scoef, pT, pS, modes, Lmax, kappa, R0, need_grad=True):
    """U = curl(T y) + curl curl(S y) for T = r^-pT sum t_q P_q(R n), S = r^-pS sum s_q P_q(R n); batched over the last
    coefficient index J: tcoef, scoef (Nq, J) or None. y: (N, 3). Returns U (J, N, 3) and GU (J, N, 3, 3) with GU[..., m, i] = d_m U_i."""
    J = (tcoef if tcoef is not None else scoef).shape[1]
    N = y.shape[0]
    yr = y[None].expand(J, N, 3).clone().requires_grad_(True)
    U = 0
    # D6FP 2026-10-28: one batched evaluation of the solid harmonics on the (J, N, 3) points instead of J separate calls (same values up to
    # summation order; the per-column gradients come from one autograd pass since column j depends on yr[j] only). The frozen loop took
    # several seconds per call at J = 233 columns and was called at every trial point of the free-parameter optimizer.
    def _batched_potential(coef, p):
        r = yr.norm(dim=-1)                                                                   # (J, N)
        n = yr / r[..., None]
        chi0 = kappa * torch.log(r / R0)
        P = eval_Y(_rotate_z(n, chi0), modes, Lmax)                                           # (J, N, Nq)
        return (r ** (-p)) * (P * coef.T[:, None, :]).sum(-1)                                 # (J, N): column j uses coef[:, j]
    if tcoef is not None:
        T = _batched_potential(tcoef, pT)
        gT = torch.autograd.grad(T.sum(), yr, create_graph=True)[0]
        U = U - torch.cross(yr, gT, dim=-1)
    if scoef is not None:
        S = _batched_potential(scoef, pS)
        gS = torch.autograd.grad(S.sum(), yr, create_graph=True)[0]                           # (J, N, 3)
        H = torch.stack([torch.autograd.grad(gS[..., i].sum(), yr, create_graph=True)[0] for i in range(3)], -2)   # H[..., i, j] = d_i d_j S
        lap = H[..., 0, 0] + H[..., 1, 1] + H[..., 2, 2]
        gK = 2 * gS + torch.einsum('jnik,jnk->jni', H, yr)
        U = U + gK - yr * lap[..., None]
    if not need_grad:
        return U.detach(), None
    GU = torch.stack([torch.autograd.grad(U[..., i].sum(), yr, create_graph=True)[0] for i in range(3)], -1)   # GU[..., m, i] = d_m U_i
    return U, GU


def first_correction(prob, z, ntheta=None, nphi=None, device=None):
    """G[F] of the state's leading tail on a Gauss grid at r = R0. Returns dict with the grid, G (Na, 3), N (Na, 3), gradQ (Na, 3),
    norms and the F norm (all L2(S^2))."""
    model = prob.model
    device = device or model.r.device
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega); alpha = alpha_of(c_lf); kappa = omf / c_lf; R0 = model.R0
    L = model.L
    ntheta = ntheta or (2 * L + 10); nphi = nphi or (4 * L + 18)
    grid = AngularGrid(ntheta, nphi, device=device)
    n = grid.n; w = grid.w                                                 # (Na, 3), weights summing to 4 pi
    y = R0 * n
    t, s = prob.tail_amplitudes(aT.detach(), aS.detach(), torch.tensor(c_lf, dtype=DT, device=device))
    t = t.detach(); s = s.detach()
    modes = model.modes; Lmax = getattr(model, "L_ext", L)
    # D6FP 2026-10-28: exact path (production jets + double-double tables; G5 (c) scope), agreeing with the former autograd path to 1e-15
    U, GU = homogeneous_velocity_exact(y, t, s, alpha, alpha - 1.0, modes, Lmax, kappa, R0)
    U = U[0]; GU = GU[0]                                                   # (Na, 3), (Na, 3, 3)
    Nvec = torch.einsum('am,ami->ai', U, GU)                               # (U.grad)U at r = R0
    src = torch.einsum('aij,aji->a', GU, GU)                               # tr(DU DU) at r = R0
    # pressure: analyse the source at r = R0 (chi = phi), solve mode by mode in the twisted frame, synthesize P_0 and its gradient
    Lq = 2 * L + 6
    pmodes = mode_list(Lq, model.m_parity, l_min=0)
    Yp = eval_solid(n, pmodes, Lq, 0, path="dd")[0]                                   # (Na, Nqp)
    sig = (Yp * (w * src.detach())[:, None]).sum(0) * R0 ** (2 * alpha + 2)   # coefficients of Sigma(theta, chi) at chi = phi
    qcoef = torch.zeros_like(sig)
    idx = {mode: i for i, mode in enumerate(pmodes)}
    for (l, m, tt) in pmodes:
        if tt == 1:
            continue
        lam = complex(-2 * alpha, m * kappa) * complex(1 - 2 * alpha, m * kappa) - l * (l + 1)
        if m == 0:
            qcoef[idx[(l, 0, 0)]] = sig[idx[(l, 0, 0)]] / (-lam.real)
        else:
            sc, ss = sig[idx[(l, m, 0)]].item(), sig[idx[(l, m, 1)]].item()
            q = complex(sc, -ss) / (-lam)
            qcoef[idx[(l, m, 0)]] = q.real; qcoef[idx[(l, m, 1)]] = -q.imag
    P0, gP = twisted_scalar_gradient_exact(y, qcoef, 2 * alpha, pmodes, Lq, kappa, R0)       # D6FP: exact tables + jets instead of autograd through eval_Y
    G = (R0 ** (2 * alpha + 1)) * (Nvec.detach() + gP)
    def l2(X):
        return math.sqrt(float(((X ** 2).sum(-1) * w).sum()))
    F = (R0 ** alpha) * U.detach()
    # SPEC v1.24 7.8 (lead 2026-10-25T09:58Z item 1; d78 / FINAL_REPORT section 2 item 34): the leading vorticity coefficient H (Omega_0 = r^-(alpha+1) H)
    # from the exact gradient GU[a, m, i] = d_m U_i of the homogeneous tail at r = R0, and the leading pressure coefficient Q (P_0 = r^-2alpha Q)
    GUd = GU.detach()
    curlU0 = torch.stack([GUd[:, 1, 2] - GUd[:, 2, 1], GUd[:, 2, 0] - GUd[:, 0, 2], GUd[:, 0, 1] - GUd[:, 1, 0]], -1)
    H = (R0 ** (alpha + 1)) * curlU0
    Q = (R0 ** (2 * alpha)) * P0.detach()
    return dict(grid=grid, n=n, w=w, G=G.detach(), N=(R0 ** (2 * alpha + 1)) * Nvec.detach(), gradQ=(R0 ** (2 * alpha + 1)) * gP.detach(), F=F, H=H, Q=Q,
                H_norm=l2(H), H_F=float(((F * H).sum(-1) * w).sum()),
                G_norm=l2(G), N_norm=l2((R0 ** (2 * alpha + 1)) * Nvec), gradQ_norm=l2((R0 ** (2 * alpha + 1)) * gP), F_norm=l2(F),
                source_resolution=float((sig.abs()[torch.tensor([l for (l, m, tt) in pmodes], device=device) >= Lq - 1]).abs().max() / sig.abs().max().clamp_min(1e-300)),
                c_l=c_lf, omega=omf, alpha=alpha, ntheta=ntheta, nphi=nphi, pmodes_degree=Lq)


def carried_mode_sets(model, modes_B=None, modes_D=None):
    """The B and D mode lists of the carried rate-(2alpha+1) channels (default: the model's own), the union mode list used to build the
    homogeneous potentials and its maximal degree."""
    mB = modes_B if modes_B is not None else [model.modes[i] for i in model.chan_cols["B"].tolist()] if model.channels.get("NkB", 0) > 0 else []
    mD = modes_D if modes_D is not None else [model.modes[i] for i in model.chan_cols["D"].tolist()] if model.channels.get("NkD", 0) > 0 else []
    allm = sorted(set(mB) | set(mD) | set(model.modes), key=lambda q: (q[0], q[1], q[2]))
    Lmax = max([q[0] for q in allm] + [1])
    return mB, mD, allm, Lmax


def carried_patterns(model, c_l, omega, y, modes_B=None, modes_D=None):
    """Asymptotic velocity patterns at points y of the B columns (T = r^-(2alpha+1) P_q(R n)) and D columns (S = r^-2alpha P_q(R n)).
    modes_B/modes_D: lists of (l, m, t); default the model's carried B/D modes. Returns (V (Na, 3, J), labels)."""
    alpha = alpha_of(float(c_l)); kappa = float(omega) / float(c_l); R0 = model.R0
    mB, mD, allm, Lmax = carried_mode_sets(model, modes_B, modes_D)
    cols, labels = [], []
    if mB:
        E = torch.zeros(len(allm), len(mB), dtype=DT, device=y.device)
        for j, q in enumerate(mB):
            E[allm.index(q), j] = 1.0
        VB = homogeneous_patterns_exact(y, E, None, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0)   # (J, Na, 3); D6FP exact path, batched over the columns (validation/test_patterns_batched.py: 3e-17 vs per-column)
        cols.append(VB.permute(1, 2, 0)); labels += [("B",) + q for q in mB]
    if mD:
        E = torch.zeros(len(allm), len(mD), dtype=DT, device=y.device)
        for j, q in enumerate(mD):
            E[allm.index(q), j] = 1.0
        VD = homogeneous_patterns_exact(y, None, E, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0)
        cols.append(VD.permute(1, 2, 0)); labels += [("D",) + q for q in mD]
    if not cols:
        return None, []
    return torch.cat(cols, -1) * (R0 ** (2 * alpha + 1)), labels


def far_helicity_coefficients(fc, Gc=None, Gc_curl=None):
    """SPEC v1.24 7.8 (lead 2026-10-25T09:58Z item 1; derivation d78, FINAL_REPORT section 2 item 34; the exterior form proved by the
    independent route 09:35Z and reviewed in d81). All integrals over S^2 with the Gauss weights w of fc, fields at r = R0 (chi = phi).
      K_H(required) = (1 - 3 alpha) Psi_F,   Psi_F = int [ (F.H) F_r + (Q - |F|^2/2) H_r ] dS
      K_H(carried)  = s^(3 alpha + 2) int (U_0 . curl V_1 + V_1 . Omega_0)(s n) dS for the carried V_1 = r^-(2alpha+1) G_carried (independent of s).
    Sphere form of the carried value (lead 09:48Z item 4): since U_0 . curl V_1 + V_1 . Omega_0 = 2 V_1 . Omega_0 + div(V_1 x U_0) and V_1 x U_0 is
    twisted-homogeneous of degree -(3 alpha + 1) with sphere flux C s^(1 - 3 alpha), C = int n . (G x F), the divergence theorem on a shell gives
    s^(3 alpha + 2) int div(V_1 x U_0) dS = (1 - 3 alpha) C, so K_H(carried) = 2 int G . H - (1 - 3 alpha) int n . (F x G).
    The same formula with G = G_required equals (1 - 3 alpha) Psi_F exactly (identity (I) of d78 for (U_0, P_0)); their numerical agreement is the
    closure check 'K_H_identity_rel_closure'. With Q + |F|^2/2 in place of Q - |F|^2/2 the identity fails (negative control). When the carried
    field's exact curl at R0 is supplied (Gc_curl = R0^(2alpha+2) curl V_1), the direct form int (F . Gc_curl + G_carried . H) is the second form of
    K_H(carried). Both ratios carried/required equal 1 for an exact profile where the required value is nonzero; the energy and helicity ratios are
    different projections of the defect V_1 - N_0 (equality of either does not imply V_1 = N_0)."""
    alpha = fc["alpha"]; F, H, Q, n, w = fc["F"], fc["H"], fc["Q"], fc["n"], fc["w"]
    def ip(X, Y):
        return float(((X * Y).sum(-1) * w).sum())
    def sp(f):
        return float((f * w).sum())
    Fr = (F * n).sum(-1); Hr = (H * n).sum(-1); FH = (F * H).sum(-1); F2 = (F ** 2).sum(-1)
    Psi_F = sp(FH * Fr + (Q - 0.5 * F2) * Hr)
    Psi_F_wrong = sp(FH * Fr + (Q + 0.5 * F2) * Hr)
    c13 = 1.0 - 3.0 * alpha
    def KH_of(G):
        return 2.0 * ip(G, H) - c13 * sp((n * torch.cross(F, G, dim=-1)).sum(-1))
    KH_req = c13 * Psi_F; KH_req_id = KH_of(fc["G"])
    scale = max(abs(KH_req), abs(KH_req_id), 1e-300)
    out = dict(Psi_F=Psi_F, K_H_required=KH_req, K_H_required_identity_form=KH_req_id, K_H_identity_rel_closure=abs(KH_req - KH_req_id) / scale,
               K_H_negative_control_rel=abs(c13 * Psi_F_wrong - KH_req_id) / scale, H_F_tail=ip(F, H), H_norm=math.sqrt(max(ip(H, H), 0.0)),
               note_K_H="SPEC v1.24 7.8: K_H(required) = (1 - 3 alpha) Psi_F; K_H(carried) = 2 int G_c.H - (1 - 3 alpha) int n.(F x G_c) (sphere form; direct curl form when present); exact profile: ratio 1")
    if Gc is not None:
        KH_car = KH_of(Gc)
        out.update(K_H_carried=KH_car, K_H_ratio_direct=(KH_car / KH_req if abs(KH_req) > 1e-300 else None))
        if Gc_curl is not None:
            KH_dir = ip(F, Gc_curl) + ip(Gc, H)
            out.update(K_H_carried_direct_curl=KH_dir, K_H_carried_two_forms_rel=abs(KH_dir - KH_car) / max(abs(KH_car), abs(KH_dir), 1e-300))
    return out


def closure_distance(prob, z, modes_B=None, modes_D=None, fc=None, rcond=1e-10):
    """dist(G[F], carried span)/||G[F]|| with the least-squares projection on the sphere (weights w); rank of the pattern matrix.
    With the model's own channels also: the carried G (from the state's B/D coefficients), its mismatch and correlation against G[F], the direct
    far-energy ratio K_E(carried)/K_E(required) (lead d67), the far-helicity coefficients and ratio (SPEC v1.24 7.8) and the F-component of the
    vector defect G_carried - G_required with the d84 bound (lead 2026-10-25T09:58Z items 2-3)."""
    model = prob.model
    fc = fc or first_correction(prob, z)
    aT, aS, c_l, omega = model.unpack(z)
    V, labels = carried_patterns(model, float(c_l), float(omega), model.R0 * fc["n"], modes_B, modes_D)
    if V is None:
        out = dict(G_norm=fc["G_norm"], dist=fc["G_norm"], dist_rel=1.0, rank=0, n_columns=0, note="no rate-(2alpha+1) channel carried: the distance is ||G[F]|| itself")
        try:                                                                         # required coefficients exist without carried channels (carried = 0)
            kh = far_helicity_coefficients(fc, Gc=torch.zeros_like(fc["G"]))
            out.update({k: v for k, v in kh.items()}); out.update(K_required_over2=float(((fc["F"] * fc["G"]).sum(-1) * fc["w"]).sum()), K_carried_over2=0.0, K_ratio_direct=0.0, carried_mismatch_rel=1.0, G_carried_norm=0.0)
        except Exception as e:
            out["K_H_error"] = repr(e)
        return out
    sw = fc["w"].sqrt()
    A = (V * sw[:, None, None]).reshape(-1, V.shape[-1])
    b = (fc["G"] * sw[:, None]).reshape(-1)
    sol = torch.linalg.lstsq(A.cpu(), b.cpu()[:, None], rcond=rcond, driver="gelsd")
    coef = sol.solution[:, 0].to(A.device)
    res = b - A @ coef
    dist = float(res.norm())
    rank = int(sol.rank.item()) if hasattr(sol, "rank") and sol.rank is not None and sol.rank.numel() else None
    svals = torch.linalg.svdvals(A.cpu())
    out = dict(G_norm=fc["G_norm"], N_norm=fc["N_norm"], gradQ_norm=fc["gradQ_norm"], F_norm=fc["F_norm"], dist=dist, dist_rel=dist / max(fc["G_norm"], 1e-300),
               rank=rank, n_columns=int(A.shape[1]), sigma_max=float(svals[0]), sigma_min=float(svals[-1]), coef_norm=float(coef.norm()),
               max_B_degree=max([q[1] for q in labels if q[0] == "B"] + [0]), max_D_degree=max([q[1] for q in labels if q[0] == "D"] + [0]),
               source_resolution=fc["source_resolution"], ntheta=fc["ntheta"], nphi=fc["nphi"])
    # G actually CARRIED by the state's B/D coefficients (SPEC 3: the rate-(2alpha+1) coefficient must equal G[F] for an exact profile):
    # asymptotically T_q -> r^-(2alpha+1) R0^(2alpha+1+l) sum_k B_kq P_q(R n) and S_q -> r^-2alpha R0^(2alpha+l) sum_k D_kq P_q(R n)
    # (Phi_k(1) = 1, damping -> 1), so G_carried = sum_q cB_q V^B_q + cD_q V^D_q with the unit patterns V of carried_patterns.
    if modes_B is None and modes_D is None:
        try:
            d = model.unpack_all(z); alpha = alpha_of(float(c_l)); R0 = model.R0; kappa = float(omega) / float(c_l)
            coefs = []
            for lab in labels:
                kind, (l, m, t) = lab[0], lab[1:]
                qi = model.modes.index((l, m, t))
                if kind == "B":
                    coefs.append(float(d["B"][:, qi].sum()) * R0 ** (2 * alpha + 1 + l))
                else:
                    coefs.append(float(d["D"][:, qi].sum()) * R0 ** (2 * alpha + l))
            cvec = torch.tensor(coefs, dtype=DT, device=V.device)
            Gc = torch.einsum('aij,j->ai', V, cvec)                                # (Na, 3)
            w = fc["w"]
            def ip(X, Y):
                return float(((X * Y).sum(-1) * w).sum())
            nGc = math.sqrt(max(ip(Gc, Gc), 0.0)); nG = fc["G_norm"]
            # lead d67 / verifier 2026-10-25T06:38Z: the first far energy coefficient K_1 = 2 int_S2 F . G dS (= 2 (2 - 3 alpha) Phi_F); the direct
            # limiting ratio K_carried / K_required = <F, G_carried> / <F, G_required> (exact profile: 1), not the finite-radius quotient kappa
            FG_req = ip(fc["F"], fc["G"]); FG_car = ip(fc["F"], Gc)
            mism = math.sqrt(max(ip(fc["G"] - Gc, fc["G"] - Gc), 0.0))
            out.update(G_carried_norm=nGc, carried_mismatch_rel=mism / max(nG, 1e-300),
                       carried_correlation=(ip(fc["G"], Gc) / max(nG * nGc, 1e-300)) if nGc > 0 else None,
                       K_required_over2=FG_req, K_carried_over2=FG_car, K_ratio_direct=(FG_car / FG_req if abs(FG_req) > 1e-300 else None),
                       note_carried="carried_mismatch_rel = ||G_required - G_carried||/||G_required|| (exact profile: 0); dist_rel is the distance to the SPAN only; K_ratio_direct = <F, G_carried>/<F, G_required> (exact profile: 1)")
            # lead 2026-10-25T09:58Z items 2-3 (d84): the F-component of the vector defect, its cosine against F (||F|| = 1 in the gauge) and the
            # Cauchy-Schwarz bound |energy ratio - 1| <= m / c, m = carried_mismatch_rel, c = |K_E required| / (2 ||G_required||) = |<F, G_req>| / ||G_req||
            dF = FG_car - FG_req
            c_d84 = abs(FG_req) / max(nG, 1e-300)
            par2 = (dF / max(fc["F_norm"], 1e-300)) ** 2                                       # squared norm of the defect's component along F
            orth = math.sqrt(max(mism ** 2 - par2, 0.0))                                       # norm of the part orthogonal to F (lead 10:12Z: angular shape, same radial order)
            out.update(G_defect_F_component=dF, G_defect_cos_F=(dF / max(fc["F_norm"] * mism, 1e-300)) if mism > 0 else None,
                       G_defect_parallel_fraction=(par2 / max(mism ** 2, 1e-300)) if mism > 0 else None, G_defect_orth_norm=orth, G_defect_orth_rel=orth / max(nG, 1e-300),
                       G_defect_parallel_rel=math.sqrt(par2) / max(nG, 1e-300),
                       d84_c=c_d84, d84_bound_energy_ratio=(out["carried_mismatch_rel"] / c_d84) if c_d84 > 0 else None,
                       note_d84="G_defect_F_component = int F.(G_carried - G_required) dS = (K_E carried - K_E required)/2; parallel fraction = share of the squared defect along F; G_defect_orth_norm = norm of the part orthogonal to F (both parts relative to ||G_required|| in *_rel); |K_ratio_direct - 1| <= d84_bound_energy_ratio")
            # SPEC v1.24 7.8 far-helicity coefficients: sphere form and the direct curl form (exact gradient of the carried homogeneous field at R0)
            try:
                mB, mD, allm, Lmax = carried_mode_sets(model, None, None)
                tB = torch.zeros(len(allm), dtype=DT, device=V.device); sD = torch.zeros(len(allm), dtype=DT, device=V.device)
                for lab, cf in zip(labels, coefs):
                    (tB if lab[0] == "B" else sD)[allm.index(lab[1:])] = cf
                Uc, GUc = homogeneous_velocity_exact(R0 * fc["n"], tB, sD, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0, need_grad=True)
                Uc = Uc[0].detach(); GUc = GUc[0].detach()
                Gc_direct = (R0 ** (2 * alpha + 1)) * Uc
                curlc = torch.stack([GUc[:, 1, 2] - GUc[:, 2, 1], GUc[:, 2, 0] - GUc[:, 0, 2], GUc[:, 0, 1] - GUc[:, 1, 0]], -1)
                Gc_curl = (R0 ** (2 * alpha + 2)) * curlc
                kh = far_helicity_coefficients(fc, Gc=Gc, Gc_curl=Gc_curl)
                kh["G_carried_rebuild_rel"] = math.sqrt(max(ip(Gc_direct - Gc, Gc_direct - Gc), 0.0)) / max(nGc, 1e-300)
                out.update(kh)
            except Exception as e:
                out["K_H_error"] = repr(e)
        except Exception as e:
            out["carried_error"] = repr(e)
    return out


# ======================================================================================================================
# D6FP (2026-10-28): autograd-complete versions of first_correction and carried_patterns (no .item(), parameters as tensors) for the
# complete gradient of the self-consistent objective (SPEC G3, 7.1). The frozen functions above are unchanged and remain the production
# (lagged, detached) closure target; the graph versions reproduce their values (tested in validation/).
# ======================================================================================================================
def _eval_Y_grid_graph(y, modes, L):
    return eval_Y(y, modes, L)


def homogeneous_velocity_graph(y, tcoef, scoef, pT, pS, modes, Lmax, kappa, R0):
    """As homogeneous_velocity for a single coefficient set (tcoef, scoef: (Nq,) tensors or None) with pT, pS, kappa tensors, keeping
    the autograd graph to the coefficients and parameters (create_graph everywhere). Returns U (N, 3), GU (N, 3, 3) with GU[.., m, i] = d_m U_i."""
    yr = y.detach().clone().requires_grad_(True)
    U = 0
    if tcoef is not None:
        T = _potential(yr, tcoef, pT, modes, Lmax, kappa, R0)
        gT = torch.autograd.grad(T.sum(), yr, create_graph=True)[0]
        U = U - torch.cross(yr, gT, dim=-1)
    if scoef is not None:
        S = _potential(yr, scoef, pS, modes, Lmax, kappa, R0)
        gS = torch.autograd.grad(S.sum(), yr, create_graph=True)[0]
        H = torch.stack([torch.autograd.grad(gS[..., i].sum(), yr, create_graph=True)[0] for i in range(3)], -2)
        lap = H[..., 0, 0] + H[..., 1, 1] + H[..., 2, 2]
        gK = 2 * gS + torch.einsum('nik,nk->ni', H, yr)
        U = U + gK - yr * lap[..., None]
    GU = torch.stack([torch.autograd.grad(U[..., i].sum(), yr, create_graph=True)[0] for i in range(3)], -1)
    return U, GU


def first_correction_graph(prob, z, ntheta=None, nphi=None):
    """G[F] of the state's leading tail with the autograd graph to z (coefficients AND parameters) kept, on the EXACT route (production jets and
    double-double angular tables as constants; the coefficients and parameters enter through the tail amplitudes, the exponents and the twist,
    which carry the graph). D6FP 2026-10-29 (lead 00:33Z item 1 (a), remedy (a1)); the former eval_Y version is kept as
    first_correction_graph_evalY for cross-checks only. Returns dict(G (Na, 3), G_norm_t (0-dim tensor), F, n, w, grid)."""
    model = prob.model
    device = model.r.device
    aT, aS, c_l, omega = model.unpack(z)
    alpha = alpha_of(c_l); kappa = omega / c_l; R0 = model.R0
    L = model.L
    ntheta = ntheta or (2 * L + 10); nphi = nphi or (4 * L + 18)
    grid = AngularGrid(ntheta, nphi, device=device)
    n = grid.n; w = grid.w
    y = R0 * n
    t, s = prob.tail_amplitudes(aT, aS, c_l)
    modes = model.modes; Lmax = getattr(model, "L_ext", L)
    U, GU = homogeneous_velocity_exact(y, t, s, alpha, alpha - 1.0, modes, Lmax, kappa, R0)
    U = U[0]; GU = GU[0]
    Nvec = torch.einsum('am,ami->ai', U, GU)
    src = torch.einsum('aij,aji->a', GU, GU)
    Lq = 2 * L + 6
    pmodes = mode_list(Lq, model.m_parity, l_min=0)
    Yp = eval_solid(n, pmodes, Lq, 0, path="dd")[0]
    sig = (Yp * (w * src)[:, None]).sum(0) * R0 ** (2 * alpha + 2)
    lv = torch.tensor([float(l) for (l, m, tt) in pmodes], dtype=DT, device=device)
    mv = torch.tensor([float(m) for (l, m, tt) in pmodes], dtype=DT, device=device)
    lam_re = (-2 * alpha) * (1 - 2 * alpha) - (mv * kappa) ** 2 - lv * (lv + 1)
    lam_im = (-2 * alpha) * (mv * kappa) + (1 - 2 * alpha) * (mv * kappa)
    parts = []
    for i, (l, m, tt) in enumerate(pmodes):
        if tt == 1:
            continue
        if m == 0:
            parts.append((i, sig[i] / (-lam_re[i])))
        else:
            sc, ss = sig[i], sig[i + 1]
            den = lam_re[i] ** 2 + lam_im[i] ** 2
            qr = -(sc * lam_re[i] - ss * lam_im[i]) / den
            qi = -(-ss * lam_re[i] - sc * lam_im[i]) / den
            parts.append((i, qr)); parts.append((i + 1, -qi))
    idx = torch.tensor([p[0] for p in parts], dtype=torch.long, device=device)
    vals = torch.stack([p[1] for p in parts])
    qcoef = torch.zeros(len(pmodes), dtype=DT, device=device).index_put((idx,), vals)
    P0, gP = twisted_scalar_gradient_exact(y, qcoef, 2 * alpha, pmodes, Lq, kappa, R0)
    G = (R0 ** (2 * alpha + 1)) * (Nvec + gP)
    G_norm_t = ((G ** 2).sum(-1) * w).sum().clamp_min(1e-300).sqrt()
    F = (R0 ** alpha) * U
    return dict(G=G, G_norm_t=G_norm_t, F=F, n=n, w=w, grid=grid)


def first_correction_graph_evalY(prob, z, ntheta=None, nphi=None):
    """G[F] of the state's leading tail with the autograd graph to z (coefficients AND parameters) kept. Returns dict(G (Na, 3),
    G_norm_t (0-dim tensor), F, n, w)."""
    model = prob.model
    device = model.r.device
    aT, aS, c_l, omega = model.unpack(z)
    alpha = alpha_of(c_l); kappa = omega / c_l; R0 = model.R0
    L = model.L
    ntheta = ntheta or (2 * L + 10); nphi = nphi or (4 * L + 18)
    grid = AngularGrid(ntheta, nphi, device=device)
    n = grid.n; w = grid.w
    y = R0 * n
    t, s = prob.tail_amplitudes(aT, aS, c_l)
    modes = model.modes; Lmax = getattr(model, "L_ext", L)
    U, GU = homogeneous_velocity_graph(y, t, s, alpha, alpha - 1.0, modes, Lmax, kappa, R0)
    Nvec = torch.einsum('am,ami->ai', U, GU)
    src = torch.einsum('aij,aji->a', GU, GU)
    Lq = 2 * L + 6
    pmodes = mode_list(Lq, model.m_parity, l_min=0)
    Yp = eval_solid(n, pmodes, Lq, 0, path="dd")[0]
    sig = (Yp * (w * src)[:, None]).sum(0) * R0 ** (2 * alpha + 2)
    # pressure coefficients mode by mode in the twisted frame: q = sigma / (-lambda), lambda = (-2a + i m k)(1 - 2a + i m k) - l(l+1)
    lv = torch.tensor([float(l) for (l, m, tt) in pmodes], dtype=DT, device=device)
    mv = torch.tensor([float(m) for (l, m, tt) in pmodes], dtype=DT, device=device)
    idx_c = torch.tensor([i for i, (l, m, tt) in enumerate(pmodes) if tt == 0], dtype=torch.long, device=device)
    lam_re = (-2 * alpha) * (1 - 2 * alpha) - (mv * kappa) ** 2 - lv * (lv + 1)
    lam_im = (-2 * alpha) * (mv * kappa) + (1 - 2 * alpha) * (mv * kappa)
    # complex sigma = sig_c - i sig_s over the pair (cos index i, sin index i+1 for m > 0); q = sigma / (-lambda)
    qcoef = torch.zeros_like(sig)
    parts = []
    for i, (l, m, tt) in enumerate(pmodes):
        if tt == 1:
            continue
        if m == 0:
            parts.append((i, sig[i] / (-lam_re[i])))
        else:
            sc, ss = sig[i], sig[i + 1]
            # (sc - i ss) / (-(lr + i li)) = -(sc - i ss)(lr - i li) / (lr^2 + li^2)
            den = lam_re[i] ** 2 + lam_im[i] ** 2
            qr = -(sc * lam_re[i] - ss * lam_im[i]) / den
            qi = -(-ss * lam_re[i] - sc * lam_im[i]) / den
            parts.append((i, qr)); parts.append((i + 1, -qi))
    idx = torch.tensor([p[0] for p in parts], dtype=torch.long, device=device)
    vals = torch.stack([p[1] for p in parts])
    qcoef = torch.zeros(len(pmodes), dtype=DT, device=device).index_put((idx,), vals)
    yq = y.detach().clone().requires_grad_(True)
    P0 = _potential(yq, qcoef, 2 * alpha, pmodes, Lq, kappa, R0)
    gP = torch.autograd.grad(P0.sum(), yq, create_graph=True)[0]
    G = (R0 ** (2 * alpha + 1)) * (Nvec + gP)
    G_norm_t = ((G ** 2).sum(-1) * w).sum().clamp_min(1e-300).sqrt()
    F = (R0 ** alpha) * U
    return dict(G=G, G_norm_t=G_norm_t, F=F, n=n, w=w, grid=grid)


def carried_patterns_graph(model, c_l, omega, y, modes_B=None, modes_D=None):
    """UNUSED in production (D6FP 2026-10-29, lead 00:33Z): eval_Y route, kept for cross-checks only."""
    """As carried_patterns with c_l, omega tensors and the graph kept: (Na, 3, J) unit patterns including R0^(2alpha+1)."""
    alpha = alpha_of(c_l); kappa = omega / c_l; R0 = model.R0
    mB, mD, allm, Lmax = carried_mode_sets(model, modes_B, modes_D)
    cols = []
    if mB:
        for q in mB:
            E = torch.zeros(len(allm), dtype=DT, device=y.device); E[allm.index(q)] = 1.0
            VB, _ = homogeneous_velocity_graph(y, E, None, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0)
            cols.append(VB)
    if mD:
        for q in mD:
            E = torch.zeros(len(allm), dtype=DT, device=y.device); E[allm.index(q)] = 1.0
            VD, _ = homogeneous_velocity_graph(y, None, E, 2 * alpha + 1, 2 * alpha, allm, Lmax, kappa, R0)
            cols.append(VD)
    if not cols:
        return None
    return torch.stack(cols, -1) * (R0 ** (2 * alpha + 1))


# ======================================================================================================================
# D6FP (2026-10-28, lead 23:08Z item 4 / verifier 23:02Z, 23:07Z): the homogeneous twisted potentials of the closure (leading tail and its
# first nonlinear correction) evaluated through the PRODUCTION machinery: radial jets (rho-derivatives of r^-p and of the twist angle
# chi0 = kappa log(r/R0), exact to the truncation order), the twist applied to the (cos, sin) pairs, the exact double-double solid-harmonic
# tables (eval_solid path "dd", nderiv 2) and Model.scalar_points / Model._assemble. No autograd through a float64 recurrence; the only
# rounding is that of the final float64 assembly. Replaces eval_Y / homogeneous_velocity in first_correction and carried_patterns.
# ======================================================================================================================
def _twisted_homogeneous_jets(rho, coef, p, l_arr, kappa, R0, m_arr, partner, tw_sign, K):
    """Radial derivative arrays g[n] (n <= K) of the twisted homogeneous radial functions: for mode q (degree l) the untwisted radial factor
    is r^-p r^-l (so that r^-p P_q(n) = r^-p r^-l P_q(y)); twist: pairs rotated by m chi0(r), chi0 = (kappa/2) log(rho / R0^2).
    coef: (Nq,) amplitudes. Returns (K+1, Np, Nq) arrays as Model.radial_derivs does (values and rho-derivatives, with the twist applied)."""
    from ..bases import jets
    import math as _m
    rho = torch.as_tensor(rho, dtype=DT)
    Np = rho.numel(); Nq = coef.numel()
    # f_q(rho) = rho^(-(p + l)/2) coef_q
    g = torch.zeros(K + 1, Np, Nq, dtype=DT, device=rho.device)
    for n in range(K + 1):
        pass
    ex = -(p + l_arr) / 2.0                                                    # (Nq,) exponents
    # Taylor coefficients of rho^ex: C(ex, n) rho^(ex - n); derivatives n! C(ex, n) rho^(ex-n)
    for n in range(K + 1):
        c = torch.ones_like(ex)
        for k in range(n):
            c = c * (ex - k)                                                    # falling factorial ex (ex-1) ... (ex-n+1) = n! C(ex, n)
        g[n] = (c[None, :] * rho[:, None] ** (ex[None, :] - n)) * coef[None, :]
    # twist tables for chi0 = (kappa/2) (log rho - log R0^2): jets of log rho are those of affine_log with u = rho
    lg = jets.affine_log(rho, K) - jets.const(torch.log(torch.as_tensor(R0 * R0, dtype=DT, device=rho.device)), jets.affine_log(rho, K))
    chi = (kappa / 2.0) * lg
    Mmax = int(m_arr.max()) if m_arr.numel() else 0
    Cs, Ss = [], []
    for m in range(Mmax + 1):
        c_, s_ = jets.cos_sin(m * chi)
        Cs.append(jets.to_derivs(c_)); Ss.append(jets.to_derivs(s_))
    C = torch.stack(Cs, 0); S = torch.stack(Ss, 0)                              # (Mmax+1, K+1, Np)
    gp = g[:, :, partner]
    Cm = C[m_arr].permute(1, 2, 0); Sm = S[m_arr].permute(1, 2, 0) * tw_sign[None, None, :]
    out = []
    for n in range(K + 1):
        t = 0
        for k in range(n + 1):
            t = t + _m.comb(n, k) * (g[k] * Cm[n - k] + gp[k] * Sm[n - k])
        out.append(t)
    return torch.stack(out, 0)


class _HomogeneousModel:
    """Minimal Model-like object for the assembly of twisted homogeneous potentials on a given mode list (exact dd angular tables at the points)."""
    def __init__(self, modes, Lmax, device):
        from ..bases.solid_harmonics import eval_solid
        self.modes = modes; self.L_ext = Lmax
        self.l_arr = torch.tensor([float(l) for (l, m, t) in modes], dtype=DT, device=device)
        self.m_arr = torch.tensor([m for (l, m, t) in modes], dtype=torch.long, device=device)
        partner, sign = [], []
        for q, (l, m, t) in enumerate(modes):
            if m == 0:
                partner.append(q); sign.append(0.0)
            elif t == 0:
                partner.append(q + 1); sign.append(1.0)
            else:
                partner.append(q - 1); sign.append(-1.0)
        self.partner = torch.tensor(partner, dtype=torch.long, device=device); self.tw_sign = torch.tensor(sign, dtype=DT, device=device)
        self.eps = torch.zeros(3, 3, 3, dtype=DT, device=device)
        for (i, j, k, s) in [(0, 1, 2, 1), (1, 2, 0, 1), (2, 0, 1, 1), (0, 2, 1, -1), (2, 1, 0, -1), (1, 0, 2, -1)]:
            self.eps[i, j, k] = s
        self._eval_solid = eval_solid

    def tables(self, pts):
        return self._eval_solid(pts, self.modes, self.L_ext, 2, path="dd")


def homogeneous_velocity_exact(y, tcoef, scoef, pT, pS, modes, Lmax, kappa, R0, need_grad=True):
    """U and GU (GU[.., m, i] = d_m U_i) at points y (N, 3) of U = curl(T y) + curl curl(S y), T = r^-pT sum_q t_q P_q(R n), S = r^-pS sum_q s_q P_q(R n),
    R the rotation by chi0(r) = kappa log(r/R0); tcoef, scoef (Nq,) or (Nq, J). Returns (U (J, N, 3), GU (J, N, 3, 3)); batched over J by a loop
    (the assembly is cheap). Exact angular tables, analytic radial jets."""
    from ..equations.fields import Model
    device = y.device
    hm = _HomogeneousModel(modes, Lmax, device)
    P0, P1, P2 = hm.tables(y)
    rho = (y ** 2).sum(-1)
    tcoef2 = None if tcoef is None else (tcoef[:, None] if tcoef.dim() == 1 else tcoef)
    scoef2 = None if scoef is None else (scoef[:, None] if scoef.dim() == 1 else scoef)
    J = (tcoef2 if tcoef2 is not None else scoef2).shape[1]
    Us, GUs = [], []
    zero_coef = torch.zeros(len(modes), dtype=DT, device=device)
    for j in range(J):
        tc = zero_coef if tcoef2 is None else tcoef2[:, j]; sc = zero_coef if scoef2 is None else scoef2[:, j]
        gT = _twisted_homogeneous_jets(rho, tc, torch.as_tensor(pT, dtype=DT, device=device), hm.l_arr, torch.as_tensor(kappa, dtype=DT, device=device), R0, hm.m_arr, hm.partner, hm.tw_sign, 4)
        gS = _twisted_homogeneous_jets(rho, sc, torch.as_tensor(pS, dtype=DT, device=device), hm.l_arr, torch.as_tensor(kappa, dtype=DT, device=device), R0, hm.m_arr, hm.partner, hm.tw_sign, 4)
        # reuse Model.scalar_sets / scalar_points / _assemble through a light proxy
        class _P:
            pass
        proxy = _P(); proxy._pt_cache = (P0, P1, P2); proxy.l_arr = hm.l_arr; proxy.eps = hm.eps
        proxy.scalar_sets = Model.scalar_sets; proxy.scalar_points = lambda h, pts, need_hess=True, _p=proxy: Model.scalar_points(_p, h, pts, need_hess)
        out = Model._assemble(proxy, gT, gS, rho, None, None, False, grid=False, pts=y)
        Us.append(out["U"].T); GUs.append(out["GU"].permute(2, 0, 1))        # (N, 3), (N, 3, 3)
    U = torch.stack(Us, 0); GU = torch.stack(GUs, 0)
    return (U, GU) if need_grad else (U, None)


def twisted_scalar_gradient_exact(y, coef, p, modes, Lmax, kappa, R0):
    """gradient at y (N, 3) of the twisted homogeneous scalar Q = r^-p sum_q coef_q P_q(R n) (the first-correction pressure): exact tables + jets."""
    from ..equations.fields import Model
    device = y.device
    hm = _HomogeneousModel(modes, Lmax, device)
    P0, P1, P2 = hm.tables(y)
    rho = (y ** 2).sum(-1)
    g = _twisted_homogeneous_jets(rho, coef, torch.as_tensor(p, dtype=DT, device=device), hm.l_arr, torch.as_tensor(kappa, dtype=DT, device=device), R0, hm.m_arr, hm.partner, hm.tw_sign, 2)
    class _P:
        pass
    proxy = _P(); proxy._pt_cache = (P0, P1, P2)
    f, grad, _ = Model.scalar_points(proxy, (g[0], g[1], g[2]), y, False)
    return f, grad.T                                                           # (N,), (N, 3)


def homogeneous_patterns_exact(y, E_T, E_S, pT, pS, modes, Lmax, kappa, R0, chunk=32):
    """Batched exact evaluation of U (J, N, 3) for J coefficient columns E_T, E_S (Nq, J) (either may be None): the velocities of the twisted
    homogeneous potentials T = r^-pT sum_q E_T[q, j] P_q(R n), S likewise, by jets + double-double tables, with the column axis carried through
    the assembly (no per-column loop). Used for the carried patterns (J = 233 unit columns at every trial point)."""
    import math as _m
    from ..bases import jets
    device = y.device
    hm = _HomogeneousModel(modes, Lmax, device)
    P0, P1, P2 = hm.tables(y)                                                  # (N, Nq), (3, N, Nq), (3, 3, N, Nq)
    N = y.shape[0]; Nq = len(modes)
    rho = (y ** 2).sum(-1); yv = y.T                                           # (N,), (3, N)
    J = (E_T if E_T is not None else E_S).shape[1]
    l_arr, m_arr, partner, sign, eps = hm.l_arr, hm.m_arr, hm.partner, hm.tw_sign, hm.eps
    K = 4
    kap = torch.as_tensor(kappa, dtype=DT, device=device)
    lg = jets.affine_log(rho, K) - jets.const(torch.log(torch.as_tensor(R0 * R0, dtype=DT, device=device)), jets.affine_log(rho, K))
    chi = (kap / 2.0) * lg
    Mmax = int(m_arr.max()) if m_arr.numel() else 0
    Cs, Ss = [], []
    for m in range(Mmax + 1):
        c_, s_ = jets.cos_sin(m * chi); Cs.append(jets.to_derivs(c_)); Ss.append(jets.to_derivs(s_))
    C = torch.stack(Cs, 0)[m_arr].permute(1, 2, 0); S = torch.stack(Ss, 0)[m_arr].permute(1, 2, 0) * sign[None, None, :]     # (K+1, N, Nq)
    def radial(p):
        ex = -(torch.as_tensor(p, dtype=DT, device=device) + l_arr) / 2.0
        out = []
        for n in range(K + 1):
            c = torch.ones_like(ex)
            for k in range(n):
                c = c * (ex - k)
            out.append(c[None, :] * rho[:, None] ** (ex[None, :] - n))
        return torch.stack(out, 0)                                             # (K+1, N, Nq) untwisted radial jets of r^-p r^-l
    rT = radial(pT) if E_T is not None else None; rS = radial(pS) if E_S is not None else None
    def twisted(rad, E):
        """(K+1, N, Nq, Jc) twisted jets for coefficient columns E (Nq, Jc): g_k = rad_k * E, partner mixing by C, S."""
        g = rad[..., None] * E[None, None, :, :]                                # (K+1, N, Nq, Jc)
        gp = g[:, :, partner, :]
        out = []
        for n in range(K + 1):
            t = 0
            for k in range(n + 1):
                t = t + _m.comb(n, k) * (g[k] * C[n - k][..., None] + gp[k] * S[n - k][..., None])
            out.append(t)
        return torch.stack(out, 0)
    def scalar_sets(gT, gS):
        l = l_arr[None, :, None]; r_ = rho[:, None, None]
        T = (gT[0], gT[1], gT[2])
        Kf = ((l + 1) * gS[0] + 2 * r_ * gS[1], (l + 3) * gS[1] + 2 * r_ * gS[2], (l + 5) * gS[2] + 2 * r_ * gS[3])
        Df = ((6 + 4 * l) * gS[1] + 4 * r_ * gS[2], (10 + 4 * l) * gS[2] + 4 * r_ * gS[3], (14 + 4 * l) * gS[3] + 4 * r_ * gS[4])
        return T, Kf, Df
    def ev(h, need_hess=True):
        h0, h1, h2 = h
        f = torch.einsum('pqj,pq->pj', h0, P0)
        grad = 2 * torch.einsum('pqj,pq->pj', h1, P0)[None] * yv[:, :, None] + torch.einsum('pqj,ipq->ipj', h0, P1)
        if not need_hess:
            return f, grad, None
        eye = torch.eye(3, dtype=DT, device=device)
        hess = 4 * torch.einsum('pqj,pq->pj', h2, P0)[None, None] * yv[:, None, :, None] * yv[None, :, :, None]
        H1P0 = torch.einsum('pqj,pq->pj', h1, P0); H1P1 = torch.einsum('pqj,ipq->ipj', h1, P1)
        hess = hess + 2 * (eye[:, :, None, None] * H1P0[None, None] + yv[:, None, :, None] * H1P1[None, :] + yv[None, :, :, None] * H1P1[:, None])
        hess = hess + torch.einsum('pqj,ikpq->ikpj', h0, P2)
        return f, grad, hess
    Us = []
    zeros_g = None
    for a0 in range(0, J, chunk):
        a1 = min(J, a0 + chunk); Jc = a1 - a0
        gT = twisted(rT, E_T[:, a0:a1]) if E_T is not None else torch.zeros(K + 1, N, Nq, Jc, dtype=DT, device=device)
        gS = twisted(rS, E_S[:, a0:a1]) if E_S is not None else torch.zeros(K + 1, N, Nq, Jc, dtype=DT, device=device)
        T, Kf, Df = scalar_sets(gT, gS)
        _, gT_, _ = ev(T, False); _, gK, _ = ev(Kf, False); dD, _, _ = ev(Df, False)
        yvj = yv[:, :, None].expand(3, N, Jc)
        U = -torch.einsum('ijk,jpc,kpc->ipc', eps, yvj, gT_) + gK - yvj * dD[None]        # (3, N, Jc)
        Us.append(U.permute(2, 1, 0))                                                        # (Jc, N, 3)
    return torch.cat(Us, 0)
