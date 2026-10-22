"""axis_ode.py -- exact axis transport check (astra cone1 (b),(c)) for a stored state: on each half-axis (s = +1 upper y > 0, s = -1 lower),
v(r) = s W_2(0, s r), A(r) = d_x W_1(0, s r), H = Theta_xx(0, s r), g = Omega_x(0, s r) satisfy
    v' = 2 beta - A,   v H' = (beta - 2 - 2A) H,   v g' + (A + 1) g = H,   H(0) = 2 a0, g(0) = 4 a0/beta
(derived from the reduced equations at s = x^2 = 0 and div W = 2 beta). v and A are computed EXACTLY on the axis from the modal data
of the velocity-generating vorticity (unknown in its basis + source block in the seed basis + eps mixing), the ODEs are integrated in
r, and H, g are compared with the solver's transported fields at near-axis points (x = eps_a r): an independent test of the characteristic
solver on the axis. Also q(r) = g r^{1+1/beta} (the axis slope scaled; its limit is Q of 4.21), the closed form
H = (2 a0/kappa^2) v^2/zeta^2, g = (2 a0/kappa^2) v zeta^{-p} int_0^r zeta^{-rho}, zeta = r exp int_0^r (kappa/v - 1/s) ds, kappa = 3 beta/2 + 1,
p = (2 beta + 1)/kappa, rho = (beta + 1)/kappa, and the estimate Q = (2 a0 beta/kappa^2) C^{-p} int_0^inf zeta^{-rho} with zeta ~ C r^{kappa/beta}.
Usage: python3 code/axis_ode.py state.npz [--rmax 1e8] [--n 80]"""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual
from fixedsrc import cross_inverse, velocity_from_modes
torch.set_default_dtype(DT)


def axis_fields(blocks, r):
    """v_up, A_up, v_down, A_down (numpy) at radii r (torch) from the velocity blocks [(geometry, coefficients, weight)]: exact axis formulas
    U_2(0, +r) = -(1/r) sum k (-1)^k Psi_k, U_2(0, -r) = (1/r) sum k Psi_k, d_x U_1(0, +r) = (1/r) sum k (-1)^k (Psi_k' - Psi_k/r),
    d_x U_1(0, -r) = (1/r) sum k (Psi_k' - Psi_k/r)."""
    U2u = torch.zeros_like(r); U2d = torch.zeros_like(r); dU1u = torch.zeros_like(r); dU1d = torch.zeros_like(r)
    for g, c, w in blocks:
        Psi, dPsi = cross_inverse(g, c, r)
        K = Psi.shape[0]; k = torch.arange(1, K + 1, dtype=DT, device=r.device)[:, None]; sg = (-1.0) ** k
        U2u += w * (-(k * sg * Psi).sum(0) / r); U2d += w * ((k * Psi).sum(0) / r)
        dU1u += w * ((k * sg * (dPsi - Psi / r)).sum(0) / r); dU1d += w * ((k * (dPsi - Psi / r)).sum(0) / r)
    return U2u, dU1u, U2d, dU1d


