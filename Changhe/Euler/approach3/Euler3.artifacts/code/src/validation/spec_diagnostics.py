"""Diagnostics of SPEC v1 sections 7.1 to 7.5 (5-term frame-invariant split, dyadic shells, nonlinear-balance
ratios, pointwise ratios, A_u, A_Om, non-axisymmetric content N_k and e_k, nontriviality guards, tail onset).
Shell RMS uses the normalized volume measure inside each shell (radial weights r^2 dr from node spacing, angular
Gauss weights). Shells are absolute dyadic [2^j, 2^(j+1)) that contain radial nodes, plus the core ball below them."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import alpha_of, Model
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver
DT = torch.float64
import os
# 2026-10-25T21:58Z (battery memory, lead 21:03Z): the ray-integral pressure check evaluates nrad x ntheta x nphi = 491 520 scattered points per
# target point in chunks; each chunk holds P0/P1/P2 solid-harmonic arrays (13 x chunk x Nq) and radial derivative arrays (10 x chunk x Nq) over
# the union mode set (Nq 195 at L8-ext, 283 at L10-ext), which made this item the battery peak (44.3 GB at L8-ext, 73.4 GB at L10-ext against
# at most 10 GB for every other item). Per-point values are the same mathematical quantity for every chunk size (no reduction over the points of a
# chunk; astra referee 23:20Z), but on a GPU different batch shapes may select different kernels and summation orders, so the agreement is at rounding
# level without a universal bound: the comparison of the two paths on the production state (scripts/compare_ray_chunk.py, 1e-12 relative with an
# absolute floor near zero) is the test, not this comment. CPU at L4: 1303 compared numeric scalars with zero numerical difference.
RAY_CHUNK = int(os.environ.get("E3_RAY_CHUNK", "25000"))      # 200000 before 2026-10-25T21:58Z
def _cuda_peak_GB(dev):
    try:
        return round(torch.cuda.max_memory_allocated(dev) / 2**30, 2) if (dev is not None and str(dev) != "cpu" and torch.cuda.is_available()) else None
    except Exception:
        return None

def eigvalsh_chunked(A, chunk=8192):
    """Batched symmetric eigenvalues in chunks (cuSOLVER batched syev fails for very large batches)."""
    shp = A.shape[:-2]
    flat = A.reshape(-1, A.shape[-2], A.shape[-1])
    out = torch.cat([torch.linalg.eigvalsh(flat[i:i + chunk]) for i in range(0, flat.shape[0], chunk)], 0)
    return out.reshape(*shp, A.shape[-1])



def _pressure(prob, c_l=None, omega=None):
    """Pressure solver matching the candidate's (c_l, omega) (rebuilt when they differ from a cached one)."""
    c_l = prob.model.c_l0 if c_l is None else float(c_l); omega = prob.model.omega0 if omega is None else float(omega)
    if prob.pressure is not None and abs(prob.pressure.c_l - c_l) < 1e-12 and abs(prob.pressure.omega - omega) < 1e-12:
        return prob.pressure
    ps = getattr(prob, "_ps_diag", None)
    if ps is None or abs(ps.c_l - c_l) > 1e-12 or abs(ps.omega - omega) > 1e-12:
        prob._ps_diag = PressureSolver(prob.model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)
    return prob._ps_diag


def five_term_split(F, gradP):
    U, GU, c_l, omega = F['U'], F['GU'], F['c_l'], F['omega']
    yv = res.yvec(F['y']); Jy = res.Jvec(yv)
    T1 = (1 - c_l) * U
    T2 = c_l * torch.einsum('m...,mi...->i...', yv, GU)
    T3 = omega * (res.Jvec(U) - torch.einsum('m...,mi...->i...', Jy, GU))
    T4 = torch.einsum('m...,mi...->i...', U, GU)
    T5 = gradP
    return [T1, T2, T3, T4, T5]


def vorticity_split(F):
    U, GU, Om, GOm, c_l, omega = F['U'], F['GU'], F['Om'], F['GOm'], F['c_l'], F['omega']
    yv = res.yvec(F['y']); Jy = res.Jvec(yv)
    V1 = Om
    V2 = c_l * torch.einsum('m...,mi...->i...', yv, GOm)
    V3 = omega * (res.Jvec(Om) - torch.einsum('m...,mi...->i...', Jy, GOm))
    V4 = torch.einsum('m...,mi...->i...', U, GOm)
    V5 = -torch.einsum('m...,mi...->i...', Om, GU)
    return [V1, V2, V3, V4, V5]


