import sys, torch, numpy as np
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
dev = 'cuda'
for rmap, grade in [('r', 1.5), ('r2', 1.5)]:
    b = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=grade)
    res = CharResidual(b, 1.5, 3.0, Nphi_res=12, device=dev, rmap=rmap)
    g = res.g; K, Nb = b.K, b.Nb; act = g.active
    Dt = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1 / Dt
    Gt = torch.exp(-(g.x ** 2 + (g.y - 2.85) ** 2) / 2)
    cfit = torch.zeros(K * Nb, dtype=DT, device=dev)
    cfit[act] = torch.linalg.lstsq((g.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
    cG = (2.5 / (g.c_op @ cfit).item()) * cfit
    beta, nodal, jet = res.prepare(cG[None])
    # off-node points: finer geometry (9 Gauss points, 48 angles)
    b2 = Basis(40, 5, 12, 48, ng_coll=9, m_reg=2, device=dev, grade=grade)
    g2 = Geometry(b2, 3.0, 1.5, rmap=rmap)
    X = torch.stack([g2.x, g2.y], 1)[None]
    W, aux = res.velocity(X, beta, nodal)
    U1d = g2.M_U1 @ cG; U2d = g2.M_U2 @ cG
    W1d = beta[0] * g2.x + U1d; W2d = beta[0] * g2.y + U2d
    e1 = (W[0, :, 0] - W1d).abs(); e2 = (W[0, :, 1] - W2d).abs()
    sc = 1 + g2.rr
    rr = g2.rr
    print(f"[{rmap}] off-node velocity error: max|dW1|/(1+r) = {(e1/sc).max().item():.2e}, max|dW2|/(1+r) = {(e2/sc).max().item():.2e}")
    for lo, hi in [(0, 0.3), (0.3, 3), (3, 100), (100, 1e99)]:
        m = (rr >= lo) & (rr < hi)
        print(f"     r in [{lo:g},{hi:g}): max|dW|/(1+r) = {torch.maximum(e1, e2)[m].div(sc[m]).max().item():.2e}  (n={int(m.sum())})")
    # divergence of the interpolated U by central differences
    h = 1e-5
    def Wat(P):
        return res.velocity(P[None], beta, nodal)[0][0]
    P = torch.stack([g2.x, g2.y], 1)
    sel = (g2.rr > 0.01) & (g2.rr < 1e3)
    P = P[sel]
    dU1dx = (Wat(P + torch.tensor([h, 0.0], device=dev))[:, 0] - Wat(P - torch.tensor([h, 0.0], device=dev))[:, 0]) / (2 * h)
    dU2dy = (Wat(P + torch.tensor([0.0, h], device=dev))[:, 1] - Wat(P - torch.tensor([0.0, h], device=dev))[:, 1]) / (2 * h)
    div = dU1dx + dU2dy - 2 * beta[0]       # div W = 2 beta exactly
    print(f"     max |div U_interp| (FD, 0.01<r<1e3) = {div.abs().max().item():.2e}")
