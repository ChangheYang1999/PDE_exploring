"""Continuation parameterized by the temperature amplitude a0 (shift 2, 19:40Z): a0 is FIXED per stage and the homotopy
parameter eps becomes an unknown, determined by the strain condition ell(a0 G_char) = 1 + beta/2. This passes through
folds of the eps-branch (where a0(eps) has a vertical tangent). Unknown vector z = (x, eps_scale*eps); map:
  x -> fit(a0 G_char[x, eps]),   eps -> eps + kappa (ell - target),
accelerated by safeguarded Anderson. Each stage saves runs/<tag>_a0<a0>.npz (with its eps).
Usage: python3 code/picard_a0.py --state runs/cont1b_eps0.05.npz --a0_schedule 1.9,2.1,... --tag a0c1"""
import sys, os, time, argparse, math, hashlib, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual, code_hashes
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--state', type=str, required=True)
ap.add_argument('--a0_schedule', type=str, required=True)
ap.add_argument('--eps0', type=float, default=None, help='starting eps (default: from the state)')
ap.add_argument('--m', type=int, default=15); ap.add_argument('--mix', type=float, default=0.3)
ap.add_argument('--iters', type=int, default=40); ap.add_argument('--tag', type=str, default='a0c')
ap.add_argument('--tol_f', type=float, default=3e-5); ap.add_argument('--tol_obj', type=float, default=1e-5)
ap.add_argument('--kappa', type=float, default=0.025); ap.add_argument('--eps_scale', type=float, default=100.0)
ap.add_argument('--Nphi_res', type=int, default=12); ap.add_argument('--reg', type=float, default=1e-10)
ap.add_argument('--blow', type=float, default=5.0); ap.add_argument('--restart_every', type=int, default=12)
ap.add_argument('--max_resets', type=int, default=4); ap.add_argument('--stop_on_fail', type=int, default=1)
ap.add_argument('--eps_min', type=float, default=-0.5); ap.add_argument('--eps_max', type=float, default=1.5)
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# picard_a0 start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d = np.load(args.state)
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else bb
target = 1 + beta_fixed / 2
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=args.Nphi_res, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=6000, rmap=str(d['rmap']),
                   beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True; res.free_a0 = False          # a0 is fixed here; run() returns unit-amplitude transported fields
res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev)
cG = torch.tensor(d['cG'], dtype=DT, device=dev); act = res.active; cG[~act] = 0.0
eps = float(d['eps']) if args.eps0 is None else args.eps0
log(f"# start: eps={eps} a0_state={float(d['a0']) if 'a0' in d.files else float('nan'):.5f} target strain={target}")
x = cG[act].clone()
def evaluate(xa, eps_, a0):
    res.eps = float(min(max(eps_, args.eps_min), args.eps_max))
    full = torch.zeros_like(cG); full[act] = xa
    R, info = res.run(full[None], return_all=True)
    Gc = info['G_char'][0]
    xfit = res.PG @ (res.wG * a0 * Gc)
    ell = (xfit @ res.c_op_act).item()
    RG = res.wG * (a0 * Gc - info['G_rep'][0]); RF = a0 * info['RF'][0]
    obj = (RG ** 2).sum().item() + (RF ** 2).sum().item()
    return xfit - xa, ell, obj, RG, RF, info
def save(path, xa, eps_, a0, info, obj, extra):
    full = torch.zeros_like(cG); full[act] = xa
    np.savez(path, cG=full.cpu().numpy(), cF=(a0 * info['cF'][0]).cpu().numpy(), beta=info['beta'].item(), L=res.L, beta_basis=res.beta_basis,
             beta_fixed=beta_fixed, Nt=res.b.Nt, deg=res.b.deg, K=res.K, Nphi=res.b.Nphi, mreg=res.b.m_reg, ngc=res.ng, grade=res.grade,
             obj=obj, r_in=res.r_in, dt=res.dt, eps=eps_, rmap=res.rmap, cG_ext=res.cG_ext.cpu().numpy(), code_sha256=code_hashes(),
             scheme='mask', a0=a0, saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), solver='anderson_a0',
             start_path=args.state, start_sha256=hashlib.sha256(open(args.state, 'rb').read()).hexdigest(), **extra)
summary = []; t_all = time.time()
if args.a0_schedule == 'auto':
    a_start = float(d['a0']) if 'a0' in d.files else 1.0
    sched_a0 = []; v = a_start * 1.1
    while v <= 50.0:
        sched_a0.append(round(v, 4)); v *= 1.15
    log(f"# auto a0 schedule from {a_start:.4f}: {sched_a0}")
else:
    sched_a0 = [float(v) for v in args.a0_schedule.split(',')]
