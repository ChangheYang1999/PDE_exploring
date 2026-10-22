import sys, time, torch, numpy as np
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, Problem, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
dev = 'cuda'
b = Basis(40, 5, 16, 32, ng_coll=7, m_reg=2, device=dev, grade=1.5)
K, Nb = b.K, b.Nb
def init(res, c0=2.5, beta=3.0):
    cG0 = torch.zeros(K * Nb, dtype=DT, device=dev); cG0[:Nb] = 4 / beta
    g0 = res.g; tq = b.t_quad_t; wq = b.w_quad_t * g0.drdtq
    I = (wq * tq * (1 - tq) ** (1 + res.beta_basis / 2)).sum().item(); cG0[Nb:2 * Nb] = -4 * c0 / I
    cG0[2*Nb:3*Nb] = 0.3
    return cG0
out = {}
for dt in [0.04, 0.02, 0.01]:
    res = CharResidual(b, 1.0, 3.0, Nphi_res=16, r_in=1e-3, dt=dt, device=dev)
    cG0 = init(res)
    torch.cuda.synchronize(); t0 = time.time()
    R, info = res.run(cG0[None], return_all=True); torch.cuda.synchronize()
    out[dt] = (info['F_char'][0].clone(), info['G_char'][0].clone())
    print(f'dt={dt}: {time.time()-t0:.1f}s steps={res.steps_used} max|R|={R[0].abs().max().item():.4e}')
for dt in [0.04, 0.02]:
    dF = (out[dt][0] - out[0.01][0]).abs() / (out[0.01][0].abs() + 1e-300); dG = (out[dt][1] - out[0.01][1]).abs() / (out[0.01][1].abs().max())
    print(f'dt={dt} vs 0.01: max rel dF_char={dF.max().item():.3e}  max dG_char/max|G|={dG.max().item():.3e}')
res = CharResidual(b, 1.0, 3.0, Nphi_res=16, r_in=1e-3, dt=0.02, device=dev)
cG0 = init(res)
for Bn in [32, 64]:
    cGb = cG0[None].expand(Bn, -1).clone(); cGb[1:] += 1e-6 * torch.randn(Bn - 1, K * Nb, dtype=DT, device=dev)
    torch.cuda.reset_peak_memory_stats(); torch.cuda.synchronize(); t0 = time.time()
    R = res.run(cGb); torch.cuda.synchronize()
    print(f'B={Bn}: {time.time()-t0:.1f}s  mem GB {torch.cuda.max_memory_allocated()/1e9:.1f}')
# r_in convergence
for rin in [3e-3, 1e-3, 3e-4]:
    res = CharResidual(b, 1.0, 3.0, Nphi_res=16, r_in=rin, dt=0.02, device=dev)
    R, info = res.run(cG0[None], return_all=True)
    out[('rin', rin)] = (info['F_char'][0].clone(), info['G_char'][0].clone())
    print(f'r_in={rin}: steps={res.steps_used}')
for rin in [3e-3, 1e-3]:
    dF = (out[('rin', rin)][0] - out[('rin', 3e-4)][0]).abs() / (out[('rin', 3e-4)][0].abs() + 1e-300)
    dG = (out[('rin', rin)][1] - out[('rin', 3e-4)][1]).abs() / out[('rin', 3e-4)][1].abs().max()
    print(f'r_in={rin} vs 3e-4: max rel dF={dF.max().item():.3e} max dG/max|G|={dG.max().item():.3e}')
