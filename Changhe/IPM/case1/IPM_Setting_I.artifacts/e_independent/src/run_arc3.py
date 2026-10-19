"""Resolution study of the identity-preserving homotopy fold (dealiased code): for several (N, M), start b0 = 1 + A s2 with
3c_l0 - 1 = c[b0], follow the branch by pseudo-arclength, log eps, c_l, smin(J), sign det J, amplitude and the angular
spectrum decay of b (ratio of the top EE coefficient to the largest)."""
import sys, time, math, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; base = ''
cl0 = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0
beta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
grids = [(48, 10), (64, 16), (96, 24), (128, 32)] if len(sys.argv) < 3 else [tuple(int(v) for v in g.split('x')) for g in sys.argv[2].split(',')]
for (N, M) in grids:
    t0 = time.time()
    m = ipm1.IPM1(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev, beta=beta); nw = solve.Newton(m, verbose=False, chunk=1024)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    b0 = one + (3 * cl0 - 1 - c1) / cs * s2; b0[0, :] = 1.0
    F0, fl0 = nw.residual_full(b0, cl0); E0 = m.residual(b0, cl0, fl0); S0 = E0.clone(); S0[0, :] = 0
    tag = f'arc3_cl{cl0}_N{N}M{M}' + (f'_beta{beta}' if beta else '')
    log = open(base + f'runs/{tag}.dat', 'w'); log.write("# eps cl max|b| b(inf)max smin ds tau_eps sign_detJ\n")
    def save_fn(e_s, bb, cc, ee):
        np.savez(base + f'runs/{tag}_eps{e_s:.2f}.npz', b=bb.cpu().numpy(), cl=cc, eps=ee, gamma=m.gamma, N=N, M=M, L=m.L, p=m.p, beta=beta)
    out, (b, cl, eps) = solve.arclength(nw, b0, cl0, 0.0, S0, 0.0, ds=0.05, nsteps=int(sys.argv[4]) if len(sys.argv) > 4 else 700, amp_stop=1e5, log=log, verbose=False, ds_max=float(sys.argv[5]) if len(sys.argv) > 5 else 2.0, svd_every=int(sys.argv[6]) if len(sys.argv) > 6 else (1 if N*M < 3000 else 10),
                                        save_at=[0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95], save_fn=save_fn)
    emax = max(o[0] for o in out); i = int(np.argmax([o[0] for o in out]))
    C = m.ang.to_coef(b, 'EE').abs().max(0).values.cpu().numpy()
    binf = (m.rad.ext1_R @ b)[0].cpu().numpy()
    print(f"{tag}: b(inf,theta) at the end: " + np.array2string(binf, precision=0, max_line_width=300) + "  theta(deg): " + np.array2string(np.degrees(m.ang.theta_np), precision=0, max_line_width=300), flush=True)
    print(f"{tag}: eps_max={emax:.5f} (c_l={out[i][1]:.5f}, max|b|={out[i][2]:.4g}) steps={len(out)} final eps={eps:.4f}; "
          f"angular spectrum at the end (max over r): top/max = {C[-1]/C.max():.2e}, coefs k=0,M/2,M-1: {C[0]:.3g} {C[M//2]:.3g} {C[-1]:.3g}; time {time.time()-t0:.0f}s", flush=True)
    np.savez(base + f'runs/{tag}_end.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=m.L, p=m.p, beta=beta)
