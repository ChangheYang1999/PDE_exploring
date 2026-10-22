"""Transplant a state (cF, cG) to a new basis (K, Nt, Nphi, grade, L, beta_basis) by weighted least squares on point values."""
import sys, os, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from solve import eval_fields_at
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('dst')
ap.add_argument('--K', type=int); ap.add_argument('--Nt', type=int); ap.add_argument('--Nphi', type=int)
ap.add_argument('--grade', type=float); ap.add_argument('--L', type=float); ap.add_argument('--beta_basis', type=float)
ap.add_argument('--ngc', type=int, default=7)
ap.add_argument('--rmap', type=str, default=None, choices=[None, 'r', 'r2'])
a = ap.parse_args()
dev = 'cuda'
d = np.load(a.src)
K0, Nt0, Nphi0, grade0 = int(d['K']), int(d['Nt']), int(d['Nphi']), float(d['grade'])
L0, bb0 = float(d['L']), float(d.get('beta_basis', d['beta']))
rmap0 = str(d['rmap']) if 'rmap' in d else 'r'
b0 = Basis(Nt0, int(d['deg']), K0, Nphi0, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade0)
cF0 = torch.tensor(d['cF'], dtype=DT, device=dev); cG0 = torch.tensor(d['cG'], dtype=DT, device=dev)
K, Nt, Nphi = a.K or K0, a.Nt or Nt0, a.Nphi or Nphi0
grade = a.grade or grade0; L = a.L or L0; bb = a.beta_basis or bb0
b = Basis(Nt, 5, K, Nphi, ng_coll=a.ngc, m_reg=2, device=dev, grade=grade)
rmap = a.rmap or rmap0
g = Geometry(b, bb, L, rmap=rmap)
F, G = eval_fields_at(b0, bb0, L0, cF0, cG0, g.x, g.y, rmap=rmap0)
act = g.active
DF = ((1 - b.t_coll_t) ** g.pF)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
DG = ((1 - b.t_coll_t) ** g.pG)[:, None].expand(b.Nc, b.Nphi).reshape(-1)
cF = torch.zeros(K * b.Nb, dtype=DT, device=dev); cG = torch.zeros_like(cF)
cF[act] = torch.linalg.lstsq((g.Phi0F / DF[:, None])[:, act], (F / DF)[:, None], driver='gels').solution[:, 0]
cG[act] = torch.linalg.lstsq((g.Phi0G / DG[:, None])[:, act], (G / DG)[:, None], driver='gels').solution[:, 0]
eF = ((g.Phi0F @ cF - F) / DF).abs().max().item(); eG = ((g.Phi0G @ cG - G) / DG).abs().max().item()
print(f"transplant {a.src} -> {a.dst}: K {K0}->{K}, Nt {Nt0}->{Nt}, L {L0}->{L}, beta_b {bb0}->{bb}, rmap {rmap0}->{rmap}; fit err F {eF:.2e} G {eG:.2e}; "
      f"c_old={float(d['beta'])/2+1:.6f} c_new={(g.c_op @ cG).item():.6f}")
out = {k: d[k] for k in d.files}
out.update(dict(cF=cF.cpu().numpy(), cG=cG.cpu().numpy(), K=K, Nt=Nt, Nphi=Nphi, grade=grade, L=L, beta_basis=bb, ngc=a.ngc, deg=5, mreg=2, rmap=rmap))
if 'cG_f' in d.files and d['cG_f'].size > 0:
    # the fixed source keeps its OWN basis (verifier 00:56Z): record the original basis if the state has no seed metadata yet; seed_* keys
    # already present are copied verbatim above. The effective (re-projected) source of older modes is dropped (basis-specific).
    if 'seed_K' not in d.files:
        out.update(dict(seed_K=K0, seed_Nt=Nt0, seed_deg=int(d['deg']), seed_Nphi=Nphi0, seed_ngc=int(d['ngc']), seed_mreg=int(d['mreg']), seed_grade=grade0, seed_L=L0, seed_rmap=rmap0))
        print('transplant: recorded the ORIGINAL basis as the seed-source basis (seed_*); cG_f and beta_seed copied verbatim')
    out['cG_f_effective'] = np.zeros(0)
    out['transplanted_from'] = a.src
if 'cG_ext' in d and d['cG_ext'].size > 0:
    cGe = torch.tensor(d['cG_ext'], dtype=DT, device=dev)
    _, Ge = eval_fields_at(b0, bb0, L0, cF0, cGe, g.x, g.y, rmap=rmap0)
    cGe_new = torch.zeros_like(cG); cGe_new[act] = torch.linalg.lstsq((g.Phi0G / DG[:, None])[:, act], (Ge / DG)[:, None], driver='gels').solution[:, 0]
    out['cG_ext'] = cGe_new.cpu().numpy()
np.savez(a.dst, **out)
