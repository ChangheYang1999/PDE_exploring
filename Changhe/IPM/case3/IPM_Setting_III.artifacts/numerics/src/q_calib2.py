"""Calibration of the least-squares Q basis against an ipm3.py sheet-1 forced state (same forcing phi = (1 + r^2)^-2, L = Lf = 1):
read the state, compute its y-axis far-field value gK = b(inf, pi/2) = sum_k (-1)^k bhat_k(1), its mu, a_0, c; then solve the
forced QL system at N x M with gauge gK (continuation in gK from 2 if gK > 3) and compare.  argv: state.pt N M [N2 M2 ...]"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3ql
torch.set_default_dtype(torch.float64); dev = 'cuda'
st = torch.load(sys.argv[1]); cl = st['cl']; N0, M0 = st['N'], st['M']
mo = ipm3.IPM3(N=N0, M=M0, L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); b = st['b'].to(dev)
bhat = mo.ang.to_coef(b, 'EE'); bK = ((mo.rad.ext1_R @ bhat)[0] * torch.cos(math.pi * torch.arange(M0, device=dev, dtype=torch.float64))).sum().item()
gK = 2.0 * bK   # w_ipm3 / w_Q -> 2 at infinity (checked numerically, WORKLOG 17:33Z), so b_Q(inf) = 2 b_ipm3(inf)
flds = mo.fields(b); c0 = mo.psi_xy0(flds).item(); a00 = b[0, 0].item(); mu0 = st['mu']
print(f"ipm3 state {sys.argv[1]}: cl={cl} beta(inf-gauge)={st.get('beta')} {N0}x{M0}: mu={mu0:.10f} a0={a00:.10f} c={c0:+.10f} b_K(ipm3)={bK:.10f} -> gK(Q)=2 b_K={gK:.10f}", flush=True)
sizes = [int(v) for v in sys.argv[2:]]
for N, M in zip(sizes[0::2], sizes[1::2]):
    q = ipm3ql.IPM3QL(N=N, M=M, L=1.0, gamma=1 / cl, device=dev, Lf=1.0)
    beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = 2.0; u = q.beta_to_u(beta0); mu = 0.0
    nst = max(4, int(math.ceil((gK - 2.0) / 0.6))); path = [2.0 + (gK - 2.0) * j / nst for j in range(nst + 1)] if gK > 2.5 else [gK]
    t0 = time.time()
    for g in path:
        bet = q.beta_full(u); u0 = q.beta_to_u(bet * (g / q.gauge_row(bet, 0.0).item()))
        u, _, mu, info = q.gn(u0, cl, g, mu=mu, forced=True, maxit=40)
        if info['nF'] > 1e-8: print(f"  gK={g:.4f}: not converged |F|={info['nF']:.1e}", flush=True)
    beta = q.beta_full(u); c = q.psi_xy0(info['flds']).item(); a0 = beta[0, 0].item()
    og = ipm3ql.between_node(q, beta, cl, info['flds'], mu)
    print(f"QL {N}x{M} at gK={gK:.10f}: |F|max={info['nF']:.1e} its(last)={info['its']} mu={mu:.10f} a0={a0:.10f} c={c:+.10f} "
          f"dmu={mu-mu0:+.1e} da0={a0-a00:+.1e} dc={c-c0:+.1e} between-node |R_f|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}] ({time.time()-t0:.0f}s)", flush=True)
