"""farfield_nextorder.py -- far-field leading and NEXT-ORDER asymptotics derived from the PDE, compared with a stored state (shift 6; PROMPT
sec. 4 item 4: "Derive or fit the far-field leading and next-order asymptotics from the PDE, compare them with the numerical profile").

Class A tail (SPEC sec. 5): Omega = r^(-1/beta) a(phi) + r^(-2/beta) a2(phi) + ..., Theta = r^(1-2/beta) b(phi) + r^(1-3/beta) b2(phi) + ...,
with the polar angle phi = atan2(x, -y) in (0, pi) on the half plane x > 0 (x = r sin phi, y = -r cos phi). Inserting the ladders into
(B2-P) with W = beta X + V - V(0) and V = e U[Omega] + (velocity of the forcing), where the forcing velocity is lower order at the orders
checked (eps-forcing states: the exact Gaussian dipole gives an O(r^-2) velocity; lambda-path states: the fixed source f has its own class A
tail with beta_seed, which enters at the next order with a MIXED power, see below), the leading orders are identically satisfied for any a, b
in the class (pure dilation), and at the next order
   a2(phi) = r^(2/beta) [ e U1.grad(r^(-1/beta) a) - d_x (r^(1-2/beta) b) ],      b2(phi) = + r^(3/beta - 1) e U1.grad(r^(1-2/beta) b),
where U1 = r^(1-1/beta) u(phi) is the velocity of the LEADING vorticity tail alone, obtained mode by mode from the half-range sine series
a(phi) = sum_k a_k sin(k phi):  Psi1 = sum_k -a_k r^p sin(k phi)/(p^2 - k^2), p = 2 - 1/beta (the homogeneous particular solution of the modal
Poisson equation; multipole and constant-velocity pieces of the canonical inverse are lower order: r^-k and r^0 against r^(1-1/beta)).
(Derivation: (beta r d_r + 1)(r^q g) = (beta q + 1) r^q g and (beta r d_r - (beta - 2))(r^q g) = (beta q - beta + 2) r^q g; at q = -2/beta
(vorticity) and q = 1 - 3/beta (temperature) both eigenvalues are -1, balanced by the leading velocity correction e U1.grad(leading term)
and, for the vorticity, the buoyancy term -d_x Theta_1: -a2 + e U1.grad Omega_1 - d_x Theta_1 = 0, -b2 + e U1.grad Theta_1 = 0. Lower-order
pieces at these orders: stream-function multipoles r^-k (velocity r^(-k-1)), the constant velocity including the centre subtraction (velocity
r^0: advects Omega_1 at r^(-1-1/beta) and Theta_1 at r^(-2/beta), the 'constant-velocity ladder' terms fitted below), the exact Gaussian dipole
(velocity r^-2). Referee round shift6a (astra) checked these formulas and signs.)
ENDPOINT coefficients (exact for the stored representation; astra shift6a): with r = L sqrt((1-t)^(-2 beta) - 1), (1-t) = (r/L)^(-1/beta)(1 + O(r^-2)),
G = (1-t)^(beta+1) [rho_odd] S_G(t, phi) and F = (1-t)^(beta+2) S_F(t, phi) (spline sums; rho_odd = 1 with zero derivative at t = 1):
   a = L^(1+1/beta) sin(phi) S_G(1, phi),  a2 = -L^(1+2/beta) sin(phi) d_t S_G(1, phi),  b = L^(1+2/beta) sin^2(phi) S_F(1, phi),  b2 = -L^(1+3/beta) sin^2(phi) d_t S_F(1, phi),
so the stored own-ladder coefficients are read off from the last spline coefficients of every angular mode, and the PDE relations can be
checked on them exactly (angular derivatives analytic). For the lambda-path states the forced equations require a MIXED power r^(-1/beta-1/beta_seed)
(coefficient (beta_seed/beta) lambda u_f.grad Omega_1, dilation eigenvalue -beta/beta_seed) that is NOT in the basis, so their stored own-ladder
coefficients cannot satisfy the own-velocity relation; the window fits below then measure a finite-window emulation, not asymptotic coefficients.)
Checks performed on a stored state:
 (i)  power-law fits of Omega(r, phi) and Theta(r, phi) on a radial window [r1, r2] with the fixed exponents of the ladder (linear LS at
      each angle; extra term r^(-1-1/beta) for the constant-velocity ladder); fit residuals reported;
 (ii) the leading velocity: actual U(r, phi) r^(-(1-1/beta)) (cross inverse of the stored vorticity) against u(phi) from the fitted a_k;
 (iii) fitted a2, b2 against the PDE predictions (relative L2 over the angles), on two radial windows (window dependence = fit uncertainty).
For lambda-path states the leading velocity of the transport field includes lambda U[f] with f's tail r^(-1/beta_seed) a_f(phi): the induced
next-order terms have the mixed exponents r^(-1/beta-1/beta_seed) and r^(1-2/beta-1/beta_seed) with coefficients (beta_seed/beta) lambda u_f.grad(leading
term) (dilation eigenvalue -beta/beta_seed); they are predicted from the fitted tails and subtracted from the data before the own ladder is fitted
(two-pass; --no_subtract 1 folds them into one r^(-2/beta) coefficient instead). The forcing's a_f is fitted from the seed representation of f.
Angular derivatives in the window fits: a by its (exact) sine series, b by its (exact) cosine series (astra shift6c); the endpoint check uses analytic derivatives.
Usage: python3 code/farfield_nextorder.py runs/state.npz [--r1 1e3 --r2 1e7] [--nphi 180] [--kmax 40] [--out runs/ffno_<tag>.json]"""
import sys, os, json, argparse, time, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from fixedsrc import cross_inverse, velocity_from_modes
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)
dev = 'cuda'


