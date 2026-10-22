"""jacobian_fp.py -- finite-difference Jacobian of the INNER fixed-point map and the continuation Jacobian at a saved lambda-path state
(shift 6; prompt section 4: "check whether the Jacobian has neutral scaling directions, weak exponent directions, near-zero singular values").

Inner map (picard_lam.py / picard_beta.py, fixed source-velocity block, basis retied to beta):
    T(x) = PG (wG a0 G_char[P x; beta, lambda]),   x = active coefficients of G = Omega/x,
where P is the affine projection of x onto {c_op.x + lambda c_f = 1 + beta/2} along c_op (CharResidual.prepare) and PG is the weighted
least-squares fit of the transported G on the residual set. The saved state x* is an Anderson fixed point, |T(x*) - x*| ~ 1e-5.
The outer scalar equation is m(lambda; beta) = c_op.x*(lambda) + lambda c_f - 1 - beta/2 = 0 (secant in lambda or beta).

Computed here (all finite-difference, sampled, no interval bounds):
  1. J_T = dT/dx (forward differences, step h, batched evaluations of res.run), A = J_T - I.
  2. singular values of A (smallest, largest, condition number); eigenvalues of J_T (spectral radius of the plain Picard iteration;
     eigenvalues near 1 = near-kernel directions of A); mode/radius decomposition of the right singular vectors of the smallest singular values.
  3. parameter columns dT/dlambda, dT/dbeta (central differences; beta changes the retied basis, the coefficient vector fixed),
     dx*/dp = (I - J_T)^{-1} dT/dp, and the reduced derivatives
        m_lambda = c_op.dx*/dlambda + c_f,     m_beta = (dc_op/dbeta).x* + c_op.dx*/dbeta - 1/2
     to be compared with the secant estimates of the continuation runs.
  4. the exact spatial scaling direction of the divided field, v_s = PG(wG d/dl [l^-1 G(X/l)]|_1) = PG(wG (-G - X.grad G)) (Omega_l = Omega(X/l) gives
     G_l = l^-1 G(X/l); the forced fixed-a0 fixed-source problem does not have this symmetry; verifier P198):
     |A v_s|/|v_s| and the angle to the weakest singular directions.
  5. a step study (h = 1e-7, 1e-6, 1e-5) on 12 columns to quantify the FD error.
Usage: python3 code/jacobian_fp.py --state runs/mbb_b3.0952_lambda0.989973.npz --ext_gauss 2.5,1.0 --tag jacL2v [--batch 16] [--h 1e-6]
Outputs: runs/jac_<tag>.log, runs/jac_<tag>.json (summary), runs/jac_<tag>.npz (J_T, singular values/vectors, eigenvalues, parameter columns).
"""
import sys, os, time, argparse, math, json, hashlib, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from charnewton import CharResidual, code_hashes
from fixedsrc import make_source_block, source_jets
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--state', type=str, required=True)
ap.add_argument('--ext_gauss', type=str, required=True, help='"y0,s" of the external dipole (as in the continuation run)')
ap.add_argument('--a0', type=float, default=None)
ap.add_argument('--tag', type=str, required=True)
ap.add_argument('--h', type=float, default=1e-6, help='forward-difference step on the coefficients')
ap.add_argument('--batch', type=int, default=16)
ap.add_argument('--dl', type=float, default=1e-4, help='central step in lambda'); ap.add_argument('--db', type=float, default=1e-4, help='central step in beta')
ap.add_argument('--Nphi_res', type=int, default=None)
ap.add_argument('--timing_only', type=int, default=0, help='1: time T for batch sizes 1, 4, batch and exit')
ap.add_argument('--max_cols', type=int, default=0, help='debug: only the first n columns')
ap.add_argument('--step_study', type=int, default=1)
ap.add_argument('--n_sv', type=int, default=8, help='number of smallest singular directions analysed')
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/jac_{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# jacobian_fp start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d = np.load(args.state)
Nt, K, Nphi, grade, L = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L'])
rmap = str(d['rmap']); r_in = float(d['r_in']); dt = float(d['dt']); ngc = int(d['ngc']); deg = int(d['deg']); mreg = int(d['mreg'])
beta = float(d['beta']); lam = float(d['lam']); a0 = float(d['a0']) if args.a0 is None else args.a0
Nphi_res = int(d['Nphi_res']) if args.Nphi_res is None else args.Nphi_res
assert str(d['source_mode']) == 'fixed_velocity_block' and abs(float(d['beta_basis']) - beta) < 1e-12, 'expects a retied fixed-source-block lambda-path state'
y0, sg = [float(v) for v in args.ext_gauss.split(',')]
b = Basis(Nt, deg, K, Nphi, ng_coll=ngc, m_reg=mreg, device=dev, grade=grade)
cF_star = torch.tensor(d['cF'], dtype=DT, device=dev); cG_star = torch.tensor(d['cG'], dtype=DT, device=dev)
cG_fsrc = torch.tensor(d['cG_f'], dtype=DT, device=dev); bb_seed = float(d['beta_seed'])
seed_meta = dict(seed_K=int(d['seed_K']), seed_Nt=int(d['seed_Nt']), seed_deg=int(d['seed_deg']), seed_Nphi=int(d['seed_Nphi']), seed_ngc=int(d['seed_ngc']),
                 seed_mreg=int(d['seed_mreg']), seed_grade=float(d['seed_grade']), seed_L=float(d['seed_L']), seed_rmap=str(d['seed_rmap']))
b_seed = b if all(seed_meta[k] == v for k, v in [('seed_K', K), ('seed_Nt', Nt), ('seed_deg', deg), ('seed_Nphi', Nphi), ('seed_ngc', ngc), ('seed_mreg', mreg), ('seed_grade', grade)]) else \
    Basis(seed_meta['seed_Nt'], seed_meta['seed_deg'], seed_meta['seed_K'], seed_meta['seed_Nphi'], ng_coll=seed_meta['seed_ngc'], m_reg=seed_meta['seed_mreg'], device=dev, grade=seed_meta['seed_grade'])
g_seed = Geometry(b_seed, bb_seed, seed_meta['seed_L'], rmap=seed_meta['seed_rmap'])
jets_f = source_jets(g_seed, cG_fsrc); c_f = float(jets_f['c'])
log(f"# state {args.state}: beta={beta} lambda={lam} a0={a0} K={K} Nt={Nt} Nphi_res={Nphi_res} L={L} rmap={rmap}; seed beta {bb_seed}; source strain c_f={c_f:.6f}; stored m={float(d['strain_mismatch']):+.3e} inner|f|={float(d['inner_f']):.2e}")

def build(beta_, lam_):
    res = CharResidual(b, L, beta_, Nphi_res=Nphi_res, r_in=r_in, dt=dt, device=dev, max_steps=20000, rmap=rmap, beta_fixed=beta_, wc=0.0, include_RF=True)
    res.use_graph = True; res.free_a0 = False
    g0 = res.g
    Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1.0 / Dt
    Gt = torch.exp(-(g0.x ** 2 + (g0.y - y0) ** 2) / (2 * sg ** 2))
    cfit = torch.zeros(K * b.Nb, dtype=DT, device=dev); act = g0.active
    cfit[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
    A = (1 + beta_ / 2) / (g0.c_op @ cfit).item()
    res.cG_ext = A * cfit; res.eps = 1.0
    make_source_block(g_seed, cG_fsrc, res, lam_); res.cG_f = None
    return res

res0 = build(beta, lam)
act = res0.active; Nact = int(act.sum()); act_idx = torch.nonzero(act)[:, 0]
x_star = cG_star[act].clone()
log(f"# Nact={Nact} of {K * b.Nb}; Nq={res0.Nq}; PG {tuple(res0.PG.shape)}")

def T_batch(res, Xa):
    """Xa (B, Nact) -> T(Xa) (B, Nact); also the unfinished count."""
    Bn = Xa.shape[0]
    full = torch.zeros(Bn, K * b.Nb, dtype=DT, device=dev); full[:, act] = Xa
    R, info = res.run(full, return_all=True)
    Gc = info['G_char']
    xfit = (res.PG @ (res.wG[None] * a0 * Gc).T).T
    return xfit, res.n_unfinished, info

# ---- fixed-point defect and timing
t0 = time.time(); T0, unf, info0 = T_batch(res0, x_star[None]); torch.cuda.synchronize(); t1 = time.time() - t0
f0 = T0[0] - x_star
m0 = (x_star @ res0.c_op_act).item() + lam * c_f - 1 - beta / 2
log(f"# T(x*) - x*: |f0|={f0.norm().item():.3e} max={f0.abs().max().item():.3e} unfinished={unf}; m(x*)={m0:+.4e} (stored {float(d['strain_mismatch']):+.4e}); time B=1: {t1:.1f}s")
if args.timing_only:
    for Bn in [4, args.batch]:
        X = x_star[None].expand(Bn, -1).clone(); torch.cuda.synchronize(); t0 = time.time(); T_batch(res0, X); torch.cuda.synchronize()
        log(f"# timing B={Bn}: {time.time() - t0:.1f}s  ({(time.time() - t0) / Bn:.2f}s per column); GPU mem {torch.cuda.max_memory_allocated() / 2**30:.1f} GB")
    sys.exit(0)

# ---- step study on 12 columns
Nb = b.Nb
if args.step_study:
    cols = []
    for k in [0, 1, 3, 6]:
        ak = torch.nonzero((act_idx // Nb) == k)[:, 0]
        for frac in [0.1, 0.5, 0.9]:
            cols.append(int(ak[min(len(ak) - 1, int(frac * len(ak)))]))
    hs = [1e-7, 1e-6, 1e-5]
    E = []
    for j in cols:
        for h in hs:
            e = x_star.clone(); e[j] += h; E.append(e)
    TE, unfE, _ = T_batch(res0, torch.stack(E, 0))
    log(f"# step study (12 columns: active indices; k = mode, j = spline index; |D_h| and relative differences; unfinished={unfE})")
    log(f"{'col':>5} {'k':>2} {'j':>3} | " + ' '.join(f"{'|D_h| h=%.0e' % h:>14}" for h in hs) + " | rel.diff(1e-7,1e-6) (1e-6,1e-5)")
    i = 0; sd = []
    for j in cols:
        Ds = []
        for h in hs:
            Ds.append((TE[i] - T0[0]) / h); i += 1
        norms = [D.norm().item() for D in Ds]
        rd = [((Ds[a] - Ds[a + 1]).norm() / max(Ds[a + 1].norm().item(), 1e-300)).item() for a in range(len(hs) - 1)]
        gi = int(act_idx[j]); sd.append(dict(col=j, k=gi // Nb, j=gi % Nb, norms=norms, reldiff=rd))
        log(f"{j:5d} {gi // Nb:2d} {gi % Nb:3d} | " + ' '.join(f"{n:14.6e}" for n in norms) + " | " + ' '.join(f"{v:10.3e}" for v in rd))
else:
    sd = []

# ---- full forward-difference Jacobian
h = args.h; ncols = Nact if args.max_cols <= 0 else min(args.max_cols, Nact)
JT = torch.zeros(Nact, ncols, dtype=DT, device=dev); t_j = time.time(); unf_tot = 0
for s in range(0, ncols, args.batch):
    js = list(range(s, min(ncols, s + args.batch)))
    E = x_star[None].expand(len(js), -1).clone()
    for i, j in enumerate(js):
        E[i, j] += h
    TE, unfE, _ = T_batch(res0, E); unf_tot += unfE
    JT[:, js] = ((TE - T0[0][None]) / h).T
    if (s // args.batch) % 10 == 0:
        el = time.time() - t_j
        log(f"  cols {s}-{js[-1]} done, {el:.0f}s elapsed, eta {el / (js[-1] + 1) * (ncols - js[-1] - 1):.0f}s, unfinished so far {unf_tot}")
log(f"# Jacobian done: {ncols} columns in {time.time() - t_j:.0f}s; unfinished trajectories in the perturbed evaluations: {unf_tot}")
if ncols < Nact:
    np.savez(f'runs/jac_{args.tag}.npz', JT=JT.cpu().numpy(), x_star=x_star.cpu().numpy(), f0=f0.cpu().numpy(), act_idx=act_idx.cpu().numpy())
    log('# partial Jacobian saved (debug mode); exiting'); sys.exit(0)

# ---- analysis
I = torch.eye(Nact, dtype=DT, device=dev); A = JT - I
U, S, Vh = torch.linalg.svd(A)
S_np = S.cpu().numpy()
# the coefficient-space singular values depend on the coordinates (verifier P198); also report them in the FIELD metric of the weighted
# residual set: ||M x||, M = (wG Phi0G)[:, active] (Nq x Nact, full column rank), M = Q R => singular values of R A R^-1
Mw = (res0.gres.Phi0G * res0.wG[:, None])[:, act]
Rq = torch.linalg.qr(Mw, mode='r')[1] if hasattr(torch.linalg, 'qr') else None
A_field = Rq @ A @ torch.linalg.inv(Rq)
S_field = torch.linalg.svdvals(A_field).cpu().numpy()
log(f"# field-metric singular values of A (R A R^-1, M = Q R, M = weighted basis on the residual set; cond(R) = {torch.linalg.cond(Rq).item():.3e}): smallest {S_field[-args.n_sv:][::-1]}; largest {S_field[:3]}; condition number {S_field[0] / S_field[-1]:.3e}")
ev = torch.linalg.eigvals(JT); ev_np = ev.cpu().numpy(); rho = float(np.abs(ev_np).max())
near1 = np.sort(np.abs(ev_np - 1.0))[:args.n_sv]
log(f"# singular values of A = J_T - I: smallest {S_np[-args.n_sv:][::-1]}; largest {S_np[:3]}; condition number {S_np[0] / S_np[-1]:.3e}")
log(f"# eigenvalues of J_T: spectral radius {rho:.4f}; number with |ev| > 1: {int((np.abs(ev_np) > 1).sum())}; |ev - 1| smallest {near1}; number with |ev| > 0.5: {int((np.abs(ev_np) > 0.5).sum())}")
# the projection direction c_op (active): T is constant along it => J_T c = 0, A c = -c
c_act = res0.c_op_act.clone(); cn = c_act / c_act.norm()
log(f"# projection direction c_op: |J_T c|/|c| = {(JT @ cn).norm().item():.3e} (expected ~0 by construction), |A c|/|c| = {(A @ cn).norm().item():.4f} (expected 1)")
# mode/radius decomposition of the weakest right singular vectors
kk = (act_idx // Nb).cpu().numpy(); jj = (act_idx % Nb).cpu().numpy()
knots = np.asarray(b.knots); tcen = np.array([knots[j + 1:j + deg + 1].mean() for j in range(Nb)])   # Greville-like centres in t
g0 = res0.g
rcen = g0.r_of_t(torch.tensor(np.clip(tcen, 0, 1 - 1e-12), dtype=DT, device=dev))[0].cpu().numpy()
weak = []
for i in range(1, args.n_sv + 1):
    v = Vh[-i].cpu().numpy(); e = v ** 2
    by_k = np.bincount(kk, weights=e, minlength=K); by_j = np.bincount(jj, weights=e, minlength=Nb)
    topk = np.argsort(by_k)[::-1][:4]; topj = np.argsort(by_j)[::-1][:4]
    rmed = float(np.interp(0.5, np.cumsum(by_j) / by_j.sum(), rcen[:len(by_j)])) if by_j.sum() > 0 else float('nan')
    weak.append(dict(sigma=float(S_np[-i]), modes=[(int(k), float(by_k[k])) for k in topk], splines=[(int(j), float(by_j[j]), float(rcen[j])) for j in topj], r_median=rmed,
                     cos_c=float(abs(v @ cn.cpu().numpy()))))
    log(f"  sigma_{Nact - i + 1} = {S_np[-i]:.4e}: mode energies {[(int(k), round(float(by_k[k]), 3)) for k in topk]}; spline (index, energy, r) {[(int(j), round(float(by_j[j]), 3), float('%.3g' % rcen[j])) for j in topj]}; median r {rmed:.3g}; |cos(v, c_op)| {abs(v @ cn.cpu().numpy()):.3f}")
# ---- parameter columns
def T_at(beta_, lam_):
    res = build(beta_, lam_); Tv, unf_, _ = T_batch(res, x_star[None]); return Tv[0], res, unf_
Tlp, _, u1 = T_at(beta, lam + args.dl); Tlm, _, u2 = T_at(beta, lam - args.dl)
dT_dlam = (Tlp - Tlm) / (2 * args.dl)
Tbp, resbp, u3 = T_at(beta + args.db, lam); Tbm, resbm, u4 = T_at(beta - args.db, lam)
dT_dbeta = (Tbp - Tbm) / (2 * args.db)
dc_dbeta = (resbp.c_op_act - resbm.c_op_act) / (2 * args.db)
log(f"# parameter columns: |dT/dlambda|={dT_dlam.norm().item():.4e}, |dT/dbeta|={dT_dbeta.norm().item():.4e} (unfinished {u1 + u2 + u3 + u4}); |dc_op/dbeta . x*| = {(dc_dbeta @ x_star).item():+.4e}")
IA = I - JT
dx_dlam = torch.linalg.solve(IA, dT_dlam); dx_dbeta = torch.linalg.solve(IA, dT_dbeta)
m_lam = (c_act @ dx_dlam).item() + c_f
m_beta = (dc_dbeta @ x_star).item() + (c_act @ dx_dbeta).item() - 0.5
log(f"# REDUCED DERIVATIVES (Jacobian-based): m_lambda = c.dx*/dlambda + c_f = {(c_act @ dx_dlam).item():+.5f} + {c_f:.5f} = {m_lam:+.5f}; m_beta = {m_beta:+.5e}; dlambda/dbeta along m = 0: {-m_beta / m_lam:+.5e}")
log(f"#   |dx*/dlambda| = {dx_dlam.norm().item():.4e}, |dx*/dbeta| = {dx_dbeta.norm().item():.4e}; secant comparison: see the continuation logs (m_lambda ~ 2.8-3.3 and m_beta ~ 3.8e-4 at the lineage-2 vertex)")
# ---- scaling direction of the DIVIDED field (verifier P198): Omega_l = Omega(X/l) => G_l = l^-1 G(X/l), d/dl at l = 1: -G - X.grad G
e_s = 1e-4; gres = res0.gres
xs, ys = gres.x, gres.y
Fp, Gp = fields_at(b, beta, L, rmap, cF_star, cG_star, xs / (1 + e_s), ys / (1 + e_s))
Fm, Gm = fields_at(b, beta, L, rmap, cF_star, cG_star, xs / (1 - e_s), ys / (1 - e_s))
dG = (Gp / (1 + e_s) - Gm / (1 - e_s)) / (2 * e_s)
v_s = res0.PG @ (res0.wG * dG); v_s_n = v_s / v_s.norm()
Av = (A @ v_s_n).norm().item()
cos_weak = [float(abs((Vh[-i] @ v_s_n).item())) for i in range(1, args.n_sv + 1)]
# the fit residual of the scaling direction (how well -X.grad G is represented)
G_fit_err = ((res0.gres.Phi0G[:, act] @ v_s - dG) * res0.wG).abs().max().item() / max((res0.wG * dG).abs().max().item(), 1e-300)
log(f"# SCALING DIRECTION v_s = PG(wG dG/de), |v_s| = {v_s.norm().item():.4e}, weighted representation error {G_fit_err:.2e}: |A v_s|/|v_s| = {Av:.4f} (a neutral direction of T would give A v_s = 0, i.e. ratio 0); |cos| with the {args.n_sv} weakest singular directions {['%.3f' % c for c in cos_weak]}")
# component of v_s along c_op and the strain of the scaling direction
log(f"#   |cos(v_s, c_op)| = {abs((v_s_n @ cn).item()):.3f}; Rayleigh quotient v_s.J_T v_s/|v_s|^2 = {(v_s_n @ (JT @ v_s_n)).item():+.4f}")
# ---- how large is the 'exponent direction' dT/dbeta in the weak subspace?
w_b = dT_dbeta / dT_dbeta.norm(); w_l = dT_dlam / dT_dlam.norm()
cos_b = [float(abs((U[:, -i] @ w_b).item())) for i in range(1, args.n_sv + 1)]; cos_l = [float(abs((U[:, -i] @ w_l).item())) for i in range(1, args.n_sv + 1)]
log(f"# |cos| of dT/dbeta with the weakest LEFT singular directions {['%.3f' % c for c in cos_b]}; of dT/dlambda {['%.3f' % c for c in cos_l]}")
# Newton correction size: how far is x* from the exact fixed point of the discrete map (linearized)
dx_newton = torch.linalg.solve(IA, f0)
log(f"# linearized Newton correction |(I - J_T)^-1 f0| = {dx_newton.norm().item():.3e} (|x*| = {x_star.norm().item():.3e}); its strain change c.dx = {(c_act @ dx_newton).item():+.3e} (shift of m at the fixed point)")
summary = dict(sv_field_smallest=S_field[-args.n_sv:][::-1].tolist(), sv_field_largest=S_field[:3].tolist(), cond_field=float(S_field[0] / S_field[-1]), cond_R=float(torch.linalg.cond(Rq)), state=args.state, state_sha256=hashlib.sha256(open(args.state, 'rb').read()).hexdigest(), beta=beta, lam=lam, a0=a0, K=K, Nt=Nt, Nphi_res=Nphi_res, Nact=Nact, Nq=int(res0.Nq), h=h,
               f0_norm=float(f0.norm()), f0_max=float(f0.abs().max()), m_at_xstar=m0, c_f=c_f, sv_smallest=S_np[-args.n_sv:][::-1].tolist(), sv_largest=S_np[:3].tolist(), cond=float(S_np[0] / S_np[-1]),
               spectral_radius_JT=rho, n_ev_gt1=int((np.abs(ev_np) > 1).sum()), n_ev_gt05=int((np.abs(ev_np) > 0.5).sum()), ev_near1=near1.tolist(), JTc_norm=float((JT @ cn).norm()),
               weak_directions=weak, dT_dlam_norm=float(dT_dlam.norm()), dT_dbeta_norm=float(dT_dbeta.norm()), m_lambda=m_lam, m_beta=m_beta, dlam_dbeta=-m_beta / m_lam,
               dx_dlam_norm=float(dx_dlam.norm()), dx_dbeta_norm=float(dx_dbeta.norm()), scaling_Av=Av, scaling_cos_weak=cos_weak, scaling_fit_err=G_fit_err, scaling_rayleigh=float(v_s_n @ (JT @ v_s_n)),
               cos_dTdbeta_weakU=cos_b, cos_dTdlam_weakU=cos_l, newton_corr_norm=float(dx_newton.norm()), newton_corr_strain=float(c_act @ dx_newton), step_study=sd, unfinished_total=unf_tot,
               code_sha256=list(code_hashes()) if not isinstance(code_hashes(), dict) else code_hashes(), utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), total_time_s=time.time() - t0)
json.dump(summary, open(f'runs/jac_{args.tag}.json', 'w'), indent=1, default=str)
np.savez(f'runs/jac_{args.tag}.npz', JT=JT.cpu().numpy(), S=S_np, ev=ev_np, Vweak=Vh[-args.n_sv:].cpu().numpy(), Uweak=U[:, -args.n_sv:].cpu().numpy(), x_star=x_star.cpu().numpy(), f0=f0.cpu().numpy(),
         act_idx=act_idx.cpu().numpy(), dT_dlam=dT_dlam.cpu().numpy(), dT_dbeta=dT_dbeta.cpu().numpy(), dc_dbeta=dc_dbeta.cpu().numpy(), v_s=v_s.cpu().numpy(), c_act=c_act.cpu().numpy(), beta=beta, lam=lam, h=h)
log(f"# jacobian_fp done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}; summary runs/jac_{args.tag}.json, arrays runs/jac_{args.tag}.npz")
