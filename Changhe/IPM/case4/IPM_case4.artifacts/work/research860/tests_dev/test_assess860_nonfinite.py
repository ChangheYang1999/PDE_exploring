"""E9 fixtures (lead fix check 3 and addendum 11:56Z; verifier nonfinite_producer): the assess860 helpers finite_max and origin_compare, extracted by AST from the source
and executed with their own globals: the verifier's five provider cases (near-origin NaN, near-origin Inf, large-r NaN, large-r Inf, origin NaN comparison) each count into
NONFINITE_SAMPLES (which enters completeness.failed: the source expression is checked) and NONFINITE_MONITOR, the reductions stay finite or null, and the origin stop
expression references the nonfinite list; a finite control counts nothing. Records source and script sha256 (E10). Usage: fixture_assess860_nonfinite.py <assess860.py> <out.json>"""
import ast, json, sys, math, hashlib
from pathlib import Path
import numpy as np
src_path = Path(sys.argv[1]).resolve(); src = src_path.read_text(); tree = ast.parse(src); out_json = Path(sys.argv[2]).resolve()
def pick(name):
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == name: return n
    raise KeyError(name)
NS = {'np': np, 'math': math, 'NONFINITE_SAMPLES': {'count': 0}, 'NONFINITE_MONITOR': []}
for fn in ('finite_max', 'origin_compare'): exec(compile(ast.Module(body=[pick(fn)], type_ignores=[]), str(src_path), 'exec'), NS)
finite_max = NS['finite_max']; origin_compare = NS['origin_compare']; S = NS['NONFINITE_SAMPLES']; M = NS['NONFINITE_MONITOR']
res = {'source': str(src_path), 'source_sha256': hashlib.sha256(src_path.read_bytes()).hexdigest(), 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': {}}
def record(name, ok, **info): res['cases'][name] = {'passed': bool(ok), **info}; print(name, 'PASS' if ok else 'FAIL', json.dumps(info, default=str)[:300], flush=True)
v = finite_max(np.array([1e-12, 3e-12, 2e-12]), 'near_origin.control'); record('finite_control_counts_nothing', v == 3e-12 and S['count'] == 0 and M == [], value=v)
v = finite_max(np.array([1e-12, float('nan'), 2e-12]), 'near_origin.E_f_max_r_lt_0p02'); record('near_origin_NaN_counted_max_over_finite', v == 2e-12 and S['count'] == 1 and M[-1]['where'] == 'near_origin.E_f_max_r_lt_0p02' and M[-1]['nonfinite_count'] == 1, value=v, count=S['count'])
v = finite_max(np.array([1e-12, float('inf')]), 'near_origin.E_rho_max_r_lt_0p02'); record('near_origin_Inf_counted', v == 1e-12 and S['count'] == 2, value=v)
v = finite_max(np.array([float('nan'), 5.]), 'direct_large_r.max_abs_Rrho.r=1000'); record('large_r_NaN_counted', v == 5. and S['count'] == 3 and M[-1]['where'].startswith('direct_large_r'), value=v)
v = finite_max(np.array([float('-inf'), float('inf')]), 'direct_large_r.max_abs_Rrho.r=10000'); record('large_r_Inf_only_gives_null_and_counts_both', v is None and S['count'] == 5, value=v)
rat, drat = origin_compare(np.array([1., float('nan')]), np.array([1., 1.]), np.array([2., 2.]), np.array([2., 2.]), ['low', [0, 1, 2]], 'f')
record('origin_NaN_comparison_counted_value_None_derivative_finite', rat is None and drat == 0. and S['count'] == 6 and M[-1] == {'where': 'origin_truncation_monitor', 'generator': ['low', [0, 1, 2]], 'key': 'f', 'nonfinite': ['value']}, rat=rat, drat=drat)
rat, drat = origin_compare(np.array([1., 1.]), np.array([1., 1.+1e-14]), np.array([2., 2.]), np.array([2., 2.]), ['high', [1, 2, 3]], 'psi')
record('origin_finite_comparison_unchanged_count', rat is not None and abs(rat-1e-14) < 1e-15 and drat == 0. and S['count'] == 6, rat=rat)
# the record contract: completeness.failed includes the nonfinite count and the origin monitor stop includes the nonfinite comparisons; worst only takes finite ratios
record('completeness_failed_includes_nonfinite_count', "NONFINITE_SAMPLES['count'] > 0" in src and "'nonfinite_monitor_inputs': NONFINITE_MONITOR" in src)
record('origin_monitor_stop_includes_nonfinite_comparisons', "'scientific_stop': bool(worst > 1e-12 or nonfinite_origin)" in src and "if r_ is not None and r_ > worst: worst = r_" in src)
record('near_origin_and_large_r_use_finite_max', src.count("finite_max(vo['E_f']") == 2 and src.count("finite_max(vo['E_rho']") == 2 and "finite_max(abs(rrho)" in src)
record('no_late_imports_remain', "    from origin860 import generator_polynomial" not in src and "from absolute_common import array_hash as _ah\nout = " not in src and "\nfrom origin860 import generator_polynomial\n" in src)
res['passed'] = all(c['passed'] for c in res['cases'].values()); out_json.write_text(json.dumps(res, indent=1, default=str)+'\n'); print('ALL PASSED' if res['passed'] else 'SOME FAILED')
