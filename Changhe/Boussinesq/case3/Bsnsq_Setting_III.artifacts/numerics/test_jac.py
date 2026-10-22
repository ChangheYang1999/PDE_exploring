"""Finite-difference Jacobian consistency test at a saved state (shift 2).
For a few active columns j and steps h, D_h = (R(cG + h e_j) - R(cG))/h; a smooth residual gives D_h differences
that shrink linearly with h; FD noise (trajectory-stop quantization, RK4) shows up as differences growing like 1/h.
Usage: python3 code/test_jac.py runs/fb30i_eps0.1.npz"""
import sys, os, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
f = sys.argv[1]; d = np.load(f); dev = 'cuda'
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else None
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=12, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=6000, rmap=str(d['rmap']),
                   beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True
res.eps = float(d['eps']); res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None
cG = torch.tensor(d['cG'], dtype=DT, device=dev)
act = torch.nonzero(res.active)[:, 0]
Nb = res.Nb
# columns: modes 0, 1, 3, 6 at inner / middle / outer radial splines
cols = []
for k in [0, 1, 3, 6]:
    ak = act[(act // Nb) == k]
    for frac in [0.1, 0.5, 0.9]:
        cols.append(int(ak[min(len(ak) - 1, int(frac * len(ak)))]))
hs = [1e-7, 1e-6, 1e-5, 1e-4]
N = cG.numel()
E = [cG]
for j in cols:
    for h in hs:
        e = cG.clone(); e[j] += h; E.append(e)
Rb = res.run(torch.stack(E, 0))
R0 = Rb[0]
print(f"state {f}: eps={res.eps} beta_fixed={beta_fixed} obj={(R0**2).sum().item():.4e} Nq={R0.numel()} unfinished={res.n_unfinished}")
print(f"{'col':>5} {'k':>2} {'j':>3} | " + ' '.join(f"{'|D_h| h=%.0e' % h:>16}" for h in hs) + " | rel.diff(1e-7,1e-6) (1e-6,1e-5) (1e-5,1e-4)")
i = 1
for j in cols:
    Ds = []
    for h in hs:
        Ds.append((Rb[i] - R0) / h); i += 1
    norms = [D.norm().item() for D in Ds]
    rd = [((Ds[a] - Ds[a + 1]).norm() / max(Ds[a + 1].norm().item(), 1e-300)).item() for a in range(len(hs) - 1)]
    print(f"{j:5d} {j // Nb:2d} {j % Nb:3d} | " + ' '.join(f"{n:16.6e}" for n in norms) + " | " + ' '.join(f"{v:10.3e}" for v in rd))
