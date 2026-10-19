"""Fold-position survey at adequate resolution: identity-preserving homotopy from several start shapes and c_l0 values,
natural continuation in eps with Newton (step 0.02, halving to 0.0025 on failure), LM fallback; records eps_max."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; base = ''
N, M = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (128, 32)
log = open(base + f'runs/survey_folds_N{N}M{M}.dat', 'a')
def shapes(m):
    r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
    s2 = r ** 2 / (m.L ** 2 + r ** 2) + 0 * th; s1 = r / (m.L + r) + 0 * th
    return {'s2': s2, 's2_xaxis': s2 * (1 + torch.cos(2 * th)) / 2, 's2_yaxis': s2 * (1 - torch.cos(2 * th)) / 2, 's1': s1,
            's2_L3': r ** 2 / (9 * m.L ** 2 + r ** 2) + 0 * th}
for cl0 in [1.5, 2.0, 2.5, 3.0, 4.0, 6.0]:
    m = ipm1.IPM1(N=N, M=M, L=1.0, gamma=1 / cl0, device=dev); nw = solve.Newton(m, verbose=False, chunk=1024)
    one = torch.ones(N + 1, M, device=dev)
    c1 = m.psi_xy0(m.fields(one)).item()
    for name, sh in shapes(m).items():
        t0 = time.time()
        cs = m.psi_xy0(m.fields(sh)).item()
        if abs(cs) < 1e-12: continue
        A = (3 * cl0 - 1 - c1) / cs
        b = one + A * sh; b[0, :] = 1.0; cl = cl0
        F0, fl0 = nw.residual_full(b, cl); E0 = m.residual(b, cl, fl0); S0 = E0.clone(); S0[0, :] = 0
        eps = 0.0; deps = 0.02; emax = 0.0; minb = 1.0
        while eps < 1.0 - 1e-12 and deps >= 0.0025:
            et = min(1.0, eps + deps)
            bt, clt, info = nw.solve(b, cl, hom=(et, S0, 0.0), tol=1e-10, maxit=25)
            if not info['converged']:
                bt, clt, info = solve.levenberg_marquardt_hom(nw, b, cl, hom=(et, S0, 0.0), lam=1e-3, maxit=80, tol=1e-10)
            if info['converged']:
                b, cl, eps = bt, clt, et; emax = eps; minb = b[1:].min().item()
            else:
                deps *= 0.5
        binf = (m.rad.ext1_R @ b).abs().max().item()
        msg = f"c_l0={cl0:4.1f} shape={name:9s} A={A:9.3f}: eps_max={emax:.4f} c_l(end)={cl:.6f} b(inf)max={binf:.1f} min b={minb:.3g} ({time.time()-t0:.0f}s)"
        print(msg, flush=True); log.write(msg + "\n"); log.flush()
