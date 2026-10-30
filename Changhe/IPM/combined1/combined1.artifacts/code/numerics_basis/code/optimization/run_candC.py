"""Candidate C: fixed exact stationary tail (branches 1..JMAX, descendants q<=Q-1 zero) + free inner functions.
argv: JMAX Q NINNER ANG steps tag hw [MID] [init npy]"""
import sys; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2, ipm_tail as TL
import time, os
JMAX = int(sys.argv[1]); Q = int(sys.argv[2]); NINNER = int(sys.argv[3]); ANG = int(sys.argv[4]); steps = int(sys.argv[5]); tag = sys.argv[6]
hw = float(sys.argv[7]); MID = int(sys.argv[8]) if len(sys.argv) > 8 else 16; init = sys.argv[9] if len(sys.argv) > 9 and sys.argv[9] != 'none' else None
HOMOTOPY = int(sys.argv[10]) if len(sys.argv) > 10 else 0   # number of homotopy stages (tail and branch targets scaled lam = k/H)
RCUT, RMAX = 0.02, 1e4
out = LANE+'/optimization/candC'; os.makedirs(out, exist_ok=True)
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
J, c, terms = load131()
gens = OPT.t1_generators_860(); a0_860, a0_exact = OPT.case4_coefficients_t1(J, c)
# inner functions with vanishing moments q <= Q-1: (1-t)^Q P_n for j<=3, m<=9
for j in range(4):
    for m in range(10):
        w = max(5-m, 0)
        for n in range(NINNER): gens.append({'m': m, 'j': j, 'spec': ['legq', w, n, Q]})
SO = json.load(open(LANE+'/far_field/state131_stationary_orders_exact_0_8.json'))
if JMAX > 8: SO = json.load(open(LANE+'/far_field/state131_stationary_orders_0_12.json'))
targets = {j: {int(k): X.Q(v) for k, v in SO['orders'][str(j)]['C'].items()} for j in range(1, JMAX+1)}
t0 = time.time(); fixed = TL.fixed_tail(c, targets, JMAX, Q, skip_blocks={(j, m) for j in range(1, 4) for m in range(10)}); print('fixed tail blocks', len(fixed)//Q, 'functions', len(fixed), 'time', time.time()-t0, flush=True)
print('free generators', len(gens), flush=True)
s, ws, bl = EV.whole_axis_radial(middle_order=MID); keep = (np.exp(s) >= RCUT) & (np.exp(s) <= RMAX); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev); print('mesh', mesh.Nr, 'x', mesh.Nt, flush=True)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=RCUT, r_max=RMAX, hw=hw, fixed=fixed); print('problem build', time.time()-t0, flush=True)
# constraints: center; branch 0: Theta_0 leading + descendants q=1..Q-1 zero; branches 1..3 (m<=9): leading = C_j, descendants zero
prob.add_center()
sect, moments = X.potential_sectors(terms, 1); p0 = X.p_branch(c, 0); C00 = sect[(p0, 0)]
for m in range(10):
    prob.add_moment(m, p0, 0, C00.get(2*m, mpq(0)), f'theta0_m{m}')
    for q in range(1, Q): prob.add_moment(m, p0, q, mpq(0), f'desc_j0_m{m}_q{q}')
for j in range(1, 4):
    pj = X.p_branch(c, j)
    for m in range(10):
        prob.add_moment(m, pj, 0, targets[j].get(2*m, mpq(0)), f'lead_j{j}_m{m}')
        for q in range(1, Q): prob.add_moment(m, pj, q, mpq(0), f'desc_j{j}_m{m}_q{q}')