for a0 in sched_a0:
    log(f"# ---- a0 = {a0}")
    mix = args.mix; Zs, Fs = [], []; best = (float('inf'), None, None, None, None); resets = 0; hist = []; converged = False; t0 = time.time()
    z = torch.cat([x, torch.tensor([args.eps_scale * eps], dtype=DT, device=dev)])
    for it in range(args.iters):
        xa = z[:-1]; eps = z[-1].item() / args.eps_scale
        fx, ell, obj, RG, RF, info = evaluate(xa, eps, a0)
        feps = args.eps_scale * args.kappa * (ell - target)
        f = torch.cat([fx, torch.tensor([feps], dtype=DT, device=dev)])
        fn = f.norm().item()
        rr = res.gres.rr; nG = RG.abs()
        def reg_(v, lo, hi):
            mm = (rr >= lo) & (rr < hi); return v[mm].max().item() if mm.any() else float('nan')
        regs = ' '.join(f"{reg_(nG, lo, hi):.1e}" for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1e99)])
        log(f"it {it:3d} a0={a0} eps={eps:.6f} ell={ell:.6f} obj={obj:.6e} rms={(obj / (RG.numel() + RF.numel())) ** 0.5:.3e} |f|={fn:.3e} "
            f"max|wRG|={nG.max().item():.3e} max|wRF|={RF.abs().max().item():.3e} |x|max={xa.abs().max().item():.3e} unf={res.n_unfinished} mix={mix:.2f} regG={regs} t={time.time() - t0:.0f}s")
        score = obj + (args.eps_scale * (ell - target)) ** 2
        if math.isfinite(score) and score < best[0]:
            best = (score, z.clone(), info, obj, (eps, ell, fn))
        hist.append(score)
        if res.n_unfinished == 0 and ((fn < args.tol_f and abs(ell - target) < 1e-6) or (obj < args.tol_obj and abs(ell - target) < 1e-6) or \
           (len(hist) >= 4 and score < 1e-3 and abs(hist[-1] - hist[-4]) < 0.05 * hist[-4])):
            converged = True; best = (score, z.clone(), info, obj, (eps, ell, fn)); break      # save THIS iterate (verifier 20:23Z)
        if (not math.isfinite(score)) or score > args.blow * best[0]:
            resets += 1
            if resets > args.max_resets:
                log('# too many resets'); break
            mix = max(0.05, mix * 0.5); Zs, Fs = [], []; z = best[1].clone()
            log(f"# safeguard reset {resets}: back to best score={best[0]:.3e}, mix={mix:.2f}")
            continue
        if args.restart_every > 0 and it > 0 and it % args.restart_every == 0:
            Zs, Fs = [], []
        Zs.append(z.clone()); Fs.append(f.clone())
        if len(Zs) > args.m + 1:
            Zs.pop(0); Fs.pop(0)
        if len(Fs) >= 2:
            dF = torch.stack([Fs[i + 1] - Fs[i] for i in range(len(Fs) - 1)], 1)
            dZ = torch.stack([Zs[i + 1] - Zs[i] for i in range(len(Zs) - 1)], 1)
            A = dF.T @ dF; A = A + args.reg * torch.trace(A) / A.shape[0] * torch.eye(A.shape[0], dtype=DT, device=dev)
            gamma = torch.linalg.solve(A, dF.T @ f)
            z = z + mix * f - (dZ + mix * dF) @ gamma
        else:
            z = z + mix * f
        z[-1] = min(max(z[-1].item(), args.eps_scale * args.eps_min), args.eps_scale * args.eps_max)
    score_b, z_b, info_b, obj_b, (eps_b, ell_b, fn_b) = best
    if z_b is None:
        log('# stage produced no finite iterate'); break
    z = z_b.clone(); x = z[:-1].clone(); eps = eps_b
    save(f'runs/{args.tag}_a0{a0:g}.npz', x, eps, a0, info_b, obj_b, dict(converged=int(converged), stage_iters=it + 1, final_f=fn_b, ell=ell_b, Nphi_res=args.Nphi_res, c_self_saved=(res.g.c_op @ torch.cat([torch.zeros(0, dtype=DT, device=dev), (lambda full_: full_)(torch.zeros_like(cG).index_put_((torch.nonzero(act)[:, 0],), x))])).item()))
    summary.append((a0, eps, converged, it + 1, obj_b, ell_b, x.abs().max().item()))
    log(f"# stage a0={a0}: converged={converged} iters={it + 1} eps={eps:.6f} ell={ell_b:.6f} obj={obj_b:.4e} |x|max={x.abs().max().item():.3e} |f|={fn_b:.2e} time={time.time() - t0:.0f}s")
    if not converged and args.stop_on_fail:
        log('# continuation stopped at a non-converged stage'); break
log("# SUMMARY a0 eps converged iters obj ell |x|max")
for s in summary:
    log(f"#  {s[0]:.3f} {s[1]:.6f} {int(s[2])} {s[3]:3d} {s[4]:.4e} {s[5]:.6f} {s[6]:.3e}")
log(f"# picard_a0 done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} total {time.time() - t_all:.0f}s")
