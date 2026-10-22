"""quad_order_check.py (shift 7): far-field velocity sensitivity of the modal Green inverse to its Gaussian quadrature order.
For a stored state, evaluate the modal stream function Psi_k, Psi_k' at target radii with the Basis quadrature order ng_quad = 12
(the solver's default) and ng_quad = NG (e.g. 48), and report the relative change of the velocity (V_r, V_phi) on a set of angles.
Usage: python3 code/quad_order_check.py runs/state.npz [--ng 48] [--radii 1e3,1e4,1e5,1e6] [--out runs/quad_<tag>.json]"""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from fixedsrc import cross_inverse
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--ng', type=int, default=48)
ap.add_argument('--radii', type=str, default='1e2,1e3,1e4,1e5,1e6'); ap.add_argument('--nphi', type=int, default=181); ap.add_argument('--out', type=str, default='')
a = ap.parse_args(); dev = 'cuda'; d = np.load(a.state)
radii = [float(v) for v in a.radii.split(',')]
r = torch.tensor(np.array(radii) * 1.0137, dtype=DT, device=dev)
cG = torch.tensor(d['cG'], dtype=DT, device=dev)
out = dict(state=a.state, radii=[float(v) for v in r.cpu().numpy()], ng_ref=12, ng_hi=a.ng, rows=[])
res = {}
for ng in (12, a.ng):
    b = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']), ng_quad=ng, m_reg=int(d['mreg']), device=dev, grade=float(d['grade']))
    g = Geometry(b, float(d['beta_basis']), float(d['L']), rmap=str(d['rmap']))
    Psi, dPsi = cross_inverse(g, cG, r, ng_part=ng)      # (K, n)
    res[ng] = (Psi.cpu().numpy(), dPsi.cpu().numpy())
K = res[12][0].shape[0]; k = np.arange(1, K + 1)[:, None]
phi = np.linspace(0, np.pi, a.nphi)[None, :]
for i, rv in enumerate(r.cpu().numpy()):
    row = dict(r=float(rv))
    V = {}
    for ng in (12, a.ng):
        Psi, dPsi = res[ng]
        Vr = (k * Psi[:, i:i + 1] * np.cos(k * phi)).sum(0) / rv       # (1/r) d/dphi sum Psi_k sin(k phi)
        Vp = -(dPsi[:, i:i + 1] * np.sin(k * phi)).sum(0)             # -d/dr
        V[ng] = (Vr, Vp)
    dV = np.sqrt((V[12][0] - V[a.ng][0]) ** 2 + (V[12][1] - V[a.ng][1]) ** 2); Vm = np.sqrt(V[a.ng][0] ** 2 + V[a.ng][1] ** 2)
    row.update(max_abs_dV=float(dV.max()), max_V=float(Vm.max()), rel_max_dV_over_maxV=float(dV.max() / Vm.max()), beta_r=float(float(d['beta']) * rv),
               rel_dV_over_beta_r=float(dV.max() / (float(d['beta']) * rv)),
               worst_mode_rel_dPsi=float(np.max(np.abs(res[12][1][:, i] - res[a.ng][1][:, i]) / (np.abs(res[a.ng][1][:, i]) + 1e-300))),
               mode_of_worst=int(np.argmax(np.abs(res[12][1][:, i] - res[a.ng][1][:, i]) / (np.abs(res[a.ng][1][:, i]) + 1e-300))) + 1,
               rel_dPsi_k1=float(abs(res[12][1][0, i] - res[a.ng][1][0, i]) / (abs(res[a.ng][1][0, i]) + 1e-300)))
    out['rows'].append(row)
    print(f"r={rv:.3e}: max|dV| (ng 12 vs {a.ng}) = {row['max_abs_dV']:.3e}, max|V| = {row['max_V']:.3e}, ratio {row['rel_max_dV_over_maxV']:.2e}, |dV|/(beta r) {row['rel_dV_over_beta_r']:.2e}; worst mode rel dPsi {row['worst_mode_rel_dPsi']:.2e} (k {row['mode_of_worst']}), k=1 rel dPsi {row['rel_dPsi_k1']:.2e}")
if a.out: json.dump(out, open(a.out, 'w'), indent=1)
