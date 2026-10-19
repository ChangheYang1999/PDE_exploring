"""Fixed-c_l formulation: for given c_l solve the (N+1)M equations (E rows + b(0)=1) for b by eps-homotopy from
b0 = 1 + A s2 (A such that the identity holds at the start), then report the identity residual r(c_l) = 3c_l-1-c[b]."""
import sys, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; N, M, L = 48, 10, 1.0
for cl in [1.5, 2.0, 3.0]:
    gamma = 1 / cl
    m = ipm1.IPM1(N=N, M=M, L=L, gamma=gamma, device=dev)
    nw = solve.Newton(m, verbose=False)
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
    c1 = m.psi_xy0(m.fields(one)).item(); cs = m.psi_xy0(m.fields(s2)).item()
    A = (3 * cl - 1 - c1) / cs
    b0 = one + A * s2
    F0, fl0 = nw.residual_full(b0, cl)
    E0 = m.residual(b0, cl, fl0); S0 = E0.clone(); S0[0, :] = 0
    b = b0.clone(); reached = 0
    for eps in np.linspace(0, 1, 41)[1:]:
        bt, _, info = nw.solve(b, cl, hom=(eps, S0, 0.0), tol=1e-10, maxit=30, fix_cl=True)
        if not info['converged']:
            print(f"  c_l={cl}: natural continuation failed at eps={eps:.3f} (|F|={info['nrm']:.2e})", flush=True); break
        b = bt; reached = eps
        F, fl = nw.residual_full(b, cl)
        J = nw.jacobian(b, cl, fl)[:-1, :-1]
        sv = torch.linalg.svdvals(J)
        print(f"  c_l={cl} eps={eps:.3f}: identity residual 3cl-1-c = {F[-1].item():+.6f}  max|b|={b.abs().max().item():.4g}  b(inf)max={(m.rad.ext1_R@b).abs().max().item():.4g}  smin={sv[-1].item():.2e}  min b={b.min().item():.3g}", flush=True)
    np.savez(f'fixcl_{cl}.npz', b=b.cpu().numpy(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=m.p, eps=reached)
