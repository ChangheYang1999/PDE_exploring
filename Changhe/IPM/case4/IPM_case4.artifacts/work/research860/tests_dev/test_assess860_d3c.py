"""D3-c fixture (lead 10:10Z / rulings 6, 10): leading_profile from the (pending or frozen) assess860.py source, extracted by AST. Cases: ordinary seed-like coefficients;
tiny (1e-170) and huge (1e160) finite coefficients (common scale keeps the profile finite); an unrepresentable (None) coefficient (no profile, note names the harmonic and
reason); a non-determined leading power (no profile, status in the note). Usage: test_assess860_d3c.py <assess860.py path> <out.json>"""
import ast, json, sys, math, hashlib
import numpy as np
src = open(sys.argv[1]).read(); tree = ast.parse(src)
SHA = {'source': sys.argv[1], 'source_sha256': hashlib.sha256(src.encode()).hexdigest(), 'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}   # E10: the result binds the source and the script
def pick(name):
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == name: return n
    raise KeyError(name)
ns = {'np': np, 'json': json, 'math': math}; exec(compile(ast.Module(body=[pick('leading_profile')], type_ignores=[]), sys.argv[1], 'exec'), ns); f = ns['leading_profile']
theta = np.linspace(0, np.pi/2, 513); res = {'cases': {}, **SHA}
def ff(coeffs, unrep=None, determined=True): return {'leading_sector_sine_coefficients_odd': coeffs, 'leading_sector_sine_coefficients_unrepresentable': unrep or {}, 'actual_leading_density_power': {'determined': determined, 'status': 'determined' if determined else 'candidate only: test'}}
p, sc, note = f(ff({'1': 0.3, '3': -0.05, '5': 0.01}), theta); res['cases']['ordinary'] = {'passed': p is not None and note is None and abs(sc-0.3) < 1e-15 and math.isfinite(float(np.linalg.norm(p))) and float(np.linalg.norm(p)) > 0, 'scale': sc, 'norm': float(np.linalg.norm(p)) if p is not None else None}
p, sc, note = f(ff({'1': 3e-170, '3': -5e-171}), theta); res['cases']['tiny_finite'] = {'passed': p is not None and note is None and math.isfinite(float(np.linalg.norm(p))) and float(np.linalg.norm(p)) > 0, 'scale': sc, 'norm': float(np.linalg.norm(p)) if p is not None else None}
p, sc, note = f(ff({'1': 3e160, '3': -5e159}), theta); res['cases']['huge_finite'] = {'passed': p is not None and note is None and math.isfinite(float(np.linalg.norm(p))) and float(np.linalg.norm(p)) > 0, 'scale': sc, 'norm': float(np.linalg.norm(p)) if p is not None else None}
p, sc, note = f(ff({'1': 0.3, '3': None}, {'3': {'reason': 'underflow: nonzero exact value rounds to 0 in binary64', 'decimal': '1e-400'}}), theta); res['cases']['unrepresentable_coefficient'] = {'passed': p is None and sc is None and note is not None and '"3"' in note and 'underflow' in note, 'note': note}
p, sc, note = f(ff({'1': 0.3}, determined=False), theta); res['cases']['not_determined'] = {'passed': p is None and note is not None and note.startswith('no determined leading sector'), 'note': note}
res['passed'] = all(c['passed'] for c in res['cases'].values()); json.dump(res, open(sys.argv[2], 'w'), indent=1, default=str)
for k, v in res['cases'].items(): print(k, 'PASS' if v['passed'] else 'FAIL', json.dumps({kk: vv for kk, vv in v.items() if kk != 'passed'}, default=str)[:140])
print('ALL PASSED' if res['passed'] else 'SOME FAILED')
