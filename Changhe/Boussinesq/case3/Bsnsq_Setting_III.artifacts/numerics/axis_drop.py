"""axis_drop.py -- lead's 03:25Z diagnostic for a lambda/eps state: the far-field angular profile a(theta) ~ sin(phi) G_char r^{1+1/beta}
of the TRANSPORTED vorticity on a fine angular grid (default 360 angles on [0, pi]) at the grid radii nearest r = 1e2, 1e4, 2.3e5:
a_pl = max of a over the upper half (phi in [90, 180) deg), the angles (from the upper axis, phi = pi) at which a falls to 90 and 10
percent of a_pl on the axis side (linear interpolation), the drop width w = phi_10 - phi_90 (degrees), the axis slope estimate
-da/dphi at the axis from the last two nodes (compare with Q_up of axis_ode.py), and the same on the lower axis. The saved temperature
is transported (no refit). Usage: python3 code/axis_drop.py state.npz [--Nphi_res 360] [--radii 1e2,1e4,2.3e5]"""
import sys, os, argparse, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from charnewton import CharResidual
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--Nphi_res', type=int, default=360)
ap.add_argument('--radii', type=str, default='1e2,1e4,2.3e5')
a = ap.parse_args(); dev = 'cuda'
d = np.load(a.state)
Nt, K, Nphi, grade, L, bb = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']), float(d['beta_basis'])
beta_fixed = float(d['beta_fixed']) if float(d['beta_fixed']) > 0 else bb
b = Basis(Nt, int(d['deg']), K, Nphi, ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=grade)
# cheap residual object (Nphi_res 4) whose evaluation points are then replaced by the fine angular grid (custom_points mode of run(), as in axis_ode.py)
res = CharResidual(b, L, bb, Nphi_res=4, r_in=float(d['r_in']), dt=float(d['dt']), device=dev, max_steps=20000, rmap=str(d['rmap']), beta_fixed=beta_fixed, wc=0.0, include_RF=True)
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
radii = [float(v) for v in a.radii.split(',')]
Np = a.Nphi_res
phi = (np.arange(Np) + 0.5) * np.pi / Np                  # midpoint angles in (0, pi): phi = 0 lower axis, phi = pi upper axis
r_all = np.repeat(np.array(radii), Np); phi_all = np.tile(phi, len(radii))
X0 = torch.tensor(np.stack([r_all * np.sin(phi_all), -r_all * np.cos(phi_all)], 1), dtype=DT, device=dev)
res.X0 = X0; res.Nq = X0.shape[0]; res.custom_points = True; res.cF_fixed = cF / a0
_, info = res.run(cG[None], return_all=True)
Gc = (a0 * info['G_char'][0]).reshape(len(radii), Np).cpu().numpy()
Frep, Grep_t = fields_at(b, bb, L, str(d['rmap']), cF, cG, X0[:, 0], X0[:, 1])
Grep = Grep_t.reshape(len(radii), Np).cpu().numpy()
r = np.array(radii)
out = dict(state=a.state, lam=lam, beta=beta_fixed, a0=a0, K=K, Nphi_res=Np, unfinished=res.n_unfinished, dphi_deg=float(np.degrees(phi[1] - phi[0])), angles='midpoints (j + 1/2) pi / Nphi_res; phi = pi is the upper axis', radii={})
def drop(aprof, phi, side):
    """side 'up': axis at phi = pi, profile approaching from smaller phi; 'down': axis at phi = 0."""
    if side == 'up':
        sel = phi >= np.pi / 2; p = phi[sel]; v = aprof[sel]; dist = np.pi - p           # distance from the upper axis
    else:
        sel = phi <= np.pi / 2; p = phi[sel]; v = aprof[sel]; dist = p
    order = np.argsort(dist); dist = dist[order]; v = v[order]        # dist increasing from the axis outward
    i_pl = int(np.argmax(v)); a_pl = float(v[i_pl])
    def cross(level):
        # first crossing of 'level' walking from the plateau toward the axis (dist decreasing)
        for j in range(i_pl, 0, -1):
            if (v[j] - level) * (v[j - 1] - level) <= 0 and v[j] != v[j - 1]:
                return float(np.degrees(dist[j - 1] + (level - v[j - 1]) * (dist[j] - dist[j - 1]) / (v[j] - v[j - 1])))
        return None
    d90, d10 = cross(0.9 * a_pl), cross(0.1 * a_pl)
    slope = float(v[0] / dist[0]) if dist[0] > 0 else None     # a / (angle from axis) at the first node: -> Q as the node approaches the axis
    slope2 = float((v[1] - v[0]) / (dist[1] - dist[0])) if len(v) > 1 else None
    return dict(a_plateau=a_pl, plateau_angle_from_axis_deg=float(np.degrees(dist[i_pl])), angle90_deg=d90, angle10_deg=d10,
                width_90_10_deg=(abs(d90 - d10) if (d90 is not None and d10 is not None) else None), a_over_angle_first_node=slope, da_dangle_first_two_nodes=slope2,
                first_node_angle_deg=float(np.degrees(dist[0])), a_first_node=float(v[0]))
for i, R0 in enumerate(radii):
    aprof = np.sin(phi) * Gc[i] * r[i] ** (1 + 1 / beta_fixed)
    arep = np.sin(phi) * Grep[i] * r[i] ** (1 + 1 / beta_fixed)
    # outer trace: a at fixed angles delta from the UPPER axis (astra jump1: distinguish a collapsing layer with a nonzero outer trace from a
    # concentrating overshoot); linear interpolation in delta on the midpoint grid
    delta = np.degrees(np.pi - phi)[::-1]; a_up = aprof[::-1]
    fixed = [1, 2, 3, 5, 7.5, 10, 15, 20, 30, 45, 60, 90]
    out['radii'][f'{r[i]:.4g}'] = dict(transported=dict(up=drop(aprof, phi, 'up'), down=drop(aprof, phi, 'down'), a_median_60_120=float(np.median(aprof[(phi > np.radians(60)) & (phi < np.radians(120))]))),
                                      represented=dict(up=drop(arep, phi, 'up'), down=drop(arep, phi, 'down')),
                                      max_abs_mismatch_a=float(np.abs(aprof - arep).max()),
                                      a_at_delta_deg_from_upper_axis={str(dd): float(np.interp(dd, delta, a_up)) for dd in fixed},
                                      profile_delta_deg=[round(float(v), 3) for v in delta], profile_a_transported=[round(float(v), 5) for v in a_up])
print(json.dumps(out, indent=1))
