"""BETA-PARAMETERIZED continuation of the additive-forcing lambda path (shift 4): beta is FIXED per stage (schedule), lambda is the
unknown found by a secant on the strain mismatch m(lambda) = c_self(lambda) - (1 + beta/2); the basis is retied to the stage beta.
Passes through a fold in lambda (lambda_min > 0) trivially. Derived from picard_beta.py (same inner solver, same source block).
Usage: python3 code/picard_lam.py --state runs/blam24v_lambda0.955.npz --ext_gauss 2.87,1.0 --a0 1.011258 --beta_schedule 3.0114,3.0163,... --tag blamB24 --Nphi_res 48 --fixed_source 1

Original picard_beta docstring: Gauge-fixed path (lead 19:22Z item 3, astra cont1 A): the temperature amplitude a0 is FIXED, beta is the unknown,
the representation (envelopes, radial map, inverse, fit operators) is rebuilt for every beta (beta_basis = beta), and
beta is determined per eps stage by a secant iteration on the strain mismatch m(beta) = ell(a0 G_char) - (1 + beta/2),
where ell is evaluated at the inner fixed point x = fit(a0 G_char[x; beta, eps]) (safeguarded Anderson, a0 fixed).
The external dipole of the forcing homotopy is refit for every beta with strain 1 + beta/2 (c_ext = 1 + beta/2).
Usage: python3 code/picard_beta.py --state runs/fb30g_eps0.npz --ext_gauss 2.87,1.0 --eps_schedule 0.02,0.04,... --tag bfree1"""
import sys, os, time, argparse, math, hashlib, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from charnewton import CharResidual, code_hashes
from fixedsrc import make_source_block, source_jets
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--state', type=str, required=True)
ap.add_argument('--ext_gauss', type=str, required=True, help='"y0,s" of the external dipole (amplitude refit per beta)')
ap.add_argument('--eps_schedule', type=str, default='', help='forcing-homotopy continuation in eps (beta free)')
ap.add_argument('--beta_schedule', type=str, required=True, help='fixed beta per stage; lambda is the unknown')
ap.add_argument('--save_secants', type=int, default=0, help='1: save every converged inner evaluation as runs/<tag>_beta<b>_sec<k>.npz')
ap.add_argument('--lam0', type=float, default=None, help='starting lambda (default: the lam of the state)'); ap.add_argument('--dlam', type=float, default=0.003, help='first secant step in lambda (taken downward)')
ap.add_argument('--lam_schedule', type=str, default='1', help='additive-forcing path (astra fold1 Q3): W = beta X + U[Omega + lam f], f = E - Omega_S fixed, eps = 1, lam 1 -> 0, beta free')
ap.add_argument('--predict', type=int, default=1, help='linear predictor of beta from the two previous stages')
ap.add_argument('--fixed_basis', type=int, default=0, help='1: keep the representation at the seed beta_basis (only the dynamical beta varies; f exactly fixed) -- DIAGNOSTIC ONLY (exponent frozen; verifier 22:48Z)')
ap.add_argument('--fixed_source', type=int, default=0, help='1: fixed SOURCE-VELOCITY block (lead 22:53Z): f stays in its seed representation, its velocity is added as a fixed block (fixedsrc.py); the unknown basis is retied to beta at every stage')
ap.add_argument('--accept_factor', type=float, default=3.0, help='stop if a stage fit floor exceeds accept_factor x the previous stage (lead 22:25Z)')
ap.add_argument('--a0', type=float, default=None, help='fixed amplitude (default: a0 of the state)')
ap.add_argument('--beta0', type=float, default=None); ap.add_argument('--dbeta', type=float, default=0.03)
ap.add_argument('--tol_m', type=float, default=5e-5); ap.add_argument('--max_secant', type=int, default=7)
ap.add_argument('--m', type=int, default=15); ap.add_argument('--mix', type=float, default=0.3)
ap.add_argument('--iters', type=int, default=40); ap.add_argument('--tag', type=str, default='bfree')
ap.add_argument('--tol_f', type=float, default=3e-5); ap.add_argument('--tol_obj', type=float, default=1e-5)
ap.add_argument('--Nphi_res', type=int, default=12); ap.add_argument('--reg', type=float, default=1e-10)
ap.add_argument('--ng_quad', type=int, default=12, help='Gauss points per radial quadrature cell of the modal Green inverse (12 = every earlier run; 48 for the shift-8 quadrature check)')
ap.add_argument('--blow', type=float, default=5.0); ap.add_argument('--restart_every', type=int, default=12); ap.add_argument('--max_resets', type=int, default=4)
ap.add_argument('--beta_min', type=float, default=2.005); ap.add_argument('--beta_max', type=float, default=8.0)
ap.add_argument('--max_steps', type=int, default=20000, help='RK4 step cap per characteristic trace (unfinished trajectories are flagged; a smaller cap fails a bad iterate fast)')
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# picard_beta start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d = np.load(args.state)
Nt, K, Nphi, grade, L = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L'])
rmap = str(d['rmap']); r_in = float(d['r_in']); dt = float(d['dt']); ngc = int(d['ngc']); deg = int(d['deg']); mreg = int(d['mreg'])
beta = (float(d['beta']) if ('beta' in d.files and float(d['beta']) > 0) else float(d['beta_basis'])) if args.beta0 is None else args.beta0   # start from the state's dynamical beta (a transplanted fixed-basis state has beta != beta_basis)
a0 = (float(d['a0']) if 'a0' in d.files else 1.0) if args.a0 is None else args.a0
y0, sg = [float(v) for v in args.ext_gauss.split(',')]
b = Basis(Nt, deg, K, Nphi, ng_coll=ngc, ng_quad=args.ng_quad, m_reg=mreg, device=dev, grade=grade)
log(f"# basis Nt={Nt} K={K} Nphi={Nphi} grade={grade} L={L} rmap={rmap} ng_quad={args.ng_quad}; start beta={beta} a0 fixed={a0:.6f}; dipole y0={y0} s={sg}")
# current fields are stored as (cF, cG) in the basis with beta_basis = cur_bb
cur_bb = float(d['beta_basis']); cF_cur = torch.tensor(d['cF'], dtype=DT, device=dev); cG_cur = torch.tensor(d['cG'], dtype=DT, device=dev)

