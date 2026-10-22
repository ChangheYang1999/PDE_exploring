import sys, time, torch, numpy as np
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, Problem, DT
from charnewton import CharResidual, BSplineTorch
torch.set_default_dtype(DT)
dev = 'cuda'
b = Basis(40, 5, 16, 32, ng_coll=7, m_reg=2, device=dev, grade=1.5)
# test de Boor evaluator against scipy
spl = BSplineTorch(b.knots, b.deg, dev)
tq = torch.rand(2000, dtype=DT, device=dev) * 0.999
span, Nv, dNv = spl.eval(tq)
Bs, dBs = b._design(tq.cpu().numpy())
full = torch.zeros(2000, b.Nb, dtype=DT, device=dev); dfull = torch.zeros_like(full)
idx = span[:, None] + torch.arange(b.deg + 1, device=dev)[None, :]
full.scatter_(1, idx, Nv); dfull.scatter_(1, idx, dNv)
print('de Boor vs scipy: max|B err| =', (full.cpu().numpy() - Bs).max(), ' max|dB err| =', np.abs(dfull.cpu().numpy() - dBs).max())
res = CharResidual(b, 1.0, 3.0, Nphi_res=16, r_in=1e-3, dt=0.02, device=dev)
K, Nb = b.K, b.Nb
cG0 = torch.zeros(K * Nb, dtype=DT, device=dev); cG0[:Nb] = 4 / 3
g0 = res.g
cG0[Nb+1:2 * Nb] = -2.0; cG0[2*Nb+2:3*Nb] = 0.3
print('c0 =', (g0.c_op @ cG0).item())
for Bn in [1, 8]:
    cGb = cG0[None].expand(Bn, -1).clone()
    cGb[1:] += 1e-6 * torch.randn(Bn - 1, K * Nb, dtype=DT, device=dev) if Bn > 1 else 0
    torch.cuda.synchronize(); t0 = time.time()
    R, info = res.run(cGb, return_all=True)
    torch.cuda.synchronize()
    print(f'B={Bn}: {time.time()-t0:.1f}s steps={res.steps_used} unfinished={res.n_unfinished} beta={info["beta"][0].item():.6f} '
          f'max|R|={R[0].abs().max().item():.3e} rms={R[0].pow(2).mean().sqrt().item():.3e} max|RF|={info["RF"][0].abs().max().item():.3e}')
    print('   mem GB', torch.cuda.max_memory_allocated() / 1e9)
