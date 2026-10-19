"""Newton on G(b) = b - Phi(b) = 0 (fixed c_l), Jacobian by batched finite differences (src/batchmap.py)."""
import sys, time, argparse, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, diag, batchmap
ap = argparse.ArgumentParser()
ap.add_argument('--cl', type=float, required=True); ap.add_argument('--start', type=str, default='')
ap.add_argument('--N', type=int, default=48); ap.add_argument('--M', type=int, default=10); ap.add_argument('--L', type=float, default=1.0)
ap.add_argument('--iters', type=int, default=15); ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6)
ap.add_argument('--eps', type=float, default=1e-5); ap.add_argument('--chunk', type=int, default=500); ap.add_argument('--tag', type=str, default='nm')
args = ap.parse_args()
dev = 'cuda'; base = ''
cl = args.cl; m = ipm1.IPM1(N=args.N, M=args.M, L=args.L, gamma=1 / cl, device=dev)
if args.start:
    m0, b, cl0, d0 = diag.load(base + args.start, device=dev)
else:
    r = m.rad.rR[:, None]; cos = m.ang.cos[None, :]
    b = 1 + 10 * r ** 2 / (m.L ** 2 + r ** 2) + 0 * cos
c = m.psi_xy0(m.fields(b)).item(); b = b * ((3 * cl - 1) / c); b[0, :] = 1.0
N, M = m.N, m.M; n = (N + 1) * M
free = torch.arange(M, n, device=dev)        # row 0 (centre) is fixed to 1
log = open(base + f'runs/{args.tag}.dat', 'w')

def G_and_info(bb):
    pb, info = batchmap.phi_batch(m, bb[None], cl, dt=args.dt, delta=args.delta)
    return (bb - pb[0]), info, pb[0]

for it in range(args.iters):
    t0 = time.time()
    G, info, pb = G_and_info(b)
    gn = G.reshape(-1)[free]
    nrm = gn.abs().max().item(); rel = nrm / b.abs().max().item()
    print(f"[NM] it {it}: |G|_inf={nrm:.4e} rel={rel:.3e}  x*={info['x_star'][0].item():.6f} mu1={info['mu1'][0].item():.5f} h(P)={info['h'][0].item():.6f} "
          f"C={info['C'][0].item():.4e} Lsc={info['Lsc'][0].item():.4f} ok={bool(info['ok'][0])} max b={b.abs().max().item():.4g} min b={b[1:].min().item():.3g}", flush=True)
    log.write(f"{it} {nrm:.6e} {rel:.6e} {info['x_star'][0].item():.8f} {info['mu1'][0].item():.6f} {info['h'][0].item():.8f} {info['C'][0].item():.6e} {info['Lsc'][0].item():.6f}\n"); log.flush()
    np.savez(base + f'runs/{args.tag}_it{it}.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=N, M=M, L=m.L, p=m.p, G=nrm, h=info['h'][0].item(), x_star=info['x_star'][0].item())
    if rel < 1e-9:
        print("converged"); break
    # FD Jacobian over free components, in chunks
    nf = len(free)
    J = torch.zeros(nf, nf, device=dev)
    bf = b.reshape(-1)
    tJ = time.time()
    for s in range(0, nf, args.chunk):
        e = min(nf, s + args.chunk)
        idxs = free[s:e]
        Bb = bf[None, :].repeat(e - s, 1)
        epsv = args.eps * torch.maximum(torch.ones(e - s, device=dev), bf[idxs].abs())
        Bb[torch.arange(e - s), idxs] += epsv
        pbB, infoB = batchmap.phi_batch(m, Bb.reshape(e - s, N + 1, M), cl, dt=args.dt, delta=args.delta)
        GB = Bb.reshape(e - s, N + 1, M) - pbB
        J[:, s:e] = ((GB.reshape(e - s, -1)[:, free] - gn[None, :]) / epsv[:, None]).T
        if not bool(infoB['has'].all()):
            print("   warning: some perturbed columns lost the stagnation point", flush=True)
    print(f"   Jacobian built in {time.time()-tJ:.0f}s", flush=True)
    sv = torch.linalg.svdvals(J)
    print(f"   singular values of dG: max {sv[0].item():.3e} min {sv[-1].item():.3e}", flush=True)
    d = torch.linalg.solve(J, -gn)
    # line search on |G|
    alpha = 1.0; best = None
    for _ in range(8):
        bt = b.clone(); bt.reshape(-1)[free] += alpha * d
        Gt, infot, _ = G_and_info(bt)
        nt = Gt.reshape(-1)[free].abs().max().item()
        print(f"   alpha={alpha:.3g}: |G|={nt:.4e}", flush=True)
        if nt < nrm:
            best = (bt, nt); break
        alpha *= 0.5
    if best is None:
        print("   no decrease; stopping"); break
    b = best[0]
    print(f"   step accepted, time {time.time()-t0:.0f}s", flush=True)