class Shells:
    def __init__(self, model):
        r = model.r.cpu().numpy()
        dr = np.empty_like(r)
        dr[1:-1] = 0.5 * (r[2:] - r[:-2]); dr[0] = 0.5 * (r[1] + r[0]); dr[-1] = r[-1] - r[-2]
        self.wvol = torch.tensor(r ** 2 * dr, dtype=torch.float64, device=model.r.device)
        j = np.floor(np.log2(r)).astype(int)
        js = sorted(set(j.tolist()))
        self.ids = np.array([js.index(v) for v in j])
        self.edges = [(2.0 ** v, 2.0 ** (v + 1)) for v in js]
        self.n = len(js)
        self.masks = [torch.tensor(self.ids == k, device=model.r.device) for k in range(self.n)]
        self.rmid = [math.sqrt(a * b) for (a, b) in self.edges]
        self.w_ang = model.grid.w / (4 * math.pi)

    def rms(self, X):
        """X: (3,Nr,Na) or (Nr,Na). Returns list of shell RMS (normalized volume measure)."""
        sq = (X ** 2).sum(0) if X.dim() == 3 else X ** 2
        per_node = (sq * self.w_ang[None, :]).sum(1)
        out = []
        for m in self.masks:
            w = self.wvol[m]
            out.append(((per_node[m] * w).sum() / w.sum()).sqrt().item())
        return out

    def maxabs(self, X):
        a = X.norm(dim=0) if X.dim() == 3 else X.abs()
        return [a[m].max().item() for m in self.masks]


def leading_tail_field(prob, aT, aS, c_l, omega, r, grid):
    """Exact homogeneous leading tail U_0 = r^-alpha F(theta, chi), chi = phi + (omega/c_l) log(r/R0), in Cartesian
    components on radii r (Nr,) x angular grid: toroidal t_q r^-alpha (grad_S Y_q x n) [curl(T y) = grad T x y], poloidal
    s_q r^-alpha [ l(l+1) Y_q n + (2-alpha) grad_S Y_q + (omega/c_l) grad_S d_chi Y_q ]. Twisted pairs rotated by m chi_0(r)."""
    model = prob.model
    alpha = alpha_of(c_l)
    t, s = prob.tail_amplitudes(aT, aS, c_l)                   # (Nq,)
    from ..bases.solid_harmonics import angular_matrices
    A0, A1, _ = angular_matrices(grid, model.modes, getattr(model, "L_ext", model.L), 1)  # (Na,Nq), (3,Na,Nq) at unit radius on this grid
    n = grid.n.T                                                 # (3, Na)
    l = model.l_arr; m = model.m_arr.to(DT)
    gradS = A1 - l[None, None, :] * n[:, :, None] * A0[None, :, :]     # surface gradient of Y_q (3, Na, Nq)
    tor = torch.stack([gradS[1] * n[2][:, None] - gradS[2] * n[1][:, None], gradS[2] * n[0][:, None] - gradS[0] * n[2][:, None],
                       gradS[0] * n[1][:, None] - gradS[1] * n[0][:, None]], 0)     # grad_S Y x n  (3, Na, Nq)
    polo = (l * (l + 1))[None, None, :] * n[:, :, None] * A0[None] + (2 - alpha) * gradS
    # d_chi Y_q: cos mode -> -m sin mode (partner), sin mode -> +m cos mode (partner)
    polo_dchi = (omega / c_l) * (-model.tw_sign[None, None, :]) * m[None, None, :] * gradS[:, :, model.partner]
    # radial phase: rotate pairs by m chi0(r), chi0 = (omega/c_l) log(r/R0): field = c cos(m(phi+chi0)) + s sin(m(phi+chi0))
    chi0 = (omega / c_l) * torch.log(r / model.R0)                                   # (Nr,)
    cm = torch.cos(m[None, :] * chi0[:, None]); sm = torch.sin(m[None, :] * chi0[:, None])   # (Nr, Nq)
    def rot(coef):   # coef (Nq,) -> rotated per radius (Nr, Nq): c' = c cos + s_partner sin ; s' = -c_partner sin + s cos
        cp = coef[model.partner]
        return coef[None, :] * cm + model.tw_sign[None, :] * cp * sm
    tq = rot(t); sq = rot(s)                                                          # (Nr, Nq)
    ralpha = r ** (-alpha)
    U0 = torch.einsum('jq,iaq->ija', tq, tor) + torch.einsum('jq,iaq->ija', sq, polo + polo_dchi)
    return U0 * ralpha[None, :, None]


