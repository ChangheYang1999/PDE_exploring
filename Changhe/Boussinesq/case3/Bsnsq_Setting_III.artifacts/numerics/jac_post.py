"""jac_post.py -- post-processing of a saved Jacobian (runs/jac_<tag>.npz from jacobian_fp.py): (1) the CORRECT scaling direction of the divided
field (verifier P198: Omega_l = Omega(X/l) => G_l = l^-1 G(X/l), direction -G - X.grad G) and its A-image; (2) field-metric singular values of
A = J_T - I (R A R^-1 with M = Q R, M = weighted basis on the residual set, so that ||M x|| is the weighted field norm of the perturbation);
(3) eigenvalue summary. Usage: python3 code/jac_post.py --state runs/mbb_b3.0952_lambda0.989973.npz --ext_gauss 2.5,1.0 --jac runs/jac_L2v.npz --tag L2v"""
import sys, os, json, argparse, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT, fields_at
from charnewton import CharResidual
from fixedsrc import make_source_block
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('--state', required=True); ap.add_argument('--ext_gauss', required=True); ap.add_argument('--jac', required=True); ap.add_argument('--tag', required=True); ap.add_argument('--n_sv', type=int, default=8)
a = ap.parse_args(); dev = 'cuda'
d = np.load(a.state); J = np.load(a.jac)
Nt, K, Nphi, grade, L = int(d['Nt']), int(d['K']), int(d['Nphi']), float(d['grade']), float(d['L']); rmap = str(d['rmap']); r_in = float(d['r_in']); dt = float(d['dt']); ngc = int(d['ngc']); deg = int(d['deg']); mreg = int(d['mreg'])
beta = float(d['beta']); lam = float(d['lam']); a0 = float(d['a0']); Nphi_res = int(d['Nphi_res']); y0, sg = [float(v) for v in a.ext_gauss.split(',')]
b = Basis(Nt, deg, K, Nphi, ng_coll=ngc, m_reg=mreg, device=dev, grade=grade)
cF = torch.tensor(d['cF'], dtype=DT, device=dev); cG = torch.tensor(d['cG'], dtype=DT, device=dev)
res = CharResidual(b, L, beta, Nphi_res=Nphi_res, r_in=r_in, dt=dt, device=dev, max_steps=100, rmap=rmap, beta_fixed=beta, wc=0.0, include_RF=True)
act = res.active; JT = torch.tensor(J['JT'], dtype=DT, device=dev); Nact = JT.shape[0]; I = torch.eye(Nact, dtype=DT, device=dev); A = JT - I
gres = res.gres; xs, ys = gres.x, gres.y; e = 1e-4
Fp, Gp = fields_at(b, beta, L, rmap, cF, cG, xs / (1 + e), ys / (1 + e)); Fm, Gm = fields_at(b, beta, L, rmap, cF, cG, xs / (1 - e), ys / (1 - e))
dG_wrong = (Gp - Gm) / (2 * e); dG = (Gp / (1 + e) - Gm / (1 - e)) / (2 * e)
out = {}
U, S, Vh = torch.linalg.svd(A); S_np = S.cpu().numpy()
for name, dGv in [('scaling_divided_(-G - X.grad G)', dG), ('X_grad_only_(old, wrong)', dG_wrong)]:
    v = res.PG @ (res.wG * dGv); vn = v / v.norm()
    fit_err = ((gres.Phi0G[:, act] @ v - dGv) * res.wG).abs().max().item() / (res.wG * dGv).abs().max().item()
    out[name] = dict(norm=float(v.norm()), Av_over_v=float((A @ vn).norm()), JTv_over_v=float((JT @ vn).norm()), rayleigh=float(vn @ (JT @ vn)), fit_err=fit_err,
                     cos_weakest_right_sv=[float(abs((Vh[-i] @ vn).item())) for i in range(1, a.n_sv + 1)], cos_c_op=float(abs((vn @ (res.c_op_act / res.c_op_act.norm())).item())))
    print(name, {k: (v_ if not isinstance(v_, list) else ['%.3f' % c for c in v_]) for k, v_ in out[name].items()})
Mw = (gres.Phi0G * res.wG[:, None])[:, act]; Rq = torch.linalg.qr(Mw, mode='r')[1]
A_field = Rq @ A @ torch.linalg.inv(Rq); S_field = torch.linalg.svdvals(A_field).cpu().numpy()
ev = np.linalg.eigvals(J['JT']) if 'ev' not in J.files else J['ev']
out['field_metric'] = dict(cond_R=float(torch.linalg.cond(Rq)), sv_smallest=S_field[-a.n_sv:][::-1].tolist(), sv_largest=S_field[:3].tolist(), cond=float(S_field[0] / S_field[-1]))
out['coefficient_metric'] = dict(sv_smallest=S_np[-a.n_sv:][::-1].tolist(), sv_largest=S_np[:3].tolist(), cond=float(S_np[0] / S_np[-1]))
out['eigs_JT'] = dict(spectral_radius=float(np.abs(ev).max()), n_gt1=int((np.abs(ev) > 1).sum()), n_gt05=int((np.abs(ev) > 0.5).sum()), nearest_to_1=np.sort(np.abs(ev - 1))[:a.n_sv].tolist(), largest_abs=np.sort(np.abs(ev))[::-1][:6].tolist())
print('field metric:', out['field_metric']); print('coefficient metric:', out['coefficient_metric']); print('eigs:', out['eigs_JT'])
json.dump(out, open(f'runs/jacpost_{a.tag}.json', 'w'), indent=1)
