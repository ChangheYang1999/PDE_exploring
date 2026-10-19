"""Compactified formulation with gamma TIED to the unknown c_l (model rebuilt whenever c_l changes), so the far-field rows do
not pin c_l. Identity-preserving homotopy from b0 = 1 + A s2(r); S0 = E[b0] evaluated on the current model. Natural continuation."""
import sys, time, torch, numpy as np
sys.path.insert(0, 'src')
import ipm1, solve
dev = 'cuda'; base = ''
N, M = int(sys.argv[1]), int(sys.argv[2]); deps = float(sys.argv[3]) if len(sys.argv) > 3 else 0.02
cl0 = 3.0; L = 1.0; tag = f'tied_cl3_N{N}M{M}'
cache = {}
def model(cl):
    key = round(cl, 12)
    if key not in cache:
        if len(cache) > 6: cache.clear()
        m = ipm1.IPM1(N=N, M=M, L=L, gamma=1 / cl, device=dev); nw = solve.Newton(m, verbose=False, chunk=1024)
        r = m.rad.rR[:, None]; th = m.ang.theta[None, :]
        s2 = r ** 2 / (L ** 2 + r ** 2) + 0 * th; one = torch.ones_like(s2)
        cache[key] = (m, nw, one, s2)
    return cache[key]
m0, nw0, one0, s20 = model(cl0)
c1 = m0.psi_xy0(m0.fields(one0)).item(); cs = m0.psi_xy0(m0.fields(s20)).item(); A = (3 * cl0 - 1 - c1) / cs
def b0_on(m, one, s2): bb = one + A * s2; bb[0, :] = 1.0; return bb
def resid(b, cl, eps):
    m, nw, one, s2 = model(cl)
    b0 = b0_on(m, one, s2)
    F0, fl0 = nw.residual_full(b0, cl0); E0 = m.residual(b0, cl0, fl0); S0 = E0.clone(); S0[0, :] = 0
    F, fl = nw.residual_full(b, cl, hom=(eps, S0, 0.0))
    return F, fl, nw, m
def newton(b, cl, eps, tol=1e-10, maxit=25):
    F, fl, nw, m = resid(b, cl, eps); nrm = F.abs().max().item()
    for it in range(maxit):
        if nrm < tol: return b, cl, True, nrm
        J = nw.jacobian(b, cl, fl)
        h = 1e-6 * max(1.0, abs(cl)); Fp = resid(b, cl + h, eps)[0]; Fm = resid(b, cl - h, eps)[0]
        J[:, -1] = (Fp - Fm) / (2 * h)
        d = torch.linalg.solve(J, -F); alpha = 1.0; ok = False
        for _ in range(8):
            bt = b + alpha * d[:-1].reshape(N + 1, M); clt = cl + alpha * d[-1].item()
            if clt < 1.05: alpha *= 0.5; continue
            Ft, flt, nw, m = resid(bt, clt, eps); nt = Ft.abs().max().item()
            if nt < nrm: b, cl, F, fl, nrm, ok = bt, clt, Ft, flt, nt, True; break
            alpha *= 0.5
        if not ok: return b, cl, False, nrm
    return b, cl, nrm < tol, nrm
b = b0_on(m0, one0, s20); cl = cl0; eps = 0.0
log = open(base + f'runs/{tag}.dat', 'w'); log.write("# eps |F| cl b(inf)max min_b\n")
while eps < 1.0 - 1e-12 and deps >= 0.0025:
    et = min(1.0, eps + deps); t1 = time.time()
    bt, clt, ok, nrm = newton(b, cl, et)
    if not ok:
        print(f"[tied] eps={et:.4f} failed |F|={nrm:.2e}; halving", flush=True); deps *= 0.5; continue
    # the grid changed with c_l: b values are on the grid of model(clt); keep them as the unknowns for the next step
    b, cl, eps = bt, clt, et
    m = model(cl)[0]
    binf = (m.rad.ext1_R @ b).abs().max().item()
    print(f"[tied] eps={eps:.4f} |F|={nrm:.2e} c_l={cl:.8f} b(inf)max={binf:.2f} min b={b[1:].min().item():.3g} ({time.time()-t1:.0f}s)", flush=True)
    log.write(f"{eps:.4f} {nrm:.6e} {cl:.10f} {binf:.6e} {b[1:].min().item():.6e}\n"); log.flush()
    if any(abs(eps - e) < 1e-6 for e in [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]):
        np.savez(base + f'runs/{tag}_eps{eps:.3f}.npz', b=b.cpu().numpy(), cl=cl, eps=eps, gamma=m.gamma, N=N, M=M, L=L, p=m.p, beta=0.0)
print(f"[tied] done: final eps={eps:.4f} c_l={cl:.6f}", flush=True)
