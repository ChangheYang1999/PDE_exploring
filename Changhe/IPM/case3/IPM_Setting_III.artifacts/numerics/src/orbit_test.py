"""Map the valley: from a converged state (free c_l), re-solve with c_l free at other gauge values beta (far-field
mean of b), starting from the rescaled state. If c_l, a0, L_can*beta^(-cl/((cl-1)(1-gamma)))... stay constant it is
one scaling orbit; report c_l(beta), a0(beta), K, Lcan."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; betas = [float(v) for v in sys.argv[3].split(',')]
st = torch.load(start)
N, M, L = st['N'], st['M'], st['L']
log = open(f'runs/{tag}.log', 'a'); log.write(f"# orbit test from {start} betas {betas} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl.gauge = 'inf'
b0 = st['b'].to(dev); cl0 = st['cl']; beta0 = (mdl.rad.ext1_R @ b0).mean().item()
print(f"start cl={cl0:.10f} a0={b0[0,0].item():.8f} beta0={beta0:.6f}")
for beta in betas:
    # initial guess: exact scaling of the state to far-field mean beta: b_lambda(r) = w(r/lam)/w(r) b(r/lam); lam^(1-gamma) = beta/beta0
    gamma = 1/cl0; lam = (beta/beta0)**(1/(1-gamma))
    r_new = mdl.rad.rR.cpu().numpy(); t_old = mdl.rad.t_of_r(r_new/lam)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, t_old, mdl.rad.wR_np), device=dev)
    w_old = mdl.rad.w_of_t(torch.tensor(t_old, device=dev), mdl.gamma); w_new = mdl.wR
    bg = (w_old/w_new)[:, None]*(P @ b0)
    F0, _, _ = mdl.system(bg, cl0, gauge_value=beta)
    t0 = time.time()
    b, cl, info = ipm3.newton(mdl, bg, cl0, gauge_value=beta, maxit=60, tol=1e-12, verbose=False, log=log)
    c = mdl.psi_xy0(info['flds']).item(); a0 = b[0,0].item()
    bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-1/cl)*bK; Lcan = (K/a0)**(cl/(cl-1))
    # scaling prediction: Lcan should scale like lam
    msg = f"beta={beta:7.3f} lam_pred={lam:9.4f}: |F(scaled guess)|={F0.abs().max().item():.1e} -> cl={cl:.10f} (d={cl-cl0:+.2e}) a0={a0:.8f} K={K:.5f} Lcan={Lcan:.5f} Lcan/lam={Lcan/lam:.5f} |F|={info['nF']:.1e} it={len(info['hist'])}  {time.time()-t0:.1f}s"
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
