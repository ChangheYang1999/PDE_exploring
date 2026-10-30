"""Candidate A family: constrained refits in the 860 basis. Constraints: center, Theta_0 fixed, D_0=D_1=0 (q=1 moments of branches 0,1),
branch h=1,2,3 leading moments = truncated stationary targets (harmonics <= 19). Objective: argv[1] in {Jabs, E2low, FrF}; steps argv[2]."""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import time, os
obj = sys.argv[1]; steps = int(sys.argv[2]); RMAX = float(sys.argv[3]) if len(sys.argv) > 3 else None; tag = f'candA_{obj}' + (f'_R{RMAX:g}' if RMAX else '')
out = LANE+'/optimization/candA'; os.makedirs(out, exist_ok=True)
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0, a0_exact = OPT.case4_coefficients_t1(J, c)
mesh = EV.training_mesh(dev)
prob = OPT.Problem(gens, c, mesh, objective=obj, r_cut=0.02, r_max=RMAX)
tg = truncated_targets(c, terms, 3, mcut=9)
json.dump({str(h): {'G_target': X.dump_q_dict(tg[h][0]), 'C_target': X.dump_q_dict(tg[h][1]), 'alpha': X.qstr(tg[h][2]), 'unresolved_quarter_norm': X.quarter_norm({k:v for k,v in tg[h][3].items() if k>19})} for h in tg}, open(out+'/truncated_targets.json','w'))
add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=(0,1), branch_targets={h: tg[h][1] for h in (1,2,3)})
print('constraint rows', len(prob.lin_rows), flush=True)
A, b = prob.constraint_matrix(); print('constraint violation at 131: max', np.abs(A@a0-b).max(), flush=True)
print('objective at 131:', prob.objective_value(a0), flush=True)
# first: project state 131 onto the constraints (min norm) to get a feasible start
a_start = prob.taylor_project(a0, iters=6)
print('objective at feasible start:', prob.objective_value(a_start), 'constraint viol', np.abs(A@a_start-b).max(), 'taylor', np.abs(prob.taylor_values(a_start)).max(), flush=True)
a, hist = prob.optimize(a_start, steps=steps, lam0=1e-4, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a)
print('final objective', prob.objective_value(a), 'taylor', prob.taylor_values(a), 'constraint viol', np.abs(A@a-b).max(), flush=True)
# report the other objectives too
for o in ('Jabs', 'F2', 'FrF', 'E2low'):
    prob.set_objective(o, 0.02, RMAX); print(f'  {o}: start131 {prob.objective_value(a0):.6e}  final {prob.objective_value(a):.6e}', flush=True)
# exact finalization + sector table
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'objective': obj, 'steps': steps, 'pivots': [int(p) for p in piv]})
rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=2)
json.dump(rep, open(out+f'/{tag}_sectors.json','w'))
print('exact json sha256', sha)
for r in rep['rows'][:12]: print(f"  exp {r['exponent']:+.4f} {r['status']:14s} maxharm {r['max_harmonic']:3d} quarter {r['quarter_L2']:.6e}")
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))))