A, b = prob.constraint_matrix(); print('constraint rows', len(prob.lin_rows), flush=True)
a0 = np.zeros(len(gens)); a0[:860] = a0_860
if init: a0 = np.load(init); assert len(a0) == len(gens)
parts, _, _ = prob.objective_parts(a0); print('start parts', {str(k): v for k, v in parts.items()}, 'viol', np.abs(A@a0-b).max(), flush=True)
if HOMOTOPY > 0 and init is None:
    # stage k: fixed tail scaled by lam, branch-1..3 targets scaled by lam (Theta_0, center, zero descendants unchanged); exact rows restored at lam = 1
    full_tail = {k: {kk: vv.clone() for kk, vv in d.items()} for k, d in prob.tail.items()}
    full_rows = list(prob.lin_rows)
    a = a0
    for k in range(1, HOMOTOPY+1):
        lam = k/HOMOTOPY
        prob.tail = {kk: {k2: lam*v2 for k2, v2 in d.items()} for kk, d in full_tail.items()}
        prob.fixed_coefs = np.array([X.qfloat(v) for _, v in prob.fixed])*lam
        prob.lin_rows = [(row, (rhs*lam if name.startswith('lead_j') else rhs), rex, (rhse*X.Q(k)/X.Q(HOMOTOPY) if name.startswith('lead_j') else rhse), name) for (row, rhs, rex, rhse, name) in full_rows]
        a = prob.taylor_project(a, iters=8)
        print(f'homotopy stage {k}/{HOMOTOPY} lam={lam}: start obj {prob.objective_value2(a):.4e}', flush=True)
        a = prob.optimize2(a, steps=max(8, steps//HOMOTOPY), lam0=1e-4, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy', verbose=True)
    prob.tail = full_tail; prob.fixed_coefs = np.array([X.qfloat(v) for _, v in prob.fixed]); prob.lin_rows = full_rows
    a_start = prob.taylor_project(a, iters=8)
else:
    a_start = prob.taylor_project(a0, iters=8)
parts, _, _ = prob.objective_parts(a_start); print('feasible start parts', {str(k): v for k, v in parts.items()}, 'viol', np.abs(A@a_start-b).max(), flush=True)
a = prob.optimize2(a_start, steps=steps, lam0=1e-4, taylor=True, log=out+f'/{tag}.log', ckpt=out+f'/{tag}_coefs.npy')
np.save(out+f'/{tag}_coefs.npy', a)
parts, comp, Fd = prob.objective_parts(a)
r = mesh.r[:, None]; base = 4*mesh.W*r**2; om2 = (1+4*r**2)**0.8
P2 = math.sqrt(float(torch.sum(base*om2*(comp[(2,0)]**2+2*comp[(1,1)]**2+comp[(0,2)]**2)))); G1 = math.sqrt(float(torch.sum(base*(comp[(1,0)]**2+comp[(0,1)]**2)))); G0 = math.sqrt(float(torch.sum(base*comp[(0,0)]**2))); rF = math.sqrt(float(torch.sum(base*r**2*comp[(0,0)]**2)))
print(f'FINAL (FLOAT, 0.02<=r<=1e4, midpoint {ANG}, middle order {MID}): P2 {P2:.6e} G1 {G1:.6e} G0 {G0:.6e} rF {rF:.6e} supF {float(comp[(0,0)].abs().max()):.4e}', flush=True)
a_exact, piv = OPT.finalize_exact(prob, a)
sha = OPT.write_candidate_json(out+f'/{tag}_exact.json', prob, a_exact, {'tag': tag, 'JMAX': JMAX, 'Q': Q, 'NINNER': NINNER, 'angular_midpoint': ANG, 'hw': hw, 'middle_order': MID, 'steps': steps, 'pivots': [int(p) for p in piv], 'design': 'fixed exact stationary tail (branches 1..JMAX, all blocks m<=10j+9 except (j<=3,m<=9)) with descendants q<=Q-1 zero; free: 860 T1 + legq inner functions'})
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=Q+1); json.dump(rep, open(out+f'/{tag}_sectors.json', 'w')); print('sector time', time.time()-t0, flush=True)
print('exact json sha256', sha, flush=True)
for rw in rep['rows'][:16]: print(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}", flush=True)
print('a0 =', X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact]))), flush=True)
