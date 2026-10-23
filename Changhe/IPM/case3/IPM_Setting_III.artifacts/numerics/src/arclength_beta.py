"""Pseudo-arclength continuation of a forced sheet in beta at fixed c_l (ANALYSIS J.3 fold search).
Unknowns u = (b, mu, beta); equations: F_forced(b, mu; beta) = 0 ((N+1)M + 1 rows including the gauge row
mean b(inf) - beta = 0) plus the arclength constraint  tau . (u - u_pred) = 0.  Newton on the augmented square system.
Reports mu, Delta, a0, smin of the fixed-beta Jacobian along the curve; a fold in beta shows as a turning point."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; ds = float(sys.argv[3]); nsteps = int(sys.argv[4]); L = 1.0
orient = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
st = torch.load(start); N, M = st['N'], st['M']; cl = st['cl']; nb = (N+1)*M
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev); mdl.gauge = 'inf'
log = open(f'runs/{tag}.log', 'a'); log.write(f"# arclength in beta from {start} ds={ds} steps={nsteps} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def P(m): print(m, flush=True); log.write(m + "\n"); log.flush()
def Ffull(b, mu, beta):
    F, E, flds = mdl.system(b, cl, gauge_value=beta, mu=mu, forced=True); return F, flds
def Jfull(b, mu, beta, flds):
    J = mdl.jacobian(b, cl, flds, forced=True)                   # (nb+1, nb+1): columns (b, mu)
    Jb = torch.zeros(nb + 1, nb + 2, device=dev); Jb[:, :nb+1] = J; Jb[nb, nb+1] = -1.0   # d(gauge row)/d(beta) = -1
    return Jb
b = st['b'].to(dev); mu = st['mu']; beta = st['beta']
u = torch.cat([b.reshape(-1), torch.tensor([mu, beta], device=dev)])
# initial tangent: increase beta
F0, flds = Ffull(b, mu, beta); J0 = Jfull(b, mu, beta, flds)
# tangent solves J tau = 0 with normalisation; use the null vector of J (nb+1 x nb+2)
_, _, Vh = torch.linalg.svd(J0); tau = Vh[-1]; 
if tau[-1] < 0: tau = -tau
tau = tau/tau.norm()
scale = torch.ones(nb + 2, device=dev)
scale[:nb] = 1.0/max(b.abs().max().item(), 1.0)          # b in units of its max
scale[nb] = 1.0/max(abs(mu), 1.0)                         # mu in units of its magnitude
scale[nb+1] = 1.0/max(abs(beta), 1.0)                     # beta in units of its magnitude
tau = tau*scale; tau = tau/tau.norm()
if tau[-1]*orient < 0: tau = -tau
for k in range(nsteps):
    u_pred = u + ds*tau/scale
    uk = u_pred.clone()
    for it in range(40):
        bk = uk[:nb].reshape(N+1, M); muk = uk[nb].item(); betak = uk[nb+1].item()
        F, flds = Ffull(bk, muk, betak); J = Jfull(bk, muk, betak, flds)
        Faug = torch.cat([F, (tau*scale*(uk - u_pred)).sum().unsqueeze(0)])
        Jaug = torch.cat([J, (tau*scale)[None, :]], 0)
        if Faug.abs().max().item() < 1e-11: break
        du = torch.linalg.solve(Jaug, -Faug); uk = uk + du
    conv = Faug.abs().max().item()
    bk = uk[:nb].reshape(N+1, M); muk = uk[nb].item(); betak = uk[nb+1].item()
    c = mdl.psi_xy0(flds).item(); a0 = bk[0,0].item(); sv = torch.linalg.svdvals(J[:, :nb+1])
    P(f"step {k:3d}: beta={betak:9.4f} mu={muk:+.8f} Delta={cl+c-1:+.6f} a0={a0:.6f} |F|={conv:.1e} it={it} smin(fixed-beta J)={sv[-1].item():.1e} tau_beta={tau[-1].item():+.3f} tau_mu={tau[nb].item():+.3f}")
    if conv > 1e-8:
        P("  not converged; halving ds"); ds *= 0.5
        if ds < 1e-4: break
        continue
    # new tangent: null vector of J, oriented along the previous tangent
    _, _, Vh = torch.linalg.svd(J); tn = Vh[-1]*scale
    if (tn*tau).sum() < 0: tn = -tn
    tau = tn/tn.norm(); u = uk
    torch.save(dict(b=bk.cpu(), cl=cl, gamma=1/cl, N=N, M=M, L=L, p=mdl.p, mu=muk, beta=betak), f'runs/{tag}_last.pt')
