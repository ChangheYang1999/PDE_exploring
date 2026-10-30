"""Singular values of the EXPLICIT weighted design matrix J Z (no normal equations; resolution ~1e-16 relative) on the admissible tangent space Z (null space of
the exact rows + linearized Taylor rows) for a candidate, plus the Gram-metric (physical L^2) generalized singular values: with G = Z^T Phi^T W Phi Z the L^2 Gram
of the densities (positive definite on an exact quotient basis), sigma_i of J Z G^(-1/2) are min/max of ||J h||/||h||_(L^2) over the tangent (theory_v03 R9(c),
T4-229 metric).  Memory: J Z is (rows) x dim(Z), rows = 6 Nr Nt (+ kappa rows); at MID 16 x 180 and 1496 columns about 2.7 GB float64.  argv: exact_json ANG MID out_json"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt3 as O3, time, hashlib
DT = torch.float64
path = sys.argv[1]; ANG = int(sys.argv[2]); MID = int(sys.argv[3]); outp = sys.argv[4]
dev = torch.device('cpu'); c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q])
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
J131, c131, terms131 = load131()
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=0.0, r_cut=0.02, r_max=1e4, hw=20/21, wlog=2.**18*100, wkap=3e6); print('build', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json')); JMAX = max(int(g['j']) for g in gens)
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=targets)
A, b = prob.constraint_matrix(); tv = prob.taylor_values(a)[1:]; Jt = prob.taylor_jacobian(a)[1:]
At = torch.as_tensor(np.vstack([A, Jt]), dtype=DT); U, S, Vh = torch.linalg.svd(At, full_matrices=True); rank = int((S > S.max()*1e-13).sum()); Z = Vh[rank:].T
n = prob.n; dimZ = Z.shape[1]; print('n', n, 'constraint rank', rank, 'dim Z', dimZ, flush=True)
# explicit weighted Jacobian J (rows x n) built chunkwise exactly as in normal_equations, then multiplied by Z chunkwise
Fd = prob.fields(a); comp = prob.F_components(Fd); Nr, Nt = mesh.Nr, mesh.Nt
DERIVS, LEIB, NL = O3.DERIVS, O3.LEIB, O3.NL
W2 = {d: prob.wts[d] for d in DERIVS}; K2 = list(prob.kap_rows)
rchunk = 53; blocks = []; resid = []
t0 = time.time()
for r0 in range(0, Nr, rchunk):
    rs = slice(r0, min(Nr, r0+rchunk)); nr = rs.stop-rs.start
    rows = [torch.sqrt(W2[d][rs])*comp[d][rs] for d in DERIVS]+[torch.sqrt(w[rs])*Fd[key][rs] for key, w in K2]
    resid.append(torch.cat([x.reshape(-1) for x in rows], 0))
    Jc = torch.zeros(sum(x.numel() for x in rows), n, dtype=DT)
    for b0 in range(0, n, 48):
        idx = list(range(b0, min(n, b0+48))); nb = len(idx); cache = {}
        def fm(key):
            if key not in cache:
                out = torch.zeros(nr, Nt, nb, dtype=DT)
                for j, i in enumerate(idx):
                    for typ, N, arr in prob.gslots[i][key]: out[:, :, j] += arr[rs, None]*prob.tabs.tab[typ][N][None, :]
                cache[key] = out
            return cache[key]
        Jparts = []
        for d in DERIVS:
            M = fm(('T', d)).clone()
            for sgn, dp, dr in NL:
                for cf, d1, d2 in LEIB[d]:
                    kp = ('psi', (dp[0]+d1[0], dp[1]+d1[1])); kr = ('rho', (dr[0]+d2[0], dr[1]+d2[1]))
                    M += sgn*cf*(Fd[kp][rs][:, :, None]*fm(kr)+Fd[kr][rs][:, :, None]*fm(kp))
            Jparts.append((M*torch.sqrt(W2[d][rs])[:, :, None]).reshape(-1, nb))
        for key, w in K2: Jparts.append((fm(key)*torch.sqrt(w[rs])[:, :, None]).reshape(-1, nb))
        Jc[:, b0:b0+nb] = torch.cat(Jparts, 0); del cache
    blocks.append(Jc@Z); del Jc
JZ = torch.cat(blocks, 0); del blocks; rvec = torch.cat(resid, 0); print('J Z assembled', JZ.shape, 'in', time.time()-t0, 's', flush=True)
colnorm = torch.linalg.norm(JZ, dim=0); colnorm[colnorm == 0] = 1
t0 = time.time(); sv = torch.linalg.svdvals(JZ/colnorm[None, :]).numpy(); print('SVD (column-scaled) in', time.time()-t0, 's', flush=True)
sv_raw = torch.linalg.svdvals(JZ).numpy()
# Gram metric: L^2 norm of the density h = rho(delta): Phi columns = density fields of the generators on the mesh with the dX weight
r = mesh.r[:, None]; base = 4*mesh.W*r**2; sqb = torch.sqrt(base).reshape(-1)
Phi = torch.zeros(Nr*Nt, n, dtype=DT)
for i in range(n):
    acc = torch.zeros(Nr, Nt, dtype=DT)
    for typ, N, arr in prob.gslots[i][('rho', (0, 0))]: acc += arr[:, None]*prob.tabs.tab[typ][N][None, :]
    Phi[:, i] = acc.reshape(-1)*sqb
PZ = Phi@Z; del Phi
Gz = PZ.T@PZ; evG = torch.linalg.eigvalsh(Gz).numpy(); print('Gram on Z: eigenvalues min %.3e max %.3e (positive definite iff exact quotient basis)' % (evG.min(), evG.max()), flush=True)
try:
    Lg = torch.linalg.cholesky(Gz); Y = torch.linalg.solve_triangular(Lg, JZ.T, upper=False).T     # J Z L^-T
    gsv = torch.linalg.svdvals(Y).numpy(); gram_ok = True
except Exception as e:
    print('Gram Cholesky failed:', e); gsv = np.array([]); gram_ok = False
def q(x): return {k: float(np.quantile(x, float(k))) for k in ('0', '0.001', '0.01', '0.05', '0.1', '0.25', '0.5', '0.75', '0.9', '1')}
print('scaled sv: min %.3e max %.3e; counts < 1e-4: %d, < 1e-6: %d, < 1e-8: %d, < 1e-10: %d, < 1e-12: %d (of %d)' % (sv.min(), sv.max(), (sv < 1e-4*sv.max()).sum(), (sv < 1e-6*sv.max()).sum(), (sv < 1e-8*sv.max()).sum(), (sv < 1e-10*sv.max()).sum(), (sv < 1e-12*sv.max()).sum(), len(sv)), flush=True)
if gram_ok: print('Gram-metric generalized sv (||J h|| / ||h||_L2): min %.4e max %.4e; counts < 1e-4 max: %d, < 1e-6: %d, < 1e-8: %d' % (gsv.min(), gsv.max(), (gsv < 1e-4*gsv.max()).sum(), (gsv < 1e-6*gsv.max()).sum(), (gsv < 1e-8*gsv.max()).sum()), flush=True)
json.dump({'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= 1e4; balanced objective weights of 007', 'n': n, 'constraint_rank': rank, 'dimZ': dimZ, 'rows': int(JZ.shape[0]),
           'scaled_sv_quantiles': q(sv), 'scaled_sv_max': float(sv.max()), 'scaled_counts_below': {str(t): int((sv < t*sv.max()).sum()) for t in (1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14)},
           'raw_sv_quantiles': q(sv_raw), 'gram_eig_min': float(evG.min()), 'gram_eig_max': float(evG.max()),
           'gram_metric_sv_quantiles': q(gsv) if gram_ok else None, 'gram_metric_counts_below': ({str(t): int((gsv < t*gsv.max()).sum()) for t in (1e-4, 1e-6, 1e-8)} if gram_ok else None),
           'gram_metric_sv_min_abs': float(gsv.min()) if gram_ok else None, 'residual_norm': float(torch.linalg.norm(rvec)),
           'label': 'FLOAT; SVD of the explicit weighted design matrix on the admissible tangent (resolution about 1e-16 relative); Gram metric = mesh L^2 norm of the density; not an inverse bound for L (theory_v03 R9(d))'}, open(outp, 'w'), indent=1)
print('written', outp)
