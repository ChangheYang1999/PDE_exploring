"""Rescale a saved state to the canonical representative L_can = target (default 1) on a grid with L = 1 (same N, M)."""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start, out = sys.argv[1], sys.argv[2]; target = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
st = torch.load(start)
mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b = st['b'].to(dev); cl = st['cl']; M = st['M']; gamma = 1/cl
bhat = mdl.ang.to_coef(b, 'EE'); bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
K = st['L']**(1-gamma)*bK; a0 = b[0,0].item(); Lcan = (K/a0)**(cl/(cl-1)); lam = target/Lcan
mdl_new = ipm3.IPM3(N=st['N'], M=M, L=1.0, gamma=gamma, device=dev)
r_new = mdl_new.rad.rR.cpu().numpy(); t_old = mdl.rad.t_of_r(r_new/lam)
P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, t_old, mdl.rad.wR_np), device=dev)
w_old = mdl.rad.w_of_t(torch.tensor(t_old, device=dev), mdl.gamma)
b_new = (w_old/mdl_new.wR)[:, None]*(P @ b)
beta_new = (mdl_new.rad.ext1_R @ b_new).mean().item()
bhat2 = mdl_new.ang.to_coef(b_new, 'EE'); bK2 = ((mdl_new.rad.ext1_R @ bhat2)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
K2 = bK2; Lcan2 = (K2/b_new[0,0].item())**(cl/(cl-1))
print(f"{start}: cl={cl:.8f} a0={a0:.6f} K={K:.6f} Lcan={Lcan:.6f} -> lam={lam:.5f}; rescaled: a0={b_new[0,0].item():.6f} K={K2:.6f} Lcan={Lcan2:.6f} beta_new(mean b(inf))={beta_new:.6f}")
torch.save(dict(b=b_new.cpu(), cl=cl, gamma=gamma, N=st['N'], M=M, L=1.0, p=mdl_new.p, mu=st.get('mu', 0.0), beta=beta_new), out)
