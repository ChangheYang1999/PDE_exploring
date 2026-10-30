"""run_quot.py: optimization from an exact candidate JSON (any generator list, e.g. the exact quotient basis of quotient_basis.py), with the constraints
of run_from_d2 (center, Theta_0, zero q = 1 descendants of branches 0,1,2 (env IPM_DESC_ZERO), exact leading moments of branches 1..JMAX from the recursion)
and the balanced E_2 objective plus optional weak-pairing rows (ipm_opt3.Problem3).  argv: exact_json ANG steps tag hw MID wlog wkap WPAIR probes(k or n:K list | none) pair_mode"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt3 as O3, time, os
path = sys.argv[1]; ANG = int(sys.argv[2]); steps = int(sys.argv[3]); tag = sys.argv[4]; hw = float(sys.argv[5]); MID = int(sys.argv[6])
WLOG = float(sys.argv[7]); WKAP = float(sys.argv[8]); WPAIR = float(sys.argv[9])
def _parse(x): return (int(x.split(':')[0]), int(x.split(':')[1])) if ':' in x else int(x)
PAIRK = tuple(_parse(x) for x in sys.argv[10].split(',')) if len(sys.argv) > 10 and sys.argv[10] != 'none' else ()
PAIRMODE = sys.argv[11] if len(sys.argv) > 11 else 'penalty'
RCUT, RMAX = 0.02, 1e4
out = LANE+'/optimization/candD2'; dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J131, c131, terms131 = load131()
c, gens, coefs_q, J = OPT.load_candidate_json(path); assert c == c131
a0 = np.array([X.qfloat(v) for v in coefs_q]); JMAX = max(int(g['j']) for g in gens if 'j' in g)
ADD = os.environ.get('IPM_ADD_LEGQS')      # 'j1,j2,...:mmin:mmax:R0:NIN' -> append multi-scale legqs functions (Q = 4 vanishing far moments) with zero start coefficients to EXISTING (j, m) blocks only
if ADD:
  for spec in ADD.split(';'):                  # several specs separated by ';' (e.g. two scales)
    js, mmin, mmax, R0, NIN = spec.split(':'); js = [int(x) for x in js.split(',')]; mmin, mmax, R0, NIN = int(mmin), int(mmax), int(R0), int(NIN)
    present = {(int(g['j']), int(g['m'])) for g in gens if 'j' in g}; added = 0
    existing = {(int(g['j']), int(g['m']), tuple(g['spec'])) for g in gens if 'j' in g}
    for j in js:
        for m in range(mmin, mmax+1):
            if (j, m) not in present: continue
            w = max(5-m, 0)
            for n in range(NIN):
                sp = ['legqs', w, n, 4, R0]
                if (j, m, tuple(sp)) in existing: continue      # do not duplicate functions already in the loaded list
                gens.append({'m': m, 'j': j, 'spec': sp}); added += 1
    a0 = np.r_[a0, np.zeros(added)]; print('added legqs functions', added, 'for blocks j in', js, 'm in', (mmin, mmax), 'R0', R0, flush=True)
print('generators', len(gens), 'branches', sorted({int(g['j']) for g in gens if 'j' in g}), 'from', os.path.basename(path), flush=True)
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= RCUT) & (np.exp(s) <= RMAX); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev); print('mesh', mesh.Nr, 'x', mesh.Nt, flush=True)
NHELD = int(os.environ.get('IPM_NHELDIN', '0')); WHELD = float(os.environ.get('IPM_WPAIR_HELDIN', WPAIR))   # the last NHELD rows of the list get the weight WHELD (held-in mid-field rows; 021 showed that 1e12 leaves rows with I ~ 5e-6 inert)
WLIST = ([WPAIR]*(len(PAIRK)-NHELD) + [WHELD]*NHELD) if PAIRK else 0.0
if NHELD: print('per-row weights: first', len(PAIRK)-NHELD, 'rows', WPAIR, '; last', NHELD, 'rows', WHELD, flush=True)
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=WLIST, pair_k=PAIRK, pair_mode=PAIRMODE, r_cut=RCUT, r_max=RMAX, hw=hw, wlog=WLOG, wkap=WKAP); print('problem build', time.time()-t0, 'pair rows', len(PAIRK), 'weight', WPAIR, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
DESC_ZERO = tuple(int(x) for x in os.environ.get('IPM_DESC_ZERO', '0,1,2').split(','))
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=DESC_ZERO, branch_targets=targets)
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), 'viol at start', np.abs(A@a0-b).max(), 'taylor', np.abs(prob.taylor_values(a0)).max(), flush=True)
def report(tagp, comp):
    r = mesh.r[:, None]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
    P2 = math.sqrt(float(torch.sum(base*om2*(comp[(2,0)]**2+2*comp[(1,1)]**2+comp[(0,2)]**2)))); G1 = math.sqrt(float(torch.sum(base*(comp[(1,0)]**2+comp[(0,1)]**2)))); G0 = math.sqrt(float(torch.sum(base*comp[(0,0)]**2))); rF = math.sqrt(float(torch.sum(base*r**2*comp[(0,0)]**2)))
    print(f'{tagp} (FLOAT, 0.02<=r<=1e4, midpoint {ANG}, middle {MID}): P2 {P2:.6e} G1 {G1:.6e} G0 {G0:.6e} rF {rF:.6e} supF {float(comp[(0,0)].abs().max()):.4e}', flush=True)
a_start = prob.taylor_project(a0, iters=8); parts, comp, Fd = prob.objective_parts(a_start); report('start', comp)
if PAIRK: print('start pairings:', ' '.join(f'{v:+.3e}' for v in prob.last_Ik), flush=True)
a = prob.optimize2(a_start, steps=steps, lam0=1e-6, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a); parts, comp, Fd = prob.objective_parts(a); report('FINAL', comp)
if PAIRK: print('FINAL pairings:', ' '.join(f'{v:+.3e}' for v in prob.last_Ik), flush=True)
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'parent_json': os.path.basename(path), 'angular_midpoint': ANG, 'hw': hw, 'middle_order': MID, 'steps': steps, 'pivots': [int(p) for p in piv], 'wlog': WLOG, 'wkap': WKAP, 'wpair': WPAIR, 'wpair_heldin': (WHELD if NHELD else None), 'n_heldin_rows': NHELD, 'pair_k': [list(q) if hasattr(q, '__len__') else q for q in PAIRK], 'pair_mode': PAIRMODE, 'desc_zero': list(DESC_ZERO), 'added_legqs': os.environ.get('IPM_ADD_LEGQS'), 'I_k_final_mesh': prob.last_Ik, 'quotient_meta': J.get('meta', {}).get('quotient_of')})
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=3); json.dump(rep, open(out+f'/{tag}_sectors.json', 'w')); print('sector time', time.time()-t0, flush=True)
print('exact json sha256', sha, flush=True)
for rw in rep['rows'][:14]: print(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}", flush=True)
