"""Off-node self-consistency check of a forced/B2 state: evaluate the transported fields of the state's own velocity on a
much finer angular residual set (Nphi_res_fine) and compare with the represented fields: max weighted mismatch
(G_char - G_rep)/D_G, (F_char - F_rep)/D_F, and the grouped normalized proxies. This approximates the off-node forced
residual that the fit nodes cannot see (verifier 20:23Z). Usage: python3 code/offnode_check.py state.npz [--Nphi_res 48]"""
import sys, os, argparse, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--Nphi_res', type=int, default=48); ap.add_argument('--s0', type=str, default='')
a = ap.parse_args(); dev = 'cuda'
d = np.load(a.state)
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else bb
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
res = CharResidual(b, L, bb, Nphi_res=a.Nphi_res, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=12000, rmap=str(d['rmap']), beta_fixed=beta_fixed, wc=0.0, include_RF=True)
res.use_graph = True; res.free_a0 = False
res.eps = float(d['eps']); res.cG_ext = torch.tensor(d['cG_ext'], dtype=DT, device=dev) if d['cG_ext'].size else None
lam = float(d['lam']) if 'lam' in d.files else 0.0
source_mode = str(d['source_mode']) if 'source_mode' in d.files else ''
if source_mode == 'fixed_velocity_block' and d['cG_f'].size:
    # retied-basis lambda state: source f in the SEED basis, added as a fixed velocity block (fixedsrc.py)
    from bq3core import Geometry
    from fixedsrc import make_source_block
    g_seed = Geometry(b, float(d['beta_seed']), L, rmap=str(d['rmap']))
    make_source_block(g_seed, torch.tensor(d['cG_f'], dtype=DT, device=dev), res, lam)
elif 'cG_f_effective' in d.files and d['cG_f_effective'].size:
    res.cG_f = torch.tensor(d['cG_f_effective'], dtype=DT, device=dev)      # lam * f in the stage basis (fixed-basis / re-projected modes)
elif 'cG_f' in d.files and d['cG_f'].size:
    res.cG_f = (lam if lam > 0 else 1.0) * torch.tensor(d['cG_f'], dtype=DT, device=dev)
elif a.s0:
    res.cG_f = res.cG_ext - torch.tensor(np.load(a.s0)['cG'], dtype=DT, device=dev)
a0 = float(d['a0']) if 'a0' in d.files else 1.0
cG = torch.tensor(d['cG'], dtype=DT, device=dev); cF = torch.tensor(d['cF'], dtype=DT, device=dev)
R, info = res.run(cG[None], return_all=True)
Gc = a0 * info['G_char'][0]; Fc = a0 * info['F_char'][0]
Grep = res.gres.Phi0G @ cG; Frep = res.gres.Phi0F @ cF
mG = res.wG * (Gc - Grep); mF = res.wF * (Fc - Frep)
rr = res.gres.rr
out = dict(state=a.state, eps=res.eps, lam=lam, source_mode=source_mode, a0=a0, Nphi_res_fine=a.Nphi_res, Npts=int(mG.numel()), unfinished=res.n_unfinished,
           max_wG_mismatch=mG.abs().max().item(), max_wF_mismatch=mF.abs().max().item(),
           rel_G=(mG.abs().max() / (res.wG * Gc).abs().max()).item(), rel_F=(mF.abs().max() / (res.wF * Fc).abs().max()).item())
bands = {}
for lo, hi in [(0, 0.3), (0.3, 1), (1, 3), (3, 10), (10, 100), (100, 1e4), (1e4, 1e99)]:
    m = (rr >= lo) & (rr < hi)
    if m.any():
        bands[f'{lo:g}-{hi:g}'] = dict(wG=mG[m].abs().max().item(), wF=mF[m].abs().max().item(),
                                       relG=(mG[m].abs().max() / (res.wG * Gc)[m].abs().max()).item())
out['bands'] = bands
# same quantities restricted to the production angles (every other node when Nphi_res_fine = 2 x 12 etc.) are not available here;
print(json.dumps(out, indent=1))
