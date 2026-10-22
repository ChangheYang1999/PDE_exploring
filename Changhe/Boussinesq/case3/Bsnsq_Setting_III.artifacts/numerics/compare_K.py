"""compare_K.py -- controlled resolution comparison of lambda-path states at ONE lambda (astra path1 (1)): beta, fit floor (sum and RMS per
residual entry), Q_R (axis_ode json if present), C2 (constvel), and the relative differences of G and d_phi G between consecutive resolutions
on a common far-field grid (100 log radii in [1e4, 1e8] x 721 angles), normalized by the finer state's envelope and supremum.
Usage: python3 code/compare_K.py runs/blam24v_lambda0.95.npz runs/blam32v_lambda0.95.npz runs/blam40v95_lambda0.95.npz"""
import sys, os, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from constvel import const_velocity
torch.set_default_dtype(DT); dev = 'cuda'
paths = sys.argv[1:]
rr = np.logspace(4, 8, 100); ph = np.linspace(0, np.pi, 721)[1:-1]
R, P = np.meshgrid(rr, ph, indexing='ij'); X = torch.tensor((R * np.sin(P)).ravel(), dtype=DT, device=dev); Y = torch.tensor((-R * np.cos(P)).ravel(), dtype=DT, device=dev)
rows = []; Gs = []
for p in paths:
    d = np.load(p)
    b = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=float(d['grade']))
    g = Geometry(b, float(d['beta_basis']), float(d['L']), rmap=str(d['rmap']))
    cF = torch.tensor(d['cF'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
    F, G = fields_at(b, g.beta, g.L, g.rmap, cF, cG, X, Y)
    G = G.cpu().numpy().reshape(len(rr), len(ph)); Gs.append(G)
    env = (1 - g.t_of_r(torch.tensor(rr, dtype=DT, device=dev))) ** g.pG; env = env.cpu().numpy()[:, None]
    Nq = int(d['Nphi_res']) * b.Nc if 'Nphi_res' in d.files else None
    cv = const_velocity(b, g, cG)
    tag = os.path.basename(p).replace('.npz', '')
    ax = f"runs/axis_{tag}.json"; Q = json.load(open(ax))['axis']['up']['Q_closed_form_est'] if os.path.exists(ax) else float('nan')
    rows.append(dict(state=tag, K=int(d['K']), Nt=int(d['Nt']), beta=float(d['beta']), floor=float(d['obj']), rms=float(np.sqrt(d['obj'] / (2 * Nq))) if Nq else float('nan'),
                     accepted=int(d['continuation_accepted']) if 'continuation_accepted' in d.files else -1, Q_R_up=Q, C2=cv['C2'], p2=cv['p_coeffs'][2], env=env, strain_m=float(d['strain_mismatch'])))
out = dict(lambda_=float(np.load(paths[0])['lam']), states=[{k: v for k, v in r.items() if k != 'env'} for r in rows], pairwise=[])
for i in range(1, len(rows)):
    env = rows[i]['env']; Gf = Gs[i] / env; Gc = Gs[i - 1] / env
    dG = np.abs(Gf - Gc).max() / np.abs(Gf).max()
    dphi_f = np.gradient(Gf, ph, axis=1); dphi_c = np.gradient(Gc, ph, axis=1)
    ddG = np.abs(dphi_f - dphi_c).max() / np.abs(dphi_f).max()
    # where is the G difference largest (angle from the upper axis, radius)
    k = np.unravel_index(np.argmax(np.abs(Gf - Gc)), Gf.shape)
    out['pairwise'].append(dict(coarse=rows[i - 1]['state'], fine=rows[i]['state'], rel_diff_G_sup=float(dG), rel_diff_dphiG_sup=float(ddG),
                                argmax_r=float(rr[k[0]]), argmax_angle_from_upper_axis_deg=float(np.degrees(np.pi - ph[k[1]])),
                                dbeta=rows[i]['beta'] - rows[i - 1]['beta']))
print(json.dumps(out, indent=1))
