"""Between-node residual check of a saved state: evaluate R = (c_l X + U).grad rho - rho and N_f, N_v on grids of
points placed between the collocation nodes (midpoints in t and theta) and on dense rays; report by region."""
import sys, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
st = torch.load(sys.argv[1]); dev = 'cuda'
mdl = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev)
b = st['b'].to(dev); cl = st['cl']; flds = mdl.fields(b)
tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1] + tR[1:]); tm = np.concatenate([tm, [0.5*(tR[-1]+1)]])
th = mdl.ang.theta_np; thm = 0.5*(th[:-1] + th[1:]); thm = np.concatenate([[0.5*th[0]], thm, [0.5*(th[-1] + np.pi/2)]])
rm = mdl.rad.rmap(torch.tensor(tm)).numpy()
RR, TT = np.meshgrid(rm, thm, indexing='ij')
ev = mdl.evaluate(b, cl, flds, RR, TT)
R = np.abs(ev['R']); Nf = ev['Nf']; Nv = ev['Nv']
# collocation residual for reference
E = mdl.residual(b, cl, flds); rhoY = (mdl.rad.rR*mdl.wR)[:,None]*mdl.ang.sin[None,:]
Rcol = (E*rhoY).abs()   # R = E * y w
print(f"state {sys.argv[1]}: cl={cl:.8f} a0={b[0,0].item():.6f} N={st['N']} M={st['M']}")
print(f"collocation |R| max (rows 1..N) = {Rcol[1:].max().item():.3e};  |E| max = {E[1:].abs().max().item():.3e}")
print(" region (r)          max|R|      max|R|/Nf    max|R|/Nv    (between-node midpoints)")
edges = [0, 0.01, 0.1, 1, 10, 100, 1e3, 1e4, 1e6, 1e9, 1e30]
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (RR >= lo) & (RR < hi)
    if m.sum() == 0: continue
    print(f" [{lo:8.0e},{hi:8.0e})  {R[m].max():.3e}   {(R[m]/Nf[m]).max():.3e}   {(R[m]/Nv[m]).max():.3e}   ({m.sum()} pts)")
# dense rays near the axes and diagonal, r in [1e-3, 1e6]
rr = np.logspace(-3, 6, 400)
for ang in [0.02, np.pi/4, np.pi/2 - 0.02]:
    ev = mdl.evaluate(b, cl, flds, rr, np.full_like(rr, ang))
    print(f" ray theta={ang:.3f}: max|R|/Nf = {(np.abs(ev['R'])/ev['Nf']).max():.3e}  at r={rr[(np.abs(ev['R'])/ev['Nf']).argmax()]:.2e};  max|R| = {np.abs(ev['R']).max():.3e}")
