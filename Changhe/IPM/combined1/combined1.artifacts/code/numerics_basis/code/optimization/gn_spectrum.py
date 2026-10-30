"""Conditioning / near-kernel diagnostic of the constrained Gauss-Newton problem at a candidate (prompt section 9 and 12): eigenvalues of the
column-scaled reduced normal matrix Z^T J^T J Z (J = weighted Jacobian of the residual components in the balanced E_2 objective, Z = null space
of the exact linear rows + linearized Taylor rows).  Reports the singular-value spectrum of the scaled J Z (sqrt of eigenvalues), the condition
number, the count below thresholds, and for the 5 smallest directions the dominating generators (block j, m, spec).  argv: exact_json ANG MID out_json"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt3 as O3, time, hashlib
path = sys.argv[1]; ANG = int(sys.argv[2]); MID = int(sys.argv[3]); outp = sys.argv[4]
dev = torch.device('cpu')
c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q])
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
J131, c131, terms131 = load131()
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=0.0, r_cut=0.02, r_max=1e4, hw=20/21, wlog=2.**18*100, wkap=3e6); print('build', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json'))
JMAX = max(int(g['j']) for g in gens)
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=targets)
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), 'viol at candidate', np.abs(A@a-b).max(), flush=True)
t0 = time.time(); G, g, phi = prob.normal_equations(a); print('normal equations', time.time()-t0, 'phi', phi, flush=True)
tv = prob.taylor_values(a)[1:]; Jt = prob.taylor_jacobian(a)[1:]
Afull = np.vstack([A, Jt]); At = torch.as_tensor(Afull, dtype=torch.float64)
U, S, Vh = torch.linalg.svd(At, full_matrices=True); rank = int((S > S.max()*1e-13).sum()); Z = Vh[rank:].T
GZ = Z.T@(G@Z)
colnorm = torch.sqrt(torch.diagonal(GZ).clamp(min=0)); colnorm[colnorm == 0] = 1
GZs = GZ/colnorm[:, None]/colnorm[None, :]
ev, V = torch.linalg.eigh(GZs); ev = ev.clamp(min=0); sv = torch.sqrt(ev).numpy()      # singular values of the scaled reduced Jacobian
ev_raw, V_raw = torch.linalg.eigh(GZ); sv_raw = torch.sqrt(ev_raw.clamp(min=0)).numpy()
print('reduced dimension', GZ.shape[0], 'constraint rank', rank, flush=True)
print('scaled sv: max %.4e min %.4e cond %.4e; counts < 1e-4: %d, < 1e-6: %d, < 1e-8: %d' % (sv.max(), sv.min(), sv.max()/max(sv.min(), 1e-300), (sv < 1e-4*sv.max()).sum(), (sv < 1e-6*sv.max()).sum(), (sv < 1e-8*sv.max()).sum()), flush=True)
print('raw (unscaled) sv: max %.4e min %.4e cond %.4e' % (sv_raw.max(), sv_raw.min(), sv_raw.max()/max(sv_raw.min(), 1e-300)), flush=True)
# gradient norm in the reduced coordinates (stationarity of the candidate for this objective)
gZ = Z.T@g; print('reduced gradient norm', float(torch.linalg.norm(gZ)), 'relative to sqrt(phi)*max sv', float(torch.linalg.norm(gZ))/(math.sqrt(phi)*sv_raw.max()), flush=True)
# smallest directions in generator space (unscaled): which generators dominate
dirs = []
for i in range(5):
    v = (Z@(V_raw[:, i])).numpy(); idx = np.argsort(-np.abs(v))[:6]
    dirs.append({'sv_raw': float(sv_raw[i]), 'top_generators': [{'index': int(k), 'weight': float(v[k]), 'm': gens[k]['m'], 'j': gens[k].get('j'), 'spec': gens[k]['spec']} for k in idx]})
    print(f'direction {i}: sv {sv_raw[i]:.3e}; top gens', [(gens[k]['j'], gens[k]['m'], gens[k]['spec'][0], gens[k]['spec'][1:], round(float(v[k]), 3)) for k in idx], flush=True)
# spectrum quantiles
q = np.quantile(sv, [0, 0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0])
json.dump({'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= 1e4', 'objective': 'balanced E_2 proxy of 007 (wF 2^18, hw 20/21, wG 2^14, wP 1, wlog 2^18*100, wkap 3e6)',
           'reduced_dim': int(GZ.shape[0]), 'constraint_rank': rank, 'scaled_sv_quantiles': dict(zip(['0', '0.01', '0.05', '0.1', '0.25', '0.5', '0.75', '0.9', '0.99', '1'], map(float, q))), 'scaled_cond': float(sv.max()/max(sv.min(), 1e-300)),
           'raw_sv_min': float(sv_raw.min()), 'raw_sv_max': float(sv_raw.max()), 'raw_cond': float(sv_raw.max()/max(sv_raw.min(), 1e-300)), 'reduced_gradient_norm': float(torch.linalg.norm(gZ)), 'phi': phi,
           'smallest_directions': dirs, 'scaled_sv_sorted_first200': [float(x) for x in sv[:200]], 'label': 'FLOAT diagnostic of the finite-dimensional least-squares problem; not a bound on the operator L'}, open(outp, 'w'), indent=1)
print('written', outp)
