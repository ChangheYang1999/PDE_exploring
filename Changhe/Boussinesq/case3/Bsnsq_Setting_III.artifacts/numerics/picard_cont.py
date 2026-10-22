"""Continuation in eps with the safeguarded Anderson-Picard solver (shift 2, 19:17Z).
At each eps of the schedule: Anderson(m, mix) on x -> fit(a0 G_char[x]) from the previous converged state; a stage stops
when |f| < tol_f, or when the objective is below tol_obj and stagnates; safeguard: if obj > 100 x best (or not finite)
the memory is reset to the best iterate and the mixing halved (at most 4 resets per stage). Each stage's state is saved
as runs/<tag>_eps<eps>.npz. Usage: python3 code/picard_cont.py --state runs/pic_e002.npz --eps_schedule 0.04,0.06,... --tag cont1"""
import sys, os, time, argparse, math, hashlib, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual, code_hashes
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--state', type=str, required=True)
ap.add_argument('--eps_schedule', type=str, default='', help='eps continuation (forcing homotopy)')
ap.add_argument('--lam_schedule', type=str, default='', help='defect-forcing path: W from Omega + lam (Omega_ext - Omega_S0), eps = 1, lam 1 -> 0; needs --s0')
ap.add_argument('--m', type=int, default=10); ap.add_argument('--mix', type=float, default=0.5)
ap.add_argument('--iters', type=int, default=40); ap.add_argument('--tag', type=str, default='cont')
ap.add_argument('--tol_f', type=float, default=3e-5); ap.add_argument('--tol_obj', type=float, default=1e-5)
ap.add_argument('--Nphi_res', type=int, default=12); ap.add_argument('--reg', type=float, default=1e-10)
ap.add_argument('--s0', type=str, default='', help='manufactured problem (Omega_f = Omega_ext - Omega_S0)')
ap.add_argument('--stop_on_fail', type=int, default=1)
ap.add_argument('--blow', type=float, default=100.0, help='reset memory (and halve mix) when obj > blow x best')
ap.add_argument('--restart_every', type=int, default=0, help='periodic Anderson memory restart (0 = never)')
ap.add_argument('--max_resets', type=int, default=4)
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# picard_cont start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d = np.load(args.state)
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else bb
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=args.Nphi_res, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=6000, rmap=str(d['rmap']),
                   beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True
res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None
cG = torch.tensor(d['cG'], dtype=DT, device=dev)
if args.s0:
    cG_S0 = torch.tensor(np.load(args.s0)['cG'], dtype=DT, device=dev); chi = res.cG_ext - cG_S0; res.cG_f = chi
act = res.active; cG[~act] = 0.0
x = cG[act].clone()
def Phi(xa):
    full = torch.zeros_like(cG); full[act] = xa
    R, info = res.run(full[None], return_all=True)
    cn = torch.zeros_like(cG); cn[act] = res.PG @ (res.wG * info['G_char'][0])
    return cn[act] - xa, R[0], info
def save(path, xa, info, obj, eps, extra):
    full = torch.zeros_like(cG); full[act] = xa
    np.savez(path, cG=full.cpu().numpy(), cF=info['cF'][0].cpu().numpy(), beta=info['beta'].item(), L=res.L, beta_basis=res.beta_basis,
             beta_fixed=beta_fixed, Nt=res.b.Nt, deg=res.b.deg, K=res.K, Nphi=res.b.Nphi, mreg=res.b.m_reg, ngc=res.ng, grade=res.grade,
             obj=obj, r_in=res.r_in, dt=res.dt, eps=eps, rmap=res.rmap, cG_ext=(res.cG_ext.cpu().numpy() if res.cG_ext is not None else np.zeros(0)),
             code_sha256=code_hashes(), scheme='mask', a0=info['a0'].item(), saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
             solver='anderson_cont', cG_f=(res.cG_f.cpu().numpy() if getattr(res, 'cG_f', None) is not None else np.zeros(0)),
             s0_path=(args.s0 or ''), s0_sha256=(hashlib.sha256(open(args.s0, 'rb').read()).hexdigest() if args.s0 else ''),
             start_path=args.state, start_sha256=hashlib.sha256(open(args.state, 'rb').read()).hexdigest(), **extra)
