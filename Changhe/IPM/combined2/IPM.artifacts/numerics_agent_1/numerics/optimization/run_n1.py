"""run_n1.py (lane numerics_agent_1, workstream N1): constrained Gauss-Newton / LM optimization in the EXISTING basis from an exact candidate JSON.
Constraints (exact linear rows): center relation (F_y(0) = 0), Theta_0 of state 131 for every m present, zero q = 1 descendants of the
branches in --desc-zero, exact leading moments of branches 1..JMAX from the stationary recursion; plus the five quadratic Taylor rows at the
origin (SQP + projection) unless --no-taylor.  Objective weights: --wF --hw --wlog --wmid --wG --wP --wkap (see ipm_optn1).
Outputs in <outdir>/<tag>/: <tag>.log (per step: objective parts and FLOAT norms), <tag>_coefs.npy (checkpoint of the last accepted
state), <tag>_exact.json (exact rational coefficients, pivots solved exactly), <tag>_sectors.json (exact far-field sector table),
<tag>_summary.json.  A file <outdir>/<tag>/STOP stops the iteration after the current step."""
import sys, os, json, time, argparse, math, hashlib
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n1_setup import *
import ipm_optn1 as ON1
ap = argparse.ArgumentParser()
ap.add_argument('--cand', required=True); ap.add_argument('--tag', required=True); ap.add_argument('--outdir', default=os.path.join(HERE, 'runs'))
ap.add_argument('--steps', type=int, default=60); ap.add_argument('--ang', type=int, default=180); ap.add_argument('--mid', type=int, default=24)
ap.add_argument('--wF', type=float, default=1.0); ap.add_argument('--hw', type=float, default=0.0); ap.add_argument('--wlog', type=float, default=0.0)
ap.add_argument('--wmid', type=float, default=0.0); ap.add_argument('--midrange', default='4,8'); ap.add_argument('--wG', type=float, default=0.0)
ap.add_argument('--wP', type=float, default=0.0); ap.add_argument('--wkap', type=float, default=0.0)
ap.add_argument('--wXs', type=float, default=0.0, help='weight of int <X>^(2 sigma) F^2 (strong-norm L2 proxy)'); ap.add_argument('--sig2', type=float, default=1.75)
ap.add_argument('--wQ2', type=float, default=0.0, help='weight of ||<D>^2 (W F)||_2^2, W = (1+r^2/r0^2)^(sigma/2) (near-field Sobolev surrogate, coordinator 19:56Z)'); ap.add_argument('--sigq', type=float, default=1.0); ap.add_argument('--r0q', type=float, default=0.25)
ap.add_argument('--lam0', type=float, default=1e-6); ap.add_argument('--lam-min', type=float, default=1e-14)
ap.add_argument('--rcut', type=float, default=0.02); ap.add_argument('--rmax', type=float, default=1e4)
ap.add_argument('--device', default=os.environ.get('IPM_DEVICE', 'cuda')); ap.add_argument('--desc-zero', default='0,1,2')
ap.add_argument('--no-taylor', action='store_true'); ap.add_argument('--init', default=None, help='npy coefficient array to start from (same generator list)')
ap.add_argument('--report-every', type=int, default=1); ap.add_argument('--ls', action='store_true', help='GN direction with exact quartic line search (optimize_ls)'); ap.add_argument('--mls', action='store_true', help='multi-damping exact line search (optimize_mls)'); ap.add_argument('--tmax', type=float, default=8.0)
args = ap.parse_args()
out = os.path.join(args.outdir, args.tag); os.makedirs(out, exist_ok=True)
dev = torch.device(args.device)
def log(msg):
    print(msg, flush=True); open(os.path.join(out, args.tag+'.log'), 'a').write(msg+'\n')
