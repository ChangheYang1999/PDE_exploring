"""Identity-preserving homotopy on the disk model (SPEC N3a closure), Newton with LM fallback; args: N M R [deps] [tag]."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1disk, solve
dev = 'cuda'; base = ''
N, M, R = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); deps0 = float(sys.argv[4]) if len(sys.argv) > 4 else 0.02
cl0 = 3.0; tag = f'disk_cl3_N{N}M{M}R{int(R)}'
m = ipm1disk.IPM1Disk(N=N, M=M, L=1.0, R=R, gamma=1 / cl0, device=dev); nw = solve.Newton(m, verbose=False, chunk=1024)
r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
b = one + (3 * cl0 - 1 - c1) / cs * s2; b[0, :] = 1.0; cl = cl0
print(f"[disk] N={N} M={M} R={R}: c[1]={c1:.6f} c[s2]={cs:.6f} A={(3*cl0-1-c1)/cs:.4f}", flush=True)
F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0); S0 = E0.clone(); S0[0, :] = 0
log = open(base + f'runs/{tag}.dat', 'w'); log.write("# eps |F| cl b(R)max min_b smin smax\n")
eps = 0.0; deps = deps0
while eps < 1.0 - 1e-12 and deps >= 0.0025:
    et = min(1.0, eps + deps); t1 = time.time()
    bt, clt, info = nw.solve(b, cl, hom=(et, S0, 0.0), tol=1e-10, maxit=25); method = 'newton'
    if not info['converged']:
        bt, clt, info = solve.levenberg_marquardt_hom(nw, b, cl, hom=(et, S0, 0.0), lam=1e-3, maxit=100, tol=1e-10); method = 'LM'
    nrm = info.get('nrm_inf', info.get('nrm', float('nan')))
    if not info['converged']:
        print(f"[disk] eps={et:.4f} {method} failed |F|={nrm:.2e}; halving step", flush=True); deps *= 0.5; continue
    b, cl, eps = bt, clt, et
    bR = (m.rad.ext1_R @ b).abs().max().item()
    smin = smax = float('nan')
    if any(abs(eps - e) < 1e-6 for e in [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]):
        F, fl = nw.residual_full(b, cl); J = nw.jacobian(b, cl, fl); sv = torch.linalg.svdvals(J); smin, smax = sv[-1].item(), sv[0].item()
        np.savez(base + f'runs/{tag}_eps{eps:.3f}.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=m.L, R=R, disk=True)
    print(f"[disk] eps={eps:.4f} {method:6s} |F|={nrm:.2e} c_l={cl:.8f} b(R)max={bR:.2f} min b={b[1:].min().item():.3g} smin/smax={smin:.2e}/{smax:.2e} ({time.time()-t1:.0f}s)", flush=True)
    log.write(f"{eps:.4f} {nrm:.6e} {cl:.10f} {bR:.6e} {b[1:].min().item():.6e} {smin:.4e} {smax:.4e}\n"); log.flush()
np.savez(base + f'runs/{tag}_last.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=m.L, R=R, disk=True)
print(f"[disk] done: final eps={eps:.4f}", flush=True)
