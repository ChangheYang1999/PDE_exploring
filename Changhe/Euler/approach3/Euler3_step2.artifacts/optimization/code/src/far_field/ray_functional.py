"""SPEC v1.22 (a), (b) (lead 2026-10-25T02:54Z item 7, 03:21Z item 5): the twisted-ray inverse G of the linear similarity operator and the
tail functional F^(R), in the azimuthal-mode form (d46 (v)): for the spherical components of a field f with azimuthal Fourier modes
f_m(rho, theta) (chi = phi + kappa log r, kappa = omega/c_l),
    (G f)_m(r, theta) = (1/c_l) r^(-alpha) int_0^r rho^(alpha-1) (r/rho)^(i m kappa) f_m(rho, theta) d rho,
    (F^(R) f)_m(theta) = (1/c_l) int_0^R rho^(alpha-1) rho^(-i m kappa) f_m(rho, theta) d rho,
with the identities G[L U] = U and F^(R)[L U] = R^alpha (twisted) U(R) for the linear part L U = T1 + T2 + T3 (self-check, route 2 in SPEC).
Reported (no threshold): tau_F(R) = ||F^(R)[R_u]||_L2(S^2) / ||F_U|| at radii R >= 2^8 r_core (||F_U|| = 1 in the F-gauge, computed here from
R^alpha U(R) at the largest radius), and delta_G = RMS_k(G R_u)/RMS_k(U) on the core ball and on every dyadic shell (and on B(y*, a_eff/2)
when y* and a_eff are supplied). Quadrature: fields on a dense geometric radial grid (n_per_octave radii per octave from R0 2^-k_in to
R0 2^k_out) with the holdout angular Gauss grid; the radial integrals use the composite trapezoid rule in log rho (error reported by a
half-resolution rerun); the cut-off [0, rho_min] contributes O(rho_min^alpha) and is reported."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver

DT = torch.float64


def _spherical_modes(X, grid, ntheta, nphi):
    """Cartesian field X (3, Nr, Na) -> azimuthal Fourier modes of the spherical components: (3, Nr, ntheta, nphi//2+1) complex."""
    er, eth, eph = grid.sph_basis()
    Xs = torch.stack([torch.einsum('ija,ai->ja', X, e) for e in (er, eth, eph)], 0).reshape(3, X.shape[1], ntheta, nphi)
    return torch.fft.rfft(Xs, dim=-1) / nphi                       # f(phi) = sum_m f_m e^{i m phi} (m >= 0; negative m by conjugation)


def ray_functionals(prob, z, n_per_octave=16, k_in=8, k_out=20, ntheta=None, nphi=None, device=None, radii_tau=None, y_star=None, a_eff=None):
    model = prob.model
    device = device or model.r.device
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega); alpha = alpha_of(c_lf); kappa = omf / c_lf; R0 = model.R0
    L = model.L; Lx = getattr(model, "L_ext", L)
    ntheta = ntheta or (2 * Lx + 12); nphi = nphi or (4 * Lx + 18)
    nr = n_per_octave * (k_in + k_out) + 1
    radii = R0 * 2.0 ** np.linspace(-k_in, k_out, nr)
    em = Model(L=L, Nk=model.Nk, m_parity=model.m_parity, R0=R0, r_nodes=radii, ntheta=ntheta, nphi=nphi, c_l=model.c_l0, omega=model.omega0,
               free_params=model.free_params, channels=model.channels, device=device, phi0=math.pi / (2 * nphi))
    F = em.fields_grid(z, need_vort=False)
    ps = PressureSolver(model, p0=2 * alpha + 2, omega=omf, c_l=c_lf, eval_model=em)
    f_src = res.pressure_source(model.fields_grid(z, need_vort=False)['GU'])
    P, gradP, _, _ = ps.solve(f_src)
    from ..validation.spec_diagnostics import five_term_split
    T = five_term_split(F, gradP); Ru = sum(T); LU = T[0] + T[1] + T[2]; U = F['U']
    r = em.r; lr = torch.log(r)
    w_ang = em.grid.w / (4 * math.pi)
    # modes
    fm = {name: _spherical_modes(X, em.grid, ntheta, nphi) for name, X in (("Ru", Ru), ("LU", LU), ("U", U))}
    mvals = torch.arange(fm["U"].shape[-1], dtype=DT, device=device)
    # integrand rho^(alpha-1) rho^(-i m kappa) f_m, integrated in d rho = rho d(log rho) by the trapezoid rule on the uniform log grid
    dlr = (lr[1] - lr[0]).item()
    phase = torch.exp(-1j * (mvals[None, :] * kappa) * lr[:, None])                  # (Nr, M): rho^(-i m kappa)
    def cumint(modes):                                                                # modes (3, Nr, ntheta, M) -> cumulative integral (3, Nr, ntheta, M)
        g = modes * (r ** alpha)[None, :, None, None] * phase[None, :, None, :]       # rho^(alpha-1) * rho (measure) = rho^alpha
        c = torch.zeros_like(g)
        c[:, 1:] = torch.cumsum(0.5 * (g[:, 1:] + g[:, :-1]) * dlr, dim=1)
        c = c + g[:, :1] * (r[0] ** 0) / alpha * 0.0                                   # cut-off [0, rho_min]: omitted, reported separately
        return c
    def apply_G(modes):
        I = cumint(modes)
        return (1.0 / c_lf) * (r ** (-alpha))[None, :, None, None] * torch.exp(1j * (mvals[None, :] * kappa) * lr[:, None])[None, :, None, :] * I
    def to_grid(modes):                                                               # modes (3, Nr, ntheta, M) -> spherical components (3, Nr, ntheta, nphi)
        return torch.fft.irfft(modes * nphi, n=nphi, dim=-1)
    def shell_rms(Xsph):                                                              # (3, Nr, ntheta, nphi) -> per-node RMS over the sphere (Nr,)
        sq = (Xsph ** 2).sum(0).reshape(Xsph.shape[1], -1)
        return (sq * w_ang[None, :]).sum(1)
    GRu = to_grid(apply_G(fm["Ru"])); GLU = to_grid(apply_G(fm["LU"]))
    Usph = to_grid(fm["U"])
    # identity check G[L U] = U (relative, per node, away from the innermost cut-off)
    num = shell_rms(GLU - Usph); den = shell_rms(Usph)
    idx_chk = (r > R0 * 2.0 ** (-k_in + 3)).nonzero().flatten()
    g_identity_rel = float((num[idx_chk].sum() / den[idx_chk].sum()).sqrt())
    # tail functional F^(R): (1/c_l) I_m(R) ; the leading coefficient from R^alpha U(R) in the twisted frame at the largest radius
    IR = cumint(fm["Ru"]) / c_lf; ILU = cumint(fm["LU"]) / c_lf
    def sphere_norm_modes(M_):                                                         # (3, ntheta, M) complex modes -> L2(S^2) norm of the field
        wth = w_ang.reshape(ntheta, nphi)[:, 0] * nphi                               # theta weights (sum over phi folded in)
        e = (M_.abs() ** 2); e[..., 1:] *= 2.0                                        # m > 0 counted twice (negative m)
        return float(math.sqrt(4 * math.pi * (e.sum(-1).sum(0) * wth).sum().item()))
    jmax = len(r) - 1
    Umodes_tw = fm["U"][:, jmax] * (r[jmax] ** alpha) * torch.exp(-1j * mvals * kappa * lr[jmax])[None, None, :]   # R^alpha U(R) in the twisted frame
    F_norm = sphere_norm_modes(Umodes_tw)
    radii_tau = radii_tau or [2.0 ** 8 * R0, 2.0 ** 12 * R0, 2.0 ** 16 * R0, 2.0 ** 20 * R0]
    tau = {}; selfcheck = {}
    for Rt in radii_tau:
        j = int(torch.argmin((r - Rt).abs()).item())
        tau[f"{r[j].item():.4g}"] = sphere_norm_modes(IR[:, j]) / max(F_norm, 1e-300)
        # self-check: F^(R)[L U] against R^alpha U(R) in the twisted frame
        UR = fm["U"][:, j] * (r[j] ** alpha) * torch.exp(-1j * mvals * kappa * lr[j])[None, None, :]
        selfcheck[f"{r[j].item():.4g}"] = sphere_norm_modes(ILU[:, j] - UR) / max(sphere_norm_modes(UR), 1e-300)
    # delta_G per dyadic shell and core ball (log-trapezoid volume average over the dense radii)
    msGRu = shell_rms(GRu); msU = shell_rms(Usph)
    edges = [(0.0, R0 * 2.0 ** -5)] + [(R0 * 2.0 ** j, R0 * 2.0 ** (j + 1)) for j in range(-5, k_out)]
    delta_G = []
    rr = r.cpu().numpy(); vol_w = rr ** 3                                              # d(volume) = r^2 dr = r^3 d(log r)
    for (a_, b_) in edges:
        m_ = (rr >= a_) & (rr < b_)
        if m_.sum() < 2:
            delta_G.append(None); continue
        wv = vol_w[m_]
        dG = math.sqrt(float((msGRu.cpu().numpy()[m_] * wv).sum() / (msU.cpu().numpy()[m_] * wv).sum()))
        delta_G.append(dG)
    # lead 2026-10-25T04:04Z (a), d50/d55 (FINAL_REPORT section 2 item 25): mean-swirl generation. Azimuthal averages at fixed (r, theta):
    # Gamma_0 = <(J y).U> (mean angular momentum), S = <U_m>.grad Gamma_0 - <(J y).((U.grad) U)> (eddy angular-momentum flux),
    # E = <(J y).R_u>; identity E = (1 - 2 c_l) Gamma_0 + W_0.grad Gamma_0 - S with W_0 = c_l y + <U_m> (mean meridional velocity);
    # Q_sw = (1 - 2 c_l) max|Gamma_0| / max|S| <= 1 for every exact profile (necessary condition; reported, no threshold).
    swirl = None
    try:
        swirl = mean_swirl_block(F, Ru, em, c_lf, ntheta, nphi)
    except Exception as e:
        swirl = dict(error=repr(e))
    # lead 03:29Z item 5 (d49b): tau_F split by |m| (squared-norm fractions) and, for m = 0, by spherical component; the tail's own split for comparison
    jR = int(torch.argmin((r - radii_tau[-1]).abs()).item())
    wth = (w_ang.reshape(ntheta, nphi)[:, 0] * nphi)
    def mode_energy(M_):                                               # (3, ntheta, M) -> per-m squared norm (M,) and m = 0 per-component (3,)
        e = (M_.abs() ** 2) * wth[None, :, None] * 4 * math.pi
        em_ = e.sum(dim=(0, 1)); em_[1:] *= 2.0
        return em_, e[:, :, 0].sum(1)
    eR, eR0 = mode_energy(IR[:, jR]); eU, eU0 = mode_energy(Umodes_tw)
    nm = min(6, eR.numel())
    out = dict(c_l=c_lf, omega=omf, alpha=alpha, kappa=kappa, n_radii=nr, n_per_octave=n_per_octave, ntheta=ntheta, nphi=nphi, F_norm_from_tail=F_norm,
               tau_F_by_m=dict(m=list(range(nm)), generated_fraction=(eR[:nm] / eR.sum().clamp_min(1e-300)).tolist(), tail_fraction=(eU[:nm] / eU.sum().clamp_min(1e-300)).tolist(),
                               amplitude_ratio=((eR[:nm] / eU[:nm].clamp_min(1e-300)).sqrt()).tolist(),
                               m0_components_generated_over_tail=((eR0 / eU0.clamp_min(1e-300)).sqrt()).tolist(), m0_component_names=["r", "theta", "phi"],
                               note="squared-norm fractions of F^(R)[R_u] (generated) and of R^alpha U(R) (imposed tail) by |m|; amplitude_ratio = generated/tail per |m|"),
               tau_F=tau, mean_swirl=swirl, selfcheck_FR_LU_vs_RalphaU=selfcheck, G_identity_rel=g_identity_rel, delta_G_shells=dict(edges=edges, delta_G=delta_G),
               delta_G_core_ball=delta_G[0], delta_G_max=max(v for v in delta_G if v is not None), cutoff_rho_min=float(r[0]),
               note="trapezoid in log rho on a uniform grid; the [0, rho_min] part of the ray integral is omitted (O(rho_min^alpha)); tau_F uses ||F_U|| from R^alpha U at the largest radius")
    if y_star is not None and a_eff is not None:
        try:
            ys = torch.as_tensor(y_star, dtype=DT, device=device); ra = float(a_eff) / 2.0
            pts = em.y.reshape(-1, 3); d = (pts - ys[None, :]).norm(dim=1); sel = d < ra
            GRu_cart = None  # the ball average on the dense grid in spherical components
            GRs = GRu.reshape(3, -1)[:, sel]; Us = Usph.reshape(3, -1)[:, sel]
            out["delta_G_ball_ystar"] = float((GRs ** 2).sum().sqrt() / (Us ** 2).sum().sqrt().clamp_min(1e-300)); out["ball_ystar_points"] = int(sel.sum())
        except Exception as e:
            out["delta_G_ball_ystar"] = repr(e)
    return out

