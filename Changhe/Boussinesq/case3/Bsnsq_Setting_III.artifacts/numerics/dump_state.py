import sys, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
dev = 'cuda'
f = sys.argv[1]
d = np.load(f)
K, Nt, Nphi, grade = int(d['K']), int(d['Nt']), int(d['Nphi']), float(d['grade'])
bb, L, eps, rmap = float(d['beta_basis']), float(d['L']), float(d['eps']), str(d['rmap'])
bf = float(d['beta_fixed']) if 'beta_fixed' in d and float(d['beta_fixed']) > 0 else None
b = Basis(Nt, 5, K, Nphi, ng_coll=int(d['ngc']), m_reg=2, device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=12, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, rmap=rmap, beta_fixed=bf, eps=eps,
                   cG_ext=torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None)
res.use_graph = True
cG = torch.tensor(d['cG'], dtype=DT, device=dev)
R, info = res.run(cG[None], return_all=True)
print(f"{f}: eps={eps} beta={info['beta'].item():.4f} obj={(R**2).sum().item():.4e} unfinished={res.n_unfinished} steps={res.steps_used}")
Nc, Np = res.bres.Nc, res.bres.Nphi
x = res.X0[:, 0].reshape(Nc, Np).cpu().numpy(); y = res.X0[:, 1].reshape(Nc, Np).cpu().numpy()
r = np.sqrt(x**2 + y**2)
Gc = info['G_char'][0].reshape(Nc, Np).cpu().numpy(); Gr = info['G_rep'][0].reshape(Nc, Np).cpu().numpy()
Fc = info['F_char'][0].reshape(Nc, Np).cpu().numpy(); Fr = info['F_rep'][0].reshape(Nc, Np).cpu().numpy()
RG = info['RG'][0].reshape(Nc, Np).cpu().numpy(); RF = info['RF'][0].reshape(Nc, Np).cpu().numpy()
i, j = np.unravel_index(np.abs(RG).argmax(), RG.shape)
print(f"max|wRG| = {abs(RG[i,j]):.3f} at r={r[i,j]:.3f}, y/r={y[i,j]/r[i,j]:+.2f}: G_char={Gc[i,j]:.3f} G_rep={Gr[i,j]:.3f}")
print("rows: r ; columns phi index j=0 (y<0 axis side) .. 11 (y>0): G_char / G_rep")
for ii in range(0, Nc, max(1, Nc // 16)):
    print(f" r={r[ii,0]:8.3g}: Gc=", ' '.join(f"{Gc[ii,jj]:6.2f}" for jj in [0,2,4,6,8,10,11]), " Gr=", ' '.join(f"{Gr[ii,jj]:6.2f}" for jj in [0,2,4,6,8,10,11]), f"  Fc/Fr(top)={Fc[ii,11]:.3f}/{Fr[ii,11]:.3f}")
