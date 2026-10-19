"""Newton on the extended characteristics fixed-point system on a FIXED grid (gamma_grid, p fixed):
   unknowns z = (b_free, c_l);  G(z) = [ b - Phi_{c_l}(A b) ;  h(P)(A b, c_l) - 1 ],  A = (3c_l-1)/c[b] (input amplitude fix).
Jacobian: batched FD over b_free (src/batchmap.py), one extra evaluation for the c_l column. Line search on |G|_inf."""
import sys, time, argparse, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, diag, batchmap
ap = argparse.ArgumentParser()
ap.add_argument('--start', type=str, required=True); ap.add_argument('--cl', type=float, default=None)
ap.add_argument('--iters', type=int, default=15); ap.add_argument('--dt', type=float, default=0.01); ap.add_argument('--delta', type=float, default=1e-6)
ap.add_argument('--eps', type=float, default=1e-5); ap.add_argument('--chunk', type=int, default=600); ap.add_argument('--tag', type=str, default='nm2')
ap.add_argument('--regrid', type=int, default=1)
args = ap.parse_args()
dev = 'cuda'; base = ''
m, b, cl0, d0 = diag.load(base + args.start, device=dev)
cl = args.cl if args.cl is not None else cl0
N, M, L = m.N, m.M, m.L; n = (N + 1) * M
free = torch.arange(M, n, device=dev)
log = open(base + f'runs/{args.tag}.dat', 'w'); log.write("# it |G|inf cl x* mu1 h C Lsc\n")

def G_batch(Bb, cls):
    """Bb: (B, N+1, M) inputs; cls: (B,) c_l values (all equal to one scalar per call here). Returns G_b (B, N+1, M), hres (B,), info."""
    c_in = m.psi_xy0(m.fields(Bb))                       # (B,)
    A = (3 * cls - 1) / c_in
    pb, info = batchmap.phi_batch(m, A[:, None, None] * Bb, float(cls[0]), dt=args.dt, delta=args.delta)
    return Bb - pb, info['h'] - 1.0, info

for outer in range(3 if args.regrid else 1):
    for it in range(args.iters):
        t0 = time.time()
        Gb, hres, info = G_batch(b[None], torch.tensor([cl], device=dev))
        g = torch.cat([Gb[0].reshape(-1)[free], hres])
        nrm = g.abs().max().item(); nb = Gb[0].reshape(-1)[free].abs().max().item() / b.abs().max().item()
        print(f"[NM2] it {it}: |G|_inf={nrm:.4e} (b part rel {nb:.3e}, h-1={hres[0].item():+.3e})  c_l={cl:.8f} x*={info['x_star'][0].item():.6f} mu1={info['mu1'][0].item():.5f} "
              f"C={info['C'][0].item():.4e} Lsc={info['Lsc'][0].item():.4f} ok={bool(info['ok'][0])} max b={b.abs().max().item():.4g} min b={b[1:].min().item():.3g} grid gamma={m.gamma:.5f}", flush=True)
        log.write(f"{it} {nrm:.6e} {cl:.10f} {info['x_star'][0].item():.8f} {info['mu1'][0].item():.6f} {info['h'][0].item():.8f} {info['C'][0].item():.6e} {info['Lsc'][0].item():.6f}\n"); log.flush()
        np.savez(base + f'runs/{args.tag}_o{outer}_it{it}.npz', b=b.cpu().numpy(), cl=cl, gamma=m.gamma, N=N, M=M, L=L, p=m.p, G=nrm, h=info['h'][0].item(), x_star=info['x_star'][0].item())
        if nrm < 1e-9:
            print("converged", flush=True); break
        nf = len(free)
        J = torch.zeros(nf + 1, nf + 1, device=dev)
        bf = b.reshape(-1)
        tJ = time.time()
        for s in range(0, nf, args.chunk):
            e = min(nf, s + args.chunk); idxs = free[s:e]
            Bb = bf[None, :].repeat(e - s, 1)
            epsv = args.eps * torch.maximum(torch.ones(e - s, device=dev), bf[idxs].abs())
            Bb[torch.arange(e - s), idxs] += epsv
            GB, hB, infoB = G_batch(Bb.reshape(e - s, N + 1, M), torch.full((e - s,), cl, device=dev))
            J[:nf, s:e] = ((GB.reshape(e - s, -1)[:, free] - g[None, :nf]) / epsv[:, None]).T
            J[nf, s:e] = (hB - g[nf]) / epsv
            if not bool(infoB['has'].all()):
                print("   warning: some perturbed columns lost P", flush=True)
        epsc = 1e-6 * max(1.0, abs(cl))
        Gc, hc, _ = G_batch(b[None], torch.tensor([cl + epsc], device=dev))
        J[:nf, nf] = (Gc[0].reshape(-1)[free] - g[:nf]) / epsc; J[nf, nf] = (hc[0] - g[nf]) / epsc
        sv = torch.linalg.svdvals(J)
        print(f"   Jacobian in {time.time()-tJ:.0f}s; singular values max {sv[0].item():.3e} min {sv[-1].item():.3e}", flush=True)
        dz = torch.linalg.solve(J, -g)
        alpha = 1.0; accepted = False
        for _ in range(7):
            bt = b.clone(); bt.reshape(-1)[free] += alpha * dz[:nf]; clt = cl + alpha * dz[nf].item()
            if clt <= 1.02:
                alpha *= 0.5; continue
            Gt, ht, infot = G_batch(bt[None], torch.tensor([clt], device=dev))
            gt = torch.cat([Gt[0].reshape(-1)[free], ht]); nt = gt.abs().max().item()
            print(f"   alpha={alpha:.3g}: |G|={nt:.4e} (c_l={clt:.6f}, h-1={ht[0].item():+.3e})", flush=True)
            if nt < nrm:
                b, cl, accepted = bt, clt, True; break
            alpha *= 0.5
        if not accepted:
            print("   no decrease; stopping this Newton loop", flush=True); break
        print(f"   accepted, iteration time {time.time()-t0:.0f}s", flush=True)
    if not args.regrid or abs(1 / cl - m.gamma) < 1e-6:
        break
    # re-grid: new model with gamma = 1/c_l; transfer b by interpolation in r (bounded function)
    import charac
    fe_old = charac.FieldEval(m, b, cl)
    m2 = ipm1.IPM1(N=N, M=M, L=L, gamma=1 / cl, device=dev)
    t_old = fe_old.t_of_r(m2.rad.rR[1:]); Pm = fe_old.radial_interp_matrix(t_old)
    b2 = torch.ones(N + 1, M, device=dev); b2[1:] = Pm @ b
    # account for the change of weight w (b = a / w): a is the physical function
    w_old_on_new = (1 + m2.rad.rR[1:] ** 2 / L ** 2) ** ((m.gamma - 3) / 2); w_new = m2.wR[1:]
    b2[1:] = b2[1:] * (w_old_on_new / w_new)[:, None]
    b, m = b2, m2
    print(f"[NM2] re-gridded to gamma = {m.gamma:.6f}", flush=True)
