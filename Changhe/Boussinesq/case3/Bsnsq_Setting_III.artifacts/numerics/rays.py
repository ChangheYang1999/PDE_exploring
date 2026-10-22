import sys, os, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, Problem, DT
from evalstate import load_state, basis_from_meta
torch.set_default_dtype(DT)
path = sys.argv[1]
cF, cG, meta = load_state(path)
b = basis_from_meta(meta, ngc=9)
g = Geometry(b, meta['beta'], meta['L']); p = Problem(g); f = p.fields(cF, cG)
RF, RG, NF, NG = p.residuals(cF, cG, f)
Nc, Nphi = b.Nc, b.Nphi
def grid(v): return v.reshape(Nc, Nphi).cpu().numpy()
r = g.r.cpu().numpy(); phi = b.phi
jmid = Nphi // 2  # phi ~ pi/2 -> y ~ 0
for name, v in [('F', f['F']), ('G', f['G']), ('A', f['A']), ('B', f['B']), ('Hy', f['Hy']), ('U2', f['U2']), ('RF/NF', RF/NF), ('RG/NG', RG/NG)]:
    gv = grid(v)
    print(name, 'along y~0 ray (phi=%.3f):' % phi[jmid])
    idx = np.unique(np.linspace(0, Nc - 1, 14).astype(int))
    print('   r:', ' '.join(f'{r[i]:9.3g}' for i in idx))
    print('  val:', ' '.join(f'{gv[i, jmid]:9.3g}' for i in idx))
# angular structure at a few radii
for i in [5, 40, 100, 200]:
    print(f'r={r[i]:.3g}: F(phi)=', ' '.join(f'{v:8.3g}' for v in grid(f["F"])[i, ::Nphi//8]), ' G(phi)=', ' '.join(f'{v:8.3g}' for v in grid(f["G"])[i, ::Nphi//8]))
