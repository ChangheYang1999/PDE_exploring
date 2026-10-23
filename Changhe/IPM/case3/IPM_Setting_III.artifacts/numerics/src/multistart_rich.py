"""Richer multistart (referee objection 8): anisotropic cores (R_x/R_y), two radial scales (core + annular bump),
higher angular modes with sign changes, both signs of the centre amplitude.  Saves distinct converged forced solutions
and runs the refinement-invariance test (48x24 -> 64x32 -> 96x48) on each; reports which pass (mu, a0 invariant)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'; N = int(sys.argv[1]); M = int(sys.argv[2]); tag = sys.argv[3]; cl = float(sys.argv[4]); beta = float(sys.argv[5]); L = 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# multistart_rich N={N} M={M} cl={cl} beta={beta} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
r = mdl.rad.rR[:, None]; th = mdl.ang.theta[None, :]; x = r*torch.cos(th); y = r*torch.sin(th)
found = []; ng = 0
rng = np.random.default_rng(0)
guesses = []
for a0g in [0.5*beta, 3*beta, 10*beta, -0.5*beta, -3*beta, -10*beta]:
    for Rx, Ry in [(0.1, 0.1), (0.03, 0.3), (0.3, 0.03), (1.0, 0.1), (0.1, 1.0), (1.0, 1.0)]:
        for (amp2, R2) in [(0.0, 1.0), (0.5*beta, 0.3), (-0.5*beta, 3.0)]:
            for (k, ak, Rk) in [(0, 0.0, 1.0), (1, 0.5, 0.3), (1, -0.5, 1.0), (2, 0.5, 0.3), (3, -0.5, 1.0)]:
                guesses.append((a0g, Rx, Ry, amp2, R2, k, ak, Rk))
print(f"{len(guesses)} guesses", flush=True)
for (a0g, Rx, Ry, amp2, R2, k, ak, Rk) in guesses:
    core = (a0g - beta)/(1 + x**2/Rx**2 + y**2/Ry**2)
    bump = amp2*(r**2/(R2**2 + r**2))/(1 + (r/(3*R2))**2)          # annular bump at scale R2
    ang = ak*(r**2/(Rk**2 + r**2))**k*torch.cos(2*k*th) if k > 0 else 0.0
    bg = beta + core + bump + beta*ang
    ng += 1
    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=60, tol=1e-12, verbose=False, log=log, mu=0.0, forced=True)
    if info['nF'] < 1e-8:
        a0 = b[0,0].item(); mu = info['mu']
        if all(abs(mu - f[0]) > 1e-3*max(1, abs(mu)) or abs(a0 - f[1]) > 1e-2*max(1, abs(a0)) for f in found):
            sv = torch.linalg.svdvals(info['J']); found.append((mu, a0, sv[-1].item())); kk = len(found)
            torch.save(dict(b=b.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=mu, beta=beta), f'runs/{tag}_s{kk}.pt')
            m = f"new solution s{kk} (guess #{ng}: a0g={a0g} Rx={Rx} Ry={Ry} amp2={amp2} R2={R2} k={k} ak={ak}): mu={mu:+.8f} a0={a0:.6f} Delta={cl+mdl.psi_xy0(info['flds']).item()-1:+.5f} smin={sv[-1].item():.1e}"
            print(m, flush=True); log.write(m+"\n"); log.flush()
m = f"SUMMARY cl={cl} beta={beta}: {len(found)} distinct solutions from {ng} guesses: {[(round(f[0],4), round(f[1],3)) for f in found]}"; print(m, flush=True); log.write(m+"\n"); log.flush()
# refinement-invariance test for every distinct solution
for kk, (mu, a0, smin) in enumerate(found, 1):
    st = torch.load(f'runs/{tag}_s{kk}.pt'); mdl_p = mdl; b_p = st['b'].to(dev); mu_p = mu; vals = [(N, M, mu, a0)]
    for (N2, M2) in [(48, 24), (64, 32), (96, 48)]:
        mdl2 = ipm3.IPM3(N=N2, M=M2, L=L, gamma=1/cl, device=dev); mdl2.gauge = 'inf'
        bg = ipm3.regrid(mdl_p, b_p, mdl2); bg = bg*(beta/(mdl2.rad.ext1_R @ bg).mean().item())
        b2, _, info2 = ipm3.newton(mdl2, bg, cl, gauge_value=beta, maxit=100, tol=1e-12, verbose=False, log=log, mu=mu_p, forced=True)
        if info2['nF'] < 1e-8:
            vals.append((N2, M2, info2['mu'], b2[0,0].item())); mdl_p, b_p, mu_p = mdl2, b2, info2['mu']
        else:
            vals.append((N2, M2, float('nan'), float('nan')))
    mus = [v[2] for v in vals]; a0s = [v[3] for v in vals]
    invariant = all(np.isfinite(mus)) and (max(mus) - min(mus)) < 1e-6*max(1, abs(mus[0])) and (max(a0s) - min(a0s)) < 1e-6*max(1, abs(a0s[0]))
    m = f"  refine s{kk}: " + " | ".join(f"{v[0]}x{v[1]}: mu={v[2]:+.8f} a0={v[3]:.6f}" for v in vals) + f"  -> {'INVARIANT' if invariant else 'drifts/fails'}"
    print(m, flush=True); log.write(m+"\n"); log.flush()
