"""Anderson-accelerated Picard iteration on the characteristic fixed point (shift 2, second solver for the same map).
Map: Phi(cG) = fit of a0*G_char(W[cG]) (active coefficients), exact strain by the a0 slaving; f(cG) = Phi(cG) - cG.
Anderson(m) with mixing parameter mix. Supports the manufactured problem (--s0 defines Omega_f) and the homotopy
problem (--state with its eps and cG_ext).
Usage: python3 code/picard.py --state runs/fb30i_eps0.1.npz --tag pic1 [--s0 runs/fb30g_eps0.npz --start ...]"""
import sys, os, time, argparse, hashlib, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual, code_hashes
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--state', type=str, required=True, help='state giving basis, eps, cG_ext and the start (unless --start)')
ap.add_argument('--start', type=str, default='')
ap.add_argument('--perturb', type=str, default='', help='"scale,f" applied to the start')
ap.add_argument('--s0', type=str, default='', help='manufactured problem: Omega_f = Omega_ext - Omega_S0 (then eps = 1)')
ap.add_argument('--eps', type=float, default=None)
ap.add_argument('--m', type=int, default=10); ap.add_argument('--mix', type=float, default=0.5)
ap.add_argument('--iters', type=int, default=100); ap.add_argument('--tag', type=str, default='pic')
ap.add_argument('--Nphi_res', type=int, default=12); ap.add_argument('--reg', type=float, default=1e-10)
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# picard start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d = np.load(args.state)
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else bb
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=args.Nphi_res, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=6000, rmap=str(d['rmap']),
                   beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True
res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None
res.eps = float(d['eps']) if args.eps is None else args.eps
cG = torch.tensor(np.load(args.start)['cG'] if args.start else d['cG'], dtype=DT, device=dev)
if args.s0:
    d0 = np.load(args.s0)
    cG_S0 = torch.tensor(d0['cG'], dtype=DT, device=dev)
    res.cG_f = res.cG_ext - cG_S0; res.eps = 1.0
    log(f"# manufactured: eps=1, Omega_f = Omega_ext - Omega_S0, |cG_f|max={res.cG_f.abs().max().item():.3e}")
if args.perturb:
    p = args.perturb.split(',')
    if p[0] == 'scale': cG = cG * float(p[1])
act = res.active; cG[~act] = 0.0
log(f"# eps={res.eps} beta_fixed={beta_fixed} Na={int(act.sum())}")
def Phi(c):
    R, info = res.run(c[None], return_all=True)
    cn = torch.zeros_like(c); cn[act] = res.PG @ (res.wG * info['G_char'][0])
    return cn, R[0], info
Xs, Fs = [], []           # histories of iterates (active part) and residuals f = Phi(x) - x
x = cG[act].clone()
t0 = time.time()
for it in range(args.iters):
    full = torch.zeros_like(cG); full[act] = x
    phi, R, info = Phi(full)
    f = phi[act] - x
    obj = (R ** 2).sum().item()
    nG = info['RG'][0].abs(); nF = info['RF'][0].abs(); rr = res.gres.rr
    def reg_(v, lo, hi):
        m = (rr >= lo) & (rr < hi); return v[m].max().item() if m.any() else float('nan')
    regs = ' '.join(f"{reg_(nG, lo, hi):.2e}/{reg_(nF, lo, hi):.2e}" for lo, hi in [(0, 1), (1, 10), (10, 100), (100, 1e99)])
    extra = ''
    if args.s0:
        extra = f" |x-S0|max={(res.cG_proj[0] - cG_S0).abs().max().item():.3e}"
    log(f"it {it:3d} obj={obj:.6e} rms={(obj / R.numel()) ** 0.5:.3e} |f|={f.norm().item():.3e} a0={info['a0'].item():.5f} "
        f"max|wRG|={nG.max().item():.3e} max|wRF|={nF.max().item():.3e} |x|max={x.abs().max().item():.3e} unfinished={res.n_unfinished} "
        f"regions={regs} t={time.time() - t0:.0f}s{extra}")
    Xs.append(x.clone()); Fs.append(f.clone())
    if len(Xs) > args.m + 1:
        Xs.pop(0); Fs.pop(0)
    if len(Fs) >= 2:
        dF = torch.stack([Fs[i + 1] - Fs[i] for i in range(len(Fs) - 1)], 1)      # (Na, mk)
        dX = torch.stack([Xs[i + 1] - Xs[i] for i in range(len(Xs) - 1)], 1)
        A = dF.T @ dF; A = A + args.reg * torch.trace(A) / A.shape[0] * torch.eye(A.shape[0], dtype=DT, device=dev)
        gamma = torch.linalg.solve(A, dF.T @ f)
        x = x + args.mix * f - (dX + args.mix * dF) @ gamma
    else:
        x = x + args.mix * f
    if not torch.isfinite(x).all():
        log('# diverged'); break
    full = torch.zeros_like(cG); full[act] = Xs[-1]      # the EVALUATED iterate (obj, cF, a0 belong to it), not the updated x
    np.savez(f'runs/{args.tag}.npz', cG=full.cpu().numpy(), cG_f=(res.cG_f.cpu().numpy() if getattr(res, 'cG_f', None) is not None else np.zeros(0)), s0_path=(args.s0 or ''), s0_sha256=(hashlib.sha256(open(args.s0, 'rb').read()).hexdigest() if args.s0 else ''), cF=info['cF'][0].cpu().numpy(), beta=info['beta'].item(), L=res.L,
             beta_basis=res.beta_basis, beta_fixed=beta_fixed, Nt=res.b.Nt, deg=res.b.deg, K=res.K, Nphi=res.b.Nphi, mreg=res.b.m_reg,
             ngc=res.ng, grade=res.grade, obj=obj, r_in=res.r_in, dt=res.dt, eps=res.eps, rmap=res.rmap,
             cG_ext=(res.cG_ext.cpu().numpy() if res.cG_ext is not None else np.zeros(0)), code_sha256=code_hashes(), scheme='mask',
             a0=info['a0'].item(), saved_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), solver='anderson')
log(f"# picard done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
