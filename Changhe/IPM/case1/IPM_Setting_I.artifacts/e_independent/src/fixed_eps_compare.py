"""Discretisation comparison at fixed eps: natural continuation 0 -> eps_target of the identity-preserving homotopy from
b0 = 1 + A s2 (c_l0 = 3) on several grids (unmapped and mapped); report c_l, b(inf) max, b(inf, theta) at common angles
(by interpolation), and the angular coefficient decay."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; cl0 = 3.0
grids = [(64, 16, 0.0), (96, 24, 0.0), (128, 32, 0.0), (64, 16, 0.5), (64, 16, 0.8), (96, 24, 0.5), (96, 24, 0.8)]
targets = [0.3, 0.5]
th_common = np.radians([5, 20, 45, 70, 80, 85, 88])
for (N, M, beta) in grids:
    t0 = time.time()
    m = ipm1.IPM1(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev, beta=beta); nw = solve.Newton(m, verbose=False, chunk=1024)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    b = one + (3 * cl0 - 1 - c1) / cs * s2; b[0, :] = 1.0; cl = cl0
    F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0); S0 = E0.clone(); S0[0, :] = 0
    for eps in np.linspace(0, max(targets), 26)[1:]:
        bt, clt, info = nw.solve(b, cl, hom=(eps, S0, 0.0), tol=1e-10, maxit=30)
        if not info['converged']:
            print(f"grid ({N},{M},beta={beta}): continuation failed at eps={eps:.3f}", flush=True); break
        b, cl = bt, clt
        if any(abs(eps - tg) < 1e-9 for tg in targets):
            C = m.ang.to_coef(b, 'EE')
            sc = m.ang.s_of_theta(torch.tensor(th_common, device=dev))
            k = torch.arange(M, device=dev, dtype=torch.float64)
            binf_c = (m.rad.ext1_R @ C)[0] @ torch.cos(sc[:, None] * (2 * k)[None, :]).T
            Cmax = C.abs().max(0).values.cpu().numpy()
            print(f"grid ({N},{M},beta={beta}) eps={eps:.2f}: c_l={cl:.8f} b(inf)max={(m.rad.ext1_R @ b).abs().max().item():.2f} "
                  f"b(inf,theta@5,20,45,70,80,85,88deg)={np.array2string(binf_c.cpu().numpy(), precision=1, max_line_width=200)} "
                  f"ang coef k=0,M/4,M/2,3M/4,M-1: {Cmax[0]:.3g} {Cmax[M//4]:.3g} {Cmax[M//2]:.3g} {Cmax[3*M//4]:.3g} {Cmax[-1]:.3g}  ({time.time()-t0:.0f}s)", flush=True)
