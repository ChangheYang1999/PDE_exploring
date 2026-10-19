"""Forced moment law (c_l - 1) pi c = h Q + (1-h) Q_E at saved forced states (code/forced_char.py, forced_pal.py),
with the analytic far-field tail of Q added: the Q integrand per unit r, f(r) = r int rho W.grad phi dth, behaves like
f(L) (r/L)^{2p-3} beyond L (rho, W ~ r^p, grad phi ~ r^-4), so Q_tail = f(L) L/(2 - 2p); f(L) is extrapolated from
the last Gauss node r_N by (L/r_N)^{2p-3}. Q_E has no tail (E is Gaussian)."""
import sys, math, numpy as np, torch
sys.path.insert(0, 'code')
from forced_char import ForcedSolver
cache = {}
for f in sys.argv[1:]:
    D = torch.load(f, weights_only=False)
    A = D['args']; key = (len(D['edges']), float(D['edges'][-1]), D['nt'])
    if key not in cache: cache[key] = ForcedSolver(D['edges'], D['q'], D['nt'], D['r1'], 'cuda')
    S = cache[key]
    h = float(D['h']); d = D['d']; p = d['p']
    S.set_forcing(h, A['mu'], A['LE'])
    xi = D['xi'].cuda(); rho = xi**2
    lhs, rhs, Q, QE = S.qlaw(xi, d)
    W1, W2 = S.velocity(rho, p)
    g1 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.cs - torch.cos(3*S.TH)*S.sn)
    g2 = 3*S.R**-4*(-torch.sin(3*S.TH)*S.sn + torch.cos(3*S.TH)*S.cs)
    fr = (S.r*torch.sum(rho*(W1*g1 + W2*g2), 1)*(2*math.pi/S.nt))
    rN = float(S.r[-1]); fL = float(fr[-1])*(S.L/rN)**(2*p - 3)
    Qt = fL*S.L/(2 - 2*p)
    rhs_t = h*(Q + Qt) + (1 - h)*QE
    print(f"{f.split('/')[-1]:28s} h={h:.4f} c={d['c']:9.4f} cl={d['cl']:.5f} p={p:.4f}  lhs={lhs:9.5f}  rhs={rhs:9.5f}  "
          f"rhs+tail={rhs_t:9.5f}  rel.defect={abs(lhs - rhs_t)/abs(lhs):.1e} (no tail {abs(lhs - rhs)/abs(lhs):.1e})")
