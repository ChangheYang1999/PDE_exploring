"""D1 fixture (SPEC v9.13 (b)): near_integer_radii from the (pending or frozen) assess860.py source, extracted by AST: at exactly c_l = 2 and 3 beta = 0 is recorded and
the radii are omitted; at 2(1+2^-40) the radii are 1048576.0000004768 and 1482910.400379605 (SPEC v9.9 sanity values); away from 2 and 3 the result is None.
Usage: test_assess860_d1.py <assess860.py path> <out.json>"""
import ast, json, sys, math, hashlib
from decimal import Decimal, localcontext
from fractions import Fraction
src = open(sys.argv[1]).read(); tree = ast.parse(src)
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'near_integer_radii')
ns = {'Fraction': Fraction, 'Decimal': Decimal, 'localcontext': localcontext, 'math': math}; exec(compile(ast.Module(body=[node], type_ignores=[]), sys.argv[1], 'exec'), ns)
f = ns['near_integer_radii']; res = {'cases': {}, 'source': sys.argv[1], 'source_sha256': hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest(), 'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}   # E10
r2 = f(2.0); r3 = f(3.0); r40 = f(2.*(1+2.**-40)); rfar = f(1.8089923602744993); r3n = f(3.*(1-2.**-21))
res['cases']['c2_beta_zero_radii_omitted'] = {'passed': r2 is not None and r2['beta_exact_rational'] == '0' and r2['r_d'] is None and r2['r_z'] is None and 'omitted' in r2['note'], 'value': r2}
res['cases']['c3_beta_zero_radii_omitted'] = {'passed': r3 is not None and r3['beta_exact_rational'] == '0' and r3['r_d'] is None and r3['r_z'] is None, 'value': r3}
res['cases']['c2_2m40_sanity'] = {'passed': r40 is not None and abs(r40['r_d']-1048576.0000004768) < 1e-6 and abs(r40['r_z']-1482910.400379605) < 1e-6 and r40['beta_exact_rational'] == '-1/1099511627777', 'value': r40}
res['cases']['seed_far_from_integers_none'] = {'passed': rfar is None, 'value': rfar}
res['cases']['c3_minus_2m21_finite'] = {'passed': r3n is not None and r3n['r_d'] is not None and math.isfinite(r3n['r_d']), 'value': r3n}
res['passed'] = all(c['passed'] for c in res['cases'].values()); json.dump(res, open(sys.argv[2], 'w'), indent=1, default=str)
for k, v in res['cases'].items(): print(k, 'PASS' if v['passed'] else 'FAIL', json.dumps(v['value'], default=str)[:120])
print('ALL PASSED' if res['passed'] else 'SOME FAILED')