def tail_fit(vals, r, powers, r_ref):
    """vals (Nr, Nphi); model sum_k c_k (r/r_ref)^powers[k]; returns c (len(powers), Nphi) and the relative fit residual."""
    A = np.stack([(r / r_ref) ** p for p in powers], 1)
    c, *_ = np.linalg.lstsq(A, vals, rcond=None)
    res = A @ c - vals
    tail_fit.cond = float(np.linalg.cond(A))
    return c, float(np.linalg.norm(res) / np.linalg.norm(vals))


def sine_coeffs(f, phi, kmax):
    """half-range sine coefficients on (0, pi) from samples at the midpoint angles phi (uniform)."""
    dphi = phi[1] - phi[0]; ks = np.arange(1, kmax + 1)
    return (2 / np.pi) * (np.sin(np.outer(ks, phi)) @ f) * dphi, ks


def homog_velocity(a_k, ks, p, phi):
    """u(phi) = velocity of Omega = r^(p-2) sum a_k sin(k phi) divided by r^(p-1): Psi = r^p sum c_k sin(k phi), c_k = -a_k/(p^2-k^2)."""
    c = -a_k / (p ** 2 - ks ** 2)
    S = np.sin(np.outer(ks, phi)); C = np.cos(np.outer(ks, phi))
    Psi = c @ S; Psir = p * (c @ S); Psiphi = (c * ks) @ C          # /r^p, /r^(p-1), /r^p
    s, co = np.sin(phi), np.cos(phi)
    u1 = co * Psir - s * Psiphi; u2 = s * Psir + co * Psiphi      # both / r^(p-1)
    return u1, u2


def grad_homog(q, g, gp, phi):
    """d_x, d_y of r^q g(phi), divided by r^(q-1): (sin phi q g + cos phi g', -cos phi q g + sin phi g')."""
    s, co = np.sin(phi), np.cos(phi)
    return s * q * g + co * gp, -co * q * g + s * gp


def dphi(g, phi, kmax=60):
    """angular derivative by the half-range SINE series: exact for a = sin(phi) sum_k g_k cos(k phi) (a finite sine polynomial)."""
    c, ks = sine_coeffs(g, phi, kmax)
    return (c * ks) @ np.cos(np.outer(ks, phi))


