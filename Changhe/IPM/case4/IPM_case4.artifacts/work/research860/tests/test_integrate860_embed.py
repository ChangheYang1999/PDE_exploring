"""Independent whole-axis J_abs of the embedded accepted278 in the 860 representation vs the reference 4.2683726070948805e-09."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
import basis860 as B
from integrate860 import independent_integral, independent_fields, outer_envelope
from fields860 import residual, fields
from absolute_common import read, ROOT, A_REF
from absolute_fields import prepare_candidate
from absolute_fields_v2 import residual as old_residual, fields as old_fields
from field_tests import independent_fields as old_independent_fields
from tail_envelope import outer_envelope as old_outer_envelope
out = {'checks': []}
def check(name, value, tol=None, **extra):
    ok = bool(value <= tol) if tol is not None else bool(value)
    out['checks'].append({'check': name, 'value': value if tol is not None else bool(value), 'tolerance': tol, 'passed': ok, **extra}); print(name, value, 'PASS' if ok else 'FAIL', flush=True)
cand = read(ROOT/'campaign/global181_v3/snapshots/accepted_00000278.json'); prep = prepare_candidate(cand, 'center_chart')
c, g = B.embed_old(prep['coefficients'], prep['extra'], prep['modes']); P = np.r_[prep['p'][0], c[1:]]
new = B.prepare(P[0], P[1:], g)
# pointwise stateless fields/residual new vs old (direct region and origin series region), relative to local magnitude
rng = np.random.default_rng(11); r = np.r_[np.geomspace(1e-4, 1e12, 60), .02, .0200001, .0199999]; th = rng.uniform(0, np.pi/2, len(r)); x = r*np.cos(th); y = r*np.sin(th)
x = np.r_[x, 0., 3., 1e-3, 0.]; y = np.r_[y, 2., 0., 0., 1e-3]
fo = old_fields(prep, x, y); fn = fields(new, x, y); ro = old_residual(prep, x, y); rn = residual(new, x, y)
worst = {}
for k in fo: worst[k] = float(np.max(abs(fo[k]-fn[k])/np.maximum(abs(fo[k]), 1e-300*0+np.max(abs(fo[k]))*1e-12)))
out['field_pointwise_rel_worst'] = worst
check('fields_pointwise_rel_worst', max(worst.values()), 1e-9)
check('residual_pointwise_abs_vs_old_scaled', float(np.max(abs(ro-rn)/np.maximum(1., abs(ro)))), 1e-13)
# 85-digit independent point evaluations: new independent_fields vs old field_tests.independent_fields and vs stateless
for pt in [(.31, .27), (1e6, .3e6), (.015, .011), (3., 0.)]:
    a = independent_fields(new, *pt); b = old_independent_fields(prep, *pt); s = residual(new, [pt[0]], [pt[1]])[0]
    check('independent85_new_vs_old_Rf_%g_%g' % pt, abs(a['Rf']-b['Rf'])/max(1e-300, abs(b['Rf'])), 1e-9)
    check('stateless_vs_independent85_Rf_%g_%g' % pt, abs(s-a['Rf'])/max(1., abs(a['Rf'])), 2e-8)
# envelope comparison
for R in (math_R for math_R in (1e3, 1e19)):
    e_new = outer_envelope(new, R, A_REF)['integral_upper_bound']; e_old = old_outer_envelope(prep, R, A_REF)['integral_upper_bound']
    check('outer_envelope_rel_vs_old_R%g' % R, abs(e_new-e_old)/e_old, 1e-9, new=e_new, old=e_old)
t0 = time.time(); ii = independent_integral(P, g, workers=4, target_abs=1e-16); out['independent_integral_seconds'] = time.time()-t0
out['independent_integral'] = {k: ii[k] for k in ('J_abs', 'error_abs', 'origin_tail_error_abs', 'infinity_tail_error_abs', 'radial_quadrature_error_abs', 'angular_quadrature_error_abs', 'accuracy_passed')}
ref = 4.2683726070948805e-09
check('J_abs_vs_reference_abs', abs(ii['J_abs']-ref), 1e-18, J_abs=ii['J_abs'], reference=ref, error_abs=ii['error_abs'])
check('independent_accuracy_passed', ii['accuracy_passed'])
check('origin_overlap_passed', ii['origin_independent_overlap']['passed'], **ii['origin_independent_overlap'])
out['passed'] = all(r['passed'] for r in out['checks'])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str)+'\n'); print('ALL PASSED' if out['passed'] else 'SOME FAILED', flush=True)
