"""Newton on G(b) = b - Psi(b) = 0, where Psi is the doubly consistent characteristics map (c_l from h(P)=1, amplitude from
the identity, transport from P, renormalisation), on a fixed grid. Jacobian by batched finite differences (batchmap.psi_batch)."""
import sys, time, argparse, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, diag, batchmap
ap = argparse.ArgumentParser()
ap.add_argument('--start', type=str, required=True); ap.add_argument('--iters', type=int, default=12)
ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6)
ap.add_argument('--eps', type=float, default=1e-5); ap.add_argument('--chunk', type=int, default=480); ap.add_argument('--tag', type=str, default='nm3')
ap.add_argument('--cl_lo', type=float, default=1.05); ap.add_argument('--cl_hi', type=float, default=12.0)
args = ap.parse_args()
dev = 'cuda'; base = ''
m, b, cl0, d0 = diag.load(base + args.start, device=dev)
N, M, L = m.N, m.M, m.L; n = (N + 1) * M
free = torch.arange(M, n, device=dev)
log = open(base + f'runs/{args.tag}.dat', 'w'); log.write("# it |G|inf rel cl x* mu1 C Lsc smin smax\n")
def Psi(Bb):
    return batchmap.psi_batch(m, Bb, cl_lo=args.cl_lo, cl_hi=args.cl_hi, dt=args.dt, delta=args.delta)
for it in range(args.iters):
    t0 = time.time()
    pb, cl, info = Psi(b[None])
    if not bool(info['hasroot'][0]):
        print("[NM3] no root of h(P)=1 for the current shape; stop", flush=True); break
    G = (b - pb[0]).reshape(-1)[free]
    nrm = G.abs().max().item(); rel = nrm / b.abs().max().item()
    print(f"[NM3] it {it}: |G|_inf={nrm:.4e} rel={rel:.3e}  c_l={cl[0].item():.8f} x*={info['x_star'][0].item():.6f} (rescaled {info['x_star'][0].item()*info['Lsc'][0].item():.6f}) mu1={info['mu1'][0].item():.5f} "
          f"C={info['C'][0].item():.4e} Lsc={info['Lsc'][0].item():.4f} ok={bool(info['ok'][0])} max b={b.abs().max().item():.4g} min b={b[1:].min().item():.3g} b(inf)={(m.rad.ext1_R@b).abs().max().item():.4g} ({time.time()-t0:.0f}s)", flush=True)
    np.savez(base + f'runs/{args.tag}_it{it}.npz', b=b.cpu().numpy(), cl=cl[0].item(), gamma=m.gamma, N=N, M=M, L=L, p=m.p, G=nrm, x_star=info['x_star'][0].item(), mu1=info['mu1'][0].item(), Lsc=info['Lsc'][0].item(), C=info['C'][0].item())
    if rel < 1e-9:
        print("converged", flush=True); break
    nf = len(free); J = torch.zeros(nf, nf, device=dev); bf = b.reshape(-1); tJ = time.time()
    for s in range(0, nf, args.chunk):
        e = min(nf, s + args.chunk); idxs = free[s:e]
        Bb = bf[None, :].repeat(e - s, 1)
        epsv = args.eps * torch.maximum(torch.ones(e - s, device=dev), bf[idxs].abs())
        Bb[torch.arange(e - s), idxs] += epsv
        pbB, clB, infoB = Psi(Bb.reshape(e - s, N + 1, M))
        GB = (Bb.reshape(e - s, N + 1, M) - pbB).reshape(e - s, -1)[:, free]
        J[:, s:e] = ((GB - G[None, :]) / epsv[:, None]).T
        nbad = int((~infoB['hasroot']).sum())
        if nbad: print(f"   warning: {nbad} perturbed columns have no root", flush=True)
    sv = torch.linalg.svdvals(J)
    print(f"   Jacobian in {time.time()-tJ:.0f}s; singular values max {sv[0].item():.3e} min {sv[-1].item():.3e}; dc_l/db max {((clB - cl[0]).abs()/epsv).max().item():.3e}", flush=True)
    log.write(f"{it} {nrm:.6e} {rel:.6e} {cl[0].item():.10f} {info['x_star'][0].item():.8f} {info['mu1'][0].item():.6f} {info['C'][0].item():.6e} {info['Lsc'][0].item():.6f} {sv[-1].item():.4e} {sv[0].item():.4e}\n"); log.flush()
    d = torch.linalg.solve(J, -G)
    alpha = 1.0; accepted = False
    for _ in range(7):
        bt = b.clone(); bt.reshape(-1)[free] += alpha * d
        pbt, clt, infot = Psi(bt[None])
        if not bool(infot['hasroot'][0]):
            print(f"   alpha={alpha:.3g}: no root; halve", flush=True); alpha *= 0.5; continue
        Gt = (bt - pbt[0]).reshape(-1)[free]; nt = Gt.abs().max().item()
        print(f"   alpha={alpha:.3g}: |G|={nt:.4e} c_l={clt[0].item():.6f} min b={bt[1:].min().item():.3g}", flush=True)
        if nt < nrm:
            b, accepted = bt, True; break
        alpha *= 0.5
    if not accepted:
        print("   no decrease; stop", flush=True); break
    print(f"   accepted; iteration time {time.time()-t0:.0f}s", flush=True)
