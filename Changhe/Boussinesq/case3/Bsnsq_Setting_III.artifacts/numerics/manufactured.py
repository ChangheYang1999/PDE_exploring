"""Manufactured nonlinear test of the characteristic LM (shift 2, 2026-10-20T19:00Z).
Velocity source Omega_unk + Omega_f with Omega_f = Omega_ext - Omega_S0 fixed, S0 a saved state whose cG fits
a0*G_char under W_ext (an eps = 0 state). Then cG_S0 is an exact solution of the eps = 1 problem up to its fit error,
and the LM, started from a different state, must converge to it (same nonlinear structure as the B2 problem).
Usage: python3 code/manufactured.py --s0 runs/fb30g_eps0.npz --start runs/other_eps0.npz --tag man1 [LM options]"""
import sys, os, time, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual, lm_solve
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('--s0', type=str, required=True, help='state defining the manufactured solution (cG, cG_ext, basis params)')
ap.add_argument('--start', type=str, default='', help='starting state (cG); default: perturbation of s0')
ap.add_argument('--perturb', type=str, default='scale,0.7', help='if no --start: "scale,f" (cG*f) or "noise,rel,seed"')
ap.add_argument('--tag', type=str, default='man')
ap.add_argument('--iters', type=int, default=12); ap.add_argument('--batch', type=int, default=64)
ap.add_argument('--lam', type=float, default=1e-2); ap.add_argument('--tik', type=float, default=1e-6)
ap.add_argument('--tik_k', type=float, default=6.0); ap.add_argument('--dfloor', type=float, default=1e-2)
ap.add_argument('--maxstep', type=float, default=20.0); ap.add_argument('--broyden_every', type=int, default=3)
ap.add_argument('--Nphi_res', type=int, default=12); ap.add_argument('--maxtime', type=float, default=1.2e4)
ap.add_argument('--eval_only', action='store_true', help='only evaluate the residual at s0 and at the start')
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# manufactured start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
d0 = np.load(args.s0)
Nt, K, Nphi, grade, L, bb = int(d0['Nt']), int(d0['K']), int(d0['Nphi']), float(d0['grade']), float(d0['L']), float(d0['beta_basis'])
beta_fixed = float(d0['beta_fixed']) if float(d0['beta_fixed']) > 0 else bb
rmap = str(d0['rmap']); r_in = float(d0['r_in']); dt = float(d0['dt']); ngc = int(d0['ngc'])
log(f"# basis from s0: Nt={Nt} K={K} Nphi={Nphi} grade={grade} L={L} beta_basis={bb} beta_fixed={beta_fixed} rmap={rmap} r_in={r_in} dt={dt}")
b = Basis(Nt, int(d0['deg']), K, Nphi, ng_coll=ngc, m_reg=int(d0['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=args.Nphi_res, r_in=r_in, dt=dt, device=dev, max_steps=6000, rmap=rmap,
                   beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True
cG_S0 = torch.tensor(d0['cG'], dtype=DT, device=dev)
cG_ext = torch.tensor(d0['cG_ext'], dtype=DT, device=dev)
res.eps = 1.0
res.cG_ext = cG_ext
res.cG_f = cG_ext - cG_S0
log(f"# strain of S0: {(res.g.c_op @ cG_S0).item():.6f}; strain of ext: {(res.g.c_op @ cG_ext).item():.6f}; |cG_f|max={res.cG_f.abs().max().item():.3e}")
R0, info0 = res.run(cG_S0[None], return_all=True)
log(f"# residual at S0 (must be the fit error only): obj={(R0[0]**2).sum().item():.3e} max|wRG|={info0['RG'][0].abs().max().item():.3e} "
    f"max|wRF|={info0['RF'][0].abs().max().item():.3e} a0={info0['a0'].item():.6f} unfinished={res.n_unfinished}")
if args.start:
    cG = torch.tensor(np.load(args.start)['cG'], dtype=DT, device=dev)
else:
    p = args.perturb.split(',')
    if p[0] == 'scale':
        cG = cG_S0 * float(p[1])
    else:
        gen = torch.Generator(device='cpu').manual_seed(int(p[2]))
        cG = cG_S0 * (1 + float(p[1]) * torch.randn(cG_S0.shape, generator=gen).to(dev))
cG[~res.active] = 0.0
R1, info1 = res.run(cG[None], return_all=True)
log(f"# residual at start: obj={(R1[0]**2).sum().item():.3e} rms={(R1[0]**2).mean().sqrt().item():.3e} a0={info1['a0'].item():.6f} "
    f"|cG-cG_S0|max={(res.cG_proj[0]-cG_S0).abs().max().item():.3e} unfinished={res.n_unfinished}")
if args.eval_only:
    sys.exit(0)
cG, info = lm_solve(res, cG, iters=args.iters, lam=args.lam, batch=args.batch, log=log, save=f'runs/{args.tag}.npz', maxtime=args.maxtime,
                    tik=args.tik, dfloor=args.dfloor, maxstep=args.maxstep, broyden_every=args.broyden_every, tik_k=args.tik_k)
err = (res.cG_proj[0] - cG_S0)
log(f"# final: |cG-cG_S0|max={err.abs().max().item():.3e} rel={(err.norm()/cG_S0.norm()).item():.3e} a0={info['a0'].item():.6f} (S0 a0={info0['a0'].item():.6f})")
log(f"# manufactured done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
