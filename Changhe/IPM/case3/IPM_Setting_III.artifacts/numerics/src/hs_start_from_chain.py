"""hs_start_from_chain.py -- re-gauge a saved fixed-c_l chain state into the 3.72 frame and project it onto an HS model's basis (lead 08:04Z item (2) starts):
g(xi, y) = rho_l(sqrt(a0) xi, y)/a0 with rho_l(X) = l rho(X/l), l = (a0/K)^(1/(1-gamma)) (so K_l = a0 and g_y(0) = 1, K_g = 1).  The HS model has the same map
exponent gamma = 1/c_l.  The field is sampled at the HS model's nodes (polar (r, theta) in the (xi, y) plane -> physical point (sqrt(a0) r cos theta / l,
r sin theta / l) of the original state), converted to mode values b = g/(y w) and projected (LS, cutoff 1e-8).  Saves runs/<tag>.pt with 'u' for hs_solve start=.
usage: python3 src/hs_start_from_chain.py state.pt N M tag"""
import sys, math, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3ql, dr, hs
torch.set_default_dtype(torch.float64); dev = 'cuda'
src, N, M, tag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
st = torch.load(src, weights_only=False); cl = st['cl']; gam = 1 / cl
qo = ipm3ql.IPM3QL(N=st['N'], M=st['M'], L=st.get('L', 1.0), gamma=gam, device=dev, Lf=st.get('Lf', 1.0)); beta = st['beta'].to(dev); flds = qo.fields(beta)
a0 = beta[0, 0].item(); bk1 = (qo.rad.ext1_R @ beta * torch.cos(math.pi * qo.kk)[None, :]).sum().item(); K = 0.5 * qo.L ** (1 - gam) * bk1; l = (a0 / K) ** (1 / (1 - gam))
m = dr.DR(N, M, cl, device=dev, basis='local', rcond=1e-8)
r = m.rad.rR.cpu().numpy(); th = m.angf.theta_np; RR, TT = np.meshgrid(r, th, indexing='ij')
XI = RR * np.cos(TT); YY = RR * np.sin(TT)
xo = math.sqrt(a0) * XI / l; yo = YY / l; ro = np.hypot(xo, yo); tho = np.arctan2(yo, xo)
ev = qo.evaluate(beta, cl, flds, ro, tho); g = l * ev['rho'] / a0                                   # g(xi, y) = rho_l(sqrt(a0) xi, y)/a0
w = m.rad.wR.cpu().numpy()[:, None]; b = g / (YY * w)                                                  # mode-value field b = g/(y w)
b[0, :] = 1.0                                                                                          # centre: g_y(0) = 1 exactly
u = m.project(torch.tensor(b, device=dev))
a0g, bg, eg = [z.item() for z in m.jets(u)]; ff = m.farfield(u)
print(f"{src}: a0 {a0:.6f} K {K:.6f} l {l:.6f}; HS start on {N}x{M}: g_y(0) {a0g:.8f} K_g {ff['K'].item():.8f} B {bg:+.6e} E {eg/a0g:+.6e} (expected B = b/l^2 = {st.get('b', float('nan')) if 'b' in st else float('nan')})")
torch.save(dict(u=u.cpu(), beta=m.beta_full(u).cpu(), c=cl, cl=cl, C=cl, N=N, M=M, L=1.0, gamma=gam, p=m.p, basis='local', rcond=1e-8, rep='HS start from chain', source=src, l=l, a0_orig=a0, K_orig=K), f'runs/{tag}.pt'); print('saved runs/' + tag + '.pt')