def dphi_cos(g, phi, kmax=60):
    """angular derivative by the COSINE series on (0, pi) (midpoint rule, exact for cosine polynomials of degree < Nphi - kmax):
    for b = sin^2(phi) sum_k f_k cos(k phi), a finite cosine polynomial (astra shift6c: its truncated sine differentiation is not exact)."""
    dphi_ = phi[1] - phi[0]; ks = np.arange(0, kmax + 1)
    c = (2 / np.pi) * (np.cos(np.outer(ks, phi)) @ g) * dphi_; c[0] *= 0.5
    return -(c * ks) @ np.sin(np.outer(ks, phi))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--r1', type=float, default=1e3); ap.add_argument('--r2', type=float, default=1e7)
    ap.add_argument('--nr', type=int, default=33); ap.add_argument('--nphi', type=int, default=180); ap.add_argument('--kmax', type=int, default=40); ap.add_argument('--out', type=str, default=''); ap.add_argument('--no_subtract', type=int, default=0, help='1: one-pass treatment (source term folded into the r^(-2/beta) coefficient at r_ref)')
    a = ap.parse_args(); t0 = time.time()
    cF, cG, meta = load_state(a.state, dev); beta = float(meta['beta']); L = float(meta['L']); bb = float(meta.get('beta_basis', beta)); rmap = str(meta.get('rmap', 'r'))
    b = basis_from_meta(meta, dev); g = Geometry(b, bb, L, rmap=rmap)
    eps = float(meta.get('eps', 1.0)); lam = float(meta.get('lam', 0.0)); src_mode = str(meta.get('source_mode', ''))
    phi = (np.arange(a.nphi) + 0.5) * np.pi / a.nphi; phit = torch.tensor(phi, dtype=DT, device=dev)
    out = dict(file=a.state, beta=beta, eps=eps, lam=lam, source_mode=src_mode, windows={})
    # centre check of the stored amplitude
    xs = torch.tensor([1e-3], dtype=DT, device=dev); ys = torch.tensor([0.0], dtype=DT, device=dev)
    F0, G0 = fields_at(b, bb, L, rmap, cF, cG, xs, ys); out['centre'] = dict(F=float(F0[0]), G=float(G0[0]), a0_meta=float(meta.get('a0', float('nan'))), G_over_4a0_beta=float(G0[0]) / (4 * float(F0[0]) / beta))
    # ---- ENDPOINT coefficients of the stored representation (exact) and the own-velocity PDE relations on them
    from scipy.interpolate import BSpline
    K, Nb = b.K, b.Nb; deg = int(meta['deg']); mcount = b.mk if rmap == 'r' else b.mk2
    spl = BSpline(b.knots, np.eye(Nb), deg, extrapolate=False); t1 = 1 - 1e-13
    B1 = np.nan_to_num(spl(t1)); dB1 = np.nan_to_num(spl.derivative()(t1))
    cFn = cF.cpu().numpy(); cGn = cG.cpu().numpy(); al = 1 / beta
    SG0 = np.zeros(a.nphi); SG1 = np.zeros(a.nphi); SF0 = np.zeros(a.nphi); SF1 = np.zeros(a.nphi)
    dSG0 = np.zeros(a.nphi); dSG1 = np.zeros(a.nphi); dSF0 = np.zeros(a.nphi); dSF1 = np.zeros(a.nphi)   # d/dphi of the mode sums
    for k in range(K):
        cGk = cGn[k * Nb:(k + 1) * Nb].copy(); cFk = cFn[k * Nb:(k + 1) * Nb].copy(); m = int(mcount[k]); cGk[:m] = 0; cFk[:m] = 0
        ck = np.cos(k * phi); dck = -k * np.sin(k * phi)
        SG0 += ck * (B1 @ cGk); SG1 += ck * (dB1 @ cGk); SF0 += ck * (B1 @ cFk); SF1 += ck * (dB1 @ cFk)
        dSG0 += dck * (B1 @ cGk); dSG1 += dck * (dB1 @ cGk); dSF0 += dck * (B1 @ cFk); dSF1 += dck * (dB1 @ cFk)
    sn, cs = np.sin(phi), np.cos(phi)
    aE = L ** (1 + al) * sn * SG0; a2E = -L ** (1 + 2 * al) * sn * SG1; bE = L ** (1 + 2 * al) * sn ** 2 * SF0; b2E = -L ** (1 + 3 * al) * sn ** 2 * SF1
    daE = L ** (1 + al) * (cs * SG0 + sn * dSG0); dbE = L ** (1 + 2 * al) * (2 * sn * cs * SF0 + sn ** 2 * dSF0)
    # exact sine coefficients of a = sin(phi) sum_k g_k cos(k phi): a_{k+1} += g_k/2, a_{k-1} -= g_k/2
    gk = np.array([B1 @ np.where(np.arange(Nb) >= int(mcount[k]), cGn[k * Nb:(k + 1) * Nb], 0.0) for k in range(K)]) * L ** (1 + al)
    AK = np.zeros(K + 2); AK[1] += gk[0]
    for k in range(1, K):
        AK[k + 1] += gk[k] / 2; AK[k - 1] -= gk[k] / 2
    ksE = np.arange(1, K + 2); aKE = AK[1:]
    e_own0 = 1.0 if (str(meta.get('source_mode', '')) == 'fixed_velocity_block') else eps
    u1E, u2E = homog_velocity(aKE, ksE, 2 - 1 / beta, phi)
    gxE, gyE = grad_homog(-1 / beta, aE, daE, phi); txE, tyE = grad_homog(1 - 2 / beta, bE, dbE, phi)
    a2E_pred = e_own0 * (u1E * gxE + u2E * gyE) - txE; b2E_pred = e_own0 * (u1E * txE + u2E * tyE)
    out['endpoint'] = dict(method='exact own-ladder coefficients from the last spline coefficients (value and t-derivative at t = 1), analytic angular derivatives, exact sine series',
                           a_L2=float(np.linalg.norm(aE) / np.sqrt(a.nphi)), a2_L2=float(np.linalg.norm(a2E) / np.sqrt(a.nphi)), b_L2=float(np.linalg.norm(bE) / np.sqrt(a.nphi)), b2_L2=float(np.linalg.norm(b2E) / np.sqrt(a.nphi)),
                           a2_rel_diff_own_relation=float(np.linalg.norm(a2E - a2E_pred) / max(np.linalg.norm(a2E_pred), 1e-300)), b2_rel_diff_own_relation=float(np.linalg.norm(b2E - b2E_pred) / max(np.linalg.norm(b2E_pred), 1e-300)),
                           note=('lambda-path state: the forced equations need the mixed power r^(-1/beta-1/beta_seed), absent from the basis; the own relation is not expected to hold' if e_own0 == 1.0 and str(meta.get('source_mode', '')) == 'fixed_velocity_block' else 'eps-forcing state: the own relation (with e = eps) is the full next-order relation up to O(r^-2) forcing terms'))
    # transport velocity multiplier of the own vorticity and the forcing tail
    if src_mode == 'fixed_velocity_block' and np.asarray(meta['cG_f']).size > 0:
        e_own = 1.0
        bs = Basis(int(meta['seed_Nt']), int(meta['seed_deg']), int(meta['seed_K']), int(meta['seed_Nphi']), ng_coll=int(meta['seed_ngc']), m_reg=int(meta['seed_mreg']), device=dev, grade=float(meta['seed_grade']))
        gs = Geometry(bs, float(meta['beta_seed']), float(meta.get('seed_L', L)), rmap=str(meta.get('seed_rmap', rmap))); beta_f = float(meta['beta_seed'])
        cGf = torch.tensor(np.asarray(meta['cG_f']), dtype=DT, device=dev); forcing = ('lam_source', lam, bs, gs, beta_f, cGf)
    else:
        e_own = eps; forcing = None
    out['transport'] = dict(own_multiplier=e_own, forcing=('lambda U[f], f class A with beta_seed %.4f, lambda %.6f' % (forcing[4], lam)) if forcing else ('eps-forcing: (1-eps) U[Omega_ext] = O(r^-2), neglected at next order' if eps < 1 else 'none'))
    p = 2 - 1 / beta
    for (r1, r2) in [(a.r1, a.r2), (a.r1, np.sqrt(a.r1 * a.r2)), (np.sqrt(a.r1 * a.r2), a.r2)]:
        r = np.logspace(np.log10(r1), np.log10(r2), a.nr); rt = torch.tensor(r, dtype=DT, device=dev); r_ref = float(np.sqrt(r1 * r2))
        X = rt[:, None] * torch.sin(phit)[None, :]; Y = -rt[:, None] * torch.cos(phit)[None, :]
        F, G = fields_at(b, bb, L, rmap, cF, cG, X.reshape(-1), Y.reshape(-1))
        Om = (X.reshape(-1) * G).reshape(a.nr, a.nphi).cpu().numpy(); Th = (X.reshape(-1) ** 2 * F).reshape(a.nr, a.nphi).cpu().numpy()
        pw_om = [-1 / beta, -2 / beta, -3 / beta, -1 - 1 / beta]; pw_th = [1 - 2 / beta, 1 - 3 / beta, 1 - 4 / beta, -2 / beta]
        c_om, res_om = tail_fit(Om, r, pw_om, r_ref); cond_om = tail_fit.cond; c_th, res_th = tail_fit(Th, r, pw_th, r_ref); cond_th = tail_fit.cond
        # coefficients at r_ref normalization -> absolute: c_k (r/r_ref)^q = c_k r_ref^-q r^q
        a1 = c_om[0] * r_ref ** (1 / beta); a2_fit = c_om[1] * r_ref ** (2 / beta); b1 = c_th[0] * r_ref ** (-(1 - 2 / beta)); b2_fit = c_th[1] * r_ref ** (-(1 - 3 / beta))
        # leading velocity from the fitted leading tail
        a_k, ks = sine_coeffs(a1, phi, min(a.kmax, K + 2)); u1, u2 = homog_velocity(a_k, ks, p, phi)
        # actual far velocity of the stored vorticity (cross inverse) at r_ref, scaled by r^(1-1/beta)
        Psi, dPsi = cross_inverse(g, cG, torch.tensor([r_ref], dtype=DT, device=dev))
        Pe = Psi.expand(-1, a.nphi); dPe = dPsi.expand(-1, a.nphi)
        xr = torch.tensor(r_ref * np.sin(phi), dtype=DT, device=dev); yr = torch.tensor(-r_ref * np.cos(phi), dtype=DT, device=dev)
        U1a, U2a = velocity_from_modes(Pe, dPe, xr, yr); U1a = U1a.cpu().numpy() / r_ref ** (1 - 1 / beta); U2a = U2a.cpu().numpy() / r_ref ** (1 - 1 / beta)
        vel_rel = float(np.linalg.norm(np.hypot(U1a - u1, U2a - u2)) / np.linalg.norm(np.hypot(u1, u2)))
        # predicted next-order coefficients (own-vorticity leading velocity, multiplier e_own)
        kd = min(a.kmax, K + 2)
        gx, gy = grad_homog(-1 / beta, a1, dphi(a1, phi, kd), phi)      # grad(r^(-1/beta) a) / r^(-1/beta-1)
        tx, ty = grad_homog(1 - 2 / beta, b1, dphi_cos(b1, phi, kd), phi)  # grad(r^(1-2/beta) b) / r^(-2/beta); cosine series (b is a cosine polynomial)
        a2_pred = e_own * (u1 * gx + u2 * gy) - tx                     # r^(1-1/beta) r^(-1/beta-1) = r^(-2/beta) ; d_x Theta1 ~ r^(-2/beta)
        b2_pred = e_own * (u1 * tx + u2 * ty)                         # r^(1-1/beta) r^(-2/beta) = r^(1-3/beta)
        extra = {}
        if forcing is not None and not getattr(a, 'no_subtract', False):
            # TWO-PASS treatment of the near-degenerate source term: the source-induced next-order terms are PREDICTED from the leading
            # tails (a1, b1 of this state, a_f of the source) and SUBTRACTED from the data, exactly with their own exponents
            # r^(-1/beta-1/beta_f) and r^(1-2/beta-1/beta_f); the remainder is fitted with the state's own ladder and compared with the
            # own-velocity prediction. (The leading coefficients a1, b1 are unaffected by the subtraction to leading order.)
            _, lam_, bs, gs, beta_f, cGf = forcing
            Ff, Gf = fields_at(bs, beta_f, float(gs.L), gs.rmap, torch.zeros_like(cGf), cGf, X.reshape(-1), Y.reshape(-1))
            Omf = (X.reshape(-1) * Gf).reshape(a.nr, a.nphi).cpu().numpy()
            c_f, res_f = tail_fit(Omf, r, [-1 / beta_f, -2 / beta_f, -3 / beta_f, -1 - 1 / beta_f], r_ref); af1 = c_f[0] * r_ref ** (1 / beta_f)
            afk, ksf = sine_coeffs(af1, phi, min(a.kmax, bs.K + 2)); uf1, uf2 = homog_velocity(afk, ksf, 2 - 1 / beta_f, phi)
            fac = beta_f / beta                                                        # dilation eigenvalue of the mixed powers is -beta/beta_f (astra shift6a)
            a2_src = fac * lam_ * (uf1 * gx + uf2 * gy); b2_src = fac * lam_ * (uf1 * tx + uf2 * ty)      # coefficients of r^(-1/beta-1/beta_f), r^(1-2/beta-1/beta_f)
            Om_sub = Om - np.outer(r ** (-1 / beta - 1 / beta_f), a2_src); Th_sub = Th - np.outer(r ** (1 - 2 / beta - 1 / beta_f), b2_src)
            c_om2, res_om2 = tail_fit(Om_sub, r, pw_om, r_ref); c_th2, res_th2 = tail_fit(Th_sub, r, pw_th, r_ref)
            a2_fit = c_om2[1] * r_ref ** (2 / beta); b2_fit = c_th2[1] * r_ref ** (-(1 - 3 / beta))
            a1b = c_om2[0] * r_ref ** (1 / beta); b1b = c_th2[0] * r_ref ** (-(1 - 2 / beta))
            Psf, dPsf = cross_inverse(gs, cGf, torch.tensor([r_ref], dtype=DT, device=dev))
            Uf1a, Uf2a = velocity_from_modes(Psf.expand(-1, a.nphi), dPsf.expand(-1, a.nphi), xr, yr)
            Uf1a = Uf1a.cpu().numpy() / r_ref ** (1 - 1 / beta_f); Uf2a = Uf2a.cpu().numpy() / r_ref ** (1 - 1 / beta_f)
            extra = dict(method='two-pass: predicted source-induced terms subtracted with their exact exponents', source_tail_fit_rel_res=res_f,
                         source_leading_vel_rel_diff=float(np.linalg.norm(np.hypot(Uf1a - uf1, Uf2a - uf2)) / np.linalg.norm(np.hypot(uf1, uf2))),
                         a2_source_term_L2_over_own_pred=float(np.linalg.norm(a2_src) * r_ref ** (-1 / beta_f + 1 / beta) / max(np.linalg.norm(a2_pred), 1e-300)),
                         b2_source_term_L2_over_own_pred=float(np.linalg.norm(b2_src) * r_ref ** (-1 / beta_f + 1 / beta) / max(np.linalg.norm(b2_pred), 1e-300)),
                         fit_rel_res_after_subtraction=(res_om2, res_th2), leading_change_by_subtraction=(float(np.linalg.norm(a1b - a1) / np.linalg.norm(a1)), float(np.linalg.norm(b1b - b1) / np.linalg.norm(b1))))
        elif forcing is not None:
            # forcing tail: f = r^(-1/beta_f) a_f(phi); its leading velocity lam r^(1-1/beta_f) u_f; contributes lam u_f.grad Omega1 ~ r^(-1/beta-1/beta_f)
            _, lam_, bs, gs, beta_f, cGf = forcing
            Ff, Gf = fields_at(bs, beta_f, float(gs.L), gs.rmap, torch.zeros_like(cGf), cGf, X.reshape(-1), Y.reshape(-1))
            Omf = (X.reshape(-1) * Gf).reshape(a.nr, a.nphi).cpu().numpy()
            c_f, res_f = tail_fit(Omf, r, [-1 / beta_f, -2 / beta_f, -3 / beta_f, -1 - 1 / beta_f], r_ref); af1 = c_f[0] * r_ref ** (1 / beta_f)
            afk, ksf = sine_coeffs(af1, phi, min(a.kmax, bs.K + 2)); uf1, uf2 = homog_velocity(afk, ksf, 2 - 1 / beta_f, phi)
            # evaluated at r_ref: the term lam r^(1-1/beta_f) u_f . r^(-1/beta-1) grad = lam r^(-1/beta-1/beta_f) (...) ; expressed as an r^(-2/beta) coefficient at r_ref
            a2_src = (beta_f / beta) * lam_ * (uf1 * gx + uf2 * gy) * r_ref ** (-1 / beta - 1 / beta_f + 2 / beta)
            b2_src = (beta_f / beta) * lam_ * (uf1 * tx + uf2 * ty) * r_ref ** (-1 / beta_f + 1 / beta)          # r^(1-1/beta_f) r^(-2/beta) vs r^(1-3/beta)
            a2_pred = a2_pred + a2_src; b2_pred = b2_pred + b2_src
            # the forcing's own leading velocity vs the actual source velocity at r_ref
            Psf, dPsf = cross_inverse(gs, cGf, torch.tensor([r_ref], dtype=DT, device=dev))
            Uf1a, Uf2a = velocity_from_modes(Psf.expand(-1, a.nphi), dPsf.expand(-1, a.nphi), xr, yr)
            Uf1a = Uf1a.cpu().numpy() / r_ref ** (1 - 1 / beta_f); Uf2a = Uf2a.cpu().numpy() / r_ref ** (1 - 1 / beta_f)
            extra = dict(source_tail_fit_rel_res=res_f, source_leading_vel_rel_diff=float(np.linalg.norm(np.hypot(Uf1a - uf1, Uf2a - uf2)) / np.linalg.norm(np.hypot(uf1, uf2))),
                         a2_source_share=float(np.linalg.norm(a2_src) / max(np.linalg.norm(a2_pred), 1e-300)), b2_source_share=float(np.linalg.norm(b2_src) / max(np.linalg.norm(b2_pred), 1e-300)))
        def rel(x, y):
            return float(np.linalg.norm(x - y) / max(np.linalg.norm(y), 1e-300))
        w = dict(r1=r1, r2=r2, r_ref=r_ref, fit_rel_res_Omega=res_om, fit_rel_res_Theta=res_th, fit_cond_Omega=cond_om, fit_cond_Theta=cond_th,
                 leading=dict(a_L2=float(np.linalg.norm(a1) / np.sqrt(a.nphi)), b_L2=float(np.linalg.norm(b1) / np.sqrt(a.nphi)), a_k_first4=a_k[:4].tolist(), a_k_tail_ratio=float(abs(a_k[-1]) / max(abs(a_k).max(), 1e-300))),
                 leading_velocity_rel_diff_actual_vs_homog=vel_rel,
                 a2=dict(fit_L2=float(np.linalg.norm(a2_fit) / np.sqrt(a.nphi)), pred_L2=float(np.linalg.norm(a2_pred) / np.sqrt(a.nphi)), rel_diff=rel(a2_fit, a2_pred), ratio_to_leading_at_rref=float(np.linalg.norm(a2_fit) / np.linalg.norm(a1) * r_ref ** (-1 / beta))),
                 b2=dict(fit_L2=float(np.linalg.norm(b2_fit) / np.sqrt(a.nphi)), pred_L2=float(np.linalg.norm(b2_pred) / np.sqrt(a.nphi)), rel_diff=rel(b2_fit, b2_pred), ratio_to_leading_at_rref=float(np.linalg.norm(b2_fit) / np.linalg.norm(b1) * r_ref ** (-1 / beta))),
                 higher=dict(a3_L2_rel=float(np.linalg.norm(c_om[2]) / np.linalg.norm(c_om[0])), a_cv_L2_rel=float(np.linalg.norm(c_om[3]) / np.linalg.norm(c_om[0])), b3_L2_rel=float(np.linalg.norm(c_th[2]) / np.linalg.norm(c_th[0])), b_cv_L2_rel=float(np.linalg.norm(c_th[3]) / np.linalg.norm(c_th[0]))), **extra)
        out['windows'][f'{r1:.3g}-{r2:.3g}'] = w
    out['time_s'] = time.time() - t0
    js = json.dumps(out, indent=1, default=str); print(js)
    if a.out:
        open(a.out, 'w').write(js)


if __name__ == '__main__':
    main()
