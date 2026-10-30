"""run_pair.py = run_from_d2.py with ipm_opt3.Problem3 (weak-pairing rows; argv[15] WPAIR, argv[16] pair_k list).
Warm start from C1-A2-d2 (exact six-branch reference of analysis2): load its generators and exact coefficients, add stationary branches
6..JMAX (blocks m <= 10j+9, NRAD Legendre functions each, exact leading moments C_j), keep d2's constraint structure (center, Theta_0,
leading moments of branches 1..5 for every m present, q=1 descendants of branches 0,1,2 zero), optimize the E_2 proxy (hw = 20/21) or the
X3 proxy (hw = 0).  argv: JMAX NRAD ANG steps tag hw [MID] [init_npy]"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2, ipm_opt3 as O3, time, os
JMAX = int(sys.argv[1]); NRAD = int(sys.argv[2]); ANG = int(sys.argv[3]); steps = int(sys.argv[4]); tag = sys.argv[5]; hw = float(sys.argv[6])
MID = int(sys.argv[7]) if len(sys.argv) > 7 else 16; init = sys.argv[8] if len(sys.argv) > 8 and sys.argv[8] != 'none' else None
HOM = int(sys.argv[9]) if len(sys.argv) > 9 else 0           # homotopy stages on the NEW branches' leading-moment targets (lower sectors stay exact)
WOFF = [int(x) for x in sys.argv[10].split(',')] if len(sys.argv) > 10 else [0]   # extra switch-on offsets w' = w + off for the new blocks (multi-scale)
R0S = [int(x) for x in sys.argv[11].split(',')] if len(sys.argv) > 11 and sys.argv[11] != 'none' else []   # legqs inner scales
NIN = int(sys.argv[12]) if len(sys.argv) > 12 else 12                                           # legqs functions per (block, scale)
QIN = 4
WLOG = float(sys.argv[13]) if len(sys.argv) > 13 else 0.0     # weight of int F^2 ds dtheta (near-field control)
WKAP = float(sys.argv[14]) if len(sys.argv) > 14 else 0.0     # kappa^2 penalty weight
WPAIR = float(sys.argv[15]) if len(sys.argv) > 15 else 0.0   # weight of the weak-pairing rows sqrt(WPAIR) I_k, k = 0..8 (ipm_opt3)
def _parse_probe(x):
    return (int(x.split(':')[0]), int(x.split(':')[1])) if ':' in x else int(x)      # 'n:K' angular probe or plain k (first mode)
PAIRK = tuple(_parse_probe(x) for x in sys.argv[16].split(",")) if len(sys.argv) > 16 else tuple(range(9))
DKFILE = sys.argv[17] if len(sys.argv) > 17 and sys.argv[17] != 'none' else None   # weaktests2 json: per-k weights w_k = WPAIR (D_0/D_k)^2 (rows measure m_k = I_k/D_k)
if DKFILE:
    _W = json.load(open(DKFILE))['NORM-T-WEAK-v1_a0']; _D = {int(k): v['D_k'] for k, v in _W.items()}
    PAIRW = [WPAIR*(_D[0]/_D[k])**2 if not hasattr(k, '__len__') else WPAIR for k in PAIRK]
else:
    PAIRW = [WPAIR]*len(PAIRK)
PAIRMODE = sys.argv[18] if len(sys.argv) > 18 else 'penalty'   # 'penalty' or 'constraint' (linearized pairing rows in the null-space step)
RCUT, RMAX = 0.02, 1e4
out = LANE+'/optimization/candD2'; os.makedirs(out, exist_ok=True)
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms131 = load131()
d2 = json.load(open('external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json'))
cd2 = X.Q(d2['cl']) if isinstance(d2['cl'], str) else X.Q(float(d2['cl'])); assert cd2 == c, 'd2 c_l differs from state 131'
gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in d2['generators']]; a_d2 = np.array([X.qfloat(X.Q(g['coef'])) for g in d2['generators']])
n_d2 = len(gens); present = {(g['j'], g['m']) for g in gens}
print('d2 generators', n_d2, 'max m', max(g['m'] for g in gens), 'branches', sorted({g['j'] for g in gens}), flush=True)
for j in range(6, JMAX+1):
    for m in range(0, 10*j+10):
        w = max(5-m, 0)
        for off in WOFF:
            for n in range(NRAD): gens.append({'m': m, 'j': j, 'spec': ['leg', w+off, n]})
# multi-scale inner functions with vanishing far-field moments q < QIN (no constraints needed), branches 0..3, m <= 9, scales R0S
for R0 in R0S:
    for j in range(4):
        for m in range(10):
            w = max(5-m, 0)
            for n in range(NIN): gens.append({'m': m, 'j': j, 'spec': ['legqs', w, n, QIN, R0]})
print('pair rows', len(PAIRK), 'weights', ' '.join(f'{w:.2e}' for w in PAIRW), flush=True)
print('generators total', len(gens), 'of which legqs inner', len(R0S)*40*NIN, flush=True)
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= RCUT) & (np.exp(s) <= RMAX); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev); print('mesh', mesh.Nr, 'x', mesh.Nt, flush=True)
t0 = time.time(); prob = O3.Problem3(gens, c, mesh, wpair=PAIRW, pair_k=PAIRK, pair_mode=PAIRMODE, r_cut=RCUT, r_max=RMAX, hw=hw, wlog=WLOG, wkap=WKAP); print('problem build', time.time()-t0, flush=True)
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
DESC_ZERO = tuple(int(x) for x in os.environ.get('IPM_DESC_ZERO', '0,1,2').split(','))   # branches whose q = 1 descendants are zeroed exactly (default as 005/007)
print('desc_zero branches', DESC_ZERO, flush=True)
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=DESC_ZERO, branch_targets=targets)
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), flush=True)
a0 = np.zeros(len(gens)); a0[:n_d2] = a_d2
if init:
    a_init = np.load(init); assert len(a_init) <= len(gens), 'init longer than the generator list'
    a0 = np.zeros(len(gens)); a0[:len(a_init)] = a_init      # shorter init (e.g. without legqs functions) is zero-padded: new functions start at 0
print('d2 start: constraint viol', np.abs(A@a0-b).max(), 'taylor', np.abs(prob.taylor_values(a0)).max(), flush=True)
parts, comp, Fd = prob.objective_parts(a0)
def report(tagp, comp):
    r = mesh.r[:, None]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
    P2 = math.sqrt(float(torch.sum(base*om2*(comp[(2,0)]**2+2*comp[(1,1)]**2+comp[(0,2)]**2)))); G1 = math.sqrt(float(torch.sum(base*(comp[(1,0)]**2+comp[(0,1)]**2)))); G0 = math.sqrt(float(torch.sum(base*comp[(0,0)]**2))); rF = math.sqrt(float(torch.sum(base*r**2*comp[(0,0)]**2)))
    Fl = math.sqrt(float(torch.sum(4*mesh.W*comp[(0,0)]**2)))
    print(f'{tagp} (FLOAT, 0.02<=r<=1e4, midpoint {ANG}, middle {MID}): P2 {P2:.6e} G1 {G1:.6e} G0 {G0:.6e} rF {rF:.6e} ||F||_(ds dth) {Fl:.4e} supF {float(comp[(0,0)].abs().max()):.4e} X3raw {math.sqrt(P2**2+2**14*G1**2+2**18*G0**2):.6e}', flush=True)
report('d2 as loaded', comp)
if HOM > 0 and init is None:
    full_rows = list(prob.lin_rows); a = a0
    newnames = tuple(f'lead_j{j}_' for j in range(6, JMAX+1))
    for k in range(1, HOM+1):
        lam = X.Q(k)/X.Q(HOM)
        prob.lin_rows = [(row, (rhs*X.qfloat(lam) if name.startswith(newnames) else rhs), rex, (rhse*lam if name.startswith(newnames) else rhse), name) for (row, rhs, rex, rhse, name) in full_rows]
        a = prob.taylor_project(a, iters=8)
        parts, comp, Fd = prob.objective_parts(a); report(f'homotopy stage {k}/{HOM} start', comp)
        a = prob.optimize2(a, steps=max(6, steps//HOM), lam0=1e-6, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
    prob.lin_rows = full_rows; a_start = prob.taylor_project(a, iters=8)
else:
    a_start = prob.taylor_project(a0, iters=8)
parts, comp, Fd = prob.objective_parts(a_start); report('feasible start', comp); print('viol', np.abs(A@a_start-b).max(), flush=True)
a = prob.optimize2(a_start, steps=steps, lam0=1e-6, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a)
parts, comp, Fd = prob.objective_parts(a); report('FINAL', comp)
print('FINAL pairings I_k (mesh, FLOAT):', ' '.join(f'{v:+.4e}' for v in (prob.last_Ik or [])), flush=True)
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'parent': 'C1-A2-d2 (nb_d2_exact.json)', 'JMAX': JMAX, 'NRAD': NRAD, 'angular_midpoint': ANG, 'hw': hw, 'middle_order': MID, 'steps': steps, 'pivots': [int(p) for p in piv], 'homotopy_stages': HOM, 'w_offsets': WOFF, 'legqs_scales': R0S, 'legqs_per_block': NIN, 'Q_inner': QIN, 'wlog': WLOG, 'wkap': WKAP, 'wpair': WPAIR, 'pair_k': [list(q) if hasattr(q, '__len__') else q for q in PAIRK], 'pair_weights': PAIRW, 'pair_Dk_file': DKFILE, 'pair_mode': PAIRMODE, 'desc_zero': list(DESC_ZERO), 'I_k_final_mesh': prob.last_Ik})
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=3); json.dump(rep, open(out+f'/{tag}_sectors.json', 'w')); print('sector time', time.time()-t0, flush=True)
print('exact json sha256', sha, flush=True)
for rw in rep['rows'][:16]: print(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
