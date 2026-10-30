"""Quick test of ipm_opt3.Problem3 on a small mesh with the 007 generator list and coefficients: (1) I_k against weak_tests2 values (coarse mesh),
(2) finite-difference check of the pairing Jacobian rows, (3) one GN step with wpair and the change of I_k."""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt2 as O2, ipm_opt3 as O3, time
path = sys.argv[1]; ANG = int(sys.argv[2]); MID = int(sys.argv[3]); WPAIR = float(sys.argv[4])
dev = torch.device('cpu')
c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q])
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
KL = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024)
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=WPAIR, pair_k=KL, r_cut=0.02, r_max=1e4, hw=20/21, wlog=2.**18*100, wkap=3e6); print('build', time.time()-t0, 'mesh', mesh.Nr, mesh.Nt, 'n', prob.n, flush=True)
parts, comp, Fd = prob.objective_parts(a)
print('parts', {str(k): f'{v:.4e}' for k, v in parts.items()})
print('I_k mesh:', ' '.join(f'k{k}:{v:+.4e}' for k, v in zip(KL, prob.last_Ik)), flush=True)
# finite-difference Jacobian check of the pairings along 3 random directions
t0 = time.time(); G, g, phi = prob.normal_equations(a); print('normal eq time', time.time()-t0, 'phi', phi, flush=True)
# recompute Jp by finite differences: d I_k / d a along direction v
rng = np.random.default_rng(1)
# The pairing Jacobian is not stored; rebuild it by one extra pass restricted to pairs: use objective_parts at a +/- eps v
for trial in range(2):
    v = rng.standard_normal(prob.n); v /= np.linalg.norm(v); eps = 1e-6
    _, cp, _ = prob.objective_parts(a+eps*v); Ip = prob.pairings(cp[(0, 0)])
    _, cm, _ = prob.objective_parts(a-eps*v); Im = prob.pairings(cm[(0, 0)])
    dI = [(p-m)/(2*eps) for p, m in zip(Ip, Im)]
    # from the normal equations: g = J^T r includes sum_k w I_k Jp_k; compare the pair part of g.v with sum_k w I_k dI_k
    prob2 = prob; prob2.pair_backup = prob.pair; prob.pair = []; G0, g0, phi0 = prob.normal_equations(a); prob.pair = prob2.pair_backup
    lhs = float((g-g0)@torch.as_tensor(v)); rhs = sum(WPAIR*I*d for I, d in zip(prob.last_Ik, dI))
    print(f'trial {trial}: (g_pair . v) {lhs:+.6e}  vs  sum w I_k dI_k/dv (FD) {rhs:+.6e}  rel diff {abs(lhs-rhs)/max(abs(rhs),1e-300):.2e}', flush=True)
# one GN step
t0 = time.time(); a1, pred, f0 = prob.gn_step2(a, 1e-6); a1 = prob.taylor_project(a1); parts1, comp1, _ = prob.objective_parts(a1)
print('GN step time', time.time()-t0, 'obj', f0, '->', sum(parts1.values()), 'pred', pred)
print('I_k after:', ' '.join(f'k{k}:{v:+.4e}' for k, v in zip(KL, prob.last_Ik)), flush=True)
A, b = prob.constraint_matrix(); print('constraint viol after step', np.abs(A@a1-b).max(), 'taylor', np.abs(prob.taylor_values(a1)).max())
