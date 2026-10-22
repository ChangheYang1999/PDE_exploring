import sys, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
dev = 'cuda'
b = Basis(40, 5, 12, 24, ng_coll=7, m_reg=2, device=dev, grade=1.5)
res = CharResidual(b, 1.5, 3.0, Nphi_res=64, r_in=1e-3, dt=0.02, device=dev, rmap='r2', beta_fixed=3.0)
res.use_graph = True
g0 = res.g; K, Nb = b.K, b.Nb; act = g0.active
Dt = ((1 - b.t_coll_t) ** g0.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1); wfit = 1 / Dt
Gt = torch.exp(-(g0.x ** 2 + (g0.y - 2.87) ** 2) / 2)
cfit = torch.zeros(K * Nb, dtype=DT, device=dev)
cfit[act] = torch.linalg.lstsq((g0.Phi0G * wfit[:, None])[:, act], (Gt * wfit)[:, None], driver='gels').solution[:, 0]
cG = (2.5 / (g0.c_op @ cfit).item()) * cfit
res.eps = 0.0; res.cG_ext = cG
R, info = res.run(torch.zeros(1, K * Nb, dtype=DT, device=dev), return_all=True)
Nc, Np = res.bres.Nc, 64
Gc = info['G_char'][0].reshape(Nc, Np).cpu().numpy(); r = res.X0[:, 0].reshape(Nc, Np).cpu().numpy(); y = res.X0[:, 1].reshape(Nc, Np).cpu().numpy()
rr = np.sqrt(r**2 + y**2)[:, 0]
phi = res.bres.phi
print("eps=0 transported G (a0 = %.4f): cosine-mode spectrum |g_k| at selected radii (DCT of G over phi)" % info['a0'].item())
for target in [0.5, 1.2, 2.0, 2.8, 4.0, 8.0]:
    i = int(np.argmin(np.abs(rr - target)))
    row = Gc[i]
    coef = [2.0 / Np * np.sum(row * np.cos(k * phi)) for k in range(0, 24)]
    coef[0] /= 2
    print(f" r={rr[i]:6.2f}: max G={row.max():6.2f} min={row.min():6.2f}  |g_k| k=0..23:", ' '.join(f"{abs(c):.2f}" for c in coef))