summary = []
t_all = time.time()
lam_mode = bool(args.lam_schedule)
sched = [float(v) for v in (args.lam_schedule if lam_mode else args.eps_schedule).split(',')]
for eps in sched:
    if lam_mode:
        res.eps = 1.0; res.cG_f = eps * chi      # 'eps' holds lambda in this mode
        log(f"# ---- lambda = {eps} (eps = 1, forcing chi scaled by lambda)")
    else:
        res.eps = eps
        log(f"# ---- eps = {eps}")
    mix = args.mix; Xs, Fs = [], []; best = (float('inf'), None, None, None); resets = 0; hist = []
    converged = False; t0 = time.time()
    for it in range(args.iters):
        f, R, info = Phi(x)
        obj = (R ** 2).sum().item(); fn = f.norm().item()
        nG = info['RG'][0].abs(); nF = info['RF'][0].abs(); rr = res.gres.rr
        def reg_(v, lo, hi):
            mm = (rr >= lo) & (rr < hi); return v[mm].max().item() if mm.any() else float('nan')
        regs = ' '.join(f"{reg_(nG, lo, hi):.1e}" for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1e99)])
        log(f"it {it:3d} eps={eps} obj={obj:.6e} rms={(obj / R.numel()) ** 0.5:.3e} |f|={fn:.3e} a0={info['a0'].item():.5f} max|wRG|={nG.max().item():.3e} "
            f"max|wRF|={nF.max().item():.3e} |x|max={x.abs().max().item():.3e} unf={res.n_unfinished} mix={mix:.2f} regG={regs} t={time.time() - t0:.0f}s")
        if math.isfinite(obj) and obj < best[0]:
            best = (obj, x.clone(), info, fn)
        hist.append(obj)
        if res.n_unfinished == 0 and (fn < args.tol_f or (obj < args.tol_obj) or (len(hist) >= 4 and obj < 1e-3 and abs(hist[-1] - hist[-4]) < 0.05 * hist[-4])):
            converged = True; best = (obj, x.clone(), info, fn); break      # save THIS iterate (verifier 20:23Z)
        if (not math.isfinite(obj)) or obj > args.blow * best[0]:
            resets += 1
            if resets > args.max_resets:
                log('# too many resets'); break
            mix = max(0.05, mix * 0.5); Xs, Fs = [], []; x = best[1].clone()
            log(f"# safeguard reset {resets}: back to best obj={best[0]:.3e}, mix={mix:.2f}")
            continue
        if args.restart_every > 0 and it > 0 and it % args.restart_every == 0:
            Xs, Fs = [], []
        Xs.append(x.clone()); Fs.append(f.clone())
        if len(Xs) > args.m + 1:
            Xs.pop(0); Fs.pop(0)
        if len(Fs) >= 2:
            dF = torch.stack([Fs[i + 1] - Fs[i] for i in range(len(Fs) - 1)], 1)
            dX = torch.stack([Xs[i + 1] - Xs[i] for i in range(len(Xs) - 1)], 1)
            A = dF.T @ dF; A = A + args.reg * torch.trace(A) / A.shape[0] * torch.eye(A.shape[0], dtype=DT, device=dev)
            gamma = torch.linalg.solve(A, dF.T @ f)
            x = x + mix * f - (dX + mix * dF) @ gamma
        else:
            x = x + mix * f
    # final state of the stage = best iterate
    obj_b, x_b, info_b, fn_b = best
    if x_b is None:
        log('# stage produced no finite iterate'); break
    x = x_b.clone()
    save(f'runs/{args.tag}_{"lam" if lam_mode else "eps"}{eps}.npz', x, info_b, obj_b, (1.0 if lam_mode else eps), dict(converged=int(converged), stage_iters=it + 1, final_f=fn_b, lam=(eps if lam_mode else 0.0), Nphi_res=args.Nphi_res))
    summary.append((eps, converged, it + 1, obj_b, info_b['a0'].item(), x.abs().max().item(), fn_b))
    log(f"# stage eps={eps}: converged={converged} iters={it + 1} obj={obj_b:.4e} a0={info_b['a0'].item():.5f} |x|max={x.abs().max().item():.3e} |f|={fn_b:.2e} "
        f"max|wRG|={info_b['RG'][0].abs().max().item():.2e} time={time.time() - t0:.0f}s")
    if not converged and args.stop_on_fail:
        log('# continuation stopped at a non-converged stage'); break
log("# SUMMARY eps converged iters obj a0 |x|max |f|")
for s in summary:
    log(f"#  {s[0]:.3f} {int(s[1])} {s[2]:3d} {s[3]:.4e} {s[4]:.5f} {s[5]:.3e} {s[6]:.2e}")
log(f"# picard_cont done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} total {time.time() - t_all:.0f}s")
