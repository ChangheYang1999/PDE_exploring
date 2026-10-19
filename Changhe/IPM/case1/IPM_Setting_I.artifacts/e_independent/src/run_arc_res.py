import sys, time, argparse, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
for (N, M) in [(64, 12), (96, 16)]:
    cl0 = 2.5; gamma = 1/cl0; L = 1.0
    m = ipm1.IPM1(N=N, M=M, L=L, gamma=gamma, device='cuda')
    nw = solve.Newton(m, verbose=False)
    b0 = torch.ones(N + 1, M, device='cuda')
    F0, fl0 = nw.residual_full(b0, cl0)
    S0 = m.residual(b0, cl0, fl0); S0[0, :] = 0
    s0 = (3 * cl0 - 1 - m.psi_xy0(fl0)).item()
    log = open(f'arc_cl2.5_N{N}M{M}.dat', 'w')
    t0 = time.time()
    out, (b, cl, eps) = solve.arclength(nw, b0, cl0, 0.0, S0, s0, ds=0.05, nsteps=120, amp_stop=2e3, log=log, verbose=False)
    emax = max(o[0] for o in out)
    i = int(np.argmax([o[0] for o in out]))
    print(f"N={N} M={M}: eps_max={emax:.6f} at c_l={out[i][1]:.6f} max|b|={out[i][2]:.4g} b(inf)={out[i][3]:.4g}; steps={len(out)} time={time.time()-t0:.0f}s", flush=True)
    np.savez(f'arc_cl2.5_N{N}M{M}_end.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=gamma, N=N, M=M, L=L, p=m.p)
