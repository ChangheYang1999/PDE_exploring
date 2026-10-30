"""Rebuild a candB problem (same argv as run_candB without objective/steps) and finalize saved coefficients: argv: coefs.npy JMAX NRAD DESC tag"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import time, os
npy = sys.argv[1]; JMAX = int(sys.argv[2]); NRAD = int(sys.argv[3]); DESC = tuple(int(x) for x in sys.argv[4].split(',')); tag = sys.argv[5]
out = LANE+'/optimization/candB'
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0_860, a0_exact = OPT.case4_coefficients_t1(J, c)
for j in range(1, JMAX+1):
    mlo = 10 if j <= 3 else 0
    for m in range(mlo, 10*j+10):
        w = max(5-m, 0)
        for n in range(NRAD): gens.append({'m': m, 'j': j, 'spec': ['leg', w, n]})
_s, _ws, _bl = EV.whole_axis_radial(); _th, _wth = EV.angular_midpoint(16)
mesh = EV.Mesh(_s, _ws, _th, _wth, dev)          # tiny mesh: only the constraint machinery is needed here
prob = OPT.Problem(gens, c, mesh, objective='Jabs', r_cut=0.02)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_exact_0_8.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=DESC, branch_targets=targets)
a = np.load(npy); assert len(a) == len(gens)
A, b = prob.constraint_matrix(); print('constraint viol', np.abs(A@a-b).max(), 'taylor', np.abs(prob.taylor_values(a)).max(), flush=True)
t0 = time.time(); a_exact, piv = OPT.finalize_exact(prob, a); print('finalize time', time.time()-t0, flush=True)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'JMAX': JMAX, 'NRAD': NRAD, 'DESC': list(DESC), 'pivots': [int(p) for p in piv], 'source_npy': npy})
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=2); print('sector time', time.time()-t0, flush=True)
json.dump(rep, open(out+f'/{tag}_sectors.json','w'))
print('exact json sha256', sha, flush=True)
for r in rep['rows'][:16]: print(f"  exp {r['exponent']:+.4f} {r['status']:14s} maxharm {r['max_harmonic']:3d} quarter {r['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