lam_mode = bool(args.lam_schedule)
if lam_mode and 'source_mode' in d.files and str(d['source_mode']) == 'fixed_velocity_block' and not args.fixed_source:
    log('# NOTE: the input state was produced in fixed_velocity_block mode: enabling --fixed_source 1 automatically (astra fixedsrc1 item 9)')
    args.fixed_source = 1
seed_meta = {}
if lam_mode:
    if 'cG_f' in d.files and d['cG_f'].size and 'beta_seed' in d.files and float(d['beta_seed']) > 0:
        # restart from a saved lambda-stage: reuse the stored seed-basis source f and its basis exponent
        cG_fsrc = torch.tensor(d['cG_f'], dtype=DT, device=dev); bb_seed = float(d['beta_seed'])
        log(f"# lambda mode: reusing the stored seed source f (beta_seed = {bb_seed}) from {args.state}")
    else:
        cG_seed = cG_cur.clone(); cG_E = torch.tensor(d['cG_ext'], dtype=DT, device=dev); cG_fsrc = cG_E - cG_seed; bb_seed = cur_bb
    if 'seed_K' in d.files:
        # the source's OWN basis (verifier 00:56Z: a transplanted unknown basis must not reinterpret the seed source)
        seed_meta = dict(seed_K=int(d['seed_K']), seed_Nt=int(d['seed_Nt']), seed_deg=int(d['seed_deg']), seed_Nphi=int(d['seed_Nphi']), seed_ngc=int(d['seed_ngc']),
                         seed_mreg=int(d['seed_mreg']), seed_grade=float(d['seed_grade']), seed_L=float(d['seed_L']), seed_rmap=str(d['seed_rmap']))
    else:
        seed_meta = dict(seed_K=K, seed_Nt=Nt, seed_deg=deg, seed_Nphi=Nphi, seed_ngc=ngc, seed_mreg=mreg, seed_grade=grade, seed_L=L, seed_rmap=rmap)
        log('# lambda mode: no seed basis metadata in the state: the source basis is taken to be the current unknown basis (valid only if the state was never transplanted)')
    b_seed = b if all(seed_meta[k] == v for k, v in [('seed_K', K), ('seed_Nt', Nt), ('seed_deg', deg), ('seed_Nphi', Nphi), ('seed_ngc', ngc), ('seed_mreg', mreg), ('seed_grade', grade)]) else \
        Basis(seed_meta['seed_Nt'], seed_meta['seed_deg'], seed_meta['seed_K'], seed_meta['seed_Nphi'], ng_coll=seed_meta['seed_ngc'], ng_quad=args.ng_quad, m_reg=seed_meta['seed_mreg'], device=dev, grade=seed_meta['seed_grade'])
    assert cG_fsrc.numel() == seed_meta['seed_K'] * b_seed.Nb, 'seed source coefficient length does not match the seed basis'
    g_seed = Geometry(b_seed, bb_seed, seed_meta['seed_L'], rmap=seed_meta['seed_rmap'])
    log(f"# lambda mode: fixed physical source f = E - Omega_S in the seed basis (beta_S = {bb_seed}, {seed_meta}); strain(f) = {(g_seed.c_op @ cG_fsrc).item():+.3e} (should be ~0)")
    if args.fixed_source:
        assert not args.fixed_basis, 'choose one of --fixed_source / --fixed_basis'
        jets_f = source_jets(g_seed, cG_fsrc)
        log(f"# FIXED SOURCE-VELOCITY BLOCK: U_f from the seed representation (beta_basis {bb_seed}), interpolated in the seed's own t; unknown basis retied to beta at every stage. Source centre data: {jets_f}")

