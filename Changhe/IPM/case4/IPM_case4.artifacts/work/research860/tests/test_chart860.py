"""Chart860 tests: embedded accepted278 is C5-feasible, constraint rank, tangent dimension 55, lift/retraction, agreement with old chart."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B, chart860 as C
from absolute_common import read, ROOT
from absolute_fields import prepare_candidate
from absolute_chart import hp_report as old_hp
from absolute_chart_v2 import AbsoluteC5ChartV2
out = {'checks': []}
def check(name, value, tol=None, **extra):
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL')
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); prep = prepare_candidate(cand, 'center_chart')
c, g = B.embed_old(prep['coefficients'], prep['extra'], prep['modes'])
P = np.r_[prep['p'][0], c[1:]]
t0 = time.time(); hp = C.hp_report(P); out['hp_seconds'] = time.time()-t0
ohp = old_hp(prep['p'])
check('embedded_c0_matches_old_analytic_c0', abs(float(hp['coefficients_decimal'][0])-prep['coefficients'][0]), 1e-15)
check('five_taylor_max_abs', hp['max_abs'], 1e-10, old=ohp['max_abs'])
check('five_taylor_match_old', max(abs(a-b) for a, b in zip(hp['constraints'], ohp['constraints'])), 1e-13)
check('a0_matches_old', abs(hp['a0']-ohp['a0']), 1e-12, a0=hp['a0'])
check('poisson_jets', hp['poisson_max_abs'], 1e-10); check('center_abs', hp['center_abs'], 1e-60)
# constraint jacobian: columns of generators with zero jets must be zero; rank 5
G = C.constraint_jacobian(P); out['constraint_jacobian_shape'] = list(G.shape)
check('constraint_rank_5', np.linalg.matrix_rank(G) == 5); out['constraint_singular_values'] = np.linalg.svd(G, compute_uv=False).tolist()
# compare with old chart constraint Jacobian on the 24 old directions (chain rule through embedding)
from absolute_chart import constraint_jacobian as old_cj
Gold = old_cj(prep['p'])          # 5 x 24 in old raw p = [cl, c1..c23]
E = np.zeros((60, 24)); E[0, 0] = 1.
for jold, (m, s) in enumerate(B.OLD_CORE_ORDER):
    if jold == 0: continue
    for kind, idx, f in B.old_core_to_internal(m, s):
        if kind == 'core': E[idx, jold] += f      # (3,2) has an extra part, which has zero jets
check('old_constraint_jacobian_reproduced_via_embedding', float(np.max(abs(G@E-Gold))/np.max(abs(Gold))), 1e-9)
t0 = time.time(); chart = C.Chart860(P); out['chart_seconds'] = time.time()-t0
gd = chart.geometry_diagnostics; out['geometry'] = {k: v for k, v in gd.items() if k != 'base_HP'}
check('tangent_rank_55', gd['tangent_rank'] == 55); check('complete_rank_60', gd['complete_rank'] == 60)
check('tangent_constraint_error', gd['tangent_constraint_error'], 1e-8); check('nonzero_constraint_columns_60', gd['nonzero_constraint_columns'] == 60)
# lift: random feasible step, verify constraints satisfied, cl preserved exactly; retraction derivative vs FD
rng = np.random.default_rng(3)
for k in range(3):
    q = rng.normal(size=55); q /= np.linalg.norm(q); q *= 1e-3
    t0 = time.time(); Pq = chart.lift_delta(q); dt = time.time()-t0
    rep = C.hp_report(Pq); check('lift%d_feasible' % k, rep['max_abs'], 1e-10, seconds=dt, iterations=len(chart.last_diagnostics['iterations']))
    check('lift%d_cl_bit_pattern_preserved' % k, float(Pq[0]).hex() == float((P+chart.free@q)[0]).hex())
    # tangent consistency: (lift(h q) - lift(-h q))/(2h) vs base_tangent @ q
    h = 1e-5; fd = (chart.lift_delta(h*q/np.linalg.norm(q))-chart.lift_delta(-h*q/np.linalg.norm(q)))/(2*h)
    an = chart.base_tangent@(q/np.linalg.norm(q))
    check('lift%d_tangent_fd_rel' % k, float(np.linalg.norm(fd-an)/np.linalg.norm(an)), 1e-6)
# old chart's 19 tangent directions lie in the new 55-dim tangent space (embedding of old feasible directions)
old_chart = AbsoluteC5ChartV2(prep['p']); Told = E@old_chart.base_tangent       # 60 x 19
proj = chart.base_tangent@np.linalg.lstsq(chart.base_tangent, Told, rcond=None)[0]
check('old_19_tangent_in_new_55_tangent', float(np.linalg.norm(proj-Told)/np.linalg.norm(Told)), 1e-9)
# exceptional cl audit: constraint rank and strain s_0 at several cl including near 2 and 3
rows = []
for cl in (1.1, 1.5, 1.8089923602744993, 1.999, 2.0, 2.5, 2.999, 3.0, 3.5, 6.0):
    M = B.jet_matrix(cl); Pc = P.copy(); Pc[0] = cl
    rows.append({'cl': cl, 's0': float(M[6, 0]), 'jet_matrix_rank': int(np.linalg.matrix_rank(M)), 'constraint_rank_at_embedded_coeffs': int(np.linalg.matrix_rank(C.constraint_jacobian(Pc)))})
out['exceptional_cl_scan'] = rows
out['passed'] = all(r['passed'] for r in out['checks'])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED')
