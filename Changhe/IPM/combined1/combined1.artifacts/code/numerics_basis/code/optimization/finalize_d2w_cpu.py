"""CPU exact finalization + sector table of an interrupted run_from_d2 run from its checkpoint .npy.
argv: coefs.npy JMAX NRAD WOFF(comma) R0S(comma|none) NIN tag"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from candA_setup import *
import ipm_opt2 as O2, time
npy = sys.argv[1]; JMAX = int(sys.argv[2]); NRAD = int(sys.argv[3]); WOFF = [int(x) for x in sys.argv[4].split(',')]; R0S = [int(x) for x in sys.argv[5].split(',')] if sys.argv[5] != 'none' else []; NIN = int(sys.argv[6]); tag = sys.argv[7]; QIN = 4
out = LANE+'/optimization/candD2'; dev = torch.device('cpu')
J, c, terms131 = load131()
d2 = json.load(open('external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json'))
gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in d2['generators']]
for j in range(6, JMAX+1):
    for m in range(0, 10*j+10):
        w = max(5-m, 0)
        for off in WOFF:
            for n in range(NRAD): gens.append({'m': m, 'j': j, 'spec': ['leg', w+off, n]})
for R0 in R0S:
    for j in range(4):
        for m in range(10):
            w = max(5-m, 0)
            for n in range(NIN): gens.append({'m': m, 'j': j, 'spec': ['legqs', w, n, QIN, R0]})
a = np.load(npy); assert len(a) == len(gens), (len(a), len(gens))
s, ws, bl = EV.whole_axis_radial(origin_order=8, middle_order=4, infinity_order=8); th, wth = EV.angular_midpoint(16); mesh = EV.Mesh(s, ws, th, wth, dev)   # tiny mesh: constraints only
t0 = time.time(); prob = OPT.Problem(gens, c, mesh, objective='Jabs', r_cut=0.02); print('problem build (tiny mesh, cpu)', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=(0, 1, 2), branch_targets=targets)
A, b = prob.constraint_matrix(); print('rows', len(prob.lin_rows), 'viol', np.abs(A@a-b).max(), 'taylor', np.abs(prob.taylor_values(a)).max(), flush=True)
t0 = time.time(); a_exact, piv = OPT.finalize_exact(prob, a); print('finalize', time.time()-t0, flush=True)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'parent': 'C1-A2-d2', 'JMAX': JMAX, 'NRAD': NRAD, 'w_offsets': WOFF, 'legqs_scales': R0S, 'legqs_per_block': NIN, 'source_npy': npy, 'note': 'finalized on CPU from the last checkpoint of a run interrupted by the GPU revocation (2026-10-29T00:58Z)', 'pivots': [int(p) for p in piv]})
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=3); json.dump(rep, open(out+f'/{tag}_sectors.json', 'w')); print('sectors', time.time()-t0, flush=True)
print('exact json sha256', sha, flush=True)
for rw in rep['rows'][:14]: print(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
