"""Valley scan (representation ipm3.IPM3): at each fixed c_l solve the overdetermined unforced system in b by
Gauss-Newton least squares (gauge 'inf': mean b(inf) = beta), starting from the previous state (regridded).
Diagnostics: a0, c, c_l + c - 1, K (y-axis far-field amplitude), L_can = (K/a0)^(cl/(cl-1)), between-node |R|/N_f,
Chebyshev tail of the angular mean beta_0(t) of b (alternating-sign amplitude and algebraic slope -> estimate of the
non-smooth exponent), near-origin local slopes of b0 - a0 and of b1."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = float(sys.argv[3]); tag = sys.argv[4]
cls = [float(v) for v in sys.argv[5].split(',')]; start = sys.argv[6]; beta = float(sys.argv[7]) if len(sys.argv) > 7 else None
log = open(f'runs/{tag}.log', 'a')
log.write(f"# valley scan N={N} M={M} L={L} cls={cls} start={start}  {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
st = torch.load(start)
mdl_old = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b_old = st['b'].to(dev)
if beta is None: beta = (mdl_old.rad.ext1_R @ b_old).mean().item()

def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1)))
    return np.linalg.lstsq(V, f, rcond=None)[0]

def gn_fixed_cl(mdl, b, cl, maxit=60, tol=1e-12):
    nb = (mdl.N + 1) * mdl.M
    F, E, flds = mdl.system(b, cl, gauge_value=beta); nF = F.norm().item()
    for it in range(maxit):
        J = mdl.jacobian(b, cl, flds)[:, :nb]
        db = torch.linalg.lstsq(J, -F.unsqueeze(1)).solution.squeeze(1)
        lam = 1.0
        for _ in range(25):
            bn = b + lam * db.reshape(mdl.N + 1, mdl.M)
            Fn, En, fn = mdl.system(bn, cl, gauge_value=beta); nFn = Fn.norm().item()
            if nFn < (1 - 1e-4 * lam) * nF: break
            lam *= 0.5
        b, F, E, flds, nF = bn, Fn, En, fn, nFn
        if nF < tol or lam < 1e-6: break
    sv = torch.linalg.svdvals(J)
    return b, dict(F=F, E=E, flds=flds, nF=nF, iters=it + 1, smin=sv[-1].item(), s2=sv[-2].item(), smax=sv[0].item())

for cl in cls:
    gamma = 1 / cl
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev); mdl.gauge = 'inf'
    b = ipm3.regrid(mdl_old, b_old, mdl)
    t0 = time.time()
    b, info = gn_fixed_cl(mdl, b, cl)
    flds = info['flds']; c = mdl.psi_xy0(flds).item(); a0 = b[0, 0].item()
    bhat = mdl.ang.to_coef(b, 'EE')
    bK = (bhat[-1] * 0).sum()  # placeholder
    binf_modes = (mdl.rad.ext1_R @ bhat)[0]                      # beta_k(inf)
    bK = (binf_modes * torch.cos(math.pi * torch.arange(M, device=dev, dtype=torch.float64))).sum().item()   # b(inf, pi/2)
    K = L ** (1 - gamma) * bK; Lcan = (K / a0) ** (cl / (cl - 1)) if K / a0 > 0 else float('nan')
    # between-node residual
    tR = mdl.rad.tR_np; tm = 0.5 * (tR[:-1] + tR[1:]); th = mdl.ang.theta_np; thm = 0.5 * (th[:-1] + th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT); q = np.abs(ev['R']) / ev['Nf']
    og = [q[(RR >= lo) & (RR < hi)].max() for lo, hi in [(0, 1), (1, 100), (100, 1e4), (1e4, 1e30)]]
    # Chebyshev tail of beta_0 and beta_1
    ck0 = cheb_coeffs(mdl, bhat[:, 0].cpu().numpy()); ck1 = cheb_coeffs(mdl, bhat[:, 1].cpu().numpy())
    n = np.arange(N + 1); tail = slice(N // 2, N - 2)
    s0 = ((-1.0) ** n * ck0)[tail]; s1 = ((-1.0) ** n * ck1)[tail]
    def slope(s):
        m = np.abs(s) > 0; x = np.log(n[tail][m]); y = np.log(np.abs(s[m])); A = np.vstack([x, np.ones_like(x)]).T
        return np.linalg.lstsq(A, y, rcond=None)[0][0]
    sl0 = slope(s0); sl1 = slope(s1)
    frac_pos0 = (s0 > 0).mean(); frac_pos1 = (s1 > 0).mean()
    # near-origin slopes
    rr = np.logspace(-4, -1, 7); tt = mdl.rad.t_of_r(rr)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (P @ bhat).cpu().numpy()
    d0 = bk[:, 0] - a0; ls0 = np.diff(np.log(np.abs(d0))) / np.diff(np.log(rr)); ls1 = np.diff(np.log(np.abs(bk[:, 1]))) / np.diff(np.log(rr))
    msg = (f"cl={cl:.5f}: |F|2={info['nF']:.1e} it={info['iters']} smin={info['smin']:.1e} s2={info['s2']:.1e}  a0={a0:.8f} c={c:+.8f} cl+c-1={cl+c-1:+.1e}  K={K:.5f} Lcan={Lcan:.4g}  "
           f"offgrid|R|/Nf={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}  cheb-tail beta0: sign-frac(+)={frac_pos0:.2f} slope={sl0:+.2f} |c_N/2|={abs(ck0[N//2]):.1e} |c_N-3|={abs(ck0[N-3]):.1e}; "
           f"beta1: frac(+)={frac_pos1:.2f} slope={sl1:+.2f}  near-0 slopes b0-a0: {np.array2string(ls0, precision=2)} b1: {np.array2string(ls1, precision=2)}  {time.time()-t0:.1f}s")
    print(msg, flush=True); log.write(msg + "\n"); log.flush()
    log.write("   cheb coeffs beta0 (signed, n=N/2..N): " + np.array2string(ck0[N//2:], precision=2, max_line_width=300) + "\n")
    torch.save(dict(b=b.cpu(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=mdl.p), f'runs/{tag}_cl{cl:.4f}.pt')
    mdl_old, b_old = mdl, b