def spec_diagnostics(prob, z, holdout=None, extras=True):
    """extras=False skips the origin Taylor ratio, the fine-grid Z/I integrals and the ray-integral pressure check (used for the
    second shell family, where only the shell ratios are needed).
    holdout: optional HoldoutGrid (src/validation/holdout.py). With it, all fields are evaluated on the holdout
    radii/angles (never used in training), the pressure is the Green solution of the source sampled on the training
    nodes and evaluated at the holdout points, and shells use exact normalized-volume Gauss quadrature. Without it,
    the training grid and node-spacing weights are used (labelled grid='training')."""
    model = prob.model
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega); alpha = alpha_of(c_lf)
    if holdout is None:
        F = model.fields_grid(z, need_vort=True)
        ps = _pressure(prob, c_lf, omf)
        f = res.pressure_source(F['GU'])
        P, gradP, Plm, dPlm = ps.solve(f)
        sh = Shells(model); emodel = model; grid_label = "training"
    else:
        emodel = holdout.model
        F = emodel.fields_grid(z, need_vort=True)
        ps = holdout.pressure_solver(model, c_lf, omf) if not hasattr(holdout, "_ps") or abs(holdout._ps.c_l - c_lf) > 1e-12 or abs(holdout._ps.omega - omf) > 1e-12 else holdout._ps
        holdout._ps = ps
        f = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])     # source on training nodes
        P, gradP, Plm, dPlm = ps.solve(f)
        sh = holdout; grid_label = "holdout"
    T = five_term_split(F, gradP); Ru = sum(T)
    V = vorticity_split(F); ROm = sum(V)
    U, GU, Om = F['U'], F['GU'], F['Om']
    rmsU = sh.rms(U); rmsDU = sh.rms(GU.reshape(9, *GU.shape[2:]))
    rmsT = [sh.rms(t) for t in T]; rmsRu = sh.rms(Ru); maxRu = sh.maxabs(Ru)
    rmsV = [sh.rms(v) for v in V]; rmsROm = sh.rms(ROm); maxROm = sh.maxabs(ROm)
    divU = res.divergence(GU); rmsdiv = sh.rms(divU)
    nsh = sh.n
    den5 = [sum(rmsT[i][k] for i in range(5)) for k in range(nsh)]
    denV = [sum(rmsV[i][k] for i in range(5)) for k in range(nsh)]
    dmax = max(den5)
    flags = []
    for k in range(nsh):
        fl = []
        if den5[k] < 1e-14 * dmax: fl.append("tiny_terms")
        if 0 < k < nsh - 1 and den5[k] * 1e3 < min(den5[k - 1], den5[k + 1]): fl.append("1e3_below_neighbours")
        flags.append(",".join(fl))
    def ratio(num, den):
        return [None if d == 0 else n / d for n, d in zip(num, den)]
    rho_u = ratio(rmsRu, den5)
    rho_nl = ratio(rmsRu, [rmsT[3][k] + rmsT[4][k] for k in range(nsh)])
    # SPEC v1.14 (lead 23:19Z, d29): rho_lin = RMS(R_u)/(RMS T1 + RMS T2 + RMS T3), rho_sp = max(rho_lin, rho_nl): a core whose large
    # nonlinear terms T4, T5 cancel each other (near-steady Euler) has small rho_u only through its denominator; rho_lin exposes it
    rho_lin = ratio(rmsRu, [rmsT[0][k] + rmsT[1][k] + rmsT[2][k] for k in range(nsh)])
    rho_sp = [None if (a is None and b is None) else max(v for v in (a, b) if v is not None) for a, b in zip(rho_lin, rho_nl)]
    # SPEC v1.15 7.2 Gram data per shell: a = RMS(L), b = RMS(N), gamma = <L, N>/(a b) with L = T1+T2+T3, N = T4+T5; check a^2 + b^2 + 2 a b gamma = RMS(R_u)^2
    Lsum = T[0] + T[1] + T[2]; Nsum = T[3] + T[4]
    gram_a = sh.rms(Lsum); gram_b = sh.rms(Nsum)
    LN = (Lsum * Nsum).sum(0)                                      # pointwise <L, N>
    per_node_LN = (LN * sh.w_ang[None, :]).sum(1)
    gram_ln = [((per_node_LN[m_] * sh.w_vol[m_]).sum() / sh.w_vol[m_].sum()).item() for m_ in sh.masks] if hasattr(sh, "w_vol") else [float("nan")] * nsh
    gram_gamma = [None if (a_ == 0 or b_ == 0 or ln != ln) else ln / (a_ * b_) for a_, b_, ln in zip(gram_a, gram_b, gram_ln)]
    gram_check = [None if g is None else abs(a_ ** 2 + b_ ** 2 + 2 * ln - r_ ** 2) / max(r_ ** 2, 1e-300) for a_, b_, ln, r_, g in zip(gram_a, gram_b, gram_ln, rmsRu, gram_gamma)]
    # d30 ratios (SPEC v1.15 7.2): ||R_u||_2 / ||(1-c_l) U||_2 over |y| < 1 and ||R_Omega||_2 / ||Omega||_2 over all shells (L2 norms, i.e. shell
    # L2^2 = volume_k RMS_k^2 with volume_k = (4 pi/3)(r_hi^3 - r_lo^3); the origin ball counts with its full volume)
    vol = [(b_ ** 3 - a_ ** 3) for (a_, b_) in sh.edges]
    inside = [k for k in range(nsh) if sh.edges[k][1] <= 1.0 + 1e-12]
    rmsOm = sh.rms(Om)
    def l2(rms_list, ks):
        return math.sqrt(sum(vol[k] * rms_list[k] ** 2 for k in ks))
    d30_Ru_over_T1_r1 = (l2(rmsRu, inside) / max(l2(rmsT[0], inside), 1e-300)) if inside else None
    d30_ROm_over_Om = l2(rmsROm, range(nsh)) / max(l2(rmsOm, range(nsh)), 1e-300)
    # SPEC v1.19 single-term ratios: sigma_u(k) = RMS_k(R_u)/RMS_k((1-c_l)U) per shell (T1-only denominator flag when RMS_k(T1) is tiny),
    # sigma_u^max over all shells and over |y| < 1; sigma_Om = ||R_Omega||_2/||Omega||_2 over all resolved shells (= d30_ROm_over_Om)
    sigma_u = ratio(rmsRu, rmsT[0])
    T1max = max(rmsT[0]) if rmsT[0] else 0.0
    sigma_u_flag = [bool(rmsT[0][k] < 1e-14 * T1max) for k in range(nsh)]
    # v1.17 items: a_max = max_k (1 + r_k)^(2alpha+1) RMS_k(R_u) (origin ball r_k = 0), origin-ball U_rms and B = RMS T4 + RMS T5
    rk_a = [0.0 if sh.edges[k][0] == 0.0 else sh.rmid[k] for k in range(nsh)]
    a_fixed = [(1 + rk_a[k]) ** (2 * alpha + 1) * rmsRu[k] for k in range(nsh)]
    origin = dict(U_rms=rmsU[0], B_nl_sum=rmsT[3][0] + rmsT[4][0], L_lin_sum=rmsT[0][0] + rmsT[1][0] + rmsT[2][0], R_u_rms=rmsRu[0], edges=sh.edges[0])
    # lead 02:02Z 2(b)/(c) and 01:52Z item 2: gradient scale RMS_k T4 / RMS_k U on the origin ball and the first two shells; ||U||_L2(|y|<1);
    # helicity integrals on |y| < 1 and 1 <= |y| < 8 (signed); core radius where the shell U_rms falls to half the origin-ball value;
    # axial-to-planar vorticity ratio on |y| < r_core_half; dominant azimuthal order of the core (|y| < r_core_half) and of the tail (leading F)
    grad_scale = [rmsT[3][k] / max(rmsU[k], 1e-300) for k in range(min(3, nsh))]
    vol_fac = 4.0 * math.pi / 3.0
    U_L2_r1 = math.sqrt(sum(vol_fac * vol[k] * rmsU[k] ** 2 for k in inside)) if inside else None
    hel_node = ((U * Om).sum(0) * sh.w_ang[None, :]).sum(1)                      # sphere mean of U.Omega per node
    hel_shell = [((hel_node[m_] * sh.w_vol[m_]).sum() / sh.w_vol[m_].sum()).item() for m_ in sh.masks] if hasattr(sh, "w_vol") else [float("nan")] * nsh
    hel_r1 = sum(vol_fac * vol[k] * hel_shell[k] for k in inside) if inside else None
    mid = [k for k in range(nsh) if sh.edges[k][0] >= 1.0 - 1e-12 and sh.edges[k][1] <= 8.0 + 1e-12]
    hel_1_8 = sum(vol_fac * vol[k] * hel_shell[k] for k in mid) if mid else None
    r_core_half = None
    for k in range(nsh):
        if rmsU[k] < 0.5 * rmsU[0]:
            r_core_half = sh.edges[k][0]; break
    core_mask = emodel.r < (r_core_half if r_core_half else sh.edges[0][1])
    if core_mask.any():
        Omc = Om[:, core_mask, :]; wc = sh.w_ang[None, :]
        ax = ((Omc[2] ** 2) * wc).sum().item(); pl = ((Omc[0] ** 2 + Omc[1] ** 2) * wc).sum().item()
        axial_planar = math.sqrt(ax / max(pl, 1e-300))
    else:
        axial_planar = None
    structure = dict(grad_scale_T4_over_U=grad_scale, grad_scale_shells=sh.edges[:len(grad_scale)], U_L2_r_lt_1=U_L2_r1, helicity_r_lt_1=hel_r1, helicity_1_8=hel_1_8,
                     r_core_half=r_core_half, axial_to_planar_vorticity=axial_planar, core_dominant_m=None, core_m_energy_fractions=None)
    pi_u = ratio(maxRu, den5)
    pi_nl = ratio(maxRu, [rmsT[3][k] + rmsT[4][k] for k in range(nsh)])
    peak = [None if (a is None or b is None or b == 0) else a / b for a, b in zip(pi_u, rho_u)]
    rho_Om = ratio(rmsROm, denV)
    rho_Om_nl = ratio(rmsROm, [rmsV[3][k] + rmsV[4][k] for k in range(nsh)])
    rho_div = ratio(rmsdiv, rmsDU)
    # non-axisymmetric content: N_k = RMS(T3)/(|omega| RMS(U)); e_k = RMS(U - <U>_phi)^2 / RMS(U)^2 (spherical comps)
    N_k = [None if (omf == 0 or u == 0) else t3 / (abs(omf) * u) for t3, u in zip(rmsT[2], rmsU)]
    er, eth, eph = emodel.grid.sph_basis()
    Usph = torch.stack([torch.einsum('ija,ai->ja', U, e) for e in (er, eth, eph)], 0)   # (3,Nr,Na) spherical components
    Us = Usph.reshape(3, emodel.Nr, emodel.ntheta, emodel.nphi)
    Umean = Us.mean(-1, keepdim=True).expand_as(Us)
    dev = (Us - Umean).reshape(3, emodel.Nr, emodel.Na)
    rms_dev = sh.rms(dev)
    if core_mask.any():      # dominant azimuthal order of the core from the spherical components on |y| < r_core_half (lead 02:02Z 2(c))
        Fm = torch.fft.rfft(Us[:, core_mask, :, :], dim=-1); em_c = (Fm.abs() ** 2).sum(dim=(0, 1, 2)); em_c[1:] *= 2.0
        structure["core_dominant_m"] = int(em_c.argmax().item()); structure["core_m_energy_fractions"] = (em_c / em_c.sum().clamp_min(1e-300)).tolist()[: min(7, em_c.numel())]
    e_k = [None if u == 0 else (d / u) ** 2 for d, u in zip(rms_dev, rmsU)]
    # core radius and vorticity profile
    sphere_mean_Om2 = ((Om ** 2).sum(0) * sh.w_ang[None, :]).sum(1)
    score = emodel.r ** 3 * sphere_mean_Om2
    jc = score.argmax().item(); r_core = emodel.r[jc].item()
    # enstrophy per log radius: 10% and 90% radii
    ens = (sphere_mean_Om2 * emodel.r ** 3).cpu().numpy()        # dE/dlog r ~ r^3 <|Om|^2>
    cum = np.cumsum(ens * np.gradient(np.log(emodel.r.cpu().numpy()))); cum /= max(cum[-1], 1e-300)
    rr = emodel.r.cpu().numpy()
    r10 = float(rr[np.searchsorted(cum, 0.1)]) if cum[-1] > 0 else None; r90 = float(rr[min(np.searchsorted(cum, 0.9), len(rr) - 1)]) if cum[-1] > 0 else None
    # tail onset: compare U with the exact homogeneous leading tail r^-alpha F(theta, phi + (omega/c_l) log(r/R0))
    U0 = leading_tail_field(prob, aT, aS, c_l, omega, emodel.r, emodel.grid)
    EF = (((U - U0) ** 2).sum(0) * sh.w_ang[None, :]).sum(1).sqrt() / ((U0 ** 2).sum(0) * sh.w_ang[None, :]).sum(1).sqrt().clamp_min(1e-300)
    EF = EF.cpu().numpy()
    ok = EF <= 0.1
    r_tail = None
    for j in range(len(rr)):
        if ok[j:].all():
            r_tail = float(rr[j]); break
    # vorticity maximum identity
    absOm = Om.norm(dim=0); idx = absOm.flatten().argmax().item(); jm, am = divmod(idx, emodel.Na)
    S = 0.5 * (GU[:, :, jm, am] + GU[:, :, jm, am].T); om = Om[:, jm, am]
    strain_ratio = (om @ (S @ om) / max((om @ om).item(), 1e-300)).item()
    lam_max = torch.linalg.eigvalsh(S)[-1].item()
    # A_u, A_Om (v1)
    rk = np.array(sh.rmid)
    Lam_u = max((1 + rk[k]) ** (2 * alpha + 1) * rmsU[k] ** 2 / rk[k] for k in range(nsh))
    Lam_Om = max((1 + rk[k]) ** (2 * alpha + 2) * rmsU[k] ** 2 / rk[k] ** 2 for k in range(nsh))
    A_u = max((1 + rk[k]) ** (2 * alpha + 1) * rmsRu[k] for k in range(nsh)) / max(Lam_u, 1e-300)
    A_Om = max((1 + rk[k]) ** (2 * alpha + 2) * rmsROm[k] for k in range(nsh)) / max(Lam_Om, 1e-300)
    valid = [k for k in range(nsh) if flags[k] == ""]
    def vmax(lst):
        vals = [lst[k] for k in valid if lst[k] is not None]
        return max(vals) if vals else None
    def bal(lst):
        vals = [lst[k] for k in valid if lst[k] is not None]
        return math.sqrt(sum(v * v for v in vals) / len(vals)) if vals else None
    # tail quantities
    l = model.l_arr; m = model.m_arr
    eT, eS = prob.mode_tail_energies(aT, aS, c_l, omega); tot = (eT + eS).sum().item()
    e_F = (eT + eS)[m > 0].sum().item() / max(tot, 1e-300)
    N_F = math.sqrt(((eT + eS) * m.double() ** 2).sum().item() / max(tot, 1e-300))     # ||d_chi F||/||F||
    em_t = {}
    for q in range(len(m)):
        em_t[int(m[q])] = em_t.get(int(m[q]), 0.0) + float((eT + eS)[q])
    tail_dom_m = max(em_t, key=em_t.get) if em_t else None
    structure.update(tail_dominant_m=tail_dom_m, tail_m_energy_fractions={str(k): v / max(tot, 1e-300) for k, v in sorted(em_t.items())})
    gr_core = [k for k in range(nsh) if sh.edges[k][1] <= 1.0 + 1e-12]
    ba = [((rmsT[3][k] + rmsT[4][k]) / max(rmsT[0][k] + rmsT[1][k] + rmsT[2][k], 1e-300)) for k in gr_core]
    structure.update(near_linear=(bool(all(v < 0.3 for v in ba)) if ba else None), b_over_a_core_min=(min(ba) if ba else None), b_over_a_core_max=(max(ba) if ba else None),
                     note="near_linear: Gram b/a < 0.3 on every core shell (lead 02:02Z 2(e))")
    core_shells = [k for k in range(nsh) if r_tail is None or sh.edges[k][0] <= r_tail]
    N_core = max([N_k[k] for k in core_shells if N_k[k] is not None] or [0.0]); e_core = max([e_k[k] for k in core_shells if e_k[k] is not None] or [0.0])
    d = dict(c_l=c_lf, omega=omf, alpha=alpha, grid=grid_label, n_eval_radii=emodel.Nr, n_eval_angles=emodel.Na, shells=dict(edges=sh.edges, rmid=sh.rmid, flags=flags),
             rms=dict(R_u=rmsRu, T=rmsT, U=rmsU, DU=rmsDU, R_Om=rmsROm, V=rmsV, divU=rmsdiv, max_R_u=maxRu, max_R_Om=maxROm),
             rho_u=rho_u, rho_nl=rho_nl, rho_lin=rho_lin, rho_sp=rho_sp, pi_u=pi_u, pi_nl=pi_nl, peak=peak, rho_Om=rho_Om, rho_Om_nl=rho_Om_nl, rho_div=rho_div,
             gram=dict(a_rms_L=gram_a, b_rms_N=gram_b, gamma=gram_gamma, check_rel=gram_check, note="a^2 + b^2 + 2 a b gamma = RMS(R_u)^2 per shell (check_rel is the relative closure)"),
             d30=dict(Ru_L2_over_T1_L2_r_lt_1=d30_Ru_over_T1_r1, ROm_L2_over_Om_L2=d30_ROm_over_Om, shells_r_lt_1=len(inside)),
             sigma_u=sigma_u, sigma_u_flag=sigma_u_flag, a_fixed_gauge=a_fixed, origin_ball=origin, structure=structure,
             N_k=N_k, e_k=e_k, E_F=[float(v) for v in EF],
             abs_fixed_gauge=dict(r_alpha_RMS_Ru=[rk[k] ** alpha * rmsRu[k] for k in range(nsh)], r_2a1_RMS_Ru=[rk[k] ** (2 * alpha + 1) * rmsRu[k] for k in range(nsh)],
                                  r_invcl_RMS_ROm=[rk[k] ** (1 / c_lf) * rmsROm[k] for k in range(nsh)]),
             global_=dict(rho_u_max=vmax(rho_u), rho_u_bal=bal(rho_u), rho_nl_max=vmax(rho_nl), pi_u_max=vmax(pi_u), pi_nl_max=vmax(pi_nl), peak_max=vmax(peak),
                          rho_Om_max=vmax(rho_Om), rho_Om_nl_max=vmax(rho_Om_nl), rho_div_max=vmax(rho_div), A_u=A_u, A_Om=A_Om,
                          rho_lin_max=vmax(rho_lin), rho_sp_max=vmax(rho_sp), d30_Ru_over_T1_r1=d30_Ru_over_T1_r1, d30_ROm_over_Om=d30_ROm_over_Om,
                          sigma_u_max=vmax([None if sigma_u_flag[k] else sigma_u[k] for k in range(nsh)]),
                          sigma_u_max_shell=(lambda vals: (sh.edges[max(range(nsh), key=lambda k: (vals[k] if vals[k] is not None else -1.0))] if any(v is not None for v in vals) else None))([None if (sigma_u_flag[k] or flags[k]) else sigma_u[k] for k in range(nsh)]),
                          sigma_u_max_r1=vmax([None if (sigma_u_flag[k] or sh.edges[k][1] > 1.0 + 1e-12) else sigma_u[k] for k in range(nsh)]),
                          sigma_Om=d30_ROm_over_Om, a_max=max(a_fixed), a_max_shell=sh.edges[max(range(nsh), key=lambda k: a_fixed[k])],
                          origin_U_rms=origin["U_rms"], origin_B=origin["B_nl_sum"], origin_L=origin["L_lin_sum"],
                          rho_lin_max_r1=vmax([rho_lin[k] if sh.edges[k][1] <= 1.0 + 1e-12 else None for k in range(nsh)]),
                          rho_sp_max_r1=vmax([rho_sp[k] if sh.edges[k][1] <= 1.0 + 1e-12 else None for k in range(nsh)])),
             nonaxi=dict(N_k=N_k, e_k=e_k, N_core=N_core, e_core=e_core, N_F=N_F, e_F=e_F,
                         warning=(N_core < 1e-2 or N_F < 1e-2 or e_core < 1e-4 or e_F < 1e-4)),
             guards=dict(N1_gauge_defect=abs(prob.tail_norm2(aT, aS, c_l, omega).item() - 1.0), N2_max_abs_Omega=absOm.max().item(), N2_r=emodel.r[jm].item(),
                         N2_strain_ratio=strain_ratio, N2_lambda_max_S=lam_max, N4_r_core=r_core, N4_r10=r10, N4_r90=r90,
                         N4_max_U=U.norm(dim=0).max().item(), N4_max_DU=GU.reshape(9, -1).norm(dim=0).max().item(),
                         N5_r_tail=r_tail, N5_r_tail_over_r_core=(None if r_tail is None else r_tail / r_core)),
             pressure=dict(max_abs_P=P.abs().max().item(), p0=ps.p0, monopole=ps.volume_integral(f).item()))
    if not extras:
        return d
    _dev = model.r.device
    d['extras_memory'] = dict(note="cumulative torch.cuda.max_memory_allocated (GB) read after each extras item (the worker resets the counter per battery item)", after_shells=_cuda_peak_GB(_dev))
    try:
        # SPEC 7.6 origin Taylor ratio tau_0: R_u(0) = (1-c_l) u0 + M u0 + omega J u0 + grad P(0), floored denominator
        F0 = model.fields_points(z, torch.zeros(1, 3, dtype=DT, device=model.r.device), need_vort=False)
        u0 = F0['U'][:, 0]; M0 = F0['GU'][:, :, 0]                         # M0[m, i] = d_m U_i(0)
        ps0 = ps if holdout is None else _pressure(prob, c_lf, omf)
        f_tr = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
        gP0 = ps0.gradP_origin(f_tr)
        terms0 = [(1 - c_lf) * u0, torch.einsum('mi,m->i', M0, u0), omf * res.Jvec(u0), gP0]
        Ru0 = sum(terms0)
        Uc = U.norm(dim=0).max().item(); rc = max(float(r_core), 1e-300)
        S0 = Uc * (1 + Uc / rc)
        den_raw = sum(t.norm().item() for t in terms0)
        d['origin'] = dict(u0=[float(v) for v in u0], trace_M=float(M0.trace()), gradP0=[float(v) for v in gP0], R_u0=[float(v) for v in Ru0],
                           tau0_raw=(Ru0.norm().item() / den_raw if den_raw > 0 else None), tau0_floored=Ru0.norm().item() / max(den_raw, 1e-3 * S0),
                           floor_S0=S0, note="tau_0 exact at y = 0; tau_1, tau_2 from the quadratic Taylor fit on small spheres (origin_taylor.py, T08)")
        try:                                                  # SPEC 7.6 orders 1 and 2 (T08; lead gate G1 request 2026-10-25T02:02Z)
            from .origin_taylor import origin_taylor
            ot = origin_taylor(prob, z, c_lf, omf, U_c=Uc, r_core=rc, exact_Ru0=Ru0, exact_M0=M0)
            d['origin'].update(tau1_raw=ot["tau_raw"][1], tau1_floored=ot["tau_floored"][1], tau2_raw=ot["tau_raw"][2], tau2_floored=ot["tau_floored"][2],
                               tau0_fit_floored=ot["tau_floored"][0], D_Ru_norms_fit=ot["D_Ru_norms"], den_sum_terms_fit=ot["den_sum_terms"], floor_1e3_S=ot["floor_1e3_S"],
                               taylor_consistency_rel_change_tau=ot["consistency_rel_change_tau"], taylor_consistency_rel_change_DRu=ot["consistency_rel_change_DRu"],
                               taylor_D0_Ru_vs_exact_rel=ot.get("D0_Ru_vs_exact_rel"), taylor_D1_U_vs_exact_rel=ot.get("D1_U_vs_exact_rel"), taylor_eps=ot["eps"],
                               taylor_radii_fit=ot["radii_fit"], taylor_radii_check=ot["radii_check"])
        except Exception as e:
            d['origin']['taylor_error'] = repr(e)
    except Exception as e:
        d['origin'] = dict(error=repr(e))
    d['extras_memory']['after_origin_taylor'] = _cuda_peak_GB(_dev)
    try:
        # Z and I on a dedicated fine radial grid (Nr = 4 Nk): the cubic integrand Omega.S Omega is under-resolved at
        # Nr = 1.5 Nk (astra review2: sign flips possible); also report the training-grid values for comparison
        fine = getattr(prob, "_fine_model", None)
        if fine is None or fine.Nr != 4 * model.Nk or fine.c_l0 != c_lf or fine.omega0 != omf:
            fine = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, Nr=4 * model.Nk, ntheta=model.ntheta, nphi=model.nphi,
                         c_l=c_lf, omega=omf, free_params=model.free_params, channels=model.channels, device=model.r.device)
            prob._fine_model = fine; prob._fine_ps = PressureSolver(fine, p0=2 * alpha_of(c_lf) + 2, omega=omf, c_l=c_lf)
        Ff = fine.fields_grid(z, need_vort=True)
        Sf = 0.5 * (Ff['GU'] + Ff['GU'].transpose(0, 1))
        Zc = prob._fine_ps.volume_integral((Ff['Om'] ** 2).sum(0)); Ic = prob._fine_ps.volume_integral(torch.einsum('i...,ij...,j...->...', Ff['Om'], Sf, Ff['Om']))
        Ftr = model.fields_grid(z, need_vort=True); Str = 0.5 * (Ftr['GU'] + Ftr['GU'].transpose(0, 1)); pst = _pressure(prob, c_lf, omf)
        Zt = pst.volume_integral((Ftr['Om'] ** 2).sum(0)); It = pst.volume_integral(torch.einsum('i...,ij...,j...->...', Ftr['Om'], Str, Ftr['Om']))
        d['global_integrals'] = dict(Z=float(Zc), I=float(Ic), Sigma_Z=float(Ic / Zc) / (1 - 1.5 * c_lf) if Zc != 0 else None,
                                     Z_training_grid=float(Zt), I_training_grid=float(It), Nr_fine=fine.Nr, Nr_training=model.Nr_src,
                                     F_norm2=float(prob.tail_norm2(aT, aS, c_l, omega)), note="fine-grid (4 Nk) quadrature with factored decay 2/c_l; Sigma_Z = (I/Z)/(1 - 3 c_l/2), exact 1")
    except Exception as e:
        d['global_integrals'] = dict(error=repr(e))
    d['extras_memory']['after_fine_grid_ZI'] = _cuda_peak_GB(_dev)
    if holdout is not None:
        # independent pressure check (SPEC 5.4): ray-integral grad P at a few core points of the holdout grid vs the Green solution
        try:
            from ..pressure.ray_integral import gradP_ray
            js = [j for j in range(emodel.Nr) if 0.3 * model.R0 < emodel.r[j] < 1.5 * model.R0][:4]
            if js:
                pts = torch.stack([emodel.y[j, 7] for j in js]); gsh = torch.stack([gradP[:, j, 7] for j in js])
                gray = gradP_ray(model, z, pts, ntheta=32, nphi=64, nrad=240, chunk=RAY_CHUNK)
                rel = ((gray - gsh).norm(dim=1) / gsh.norm(dim=1).clamp_min(1e-300)).cpu().numpy()
                d['pressure']['ray_check'] = dict(radii=[float(emodel.r[j]) for j in js], rel_diff=[float(v) for v in rel], max_rel_diff=float(rel.max()),
                                                  gradP_ray=[[float(v) for v in row] for row in gray.cpu()], gradP_sh=[[float(v) for v in row] for row in gsh.cpu()], chunk=RAY_CHUNK)
        except Exception as e:
            d['pressure']['ray_check'] = dict(error=repr(e))
        d['extras_memory']['after_ray_check'] = _cuda_peak_GB(_dev)
    return d