def mean_swirl_block(F, Ru, em, c_l, ntheta, nphi):
    """d50 identity and d55 Q_sw on the dense product grid (uniform phi: exact azimuthal averages of the represented modes).
    F: fields dict (U (3,Nr,Na), GU (3,3,Nr,Na) with GU[m, i] = d_m U_i, y (Nr,Na,3)); Ru (3,Nr,Na). Returns maxima over the grid."""
    U, GU = F['U'], F['GU']; y = F['y']
    yv = y.permute(2, 0, 1)                                                   # (3, Nr, Na)
    Jy = torch.stack([-yv[1], yv[0], torch.zeros_like(yv[0])], 0)
    f = (Jy * U).sum(0)                                                       # (J y).U
    gf = torch.stack([U[1], -U[0], torch.zeros_like(U[0])], 0) + torch.einsum('ij...,j...->i...', GU, Jy)   # grad((J y).U)
    adv = torch.einsum('m...,mj...->j...', U, GU)                              # (U.grad) U
    er, eth, _ = em.grid.sph_basis()                                          # (Na, 3)
    Nr = U.shape[1]
    def M(q):                                                                 # azimuthal mean: (Nr, Na) -> (Nr, ntheta)
        return q.reshape(Nr, ntheta, nphi).mean(-1)
    def dot(V, e):
        return torch.einsum('ija,ai->ja', V, e)                                # (3,Nr,Na).(Na,3) -> (Nr,Na)
    G0 = M(f); dr = M(dot(gf, er)); dt = M(dot(gf, eth)); Ur = M(dot(U, er)); Ut = M(dot(U, eth))
    A = M((Jy * adv).sum(0))
    S = Ur * dr + Ut * dt - A
    E = M((Jy * Ru).sum(0))
    r = em.r
    rhs = (1 - 2 * c_l) * G0 + (c_l * r[:, None] * dr + Ur * dr + Ut * dt) - S
    scale = (E.abs().max() + S.abs().max()).clamp_min(1e-300)
    clos = float((E - rhs).abs().max() / scale)
    i0 = int(G0.abs().argmax().item()) // ntheta; i1 = int(S.abs().argmax().item()) // ntheta; i2 = int(E.abs().argmax().item()) // ntheta
    Smax = float(S.abs().max()); G0max = float(G0.abs().max())
    return dict(Q_sw=((1 - 2 * c_l) * G0max / Smax if Smax > 0 else None), Gamma0_max=G0max, S_max=Smax, E_max=float(E.abs().max()),
                r_at_Gamma0_max=float(r[i0]), r_at_S_max=float(r[i1]), r_at_E_max=float(r[i2]), identity_closure=clos,
                note="Q_sw = (1 - 2 c_l) max|Gamma_0| / max|S| over the dense ray grid (exact profile: <= 1); closure = max|E - rhs| / (max|E| + max|S|) of the d50 identity")
