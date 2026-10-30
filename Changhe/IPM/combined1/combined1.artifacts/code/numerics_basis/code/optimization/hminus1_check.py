"""Hdot^-1 FLOAT check on a candidate: argv candidate_json ANG R  (uses exact sectors beyond R)"""
import sys, os; sys.path.insert(0, 'RUN_ROOT/numerics_N1N2/numerics/optimization')
from candA_setup import *
import ipm_opt2 as O2, ipm_hminus1 as HM, time
path = sys.argv[1]; ANG = int(sys.argv[2]); R = float(sys.argv[3])
dev = torch.device(os.environ.get('IPM_DEVICE', 'cpu'))
if 'nb_' in path:
    d2 = json.load(open(path)); c = X.Q(d2['cl']) if isinstance(d2['cl'], str) else X.Q(float(d2['cl']))
    gens = [{'m': g['m'], 'j': g['j'], 'spec': g['spec']} for g in d2['generators']]; coefs_q = [X.Q(g['coef']) for g in d2['generators']]
else:
    c, gens, coefs_q, _ = OPT.load_candidate_json(path)
coefs = np.array([X.qfloat(v) for v in coefs_q])
s, ws, bl = EV.whole_axis_radial(origin_order=48, middle_order=32); keep = (np.exp(s) >= 0.02) & (s <= math.log(R)+1e-9); s, ws = s[keep], ws[keep]
th, wth = EV.angular_midpoint(ANG); mesh = EV.Mesh(s, ws, th, wth, dev)
t0 = time.time(); prob = O2.Problem2(gens, c, mesh, r_cut=0.02, r_max=R); print('build', time.time()-t0, flush=True)
parts, comp, Fd = prob.objective_parts(coefs); F = comp[(0, 0)]
terms = X.generators_to_terms(c, [dict(g, coef=v) for g, v in zip(gens, coefs_q)])
t0 = time.time(); E, dens, strm, mom = X.residual_sectors(c, terms, 5, exp_min=X.mpq(-7)); print('sectors', time.time()-t0, flush=True)
t0 = time.time(); res = HM.hminus1(F, mesh, R, E); print('hminus1 time', time.time()-t0, flush=True)
print({k: v for k, v in res.items() if k != 'per_mode_sq'})
pm = res['per_mode_sq']; print('first modes sq:', {n: pm[n] for n in list(pm)[:6]})
print('n=1 contribution norm', math.sqrt(pm.get(1, 0)), '(c1-n4: 213.6349 for d2)')
