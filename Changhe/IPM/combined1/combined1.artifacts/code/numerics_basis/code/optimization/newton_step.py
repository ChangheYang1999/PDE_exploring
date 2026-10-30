"""theory_v03 R6(b)/R9(e) design diagnostic (FLOAT): the Galerkin least-squares Newton step h0 in the generator span at a candidate:
  min over delta in the constraint null space (exact rows + linearized Taylor rows) of ||F(a) + J delta||_{L^2(R^2)}  (plain L^2 weight, no derivative terms),
with J = dF/da (so J delta = L h0 for the density h0 = rho(delta), up to the quadratic term).  Reports ||h0||_2 (mesh L^2 norm of the density of delta),
the linearized residual norm ||F + J delta||_2 (computed as F(a + eps delta)/eps-difference, eps small, and also the exact quadratic form), the first-mode
and angular (N4-160 family) pairings of F + J delta, and the comparison with the T4-185 bound ||h0||_2 > 0.0047694 for every L^2 Newton step from 007.
argv: exact_json ANG MID out_json [lam]"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization'); os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt3 as O3, time, hashlib
path = sys.argv[1]; ANG = int(sys.argv[2]); MID = int(sys.argv[3]); outp = sys.argv[4]; LAM = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-10
dev = torch.device('cpu')
c, gens, coefs_q, _ = OPT.load_candidate_json(path); a = np.array([X.qfloat(v) for v in coefs_q]); cf = X.qfloat(c)
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= 0.02) & (np.exp(s) <= 1e4); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
J131, c131, terms131 = load131()
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=0.0, r_cut=0.02, r_max=1e4, wF=1.0, hw=0.0, wG=0.0, wP=0.0, wlog=0.0, wkap=0.0); print('build', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json')); JMAX = max(int(g['j']) for g in gens)
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=targets)
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), 'viol', np.abs(A@a-b).max(), flush=True)
t0 = time.time(); a1, pred, phi0 = prob.gn_step2(a, LAM, taylor=True); print('GN step', time.time()-t0, 'phi0 = ||F||_2^2 (mesh, 4 quadrants)', phi0, 'pred reduction', pred, flush=True)
delta = a1-a
r = mesh.r[:, None]; base = 4*mesh.W*r**2; theta = mesh.theta[None, :]; v = 1/(1+r**2); t = r**2*v
Fd0 = prob.fields(a); F0 = prob.F_components(Fd0)[(0, 0)]
Fdd = prob.fields(delta); h0 = Fdd[('rho', (0, 0))]                      # density of the step (fields are linear in the coefficients)
h0_L2 = math.sqrt(float(torch.sum(base*h0**2)))
eps = 1e-4; Fe = prob.F_components(prob.fields(a+eps*delta))[(0, 0)]; Fm = prob.F_components(prob.fields(a-eps*delta))[(0, 0)]
Jd = (Fe-Fm)/(2*eps)                                                      # J delta (central difference, exact for a quadratic up to rounding)
lin = F0+Jd; F1 = prob.F_components(prob.fields(a1))[(0, 0)]
G0 = math.sqrt(float(torch.sum(base*F0**2))); lin_norm = math.sqrt(float(torch.sum(base*lin**2))); new_norm = math.sqrt(float(torch.sum(base*F1**2)))
quad = math.sqrt(float(torch.sum(base*(F1-lin)**2)))
def pairs(Fx):
    out = {}
    for n in (1, 3, 5, 7, 9, 11):
        for K0 in (0, 8, 32, 128, 512):
            K = (n-1)//2+K0; phi = r*v**2*t**K*torch.sin(n*theta); out[f'{n}:{K}'] = float(torch.sum(base*Fx*phi))
    return out
P0 = pairs(F0); P1 = pairs(lin); P2 = pairs(F1)
print(f'||F||_2 {G0:.6f} -> linearized ||F + J delta||_2 {lin_norm:.6f} (new F(a+delta) {new_norm:.6f}, quadratic term {quad:.3e}); ||h0||_2 {h0_L2:.6e}  (T4-185: every L^2 Newton step from 007 has ||h0||_2 > 0.0047694)', flush=True)
print('pairings (n:K) F -> F + J delta -> F(a+delta):'); [print(f'  {q}: {P0[q]:+.3e} -> {P1[q]:+.3e} -> {P2[q]:+.3e}') for q in P0]
json.dump({'candidate': os.path.basename(path), 'sha256': hashlib.sha256(open(path, 'rb').read()).hexdigest(), 'rule': f'radial Gauss {MID}/panel x midpoint {ANG}, 0.02 <= r <= 1e4', 'lam': LAM,
           'G0_mesh': G0, 'linearized_residual_L2': lin_norm, 'F_after_step_L2': new_norm, 'quadratic_term_L2': quad, 'h0_L2': h0_L2, 'pred_reduction_phi': pred, 'phi0': phi0,
           'pairings_F': P0, 'pairings_linearized': P1, 'pairings_after_step': P2, 'delta_coef_norm': float(np.linalg.norm(delta)),
           'label': 'FLOAT; Galerkin least-squares Newton step in the generator span (constraint null space), plain L^2 weight on 0.02 <= r <= 1e4; LM damping lam on the column-scaled normal matrix'}, open(outp, 'w'), indent=1)
print('written', outp)