def tier_S(d, located_lambda_max=None):
    """SPEC 8 Tier S screen. Items not computed by this code (rho_P on an independent Poisson check) are recorded as False
    with the reason, so the screen cannot pass by omission; flagged shells fail the screen (never counted as successes)."""
    g = d['global_']; n = d['nonaxi']; gu = d['guards']
    rt = gu.get('N5_r_tail_over_r_core')
    checks = dict(rho_u=(g['rho_u_max'] is not None and g['rho_u_max'] <= 1e-2), rho_nl=(g['rho_nl_max'] is not None and g['rho_nl_max'] <= 1e-1),
                  rho_sp=(g.get('rho_sp_max') is not None and g['rho_sp_max'] <= 1e-1),
                  rho_P="not computed (independent Poisson residual missing)", rho_div=(g['rho_div_max'] is not None and g['rho_div_max'] <= 1e-8),
                  N1=(gu['N1_gauge_defect'] <= 1e-8),
                  N2=((located_lambda_max if located_lambda_max is not None else gu['N2_lambda_max_S']) >= 0.9),
                  N4_core_inside=(gu['N4_r_core'] is not None), N5_tail=(rt is not None and rt <= 2 ** 8),
                  N6_spectral=(d.get('spectra_top_fraction') is None or d['spectra_top_fraction'] <= 0.1),
                  N_core=(n['N_core'] >= 1e-2), N_F=(n['N_F'] >= 1e-2), e_core=(n['e_core'] >= 1e-4), e_F=(n['e_F'] >= 1e-4),
                  no_flagged_shells=(not any(f for f in d['shells']['flags'])), holdout_grid=(d.get('grid') == 'holdout'))
    ok = all(v is True for v in checks.values())
    return ok, checks