def main(path, rmax=1e8, n=80, eps_a=1e-5):
    dev = 'cuda'
    d = np.load(path)
    Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
    beta = float(d['beta']) if 'beta' in d.files and float(d['beta']) > 0 else bb
    rmap = str(d['rmap'])
    b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
    g = Geometry(b, bb, L, rmap=rmap)
    cG = torch.tensor(d['cG'], dtype=DT, device=dev); cF = torch.tensor(d['cF'], dtype=DT, device=dev)
    a0 = float(cF[0]); eps = float(d['eps']) if 'eps' in d.files else 1.0; lam = float(d['lam']) if 'lam' in d.files else 0.0
    source_mode = str(d['source_mode']) if 'source_mode' in d.files else ''
    # the solver transports with the unknown coefficients PROJECTED onto the exact centre-strain constraint c_unk + lam c_f = 1 + beta/2
    # (CharResidual.prepare); use the same projected coefficients here (astra path1), and report the projection size
    c_f = 0.0
    if source_mode == 'fixed_velocity_block' and d['cG_f'].size:
        from fixedsrc import source_jets
        if 'seed_K' in d.files:
            _bs = Basis(int(d['seed_Nt']), int(d['seed_deg']), int(d['seed_K']), int(d['seed_Nphi']), ng_coll=int(d['seed_ngc']), m_reg=int(d['seed_mreg']), device=dev, grade=float(d['seed_grade']))
            _gs = Geometry(_bs, float(d['beta_seed']), float(d['seed_L']), rmap=str(d['seed_rmap']))
        else:
            _gs = Geometry(b, float(d['beta_seed']), L, rmap=rmap)
        c_f = source_jets(_gs, torch.tensor(d['cG_f'], dtype=DT, device=dev))['c']
    dvec = g.c_op * g.active.to(DT)
    target = 1 + beta / 2 - lam * c_f
    c_raw = float(cG @ g.c_op)
    cG = cG + dvec * ((target - cG @ g.c_op) / (g.c_op @ dvec))
    blocks = [(g, cG, eps)]
    if eps != 1.0 and d['cG_ext'].size:
        blocks.append((g, torch.tensor(d['cG_ext'], dtype=DT, device=dev), 1.0 - eps))
    src_block = None
    if source_mode == 'fixed_velocity_block' and d['cG_f'].size:
        if 'seed_K' in d.files:
            bs = Basis(int(d['seed_Nt']), int(d['seed_deg']), int(d['seed_K']), int(d['seed_Nphi']), ng_coll=int(d['seed_ngc']), m_reg=int(d['seed_mreg']), device=dev, grade=float(d['seed_grade']))
            gs = Geometry(bs, float(d['beta_seed']), float(d['seed_L']), rmap=str(d['seed_rmap']))
        else:
            gs = Geometry(b, float(d['beta_seed']), L, rmap=rmap)
        cGf = torch.tensor(d['cG_f'], dtype=DT, device=dev); blocks.append((gs, cGf, lam)); src_block = (gs, cGf, lam)
    elif 'cG_f_effective' in d.files and d['cG_f_effective'].size:
        blocks.append((g, torch.tensor(d['cG_f_effective'], dtype=DT, device=dev), 1.0))
    elif 'cG_f' in d.files and d['cG_f'].size:
        blocks.append((g, torch.tensor(d['cG_f'], dtype=DT, device=dev), lam if lam > 0 else 1.0))
    # ---- axis velocity data on a fine log grid
    rg = torch.tensor(np.logspace(-4, np.log10(rmax), 1200), dtype=DT, device=dev)
    U2u, dU1u, U2d, dU1d = axis_fields(blocks, rg)
    rn = rg.cpu().numpy()
    v_up = beta * rn + U2u.cpu().numpy(); A_up = beta + dU1u.cpu().numpy()
    v_dn = beta * rn - U2d.cpu().numpy(); A_dn = beta + dU1d.cpu().numpy()
    # sanity: finite-difference check of the axis formulas (velocity_from_modes at x = eps_a r) at a few radii
    chk = {}
    for ri in [0.5, 5.0, 500.0]:
        rr = torch.tensor([ri], dtype=DT, device=dev)
        for s_, name in [(1.0, 'up'), (-1.0, 'down')]:
            U1 = 0.0; U2 = 0.0
            for gg, c, w in blocks:
                Psi, dPsi = cross_inverse(gg, c, rr)
                x = rr * eps_a; y = s_ * rr * np.sqrt(1 - eps_a ** 2)
                u1, u2 = velocity_from_modes(Psi, dPsi, x, y); U1 += w * float(u1[0]); U2 += w * float(u2[0])
            # formula evaluated at exactly ri (the grid values v_up[i] sit at rn[i] != ri)
            U2u_, dU1u_, U2d_, dU1d_ = axis_fields(blocks, rr)
            if name == 'up':
                chk[f'{name}_r{ri:g}'] = dict(dU1dx_formula=float(dU1u_[0]), dU1dx_fd=U1 / (ri * eps_a), U2_formula=float(U2u_[0]), U2_fd=U2)
            else:
                chk[f'{name}_r{ri:g}'] = dict(dU1dx_formula=float(dU1d_[0]), dU1dx_fd=U1 / (ri * eps_a), U2_formula=float(U2d_[0]), U2_fd=U2)
    # div check v' = 2 beta - A on the grid (log-derivative)
    def divdef(v, A):
        dv = np.gradient(v, rn); return float(np.abs(dv - (2 * beta - A)).max() / (2 * beta))
    # ---- ODE integration on each half-axis
    out = dict(file=path, beta=beta, beta_basis=bb, a0=a0, lam=lam, eps=eps, source_mode=source_mode, axis_formula_check=chk,
               strain_projection=dict(c_raw=c_raw, c_target_unknown=target, shift=float(target - c_raw)),
               div_defect_rel=dict(up=divdef(v_up, A_up), down=divdef(v_dn, A_dn)),
               note='Q_closed_form_est is a FINITE-CUTOFF estimate at r = rmax (trapezoid on the log grid; ~0.1 percent quadrature bias, outer tail ~ rmax^{-1/beta} not added)')
    kappa = 1.5 * beta + 1; p_ = (2 * beta + 1) / kappa; rho = (beta + 1) / kappa
    r_eval = np.logspace(-2, np.log10(rmax * 0.5), n)
    res_axis = {}
    for name, v, A in [('up', v_up, A_up), ('down', v_dn, A_dn)]:
        lv = CubicSpline(np.log(rn), np.log(v)); Ai = CubicSpline(np.log(rn), A)
        def rhs(lr, y):
            r_ = np.exp(lr); vv = np.exp(lv(lr)); AA = Ai(lr)
            H, gg = y
            return [r_ * (beta - 2 - 2 * AA) * H / vv, r_ * (H - (AA + 1) * gg) / vv]
        r0 = 1e-3
        sol = solve_ivp(rhs, [np.log(r0), np.log(r_eval[-1])], [2 * a0, 4 * a0 / beta], t_eval=np.log(r_eval), method='DOP853', rtol=1e-11, atol=1e-14)
        H_ode, g_ode = sol.y
        # closed form via zeta
        integrand = kappa / v - 1.0 / rn
        cum = np.concatenate([[0.0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(rn))])      # int_{rmin}^r (kappa/v - 1/s) ds; rmin = 1e-4 (tail below ~0)
        zeta = rn * np.exp(cum)
        Cfit = zeta / rn ** (kappa / beta)
        inner = np.concatenate([[0.0], np.cumsum(0.5 * (zeta[1:] ** (-rho) + zeta[:-1] ** (-rho)) * np.diff(rn))]) + rn[0] ** (1 - rho) / (1 - rho)   # int_0^r zeta^-rho (zeta ~ r near 0)
        H_cf = (2 * a0 / kappa ** 2) * v ** 2 / zeta ** 2
        g_cf = (2 * a0 / kappa ** 2) * v * zeta ** (-p_) * inner
        Q_est = (2 * a0 * beta / kappa ** 2) * Cfit[-1] ** (-p_) * inner[-1]            # with int_0^inf ~ int_0^rmax (tail ~ rmax^{-1/beta}, slow)
        q_cf = g_cf * rn ** (1 + 1 / beta)
        res_axis[name] = dict(H_ode=[float(x) for x in H_ode], g_ode=[float(x) for x in g_ode], q_ode=[float(x) for x in g_ode * r_eval ** (1 + 1 / beta)],
                              C_zeta_at_rmax=float(Cfit[-1]), Q_closed_form_est=float(Q_est), C_factor=float(Cfit[-1] ** (-p_)), I_R=float(inner[-1]), prefactor=float(2 * a0 * beta / kappa ** 2), q_closed_form_at=[float(np.interp(np.log(rr_), np.log(rn), q_cf)) for rr_ in [1e2, 1e4, 1e6, 1e8]],
                              closed_form_vs_ode_relH=float(np.max(np.abs(np.interp(np.log(r_eval), np.log(rn), H_cf) / H_ode - 1))),
                              closed_form_vs_ode_relg=float(np.max(np.abs(np.interp(np.log(r_eval), np.log(rn), g_cf) / g_ode - 1))),
                              v_over_beta_r_at=[float(np.interp(np.log(rr_), np.log(rn), v / (beta * rn))) for rr_ in [1, 10, 100, 1e4, 1e6, 1e8]],
                              A_over_beta_at=[float(np.interp(np.log(rr_), np.log(rn), A / beta)) for rr_ in [1, 10, 100, 1e4, 1e6, 1e8]])
    out['r_eval'] = [float(x) for x in r_eval]
    # ---- transported fields of the solver at near-axis points (x = eps_c r, y = +-r), unit amplitude, with the state's own cF
    res = CharResidual(b, L, bb, Nphi_res=4, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=20000, rmap=rmap, beta_fixed=beta, wc=0.0, include_RF=True)
    res.use_graph = True; res.free_a0 = False
    res.eps = eps; res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None
    if src_block is not None:
        from fixedsrc import make_source_block
        make_source_block(src_block[0], src_block[1], res, src_block[2])
    elif 'cG_f_effective' in d.files and d['cG_f_effective'].size:
        res.cG_f = torch.tensor(d['cG_f_effective'], dtype=DT, device=dev)
    elif 'cG_f' in d.files and d['cG_f'].size:
        res.cG_f = (lam if lam > 0 else 1.0) * torch.tensor(d['cG_f'], dtype=DT, device=dev)
    eps_c = 1e-4
    rr = torch.tensor(r_eval, dtype=DT, device=dev)
    X0 = torch.cat([torch.stack([eps_c * rr, rr * np.sqrt(1 - eps_c ** 2)], 1), torch.stack([eps_c * rr, -rr * np.sqrt(1 - eps_c ** 2)], 1)], 0)
    res.X0 = X0; res.Nq = X0.shape[0]; res.custom_points = True; res.cF_fixed = cF / a0
    _, info = res.run(cG[None], return_all=True)
    Fc = (a0 * info['F_char'][0]).cpu().numpy(); Gc = (a0 * info['G_char'][0]).cpu().numpy()
    out['unfinished'] = res.n_unfinished
    for i_, name in enumerate(['up', 'down']):
        H_char = 2 * Fc[i_ * n:(i_ + 1) * n]; g_char = Gc[i_ * n:(i_ + 1) * n]
        ra = res_axis[name]
        ra['H_char'] = [float(x) for x in H_char]; ra['g_char'] = [float(x) for x in g_char]
        ra['rel_diff_H'] = [float(x) for x in np.abs(H_char / np.array(ra['H_ode']) - 1)]
        ra['rel_diff_g'] = [float(x) for x in np.abs(g_char / np.array(ra['g_ode']) - 1)]
        ra['q_char'] = [float(x) for x in g_char * r_eval ** (1 + 1 / beta)]
    out['axis'] = res_axis
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--rmax', type=float, default=1e8); ap.add_argument('--n', type=int, default=80)
    a = ap.parse_args()
    o = main(a.state, a.rmax, a.n)
    print(json.dumps(o, indent=1))
