"""E_2-proxy optimization on the trimmed mesh [r_cut, r_max]. argv: init_exact_json_or_npy JMAX NRAD DESC ANG steps tag [wF wG wP]"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2
import time, os
init = sys.argv[1]; JMAX = int(sys.argv[2]); NRAD = int(sys.argv[3]); DESC = tuple(int(x) for x in sys.argv[4].split(',') if x not in ('', 'none')); ANG = int(sys.argv[5]); steps = int(sys.argv[6]); tag = sys.argv[7]
wF, wG, wP = (float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10])) if len(sys.argv) > 10 else (2.**18, 2.**14, 1.0)
hw = float(sys.argv[11]) if len(sys.argv) > 11 else 20/21
MID = int(sys.argv[12]) if len(sys.argv) > 12 else 32   # middle Gauss order per unit log-radius panel
RCUT, RMAX = 0.02, 1e4
out = LANE+'/optimization/candE2'; os.makedirs(out, exist_ok=True)
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0_860, a0_exact = OPT.case4_coefficients_t1(J, c)
for j in range(1, JMAX+1):
    mlo = 10 if j <= 3 else 0
    for m in range(mlo, 10*j+10):
        w = max(5-m, 0)
        for n in range(NRAD): gens.append({'m': m, 'j': j, 'spec': ['leg', w, n]})
print('generators', len(gens), flush=True)
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= RCUT) & (np.exp(s) <= RMAX); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG)
mesh = EV.Mesh(s, ws, th, wth, dev); print('trimmed mesh', mesh.Nr, 'x', mesh.Nt, flush=True)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=RCUT, r_max=RMAX, wF=wF, hw=hw, wG=wG, wP=wP); print('problem build', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_exact_0_8.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
add_standard_constraints(prob, c, terms, theta0_fix=True, desc_zero=DESC, branch_targets=targets)
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), flush=True)
if init == 'STATE131': a0 = np.zeros(len(gens)); a0[:860] = a0_860
elif init.endswith('.npy'): a0 = np.load(init)
else:
    cc, g2, coefs, _ = OPT.load_candidate_json(init); a0 = np.array([X.qfloat(v) for v in coefs])
assert len(a0) == len(gens)
parts, _, _ = prob.objective_parts(a0); print('start parts', parts, 'viol', np.abs(A@a0-b).max(), flush=True)
a_start = prob.taylor_project(a0, iters=6)
a = prob.optimize2(a_start, steps=steps, lam0=1e-4, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a)
parts, comp, Fd = prob.objective_parts(a)
r = mesh.r[:, None]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
P2 = math.sqrt(float(torch.sum(base*om2*(comp[(2,0)]**2+2*comp[(1,1)]**2+comp[(0,2)]**2)))); G1 = math.sqrt(float(torch.sum(base*(comp[(1,0)]**2+comp[(0,1)]**2)))); G0 = math.sqrt(float(torch.sum(base*comp[(0,0)]**2))); rF = math.sqrt(float(torch.sum(base*r**2*comp[(0,0)]**2)))
print(f'FINAL (FLOAT, 0.02<=r<=1e4, midpoint {ANG}): P2 {P2:.6e} G1 {G1:.6e} G0 {G0:.6e} rF {rF:.6e} supF {float(comp[(0,0)].abs().max()):.4e}', flush=True)
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'JMAX': JMAX, 'NRAD': NRAD, 'DESC': list(DESC), 'angular_midpoint': ANG, 'weights': [wF, wG, wP], 'hw': hw, 'middle_order': MID, 'steps': steps, 'init': init, 'pivots': [int(p) for p in piv]})
rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=2); json.dump(rep, open(out+f'/{tag}_sectors.json', 'w'))
print('exact json sha256', sha, flush=True)
for rw in rep['rows'][:14]: print(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
