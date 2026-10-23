"""Lead's request (15:09Z): large-beta limit of sheet 1 in the fixed-amplitude picture.  Grid scale L = 1, gauge
mean b(inf) = beta fixed, forcing width Lf = eps decreasing (eps -> 0 is beta -> infinity at fixed forcing width).
Per state: a0, Delta, K, L_can, cubic x^2 y coefficient b_cub (from a small-r fit of the modes) and b_cub L_can^2, the
quartic datum H = int s^-3 f_2, the forced denominator a0 - 4A + 2 Delta, smin, |F|, between-node residual of the forced
equation; the K = 1 rescaled profile on 1/4 < |X| < 4 (sup difference between successive eps)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; N = int(sys.argv[3]); M = int(sys.argv[4]); beta = float(sys.argv[5])
epss = [float(v) for v in sys.argv[6].split(',')]; L = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# eps continuation from {start} N={N} M={M} beta={beta} eps={epss} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def P(m): print(m, flush=True); log.write(m + "\n"); log.flush()
st = torch.load(start); cl = st['cl']; gamma = 1/cl; A = 2*cl - 1
mo = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=gamma, device=dev); mdl.gauge = 'inf'
b = ipm3.regrid(mo, st['b'].to(dev), mdl); b = b*(beta/(mdl.rad.ext1_R @ b).mean().item()); mu = st.get('mu', 0.0)
# evaluation points for the K = 1 profile comparison: polar grid on 1/4 < r < 4 in units of L_can
rq = np.exp(np.linspace(np.log(0.25), np.log(4), 25)); tq = np.linspace(0.05, 0.95, 19)*np.pi/2; RQ, TQ = np.meshgrid(rq, tq, indexing='ij')
prev_prof = None
for eps in epss:
    mdl.Lf = eps
    b2, _, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=120, tol=1e-12, verbose=False, log=log, mu=mu, forced=True)
    flds = info['flds']; c = mdl.psi_xy0(flds).item(); a0 = b2[0,0].item(); mu2 = info['mu']; Delta = cl + c - 1
    bhat = mdl.ang.to_coef(b2, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    # cubic coefficient: rho_1 = a0 r + ((b_cub + 3e)/4) r^3, rho_3 = ((b_cub - e)/4) r^3 (small-r fit, r in [1e-3, 3e-2] x min(1, eps))
    rr = np.logspace(-3.5, -1.5, 30)*min(1.0, eps); tt = mdl.rad.t_of_r(rr); Pr = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev)
    bk = (Pr @ bhat).cpu().numpy(); wr = mdl.rad.w_of_t(torch.tensor(tt), mdl.gamma).numpy()
    rho1 = rr*wr*(bk[:,0] - bk[:,1]/2); rho3 = rr*wr*(bk[:,1] - bk[:,2])/2
    c1 = np.polyfit(rr**2, rho1/rr, 3); c3 = np.polyfit(rr**2, rho3/rr, 3); s13 = 4*c1[-2]; d13 = 4*c3[-2]; bcub = (s13 + 3*d13)/4
    # quartic datum H
    C = flds['Fhat_L'] @ mdl.angf.A['OO'].T; F4_L = C[:, 1]
    tg, wg = ipm3.gauss_legendre(2000); tgt = torch.tensor(tg, device=dev); wgt = torch.tensor(wg, device=dev)
    PL = torch.tensor(ipm3.interp_matrix(mdl.rad.tL_np, tg, mdl.rad.wL_np), device=dev); F4 = PL @ F4_L
    w = mdl.rad.w_of_t(tgt, mdl.gamma); r = mdl.rad.rmap(tgt); Q = (1 - tgt) + mdl.p*(1 + tgt)
    H = (w*F4/r**2*Q/(1 - tgt**2)*wgt).sum().item()
    sv = torch.linalg.svdvals(info['J'])
    # between-node residual of the forced equation
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b2, cl, flds, RR, TT); phi = (1 + RR**2/eps**2)**(-2); q = (np.abs(ev['R'] - mu2*ev['y']*phi)/ev['Nf']).max()
    # K = 1 rescaled profile: rho_K(X) = l rho(X/l) with l = 1/Lcan ... use the representative with L_can = 1: rho_can(X) = Lcan^-1 rho(Lcan X)?  rho_l(X) = l rho(X/l), L_can(rho_l) = l L_can -> l = 1/Lcan.
    l = 1.0/Lcan
    evp = mdl.evaluate(b2, cl, flds, RQ/l, TQ); prof = l*evp['rho']/ (RQ**gamma)      # rho_l(X)/|X|^gamma on the comparison grid
    dprof = float('nan') if prev_prof is None else np.abs(prof - prev_prof).max()/np.abs(prof).max()
    P(f"eps={eps:8.4f}: |F|={info['nF']:.1e} it={len(info['hist'])} smin={sv[-1].item():.1e} mu={mu2:+.8f} a0={a0:.8f} Delta={Delta:+.8f} K={K:.6f} Lcan={Lcan:.6g} "
      f"b_cub={bcub:+.5e} b_cub*Lcan^2={bcub*Lcan**2:+.5e} H={H:+.5e} a0-4A+2Delta={a0-4*A+2*Delta:+.5f} offgrid|R_f|/Nf={q:.1e} sup|dprof|/sup|prof|={dprof:.2e}")
    if info['nF'] < 1e-8:
        b, mu = b2, mu2; prev_prof = prof
        torch.save(dict(b=b.cpu(), cl=cl, gamma=gamma, N=N, M=M, L=L, p=mdl.p, mu=mu, beta=beta, Lf=eps), f'runs/{tag}_eps{eps:.4f}.pt')
    else:
        P("  not converged; stop"); break
