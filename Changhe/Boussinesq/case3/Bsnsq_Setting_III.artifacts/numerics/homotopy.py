"""Forcing homotopy (lead NOTES 13:49Z item 4c): W_eps = beta X + U_rel[eps Omega + (1-eps) Omega_ext].
eps = 0: linear problem, cG = fit(G_char[W_ext]); then LM at increasing eps from the previous solution."""
import sys, os, time, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual, lm_solve
torch.set_default_dtype(DT)

ap = argparse.ArgumentParser()
ap.add_argument('--beta_basis', type=float, default=3.0); ap.add_argument('--L', type=float, default=1.5)
ap.add_argument('--Nt', type=int, default=32); ap.add_argument('--K', type=int, default=12)
ap.add_argument('--Nphi', type=int, default=24); ap.add_argument('--Nphi_res', type=int, default=12)
ap.add_argument('--ngc', type=int, default=7); ap.add_argument('--grade', type=float, default=1.5)
ap.add_argument('--dt', type=float, default=0.02); ap.add_argument('--r_in', type=float, default=1e-3)
ap.add_argument('--max_steps', type=int, default=6000)
ap.add_argument('--ext_gauss', type=str, required=True, help='"cin,y0,s"')
ap.add_argument('--eps_schedule', type=str, default='0.25,0.5,0.75,1.0')
ap.add_argument('--iters', type=int, default=12); ap.add_argument('--batch', type=int, default=64)
ap.add_argument('--lam', type=float, default=1e-2); ap.add_argument('--tik', type=float, default=0.0)
ap.add_argument('--dfloor', type=float, default=1e-3); ap.add_argument('--maxstep', type=float, default=None)
ap.add_argument('--init', type=str, default='', help='start from this state (cG) instead of the eps=0 fit')
ap.add_argument('--tag', type=str, default='hom')
ap.add_argument('--maxtime', type=float, default=1.2e4)
ap.add_argument('--broyden_every', type=int, default=1)
ap.add_argument('--tik_k', type=float, default=0.0)
ap.add_argument('--rmap', type=str, default='r', choices=['r', 'r2'])
ap.add_argument('--graph', type=int, default=1)
ap.add_argument('--beta_fixed', type=float, default=None, help='fix beta (= beta_basis recommended); centre constraint row')
ap.add_argument('--wc', type=float, default=0.0)
ap.add_argument('--no_RF', action='store_true')
args = ap.parse_args()
dev = 'cuda'
logf = open(f'runs/{args.tag}.log', 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
log(f"# homotopy start {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {vars(args)}")
b = Basis(args.Nt, 5, args.K, args.Nphi, ng_coll=args.ngc, m_reg=2, device=dev, grade=args.grade)
res = CharResidual(b, args.L, args.beta_basis, Nphi_res=args.Nphi_res, r_in=args.r_in, dt=args.dt, device=dev, max_steps=args.max_steps, rmap=args.rmap,
                   beta_fixed=args.beta_fixed, wc=args.wc, include_RF=not args.no_RF)
res.use_graph = bool(args.graph)
g0 = res.g; K, Nb = b.K, b.Nb; act = g0.active
cin, y0, sg = [float(v) for v in args.ext_gauss.split(',')]
Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1.0 / Dt
Gt = torch.exp(-(g0.x ** 2 + (g0.y - y0) ** 2) / (2 * sg ** 2))
cfit = torch.zeros(K * Nb, dtype=DT, device=dev)
cfit[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
A = cin / (g0.c_op @ cfit).item()
res.cG_ext = A * cfit
log(f"# ext: A={A:.5f} y0={y0} s={sg} c_in={cin} fit err {((g0.Phi0G @ cfit - Gt) * wfit).abs().max().item():.2e}")
if args.init:
    cG = torch.tensor(np.load(args.init)['cG'], dtype=DT, device=dev)
else:
    res.eps = 0.0
    R, info = res.run(torch.zeros(1, K * Nb, dtype=DT, device=dev), return_all=True)
    wG = res.wG
    PG = torch.linalg.pinv((res.gres.Phi0G * wG[:, None])[:, act], rtol=1e-12)
    cG = torch.zeros(K * Nb, dtype=DT, device=dev); cG[act] = PG @ (wG * info['G_char'][0])
    if args.beta_fixed is not None:
        d = g0.c_op * act.to(DT); cG = cG + d * ((1 + args.beta_fixed / 2 - cG @ g0.c_op) / (g0.c_op @ d))
        log(f"# eps=0 fit projected onto c = 1 + beta/2: c = {(g0.c_op @ cG).item():.6f}")
    log(f"# eps=0: beta={info['beta'].item():.6f} a0={info['a0'].item():.6f} c_out={(g0.c_op @ cG).item():.6f} unfinished={res.n_unfinished} "
        f"G fit err {(wG * (res.gres.Phi0G @ cG - info['G_char'][0])).abs().max().item():.2e}")
    np.savez(f'runs/{args.tag}_eps0.npz', cG=cG.cpu().numpy(), cF=info['cF'][0].cpu().numpy(), beta=info['beta'].item(), L=res.L,
             beta_basis=res.beta_basis, beta_fixed=-1.0, Nt=b.Nt, deg=b.deg, K=K, Nphi=b.Nphi, mreg=b.m_reg, ngc=res.ng,
             grade=res.grade, obj=0.0, r_in=res.r_in, dt=res.dt, eps=0.0, cG_ext=res.cG_ext.cpu().numpy(), rmap=res.rmap)
t_start = time.time()
for eps in [float(v) for v in args.eps_schedule.split(',')]:
    res.eps = eps
    log(f"# ---- eps = {eps}")
    cG, info = lm_solve(res, cG, iters=args.iters, lam=args.lam, batch=args.batch, log=log, save=f'runs/{args.tag}_eps{eps}.npz',
                        maxtime=max(60, args.maxtime - (time.time() - t_start)), tik=args.tik, dfloor=args.dfloor, maxstep=args.maxstep,
                        broyden_every=args.broyden_every, tik_k=args.tik_k)
log(f"# homotopy done {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
