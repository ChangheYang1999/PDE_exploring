"""transported_tail.py -- where and how the transported fields of a lambda/eps state fail to be represented: local radial exponents of
max_phi |G_char| and of the represented max_phi |G_rep| per decade (basis envelope: r^{-1-1/b}), the angular profile of the weighted
mismatch at selected far radii, and the mismatch per angular mode (cosine transform in phi of (G_char - G_rep)/D_G at each radius).
Usage: python3 code/transported_tail.py state.npz [--Nphi_res 48]"""
import sys, os, argparse, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from charnewton import CharResidual
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--Nphi_res', type=int, default=48)
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
    from fixedsrc import make_source_block
    if 'seed_K' in d.files:
        bs = Basis(int(d['seed_Nt']), int(d['seed_deg']), int(d['seed_K']), int(d['seed_Nphi']), ng_coll=int(d['seed_ngc']), m_reg=int(d['seed_mreg']), device=dev, grade=float(d['seed_grade']))
        gs = Geometry(bs, float(d['beta_seed']), float(d['seed_L']), rmap=str(d['seed_rmap']))
    else:
        gs = Geometry(b, float(d['beta_seed']), L, rmap=str(d['rmap']))
    make_source_block(gs, torch.tensor(d['cG_f'], dtype=DT, device=dev), res, lam)
elif 'cG_f_effective' in d.files and d['cG_f_effective'].size:
    res.cG_f = torch.tensor(d['cG_f_effective'], dtype=DT, device=dev)
elif 'cG_f' in d.files and d['cG_f'].size:
    res.cG_f = (lam if lam > 0 else 1.0) * torch.tensor(d['cG_f'], dtype=DT, device=dev)
a0 = float(d['a0']) if 'a0' in d.files else 1.0
cG = torch.tensor(d['cG'], dtype=DT, device=dev); cF = torch.tensor(d['cF'], dtype=DT, device=dev)
res.cF_fixed = cF / a0          # transport the SAVED temperature pair (no refit on the diagnostic grid; astra path1)
R, info = res.run(cG[None], return_all=True)
Nc, Np = res.bres.Nc, a.Nphi_res
Gc = (a0 * info['G_char'][0]).reshape(Nc, Np); Grep = (res.gres.Phi0G @ cG).reshape(Nc, Np)
Fc = (a0 * info['F_char'][0]).reshape(Nc, Np); Frep = (res.gres.Phi0F @ cF).reshape(Nc, Np)
DG = res.DresG.reshape(Nc, Np)[:, 0]; DF = res.DresF.reshape(Nc, Np)[:, 0]
r = res.gres.r.cpu().numpy(); phi = res.bres.phi
mG = ((Gc - Grep) / DG[:, None]).cpu().numpy(); mF = ((Fc - Frep) / DF[:, None]).cpu().numpy()
Gc_n = Gc.cpu().numpy(); Grep_n = Grep.cpu().numpy()
out = dict(state=a.state, lam=lam, source_mode=source_mode, beta=beta_fixed, beta_basis=bb, unfinished=res.n_unfinished, temperature='saved cF transported (cF_fixed), no refit')
# local exponents per decade of max_phi |G| (transported vs represented) ; envelope exponent of the basis is -(1 + 1/bb)
def expo(arr, lo, hi):
    m = (r >= lo) & (r < hi)
    if m.sum() < 3: return None
    y = np.log(np.abs(arr[m]).max(1) + 1e-300); x = np.log(r[m])
    return float(np.polyfit(x, y, 1)[0])
out['exponents'] = {f'{lo:g}-{hi:g}': dict(G_char=expo(Gc_n, lo, hi), G_rep=expo(Grep_n, lo, hi)) for lo, hi in [(10, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e5), (1e5, 1e6), (1e6, 1e8)]}
out['exponent_targets'] = dict(G_envelope=-(1 + 1 / bb), G_beta=-(1 + 1 / beta_fixed))
# mismatch by band and by angular mode (cosine transform over phi in [0, pi])
C = np.cos(np.outer(phi, np.arange(K)))            # Np x K
modes = mG @ C * (2.0 / Np)                         # Nc x K (mode 0 doubled; fine for comparison)
bands = {}
for lo, hi in [(1, 10), (10, 100), (100, 1e3), (1e3, 1e4), (1e4, 1e6), (1e6, 1e99)]:
    m = (r >= lo) & (r < hi)
    if m.any():
        mm = np.abs(modes[m]).max(0)
        bands[f'{lo:g}-{hi:g}'] = dict(max_wG=float(np.abs(mG[m]).max()), max_wF=float(np.abs(mF[m]).max()),
                                       top_modes=[(int(k), round(float(mm[k]), 4)) for k in np.argsort(-mm)[:4]])
out['bands'] = bands
# angular profile of the weighted G mismatch at three far radii
prof = {}
for R0 in [300, 3e3, 3e4, 3e5]:
    i = int(np.argmin(np.abs(r - R0)))
    prof[f'{r[i]:.3g}'] = dict(mismatch=[round(float(v), 4) for v in mG[i]], Gchar_over_D=[round(float(v), 3) for v in (Gc_n[i] / float(DG[i]))], phi_deg=[round(float(np.degrees(p)), 1) for p in phi],
                               a_profile=[round(float(v), 3) for v in (np.sin(phi) * Gc_n[i] * r[i] ** (1 + 1 / beta_fixed))])   # slow-tail angular profile a(theta) ~ sin(phi) G r^{1+1/beta}
out['far_profiles'] = prof
# axis slope proxy Q(r) = G_char(near upper axis) r^{1+1/beta} and the half-width of the cone (angle from the upper axis where a drops to half its plateau)
Qr = {}
for i in range(0, Nc, max(1, Nc // 14)):
    if r[i] < 10: continue
    aprof = np.sin(phi) * Gc_n[i] * r[i] ** (1 + 1 / beta_fixed)
    plateau = float(np.median(aprof[(phi > np.radians(60)) & (phi < np.radians(120))]))
    # from the upper axis (phi = pi) inward: first angle where a exceeds half the plateau
    idx = np.nonzero(aprof[::-1] > 0.5 * plateau)[0]
    half = float(np.degrees(np.pi - phi[::-1][idx[0]])) if len(idx) else None
    Qr[f'{r[i]:.3g}'] = dict(G_up_axis_scaled=float(Gc_n[i, -1] * r[i] ** (1 + 1 / beta_fixed)), G_down_axis_scaled=float(Gc_n[i, 0] * r[i] ** (1 + 1 / beta_fixed)), a_plateau=plateau, cone_half_width_deg=half)
out['axis_slope_and_cone'] = Qr
print(json.dumps(out, indent=1))
