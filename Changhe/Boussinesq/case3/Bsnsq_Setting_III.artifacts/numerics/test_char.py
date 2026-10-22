import sys, os, time, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, Problem, DT
from charsolve import CharModel
torch.set_default_dtype(DT)
dev = 'cuda'
beta_b, L = 3.0, 1.0
b = Basis(40, 5, 16, 32, ng_coll=7, m_reg=2, device=dev, grade=1.5)
g = Geometry(b, beta_b, L)
K, Nb = b.K, b.Nb
# a test state: F = D(t), G = (4/beta) D(t) + g_1 mode giving c = 2.5
cF = torch.zeros(K * Nb, dtype=DT, device=dev); cG = torch.zeros(K * Nb, dtype=DT, device=dev)
cF[:Nb] = 1.0; cG[:Nb] = 4 / 3.0
tq = b.t_quad_t; wq = b.w_quad_t * g.drdtq
I = (wq * tq * (1 - tq) ** (1 + beta_b / 2)).sum().item(); gamma = 4 * 2.5 / I
cG[Nb:2 * Nb] = -gamma
cG[2 * Nb:3 * Nb] = 0.3   # some g_2 content
cF[Nb:2 * Nb] = 0.2
m = CharModel(b, L, r_in=1e-3, dt=0.02, device=dev)
m.set_state(cF, cG, g)
print('beta_dyn =', m.beta, ' jet:', {k: float(v) for k, v in m.jet.items()})
# consistency of rhs at collocation points vs direct operators
X = torch.stack([g.x, g.y], 1)
W, Thx = m.rhs(X)
p = Problem(g); f = p.fields(cF, cG)
U1d = g.M_U1 @ cG; U2d = g.M_U2 @ cG
W1d = m.beta * g.x + U1d; W2d = m.beta * g.y + U2d
Thxd = 2 * g.x * f['F1']
print('max|W1 - direct| =', (W[:, 0] - W1d).abs().max().item(), ' max|W1| =', W1d.abs().max().item())
print('max|W2 - direct| =', (W[:, 1] - W2d).abs().max().item(), ' max|W2| =', W2d.abs().max().item())
print('max|Thx - direct| =', (Thx - Thxd).abs().max().item(), ' max|Thx| =', Thxd.abs().max().item())
# off-node points: compare interpolation against a finer Geometry evaluation
b2 = Basis(40, 5, 16, 32, ng_coll=9, m_reg=2, device=dev, grade=1.5)
g2 = Geometry(b2, beta_b, L)
X2 = torch.stack([g2.x, g2.y], 1)
W2_, Thx2 = m.rhs(X2)
U1d2 = g2.M_U1 @ cG; U2d2 = g2.M_U2 @ cG
e1 = (W2_[:, 0] - (m.beta * g2.x + U1d2)).abs(); e2 = (W2_[:, 1] - (m.beta * g2.y + U2d2)).abs()
sc = (1 + g2.rr)
print('off-node: max|dW1|/(1+r) =', (e1 / sc).max().item(), ' max|dW2|/(1+r) =', (e2 / sc).max().item())
p2 = Problem(g2); f2 = p2.fields(cF, cG)
print('off-node: max|dThx|/(1+r) =', ((Thx2 - 2 * g2.x * f2['F1']).abs() / sc).max().item())
# run characteristics from the collocation points
t0 = time.time()
Th, Om, T, Xe = m.run(X)
torch.cuda.synchronize()
print(f'run: {time.time()-t0:.1f}s steps {m.steps_used} unfinished {m.n_unfinished}  T range {T.min().item():.2f}..{T.max().item():.2f}')
Fch = Th / g.x ** 2; Gch = Om / g.x
rr = g.rr.cpu().numpy()
for lo, hi in [(0, 0.01), (0.01, 0.1), (0.1, 1), (1, 10), (10, 100), (100, 1e4), (1e4, 1e99)]:
    mm = (rr >= lo) & (rr < hi)
    if mm.any():
        print(f'r in [{lo:g},{hi:g}): F_char range [{Fch[mm].min().item():.4g},{Fch[mm].max().item():.4g}] F range [{f["F"][mm].min().item():.4g},{f["F"][mm].max().item():.4g}]  G_char [{Gch[mm].min().item():.4g},{Gch[mm].max().item():.4g}] G [{f["G"][mm].min().item():.4g},{f["G"][mm].max().item():.4g}]')
