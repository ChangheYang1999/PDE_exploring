import sys, time, torch, numpy as np
sys.path.insert(0, 'code')
from bq3core import Basis, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
dev = 'cuda'
b = Basis(32, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=1.5)
res = CharResidual(b, 1.5, 3.0, Nphi_res=12, r_in=1e-3, dt=0.02, device=dev)
g0 = res.g; K, Nb = b.K, b.Nb; act = g0.active
Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1 / Dt
Gt = torch.exp(-(g0.x ** 2 + (g0.y - 2.85) ** 2) / 2)
cfit = torch.zeros(K * Nb, dtype=DT, device=dev)
cfit[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
cG = (2.5 / (g0.c_op @ cfit).item()) * cfit
for Bn in [1, 16]:
    cGb = cG[None].expand(Bn, -1).clone()
    if Bn > 1: cGb[1:] += 1e-4 * torch.randn(Bn - 1, K * Nb, dtype=DT, device=dev)
    out = {}
    for ug in [False, True]:
        torch.cuda.synchronize(); t0 = time.time()
        R, info = res.run(cGb, return_all=True, use_graph=ug); torch.cuda.synchronize()
        out[ug] = (R.clone(), info['F_char'].clone(), info['G_char'].clone())
        print(f"B={Bn} graph={ug}: {time.time()-t0:.1f}s steps={res.steps_used} unfinished={res.n_unfinished} beta={info['beta'][0].item():.6f} max|R|={R.abs().max().item():.4e}")
    print(f"   max|R diff| = {(out[True][0]-out[False][0]).abs().max().item():.2e}  max|F diff| = {(out[True][1]-out[False][1]).abs().max().item():.2e}  max|G diff| = {(out[True][2]-out[False][2]).abs().max().item():.2e}")
