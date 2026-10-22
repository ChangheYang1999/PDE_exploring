import sys, numpy as np, torch
sys.path.insert(0, 'code')
from bq3core import Basis, Geometry, DT
torch.set_default_dtype(DT)
f = sys.argv[1]
d = np.load(f)
b = Basis(32, 5, 12, 12, ng_coll=7, m_reg=2, device='cuda', grade=1.5)
g = Geometry(b, 3.0, 1.5)
x = g.x.cpu().numpy(); y = g.y.cpu().numpy(); r = g.rr.cpu().numpy()
Gext = (g.Phi0G @ torch.tensor(d['cG_ext'], dtype=DT, device='cuda')).cpu().numpy()
Gch = d['G']
Nc, Nphi = b.Nc, b.Nphi
print(f"{f}: c_in={float(d['c_in']):.3f} c_out={float(d['c_out']):.3f} beta={float(d['beta']):.3f}")
print("Omega_ext vs Omega_char along rays (phi index j: 0 = below axis side y<0 ... Nphi-1 = y>0):")
rg = r.reshape(Nc, Nphi)[:, 0]
for j in [1, 4, 6, 7, 9, 10]:
    print(f"  phi={b.phi[j]:.2f} (y/r={-np.cos(b.phi[j]):+.2f}):")
    idx = [i for i in range(0, Nc, Nc // 10)]
    print("     r      :", ' '.join(f"{rg[i]:9.3g}" for i in idx))
    print("     Om_ext :", ' '.join(f"{(x*Gext).reshape(Nc,Nphi)[i,j]:9.3g}" for i in idx))
    print("     Om_char:", ' '.join(f"{(x*Gch).reshape(Nc,Nphi)[i,j]:9.3g}" for i in idx))
