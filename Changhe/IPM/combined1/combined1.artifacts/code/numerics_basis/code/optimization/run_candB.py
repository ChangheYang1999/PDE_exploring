"""Candidate B family: enlarged basis with stationary branches j=0..JMAX (default 6), angular range m <= 10j+9 for j>=1, exact stationary leading
moments C_j (from far_field/state131_stationary_orders_exact_0_8.json), zero q=1 descendants for branches in DESC, Theta_0 and center fixed.
argv: objective steps JMAX nrad DESC(comma) angular_order [init_npy]"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import time, os
obj = sys.argv[1]; steps = int(sys.argv[2]); JMAX = int(sys.argv[3]); NRAD = int(sys.argv[4]); DESC = tuple(int(x) for x in sys.argv[5].split(',')); ANG = int(sys.argv[6])
RMAX = float(sys.argv[7]) if len(sys.argv) > 7 else None
init = sys.argv[8] if len(sys.argv) > 8 else None
tag = f'candB_j{JMAX}_n{NRAD}_d{"".join(map(str,DESC))}_{obj}' + (f'_R{RMAX:g}' if RMAX else '') + ('_mid%d' % ANG if os.environ.get('ANGRULE','midpoint') == 'midpoint' else '_gauss%d' % ANG)
out = LANE+'/optimization/candB'; os.makedirs(out, exist_ok=True)
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0_860, a0_exact = OPT.case4_coefficients_t1(J, c)
# new blocks
for j in range(1, JMAX+1):
    mlo = 10 if j <= 3 else 0
    for m in range(mlo, 10*j+10):
        w = max(5-m, 0)
        for n in range(NRAD): gens.append({'m': m, 'j': j, 'spec': ['leg', w, n]})
print('generators', len(gens), flush=True)
_s, _ws, _bl = EV.whole_axis_radial(); _th, _wth = (EV.angular_midpoint(ANG) if os.environ.get('ANGRULE','midpoint') == 'midpoint' else EV.angular_gauss(ANG)); mesh = EV.Mesh(_s, _ws, _th, _wth, dev)
t0 = time.time(); prob = OPT.Problem(gens, c, mesh, objective=obj, r_cut=0.02, r_max=RMAX); print('problem build', time.time()-t0, flush=True)
# stationary targets (exact)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_exact_0_8.json'))
targets = {}
for j in range(1, JMAX+1):
    Cj = {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()}
    targets[j] = Cj
add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=DESC, branch_targets=targets)
print('constraint rows', len(prob.lin_rows), flush=True)
A, b = prob.constraint_matrix()
a0 = np.zeros(len(gens)); a0[:860] = a0_860
if init: a0 = np.load(init); assert len(a0) == len(gens)
print('objective at start:', prob.objective_value(a0), 'constraint viol', np.abs(A@a0-b).max(), flush=True)
a_start = prob.taylor_project(a0, iters=6)
print('objective at feasible start:', prob.objective_value(a_start), 'viol', np.abs(A@a_start-b).max(), 'taylor', np.abs(prob.taylor_values(a_start)).max(), flush=True)
a, hist = prob.optimize(a_start, steps=steps, lam0=1e-4, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a)
print('final objective', prob.objective_value(a), 'taylor', np.abs(prob.taylor_values(a)).max(), 'constraint viol', np.abs(A@a-b).max(), flush=True)
for o in ('Jabs', 'F2', 'FrF', 'E2low'):
    prob.set_objective(o, 0.02, RMAX); print(f'  {o}: final {prob.objective_value(a):.6e}', flush=True)
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'objective': obj, 'steps': steps, 'JMAX': JMAX, 'NRAD': NRAD, 'DESC': list(DESC), 'angular_order': ANG, 'pivots': [int(p) for p in piv]})
rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=2)
json.dump(rep, open(out+f'/{tag}_sectors.json','w'))
print('exact json sha256', sha, flush=True)
for r in rep['rows'][:16]: print(f"  exp {r['exponent']:+.4f} {r['status']:14s} maxharm {r['max_harmonic']:3d} quarter {r['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