log(f'# run_n1 {args.tag} start {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} args {vars(args)}')
J131, c131, terms131 = load131()
c, gens, coefs_q, J = OPT.load_candidate_json(args.cand); assert c == c131, 'c_l differs from state 131'
cand_sha = sha256_file(args.cand)
a0 = np.array([X.qfloat(v) for v in coefs_q]); JMAX = max(int(g['j']) for g in gens if 'j' in g)
if args.init: a0 = np.load(args.init); assert len(a0) == len(gens)
log(f'generators {len(gens)} branches {sorted({int(g["j"]) for g in gens if "j" in g})} from {os.path.basename(args.cand)} sha256 {cand_sha}')
mesh = build_mesh(args.mid, args.ang, args.rcut, args.rmax, dev); log(f'mesh {mesh.Nr} x {mesh.Nt} (radial Gauss {args.mid}/panel, midpoint {args.ang}, {args.rcut} <= r <= {args.rmax:g})')
midr = tuple(float(x) for x in args.midrange.split(','))
t0 = time.time()
prob = ON1.ProblemN1(gens, c, mesh, r_cut=args.rcut, r_max=args.rmax, wF=args.wF, hw=args.hw, wG=args.wG, wP=args.wP, wlog=args.wlog, wkap=args.wkap, wmid=args.wmid, mid_range=midr, wXs=args.wXs, sig2=args.sig2)
if args.wQ2 > 0: prob.add_sobolev2_rows(args.wQ2, args.sigq, args.r0q)
log(f'problem build {time.time()-t0:.1f}s active components {prob.active} sobolev2 rows {len(getattr(prob, "rowspecs", []))}')
targets = stationary_targets(JMAX)
DESC = tuple(int(x) for x in args.desc_zero.split(',')) if args.desc_zero else ()
add_standard_constraints(prob, c, terms131, theta0_fix=True, desc_zero=DESC, branch_targets=targets)
A, b = prob.constraint_matrix()
log(f'constraint rows {len(prob.lin_rows)} viol at start {np.abs(A@a0-b).max():.3e} taylor {np.abs(prob.taylor_values(a0)).max():.3e}')
taylor = not args.no_taylor
a_start = prob.taylor_project(a0, iters=8) if taylor else a0
parts, comp, Fd = prob.objective_parts(a_start); nr = prob.norms_report(a_start)
log('start obj %.6e parts %s | %s' % (sum(parts.values()), ' '.join(f'{k}:{v:.3e}' for k, v in parts.items()), ' '.join(f'{k} {v:.5e}' for k, v in nr.items())))
opt = prob.optimize_mls if args.mls else (prob.optimize_ls if args.ls else prob.optimize2)
kw = dict(tmax=args.tmax) if (args.ls or args.mls) else {}
a, hist = opt(a_start, steps=args.steps, lam0=args.lam0, taylor=taylor, log=os.path.join(out, args.tag+'.log'), ckpt=os.path.join(out, args.tag+'_coefs.npy'), lam_min=args.lam_min, report_every=args.report_every, stop_file=os.path.join(out, 'STOP'), **kw)
np.save(os.path.join(out, args.tag+'_coefs.npy'), a)
parts, comp, Fd = prob.objective_parts(a); nr = prob.norms_report(a)
log('FINAL obj %.6e parts %s | %s' % (sum(parts.values()), ' '.join(f'{k}:{v:.3e}' for k, v in parts.items()), ' '.join(f'{k} {v:.5e}' for k, v in nr.items())))
log(f'FINAL taylor {np.abs(prob.taylor_values(a)).max():.3e} linear viol {np.abs(A@a-b).max():.3e}')
a_exact, piv = OPT.finalize_exact(prob, a)
meta = {'tag': args.tag, 'lane': 'numerics_agent_1', 'parent_json': os.path.basename(args.cand), 'parent_sha256': cand_sha, 'angular_midpoint': args.ang, 'middle_order': args.mid,
        'steps': args.steps, 'accepted_steps': len(hist), 'pivots': [int(p) for p in piv], 'weights': {k: getattr(args, k) for k in ('wF', 'hw', 'wlog', 'wmid', 'wG', 'wP', 'wkap', 'wXs', 'sig2', 'wQ2', 'sigq', 'r0q')}, 'midrange': list(midr),
        'desc_zero': list(DESC), 'taylor_rows': taylor, 'n_linear_rows': len(prob.lin_rows), 'line_search': bool(args.ls), 'multi_lambda_line_search': bool(args.mls), 'fast_fields': os.environ.get('IPM_FAST_FIELDS', '1'), 'lam0': args.lam0, 'rcut': args.rcut, 'rmax': args.rmax, 'final_float_norms_mesh': nr, 'final_objective': sum(parts.values()), 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
sha = OPT.write_candidate_json(os.path.join(out, args.tag+'_exact.json'), prob, a_exact, meta)
log(f'exact json sha256 {sha}')
t0 = time.time(); rep = OPT.sector_report(c, OPT.exact_terms(prob, a_exact), qmax=3); json.dump(rep, open(os.path.join(out, args.tag+'_sectors.json'), 'w')); log(f'sector time {time.time()-t0:.1f}s')
for rw in rep['rows'][:14]: log(f"  exp {rw['exponent']:+.4f} {rw['status']:14s} maxharm {rw['max_harmonic']:3d} quarter {rw['quarter_L2']:.6e}")
a0v = X.qfloat(prob._OJ.a0(prob._flat_coefs([X.qfloat(v) for v in a_exact])))
log(f'a0 = {a0v}')
json.dump({'meta': meta, 'exact_sha256': sha, 'history': hist, 'first_nonzero_sector': rep['first_nonzero'], 'a0_float': a0v}, open(os.path.join(out, args.tag+'_summary.json'), 'w'), indent=1)
log('DONE')
