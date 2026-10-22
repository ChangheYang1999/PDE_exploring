"""field_continuity.py -- fold2 protocol item: continuity of the STORED fields F = Theta/x^2 and G = Omega/x between consecutive saved
states of a beta-parameterized continuation, evaluated on a COMMON PHYSICAL GRID (not coefficient differences, since the basis is retied to
beta at every stage): polar grid r = logspace(rmin, rmax, nr), phi = atan2(x, -y) in (0, pi) (x > 0), nphi angles. For each consecutive
pair (and for the first/last pair) prints max over r of  max_phi |F1 - F2| / max_phi |F1|  and the same for G, plus dbeta, dlambda.
Usage: python3 code/field_continuity.py state1.npz state2.npz [...] [--rmin 1e-2 --rmax 1e6 --nr 41 --nphi 180]"""
import sys, os, argparse, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, DT, fields_at
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('states', nargs='+'); ap.add_argument('--rmin', type=float, default=1e-2)
ap.add_argument('--rmax', type=float, default=1e6); ap.add_argument('--nr', type=int, default=41); ap.add_argument('--nphi', type=int, default=180)
ap.add_argument('--json', type=str, default='')
a = ap.parse_args(); dev = 'cuda'
r = np.logspace(np.log10(a.rmin), np.log10(a.rmax), a.nr); phi = np.linspace(0.5, 179.5, a.nphi) * np.pi / 180
R, P = np.meshgrid(r, phi, indexing='ij')
x = torch.tensor(R * np.sin(P), dtype=DT, device=dev); y = torch.tensor(-R * np.cos(P), dtype=DT, device=dev)
def ev(path):
    d = np.load(path)
    b = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=float(d['grade']))
    cF = torch.tensor(d['cF'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    F, G = fields_at(b, float(d['beta_basis']), float(d['L']), str(d['rmap']), cF, cG, x, y)
    return dict(path=path, beta=float(d['beta']), lam=float(d['lam']), obj=float(d['obj']), K=int(d['K']), F=F.cpu().numpy(), G=G.cpu().numpy())
S = [ev(p) for p in a.states]
def cmp(s1, s2):
    out = {}
    for nm in ('F', 'G'):
        A, B = s1[nm], s2[nm]
        num = np.abs(A - B).max(axis=1); den = np.abs(A).max(axis=1)
        rel = num / den
        out[nm] = dict(max_rel=float(rel.max()), r_at_max=float(r[int(rel.argmax())]), median_rel=float(np.median(rel)), rel_r1=float(rel[np.argmin(np.abs(r - 1))]), rel_r1e4=float(rel[np.argmin(np.abs(r - 1e4))]))
    return out
rows = []
pairs = [(i, i + 1) for i in range(len(S) - 1)]
if len(S) > 2: pairs.append((0, len(S) - 1))
print(f"# common grid: r in [{a.rmin:g}, {a.rmax:g}] ({a.nr} log-spaced), {a.nphi} angles; rel = max_phi|dF| / max_phi|F1| per radius")
print("# pair                                   dbeta     dlambda     F: max_rel (r)      median   at r=1    at r=1e4 | G: max_rel (r)      median   at r=1    at r=1e4")
for i, j in pairs:
    s1, s2 = S[i], S[j]; c = cmp(s1, s2)
    n1 = os.path.basename(s1['path'])[:-4]; n2 = os.path.basename(s2['path'])[:-4]
    print(f"{n1} -> {n2}: {s2['beta'] - s1['beta']:+.4f} {s2['lam'] - s1['lam']:+.3e}  F {c['F']['max_rel']:.2e} ({c['F']['r_at_max']:.0e}) {c['F']['median_rel']:.2e} {c['F']['rel_r1']:.2e} {c['F']['rel_r1e4']:.2e} | G {c['G']['max_rel']:.2e} ({c['G']['r_at_max']:.0e}) {c['G']['median_rel']:.2e} {c['G']['rel_r1']:.2e} {c['G']['rel_r1e4']:.2e}")
    rows.append(dict(s1=n1, s2=n2, beta1=s1['beta'], beta2=s2['beta'], lam1=s1['lam'], lam2=s2['lam'], **{f'{k}_{kk}': v for k in c for kk, v in c[k].items()}))
if a.json: json.dump(dict(grid=dict(rmin=a.rmin, rmax=a.rmax, nr=a.nr, nphi=a.nphi), rows=rows), open(a.json, 'w'), indent=1)
