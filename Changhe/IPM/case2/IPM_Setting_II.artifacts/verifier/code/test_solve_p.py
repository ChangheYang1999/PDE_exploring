"""checks of CharSolver.solve_p: (1) residual f(u) = 0 and agreement with a long, contractive fixed-point loop
p <- 1/c_l(p) where that loop converges; (2) forward-AD tangent of (c, c_l, p) vs central finite differences."""
import sys, numpy as np, torch, math
sys.path.insert(0, 'code')
from forced_char import ForcedSolver
import torch.autograd.forward_ad as fwAD
edges = np.concatenate([[0.0], np.geomspace(1e-6, 0.1, 12), np.geomspace(0.1, 10, 25)[1:], np.geomspace(10, 1e4, 16)[1:]])
S = ForcedSolver(edges, 8, 64, 1e-6, 'cuda')
d0 = torch.load('runs/fc_mu1_L4_h0.100.pt', weights_only=False)
xi = d0['xi'].cuda()
for h, mu in [(0.1, 1.0), (0.2, 1.0), (1.0, 0.0)]:
    rho = xi**2
    c, b, cl, l, p, f = S.solve_p(rho, h, mu, 0.6)
    pp = 0.6
    for k in range(2000):
        cc, bb = S.moments(rho, pp); cl2, _ = S.jet(h*cc + (1 - h)*mu, h*bb); pn = float(1/cl2)
        if abs(pn - pp) < 1e-15: break
        pp = pn
    print(f'h={h} mu={mu}: solve_p c={float(c):.12f} cl={float(cl):.12f} p={float(p):.12f} |f|={f:.1e};  loop p={pp:.12f} ({k} its) cl={float(cl2):.12f}')
# AD vs FD
torch.manual_seed(0)
u = torch.randn_like(xi)*S.R/(1 + S.R**2)**0.5
h, mu = 0.2, 1.0
def fun(z):
    c, b, cl, l, p, f = S.solve_p(z**2, h, mu, 0.6)
    return torch.stack([c, cl, p])
with fwAD.dual_level():
    t = fwAD.unpack_dual(fun(fwAD.make_dual(xi, u))).tangent
for e in [1e-4, 1e-5, 1e-6]:
    fd = (fun(xi + e*u) - fun(xi - e*u))/(2*e)
    print('eps', e, 'AD', t.cpu().numpy(), 'FD', fd.cpu().numpy(), 'rel diff', float((t - fd).abs().max()/t.abs().max()))