def build(beta_):
    """CharResidual for beta_basis = beta_ (or the seed basis if --fixed_basis), dynamical beta = beta_, external dipole refit
    with strain 1 + beta_/2, unit amplitude map."""
    bb_use = cur_bb if args.fixed_basis else beta_
    res = CharResidual(b, L, bb_use, Nphi_res=args.Nphi_res, r_in=r_in, dt=dt, device=dev, max_steps=args.max_steps, rmap=rmap, beta_fixed=beta_, wc=0.0, include_RF=True)
    res.use_graph = True; res.free_a0 = False
    g0 = res.g
    Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1.0 / Dt
    Gt = torch.exp(-(g0.x ** 2 + (g0.y - y0) ** 2) / (2 * sg ** 2))
    cfit = torch.zeros(K * b.Nb, dtype=DT, device=dev); act = g0.active
    cfit[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
    A = (1 + beta_ / 2) / (g0.c_op @ cfit).item()
    res.cG_ext = A * cfit
    if lam_mode:
        res.eps = 1.0
        if args.fixed_source:
            make_source_block(g_seed, cG_fsrc, res, build.lam)      # f exactly fixed; velocity block; basis retied (bb_use = beta_)
            res.cG_f = None
            return res
        if args.fixed_basis:
            res.cG_f = build.lam * cG_fsrc          # f exactly fixed in the seed representation
            return res
        _, cGf = transplant(res, bb_seed, torch.zeros_like(cG_fsrc), cG_fsrc)
        if abs(bb_seed - beta_) > 1e-14:
            Ff, Gf = fields_at(b, bb_seed, L, rmap, torch.zeros_like(cG_fsrc), cG_fsrc, g0.x, g0.y)
            DG = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
            err = ((g0.Phi0G @ cGf - Gf) / DG).abs().max().item()
            log(f"    # source f re-projected onto the beta={beta_:.6f} basis: weighted fit error {err:.2e}, strain {(g0.c_op @ cGf).item():+.3e}")
        res.cG_f = build.lam * cGf
    return res

def transplant(res, bb_from, cF_from, cG_from):
    """Re-project fields given in basis beta_basis = bb_from onto res.g (weighted LS on the collocation nodes)."""
    g = res.g
    if args.fixed_basis or abs(bb_from - res.beta_basis) < 1e-14:
        return cF_from.clone(), cG_from.clone()
    F, G = fields_at(b, bb_from, L, rmap, cF_from, cG_from, g.x, g.y)
    act = g.active
    DF = ((1 - b.t_coll_t) ** g.pF)[:, None].expand(b.Nc, b.Nphi).reshape(-1); DG = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
    cF = torch.zeros(K * b.Nb, dtype=DT, device=dev); cG = torch.zeros_like(cF)
    cF[act] = torch.linalg.lstsq((g.Phi0F / DF[:, None])[:, act], (F / DF)[:, None], driver='gels').solution[:, 0]
    cG[act] = torch.linalg.lstsq((g.Phi0G / DG[:, None])[:, act], (G / DG)[:, None], driver='gels').solution[:, 0]
    return cF, cG

def src_strain(res):
    src = getattr(res, 'src', None)
    return src['lam'] * src['c'] if src is not None else 0.0

def inner_solve(res, eps, x0):
    """Anderson on x -> fit(a0 G_char[x]) at fixed (beta_basis, eps, a0). Returns best (x, ell, obj, info, converged, iters)."""
    if not lam_mode:
        res.eps = eps
    act = res.active
    def evaluate(xa):
        full = torch.zeros(K * b.Nb, dtype=DT, device=dev); full[act] = xa
        R, info = res.run(full[None], return_all=True)
        Gc = info['G_char'][0]; xfit = res.PG @ (res.wG * a0 * Gc); ell = (xfit @ res.c_op_act).item()
        RG = res.wG * (a0 * Gc - info['G_rep'][0]); RF = a0 * info['RF'][0]
        return xfit - xa, ell, (RG ** 2).sum().item() + (RF ** 2).sum().item(), RG, RF, info
    x = x0.clone(); mix = args.mix; Xs, Fs = [], []; best = None; bestf = None; resets = 0; hist = []; converged = False; crit = 'none'
    for it in range(args.iters):
        f, ell, obj, RG, RF, info = evaluate(x); fn = f.norm().item()
        ell = ell + src_strain(res)      # total strain of the velocity-generating vorticity: fitted unknown + lam * c_f (c_f ~ 0)
        log(f"    in {it:3d} eps={eps} beta={res.beta_fixed:.6f} (basis {res.beta_basis:.4f}) obj={obj:.4e} |f|={fn:.3e} ell={ell:.6f} m={ell - 1 - res.beta_fixed / 2:+.6f} max|wRG|={RG.abs().max().item():.2e} max|wRF|={RF.abs().max().item():.2e} unf={res.n_unfinished} mix={mix:.2f}")
        cur = (x.clone(), ell, obj, info, fn, res.n_unfinished)      # the iterate carries its own unfinished count (astra fixedsrc1 item 8)
        if math.isfinite(obj) and (best is None or obj < best[2]):
            best = cur
        if math.isfinite(fn) and (bestf is None or fn < bestf[4]):
            bestf = cur
        hist.append(obj)
        # the convergence predicate is applied to THIS iterate and this iterate is returned (verifier 20:23Z)
        if fn < args.tol_f and res.n_unfinished == 0:
            converged = True; crit = 'fixed_point'; best = cur; break
        if obj < args.tol_obj and res.n_unfinished == 0:
            converged = True; crit = 'objective'; best = cur; break
        if res.n_unfinished == 0 and len(hist) >= 4 and obj < 1e-3 and abs(hist[-1] - hist[-4]) < 0.05 * hist[-4]:
            converged = True; crit = 'stagnation'; best = cur; break
        if (not math.isfinite(obj)) or obj > args.blow * best[2]:
            resets += 1
            if resets > args.max_resets:
                break
            mix = max(0.05, mix * 0.5); Xs, Fs = [], []; x = best[0].clone(); continue
        if args.restart_every > 0 and it > 0 and it % args.restart_every == 0:
            Xs, Fs = [], []
        Xs.append(x.clone()); Fs.append(f.clone())
        if len(Xs) > args.m + 1:
            Xs.pop(0); Fs.pop(0)
        if len(Fs) >= 2:
            dF = torch.stack([Fs[i + 1] - Fs[i] for i in range(len(Fs) - 1)], 1); dX = torch.stack([Xs[i + 1] - Xs[i] for i in range(len(Xs) - 1)], 1)
            A = dF.T @ dF; A = A + args.reg * torch.trace(A) / A.shape[0] * torch.eye(A.shape[0], dtype=DT, device=dev)
            gamma = torch.linalg.solve(A, dF.T @ f); x = x + mix * f - (dX + mix * dF) @ gamma
        else:
            x = x + mix * f
    if not converged and bestf is not None:
        best = bestf          # not converged: return the iterate with the smallest fixed-point defect
    return best + (converged, it + 1, crit)

summary = []; t_all = time.time(); hist_stage = []     # (beta, lambda) of converged stages for the predictor
assert lam_mode and args.fixed_source, 'picard_lam.py is for the additive-forcing path with the fixed source-velocity block'
sched = [float(v) for v in args.beta_schedule.split(',')]
lam = (float(d['lam']) if 'lam' in d.files else 1.0) if args.lam0 is None else args.lam0
log(f"# BETA-PARAMETERIZED continuation: beta schedule {sched}; start lambda {lam:.6f}; secant unknown = lambda at fixed beta")
for beta_s in sched:
    lam_try = lam
    if args.predict and len(hist_stage) >= 2:
        (b1, l1), (b2, l2) = hist_stage[-2], hist_stage[-1]
        if abs(b2 - b1) > 1e-12:
            lam_try = l2 + (l2 - l1) * (beta_s - b2) / (b2 - b1)
            lam_try = min(max(lam_try, l2 - 0.05), l2 + 0.05)
    log(f"# ---- beta = {beta_s}: secant in lambda from {lam_try:.6f} (previous stage lambda {lam:.6f})")
    t0 = time.time(); lams, ms, convs = [], [], []; sol = None; ok = False
    for k in range(args.max_secant):
        if lam_try < 0.0 or lam_try > 1.0:
            log(f"  # secant asked for lambda={lam_try:.6f}: CLIPPED to [0, 1] (recorded)")
        lam_try = min(max(lam_try, 0.0), 1.0)
        build.lam = lam_try
        res = build(beta_s)
        cF_t, cG_t = transplant(res, cur_bb, cF_cur, cG_cur)
        x_best, ell, obj, info, fn, unf_best, conv, nit, crit = inner_solve(res, lam_try, cG_t[res.active].clone())
        m = ell - (1 + beta_s / 2)
        log(f"  secant {k}: beta={beta_s:.6f} lambda={lam_try:.6f} m={m:+.6e} inner converged={conv} ({crit}) iters={nit} obj={obj:.3e} |f|={fn:.2e}")
        lams.append(lam_try); ms.append(m); convs.append(conv)
        full = torch.zeros(K * b.Nb, dtype=DT, device=dev); full[res.active] = x_best
        if getattr(args, 'save_secants', 0):
            # save EVERY converged inner evaluation (astra fold2: field continuity in beta/lambda must be checkable), same metadata as a stage
            np.savez(f'runs/{args.tag}_beta{beta_s}_sec{k}.npz', cG=full.cpu().numpy(), cF=(a0 * info['cF'][0]).cpu().numpy(), beta=beta_s, L=L, beta_basis=beta_s, beta_fixed=beta_s,
                     Nt=Nt, deg=deg, K=K, Nphi=Nphi, mreg=mreg, ngc=ngc, grade=grade, obj=obj, r_in=r_in, dt=dt, eps=1.0, lam=lam_try, cG_f=cG_fsrc.cpu().numpy(), beta_seed=bb_seed,
                     cG_f_effective=np.zeros(0), unfinished_selected=unf_best, rmap=rmap, source_mode='fixed_velocity_block', param='beta', secant_index=k,
                     src_strain=src_strain(res), src_jets=np.array([jets_f[kk_] for kk_ in ('c', 'h20', 'h30', 'h40', 'G0', 'g1p')]), **seed_meta,
                     cG_ext=res.cG_ext.cpu().numpy(), code_sha256=code_hashes(), scheme='mask', a0=a0, saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                     solver='anderson_lamfree_secant_point', strain_mismatch=m, converged=0, inner_f=fn, inner_converged=int(conv), inner_crit=crit, c_self_saved=(res.g.c_op @ full).item(),
                     c_target=1 + beta_s / 2, Nphi_res=args.Nphi_res, start_path=args.state, ext_gauss=np.array([y0, sg]))
        cur_tuple = (lam_try, full.clone(), m, a0 * info['cF'][0].clone(), obj, info, conv, res.cG_ext.clone(), fn, crit, (res.g.c_op @ full).item(), None, unf_best)
        if abs(m) < args.tol_m and conv:
            sol = cur_tuple
        elif sol is None or (abs(m) < abs(sol[2]) and not (abs(sol[2]) < args.tol_m and sol[6])):
            sol = cur_tuple
        cur_bb, cF_cur, cG_cur = beta_s, a0 * info['cF'][0].clone(), full.clone()
        if abs(m) < args.tol_m and conv:
            ok = True; break
        if k == 0:
            lam_try = lam_try - args.dlam
        else:
            dm = ms[-1] - ms[-2]
            step = -ms[-1] * (lams[-1] - lams[-2]) / dm if abs(dm) > 1e-14 else -args.dlam
            step = max(-0.05, min(0.05, step))
            lam_try = lams[-1] + step
            neg = [(ll_, mm_) for ll_, mm_, cv_ in zip(lams, ms, convs) if cv_ and mm_ < 0]
            pos = [(ll_, mm_) for ll_, mm_, cv_ in zip(lams, ms, convs) if cv_ and mm_ > 0]
            if neg and pos:
                ln = min(neg, key=lambda z: abs(z[1]))[0]; lp = min(pos, key=lambda z: abs(z[1]))[0]
                lo_, hi_ = min(ln, lp), max(ln, lp)
                if not (lo_ < lam_try < hi_):
                    lam_try = 0.5 * (lo_ + hi_)
                    log(f"  # secant step left the bracket [{lo_:.6f}, {hi_:.6f}]: using its midpoint {lam_try:.6f}")
    lam, full, m, cFsol, obj, info, conv, cGext, fn_sol, crit_sol, c_self_saved, cGf_eff, unf_sol = sol
    prev_obj = summary[-1][3] if summary else (float(d['obj']) if 'obj' in d.files and float(d['obj']) > 0 else None)
    rejected = bool(ok and prev_obj is not None and obj > args.accept_factor * prev_obj and obj > 1.0)
    accepted = bool(ok and not rejected)
    cur_bb, cF_cur, cG_cur = beta_s, cFsol, full
    if ok:
        hist_stage.append((beta_s, lam))
    np.savez(f'runs/{args.tag}_beta{beta_s}.npz', cG=full.cpu().numpy(), cF=cFsol.cpu().numpy(), beta=beta_s, L=L, beta_basis=beta_s, beta_fixed=beta_s,
             Nt=Nt, deg=deg, K=K, Nphi=Nphi, mreg=mreg, ngc=ngc, grade=grade, obj=obj, r_in=r_in, dt=dt, eps=1.0, lam=lam,
             cG_f=cG_fsrc.cpu().numpy(), beta_seed=bb_seed, cG_f_effective=np.zeros(0), unfinished_selected=unf_sol,
             forcing_note='FIXED SOURCE-VELOCITY BLOCK: W = beta X + U_rel[Omega] + lam U_rel[f], f = cG_f in the SEED basis (beta_seed) with its exact modal inverse; unknown basis retied: beta_basis = beta; BETA-PARAMETERIZED stage (beta fixed, lambda solved)',
             rmap=rmap, source_mode='fixed_velocity_block', param='beta',
             src_strain=src_strain(res), src_jets=np.array([jets_f[kk_] for kk_ in ('c', 'h20', 'h30', 'h40', 'G0', 'g1p')]),
             **seed_meta,
             cG_ext=cGext.cpu().numpy(), code_sha256=code_hashes(), scheme='mask', a0=a0, saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
             solver='anderson_lamfree', strain_mismatch=m, converged=int(ok), continuation_accepted=int(accepted), prev_stage_obj=(prev_obj if prev_obj is not None else -1.0), inner_f=fn_sol, inner_converged=int(conv), inner_crit=crit_sol,
             c_self_saved=c_self_saved, c_target=1 + beta_s / 2, Nphi_res=args.Nphi_res, start_path=args.state,
             start_sha256=hashlib.sha256(open(args.state, 'rb').read()).hexdigest(), ext_gauss=np.array([y0, sg]))
    summary.append((beta_s, lam, m, obj, ok))
    log(f"# stage beta={beta_s}: lambda={lam:.6f} m={m:+.3e} obj={obj:.3e} ok={ok} inner|f|={fn_sol:.2e} inner_conv={conv} ({crit_sol}) c_self_saved={c_self_saved:.6f} (target {1 + beta_s / 2:.6f}) |cG|max={full.abs().max().item():.3e} time={time.time() - t0:.0f}s")
    if not ok:
        log('# stage not converged: stopping'); break
    if rejected:
        log(f"# stage beta={beta_s} REJECTED by the fit-floor acceptance test: obj {obj:.3e} > {args.accept_factor} x {prev_obj:.3e}; saved with continuation_accepted=0. Stopping.")
        break
log(f"# SUMMARY beta lambda m obj ok")
for s_ in summary:
    log(f"#  {s_[0]:.6f} {s_[1]:.6f} {s_[2]:+.3e} {s_[3]:.3e} {int(s_[4])}")
log(f"# picard_lam done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} total {time.time() - t_all:.0f}s")
