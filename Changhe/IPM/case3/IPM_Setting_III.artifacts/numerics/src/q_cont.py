"""Q representation: forced continuation in gK (2 -> 4 -> 8) at fixed c_l, then regrid to a finer grid and re-solve, to test
robustness and compare with ipm3 sheet-1 values at larger amplitude (beta_3 = gK/2 in the ipm3 'inf' gauge up to the mean/axis
difference)."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q
torch.set_default_dtype(torch.float64); dev = 'cuda'
cl = float(sys.argv[1]); tag = sys.argv[2]; log = open(f'runs/{tag}.log', 'a')
N0 = int(sys.argv[3]) if len(sys.argv) > 3 else 64; M0 = int(sys.argv[4]) if len(sys.argv) > 4 else 16
N1 = int(sys.argv[5]) if len(sys.argv) > 5 else 96; M1 = int(sys.argv[6]) if len(sys.argv) > 6 else 24
q = ipm3q.IPM3Q(N=N0, M=M0, L=1.0, gamma=1/cl, device=dev)
beta0 = torch.zeros(N0+1, M0, device=dev); beta0[:, 0] = 2.0; u = q.beta_to_u(beta0); mu = 0.0
for gK in [2.0, 3.0, 4.0, 6.0, 8.0]:
    bet = q.beta_full(u); u0 = q.beta_to_u(bet*(gK/q.gauge_row(bet, 0.0).item()))
    u2, _, mu2, info = q.newton(u0, cl, gK, mu=mu, forced=True, maxit=60, log=log)
    beta = q.beta_full(u2); c = q.psi_xy0(info['flds']).item(); og = ipm3q.between_node(q, beta, cl, info['flds'], mu2)
    m = f"Q forced cont {N0}x{M0} cl={cl} gK={gK}: |F|={info['nF']:.1e} its={info['its']} mu={mu2:+.8f} a0={beta[0,0].item():.8f} Delta={cl+c-1:+.6f} between-node |R_f|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}]"
    print(m, flush=True); log.write(m+"\n")
    if info['nF'] < 1e-8: u, mu = u2, mu2
    else: break
# regrid the last converged state to 96x24 and re-solve
q2 = ipm3q.IPM3Q(N=N1, M=M1, L=1.0, gamma=1/cl, device=dev)
beta_new = ipm3s.regrid_s(q, q.beta_full(u), q2); u_new = q2.beta_to_u(beta_new)
gK_last = q.gauge_row(q.beta_full(u), 0.0).item()
u3, _, mu3, info3 = q2.newton(u_new, cl, gK_last, mu=mu, forced=True, maxit=60, log=log)
beta3 = q2.beta_full(u3); c3 = q2.psi_xy0(info3['flds']).item(); og = ipm3q.between_node(q2, beta3, cl, info3['flds'], mu3)
m = f"Q forced regrid {N1}x{M1} cl={cl} gK={gK_last:.4f}: |F|={info3['nF']:.1e} its={info3['its']} mu={mu3:+.8f} a0={beta3[0,0].item():.8f} Delta={cl+c3-1:+.6f} between-node |R_f|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}]"
print(m, flush=True); log.write(m+"\n")
